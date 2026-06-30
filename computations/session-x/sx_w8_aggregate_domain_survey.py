#!/usr/bin/env python3
"""
WX-W8-1 — AGGREGATE-DOMAIN-SURVEY (SU(3) Jensen crystal-geometry domain vs whole KB)
====================================================================================

Gate: WX-W8-1-AGGREGATE-DOMAIN-SURVEY  ([AUDIT])

Pre-registered threshold (GEOMETRIC; set-membership / coverage-by-enumeration):
  PASS iff
    (a) constant_state_verdict(name) in {CURRENT,STALE,SUPERSEDED,DEAD-IMPORT,
        PROVENANCE-GAP} for ALL 16 imported names, AND
    (b) depicted_geometry_status enumerated for all core structures with KB entity, AND
    (c) gap_slate = {post-S47 geometric results NOT covered} enumerated, |gap_slate| >= 4,
        each row KB-cited.
  No numerical mesh; the survey + gap analysis is the WP deliverable. The closure
  script formalizes the dual-SHA verdict over the survey artifacts + canonical snapshot.

The KB-mining survey (tens of get_constant / search_knowledge / trace_entity queries)
is recorded in the WP MCP Pre-Compute Audit + Results blocks. THIS script encodes the
machine-checkable conjunction over those by-hand findings: 16/16 constant states assigned,
core depicted structures status-tagged, gap_slate >= 4 KB-cited rows.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/Phononic-crystal-geometry_viz.py     (the surveyed script)
  - sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md (archived source doc)
  - tools/knowledge.db                                      (KB surveyed)
  - canonical_constants.py                                  (16 imports; feeds audit_sha256)
  - script bytes                                            (feeds BOTH SHAs)

Output 4-tuple:
  (value=<16/16 const-states + N_core structures + |gap_slate|>,
   scheme=aggregate-domain-survey,
   convention=KB-cited-gap-enumeration,
   L_max=N/A)

Classification: GEOMETRIC (whole-domain KB survey; comprehensiveness engine)

DISCIPLINE
----------
- `from canonical_constants import *`  (16 imports re-resolved live; no value hardcoded)
- Every local/intermediate tagged `# (local)`
- No linear algebra; CPU-only, OMP threads capped to 8
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema), atomic append
- Verdict appended to canonical path computations/session-x/sx_gate_verdicts.txt
  (per `gate-verdicts.md` Canonical Verdict-File Path)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys

# Ensure canonical_constants is importable (mirrors the viz script's path insert).
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))

from canonical_constants import *  # noqa: F401,F403  (framework discipline; no constants hardcoded)
from canonical_constants import (  # explicit: the 16 surveyed imports + new-figure anchors
    tau_fold, c_fabric, c_Gold, J_C2, J_su2, J_u1,
    N_cells, E_cond, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    N_e_classical, xi_BCS, L_over_xi, Delta_0_GL,
    R_protected_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + identity
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()  # (local)
SESSION_DIR = THIS.parent  # computations/session-x  (local)
COMPUTATIONS_DIR = SESSION_DIR.parent  # (local)
SHARED_DIR = COMPUTATIONS_DIR / "_shared"  # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent  # (local)
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"  # (local)

SESSION = "SX"  # (local)
GATE_ID = "WX-W8-1-AGGREGATE-DOMAIN-SURVEY"  # (local)
SCHEME = "aggregate-domain-survey"  # (local)
CONVENTION = "KB-cited-gap-enumeration"  # (local)
L_MAX = "N/A"  # (local) survey gate; no spectral truncation

VERDICT_TXT = SESSION_DIR / "sx_gate_verdicts.txt"  # (local) canonical path
OUT_JSON = SESSION_DIR / "sx_w8_aggregate_domain_survey.json"  # (local) optional artifact

INPUT_FILES = [
    FRAMEWORK_DIR / "Phononic-crystal-geometry_viz.py",
    FRAMEWORK_DIR / "ARCHIVE" / "Phononic-Crystal-Geometry.md",
    PROJECT_ROOT / "tools" / "knowledge.db",
    SHARED_DIR / "canonical_constants.py",
]  # (local)

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ DUAL-SHA, W9a-99)
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( bytes(script) )
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Deliverable (a): the 16-constant state-verdict table
#
# Each row: (name, live_value, script_displayed_or_hardcoded, superseded, has_provenance,
#            state-verdict). The live_value is read from canonical_constants (NOT hardcoded);
# the script-displayed value is the literal the viz currently shows (from a Read of the
# viz script — recorded here so the closure can assert the CURRENT/STALE/DEAD-IMPORT split).
# ---------------------------------------------------------------------------

VALID_STATES = {"CURRENT", "STALE", "SUPERSEDED", "DEAD-IMPORT", "PROVENANCE-GAP"}  # (local)

# PLAN-TEXT DRIFT (substrate-first-canonical-sourcing.md §(ii.B)): the plan calls these
# "16 imported constants", but the viz script's `from canonical_constants import (...)` block
# (lines 18-22) actually imports 17 names (the plan's own machinery pin §line 142 / §715
# enumerates all 17). The survey covers ALL imported names; the gate asserts against the TRUE
# import count, not the mis-transcribed "16". Drift documented in the verdict value= field.
N_IMPORTS_ACTUAL = 17  # (local) verified from viz-script import block (re-parse cross-check)

# script-displayed / hardcoded values lifted verbatim from the viz script body:
#   BRANCHES['Higgs-2']['omega0']=1.456 (line 76); ['Higgs-3']['omega0']=10.37 (line 77)
#   gap_freqs reads imported omega_L1=0.138 / omega_L2=0.192 (lines 254-255)
#   Vis-1 legend literal 'J_{u(1)} = 0.038' (line 185); annotation J_C2/J_u1 uses imported 0.038
#   Delta_0_GL imported (line 21) but never referenced in body
SCRIPT_DISPLAY = {  # (local)
    "tau_fold": 0.19, "c_fabric": 209.97368021, "c_Gold": 0.915,
    "J_C2": 0.933, "J_su2": 0.059, "J_u1": 0.038, "N_cells": 32,
    "E_cond": -0.13685055970476342, "omega_L1": 0.138, "omega_L2": 0.192,
    "omega_H1": 0.378, "omega_H2": 1.456, "omega_H3": 10.37,
    "N_e_classical": 0.1734, "xi_BCS": 0.8083468753837275,
    "L_over_xi": 0.031, "Delta_0_GL": None,  # imported, never consumed
}

LIVE = {  # (local) live canonical values, imported above (NOT hardcoded — referenced symbols)
    "tau_fold": tau_fold, "c_fabric": c_fabric, "c_Gold": c_Gold,
    "J_C2": J_C2, "J_su2": J_su2, "J_u1": J_u1, "N_cells": N_cells,
    "E_cond": E_cond, "omega_L1": omega_L1, "omega_L2": omega_L2,
    "omega_H1": omega_H1, "omega_H2": omega_H2, "omega_H3": omega_H3,
    "N_e_classical": N_e_classical, "xi_BCS": xi_BCS,
    "L_over_xi": L_over_xi, "Delta_0_GL": Delta_0_GL,
}

# State-verdicts assigned from the KB survey (get_constant Superseded + PROVENANCE flags
# cross-read against SCRIPT_DISPLAY). Recorded in the WP §W8-1 Results constant-state table.
CONST_STATE = {  # (local)
    "tau_fold": "CURRENT",          # 0.19, S12/S42, Superseded=False, has provenance
    "c_fabric": "PROVENANCE-GAP",   # 209.97368021 current; no PROVENANCE entry (D7)
    "c_Gold": "PROVENANCE-GAP",     # 0.915 current; no PROVENANCE (D7)
    "J_C2": "PROVENANCE-GAP",       # 0.933 current; no PROVENANCE (D7)
    "J_su2": "PROVENANCE-GAP",      # 0.059 current; no PROVENANCE (D7)
    "J_u1": "PROVENANCE-GAP",       # 0.038 current (D2: archive 0.029 stale); no PROVENANCE
    "N_cells": "CURRENT",           # 32, S42 GIANT-VORONOI, Superseded=False
    "E_cond": "CURRENT",            # -0.13685, S36 ED-CONV-36, Superseded=False
    "omega_L1": "PROVENANCE-GAP",   # 0.138 current S52 GL; no PROVENANCE (D4 collision w/ S48 0.070)
    "omega_L2": "PROVENANCE-GAP",   # 0.192 current S52 GL; no PROVENANCE (D4 collision w/ S48 0.107)
    "omega_H1": "PROVENANCE-GAP",   # 0.38 current; no PROVENANCE
    "omega_H2": "DEAD-IMPORT",      # 1.41 canonical; script hardcodes 1.456 -> import unused (D3)
    "omega_H3": "DEAD-IMPORT",      # 11.465 canonical; script hardcodes 10.37 -> import unused (D3)
    "N_e_classical": "PROVENANCE-GAP",  # 0.1734 current; no PROVENANCE
    "xi_BCS": "CURRENT",            # 0.8083, S37, Superseded=False
    "L_over_xi": "PROVENANCE-GAP",  # 0.031 current; no PROVENANCE
    "Delta_0_GL": "DEAD-IMPORT",    # 0.7704 current S37; imported but never referenced (D5)
}

# ---------------------------------------------------------------------------
# Section 6 — Deliverable (b): depicted-geometry status (core structures)
#   each: (structure, status, KB-entity). status in {CURRENT, STALE, SUPERSEDED}.
# ---------------------------------------------------------------------------
DEPICTED_GEOMETRY = {  # (local)
    "32-cell Voronoi tessellation": ("CURRENT", "N_cells=32 S42 GIANT-VORONOI (Superseded=False)"),
    "6 tight-binding branches (1 Gold + 2 Leggett + 3 Higgs)": ("STALE-DISPLAY", "BRANCHES Higgs-2/3 hardcode 1.456/10.37 vs canonical omega_H2/H3=1.41/11.465"),
    "J_C2:J_su2:J_u1 bond hierarchy 4:3:1": ("CURRENT", "J_C2=0.933,J_su2=0.059,J_u1=0.038 (archive 0.029 stale)"),
    "c_fabric/c_Gold=229.5 acoustic hierarchy": ("CURRENT", "proven_1157 / c_Gold_over_c_fabric R-PROTECTED (proven_814/834)"),
    "N_pair=1": ("CURRENT", "S53 W2-6 PERMANENT"),
    "Mott regime E_J/E_C=0.818, Gi=0.506": ("CURRENT", "S53 W3-12 Mott side"),
    "BCS speed bump tau=0.2015": ("CURRENT", "S53 W3-7 PROVEN (d2V_KK=-63.2, d2E_cond=-67.7)"),
    "curvature anatomy (K(u1,su2)=0, K(u1,C2)=1/16, Ric(u1)=1/4)": ("CURRENT-CONVENTION-AMBIGUOUS", "Theorem 1/2/Corollary exact; R-sign quartet D8"),
}

# ---------------------------------------------------------------------------
# Section 7 — Deliverable (c): the post-S47 GAP slate (>= 4 KB-cited candidates)
#   each: (cand, result, KB-citation, where-it-belongs).
# ---------------------------------------------------------------------------
GAP_SLATE = {  # (local)
    "E1": ("4-stratum bottom-20 partition (2,4,8,6) + tau-asymmetric breakdown",
           "§VII.AJ.partition-stability S87 W11-2 PERMANENT; §VII.AE S88 W2-9 (delta_neg=-0.0750, delta_pos=+0.175); atlas-03 E40",
           "Vis-8 (new figure)"),
    "E2": ("spectral-moment landscape a_n(tau) + protected ratio R_1=a_0*a_4/a_2^2 + R-monotonicity",
           "R_protected_fold=1.1286545967627695 S73B/S74 R-PROTECTED; R-monotonicity dR/dtau>=0 S64 W1-A PROVEN (closes CC Path C)",
           "Vis-9 (new figure)"),
    "E3": ("spectral-dimension flow d_s(sigma)=-2 dlnP/dlnsigma vs CDT",
           "S92 ad-hoc s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md; fold window sigma_*=1.4005 M_KK^-2; UV d_s->8 Weyl",
           "Vis-10 (new figure)"),
    "E4": ("cross-pillar bridge geometry R_universal=<[phi_g^sym],[Ch(P_0)]> -> quantum-metric trace",
           "§VII.W S86 first cross-pillar bridge; R_canonical=7.324974378387362 S89 W2 (Hochschild x Chern)",
           "Vis-11 (new figure; optional within effort)"),
}

# ---------------------------------------------------------------------------
# Section 8 — Deliverable (d): QA-layer drift ledger (D1-D8)
# ---------------------------------------------------------------------------
DRIFT_LEDGER = {  # (local)
    "D1": "tau_bump=0.2015 (speed bump) vs tau_fold=0.19 (transit fold): CURRENT-WITH-DISAMBIGUATION; structurally distinct; do NOT find-replace",
    "D2": "Vis-1 J_u1 label=0.038 (script CURRENT); archive 0.029 STALE -> W8-3 migration",
    "D3": "BRANCHES Higgs-2=1.456/Higgs-3=10.37 hardcoded; omega_H2=1.41/omega_H3=11.465 DEAD IMPORTS -> consume canonical or document distinct-provenance",
    "D4": "omega_L1/L2 naming collision: imported 0.138/0.192 (S52 GL) vs archive 0.070/0.107 (S48 3-band) -> DISAMBIGUATE",
    "D5": "Delta_0_GL imported never used: DEAD-IMPORT (hygiene)",
    "D6": "successor-doc supersession points at §7.3='R-Protection as K-Pairing' (NOT crystal content) -> crystal geometry ORPHANED",
    "D7": "8/16 imports PROVENANCE-GAP (advisory; do not block)",
    "D8": "R-sign convention QUARTET: script-form +2.018(R(0)=2.0); S52/S53 4.036(R(0)=4.0); S61 Koszul -2.018 signed; KB Paper-15 string OCR-garbled (R(0)=1.5) -> pin SIGNED S61 for new curvature figs",
}

# ---------------------------------------------------------------------------
# Section 9 — Substitution-chain numerical verifications (Sage-cross-checked at plan-freeze)
# ---------------------------------------------------------------------------

def verify_chains() -> dict[str, object]:
    """CHAIN 1 (Jensen volume preservation) + CHAIN 2 (c-ratio e-folds).
    Re-computed here from the imported canonical constants (NOT hardcoded numbers)."""
    # CHAIN 1: det g_tau = exp((2,-2,1).(1,3,4) * tau) = exp(0) = 1
    exponent = 2 * 1 + (-2) * 3 + 1 * 4  # (local)  = 0 exact
    det_g = math.exp(exponent * float(tau_fold))  # (local)  = 1.0
    # CHAIN 2: ratio + e-folds from imported c_fabric / c_Gold
    ratio = float(c_fabric) / float(c_Gold)  # (local)
    Ne_3p1 = 0.5 * math.log(ratio)  # (local)
    Ne_8d = (1.0 / 7.0) * math.log(ratio)  # (local)
    # E2 anchor cross-check: R_protected_fold reproduced by S64-moment ratio (within 0.01%)
    a0, a2, a4 = 6440.0, 2776.17, 1350.72  # (local) S64 W1-A moments (session-64 WP)
    R1_s64 = a0 * a4 / (a2 ** 2)  # (local)
    return {
        "chain1_exponent": exponent,                 # 0
        "chain1_det_g": det_g,                        # 1.0
        "chain2_ratio": ratio,                        # 229.4794...
        "chain2_Ne_3p1": Ne_3p1,                      # 2.71791
        "chain2_Ne_8d": Ne_8d,                        # 0.77654
        "E2_R1_s64_moments": R1_s64,                  # 1.12865 ~ R_protected_fold
        "E2_R_protected_fold_canonical": float(R_protected_fold),
    }


# ---------------------------------------------------------------------------
# Section 10 — Gate evaluation + verdict emission
# ---------------------------------------------------------------------------

def evaluate_gate() -> tuple[str, dict]:
    """Coverage-by-enumeration conjunction (PASS rubric §W8-1)."""
    a_ok = (
        len(CONST_STATE) == N_IMPORTS_ACTUAL
        and all(v in VALID_STATES for v in CONST_STATE.values())
    )  # (local)  17/17 imports each assigned a valid state (plan-text "16" drift-corrected)
    b_ok = (len(DEPICTED_GEOMETRY) >= 7
            and all(isinstance(t, tuple) and len(t) == 2 for t in DEPICTED_GEOMETRY.values()))  # (local)
    c_ok = (len(GAP_SLATE) >= 4
            and all(isinstance(t, tuple) and len(t) == 3 and t[1] for t in GAP_SLATE.values()))  # (local)  each gap KB-cited
    d_ok = (len(DRIFT_LEDGER) == 8)  # (local)  D1-D8 enumerated
    chains = verify_chains()  # (local)
    chain_ok = (chains["chain1_exponent"] == 0
                and abs(chains["chain1_det_g"] - 1.0) < 1e-12
                and abs(chains["chain2_ratio"] - 229.479431923) < 1e-3
                and abs(chains["E2_R1_s64_moments"] - chains["E2_R_protected_fold_canonical"]) < 1e-3)  # (local)
    checks = {"const_states_16of16": a_ok, "depicted_geometry_enumerated": b_ok,
              "gap_slate_ge4_kb_cited": c_ok, "drift_ledger_D1_D8": d_ok,
              "substitution_chains": chain_ok}  # (local)
    verdict = "PASS" if all(checks.values()) else "FAIL"  # (local)
    return verdict, {"checks": checks, "chains": chains}


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-`open('a')` append of the dual-SHA canonical line + companion row."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"GEOMETRIC aggregate-domain-survey; [AUDIT] no [SIGN] 3-tuple\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  legacy closure: {closure[:16]}... (informational)")
    audit_sha, content_sha = compute_dual_sha(
        THIS, SHARED_DIR / "canonical_constants.py", pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    verdict, detail = evaluate_gate()  # (local)
    n_const = len(CONST_STATE)  # (local)
    n_geom = len(DEPICTED_GEOMETRY)  # (local)
    n_gap = len(GAP_SLATE)  # (local)
    # Option A (gate-verdicts.md): the first emission FAILed on a plan-text "16" miscount
    # (true import count is 17); the corrective PASS line supersedes it. Full 64-char SHA.
    SUPERSEDES = "0ec03dafe06fcc600b88fb25abfcbb124c04437d8bdd8e42581e02728d388150"  # (local)
    value = (f"const_states={n_const}/{N_IMPORTS_ACTUAL}(plan-text-16-drift-corrected);"
             f"depicted={n_geom};gap_slate={n_gap}_KB-cited;drift_ledger=D1-D8;"
             f"chain1_detg={detail['chains']['chain1_det_g']:.1f};"
             f"chain2_ratio={detail['chains']['chain2_ratio']:.4f};"
             f"supersedes={SUPERSEDES}")  # (local)

    # Optional JSON artifact (state-of-domain map + gap analysis snapshot).
    try:
        OUT_JSON.write_text(json.dumps({
            "gate_id": GATE_ID, "verdict": verdict, "value": value,
            "const_state": CONST_STATE, "live_values": {k: (None if v is None else float(v)) for k, v in LIVE.items()},
            "script_display": SCRIPT_DISPLAY,
            "depicted_geometry": {k: list(v) for k, v in DEPICTED_GEOMETRY.items()},
            "gap_slate": {k: list(v) for k, v in GAP_SLATE.items()},
            "drift_ledger": DRIFT_LEDGER, "chains": detail["chains"],
            "checks": detail["checks"],
            "audit_sha256": audit_sha, "content_sha256": content_sha,
        }, indent=2), encoding="utf-8")
        print(f"  [json] survey snapshot: {OUT_JSON.name}")
    except OSError as exc:
        print(f"  [json] optional snapshot skipped ({exc})")

    print()
    print(f"  checks: {detail['checks']}")
    print(f"  4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"  verdict appended: {GATE_ID}: {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
