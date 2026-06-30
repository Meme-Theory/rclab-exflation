"""
S74 W4-P: MOTT-GAP-RENORMALIZATION-74 -- M_KK -> Present Horizon

S74-CF-8. Compute the Mott charging gap E_C = 0.464 M_KK at the fold and
propagate its physical value forward to "today" via the canonical
EFOLD-MAPPING-73B expansion history (N_total = 132.45 e-folds from fold to
today). Report the present-day Mott gap in GeV, eV, and Planck units, and
classify into detector-range buckets.

Pre-registered gate
-------------------
MOTT-GAP-RENORMALIZATION-74:
  PASS  -- present-day gap is identified in at least one of {GeV, eV, Planck}
  FAIL  -- the rescaling is undefined (missing N_total or E_C)

Physical framing
----------------
In the substrate picture, the Mott gap E_C is an excitation gap of the
BCS/Josephson network on CG(24). Its fold-local value is the charging energy
per pair-addition on a single 24-cell coset unit, E_C = 0.4643 M_KK (S66
ROUTE2-OES). The fabric itself is not "in" space; space is an emergent
description of the fabric's spectral weight. As the fabric's emergent scale
factor grows by exp(N_total) between fold and today, the physical frequency
of any gapped mode redshifts the same way as any other frequency in the
emergent FRW background:

    omega_phys(t) = omega_fold * (a_fold / a_today)

This single-power-of-a redshift is the universal "frequency-like" scaling: it
follows from the fact that the gap is an eigenvalue of a first-order operator
(Dirac / Josephson), so its dimensions are (length)^{-1} in the emergent
metric, and a length scales as a(t). Landau's 1941 two-fluid framework
treats gapped excitations (phonons, rotons) as quasiparticles whose
dispersion E(p) has both a rest-mass-like constant piece and a momentum
piece that scale together as the medium's "sound scale" redshifts; the
gap and the sound speed renormalize with the same power. That universal
scaling is what we apply here.

We also report two alternative scalings for completeness:
  - a^{-2} (kinetic / mass-like): the rest-mass scaling of a non-relativistic
    kinetic energy E_kin = p^2/2m where p ~ 1/a.
  - a^0    (frozen / no redshift): the limit in which E_C is a rest mass and
    decouples from the cosmological scale factor. This is the "Mott DM as
    pinned charging energy" reading and corresponds to treating E_C as a
    mass scale that is protected by an internal symmetry from rescaling.
All three are reported so the downstream A_s / DM analysis can choose among
them, but the canonical "horizon"-normalized answer is the a^{-1} scaling.

Verdict
-------
This computation is structural: the rescaling is well-defined because
N_total is finite and E_C is canonical. Gate PASSES.
"""

import sys
from pathlib import Path

# Make canonical_constants importable regardless of CWD
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import numpy as np  # noqa: E402
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from canonical_constants import (  # noqa: E402
    M_KK,
    Delta_0_OES,
    M_Pl_reduced,
    M_Pl_unreduced,
    H_0_GeV,
    hbar_c_GeV_m,
    l_Planck,
    t_universe_s,
    t_Planck,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Inputs: fold-local Mott gap and EFOLD-MAPPING-73B expansion history
# ---------------------------------------------------------------------------

# Fold-local Mott charging gap (S66 ROUTE2-OES canonical, confirmed W1-D S74)
E_C_fold_MKK = Delta_0_OES  # = 0.4642547394830737 M_KK (canonical alias)

E_C_fold_GeV = E_C_fold_MKK * M_KK  # (local) -- in GeV

# Expansion history: EFOLD-MAPPING-73B npz
EFOLD_NPZ = _HERE / "s73b_efold_mapping.npz"
if not EFOLD_NPZ.exists():
    raise FileNotFoundError(
        f"EFOLD-MAPPING-73B data file not found at {EFOLD_NPZ}. "
        "Rerun computations/session-73/s73b_efold_mapping.py first."
    )
efold = np.load(EFOLD_NPZ)
N_total = float(efold["N_total"])  # (local) -- e-folds fold -> today
H_fold_GeV = float(efold["H_phys_fold_GeV"])  # (local) -- physical H at fold
z_fold = float(efold["z_fold"])  # (local)

# Scale-factor ratios
a_ratio_fold_today = float(np.exp(-N_total))  # (local) a_fold / a_today
a_ratio_today_fold = float(np.exp(+N_total))  # (local) a_today / a_fold

# ---------------------------------------------------------------------------
# Three scaling assumptions for the Mott gap
#     (1) a^{-1}  -- universal frequency / gap-like (CANONICAL)
#     (2) a^{-2}  -- kinetic / p^2/2m-like
#     (3) a^{ 0}  -- pinned / rest-mass-like (NO redshift)
# ---------------------------------------------------------------------------

scalings = {
    "a^-1_frequency": a_ratio_fold_today ** 1,
    "a^-2_kinetic":   a_ratio_fold_today ** 2,
    "a^0_pinned":     a_ratio_fold_today ** 0,
}

# Today's Mott gap under each scaling, in GeV
E_C_today_GeV = {
    label: E_C_fold_GeV * s for label, s in scalings.items()
}

# Conversions
def gev_to_ev(x):
    return x * 1.0e9

def gev_to_planck_reduced(x):
    return x / M_Pl_reduced

def gev_to_planck_unreduced(x):
    return x / M_Pl_unreduced

# Build the output table
print("=" * 78)
print("S74 W4-P  MOTT-GAP-RENORMALIZATION-74")
print("=" * 78)
print()
print("Inputs")
print("------")
print(f"  E_C_fold (Mott charging gap, Route 2 OES)")
print(f"      = {E_C_fold_MKK:.10f} M_KK")
print(f"      = {E_C_fold_GeV:.6e} GeV")
print(f"  M_KK (gravity route, S42)  = {M_KK:.6e} GeV")
print(f"  M_Pl_reduced               = {M_Pl_reduced:.6e} GeV")
print(f"  M_Pl_unreduced             = {M_Pl_unreduced:.6e} GeV")
print(f"  tau_fold                   = {tau_fold}")
print()
print("EFOLD-MAPPING-73B canonical expansion history")
print("---------------------------------------------")
print(f"  N_total  (fold -> today)   = {N_total:.6f}")
print(f"  a_fold / a_today           = {a_ratio_fold_today:.6e}")
print(f"  a_today / a_fold           = {a_ratio_today_fold:.6e}")
print(f"  z_fold                     = {z_fold:.6e}")
print(f"  H_fold (physical)          = {H_fold_GeV:.6e} GeV")
print()
print("Present-day Mott gap under three redshift assumptions")
print("------------------------------------------------------")
header = (
    f"  {'scaling':<20s} {'E_C_today [GeV]':>22s} "
    f"{'[eV]':>16s} {'[M_Pl_red]':>16s}"
)
print(header)
print("  " + "-" * (len(header) - 2))
for label, E_today_GeV in E_C_today_GeV.items():
    E_today_eV = gev_to_ev(E_today_GeV)  # (local)
    E_today_MPl = gev_to_planck_reduced(E_today_GeV)  # (local)
    print(
        f"  {label:<20s} {E_today_GeV:>22.6e} "
        f"{E_today_eV:>16.6e} {E_today_MPl:>16.6e}"
    )
print()

# Detector-range classification under the canonical a^{-1} scaling
E_C_today_canonical_GeV = E_C_today_GeV["a^-1_frequency"]
E_C_today_canonical_eV = gev_to_ev(E_C_today_canonical_GeV)

# Detector bands (conventional particle-DM energy windows)
DETECTOR_BANDS = [
    ("ultralight",            1e-33,   1e-12, "eV"),   # fuzzy DM, ultralight
    ("axion / sub-eV",        1e-12,   1e-3,  "eV"),
    ("eV / keV (warm DM)",    1e-3,    1e3,   "eV"),
    ("keV / MeV (light DM)",  1e3,     1e6,   "eV"),
    ("MeV / GeV (WIMP-lite)", 1e6,     1e9,   "eV"),
    ("GeV / TeV (WIMP)",      1e9,     1e12,  "eV"),
    ("TeV / PeV",             1e12,    1e15,  "eV"),
]

def classify_eV(E_eV):
    for name, lo, hi, _units in DETECTOR_BANDS:
        if (E_eV >= lo) and (E_eV < hi):
            return name
    if E_eV < DETECTOR_BANDS[0][1]:
        return "below detector floor"
    return "above detector ceiling"

band_canonical = classify_eV(E_C_today_canonical_eV)
print("Canonical (a^-1) detector-range classification")
print("-----------------------------------------------")
print(f"  E_C_today (canonical, a^-1) = {E_C_today_canonical_GeV:.6e} GeV")
print(f"                              = {E_C_today_canonical_eV:.6e} eV")
print(f"  Detector band               = {band_canonical}")
print()

# Also report the two alternatives' bands
for label in ("a^-2_kinetic", "a^0_pinned"):
    E_today_GeV = E_C_today_GeV[label]
    E_today_eV = gev_to_ev(E_today_GeV)  # (local)
    print(
        f"  {label:<20s}  E_today = {E_today_GeV:.6e} GeV "
        f"= {E_today_eV:.6e} eV  --  {classify_eV(E_today_eV)}"
    )
print()

# ---------------------------------------------------------------------------
# Cross-checks
# ---------------------------------------------------------------------------

# (1) Comparison to H_0 today
H_0_today_GeV = H_0_GeV  # (local) -- 1.438e-42 GeV (canonical Planck 2018)
ratio_EC_over_H0_canonical = E_C_today_canonical_GeV / H_0_today_GeV  # (local)

# (2) Comparison to H_fold (same ratio at fold should be >> 1)
ratio_EC_over_H_fold = E_C_fold_GeV / H_fold_GeV  # (local)

# (3) Sanity: E_C_today * exp(N_total) should equal E_C_fold (invertibility)
invert_check = E_C_today_canonical_GeV * a_ratio_today_fold  # (local)
invert_rel_err = abs(invert_check - E_C_fold_GeV) / E_C_fold_GeV  # (local)

# (4) Frequency equivalents
GeV_to_Hz = 1.5193e24  # (local) GeV -> s^-1 = Hz (natural units)
f_C_fold_Hz = E_C_fold_GeV * GeV_to_Hz  # (local)
f_C_today_Hz = E_C_today_canonical_GeV * GeV_to_Hz  # (local)

# (5) Wavelength equivalents (Compton-like)
lambda_C_fold_m = hbar_c_GeV_m / E_C_fold_GeV  # (local)
lambda_C_today_m = hbar_c_GeV_m / E_C_today_canonical_GeV  # (local)
Hubble_radius_today_m = 1.0 / (H_0_inv_s_check := 2.184e-18)  # (local) c*1/H_0
Hubble_radius_today_m *= 2.998e8
# (Above is c/H_0 in m; equivalent to ~1.37e26 m. Check below.)

# (6) Compare a^-1 mode wavelength today to the Hubble radius
# A wavelength that redshifted from lambda_C_fold_m by a_ratio_today_fold:
lambda_mode_today_m = lambda_C_fold_m * a_ratio_today_fold  # (local)

print("Cross-checks")
print("------------")
print(f"  (1) E_C_today / H_0           = {ratio_EC_over_H0_canonical:.6e}")
print(f"      E_C_fold  / H_fold        = {ratio_EC_over_H_fold:.6e}")
print(f"  (2) Invert: E_C_today*a_ratio = {invert_check:.6e} GeV")
print(f"      vs E_C_fold                = {E_C_fold_GeV:.6e} GeV")
print(f"      relative error             = {invert_rel_err:.3e}")
print(f"  (3) f_C_fold   = {f_C_fold_Hz:.6e} Hz")
print(f"      f_C_today  = {f_C_today_Hz:.6e} Hz")
print(f"  (4) lambda_C_fold   = {lambda_C_fold_m:.6e} m")
print(f"      lambda_C_today  = {lambda_C_today_m:.6e} m  (Compton at E_today)")
print(f"      lambda_mode_today (redshifted) = {lambda_mode_today_m:.6e} m")
print(f"      Hubble radius today c/H_0      = {Hubble_radius_today_m:.6e} m")
print()

# ---------------------------------------------------------------------------
# Gate verdict
# ---------------------------------------------------------------------------

def is_finite(x):
    return np.isfinite(x) and (x > 0.0)

units_identified = []  # (local)
if is_finite(E_C_today_canonical_GeV):
    units_identified.append("GeV")
if is_finite(gev_to_ev(E_C_today_canonical_GeV)):
    units_identified.append("eV")
if is_finite(gev_to_planck_reduced(E_C_today_canonical_GeV)):
    units_identified.append("Planck (reduced)")
if is_finite(gev_to_planck_unreduced(E_C_today_canonical_GeV)):
    units_identified.append("Planck (unreduced)")

gate_name = "MOTT-GAP-RENORMALIZATION-74"  # (local)
if len(units_identified) >= 1 and is_finite(N_total) and N_total > 0:
    gate_verdict = "PASS"  # (local)
    gate_detail = (
        f"E_C_today identified in {len(units_identified)} units: "
        + ", ".join(units_identified)
        + f". Rescaling well-defined (N_total = {N_total:.4f})."
    )  # (local)
else:
    gate_verdict = "FAIL"  # (local)
    gate_detail = "Rescaling undefined (missing N_total or E_C)."  # (local)

print("Gate verdict")
print("------------")
print(f"  {gate_name}")
print(f"  verdict: {gate_verdict}")
print(f"  detail : {gate_detail}")
print()

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Panel 1: E_C vs N_e (from fold N_e=0 to today N_e=N_total) for 3 scalings
Ne_axis = np.linspace(0.0, N_total, 500)  # (local)
E_C_axis_a1 = E_C_fold_GeV * np.exp(-1.0 * Ne_axis)  # (local)
E_C_axis_a2 = E_C_fold_GeV * np.exp(-2.0 * Ne_axis)  # (local)
E_C_axis_a0 = np.full_like(Ne_axis, E_C_fold_GeV)  # (local)

ax = axes[0]
ax.semilogy(Ne_axis, E_C_axis_a1, label=r"$a^{-1}$ (frequency, canonical)", lw=2.0)
ax.semilogy(Ne_axis, E_C_axis_a2, label=r"$a^{-2}$ (kinetic / p$^2$/2m)", lw=1.5, ls="--")
ax.semilogy(Ne_axis, E_C_axis_a0, label=r"$a^{0}$ (pinned / rest mass)", lw=1.5, ls=":")
ax.axvline(x=N_total, color="k", lw=0.8, alpha=0.5)
ax.axhline(y=H_0_GeV, color="r", lw=0.8, alpha=0.5)
ax.annotate(
    f"today\n$N_e$={N_total:.2f}",
    xy=(N_total, E_C_fold_GeV * 1e-30),
    xytext=(N_total * 0.7, E_C_fold_GeV * 1e-20),
    arrowprops=dict(arrowstyle="->", alpha=0.5),
)
ax.annotate(
    f"$H_0={H_0_GeV:.1e}$ GeV",
    xy=(2.0, H_0_GeV),
    xytext=(5.0, H_0_GeV * 1e4),
    fontsize=8,
)
ax.set_xlabel("e-folds from fold, $N_e$")
ax.set_ylabel(r"$E_C(N_e)$ [GeV]")
ax.set_title("Mott charging gap vs e-fold")
ax.legend(fontsize=9)
ax.grid(True, which="both", alpha=0.3)

# Panel 2: Detector bands in eV, with E_C_today markers under each scaling
ax = axes[1]
ax.set_yscale("log")
for i, (name, lo, hi, _units) in enumerate(DETECTOR_BANDS):
    ax.fill_betweenx([lo, hi], i - 0.4, i + 0.4, alpha=0.2, edgecolor="k")
    mid = np.sqrt(lo * hi)  # (local)
    ax.text(
        i,
        mid,
        name,
        ha="center",
        va="center",
        fontsize=8,
        rotation=0,
    )
ax.set_xticks(range(len(DETECTOR_BANDS)))
ax.set_xticklabels([b[0] for b in DETECTOR_BANDS], rotation=25, ha="right", fontsize=8)
for label, style in [
    ("a^-1_frequency", ("o", "C0", "canonical $a^{-1}$")),
    ("a^-2_kinetic",   ("s", "C1", "kinetic $a^{-2}$")),
    ("a^0_pinned",     ("^", "C2", "pinned $a^{0}$")),
]:
    marker, color, nice = style
    y = gev_to_ev(E_C_today_GeV[label])  # (local)
    ax.scatter(
        [len(DETECTOR_BANDS) / 2.0],
        [y],
        marker=marker,
        color=color,
        s=80,
        label=f"{nice}: {y:.2e} eV",
        zorder=5,
    )
ax.set_ylabel(r"$E_C$ today [eV]")
ax.set_title("Present-day Mott gap vs DM detector bands")
ax.legend(loc="lower right", fontsize=8)
ax.grid(True, which="both", alpha=0.3)

plt.suptitle(
    f"S74 W4-P MOTT-GAP-RENORMALIZATION-74  |  "
    f"$E_C^{{\\rm fold}} = {E_C_fold_MKK:.4f}\\,M_{{\\rm KK}}$, "
    f"$N_e = {N_total:.2f}$,  verdict: {gate_verdict}",
    fontsize=11,
)
plt.tight_layout()

OUT_PNG = _HERE / "s74_mott_gap_renormalization.png"
fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
plt.close(fig)
print(f"Plot saved: {OUT_PNG}")

# ---------------------------------------------------------------------------
# Save npz
# ---------------------------------------------------------------------------

OUT_NPZ = _HERE / "s74_mott_gap_renormalization.npz"

np.savez(
    OUT_NPZ,
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Inputs
    E_C_fold_MKK=E_C_fold_MKK,
    E_C_fold_GeV=E_C_fold_GeV,
    M_KK_GeV=M_KK,
    M_Pl_reduced_GeV=M_Pl_reduced,
    M_Pl_unreduced_GeV=M_Pl_unreduced,
    tau_fold=tau_fold,
    # Expansion history
    N_total_efolds=N_total,
    a_ratio_fold_today=a_ratio_fold_today,
    a_ratio_today_fold=a_ratio_today_fold,
    z_fold=z_fold,
    H_fold_GeV=H_fold_GeV,
    H_0_GeV=H_0_GeV,
    # Rescaling factors per scaling
    rescale_a_minus_1=scalings["a^-1_frequency"],
    rescale_a_minus_2=scalings["a^-2_kinetic"],
    rescale_a_0=scalings["a^0_pinned"],
    # Present-day gap, three scalings x three units
    E_C_today_a1_GeV=E_C_today_GeV["a^-1_frequency"],
    E_C_today_a1_eV=gev_to_ev(E_C_today_GeV["a^-1_frequency"]),
    E_C_today_a1_MPl_reduced=gev_to_planck_reduced(E_C_today_GeV["a^-1_frequency"]),
    E_C_today_a1_MPl_unreduced=gev_to_planck_unreduced(E_C_today_GeV["a^-1_frequency"]),
    E_C_today_a2_GeV=E_C_today_GeV["a^-2_kinetic"],
    E_C_today_a2_eV=gev_to_ev(E_C_today_GeV["a^-2_kinetic"]),
    E_C_today_a2_MPl_reduced=gev_to_planck_reduced(E_C_today_GeV["a^-2_kinetic"]),
    E_C_today_a2_MPl_unreduced=gev_to_planck_unreduced(E_C_today_GeV["a^-2_kinetic"]),
    E_C_today_a0_GeV=E_C_today_GeV["a^0_pinned"],
    E_C_today_a0_eV=gev_to_ev(E_C_today_GeV["a^0_pinned"]),
    E_C_today_a0_MPl_reduced=gev_to_planck_reduced(E_C_today_GeV["a^0_pinned"]),
    E_C_today_a0_MPl_unreduced=gev_to_planck_unreduced(E_C_today_GeV["a^0_pinned"]),
    # Cross-checks
    ratio_EC_over_H0_canonical=ratio_EC_over_H0_canonical,
    ratio_EC_over_H_fold=ratio_EC_over_H_fold,
    invert_check_GeV=invert_check,
    invert_rel_err=invert_rel_err,
    f_C_fold_Hz=f_C_fold_Hz,
    f_C_today_Hz=f_C_today_Hz,
    lambda_C_fold_m=lambda_C_fold_m,
    lambda_C_today_m=lambda_C_today_m,
    lambda_mode_today_m=lambda_mode_today_m,
    # Classification
    band_canonical=band_canonical,
    units_identified=np.array(units_identified),
    detector_bands=np.array([b[0] for b in DETECTOR_BANDS]),
    detector_lows_eV=np.array([b[1] for b in DETECTOR_BANDS]),
    detector_highs_eV=np.array([b[2] for b in DETECTOR_BANDS]),
)
print(f"Data saved: {OUT_NPZ}")

print()
print("=" * 78)
print(f"S74 W4-P MOTT-GAP-RENORMALIZATION-74  verdict = {gate_verdict}")
print("=" * 78)
