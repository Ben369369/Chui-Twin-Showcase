"""Check that each sealed forecast file still matches the hash published before the outcome.

Usage: python verify_seal.py
The Bitcoin timestamp itself is checked separately: drop the .json and its .ots proof
on https://opentimestamps.org.
"""

import hashlib
import json
from pathlib import Path

PUBLISHED = {
    "DAL_20261002T205817+0000_f6892ab93661.json":
        "f6892ab9366122fd81b64c1106b052c1962638c6ab8644587c5baee2d2058bd8",
    "CMG_20261018T190051+0000_fabe5e811fcf.json":
        "fabe5e811fcf5fe2e0b909a5d7c7e6ff5e69a8ee691645214ec7e816c0016282",
}

SEALED = Path(__file__).parent / "forecasts" / "sealed"

ok = True
for name, expected in PUBLISHED.items():
    path = SEALED / name
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    match = digest == expected
    ok &= match
    record = json.loads(path.read_text(encoding="utf-8"))
    print(f"{'OK  ' if match else 'FAIL'} {record['ticker']} sealed {record['sealed_at']}  {digest}")
    for kpi, periods in sorted(record["forecast"].items()):
        for period, f in sorted(periods.items()):
            print(f"       {kpi:15s} {period}  median {f['p50']:6.2f}   80% range {f['p10']:6.2f} to {f['p90']:6.2f}")

raise SystemExit(0 if ok else 1)
