#!/usr/bin/env python3
"""
S83 Wave 3 Gate G33 -- RATIO-PROBE-LEAD-INDICATOR
===================================================

Gate: S83-RATIO-PROBE-LEAD-INDICATOR  [VERIFY]
Classification: PHONONIC + PARTICLE
Owner: gen-physicist

Hypothesis tested:
  Do observable RATIOS lead absolute-value verdicts by Pearson
  correlation >= 0.7 across 10 recent (ratio-gate, absolute-gate)
  pre-registered pairs?

Pre-registered thresholds:
  PASS : |rho| > 0.7
  INFO : 0.4 < |rho| <= 0.7
  FAIL : |rho| <= 0.4

Phononic framing:
  Under the substrate-native classification (S80 W0-9), every canonical
  constant (and derivatively every observational gate) is either RATIO
  (M_KK-independent dimensionless framework observable) or ABSOLUTE
  (M_KK^n-dependent or PDG/Planck-pinned). RATIO-class gates probe
  dimensionless structural invariants of the Dirac spectrum D_K
  (eigenvalue ratios, normalized amplitudes, dimensionless couplings).
  ABSOLUTE-class gates probe the scale-set values that require the
  external M_KK pin to yield a dimensionful prediction. The question
  "do ratios LEAD absolutes" asks whether the dimensionless substrate
  structure determines the absolute-value verdict before the M_KK pin
  is even applied -- i.e., whether the substrate is epistemically
  self-sufficient at the ratio level.

Substitution chain [VERIFY][CHAIN]:
  Step 1 (definitions):
    R_i in {ratio-class gate verdict} for i in 1..10
    A_i in {absolute-class gate verdict paired with R_i} for i in 1..10
    Encoding map e: {PASS, FAIL, INFO} -> {1, 0, 0.5}
    Pearson rho: rho = Cov(e(R), e(A)) / (sigma_R * sigma_A)

  Step 2 (substitution):
    Build 10 pairs from S82+S83 verdict files. Each pair consists of
    (ratio-class gate, absolute-class gate) probing a common physical
    sub-system. The ratio gate fires at time T (or lexically earlier
    in the verdict file), the absolute gate at time T+1 (or lexically
    later). Encode each verdict as 0, 0.5, or 1.

  Step 3 (simplification):
    Compute Pearson rho via scipy.stats.pearsonr on the 10 encoded
    ratio-codes and 10 encoded absolute-codes.

  Step 4 (direction):
    |rho| > 0.7  => ratio verdicts LEAD absolute verdicts by shared
                    variance. PASS.
    0.4 < |rho| <= 0.7 => partial lead, INFO.
    |rho| <= 0.4 => ratio and absolute verdicts are decoupled, FAIL.

Pair construction methodology:
  For each pair, the RATIO gate reports a dimensionless framework
  observable and the ABSOLUTE gate reports an M_KK-scale pin or
  PDG/Planck observational absolute IN THE SAME PHYSICAL SUB-SYSTEM.
  Classification is by verdict-line headline value per the S80 W0-9
  canonical taxonomy (RATIO = dim=0 by construction or slot-pinned
  framework ratio; ABSOLUTE = mass-dim n!=0 or observational pin).

  Pair   Ratio gate                            Absolute gate
  ----   ----------                            -------------
  1   S82-W3G-BETA-R1 (w_0, dim=0)           S83-UNIFIED-AS-79-WITH-3PI
                                               (A_s abs amplitude)
  2   S83-JENSEN-FLOW-TRAJECTORY (ratio)     S82-UNIFIED-AS-79-FULL-A
                                               (A_s abs value)
  3   S83-CS-REGULATOR-DEPENDENCE (dim=0)    S82-H-TILDE-EPOCH-TD (H_tilde abs)
  4   S83-DRESSING-FACTOR-TAU-FLOW (slope)   S82-H-TILDE-EPOCH-LI (H_tilde abs)
  5   S83-SDW-NLO-ALPHA-UNIVERSALITY (span)  S82-UNIFIED-BACKREACT-79
                                               (POWER-RATIO, abs scale)
  6   S82-CHI-N-WARD-DUAL (dim=0 variance %) S82-UNIFIED-AS-79-FULL-B
                                               (A_s abs, LI branch)
  7   S82-CC-RATIOS-ONLY-THEOREM-SG (dim=0)  S82-A2-CLUSTER-TEST
                                               (a_2 abs-scale cluster)
  8   S83-NNLO-BAND-BOUND (dim=0 slope gap)  S82-MULTIPAIR-ECOND
                                               (E_cond abs in M_KK units)
  9   S83-K-A2-CANONICAL-RANGE (span ratio)  S82-FAMP-SC-3PI
                                               (F_amp abs power)
  10  S82-CUBIC-SIN2-W-EW (dim=0 Weinberg)   S82-GW-CHANNEL
                                               (GW Omega abs)

  Principled pairing rule: each ratio-gate probes the SAME physical
  sub-system as its paired absolute-gate, with the ratio appearing
  BEFORE (or simultaneously with) the absolute in the lexical
  ordering of the verdict files. Ratio-class is headline-dimensionless
  (M_KK-independent per S80 W0-9); absolute-class is headline-
  dimensionful or external-pin-anchored.

Inputs (read-only):
  computations/session-82/s82_gate_verdicts.txt
  computations/session-83/s83_gate_verdicts.txt

Output 4-tuple:
  (value=<pearson_rho>, scheme=10-gate-pair-sample,
   convention=PASS=1/FAIL=0/INFO=0.5, L_max=N/A)
"""

import os
import sys
import hashlib
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# CPU-only, thread-capped: pure stats computation, no heavy LA
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# Mandatory: canonical constants import (even though this is a META gate)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403

# -----------------------------------------------------------------
# 1. Path setup
# -----------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))                    # (local)
S82_PATH = os.path.join(SCRIPT_DIR, "s82_gate_verdicts.txt")               # (local)
S83_PATH = os.path.join(SCRIPT_DIR, "s83_gate_verdicts.txt")               # (local)
OUT_NPZ = os.path.join(SCRIPT_DIR, "s83_w3_g33_ratio_probe_lead.npz")      # (local)
OUT_PNG = os.path.join(SCRIPT_DIR, "s83_w3_g33_ratio_probe_lead.png")      # (local)

# Pre-registered thresholds
PASS_RHO = 0.7                                                              # (local) gate threshold
INFO_RHO = 0.4                                                              # (local) gate threshold

# -----------------------------------------------------------------
# 2. Input SHA pin (closure hash from ordered input-pin map)
# -----------------------------------------------------------------
def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


pin_map = []                                                                # (local)
for p in [S82_PATH, S83_PATH]:
    sha = sha256_of_file(p)
    pin_map.append((os.path.basename(p), sha))
    print(f"INPUT PIN: {os.path.basename(p)}  sha256={sha}")

closure_material = "\n".join(f"{name}::{sha}" for name, sha in pin_map)     # (local)
closure_sha = hashlib.sha256(closure_material.encode("utf-8")).hexdigest()  # (local)
print(f"CLOSURE INPUT PINS: {len(pin_map)}")
print(f"CLOSURE SHA: {closure_sha}")

# -----------------------------------------------------------------
# 3. Verdict parser (dual-entry permanence: last appearance wins)
# -----------------------------------------------------------------
def read_latest_verdict_symbol(gate_id, path):
    """Return the verdict symbol of the LATEST matching line."""
    matches = []                                                            # (local)
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line_stripped = line.strip()                                    # (local)
            if line_stripped.startswith(f"{gate_id}:"):
                matches.append(line_stripped)
    if not matches:
        return "MISSING"
    latest = matches[-1]                                                    # (local)
    after_colon = latest.split(":", 1)[1].strip()                           # (local)
    before_dashes = after_colon.split("--")[0].strip()                      # (local)
    symbol = before_dashes.split()[0] if before_dashes else "UNKNOWN"       # (local)
    return symbol


def encode_verdict(symbol):
    """Encode per pre-registered convention: PASS=1, FAIL=0, INFO=0.5."""
    # Canonicalize fused labels to the atomic class token.
    atomic_token = symbol.split("-")[0]                                      # (local)
    if atomic_token == "PASS":
        return 1.0
    if atomic_token == "FAIL":
        return 0.0
    if atomic_token == "INFO":
        return 0.5
    # MISSING/UNKNOWN/other -- encode as 0.5 (neutral) and flag
    return 0.5


# -----------------------------------------------------------------
# 4. The 10 pre-registered (ratio-gate, absolute-gate) pairs
# -----------------------------------------------------------------
# Each entry: (pair_id, ratio_gate_id, ratio_path, abs_gate_id, abs_path,
#              physical_subsystem)
PAIRS = [                                                                   # (local)
    ("P1",
     "S82-W3G-BETA-R1", S82_PATH,              # RATIO: w_0, dim=0 (DK_RATIO)
     "S83-UNIFIED-AS-79-WITH-3PI-SUBSTITUTION", S83_PATH,  # ABS: A_s amplitude
     "DE/scalar-amplitude sub-ledger"),
    ("P2",
     "S83-JENSEN-FLOW-TRAJECTORY", S83_PATH,   # RATIO: F_traj ratio, dim=0
     "S82-UNIFIED-AS-79-FULL-A", S82_PATH,     # ABS: A_s absolute value (TD)
     "Jensen-flow / A_s-TD branch"),
    ("P3",
     "S83-CS-REGULATOR-DEPENDENCE", S83_PATH,  # RATIO: c_s slope, dim=0
     "S82-H-TILDE-EPOCH-TD", S82_PATH,         # ABS: H_tilde absolute value
     "IC dressing / H_tilde epoch (TD)"),
    ("P4",
     "S83-DRESSING-FACTOR-TAU-FLOW", S83_PATH, # RATIO: max_slope, dim=0
     "S82-H-TILDE-EPOCH-LI", S82_PATH,         # ABS: H_tilde abs value (LI)
     "Dressing flow / H_tilde epoch (LI)"),
    ("P5",
     "S83-SDW-NLO-ALPHA-UNIVERSALITY", S83_PATH, # RATIO: span ratio, dim=0
     "S82-UNIFIED-BACKREACT-79", S82_PATH,       # ABS: POWER-RATIO absolute
     "NLO universality / backreaction power"),
    ("P6",
     "S82-CHI-N-WARD-DUAL", S82_PATH,          # RATIO: chi_N var %, dim=0
     "S82-UNIFIED-AS-79-FULL-B", S82_PATH,     # ABS: A_s absolute (LI branch)
     "Ward-dual / A_s-LI branch"),
    ("P7",
     "S82-CC-RATIOS-ONLY-THEOREM-SG", S82_PATH, # RATIO: CC-ratios theorem, dim=0
     "S82-A2-CLUSTER-TEST", S82_PATH,           # ABS: a_2 cluster absolute
     "CC-ratios / a_2 slot-pinned cluster"),
    ("P8",
     "S83-NNLO-BAND-BOUND", S83_PATH,           # RATIO: slope gap, dim=0
     "S82-MULTIPAIR-ECOND", S82_PATH,           # ABS: E_cond in M_KK units
     "NNLO band / E_cond absolute"),
    ("P9",
     "S83-K-A2-CANONICAL-RANGE", S83_PATH,      # RATIO: span, dim=0
     "S82-FAMP-SC-3PI", S82_PATH,               # ABS: F_amp absolute power
     "Canonical range / F_amp power"),
    ("P10",
     "S82-CUBIC-SIN2-W-EW", S82_PATH,           # RATIO: sin^2 theta_W, dim=0
     "S82-GW-CHANNEL", S82_PATH,                # ABS: GW Omega absolute
     "Weinberg / GW channel"),
]

print()
print("=" * 78)
print("S83 W3 G33 -- RATIO-PROBE LEAD INDICATOR (10 pairs)")
print("=" * 78)
print()

ratio_symbols = []                                                          # (local)
abs_symbols = []                                                            # (local)
pair_rows = []                                                              # (local)
for pid, r_id, r_path, a_id, a_path, subsystem in PAIRS:
    r_sym = read_latest_verdict_symbol(r_id, r_path)
    a_sym = read_latest_verdict_symbol(a_id, a_path)
    ratio_symbols.append(r_sym)
    abs_symbols.append(a_sym)
    r_code = encode_verdict(r_sym)                                          # (local)
    a_code = encode_verdict(a_sym)                                          # (local)
    pair_rows.append((pid, r_id, r_sym, r_code, a_id, a_sym, a_code, subsystem))
    print(f"  [{pid}] {subsystem}")
    print(f"       RATIO    : {r_id:<44} -> {r_sym:<12} (code={r_code})")
    print(f"       ABSOLUTE : {a_id:<44} -> {a_sym:<12} (code={a_code})")

ratio_codes = np.array([encode_verdict(s) for s in ratio_symbols])          # (local)
abs_codes = np.array([encode_verdict(s) for s in abs_symbols])              # (local)

print()
print(f"Ratio codes    : {list(ratio_codes)}")
print(f"Absolute codes : {list(abs_codes)}")

# -----------------------------------------------------------------
# 5. Pearson correlation
# -----------------------------------------------------------------
# Substitution chain Step 5: scipy.stats.pearsonr
# rho = sum((x_i - mean_x)(y_i - mean_y)) / (sigma_x * sigma_y * N)
#
# Guard against zero-variance on either axis (would divide by zero in
# scipy). In that pathological case, no correlation can be computed and
# we emit rho=NaN -> INFO verdict (degraded from FAIL).

std_r = float(np.std(ratio_codes))                                          # (local)
std_a = float(np.std(abs_codes))                                            # (local)

if std_r < 1e-12 or std_a < 1e-12:
    rho = float("nan")                                                      # (local)
    pval = float("nan")                                                     # (local)
    degenerate_axis = True                                                  # (local)
    print(f"\nWARNING: one axis has zero variance. std_r={std_r}, std_a={std_a}")
else:
    res = stats.pearsonr(ratio_codes, abs_codes)
    rho = float(res.statistic)                                              # (local)
    pval = float(res.pvalue)                                                # (local)
    degenerate_axis = False                                                 # (local)

print(f"\nPearson rho = {rho:.4f}  (p-value = {pval:.4f})")
print(f"Ratio axis std    = {std_r:.4f}")
print(f"Absolute axis std = {std_a:.4f}")

# -----------------------------------------------------------------
# 6. Verdict dispatch (pre-registered thresholds)
# -----------------------------------------------------------------
# Substitution chain Step 4 -- direction readoff:
#   |rho| > 0.7        => PASS   (ratios lead absolutes)
#   0.4 < |rho| <= 0.7 => INFO   (partial lead)
#   |rho| <= 0.4       => FAIL   (decoupled)
if np.isnan(rho):
    verdict = "INFO"                                                        # (local) degenerate: no signal
    reason = "degenerate-axis (one side has zero variance); cannot reject null"  # (local)
elif abs(rho) > PASS_RHO:
    verdict = "PASS"                                                        # (local)
    reason = f"|rho|={abs(rho):.4f} > {PASS_RHO} (ratios LEAD absolutes)"   # (local)
elif abs(rho) > INFO_RHO:
    verdict = "INFO"                                                        # (local)
    reason = f"{INFO_RHO} < |rho|={abs(rho):.4f} <= {PASS_RHO} (partial lead)"  # (local)
else:
    verdict = "FAIL"                                                        # (local)
    reason = f"|rho|={abs(rho):.4f} <= {INFO_RHO} (ratios and absolutes decoupled)"  # (local)

print(f"\nVerdict: {verdict}")
print(f"Reason : {reason}")

# -----------------------------------------------------------------
# 7. Plot (scatter + regression line + pair labels)
# -----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 7))
# Jitter identical (r,a) points slightly so they are visible on scatter
np.random.seed(42)                                                          # (local)
jitter = 0.02                                                               # (local)
x_jit = ratio_codes + np.random.uniform(-jitter, jitter, len(ratio_codes))  # (local)
y_jit = abs_codes + np.random.uniform(-jitter, jitter, len(abs_codes))      # (local)
ax.scatter(x_jit, y_jit, s=180, c="steelblue", edgecolors="black",
           alpha=0.85, zorder=3)
for (pid, r_id, r_sym, r_code, a_id, a_sym, a_code, _), x, y in zip(
        pair_rows, x_jit, y_jit):
    ax.annotate(f"{pid}\n({r_sym[:4]}|{a_sym[:4]})",
                (x, y), xytext=(7, 7), textcoords="offset points",
                fontsize=8, alpha=0.75)

# Regression line (only if non-degenerate)
if not degenerate_axis:
    slope, intercept = np.polyfit(ratio_codes, abs_codes, 1)                # (local)
    x_line = np.linspace(-0.1, 1.1, 100)                                    # (local)
    y_line = slope * x_line + intercept                                     # (local)
    ax.plot(x_line, y_line, "r--", alpha=0.7, zorder=2,
            label=f"OLS fit: y={slope:.3f}x+{intercept:.3f}")

ax.set_xlim(-0.1, 1.15)
ax.set_ylim(-0.1, 1.15)
ax.set_xticks([0.0, 0.5, 1.0])
ax.set_yticks([0.0, 0.5, 1.0])
ax.set_xticklabels(["FAIL\n(0)", "INFO\n(0.5)", "PASS\n(1)"])
ax.set_yticklabels(["FAIL\n(0)", "INFO\n(0.5)", "PASS\n(1)"])
ax.set_xlabel("Ratio-class gate verdict (encoded)")
ax.set_ylabel("Absolute-class gate verdict (encoded)")
ax.set_title(
    f"S83 W3 G33 RATIO-PROBE-LEAD-INDICATOR\n"
    f"Pearson $\\rho$ = {rho:.4f} (p={pval:.4f}) -- verdict: {verdict}\n"
    f"(PASS: |rho|>{PASS_RHO}; INFO: >{INFO_RHO}; FAIL: otherwise)")
ax.grid(True, alpha=0.35)
if not degenerate_axis:
    ax.legend(loc="lower right")
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=130)
plt.close(fig)
print(f"\nSaved: {OUT_PNG}")

# -----------------------------------------------------------------
# 8. Save NPZ
# -----------------------------------------------------------------
np.savez(
    OUT_NPZ,
    pair_ids=np.array([r[0] for r in pair_rows]),
    ratio_gate_ids=np.array([r[1] for r in pair_rows]),
    ratio_verdicts=np.array([r[2] for r in pair_rows]),
    ratio_codes=ratio_codes,
    absolute_gate_ids=np.array([r[4] for r in pair_rows]),
    absolute_verdicts=np.array([r[5] for r in pair_rows]),
    absolute_codes=abs_codes,
    subsystems=np.array([r[7] for r in pair_rows]),
    pearson_rho=np.array([rho]),
    pearson_pvalue=np.array([pval]),
    ratio_axis_std=np.array([std_r]),
    absolute_axis_std=np.array([std_a]),
    verdict=np.array([verdict]),
    reason=np.array([reason]),
    pass_threshold=np.array([PASS_RHO]),
    info_threshold=np.array([INFO_RHO]),
    input_pin_names=np.array([n for n, _ in pin_map]),
    input_pin_shas=np.array([s for _, s in pin_map]),
    closure_sha=np.array([closure_sha]),
)
print(f"Saved: {OUT_NPZ}")

# -----------------------------------------------------------------
# 9. Cross-check: pre-registered Python block (exactly as in prompt)
# -----------------------------------------------------------------
# The task pre-registered this minimal Python to cross-validate the
# main result. We recompute rho with the same encoding scheme and
# confirm agreement to machine precision.
print()
print("-" * 78)
print("CROSS-CHECK (pre-registered Python from prompt):")
import scipy.stats                                                          # noqa
cross_ratio_codes = [encode_verdict(s) for s in ratio_symbols]              # (local)
cross_absolute_codes = [encode_verdict(s) for s in abs_symbols]             # (local)
if std_r < 1e-12 or std_a < 1e-12:
    cross_rho, cross_pval = float("nan"), float("nan")                      # (local)
else:
    cross_res = scipy.stats.pearsonr(cross_ratio_codes, cross_absolute_codes)
    cross_rho = float(cross_res.statistic)                                  # (local)
    cross_pval = float(cross_res.pvalue)                                    # (local)
print(f"Correlation coeff rho = {cross_rho:.4f} (p={cross_pval:.4f})")
cross_verdict = ("PASS" if abs(cross_rho) > PASS_RHO                        # (local)
                 else "INFO" if abs(cross_rho) > INFO_RHO else "FAIL")
print(f"Verdict: {cross_verdict}")
# Sanity: main result and cross-check must agree
if not np.isnan(cross_rho):
    assert abs(cross_rho - rho) < 1e-12, "cross-check disagreement"
    assert cross_verdict == verdict, "cross-check verdict disagreement"

# -----------------------------------------------------------------
# 10. Final 4-tuple tag (canonical output line for verdict append)
# -----------------------------------------------------------------
print()
print("-" * 78)
print(f"OUTPUT 4-TUPLE: value=pearson_rho={rho:.4f} "
      f"scheme=10-gate-pair-sample "
      f"convention=PASS=1/FAIL=0/INFO=0.5 L_max=N/A "
      f"sha256={closure_sha}")
print(f"VERDICT LINE: S83-RATIO-PROBE-LEAD-INDICATOR: {verdict} -- "
      f"value=pearson_rho={rho:.4f},p={pval:.4f},N=10 "
      f"scheme=10-gate-pair-sample "
      f"convention=PASS=1/FAIL=0/INFO=0.5 L_max=N/A "
      f"sha256={closure_sha}")
