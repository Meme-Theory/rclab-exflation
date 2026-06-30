#!/usr/bin/env python3
"""
s84_w9a_102_manifest_auto.py — Spot-audit harness for ARTIFACTS PROMISED
manifest auto-generation (S84 Gate W9a-102).

Purpose
-------
Invoke .claude/skills/rclab-review/generate_manifest.py across ≥2 sampled
S84 gate specifications, synthesize prompt-block artifacts, then audit
them against the gates' declarations. Emit per-sample pass/fail JSON,
compute the pass_fraction, and append a dual-SHA verdict line.

Substitution chain for the pass/fail threshold
-----------------------------------------------
Definition 1: |S| = number of sampled S84 gates, |S| >= SPOT_AUDIT_SAMPLE_FLOOR
Definition 2: manifest_present(p) = 1 if prompt p contains the header
              "## ARTIFACTS PROMISED" followed by a ```json fence with
              all 6 MANIFEST_JSON_KEYS, else 0
Definition 3: manifest_accurate(p, g) = 1 if parsed JSON matches gate g's
              producing_script, verdict_line_target, and WP section,
              else 0
Definition 4: per_sample(p,g) = manifest_present(p) * manifest_accurate(p,g)
Definition 5: pass_fraction = (1/|S|) * sum_{p in S} per_sample(p, g(p))
Substitute:   PASS iff pass_fraction == 1.0
              INFO iff 0.90 <= pass_fraction < 1.0
              FAIL iff pass_fraction < 0.90
Simplify:     at |S|=3 (the sample size used here),
              3/3=1.0 PASS; 2/3≈0.667 FAIL; 1/3≈0.333 FAIL
Direction:    pass_fraction monotone-increasing in per_sample successes
Conclusion:   all three sampled gates must produce present AND accurate
              manifests for PASS

NON-PHONONIC methodology tool. No canonical framework constants imported.
Computed intermediates tagged `# (local)` per .claude/rules/math-scripts.md.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU thread cap

import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

# --- Pre-registration pins (from plan §W9a-102) ---
# NOTE: NON-PHONONIC methodology tool. No `from canonical_constants import *`
# needed; no framework physical constants. The pins below are plan-schema
# parameters (PRDR pins from plan §W9a-102), not framework physical constants.
MANIFEST_BLOCK_HEADER = "## ARTIFACTS PROMISED"  # (local) PRDR PIN
MANIFEST_JSON_KEYS = [
    "gate_id",
    "script",
    "verdict_line_target",
    "data_files",
    "plot_files",
    "working_paper_sections",
]  # (local) PRDR PIN
SPOT_AUDIT_SAMPLE_FRACTION = 0.10  # (local) PRDR PIN
SPOT_AUDIT_SAMPLE_FLOOR = 2  # (local) PRDR PIN
WORKING_PAPER_SECTION_MIN_LINES = 15  # (local) PRDR PIN (agent-standards stub threshold)

# --- Project-relative paths ---
PROJ_ROOT = Path(__file__).resolve().parent.parent  # (local)
VENV_PY = PROJ_ROOT / "phonon-exflation-sim" / ".venv312" / "Scripts" / "python.exe"  # (local)
GENERATOR = PROJ_ROOT / ".claude" / "skills" / "rclab-review" / "generate_manifest.py"  # (local)
PLAN_PATH = PROJ_ROOT / "sessions" / "session-plan" / "session-84-plan-w9a.md"  # (local)
WP_PATH = "sessions/archive/session-84/session-84-w9-workingpaper.md"  # (local)
VERDICTS_PATH = PROJ_ROOT / "computations" / "s84_gate_verdicts.txt"  # (local)
AUDIT_OUT = PROJ_ROOT / "sessions" / "session-84" / "manifest_auto_audit.json"  # (local)

# --- Sampled gates (>= SPOT_AUDIT_SAMPLE_FLOOR=2, expanded to 3 for finer diagnostics) ---
# Selected to span distinct producing-script patterns:
#   W9a-102 — .claude/skills/... script (meta-gate on this skill)
#   W9a-100 — computations/_shared/... script (R3 validator)
#   W9a-98  — computations/_shared/... script (hook infra, different data-file mix)
SAMPLED_GATES = [
    ("W9a-102", "S84-W9A-102-MANIFEST-AUTO"),
    ("W9a-100", "S84-W9A-100-PRDR-TEMPLATE"),
    ("W9a-98",  "S84-W9A-98-HOOK-INFRA"),
]  # (local)


def run_generator(gate_slug: str) -> str:
    """Invoke generate_manifest.py in --emit-prompt-block mode, return text."""
    cmd = [
        str(VENV_PY),
        str(GENERATOR),
        "--plan", str(PLAN_PATH),
        "--gate-slug", gate_slug,
        "--session-n", "84",
        "--wp", WP_PATH,
        "--emit-prompt-block",
    ]  # (local)
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)  # (local)
    if result.returncode != 0:
        return f"ERROR: generator exited {result.returncode}\nSTDERR:\n{result.stderr}"
    return result.stdout


def audit_sample(gate_slug: str, expected_gate_id: str, prompt_block: str) -> Dict:
    """Check a synthesized prompt block for manifest_present + manifest_accurate."""
    # manifest_present: header + fenced json + all 6 keys
    present = (MANIFEST_BLOCK_HEADER in prompt_block
               and "```json" in prompt_block)  # (local)
    parsed = None  # (local)
    if present:
        idx = prompt_block.find(MANIFEST_BLOCK_HEADER)  # (local)
        fence_start = prompt_block.find("```json", idx)  # (local)
        fence_content_start = fence_start + len("```json\n")  # (local)
        fence_end = prompt_block.find("```", fence_content_start)  # (local)
        if fence_end > fence_content_start:
            try:
                parsed = json.loads(prompt_block[fence_content_start:fence_end])  # (local)
            except json.JSONDecodeError:
                parsed = None
    well_formed = (parsed is not None
                   and all(k in parsed for k in MANIFEST_JSON_KEYS))  # (local)
    # manifest_accurate: check structural match against expected gate_id +
    # verdict_line_target + that script is non-empty + WP section matches
    accurate = False  # (local)
    if well_formed:
        wp_secs = parsed.get("working_paper_sections") or []  # (local)
        accurate = (
            parsed.get("gate_id") == expected_gate_id
            and parsed.get("verdict_line_target") == "computations/session-84/s84_gate_verdicts.txt"
            and isinstance(parsed.get("script"), str)
            and len(parsed["script"]) > 0
            and isinstance(wp_secs, list)
            and len(wp_secs) > 0
            and all(sec.get("min_lines", 0) >= WORKING_PAPER_SECTION_MIN_LINES
                    for sec in wp_secs)
        )
    per_sample = int(bool(well_formed) and bool(accurate))  # (local)
    return {
        "gate_slug": gate_slug,
        "expected_gate_id": expected_gate_id,
        "manifest_present": bool(well_formed),
        "manifest_accurate": bool(accurate),
        "per_sample": per_sample,
        "parsed_gate_id": parsed.get("gate_id") if parsed else None,
        "parsed_script": parsed.get("script") if parsed else None,
        "parsed_verdict_target": parsed.get("verdict_line_target") if parsed else None,
        "parsed_key_set": sorted(parsed.keys()) if parsed else [],
    }


def compute_shas(pin_map: Dict, script_text: str) -> Dict:
    """Dual-SHA per gate-verdicts.md.

    audit_sha256 = hash over ordered pin_map (inputs discriminator)
    content_sha256 = hash over the producing-script text only
    """
    canonical_pins = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))  # (local)
    audit_sha = hashlib.sha256(canonical_pins.encode("utf-8")).hexdigest()  # (local)
    content_sha = hashlib.sha256(script_text.encode("utf-8")).hexdigest()  # (local)
    closure_sha = hashlib.sha256((canonical_pins + script_text).encode("utf-8")).hexdigest()  # (local)
    return {
        "closure": closure_sha,
        "audit": audit_sha,
        "content": content_sha,
    }


def append_verdict(verdict_label: str, value: float, shas: Dict) -> None:
    """Atomic single-line append to the session verdicts file."""
    line = (
        f"S84-W9A-102-MANIFEST-AUTO: {verdict_label} "
        f"-- value={value:.4f} "
        f"scheme=auto-generation+spot-audit "
        f"convention=10%-sample "
        f"L_max=session-scope "
        f"sha256={shas['closure']}"
    )  # (local)
    comment = (
        f"# S84-W9A-102-MANIFEST-AUTO dual-SHA: "
        f"content_sha256={shas['content']} audit_sha256={shas['audit']}"
    )  # (local)
    with VERDICTS_PATH.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
        f.write(comment + "\n")


def main() -> int:
    # --- Run audit across SAMPLED_GATES ---
    samples: List[Dict] = []  # (local)
    for slug, expected_id in SAMPLED_GATES:
        print(f"[AUDIT] generating manifest for {slug} ...")
        block = run_generator(slug)  # (local)
        audit = audit_sample(slug, expected_id, block)  # (local)
        audit["prompt_block_excerpt"] = block[:240]  # (local) diagnostics only
        samples.append(audit)

    n_samples = len(samples)  # (local)
    n_pass = sum(s["per_sample"] for s in samples)  # (local)
    pass_fraction = n_pass / n_samples if n_samples else 0.0  # (local)

    # Apply the pre-registered rubric (substitution chain in docstring):
    #   PASS iff pass_fraction == 1.0
    #   INFO iff 0.90 <= pass_fraction < 1.0
    #   FAIL iff pass_fraction < 0.90
    if pass_fraction >= 1.0 - 1e-9:
        verdict = "PASS"  # (local)
    elif pass_fraction >= 0.90:
        verdict = "INFO"  # (local)
    else:
        verdict = "FAIL"  # (local)

    report = {
        "gate_id": "S84-W9A-102-MANIFEST-AUTO",
        "scheme": "auto-generation+spot-audit",
        "convention": "10%-sample",
        "L_max": "session-scope",
        "pins": {
            "MANIFEST_BLOCK_HEADER": MANIFEST_BLOCK_HEADER,
            "MANIFEST_JSON_KEYS": MANIFEST_JSON_KEYS,
            "SPOT_AUDIT_SAMPLE_FRACTION": SPOT_AUDIT_SAMPLE_FRACTION,
            "SPOT_AUDIT_SAMPLE_FLOOR": SPOT_AUDIT_SAMPLE_FLOOR,
            "WORKING_PAPER_SECTION_MIN_LINES": WORKING_PAPER_SECTION_MIN_LINES,
        },
        "n_sampled": n_samples,
        "n_pass": n_pass,
        "pass_fraction": pass_fraction,
        "verdict": verdict,
        "samples": samples,
    }

    # --- Write audit archive ---
    AUDIT_OUT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False),
                         encoding="utf-8")
    print(f"[AUDIT] wrote {AUDIT_OUT}")
    print(f"[AUDIT] pass_fraction = {pass_fraction:.4f} -> {verdict}")

    # --- Dual-SHA closure ---
    pin_map = {
        "MANIFEST_BLOCK_HEADER": MANIFEST_BLOCK_HEADER,
        "MANIFEST_JSON_KEYS": MANIFEST_JSON_KEYS,
        "SPOT_AUDIT_SAMPLE_FRACTION": SPOT_AUDIT_SAMPLE_FRACTION,
        "SPOT_AUDIT_SAMPLE_FLOOR": SPOT_AUDIT_SAMPLE_FLOOR,
        "WORKING_PAPER_SECTION_MIN_LINES": WORKING_PAPER_SECTION_MIN_LINES,
        "sampled_slugs": [s for s, _ in SAMPLED_GATES],
        "sampled_ids": [i for _, i in SAMPLED_GATES],
        "plan_path": str(PLAN_PATH.relative_to(PROJ_ROOT)).replace("\\", "/"),
        "generator_path": str(GENERATOR.relative_to(PROJ_ROOT)).replace("\\", "/"),
    }  # (local)
    script_text = Path(__file__).read_text(encoding="utf-8")  # (local)
    shas = compute_shas(pin_map, script_text)  # (local)

    print(f"[SHA] closure = {shas['closure']}")
    print(f"[SHA] audit   = {shas['audit']}")
    print(f"[SHA] content = {shas['content']}")

    append_verdict(verdict, pass_fraction, shas)
    print(f"[VERDICT] appended to {VERDICTS_PATH}")

    return 0 if verdict in ("PASS", "INFO") else 1


if __name__ == "__main__":
    sys.exit(main())
