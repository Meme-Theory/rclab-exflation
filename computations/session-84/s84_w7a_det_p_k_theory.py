#!/usr/bin/env python3
"""
S84 W7a-74 — DET-P-K-THEORY (K-theoretic uplift of det(P)=1 to Witten 1998)
==========================================================================

Gate: S84-DET-P-K-THEORY ([VERIFY])

Pre-registered thresholds (from session-84-plan-w7a.md §W7a-74):
  PASS: structure-preserving map phi: KK^6(A_F, A_F^o) -> K^0(M^4 x X_fiber)
        exists that carries det(P)=1 to Witten's anomaly-cancellation identity
        at K_0 level. Map respects Bott periodicity AND torsion classes.
  INFO: map exists at homotopy level (classifying-space equivalence) but is
        not structure-preserving at K_0. Homotopically equivalent but
        algebraically distinct.
  FAIL: no map exists; obstruction identified in a specific KK-group
        (KK^6 torsion, Bott periodicity mismatch, or K_0 rank mismatch).

Classification: GEOMETRIC (Kasparov KK^6 structural identity)
Scheme: Kasparov_KK
Convention: Witten_1998
L_max: NA (K-theoretic, not spectral)

METHODOLOGY
-----------
6-step substitution chain per plan §W7a-74:
  1. S45 permanent: det(P)=1 with K_0(A_F) = Z^3 (SM A_F = C + H + M_3(C))
  2. Bott periodicity: KO^6(pt) = Z/2 torsion; K^0(pt) = Z torsion-free;
     complexification KO^6 -> K^0 is zero map.
  3. Chern character: ch_0(fundamental class) = rank of projection on
     H_F^+ half-generation = 16.
  4. A-roof genus: M^4 flat at the fold (no Pontryagin classes active at
     the emergent-geometry scale), A-roof(TM^4) = 1.
  5. Witten's anomaly integral: int ch wedge A-roof = 16 * 1 = 16.
     Witten single-brane normalization requires integral = 1.
  6. Classification: 16 != 1 in Z; 16 = 0 mod 8 (KO Bott period); no
     K_0 iso exists (rank Z^3 != rank Z). Obstruction identified.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU numpy.linalg sufficient (8x8 matrices)
- SHA-256 of all input files logged in first 20 lines of stdout
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to s84_gate_verdicts.txt with SHA pin
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
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

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
ARCHIVE_DIR = PROJECT_ROOT / "computations" / "_shared"

SESSION = "S84"                          # (local)
GATE_ID = "S84-DET-P-K-THEORY"           # (local)
SCHEME = "Kasparov_KK"                   # (local)
CONVENTION = "Witten_1998"               # (local)
L_MAX = "N/A"                            # (local)

# Output destinations
OUT_NPZ = resolve_output(84, 's84_w7a_74_data.npz')
OUT_PNG = resolve_output(84, 's84_w7a_74_plot.png')
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

# Input files for SHA-256 pinning
INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    ARCHIVE_DIR / "s45_occupied_cyclic.py",    # S45 provenance for det(P)=1
    ARCHIVE_DIR / "s45_occupied_cyclic.npz",   # S45 output data
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        pins[rel] = sha
        print(f"  {rel}: {sha[:16]}...")
    return pins


def closure_hash(pins) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute: 6-step substitution chain
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Execute the 6-step K-theoretic uplift substitution chain.

    Returns a dict with all intermediate values, final homotopy_level,
    and diagnostic data for the npz output.
    """
    print()
    print("=" * 72)
    print("SUBSTITUTION CHAIN — K-theoretic uplift of det(P)=1")
    print("=" * 72)

    results = {}  # (local)

    # -------------------------------------------------------------------
    # STEP 1: S45 permanent — det(P) = 1 in KK^6(A_F, A_F^o)
    # -------------------------------------------------------------------
    # A_F = C + H + M_3(C); K_0(A_F) = Z^3 (one generator per summand)
    # Vacuum pairing matrix P^vac = diag(1,1,1) (normalized traces on
    # orthogonal summands). Framework permanent (S45 Theorem 5):
    #   det(P^occ) = det(W) * det(P^vac) != 0 for any physical occupation.
    # -------------------------------------------------------------------
    print()
    print("STEP 1: S45 permanent det(P) = 1")
    print("-" * 72)

    # The K_0(A_F) = Z^3 pairing matrix (diagonal, unit traces)
    P_K0 = np.diag([1.0, 1.0, 1.0])   # (local) S45 diagonal pairing
    det_P_K0 = float(np.linalg.det(P_K0))  # (local)
    print(f"  K_0(A_F) = Z^3 pairing: P = diag(1,1,1)")
    print(f"  det(P_K0) = {det_P_K0}")

    # Plan's 8x8 interpretation: KK^6 fundamental class rank-8 projection
    # on half of H_F^+ (single chirality) — used for Bott-periodicity mapping
    P_8x8 = np.eye(8)  # (local) KK^6 fundamental-class rank-8 block
    det_P_8x8 = float(np.linalg.det(P_8x8))  # (local)
    print(f"  KK^6 fundamental-class rank-8 block: P_8x8 = I_8")
    print(f"  det(P_8x8) = {det_P_8x8}")

    assert det_P_K0 == 1.0, "S45 permanent violated"
    assert det_P_8x8 == 1.0, "KK^6 rank-8 identity violated"

    results['step1_det_P_K0'] = det_P_K0
    results['step1_det_P_8x8'] = det_P_8x8
    results['step1_K0_rank'] = 3   # rank of K_0(A_F)

    # -------------------------------------------------------------------
    # STEP 2: Bott periodicity — KO^6(pt) = Z/2, K^0(pt) = Z
    # -------------------------------------------------------------------
    # Real Bott periodicity: KO^n ~ KO^{n+8}
    # KO^0, KO^4 = Z (torsion-free)
    # KO^1, KO^2 = Z/2 (torsion)
    # KO^6 = Z/2 (torsion) via KO^6 ~ KO^{-2}
    # Complex Bott periodicity: K^n ~ K^{n+2}
    # K^0 = Z, K^1 = 0 (for connected base point)
    # Complexification c: KO -> K:
    #   c: KO^0(pt) = Z -> K^0(pt) = Z, multiplication by 2 (real dim = 2*complex)
    #   c: KO^6(pt) = Z/2 -> K^0(pt) = Z, ZERO MAP (torsion killed)
    # -------------------------------------------------------------------
    print()
    print("STEP 2: Bott periodicity and complexification")
    print("-" * 72)

    KO_6_ring = 'Z/2'              # (local) real K-theory at KO-dim 6
    K_0_ring = 'Z'                 # (local) complex K-theory
    c_KO6_to_K0_rank = 0           # (local) rank of complexification map
    torsion_KO6 = 2                # (local) Z/2 torsion order
    torsion_K0 = 0                 # (local) no torsion in Z

    print(f"  KO^6(pt) = {KO_6_ring} (torsion, order {torsion_KO6})")
    print(f"  K^0(pt)  = {K_0_ring} (torsion-free)")
    print(f"  Complexification c: KO^6 -> K^0 is zero map (rank {c_KO6_to_K0_rank})")
    print(f"  => Framework's KO-dim=6 torsion class is KILLED by complexification.")

    results['step2_KO6_torsion'] = torsion_KO6
    results['step2_K0_torsion'] = torsion_K0
    results['step2_complexification_rank'] = c_KO6_to_K0_rank

    # -------------------------------------------------------------------
    # STEP 3: Chern character of fundamental class
    # -------------------------------------------------------------------
    # For the SM finite algebra A_F = C + H + M_3(C) acting on H_F = C^32
    # (per generation), the chirality-positive half H_F^+ has complex
    # dimension 16. The fundamental class in KK^6(A_F, A_F^o) is
    # represented by the unit projection, and its Chern character at
    # degree 0 is:
    #   ch_0(fund) = rank of representation = 16
    # Higher ch_k vanish because the finite algebra is 0-dimensional
    # (no differential forms).
    # -------------------------------------------------------------------
    print()
    print("STEP 3: Chern character of Kasparov fundamental class")
    print("-" * 72)

    dim_HF_full = 32    # (local) H_F complex dim per generation
    dim_HF_half = 16    # (local) chirality-positive half
    ch_0_fund = float(dim_HF_half)   # (local) ch_0 = rank
    ch_k_higher = 0.0                # (local) ch_k = 0 for k >= 1

    print(f"  H_F (per generation, full) = C^{dim_HF_full}")
    print(f"  H_F^+ (chirality-positive half) = C^{dim_HF_half}")
    print(f"  ch_0(fundamental class) = {ch_0_fund}")
    print(f"  ch_k(fundamental class) = {ch_k_higher} for k >= 1 (0-dim algebra)")

    results['step3_ch_0'] = ch_0_fund
    results['step3_dim_HF_half'] = dim_HF_half

    # -------------------------------------------------------------------
    # STEP 4: A-roof genus on effective M^4 at the fold
    # -------------------------------------------------------------------
    # A-roof(TM) = 1 - p_1/24 + (7*p_1^2 - 4*p_2)/5760 + ...
    # At the fold (tau = tau_fold), M^4 is emergent and effectively flat
    # at the scale relevant to fiber-level K-theory: the Pontryagin
    # classes p_1, p_2 are DERIVED from the fiber spectral geometry and
    # are zero in the "bare" M^4 that the K-theoretic uplift would map
    # onto. This is consistent with:
    #   (a) Emergent gravity: p_i arise from a_2 Seeley-DeWitt moment,
    #       not from M^4 itself
    #   (b) Framework substrate framing: M^4 is NOT a curved background
    #       carrying the fiber; it IS the emergent spectral coordinate
    # -------------------------------------------------------------------
    print()
    print("STEP 4: A-roof genus on emergent M^4")
    print("-" * 72)

    p_1 = 0.0   # (local) first Pontryagin number (flat emergent M^4)
    p_2 = 0.0   # (local) second Pontryagin number
    a_roof_M4 = 1.0 - p_1/24.0 + (7.0*p_1**2 - 4.0*p_2)/5760.0  # (local)

    print(f"  p_1(TM^4) at fold = {p_1} (flat emergent M^4)")
    print(f"  p_2(TM^4) at fold = {p_2}")
    print(f"  A-roof(TM^4) = 1 - p_1/24 + (7*p_1^2 - 4*p_2)/5760 = {a_roof_M4}")

    results['step4_a_roof'] = a_roof_M4

    # -------------------------------------------------------------------
    # STEP 5: Witten's anomaly-cancellation integral
    # -------------------------------------------------------------------
    # Witten 1998 "D-Branes and K-Theory" (JHEP 9812:019):
    #   D-brane charge Q in K^0(X) has cancellation integral
    #   int_X ch(Q) /\ A-roof(TX) = integer (charge in K^0 units)
    # Single-brane (unit-charge) normalization requires integral = 1.
    # For the framework's fundamental class pushed forward to M^4 x X:
    #   int = ch_0(fund) * A-roof(TM^4) = 16 * 1 = 16
    # -------------------------------------------------------------------
    print()
    print("STEP 5: Witten anomaly-cancellation integral")
    print("-" * 72)

    witten_integral = ch_0_fund * a_roof_M4   # (local)
    witten_required_unit_brane = 1.0          # (local) single-brane Witten target

    print(f"  Witten identity: int_X ch(Q) /\\ A-roof(TX) = charge in K^0 units")
    print(f"  Single-brane normalization: integral must equal {witten_required_unit_brane}")
    print(f"  Framework: int = ch_0 * A-roof = {ch_0_fund} * {a_roof_M4} = {witten_integral}")

    absolute_diff = abs(witten_integral - witten_required_unit_brane)  # (local)
    print(f"  |framework - Witten_required| = {absolute_diff}")

    # Bott-period modular checks
    mod_8_KO = int(witten_integral) % 8   # (local) real Bott period
    mod_2_K = int(witten_integral) % 2    # (local) complex Bott period
    print(f"  {int(witten_integral)} mod 8 (KO Bott period) = {mod_8_KO}")
    print(f"  {int(witten_integral)} mod 2 (K Bott period) = {mod_2_K}")

    results['step5_witten_integral'] = witten_integral
    results['step5_witten_required'] = witten_required_unit_brane
    results['step5_abs_diff'] = absolute_diff
    results['step5_mod_8_KO'] = mod_8_KO
    results['step5_mod_2_K'] = mod_2_K

    # -------------------------------------------------------------------
    # STEP 6: Classification of uplift homotopy level
    # -------------------------------------------------------------------
    # Check three successive criteria:
    #
    # Level 3 (PASS - strong): structure-preserving K_0 isomorphism
    #   Requires: rank K_0(A_F) = rank K^0(X) AND torsion match
    #   Framework: rank K_0(A_F) = 3 vs rank K^0(X) = 1 -> RANK MISMATCH
    #   Framework: K_0(A_F) torsion-free vs KO^6 Z/2 torsion -> TORSION MISMATCH
    #   Level 3: FAIL
    #
    # Level 2 (INFO - weak): classifying-space homotopy equivalence
    #   Requires: B(K_0(A_F)) ~_h B(K^0(X)) (same homotopy groups)
    #   pi_0(BU^3 x Z^3) = Z^3; pi_0(BU x Z) = Z -> pi_0 mismatch
    #   Level 2: FAIL
    #
    # Level 1: Z-linear map phi: Z^3 -> Z exists sending (1,1,1) to 1
    #   Many such maps exist (e.g., projection (a,b,c) -> a)
    #   Level 1: EXISTS but not an iso/equivalence
    #
    # Level 0: no map at all
    #   Level 0: FAIL (maps exist)
    # -------------------------------------------------------------------
    print()
    print("STEP 6: Homotopy-level classification")
    print("-" * 72)

    # --- Level 3 (structure-preserving K_0 iso) ---
    rank_K0_AF = 3                          # (local) K_0(A_F) = Z^3
    rank_K0_X = 1                           # (local) K^0(X) connected base = Z
    rank_iso_possible = (rank_K0_AF == rank_K0_X)  # (local)
    torsion_match = (torsion_K0 == torsion_KO6)    # (local)
    level_3_PASS = rank_iso_possible and torsion_match  # (local)

    print(f"  Level 3 (structure-preserving K_0 iso):")
    print(f"    rank K_0(A_F) = {rank_K0_AF}, rank K^0(X) = {rank_K0_X}")
    print(f"    Rank iso possible: {rank_iso_possible}")
    print(f"    Torsion match: {torsion_match} "
          f"(framework={torsion_K0} vs KO^6={torsion_KO6})")
    print(f"    Level 3: {'PASS' if level_3_PASS else 'FAIL'}")

    # --- Level 2 (classifying-space homotopy equivalence) ---
    pi_0_AF_rank = 3                         # (local) rank of pi_0
    pi_0_X_rank = 1                          # (local)
    pi_0_match = (pi_0_AF_rank == pi_0_X_rank)  # (local)
    level_2_PASS = pi_0_match                    # (local) necessary condition

    print(f"  Level 2 (classifying-space homotopy equivalence):")
    print(f"    pi_0 of B(K_0(A_F)) = Z^{pi_0_AF_rank}")
    print(f"    pi_0 of B(K^0(X)) = Z^{pi_0_X_rank}")
    print(f"    pi_0 match: {pi_0_match}")
    print(f"    Level 2: {'PASS' if level_2_PASS else 'FAIL'}")

    # --- Level 1 (Z-linear map exists sending distinguished class) ---
    # phi: Z^3 -> Z, phi(1,1,1) = 1
    # Need n1+n2+n3 = 1 with integer n_i. E.g., (n1,n2,n3) = (1,0,0).
    # Exists iff 1 is in the image of the sum map, which is trivially true.
    level_1_map_exists = True  # (local) always exists
    level_1_example_coeffs = (1, 0, 0)  # (local) projection onto first summand

    print(f"  Level 1 (Z-linear map phi: Z^3 -> Z sending det=1 to charge=1):")
    print(f"    Exists: {level_1_map_exists}")
    print(f"    Example: phi(a,b,c) = {level_1_example_coeffs[0]}*a + "
          f"{level_1_example_coeffs[1]}*b + {level_1_example_coeffs[2]}*c")
    print(f"    (Such a map is a projection, NOT an isomorphism)")

    # --- Final homotopy level assignment ---
    # Level 3 is PASS criterion in plan thresholds
    # Level 2 is INFO criterion
    # Level 1 (map exists but not iso/eq) -> Level 0 effectively: FAIL
    # since plan FAIL criterion says 'no structure-preserving map'
    #
    # Homotopy level integer code for verdict reporting:
    #   3 = strong structural iso (PASS)
    #   2 = classifying-space equivalence (INFO)
    #   1 = weak map only (FAIL with map)
    #   0 = no map (FAIL without map)

    if level_3_PASS:
        homotopy_level = 3    # (local)
        verdict = "PASS"      # (local)
    elif level_2_PASS:
        homotopy_level = 2    # (local)
        verdict = "INFO"      # (local)
    elif level_1_map_exists:
        homotopy_level = 1    # (local)
        verdict = "FAIL"      # (local)
    else:
        homotopy_level = 0    # (local)
        verdict = "FAIL"      # (local)

    print()
    print(f"  Final homotopy level: {homotopy_level}")
    print(f"  Pre-registered verdict: {verdict}")

    results['step6_level_3_PASS'] = level_3_PASS
    results['step6_level_2_PASS'] = level_2_PASS
    results['step6_level_1_map_exists'] = level_1_map_exists
    results['homotopy_level'] = homotopy_level
    results['verdict'] = verdict

    # -------------------------------------------------------------------
    # OBSTRUCTION IDENTIFICATION (for FAIL case)
    # -------------------------------------------------------------------
    print()
    print("OBSTRUCTION ANALYSIS")
    print("-" * 72)
    obstructions = []  # (local)
    if not rank_iso_possible:
        obstructions.append(f"K_0 rank mismatch: Z^{rank_K0_AF} vs Z^{rank_K0_X}")
    if not torsion_match:
        obstructions.append(
            f"Torsion mismatch: framework K_0 torsion-free vs KO^6 = Z/{torsion_KO6}"
        )
    if abs(witten_integral - witten_required_unit_brane) > 1e-10:
        obstructions.append(
            f"Witten integral mismatch: {witten_integral} != "
            f"{witten_required_unit_brane} (diff {absolute_diff})"
        )
    if mod_8_KO != 1:
        obstructions.append(
            f"KO Bott period mismatch: {int(witten_integral)} mod 8 = {mod_8_KO} (not 1)"
        )

    for i, ob in enumerate(obstructions):
        print(f"  [{i+1}] {ob}")

    results['obstructions'] = obstructions

    # -------------------------------------------------------------------
    # Primary value returned
    # -------------------------------------------------------------------
    results['value'] = homotopy_level

    return results


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, closure_sha):
    """Append a single-line verdict to s84_gate_verdicts.txt with full 64-char SHA pin."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def evaluate_gate(homotopy_level):
    """Pre-registered thresholds per plan §W7a-74.

    PASS: homotopy_level == 3 (structure-preserving K_0 iso)
    INFO: homotopy_level == 2 (classifying-space homotopy equivalence)
    FAIL: homotopy_level <= 1 (weak map only or no map)
    """
    if homotopy_level == 3:
        return "PASS"
    if homotopy_level == 2:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 7 — Plot (optional)
# ---------------------------------------------------------------------------

def make_plot(results):
    """Diagnostic plot: 6-step substitution chain + obstruction summary."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("S84-DET-P-K-THEORY — K-theoretic uplift of det(P)=1",
                 fontsize=13, fontweight='bold')

    # Left panel: substitution chain bar chart
    ax = axes[0]
    steps = ['S1:\ndet(P)', 'S2:\nBott', 'S3:\nch_0',
             'S4:\nA-roof', 'S5:\nWitten int', 'S6:\nLevel']
    values = [
        results['step1_det_P_K0'],
        results['step2_complexification_rank'],
        results['step3_ch_0'],
        results['step4_a_roof'],
        results['step5_witten_integral'],
        results['homotopy_level'],
    ]
    colors = ['#4daf4a', '#377eb8', '#ff7f00',
              '#984ea3', '#e41a1c', '#a65628']
    ax.bar(steps, values, color=colors, edgecolor='black', linewidth=1.2)
    ax.axhline(1.0, color='k', ls='--', alpha=0.5,
               label='Witten single-brane = 1')
    for i, v in enumerate(values):
        ax.text(i, v + 0.5, f"{v}", ha='center', va='bottom', fontsize=10)
    ax.set_ylabel('Value')
    ax.set_title('6-step substitution chain')
    ax.set_ylim(bottom=-0.5, top=max(values) * 1.2 + 1)
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)

    # Right panel: level criteria decision tree
    ax = axes[1]
    ax.axis('off')
    verdict = results['verdict']
    level = results['homotopy_level']
    txt_lines = [
        f"VERDICT: {verdict}",
        f"Homotopy level: {level}",
        "",
        "Level 3 (PASS, strong): structure-preserving K_0 iso",
        f"  K_0 rank match: {results['step6_level_3_PASS']}",
        "",
        "Level 2 (INFO): classifying-space equivalence",
        f"  pi_0 match: {results['step6_level_2_PASS']}",
        "",
        "Level 1 (FAIL w/ map): Z-linear map exists",
        f"  Exists: {results['step6_level_1_map_exists']}",
        "",
        "Obstructions identified:",
    ]
    for ob in results['obstructions']:
        txt_lines.append(f"  - {ob}")

    txt = "\n".join(txt_lines)
    ax.text(0.02, 0.98, txt, transform=ax.transAxes,
            fontsize=10, va='top', ha='left',
            family='monospace')
    ax.set_title('Homotopy-level decision tree')

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150)
    plt.close()
    print(f"Saved: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...  (full: {closure})")
    print()

    # 2. Compute substitution chain
    result = compute()
    value = result["value"]

    # 3. Evaluate gate
    verdict = evaluate_gate(value)

    # 4. Cross-check: verdict assigned in compute() matches evaluate_gate()
    assert verdict == result['verdict'], (
        f"Internal inconsistency: compute assigned {result['verdict']} "
        f"but evaluate_gate returned {verdict}"
    )

    # 5. Save npz data
    np.savez(OUT_NPZ,
        # Step 1
        step1_det_P_K0=result['step1_det_P_K0'],
        step1_det_P_8x8=result['step1_det_P_8x8'],
        step1_K0_rank=result['step1_K0_rank'],
        # Step 2
        step2_KO6_torsion=result['step2_KO6_torsion'],
        step2_K0_torsion=result['step2_K0_torsion'],
        step2_complexification_rank=result['step2_complexification_rank'],
        # Step 3
        step3_ch_0=result['step3_ch_0'],
        step3_dim_HF_half=result['step3_dim_HF_half'],
        # Step 4
        step4_a_roof=result['step4_a_roof'],
        # Step 5
        step5_witten_integral=result['step5_witten_integral'],
        step5_witten_required=result['step5_witten_required'],
        step5_abs_diff=result['step5_abs_diff'],
        step5_mod_8_KO=result['step5_mod_8_KO'],
        step5_mod_2_K=result['step5_mod_2_K'],
        # Step 6
        step6_level_3_PASS=result['step6_level_3_PASS'],
        step6_level_2_PASS=result['step6_level_2_PASS'],
        step6_level_1_map_exists=result['step6_level_1_map_exists'],
        # Output
        homotopy_level=result['homotopy_level'],
        verdict=np.array([result['verdict']]),
        obstructions=np.array(result['obstructions'], dtype=object),
        # Provenance
        closure_sha256=np.array([closure]),
    )
    print(f"Saved: {OUT_NPZ}")

    # 6. Optional plot
    try:
        make_plot(result)
    except Exception as exc:
        print(f"Plot generation failed (non-blocking): {exc}")

    # 7. Emit 4-tuple + append verdict
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print()
    print(tag)
    append_verdict(verdict, value, closure)

    # 8. Final summary
    wall = time.time() - t0  # (local)
    print()
    print("=" * 72)
    print(f"=== {GATE_ID}: {verdict} (homotopy_level={value}, wall {wall:.2f}s) ===")
    print("=" * 72)
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
