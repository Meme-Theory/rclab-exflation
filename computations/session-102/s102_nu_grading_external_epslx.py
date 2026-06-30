#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S102-NU-GRADING-EXTERNAL-EPSLX  (Session 102, Wave 4, item 17)

scale-from-gap-eq / shape-from-epsilon_LX division of labor for the neutrino
generation grading.

HYPOTHESIS (plan §W4-17):
  An external non-LI epsilon_LX structure (the §VII.BL corollary design rule: an
  external non-LI fibre connection breaking W2 while PRESERVING the grading)
  supplies the neutrino generation shape-steepness Y_3/Y_2 = 2.4882512 (rel <= 5%)
  -- which the gap-equation route provably COULD NOT (W3-4 shape-FAIL +39.7%) --
  WHILE the gap equation supplies the scale (x8.6-10.5); epsilon_LX
  substrate-motivated NOT fitted.

SUBSTRATE FRAMING (PARTICLE-class):
  The §VII.BL Generation-Blindness Obstruction is a STRUCTURAL wall: the
  left-invariant (LI) fibre structure of D_K is generation-blind up to the
  permanent residual R_cross = 1.019704. The gap-equation route inherits this
  blindness => its generation SHAPE is nearly flat (the scale CANCELS in any
  generation ratio). The corollary design rule: the ONLY escape is an EXTERNAL
  non-LI fibre connection breaking the left-invariance (W2) while preserving the
  chiral grading. epsilon_LX is the strength of that external connection; its
  generation-dependent action g_eps(C_2(g)) IS the shape leg. The gap eq supplies
  WHERE the neutrino sector sits (scale); epsilon_LX supplies HOW STEEPLY it
  grades across generations (shape).
  Direction: D_K fibre-connection geometry (external non-LI part)
             -> generation-graded shape factor -> neutrino Y_3/Y_2 steepness,
             with the gap-eq scale orthogonal.

VERDICT LOGIC (plan rubric):
  PASS  = substrate-MOTIVATED external epsilon_LX reproduces Y_3/Y_2 (rel<=5%)
          AND scale leg in [8.6, 10.5].
  FAIL  = no admissible external structure lifts the grading to within 5%.
  INFO  = the external structure DOES lift the grading to the target, but the
          epsilon_LX VALUE required is NOT substrate-motivated (a fit) ->
          re-route to a fibre-connection-geometry derivation workshop.

NUMBERS first, gate second, interpretation third.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU fallback cap (before numpy)

import sys
import json
import hashlib
import numpy as np  # noqa: E402

# --- canonical constants (MANDATORY import; never hardcode framework constants) ---
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))
from canonical_constants import R_cross_yukawa_t1_t2, tau_fold  # noqa: E402

# =====================================================================
# Section 1 -- INPUT PINS (SHA-256 of every file the script reads)
# =====================================================================
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

CANON_PATH = os.path.join(ROOT, "computations", "_shared", "canonical_constants.py")
MD_GAPEQ_PATH = os.path.join(ROOT, "computations", "session-101", "s101_d5_md_gapeq.npz")
SCRIPT_PATH = os.path.abspath(__file__)

EXPECTED_SHA = {
    "canonical_constants": "9f2fe9983ecbbb76a2ba1b3e951cf9275deda8d7f2241576ef23b7f728ba1047",
    "md_gapeq": "d0267a07b1aec3da587b33daebf5a9da1ecd50d37c2c4497a6600c915e383797",
}


def _sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


sha_canon = _sha256_file(CANON_PATH)
sha_md = _sha256_file(MD_GAPEQ_PATH)
sha_script = _sha256_file(SCRIPT_PATH)

print("=" * 70)
print("CF-S102-NU-GRADING-EXTERNAL-EPSLX  -- input SHA-256 pins")
print("=" * 70)
print(f"  canonical_constants.py : {sha_canon}")
print(f"  s101_d5_md_gapeq.npz   : {sha_md}")
print(f"  script (this file)     : {sha_script}")

assert sha_canon == EXPECTED_SHA["canonical_constants"], "canonical_constants.py SHA mismatch"
assert sha_md == EXPECTED_SHA["md_gapeq"], "s101_d5_md_gapeq.npz SHA mismatch"
print("  [SHA pins OK]")
print(f"  canonical R_cross_yukawa_t1_t2 = {R_cross_yukawa_t1_t2}")
print(f"  canonical tau_fold             = {tau_fold}")

# =====================================================================
# Section 2 -- LOAD S101 D5 gap-equation data
# =====================================================================
d = np.load(MD_GAPEQ_PATH, allow_pickle=True)

C2 = np.asarray(d["am1_C2"], dtype=float)          # [0, 4/3, 3]  generation Casimirs (Peter-Weyl sectors)
Y_S99 = np.asarray(d["Y_S99"], dtype=float)        # [0, 4.79357, 11.92760]  W3-1 required Yukawas (seesaw/oscillation-anchored)
dC2 = float(d["DeltaC2"])                          # 5/3  = C_2(3) - C_2(2)
dlnY_req = float(d["d_lnYreq_dC2"])                # 0.546948  required log-slope (substrate: oscillation-anchored masses)
dlnY_sol = float(d["d_lnYsol_dC2"])                # 0.243279  gap-eq SOLVED log-slope (substrate: KS-LINEAR stationarity)
shape_required = float(d["shape_required"])        # 2.4882511868  (W3-1 target)
shape_dev_gapeq = float(d["shape_dev"])            # 0.397167  W3-4 shape-FAIL (+39.7% too flat)
rescale_A = float(d["rescale_A"])                  # 10.4878  scale leg (upper)
rescale_B = float(d["rescale_B"])                  # 8.6377   scale leg (lower)
r_sol = float(d["r_sol"])                          # 9.5179   gap-eq scale ratio
scale_lo = float(d["scale_band_lo"])               # 8.6
scale_hi = float(d["scale_band_hi"])               # 10.5
shape_tol = float(d["shape_tol"])                  # 0.05  (RATIO 5% on shape)
gapeq_audit_sha = str(d["audit_sha256"])
gapeq_content_sha = str(d["content_sha256"])

# pre-registered targets / pins
SHAPE_TARGET = 2.4882512        # (local) plan §W4-17 strict target (Y_3/Y_2), W3-1 requirement
TAU_SHAPE = 0.05                # (local) RATIO tol 5% on shape steepness (plan pin)
SCALE_BAND = (8.6, 10.5)        # (local) gap-eq scale leg band (plan pin)
N_EVAL = 3                      # (local) three generations (plan machinery pin)
L_MAX = 10                      # (local) canonical Peter-Weyl truncation (plan machinery pin)

print()
print("-" * 70)
print("Section 2 -- gap-equation substrate quantities (S101 D5)")
print("-" * 70)
print(f"  generation Casimirs C_2(g)   = {C2}   (sectors (0,0),(1,0),(1,1))")
print(f"  W3-1 required Yukawas Y_S99   = {Y_S99}")
print(f"  Delta C_2 (gen 3 - gen 2)     = {dC2:.10f}  (= 5/3)")
print(f"  d ln Y_req / d C_2 (required) = {dlnY_req:.10f}   [oscillation-anchored masses]")
print(f"  d ln Y_sol / d C_2 (gap-eq)   = {dlnY_sol:.10f}   [KS-LINEAR stationarity]")
print(f"  shape_required (W3-1)         = {shape_required:.10f}")
print(f"  gap-eq shape_dev (W3-4 FAIL)  = {shape_dev_gapeq:+.6f}  (too flat)")
print(f"  scale leg rescale_A / _B      = {rescale_A:.6f} / {rescale_B:.6f}")
print(f"  gap-eq scale ratio r_sol      = {r_sol:.6f}")

# =====================================================================
# Section 3 -- SUBSTITUTION CHAIN (explicit; plan §W4-17 substitution_chain)
# =====================================================================
# Step 1 (definitions): Y_g = Scale_gap * h(C_2(g)); §VII.BL: h NEARLY FLAT
#         across generations (LI generation-blindness, residual R_cross).
# Step 2 (gap-eq shape ratio): Scale_gap CANCELS in the 3/2 ratio =>
#         (Y_3/Y_2)^gap = h(C_2(3))/h(C_2(2)) = exp(dlnY_sol * dC2).
# Step 3 (external eps_LX grading): Y_g^full = Scale_gap*h(C_2)*g_eps(C_2);
#         (Y_3/Y_2)^full = (Y_3/Y_2)^gap * (g_eps,3/g_eps,2).
# Step 4 (division of labor): scale leg from gap-eq (in-band); shape leg from
#         eps_LX. To hit the target from the +39.7%-too-flat gap value, the
#         external grading must supply g_eps,3/g_eps,2 = exp(missing_slope*dC2).
# Step 5 (direction): gap eq provably shape-flat (scale cancels); ONLY the
#         external non-LI grading lifts the steepness.
print()
print("-" * 70)
print("Section 3 -- substitution chain (numbers)")
print("-" * 70)

# Step 2: gap-eq solved shape ratio (scale cancels)
gap_shape_ratio = float(np.exp(dlnY_sol * dC2))                    # (local)
gap_shape_dev_check = (shape_required - gap_shape_ratio) / shape_required  # (local) reproduce W3-4 sign/magnitude
print(f"  [Step 2] (Y3/Y2)^gap = exp(dlnY_sol*dC2)        = {gap_shape_ratio:.10f}")
print(f"           gap shape shortfall (req-gap)/req       = {gap_shape_dev_check:+.6f}")
print(f"           cf npz shape_dev                        = {shape_dev_gapeq:+.6f}  "
      f"(|diff|={abs(gap_shape_dev_check-shape_dev_gapeq):.2e})")

# Step 4: external grading factor REQUIRED to close the shape gap
geps_ratio_needed = shape_required / gap_shape_ratio              # (local)
missing_slope = dlnY_req - dlnY_sol                               # (local) per unit C_2
geps_ratio_from_slope = float(np.exp(missing_slope * dC2))        # (local) consistency form
print(f"  [Step 4] g_eps,3/g_eps,2 NEEDED (req/gap)        = {geps_ratio_needed:.10f}")
print(f"           missing_slope = dlnY_req - dlnY_sol      = {missing_slope:.10f}  (per unit C_2)")
print(f"           g_eps,3/g_eps,2 from missing_slope       = {geps_ratio_from_slope:.10f}")
print(f"           consistency |needed - slope-form|        = {abs(geps_ratio_needed-geps_ratio_from_slope):.2e}")

# Full reconstruction: scale-from-gap-eq * shape-from-eps_LX
Y3Y2_full = gap_shape_ratio * geps_ratio_from_slope              # (local)
shape_rel_err = abs(Y3Y2_full - SHAPE_TARGET) / SHAPE_TARGET     # (local)
print(f"  [recon] (Y3/Y2)^full = gap_shape * g_eps_ratio  = {Y3Y2_full:.10f}")
print(f"          rel error vs target {SHAPE_TARGET}        = {shape_rel_err:.3e}")

# Scale leg: gap-eq scale window vs band
scale_in_band = (rescale_B >= scale_lo - 1e-9) and (rescale_A <= scale_hi + 1e-9)  # (local)
print(f"  [scale] gap-eq scale window [{rescale_B:.4f}, {rescale_A:.4f}] "
      f"vs band [{scale_lo}, {scale_hi}]  -> in-band = {scale_in_band}")

# =====================================================================
# Section 4 -- SUBSTRATE-MOTIVATION TEST for eps_LX (PASS vs INFO discriminator)
# =====================================================================
# The shape leg can ALWAYS be made to hit the target because the external
# grading factor required, g_eps,3/g_eps,2, is EXACTLY req/gap (residual ~1e-16).
# The decisive question (plan INFO_meaning): is the eps_LX magnitude
# (missing_slope) INDEPENDENTLY derived from fibre geometry, or is it the
# residual back-out (a fit)?
#
# Substrate-motivation criterion (pre-registered logic):
#   eps_LX is SUBSTRATE-MOTIVATED iff its connection-strength magnitude is pinned
#   by an INDEPENDENT fibre-geometry derivation (a canonical constant / a derived
#   geometric scale) that can be confronted against missing_slope -- i.e. the
#   external grading is NOT merely defined to be (required - gap-eq).
#
# Knowledge-MCP audit (documented in WP): there is NO canonical constant for
#   eps_LX / d_lnYreq_dC2 / delta_A_nLI. The canonical R_cross_yukawa_t1_t2
#   provenance explicitly tags the external eps_LX as
#   "NON-PROMOTION-BY-HELD-NUMBER (sign-lock differentia); HELD number, NOT a
#   framework prediction. local-diagnostic-anchor." (S97). The S97 W3 plan posits
#   A_nLI = A_homog + delta_A "pinned, NOT discovered at runtime" -- a STRUCTURAL
#   posit (existence/necessity of the external connection), with NO independent
#   numerical magnitude for delta_A read from fibre geometry.
print()
print("-" * 70)
print("Section 4 -- substrate-motivation test for eps_LX")
print("-" * 70)

# Has an independent fibre-geometry magnitude been pinned for eps_LX?
# (encoded as a script-level fact, cross-checked against the canonical provenance
#  string which self-identifies the value as HELD, not a framework prediction)
canon_provenance_flags_held = True   # R_cross provenance: "HELD number, NOT a framework prediction"
independent_epsLX_magnitude_exists = False  # no canonical eps_LX / delta_A_nLI; S97 posit only

# The required grading is the residual back-out (exact by construction):
geps_is_residual_backout = (abs(geps_ratio_needed - geps_ratio_from_slope) < 1e-9)  # (local)

eps_LX_substrate_motivated = (independent_epsLX_magnitude_exists
                              and not canon_provenance_flags_held)

print(f"  external grading hits target (rel<=5%)         : {shape_rel_err <= TAU_SHAPE}")
print(f"  required g_eps ratio == residual back-out      : {geps_is_residual_backout}")
print(f"  independent fibre-geometry eps_LX magnitude?   : {independent_epsLX_magnitude_exists}")
print(f"  canonical provenance flags eps_LX as HELD?     : {canon_provenance_flags_held}")
print(f"  => eps_LX SUBSTRATE-MOTIVATED                  : {eps_LX_substrate_motivated}")

# =====================================================================
# Section 5 -- VERDICT (plan rubric)
# =====================================================================
shape_ok = shape_rel_err <= TAU_SHAPE
scale_ok = scale_in_band

if not shape_ok:
    verdict = "FAIL"
    verdict_reason = "no admissible external structure lifts grading to within 5%"
elif shape_ok and scale_ok and eps_LX_substrate_motivated:
    verdict = "PASS"
    verdict_reason = "substrate-motivated eps_LX reproduces shape; scale in-band; §VII.BL corollary operationalized"
else:
    # external structure DOES lift the grading to target, but eps_LX is a fit
    verdict = "INFO"
    verdict_reason = ("external grading reproduces Y3/Y2 (rel=%.1e) and scale in-band, "
                      "but eps_LX magnitude is the residual back-out (HELD, NOT substrate-motivated) "
                      "-> re-route to fibre-connection-geometry derivation workshop") % shape_rel_err

print()
print("=" * 70)
print(f"  VERDICT: {verdict}")
print(f"  reason : {verdict_reason}")
print("=" * 70)

# =====================================================================
# Section 6 -- save data + plot
# =====================================================================
NPZ_PATH = os.path.join(HERE, "s102_nu_grading_external_epslx.npz")
PNG_PATH = os.path.join(HERE, "s102_nu_grading_external_epslx.png")

np.savez(
    NPZ_PATH,
    C2=C2,
    Y_S99=Y_S99,
    dC2=dC2,
    dlnY_req=dlnY_req,
    dlnY_sol=dlnY_sol,
    missing_slope=missing_slope,
    shape_required=shape_required,
    shape_target=SHAPE_TARGET,
    gap_shape_ratio=gap_shape_ratio,
    gap_shape_dev_check=gap_shape_dev_check,
    shape_dev_gapeq=shape_dev_gapeq,
    geps_ratio_needed=geps_ratio_needed,
    geps_ratio_from_slope=geps_ratio_from_slope,
    Y3Y2_full=Y3Y2_full,
    shape_rel_err=shape_rel_err,
    shape_tol=TAU_SHAPE,
    rescale_A=rescale_A,
    rescale_B=rescale_B,
    r_sol=r_sol,
    scale_band=np.array(SCALE_BAND),
    scale_in_band=scale_in_band,
    shape_ok=shape_ok,
    scale_ok=scale_ok,
    eps_LX_substrate_motivated=eps_LX_substrate_motivated,
    independent_epsLX_magnitude_exists=independent_epsLX_magnitude_exists,
    canon_provenance_flags_held=canon_provenance_flags_held,
    R_cross_yukawa_t1_t2=R_cross_yukawa_t1_t2,
    verdict=verdict,
    verdict_reason=verdict_reason,
    gapeq_audit_sha=gapeq_audit_sha,
    gapeq_content_sha=gapeq_content_sha,
    tau_anchor=tau_fold,
    L_max=L_MAX,
    N_eval=N_EVAL,
)
print(f"  data saved: {NPZ_PATH}")

# plot: generation grading -- gap-eq (flat) vs gap+eps_LX (steep) vs required
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # left: log Y vs C_2 -- slopes
    c2_line = np.linspace(C2[1], C2[2], 50)  # (local) gen 2 -> gen 3 segment
    # anchor at gen 2 (set ln Y_2 = 0 reference)
    lnY_gap = dlnY_sol * (c2_line - C2[1])    # (local)
    lnY_full = dlnY_req * (c2_line - C2[1])   # (local) gap + eps_LX = required slope
    ax1.plot(c2_line, lnY_gap, "b-", lw=2.2,
             label=f"gap-eq (LI, flat): slope={dlnY_sol:.4f}")
    ax1.plot(c2_line, lnY_full, "r-", lw=2.2,
             label=f"gap + eps_LX (required): slope={dlnY_req:.4f}")
    ax1.fill_between(c2_line, lnY_gap, lnY_full, color="orange", alpha=0.25,
                     label=f"eps_LX shape leg (missing slope={missing_slope:.4f})")
    ax1.scatter([C2[1], C2[2]], [0.0, np.log(shape_required)], c="k", zorder=5, s=55,
                label="W3-1 required (gen 2, gen 3)")
    ax1.set_xlabel(r"generation Casimir $C_2(g)$")
    ax1.set_ylabel(r"$\ln(Y_g / Y_2)$")
    ax1.set_title("Generation grading: LI gap-eq flat vs external non-LI steep")
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(alpha=0.3)

    # right: Y_3/Y_2 ratio comparison bar
    labels = ["gap-eq\n(LI, flat)", "gap + eps_LX\n(full)", "W3-1\nrequired"]
    vals = [gap_shape_ratio, Y3Y2_full, SHAPE_TARGET]
    colors = ["#3b6fb0", "#c0392b", "#2e7d32"]
    bars = ax2.bar(labels, vals, color=colors, alpha=0.85)
    ax2.axhline(SHAPE_TARGET, color="green", ls="--", lw=1.3, alpha=0.7)
    ax2.axhspan(SHAPE_TARGET * (1 - TAU_SHAPE), SHAPE_TARGET * (1 + TAU_SHAPE),
                color="green", alpha=0.12, label=f"+/-{int(TAU_SHAPE*100)}% band")
    for b, v in zip(bars, vals):
        ax2.text(b.get_x() + b.get_width() / 2, v + 0.03, f"{v:.4f}",
                 ha="center", va="bottom", fontsize=9)
    ax2.set_ylabel(r"$Y_3 / Y_2$ (shape steepness)")
    ax2.set_title(f"VERDICT: {verdict}  (shape rel err = {shape_rel_err:.1e})")
    ax2.legend(fontsize=8)
    ax2.grid(alpha=0.3, axis="y")

    fig.suptitle("CF-S102-NU-GRADING-EXTERNAL-EPSLX  --  scale-from-gap-eq / shape-from-eps_LX",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(PNG_PATH, dpi=130)
    plt.close(fig)
    print(f"  plot saved: {PNG_PATH}")
except Exception as e:  # noqa: BLE001
    print(f"  [plot warning] {e}")

# =====================================================================
# Section 7 -- dual-SHA closure + verdict payload
# =====================================================================
# audit_sha256 inputs: ["script", "canonical", "pinmap", "s101_d5_md_gapeq.npz"]
# content_sha256 inputs: ["script"]
pinmap = {
    "gate_id": "CF-S102-NU-GRADING-EXTERNAL-EPSLX",
    "N_eval": str(N_EVAL),
    "L_max": str(L_MAX),
    "scheme": "FW",
    "convention": "RATIO",
    "shape_target": f"{SHAPE_TARGET}",
    "shape_tol": f"{TAU_SHAPE}",
    "scale_band": f"[{SCALE_BAND[0]},{SCALE_BAND[1]}]",
    "sha_canonical": sha_canon,
    "sha_md_gapeq": sha_md,
}


def _closure_hash(mapping):
    payload = json.dumps(mapping, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


audit_inputs = {
    "script": sha_script,
    "canonical": sha_canon,
    "pinmap": _closure_hash(pinmap),
    "s101_d5_md_gapeq.npz": sha_md,
}
audit_sha256 = _closure_hash(audit_inputs)
content_sha256 = sha_script  # content_sha256 inputs: ["script"]

# value payload (no single-quote chars; <= publication_precision 5 sig figs on derived)
value_payload = (
    f"shape_target={SHAPE_TARGET}_recon_Y3Y2={Y3Y2_full:.5f}_rel_err={shape_rel_err:.2e}_"
    f"gap_flat={gap_shape_ratio:.5f}_geps_ratio={geps_ratio_from_slope:.5f}_"
    f"missing_slope={missing_slope:.5f}_scale[{rescale_B:.4f},{rescale_A:.4f}]_in-band={scale_in_band}_"
    f"eps_LX-substrate-motivated={eps_LX_substrate_motivated}_HELD-not-prediction_"
    f"shape-lifts-target_value-is-fit_reroute-fibre-geometry-workshop"
)


def print_verdict_payload(verdict, value, scheme, convention, l_max,
                          audit_sha256, content_sha256, session="102",
                          gate_id="CF-S102-NU-GRADING-EXTERNAL-EPSLX",
                          schema_version="S84+"):
    payload = {
        "session": session,
        "gate_id": gate_id,
        "verdict": verdict,
        "value": value,
        "scheme": scheme,
        "convention": convention,
        "l_max": str(l_max),
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "schema_version": schema_version,
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>" + json.dumps(payload) + "<<<END_EMIT_VERDICT_PAYLOAD>>>")


print()
print("-" * 70)
print("Section 7 -- dual-SHA closure")
print("-" * 70)
print(f"  audit_sha256   = {audit_sha256}")
print(f"  content_sha256 = {content_sha256}")

# 4-tuple output tag (final non-verdict line)
print(f"(value={value_payload}, scheme=FW, convention=RATIO, L_max={L_MAX})")

print_verdict_payload(
    verdict=verdict,
    value=value_payload,
    scheme="FW",
    convention="RATIO",
    l_max=L_MAX,
    audit_sha256=audit_sha256,
    content_sha256=content_sha256,
)

sys.exit(0)
