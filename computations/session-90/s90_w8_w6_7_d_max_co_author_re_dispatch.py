#!/usr/bin/env python3
"""
S90 W8-8 CF-66 — S90-W6-7-D-MAX-CO-AUTHOR-RE-DISPATCH
=====================================================

Gate: S90-W6-7-D-MAX-CO-AUTHOR-RE-DISPATCH ([AUDIT])

Substantive D_max measurement at substrate-distance-2 pole s=4 between
SCHEMATIC tier outputs (W9b-2 `_spectral_action_regulators.py`
analytic helpers) and FULL physical PRIMARY 2-point Pauli-Villars
pipeline at Λ_UV = M_KK = 7.428660036284456e+16 GeV.

Pre-registered threshold:
  D_max := max(|Δ log10 rho_S_s4|, |Δ log10 zeta_D_s4|)
  PASS iff D_max < 1.0 OOM (NO-ACTION or ADVISORY band)
  INFO iff 1.0 <= D_max < 3.0 OOM (MANDATORY band; halts plan-freeze)
  FAIL iff D_max >= 3.0 OOM (HARD-HALT band)

Inputs (SHA-256 dual-pinned at runtime, S84+ schema):
  - computations/session-87/s87_w9b_pole_specificity_scan.npz (SCHEMATIC)
  - computations/session-89/s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz (W3 A.14)
  - computations/_shared/canonical_constants.py (M_KK, tau_fold; feeds audit_sha256)
  - computations/_pauli_villars_subtraction.py (FULL physical PV PRIMARY pipeline)
  - computations/_shared/_spectral_action_regulators.py (SCHEMATIC helpers; cited for self-id)
  - computations/_shared/_analytic_zeta.py (TIER-1 zeta_D_direct + load_spectrum)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (FULL D_K eigenvalue cache)
  - script bytes (feeds both audit_sha256 and content_sha256)

Output 4-tuple:
  (value=(D_max, severity_band), scheme=FULL-physical-PV-pipeline-vs-SCHEMATIC,
   convention=substrate-distance-2-pole-s4, L_max=10)

Classification: META (D_max measurement methodology + W3 A.14 cross-wave npz consumption;
substantive cross-tier structural fidelity probe at the UV-regulator axis)

METHODOLOGY
-----------
Step 1: Load SCHEMATIC inputs from W9b-2 (`s87_w9b_pole_specificity_scan.npz`):
  - rho_S_s4 (composite signed Spearman r at s=4, -1.0)
  - rho_S_per_regulator_s4 (5-regulator atlas)
  - zeta_D_s4 (TIER-1 analytic_zeta value)
  - spectral_projection_s4 (4-class)
  - dynamical_projection_s4

Step 2: Load W3 A.14 cross-wave cocycle-ratio regulator-class-invariance npz
        (s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz)
        for regulator-class invariance cross-validation of the ratio family.

Step 3: Build FULL physical PRIMARY 2-point PV pipeline at Λ_UV = M_KK using
        `_pauli_villars_subtraction.pv_mellin_moment_primary` with masses
        M_1 = M_KK (dimensionless 1.0 in M_KK units) and M_2 = √2·M_KK
        (dimensionless √2 in M_KK units); coefficients c_1=+2, c_2=-1
        satisfying Σ c_r = 1 and Σ c_r·M_r² = 0 (Connes-Chamseddine 1996
        §2.2-2.3 PV consistency identities).

Step 4: Compute FULL-tier per-class spectral_projection at s=4 on the L_max=12
        D_K cache (`s84_spectrum_cache_L12_tau019.npz`):
          - F_2 (zeta/bare):    Σ m_k λ_k^{-4} / Vol
          - cutoff_sqrt:        hard-cutoff version
          - anomaly (PV PRIM):  pv_mellin_moment_primary(s=2)/Vol  [s_idx=2 ⇒ λ^{-4}]
          - Zubarev:            heat-kernel-dressed version
        Compute rho_S_s4^{FULL} = Spearman r between FULL spectral_projection
        and dynamical_projection (substrate-IS, regulator-independent).
        Compute zeta_D_s4^{FULL} = zeta_D_direct(s=4, L=12) — bit-identical to
        SCHEMATIC by construction (both call the same TIER-1 helper).

Step 5: D_max = max(|log10|rho_S_s4^{SCH}| - log10|rho_S_s4^{FULL}||,
                    |log10|zeta_D_s4^{SCH}| - log10|zeta_D_s4^{FULL}||)
        Classify per the 4-band severity calibration.

Step 6: Inheritance-pin retroactive remediation check per
        substrate-first-canonical-sourcing.md §(iv) §"Inheritance-pin retroactive
        remediation" (S88 W-24 V.4 / B.62): trigger MANDATORY tagging on S89+
        gates inheriting W4-2/W9b-2 SCHEMATIC outputs if D_max >= 1.0 OOM.

DISCIPLINE
----------
- `from canonical_constants import *`
- All computed intermediates tagged `# (local)`
- CPU path (small problem; <100K eigenvalues; no GPU needed for the moment evaluations)
- Atomic single-shot `open("a")` verdict append per gate-verdicts.md
- Dual-SHA closure (S84+ schema) + 3-tuple companion row (S87 schema-v2)
- Substitution chain Step 5 carries directional prediction D_max<1.0 ⟹ SCHEMATIC
  faithful proxy; D_max>=1.0 ⟹ inheritance-pin retroactive remediation MANDATORY.

PROVENANCE
----------
Plan: sessions/session-plan/session-90-plan-w8.md §W8-8 (lines 2007-2255).
Owner: gen-physicist PRIMARY + connes-ncg-theorist CO-AUTHOR.
Working paper: sessions/archive/session-90/session-90-w8-workingpaper.md §W8-8.
"""

from __future__ import annotations

# OMP thread cap for safety alongside potential concurrent agents.
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
sys.path.insert(0, str(COMPUTATIONS_DIR))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import time

import numpy as np
from scipy.stats import spearmanr

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Shared helpers
from _analytic_zeta import load_spectrum, zeta_D_direct
from _pauli_villars_subtraction import (
    pv_mellin_moment_primary,
    pv_mellin_moment_schematic,
    bare_mellin_moment,
    heat_kernel_mellin_moment,
    hard_cutoff_mellin_moment,
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
    _verify_pv_identities,
)
from _spectral_action_regulators import (
    zeta_a_n, heat_kernel_a_n, hard_cutoff_a_n, pauli_villars_a_n, mellin_a_n,
)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S90"                                                       # (local)
GATE_ID = "S90-W6-7-D-MAX-CO-AUTHOR-RE-DISPATCH"                      # (local)
SCHEME = "FULL-physical-PV-pipeline-vs-SCHEMATIC"                     # (local)
CONVENTION = "substrate-distance-2-pole-s4"                           # (local)
L_MAX = 10                                                            # (local)
L_MAX_FULL_PHYSICAL_PV = 12                                           # (local; matches s87_w9b cache metadata)

# Pre-registered severity-band thresholds (4-band per epistemic-discipline.md
# §"Source Reconciliation"). DO NOT modify after seeing computed value
# (PROHIBITED_ACTIONS Class 3).
D_MAX_NO_ACTION_THRESHOLD = 0.1                                       # (local)
D_MAX_ADVISORY_THRESHOLD = 1.0                                        # (local)
D_MAX_MANDATORY_THRESHOLD = 3.0                                       # (local)

# Inheritance-pin remediation trigger threshold (S88 W-24 V.4 / B.62).
INHERITANCE_PIN_REMEDIATION_TRIGGER = 1.0                             # (local)

# Substrate-distance-2 pole s=4. The Mellin moment Σ m_k · λ_k^{-2s} uses
# s_idx = s/2 to land at λ^{-s} convention; pv_mellin_moment_primary uses
# Σ m_k · w · λ_k^{-2s}, so for the s=4 pole (substrate-distance-2) we
# pass s_index=2.0 to the helper (yields λ^{-4} weighting).
S_SUBSTRATE_POLE = 4.0                                                # (local)
S_INDEX_FOR_PV_HELPER = 2.0                                           # (local; s_idx → λ^{-2*s_idx})

# Hard-cutoff fraction and heat-kernel reference time (match SCHEMATIC defaults)
HARD_CUTOFF_FRAC_DEFAULT = 0.7                                        # (local)
HEAT_KERNEL_T_REF_DEFAULT = 0.1                                       # (local)

# Vol_SU3_Haar (canonical normalization) — from canonical_constants
VOL_SU3_HAAR_LOCAL = float(Vol_SU3_Haar)                              # (local, mirror of canonical Vol_SU3_Haar)

# A_5 4-class projection order (matches W9b-2 npz `a5_4class_order`)
A5_4CLASS_ORDER = ("F_2", "cutoff_sqrt", "anomaly", "Zubarev")

# Output destinations
OUT_NPZ = SESSION_DIR / "s90_w8_w6_7_d_max_co_author_re_dispatch.npz"
OUT_JSON = SESSION_DIR / "s90_w8_w6_7_d_max_co_author_re_dispatch.json"
OUT_PNG = SESSION_DIR / "s90_w8_w6_7_d_max_co_author_re_dispatch.png"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# Inputs
SCH_INPUT_NPZ = COMPUTATIONS_DIR / "session-87" / "s87_w9b_pole_specificity_scan.npz"
W3_A14_CROSS_WAVE_NPZ = COMPUTATIONS_DIR / "session-89" / "s89_w3_substrate_cocycle_ratio_regulator_class_invariance_scan.npz"
DIRAC_SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
PV_PRIMARY_HELPER = COMPUTATIONS_DIR / "_pauli_villars_subtraction.py"
SCHEMATIC_HELPER = SHARED_DIR / "_spectral_action_regulators.py"
ANALYTIC_ZETA_HELPER = SHARED_DIR / "_analytic_zeta.py"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SCH_INPUT_NPZ,
    W3_A14_CROSS_WAVE_NPZ,
    DIRAC_SPECTRUM_CACHE,
    PV_PRIMARY_HELPER,
    SCHEMATIC_HELPER,
    ANALYTIC_ZETA_HELPER,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema; W9a-99 split)
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
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
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
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def load_schematic_inputs() -> dict:
    """Load W9b-2 SCHEMATIC inputs from s87_w9b_pole_specificity_scan.npz."""
    sch = np.load(SCH_INPUT_NPZ, allow_pickle=True)  # (local)
    out = {  # (local)
        "rho_S_s4_composite": float(sch["rho_S_s4"][0]),
        "rho_S_per_reg_s4_keys": list(sch["rho_S_per_regulator_s4_keys"]),
        "rho_S_per_reg_s4_vals": list(sch["rho_S_per_regulator_s4_vals"]),
        "spectral_projection_s4_4class": np.asarray(sch["spectral_projection_s4"], dtype=np.float64),
        "spectral_projection_s4_5reg": np.asarray(sch["spectral_projection_s4_5reg"], dtype=np.float64),
        "dynamical_projection_s4": np.asarray(sch["dynamical_projection_s4"], dtype=np.float64),
        "zeta_D_s4_complex": complex(sch["zeta_D_s4"][0]),
        "n_helper_s4": int(sch["n_helper_s4"][0]),
        "L_max_cache": int(sch["L_max"][0]),
        "Vol_SU3_Haar": float(sch["Vol_SU3_Haar"][0]),
        "tau_fold_npz": float(sch["tau_fold"][0]),
    }
    return out


def load_w3_a14_cross_wave() -> dict:
    """Load W3 A.14 cross-wave regulator-invariant cocycle ratio inputs."""
    d = np.load(W3_A14_CROSS_WAVE_NPZ, allow_pickle=True)  # (local)
    return {
        "ratio_zeta": float(d["ratio_zeta"]),
        "ratio_PV": float(d["ratio_PV"]),
        "ratio_Mellin": float(d["ratio_Mellin"]),
        "ratio_cutoff": float(d["ratio_cutoff"]),
        "max_rel_dev": float(d["max_rel_dev"]),
        "spread_across_regulators": float(d["spread_across_regulators"]),
        "regulator_class_invariant": bool(d["regulator_class_invariant"]),
        "substrate_canonical": float(d["substrate_canonical"]),
    }


def build_full_physical_pv_pipeline_outputs(evs: np.ndarray, mults: np.ndarray) -> dict:
    """Compute FULL-tier per-class spectral moments at s=4 on the L_max=12 cache
    using the PRIMARY 2-point Pauli-Villars pipeline at Λ_UV = M_KK.

    Conventions:
      - s_idx=2 corresponds to Mellin moment Σ m_k · λ_k^{-4}, i.e. substrate-
        distance-2 pole at s=4.
      - PV PRIMARY 2-point pair: M_1 = M_KK (dim-less 1.0), M_2 = √2·M_KK
        (dim-less √2), c_1=+2, c_2=-1. Identities Σc_r=1, Σc_r·M_r²=0
        verified at module load.
      - Bare F_2: Σ m_k · λ_k^{-4} / Vol_SU3_Haar (zeta == bare on positive spectrum).
      - cutoff_sqrt: hard-cutoff at frac × max(λ²).
      - anomaly: pv_mellin_moment_primary (FULL physical PRIMARY).
      - Zubarev: heat-kernel exp(-t·λ²) dressed bare moment.
    """
    s_idx = S_INDEX_FOR_PV_HELPER  # (local) → λ^{-4}
    # F_2 (bare; zeta == bare on positive spectrum)
    M_F2 = bare_mellin_moment(s_idx, evs, mults) / VOL_SU3_HAAR_LOCAL              # (local)
    # cutoff_sqrt — hard-cutoff version
    M_cutoff = hard_cutoff_mellin_moment(s_idx, evs, mults,
                                         cutoff_frac=HARD_CUTOFF_FRAC_DEFAULT) / VOL_SU3_HAAR_LOCAL  # (local)
    # anomaly — PRIMARY 2-point Pauli-Villars (FULL physical)
    M_anomaly_PV = pv_mellin_moment_primary(s_idx, evs, mults) / VOL_SU3_HAAR_LOCAL  # (local)
    # Zubarev — heat-kernel dressed
    M_Zubarev = heat_kernel_mellin_moment(s_idx, evs, mults,
                                          t_ref=HEAT_KERNEL_T_REF_DEFAULT) / VOL_SU3_HAAR_LOCAL  # (local)

    return {
        "F_2": M_F2,
        "cutoff_sqrt": M_cutoff,
        "anomaly": M_anomaly_PV,
        "Zubarev": M_Zubarev,
    }


def compute_rho_S_s4_full(spectral_projection_FULL_4class: np.ndarray,
                          dynamical_projection: np.ndarray) -> tuple[float, float]:
    """Compute the FULL physical rho_S_s4 via Spearman r between FULL-tier
    spectral projection and the substrate-IS dynamical projection.

    The dynamical projection is regulator-INDEPENDENT (substrate-IS object at
    the dynamical-axis layer), so we reuse the SCHEMATIC-cached values; only
    the spectral_projection differs between SCHEMATIC and FULL physical."""
    rho, p = spearmanr(spectral_projection_FULL_4class, dynamical_projection)
    return float(rho), float(p)


def compute_d_max(rho_S_SCH: float, rho_S_FULL: float,
                  zeta_D_SCH: complex, zeta_D_FULL: complex) -> tuple[float, float, float]:
    """Compute D_max := max(|Δ log10 rho_S|, |Δ log10 zeta_D|) and the
    component D values."""
    # log10|·| is well-defined for non-zero magnitudes. Spearman rho_S is in
    # [-1, +1]; if either side returns exactly 0, set D_log_rho_S = inf (no
    # log-meaning); but rho_S_s4 SCH = -1 by construction, so this branch
    # only fires under structural pathology.
    abs_rho_SCH = abs(rho_S_SCH)  # (local)
    abs_rho_FULL = abs(rho_S_FULL)  # (local)
    if abs_rho_SCH == 0.0 or abs_rho_FULL == 0.0:
        D_log_rho_S = float("inf")  # (local)
    else:
        D_log_rho_S = abs(math.log10(abs_rho_SCH) - math.log10(abs_rho_FULL))  # (local)

    abs_zeta_SCH = abs(zeta_D_SCH)  # (local)
    abs_zeta_FULL = abs(zeta_D_FULL)  # (local)
    if abs_zeta_SCH == 0.0 or abs_zeta_FULL == 0.0:
        D_log_zeta_D = float("inf")  # (local)
    else:
        D_log_zeta_D = abs(math.log10(abs_zeta_SCH) - math.log10(abs_zeta_FULL))  # (local)

    D_max = max(D_log_rho_S, D_log_zeta_D)  # (local)
    return D_max, D_log_rho_S, D_log_zeta_D


def classify_severity_band(D_max: float) -> str:
    """4-band severity classification per epistemic-discipline.md §"Source
    Reconciliation". Pre-registered thresholds; modifying after seeing the
    value is PROHIBITED_ACTIONS Class 3."""
    if D_max < D_MAX_NO_ACTION_THRESHOLD:
        return "NO-ACTION"
    if D_max < D_MAX_ADVISORY_THRESHOLD:
        return "ADVISORY"
    if D_max < D_MAX_MANDATORY_THRESHOLD:
        return "MANDATORY"
    return "HARD-HALT"


def compute() -> dict:
    """Main computation. Returns a dict with D_max + severity band + diagnostics."""
    # ---------- Step 1: Load SCHEMATIC inputs ----------
    print("\n--- Step 1: Load W9b-2 SCHEMATIC inputs ---")
    sch = load_schematic_inputs()
    print(f"  SCHEMATIC composite rho_S_s4 = {sch['rho_S_s4_composite']:+.6f}")
    per_reg_dict = dict(zip(sch["rho_S_per_reg_s4_keys"], sch["rho_S_per_reg_s4_vals"]))  # (local)
    print(f"  SCHEMATIC per-regulator s=4: {per_reg_dict}")
    print(f"  SCHEMATIC zeta_D_s4 = {sch['zeta_D_s4_complex']}")
    print(f"  SCHEMATIC spectral_projection_s4 (4-class) = {sch['spectral_projection_s4_4class']}")
    print(f"  SCHEMATIC dynamical_projection_s4         = {sch['dynamical_projection_s4']}")
    print(f"  SCHEMATIC n_helper_s4 = {sch['n_helper_s4']}, L_max_cache = {sch['L_max_cache']}, "
          f"Vol_SU3_Haar = {sch['Vol_SU3_Haar']:.5f}, tau_fold_npz = {sch['tau_fold_npz']}")

    # ---------- Step 2: Load W3 A.14 cross-wave npz ----------
    print("\n--- Step 2: Load W3 A.14 cross-wave regulator-invariance npz ---")
    w3 = load_w3_a14_cross_wave()
    print(f"  W3 A.14 ratio_zeta    = {w3['ratio_zeta']:.10f}")
    print(f"  W3 A.14 ratio_PV      = {w3['ratio_PV']:.10f}")
    print(f"  W3 A.14 ratio_Mellin  = {w3['ratio_Mellin']:.10f}")
    print(f"  W3 A.14 ratio_cutoff  = {w3['ratio_cutoff']:.10f}")
    print(f"  W3 A.14 max_rel_dev   = {w3['max_rel_dev']:.4e}")
    print(f"  W3 A.14 regulator_class_invariant = {w3['regulator_class_invariant']}")
    print(f"  W3 A.14 substrate_canonical (7.324992 = phi_67/phi_88 ratio) = {w3['substrate_canonical']:.6f}")

    # ---------- Step 3: Build FULL physical PV PRIMARY pipeline ----------
    print("\n--- Step 3: Build FULL physical PRIMARY 2-point PV pipeline ---")
    print(f"  M_KK (canonical) = {M_KK:.10e} GeV")
    print(f"  tau_fold = {tau_fold}")
    print(f"  Λ_UV = M_KK; PV masses M_1 = M_KK, M_2 = √2·M_KK")
    print(f"  PV coefficients c = {PV_PRIMARY_C.tolist()} (target Σc_r=1)")
    print(f"  PV dimensionless masses m_r = {PV_PRIMARY_M_DIMLESS.tolist()} (in M_KK units)")
    s_c_chk, s_cm2_chk = _verify_pv_identities()  # (local)
    print(f"  Identity Σ c_r           = {s_c_chk:.16e} (target 1.0; |dev|={abs(s_c_chk-1):.4e})")
    print(f"  Identity Σ c_r·m_r²      = {s_cm2_chk:.16e} (target 0.0; |dev|={abs(s_cm2_chk):.4e})")

    # ---------- Step 4: Compute FULL-tier rho_S_s4 + zeta_D_s4 ----------
    print("\n--- Step 4: Compute FULL physical rho_S_s4^{FULL} + zeta_D_s4^{FULL} ---")
    # Load L_max=12 D_K spectrum cache (matches W9b-2 cache metadata)
    evs, mults = load_spectrum(L_MAX_FULL_PHYSICAL_PV)
    print(f"  L_max={L_MAX_FULL_PHYSICAL_PV} spectrum loaded: {len(evs)} eigenvalues, "
          f"|λ|_min={evs.min():.6f}, |λ|_max={evs.max():.6f}")

    # Per-class FULL physical spectral_projection at s=4 (Mellin power λ^{-4})
    M_R_full = build_full_physical_pv_pipeline_outputs(evs, mults)
    print(f"  FULL physical per-class spectral_projection at s=4 (Σ m_k · w_R · λ_k^{{-4}} / Vol_SU3_Haar):")
    for k in A5_4CLASS_ORDER:
        print(f"    {k:15s}: {M_R_full[k]:.6e}")

    # FULL spectral_projection 4-vector matching A5_4CLASS_ORDER
    spectral_projection_FULL = np.array([M_R_full[c] for c in A5_4CLASS_ORDER], dtype=np.float64)

    # rho_S_s4^{FULL} = Spearman r(spectral_projection_FULL, dynamical_projection)
    rho_S_s4_FULL, p_full = compute_rho_S_s4_full(
        spectral_projection_FULL, sch["dynamical_projection_s4"]
    )
    print(f"  FULL physical rho_S_s4 = Spearman r(spectral_FULL, dynamical) = {rho_S_s4_FULL:+.6f}  (p={p_full:.4f})")

    # zeta_D_s4^{FULL} on L_max=12 spectrum (bit-identical to SCHEMATIC by construction)
    zeta_D_s4_FULL = zeta_D_direct(complex(S_SUBSTRATE_POLE, 0.0), L_MAX_FULL_PHYSICAL_PV)
    print(f"  FULL physical zeta_D_s4 = zeta_D_direct(s=4, L=12) = {zeta_D_s4_FULL}")
    print(f"  SCHEMATIC     zeta_D_s4 (cached W9b-2)             = {sch['zeta_D_s4_complex']}")

    # SCHEMATIC L=12 per-class spectral_projection (cached as 5-reg; here we
    # use the cached SCHEMATIC L=12 vector from W9b-2 npz to ensure apples-
    # to-apples ordering).
    spectral_projection_SCH = sch["spectral_projection_s4_4class"].copy()

    # ---------- Step 5: Compute D_max ----------
    print("\n--- Step 5: Compute D_max ---")
    rho_S_s4_SCH = sch["rho_S_s4_composite"]  # (local)
    zeta_D_s4_SCH_value = sch["zeta_D_s4_complex"]  # (local)

    D_max, D_log_rho_S, D_log_zeta_D = compute_d_max(
        rho_S_s4_SCH, rho_S_s4_FULL,
        zeta_D_s4_SCH_value, zeta_D_s4_FULL,
    )
    print(f"  D_log_rho_S  = |log10|{rho_S_s4_SCH:+.6f}| - log10|{rho_S_s4_FULL:+.6f}|| = {D_log_rho_S:.6e}")
    print(f"  D_log_zeta_D = |log10|{abs(zeta_D_s4_SCH_value):.6e}| - log10|{abs(zeta_D_s4_FULL):.6e}|| = {D_log_zeta_D:.6e}")
    print(f"  D_max = max(D_log_rho_S, D_log_zeta_D) = {D_max:.6e}")

    # ---------- Step 6: Severity band classification ----------
    severity_band = classify_severity_band(D_max)  # (local)
    print(f"  Severity band: {severity_band} "
          f"(thresholds: NO-ACTION<{D_MAX_NO_ACTION_THRESHOLD}, "
          f"ADVISORY<{D_MAX_ADVISORY_THRESHOLD}, "
          f"MANDATORY<{D_MAX_MANDATORY_THRESHOLD}, HARD-HALT≥{D_MAX_MANDATORY_THRESHOLD})")

    # ---------- Step 7: Inheritance-pin retroactive remediation flag ----------
    print("\n--- Step 7: Inheritance-pin retroactive remediation check ---")
    inheritance_pin_remediation_required = bool(D_max >= INHERITANCE_PIN_REMEDIATION_TRIGGER)  # (local)
    if inheritance_pin_remediation_required:
        print(f"  D_max = {D_max:.4e} >= {INHERITANCE_PIN_REMEDIATION_TRIGGER} OOM")
        print(f"  ⟹ S89+ gates inheriting W4-2 / W9b-2 SCHEMATIC outputs REQUIRE")
        print(f"    Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY tagging per")
        print(f"    substrate-first-canonical-sourcing.md §(iv) §'Inheritance-pin'")
        print(f"    (S88 W-24 V.4 / B.62)")
    else:
        print(f"  D_max = {D_max:.4e} < {INHERITANCE_PIN_REMEDIATION_TRIGGER} OOM")
        print(f"  ⟹ inheritance-pin retroactive remediation NOT required")
        print(f"  SCHEMATIC tier IS faithful proxy at substrate-distance-2 pole s=4")
        print(f"  §VII.AR LEVEL-DRESSED K=4 calibration corpus admissibility on")
        print(f"  SCHEMATIC-tier basis is preserved.")

    return {
        "value": (float(D_max), severity_band),
        "D_max": float(D_max),
        "severity_band": severity_band,
        "D_log_rho_S": float(D_log_rho_S),
        "D_log_zeta_D": float(D_log_zeta_D),
        "rho_S_s4_SCH": float(rho_S_s4_SCH),
        "rho_S_s4_FULL": float(rho_S_s4_FULL),
        "spearman_p_full": float(p_full),
        "zeta_D_s4_SCH_real": float(zeta_D_s4_SCH_value.real),
        "zeta_D_s4_SCH_imag": float(zeta_D_s4_SCH_value.imag),
        "zeta_D_s4_FULL_real": float(zeta_D_s4_FULL.real),
        "zeta_D_s4_FULL_imag": float(zeta_D_s4_FULL.imag),
        "spectral_projection_SCH_4class": spectral_projection_SCH.tolist(),
        "spectral_projection_FULL_4class": spectral_projection_FULL.tolist(),
        "dynamical_projection_s4": sch["dynamical_projection_s4"].tolist(),
        "M_R_full_dict": {k: float(v) for k, v in M_R_full.items()},
        "L_max_schematic_truncation_target": L_MAX,
        "L_max_full_physical_pv": L_MAX_FULL_PHYSICAL_PV,
        "Lambda_UV_GeV": float(M_KK),
        "M_PV_dimensionless": PV_PRIMARY_M_DIMLESS.tolist(),
        "PV_coefficients": PV_PRIMARY_C.tolist(),
        "PV_identity_sum_c_r": float(s_c_chk),
        "PV_identity_sum_c_r_m_r_sq": float(s_cm2_chk),
        "W3_A14_cross_wave": w3,
        "inheritance_pin_remediation_required": inheritance_pin_remediation_required,
        "inheritance_pin_remediation_trigger_threshold": INHERITANCE_PIN_REMEDIATION_TRIGGER,
        "L_max_cache_metadata": sch["L_max_cache"],
        "Vol_SU3_Haar": VOL_SU3_HAAR_LOCAL,
        "tau_fold_evaluation": float(tau_fold),
        "n_helper_s4_schematic": sch["n_helper_s4"],
        "s_substrate_pole": S_SUBSTRATE_POLE,
        "s_index_for_pv_helper": S_INDEX_FOR_PV_HELPER,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(result: dict) -> None:
    """4-panel plot:
       (a) SCH vs FULL per-class spectral_projection bar chart (log y)
       (b) rho_S_s4 SCH vs FULL bar chart
       (c) zeta_D_s4 SCH vs FULL bar chart (log y)
       (d) D_max severity-band thermometer
    """
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))
    classes = A5_4CLASS_ORDER

    # Panel (a): per-class spectral_projection SCH vs FULL
    ax = axes[0, 0]
    sch_vals = result["spectral_projection_SCH_4class"]
    full_vals = result["spectral_projection_FULL_4class"]
    x = np.arange(len(classes))
    width = 0.36  # (local)
    ax.bar(x - width / 2, sch_vals, width, color="C0", edgecolor="black", label="SCHEMATIC L=12")
    ax.bar(x + width / 2, full_vals, width, color="C3", edgecolor="black", label="FULL physical PV PRIMARY L=12")
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(classes)
    ax.set_ylabel("spectral_projection (Σ m_k w_R λ_k^{-4} / Vol_SU3_Haar)")
    ax.set_title("(a) Per-class spectral_projection at s=4 (substrate-distance-2)")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3, axis="y", which="both")

    # Panel (b): rho_S_s4 SCH vs FULL
    ax = axes[0, 1]
    names = ["SCHEMATIC", "FULL physical PV PRIMARY"]
    vals = [result["rho_S_s4_SCH"], result["rho_S_s4_FULL"]]
    colors = ["C0", "C3"]
    bars = ax.bar(names, vals, color=colors, edgecolor="black", width=0.6)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.04 * np.sign(v) if v != 0 else 0.05,
                f"{v:+.4f}", ha="center", va="bottom" if v >= 0 else "top", fontsize=11)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_ylabel("rho_S(s=4) = Spearman r(spectral_R, dynamical)")
    ax.set_ylim(-1.2, 1.2)
    ax.set_title(f"(b) rho_S_s4 SCH vs FULL  |Δlog10|={result['D_log_rho_S']:.4e}")
    ax.grid(alpha=0.3, axis="y")

    # Panel (c): zeta_D_s4 SCH vs FULL on log y
    ax = axes[1, 0]
    sch_zeta = abs(complex(result["zeta_D_s4_SCH_real"], result["zeta_D_s4_SCH_imag"]))
    full_zeta = abs(complex(result["zeta_D_s4_FULL_real"], result["zeta_D_s4_FULL_imag"]))
    bars = ax.bar(["SCHEMATIC", "FULL physical"], [sch_zeta, full_zeta],
                  color=["C0", "C3"], edgecolor="black", width=0.6)
    for b, v in zip(bars, [sch_zeta, full_zeta]):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.1, f"{v:.5e}", ha="center", va="bottom", fontsize=10)
    ax.set_yscale("log")
    ax.set_ylabel("|zeta_D(s=4)| (truncated Dirichlet form, L=12)")
    ax.set_title(f"(c) zeta_D_s4 SCH vs FULL  |Δlog10|={result['D_log_zeta_D']:.4e}")
    ax.grid(alpha=0.3, axis="y", which="both")

    # Panel (d): D_max severity-band thermometer
    ax = axes[1, 1]
    bands = ["NO-ACTION\n[0, 0.1)", "ADVISORY\n[0.1, 1.0)", "MANDATORY\n[1.0, 3.0)", "HARD-HALT\n[3.0, ∞)"]
    band_edges = [0.0, D_MAX_NO_ACTION_THRESHOLD, D_MAX_ADVISORY_THRESHOLD, D_MAX_MANDATORY_THRESHOLD, 4.0]
    band_colors = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728"]
    for i in range(4):
        ax.fill_betweenx([0, 1], band_edges[i], band_edges[i + 1], color=band_colors[i],
                         alpha=0.32, label=bands[i])
    # D_max marker
    ax.axvline(result["D_max"], color="black", linestyle="--", linewidth=2.0,
               label=f"D_max = {result['D_max']:.4e}")
    ax.set_xlim(0, 4.0)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel("D_max (OOM in log10)")
    ax.set_title(f"(d) Severity band: {result['severity_band']}  "
                 f"(inheritance_pin_remediation_required={result['inheritance_pin_remediation_required']})")
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(alpha=0.3, axis="x")

    plt.suptitle(
        f"{GATE_ID}  L_max=10 (SCH) / 12 (FULL)  Λ_UV=M_KK={M_KK:.4e} GeV  "
        f"D_max={result['D_max']:.4e}  band={result['severity_band']}",
        fontsize=11, y=1.00,
    )
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"\n  Plot saved: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + dual-SHA + 3-tuple companion row
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def evaluate_gate(D_max: float) -> tuple[str, str, str, str]:
    """Return (composite_verdict, sign_verdict, magnitude_verdict, regime_verdict).

    Pre-registered:
      composite PASS iff D_max < D_MAX_ADVISORY_THRESHOLD (1.0 OOM); the
      magnitude_verdict tracks the 4-band thresholds (PASS=NO-ACTION+ADVISORY,
      INFO=MANDATORY, FAIL=HARD-HALT). The sign_verdict is direction-based:
      Step 5 of the substitution chain pre-registers `D_max in NO-ACTION/
      ADVISORY ⟹ SCHEMATIC faithful proxy; D_max in MANDATORY/HARD-HALT ⟹
      inheritance-pin retroactive remediation MANDATORY`. The expected
      direction (per `pauli_villars_a_n` docstring) is that SCHEMATIC and
      FULL physical PV coincide modulo closed-form scalar, so D_max < 1.0
      is the predicted direction. sign_verdict=PASS iff D_max < 1.0; FAIL
      otherwise.

      regime_verdict: VALID (both SCHEMATIC and FULL physical are evaluated
      on positive-definite truncated spectra at L_max ≤ 12 with no boundary
      crossings; the 4-band 5%/50% domain test does NOT apply because the
      evaluation has no scan-domain shortening).
    """
    if D_max < D_MAX_NO_ACTION_THRESHOLD or D_max < D_MAX_ADVISORY_THRESHOLD:
        magnitude_verdict = "PASS"
    elif D_max < D_MAX_MANDATORY_THRESHOLD:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"

    sign_verdict = "PASS" if D_max < D_MAX_ADVISORY_THRESHOLD else "FAIL"

    regime_verdict = "VALID"

    # Composite collapse (gate-verdicts.md §"Composite-collapse rule")
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    return composite, sign_verdict, magnitude_verdict, regime_verdict


def append_verdict(composite: str, value_payload: str,
                   audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    """Single-shot atomic append: canonical line + dual-SHA companion + 3-tuple
    companion row + tier_pin TIER-2 SCHEMATIC level pin disclosure row.

    Forbidden: read-modify-write or truncate-and-rewrite. Single `open("a")`
    write per POSIX O_APPEND semantics."""
    audit_short = audit_sha[:16]
    content_short = content_sha[:16]
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_payload}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+\n"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_short} content_sha256_short={content_short} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2) | "
        f"Substitution chain Step 5: D_max in NO-ACTION/ADVISORY ⟹ SCHEMATIC faithful proxy + "
        f"inheritance-pin retroactive remediation NOT required; "
        f"D_max in MANDATORY/HARD-HALT ⟹ inheritance-pin retroactive remediation MANDATORY per "
        f"substrate-first-canonical-sourcing.md §(iv) §'Inheritance-pin' (S88 W-24 V.4 / B.62)\n"
    )
    tier_pin_companion = (
        f"# tier_pin=TIER-2 # {GATE_ID} SCHEMATIC level pin discipline "
        f"(per substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY; "
        f"SCHEMATIC tier consumed via s87_w9b_pole_specificity_scan.npz "
        f"+ _spectral_action_regulators.py SCHEMATIC docstring lines 23-30; "
        f"FULL physical PRIMARY 2-point PV pipeline via _pauli_villars_subtraction.py "
        f"Connes-Chamseddine 1996 §2.2-2.3 multipliers)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_companion)
        fp.write(three_tuple_companion)
        fp.write(tier_pin_companion)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input SHA-256 pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure (legacy): {closure[:16]}...")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 2. Compute
    result = compute()

    # 3. Evaluate gate
    composite, sign_v, mag_v, regime_v = evaluate_gate(result["D_max"])

    # 4. Emit 4-tuple + npz + json + plot
    value_payload = (
        f"D_max={result['D_max']:.6e};severity_band={result['severity_band']};"
        f"D_log_rho_S={result['D_log_rho_S']:.6e};D_log_zeta_D={result['D_log_zeta_D']:.6e};"
        f"rho_S_s4_SCH={result['rho_S_s4_SCH']:+.6f};rho_S_s4_FULL={result['rho_S_s4_FULL']:+.6f};"
        f"zeta_D_s4_SCH={result['zeta_D_s4_SCH_real']:.6e};zeta_D_s4_FULL={result['zeta_D_s4_FULL_real']:.6e};"
        f"inheritance_pin_remediation_required={result['inheritance_pin_remediation_required']};"
        f"L_max_schematic_truncation_target={result['L_max_schematic_truncation_target']};"
        f"L_max_full_physical_pv={result['L_max_full_physical_pv']};"
        f"Lambda_UV_GeV={result['Lambda_UV_GeV']:.6e};"
        f"PV_2point_M_dimless={result['M_PV_dimensionless']};"
        f"PV_2point_c={result['PV_coefficients']};"
        f"PV_identity_sum_c_r={result['PV_identity_sum_c_r']:.16e};"
        f"PV_identity_sum_c_r_m_r_sq={result['PV_identity_sum_c_r_m_r_sq']:.16e};"
        f"W3_A14_regulator_class_invariant={result['W3_A14_cross_wave']['regulator_class_invariant']};"
        f"W3_A14_max_rel_dev={result['W3_A14_cross_wave']['max_rel_dev']:.4e};"
        f"W3_A14_substrate_canonical={result['W3_A14_cross_wave']['substrate_canonical']};"
        f"tau_fold={result['tau_fold_evaluation']}"
    )
    tag = emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX)
    print(f"\n{tag}")

    # NPZ dump
    np.savez(
        OUT_NPZ,
        D_max=np.array([result["D_max"]]),
        severity_band=np.array([result["severity_band"]]),
        D_log_rho_S=np.array([result["D_log_rho_S"]]),
        D_log_zeta_D=np.array([result["D_log_zeta_D"]]),
        rho_S_s4_SCH=np.array([result["rho_S_s4_SCH"]]),
        rho_S_s4_FULL=np.array([result["rho_S_s4_FULL"]]),
        spearman_p_full=np.array([result["spearman_p_full"]]),
        zeta_D_s4_SCH=np.array([complex(result["zeta_D_s4_SCH_real"], result["zeta_D_s4_SCH_imag"])]),
        zeta_D_s4_FULL=np.array([complex(result["zeta_D_s4_FULL_real"], result["zeta_D_s4_FULL_imag"])]),
        spectral_projection_SCH_4class=np.array(result["spectral_projection_SCH_4class"]),
        spectral_projection_FULL_4class=np.array(result["spectral_projection_FULL_4class"]),
        dynamical_projection_s4=np.array(result["dynamical_projection_s4"]),
        M_R_full_keys=np.array(list(result["M_R_full_dict"].keys())),
        M_R_full_vals=np.array(list(result["M_R_full_dict"].values())),
        L_max_schematic_truncation_target=np.array([result["L_max_schematic_truncation_target"]]),
        L_max_full_physical_pv=np.array([result["L_max_full_physical_pv"]]),
        Lambda_UV_GeV=np.array([result["Lambda_UV_GeV"]]),
        PV_M_dimensionless=np.array(result["M_PV_dimensionless"]),
        PV_coefficients=np.array(result["PV_coefficients"]),
        PV_identity_sum_c_r=np.array([result["PV_identity_sum_c_r"]]),
        PV_identity_sum_c_r_m_r_sq=np.array([result["PV_identity_sum_c_r_m_r_sq"]]),
        Vol_SU3_Haar=np.array([result["Vol_SU3_Haar"]]),
        tau_fold=np.array([result["tau_fold_evaluation"]]),
        n_helper_s4_schematic=np.array([result["n_helper_s4_schematic"]]),
        s_substrate_pole=np.array([result["s_substrate_pole"]]),
        s_index_for_pv_helper=np.array([result["s_index_for_pv_helper"]]),
        inheritance_pin_remediation_required=np.array([result["inheritance_pin_remediation_required"]]),
        inheritance_pin_remediation_trigger_threshold=np.array([result["inheritance_pin_remediation_trigger_threshold"]]),
        W3_A14_ratio_zeta=np.array([result["W3_A14_cross_wave"]["ratio_zeta"]]),
        W3_A14_ratio_PV=np.array([result["W3_A14_cross_wave"]["ratio_PV"]]),
        W3_A14_ratio_Mellin=np.array([result["W3_A14_cross_wave"]["ratio_Mellin"]]),
        W3_A14_ratio_cutoff=np.array([result["W3_A14_cross_wave"]["ratio_cutoff"]]),
        W3_A14_max_rel_dev=np.array([result["W3_A14_cross_wave"]["max_rel_dev"]]),
        W3_A14_spread_across_regulators=np.array([result["W3_A14_cross_wave"]["spread_across_regulators"]]),
        W3_A14_regulator_class_invariant=np.array([result["W3_A14_cross_wave"]["regulator_class_invariant"]]),
        W3_A14_substrate_canonical=np.array([result["W3_A14_cross_wave"]["substrate_canonical"]]),
        composite_verdict=np.array([composite]),
        sign_verdict=np.array([sign_v]),
        magnitude_verdict=np.array([mag_v]),
        regime_verdict=np.array([regime_v]),
        gate_id=np.array([GATE_ID]),
        scheme=np.array([SCHEME]),
        convention=np.array([CONVENTION]),
        audit_sha256=np.array([audit_sha]),
        content_sha256=np.array([content_sha]),
    )
    print(f"  NPZ saved: {OUT_NPZ}")

    # JSON sidecar
    json_payload = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max_schematic_truncation_target": result["L_max_schematic_truncation_target"],
        "L_max_full_physical_pv": result["L_max_full_physical_pv"],
        "Lambda_UV_GeV": result["Lambda_UV_GeV"],
        "tau_fold": result["tau_fold_evaluation"],
        "D_max": result["D_max"],
        "severity_band": result["severity_band"],
        "D_log_rho_S": result["D_log_rho_S"],
        "D_log_zeta_D": result["D_log_zeta_D"],
        "rho_S_s4_SCH": result["rho_S_s4_SCH"],
        "rho_S_s4_FULL": result["rho_S_s4_FULL"],
        "spearman_p_full": result["spearman_p_full"],
        "zeta_D_s4_SCH": {"real": result["zeta_D_s4_SCH_real"], "imag": result["zeta_D_s4_SCH_imag"]},
        "zeta_D_s4_FULL": {"real": result["zeta_D_s4_FULL_real"], "imag": result["zeta_D_s4_FULL_imag"]},
        "spectral_projection_SCH_4class": result["spectral_projection_SCH_4class"],
        "spectral_projection_FULL_4class": result["spectral_projection_FULL_4class"],
        "dynamical_projection_s4": result["dynamical_projection_s4"],
        "M_R_full": result["M_R_full_dict"],
        "PV_2point_M_dimensionless": result["M_PV_dimensionless"],
        "PV_2point_coefficients": result["PV_coefficients"],
        "PV_identity_sum_c_r": result["PV_identity_sum_c_r"],
        "PV_identity_sum_c_r_m_r_sq": result["PV_identity_sum_c_r_m_r_sq"],
        "Vol_SU3_Haar": result["Vol_SU3_Haar"],
        "n_helper_s4_schematic": result["n_helper_s4_schematic"],
        "s_substrate_pole": result["s_substrate_pole"],
        "s_index_for_pv_helper": result["s_index_for_pv_helper"],
        "inheritance_pin_remediation_required": result["inheritance_pin_remediation_required"],
        "inheritance_pin_remediation_trigger_threshold": result["inheritance_pin_remediation_trigger_threshold"],
        "W3_A14_cross_wave": result["W3_A14_cross_wave"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "verdict": {
            "composite": composite,
            "sign_verdict": sign_v,
            "magnitude_verdict": mag_v,
            "regime_verdict": regime_v,
        },
        "thresholds_pre_registered": {
            "D_max_no_action": D_MAX_NO_ACTION_THRESHOLD,
            "D_max_advisory": D_MAX_ADVISORY_THRESHOLD,
            "D_max_mandatory": D_MAX_MANDATORY_THRESHOLD,
            "inheritance_pin_remediation_trigger": INHERITANCE_PIN_REMEDIATION_TRIGGER,
        },
    }
    OUT_JSON.write_text(json.dumps(json_payload, indent=2, sort_keys=True), encoding="utf-8")
    print(f"  JSON saved: {OUT_JSON}")

    # Plot
    make_plot(result)

    # Append canonical verdict line (single-shot atomic append)
    append_verdict(composite, value_payload, audit_sha, content_sha, sign_v, mag_v, regime_v)
    print(f"\n  Verdict line appended to: {VERDICT_TXT}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (D_max={result['D_max']:.4e}, "
          f"band={result['severity_band']}, wall {wall:.1f}s) ===")
    print(f"    sign_verdict={sign_v}, magnitude_verdict={mag_v}, regime_verdict={regime_v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
