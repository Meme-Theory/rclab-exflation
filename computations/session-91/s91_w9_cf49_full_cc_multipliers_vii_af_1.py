#!/usr/bin/env python3
"""
S91 W9-4 - S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE  (T2.15)
======================================================================

Gate-ID:  S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE
Aliases:  S91-W9-4 ; S91-VII-AF-1-OP-PROJ-FULL-CC-MULTIPLIERS-UPGRADE
Trigger:  [VERIFY]  (S87+ schema-v2 3-tuple companion row required)
Owner:    connes-ncg-theorist  (PRIMARY; canonical authority for
          Connes-Chamseddine 1996 §2.2-2.3 physical multiplier pipeline)

Provenance:  S90 W6 CF-W7-1 / CF-49 carry-forward
             (lizzi-spectral-functional-theorist s7 §(5)).
Plan ref:    sessions/session-plan/session-91-plan-w9.md §W9-4
             (lines 595-763).

PURPOSE
-------
UPGRADE the §VII.AF.1.OP-PROJ Pillar III ↔ Pillar IV bridge theorem from
PARTIAL-POSITIVE compliance (SCHEMATIC `_spectral_action_regulators.py`
Mellin helper) to POSITIVE compliance (FULL Connes-Chamseddine 1996
§2.2-2.3 physical multipliers).  Per `.claude/rules/substrate-first-
canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline, the
SCHEMATIC tag is replaced by the FULL physical multipliers tag
`-FULL-CC-MULTIPLIERS-PHYSICAL`; CLASS pin = FULL.

PIPELINE
--------
Per plan §W9-4 Field 6 substitution chain Step 1-5:

  Step 1 (Definition, Connes-Chamseddine 1996 §2.2-2.3):
    Tr f(D_K / Λ)  with  f(x) = Σ_{j=1..2} c_j · exp(-(x/M_j)^2)
      (M_1, c_1) = (M_KK,         +2)
      (M_2, c_2) = (√2 · M_KK,    -1)
    Pauli-Villars consistency at the substrate-IS algebra layer:
      Σ_r c_r        = +1       (UV identity; Σc_r = 1)
      Σ_r c_r M_r²   = 0        (no quadratic divergence; Σc_r M_r² = 0)

  Step 2 (Seeley-DeWitt closed forms):
    a_n^{CC} = Γ(n/2) · (c_1 · M_1^n + c_2 · M_2^n)
    n=2:  a_2^{CC} = Γ(1) · (2·M_KK² + (-1)·2·M_KK²) = 0       (PV cancellation)
    n=4:  a_4^{CC} = Γ(2) · (2·M_KK⁴ + (-1)·4·M_KK⁴) = -2·M_KK⁴

  Step 3 (Hochschild pairing on A_F core algebra at substrate-distance-1
          pole s=3):
    R_universal_FULL = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩
                       evaluated under FULL CC PV multiplier
                       w_PV(λ²; s) = 1 - Σ_r c_r · (M_r² / (λ² + M_r²))^s
                       at substrate-distance-1 pole s=3 on the
                       L_max=12 master cache.

  Step 4 (Numerical evaluation):
    Load L_max=12 master spectrum cache (90 Peter-Weyl sectors;
    166,896 raw eigenvalues; multiplicity-weighted ~32M states).
    Compute regulator-INVARIANT atlas ratio:
        rho_FULL(s=3) := M_FULL(s=3) / M_BARE(s=3)
    (Mellin moments at substrate-distance-1 pole; FULL = PV-regulated
    via Connes-Chamseddine 1996; BARE = zeta/SDW pure spectrum-sum.)
    The §VII.AF.1.OP-PROJ substrate-IS Hochschild-pairing image at
    L_max=12 reads back as the regulator-invariant atlas ratio under
    the canonical Pillar III ↔ Pillar IV cohomology-class identity.

  Step 5 (Direction reading):
    Per registry §VII.AF.1.OP-PROJ Level-3 anchor at L_max=10:
        R_universal_HP1_strict_F4 -> 1.030902
        (canonical pin per canonical_constants.py;
         W-5 V4 SDW residual ratio)
        match/envelope ratio r -> 19/200 -> 0.0950
    The FULL CC regulator-INVARIANT atlas ratio rho_FULL(s=3) at
    L_max=12 reproduces the regulator-invariant cohomology-class
    identity of §VII.AF.1.OP-PROJ within the sub-envelope first-
    extraction floor:
        Delta_FULL := (rho_FULL_image - R_canonical_AF1) / R_canonical_AF1
        PASS iff |Delta_FULL| < 1e-3   (0.1%; per plan Field 9)
        FAIL iff |Delta_FULL| > 1e-2   (1%; SCHEMATIC pin systematically biased)
        INFO iff 1e-3 ≤ |Delta_FULL| ≤ 1e-2   (marginal)

  Cross-link (plan Field 6 Step 5 NB):
    gv_canonical_difference_FW = -40579.1500479506   is the §VII.AQ
    pin (NOT the §VII.AF.1 canonical; §VII.AF.1 canonical lives at
    L_emp(L_max=10) per registry — Level-3 anchor 1.030902 = STRICT_F4
    atlas match per S87 W5-1 LANDING).  The plan substitution chain
    cites this only as cross-link for W1 T1.1 §VII.AV cross-pin.

SUBSTRATE FRAMING (per phononic-framing.md §"IS Space, Not IN Space")
---------------------------------------------------------------------
The substrate IS the spectral triple (A_K, H_K, D_K) at τ_fold = 0.19;
the FULL CC multipliers (M_KK, √2·M_KK, +2, -1) ARE the substrate's
intrinsic regularization tuple at the M_KK compactification scale (NOT
"an external regulator applied to the substrate").  The Pauli-Villars
cancellation identities (Σc_r = 1 and Σc_r M_r² = 0) ARE substrate-IS
algebraic constraints on the regularization tuple, derived from the
Connes-Chamseddine 1996 framework at the NCG-axiomatic spectral-action
layer.  The §VII.AF.1.OP-PROJ over-performance regime IS the substrate's
Hochschild pairing on the F_2-class K-invariant identity sub-atlas
evaluated at L_max=12 under FULL CC physical multipliers.

Direction:
    substrate (Hochschild pairing on (A_K, H_K, D_K) IS regularized
    via FULL CC) → bridge (HKR L_max → ∞) → laboratory (Pillar IV
    BZ-trace R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k;τ_fold) d^d k).

FORBIDDEN container-inversion:
    "Pillar IV BZ-trace IS the canonical and Pillar III/IV Hochschild
     pairing IS its approximation"
INVERT:
    "substrate Hochschild pairing IS the canonical; Pillar IV BZ-trace
     IS the laboratory image under HKR."

CONVENTION TAG  (per substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY)
----------------------------------------------------------------------------
    LEVEL_CLASS_PIN = FULL  (FULL physical replacement of SCHEMATIC
                              `_spectral_action_regulators.py` Mellin helper;
                              consumes _pauli_villars_subtraction.py PRIMARY
                              landed S88 W13-159 lizzi)
    convention      = VII-AF-1-OP-PROJ-FULL-CC-MULTIPLIERS-PHYSICAL-
                       substrate-distance-1-pole-s3

INPUT FILES
-----------
- computations/_shared/canonical_constants.py
- computations/session-84/s84_spectrum_cache_L12_tau019.npz (L_max=12
  master spectrum cache; 90 (p,q) sectors)
- computations/_pauli_villars_subtraction.py (PRIMARY FULL CC PV helper)
- script bytes

OUTPUTS (per plan §W9-4 Field 8)
--------------------------------
- computations/session-91/s91_w9_cf49_full_cc_multipliers_vii_af_1.npz
- computations/session-91/s91_w9_cf49_full_cc_multipliers_vii_af_1.png
- computations/session-91/s91_gate_verdicts.txt
   (canonical line + dual-SHA companion + S87+ 3-tuple companion +
    LEVEL pin row + promotion-target row)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import math
import sys
import time
from pathlib import Path

from scipy.special import gamma

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
sys.path.insert(0, str(ROOT / "computations"))

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Canonical constants (mandatory imports per math-scripts.md S34+).
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    gv_canonical_difference_FW,
    R_universal_HP1_strict_F4,
    eps_H_HP1_norm,
)

# FULL physical Pauli-Villars helper (PRIMARY tier per
# substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY).
from _pauli_villars_subtraction import (  # noqa: E402
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
    bare_mellin_moment,
    pv_mellin_moment_primary,
    pv_multiplier_primary,
    _verify_pv_identities,
)


# ====================== Gate-block constants (plan §W9-4 Field 7) ======================

GATE_ID = "S91-W6-CF-W7-1-CF-49-FULL-CC-MULTIPLIERS-UPGRADE"
SCHEME = "full-connes-chamseddine-1996-physical-multipliers-spectral-action-pipeline"
CONVENTION = (
    "VII-AF-1-OP-PROJ-FULL-CC-MULTIPLIERS-PHYSICAL-substrate-distance-1-pole-s3"
)
L_MAX = 12  # (local) plan-pinned canonical anchor at L_max=12 master cache

# Connes-Chamseddine 1996 §2.2-2.3 physical multipliers (canonical PV pair).
M_1_FW_CC = M_KK                       # (local) canonical mass scale
M_2_FW_CC = math.sqrt(2.0) * M_KK      # (local) 2-point PV pair upper mass
C_1_FW_CC = +2                         # (local) PV coefficient 1
C_2_FW_CC = -1                         # (local) PV coefficient 2

# Substrate-distance-1 pole at Mellin index s=3 (per registry §VII.AF.1.OP-PROJ
# Cell I classification: INVARIANT × s=3; spectrum-only INVARIANT functional
# via a_4^ζ residue at s=0; substrate-distance-1 cone ↔ s=3 Mellin pole).
S_POLE = 3                              # (local) substrate-distance-1 pole

# Pre-registered thresholds (plan §W9-4 Field 9 RATIO tolerance rule).
SUB_ENVELOPE_TOL = 1e-3                 # (local) PASS threshold (0.1%)
FAIL_TOL = 1e-2                         # (local) FAIL threshold (1%)

# §VII.AF.1.OP-PROJ Level-3 anchor canonical (per registry line 14790, W-5 V4
# substitution chain Step 3; STRICT_F4 atlas match at L_max=10).
R_CANONICAL_AF1 = R_universal_HP1_strict_F4  # (local) = 1.030902 canonical pin

# Cross-link pin (plan §W9-4 Step 5 NB; §VII.AQ pin, NOT §VII.AF.1 canonical).
GV_CROSS_LINK = gv_canonical_difference_FW    # (local) = -40579.1500479506

# Output paths.
OUT_NPZ = ROOT / "computations" / "session-91" / "s91_w9_cf49_full_cc_multipliers_vii_af_1.npz"
OUT_PNG = ROOT / "computations" / "session-91" / "s91_w9_cf49_full_cc_multipliers_vii_af_1.png"
VERDICT_FILE = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"

# Input file paths (for SHA-pin map).
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
PV_HELPER = ROOT / "computations" / "_pauli_villars_subtraction.py"
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "L12_spectrum_cache_tau019": L12_CACHE,
    "pauli_villars_helper_PRIMARY": PV_HELPER,
    "registry_vii_af_1_op_proj": REGISTRY,
    "script": SCRIPT_PATH,
}


# ============================== SHA helpers ==============================

def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()                # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}                            # (local)
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print("=" * 72)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:36s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)          # (local)
        pins[name] = sha
        print(f"  {name:36s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()                                  # (local)
    return audit, content


# ============================== Spectrum loader ==============================

def load_spectrum_flat(cache_path: Path):
    """Load L_max=12 master spectrum cache.

    Returns flat (lambdas, mults, n_sectors) where each (p,q) sector
    contributes Peter-Weyl multiplicity dim(p,q) per eigenvalue.  Per
    plan §W9-4 Field 7 and the canonical S88 W13-159 PRIMARY PV helper
    convention.
    """
    cache = np.load(cache_path, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    lambdas_list = []                    # (local)
    mults_list = []                      # (local)
    n_sectors = 0                        # (local)
    for (p, q), info in sector_evals.items():
        n_sectors += 1
        dim = int(info["dim"])           # (local) Peter-Weyl dim(p,q)
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)
        for v in evals_arr:
            lambdas_list.append(float(v))
            mults_list.append(dim)
    lambdas = np.array(lambdas_list, dtype=np.float64)
    mults = np.array(mults_list, dtype=np.float64)
    return lambdas, mults, n_sectors


# ============================ Seeley-DeWitt CC closed forms ============================

def cc_a_n_closed_form(n: int, M1: float, c1: float, M2: float, c2: float) -> float:
    """a_n^{CC} = Γ(n/2) · (c_1 · M_1^n + c_2 · M_2^n).

    Per plan §W9-4 Field 6 Step 2 (Connes-Chamseddine 1996 §2.2-2.3).
    """
    return float(gamma(n / 2.0)) * (c1 * (M1 ** n) + c2 * (M2 ** n))


# ============================ Verdict evaluation ============================

def evaluate_verdict(delta_full: float) -> dict:
    """Plan §W9-4 Field 9 RATIO tolerance rule (S87+ schema-v2 3-tuple form):
        PASS iff |Delta_FULL| < SUB_ENVELOPE_TOL = 1e-3
        INFO iff SUB_ENVELOPE_TOL ≤ |Delta_FULL| ≤ FAIL_TOL = 1e-2
        FAIL iff |Delta_FULL| > FAIL_TOL
    """
    abs_delta = abs(delta_full)
    if abs_delta < SUB_ENVELOPE_TOL:
        composite = "PASS"
        sign_v = "PASS"
        mag_v = "PASS"
        reg_v = "VALID"
    elif abs_delta <= FAIL_TOL:
        composite = "INFO"
        sign_v = "PASS"
        mag_v = "INFO"
        reg_v = "MARGINAL"
    else:
        composite = "FAIL"
        sign_v = "FAIL"
        mag_v = "FAIL"
        reg_v = "VALID"
    return {
        "composite": composite,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
        "promote_pass": (composite == "PASS"),
    }


# ============================ Diagnostic plot ============================

def make_plot(
    M_BARE: float,
    M_FULL_CC: float,
    rho_FULL: float,
    R_canonical: float,
    delta_full: float,
    a_2_CC: float,
    a_4_CC: float,
    w_PV_min: float,
    w_PV_mean: float,
    w_PV_max: float,
):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: BARE vs FULL CC Mellin moment at substrate-distance-1 pole s=3.
    ax1.bar(
        ["M_BARE(s=3)", "M_FULL_CC(s=3)"],
        [M_BARE, M_FULL_CC],
        color=["steelblue", "darkorange"],
        edgecolor="black",
    )
    ax1.set_yscale("log")
    ax1.set_ylabel("Mellin moment value (log scale)")
    ax1.set_title(
        f"Substrate-distance-1 pole s={S_POLE} Mellin moments (L_max={L_MAX})\n"
        f"rho_FULL = M_FULL_CC / M_BARE = {rho_FULL:+.6e}"
    )
    ax1.grid(True, axis="y", alpha=0.3)

    # Panel 2: rho_FULL_image vs R_canonical_AF1.
    ax2.bar(
        ["rho_FULL_image", "R_canonical_AF1"],
        [rho_FULL, R_canonical],
        color=["darkorange", "forestgreen"],
        edgecolor="black",
    )
    ax2.set_ylabel("Atlas ratio (dimensionless)")
    ax2.set_title(
        f"§VII.AF.1.OP-PROJ canonical comparison\n"
        f"Delta_FULL = (rho - R_canonical) / R_canonical = {delta_full:+.6e}\n"
        f"SUB_ENVELOPE_TOL = {SUB_ENVELOPE_TOL:.0e}  FAIL_TOL = {FAIL_TOL:.0e}"
    )
    ax2.grid(True, axis="y", alpha=0.3)

    # Panel 3: Closed-form CC a_n coefficients (machine-precision identity check).
    a_2_predicted = 0.0                                                # (local)
    a_4_predicted = -2.0 * (M_KK ** 4)                                  # (local)
    ax3.bar(
        ["a_2_CC (computed)", "a_2 (expected=0)",
         "a_4_CC / M_KK^4 (computed)", "a_4 / M_KK^4 (expected=-2)"],
        [a_2_CC / (M_KK ** 2), 0.0,
         a_4_CC / (M_KK ** 4), a_4_predicted / (M_KK ** 4)],
        color=["darkorange", "forestgreen", "darkorange", "forestgreen"],
        edgecolor="black",
    )
    ax3.axhline(0.0, color="black", linewidth=1.0)
    ax3.set_ylabel("Seeley-DeWitt coefficient (M_KK-normalized)")
    ax3.set_title(
        "Closed-form Seeley-DeWitt CC coefficients\n"
        "a_n^{CC} = Γ(n/2) · (c_1·M_1^n + c_2·M_2^n) ; PV cancellation at n=2"
    )
    ax3.grid(True, axis="y", alpha=0.3)
    ax3.tick_params(axis="x", labelsize=8, rotation=20)

    # Panel 4: PV multiplier statistics across the L_max=12 spectrum.
    ax4.bar(
        ["w_PV_min", "w_PV_mean", "w_PV_max"],
        [w_PV_min, w_PV_mean, w_PV_max],
        color=["green", "gray", "red"],
        edgecolor="black",
    )
    ax4.axhline(1.0, color="black", linestyle="--", linewidth=1.0,
                label="UV identity (w_PV = 1)")
    ax4.axhline(0.0, color="black", linestyle="-", linewidth=1.0,
                label="IR zero (w_PV = 0)")
    ax4.set_ylabel("PV multiplier value")
    ax4.set_title(
        f"PV multiplier statistics on L_max={L_MAX} spectrum (s={S_POLE})\n"
        f"min, mean, max across all 90 Peter-Weyl sectors"
    )
    ax4.legend(loc="best", fontsize=9)
    ax4.grid(True, axis="y", alpha=0.3)

    fig.suptitle(
        f"S91 W9-4 §VII.AF.1.OP-PROJ FULL CC multipliers upgrade  "
        f"(SCHEMATIC → FULL physical)",
        fontsize=12,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ============================== Verdict emission ==============================

def append_verdict(
    composite: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
    sign_v: str,
    mag_v: str,
    reg_v: str,
    promote_pass: bool,
):
    """Atomic single-shot append per gate-verdicts.md S87+ canonical form:
    canonical line + dual-SHA companion + S87+ 3-tuple companion + LEVEL pin
    + §VII.AF.1.OP-PROJ promotion-target row.
    """
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    level_pin = (
        f"# LEVEL_CLASS_PIN=FULL "
        f"# {GATE_ID} substrate-first-canonical-sourcing.md §(iv) "
        f"K=4 MANDATORY level-pin compliance "
        f"(SCHEMATIC -> FULL physical CC multipliers upgrade; "
        f"PARTIAL-POSITIVE -> POSITIVE compliance class)\n"
    )
    if promote_pass:
        promotion_target = (
            f"# promotion_target=permanent-results-registry.md §VII.AF.1.OP-PROJ "
            f"compliance_class_transition=PARTIAL-POSITIVE->POSITIVE "
            f"# {GATE_ID} VII.AF.1.OP-PROJ K=4 level-pin POSITIVE compliance achieved\n"
        )
    else:
        promotion_target = (
            f"# promotion_target=permanent-results-registry.md §VII.AF.1.OP-PROJ "
            f"compliance_class_transition=PARTIAL-POSITIVE-RETAINED "
            f"# {GATE_ID} VII.AF.1.OP-PROJ FULL CC upgrade NOT achieved "
            f"(composite={composite}; FULL CC diverges from SCHEMATIC canonical)\n"
        )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        f.write(level_pin)
        f.write(promotion_target)


# ============================== Main ==============================

def main() -> int:
    t0 = time.time()

    # 1. Log input pins + compute dual SHA.
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print()
    print(f"  audit_sha256   = {audit_sha[:16]}...  (script + canonical + pinmap)")
    print(f"  content_sha256 = {content_sha[:16]}...  (script only)")
    print()

    # 2. PV identity machine-precision self-check (substrate-IS algebra layer
    #    constraints; Connes-Chamseddine 1996 §2.2-2.3 multiplier pipeline).
    print("PV PRIMARY helper self-check (substrate-IS PV identities):")
    s_c, s_cm2 = _verify_pv_identities()
    print(f"  Σ c_r        = {s_c:.16e}   (target +1.0)")
    print(f"  Σ c_r m_r²   = {s_cm2:.16e}   (target  0.0)")
    print(f"  PV pair: (c_1, c_2) = ({PV_PRIMARY_C[0]:+.1f}, {PV_PRIMARY_C[1]:+.1f})")
    print(f"  PV pair: (m_1, m_2) = ({PV_PRIMARY_M_DIMLESS[0]:.6f}, {PV_PRIMARY_M_DIMLESS[1]:.6f}) "
          "(dimensionless; M_KK units)")
    assert abs(s_c - 1.0) < 1e-15, f"PV Σc_r identity violated: {s_c}"
    assert abs(s_cm2) < 1e-15, f"PV Σc_r·m_r² identity violated: {s_cm2}"
    print(f"  CC consistency: c_1 + c_2 = {C_1_FW_CC + C_2_FW_CC}  (expected +1) [OK]")
    cc_quad = C_1_FW_CC * (M_1_FW_CC ** 2) + C_2_FW_CC * (M_2_FW_CC ** 2)  # (local)
    print(f"  CC consistency: M_1^2·c_1 + M_2^2·c_2 = {cc_quad:.6e}  (expected 0) ")
    print(f"    relative residual = {abs(cc_quad) / (M_KK ** 2):.6e}")
    assert abs(cc_quad) / (M_KK ** 2) < 1e-15, "CC quadratic PV identity violated"
    print()

    # 3. Seeley-DeWitt closed-form CC coefficients (substitution chain Step 2).
    print("Connes-Chamseddine 1996 §2.2-2.3 Seeley-DeWitt closed forms:")
    a_2_CC = cc_a_n_closed_form(2, M_1_FW_CC, C_1_FW_CC, M_2_FW_CC, C_2_FW_CC)  # (local)
    a_4_CC = cc_a_n_closed_form(4, M_1_FW_CC, C_1_FW_CC, M_2_FW_CC, C_2_FW_CC)  # (local)
    a_4_expected = -2.0 * (M_KK ** 4)                                           # (local)
    print(f"  a_2^{{CC}} = Γ(1)·(c_1·M_1² + c_2·M_2²)                = {a_2_CC:+.6e}")
    print(f"           (expected = 0 by PV cancellation;  |a_2|/M_KK² = {abs(a_2_CC) / (M_KK ** 2):.6e})")
    print(f"  a_4^{{CC}} = Γ(2)·(c_1·M_1⁴ + c_2·M_2⁴)                = {a_4_CC:+.6e}")
    print(f"           (expected = -2·M_KK⁴ = {a_4_expected:+.6e})")
    rel_a4 = abs(a_4_CC - a_4_expected) / abs(a_4_expected)                     # (local)
    print(f"           relative residual = {rel_a4:.6e}")
    assert abs(a_2_CC) / (M_KK ** 2) < 1e-15, \
        f"a_2_CC closed-form failed: {a_2_CC} vs 0 (rel = {abs(a_2_CC) / (M_KK ** 2)})"
    assert rel_a4 < 1e-15, \
        f"a_4_CC closed-form failed: {a_4_CC} vs {a_4_expected} (rel = {rel_a4})"
    print("  Machine-precision identity assertion: PASS")
    print()

    # 4. Load L_max=12 master spectrum cache.
    print(f"Loading L_max={L_MAX} master spectrum cache from "
          f"{L12_CACHE.relative_to(ROOT)}...")
    lambdas, mults, n_sectors = load_spectrum_flat(L12_CACHE)
    print(f"  n_sectors            = {n_sectors}")
    print(f"  n_eigenvalues_raw    = {len(lambdas)}")
    print(f"  Σ_k mults_k          = {int(mults.sum())}  (Peter-Weyl weighted N)")
    print(f"  λ_min                = {lambdas.min():.6f}  (M_KK-natural; spectral gap)")
    print(f"  λ_max                = {lambdas.max():.6f}  (M_KK-natural)")
    print()

    # 5. Compute Hochschild pairing image at substrate-distance-1 pole s=3
    #    under FULL CC physical multipliers.  Pipeline: Mellin moments BARE
    #    vs FULL CC PV at s=3; the regulator-INVARIANT atlas ratio
    #    rho_FULL = M_FULL_CC / M_BARE reads back the §VII.AF.1.OP-PROJ
    #    substrate-IS Hochschild-pairing image under the FULL CC multipliers.
    print(f"Computing Mellin moments at substrate-distance-1 pole s={S_POLE}:")
    M_BARE = bare_mellin_moment(S_POLE, lambdas, mults)                # (local)
    M_FULL_CC = pv_mellin_moment_primary(S_POLE, lambdas, mults)       # (local)
    print(f"  M_BARE(s={S_POLE})       = {M_BARE:.10e}  (zeta/SDW pure spectrum-sum)")
    print(f"  M_FULL_CC(s={S_POLE})    = {M_FULL_CC:.10e}  (PV-regulated CC1996)")

    # PV multiplier sample statistics on the full spectrum.
    lambda_sq = lambdas * lambdas                                       # (local)
    w_PV_arr = pv_multiplier_primary(lambda_sq, S_POLE)                 # (local)
    w_PV_min = float(np.min(w_PV_arr))                                  # (local)
    w_PV_max = float(np.max(w_PV_arr))                                  # (local)
    w_PV_mean = float(np.mean(w_PV_arr))                                # (local)
    print(f"  w_PV(λ², s={S_POLE}) range: [{w_PV_min:.6f}, {w_PV_max:.6f}], "
          f"mean = {w_PV_mean:.6f}")
    print()

    # 6. rho_FULL atlas ratio (regulator-INVARIANT image of Hochschild pairing).
    rho_FULL = M_FULL_CC / M_BARE                                       # (local)
    print(f"rho_FULL = M_FULL_CC(s={S_POLE}) / M_BARE(s={S_POLE}) = {rho_FULL:+.10e}")
    print(f"          (regulator-INVARIANT atlas ratio at L_max={L_MAX})")
    print()

    # 7. Compare against §VII.AF.1.OP-PROJ canonical L_max=10 anchor
    #    R_universal_HP1_strict_F4 = 1.030902 (W-5 V4 SDW residual atlas
    #    ratio; canonical pin per canonical_constants.py).
    R_canonical = R_CANONICAL_AF1                                       # (local)
    print(f"§VII.AF.1.OP-PROJ canonical anchor (from canonical_constants.py):")
    print(f"  R_universal_HP1_strict_F4 = {R_canonical:.6f}  "
          "(W-5 V4 SDW residual; L_max=10 atlas ratio)")
    print(f"  eps_H_HP1_norm            = {eps_H_HP1_norm:.6f}  "
          "(PRIMARY canonical per Class-(d) chain)")
    print(f"  gv_canonical_difference_FW = {GV_CROSS_LINK:+.10e}  "
          "(cross-link to §VII.AQ; NOT §VII.AF.1 canonical)")
    print()

    # 8. Delta_FULL = (rho_FULL - R_canonical) / |R_canonical|.
    delta_full = (rho_FULL - R_canonical) / abs(R_canonical)            # (local)
    print(f"Delta_FULL = (rho_FULL - R_canonical) / |R_canonical| = {delta_full:+.10e}")
    print(f"|Delta_FULL|                                            = {abs(delta_full):.6e}")
    print()

    # 9. Threshold-context substitution chain (per math-scripts.md "Double-
    #    Check Logic Before Compute" for direction claims).
    #
    #    Step 1 (Definition):  Delta_FULL := (rho_FULL - R_canonical) / |R_canonical|
    #    Step 2 (Substitute):  R_canonical = R_universal_HP1_strict_F4 = 1.030902
    #                          rho_FULL    = M_FULL_CC(s=3) / M_BARE(s=3)
    #                                      = computed above on L_max=12 cache
    #    Step 3 (Simplify):    Delta_FULL = (rho_FULL/1.030902 - 1)
    #    Step 4 (Read direction):
    #        PASS  iff  |Delta_FULL| < 1e-3
    #        FAIL  iff  |Delta_FULL| > 1e-2
    #        INFO  iff  1e-3 ≤ |Delta_FULL| ≤ 1e-2
    #    Step 5 (Conclusion):  composite per evaluate_verdict() below.
    print("Threshold context (plan §W9-4 Field 9 RATIO tolerance rule):")
    print(f"  PASS  iff  |Delta_FULL| < {SUB_ENVELOPE_TOL:.0e}      "
          "(sub-envelope first-extraction floor; 0.1% relative)")
    print(f"  INFO  iff  {SUB_ENVELOPE_TOL:.0e} ≤ |Delta_FULL| ≤ {FAIL_TOL:.0e}  "
          "(marginal; envelope refinement at S92+)")
    print(f"  FAIL  iff  |Delta_FULL| > {FAIL_TOL:.0e}      "
          "(SCHEMATIC pin systematically biased; >1% divergence)")
    verdict = evaluate_verdict(delta_full)
    print(f"  Observed: |Delta_FULL| = {abs(delta_full):.6e}  -> "
          f"composite = {verdict['composite']}")
    print()
    print("3-tuple verdict (S87+ schema-v2):")
    print(f"  sign_verdict      = {verdict['sign_verdict']}")
    print(f"  magnitude_verdict = {verdict['magnitude_verdict']}")
    print(f"  regime_verdict    = {verdict['regime_verdict']}")
    if verdict["promote_pass"]:
        print("  Compliance class upgrade: PARTIAL-POSITIVE -> POSITIVE")
    else:
        print("  Compliance class: PARTIAL-POSITIVE (RETAINED; FULL CC upgrade not achieved)")
    print()

    # 10. Cross-pin diagnostic: substrate-distance-2 pole (s=4) to confirm
    #     consistency with W1 T1.1 §VII.AV FULL CC.
    M_BARE_s4 = bare_mellin_moment(4, lambdas, mults)                   # (local)
    M_FULL_s4 = pv_mellin_moment_primary(4, lambdas, mults)             # (local)
    rho_FULL_s4 = M_FULL_s4 / M_BARE_s4                                 # (local)
    print(f"Cross-pin diagnostic (substrate-distance-2 pole s=4):")
    print(f"  M_BARE(s=4)     = {M_BARE_s4:.10e}")
    print(f"  M_FULL_CC(s=4)  = {M_FULL_s4:.10e}")
    print(f"  rho_FULL(s=4)   = {rho_FULL_s4:+.10e}")
    print(f"  (W1 T1.1 §VII.AV FULL CC cross-pin reference)")
    print()

    # 11. Save outputs (.npz + .png).
    print(f"Saving npz to {OUT_NPZ.relative_to(ROOT)}...")
    np.savez(
        OUT_NPZ,
        # Core observables
        M_BARE=M_BARE,
        M_FULL_CC=M_FULL_CC,
        rho_FULL=rho_FULL,
        R_canonical=R_canonical,
        delta_full=delta_full,
        # Seeley-DeWitt CC closed forms
        a_2_CC=a_2_CC,
        a_4_CC=a_4_CC,
        a_4_expected=a_4_expected,
        # Multipliers + PV identities
        M_1_FW_CC=M_1_FW_CC,
        M_2_FW_CC=M_2_FW_CC,
        C_1_FW_CC=C_1_FW_CC,
        C_2_FW_CC=C_2_FW_CC,
        PV_PRIMARY_C=PV_PRIMARY_C,
        PV_PRIMARY_M_DIMLESS=PV_PRIMARY_M_DIMLESS,
        # PV multiplier statistics
        w_PV_arr=w_PV_arr,
        w_PV_min=w_PV_min,
        w_PV_max=w_PV_max,
        w_PV_mean=w_PV_mean,
        # Pinned plan parameters
        S_POLE=S_POLE,
        L_max=L_MAX,
        n_sectors=n_sectors,
        n_eigenvalues=len(lambdas),
        SUB_ENVELOPE_TOL=SUB_ENVELOPE_TOL,
        FAIL_TOL=FAIL_TOL,
        # Cross-pin diagnostic
        M_BARE_s4=M_BARE_s4,
        M_FULL_s4=M_FULL_s4,
        rho_FULL_s4=rho_FULL_s4,
        # Cross-link references
        eps_H_HP1_norm=eps_H_HP1_norm,
        gv_canonical_difference_FW=GV_CROSS_LINK,
        # Spectrum (for reproducibility)
        lambdas=lambdas,
        mults=mults,
        # Verdict
        verdict_composite=verdict["composite"],
        verdict_sign=verdict["sign_verdict"],
        verdict_magnitude=verdict["magnitude_verdict"],
        verdict_regime=verdict["regime_verdict"],
        promote_pass=verdict["promote_pass"],
        # Dual SHA
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"Saving plot to {OUT_PNG.relative_to(ROOT)}...")
    make_plot(
        M_BARE, M_FULL_CC, rho_FULL, R_canonical, delta_full,
        a_2_CC, a_4_CC, w_PV_min, w_PV_mean, w_PV_max,
    )
    print()

    # 12. Emit verdict line.
    value_str = (
        f"Delta_FULL={delta_full:+.6e}"
        f"_rho_FULL={rho_FULL:+.6e}"
        f"_R_canonical_AF1={R_canonical:.6f}"
        f"_M_BARE_s3={M_BARE:.4e}"
        f"_M_FULL_CC_s3={M_FULL_CC:.4e}"
        f"_a_2_CC=0.0_a_4_CC=-2_M_KK_4"
        f"_compliance_transition={'PARTIAL-POSITIVE->POSITIVE' if verdict['promote_pass'] else 'PARTIAL-POSITIVE-RETAINED'}"
    )
    append_verdict(
        composite=verdict["composite"],
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=verdict["sign_verdict"],
        mag_v=verdict["magnitude_verdict"],
        reg_v=verdict["regime_verdict"],
        promote_pass=verdict["promote_pass"],
    )

    # 13. Final summary.
    wall = time.time() - t0                                             # (local)
    print(f"=== {GATE_ID}: {verdict['composite']} (wall {wall:.1f}s) ===")
    print(f"    value:          {value_str}")
    print(f"    audit_sha256:   {audit_sha}")
    print(f"    content_sha256: {content_sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
