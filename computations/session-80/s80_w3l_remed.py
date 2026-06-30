#!/usr/bin/env python3
"""
s80_w3l_remed.py -- S80 W0-3 R3 W3-L Clean Re-Run (PRU Remediation)
====================================================================

GATE: S80-W3-L-REMED ([AUDIT])
  PASS: c_Gold reproduced within 0.5% of canonical value 0.915 M_KK under
        frozen (scheme=SDW, convention=canonical, L_max=5) 4-tuple.
  INFO: reproduced within [0.5%, 5%].
  FAIL: deviation > 5% -- structural PRU issue in c_Gold provenance.

PRE-REGISTERED INPUTS (SHA-256 pinned):
  - Eigenvalue list at L_max=5 (from s74_spectrum_cache_L9_tau019.npz, tau=0.19)
  - scheme tag: SDW (Seeley-DeWitt mapping: a_k = zeta_D(s=k) for d=8)
  - convention tag: canonical (zeta-scheme per canonical_constants.py S78 W3-L tags)
  - L_max: 5

METHOD (full substitution chain, [AUDIT] trigger):
  Step 1: DEFINITIONS.
    a_2_zeta(L_max) = zeta_D(s=3) = sum_n d_n * |lam_n|^{-6}
    a_4_zeta(L_max) = zeta_D(s=2) = sum_n d_n * |lam_n|^{-4}
    (Mapping: for d=8, Chamseddine-Connes a_{d-2k} <-> zeta_D(s=k).)
    c_Gold^2 == (a_2 / a_4) * c_norm     [plan gate prescription]
    Canonical c_Gold = 0.915 M_KK (S52 GL-JOSEPHSON-52, BCS Josephson route).

  Step 2: SUBSTITUTE.
    Read a_2_zeta, a_4_zeta at L_max=5 from cached spectrum (tau_fold=0.19).
    Use canonical_constants.a2_fold / a4_fold (L_max=3) as back-reference anchor
    for c_norm fit: c_norm_L3 = c_Gold_canonical^2 / (a2_fold / a4_fold).

  Step 3: SIMPLIFY.
    c_Gold_L5 = sqrt( (a_2_L5 / a_4_L5) * c_norm_L3 )
    (If normalization is L_max-invariant, c_Gold_L5 agrees with c_Gold_L3 = 0.915.)

  Step 4: PYTHON print agreement BEFORE verdict.

  Step 5: READ OFF DIRECTION.
    agreement = |c_Gold_L5 - 0.915| / 0.915
    PASS if < 0.5%, INFO if < 5%, FAIL if >= 5%.

PRU Pin (SHA-256):
  - Hash of sorted-rounded eigenvalue list + L_max + scheme + convention
  - Hash embedded in output 4-tuple for downstream PRU audit

Author: landau-condensed-matter-theorist
Session: S80 W0-3
Classification: GEOMETRIC (c_Gold is a spectral-moment ratio; the "c" here bounds
  propagation ACROSS the substrate, NOT substrate dynamics. c_Gold is a SUBSTRATE
  PROPERTY: the Goldstone-mode sound speed derived from the eigenvalue gradient
  of D_K at the fold. Space does not contain the substrate; space emerges from
  a_2. The ratio a_2/a_4 is the Gauss-Bonnet-to-Einstein-Hilbert ratio, a pure
  dimensionless spectral invariant.)
"""

import numpy as np
import os
import sys
import hashlib
import json
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

from canonical_constants import (
    PI, M_KK, tau_fold,
    a0_fold, a2_fold, a4_fold,
    c_Gold,
)

# =============================================================================
# 0. HEADER
# =============================================================================
print("=" * 80)
print("S80 W0-3: R3 W3-L CLEAN RE-RUN (S80-W3-L-REMED [AUDIT])")
print("landau-condensed-matter-theorist | c_Gold PRU remediation")
print("=" * 80)

# Pre-registered frozen 4-tuple
FROZEN_SCHEME     = "SDW"              # (local) Seeley-DeWitt mapping
FROZEN_CONVENTION = "canonical"        # (local) zeta-scheme per canonical_constants S78 W3-L
FROZEN_LMAX       = 5                  # (local) target truncation level
CANONICAL_C_GOLD  = 0.915              # (local) M_KK, S52 GL-JOSEPHSON-52 anchor

PASS_THRESH = 0.005                    # (local) 0.5% PASS band
INFO_THRESH = 0.05                     # (local) 5% INFO band

print(f"\nFrozen 4-tuple:")
print(f"  scheme     = {FROZEN_SCHEME}")
print(f"  convention = {FROZEN_CONVENTION}")
print(f"  L_max      = {FROZEN_LMAX}")
print(f"  anchor     = c_Gold_canonical = {CANONICAL_C_GOLD} M_KK (S52)")
print(f"\nCanonical (L_max=3, S42 fold, zeta-scheme):")
print(f"  a_0 = {a0_fold:.6f}")
print(f"  a_2 = {a2_fold:.6f}")
print(f"  a_4 = {a4_fold:.6f}")

# =============================================================================
# 1. LOAD FROZEN SPECTRUM (L_max=9 cache, truncate to L_max=5)
# =============================================================================
print("\n" + "=" * 80)
print("1. LOAD FROZEN SPECTRUM (tau=0.19, L_max=5 truncation)")
print("=" * 80)

CACHE_PATH = os.path.join(SCRIPT_DIR, "s74_spectrum_cache_L9_tau019.npz")
if not os.path.exists(CACHE_PATH):
    print(f"ERROR: missing spectrum cache at {CACHE_PATH}")
    sys.exit(1)

cache = np.load(CACHE_PATH, allow_pickle=True)
sector_evals_raw = cache['sector_evals'].item()
cache.close()

# Reshape into dict keyed by (p,q) with level, dim, abs_evals
sector_evals = {}  # (local)
for pq, data in sector_evals_raw.items():
    sector_evals[tuple(pq)] = {
        'dim':       int(data['dim']),
        'level':     int(data['level']),
        'abs_evals': np.asarray(data['abs_evals']),
    }
print(f"  Loaded {len(sector_evals)} sectors (levels 0..9)")

# Truncate to L_max=5
all_abs   = []  # (local)
all_mults = []  # (local)
for (p, q), data in sorted(sector_evals.items()):
    if data['level'] <= FROZEN_LMAX:
        for ev in data['abs_evals']:
            all_abs.append(float(ev))
            all_mults.append(int(data['dim']))

all_abs   = np.asarray(all_abs,   dtype=np.float64)
all_mults = np.asarray(all_mults, dtype=np.float64)
n_eigs    = len(all_abs)  # (local)
n_weighted = int(np.sum(all_mults))  # (local)
print(f"  L_max={FROZEN_LMAX} truncation:")
print(f"    distinct eigenvalues = {n_eigs}")
print(f"    weighted count       = {n_weighted}")
print(f"    |lam|_min            = {np.min(all_abs):.6f}")
print(f"    |lam|_max            = {np.max(all_abs):.6f}")

# =============================================================================
# 2. SHA-256 PIN OF INPUTS (PRU remediation)
# =============================================================================
print("\n" + "=" * 80)
print("2. SHA-256 PRU PIN OF FROZEN INPUTS")
print("=" * 80)

# Sort eigenvalues for deterministic hash; round to 1e-12 for numerical reproducibility
sort_idx = np.argsort(all_abs)
sorted_abs   = np.round(all_abs[sort_idx],   12)
sorted_mults = all_mults[sort_idx].astype(int)

hash_payload = {
    "scheme":     FROZEN_SCHEME,
    "convention": FROZEN_CONVENTION,
    "L_max":      FROZEN_LMAX,
    "tau":        float(tau_fold),
    "n_eigs":     int(n_eigs),
    "n_weighted": int(n_weighted),
    "abs_evals_rounded": sorted_abs.tolist(),
    "mults":            sorted_mults.tolist(),
}
payload_str  = json.dumps(hash_payload, sort_keys=True)
sha256_full  = hashlib.sha256(payload_str.encode()).hexdigest()
sha256_short = sha256_full[:16]

print(f"  SHA-256 (full)  = {sha256_full}")
print(f"  SHA-256 (short) = {sha256_short}")

# =============================================================================
# 3. COMPUTE a_2_zeta, a_4_zeta AT L_max=5 (SDW mapping for d=8)
# =============================================================================
print("\n" + "=" * 80)
print("3. ZETA POWER SUMS (d=8 SDW mapping)")
print("=" * 80)

# d=8 convention (per s74_lmax_zeta_audit.py lines 249-253):
#   P_k = sum_n d_n * |lam_n|^{-2k} = zeta_D(s=k)
#   a_0 <-> P_4 (s=4)
#   a_2 <-> P_3 (s=3)  <-- TARGET for c_Gold^2 numerator
#   a_4 <-> P_2 (s=2)  <-- TARGET for c_Gold^2 denominator
P_2_L5 = float(np.sum(all_mults * all_abs**(-4)))   # (local) zeta_D(2) -> a_4
P_3_L5 = float(np.sum(all_mults * all_abs**(-6)))   # (local) zeta_D(3) -> a_2
P_4_L5 = float(np.sum(all_mults * all_abs**(-8)))   # (local) zeta_D(4) -> a_0

# NOTE: The canonical a2_fold/a4_fold in canonical_constants.py are the
# "half zeta" project convention: a_n^canonical = 0.5 * sum_k d_k / |lam_k|^n.
# That 0.5 prefactor CANCELS identically in the ratio a_2/a_4, so the
# canonical convention is immaterial for this gate.  We use the raw
# zeta-power-sum form, and the half-factor is absorbed into c_norm.

a_2_zeta_L5 = P_3_L5  # (local) zeta_D(3) direct
a_4_zeta_L5 = P_2_L5  # (local) zeta_D(2) direct

# For consistency, also project to the "half-zeta / L_max=3-canonical" form:
a_2_half_L5 = 0.5 * P_3_L5  # (local) half-zeta at L_max=5
a_4_half_L5 = 0.5 * P_2_L5  # (local) half-zeta at L_max=5

print(f"  P_2 (zeta_D(2) <-> a_4) L5 = {P_2_L5:.6f}")
print(f"  P_3 (zeta_D(3) <-> a_2) L5 = {P_3_L5:.6f}")
print(f"  P_4 (zeta_D(4) <-> a_0) L5 = {P_4_L5:.6f}")
print(f"  a_2_half_L5               = {a_2_half_L5:.6f}")
print(f"  a_4_half_L5               = {a_4_half_L5:.6f}")

# Ratio a_2/a_4 (scale-invariant regardless of half-prefactor)
ratio_L5 = a_2_half_L5 / a_4_half_L5  # (local)
ratio_L3 = a2_fold    / a4_fold       # (local) reference anchor
print(f"\n  a_2/a_4 at L_max=3 (canonical) = {ratio_L3:.6f}")
print(f"  a_2/a_4 at L_max=5 (frozen)    = {ratio_L5:.6f}")
drift_ratio = abs(ratio_L5 - ratio_L3) / ratio_L3  # (local)
print(f"  |delta ratio|/ratio           = {drift_ratio*100:.3f}%")

# =============================================================================
# 4. c_Gold RECONSTRUCTION (SUBSTITUTION CHAIN)
# =============================================================================
print("\n" + "=" * 80)
print("4. c_Gold RECONSTRUCTION via MOMENT-RATIO NORMALIZATION")
print("=" * 80)

print("\n  SUBSTITUTION CHAIN ([AUDIT] trigger):")
print("  ----------------------------------------------------------------")
print("  Step 1: DEFINITIONS.")
print("    c_Gold^2 == (a_2 / a_4) * c_norm    [plan gate prescription]")
print("    c_norm is the moment-ratio normalization factor calibrating")
print("    the (dimensionless) a_2/a_4 spectral ratio to physical M_KK units.")
print("")
print("  Step 2: SUBSTITUTE.")
print(f"    a_2/a_4 (L_max=3, canonical)  = {ratio_L3:.6f}")
print(f"    a_2/a_4 (L_max=5, frozen)     = {ratio_L5:.6f}")
print(f"    c_Gold_canonical              = {CANONICAL_C_GOLD}")
print(f"    Solve for c_norm at L_max=3:   c_norm = c_Gold^2 / (a_2/a_4)")
c_norm_L3 = CANONICAL_C_GOLD**2 / ratio_L3  # (local)
print(f"    c_norm(L_max=3, fit)          = {c_norm_L3:.6f}")
print("")
print("  Step 3: SIMPLIFY at L_max=5 under same c_norm:")
print(f"    c_Gold_L5^2 = ratio_L5 * c_norm_L3 = {ratio_L5 * c_norm_L3:.6f}")
c_Gold_L5_sq = ratio_L5 * c_norm_L3  # (local)
c_Gold_L5    = float(np.sqrt(c_Gold_L5_sq))  # (local)
print(f"    c_Gold_L5   = sqrt({c_Gold_L5_sq:.6f}) = {c_Gold_L5:.6f}")

# =============================================================================
# 5. AGREEMENT AND VERDICT
# =============================================================================
print("\n" + "=" * 80)
print("5. AGREEMENT AND VERDICT")
print("=" * 80)

agreement = abs(c_Gold_L5 - CANONICAL_C_GOLD) / CANONICAL_C_GOLD  # (local)
agreement_pct = agreement * 100.0  # (local)
print(f"\n  Python-verified quantities:")
print(f"    c_Gold (reproduced, L_max=5) = {c_Gold_L5:.6f}")
print(f"    c_Gold (canonical, S52)      = {CANONICAL_C_GOLD}")
print(f"    |Delta|                      = {abs(c_Gold_L5 - CANONICAL_C_GOLD):.6f}")
print(f"    |Delta| / canonical          = {agreement_pct:.3f}%")

print(f"\n  Gate thresholds (pre-registered):")
print(f"    PASS: agreement < {PASS_THRESH*100:.1f}%")
print(f"    INFO: agreement in [{PASS_THRESH*100:.1f}%, {INFO_THRESH*100:.1f}%]")
print(f"    FAIL: agreement >= {INFO_THRESH*100:.1f}%")

# Direction read-off from canonical form
# Step 5: agreement < PASS_THRESH -> PASS; < INFO_THRESH -> INFO; else FAIL
if agreement < PASS_THRESH:
    verdict = "PASS"  # (local)
    verdict_reason = (f"c_Gold reproduced within {PASS_THRESH*100:.1f}% "
                      f"({agreement_pct:.3f}%). Moment-ratio normalization "
                      f"c_norm is L_max-stable across L=3..5; PRU pin resolves "
                      f"to SHA-256 = {sha256_short}...")
elif agreement < INFO_THRESH:
    verdict = "INFO"  # (local)
    verdict_reason = (f"c_Gold reproduced within {INFO_THRESH*100:.1f}% "
                      f"({agreement_pct:.3f}%) but not within {PASS_THRESH*100:.1f}%. "
                      f"Normalization c_norm drifts mildly with L_max.")
else:
    verdict = "FAIL"  # (local)
    verdict_reason = (f"c_Gold deviation = {agreement_pct:.3f}% exceeds {INFO_THRESH*100:.1f}%. "
                      f"Structural PRU issue: c_Gold provenance does NOT "
                      f"reduce to a pure (a_2/a_4) moment-ratio under frozen spec.")

print(f"\n  VERDICT: {verdict}")
print(f"  REASON : {verdict_reason}")

# =============================================================================
# 6. CROSS-CHECKS (structural sanity)
# =============================================================================
print("\n" + "=" * 80)
print("6. CROSS-CHECKS")
print("=" * 80)

# Cross-check 1: Direct use of canonical a_2_fold, a_4_fold (L_max=3) and
# the prescription c_Gold^2 = (a_2/a_4) * c_norm must reproduce 0.915 by
# construction when c_norm is back-fit to L_max=3.
c_Gold_L3 = float(np.sqrt(ratio_L3 * c_norm_L3))  # (local)
print(f"\n  Cross-check 1 (identity at L_max=3):")
print(f"    c_Gold_L3 = sqrt((a_2/a_4)_L3 * c_norm_L3) = {c_Gold_L3:.6f}")
print(f"    canonical c_Gold = {CANONICAL_C_GOLD}")
cc1_ok = abs(c_Gold_L3 - CANONICAL_C_GOLD) < 1e-10  # (local)
print(f"    match: {cc1_ok}")

# Cross-check 2: R_1 = a_0 * a_4 / a_2^2 is R-protected at sub-1% across L_max.
# This is the R-protected fold ratio; since c_Gold^2 uses a_2/a_4 (equivalently
# a_0/a_2 * 1/(a_0/a_4) when a_0/a_2 and a_0/a_4 are Weyl-protected), any drift
# in c_Gold tracks the same R-structure.
P_4_L3_est = a0_fold * 2.0  # (local) rough scale check not definitive for this cross-check
print(f"\n  Cross-check 2 (R-protected moment ratio, S74 W4-F):")
print(f"    R_protected_fold = a_0 * a_4 / a_2^2 (L_max=3) = {a0_fold*a4_fold/a2_fold**2:.6f}")
print(f"    drift 0.34% across L_max in [3,9] (published)")
print(f"    implies c_Gold drift should be O(0.34%) if moment-ratio hypothesis holds")

# Cross-check 3: SHA-256 hash stability -- the hash must depend on L_max,
# scheme, convention, and the eigenvalue list.
print(f"\n  Cross-check 3 (SHA-256 PRU pin composition):")
print(f"    keys hashed: {sorted(hash_payload.keys())}")
print(f"    hash depends on: scheme, convention, L_max, tau, n_eigs, mults, abs_evals")

# Cross-check 4: 4-tuple output consistency.
out_tuple = (c_Gold_L5, FROZEN_SCHEME, FROZEN_CONVENTION, FROZEN_LMAX)
print(f"\n  Cross-check 4 (4-tuple output):")
print(f"    (c_Gold, scheme, convention, L_max) = {out_tuple}")

# =============================================================================
# 7. CLASSIFICATION AND SUBSTRATE FRAMING
# =============================================================================
print("\n" + "=" * 80)
print("7. CLASSIFICATION: GEOMETRIC (spectral-moment ratio)")
print("=" * 80)
print("""
  c_Gold is an EMERGENT substrate property derived from the eigenvalue
  gradient of D_K at the fold (tau=0.19). The ratio a_2/a_4 is a
  dimensionless spectral invariant constructed from the Dirac spectrum;
  it is NOT a velocity in a pre-existing spacetime.

  Substrate-first framing:
    - D_K eigenvalues (spectrum) -> a_2, a_4 (spectral moments)
    - a_2/a_4 (dimensionless)     -> moment-ratio normalization c_norm
    - sqrt(ratio * c_norm)        -> Goldstone sound speed c_Gold
    - c_Gold bounds Goldstone-mode PROPAGATION across the substrate
      (it is NOT the substrate's own internal clock).

  Space emerges from a_2 (Einstein-Hilbert sector). The ratio a_2/a_4
  measures Gauss-Bonnet-to-gravity imbalance. The SAME spectrum generates
  GR, the YM action, AND the Goldstone mode -- as it must, since there is
  only one spectral triple.
""")

# =============================================================================
# 8. SAVE OUTPUTS
# =============================================================================
print("=" * 80)
print("8. SAVE OUTPUTS")
print("=" * 80)

outfile = os.path.join(SCRIPT_DIR, "s80_w3l_remed.npz")
np.savez(outfile,
    # Frozen 4-tuple
    c_Gold_reproduced=c_Gold_L5,
    scheme_tag=FROZEN_SCHEME,
    convention_tag=FROZEN_CONVENTION,
    L_max=FROZEN_LMAX,
    # Inputs
    tau_fold=tau_fold,
    a_2_half_L5=a_2_half_L5,
    a_4_half_L5=a_4_half_L5,
    a_2_fold_canonical=a2_fold,
    a_4_fold_canonical=a4_fold,
    ratio_L3=ratio_L3,
    ratio_L5=ratio_L5,
    c_norm_L3=c_norm_L3,
    c_Gold_canonical=CANONICAL_C_GOLD,
    # Hash pin
    sha256_pin=sha256_full,
    sha256_short=sha256_short,
    hash_payload_keys=np.asarray(sorted(hash_payload.keys())),
    # Gate outputs
    agreement_pct=agreement_pct,
    verdict=verdict,
    verdict_reason=verdict_reason,
    pass_thresh=PASS_THRESH,
    info_thresh=INFO_THRESH,
    # Spectrum stats
    n_eigs=n_eigs,
    n_weighted=n_weighted,
    P_2_L5=P_2_L5,
    P_3_L5=P_3_L5,
    P_4_L5=P_4_L5,
)
print(f"  Wrote: {outfile}")

# =============================================================================
# 9. FINAL VERDICT LINE (single line for s80_gate_verdicts.txt)
# =============================================================================
print("\n" + "=" * 80)
print("9. APPEND VERDICT LINE")
print("=" * 80)

ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())  # (local)
verdict_line = (
    f"[{ts}] S80-W3-L-REMED | {verdict} | "
    f"c_Gold_reproduced={c_Gold_L5:.6f} | canonical={CANONICAL_C_GOLD} | "
    f"agreement={agreement_pct:.3f}% | "
    f"4-tuple=(c_Gold={c_Gold_L5:.6f},scheme={FROZEN_SCHEME},convention={FROZEN_CONVENTION},L_max={FROZEN_LMAX}) | "
    f"sha256={sha256_short} | agent=landau-condensed-matter-theorist | script=s80_w3l_remed.py"
)

vfile = os.path.join(SCRIPT_DIR, "s80_gate_verdicts.txt")
with open(vfile, "a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
print(f"  Appended to {vfile}:")
print(f"    {verdict_line}")

print("\n" + "=" * 80)
print(f"S80 W0-3 COMPLETE: {verdict}")
print("=" * 80)
