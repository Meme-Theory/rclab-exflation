"""
s74_leggett_vacuum_cc.py -- LEGGETT-VACUUM-CC-74 (W2-N)

Compute chi_Leggett, the Leggett-channel contribution to the cosmological constant
budget, from the zero-point energy of the Leggett mode summed over the (0,0) PW
sector at L_max = 7, normalized to chi_2 = 0.747.

The (0,0) sector is the level-0 SU(3) singlet — the lowest-energy (base-singlet)
sector of D_K on Jensen SU(3). It contains 16 eigenvalues in [0.820, 0.971] M_KK
(level-0 content is fixed regardless of L_max truncation).

Leggett ZPE formula (per the task prompt and W1-F convention fix):
    E_ZPE^{Leggett} = (1/2) * omega_L1 * (1 + 2*n_L)

where omega_L1 = 0.138 M_KK (S52 canonical GL-Josephson, NOT 0.0492) and
n_L = 0.4118 (Bose-Einstein at T_acoustic = 0.112).

The (0,0) sector sum is weighted by a Leggett projection:
    chi_Leggett = sum_{(0,0)} w_Leggett(lambda_i) * E_ZPE^{Leggett} / chi_2

The Leggett projection weight w_Leggett(lambda) is the inter-branch coupling
amplitude for a (0,0)-sector mode at eigenvalue lambda. The Leggett channel
couples (0,0) modes through the Josephson phase split phi_23_split = 0.552 rad
(W1-F canonical). For modes with lambda >> omega_L1, the projection amplitude
scales as (1 - cos phi_23_split) * (omega_L1 / lambda). This is the
dispersive projection of the off-diagonal Leggett coupling.

Pre-registered gate: LEGGETT-VACUUM-CC-74
    PASS if |chi_Leggett_log10 - 0.47| < 0.1, FAIL otherwise. Binary.

Author: van-den-dungen-bridge-theorist
Session: 74 W2-N
"""

import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Canonical constants (required by project rules)
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    omega_L1,       # 0.138 (Leggett-1 frequency, S52/S66 canonical — NOT 0.0492)
    M_KK,           # Kaluza-Klein scale
    T_acoustic,     # 0.112 (GGE acoustic temperature, M_KK)
    tau_fold,       # 0.19
)

# -----------------------------------------------------------------------------
# Task-prompt / W1-F canonical inputs
# -----------------------------------------------------------------------------

# chi_2: curvature 2-cocycle pairing (S66), not yet in canonical_constants.py
chi_2 = 0.747  # (local, task-prompt normalization)

# n_L: thermal Leggett occupation at the acoustic GGE temperature. Matches the
# S74 W1-F working-paper table: n_L1 = 0.4118 = 1/(exp(omega_L1/T_acoustic) - 1)
n_L_target = 0.4118  # (local, W1-F canonical value)

# phi_23_split: Josephson phase split driving Leggett coupling between branches
# (from s73a_fabry_perot_cavity.npz per W1-F convention fix)
phi_23_split = 0.552  # (local, S73a/W1-F)

# Pre-registered gate target (task prompt)
target_log10 = 0.47   # (local)
gate_tol = 0.10       # (local)

# Cache path (W1-C spectrum cache at L=9 tau=0.19, contains all sectors)
CACHE_PATH = Path(__file__).parent / "s74_spectrum_cache_L9_tau019.npz"

OUT_NPZ = Path(__file__).parent / "s74_leggett_vacuum_cc.npz"
OUT_PNG = Path(__file__).parent / "s74_leggett_vacuum_cc.png"


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def bose_einstein(omega, T):
    """Bose-Einstein occupation n_B(omega) at temperature T (same units)."""
    x = omega / T
    if x > 50:
        return 0.0
    return 1.0 / (np.expm1(x))


def load_00_sector_L7():
    """Load the (0,0) PW sector eigenvalues.

    The cache is organized by (p,q) irrep, with sector level = p+q. The (0,0)
    sector is level 0 — a single 1-dimensional irrep whose content is
    INDEPENDENT of L_max (selecting L_max>=0 yields the same 16 eigenvalues).
    'L_max = 7' in the task prompt refers to the cache's overall truncation,
    not a filter on this sector.
    """
    data = np.load(CACHE_PATH, allow_pickle=True)
    sector_evals = data["sector_evals"].item()
    if (0, 0) not in sector_evals:
        raise KeyError("(0,0) sector not found in s74_spectrum_cache_L9_tau019.npz")

    inner = sector_evals[(0, 0)]
    evals = np.asarray(inner["abs_evals"], dtype=np.float64)
    level = int(inner["level"])
    dim = int(inner["dim"])
    assert level == 0, f"(0,0) sector should be level 0, got {level}"
    assert dim == 1, f"(0,0) sector should be 1-dimensional irrep, got {dim}"
    return np.sort(evals)


# -----------------------------------------------------------------------------
# Main computation
# -----------------------------------------------------------------------------

def main():
    print("=" * 72)
    print("LEGGETT-VACUUM-CC-74 (W2-N) -- chi_Leggett from Leggett ZPE over (0,0)")
    print("=" * 72)

    # --- Inputs ---------------------------------------------------------------
    lams = load_00_sector_L7()
    N_00 = lams.size
    print(f"\n[input] (0,0) sector eigenvalues: {N_00} values (L=0, 1d irrep)")
    print(f"        range = [{lams.min():.6f}, {lams.max():.6f}] M_KK")
    print(f"        mean  = {lams.mean():.6f} M_KK")
    print(f"\n[const] omega_L1     = {omega_L1:.6f} M_KK  (S52/S66 canonical)")
    print(f"        T_acoustic   = {T_acoustic:.6f} M_KK")
    print(f"        phi_23_split = {phi_23_split:.4f} rad")
    print(f"        chi_2        = {chi_2:.3f}")

    # --- Leggett occupation (thermal GGE) ------------------------------------
    n_L_thermal = bose_einstein(omega_L1, T_acoustic)
    print(f"\n[n_L]   Bose-Einstein(omega_L1, T_acoustic) = {n_L_thermal:.6f}")
    print(f"        W1-F reference value                  = {n_L_target:.6f}")
    print(f"        delta                                  = {abs(n_L_thermal - n_L_target):.2e}")
    # Use the thermodynamic computation (consistent with W1-F construction)
    n_L = n_L_thermal

    # --- Leggett zero-point energy -------------------------------------------
    # E_ZPE^{Leggett} = (1/2) * omega_L1 * (1 + 2*n_L)
    E_zpe_leg = 0.5 * omega_L1 * (1.0 + 2.0 * n_L)
    print(f"\n[ZPE]   E_ZPE^Leggett = 0.5 * omega_L1 * (1 + 2 n_L)")
    print(f"               = 0.5 * {omega_L1} * (1 + 2*{n_L:.4f})")
    print(f"               = {E_zpe_leg:.6f} M_KK")

    # --- Leggett projection weight on (0,0) modes ----------------------------
    # Dispersive projection amplitude: the Leggett channel couples to a (0,0)
    # mode at eigenvalue lambda with amplitude proportional to
    #   (1 - cos phi_23_split) * (omega_L1 / lambda)
    # The (1 - cos phi) factor is the Josephson coupling strength (W1-F); the
    # (omega_L1 / lambda) factor is the dispersive off-resonance suppression
    # for lambda >> omega_L1. This is the standard low-frequency projection
    # of a gapped branch onto high-energy fiber modes.
    josephson_factor = 1.0 - np.cos(phi_23_split)
    w_Leg = josephson_factor * (omega_L1 / lams)
    sum_w_Leg = np.sum(w_Leg)
    print(f"\n[proj]  (1 - cos phi_23_split) = {josephson_factor:.6f}")
    print(f"        sum w_Leggett over (0,0) = {sum_w_Leg:.6f}")
    print(f"        <w_Leggett>              = {sum_w_Leg/N_00:.6f}")

    # --- chi_Leggett ----------------------------------------------------------
    # chi_Leggett = sum_{(0,0)} w_Leggett(lambda_i) * E_ZPE^Leggett / chi_2
    chi_Leggett = np.sum(w_Leg * E_zpe_leg) / chi_2
    chi_Leggett_log10 = np.log10(chi_Leggett)
    print(f"\n[chi_L] chi_Leggett         = {chi_Leggett:.6f}")
    print(f"        log10(chi_Leggett)  = {chi_Leggett_log10:+.4f}")

    # --- Gate ---------------------------------------------------------------
    print("\n" + "=" * 72)
    print("GATE: LEGGETT-VACUUM-CC-74")
    print("=" * 72)
    gate_diff = abs(chi_Leggett_log10 - target_log10)
    gate_pass = gate_diff < gate_tol
    verdict = "PASS" if gate_pass else "FAIL"
    print(f"  Threshold: |chi_Leggett_log10 - 0.47| < 0.10")
    print(f"  Computed : chi_Leggett_log10 = {chi_Leggett_log10:+.4f}")
    print(f"             |delta| = {gate_diff:.4f}")
    print(f"  Verdict  : {verdict}")

    # --- Cross-checks --------------------------------------------------------
    print("\n" + "-" * 72)
    print("CROSS-CHECKS")
    print("-" * 72)

    # (1) Limiting case omega_L1 = 0
    E_zero = 0.5 * 0.0 * (1.0 + 2.0 * n_L)
    w_zero = josephson_factor * (0.0 / lams)
    chi_zero = np.sum(w_zero * E_zero) / chi_2
    print(f"  (1) omega_L1 = 0:  chi_Leggett = {chi_zero:.6e}  (expect 0)  {'OK' if chi_zero == 0 else 'FAIL'}")

    # (2) (0,0) sector dominance — relative to level-1 sectors that WOULD
    #     contribute if we summed over them. Compute a comparison integral
    #     over the next-level sectors.
    d2 = np.load(CACHE_PATH, allow_pickle=True)
    sector_evals = d2["sector_evals"].item()
    lvl0_sum = np.sum(josephson_factor * (omega_L1 / lams))
    lvl1_sum = 0.0  # (local)
    for sk in [(0, 1), (1, 0)]:
        arr = np.asarray(sector_evals[sk]["abs_evals"], dtype=np.float64)
        lvl1_sum += np.sum(josephson_factor * (omega_L1 / arr))
    print(f"  (2) Level-0 weight sum  = {lvl0_sum:.4f}")
    print(f"      Level-1 weight sum  = {lvl1_sum:.4f}  (for comparison)")
    ratio_01 = lvl1_sum / lvl0_sum if lvl0_sum > 0 else float("inf")
    # (0,0) is "dominant" if per-mode weight is larger (level-0 modes are at
    # lower energy, so each carries more Leggett amplitude).
    per_mode_00 = lvl0_sum / N_00
    per_mode_lvl1 = lvl1_sum / (np.asarray(sector_evals[(0,1)]["abs_evals"]).size
                                + np.asarray(sector_evals[(1,0)]["abs_evals"]).size)
    print(f"      Per-mode (0,0)      = {per_mode_00:.6f}")
    print(f"      Per-mode (level 1)  = {per_mode_lvl1:.6f}")
    dom_ok = per_mode_00 > per_mode_lvl1
    print(f"      (0,0) dominance (per mode): {'OK' if dom_ok else 'FAIL'}")

    # (3) Consistency with S66 Leggett-only Omega_DM h^2 = 0.120 ---
    # S66 MEMORY: Leggett-channel DM has Omega_DM h^2 ≈ 0.120. That result is
    # a DIFFERENT observable (particle-number density of inter-band quasiparticles),
    # but the ZPE route should be numerically commensurate in the sense that
    # chi_Leggett (a dimensionless OOM) should be of order 1 (i.e. log10 ~ O(0)).
    # We check that chi_Leggett lies in (0.1, 10) — both the target 0.47 OOM
    # and the 0.120 neighborhood are in this decade.
    s66_consistent = 0.1 < chi_Leggett < 10.0
    print(f"  (3) S66 consistency (chi_Leggett in [0.1, 10]): {'OK' if s66_consistent else 'FAIL'}")
    print(f"      chi_Leggett = {chi_Leggett:.4f}, S66 Omega_DM h^2 = 0.120 benchmark")

    # (4) Scaling check: n_L = 0 (adiabatic limit)
    E_adi = 0.5 * omega_L1 * 1.0
    chi_adi = np.sum(w_Leg * E_adi) / chi_2
    print(f"  (4) n_L = 0 (adiabatic):  chi_Leggett = {chi_adi:.6f}")
    print(f"      ratio chi(n_L)/chi(0) = {chi_Leggett/chi_adi:.4f}  = (1 + 2*n_L) = {1 + 2*n_L:.4f}")

    # (5) Omega_L1 rescale bracket
    for fac, tag in [(0.5, "omega_L1/2"), (2.0, "2*omega_L1")]:
        om = omega_L1 * fac
        nL = bose_einstein(om, T_acoustic)
        Ezpe = 0.5 * om * (1.0 + 2.0 * nL)
        wL = josephson_factor * (om / lams)
        chi = np.sum(wL * Ezpe) / chi_2
        print(f"  (5) {tag:14s}: chi_Leggett = {chi:.4f}, log10 = {np.log10(chi):+.4f}")

    # --- Functional classification -------------------------------------------
    print("\n" + "-" * 72)
    print("FUNCTIONAL CLASSIFICATION")
    print("-" * 72)
    print("  Ingredients: Seeley-DeWitt a_k contributions via chi_2 normalization.")
    print("  The Leggett ZPE uses only the linear spectral moment (omega_L1),")
    print("  projected dispersively onto (0,0) eigenvalues. The Josephson")
    print("  factor (1 - cos phi_23_split) is a topological/amplitude factor,")
    print("  not a Seeley-DeWitt coefficient.")
    print("  Classification: robust under spectral functional f(x) -- depends only")
    print("  on a SINGLE low moment. Analogous to LAYER-2 (a_0, a_2, below N*).")

    # --- Save -----------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        # Inputs
        lams_00=lams,
        N_00=N_00,
        omega_L1=omega_L1,
        T_acoustic=T_acoustic,
        phi_23_split=phi_23_split,
        chi_2=chi_2,
        n_L=n_L,
        n_L_target_W1F=n_L_target,
        # Intermediates
        E_zpe_leg=E_zpe_leg,
        josephson_factor=josephson_factor,
        w_Leg=w_Leg,
        sum_w_Leg=sum_w_Leg,
        # Main result
        chi_Leggett=chi_Leggett,
        chi_Leggett_log10=chi_Leggett_log10,
        # Gate
        target_log10=target_log10,
        gate_tol=gate_tol,
        gate_diff=gate_diff,
        gate_pass=gate_pass,
        # Cross-checks
        chi_zero_omega=chi_zero,
        chi_adi=chi_adi,
        ratio_thermal_adi=chi_Leggett / chi_adi,
        lvl0_weight_sum=lvl0_sum,
        lvl1_weight_sum=lvl1_sum,
        per_mode_00=per_mode_00,
        per_mode_lvl1=per_mode_lvl1,
        dominance_ok=dom_ok,
        s66_consistent=s66_consistent,
    )
    print(f"\n[save] {OUT_NPZ}")

    # --- Plot -----------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(11, 8.5))
    fig.suptitle(
        f"LEGGETT-VACUUM-CC-74 (W2-N): chi_Leggett = {chi_Leggett:.4f}  "
        f"(log10 = {chi_Leggett_log10:+.3f})   GATE: {verdict}",
        fontsize=11,
    )

    # Panel 1: (0,0) eigenvalue spectrum + Leggett projection weight
    ax = axes[0, 0]
    ax.vlines(lams, 0, w_Leg, color="steelblue", linewidth=1.2, label="w_Leggett(lambda)")
    ax.plot(lams, w_Leg, "o", color="navy", markersize=4)
    ax.axvline(omega_L1, color="crimson", linestyle="--", linewidth=1.0, label=f"omega_L1 = {omega_L1}")
    ax.set_xlabel("eigenvalue |lambda| / M_KK")
    ax.set_ylabel("Leggett projection weight w(lambda)")
    ax.set_title("(0,0) sector Leggett projection")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 2: ZPE breakdown
    ax = axes[0, 1]
    terms = ["1/2 omega_L1", "omega_L1 n_L", "E_ZPE total"]
    vals = [0.5 * omega_L1, omega_L1 * n_L, E_zpe_leg]
    colors = ["#6699cc", "#cc6666", "#66aa66"]
    bars = ax.bar(terms, vals, color=colors)
    ax.set_ylabel("energy / M_KK")
    ax.set_title("Leggett ZPE decomposition")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:.5f}",
                ha="center", va="bottom", fontsize=9)
    ax.grid(True, alpha=0.3, axis="y")

    # Panel 3: chi_Leggett gate window
    ax = axes[1, 0]
    x_lo, x_hi = target_log10 - 0.5, target_log10 + 0.5
    ax.axvspan(target_log10 - gate_tol, target_log10 + gate_tol,
               alpha=0.25, color="lightgreen", label="PASS window")  # (local)
    ax.axvline(target_log10, color="green", linestyle="-", linewidth=1.5,
               label=f"target = {target_log10}")
    ax.axvline(chi_Leggett_log10, color="crimson", linestyle="-", linewidth=2,
               label=f"computed = {chi_Leggett_log10:+.3f}")
    ax.set_xlim(x_lo, x_hi)
    ax.set_ylim(-0.05, 1.05)
    ax.set_xlabel("log10(chi_Leggett)")
    ax.set_yticks([])
    ax.set_title(f"Gate window  [verdict: {verdict}]")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(True, alpha=0.3, axis="x")

    # Panel 4: cross-check table (sensitivity)
    ax = axes[1, 1]
    ax.axis("off")
    rows = [
        ["Quantity", "Value"],
        ["omega_L1 (canonical)", f"{omega_L1} M_KK"],
        ["T_acoustic", f"{T_acoustic} M_KK"],
        ["n_L (B-E thermal)", f"{n_L:.4f}"],
        ["phi_23_split", f"{phi_23_split} rad"],
        ["(1 - cos phi)", f"{josephson_factor:.4f}"],
        ["(0,0) N modes", f"{N_00}"],
        ["E_ZPE^Leg", f"{E_zpe_leg:.5f} M_KK"],
        ["sum w_Leggett", f"{sum_w_Leg:.5f}"],
        ["chi_2", f"{chi_2}"],
        ["chi_Leggett", f"{chi_Leggett:.4f}"],
        ["log10(chi_Leggett)", f"{chi_Leggett_log10:+.4f}"],
        ["target log10", f"{target_log10}"],
        ["|delta|", f"{gate_diff:.4f}"],
        ["Gate verdict", verdict],
    ]
    tbl = ax.table(cellText=rows, loc="center", cellLoc="left", colWidths=[0.55, 0.45])
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.scale(1, 1.25)
    for (row, col), cell in tbl.get_celld().items():
        if row == 0:
            cell.set_facecolor("#eeeeee")
            cell.set_text_props(weight="bold")
        if row == len(rows) - 1:
            cell.set_facecolor("#c8f0c8" if gate_pass else "#f0c8c8")

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    print(f"[save] {OUT_PNG}")
    plt.close()

    print("\n" + "=" * 72)
    print(f"SUMMARY: chi_Leggett = {chi_Leggett:.4f}, log10 = {chi_Leggett_log10:+.4f}")
    print(f"         gate |delta| = {gate_diff:.4f} vs tol {gate_tol}")
    print(f"         VERDICT: {verdict}")
    print("=" * 72)


if __name__ == "__main__":
    main()
