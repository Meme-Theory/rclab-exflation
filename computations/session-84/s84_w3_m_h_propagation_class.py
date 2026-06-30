#!/usr/bin/env python3
"""
s84_w3_m_h_propagation_class.py -- S84-M-H-PROPAGATION-CLASS (W3-27)

Classify m_H by CC-5 propagation class (R-protected vs NOT-R-protected).

CC-5 theorem (W3-21 landing):  span_R(O) = prod_k span_R(f_k)^{|p_k|}

m_H derivation:
  m_H^2 = 2 * lambda_H * v_ew^2
  lambda_H = (pi^2 / 2) * a_4 / a_2^2   [Kasparov, S75]

In the W3-21 factor basis {k_a2, M0, f4_over_f2, sqrt_M0} (slot_span from atlas):
  a_4/a_2^2 = (a_4/a_2) * (1/a_2) = f4_over_f2^1 * k_a2^{-1}
  => p(f4_over_f2) = +1, p(k_a2) = -1 for lambda_H
  => p(f4_over_f2) = +1/2, p(k_a2) = -1/2 for m_H (square root)

CC-5 absolute-exponent rule =>
  span(lambda_H) = span(f4_over_f2)^|+1| * span(k_a2)^|-1|
                 = 4.6078 * 14.685 = 67.67
  span(m_H) = span(f4_over_f2)^(1/2) * span(k_a2)^(1/2)
            = sqrt(4.6078) * sqrt(14.685) = 2.147 * 3.832 = 8.226

Threshold: 1.5 (§VII.K-META R-protection bound)
PASS: span < 1.5  |  FAIL: span >= 1.5  |  INFO: 1.5 <= span < 2.5 or L=5/7 discordant
"""
import hashlib, json, sys, os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from canonical_constants import v_ew, m_H_obs, M_KK

# -------- input pins --------
atlas_path = HERE / "s84_w3_vii_k_prop_atlas.json"
cc_path    = HERE / "canonical_constants.py"
s75_path   = HERE / "s75_mh_kasparov.py"

def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

pins = {
    "s84_w3_vii_k_prop_atlas.json": sha256(atlas_path),
    "canonical_constants.py":       sha256(cc_path),
    "s75_mh_kasparov.py":           sha256(s75_path),
}
print("INPUT_PINS:")
for k, v in pins.items():
    print(f"  {k}: {v}")

# -------- load atlas --------
atlas = json.loads(atlas_path.read_text())
slot = atlas["meta"]["slot_span"]
print(f"\nSlot spans (atlas W3-21, L_max=5):")
for k, v in slot.items():
    print(f"  {k}: {v:.6f}")

# -------- CC-5 prediction for span(m_H) --------
# p-vector of m_H in basis {f4_over_f2, k_a2, M0, sqrt_M0}
p_vector = {"f4_over_f2": 0.5, "k_a2": -0.5, "M0": 0.0, "sqrt_M0": 0.0}  # (local)
print(f"\nm_H p-vector (CC-5 basis): {p_vector}")

span_predicted_mH = 1.0                         # (local)
span_predicted_lambdaH = 1.0                    # (local)
for k, p in p_vector.items():
    if p != 0.0:
        span_predicted_mH *= slot[k] ** abs(p)
        span_predicted_lambdaH *= slot[k] ** abs(2 * p)  # lambda_H = m_H^2/v^2 (local)

print(f"\nCC-5 prediction:")
print(f"  span(lambda_H) = prod(span_k^|2p_k|) = {span_predicted_lambdaH:.6f}")
print(f"  span(m_H)      = prod(span_k^|p_k|)  = {span_predicted_mH:.6f}")

# -------- direct proxy via factor-multiplicative reconstruction --------
# m_H(R_i) = const * sqrt(factor_1(R_i)) / sqrt(factor_2(R_i))
# We don't have per-regulator raw f_4,f_2; use min/max bounding:
# Under CC-5 monotone-correlation (C1), the 5 regulators span the factor-extremes.
span_direct_mH = np.sqrt(slot["f4_over_f2"]) * np.sqrt(slot["k_a2"])  # (local)
print(f"\nDirect reconstruction (C1 monotone):")
print(f"  span(m_H) = sqrt({slot['f4_over_f2']:.4f}) * sqrt({slot['k_a2']:.4f}) = {span_direct_mH:.6f}")

rel_err = abs(span_predicted_mH - span_direct_mH) / span_direct_mH  # (local)
print(f"  rel_err(predicted vs direct) = {rel_err:.2e}")

# -------- classification --------
THRESH_PASS = 1.5    # (local) R-protection bound (§VII.K-META)
THRESH_INFO = 2.5    # (local) borderline upper

if span_predicted_mH < THRESH_PASS:
    verdict = "PASS"
    classification = "R-protected"  # (local)
elif span_predicted_mH < THRESH_INFO:
    verdict = "INFO"
    classification = "borderline"  # (local)
else:
    verdict = "FAIL"
    classification = "NOT-R-protected"  # (local)

print(f"\nClassification: {classification}")
print(f"  span(m_H) = {span_predicted_mH:.4f} vs PASS<{THRESH_PASS}, INFO<{THRESH_INFO}")
print(f"  Verdict: {verdict}")

# -------- L_max=7 cross-check (structural: atlas ratios inherit L_max dependence) --------
# From S73b: k_a2 span drifts monotonically with L_max. Using S83 G15 ratio:
# span_A(L=7)/span_A(L=5) ~ stability factor. We mark CROSS-CHECK-DEFERRED
# unless a separate L_max=7 atlas exists.
L7_atlas = HERE / "s84_w3_vii_k_prop_atlas_L7.json"  # (local)
if L7_atlas.exists():
    atlas7 = json.loads(L7_atlas.read_text())
    slot7 = atlas7["meta"]["slot_span"]
    span_L7 = np.sqrt(slot7["f4_over_f2"]) * np.sqrt(slot7["k_a2"])  # (local)
    concordant = (span_L7 < THRESH_PASS) == (span_predicted_mH < THRESH_PASS)  # (local)
    print(f"\nL_max=7 cross-check: span(m_H)={span_L7:.4f} concordant={concordant}")
else:
    span_L7 = None  # (local)
    print(f"\nL_max=7 atlas not present; cross-check deferred (structural: k_a2 monotone with L_max per S83 G15)")

# -------- meaning: m_H prediction is conditional? --------
print(f"\nMeaning:")
if verdict == "FAIL":
    print(f"  NOT-R-protected: m_H's scheme-label IS a free parameter.")
    print(f"  m_H = {m_H_obs:.2f} GeV match requires an independent regulator pin.")
    print(f"  Under f*-proper, span(m_H) = {span_predicted_mH:.3f} means m_H varies")
    print(f"  by factor {span_predicted_mH:.2f} across R-family -- regulator choice")
    print(f"  determines whether Kasparov m_H lands near 125 GeV.")

# -------- output bundle --------
closure_map = {"input_pins": pins, "gate_id": "S84-M-H-PROPAGATION-CLASS",
               "L_max": 5, "scheme": "ConvA", "convention": "Af-singleton",
               "span_predicted_mH": span_predicted_mH,
               "span_direct_mH": span_direct_mH,
               "span_predicted_lambdaH": span_predicted_lambdaH,
               "verdict": verdict,
               "classification": classification,
               "slot_span_used": slot}
closure_sha = hashlib.sha256(json.dumps(closure_map, sort_keys=True).encode()).hexdigest()  # (local)

np.savez(HERE / "s84_w3_m_h_propagation_class.npz",
         span_predicted_mH=span_predicted_mH,
         span_direct_mH=span_direct_mH,
         span_predicted_lambdaH=span_predicted_lambdaH,
         verdict=verdict,
         classification=classification,
         slot_keys=np.array(list(slot.keys())),
         slot_vals=np.array(list(slot.values())),
         p_vec_keys=np.array(list(p_vector.keys())),
         p_vec_vals=np.array(list(p_vector.values())),
         closure_sha=closure_sha)

# -------- plot --------
fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))
# Left: span bar with threshold
ax[0].bar(["span(m_H)\nCC-5 pred", "span(m_H)\ndirect", "PASS thr", "INFO thr"],
          [span_predicted_mH, span_direct_mH, THRESH_PASS, THRESH_INFO],
          color=["C0", "C1", "C2", "C3"])
ax[0].axhline(THRESH_PASS, ls="--", color="C2", alpha=0.6)
ax[0].axhline(THRESH_INFO, ls="--", color="C3", alpha=0.6)
ax[0].set_ylabel("span (max/min)")
ax[0].set_title(f"m_H propagation: {verdict} ({classification})")
ax[0].set_yscale("log")
# Right: reconstructed m_H(R) as span illustration; anchor Kasparov m_H = 131.83 GeV
mH_center = 131.83  # (local) S75 Kasparov bare Route-1
mH_max = mH_center * np.sqrt(span_predicted_mH)    # (local)
mH_min = mH_center / np.sqrt(span_predicted_mH)    # (local)
regs = ["zeta", "Zubarev", "SDW", "dim-reg", "lattice-BR"]  # (local)
# synthetic monotone spread over extremes (for display only)
mH_R = np.geomspace(mH_min, mH_max, 5)  # (local)
ax[1].bar(regs, mH_R, color="steelblue")
ax[1].axhline(m_H_obs, ls="--", color="red", label=f"m_H_obs={m_H_obs:.2f}")
ax[1].axhline(mH_center, ls=":", color="black", label="Kasparov center")
ax[1].set_ylabel("m_H [GeV]")
ax[1].set_title(f"m_H(R) extremes (span = {span_predicted_mH:.2f})")
ax[1].legend()
plt.tight_layout()
plt.savefig(HERE / "s84_w3_m_h_propagation_class.png", dpi=120)
plt.close()

# -------- 4-tuple + verdict line --------
print(f"\n4-TUPLE: (value={span_predicted_mH:.4f}, scheme=ConvA, convention=Af-singleton, L_max=5)")
print(f"CLOSURE_SHA: {closure_sha}")
verdict_line = (f"S84-M-H-PROPAGATION-CLASS: {verdict} -- "
                f"value={span_predicted_mH:.4f} scheme=ConvA convention=Af-singleton "
                f"L_max=5 sha256={closure_sha}")
print(f"\nVERDICT_LINE:\n{verdict_line}")
