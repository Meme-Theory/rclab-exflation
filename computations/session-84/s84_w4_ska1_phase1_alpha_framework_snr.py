"""
S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR  (S84 W4-43)
--------------------------------------------------

Gate: S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR
Trigger: [VERIFY][CHAIN]
Classification: PHONONIC (GGE bispectrum running observable)

Hypothesis: SNR_SKA1 = |alpha_framework| / sigma(alpha)_SKA1 reaches >= 2-sigma
detectability in SKA-1 Phase-1 (2027-2029 window, pre-SKA-2).

Substitution chain:
  Step 1 (definition):    SNR = |signal| / noise = |alpha_framework| / sigma(alpha)
  Step 2 (substitution):  alpha_framework from #38 = -0.142566 (sigma_alpha_pred = 0.0441790)
                          sigma(alpha)_SKA1 = 5.118   (G45 canonical, S83 pre-reg)
                          sigma(alpha)_SKA2 = 0.80    (G45 PASS target, 2032-2035)
  Step 3 (simplification):SNR_SKA1 = 0.142566 / 5.118
                          SNR_SKA2 = 0.142566 / 0.80
  Step 4 (direction):     Compare each to threshold. PASS iff SNR >= 2.

PASS / INFO / FAIL thresholds (pre-registered in plan W4 §W4-43):
  PASS: SNR_SKA1 >= 2       -> SKA-1 is a pre-SKA-2 discriminator
  INFO: 1 <= SNR_SKA1 < 2   -> marginal; SKA-2 is the strong channel
  FAIL: SNR_SKA1 < 1        -> SKA-1 cannot see alpha; SKA-2 / 21-cm sole

Machinery pin (PRDR):
  alpha_framework        : read from #38 npz (value, sigma); no recomputation
  sigma_alpha_SKA1       : 5.118   (plan-authoritative, G45 S83 canonical)
  sigma_alpha_SKA2       : 0.80    (plan-authoritative, G45 PASS)
  Threshold              : SNR >= 2
  SKA-1 timeline         : first-light 2027-Q1, first-science 2027-Q3, Phase-1 full 2029
  SKA-2 timeline         : 2032-2035 full science operations

Outputs:
  computations/session-84/s84_w4_ska1_phase1_alpha_framework_snr.py   (this file)
  computations/session-84/s84_w4_ska1_phase1_alpha_framework_snr.npz
  verdict line appended to s84_gate_verdicts.txt
  working-paper section §VI.W4-43 written separately
"""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403  -- standard framework imports

# ---------------------------------------------------------------------------
# 0.  File paths and SHA-256 input pins
# ---------------------------------------------------------------------------
DATA_DIR = Path(__file__).resolve().parent
UPSTREAM_PRED_NPZ = DATA_DIR / "s84_w4_alpha_fnl_framework_pred.npz"      # #38
G45_SKA_NPZ       = DATA_DIR / "s83_w3_g45_ska_alpha_fnl.npz"              # G45 canonical (if present)
CANON_PY          = DATA_DIR / "canonical_constants.py"

OUT_NPZ           = DATA_DIR / "s84_w4_ska1_phase1_alpha_framework_snr.npz"
VERDICT_FILE      = DATA_DIR / "s84_gate_verdicts.txt"


def sha256_file(path: Path) -> str:
    """Return full 64-char hex SHA-256 of a file (empty string if missing)."""
    if not path.exists():
        return ""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# 1.  Compute and log input SHAs FIRST (first 20 lines of stdout)
# ---------------------------------------------------------------------------
sha_upstream  = sha256_file(UPSTREAM_PRED_NPZ)
sha_g45       = sha256_file(G45_SKA_NPZ)
sha_canon     = sha256_file(CANON_PY)

print("=" * 78)
print("S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR  --  INPUT PIN MAP")
print("=" * 78)
print(f"  upstream_38_npz     : {UPSTREAM_PRED_NPZ.name}")
print(f"    sha256            : {sha_upstream}")
print(f"  g45_ska_npz         : {G45_SKA_NPZ.name}")
print(f"    sha256            : {sha_g45 if sha_g45 else '<not present -- using plan-pinned sigma values>'}")
print(f"  canonical_constants : {CANON_PY.name}")
print(f"    sha256            : {sha_canon}")
print("=" * 78)

# ---------------------------------------------------------------------------
# 2.  Load alpha_framework from #38 upstream output
# ---------------------------------------------------------------------------
if not UPSTREAM_PRED_NPZ.exists():
    raise FileNotFoundError(
        f"Upstream #38 output not found: {UPSTREAM_PRED_NPZ}. "
        "Gate cannot run without alpha_framework from #38."
    )

up = np.load(UPSTREAM_PRED_NPZ, allow_pickle=True)
alpha_framework_signed = float(up["alpha_fnl_value"])            # (local)  signed value
sigma_alpha_pred       = float(up["alpha_fnl_sigma"])            # (local)  prediction 1-sigma band
alpha_framework_abs    = abs(alpha_framework_signed)             # (local)

print("\nUpstream #38 alpha_framework extracted:")
print(f"  alpha_fnl_value (signed) = {alpha_framework_signed:+.6f}")
print(f"  |alpha_framework|        = {alpha_framework_abs:.6f}")
print(f"  sigma_alpha_pred (1-sig) = {sigma_alpha_pred:.6f}")
print(f"  relative uncertainty     = {sigma_alpha_pred / alpha_framework_abs * 100.0:.2f}%")

# ---------------------------------------------------------------------------
# 3.  Plan-pinned detector noise terms (SECTION E-class; plan-authoritative)
# ---------------------------------------------------------------------------
# These are the canonical pins from the W4-43 plan block. They are the G45
# canonical values (S83 pre-reg) and are plan-authoritative for this gate,
# overriding any sidebar value in #38's own printed output.
sigma_alpha_SKA1 = 5.118    # (local)  G45 canonical, S83 pre-reg  -- SKA-1 Phase-1
sigma_alpha_SKA2 = 0.80     # (local)  G45 PASS threshold          -- SKA-2 full

# Pre-registered threshold
SNR_PASS_THRESHOLD = 2.0    # (local)
SNR_INFO_THRESHOLD = 1.0    # (local)

# ---------------------------------------------------------------------------
# 4.  Substitution chain -- explicit
# ---------------------------------------------------------------------------
print("\n" + "-" * 78)
print("SUBSTITUTION CHAIN  [VERIFY][CHAIN]")
print("-" * 78)
print("  Step 1 (definition):")
print("    SNR = |alpha_framework| / sigma(alpha)")
print("  Step 2 (substitution):")
print(f"    |alpha_framework|  = {alpha_framework_abs:.6f}")
print(f"    sigma(alpha)_SKA1  = {sigma_alpha_SKA1:.3f}")
print(f"    sigma(alpha)_SKA2  = {sigma_alpha_SKA2:.3f}")
SNR_SKA1 = alpha_framework_abs / sigma_alpha_SKA1                # (local)
SNR_SKA2 = alpha_framework_abs / sigma_alpha_SKA2                # (local)
print("  Step 3 (simplification):")
print(f"    SNR_SKA1 = {alpha_framework_abs:.6f} / {sigma_alpha_SKA1:.3f} = {SNR_SKA1:.6f}")
print(f"    SNR_SKA2 = {alpha_framework_abs:.6f} / {sigma_alpha_SKA2:.3f} = {SNR_SKA2:.6f}")
print("  Step 4 (direction vs pre-registered thresholds):")
print(f"    PASS iff SNR >= {SNR_PASS_THRESHOLD}")
print(f"    INFO iff {SNR_INFO_THRESHOLD} <= SNR < {SNR_PASS_THRESHOLD}")
print(f"    FAIL iff SNR < {SNR_INFO_THRESHOLD}")

# ---------------------------------------------------------------------------
# 5.  Classify
# ---------------------------------------------------------------------------
def classify(snr: float) -> str:
    if snr >= SNR_PASS_THRESHOLD:
        return "PASS"
    if snr >= SNR_INFO_THRESHOLD:
        return "INFO"
    return "FAIL"


verdict_SKA1 = classify(SNR_SKA1)                                # (local)
verdict_SKA2 = classify(SNR_SKA2)                                # (local)

ratio_below_pass_SKA1 = SNR_PASS_THRESHOLD / SNR_SKA1 if SNR_SKA1 > 0 else float("inf")  # (local)
ratio_below_info_SKA1 = SNR_INFO_THRESHOLD / SNR_SKA1 if SNR_SKA1 > 0 else float("inf")  # (local)
ratio_below_pass_SKA2 = SNR_PASS_THRESHOLD / SNR_SKA2 if SNR_SKA2 > 0 else float("inf")  # (local)

print("\n" + "-" * 78)
print("RESULTS")
print("-" * 78)
print(f"  SNR_SKA1                 = {SNR_SKA1:.6f}")
print(f"  Verdict (SKA-1)          = {verdict_SKA1}")
print(f"  Ratio below PASS (SKA-1) = {ratio_below_pass_SKA1:.2f}x")
print(f"  Ratio below INFO (SKA-1) = {ratio_below_info_SKA1:.2f}x")
print()
print(f"  SNR_SKA2 (cross-check)   = {SNR_SKA2:.6f}")
print(f"  Verdict (SKA-2)          = {verdict_SKA2}")
print(f"  Ratio below PASS (SKA-2) = {ratio_below_pass_SKA2:.2f}x")

# ---------------------------------------------------------------------------
# 6.  Closure SHA over ordered input-pin map
# ---------------------------------------------------------------------------
pin_map = (
    f"gate=S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR\n"
    f"upstream_38_sha={sha_upstream}\n"
    f"g45_ska_sha={sha_g45}\n"
    f"canon_sha={sha_canon}\n"
    f"alpha_framework_signed={alpha_framework_signed:.9e}\n"
    f"alpha_framework_abs={alpha_framework_abs:.9e}\n"
    f"sigma_alpha_pred={sigma_alpha_pred:.9e}\n"
    f"sigma_alpha_SKA1={sigma_alpha_SKA1:.9e}\n"
    f"sigma_alpha_SKA2={sigma_alpha_SKA2:.9e}\n"
    f"SNR_SKA1={SNR_SKA1:.9e}\n"
    f"SNR_SKA2={SNR_SKA2:.9e}\n"
    f"threshold_PASS={SNR_PASS_THRESHOLD:.3f}\n"
    f"threshold_INFO={SNR_INFO_THRESHOLD:.3f}\n"
    f"verdict_SKA1={verdict_SKA1}\n"
    f"verdict_SKA2={verdict_SKA2}\n"
)
content_sha = hashlib.sha256(pin_map.encode("utf-8")).hexdigest()
audit_sha = hashlib.sha256(
    (f"audit|{verdict_SKA1}|{SNR_SKA1:.9e}|{sha_upstream}|{sigma_alpha_SKA1:.6f}").encode("utf-8")
).hexdigest()

print("\n" + "-" * 78)
print(f"  content_sha256 = {content_sha}")
print(f"  audit_sha256   = {audit_sha}")
print("-" * 78)

# ---------------------------------------------------------------------------
# 7.  Save .npz artifact
# ---------------------------------------------------------------------------
np.savez(
    OUT_NPZ,
    gate_id="S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR",
    alpha_framework_signed=alpha_framework_signed,
    alpha_framework_abs=alpha_framework_abs,
    sigma_alpha_pred=sigma_alpha_pred,
    sigma_alpha_SKA1=sigma_alpha_SKA1,
    sigma_alpha_SKA2=sigma_alpha_SKA2,
    SNR_SKA1=SNR_SKA1,
    SNR_SKA2=SNR_SKA2,
    threshold_PASS=SNR_PASS_THRESHOLD,
    threshold_INFO=SNR_INFO_THRESHOLD,
    verdict_SKA1=verdict_SKA1,
    verdict_SKA2=verdict_SKA2,
    ratio_below_pass_SKA1=ratio_below_pass_SKA1,
    ratio_below_info_SKA1=ratio_below_info_SKA1,
    ratio_below_pass_SKA2=ratio_below_pass_SKA2,
    upstream_38_sha=sha_upstream,
    g45_ska_sha=sha_g45,
    canon_sha=sha_canon,
    content_sha=content_sha,
    audit_sha=audit_sha,
    ska1_timeline="commissioning=2027-Q1; first-science=2027-Q3; phase1-full=2029",
    ska2_timeline="full-science=2032-2035",
    fallback_channel_21cm="l_max ~ 1e5 required; post-reion 21-cm tomography",
    carry_forward_shape_folded="folded-triangle shape f_NL (substrate-unique pair-prod)",
)
print(f"\nSaved: {OUT_NPZ}")

# ---------------------------------------------------------------------------
# 8.  Append verdict line (S84+ dual-64-char-SHA form)
# ---------------------------------------------------------------------------
verdict_line = (
    f"S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR: {verdict_SKA1} "
    f"-- value={SNR_SKA1:.6e} "
    f"scheme=Fisher-alpha-SKA1 "
    f"convention=equilateral-alpha "
    f"L_max=N/A "
    f"audit_sha256={audit_sha} "
    f"content_sha256={content_sha}\n"
)
with open(VERDICT_FILE, "a", encoding="utf-8") as fh:
    fh.write(verdict_line)
print("\nAppended verdict line:")
print("  " + verdict_line.strip())

# ---------------------------------------------------------------------------
# 9.  Expected-output 4-tuple (final non-verdict stdout line, per template)
# ---------------------------------------------------------------------------
FOUR_TUPLE = (
    f"(value={SNR_SKA1:.6f}, scheme=Fisher-alpha-SKA1, "
    f"convention=equilateral-alpha, L_max=N/A)"
)
print("\n" + FOUR_TUPLE)
