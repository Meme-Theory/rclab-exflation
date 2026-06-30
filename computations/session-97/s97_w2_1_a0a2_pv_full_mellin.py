#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S97-W2-1-A0A2-PV-FULL-MELLIN  —  clean Seeley-DeWitt CC-ratio a_0^PV/a_2^PV via the
FULL analytic-continuation Mellin evaluator with FULL physical Pauli-Villars subtraction.

Gate: S97-W2-1-A0A2-PV-FULL-MELLIN  (session-97, wave 2, gate 1; lizzi-spectral-functional-theorist)
Plan: sessions/session-plan/session-97-plan-w2.md  §W2-1
Trigger: [VERIFY]  (schema_v2_3tuple_required=false — NO [SIGN] 3-tuple row)
Classification: GEOMETRIC

WHAT THIS DOES (object-definedness axis — DI1 SCOPE)
----------------------------------------------------
Recompute a_0^PV and a_2^PV on the substrate's intrinsic D_K^2 spectrum using the FULL
off-pole analytic-continuation Mellin evaluator analytic_zeta(s, L_max) (the exact
Mellin<->Dirichlet heat-kernel integral, mp.dps=50), then apply FULL PHYSICAL Pauli-
Villars subtraction with coefficient set {c_j}={2,-1} and mass set {m_j^2/M_KK^2}={1,2}
at Lambda_UV=M_KK. Form the dimensionless CC-ratio a_0^PV/a_2^PV and the schematic-
normalized form f0/f2 (f_n := a_n^PV/a_n^zeta) and compare f2/f0 to the schematic-Gilkey
cross-check f2/f0=0.6314 carried by the S96 CC-GAP canonical line da899b4d... .

PASS  <=> |(a_0^PV/a_2^PV) ... ] normalized residual| < 0.10 (object well-DEFINED).
FAIL  <=> residual > 1 OOM (the schematic 0.6314 was a Gilkey-normalization artifact;
          the FULL physical PV diverges — S94 absolute-divergence signature).
INFO  <=> 0.10 <= residual <= 1 OOM (FI-WITHIN the analytic-continuation family but
          functional-DEPENDENT across the PV subtraction).

DI1: this tests OBJECT-DEFINEDNESS of a_2/a_0 ONLY. A FAIL here retracts NEITHER the
§8.5 tier-2 survival NOR the CC closure (those rest on the FI-WITHIN-family ratio per
the da899b4d... line, on a separate axis). It shares NO inputs with gate 2.2 (q-flow
C10 n-exponent) and MUST NOT be conflated.

CRITICAL (CLASS=FULL): this script implements its OWN FULL physical PV subtraction on top
of analytic_zeta. It MUST NOT import _spectral_action_regulators.py::pauli_villars_a_n
(that helper's docstring line 26 self-identifies as "NOT the full physical regularizations"
— it uses M_PV^2 = fraction x Casimir-ceiling, NOT the physical {1,2} mass set). The
schematic helper output (f2/f0=0.6314) is the CROSS-CHECK baseline, NOT the canonical
replacement. No -SCHEMATIC convention suffix; no tier_pin=TIER-2 row.

SUBSTRATE-FIRST FRAMING (phononic-framing.md)
---------------------------------------------
GEOMETRIC. The cosmological constant IS the spectral-action zeroth moment a_0 — a
DIFFERENT spectral moment of D_K than gravity (the second moment a_2). The chain:
  D_K eigenvalues {lambda_k, m_k} on the L_max-truncated finite spectral triple
    -> Mellin moments a_n^Mellin(s_n) = sum_k m_k lambda_k^{-s_n} (exact Mellin<->Dirichlet)
    -> physical Pauli-Villars-subtracted moments a_n^PV
    -> the dimensionless CC-ratio a_0/a_2.
The lizzi signature question: does the choice of regulator WITHIN the FULL analytic-
continuation/physical-PV family produce a well-DEFINED ratio, or does it depend on the
(schematic-Gilkey direct-power-sum vs full-Mellin physical-PV) scheme? What is functional-
INDEPENDENT across the family is structural (object atlas-defined); what is functional-
DEPENDENT requires determination. The schematic-Gilkey f2/f0=0.6314 is the laboratory-IN
cross-check; the FULL Mellin/physical-PV a_0^PV/a_2^PV is the substrate-IS object. The
direction of explanation flows FROM the substrate Mellin moments TOWARD the CC-ratio
observable, never inverted.

SUBSTITUTION CHAIN (math-scripts.md §"Double-Check Logic Before Compute")
-------------------------------------------------------------------------
Claim: "If the FULL physical PV/Mellin evaluation gives a_0^PV/a_2^PV within 10% of the
        schematic cross-check (in the f2/f0=0.6314 normalized form), the a_2/a_0 regulator-
        atlas object is well-DEFINED; if it diverges by >1 OOM, the schematic 0.6314 was a
        Gilkey-normalization artifact."
 Def 1: a_n^Mellin(s_n, L) = analytic_zeta(s_n, L) = sum_k m_k lambda_k^{-s_n}  (exact
        Mellin<->Dirichlet, _analytic_zeta.py lines 184-258; verified rel_dev=0 vs direct
        power-sum at s=6,8). Conv. A double-power labeling poles at s=(d-n)/2, d=8:
        a_0 <-> pole_in_s=4 (curvature-grade n=0) <-> Dirichlet exponent -8 = -2*4;
        a_2 <-> pole_in_s=3 (curvature-grade n=2) <-> Dirichlet exponent -6 = -2*3.
        => evaluate analytic_zeta(8) for a_0, analytic_zeta(6) for a_2.
        [source: _analytic_zeta.py + regulator-pin-discipline.md Mellin pole-set labeling;
         {0,2,4,6,8} is ALWAYS the curvature-grade n, the s-pole set under Conv. A is {4,3,2,1,0}]
 Def 2: a_n^PV(L) = full physical Pauli-Villars subtraction of a_n^Mellin:
        a_n^PV = a_n^Mellin(s_n) - sum_j c_j * a_n^{Mellin,shifted}(s_n; m_j^2),
        with {c_j}={2,-1}, {m_j^2/M_KK^2}={1,2}, Lambda_UV=M_KK. The PV mass shift enters
        the heat kernel as exp(-(lambda^2+m_j^2) t); at Dirichlet exponent -s_n in lambda
        this is exponent -s_n/2 in lambda^2, so the shifted moment is
        sum_k m_k (lambda_k^2 + m_j^2)^{-s_n/2} = analytic_zeta_shifted(s_n; m_j^2).
        [source: this gate's machinery_pin_map; physical PV set, NOT the schematic
         Casimir-fraction set]
 Def 3: schematic-Gilkey cross-check (direct-power-sum PV, S96 pv_ratio_cancellation):
        f0_sch = a_0^PV/a_0^zeta = 0.7885 ; f2_sch = a_2^PV/a_2^zeta = 0.4979 ;
        f2_sch/f0_sch = 0.4979/0.7885 = 0.6314.
        [source: S96 CC-GAP canonical line da899b4d... value field:
         partB_FI_across_PV=False_PVshift=36.86pct_f0=0.7885_f2=0.4979_f2overf0=0.6314]
 Sub : f0_Mellin := a_0^PV/a_0^zeta  via the FULL Mellin route (a_0^zeta = analytic_zeta(8));
        f2_Mellin := a_2^PV/a_2^zeta  via the FULL Mellin route (a_2^zeta = analytic_zeta(6));
        target normalized ratio = f2_Mellin/f0_Mellin; absolute ratio = a_0^PV/a_2^PV.
 Simp: residual_norm = |(f2_Mellin/f0_Mellin) - 0.6314| / 0.6314.
        IF the FULL physical PV reproduces the schematic direct-power-sum f0,f2
        => f2_Mellin/f0_Mellin -> 0.6314 => residual_norm -> 0, PASS.
 Dir : IF the FULL PV diverges (a_2^PV -> 0 OR a_0^PV blows up under the physical {1,2}
        mass set — the S94 absolute-divergence signature) => residual > 1 OOM, FAIL.
 Concl: PASS <=> a_2/a_0 object is regulator-atlas well-DEFINED across the FULL analytic-
        continuation/PV family; FAIL <=> the schematic 0.6314 was a Gilkey-normalization
        artifact, the object is NOT atlas-defined. DI1: object-definedness axis ONLY.

ENV: phonon-exflation-sim/.venv312/Scripts/python.exe ; analytic_zeta Mellin quadrature is
     mp.dps=50 CPU-bound (~tens of s per s-pole, 2 poles x (1 unsubtracted + 2 PV) terms);
     heat-kernel K(t) accumulation uses torch GPU per the analytic_zeta module.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")      # (local) cap CPU threads; mp.quad is CPU-bound
os.environ.setdefault("MKL_NUM_THREADS", "8")      # (local)

import sys
import json
import math
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import mpmath as mpm
from mpmath import mp, mpc

# --- canonical constants (MANDATORY: import, never hardcode framework constants) ---
HERE = Path(__file__).resolve().parent                              # (local) computations/session-97
SHARED = HERE.parent / "_shared"                                    # (local) computations/_shared
PROJECT_ROOT = HERE.parent.parent                                   # (local) repo root
sys.path.insert(0, str(SHARED))

from canonical_constants import (   # noqa: E402
    a_0_FW_zeta,     # 6440.0      zeta-regulated a_0 (= zeta_{D_K}(0) = Tr(1))   (S88)
    a_2_FW_zeta,     # 2776.165389 zeta-regulated a_2                            (S88)
    M_KK,            # 7.428660036284456e16 GeV  (alias M_KK_gravity, S42)
    tau_fold,        # 0.19        Jensen fold slice (S42 CONST-FREEZE-42)
)

# Mellin-cone evaluator (FULL — _analytic_zeta.py per plan CLASS=FULL). NOTE: we do NOT
# import _spectral_action_regulators.py::pauli_villars_a_n (SCHEMATIC). Our PV is FULL.
import _analytic_zeta as _az  # noqa: E402
from _analytic_zeta import analytic_zeta, zeta_D_direct, load_spectrum  # noqa: E402

# --- RUNTIME CANONICAL-PATH CORRECTION (substrate-first-canonical-sourcing.md §(ii.B)) ---
# The _shared/ copy of _analytic_zeta.py resolves its SPECTRUM_CACHE via the X2-transform
# resolve_output(84, ...) to a path that does NOT exist for the _shared/ copy (infra resolver
# drift). Correct the module cache path to the canonical session-84 master spectrum so the
# FULL Mellin-cone evaluator runs on the correct spectrum. Infra-path correction (documented
# per §(ii.B)), NOT a convention/scheme change: the FULL evaluator math is untouched (CLASS=FULL).
_CORRECT_CACHE = (PROJECT_ROOT / "computations" / "session-84"
                  / "s84_spectrum_cache_L12_tau019.npz")            # (local) canonical session-84 cache
_AZ_CACHE_PATH_CORRECTED = False                                    # (local)
if not _az.SPECTRUM_CACHE.exists() and _CORRECT_CACHE.exists():
    _az.SPECTRUM_CACHE = _CORRECT_CACHE
    _az._SPEC_CACHE.clear()
    _az._HK_TENSOR_CACHE.clear()
    _AZ_CACHE_PATH_CORRECTED = True


# ============================================================
# SECTION 0: Identifiers, paths, thresholds
# ============================================================
GATE_ID = "S97-W2-1-A0A2-PV-FULL-MELLIN"                            # (local)
SCHEME = "FULL-MELLIN-ANALYTIC-CONTINUATION-plus-FULL-PV"           # (local) plan scheme tag
CONVENTION = "RATIO-a0PV-over-a2PV-poleconv-A-double"               # (local) plan convention (Conv.A double-power)
L_MAX = "10"                                                        # (local) canonical analytic_zeta L_max; x-check at L=12

# Pre-registered thresholds (plan operator / strict_PASS_boundary)
SCHEMATIC_TARGET = 0.6314                                           # (local) schematic-Gilkey f2/f0 cross-check (da899b4d)
OBJECT_DEF_BAND = 0.10                                              # (local) object-definedness band: |residual_norm| <= 0.10 => PASS
DIVERGENCE_OOM = 1.0                                                # (local) FAIL boundary: residual > 1 OOM => Gilkey-norm artifact
ABS_TOL = 1e-10                                                     # (local) float64 absolute tolerance
D_SPEC_NCG = 8                                                      # (local) NCG dimension-spectrum (d=8 cone labeling)

# FULL physical Pauli-Villars set (NOT the schematic Casimir-fraction set):
PV_C = [2.0, -1.0]                                                  # (local) {c_j} physical PV coefficients
PV_M2_DIMLESS = [1.0, 2.0]                                          # (local) {m_j^2/M_KK^2} physical PV mass set (M_KK^2 units)
# Lambda_UV = M_KK (imported). lambda on the cache is already in M_KK units, so m_j^2 add directly to lambda^2.

# Conv. A double-power pole indices -> Dirichlet exponents in lambda (single-power-in-s arg to analytic_zeta):
S_POLE_A0_CONVA = 4                                                 # (local) a_0: pole_in_s=4 (curvature_grade n=0)
S_POLE_A2_CONVA = 3                                                 # (local) a_2: pole_in_s=3 (curvature_grade n=2)
DIRICHLET_EXP_A0 = 2 * S_POLE_A0_CONVA                             # (local) = 8  (lambda^-8) = analytic_zeta arg for a_0
DIRICHLET_EXP_A2 = 2 * S_POLE_A2_CONVA                             # (local) = 6  (lambda^-6) = analytic_zeta arg for a_2

PUB_PRECISION = 6                                                   # (local) a_0^PV/a_2^PV cited downstream; 6 sig figs

SCRIPT_PATH = Path(__file__).resolve()                             # (local)
CANONICAL_PY = SHARED / "canonical_constants.py"                   # (local)
ANALYTIC_ZETA_PY = SHARED / "_analytic_zeta.py"                    # (local)
SPECTRUM_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
S96_VERDICTS = PROJECT_ROOT / "computations" / "session-96" / "s96_gate_verdicts.txt"  # (local) da899b4d cross-check host
NPZ_PATH = HERE / "s97_w2_1_a0a2_pv_full_mellin.npz"               # (local)
PNG_PATH = HERE / "s97_w2_1_a0a2_pv_full_mellin.png"              # (local)
VERDICT_TXT = HERE / "s97_gate_verdicts.txt"                       # (local) CANONICAL path per gate-verdicts.md

# Plan-pinned input SHAs (Input-SHA Ledger). canonical_constants.py drifted between plan-freeze
# (cc7d1d26...) and runtime (838c7145...) — Class-(c) PIN-DRIFT-FROM-STALE-SOURCE; the values we
# consume (a_0_FW_zeta=6440.0, a_2_FW_zeta=2776.165389, M_KK) are knowledge-MCP-canonical and
# non-superseded, so the drift is content-edit-only, not a convention change. We pin the
# runtime-actual SHA and document the drift (substrate-first-canonical-sourcing.md §(ii.B)).
PLAN_PIN_SHA = {                                                    # (local) plan Input-SHA Ledger
    "computations/_shared/_analytic_zeta.py": "6383c87717c17040f596264a2e33cdc630089fb750681ab2eb149e934d84f660",
    "computations/session-84/s84_spectrum_cache_L12_tau019.npz": "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9",
    "computations/session-96/s96_gate_verdicts.txt": "0ff68a9589b50cb0519ad240aea8d9a3d10f95d4cf4302fdac25fde559038186",
    "computations/_shared/canonical_constants.py": "cc7d1d26a789311e34a11c221ff625096a91889f1c12e53d39b16a6adc4d972a",
}


# ============================================================
# SECTION 1: dual-SHA helpers (S84+ schema)
#   audit_sha256_inputs (plan) = [script, analytic_zeta_module, s84_spectrum_cache,
#                                 s96_ccgap_verdict_line, canonical, pinmap]
#   content_sha256_inputs = [script]
# ============================================================
def sha256_of(path: Path) -> str:                                  # (local)
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:                               # (local)
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                        # (local)
        try:
            rel = str(Path(p).relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)                                          # (local)
        plan_sha = PLAN_PIN_SHA.get(rel)                          # (local)
        drift = "" if (plan_sha is None or plan_sha == sha) else f"  [PIN-DRIFT vs plan {plan_sha[:16]}...]"  # (local)
        print(f"  {rel}: {sha[:16]}...{drift}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:                             # (local)
    items = sorted(pins.items())                                  # (local)
    h = hashlib.sha256()                                          # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(audit_input_paths, pins: dict):              # (local)
    """audit_sha256 = sha256( bytes(script||analytic_zeta||s84_cache||s96_verdicts||canonical)
                              || bytes(pinmap_json) );
       content_sha256 = sha256( bytes(script) )."""
    h_audit = hashlib.sha256()                                    # (local)
    for p in audit_input_paths:
        try:
            h_audit.update(Path(p).read_bytes())
        except OSError:
            h_audit.update(b"")
    pinmap_json = json.dumps(                                     # (local)
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                   # (local)

    h_content = hashlib.sha256()                                  # (local)
    try:
        h_content.update(Path(SCRIPT_PATH).read_bytes())
    except OSError:
        h_content.update(b"")
    content = h_content.hexdigest()                               # (local)
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:  # (local)
    """Atomic append (single open('a')) of the dual-SHA verdict to the CANONICAL verdict file.
       APPEND ONLY (Wave 1 already wrote 5 gates + a 1.3 supersedes chain). No supersedes tag
       (this is a fresh gate-ID, first emission)."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] object-definedness a_0^PV/a_2^PV vs "
        f"schematic f2/f0=0.6314; CLASS=FULL (no -SCHEMATIC, no tier_pin); "
        f"no [SIGN] 3-tuple (schema_v2_3tuple_required=false)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ============================================================
# SECTION 2: FULL Mellin moments + FULL physical PV subtraction
# ============================================================
print("=" * 78)
print(f"{GATE_ID}  (clean SDW CC-ratio a_0^PV/a_2^PV via FULL Mellin + FULL physical PV)")
print("=" * 78)
print(f"\n[SEC 2] _analytic_zeta cache-path correction (infra resolver drift, §(ii.B)): "
      f"corrected={_AZ_CACHE_PATH_CORRECTED}; module cache -> {_az.SPECTRUM_CACHE.name}")
print(f"[SEC 2] tau_fold={tau_fold}  M_KK={M_KK:.6e} GeV (Lambda_UV)  d_spec={D_SPEC_NCG}")
print(f"[SEC 2] zeta anchors: a_0_FW_zeta={a_0_FW_zeta}  a_2_FW_zeta={a_2_FW_zeta}  "
      f"a_2/a_0(zeta-FW)={a_2_FW_zeta/a_0_FW_zeta:.8f}  a_0/a_2(zeta-FW)={a_0_FW_zeta/a_2_FW_zeta:.8f}")
print(f"[SEC 2] Conv. A double-power: a_0 (pole_in_s={S_POLE_A0_CONVA}, n=0) -> lambda^-{DIRICHLET_EXP_A0}; "
      f"a_2 (pole_in_s={S_POLE_A2_CONVA}, n=2) -> lambda^-{DIRICHLET_EXP_A2}")
print(f"[SEC 2] FULL physical PV: c_j={PV_C}  m_j^2/M_KK^2={PV_M2_DIMLESS}  (NOT schematic Casimir-fraction)")


def mellin_moment_shifted(dirichlet_exp_lambda: float, L_max: int, m2_shift: float) -> float:
    """FULL Mellin-route moment with a heat-kernel mass shift m2_shift (in M_KK^2 units).

       Unshifted (m2_shift=0) reproduces analytic_zeta(dirichlet_exp_lambda) =
       sum_k m_k lambda_k^{-dirichlet_exp} (exact Mellin<->Dirichlet; verified rel_dev=0).

       Mass-shifted: the PV regulator field of mass m_j enters the heat kernel as
       K_shift(t) = sum_k m_k exp(-(lambda_k^2 + m2_shift) t) = exp(-m2_shift t) * K(t),
       and the Mellin<->Dirichlet identity gives
         sum_k m_k (lambda_k^2 + m2_shift)^{-s/2} * Gamma(s/2)
           = int_0^inf t^(s/2-1) exp(-m2_shift t) K(t) dt
       with s = dirichlet_exp_lambda (the lambda-power), s/2 the lambda^2-power.
       We evaluate via mp.quad on the GPU heat kernel (CLASS=FULL, mp.dps=50)."""
    s = mpc(float(dirichlet_exp_lambda))                          # (local) lambda-power
    half_s = s / 2                                                # (local) lambda^2-power
    hk = _az._heat_kernel_gpu_factory(L_max)                     # (local) GPU K(t) on the corrected cache

    if abs(float(m2_shift)) < 1e-300:
        # Unshifted: defer to the module's canonical off-pole evaluator (s in {8,6} is off {2,4}).
        return float(_az.analytic_zeta(float(dirichlet_exp_lambda) + 0j, L_max).real)

    def integrand(t):
        try:
            tt = float(t)
        except (TypeError, ValueError):
            tt = float(mpm.mpf(t))
        if tt <= 0.0:
            return mpm.mpf(0)
        # exp(-m2_shift t) damps the small-t (lambda~0) part; K(t) decays at large t.
        damp = mpm.e ** (-mpm.mpf(float(m2_shift)) * mpm.mpf(tt))  # (local) exp(-m2 t)
        K_val = hk(tt)                                            # (local) sum_k m_k exp(-lambda^2 t) on GPU
        return mpm.power(t, half_s - 1) * damp * mpm.mpf(K_val)

    # Split [0,1] (small-t, integrable t^(s/2-1)) and [1, inf] (large-t exp decay).
    I1 = mp.quad(integrand, [0, 1])                              # (local)
    I2 = mp.quad(integrand, [1, mp.inf])                         # (local)
    val = (I1 + I2) / mpm.gamma(half_s)                          # (local)
    return float(complex(val).real)


def mellin_moment_pv(dirichlet_exp_lambda: float, L_max: int):
    """FULL physical Pauli-Villars-subtracted Mellin moment:
         a_n^PV = a_n^Mellin(s_n) - sum_j c_j * a_n^{Mellin,shifted}(s_n; m_j^2)
       with {c_j}={2,-1}, {m_j^2/M_KK^2}={1,2}, Lambda_UV=M_KK.
       Returns (a_n^zeta=Mellin-unshifted, a_n^PV, [shifted terms])."""
    a_zeta = mellin_moment_shifted(dirichlet_exp_lambda, L_max, 0.0)   # (local) unsubtracted = a_n^zeta(=Mellin)
    a_pv = a_zeta                                                      # (local)
    shifted = []                                                       # (local)
    for c, m2 in zip(PV_C, PV_M2_DIMLESS):
        a_shift = mellin_moment_shifted(dirichlet_exp_lambda, L_max, m2)  # (local)
        a_pv -= c * a_shift
        shifted.append((c, m2, a_shift))
    return a_zeta, a_pv, shifted


# Cross-check: the unshifted Mellin moment MUST equal the direct power-sum (rel_dev ~ 0).
evs10, mults10 = load_spectrum(10)                                # (local)
a0_directsum = float(np.sum(mults10 * evs10 ** (-float(DIRICHLET_EXP_A0))))  # (local) sum m_k lambda^-8
a2_directsum = float(np.sum(mults10 * evs10 ** (-float(DIRICHLET_EXP_A2))))  # (local) sum m_k lambda^-6

print("\n[SEC 2] FULL Mellin moments at L_max=10 (a_0^zeta=Mellin unshifted; PV-subtracted):")
a0_zeta, a0_pv, a0_shifted = mellin_moment_pv(DIRICHLET_EXP_A0, 10)
a2_zeta, a2_pv, a2_shifted = mellin_moment_pv(DIRICHLET_EXP_A2, 10)

a0_mellin_vs_direct = abs(a0_zeta - a0_directsum) / abs(a0_directsum)  # (local)
a2_mellin_vs_direct = abs(a2_zeta - a2_directsum) / abs(a2_directsum)  # (local)
print(f"  a_0^Mellin(unshifted, s=8) = {a0_zeta:.10e}   direct sum lambda^-8 = {a0_directsum:.10e}   "
      f"rel_dev={a0_mellin_vs_direct:.3e}")
print(f"  a_2^Mellin(unshifted, s=6) = {a2_zeta:.10e}   direct sum lambda^-6 = {a2_directsum:.10e}   "
      f"rel_dev={a2_mellin_vs_direct:.3e}")
for tag, sh in (("a_0", a0_shifted), ("a_2", a2_shifted)):
    for c, m2, a_s in sh:
        print(f"    {tag} PV-shifted term c={c:+.1f} m^2={m2:.1f}: a_shift={a_s:.10e}")
print(f"  a_0^PV = a_0^Mellin - sum_j c_j a_shift_j = {a0_pv:.10e}")
print(f"  a_2^PV = a_2^Mellin - sum_j c_j a_shift_j = {a2_pv:.10e}")


# ============================================================
# SECTION 3: CC-ratio (absolute + schematic-normalized) + comparison to 0.6314
#   (Mnemonic-vs-exact discipline, math-scripts.md: report BOTH forms apples-to-apples)
# ============================================================
print("\n" + "=" * 78)
print("[SEC 3] CC-ratio object: absolute a_0^PV/a_2^PV AND schematic-normalized f2/f0 vs 0.6314")
print("=" * 78)

# ABSOLUTE ratio (the substrate-IS object this gate's literal title names):
R_CC_PV_abs = a0_pv / a2_pv                                       # (local) a_0^PV / a_2^PV (direct Mellin/PV object)
R_CC_zeta_abs = a0_zeta / a2_zeta                                 # (local) a_0^zeta / a_2^zeta (unsubtracted Mellin) cross-ref

# SCHEMATIC-NORMALIZED form (apples-to-apples vs the da899b4d f0/f2 split):
#   f_n = a_n^PV / a_n^zeta  (the per-coefficient PV factor, same definition as S96 f0,f2);
#   schematic cross-check compares f2/f0 to 0.6314 (= f2_sch/f0_sch = 0.4979/0.7885).
f0_mellin = a0_pv / a0_zeta                                       # (local) a_0^PV/a_0^zeta via FULL Mellin
f2_mellin = a2_pv / a2_zeta                                       # (local) a_2^PV/a_2^zeta via FULL Mellin
f2_over_f0_mellin = f2_mellin / f0_mellin                         # (local) the schematic-normalized comparison object

# Schematic-Gilkey baseline carried by da899b4d (direct-power-sum PV; S96 pv_ratio_cancellation):
F0_SCH = 0.7885                                                   # (local) da899b4d f0
F2_SCH = 0.4979                                                   # (local) da899b4d f2
F2_OVER_F0_SCH = F2_SCH / F0_SCH                                  # (local) = 0.6314 (the cross-check target)

# Normalized residual (the gate's literal operator |(...)-0.6314|/0.6314):
residual_norm = abs(f2_over_f0_mellin - SCHEMATIC_TARGET) / SCHEMATIC_TARGET   # (local)
# OOM of the residual relative to target (FAIL boundary at > 1 OOM):
residual_OOM = abs(math.log10(f2_over_f0_mellin / SCHEMATIC_TARGET)) if f2_over_f0_mellin > 0 else float("inf")  # (local)

# Divergence cross-check: did a_2^PV collapse toward 0 or a_0^PV blow up under physical {1,2}?
a2_pv_collapsed = bool(abs(a2_pv) < ABS_TOL or (abs(a2_pv) < 1e-3 * abs(a2_zeta)))  # (local)
a0_pv_blew_up = bool(abs(a0_pv) > 1e3 * abs(a0_zeta))            # (local)
divergence_signature = bool(a2_pv_collapsed or a0_pv_blew_up or residual_OOM > DIVERGENCE_OOM)  # (local)

print(f"  ABSOLUTE  a_0^PV/a_2^PV       = {R_CC_PV_abs:.{PUB_PRECISION}f}   "
      f"(cross-ref a_0^zeta/a_2^zeta = {R_CC_zeta_abs:.{PUB_PRECISION}f})")
print(f"  PV factors via FULL Mellin:    f0_Mellin=a_0^PV/a_0^zeta={f0_mellin:.6f}  "
      f"f2_Mellin=a_2^PV/a_2^zeta={f2_mellin:.6f}")
print(f"  schematic-normalized f2/f0     = {f2_over_f0_mellin:.6f}   "
      f"(schematic-Gilkey target f2/f0={F2_OVER_F0_SCH:.4f} = {F2_SCH}/{F0_SCH})")
print(f"  [schematic baseline (da899b4d direct-power-sum PV): f0={F0_SCH} f2={F2_SCH} f2/f0={F2_OVER_F0_SCH:.4f}]")
print(f"\n  NORMALIZED RESIDUAL |(f2/f0)_Mellin - {SCHEMATIC_TARGET}|/{SCHEMATIC_TARGET} = {residual_norm:.6f}  "
      f"(object-defined band <= {OBJECT_DEF_BAND})")
print(f"  residual OOM |log10((f2/f0)_Mellin / {SCHEMATIC_TARGET})| = {residual_OOM:.6f}  "
      f"(divergence/artifact FAIL boundary > {DIVERGENCE_OOM} OOM)")
print(f"  divergence cross-check: a_2^PV_collapsed={a2_pv_collapsed}  a_0^PV_blew_up={a0_pv_blew_up}  "
      f"=> S94-divergence-signature={divergence_signature}")


# ============================================================
# SECTION 4: L_max=12 truncation-stability cross-check (analytic_zeta docstring)
# ============================================================
print("\n" + "=" * 78)
print("[SEC 4] Truncation-stability cross-check at L_max=12 (analytic_zeta docstring)")
print("=" * 78)
a0_zeta_12, a0_pv_12, _ = mellin_moment_pv(DIRICHLET_EXP_A0, 12)
a2_zeta_12, a2_pv_12, _ = mellin_moment_pv(DIRICHLET_EXP_A2, 12)
f0_mellin_12 = a0_pv_12 / a0_zeta_12                              # (local)
f2_mellin_12 = a2_pv_12 / a2_zeta_12                              # (local)
f2_over_f0_mellin_12 = f2_mellin_12 / f0_mellin_12               # (local)
R_CC_PV_abs_12 = a0_pv_12 / a2_pv_12                             # (local)
Lmax_drift_ratio = abs(R_CC_PV_abs_12 - R_CC_PV_abs) / abs(R_CC_PV_abs)        # (local) abs-ratio L10->L12 drift
Lmax_drift_f2f0 = abs(f2_over_f0_mellin_12 - f2_over_f0_mellin) / abs(f2_over_f0_mellin)  # (local) norm-form drift
print(f"  L=12: a_0^PV/a_2^PV={R_CC_PV_abs_12:.6f}  (f2/f0)_Mellin={f2_over_f0_mellin_12:.6f}")
print(f"  L10->L12 drift: absolute-ratio={Lmax_drift_ratio*100:.3f}%  f2/f0-form={Lmax_drift_f2f0*100:.3f}%")


# ============================================================
# SECTION 5: VERDICT (object-definedness rubric)
# ============================================================
print("\n" + "=" * 78)
print("[SEC 5] VERDICT — object-definedness of a_2/a_0 across FULL analytic-continuation/PV family")
print("=" * 78)

# Rubric (plan operator + PASS/FAIL/INFO meaning):
#   PASS : residual_norm < 0.10                       -> object well-DEFINED (clean SDW ratio)
#   FAIL : residual_OOM > 1.0 (or divergence sig)     -> schematic 0.6314 was Gilkey-norm artifact
#   INFO : 0.10 <= residual_norm AND residual_OOM<=1  -> FI-WITHIN family, functional-DEPENDENT across PV
if divergence_signature or residual_OOM > DIVERGENCE_OOM:
    verdict = "FAIL"                                             # (local)
    outcome = "FULL_PV_DIVERGES_SCHEMATIC_0p6314_IS_GILKEY_NORMALIZATION_ARTIFACT"  # (local)
elif residual_norm < OBJECT_DEF_BAND:
    verdict = "PASS"                                             # (local)
    outcome = "A2_OVER_A0_OBJECT_WELL_DEFINED_FULL_MELLIN_PV_REPRODUCES_SCHEMATIC"  # (local)
else:
    verdict = "INFO"                                             # (local)
    outcome = "OBJECT_FI_WITHIN_ANALYTIC_CONTINUATION_FAMILY_FUNCTIONAL_DEPENDENT_ACROSS_PV"  # (local)

# DI1 scope pin (object-definedness ONLY; does NOT touch §8.5 tier-2 nor CC closure):
DI1_SCOPE = ("OBJECT-DEFINEDNESS-AXIS-ONLY; does-NOT-establish-or-retract-§8.5-tier-2-survival; "
             "does-NOT-establish-or-retract-CC-closure; shares-NO-inputs-with-gate-2.2-q-flow")  # (local)

print(f"  residual_norm = {residual_norm:.6f} (band {OBJECT_DEF_BAND})  residual_OOM = {residual_OOM:.6f} "
      f"(FAIL > {DIVERGENCE_OOM})  divergence_sig = {divergence_signature}")
print(f"  OUTCOME = {outcome}")
print(f"  VERDICT = {verdict}")
print(f"  DI1 SCOPE: {DI1_SCOPE}")


# ============================================================
# SECTION 6: persist npz + png
# ============================================================
np.savez(
    NPZ_PATH,
    gate_id=GATE_ID,
    verdict=str(verdict),
    outcome=str(outcome),
    di1_scope=str(DI1_SCOPE),
    scheme=str(SCHEME),
    convention=str(CONVENTION),
    L_max=int(10),
    tau_fold=float(tau_fold),
    M_KK=float(M_KK),
    Lambda_UV=float(M_KK),
    d_spec_ncg=int(D_SPEC_NCG),
    # Conv. A pole labeling
    s_pole_a0_convA=int(S_POLE_A0_CONVA),
    s_pole_a2_convA=int(S_POLE_A2_CONVA),
    dirichlet_exp_a0=int(DIRICHLET_EXP_A0),
    dirichlet_exp_a2=int(DIRICHLET_EXP_A2),
    # FULL physical PV set
    pv_c=np.array(PV_C),
    pv_m2_dimless=np.array(PV_M2_DIMLESS),
    # zeta anchors
    a_0_FW_zeta=float(a_0_FW_zeta),
    a_2_FW_zeta=float(a_2_FW_zeta),
    # FULL Mellin moments @ L=10
    a0_zeta_mellin=float(a0_zeta),
    a2_zeta_mellin=float(a2_zeta),
    a0_pv=float(a0_pv),
    a2_pv=float(a2_pv),
    a0_directsum=float(a0_directsum),
    a2_directsum=float(a2_directsum),
    a0_mellin_vs_direct_reldev=float(a0_mellin_vs_direct),
    a2_mellin_vs_direct_reldev=float(a2_mellin_vs_direct),
    # ratios + comparison
    R_CC_PV_abs=float(R_CC_PV_abs),
    R_CC_zeta_abs=float(R_CC_zeta_abs),
    f0_mellin=float(f0_mellin),
    f2_mellin=float(f2_mellin),
    f2_over_f0_mellin=float(f2_over_f0_mellin),
    # schematic cross-check (da899b4d)
    f0_schematic=float(F0_SCH),
    f2_schematic=float(F2_SCH),
    f2_over_f0_schematic=float(F2_OVER_F0_SCH),
    schematic_target=float(SCHEMATIC_TARGET),
    # residual + bands
    residual_norm=float(residual_norm),
    residual_OOM=float(residual_OOM),
    object_def_band=float(OBJECT_DEF_BAND),
    divergence_OOM=float(DIVERGENCE_OOM),
    a2_pv_collapsed=bool(a2_pv_collapsed),
    a0_pv_blew_up=bool(a0_pv_blew_up),
    divergence_signature=bool(divergence_signature),
    # L=12 cross-check
    a0_pv_L12=float(a0_pv_12),
    a2_pv_L12=float(a2_pv_12),
    R_CC_PV_abs_L12=float(R_CC_PV_abs_12),
    f2_over_f0_mellin_L12=float(f2_over_f0_mellin_12),
    Lmax_drift_ratio=float(Lmax_drift_ratio),
    Lmax_drift_f2f0=float(Lmax_drift_f2f0),
    az_cache_path_corrected=bool(_AZ_CACHE_PATH_CORRECTED),
)
print(f"\n[SEC 6] npz -> {NPZ_PATH}")

# --- plot: PV factors f0/f2 (left, Mellin vs schematic) + ratio bar (right) ---
fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.5, 4.8))

# Left: per-coefficient PV factors f0, f2 — FULL Mellin vs schematic-Gilkey direct-power-sum
xpos = np.array([0, 1])                                           # (local)
w = 0.35                                                          # (local) bar width
axL.bar(xpos - w / 2, [f0_mellin, f2_mellin], w, color="#7570b3", label="FULL Mellin/physical-PV")
axL.bar(xpos + w / 2, [F0_SCH, F2_SCH], w, color="#d95f02", alpha=0.8, label="schematic-Gilkey (da899b4d)")
axL.set_xticks(xpos)
axL.set_xticklabels(["f0 = a$_0^{PV}$/a$_0^{\\zeta}$", "f2 = a$_2^{PV}$/a$_2^{\\zeta}$"])
axL.set_ylabel("PV factor f$_n$")
axL.set_title(f"PV factors: FULL Mellin vs schematic\n"
              f"f0_M={f0_mellin:.4f} f2_M={f2_mellin:.4f}  (sch f0={F0_SCH} f2={F2_SCH})", fontsize=9)
axL.legend(fontsize=8, loc="best")
axL.grid(True, axis="y", alpha=0.3)

# Right: the normalized comparison object f2/f0 vs target 0.6314, + absolute ratio annotation
axR.bar([0], [f2_over_f0_mellin], 0.5, color="#1b9e77", label=f"(f2/f0)_Mellin = {f2_over_f0_mellin:.4f}")
axR.axhline(SCHEMATIC_TARGET, color="#d95f02", ls="--", lw=1.4, label=f"schematic target 0.6314")
band_lo = SCHEMATIC_TARGET * (1 - OBJECT_DEF_BAND)               # (local)
band_hi = SCHEMATIC_TARGET * (1 + OBJECT_DEF_BAND)               # (local)
axR.axhspan(band_lo, band_hi, color="#1b9e77", alpha=0.12, label=f"object-defined band ±{OBJECT_DEF_BAND:.0%}")
axR.set_xticks([0]); axR.set_xticklabels(["f2/f0 (Mellin)"])
axR.set_ylabel("schematic-normalized CC-ratio  f2/f0")
axR.set_title(f"object-definedness: residual={residual_norm*100:.2f}% ({residual_OOM:.3f} OOM)\n"
              f"absolute a$_0^{{PV}}$/a$_2^{{PV}}$={R_CC_PV_abs:.4f}  [{verdict}]", fontsize=9)
axR.legend(fontsize=8, loc="best")
axR.grid(True, axis="y", alpha=0.3)

fig.suptitle(f"{GATE_ID} — clean SDW CC-ratio via FULL Mellin + FULL physical PV  ->  {outcome[:46]}  [{verdict}]\n"
             f"DI1: object-definedness axis ONLY (NOT §8.5 tier-2, NOT CC closure)", fontsize=9.5)
fig.tight_layout(rect=[0, 0, 1, 0.92])
fig.savefig(PNG_PATH, dpi=130)
plt.close(fig)
print(f"[SEC 6] png -> {PNG_PATH}")


# ============================================================
# SECTION 7: dual-SHA + verdict emission
# ============================================================
# audit_sha256_inputs (plan) = [script, analytic_zeta_module, s84_spectrum_cache,
#                               s96_ccgap_verdict_line, canonical, pinmap]
INPUT_FILES = [SCRIPT_PATH, ANALYTIC_ZETA_PY, SPECTRUM_CACHE, S96_VERDICTS, CANONICAL_PY]  # (local) pin all reads
pins = log_input_pins(INPUT_FILES)                               # (local)
clos = closure_hash(pins)                                        # (local)
# audit byte inputs ordered per plan (pinmap appended inside compute_dual_sha):
AUDIT_BYTE_INPUTS = [SCRIPT_PATH, ANALYTIC_ZETA_PY, SPECTRUM_CACHE, S96_VERDICTS, CANONICAL_PY]  # (local)
audit_sha, content_sha = compute_dual_sha(AUDIT_BYTE_INPUTS, pins)  # (local)

print(f"\n[SEC 7] closure_hash(pins) = {clos[:16]}...")
print(f"        audit_sha256       = {audit_sha[:16]}...  (script+analytic_zeta+s84+s96_verdicts+canonical+pinmap)")
print(f"        content_sha256     = {content_sha[:16]}...  (script only)")

value_str = (
    f"OUTCOME={outcome};verdict={verdict};"
    f"absolute_a0PV_over_a2PV={R_CC_PV_abs:.6f};"
    f"schematic_normalized_f2_over_f0_Mellin={f2_over_f0_mellin:.6f}_vs_target_0.6314;"
    f"f0_Mellin={f0_mellin:.6f}_f2_Mellin={f2_mellin:.6f};"
    f"residual_norm={residual_norm:.6f}_band={OBJECT_DEF_BAND};"
    f"residual_OOM={residual_OOM:.6f}_FAIL_if_gt_{DIVERGENCE_OOM};"
    f"divergence_sig={divergence_signature}_a2PVcollapsed={a2_pv_collapsed}_a0PVblewup={a0_pv_blew_up};"
    f"a0_pv={a0_pv:.6e}_a2_pv={a2_pv:.6e}_a0zeta={a0_zeta:.6e}_a2zeta={a2_zeta:.6e};"
    f"mellin_eq_direct_reldev=a0:{a0_mellin_vs_direct:.2e}_a2:{a2_mellin_vs_direct:.2e};"
    f"Lmax10to12_drift_absratio={Lmax_drift_ratio*100:.3f}pct_f2f0={Lmax_drift_f2f0*100:.3f}pct;"
    f"schematic_baseline_da899b4d_f0=0.7885_f2=0.4979_f2overf0=0.6314_direct_power_sum_PV;"
    f"CLASS=FULL_no_SCHEMATIC_suffix_no_tier_pin;"
    f"regulator_pin=a0_PauliVillars_a2_PauliVillars_AND_a0_zeta_a2_zeta;"
    f"poleconv=A-double_a0_s4_n0_a2_s3_n2;"
    f"DI1={DI1_SCOPE}"
)  # (local)

# 4-tuple output tag (final non-verdict line)
print(f"\n(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

append_verdict(verdict, value_str, audit_sha, content_sha)
print(f"\n[SEC 7] verdict appended -> {VERDICT_TXT}")
print(f"        {GATE_ID}: {verdict}")

sys.exit(0)   # exit code reflects SCRIPT HEALTH, not the scientific verdict (math-scripts.md)
