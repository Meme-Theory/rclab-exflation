"""S85-W7-BASELINE-HTILDE-DERIVATION — W7-1.

[VERIFY] gate — close the TD-vs-LI H_tilde divergence chase opened by
S84 W1a-1 and carried in S83 Dynamics-Dressing Workshop Final.

Hypothesis (plan §W7-1 step 5):
  H_tilde_DC = H_tilde_Friedmann / F_stretch reconciles TD and LI
  anchors inside the S84 W1a-1 PASS window [4.599e-3, 4.829e-3] once
  the substrate-emergent Friedmann H is distinguished from the
  Jensen-parameter transit rate H_transit per S76 Transit-Einstein
  WS R1 "z''/z requires H_Friedmann" result.

Substitution chain (plan §W7-1 step 10):

  Step 1 (definitions, canonical-constants + S76 WS R1):
    H_Friedmann = (8pi G/3 * rho_eff)^{1/2}    [emergent, substrate a_2]
    H_transit   = (1/Vol_SU3) * dS_fold/dtau   [Jensen-parameter rate]
    H_tilde     = band-averaged pump rate entering z''/z at CMB pivot
    z''/z       = H_Friedmann^2 * [2 - eps_H
                  + F_stretch * (H_transit/H_Friedmann)^2]
    F_stretch   = (H_transit/H_Friedmann)^2

  Step 2 (plan substitution, using plan's TD/LI anchors):
    H_tilde_center = 0.5*(H_tilde_lo + H_tilde_hi) = 4.714e-3
    H_tilde_TD_plan = H_tilde_center * 1.57
    H_tilde_LI_plan = H_tilde_center * 181.0
    (NB: plan's step-2 anchors differ from S82 W1-2 microscopic
     anchors; see diagnostic section below. Gate executes plan's
     substitution chain as written.)

  Step 3 (simplification):
    LI/TD ratio        = 181.0 / 1.57 = 115.29      [python-verified]
    log10(LI/TD)       = 2.062 OOM                  [python-verified]
    F_stretch_target   = 115.29                     [if reconciled]
    H_tilde_DC_derived = H_tilde_LI_plan / F_stretch_derived

  Step 4 (direction, from canonical form):
    Microscopic F_stretch = (H_transit/H_Friedmann)^2 with
      H_transit   = dS_fold * dt_transit / Vol_SU3_Haar  [dim match]
      H_Friedmann = H_tilde_center                       [substrate emergent]
    PASS direction: F_stretch_derived within 0.5 OOM of 115.29.

PASS/FAIL/INFO (plan §W7-1 step 9):
  PASS   : [1] H_tilde_DC_derived in [4.599e-3, 4.829e-3]
           AND [2] |log10(H_tilde_DC_derived/H_tilde_TD_plan)| <= 0.196
           AND [3] |log10(F_stretch_derived/115.29)| <= 0.5
  FAIL   : [1] fails OR [3] > 1.0
  INFO   : [1] fails AND 0.5 < [3] <= 1.0 (partial reconciliation)

Machinery pins (plan §7):
  L_max=10, scheme=Zubarev, convention=W1-G1-Branch-B,
  N_eval=1024, scan_range=[4.599e-3, 4.829e-3], step_size=1e-5,
  tolerance=0.91% log-DC, random_seed=42.

Outputs:
  computations/session-85/s85_w7_baseline_htilde.npz
  computations/session-85/s85_w7_baseline_htilde.png
Verdict appended to computations/session-85/s85_gate_verdicts.txt with
S85+ dual-SHA (content_sha256 + audit_sha256).
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

# CPU thread cap — scalar gate; GPU eigen not required at this gate.
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
    dS_fold,
    dt_transit,
    Vol_SU3_Haar,
    H_tilde_lo,
    H_tilde_hi,
    H_tilde_center,
    H_tilde_canonical_TD,
    H_tilde_canonical_LI,
    M_KK,
    tau_fold,
    PI,
)


# ----------------------------------------------------------------------------
# Section 0 — input-pin map and closure SHA (gate-verdicts.md §Pre-Registration)
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
    _HERE / "s84_w1a_baseline_htilde_sensitivity.py",
    _HERE / "s82_w1_2_unified_as_79_full.py",
    _HERE / "s83_w1_g1_ic_scheme_derivation.py",
]
for _sf in _static_files:
    if _sf.exists():
        INPUT_PINS[_sf.name] = _file_sha(_sf)
    else:
        INPUT_PINS[_sf.name] = "MISSING"

# Machinery pins (plan §7 verbatim)
L_max = 10  # (local) Zubarev canonical, W1-G1 Branch-B (plan §7)
scheme = "Zubarev"  # (local) plan §7, NO convention-shopping
convention = "W1-G1-Branch-B"  # (local) plan §7
N_eval = 1024  # (local) Mukhanov-mode samples (plan §7)
step_size = 1e-5  # (local) H_tilde grid step (plan §7)
tolerance_log_DC_pct = 0.91  # (local) S84 W1a-1 band width (plan §7)
random_seed = 42  # (local) template-output discriminator only (plan §7)

# Plan-specific target pins (plan §10 step 3)
F_stretch_target_plan = 181.0 / 1.57  # (local) plan §10 step 3 (= 115.29)
log10_LI_TD_plan = np.log10(F_stretch_target_plan)  # (local) = 2.062
RATIO_TOL_LOG10 = 0.196  # (local) plan §9 (RATIO tolerance = S84 Delta_OOM)
RECON_TOL_OOM = 0.5  # (local) plan §9 (reconciliation PASS bound)
RECON_INFO_OOM = 1.0  # (local) plan §9 (reconciliation INFO upper bound)

# Register scan / convention pins
INPUT_PINS["L_max"] = f"{L_max:d}"
INPUT_PINS["scheme"] = scheme
INPUT_PINS["convention"] = convention
INPUT_PINS["N_eval"] = f"{N_eval:d}"
INPUT_PINS["scan_lo"] = f"{H_tilde_lo:.10e}"
INPUT_PINS["scan_hi"] = f"{H_tilde_hi:.10e}"
INPUT_PINS["step_size"] = f"{step_size:.10e}"
INPUT_PINS["tolerance_log_DC_pct"] = f"{tolerance_log_DC_pct:.4f}"
INPUT_PINS["random_seed"] = f"{random_seed:d}"
INPUT_PINS["F_stretch_target_plan"] = f"{F_stretch_target_plan:.6f}"
INPUT_PINS["log10_LI_TD_plan"] = f"{log10_LI_TD_plan:.6f}"
INPUT_PINS["RATIO_TOL_LOG10"] = f"{RATIO_TOL_LOG10:.6f}"
INPUT_PINS["RECON_TOL_OOM"] = f"{RECON_TOL_OOM:.6f}"
INPUT_PINS["RECON_INFO_OOM"] = f"{RECON_INFO_OOM:.6f}"
INPUT_PINS["dS_fold"] = f"{dS_fold:.10e}"
INPUT_PINS["dt_transit"] = f"{dt_transit:.10e}"
INPUT_PINS["Vol_SU3_Haar"] = f"{Vol_SU3_Haar:.10e}"
INPUT_PINS["H_tilde_center"] = f"{H_tilde_center:.10e}"
INPUT_PINS["H_tilde_canonical_TD"] = f"{H_tilde_canonical_TD:.10e}"
INPUT_PINS["H_tilde_canonical_LI"] = f"{H_tilde_canonical_LI:.10e}"

CLOSURE_INPUT = json.dumps(INPUT_PINS, sort_keys=True, separators=(",", ":"))
CLOSURE_SHA = hashlib.sha256(CLOSURE_INPUT.encode("utf-8")).hexdigest()

print("=" * 78)
print("S85 W7-1: BASELINE-HTILDE-DERIVATION")
print("=" * 78)
print(f"closure SHA-256 (64 char): {CLOSURE_SHA}")
print(f"closure SHA-256 (16 head): {CLOSURE_SHA[:16]}")
print()
print("--- input pin SHAs and values ---")
for _k, _v in INPUT_PINS.items():
    print(f"  {_k:<32s}: {_v}")
print()


# ----------------------------------------------------------------------------
# Section 1 — Plan Step 1/2 definitions (canonical-constants + plan)
# ----------------------------------------------------------------------------
# Plan Step 1 definitions:
#   H_transit = (1/Vol_SU3) * dS_fold/dtau  [Jensen-parameter rate]
# Units: dS_fold is dS/dtau (dimensionless), Vol_SU3 dimensionless,
# dt_transit in M_KK^{-1}. The plan does NOT fix a normalization from
# "per dtau" to "per M_KK"; we use dt_transit as the canonical transit
# timescale to convert the dimensionless rate into M_KK units. This is
# the simplest choice consistent with M_KK as the only transit scale.
H_transit_natural = dS_fold / Vol_SU3_Haar  # (local) plan step 1, per-dtau rate
H_transit = H_transit_natural * dt_transit  # (local) M_KK-normalized (by dt_transit)

# Plan Step 1: H_Friedmann = (8pi G/3 * rho_eff)^{1/2}
# Substrate emergent: pre-registered as the band-centre H_tilde.
H_Friedmann = H_tilde_center  # (local) S84 W1a-1 PASS-window center

# Plan Step 2 anchors (plan's convention)
H_tilde_TD_plan = H_tilde_center * 1.57  # (local) plan §10 step 2
H_tilde_LI_plan = H_tilde_center * 181.0  # (local) plan §10 step 2

# Sanity-assert plan arithmetic (Python-verified substitution chain)
assert abs(log10_LI_TD_plan - 2.062) < 0.01, (
    f"log10(181/1.57)={log10_LI_TD_plan:.4f} != 2.062 (plan claims ~2.06)"
)

print("--- plan step 1/2 definitions (canonical-constants + plan) ---")
print(f"  dS_fold                 = {dS_fold:.6e}")
print(f"  Vol_SU3_Haar            = {Vol_SU3_Haar:.6e}")
print(f"  dt_transit              = {dt_transit:.6e}  (M_KK^-1)")
print(f"  H_transit_natural       = {H_transit_natural:.6e}  (= dS_fold/Vol_SU3)")
print(f"  H_transit (M_KK normd)  = {H_transit:.6e}  (= H_transit_natural*dt_transit)")
print(f"  H_Friedmann (M_KK)      = {H_Friedmann:.6e}  (= H_tilde_center)")
print(f"  H_tilde_TD_plan         = {H_tilde_TD_plan:.6e}  (= center*1.57)")
print(f"  H_tilde_LI_plan         = {H_tilde_LI_plan:.6e}  (= center*181)")
print()


# ----------------------------------------------------------------------------
# Section 2 — Plan Step 3/4: reconciliation hypothesis and microscopic derivation
# ----------------------------------------------------------------------------
# Plan Step 3:
#   F_stretch_target = LI/TD ratio = 181/1.57 = 115.29 (python-verified)
F_stretch_target = F_stretch_target_plan  # (local) alias for clarity

# Plan Step 4 microscopic derivation:
#   F_stretch_derived = (H_transit/H_Friedmann)^2
F_stretch_derived = (H_transit / H_Friedmann) ** 2  # (local)
log10_F_stretch_derived = np.log10(F_stretch_derived)  # (local)

# Plan Step 3 H_tilde_DC derivation:
#   H_tilde_DC_derived = H_tilde_LI_plan / F_stretch_derived
H_tilde_DC_derived = H_tilde_LI_plan / F_stretch_derived  # (local)

print("--- plan step 3 reconciliation target ---")
print(f"  F_stretch_target         = {F_stretch_target:.4f}   (= 181/1.57)")
print(f"  log10(F_stretch_target)  = {log10_LI_TD_plan:.4f}")
print()
print("--- plan step 4 microscopic derivation ---")
print(
    f"  F_stretch_derived        = (H_transit/H_Friedmann)^2"
)
print(
    f"                           = ({H_transit:.6e}/{H_Friedmann:.6e})^2"
)
print(f"                           = {F_stretch_derived:.4f}")
print(f"  log10(F_stretch_derived) = {log10_F_stretch_derived:.4f}")
print()
print("--- plan step 3 H_tilde_DC_derived ---")
print(f"  H_tilde_DC_derived = H_tilde_LI_plan / F_stretch_derived")
print(f"                     = {H_tilde_LI_plan:.6e} / {F_stretch_derived:.4f}")
print(f"                     = {H_tilde_DC_derived:.6e}")
print()


# ----------------------------------------------------------------------------
# Section 2b — S82 W1-2 anchor cross-check (diagnostic only)
# ----------------------------------------------------------------------------
S82_TD_over_center = H_tilde_canonical_TD / H_tilde_center  # (local)
S82_LI_over_TD = H_tilde_canonical_LI / H_tilde_canonical_TD  # (local)
log10_S82_TD_over_LI = np.log10(
    H_tilde_canonical_TD / H_tilde_canonical_LI
)  # (local)
print("--- S82 W1-2 anchor cross-check (diagnostic) ---")
print(f"  H_tilde_canonical_TD (S82) = {H_tilde_canonical_TD:.6e}")
print(f"  H_tilde_canonical_LI (S82) = {H_tilde_canonical_LI:.6e}")
print(f"  S82 TD/center              = {S82_TD_over_center:.4f}")
print(f"                               (plan claims 1.57; S82 gives {S82_TD_over_center:.4f})")
print(f"  log10(S82 TD/LI)           = {log10_S82_TD_over_LI:.4f}")
print(f"                               (plan claims ~2.06; S82 gives {log10_S82_TD_over_LI:.4f})")
print("  NOTE: plan's step-2 anchors appear to conflate A_s-ratio with")
print("        H_tilde-ratio. We execute the plan's chain LITERALLY as")
print("        written (using plan anchors). Inconsistency documented.")
print()


# ----------------------------------------------------------------------------
# Section 3 — PASS/FAIL/INFO evaluation per plan §9 AND-conjunction
# ----------------------------------------------------------------------------
# Criterion 1: H_tilde_DC_derived in S84 W1a-1 PASS window
in_window = (H_tilde_DC_derived >= H_tilde_lo) and (H_tilde_DC_derived <= H_tilde_hi)

# Criterion 2: |log10(H_tilde_DC_derived / H_tilde_TD_plan)| <= RATIO_TOL_LOG10
log10_ratio_DC_TD = float(np.log10(H_tilde_DC_derived / H_tilde_TD_plan))  # (local)
ratio_check = abs(log10_ratio_DC_TD) <= RATIO_TOL_LOG10

# Criterion 3: |log10(F_stretch_derived/F_stretch_target)| <= RECON_TOL_OOM
log10_recon_residual = float(
    np.log10(F_stretch_derived / F_stretch_target)
)  # (local)
recon_check = abs(log10_recon_residual) <= RECON_TOL_OOM
recon_info_band = RECON_TOL_OOM < abs(log10_recon_residual) <= RECON_INFO_OOM

# Verdict per plan §9:
#   PASS = (1) AND (2) AND (3)
#   INFO = (NOT 1) AND (0.5 < |recon| <= 1.0)
#   FAIL = otherwise
if in_window and ratio_check and recon_check:
    verdict = "PASS"
elif (not in_window) and recon_info_band:
    verdict = "INFO"
else:
    verdict = "FAIL"

print("--- PASS criteria (plan §9 AND-conjunction) ---")
print(
    f"  [1] H_tilde_DC_derived in window: "
    f"{H_tilde_DC_derived:.6e} in [{H_tilde_lo:.3e}, {H_tilde_hi:.3e}]  =>  {in_window}"
)
print(
    f"  [2] |log10(DC_derived/TD_plan)| <= {RATIO_TOL_LOG10}: "
    f"|{log10_ratio_DC_TD:.4f}| <= {RATIO_TOL_LOG10}  =>  {ratio_check}"
)
print(
    f"  [3] |log10(F_derived/F_target)| <= {RECON_TOL_OOM}: "
    f"|{log10_recon_residual:.4f}| <= {RECON_TOL_OOM}  =>  {recon_check}"
)
print()
print(f"  VERDICT: {verdict}")
print()


# ----------------------------------------------------------------------------
# Section 4 — .npz / .png artifacts
# ----------------------------------------------------------------------------
npz_path = _HERE / "s85_w7_baseline_htilde.npz"
png_path = _HERE / "s85_w7_baseline_htilde.png"

# Also build a small H_tilde scan array across the pre-registered window for
# the .npz (plan §6 "H_tilde_scan[k]")
N_scan = 64  # (local) scan resolution for .npz + plot
H_tilde_scan = np.linspace(H_tilde_lo, H_tilde_hi, N_scan)  # (local)
# F_stretch_trajectory across scan (window-relative)
F_stretch_trajectory = (H_tilde_LI_plan / H_tilde_scan)  # (local) per plan step 3
H_transit_array = np.full_like(H_tilde_scan, H_transit)  # (local) constant across scan

np.savez(
    npz_path,
    # Primary derived outputs
    H_tilde_DC_derived=H_tilde_DC_derived,
    F_stretch_derived=F_stretch_derived,
    F_stretch_target=F_stretch_target,
    # Plan-defined anchors
    H_tilde_lo=H_tilde_lo,
    H_tilde_hi=H_tilde_hi,
    H_tilde_center=H_tilde_center,
    H_tilde_TD_plan=H_tilde_TD_plan,
    H_tilde_LI_plan=H_tilde_LI_plan,
    # Microscopic inputs
    H_transit=H_transit,
    H_transit_natural=H_transit_natural,
    H_Friedmann=H_Friedmann,
    dS_fold_pinned=dS_fold,
    dt_transit_pinned=dt_transit,
    Vol_SU3_Haar_pinned=Vol_SU3_Haar,
    # S82 cross-check anchors
    H_tilde_canonical_TD=H_tilde_canonical_TD,
    H_tilde_canonical_LI=H_tilde_canonical_LI,
    # Scan arrays (plan §6)
    H_tilde_scan=H_tilde_scan,
    F_stretch_trajectory=F_stretch_trajectory,
    H_transit_array=H_transit_array,
    # CC residuals
    log10_ratio_DC_TD=log10_ratio_DC_TD,
    log10_recon_residual=log10_recon_residual,
    log_DC_fraction=tolerance_log_DC_pct,
    # Gate-state flags
    in_window=in_window,
    ratio_check=ratio_check,
    recon_check=recon_check,
    verdict=verdict,
    # 4-tuple
    value=H_tilde_DC_derived,
    scheme=scheme,
    convention=convention,
    L_max=L_max,
    # SHAs
    closure_sha=CLOSURE_SHA,
)

# Plot — 0.91% DC window with TD/LI anchors and derived H_tilde_DC
fig, ax = plt.subplots(figsize=(10.2, 6.2), dpi=130)
ax.axvspan(
    H_tilde_lo,
    H_tilde_hi,
    color="#dde5f0",
    alpha=0.85,
    label=f"S84 W1a-1 PASS window (0.91% log-DC)",
)
ax.axvline(
    H_tilde_center, color="k", ls="--", lw=1.3, label=f"H̃_center = {H_tilde_center:.4e}"
)
ax.axvline(
    H_tilde_TD_plan,
    color="tab:blue",
    ls=":",
    lw=2.2,
    label=f"H̃_TD (plan, ×1.57) = {H_tilde_TD_plan:.4e}",
)
ax.axvline(
    H_tilde_canonical_TD,
    color="tab:blue",
    ls="-",
    lw=1.1,
    alpha=0.6,
    label=f"H̃_TD (S82 canonical) = {H_tilde_canonical_TD:.4e}",
)
ax.axvline(
    H_tilde_canonical_LI,
    color="tab:cyan",
    ls="-",
    lw=1.1,
    alpha=0.6,
    label=f"H̃_LI (S82 canonical) = {H_tilde_canonical_LI:.4e}",
)
ax.axvline(
    H_tilde_DC_derived,
    color="tab:red",
    ls="-",
    lw=3.0,
    label=f"H̃_DC_derived = {H_tilde_DC_derived:.4e}",
)
# Scatter across scan showing F_stretch trajectory as a decorative layer
ax_sec = ax.twinx()
ax_sec.plot(H_tilde_scan, F_stretch_trajectory, color="tab:green", lw=1.2, alpha=0.7)
ax_sec.axhline(
    F_stretch_target,
    color="tab:orange",
    ls="--",
    lw=1.4,
    label=f"F_stretch target = {F_stretch_target:.2f}",
)
ax_sec.axhline(
    F_stretch_derived,
    color="tab:red",
    ls=":",
    lw=1.8,
    label=f"F_stretch derived = {F_stretch_derived:.2f}",
)
ax_sec.set_ylabel("F_stretch (green = H̃_LI/H̃_scan)")
ax_sec.set_yscale("log")

ax.set_xscale("log")
ax.set_xlabel("H̃ (M_KK units)")
ax.set_ylabel("(log axis)")
ax.set_title(
    f"S85-W7-1 BASELINE-HTILDE-DERIVATION — verdict {verdict}\n"
    f"F_stretch_derived={F_stretch_derived:.2f} vs target={F_stretch_target:.2f}, "
    f"|log10-recon|={abs(log10_recon_residual):.3f} OOM"
)
ax.legend(loc="upper left", fontsize=8, framealpha=0.9)
ax_sec.legend(loc="upper right", fontsize=8, framealpha=0.9)
ax.grid(True, alpha=0.3, which="both")
plt.tight_layout()
plt.savefig(png_path, dpi=130)
plt.close()

print("--- outputs ---")
print(f"  .npz: {npz_path.name} ({npz_path.stat().st_size} bytes)")
print(f"  .png: {png_path.name} ({png_path.stat().st_size} bytes)")
print()


# ----------------------------------------------------------------------------
# Section 5 — Verdict-line append with S85+ dual-SHA schema
# ----------------------------------------------------------------------------
GATE_ID = "S85-W7-BASELINE-HTILDE-DERIVATION"
verdict_path = _HERE / "s85_gate_verdicts.txt"

# Content SHA = SHA of the .npz artifact (S85+ schema)
content_sha = _file_sha(npz_path)
# Audit SHA = closure SHA over the ordered input-pin map
audit_sha = CLOSURE_SHA

value_str = f"{H_tilde_DC_derived:.6e}"
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
print(f"  path: {verdict_path.relative_to(_HERE.parent)}")
print(f"  line: {canonical_line}")
print(f"  dual: {dual_sha_comment}")
print()
print(
    f"FINAL 4-tuple: (value={value_str}, scheme={scheme}, "
    f"convention={convention}, L_max={L_max})"
)

# Exit 0: script health OK. Verdict PASS/FAIL/INFO is data per math-scripts.md.
sys.exit(0)
