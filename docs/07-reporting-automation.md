# Python in Analytics and Reporting Automation

A practical, generic workflow: **input → validation → transformation → reconciliation → report → QA**. In production, each stage has an approved owner, data-access boundary and source reference. This guide uses invented records only.

## What Python contributes

| Task | Typical tools | Important control |
|---|---|---|
| Import CSV / Excel | `csv`, `pathlib`, optional `pandas` / `openpyxl` | Schema, types, encoding, unexpected empty input |
| Inspect read-only SQL exports | Approved DB client or downloaded test fixture | Source grain, observation date and join cardinality |
| Transform and aggregate | Standard library, pandas / NumPy where appropriate | Additive amounts before ratios; duplicate checks |
| Produce workbook | `openpyxl` or Excel-native templates | Preserve formulas, pivots and existing styles |
| Build presentation | `python-pptx` when appropriate | Verify content, chart sources and visual render |
| Schedule processing | Windows BAT, Task Scheduler, Bash, CI runner | Failure status, logs and deterministic reruns |
| Publish a result | Git PR, reviewed artifact | Never include confidential exports in commits |

## One reproducible synthetic exercise

Run `python examples/synthetic_summary.py --input examples/data/demo_events.csv --output output/summary.csv`. The example relies only on Python's standard library; it validates input fields, numeric values, unique event-period keys and reconciles aggregated totals.

Expected fictional input totals: ALPHA = **17.50**, BETA = **7.00**, all segments = **24.50**. These are fixture expectations, not operational KPI values.

The script deliberately **fails** on duplicate keys or malformed numbers. A zero denominator, a missing reporting period and a schema mismatch must be reported, not silently converted into a believable percentage.

## SQL and BAT integration without leaking credentials

A Windows BAT file is a launcher: it can call an authorized **read-only** SQL tool, verify that a new export exists and invoke Python. The SQL client and its authentication method are configured **outside** a public repository. Do not embed passwords, wallet files, DSNs, remote hostnames, or employer-owned SQL here.

```bat
@echo off
setlocal
py -3 examples\synthetic_summary.py --input examples\data\demo_events.csv --output output\summary.csv
if errorlevel 1 exit /b 1
echo Synthetic reporting step passed.
```

The example above runs solely against committed fake CSV data. The analogous Linux workflow is in the [Linux automation guide](https://github.com/KonstantinOreshnikov/linux-testing-python).

## QA checklist

Check input and output row counts, unique keys, date coverage, null/invalid values, sums at both grand-total and segment levels, idempotent results and error exits. A green process exit is not proof that a report is right unless acceptance totals have also been checked.

**RU:** Python для CSV/Excel/SQL-выгрузок, Data Quality, агрегирования, автоматического обновления отчётов и запуска из BAT. Практическая реализация полностью синтетическая.

References: [Python CSV](https://docs.python.org/3/library/csv.html), [Decimal](https://docs.python.org/3/library/decimal.html), [subprocess](https://docs.python.org/3/library/subprocess.html).
