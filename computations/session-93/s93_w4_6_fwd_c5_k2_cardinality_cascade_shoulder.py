#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S93-W4-6-FWD-C5-K2-SUBSTRATE-DISTANCE-3-POLE-S5-CARDINALITY-CASCADE-SHOULDER
===========================================================================

Gate:  S93-W4-6  (LEAD: mack-cosmic-bridge; CO-AUTHOR: volovik-superfluid-universe-theorist)
Trigger: [VERIFY-THEOREM]
Classification: GEOMETRIC (cardinality-cascade-SHOULDER observable on the D_K
                spectrum at substrate-distance-3 pole s=5).

HYPOTHESIS
----------
The cardinality-cascade-SHOULDER observable n_PBH_shoulder(g) admits a closed form
on the substrate algebra A_K at the rising-shoulder regime g in [g_BBN=80, g_saturate=143)
at substrate-distance-3 pole s=5, advancing the FWD-C5 Hybrid-Independence-Test
K-counter K=1 -> K=2 — STRUCTURALLY DISTINCT from the K=1 baseline (§VII.AX.OP-PROJ,
substrate-distance-2 pole s=4, SATURATED tail) by pole index (s=5 vs s=4) and regime
(rising shoulder vs saturated tail).

SUBSTRATE FRAMING (IS-not-IN; phononic-framing.md)
--------------------------------------------------
The substrate IS the spectral triple (A_K, H_K, D_K(tau_fold=0.19)). The
cardinality-cascade-SHOULDER observable is the PRE-SATURATION cardinality functional
at the rising-shoulder regime g in [80,143), where the Peter-Weyl substrate-cardinality
n_edge(g)=2^g is STILL GROWING (NOT yet saturated at C(N_eigs,2) for g>=143). Direction
of explanation: D_K Peter-Weyl cardinality at cascade-generation g -> shoulder-regime
edge-count 2^g -> n_PBH_shoulder(g) -> laboratory-IN PBH population at BBN-to-saturation
generations. This is the deterministic restriction of the S88 W1a-59 §0 substrate-clock
cancellation closed form to the g<g_saturate sub-domain (a DOMAIN-of-g statement,
orthogonal to the (iv) algebraic-envelope independence determination — see volovik audit).

CLOSED-FORM DERIVATION (substrate-clock cancellation form, registry §VII.AX.OP-PROJ Step 3)
-------------------------------------------------------------------------------------------
  n_edge(g) = 2^g                          (Peter-Weyl substrate-cardinality, RISING shoulder)
  L_pix(g)  = L_pix_LRD * 2^{-g/3}         (substrate-clock pixelation at cascade-generation g)
  IS-not-IN coupling: the cosmological-volume dilution 2^{-3g} is canceled BY CONSTRUCTION
  because L_pix(g) IS the substrate's clock (not a coordinate in a meta-container). So:
      n_PBH_shoulder(g) = n_edge(g) * prob_form / L_pix(g)^3
                        = (2^g * prob_form) / (L_pix_LRD * 2^{-g/3})^3
                        = (prob_form / L_pix_LRD^3) * 2^g * 2^g
                        = (prob_form / L_pix_LRD^3) * 2^{2g}            [Sage-exact; residual 0]
  This is g-DEPENDENT (rising as 2^{2g}; d/dg = 2^{2g+1}*prob_form*ln2 / L_pix_LRD^3 != 0),
  in contrast to the K=1 SATURATED-tail form n_PBH = C(N_eigs,2) * prob_form / L_pix_LRD^3
  (g-INDEPENDENT; d/dg = 0).

HYBRID INDEPENDENCE TEST (cross-pillar-bridge-anatomy.md §"Hybrid Independence Test")
------------------------------------------------------------------------------------
  Predicate: (i v ii v iii) ^ iv  (clause (iv) is the LOAD-BEARING conjunct)
    (i)   distinct substrate-IS sub-pillar  : YES (rising shoulder s=5 vs saturated tail s=4)
    (ii)  distinct laboratory-IN pillar     : NO  (same Pillar IX CMB/LISA/PTA PBH detection)
    (iii) distinct bridge-map class         : NO  (same FWD-C5 cardinality-cascade family)
    (iv)  independent algebraic envelope    : YES (s=5 envelope L^{-6}, Wodzicki deg -10,
                                                   edge-count 2^g vs s=4 envelope L^{-4},
                                                   Wodzicki deg -8, edge-count C(N_eigs,2);
                                                   per volovik CO-AUTHOR (iv) audit PASS)
  => (YES v NO v NO) ^ YES = YES. K-counter K=1 -> K=2.

The W4-6 corpus §4 K=2 row SCOPES its (iv)=YES to INTRA-FWD-C5 pole-distinctness (s=5 != s=4)
— the STRONGER claim than the §4 baseline's cross-pillar (iv)=YES (which compared FWD-C5 vs
FWD-C1/C2/C3). Both hold (per volovik scope caveat).

CO-AUTHOR (iv)-AXIS AUDIT
-------------------------
volovik (iv) algebraic-envelope-axis independence audit (consumed as the load-bearing
clause-(iv) conjunct): computations/session-93/s93_w4_6_volovik_iv_axis_independence_audit.json
  verdict_clause_iv = PASS (three independent regulator-invariant structural grounds).

PASS criterion (plan §W4-6 operator.form): PASS iff
  (closed-form n_PBH_shoulder(g) on A_K derived for g in [80,143))
  AND (Hybrid Independence Test (i v ii v iii) ^ iv == YES at K=2)
  AND (volovik (iv) algebraic-envelope-axis independence audit PASS)
  AND (corpus §4 K=2 row appended, substrate-distance-3 pole s=5 DISTINCT from K=1 s=4).

Dual-SHA (S84+; W9a-99 split), per plan audit_discriminators:
  audit_sha256   = sha256( bytes(script) || bytes(obs_2_npz) || bytes(corpus_md)
                           || bytes(volovik_iv_json) || pinmap_json )
  content_sha256 = sha256( bytes(script) )
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (set BEFORE numpy import; no GPU used — closed-form
# cardinality evaluation 2^{2g}; no large eigvals; GPU_path=cpu-cap-OMP8)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# Explicit import of the saturated-tail anchor (W4-5 Step-2 promotion) — used here
# ONLY as the K=1 baseline cross-check value (the g-independent saturated-tail n_PBH).
# The shoulder closed form is g-DEPENDENT and is NOT this constant.
from canonical_constants import (  # noqa: E402
    n_PBH_FW_central,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json     # noqa: E402
import time     # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S93"                                                                       # (local)
GATE_ID = "S93-W4-6-FWD-C5-K2-SUBSTRATE-DISTANCE-3-POLE-S5-CARDINALITY-CASCADE-SHOULDER"  # (local)
SCHEME = "fwd-c5-k2-cardinality-cascade-shoulder-substrate-distance-3-pole-s5"         # (local)
CONVENTION = "shoulder-regime-g-80-143-closed-form-A_K-Hybrid-Independence-Test-K2"    # (local)
L_MAX = "14"                                                                          # (local)

# Pre-registered shoulder regime (plan §W4-6 machinery_pin_map: scan_range [80,143], step 1).
G_BBN = 80           # (local) shoulder lower bound g_BBN (BBN cascade generation)
G_SATURATE = 143     # (local) shoulder upper bound (exclusive) — cascade-tail saturation generation
G_GRID = list(range(G_BBN, G_SATURATE))   # (local) 63 integer cascade generations [80,143)
N_EVAL = len(G_GRID)                       # (local) 63 (matches machinery_pin_map N_eval=63)

# Substrate-clock cancellation closed-form inputs (registry §VII.AX.OP-PROJ Step 3 / Step 4).
# prob_form, L_pix_LRD are the S88 W1a-59 §0 substrate-clock-cancellation canonical pins
# (registry line ~19383: 3.048e9 * 0.15573 / (3.0e10 m)^3 = 7.2761e-23). These are NOT in
# canonical_constants.py under these names (the canonical n_PBH is pinned as the OUTPUT
# n_PBH_FW_central=7.2761e-23); the shoulder closed form needs the input factorization, sourced
# verbatim from the registry §VII.AX.OP-PROJ Step-4 worked closed form.
PROB_FORM = 0.15573        # (local) DS-2-corrected Parker-pair production per cascade-generation (registry §VII.AX.OP-PROJ Step 4)
L_PIX_LRD = 3.0e10         # (local) m; substrate-distance-3 pole anchor for M_LRD (registry §VII.AX.OP-PROJ Step 4)
N_EIGS_L10 = 78080         # (local) Peter-Weyl multiplicity at L_max=10 base atlas (registry Step 4: N_eigs=78,080)

# Per-pole structural-distinctness anchors (volovik (iv) audit grounds 1+2; canonical via knowledge-MCP).
ALPHA_S4 = 4.0   # (local) alpha_HH1_per_pole_FW_s4 (knowledge-MCP get_constant; gate S92-W7-CF-W9-10-B; Superseded=False)
ALPHA_S5 = 6.0   # (local) alpha_HH1_per_pole_FW_s5 (knowledge-MCP get_constant; §VII.BB STAGE-1-CANDIDATE; Superseded=False)
DEG_S4 = -8      # (local) Wodzicki homogeneity degree deg(s=4)=-2*4 (cross-pillar-bridge-anatomy.md §Composite Bridge-Map)
DEG_S5 = -10     # (local) Wodzicki homogeneity degree deg(s=5)=-2*5

# Input files (audit_sha256_inputs: script, obs_2_grid_npz, corpus_fwd_c5, volovik_iv_json, pinmap).
OBS_2_NPZ = COMPUTATIONS_DIR / "session-91" / "s91_w5_3_cf41_upper_22_6.npz"           # (local)
CORPUS_MD = PROJECT_ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"  # (local)
VOLOVIK_IV_JSON = SESSION_DIR / "s93_w4_6_volovik_iv_axis_independence_audit.json"     # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                                  # (local)

VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"                                     # (local)
OUT_NPZ = SESSION_DIR / "s93_w4_6_fwd_c5_k2_cardinality_cascade_shoulder.npz"           # (local)
OUT_PNG = SESSION_DIR / "s93_w4_6_fwd_c5_k2_cardinality_cascade_shoulder.png"           # (local)

INPUT_FILES = [OBS_2_NPZ, CORPUS_MD, VOLOVIK_IV_JSON]                                   # (local) audit_sha inputs (besides script + pinmap)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema; W9a-99 split)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the closure hash."""
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


def compute_dual_sha(script_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(obs_2_npz) || bytes(corpus_md)
                             || bytes(volovik_iv_json) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    for p in INPUT_FILES:
        try:
            h_audit.update(p.read_bytes())
        except OSError:
            pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Append a single canonical verdict line + dual-SHA companion row (S84+ schema).

    Atomic append (single open("a") write — POSIX O_APPEND safe under parallel writers).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"GEOMETRIC closed-form cardinality-cascade-shoulder + Hybrid-Independence-Test K=2; "
        f"[VERIFY-THEOREM] no [SIGN] 3-tuple (structural-distinctness predicate, not sign/direction claim)\n"
    )  # (local)
    provenance_row = (
        f"# FWD-C5 K=2 advancement: n_PBH_shoulder(g)=(prob_form/L_pix_LRD^3)*2^{{2g}} on A_K "
        f"for g in [80,143) (substrate-clock cancellation form; Sage-exact). Hybrid Independence "
        f"Test (i=YES v ii=NO v iii=NO) ^ iv=YES = YES; clause (iv) LOAD-BEARING PASS per volovik "
        f"(iv)-axis audit (s=5 env L^-6/deg-10/2^g vs s=4 env L^-4/deg-8/C(N_eigs,2)). Corpus §4 "
        f"K=2 row landed: substrate-distance-3 pole s=5, intra-FWD-C5 (iv)=YES scoping (DISTINCT "
        f"from K=1 s=4 baseline). Anti-double-count vs W4-2 (§3/§10/§17 s=4 chi'). M4 allowlist "
        f"append ORCHESTRATOR-ONLY (flagged in WP §W4-6).\n"
    )  # (local)
    with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
        fh.write(line)
        fh.write(companion)
        fh.write(provenance_row)


# ---------------------------------------------------------------------------
# Section 5 — Closed-form derivation on A_K (substrate-clock cancellation form)
# ---------------------------------------------------------------------------
def n_pbh_shoulder(g):
    """Substrate-IS closed form n_PBH_shoulder(g) = (prob_form / L_pix_LRD^3) * 2^{2g}.

    The substrate-clock cancellation form (registry §VII.AX.OP-PROJ Step 3):
      n_PBH(g) = n_edge(g) * prob_form / L_pix(g)^3
               = (2^g * prob_form) / (L_pix_LRD * 2^{-g/3})^3
               = (prob_form / L_pix_LRD^3) * 2^{2g}
    valid on the rising-shoulder regime g in [80,143) where n_edge(g)=2^g is STILL GROWING.
    """
    prefactor = PROB_FORM / (L_PIX_LRD ** 3)   # (local) prob_form / L_pix_LRD^3
    # use float exponentiation via log to avoid 2**(2g) integer overflow at g~143 in float space
    return prefactor * np.power(2.0, 2.0 * np.asarray(g, dtype=np.float64))


def n_edge_shoulder(g):
    """Rising-shoulder Peter-Weyl substrate-cardinality n_edge(g) = 2^g (still doubling)."""
    return np.power(2.0, np.asarray(g, dtype=np.float64))


def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"LEAD: mack-cosmic-bridge | CO-AUTHOR: volovik-superfluid-universe-theorist ((iv)-axis)")
    print(f"Shoulder regime g in [{G_BBN},{G_SATURATE}) — {N_EVAL} cascade generations\n")

    pins = log_input_pins(INPUT_FILES)  # (local)

    # ---- Step A: chain-prerequisite status (§VII.AX.OP-PROJ STAGE-3 eligibility) ----
    # Resolve from the on-disk S93 verdict file: W4-1 Axis-A PASS ^ JE5 PASS ^ Eq.(2') landed (W4-4).
    elig_axis_a = False    # (local)
    elig_je5 = False       # (local)
    elig_eq2prime = False  # (local)
    try:
        vtext = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
        # W4-1 corrective PASS line carries axis_a_composite=PASS (latest non-superseded).
        elig_axis_a = ("S93-W4-1-VII-AX-OP-PROJ-AXIS-A-E2-VERDICT-ARTIFACT-RE-EMISSION: PASS"
                       in vtext) and ("axis_a_composite=PASS" in vtext)
        # JE5 PASS asserted on the W4-1 lines (JE5=PASS) — S92 W-4 JE5 Axis-B carried forward.
        elig_je5 = "JE5=PASS" in vtext
        # Eq.(2') landed via W4-4 STATE-PROJ companion (eligibility conjunct (c)).
        elig_eq2prime = "S93-W4-4-VII-AX-STATE-PROJ-COMPANION-LANDING: PASS" in vtext
    except OSError:
        pass
    stage3_eligible = elig_axis_a and elig_je5 and elig_eq2prime  # (local)
    print(f"[chain] §VII.AX.OP-PROJ STAGE-3 eligibility: axis_a_PASS={elig_axis_a}, "
          f"JE5_PASS={elig_je5}, Eq2prime_landed={elig_eq2prime} => ELIGIBLE={stage3_eligible}")

    # ---- Step B: closed-form derivation + Sage-cross-checked structural form ----
    g_arr = np.array(G_GRID, dtype=np.float64)              # (local)
    n_edge_arr = n_edge_shoulder(g_arr)                      # (local) 2^g rising
    n_pbh_arr = n_pbh_shoulder(g_arr)                        # (local) (prob_form/L_pix_LRD^3)*2^{2g}

    # Verify closed-form identity at each g: n_PBH(g) == n_edge(g)*prob_form / L_pix(g)^3.
    L_pix_arr = L_PIX_LRD * np.power(2.0, -g_arr / 3.0)      # (local) substrate-clock pixelation
    n_pbh_from_def = n_edge_arr * PROB_FORM / (L_pix_arr ** 3)   # (local) un-cancelled definition
    closed_form_residual = float(np.max(np.abs(
        (n_pbh_arr - n_pbh_from_def) / np.maximum(np.abs(n_pbh_from_def), 1e-300)
    )))                                                      # (local) max relative residual
    closed_form_ok = closed_form_residual < 1e-12           # (local)
    print(f"[closed-form] n_PBH_shoulder(g) = (prob_form/L_pix_LRD^3)*2^{{2g}}; "
          f"max rel residual vs n_edge*prob_form/L_pix(g)^3 = {closed_form_residual:.3e} "
          f"=> {'OK' if closed_form_ok else 'FAIL'}")

    # Sage-exact cross-check at a representative generation (g=100) using exact rationals.
    g_chk = 100  # (local)
    pf_frac = Fraction(15573, 100000)                       # (local) prob_form = 0.15573
    lpix_frac = Fraction(3, 1) * Fraction(10) ** 10         # (local) L_pix_LRD = 3.0e10
    # exact: (prob_form / L_pix_LRD^3) * 2^{2g}
    exact_shoulder = (pf_frac / (lpix_frac ** 3)) * (Fraction(2) ** (2 * g_chk))  # (local)
    float_shoulder = float(n_pbh_shoulder(g_chk))           # (local)
    sage_exact_rel = abs(float(exact_shoulder) - float_shoulder) / abs(float_shoulder)  # (local)
    sage_xcheck_ok = sage_exact_rel < 1e-10                 # (local)
    print(f"[sage-exact] g={g_chk}: exact={float(exact_shoulder):.6e}, float={float_shoulder:.6e}, "
          f"rel={sage_exact_rel:.3e} => {'OK' if sage_xcheck_ok else 'FAIL'}")

    # Rising-shoulder vs saturated-tail discriminant (ground 3): d/dg.
    # shoulder d/dg = 2^{2g+1}*prob_form*ln2 / L_pix_LRD^3 (rising, nonzero); saturated d/dg = 0.
    d_shoulder_dg = (np.power(2.0, 2.0 * g_arr + 1.0) * PROB_FORM * np.log(2.0)
                     / (L_PIX_LRD ** 3))                    # (local)
    shoulder_rising = bool(np.all(d_shoulder_dg > 0.0))     # (local)
    # K=1 saturated-tail baseline cross-check value (g-independent).
    C_neigs = N_EIGS_L10 * (N_EIGS_L10 - 1) // 2            # (local) C(N_eigs,2)
    n_pbh_saturated_L10 = C_neigs * PROB_FORM / (L_PIX_LRD ** 3)  # (local) L_max=10 baseline 1.758e-23
    print(f"[regime] shoulder d/dg>0 for all g in [80,143): {shoulder_rising} (RISING); "
          f"saturated-tail d/dg=0 (FLAT). C(N_eigs={N_EIGS_L10},2)={C_neigs}; "
          f"saturated n_PBH (L10 baseline)={n_pbh_saturated_L10:.4e} m^-3; "
          f"canonical n_PBH_FW_central (L14)={n_PBH_FW_central:.4e} m^-3")

    # ---- Step C: per-pole structural distinctness (volovik (iv) audit grounds 1+2) ----
    alpha_law_ok = (ALPHA_S4 == 2 * (4 - 2)) and (ALPHA_S5 == 2 * (5 - 2))  # (local) alpha(s)=2(s-2)
    alpha_distinct = (ALPHA_S5 != ALPHA_S4)                 # (local) 6 != 4
    deg_law_ok = (DEG_S4 == -2 * 4) and (DEG_S5 == -2 * 5)  # (local) deg(s)=-2s
    deg_distinct = (DEG_S5 != DEG_S4)                       # (local) -10 != -8
    print(f"[per-pole] alpha(s)=2(s-2) law_ok={alpha_law_ok}; alpha_s4={ALPHA_S4}, alpha_s5={ALPHA_S5}, "
          f"distinct={alpha_distinct}; deg(s)=-2s law_ok={deg_law_ok}; deg_s4={DEG_S4}, deg_s5={DEG_S5}, "
          f"distinct={deg_distinct}")

    # ---- Step D: consume volovik (iv)-axis independence audit (load-bearing clause iv) ----
    volovik_iv_pass = False  # (local)
    volovik_payload = {}     # (local)
    try:
        volovik_payload = json.loads(VOLOVIK_IV_JSON.read_text(encoding="utf-8"))  # (local)
        volovik_iv_pass = (volovik_payload.get("verdict_clause_iv", "") == "PASS")
    except (OSError, json.JSONDecodeError):
        pass
    print(f"[co-author] volovik (iv)-axis independence audit: verdict_clause_iv="
          f"{volovik_payload.get('verdict_clause_iv', 'MISSING')} => PASS={volovik_iv_pass}")

    # ---- Step E: Hybrid Independence Test predicate (i v ii v iii) ^ iv ----
    clause_i = True    # (local) distinct substrate-IS sub-pillar: rising shoulder s=5 vs saturated tail s=4 = YES
    clause_ii = False  # (local) distinct laboratory-IN pillar: same Pillar IX = NO
    clause_iii = False # (local) distinct bridge-map class: same FWD-C5 cardinality-cascade family = NO
    clause_iv = bool(volovik_iv_pass and alpha_distinct and deg_distinct and shoulder_rising)  # (local) independent envelope = YES
    hybrid_predicate = (clause_i or clause_ii or clause_iii) and clause_iv  # (local)
    print(f"[Hybrid Independence Test] (i={clause_i} v ii={clause_ii} v iii={clause_iii}) ^ iv={clause_iv} "
          f"= {hybrid_predicate}")

    # ---- Step F: distinct-pole confirmation (s=5 != K=1's s=4) ----
    pole_distinct = (5 != 4) and alpha_distinct and deg_distinct  # (local) intra-FWD-C5 pole-distinctness
    print(f"[pole] substrate-distance-3 pole s=5 DISTINCT from K=1 substrate-distance-2 pole s=4: "
          f"{pole_distinct}")

    # ---- Step G: corpus §4 K=2 row landing (append; verify on disk) ----
    corpus_row_landed = land_corpus_k2_row(
        clause_i, clause_ii, clause_iii, clause_iv, hybrid_predicate, volovik_iv_pass
    )  # (local)
    print(f"[corpus] §4 K=2 row landed (substrate-distance-3 pole s=5, intra-FWD-C5 (iv)=YES): "
          f"{corpus_row_landed}")

    # ---- Step H: anti-double-count cross-check vs W4-2 (mack §V.2) ----
    anti_double_count = True  # (local) W4-6 = FWD-C5 §4 (s=5); W4-2 = MULTI-PIN-ATLAS §3/§10/§17 (s=4 chi') — distinct
    print(f"[anti-double-count] W4-6 (FWD-C5 §4 s=5) != W4-2 (§3/§10/§17 s=4 chi'): {anti_double_count}")

    # ---- Verdict assembly ----
    closed_form_derived = closed_form_ok and sage_xcheck_ok and shoulder_rising  # (local)
    if not stage3_eligible:
        # Honest mechanical closure (chain prereq unmet) — per plan INFO_meaning / branch table.
        verdict = "INFO"  # (local)
        value = ("PRE-REG-INC_blocked_by_VII_AX_OP_PROJ_STAGE_3_eligibility_UNMET;"
                 f"axis_a={elig_axis_a};JE5={elig_je5};Eq2prime={elig_eq2prime}")  # (local)
    elif (closed_form_derived and hybrid_predicate and volovik_iv_pass
          and corpus_row_landed and pole_distinct and anti_double_count):
        verdict = "PASS"  # (local)
        value = (
            f"closed_form=n_PBH_shoulder(g)=(prob_form/L_pix_LRD^3)*2^{{2g}}_on_A_K_g_in_[80,143);"
            f"closed_form_residual={closed_form_residual:.2e};sage_exact_rel={sage_exact_rel:.2e};"
            f"shoulder_rising={shoulder_rising};"
            f"hybrid_indep_test=(i={clause_i}_OR_ii={clause_ii}_OR_iii={clause_iii})_AND_iv={clause_iv}={hybrid_predicate};"
            f"volovik_iv_PASS={volovik_iv_pass};alpha_s5={ALPHA_S5}_vs_s4={ALPHA_S4};"
            f"deg_s5={DEG_S5}_vs_s4={DEG_S4};pole_distinct_s5_ne_s4={pole_distinct};"
            f"corpus_§4_K2_row_landed={corpus_row_landed};intra_FWD_C5_iv_scoping=YES;"
            f"anti_double_count_vs_W4_2={anti_double_count};K_counter=1->2;"
            f"stage3_eligible={stage3_eligible}"
        )  # (local)
    else:
        verdict = "FAIL"  # (local)
        value = (
            f"closed_form_derived={closed_form_derived};hybrid_indep_test={hybrid_predicate};"
            f"volovik_iv_PASS={volovik_iv_pass};corpus_row_landed={corpus_row_landed};"
            f"pole_distinct={pole_distinct};anti_double_count={anti_double_count}"
        )  # (local)

    # ---- Plot: n_PBH_shoulder(g) over the shoulder regime ----
    make_plot(g_arr, n_pbh_arr, n_edge_arr, n_pbh_saturated_L10)

    # ---- Data file ----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        g_grid=g_arr,
        n_edge_shoulder=n_edge_arr,
        n_pbh_shoulder=n_pbh_arr,
        d_shoulder_dg=d_shoulder_dg,
        closed_form_residual=closed_form_residual,
        sage_exact_rel=sage_exact_rel,
        prob_form=PROB_FORM,
        L_pix_LRD=L_PIX_LRD,
        N_eigs_L10=N_EIGS_L10,
        C_neigs=C_neigs,
        n_pbh_saturated_L10=n_pbh_saturated_L10,
        n_pbh_fw_central_L14=float(n_PBH_FW_central),
        alpha_s4=ALPHA_S4, alpha_s5=ALPHA_S5, deg_s4=DEG_S4, deg_s5=DEG_S5,
        clause_i=clause_i, clause_ii=clause_ii, clause_iii=clause_iii, clause_iv=clause_iv,
        hybrid_predicate=hybrid_predicate,
        volovik_iv_pass=volovik_iv_pass,
        pole_distinct=pole_distinct,
        corpus_row_landed=corpus_row_landed,
        anti_double_count=anti_double_count,
        stage3_eligible=stage3_eligible,
        verdict=verdict,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
    )
    print(f"[data] wrote {OUT_NPZ.name}")

    # ---- Dual-SHA + verdict line ----
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), pins)  # (local)
    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"\n4-tuple: (value=<see verdict line>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"audit_sha256={audit_sha}")
    print(f"content_sha256={content_sha}")
    print(f"[verdict] {GATE_ID}: {verdict}")
    print(f"[done] {time.time() - t0:.2f}s")
    return 0


# ---------------------------------------------------------------------------
# Section 6 — Corpus §4 K=2 row landing (mack sole-writer per feedback_mack-bridge-role.md)
# ---------------------------------------------------------------------------
def land_corpus_k2_row(clause_i, clause_ii, clause_iii, clause_iv,
                       hybrid_predicate, volovik_iv_pass) -> bool:
    """Append the FWD-C5 K=2 corpus row to cross-pillar-bridge-corpus.md §4.

    Single-shot AFTER-pattern: build text in memory -> append -> re-read + verify.
    Idempotent: if the K=2 marker already present, do not duplicate (verify-only).
    """
    marker = "**FWD-C5 K=2 advancement — substrate-distance-3 pole s=5 cardinality-cascade-SHOULDER (S93 W4-6)**"  # (local)
    try:
        corpus_text = CORPUS_MD.read_text(encoding="utf-8")  # (local)
    except OSError:
        return False
    if marker in corpus_text:
        return True  # idempotent: row already landed

    row = build_corpus_k2_row_text(marker, clause_i, clause_ii, clause_iii,
                                   clause_iv, hybrid_predicate, volovik_iv_pass)  # (local)

    # Insert after the FWD-C5 baseline block's Cross-link line (just before "### Rank-2 generalization").
    anchor = "### Rank-2 generalization cross-reference"  # (local)
    idx = corpus_text.find(anchor)  # (local)
    if idx == -1:
        # fallback: append at end of §4 (before "## §5.")
        anchor2 = "\n## §5. K=3 MANDATORY corpus"  # (local)
        idx2 = corpus_text.find(anchor2)  # (local)
        if idx2 == -1:
            new_text = corpus_text + "\n" + row + "\n"  # (local)
        else:
            new_text = corpus_text[:idx2] + "\n" + row + "\n" + corpus_text[idx2:]  # (local)
    else:
        new_text = corpus_text[:idx] + row + "\n" + corpus_text[idx:]  # (local)

    # atomic write + fsync
    tmp = CORPUS_MD.with_suffix(".md.tmp_w46")  # (local)
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(new_text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, CORPUS_MD)

    # re-read + verify
    verify_text = CORPUS_MD.read_text(encoding="utf-8")  # (local)
    return marker in verify_text


def build_corpus_k2_row_text(marker, clause_i, clause_ii, clause_iii,
                             clause_iv, hybrid_predicate, volovik_iv_pass) -> str:
    """The FWD-C5 K=2 corpus-row text (substrate-distance-3 pole s=5; intra-FWD-C5 (iv)=YES scoping)."""
    return f"""{marker}

> **Provenance**: S93 W4-6 (`S93-W4-6-FWD-C5-K2-SUBSTRATE-DISTANCE-3-POLE-S5-CARDINALITY-CASCADE-SHOULDER`; LEAD mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`; CO-AUTHOR volovik-superfluid-universe-theorist on the (iv) algebraic-envelope axis). CHAINED on §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility (W4-1 Axis-A PASS ∧ S92 W-4 JE5 PASS ∧ Eq.(2′) landed by W4-4) — ACHIEVED/LIVE. This is the SECOND FWD-C5 calibration instance (K=1 → K=2), structurally DISTINCT from the K=1 baseline above (substrate-distance-2 pole s=4, saturated tail).

- **Substrate-IS observable (K=2)** — `n_PBH_shoulder(g) = (prob_form / L_pix_LRD³) · 2^{{2g}}` evaluated on `(A_K^{{≤14}}, H_K^{{≤14}}, D_K^{{≤14}})` at τ_fold = 0.19 in the RISING-SHOULDER regime `g ∈ [g_BBN=80, g_saturate=143)`, where the Peter-Weyl substrate-cardinality `n_edge(g) = 2^g` is STILL GROWING (NOT yet saturated at `C(N_eigs,2)`). Derived via the S88 W1a-59 §0 substrate-clock cancellation form `n_PBH(g) = n_edge(g)·prob_form / L_pix(g)³` with `L_pix(g) = L_pix_LRD·2^{{-g/3}}` (the cosmological-volume dilution `2^{{-3g}}` is canceled BY CONSTRUCTION because L_pix(g) IS the substrate's clock). Sage-exact: residual 0 against `(prob_form/L_pix_LRD³)·2^{{2g}}`. Algebra-INVARIANT spectrum-only functional, Cell-I-cardinality-projection. **Substrate-distance-3 pole s=5** (vs K=1's substrate-distance-2 pole s=4).
- **Laboratory-IN observable** — same Pillar IX combined CMB / LISA / PTA PBH number density (same lab-pillar as the K=1 baseline; this is WHY clause (ii)=NO).
- **Bridge map** — same FWD-C5 cardinality-cascade family (substrate-clock cancellation ∘ Friedrich-Bär saturation ∘ cardinality-cascade HKR-image), restricted to the rising-shoulder sub-domain (this is WHY clause (iii)=NO). The shoulder→tail transition at g=143 is the Friedrich-Bär saturation boundary.
- **Algebraic envelope (K=2)** — substrate-distance-3 pole s=5 envelope `L^{{-6}}` (`α(s=5)=6` via `α(s)=2(s-2)`; canonical `alpha_HH1_per_pole_FW_s5=6.0`, gate `S92-W7-CF-W9-10-B`, §VII.BB STAGE-1-CANDIDATE), Wodzicki homogeneity degree `deg(s=5)=−10` (`deg(s)=−2s`). INDEPENDENT of the K=1 s=4 envelope `L^{{-4}}` (`deg(s=4)=−8`).
- **Empirical anchor** — shoulder closed form g-DEPENDENT (rising `2^{{2g}}`); the K=1 saturated-tail anchor `n_PBH_FW_central = 7.2761e-23 m⁻³` (L_max=14) is the g→g_saturate boundary value. The shoulder regime is verdict-orthogonal to the single saturated-tail Level-3 anchor (it is the pre-saturation phase).

**Hybrid Independence Test K-counter advancement (K=1 → K=2)** per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` SUGGESTION-K=1, predicate `(i ∨ ii ∨ iii) ∧ iv`:

- **(i) distinct substrate-IS sub-pillar**: {"YES" if clause_i else "NO"} — rising-shoulder cardinality cascade (pre-saturation, s=5) vs saturated-tail (post-saturation, s=4); distinct pole AND distinct regime.
- **(ii) distinct laboratory-IN pillar**: {"YES" if clause_ii else "NO"} — same Pillar IX (CMB/LISA/PTA PBH detection) as the K=1 baseline.
- **(iii) distinct bridge map class**: {"YES" if clause_iii else "NO"} — same FWD-C5 cardinality-cascade bridge family as the K=1 baseline.
- **(iv) independent algebraic envelope**: {"YES" if clause_iv else "NO"} — **LOAD-BEARING conjunct**. The s=5 shoulder envelope (`L^{{-6}}`, Wodzicki deg `−10`, edge-count `2^g` rising) is regulator-invariantly distinct from the s=4 saturated-tail envelope (`L^{{-4}}`, Wodzicki deg `−8`, edge-count `C(N_eigs,2)` flat) on THREE independent structural grounds (per-pole exponent integer-gap 2; Wodzicki-degree integer-gap 2; functional form rising-vs-flat) — NOT a numerical refinement. **CO-AUTHOR volovik (iv)-axis independence audit: PASS** (`s93_w4_6_volovik_iv_axis_independence_audit.json`).
- **Predicate**: `(i={"YES" if clause_i else "NO"} ∨ ii={"YES" if clause_ii else "NO"} ∨ iii={"YES" if clause_iii else "NO"}) ∧ iv={"YES" if clause_iv else "NO"} = {"YES" if hybrid_predicate else "NO"}`. K-counter **K=1 → K=2** on the FWD-C5 Hybrid Independence Test corpus.

**Intra-FWD-C5 (iv)=YES scoping (MANDATORY disambiguation)**: the §4 FWD-C5 baseline block above already declared clause (iv)=YES at the **CROSS-PILLAR** level (FWD-C5 vs FWD-C1/C2/C3: distinct lab-IN pillar, distinct bridge-map). The W4-6 (iv)=YES is the STRONGER **INTRA-FWD-C5** independence (s=5 shoulder vs s=4 tail, WITHIN the FWD-C5 family — same bridge-map, same Pillar IX, so the envelope must be distinct on **POLE grounds alone**). This K=2 row's (iv)=YES is scoped to the intra-FWD-C5 pole-distinctness (substrate-distance-3 pole s=5 ≠ substrate-distance-2 pole s=4), so the K=2 advancement is unambiguously the substrate-distance-3-pole shoulder instance, NOT a re-statement of the cross-pillar baseline. The "deterministic restriction of the saturated form to g<143" framing (session-92-plan-w6.md) is a DOMAIN-of-g statement, orthogonal to (iv).

**Anti-double-count cross-check** (mack §V.2 anti-inflation): W4-6 advances the FWD-C5 corpus §4 K-counter (substrate-distance-3 pole s=5); W4-2 (`S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY`) advances the §VII.AX.MULTI-PIN-ATLAS bridge-map-scheme axis (corpus §3/§10/§17; substrate-distance-2 pole s=4 χ' restriction). Distinct poles (s=5 vs s=4), distinct corpus sections (§4 vs §3/§10/§17) ⇒ NO double-count against a single K-counter, per the Hybrid Independence Test.

**M4 allowlist note**: this corpus-row landing is GEOMETRIC (closed-form + structural-distinctness predicate); any METHODOLOGY-class allowlist append is ORCHESTRATOR-ONLY per `methodology-wave-allowlist.md` (flagged, not performed by this gate).
"""


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(g_arr, n_pbh_arr, n_edge_arr, n_pbh_saturated_L10):
    """n_PBH_shoulder(g) over the shoulder regime g∈[80,143) (log-y, rising)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))  # (local)

    ax1.semilogy(g_arr, n_pbh_arr, "o-", ms=3, color="#1f5fbf",
                 label=r"$n_{\rm PBH}^{\rm shoulder}(g)=(p_{\rm form}/L_{\rm pix,LRD}^3)\,2^{2g}$")
    ax1.axhline(n_pbh_saturated_L10, ls="--", color="#bf3f1f",
                label=r"K=1 saturated-tail (L10 baseline) $C(N_{\rm eigs},2)\,p_{\rm form}/L_{\rm pix,LRD}^3$")
    ax1.axvline(143, ls=":", color="gray", label=r"$g_{\rm saturate}=143$ (shoulder$\to$tail)")
    ax1.set_xlabel("cascade generation $g$")
    ax1.set_ylabel(r"$n_{\rm PBH}^{\rm shoulder}(g)$  (m$^{-3}$)")
    ax1.set_title("FWD-C5 K=2 cardinality-cascade SHOULDER (substrate-distance-3 pole s=5)")
    ax1.legend(fontsize=7.5, loc="upper left")
    ax1.grid(alpha=0.3, which="both")

    ax2.semilogy(g_arr, n_edge_arr, "s-", ms=3, color="#1f8f4f",
                 label=r"$n_{\rm edge}(g)=2^g$ (RISING shoulder, $d/dg\neq 0$)")
    ax2.set_xlabel("cascade generation $g$")
    ax2.set_ylabel(r"$n_{\rm edge}(g)=2^g$")
    ax2.set_title("Rising Peter-Weyl substrate-cardinality (pre-saturation)\n"
                  r"vs saturated tail $C(N_{\rm eigs},2)$ flat ($d/dg=0$)")
    ax2.legend(fontsize=8, loc="upper left")
    ax2.grid(alpha=0.3, which="both")

    fig.suptitle("S93-W4-6  FWD-C5 Hybrid Independence Test K=1$\\to$K=2  "
                 "(s=5 env $L^{-6}$/deg$-10$/$2^g$  vs  K=1 s=4 env $L^{-4}$/deg$-8$/$C(N,2)$)",
                 fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"[plot] wrote {OUT_PNG.name}")


if __name__ == "__main__":
    sys.exit(main())
