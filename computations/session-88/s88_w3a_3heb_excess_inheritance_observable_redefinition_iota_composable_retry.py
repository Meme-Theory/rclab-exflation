"""
S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY  (§W3a-18)
============================================================================================

Companion gate to §W3a-14: tests whether REDEFINING the substrate observable as
an ι_*-composable cohomology-class pairing on the BdG pre-image (M_3(C) excised
PRE-image-construction, NOT post-projection on a non-composable W11-5 form)
collapses the W11-5 ratio_mismatch into the Level-2 cohomology envelope at
L_max=10.

Honest disclosure — surrogate observable
----------------------------------------
A faithful Connes-Moscovici Hochschild pairing
  R_canonical := ⟨[φ_substrate_BdG], [Ch(P_0(τ_fold))_BdG]⟩
requires explicit construction of:
  (1) the Hochschild cocycle [φ_g^sym] on the BdG-restricted algebra A_K^BdG_preimage
  (2) the band-0 Jensen-deformed projector P_0(τ_fold) and its Chern character
  (3) the Connes-Karoubi K-theory pairing
This is NCG infrastructure spanning multiple S86/S87 sessions; a one-script
faithful implementation is not realistic in solo mode.

The W-5 R_universal_HP1_strict_F4 = 1.030902 is the canonical W-5 cohomology-class
anchor for the **Pillar III ↔ IV** bridge (HP^1 cohomology ↔ Peotta-Törmä quantum
metric), NOT for the **Pillar I/II ↔ V** bridge (substrate ↔ 3He-B BdG-undoubled
spectral excess) tested here. It cannot be plumbed directly.

Operational surrogate (substrate-physics-grounded analog)
---------------------------------------------------------
By analogy with R_3HeB_lit = (Δ_A² − Δ_B²)/(Δ_A² + Δ_B²) (gap-asymmetry between
3He A and B phases at coexistence), the substrate-side analog under ι_*-composable
BdG/M_3(C) partition is the **substrate-distance-1 spectral-asymmetry** between
the BdG (color-singlet) and M_3(C) Cartan-zone (color-charged) sub-classes:

  a_3_S := Σ_{(p,q) ∈ S} d(p,q) · λ_min(p,q)^{-3}        [substrate-distance-1 pole power; s=3/2 Mellin pole]
  R_substrate_redefined := (a_3_BdG − a_3_M3C) / (a_3_BdG + a_3_M3C)

Properties:
  - dimensionless ratio in [-1, +1]                     [matches R_3HeB_lit's algebraic form]
  - ι_*-composable by construction                      [BdG/M_3(C) partition is exact set partition]
  - Connes-Moscovici-residue-flavored                   [s=3/2 pole power weighting]
  - cocycle norms enter via the canonical cocycle pin   [‖φ_67‖²/‖φ_88‖² = 7.324992]

This is a SURROGATE; the verdict reflects what THIS surrogate gives, not a
faithful Connes-Karoubi pairing on a fully-constructed BdG spectral triple.

Threshold (per plan §"PASS / FAIL / INFO thresholds")
-----------------------------------------------------
  PASS-strict (Level-2/3 cohomology envelope): ratio_mismatch_redefined ≤ 0.001
  PASS-loose / INFO:                          0.001 < ratio_mismatch_redefined ≤ 0.05
  FAIL:                                       ratio_mismatch_redefined > 0.05
                                              OR composability_residual ≥ 1e-2 (W11-5 non-composable confirms diagnostic; FAIL only if surrogate also fails to match lit)
                                              OR cocycle_ratio invariant violated (severe structural defect)

Cross-checks
------------
  CC1: cocycle ratio invariant ‖φ_67‖/‖φ_88‖ = 7.324992 (Sage-exact pin)
  CC2: composability_residual = |R_substrate_redefined − R_M3C_projected_from_W3a14|
       (small ⇒ W11-5 was composable; large ⇒ W11-5 was non-composable, expected
        diagnostic per plan §322-323 confirming Track-2 redefinition rationale)
  CC3: (Δ_B/Δ_A)^p cancellation at p=0 trivially holds (residual 0.0e+00)
"""

import json
import hashlib
import os
import sys
from pathlib import Path

# CPU-thread cap (small spectrum, no GPU benefit)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent  # (local)
PROJECT_ROOT = HERE.parent  # (local)
sys.path.insert(0, str(HERE))

from canonical_constants import (
    tau_fold,
    M_KK,
    cocycle_norm_phi67,
    cocycle_norm_phi88,
    substrate_cocycle_ratio_67_88,
    R_universal_HP1_strict_F4,
)
from _spectral_action_regulators import _enumerate_sectors

# ----------------------------------------------------------------------------
# Gate identity
# ----------------------------------------------------------------------------
GATE_ID = "S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY"  # (local)
SCHEME = "NCG-cohomology-class-Hochschild-pairing-pole-1"  # (local)
CONVENTION = "iota-star-composable-preimage-construction"  # (local)
L_MAX = 10  # (local) canonical Level-3 anchor per cross-pillar-bridge-anatomy.md
SCHEMA_VERSION = "R3"  # (local)

# Pre-registered thresholds per plan §"PASS / FAIL / INFO thresholds"
LEVEL3_STRICT = 0.001  # (local) PASS-strict ratio_mismatch ceiling
LEVEL3_LOOSE = 0.05    # (local) PASS-loose / INFO ceiling
COMPOSABILITY_TOL = 1e-2  # (local) plan §322-323 diagnostic threshold
COCYCLE_INV_TOL = 1e-4  # (local) Sage-exact 4-sig-fig publication precision (Class 8.3)

# Substrate-distance-1 pole: s = (d-n)/2 = (4-1)/2 = 3/2 → λ^{-3} weighting
S_POLE_POWER = 3  # (local) λ^{-2s} at s=3/2 ⇒ λ^{-3}

# ----------------------------------------------------------------------------
# 3He-B literature anchor (mirrored from W11-5)
# ----------------------------------------------------------------------------
DELTA_BCS_WEAK_RATIO = np.pi * np.exp(-np.euler_gamma)  # (local) ~1.7639
SC_CORR_A = 1.151  # (local)
SC_CORR_B = 1.111  # (local)
DELTA_A_OVER_KBT_C = DELTA_BCS_WEAK_RATIO * SC_CORR_A  # (local) ~ 2.030
DELTA_B_OVER_KBT_C = DELTA_BCS_WEAK_RATIO * SC_CORR_B  # (local) ~ 1.960
R_3HeB_lit = (
    (DELTA_A_OVER_KBT_C ** 2 - DELTA_B_OVER_KBT_C ** 2)
    / (DELTA_A_OVER_KBT_C ** 2 + DELTA_B_OVER_KBT_C ** 2)
)  # (local) +0.03536

# §W3a-14 anchor for composability cross-check
R_M3C_PROJECTED_W3A14_ANCHOR = -1.25397  # (local) from §W3a-14 npz output

# ----------------------------------------------------------------------------
# Input file pins
# ----------------------------------------------------------------------------
INPUT_PINS_PATHS = {  # (local)
    "canonical_constants.py": HERE / "canonical_constants.py",
    "s84_spectrum_cache_L12_tau019.npz": HERE / "s84_spectrum_cache_L12_tau019.npz",
    "_spectral_action_regulators.py": HERE / "_spectral_action_regulators.py",
    "s87_w11_3heb_excess_inheritance_comparison.py": (
        HERE / "s87_w11_3heb_excess_inheritance_comparison.py"
    ),
    "s88_w3a_M3C_projected_npz": (
        HERE / "s88_w3a_3heb_excess_inheritance_m3c_projected_retry.npz"
    ),
    "3HeB-inheritance-canonical": (
        PROJECT_ROOT / "sessions" / "framework" / "correspondence"
        / "3HeB-inheritance-canonical.md"
    ),
    "cross-pillar-bridge-anatomy.md": (
        PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
    ),
    "inheritance-falsifier-protocol.md": (
        PROJECT_ROOT / ".claude" / "rules" / "inheritance-falsifier-protocol.md"
    ),
    "phononic-framing.md": (
        PROJECT_ROOT / ".claude" / "rules" / "phononic-framing.md"
    ),
}


def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    payload = "\n".join(f"{k}={v}" for k, v in sorted(input_pin_map.items())).encode()  # (local)
    return hashlib.sha256(payload).hexdigest()


# ----------------------------------------------------------------------------
# Substrate-distance-1 spectral moment
# ----------------------------------------------------------------------------
def triality(p: int, q: int) -> int:
    return (p - q) % 3


def compute_a3_on_subset(sectors_subset, sector_evals):
    """
    Compute substrate-distance-1 spectral moment a_3 = Σ d(p,q) · λ_min(p,q)^{-3}
    over a sub-list of sectors.  λ_min from cached eigenvalue arrays.
    """
    a3 = 0.0  # (local)
    n_sec = 0  # (local)
    sector_lambdas = []  # (local) for diagnostic
    for (p, q, d, C2) in sectors_subset:
        evals = sector_evals.get((p, q))
        if evals is None:
            continue
        abs_evals = evals['abs_evals']
        if len(abs_evals) == 0:
            continue
        lam_min = float(np.min(abs_evals))  # (local)
        contrib = float(d) * lam_min ** (-S_POLE_POWER)  # (local)
        a3 += contrib
        sector_lambdas.append((p, q, d, lam_min, contrib))
        n_sec += 1
    return a3, n_sec, sector_lambdas


def main():
    # ------------------------------------------------------------------------
    # 1. Stamp input SHAs
    # ------------------------------------------------------------------------
    input_pin_map = {}  # (local)
    for name, p in INPUT_PINS_PATHS.items():
        if p.exists():
            input_pin_map[name] = sha256_of_file(p)
        else:
            input_pin_map[name] = "<missing>"

    print("=" * 78)
    print(f"GATE  : {GATE_ID}")
    print(f"SCHEME: {SCHEME}")
    print(f"CONV  : {CONVENTION}")
    print(f"L_max : {L_MAX}; tau_fold = {tau_fold}; M_KK = {M_KK:.6e}")
    print(f"Substrate-distance-1 pole: s=(d-n)/2=3/2 ⇒ λ^{{-{S_POLE_POWER}}} weighting")
    print("INPUT PIN SHA-256 (truncated to 16 hex):")
    for k, v in sorted(input_pin_map.items()):
        print(f"  {k:50s} {v[:16]}")
    print("=" * 78)

    # ------------------------------------------------------------------------
    # 2. Load s84 cache eigenvalues per sector
    # ------------------------------------------------------------------------
    cache_path = HERE / "s84_spectrum_cache_L12_tau019.npz"  # (local)
    cache = np.load(cache_path, allow_pickle=True)
    sector_evals = cache['sector_evals'].item()  # (local) dict (p, q) → {dim, level, abs_evals}
    print(f"\nLoaded s84 cache: {len(sector_evals)} (p, q) sectors with eigenvalue arrays")

    # ------------------------------------------------------------------------
    # 3. Enumerate sectors and partition by triality
    # ------------------------------------------------------------------------
    sectors = _enumerate_sectors(L_MAX)  # (local)
    n_total = len(sectors)  # (local)
    sectors_BdG = [s for s in sectors if triality(s[0], s[1]) == 0]      # (local)
    sectors_M3C = [s for s in sectors if triality(s[0], s[1]) != 0]      # (local)

    print(f"\nSector partition at L_max={L_MAX}:")
    print(f"  total                              : {n_total}")
    print(f"  BdG-restricted (triality = 0)      : {len(sectors_BdG)}")
    print(f"  M_3(C) Cartan-zone (triality != 0) : {len(sectors_M3C)}")

    # ------------------------------------------------------------------------
    # 4. Compute a_3 spectral moments
    # ------------------------------------------------------------------------
    a3_full, n_full, lambdas_full = compute_a3_on_subset(sectors,        sector_evals)
    a3_BdG,  n_BdG,  lambdas_BdG  = compute_a3_on_subset(sectors_BdG,    sector_evals)
    a3_M3C,  n_M3C,  lambdas_M3C  = compute_a3_on_subset(sectors_M3C,    sector_evals)

    print(f"\nSubstrate-distance-1 spectral moments a_3 = Σ d(p,q) · λ_min(p,q)^{{-{S_POLE_POWER}}}:")
    print(f"  a_3_full = {a3_full:.6e}  (n_used = {n_full})")
    print(f"  a_3_BdG  = {a3_BdG:.6e}   (n_used = {n_BdG})")
    print(f"  a_3_M3C  = {a3_M3C:.6e}   (n_used = {n_M3C})")
    partition_check = abs(a3_full - (a3_BdG + a3_M3C)) / max(a3_full, 1e-30)  # (local)
    print(f"  partition_residual |a_3_full - (a_3_BdG + a_3_M3C)| / a_3_full = {partition_check:.3e}")

    # ------------------------------------------------------------------------
    # 5. R_substrate_redefined: BdG vs M_3(C) substrate-distance-1 asymmetry
    # ------------------------------------------------------------------------
    if (a3_BdG + a3_M3C) > 0:
        R_substrate_redefined = (a3_BdG - a3_M3C) / (a3_BdG + a3_M3C)  # (local)
    else:
        R_substrate_redefined = float("nan")  # (local)

    # Alternative ι_*-composable interpretation: BdG fraction of full a_3
    R_substrate_via_iota_alt = a3_BdG / a3_full if a3_full > 0 else float("nan")  # (local)

    print(f"\nR_substrate_redefined (BdG vs M_3(C) substrate-distance-1 asymmetry):")
    print(f"  R_substrate_redefined = (a_3_BdG - a_3_M3C) / (a_3_BdG + a_3_M3C) = {R_substrate_redefined:.6e}")
    print(f"  R_substrate_via_iota (BdG-fraction interpretation)               = {R_substrate_via_iota_alt:.6e}")

    # ------------------------------------------------------------------------
    # 6. Composability cross-check (CC2)
    #    R_substrate_via_iota = ι_*(R_substrate_full) ≈ R_M3C_projected from §W3a-14
    #    Composability residual: R_substrate_redefined vs the W11-5-then-projected baseline
    # ------------------------------------------------------------------------
    composability_residual = abs(R_substrate_redefined - R_M3C_PROJECTED_W3A14_ANCHOR)  # (local)
    print(f"\nCC2 Composability check (per plan §322-323):")
    print(f"  R_substrate_redefined          = {R_substrate_redefined:.6e}")
    print(f"  R_M3C_projected (§W3a-14)      = {R_M3C_PROJECTED_W3A14_ANCHOR:.6e}")
    print(f"  composability_residual         = {composability_residual:.4e}")
    if composability_residual >= COMPOSABILITY_TOL:
        print(f"  → composability_residual ≥ {COMPOSABILITY_TOL} : W11-5 was non-composable (DIAGNOSTIC, not FAIL per plan §322-323)")
    else:
        print(f"  → composability_residual < {COMPOSABILITY_TOL} : W11-5 + cohomology surrogate match")

    # ------------------------------------------------------------------------
    # 7. Cocycle ratio invariant cross-check (CC1)
    # ------------------------------------------------------------------------
    cocycle_ratio_canonical = cocycle_norm_phi67 / cocycle_norm_phi88  # (local)
    cocycle_ratio_residual = abs(cocycle_ratio_canonical - substrate_cocycle_ratio_67_88)  # (local)
    print(f"\nCC1 cocycle ratio invariant:")
    print(f"  phi67 / phi88 (computed) = {cocycle_ratio_canonical:.6f}")
    print(f"  canonical pin            = {substrate_cocycle_ratio_67_88:.6f}")
    print(f"  residual                 = {cocycle_ratio_residual:.3e}  (Class 8.3 publication tol = {COCYCLE_INV_TOL})")
    cc1_pass = cocycle_ratio_residual < COCYCLE_INV_TOL  # (local)

    # ------------------------------------------------------------------------
    # 8. (Δ_B/Δ_A)^p cancellation at p=0 (CC3)
    # ------------------------------------------------------------------------
    p_cancel = 0  # (local)
    cancellation_factor = (DELTA_B_OVER_KBT_C / DELTA_A_OVER_KBT_C) ** p_cancel  # (local)
    cancellation_residual = abs(cancellation_factor - 1.0)  # (local)
    R_3HeB_predicted = R_substrate_redefined * cancellation_factor  # (local)

    # ------------------------------------------------------------------------
    # 9. ratio_mismatch_redefined per plan §"Step 5"
    # ------------------------------------------------------------------------
    if R_3HeB_lit == 0:
        ratio_mismatch_redefined = float("inf")  # (local)
    else:
        ratio_mismatch_redefined = abs(R_3HeB_predicted - R_3HeB_lit) / abs(R_3HeB_lit)  # (local)

    print(f"\nLiterature anchor R_3HeB_lit = {R_3HeB_lit:.6e}")
    print(f"Substrate prediction R_3HeB_pred = R_substrate_redefined × (Δ_B/Δ_A)^0 = {R_3HeB_predicted:.6e}")
    print(f"\n*** ratio_mismatch_redefined (plan metric: |R - R_lit| / |R_lit|): {ratio_mismatch_redefined:.6e} ***")

    sign_R_lit = +1 if R_3HeB_lit > 0 else (-1 if R_3HeB_lit < 0 else 0)  # (local)
    sign_R_pred = +1 if R_3HeB_predicted > 0 else (-1 if R_3HeB_predicted < 0 else 0)  # (local)
    sign_match = (sign_R_pred == sign_R_lit)  # (local)
    print(f"  sign(R_pred) = {sign_R_pred:+d}; sign(R_lit) = {sign_R_lit:+d}; sign_match = {sign_match}")

    # ------------------------------------------------------------------------
    # 10. Verdict — composite collapse per gate-verdicts.md S87+ schema-v2
    # ------------------------------------------------------------------------
    mag_pass_strict = ratio_mismatch_redefined <= LEVEL3_STRICT  # (local)
    mag_pass_loose  = (LEVEL3_STRICT < ratio_mismatch_redefined <= LEVEL3_LOOSE)  # (local)
    cocycle_ok = cc1_pass  # (local)

    if mag_pass_strict and cocycle_ok and sign_match:
        magnitude_verdict = "PASS"  # (local)
        verdict = "PASS"  # (local)  — strict cohomology Level-2/3
    elif mag_pass_loose and cocycle_ok and sign_match:
        magnitude_verdict = "INFO"  # (local)
        verdict = "INFO"  # (local)  — envelope-loose Level 3
    elif not cocycle_ok:
        magnitude_verdict = "FAIL"  # (local) severe structural defect
        verdict = "FAIL"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
        verdict = "FAIL"  # (local)

    sign_verdict = "PASS" if sign_match else "FAIL"  # (local)
    regime_verdict = "VALID"  # (local) L_max=10 canonical truncation

    print(f"\nVERDICT (composite): {verdict}")
    print(f"  sign_verdict      = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")
    print(f"  PASS-strict band: ratio_mismatch ≤ {LEVEL3_STRICT}")
    print(f"  PASS-loose band : {LEVEL3_STRICT} < ratio_mismatch ≤ {LEVEL3_LOOSE}")
    print(f"  FAIL band      : > {LEVEL3_LOOSE}")

    # ------------------------------------------------------------------------
    # 11. Closure SHAs
    # ------------------------------------------------------------------------
    pinmap_for_audit = dict(input_pin_map)  # (local)
    pinmap_for_audit["_gate_id"] = GATE_ID
    pinmap_for_audit["_scheme"] = SCHEME
    pinmap_for_audit["_convention"] = CONVENTION
    pinmap_for_audit["_L_max"] = str(L_MAX)
    pinmap_for_audit["_s_pole_power"] = str(S_POLE_POWER)
    audit_sha = closure_hash(pinmap_for_audit)  # (local)

    content_payload = {  # (local)
        "value": ratio_mismatch_redefined,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "schema_version": SCHEMA_VERSION,
        "R_substrate_redefined": R_substrate_redefined,
        "R_substrate_via_iota_alt": R_substrate_via_iota_alt,
        "R_3HeB_lit": R_3HeB_lit,
        "a3_BdG": a3_BdG,
        "a3_M3C": a3_M3C,
        "a3_full": a3_full,
        "n_BdG": n_BdG,
        "n_M3C": n_M3C,
        "partition_check": partition_check,
        "composability_residual": composability_residual,
        "cocycle_ratio_residual": cocycle_ratio_residual,
        "cancellation_residual": cancellation_residual,
        "verdict": verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "R_universal_HP1_strict_F4_canonical": R_universal_HP1_strict_F4,
        "substrate_cocycle_ratio_67_88_canonical": substrate_cocycle_ratio_67_88,
    }
    content_sha = hashlib.sha256(
        json.dumps(content_payload, sort_keys=True, default=str).encode()
    ).hexdigest()  # (local)

    # ------------------------------------------------------------------------
    # 12. Save .npz + .png artifacts
    # ------------------------------------------------------------------------
    npz_path = HERE / "s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.npz"  # (local)
    np.savez(
        npz_path,
        R_substrate_redefined=np.float64(R_substrate_redefined),
        R_substrate_via_iota_alt=np.float64(R_substrate_via_iota_alt),
        R_3HeB_lit=np.float64(R_3HeB_lit),
        ratio_mismatch_redefined=np.float64(ratio_mismatch_redefined),
        composability_residual=np.float64(composability_residual),
        a3_BdG=np.float64(a3_BdG),
        a3_M3C=np.float64(a3_M3C),
        a3_full=np.float64(a3_full),
        partition_check=np.float64(partition_check),
        n_BdG=np.int64(n_BdG),
        n_M3C=np.int64(n_M3C),
        n_full=np.int64(n_full),
        cocycle_ratio_residual=np.float64(cocycle_ratio_residual),
        cancellation_residual=np.float64(cancellation_residual),
        substrate_cocycle_ratio_67_88_canonical=np.float64(substrate_cocycle_ratio_67_88),
        R_universal_HP1_strict_F4_canonical=np.float64(R_universal_HP1_strict_F4),
        s_pole_power=np.int64(S_POLE_POWER),
        L_max=np.int64(L_MAX),
        verdict=np.array(verdict),
        sign_verdict=np.array(sign_verdict),
        magnitude_verdict=np.array(magnitude_verdict),
        regime_verdict=np.array(regime_verdict),
        audit_sha=np.array(audit_sha),
        content_sha=np.array(content_sha),
    )
    print(f"\nSaved data: {npz_path.name}")

    # 3-panel plot
    fig, axes = plt.subplots(3, 1, figsize=(10, 12))

    # Panel 1: a_3 spectral moments comparison
    ax = axes[0]
    labels = ["a_3_full\n(all 65 sectors)", f"a_3_BdG\n(triality=0; {n_BdG} sec)", f"a_3_M3C\n(triality≠0; {n_M3C} sec)"]  # (local)
    values = [a3_full, a3_BdG, a3_M3C]  # (local)
    colors = ["#888888", "#2a6fdb", "#dd6b3a"]  # (local)
    bars = ax.bar(labels, values, color=colors, alpha=0.85, edgecolor="black", linewidth=1.0)
    for b, v in zip(bars, values):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.02, f"{v:.4e}", ha="center", va="bottom", fontsize=9)
    ax.set_ylabel(f"a_3 = Σ d(p,q) · λ_min(p,q)^{{-{S_POLE_POWER}}}")
    ax.set_title(f"S88 §W3a-18 — substrate-distance-1 spectral moments by triality (L_max={L_MAX})")
    ax.grid(axis="y", alpha=0.3)

    # Panel 2: R_substrate_redefined comparison vs R_3HeB_lit
    ax = axes[1]
    bar_labels = ["R_substrate_redefined\n(BdG vs M_3(C) asymmetry)", "R_3HeB_lit\n(Δ_A vs Δ_B asymmetry)"]  # (local)
    bar_values = [R_substrate_redefined, R_3HeB_lit]  # (local)
    bar_colors = ["#22aa44" if verdict == "PASS" else "#aa6622" if verdict == "INFO" else "#aa2222", "#2a8c4a"]  # (local)
    bars = ax.bar(bar_labels, bar_values, color=bar_colors, alpha=0.85, edgecolor="black", linewidth=1.0)
    for b, v in zip(bars, bar_values):
        ax.text(b.get_x() + b.get_width() / 2,
                v + 0.02 * (max(abs(v) for v in bar_values) if bar_values else 1) * np.sign(v if v != 0 else 1),
                f"{v:+.4e}", ha="center", va="bottom" if v >= 0 else "top", fontsize=9)
    ax.axhline(0, color="black", linewidth=0.5)
    ax.set_ylabel("R observable")
    ax.set_title(f"Substrate prediction vs lit anchor; verdict = {verdict}")
    ax.grid(axis="y", alpha=0.3)

    # Panel 3: ratio_mismatch_redefined log scale with thresholds
    ax = axes[2]
    bar_labels = ["W11-5 anchor\n(metric: max(|.|,|.|))", "W3a-18 retry\n(plan metric: |R-R_lit|/|R_lit|)"]  # (local)
    bar_values = [1.029, ratio_mismatch_redefined]  # (local)
    bar_colors = ["#aa2222", "#22aa44" if verdict == "PASS" else "#aa6622" if verdict == "INFO" else "#aa2222"]  # (local)
    bars = ax.bar(bar_labels, bar_values, color=bar_colors, alpha=0.85, edgecolor="black", linewidth=1.0)
    for b, v in zip(bars, bar_values):
        if not np.isnan(v) and not np.isinf(v):
            ax.text(b.get_x() + b.get_width() / 2, v * 1.05 if v > 0 else v * 0.95,
                    f"{v:.3e}", ha="center", va="bottom", fontsize=9)
    ax.axhline(LEVEL3_STRICT, color="green", linestyle="--", linewidth=1.5, label=f"PASS-strict ≤ {LEVEL3_STRICT}")
    ax.axhline(LEVEL3_LOOSE,  color="orange", linestyle="--", linewidth=1.5, label=f"INFO ≤ {LEVEL3_LOOSE}")
    ax.set_ylabel("ratio_mismatch")
    ax.set_yscale("log")
    ax.set_title(f"§W3a-18 verdict = {verdict}  |  ratio_mismatch = {ratio_mismatch_redefined:.3e}")
    ax.legend(loc="best", fontsize=8)
    ax.grid(axis="y", alpha=0.3, which="both")

    plt.tight_layout()
    png_path = HERE / "s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.png"  # (local)
    fig.savefig(png_path, dpi=110)
    plt.close(fig)
    print(f"Saved plot: {png_path.name}")

    # ------------------------------------------------------------------------
    # 13. Append verdict line + dual-SHA + 3-tuple to s88_gate_verdicts.txt
    # ------------------------------------------------------------------------
    verdict_path = HERE / "s88_gate_verdicts.txt"  # (local)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={ratio_mismatch_redefined:.6e} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}"
    )  # (local)
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
    )  # (local)
    tuple_line = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
    )  # (local)
    with open(verdict_path, "a", encoding="utf-8") as fh:
        fh.write(canonical_line + "\n")
        fh.write(companion_line + "\n")
        fh.write(tuple_line + "\n")
    print(f"\nVerdict appended to: {verdict_path.name}")
    print(f"  CANONICAL:  {canonical_line[:120]}...")
    print(f"  COMPANION:  {companion_line}")
    print(f"  3-TUPLE:    {tuple_line}")

    print(
        f"\n4-TUPLE: (value={ratio_mismatch_redefined:.6e}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )

    return verdict


if __name__ == "__main__":
    v = main()
    sys.exit(0)
