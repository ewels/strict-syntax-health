# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This tool monitors nf-core Nextflow pipelines, modules, and subworkflows for strict syntax linting errors. It clones repositories, runs `nextflow lint`, and generates health reports with trend charts.

## Commands

```bash
# Install dependencies
pip install -e .

# Run the linter on all nf-core pipelines, modules, and subworkflows
strict-syntax-health

# Update the pipelines list from nf-co.re before running
strict-syntax-health --update-pipelines

# Update README.md with results
strict-syntax-health --update-readme

# Lint specific pipeline(s) only
strict-syntax-health -p demo -p rnaseq

# Skip specific types
strict-syntax-health --skip-modules --skip-subworkflows  # Only lint pipelines
strict-syntax-health --skip-pipelines                     # Only lint modules/subworkflows

# Run pre-commit hooks (uses prek instead of pre-commit)
prek run --all-files
```

## Architecture

Single-module CLI (`src/strict_syntax_health/cli.py`) using rich-click:

1. **Pipeline discovery**: Fetches `pipelines.json` from nf-co.re, filters out archived pipelines
2. **Module/Subworkflow discovery**: Clones nf-core/modules repo, discovers components from directory structure
3. **Cloning**: Shallow clones pipelines to `pipelines/` directory, nf-core/modules to `modules/`
4. **Linting**: Runs `nextflow lint` on each component, parses JSON output
5. **History tracking**: Stores daily aggregates in `lint_results/history.json` (counts by error/warning severity buckets)
6. **Chart generation**: Creates stacked area charts with Plotly showing trends over time
7. **README generation**: Outputs markdown with charts and collapsible result tables for each type

### Directory Structure

```
pipelines/
├── pipelines.json          # Pipeline list from nf-co.re (tracked in git)
└── <cloned pipeline repos> # (gitignored)

modules/                    # nf-core/modules clone (gitignored)

lint_results/
├── history.json            # Combined history for pipelines, modules, subworkflows
├── pipelines/
│   ├── errors_chart.png
│   ├── warnings_chart.png
│   └── <pipeline>_lint.md
├── modules/
│   ├── errors_chart.png
│   ├── warnings_chart.png
│   └── <module>_lint.md
└── subworkflows/
    ├── errors_chart.png
    ├── warnings_chart.png
    └── <subworkflow>_lint.md
```

## External Dependencies

- **Nextflow**: Must be installed and available on PATH. In CI, it's built from the master branch to get latest lint features.
- **Git**: Required for cloning pipelines and nf-core/modules

## Code Style

- Line length: 120 characters
- Ruff for linting (E, F, I, W rules) and formatting
- Double quotes for strings
