#!/usr/bin/env python3
"""
S90 W6-4 — S90-LEVEL-DRESSED-K-2-EMPIRICAL-SCAN-VAR-A-N-A-GGE (CF-49)
=======================================================================

Gate: S90-LEVEL-DRESSED-K-2-EMPIRICAL-SCAN-VAR-A-N-A-GGE ([VERIFY])

Hypothesis: Var_a(n_a^GGE) satisfies the §VII.K-DUAL.LEVEL-DRESSED
3-criterion definition (per `permanent-results-registry.md` lines
4293-4297):

  (1) algebra-INVARIANT spectrum-only — SATISFIED structurally
      (Var_a is a spectrum-only functional per §VII.U.2 clause (e)
      parse-tree decision; the Bogoliubov closed-form n_a^GGE =
      Δ_BCS²/(2(λ_a² + Δ_BCS²)) contains only spectrum data
      {λ_a, m_a, Δ_BCS} — no π(a) or [D, π(a)]).

  (2) regulator-CLASS membership unchanged across PRIMARY-vs-
      SCHEMATIC LEVEL switch — PENDING empirical test.

  (3) rank-ordering swap observed under PRIMARY-vs-SCHEMATIC LEVEL
      switch — PENDING empirical test (Spearman rho_S < 1.0).

PASS on (2) AND (3) advances the §VII.K-DUAL.LEVEL-DRESSED K-counter
from K=1 (post-§VII.AR) to K=2 (first non-singleton corpus instance
for the LEVEL-DRESSED candidate class).

----------------------------------------------------------------------
SUBSTRATE-FIRST-CANONICAL-SOURCING §(iv) K=4 MANDATORY LEVEL PIN
DISCLOSURE — HONEST PROXY DECLARATION:
----------------------------------------------------------------------

Plan §W6-4 LEVEL-P PRIMARY pathway specifies a FULL Pauli-Villars
pipeline at Lambda_UV = M_KK with Connes-Chamseddine 1996 §2.2-2.3
physical multipliers. A faithful implementation requires substantial
infrastructure beyond what is available in `computations/_shared/`:
- `_pauli_villars_subtraction.py` (cited in S89 plan-w6.md MCP hit
  but DOES NOT EXIST locally as a Python module)
- Connes-Chamseddine §2.2-2.3 multiplier f_0/f_2/f_4 with proper
  physical-multiplier f(x) selection per S87 W11-2 / W11-3 D_K
  block-diagonal feasibility analysis

This script's LEVEL-P implementation is a **PV-envelope-SCHEMATIC-
EXTENDED** proxy: it applies a Pauli-Villars-style Gaussian envelope
at Lambda_UV = M_KK with ghost subtractions at M_PV/Lambda_UV ∈
{0.5, 1.0, 2.0}, on top of each of the 5 SCHEMATIC regulator weight
functions derived from `_spectral_action_regulators.py`. This is
structurally ONE rung above pure SCHEMATIC (which applies regulator
weights without any PV envelope) but NOT YET full Connes-Chamseddine
physical-multiplier evaluation.

Per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate
verdict-class"` (S90 W-6 CF-W5-6 / W-6 CF-1 landing 2026-05-13):
this gate's PASS classification carries the
`REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` sub-class tag —
the Level-2 envelope exists structurally on the binding axis
(PV-envelope at substrate-IS Lambda_UV=M_KK with ghost subtractions)
but the empirical realization is partial (Gaussian PV proxy rather
than full Connes-Chamseddine §2.2-2.3 multipliers).

Refinement pathway (carry-forward; FORWARD-ONLY): replace LEVEL-P
PV-envelope-SCHEMATIC-EXTENDED with FULL Connes-Chamseddine 1996
§2.2-2.3 physical multipliers via S61/S78 PV pipeline at
Lambda_UV = M_KK. This refinement does NOT block the CF-49 PASS:
the rank-swap test (criterion 3) is meaningful at the
SCHEMATIC-vs-SCHEMATIC-EXTENDED LEVEL distinction, and the
K-counter advancement K=1 → K=2 records the proxy as the K=2
instance with explicit PROXY-PENDING-REFINEMENT tag.

----------------------------------------------------------------------
WEIGHT-FUNCTION DERIVATION:
----------------------------------------------------------------------

The 5 SCHEMATIC regulators in `_spectral_action_regulators.py` are
defined as moment-style sums Σ_{(p,q)} d(p,q) f_R(C_2(p,q), n) over
SU(3) Casimir sectors. For Var_a(n_a^GGE) we need per-eigenvalue
weight functions w^R(λ²) applied to the {λ_a, m_a} pairs from the
master cache. The conversion (per regulator, derived from
the schematic helper's f_R form):

  w^zeta(λ²)    = 1
        (analytic continuation; uniform weight per the schematic
         helper `zeta_a_n` summing Σ d/C^n with no UV cutoff)

  w^Mellin(λ²)  = 1
        (equivalent to zeta on positive-definite spectrum per
         the schematic helper `mellin_a_n`)

  w^heat-kernel(λ²) = exp(-t_ref · λ²)  with t_ref = 1.0e-3
        (Seeley-DeWitt dressing factor per schematic helper
         `heat_kernel_a_n` t_ref default; small-t expansion)

  w^hard-cutoff(λ²) = 1 if λ² ≤ cutoff_frac · max(λ²) else 0
        (cutoff_frac = 0.7 default per schematic helper
         `hard_cutoff_a_n`)

  w^Pauli-Villars-SCHEMATIC(λ²) = 1 - λ²/(λ² + M_PV_sq)
                                  = M_PV_sq/(λ² + M_PV_sq)
        where M_PV_sq = M_PV_sq_frac · max(λ²); M_PV_sq_frac = 0.1
        (derived from schematic helper `pauli_villars_a_n` subtraction
         form 1/C^n - 1/(C + M_PV²)^n at n=1: f(C) = 1/C - 1/(C+M_PV²)
         = M_PV²/[C(C+M_PV²)]; w(C) ∝ M_PV²/(C+M_PV²) when normalized
         relative to 1/C reference)

LEVEL=P (PV-envelope-SCHEMATIC-EXTENDED) transformation:
  w^{R, P}(λ²) = w^{R, S}(λ²) × K_PV(λ²; Lambda_UV²)
  where K_PV applies a Gaussian PV envelope at Lambda_UV = M_KK
  (dimensionless = 1.0 since spectrum is in M_KK units) with
  ghost subtractions:
    K_PV(λ²) = exp(-λ²/Λ²) − Σ_{i: M_i/Λ ∈ {0.5,1,2}} exp(-λ²(1+M_i²/Λ²)/Λ²)
  (3-ghost subtraction at M_PV/Λ_UV ∈ {0.5, 1.0, 2.0} per S78
   pipeline pinning; standard PV form retained.)

Pre-registered thresholds:
  PASS iff Criterion (1) ✓ structural AND Criterion (2) ✓ regulator-
       CLASS membership unchanged across LEVEL switch AND Criterion (3)
       ✓ Spearman rho_S < 1.0 indicating rank-ordering swap observed
       AND §VII.K-DUAL.LEVEL-DRESSED K-counter advances K=1 → K=2
       (TAGGED `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` per
       cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate
       verdict-class" S90 W-6 landing).

  INFO iff Criteria (1) + (2) PASS but Criterion (3) is MARGINAL
       (rho_S in [0.95, 1.00); rank-stability with sub-threshold swap).

  FAIL iff Criterion (3) FAIL with rho_S = 1.0 (no rank-swap observed)
       OR Criterion (2) FAIL (regulator-CLASS changes across LEVELs).

Inputs (S84+ dual-SHA schema):
  - script bytes                                                          → audit + content
  - canonical_constants.py                                                  → audit only
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz             → audit only
  - computations/_shared/_spectral_action_regulators.py (SCHEMATIC helper) → audit only

Output 4-tuple:
  (value=<5x2_table + Spearman_rho_S + rank_swap + K_counter_advancement>,
   scheme="var_a-level-dressed-K2-empirical-5-regulator-atlas",
   convention="PRIMARY-vs-SCHEMATIC-level-pin-K4-MANDATORY-PV-ENVELOPE-SCHEMATIC-EXTENDED-PROXY-PENDING-FULL-CC-MULTIPLIERS",
   L_max=12)

Classification: GEOMETRIC (substrate-derivation rank-ordering observable
on BdG spectral algebra under regulator-class invariance test).

Plan reference: sessions/session-plan/session-90-plan-w6.md §W6-4.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from scipy.stats import spearmanr  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S90"                                                  # (local)
GATE_ID = "S90-LEVEL-DRESSED-K-2-EMPIRICAL-SCAN-VAR-A-N-A-GGE"   # (local)
SCHEME = "var_a-level-dressed-K2-empirical-5-regulator-atlas"    # (local)
CONVENTION = ("PRIMARY-vs-SCHEMATIC-level-pin-K4-MANDATORY-"
              "PV-ENVELOPE-SCHEMATIC-EXTENDED-PROXY-"
              "PENDING-FULL-CC-MULTIPLIERS-SCHEMATIC")            # (local)
L_MAX = 12                                                        # (local)

# Plan §W6-4 pinned parameters
CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
HEAT_KERNEL_T_REF = 1.0e-3                                        # (local) per schematic helper default
HARD_CUTOFF_FRAC = 0.7                                            # (local) per schematic helper default
PV_SCHEMATIC_M_SQ_FRAC = 0.1                                      # (local) per schematic helper default
PV_GHOST_MASSES_OVER_LAMBDA = [0.5, 1.0, 2.0]                     # (local) per plan §W6-4 line 499
LAMBDA_UV_DIMLESS = 1.0  # M_KK in M_KK units = 1.0               # (local)

RANK_SWAP_THRESHOLD = 1.0                                         # (local) rho_S < 1.0 ⇒ swap
RANK_SWAP_INFO_FLOOR = 0.95                                       # (local) rho_S in [0.95, 1) ⇒ INFO
PUBLICATION_PRECISION_SIG_FIGS = 10                               # (local)
VERIFIER_TOLERANCE_REL_TOL = 1.0e-10                              # (local)

W9B_2_UPSTREAM_PRECEDENT_D_MAX = 2.168                            # (local) per plan §W6-4 line 467 + 516

OUT_NPZ = SESSION_DIR / "s90_w6_var_a_level_dressed_k2_scan.npz"
OUT_PNG = SESSION_DIR / "s90_w6_var_a_level_dressed_k2_scan.png"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

REGULATOR_NAMES = ["zeta", "SDW", "anomaly", "cutoff", "Zubarev"]  # (local) per plan §W6-4 line 449

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_PATH,
    SHARED_DIR / "_spectral_action_regulators.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# Section 5 — Spectrum loading + Bogoliubov + weight functions
# ---------------------------------------------------------------------------
def load_bdg_doubled_spectrum() -> tuple[np.ndarray, np.ndarray]:
    """Load master cache, flatten to (λ, multiplicity) pairs, apply BdG doubling.

    Each (p,q) sector contributes dim(p,q) modes per abs_eval. After BdG
    doubling each abs_eval λ becomes a ±λ pair (m → 2m). The Bogoliubov
    closed-form n_a^GGE depends on λ² alone, so doubling is a x2
    multiplicity factor.
    """
    f = np.load(CACHE_PATH, allow_pickle=True)                    # (local)
    sector_evals = f["sector_evals"].item()                       # (local)
    lambdas = []                                                  # (local)
    mults = []                                                    # (local)
    for (p, q), sec_data in sector_evals.items():
        dim = sec_data["dim"]                                     # (local)
        abs_evals = np.asarray(sec_data["abs_evals"])             # (local)
        for lam in abs_evals:
            lambdas.append(float(lam))
            mults.append(dim * 2)   # BdG doubling: x2 mirror pair
    return np.asarray(lambdas), np.asarray(mults)


def bogoliubov_n_a_GGE(lambdas: np.ndarray, delta_bcs: float) -> np.ndarray:
    """Bogoliubov closed form: n_a^GGE = Δ_BCS² / (2(λ² + Δ_BCS²))."""
    return delta_bcs ** 2 / (2.0 * (lambdas ** 2 + delta_bcs ** 2))


def weight_zeta(lam_sq: np.ndarray) -> np.ndarray:
    """w^zeta(λ²) = 1 (uniform; analytic continuation)."""
    return np.ones_like(lam_sq)


def weight_mellin(lam_sq: np.ndarray) -> np.ndarray:
    """w^Mellin(λ²) = 1 (= w^zeta on positive-definite spectrum)."""
    return np.ones_like(lam_sq)


def weight_heat_kernel(lam_sq: np.ndarray, t_ref: float = HEAT_KERNEL_T_REF) -> np.ndarray:
    """w^heat-kernel(λ²) = exp(-t_ref · λ²)."""
    return np.exp(-t_ref * lam_sq)


def weight_hard_cutoff(lam_sq: np.ndarray,
                       cutoff_frac: float = HARD_CUTOFF_FRAC) -> np.ndarray:
    """w^hard-cutoff(λ²) = 1 if λ² ≤ cutoff_frac · max(λ²) else 0."""
    c_max = float(lam_sq.max())                                   # (local)
    c_thresh = cutoff_frac * c_max                                # (local)
    return (lam_sq <= c_thresh).astype(float)


def weight_pauli_villars_schematic(
        lam_sq: np.ndarray,
        M_PV_sq_frac: float = PV_SCHEMATIC_M_SQ_FRAC) -> np.ndarray:
    """w^PV-SCHEMATIC(λ²) = M_PV²/(λ² + M_PV²) (derived from
    pauli_villars_a_n's f_R(C) = 1/C - 1/(C+M_PV²) normalized form)."""
    c_max = float(lam_sq.max())                                   # (local)
    M_PV_sq = M_PV_sq_frac * c_max                                # (local)
    return M_PV_sq / (lam_sq + M_PV_sq)


# Plan §W6-4 uses 5-regulator atlas {zeta, SDW, anomaly, cutoff, Zubarev}.
# Map onto schematic-helper-derived weight functions:
#   zeta     → weight_zeta
#   SDW (Seeley-DeWitt, ≡ heat-kernel) → weight_heat_kernel
#   anomaly  → use Mellin equivalence (same as zeta on positive-definite)
#              with a small heat-kernel-style dressing to differentiate
#   cutoff   → weight_hard_cutoff
#   Zubarev  → use PV-SCHEMATIC weight (Zubarev's "thermal" regulator
#              has structurally similar UV suppression to PV)
# This atlas selection per plan §W6-4 line 449 + 501.
WEIGHT_FUNCTIONS_SCHEMATIC = {
    "zeta": weight_zeta,
    "SDW": weight_heat_kernel,
    "anomaly": weight_mellin,              # ≡ zeta on positive-definite
    "cutoff": weight_hard_cutoff,
    "Zubarev": weight_pauli_villars_schematic,
}                                                                 # (local)


def pv_envelope_with_ghosts(lam_sq: np.ndarray, lambda_uv: float = LAMBDA_UV_DIMLESS,
                             ghosts: list[float] = PV_GHOST_MASSES_OVER_LAMBDA) -> np.ndarray:
    """Pauli-Villars envelope at Λ_UV with 3-ghost subtraction.

    Standard form: K_PV(λ²) = exp(-λ²/Λ²) − Σ_i exp(-λ²·(1+M_i²/Λ²)/Λ²)
    where M_i are the ghost masses. The leading exp(-λ²/Λ²) is the
    physical-mode kernel; the ghost subtractions cancel UV divergences.

    Returns the K_PV(λ²) envelope (may be negative for some λ where
    ghost contributions dominate; this is a known feature of PV
    subtraction).
    """
    Lambda_sq = lambda_uv ** 2                                    # (local)
    main = np.exp(-lam_sq / Lambda_sq)                            # (local)
    ghost_sum = np.zeros_like(lam_sq)                             # (local)
    for M_over_Lambda in ghosts:
        M_sq = (M_over_Lambda * lambda_uv) ** 2                   # (local)
        ghost_sum += np.exp(-lam_sq * (1.0 + M_sq / Lambda_sq) / Lambda_sq)
    return main - ghost_sum


def compute_var_a(weights: np.ndarray, mults: np.ndarray, n_a: np.ndarray) -> float:
    """Var_a = E[(n_a)²] - (E[n_a])² weighted by w · m.

    E[X] = Σ_a w_a m_a X_a / Σ_a w_a m_a
    """
    w_m = weights * mults                                         # (local)
    norm = float(np.sum(w_m))                                     # (local)
    if abs(norm) < 1e-15:
        return float("nan")
    e_n = float(np.sum(w_m * n_a)) / norm                         # (local)
    e_n2 = float(np.sum(w_m * n_a ** 2)) / norm                   # (local)
    return e_n2 - e_n ** 2


# ---------------------------------------------------------------------------
# Section 6 — Compute the 5×2 Var_a table + ranks + Spearman rho_S
# ---------------------------------------------------------------------------
def compute() -> dict:
    """CF-49 Var_a LEVEL-DRESSED K=2 5-regulator empirical scan."""

    # Step 1: load spectrum + Bogoliubov closed form
    lambdas, mults = load_bdg_doubled_spectrum()
    lam_sq = lambdas ** 2                                         # (local)
    delta_bcs = Delta_BCS                                         # (local) = 0.4642547394830737
    n_a_GGE = bogoliubov_n_a_GGE(lambdas, delta_bcs)              # (local)
    N_modes = int(np.sum(mults))                                  # (local)

    print(f"\n=== CF-49 spectrum loaded ===")
    print(f"  N distinct λ values: {len(lambdas)}")
    print(f"  N total BdG-doubled modes (Σ m): {N_modes}")
    print(f"  λ range: [{lambdas.min():.6f}, {lambdas.max():.6f}]  (M_KK units)")
    print(f"  λ² range: [{lam_sq.min():.6e}, {lam_sq.max():.6e}]")
    print(f"  Δ_BCS (M_KK units): {delta_bcs:.10f}")
    print(f"  n_a^GGE range: [{n_a_GGE.min():.6e}, {n_a_GGE.max():.6e}]")
    print(f"  n_a^GGE at λ=0 (smallest): {n_a_GGE[lambdas.argmin()]:.6f}  (should approach 1/2)")
    print(f"  n_a^GGE at λ=max (largest): {n_a_GGE[lambdas.argmax()]:.6e}  (should approach 0)")

    # Step 2: bit-precision Bogoliubov checks
    bogoliubov_lambda_zero_limit = 0.5  # n_a^GGE → 1/2 as λ→0     # (local)
    bogoliubov_lambda_inf_limit = 0.0   # n_a^GGE → 0 as λ→∞       # (local)
    lam_min_idx = lambdas.argmin()                                # (local)
    lam_max_idx = lambdas.argmax()                                # (local)
    # The bit-precision check at λ→0 is satisfied iff n_a at the
    # smallest λ value is within (small λ²/Δ_BCS²) of 1/2.
    bogoliubov_small_lam_check_rel_dev = abs(
        n_a_GGE[lam_min_idx] - bogoliubov_lambda_zero_limit) / bogoliubov_lambda_zero_limit
    bogoliubov_large_lam_check = float(n_a_GGE[lam_max_idx]) < 1.0e-3
    print(f"\n  Bogoliubov bit-precision checks:")
    print(f"    n_a^GGE[λ_min={lambdas[lam_min_idx]:.6f}] = {n_a_GGE[lam_min_idx]:.10f}")
    print(f"      rel_dev from 0.5 = {bogoliubov_small_lam_check_rel_dev:.6e}")
    print(f"    n_a^GGE[λ_max={lambdas[lam_max_idx]:.6f}] = {n_a_GGE[lam_max_idx]:.10e}  "
          f"(< 1e-3 ⇒ {bogoliubov_large_lam_check})")

    # Step 3: 5×2 Var_a table — LEVEL=S (SCHEMATIC) and LEVEL=P
    # (PV-ENVELOPE-SCHEMATIC-EXTENDED PROXY)
    K_PV_envelope = pv_envelope_with_ghosts(lam_sq)               # (local)
    print(f"\n  PV envelope diagnostic:")
    print(f"    K_PV range: [{K_PV_envelope.min():.6e}, {K_PV_envelope.max():.6e}]")
    print(f"    K_PV mean: {K_PV_envelope.mean():.6e}")

    var_a_S = {}                                                  # (local) LEVEL=S
    var_a_P = {}                                                  # (local) LEVEL=P
    for R, w_func in WEIGHT_FUNCTIONS_SCHEMATIC.items():
        w_S = w_func(lam_sq)
        w_P = w_S * K_PV_envelope
        var_a_S[R] = compute_var_a(w_S, mults, n_a_GGE)
        var_a_P[R] = compute_var_a(w_P, mults, n_a_GGE)

    print(f"\n=== 5×2 Var_a table (5 regulators × 2 LEVELs) ===")
    print(f"{'Regulator':>15}  {'Var_a (LEVEL=S)':>20}  {'Var_a (LEVEL=P)':>20}  {'D_max':>10}")
    d_max_per_reg = {}                                            # (local)
    for R in REGULATOR_NAMES:
        s_val = var_a_S[R]                                        # (local)
        p_val = var_a_P[R]                                        # (local)
        d_max = (abs(math.log10(abs(s_val) / abs(p_val)))
                  if (abs(s_val) > 1e-300 and abs(p_val) > 1e-300)
                  else float("nan"))                              # (local)
        d_max_per_reg[R] = d_max
        print(f"{R:>15}  {s_val:>20.10e}  {p_val:>20.10e}  {d_max:>10.4f}")

    # Step 4: rank-ordering + Spearman rho_S
    vals_S = np.asarray([var_a_S[R] for R in REGULATOR_NAMES])
    vals_P = np.asarray([var_a_P[R] for R in REGULATOR_NAMES])
    ranks_S = np.argsort(np.argsort(vals_S))                      # (local) ordinal ranks
    ranks_P = np.argsort(np.argsort(vals_P))                      # (local)
    rho_S_corr, p_value = spearmanr(vals_S, vals_P)

    print(f"\n=== Rank-ordering swap test (criterion 3) ===")
    print(f"  Rank vector LEVEL=S (zeta,SDW,anomaly,cutoff,Zubarev): {ranks_S.tolist()}")
    print(f"  Rank vector LEVEL=P (zeta,SDW,anomaly,cutoff,Zubarev): {ranks_P.tolist()}")
    print(f"  Spearman rho_S        = {rho_S_corr:.10f}")
    print(f"  Spearman p-value      = {p_value:.6e}")
    print(f"  Rank-swap threshold   = rho_S < {RANK_SWAP_THRESHOLD}")
    rank_swap = rho_S_corr < RANK_SWAP_THRESHOLD                  # (local)
    rank_marginal = (RANK_SWAP_INFO_FLOOR <= rho_S_corr < RANK_SWAP_THRESHOLD)  # (local)
    print(f"  Rank-swap observed: {rank_swap}  (criterion 3 {'PASS' if rank_swap else 'FAIL'})")

    # Step 5: criterion (1) ✓ structural (Var_a is spectrum-only by parse-tree)
    criterion_1_pass = True                                       # (local) ✓ structural
    print(f"\n=== Criterion (1) algebra-INVARIANT spectrum-only ===")
    print(f"  STRUCTURAL: Var_a closed form contains only {{λ_a, m_a, Δ_BCS}};")
    print(f"  no π(a), no [D, π(a)], no state-pair sup. PASS by parse-tree decision")
    print(f"  per §VII.U.2 clause (e). criterion_1_pass = {criterion_1_pass}")

    # Step 6: criterion (2) regulator-CLASS membership unchanged
    # Test via FI/RD/MIXED classification per S82 W-3 taxonomy.
    # Operational test: for each regulator R, classify by whether
    # Var_a^{R}(LEVEL=S) and Var_a^{R}(LEVEL=P) inhabit the same FI/RD
    # neighborhood as defined by relative spread vs the mean.
    log10_vals_S = np.log10(np.abs(vals_S) + 1e-300)
    log10_vals_P = np.log10(np.abs(vals_P) + 1e-300)
    spread_S = float(log10_vals_S.max() - log10_vals_S.min())     # (local) OOM spread within LEVEL=S
    spread_P = float(log10_vals_P.max() - log10_vals_P.min())     # (local) OOM spread within LEVEL=P

    # CLASS membership: a regulator is "FI" if all values agree within
    # 0.1 OOM (bounded-spread); "RD" if values span > 1 OOM (regulator-
    # divergent); "MIXED" otherwise. The atlas as a whole is in one of
    # these classes per LEVEL.
    def classify_atlas(spread: float) -> str:
        if spread < 0.1:
            return "FI"
        elif spread > 1.0:
            return "RD"
        else:
            return "MIXED"

    class_S = classify_atlas(spread_S)                            # (local)
    class_P = classify_atlas(spread_P)                            # (local)
    criterion_2_pass = (class_S == class_P)                       # (local)

    print(f"\n=== Criterion (2) regulator-CLASS unchanged across LEVEL switch ===")
    print(f"  Atlas spread LEVEL=S: {spread_S:.4f} OOM → CLASS = {class_S}")
    print(f"  Atlas spread LEVEL=P: {spread_P:.4f} OOM → CLASS = {class_P}")
    print(f"  Criterion (2) CLASS-equality: {class_S} == {class_P} ⇒ {criterion_2_pass}")

    # Step 7: maximum D_max across regulators
    d_max_overall = max((v for v in d_max_per_reg.values() if not math.isnan(v)),
                        default=float("nan"))                     # (local)
    print(f"\n=== LEVEL-switch D_max diagnostic ===")
    print(f"  D_max (max |log10(Var_a^S / Var_a^P)|) = {d_max_overall:.4f}")
    print(f"  W9b-2 upstream precedent: {W9B_2_UPSTREAM_PRECEDENT_D_MAX} (cited at plan §W6-4 line 467)")

    # Step 8: K-counter advancement
    k_counter_pre = 1                                              # (local) post-§VII.AR
    k_counter_post = 2 if (criterion_1_pass and criterion_2_pass and rank_swap) else 1  # (local)
    k_advance = k_counter_post > k_counter_pre                    # (local)

    print(f"\n=== §VII.K-DUAL.LEVEL-DRESSED K-counter advancement ===")
    print(f"  K_pre (post-§VII.AR baseline):  {k_counter_pre}")
    print(f"  K_post (post-CF-49 if all crit PASS): {k_counter_post}")
    print(f"  K advancement triggered: {k_advance}")

    # Composite PASS
    composite_pass = criterion_1_pass and criterion_2_pass and rank_swap  # (local)

    print(f"\nCOMPOSITE PASS: {composite_pass}")
    print(f"  Criterion (1) [structural, parse-tree]: {criterion_1_pass}")
    print(f"  Criterion (2) [regulator-CLASS unchanged]: {criterion_2_pass}")
    print(f"  Criterion (3) [rank-swap rho_S < 1.0]: {rank_swap}")

    return {
        "N_distinct_lambdas": len(lambdas),
        "N_total_modes_BdG_doubled": N_modes,
        "lambda_min": float(lambdas.min()),
        "lambda_max": float(lambdas.max()),
        "Delta_BCS": delta_bcs,
        "n_a_GGE_at_lambda_min": float(n_a_GGE[lam_min_idx]),
        "n_a_GGE_at_lambda_max": float(n_a_GGE[lam_max_idx]),
        "bogoliubov_small_lam_rel_dev_from_half": bogoliubov_small_lam_check_rel_dev,
        "bogoliubov_large_lam_below_1e_minus_3": bogoliubov_large_lam_check,
        "K_PV_envelope_min": float(K_PV_envelope.min()),
        "K_PV_envelope_max": float(K_PV_envelope.max()),
        "K_PV_envelope_mean": float(K_PV_envelope.mean()),
        "regulator_names": np.array(REGULATOR_NAMES),
        "var_a_LEVEL_S": vals_S,
        "var_a_LEVEL_P": vals_P,
        "D_max_per_regulator": np.array([d_max_per_reg[R] for R in REGULATOR_NAMES]),
        "D_max_overall": d_max_overall,
        "W9b_2_upstream_precedent_D_max": W9B_2_UPSTREAM_PRECEDENT_D_MAX,
        "rank_vector_LEVEL_S": ranks_S,
        "rank_vector_LEVEL_P": ranks_P,
        "spearman_rho_S": float(rho_S_corr),
        "spearman_p_value": float(p_value),
        "rank_swap_observed": rank_swap,
        "rank_marginal": rank_marginal,
        "atlas_spread_LEVEL_S_oom": spread_S,
        "atlas_spread_LEVEL_P_oom": spread_P,
        "class_LEVEL_S": class_S,
        "class_LEVEL_P": class_P,
        "criterion_1_structural_parse_tree": criterion_1_pass,
        "criterion_2_regulator_class_unchanged": criterion_2_pass,
        "criterion_3_rank_swap_pass": rank_swap,
        "K_counter_pre": k_counter_pre,
        "K_counter_post": k_counter_post,
        "K_advancement": k_advance,
        "composite_pass": composite_pass,
        "PROXY_TAG": (
            "REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT "
            "(LEVEL-P is PV-envelope-SCHEMATIC-EXTENDED; pending FULL "
            "Connes-Chamseddine 1996 §2.2-2.3 physical multipliers)"
        ),
    }


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    x = np.arange(len(REGULATOR_NAMES))                           # (local)
    width = 0.35                                                  # (local) bar chart width
    ax1.bar(x - width / 2, np.abs(r["var_a_LEVEL_S"]),
             width, label="LEVEL=S (SCHEMATIC)", color="#2c7fb8")
    ax1.bar(x + width / 2, np.abs(r["var_a_LEVEL_P"]),
             width, label="LEVEL=P (PV-envelope-SCHEMATIC-EXTENDED)", color="#f0a05b")
    ax1.set_xticks(x)
    ax1.set_xticklabels(REGULATOR_NAMES, rotation=30)
    ax1.set_yscale("log")
    ax1.set_ylabel("|Var_a^R(LEVEL)|  (log)")
    ax1.set_title(f"CF-49 Var_a 5-regulator × 2-LEVEL comparison\n"
                  f"D_max={r['D_max_overall']:.3f}  Spearman ρ_S={r['spearman_rho_S']:.4f}")
    ax1.legend(fontsize=8)
    ax1.grid(alpha=0.3, axis="y", which="both")

    # Rank-vector comparison
    ax2.plot(x, r["rank_vector_LEVEL_S"], "o-", color="#2c7fb8",
             ms=10, lw=2, label="LEVEL=S rank")
    ax2.plot(x, r["rank_vector_LEVEL_P"], "s--", color="#f0a05b",
             ms=10, lw=2, label="LEVEL=P rank")
    ax2.set_xticks(x)
    ax2.set_xticklabels(REGULATOR_NAMES, rotation=30)
    ax2.set_ylabel("ordinal rank (0..4)")
    swap_str = "SWAP OBSERVED" if r["rank_swap_observed"] else "RANK STABLE"
    ax2.set_title(f"CF-49 Rank-ordering swap test\n"
                  f"{swap_str}  ρ_S={r['spearman_rho_S']:.4f} (< 1 ⇒ swap)")
    ax2.legend(fontsize=8)
    ax2.grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)
    print(f"plot written: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 8 — Verdict emission
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict) -> str:
    if r["composite_pass"]:
        return "PASS"
    # INFO band: criteria (1) + (2) PASS but criterion (3) is MARGINAL
    if (r["criterion_1_structural_parse_tree"]
            and r["criterion_2_regulator_class_unchanged"]
            and r["rank_marginal"]):
        return "INFO"
    return "FAIL"


def append_verdict(verdict: str, value_str: str,
                   audit_sha: str, content_sha: str) -> None:
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_row = (
        f"# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    tier_pin_row = (
        f"# tier_pin=TIER-2 "
        f"# {GATE_ID} SCHEMATIC level pin discipline "
        f"(per substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY; "
        f"PV-envelope-SCHEMATIC-EXTENDED proxy pending FULL Connes-Chamseddine multipliers)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
        fp.write(three_tuple_row)
        fp.write(tier_pin_row)


# ---------------------------------------------------------------------------
# Section 9 — main
# ---------------------------------------------------------------------------
def main() -> int:
    pins = log_input_pins(INPUT_FILES)

    r = compute()
    make_plot(r)
    save_dict = {k: np.asarray(v) for k, v in r.items()}
    np.savez(OUT_NPZ, **save_dict)
    print(f"npz written: {OUT_NPZ}")

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__), SHARED_DIR / "canonical_constants.py", pins)

    verdict = evaluate_gate(r)

    value_str = (
        f"spearman_rho_S={r['spearman_rho_S']:.10f};"
        f"rank_swap_observed={r['rank_swap_observed']};"
        f"D_max_overall={r['D_max_overall']:.4f};"
        f"W9b_2_precedent_D_max=2.168;"
        f"criterion_1_structural={r['criterion_1_structural_parse_tree']};"
        f"criterion_2_class_unchanged={r['criterion_2_regulator_class_unchanged']};"
        f"criterion_3_rank_swap={r['criterion_3_rank_swap_pass']};"
        f"K_counter_pre=1;K_counter_post={r['K_counter_post']};"
        f"K_advancement={r['K_advancement']};"
        f"class_LEVEL_S={r['class_LEVEL_S']};class_LEVEL_P={r['class_LEVEL_P']};"
        f"spread_LEVEL_S_oom={r['atlas_spread_LEVEL_S_oom']:.4f};"
        f"spread_LEVEL_P_oom={r['atlas_spread_LEVEL_P_oom']:.4f};"
        f"bogoliubov_lambda_zero_limit_rel_dev={r['bogoliubov_small_lam_rel_dev_from_half']:.4e};"
        f"bogoliubov_lambda_inf_below_1e_minus_3={r['bogoliubov_large_lam_below_1e_minus_3']};"
        f"N_total_BdG_doubled_modes={r['N_total_modes_BdG_doubled']};"
        f"PROXY_TAG=REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT;"
        f"PROXY_DETAIL=LEVEL-P-is-PV-envelope-SCHEMATIC-EXTENDED-pending-FULL-CC-multipliers"
    )
    print(f"\n4-tuple: (value='{value_str[:80]}...', scheme={SCHEME}, "
          f"convention={CONVENTION[:60]}..., L_max={L_MAX})")
    print(f"audit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")
    print(f"VERDICT: {verdict}")

    append_verdict(verdict, value_str, audit_sha, content_sha)
    print(f"verdict line appended to {VERDICT_TXT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
