#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S99-W4-A0A2-LMAX13  —  Wave 4 robustness: FULL-physical Pauli-Villars a_0/a_2
within-family L_max drift extended to L_max>=13 (operationally L_max=14 via the
on-disk master spectrum cache), testing whether the within-family drift d_PV
shrinks below eps_FI=0.05 (promoting the capstone §8.5 tier-2 survival INFO->PASS).

Gate: S99-W4-A0A2-LMAX13  (session-99, wave 4; lizzi-spectral-functional-theorist)
Plan: sessions/session-plan/session-99-plan-w4.md  §W4-1
Trigger: [SIGN]  (schema_v2_3tuple_required=true)
Classification: GEOMETRIC

WHAT THIS DOES (L_max-axis RD residual — the ONLY axis this gate probes)
------------------------------------------------------------------------
The S98 V.8 gate (S98-A0A2-TIER2-PV-INVARIANCE, INFO) established that the
§8.5 tier-2 a_0/a_2 SURVIVAL LABEL is regulator-INVARIANT (byte-identical
SURVIVE under both the FI-anchor a_0/a_2=0.217563 and the full-PV anchor
0.510595; Delta_survival_margin=0). The residual regulator-DEPENDENCE (RD)
is localized to the L_max axis, registered as d_PV = |ratio_PV(L) -
ratio_PV(L10)| / |ratio_PV(L10)| with the L10->L12 baseline d_PV(L12)=0.05703
sitting in the INFO band (eps_FI=0.05, info_band=0.10].

This gate extends that drift to L_max=14 (the largest on-disk master spectrum
cache; L_max_plan=13 <= L_max_operational=14) and recomputes d_PV(L14). It
tests ONLY the L_max-axis RD residual; the survival LABEL is NOT recomputed
(it is regulator-INVARIANT, S98 V.8). A FAIL here records the RD as a
structural L_max-axis property (Two-Layer reading per epistemic-discipline.md
§"Resolution-Specificity Scoping": Layer-1 pole-universal survival LABEL
untouched; Layer-2 L_max-axis RD residual is the structural finding) and
retracts NO substrate-IS structural fact.

FULL-PHYSICAL PV (CLASS=FULL; NOT SCHEMATIC)
--------------------------------------------
The PV moment is the FULL-physical evaluation (the EXACT S97 W2-1 / S98 V.8
machinery): a_n^PV = a_n^Mellin(s_n) - sum_j c_j * a_n^{Mellin,shifted}(s_n; m_j^2)
with the physical PV set {c_j}={2,-1}, {m_j^2/M_KK^2}={1,2}, Lambda_UV=M_KK
(NOT the schematic Casimir-fraction set of _spectral_action_regulators.py).
CLASS=FULL ==> NO -SCHEMATIC convention suffix, NO `# tier_pin=TIER-2` row
(per substrate-first-canonical-sourcing.md §(iv) FULL-side; S97 W2-1 / S98 V.8
precedent). regulator_pin a_0^{Pauli-Villars} / a_2^{Pauli-Villars},
poleconv-A-double (zeta(s)=sum m_k lambda_k^{-2s}, poles at s=(d-n)/2, d=8):
a_0 at pole_in_s=4 (curvature_grade n=0); a_2 at pole_in_s=3 (n=2).

L_max FEASIBILITY (LOAD-BEARING; math-scripts.md §"D_K Block-Diagonality +
Recursive-Casimir-Projection Feasibility Pre-Check")
----------------------------------------------------------------------------
Recursive Casimir-projection irrep construction at p+q>=13 may TIMEOUT within
an agent slot. RESOLVED via the Casimir-bound + cache cross-check route
(option 1): the L_max=14 master spectrum cache
computations/session-87/s87_spectrum_cache_L14_tau019.npz is ALREADY ON DISK
(sector_evals keyed by Peter-Weyl (p,q), abs_evals per sector; identical schema
to the canonical L12 cache _analytic_zeta consumes). L_max_operational=14 >=
L_max_plan=13 is achieved by RE-POINTING the heat kernel to the cached L14
sector eigenvalues -- NO new irrep construction fires, so the timeout risk is
structurally moot. The script asserts the L14 cache supplies all sectors the
bottom-K Mellin moment consumes (truncation_consistent flag = all p+q<=14
sectors present, 0..14 contiguous). If the L14 cache is unusable at runtime,
the script FALLS BACK to the Friedrich-Bar structural-saturation analytic
argument (option 2) and tags the verdict scheme `...-FB-SATURATION-ANALYTIC`.

NOTE on the shared module: this script does NOT edit or import the L12-pinned
SPECTRUM_CACHE inside _shared/_analytic_zeta.py (that module is a SHA-pinned
input). It reuses the module's EXACT Mellin<->Dirichlet math (heat-kernel GPU
factory + mp.dps=50 quadrature) re-pointed to the L14 cache in-script, so the
FULL-physical PV evaluation is byte-faithful to the S97 W2-1 evaluator while
the spectrum truncation is L_max=14.

SUBSTRATE-FIRST FRAMING (phononic-framing.md)
---------------------------------------------
GEOMETRIC. The arrow flows D_K eigenvalues {lambda_k, m_k} on the L_max-
truncated finite spectral triple (A_K^{<=L}, H_K^{<=L}, D_K^{<=L}) at
tau_fold=0.190 -> a_0 (zeroth, cosmological-term weight-0) / a_2 (second,
Einstein-Hilbert weight-2) Seeley-DeWitt spectral moments -> the §8.5 tier-2
survival partition. The a_0/a_2 ratio is a substrate-IS read-off, NOT a
laboratory measurement. The substrate IS the truncated spectral triple. This
gate asks whether extending the truncation L_max to 13/14 leaves the surviving-
side partition signed-distance invariant to within the FI tolerance -- a
robustness check on the spectral-moment partition, NOT a new prediction. The
survival LABEL is already a regulator-INVARIANT substrate-IS fact (S98 V.8);
this gate probes only the L_max-axis RD residual on the ratio magnitude, a
methodology-floor refinement of an already-established substrate-IS survival.

SUBSTITUTION CHAIN (math-scripts.md §"Double-Check Logic Before Compute")
-------------------------------------------------------------------------
Claim: "Extending L_max from 10 to >=13 (operationally 14) SHRINKS the
        within-family PV drift d_PV toward zero (below eps_FI=0.05)."
 Step 1 (Definitions, cited):
   ratio_PV(L) := a_0^{PV}(L) / a_2^{PV}(L)    [FULL-physical PV-subtracted SDW ratio;
                  S97 W2-1 mellin_moment_pv, PV set c={2,-1}, m^2={1,2}]
   a_0^{PV}(L)  = Mellin moment at s-pole=4 (n=0), PV-subtracted [a_0^{Pauli-Villars}, poleconv-A-double, d=8]
   a_2^{PV}(L)  = Mellin moment at s-pole=3 (n=2), PV-subtracted [a_2^{Pauli-Villars}, poleconv-A-double, d=8]
   ratio_PV(L10)= 0.510595   [S98 V.8 canonical, npz key ratio_PV_L10]
   ratio_PV(L12)= 0.481478   [S98 V.8 cross-check, npz key ratio_PV_L12]
   d_PV(L)     := |ratio_PV(L) - ratio_PV(L10)| / |ratio_PV(L10)|   [within-family relative drift vs L10 anchor]
   eps_FI = 0.05   [capstone §8.5 tier-2 FI-survival drift tolerance]
 Step 2 (Substitute the L10->L12 baseline, no simplification):
   d_PV(L12) = |0.481478 - 0.510595| / |0.510595| = |-0.029117| / 0.510595
 Step 3 (Simplify, one step per line):
   d_PV(L12) = 0.029117 / 0.510595 = 0.057026
   => 0.05 < 0.057026 <= 0.10 => d_PV(L12) sits in the INFO band (eps_FI, info_band].
 Step 4 (Direction read-off -- the [SIGN] claim under test):
   The signed step ratio_PV(L10)->ratio_PV(L12) = 0.510595->0.481478 is DECREASING (Delta=-0.029117).
   The DRIFT-SHRINK hypothesis predicts continuing L10->L14 the SUCCESSIVE relative change SHRINKS:
     d_PV(L14) = |ratio_PV(L14) - ratio_PV(L10)| / |ratio_PV(L10)| < d_PV(L12) = 0.057026
   i.e. the cache-moment ratio CONVERGES (Friedrich-Bar truncation-saturation: new high-(p,q)
   sectors at p+q in {13,14} carry |lambda| >= eta_FB*sqrt(C_2+1); their Mellin weight at s-pole>=3
   is suppressed by |lambda|^{-2s}, bounded and diminishing).
   PASS direction: d_PV(L14) < eps_FI=0.05 (drift crosses below FI tolerance => survival INFO->PASS).
   The gate is OPEN between PASS (convergent below eps_FI), INFO (narrows but stays in (0.05,0.10]),
   and FAIL (does not shrink => RD is structural on the L_max axis).
 Conclusion (NOT pre-judged): sign_verdict=PASS iff sign(ratio_PV(L14)-ratio_PV(L10)) tracks the
   predicted convergent-decrease AND d_PV(L14) < d_PV(L12); magnitude_verdict keys d_PV(L14) vs
   eps_FI/info_band; regime_verdict=VALID (deterministic Mellin quadrature, no SR/ODE regime).

VERDICT RUBRIC (plan PASS/FAIL/INFO_meaning):
   PASS : d_PV(L14) < eps_FI=0.05                          -> RD vanishing truncation artifact; §8.5 survival INFO->PASS
   FAIL : d_PV(L14) does NOT shrink (>= info_band=0.10 OR >= d_PV(L12)=0.05703)
                                                           -> RD STRUCTURAL on the L_max axis (Track B); survival LABEL untouched (regulator-INVARIANT)
   INFO : 0.05 < d_PV(L14) <= 0.10 AND d_PV(L14) < d_PV(L12) -> narrows toward eps_FI but does not cross

ENV: phonon-exflation-sim/.venv312/Scripts/python.exe ; FULL Mellin quadrature mp.dps=50
     CPU-bound (~tens of s per s-pole x (1 unshifted + 2 PV) terms x 2 truncations); the
     heat kernel K(t) accumulation runs on torch GPU (AMD RX 9070 XT, ROCm) on the
     pre-built L14 cache eigenvalues -- NO diagonalization.
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
HERE = Path(__file__).resolve().parent                              # (local) computations/session-99
SHARED = HERE.parent / "_shared"                                    # (local) computations/_shared
PROJECT_ROOT = HERE.parent.parent                                   # (local) repo root
sys.path.insert(0, str(SHARED))

from canonical_constants import (   # noqa: E402
    a_0_FW_zeta,     # 6440.0       zeta-regulated a_0 (= zeta_{D_K}(0) = Tr(1))   (S88)
    a_2_FW_zeta,     # 2776.165389  zeta-regulated a_2                            (S88)
    M_KK,            # 7.428660036284456e16 GeV  (alias M_KK_gravity, S42)
    tau_fold,        # 0.19         Jensen fold slice (S42 CONST-FREEZE-42)
)

# torch GPU heat-kernel (AMD RX 9070 XT, ROCm). CPU fallback if torch unavailable.
try:
    import torch
    _TORCH_OK = True
    _DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
except Exception:
    _TORCH_OK = False
    _DEVICE = "cpu"

mp.dps = 50  # workdps for off-pole / mass-shifted Mellin integrand


# ============================================================
# SECTION 0: Identifiers, paths, thresholds
# ============================================================
GATE_ID = "S99-W4-A0A2-LMAX13"                                      # (local)
SCHEME = "TIER2-SURVIVAL-DUAL-ANCHOR-FI-vs-FULL-PV"                 # (local) matches S98 V.8 scheme lineage
CONVENTION = "RATIO-LABEL-DISTANCE-poleconv-A-double-PV-FULL-PHYSICAL"  # (local) matches S98 V.8; FULL physical PV
L_MAX_PLAN = 13                                                     # (local) pre-registered extension target
L_MAX_OPERATIONAL = 14                                             # (local) on-disk L14 master cache covers L>=13
L_MAX_TAG = "13"                                                    # (local) L_max= verdict field (plan-pinned L_max_plan)

# Pre-registered thresholds (plan operator / strict_PASS_boundary / verdict rubric)
EPS_FI = 0.05                                                       # (local) capstone §8.5 tier-2 FI-survival drift tolerance (PASS<)
INFO_BAND = 0.10                                                    # (local) INFO ceiling; FAIL if d_PV >= info_band
RATIO_PV_L10 = 0.5105953845835941                                  # (local) S98 V.8 canonical anchor (npz key ratio_PV_L10)
RATIO_PV_L12 = 0.48147807091983613                                # (local) S98 V.8 cross-check (npz key ratio_PV_L12)
D_PV_L12_BASELINE = 0.05702619832238401                            # (local) S98 V.8 d_PV_within_family_drift baseline
D_SPEC_NCG = 8                                                     # (local) NCG dimension-spectrum d=8 (cone-apex labeling, S85 W6-13; NOT the substrate dim d_spec=3 — this is the spectral-triple dimension-spectrum for the Conv.A pole map poles at s=(d-n)/2). Matches S97 W2-1 / S98 V.8 local literal.

# FULL physical Pauli-Villars set (NOT the schematic Casimir-fraction set):
PV_C = [2.0, -1.0]                                                 # (local) {c_j} physical PV coefficients
PV_M2_DIMLESS = [1.0, 2.0]                                         # (local) {m_j^2/M_KK^2} physical PV mass set (M_KK^2 units)

# Conv. A double-power pole indices -> Dirichlet exponents in lambda:
S_POLE_A0_CONVA = 4                                                # (local) a_0: pole_in_s=4 (curvature_grade n=0)
S_POLE_A2_CONVA = 3                                                # (local) a_2: pole_in_s=3 (curvature_grade n=2)
DIRICHLET_EXP_A0 = 2 * S_POLE_A0_CONVA                            # (local) = 8  (lambda^-8) heat-kernel Mellin arg for a_0
DIRICHLET_EXP_A2 = 2 * S_POLE_A2_CONVA                            # (local) = 6  (lambda^-6) heat-kernel Mellin arg for a_2

ABS_TOL = 1e-10                                                     # (local) float64 absolute tolerance
PUB_PRECISION = 6                                                  # (local) d_PV cited downstream; 6 sig figs

SCRIPT_PATH = Path(__file__).resolve()                            # (local)
CANONICAL_PY = SHARED / "canonical_constants.py"                  # (local)
ANALYTIC_ZETA_PY = SHARED / "_analytic_zeta.py"                   # (local) FULL-physical PV evaluator (math source)
L14_CACHE = PROJECT_ROOT / "computations" / "session-87" / "s87_spectrum_cache_L14_tau019.npz"  # (local) L_max>=13 resolver
S98_V8_NPZ = PROJECT_ROOT / "computations" / "session-98" / "s98_a0a2_tier2_pv_invariance.npz"   # (local) drift machinery + survival label
S97_W2_1_NPZ = PROJECT_ROOT / "computations" / "session-97" / "s97_w2_1_a0a2_pv_full_mellin.npz"  # (local) FULL-PV producer + L12 baseline
NPZ_PATH = HERE / "s99_w4_a0a2_lmax13.npz"                        # (local)
PNG_PATH = HERE / "s99_w4_a0a2_lmax13.png"                        # (local)
VERDICT_TXT = HERE / "s99_gate_verdicts.txt"                      # (local) CANONICAL path per gate-verdicts.md

# Plan-pinned input SHAs (Input-SHA Ledger, session-99-plan-w4.md §"Wave 4 Input-SHA Ledger").
PLAN_PIN_SHA = {                                                   # (local)
    "computations/_shared/_analytic_zeta.py": "6383c87717c17040f596264a2e33cdc630089fb750681ab2eb149e934d84f660",
    "computations/session-87/s87_spectrum_cache_L14_tau019.npz": "fa2bfb83c74ff151b138c83498f54ca2c87a61fc59ec1ae5189bb6aab360480c",
    "computations/session-98/s98_a0a2_tier2_pv_invariance.npz": "77f8ea525b02d2710677eaa2afa0fc5eac6049c4d03b9a871a825488470a4e3b",
    "computations/session-97/s97_w2_1_a0a2_pv_full_mellin.npz": "20a398bd2b7386970a036b551d29d9fa449423edaff4ad071cb329796c910d3a",
}


# ============================================================
# SECTION 1: dual-SHA helpers (S84+ schema)
#   audit_sha256_inputs (plan) = [script, analytic_zeta_module, s87_L14_cache,
#                                 s98_v8_npz, s97_w2_1_npz, canonical, pinmap]
#   content_sha256_inputs = [script]
# ============================================================
def sha256_of(path: Path) -> str:                                  # (local)
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:                                # (local)
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                      # (local)
    for p in inputs:
        sha = sha256_of(p)                                         # (local)
        try:
            rel = str(Path(p).relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)                                           # (local)
        plan_sha = PLAN_PIN_SHA.get(rel)                           # (local)
        drift = "" if (plan_sha is None or plan_sha == sha) else f"  [PIN-DRIFT vs plan {plan_sha[:16]}...]"  # (local)
        print(f"  {rel}: {sha[:16]}...{drift}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:                               # (local)
    items = sorted(pins.items())                                   # (local)
    h = hashlib.sha256()                                           # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(audit_input_paths, pins: dict):               # (local)
    """audit_sha256 = sha256( bytes(script||analytic_zeta||s87_L14_cache||s98_v8_npz||
                              s97_w2_1_npz||canonical) || bytes(pinmap_json) );
       content_sha256 = sha256( bytes(script) )."""
    h_audit = hashlib.sha256()                                     # (local)
    for p in audit_input_paths:
        try:
            h_audit.update(Path(p).read_bytes())
        except OSError:
            h_audit.update(b"")
    pinmap_json = json.dumps(                                      # (local)
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                    # (local)

    h_content = hashlib.sha256()                                   # (local)
    try:
        h_content.update(Path(SCRIPT_PATH).read_bytes())
    except OSError:
        h_content.update(b"")
    content = h_content.hexdigest()                                # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None):                        # (local)
    """Print the EMIT_VERDICT payload for the agent to pass to the race-safe
       emit_verdict knowledge-MCP tool (per gate-verdicts.md §"Race-Safe Emission";
       the script NEVER open-codes a verdict-file append)."""
    payload = {                                                    # (local)
        "session": 99,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX_TAG,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "extra_rows": extra_rows or [],
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>" + json.dumps(payload) + "<<<END_EMIT_VERDICT_PAYLOAD>>>")


# ============================================================
# SECTION 2: L14-cache spectrum loader + GPU heat kernel
#   (mirrors _analytic_zeta.load_spectrum / _heat_kernel_gpu_factory EXACTLY,
#    re-pointed to the on-disk L14 master cache -- NO diagonalization,
#    NO edit/import of the L12-pinned SPECTRUM_CACHE in the shared module)
# ============================================================
print("=" * 78)
print(f"{GATE_ID}  (FULL-physical PV a_0/a_2 within-family L_max drift -> L_max=14)")
print("=" * 78)
print(f"[SEC 2] torch_ok={_TORCH_OK}  device={_DEVICE}  mp.dps={mp.dps}")
print(f"[SEC 2] tau_fold={tau_fold}  M_KK={M_KK:.6e} GeV (Lambda_UV)  d_spec={D_SPEC_NCG}")
print(f"[SEC 2] L_max_plan={L_MAX_PLAN}  L_max_operational={L_MAX_OPERATIONAL} (on-disk L14 master cache)")
print(f"[SEC 2] zeta anchors: a_0_FW_zeta={a_0_FW_zeta}  a_2_FW_zeta={a_2_FW_zeta}")
print(f"[SEC 2] Conv. A double-power: a_0 (pole_in_s={S_POLE_A0_CONVA}, n=0) -> lambda^-{DIRICHLET_EXP_A0}; "
      f"a_2 (pole_in_s={S_POLE_A2_CONVA}, n=2) -> lambda^-{DIRICHLET_EXP_A2}")
print(f"[SEC 2] FULL physical PV: c_j={PV_C}  m_j^2/M_KK^2={PV_M2_DIMLESS}  (NOT schematic Casimir-fraction)")

# Load the L14 master spectrum cache. Fallback flag for Friedrich-Bar saturation.
_FB_FALLBACK = False                                               # (local) set True only if L14 cache unusable
_TRUNCATION_CONSISTENT = False                                     # (local) all p+q<=L_max_operational sectors present, contiguous
try:
    _L14 = np.load(L14_CACHE, allow_pickle=True)
    _SECTOR_EVALS = _L14["sector_evals"].item()
    _levels = sorted({(p + q) for (p, q) in _SECTOR_EVALS.keys()})  # (local) contiguous-level check
    _max_level = max(_levels)                                       # (local)
    # truncation_consistent: levels 0..L_max_operational all present (contiguous), and the
    # cache's max level covers L_max_operational (=14) -> supplies every sector the Mellin
    # moment at L_max_operational consumes.
    _TRUNCATION_CONSISTENT = (
        _max_level >= L_MAX_OPERATIONAL
        and _levels == list(range(0, _max_level + 1))
    )
    print(f"[SEC 2] L14 cache: {len(_SECTOR_EVALS)} sectors, levels 0..{_max_level}; "
          f"truncation_consistent={_TRUNCATION_CONSISTENT}")
    if not _TRUNCATION_CONSISTENT:
        _FB_FALLBACK = True
        print("[SEC 2] WARNING: L14 cache levels not contiguous through L_max_operational "
              "-> FB-SATURATION-ANALYTIC fallback engaged.")
except Exception as _e:  # noqa: F841
    _FB_FALLBACK = True
    _SECTOR_EVALS = {}
    print(f"[SEC 2] WARNING: L14 cache load failed ({_e!r}) -> FB-SATURATION-ANALYTIC fallback engaged.")

_SPEC_CACHE: dict = {}                                             # (local) keyed by L_max
_HK_TENSOR_CACHE: dict = {}                                       # (local) keyed by (L_max, device)


def load_spectrum_L14(L_max: int):                                 # (local)
    """|lambda_k| magnitudes + integer Weyl-dim multiplicities for p+q<=L_max,
       from the L14 master cache. Identical filter logic to _analytic_zeta.load_spectrum."""
    if L_max in _SPEC_CACHE:
        return _SPEC_CACHE[L_max]
    evs_list = []                                                  # (local)
    mults_list = []                                                # (local)
    for (p, q), info in _SECTOR_EVALS.items():
        if (p + q) > L_max:
            continue
        es = np.asarray(info["abs_evals"], dtype=np.float64)       # (local)
        if es.size == 0:
            continue
        mults_list.append(np.full(es.shape, float(info["dim"])))   # (local)
        evs_list.append(es)
    evs = np.concatenate(evs_list)                                 # (local)
    mults = np.concatenate(mults_list)                             # (local)
    mask = evs > 1e-12                                             # (local) drop numerical zeros
    evs = evs[mask]
    mults = mults[mask]
    _SPEC_CACHE[L_max] = (evs, mults)
    return evs, mults


def hk_factory_L14(L_max: int):                                    # (local)
    """K(t) = sum_k m_k exp(-lambda_k^2 t) on GPU (torch.float64 on _DEVICE),
       from the L14 master cache. Mirrors _analytic_zeta._heat_kernel_gpu_factory."""
    evs, mults = load_spectrum_L14(L_max)
    lam2 = evs * evs                                               # (local) lambda_k^2
    if _TORCH_OK:
        key = (L_max, _DEVICE)                                     # (local)
        if key not in _HK_TENSOR_CACHE:
            t_lam2 = torch.tensor(lam2, dtype=torch.float64, device=_DEVICE)  # (local)
            t_mult = torch.tensor(mults, dtype=torch.float64, device=_DEVICE)  # (local)
            _HK_TENSOR_CACHE[key] = (t_lam2, t_mult)
        t_lam2, t_mult = _HK_TENSOR_CACHE[key]

        def hk(t: float) -> float:
            return float(torch.sum(t_mult * torch.exp(-float(t) * t_lam2)).item())
        return hk

    def hk_cpu(t: float) -> float:
        return float(np.sum(mults * np.exp(-float(t) * lam2)))
    return hk_cpu


def mellin_moment_shifted(dirichlet_exp_lambda: float, L_max: int, m2_shift: float) -> float:  # (local)
    """FULL Mellin-route moment with heat-kernel mass shift m2_shift (M_KK^2 units).
       EXACT S97 W2-1 machinery, re-pointed to the L14 GPU heat kernel.
         sum_k m_k (lambda_k^2 + m2_shift)^{-s/2} * Gamma(s/2)
           = int_0^inf t^(s/2-1) exp(-m2_shift t) K(t) dt,  s = dirichlet_exp_lambda."""
    s = mpc(float(dirichlet_exp_lambda))                           # (local) lambda-power
    half_s = s / 2                                                 # (local) lambda^2-power
    hk = hk_factory_L14(L_max)                                     # (local) GPU K(t) on L14 cache

    def integrand(t):
        try:
            tt = float(t)
        except (TypeError, ValueError):
            tt = float(mpm.mpf(t))
        if tt <= 0.0:
            return mpm.mpf(0)
        damp = mpm.e ** (-mpm.mpf(float(m2_shift)) * mpm.mpf(tt))  # (local) exp(-m2 t)
        K_val = hk(tt)                                             # (local) sum_k m_k exp(-lambda^2 t)
        return mpm.power(t, half_s - 1) * damp * mpm.mpf(K_val)

    I1 = mp.quad(integrand, [0, 1])                                # (local) small-t integrable
    I2 = mp.quad(integrand, [1, mp.inf])                           # (local) large-t exp decay
    val = (I1 + I2) / mpm.gamma(half_s)                            # (local)
    return float(complex(val).real)


def mellin_moment_pv(dirichlet_exp_lambda: float, L_max: int):     # (local)
    """FULL physical PV-subtracted Mellin moment (EXACT S97 W2-1):
         a_n^PV = a_n^Mellin(s_n) - sum_j c_j * a_n^{Mellin,shifted}(s_n; m_j^2).
       Returns (a_n^zeta=unshifted, a_n^PV, [shifted terms])."""
    a_zeta = mellin_moment_shifted(dirichlet_exp_lambda, L_max, 0.0)  # (local) unsubtracted = a_n^zeta(=Mellin)
    a_pv = a_zeta                                                   # (local)
    shifted = []                                                   # (local)
    for c, m2 in zip(PV_C, PV_M2_DIMLESS):
        a_shift = mellin_moment_shifted(dirichlet_exp_lambda, L_max, m2)  # (local)
        a_pv -= c * a_shift
        shifted.append((c, m2, a_shift))
    return a_zeta, a_pv, shifted


# --- L10 reproduction cross-check (machinery faithfulness; must match S98 V.8 canon) ---
print("\n[SEC 2] L10 reproduction cross-check (from L14 cache, p+q<=10) -- must match S98 V.8 canon:")
if not _FB_FALLBACK:
    a0z10, a0pv10, _ = mellin_moment_pv(DIRICHLET_EXP_A0, 10)
    a2z10, a2pv10, _ = mellin_moment_pv(DIRICHLET_EXP_A2, 10)
    ratio_PV_L10_recomputed = a0pv10 / a2pv10                      # (local)
    xc_a0pv_L10 = bool(abs(a0pv10 - 1300.2094666215025) / 1300.2094666215025 < 1e-6)  # (local) vs S98 V.8 a0_PV
    xc_a2pv_L10 = bool(abs(a2pv10 - 2546.457539332954) / 2546.457539332954 < 1e-6)    # (local) vs S98 V.8 a2_PV
    xc_ratio_L10 = bool(abs(ratio_PV_L10_recomputed - RATIO_PV_L10) / RATIO_PV_L10 < 1e-6)  # (local)
    print(f"  a_0^PV(L10)={a0pv10:.10f} (canon 1300.2094666)  match={xc_a0pv_L10}")
    print(f"  a_2^PV(L10)={a2pv10:.10f} (canon 2546.4575393)  match={xc_a2pv_L10}")
    print(f"  ratio_PV(L10)={ratio_PV_L10_recomputed:.10f} (canon {RATIO_PV_L10:.10f})  match={xc_ratio_L10}")
else:
    a0z10 = a0pv10 = a2z10 = a2pv10 = float("nan")
    ratio_PV_L10_recomputed = RATIO_PV_L10
    xc_a0pv_L10 = xc_a2pv_L10 = xc_ratio_L10 = False
    print("  [FB-SATURATION fallback: L10 recomputation skipped; S98 V.8 canon used]")


# ============================================================
# SECTION 3: L14 FULL-physical PV moments + ratio + drift
# ============================================================
print("\n" + "=" * 78)
print(f"[SEC 3] FULL-physical PV moments at L_max_operational={L_MAX_OPERATIONAL}")
print("=" * 78)

if not _FB_FALLBACK:
    a0z14, a0pv14, a0sh14 = mellin_moment_pv(DIRICHLET_EXP_A0, L_MAX_OPERATIONAL)
    a2z14, a2pv14, a2sh14 = mellin_moment_pv(DIRICHLET_EXP_A2, L_MAX_OPERATIONAL)
    ratio_PV_L14 = a0pv14 / a2pv14                                 # (local) a_0^PV(L14)/a_2^PV(L14)
    print(f"  a_0^zeta(L14, s=8) = {a0z14:.10e}")
    print(f"  a_2^zeta(L14, s=6) = {a2z14:.10e}")
    for tag, sh in (("a_0", a0sh14), ("a_2", a2sh14)):
        for c, m2, a_s in sh:
            print(f"    {tag} PV-shifted term c={c:+.1f} m^2={m2:.1f}: a_shift={a_s:.10e}")
    print(f"  a_0^PV(L14) = {a0pv14:.10e}")
    print(f"  a_2^PV(L14) = {a2pv14:.10e}")
    print(f"  ratio_PV(L14) = a_0^PV/a_2^PV = {ratio_PV_L14:.10f}")
else:
    # Friedrich-Bar structural-saturation analytic fallback: new sectors p+q in {13,14}
    # carry |lambda| >= eta_FB*sqrt(C_2+1); their Mellin weight at s>=3 is |lambda|^{-2s}-
    # suppressed. With the cache unusable we cannot numerically resolve the L14 ratio, so
    # the drift is bounded analytically by the L12 baseline (saturation argument). This
    # branch is engaged ONLY if the cache is genuinely unusable (it is NOT, here).
    a0z14 = a2z14 = a0pv14 = a2pv14 = float("nan")
    a0sh14 = a2sh14 = []
    ratio_PV_L14 = RATIO_PV_L12  # (local) saturation proxy (NOT used in the numerical path)
    print("  [FB-SATURATION-ANALYTIC fallback: L14 numerical ratio unavailable; "
          "saturation-bounded by L12 baseline]")

# Within-family drift d_PV(L14) = |ratio_PV(L14) - ratio_PV(L10)| / |ratio_PV(L10)|
delta_L14 = ratio_PV_L14 - RATIO_PV_L10                            # (local) signed step vs L10 anchor
d_PV_L14 = abs(delta_L14) / abs(RATIO_PV_L10)                      # (local) within-family relative drift @ L14
# L12 baseline (recompute from anchors for self-consistency; cross-check vs S98 V.8 pin):
delta_L12 = RATIO_PV_L12 - RATIO_PV_L10                            # (local)
d_PV_L12 = abs(delta_L12) / abs(RATIO_PV_L10)                      # (local) should equal D_PV_L12_BASELINE
xc_d_PV_L12 = bool(abs(d_PV_L12 - D_PV_L12_BASELINE) < 1e-9)       # (local)

print("\n" + "=" * 78)
print("[SEC 3] DRIFT (substitution chain Step 2-4)")
print("=" * 78)
print(f"  ratio_PV(L10) = {RATIO_PV_L10:.10f}  [S98 V.8 anchor]")
print(f"  ratio_PV(L12) = {RATIO_PV_L12:.10f}  [S98 V.8 cross-check]   d_PV(L12) = {d_PV_L12:.6f} "
      f"(baseline {D_PV_L12_BASELINE:.6f}, match={xc_d_PV_L12})")
print(f"  ratio_PV(L14) = {ratio_PV_L14:.10f}                          d_PV(L14) = {d_PV_L14:.6f}")
print(f"  signed step Delta_L12 = {delta_L12:+.6f}   Delta_L14 = {delta_L14:+.6f}   "
      f"(sign_L14={np.sign(delta_L14):+.0f}, sign_L12={np.sign(delta_L12):+.0f})")
print(f"  eps_FI = {EPS_FI}   info_band = {INFO_BAND}")
print(f"  d_PV(L14) < eps_FI ? {d_PV_L14 < EPS_FI}")
print(f"  d_PV(L14) < d_PV(L12) (DRIFT-SHRINK direction) ? {d_PV_L14 < d_PV_L12}")


# ============================================================
# SECTION 4: VERDICT — 3-tuple ([SIGN]) + composite collapse
# ============================================================
print("\n" + "=" * 78)
print("[SEC 4] VERDICT — L_max-axis RD residual (3-tuple [SIGN])")
print("=" * 78)

# sign_verdict: the substitution-chain Step-4 DRIFT-SHRINK direction prediction is
# "d_PV(L14) < d_PV(L12)" (the successive relative change toward the L10 anchor shrinks =>
# convergent). sign_verdict=PASS iff the computed direction matches that prediction.
drift_shrinks = bool(d_PV_L14 < d_PV_L12)                          # (local) computed convergent-decrease direction
sign_verdict = "PASS" if drift_shrinks else "FAIL"                 # (local)

# magnitude_verdict: keyed on d_PV(L14) vs eps_FI (PASS), info_band (INFO/FAIL).
#   PASS : d_PV(L14) <  eps_FI
#   INFO : eps_FI <= d_PV(L14) <= info_band  AND drift_shrinks (narrows but does not cross)
#   FAIL : d_PV(L14) >  info_band  OR  d_PV(L14) >= d_PV(L12) (does NOT shrink, per FAIL_meaning)
if d_PV_L14 < EPS_FI:
    magnitude_verdict = "PASS"                                     # (local)
elif (d_PV_L14 > INFO_BAND) or (not drift_shrinks):
    magnitude_verdict = "FAIL"                                     # (local) does-NOT-shrink clause (>= d_PV(L12)) OR exceeds info_band
else:
    magnitude_verdict = "INFO"                                     # (local) (eps_FI, info_band] AND shrinks

# regime_verdict: deterministic Mellin quadrature on a finite L_max-truncated spectrum;
# no small-parameter / ODE-breakdown regime. VALID throughout (unless FB fallback).
regime_verdict = "VALID" if not _FB_FALLBACK else "MARGINAL"      # (local)

# Composite collapse (PRE-REGISTERED, gate-verdicts.md §"Composite-collapse rule"):
if regime_verdict == "BREAKDOWN":
    composite = "FAIL"                                            # (local)
elif sign_verdict == "FAIL":
    composite = "FAIL"                                            # (local)
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    composite = "FAIL"                                            # (local)
elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
    composite = "INFO"                                            # (local)
elif magnitude_verdict == "INFO":
    composite = "INFO"                                            # (local)
else:
    composite = "PASS"                                            # (local)

# Track allocation (dual_prior discriminator):
if composite == "PASS":
    track = "TRACK_A_RD_VANISHING_TRUNCATION_ARTIFACT_survival_INFO_to_PASS"   # (local)
elif composite == "FAIL":
    track = "TRACK_B_RD_STRUCTURAL_ON_LMAX_AXIS_survival_stays_INFO_label_untouched"  # (local)
else:
    track = "UNCHANGED_extension_narrows_but_does_not_decide"      # (local)

print(f"  sign_verdict      = {sign_verdict}  (DRIFT-SHRINK prediction d_PV(L14)<d_PV(L12)={d_PV_L12:.6f}; "
      f"computed d_PV(L14)={d_PV_L14:.6f}; shrinks={drift_shrinks})")
print(f"  magnitude_verdict = {magnitude_verdict}  (d_PV(L14)={d_PV_L14:.6f} vs eps_FI={EPS_FI}, info_band={INFO_BAND})")
print(f"  regime_verdict    = {regime_verdict}  (deterministic Mellin quadrature; FB_fallback={_FB_FALLBACK})")
print(f"  COMPOSITE         = {composite}")
print(f"  TRACK             = {track}")
print("  DI1 SCOPE: L_max-AXIS-RD-RESIDUAL-ONLY; survival LABEL is regulator-INVARIANT (S98 V.8 "
      "byte-identical SURVIVE); this gate does NOT establish or retract the §8.5 tier-2 survival "
      "LABEL nor any substrate-IS structural fact; FAIL records RD as a Layer-2 L_max-axis "
      "structural property (epistemic-discipline.md §Resolution-Specificity Scoping).")


# ============================================================
# SECTION 5: persist npz + png
# ============================================================
np.savez(
    NPZ_PATH,
    gate_id=GATE_ID,
    scheme=str(SCHEME),
    convention=str(CONVENTION),
    L_max_plan=int(L_MAX_PLAN),
    L_max_operational=int(L_MAX_OPERATIONAL),
    truncation_consistent=bool(_TRUNCATION_CONSISTENT),
    fb_fallback=bool(_FB_FALLBACK),
    tau_fold=float(tau_fold),
    M_KK=float(M_KK),
    Lambda_UV=float(M_KK),
    d_spec_ncg=int(D_SPEC_NCG),
    # Conv. A pole labeling
    s_pole_a0=int(S_POLE_A0_CONVA),
    n_grade_a0=int(0),
    s_pole_a2=int(S_POLE_A2_CONVA),
    n_grade_a2=int(2),
    dirichlet_exp_a0=int(DIRICHLET_EXP_A0),
    dirichlet_exp_a2=int(DIRICHLET_EXP_A2),
    poleconv="A-double",
    regulator_pin_a0="a_n^{Pauli-Villars}",
    regulator_pin_a2="a_n^{Pauli-Villars}",
    CLASS="FULL",
    # FULL physical PV set
    pv_c=np.array(PV_C),
    pv_m2_dimless=np.array(PV_M2_DIMLESS),
    # zeta anchors
    a_0_FW_zeta=float(a_0_FW_zeta),
    a_2_FW_zeta=float(a_2_FW_zeta),
    # L10 reproduction cross-check
    a0_zeta_L10=float(a0z10),
    a2_zeta_L10=float(a2z10),
    a0_PV_L10=float(a0pv10),
    a2_PV_L10=float(a2pv10),
    ratio_PV_L10_recomputed=float(ratio_PV_L10_recomputed),
    xc_a0pv_L10=bool(xc_a0pv_L10),
    xc_a2pv_L10=bool(xc_a2pv_L10),
    xc_ratio_L10=bool(xc_ratio_L10),
    # L14 FULL-physical PV moments
    a0_zeta_L14=float(a0z14),
    a2_zeta_L14=float(a2z14),
    a0_PV_L14=float(a0pv14),
    a2_PV_L14=float(a2pv14),
    # ratios + drift
    ratio_PV_L10=float(RATIO_PV_L10),
    ratio_PV_L12=float(RATIO_PV_L12),
    ratio_PV_L14=float(ratio_PV_L14),
    delta_L12=float(delta_L12),
    delta_L14=float(delta_L14),
    d_PV_L12=float(d_PV_L12),
    d_PV_L12_baseline=float(D_PV_L12_BASELINE),
    xc_d_PV_L12=bool(xc_d_PV_L12),
    d_PV_L14=float(d_PV_L14),
    drift_shrinks=bool(drift_shrinks),
    # thresholds
    eps_FI=float(EPS_FI),
    info_band=float(INFO_BAND),
    # verdict
    sign_verdict=str(sign_verdict),
    magnitude_verdict=str(magnitude_verdict),
    regime_verdict=str(regime_verdict),
    composite_verdict=str(composite),
    track=str(track),
)
print(f"\n[SEC 5] npz -> {NPZ_PATH}")

# --- plot: ratio_PV(L) trajectory (left) + drift d_PV(L) vs bands (right) ---
fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.5, 4.8))

Ls = np.array([10, 12, L_MAX_OPERATIONAL])                         # (local)
ratios = np.array([RATIO_PV_L10, RATIO_PV_L12, ratio_PV_L14])     # (local)
axL.plot(Ls, ratios, "o-", color="#7570b3", lw=1.6, ms=8, label="ratio_PV(L) = a$_0^{PV}$/a$_2^{PV}$")
axL.axhline(RATIO_PV_L10, color="#d95f02", ls="--", lw=1.1, label=f"L10 anchor = {RATIO_PV_L10:.4f}")
for x, y in zip(Ls, ratios):
    axL.annotate(f"{y:.4f}", (x, y), textcoords="offset points", xytext=(0, 9), fontsize=8, ha="center")
axL.set_xlabel("L_max")
axL.set_ylabel("ratio_PV(L) = a$_0^{PV}$ / a$_2^{PV}$")
axL.set_xticks(Ls)
axL.set_title(f"FULL-physical PV a$_0$/a$_2$ ratio vs L_max\n"
              f"L10={RATIO_PV_L10:.4f} L12={RATIO_PV_L12:.4f} L14={ratio_PV_L14:.4f} "
              f"(monotone {'decreasing' if (delta_L14<0 and delta_L12<0) else 'mixed'})", fontsize=9)
axL.legend(fontsize=8, loc="best")
axL.grid(True, alpha=0.3)

xpos = np.array([0, 1])                                            # (local) L12, L14
axR.bar(xpos, [d_PV_L12, d_PV_L14], 0.5,
        color=["#1b9e77", "#e7298a" if composite == "FAIL" else "#1b9e77"],
        label="d_PV(L) within-family drift")
axR.axhline(EPS_FI, color="#1b9e77", ls="--", lw=1.4, label=f"eps_FI = {EPS_FI} (PASS<)")
axR.axhline(INFO_BAND, color="#d95f02", ls="--", lw=1.4, label=f"info_band = {INFO_BAND} (FAIL>=)")
axR.axhspan(0, EPS_FI, color="#1b9e77", alpha=0.10)
axR.axhspan(EPS_FI, INFO_BAND, color="#e6ab02", alpha=0.10)
for x, y in zip(xpos, [d_PV_L12, d_PV_L14]):
    axR.annotate(f"{y:.5f}", (x, y), textcoords="offset points", xytext=(0, 6), fontsize=8, ha="center")
axR.set_xticks(xpos)
axR.set_xticklabels(["d_PV(L12)\n[S98 baseline]", "d_PV(L14)\n[this gate]"])
axR.set_ylabel("within-family drift d_PV = |ratio(L)-ratio(L10)|/|ratio(L10)|")
axR.set_title(f"L_max-axis RD residual: d_PV(L14)={d_PV_L14:.5f}\n"
              f"shrinks vs L12={d_PV_L12:.5f}? {drift_shrinks}  [{composite}]", fontsize=9)
axR.legend(fontsize=7.5, loc="best")
axR.grid(True, axis="y", alpha=0.3)

fig.suptitle(f"{GATE_ID} — FULL-physical PV a$_0$/a$_2$ within-family L_max drift -> L_max=14  [{composite}]\n"
             f"DI1: L_max-axis RD residual ONLY (survival LABEL regulator-INVARIANT, S98 V.8)", fontsize=9.5)
fig.tight_layout(rect=[0, 0, 1, 0.91])
fig.savefig(PNG_PATH, dpi=130)
plt.close(fig)
print(f"[SEC 5] png -> {PNG_PATH}")


# ============================================================
# SECTION 6: dual-SHA + verdict payload (race-safe emit_verdict)
# ============================================================
# audit_sha256_inputs (plan) = [script, analytic_zeta_module, s87_L14_cache,
#                               s98_v8_npz, s97_w2_1_npz, canonical, pinmap]
INPUT_FILES = [SCRIPT_PATH, ANALYTIC_ZETA_PY, L14_CACHE, S98_V8_NPZ, S97_W2_1_NPZ, CANONICAL_PY]  # (local)
pins = log_input_pins(INPUT_FILES)                                # (local)
clos = closure_hash(pins)                                         # (local)
AUDIT_BYTE_INPUTS = [SCRIPT_PATH, ANALYTIC_ZETA_PY, L14_CACHE, S98_V8_NPZ, S97_W2_1_NPZ, CANONICAL_PY]  # (local)
audit_sha, content_sha = compute_dual_sha(AUDIT_BYTE_INPUTS, pins)  # (local)

print(f"\n[SEC 6] closure_hash(pins) = {clos[:16]}...")
print(f"        audit_sha256       = {audit_sha[:16]}...  (script+analytic_zeta+L14_cache+s98v8+s97w2_1+canonical+pinmap)")
print(f"        content_sha256     = {content_sha[:16]}...  (script only)")

scheme_emit = SCHEME if not _FB_FALLBACK else (SCHEME + "-FB-SATURATION-ANALYTIC")  # (local)

value_str = (
    f"OUTCOME={track};composite={composite};"
    f"d_PV_L14={d_PV_L14:.6f}_vs_eps_FI={EPS_FI}_info_band={INFO_BAND};"
    f"d_PV_L12_baseline={d_PV_L12:.6f}_drift_shrinks={drift_shrinks};"
    f"ratio_PV_L10={RATIO_PV_L10:.6f}_L12={RATIO_PV_L12:.6f}_L14={ratio_PV_L14:.6f};"
    f"signed_step_L14={delta_L14:+.6f}_L12={delta_L12:+.6f}_monotone_decreasing={bool(delta_L14<0 and delta_L12<0)};"
    f"a0_PV_L14={a0pv14:.6e}_a2_PV_L14={a2pv14:.6e}_a0_zeta_L14={a0z14:.6e}_a2_zeta_L14={a2z14:.6e};"
    f"L10_repro_xc=a0pv:{xc_a0pv_L10}_a2pv:{xc_a2pv_L10}_ratio:{xc_ratio_L10};"
    f"L_max_plan={L_MAX_PLAN}_L_max_operational={L_MAX_OPERATIONAL}_truncation_consistent={_TRUNCATION_CONSISTENT};"
    f"survival_LABEL_regulator_INVARIANT_S98_V8_byte_identical_SURVIVE_NOT_recomputed_NOT_retracted;"
    f"CLASS=FULL_no_SCHEMATIC_suffix_no_tier_pin;"
    f"regulator_pin=a0_PauliVillars_a2_PauliVillars;poleconv=A-double_a0_s4_n0_a2_s3_n2;"
    f"DI1=L_max-AXIS-RD-RESIDUAL-ONLY_does-NOT-establish-or-retract-§8.5-tier-2-survival-LABEL"
)  # (local)

# Companion rows (regulator_pin + DI1 scope; FULL-class => NO -SCHEMATIC, NO tier_pin row):
extra_rows = [                                                    # (local)
    (f"# regulator_pin a_0^{{Pauli-Villars}} (pole_in_s={S_POLE_A0_CONVA},n=0) "
     f"a_2^{{Pauli-Villars}} (pole_in_s={S_POLE_A2_CONVA},n=2) poleconv-A-double d={D_SPEC_NCG}; "
     f"CLASS=FULL (full-physical PV c={PV_C} m^2={PV_M2_DIMLESS}; NO -SCHEMATIC, NO tier_pin)"),
    (f"# DI1: L_max-axis RD residual ONLY; survival LABEL regulator-INVARIANT (S98 V.8 byte-identical "
     f"SURVIVE); FAIL records RD as Layer-2 L_max-axis structural property; retracts NO substrate-IS fact; "
     f"L_max_plan={L_MAX_PLAN} L_max_operational={L_MAX_OPERATIONAL} truncation_consistent={_TRUNCATION_CONSISTENT}"),
]

# 4-tuple output tag (final non-verdict line)
print(f"\n(value={value_str!r}, scheme={scheme_emit}, convention={CONVENTION}, L_max={L_MAX_TAG})")

# Override SCHEME-in-payload if FB fallback fired:
SCHEME_FINAL = scheme_emit                                        # (local)
_orig_scheme = SCHEME
globals()["SCHEME"] = SCHEME_FINAL  # ensure payload carries the FB suffix when applicable
print_verdict_payload(composite, value_str, audit_sha, content_sha,
                      sign_verdict, magnitude_verdict, regime_verdict,
                      extra_rows=extra_rows)
globals()["SCHEME"] = _orig_scheme

print(f"\n[SEC 6] {GATE_ID}: composite={composite}  "
      f"(sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict})")
print("[SEC 6] Payload printed; agent will call the race-safe emit_verdict knowledge-MCP tool.")

sys.exit(0)   # exit code reflects SCRIPT HEALTH, not the scientific verdict (math-scripts.md)
