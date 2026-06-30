"""
S84 W3-31: S84-CC5-L-MAX-ASYMPTOTIC
Fit span_1/span_2/span_3 (CC-5 cluster) at L_max in {3,5,7,9} to power-law vs
exponential forms; classify each as EXP-DOM / POW-DOM / AMBIGUOUS.

Consumes S83 G34 precomputed L_max scan (span_scan_*_* arrays).
"""
import os, sys, json, hashlib, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GATE_ID = "S84-CC5-L-MAX-ASYMPTOTIC"
SCRIPT = os.path.abspath(__file__)

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(8192), b""):
            h.update(b)
    return h.hexdigest()

# --- input pins ---
src_npz = "computations/session-83/s83_w3_g34_cc_ratio_cluster_universality.npz"
pins = {
    "gate_id": GATE_ID,
    "script_sha256": sha256_file(SCRIPT),
    "s83_g34_npz_sha256": sha256_file(src_npz),
    "canonical_constants_sha256": sha256_file("computations/_shared/canonical_constants.py"),
}
print("=== INPUT PINS ===")
for k, v in pins.items():
    print(f"  {k}: {v}")

d = np.load(src_npz, allow_pickle=True)
L = np.array(d["L_max_scan"], dtype=float)  # (local)
span_1 = np.array(d["span_scan_ns_alphas"], dtype=float)  # (local)
span_2 = np.array(d["span_scan_As_mu"], dtype=float)      # (local)
span_3 = np.array(d["span_scan_fNL_r"], dtype=float)      # (local)
print(f"L_max scan: {L.tolist()}")
print(f"span_1 (ns/alphas): {span_1.tolist()}")
print(f"span_2 (As/mu):     {span_2.tolist()}")
print(f"span_3 (fNL/r):     {span_3.tolist()}")

def r2(y, yhat):  # (local)
    ss_res = np.sum((y - yhat) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")

def fit_pow_exp(L_arr, span):  # (local)
    ly = np.log(span)
    # power-law: ly = a_pow + b_pow * ln L
    xp = np.log(L_arr)
    b_pow, a_pow = np.polyfit(xp, ly, 1)
    ly_pow = a_pow + b_pow * xp
    R2_pow = r2(ly, ly_pow)
    # exponential: ly = a_exp + c_exp * L^2
    xe = L_arr ** 2
    c_exp, a_exp = np.polyfit(xe, ly, 1)
    ly_exp = a_exp + c_exp * xe
    R2_exp = r2(ly, ly_exp)
    return dict(b_pow=float(b_pow), a_pow=float(a_pow), R2_pow=float(R2_pow),
                c_exp=float(c_exp), a_exp=float(a_exp), R2_exp=float(R2_exp))

def classify(fit):  # (local)
    if fit["R2_exp"] > fit["R2_pow"] + 0.01:
        return "EXP-DOM"
    if fit["R2_pow"] > fit["R2_exp"] + 0.01:
        return "POW-DOM"
    return "AMBIGUOUS"

fits = {}
for name, y in [("span_1_ns_alphas", span_1), ("span_2_As_mu", span_2), ("span_3_fNL_r", span_3)]:
    f = fit_pow_exp(L, y)
    f["class"] = classify(f)
    fits[name] = f
    print(f"  {name}: R2_pow={f['R2_pow']:.6f} (b={f['b_pow']:.4f})  "
          f"R2_exp={f['R2_exp']:.6f} (c={f['c_exp']:.4f})  => {f['class']}")

# --- predicted classes from §V substitution chain ---
# span_2 = As/mu ~ direct f_conv span, Zubarev appears in DENOMINATOR via
#   f_conv^Zubarev ~ exp(-c L^2)^{-1} contribution => predicted EXP-DOM.
# span_1 = ns/alphas (ratio-of-ratios; partial cancellations) => predicted POW-DOM.
# span_3 = fNL/r ~ sqrt(M_0 cluster) => predicted POW-DOM (milder).
predicted = {
    "span_1_ns_alphas": "POW-DOM",
    "span_2_As_mu":     "EXP-DOM",
    "span_3_fNL_r":     "POW-DOM",
}

matches = 0  # (local)
for name, pred in predicted.items():
    obs = fits[name]["class"]  # (local)
    ok = (obs == pred)  # (local)
    matches += int(ok)
    print(f"  prediction[{name}]: {pred}  observed: {obs}  match={ok}")

# PASS if >=2 of 3 predicted classes match (plan §W3-31).
if matches >= 2:
    verdict = "PASS"
elif matches == 1:
    verdict = "INFO"
else:
    verdict = "FAIL"
print(f"matches = {matches}/3 -> verdict = {verdict}")

# --- extra diagnostic: growth-rate consistency ---
# If EXP-DOM, extract c_exp and compare to Weyl-bound prediction c ~ 1/Lambda_sq_asymptotic.
# We report c_exp for span_2 and b_pow for span_1, span_3 as diagnostic, not gate-binding.
diag = {
    "c_exp_span_2": fits["span_2_As_mu"]["c_exp"],
    "b_pow_span_1": fits["span_1_ns_alphas"]["b_pow"],
    "b_pow_span_3": fits["span_3_fNL_r"]["b_pow"],
}
print(f"diagnostic: c_exp(span_2)={diag['c_exp_span_2']:.4f}  "
      f"b_pow(span_1)={diag['b_pow_span_1']:.4f}  b_pow(span_3)={diag['b_pow_span_3']:.4f}")

# --- save artifacts ---
out_npz = "computations/session-84/s84_w3_cc5_l_max_asymptotic.npz"
np.savez(out_npz,
         L_max_scan=L, span_1=span_1, span_2=span_2, span_3=span_3,
         fit_span_1=np.array(json.dumps(fits["span_1_ns_alphas"])),
         fit_span_2=np.array(json.dumps(fits["span_2_As_mu"])),
         fit_span_3=np.array(json.dumps(fits["span_3_fNL_r"])),
         predicted_classes=np.array(json.dumps(predicted)),
         matches=matches, verdict=verdict, pins=np.array(json.dumps(pins)))
print(f"wrote {out_npz}")

# --- plot: 4-panel ---
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
panels = [
    ("span_1_ns_alphas", span_1, axes[0, 0], "span_1: n_s/alpha_s"),
    ("span_2_As_mu",     span_2, axes[0, 1], "span_2: A_s/mu"),
    ("span_3_fNL_r",     span_3, axes[1, 0], "span_3: f_NL/r"),
]
for name, y, ax, title in panels:
    f = fits[name]
    ax.plot(L, y, "o", ms=8, label="data")
    Lfine = np.linspace(L.min(), L.max(), 100)  # (local)
    y_pow = np.exp(f["a_pow"] + f["b_pow"] * np.log(Lfine))  # (local)
    y_exp = np.exp(f["a_exp"] + f["c_exp"] * Lfine ** 2)      # (local)
    ax.plot(Lfine, y_pow, "--", label=f"pow-law (R2={f['R2_pow']:.4f}, b={f['b_pow']:.2f})")
    ax.plot(Lfine, y_exp, ":",  label=f"exp-law (R2={f['R2_exp']:.4f}, c={f['c_exp']:.2f})")
    ax.set_yscale("log")
    ax.set_xlabel("L_max")
    ax.set_ylabel(name)
    ax.set_title(f"{title}  [{f['class']}]")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
ax4 = axes[1, 1]
ax4.axis("off")
summary = [
    f"Gate: {GATE_ID}",
    f"Verdict: {verdict}  (matches {matches}/3)",
    "",
    "Predicted  | Observed",
    f"span_1 POW | {fits['span_1_ns_alphas']['class']}",
    f"span_2 EXP | {fits['span_2_As_mu']['class']}",
    f"span_3 POW | {fits['span_3_fNL_r']['class']}",
    "",
    f"c_exp(span_2) = {fits['span_2_As_mu']['c_exp']:.4f}",
    f"b_pow(span_1) = {fits['span_1_ns_alphas']['b_pow']:.4f}",
    f"b_pow(span_3) = {fits['span_3_fNL_r']['b_pow']:.4f}",
]
ax4.text(0.05, 0.95, "\n".join(summary), va="top", family="monospace", fontsize=10)
fig.suptitle("S84 W3-31: CC-5 L_max-asymptotic scaling")
fig.tight_layout()
out_png = "computations/session-84/s84_w3_cc5_l_max_asymptotic.png"
fig.savefig(out_png, dpi=110)
print(f"wrote {out_png}")

# --- closure SHA ---
closure_payload = json.dumps({
    "pins": pins, "L": L.tolist(),
    "span_1": span_1.tolist(), "span_2": span_2.tolist(), "span_3": span_3.tolist(),
    "fits": fits, "predicted": predicted, "matches": matches, "verdict": verdict,
}, sort_keys=True).encode()
closure = hashlib.sha256(closure_payload).hexdigest()
print(f"closure_sha256 = {closure}")

# --- canonical 4-tuple ---
print(f"4-tuple: (value=matches/3={matches}/3, scheme=F_KK=5-regulator, "
      f"convention=ConvA, L_max=scan{{3,5,7,9}})")
print(f"{GATE_ID}: {verdict} -- value=matches/3={matches}/3 scheme=F_KK=5-reg "
      f"convention=ConvA L_max=scan{{3,5,7,9}} sha256={closure}")
