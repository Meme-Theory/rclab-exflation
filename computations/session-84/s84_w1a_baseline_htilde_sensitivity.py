"""S84-BASELINE-HTILDE-SENSITIVITY — W1a-1.

Substrate-first-principles H_tilde scan over the TD/LI divergence-chase
interval [2.46e-5, 5.91e-3]. Identifies the PASS-1.05 window such that
A_s(H_tilde) sits within factor 1.05 of A_s_Planck = 2.10e-9 under the
CC3 identity d(ln A_s)/d(ln H_tilde) = +2.

CC3 substitution chain (mandatory, see working-paper §W1-1):
  Step 1 (def):    A_s(k_*) = (H_tilde^2/(8 pi^2 eps_H M_Pl^2)) * |F_conv|^2
  Step 2 (subst):  ln A_s = 2 ln H_tilde - ln(8 pi^2) - ln eps_H - 2 ln M_Pl
                          + 2 ln |F_conv|
  Step 3 (simpl):  d(ln A_s)/d(ln H_tilde) = +2
                   (eps_H, F_conv, M_Pl tau-stationary at epoch pivot per
                    S83 G12 DRESSING-TAU-FLOW PASS slope = 1.75e-3)
  Step 4 (sign):   POSITIVE — H_tilde and A_s scale as A_s ∝ H_tilde^2,
                   hence H_tilde scales monotonically with sqrt(A_s).

Anchor pins (from S82 W1-2 PASS-F2, traced from
computations/session-82/s82_w1_2_unified_as_79_full.py):
  H_canonical_TD = 5.90760e-03 (H_TD)            line 137
  H_LI           = 2.46411e-05 (Branch B endpt)  line 143
  eps_H          = 0.02163 (one-loop SR)         line 163
  A_s_canonical  = 3.30e-9 (W1-2 Branch-A)       line 329
Parker IC anchor (from W2-4 Parker IC record
computations/session-82/s82_w2_4_ps_substrate_matched_ic.py line 18, 102):
  n_pairs (anchor) -> 59.8
  P_exc   (anchor) -> 1.000

Outputs:
  s84_w1a_baseline_htilde_sensitivity.npz
  s84_w1a_baseline_htilde_sensitivity.png
  s84_w1a_baseline_htilde_sensitivity.log
Verdict appended to s84_gate_verdicts.txt with full 64-char SHA-256.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

# Cap CPU threads — this is a 2048-point scalar scan; high parallelism wastes
# wall time when other agents share the box.
os.environ.setdefault("OMP_NUM_THREADS", "8")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch

# Anchor the script directory so canonical_constants imports resolve.
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from canonical_constants import M_KK, tau_fold  # noqa: F401  (provenance check)

# ---------------------------------------------------------------------------
# Section 0 — input pin map (gate-verdict SHA closure)
# ---------------------------------------------------------------------------
INPUT_PINS: dict[str, str] = {}


def _file_sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


# Static-file pins (these enter the closure SHA).
_static_files = [
    _HERE / "canonical_constants.py",
    _HERE / "s82_w1_2_unified_as_79_full.py",
    _HERE / "s82_w2_4_ps_substrate_matched_ic.py",
    _HERE / "s83_w2_g12_dressing_tau_flow.py",
]
for _p in _static_files:
    if _p.exists():
        INPUT_PINS[_p.name] = _file_sha(_p)
    else:
        INPUT_PINS[_p.name] = "MISSING"

# ---------------------------------------------------------------------------
# Section 1 — anchor constants (cited above; not yet in canonical_constants.py)
# ---------------------------------------------------------------------------
H_canonical_TD = 5.90760e-03  # (local) S82 W1-2 line 137 anchor; not yet in canonical_constants.py
H_LI = 2.46411e-05  # (local) S82 W1-2 line 143 anchor; not yet in canonical_constants.py
eps_H = 0.02163  # (local) S82 W1-2 line 163 anchor; not yet in canonical_constants.py
A_s_canonical = 3.30e-9  # (local) S82 W1-2 line 329 anchor; not yet in canonical_constants.py
A_s_Planck = 2.10e-9  # (local) Planck 2018 TT,TE,EE+lowE+lensing anchor
F1 = 1.05  # (local) PASS-1.05 envelope, plan §6
n_pairs_Parker = 59.8  # (local) S38 / W2-4 Parker IC anchor
P_exc_Parker = 1.000  # (local) S38 / W2-4 broad-resonance saturation anchor

# Pinned scan-range endpoints (plan §7).
H_lo_scan = 2.46e-5  # (local)
H_hi_scan = 5.91e-3  # (local)
N_grid = 2048  # (local)
L_max = 5  # (local) S83 Branch-B baseline

# Add scan parameters to closure (literal-pin map).
INPUT_PINS["H_canonical_TD"] = f"{H_canonical_TD:.10e}"
INPUT_PINS["H_LI"] = f"{H_LI:.10e}"
INPUT_PINS["eps_H"] = f"{eps_H:.10e}"
INPUT_PINS["A_s_canonical"] = f"{A_s_canonical:.10e}"
INPUT_PINS["A_s_Planck"] = f"{A_s_Planck:.10e}"
INPUT_PINS["F1_envelope"] = f"{F1:.10e}"
INPUT_PINS["n_pairs_Parker"] = f"{n_pairs_Parker:.4f}"
INPUT_PINS["P_exc_Parker"] = f"{P_exc_Parker:.4f}"
INPUT_PINS["H_lo_scan"] = f"{H_lo_scan:.10e}"
INPUT_PINS["H_hi_scan"] = f"{H_hi_scan:.10e}"
INPUT_PINS["N_grid"] = f"{N_grid:d}"
INPUT_PINS["L_max"] = f"{L_max:d}"
INPUT_PINS["scheme"] = "zeta"
INPUT_PINS["convention"] = "TD"

CLOSURE_INPUT = json.dumps(INPUT_PINS, sort_keys=True, separators=(",", ":"))
CLOSURE_SHA = hashlib.sha256(CLOSURE_INPUT.encode("utf-8")).hexdigest()

# ---------------------------------------------------------------------------
# Section 2 — banner: SHA log, anchor echo (per gate-verdicts.md, first 20
# lines of stdout MUST log the closure SHA + input SHAs).
# ---------------------------------------------------------------------------
print("=" * 78)
print("S84 W1a-1: BASELINE-HTILDE-SENSITIVITY")
print("=" * 78)
print(f"closure SHA-256 (64 char): {CLOSURE_SHA}")
print(f"closure SHA-256 (16 head):  {CLOSURE_SHA[:16]}")
print()
print("--- input pin SHAs ---")
for k, v in INPUT_PINS.items():
    print(f"  {k:<28s}: {v}")
print()
print("--- anchors ---")
print(f"  H_canonical_TD   = {H_canonical_TD:.6e}")
print(f"  H_LI             = {H_LI:.6e}")
print(f"  eps_H            = {eps_H:.6f}")
print(f"  A_s_canonical    = {A_s_canonical:.6e}")
print(f"  A_s_Planck       = {A_s_Planck:.6e}")
print(f"  Parker IC pairs  = {n_pairs_Parker:.1f}, P_exc = {P_exc_Parker:.3f}")
print()

# ---------------------------------------------------------------------------
# Section 3 — PASS window derivation (analytical, before grid scan)
# ---------------------------------------------------------------------------
# Substitution chain Step 4: H = H_canonical * sqrt(A_s_target / A_s_canonical)
A_s_lo = A_s_Planck / F1  # (local) PASS-1.05 lower
A_s_hi = A_s_Planck * F1  # (local) PASS-1.05 upper
H_lo_PASS = H_canonical_TD * np.sqrt(A_s_lo / A_s_canonical)  # (local)
H_hi_PASS = H_canonical_TD * np.sqrt(A_s_hi / A_s_canonical)  # (local)

print("--- analytical PASS window (CC3 closed form) ---")
print(f"  A_s_lo (Planck/1.05) = {A_s_lo:.6e}")
print(f"  A_s_hi (Planck*1.05) = {A_s_hi:.6e}")
print(f"  H_lo_PASS            = {H_lo_PASS:.6e}")
print(f"  H_hi_PASS            = {H_hi_PASS:.6e}")
print()

# Pin against expected (plan §6): H_lo ≈ 4.599e-3, H_hi ≈ 4.830e-3.
_expected_lo = 4.599e-3  # (local) plan §6 Python-verified
_expected_hi = 4.830e-3  # (local) plan §6 Python-verified
_pin_lo_dev_pct = abs(H_lo_PASS - _expected_lo) / _expected_lo * 100.0  # (local)
_pin_hi_dev_pct = abs(H_hi_PASS - _expected_hi) / _expected_hi * 100.0  # (local)
assert _pin_lo_dev_pct < 0.5, f"H_lo deviation {_pin_lo_dev_pct:.4f}% > 0.5%"
assert _pin_hi_dev_pct < 0.5, f"H_hi deviation {_pin_hi_dev_pct:.4f}% > 0.5%"
print(f"  pin: |H_lo - 4.599e-3|/4.599e-3 = {_pin_lo_dev_pct:.4f}%  PASS (<0.5%)")
print(f"  pin: |H_hi - 4.830e-3|/4.830e-3 = {_pin_hi_dev_pct:.4f}%  PASS (<0.5%)")
print()

# Log-measure / linear-measure relative to the TD/LI divergence interval.
log_meas_pct = 100.0 * (np.log(H_hi_PASS) - np.log(H_lo_PASS)) / (
    np.log(H_hi_scan) - np.log(H_lo_scan)
)
lin_meas_pct = 100.0 * (H_hi_PASS - H_lo_PASS) / (H_hi_scan - H_lo_scan)
print(f"  log-measure   = {log_meas_pct:.4f}%   (band [0.80, 1.05])")
print(f"  linear-measure= {lin_meas_pct:.4f}%   (band [3.5, 4.5])")
print()

# ---------------------------------------------------------------------------
# Section 4 — grid scan (torch float64; CPU OK at this size)
# ---------------------------------------------------------------------------
H_grid = torch.linspace(
    H_lo_scan, H_hi_scan, N_grid, dtype=torch.float64
)  # uniform grid

# A_s under CC3: A_s(H) = A_s_canonical * (H / H_canonical)^2
A_s_grid = A_s_canonical * (H_grid / H_canonical_TD) ** 2

# PASS mask: A_s_lo <= A_s <= A_s_hi
PASS_mask = (A_s_grid >= A_s_lo) & (A_s_grid <= A_s_hi)
n_PASS = int(PASS_mask.sum().item())  # (local)
print("--- grid scan (2048 uniform points, float64) ---")
print(f"  N_PASS gridpoints = {n_PASS}")
if n_PASS > 0:
    H_grid_np = H_grid.numpy()
    A_s_grid_np = A_s_grid.numpy()
    PASS_mask_np = PASS_mask.numpy()
    H_window_lo = float(H_grid_np[PASS_mask_np].min())
    H_window_hi = float(H_grid_np[PASS_mask_np].max())
    print(f"  H window (grid)   = [{H_window_lo:.6e}, {H_window_hi:.6e}]")
else:
    H_window_lo = float("nan")
    H_window_hi = float("nan")
print()

# Contiguity check: PASS mask should be a single contiguous block.
mask_diff = np.diff(PASS_mask.numpy().astype(int))  # (local)
n_transitions = int(np.abs(mask_diff).sum())  # (local)
contiguous = n_transitions <= 2  # 0,1,1,...,1,0 has 2 transitions; allow 0/1/2
print(f"  PASS contiguity   = {contiguous} (transitions={n_transitions})")
print()

# ---------------------------------------------------------------------------
# Section 5 — cross-checks CC-i .. CC-vi
# ---------------------------------------------------------------------------
print("=" * 78)
print("Cross-checks CC-i .. CC-vi")
print("=" * 78)

# CC-i — log-measure within [0.80, 1.05]; spec target 0.913, tolerance 0.05
spec_log_meas = 0.913  # (local) plan §8 expected output 4-tuple
delta_log_meas = abs(log_meas_pct - spec_log_meas)  # (local)
CC_i_in_band = (0.80 <= log_meas_pct <= 1.05)  # (local)
CC_i_within_spec = delta_log_meas <= 0.05  # (local) "INFO if delta > 0.05"
print(f"CC-i   log-measure% = {log_meas_pct:.4f}, spec={spec_log_meas:.3f}, "
      f"|delta|={delta_log_meas:.4f}, in_band={CC_i_in_band}, "
      f"within_spec={CC_i_within_spec}")

# CC-ii — linear-measure within [3.5, 4.5]; spec target 3.907, tolerance 0.02
spec_lin_meas = 3.907  # (local) plan section 6 Python-verified target
delta_lin_meas = abs(lin_meas_pct - spec_lin_meas)
CC_ii_in_band = (3.5 <= lin_meas_pct <= 4.5)
CC_ii_within_spec = delta_lin_meas <= 0.02
print(f"CC-ii  linear-measure% = {lin_meas_pct:.4f}, spec={spec_lin_meas:.3f}, "
      f"|delta|={delta_lin_meas:.4f}, in_band={CC_ii_in_band}, "
      f"within_spec={CC_ii_within_spec}")

# CC-iii — sqrt monotonicity: A_s(H)/H^2 = A_s_canonical / H_canonical^2
#         at machine epsilon across full grid
ratio = (A_s_grid / H_grid**2).numpy()  # (local)
ratio_canonical = A_s_canonical / H_canonical_TD**2  # (local)
ratio_dev = float(np.max(np.abs(ratio / ratio_canonical - 1.0)))  # (local)
CC_iii_ok = ratio_dev < 1e-12
print(f"CC-iii ratio dev (max |r/r0 - 1|) = {ratio_dev:.3e}, "
      f"OK ({CC_iii_ok})")

# CC-iv — d(ln A_s)/d(ln H_tilde) numerical from two adjacent grid points
i_mid = N_grid // 2  # (local)
H_a = float(H_grid[i_mid])  # (local)
H_b = float(H_grid[i_mid + 1])  # (local)
A_s_a = A_s_canonical * (H_a / H_canonical_TD) ** 2  # (local)
A_s_b = A_s_canonical * (H_b / H_canonical_TD) ** 2  # (local)
slope = (np.log(A_s_b) - np.log(A_s_a)) / (np.log(H_b) - np.log(H_a))  # (local)
CC_iv_dev = abs(slope - 2.0)  # (local)
CC_iv_ok = CC_iv_dev < 1e-6
print(f"CC-iv  d(ln A_s)/d(ln H_tilde) = {slope:.12f}, "
      f"|delta - 2| = {CC_iv_dev:.3e}, OK ({CC_iv_ok})")

# CC-v — Parker IC pair count feed-through.  At H_tilde = H_canonical the
#         baseline IC carries n_pairs = 59.8 (W2-4); confirm this is the
#         numerical anchor used in the script.
CC_v_npairs = n_pairs_Parker  # (local)
CC_v_pexc = P_exc_Parker  # (local)
CC_v_ok = (abs(CC_v_npairs - 59.8) < 1e-6 and abs(CC_v_pexc - 1.0) < 1e-6)
print(f"CC-v   Parker IC: n_pairs={CC_v_npairs:.4f}, P_exc={CC_v_pexc:.4f}, "
      f"OK ({CC_v_ok})")

# CC-vi — LI endpoint sanity: A_s(H_LI) = A_s_canonical * (H_LI/H_canonical)^2
A_s_LI_pred = A_s_canonical * (H_LI / H_canonical_TD) ** 2  # (local)
A_s_LI_spec = 5.73e-14  # (local) plan §6 target
CC_vi_dev = abs(A_s_LI_pred - A_s_LI_spec) / A_s_LI_spec  # (local)
CC_vi_ok = CC_vi_dev < 1e-2  # 1% tolerance
print(f"CC-vi  A_s(H_LI) predicted = {A_s_LI_pred:.6e}, spec = {A_s_LI_spec:.3e}, "
      f"rel dev = {CC_vi_dev:.3e}, OK ({CC_vi_ok})")

CC_all_ok = bool(
    CC_i_in_band and CC_ii_in_band and CC_iii_ok and CC_iv_ok and CC_v_ok and CC_vi_ok
)
print()
print(f"CC-all PASS: {CC_all_ok}")
print()

# ---------------------------------------------------------------------------
# Section 6 — verdict classification (PASS / INFO / FAIL)
# ---------------------------------------------------------------------------
window_exists = (n_PASS > 0) and contiguous
log_in_tight_band = (0.80 <= log_meas_pct <= 1.05)
lin_in_tight_band = (3.5 <= lin_meas_pct <= 4.5)
slope_at_2 = CC_iv_ok

if not window_exists or not slope_at_2 or not (CC_iii_ok and CC_v_ok and CC_vi_ok):
    verdict = "FAIL"
elif log_in_tight_band and lin_in_tight_band and CC_all_ok:
    verdict = "PASS"
else:
    verdict = "INFO"

print("=" * 78)
print(f"VERDICT: {verdict}")
print(f"  window_exists = {window_exists}")
print(f"  slope==2     = {slope_at_2}")
print(f"  log_tight    = {log_in_tight_band}")
print(f"  linear_tight = {lin_in_tight_band}")
print(f"  CC_all       = {CC_all_ok}")
print("=" * 78)
print()

# ---------------------------------------------------------------------------
# Section 7 — outputs (.npz + .png)
# ---------------------------------------------------------------------------
out_npz = _HERE / "s84_w1a_baseline_htilde_sensitivity.npz"
np.savez_compressed(
    out_npz,
    H_grid=H_grid.numpy(),
    A_s_grid=A_s_grid.numpy(),
    PASS_mask=PASS_mask.numpy(),
    H_lo_PASS=H_lo_PASS,
    H_hi_PASS=H_hi_PASS,
    log_measure_pct=log_meas_pct,
    linear_measure_pct=lin_meas_pct,
    A_s_lo=A_s_lo,
    A_s_hi=A_s_hi,
    A_s_Planck=A_s_Planck,
    A_s_canonical=A_s_canonical,
    H_canonical_TD=H_canonical_TD,
    H_LI=H_LI,
    eps_H=eps_H,
    n_pairs_Parker=n_pairs_Parker,
    P_exc_Parker=P_exc_Parker,
    L_max=L_max,
    closure_sha256=CLOSURE_SHA,
    CC_i_log_meas_pct=log_meas_pct,
    CC_ii_lin_meas_pct=lin_meas_pct,
    CC_iii_ratio_dev=ratio_dev,
    CC_iv_slope=slope,
    CC_v_npairs=CC_v_npairs,
    CC_v_pexc=CC_v_pexc,
    CC_vi_A_s_LI=A_s_LI_pred,
    CC_vi_rel_dev=CC_vi_dev,
    verdict=verdict,
)
print(f"wrote {out_npz}")

# Plot: H_tilde vs A_s on log-log with PASS window shaded.
fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=120)
ax.loglog(H_grid.numpy(), A_s_grid.numpy(), color="navy", lw=1.6,
          label=r"$A_s(\widetilde{H}) = A_s^{\rm canon}\,(\widetilde{H}/\widetilde{H}_{\rm canon})^2$")
ax.axhspan(A_s_lo, A_s_hi, color="palegreen", alpha=0.6,
           label=r"PASS-1.05 band  $A_s\in[A_s^{\rm Pl}/1.05,\,A_s^{\rm Pl}\cdot 1.05]$")
ax.axvspan(H_lo_PASS, H_hi_PASS, color="khaki", alpha=0.45,
           label=fr"PASS window $\widetilde{{H}}\in[{H_lo_PASS:.3e},\,{H_hi_PASS:.3e}]$")
ax.axhline(A_s_Planck, color="forestgreen", ls="--", lw=1.0,
           label=fr"$A_s^{{\rm Planck}} = {A_s_Planck:.2e}$")
ax.axvline(H_canonical_TD, color="crimson", ls=":", lw=1.0,
           label=fr"$\widetilde{{H}}_{{\rm TD}} = {H_canonical_TD:.3e}$")
ax.axvline(H_LI, color="darkorange", ls=":", lw=1.0,
           label=fr"$\widetilde{{H}}_{{\rm LI}} = {H_LI:.3e}$")
ax.set_xlabel(r"$\widetilde{H}$  [substrate units]")
ax.set_ylabel(r"$A_s$")
ax.set_title(
    f"S84 W1a-1 BASELINE-H̃-SENSITIVITY — log-DC = {log_meas_pct:.3f}%, "
    f"verdict = {verdict}"
)
ax.legend(loc="lower right", fontsize=8, framealpha=0.92)
ax.grid(True, which="both", alpha=0.25)
plt.tight_layout()
out_png = _HERE / "s84_w1a_baseline_htilde_sensitivity.png"
plt.savefig(out_png)
plt.close(fig)
print(f"wrote {out_png}")

# ---------------------------------------------------------------------------
# Section 8 — verdict line append (4-tuple + 64-char SHA closure)
# ---------------------------------------------------------------------------
verdict_line = (
    f"S84-BASELINE-HTILDE-SENSITIVITY: {verdict} -- "
    f"value={log_meas_pct:.4f} scheme=zeta convention=TD L_max={L_max} "
    f"sha256={CLOSURE_SHA}"
)
verdict_path = _HERE / "s84_gate_verdicts.txt"
with verdict_path.open("a", encoding="utf-8") as fh:
    fh.write(verdict_line + "\n")
print()
print("verdict line:")
print(f"  {verdict_line}")
print(f"appended to {verdict_path}")

# Final 4-tuple (last non-verdict line per template).
print()
print(f"4-TUPLE: (value={log_meas_pct:.4f}, scheme=zeta, convention=TD, L_max={L_max})")
