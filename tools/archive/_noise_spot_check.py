"""5% random spot check of NOISE classifications across all 10 anchor-validation tables.

For each table, samples max(ceil(5% * |NOISE|), 2) entries (or all if <= 20),
then for each sampled entry shows:
  - anchor_id, name, source_file
  - Haiku NOISE reason
  - 8 lines of source context (what Haiku actually saw)
  - Heuristic spot-check judgment (AGREE / DISAGREE / BORDERLINE)

Output path embeds the seed so different seeds don't overwrite each other:
  --seed 42 (default)  -> tools/_noise_spot_check.md
  --seed 43            -> tools/_noise_spot_check_seed43.md
"""
import argparse
import json
import random
import re
from pathlib import Path
from math import ceil

ROOT = Path(".")
AGG_PATH = ROOT / "tools" / "_anchor_validation_results.json"
BATCH = ROOT / "tools" / "anchor_validation_batches"

_ap = argparse.ArgumentParser()
_ap.add_argument("--seed", type=int, default=42)
_ap.add_argument("--pct", type=float, default=0.05, help="Sample fraction per table")
_args = _ap.parse_args()

random.seed(_args.seed)
SEED = _args.seed
SAMPLE_PCT = _args.pct

if SEED == 42:
    OUT = ROOT / "tools" / "_noise_spot_check.md"
else:
    OUT = ROOT / "tools" / f"_noise_spot_check_seed{SEED}.md"

agg = json.loads(AGG_PATH.read_text(encoding="utf-8"))

# Build unified anchor_id -> info dict from all batch files
all_idx = {}
for b in sorted(BATCH.glob("*.json")):
    try:
        payload = json.loads(b.read_text(encoding="utf-8"))
    except Exception:
        continue
    for a in payload.get("anchors", []):
        aid = a.get("anchor_id")
        if not aid:
            continue
        all_idx[aid] = {
            "table": payload.get("table"),
            "name": (a.get("name") or "").replace("\n", " ").replace("\r", " "),
            "context": a.get("source_context_30_lines", ""),
            "source_file": a.get("source_file"),
            "status": a.get("status"),
            "statement": (a.get("statement") or "").replace("\n", " ")[:200],
            "path": a.get("path"),
            "batch_file": b.name,
        }


def classify(entry):
    """Heuristic spot-check judgment of whether Haiku NOISE call was correct.

    Approach: identify document-type from source_context, then apply
    context-aware classification. The branches are mutually exclusive and
    ordered by specificity (most-specific first).
    """
    nm = entry.get("name") or ""
    ctx = entry.get("context") or ""
    stmt = entry.get("statement") or ""
    nm_strip = nm.strip()

    # --- Context-type detection (used by multiple branches below) ---
    # Markdown-table: many pipe chars overall AND at least one pipe in the
    # first 300 chars of context (i.e., the cell row is near the match line).
    ctx_lines = ctx.splitlines()
    pipe_lines = sum(1 for ln in ctx_lines if ln.lstrip().startswith("|") or " | " in ln)
    is_table_ctx = pipe_lines >= 2 or (ctx.count("|") >= 8 and "|" in ctx[:300])

    # Verdict-file: characteristic structure with gate_name / gate_verdict / gate_detail
    is_verdict_ctx = any(k in ctx for k in ("gate_name", "gate_verdict", "gate_detail",
                                            "audit_sha256", "schema_version", "PASS --"))

    # YAML / pin-block: lines of the form `<key>=<value>` or `<key>: <value>`
    yaml_pin_lines = sum(1 for ln in ctx_lines if re.search(r"^\s*\d+:\s*\S+\s*[=:]\s*", ln))
    is_yaml_ctx = yaml_pin_lines >= 3

    # Bullet inside theorem: a bullet ("- foo") on the matching line
    is_bullet_ctx = bool(re.search(r"^\s*\d+:\s*-\s", ctx, re.MULTILINE))

    # Theorem-marker context: explicit **Theorem** or "Theorem" header markers
    has_theorem_marker = bool(re.search(r"\*\*[A-Z]\w*\s*[Tt]heorem", ctx)) or \
                         bool(re.search(r"####?\s*\d*\.?\s*[A-Z]+\s*THEOREM", ctx))

    # === Branch 1: Bare ID fragments / wave labels ===
    if re.fullmatch(r"[A-Z]{1,3}-\d{1,3}[a-z]?", nm_strip):
        return "AGREE", "bare ID fragment (e.g. KC-2, L-1)"

    # === Branch 2: Status / placeholder words ===
    if nm_strip in {
        "PENDING", "CONVERGED", "TBD", "N/A", "None", "PERMANENT",
        "PASS", "FAIL", "PROVEN", "CLOSED", "—", "NEW", "OPEN",
    }:
        return "AGREE", "status-marker-only string"

    # === Branch 3: Bare number / cell-value ===
    if re.fullmatch(r"-?\d+(\.\d+)?", nm_strip):
        return "AGREE", "bare number"
    if re.fullmatch(r"[+\-]?\d+", nm_strip):
        return "AGREE", "bare signed integer (cell value)"

    # === Branch 4: Literal placeholder text ===
    if any(p in nm for p in ["<Registry Name>", "<placeholder>", "<name>", "TODO", "FIXME"]):
        return "AGREE", "literal placeholder text"

    # === Branch 5: Markdown table cell (name+statement both look like cells) ===
    if len(nm) < 60 and stmt and re.fullmatch(r"[+\-]?\d+(\.\d+)?", stmt.strip()):
        return "AGREE", "markdown table row (name=cell, statement=numeric value)"

    # === Branch 6: YAML pin / convention-tag (`scheme=...`, `convention=...`) ===
    if re.search(r"^(scheme|convention|value|tier_pin|content_sha256|audit_sha256)\s*=", nm_strip):
        return "AGREE", "YAML pin / convention-tag (not a mathematical equation)"

    # === Branch 7: Constant assignment with bracketed annotation ===
    #     pattern: `name = value  [<annotation>]`  -- canonical_constants entries
    if re.search(r"^\w[\w_]*\s*=\s*\S+\s*\[", nm_strip):
        return "AGREE", "annotated constant assignment (e.g. canonical_constants pin)"

    # === Branch 8: Verdict-file output line (`R(0) = 4.000`, etc.) ===
    if is_verdict_ctx and "=" in nm and len(nm) < 60:
        return "AGREE", "numerical result line in gate verdict-file output"

    # === Branch 9: Name appears in a markdown table context (cell-extraction) ===
    if is_table_ctx and len(nm) < 80:
        return "AGREE", "name extracted from markdown table cell (context shows table structure)"

    # === Branch 10: Name appears as a bullet inside a larger theorem statement ===
    if is_bullet_ctx and len(nm) < 100:
        return "AGREE", "name extracted as bullet sub-clause inside larger theorem/proof"

    # === Branch 11: Name is an algebraic identity (real math) NOT in a table/bullet ===
    has_math = any(c in nm for c in "=±≈⊗∇∂∫^") or "(x)" in nm
    if has_math and len(nm) > 10:
        # By now: not table, not bullet, not verdict-file, not YAML pin.
        # Could legitimately be a standalone identity statement.
        return "DISAGREE", "algebraic identity with no table/bullet/verdict/pin context"

    # === Branch 12: Short section-heading-like name, no table context ===
    if len(nm) < 50 and nm and nm[:1].isupper() and nm.count(" ") <= 5:
        if has_theorem_marker:
            return "BORDERLINE", "short title; context has explicit Theorem marker nearby"
        return "BORDERLINE", "short title; insufficient evidence to judge"

    # === Branch 13: Long prose-like name (potentially a real theorem statement) ===
    if len(nm) > 100 and "." in nm and " " in nm:
        return "BORDERLINE", "prose-length name; may be theorem or narrative fragment"

    return "BORDERLINE", "uncertain"


# Tables in fixed order
TABLES = [
    "closed_mechanisms", "open_channels", "theorems", "gates",
    "data_provenance", "session_files", "equations",
    "researchers", "constants", "registries",
]

# Header
report = [
    "# NOISE Spot Check — 5% random sample per table",
    "",
    f"Random seed: {SEED} (deterministic; rerun produces identical sample).",
    f"Sample rule: max(ceil({SAMPLE_PCT*100:.1f}% * |NOISE|), 2) per table; tables with <= 20 NOISE include ALL entries.",
    "",
    "## Summary",
    "",
]

per_table = []
detail = []

for t in TABLES:
    noise_ids = sorted([aid for aid, v in agg.get(t, {}).items() if v["verdict"] == "NOISE"])
    n = len(noise_ids)
    if n == 0:
        per_table.append((t, 0, 0, {}))
        continue
    if n <= 20:
        sample = noise_ids
    else:
        k = max(ceil(SAMPLE_PCT * n), 2)
        sample = random.sample(noise_ids, k)

    classifications = {}
    sec = [f"## Table: {t}  -  sampled {len(sample)} of {n} NOISE ({len(sample)/n*100:.1f}%)", ""]
    for aid in sample:
        entry = all_idx.get(aid, {})
        v = agg[t][aid]
        reason = v.get("reason", "") or ""
        bucket, sub_reason = classify(entry)
        classifications[bucket] = classifications.get(bucket, 0) + 1
        sec.append(f"### {aid}")
        sec.append(f"- **name**: {entry.get('name','<missing>')[:200]}")
        sec.append(f"- **source_file**: {entry.get('source_file') or '<?>'}")
        if entry.get("statement"):
            sec.append(f"- **statement (DB field)**: {entry['statement'][:200]}")
        sec.append(f"- **Haiku NOISE reason**: {reason[:200]}")
        sec.append(f"- **Spot-check judgment**: **{bucket}**  -  {sub_reason}")
        sec.append(f"- **source_context (first 8 lines)**:")
        ctx_lines = (entry.get("context") or "").splitlines()
        for ln in ctx_lines[:8]:
            sec.append(f"    {ln[:220]}")
        if len(ctx_lines) > 8:
            sec.append(f"    ... +{len(ctx_lines)-8} more lines")
        sec.append("")
    per_table.append((t, n, len(sample), classifications))
    detail.append("\n".join(sec))

# Summary table
report.append("| Table | NOISE total | Sampled | AGREE | DISAGREE | BORDERLINE |")
report.append("|:------|----:|----:|----:|----:|----:|")
total_agree = total_disagree = total_border = total_sampled = total_noise = 0
for t, n, k, cls in per_table:
    if n == 0:
        report.append(f"| {t} | 0 | 0 | - | - | - |")
        continue
    a = sum(c for b, c in cls.items() if b == "AGREE")
    d = sum(c for b, c in cls.items() if b == "DISAGREE")
    br = sum(c for b, c in cls.items() if b == "BORDERLINE")
    total_agree += a; total_disagree += d; total_border += br
    total_sampled += k; total_noise += n
    report.append(f"| {t} | {n} | {k} | {a} | {d} | {br} |")
report.append(f"| **TOTAL** | **{total_noise}** | **{total_sampled}** | **{total_agree}** | **{total_disagree}** | **{total_border}** |")
report.append("")
if total_sampled:
    agree_pct = 100 * total_agree / total_sampled
    disagree_pct = 100 * total_disagree / total_sampled
    border_pct = 100 * total_border / total_sampled
    report.append(f"Spot-check agreement: {agree_pct:.1f}% AGREE, {disagree_pct:.1f}% DISAGREE, {border_pct:.1f}% BORDERLINE.")
report.append("")
report.append("---")
report.append("")
report.extend(detail)

OUT.write_text("\n".join(report), encoding="utf-8")
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
print()
print("=" * 80)
print("SPOT-CHECK SUMMARY")
print("=" * 80)
print(f"{'table':<22}{'NOISE':>7}{'sampled':>9}{'agree':>7}{'disagr':>8}{'border':>8}")
for t, n, k, cls in per_table:
    if n == 0:
        print(f"{t:<22}{0:>7}{0:>9}{'-':>7}{'-':>8}{'-':>8}")
        continue
    a = sum(c for b, c in cls.items() if b == "AGREE")
    d = sum(c for b, c in cls.items() if b == "DISAGREE")
    br = sum(c for b, c in cls.items() if b == "BORDERLINE")
    print(f"{t:<22}{n:>7}{k:>9}{a:>7}{d:>8}{br:>8}")
print("-" * 80)
print(f"{'TOTAL':<22}{total_noise:>7}{total_sampled:>9}{total_agree:>7}{total_disagree:>8}{total_border:>8}")
if total_sampled:
    print(f"agreement: {agree_pct:.1f}% / disagree: {disagree_pct:.1f}% / borderline: {border_pct:.1f}%")
