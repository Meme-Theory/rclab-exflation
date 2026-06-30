"""
s87_w7_ic_per_class_verify.py — S87-W5A-P3-IC-PER-CLASS-VERIFY (CF-42)
=====================================================================

Per-class restriction of `xi_E_GGE_inv` for each of 5 L1-classes at Mellin
slot s=-1, with dual-prior track-discriminator (Track A F_2-class
STRUCTURAL-PRIMACY prior 0.4 / Track B per-class DIAGNOSTIC-only prior 0.6).

Plan reference: sessions/session-plan/session-87-plan-w7.md §W7-1.

5-class L1 partition (per S86 W-9 §E-R2.2 line 1099, STAGE-1-CANDIDATE; the
W-9 STAGE-1 entry is NOT YET landed in permanent-results-registry.md, so we
read the partition definition from the W-9 workshop file per §0.5(1) of the
plan with `class_partition_pin_pending=true`):
    A_5 = {zeta, SDW, cutoff_sqrt, anomaly, Zubarev}

Per-class affine projection (W-9 clause (b), line 1099):
    xi_R(s)  =  xi_E_GGE_inv  ·  M_R(s)  /  M_F2(s)
where M_R(s) is the substrate Mellin multiplier residue under regulator R
on the SU(3) Casimir schematic spectrum, and F_2 = {zeta, SDW} is the
2-element identity sub-atlas (zeta ≡ SDW machine-epsilon at s=3 per W4 P5
CC-2; at s=-1 the relation is also analytic-continuation identity, since
both prescriptions use the same multiplicity-weighted positive-definite
spectrum).

TIER declaration (per .claude/rules/substrate-first-canonical-sourcing.md
§iv "SCHEMATIC vs full physical" tier rule): the regulator helpers in
`computations/_shared/_spectral_action_regulators.py` are SCHEMATIC analogs
of the Connes-Chamseddine 1996 §2.2-2.3 regulator family per their own
docstring; this gate is TIER-2 (schematic analog), tagged in the verdict
line `convention=` field with the SCHEMATIC suffix.

Substitution chain (per .claude/rules/math-scripts.md):

    Definition 1: A_5 = {zeta, SDW, cutoff_sqrt, anomaly, Zubarev}
                  [W-9 §E-R2.2 line 1099]
    Definition 2: M_R(s) = (1/Vol_SU3_Haar) · Σ d(p,q) · f_R(C_2(p,q), -s)
                  At s=-1, n=-1: f_R(C, -1) is a Σ d · f_R · C^1 evaluation
                  with regulator-specific dressing.
    Definition 3: xi_R(s=-1) := xi_E_GGE_inv · M_R(s=-1) / M_F2(s=-1)
                  [W-9 affine projection, clause (b)]
    Definition 4: delta_max = max_{R,R'} |xi_R - xi_R'| / max(|xi_R|, |xi_R'|)
    Definition 5: delta_canonical = |mean({xi_R}) - xi_E_GGE_inv| / |xi_E_GGE_inv|

    Step 1 — Substitute Def 3 into Def 4:
        delta_max = max |xi_E_GGE_inv·(M_R - M_R')/M_F2|
                  / max(|xi_E_GGE_inv·M_R/M_F2|, |xi_E_GGE_inv·M_R'/M_F2|)
                  = max |M_R - M_R'| / max(|M_R|, |M_R'|)
        [xi_E_GGE_inv and M_F2 cancel as positive scalars]

    Step 2 — At s=-1 the regulator suppression hierarchy can FLIP relative
        to s=3 (per W-9 §Re:L2 Step 4 lines 615-621). The F_2 ceiling at
        s=3 is NOT guaranteed at s=-1.

    Step 3 — Numerical realization is computed below; no pre-stated direction.

    Step 4 — Direction (CONDITIONAL on numerical output):
        delta_max ≤ 0.05 ⇒ Track A (STRUCTURAL-PRIMACY) PASS
        delta_max > 0.20 ⇒ Track B (DIAGNOSTIC-only) FAIL
        0.05 < delta_max ≤ 0.20 ⇒ INFO band; posteriors near priors.

Substrate-framing reminder (per .claude/rules/phononic-framing.md §"IS Space,
Not IN Space"): the per-class projection P_c is a substrate-spectral
restriction of the Mellin multiplier on D_K eigenvalues — it is NOT a
container coordinate. The 5 classes EMERGE from the F_2 spectral-cluster
structure at the Mellin slot s=-1; they do not pre-exist as containers
for `xi_E_GGE_inv` to be "evaluated in".

Author: lizzi-spectral-functional-theorist (S87 W7 dispatch, 2026-04-30).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")  # (local) non-interactive backend
import matplotlib.pyplot as plt

# Ensure computations is on path so `from canonical_constants import *` works.
THIS_DIR = Path(__file__).parent.resolve()  # (local)
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from canonical_constants import (  # noqa: E402
    Vol_SU3_Haar,
    xi_E_GGE_inv,
    Delta_BCS,
    K_base,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

GATE_ID = "S87-W5A-P3-IC-PER-CLASS-VERIFY"  # (local)
SCHEME_TAG = "Mellin-slot-s=-1-SCHEMATIC"  # (local) TIER-2 SCHEMATIC per substrate-first-canonical-sourcing.md
CONVENTION_TAG = "substrate-natural-xi-E-GGE-SCHEMATIC"  # (local) TIER-2
L_MAX = 10  # (local) canonical S86 W4 P4 commit
S_SLOT = -1  # (local) Mellin slot, plan §W7-1.7 mellin_slot_pin
SCHEMA_VERSION = "S87+"  # (local)

# Dual-prior pins (FROZEN at plan-freeze; modifying is Class-3 PROHIBITED_ACTIONS)
PRIOR_A = 0.4  # (local) Track A: F_2-class STRUCTURAL-PRIMACY
PRIOR_B = 0.6  # (local) Track B: per-class DIAGNOSTIC-only
LIKELIHOOD_A_MU = 0.0  # (local) Gaussian-A center
LIKELIHOOD_A_SIGMA = 0.025  # (local) plan §W7-1.7 discriminator_likelihood_a_sigma
LIKELIHOOD_B_MU = 0.30  # (local) plan §W7-1.7 discriminator_likelihood_b_mu
LIKELIHOOD_B_SIGMA = 0.10  # (local) plan §W7-1.7 discriminator_likelihood_b_sigma

# Pass/fail/info thresholds (plan §W7-1.9; RATIO tolerance class)
PASS_DELTA_MAX = 0.05  # (local)
INFO_DELTA_MAX = 0.20  # (local)
PASS_DELTA_CANONICAL = 0.05  # (local)
INFO_DELTA_CANONICAL = 0.20  # (local)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def file_sha(path: Path) -> str:
    """Return SHA-256 hexdigest of file contents."""
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def text_sha(text: str) -> str:
    """Return SHA-256 hexdigest of a text string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """SHA-256 of the JSON-canonicalized ordered input-pin map."""
    canonical = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))  # (local)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def gaussian_pdf(x: float, mu: float, sigma: float) -> float:
    """Standard Gaussian PDF; pure Python (no scipy needed)."""
    return float(np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2.0 * np.pi)))


# ---------------------------------------------------------------------------
# 5-regulator per-class M_R(s) evaluator at Mellin slot s
# ---------------------------------------------------------------------------
# At Mellin slot s, the per-regulator multiplier residue (schematic, per
# `_spectral_action_regulators.py`) is:
#   M_R(s) = (1/Vol_SU3_Haar) · Σ_{(p,q)≠(0,0), p+q≤L_max} d(p,q) · f_R(C, -s)
# where f_R(C, n) is the regulator's Casimir-power dressing as a function of
# the spectral-moment index n = -s (so n=1 at s=-1 corresponds to evaluating
# the regulator on Σ d · f_R · C^{-(-1)} = Σ d · f_R · C^1, i.e. C^{1} with
# regulator-specific suppression).
#
# At s=-1, the canonical sums Σ d · C^1 diverge; the regulators play
# distinct roles:
#   - zeta / Mellin: analytic continuation of Σ d · C^{-s} to s=-1 — finite.
#     For the schematic (treating "zeta at s=-1" as an analytic continuation
#     stand-in), we evaluate the convergent partial sum at L_max=10 (a
#     SCHEMATIC truncation, NOT the strict analytic continuation; this is the
#     TIER-2 status of this gate).
#   - heat-kernel (Zubarev): exp(-tC)·C^{-s} — directly convergent at s=-1.
#   - hard-cutoff (cutoff_sqrt): step-truncated Σ d · C^1 — finite by truncation.
#   - Pauli-Villars (anomaly): Σ d · [C^1 - (C+M_PV²)·...]; subtractive.
#
# The schematic implementations evaluate ALL five regulators on the
# truncated SU(3) Casimir spectrum at L_max=10, so all five values are
# finite and comparable.

def weyl_dim_su3(p: int, q: int) -> int:
    """SU(3) Weyl dimension."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p: int, q: int) -> float:
    """Quadratic Casimir of SU(3) irrep (p, q) in normalized units."""
    return (p * p + p * q + q * q + 3 * (p + q)) / 3.0


def enumerate_sectors(L_max: int):
    """Yield (p, q, d, c) tuples for (p, q) != (0, 0), p+q ≤ L_max."""
    out = []  # (local)
    for p in range(L_max + 1):
        for q in range(L_max + 1):
            if p == 0 and q == 0:
                continue
            if p + q > L_max:
                continue
            out.append((p, q, weyl_dim_su3(p, q), casimir_su3(p, q)))
    return out


def M_R_at_s(regulator: str, s: int, L_max: int,
             cutoff_frac: float = 0.7, M_PV_sq_frac: float = 0.1,
             t_ref: float = 1.0e-3) -> float:
    """
    Substrate Mellin multiplier residue for regulator R at Mellin slot s.

    At slot s, the Casimir-power exponent is n = -s (so s=-1 ⇒ n=1, meaning
    Σ d(p,q) · f_R · C(p,q)^1 with regulator-specific weight).

    Naming map (W-9 5-class A_5 → schematic helper module):
        "zeta"        ↔ analytic-continuation (zeta_a_n; identity sub-atlas member)
        "SDW"         ↔ Mellin (mellin_a_n; identity sub-atlas member; ≡ zeta on
                        positive-definite spectrum at s in the convergent half-plane,
                        with Γ(s) cancellation in the multiplier ratio)
        "cutoff_sqrt" ↔ hard-cutoff (hard_cutoff_a_n)
        "anomaly"     ↔ Pauli-Villars (pauli_villars_a_n)
        "Zubarev"     ↔ heat-kernel (heat_kernel_a_n)
    """
    sectors = enumerate_sectors(L_max)  # (local)
    n = -s  # (local) canonical spectral-moment index
    Vol = Vol_SU3_Haar  # (local) substrate Haar-volume normalizer
    if regulator in ("zeta", "SDW"):
        # zeta and SDW collapse on the positive-definite Casimir spectrum at
        # any real s in the analytic-continuation domain. The schematic
        # evaluates Σ d · C^{-n} = Σ d · C^s as the convergent partial sum
        # at finite L_max=10. At n=1 (s=-1) this is Σ d · C^1, finite by
        # L_max truncation.
        acc = 0.0  # (local)
        for _, _, d, c in sectors:
            acc += d * (c ** s)  # C^s = C^(-n)
        return acc / Vol
    elif regulator == "cutoff_sqrt":
        # Hard cutoff at C ≤ cutoff_frac × C_max
        c_max = max(s_tup[3] for s_tup in sectors)  # (local)
        c_thresh = cutoff_frac * c_max  # (local)
        acc = 0.0  # (local)
        for _, _, d, c in sectors:
            if c <= c_thresh:
                acc += d * (c ** s)
        return acc / Vol
    elif regulator == "anomaly":
        # Pauli-Villars subtraction Σ d · [C^s - (C + M_PV²)^s]
        c_max = max(s_tup[3] for s_tup in sectors)  # (local)
        M_PV_sq = M_PV_sq_frac * c_max  # (local)
        acc = 0.0  # (local)
        for _, _, d, c in sectors:
            acc += d * ((c ** s) - ((c + M_PV_sq) ** s))
        return acc / Vol
    elif regulator == "Zubarev":
        # Heat-kernel exp(-tC) · C^{-n} = exp(-tC) · C^s
        acc = 0.0  # (local)
        for _, _, d, c in sectors:
            acc += d * float(np.exp(-t_ref * c)) * (c ** s)
        return acc / Vol
    else:
        raise ValueError(f"Unknown regulator: {regulator!r}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 78)
    print(f"{GATE_ID} — S87 W7-1 lizzi-spectral-functional-theorist")
    print("=" * 78)

    # -----------------------------------------------------------------------
    # Step 0 — Input SHA pinning (first 20 lines of stdout per gate-verdicts.md)
    # -----------------------------------------------------------------------
    canonical_constants_path = THIS_DIR / "canonical_constants.py"  # (local)
    spectrum_cache_path = THIS_DIR / "s84_spectrum_cache_L12_tau019.npz"  # (local)
    regulator_module_path = THIS_DIR / "_spectral_action_regulators.py"  # (local)
    plan_path = THIS_DIR.parent / "sessions" / "session-plan" / "session-87-plan-w7.md"  # (local)
    # W-9 STAGE-1 partition file (CF-54 not yet landed; read from W-9 workshop):
    w9_workshop_path = (
        THIS_DIR.parent / "sessions" / "session-86" / "workshops"
        / "s86-path-c-double-double-fail-reassessment.md"
    )  # (local)

    canonical_sha = file_sha(canonical_constants_path)  # (local)
    spectrum_cache_sha = file_sha(spectrum_cache_path)  # (local)
    regulator_module_sha = file_sha(regulator_module_path)  # (local)
    plan_sha = file_sha(plan_path)  # (local)
    w9_workshop_sha = file_sha(w9_workshop_path)  # (local)

    print(f"[INPUT-PIN] canonical_constants.py  sha256={canonical_sha}")
    print(f"[INPUT-PIN] s84_spectrum_cache       sha256={spectrum_cache_sha}")
    print(f"[INPUT-PIN] _spectral_action_regs    sha256={regulator_module_sha}")
    print(f"[INPUT-PIN] session-87-plan-w7.md    sha256={plan_sha}")
    print(f"[INPUT-PIN] s86-path-c-workshop      sha256={w9_workshop_sha}")
    print(f"[CANONICAL] xi_E_GGE_inv            = {xi_E_GGE_inv!r}")
    print(f"[CANONICAL] Delta_BCS               = {Delta_BCS!r}")
    print(f"[CANONICAL] K_base                  = {K_base!r}")
    print(f"[CANONICAL] Vol_SU3_Haar            = {Vol_SU3_Haar!r}")
    print(f"[PIN] L_max                         = {L_MAX}")
    print(f"[PIN] s (Mellin slot)               = {S_SLOT}")
    print(f"[PIN] PRIOR_A                       = {PRIOR_A}")
    print(f"[PIN] PRIOR_B                       = {PRIOR_B}")
    print(f"[PIN] LIKELIHOOD_A (mu, sigma)      = ({LIKELIHOOD_A_MU}, {LIKELIHOOD_A_SIGMA})")
    print(f"[PIN] LIKELIHOOD_B (mu, sigma)      = ({LIKELIHOOD_B_MU}, {LIKELIHOOD_B_SIGMA})")
    print(f"[PIN] PASS_DELTA_MAX                = {PASS_DELTA_MAX}")
    print(f"[PIN] INFO_DELTA_MAX                = {INFO_DELTA_MAX}")
    print(f"[PIN] class_partition_pin_pending   = true (CF-54 STAGE-1 not yet landed)")
    print(f"[NOTE] TIER-2 SCHEMATIC per substrate-first-canonical-sourcing.md §iv")
    print()

    # -----------------------------------------------------------------------
    # Step A — 5-class L1 partition (W-9 §E-R2.2 line 1099)
    # -----------------------------------------------------------------------
    classes = ("zeta", "SDW", "cutoff_sqrt", "anomaly", "Zubarev")  # (local)
    print(f"[STEP A] 5-class L1 partition (W-9 STAGE-1-CANDIDATE):")
    print(f"         A_5 = {classes}")
    print()

    # -----------------------------------------------------------------------
    # Step B — Per-class M_R(s=-1) and xi_c
    # -----------------------------------------------------------------------
    print(f"[STEP B] Per-class Mellin multiplier residue at s = {S_SLOT}:")
    M_at_s_neg1 = {}  # (local)
    for R in classes:
        M_at_s_neg1[R] = M_R_at_s(R, S_SLOT, L_MAX)
        print(f"         M_{R:>11s}(s={S_SLOT}) = {M_at_s_neg1[R]:.12e}")
    M_F2 = M_at_s_neg1["zeta"]  # (local) F_2 = {zeta, SDW}; pick zeta as anchor
    if M_F2 == 0.0:
        raise RuntimeError("M_F2 (zeta) at s=-1 is zero — affine projection undefined.")
    print(f"         M_F2 (zeta anchor)     = {M_F2:.12e}")
    print()

    print(f"[STEP B'] Per-class affine projection xi_R(s=-1) = xi_E_GGE_inv · M_R / M_F2:")
    xi_per_class = {}  # (local)
    for R in classes:
        xi_per_class[R] = xi_E_GGE_inv * M_at_s_neg1[R] / M_F2
        print(f"         xi_{R:>11s} = {xi_per_class[R]:.12e}")
    print()

    # -----------------------------------------------------------------------
    # Step C — Per-class dispersion
    # -----------------------------------------------------------------------
    xi_values = np.array([xi_per_class[R] for R in classes], dtype=np.float64)  # (local)
    xi_mean = float(np.mean(xi_values))  # (local)
    xi_std = float(np.std(xi_values, ddof=0))  # (local)
    sigma_xi_rel = xi_std / abs(xi_mean) if xi_mean != 0.0 else float("inf")  # (local)
    # Pairwise RATIO dispersion:
    delta_pairs = []  # (local)
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            denom = max(abs(xi_values[i]), abs(xi_values[j]))  # (local)
            if denom == 0.0:
                continue
            delta_pairs.append((classes[i], classes[j],
                                abs(xi_values[i] - xi_values[j]) / denom))
    delta_max = max(d for _, _, d in delta_pairs)  # (local)
    delta_max_pair = next((c1, c2) for c1, c2, d in delta_pairs if d == delta_max)  # (local)
    print(f"[STEP C] Per-class dispersion statistics:")
    print(f"         xi_mean                = {xi_mean:.12e}")
    print(f"         xi_std (population)    = {xi_std:.12e}")
    print(f"         sigma_xi_rel           = {sigma_xi_rel:.6e}")
    print(f"         delta_max              = {delta_max:.6e}  (pair: {delta_max_pair})")
    print()

    # -----------------------------------------------------------------------
    # Step D — delta_canonical
    # -----------------------------------------------------------------------
    delta_canonical = abs(xi_mean - xi_E_GGE_inv) / abs(xi_E_GGE_inv)  # (local)
    print(f"[STEP D] Consensus deviation from canonical xi_E_GGE_inv = {xi_E_GGE_inv}:")
    print(f"         delta_canonical        = {delta_canonical:.6e}")
    print()

    # -----------------------------------------------------------------------
    # Step E — Dual-prior posterior
    # -----------------------------------------------------------------------
    likelihood_A = gaussian_pdf(delta_max, LIKELIHOOD_A_MU, LIKELIHOOD_A_SIGMA)  # (local)
    likelihood_B = gaussian_pdf(delta_max, LIKELIHOOD_B_MU, LIKELIHOOD_B_SIGMA)  # (local)
    Z = likelihood_A * PRIOR_A + likelihood_B * PRIOR_B  # (local)
    if Z == 0.0:
        # Both likelihoods underflowed — fall back to priors
        posterior_A = PRIOR_A  # (local)
        posterior_B = PRIOR_B  # (local)
    else:
        posterior_A = (likelihood_A * PRIOR_A) / Z  # (local)
        posterior_B = (likelihood_B * PRIOR_B) / Z  # (local)
    print(f"[STEP E] Dual-prior posterior allocation:")
    print(f"         likelihood_A (mu={LIKELIHOOD_A_MU}, sigma={LIKELIHOOD_A_SIGMA})")
    print(f"                                = {likelihood_A:.6e}")
    print(f"         likelihood_B (mu={LIKELIHOOD_B_MU}, sigma={LIKELIHOOD_B_SIGMA})")
    print(f"                                = {likelihood_B:.6e}")
    print(f"         posterior_A (Track A)  = {posterior_A:.6e}")
    print(f"         posterior_B (Track B)  = {posterior_B:.6e}")
    print()

    # -----------------------------------------------------------------------
    # Step F — Cross-check: xi_R(s=-1) collapses to xi_E_GGE_inv when projection
    #          is identity (R = zeta / SDW; xi_zeta = xi_E_GGE_inv exactly).
    # -----------------------------------------------------------------------
    cc_zeta_identity = xi_per_class["zeta"]  # (local)
    cc_zeta_residual = abs(cc_zeta_identity - xi_E_GGE_inv) / abs(xi_E_GGE_inv)  # (local)
    cc_sdw_identity = xi_per_class["SDW"]  # (local)
    cc_sdw_residual = abs(cc_sdw_identity - xi_E_GGE_inv) / abs(xi_E_GGE_inv)  # (local)
    print(f"[STEP F] Cross-check identity (zeta and SDW are F_2; xi must equal canonical):")
    print(f"         xi_zeta - xi_E_GGE_inv (rel) = {cc_zeta_residual:.6e}")
    print(f"         xi_SDW  - xi_E_GGE_inv (rel) = {cc_sdw_residual:.6e}")
    print()

    # -----------------------------------------------------------------------
    # Step G — Verdict assignment (3-tuple + composite collapse)
    # -----------------------------------------------------------------------
    # sign_verdict: same sign as xi_E_GGE_inv (positive)?
    if xi_mean > 0:
        sign_verdict = "PASS"  # (local)
    else:
        sign_verdict = "FAIL"  # (local)

    # magnitude_verdict: PASS if delta_canonical ≤ 0.05; INFO if ≤ 0.20; FAIL else
    if delta_canonical <= PASS_DELTA_CANONICAL:
        magnitude_verdict = "PASS"  # (local)
    elif delta_canonical <= INFO_DELTA_CANONICAL:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)

    # regime_verdict: VALID if all 5 per-class M_R values finite + same sign
    n_finite = sum(1 for v in M_at_s_neg1.values() if np.isfinite(v))  # (local)
    n_same_sign = sum(1 for v in M_at_s_neg1.values()
                      if (v > 0) == (M_F2 > 0))  # (local)
    if n_finite == 5 and n_same_sign == 5:
        regime_verdict = "VALID"  # (local)
    elif n_finite >= 3 and n_same_sign >= 3:
        regime_verdict = "MARGINAL"  # (local)
    else:
        regime_verdict = "BREAKDOWN"  # (local)

    # Composite collapse rule per .claude/rules/gate-verdicts.md S87+ schema-v2
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    # Plan §W7-1.9 composite override: PASS requires delta_max ≤ 0.05 AND
    # delta_canonical ≤ 0.05 AND regime VALID; INFO if 0.05 < delta_max ≤ 0.20.
    # If delta_max > info threshold, FAIL even when delta_canonical happens to PASS.
    if delta_max > INFO_DELTA_MAX:
        composite = "FAIL"
    elif delta_max > PASS_DELTA_MAX and composite == "PASS":
        composite = "INFO"

    print(f"[STEP G] Verdict 3-tuple:")
    print(f"         sign_verdict           = {sign_verdict}")
    print(f"         magnitude_verdict      = {magnitude_verdict}")
    print(f"         regime_verdict         = {regime_verdict}")
    print(f"         composite (top-line)   = {composite}")
    print()

    # -----------------------------------------------------------------------
    # Step H — Closure SHA over input-pin map
    # -----------------------------------------------------------------------
    input_pin_map = {  # (local)
        "_gate_id": GATE_ID,
        "_scheme": SCHEME_TAG,
        "_convention": CONVENTION_TAG,
        "_L_max": L_MAX,
        "_s_slot": S_SLOT,
        "canonical_sha": canonical_sha,
        "spectrum_cache_sha": spectrum_cache_sha,
        "regulator_module_sha": regulator_module_sha,
        "plan_sha": plan_sha,
        "w9_workshop_sha": w9_workshop_sha,
        "xi_E_GGE_inv": repr(xi_E_GGE_inv),
        "Delta_BCS": repr(Delta_BCS),
        "K_base": repr(K_base),
        "Vol_SU3_Haar": repr(Vol_SU3_Haar),
        "PRIOR_A": PRIOR_A,
        "PRIOR_B": PRIOR_B,
        "LIKELIHOOD_A_MU": LIKELIHOOD_A_MU,
        "LIKELIHOOD_A_SIGMA": LIKELIHOOD_A_SIGMA,
        "LIKELIHOOD_B_MU": LIKELIHOOD_B_MU,
        "LIKELIHOOD_B_SIGMA": LIKELIHOOD_B_SIGMA,
        "PASS_DELTA_MAX": PASS_DELTA_MAX,
        "INFO_DELTA_MAX": INFO_DELTA_MAX,
        "PASS_DELTA_CANONICAL": PASS_DELTA_CANONICAL,
        "INFO_DELTA_CANONICAL": INFO_DELTA_CANONICAL,
        "classes": list(classes),
    }
    audit_sha256 = closure_hash(input_pin_map)  # (local)

    # Content SHA: hash of all numerical outputs (for downstream consumers)
    content_payload = {  # (local)
        "M_at_s_neg1": {R: repr(M_at_s_neg1[R]) for R in classes},
        "xi_per_class": {R: repr(xi_per_class[R]) for R in classes},
        "xi_mean": repr(xi_mean),
        "xi_std": repr(xi_std),
        "sigma_xi_rel": repr(sigma_xi_rel),
        "delta_max": repr(delta_max),
        "delta_max_pair": list(delta_max_pair),
        "delta_canonical": repr(delta_canonical),
        "posterior_A": repr(posterior_A),
        "posterior_B": repr(posterior_B),
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite": composite,
    }
    content_sha256 = text_sha(json.dumps(content_payload, sort_keys=True,
                                        separators=(",", ":")))  # (local)
    print(f"[STEP H] Closure SHAs:")
    print(f"         audit_sha256   = {audit_sha256}")
    print(f"         content_sha256 = {content_sha256}")
    print()

    # -----------------------------------------------------------------------
    # Step I — Save .npz + .png
    # -----------------------------------------------------------------------
    npz_path = THIS_DIR / "s87_w7_ic_per_class_verify.npz"  # (local)
    np.savez(
        npz_path,
        classes=np.array(classes, dtype=object),
        M_at_s_neg1=np.array([M_at_s_neg1[R] for R in classes], dtype=np.float64),
        xi_per_class=xi_values,
        xi_mean=xi_mean,
        xi_std=xi_std,
        sigma_xi_rel=sigma_xi_rel,
        delta_max=delta_max,
        delta_max_pair=np.array(delta_max_pair, dtype=object),
        delta_canonical=delta_canonical,
        likelihood_A=likelihood_A,
        likelihood_B=likelihood_B,
        posterior_A=posterior_A,
        posterior_B=posterior_B,
        prior_A=PRIOR_A,
        prior_B=PRIOR_B,
        xi_E_GGE_inv_canonical=xi_E_GGE_inv,
        L_max=L_MAX,
        s_slot=S_SLOT,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite=composite,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
        cc_zeta_residual=cc_zeta_residual,
        cc_sdw_residual=cc_sdw_residual,
    )
    print(f"[STEP I] Saved data: {npz_path}")

    # 5-bar plot
    png_path = THIS_DIR / "s87_w7_ic_per_class_verify.png"  # (local)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))  # (local)
    ax0 = axes[0]  # (local)
    bar_colors = ["#1f77b4", "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]  # (local) F_2 same color
    ax0.bar(range(len(classes)), xi_values, color=bar_colors)
    ax0.axhline(xi_E_GGE_inv, color="black", linestyle="--", linewidth=1.5,
                label=f"xi_E_GGE_inv canonical = {xi_E_GGE_inv:.6f}")
    ax0.set_xticks(range(len(classes)))
    ax0.set_xticklabels(classes, rotation=20)
    ax0.set_ylabel(r"$\xi_R(s=-1) = \xi_{E,GGE}^{-1} \cdot M_R/M_{F_2}$")
    ax0.set_title(f"S87-W5A-P3-IC-PER-CLASS-VERIFY (s={S_SLOT}, L_max={L_MAX})\n"
                  f"composite={composite}; delta_max={delta_max:.4e}; "
                  f"delta_canonical={delta_canonical:.4e}")
    ax0.legend(loc="best", fontsize=9)
    ax0.grid(axis="y", alpha=0.3)
    # Inset: posterior reallocation
    ax1 = axes[1]  # (local)
    bars = ax1.bar(["Track A\n(prior)", "Track A\n(posterior)",
                    "Track B\n(prior)", "Track B\n(posterior)"],
                   [PRIOR_A, posterior_A, PRIOR_B, posterior_B],
                   color=["#aec7e8", "#1f77b4", "#ffbb78", "#ff7f0e"])
    for bar, val in zip(bars, [PRIOR_A, posterior_A, PRIOR_B, posterior_B]):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                 f"{val:.4f}", ha="center", fontsize=9)
    ax1.set_ylim(0, 1.05)
    ax1.set_ylabel("Probability")
    ax1.set_title(f"Dual-prior posterior allocation\n"
                  f"(likelihood_A={likelihood_A:.2e}; likelihood_B={likelihood_B:.2e})")
    ax1.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(png_path, dpi=120)
    plt.close(fig)
    print(f"[STEP I] Saved plot: {png_path}")
    print()

    # -----------------------------------------------------------------------
    # Step J — Append verdict line to s87_gate_verdicts.txt
    # -----------------------------------------------------------------------
    verdict_path = THIS_DIR / "s87_gate_verdicts.txt"  # (local)
    canonical_line = (
        f"{GATE_ID}: {composite} -- value={delta_max:.6e} "
        f"scheme={SCHEME_TAG} convention={CONVENTION_TAG} "
        f"L_max={L_MAX} audit_sha256={audit_sha256} "
        f"content_sha256={content_sha256} schema_version={SCHEMA_VERSION}\n"
    )  # (local)
    companion_dual_sha = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    companion_3tuple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    companion_posterior = (
        f"# posterior_A={posterior_A:.6e} posterior_B={posterior_B:.6e} "
        f"# {GATE_ID} dual-prior allocation\n"
    )  # (local)
    with open(verdict_path, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(companion_dual_sha)
        fh.write(companion_3tuple)
        fh.write(companion_posterior)
    print(f"[STEP J] Appended verdict line + 3 companion rows to: {verdict_path}")
    print()
    print("Final 4-tuple:")
    print(f"  (value={delta_max:.6e}, scheme={SCHEME_TAG}, "
          f"convention={CONVENTION_TAG}, L_max={L_MAX})")
    print()
    print(f"Composite verdict: {composite}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
