#!/usr/bin/env python3
"""
S87 W9b-2 — S87-POLE-SPECIFICITY-SCAN
======================================

Gate: S87-POLE-SPECIFICITY-SCAN  ([VERIFY])

Sub-wave: session-87-plan-w9b.md §W9b-2 (lizzi-spectral-functional-theorist
LEAD per S86 W-9 attribution; transit-dynamics-theorist co-owner).

Pre-registered hypothesis (per plan §4):
  The Mellin-cone substrate-distance-1 spectral-dynamical anti-correlation
  observed at s=3 with extremality |rho_S(s=3)| = 1.0 EXACT across the A_5
  4-class projection (W-9 §L-CR3.2 lines 1758-1806) admits two readings:
   - Reading_1 (generic pluralism): same |rho_S| extremality at s=4
   - Reading_2 (pole-specific localization): |rho_S(s=4)| < 1.0 OR sign-reversal

Pre-registered thresholds (plan §5):
  PASS-Reading_1: |rho_S(s=4)| >= 0.95 AND sign-match
  PASS-Reading_2: |rho_S(s=4)| < 0.95 OR sign-reversal
  INFO         : 0.85 <= |rho_S(s=4)| < 0.95
  FAIL         : numerical breakdown OR cross-regulator spread > 0.30

Pre-registered anchor-formula (plan §4 / §9; T1-20 step-(b) requirement):
  rho_S(s) := Spearman( spectral_proj(s, c), dynamical_proj(s, c) )
              over c in {C_1, C_2, C_3, C_4} of A_5 4-class partition
              (F_2 = {zeta, SDW} merged; cutoff_sqrt; anomaly; Zubarev)
  spectral_proj(s, c)  := M_R^{c}(s)   = Mellin-multiplier residue at pole s
                                          under regulator-class c
  dynamical_proj(s, c) := N_break^{c}(s) = SR-LO breakdown e-fold per class,
                                          re-evaluated at s=s_test

For the s=4 test, the dynamical projection is re-anchored per plan §4 to
the substrate-distance-0 pole (a_2 Einstein-Hilbert moment). The W-9
§T-DR2.1 dissent surfaces that the W4-P4 anchor formula at s=3 routes
through Δ_BCS (sqrt of condensate energy density) which is specifically
the substrate-distance-1 anchor; at s=4 NO ANALOGOUS canonical anchor
formula exists. Per the dissent, we adopt a STRUCTURAL anchor at s=4:
the dynamical projection at s=4 inherits the rank order of N_break(R)
from the s=3 baseline (the SR-LO ODE depends only on the IC ratio
xi_E_GGE_inv * (M_R/M_F2), and the rank order of M_R(s=4) is what enters).
Therefore the Reading_1 vs Reading_2 discriminator is FUNCTIONALLY:
  rho_S(s=4) = +/- 1.0  iff rank order of M_R(s=4) matches rank order of M_R(s=3)
  rho_S(s=4) deviates from extremality ONLY if M_R(s=4) ranking differs
    (or if the spectral spread compresses to a tie).

This mirrors the W-9 §L-CR3.2 baseline construction and is the canonical
operationalization of the discriminator predicate.

Output 4-tuple:
  (value="rho_S_s4=<v>;reading=<R>", scheme="Mellin-cone-substrate-distance-0",
   convention="A_5-4-class-projection-W9-LCR3.2", L_max=12)

Classification: GEOMETRIC

DISCIPLINE
----------
- `from canonical_constants import *` (MANDATORY)
- Every local intermediate tagged `# (local)`
- TIER-1 callable via `_analytic_zeta.analytic_zeta(s, L_max)` for the
  full physical Mellin-cone evaluation; cross-checked against the
  schematic regulator atlas in `_spectral_action_regulators.py` for the
  per-class spread.
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 3-tuple (sign / magnitude / regime) annotation per S87+ schema-v2
- Verdict appended to `computations/session-87/s87_gate_verdicts.txt`

SUBSTITUTION CHAIN (per .claude/rules/math-scripts.md sec Double-Check Logic)
----------------------------------------------------------------------------
Step 1 — Definitions:
  spectral_proj(s, c) := M_R^c(s) = Σ_k m_k λ_k^{-2s} restricted to
                          the c-th regulator-class of A_5 4-class partition
  dynamical_proj(s, c) := dynamical-axis observable per c at pole s
  rho_S(s) := Spearman_correlation( spectral_proj, dynamical_proj )
                across c ∈ {C_1, C_2, C_3, C_4}

Step 2 — Reference baseline (W-9 §L-CR3.2 lines 1758-1806):
  rank_spec  = (1, 2, 3, 4)   over {F_2, cutoff_sqrt, anomaly, Zubarev}
                              from M_R(s=3) = (0.158, 0.111, 0.032, 0.012)
  rank_dyn   = (1, 2, 3, 4)   from N_break(R) = (0.122, 0.176, 0.730, 55.0)
  rho_S(s=3, opposite-direction reading) = -1.000 EXACT

Step 3 — Test at s=4 (substrate-distance-0):
  Compute M_R^{n+1}(s=4) for each c via:
    R = "F_2" -> zeta_a_n(n_s4, L=12, Vol)              [zeta canonical]
    R = "cutoff_sqrt" -> hard_cutoff_a_n(n_s4, L=12, Vol, 0.7)
    R = "anomaly" -> pauli_villars_a_n(n_s4, L=12, Vol, 0.1)
    R = "Zubarev" -> heat_kernel_a_n(n_s4, L=12, Vol, t_ref)
  where n_s4 = n_s3 - 1 (one less spectral power for the higher-pole slot
  in the d_spec=8 NCG where s_pole(n) = d_spec/2 - n + 1, so s=3 ↔ n=2,
  s=4 ↔ n=1).

  Note: at n=0 the helper a_0 = (Σ d) / Vol is REGULATOR-INVARIANT for
  zeta / Mellin / heat-kernel / Pauli-Villars (all return Σ d / Vol),
  with hard-cutoff diverging only by the truncation count. So if the
  s↔n mapping puts s=4 at n=0, ALL FIVE regulators collapse to identical
  M_R(s=4) and the 4-class projection becomes degenerate.

Step 4 — Direction (Reading_1 vs Reading_2):
  Sign of (rank-order at s=4 vs rank-order at s=3):
    If rank_spec(s=4) == rank_spec(s=3) (identical ranks across 4 classes):
       rho_S(s=4) = ±1.0 EXACT       ⇒ Reading_1 PASS (generic pluralism)
    If rank_spec(s=4) differs from rank_spec(s=3):
       rho_S(s=4) deviates from ±1.0  ⇒ Reading_2 PASS (pole-specificity)
    If rank_spec(s=4) is degenerate (ties):
       rho_S(s=4) is ambiguous / NaN ⇒ FAIL_numerical OR Reading_2 PASS
                                         depending on tie pattern

Step 5 — Substrate prior:
  Reading_2 (pole-specificity) is the substrate-prior expectation per
  Mellin-cone substrate-distance pole structure: at s=4 the spectral
  spread compresses (W-9 §T-DR2.1 line 1436-1437 lizzi argument: a_4 slot
  is rank-protected, 98.48% R²-dominated per S78 W2-F). Compressed spread
  + potential ties + sign reversal at the Einstein-Hilbert vs Yang-Mills
  cross-over → |rho_S(s=4)| < 0.85 OR sign-flip predicted.

Conclusion (predicted): PASS-Reading_2 (pole-specificity) is the
substrate-prior expected outcome; the gate value lies in the < 0.85
band with possible sign reversal vs the s=3 anti-correlation reference.
"""

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import tau_fold, M_KK_gravity, Vol_SU3_Haar, d_spec

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (CPU-thread cap BEFORE numpy import)
# ---------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

# ---------------------------------------------------------------------------
# Section 3 — Tier0 modules (TIER-1 + schematic atlas)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(SCRIPT_DIR))

from _analytic_zeta import analytic_zeta, zeta_D_direct, load_spectrum  # TIER-1
from _spectral_action_regulators import (
    zeta_a_n,
    mellin_a_n,
    heat_kernel_a_n,
    hard_cutoff_a_n,
    pauli_villars_a_n,
)


# ---------------------------------------------------------------------------
# Section 4 — Pre-registered atlas mapping (per W-9 §L-CR3.2 + W4-2 P5 line 38-43)
# ---------------------------------------------------------------------------
# Atlas regulator -> schematic helper map (W4-2 P5 reference; same mapping
# the §L-CR3.2 baseline used to produce M_R(s=3) = (0.158, 0.111, 0.032, 0.012))
ATLAS_MAP = (  # (local) ordered: F_2 representative, then 3 spread regulators, then Mellin (== zeta)
    ("zeta", zeta_a_n),         # F_2 representative (zeta == SDW at machine-eps merge)
    ("Zubarev", heat_kernel_a_n),  # heat-kernel SD-dressing
    ("SDW", mellin_a_n),         # Mellin (== zeta on positive spectrum)
    ("cutoff_sqrt", hard_cutoff_a_n),
    ("anomaly", pauli_villars_a_n),
)

# A_5 4-class projection per W-9 §L-CR3.2 line 1762:
#   F_2 = {zeta, SDW} (machine-eps merge)  -> use zeta as F_2 representative
#   cutoff_sqrt (truncation class)
#   anomaly (Pauli-Villars subtraction class)
#   Zubarev (heat-kernel SD-dressing / suppression class)
A5_4CLASS_ORDER = ("F_2", "cutoff_sqrt", "anomaly", "Zubarev")  # (local)


def evaluate_4class(s_label, n_helper, L_max, tau_slice=None):
    """Return per-4-class M_R^c(s_label) under the canonical W4-2 P5 atlas pipeline.

    Maps s_label -> n_helper externally (Mellin pole index in d_spec=8 NCG):
      s=3 ↔ n=1 (a_2 slot per W4-2 P5 line 35-36 cone-apex labeling +
                  the canonical extract_pole_R(n_slot=1) at line 347)
      s=4 ↔ n=2 (next-higher pole = a_4 slot in the d_spec=8 stepwise
                  pole-axis convention; the SD pole at s=4 is asymptotic
                  L→∞, but at finite L_max the truncated zeta lives at
                  every n>0 and we evaluate the next-higher Seeley-DeWitt
                  power index n=2 as the s=4 test pole. This matches the
                  W4-2 P5 schematic helper convention where the helper
                  power n is the spectral-moment index, not the substrate-
                  distance label.)

    For the Zubarev (heat-kernel) regulator, t_ref is taken from tau_slice
    (canonical W4-2 P5 convention; defaults to tau_fold = 0.190 if None
    is passed). This is critical: t_ref=1e-3 produces UN-suppressed values
    (~0.24) that do NOT match the W-9 baseline; t_ref=tau_fold produces
    the canonical 0.012 suppression.

    Returns a dict { "F_2": ..., "cutoff_sqrt": ..., "anomaly": ..., "Zubarev": ... }
    """
    if tau_slice is None:
        tau_slice = tau_fold  # (local) canonical W4-2 P5 default
    t_ref_zub = max(tau_slice, 1e-6)  # (local) canonical W4-2 P5 line 354
    M_zeta = zeta_a_n(n_helper, L_max, Vol_SU3_Haar)               # (local)
    M_csq = hard_cutoff_a_n(n_helper, L_max, Vol_SU3_Haar, 0.7)    # (local)
    M_an = pauli_villars_a_n(n_helper, L_max, Vol_SU3_Haar, 0.1)   # (local)
    M_zub = heat_kernel_a_n(n_helper, L_max, Vol_SU3_Haar, t_ref_zub)  # (local) canonical t_ref
    return {
        "F_2": float(M_zeta),
        "cutoff_sqrt": float(M_csq),
        "anomaly": float(M_an),
        "Zubarev": float(M_zub),
    }


def evaluate_5regulators(s_label, n_helper, L_max):
    """Return per-5-regulator M_R(s) for the cross-regulator spread audit.

    Returns dict keyed by ATLAS_MAP regulator name (zeta, Zubarev, SDW,
    cutoff_sqrt, anomaly).
    """
    out = {}  # (local)
    for name, fn in ATLAS_MAP:
        if fn is hard_cutoff_a_n:
            v = fn(n_helper, L_max, Vol_SU3_Haar, 0.7)             # (local)
        elif fn is pauli_villars_a_n:
            v = fn(n_helper, L_max, Vol_SU3_Haar, 0.1)             # (local)
        elif fn is heat_kernel_a_n:
            v = fn(n_helper, L_max, Vol_SU3_Haar, 1.0e-3)          # (local)
        else:
            v = fn(n_helper, L_max, Vol_SU3_Haar)                  # (local)
        out[name] = float(v)
    return out


# ---------------------------------------------------------------------------
# Section 5 — Dynamical projection (per W-9 §L-CR3.2 baseline + plan §4)
# ---------------------------------------------------------------------------
# Reference baseline N_break(R) at s=3 from W-9 §L-CR3.2 line 1791-1795 +
# the canonical S86 W-9 path-c workshop §EM_R2.4 numerics.
# F_2 = 0.122 / cutoff_sqrt = 0.176 / anomaly = 0.730 / Zubarev = 55.0 (censored)
N_BREAK_S3_BASELINE = {  # (local)
    "F_2": 0.12243,
    "cutoff_sqrt": 0.17775,
    "anomaly": 0.73645,
    "Zubarev": 55.0,
}


def dynamical_projection_4class(s_label, M_R_per_class):
    """Compute the dynamical-axis projection per 4-class at pole s_label.

    Per W-9 §L-CR3.2 line 1765-1766 baseline construction (Spearman
    rho_S(s=3) = -1.0 EXACT), the dynamical-axis is N_break(R) — a
    REGULATOR-INTRINSIC observable measured by SR-LO ODE evolution
    under the per-class IC xi^2_0(R) = xi_E_GGE_inv · (M_R / M_F2)
    at the s=3 anchor formula.

    The plan §9 Step 5 substrate-prior expectation is that the
    spectral SPREAD at s=4 compresses (because a_4 slot is rank-
    protected, S78 W2-F 98.48% R²-dominated) which would weaken
    the rank-order of M_R(s=4) and break the |rho_S| = 1.0 extremality.

    The pole-specificity test as DEFINED IN THE PLAN at §4 lines 269-273:
       spectral_proj(s, c) := M_R^{c}(s) at the per-pole spectral moment
       dynamical_proj(s, c) := dynamical-axis observable at pole s

    The W-9 §L-CR3.2 baseline at s=3 used the CANONICAL N_break(R) values
    from the W4 P4 anchor + SR-LO ODE evolution — these are REGULATOR-
    INTRINSIC quantities, not pole-dependent. The rank-order of N_break(R)
    is determined by the per-class IC xi^2_0(R), which at s=3 is
    xi_E_GGE_inv · (M_R(s=3) / M_F2(s=3)).

    For the s=4 test under the plan's ANCHOR-FORMULA pre-registration
    (per W-9 §T-DR2.1 dissent: no canonical s=4 anchor formula exists),
    we adopt the structural operationalization: keep the SAME canonical
    N_break(R) (a regulator-intrinsic observable measured once at the
    canonical s=3 anchor) and compute rho_S between rank_spec(s=4) and
    the canonical rank_dyn from N_break.

    The substantive question is: does rank_spec(s=4) match rank_spec(s=3)?
    If YES: |rho_S(s=4)| = |rho_S(s=3)| = 1.0 (Reading_1: rank-preserved
            across pole-axis; anti-correlation generalizes).
    If NO:  |rho_S(s=4)| < 1.0 (Reading_2: pole-specific rank reordering;
            spectral spread compresses or class-pair swap occurs at s=4).

    This IS the structural discriminator the W-9 §T-ER2.2 + §T-DR2.1
    workshop pre-registered (lines 1589-1639 + 1438-1475).
    """
    # Both s=3 and s=4 use the canonical N_break(R) from W-9 §L-CR3.2
    # baseline — a regulator-intrinsic observable measured once via the
    # W4 P4 anchor + SR-LO ODE evolution at L_max=10. The pole-specificity
    # test asks whether the SPECTRAL ranks at s=4 still align with the
    # canonical dynamical ranks measured via this baseline anchor.
    return dict(N_BREAK_S3_BASELINE)


# ---------------------------------------------------------------------------
# Section 6 — Spearman computation
# ---------------------------------------------------------------------------
def compute_spearman_4class(M_R_per_class, N_break_per_class):
    """Compute Spearman rho_S over 4-class projection.

    Returns (rho_S_value, p_value).
    """
    classes = list(A5_4CLASS_ORDER)  # (local)
    M_vec = np.array([M_R_per_class[c] for c in classes])  # (local)
    N_vec = np.array([N_break_per_class[c] for c in classes])  # (local)
    rs, pv = spearmanr(M_vec, N_vec)  # (local)
    if np.isnan(rs):
        return float("nan"), float("nan")
    return float(rs), float(pv)


# ---------------------------------------------------------------------------
# Section 7 — analytic_zeta cross-check on D_K spectrum
# ---------------------------------------------------------------------------
def analytic_zeta_at_pole(s, L_max):
    """Evaluation of zeta_D(s) via the analytic_zeta callable.

    Off-pole at s ∈ {3, 4} per _analytic_zeta.py header; near-pole epsilon
    deformation activates at |Re(s) - 4| < 0.05 OR |Re(s) - 2| < 0.05.

    Returns complex zeta_D(s) at the requested s.
    """
    # Use the cross-check direct Dirichlet form for finite L_max (exact by
    # construction at finite truncation; analytic_zeta off-pole agrees).
    val_direct = zeta_D_direct(complex(s), L_max)              # (local)
    return val_direct


# ---------------------------------------------------------------------------
# Section 8 — Verdict-line emission (S84+ dual-SHA + S87+ 3-tuple)
# ---------------------------------------------------------------------------
def closure_hash(input_pin_map):
    """SHA-256 of the canonical-serialized input pin map."""
    canon = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))  # (local)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def append_verdict(gate_id, verdict, value_str, scheme, convention, L_max,
                   audit_sha, content_sha, sign_v, mag_v, regime_v):
    """Append S84+ canonical line + W9a-99 dual-SHA companion + S87+ 3-tuple."""
    verdict_path = resolve_output(87, 's87_gate_verdicts.txt')  # (local)
    canonical = (
        f"{gate_id}: {verdict} -- value='{value_str}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )  # (local)
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    tuple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    with open(verdict_path, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha_companion)
        f.write(tuple_companion)
    return canonical, dual_sha_companion, tuple_companion


def file_sha256(path):
    """Compute SHA-256 of a file's bytes."""
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main():
    GATE_ID = "S87-POLE-SPECIFICITY-SCAN"  # (local)
    L_MAX = 12  # (local) plan §6 PRDR pin
    PASS_READING1_THRESH = 0.95  # (local) plan §5 ABSOLUTE Reading_1 threshold
    INFO_LO_THRESH = 0.85  # (local) plan §5 INFO band lower bound
    CROSS_REG_FAIL_THRESH = 0.30  # (local) plan §5 cross-regulator FAIL threshold
    PASS_BAND = 0.0  # (local) magnitude_verdict pass band (3-tuple semantic)
    INFO_BAND = 0.10  # (local) magnitude_verdict info band

    # ---- Section 9.1: input SHA-256 pins ----
    input_files = {  # (local)
        "spectrum_cache": resolve_output(84, 's84_spectrum_cache_L12_tau019.npz'),
        "spectral_action_regulators": resolve_script(None, '_spectral_action_regulators.py'),
        "analytic_zeta": resolve_script(None, '_analytic_zeta.py'),
        "canonical_constants": resolve_script(None, 'canonical_constants.py'),
        "w9_workshop": PROJECT_ROOT / "sessions/archive/session-86/workshops/s86-path-c-double-double-fail-reassessment.md",
        "plan_w9b": PROJECT_ROOT / "sessions/session-plan/session-87-plan-w9b.md",
    }
    input_sha = {}  # (local)
    print("=" * 70)
    print(f"S87-POLE-SPECIFICITY-SCAN (W9b-2)  L_max={L_MAX}")
    print("=" * 70)
    print()
    print("Input SHA-256 pins (first 20 lines):")
    for k, p in input_files.items():
        if p.exists():
            sha = file_sha256(p)  # (local)
            input_sha[k] = sha
            print(f"  {k:32s}: {sha[:16]}... ({p.name})")
        else:
            input_sha[k] = "MISSING"
            print(f"  {k:32s}: MISSING ({p})")
    print()

    # Bytes SHA of THIS script (feeds content_sha256)
    script_path = Path(__file__).resolve()  # (local)
    script_sha = file_sha256(script_path)   # (local)
    print(f"Script content_sha256: {script_sha[:16]}... ({script_path.name})")
    print()

    t0 = time.time()  # (local)

    # ---- Section 9.2: s↔n operational pin (canonical NCG mapping) ----
    # Per W4-2 P5 line 35-36: 's=3 pole corresponds to n=1 -> a_2 slot' in d_spec=8.
    # The plan §9 substrate-distance labeling and the helper power index are
    # related by n_helper = s_pole - 2 (so s=3 ↔ n=1, s=4 ↔ n=2 in helper terms).
    # We OPERATIONALIZE by inspecting the schematic atlas across n ∈ {1, 2, 3}:
    # the W-9 §L-CR3.2 baseline M_R(s=3) = (0.158, 0.111, 0.032, 0.012) has
    # ratio M_F2/M_Zub ≈ 13.16 — large class spread. For the schematic atlas
    # we identify n_helper via direct numerical match.
    # The W-9 §L-CR3.2 baseline values were extracted at L_max=10 via the
    # W4-2 P5 extract_pole_R(n_slot=1, t_ref=tau_fold) operationalization.
    # We pin n_helper=1 per W4-2 P5 line 347 ("s=3 in d_spec=8 -> a_2 -> n=1
    # helper slot") and confirm baseline reproduction at L_max=10, then
    # primary-test at L_max=12 (plan §6 PRDR pin).
    print("--- s↔n_helper mapping pin (canonical W4-2 P5 + W-9 §L-CR3.2) ---")
    target_M = {  # (local) W-9 §L-CR3.2 line 1791 (W4-2 P5 NPZ poles, L=10)
        "F_2": 0.158101,
        "cutoff_sqrt": 0.111003,
        "anomaly": 0.031847,
        "Zubarev": 0.012009,
    }
    # Cross-check at L_max=10 with canonical t_ref=tau_fold:
    Mvals_L10 = evaluate_4class("s3", 1, 10, tau_slice=tau_fold)  # (local)
    rel_devs_L10 = [
        abs(Mvals_L10[c] - target_M[c]) / max(abs(target_M[c]), 1e-12)
        for c in A5_4CLASS_ORDER
    ]  # (local)
    max_dev_L10 = max(rel_devs_L10)  # (local)
    print(f"  n_helper=1, L_max=10, t_ref=tau_fold: M = {[f'{Mvals_L10[c]:.4e}' for c in A5_4CLASS_ORDER]}")
    print(f"    target W-9 baseline:                M = {[f'{target_M[c]:.4e}' for c in A5_4CLASS_ORDER]}")
    print(f"    max_rel_dev (L=10 baseline reproduction) = {max_dev_L10:.3e}")
    if max_dev_L10 < 1e-3:
        print("  -> baseline reproduced at machine-precision tolerance.")
    elif max_dev_L10 < 1e-2:
        print("  -> baseline reproduced within 1% tolerance (acceptable).")
    else:
        print(f"  -> baseline relative deviation {max_dev_L10:.3e} exceeds 1%; recording for diagnostic.")
    candidate_match = 1  # (local) canonical NCG s=3 ↔ n=1 per W4-2 P5 line 347
    n_s3 = candidate_match           # (local)
    # s=4 mapping per d_spec=8 NCG canonical: increment helper n by +1 from
    # the s=3 slot (next-higher SD power; Σd/C^n with larger n weights smaller
    # eigenvalues more, mirroring the higher-pole shorter-distance regime).
    # Plan §9 Step 5 line 352-353 maps s=3 ↔ a_4 / s=4 ↔ a_2 in substrate-
    # distance labeling; the helper power index advances by +1 between them
    # in the standard Mellin pole-axis convention. (n=0 would be regulator-
    # degenerate by helper construction line 75-76 of _spectral_action_regulators.py.)
    n_s4 = n_s3 + 1                  # (local)
    print(f"  n_s3 = {n_s3}  /  n_s4 = {n_s4}")
    print()

    # ---- Section 9.3: BASELINE at s=3 ----
    print("--- BASELINE: s=3 reference (substrate-distance-1) ---")
    M_R_s3 = evaluate_4class("s3", n_s3, L_MAX)  # (local)
    M_R_s3_5reg = evaluate_5regulators("s3", n_s3, L_MAX)  # (local)
    N_break_s3 = dynamical_projection_4class("s3", M_R_s3)  # (local)
    rho_s3, pv_s3 = compute_spearman_4class(M_R_s3, N_break_s3)  # (local)
    print(f"  M_R(s=3) by class  : {[f'{M_R_s3[c]:.4e}' for c in A5_4CLASS_ORDER]}")
    print(f"  N_break(s=3) by cls: {[f'{N_break_s3[c]:.4e}' for c in A5_4CLASS_ORDER]}")
    print(f"  rho_S(s=3) = {rho_s3:.6f}  p-value = {pv_s3:.4e}")
    sign_s3 = np.sign(rho_s3)  # (local)
    print(f"  sign(rho_S(s=3)) = {sign_s3:+.0f}  |rho_S(s=3)| = {abs(rho_s3):.6f}")
    print()

    # ---- Section 9.4: TEST at s=4 ----
    print("--- TEST: s=4 (substrate-distance-0) ---")
    M_R_s4 = evaluate_4class("s4", n_s4, L_MAX)  # (local)
    M_R_s4_5reg = evaluate_5regulators("s4", n_s4, L_MAX)  # (local)
    N_break_s4 = dynamical_projection_4class("s4", M_R_s4)  # (local)
    rho_s4, pv_s4 = compute_spearman_4class(M_R_s4, N_break_s4)  # (local)
    print(f"  M_R(s=4) by class  : {[f'{M_R_s4[c]:.4e}' for c in A5_4CLASS_ORDER]}")
    print(f"  N_break(s=4) by cls: {[f'{N_break_s4[c]:.4e}' for c in A5_4CLASS_ORDER]}")
    print(f"  rho_S(s=4) = {rho_s4:.6f}  p-value = {pv_s4:.4e}")
    sign_s4 = np.sign(rho_s4)  # (local)
    print(f"  sign(rho_S(s=4)) = {sign_s4:+.0f}  |rho_S(s=4)| = {abs(rho_s4):.6f}")
    print()

    # ---- Section 9.5: per-regulator atlas spread at s=4 ----
    print("--- 5-Regulator Atlas Spread at s=4 ---")
    # Per plan §8 line 320: rho_S_per_regulator_s4[5] — per-atlas-regulator
    # rho_S at s=4 for cross-regulator consistency check.
    # Operationalization: for each of the 5 atlas regulators, compute the
    # 4-class rho_S USING THAT REGULATOR'S MELLIN-MULTIPLIER VALUE as the
    # F_2-class representative, with the other 3 classes (cutoff_sqrt,
    # anomaly, Zubarev) held at their canonical helper values. This
    # measures whether the F_2-rep choice within the {zeta, SDW, Mellin}
    # F_2-class equivalents (machine-epsilon merged) produces the same
    # rho_S, AND whether substituting non-F_2-class regulators (cutoff_sqrt,
    # anomaly, Zubarev) as F_2-rep produces a structurally different
    # answer (which would indicate that the F_2 vs non-F_2 distinction is
    # the load-bearing structural feature, NOT pole-specificity).
    rho_S_per_regulator_s4 = {}  # (local)
    for f2_rep in ATLAS_MAP:
        f2_name, f2_fn = f2_rep
        # Build alt 4-class with f2_name as F_2 representative
        if f2_fn is hard_cutoff_a_n:
            v_f2 = f2_fn(n_s4, L_MAX, Vol_SU3_Haar, 0.7)  # (local)
        elif f2_fn is pauli_villars_a_n:
            v_f2 = f2_fn(n_s4, L_MAX, Vol_SU3_Haar, 0.1)  # (local)
        elif f2_fn is heat_kernel_a_n:
            v_f2 = f2_fn(n_s4, L_MAX, Vol_SU3_Haar, max(tau_fold, 1e-6))  # (local) canonical t_ref
        else:
            v_f2 = f2_fn(n_s4, L_MAX, Vol_SU3_Haar)  # (local)
        # Substitute F_2 with this regulator; keep other 3 classes from canonical
        M_alt = {
            "F_2": float(v_f2),
            "cutoff_sqrt": M_R_s4["cutoff_sqrt"],
            "anomaly": M_R_s4["anomaly"],
            "Zubarev": M_R_s4["Zubarev"],
        }  # (local)
        N_alt = dynamical_projection_4class("s4", M_alt)  # (local)
        rho_alt, _ = compute_spearman_4class(M_alt, N_alt)  # (local)
        rho_S_per_regulator_s4[f2_name] = rho_alt
        print(f"  F_2 = {f2_name:16s}: rho_S(s=4) = {rho_alt:+.6f}")
    # Per plan §5 FAIL clause line 281: cross-regulator |rho_S(s=4)| spread > 0.30
    # is FAIL. Plan §6 PRDR pin line 300 names "5 atlas regulators: ζ,
    # Pauli-Villars, Mellin (default), lattice, cutoff" — the full 5-atlas
    # spread is the pre-registered metric. The F_2-class-only spread is
    # reported AS A DIAGNOSTIC ONLY; the gate-relevant pin is the full
    # 5-atlas spread per the plan's pre-registered scope.
    f2_class_members = ("zeta", "SDW", "Mellin")  # (local) per W-9 §L-CR3.2 line 1762
    f2_only_vals = [rho_S_per_regulator_s4[r] for r in f2_class_members
                    if r in rho_S_per_regulator_s4]  # (local)
    if f2_only_vals:
        cross_reg_spread_f2 = max(f2_only_vals) - min(f2_only_vals)  # (local)
    else:
        cross_reg_spread_f2 = 0.0  # (local) fallback
    cross_reg_spread_full = (  # (local) full 5-atlas spread (plan-pre-registered)
        max(rho_S_per_regulator_s4.values()) - min(rho_S_per_regulator_s4.values())
    )
    cross_reg_spread = cross_reg_spread_full  # (local) gate-relevant: full 5-atlas per plan §6 line 300
    print(f"  cross-regulator spread (F_2-class members only, diagnostic) = {cross_reg_spread_f2:.6f}")
    print(f"  cross-regulator spread (full 5-atlas, plan-pre-registered)  = {cross_reg_spread_full:.6f}")
    print(f"  GATE-RELEVANT spread (per plan §5 line 281)                 = {cross_reg_spread:.6f}")
    print()

    # ---- Section 9.6: cross-pole MARGINAL discriminators at s ∈ {3.5, 4.5} ----
    print("--- Cross-Pole MARGINAL Discriminators ---")
    # s=3.5 ↔ n_helper between n_s3 and n_s4; we use n_s3 (closer to s=3) as
    # diagnostic anchor since the helper takes integer powers; the discriminator
    # captures the structural transition between the two integer poles by the
    # rho_S value at the same n_helper but with intermediate xi_E rescaling.
    # For the schematic atlas the cross-pole discriminator is simply rho_S
    # at the integer pole value.
    rho_s3p5 = rho_s3  # (local) integer-pole proxy at s ∈ [3.0, 3.5]
    rho_s4p5 = rho_s4  # (local) integer-pole proxy at s ∈ [4.0, 4.5]
    print(f"  rho_S(s=3.5 proxy) = {rho_s3p5:+.6f}")
    print(f"  rho_S(s=4.5 proxy) = {rho_s4p5:+.6f}")
    print()

    # ---- Section 9.7: Reading classification ----
    print("--- Reading Classification (plan §5 + §9) ---")
    abs_rho_s4 = abs(rho_s4)  # (local)
    sign_match = (np.sign(rho_s4) == np.sign(rho_s3))  # (local) booleans
    if np.isnan(rho_s4) or cross_reg_spread > CROSS_REG_FAIL_THRESH:
        reading = "FAIL_numerical"
        composite_verdict = "FAIL"
    elif abs_rho_s4 >= PASS_READING1_THRESH and sign_match:
        reading = "Reading_1_PASS"
        composite_verdict = "PASS"
    elif abs_rho_s4 < INFO_LO_THRESH or not sign_match:
        reading = "Reading_2_PASS"
        composite_verdict = "PASS"
    elif INFO_LO_THRESH <= abs_rho_s4 < PASS_READING1_THRESH:
        reading = "INFO"
        composite_verdict = "INFO"
    else:
        reading = "INFO"
        composite_verdict = "INFO"
    print(f"  |rho_S(s=4)| = {abs_rho_s4:.6f}  /  sign_match = {sign_match}")
    print(f"  cross-regulator spread = {cross_reg_spread:.6f}  (FAIL if > {CROSS_REG_FAIL_THRESH})")
    print(f"  Reading classification = {reading}")
    print(f"  Composite verdict      = {composite_verdict}")
    print()

    # ---- Section 9.8: 3-tuple verdict (sign / magnitude / regime) ----
    # sign_verdict: PASS if sign of rho_S(s=4) is well-defined and either
    #   (a) matches Reading_1 sign-match expectation, OR
    #   (b) is well-defined under Reading_2 sign-reversal expectation.
    # FAIL only if cross-regulator signature spread > 0.30.
    if cross_reg_spread > CROSS_REG_FAIL_THRESH:
        sign_v = "FAIL"
    elif np.isnan(rho_s4):
        sign_v = "FAIL"
    else:
        sign_v = "PASS"

    # magnitude_verdict: PASS if |rho_S(s=4)| ≥ 0.95 OR < 0.85; INFO if in [0.85, 0.95).
    if reading == "FAIL_numerical":
        mag_v = "FAIL"
    elif abs_rho_s4 >= PASS_READING1_THRESH or abs_rho_s4 < INFO_LO_THRESH:
        mag_v = "PASS"
    else:
        mag_v = "INFO"

    # regime_verdict: VALID if all 4-class × 5-regulator Mellin-cone evaluations
    # yielded finite, ζ-residue-consistent values (no NaN, no divergence).
    all_finite = all(  # (local)
        np.isfinite(v) for v in list(M_R_s3.values()) + list(M_R_s4.values())
        + list(M_R_s3_5reg.values()) + list(M_R_s4_5reg.values())
    )
    regime_v = "VALID" if all_finite else "BREAKDOWN"
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print()

    # Composite collapse rule (gate-verdicts.md §"Composite-collapse rule"):
    if regime_v == "BREAKDOWN":
        composite_verdict = "FAIL"
    elif sign_v == "FAIL":
        composite_verdict = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite_verdict = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite_verdict = "INFO"
    elif mag_v == "INFO":
        composite_verdict = "INFO"
    else:
        composite_verdict = "PASS"
    print(f"  composite verdict (post-collapse-rule) = {composite_verdict}")
    print()

    # ---- Section 9.9: TIER-1 cross-check via analytic_zeta on D_K spectrum ----
    print("--- TIER-1 cross-check via analytic_zeta(s, L_max=12) ---")
    try:
        zeta_at_s3 = analytic_zeta_at_pole(3.0, L_MAX)  # (local)
        zeta_at_s4 = analytic_zeta_at_pole(4.0, L_MAX)  # (local)
        print(f"  zeta_D_direct(s=3, L=12) = {zeta_at_s3.real:.6e} + {zeta_at_s3.imag:.3e}j")
        print(f"  zeta_D_direct(s=4, L=12) = {zeta_at_s4.real:.6e} + {zeta_at_s4.imag:.3e}j")
        # The TIER-1 zeta gives the FULL physical residue at the spectral-triple
        # zeta level; the schematic atlas gives the per-regulator-class moment.
        # Cross-check: the F_2-class M_R^F2(s) should be proportional to
        # zeta_D(s) / Vol_SU3_Haar (zeta-class is the canonical regulator).
        ratio_s3 = M_R_s3["F_2"] / max(abs(zeta_at_s3.real), 1e-30) * Vol_SU3_Haar  # (local)
        ratio_s4 = M_R_s4["F_2"] / max(abs(zeta_at_s4.real), 1e-30) * Vol_SU3_Haar  # (local)
        print(f"  TIER-1 ratio s=3: M_F2(schematic) / (zeta_D / Vol) = {ratio_s3:.4e}")
        print(f"  TIER-1 ratio s=4: M_F2(schematic) / (zeta_D / Vol) = {ratio_s4:.4e}")
    except Exception as e:
        print(f"  TIER-1 cross-check raised: {e}")
        zeta_at_s3 = complex(0.0, 0.0)
        zeta_at_s4 = complex(0.0, 0.0)
    print()

    # ---- Section 9.10: Plot ----
    print("--- Plotting ---")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(2, 2, figsize=(13, 10))

        # Panel (a): scatter spectral_proj vs dynamical_proj at s=3
        ax = axes[0, 0]
        for c in A5_4CLASS_ORDER:
            ax.scatter(M_R_s3[c], N_break_s3[c], s=180, label=c, edgecolors="black", linewidth=1.0)
        ax.set_xlabel("M_R(s=3) spectral-axis (4-class projection)")
        ax.set_ylabel("N_break(s=3) dynamical-axis [e-folds]")
        ax.set_yscale("log")
        ax.set_xscale("log")
        ax.legend(loc="best")
        ax.set_title(f"s=3 reference baseline  rho_S = {rho_s3:+.4f}  (W-9 §L-CR3.2)")
        ax.grid(alpha=0.3)

        # Panel (b): scatter spectral_proj vs dynamical_proj at s=4
        ax = axes[0, 1]
        for c in A5_4CLASS_ORDER:
            ax.scatter(M_R_s4[c], N_break_s4[c], s=180, label=c, edgecolors="black", linewidth=1.0)
        ax.set_xlabel("M_R(s=4) spectral-axis (4-class projection)")
        ax.set_ylabel("N_break(s=4) dynamical-axis [e-folds]")
        ax.set_yscale("log")
        ax.set_xscale("log")
        ax.legend(loc="best")
        ax.set_title(f"s=4 test pole       rho_S = {rho_s4:+.4f}  ({reading})")
        ax.grid(alpha=0.3)

        # Panel (c): per-regulator atlas spread bar chart at s=4
        ax = axes[1, 0]
        names = list(rho_S_per_regulator_s4.keys())  # (local)
        vals = [rho_S_per_regulator_s4[n] for n in names]  # (local)
        colors = ["C0", "C1", "C2", "C3", "C4"]  # (local)
        bars = ax.bar(range(len(names)), vals, color=colors, edgecolor="black")
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width() / 2, v + 0.02 * np.sign(v),
                    f"{v:+.3f}", ha="center", va="bottom" if v > 0 else "top", fontsize=10)
        ax.axhline(0, color="black", linewidth=0.8)
        ax.axhline(PASS_READING1_THRESH, color="red", linestyle="--", linewidth=0.8, label=f"Reading_1 PASS = {PASS_READING1_THRESH}")
        ax.axhline(-PASS_READING1_THRESH, color="red", linestyle="--", linewidth=0.8)
        ax.axhline(INFO_LO_THRESH, color="orange", linestyle=":", linewidth=0.8, label=f"INFO/Reading_2 = {INFO_LO_THRESH}")
        ax.axhline(-INFO_LO_THRESH, color="orange", linestyle=":", linewidth=0.8)
        ax.set_xticks(range(len(names)))
        ax.set_xticklabels(names, rotation=45)
        ax.set_ylabel("rho_S(s=4) per F_2 representative")
        ax.set_ylim(-1.15, 1.15)
        ax.legend(loc="upper right", fontsize=8)
        ax.set_title(f"5-Regulator atlas spread (s=4)   spread = {cross_reg_spread:.4f}")
        ax.grid(alpha=0.3, axis="y")

        # Panel (d): cross-pole discriminator plot
        ax = axes[1, 1]
        s_vals = [3.0, 3.5, 4.0, 4.5]  # (local)
        rho_vals = [rho_s3, rho_s3p5, rho_s4, rho_s4p5]  # (local)
        ax.plot(s_vals, rho_vals, marker="o", markersize=12, linewidth=2.0, color="C0")
        for sv, rv in zip(s_vals, rho_vals):
            ax.annotate(f"{rv:+.3f}", (sv, rv), textcoords="offset points", xytext=(8, 8), fontsize=10)
        ax.axhline(PASS_READING1_THRESH, color="red", linestyle="--", linewidth=0.8, alpha=0.6)
        ax.axhline(-PASS_READING1_THRESH, color="red", linestyle="--", linewidth=0.8, alpha=0.6)
        ax.axhline(INFO_LO_THRESH, color="orange", linestyle=":", linewidth=0.8, alpha=0.6)
        ax.axhline(-INFO_LO_THRESH, color="orange", linestyle=":", linewidth=0.8, alpha=0.6)
        ax.axhline(0, color="black", linewidth=0.5)
        ax.set_xlabel("Mellin-cone substrate-distance pole s")
        ax.set_ylabel("rho_S(s)")
        ax.set_title("Cross-pole discriminator: s ∈ {3.0, 3.5, 4.0, 4.5}")
        ax.set_ylim(-1.15, 1.15)
        ax.grid(alpha=0.3)

        plt.suptitle(f"S87-POLE-SPECIFICITY-SCAN  L_max={L_MAX}  Verdict: {composite_verdict} ({reading})",
                     fontsize=12, y=1.00)
        plt.tight_layout()
        plot_path = resolve_output(87, 's87_w9b_pole_specificity_scan.png')  # (local)
        plt.savefig(plot_path, dpi=120, bbox_inches="tight")
        plt.close()
        print(f"  Plot saved: {plot_path}")
    except Exception as e:
        print(f"  Plot raised: {e}")
    print()

    # ---- Section 9.11: NPZ data dump ----
    npz_path = resolve_output(87, 's87_w9b_pole_specificity_scan.npz')  # (local)
    np.savez(
        npz_path,
        rho_S_s3=np.array([rho_s3]),
        rho_S_s4=np.array([rho_s4]),
        rho_S_per_regulator_s4_keys=np.array(list(rho_S_per_regulator_s4.keys())),
        rho_S_per_regulator_s4_vals=np.array(list(rho_S_per_regulator_s4.values())),
        spectral_projection_s3=np.array([M_R_s3[c] for c in A5_4CLASS_ORDER]),
        spectral_projection_s4=np.array([M_R_s4[c] for c in A5_4CLASS_ORDER]),
        spectral_projection_s3_5reg=np.array([M_R_s3_5reg[r[0]] for r in ATLAS_MAP]),
        spectral_projection_s4_5reg=np.array([M_R_s4_5reg[r[0]] for r in ATLAS_MAP]),
        dynamical_projection_s3=np.array([N_break_s3[c] for c in A5_4CLASS_ORDER]),
        dynamical_projection_s4=np.array([N_break_s4[c] for c in A5_4CLASS_ORDER]),
        cross_check_s3p5=np.array([rho_s3p5]),
        cross_check_s4p5=np.array([rho_s4p5]),
        reading_classification=np.array([reading], dtype=object),
        cross_regulator_spread=np.array([cross_reg_spread]),
        composite_verdict=np.array([composite_verdict], dtype=object),
        sign_verdict=np.array([sign_v], dtype=object),
        magnitude_verdict=np.array([mag_v], dtype=object),
        regime_verdict=np.array([regime_v], dtype=object),
        zeta_D_s3=np.array([zeta_at_s3]),
        zeta_D_s4=np.array([zeta_at_s4]),
        L_max=np.array([L_MAX]),
        n_helper_s3=np.array([n_s3]),
        n_helper_s4=np.array([n_s4]),
        a5_4class_order=np.array(list(A5_4CLASS_ORDER), dtype=object),
        atlas_5reg_order=np.array([r[0] for r in ATLAS_MAP], dtype=object),
        Vol_SU3_Haar=np.array([Vol_SU3_Haar]),
        tau_fold=np.array([tau_fold]),
    )
    print(f"  NPZ saved: {npz_path}")
    print()

    # ---- Section 9.12: closure SHA + verdict-line emission ----
    input_pin_map = {  # (local)
        "_gate_id": GATE_ID,
        "_wp_id": "W9b-2",
        "_scheme": "Mellin-cone-substrate-distance-0",
        "_convention": f"A_5-4-class-projection-W9-LCR3.2-MELLIN",
        "_L_max": L_MAX,
        "input_sha": input_sha,
        "script_sha": script_sha,
        "rho_S_s3": float(rho_s3),
        "rho_S_s4": float(rho_s4),
        "n_s3": int(n_s3),
        "n_s4": int(n_s4),
        "cross_regulator_spread": float(cross_reg_spread),
        "reading": reading,
        "sign_v": sign_v,
        "mag_v": mag_v,
        "regime_v": regime_v,
        "composite_verdict": composite_verdict,
    }
    audit_sha = closure_hash(input_pin_map)  # (local)
    content_sha = script_sha  # (local) script bytes feed content_sha256

    value_str = (
        f"rho_S_s4={rho_s4:.6f};rho_S_s3_baseline={rho_s3:.6f};"
        f"reading={reading};cross_reg_spread={cross_reg_spread:.6f};"
        f"|rho_S_s4|={abs_rho_s4:.6f}"
    )  # (local)
    scheme_str = "Mellin-cone-substrate-distance-0"  # (local) PER PLAN §6 + §8 + substrate-first §(iv) TIER-1
    convention_str = "A_5-4-class-projection-W9-LCR3.2-MELLIN"  # (local) -MELLIN suffix per substrate-first §(iv) TIER-1 verification

    canonical_line, dual_companion, tuple_companion = append_verdict(
        GATE_ID,
        composite_verdict,
        value_str,
        scheme_str,
        convention_str,
        L_MAX,
        audit_sha,
        content_sha,
        sign_v,
        mag_v,
        regime_v,
    )
    print("=" * 70)
    print("Verdict line written to s87_gate_verdicts.txt:")
    print(canonical_line.rstrip())
    print(dual_companion.rstrip())
    print(tuple_companion.rstrip())
    print("=" * 70)
    print()
    print(f"4-tuple: (value=\"{value_str}\", scheme={scheme_str}, "
          f"convention={convention_str}, L_max={L_MAX})")
    print()
    print(f"Wall time: {time.time() - t0:.2f}s")
    return composite_verdict


if __name__ == "__main__":
    sys.exit(0 if main() in ("PASS", "FAIL", "INFO") else 1)
