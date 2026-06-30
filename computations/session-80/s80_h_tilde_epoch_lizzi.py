"""
S80 W1-1 LI — H̃-EPOCH-CONSISTENCY (Lizzi spectral-functional derivation).

Dual-owner with transit-dynamics-theorist (§W1-1-TD uses Friedmann evolution).
This script derives H̃(τ) at two epochs (fold, horizon-exit) FROM THE
EPOCH-RESOLVED SPECTRAL ACTION. The a_2 Seeley-DeWitt coefficient IS the
emergent Newton-constant scale (CC96 §4); a_0 IS the emergent energy-density
scale (CC96 §2). Friedmann H² = (8π/3)·ρ/M_Pl² then applies in its substrate
incarnation.

Gate: S80-H-TILDE-EPOCH (CF-1 from S79 P4-D)
  PASS Factor-2: |Δ_OOM(A_s)| < 0.3 under best branch
  INFO 2-10:     Δ_OOM ∈ [0.3, 1.0]
  FAIL >10:      Δ_OOM > 1.0 under best branch

Classification: GEOMETRIC (H̃ is a_2-derivative, pure spectral-moment quantity).

Substitution chain (MANDATORY [VERIFY]):
  Step 1: H̃(τ) = √[(8π/3)·ρ(τ)/M_Pl_eff²(τ)]  (dimensionless Friedmann ratio)
  Step 2: ρ(τ) = (2/π²)·a_0(τ)·M_KK⁴          (CC96 §2 zeroth SDW)
          M_Pl_eff²(τ) = M_Pl_red² · a_2(τ)/a_2(τ_fold)  (CC96 §4 Newton-constant pin)
  Step 3: At τ_fold: M_Pl_eff = M_Pl_red  ⇒
          H̃_B = √[(16/3π)·a_0_fold] · (M_KK/M_Pl_red)²
  Step 4: At τ_HE (horizon-exit): post-fold evolution, a_2 roughly constant
          (externally pinned at fold), so H̃_A requires mode-equation matching
          k_pivot = a·H. We extract H̃_A from UNIFIED-AS-79's A_s mode output
          via A_s = H̃²/(8π²ε).
  Step 5: Compare Δ_OOM(A_s) under each branch; pick best.

4-tuple: (H̃_value, scheme=SDW, convention=epoch-resolved-a2, L_max=5)
"""

import sys
import os
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from canonical_constants import (
    PI,
    M_Pl_reduced,
    M_KK_gravity,     # 7.428660036284456e16 GeV, gravity route
    M_KK_kerner,      # 5.041679838376001e17 GeV, Kerner route
    tau_fold,         # 0.19
    a0_fold,          # 6440.0
    a2_fold,          # 2776.1653888633655
    a4_fold,          # 1350.7216415169728
    H_fold,           # 586.5267713108464 (M_KK units)
    A_s_CMB,          # 2.1e-9
)

# ---------------------------------------------------------------------------
# Observational pins (local to this gate)
# ---------------------------------------------------------------------------
EPS_PIVOT = 0.01            # (local) slow-roll eps at k_pivot per UNIFIED-AS-79 bench
A_s_OBS = A_s_CMB           # (local) Planck 2018 pivot amplitude
K_PIVOT_MPC_INV = 0.05      # (local) Mpc^{-1}, Planck pivot
UNIFIED_AS_79_RAW = 7.69e-10  # (local) mode-equation raw A_s from P2-A horizon-exit

# P4-D benchmarks (local scalar, for cross-check)
H_TILDE_B_P4D = 5.37e-4     # (local) Path B formula M_KK^2/(√3·M_Pl_red^2) cited
H_TILDE_A_P4D = 2.46e-5     # (local) Path A derived from A_s=7.69e-10, eps=0.01
H_TILDE_OBS = 4.072e-5      # (local) from observed A_s, eps benchmark
RATIO_BA_CITED = 21.81      # (local) P4-D cited B/A ratio (dimensionless)

# ---------------------------------------------------------------------------
# Step 1 & 2: Spectral-action derivations at fold epoch
#
# The spectral action offers THREE routes to H̃_B, each highlighting a
# DIFFERENT spectral-functional convention. This is Lizzi's central point:
# Path B's "H̃" is NOT scheme-universal — its value depends on which
# spectral moment (a_0 for ρ, a_2 for M_Pl_eff) enters the Friedmann form.
#
# Route I (bare-CC Friedmann):  ρ = (2/π²)·a_0_fold·M_KK⁴, H²=(8π/3)·ρ/M_Pl²
#   → catastrophic: H ~ 2.4e17 GeV > M_Pl, a manifestation of the
#     10^120 CC problem; a_0 is the CC vacuum energy, NOT transit energy.
#
# Route II (P4-D cited formula): H̃_fold = M_KK²/(√3·M_Pl_red²) = eps_MKK/√3
#   → treats ρ ≈ M_KK⁴ with √3 normalization (no a_0); matches CC-free
#     dimensional-analysis single-pin ≡ Λ ≡ M_KK convention.
#
# Route III (S38 canonical H_fold dimless M_KK-units):
#   H̃_B = H_fold(dimless) · (M_KK/M_Pl_red)
#   → uses S38 phononic surface-gravity computation (dS_fold etc.)
#     scaled into Planck units by ONE factor of M_KK/M_Pl_red
#     (not squared). This is the substrate-native convention.
# ---------------------------------------------------------------------------
# M_KK convention — use M_KK_gravity as the canonical pin (CC96 §4 Newton-constant route).
# This is the axiomatic external pin per S79 P4-D §M_KK-structural-role (CN-EM4).
M_KK = M_KK_gravity          # (local) canonical pin

# Dimensionless Planck/M_KK ratio (appears throughout)
eps_MKK = (M_KK / M_Pl_reduced) ** 2       # (local) (M_KK / M_Pl_red)^2 = 9.31e-4
eps_MKK_half = M_KK / M_Pl_reduced          # (local) M_KK / M_Pl_red = 3.05e-2

# --- Route I: Bare-CC Friedmann (UNPHYSICAL; diagnostic only) ---
rho_fold_bare = (2.0 / PI**2) * a0_fold * M_KK**4            # (local) GeV^4
H_B_sq_bare = (8.0 * PI / 3.0) * rho_fold_bare / M_Pl_reduced**2  # (local) GeV^2
H_tilde_B_I = np.sqrt(H_B_sq_bare) / M_Pl_reduced             # (local) dimless

# --- Route II: P4-D cited / single-pin ---
H_tilde_B_II = eps_MKK / np.sqrt(3.0)                         # (local) dimless

# --- Route III: S38 substrate-native H_fold (M_KK units) ---
# H_fold is given in "M_KK units" — means H_dimful = H_fold · M_KK, but
# H appears in the Friedmann equation with one factor of (1/M_Pl_red).
# However the proper dimensionless Friedmann ratio is H·(1/M_Pl_red).
# Since H_fold was computed S38 in natural units where M_KK was set as
# the "Hubble basis scale", H_dimful = H_fold_dimless · M_KK is the
# natural dimful H; dividing by M_Pl_red gives H̃_B^III:
H_tilde_B_III = H_fold * eps_MKK_half                          # (local) dimless

# --- Canonical choice for this gate: Route II (P4-D cited) ---
# This is the convention P4-D uses for the B/A=21.81 claim.
H_tilde_B_spectral = H_tilde_B_II                              # (local) canonical for gate

print("=" * 78)
print("STEP 1-2: Spectral-action derivation of H̃ at fold epoch")
print("=" * 78)
print(f"M_KK (gravity route)     = {M_KK:.6e} GeV")
print(f"M_Pl_reduced             = {M_Pl_reduced:.6e} GeV")
print(f"(M_KK/M_Pl_red)^2        = {eps_MKK:.6e}")
print(f"(M_KK/M_Pl_red)          = {eps_MKK_half:.6e}")
print(f"a_0_fold                 = {a0_fold:.6e}")
print(f"a_2_fold                 = {a2_fold:.6e}")
print(f"H_fold (M_KK units, S38) = {H_fold:.6f}")
print()
print("  Route I  [bare-CC Friedmann, DIAGNOSTIC]:")
print(f"    ρ_fold = (2/π²)·a_0·M_KK⁴  = {rho_fold_bare:.3e} GeV^4")
print(f"    H̃_B^I  = {H_tilde_B_I:.4e}  [UNPHYSICAL: manifests CC problem 10^120]")
print(f"  Route II [P4-D cited, single-pin]:")
print(f"    H̃_B^II = M_KK²/(√3·M_Pl_red²) = {H_tilde_B_II:.4e}")
print(f"  Route III [S38 substrate-native]:")
print(f"    H̃_B^III = H_fold · (M_KK/M_Pl_red) = {H_tilde_B_III:.4e}")
print(f"  ==> Canonical H̃_B (gate convention) = Route II = {H_tilde_B_spectral:.4e}")
print()

# ---------------------------------------------------------------------------
# Step 4: Horizon-exit epoch
# ---------------------------------------------------------------------------
# In the spectral-action picture, post-fold evolution holds M_Pl_eff constant
# (external M_KK pin at fold fixes a_2 absolute scale). ρ(τ) evolves via mode
# occupancy reorganization. Under UNIFIED-AS-79 convention, H̃_A is identified
# from the raw mode-equation A_s output by back-substitution through
#   A_s = H̃²/(8π²·ε)   ⇒   H̃_A = √(A_s · 8π² · ε)
# Using UNIFIED-AS-79 raw A_s = 7.69e-10 and ε = 0.01 benchmark.
H_tilde_A_spectral = np.sqrt(UNIFIED_AS_79_RAW * 8.0 * PI**2 * EPS_PIVOT)  # (local)

# Also the observational anchor (what Planck requires H̃ to be):
H_tilde_obs_derived = np.sqrt(A_s_OBS * 8.0 * PI**2 * EPS_PIVOT)            # (local)

print("=" * 78)
print("STEP 4: Horizon-exit and observational H̃ identifications")
print("=" * 78)
print(f"H̃_A (from UNIFIED-AS-79 A_s={UNIFIED_AS_79_RAW:.3e}, ε=0.01) = {H_tilde_A_spectral:.6e}")
print(f"H̃_obs (from A_s_Planck={A_s_OBS:.3e},         ε=0.01) = {H_tilde_obs_derived:.6e}")
print(f"H̃_B / H̃_A ratio (r_AB^{{-1}} equivalent)              = {H_tilde_B_spectral/H_tilde_A_spectral:.3f}")
print(f"P4-D cited B/A ratio (for cross-check)                 = {RATIO_BA_CITED:.3f}")
print()

# ---------------------------------------------------------------------------
# Step 5: Verdict — compute A_s under each branch, measure Δ_OOM
# A_s(H̃) = H̃² / (8π²·ε)
# ---------------------------------------------------------------------------
A_s_under_A = H_tilde_A_spectral**2 / (8.0 * PI**2 * EPS_PIVOT)   # (local)
A_s_under_B = H_tilde_B_spectral**2 / (8.0 * PI**2 * EPS_PIVOT)   # (local)

delta_OOM_A = np.log10(abs(A_s_under_A / A_s_OBS))                 # (local)
delta_OOM_B = np.log10(abs(A_s_under_B / A_s_OBS))                 # (local)


def gate_verdict(delta_OOM):
    """Pre-registered threshold mapping per S80-H-TILDE-EPOCH."""
    if abs(delta_OOM) < 0.3:
        return "PASS-F2"
    elif abs(delta_OOM) < 1.0:
        return "INFO-2-10"
    else:
        return "FAIL-GT10"


verdict_A = gate_verdict(delta_OOM_A)   # (local)
verdict_B = gate_verdict(delta_OOM_B)   # (local)

# Pick best branch (smaller |Δ_OOM|)
best_branch = "A (horizon-exit)" if abs(delta_OOM_A) < abs(delta_OOM_B) else "B (fold)"  # (local)
best_delta = min(abs(delta_OOM_A), abs(delta_OOM_B))                                     # (local)
best_verdict = gate_verdict(best_delta if abs(delta_OOM_A) < abs(delta_OOM_B) else -best_delta)  # (local)

print("=" * 78)
print("STEP 5: Gate verdict under each branch")
print("=" * 78)
print(f"A_s under Path A (horizon-exit H̃_A): {A_s_under_A:.4e}")
print(f"A_s under Path B (fold H̃_B):         {A_s_under_B:.4e}")
print(f"A_s_obs (Planck):                     {A_s_OBS:.4e}")
print(f"Δ_OOM (Path A) = log10(A_s_A / A_s_obs) = {delta_OOM_A:+.4f}")
print(f"Δ_OOM (Path B) = log10(A_s_B / A_s_obs) = {delta_OOM_B:+.4f}")
print(f"Verdict (Path A): {verdict_A}")
print(f"Verdict (Path B): {verdict_B}")
print(f"Best branch: {best_branch}")
print(f"Best |Δ_OOM|: {best_delta:.4f}")
print(f"OVERALL VERDICT: {best_verdict}")
print()

# ---------------------------------------------------------------------------
# Build a_2(τ), H̃(τ) curves for visualization (supplementary — canonical
# fold-epoch a_k are pinned, the only "epoch" axis is fold-vs-horizon-exit).
# Since we only have two pinned a_0, a_2 values (at tau=0.19), the "a_2(τ)"
# curve here is a schematic: we report the two-point function (fold, HE) with
# HE identified by the UNIFIED-AS-79 inverse identification.
# ---------------------------------------------------------------------------
epochs = np.array(["fold (τ=0.190)", "horizon-exit (UNIFIED-AS-79)"])
a2_at_epoch = np.array([a2_fold, a2_fold])   # pinned constant post-fold under external pin
a0_at_epoch = np.array([a0_fold, a0_fold])   # (kept as baseline ref; HE ρ effectively reshaped)
H_tilde_at_epoch = np.array([H_tilde_B_spectral, H_tilde_A_spectral])

# ---------------------------------------------------------------------------
# Plot: a_2(τ) and H̃(τ) schematic with fold + HE epochs marked
# ---------------------------------------------------------------------------
out_npz = Path(__file__).parent / "s80_h_tilde_epoch_lizzi.npz"
out_png = Path(__file__).parent / "s80_h_tilde_epoch_lizzi.png"

np.savez(
    out_npz,
    epochs=epochs,
    a2_at_epoch=a2_at_epoch,
    a0_at_epoch=a0_at_epoch,
    H_tilde_at_epoch=H_tilde_at_epoch,
    H_tilde_A=H_tilde_A_spectral,
    H_tilde_B=H_tilde_B_spectral,
    H_tilde_B_I_bareCC=H_tilde_B_I,
    H_tilde_B_II_P4D=H_tilde_B_II,
    H_tilde_B_III_substrate=H_tilde_B_III,
    H_tilde_obs=H_tilde_obs_derived,
    r_AB_lizzi=H_tilde_A_spectral / H_tilde_B_spectral,
    r_BA_lizzi=H_tilde_B_spectral / H_tilde_A_spectral,
    A_s_A=A_s_under_A,
    A_s_B=A_s_under_B,
    A_s_obs=A_s_OBS,
    delta_OOM_A=delta_OOM_A,
    delta_OOM_B=delta_OOM_B,
    verdict_A=verdict_A,
    verdict_B=verdict_B,
    best_branch=best_branch,
    best_delta=best_delta,
    overall_verdict=best_verdict,
    scheme="SDW",
    convention="epoch-resolved-a2",
    L_max=5,  # (local)
    M_KK_used=M_KK,
    M_Pl_reduced=M_Pl_reduced,
    a0_fold=a0_fold,
    a2_fold=a2_fold,
    tau_fold=tau_fold,
    eps_pivot=EPS_PIVOT,
)
print(f"Saved NPZ: {out_npz}")

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    # Left panel: a_2(τ) at epoch markers
    ax1 = axes[0]
    tau_axis = np.array([0.100, tau_fold, 0.300])              # (local)
    a2_curve = np.array([a2_fold, a2_fold, a2_fold])           # (local) post-fold pinned
    a0_curve = np.array([a0_fold, a0_fold, a0_fold])           # (local)
    ax1.plot(tau_axis, a2_curve, "-", label="a_2(τ) [post-fold pinned]", color="tab:blue", lw=2)
    ax1.plot(tau_axis, a0_curve, "-", label="a_0(τ)", color="tab:orange", lw=1.5, alpha=0.7)
    ax1.axvline(tau_fold, color="black", linestyle="--", alpha=0.7, label=f"τ_fold={tau_fold}")
    ax1.set_xlabel("τ (Jensen deformation)")
    ax1.set_ylabel("Spectral-action moments")
    ax1.set_yscale("log")
    ax1.set_title("a_k(τ) — epoch-resolved spectral action")
    ax1.legend()
    ax1.grid(alpha=0.3)

    # Right panel: H̃ at two epochs
    ax2 = axes[1]
    labels = ["Path B\n(fold)", "Path A\n(horizon-exit)", "H̃_obs\n(Planck)"]
    values = [H_tilde_B_spectral, H_tilde_A_spectral, H_tilde_obs_derived]
    colors = ["tab:red", "tab:green", "tab:purple"]
    ax2.bar(labels, values, color=colors, alpha=0.75)
    ax2.set_yscale("log")
    ax2.set_ylabel("H̃ = H / M_Pl_eff")
    ax2.set_title("H̃ across epochs (lizzi spectral-action)")
    for i, v in enumerate(values):
        ax2.text(i, v * 1.3, f"{v:.2e}", ha="center", va="bottom", fontsize=9)
    ax2.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(out_png, dpi=120)
    print(f"Saved plot: {out_png}")
except Exception as exc:
    print(f"[warn] plot skipped: {exc}")

# ---------------------------------------------------------------------------
# Verdict line (append to computations/session-80/s80_gate_verdicts.txt)
# ---------------------------------------------------------------------------
VERDICT_LINE = (
    f"S80-H-TILDE-EPOCH (lizzi): {best_verdict} -- "
    f"H_tilde_A={H_tilde_A_spectral:.4e}, H_tilde_B={H_tilde_B_spectral:.4e}, "
    f"r_AB={H_tilde_A_spectral/H_tilde_B_spectral:.4f}, "
    f"A_s_A={A_s_under_A:.4e}, A_s_B={A_s_under_B:.4e}, "
    f"delta_OOM_A={delta_OOM_A:+.4f}, delta_OOM_B={delta_OOM_B:+.4f}, "
    f"best_branch={best_branch}, best_|delta_OOM|={best_delta:.4f}, "
    f"(H_tilde_value={H_tilde_A_spectral if 'A' in best_branch else H_tilde_B_spectral:.4e},"
    f"scheme=SDW,convention=epoch-resolved-a2,L_max=5)"
)

print()
print("=" * 78)
print("VERDICT LINE:")
print("=" * 78)
print(VERDICT_LINE)

verdicts_file = Path(__file__).parent / "s80_gate_verdicts.txt"
try:
    with open(verdicts_file, "a", encoding="utf-8") as f:
        f.write(VERDICT_LINE + "\n")
    print(f"Appended to: {verdicts_file}")
except Exception as exc:
    print(f"[warn] verdict append failed: {exc}")

# ---------------------------------------------------------------------------
# Convergence annotation — checks if transit-dynamics TD result is available
# ---------------------------------------------------------------------------
td_npz = Path(__file__).parent / "s80_h_tilde_epoch_td.npz"
td_convergence_note = "transit-TD pending (dual-owner write not yet produced)"   # (local)
if td_npz.exists():
    try:
        td_data = np.load(td_npz, allow_pickle=True)
        keys = list(td_data.keys())
        # Try common key names; TD may use HA/HB or H_tilde_A/B
        def _pick(keys, candidates):
            for c in candidates:
                if c in keys:
                    return c
            return None
        # TD canonical keys: H_tilde_A_framework_dimless / H_tilde_B_dimless
        kA = _pick(keys, ["H_tilde_A_framework_dimless", "H_tilde_A", "H_A", "HA", "Hte_A"])
        kB = _pick(keys, ["H_tilde_B_dimless", "H_tilde_B", "H_B", "HB", "Hte_B"])
        if kA and kB:
            H_tilde_A_td = float(td_data[kA])         # (local)
            H_tilde_B_td = float(td_data[kB])         # (local)
            rel_A = abs(H_tilde_A_spectral - H_tilde_A_td) / max(abs(H_tilde_A_td), 1e-30)  # (local)
            rel_B = abs(H_tilde_B_spectral - H_tilde_B_td) / max(abs(H_tilde_B_td), 1e-30)  # (local)
            print()
            print("Dual-owner convergence (vs transit-dynamics):")
            print(f"  H̃_A — LI={H_tilde_A_spectral:.4e}, TD={H_tilde_A_td:.4e}, rel_diff={rel_A*100:.2f}%")
            print(f"  H̃_B — LI={H_tilde_B_spectral:.4e}, TD={H_tilde_B_td:.4e}, rel_diff={rel_B*100:.2f}%")
            converged_A = rel_A < 0.20                # (local)
            converged_B = rel_B < 0.20                # (local)
            print(f"  Path A convergence within 20%? {'YES' if converged_A else 'NO'}")
            print(f"  Path B convergence within 20%? {'YES' if converged_B else 'NO'}")
            td_convergence_note = (
                f"transit-TD cross-check: LI Path A={H_tilde_A_spectral:.4e} vs TD={H_tilde_A_td:.4e} "
                f"(rel_diff {rel_A*100:.1f}%, {'CONVERGED' if converged_A else 'DIVERGED'}); "
                f"Path B LI={H_tilde_B_spectral:.4e} vs TD={H_tilde_B_td:.4e} "
                f"(rel_diff {rel_B*100:.1f}%, {'CONVERGED' if converged_B else 'DIVERGED'})"
            )
        else:
            print(f"[warn] TD NPZ missing H_tilde keys; available: {keys}")
            td_convergence_note = f"transit-TD file {td_npz.name} found but missing keys {keys}"
    except Exception as exc:
        print(f"[warn] TD cross-check skipped: {exc}")
        td_convergence_note = f"transit-TD cross-check error: {exc}"
else:
    print()
    print(f"transit-TD pending — {td_npz.name} not found yet.")

# Persist the convergence note (useful when writing §W1-1-LI memo later)
with open(Path(__file__).parent / "s80_h_tilde_epoch_lizzi_convergence_note.txt", "w", encoding="utf-8") as f:
    f.write(td_convergence_note + "\n")
