"""Summarize fictional events with key, type and total checks."""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path


REQUIRED = {"record_id", "period", "segment", "value"}


def summarize(path: Path) -> tuple[list[tuple[str, str, int, Decimal]], Decimal]:
    counts: dict[tuple[str, str], int] = defaultdict(int)
    amounts: dict[tuple[str, str], Decimal] = defaultdict(lambda: Decimal("0"))
    seen: set[tuple[str, str]] = set()
    source_total = Decimal("0")

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or set(reader.fieldnames) != REQUIRED:
            raise ValueError(f"Expected columns: {sorted(REQUIRED)}")
        rows = 0
        for row in reader:
            rows += 1
            rid, period, segment = (row[key].strip() for key in ("record_id", "period", "segment"))
            if not rid or not segment or len(period) != 7 or period[4] != "-" or not period[:4].isdigit() or not period[5:].isdigit() or not (1 <= int(period[5:]) <= 12):
                raise ValueError(f"Invalid identifier, segment or period on data row {rows}")
            key = (rid, period)
            if key in seen:
                raise ValueError(f"Duplicate record-period key on data row {rows}")
            seen.add(key)
            try:
                amount = Decimal(row["value"].strip())
            except (InvalidOperation, AttributeError) as exc:
                raise ValueError(f"Invalid decimal on data row {rows}") from exc
            if not amount.is_finite() or amount < 0:
                raise ValueError(f"Non-finite or negative value on data row {rows}")
            group = (period, segment)
            counts[group] += 1
            amounts[group] += amount
            source_total += amount

    if not rows:
        raise ValueError("Input file contains no data rows")
    result = [(p, s, counts[(p, s)], amounts[(p, s)]) for p, s in sorted(counts)]
    if sum((amount for _, _, _, amount in result), Decimal("0")) != source_total:
        raise AssertionError("Grouped amounts do not reconcile")
    if sum(count for _, _, count, _ in result) != rows:
        raise AssertionError("Grouped counts do not reconcile")
    return result, source_total


def main() -> int:
    parser = argparse.ArgumentParser(description="Synthetic CSV summary; no database access.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    rows, total = summarize(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["period", "segment", "case_count", "amount"])
        for period, segment, count, amount in rows:
            writer.writerow([period, segment, count, f"{amount:.2f}"])
    temporary.replace(args.output)
    print(f"Groups: {len(rows)}; total: {total:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
