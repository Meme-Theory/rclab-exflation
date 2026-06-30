"""
S92 W2-3 — S92-W2-CF-W9-9-1-WODZICKI-F-FUNCTOR-M-KK-5-NORMALIZATION
====================================================================

Gate: S92-W2-CF-W9-9-1-WODZICKI-F-FUNCTOR-M-KK-5-NORMALIZATION  ([SIGN])
Class: GEOMETRIC
Agent: connes-ncg-theorist
Convention: VII-BA-Wodzicki-BCS-Level-3-anchor-with-F-functor-M_KK_5-normalization-FULL-physical
Scheme: wodzicki-residue-F-functor-image-normalization-M_KK-5-dimensional-derivation-substrate-natural
L_max: 12 (S84 master cache anchor)
CLASS: FULL physical per substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY
  — NO SCHEMATIC helpers consumed; NO `-SCHEMATIC` convention suffix; NO `tier_pin=TIER-2`.

Hypothesis (PASS): post-normalization Level-3 ratio
    |N · Res_W(L_max=12) − Δ_BCS_canonical| / |Δ_BCS_canonical|  ≤  1e-1
with N = M_KK^5 derived analytically from substrate-natural dimensional analysis
on Ψ(A_K) per Connes 1995 §III.4 (Wodzicki residue uniqueness on finite spectral
triples; dimensional sum rule [N] · [M_KK^{-4}] = [M_KK^1] ⇒ [N] = [M_KK^5]).

Hypothesis (FAIL alternatives per plan FAIL_meaning):
  (a) F-functor image identification structurally incomplete (more than a
      single scalar multiplicative rescaling required);
  (b) Δ_BCS canonical pin dimensional class mis-tagged (audit-side mismatch);
  (c) master cache eigenvalue computation contains subtle numerical bias at
      order [M_KK^{-4}] that does not cancel under M_KK^5 rescaling.

Substrate framing per plan §13 + phononic-framing.md §"IS Space, Not IN Space":
the substrate IS the pseudodifferential operator algebra Ψ(A_K) over A_K =
ℂ ⊕ ℍ ⊕ M_3(ℂ); the Wodzicki residue Res_W IS the unique (up to scalar) NC trace
on Ψ^{-∞}(A_K)/trace-class per Wodzicki 1984 uniqueness. The dimensional class
[M_KK^{-4}] for Res_W(D_K^{-4}) IS substrate-IS at the substrate-distance-1 pole
image s=2; the dimensional class [M_KK^1] for Δ_BCS IS substrate-IS per S70
BCS-GAP-CANONICAL-70. FORBIDDEN inversion: "we choose N = M_KK^5 by hand."
INVERT: "the dimensional class of Res_W(D_K^{-4}) IS [M_KK^{-4}] by substrate-IS
Connes 1995 §III.4; the F-functor normalization exponent IS 1 − (−4) = 5 by
substrate-IS dimensional sum rule."

Substitution chain (Definitions 1-3) reproduced in WP §W2-3 Results section per
math-scripts.md §"Double-Check Logic Before Compute". This is a [SIGN] trigger
gate; 3-tuple companion row is MANDATORY per gate-verdicts.md §"S87+ canonical
form".

Verdict honesty discipline (math-scripts.md §"All Results Are Good Results"):
PASS, FAIL, INFO are all results. The pre-registered DIRECTION prediction (Step 4
of substitution chain) is that the ratio falls in [0, 1e-1] PASS-band after
M_KK^5 rescaling. The numerical reality (eigenvalues stored in M_KK=1 internal
units, dimensional rescaling is a unit change that cancels in the ratio) is
what is computed and emitted. NO convention-shopping; NO iterate-until-PASS.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

# Per math-scripts.md §"Canonical Constants (MANDATORY)"
PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))  # (local)
from canonical_constants import Delta_BCS, M_KK, M_KK_gravity  # noqa: E402

# ----------------------------------------------------------------------------
# File pins
# ----------------------------------------------------------------------------
CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CC_PATH = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S91_VERDICTS_PATH = PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
VERDICT_FILE = PROJECT_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"

SCRIPT_PATH = Path(__file__).resolve()
DATA_OUT = SCRIPT_PATH.with_suffix(".npz")
PLOT_OUT = SCRIPT_PATH.with_suffix(".png")

GATE_ID = "S92-W2-CF-W9-9-1-WODZICKI-F-FUNCTOR-M-KK-5-NORMALIZATION"
SCHEME = (
    "wodzicki-residue-F-functor-image-normalization-M_KK-5-"
    "dimensional-derivation-substrate-natural"
)
CONVENTION = (
    "VII-BA-Wodzicki-BCS-Level-3-anchor-with-F-functor-M_KK_5-normalization-"
    "FULL-physical"
)
L_MAX = 12  # (local; S84 master cache anchor per plan §W2-3)

# Plan-pinned anchor from S91 W1-14 verdict line 212 (audit_sha256=fe8e0a65...)
RES_W_L12_ANCHOR_S91 = 1.7498119758e+05  # (local; cross-check anchor)
XI_W_S2 = 1.0  # (local; Γ(2)=1 canonical NC-trace normalization at s=2)

# Pre-registered PASS/INFO/FAIL bands per plan §W2-3 strict_PASS_boundary
PASS_BAND = 1e-1  # (local; plan §W2-3 strict_PASS_boundary)
INFO_BAND = 5e-1  # (local; plan §W2-3 INFO band upper bound)

# Pre-registered SIGN-trigger direction prediction per plan §W2-3 substitution
# chain Direction step: "AFTER normalization the Level-3 ratio falls within the
# [0, 1e-1] PASS-band" — the SIGN prediction is that the M_KK^5 rescaling
# closes the gap to within PASS_BAND.
PRE_REGISTERED_DIRECTION = "ratio_post_normalization_in_[0,PASS_BAND]"


# ----------------------------------------------------------------------------
# SHA + closure helpers (canonical per s91 append_verdict template)
# ----------------------------------------------------------------------------
def file_sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Audit-SHA closure over the input-pin map (ordered, |-separated)."""
    items = [f"{k}:{v}" for k, v in sorted(pin_map.items())]
    return hashlib.sha256("|".join(items).encode()).hexdigest()


def append_verdict(
    gate_id: str,
    verdict: str,
    value: str,
    scheme: str,
    convention: str,
    L_max: int,
    audit_sha: str,
    content_sha: str,
    sign_v: str,
    mag_v: str,
    regime_v: str,
) -> None:
    """Atomic O_APPEND of 3-line verdict block (canonical + dual-SHA + 3-tuple)
    per gate-verdicts.md §"S87+ canonical form" — [SIGN] trigger MANDATES the
    3-tuple companion row.
    """
    canonical = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} "
        f"L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )
    block = canonical + dual_sha_row + three_tuple_row
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(block)
    print(f"APPENDED: {gate_id}")
    print(f"  audit={audit_sha[:16]} content={content_sha[:16]}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")


# ----------------------------------------------------------------------------
# Substrate-IS computation: Wodzicki residue + F-functor M_KK^5 normalization
# ----------------------------------------------------------------------------
def compute_wodzicki_residue_at_L12() -> tuple[float, dict]:
    """Re-evaluate Res_W(D_K^{-2s})|_{s=2} on the L_max=12 master cache.

    Substrate-IS observable: Res_W(D_K^{-2s})|_{s=2} = Σ_α m_α · |λ_α|^{-4} · ξ_W(s=2)
    with ξ_W(s=2) = Γ(2) = 1.

    The cache stores Peter-Weyl sector eigenvalues keyed by (p, q) with per-sector
    'dim' (multiplicity) and 'abs_evals' (eigenvalue magnitudes). Per-(p,q) sector
    the contribution to Tr(|D_K|^{-4}) is dim · Σ_i |λ_α,i|^{-4}.

    The eigenvalues are stored in M_KK=1 internal units (Kerner-Dirac operator on
    Jensen-deformed SU(3) at τ_fold = 0.19). Res_W is dimensionally [M_KK^{-4}]
    but numerically reported as a pure number in M_KK=1 units.
    """
    cache = np.load(CACHE_PATH, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()

    total_contribution = 0.0  # (local)
    total_evcount = 0  # (local)
    sectors_used_count = 0  # (local)
    abs_min = np.inf  # (local)
    abs_max = -np.inf  # (local)

    for (p, q), payload in sector_evals.items():
        dim = int(payload["dim"])  # (local; Peter-Weyl multiplicity factor)
        evals = np.asarray(payload["abs_evals"], dtype=np.float64)  # (local)
        if evals.size == 0:
            continue
        contribution_per_sector = dim * np.sum(evals ** (-4.0))  # (local)
        total_contribution += contribution_per_sector
        total_evcount += evals.size
        sectors_used_count += 1
        if evals.min() < abs_min:
            abs_min = float(evals.min())
        if evals.max() > abs_max:
            abs_max = float(evals.max())

    res_W_L12 = total_contribution * XI_W_S2  # (local)
    metadata = {
        "xi_W_s2": XI_W_S2,
        "sectors_used_count": sectors_used_count,
        "total_evcount": total_evcount,
        "abs_min": abs_min,
        "abs_max": abs_max,
    }
    return float(res_W_L12), metadata


def derive_F_functor_normalization() -> dict:
    """Derive N = M_KK^5 from substrate-natural dimensional analysis on Ψ(A_K)
    per Connes 1995 §III.4 (Wodzicki residue uniqueness + dimensional sum rule).

    Substitution chain (substrate-IS, no free parameters):
      Definition 1: [Res_W(D_K^{-4})] = [M_KK^{-4}]  (Connes 1995 §III.4 Prop 3;
                    D_K has [M_KK^1] in framework convention; D_K^{-4} has
                    [M_KK^{-4}]; Wodzicki residue inherits the order-(-n) symbol
                    class dimension).
      Definition 2: [Δ_BCS] = [M_KK^1]  (canonical_constants.py:387; R-PROTECTED
                    S70 BCS-GAP-CANONICAL-70).
      Definition 3: [N] · [M_KK^{-4}] = [M_KK^1]  (F-functor image-normalization
                    predicate: N · Res_W and Δ_BCS units-commensurate).
      Substitute:   [N] = [M_KK^{1 - (-4)}] = [M_KK^5].
      Simplify:     N = M_KK^5 (exact integer exponent; no free parameter).
      Direction:    M_KK > 0; M_KK^5 > 0; ∂N/∂M_KK = 5 · M_KK^4 > 0; SIGN-trigger
                    direction prediction = "post-normalization ratio in [0, 1e-1]"
                    per plan substitution chain.
      Conclusion:   The dimensional exponent IS 5 by substrate-IS Connes 1995
                    §III.4 dimensional sum rule (structural-theorem level).
    """
    # Definition 1: dimensional class of Res_W(D_K^{-4})
    dim_exponent_D_K = 1  # (local; D_K carries [M_KK^1])
    dim_exponent_D_K_inv4 = -4 * dim_exponent_D_K  # (local; D_K^{-4} carries [M_KK^{-4}])
    dim_class_Res_W = dim_exponent_D_K_inv4  # (local; Res_W inherits order-(-n) symbol class)

    # Definition 2: dimensional class of Δ_BCS
    dim_class_Delta_BCS = 1  # (local; canonical_constants.py:387; R-PROTECTED)

    # Definition 3 + substitute: F-functor image-normalization predicate
    # [N] · [M_KK^{dim_class_Res_W}] = [M_KK^{dim_class_Delta_BCS}]
    # ⇒ [N] = [M_KK^{dim_class_Delta_BCS - dim_class_Res_W}]
    F_functor_dim_exponent = dim_class_Delta_BCS - dim_class_Res_W  # 1 - (-4) = 5

    assert F_functor_dim_exponent == 5, (
        f"Dimensional sum rule failed: 1 - (-4) = {F_functor_dim_exponent}, "
        f"expected 5 by Connes 1995 §III.4"
    )

    # Numerical N in two reading conventions
    # Reading I (substrate-natural internal units, M_KK=1): N = 1
    N_internal = 1.0 ** F_functor_dim_exponent  # = 1.0 in M_KK=1 units
    # Reading II (lab units, M_KK = 7.43e16 GeV): N = M_KK^5
    N_lab = float(M_KK) ** F_functor_dim_exponent

    return {
        "dim_class_D_K": dim_exponent_D_K,
        "dim_class_D_K_inv4": dim_exponent_D_K_inv4,
        "dim_class_Res_W": dim_class_Res_W,
        "dim_class_Delta_BCS": dim_class_Delta_BCS,
        "F_functor_dim_exponent": F_functor_dim_exponent,  # 5
        "N_internal_M_KK_eq_1_units": N_internal,
        "N_lab_units_GeV5": N_lab,
        "provenance": (
            "Connes 1995 §III.4 Proposition 3 dimensional formula on finite "
            "spectral triples; D_K has [M_KK^1] in canonical_constants.py "
            "convention (M_KK = M_KK_gravity = 7.428660036284456e+16 GeV); "
            "Δ_BCS has [M_KK^1] per canonical_constants.py:387 S70 "
            "BCS-GAP-CANONICAL-70 R-PROTECTED pin (0.4642547394830737 M_KK)."
        ),
    }


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"[{datetime.now(timezone.utc).isoformat()}] START {GATE_ID}")
    print()

    # --- Step 0: log input SHAs per math-scripts.md (first 20 lines stdout) ---
    cc_sha = file_sha(CC_PATH)
    cache_sha = file_sha(CACHE_PATH)
    registry_sha = file_sha(REGISTRY_PATH)
    s91_sha = file_sha(S91_VERDICTS_PATH)

    print("Input SHA-256 pins:")
    print(f"  canonical_constants.py        = {cc_sha}")
    print(f"  s84_spectrum_cache_L12        = {cache_sha}")
    print(f"  permanent-results-registry.md = {registry_sha}")
    print(f"  s91_gate_verdicts.txt         = {s91_sha}")
    print()

    # SHA cross-check against plan-pinned values (math-scripts.md double-check)
    PLAN_PIN_CC = "9cafdc97bcafa5fea99742b5aecc822d907b38f56a4ab5057ba03fbf12c0f1ca"
    PLAN_PIN_CACHE = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
    assert cc_sha == PLAN_PIN_CC, f"canonical_constants SHA drift: {cc_sha} vs {PLAN_PIN_CC}"
    assert cache_sha == PLAN_PIN_CACHE, f"master cache SHA drift: {cache_sha} vs {PLAN_PIN_CACHE}"
    print(f"SHA pin verification: PASS (canonical_constants + master cache match plan pins)")
    print()

    # --- Step 1: Substrate-IS Wodzicki residue at L_max=12 -------------------
    print("Step 1: Compute Res_W(D_K^{-2s})|_{s=2} on L_max=12 master cache")
    res_W_L12, residue_md = compute_wodzicki_residue_at_L12()
    print(f"  Res_W(L_max=12) = {res_W_L12:.10e}  [M_KK^{{-4}}; numerically pure number in M_KK=1 units]")
    print(f"  sectors_used    = {residue_md['sectors_used_count']}")
    print(f"  total_evcount   = {residue_md['total_evcount']}")
    print(f"  |λ| range       = [{residue_md['abs_min']:.6e}, {residue_md['abs_max']:.6e}]")
    print()

    # Cross-check against S91 W1-14 anchor
    res_W_anchor_drift = abs(res_W_L12 - RES_W_L12_ANCHOR_S91) / abs(RES_W_L12_ANCHOR_S91)
    print(f"  S91 W1-14 anchor cross-check: {RES_W_L12_ANCHOR_S91:.10e}")
    print(f"  relative drift = {res_W_anchor_drift:.6e}")
    assert res_W_anchor_drift < 1e-6, f"Res_W drift from S91 anchor: {res_W_anchor_drift}"
    print(f"  Anchor cross-check: PASS (drift < 1e-6)")
    print()

    # --- Step 2: Derive N = M_KK^5 from dimensional analysis -----------------
    print("Step 2: Derive F-functor image-normalization N from substrate-natural")
    print("        dimensional analysis on Ψ(A_K) per Connes 1995 §III.4")
    norm = derive_F_functor_normalization()
    print(f"  [D_K]            = [M_KK^{norm['dim_class_D_K']}]")
    print(f"  [D_K^(-4)]       = [M_KK^{norm['dim_class_D_K_inv4']}]")
    print(f"  [Res_W(D_K^-4)]  = [M_KK^{norm['dim_class_Res_W']}]")
    print(f"  [Δ_BCS]          = [M_KK^{norm['dim_class_Delta_BCS']}]")
    print(f"  [N] = [Δ_BCS] / [Res_W] = [M_KK^{{{norm['dim_class_Delta_BCS']} - ({norm['dim_class_Res_W']})}}] = [M_KK^{norm['F_functor_dim_exponent']}]")
    print(f"  ⇒ N = M_KK^5 (exact integer exponent; structural per Connes 1995 §III.4)")
    print()
    print(f"  N_internal (M_KK=1 units)  = {norm['N_internal_M_KK_eq_1_units']:.10e}  (dimensionless 1.0)")
    print(f"  N_lab      (M_KK ≈ 7.43e16 GeV) = {norm['N_lab_units_GeV5']:.10e}  GeV^5")
    print()

    # --- Step 3: Evaluate post-normalization Level-3 ratio -------------------
    # The substrate-natural reading: eigenvalues stored in M_KK=1 internal units
    # → Res_W is a pure number 1.7498e+05 → N (which is 1.0^5 = 1.0 in internal
    # units) leaves the ratio unchanged. The dimensional rescaling N = M_KK^5
    # is a UNIT CHANGE, not a numerical correction:
    #   Lab units: Res_W^lab = M_KK^{-4} · Res_W^internal
    #              Δ_BCS^lab = M_KK^1     · Δ_BCS^internal
    #              N · Res_W^lab − Δ_BCS^lab = M_KK · (Res_W^internal − Δ_BCS^internal)
    #              ratio_lab = M_KK · |Res_W^int − Δ_BCS^int| / (M_KK · |Δ_BCS^int|)
    #                        = |Res_W^int − Δ_BCS^int| / |Δ_BCS^int|  (M_KK cancels)
    # Hence the post-normalization Level-3 ratio is INVARIANT under the M_KK^5
    # rescaling: it is the SAME 5-OOM gap S91 W1-14 reported.
    print("Step 3: Evaluate post-normalization Level-3 ratio")
    print(f"  Δ_BCS_canonical = {float(Delta_BCS):.16e}  [M_KK^1; R-PROTECTED S70]")

    # Pre-normalization (S91 W1-14 reference state)
    delta_emp_pre = abs(res_W_L12 - float(Delta_BCS))  # (local)
    ratio_pre = delta_emp_pre / abs(float(Delta_BCS))  # (local)
    print(f"  PRE-normalization  |Res_W − Δ_BCS|        = {delta_emp_pre:.10e}")
    print(f"  PRE-normalization  ratio_pre              = {ratio_pre:.10e}")
    print()

    # Post-normalization (internal units; N=1.0; ratio identical)
    N_internal = norm["N_internal_M_KK_eq_1_units"]
    N_Res_W_internal = N_internal * res_W_L12  # (local)
    delta_emp_post = abs(N_Res_W_internal - float(Delta_BCS))  # (local)
    ratio_post = delta_emp_post / abs(float(Delta_BCS))  # (local)
    print(f"  POST-normalization (M_KK=1 internal units; N_internal = 1.0^5 = 1.0):")
    print(f"    N · Res_W                = {N_Res_W_internal:.10e}")
    print(f"    |N·Res_W − Δ_BCS|        = {delta_emp_post:.10e}")
    print(f"    level_3_ratio_post_norm  = {ratio_post:.10e}")
    print()

    # Explicit cross-check in lab units (M_KK ≈ 7.43e16 GeV)
    M_KK_val = float(M_KK)
    Res_W_lab = (M_KK_val ** -4) * res_W_L12  # GeV^{-4}
    Delta_BCS_lab = M_KK_val * float(Delta_BCS)  # GeV
    N_Res_W_lab = (M_KK_val ** 5) * Res_W_lab  # = M_KK · Res_W_internal in GeV
    delta_emp_post_lab = abs(N_Res_W_lab - Delta_BCS_lab)
    ratio_post_lab = delta_emp_post_lab / abs(Delta_BCS_lab)
    print(f"  POST-normalization (lab units; M_KK = {M_KK_val:.6e} GeV):")
    print(f"    Res_W^lab               = {Res_W_lab:.10e}  GeV^{{-4}}")
    print(f"    Δ_BCS^lab               = {Delta_BCS_lab:.10e}  GeV")
    print(f"    N · Res_W^lab           = {N_Res_W_lab:.10e}  GeV")
    print(f"    |N·Res_W^lab − Δ_BCS^lab| = {delta_emp_post_lab:.10e}  GeV")
    print(f"    level_3_ratio (lab)     = {ratio_post_lab:.10e}")
    print(f"    [M_KK cancels in lab ratio → identical to internal-units ratio]")
    print()

    # Sanity: internal-units ratio and lab-units ratio agree to float64 precision
    ratio_agreement = abs(ratio_post - ratio_post_lab) / abs(ratio_post)
    print(f"  Cross-units sanity: |ratio_internal − ratio_lab| / ratio = {ratio_agreement:.6e}")
    print(f"  (M_KK^5 · M_KK^{{-4}} = M_KK^1 cancels with Δ_BCS's M_KK^1 in ratio)")
    print()

    # --- Step 4: Pre-registered band classification --------------------------
    print("Step 4: Pre-registered band classification per plan §W2-3")
    print(f"  PASS_BAND  = {PASS_BAND}")
    print(f"  INFO_BAND  = ({PASS_BAND}, {INFO_BAND}]")
    print(f"  FAIL_BAND  = > {INFO_BAND}")
    print(f"  level_3_ratio_post_norm = {ratio_post:.10e}")

    if ratio_post <= PASS_BAND:
        magnitude_verdict = "PASS"
    elif ratio_post <= INFO_BAND:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"

    # Sign verdict: SIGN-trigger direction predicted ratio ∈ [0, PASS_BAND] post-norm
    # Direction matches iff ratio_post ≤ PASS_BAND
    if ratio_post <= PASS_BAND:
        sign_verdict = "PASS"
    else:
        sign_verdict = "FAIL"

    # Regime verdict: dimensional-analysis regime is well-defined throughout
    # (no auto-shortening clause; integer exponent; analytic substitution chain)
    regime_verdict = "VALID"

    # Composite collapse rule per gate-verdicts.md §"S87+ canonical form"
    if regime_verdict == "BREAKDOWN":
        composite_verdict = "FAIL"
    elif sign_verdict == "FAIL":
        composite_verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite_verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite_verdict = "INFO"
    elif magnitude_verdict == "INFO":
        composite_verdict = "INFO"
    else:
        composite_verdict = "PASS"

    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  sign_verdict      = {sign_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")
    print(f"  composite_verdict = {composite_verdict}  (per gate-verdicts.md collapse rule)")
    print()

    # --- Step 5: Save data + plot --------------------------------------------
    print("Step 5: Save artifacts (npz + png)")
    np.savez(
        DATA_OUT,
        N_F_functor_dim_exponent=norm["F_functor_dim_exponent"],
        N_internal_M_KK_eq_1=N_internal,
        N_lab_GeV5=norm["N_lab_units_GeV5"],
        Res_W_L12=res_W_L12,
        Res_W_L12_anchor_S91=RES_W_L12_ANCHOR_S91,
        Res_W_anchor_drift=res_W_anchor_drift,
        Delta_BCS_canonical=float(Delta_BCS),
        N_Res_W_internal=N_Res_W_internal,
        Res_W_lab_GeV_minus_4=Res_W_lab,
        Delta_BCS_lab_GeV=Delta_BCS_lab,
        N_Res_W_lab_GeV=N_Res_W_lab,
        delta_emp_pre=delta_emp_pre,
        delta_emp_post_internal=delta_emp_post,
        delta_emp_post_lab=delta_emp_post_lab,
        ratio_pre=ratio_pre,
        ratio_post_internal=ratio_post,
        ratio_post_lab=ratio_post_lab,
        PASS_BAND=PASS_BAND,
        INFO_BAND=INFO_BAND,
        M_KK_value_GeV=M_KK_val,
        magnitude_verdict=magnitude_verdict,
        sign_verdict=sign_verdict,
        regime_verdict=regime_verdict,
        composite_verdict=composite_verdict,
        sectors_used_count=residue_md["sectors_used_count"],
        total_evcount=residue_md["total_evcount"],
        abs_lambda_min=residue_md["abs_min"],
        abs_lambda_max=residue_md["abs_max"],
        dimensional_derivation_provenance=norm["provenance"],
    )
    print(f"  Saved: {DATA_OUT.name}")

    # --- Bar plot: pre vs post Level-3 ratio + PASS-band line ----------------
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 6))
    labels = ["Pre-normalization\n(S91 W1-14)", "Post-normalization\n(N = M_KK^5, internal)", "Post-normalization\n(N = M_KK^5, lab units)"]
    values = [ratio_pre, ratio_post, ratio_post_lab]
    colors = ["#cc4444", "#cc8844", "#8844cc"]
    bars = ax.bar(labels, values, color=colors, alpha=0.78, edgecolor="black", linewidth=0.7)
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.06, f"{v:.3e}",
                ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax.axhline(PASS_BAND, color="green", linestyle="--", linewidth=1.6,
               label=f"PASS band ≤ {PASS_BAND}")
    ax.axhline(INFO_BAND, color="orange", linestyle="--", linewidth=1.0,
               label=f"INFO band ≤ {INFO_BAND}")
    ax.set_yscale("log")
    ax.set_ylim(1e-2, max(values) * 8)
    ax.set_ylabel("Level-3 ratio  |N · Res_W − Δ_BCS| / |Δ_BCS|", fontsize=10)
    ax.set_title(
        f"S92 W2-3: Wodzicki F-functor M_KK^5 normalization at L_max=12\n"
        f"§VII.BA Level-3 anchor — composite verdict = {composite_verdict}\n"
        f"(M_KK^5 cancels in ratio: dimensional rescaling is unit change, not numerical correction)",
        fontsize=10,
    )
    ax.legend(fontsize=9, loc="center right")
    ax.grid(axis="y", linestyle="-", alpha=0.18)
    ax.text(0.01, 0.98,
            f"N = M_KK^5 derived from Connes 1995 §III.4\n"
            f"[N] = [Δ_BCS]/[Res_W] = [M_KK^1]/[M_KK^{{-4}}] = [M_KK^5]\n"
            f"sign_verdict={sign_verdict}, magnitude_verdict={magnitude_verdict}, regime_verdict={regime_verdict}",
            transform=ax.transAxes, fontsize=8, va="top", ha="left",
            bbox=dict(facecolor="white", alpha=0.85, edgecolor="gray"))
    plt.tight_layout()
    plt.savefig(PLOT_OUT, dpi=140)
    plt.close()
    print(f"  Saved: {PLOT_OUT.name}")
    print()

    # --- Step 6: Compute audit + content SHAs and append verdict --------------
    content_sha = file_sha(SCRIPT_PATH)  # content SHA = script itself per template
    data_sha = file_sha(DATA_OUT)

    pin_map = {
        "gate_id": GATE_ID,
        "L_max": L_MAX,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "cache_sha256": cache_sha,
        "canonical_constants_sha256": cc_sha,
        "registry_sha256": registry_sha,
        "s91_verdicts_sha256": s91_sha,
        "script_sha256": content_sha,
        "data_sha256": data_sha,
        "F_functor_dim_exponent": norm["F_functor_dim_exponent"],
        "Res_W_L12": f"{res_W_L12:.10e}",
        "Delta_BCS": f"{float(Delta_BCS):.16e}",
        "ratio_post_internal": f"{ratio_post:.10e}",
        "ratio_post_lab": f"{ratio_post_lab:.10e}",
        "pass_band": PASS_BAND,
        "info_band": INFO_BAND,
        "pre_registered_direction": PRE_REGISTERED_DIRECTION,
        "magnitude_verdict": magnitude_verdict,
        "sign_verdict": sign_verdict,
        "regime_verdict": regime_verdict,
        "composite_verdict": composite_verdict,
    }
    audit_sha = closure_hash(pin_map)

    value_str = (
        f"N=M_KK**5_exponent=5;"
        f"Res_W_L12={res_W_L12:.10e};"
        f"Res_W_anchor_drift={res_W_anchor_drift:.3e};"
        f"Delta_BCS={float(Delta_BCS):.10e};"
        f"N_internal=1.0;"
        f"N_lab={norm['N_lab_units_GeV5']:.6e}_GeV5;"
        f"ratio_pre={ratio_pre:.6e};"
        f"ratio_post_internal={ratio_post:.6e};"
        f"ratio_post_lab={ratio_post_lab:.6e};"
        f"PASS_band={PASS_BAND};"
        f"INFO_band_upper={INFO_BAND};"
        f"M_KK_cancels_in_ratio=TRUE;"
        f"dimensional_rescaling_is_unit_change_not_numerical_correction=TRUE;"
        f"structural_diagnostic=F-functor_image_identification_structurally_incomplete_more_than_scalar_rescaling_required;"
        f"FAIL_pathway_per_plan=a_F_functor_image_NOT_single_scalar_multiplicative_rescaling"
    )

    print(f"4-tuple output:")
    print(f"  (value={ratio_post:.6e}, scheme={SCHEME},")
    print(f"   convention={CONVENTION}, L_max={L_MAX})")
    print()
    print(f"Closure hashes:")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print()

    append_verdict(
        gate_id=GATE_ID,
        verdict=composite_verdict,
        value=value_str,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=sign_verdict,
        mag_v=magnitude_verdict,
        regime_v=regime_verdict,
    )

    t1 = time.time()  # (local)
    print()
    print(f"[{datetime.now(timezone.utc).isoformat()}] DONE {GATE_ID} in {t1 - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
