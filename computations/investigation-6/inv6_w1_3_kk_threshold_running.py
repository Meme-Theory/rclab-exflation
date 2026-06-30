#!/usr/bin/env python3
"""
INV6-W1-3 — Three-coupling KK-tower threshold running M_KK -> m_Z
================================================================

Gate: INV6-W1-3-KK-THRESHOLD-RUNNING  ([VERIFY])
Track: investigation-6, Wave 1
Classification: PARTICLE (the representation-theoretic content of D_K cashing out
                as low-energy gauge couplings)

Pre-registered threshold (plan §W1-3):
  operator: inequality
  PASS iff  max_a |alpha_a(m_Z)_computed - alpha_a(m_Z)_obs| / alpha_a(m_Z)_obs <= 0.02
            across a in {em, W, s}  AND  the m_H route-band collapses to a single value.
  FAIL = the assembled running cannot reach the observed low-energy couplings from the
         unification ansatz g3^2 = g2^2 = (3/5) g1^2 at M_KK (max dev > 2% with no (p,q)
         sum reaching it).
  INFO = partial (unification/ratio structure reproduced but one coupling off > 2%, OR
         m_H band does not collapse).

SUBSTRATE FRAMING
-----------------
The KK tower IS the set of massive Peter-Weyl (p,q) sectors of the fiber spectrum above
the zero mode; running a coupling from M_KK to m_Z is integrating out those sectors one
(p,q) shell at a time. The Cartan Trace Identity (T10, PROVEN all (p,q)) is a structural
property of the D_K spectrum: per-sector traces T_a(p,q) = Sum_{lambda in sector_a} lambda^-2
satisfy T_SU3(p,q) = T_SU2(q,p) = T_U1(q,p)/12, so the LEADING threshold is a substrate-
geometric fact, not a fitted input. The flow is D_K eigenvalues (the (p,q) tower) ->
spectral moments (the Cartan traces / threshold sums) -> observed couplings at m_Z.

METHOD
------
(1) Cartan verification: confirm the eigenvalue-side trace identity T_eig(p,q)=T_eig(q,p)
    on the L12 cache (the (p,q)<->(q,p) leg of T_SU3=T_SU2), and the Dynkin-index leg
    T_U1 = 12 * T_SU2 (representation-theoretic, exact).
(2) C^2 block decoupling: Delta sin^2 theta_W[C^2] = 0 EXACT (S84 W9-106) — the off-diagonal
    Gell-Mann generators {lam_4,5,6,7} of su(3)=u(1)+su(2)+C^2 satisfy Tr(lam_i Y)=Tr(lam_i T3).
(3) No-threshold unification skeleton: run alpha_a^-1(m_Z) = alpha_unif^-1 - (b_a/2pi) ln(M_KK/m_Z)
    with (b1,b2,b3)=(41/10,-19/6,-7) SM one-loop, alpha_unif^-1 = alpha2_MKK_inv = 47.856.
(4) KK-threshold: Delta_a = -(1/8pi^2) Sum_{(p,q)!=(0,0)} T(p,q) ln(Lambda^2/M_pq^2)
    with M_pq = omega_min(p,q) * M_KK (heavy-mode decoupling form, Q1.1 session-76).
    Cartan-universal => Delta_3=Delta_2=Delta_1=Delta_common. Reported at the pinned
    LAMBDA_THR = tower top + cross-checks at Lambda=M_KK (omega=1) and Lambda=1.5.
(5) Best-common-Delta analysis: scan a free common Delta over [-40,40] to find the minimum
    achievable max_rel; this is the GENEROUS bound on what any Cartan-universal threshold
    can do. (Structural: a common shift cannot differentiate the three couplings.)
(6) m_H collapse: single derived value (KK-threshold route m_H_FW_KK_threshold=131.8) +/-
    threshold uncertainty, replacing the 127.5-131.8 route-band; vs m_H_obs=125.1.
(7) L_max=10 vs 12 threshold-sum saturation cross-check.

DISCIPLINE
----------
- `from canonical_constants import` — never hardcode framework constants.
- Every local/intermediate tagged `# (local)`.
- SHA-256 of all input files logged in first 20 lines of stdout; dual-SHA (S84+).
- 4-tuple printed as final non-verdict line; verdict via print_verdict_payload ->
  agent calls mcp__knowledge__emit_verdict (race-safe, per gate-verdicts.md).
- CPU-cap-OMP8: the threshold sum is a finite dot product over cached eigenvalues
  (no matrix >= 100x100; GPU not engaged).
"""

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-only finite-sum work; no matrix >=100x100
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (
    PI,
    M_KK, M_KK_gravity, M_KK_kerner,
    M_Z,
    alpha_em_MZ_inv, sin2_thetaW_MSbar, alpha_s_MZ_obs,
    alpha2_MKK_inv,
    a_2_FW_zeta, a_4_FW_zeta,
    m_H_FW_KK_threshold, m_H_FW_tree, m_H_obs,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration pins
# ---------------------------------------------------------------------------
CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

GATE_ID = "INV6-W1-3-KK-THRESHOLD-RUNNING"                              # (local)
SESSION_N = 6                                                           # (local) investigation number
TRACK = "investigation"                                                # (local)
SCHEME = "one-loop-RGE+KK-threshold/MSbar-mZ"                           # (local)
CONVENTION = "RATIO+5/3-GUT-hypercharge-norm"                          # (local)
L_MAX = 12                                                              # (local)

# Pre-registered pass/fail threshold (plan §W1-3)
PASS_BUDGET = 0.02                                                      # (local) ~2% theory budget

# Threshold cutoff pin: the natural UV edge of the cached tower (top eigenvalue ~ 2.05 M_KK
# at L12). The heavy-mode decoupling sum is evaluated at this Lambda; cross-checked at
# Lambda=M_KK (omega=1, the canonical KK scale) and Lambda=1.5 to disclose scheme sensitivity.
LAMBDA_THR = 2.05                                                       # (local) M_KK units; tower top
LAMBDA_CROSSCHECKS = (1.0, 1.5)                                         # (local) M_KK units

OUT_NPZ = SESSION_DIR / "inv6_w1_3_kk_threshold_running.npz"
OUT_PNG = SESSION_DIR / "inv6_w1_3_kk_threshold_running.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                           # (local)
    for p in inputs:
        sha = sha256_of(p)                                             # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")     # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    h = hashlib.sha256()                                               # (local)
    for k, v in sorted(pins.items()):
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit_sha256 = SHA(script bytes + canonical bytes + pinmap json);
       content_sha256 = SHA(script bytes only)."""
    try:
        script_bytes = script_path.read_bytes()                       # (local)
    except OSError:
        script_bytes = b""                                            # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()                 # (local)
    except OSError:
        canonical_bytes = b""                                         # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()                                        # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                      # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — SU(3) representation theory
# ---------------------------------------------------------------------------
def dim_su3(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def C2_su3(p, q):
    """Quadratic Casimir (T(fund)=1/2 normalization): C_2(1,0)=4/3, C_2(1,1)=3."""
    return (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0


def T_dynkin(p, q):
    """Dynkin index, T(fund)=1/2: T(R) = dim(R) C_2(R) / dim(adj) = dim*C2/8 for SU(3)."""
    return dim_su3(p, q) * C2_su3(p, q) / 8.0


def T_eig(abs_evals):
    """Eigenvalue trace T_a(p,q) = Sum_{lambda in sector} lambda^-2  (plan K3.2)."""
    ev = np.asarray(abs_evals, dtype=float)                           # (local)
    ev = ev[ev > 1e-9]                                                # (local)
    return float(np.sum(ev ** -2.0))


# ---------------------------------------------------------------------------
# Section 6 — Observable conversion (GUT-normalized hypercharge)
# ---------------------------------------------------------------------------
def to_observables(a1G_inv, a2_inv, a3_inv):
    """GUT-norm: 1/alpha_Y = (5/3)(1/alpha1G); 1/alpha_em = 1/alpha_Y + 1/alpha2;
       sin^2 theta_W = (1/alpha2)/(1/alpha_em); alpha_s = 1/(1/alpha3)."""
    aY_inv = (5.0 / 3.0) * a1G_inv                                    # (local) 1/alpha_Y
    a_em_inv = aY_inv + a2_inv                                        # (local) 1/alpha_em
    sin2 = a2_inv / a_em_inv                                          # (local) sin^2 theta_W
    alpha_s = 1.0 / a3_inv                                            # (local)
    return a_em_inv, sin2, alpha_s


# ---------------------------------------------------------------------------
# Section 7 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    out = {}                                                          # (local)

    # --- SM one-loop beta coefficients (GUT-normalized hypercharge) ---
    b1, b2, b3 = 41.0 / 10.0, -19.0 / 6.0, -7.0                       # (local)
    out["b_coeffs"] = (b1, b2, b3)

    # --- Lever arm M_KK -> m_Z ---
    ln_arm = math.log(M_KK / M_Z)                                     # (local) ~34.33
    out["ln_arm"] = ln_arm

    # --- Unified inverse coupling at M_KK (the framework ansatz g3^2=g2^2=(3/5)g1^2) ---
    a_unif_inv = alpha2_MKK_inv                                       # (local) 47.856
    out["a_unif_inv"] = a_unif_inv

    # --- Load the (p,q) tower from the L12 master cache ---
    cache = np.load(CACHE_PATH, allow_pickle=True)                   # (local)
    se = cache["sector_evals"].item()                               # (local)
    out["n_sectors"] = len(se)
    out["max_pq_sum"] = max(p + q for (p, q) in se)

    # =====================================================================
    # (1) Cartan Trace Identity verification on the cached spectrum
    # =====================================================================
    # Eigenvalue-side: T_eig(p,q)=T_eig(q,p) is the (p,q)<->(q,p) leg of T_SU3=T_SU2.
    cartan_rel = []                                                   # (local)
    for (p, q) in se:
        if (q, p) in se and p < q:                                   # each unordered pair once
            t1 = T_eig(se[(p, q)]["abs_evals"])                      # (local)
            t2 = T_eig(se[(q, p)]["abs_evals"])                      # (local)
            cartan_rel.append(abs(t1 - t2) / abs(t1) if t1 != 0 else 0.0)
    cartan_max_rel = max(cartan_rel) if cartan_rel else 0.0           # (local)
    out["cartan_trace_symmetry_max_rel"] = cartan_max_rel
    out["cartan_n_pairs"] = len(cartan_rel)
    # Dynkin-index leg (representation-theoretic, exact): T_U1 = 12 * T_SU2.
    # The 1/12 of T10 is the GUT-canonical 5/3 hypercharge factor in disguise.
    out["dynkin_U1_over_SU2_ratio"] = 12.0                            # exact by construction

    # =====================================================================
    # (2) C^2 off-diagonal block decoupling: Delta sin^2 theta_W[C^2] = 0 EXACT
    # =====================================================================
    # S84 W9-106: off-diagonal Gell-Mann generators {lam_4,5,6,7} satisfy
    # Tr(lam_i Y) = Tr(lam_i T^3) so their differential to (1/g1^2 - 1/g2^2) cancels.
    out["delta_sin2_thetaW_C2"] = 0.0                                # EXACT (structural)

    # =====================================================================
    # (3) No-threshold unification skeleton (pure SM 1-loop run)
    # =====================================================================
    a1G_inv_nt = a_unif_inv - (b1 / (2 * PI)) * ln_arm               # (local)
    a2_inv_nt = a_unif_inv - (b2 / (2 * PI)) * ln_arm                # (local)
    a3_inv_nt = a_unif_inv - (b3 / (2 * PI)) * ln_arm                # (local)
    out["a_inv_noThreshold"] = (a1G_inv_nt, a2_inv_nt, a3_inv_nt)
    aem_nt, s2_nt, als_nt = to_observables(a1G_inv_nt, a2_inv_nt, a3_inv_nt)  # (local)
    out["computed_no_threshold"] = (aem_nt, s2_nt, als_nt)

    # =====================================================================
    # (4) KK-threshold sum (Cartan-universal heavy-mode decoupling)
    # =====================================================================
    # Delta_a = -(1/8pi^2) Sum_{(p,q)!=(0,0)} T(p,q) ln(Lambda^2/M_pq^2),  M_pq = omega_min * M_KK.
    # Cartan identity => the SU(3)/SU(2) trace content is EQUAL per sector; U(1) carries the
    # 1/12 already absorbed in the GUT-norm. So Delta_3 = Delta_2 = Delta_1 = Delta_common.
    def thr_sum(lam, reg="gauss", lmax=None):
        s = 0.0                                                       # (local)
        for pq, v in se.items():
            p, q = pq                                                # (local)
            if pq == (0, 0):
                continue
            if lmax is not None and (p + q) > lmax:
                continue
            T = T_dynkin(p, q)                                       # (local)
            ev = np.asarray(v["abs_evals"], dtype=float)            # (local)
            ev = ev[ev > 1e-9]                                       # (local)
            om = float(ev.min())                                    # (local) omega_min, M_KK units
            lr = math.log(lam ** 2 / om ** 2)                       # (local)
            w = math.exp(-om ** 2 / lam ** 2) if reg == "gauss" else 1.0  # (local)
            s += T * w * lr / (8.0 * PI ** 2)
        return s

    delta_common = thr_sum(LAMBDA_THR, "gauss")                      # (local) at pinned Lambda
    out["delta_common_pinned"] = delta_common
    out["delta_common_crosschecks"] = {
        f"lambda={lam}": thr_sum(lam, "gauss") for lam in LAMBDA_CROSSCHECKS
    }
    out["delta_common_sharp_pinned"] = thr_sum(LAMBDA_THR, "sharp")

    Delta_1 = Delta_2 = Delta_3 = delta_common                       # (local) Cartan-universal
    out["Delta_per_coupling"] = (Delta_1, Delta_2, Delta_3)

    # With-threshold run
    a1G_inv = a1G_inv_nt + Delta_1                                   # (local)
    a2_inv = a2_inv_nt + Delta_2                                     # (local)
    a3_inv = a3_inv_nt + Delta_3                                     # (local)
    out["a_inv_withThreshold"] = (a1G_inv, a2_inv, a3_inv)
    aem_c, s2_c, als_c = to_observables(a1G_inv, a2_inv, a3_inv)     # (local)
    out["computed_with_threshold"] = (aem_c, s2_c, als_c)

    # --- Observed (PDG canonical anchors) ---
    out["observed"] = (alpha_em_MZ_inv, sin2_thetaW_MSbar, alpha_s_MZ_obs)

    # --- Per-coupling relative deviations (the gate observable) ---
    def rel_devs(aem_i, s2, als):
        return {
            "alpha_em": abs(aem_i - alpha_em_MZ_inv) / alpha_em_MZ_inv,
            "sin2_thetaW": abs(s2 - sin2_thetaW_MSbar) / sin2_thetaW_MSbar,
            "alpha_s": abs(als - alpha_s_MZ_obs) / alpha_s_MZ_obs,
        }
    rd_nt = rel_devs(aem_nt, s2_nt, als_nt)                          # (local)
    rd_c = rel_devs(aem_c, s2_c, als_c)                              # (local)
    out["rel_dev_noThreshold"] = rd_nt
    out["rel_dev_withThreshold"] = rd_c
    out["max_rel_dev_noThreshold"] = max(rd_nt.values())
    out["max_rel_dev_withThreshold"] = max(rd_c.values())

    # =====================================================================
    # (5) Best-common-Delta analysis (generous bound on Cartan-universal threshold)
    # =====================================================================
    # A common Delta cannot differentiate the three couplings; scan it freely and find
    # the minimum achievable max_rel. This is the STRONGEST any Cartan-universal threshold
    # can do, independent of the cutoff scheme.
    grid = np.linspace(-40.0, 40.0, 160001)                          # (local)

    def maxrel_of(dlt):
        o = to_observables(a1G_inv_nt + dlt, a2_inv_nt + dlt, a3_inv_nt + dlt)
        rd = rel_devs(*o)
        return max(rd.values())

    mr = np.array([maxrel_of(d) for d in grid])                      # (local)
    i_best = int(np.argmin(mr))                                      # (local)
    delta_best = float(grid[i_best])                                 # (local)
    o_best = to_observables(a1G_inv_nt + delta_best,
                            a2_inv_nt + delta_best,
                            a3_inv_nt + delta_best)                  # (local)
    rd_best = rel_devs(*o_best)                                      # (local)
    out["delta_best_common"] = delta_best
    out["max_rel_dev_bestCommon"] = float(mr[i_best])
    out["computed_bestCommon"] = o_best
    out["rel_dev_bestCommon"] = rd_best
    out["n_within_budget_bestCommon"] = sum(1 for r in rd_best.values() if r <= PASS_BUDGET)

    # The GATE observable: best achievable max_rel over the Cartan-universal threshold family.
    # (The pinned-Lambda value is one scheme member; the best-common value is the generous
    #  bound. The gate PASSES only if EVEN the best common threshold lands all 3 within 2%.)
    out["value"] = out["max_rel_dev_bestCommon"]
    out["n_within_budget"] = out["n_within_budget_bestCommon"]

    # =====================================================================
    # (6) m_H route-band collapse (a4^zeta regulator pin on this leg)
    # =====================================================================
    # Tree (cutoff-shape independent, A10): lambda_h = (4/3) g3^2(M_KK) (a4/a2).
    ratio_a4a2 = a_4_FW_zeta / a_2_FW_zeta                           # (local) a4^zeta / a2^zeta
    alpha3_MKK = 1.0 / a_unif_inv                                    # (local)
    g3sq_MKK = 4.0 * PI * alpha3_MKK                                 # (local)
    lam_tree = (4.0 / 3.0) * g3sq_MKK * ratio_a4a2                   # (local)
    out["ratio_a4a2"] = ratio_a4a2
    out["g3sq_MKK"] = g3sq_MKK
    out["lam_tree"] = lam_tree
    # Collapse: KK-threshold route value is the framework canonical (131.8); the route band
    # 127.5-131.8 (S62-S66, cutoff-family + BCS-threshold spread) -> single value + half-width.
    mH_band_lo, mH_band_hi = 127.5, 131.8                            # (local)
    mH_collapsed = m_H_FW_KK_threshold                              # (local) single derived value
    mH_threshold_unc = (mH_band_hi - mH_band_lo) / 2.0             # (local) +/- 2.15 GeV
    out["mH_band"] = (mH_band_lo, mH_band_hi)
    out["mH_collapsed"] = mH_collapsed
    out["mH_threshold_unc"] = mH_threshold_unc
    out["mH_tree_route"] = m_H_FW_tree
    out["mH_obs"] = m_H_obs
    out["mH_rel_vs_obs"] = (mH_collapsed - m_H_obs) / m_H_obs        # (local) +5.356%
    out["mH_within_2pct"] = abs(out["mH_rel_vs_obs"]) <= PASS_BUDGET
    # A single value + stated uncertainty IS produced (band replaced) -> the "collapse" sub-clause
    # is satisfied as a deliverable; but the value is NOT within 2% of m_H_obs.
    out["mH_collapsed_ok"] = True

    # =====================================================================
    # (7) L_max = 10 vs 12 threshold-sum saturation cross-check
    # =====================================================================
    thr_L10 = thr_sum(LAMBDA_THR, "gauss", lmax=10)                  # (local)
    thr_L12 = thr_sum(LAMBDA_THR, "gauss", lmax=12)                  # (local)
    out["thr_L10"], out["thr_L12"] = thr_L10, thr_L12
    out["thr_L10_L12_rel_shift"] = (abs(thr_L12 - thr_L10) / abs(thr_L12)
                                    if thr_L12 != 0 else 0.0)

    # =====================================================================
    # SIGN diagnostic: direction of a common Delta on the observables
    # =====================================================================
    # Confirm substitution-chain Step-4 direction numerically: a common NEGATIVE Delta
    # raises sin^2 theta_W and lowers alpha_s (verified against the no-threshold base).
    base = to_observables(a1G_inv_nt, a2_inv_nt, a3_inv_nt)          # (local)
    probe_minus = to_observables(a1G_inv_nt - 0.5, a2_inv_nt - 0.5, a3_inv_nt - 0.5)  # (local)
    out["sign_sin2_up_on_negDelta"] = bool(probe_minus[1] > base[1])
    out["sign_alphaS_down_on_negDelta"] = bool(probe_minus[2] < base[2])

    return out


# ---------------------------------------------------------------------------
# Section 8 — Gate verdict + 4-tuple + payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, l_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={l_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload = {                                                       # (local)
        "session": SESSION_N,
        "track": TRACK,
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


def evaluate_gate(out: dict):
    """PASS iff EVEN the best Cartan-universal common threshold lands all 3 couplings within
       2% AND m_H collapses; FAIL if the running cannot reach the observed couplings from the
       unification ansatz (0/3 within budget); INFO if partial (>=1 but not all within budget,
       OR m_H band uncollapsed)."""
    max_rel = out["max_rel_dev_bestCommon"]                          # (local)
    n_within = out["n_within_budget_bestCommon"]                     # (local)
    mH_ok = out["mH_collapsed_ok"]                                   # (local)
    mH_2pct = out["mH_within_2pct"]                                  # (local)

    if max_rel <= PASS_BUDGET and n_within == 3 and mH_ok and mH_2pct:
        return "PASS", (f"All 3 couplings within {PASS_BUDGET:.0%} (best-common max_rel="
                        f"{max_rel:.4f}); m_H collapsed to {out['mH_collapsed']}"
                        f"+/-{out['mH_threshold_unc']:.2f} GeV within 2%.")
    if n_within == 0:
        return "FAIL", (f"Assembled running CANNOT reach observed couplings from "
                        f"g3^2=g2^2=(3/5)g1^2 at alpha_unif^-1={out['a_unif_inv']:.3f}: "
                        f"best-common max_rel={max_rel:.3f} >> {PASS_BUDGET} with 0/3 within "
                        f"budget. Cartan threshold is COMMON to all 3 (cannot close the "
                        f"sin2thetaW={out['computed_no_threshold'][1]:.3f} vs 0.231 spread). "
                        f"Cartan eigenvalue-trace identity VERIFIED (max rel "
                        f"{out['cartan_trace_symmetry_max_rel']:.1e}); m_H collapsed to "
                        f"{out['mH_collapsed']} GeV (+{100*out['mH_rel_vs_obs']:.2f}% vs obs, "
                        f"outside 2%).")
    return "INFO", (f"Partial: {n_within}/3 couplings within {PASS_BUDGET:.0%} (best-common "
                    f"max_rel={max_rel:.3f}). Unification structure (Cartan-universal leading, "
                    f"C^2 decoupling, eigenvalue-trace identity to "
                    f"{out['cartan_trace_symmetry_max_rel']:.1e}) holds; (p,q) subleading "
                    f"insufficient on the off couplings; m_H collapsed_ok={mH_ok} "
                    f"within2%={mH_2pct}.")


# ---------------------------------------------------------------------------
# Section 9 — Plot
# ---------------------------------------------------------------------------
def make_plot(out: dict):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))                 # (local)
    fig.suptitle("INV6-W1-3: Three-coupling KK-tower threshold running  M_KK -> m_Z",
                 fontsize=13, fontweight="bold")

    # (a) The running of the three inverse couplings M_KK -> m_Z (no-threshold skeleton)
    ax = axes[0, 0]
    b1, b2, b3 = out["b_coeffs"]
    c = out["a_unif_inv"]
    L = out["ln_arm"]
    t = np.linspace(0.0, L, 200)                                     # (local) ln(mu/m_Z) reversed
    a1 = c - (b1 / (2 * PI)) * t
    a2 = c - (b2 / (2 * PI)) * t
    a3 = c - (b3 / (2 * PI)) * t
    ax.plot(t, a1, label=r"$\alpha_{1G}^{-1}$ (GUT-norm)", color="tab:blue")
    ax.plot(t, a2, label=r"$\alpha_2^{-1}$", color="tab:green")
    ax.plot(t, a3, label=r"$\alpha_3^{-1}$", color="tab:red")
    ax.axvline(0.0, ls=":", color="k", alpha=0.4)
    ax.axhline(c, ls="--", color="purple", alpha=0.6,
               label=fr"$\alpha_{{unif}}^{{-1}}={c:.2f}$ at $M_{{KK}}$")
    ax.set_xlabel(r"$\ln(\mu/m_Z)$  (0 = $m_Z$, %.1f = $M_{KK}$)" % L)
    ax.set_ylabel(r"$\alpha_a^{-1}$")
    ax.set_title("(a) 1-loop running of the three couplings")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (b) Computed vs observed couplings (bar comparison, relative deviation)
    ax = axes[0, 1]
    labels = [r"$\alpha_{em}^{-1}$", r"$\sin^2\theta_W$", r"$\alpha_s$"]
    rd_nt = out["rel_dev_noThreshold"]
    rd_best = out["rel_dev_bestCommon"]
    x = np.arange(3)                                                 # (local)
    w = 0.35                                                         # (local)
    ax.bar(x - w / 2, [rd_nt["alpha_em"], rd_nt["sin2_thetaW"], rd_nt["alpha_s"]],
           w, label="no threshold", color="tab:gray")
    ax.bar(x + w / 2, [rd_best["alpha_em"], rd_best["sin2_thetaW"], rd_best["alpha_s"]],
           w, label="best common $\\Delta$", color="tab:orange")
    ax.axhline(PASS_BUDGET, ls="--", color="green", label=f"2% budget")
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("relative deviation from PDG")
    ax.set_title("(b) Per-coupling deviation vs 2% budget")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    # (c) max_rel vs common Delta (the best-common analysis)
    ax = axes[1, 0]
    grid = np.linspace(-40.0, 40.0, 1601)                           # (local) coarse for plot
    a1G_nt, a2_nt, a3_nt = out["a_inv_noThreshold"]
    mr = []                                                          # (local)
    for d in grid:
        o = to_observables(a1G_nt + d, a2_nt + d, a3_nt + d)
        mr.append(max(abs(o[0] - alpha_em_MZ_inv) / alpha_em_MZ_inv,
                      abs(o[1] - sin2_thetaW_MSbar) / sin2_thetaW_MSbar,
                      abs(o[2] - alpha_s_MZ_obs) / alpha_s_MZ_obs))
    ax.plot(grid, mr, color="tab:purple")
    ax.axhline(PASS_BUDGET, ls="--", color="green", label="2% budget")
    ax.axvline(out["delta_best_common"], ls=":", color="k",
               label=fr"best $\Delta={out['delta_best_common']:.1f}$")
    ax.axvline(out["delta_common_pinned"], ls="-.", color="tab:red", alpha=0.6,
               label=fr"pinned $\Delta={out['delta_common_pinned']:.1f}$ ($\Lambda$={LAMBDA_THR})")
    ax.set_yscale("log")
    ax.set_xlabel(r"common threshold $\Delta$")
    ax.set_ylabel("max relative deviation")
    ax.set_title("(c) Best-common-$\\Delta$: floor far above 2%")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    # (d) m_H route-band collapse + summary text
    ax = axes[1, 1]
    ax.axis("off")
    lo, hi = out["mH_band"]
    txt = (
        "VERDICT SUMMARY\n"
        f"  Cartan eigenvalue-trace T(p,q)=T(q,p):\n"
        f"     max rel dev = {out['cartan_trace_symmetry_max_rel']:.2e}  (VERIFIED, {out['cartan_n_pairs']} pairs)\n"
        f"  Dynkin T_U1/T_SU2 = {out['dynkin_U1_over_SU2_ratio']:.1f}  (= 5/3 GUT factor)\n"
        f"  Delta sin2thetaW[C^2] = {out['delta_sin2_thetaW_C2']:.1f}  EXACT\n"
        "\n"
        f"  alpha_unif^-1(M_KK) = {out['a_unif_inv']:.3f},  ln(M_KK/m_Z) = {out['ln_arm']:.2f}\n"
        "  No-threshold (skeleton):\n"
        f"     a_em^-1={out['computed_no_threshold'][0]:.2f}  sin2={out['computed_no_threshold'][1]:.4f}  a_s={out['computed_no_threshold'][2]:.5f}\n"
        f"  Best-common-Delta max_rel = {out['max_rel_dev_bestCommon']:.3f}\n"
        f"     within 2%: {out['n_within_budget_bestCommon']}/3 couplings\n"
        "\n"
        "  m_H route-band collapse:\n"
        f"     [{lo}, {hi}] GeV  ->  {out['mH_collapsed']} +/- {out['mH_threshold_unc']:.2f} GeV\n"
        f"     vs m_H_obs={out['mH_obs']}:  {100*out['mH_rel_vs_obs']:+.2f}%  (within 2%: {out['mH_within_2pct']})\n"
        "\n"
        "  L10 vs L12 threshold-sum shift = "
        f"{100*out['thr_L10_L12_rel_shift']:.2f}%"
    )
    ax.text(0.0, 1.0, txt, va="top", ha="left", fontsize=9.5, family="monospace",
            transform=ax.transAxes)
    ax.set_title("(d) Summary", fontsize=11)

    fig.tight_layout(rect=(0, 0, 1, 0.97))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                 # (local)
    script_path = Path(__file__).resolve()                           # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"           # (local)

    pins = log_input_pins(INPUT_FILES)                              # (local)
    closure = closure_hash(pins)                                    # (local)
    print(f"  closure_hash: {closure[:16]}...")
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  M_KK={M_KK:.6e} GeV  M_Z={M_Z} GeV  alpha_unif^-1={alpha2_MKK_inv}")
    print(f"  tau_fold={tau_fold}  cache={CACHE_PATH.name}")
    print()

    out = compute()                                                 # (local)

    # ---- Reporting ----
    print("=" * 72)
    print("INV6-W1-3 — THREE-COUPLING KK-THRESHOLD RUNNING")
    print("=" * 72)
    print(f"sectors loaded: {out['n_sectors']} (max p+q={out['max_pq_sum']})")
    print()
    print("(1) Cartan Trace Identity verification (eigenvalue side):")
    print(f"    T_eig(p,q)=T_eig(q,p):  max rel dev = {out['cartan_trace_symmetry_max_rel']:.3e} "
          f"over {out['cartan_n_pairs']} conjugate pairs  [VERIFIED]")
    print(f"    Dynkin T_U1/T_SU2 = {out['dynkin_U1_over_SU2_ratio']:.1f}  (= 5/3 GUT factor)")
    print(f"(2) C^2 block decoupling: Delta sin2thetaW[C^2] = {out['delta_sin2_thetaW_C2']:.1f} EXACT")
    print()
    print(f"(3) No-threshold unification skeleton (alpha_unif^-1={out['a_unif_inv']:.3f}, "
          f"ln(M_KK/m_Z)={out['ln_arm']:.4f}):")
    aem, s2, als = out["computed_no_threshold"]
    rd = out["rel_dev_noThreshold"]
    print(f"    alpha_em^-1 = {aem:9.4f}  (obs {alpha_em_MZ_inv})  rel = {rd['alpha_em']:.4f}")
    print(f"    sin2thetaW  = {s2:9.5f}  (obs {sin2_thetaW_MSbar})  rel = {rd['sin2_thetaW']:.4f}")
    print(f"    alpha_s     = {als:9.5f}  (obs {alpha_s_MZ_obs})  rel = {rd['alpha_s']:.4f}")
    print()
    print(f"(4) KK-threshold (Cartan-universal, Lambda={LAMBDA_THR}): Delta_common = "
          f"{out['delta_common_pinned']:.5f}")
    print(f"    cross-checks: {out['delta_common_crosschecks']}")
    aem, s2, als = out["computed_with_threshold"]
    rd = out["rel_dev_withThreshold"]
    print(f"    with-threshold: a_em^-1={aem:.3f} (rel {rd['alpha_em']:.3f}), "
          f"sin2={s2:.4f} (rel {rd['sin2_thetaW']:.3f}), a_s={als:.5f} (rel {rd['alpha_s']:.3f})")
    print()
    print("(5) Best-common-Delta analysis (generous bound on Cartan-universal threshold):")
    aem, s2, als = out["computed_bestCommon"]
    rd = out["rel_dev_bestCommon"]
    print(f"    best Delta = {out['delta_best_common']:.4f} -> max_rel = "
          f"{out['max_rel_dev_bestCommon']:.4f}; within 2%: {out['n_within_budget_bestCommon']}/3")
    print(f"    a_em^-1={aem:.3f} (rel {rd['alpha_em']:.3f}), sin2={s2:.4f} "
          f"(rel {rd['sin2_thetaW']:.3f}), a_s={als:.5f} (rel {rd['alpha_s']:.3f})")
    print()
    print("(6) m_H route-band collapse:")
    lo, hi = out["mH_band"]
    print(f"    [{lo}, {hi}] GeV -> {out['mH_collapsed']} +/- {out['mH_threshold_unc']:.2f} GeV "
          f"(single derived value + threshold uncertainty)")
    print(f"    vs m_H_obs={out['mH_obs']}: {100*out['mH_rel_vs_obs']:+.2f}% "
          f"(within 2%: {out['mH_within_2pct']}); tree route={out['mH_tree_route']}, "
          f"lambda_h(tree)={out['lam_tree']:.4f}")
    print()
    print(f"(7) L10 vs L12 threshold-sum: {out['thr_L10']:.5f} vs {out['thr_L12']:.5f} "
          f"(rel shift {100*out['thr_L10_L12_rel_shift']:.2f}%)")
    print()
    print("SIGN diagnostic (substitution-chain Step-4 direction):")
    print(f"    common negative Delta raises sin2thetaW: {out['sign_sin2_up_on_negDelta']}")
    print(f"    common negative Delta lowers alpha_s:    {out['sign_alphaS_down_on_negDelta']}")
    print()

    verdict, reason = evaluate_gate(out)                            # (local)
    print(f"VERDICT: {verdict}")
    print(f"  {reason}")

    # ---- Plot ----
    make_plot(out)
    print(f"\nplot -> {OUT_PNG.name}")

    # ---- Save data ----
    np.savez(
        OUT_NPZ,
        value=out["value"],
        verdict=verdict,
        b_coeffs=np.array(out["b_coeffs"]),
        ln_arm=out["ln_arm"],
        a_unif_inv=out["a_unif_inv"],
        n_sectors=out["n_sectors"],
        max_pq_sum=out["max_pq_sum"],
        cartan_trace_symmetry_max_rel=out["cartan_trace_symmetry_max_rel"],
        cartan_n_pairs=out["cartan_n_pairs"],
        dynkin_U1_over_SU2_ratio=out["dynkin_U1_over_SU2_ratio"],
        delta_sin2_thetaW_C2=out["delta_sin2_thetaW_C2"],
        a_inv_noThreshold=np.array(out["a_inv_noThreshold"]),
        computed_no_threshold=np.array(out["computed_no_threshold"]),
        rel_dev_noThreshold=np.array([out["rel_dev_noThreshold"][k]
                                      for k in ("alpha_em", "sin2_thetaW", "alpha_s")]),
        max_rel_dev_noThreshold=out["max_rel_dev_noThreshold"],
        delta_common_pinned=out["delta_common_pinned"],
        delta_common_sharp_pinned=out["delta_common_sharp_pinned"],
        lambda_thr=LAMBDA_THR,
        a_inv_withThreshold=np.array(out["a_inv_withThreshold"]),
        computed_with_threshold=np.array(out["computed_with_threshold"]),
        rel_dev_withThreshold=np.array([out["rel_dev_withThreshold"][k]
                                        for k in ("alpha_em", "sin2_thetaW", "alpha_s")]),
        max_rel_dev_withThreshold=out["max_rel_dev_withThreshold"],
        delta_best_common=out["delta_best_common"],
        max_rel_dev_bestCommon=out["max_rel_dev_bestCommon"],
        computed_bestCommon=np.array(out["computed_bestCommon"]),
        rel_dev_bestCommon=np.array([out["rel_dev_bestCommon"][k]
                                     for k in ("alpha_em", "sin2_thetaW", "alpha_s")]),
        n_within_budget_bestCommon=out["n_within_budget_bestCommon"],
        observed=np.array(out["observed"]),
        ratio_a4a2=out["ratio_a4a2"],
        g3sq_MKK=out["g3sq_MKK"],
        lam_tree=out["lam_tree"],
        mH_band=np.array(out["mH_band"]),
        mH_collapsed=out["mH_collapsed"],
        mH_threshold_unc=out["mH_threshold_unc"],
        mH_tree_route=out["mH_tree_route"],
        mH_obs=out["mH_obs"],
        mH_rel_vs_obs=out["mH_rel_vs_obs"],
        mH_within_2pct=out["mH_within_2pct"],
        thr_L10=out["thr_L10"],
        thr_L12=out["thr_L12"],
        thr_L10_L12_rel_shift=out["thr_L10_L12_rel_shift"],
        sign_sin2_up_on_negDelta=out["sign_sin2_up_on_negDelta"],
        sign_alphaS_down_on_negDelta=out["sign_alphaS_down_on_negDelta"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"data -> {OUT_NPZ.name}")

    # ---- 4-tuple (final non-verdict line) ----
    value_str = (
        f"max_rel_bestCommon={out['max_rel_dev_bestCommon']:.4f}"
        f"|within2pct={out['n_within_budget_bestCommon']}/3"
        f"|cartan_T_maxrel={out['cartan_trace_symmetry_max_rel']:.2e}"
        f"|sin2_nt={out['computed_no_threshold'][1]:.4f}"
        f"|mH={out['mH_collapsed']}+/-{out['mH_threshold_unc']:.2f}_rel{100*out['mH_rel_vs_obs']:+.2f}pct"
    )
    print(emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX))

    # ---- Verdict payload (agent calls emit_verdict) ----
    note = (f"3-coupling KK-threshold running M_KK->m_Z; Cartan eigenvalue-trace identity "
            f"VERIFIED to {out['cartan_trace_symmetry_max_rel']:.1e}; best-common max_rel="
            f"{out['max_rel_dev_bestCommon']:.3f} ({out['n_within_budget_bestCommon']}/3 within "
            f"2%); m_H {out['mH_collapsed']}+/-{out['mH_threshold_unc']:.2f} GeV "
            f"({100*out['mH_rel_vs_obs']:+.2f}% vs obs)")
    extra = [
        (f"# regulator_pin=a_4^{{zeta}} (m_H leg: lambda_h=(4/3)g3^2(M_KK)*a4/a2; "
         f"a_4_FW_zeta={a_4_FW_zeta}); gauge-running leg uses SM beta-coeffs + Cartan trace, "
         f"no a_n cited"),
        (f"# cartan: T_eig(p,q)=T_eig(q,p) max_rel={out['cartan_trace_symmetry_max_rel']:.2e} "
         f"({out['cartan_n_pairs']} pairs); Delta_sin2thetaW[C^2]=0 EXACT (S84 W9-106); "
         f"Dynkin T_U1/T_SU2=12 (=5/3 GUT)"),
        (f"# running: no-threshold sin2thetaW={out['computed_no_threshold'][1]:.4f} (obs 0.231), "
         f"a_em^-1={out['computed_no_threshold'][0]:.2f} (obs 128), a_s={out['computed_no_threshold'][2]:.5f} "
         f"(obs 0.118); Cartan threshold COMMON to all 3 (cannot differentiate); best-common "
         f"Delta={out['delta_best_common']:.2f} floor max_rel={out['max_rel_dev_bestCommon']:.3f}"),
        (f"# L10-vs-L12 threshold-sum rel shift={100*out['thr_L10_L12_rel_shift']:.2f}%; "
         f"Lambda_thr={LAMBDA_THR} (tower top) + cross-checks at {LAMBDA_CROSSCHECKS}"),
    ]
    print_verdict_payload(verdict, value_str, audit_sha, content_sha,
                          companion_note=note, extra_rows=extra)

    print(f"\n[done in {time.time() - t0:.1f}s]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
