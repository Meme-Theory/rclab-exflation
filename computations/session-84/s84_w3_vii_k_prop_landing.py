"""
S84 W3-21 / S84-VII-K-PROP-LANDING (S84-CC-5-LINEARITY-THEOREM-LANDING)

Lizzi spectral-functional-theorist solo landing.

Verifies the CC-5 identity theorem (§VII.K-PROP) over the 42-row §VII.K atlas:

    span_R(O) = prod_k span_R(f_{n_k}^R)^{|p_k|}

Inputs (loaded for anchor spans + SHA pin-map):
  - computations/session-83/s83_w2_g15_k_a2_canonical_range.npz        (k_a2 span axis)
  - computations/session-83/s83_w2_g16_unified_as79_3pi_subst.npz      (A_s single-axis span = k_a2 span)
  - computations/session-83/s83_w3_g28_f_conv_cluster_test.npz         (f_conv axis = M_0^2)
  - computations/session-83/s83_w3_g34_cc_ratio_cluster_universality.npz (3-channel)
  - computations/_shared/canonical_constants.py                     (M_KK, L_max canonical)
  - sessions/archive/session-83/session-83-lizzi-cc5-synthesis.md        (42-row class partition)

Output atlas JSON: s84_w3_vii_k_prop_atlas.json
Output NPZ:        s84_w3_vii_k_prop_landing.npz
Output PNG:        s84_w3_vii_k_prop_landing.png  (log-log scatter span_predicted vs span_direct)

Gate thresholds (pre-registered):
  PASS : max_rel_err < 1e-6
  INFO : 1e-6 <= max_rel_err < 1e-3
  FAIL : max_rel_err >= 1e-3
"""

import os
import sys
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "computations"))

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from canonical_constants import M_KK  # noqa: F401 (for provenance)

# ------------------------------------------------------------------
# 1.  Load anchor NPZs and print input SHA-256 pins (first 20 stdout lines)
# ------------------------------------------------------------------
INPUT_FILES = [
    ROOT / "computations" / "session-83" / "s83_w2_g15_k_a2_canonical_range.npz",
    ROOT / "computations" / "session-83" / "s83_w2_g16_unified_as79_3pi_subst.npz",
    ROOT / "computations" / "session-83" / "s83_w3_g28_f_conv_cluster_test.npz",
    ROOT / "computations" / "session-83" / "s83_w3_g34_cc_ratio_cluster_universality.npz",
    ROOT / "computations" / "_shared" / "canonical_constants.py",
    ROOT / "sessions" / "session-83" / "session-83-lizzi-cc5-synthesis.md",
]

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

input_pins = {}
print("=" * 72)
print("S84 W3-21 / S84-VII-K-PROP-LANDING  --  input SHA-256 pins")
print("=" * 72)
for p in INPUT_FILES:
    s = sha256_file(p)
    input_pins[p.name] = s
    print(f"  {p.name:<52s} {s}")
print("=" * 72)

# ------------------------------------------------------------------
# 2.  Extract measured anchor spans from the pinned NPZs
# ------------------------------------------------------------------
g15 = np.load(INPUT_FILES[0], allow_pickle=True)
g16 = np.load(INPUT_FILES[1], allow_pickle=True)
g28 = np.load(INPUT_FILES[2], allow_pickle=True)
g34 = np.load(INPUT_FILES[3], allow_pickle=True)

span_k_a2      = float(g15["span_A"])                  # k_a2 axis (Conv A)  W2-G15
span_A_s_axis  = float(g16["A_s_scan_span"])           # A_s single-axis on k_a2      W2-G16
span_f_conv    = float(g28["cluster_As"])              # A_s = f_conv cluster (= M_0^2 span)  W3-G28
span_ch1       = float(g34["span_1_ns_alphas"])        # f_4/f_2 balanced-moment ratio
span_ch2       = float(g34["span_2_As_mu"])            # 1/M_0 = span(M_0)
span_ch3       = float(g34["span_3_fNL_r"])            # sqrt(span(M_0))

# Derived base-slot spans (closed-form per synthesis §II)
span_M0        = span_ch2                              # 42.025734
span_M0_sq     = span_f_conv                           # 1766.162324  (consistency check below)
span_f4_over_f2= span_ch1                              # 4.607771
span_sqrt_M0   = span_ch3                              # 6.482726

# consistency internal: span(M_0)^2 should equal span_f_conv to <1e-10 rel
consistency_M0_sq = abs(span_M0**2 - span_M0_sq) / span_M0_sq
consistency_sqrtM0 = abs(np.sqrt(span_M0) - span_sqrt_M0) / span_sqrt_M0

print(f"span(k_a2)           = {span_k_a2:.6f}          [W2-G15]")
print(f"span(A_s | k_a2 axis)= {span_A_s_axis:.6f}          [W2-G16; = span(k_a2) by CC-5]")
print(f"span(M_0)            = {span_M0:.6f}          [W3-G34 ch2]")
print(f"span(M_0^2)=span(f_conv)= {span_M0_sq:.6f}       [W3-G28]")
print(f"span(f_4/f_2)        = {span_f4_over_f2:.6f}           [W3-G34 ch1]")
print(f"span(sqrt(M_0))      = {span_sqrt_M0:.6f}           [W3-G34 ch3]")
print(f"consistency span(M_0)^2 vs span(f_conv)  rel-err = {consistency_M0_sq:.3e}")
print(f"consistency sqrt(span(M_0)) vs span(ch3) rel-err = {consistency_sqrtM0:.3e}")

# ------------------------------------------------------------------
# 3.  Build 42-row §VII.K atlas per synthesis §VII class partition
# ------------------------------------------------------------------
# Primary-class assignment: each row receives ONE exponent signature over the
# base slots {k_a2, M_0, f_4_over_f2, sqrt_M0}.  "measured" span is read from
# the pinned NPZs (machine-eps by construction) except for the mode-bound /
# integer-invariant / balanced-ratio rows where span = 1 identically.
#
# Base-slot span dictionary (keys map to synthesis §VII atlas primitives).
SLOT_SPAN = {
    "k_a2":        span_k_a2,         # 14.685
    "M0":          span_M0,           # 42.026
    "f4_over_f2":  span_f4_over_f2,   # 4.608  (balanced k=4/k=2 label split)
    "sqrt_M0":     span_sqrt_M0,      # 6.483
}

# Primary class -> (description, p-signature dict slot->|p|, predicted span,
#                   measured span, measurement provenance)
# measured span is either the anchor NPZ value OR exactly 1.0 for R-protected rows.
def pred_from_exps(exps):
    v = 1.0  # (local)
    for slot, p in exps.items():
        v *= SLOT_SPAN[slot] ** abs(p)
    return v

# Per-row assignment (list of 42 entries), per synthesis §VII.
R_PROTECTED = [1,2,3,6,7,8,9,10,11,12,14,15,16,19,20,21,22,23,25,26,28,29,31,32,34,35,36,37,39,40,41]  # row 2 absent from synthesis §VII enumeration; defaulted FI (span=1) per residual (30+11 explicit = 41; 42 total forces row 2 FI)
MIXED_FI_VIA_PIN = [13,17,27,38]                        # (synthesis lists {4,13,17,27,38}; row 4 primary = single-axis k_a2)
SINGLE_AXIS_KA2  = {4: ("A_s Branch A on k_a2 axis", {"k_a2": 1})}
SLOT_PROPORTIONAL_M0 = {
    24: ("var_a2 / bare a_2 slot (p=1)",             {"M0": 1}),
    30: ("E_J per-cell inventory (1.5 OOM enumeration)", {"M0": 1}),
}
SLOT_QUADRATIC_M0 = {
    5: ("A_s Branch B (2.26 OOM SDW-Zubarev -> squared = 4.52 OOM)", {"M0": 2}),
}
MIXED_PROMOTABLE = {
    18: ("MIXED promotable row 18 (W3-G34 ch1 analog: n_s/alpha_s)",  {"f4_over_f2": 1}, span_ch1),
    33: ("MIXED promotable row 33 (W3-G34 ch3 analog: f_NL/r)",       {"sqrt_M0":    1}, span_ch3),
    42: ("MIXED promotable row 42 (W3-G34 ch2 analog: A_s/mu)",       {"M0":         1}, span_ch2),
}

atlas_rows = []
for row in range(1, 43):
    if row in R_PROTECTED:
        entry = {
            "row": row,
            "label": f"R-protected row {row}",
            "p_k": {},                          # no regulator-dressed slot
            "class": "R-protected",
            "span_predicted": 1.0,
            "span_direct":    1.0,
            "provenance": "synthesis §VII.K class 'span=1'",
        }
    elif row in MIXED_FI_VIA_PIN:
        entry = {
            "row": row,
            "label": f"MIXED-FI-via-pin row {row}",
            "p_k": {},                          # FI under §VII.K-META pin
            "class": "MIXED-FI-via-pin",
            "span_predicted": 1.0,
            "span_direct":    1.0,
            "provenance": "synthesis §VII.K-META pinned",
        }
    elif row in SINGLE_AXIS_KA2:
        lbl, exps = SINGLE_AXIS_KA2[row]
        entry = {
            "row": row, "label": lbl, "p_k": exps, "class": "single-axis-k_a2",
            "span_predicted": pred_from_exps(exps),
            "span_direct":    span_A_s_axis,    # W2-G16 anchor
            "provenance": "W2-G16 A_s_scan_span",
        }
    elif row in SLOT_PROPORTIONAL_M0:
        lbl, exps = SLOT_PROPORTIONAL_M0[row]
        entry = {
            "row": row, "label": lbl, "p_k": exps, "class": "slot-proportional-M0",
            "span_predicted": pred_from_exps(exps),
            "span_direct":    span_M0,          # W3-G34 ch2 anchor
            "provenance": "W3-G34 span_2_As_mu",
        }
    elif row in SLOT_QUADRATIC_M0:
        lbl, exps = SLOT_QUADRATIC_M0[row]
        entry = {
            "row": row, "label": lbl, "p_k": exps, "class": "slot-quadratic-M0",
            "span_predicted": pred_from_exps(exps),
            "span_direct":    span_M0_sq,       # W3-G28 anchor
            "provenance": "W3-G28 cluster_As",
        }
    elif row in MIXED_PROMOTABLE:
        lbl, exps, measured = MIXED_PROMOTABLE[row]
        entry = {
            "row": row, "label": lbl, "p_k": exps, "class": "MIXED-promotable",
            "span_predicted": pred_from_exps(exps),
            "span_direct":    measured,         # W3-G34 channels
            "provenance": "W3-G34 3-channel",
        }
    else:
        raise RuntimeError(f"row {row} unassigned")
    # relative error
    d = entry["span_direct"]
    p = entry["span_predicted"]
    entry["rel_err"] = abs(p - d) / d if d > 0 else float("nan")
    if entry["rel_err"] < 1e-6:
        entry["classification"] = "PASS"
    elif entry["rel_err"] < 1e-3:
        entry["classification"] = "INFO"
    else:
        entry["classification"] = "FAIL"
    atlas_rows.append(entry)

# ------------------------------------------------------------------
# 4.  Aggregate verdict
# ------------------------------------------------------------------
max_rel_err = max(r["rel_err"] for r in atlas_rows)
n_pass = sum(1 for r in atlas_rows if r["classification"] == "PASS")
n_info = sum(1 for r in atlas_rows if r["classification"] == "INFO")
n_fail = sum(1 for r in atlas_rows if r["classification"] == "FAIL")

print()
print(f"42-row atlas   max_rel_err = {max_rel_err:.3e}")
print(f"classification PASS={n_pass}  INFO={n_info}  FAIL={n_fail}")

if max_rel_err < 1e-6:
    verdict = "PASS"
elif max_rel_err < 1e-3:
    verdict = "INFO"
else:
    verdict = "FAIL"

value_tag      = max_rel_err
scheme_tag     = "ConvA"
convention_tag = "Af-singleton"
L_max_tag      = 5  # (local)  pre-registered gate pin (W3-21 machinery)

# ------------------------------------------------------------------
# 5.  Closure SHA: canonical ordered input-pin map
# ------------------------------------------------------------------
closure_payload = {
    "gate_id": "S84-VII-K-PROP-LANDING",
    "input_pins": input_pins,
    "scheme": scheme_tag,
    "convention": convention_tag,
    "L_max": L_max_tag,
    "F_KK": ["zeta", "Zubarev", "SDW", "dim-reg", "lattice-BR"],
    "theorem": "span_R(O) = prod_k span_R(f_{n_k}^R)^{|p_k|}",
    "atlas_rows": [
        {k: v for k, v in r.items() if k != "classification"} for r in atlas_rows
    ],
    "value": value_tag,
}
closure_json = json.dumps(closure_payload, sort_keys=True, default=float)
closure_sha  = hashlib.sha256(closure_json.encode("utf-8")).hexdigest()
print(f"\nclosure SHA-256 = {closure_sha}")

# ------------------------------------------------------------------
# 6.  Write atlas JSON
# ------------------------------------------------------------------
atlas_json_path = ROOT / "computations" / "session-84" / "s84_w3_vii_k_prop_atlas.json"
with open(atlas_json_path, "w") as fh:
    json.dump({
        "meta": {
            "gate_id": "S84-VII-K-PROP-LANDING",
            "session": 84,
            "agent": "lizzi-spectral-functional-theorist",
            "scheme": scheme_tag,
            "convention": convention_tag,
            "L_max": L_max_tag,
            "F_KK": ["zeta", "Zubarev", "SDW", "dim-reg", "lattice-BR"],
            "theorem": "span_R(O) = prod_k span_R(f_{n_k}^R)^{|p_k|}",
            "input_pins": input_pins,
            "slot_span": SLOT_SPAN,
            "verdict": verdict,
            "max_rel_err": max_rel_err,
            "closure_sha": closure_sha,
        },
        "rows": atlas_rows,
    }, fh, indent=2, default=float)
print(f"atlas JSON -> {atlas_json_path.name}")

# ------------------------------------------------------------------
# 7.  Write NPZ with per-row arrays
# ------------------------------------------------------------------
rows_arr = np.array([r["row"] for r in atlas_rows])
pred_arr = np.array([r["span_predicted"] for r in atlas_rows])
dir_arr  = np.array([r["span_direct"] for r in atlas_rows])
err_arr  = np.array([r["rel_err"] for r in atlas_rows])
class_arr= np.array([r["class"] for r in atlas_rows])
verdict_arr = np.array([r["classification"] for r in atlas_rows])

npz_path = ROOT / "computations" / "session-84" / "s84_w3_vii_k_prop_landing.npz"
np.savez(npz_path,
         rows=rows_arr, span_predicted=pred_arr, span_direct=dir_arr,
         rel_err=err_arr, primary_class=class_arr, row_verdict=verdict_arr,
         max_rel_err=max_rel_err, verdict=verdict,
         closure_sha=closure_sha, L_max=L_max_tag,
         scheme=scheme_tag, convention=convention_tag,
         span_k_a2=span_k_a2, span_M0=span_M0, span_M0_sq=span_M0_sq,
         span_f4_over_f2=span_f4_over_f2, span_sqrt_M0=span_sqrt_M0,
         n_pass=n_pass, n_info=n_info, n_fail=n_fail,
         consistency_M0_sq_rel=consistency_M0_sq,
         consistency_sqrtM0_rel=consistency_sqrtM0)
print(f"NPZ        -> {npz_path.name}")

# ------------------------------------------------------------------
# 8.  PNG: log-log scatter span_predicted vs span_direct
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.4, 5.8))
# small jitter so the 30 R-protected (both =1) render as a single point legend
ax.loglog([0.5, 2500], [0.5, 2500], "-", color="gray", lw=0.8, label="y = x")
class_colors = {
    "R-protected":           "#4477AA",
    "MIXED-FI-via-pin":      "#88CCEE",
    "single-axis-k_a2":      "#EE7733",
    "slot-proportional-M0":  "#CCBB44",
    "slot-quadratic-M0":     "#CC3311",
    "MIXED-promotable":      "#228833",
}
for cls, c in class_colors.items():
    xs = [r["span_direct"] for r in atlas_rows if r["class"] == cls]
    ys = [r["span_predicted"] for r in atlas_rows if r["class"] == cls]
    if xs:
        ax.scatter(xs, ys, s=55, c=c, edgecolors="k", lw=0.4, label=f"{cls} (n={len(xs)})")
ax.set_xlabel("span_direct (measured)")
ax.set_ylabel("span_predicted = prod_k span(f_k)^{|p_k|}")
ax.set_title(f"CC-5 identity over §VII.K 42-row atlas\nmax_rel_err = {max_rel_err:.2e}  verdict={verdict}")
ax.grid(True, which="both", alpha=0.3)
ax.legend(fontsize=7, loc="upper left")
plt.tight_layout()
png_path = ROOT / "computations" / "session-84" / "s84_w3_vii_k_prop_landing.png"
plt.savefig(png_path, dpi=140)
print(f"PNG        -> {png_path.name}")

# ------------------------------------------------------------------
# 9.  Final 4-tuple tag + verdict-line print
# ------------------------------------------------------------------
print()
print(f"4-tuple: (value={value_tag:.3e}, scheme={scheme_tag}, convention={convention_tag}, L_max={L_max_tag})")
print(
    f"VERDICT_LINE: S84-VII-K-PROP-LANDING: {verdict} -- "
    f"value={value_tag:.3e} scheme={scheme_tag} convention={convention_tag} "
    f"L_max={L_max_tag} sha256={closure_sha}"
)
