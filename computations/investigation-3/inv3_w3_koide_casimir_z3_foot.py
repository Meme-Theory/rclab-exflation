#!/usr/bin/env python3
"""
INV3-W3-5 — INV3-W3-5-KOIDE-CASIMIR-Z3-FOOT
===========================================

Gate: INV3-W3-5  ([CHAIN] trigger -> substitution chain mandatory; NOT [SIGN],
so NO schema-v2 3-tuple per plan §W3-5 schema_v2_3tuple_required: false.)

Pre-registered hypothesis (plan §W3-5):
  Koide's Q = (sum m_l)/(sum sqrt(m_l))^2 = 2/3 falls out of the framework's
  Casimir-envelope sqrt(m) vector sqrt(m_g) ~ exp(-k*C2(p,q)/2) over the THREE
  triality-distinct sectors (1,0)/(1,1)/(3,0), with the 45-deg Foot angle
  (cos^2(theta)=1/2 between the sqrt(m) vector and (1,1,1)) emerging from the Z3
  junction symmetry of the three wall types.

Pre-registered operator + boundary (plan §W3-5):
  |Q(k*) - 2/3| <= 1e-3  AND  |theta_Foot(k*) - 45deg| <= 0.5deg,
  with the achieving k* DERIVABLE from Z3 symmetry (not fitted).
  PASS  iff Q=2/3 AND theta=45deg at a Z3-FORCED k*.
  INFO  iff Q=2/3 achievable but ONLY by a fitted k (no Z3-symmetry forcing of k*),
        OR Q=2/3 at theta=45 but the Z3-forcing argument is not closed.
  FAIL  iff NO k gives Q=2/3 from exp(-k*C2/2) over (1,0)/(1,1)/(3,0).

--------------------------------------------------------------------------------
SUBSTRATE-FIRST FRAMING (phononic-framing.md)
--------------------------------------------------------------------------------
PARTICLE on a GEOMETRIC substrate. Koide's Q=2/3 is a charged-lepton mass
relation; the sqrt(m) vector IS Paasch's M-value vector M(j)=(m_j/m_e)^{1/3}.
The arrow is:

    D_K's three triality-distinct Peter-Weyl sectors (1,0)/(1,1)/(3,0)
      -> SU(3) quadratic Casimir C2 = (4/3, 3, 6)  [GEOMETRIC, exact]
      -> Casimir-envelope masses sqrt(m_g) = exp(-k*C2/2)
      -> the sqrt(m) "democratic" vector
      -> Koide Q and the Foot angle theta between sqrt(m) and (1,1,1).

The 45-deg Foot angle is a GEOMETRIC fact about the angle between the
Casimir-envelope sqrt(m) vector and the democratic direction (1,1,1) in
MASS-space. The gate asks whether the Z3 symmetry of the triality assignment
FORCES that 45-deg. This is the right way to address the 45-vs-120-deg
incommensurability (framework-paasch-potential.md §3.3): the Z3 walls meet at
120-deg in REAL space, but the Foot angle lives in MASS-space (set by the
triality-sector Casimirs). The substrate is NOT a container in which three
lepton masses "happen" to satisfy Q=2/3; Q=2/3 IS a statement about the geometry
of the Casimir-envelope over the three triality-odd sectors.

PRIOR FRAMEWORK CONTEXT (knowledge-MCP pre-compute):
  framework-paasch-potential.md line 461 already flags this exact hypothesis as
  "speculative but structurally motivated", and the JUNCTION-angle gate
  (effective spiral angle < 50-deg, "compatible with Paasch's 45-deg") is
  UNCOMPUTED. THIS gate makes it concrete and DECIDABLE on C2=(4/3,3,6).

--------------------------------------------------------------------------------
SUBSTITUTION CHAIN (plan §W3-5, verified by Sage pre-flight in-script)
--------------------------------------------------------------------------------
  Step 1: Koide Q = (sum m_l)/(sum sqrt(m_l))^2 [Koide 1983]. PDG: Q=0.66666051.
  Step 2: Foot (1994): Q=2/3 <=> cos^2(theta)=1/2 <=> theta=45deg, theta the angle
          between v=(sqrt(m_e),sqrt(m_mu),sqrt(m_tau)) and (1,1,1). This is an
          ALGEBRAIC IDENTITY, not an independent prediction.
  Step 3: Casimir-envelope sqrt(m_g)=exp(-k*C2(p,q)/2); C2=(4/3,3,6) for
          (1,0)/(1,1)/(3,0). v(k)=(exp(-2k/3), exp(-3k/2), exp(-3k)).
  Step 4: Q(k) = [exp(-4k/3)+exp(-3k)+exp(-6k)] / [exp(-2k/3)+exp(-3k/2)+exp(-3k)]^2.
          Solve Q(k)=2/3 for k*; check whether k* coincides with a Z3-symmetry-
          distinguished value (e.g. the democratic point where the three
          triality-odd amplitudes become equal).
  Step 5: theta_Foot(k)=arccos( [sum exp(-k*C2/2)] / [sqrt(3)*sqrt(sum exp(-k*C2))] );
          test theta_Foot(k*)=45deg.
  Direction: NOT pre-determinable at plan-freeze. The discriminator is whether
             Q(k) crosses 2/3 at a Z3-FORCED k* (derivation) or at an arbitrary
             fitted k (fit). In-script finding: the Z3-democratic point (k=0,
             all three sqrt(m) equal) gives Q=1/3 (the N-democratic value for
             N=3), NOT 2/3; Q=2/3 is reached only at a finite hierarchy point
             k*=1.7053, which matches NO Casimir/phi/golden constant within 2%.
             => Q=2/3 is REACHABLE-BY-FIT, NOT Z3-FORCED => INFO.

--------------------------------------------------------------------------------
MASS-PHENOMENOLOGY HONEST-COUNT DISCIPLINE
--------------------------------------------------------------------------------
The KILL criterion is pre-registered: distinguish derived-from-Z3 (a k* the Z3
symmetry singles out) from fitted-k (any k tuned to land Q=2/3). The Foot-45-deg
coincidence at k* is Foot's 1983/1994 ALGEBRAIC IDENTITY and is reported as such
(it is NOT a second, independent confirmation of the Z3 origin). A monotone Q(k)
with continuum range will cross 2/3 SOMEWHERE for a wide class of three-sector
envelopes; reachability alone is cheap and is INFO-level, not PASS-level.
"""

# ---------------------------------------------------------------------------
# Section 0 — Environment (closed-form 3x3 + k-scan; cpu-cap-OMP8 per plan)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants import (MANDATORY)
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (brings phi_paasch, M_KK, ...)
from canonical_constants import phi_paasch  # explicit for clarity

# ---------------------------------------------------------------------------
# Section 2 — Gate identity (module-level; consumed by print_verdict_payload)
# ---------------------------------------------------------------------------
SESSION = "3"                              # investigation number (track passed at emit)
GATE_ID = "INV3-W3-5"                       # short form per orchestrator override
SCHEME = "KOIDE-CASIMIR-Z3-FOOT"            # per orchestrator override (scheme= field)
CONVENTION = "RATIO"                        # Q is scale-invariant (ratio); plan §W3-5
L_MAX = "12"                                # cache cross-check sub-test 3 (analytic for 1-2)

THIS = Path(__file__).resolve()
INV3_DIR = THIS.parent
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
# THIS = .../computations/investigation-3/<script>.py ; parents[1] = .../computations
L12_CACHE = THIS.parents[1] / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = INV3_DIR / "inv3_w3_koide_casimir_z3_foot.npz"
OUT_PNG = INV3_DIR / "inv3_w3_koide_casimir_z3_foot.png"

# Pre-registered thresholds (plan §W3-5 strict_PASS_boundary; gate-local pins, NOT
# framework constants — they live only in this gate per gate-verdicts.md pre-reg protocol)
Q_TARGET = 2.0 / 3.0         # (local) Koide target, plan §W3-5
TOL_Q = 1e-3                 # (local) plan §W3-5 strict_PASS_boundary |Q-2/3|<=1e-3
THETA_TARGET_DEG = 45.0      # (local) Foot angle target, plan §W3-5
TOL_THETA_DEG = 0.5          # (local) plan §W3-5 strict_PASS_boundary |theta-45|<=0.5deg
Z3_FORCE_RELTOL = 0.02       # (local) Z3-forcing tolerance; same 2% as wave ratio gates (plan §W3-2)

# Casimir-envelope sector data (Sage-confirmed; cross-link session-100a-plan-w2.md)
SECTORS = [(1, 0), (1, 1), (3, 0)]          # the three triality-DISTINCT sectors
C2 = np.array([4.0 / 3.0, 3.0, 6.0])         # SU(3) quadratic Casimir C2(p,q)
# triality t(p,q)=(p-q) mod 3: (1,0)->1, (1,1)->0, (3,0)->0  -- see note in compute()


# ---------------------------------------------------------------------------
# Section 3 — Input-pin logging + dual-SHA (verbatim from script-template.py)
# ---------------------------------------------------------------------------
def sha256_of_file(path: Path) -> str:
    try:
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = b""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION.lstrip("Ss")),
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
# Section 4 — Koide / Foot closed-form helpers
# ---------------------------------------------------------------------------
def sqrt_m_vector(k, c2=C2):
    """Casimir-envelope sqrt(m_g) = exp(-k*C2/2)."""
    return np.exp(-k * np.asarray(c2) / 2.0)                       # (local)


def koide_Q(k, c2=C2):
    """Q(k) = sum(m) / (sum sqrt(m))^2, m_g = sqrt(m_g)^2 = exp(-k*C2)."""
    sm = sqrt_m_vector(k, c2)                                      # (local)
    num = np.sum(sm ** 2)                                          # (local)
    den = np.sum(sm) ** 2                                          # (local)
    return num / den


def foot_costheta(k, c2=C2):
    """cos(theta) between sqrt(m) vector and (1,1,1)."""
    v = sqrt_m_vector(k, c2)                                       # (local)
    return np.sum(v) / (np.linalg.norm(v) * np.sqrt(3.0))         # (local)


def foot_theta_deg(k, c2=C2):
    c = np.clip(foot_costheta(k, c2), -1.0, 1.0)                   # (local)
    return np.degrees(np.arccos(c))


def koide_Q_from_sqrtm(sm):
    """Q directly from a sqrt(m) vector (cache cross-check)."""
    sm = np.asarray(sm, dtype=float)                              # (local)
    return float(np.sum(sm ** 2) / np.sum(sm) ** 2)               # (local)


def foot_theta_deg_from_sqrtm(sm):
    sm = np.asarray(sm, dtype=float)                              # (local)
    c = np.sum(sm) / (np.linalg.norm(sm) * np.sqrt(3.0))         # (local)
    return float(np.degrees(np.arccos(np.clip(c, -1.0, 1.0))))    # (local)


def solve_Qeq(target, c2=C2, lo=1e-6, hi=8.0):
    """Bisection for Q(k)=target on [lo,hi]; returns k* or None if no crossing."""
    f = lambda kk: koide_Q(kk, c2) - target                       # (local)
    flo, fhi = f(lo), f(hi)                                        # (local)
    if flo * fhi > 0:
        return None
    for _ in range(200):                                          # (local)
        mid = 0.5 * (lo + hi)                                     # (local)
        fm = f(mid)                                               # (local)
        if abs(fm) < 1e-15:
            return mid
        if flo * fm <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute():
    out = {}                                                      # (local)

    # --- Sub-test 1: scan Q(k), find Q=2/3 crossing -----------------------
    k_grid = np.arange(0.0, 5.0 + 1e-9, 0.01)                     # (local) plan scan_range/step
    Q_grid = np.array([koide_Q(kk) for kk in k_grid])             # (local)
    theta_grid = np.array([foot_theta_deg(kk) for kk in k_grid])  # (local)

    k_star = solve_Qeq(Q_TARGET, lo=0.5, hi=3.0)                  # (local) Q=2/3 root
    Q_at_kstar = koide_Q(k_star) if k_star is not None else float("nan")        # (local)
    theta_at_kstar = foot_theta_deg(k_star) if k_star is not None else float("nan")  # (local)
    cos2_at_kstar = foot_costheta(k_star) ** 2 if k_star is not None else float("nan")  # (local)
    sqrtm_at_kstar = sqrt_m_vector(k_star) if k_star is not None else np.array([np.nan] * 3)  # (local)

    # Q at endpoints / democratic point
    Q_democratic = koide_Q(0.0)              # (local) k=0: all sqrt(m) equal (Z3-symmetric)
    Q_kinf = koide_Q(50.0)                   # (local) k->inf limit (->1)
    theta_democratic = foot_theta_deg(0.0)   # (local) at k=0, v parallel (1,1,1) => theta=0

    out.update(dict(k_grid=k_grid, Q_grid=Q_grid, theta_grid=theta_grid,
                    k_star=float(k_star) if k_star is not None else np.nan,
                    Q_at_kstar=float(Q_at_kstar), theta_at_kstar=float(theta_at_kstar),
                    cos2_at_kstar=float(cos2_at_kstar),
                    sqrtm_at_kstar=np.asarray(sqrtm_at_kstar, dtype=float),
                    Q_democratic=float(Q_democratic), Q_kinf=float(Q_kinf),
                    theta_democratic=float(theta_democratic)))

    # --- Sub-test 2 (the DISCRIMINATOR): is k* Z3-forced or fitted? --------
    # The Z3-democratic point is k=0 (the ONLY k where exp(-k*C2/2) are equal,
    # since C2=(4/3,3,6) are distinct). At k=0, Q=1/3 (the N=3 democratic Koide
    # value), NOT 2/3. So the symmetry-distinguished point does NOT give Q=2/3.
    # Test whether k* matches any Casimir/phi/golden-distinguished constant.
    golden = (1.0 + np.sqrt(5.0)) / 2.0                           # (local)
    fN = np.sqrt(5.0) - 1.0                                       # (local) Paasch M-ratio
    z3_candidates = {                                             # (local)
        "k=0_democratic_allsqrtm_equal": 0.0,
        "ln(phi_paasch)": float(np.log(phi_paasch)),
        "ln(golden)": float(np.log(golden)),
        "phi_paasch": float(phi_paasch),
        "golden_1.618": float(golden),
        "fN_sqrt5-1": float(fN),
        "1/fN": float(1.0 / fN),
        "C2(1,1)/C2(1,0)=9/4": 9.0 / 4.0,
        "3/2": 1.5,
        "5/3": 5.0 / 3.0,
        "ln(2)": float(np.log(2.0)),
        "ln(3)": float(np.log(3.0)),
    }
    z3_match = {}                                                 # (local)
    best_name, best_rel = None, np.inf                            # (local)
    for nm, val in z3_candidates.items():
        if val == 0.0:
            # democratic point: report its Q, not a k*-match
            z3_match[nm] = dict(value=val, rel_dev_to_kstar=np.nan,
                                Q_at_this_k=float(koide_Q(0.0)))
            continue
        rel = abs(k_star - val) / abs(val) if k_star is not None else np.nan  # (local)
        z3_match[nm] = dict(value=val, rel_dev_to_kstar=float(rel),
                            Q_at_this_k=float(koide_Q(val)))
        if rel < best_rel:
            best_rel, best_name = rel, nm
    z3_forced = bool(best_rel <= Z3_FORCE_RELTOL)                 # (local)

    out.update(dict(z3_best_match_name=best_name,
                    z3_best_match_reldev=float(best_rel),
                    z3_forced=z3_forced,
                    Q_at_democratic_point=float(koide_Q(0.0))))

    # --- Sub-test 3: cache realization (bottom-of-band masses) -------------
    cache_block = {}                                              # (local)
    cache_sha = sha256_of_file(L12_CACHE)                         # (local)
    if cache_sha != "MISSING":
        d = np.load(L12_CACHE, allow_pickle=True)                # (local)
        se = d["sector_evals"].item()                            # (local)
        lam_min = []                                             # (local)
        dims = []                                                # (local)
        for s in SECTORS:
            ae = np.asarray(se[s]["abs_evals"], dtype=float)     # (local)
            lam_min.append(float(np.min(ae)))                    # (local)
            dims.append(int(se[s]["dim"]))                       # (local)
        lam_min = np.array(lam_min)                              # (local)
        # Two cache-derived sqrt(m) realizations (independent of the analytic envelope):
        # (a) sqrt(m) ~ |lambda|_min directly (bottom-of-band as a mass proxy)
        # (b) sqrt(m) ~ exp(-|lambda|_min) (ladder mass m ~ exp(-2|lambda|_min))
        Q_cache_direct = koide_Q_from_sqrtm(lam_min)             # (local)
        theta_cache_direct = foot_theta_deg_from_sqrtm(lam_min)  # (local)
        sm_exp = np.exp(-lam_min)                                # (local)
        Q_cache_exp = koide_Q_from_sqrtm(sm_exp)                 # (local)
        theta_cache_exp = foot_theta_deg_from_sqrtm(sm_exp)      # (local)
        cache_block = dict(
            cache_lam_min=lam_min, cache_dims=np.array(dims),
            Q_cache_direct=float(Q_cache_direct),
            theta_cache_direct=float(theta_cache_direct),
            Q_cache_exp=float(Q_cache_exp),
            theta_cache_exp=float(theta_cache_exp),
        )
    out.update(cache_block)
    out["cache_present"] = bool(cache_sha != "MISSING")

    # --- PDG charged-lepton reference (the real Foot fact) -----------------
    me, mmu, mtau = 0.000510998950, 0.1056583755, 1.77686         # (local) PDG GeV
    v_pdg = np.array([np.sqrt(me), np.sqrt(mmu), np.sqrt(mtau)])  # (local)
    out["Q_pdg"] = koide_Q_from_sqrtm(v_pdg)                      # (local)
    out["theta_pdg_deg"] = foot_theta_deg_from_sqrtm(v_pdg)       # (local)

    return out


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict (pre-registered rubric, plan §W3-5)
# ---------------------------------------------------------------------------
def evaluate_gate(res):
    """
    PASS: Q=2/3 AND theta=45 at a Z3-FORCED k* (z3_forced True).
    INFO: Q=2/3 reachable (|Q-2/3|<=tol AND |theta-45|<=tol) but ONLY by a fitted k
          (z3_forced False), OR Foot-45 holds but Z3-forcing not closed.
    FAIL: no k gives Q=2/3 (k_star is None / Q crossing absent).
    """
    if res.get("k_star") is None or not np.isfinite(res.get("k_star", np.nan)):
        return "FAIL"
    q_ok = abs(res["Q_at_kstar"] - Q_TARGET) <= TOL_Q                    # (local)
    th_ok = abs(res["theta_at_kstar"] - THETA_TARGET_DEG) <= TOL_THETA_DEG  # (local)
    if not q_ok:
        return "FAIL"      # Q crossing exists but does not actually land 2/3 to tol
    # q_ok holds (Q=2/3 reached). The Foot-45 is the Foot identity (th_ok by construction).
    if res["z3_forced"]:
        return "PASS"      # the achieving k* is singled out by Z3 symmetry -> derivation
    return "INFO"          # reachable-by-fit; Z3 does NOT force k* -> not a derivation


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()

    # 1. Input pins
    pins = {
        "computations/_shared/canonical_constants.py": sha256_of_file(CANONICAL_PATH),
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": sha256_of_file(L12_CACHE),
    }
    print("=" * 78)
    print(f"{GATE_ID} — Koide Q=2/3 from Casimir-envelope over (1,0)/(1,1)/(3,0) + Z3 Foot angle")
    print("=" * 78)
    print("Input pins (SHA-256):")
    for k, v in sorted(pins.items()):
        print(f"  {k} = {v}")
    closure = closure_hash(pins)
    print(f"  closure (legacy): {closure[:16]}...")

    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  phi_paasch (canonical) = {phi_paasch}")
    print("-" * 78)

    # 2. Compute
    res = compute()

    # 3. Report
    print("SUB-TEST 1 — Q(k) scan + Q=2/3 crossing")
    print(f"  C2 sectors (1,0)/(1,1)/(3,0) = {tuple(C2)}")
    print(f"  Q(k=0, Z3-democratic, all sqrt(m) equal) = {res['Q_democratic']:.10f}   (= 1/3 for N=3; NOT 2/3)")
    print(f"  Q(k->inf)                                = {res['Q_kinf']:.10f}   (-> 1)")
    print(f"  k*  (Q=2/3 crossing)                     = {res['k_star']:.10f}")
    print(f"  Q(k*)                                    = {res['Q_at_kstar']:.10f}  (target 2/3={Q_TARGET:.10f})")
    print(f"  theta_Foot(k*)                           = {res['theta_at_kstar']:.8f} deg  (target 45)")
    print(f"  cos^2(theta)(k*)                         = {res['cos2_at_kstar']:.12f}  (Foot target 1/2)")
    print(f"  sqrt(m) vector at k*                     = {np.array2string(res['sqrtm_at_kstar'], precision=6)}")
    print()
    print("SUB-TEST 2 — DISCRIMINATOR: is k* Z3-FORCED or FITTED?")
    print(f"  Z3-democratic point is k=0 (only k with equal sqrt(m); C2 distinct) -> Q={res['Q_at_democratic_point']:.6f} (1/3, NOT 2/3)")
    print(f"  closest Z3/Casimir/phi/golden constant to k* : {res['z3_best_match_name']}  rel_dev={res['z3_best_match_reldev']*100:.3f}%")
    print(f"  Z3-FORCED (rel_dev <= {Z3_FORCE_RELTOL*100:.0f}%)?  {res['z3_forced']}")
    print()
    print("SUB-TEST 3 — cache realization (s84_spectrum_cache_L12_tau019.npz)")
    if res.get("cache_present"):
        print(f"  |lambda|_min for (1,0)/(1,1)/(3,0) = {np.array2string(res['cache_lam_min'], precision=6)}")
        print(f"  dims                               = {tuple(int(x) for x in res['cache_dims'])}")
        print(f"  Q (sqrt(m)=|lambda|_min direct)    = {res['Q_cache_direct']:.6f}  theta={res['theta_cache_direct']:.4f} deg")
        print(f"  Q (sqrt(m)=exp(-|lambda|_min))     = {res['Q_cache_exp']:.6f}  theta={res['theta_cache_exp']:.4f} deg")
    else:
        print("  CACHE MISSING -> sub-test 3 skipped (analytic sub-tests 1-2 carry the verdict)")
    print()
    print(f"  PDG charged-lepton check: Q={res['Q_pdg']:.8f}  theta={res['theta_pdg_deg']:.6f} deg  (the real Foot fact)")
    print("-" * 78)

    # 4. Verdict
    verdict = evaluate_gate(res)
    cache_present = res.get("cache_present", False)

    # descriptive value string (mass-phenomenology honest framing)
    value = (f"Q2/3_reachable_at_fitted_k*={res['k_star']:.6f}_Q={res['Q_at_kstar']:.6f}_"
             f"theta={res['theta_at_kstar']:.4f}deg_Z3democratic(k=0)Q=1/3_"
             f"k*-matches-no-Casimir/phi/golden-within-2pct(closest_{res['z3_best_match_name']}_"
             f"{res['z3_best_match_reldev']*100:.2f}pct)_Foot45=algebraic-identity_NOT-Z3-forced")
    # value cannot contain a single-quote per emit_verdict; ensure none
    value = value.replace("'", "")

    print(f"VERDICT: {verdict}")
    print(f"  value = {value}")

    # 5. Save data
    save = dict(
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        sectors=np.array(SECTORS), C2=C2,
        Q_target=Q_TARGET, tol_Q=TOL_Q, theta_target_deg=THETA_TARGET_DEG,
        tol_theta_deg=TOL_THETA_DEG, z3_force_reltol=Z3_FORCE_RELTOL,
        verdict=verdict, value=value,
        audit_sha256=audit_sha, content_sha256=content_sha,
        phi_paasch=float(phi_paasch),
        z3_match_json=json.dumps(
            {k: (v if not isinstance(v, dict) else v) for k, v in
             {kk: dict(value=vv["value"],
                       rel_dev_to_kstar=vv["rel_dev_to_kstar"],
                       Q_at_this_k=vv["Q_at_this_k"])
              for kk, vv in res.get("_z3_match", {}).items()}.items()}
        ) if res.get("_z3_match") else "{}",
    )
    # merge the scalar/array results (skip the big private dict if any)
    for k, v in res.items():
        if k.startswith("_"):
            continue
        save[k] = v
    np.savez_compressed(OUT_NPZ, **save)
    print(f"  data -> {OUT_NPZ.name}")

    # 6. Plot
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    ax = axes[0]
    ax.plot(res["k_grid"], res["Q_grid"], "b-", lw=2, label=r"$Q(k)$")
    ax.axhline(Q_TARGET, color="r", ls="--", lw=1.3, label=r"Koide $Q=2/3$")
    ax.axhline(1.0 / 3.0, color="g", ls=":", lw=1.3, label=r"$Q=1/3$ (k=0 democratic)")
    if np.isfinite(res["k_star"]):
        ax.axvline(res["k_star"], color="k", ls="-.", lw=1.0,
                   label=fr"$k^*={res['k_star']:.4f}$ (FITTED)")
        ax.plot([res["k_star"]], [res["Q_at_kstar"]], "ko", ms=7)
    ax.set_xlabel(r"$k$ (Casimir-envelope decay constant)")
    ax.set_ylabel(r"$Q(k)=\sum m / (\sum\sqrt{m})^2$")
    ax.set_title("Koide $Q(k)$ over (1,0)/(1,1)/(3,0), $C_2=(4/3,3,6)$\n"
                 "Z3-symmetric point $k{=}0$ gives $Q{=}1/3$, not $2/3$")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[1]
    ax.plot(res["k_grid"], res["theta_grid"], "m-", lw=2, label=r"$\theta_{\rm Foot}(k)$")
    ax.axhline(45.0, color="r", ls="--", lw=1.3, label=r"$45^\circ$ (Foot)")
    if np.isfinite(res["k_star"]):
        ax.axvline(res["k_star"], color="k", ls="-.", lw=1.0,
                   label=fr"$k^*={res['k_star']:.4f}$")
        ax.plot([res["k_star"]], [res["theta_at_kstar"]], "ko", ms=7)
    ax.set_xlabel(r"$k$")
    ax.set_ylabel(r"$\theta_{\rm Foot}$ between $\sqrt{m}$ and $(1,1,1)$ [deg]")
    ax.set_title(r"Foot angle: $\theta(k^*){=}45^\circ$ is Foot's IDENTITY ($Q{=}2/3\Leftrightarrow\cos^2\theta{=}1/2$)"
                 "\nnot an independent Z3 confirmation")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(f"INV3-W3-5  Koide-Casimir-Z3-Foot  —  VERDICT: {verdict}  "
                 f"(reachable-by-fit, NOT Z3-forced)", fontsize=11, y=1.02)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    print(f"  plot -> {OUT_PNG.name}")
    print("-" * 78)

    # 7. 4-tuple + emit payload
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    extra = [
        f"# INV3-W3-5 detail: k*={res['k_star']:.6f} Q(k*)={res['Q_at_kstar']:.8f} "
        f"theta(k*)={res['theta_at_kstar']:.6f}deg cos2={res['cos2_at_kstar']:.10f}; "
        f"Z3-democratic k=0 -> Q=1/3; z3_forced={res['z3_forced']} "
        f"(closest {res['z3_best_match_name']} {res['z3_best_match_reldev']*100:.2f}%); "
        f"Foot-45 = Foot 1994 algebraic identity (Q=2/3<=>cos^2theta=1/2)"
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="reachable-by-fit; NOT-Z3-forced; Foot-45=identity",
                          extra_rows=extra)
    print(f"  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
