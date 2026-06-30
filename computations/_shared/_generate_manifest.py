#!/usr/bin/env python3
"""
_generate_manifest.py — ARTIFACTS PROMISED JSON block generator (S84 W9a-102)

Provenance
----------
Originally created at .claude/skills/rclab-review/generate_manifest.py
(commit b9b3394, S84 W9a-102, 2026-04-19). Relocated to computations/_shared/
in S88 (2026-05-07) per shared-infrastructure naming convention (_-prefix;
matches sibling _yaml_gate_validator.py + _pru_cardinality_audit.py + the
broader _xxx_audit.py family). The script's consumer is /rclab-coordinate
(compute-mode dispatch), not /rclab-review (solo synthesis); it never
logically belonged in the review skill folder. The verdict-file path pin
in the docstring below is also corrected per gate-verdicts.md canonical
location rule (computations/session-{N}/, not computations/_shared/).

Purpose
-------
Read a gate's pre-registration block (R3 YAML or 13-field markdown equivalent)
from a session plan file and emit a canonical `## ARTIFACTS PROMISED` JSON
block for insertion into compute-mode dispatch prompts. Also supports
spot-auditing existing prompt files against their gate declarations.

The generator consumes `_yaml_gate_validator.py` (W9a-100 dependency, sibling
in computations/_shared/) to parse gate blocks in both markdown and YAML
formats, then extracts:
  - gate_id             — canonical gate ID
  - script              — from gate.method.producing_script
  - verdict_line_target — always computations/session-{N}/s{N}_gate_verdicts.txt
                          per .claude/rules/gate-verdicts.md canonical-path rule
  - data_files          — regex on method body for .npz|.npy|.json|.csv|.yaml|.txt
  - plot_files          — regex on method body for .png|.pdf|.svg
  - working_paper_sections — gate section ID + WP path + min_lines

Modes
-----
  --emit-prompt-block : markdown + fenced-json block (default)
  --emit-json         : raw manifest JSON (one line per gate)
  --audit <dir>       : spot-audit prompts in <dir>, emit audit JSON

Usage
-----
    python computations/_shared/_generate_manifest.py \\
        --plan <plan.md> --gate-slug W9a-102 \\
        --session-n 84 --wp <workingpaper.md> --emit-prompt-block

    python computations/_shared/_generate_manifest.py \\
        --audit sessions/session-N/prompts/ \\
        --sample-fraction 0.10 --sample-floor 2 \\
        --out sessions/session-N/manifest_auto_audit.json

No framework constants imported (NON-PHONONIC methodology tool).
Computed intermediates tagged `# (local)` per .claude/rules/math-scripts.md.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU thread cap

import argparse
import json
import random
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Import the R3 validator for gate parsing — sibling module in this directory.
_THIS_DIR = Path(__file__).resolve().parent  # (local) computations/_shared/
sys.path.insert(0, str(_THIS_DIR))
import _yaml_gate_validator as YGV  # noqa: E402

# --- Pre-registration pins (S84 W9a-102) ---
MANIFEST_BLOCK_HEADER = "## ARTIFACTS PROMISED"  # PIN
MANIFEST_JSON_KEYS = [
    "gate_id",
    "script",
    "verdict_line_target",
    "data_files",
    "plot_files",
    "working_paper_sections",
]  # PIN
SPOT_AUDIT_SAMPLE_FRACTION = 0.10  # (local) PIN — S84 W9a-102 audit sampling fraction
SPOT_AUDIT_SAMPLE_FLOOR = 2  # (local) PIN — minimum prompts to sample regardless of fraction
WORKING_PAPER_SECTION_MIN_LINES = 15  # (local) PIN — from agent-standards.md stub threshold

# --- File-extension patterns for data/plot extraction ---
DATA_EXT_RE = re.compile(
    r"[A-Za-z0-9_\-./]+?\.(npz|npy|json|csv|yaml|yml|txt)\b", re.IGNORECASE
)
PLOT_EXT_RE = re.compile(
    r"[A-Za-z0-9_\-./]+?\.(png|pdf|svg)\b", re.IGNORECASE
)
SCRIPT_RE = re.compile(
    r"(?:computations/_shared|\.claude/skills/[A-Za-z0-9_\-]+)/[A-Za-z0-9_\-./]+?\.py\b"
)
VERDICT_FILENAME_RE = re.compile(r"s\d*_?gate_verdicts\.txt")
WP_SECTION_RE = re.compile(r"§\s*([A-Za-z0-9\-.]+)")


# --------------------------------------------------------------------------
# Gate extraction helpers
# --------------------------------------------------------------------------

def _find_gate(plan_path: Path, gate_slug: str) -> Optional[Dict]:
    """Return the parsed gate dict for the given slug, or None."""
    text = plan_path.read_text(encoding="utf-8")  # (local)
    md_gates = YGV._extract_gate_blocks_markdown(text)  # (local)
    for g in md_gates:
        if g["slug"] == gate_slug or gate_slug in g["gate_id"]:
            return g
    # Fallback: YAML-fenced
    yaml_gates = YGV._extract_yaml_gates(text)  # (local)
    for g in yaml_gates:
        if g.get("gate_id") == gate_slug or gate_slug in g.get("gate_id", ""):
            return {"slug": "yaml", "gate_id": g.get("gate_id"), "body": json.dumps(g), "subsections": {}}
    return None


def _extract_producing_script(gate: Dict) -> str:
    """Extract script path from gate.method.producing_script.

    Preference order:
      1. The explicit ### Method block (first hit, matches canonical
         producing_script convention).
      2. Any SCRIPT_RE match in the gate body.
    """
    subs = gate.get("subsections", {})  # (local)
    method_blob = subs.get("Method", "") or subs.get("1. Method", "") or ""  # (local)
    for m in SCRIPT_RE.finditer(method_blob):
        return m.group(0)
    body = gate.get("body", "")  # (local)
    for m in SCRIPT_RE.finditer(body):
        return m.group(0)
    return ""


def _extract_files(body: str, pattern: re.Pattern, blacklist_suffixes=(),
                   blacklist_substrings=()) -> List[str]:
    """Extract all files matching pattern, dedup + preserve order.

    Deduplication prefers the longest path for each basename (so
    `sessions/archive/session-84/foo.json` wins over bare `foo.json`).
    """
    hits = []  # (local) list of (start_idx, path)
    for m in pattern.finditer(body):
        path = m.group(0)  # (local)
        if any(path.endswith(bad) for bad in blacklist_suffixes):
            continue
        if any(bad in path for bad in blacklist_substrings):
            continue
        hits.append((m.start(), path))
    # Dedup by basename, prefer longest path, preserve first-occurrence order
    by_base: Dict[str, str] = {}  # (local)
    first_pos: Dict[str, int] = {}  # (local)
    for pos, path in hits:
        base = path.rsplit("/", 1)[-1]  # (local)
        if base not in by_base or len(path) > len(by_base[base]):
            by_base[base] = path
            first_pos.setdefault(base, pos)
    # Return ordered by first-occurrence of the basename
    order = sorted(by_base.keys(), key=lambda b: first_pos[b])  # (local)
    return [by_base[b] for b in order]


def _extract_wp_sections(gate: Dict, wp_path: str) -> List[Dict]:
    """Derive [{section, path, min_lines}] from the gate slug / body."""
    subs = gate.get("subsections", {})  # (local)
    body = gate.get("body", "")  # (local)
    # Section ID: convention §W{wave}-{index} (e.g., §W9-102)
    slug = gate.get("slug", "")  # (local)
    # Convert W9a-102 -> §W9-102 (the WP section form); W1-3-CN -> §W1-3-CN
    section_id = None  # (local)
    m_wp = re.search(r"§(W[0-9]+[a-z]*-[0-9]+(?:-[A-Z]+)?)", body)  # (local)
    if m_wp:
        section_id = "§" + m_wp.group(1)
    else:
        # Derive from slug: W9a-102 -> W9-102 (strip lowercase wave letter)
        m_slug = re.match(r"(W[0-9]+)[a-z]*(-.+)", slug)  # (local)
        if m_slug:
            section_id = "§" + m_slug.group(1) + m_slug.group(2)
        else:
            section_id = f"§{slug}"
    return [
        {
            "section": section_id,
            "path": wp_path,
            "min_lines": WORKING_PAPER_SECTION_MIN_LINES,
        }
    ]


def build_manifest(
    plan_path: Path,
    gate_slug: str,
    session_n: int,
    wp_path: str,
) -> Dict:
    """Build the 6-key manifest dict for a single gate."""
    gate = _find_gate(plan_path, gate_slug)  # (local)
    if gate is None:
        raise RuntimeError(f"gate_slug '{gate_slug}' not found in {plan_path}")
    body = gate.get("body", "") + "\n" + "\n".join(gate.get("subsections", {}).values())  # (local)
    script = _extract_producing_script(gate)  # (local)
    data_files = _extract_files(
        body, DATA_EXT_RE,
        blacklist_suffixes=("canonical_constants.py",),
        blacklist_substrings=("gate_verdicts", "canonical_constants"),
    )  # (local)
    # Drop the verdict file itself from data_files — it has its own slot
    data_files = [f for f in data_files if not VERDICT_FILENAME_RE.search(f)]
    plot_files = _extract_files(body, PLOT_EXT_RE)  # (local)
    wp_sections = _extract_wp_sections(gate, wp_path)  # (local)
    manifest = {
        "gate_id": gate.get("gate_id", ""),
        "script": script,
        "verdict_line_target": f"computations/_shared/s{session_n}_gate_verdicts.txt",
        "data_files": data_files,
        "plot_files": plot_files,
        "working_paper_sections": wp_sections,
    }
    return manifest


def emit_prompt_block(manifest: Dict) -> str:
    """Render the markdown + fenced-json block ready for prompt insertion."""
    body = json.dumps(manifest, indent=2, ensure_ascii=False)  # (local)
    return f"{MANIFEST_BLOCK_HEADER}\n```json\n{body}\n```"


# --------------------------------------------------------------------------
# Spot audit
# --------------------------------------------------------------------------

def _parse_prompt_manifest(prompt_text: str) -> Tuple[bool, Optional[Dict]]:
    """Extract the ARTIFACTS PROMISED JSON block from a prompt text."""
    # Locate the header
    idx = prompt_text.find(MANIFEST_BLOCK_HEADER)  # (local)
    if idx < 0:
        return False, None
    tail = prompt_text[idx:]  # (local)
    fence_re = re.compile(r"```json\s*\n(.*?)\n```", re.DOTALL)  # (local)
    m = fence_re.search(tail)  # (local)
    if not m:
        return False, None
    try:
        data = json.loads(m.group(1))  # (local)
    except json.JSONDecodeError:
        return False, None
    return True, data


def _audit_single(
    prompt_path: Path, gate_manifest: Optional[Dict]
) -> Dict:
    """Audit one prompt file. Returns per-sample result dict."""
    text = prompt_path.read_text(encoding="utf-8")  # (local)
    present, parsed = _parse_prompt_manifest(text)  # (local)
    well_formed = present and parsed is not None and all(
        k in parsed for k in MANIFEST_JSON_KEYS
    )  # (local)
    if gate_manifest is not None and well_formed:
        accurate = (
            parsed["gate_id"] == gate_manifest["gate_id"]
            and parsed["script"] == gate_manifest["script"]
            and parsed["verdict_line_target"] == gate_manifest["verdict_line_target"]
        )
    else:
        accurate = well_formed  # no reference: structural correctness only
    return {
        "prompt_path": str(prompt_path).replace("\\", "/"),
        "manifest_present": bool(well_formed),
        "manifest_accurate": bool(accurate),
        "per_sample": int(well_formed and accurate),
        "parsed_keys_present": sorted(parsed.keys()) if parsed else [],
        "parsed_gate_id": parsed.get("gate_id") if parsed else None,
    }


def spot_audit(
    prompts_dir: Path,
    sample_fraction: float,
    sample_floor: int,
    gate_manifests: Optional[Dict[str, Dict]] = None,
    seed: int = 1984,
) -> Dict:
    """Audit a directory of prompt files. Returns report dict."""
    rng = random.Random(seed)  # (local)
    all_prompts = sorted(prompts_dir.glob("*.md")) + sorted(prompts_dir.glob("*.txt"))  # (local)
    n_total = len(all_prompts)  # (local)
    n_sample = max(sample_floor, int(round(sample_fraction * n_total)))  # (local)
    n_sample = min(n_sample, n_total)
    if n_total == 0:
        return {
            "n_dispatches": 0,
            "n_sampled": 0,
            "pass_fraction": 0.0,
            "verdict": "FAIL",
            "samples": [],
            "note": "no prompt files found",
        }
    sample = rng.sample(all_prompts, n_sample)  # (local)
    samples = []  # (local)
    for p in sample:
        gm = None  # (local)
        if gate_manifests is not None:
            for gid, m in gate_manifests.items():
                if gid in p.name:
                    gm = m
                    break
        samples.append(_audit_single(p, gm))
    n_pass = sum(s["per_sample"] for s in samples)  # (local)
    pass_fraction = n_pass / len(samples) if samples else 0.0  # (local)
    # Substitution chain: PASS iff ==1.0, INFO iff [0.9,1.0), FAIL if <0.9
    if pass_fraction >= 1.0 - 1e-9:
        verdict = "PASS"  # (local)
    elif pass_fraction >= 0.90:
        verdict = "INFO"  # (local)
    else:
        verdict = "FAIL"  # (local)
    return {
        "n_dispatches": n_total,
        "n_sampled": len(samples),
        "sample_fraction": sample_fraction,
        "sample_floor": sample_floor,
        "seed": seed,
        "pass_fraction": pass_fraction,
        "verdict": verdict,
        "samples": samples,
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="ARTIFACTS PROMISED manifest generator (S84 W9a-102)")
    ap.add_argument("--plan", help="session plan markdown file")
    ap.add_argument("--gate-slug", help="gate slug, e.g. W9a-102")
    ap.add_argument("--session-n", type=int, default=84, help="session number")
    ap.add_argument("--wp", default="", help="working-paper path for wp_sections[0].path")
    ap.add_argument("--emit-prompt-block", action="store_true",
                    help="emit markdown + fenced-json block (default)")
    ap.add_argument("--emit-json", action="store_true",
                    help="emit raw JSON manifest")
    ap.add_argument("--audit", help="spot-audit prompts in this directory")
    ap.add_argument("--sample-fraction", type=float, default=SPOT_AUDIT_SAMPLE_FRACTION)
    ap.add_argument("--sample-floor", type=int, default=SPOT_AUDIT_SAMPLE_FLOOR)
    ap.add_argument("--out", help="write output to this file (default: stdout)")
    args = ap.parse_args(argv)

    # --- Audit mode ---
    if args.audit:
        d = Path(args.audit)  # (local)
        if not d.exists() or not d.is_dir():
            print(f"ERROR: audit dir not found: {args.audit}", file=sys.stderr)
            return 2
        report = spot_audit(d, args.sample_fraction, args.sample_floor)  # (local)
        blob = json.dumps(report, indent=2)  # (local)
        if args.out:
            Path(args.out).write_text(blob, encoding="utf-8")
        else:
            print(blob)
        return 0 if report["verdict"] in ("PASS", "INFO") else 1

    # --- Build single-gate manifest ---
    if not args.plan or not args.gate_slug:
        print("ERROR: --plan and --gate-slug required (or use --audit)", file=sys.stderr)
        return 2
    plan_p = Path(args.plan)  # (local)
    if not plan_p.exists():
        print(f"ERROR: plan file not found: {args.plan}", file=sys.stderr)
        return 2
    manifest = build_manifest(plan_p, args.gate_slug, args.session_n, args.wp)  # (local)
    if args.emit_json:
        blob = json.dumps(manifest, indent=2)  # (local)
    else:
        blob = emit_prompt_block(manifest)  # (local)
    if args.out:
        Path(args.out).write_text(blob, encoding="utf-8")
    else:
        print(blob)
    return 0


if __name__ == "__main__":
    sys.exit(main())
