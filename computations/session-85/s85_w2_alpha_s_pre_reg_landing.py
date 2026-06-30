#!/usr/bin/env python
"""
S85-W2-ALPHA-S-PRE-REG-REGISTRY-LANDING

Consolidation audit for the 8 alpha_s / beta_s event-driven pre-registrations
accumulated across S82-S84 + S85 W0/W1a. Verdict: are any two pre-regs
internally contradictory (same observable + detector, contradictory pass-band)?
If num_contradictions = 0, PASS and emit §VII.M.2 registry-section draft.

The 8 pre-registrations per plan §W2-8:
  1. CMB-S4 flagship alpha_s (S84 W6-D.4 / CMB-S4-ALPHA-FLAGSHIP)
  2. CMB-HD MacInnis-explicit (S85-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT)
  3. LiteBIRD Hazumi-verified (S85-LITEBIRD-ALPHA-S-HAZUMI-VERIFIED)
  4. Joint Fisher correlated (S85-ALPHA-S-JOINT-FISHER-CORRELATED)
  5. Prior-range LCDM (S85-ALPHA-S-PRIOR-RANGE-LCDM)
  6. Transit PS-67 simultaneous (S85-ALPHA-S-TRANSIT-PS-67-SIMULTANEOUS)
  7. W0 CMB-S4 beta_s (S85-BETA-S-CMB-S4-PREREG) — companion to alpha_s
  8. W1a ALPHA-S-REGISTRY-UPGRADE (S85-W1a-ALPHA-S-REGISTRY-UPGRADE)

Reference:
  - sessions/session-plan/session-85-buckets/alpha-s-preregistration.json
  - sessions/session-plan/session-85-plan-w0.md §W0-1
  - sessions/session-plan/session-85-plan-w1a.md §W1a-2
  - S84 W8-86 OZ-derivation (canonical central: alpha_s = -0.068968)
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403

INPUT_FILES = [
    "sessions/session-plan/session-85-buckets/alpha-s-preregistration.json",
    "sessions/session-plan/session-85-plan-w0.md",
    "sessions/session-plan/session-85-plan-w1a.md",
    "sessions/session-plan/session-85-plan-w1b.md",
    "sessions/permanent-results-registry.md",
]


def sha256_of(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return "MISSING"
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# The 8 pre-registrations with their (channel, central, 1σ, 2σ, pass-band,
# fail-band, prior) extracted from source material.
#
# Canonical central values:
#   alpha_s = -0.068968 (S50 n_s² - 1, W8-86 OZ machine-ε derivation)
#   beta_s  = -0.1331   (third Taylor coefficient, W8-86)
# ---------------------------------------------------------------------------
ALPHA_S_CENTRAL = -0.068968   # (local) canonical framework central, S50 + W8-86
BETA_S_CENTRAL  = -0.1331     # (local) canonical framework central, W8-86 3rd moment

PRE_REGS = [
    {
        "id": "CMB-S4-ALPHA-FLAGSHIP",
        "observable": "alpha_s",
        "detector": "CMB-S4",
        "central": ALPHA_S_CENTRAL,
        "sigma_1": 0.002,          # per W6-52 CMB-S4 = 34.48σ for alpha_s=-0.069 gives σ ≈ 0.002
        "sigma_2": 0.004,
        "pass_band": (-0.073, -0.065),   # central ± 2σ
        "fail_band_outside": (-0.080, -0.058),
        "prior": "framework (zero-free-parameter)",
        "source": "S84 W6-D.4 flagship, Mack V.2",
    },
    {
        "id": "CMB-HD-ALPHA-S-MACINNIS-EXPLICIT",
        "observable": "alpha_s",
        "detector": "CMB-HD",
        "central": ALPHA_S_CENTRAL,
        "sigma_1": 0.0013,         # MacInnis+ 2023 σ(n_s) scaled
        "sigma_2": 0.0026,
        "pass_band": (-0.0716, -0.0663),
        "fail_band_outside": (-0.0742, -0.0637),
        "prior": "framework (zero-free-parameter)",
        "source": "S85 W2-8 Mack V.4, MacInnis+ 2023",
    },
    {
        "id": "LITEBIRD-ALPHA-S-HAZUMI-VERIFIED",
        "observable": "alpha_s",
        "detector": "LiteBIRD",
        "central": ALPHA_S_CENTRAL,
        "sigma_1": 0.006,          # Hazumi+ 2022 projected
        "sigma_2": 0.012,
        "pass_band": (-0.081, -0.057),
        "fail_band_outside": (-0.093, -0.045),
        "prior": "framework (zero-free-parameter)",
        "source": "S85 W2-8 Mack, Hazumi+ 2022",
    },
    {
        "id": "ALPHA-S-JOINT-FISHER-CORRELATED",
        "observable": "alpha_s",
        "detector": "joint (S4 + SO + HD + LiteBIRD)",
        "central": ALPHA_S_CENTRAL,
        "sigma_1": 0.00108,        # joint 64.31σ -> σ ≈ 0.001
        "sigma_2": 0.00216,
        "pass_band": (-0.0711, -0.0668),
        "fail_band_outside": (-0.0733, -0.0647),
        "prior": "framework (zero-free-parameter)",
        "source": "S85 W2-8 Mack V.3, Abazajian+ 2022 Snowmass",
    },
    {
        "id": "ALPHA-S-PRIOR-RANGE-LCDM",
        "observable": "alpha_s",
        "detector": "LCDM prior predictive",
        "central": None,           # LCDM prior distribution, not a point estimate
        "prior_range": (0.03, 0.10),
        "prior": "LCDM slow-roll model catalog (Martin+ 2014 Encyclopaedia Inflationaris)",
        "pass_band": None,         # prior is informational, not a pass-band
        "fail_band_outside": None,
        "source": "S85 W2-8 Mack prior range",
    },
    {
        "id": "ALPHA-S-TRANSIT-PS-67-SIMULTANEOUS",
        "observable": "alpha_s",
        "detector": "S84 registry (3 rows)",
        "central": ALPHA_S_CENTRAL,
        "note": "resolves three-valued registry: slow-roll L=4 (-0.038 FAIL), acoustic-CMB (~0 pending), S50 OZ (-0.069). Selects S50 OZ as canonical.",
        "sigma_1": 0.0,            # resolution, not sensitivity
        "sigma_2": 0.0,
        "pass_band": (ALPHA_S_CENTRAL, ALPHA_S_CENTRAL),
        "fail_band_outside": None,
        "prior": "framework (resolves contradiction)",
        "source": "S85 W2-8 Mack, S62 slow-roll + S84 W8-86",
    },
    {
        "id": "BETA-S-CMB-S4-PREREG",
        "observable": "beta_s",
        "detector": "CMB-S4",
        "central": BETA_S_CENTRAL,
        "sigma_1": 0.0022,         # CMB-S4 Science Book v2 Table 6.1
        "sigma_2": 0.0044,
        "pass_band": (-0.1375, -0.1287),
        "fail_band_outside": (-0.1419, -0.1243),
        "prior": "framework (3rd Taylor coefficient)",
        "source": "S85 W0-1, CMB-S4 Science Book v2 Table 6.1",
    },
    {
        "id": "W1a-ALPHA-S-REGISTRY-UPGRADE",
        "observable": "alpha_s (meta: registry-row upgrade)",
        "detector": "registry-internal",
        "central": ALPHA_S_CENTRAL,
        "sigma_1": 0.0,            # registry action, not observational sensitivity
        "sigma_2": 0.0,
        "pass_band": (ALPHA_S_CENTRAL, ALPHA_S_CENTRAL),
        "fail_band_outside": None,
        "prior": "framework (promotes numerical identity to zero-free-parameter theorem)",
        "source": "S85 W1a-2 plan §W1a-2",
    },
]


def compatible(pre_a: dict, pre_b: dict) -> bool:
    """
    Two pre-regs are contradictory iff:
      (i) same observable AND same detector,
      (ii) pass-bands are non-overlapping (disjoint).
    Compatibility check: either different obs/detector OR pass-bands overlap.
    """
    # Different observable? => not contradictory (different things)
    if pre_a["observable"] != pre_b["observable"]:
        return True
    # Different detector? => not contradictory (can give independent σ)
    if pre_a["detector"] != pre_b["detector"]:
        return True
    # Same observable + same detector: pass-bands must overlap
    pb_a = pre_a.get("pass_band")
    pb_b = pre_b.get("pass_band")
    if pb_a is None or pb_b is None:
        return True  # meta-level (no pass-band) - no observational contradiction
    lo_a, hi_a = pb_a
    lo_b, hi_b = pb_b
    # Pass-bands overlap iff NOT (hi_a < lo_b OR hi_b < lo_a)
    return not (hi_a < lo_b or hi_b < lo_a)


def build_vii_m2_section() -> str:
    """Emit the §VII.M.2 registry-section draft."""
    lines = [
        "## §VII.M.2 — Event-driven alpha_s and beta_s pre-registrations (S82-S85 consolidated)",
        "",
        "**Consolidation source**: S85 W2-8 (S85-W2-ALPHA-S-PRE-REG-REGISTRY-LANDING).",
        "",
        "**Canonical central values** (from S50 + S84 W8-86 OZ-derivation):",
        f"  - alpha_s = {ALPHA_S_CENTRAL} (= n_s^2 - 1 at Planck n_s central)",
        f"  - beta_s  = {BETA_S_CENTRAL} (3rd Taylor coefficient)",
        "",
        "**Per-pre-reg table**:",
        "",
        "| Pre-reg ID | Observable | Detector | σ(1σ) | Pass-band | Prior |",
        "|:-----------|:-----------|:---------|:------|:----------|:------|",
    ]
    for p in PRE_REGS:
        cid = p["id"]
        obs = p["observable"]
        det = p["detector"]
        sig = p.get("sigma_1", "N/A")
        pb = p.get("pass_band", "N/A")
        pr = p["prior"]
        lines.append(f"| {cid} | {obs} | {det} | {sig} | {pb} | {pr} |")
    lines.append("")
    lines.append("**Scheme lockouts** (from W10-123 axiom closure chain):")
    lines.append("  1. No post-data auxiliary couplings.")
    lines.append("  2. No n_s redefinition.")
    lines.append("  3. No derivation-chain change.")
    lines.append("  4. No pivot migration.")
    lines.append("  5. No axiom subtraction.")
    lines.append("  6. No detector cherry-picking.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    print("=" * 70)
    print("S85-W2-ALPHA-S-PRE-REG-REGISTRY-LANDING")
    print("=" * 70)
    input_shas: dict[str, str] = {}
    for f in INPUT_FILES:
        sha = sha256_of(f)
        input_shas[f] = sha
        print(f"INPUT  {f}  sha256={sha}")
    print("-" * 70)

    # Enumerate contradictions
    contradictions = []
    for a, b in combinations(PRE_REGS, 2):
        if not compatible(a, b):
            contradictions.append({
                "a_id": a["id"],
                "b_id": b["id"],
                "a_pass_band": a.get("pass_band"),
                "b_pass_band": b.get("pass_band"),
                "reason": f"same observable={a['observable']} + same detector={a['detector']}; disjoint bands",
            })

    num_contradictions = len(contradictions)

    # Gap check: do any pre-regs have documentation gaps (missing prior / 2σ)?
    has_doc_gap = False
    doc_gaps = []
    for p in PRE_REGS:
        if p.get("prior") is None:
            has_doc_gap = True
            doc_gaps.append({"id": p["id"], "issue": "missing prior"})
        if p.get("sigma_1") is None and p.get("pass_band") is not None:
            has_doc_gap = True
            doc_gaps.append({"id": p["id"], "issue": "missing 1σ"})

    if num_contradictions == 0 and not has_doc_gap:
        verdict = "PASS"
    elif num_contradictions == 0 and has_doc_gap:
        verdict = "INFO"   # landing proceeds with gap note
    else:
        verdict = "FAIL"

    # Per-pre-reg table
    print(f"{'ID':<40}{'Observable':<15}{'Detector':<30}{'σ(1σ)':>10}")
    for p in PRE_REGS:
        sig = p.get("sigma_1", "N/A")
        sig_str = f"{sig:.4g}" if isinstance(sig, (int, float)) else str(sig)
        print(f"{p['id']:<40}{p['observable']:<15}{p['detector']:<30}{sig_str:>10}")
    print("-" * 70)
    print(f"num_contradictions = {num_contradictions}")
    print(f"doc_gaps count     = {len(doc_gaps)}")
    print("-" * 70)

    # Emit §VII.M.2 section
    section_md = build_vii_m2_section()
    section_path = Path(__file__).parent / "s85_w2_alpha_s_pre_reg_landing_section.md"
    section_path.write_text(section_md)
    print(f"WROTE {section_path}")

    # Closure SHA
    pin_map_str = json.dumps(
        {
            "inputs": input_shas,
            "num_pre_regs": len(PRE_REGS),
            "num_contradictions": num_contradictions,
            "contradictions": contradictions,
            "doc_gaps": doc_gaps,
            "pre_reg_ids": [p["id"] for p in PRE_REGS],
        },
        sort_keys=True,
        default=str,
    )
    closure_sha = hashlib.sha256(pin_map_str.encode()).hexdigest()
    content_sha = hashlib.sha256(
        json.dumps(PRE_REGS, sort_keys=True, default=str).encode()
    ).hexdigest()

    out_json = {
        "gate_id": "S85-W2-ALPHA-S-PRE-REG-REGISTRY-LANDING",
        "verdict": verdict,
        "value_4tuple": {
            "value": num_contradictions,
            "scheme": "pre-reg-consolidation-audit",
            "convention": "registry-§VII.M.2",
            "L_max": "N/A",
        },
        "num_pre_regs": len(PRE_REGS),
        "num_contradictions": num_contradictions,
        "contradictions": contradictions,
        "doc_gaps": doc_gaps,
        "pre_regs": PRE_REGS,
        "closure_sha256": closure_sha,
        "content_sha256": content_sha,
        "input_shas": input_shas,
    }
    out_path = Path(__file__).with_suffix(".json")
    out_path.write_text(json.dumps(out_json, indent=2, default=str))
    print(f"WROTE {out_path}")
    print(f"VERDICT: {verdict}")
    print(f"closure_sha256 = {closure_sha}")
    print(f"content_sha256 = {content_sha}")
    print(
        f"4-tuple: value={num_contradictions}, scheme=pre-reg-consolidation-audit, "
        f"convention=registry-§VII.M.2, L_max=N/A"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
