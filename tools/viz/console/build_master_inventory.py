#!/usr/bin/env python3
"""
Master falsifier inventory builder.

Parses `sessions/framework/registry/falsifier-watchlist.md` — the authoritative live
falsifier-watch registry — and emits a structured JSON inventory keyed for
the Gantt-timeline view.

Source has two layers:
  1. Summary table (lines 21–27) — concise: Test, Framework prediction,
     Instrument, Data year, σ from LCDM, Status.
  2. Post-W4 Unified Schema (lines 95–169) — per-row 8-column unified
     entries: prediction, sigma_pred, detector, sigma_detect,
     sigma_distance, xcorr_class, evoi_class, fisher_sha.

Output schema (per row):
  {
    "prediction_id":       "w_0",
    "observable":          "dark-energy equation of state (zeroth moment)",
    "framework_prediction":"-0.918 (Volovik partition)",
    "framework_gate":      "S58 Volovik-partition; baseline-findings-s66",
    "detector":            "DESI DR3",
    "t_low":               2026.5,        # decimal years
    "t_high":              2027.5,
    "sigma_distance":      "+3.28σ",
    "xcorr_class":         "PARTIALLY_CORRELATED ...",
    "evoi_class":          "FLAGSHIP",
    "evoi_rank":           1,             # 1 = highest priority for Gantt sort
    "status":              "LIVE",
    "fisher_sha":          "WARRANT-DEFERRED",
  }

Output:
  tools/viz/console/master_inventory.json
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent.parent
WATCHLIST = ROOT / "sessions" / "framework" / "registry" / "falsifier-watchlist.md"
OUT = ROOT / "tools" / "viz" / "console" / "master_inventory.json"

CURRENT_YEAR = datetime.now().year


# ---------------------------------------------------------------------------
# EVOI ordering — lower = higher priority on the Gantt
# ---------------------------------------------------------------------------
EVOI_RANK = {
    "FLAGSHIP":         1,
    "FLAGSHIP-JOINT":   2,
    "SECONDARY":        3,
    "DERIVED":          4,
    "LONG-TERM":        5,
    "CONTINGENT":       6,
}


# ---------------------------------------------------------------------------
# Date-window parsing
# ---------------------------------------------------------------------------

def parse_year_window(raw: str) -> tuple[float, float]:
    """Convert a 'Data year' field to (t_low, t_high) decimal years.

    Handles:
      "~2027"       → (2026.5, 2027.5)
      "~2030"       → (2029.5, 2030.5)
      "~2030s"      → (2030.0, 2039.0)
      "now"         → (current_year, current_year)
      "S59+"        → (current_year, current_year + 1)   [computed-now]
      "post-2030"   → (2030, 2040)
      "2027–2030"   → (2027, 2030)
    """
    s = (raw or "").strip().lower()
    if not s:
        return (CURRENT_YEAR, CURRENT_YEAR)

    if s == "now":
        return (CURRENT_YEAR, CURRENT_YEAR)

    # decade form e.g. "~2030s"
    m = re.search(r"(\d{4})\s*s\b", s)
    if m:
        y = int(m.group(1))
        return (float(y), float(y + 9))

    # "post-YYYY"
    m = re.search(r"post[\s-]*(\d{4})", s)
    if m:
        y = int(m.group(1))
        return (float(y), float(y + 10))

    # "YYYY-YYYY" or "YYYY–YYYY"
    m = re.search(r"(\d{4})\s*[–\-]\s*(\d{4})", s)
    if m:
        return (float(m.group(1)), float(m.group(2)))

    # "~YYYY"
    m = re.search(r"~?\s*(\d{4})", s)
    if m:
        y = int(m.group(1))
        return (y - 0.5, y + 0.5)

    # session-anchor only ("S59+", "RGE computation", ...)
    return (float(CURRENT_YEAR), float(CURRENT_YEAR + 1))


# ---------------------------------------------------------------------------
# Markdown parsing
# ---------------------------------------------------------------------------

SUMMARY_ROW_RE = re.compile(
    r"^\|\s*`?(?P<id>[^|`]+?)`?\s*\|"
    r"\s*(?P<pred>[^|]+?)\s*\|"
    r"\s*(?P<inst>[^|]+?)\s*\|"
    r"\s*(?P<year>[^|]+?)\s*\|"
    r"\s*(?P<sigma>[^|]+?)\s*\|"
    r"\s*(?P<status>[^|]+?)\s*\|",
    re.M,
)
ENTRY_DETAIL_RE = re.compile(
    r"###\s+`?(?P<id>[^`\n]+?)`?\s*(?:—\s*(?P<obs>[^\n]+))?\n(?P<body>(?:(?!\n###|\n##\s).)+)",
    re.S,
)
UNIFIED_RE = re.compile(
    r"####\s+`?(?P<id>[^`\n]+?)`?\s*\n(?P<body>(?:(?!\n####|\n##\s|\n---).)+)",
    re.S,
)


def first_field(body: str, label: str) -> str:
    """Return the value of `- **label**: ...` in a markdown bullet list."""
    pat = rf"\*\*{re.escape(label)}\*\*\s*:\s*(.+?)(?=\n\s*-\s*\*\*|\n\n|\Z)"
    m = re.search(pat, body, re.S | re.I)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1)).strip()


def parse_watchlist(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    rows: dict[str, dict] = {}

    # 1. Summary table — establishes prediction_id + Data year + Status.
    in_table = False
    for line in text.splitlines():
        if line.startswith("| Test |"):
            in_table = True
            continue
        if in_table and (not line.startswith("|") or line.startswith("|:")):
            in_table = False if not line.startswith("|") else in_table
            continue
        if in_table:
            cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
            if len(cells) < 6:
                continue
            pid = cells[0]
            if pid.lower() == "test":
                continue
            t_low, t_high = parse_year_window(cells[3])
            rows[pid] = {
                "prediction_id":        pid,
                "observable":           "",
                "framework_prediction": cells[1],
                "framework_gate":       "",
                "detector":             cells[2],
                "data_year":            cells[3],
                "t_low":                t_low,
                "t_high":               t_high,
                "sigma_distance":       cells[4],
                "xcorr_class":          "",
                "evoi_class":           "",
                "evoi_rank":            99,
                "status":               cells[5],
                "fisher_sha":           "",
            }

    # 2. Entry detail — pulls observable + framework_gate (Source / Session anchor).
    detail_blocks = re.split(r"\n###\s+", text)
    for chunk in detail_blocks[1:]:
        m_id = re.match(r"`?([^`\n]+?)`?\s*(?:—\s*([^\n]+))?\n", chunk)
        if not m_id:
            continue
        pid = m_id.group(1).strip().strip("`")
        obs = (m_id.group(2) or "").strip()
        body = chunk[m_id.end():]
        if pid not in rows:
            continue
        if obs and not rows[pid]["observable"]:
            rows[pid]["observable"] = obs
        src = first_field(body, "Source") or first_field(body, "Session anchor")
        if src:
            rows[pid]["framework_gate"] = src

    # 3. Post-W4 Unified Schema — overwrites with structured 8-column data.
    for chunk in re.split(r"\n####\s+", text)[1:]:
        m_id = re.match(r"`?([^`\n]+?)`?\s*\n", chunk)
        if not m_id:
            continue
        pid = m_id.group(1).strip().strip("`")
        body = chunk[m_id.end():]
        if pid not in rows:
            # Add a row inferred from the unified block alone.
            rows[pid] = {
                "prediction_id":        pid,
                "observable":           "",
                "framework_prediction": "",
                "framework_gate":       "",
                "detector":             "",
                "data_year":            "",
                "t_low":                CURRENT_YEAR,
                "t_high":               CURRENT_YEAR,
                "sigma_distance":       "",
                "xcorr_class":          "",
                "evoi_class":           "",
                "evoi_rank":            99,
                "status":               "LIVE",
                "fisher_sha":           "",
            }
        for key, label in (
            ("framework_prediction", "prediction"),
            ("detector",             "detector"),
            ("sigma_distance",       "sigma_distance"),
            ("xcorr_class",          "xcorr_class"),
            ("evoi_class",           "evoi_class"),
            ("fisher_sha",           "fisher_sha"),
        ):
            v = first_field(body, label)
            if v:
                rows[pid][key] = v

    # EVOI rank: numeric for sorting; lower-is-better; the first token of
    # multi-flag classes (e.g. "FLAGSHIP (CMB-S4) / SECONDARY (CMB-HD)") wins.
    for r in rows.values():
        cls_raw = r["evoi_class"].upper().strip()
        first = re.split(r"[\s/(]", cls_raw, 1)[0] if cls_raw else ""
        first = first.strip("., ")
        r["evoi_rank"] = EVOI_RANK.get(first, 99)

    # Sort: EVOI rank ascending, then t_low ascending.
    return sorted(rows.values(), key=lambda r: (r["evoi_rank"], r["t_low"], r["prediction_id"]))


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main() -> None:
    if not WATCHLIST.exists():
        print(f"[build_master_inventory] ERROR: {WATCHLIST} not found.")
        raise SystemExit(1)
    rows = parse_watchlist(WATCHLIST)
    payload = {
        "generated_from": "tools/viz/console/build_master_inventory.py",
        "source":         "sessions/framework/registry/falsifier-watchlist.md",
        "current_year":   CURRENT_YEAR,
        "rows":           rows,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[build_master_inventory] {len(rows)} rows")
    for r in rows:
        print(
            f"  {r['prediction_id']:18s}  EVOI={r['evoi_class'][:18]:18s}"
            f"  {r['detector'][:24]:24s}  [{r['t_low']:.1f}–{r['t_high']:.1f}]"
        )
    print(f"  -> {OUT} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
