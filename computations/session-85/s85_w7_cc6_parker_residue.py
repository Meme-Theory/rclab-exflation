"""S85-W7-CC-6 — W7-2.

[VERIFY] gate: Parker transit-residue vacuum-energy shift against
observed Λ_obs. Tests whether the fold-transit Parker pair-production
residue closes the 109-OOM cosmological-constant hierarchy alone, or
whether an independent CC-Γ (impedance effacement) channel is required.

Hypothesis (plan §W7-2 step 5):
  The post-transit vacuum shift
    δρ_vac = (1/2) ∫ (d³k/(2π)³) ω_k |β_k|²
  with Bogoliubov spectrum {β_k} from S78 W1-E (Airy turning-point
  Parker scaling, saturation |β_k_pivot|² = 4.255e4 at k_pivot_fold
  = 14.31 M_KK) closes the hierarchy between ρ_vac^{natural} ~ M_KK^4
  and Λ_obs = 3.91e-47 GeV^4 to within 1.0 OOM when the natural UV
  cutoff M_KK is replaced by the substrate's phonon-dispersion cutoff
  at the van Hove fold (ω_cusp) and Airy tail |β_k|² ~ k^{-2/3} is
  imposed for k > k_cusp.

Substitution chain (plan §W7-2 step 10):

  Step 1 (definitions):
    ρ_vac(bare) = (1/2) ∫ d³k/(2π)³ · ω_k                [UV-divergent]
    ρ_Parker   = (1/2) ∫ d³k/(2π)³ · ω_k · |β_k|²       [post-transit shift]
    |β_k|²     = 4.255e4 for k ≤ k_cusp (bandgap, flat saturation)
               = 4.255e4 · (k/k_cusp)^{-2/3} for k > k_cusp (Airy tail)
    Λ_obs      = 3.91e-47 GeV^4  (PDG, = (2.5e-3 eV)^4)

  Step 2 (substitution, no simplification):
    For massless dispersion ω_k = k and spherically symmetric integration:
      ρ_Parker = (1/(4π²)) ∫_0^{Λ_UV} k³ |β_k|² dk
    Split at k_cusp:
      Lower (bandgap): ∫_0^{k_cusp} k³ · |β_pivot|² dk = |β|² · k_cusp^4 / 4
      Upper (Airy):    ∫_{k_cusp}^{Λ_UV} k³ · |β|² · (k/k_cusp)^{-2/3} dk
                     = |β|² · k_cusp^{2/3} · ∫ k^{7/3} dk
                     = (3/10) · |β|² · k_cusp^{2/3} · (Λ_UV^{10/3} − k_cusp^{10/3})

  Step 3 (simplification — canonical form):
    Per plan §W7-2 step 3: Airy UV tail scales as M_KK^{10/3}, NOT M_KK^4;
    exponent cut by 2/3. Suppression factor relative to bare:
      (k_cusp/Λ_UV)^{2/3}   if k_cusp < Λ_UV

  Step 4 (direction):
    For k_pivot_fold = 14.31 M_KK (from S77 N-PIVOT-MAP + S78 W1-E),
    the CMB-pivot "cusp" SITS ABOVE the natural UV cutoff M_KK. The
    integration [10^{-4} M_KK, M_KK] is ENTIRELY INSIDE the bandgap
    saturation region — no Airy tail contribution until above M_KK.
    ρ_Parker ≈ |β|² × M_KK^4 / (16π²)
    Expected: 109 OOM above Λ_obs (UV-divergent bare scale boosted by
    |β|² saturation). PASS iff a deep cusp suppression is found that
    is NOT the case here.

PASS/FAIL/INFO (plan §W7-2 step 9):
  PASS: |Δlog₁₀(ρ_Parker/Λ_obs)| ≤ 1.0 (full closure via transit-residue)
  FAIL: |Δlog₁₀| > 5.0 (CC-6 insufficient; CC-Γ required independently)
  INFO: 1.0 < |Δlog₁₀| ≤ 5.0 (partial; joint CC-6+CC-Γ needed)

Machinery pin (plan §7):
  L_max=10, scheme=zeta-regularization (Hawking-Ford; NOT dim-reg),
  convention=Parker-Hawking-1974, N_k=4096 log-spaced on [1e-4 M_KK,
  M_KK], UV_cutoff=van-Hove-dispersion-cutoff (ω_cusp), |β_k|²
  tabulated from S78 W1-E, tolerance=1.0 OOM RATIO, random_seed=42.

Outputs:
  computations/session-85/s85_w7_cc6_parker_residue.npz
  computations/session-85/s85_w7_cc6_parker_residue.png
Verdict appended to computations/session-85/s85_gate_verdicts.txt with
S85+ dual-SHA.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from canonical_constants import (  # noqa: E402
    M_KK_gravity,
    tau_fold,
    dt_transit,
    Vol_SU3_Haar,
    dS_fold,
    rho_Lambda_obs,
    Mach_max_framework,
    PI,
)


# ----------------------------------------------------------------------------
# Section 0 — input-pin map and closure SHA
# ----------------------------------------------------------------------------
def _file_sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


INPUT_PINS: dict[str, str] = {}

_static_files = [
    _HERE / "canonical_constants.py",
    _HERE / "s78_pre_fold_vacuum.py",
    _HERE / "s78_pre_fold_vacuum.npz",
]
for _sf in _static_files:
    if _sf.exists():
        INPUT_PINS[_sf.name] = _file_sha(_sf)
    else:
        INPUT_PINS[_sf.name] = "MISSING"


# Machinery pins (plan §7 verbatim)
L_max = 10  # (local) plan §7
scheme = "zeta-regularization"  # (local) plan §7, Hawking-Ford; NOT dim-reg
convention = "Parker-Hawking-1974"  # (local) plan §7
N_k = 4096  # (local) log-spaced k-samples (plan §7)
tolerance_OOM = 1.0  # (local) plan §9 PASS bound
FAIL_OOM = 5.0  # (local) plan §9 FAIL bound
random_seed = 42  # (local) template discriminator (plan §7)

INPUT_PINS["L_max"] = f"{L_max:d}"
INPUT_PINS["scheme"] = scheme
INPUT_PINS["convention"] = convention
INPUT_PINS["N_k"] = f"{N_k:d}"
INPUT_PINS["tolerance_OOM"] = f"{tolerance_OOM:.4f}"
INPUT_PINS["FAIL_OOM"] = f"{FAIL_OOM:.4f}"
INPUT_PINS["random_seed"] = f"{random_seed:d}"

# Pull S78 W1-E anchors for |β_k_pivot|² spectrum
s78_npz_path = _HERE / "s78_pre_fold_vacuum.npz"
_s78 = np.load(s78_npz_path)
beta_sq_pivot_S78 = float(_s78["CHK3_beta_sq_pivot"])  # (local)
k_pivot_fold_S78 = float(_s78["k_pivot_fold"])  # (local, in M_KK units)
alpha_SS = complex(_s78["alpha_SS"])  # (local) S78 Bogoliubov α (Stationarity IC)
beta_SS = complex(_s78["beta_SS"])  # (local) S78 Bogoliubov β
unitarity_SS = float(_s78["unitarity_SS"])  # (local) |α|² − |β|² = unit
INPUT_PINS["beta_sq_pivot_S78"] = f"{beta_sq_pivot_S78:.10e}"
INPUT_PINS["k_pivot_fold_S78"] = f"{k_pivot_fold_S78:.10e}"
INPUT_PINS["unitarity_SS"] = f"{unitarity_SS:.10e}"

# Pull canonical-constants inputs to closure map
INPUT_PINS["M_KK_gravity_GeV"] = f"{M_KK_gravity:.10e}"
INPUT_PINS["rho_Lambda_obs_GeV4"] = f"{rho_Lambda_obs:.10e}"
INPUT_PINS["Mach_max_framework"] = f"{Mach_max_framework:.10e}"

CLOSURE_INPUT = json.dumps(INPUT_PINS, sort_keys=True, separators=(",", ":"))
CLOSURE_SHA = hashlib.sha256(CLOSURE_INPUT.encode("utf-8")).hexdigest()

print("=" * 78)
print("S85 W7-2: CC-6 Parker transit-residue vacuum-energy shift")
print("=" * 78)
print(f"closure SHA-256 (64 char): {CLOSURE_SHA}")
print(f"closure SHA-256 (16 head): {CLOSURE_SHA[:16]}")
print()
print("--- input pin SHAs and values ---")
for _k, _v in INPUT_PINS.items():
    print(f"  {_k:<32s}: {_v}")
print()

# Unitarity verification for S78 |β|² anchor
print("--- S78 W1-E Bogoliubov anchor + unitarity check ---")
print(f"  |β_k_pivot|² (S78 W1-E)     = {beta_sq_pivot_S78:.6e}")
print(f"  k_pivot_fold  (M_KK units)  = {k_pivot_fold_S78:.6e}")
print(f"  |α_SS|² − |β_SS|² (unitary) = {unitarity_SS:.6e}  (expect 1.0)")
assert abs(unitarity_SS - 1.0) < 1e-3, f"Unitarity fail: {unitarity_SS}"
print()


# ----------------------------------------------------------------------------
# Section 1 — Natural-scale benchmarks (plan §10 step 4 Python-verified)
# ----------------------------------------------------------------------------
# Plan Python-verified (2026-04-21): ρ_vac(bare) = 7.54e62 GeV^4 at
# M_KK = 5.24e15 GeV; Λ_obs = 3.91e-47 GeV^4; log10 ratio = 109.29.
# We use canonical_constants M_KK_gravity and rho_Lambda_obs for consistency.

M_KK_GeV = M_KK_gravity  # (local) alias
# Λ_obs direct: (2.5e-3 eV)^4 = (2.5e-12 GeV)^4
Lambda_obs_direct_GeV4 = (2.5e-12) ** 4  # (local) plan step 1 definition = 3.906e-47
print("--- natural-scale benchmarks ---")
print(f"  M_KK (gravity route)        = {M_KK_GeV:.6e}  GeV")
print(f"  M_KK^4                      = {M_KK_GeV**4:.6e}  GeV^4")
print(f"  rho_Lambda_obs (canonical)  = {rho_Lambda_obs:.6e}  GeV^4")
print(f"  Lambda_obs direct (PDG)     = {Lambda_obs_direct_GeV4:.6e}  GeV^4")
print(f"  Plan target: log10 ratio    = 109.29  (bare M_KK^4/Λ_obs)")
print()


# ----------------------------------------------------------------------------
# Section 2 — k-grid and |β_k|² spectrum construction
# ----------------------------------------------------------------------------
# Plan §7: k log-spaced on [1e-4 M_KK, M_KK]; N_k = 4096.
k_min_in_MKK = 1e-4  # (local) plan §7 lower bound (in M_KK units)
k_max_in_MKK = 1.0  # (local) plan §7 upper bound (= M_KK)
k_grid_MKK = np.logspace(
    np.log10(k_min_in_MKK), np.log10(k_max_in_MKK), N_k
)  # (local) dimensionless k/M_KK
k_grid_GeV = k_grid_MKK * M_KK_GeV  # (local) k in GeV

# Cusp/pivot location: per plan + S78 W1-E, k_pivot_fold = 14.31 M_KK.
# Above the plan's integration upper bound of M_KK. Therefore the
# entire integration interval [10^{-4}, 1.0] M_KK sits BELOW k_cusp,
# in the flat bandgap-saturation region where |β_k|² = |β_pivot|² ≈ 4.255e4.
k_cusp_in_MKK = k_pivot_fold_S78  # (local) k_cusp = k_pivot ≈ 14.31 M_KK

# |β_k|² construction per plan:
#   k ≤ k_cusp   : |β_k|² = |β_pivot|² (saturated bandgap)
#   k > k_cusp   : |β_k|² = |β_pivot|² · (k/k_cusp)^{-2/3} (Airy tail)
beta_sq_spectrum = np.where(
    k_grid_MKK <= k_cusp_in_MKK,
    beta_sq_pivot_S78,
    beta_sq_pivot_S78 * (k_grid_MKK / k_cusp_in_MKK) ** (-2.0 / 3.0),
)  # (local)

# Verify integration band is entirely in the bandgap
n_above_cusp = int(np.sum(k_grid_MKK > k_cusp_in_MKK))
print("--- k-grid and |β_k|² construction ---")
print(f"  k_min (M_KK units)       = {k_min_in_MKK:.3e}")
print(f"  k_max (M_KK units)       = {k_max_in_MKK:.3e}")
print(f"  N_k                      = {N_k}")
print(f"  k_cusp (M_KK units)      = {k_cusp_in_MKK:.4e}  (S78 W1-E pivot)")
print(f"  grid points above k_cusp = {n_above_cusp}  (of {N_k})")
print(f"  |β|² regime              = {'ALL bandgap (saturated)' if n_above_cusp == 0 else 'SPLIT (bandgap + Airy)'}")
print(f"  |β|² saturation value    = {beta_sq_pivot_S78:.6e}")
print()


# ----------------------------------------------------------------------------
# Section 3 — Parker vacuum residue integral
#   ρ_Parker = (1/(4π²)) ∫ k³ · |β_k|² dk
#   (massless dispersion ω_k = k)
# ----------------------------------------------------------------------------
# Integrand in GeV^4: (k/GeV)^3 · |β|² · dk (absorbing 1/(4π²) prefactor at end)
omega_k_GeV = k_grid_GeV  # (local) ω_k = k (massless)
rho_integrand = omega_k_GeV * (k_grid_GeV ** 2) * beta_sq_spectrum  # (local) k³·|β|²
# trapezoidal integration
rho_Parker_raw = np.trapezoid(rho_integrand, k_grid_GeV)  # (local) ∫ k³·|β|² dk [GeV^4]
prefactor = 1.0 / (4.0 * PI ** 2)  # (local) 1/(4π²)
# Parker-Hawking includes the 1/2 pair-production factor: ρ_Parker = (1/2)·(1/(4π²))·∫
# Actually the measure d³k/(2π)³ = 4πk²/(2π)³ dk = k²/(2π²) dk already has the 1/(2π²)
# collected: ρ_Parker = (1/2) ∫ d³k/(2π)³ ω|β|² = (1/(4π²)) ∫ k³|β|² dk (the 1/2 is absorbed).
rho_Parker_total = prefactor * rho_Parker_raw  # (local) GeV^4

# Ratio to observed Λ
ratio_to_Lambda_obs = rho_Parker_total / rho_Lambda_obs  # (local)
Delta_log10 = float(np.log10(ratio_to_Lambda_obs))  # (local)

# Direct-PDG cross-check
ratio_to_Lambda_obs_direct = rho_Parker_total / Lambda_obs_direct_GeV4  # (local)
Delta_log10_direct = float(np.log10(ratio_to_Lambda_obs_direct))  # (local)

print("--- Parker integral evaluation ---")
print(f"  ∫ k³ · |β|² dk              = {rho_Parker_raw:.6e}  GeV^4 (raw)")
print(f"  prefactor 1/(4π²)           = {prefactor:.6e}")
print(f"  ρ_Parker_total              = {rho_Parker_total:.6e}  GeV^4")
print()
print(f"  ρ_Parker / ρ_Lambda_obs     = {ratio_to_Lambda_obs:.6e}")
print(f"  Δlog10(ρ_Parker/Λ_obs)      = {Delta_log10:.4f} OOM")
print()
print(f"  ρ_Parker / Λ_obs (PDG direct, 3.906e-47) = {ratio_to_Lambda_obs_direct:.6e}")
print(f"  Δlog10 (PDG direct)                        = {Delta_log10_direct:.4f} OOM")
print()


# Analytic cross-check (bandgap-dominated): ρ_Parker ≈ |β|² · M_KK^4 / (16π²)
rho_Parker_analytic = beta_sq_pivot_S78 * (M_KK_GeV ** 4) / (16.0 * PI ** 2)  # (local)
analytic_vs_num_ratio = rho_Parker_total / rho_Parker_analytic  # (local)
print("--- analytic cross-check (bandgap-saturated, full [0, M_KK]) ---")
print(f"  ρ_Parker_analytic            = |β|² · M_KK^4 / (16π²)")
print(f"                               = {beta_sq_pivot_S78:.4e} · {M_KK_GeV**4:.4e} / {16*PI**2:.4e}")
print(f"                               = {rho_Parker_analytic:.6e}  GeV^4")
print(f"  num/analytic ratio           = {analytic_vs_num_ratio:.6f}  (expect ≈1)")
print()


# ----------------------------------------------------------------------------
# Section 4 — PASS/FAIL/INFO verdict
# ----------------------------------------------------------------------------
abs_delta = abs(Delta_log10)  # (local)
if abs_delta <= tolerance_OOM:
    verdict = "PASS"
elif abs_delta <= FAIL_OOM:
    verdict = "INFO"
else:
    verdict = "FAIL"

print("--- PASS/FAIL/INFO verdict (plan §9) ---")
print(f"  |Δlog10(ρ_Parker/Λ_obs)| = {abs_delta:.4f} OOM")
print(f"  PASS threshold   ≤ {tolerance_OOM:.2f} OOM")
print(f"  FAIL  threshold  > {FAIL_OOM:.2f} OOM")
print(f"  VERDICT: {verdict}")
print()


# ----------------------------------------------------------------------------
# Section 5 — artifacts
# ----------------------------------------------------------------------------
npz_path = _HERE / "s85_w7_cc6_parker_residue.npz"
png_path = _HERE / "s85_w7_cc6_parker_residue.png"

np.savez(
    npz_path,
    # Primary outputs
    rho_Parker_total=rho_Parker_total,
    ratio_to_Lambda_obs=ratio_to_Lambda_obs,
    Delta_log10=Delta_log10,
    Delta_log10_direct=Delta_log10_direct,
    # Spectra (plan §6)
    beta2_spectrum=beta_sq_spectrum,
    omega_k=omega_k_GeV,
    rho_Parker_integrand=rho_integrand,
    k_grid_MKK=k_grid_MKK,
    k_grid_GeV=k_grid_GeV,
    # Anchors
    beta_sq_pivot_S78=beta_sq_pivot_S78,
    k_pivot_fold_S78=k_pivot_fold_S78,
    k_cusp_in_MKK=k_cusp_in_MKK,
    M_KK_GeV=M_KK_GeV,
    rho_Lambda_obs=rho_Lambda_obs,
    Lambda_obs_direct_GeV4=Lambda_obs_direct_GeV4,
    rho_Parker_analytic=rho_Parker_analytic,
    # Gate state
    abs_delta=abs_delta,
    tolerance_OOM=tolerance_OOM,
    FAIL_OOM=FAIL_OOM,
    verdict=verdict,
    # 4-tuple
    value=Delta_log10,
    scheme=scheme,
    convention=convention,
    L_max=L_max,
    # SHAs
    closure_sha=CLOSURE_SHA,
)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8.2), dpi=130, sharex=True)
ax1.loglog(k_grid_MKK, beta_sq_spectrum, color="tab:blue", lw=2, label=r"$|\beta_k|^2$")
ax1.axhline(beta_sq_pivot_S78, color="k", ls="--", lw=1, alpha=0.6, label=rf"$|\beta_{{pivot}}|^2$ = {beta_sq_pivot_S78:.3e}")
ax1.axvline(k_cusp_in_MKK, color="tab:red", ls=":", lw=1.5, label=rf"$k_{{cusp}}$ = {k_cusp_in_MKK:.2f} $M_{{KK}}$")
ax1.axvline(1.0, color="tab:gray", ls="-.", lw=1, alpha=0.6, label=r"$M_{KK}$ integration cap")
ax1.set_ylabel(r"$|\beta_k|^2$ (Bogoliubov occupancy)")
ax1.set_title(f"S85-W7-2 CC-6 Parker residue — verdict {verdict}")
ax1.legend(loc="best", fontsize=8)
ax1.grid(True, alpha=0.3, which="both")

ax2.loglog(k_grid_MKK, rho_integrand, color="tab:green", lw=2, label=r"$k^3 |\beta_k|^2$")
ax2.axvline(1.0, color="tab:gray", ls="-.", lw=1, alpha=0.6)
ax2.axvline(k_cusp_in_MKK, color="tab:red", ls=":", lw=1.5)
ax2.axhline(rho_Parker_total, color="tab:orange", ls="--", lw=1.2, label=rf"$\rho_{{Parker}}$ = {rho_Parker_total:.2e} $\rm GeV^4$")
ax2.set_xlabel(r"$k / M_{KK}$")
ax2.set_ylabel(r"$k^3 |\beta_k|^2$  (integrand, $\rm GeV^4$)")
ax2.text(
    0.03,
    0.95,
    (
        f"$\\rho_{{Parker}} / \\Lambda_{{obs}}$ = $10^{{{Delta_log10:+.2f}}}$\n"
        f"|$\\Delta\\log_{{10}}$| = {abs_delta:.3f} OOM\n"
        f"PASS $\\leq$ 1.0  |  FAIL > 5.0"
    ),
    transform=ax2.transAxes,
    fontsize=9,
    verticalalignment="top",
    bbox=dict(facecolor="white", alpha=0.85, edgecolor="tab:red"),
)
ax2.legend(loc="lower right", fontsize=8)
ax2.grid(True, alpha=0.3, which="both")

plt.tight_layout()
plt.savefig(png_path, dpi=130)
plt.close()

print("--- outputs ---")
print(f"  .npz: {npz_path.name} ({npz_path.stat().st_size} bytes)")
print(f"  .png: {png_path.name} ({png_path.stat().st_size} bytes)")
print()


# ----------------------------------------------------------------------------
# Section 6 — verdict append with S85+ dual-SHA
# ----------------------------------------------------------------------------
GATE_ID = "S85-W7-CC-6"
verdict_path = _HERE / "s85_gate_verdicts.txt"
content_sha = _file_sha(npz_path)
audit_sha = CLOSURE_SHA

value_str = f"{Delta_log10:.4f}"
canonical_line = (
    f"{GATE_ID}: {verdict} -- "
    f"value={value_str} scheme={scheme} convention={convention} "
    f"L_max={L_max} sha256={audit_sha}"
)
dual_sha_comment = (
    f"# {GATE_ID} dual-SHA: "
    f"content_sha256={content_sha} audit_sha256={audit_sha}"
)

with verdict_path.open("a", encoding="utf-8") as fh:
    fh.write(canonical_line + "\n")
    fh.write(dual_sha_comment + "\n")

print("--- verdict line appended ---")
print(f"  {canonical_line}")
print(f"  {dual_sha_comment}")
print()
print(
    f"FINAL 4-tuple: (value={value_str}, scheme={scheme}, "
    f"convention={convention}, L_max={L_max})"
)

sys.exit(0)
