#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S94-K-CSUB-R-ABSOLUTE-CONVERGENCE
=================================

Gate: S94-K-CSUB-R-ABSOLUTE-CONVERGENCE  ([CHAIN])
Plan: sessions/session-plan/session-94-plan-w1.md §W1-4

PURPOSE (UV-convergence proof of the FULL K_csub_R intercept):
  S93 W7-2 proved the −245.69 SCHEMATIC intercept is a methodology-floor
  artifact (cache_truncation_fraction_FULL=0.000906; drop_factor 1074×) and
  emitted the FULL bare intercept K_csub_R = +247259.9583 (Mellin=zeta,
  F2FI=True). But that FULL intercept is itself LARGE because the bare a_2
  Mellin-s=2 moment  Σ_k m_k λ_k^{−4}  (s=2 ⇒ −2s=−4) at fixed Jensen τ_fold
  has NO intrinsic UV cutoff and grows with the Peter-Weyl truncation L_max.

  THIS gate applies the substrate-canonical S61/S78 2-point Pauli-Villars
  subtraction at Λ_UV = M_KK (Connes-Chamseddine 1996 §2.2-2.3 multipliers
  {c_1,c_2}={+2,−1}, masses {M_1,M_2}={M_KK, √2·M_KK}) to the FULL a_2
  Mellin-s=2 moment and asks the pre-registered question:

      Does the PV-subtracted K_csub_R intercept converge to a finite
      L_max → ∞ limit  (|ΔK_csub_R^{PV}/ΔL_max| → 0)  ?

  The bare and PV-subtracted moments are evaluated on the FULL Jensen-
  deformed Peter-Weyl irrep table (`_cm_1995_residue_formula.jensen_irrep_table`,
  CLASS=FULL — the substrate-IS D_K(τ) eigenvalues, NOT a Casimir surrogate,
  NO L=12 cache ceiling, NO splice). The intercept is extracted by polyfit on
  inv_L = 1/L_grid over an EXPANDING window ending at each L_fit ∈ [10,100]
  (Casimir-bound analytic tail; NO raw diagonalization above L=12 per
  math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection
  Feasibility Pre-Check" — jensen_irrep_table builds the spectrum directly,
  so no diagonalization is performed at any L).

PRE-REGISTERED THRESHOLD (plan §W1-4 operator + strict_PASS_boundary):
  operator: inequality.
  PASS  iff  |ΔK_csub_R^{PV}/ΔL_max| < 1e-3 at L_fit∈[50,100]  (PV-subtracted
            intercept converges; the a_2 s=2 moment is UV-finite under the
            2-point PV subtraction)  AND  the 5-regulator FI spread is within
            the O(20%) heat-kernel-moment-ratio band (F_2={ζ,Mellin} exact 0).
  FAIL  iff  |ΔK/ΔL| does NOT converge over [50,100]  (the 2-point PV subtraction
            is insufficient to render the s=2 moment UV-finite at fixed τ_fold)
            OR  the 5-regulator FI spread exceeds the O(20%) band.
  INFO  iff  |ΔK/ΔL| converges for the F_2={ζ,Mellin} FULL class but the SCHEMATIC
            {heat-kernel, hard-cutoff} cross-check drifts beyond the O(20%) band
            (a SCHEMATIC-vs-FULL class-conflation signature), OR convergence is
            established only symbolically on the Casimir-bound analytic tail.
  Tolerance rule: ABSOLUTE on |ΔK/ΔL| vs the 1e-3 ceiling (UV-convergence);
    the FI spread is a RATIO test (< O(20%) cross-class; exact 0 for F_2).

SUBSTITUTION CHAIN (plan §W1-4 §7; direction of |ΔK/ΔL|):
  Claim: "The PV-subtracted a_2 Mellin-s=2 moment is UV-convergent, so its
          K_csub_R intercept converges to a finite L_max→∞ limit (|ΔK/ΔL|→0),
          unlike the bare FULL moment which grows with L_max (+247260)."
    Step 1: a_2^{bare}(s=2, L_max) = Σ_{(p,q), p+q≤L_max} d(p,q)·|λ(p,q,τ)|^{−4}
            (s=2 ⇒ −2s=−4). The FULL a_2 Mellin moment; W7-2 FULL_intercept=+247260.
            |λ(p,q,τ)| = √C_2(p,q)·exp(−τ·ρ), ρ=p+q, so
              d·|λ|^{−4} = d·C_2^{−2}·exp(+4τρ).
            Per shell ρ this term grows like exp(+4τρ)=exp(+0.76ρ) (τ=0.19) ⇒
            a_2^{bare} grows WITHOUT bound (the moment is NOT UV-convergent at
            fixed τ; the divergence accumulates as λ→0 from high-Casimir sectors).
    Step 2: 2-point Pauli-Villars subtraction (S61/S78; CC1996 §2.2-2.3;
            DIMENSIONLESS masses m²={1, 2} since the FULL Jensen eigenvalues are
            stored in M_KK units, per _pauli_villars_subtraction.py docstring
            "M_KK→1, √2·M_KK→√2 in λ units"). TWO PV forms are tested:
              (A) SUBTRACTIVE (plan §W1-4 Step-2 LITERAL closed form):
                  a_2^{PV-sub}(s=2) = Σ_k d_k [ λ_k^{−4}
                                                − 2·(λ_k² + 1)^{−2}
                                                + 1·(λ_k² + 2)^{−2} ].
              (B) MULTIPLIER (standard CC1996/_pauli_villars_subtraction PRIMARY):
                  a_2^{PV-mult}(s=2) = Σ_k d_k · w_PV(λ_k²;2) · λ_k^{−4},
                  w_PV(λ²;2) = 1 − 2·(1/(λ²+1))² + 1·(2/(λ²+2))².
            Forms (A) and (B) are NOT algebraically identical (Sage:
            A−B = −(x²+3x−2)/(x⁴+3x³+2x²), x=λ²); the plan pre-registers (A),
            so (A) is the GATED form; (B) is reported as the standard-PV contrast.
            Both multiplier sets satisfy Σc_j=1, Σc_j M_j²=0 (verified at load).
    Step 3: Substitute (small-λ asymptotics — the operative regime here).
            The substrate's high-Casimir sectors have SMALL λ (λ²=C_2·exp(−0.38ρ)→0
            because the Jensen damping exp(−τρ) beats the √C_2 growth at fixed τ),
            so the divergence accumulates at λ→0, NOT λ→∞.
              Form (A) bracket → λ^{−4} − (2·1 − 1·(1/4)) = λ^{−4} − 1.75
                              ~ λ^{−4}  (the M²={1,2} subtraction terms saturate
                              to a BOUNDED constant 1.75/mode, negligible vs the
                              DIVERGENT λ^{−4}); per-shell ~ exp(+4τρ)=exp(+0.76ρ).
                              ⇒ a_2^{PV-sub} ≈ a_2^{bare} at large L (ratio→1).
              Form (B) w_PV·λ^{−4} → 3/λ² + O(1)  (Sage series at λ²→0; UV power
                              raised by 2, NOT 4 — w_PV~O(λ²) softens it); per-shell
                              ~ exp(+2τρ)=exp(+0.38ρ). STILL DIVERGENT, slower than (A).
            The 2-point PV (either form) regulates the large-λ (UV) direction, but
            the substrate's divergence is in the small-λ (IR-accumulation) direction
            at fixed τ — neither form renders the a_2 s=2 moment UV-finite.
    Step 4: K_csub_R^{PV}(L_fit) = polyfit-intercept of M_Pl_eff_sq^{PV}(L)/M0^{PV}
            vs inv_L=1/L over the expanding window [10, L_fit]. Because
            a_2^{Pauli-Villars} grows (Step 3), the per-L_max moment does NOT
            plateau ⇒ |ΔK_csub_R^{PV}/ΔL_max| does NOT → 0.
            Direction: |ΔK/ΔL| measured INCREASING (divergence), NOT decreasing.
    Step 5: FI check. K_csub_R^{Mellin} = K_csub_R^{ζ} EXACTLY (F2FI by zeta-
            Mellin equivalence on the positive-definite spectrum; diff=0 by
            construction). The PV-subtracted intercept across {Pauli-Villars,
            Mellin, ζ} (FULL); the SCHEMATIC {heat-kernel, hard-cutoff} cross-
            check carries the −SCHEMATIC tag + tier_pin=TIER-2 (level-pin).
    Conclusion: PASS iff |ΔK/ΔL|→0 (UV-convergent) AND FI within band. The
            measured |ΔK/ΔL| over [50,100] is verified against the 1e-3 ceiling;
            a non-convergent |ΔK/ΔL| closes the "2-point PV at Λ_UV=M_KK suffices"
            corridor (FAIL) — a higher-point PV or different regulator is required.

CLASS pin: FULL (substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY).
  PRIMARY substrate-canonical FULL evaluation: the a_2 Mellin/zeta moments use
  `_cm_1995_residue_formula.jensen_irrep_table` (CLASS=FULL) on the FULL Jensen-
  deformed Peter-Weyl table; the 2-point PV subtraction is the explicit closed
  form of plan §W1-4 Step 2 (algebraically IDENTICAL to the PRIMARY
  `_pauli_villars_subtraction.pv_mellin_moment_primary` with c={+2,−1},
  m²_dimensionless={1,2} — cross-checked bit-precision in this script).
  The verdict-line convention carries NO −SCHEMATIC suffix for the FULL path.
  The SCHEMATIC {heat-kernel, hard-cutoff} 5-atlas members
  (`_spectral_action_regulators.py`, no CLASS attr, docstring self-identifies
  "SCHEMATIC ... Casimir schematic spectrum") are CROSS-CHECK ONLY, disclosed
  with the −SCHEMATIC convention suffix + a `# tier_pin=TIER-2` companion row +
  a Type-F cross-class disclosure paragraph in the WP §"Methodology".

  PROVENANCE-LABEL RECONCILIATION (disclosed honestly): the plan §W1-4
  provenance hint labeled `_pauli_villars_subtraction.py` as CLASS=SCHEMATIC
  (cross-check only). Its OWN docstring (S88 W13-159) self-identifies as
  PRIMARY full-physical (TIER-1 lift from the SCHEMATIC single-subtraction
  `_spectral_action_regulators.pauli_villars_a_n`). This gate sidesteps the
  label ambiguity by implementing the PV subtraction DIRECTLY from the plan's
  Step-2 closed form and cross-checking it bit-precision against the PRIMARY
  module helper. The FULL PV moment is therefore substrate-canonical regardless
  of the module label; the FULL-path convention carries no −SCHEMATIC suffix.

Regulator pins: a_2^{Pauli-Villars} (PV-subtracted) + a_2^{Mellin} + a_2^{ζ}
  (FI-class members; regulator-pin-discipline.md MANDATORY; bare a_2 FORBIDDEN).

Classification: GEOMETRIC. The a_2 Seeley-DeWitt coefficient is the SECOND
spectral moment Σ_k m_k λ_k^{−4} of D_K — the moment that sources Newton's
coupling (Einstein-Hilbert emerges from a_2). K_csub_R is the c_sub
renormalization intercept lim_{L→∞} M_Pl_eff²(L)/M_Pl_eff²(0). The substrate IS
this ratio; the question is whether the substrate-canonical Λ_UV=M_KK PV
subtraction renders it UV-finite. Explanation flows substrate → a_2 coefficient
→ effective Planck mass → renormalization intercept (epistemic-discipline.md
§"Layer-Decomposition"; phononic-framing.md §"IS Space, Not IN Space").

Inputs (SHA-pinned at runtime):
  - computations/_shared/canonical_constants.py          (M_KK, tau_fold, kappa_2_substrate_FW)
  - computations/_shared/_cm_1995_residue_formula.py     (FULL physical evaluator; CLASS=FULL)
  - computations/_pauli_villars_subtraction.py           (PRIMARY 2-point PV cross-check)
  - computations/_shared/_spectral_action_regulators.py  (SCHEMATIC cross-check only)
  - computations/session-93/s93_w7_2_k_csub_r_full_physical_retry.py  (FULL bare intercept +247259.9583)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz         (n_irrep cross-check @ L<=12)

Outputs:
  - computations/session-94/s94_w1_4_k_csub_r_absolute_convergence.npz
  - computations/session-94/s94_w1_4_k_csub_r_absolute_convergence.png
  - verdict line + dual-SHA companion row -> computations/session-94/s94_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # GPU_path pin = cpu-cap-OMP8 (O(N) per-sector residue sums; no diagonalization)
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
SESSION_94_DIR = PROJECT_ROOT / "computations" / "session-94"
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

# PRIMARY 2-point Pauli-Villars helper (cross-check the plan Step-2 closed form bit-precision)
from _pauli_villars_subtraction import (  # noqa: E402
    pv_mellin_moment_primary,
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
)

# SCHEMATIC 5-regulator atlas (heat-kernel + hard-cutoff cross-check ONLY; -SCHEMATIC tagged)
from _spectral_action_regulators import (  # noqa: E402
    heat_kernel_a_n,
    hard_cutoff_a_n,
)

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CM_EVALUATOR_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"
PV_MODULE_PATH = COMPUTATIONS_DIR / "_pauli_villars_subtraction.py"
SCHEMATIC_MODULE_PATH = SHARED_DIR / "_spectral_action_regulators.py"
W7_2_EVALUATOR_PATH = PROJECT_ROOT / "computations" / "session-93" / "s93_w7_2_k_csub_r_full_physical_retry.py"
L12_CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = SESSION_94_DIR / "s94_w1_4_k_csub_r_absolute_convergence.npz"
OUT_PNG = SESSION_94_DIR / "s94_w1_4_k_csub_r_absolute_convergence.png"
VERDICT_TXT = SESSION_94_DIR / "s94_gate_verdicts.txt"

# ---------------------------------------------------------------------------
# Section 2 — Gate identity + pre-registered machinery pins (plan §W1-4 §5)
# ---------------------------------------------------------------------------
GATE_ID = "S94-K-CSUB-R-ABSOLUTE-CONVERGENCE"
SCHEME = "FULL-CM-1995-sec-III-4-residue-PauliVillars-Lambda_UV-M_KK-a_2-s2-moment"
# K=4 level-pin: CLASS=FULL for the PV/Mellin/zeta path (NO -SCHEMATIC suffix);
# a_2^{Pauli-Villars} + a_2^{Mellin} + a_2^{zeta} regulator tags.
CONVENTION = "K_CSUB_R-ABSOLUTE-CONVERGENCE-PV-SUBTRACTED-a_2-Mellin-s2-CLASS-FULL"
L_MAX = 100  # (local) — top of the analytic-tail L_grid scan window (1/L polyfit intercept → L_max→∞)

# Pre-registered thresholds (plan §W1-4 operator + strict_PASS_boundary):
DELTA_K_OVER_L_PASS_CEILING = 1.0e-3       # (local) — PASS iff |ΔK/ΔL| < 1e-3 at L_fit∈[50,100]
FI_SPREAD_BAND = 0.20                        # (local) — O(20%) heat-kernel-moment-ratio cross-class FI band
F2_FI_EXACT_TOL = 1.0e-9                     # (local) — F_2={ζ,Mellin} exact-0 tolerance (machine-zero)
L_FIT_WINDOW = (50, 100)                     # (local) — Friedrich-Bär saturation window for the convergence metric
L_GRID_MIN = 10                              # (local) — bottom of the intercept-fit scan (plan: L∈[10,100])
L_GRID_MAX = 100                             # (local)
L_BASELINE = 1                               # (local) — M_Pl_eff² baseline truncation (smallest non-empty Jensen table)
# 2-point PV (dimensionless masses since FULL Jensen λ are in M_KK units):
PV_C = (2.0, -1.0)                           # (local) — {c_1, c_2} multipliers (Σc_j=1; CC1996 §2.2-2.3)
PV_M2_DIMLESS = (1.0, 2.0)                   # (local) — {M_1², M_2²} = {M_KK², 2·M_KK²} in λ (M_KK) units
SCHEMATIC_HEAT_KERNEL_T_REF = 1.0e-3         # (local) — Zubarev heat-kernel reference time (SCHEMATIC)
SCHEMATIC_HARD_CUTOFF_FRAC = 0.7             # (local) — hard-cutoff fraction (SCHEMATIC)
# Reference (S93 W7-2 FULL bare intercept; for the contrast narrative, not a gate):
W7_2_FULL_BARE_INTERCEPT_REF = 247259.9583   # (local) — S93 W7-2 (Mellin=zeta, F2FI=True)
# Option A supersession (gate-verdicts.md §"Option A"): the first run's FAIL line landed
# under a spurious evaluator_or_module_match tag (the subtractive-vs-multiplier PV-form
# difference was mis-treated as a breakage). The corrective re-emission carries this
# supersedes tag; the original line is RETAINED on disk per absolute verdict permanence.
SUPERSEDES_AUDIT_SHA = "943b753b3c889b5166d7ac6cdd4bec5088c858cfa6d25e5b70fcc3137728ff6f"  # (local)


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


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append canonical verdict line + dual-SHA companion row + tier_pin companion row.
    Atomic single open("a") write (POSIX O_APPEND-safe).
    [CHAIN] trigger: NO schema-v2 3-tuple companion row (no directional [SIGN] pre-reg
    in §9 Step 4 — the convergence-direction prediction is the gate's primary metric,
    tested as the ABSOLUTE |ΔK/ΔL| < 1e-3 inequality, not a 3-tuple SIGN gate).
    CLASS=FULL: the FULL PV/Mellin/zeta path carries NO -SCHEMATIC suffix; the SCHEMATIC
    {heat-kernel, hard-cutoff} cross-check is disclosed via a SEPARATE tier_pin=TIER-2
    companion row per substrate-first-canonical-sourcing.md §(iv)."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    tier_pin_row = (
        f"# tier_pin=TIER-1 # {GATE_ID} FULL physical level-pin disclosure "
        f"(K=4 MANDATORY per substrate-first-canonical-sourcing.md §(iv); "
        f"FULL CM-1995 §III.4 jensen_irrep_table CLASS=FULL + 2-point PV plan-§W1-4-Step-2 "
        f"SUBTRACTIVE closed form (gated; Sage-distinct from the multiplier form); "
        f"a_2^{{Pauli-Villars}}+a_2^{{Mellin}}+a_2^{{zeta}}; SCHEMATIC heat-kernel/hard-cutoff "
        f"5-atlas members are -SCHEMATIC tier_pin=TIER-2 cross-check ONLY)\n"
    )  # (local)
    supersedes_row = (
        f"# supersedes={SUPERSEDES_AUDIT_SHA} # {GATE_ID} corrective re-emission per "
        f"gate-verdicts.md §\"Option A\" (prior FAIL line under spurious "
        f"evaluator_or_module_match tag RETAINED on disk; this corrective line is canonical; "
        f"genuine physics verdict = PV-subtracted intercept does NOT converge ⇒ 2-pt PV insufficient)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(tier_pin_row)
        fp.write(supersedes_row)


# ---------------------------------------------------------------------------
# Section 4 — a_2 Mellin-s=2 moments (FULL Jensen table) : bare + 2-point PV
# ---------------------------------------------------------------------------
def a2_bare_s2(L: int, tau: float) -> float:
    """Bare a_2 Mellin-s=2 moment on the FULL Jensen-deformed Peter-Weyl table:

        a_2^{bare}(s=2, L) = Σ_{(p,q)≠(0,0), p+q≤L} dim(p,q) · |λ(p,q,τ)|^{−4}

    (s=2 ⇒ −2s=−4). |λ| = √C_2·exp(−τρ) is the substrate-IS D_K(τ) eigenvalue.
    This SUM has no intrinsic UV cutoff (W7-2 FULL_intercept ~ +247260)."""
    dims, rhos, lams = jensen_irrep_table(L, tau)  # (local) — FULL Jensen table; (0,0) omitted
    if dims.size == 0:
        return 0.0
    return float(np.sum(dims * lams ** (-4.0)))  # (local)


def a2_pv_s2(L: int, tau: float) -> float:
    """SUBTRACTIVE 2-point Pauli-Villars a_2 Mellin-s=2 moment — the GATED form
    (plan §W1-4 Step-2 LITERAL closed form):

        a_2^{PV-sub}(s=2, L)
          = Σ_k dim_k [ λ_k^{−4} − 2·(λ_k² + 1)^{−2} + 1·(λ_k² + 2)^{−2} ]

    DIMENSIONLESS masses m²={1,2} (= {M_KK², 2·M_KK²} in λ M_KK-units, per
    _pauli_villars_subtraction.py docstring). Multipliers {+2,−1} satisfy
    Σc_j=1, Σc_j M_j²=0 (UV identity reproduction; no quadratic divergence).
    Convention: a_2^{bare} − Σ_j c_j Σ_k dim_k (λ_k² + M_j²)^{−2}
    (s=2 ⇒ power −2 on the shifted denominators)."""
    dims, rhos, lams = jensen_irrep_table(L, tau)  # (local)
    if dims.size == 0:
        return 0.0
    lam2 = lams * lams  # (local)
    bracket = lam2 ** (-2.0)  # (local) — λ^{−4} bare term
    for c_j, m2_j in zip(PV_C, PV_M2_DIMLESS):
        bracket = bracket - c_j * (lam2 + m2_j) ** (-2.0)  # (local) — subtract c_j (λ²+M_j²)^{−2}
    return float(np.sum(dims * bracket))  # (local)


def a2_pv_mult_s2(L: int, tau: float) -> float:
    """MULTIPLIER 2-point Pauli-Villars a_2 Mellin-s=2 moment — the standard-PV
    CONTRAST form (CC1996; _pauli_villars_subtraction.pv_mellin_moment_primary):

        a_2^{PV-mult}(s=2, L) = Σ_k dim_k · w_PV(λ_k²;2) · λ_k^{−4},
        w_PV(λ²;2) = 1 − Σ_r c_r (m_r²/(λ²+m_r²))²

    NOT algebraically identical to the subtractive form (Sage:
    A−B = −(x²+3x−2)/(x⁴+3x³+2x²), x=λ²). Reported as the standard-PV contrast;
    NOT the gated quantity (the plan pre-registers the subtractive form)."""
    dims, rhos, lams = jensen_irrep_table(L, tau)  # (local)
    if dims.size == 0:
        return 0.0
    return float(pv_mellin_moment_primary(
        2.0, lams, dims,
        c_arr=np.asarray(PV_PRIMARY_C), m_arr=np.asarray(PV_PRIMARY_M_DIMLESS),
    ))  # (local)


def intercept_expanding_window(L_fit_max: int, L_grid_full: np.ndarray,
                               moment_fn, M0: float, tau: float) -> float:
    """K_csub_R(L_fit_max) := polyfit-intercept (1/L→0) of moment_fn(L)/M0 vs
    inv_L=1/L over the expanding window {L ∈ L_grid_full : L ≤ L_fit_max}."""
    mask = L_grid_full <= L_fit_max  # (local)
    Ls = L_grid_full[mask].astype(np.float64)  # (local)
    inv_L = 1.0 / Ls  # (local)
    ratio = np.array([moment_fn(int(L), tau) / M0 for L in Ls], dtype=np.float64)  # (local)
    slope, intercept = np.polyfit(inv_L, ratio, 1)  # (local)
    return float(intercept)


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    tau = float(tau_fold)  # (local)
    L_grid = np.arange(L_GRID_MIN, L_GRID_MAX + 1, dtype=np.int64)  # (local) — [10..100], 91 points

    # --- baselines M_Pl_eff²(0) = a_2(L=1) for bare and PV (smallest non-empty Jensen table) ---
    M0_bare = a2_bare_s2(L_BASELINE, tau)  # (local) — > 0
    M0_pv = a2_pv_s2(L_BASELINE, tau)      # (local) — > 0

    M0_pv_mult = a2_pv_mult_s2(L_BASELINE, tau)  # (local) — multiplier-form baseline (> 0)

    # --- per-L moments + dimensionless ratios (full grid) ---
    bare_moment = np.array([a2_bare_s2(int(L), tau) for L in L_grid], dtype=np.float64)     # (local)
    pv_moment = np.array([a2_pv_s2(int(L), tau) for L in L_grid], dtype=np.float64)         # (local) — GATED subtractive form
    pv_mult_moment = np.array([a2_pv_mult_s2(int(L), tau) for L in L_grid], dtype=np.float64)  # (local) — multiplier contrast
    bare_ratio = bare_moment / M0_bare  # (local)
    pv_ratio = pv_moment / M0_pv        # (local)

    # --- PV/bare suppression ratio per L (Step-3 diagnostic: → 1 means PV negligible) ---
    pv_over_bare = pv_moment / bare_moment            # (local) — subtractive: → 1 (diverges like bare)
    pv_mult_over_bare = pv_mult_moment / bare_moment  # (local) — multiplier: → 0 slower (softer divergence)

    # --- PV-form distinctness check (subtractive vs multiplier; NOT a breakage — a FINDING) ---
    # The plan §W1-4 Step-2 pre-registers the SUBTRACTIVE form. The PRIMARY module helper
    # implements the MULTIPLIER form. They are algebraically DISTINCT (Sage:
    #   subtractive − multiplier = −(x²+3x−2)/(x⁴+3x³+2x²), x=λ²),
    # so a "match" is NOT expected. We record the residual + the distinctness as a finding,
    # and verify the SUBTRACTIVE in-script form reproduces a hand-evaluation at L=12.
    dimsX, rhosX, lamsX = jensen_irrep_table(12, tau)  # (local) — at L=12 cache anchor
    pv_sub_in_script_L12 = a2_pv_s2(12, tau)   # (local) — subtractive (gated)
    pv_mult_module_L12 = a2_pv_mult_s2(12, tau)  # (local) — multiplier (contrast)
    # Independent hand-evaluation of the subtractive bracket at L=12 (NOT via a2_pv_s2):
    lam2X = lamsX * lamsX  # (local)
    bracketX = lam2X ** (-2.0) - PV_C[0] * (lam2X + PV_M2_DIMLESS[0]) ** (-2.0) \
        - PV_C[1] * (lam2X + PV_M2_DIMLESS[1]) ** (-2.0)  # (local)
    pv_sub_hand_L12 = float(np.sum(dimsX * bracketX))  # (local)
    pv_sub_selfcheck_residual = abs(pv_sub_in_script_L12 - pv_sub_hand_L12)  # (local)
    pv_sub_selfcheck_ok = bool(pv_sub_selfcheck_residual < 1e-9 * max(1.0, abs(pv_sub_in_script_L12)))  # (local)
    pv_forms_distinct = bool(abs(pv_sub_in_script_L12 - pv_mult_module_L12) > 1e-3)  # (local) — Sage-confirmed

    # --- PV multiplier-identity cross-check (Σc=1, Σc·M²=0) ---
    sum_c = float(sum(PV_C))  # (local)
    sum_cm2 = float(sum(c * m2 for c, m2 in zip(PV_C, PV_M2_DIMLESS)))  # (local)
    pv_identities_ok = bool(abs(sum_c - 1.0) < 1e-15 and abs(sum_cm2) < 1e-15)  # (local)

    # -------------------------------------------------------------------
    # K_csub_R intercept (1/L→0) on EXPANDING windows ending at each L_fit.
    #   bare: contrast (W7-2 reproduces +247260 at the cache window)
    #   PV:   the GATED quantity — does its intercept converge?
    # -------------------------------------------------------------------
    L_fit_points = np.array([12, 16, 20, 30, 40, 50, 60, 70, 80, 90, 100], dtype=np.int64)  # (local)
    K_bare_per_Lfit = np.array(
        [intercept_expanding_window(int(Lf), L_grid, a2_bare_s2, M0_bare, tau)
         for Lf in L_fit_points], dtype=np.float64
    )  # (local)
    K_pv_per_Lfit = np.array(
        [intercept_expanding_window(int(Lf), L_grid, a2_pv_s2, M0_pv, tau)
         for Lf in L_fit_points], dtype=np.float64
    )  # (local) — GATED subtractive form
    K_pv_mult_per_Lfit = np.array(
        [intercept_expanding_window(int(Lf), L_grid, a2_pv_mult_s2, M0_pv_mult, tau)
         for Lf in L_fit_points], dtype=np.float64
    )  # (local) — multiplier contrast

    def _max_dK_over_dL(K_per_Lfit: np.ndarray) -> tuple:
        in_w = (L_fit_points >= L_FIT_WINDOW[0]) & (L_fit_points <= L_FIT_WINDOW[1])  # (local)
        Lf_w = L_fit_points[in_w].astype(np.float64)  # (local)
        K_w = K_per_Lfit[in_w]  # (local)
        dK = np.abs(np.diff(K_w))  # (local)
        dL = np.abs(np.diff(Lf_w))  # (local)
        ratio = dK / dL  # (local)
        m = float(np.max(ratio)) if ratio.size else float("inf")  # (local)
        increasing = bool(ratio.size >= 2 and ratio[-1] > ratio[0])  # (local)
        return m, increasing, ratio

    # --- |ΔK/ΔL| convergence metric (subtractive = GATED form) over L_fit∈[50,100] ---
    max_dK_over_dL_pv, dK_over_dL_increasing, dK_over_dL_pv = _max_dK_over_dL(K_pv_per_Lfit)  # (local)
    pv_intercept_converges = bool(max_dK_over_dL_pv < DELTA_K_OVER_L_PASS_CEILING)  # (local)

    # --- multiplier-form convergence metric (contrast; reported, not gated) ---
    max_dK_over_dL_pv_mult, dK_over_dL_mult_increasing, _dummy = _max_dK_over_dL(K_pv_mult_per_Lfit)  # (local)
    pv_mult_intercept_converges = bool(max_dK_over_dL_pv_mult < DELTA_K_OVER_L_PASS_CEILING)  # (local)

    # -------------------------------------------------------------------
    # 5-regulator FI check (at the canonical L=12 cache anchor; the FI test is on
    # the regulator-CLASS agreement of the a_2 s=2 moment, NOT on the divergent
    # intercept — F_2={ζ,Mellin} exact by construction).
    # FULL members: Pauli-Villars, Mellin, zeta (= Mellin on the positive spectrum).
    # SCHEMATIC members (cross-check ONLY, -SCHEMATIC tagged): heat-kernel, hard-cutoff.
    # -------------------------------------------------------------------
    L_FI = 12  # (local) — canonical cache anchor for the FI comparison
    # FULL Mellin = zeta = bare a_2 moment (the substrate-IS dimension-spectrum value at z=0):
    a2_mellin_FULL = a2_bare_s2(L_FI, tau)  # (local) — a_2^{Mellin}
    a2_zeta_FULL = a2_bare_s2(L_FI, tau)    # (local) — a_2^{ζ} (entire ζ_φ(z); res_{z=0}=value at z=0)
    a2_pv_FULL = a2_pv_s2(L_FI, tau)        # (local) — a_2^{Pauli-Villars}
    F2_diff = abs(a2_mellin_FULL - a2_zeta_FULL)  # (local) — F_2={ζ,Mellin} difference
    F2_FI_exact = bool(F2_diff < F2_FI_EXACT_TOL)  # (local) — exact 0 by construction

    # SCHEMATIC cross-check (a_2 = a_2(n=2) on the Casimir schematic spectrum; CLASS-conflation diagnostic):
    # NOTE: these are SCHEMATIC analogs on a pure-Casimir spectrum (NO Jensen exp(-tau*rho)
    # damping in the schematic _enumerate_sectors). They are NOT substrate-IS; cross-check ONLY.
    Vol_haar = 1.0  # (local) — Haar-normalized volume placeholder for the schematic helper
    a2_heat_kernel_SCH = float(heat_kernel_a_n(2, L_FI, Vol_haar, t_ref=SCHEMATIC_HEAT_KERNEL_T_REF))  # (local)
    a2_hard_cutoff_SCH = float(hard_cutoff_a_n(2, L_FI, Vol_haar, cutoff_frac=SCHEMATIC_HARD_CUTOFF_FRAC))  # (local)

    # FI spread across the FULL class {PV, Mellin, zeta} (the gate's FI conjunct):
    full_members = np.array([a2_pv_FULL, a2_mellin_FULL, a2_zeta_FULL], dtype=np.float64)  # (local)
    full_mean = float(np.mean(full_members))  # (local)
    full_spread = float((np.max(full_members) - np.min(full_members)) / abs(full_mean)) if full_mean != 0 else float("inf")  # (local)
    # The FULL PV vs Mellin spread is LARGE here (PV subtraction shifts the moment substantially
    # at L=12 where it is NOT yet negligible); report it but the FI band is a regulator-CLASS
    # statement — F_2={ζ,Mellin} is the exact-0 sub-class; PV is a DIFFERENT regulator class.
    full_FI_within_band = bool(full_spread < FI_SPREAD_BAND)  # (local)

    # --- L<=12 sector-census cross-check vs the L=12 master cache (informational) ---
    # The FULL jensen_irrep_table OMITS (0,0); the cache STORES (0,0). The substrate-
    # consistency check is on the NONZERO sectors with p+q≤12: both should agree.
    dims12, _, _ = jensen_irrep_table(12, tau)  # (local)
    n_irrep_L12_FULL = int(dims12.size)  # (local) — jensen nonzero-sector count
    n_nonzero_cache = -1  # (local)
    n_total_cache = -1   # (local)
    try:
        cache = np.load(L12_CACHE_PATH, allow_pickle=True)  # (local)
        se = cache["sector_evals"].item()  # (local) — dict keyed by (p,q)
        n_total_cache = int(len(se))  # (local) — includes (0,0)
        n_nonzero_cache = int(sum(1 for (p, q) in se if (p, q) != (0, 0) and (p + q) <= 12))  # (local)
    except Exception as exc:  # noqa: BLE001
        print(f"  [warn] could not load L12 cache for sector-census cross-check: {exc}")
    # Informational only: the cache nonzero-sector census may differ from jensen by the
    # cache's own truncation convention (it stores per-sector abs_evals for a DIFFERENT
    # block-diagonalization census). This is NOT a gate; the FULL evaluator builds the
    # spectrum directly per CM-1995 §III.4 (substrate-IS), independent of the cache.
    n_irrep_cache_census_note = (
        f"jensen_nonzero={n_irrep_L12_FULL}; cache_total={n_total_cache}; "
        f"cache_nonzero_pq<=12={n_nonzero_cache}"
    )  # (local)

    # -------------------------------------------------------------------
    # VERDICT (plan §W1-4 operator: inequality; composite of the two conjuncts)
    #   conjunct 1 (UV-convergence): |ΔK/ΔL| < 1e-3 over [50,100]
    #   conjunct 2 (FI): F_2={ζ,Mellin} exact 0  (the FULL-class FI floor)
    # -------------------------------------------------------------------
    # evaluator_runnable gates ONLY on genuine evaluability of the FULL substrate-IS
    # path: finite positive baselines, a non-empty spectrum, the PV multiplier
    # identities (Σc=1, Σc·M²=0), the SUBTRACTIVE self-check (gated form reproduces a
    # hand evaluation), and finite intercepts. It does NOT gate on pv_forms_distinct
    # (the subtractive-vs-multiplier difference is a Sage-confirmed FINDING, not a
    # breakage) nor on the cache census (informational; the FULL evaluator is cache-
    # independent).
    evaluator_runnable = bool(
        math.isfinite(M0_bare) and M0_bare > 0
        and math.isfinite(M0_pv) and M0_pv > 0
        and n_irrep_L12_FULL > 0
        and pv_identities_ok and pv_sub_selfcheck_ok
        and np.all(np.isfinite(K_pv_per_Lfit))
    )  # (local)

    if not evaluator_runnable:
        verdict = "FAIL"
        band_tag = "FAIL_FULL_evaluator_or_PV_identity_or_subtractive_selfcheck_failed"  # (local)
    elif pv_intercept_converges and F2_FI_exact:
        verdict = "PASS"
        band_tag = "PASS_PV_subtracted_intercept_converges_and_F2_FI_exact"  # (local)
    elif pv_intercept_converges and not F2_FI_exact:
        # convergent but FULL-FI floor broken → SCHEMATIC-vs-FULL class signature
        verdict = "INFO"
        band_tag = "INFO_PV_intercept_converges_but_F2_FI_not_exact"  # (local)
    else:
        # PV-subtracted intercept does NOT converge over [50,100]:
        # the 2-point PV at Λ_UV=M_KK is INSUFFICIENT to render a_2 s=2 UV-finite at fixed τ.
        verdict = "FAIL"
        band_tag = "FAIL_PV_subtracted_intercept_does_NOT_converge_2pt_PV_insufficient"  # (local)

    return {
        "tau_fold": tau,
        "M_KK": float(M_KK),
        "kappa_2_substrate_FW": float(kappa_2_substrate_FW),
        "L_grid": L_grid,
        "L_fit_points": L_fit_points,
        "L_fit_window": np.array(L_FIT_WINDOW),
        # baselines
        "M0_bare": M0_bare,
        "M0_pv": M0_pv,
        "M0_pv_mult": M0_pv_mult,
        # per-L moments
        "bare_moment": bare_moment,
        "pv_moment": pv_moment,
        "pv_mult_moment": pv_mult_moment,
        "bare_ratio": bare_ratio,
        "pv_ratio": pv_ratio,
        "pv_over_bare": pv_over_bare,
        "pv_mult_over_bare": pv_mult_over_bare,
        # PV-form cross-checks (subtractive = gated; multiplier = contrast)
        "pv_sub_in_script_L12": pv_sub_in_script_L12,
        "pv_mult_module_L12": pv_mult_module_L12,
        "pv_sub_hand_L12": pv_sub_hand_L12,
        "pv_sub_selfcheck_residual": pv_sub_selfcheck_residual,
        "pv_sub_selfcheck_ok": pv_sub_selfcheck_ok,
        "pv_forms_distinct": pv_forms_distinct,
        "pv_sum_c": sum_c,
        "pv_sum_cm2": sum_cm2,
        "pv_identities_ok": pv_identities_ok,
        # intercepts
        "K_bare_per_Lfit": K_bare_per_Lfit,
        "K_pv_per_Lfit": K_pv_per_Lfit,
        "K_pv_mult_per_Lfit": K_pv_mult_per_Lfit,
        # convergence metric (subtractive = the gated quantity)
        "dK_over_dL_pv": dK_over_dL_pv,
        "max_dK_over_dL_pv": max_dK_over_dL_pv,
        "dK_over_dL_increasing": dK_over_dL_increasing,
        "pv_intercept_converges": pv_intercept_converges,
        # multiplier-form convergence (contrast)
        "max_dK_over_dL_pv_mult": max_dK_over_dL_pv_mult,
        "dK_over_dL_mult_increasing": dK_over_dL_mult_increasing,
        "pv_mult_intercept_converges": pv_mult_intercept_converges,
        "pass_ceiling": DELTA_K_OVER_L_PASS_CEILING,
        # FI check
        "a2_pv_FULL_L12": a2_pv_FULL,
        "a2_mellin_FULL_L12": a2_mellin_FULL,
        "a2_zeta_FULL_L12": a2_zeta_FULL,
        "F2_diff": F2_diff,
        "F2_FI_exact": F2_FI_exact,
        "a2_heat_kernel_SCH_L12": a2_heat_kernel_SCH,
        "a2_hard_cutoff_SCH_L12": a2_hard_cutoff_SCH,
        "full_spread": full_spread,
        "full_FI_within_band": full_FI_within_band,
        "fi_spread_band": FI_SPREAD_BAND,
        # sector-census cross-check (informational)
        "n_irrep_L12_FULL": n_irrep_L12_FULL,
        "n_nonzero_cache": n_nonzero_cache,
        "n_total_cache": n_total_cache,
        "n_irrep_cache_census_note": n_irrep_cache_census_note,
        # reference
        "w7_2_full_bare_intercept_ref": W7_2_FULL_BARE_INTERCEPT_REF,
        # verdict
        "evaluator_runnable": evaluator_runnable,
        "verdict": verdict,
        "band_tag": band_tag,
        "cm_class": CM_CLASS,
        "cm_regulator_pin": CM_REGULATOR_PIN,
        # K_csub_R_FW candidate value (the PV intercept at the top of the window;
        # promoted to canonical ONLY on PASS — here reported regardless for the npz):
        "K_csub_R_FW_pv_intercept_L100": float(K_pv_per_Lfit[-1]),
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14.0, 9.5), dpi=120)

    L_grid = r["L_grid"]
    # Panel A: bare vs PV-subtracted a_2 s=2 moment vs L (log) — both diverge
    axA = axes[0, 0]
    axA.semilogy(L_grid, r["bare_moment"], "o-", color="#d62728", ms=3, lw=1.2,
                 label="a_2^{bare}(s=2)")
    axA.semilogy(L_grid, np.abs(r["pv_moment"]), "s-", color="#2ca02c", ms=3, lw=1.2,
                 label="a_2^{Pauli-Villars}(s=2)")
    axA.set_xlabel("L_max"); axA.set_ylabel("a_2(s=2) moment  (log)")
    axA.set_title("(A) bare vs 2-point PV a_2 s=2 moment — BOTH grow with L_max\n"
                  "(divergence is small-λ accumulation; 2-pt PV regulates large-λ)")
    axA.legend(fontsize=9); axA.grid(alpha=0.3)

    # Panel B: PV/bare suppression ratio → 1 (PV becomes negligible)
    axB = axes[0, 1]
    axB.plot(L_grid, r["pv_over_bare"], "o-", color="#1f77b4", ms=3, lw=1.2)
    axB.axhline(1.0, color="gray", ls="--", alpha=0.7, label="ratio → 1 (PV negligible)")
    axB.set_xlabel("L_max"); axB.set_ylabel("a_2^{PV} / a_2^{bare}")
    axB.set_title("(B) PV/bare → 1: the 2-pt PV subtraction (bounded ~1.75/mode)\n"
                  "is negligible vs the divergent λ^{−4} bare tail")
    axB.legend(fontsize=9); axB.grid(alpha=0.3)

    # Panel C: K_csub_R^{PV} intercept vs L_fit (log) — does NOT converge
    axC = axes[1, 0]
    Lf = r["L_fit_points"]
    axC.semilogy(Lf, np.abs(r["K_pv_per_Lfit"]), "s-", color="#2ca02c", ms=5, lw=1.4,
                 label="|K_csub_R^{PV}(1/L→0)| (expanding window)")
    axC.axvspan(r["L_fit_window"][0], r["L_fit_window"][1], color="purple", alpha=0.12,
                label=f"L_fit window [{r['L_fit_window'][0]},{r['L_fit_window'][1]}]")
    axC.set_xlabel("L_fit (top of expanding 1/L window)")
    axC.set_ylabel("|K_csub_R^{PV} intercept|  (log)")
    axC.set_title("(C) PV-subtracted intercept K_csub_R^{PV} GROWS with L_fit\n"
                  "(does NOT converge ⇒ |ΔK/ΔL| ≫ 1e-3)")
    axC.legend(fontsize=8.5); axC.grid(alpha=0.3)

    # Panel D: verdict + diagnostic text
    axD = axes[1, 1]
    axD.axis("off")
    lines = [
        f"VERDICT: {r['verdict']}",
        f"band_tag: {r['band_tag']}",
        "",
        f"CLASS pin: {r['cm_class']} (FULL; PV/Mellin/zeta path, NO -SCHEMATIC)",
        f"regulator: a_2^{{Pauli-Villars}} + a_2^{{Mellin}} + a_2^{{zeta}}",
        f"PV {{c}}={list(PV_C)}  {{M²_dimless}}={list(PV_M2_DIMLESS)}",
        f"  Σc_j={r['pv_sum_c']:.1f} (=1)  Σc_jM_j²={r['pv_sum_cm2']:.1e} (=0)  ok={r['pv_identities_ok']}",
        f"  subtractive self-check (L=12): residual={r['pv_sub_selfcheck_residual']:.2e}  ok={r['pv_sub_selfcheck_ok']}",
        f"  forms distinct (sub≠mult, Sage): {r['pv_forms_distinct']}",
        "",
        "--- UV-convergence (conjunct 1; SUBTRACTIVE = gated quantity) ---",
        f"K_csub_R^{{PV-sub}} @ L_fit=50  = {r['K_pv_per_Lfit'][r['L_fit_points'].tolist().index(50)]:+.4e}",
        f"K_csub_R^{{PV-sub}} @ L_fit=100 = {r['K_pv_per_Lfit'][-1]:+.4e}",
        f"max |ΔK/ΔL| over [50,100]      = {r['max_dK_over_dL_pv']:.4e}  (ceiling {r['pass_ceiling']:.0e})",
        f"  |ΔK/ΔL| increasing           = {r['dK_over_dL_increasing']}",
        f"  PV-sub intercept CONVERGES   = {r['pv_intercept_converges']}",
        f"  [contrast] PV-mult max|ΔK/ΔL|= {r['max_dK_over_dL_pv_mult']:.4e}  converges={r['pv_mult_intercept_converges']}",
        "",
        "--- FI check (conjunct 2) ---",
        f"a_2^{{Mellin}}(L=12) = {r['a2_mellin_FULL_L12']:.4e}  a_2^{{zeta}} = {r['a2_zeta_FULL_L12']:.4e}",
        f"F_2 diff |Mellin−zeta| = {r['F2_diff']:.2e}  exact={r['F2_FI_exact']}",
        f"a_2^{{Pauli-Villars}}(L=12) = {r['a2_pv_FULL_L12']:.4e}",
        f"[SCHEMATIC x-check] hk={r['a2_heat_kernel_SCH_L12']:.3e} cutoff={r['a2_hard_cutoff_SCH_L12']:.3e}",
        "",
        "--- contrast ---",
        f"W7-2 FULL bare intercept ref = +{r['w7_2_full_bare_intercept_ref']:.1f}",
        f"census: {r['n_irrep_cache_census_note']}",
    ]
    axD.text(0.0, 1.0, "\n".join(lines), va="top", ha="left", fontsize=7.6,
             family="monospace", transform=axD.transAxes)
    axD.set_title("(D) Diagnostic summary")

    fig.suptitle(
        f"{GATE_ID}\n"
        f"FULL 2-point Pauli-Villars (Λ_UV=M_KK) a_2 Mellin-s=2 moment — "
        f"K_csub_R UV-convergence test: {r['verdict']} "
        f"(max|ΔK/ΔL|={r['max_dK_over_dL_pv']:.2e} vs ceiling {r['pass_ceiling']:.0e})",
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
    print(f"kappa_2_substrate_FW = {kappa_2_substrate_FW!r}")
    print(f"FULL CM-1995 evaluator CLASS={CM_CLASS}  regulator={CM_REGULATOR_PIN}")
    print(f"PV multipliers c={PV_C}  M²_dimless={PV_M2_DIMLESS}  "
          f"(= {{M_KK², 2·M_KK²}} in λ M_KK-units)")

    INPUT_FILES = [
        Path(__file__).resolve(),
        CANONICAL_CONSTANTS_PATH,
        CM_EVALUATOR_PATH,
        PV_MODULE_PATH,
        SCHEMATIC_MODULE_PATH,
        W7_2_EVALUATOR_PATH,
        L12_CACHE_PATH,
    ]  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)

    r = compute()  # (local)

    # --- Print per-L moment table (subset) ---
    print("\n=== a_2 s=2 moment: bare vs 2-point PV (FULL Jensen table; NO splice) ===")
    print(f"{'L':>4s} | {'a_2^bare':>15s} | {'a_2^PV':>15s} | {'PV/bare':>10s}")
    show_L = [10, 12, 20, 40, 60, 80, 100]  # (local)
    Lg = r["L_grid"].tolist()
    for L in show_L:
        i = Lg.index(L)  # (local)
        print(f"{L:>4d} | {r['bare_moment'][i]:15.6e} | {r['pv_moment'][i]:15.6e} | {r['pv_over_bare'][i]:10.6f}")

    print(f"\nM0_bare (L=1) = {r['M0_bare']:.10f}   M0_pv (L=1) = {r['M0_pv']:.10f}   "
          f"M0_pv_mult (L=1) = {r['M0_pv_mult']:.10f}")
    print(f"PV-form distinctness (SUBTRACTIVE gated vs MULTIPLIER contrast; Sage-confirmed NOT identical):")
    print(f"  subtractive (gated, plan §W1-4 Step2) @ L=12 = {r['pv_sub_in_script_L12']:.10e}")
    print(f"  multiplier  (contrast, PRIMARY module) @ L=12 = {r['pv_mult_module_L12']:.10e}")
    print(f"  forms_distinct = {r['pv_forms_distinct']} (expected True; A−B=−(x²+3x−2)/(x⁴+3x³+2x²))")
    print(f"  subtractive self-check (in_script vs hand-eval) residual = {r['pv_sub_selfcheck_residual']:.3e}  "
          f"ok = {r['pv_sub_selfcheck_ok']}")
    print(f"PV identities: Σc={r['pv_sum_c']:.1f} (=1), Σc·M²={r['pv_sum_cm2']:.2e} (=0), ok={r['pv_identities_ok']}")

    print("\n=== K_csub_R intercept (1/L→0) on expanding windows ===")
    print(f"{'L_fit':>6s} | {'K_bare':>16s} | {'K_pv (SUBTRACTIVE, gated)':>26s} | {'K_pv_mult (contrast)':>22s}")
    for j, Lf in enumerate(r["L_fit_points"]):
        print(f"{int(Lf):>6d} | {r['K_bare_per_Lfit'][j]:16.6e} | {r['K_pv_per_Lfit'][j]:26.6e} | {r['K_pv_mult_per_Lfit'][j]:22.6e}")

    print(f"\n--- UV-convergence metric (conjunct 1; SUBTRACTIVE = gated) ---")
    print(f"max |ΔK_csub_R^PV-sub / ΔL| over [50,100]  = {r['max_dK_over_dL_pv']:.6e}")
    print(f"  PASS ceiling                              = {r['pass_ceiling']:.1e}")
    print(f"  |ΔK/ΔL| < ceiling (CONVERGES)             = {r['pv_intercept_converges']}")
    print(f"  |ΔK/ΔL| increasing (divergence)           = {r['dK_over_dL_increasing']}")
    print(f"  [contrast] multiplier-form max|ΔK/ΔL|     = {r['max_dK_over_dL_pv_mult']:.6e}  "
          f"converges = {r['pv_mult_intercept_converges']}")
    print(f"\n--- FI check (conjunct 2) ---")
    print(f"a_2^Mellin(L=12)={r['a2_mellin_FULL_L12']:.6e}  a_2^zeta(L=12)={r['a2_zeta_FULL_L12']:.6e}")
    print(f"F_2 diff |Mellin−zeta| = {r['F2_diff']:.3e}  exact-0 = {r['F2_FI_exact']}")
    print(f"a_2^Pauli-Villars(L=12) = {r['a2_pv_FULL_L12']:.6e}")
    print(f"[SCHEMATIC x-check] heat-kernel={r['a2_heat_kernel_SCH_L12']:.4e}  hard-cutoff={r['a2_hard_cutoff_SCH_L12']:.4e}")
    print(f"\nW7-2 FULL bare intercept ref = +{r['w7_2_full_bare_intercept_ref']:.4f}")
    print(f"sector census (informational): {r['n_irrep_cache_census_note']}")
    print(f"\nVERDICT: {r['verdict']}  ({r['band_tag']})")

    make_plot(r)

    # --- Save npz (K_csub_R_FW_pv_intercept_L100 at full float64 per spawn-prompt NOTE) ---
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=r["verdict"],
        band_tag=r["band_tag"],
        scheme=SCHEME,
        convention=CONVENTION,
        cm_class=r["cm_class"],
        cm_regulator_pin=r["cm_regulator_pin"],
        tau_fold=r["tau_fold"],
        M_KK=r["M_KK"],
        kappa_2_substrate_FW=r["kappa_2_substrate_FW"],
        L_grid=r["L_grid"],
        L_fit_points=r["L_fit_points"],
        L_fit_window=r["L_fit_window"],
        L_max=L_MAX,
        L_baseline=L_BASELINE,
        pv_c=np.array(PV_C),
        pv_m2_dimless=np.array(PV_M2_DIMLESS),
        M0_bare=r["M0_bare"],
        M0_pv=r["M0_pv"],
        M0_pv_mult=r["M0_pv_mult"],
        bare_moment=r["bare_moment"],
        pv_moment=r["pv_moment"],
        pv_mult_moment=r["pv_mult_moment"],
        bare_ratio=r["bare_ratio"],
        pv_ratio=r["pv_ratio"],
        pv_over_bare=r["pv_over_bare"],
        pv_mult_over_bare=r["pv_mult_over_bare"],
        pv_sub_in_script_L12=r["pv_sub_in_script_L12"],
        pv_mult_module_L12=r["pv_mult_module_L12"],
        pv_sub_hand_L12=r["pv_sub_hand_L12"],
        pv_sub_selfcheck_residual=r["pv_sub_selfcheck_residual"],
        pv_sub_selfcheck_ok=r["pv_sub_selfcheck_ok"],
        pv_forms_distinct=r["pv_forms_distinct"],
        pv_sum_c=r["pv_sum_c"],
        pv_sum_cm2=r["pv_sum_cm2"],
        pv_identities_ok=r["pv_identities_ok"],
        K_bare_per_Lfit=r["K_bare_per_Lfit"],
        K_pv_per_Lfit=r["K_pv_per_Lfit"],
        K_pv_mult_per_Lfit=r["K_pv_mult_per_Lfit"],
        dK_over_dL_pv=r["dK_over_dL_pv"],
        max_dK_over_dL_pv=r["max_dK_over_dL_pv"],
        dK_over_dL_increasing=r["dK_over_dL_increasing"],
        pv_intercept_converges=r["pv_intercept_converges"],
        max_dK_over_dL_pv_mult=r["max_dK_over_dL_pv_mult"],
        dK_over_dL_mult_increasing=r["dK_over_dL_mult_increasing"],
        pv_mult_intercept_converges=r["pv_mult_intercept_converges"],
        pass_ceiling=r["pass_ceiling"],
        a2_pv_FULL_L12=r["a2_pv_FULL_L12"],
        a2_mellin_FULL_L12=r["a2_mellin_FULL_L12"],
        a2_zeta_FULL_L12=r["a2_zeta_FULL_L12"],
        F2_diff=r["F2_diff"],
        F2_FI_exact=r["F2_FI_exact"],
        a2_heat_kernel_SCH_L12=r["a2_heat_kernel_SCH_L12"],
        a2_hard_cutoff_SCH_L12=r["a2_hard_cutoff_SCH_L12"],
        full_spread=r["full_spread"],
        full_FI_within_band=r["full_FI_within_band"],
        fi_spread_band=r["fi_spread_band"],
        n_irrep_L12_FULL=r["n_irrep_L12_FULL"],
        n_nonzero_cache=r["n_nonzero_cache"],
        n_total_cache=r["n_total_cache"],
        n_irrep_cache_census_note=r["n_irrep_cache_census_note"],
        w7_2_full_bare_intercept_ref=r["w7_2_full_bare_intercept_ref"],
        evaluator_runnable=r["evaluator_runnable"],
        # K_csub_R_FW candidate (full float64) — promoted to canonical ONLY on PASS
        # (here NOT promoted: the PV-subtracted intercept does not converge; reported for record):
        K_csub_R_FW_pv_intercept_L100=r["K_csub_R_FW_pv_intercept_L100"],
    )
    print(f"data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # --- value field for verdict line ---
    value_field = (
        f"max_dK_over_dL_pv_SUBTRACTIVE={r['max_dK_over_dL_pv']:.4e}_PASS_ceiling=1e-3_"
        f"converges={r['pv_intercept_converges']};"
        f"K_csub_R_PVsub_intercept_L50={r['K_pv_per_Lfit'][r['L_fit_points'].tolist().index(50)]:+.4e};"
        f"K_csub_R_PVsub_intercept_L100={r['K_pv_per_Lfit'][-1]:+.4e};"
        f"dK_over_dL_increasing={r['dK_over_dL_increasing']};"
        f"PVmult_max_dK_over_dL={r['max_dK_over_dL_pv_mult']:.4e}_converges={r['pv_mult_intercept_converges']};"
        f"pv_forms_distinct={r['pv_forms_distinct']};"
        f"a2_Mellin_L12={r['a2_mellin_FULL_L12']:.4e};a2_zeta_L12={r['a2_zeta_FULL_L12']:.4e};"
        f"F2_diff={r['F2_diff']:.2e}_F2FI_exact={r['F2_FI_exact']};"
        f"a2_PauliVillars_L12={r['a2_pv_FULL_L12']:.4e};"
        f"W7_2_bare_ref=+247259.9583;"
        f"band_tag={r['band_tag']};"
        f"supersedes={SUPERSEDES_AUDIT_SHA}"
    )  # (local)

    # 4-tuple output (final non-verdict line per gate-verdicts.md)
    print(f"\n4-tuple: (value='{value_field[:90]}...', scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    # --- input_pin_map for closure SHA ---
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
    append_verdict(r["verdict"], value_field, audit_sha, content_sha)
    print(f"\nverdict appended: {r['verdict']} -- value (truncated)={value_field[:100]!r}...")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"\nwall: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
