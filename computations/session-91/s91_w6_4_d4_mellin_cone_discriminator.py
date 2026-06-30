#!/usr/bin/env python3
"""
S91 W6-4: S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR (M10 / CF-LZ-S7-1)
=================================================================================

Gate: S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR ([VERIFY-THEOREM])

PRIMARY:   lizzi-spectral-functional-theorist
CO-AUTHOR: connes-ncg-theorist (Connes-Moscovici 1995 §III.4 residue-formula
           evaluator on multi-projector / multi-pole independent observables;
           NCG-axiomatic shell-sum derivation)

Method
------
4-way d=4 universal envelope discriminator via shell-sum log-log regression
on L ∈ {4..11} from L_max=12 master cache `s84_spectrum_cache_L12_tau019.npz`.

Bypasses BOTH the in-cache truncation residual route (which dominated CF-54's
FAIL) AND the c_sub_corrected anti-symmetry route (which dominated CF-65's
FAIL) by computing shell-sum series S_i(L) at each L from the cache, then
extracting α directly via log-log slope of log S_i(L) vs log L over the
gate window.

MNEMONIC-VS-EXACT DEVIATION (math-scripts.md §"Mnemonic-vs-exact ratio
discipline" RULE-3; honest disclosure per OPERATIONAL DEVIATION protocol):

The plan §10 Step 2 substitution chain pre-registers the EXACT form:
    S(L+1)/S(L) ~ ((L+1)/L)^{-β}     [for L on power-law decay]
                = (1 + 1/L)^{-β}
                ≈ 1 − β · (1/L) + O(L^{-2})  [Taylor expansion for large L]
The plan §6 implementation snippet truncated at O(L^{-1}) ("Linear fit
of (ratio − 1) vs (-1/L) gives slope = β"). At the gate window L ∈ [4,
11], the O(L^{-2}) correction `+β(β+1)/(2L^2)` is comparable to the
leading term at L=4 (e.g. for β=2: O(L^{-2}) term ≈ 4·5/(2·16) ≈ 0.625,
vs leading β/L = 0.5). On the analytically-computable O_1 shell sum,
the mnemonic Taylor-truncated regression yields β=0.79 while the
STRUCTURALLY-EXACT extraction (matching CF-54 + CF-65 + W6-3 precedent)
yields α=1.55; mnemonic-vs-exact relative deviation ~96%, far exceeding
the math-scripts.md RULE-3 1% bound that mandates the exact form.

Per the discipline (and per the plan §10 Step 2's own pre-registered
EXACT form `((L+1)/L)^{-β}`), this script implements the STRUCTURALLY
EXACT regression:

    β_i := −slope( log(S_i(L+1)/S_i(L))  vs  log((L+1)/L) )
         over L ∈ {4..11}

which is the exact-form regression of the plan §10 Step 2 identity
without the O(L^{-2}) truncation. Equivalently: a log-log slope of
the shell-sum-ratio against its asymptotic-decay variable. This
preserves the plan-pinned SCHEME `shell-sum-ratio-regression-4-way-
discriminator` (it is still ratio regression; just with the EXACT
log-ratio form instead of the mnemonic Taylor linearization) and the
plan-pinned CONVENTION `Mellin-class-substrate-distance-1-pole-s3-
CACHE-PROJECTION` (the convention pin is at the substrate level, not
the regression-arithmetic level).

For O_1, this yields α ≈ 1.55 at L ∈ [4..11] (consistent with CF-65
log-log α=1.929 on L ∈ [6..11] given window-dependent boundary). The
verdict bands at [1.8, 2.1] / [1.5, 2.5] are applied to the exact-form
β as pre-registered.

This is NOT a PROHIBITED_ACTIONS Class 1 (convention-shopping) violation:
the convention pin is unchanged; the SCHEME pin is unchanged; only the
implementation of the regression-arithmetic moves from the Taylor mnemonic
(plan §6 snippet) to the exact form (plan §10 substitution chain Step 2).
Audit-trail disclosure: full math comparison in the WORKING-PAPER
§W6-4 Methodology subsection.

Observables (4 structurally independent d=4 substrate-distance-1 pole s=3
observables on the substrate's KO-dim=6 finite spectral triple per lizzi-S7
synthesis §(4.c) Table 1):

  O_1 = M^(ζ)_3:          full Mellin-cone trace, all (p,q) at level L
                          contribute dim(p,q)·(C_2(p,q)+1)^{-3}
                          [no projector, no bridge; Level-2-non-binding]

  O_2 = R_universal_FWD_C1: P_0 band-0 projector + HKR L→∞;
                          band-0 = lowest-Casimir sector per level L,
                          contributes (C_2_min(L)+1)^{-3} weighted by its dim
                          [Level-2-binding via HKR bridge to Pillar II n_s]

  O_3 = R_universal_FWD_C2 candidate: P_BdG projector at substrate-distance-2
                          pole s=4; P_BdG = Cartan-diagonal (p=q) sectors
                          which contain the substrate's BdG 2x2 image
                          (M_2(C) sub-algebra carrier);
                          [deferred-pending PROXY-REFINEMENT per §VII.AV]

  O_4 = Tr(D_K^{-6}):     pure spectral moment; for each (p,q) at level L
                          contributes Σ |λ|^{-6} over the cached |λ|
                          [algebra-INVARIANT; no Hochschild structure]

OPERATIONAL DEVIATION (honest disclosure per math-scripts.md §"D_K
Block-Diagonality Pre-Check" plan-authorship discipline):

  - The plan §6 snippet at line 802 reads `if (p, q) == (0, 0)` for O_2.
    That literal selector contributes zero for L ≥ 1 (since (0,0) only
    inhabits L=0), making the shell-sum-ratio regression structurally
    degenerate. The substrate-IS interpretation of "P_0 band-0 projector"
    in CF-65 / FWD-C1 context is the projector that selects band-0 ≡ the
    lowest-Casimir Peter-Weyl sector at each level L. We implement this
    substrate-IS reading: at each L, P_0 selects argmin_{(p,q): p+q=L} C_2(p,q).
  - The plan §6 snippet at line 805 invokes `is_bdg_sector(p, q)` undefined.
    The substrate-IS BdG image at M_2(C) sub-algebra selects (p,q) sectors
    carrying the 2-dim substrate Bogoliubov pair structure under SU(3) ⊃
    SO(3)_isospin; the algebra-clean Cartan-diagonal proxy is p == q.
    We implement P_BdG := {(p,q) : p == q AND p+q == L} at each L.
  - Both deviations preserve the gate's substrate-IS structural intent:
    O_2 still tests the band-0 projector + HKR pathway; O_3 still tests
    the BdG / Cartan-symmetric projector + substrate-distance-2 pole
    pathway. The Reading B vs Reading A discriminator is unchanged.

Pre-registered PASS / FAIL / INFO thresholds (plan §9, lizzi-S7 §(4.d)):

  PASS (Reading B substrate-structural confirmed):
    ALL 4 observables: β_i ∈ [1.8, 2.1]
    AND σ_β ≤ 0.10
    AND min(C_ij off-diagonal) ≥ 0.7

  FAIL (Reading A coincidence confirmed):
    ≥ 2 of 4 observables with β_i outside [1.5, 2.5]
    AND σ_β ≥ 0.30

  INFO: between PASS and FAIL bands (σ_β ∈ (0.10, 0.30); intermediate)

Substitution chain (plan §10, MANDATORY for [VERIFY-THEOREM]):

  Definitions:
    S_i(L)    := shell-sum of observable i at Peter-Weyl level L
    β_i       := −slope of linear regression of S_i(L+1)/S_i(L) vs 1/L over L ∈ {4..11}
    β̄         := mean(β_1..β_4)
    σ_β       := sample-std(β_1..β_4) (ddof=1)
    C_ij      := corr(β_i residual_series, β_j residual_series)

  Step 1: shell-sum at substrate-distance-1 pole s=3 (s=4 for O_3):
            contribution_i(p,q) = projector_i(p,q) · dim(p,q) · (C_2(p,q)+1)^{-s_i}
          [Substrate's combinatorial geometry; regulator-INVARIANT BY CONSTRUCTION per EV3]

  Step 2: Asymptotic ratio at large L:
            S(L+1)/S(L) ~ ((L+1)/L)^{-β} = (1+1/L)^{-β} ≈ 1 − β/L + O(L^{-2})

  Step 3: Linear regression on L ∈ {4..11} (eight points; avoids L=2,3
          too-small AND L=12 cache-ceiling):
            ratio_minus_1 vs (1/L); slope = −β_i

  Step 4: Reading B PREDICTION: all β_i in tight band ≈ 1.9; σ_β ≤ 0.10; C_ij ≥ 0.7
  Step 5: Reading A PREDICTION: ≥ 2 of 4 outside [1.5, 2.5]; σ_β ≥ 0.30

  Direction: PASS = "all 4 observables agree at universal β"; FAIL = "scatter".
  Conclusion: substrate-IS combinatorial geometry produces universal exponent
              (Reading B) OR observable-specific contingencies break universality
              (Reading A). Verdict is direct test of the EV1/EV3 boxed theorem.

Substrate framing
-----------------
The 4 observables ARE 4 substrate-IS projections of the substrate's
combinatorial shell-sum geometry. There is no enveloping 4-way space
they inhabit; the discriminator IS a substrate-spectral-functional test
of d=4 universality at substrate-distance-1 pole s=3.

Connes-Moscovici 1995 §III.4 anchor (connes-ncg-theorist CO-AUTHOR):
The shell-sum-ratio extraction realizes the residue-formula evaluator
on multi-projector / multi-pole observables. CM-1995 §III.4 gives the
dimension-spectrum residue at s=d-k for the noncommutative-spectral-triple
heat kernel; for d=4 and substrate-distance-1 (k=1), the residue at s=3
governs the L^{-β} envelope through the (C_2+1)^{-3} shell weighting.
The 4-way discriminator probes whether the residue is universal across
{bare-trace, P_0-projected + HKR-bridged, P_BdG-projected, pure spectral
moment} observables — a direct NCG-axiomatic universality test.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
sys.path.insert(0, str(ROOT / "computations"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    gv_canonical_difference_FW,
    n_s_FW_exact,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# ============================ Gate-block constants ============================
GATE_ID = "S91-D4-MELLIN-CONE-UNIVERSAL-ENVELOPE-DISCRIMINATOR"
SCHEME = "shell-sum-ratio-regression-4-way-discriminator"
CONVENTION = "Mellin-class-substrate-distance-1-pole-s3-CACHE-PROJECTION"
L_MAX_TAG = 12  # (local) gate-pre-registered L_max output tag per plan §6 line 876
PROJECT_ROOT = ROOT
SHARED_DIR = ROOT / "computations" / "_shared"
SESSION_91_DIR = ROOT / "computations" / "session-91"
SESSION_84_DIR = ROOT / "computations" / "session-84"
SESSION_90_DIR = ROOT / "sessions" / "session-90"
VERDICT_TXT = SESSION_91_DIR / "s91_gate_verdicts.txt"
OUT_NPZ = SESSION_91_DIR / "s91_w6_4_d4_mellin_cone_discriminator.npz"
OUT_PNG = SESSION_91_DIR / "s91_w6_4_d4_mellin_cone_discriminator.png"

# Pre-registered PASS / FAIL / INFO thresholds (plan §9; lizzi-S7 §(4.d))
PASS_BAND_BETA_LOW = 1.8       # (local)
PASS_BAND_BETA_HIGH = 2.1      # (local)
PASS_SIGMA_BETA_MAX = 0.10     # (local)
PASS_CIJ_MIN_OFF_DIAG = 0.7    # (local)

# Option A supersedes-tag protocol (gate-verdicts.md §"Option A — sig_5
# remediation pathway"). The script was iterated three times during
# development: original emission (NaN propagation from O_3 cache-zero
# divides) at audit_sha=0da7e7205a38016f7e60fe97565bac4c959537e3b7f7e854229a473f483dfc02,
# intermediate emission (exact log-ratio regression but still NaN from O_3
# cache-coverage) at audit_sha=3bf5b89209f065aeba3786961b0a22c58e5ef7118bce02958005cf6afa290346,
# corrective substantive emission (combinatorial-form O_1/O_2/O_3) at
# audit_sha=914e52092f1a2a8c738e136e4f02db92548f25eb93101365f6c3405086b6c65b.
# The latest substantive emission is canonical per Option A "latest non-
# superseded line"; the FINAL emission below carries supersedes pointing
# at the prior 3 canonical lines for forward audit-trail clarity.
SUPERSEDES_AUDIT_SHAS = [
    "0da7e7205a38016f7e60fe97565bac4c959537e3b7f7e854229a473f483dfc02",
    "3bf5b89209f065aeba3786961b0a22c58e5ef7118bce02958005cf6afa290346",
    "914e52092f1a2a8c738e136e4f02db92548f25eb93101365f6c3405086b6c65b",
]  # (local) — prior canonical lines for the gate, retained on disk per Option A

FAIL_BAND_BETA_LOW = 1.5       # (local)
FAIL_BAND_BETA_HIGH = 2.5      # (local)
FAIL_COUNT_THRESHOLD = 2       # (local) >= 2 of 4 outside [1.5, 2.5]
FAIL_SIGMA_BETA_MIN = 0.30     # (local)

# Pinned input files (per plan §7 Input SHA-256 pins; runtime-pinned)
INPUT_FILES = [
    SESSION_84_DIR / "s84_spectrum_cache_L12_tau019.npz",
    SHARED_DIR / "canonical_constants.py",
    SESSION_90_DIR / "session-90-lizzi-s7-d4-envelope-synthesis.md",
    SESSION_90_DIR / "workshops" / "s90-w6-d4-envelope-identity.md",
    ROOT / "sessions" / "permanent-results-registry.md",
]


# ============================ SHA helpers ============================
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha = SHA(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha = SHA(script_bytes)."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


# ============================ SU(3) representation helpers ============================
def peter_weyl_dim(p: int, q: int) -> int:
    """SU(3) irrep dimension formula: dim(p,q) = (p+1)(q+1)(p+q+2)/2.
    Verified against cache 'dim' field for (0,0)..(0,12), (1,0), (1,1)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def su3_casimir_quadratic(p: int, q: int) -> float:
    """SU(3) quadratic Casimir: C_2(p,q) = (1/3)(p^2 + q^2 + p·q + 3p + 3q)."""
    return (1.0 / 3.0) * (p * p + q * q + p * q + 3 * p + 3 * q)


# ============================ Shell-sum evaluators ============================
def shell_sum_O1(sector_evals: dict, L: int) -> float:
    """O_1 = M^(ζ)_3: full Mellin trace at level L, substrate-distance-1 pole s=3.
       S_1(L) = Σ_{p+q=L} dim(p,q) · (C_2(p,q) + 1)^{-3}.

       SUBSTRATE-IS COMBINATORIAL FORM: this observable is defined directly
       on the SU(3) representation theory (no eigenvalue lookup required).
       We enumerate ALL (p,q) with p+q=L using the analytic combinatorial
       formula, NOT cache.keys() — the cache may have coverage gaps
       (e.g., (4,4) missing at L=8 in s84_spectrum_cache_L12_tau019.npz)
       but the substrate-IS shell sum IS algebra-canonical per plan §10
       Step 1: 'For each (p,q) Peter-Weyl block with p+q = L: contribution
       = projector · dim · (C_2+1)^{-s}'. The cache is consulted ONLY for
       coverage diagnostic; the value is computed combinatorially."""
    S = 0.0  # (local)
    for p in range(L + 1):
        q = L - p
        dim_pq = peter_weyl_dim(p, q)  # (local) algebra dim
        C2 = su3_casimir_quadratic(p, q)  # (local)
        S += float(dim_pq) * (C2 + 1.0) ** (-3.0)
    return S


def shell_sum_O2(sector_evals: dict, L: int) -> float:
    """O_2 = R_universal_FWD_C1 with P_0 band-0 + HKR L→∞.

       P_0 selects the lowest-Casimir (p,q) sector at each L
       (band-0 ≡ lowest C_2; substrate-IS minimal-Casimir image of P_0).
       S_2(L) = dim(p*,q*) · (C_2(p*,q*) + 1)^{-3}
       where (p*,q*) = argmin_{p+q=L} C_2(p,q).

       SUBSTRATE-IS COMBINATORIAL FORM: enumerate ALL (p,q) with p+q=L
       analytically (NOT from cache.keys()); for L=8 the lowest-Casimir
       sector is (4,4) with C_2=24 — even though this sector is missing
       from the L_max=12 cache, the substrate-IS projector P_0 selects
       it on the substrate algebra by construction."""
    candidates = []  # (local)
    for p in range(L + 1):
        q = L - p
        candidates.append((su3_casimir_quadratic(p, q), p, q))
    if not candidates:
        return 0.0
    C2_min, p_star, q_star = min(candidates, key=lambda x: x[0])  # (local)
    dim_star = peter_weyl_dim(p_star, q_star)  # (local)
    return float(dim_star) * (C2_min + 1.0) ** (-3.0)


def shell_sum_O3(sector_evals: dict, L: int) -> float:
    """O_3 = R_universal_FWD_C2 candidate with P_BdG at substrate-distance-2 pole s=4.

       P_BdG selects Cartan-diagonal (p=q) sectors at level L
       (substrate-IS BdG carrier under SU(3) ⊃ SO(3)_isospin restriction;
       Cartan-diagonal is the algebra-clean substrate-IS BdG proxy at
       finite L).

       S_3(L) = dim(p,p) · (C_2(p,p) + 1)^{-4}  for L=2p (even)
              = 0                               for L odd

       SUBSTRATE-IS COMBINATORIAL FORM: cache-independent; the Cartan-
       diagonal sector (p,p) at L=2p is substrate-IS defined even if
       missing from the L_max=12 cache (e.g., (4,4) at L=8). The
       substrate algebra carries the (p,p) Peter-Weyl block independent
       of cache coverage."""
    S = 0.0  # (local)
    if L % 2 != 0:
        return 0.0
    p_card = L // 2  # (local)
    dim_pq = peter_weyl_dim(p_card, p_card)  # (local)
    C2 = su3_casimir_quadratic(p_card, p_card)  # (local)
    S = float(dim_pq) * (C2 + 1.0) ** (-4.0)
    return S


def shell_sum_O4(sector_evals: dict, L: int) -> float:
    """O_4 = Tr(D_K^{-6}): pure spectral moment at level L.
       S_4(L) = Σ_{p+q=L} Σ_a |λ_a^{(p,q)}|^{-6}
       summing over ALL cached |λ| in each (p,q) sector with p+q=L.
       algebra-INVARIANT; no Hochschild structure; no projector."""
    S = 0.0  # (local)
    for (p, q), entry in sector_evals.items():
        if p + q != L:
            continue
        abs_evals = entry["abs_evals"]  # (local)
        S += float(np.sum(abs_evals.astype(np.float64) ** (-6.0)))
    return S


# ============================ Section 5 — Compute ============================
def compute() -> dict:
    # ---------------------------------------------------------------------------
    # Step 0: load L_max=12 master cache (sector_evals dict by (p,q))
    # ---------------------------------------------------------------------------
    cache_path = SESSION_84_DIR / "s84_spectrum_cache_L12_tau019.npz"
    cache_data = np.load(cache_path, allow_pickle=True)
    sector_evals = cache_data["sector_evals"].item()  # (local)
    n_sectors = len(sector_evals)  # (local)
    print(f"\n>> Loaded L_max=12 master cache: {n_sectors} Peter-Weyl sectors")
    print(f">> tau_fold pin = {tau_fold:.6f}; M_KK pin = {M_KK:.6e} GeV")

    # ---------------------------------------------------------------------------
    # Step 1: compute shell sums S_i(L) for L ∈ {2..12} for each of 4 observables
    # (plan §6 line 814 + lizzi-S7 §(4.c) Step 2)
    # ---------------------------------------------------------------------------
    L_full = list(range(2, 13))  # (local) — L = 2..12 inclusive
    shell_sums: dict[str, np.ndarray] = {}  # (local)
    print("\n>> Computing shell sums S_i(L) for L ∈ {2..12}:")
    for O, sum_fn in [("O_1", shell_sum_O1),
                      ("O_2", shell_sum_O2),
                      ("O_3", shell_sum_O3),
                      ("O_4", shell_sum_O4)]:
        S_vals = np.array([sum_fn(sector_evals, L) for L in L_full], dtype=np.float64)
        shell_sums[O] = S_vals
        snippet = ", ".join(f"S({L})={v:.4e}" for L, v in zip(L_full, S_vals))
        print(f"  {O}: {snippet}")

    # ---------------------------------------------------------------------------
    # Step 2: EXACT-FORM log-ratio regression (mnemonic-vs-exact discipline)
    # The plan §10 Step 2 substitution chain pre-registers the EXACT identity:
    #   S(L+1)/S(L) ~ ((L+1)/L)^{-β}     ⇔   log(ratio) = -β · log((L+1)/L)
    # The plan §6 snippet implements the Taylor-truncated mnemonic form
    #   (ratio - 1) vs (1/L) with slope = -β + O(L^{-2}); the O(L^{-2})
    # correction is comparable to the leading term at L ∈ [4..11].
    # We implement the EXACT log-ratio regression per math-scripts.md
    # §"Mnemonic-vs-exact ratio discipline" RULE-3 (>1% deviation mandate);
    # convention pin unchanged; this is regression-arithmetic-only.
    #
    # For O_3 (Cartan-diagonal p=q non-zero only at even L), we use the
    # even-L subgrid {4, 6, 8, 10} with step Δ=2:
    #   S(L+2)/S(L) = ((L+2)/L)^{-β}  ⇔  log(ratio) = -β · log((L+2)/L)
    # ---------------------------------------------------------------------------
    L_fit = np.arange(4, 12, dtype=np.int64)  # (local) — 4..11 inclusive (8 pts)
    log_step_standard = np.log(
        (L_fit.astype(np.float64) + 1.0) / L_fit.astype(np.float64)
    )  # (local) — log((L+1)/L) per fit point

    beta: dict[str, float] = {}  # (local)
    intercepts: dict[str, float] = {}  # (local)
    ratios: dict[str, np.ndarray] = {}  # (local)
    log_ratios: dict[str, np.ndarray] = {}  # (local)
    log_step_used: dict[str, np.ndarray] = {}  # (local) — log((L+Δ)/L) per fit
    L_fit_used: dict[str, np.ndarray] = {}  # (local) — per-observable fit L grid
    residuals_dict: dict[str, np.ndarray] = {}  # (local) — log-domain residuals

    print("\n>> Step 2: EXACT log-ratio regression "
          "(log(S(L+Δ)/S(L)) vs log((L+Δ)/L); slope = -β):")
    for O in ["O_1", "O_2", "O_3", "O_4"]:
        S = shell_sums[O]  # (local)
        if O == "O_3":
            # Even-L subgrid: step Δ=2 in L ∈ {4, 6, 8, 10}
            L_even = np.array([4, 6, 8, 10], dtype=np.int64)  # (local)
            idx = L_even - 2  # (local) — index in shell_sums (L_full starts at 2)
            S_at = S[idx]  # (local) S(4), S(6), S(8), S(10)
            S_next = S[idx + 2]  # (local) S(6), S(8), S(10), S(12)
            # Guard against zero / negative
            if np.any(S_at <= 0) or np.any(S_next <= 0):
                beta[O] = float("nan")
                intercepts[O] = float("nan")
                ratios[O] = (S_next / np.where(S_at > 0, S_at, np.nan))
                log_ratios[O] = np.full_like(L_even, np.nan, dtype=np.float64)
                log_step_used[O] = np.log(
                    (L_even.astype(np.float64) + 2.0) / L_even.astype(np.float64))
                L_fit_used[O] = L_even
                residuals_dict[O] = np.full_like(L_even, np.nan, dtype=np.float64)
                print(f"  {O}: even-L subgrid {L_even.tolist()}; "
                      f"NaN propagation (zero shell sum present)")
                continue
            ratio = (S_next / S_at).astype(np.float64)  # (local)
            log_r = np.log(ratio)  # (local) — log of S(L+2)/S(L)
            log_step = np.log(
                (L_even.astype(np.float64) + 2.0) / L_even.astype(np.float64)
            )  # (local) — log((L+2)/L)
            # Exact identity: log_r = -β · log_step + intercept_term
            # Pre-registered structural form has intercept = 0 in the strict
            # power-law limit; we fit with intercept (free) and report both
            # slope and intercept for diagnostic.
            slope, intercept = np.polyfit(log_step, log_r, 1)
            beta[O] = -float(slope)
            intercepts[O] = float(intercept)
            ratios[O] = ratio
            log_ratios[O] = log_r
            log_step_used[O] = log_step
            L_fit_used[O] = L_even
            pred = -beta[O] * log_step + intercepts[O]  # (local)
            residuals_dict[O] = (log_r - pred).astype(np.float64)
            print(f"  {O}: even-L subgrid {L_even.tolist()}; "
                  f"β={beta[O]:.6f}, intercept_log={intercepts[O]:.6e}, "
                  f"ratios={[f'{r:.6f}' for r in ratio]}")
        else:
            # Standard path: L_fit = 4..11; ratio[L] = S(L+1)/S(L)
            idx = L_fit - 2  # (local)
            S_at = S[idx]  # (local)
            S_next = S[idx + 1]  # (local)
            if np.any(S_at <= 0) or np.any(S_next <= 0):
                beta[O] = float("nan")
                intercepts[O] = float("nan")
                ratios[O] = (S_next / np.where(S_at > 0, S_at, np.nan))
                log_ratios[O] = np.full(len(L_fit), np.nan, dtype=np.float64)
                log_step_used[O] = log_step_standard.copy()
                L_fit_used[O] = L_fit
                residuals_dict[O] = np.full(len(L_fit), np.nan, dtype=np.float64)
                print(f"  {O}: L_fit={L_fit.tolist()}; "
                      f"NaN propagation (zero shell sum present)")
                continue
            ratio = (S_next / S_at).astype(np.float64)  # (local)
            log_r = np.log(ratio)  # (local)
            log_step = log_step_standard  # (local) — log((L+1)/L)
            slope, intercept = np.polyfit(log_step, log_r, 1)
            beta[O] = -float(slope)
            intercepts[O] = float(intercept)
            ratios[O] = ratio
            log_ratios[O] = log_r
            log_step_used[O] = log_step
            L_fit_used[O] = L_fit
            pred = -beta[O] * log_step + intercepts[O]  # (local)
            residuals_dict[O] = (log_r - pred).astype(np.float64)
            print(f"  {O}: L_fit={L_fit.tolist()}; "
                  f"β={beta[O]:.6f}, intercept_log={intercepts[O]:.6e}")

    # ---------------------------------------------------------------------------
    # Step 3: β̄, σ_β, 4-way cross-correlation matrix on per-L residuals
    # (NB: O_3 residuals on 4 even-L points; O_1/O_2/O_4 residuals on 8 points.
    # We compute C_ij on the COMMON even-L slice {4,6,8,10} where all 4
    # observables have residual values, for the rank correlation matrix.)
    # ---------------------------------------------------------------------------
    observables = ["O_1", "O_2", "O_3", "O_4"]  # (local)
    beta_values = np.array([beta[O] for O in observables], dtype=np.float64)
    beta_bar = float(beta_values.mean())  # (local)
    sigma_beta = float(beta_values.std(ddof=1))  # (local) sample std

    # Build common residual slice on even-L: residual at L=4, 6, 8, 10
    even_targets = [4, 6, 8, 10]  # (local)
    common_residuals: dict[str, np.ndarray] = {}  # (local)
    for O in observables:
        L_grid = L_fit_used[O].tolist()  # (local)
        res = residuals_dict[O]  # (local)
        slice_vals = np.array([res[L_grid.index(L)] for L in even_targets],
                              dtype=np.float64)
        common_residuals[O] = slice_vals

    C_matrix = np.eye(4, dtype=np.float64)  # (local) — start with identity
    for i, Oi in enumerate(observables):
        for j, Oj in enumerate(observables):
            if i == j:
                C_matrix[i, j] = 1.0
                continue
            ri = common_residuals[Oi]
            rj = common_residuals[Oj]
            # Guard against degenerate constant series (zero variance)
            if np.std(ri) < 1e-15 or np.std(rj) < 1e-15:
                C_matrix[i, j] = 0.0
            else:
                C_matrix[i, j] = float(np.corrcoef(ri, rj)[0, 1])

    off_diag_values = [C_matrix[i, j]
                       for i in range(4) for j in range(4) if i != j]  # (local)
    off_diag_min = float(np.min(off_diag_values))  # (local)
    off_diag_mean = float(np.mean(off_diag_values))  # (local)

    print(f"\n>> Step 3: β values + spread:")
    for O, b in zip(observables, beta_values):
        print(f"  β_{O} = {b:.6f}")
    print(f"  β̄ = {beta_bar:.6f}")
    print(f"  σ_β (sample std, ddof=1) = {sigma_beta:.6f}")
    print(f"  min(C_ij off-diagonal) = {off_diag_min:.6f}")
    print(f"  mean(C_ij off-diagonal) = {off_diag_mean:.6f}")

    # ---------------------------------------------------------------------------
    # Step 4: Verdict per plan §9 / lizzi-S7 §(4.d) bands
    # Verifier-rubric pre-registration (Class-8.2 MANDATORY):
    #   PASS_Reading_B iff (pass_band) ∧ (sigma_pass) ∧ (cij_pass)
    # all three criteria must hold (conjunction; not disjunction)
    # ---------------------------------------------------------------------------
    pass_band = all(PASS_BAND_BETA_LOW <= beta[O] <= PASS_BAND_BETA_HIGH
                    for O in observables)  # (local)
    sigma_pass = sigma_beta <= PASS_SIGMA_BETA_MAX  # (local)
    cij_pass = off_diag_min >= PASS_CIJ_MIN_OFF_DIAG  # (local)
    PASS_Reading_B = pass_band and sigma_pass and cij_pass  # (local)

    fail_count = sum(1 for O in observables
                     if not (FAIL_BAND_BETA_LOW <= beta[O] <= FAIL_BAND_BETA_HIGH))  # (local)
    sigma_fail = sigma_beta >= FAIL_SIGMA_BETA_MIN  # (local)
    FAIL_Reading_A = (fail_count >= FAIL_COUNT_THRESHOLD) and sigma_fail  # (local)

    print(f"\n>> Step 4: Pre-registered verdict bands (rubric: 3-criterion conjunction):")
    print(f"  pass_band  (all β_i in [{PASS_BAND_BETA_LOW},{PASS_BAND_BETA_HIGH}]) = {pass_band}")
    print(f"  sigma_pass (σ_β ≤ {PASS_SIGMA_BETA_MAX})                              = {sigma_pass}")
    print(f"  cij_pass   (min C_ij ≥ {PASS_CIJ_MIN_OFF_DIAG})                       = {cij_pass}")
    print(f"  PASS_Reading_B (conjunction)                                          = {PASS_Reading_B}")
    print(f"  fail_count (β_i outside [{FAIL_BAND_BETA_LOW},{FAIL_BAND_BETA_HIGH}]) = {fail_count}/4")
    print(f"  sigma_fail (σ_β ≥ {FAIL_SIGMA_BETA_MIN})                              = {sigma_fail}")
    print(f"  FAIL_Reading_A (≥{FAIL_COUNT_THRESHOLD} of 4 ∧ sigma_fail)            = {FAIL_Reading_A}")

    # ---------------------------------------------------------------------------
    # Composite verdict + 3-tuple annotation (S87 schema-v2 per plan §9):
    #   PASS:  sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID
    #   FAIL:  sign_verdict=FAIL, magnitude_verdict=FAIL, regime_verdict=VALID
    #   INFO:  sign_verdict=PASS/N-A, magnitude_verdict=INFO, regime_verdict=MARGINAL
    # ---------------------------------------------------------------------------
    if PASS_Reading_B:
        verdict = "PASS"
        band_tag = "PASS_Reading_B"
        sign_v, mag_v, regime_v = "PASS", "PASS", "VALID"
    elif FAIL_Reading_A:
        verdict = "FAIL"
        band_tag = "FAIL_Reading_A"
        sign_v, mag_v, regime_v = "FAIL", "FAIL", "VALID"
    else:
        verdict = "INFO"
        band_tag = "INFO_intermediate"
        # Direction read on β̄ — if β̄ in [1.5, 2.5] sign_verdict aligns with PASS direction
        sign_v = "PASS" if (FAIL_BAND_BETA_LOW <= beta_bar <= FAIL_BAND_BETA_HIGH) else "N/A"
        mag_v = "INFO"
        regime_v = "MARGINAL"

    print(f"\n>> Composite verdict: {verdict} ({band_tag})")
    print(f"  3-tuple: sign={sign_v}, magnitude={mag_v}, regime={regime_v}")

    return {
        "L_full": np.array(L_full, dtype=np.int64),
        "shell_sums": shell_sums,
        "L_fit": L_fit,
        "L_fit_used": L_fit_used,
        "ratios": ratios,
        "residuals_dict": residuals_dict,
        "common_residuals": common_residuals,
        "beta": beta,
        "intercepts": intercepts,
        "beta_values": beta_values,
        "beta_bar": beta_bar,
        "sigma_beta": sigma_beta,
        "C_matrix": C_matrix,
        "off_diag_min": off_diag_min,
        "off_diag_mean": off_diag_mean,
        "pass_band": pass_band,
        "sigma_pass": sigma_pass,
        "cij_pass": cij_pass,
        "PASS_Reading_B": PASS_Reading_B,
        "fail_count": fail_count,
        "sigma_fail": sigma_fail,
        "FAIL_Reading_A": FAIL_Reading_A,
        "verdict": verdict,
        "band_tag": band_tag,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
    }


# ============================ Section 6 — Plot ============================
def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14.0, 6.5), dpi=110)

    colors = {"O_1": "C0", "O_2": "C1", "O_3": "C2", "O_4": "C3"}
    labels = {
        "O_1": "O_1 = M^(ζ)_3 (Mellin trace, no projector)",
        "O_2": "O_2 = R_FWD_C1 (P_0 band-0 + HKR)",
        "O_3": "O_3 = R_FWD_C2 (P_BdG p=q, s=4 pole)",
        "O_4": "O_4 = Tr(D_K^{-6}) (pure spectral moment)",
    }

    # Left panel: log-log of S(L+1)/S(L) vs 1/L overlay across 4 observables
    for O in ["O_1", "O_2", "O_3", "O_4"]:
        L_grid = r["L_fit_used"][O]
        if O == "O_3":
            inv_L_axis = 2.0 / L_grid.astype(np.float64)
        else:
            inv_L_axis = 1.0 / L_grid.astype(np.float64)
        ratio = r["ratios"][O]
        beta_O = r["beta"][O]
        intercept_O = r["intercepts"][O]
        ax1.scatter(inv_L_axis, ratio - 1.0, s=68, color=colors[O], zorder=3,
                    label=f"{labels[O]}  β={beta_O:.4f}")
        # Best-fit line
        x_line = np.linspace(0.0, inv_L_axis.max() * 1.06, 50)
        y_line = -beta_O * x_line + intercept_O
        ax1.plot(x_line, y_line, "--", color=colors[O], lw=1.3, alpha=0.8)

    ax1.axhline(0.0, color="k", lw=0.6, alpha=0.55)
    ax1.set_xlabel("1/L  (O_3 uses 2/L on even-L subgrid)", fontsize=10.5)
    ax1.set_ylabel("S(L+1)/S(L) − 1  (or S(L+2)/S(L) − 1 for O_3)", fontsize=10.5)
    ax1.set_title(
        f"{GATE_ID}\n"
        f"shell-sum-ratio regression on L_max=12 cache; L_fit ∈ {{4..11}}\n"
        f"β̄ = {r['beta_bar']:.4f}, σ_β = {r['sigma_beta']:.4f}, "
        f"min(C_ij) = {r['off_diag_min']:.4f}; verdict = {r['verdict']} ({r['band_tag']})",
        fontsize=10,
    )
    ax1.legend(loc="upper left", fontsize=8.5, framealpha=0.92)
    ax1.grid(True, alpha=0.32)

    # Right panel: 4x4 cross-correlation matrix heatmap
    im = ax2.imshow(r["C_matrix"], cmap="RdBu_r", vmin=-1.0, vmax=1.0)
    ax2.set_xticks(range(4))
    ax2.set_yticks(range(4))
    obs_labels_short = ["O_1\n(Mellin)", "O_2\n(P_0+HKR)", "O_3\n(BdG s=4)", "O_4\n(Tr D^-6)"]
    ax2.set_xticklabels(obs_labels_short, fontsize=9)
    ax2.set_yticklabels(obs_labels_short, fontsize=9)
    for i in range(4):
        for j in range(4):
            val = r["C_matrix"][i, j]
            color = "white" if abs(val) > 0.5 else "black"
            ax2.text(j, i, f"{val:+.3f}", ha="center", va="center",
                     fontsize=10, color=color)
    ax2.set_title(
        f"4×4 cross-correlation matrix C_ij\n"
        f"on per-L residuals (common even-L slice L ∈ {{4,6,8,10}})\n"
        f"PASS criterion: min off-diagonal ≥ {PASS_CIJ_MIN_OFF_DIAG} "
        f"→ {'PASS' if r['cij_pass'] else 'FAIL'}",
        fontsize=10,
    )
    plt.colorbar(im, ax=ax2, fraction=0.046, pad=0.04, label="corr")

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110)
    plt.close(fig)
    print(f"\nplot written: {OUT_PNG}")


# ============================ Section 7 — Verdict emission ============================
def append_verdict(gate_id: str, verdict: str, value: str,
                   scheme: str, convention: str, L_max,
                   input_pin_map: dict,
                   schema_v2_annotation: dict,
                   script_path: Path, canonical_path: Path,
                   supersedes_shas: list[str] | None = None
                   ) -> tuple[str, str]:
    """Emit the canonical verdict line + dual-SHA companion comment row +
    schema-v2 3-tuple annotation companion row per
    `.claude/rules/gate-verdicts.md §"S87+ canonical form"` and
    Option A supersedes-chain protocol §"Option A — sig_5 remediation
    pathway under absolute verdict permanence".

    `supersedes_shas` is a list of FULL 64-char audit_sha256 values of
    prior canonical lines this emission supersedes; encoded into the
    value= field per Option A rule (2). Prior lines remain on disk per
    Option A rule (1) absolute verdict permanence."""
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, input_pin_map)

    # Option A supersedes encoding in value field
    if supersedes_shas:
        sup_field = "_".join(supersedes_shas)
        value_with_supersedes = f"{value};supersedes={sup_field}"
    else:
        value_with_supersedes = value

    canonical_line = (
        f"{gate_id}: {verdict} -- value='{value_with_supersedes}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_row = (
        f"# sign_verdict={schema_v2_annotation['sign_verdict']} "
        f"magnitude_verdict={schema_v2_annotation['magnitude_verdict']} "
        f"regime_verdict={schema_v2_annotation['regime_verdict']} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
        fp.write(three_tuple_row)
    print(f"\n=== verdict line emitted to {VERDICT_TXT} ===")
    print(canonical_line.rstrip())
    print(dual_sha_row.rstrip())
    print(three_tuple_row.rstrip())
    if supersedes_shas:
        print(f"  supersedes (Option A): {len(supersedes_shas)} prior canonical "
              f"line(s) at audit_sha256={[s[:16]+'...' for s in supersedes_shas]}")
    return audit_sha, content_sha


# ============================ Section 8 — main ============================
def main() -> int:
    pins = log_input_pins(INPUT_FILES)
    r = compute()
    make_plot(r)

    # ---------------------------------------------------------------------------
    # Save .npz per plan §6 lines 887-892
    # ---------------------------------------------------------------------------
    observables_list = ["O_1", "O_2", "O_3", "O_4"]
    save_dict = {
        "observables": np.array(observables_list),
        "beta_O1": np.array(r["beta"]["O_1"]),
        "beta_O2": np.array(r["beta"]["O_2"]),
        "beta_O3": np.array(r["beta"]["O_3"]),
        "beta_O4": np.array(r["beta"]["O_4"]),
        "beta_values_array": r["beta_values"],
        "beta_bar": np.array(r["beta_bar"]),
        "sigma_beta": np.array(r["sigma_beta"]),
        "C_matrix": r["C_matrix"],
        "off_diag_min": np.array(r["off_diag_min"]),
        "off_diag_mean": np.array(r["off_diag_mean"]),
        "pass_band": np.array(r["pass_band"]),
        "sigma_pass": np.array(r["sigma_pass"]),
        "cij_pass": np.array(r["cij_pass"]),
        "PASS_Reading_B": np.array(r["PASS_Reading_B"]),
        "fail_count": np.array(r["fail_count"]),
        "sigma_fail": np.array(r["sigma_fail"]),
        "FAIL_Reading_A": np.array(r["FAIL_Reading_A"]),
        "verdict": np.array(r["verdict"]),
        "band_tag": np.array(r["band_tag"]),
        "sign_verdict": np.array(r["sign_verdict"]),
        "magnitude_verdict": np.array(r["magnitude_verdict"]),
        "regime_verdict": np.array(r["regime_verdict"]),
        "L_full": r["L_full"],
        "L_fit": r["L_fit"],
        "shell_sums_O1": r["shell_sums"]["O_1"],
        "shell_sums_O2": r["shell_sums"]["O_2"],
        "shell_sums_O3": r["shell_sums"]["O_3"],
        "shell_sums_O4": r["shell_sums"]["O_4"],
        # diagnostic provenance
        "tau_fold": np.array(tau_fold),
        "M_KK": np.array(M_KK),
        "gv_canonical_difference_FW": np.array(gv_canonical_difference_FW),
        "n_s_FW_exact_str": np.array(str(n_s_FW_exact)),
    }
    np.savez(OUT_NPZ, **save_dict)
    print(f"npz written: {OUT_NPZ}")

    # ---------------------------------------------------------------------------
    # value field per plan §8 expected output 4-tuple
    # ---------------------------------------------------------------------------
    value_field = (
        f"beta_bar={r['beta_bar']:.4f}"
        f"_sigma_beta={r['sigma_beta']:.4f}"
        f"_Cij_min={r['off_diag_min']:.4f}"
        f"_{r['band_tag']};"
        f"beta_O1={r['beta']['O_1']:.4f}"
        f"_beta_O2={r['beta']['O_2']:.4f}"
        f"_beta_O3={r['beta']['O_3']:.4f}"
        f"_beta_O4={r['beta']['O_4']:.4f};"
        f"pass_band={int(r['pass_band'])}"
        f"_sigma_pass={int(r['sigma_pass'])}"
        f"_cij_pass={int(r['cij_pass'])};"
        f"fail_count={r['fail_count']}_sigma_fail={int(r['sigma_fail'])}"
    )

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md)
    tuple_str = (
        f"(value='{value_field[:90]}...', scheme={SCHEME}, "
        f"convention={CONVENTION[:60]}..., L_max={L_MAX_TAG})"
    )
    print(f"\n4-tuple: {tuple_str}")

    # Build input_pin_map for closure SHA computation
    input_pin_map = {rel: sha for rel, sha in pins.items()}
    input_pin_map["canonical_constants_M_KK"] = f"{M_KK:.18e}"
    input_pin_map["canonical_constants_tau_fold"] = f"{tau_fold:.18e}"
    input_pin_map["canonical_constants_gv_canonical_difference_FW"] = (
        f"{gv_canonical_difference_FW:.18e}")
    input_pin_map["canonical_constants_n_s_FW_exact_numerator"] = "9561"
    input_pin_map["canonical_constants_n_s_FW_exact_denominator"] = "10000"

    schema_v2_annotation = {
        "sign_verdict": r["sign_verdict"],
        "magnitude_verdict": r["magnitude_verdict"],
        "regime_verdict": r["regime_verdict"],
    }

    audit_sha, content_sha = append_verdict(
        gate_id=GATE_ID,
        verdict=r["verdict"],
        value=value_field,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX_TAG,
        input_pin_map=input_pin_map,
        schema_v2_annotation=schema_v2_annotation,
        script_path=Path(__file__),
        canonical_path=SHARED_DIR / "canonical_constants.py",
        supersedes_shas=SUPERSEDES_AUDIT_SHAS,
    )

    # ---------------------------------------------------------------------------
    # Diagnostic summary
    # ---------------------------------------------------------------------------
    print(f"\n=== {GATE_ID} summary ===")
    print(f"  observables (4):              O_1, O_2, O_3, O_4")
    print(f"  β_O_1 (Mellin trace):         {r['beta']['O_1']:.6f}")
    print(f"  β_O_2 (P_0 band-0 + HKR):     {r['beta']['O_2']:.6f}")
    print(f"  β_O_3 (P_BdG p=q, s=4):       {r['beta']['O_3']:.6f}")
    print(f"  β_O_4 (Tr(D^-6)):             {r['beta']['O_4']:.6f}")
    print(f"  β̄ (4-way mean):               {r['beta_bar']:.6f}")
    print(f"  σ_β (4-way sample std):       {r['sigma_beta']:.6f}")
    print(f"  min(C_ij off-diagonal):       {r['off_diag_min']:.6f}")
    print(f"  mean(C_ij off-diagonal):      {r['off_diag_mean']:.6f}")
    print(f"  pass_band ∧ sigma_pass ∧ cij_pass:  {r['PASS_Reading_B']}")
    print(f"  fail_count ≥ 2 ∧ σ_β ≥ 0.30:        {r['FAIL_Reading_A']}")
    print(f"  verdict:                              {r['verdict']}  ({r['band_tag']})")
    print(f"  3-tuple:        sign={r['sign_verdict']}  "
          f"mag={r['magnitude_verdict']}  regime={r['regime_verdict']}")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
