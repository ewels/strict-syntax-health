# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This tool monitors nf-core Nextflow pipelines for strict syntax linting errors. It clones pipelines, runs `nextflow lint`, and generates a health report with trend charts.

## Commands

```bash
# Install dependencies
pip install -e .

# Run the linter on all nf-core pipelines
strict-syntax-health

# Update the pipelines list from nf-co.re before running
strict-syntax-health --update-pipelines

# Update README.md with results
strict-syntax-health --update-readme

# Lint specific pipeline(s) only
strict-syntax-health -p demo -p rnaseq

# Run pre-commit hooks (uses prek instead of pre-commit)
prek run --all-files
```

## Architecture

Single-module CLI (`src/strict_syntax_health/cli.py`) using rich-click:

1. **Pipeline discovery**: Fetches `pipelines.json` from nf-co.re, filters out archived pipelines
2. **Cloning**: Shallow clones pipelines to `pipelines/` directory (or pulls if already cloned), prefers `dev` branch
3. **Linting**: Runs `nextflow lint . -o json` on each pipeline, parses JSON output
4. **History tracking**: Stores daily aggregates in `history.json` (counts by error/warning severity buckets)
5. **Chart generation**: Creates stacked area charts with Plotly showing trends over time
6. **README generation**: Outputs markdown table with per-pipeline results and links to per-pipeline markdown reports

Key files produced: `README.md`, `history.json`, `errors_chart.png`, `warnings_chart.png`, `lint_results/*.md`

## External Dependencies

- **Nextflow**: Must be installed and available on PATH. In CI, it's built from the master branch to get latest lint features.
- **Git**: Required for cloning pipelines

## Code Style

- Line length: 120 characters
- Ruff for linting (E, F, I, W rules) and formatting
- Double quotes for strings
