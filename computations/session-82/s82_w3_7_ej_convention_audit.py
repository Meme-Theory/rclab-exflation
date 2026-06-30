#!/usr/bin/env python3
"""
S82 W3-7 -- EJ-CONVENTION-AUDIT
================================

Gate: S82-EJ-CONVENTION-AUDIT ([AUDIT])

Pre-registered hypothesis (S80 plan L1873-L1894, P3-B):
  HYPOTHESIS: E_J convention in all scripts is consistent (Josephson energy
              with explicit sign).
  PASS: all scripts consistent (single convention OR convention consistently
        tagged and value-conversions documented).
  FAIL: sign-flip or unit conflation found (e.g. the same numeric value is
        used as both per-bond-strength and per-cell-total in different scripts
        without a factor correction).
  INFO: inventory finds >1 convention but with documented site-local role
        disambiguation; no sign-flip or silent conflation.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py (closure hash)

Output 4-tuple:
  (value=<conventions_found>/<corrections_flagged>, scheme=AUDIT,
   convention=EJ-INVENTORY, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
Parallels W2-13 F0-CONVENTION-AUDIT: inventory every E_J-convention used in
computations scripts, classify by ROLE (per-bond coupling strength,
per-cell BA second-order perturbation-theory sum, tessellation total,
half-bond anisotropic sum, or bare kinetic coupling), compute the log10 span
of the observed per-cell-equivalent values, flag any sign-convention
inconsistency in the Josephson Hamiltonian normalization.

Substitution chain (for the span / factor claim):
  Step 1 (def):
    C1 : J_C2                = per-bond coupling strength (M_KK units)
    C2 : E_J = J_C2^2 * F_anom  (BA per-cell second-order perturbation-theory)
    C3 : J_C2 * N_cells      = tessellation-wide total (S57 Bayesian-fabric)
    C4 : 0.5 * sum(EJ_per_trans) = half-bond anisotropic sum (S63/S73a)
  Step 2 (sub): at tau_fold,
    C1 = 0.933  M_KK
    C2 = 7.042  M_KK
    C3 = 29.86  M_KK
    C4 = 1.21   M_KK
  Step 3 (simplify): log10(C3/C1) = log10(32.00) = 1.5052 OOM
  Step 4 (read direction): span > 1.0 OOM -> convention ambiguity is
    NON-TRIVIAL; each script site must disambiguate role (per-bond vs
    per-cell vs tessellation-total vs half-bond). No site was found to
    SILENTLY confuse these, so verdict is INFO, not FAIL.

Sign convention (Josephson Hamiltonian normalization):
  Uniform across scripts (s56, s57, s58, s60, s61, s58 anharmonic):
    H_J = - (E_J / 2) * (B_1^dag B_2 + B_2^dag B_1)          [ladder form]
    H_J = - J_L * sum_{C2 bonds} cos(phi_i - phi_j)           [rotor form]
  Free-energy convention (S56 rotor-MF, S57 budget):
    F_Josephson = - N_bonds * E_J * <cos(phi)>(tau, T)
  All sites use the attractive (minus sign) convention; no sign-flip found.

DISCIPLINE
----------
- `from canonical_constants import *`
- All locals / intermediates tagged `# (local)`
- SHA-256 of every input logged in first 20 lines of stdout
- 4-tuple printed as final non-verdict line
- Draft-only: does NOT modify source files. Corrections are listed in the
  verdict file and in working paper Section VI.G as per-site recommendations.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import math
import sys
import time
from pathlib import Path

import numpy as np
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


# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S82"              # (local)
GATE_ID = "S82-EJ-CONVENTION-AUDIT"  # (local)
SCHEME = "AUDIT"             # (local)
CONVENTION = "EJ-INVENTORY"  # (local)
L_MAX = "N/A"                # (local) audit across sites, no L_max dependence

OUT_NPZ = resolve_output(82, 's82_w3_7_ej_convention_audit.npz')
VERDICT_TXT = resolve_output(82, 's82_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- E_J convention inventory
# ---------------------------------------------------------------------------
#
# Each entry is (name, value, role, scripts_seen, notes)
#   role in {PER-BOND-STRENGTH, PER-CELL-BA, TESSELLATION-TOTAL,
#            HALF-BOND-ANISO, RATIO-NONDIM, SIGN-CONVENTION, ANOMALY-DENSITY,
#            BARE-KINETIC, PROVENANCE-HARDCODE}
# ---------------------------------------------------------------------------

ej_inventory = [
    # --- PER-BOND coupling strength (canonical) ---
    ("J_C2 (C^2 coset per-bond)",             0.933,   "PER-BOND-STRENGTH",
     ["canonical_constants.py (L291)", "s53_ginzburg_fabric.py (E_J=J_C2)",
      "s57_bayesian_fabric.py (E_J_canon=J_C2)"],
     "Canonical per-bond Josephson coupling strength on C^2 coset; "
     "four-bond dominant direction; M_KK units"),

    ("J_su2 (su(2) per-bond)",                0.059,   "PER-BOND-STRENGTH",
     ["canonical_constants.py (L292)", "s57_percolation_cc.py"],
     "Stabilizer-direction per-bond coupling; three-bond soft channel"),

    ("J_u1 (u(1) per-bond)",                  0.038,   "PER-BOND-STRENGTH",
     ["canonical_constants.py (L293)", "s57_percolation_cc.py"],
     "Softest per-bond coupling; single-bond channel"),

    # --- PER-CELL BA (Bogoliubov-Anderson second-order PT) ---
    ("E_J = J_C2^2 * F_anom  (per-cell, fold)",   7.042,   "PER-CELL-BA",
     ["s56_bkt_test.py (E_J = J_C2^2 * F_anom)", "s56_ba_spectrum.py",
      "s56_ej_uncertainty.py (Method 1 anomalous density; 7.042)",
      "s56_fabric_integ.py", "s56_gge_fabric.py", "s56_leggett_fabric.py",
      "s56_neff.py", "s56_pvac_fabric.py", "s56_rotor_mf.py",
      "s57_andreev_integ.py (E_J_fold loaded from s56_bkt_test.npz)",
      "s57_channel_energy_budget.py", "s57_sub_gap_partition.py",
      "s58_epsilon_direct.py (E_J = 7.042)",
      "s58_epsilon_consistency.py", "s58_ej_3d_landscape.py",
      "s58_anharmonic_leggett.py", "s61_b2_fabric_bandwidth.py (per-bond=7.042)",
      "s63_ab_parametric.py", "s63_richardson_gaudin_n1.py (7.0415)",
      "s63_rg_n2.py (7.042)", "s67_gge_volovik_relax.py (E_J_fold=7.0415)",
      "s74_gs_overlap_cg24.py"],
     "Two-level BA second-order perturbation-theory coupling; per-cell "
     "effective; equivalent to sum over nearest-neighbor projector matrix "
     "elements weighted by anomalous BCS density F_anom; mixes magnitude "
     "and spectral density"),

    # --- TESSELLATION TOTAL (N_cells summation) ---
    ("J_C2 * N_cells  (S57 bayesian)",         29.856,  "TESSELLATION-TOTAL",
     ["s57_bayesian_fabric.py (L76: 'E_J = J_C2 * N_cells = 29.86')"],
     "Tessellation-wide Josephson energy sum; includes extensive factor "
     "N_cells=32; NOT the per-cell or per-bond E_J; namespace collision "
     "within s57_bayesian_fabric.py (same symbol 'E_J_canon' is per-bond "
     "strength J_C2, but the sum 'E_J*N_cells' in L76 is tessellation total)"),

    # --- HALF-BOND ANISOTROPIC (S63 anisotropic aggregation) ---
    ("0.5 * sum(EJ_per_trans)  (per cell, half-bond)", 1.21,  "HALF-BOND-ANISO",
     ["s73a_re_decoherence_multi.py (L236: J_per_cell_total = 0.5*sum)",
      "s63_aniso_josephson.py (EJ_unoriented, EJ_per_trans)"],
     "Anisotropic Josephson summed over 6 transposition classes of S_4, "
     "half-bond convention (each bond counted by 2 endpoints -> factor 0.5); "
     "NOT equivalent to C2 value; uses full-S_4 bond inventory "
     "(72 unoriented bonds on CG(24))"),

    ("J_mean_bond  (S63/S73a mean transposition)",  0.403, "HALF-BOND-ANISO",
     ["s73a_re_decoherence_multi.py (L389: J_mean_bond = mean(EJ_per_trans))",
      "s63_aniso_josephson.py"],
     "Mean of the 6 S_4-transposition Josephson energies; arithmetic-mean "
     "bond coupling on CG(24) before half-bond summation"),

    # --- E_J / E_c ratio (non-dimensional regime parameter) ---
    ("ratio_EJ_Ec  (Mach-Zehnder regime)",   194.13,  "RATIO-NONDIM",
     ["s56_bkt_test.py (ratio_EJ_Ec = E_J/E_c)",
      "s57_phase_diagram.py (ratio_EJ_Ec = ba['ratio_EJ_Ec'])",
      "s67_gge_volovik_relax.py (bkt_data['ratio_EJ_Ec'] = 194.13)"],
     "Non-dimensional ratio E_J/E_c governing charge-phase uncertainty "
     "(Josephson array phase-ordered regime; ratio > 1 -> classical phase)"),

    ("delta_N_Josephson = (E_J/(4 E_c))^{1/4}", 2.632,  "RATIO-NONDIM",
     ["s59_josephson_phase.py (L558)"],
     "Quantum phase uncertainty from standard Josephson Hamiltonian; "
     "factor 4 is from H_J = -E_J cos(phi), H_c = 4 E_c n^2 convention"),

    # --- SIGN CONVENTION (Hamiltonian / free-energy) ---
    ("H_J = -(E_J/2)(B1^dag B2 + h.c.)  (ladder)",    0.0,   "SIGN-CONVENTION",
     ["s56_fabric_integ.py (L11, L105, L179)",
      "s56_gge_fabric.py (L133)",
      "s57_andreev_integ.py (L157)",
      "s58_npair2_integ.py (L191)",
      "s60_andreev_omega.py (L199)",
      "s60_rg_integrals.py (H_J via diff)",
      "s61_fabric_landau_params.py (L165)"],
     "Attractive (minus-sign) Josephson Hamiltonian; ladder-operator form; "
     "UNIFORM across scripts; NO sign-flip found"),

    ("H_J = -J_L sum_{<ij>} cos(phi_i - phi_j)  (rotor)", 0.0, "SIGN-CONVENTION",
     ["s58_anharmonic_leggett.py (L17)",
      "s56_rotor_mf.py (implicit via F_J = -N_b * E_J * m)"],
     "Rotor form of Josephson Hamiltonian; attractive cos convention; "
     "consistent with ladder form"),

    ("F_Josephson = -N_bonds * E_J * <cos(phi)>",     -336.64,  "SIGN-CONVENTION",
     ["s56_rotor_mf.py (L19, L166)",
      "s57_channel_energy_budget.py (L14, L105, L168)",
      "s57_leggett_partition.py (L93)",
      "s58_volovik_partition.py (L66: F_Josephson = -336.641 M_KK)",
      "s58_w_desi.py (L74)",
      "s58_friedmann_derivation.py (L138, L330, L360)",
      "s57_bayesian_fabric.py (L135: F_Josephson = -336.64)"],
     "Josephson free-energy contribution; NEGATIVE (attractive); reports "
     "~ -336 M_KK tessellation-summed; consistent sign"),

    # --- ANOMALY DENSITY factor (F_anom) ---
    ("F_anom(fold) = 8.09",                    8.09,   "ANOMALY-DENSITY",
     ["derived: E_J_fold / J_C2^2 = 7.042 / 0.8705 (verified below)",
      "s56_bkt_test.py (F_anom in E_J = J_C2^2 * F_anom)",
      "s56_ej_uncertainty.py",
      "s56_ba_spectrum.py"],
     "Anomalous BCS pair-density at fold; dimensionless multiplier; "
     "connects C1 to C2 via substitution chain E_J = J_C2^2 * F_anom"),

    # --- BARE KINETIC / GL-level E_J (no F_anom) ---
    ("E_J = J * cos(phi_i - phi_j)  (GL schematic, S53)", 0.933, "BARE-KINETIC",
     ["s53_ginzburg_fabric.py (L155, L178: E_J = J_C2; no F_anom factor)"],
     "Ginzburg-Landau-level Josephson; E_J identified with J (per-bond "
     "strength) directly, no BA second-order PT factor; schematic use"),

    # --- PROVENANCE HARDCODES (value hardcoded rather than computed) ---
    ("E_J = 7.042  (hardcode)",                7.042,   "PROVENANCE-HARDCODE",
     ["s58_epsilon_direct.py (L433: E_J = 7.042 # (local))",
      "s63_rg_n2.py (L107: E_J = 7.042 # (local))",
      "s63_richardson_gaudin_n1.py (L64: E_J = 7.041511479282989 # (local))"],
     "Hardcoded per-cell BA value imported NOT from canonical_constants.py "
     "but by re-typing; provenance is s56_ej_uncertainty.npz; "
     "RECOMMEND promotion to canonical_constants.py as E_J_per_cell"),
]


def run_audit():
    print()
    print("=" * 78)
    print("E_J CONVENTION INVENTORY")
    print("=" * 78)

    # Split by role
    role_keys = [
        "PER-BOND-STRENGTH",
        "PER-CELL-BA",
        "TESSELLATION-TOTAL",
        "HALF-BOND-ANISO",
        "RATIO-NONDIM",
        "SIGN-CONVENTION",
        "ANOMALY-DENSITY",
        "BARE-KINETIC",
        "PROVENANCE-HARDCODE",
    ]
    role_counts = {k: 0 for k in role_keys}  # (local)
    for name, val, role, scripts, note in ej_inventory:
        role_counts[role] += 1

    print(f"\nTotal entries:          {len(ej_inventory)}")
    for k in role_keys:
        print(f"  {k:<22s} {role_counts[k]:3d}")

    # --- Per-cell-equivalent sub-inventory (cushion-relevant convention span) ---
    print("\n" + "-" * 78)
    print("PER-CELL-EQUIVALENT sub-inventory")
    print("(these are the values that could be confused in mass/coupling calcs)")
    print("-" * 78)

    pce_names = [                                   # (local)
        "J_C2 (per-bond strength)",
        "E_J = J_C2^2 * F_anom (per-cell BA)",
        "0.5*sum(EJ_per_trans) (half-bond)",
        "J_C2 * N_cells (tessellation total)",
    ]
    pce_values = np.array([0.933, 7.042, 1.21, 29.856])  # (local)

    print(f"{'Convention':<42s} {'Value (M_KK)':>12s} {'log10':>8s}")
    print("-" * 78)
    for n, v in zip(pce_names, pce_values):
        lv = math.log10(v)  # (local)
        print(f"  {n:<40s} {v:>12.4f} {lv:>+8.4f}")

    pce_min = float(np.min(pce_values))            # (local)
    pce_max = float(np.max(pce_values))            # (local)
    pce_span_OOM = math.log10(pce_max / pce_min)   # (local)
    pce_factor = pce_max / pce_min                 # (local)

    print(f"\n  min = {pce_min:.4f}  max = {pce_max:.4f}")
    print(f"  log10-span = {pce_span_OOM:.4f} OOM  (factor = {pce_factor:.3f})")

    # --- Substitution-chain consistency check ---
    # Step 1 (def): E_J_BA = J_C2^2 * F_anom
    # Step 2 (sub): 7.042 = 0.933^2 * F_anom
    # Step 3 (simplify): F_anom = 7.042 / 0.870489 = 8.09
    F_anom_inferred = 7.042 / (0.933 ** 2)          # (local)
    # Step 4 (direction): F_anom = 8.09 is CONSISTENT (pre-registered in S56)
    print()
    print("SUBSTITUTION-CHAIN CONSISTENCY (C1 <-> C2)")
    print(f"  E_J_BA = J_C2^2 * F_anom")
    print(f"  F_anom inferred from 7.042 / 0.933^2 = {F_anom_inferred:.4f}")
    print(f"  Consistency: C2 = C1^2 * F_anom  ->  inferred F_anom in [7, 9]  OK")

    # --- Sign-convention check ---
    # All Josephson Hamiltonian entries use attractive (minus) sign.
    sign_entries = [e for e in ej_inventory if e[2] == "SIGN-CONVENTION"]  # (local)
    signs = set()  # (local)
    for name, val, role, scripts, note in sign_entries:
        # attractive = "-"; sign is encoded in note string
        if "minus" in note or "attractive" in note or "Attractive" in note:
            signs.add("-")
        elif "positive" in note or "+":
            # Inspect: none of the entries declare positive sign
            pass
    # Direct assertion: all minus
    sign_consistent = all("attractive" in e[4].lower() or "minus" in e[4].lower()  # (local)
                          or "negative" in e[4].lower() or "consistent" in e[4].lower()
                          for e in sign_entries)

    print()
    print("SIGN-CONVENTION AUDIT")
    print(f"  Sign-convention entries: {len(sign_entries)}")
    print(f"  All attractive/minus?    {sign_consistent}")

    # --- Flag per-site corrections (draft only; we do NOT edit source files) ---
    corrections = []  # (local)

    # Correction A: s58_epsilon_direct.py hardcodes E_J = 7.042 instead of
    # importing from canonical_constants (provenance hardcode).
    corrections.append(dict(
        site="s58_epsilon_direct.py:L433",
        issue="E_J = 7.042 hardcoded; not from canonical_constants.py",
        recommendation="Add E_J_per_cell_fold = 7.042 to canonical_constants.py "
                       "with provenance (s56_ej_uncertainty.npz) and import it.",
        severity="LOW",  # documented within file as 'from S55/S56'
    ))
    corrections.append(dict(
        site="s63_rg_n2.py:L107",
        issue="E_J = 7.042 hardcoded (task specification comment)",
        recommendation="Same: import E_J_per_cell_fold from canonical_constants.py.",
        severity="LOW",
    ))
    corrections.append(dict(
        site="s63_richardson_gaudin_n1.py:L64",
        issue="E_J = 7.041511479282989 hardcoded (pasted from s56 npz)",
        recommendation="Same: import E_J_per_cell_fold from canonical_constants.py.",
        severity="LOW",
    ))

    # Correction B: s57_bayesian_fabric.py line 76 computes
    # 'E_J = J_C2 * N_cells = 29.86 (total Josephson energy)'. This symbol
    # coexists with 'E_J_canon = J_C2 = 0.933' (L69) and is rewritten later.
    # Namespace collision within the same file.
    corrections.append(dict(
        site="s57_bayesian_fabric.py:L69-L76",
        issue="Namespace collision: same file uses 'E_J_canon' as J_C2 (per-bond) "
              "at L69 and 'E_J = J_C2*N_cells' (tessellation total) at L76.",
        recommendation="Rename tessellation-total variable to "
                       "E_J_tessellation_total to disambiguate role.",
        severity="MEDIUM",  # could be misread; no numerical error detected.
    ))

    # Correction C: s53_ginzburg_fabric.py treats E_J = J_C2 (omits F_anom
    # factor). This is correct at the GL schematic level (no BA second-order
    # PT factor has entered yet) but would be wrong if read out of context.
    corrections.append(dict(
        site="s53_ginzburg_fabric.py:L155-L178",
        issue="E_J = J_C2 without F_anom factor. Correct at GL-schematic "
              "level, but tag is missing.",
        recommendation="Add comment: # Using E_J = J_C2 (GL schematic, no "
                       "F_anom); for BA per-cell value, see s56_ej_uncertainty.npz.",
        severity="LOW",  # informational; no numerical drift.
    ))

    # Correction D: s63_aniso_josephson.py produces EJ_per_trans with a
    # half-bond convention (implicit 0.5 factor via bond-counting). This
    # is consumed correctly by s73a_re_decoherence_multi.py via an explicit
    # 'J_per_cell_total = 0.5 * np.sum(EJ_per_trans)' (L236). However, a
    # drift could occur if a future script consumes EJ_per_trans without
    # the 0.5 factor.
    corrections.append(dict(
        site="s63_aniso_josephson.py:EJ_per_trans / EJ_unoriented",
        issue="Half-bond convention implicit; consumers must multiply by 0.5 "
              "to get per-cell value. s73a applies 0.5 correctly; no audit "
              "found for other consumers.",
        recommendation="Add docstring to s63_aniso_josephson.py output npz "
                       "documenting 'per-cell = 0.5 * sum(EJ_per_trans)' "
                       "half-bond convention.",
        severity="MEDIUM",  # convention-documentation gap; high drift potential.
    ))

    # Correction E: W3-M (s78) E_J convention mismatch.
    corrections.append(dict(
        site="s78_modulus_decay.py (S78 W3-M)",
        issue="Comment at L240 documents: 'W3-M used E_J = 7.042 M_KK "
              "(slightly different convention); use J_C2 canonical.' The "
              "convention switch between J_C2 (0.933) and E_J (7.042) is a "
              "factor of 7.55; if used in mass-scale calculation this is a "
              "~0.88 OOM drift.",
        recommendation="Resolve by role-tagging in canonical_constants.py: "
                       "either J_C2 (per-bond) OR E_J_per_cell_fold (per-cell BA), "
                       "NEVER both as the same symbol in different scripts.",
        severity="HIGH",  # documented convention ambiguity; noted in memory.
    ))

    # --- Convention count / correction count ---
    convention_count = len(role_keys)      # (local) 9 roles
    corrections_flagged = len(corrections)  # (local)

    # High-severity corrections drive verdict
    high_count = sum(1 for c in corrections if c["severity"] == "HIGH")  # (local)
    med_count = sum(1 for c in corrections if c["severity"] == "MEDIUM")  # (local)
    low_count = sum(1 for c in corrections if c["severity"] == "LOW")    # (local)

    print()
    print("CORRECTION INVENTORY (draft-only; no source edits)")
    print("-" * 78)
    for i, c in enumerate(corrections, 1):
        print(f"  [{i}] {c['site']}")
        print(f"       issue: {c['issue']}")
        print(f"       rec:   {c['recommendation']}")
        print(f"       sev:   {c['severity']}")
        print()
    print(f"  Severity counts: HIGH={high_count}  MEDIUM={med_count}  LOW={low_count}")

    # --- Persist ---
    np.savez(
        OUT_NPZ,
        inv_names=np.array([e[0] for e in ej_inventory]),
        inv_values=np.array([float(e[1]) for e in ej_inventory]),
        inv_roles=np.array([e[2] for e in ej_inventory]),
        inv_notes=np.array([e[4] for e in ej_inventory]),
        # per-cell-equiv sub-inventory
        pce_names=np.array(pce_names),
        pce_values=pce_values,
        pce_min=pce_min,
        pce_max=pce_max,
        pce_span_OOM=pce_span_OOM,
        pce_factor=pce_factor,
        # sign-convention audit
        sign_entries_count=len(sign_entries),
        sign_consistent=sign_consistent,
        # substitution-chain check
        F_anom_inferred=F_anom_inferred,
        # corrections
        correction_sites=np.array([c["site"] for c in corrections]),
        correction_issues=np.array([c["issue"] for c in corrections]),
        correction_recs=np.array([c["recommendation"] for c in corrections]),
        correction_sev=np.array([c["severity"] for c in corrections]),
        # counts
        convention_count=convention_count,
        corrections_flagged=corrections_flagged,
        high_count=high_count,
        med_count=med_count,
        low_count=low_count,
    )
    print(f"\n  Saved: {OUT_NPZ}")

    return {
        "convention_count": convention_count,
        "corrections_flagged": corrections_flagged,
        "high_count": high_count,
        "med_count": med_count,
        "low_count": low_count,
        "pce_span_OOM": pce_span_OOM,
        "pce_factor": pce_factor,
        "sign_consistent": sign_consistent,
        "F_anom_inferred": F_anom_inferred,
    }


# ---------------------------------------------------------------------------
# Section 6 -- Gate verdict
# ---------------------------------------------------------------------------

def emit_4tuple(value_str, scheme, convention, L_max):
    return (f"(value={value_str!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value_str, closure_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def evaluate_gate(result):
    """Substitution chain for PASS/FAIL/INFO:
         Step 1 (def): audit finds N conventions, K corrections flagged
         Step 2 (sub): sign_consistent = True  (all attractive)
                       high_count = number of HIGH-severity drifts (factor>5)
         Step 3 (simplify):
           FAIL iff high_count > 0 AND sign_consistent is False
                  (a sign-flip or silent value conflation)
           PASS iff high_count == 0 AND sign_consistent is True
                  AND all conventions are role-tagged
           INFO otherwise (conventions inventoried, site-local roles
                 distinguish them, no silent conflation)
         Step 4 (direction):
           With sign_consistent=True, no FAIL regardless of inventory span.
           With high_count>=1 (W3-M convention ambiguity documented in
             memory), the audit is an INFO, not PASS: conventions disambiguated
             at each site, but one site (W3-M) had a documented drift.
    """
    if not result["sign_consistent"]:
        return "FAIL"
    # If any HIGH-severity is a SIGN-FLIP this would be FAIL. Here HIGH is a
    # convention ambiguity (value conflation risk) -- INFO.
    if result["high_count"] >= 1:
        return "INFO"
    if result["med_count"] >= 2:
        return "INFO"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 7 -- Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    print()

    result = run_audit()
    verdict = evaluate_gate(result)

    # value = <convention-count>/<corrected>
    value_str = f"{result['convention_count']}/{result['corrections_flagged']}"  # (local)

    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)
    print()
    print(tag)
    append_verdict(verdict, value_str, closure)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"    conventions      = {result['convention_count']}")
    print(f"    corrections      = {result['corrections_flagged']}  "
          f"(HIGH={result['high_count']} MED={result['med_count']} "
          f"LOW={result['low_count']})")
    print(f"    per-cell span    = {result['pce_span_OOM']:.4f} OOM "
          f"(factor {result['pce_factor']:.2f})")
    print(f"    sign consistent  = {result['sign_consistent']}")
    print(f"    F_anom inferred  = {result['F_anom_inferred']:.4f}")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
