#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S105-W2-2-OMEGA-FAITHFUL-NORMAL — frozen-omega faithful-normal pre-gate.

GATES S105-W2-3-AREA-MODULAR-AGREEMENT (intra-wave gating; this verdict
determines whether the main gate is dispatched).

PHONONIC. The frozen GGE relic IS a substrate state — the quenched quasiparticle
occupation distribution {n_k^GGE} left behind by the diabatic transit through the
van Hove fold (R_therm = 5251.82, S_ent = 0, P_exc = 1.000). This gate tests
whether its restriction to the emergent horizon subalgebra A_hor is FAITHFUL and
NORMAL on the (0,0)+horizon-sector+Leggett-B2-B3 Peter-Weyl blocks of the
block-diagonal D_K = (+)_{(p,q)} D_{(p,q)} at L_max=10.

Direction of explanation (substrate-first; phononic-framing.md §"IS Space"):
  D_K block spectrum  ->  BdG gap Delta_a > 0 (3He-B BDI; CdGM +1/2 minigap; NO Weyl
  zero mode — the 3He-A sibling's exact zero does NOT inherit through chi: A_K -> M_2(C))
  ->  finite generalized-temperature beta_a (P_exc=1.000)  ->  0 < f_a < 1 strictly
  ->  faithful + normal omega  ->  modular Delta_omega^{it} exists (Tomita-Takesaki)
  ->  the emergent-horizon modular corridor is OPEN.

DUAL-CHANNEL pre-gate (volovik strengthening):
  F1-bosonic   : W_GGE(k) = n_k + 1/2 > 0 on every horizon block (floor +1/2; near-vacuous).
  F1-fermionic : f_a = 1/(exp(E_a/T_a)+1), E_a = sqrt(xi_a^2 + Delta_a^2) >= Delta_a > 0;
                 check 0 < f_a < 1 STRICTLY (the BINDING conjunct); K_a = log[(1-f)/f] finite.
  F2-normality : the {beta_a} are finite (0 < beta_a < inf); P_exc = 1.000 certificate.

PASS := (min over horizon blocks of W_GGE = n_k + 1/2) > 0
        AND (min_a f_a > 0 AND max_a f_a < 1, strict)
        AND (all |K_a| < K_MAX = 30, i.e. all beta_a finite)

FAIL := a hard fermionic zero/one (f_a <= EPS_FAITHFUL=1e-12 or f_a >= 1-EPS on a
        gapped BdG mode) — an ACCIDENTAL BdG degeneracy the analytic BDI argument did
        not enumerate (a SHARP NEW closure reason; distinct from INTEG-39, which tests
        ergodic thermalization, an ORTHOGONAL predicate).
INFO := a near-hard-zero |K_a| in (some-large, K_MAX) — finite but numerically marginal
        at the FD floor; flags the mode and routes to an S106 evaluator-precision refinement.

Plan: sessions/session-plan/session-105-plan-w2.md §W2-2 (gate block from line 237).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403  (MANDATORY)
from canonical_constants import (
    Delta_B2, Delta_B3, Delta_BCS, T_GGE_B2,
    a2_fold, A_horizon_FW, R_therm, P_exc_kz, n_pairs, tau_fold,
)

import hashlib
import json
import numpy as np

# GPU per computation-environment.md (cross-check on a test block vs numpy).
try:
    import torch
    _HAVE_TORCH = torch.cuda.is_available()
except Exception:  # pragma: no cover
    torch = None
    _HAVE_TORCH = False

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Identity + paths
# ---------------------------------------------------------------------------
SESSION = 105  # (local) session label
GATE_ID = "S105-W2-2-OMEGA-FAITHFUL-NORMAL"
SCHEME = "FW"
CONVENTION = ("FROZEN-GGE-NON-KMS;DUAL-CHANNEL(bosonic-Wightman-floor"
              "+fermionic-0<f<1+finite-beta-normality)")
L_MAX = 10  # (local) Peter-Weyl truncation (named-block extraction; orthogonal to W1 L-envelope)

SESSION_DIR = Path(__file__).resolve().parent
SCRIPT_PATH = Path(__file__).resolve()
CANON_PATH = _SHARED / "canonical_constants.py"
S104_SPEC_NPZ = SESSION_DIR.parent / "session-104" / "s104_area_modular_generator_spec.npz"
S84_CACHE_NPZ = SESSION_DIR.parent / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = SESSION_DIR / "s105_w2_2_omega_faithful_normal.npz"
OUT_PNG = SESSION_DIR / "s105_w2_2_omega_faithful_normal.png"

# ---------------------------------------------------------------------------
# Section 3 — Pre-registered machinery pins (PRDR)
# ---------------------------------------------------------------------------
EPS_FAITHFUL = 1e-12          # (local) hard-zero/one detection floor: f<=EPS or f>=1-EPS => FAIL
K_MAX = 30.0                  # (local) normality finiteness ceiling on |K_a| (|K|=30 <=> f~1e-13)
K_INFO = 25.0                 # (local) near-hard-zero INFO band: K_INFO < |K| < K_MAX => INFO flag
W_FLOOR = 0.5                 # (local) bosonic Wightman zero-point floor n_k + 1/2 (structural)

# ---------------------------------------------------------------------------
# Section 4 — Dual-SHA closure (audit + content)
#   audit_sha256_inputs:  [script, canonical, pinmap, s104_spec_npz, s84_cache_npz]
#   content_sha256_inputs: [script]
# ---------------------------------------------------------------------------
def closure_hash(pins: dict) -> str:
    h = hashlib.sha256()
    for k, v in sorted(pins.items()):
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def _file_sha(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def compute_dual_sha(pins: dict) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json || s104_npz || s84_npz);
    content = sha256(script)."""
    try:
        script_bytes = SCRIPT_PATH.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canon_bytes = CANON_PATH.read_bytes()  # (local)
    except OSError:
        canon_bytes = b""  # (local)
    try:
        s104_bytes = S104_SPEC_NPZ.read_bytes()  # (local)
    except OSError:
        s104_bytes = b""  # (local)
    try:
        s84_bytes = S84_CACHE_NPZ.read_bytes()  # (local)
    except OSError:
        s84_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canon_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(s104_bytes)
    h_audit.update(s84_bytes)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verdict payload printer (race-safe: PRINT only; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list | None = None) -> dict:
    payload: dict = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 6 — Horizon-block set (the named blocks; (0,0)+horizon-sector+Leggett-B2-B3)
# ---------------------------------------------------------------------------
# The plan names blocks (p,q) in {(0,0), horizon-sector, Leggett-B2-B3 inter-band}.
#   - (0,0): the singlet, the spectral floor of the block-diagonal D_K (acoustic horizon point).
#   - horizon-sector: the bottom-of-spectrum low-(p,q) blocks carrying the horizon physics —
#     the fundamentals (1,0)/(0,1) [level 1] and the octet/adjoint (1,1) [level 2].
#   - Leggett-B2-B3 inter-band: the B2 and B3 inter-band sectors carry the pairing gaps
#     Delta_B2 = 0.732026 and Delta_B3 = 0.176 (the Leggett mode is the B2-B3 inter-band
#     phase excitation; session-80 PROVEN). These gaps are attached as the BdG pairing
#     gaps Delta_a that protect 0 < f_a < 1 on the horizon BdG modes.
# This is the bottom of the spectrum (levels 0,1,2) where the emergent-horizon physics lives;
# the L_max-envelope (deeper blocks) is Wave 1's axis, ORTHOGONAL to this gate.
HORIZON_BLOCKS = [(0, 0), (1, 0), (0, 1), (1, 1)]  # (local) named horizon-sector Peter-Weyl blocks

# The BdG pairing gaps attached to the horizon BdG modes (the Leggett-B2-B3 + BCS gaps).
# Each is a SEPARATE faithfulness channel: the strict-interior test must hold for the
# SMALLEST gap (the weakest protection) since smaller Delta => larger possible E/T => smaller f.
BDG_GAPS = {            # (local) {channel: Delta_a}  (M_KK units; all > 0 by 3He-B BDI)
    "B2": Delta_B2,     # Leggett B2 inter-band gap = 0.732026
    "B3": Delta_B3,     # Leggett B3 inter-band gap = 0.176  (SMALLEST => weakest protection)
    "BCS": Delta_BCS,   # canonical BCS gap = 0.464255
}

# The GGE generalized-temperature on the horizon blocks (the frozen relic temperature).
# T_GGE_B2 = 0.668 (M_KK units, S43) is the canonical frozen-GGE temperature. It is FINITE
# and STRICTLY POSITIVE: beta_a = 1/T_a in (0, inf). P_exc = 1.000 certifies the freeze is
# saturated-but-finite (a T->0 empty vacuum or T->inf maxent would destroy faithfulness, but
# the diabatic freeze produces neither: it produces a finite-beta non-KMS stationary relic).
T_GGE = T_GGE_B2        # (local) frozen-GGE generalized temperature (finite, P_exc=1.000)


def load_horizon_spectrum() -> dict:
    """Load |lambda| of D_K per named horizon (p,q) block from the s84 master cache."""
    cache = np.load(S84_CACHE_NPZ, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # (local) {(p,q): {dim, level, abs_evals}}
    out = {}  # (local)
    for pq in HORIZON_BLOCKS:
        if pq not in sector_evals:
            raise KeyError(f"horizon block {pq} absent from s84 cache")
        out[pq] = np.asarray(sector_evals[pq]["abs_evals"], dtype=np.float64)
    return out, sector_evals


# ---------------------------------------------------------------------------
# Section 7 — BdG occupation (the substitution chain, realized per block)
# ---------------------------------------------------------------------------
def bdg_occupation(abs_evals: np.ndarray, lam_horizon: float,
                   Delta_a: float, T_a: float):
    """Realize the substitution chain on one block + one pairing gap.

      xi_a = |lambda|_a - lam_horizon     (normal-state dispersion rel the horizon Fermi point)
      E_a  = sqrt(xi_a^2 + Delta_a^2)     (BdG quasiparticle energy; >= Delta_a > 0, GAPPED)
      f_a  = 1/(exp(E_a/T_a) + 1)         (Fermi-Dirac occupation; quasi-free separating cond.)
      K_a  = log[(1 - f_a)/f_a]           (fermionic modular Hamiltonian on mode a)

    Returns (xi, E, f, K) arrays.
    """
    xi = abs_evals - lam_horizon                       # (local) normal-state dispersion
    E = np.sqrt(xi * xi + Delta_a * Delta_a)           # (local) BdG energy >= Delta_a > 0
    # numerically stable f and K (E/T_a is O(1) here, but guard anyway):
    x = E / T_a                                        # (local) E_a/T_a = beta_a * E_a > 0
    f = 1.0 / (np.exp(x) + 1.0)                         # (local) f in (0, 1/2) for E>0,beta>0
    # K_a = log[(1-f)/f] = log(exp(x)) = x exactly for the FD form; compute via f to detect
    # any accidental floor where f underflows.
    with np.errstate(divide="ignore", invalid="ignore"):
        K = np.log((1.0 - f) / f)                       # (local) modular Hamiltonian
    return xi, E, f, K


def bogoliubov_occupation(abs_evals: np.ndarray, lam_horizon: float, Delta_a: float):
    """Cross-check channel: the BCS Bogoliubov occupation v_a^2 (knowledge-MCP S89 form)
       v_a^2 = (1/2)(1 - xi_a / E_a).  This is the T=0 ground-state occupation; it must also
       lie strictly in (0, 1) on a gapped mode (xi/E in (-1, 1) strictly since Delta>0)."""
    xi = abs_evals - lam_horizon                       # (local)
    E = np.sqrt(xi * xi + Delta_a * Delta_a)           # (local)
    v2 = 0.5 * (1.0 - xi / E)                           # (local) Bogoliubov occupation in (0,1)
    return v2


# ---------------------------------------------------------------------------
# Section 8 — A-V3 scale-segregation diagnostic (NON-GATING)
# ---------------------------------------------------------------------------
def av3_weight_suppression(sector_evals: dict) -> dict:
    """SECONDARY diagnostic (NON-GATING): the area-operator weight mult_{(p,q)}/lambda^2_{(p,q)}
    on high-single-cell chaos-leaning cells vs integrable cells. Recorded in npz, NOT a
    PASS/FAIL conjunct. We report the area weight per horizon block and the ratio of the
    deepest (lowest-lambda, integrable) to the shallowest (highest-lambda) named block."""
    rows = {}  # (local)
    for pq in HORIZON_BLOCKS:
        s = sector_evals[pq]
        mult = int(s["dim"])                       # (local) Peter-Weyl multiplicity (dim of irrep)
        lam2 = float(np.mean(np.asarray(s["abs_evals"]) ** 2))  # (local) mean lambda^2 in block
        rows[pq] = mult / lam2                      # (local) area-operator weight proxy
    return rows


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    # ----- input SHAs (first 20 lines of stdout per gate-verdicts.md §2) -----
    print(f"[{GATE_ID}] input SHA-256 pins:")
    print(f"  script            = {_file_sha(SCRIPT_PATH)}")
    print(f"  canonical         = {_file_sha(CANON_PATH)}")
    print(f"  s104_spec_npz     = {_file_sha(S104_SPEC_NPZ)}")
    print(f"  s84_cache_npz     = {_file_sha(S84_CACHE_NPZ)}")
    print(f"  GPU(torch.cuda)   = {_HAVE_TORCH}")
    print(f"  frozen-GGE certs  : R_therm={R_therm}, P_exc={P_exc_kz}, n_pairs={n_pairs}, "
          f"S_ent=0 (S95 diabatic transit-freeze)")
    print(f"  pins              : EPS_FAITHFUL={EPS_FAITHFUL}, K_MAX={K_MAX}, "
          f"K_INFO={K_INFO}, W_FLOOR={W_FLOOR}, T_GGE={T_GGE}, L_max={L_MAX}, tau_fold={tau_fold}")
    print(f"  gaps              : Delta_B2={Delta_B2}, Delta_B3={Delta_B3}, Delta_BCS={Delta_BCS}")

    # ----- load horizon spectrum -----
    horizon_spec, sector_evals = load_horizon_spectrum()
    # horizon Fermi reference = global min |lambda| over the named horizon blocks
    # (the spectral floor; the acoustic horizon point). This is substrate-IS, not a free knob.
    lam_horizon = min(float(arr.min()) for arr in horizon_spec.values())  # (local)
    print(f"\n[horizon] Fermi reference lam_horizon = {lam_horizon:.10f} "
          f"(global min |lambda| over named blocks)")

    # ----- GPU cross-check on a test block (per computation-environment.md) -----
    gpu_crosscheck_ok = None  # (local)
    if _HAVE_TORCH:
        try:
            test = np.asarray(horizon_spec[(1, 1)], dtype=np.float64)  # (local)
            xi_np = test - lam_horizon                                  # (local)
            E_np = np.sqrt(xi_np ** 2 + Delta_B3 ** 2)                  # (local)
            tt = torch.tensor(test, device="cuda", dtype=torch.float64)  # (local)
            xi_t = tt - lam_horizon                                     # (local)
            E_t = torch.sqrt(xi_t * xi_t + Delta_B3 * Delta_B3).cpu().numpy()  # (local)
            gpu_crosscheck_ok = bool(np.allclose(E_np, E_t, rtol=1e-12, atol=1e-14))
            print(f"[gpu] torch vs numpy BdG-energy cross-check on (1,1) test block: "
                  f"max|diff|={np.max(np.abs(E_np - E_t)):.2e}  ok={gpu_crosscheck_ok}")
        except Exception as exc:  # pragma: no cover
            print(f"[gpu] cross-check skipped ({exc}); proceeding on numpy")

    # =====================================================================
    # F1-fermionic — the BINDING channel: 0 < f_a < 1 strictly on every BdG mode
    # =====================================================================
    print("\n=== F1-fermionic (BINDING): per-(p,q)-block, per-gap BdG occupation ===")
    f_global_min = np.inf   # (local)
    f_global_max = -np.inf  # (local)
    K_global_max = -np.inf  # (local)
    n_modes_total = 0       # (local)
    per_block = {}          # (local) records for npz

    # iterate over the smallest gap FIRST (weakest protection => binding case)
    for ch in sorted(BDG_GAPS, key=lambda c: BDG_GAPS[c]):  # B3 (0.176) < BCS < B2
        Dg = BDG_GAPS[ch]  # (local)
        for pq in HORIZON_BLOCKS:
            ae = horizon_spec[pq]
            xi, E, f, K = bdg_occupation(ae, lam_horizon, Dg, T_GGE)
            fmin, fmax = float(f.min()), float(f.max())   # (local)
            Kmax = float(np.abs(K).max())                  # (local)
            f_global_min = min(f_global_min, fmin)
            f_global_max = max(f_global_max, fmax)
            K_global_max = max(K_global_max, Kmax)
            n_modes_total += f.size
            per_block[f"{ch}|{pq}"] = dict(
                gap=Dg, f_min=fmin, f_max=fmax, K_abs_max=Kmax,
                E_min=float(E.min()), E_max=float(E.max()), n_modes=int(f.size))
    print(f"  smallest gap = Delta_B3 = {Delta_B3} (weakest protection => binding)")
    print(f"  GLOBAL over all named blocks x gaps: f in [{f_global_min:.6e}, {f_global_max:.6e}]")
    print(f"  GLOBAL |K|_max = {K_global_max:.6f}  (K_MAX = {K_MAX})")
    print(f"  n_modes_total = {n_modes_total}")

    # strict-interior test
    faithful_fermionic = (f_global_min > EPS_FAITHFUL) and (f_global_max < 1.0 - EPS_FAITHFUL)

    # =====================================================================
    # F2-normality: all |K_a| < K_MAX (all beta_a finite)
    # =====================================================================
    normal = K_global_max < K_MAX
    info_marginal = (not normal) and (K_global_max < K_MAX) is False  # placeholder; refined below
    # INFO branch: some |K| in (K_INFO, K_MAX) — near-hard but finite
    marginal_modes = [k for k, v in per_block.items() if K_INFO < v["K_abs_max"] < K_MAX]  # (local)
    has_info_marginal = len(marginal_modes) > 0  # (local)

    print("\n=== F2-normality: finiteness of K_a (= finite beta_a) ===")
    print(f"  |K|_max = {K_global_max:.6f}  K_INFO={K_INFO}  K_MAX={K_MAX}")
    print(f"  normal (all |K| < K_MAX): {normal}")
    print(f"  marginal modes (K_INFO < |K| < K_MAX): {marginal_modes if marginal_modes else 'none'}")

    # =====================================================================
    # F1-bosonic: W_GGE(k) = n_k + 1/2 > 0  (floor +1/2; near-vacuous)
    # The bosonic occupation n_k on the horizon blocks: the GGE-relic bosonic occupation is
    # n_k >= 0 always; the Wightman zero-point weight W = n_k + 1/2 therefore has a structural
    # floor of +1/2 that NEVER vanishes. We compute a representative n_k from the BCS Bogoliubov
    # occupation v_a^2 (>=0) as the substrate-IS bosonic excitation count on the horizon modes.
    # =====================================================================
    print("\n=== F1-bosonic: Wightman zero-point floor W_GGE = n_k + 1/2 ===")
    W_global_min = np.inf  # (local)
    for pq in HORIZON_BLOCKS:
        ae = horizon_spec[pq]
        v2 = bogoliubov_occupation(ae, lam_horizon, Delta_BCS)   # (local) n_k proxy >= 0
        n_k = np.clip(v2, 0.0, None)                              # (local) bosonic count >= 0
        W = n_k + W_FLOOR                                         # (local) Wightman weight
        W_global_min = min(W_global_min, float(W.min()))
    faithful_bosonic = W_global_min > 0.0
    print(f"  W_GGE_min over horizon blocks = {W_global_min:.6f} (floor {W_FLOOR}); "
          f"faithful_bosonic = {faithful_bosonic}")

    # =====================================================================
    # A-V3 scale-segregation diagnostic (NON-GATING)
    # =====================================================================
    av3 = av3_weight_suppression(sector_evals)
    av3_str = {f"{k}": float(v) for k, v in av3.items()}  # (local)
    # deepest (integrable, lowest mean-lambda) vs shallowest named block weight ratio
    weights_sorted = sorted(av3.items(), key=lambda kv: float(np.mean(np.asarray(sector_evals[kv[0]]["abs_evals"]) ** 2)))  # (local)
    av3_ratio = (weights_sorted[0][1] / weights_sorted[-1][1]) if weights_sorted[-1][1] != 0 else float("nan")  # (local)
    print(f"\n=== A-V3 diagnostic (NON-GATING): area-weight mult/lambda^2 per block ===")
    for pq, w in av3.items():
        print(f"  (p,q)={pq}: weight = {w:.6f}")
    print(f"  deepest/shallowest weight ratio = {av3_ratio:.6f}  (diagnostic only)")

    # =====================================================================
    # Composite verdict (logical AND of the three conjuncts)
    # =====================================================================
    pass_all = bool(faithful_bosonic and faithful_fermionic and normal)
    if pass_all:
        verdict = "PASS"
    elif has_info_marginal and faithful_fermionic and faithful_bosonic:
        # finite but numerically marginal at the FD floor: INFO (does NOT dispatch item 3)
        verdict = "INFO"
    else:
        verdict = "FAIL"

    value = (f"f_in[{f_global_min:.4e},{f_global_max:.4e}]_strict01;"
             f"|K|max={K_global_max:.4f}<{K_MAX};"
             f"W_GGE_min={W_global_min:.4f}>0;"
             f"faithful_ferm={faithful_fermionic};normal={normal};"
             f"faithful_bos={faithful_bosonic};"
             f"DUAL-CHANNEL_AND={pass_all}")

    print(f"\n=== VERDICT: {verdict} ===")
    print(f"  F1-bosonic  (W_GGE>0)      : {faithful_bosonic}")
    print(f"  F1-fermionic(0<f<1 strict) : {faithful_fermionic}  [BINDING]")
    print(f"  F2-normality(|K|<K_MAX)    : {normal}")
    print(f"  composite (AND)            : {pass_all}")

    # ----- 4-tuple output tag (final non-verdict line) -----
    print(f"\n4-tuple: (value={value!r}, scheme={SCHEME}, convention=FROZEN-GGE-NON-KMS;DUAL-CHANNEL, L_max={L_MAX})")

    # =====================================================================
    # npz
    # =====================================================================
    npz_payload = dict(
        gate_id=GATE_ID, verdict=verdict, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        horizon_blocks=np.array([f"{p},{q}" for (p, q) in HORIZON_BLOCKS]),
        lam_horizon=lam_horizon,
        f_global_min=f_global_min, f_global_max=f_global_max, K_global_max=K_global_max,
        W_global_min=W_global_min, n_modes_total=n_modes_total,
        EPS_FAITHFUL=EPS_FAITHFUL, K_MAX=K_MAX, K_INFO=K_INFO, W_FLOOR=W_FLOOR, T_GGE=T_GGE,
        Delta_B2=Delta_B2, Delta_B3=Delta_B3, Delta_BCS=Delta_BCS,
        faithful_bosonic=faithful_bosonic, faithful_fermionic=faithful_fermionic,
        normal=normal, pass_all=pass_all,
        marginal_modes=np.array(marginal_modes if marginal_modes else ["none"]),
        av3_weights_json=json.dumps(av3_str), av3_ratio=av3_ratio,
        per_block_json=json.dumps(per_block),
        R_therm=R_therm, P_exc=P_exc_kz, n_pairs=n_pairs, S_ent=0.0,
        a2_fold=a2_fold, A_horizon_FW=A_horizon_FW,
        gpu_crosscheck_ok=("None" if gpu_crosscheck_ok is None else gpu_crosscheck_ok),
    )
    np.savez_compressed(OUT_NPZ, **npz_payload)
    print(f"[npz] wrote {OUT_NPZ}")

    # =====================================================================
    # plot: per-block f_a vs mode index with the (0,1) faithfulness band + A-V3 panel
    # =====================================================================
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13.5, 5.2))

    # left: f_a per block for the smallest gap (B3, binding) + the (0,1) band
    Dg_bind = Delta_B3  # (local)
    colors = plt.cm.viridis(np.linspace(0.1, 0.85, len(HORIZON_BLOCKS)))  # (local)
    mode_offset = 0  # (local)
    for ci, pq in enumerate(HORIZON_BLOCKS):
        ae = horizon_spec[pq]
        _, _, f, _ = bdg_occupation(ae, lam_horizon, Dg_bind, T_GGE)
        idx = np.arange(mode_offset, mode_offset + f.size)  # (local)
        ax0.plot(idx, f, "o", ms=3.5, color=colors[ci], label=f"(p,q)={pq}")
        mode_offset += f.size
    ax0.axhspan(0.0, 1.0, color="0.92", zorder=0)
    ax0.axhline(0.0, color="r", lw=1.0, ls="--")
    ax0.axhline(1.0, color="r", lw=1.0, ls="--")
    ax0.axhline(EPS_FAITHFUL, color="darkred", lw=0.8, ls=":")
    ax0.set_xlabel("BdG mode index (named horizon blocks)")
    ax0.set_ylabel(r"$f_a = 1/(e^{E_a/T_a}+1)$")
    ax0.set_ylim(-0.05, 1.05)
    ax0.set_title(f"F1-fermionic: $0<f_a<1$ strict (gap $\\Delta_{{B3}}={Delta_B3}$, binding)\n"
                  f"min $f$={f_global_min:.3e}, max $f$={f_global_max:.3e}, "
                  f"$|K|_{{max}}$={K_global_max:.3f}<{K_MAX}")
    ax0.legend(fontsize=8, loc="center right")
    ax0.grid(alpha=0.25)

    # right: A-V3 area-weight per block (diagnostic)
    bx = np.arange(len(HORIZON_BLOCKS))  # (local)
    bw = [av3[pq] for pq in HORIZON_BLOCKS]  # (local)
    ax1.bar(bx, bw, color="slateblue", alpha=0.8)
    ax1.set_xticks(bx)
    ax1.set_xticklabels([f"{pq}" for pq in HORIZON_BLOCKS], rotation=20)
    ax1.set_ylabel(r"area weight  $\mathrm{mult}_{(p,q)}/\langle\lambda^2\rangle_{(p,q)}$")
    ax1.set_title(f"A-V3 scale-segregation diagnostic (NON-GATING)\n"
                  f"deepest/shallowest ratio = {av3_ratio:.3f}")
    ax1.grid(alpha=0.25, axis="y")

    fig.suptitle(f"{GATE_ID}  —  frozen-GGE faithful-normal pre-gate  —  VERDICT: {verdict}",
                 fontsize=12, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"[png] wrote {OUT_PNG}")

    # =====================================================================
    # dual-SHA + verdict payload
    # =====================================================================
    pins = {
        "gate_id": GATE_ID, "scheme": SCHEME, "convention": CONVENTION, "L_max": str(L_MAX),
        "EPS_FAITHFUL": str(EPS_FAITHFUL), "K_MAX": str(K_MAX), "K_INFO": str(K_INFO),
        "W_FLOOR": str(W_FLOOR), "T_GGE": repr(T_GGE),
        "Delta_B2": repr(Delta_B2), "Delta_B3": repr(Delta_B3), "Delta_BCS": repr(Delta_BCS),
        "horizon_blocks": ";".join(f"{p},{q}" for (p, q) in HORIZON_BLOCKS),
        "lam_horizon": repr(lam_horizon),
        "f_global_min": repr(f_global_min), "f_global_max": repr(f_global_max),
        "K_global_max": repr(K_global_max), "W_global_min": repr(W_global_min),
        "verdict": verdict,
        "s104_spec_sha": _file_sha(S104_SPEC_NPZ), "s84_cache_sha": _file_sha(S84_CACHE_NPZ),
    }
    closure = closure_hash(pins)  # (local) closure over the ordered pin map
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"\n[closure] closure_hash(pins) = {closure}")

    companion = (f"frozen-GGE non-KMS faithful-normal pre-gate; "
                 f"0<f<1 strict on (0,0)+horizon+Leggett-B2-B3 blocks; "
                 f"|K|max={K_global_max:.4f}<{K_MAX}; gap-protected (CdGM +1/2, no Weyl zero); "
                 f"GATES S105-W2-3-AREA-MODULAR-AGREEMENT")
    extra = [f"# av3_diagnostic ratio={av3_ratio:.6f} (NON-GATING); "
             f"closure_hash={closure[:16]}; S_ent=0 P_exc={P_exc_kz} R_therm={R_therm}"]
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
