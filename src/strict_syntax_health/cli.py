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

PIPELINES_URL = "https://nf-co.re/pipelines.json"
PIPELINES_JSON_PATH = Path("pipelines.json")
PIPELINES_DIR = Path("pipelines")
LINT_RESULTS_DIR = Path("lint_results")
README_PATH = Path("README.md")
HISTORY_PATH = Path("history.json")
ERRORS_CHART_PATH = Path("errors_chart.png")
WARNINGS_CHART_PATH = Path("warnings_chart.png")

console = Console()


def _sort_results(results: list[dict]) -> list[dict]:
    """Sort results by parse_error last, then errors (ascending), then warnings (ascending)."""
    return sorted(results, key=lambda x: (x.get("parse_error", False), x["errors"], x["warnings"]))


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


def lint_pipeline(repo_path: Path) -> dict:
    """Run nextflow lint on a pipeline (JSON output for parsing)."""
    result = subprocess.run(
        ["nextflow", "lint", "-exclude", ".git,.nf-test,nf-test.config", ".", "-o", "json"],
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
        console.print(f"[red]Failed to parse lint output for {repo_path.name}[/red]")
        console.print(f"stdout: {result.stdout}")
        console.print(f"stderr: {result.stderr}")
        return {"summary": {"errors": 0}, "errors": [], "warnings": [], "parse_error": True}


def lint_pipeline_text(repo_path: Path, pipeline_name: str) -> None:
    """Run nextflow lint on a pipeline and save text output to file."""
    LINT_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    output_file = LINT_RESULTS_DIR / f"{pipeline_name}_lint.txt"

    result = subprocess.run(
        ["nextflow", "lint", "-exclude", ".git,.nf-test,nf-test.config", "."],
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


def run_lint(pipelines: list[dict]) -> list[dict]:
    """Clone and lint all pipelines."""
    results = []

    for pipeline in pipelines:
        console.print(f"Processing {pipeline['name']}...")

        try:
            repo_path = clone_pipeline(pipeline)
            lint_result = lint_pipeline(repo_path)
            lint_pipeline_text(repo_path, pipeline["name"])

            results.append(
                {
                    "name": pipeline["name"],
                    "full_name": pipeline["full_name"],
                    "html_url": pipeline["html_url"],
                    "errors": lint_result.get("summary", {}).get("errors", 0),
                    "warnings": len(lint_result.get("warnings", [])),
                    "parse_error": lint_result.get("parse_error", False),
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
                    "errors": 0,
                    "warnings": 0,
                    "parse_error": True,
                    "lint_details": {},
                }
            )

    return results


def display_results(results: list[dict]) -> None:
    """Display results in a rich table."""
    table = Table(title="nf-core Pipeline Strict Syntax Health")
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


def load_history() -> list[dict]:
    """Load historical results from the history file."""
    if HISTORY_PATH.exists():
        return json.loads(HISTORY_PATH.read_text())
    return []


def save_history(history: list[dict]) -> None:
    """Save historical results to the history file."""
    HISTORY_PATH.write_text(json.dumps(history, indent=2))
    console.print(f"Updated {HISTORY_PATH}")


def update_history(results: list[dict]) -> list[dict]:
    """Add current results to history and return updated history."""
    history = load_history()

    # Calculate categories for this run
    valid_results = [r for r in results if not r.get("parse_error", False)]
    parse_error_results = [r for r in results if r.get("parse_error", False)]

    entry = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "total_pipelines": len(results),
        "parse_errors": len(parse_error_results),
        "errors_zero": sum(1 for r in valid_results if r["errors"] == 0),
        "errors_low": sum(1 for r in valid_results if 0 < r["errors"] <= 5),
        "errors_high": sum(1 for r in valid_results if r["errors"] > 5),
        "warnings_zero": sum(1 for r in valid_results if r["warnings"] == 0),
        "warnings_low": sum(1 for r in valid_results if 0 < r["warnings"] <= 20),
        "warnings_high": sum(1 for r in valid_results if r["warnings"] > 20),
    }

    # Check if we already have an entry for today and update it, otherwise append
    today = entry["date"]
    for i, h in enumerate(history):
        if h["date"] == today:
            history[i] = entry
            break
    else:
        history.append(entry)

    save_history(history)
    return history


def _create_stacked_chart(
    dates: list[str],
    series: list[tuple[list[int], str, str, str]],  # (values, name, line_color, fill_color)
    title: str,
    output_path: Path,
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
        yaxis_title="Number of Pipelines",
        legend={"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "center", "x": 0.5},
        template="plotly_white",
        hovermode="x unified",
        width=1000,
        height=500,
    )
    fig.write_image(str(output_path), scale=2)
    console.print(f"Generated {output_path}")


def generate_charts(history: list[dict]) -> None:
    """Generate charts showing pipeline health over time."""
    if not history:
        console.print("[yellow]Not enough history to generate charts[/yellow]")
        return

    dates = [h["date"] for h in history]

    _create_stacked_chart(
        dates,
        [
            ([h["errors_zero"] for h in history], "No errors", "#2ecc71", "rgba(46, 204, 113, 0.7)"),
            ([h["errors_low"] for h in history], "1-5 errors", "#f39c12", "rgba(243, 156, 18, 0.7)"),
            ([h["errors_high"] for h in history], ">5 errors", "#e74c3c", "rgba(231, 76, 60, 0.7)"),
            ([h.get("parse_errors", 0) for h in history], "Parse errors", "#8e44ad", "rgba(142, 68, 173, 0.7)"),
        ],
        "Errors Over Time",
        ERRORS_CHART_PATH,
    )

    _create_stacked_chart(
        dates,
        [
            ([h["warnings_zero"] for h in history], "No warnings", "#1abc9c", "rgba(26, 188, 156, 0.7)"),
            ([h["warnings_low"] for h in history], "1-20 warnings", "#3498db", "rgba(52, 152, 219, 0.7)"),
            ([h["warnings_high"] for h in history], ">20 warnings", "#9b59b6", "rgba(155, 89, 182, 0.7)"),
            ([h.get("parse_errors", 0) for h in history], "Parse errors", "#8e44ad", "rgba(142, 68, 173, 0.7)"),
        ],
        "Warnings Over Time",
        WARNINGS_CHART_PATH,
    )


def generate_readme(results: list[dict], include_chart: bool = False, nextflow_version: str = "unknown") -> str:
    """Generate README content with results."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    sorted_results = _sort_results(results)

    valid_results = [r for r in results if not r.get("parse_error", False)]
    parse_error_count = sum(1 for r in results if r.get("parse_error", False))
    total_errors = sum(r["errors"] for r in valid_results)
    total_warnings = sum(r["warnings"] for r in valid_results)

    lines = [
        "# nf-core Strict Syntax Health Report",
        "",
        "This repository tracks the health of nf-core pipelines with respect to Nextflow's strict syntax linting.",
        "",
        f"**Last updated:** {now}",
        "",
        f"**Nextflow version:** {nextflow_version}",
        "",
        f"**Total:** {parse_error_count} parse errors, {total_errors} errors, "
        f"{total_warnings} warnings across {len(results)} pipelines",
        "",
    ]

    if include_chart and ERRORS_CHART_PATH.exists() and WARNINGS_CHART_PATH.exists():
        lines.extend(
            [
                "## Trends",
                "",
                "### Errors",
                "",
                f"![Errors Chart]({ERRORS_CHART_PATH})",
                "",
                "### Warnings",
                "",
                f"![Warnings Chart]({WARNINGS_CHART_PATH})",
                "",
            ]
        )

    lines.extend(
        [
            "## Results",
            "",
            "| Pipeline | Parse Error | Errors | Warnings | Lint Output |",
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
        else:
            parse_error_str = "No"
            error_str = str(errors)
            warning_str = str(warnings)

        name_link = f"[{result['name']}]({result['html_url']})"
        lint_file_link = f"[View]({LINT_RESULTS_DIR}/{result['name']}_lint.txt)"
        lines.append(f"| {name_link} | {parse_error_str} | {error_str} | {warning_str} | {lint_file_link} |")

    lines.extend(
        [
            "",
            "## About",
            "",
            "This report is generated weekly by running `nextflow lint` on each nf-core pipeline.",
            "The linting checks for strict syntax compliance in Nextflow DSL2 code.",
            "",
            "- **Parse errors** indicate pipelines where `nextflow lint` could not run at all, "
            "typically due to syntax errors that prevent Nextflow from parsing the pipeline code",
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

    # Get nextflow version
    nextflow_version = get_nextflow_version()
    console.print(f"Using Nextflow version: {nextflow_version}")

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

    # Update history and generate charts (only when not filtering pipelines)
    include_chart = False
    if not pipeline:
        history = update_history(results)
        generate_charts(history)
        include_chart = True

    if update_readme:
        readme_content = generate_readme(results, include_chart=include_chart, nextflow_version=nextflow_version)
        README_PATH.write_text(readme_content)
        console.print(f"\n[green]Updated {README_PATH}[/green]")


if __name__ == "__main__":
    main()
