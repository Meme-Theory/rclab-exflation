"""S85-W7-CUSP-BOGOLIUBOV — W7-4.

[VERIFY] gate: direct numerical integration of v″_k + [k² − z″/z(t)] v_k = 0
across a square-root van Hove cusp ω²(t) ~ A·|t − t_c| (α=1). Extracts
the Bogoliubov β_k exponent from in→out vacuum transfer and compares
against the Airy asymptotic |β_k|² ~ (k/k_cusp)^{−2/3}.

Hypothesis (plan §W7-4 step 5):
  Square-root cusp α=1 is the generic 2D van Hove form. Bogoliubov
  |β_k|² ~ k^{-2/3} for k > k_cusp from Airy-turning-point asymptotics,
  saturating at O(1)×|β|²_anchor for k ≤ k_cusp.

Substitution chain (plan §W7-4 step 10):

  Step 1 (definitions):
    ω²(t) = k² + z″/z(t)                    [Mukhanov mode frequency]
    z″/z(t) = A · |t − t_c|^α with α = 1     [square-root cusp]
    β_k: v_k(out) = α_k u_k^in + β_k (u_k^in)*
    Airy asymptotic: |β_k|² ~ (k/k_cusp)^{−2/3} for k > k_cusp

  Step 2 (substitution, α=1):
    v″_k + [k² − A|t−t_c|] v_k = 0    [Airy equation, shifted turning point]
    Transform to standard Airy via ξ = (A)^{1/3} · (t − t_c − k²/A):
      v″(ξ) = ξ · v(ξ)

  Step 3 (simplification — log-log fit):
    log |β_k|² = −(2/3) · log(k/k_cusp) + const  (UV tail k > k_cusp)
    Fit slope from numerical transfer-matrix should return
      exponent = −0.6667 ± ε_numerical

  Step 4 (direction):
    PASS iff fit exponent ∈ [−0.7167, −0.6167] AND |β_k_pivot|² matches
    S78 W1-E anchor (4.255e+04) to 20% RATIO.
    Direction: if fit > −0.6167 (less negative): cusp milder → NOT 2D
    van Hove; W0 VAN-HOVE-CUSP-THEOREM re-opens.
    If fit < −0.7167 (sharper): possibly log-2D or 3D cusp; re-audit.

PASS/FAIL/INFO (plan §W7-4 step 9):
  PASS:   exponent ∈ [−0.7167, −0.6167] AND |β_pivot|² match ≤ 20%
  FAIL:   exponent outside band OR |β_pivot|² mismatch > 50%
  INFO:   exponent inside band AND 20% < |β_pivot|² residual ≤ 50%

Machinery pin (plan §7):
  L_max=10, scheme=transfer-matrix, convention=BD-in-out,
  alpha_cusp=1.0 (2D van Hove generic), N_k=4096 (reduced to 256 on
  CPU with L_max-REDUCED flag), N_t=1e5 (reduced to 4000), tolerance
  0.05 ABSOLUTE exponent, random_seed=42.

Outputs:
  computations/session-85/s85_w7_cusp_bogoliubov.npz
  computations/session-85/s85_w7_cusp_bogoliubov.png
Verdict to computations/session-85/s85_gate_verdicts.txt with dual-SHA.
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
    dS_fold,
    d2S_fold,
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

# Machinery pins (plan §7) — reduced on CPU
L_max = 10  # (local) plan §7
scheme = "transfer-matrix"  # (local) plan §7
convention = "BD-in-out"  # (local) plan §7
alpha_cusp = 1.0  # (local) plan §7 pre-registered 2D van Hove
N_k = 256  # (local) plan §7 target 4096; CPU-reduced with L_max-REDUCED flag
N_t = 4000  # (local) plan §7 target 1e5; CPU-reduced
tolerance_ABS_exp = 0.05  # (local) plan §7 exponent fit tolerance
tolerance_anchor_pct = 0.20  # (local) plan §9 |β|² anchor PASS RATIO
FAIL_anchor_pct = 0.50  # (local) plan §9 |β|² anchor FAIL RATIO
exponent_target = -2.0 / 3.0  # (local) Airy universal
PASS_lo = exponent_target - tolerance_ABS_exp  # (local) = -0.7167
PASS_hi = exponent_target + tolerance_ABS_exp  # (local) = -0.6167
random_seed = 42  # (local)

INPUT_PINS["L_max"] = f"{L_max:d}"
INPUT_PINS["scheme"] = scheme
INPUT_PINS["convention"] = convention
INPUT_PINS["alpha_cusp"] = f"{alpha_cusp:.4f}"
INPUT_PINS["N_k"] = f"{N_k:d}"
INPUT_PINS["N_t"] = f"{N_t:d}"
INPUT_PINS["tolerance_ABS_exp"] = f"{tolerance_ABS_exp:.6f}"
INPUT_PINS["tolerance_anchor_pct"] = f"{tolerance_anchor_pct:.6f}"
INPUT_PINS["FAIL_anchor_pct"] = f"{FAIL_anchor_pct:.6f}"
INPUT_PINS["exponent_target"] = f"{exponent_target:.6f}"
INPUT_PINS["PASS_lo"] = f"{PASS_lo:.6f}"
INPUT_PINS["PASS_hi"] = f"{PASS_hi:.6f}"
INPUT_PINS["random_seed"] = f"{random_seed:d}"
INPUT_PINS["M_KK_gravity_GeV"] = f"{M_KK_gravity:.10e}"
INPUT_PINS["dt_transit"] = f"{dt_transit:.10e}"
INPUT_PINS["Mach_max_framework"] = f"{Mach_max_framework:.10e}"

# Pull S78 W1-E anchor
s78_npz = _HERE / "s78_pre_fold_vacuum.npz"
_s78 = np.load(s78_npz)
beta_sq_pivot_S78 = float(_s78["CHK3_beta_sq_pivot"])  # (local) anchor target
k_pivot_fold_S78 = float(_s78["k_pivot_fold"])  # (local) M_KK units
INPUT_PINS["beta_sq_pivot_S78"] = f"{beta_sq_pivot_S78:.10e}"
INPUT_PINS["k_pivot_fold_S78"] = f"{k_pivot_fold_S78:.10e}"

CLOSURE_INPUT = json.dumps(INPUT_PINS, sort_keys=True, separators=(",", ":"))
CLOSURE_SHA = hashlib.sha256(CLOSURE_INPUT.encode("utf-8")).hexdigest()

print("=" * 78)
print("S85 W7-4: CUSP-BOGOLIUBOV — transfer-matrix across square-root cusp")
print("=" * 78)
print(f"closure SHA-256 (64 char): {CLOSURE_SHA}")
print(f"closure SHA-256 (16 head): {CLOSURE_SHA[:16]}")
print()
print("--- input pin SHAs and values ---")
for _k, _v in INPUT_PINS.items():
    print(f"  {_k:<32s}: {_v}")
print()


# ----------------------------------------------------------------------------
# Section 1 — cusp profile + k-grid construction
# ----------------------------------------------------------------------------
# Work in natural units where M_KK = 1. The cusp amplitude A is chosen
# so that the Airy turning point k² = A·|t_max − t_c| lies inside the
# transit window for k ~ O(1) M_KK, enabling detection of the k^{−2/3}
# tail in the UV. Concretely: A ≡ 1 in M_KK units; then k_cusp defined
# by k_cusp² = A · dt_transit gives k_cusp ≈ √(dt_transit) ≈ 0.0336
# M_KK in the transit window.
A_cusp = 1.0  # (local) natural-units amplitude (sets k_cusp via k² = A·dt_trans)
t_c = 0.0  # (local) cusp at transit midpoint
t_range = dt_transit  # (local) integration window [−dt_transit, +dt_transit]

# Turning-point at t* = t_c + k²/A; for mode to experience turning point inside
# [−dt, +dt], need k² < A·dt_transit
k_cusp_analytic = np.sqrt(A_cusp * dt_transit)  # (local) M_KK units
INPUT_PINS["A_cusp"] = f"{A_cusp:.10e}"
INPUT_PINS["k_cusp_analytic"] = f"{k_cusp_analytic:.10e}"

print("--- cusp profile + k-grid ---")
print(f"  A_cusp (natural)                = {A_cusp:.4f}")
print(f"  t_range (= dt_transit)          = {t_range:.4e}  M_KK^-1")
print(f"  k_cusp_analytic (= √(A·t_range)) = {k_cusp_analytic:.4e}  M_KK")
print(f"  N_k (reduced from plan 4096)    = {N_k}")
print(f"  N_t (reduced from plan 1e5)     = {N_t}")
print()

# k-grid log-spaced; we span [0.3·k_cusp, 100·k_cusp] to capture IR saturation
# and UV power-law tail
k_grid = np.logspace(
    np.log10(0.3 * k_cusp_analytic),
    np.log10(100.0 * k_cusp_analytic),
    N_k,
)  # (local)
# Time grid across transit
t_grid = np.linspace(-t_range, t_range, N_t)  # (local)
dt = float(t_grid[1] - t_grid[0])  # (local)
# Pump profile z″/z(t) = A·|t − t_c|^α with α=1
zpp_over_z_t = A_cusp * np.abs(t_grid - t_c) ** alpha_cusp  # (local)


# ----------------------------------------------------------------------------
# Section 2 — Mode-equation integrator (RK4 per k-mode)
# ----------------------------------------------------------------------------
# Integrate v″ + (k² − z″/z(t)) v = 0 with BD in-vacuum initial condition
# at t = -t_range:
#   v_k(t) = e^{-iω_in·t} / √(2ω_in), dv/dt = -iω_in · v
#   where ω_in² = k² − z″/z(-t_range) = k² − A·t_range  (may be positive or negative)

def integrate_mode(k: float) -> tuple[complex, complex, complex, complex]:
    """Integrate one k-mode and return (v_end, dv_end, alpha_k, beta_k)."""
    # Initial frequency
    omega_in_sq = k * k - A_cusp * t_range  # (local)
    # If omega_in_sq <= 0, mode is in bandgap at t_start; use |omega| with imaginary rotation
    omega_in = np.sqrt(complex(omega_in_sq))  # (local) complex if negative
    # BD in-vacuum at t = -t_range
    # u_in(t) = e^{-iω_in·t} / √(2ω_in)
    t_start = -t_range
    v = np.exp(-1j * omega_in * t_start) / np.sqrt(2.0 * omega_in)  # complex
    dvdt = -1j * omega_in * v  # complex

    # RK4 integration of (v, dvdt) with effective ω²(t) = k² − z″/z(t)
    # System: dv/dt = dvdt;  d(dvdt)/dt = -(k² − z″/z) v
    for i in range(N_t - 1):
        t = t_grid[i]
        zpp = A_cusp * abs(t - t_c) ** alpha_cusp
        zpp_half = A_cusp * abs(t + 0.5 * dt - t_c) ** alpha_cusp
        zpp_next = A_cusp * abs(t + dt - t_c) ** alpha_cusp
        # Effective omega²
        o2_0 = k * k - zpp
        o2_h = k * k - zpp_half
        o2_1 = k * k - zpp_next

        k1_v = dvdt
        k1_d = -o2_0 * v
        k2_v = dvdt + 0.5 * dt * k1_d
        k2_d = -o2_h * (v + 0.5 * dt * k1_v)
        k3_v = dvdt + 0.5 * dt * k2_d
        k3_d = -o2_h * (v + 0.5 * dt * k2_v)
        k4_v = dvdt + dt * k3_d
        k4_d = -o2_1 * (v + dt * k3_v)
        v = v + (dt / 6.0) * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)
        dvdt = dvdt + (dt / 6.0) * (k1_d + 2 * k2_d + 2 * k3_d + k4_d)

    # Out-frequency at t = +t_range
    t_end = t_range
    omega_out_sq = k * k - A_cusp * t_range  # same form as in by symmetry
    omega_out = np.sqrt(complex(omega_out_sq))

    # Bogoliubov decomposition: v(T) = α·e^{-iω_out·T}/√(2ω_out) + β·e^{+iω_out·T}/√(2ω_out)
    # Solve for α, β:
    phase_plus = np.exp(-1j * omega_out * t_end)  # u_out(T) phase without normalization
    phase_minus = np.exp(+1j * omega_out * t_end)  # (u_out)* phase
    norm = 1.0 / np.sqrt(2.0 * omega_out)
    # v = (α · phase_plus + β · phase_minus) · norm
    # dv/dt = (-iω · α · phase_plus + iω · β · phase_minus) · norm
    # => α = (0.5/norm) · [v · (1/phase_plus) + (dv/dt) · (1/(-iω·phase_plus))]
    #       = (0.5/norm) · (v − i·dv/dt/ω) · (1/phase_plus)
    #     β = (0.5/norm) · (v + i·dv/dt/ω) · (1/phase_minus)
    alpha_k = 0.5 * (v + (1j / omega_out) * dvdt) / (norm * phase_plus)  # (local)
    beta_k = 0.5 * (v - (1j / omega_out) * dvdt) / (norm * phase_minus)  # (local)
    # (Sign convention: β_k is the out-negative-frequency projection.)
    return v, dvdt, alpha_k, beta_k


print("--- integrating mode equation for N_k modes ---")
alpha_arr = np.zeros(N_k, dtype=complex)  # (local)
beta_arr = np.zeros(N_k, dtype=complex)  # (local)
v_end_arr = np.zeros(N_k, dtype=complex)  # (local)
dv_end_arr = np.zeros(N_k, dtype=complex)  # (local)
for i, kk in enumerate(k_grid):
    v_end, dv_end, a_k, b_k = integrate_mode(float(kk))
    alpha_arr[i] = a_k
    beta_arr[i] = b_k
    v_end_arr[i] = v_end
    dv_end_arr[i] = dv_end

beta_sq_arr = np.abs(beta_arr) ** 2  # (local)
alpha_sq_arr = np.abs(alpha_arr) ** 2  # (local)
unitarity_dev = np.abs(alpha_sq_arr - beta_sq_arr - 1.0)  # (local)

print(f"  integrated {N_k} modes, N_t={N_t} time-steps each")
print(f"  unitarity |α|²−|β|²−1 max-dev  = {float(np.max(unitarity_dev)):.4e}")
print(f"  unitarity mean-dev              = {float(np.mean(unitarity_dev)):.4e}")
print(f"  |β|² range                      = [{float(np.min(beta_sq_arr)):.4e}, {float(np.max(beta_sq_arr)):.4e}]")
print()


# ----------------------------------------------------------------------------
# Section 3 — log-log fit of UV tail for Airy exponent
# ----------------------------------------------------------------------------
# Restrict fit to k > 3·k_cusp (safely in UV tail) and where β² > 0
uv_mask = (k_grid > 3.0 * k_cusp_analytic) & (beta_sq_arr > 1e-30)  # (local)
k_uv = k_grid[uv_mask]  # (local)
beta_sq_uv = beta_sq_arr[uv_mask]  # (local)
log_k = np.log10(k_uv / k_cusp_analytic)  # (local)
log_beta = np.log10(beta_sq_uv)  # (local)

# Linear least-squares fit: log_beta = exponent · log_k + const
if len(log_k) >= 3:
    # np.polyfit fits highest-degree-first
    fit_coeffs = np.polyfit(log_k, log_beta, 1)  # (local) [slope, intercept]
    exponent_fit = float(fit_coeffs[0])  # (local) slope = exponent
    intercept_fit = float(fit_coeffs[1])  # (local)
    # Residuals
    pred = np.polyval(fit_coeffs, log_k)
    resid = np.sqrt(float(np.mean((log_beta - pred) ** 2)))  # (local) RMS
else:
    exponent_fit = float("nan")
    intercept_fit = float("nan")
    resid = float("nan")

print("--- UV-tail log-log fit ---")
print(f"  fit-range N_points               = {len(log_k)}")
print(f"  fit exponent (slope)             = {exponent_fit:.4f}")
print(f"  fit intercept                    = {intercept_fit:.4f}")
print(f"  RMS residual (log_beta)          = {resid:.4f}")
print(f"  Airy target                      = {exponent_target:.4f}  (−2/3)")
print(f"  PASS band                        = [{PASS_lo:.4f}, {PASS_hi:.4f}]")
print()


# ----------------------------------------------------------------------------
# Section 4 — anchor comparison at k_pivot_fold (S78 W1-E anchor)
# ----------------------------------------------------------------------------
# The S78 anchor is at k_pivot = 14.31 M_KK, which is above our k-grid max
# (we span 0.3·k_cusp to 100·k_cusp ≈ 3.36). To compare anchors we must
# EXTRAPOLATE the fitted power law to k = k_pivot, then compare.
#
# Extrapolation: |β|²(k_pivot) = 10^(intercept + exponent · log10(k_pivot/k_cusp))
if not np.isnan(exponent_fit):
    log_k_pivot = np.log10(k_pivot_fold_S78 / k_cusp_analytic)  # (local)
    beta_sq_pivot_extrapolated = 10.0 ** (intercept_fit + exponent_fit * log_k_pivot)  # (local)
    anchor_residual_pct = abs(
        beta_sq_pivot_extrapolated - beta_sq_pivot_S78
    ) / beta_sq_pivot_S78  # (local)
else:
    beta_sq_pivot_extrapolated = float("nan")
    anchor_residual_pct = float("nan")

print("--- anchor comparison at k_pivot = 14.31 M_KK (S78 W1-E) ---")
print(f"  k_pivot_fold_S78                 = {k_pivot_fold_S78:.4f} M_KK")
print(f"  k_pivot / k_cusp_analytic         = {k_pivot_fold_S78/k_cusp_analytic:.4e}")
print(f"  |β|²_pivot extrapolated (this run)= {beta_sq_pivot_extrapolated:.6e}")
print(f"  |β|²_pivot S78 anchor             = {beta_sq_pivot_S78:.6e}")
print(f"  anchor residual RATIO             = {anchor_residual_pct:.4f}  ({100*anchor_residual_pct:.1f}%)")
print(f"  PASS anchor  ≤ 20%                = {anchor_residual_pct <= tolerance_anchor_pct}")
print(f"  FAIL anchor  > 50%                = {anchor_residual_pct > FAIL_anchor_pct}")
print()


# ----------------------------------------------------------------------------
# Section 5 — PASS/FAIL/INFO verdict
# ----------------------------------------------------------------------------
exponent_in_band = (
    (not np.isnan(exponent_fit))
    and (PASS_lo <= exponent_fit <= PASS_hi)
)
anchor_pass = (not np.isnan(anchor_residual_pct)) and (
    anchor_residual_pct <= tolerance_anchor_pct
)
anchor_info = (not np.isnan(anchor_residual_pct)) and (
    tolerance_anchor_pct < anchor_residual_pct <= FAIL_anchor_pct
)

# Plan §9 verdict:
# PASS = exponent_in_band AND anchor_pass
# FAIL = (exponent outside band) OR (anchor_residual > 50%)
# INFO = exponent_in_band AND anchor_info
if exponent_in_band and anchor_pass:
    verdict = "PASS"
elif (not exponent_in_band) or (
    (not np.isnan(anchor_residual_pct)) and anchor_residual_pct > FAIL_anchor_pct
):
    verdict = "FAIL"
elif exponent_in_band and anchor_info:
    verdict = "INFO"
else:
    verdict = "FAIL"

# Add L_max-REDUCED flag if N_k is below plan target
L_max_reduced_flag = (N_k < 4096) or (N_t < 100000)
print("--- PASS/FAIL/INFO verdict (plan §9 AND) ---")
print(f"  [1] exponent_fit in band [{PASS_lo:.4f},{PASS_hi:.4f}]: {exponent_fit:.4f}  →  {exponent_in_band}")
print(
    f"  [2] anchor residual RATIO ≤ {tolerance_anchor_pct:.2f}: "
    f"{anchor_residual_pct:.4f}  →  {anchor_pass}"
)
print(f"  L_max-REDUCED flag (N_k={N_k}<4096 or N_t={N_t}<1e5): {L_max_reduced_flag}")
print(f"  VERDICT: {verdict}")
print()


# ----------------------------------------------------------------------------
# Section 6 — artifacts
# ----------------------------------------------------------------------------
npz_path = _HERE / "s85_w7_cusp_bogoliubov.npz"
png_path = _HERE / "s85_w7_cusp_bogoliubov.png"

np.savez(
    npz_path,
    k_grid=k_grid,
    beta2_k=beta_sq_arr,
    alpha2_k=alpha_sq_arr,
    unitarity_dev=unitarity_dev,
    exponent_fit_log_log=exponent_fit,
    intercept_fit=intercept_fit,
    residual_vs_Airy=float(exponent_fit - exponent_target) if not np.isnan(exponent_fit) else float("nan"),
    beta_sq_pivot_extrapolated=beta_sq_pivot_extrapolated,
    beta_sq_pivot_S78=beta_sq_pivot_S78,
    anchor_residual_pct=anchor_residual_pct,
    k_cusp_analytic=k_cusp_analytic,
    A_cusp=A_cusp,
    alpha_cusp=alpha_cusp,
    verdict=verdict,
    L_max_reduced_flag=L_max_reduced_flag,
    # 4-tuple
    value=exponent_fit,
    scheme=scheme,
    convention=convention,
    L_max=L_max,
    # SHA
    closure_sha=CLOSURE_SHA,
)

fig, ax = plt.subplots(figsize=(10.2, 6.4), dpi=130)
ax.loglog(
    k_grid / k_cusp_analytic,
    beta_sq_arr,
    color="tab:blue",
    lw=2,
    label=r"$|\beta_k|^2$ (transfer-matrix)",
)
# Airy reference
k_ref = k_grid / k_cusp_analytic
beta_sq_ref = (10 ** intercept_fit) * k_ref ** exponent_target if not np.isnan(intercept_fit) else None
if beta_sq_ref is not None:
    ax.loglog(
        k_ref,
        beta_sq_ref,
        color="tab:red",
        ls="--",
        lw=1.5,
        label=r"Airy $k^{-2/3}$ reference",
    )
# Fit line
if not np.isnan(exponent_fit):
    fit_line = (10 ** intercept_fit) * k_ref ** exponent_fit
    ax.loglog(k_ref, fit_line, color="tab:green", ls=":", lw=1.8, label=f"Fit slope = {exponent_fit:.3f}")
ax.axvline(1.0, color="k", ls="-", lw=0.8, alpha=0.6, label=r"$k_{cusp}$")
ax.axhline(beta_sq_pivot_S78, color="tab:orange", ls="-.", lw=1, alpha=0.7, label=rf"S78 W1-E anchor {beta_sq_pivot_S78:.2e}")
ax.set_xlabel(r"$k / k_{cusp}$")
ax.set_ylabel(r"$|\beta_k|^2$")
ax.set_title(
    f"S85-W7-4 CUSP-BOGOLIUBOV — verdict {verdict}\n"
    f"fit exponent = {exponent_fit:.4f} vs Airy −0.6667; "
    f"anchor residual = {100*anchor_residual_pct:.1f}%"
)
ax.legend(loc="best", fontsize=8)
ax.grid(True, alpha=0.3, which="both")
plt.tight_layout()
plt.savefig(png_path, dpi=130)
plt.close()

print("--- outputs ---")
print(f"  .npz: {npz_path.name} ({npz_path.stat().st_size} bytes)")
print(f"  .png: {png_path.name} ({png_path.stat().st_size} bytes)")
print()


# ----------------------------------------------------------------------------
# Section 7 — verdict append with S85+ dual-SHA
# ----------------------------------------------------------------------------
GATE_ID = "S85-W7-CUSP-BOGOLIUBOV"
verdict_path = _HERE / "s85_gate_verdicts.txt"
content_sha = _file_sha(npz_path)
audit_sha = CLOSURE_SHA

value_str = f"{exponent_fit:.6f}"
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
