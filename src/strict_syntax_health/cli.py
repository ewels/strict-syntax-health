"""CLI for strict-syntax-health."""

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx
import rich_click as click
from rich.console import Console
from rich.table import Table

PIPELINES_URL = "https://nf-co.re/pipelines.json"
PIPELINES_JSON_PATH = Path("pipelines.json")
PIPELINES_DIR = Path("pipelines")
README_PATH = Path("README.md")

console = Console()


def update_pipelines_json() -> None:
    """Download the latest pipelines.json from nf-co.re."""
    console.print(f"Downloading {PIPELINES_URL}...")
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


def clone_pipeline(pipeline: dict) -> Path:
    """Clone a pipeline repository."""
    repo_path = PIPELINES_DIR / pipeline["name"]

    if repo_path.exists():
        console.print(f"  Pipeline already cloned: {pipeline['name']}")
        # Pull latest changes
        subprocess.run(
            ["git", "-C", str(repo_path), "pull", "--quiet"],
            check=True,
            capture_output=True,
        )
    else:
        console.print(f"  Cloning {pipeline['full_name']}...")
        PIPELINES_DIR.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", pipeline["html_url"], str(repo_path)],
            check=True,
            capture_output=True,
        )

    return repo_path


def lint_pipeline(repo_path: Path) -> dict:
    """Run nextflow lint on a pipeline."""
    result = subprocess.run(
        ["nextflow", "lint", ".", "-o", "json"],
        cwd=repo_path,
        capture_output=True,
        text=True,
    )

    # nextflow lint returns non-zero exit code if there are errors
    # but we still want to parse the output
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        console.print(f"[red]Failed to parse lint output for {repo_path.name}[/red]")
        console.print(f"stdout: {result.stdout}")
        console.print(f"stderr: {result.stderr}")
        return {"summary": {"errors": -1}, "errors": [], "warnings": []}


def run_lint(pipelines: list[dict]) -> list[dict]:
    """Clone and lint all pipelines."""
    results = []

    for pipeline in pipelines:
        console.print(f"Processing {pipeline['name']}...")

        try:
            repo_path = clone_pipeline(pipeline)
            lint_result = lint_pipeline(repo_path)

            results.append(
                {
                    "name": pipeline["name"],
                    "full_name": pipeline["full_name"],
                    "html_url": pipeline["html_url"],
                    "errors": lint_result.get("summary", {}).get("errors", 0),
                    "warnings": len(lint_result.get("warnings", [])),
                    "lint_details": lint_result,
                }
            )
        except subprocess.CalledProcessError as e:
            console.print(f"[red]Failed to process {pipeline['name']}: {e}[/red]")
            results.append(
                {
                    "name": pipeline["name"],
                    "full_name": pipeline["full_name"],
                    "html_url": pipeline["html_url"],
                    "errors": -1,
                    "warnings": -1,
                    "lint_details": {},
                }
            )

    return results


def display_results(results: list[dict]) -> None:
    """Display results in a rich table."""
    table = Table(title="nf-core Pipeline Strict Syntax Health")
    table.add_column("Pipeline", style="cyan")
    table.add_column("Errors", justify="right")
    table.add_column("Warnings", justify="right")

    # Sort by errors (descending), then warnings (descending)
    sorted_results = sorted(results, key=lambda x: (-x["errors"], -x["warnings"]))

    total_errors = 0
    total_warnings = 0

    for result in sorted_results:
        errors = result["errors"]
        warnings = result["warnings"]

        if errors == -1:
            error_str = "[red]FAILED[/red]"
            warning_str = "[red]FAILED[/red]"
        else:
            total_errors += errors
            total_warnings += warnings
            error_str = f"[red]{errors}[/red]" if errors > 0 else "[green]0[/green]"
            warning_str = f"[yellow]{warnings}[/yellow]" if warnings > 0 else "[green]0[/green]"

        table.add_row(result["name"], error_str, warning_str)

    console.print(table)
    console.print(f"\n[bold]Total: {total_errors} errors, {total_warnings} warnings[/bold]")


def generate_readme(results: list[dict]) -> str:
    """Generate README content with results."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    sorted_results = sorted(results, key=lambda x: (-x["errors"], -x["warnings"]))

    total_errors = sum(r["errors"] for r in results if r["errors"] >= 0)
    total_warnings = sum(r["warnings"] for r in results if r["warnings"] >= 0)

    lines = [
        "# nf-core Strict Syntax Health Report",
        "",
        "This repository tracks the health of nf-core pipelines with respect to Nextflow's strict syntax linting.",
        "",
        f"**Last updated:** {now}",
        "",
        f"**Total:** {total_errors} errors, {total_warnings} warnings across {len(results)} pipelines",
        "",
        "## Results",
        "",
        "| Pipeline | Errors | Warnings |",
        "|----------|-------:|--------:|",
    ]

    for result in sorted_results:
        errors = result["errors"]
        warnings = result["warnings"]

        if errors == -1:
            error_str = "FAILED"
            warning_str = "FAILED"
        else:
            error_str = str(errors)
            warning_str = str(warnings)

        name_link = f"[{result['name']}]({result['html_url']})"
        lines.append(f"| {name_link} | {error_str} | {warning_str} |")

    lines.extend(
        [
            "",
            "## About",
            "",
            "This report is generated weekly by running `nextflow lint` on each nf-core pipeline.",
            "The linting checks for strict syntax compliance in Nextflow DSL2 code.",
            "",
            "- **Errors** indicate syntax issues that will cause problems in future Nextflow versions",
            "- **Warnings** indicate deprecated patterns that should be updated",
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
def main(update_readme: bool, update_pipelines: bool, pipeline: tuple[str, ...]) -> None:
    """Check nf-core pipelines for Nextflow strict syntax linting issues."""
    if update_pipelines:
        update_pipelines_json()

    pipelines = load_pipelines()

    if pipeline:
        pipeline_names = set(pipeline)
        pipelines = [p for p in pipelines if p["name"] in pipeline_names]
        if not pipelines:
            console.print(f"[red]No matching pipelines found for: {', '.join(pipeline_names)}[/red]")
            sys.exit(1)
        console.print(f"Filtering to {len(pipelines)} pipeline(s): {', '.join(p['name'] for p in pipelines)}")

    results = run_lint(pipelines)
    display_results(results)

    if update_readme:
        readme_content = generate_readme(results)
        README_PATH.write_text(readme_content)
        console.print(f"\n[green]Updated {README_PATH}[/green]")


if __name__ == "__main__":
    main()
