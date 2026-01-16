"""CLI for strict-syntax-health."""

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx
import plotly.graph_objects as go
import rich_click as click
from rich.console import Console
from rich.table import Table

# API URLs
PIPELINES_URL = "https://nf-co.re/pipelines.json"
MODULES_REPO_URL = "https://github.com/nf-core/modules.git"

# Directory paths
PIPELINES_DIR = Path("pipelines")
MODULES_DIR = Path("modules")
LINT_RESULTS_DIR = Path("lint_results")

# Pipelines.json now lives inside pipelines/
PIPELINES_JSON_PATH = PIPELINES_DIR / "pipelines.json"

# README path
README_PATH = Path("README.md")

# Lint results subdirectories (named to avoid gitignore patterns matching "pipelines/" and "modules/")
PIPELINES_LINT_RESULTS_DIR = LINT_RESULTS_DIR / "pipeline-results"
MODULES_LINT_RESULTS_DIR = LINT_RESULTS_DIR / "module-results"
SUBWORKFLOWS_LINT_RESULTS_DIR = LINT_RESULTS_DIR / "subworkflow-results"

console = Console()


# ============================================================================
# Git commit hash utilities for caching
# ============================================================================


def get_remote_commit_hash(repo_url: str, branch: str = "HEAD") -> str | None:
    """Get the latest commit hash from a remote repository without cloning.

    Uses `git ls-remote` which only queries the remote server - no download needed.
    This is the key optimization for skipping unchanged repos.

    Args:
        repo_url: The URL of the git repository
        branch: The branch/ref to check (default: HEAD). Use "refs/heads/dev" for dev branch.

    Returns:
        The commit hash string, or None if the query fails.
    """
    try:
        result = subprocess.run(
            ["git", "ls-remote", repo_url, branch],
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )
        if result.stdout:
            return result.stdout.split()[0]
        return None
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None


def get_local_commit_hash(repo_path: Path) -> str:
    """Get the current HEAD commit hash of a cloned repository.

    Args:
        repo_path: Path to the cloned git repository.

    Returns:
        The commit hash string.
    """
    result = subprocess.run(
        ["git", "-C", str(repo_path), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


# ============================================================================
# Result sorting and utilities
# ============================================================================


def _sort_results(results: list[dict]) -> list[dict]:
    """Sort results by parse_error first, then errors (descending), then warnings (descending)."""
    return sorted(results, key=lambda x: (not x.get("parse_error", False), -x["errors"], -x["warnings"]))


def update_pipelines_json() -> None:
    """Download the latest pipelines.json from nf-co.re."""
    console.print(f"Downloading {PIPELINES_URL}...")
    PIPELINES_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    response = httpx.get(PIPELINES_URL, timeout=60)
    response.raise_for_status()
    PIPELINES_JSON_PATH.write_bytes(response.content)
    console.print(f"Updated {PIPELINES_JSON_PATH}")


def load_pipelines() -> list[dict]:
    """Load pipelines from the local pipelines.json file."""
    if not PIPELINES_JSON_PATH.exists():
        console.print(f"[red]{PIPELINES_JSON_PATH} not found. Run with --update-pipelines first.[/red]")
        sys.exit(1)

    console.print(f"Loading pipelines from {PIPELINES_JSON_PATH}...")
    data = json.loads(PIPELINES_JSON_PATH.read_text())

    pipelines = []
    for pipeline in data.get("remote_workflows", []):
        if pipeline.get("archived", False):
            continue
        pipelines.append(
            {
                "name": pipeline["name"],
                "full_name": pipeline["full_name"],
                "html_url": f"https://github.com/{pipeline['full_name']}",
            }
        )

    console.print(f"Found {len(pipelines)} active pipelines")
    return pipelines


def check_modules_repo_unchanged(
    no_cache: bool = False, check_modules: bool = True, check_subworkflows: bool = True
) -> tuple[bool, str | None]:
    """Check if the nf-core/modules repo is unchanged from cache (without cloning).

    Args:
        no_cache: If True, always return False (treat as changed)
        check_modules: Whether to check the modules cache
        check_subworkflows: Whether to check the subworkflows cache

    Returns:
        Tuple of (is_unchanged, remote_commit_hash)
        - is_unchanged: True if repo hasn't changed and we can use cached results
        - remote_commit_hash: The remote commit hash (for updating cache later)
    """
    if no_cache:
        return False, None

    # Get remote commit hash WITHOUT cloning
    remote_commit = get_remote_commit_hash(MODULES_REPO_URL, "refs/heads/master")
    if remote_commit is None:
        return False, None

    # Check caches for the types being linted
    cache_matches = True

    if check_modules:
        modules_cache = load_results_dict_for_type("modules")
        modules_repo_commit = modules_cache.get("_repo_commit")
        if modules_repo_commit != remote_commit:
            cache_matches = False

    if check_subworkflows:
        subworkflows_cache = load_results_dict_for_type("subworkflows")
        subworkflows_repo_commit = subworkflows_cache.get("_repo_commit")
        if subworkflows_repo_commit != remote_commit:
            cache_matches = False

    return cache_matches, remote_commit


def clone_modules_repo() -> str:
    """Clone or update the nf-core/modules repository.

    Returns:
        The current commit hash of the cloned/updated repository.
    """
    if MODULES_DIR.exists():
        console.print("Updating nf-core/modules repository...")
        subprocess.run(
            ["git", "-C", str(MODULES_DIR), "fetch", "--quiet", "origin", "master"],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "-C", str(MODULES_DIR), "checkout", "--quiet", "master"],
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "-C", str(MODULES_DIR), "pull", "--quiet"],
            check=True,
            capture_output=True,
        )
    else:
        console.print("Cloning nf-core/modules repository...")
        subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", MODULES_REPO_URL, str(MODULES_DIR)],
            check=True,
            capture_output=True,
        )

    commit_hash = get_local_commit_hash(MODULES_DIR)
    console.print(f"nf-core/modules repository ready at {MODULES_DIR} ({commit_hash[:8]})")
    return commit_hash


def discover_modules() -> list[dict]:
    """Discover all modules in the nf-core/modules repository."""
    modules_path = MODULES_DIR / "modules" / "nf-core"
    if not modules_path.exists():
        console.print(f"[red]Modules path not found: {modules_path}[/red]")
        return []

    modules = []
    # Walk through tool directories
    for tool_dir in sorted(modules_path.iterdir()):
        if not tool_dir.is_dir() or tool_dir.name.startswith("."):
            continue
        # Walk through subcommand directories
        for subcommand_dir in sorted(tool_dir.iterdir()):
            if not subcommand_dir.is_dir() or subcommand_dir.name.startswith("."):
                continue
            main_nf = subcommand_dir / "main.nf"
            if main_nf.exists():
                # Module name is tool_subcommand (e.g., bwa_mem)
                name = f"{tool_dir.name}_{subcommand_dir.name}"
                modules.append(
                    {
                        "name": name,
                        "path": subcommand_dir,
                        "html_url": (
                            f"https://github.com/nf-core/modules/tree/master/modules/nf-core/"
                            f"{tool_dir.name}/{subcommand_dir.name}"
                        ),
                    }
                )

    console.print(f"Found {len(modules)} modules")
    return modules


def discover_subworkflows() -> list[dict]:
    """Discover all subworkflows in the nf-core/modules repository."""
    subworkflows_path = MODULES_DIR / "subworkflows" / "nf-core"
    if not subworkflows_path.exists():
        console.print(f"[red]Subworkflows path not found: {subworkflows_path}[/red]")
        return []

    subworkflows = []
    for subworkflow_dir in sorted(subworkflows_path.iterdir()):
        if not subworkflow_dir.is_dir() or subworkflow_dir.name.startswith("."):
            continue
        main_nf = subworkflow_dir / "main.nf"
        if main_nf.exists():
            subworkflows.append(
                {
                    "name": subworkflow_dir.name,
                    "path": subworkflow_dir,
                    "html_url": (
                        f"https://github.com/nf-core/modules/tree/master/subworkflows/nf-core/{subworkflow_dir.name}"
                    ),
                }
            )

    console.print(f"Found {len(subworkflows)} subworkflows")
    return subworkflows


def clone_pipeline(pipeline: dict) -> Path:
    """Clone a pipeline repository, preferring the 'dev' branch."""
    repo_path = PIPELINES_DIR / pipeline["name"]

    if repo_path.exists():
        console.print(f"  Pipeline already cloned: {pipeline['name']}")
        # Try to checkout dev branch, fall back to default if it doesn't exist
        try:
            subprocess.run(
                ["git", "-C", str(repo_path), "fetch", "--quiet", "origin", "dev"],
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "-C", str(repo_path), "checkout", "--quiet", "dev"],
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError:
            # dev branch doesn't exist, stay on current branch
            pass
        # Pull latest changes
        subprocess.run(
            ["git", "-C", str(repo_path), "pull", "--quiet"],
            check=True,
            capture_output=True,
        )
    else:
        console.print(f"  Cloning {pipeline['full_name']}...")
        PIPELINES_DIR.mkdir(parents=True, exist_ok=True)
        # Try to clone dev branch first
        try:
            subprocess.run(
                ["git", "clone", "--quiet", "--depth", "1", "--branch", "dev", pipeline["html_url"], str(repo_path)],
                check=True,
                capture_output=True,
            )
        except subprocess.CalledProcessError:
            # dev branch doesn't exist, clone default branch
            subprocess.run(
                ["git", "clone", "--quiet", "--depth", "1", pipeline["html_url"], str(repo_path)],
                check=True,
                capture_output=True,
            )

    return repo_path


def get_nextflow_version() -> str:
    """Get the current nextflow version."""
    result = subprocess.run(
        ["nextflow", "-version"],
        capture_output=True,
        text=True,
    )
    # Parse version from output like "nextflow version 24.10.0.5928"
    for line in result.stdout.split("\n"):
        if "version" in line.lower():
            parts = line.split()
            for i, part in enumerate(parts):
                if part.lower() == "version" and i + 1 < len(parts):
                    return parts[i + 1]
    return "unknown"


def lint_component(repo_path: Path, target_path: Path | None = None) -> dict:
    """Run nextflow lint on a component (JSON output for parsing).

    Args:
        repo_path: The repository root path (used as cwd)
        target_path: Optional specific path to lint (relative to repo_path or absolute)
    """
    if target_path:
        # Make path relative to repo_path if it's absolute or inside repo_path
        try:
            relative_path = target_path.relative_to(repo_path)
        except ValueError:
            relative_path = target_path
        cmd = ["nextflow", "lint", str(relative_path), "-o", "json"]
    else:
        cmd = ["nextflow", "lint", ".", "-o", "json"]

    result = subprocess.run(
        cmd,
        cwd=repo_path,
        capture_output=True,
        text=True,
    )

    # nextflow lint returns non-zero exit code if there are errors
    # but we still want to parse the output
    try:
        lint_result = json.loads(result.stdout)
        lint_result["parse_error"] = False
        return lint_result
    except json.JSONDecodeError:
        name = target_path.name if target_path else repo_path.name
        console.print(f"[red]Failed to parse lint output for {name}[/red]")
        console.print(f"stdout: {result.stdout}")
        console.print(f"stderr: {result.stderr}")
        return {"summary": {"errors": 0}, "errors": [], "warnings": [], "parse_error": True}


def lint_directory_bulk(repo_path: Path, target_path: Path) -> dict:
    """Run nextflow lint on a directory containing multiple components (JSON output).

    This runs lint once on the entire directory and returns all results,
    which is much faster than running lint on each component individually.

    Args:
        repo_path: The repository root path (used as cwd)
        target_path: The directory to lint (e.g., modules/nf-core or subworkflows/nf-core)
    """
    try:
        relative_path = target_path.relative_to(repo_path)
    except ValueError:
        relative_path = target_path

    cmd = ["nextflow", "lint", str(relative_path), "-o", "json"]

    result = subprocess.run(
        cmd,
        cwd=repo_path,
        capture_output=True,
        text=True,
    )

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        console.print(f"[red]Failed to parse bulk lint output for {target_path}[/red]")
        console.print(f"stdout: {result.stdout[:500]}...")
        console.print(f"stderr: {result.stderr}")
        return {"errors": [], "warnings": []}


def _extract_component_name_from_path(filepath: str, component_type: str) -> str | None:
    """Extract component name from a file path.

    Args:
        filepath: Path like 'modules/nf-core/bwa/mem/main.nf' or 'subworkflows/nf-core/foo/main.nf'
        component_type: Either 'modules' or 'subworkflows'

    Returns:
        Component name like 'bwa_mem' for modules or 'foo' for subworkflows, or None if not matched
    """
    parts = Path(filepath).parts

    # Find the nf-core part and extract the component name
    try:
        nf_core_idx = parts.index("nf-core")
    except ValueError:
        return None

    if component_type == "modules":
        # modules/nf-core/tool/subcommand/main.nf -> tool_subcommand
        if len(parts) > nf_core_idx + 2:
            return f"{parts[nf_core_idx + 1]}_{parts[nf_core_idx + 2]}"
    else:
        # subworkflows/nf-core/name/main.nf -> name
        if len(parts) > nf_core_idx + 1:
            return parts[nf_core_idx + 1]

    return None


def _group_lint_results_by_component(
    lint_result: dict,
    component_type: str,
) -> dict[str, dict]:
    """Group lint errors and warnings by component name.

    Args:
        lint_result: The JSON output from nextflow lint
        component_type: Either 'modules' or 'subworkflows'

    Returns:
        Dict mapping component name to {"errors": [...], "warnings": [...]}
    """
    grouped: dict[str, dict] = {}

    for error in lint_result.get("errors", []):
        filename = error.get("filename", "")
        name = _extract_component_name_from_path(filename, component_type)
        if name:
            if name not in grouped:
                grouped[name] = {"errors": [], "warnings": []}
            grouped[name]["errors"].append(error)

    for warning in lint_result.get("warnings", []):
        filename = warning.get("filename", "")
        name = _extract_component_name_from_path(filename, component_type)
        if name:
            if name not in grouped:
                grouped[name] = {"errors": [], "warnings": []}
            grouped[name]["warnings"].append(warning)

    return grouped


def _get_code_snippet(repo_path: Path, filename: str, line_num: int, column: int) -> str | None:
    """Read a code snippet from a file for display in markdown.

    Args:
        repo_path: Base repository path
        filename: Relative path to the file
        line_num: Line number (1-indexed)
        column: Column number (1-indexed)

    Returns:
        Formatted code snippet with caret marker, or None if file not found
    """
    try:
        file_path = repo_path / filename
        if not file_path.exists():
            return None

        source_lines = file_path.read_text().splitlines()
        if line_num < 1 or line_num > len(source_lines):
            return None

        source_line = source_lines[line_num - 1]
        # Create caret marker line pointing to the column
        # Account for the column being 1-indexed
        caret_line = " " * (column - 1) + "^" * max(1, min(10, len(source_line) - column + 1))

        return f"    ```nextflow\n    {source_line}\n    {caret_line}\n    ```"
    except Exception:
        return None


def _generate_markdown_from_issues(
    errors: list[dict],
    warnings: list[dict],
    nextflow_version: str,
    repo_path: Path | None = None,
) -> str:
    """Generate markdown output matching nextflow lint markdown format.

    Args:
        errors: List of error dicts with filename, startLine, startColumn, message
        warnings: List of warning dicts with same structure
        nextflow_version: Nextflow version string
        repo_path: Optional repository path for reading source code snippets

    Returns:
        Markdown string matching nextflow lint output format
    """
    now = datetime.now(timezone.utc).isoformat()
    error_count = len(errors)
    warning_count = len(warnings)

    lines = [
        "# Nextflow lint results",
        "",
        f"- Generated: {now}",
        f"- Nextflow version: {nextflow_version}",
    ]

    if error_count == 0 and warning_count == 0:
        lines.append("- Summary: No issues found")
        return "\n".join(lines)

    summary_parts = []
    if error_count > 0:
        summary_parts.append(f"{error_count} error{'s' if error_count != 1 else ''}")
    if warning_count > 0:
        summary_parts.append(f"{warning_count} warning{'s' if warning_count != 1 else ''}")
    lines.append(f"- Summary: {', '.join(summary_parts)}")

    if errors:
        lines.extend(["", "## :x: Errors", ""])
        for error in errors:
            filename = error.get("filename", "unknown")
            line_num = error.get("startLine", 0)
            col = error.get("startColumn", 0)
            message = error.get("message", "")
            lines.append(f"- Error: `{filename}:{line_num}:{col}`: {message}")
            lines.append("")
            if repo_path:
                snippet = _get_code_snippet(repo_path, filename, line_num, col)
                if snippet:
                    lines.append(snippet)
                    lines.append("")

    if warnings:
        lines.extend(["", "## :warning: Warnings", ""])
        for warning in warnings:
            filename = warning.get("filename", "unknown")
            line_num = warning.get("startLine", 0)
            col = warning.get("startColumn", 0)
            message = warning.get("message", "")
            lines.append(f"- Warning: `{filename}:{line_num}:{col}`: {message}")
            lines.append("")
            if repo_path:
                snippet = _get_code_snippet(repo_path, filename, line_num, col)
                if snippet:
                    lines.append(snippet)
                    lines.append("")

    return "\n".join(lines)


def lint_pipeline(repo_path: Path) -> dict:
    """Run nextflow lint on a pipeline (JSON output for parsing)."""
    return lint_component(repo_path)


def lint_component_markdown(repo_path: Path, name: str, output_dir: Path, target_path: Path | None = None) -> None:
    """Run nextflow lint on a component and save markdown output to file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{name}_lint.md"

    # Build command - if target_path specified, lint that specific path
    if target_path:
        # Make path relative to repo_path if it's absolute or inside repo_path
        try:
            relative_path = target_path.relative_to(repo_path)
        except ValueError:
            relative_path = target_path
        cmd = ["nextflow", "lint", str(relative_path), "-o", "markdown"]
    else:
        cmd = ["nextflow", "lint", ".", "-o", "markdown"]

    result = subprocess.run(
        cmd,
        cwd=repo_path,
        capture_output=True,
        text=True,
    )

    # Combine stdout and stderr for full output
    output = result.stdout
    if result.stderr:
        output += "\n" + result.stderr

    output_file.write_text(output)
    console.print(f"  Saved lint output to {output_file}")


def run_pipeline_lint(pipelines: list[dict], no_cache: bool = False) -> list[dict]:
    """Clone and lint all pipelines, using commit cache to skip unchanged repos.

    Args:
        pipelines: List of pipeline dicts with name, full_name, html_url
        no_cache: If True, ignore cache and re-lint everything
    """
    commits_cache = load_results_dict_for_type("pipelines")
    results = []
    skipped_count = 0
    linted_count = 0

    for pipeline in pipelines:
        name = pipeline["name"]
        cached = commits_cache.get(name)

        # BEFORE cloning: check if we can skip by comparing remote commit hash
        if not no_cache and cached:
            # Try dev branch first, then HEAD (default branch)
            remote_commit = get_remote_commit_hash(pipeline["html_url"], "refs/heads/dev")
            if remote_commit is None:
                remote_commit = get_remote_commit_hash(pipeline["html_url"], "HEAD")

            if remote_commit and remote_commit == cached.get("commit"):
                console.print(f"[dim]Skipping {name} (unchanged at {remote_commit[:8]})[/dim]")
                results.append(
                    {
                        "name": name,
                        "full_name": pipeline["full_name"],
                        "html_url": pipeline["html_url"],
                        "commit": remote_commit,
                        "errors": cached["errors"],
                        "warnings": cached["warnings"],
                        "parse_error": cached.get("parse_error", False),
                        "lint_details": {},  # Don't store full details in cache
                    }
                )
                skipped_count += 1
                continue

        # Cache miss or commit changed - need to clone and lint
        console.print(f"Processing pipeline {name}...")

        try:
            repo_path = clone_pipeline(pipeline)
            commit_hash = get_local_commit_hash(repo_path)
            lint_result = lint_pipeline(repo_path)
            lint_component_markdown(repo_path, name, PIPELINES_LINT_RESULTS_DIR)

            error_count = lint_result.get("summary", {}).get("errors", 0)
            warning_count = len(lint_result.get("warnings", []))
            parse_error = lint_result.get("parse_error", False)

            results.append(
                {
                    "name": name,
                    "full_name": pipeline["full_name"],
                    "html_url": pipeline["html_url"],
                    "commit": commit_hash,
                    "errors": error_count,
                    "warnings": warning_count,
                    "parse_error": parse_error,
                    "lint_details": lint_result,
                }
            )
            linted_count += 1

        except subprocess.CalledProcessError as e:
            console.print(f"[red]Failed to process {name}: {e}[/red]")
            results.append(
                {
                    "name": name,
                    "full_name": pipeline["full_name"],
                    "html_url": pipeline["html_url"],
                    "errors": 0,
                    "warnings": 0,
                    "parse_error": True,
                    "lint_details": {},
                }
            )
            linted_count += 1

    if skipped_count > 0:
        console.print(f"[green]Skipped {skipped_count} unchanged pipelines, linted {linted_count}[/green]")

    return results


def run_modules_lint(modules: list[dict], nextflow_version: str = "unknown") -> list[dict]:
    """Lint all modules using bulk lint for efficiency.

    Args:
        modules: List of module dicts with name, path, html_url
        nextflow_version: Nextflow version string for markdown output
    """
    # Check if we're filtering to specific modules (small list)
    # If so, use individual linting for accuracy; otherwise use bulk
    if len(modules) <= 5:
        results = _run_modules_lint_individual(modules, nextflow_version)
    else:
        results = _run_modules_lint_bulk(modules, nextflow_version)

    return results


def load_cached_modules_results(modules: list[dict]) -> list[dict]:
    """Load cached lint results for modules when repo is unchanged.

    Args:
        modules: List of module dicts with name, path, html_url

    Returns:
        List of result dicts with cached error/warning counts
    """
    results_cache = load_results_dict_for_type("modules")
    results = []

    for module in modules:
        name = module["name"]
        cached = results_cache.get(name, {})
        results.append(
            {
                "name": name,
                "html_url": module["html_url"],
                "errors": cached.get("errors", 0),
                "warnings": cached.get("warnings", 0),
                "parse_error": cached.get("parse_error", False),
                "lint_details": {},
            }
        )

    return results


def _run_modules_lint_individual(modules: list[dict], nextflow_version: str) -> list[dict]:
    """Lint modules individually (used when filtering to specific modules)."""
    results = []

    for module in modules:
        console.print(f"Processing module {module['name']}...")

        try:
            lint_result = lint_component(MODULES_DIR, module["path"])
            lint_component_markdown(MODULES_DIR, module["name"], MODULES_LINT_RESULTS_DIR, module["path"])

            results.append(
                {
                    "name": module["name"],
                    "html_url": module["html_url"],
                    "errors": lint_result.get("summary", {}).get("errors", 0),
                    "warnings": len(lint_result.get("warnings", [])),
                    "parse_error": lint_result.get("parse_error", False),
                    "lint_details": lint_result,
                }
            )
        except subprocess.CalledProcessError as e:
            console.print(f"[red]Failed to process module {module['name']}: {e}[/red]")
            results.append(
                {
                    "name": module["name"],
                    "html_url": module["html_url"],
                    "errors": 0,
                    "warnings": 0,
                    "parse_error": True,
                    "lint_details": {},
                }
            )

    return results


def _run_modules_lint_bulk(modules: list[dict], nextflow_version: str) -> list[dict]:
    """Lint all modules at once using bulk lint (much faster)."""
    console.print(f"Running bulk lint on {len(modules)} modules...")

    # Run lint once on the entire modules/nf-core directory
    modules_path = MODULES_DIR / "modules" / "nf-core"
    bulk_result = lint_directory_bulk(MODULES_DIR, modules_path)

    # Group results by component name
    grouped = _group_lint_results_by_component(bulk_result, "modules")

    # Generate results and markdown files for each module
    results = []
    MODULES_LINT_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    for module in modules:
        name = module["name"]
        component_issues = grouped.get(name, {"errors": [], "warnings": []})
        errors = component_issues["errors"]
        warnings = component_issues["warnings"]

        # Generate markdown file
        markdown_content = _generate_markdown_from_issues(errors, warnings, nextflow_version, MODULES_DIR)
        output_file = MODULES_LINT_RESULTS_DIR / f"{name}_lint.md"
        output_file.write_text(markdown_content)

        results.append(
            {
                "name": name,
                "html_url": module["html_url"],
                "errors": len(errors),
                "warnings": len(warnings),
                "parse_error": False,
                "lint_details": {"errors": errors, "warnings": warnings},
            }
        )

    console.print(f"Generated {len(results)} module lint reports")
    return results


def run_subworkflows_lint(subworkflows: list[dict], nextflow_version: str = "unknown") -> list[dict]:
    """Lint all subworkflows using bulk lint for efficiency.

    Args:
        subworkflows: List of subworkflow dicts with name, path, html_url
        nextflow_version: Nextflow version string for markdown output
    """
    # Check if we're filtering to specific subworkflows (small list)
    # If so, use individual linting for accuracy; otherwise use bulk
    if len(subworkflows) <= 5:
        results = _run_subworkflows_lint_individual(subworkflows, nextflow_version)
    else:
        results = _run_subworkflows_lint_bulk(subworkflows, nextflow_version)

    return results


def load_cached_subworkflows_results(subworkflows: list[dict]) -> list[dict]:
    """Load cached lint results for subworkflows when repo is unchanged.

    Args:
        subworkflows: List of subworkflow dicts with name, path, html_url

    Returns:
        List of result dicts with cached error/warning counts
    """
    results_cache = load_results_dict_for_type("subworkflows")
    results = []

    for subworkflow in subworkflows:
        name = subworkflow["name"]
        cached = results_cache.get(name, {})
        results.append(
            {
                "name": name,
                "html_url": subworkflow["html_url"],
                "errors": cached.get("errors", 0),
                "warnings": cached.get("warnings", 0),
                "parse_error": cached.get("parse_error", False),
                "lint_details": {},
            }
        )

    return results


def _run_subworkflows_lint_individual(subworkflows: list[dict], nextflow_version: str) -> list[dict]:
    """Lint subworkflows individually (used when filtering to specific subworkflows)."""
    results = []

    for subworkflow in subworkflows:
        console.print(f"Processing subworkflow {subworkflow['name']}...")

        try:
            lint_result = lint_component(MODULES_DIR, subworkflow["path"])
            lint_component_markdown(
                MODULES_DIR, subworkflow["name"], SUBWORKFLOWS_LINT_RESULTS_DIR, subworkflow["path"]
            )

            results.append(
                {
                    "name": subworkflow["name"],
                    "html_url": subworkflow["html_url"],
                    "errors": lint_result.get("summary", {}).get("errors", 0),
                    "warnings": len(lint_result.get("warnings", [])),
                    "parse_error": lint_result.get("parse_error", False),
                    "lint_details": lint_result,
                }
            )
        except subprocess.CalledProcessError as e:
            console.print(f"[red]Failed to process subworkflow {subworkflow['name']}: {e}[/red]")
            results.append(
                {
                    "name": subworkflow["name"],
                    "html_url": subworkflow["html_url"],
                    "errors": 0,
                    "warnings": 0,
                    "parse_error": True,
                    "lint_details": {},
                }
            )

    return results


def _run_subworkflows_lint_bulk(subworkflows: list[dict], nextflow_version: str) -> list[dict]:
    """Lint all subworkflows at once using bulk lint (much faster)."""
    console.print(f"Running bulk lint on {len(subworkflows)} subworkflows...")

    # Run lint once on the entire subworkflows/nf-core directory
    subworkflows_path = MODULES_DIR / "subworkflows" / "nf-core"
    bulk_result = lint_directory_bulk(MODULES_DIR, subworkflows_path)

    # Group results by component name
    grouped = _group_lint_results_by_component(bulk_result, "subworkflows")

    # Generate results and markdown files for each subworkflow
    results = []
    SUBWORKFLOWS_LINT_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    for subworkflow in subworkflows:
        name = subworkflow["name"]
        component_issues = grouped.get(name, {"errors": [], "warnings": []})
        errors = component_issues["errors"]
        warnings = component_issues["warnings"]

        # Generate markdown file
        markdown_content = _generate_markdown_from_issues(errors, warnings, nextflow_version, MODULES_DIR)
        output_file = SUBWORKFLOWS_LINT_RESULTS_DIR / f"{name}_lint.md"
        output_file.write_text(markdown_content)

        results.append(
            {
                "name": name,
                "html_url": subworkflow["html_url"],
                "errors": len(errors),
                "warnings": len(warnings),
                "parse_error": False,
                "lint_details": {"errors": errors, "warnings": warnings},
            }
        )

    console.print(f"Generated {len(results)} subworkflow lint reports")
    return results


def display_results(results: list[dict], title: str = "nf-core Strict Syntax Health") -> None:
    """Display results in a rich table."""
    table = Table(title=title)
    table.add_column("Pipeline", style="cyan")
    table.add_column("Parse Error", justify="right")
    table.add_column("Errors", justify="right")
    table.add_column("Warnings", justify="right")

    sorted_results = _sort_results(results)

    total_errors = 0
    total_warnings = 0
    total_parse_errors = 0

    for result in sorted_results:
        errors = result["errors"]
        warnings = result["warnings"]
        parse_error = result.get("parse_error", False)

        if parse_error:
            total_parse_errors += 1
            parse_error_str = "[red]Yes[/red]"
            error_str = "-"
            warning_str = "-"
        else:
            total_errors += errors
            total_warnings += warnings
            parse_error_str = "[green]No[/green]"
            error_str = f"[red]{errors}[/red]" if errors > 0 else "[green]0[/green]"
            warning_str = f"[yellow]{warnings}[/yellow]" if warnings > 0 else "[green]0[/green]"

        table.add_row(result["name"], parse_error_str, error_str, warning_str)

    console.print(table)
    console.print(
        f"\n[bold]Total: {total_parse_errors} parse errors, {total_errors} errors, {total_warnings} warnings[/bold]"
    )


def _get_type_dir(type_name: str) -> Path:
    """Get the lint results directory for a specific type."""
    type_dirs = {
        "pipelines": PIPELINES_LINT_RESULTS_DIR,
        "modules": MODULES_LINT_RESULTS_DIR,
        "subworkflows": SUBWORKFLOWS_LINT_RESULTS_DIR,
    }
    return type_dirs[type_name]


def _get_history_path_for_type(type_name: str) -> Path:
    """Get the history file path for a specific type (stored in lint_results/ root)."""
    return LINT_RESULTS_DIR / f"{type_name}_history.json"


def _get_results_path_for_type(type_name: str) -> Path:
    """Get the results file path for a specific type (stored in lint_results/ root)."""
    return LINT_RESULTS_DIR / f"{type_name}_results.json"


def save_results_for_type(type_name: str, results: list[dict], repo_commit: str | None = None) -> None:
    """Save lint results for a specific type (includes commit cache data).

    Results are stored as a dict keyed by component name for efficient lookup.
    Each entry contains: commit, errors, warnings, parse_error, full_name/html_url.

    Args:
        type_name: One of "pipelines", "modules", "subworkflows"
        results: List of result dicts from linting
        repo_commit: For modules/subworkflows, the shared repo commit hash
    """
    path = _get_results_path_for_type(type_name)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Convert list to dict keyed by name, stripping lint_details
    results_dict = {}

    # For modules/subworkflows, store the shared repo commit
    if repo_commit:
        results_dict["_repo_commit"] = repo_commit

    for r in results:
        name = r["name"]
        entry = {k: v for k, v in r.items() if k not in ("lint_details", "name")}
        results_dict[name] = entry

    path.write_text(json.dumps(results_dict, indent=2) + "\n")
    console.print(f"Saved results to {path}")


def load_results_for_type(type_name: str) -> list[dict]:
    """Load lint results for a specific type as a list.

    Converts the dict format back to a list for compatibility with existing code.
    """
    results_dict = load_results_dict_for_type(type_name)
    results = []
    for name, data in results_dict.items():
        if name.startswith("_"):  # Skip metadata keys like _repo_commit
            continue
        entry = {"name": name, **data}
        results.append(entry)
    return results


def load_results_dict_for_type(type_name: str) -> dict:
    """Load lint results for a specific type as a dict (for cache lookups).

    Returns dict keyed by component name with commit, errors, warnings, parse_error, etc.
    """
    path = _get_results_path_for_type(type_name)
    if path.exists():
        try:
            data = json.loads(path.read_text())
            # Handle both old list format and new dict format
            if isinstance(data, list):
                # Convert old list format to dict
                return {r["name"]: {k: v for k, v in r.items() if k != "name"} for r in data}
            return data
        except json.JSONDecodeError:
            return {}
    return {}


def load_history_for_type(type_name: str) -> list[dict]:
    """Load historical results for a specific type."""
    path = _get_history_path_for_type(type_name)
    if path.exists():
        return json.loads(path.read_text())
    return []


def save_history_for_type(type_name: str, history: list[dict]) -> None:
    """Save historical results for a specific type."""
    path = _get_history_path_for_type(type_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(history, indent=2) + "\n")
    console.print(f"Updated {path}")


def load_history() -> dict:
    """Load historical results from all per-type history files."""
    return {
        "pipelines": load_history_for_type("pipelines"),
        "modules": load_history_for_type("modules"),
        "subworkflows": load_history_for_type("subworkflows"),
    }


def _create_history_entry(results: list[dict]) -> dict:
    """Create a history entry from results."""
    valid_results = [r for r in results if not r.get("parse_error", False)]
    parse_error_results = [r for r in results if r.get("parse_error", False)]

    return {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "total": len(results),
        "parse_errors": len(parse_error_results),
        "errors_zero": sum(1 for r in valid_results if r["errors"] == 0),
        "errors_low": sum(1 for r in valid_results if 0 < r["errors"] <= 5),
        "errors_high": sum(1 for r in valid_results if r["errors"] > 5),
        "warnings_zero": sum(1 for r in valid_results if r["warnings"] == 0),
        "warnings_low": sum(1 for r in valid_results if 0 < r["warnings"] <= 20),
        "warnings_high": sum(1 for r in valid_results if r["warnings"] > 20),
    }


def _update_history_for_type(history_list: list[dict], entry: dict) -> list[dict]:
    """Update history list for a specific type, replacing today's entry if it exists."""
    today = entry["date"]
    for i, h in enumerate(history_list):
        if h["date"] == today:
            history_list[i] = entry
            return history_list
    history_list.append(entry)
    return history_list


def update_history(
    pipeline_results: list[dict] | None = None,
    module_results: list[dict] | None = None,
    subworkflow_results: list[dict] | None = None,
) -> dict:
    """Add current results to history and return updated history.

    Each type's history is stored in its own file to allow parallel updates.
    """
    history = {}

    if pipeline_results is not None:
        pipelines_history = load_history_for_type("pipelines")
        entry = _create_history_entry(pipeline_results)
        pipelines_history = _update_history_for_type(pipelines_history, entry)
        save_history_for_type("pipelines", pipelines_history)
        history["pipelines"] = pipelines_history

    if module_results is not None:
        modules_history = load_history_for_type("modules")
        entry = _create_history_entry(module_results)
        modules_history = _update_history_for_type(modules_history, entry)
        save_history_for_type("modules", modules_history)
        history["modules"] = modules_history

    if subworkflow_results is not None:
        subworkflows_history = load_history_for_type("subworkflows")
        entry = _create_history_entry(subworkflow_results)
        subworkflows_history = _update_history_for_type(subworkflows_history, entry)
        save_history_for_type("subworkflows", subworkflows_history)
        history["subworkflows"] = subworkflows_history

    return history


def _create_stacked_chart(
    dates: list[str],
    series: list[tuple[list[int], str, str, str]],  # (values, name, line_color, fill_color)
    title: str,
    output_path: Path,
    y_label: str = "Number of Items",
) -> None:
    """Create a stacked area chart and save it to a file."""
    fig = go.Figure()
    for i, (values, name, line_color, fill_color) in enumerate(series):
        fig.add_trace(
            go.Scatter(
                x=dates,
                y=values,
                name=name,
                fill="tozeroy" if i == 0 else "tonexty",
                mode="lines",
                line={"width": 0.5, "color": line_color},
                fillcolor=fill_color,
                stackgroup="stack",
            )
        )
    fig.update_layout(
        title={"text": title, "x": 0.5, "xanchor": "center", "font": {"size": 20}},
        xaxis_title="Date",
        yaxis_title=y_label,
        legend={"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "center", "x": 0.5},
        template="plotly_white",
        hovermode="x unified",
        width=1000,
        height=500,
    )
    fig.write_image(str(output_path), scale=2)
    console.print(f"Generated {output_path}")


def generate_charts_for_type(history: list[dict], output_dir: Path, type_name: str) -> None:
    """Generate error and warning charts for a specific type (pipelines, modules, subworkflows).

    Charts are saved to LINT_RESULTS_DIR with type-prefixed filenames (e.g., pipelines_errors.png).
    """
    if not history:
        console.print(f"[yellow]Not enough history to generate {type_name} charts[/yellow]")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    dates = [h["date"] for h in history]
    y_label = f"Number of {type_name.title()}"

    _create_stacked_chart(
        dates,
        [
            ([h["errors_zero"] for h in history], "No errors", "#2ecc71", "rgba(46, 204, 113, 0.7)"),
            ([h["errors_low"] for h in history], "1-5 errors", "#f39c12", "rgba(243, 156, 18, 0.7)"),
            ([h["errors_high"] for h in history], ">5 errors", "#e74c3c", "rgba(231, 76, 60, 0.7)"),
            ([h.get("parse_errors", 0) for h in history], "Parse errors", "#8e44ad", "rgba(142, 68, 173, 0.7)"),
        ],
        f"{type_name.title()} Errors Over Time",
        LINT_RESULTS_DIR / f"{type_name}_errors.png",
        y_label,
    )

    _create_stacked_chart(
        dates,
        [
            ([h["warnings_zero"] for h in history], "No warnings", "#1abc9c", "rgba(26, 188, 156, 0.7)"),
            ([h["warnings_low"] for h in history], "1-20 warnings", "#3498db", "rgba(52, 152, 219, 0.7)"),
            ([h["warnings_high"] for h in history], ">20 warnings", "#9b59b6", "rgba(155, 89, 182, 0.7)"),
            ([h.get("parse_errors", 0) for h in history], "Parse errors", "#8e44ad", "rgba(142, 68, 173, 0.7)"),
        ],
        f"{type_name.title()} Warnings Over Time",
        LINT_RESULTS_DIR / f"{type_name}_warnings.png",
        y_label,
    )


def generate_all_charts(history: dict) -> None:
    """Generate charts for all types (pipelines, modules, subworkflows)."""
    if history.get("pipelines"):
        generate_charts_for_type(history["pipelines"], PIPELINES_LINT_RESULTS_DIR, "pipelines")
    if history.get("modules"):
        generate_charts_for_type(history["modules"], MODULES_LINT_RESULTS_DIR, "modules")
    if history.get("subworkflows"):
        generate_charts_for_type(history["subworkflows"], SUBWORKFLOWS_LINT_RESULTS_DIR, "subworkflows")


def _generate_results_section(
    results: list[dict],
    type_name: str,
    type_singular: str,
    lint_results_dir: Path,
    include_charts: bool,
) -> list[str]:
    """Generate a results section for a specific type (pipelines, modules, subworkflows)."""
    if not results:
        return []

    sorted_results = _sort_results(results)
    valid_results = [r for r in results if not r.get("parse_error", False)]
    parse_error_count = sum(1 for r in results if r.get("parse_error", False))
    total_errors = sum(r["errors"] for r in valid_results)
    total_warnings = sum(r["warnings"] for r in valid_results)
    zero_error_count = sum(1 for r in valid_results if r["errors"] == 0)
    zero_error_percentage = (zero_error_count / len(results) * 100) if results else 0

    lines = [
        f"## {type_name.title()}",
        "",
        f"- **Total:** {parse_error_count} parse errors, {total_errors} errors, "
        f"{total_warnings} warnings across {len(results)} {type_name}",
        f"- **Zero errors:** {zero_error_count} {type_name} ({zero_error_percentage:.1f}%)",
        "",
    ]

    # Add charts in a side-by-side table (charts are in LINT_RESULTS_DIR with type-prefixed names)
    errors_chart = LINT_RESULTS_DIR / f"{type_name}_errors.png"
    warnings_chart = LINT_RESULTS_DIR / f"{type_name}_warnings.png"
    if include_charts and errors_chart.exists() and warnings_chart.exists():
        lines.extend(
            [
                "| Errors | Warnings |",
                "|:------:|:--------:|",
                f"| ![Errors]({errors_chart}) | ![Warnings]({warnings_chart}) |",
                "",
            ]
        )

    # Results table in a collapsible details section
    lines.extend(
        [
            "<details>",
            f"<summary>{type_singular.title()} Results ({len(results)} {type_name})</summary>",
            "",
            f"| {type_singular.title()} | Parse Error | Errors | Warnings | Lint Output |",
            "|----------|:-----------:|-------:|---------:|:-----------:|",
        ]
    )

    for result in sorted_results:
        errors = result["errors"]
        warnings = result["warnings"]
        parse_error = result.get("parse_error", False)

        if parse_error:
            parse_error_str = "Yes"
            error_str = "-"
            warning_str = "-"
            status_emoji = ":x:"
        else:
            parse_error_str = "No"
            error_str = str(errors)
            warning_str = str(warnings)
            status_emoji = ":white_check_mark:" if errors == 0 else ":x:"

        name_link = f"{status_emoji} [{result['name']}]({result['html_url']})"
        lint_file_link = f"[View]({lint_results_dir}/{result['name']}_lint.md)"
        lines.append(f"| {name_link} | {parse_error_str} | {error_str} | {warning_str} | {lint_file_link} |")

    lines.extend(
        [
            "",
            "</details>",
            "",
        ]
    )

    return lines


def generate_readme(
    pipeline_results: list[dict] | None = None,
    module_results: list[dict] | None = None,
    subworkflow_results: list[dict] | None = None,
    include_charts: bool = False,
    nextflow_version: str = "unknown",
) -> str:
    """Generate README content with results for all types."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = [
        "# nf-core Strict Syntax Health Report",
        "",
        "This repository tracks the health of nf-core pipelines, modules, and subworkflows "
        "with respect to Nextflow's _strict syntax_ linting.",
        "",
        "The [Nextflow docs](https://www.nextflow.io/docs/latest/strict-syntax.html) describes the differences "
        "from standard Nextflow syntax and includes many examples to help with migration and fixing errors.",
        "Strict syntax is backwards compatible with existing Nextflow code, "
        "but enforces stricter rules to catch common errors and improve code quality.",
        "",
        "The goal is for all nf-core pipelines to run without errors using strict syntax.",
        "",
        "> [!IMPORTANT]",
        "> See the [nf-core blog post](https://nf-co.re/blog/2025/nextflow_syntax_nf-core_roadmap) "
        "for details on the migration timeline.",
        "> **Fixing all errors from `nextflow lint` will be a requirement by early spring 2026.**",
        "",
        f"- **Last updated:** {now}",
        f"- **Nextflow version:** {nextflow_version}",
        "",
    ]

    # Add sections for each type
    if pipeline_results:
        lines.extend(
            _generate_results_section(
                pipeline_results, "pipelines", "pipeline", PIPELINES_LINT_RESULTS_DIR, include_charts
            )
        )

    if module_results:
        lines.extend(
            _generate_results_section(module_results, "modules", "module", MODULES_LINT_RESULTS_DIR, include_charts)
        )

    if subworkflow_results:
        lines.extend(
            _generate_results_section(
                subworkflow_results, "subworkflows", "subworkflow", SUBWORKFLOWS_LINT_RESULTS_DIR, include_charts
            )
        )

    lines.extend(
        [
            "## About",
            "",
            "This report is generated daily by running `nextflow lint` on each nf-core pipeline, module, "
            "and subworkflow.",
            "The linting checks for strict syntax compliance in Nextflow DSL2 code.",
            "",
            "- **Parse errors** indicate items where `nextflow lint` could not run at all, "
            "typically due to syntax errors that prevent Nextflow from parsing the code",
            "- **Errors** indicate syntax issues that will cause problems in future Nextflow versions",
            "- **Warnings** indicate deprecated patterns that should be updated, "
            "but having warnings is fine (though it's nice to fix those as well if possible)",
            "",
            "## Running Locally",
            "",
            "You can run `nextflow lint` on your own pipeline to check for strict syntax issues:",
            "",
            "```bash",
            "nextflow lint .",
            "```",
            "",
            "> **Note:** Until [this fix](https://github.com/nextflow-io/nextflow/pull/6716) is included "
            "in a Nextflow edge release, you may need to exclude nf-test files manually:",
            "> ```bash",
            '> nextflow lint . -exclude ".git,.nf-test,nf-test.config"',
            "> ```",
            "",
            "See the [strict syntax documentation](https://www.nextflow.io/docs/latest/strict-syntax.html) "
            "for more information about the rules being checked.",
            "",
            "## Getting Help",
            "",
            "If you need help fixing strict syntax errors in your pipeline, "
            "the [Nextflow community forum](https://community.seqera.io/) is a great place to ask questions.",
            "",
        ]
    )

    return "\n".join(lines)


@click.command()
@click.option(
    "--update-readme",
    is_flag=True,
    help="Update the README.md file with the results",
)
@click.option(
    "--update-pipelines",
    is_flag=True,
    help="Download the latest pipelines.json from nf-co.re before running",
)
@click.option(
    "--pipeline",
    "-p",
    multiple=True,
    help="Only process specific pipeline(s) by name (can be used multiple times)",
)
@click.option(
    "--module",
    "-m",
    multiple=True,
    help="Only process specific module(s) by name (can be used multiple times)",
)
@click.option(
    "--subworkflow",
    "-s",
    multiple=True,
    help="Only process specific subworkflow(s) by name (can be used multiple times)",
)
@click.option(
    "--skip-pipelines",
    is_flag=True,
    help="Skip linting pipelines",
)
@click.option(
    "--skip-modules",
    is_flag=True,
    help="Skip linting modules",
)
@click.option(
    "--skip-subworkflows",
    is_flag=True,
    help="Skip linting subworkflows",
)
@click.option(
    "--generate-charts-only",
    is_flag=True,
    help="Only generate charts and README from existing history files (no linting)",
)
@click.option(
    "--no-cache",
    is_flag=True,
    help="Ignore commit cache and re-lint everything (by default, unchanged repos are skipped)",
)
def main(
    update_readme: bool,
    update_pipelines: bool,
    pipeline: tuple[str, ...],
    module: tuple[str, ...],
    subworkflow: tuple[str, ...],
    skip_pipelines: bool,
    skip_modules: bool,
    skip_subworkflows: bool,
    generate_charts_only: bool,
    no_cache: bool,
) -> None:
    """Check nf-core pipelines, modules, and subworkflows for Nextflow strict syntax linting issues."""
    if update_pipelines:
        update_pipelines_json()

    # Get nextflow version
    nextflow_version = get_nextflow_version()
    console.print(f"Using Nextflow version: {nextflow_version}")

    # Generate charts only mode - skip linting, load existing results and generate outputs
    if generate_charts_only:
        console.print("[bold]Generate charts only mode - loading existing data...[/bold]")

        # Load results from JSON files (saved by lint jobs)
        pipeline_results = load_results_for_type("pipelines") or None
        module_results = load_results_for_type("modules") or None
        subworkflow_results = load_results_for_type("subworkflows") or None

        # Load history and generate charts
        history = load_history()
        generate_all_charts(history)

        if update_readme:
            readme_content = generate_readme(
                pipeline_results=pipeline_results,
                module_results=module_results,
                subworkflow_results=subworkflow_results,
                include_charts=True,
                nextflow_version=nextflow_version,
            )
            README_PATH.write_text(readme_content)
            console.print(f"\n[green]Updated {README_PATH}[/green]")
        return

    pipeline_results: list[dict] | None = None
    module_results: list[dict] | None = None
    subworkflow_results: list[dict] | None = None

    # Lint pipelines
    if not skip_pipelines:
        pipelines = load_pipelines()

        if pipeline:
            pipeline_names = set(pipeline)
            pipelines = [p for p in pipelines if p["name"] in pipeline_names]
            if not pipelines:
                console.print(f"[red]No matching pipelines found for: {', '.join(pipeline_names)}[/red]")
                sys.exit(1)
            console.print(f"Filtering to {len(pipelines)} pipeline(s): {', '.join(p['name'] for p in pipelines)}")

        pipeline_results = run_pipeline_lint(pipelines, no_cache=no_cache)
        display_results(pipeline_results, title="nf-core Pipeline Strict Syntax Health")
        # Save results for aggregation (only when not filtering specific pipelines)
        if not pipeline:
            save_results_for_type("pipelines", pipeline_results)

    # Lint modules and subworkflows (requires modules repo)
    if not skip_modules or not skip_subworkflows:
        # Check if we can skip cloning by using cached results
        # Only use cache when linting ALL modules/subworkflows (no -m/-s filters)
        use_modules_cache = not module and not subworkflow and not no_cache
        modules_repo_unchanged, remote_commit = check_modules_repo_unchanged(
            no_cache=not use_modules_cache,
            check_modules=not skip_modules,
            check_subworkflows=not skip_subworkflows,
        )

        if modules_repo_unchanged:
            console.print(f"[dim]nf-core/modules repo unchanged at {remote_commit[:8]} - using cached results[/dim]")
            repo_commit = remote_commit
        else:
            # Clone/update the repo
            repo_commit = clone_modules_repo()

        if not skip_modules:
            if modules_repo_unchanged:
                # Use cached results - need to load module list for the cache lookup
                # We need the modules repo to be present for discover_modules, but since it's unchanged
                # we can just use the cached results directly
                modules_cache = load_results_dict_for_type("modules")
                # Build modules list from cache keys (excluding _repo_commit)
                base_url = "https://github.com/nf-core/modules/tree/master/modules/nf-core"
                modules = [
                    {"name": name, "html_url": f"{base_url}/{name.replace('_', '/')}"}
                    for name in modules_cache.keys()
                    if name != "_repo_commit"
                ]
                module_results = load_cached_modules_results(modules)
                console.print(f"[dim]Loaded {len(module_results)} cached module results[/dim]")
            else:
                modules = discover_modules()

                if module:
                    module_names = set(module)
                    modules = [m for m in modules if m["name"] in module_names]
                    if not modules:
                        console.print(f"[red]No matching modules found for: {', '.join(module_names)}[/red]")
                        sys.exit(1)
                    console.print(f"Filtering to {len(modules)} module(s): {', '.join(m['name'] for m in modules)}")

                module_results = run_modules_lint(modules, nextflow_version)

            display_results(module_results, title="nf-core Module Strict Syntax Health")
            # Save results for aggregation (only when not filtering specific modules)
            if not module:
                save_results_for_type("modules", module_results, repo_commit=repo_commit)

        if not skip_subworkflows:
            if modules_repo_unchanged:
                # Use cached results
                subworkflows_cache = load_results_dict_for_type("subworkflows")
                base_url = "https://github.com/nf-core/modules/tree/master/subworkflows/nf-core"
                subworkflows = [
                    {"name": name, "html_url": f"{base_url}/{name}"}
                    for name in subworkflows_cache.keys()
                    if name != "_repo_commit"
                ]
                subworkflow_results = load_cached_subworkflows_results(subworkflows)
                console.print(f"[dim]Loaded {len(subworkflow_results)} cached subworkflow results[/dim]")
            else:
                subworkflows = discover_subworkflows()

                if subworkflow:
                    subworkflow_names = set(subworkflow)
                    subworkflows = [s for s in subworkflows if s["name"] in subworkflow_names]
                    if not subworkflows:
                        console.print(f"[red]No matching subworkflows found for: {', '.join(subworkflow_names)}[/red]")
                        sys.exit(1)
                    console.print(
                        f"Filtering to {len(subworkflows)} subworkflow(s): {', '.join(s['name'] for s in subworkflows)}"
                    )

                subworkflow_results = run_subworkflows_lint(subworkflows, nextflow_version)

            display_results(subworkflow_results, title="nf-core Subworkflow Strict Syntax Health")
            # Save results for aggregation (only when not filtering specific subworkflows)
            if not subworkflow:
                save_results_for_type("subworkflows", subworkflow_results, repo_commit=repo_commit)

    # Update history and generate charts
    # History is updated per-type when all items of that type are linted (no -p/-m/-s filters)
    # This allows parallel jobs to each update their own history file
    include_charts = False
    history = {}

    # Update history for each type that was fully linted
    if pipeline_results is not None and not pipeline:
        update_history(pipeline_results=pipeline_results)
        history["pipelines"] = load_history_for_type("pipelines")

    if module_results is not None and not module:
        update_history(module_results=module_results)
        history["modules"] = load_history_for_type("modules")

    if subworkflow_results is not None and not subworkflow:
        update_history(subworkflow_results=subworkflow_results)
        history["subworkflows"] = load_history_for_type("subworkflows")

    # Generate charts if any history was updated
    if history:
        # Load full history for chart generation
        full_history = load_history()
        generate_all_charts(full_history)
        include_charts = True

    if update_readme:
        readme_content = generate_readme(
            pipeline_results=pipeline_results,
            module_results=module_results,
            subworkflow_results=subworkflow_results,
            include_charts=include_charts,
            nextflow_version=nextflow_version,
        )
        README_PATH.write_text(readme_content)
        console.print(f"\n[green]Updated {README_PATH}[/green]")


if __name__ == "__main__":
    main()
