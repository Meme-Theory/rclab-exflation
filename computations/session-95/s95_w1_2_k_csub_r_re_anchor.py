#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S95-K-CSUB-R-RE-ANCHOR
=========================

Gate: CF-S95-K-CSUB-R-RE-ANCHOR  ([VERIFY])
Plan: sessions/session-plan/session-95-plan-w1.md §W1-2
Owner: lizzi-spectral-functional-theorist

PURPOSE (re-attempt K_csub_R UV-finiteness after the S94 W1-4 FAIL):
  S94 W1-4 (S94-K-CSUB-R-ABSOLUTE-CONVERGENCE, FAIL) established that the
  2-point Pauli-Villars subtraction at Λ_UV = M_KK does NOT regulate the
  K_csub_R intercept: the a_2 Mellin-s=2 moment Σ_k dim_k λ_k^{−4} on the FULL
  Jensen-deformed spectrum (λ = √C_2·exp(−τρ), ρ=p+q, τ=τ_fold=0.19) DIVERGES
  because per shell ρ the contribution grows like exp(+4τρ)=exp(+0.76ρ) — an
  IR-ACCUMULATION tower (the divergence is at small λ, λ→0 from the high-Casimir
  sectors where the Jensen damping beats the √C_2 growth). The 2-pt PV regulates
  the LARGE-λ (UV) direction; the substrate's divergence is in the SMALL-λ
  (IR-accumulation) direction. S94 measured max_dK_over_dL_pv = 2.1071e+30.

  THIS gate re-attempts via THREE corridors per plan §W1-2:
    (a) N-point (N>=3) Pauli-Villars: Σ c_r = 1, Σ c_r m_r^{2k}=0 for k=1..N−1,
        at Λ_UV = M_KK on the FULL CM-1995 Jensen table; scan |dK/dL| over [50,100].
    (b) τ-running spectral-action regulator mass M_r(τ) tied to the Jensen
        deformation; test whether the IR-accumulation tower is regulated.
    (c) Tier-2 DIMENSIONLESS re-anchor: the log-derivative D(L) = d ln K_csub_R/d ln L
        (which annihilates a MULTIPLICATIVE L-divergent prefactor per math-scripts.md
        §"Multiplicative-normalization cancellation invariants", MANDATORY K=3); test
        Tier-2 re-anchorability per cross-pillar-bridge-anatomy.md Tier-1/Tier-2 gate
        (Tier-2-DIMENSIONLESS re-anchorable, the §VII.AV.STATE-PROJ L_emp precedent,
        vs Tier-2-DIMENSIONFUL held, the §VII.AX.OP-PROJ n_PBH precedent, corpus §25).

PRE-REGISTERED THRESHOLD (plan §W1-2 operator + strict_PASS_boundary):
  operator: inequality (convergence test) OR Tier-2 re-anchorability predicate.
  Tier-1 (corridors a/b):  PASS iff  max_{L in [50,100]} |K(L+dL) − K(L)|/dL  <  1e-3.
  Tier-2 (corridor c):     PASS iff  D(L) = d ln K_csub_R/d ln L  converges
                           (|ΔD/ΔL| < 1e-3)  AND  its limit is a truncation-INVARIANT
                           dimensionless quantity (Tier-2-DIMENSIONLESS, re-anchorable
                           per the Tier-1/Tier-2 gate — NOT Tier-2-dimensionful).
  PASS  iff  EITHER Tier-1 corridor converges OR the Tier-2 log-derivative re-anchors.
  FAIL  iff  all three corridors diverge (no finite-N PV regulates the IR tower AND
            the log-derivative does not converge to a re-anchorable dimensionless limit
            — the dimensionful K_csub_R corridor closes; Tier-2-dimensionful held-number).
  INFO  iff  Tier-1 diverges but the Tier-2 log-derivative converges to a finite limit
            whose Tier-1/Tier-2 re-anchorability is AMBIGUOUS (dimension/divergence
            share a multiplicative slot at the Tier-2-dimensionful boundary).
  Tolerance rule: ABSOLUTE on |dK/dL| and |ΔD/ΔL| vs the 1e-3 ceiling (consumed
    verbatim from the S94 W1-4 convergence ceiling).

SUBSTITUTION CHAIN (plan §W1-2 §7; direction of |dK/dL| + log-derivative):
  Claim: "An N-point (N>=3) PV chain MAY regulate the IR-accumulation tower the
          2-pt PV could not; if not, the Tier-2 log-derivative is the dimensionless
          truncation-invariant re-anchor."
    Step 1 (S94 W1-4 divergence): per-shell K_csub_R contribution ~ exp(+0.76 rho)
            (IR-accumulation under Jensen exp(−τρ) at fixed τ). 2-pt PV (c={+2,−1},
            m²={1,2}) cancels the LARGE-λ (UV) divergence but NOT the IR tower;
            max_dK_over_dL_pv = 2.1071e30 (Sage/npz confirmed).
    Step 2 (N-point PV): N-pt imposes Σ c_r=1 AND Σ c_r m_r^{2k}=0 for k=1..N−1 —
            subtracting the leading N−1 POLYNOMIAL moments of the large-λ Laurent
            series. N=3: 2 conditions (k=1,2); N=4: 3 conditions (k=1,2,3). The PV
            bracket per mode: λ^{−4} − Σ c_r (λ²+m_r²)^{−2}.
    Step 3 (Substitute small-λ asymptotics — the OPERATIVE regime): as λ→0 the
            bracket → λ^{−4} − Σ c_r m_r^{−4} = λ^{−4} − (BOUNDED constant). Any
            finite-N PV subtraction saturates to a BOUNDED per-mode constant at
            λ→0; it CANNOT touch the divergent λ^{−4} at small λ. The IR tower
            exp(+0.76ρ) is an EXPONENTIAL growth, NOT a polynomial moment — a PV
            chain subtracts polynomial moments. Direction is the COMPUTED question;
            the structural expectation is that finite-N PV does NOT regulate an
            exponential tail (TESTED here, not assumed).
    Step 3b (τ-running regulator, corridor b): to regulate exp(+4τρ) the regulator
            would need to inject exp(−4τρ) PER SHELL ρ — i.e. a regulator mass GROWING
            exponentially with ρ at fixed τ. A PV mass M_r(τ) is ρ-INDEPENDENT (one
            scale, possibly τ-dependent). A τ-running M_r(τ) shifts the overall
            subtraction scale but injects NO ρ-dependence. Direction: a ρ-independent
            regulator cannot regulate a ρ-dependent (exponential) tower.
    Step 4 (Tier-2 log-derivative, corridor c): if K_csub_R(L) = w(L)·g with w(L)
            the L-divergent dimensionful weight and g L-INDEPENDENT, then
              d ln K_csub_R/d ln L = d ln w/d ln L + d ln g/d ln L = d ln w/d ln L
            (second term 0). The dimensionful prefactor w(L) is annihilated in the
            log-derivative's SUBSTANTIVE content. BUT: K_csub_R(L) grows ~exp(c·L)
            (super-exponential intercept), so ln K_csub_R ~ c·L (LINEAR in L), and
            D(L) = d ln K/d ln L = L·(d ln K/dL) ~ c·L → GROWS without bound (the
            log-derivative tracks the EXPONENTIAL divergence, NOT a power-law). The
            dimensionless content (the cascade exponent analog) is the question:
            does D(L) converge to a finite dimensionless limit (Tier-2-DIMENSIONLESS,
            re-anchorable) or grow (the divergence and dimension share the slot,
            Tier-2-DIMENSIONFUL, held per §VII.AX n_PBH precedent)?
    Step 5 (Canonical form):
              Tier-1 PASS  <=>  max_{L∈[50,100]} |dK/dL| < 1e-3  (finite-N PV regulates)
              Tier-2 PASS  <=>  D(L) converges (|ΔD/ΔL|<1e-3) AND Tier-2-DIMENSIONLESS.
    Direction: Tier-1 requires |dK/dL| DECREASING below 1e-3 (the S94 value 2.1e30 must
            collapse); Tier-2 requires D(L) (annihilating the dimensionful prefactor)
            to converge. If K_csub_R ~ exp(c·L), the SECOND log-derivative
            d²ln K/d(ln L)² is the truncation-invariant probe (annihilates a power-law
            prefactor); whether it is DIMENSIONLESS-re-anchorable is the Tier-2 verdict.
    Conclusion: PASS in EITHER Tier-1 (finite-N PV converges) OR Tier-2 (the
            dimensionless log-derivative converges + re-anchors). FAIL if all three
            diverge (the dimensionful K_csub_R corridor closes; Tier-2-dimensionful
            held per cross-pillar-bridge-corpus §25/§26).

CLASS pin: FULL (substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY).
  The a_2 Mellin/zeta moments use `_cm_1995_residue_formula.jensen_irrep_table`
  (CLASS=FULL) on the FULL Jensen-deformed Peter-Weyl table (substrate-IS D_K(τ)
  eigenvalues, NO Casimir surrogate, NO L=12 cache ceiling, NO splice). The
  N-point PV subtraction is the explicit closed form generalizing the plan §W1-4
  Step-2 2-pt SUBTRACTIVE form to N>=3 via the Vandermonde moment-condition system.
  The verdict-line convention carries NO -SCHEMATIC suffix for the FULL path. NO
  SCHEMATIC helper is consumed by this gate (the S94 W1-4 heat-kernel/hard-cutoff
  SCHEMATIC cross-check is NOT carried — this gate is a FULL-only retry).

Regulator pins: a_2^{Pauli-Villars} (N-point PV-subtracted) + a_2^{Mellin} + a_2^{zeta}
  (FI-class members; regulator-pin-discipline.md MANDATORY; bare a_2 FORBIDDEN).

Classification: GEOMETRIC. K_csub_R is the c_sub renormalization intercept
  lim_{L→∞} M_Pl_eff²(L)/M_Pl_eff²(0), built from the a_2 Seeley-DeWitt SECOND
  spectral moment Σ_k m_k λ_k^{−4} of D_K (the moment that sources Newton's
  coupling). The substrate IS this ratio; the question is which spectral functional
  of the K_csub_R moment (dimensionful intercept vs dimensionless log-derivative)
  survives the Jensen IR-accumulation. Explanation flows substrate → a_2 coefficient
  → effective Planck mass → renormalization intercept (phononic-framing.md §"IS
  Space, Not IN Space"; epistemic-discipline.md §"Layer-Decomposition").

Inputs (SHA-pinned at runtime):
  - computations/_shared/canonical_constants.py            (M_KK, tau_fold, kappa_2_substrate_FW)
  - computations/_shared/_cm_1995_residue_formula.py       (FULL physical evaluator; CLASS=FULL)
  - computations/_pauli_villars_subtraction.py             (2-pt baseline; extended to N-pt here)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (sector-census cross-check @ L<=12)
  - computations/session-94/s94_w1_4_k_csub_r_absolute_convergence.npz  (S94 divergence diagnosis)

Outputs:
  - computations/session-95/s95_w1_2_k_csub_r_re_anchor.npz
  - computations/session-95/s95_w1_2_k_csub_r_re_anchor.png
  - verdict line + dual-SHA companion row (+ schema-v2 3-tuple, directional pre-reg)
    -> computations/session-95/s95_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # GPU_path pin = cpu-cap-OMP8 (analytic per-sector residue sums; no diagonalization)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import math
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical constants import
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
SESSION_95_DIR = PROJECT_ROOT / "computations" / "session-95"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(COMPUTATIONS_DIR))   # for _pauli_villars_subtraction (lives in computations/, not _shared/)

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    kappa_2_substrate_FW,
)

# FULL physical CM-1995 §III.4 residue evaluator (CLASS="FULL") — substrate-IS Jensen table
from _cm_1995_residue_formula import (  # noqa: E402
    jensen_irrep_table,
    CLASS as CM_CLASS,
    REGULATOR_PIN as CM_REGULATOR_PIN,
)

# 2-point Pauli-Villars baseline helper (cross-check the N=2 limit of the N-point chain)
from _pauli_villars_subtraction import (  # noqa: E402
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
)

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CM_EVALUATOR_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"
PV_MODULE_PATH = COMPUTATIONS_DIR / "_pauli_villars_subtraction.py"
L12_CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
W1_4_NPZ_PATH = PROJECT_ROOT / "computations" / "session-94" / "s94_w1_4_k_csub_r_absolute_convergence.npz"

OUT_NPZ = SESSION_95_DIR / "s95_w1_2_k_csub_r_re_anchor.npz"
OUT_PNG = SESSION_95_DIR / "s95_w1_2_k_csub_r_re_anchor.png"
VERDICT_TXT = SESSION_95_DIR / "s95_gate_verdicts.txt"

# ---------------------------------------------------------------------------
# Section 2 — Gate identity + pre-registered machinery pins (plan §W1-2 §5)
# ---------------------------------------------------------------------------
GATE_ID = "CF-S95-K-CSUB-R-RE-ANCHOR"
SCHEME = "Pauli-Villars-N-point-at-Lambda_UV-M_KK-corridors-a-b-Tier-2-log-derivative-corridor-c-CLASS-FULL"
CONVENTION = "FULL-CM-1995-sec-III-4-residue-N-point-PV-Tier-1-OR-Tier-2-dimensionless-reanchor"
L_MAX = 100  # (local) — scan ceiling; Tier-1 convergence window L in [50,100]

# Pre-registered thresholds (plan §W1-2 operator + strict_PASS_boundary):
DELTA_K_OVER_L_PASS_CEILING = 1.0e-3       # (local) — Tier-1 PASS iff |dK/dL| < 1e-3 over [50,100] (S94 ceiling)
DELTA_D_OVER_L_PASS_CEILING = 1.0e-3       # (local) — Tier-2 PASS iff |ΔD/ΔL| < 1e-3 (log-derivative convergence)
L_FIT_WINDOW = (50, 100)                   # (local) — Friedrich-Bär saturation window
L_GRID_MIN = 10                            # (local) — bottom of the intercept-fit scan (plan: L∈[10,100])
L_GRID_MAX = 100                           # (local)
L_BASELINE = 1                             # (local) — M_Pl_eff² baseline truncation (smallest non-empty Jensen table)
# PV orders tested (plan §4 reachable_rationals: PV order N in {3,4} integer mesh):
PV_ORDERS = (2, 3, 4)                      # (local) — N=2 (S94 baseline reproduction) + N=3, N=4 (the new corridors)
# τ-running regulator (corridor b): regulator mass M_r runs with τ relative to τ_fold.
TAU_RUN_FACTORS = (0.5, 1.0, 2.0)          # (local) — M_r(τ) = m_r·(τ_fold/τ_run); τ_run scan around τ_fold (corridor b)


# ---------------------------------------------------------------------------
# Section 3 — Dual-SHA closure helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 := SHA256(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha256 := SHA256(script_bytes)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    """Append canonical verdict line + dual-SHA companion row + tier_pin companion row
    + schema-v2 3-tuple companion row.

    [VERIFY] trigger, but the §7 substitution chain pre-registers DIRECTIONAL predictions
    (Step 3 |dK/dL| INCREASING under finite-N PV; Step 3b ρ-independent regulator cannot
    regulate ρ-dependent tower; Step 4 D(L) GROWS tracking the exponential divergence), so
    the schema-v2 3-tuple companion row is REQUIRED per gate-verdicts.md §"Schema-v2".

    CLASS=FULL: the FULL CM-1995 + N-point-PV path carries NO -SCHEMATIC suffix; a
    tier_pin=TIER-1 companion row documents the FULL physical level-pin (no SCHEMATIC
    helper consumed)."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )  # (local)
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; §7 directional pre-reg: "
        f"finite-N PV |dK/dL| INCREASING + Tier-2 D(L) GROWS tracking exp divergence)\n"
    )  # (local)
    tier_pin_row = (
        f"# tier_pin=TIER-1 # {GATE_ID} FULL physical level-pin disclosure "
        f"(K=4 MANDATORY per substrate-first-canonical-sourcing.md §(iv); "
        f"FULL CM-1995 §III.4 jensen_irrep_table CLASS=FULL + N-point PV "
        f"Vandermonde moment-condition closed form; a_2^{{Pauli-Villars}}+a_2^{{Mellin}}+"
        f"a_2^{{zeta}}; NO SCHEMATIC helper consumed)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(tuple_row)
        fp.write(tier_pin_row)


# ---------------------------------------------------------------------------
# Section 4 — N-point Pauli-Villars coefficient solver (Vandermonde moment system)
# ---------------------------------------------------------------------------
def solve_pv_coefficients(m2_arr: np.ndarray) -> np.ndarray:
    """Solve the N-point Pauli-Villars consistency system for N masses m_r².

    The PV subtraction reproduces the bare identity at λ²→∞ (Σ c_r = 1) and kills
    the leading N−1 POLYNOMIAL moments of the large-λ Laurent series:

        Σ_{r=1..N} c_r           = 1        (UV identity; k=0)
        Σ_{r=1..N} c_r · m_r^{2k} = 0        (k = 1 .. N−1; no k-th moment divergence)

    This is a Vandermonde-type linear system V c = b with V[k,r] = m_r^{2k},
    b = (1, 0, 0, ..., 0)^T (N equations, N unknowns). For N=2 with m²={1,2} it
    reproduces c={+2,−1} (the S94 baseline). Returns c (length N).

    Note: this generalizes the 2-pt PV SUBTRACTIVE closed form of plan §W1-4 Step 2
    to N>=3. The masses m_r² are dimensionless (λ stored in M_KK units)."""
    N = m2_arr.size  # (local)
    V = np.vander(m2_arr, N, increasing=True).T  # (local) — V[k,r] = m_r^{2k}, k=0..N−1
    b = np.zeros(N, dtype=np.float64)  # (local)
    b[0] = 1.0  # Σ c_r = 1
    c = np.linalg.solve(V, b)  # (local)
    return c


def pv_masses_for_order(N: int, tau_scale: float = 1.0) -> tuple:
    """N-point PV mass set m_r² (dimensionless, M_KK units). Standard CC1996 geometric
    ladder m_r = √r for r=1..N (m_1=1=M_KK, m_2=√2, m_3=√3, ...), so m_r² = r.
    The τ-running corridor (b) scales the masses by tau_scale = (τ_fold/τ_run)."""
    m2 = np.array([float(r) * (tau_scale ** 2) for r in range(1, N + 1)], dtype=np.float64)  # (local)
    c = solve_pv_coefficients(m2)  # (local)
    return c, m2


def a2_bare_s2(L: int, tau: float) -> float:
    """Bare a_2 Mellin-s=2 moment on the FULL Jensen table:
        a_2^{bare}(s=2,L) = Σ_{(p,q)≠(0,0), p+q≤L} dim(p,q)·|λ(p,q,τ)|^{−4}  (s=2 ⇒ −2s=−4).
    |λ| = √C_2·exp(−τρ) (substrate-IS D_K(τ) eigenvalue). NO intrinsic UV cutoff."""
    dims, rhos, lams = jensen_irrep_table(L, tau)  # (local) — FULL Jensen table; (0,0) omitted
    if dims.size == 0:
        return 0.0
    return float(np.sum(dims * lams ** (-4.0)))  # (local)


def a2_pv_npoint_s2(L: int, tau: float, c_arr: np.ndarray, m2_arr: np.ndarray) -> float:
    """N-point SUBTRACTIVE Pauli-Villars a_2 Mellin-s=2 moment (generalizes plan §W1-4
    Step-2 closed form to N masses):

        a_2^{PV-N}(s=2,L) = Σ_k dim_k [ λ_k^{−4} − Σ_{r=1..N} c_r (λ_k² + m_r²)^{−2} ]

    With Σ c_r = 1 and Σ c_r m_r^{2k}=0 for k=1..N−1 (the Vandermonde solution)."""
    dims, rhos, lams = jensen_irrep_table(L, tau)  # (local)
    if dims.size == 0:
        return 0.0
    lam2 = lams * lams  # (local)
    bracket = lam2 ** (-2.0)  # (local) — λ^{−4} bare term
    for c_r, m2_r in zip(c_arr, m2_arr):
        bracket = bracket - c_r * (lam2 + m2_r) ** (-2.0)  # (local) — subtract c_r (λ²+m_r²)^{−2}
    return float(np.sum(dims * bracket))  # (local)


def intercept_expanding_window(L_fit_max: int, L_grid_full: np.ndarray,
                               moment_fn, M0: float, tau: float) -> float:
    """K_csub_R(L_fit_max) := polyfit-intercept (1/L→0) of moment_fn(L)/M0 vs inv_L=1/L
    over the expanding window {L ∈ L_grid_full : L ≤ L_fit_max}. (Matches S94 W1-4.)"""
    mask = L_grid_full <= L_fit_max  # (local)
    Ls = L_grid_full[mask].astype(np.float64)  # (local)
    inv_L = 1.0 / Ls  # (local)
    ratio = np.array([moment_fn(int(L), tau) / M0 for L in Ls], dtype=np.float64)  # (local)
    slope, intercept = np.polyfit(inv_L, ratio, 1)  # (local)
    return float(intercept)


def max_dK_over_dL(K_per_Lfit: np.ndarray, L_fit_points: np.ndarray) -> tuple:
    """max |ΔK/ΔL| over the L_FIT_WINDOW; also report whether increasing."""
    in_w = (L_fit_points >= L_FIT_WINDOW[0]) & (L_fit_points <= L_FIT_WINDOW[1])  # (local)
    Lf_w = L_fit_points[in_w].astype(np.float64)  # (local)
    K_w = K_per_Lfit[in_w]  # (local)
    dK = np.abs(np.diff(K_w))  # (local)
    dL = np.abs(np.diff(Lf_w))  # (local)
    ratio = dK / dL  # (local)
    m = float(np.max(ratio)) if ratio.size else float("inf")  # (local)
    increasing = bool(ratio.size >= 2 and ratio[-1] > ratio[0])  # (local)
    return m, increasing, ratio


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    tau = float(tau_fold)  # (local)
    L_grid = np.arange(L_GRID_MIN, L_GRID_MAX + 1, dtype=np.int64)  # (local) — [10..100], 91 points
    L_fit_points = np.array([12, 16, 20, 30, 40, 50, 60, 70, 80, 90, 100], dtype=np.int64)  # (local)

    # --- per-shell growth diagnosis (Step 1 confirmation; analytic) ---
    # |λ|^{−4} per mode = C_2^{−2}·exp(+4τρ). Per-shell SUM over (p,q) with p+q=ρ.
    rho_grid = np.arange(1, 41, dtype=np.int64)  # (local) — shell-index ρ for the growth fit
    shell_weight = np.zeros(rho_grid.size, dtype=np.float64)  # (local)
    from _cm_1995_residue_formula import su3_casimir, su3_dimension  # (local) — closed forms
    for i, rho in enumerate(rho_grid):
        s = 0.0  # (local)
        for p in range(int(rho) + 1):
            q = int(rho) - p  # (local)
            if p == 0 and q == 0:
                continue
            c2 = su3_casimir(p, q)  # (local)
            d = su3_dimension(p, q)  # (local)
            lam = math.sqrt(c2) * math.exp(-tau * rho)  # (local)
            s += d * lam ** (-4.0)  # (local)
        shell_weight[i] = s
    # log-linear fit: ln(shell_weight) ~ slope·ρ + const  ⇒ slope ≈ +4τ = +0.76
    ln_sw = np.log(shell_weight)  # (local)
    shell_slope, shell_const = np.polyfit(rho_grid.astype(np.float64), ln_sw, 1)  # (local)
    expected_slope = 4.0 * tau  # (local) — +0.76 at τ=0.19

    # --- baselines M_Pl_eff²(0) = a_2(L=1) (smallest non-empty Jensen table) ---
    M0_bare = a2_bare_s2(L_BASELINE, tau)  # (local)

    # ===================================================================
    # CORRIDOR (a) — N-point Pauli-Villars (N in PV_ORDERS = {2,3,4})
    # ===================================================================
    pv_results = {}  # (local) — keyed by N
    for N in PV_ORDERS:
        c_arr, m2_arr = pv_masses_for_order(N, tau_scale=1.0)  # (local)
        # PV consistency verification (Σc=1; Σc·m^{2k}=0 for k=1..N−1):
        sum_c = float(np.sum(c_arr))  # (local)
        moment_residuals = [float(np.sum(c_arr * m2_arr ** k)) for k in range(1, N)]  # (local)
        identities_ok = bool(abs(sum_c - 1.0) < 1e-9 and all(abs(mr) < 1e-9 for mr in moment_residuals))  # (local)

        def _mom(L, t, _c=c_arr, _m=m2_arr):
            return a2_pv_npoint_s2(int(L), t, _c, _m)  # (local)

        M0_N = _mom(L_BASELINE, tau)  # (local)
        moments = np.array([_mom(int(L), tau) for L in L_grid], dtype=np.float64)  # (local)
        K_per_Lfit = np.array(
            [intercept_expanding_window(int(Lf), L_grid, _mom, M0_N, tau) for Lf in L_fit_points],
            dtype=np.float64,
        )  # (local)
        mx, incr, ratio = max_dK_over_dL(K_per_Lfit, L_fit_points)  # (local)
        converges = bool(mx < DELTA_K_OVER_L_PASS_CEILING)  # (local)
        # small-λ asymptotic per-mode subtraction constant Σ c_r m_r^{−4} (Step 3 bound):
        ir_sub_const = float(np.sum(c_arr * m2_arr ** (-2.0)))  # (local) — BOUNDED constant; ≠ λ^{−4}
        pv_results[N] = {
            "c_arr": c_arr, "m2_arr": m2_arr, "sum_c": sum_c,
            "moment_residuals": moment_residuals, "identities_ok": identities_ok,
            "M0_N": M0_N, "moments": moments, "K_per_Lfit": K_per_Lfit,
            "max_dK_over_dL": mx, "increasing": incr, "converges": converges,
            "K_intercept_L100": float(K_per_Lfit[-1]), "ir_sub_const": ir_sub_const,
        }

    tier1_a_any_converges = bool(any(pv_results[N]["converges"] for N in PV_ORDERS))  # (local)

    # ===================================================================
    # CORRIDOR (b) — τ-running regulator mass M_r(τ) tied to the Jensen deformation
    # Test: with N=3 PV, run the regulator masses by tau_scale = τ_fold/τ_run.
    # A ρ-INDEPENDENT regulator mass (even τ-running) cannot regulate exp(+4τρ).
    # ===================================================================
    N_b = 3  # (local) — use the N=3 chain for the τ-running test
    tau_run_results = {}  # (local) — keyed by tau_run_factor
    for trf in TAU_RUN_FACTORS:
        # τ_run = τ_fold · trf ; tau_scale = τ_fold/τ_run = 1/trf (mass runs inversely with τ_run)
        tau_scale = 1.0 / trf  # (local)
        c_b, m2_b = pv_masses_for_order(N_b, tau_scale=tau_scale)  # (local)

        def _mom_b(L, t, _c=c_b, _m=m2_b):
            return a2_pv_npoint_s2(int(L), t, _c, _m)  # (local)

        M0_b = _mom_b(L_BASELINE, tau)  # (local)
        K_per_Lfit_b = np.array(
            [intercept_expanding_window(int(Lf), L_grid, _mom_b, M0_b, tau) for Lf in L_fit_points],
            dtype=np.float64,
        )  # (local)
        mx_b, incr_b, _r = max_dK_over_dL(K_per_Lfit_b, L_fit_points)  # (local)
        conv_b = bool(mx_b < DELTA_K_OVER_L_PASS_CEILING)  # (local)
        tau_run_results[trf] = {
            "tau_scale": tau_scale, "m2_b": m2_b, "max_dK_over_dL": mx_b,
            "increasing": incr_b, "converges": conv_b, "K_intercept_L100": float(K_per_Lfit_b[-1]),
        }
    tier1_b_any_converges = bool(any(tau_run_results[trf]["converges"] for trf in TAU_RUN_FACTORS))  # (local)

    # ===================================================================
    # CORRIDOR (c) — Tier-2 DIMENSIONLESS log-derivative re-anchor
    # D(L) = d ln K_csub_R / d ln L  (annihilates a MULTIPLICATIVE L-divergent prefactor).
    # Use the BARE intercept (the canonical K_csub_R; the N-pt PV does not change the
    # divergence class — confirmed by corridor a). Probe:
    #   (1st log-deriv) D1(L) = d ln K / d ln L
    #   (2nd log-deriv) D2(L) = d² ln K / d(ln L)²  (annihilates a POWER-LAW prefactor)
    # Tier-2-DIMENSIONLESS iff D converges to a finite limit whose dimension is NOT
    # trapped in the divergence's multiplicative slot.
    # ===================================================================
    K_bare_per_Lfit = np.array(
        [intercept_expanding_window(int(Lf), L_grid, a2_bare_s2, M0_bare, tau) for Lf in L_fit_points],
        dtype=np.float64,
    )  # (local) — the canonical K_csub_R(L) (bare; PV-invariant divergence class)
    lnK = np.log(np.abs(K_bare_per_Lfit))  # (local)
    lnL = np.log(L_fit_points.astype(np.float64))  # (local)
    # 1st log-derivative D1(L) = Δ ln K / Δ ln L (centered difference on the grid)
    D1 = np.gradient(lnK, lnL)  # (local)
    # 2nd log-derivative D2(L) = Δ D1 / Δ ln L
    D2 = np.gradient(D1, lnL)  # (local)
    # convergence of D1 over the window [50,100]:
    in_w = (L_fit_points >= L_FIT_WINDOW[0]) & (L_fit_points <= L_FIT_WINDOW[1])  # (local)
    D1_w = D1[in_w]  # (local)
    Lf_w = L_fit_points[in_w].astype(np.float64)  # (local)
    lnL_w = np.log(Lf_w)  # (local)
    dD1_dlnL = np.abs(np.diff(D1_w) / np.diff(lnL_w))  # (local)
    max_dD1_dlnL = float(np.max(dD1_dlnL)) if dD1_dlnL.size else float("inf")  # (local)
    D1_converges = bool(max_dD1_dlnL < DELTA_D_OVER_L_PASS_CEILING)  # (local)
    D1_increasing = bool(D1_w.size >= 2 and D1_w[-1] > D1_w[0])  # (local)
    # 2nd log-derivative convergence (power-law-prefactor-annihilating probe):
    D2_w = D2[in_w]  # (local)
    dD2_dlnL = np.abs(np.diff(D2_w) / np.diff(lnL_w))  # (local)
    max_dD2_dlnL = float(np.max(dD2_dlnL)) if dD2_dlnL.size else float("inf")  # (local)
    D2_converges = bool(max_dD2_dlnL < DELTA_D_OVER_L_PASS_CEILING)  # (local)

    # --- ln K vs L (NOT ln L) linear fit: if K ~ exp(c·L) then ln K = c·L + const ---
    # This is the diagnostic that distinguishes EXPONENTIAL (IR-accumulation) from POWER-LAW.
    Lf_all = L_fit_points.astype(np.float64)  # (local)
    expL_slope, expL_const = np.polyfit(Lf_all, lnK, 1)  # (local) — slope c if ln K ~ c·L
    # residual of the exp(c·L) fit (how well ln K is LINEAR in L, not ln L):
    lnK_pred_expL = expL_slope * Lf_all + expL_const  # (local)
    expL_resid = float(np.max(np.abs(lnK - lnK_pred_expL)))  # (local)
    # contrast: power-law fit ln K ~ alpha·ln L + const (residual should be WORSE if exp):
    powL_slope, powL_const = np.polyfit(lnL, lnK, 1)  # (local) — slope α if ln K ~ α·ln L
    lnK_pred_powL = powL_slope * lnL + powL_const  # (local)
    powL_resid = float(np.max(np.abs(lnK - lnK_pred_powL)))  # (local)
    # exp dominates iff exp-fit residual << power-law-fit residual:
    growth_is_exponential = bool(expL_resid < 0.5 * powL_resid)  # (local)

    # -------------------------------------------------------------------
    # Tier-1/Tier-2 classification (cross-pillar-bridge-anatomy.md gate; corpus §25):
    #   Tier-1: convergent ⇒ a substrate-singled-out L* exists. Here Tier-1 FAILS
    #           (all corridor a/b PV forms diverge — IR-accumulation tower).
    #   Tier-2-DIMENSIONLESS (re-anchorable, §VII.AV L_emp precedent): the divergent
    #           channel's truncation-invariant content is DIMENSIONLESS and a
    #           log-derivative / ratio annihilates the divergence cleanly.
    #   Tier-2-DIMENSIONFUL (held, §VII.AX n_PBH precedent): the dimension prefactor
    #           and the L-divergence share ONE multiplicative slot; the log-derivative
    #           annihilates the prefactor but the held NUMBER is dimensionful.
    #
    # K_csub_R(L) = M_Pl_eff²(L)/M_Pl_eff²(0) ≡ a_2(L)/a_2(0). The a_2 moment carries
    # M_KK² physical units (Newton's coupling); K_csub_R as a RATIO is dimensionless in
    # the moment-ratio sense, but the physically-anchored K_csub_R magnitude is the
    # M_Pl_eff² intercept which is M_KK²-scaled. The divergence is EXPONENTIAL (ln K ~ c·L),
    # NOT a multiplicative power-law prefactor w(L)=L^p — so d ln K/d ln L = L·c GROWS (does
    # NOT converge), and d² ln K/d(ln L)² also does not converge to a finite cascade-exponent.
    # The dimensionless cascade-exponent (the §VII.AX route, where d ln N_eigs/d ln L → integer 5)
    # does NOT exist here because the growth is exp(c·L), not L^5. ⇒ NEITHER log-derivative
    # re-anchors to a finite dimensionless limit. The dimension (M_KK²) is in the SAME
    # multiplicative slot as the exp(+0.76ρ) divergence (the a_2 moment is M_KK²·Σλ^{−4}).
    # -------------------------------------------------------------------
    tier1_converges = bool(tier1_a_any_converges or tier1_b_any_converges)  # (local)
    tier2_log_deriv_converges = bool(D1_converges or D2_converges)  # (local)
    # Tier-2-DIMENSIONLESS requires (i) a log-derivative converges AND (ii) the limit is
    # a dimensionless truncation-invariant (e.g. an integer cascade exponent). Here the
    # growth is exponential, so NO log-derivative converges; classification = DIMENSIONFUL.
    tier2_dimensionless_reanchorable = bool(tier2_log_deriv_converges and not growth_is_exponential)  # (local)
    tier2_classification = (
        "Tier-2-DIMENSIONLESS-reanchorable" if tier2_dimensionless_reanchorable
        else "Tier-2-DIMENSIONFUL-held"
    )  # (local)

    # -------------------------------------------------------------------
    # VERDICT (plan §W1-2 operator: inequality OR Tier-2 re-anchorability predicate)
    # -------------------------------------------------------------------
    evaluator_runnable = bool(
        math.isfinite(M0_bare) and M0_bare > 0
        and all(pv_results[N]["identities_ok"] for N in PV_ORDERS)
        and all(np.all(np.isfinite(pv_results[N]["K_per_Lfit"])) for N in PV_ORDERS)
    )  # (local)

    if not evaluator_runnable:
        verdict = "FAIL"
        band_tag = "FAIL_evaluator_or_PV_identity_failed"  # (local)
    elif tier1_converges:
        verdict = "PASS"
        band_tag = "PASS_Tier-1_finite-N-PV_or_tau-running_regulates_IR_tower"  # (local)
    elif tier2_dimensionless_reanchorable:
        verdict = "PASS"
        band_tag = "PASS_Tier-2_dimensionless_log-derivative_reanchors"  # (local)
    elif tier2_log_deriv_converges and not tier2_dimensionless_reanchorable:
        # log-derivative converges but Tier-1/Tier-2 re-anchorability AMBIGUOUS
        verdict = "INFO"
        band_tag = "INFO_Tier-2_log-derivative_converges_but_reanchorability_ambiguous"  # (local)
    else:
        # all three corridors diverge: dimensionful K_csub_R corridor closes;
        # Tier-2-DIMENSIONFUL held-number (§VII.AX n_PBH precedent, corpus §25/§26)
        verdict = "FAIL"
        band_tag = "FAIL_all_three_corridors_diverge_Tier-2-DIMENSIONFUL_held"  # (local)

    # --- schema-v2 3-tuple (directional pre-reg per §7) ---
    # sign_verdict: §7 Step 3 predicts finite-N PV |dK/dL| INCREASING (divergence persists);
    #   Step 4 predicts D(L) GROWS tracking the exponential. PASS = predicted direction matches.
    #   Predicted: divergence (tier1 does NOT converge) AND D1 increasing AND growth exponential.
    sign_predicted_divergence = True  # (local) — §7 directional prediction: corridors a/b diverge
    sign_observed_divergence = bool((not tier1_converges) and D1_increasing and growth_is_exponential)  # (local)
    sign_v = "PASS" if (sign_predicted_divergence == sign_observed_divergence) else "FAIL"  # (local)
    # magnitude_verdict: does the gate land a finite re-anchored value? PASS iff Tier-1 or
    #   Tier-2-dimensionless re-anchors (a finite re-anchorable quantity); FAIL iff held.
    mag_v = "PASS" if (tier1_converges or tier2_dimensionless_reanchorable) else "FAIL"  # (local)
    # regime_verdict: the FULL Jensen evaluator + N-pt PV are valid throughout [10,100].
    regime_v = "VALID" if evaluator_runnable else "BREAKDOWN"  # (local)

    return {
        "tau_fold": tau, "M_KK": float(M_KK), "kappa_2_substrate_FW": float(kappa_2_substrate_FW),
        "L_grid": L_grid, "L_fit_points": L_fit_points, "L_fit_window": np.array(L_FIT_WINDOW),
        "M0_bare": M0_bare,
        # per-shell growth diagnosis (Step 1):
        "rho_grid": rho_grid, "shell_weight": shell_weight,
        "shell_slope": float(shell_slope), "expected_slope": expected_slope,
        # corridor (a) N-point PV (store per-N; flatten the arrays for npz):
        "pv_orders": np.array(PV_ORDERS),
        "K_bare_per_Lfit": K_bare_per_Lfit,
        "tier1_a_any_converges": tier1_a_any_converges,
        # corridor (b) τ-running:
        "tau_run_factors": np.array(TAU_RUN_FACTORS),
        "tier1_b_any_converges": tier1_b_any_converges,
        # corridor (c) Tier-2 log-derivative:
        "D1": D1, "D2": D2, "max_dD1_dlnL": max_dD1_dlnL, "max_dD2_dlnL": max_dD2_dlnL,
        "D1_converges": D1_converges, "D2_converges": D2_converges, "D1_increasing": D1_increasing,
        "expL_slope": float(expL_slope), "expL_resid": expL_resid,
        "powL_slope": float(powL_slope), "powL_resid": powL_resid,
        "growth_is_exponential": growth_is_exponential,
        # Tier-1/Tier-2 classification:
        "tier1_converges": tier1_converges, "tier2_log_deriv_converges": tier2_log_deriv_converges,
        "tier2_dimensionless_reanchorable": tier2_dimensionless_reanchorable,
        "tier2_classification": tier2_classification,
        "pass_ceiling": DELTA_K_OVER_L_PASS_CEILING,
        # verdict:
        "evaluator_runnable": evaluator_runnable, "verdict": verdict, "band_tag": band_tag,
        "sign_v": sign_v, "mag_v": mag_v, "regime_v": regime_v,
        "cm_class": CM_CLASS, "cm_regulator_pin": CM_REGULATOR_PIN,
        # nested per-N + per-trf dicts (kept out of npz top-level; serialized below):
        "_pv_results": pv_results, "_tau_run_results": tau_run_results,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14.0, 9.5), dpi=120)
    pv = r["_pv_results"]  # (local)
    L_fit = r["L_fit_points"]  # (local)

    # Panel A: K_csub_R^{PV-N}(1/L→0) intercept vs L_fit for N=2,3,4 (log) — all diverge
    axA = axes[0, 0]
    colors = {2: "#d62728", 3: "#2ca02c", 4: "#1f77b4"}  # (local)
    for N in r["pv_orders"].tolist():
        axA.semilogy(L_fit, np.abs(pv[N]["K_per_Lfit"]), "o-", color=colors.get(N, "k"),
                     ms=4, lw=1.2, label=f"N={N}-pt PV (max|ΔK/ΔL|={pv[N]['max_dK_over_dL']:.2e})")
    axA.axvspan(r["L_fit_window"][0], r["L_fit_window"][1], color="purple", alpha=0.10,
                label=f"window [{r['L_fit_window'][0]},{r['L_fit_window'][1]}]")
    axA.set_xlabel("L_fit (top of expanding 1/L window)")
    axA.set_ylabel("|K_csub_R^{PV-N} intercept|  (log)")
    axA.set_title("(A) Corridor (a): N-point PV intercept GROWS for all N=2,3,4\n"
                  "(finite-N PV subtracts polynomial moments; IR tower is exponential)")
    axA.legend(fontsize=8); axA.grid(alpha=0.3)

    # Panel B: per-shell growth ln(shell_weight) vs ρ — slope ≈ +0.76 = +4τ
    axB = axes[0, 1]
    rho = r["rho_grid"]  # (local)
    axB.plot(rho, np.log(r["shell_weight"]), "o", color="#9467bd", ms=3,
             label="ln(Σ_{p+q=ρ} dim·λ^{−4})")
    axB.plot(rho, r["shell_slope"] * rho + np.log(r["shell_weight"])[0] - r["shell_slope"] * rho[0],
             "-", color="k", lw=1.2,
             label=f"fit slope={r['shell_slope']:.4f} (expect +4τ={r['expected_slope']:.4f})")
    axB.set_xlabel("shell index ρ = p+q"); axB.set_ylabel("ln(per-shell a_2 weight)")
    axB.set_title("(B) Step-1 IR-accumulation: per-shell weight ~ exp(+0.76ρ)\n"
                  "(Jensen damping exp(−τρ) drives λ→0 ⇒ λ^{−4} accumulates)")
    axB.legend(fontsize=8.5); axB.grid(alpha=0.3)

    # Panel C: Tier-2 log-derivatives D1(L), D2(L) vs L (does NOT converge)
    axC = axes[1, 0]
    axC.plot(L_fit, r["D1"], "s-", color="#2ca02c", ms=4, lw=1.3, label="D1 = d ln K/d ln L")
    axC.plot(L_fit, r["D2"], "^-", color="#ff7f0e", ms=4, lw=1.3, label="D2 = d² ln K/d(ln L)²")
    axC.axvspan(r["L_fit_window"][0], r["L_fit_window"][1], color="purple", alpha=0.10)
    axC.set_xlabel("L_fit"); axC.set_ylabel("log-derivative")
    axC.set_title("(C) Corridor (c) Tier-2: D1, D2 GROW (do NOT converge)\n"
                  f"max|ΔD1/ΔlnL|={r['max_dD1_dlnL']:.2e} (ceiling 1e-3); growth is exp(c·L)")
    axC.legend(fontsize=8.5); axC.grid(alpha=0.3)

    # Panel D: verdict + diagnostic text
    axD = axes[1, 1]
    axD.axis("off")
    lines = [
        f"VERDICT: {r['verdict']}",
        f"band_tag: {r['band_tag']}",
        f"3-tuple: sign={r['sign_v']} mag={r['mag_v']} regime={r['regime_v']}",
        "",
        f"CLASS pin: {r['cm_class']} (FULL; CM-1995 + N-pt PV; NO -SCHEMATIC)",
        f"regulator: a_2^{{Pauli-Villars}} + a_2^{{Mellin}} + a_2^{{zeta}}",
        "",
        "--- Corridor (a) N-point PV (Tier-1) ---",
    ]
    for N in r["pv_orders"].tolist():
        lines.append(
            f"  N={N}: Σc={pv[N]['sum_c']:.3f} ids_ok={pv[N]['identities_ok']}  "
            f"max|ΔK/ΔL|={pv[N]['max_dK_over_dL']:.3e} conv={pv[N]['converges']}"
        )
        lines.append(f"        IR-sub-const Σc_r m_r^{{−4}}={pv[N]['ir_sub_const']:+.4f} (BOUNDED, ≠λ^{{−4}})")
    lines += [
        f"  Tier-1(a) any converges = {r['tier1_a_any_converges']}",
        "",
        "--- Corridor (b) τ-running regulator (Tier-1) ---",
    ]
    trr = r["_tau_run_results"]  # (local)
    for trf in r["tau_run_factors"].tolist():
        lines.append(
            f"  τ_run×{trf}: max|ΔK/ΔL|={trr[trf]['max_dK_over_dL']:.3e} conv={trr[trf]['converges']}"
        )
    lines += [
        f"  Tier-1(b) any converges = {r['tier1_b_any_converges']}",
        "",
        "--- Corridor (c) Tier-2 log-derivative ---",
        f"  D1 converges = {r['D1_converges']} (max|ΔD1/ΔlnL|={r['max_dD1_dlnL']:.2e})",
        f"  D2 converges = {r['D2_converges']} (max|ΔD2/ΔlnL|={r['max_dD2_dlnL']:.2e})",
        f"  ln K ~ exp(c·L): c={r['expL_slope']:.4f} resid={r['expL_resid']:.2e}",
        f"  ln K ~ α·ln L:   α={r['powL_slope']:.4f} resid={r['powL_resid']:.2e}",
        f"  growth_is_exponential = {r['growth_is_exponential']}",
        f"  classification: {r['tier2_classification']}",
        "",
        "--- S94 W1-4 baseline ---",
        "  2-pt PV: max|ΔK/ΔL| = 2.1071e+30 (FAIL)",
    ]
    axD.text(0.0, 1.0, "\n".join(lines), va="top", ha="left", fontsize=7.0,
             family="monospace", transform=axD.transAxes)
    axD.set_title("(D) Diagnostic summary")

    fig.suptitle(
        f"{GATE_ID}\nK_csub_R re-anchor: 3 corridors (N-pt PV / τ-running / Tier-2 log-deriv) — "
        f"{r['verdict']}  ({r['tier2_classification']})",
        fontsize=10.5, y=1.005,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"\nplot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"tau_fold = {tau_fold!r}  M_KK = {M_KK!r}")
    print(f"FULL CM-1995 evaluator CLASS={CM_CLASS}  regulator={CM_REGULATOR_PIN}")
    print(f"2-pt PV baseline c={PV_PRIMARY_C.tolist()}  m²={(PV_PRIMARY_M_DIMLESS**2).tolist()}")

    INPUT_FILES = [
        Path(__file__).resolve(),
        CANONICAL_CONSTANTS_PATH,
        CM_EVALUATOR_PATH,
        PV_MODULE_PATH,
        L12_CACHE_PATH,
        W1_4_NPZ_PATH,
    ]  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)

    r = compute()  # (local)
    pv = r["_pv_results"]  # (local)
    trr = r["_tau_run_results"]  # (local)

    print("\n=== Step 1: per-shell IR-accumulation growth ===")
    print(f"  fit slope = {r['shell_slope']:.6f}  (expected +4τ = {r['expected_slope']:.6f})")

    print("\n=== Corridor (a): N-point Pauli-Villars ===")
    for N in r["pv_orders"].tolist():
        print(f"  N={N}: c={pv[N]['c_arr'].tolist()}")
        print(f"        m²={pv[N]['m2_arr'].tolist()}  Σc={pv[N]['sum_c']:.6f}  "
              f"moment_resid={['%.2e' % x for x in pv[N]['moment_residuals']]}  ids_ok={pv[N]['identities_ok']}")
        print(f"        K_intercept(L=12)={pv[N]['K_per_Lfit'][0]:+.4e}  "
              f"K_intercept(L=100)={pv[N]['K_intercept_L100']:+.4e}")
        print(f"        max|ΔK/ΔL| over [50,100] = {pv[N]['max_dK_over_dL']:.6e}  "
              f"converges={pv[N]['converges']}  increasing={pv[N]['increasing']}")
        print(f"        IR-sub-const Σc_r m_r^{{−4}} = {pv[N]['ir_sub_const']:+.6f} (bounded; ≠ λ^{{−4}})")
    print(f"  Tier-1 corridor (a) ANY converges = {r['tier1_a_any_converges']}")

    print("\n=== Corridor (b): τ-running regulator ===")
    for trf in r["tau_run_factors"].tolist():
        print(f"  τ_run×{trf} (tau_scale={trr[trf]['tau_scale']:.3f}): "
              f"max|ΔK/ΔL|={trr[trf]['max_dK_over_dL']:.6e}  converges={trr[trf]['converges']}")
    print(f"  Tier-1 corridor (b) ANY converges = {r['tier1_b_any_converges']}")

    print("\n=== Corridor (c): Tier-2 dimensionless log-derivative ===")
    print(f"  D1 = d ln K/d ln L converges = {r['D1_converges']} (max|ΔD1/ΔlnL|={r['max_dD1_dlnL']:.4e})")
    print(f"  D2 = d² ln K/d(ln L)² converges = {r['D2_converges']} (max|ΔD2/ΔlnL|={r['max_dD2_dlnL']:.4e})")
    print(f"  ln K ~ exp(c·L): c={r['expL_slope']:.6f}  residual={r['expL_resid']:.4e}")
    print(f"  ln K ~ α·ln L:   α={r['powL_slope']:.6f}  residual={r['powL_resid']:.4e}")
    print(f"  growth_is_exponential = {r['growth_is_exponential']}")
    print(f"  Tier-2 classification = {r['tier2_classification']}")

    print(f"\nVERDICT: {r['verdict']}  ({r['band_tag']})")
    print(f"3-tuple: sign={r['sign_v']} magnitude={r['mag_v']} regime={r['regime_v']}")

    make_plot(r)

    # --- serialize per-N PV arrays for npz (flatten the nested dict) ---
    pv_max_dK = np.array([pv[N]["max_dK_over_dL"] for N in r["pv_orders"].tolist()], dtype=np.float64)  # (local)
    pv_converges = np.array([pv[N]["converges"] for N in r["pv_orders"].tolist()], dtype=bool)  # (local)
    pv_K_intercept_L100 = np.array([pv[N]["K_intercept_L100"] for N in r["pv_orders"].tolist()], dtype=np.float64)  # (local)
    pv_ir_sub_const = np.array([pv[N]["ir_sub_const"] for N in r["pv_orders"].tolist()], dtype=np.float64)  # (local)
    pv_identities_ok = np.array([pv[N]["identities_ok"] for N in r["pv_orders"].tolist()], dtype=bool)  # (local)
    pv_K_per_Lfit_stack = np.array([pv[N]["K_per_Lfit"] for N in r["pv_orders"].tolist()], dtype=np.float64)  # (local)
    trf_list = r["tau_run_factors"].tolist()  # (local)
    trr_max_dK = np.array([trr[t]["max_dK_over_dL"] for t in trf_list], dtype=np.float64)  # (local)
    trr_converges = np.array([trr[t]["converges"] for t in trf_list], dtype=bool)  # (local)

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, verdict=r["verdict"], band_tag=r["band_tag"],
        scheme=SCHEME, convention=CONVENTION, cm_class=r["cm_class"], cm_regulator_pin=r["cm_regulator_pin"],
        sign_verdict=r["sign_v"], magnitude_verdict=r["mag_v"], regime_verdict=r["regime_v"],
        tau_fold=r["tau_fold"], M_KK=r["M_KK"], kappa_2_substrate_FW=r["kappa_2_substrate_FW"],
        L_grid=r["L_grid"], L_fit_points=r["L_fit_points"], L_fit_window=r["L_fit_window"],
        L_max=L_MAX, L_baseline=L_BASELINE, pass_ceiling=r["pass_ceiling"],
        M0_bare=r["M0_bare"], K_bare_per_Lfit=r["K_bare_per_Lfit"],
        # Step 1 per-shell growth:
        rho_grid=r["rho_grid"], shell_weight=r["shell_weight"],
        shell_slope=r["shell_slope"], expected_slope=r["expected_slope"],
        # corridor (a):
        pv_orders=r["pv_orders"], pv_max_dK_over_dL=pv_max_dK, pv_converges=pv_converges,
        pv_K_intercept_L100=pv_K_intercept_L100, pv_ir_sub_const=pv_ir_sub_const,
        pv_identities_ok=pv_identities_ok, pv_K_per_Lfit_stack=pv_K_per_Lfit_stack,
        tier1_a_any_converges=r["tier1_a_any_converges"],
        # corridor (b):
        tau_run_factors=r["tau_run_factors"], trr_max_dK_over_dL=trr_max_dK, trr_converges=trr_converges,
        tier1_b_any_converges=r["tier1_b_any_converges"],
        # corridor (c) Tier-2:
        D1=r["D1"], D2=r["D2"], max_dD1_dlnL=r["max_dD1_dlnL"], max_dD2_dlnL=r["max_dD2_dlnL"],
        D1_converges=r["D1_converges"], D2_converges=r["D2_converges"], D1_increasing=r["D1_increasing"],
        expL_slope=r["expL_slope"], expL_resid=r["expL_resid"],
        powL_slope=r["powL_slope"], powL_resid=r["powL_resid"],
        growth_is_exponential=r["growth_is_exponential"],
        # Tier-1/Tier-2 classification:
        tier1_converges=r["tier1_converges"], tier2_log_deriv_converges=r["tier2_log_deriv_converges"],
        tier2_dimensionless_reanchorable=r["tier2_dimensionless_reanchorable"],
        tier2_classification=r["tier2_classification"],
        evaluator_runnable=r["evaluator_runnable"],
        # S94 reference:
        s94_w1_4_max_dK_over_dL_pv_2pt=2.107060298000938e+30,
    )
    print(f"data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # --- value field for verdict line ---
    value_field = (
        f"tier1_a_converges={r['tier1_a_any_converges']};tier1_b_converges={r['tier1_b_any_converges']};"
        f"tier2_log_deriv_converges={r['tier2_log_deriv_converges']};"
        f"tier2_class={r['tier2_classification']};"
        f"N3_max_dK_dL={pv[3]['max_dK_over_dL']:.4e};N4_max_dK_dL={pv[4]['max_dK_over_dL']:.4e};"
        f"N2_max_dK_dL={pv[2]['max_dK_over_dL']:.4e};"
        f"D1_max_dD_dlnL={r['max_dD1_dlnL']:.4e};lnK_expL_slope={r['expL_slope']:.4f};"
        f"lnK_expL_resid={r['expL_resid']:.2e};lnK_powL_resid={r['powL_resid']:.2e};"
        f"growth_exponential={r['growth_is_exponential']};shell_slope={r['shell_slope']:.4f}_expect={r['expected_slope']:.4f};"
        f"PASS_ceiling=1e-3;S94_2pt_baseline=2.1071e30;band_tag={r['band_tag']}"
    )  # (local)

    print(f"\n4-tuple: (value='{value_field[:90]}...', scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    input_pin_map = {rel: sha for rel, sha in pins.items()}  # (local)
    input_pin_map["canonical_constants_M_KK"] = f"{M_KK:.18e}"
    input_pin_map["canonical_constants_tau_fold"] = f"{tau_fold:.18e}"
    input_pin_map["canonical_constants_kappa_2_substrate_FW"] = f"{kappa_2_substrate_FW:.18e}"
    input_pin_map["_gate_id"] = GATE_ID
    input_pin_map["_scheme"] = SCHEME
    input_pin_map["_convention"] = CONVENTION

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_CONSTANTS_PATH, input_pin_map
    )  # (local)
    append_verdict(r["verdict"], value_field, audit_sha, content_sha,
                   r["sign_v"], r["mag_v"], r["regime_v"])
    print(f"\nverdict appended: {r['verdict']} -- value (truncated)={value_field[:100]!r}...")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"\nwall: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
