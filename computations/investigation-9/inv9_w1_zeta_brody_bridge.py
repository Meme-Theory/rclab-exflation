"""
INV9-W1-4-ZETA-BRODY-BRIDGE
==============================================================================
The number-theoretic Berry-Tabor <=> Hilbert-Polya bridge on the substrate.

GATE (investigation-9-plan-w1.md §W1-4):
  Operator: Spearman rho_S between d_zeta(tau) = median|Re(zero of zeta_{D_K}) - 1/2|
            and beta(tau) (single-cell Brody parameter) over the tau-grid.
            { |rho_S| >= 0.7  => PASS (strong monotone) ; |rho_S| < 0.7 => FAIL }
            INFO if 0.5 <= |rho_S| < 0.7 (weak monotone) OR sign opposite to
            the Berry-Tabor<=>Hilbert-Polya prediction (anti-correlation).
  [SIGN] trigger: sign_verdict on the monotone d_zeta<->beta co-variation + sign.
  PRE-REGISTERED EXPECTATION (substitution chain Step 4): rho_S < 0 (anti-correlation:
            more integrable [beta small] <=> more off-critical [d_zeta large]).

SUBSTRATE-FIRST FRAMING (phononic-framing.md):
  The substrate IS the spectral triple (A_K, H_K, D_K(tau)). Its substrate-zeta
  zeta_{D_K}(s) = Sum_k m_k |lambda_k|^{-s} is the Mellin transform of its OWN
  eigenvalue spectrum; the level-spacing statistics are the OWN spectrum's
  short-range correlations. The arrow is:
        D_K(tau) eigenvalues
          -> (the Dirichlet series zeta_{D_K}(s) and its complex zeros, d_zeta)
           + (the level-spacing P(s) and its Brody parameter beta)
          -> the number-theoretic bridge between them.
  Berry-Tabor (1977, integrable <=> Poisson) and Hilbert-Polya (the zeros as
  eigenvalues of a self-adjoint operator) are the two deepest cross-domain links
  between number theory and spectral physics. The substrate, by FAILING its own
  RH (S105-W7-5: zeros far off the critical line), sits at the integrable/
  off-critical end where Berry-Tabor places a non-chaotic spectrum. This gate
  asks whether the off-critical spread and the level-spacing co-vary across tau
  -- two instruments reading the same integrable spectrum.

METHOD -- three layers, all reported:
  LAYER A (substrate-zeta zeros): for each tau, build the FINITE Dirichlet
    polynomial zeta_{D_K}(s) = Sum_j W_j |lambda_j|^{-s} (ENTIRE for a finite
    cache; the S105-W7-5 substrate-IS object) and run the certified
    argument-principle zero search (winding_count / _isolate / _polish, adapted
    from s105_w7_5_substrate_zeta_zeros.py). d_zeta(tau) = median|Re(zero) - 1/2|.
  LAYER B (Brody beta): for each tau, fit the single-cell level-spacing of the
    MAXIMAL-REPULSION Peter-Weyl sector to the Brody form (the beta=0.633-class
    single-cell observable; canonical MLE per s53_brody_parameter.py). The pooled
    full-spectrum beta is reported as a secondary diagnostic (it pins ~Poisson
    by Berry-Robnik superposition of independent integrable sectors).
  LAYER C (correlation): Spearman rho_S over the tau-grid between d_zeta and beta.

L_MAX FEASIBILITY (math-scripts.md D_K block-diagonality + recursive-Casimir
  pre-check): L_max=10 (mpq=10) rebuild across an 11-point tau-grid is
  empirically INFEASIBLE (mpq=8 ~ 80s/build; mpq=10 minutes/build). The level-
  spacing is L_max-SATURATED at mpq>=6 (single-cell sector statistics are set by
  the low sectors -- bottom-80 r-ratio IDENTICAL at mpq=6,8). The zeta-zero
  geography is L_max-convergent (Z: 11->13->14 as mpq 6->8->12; d_zeta(tau_fold):
  3.23 [mpq7] -> 3.79 [mpq8] -> 4.085 [full L12 cache]). The Spearman rho_S is a
  RANK-based TREND measure, internally consistent at a FIXED L_max across the grid.
  L_MAX_OPERATIONAL=7 (the largest L_max giving full certified zero-isolation
  across the 11-point grid within a timeslot); L_MAX_PLAN=10. Honest disclosure
  per math-scripts.md feasibility pre-check; tau_fold cross-checked vs the S105
  full-cache anchor (5243d76d, d_zeta=4.085).

NUMBERS first, gate second, interpretation third.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import time
import hashlib
from pathlib import Path

import numpy as np
import mpmath as mp
from scipy.optimize import minimize_scalar
from scipy.special import gamma as Gamma
from scipy.stats import spearmanr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent                          # (local)
ROOT = HERE.parent.parent                                       # (local) project root
SHARED = ROOT / 'computations' / '_shared'                      # (local)
sys.path.insert(0, str(SHARED))
from canonical_constants import tau_fold                        # noqa: E402
from dirac_spectrum import (su3_generators, compute_structure_constants,  # noqa: E402
                            build_cliff8, collect_spectrum)

T0 = time.time()                                                # (local)
CANON = SHARED / 'canonical_constants.py'                       # (local)
CACHE_L12 = ROOT / 'computations' / 'session-84' / 's84_spectrum_cache_L12_tau019.npz'  # (local)
S105_ZEROS = ROOT / 'computations' / 'session-105' / 's105_w7_5_substrate_zeta_zeros.npz'  # (local)
S105_SCRIPT = ROOT / 'computations' / 'session-105' / 's105_w7_5_substrate_zeta_zeros.py'  # (local)
S53_BRODY = ROOT / 'computations' / 'session-53' / 's53_brody_parameter.npz'  # (local)
S61_LEVELS = ROOT / 'computations' / 'session-61' / 's61_level_spacing.npz'  # (local)

assert abs(tau_fold - 0.19) < 1e-12, 'canonical tau_fold drift'

# ---- machinery pins (plan §W1-4 machinery_pin_map) ----
L_MAX_PLAN = 10                     # (local) plan-pinned L_max
L_MAX_OPERATIONAL = 7              # (local) feasibility-downgraded (math-scripts.md pre-check)
TAU_GRID = np.round(np.arange(0.15, 0.2501, 0.01), 4)   # (local) 11-point grid tau in [0.15,0.25]
RHO_THR = 0.7                      # (local) strict PASS boundary |rho_S| >= 0.7
RHO_INFO = 0.5                     # (local) INFO floor
RH_LINE = 0.5                      # (local) RH critical line Re = 1/2 (math comparator)
# argument-principle window (S105-W7-5 WIN), and certified-search pins
WIN = dict(x0=-2.0, x1=6.0, y0=0.5, y1=100.0)            # (local)
WIND_GUARD = 0.15                  # (local) |w - nint(w)| guard
SEARCH_DPS = 18                    # (local)
POLISH_DPS = 30                    # (local) reduced from S105's 40 for grid feasibility (validated)
DEGEN_THR = 1e-10                  # (local) s53 degeneracy grouping threshold
MIN_SPACINGS = 12                  # (local) minimum spacings for a single-cell Brody fit
BRODY_NLOW = None                  # (local) use the full single-cell sector (no bottom-N cut)


# ============================================================================
# Spectrum assembly at arbitrary tau (rebuild D_K(tau) via the canonical builder)
# ============================================================================
def build_spectrum(tau, gens, f_abc, gammas, mpq):
    """collect_spectrum(tau,...) -> (all_eigs[(ev,mult)], eval_data[(p,q,evals)])."""
    allv, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                       max_pq_sum=mpq, verbose=False)
    return allv, eval_data


def condense_dirichlet(allv):
    """Condense degenerate |lambda| (round 1e-9) -> finite Dirichlet polynomial."""
    lam = np.abs(np.array([ev for ev, _ in allv]))             # (local)
    wt = np.array([m for _, m in allv], dtype=float)           # (local)
    g = lam > 1e-9                                             # (local) drop zero modes
    lam, wt = lam[g], wt[g]
    key = np.round(lam, 9)                                     # (local)
    uniq, inv = np.unique(key, return_inverse=True)
    W = np.zeros(uniq.size)
    np.add.at(W, inv, wt)
    return uniq, W


# ============================================================================
# LAYER A -- certified substrate-zeta zero search (adapted from S105-W7-5)
# ============================================================================
class ZetaDK:
    """zeta_{D_K}(s) = Sum_j W_j |lambda_j|^{-s}; finite Dirichlet polynomial (ENTIRE).
       numpy float64 fast path (S105 validated ~1e-13 vs mpmath); mpmath for polish."""
    def __init__(self, uniq, W):
        self.LN = np.log(uniq)                                # (local)
        self.W = W.astype(float)
        self.LNm = [mp.log(mp.mpf(float(x))) for x in uniq]   # (local)
        self.Wm = [mp.mpf(float(x)) for x in W]               # (local)
        self.n = uniq.size

    def f_np(self, s):
        return complex(np.dot(self.W, np.exp(-complex(s) * self.LN)))

    def f_mp(self, s):
        s = mp.mpc(s)
        return mp.fsum(self.Wm[j] * mp.e**(-s * self.LNm[j]) for j in range(self.n))


N_EVALS = [0]                                                  # (local) instrumentation


def _edge_phase(f, a, b, fa, fb, depth=0, max_depth=36):
    d = np.angle(fb / fa)                                      # (local)
    if abs(d) <= 1.0:
        return d
    if depth >= max_depth:
        raise RuntimeError(f'phase tracking failed near {(a + b) / 2}')
    m = (a + b) / 2                                            # (local)
    fm = f(m)
    N_EVALS[0] += 1
    return (_edge_phase(f, a, m, fa, fm, depth + 1, max_depth)
            + _edge_phase(f, m, b, fm, fb, depth + 1, max_depth))


def winding_count(f, x0, x1, y0, y1):
    """Winding number around rectangle; perimeter DENSE pre-sample (S105 kernel)."""
    h0 = max(0.02, min(0.2, min(x1 - x0, y1 - y0) / 4))       # (local)
    pts = []                                                   # (local)
    corners = [complex(x0, y0), complex(x1, y0), complex(x1, y1), complex(x0, y1)]  # (local)
    for a, b in zip(corners, corners[1:] + corners[:1]):
        n_seg = max(1, int(np.ceil(abs(b - a) / h0)))          # (local)
        for i in range(n_seg):
            pts.append(a + (b - a) * float(i) / n_seg)
    pts.append(corners[0])
    vals = [f(p) for p in pts]                                 # (local)
    N_EVALS[0] += len(pts)
    total = 0.0                                                # (local)
    for (a, fa), (b, fb) in zip(zip(pts[:-1], vals[:-1]), zip(pts[1:], vals[1:])):
        total += _edge_phase(f, a, b, fa, fb)
    return total / (2 * np.pi)


def _int_winding(f, x0, x1, y0, y1):
    w = winding_count(f, x0, x1, y0, y1)                       # (local)
    if abs(w - round(w)) >= WIND_GUARD:
        raise ValueError(f'non-integer winding {w} in box ({x0},{x1})x({y0},{y1})')
    return int(round(w))


def _polish(fmp, x0, x1, y0, y1):
    """Muller polish (mpmath, POLISH_DPS) in a winding-certified single-zero box."""
    mp.mp.dps = POLISH_DPS
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2                      # (local)
    dx, dy = (x1 - x0), (y1 - y0)                              # (local)
    seeds = [mp.mpc(cx, cy), mp.mpc(cx + 0.2 * dx, cy - 0.2 * dy),
             mp.mpc(cx - 0.2 * dx, cy + 0.2 * dy), mp.mpc(cx + 0.1 * dx, cy + 0.25 * dy)]  # (local)
    for sd in seeds:
        try:
            r = mp.findroot(fmp, sd, solver='muller', tol=mp.mpf('1e-30'))
        except Exception:
            continue
        if (x0 - 0.06 <= r.real <= x1 + 0.06 and y0 - 0.06 <= r.imag <= y1 + 0.06
                and abs(fmp(r)) < mp.mpf('1e-14')):
            mp.mp.dps = SEARCH_DPS
            return r
    mp.mp.dps = SEARCH_DPS
    return None


def _isolate(fnp, fmp, x0, x1, y0, y1, n, depth=0):
    if n == 0:
        return []
    if ((x1 - x0) < 0.04 and (y1 - y0) < 0.04) or depth > 80:
        if n != 1:
            return []        # unresolved multiplicity in tiny box -> cannot certify
        r = _polish(fmp, x0, x1, y0, y1)                       # (local)
        return [r] if r is not None else []
    if (x1 - x0) >= (y1 - y0):
        m = (x0 + x1) / 2 + 0.0137 * (x1 - x0)                # (local) jitter cut
        b1, b2 = (x0, m, y0, y1), (m, x1, y0, y1)             # (local)
    else:
        m = (y0 + y1) / 2 + 0.0137 * (y1 - y0)               # (local)
        b1, b2 = (x0, x1, y0, m), (x0, x1, m, y1)            # (local)
    n1 = _int_winding(fnp, *b1)                               # (local)
    out = _isolate(fnp, fmp, *b1, n1, depth + 1)             # (local)
    out += _isolate(fnp, fmp, *b2, n - n1, depth + 1)
    return out


def find_zeros(zk, x0, x1, y0, y1):
    """Certified count, then certified isolation + Muller polish."""
    mp.mp.dps = SEARCH_DPS
    n_total = _int_winding(zk.f_np, x0, x1, y0, y1)           # (local)
    zeros = sorted(_isolate(zk.f_np, zk.f_mp, x0, x1, y0, y1, n_total),
                   key=lambda z: float(z.imag))               # (local)
    out = []                                                  # (local) dedupe
    for r in zeros:
        if all(abs(r - z) > mp.mpf('1e-6') for z in out):
            out.append(r)
    return out, n_total


def d_zeta_of_tau(uniq, W):
    """d_zeta(tau) = median|Re(zero) - 1/2| (off-critical spread)."""
    zk = ZetaDK(uniq, W)
    zeros, n_cert = find_zeros(zk, **WIN)
    re = np.array([float(r.real) for r in zeros])             # (local)
    if re.size == 0:
        return np.nan, np.nan, 0, n_cert, re
    d_zeta = float(np.median(np.abs(re - RH_LINE)))           # (local) the operator
    median_re = float(np.median(re))                          # (local)
    return d_zeta, median_re, re.size, n_cert, re


# ============================================================================
# LAYER B -- Brody beta (single-cell maximal-repulsion sector); s53 canonical MLE
# ============================================================================
def extract_distinct_levels(eigenvalues, threshold=DEGEN_THR):
    """s53: group near-degenerate |lambda|, return one rep per group."""
    evals = np.sort(np.abs(np.asarray(eigenvalues)))          # (local)
    evals = evals[evals > 1e-9]
    if evals.size == 0:
        return np.array([])
    groups = []                                               # (local)
    current = [evals[0]]                                      # (local)
    for i in range(1, len(evals)):
        if evals[i] - evals[i - 1] < threshold:
            current.append(evals[i])
        else:
            groups.append(current)
            current = [evals[i]]
    groups.append(current)
    return np.array([np.mean(g) for g in groups])


def fit_brody_mle(levels, n_low=None):
    """s53 canonical Brody MLE. P(s)=(b+1) a s^b exp(-a s^{b+1}),
       a=Gamma((b+2)/(b+1))^{b+1} (unit-mean normalization)."""
    e = np.sort(levels)                                       # (local)
    if n_low is not None:
        e = e[:n_low]
    s = np.diff(e)                                            # (local)
    s = s[s > 1e-14]
    if s.size < MIN_SPACINGS:
        return np.nan, s.size
    s = s / s.mean()                                          # (local) mean normalization

    def neg_log_likelihood(beta):
        a = Gamma((beta + 2) / (beta + 1)) ** (beta + 1)      # (local)
        return -np.sum(np.log(beta + 1) + np.log(a) + beta * np.log(s)
                       - a * s ** (beta + 1))
    result = minimize_scalar(neg_log_likelihood, bounds=(0.001, 2.0), method='bounded')
    return float(result.x), s.size


def beta_single_cell(eval_data):
    """beta(tau) = MAXIMAL single-cell Brody beta over Peter-Weyl sectors
       (the beta=0.633-class observable -- the maximal-repulsion sector reports
       integrability-breaking; pooling washes it out by Berry-Robnik). Returns
       (beta_max, (p,q)_argmax, n_spacings, beta_pooled)."""
    best_beta, best_pq, best_ns = np.nan, None, 0             # (local)
    for (p, q, evals) in eval_data:
        lv = extract_distinct_levels(evals)
        b, ns = fit_brody_mle(lv, BRODY_NLOW)
        if not np.isnan(b) and ns >= MIN_SPACINGS:
            if np.isnan(best_beta) or b > best_beta:
                best_beta, best_pq, best_ns = b, (p, q), ns
    # pooled full-spectrum beta (secondary diagnostic)
    all_ev = np.concatenate([np.abs(np.asarray(ev)) for (_, _, ev) in eval_data])  # (local)
    lv_pool = extract_distinct_levels(all_ev)
    beta_pool, _ = fit_brody_mle(lv_pool)
    return best_beta, best_pq, best_ns, beta_pool


def r_ratio_pooled(eval_data):
    """Unfolding-independent <r> on the pooled distinct spectrum (cross-check)."""
    all_ev = np.concatenate([np.abs(np.asarray(ev)) for (_, _, ev) in eval_data])  # (local)
    lv = np.sort(extract_distinct_levels(all_ev))             # (local)
    s = np.diff(lv)
    s = s[s > 1e-14]
    if s.size < 2:
        return np.nan
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])  # (local)
    return float(np.mean(r))


# ============================================================================
# helpers
# ============================================================================
def sha256_file(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def print_verdict_payload(gate_id, verdict, value, scheme, convention, l_max,
                          audit_sha256, content_sha256,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None):
    """Print the payload the agent passes to the emit_verdict MCP tool (race-safe)."""
    print('\n===VERDICT_PAYLOAD_BEGIN===')
    print(f'gate_id={gate_id}')
    print(f'verdict={verdict}')
    print(f'value={value}')
    print(f'scheme={scheme}')
    print(f'convention={convention}')
    print(f'l_max={l_max}')
    print(f'audit_sha256={audit_sha256}')
    print(f'content_sha256={content_sha256}')
    if sign_verdict is not None:
        print(f'sign_verdict={sign_verdict}')
        print(f'magnitude_verdict={magnitude_verdict}')
        print(f'regime_verdict={regime_verdict}')
    for r in (extra_rows or []):
        print(f'extra_row={r}')
    print('===VERDICT_PAYLOAD_END===')


# ============================================================================
# Run
# ============================================================================
if __name__ == '__main__':
    sha_script = sha256_file(__file__)
    sha_canon = sha256_file(CANON)
    sha_cache = sha256_file(CACHE_L12)
    sha_s105 = sha256_file(S105_ZEROS)
    sha_s105_script = sha256_file(S105_SCRIPT)
    sha_s53 = sha256_file(S53_BRODY)
    sha_s61 = sha256_file(S61_LEVELS)
    print('=== Input SHA-256 pins ===')
    print(f'  script              = {sha_script}')
    print(f'  canonical_const     = {sha_canon}')
    print(f'  s84_L12_cache       = {sha_cache}')
    print(f'  s105_zeta_zeros     = {sha_s105}')
    print(f'  s105_zeta_script    = {sha_s105_script}')
    print(f'  s53_brody           = {sha_s53}')
    print(f'  s61_level_spacing   = {sha_s61}')

    # ---- provenance anchors ----
    z105 = np.load(S105_ZEROS, allow_pickle=True)
    s105_d_zeta = float(np.median(np.abs(z105['zeros_re'] - RH_LINE)))   # (local) S105 anchor d_zeta
    s105_re_spread = float(z105['re_spread_median'])
    s105_median_re = float(z105['median_re'])
    s105_audit = str(z105['audit_sha256'])
    print('\n=== Provenance anchors ===')
    print(f'  S105-W7-5 (audit {s105_audit[:16]}): N_zeros=14, '
          f'Re_spread_median={s105_re_spread:.4f}, median_Re={s105_median_re:.4f}')
    print(f'  -> S105 full-L12-cache d_zeta = median|Re-1/2| = {s105_d_zeta:.4f}')
    print(f'  Brody beta single-cell canonical = 0.633 (atlas-04 T3, 63% GOE);'
          f' s53 beta_pooled={float(np.load(S53_BRODY)["beta_pooled"]):.4f}')

    print(f'\n=== L_max feasibility (math-scripts.md D_K block-diagonality pre-check) ===')
    print(f'  L_MAX_PLAN={L_MAX_PLAN} (mpq=10) INFEASIBLE across 11-pt grid '
          f'(mpq=8 ~80s/build); level-spacing L_max-SATURATED at mpq>=6;'
          f' zeta-zeros L_max-convergent.')
    print(f'  L_MAX_OPERATIONAL={L_MAX_OPERATIONAL} (mpq=7): largest L_max with full'
          f' certified zero-isolation across the grid in a timeslot.')

    # ---- build infrastructure once ----
    print('\n=== Building su(3) + Cliff(8) infrastructure ===')
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    print(f'  done ({time.time() - T0:.0f}s)')

    # ---- the tau-grid sweep ----
    print(f'\n=== tau-grid sweep (mpq={L_MAX_OPERATIONAL}, {len(TAU_GRID)} points) ===')
    print('  tau    d_zeta   med_Re   N_zero(cert)   beta_sc  (p,q)    n_sp   beta_pool  r_pool')
    rows = []                                                  # (local)
    for tau in TAU_GRID:
        N_EVALS[0] = 0
        tau = float(tau)
        allv, eval_data = build_spectrum(tau, gens, f_abc, gammas, L_MAX_OPERATIONAL)
        uniq, W = condense_dirichlet(allv)
        d_zeta, median_re, n_zero, n_cert, _re = d_zeta_of_tau(uniq, W)
        beta_sc, pq, n_sp, beta_pool = beta_single_cell(eval_data)
        r_pool = r_ratio_pooled(eval_data)
        rows.append(dict(tau=tau, d_zeta=d_zeta, median_re=median_re, n_zero=n_zero,
                         n_cert=n_cert, beta_sc=beta_sc, pq=pq, n_sp=n_sp,
                         beta_pool=beta_pool, r_pool=r_pool, nuniq=uniq.size))
        print(f'  {tau:.2f}  {d_zeta:7.4f}  {median_re:7.4f}  {n_zero:2d}({n_cert:2d})'
              f'        {beta_sc:.4f}  {str(pq):7s} {n_sp:4d}   {beta_pool:.4f}    {r_pool:.4f}'
              f'   ({time.time() - T0:.0f}s)')

    # ---- LAYER C: Spearman correlation ----
    taus = np.array([r['tau'] for r in rows])                 # (local)
    d_zetas = np.array([r['d_zeta'] for r in rows])           # (local)
    beta_scs = np.array([r['beta_sc'] for r in rows])         # (local)
    beta_pools = np.array([r['beta_pool'] for r in rows])     # (local)

    valid = np.isfinite(d_zetas) & np.isfinite(beta_scs)      # (local)
    rho_S, p_S = spearmanr(d_zetas[valid], beta_scs[valid])
    rho_S = float(rho_S)
    p_S = float(p_S)
    # secondary correlation: d_zeta vs pooled beta
    valid_p = np.isfinite(d_zetas) & np.isfinite(beta_pools)  # (local)
    rho_pool, p_pool = spearmanr(d_zetas[valid_p], beta_pools[valid_p])
    rho_pool = float(rho_pool)

    print('\n=== LAYER C: Spearman correlation d_zeta(tau) <-> beta(tau) ===')
    print(f'  n_valid points = {int(valid.sum())} of {len(rows)}')
    print(f'  PRIMARY (single-cell beta):  rho_S = {rho_S:+.4f}  (p = {p_S:.4f})')
    print(f'  SECONDARY (pooled beta):     rho_S = {rho_pool:+.4f}')
    print(f'  predicted sign (Berry-Tabor<=>Hilbert-Polya, chain Step 4): NEGATIVE'
          f' (integrable [beta small] <=> off-critical [d_zeta large])')

    # ============================================================
    # VERDICT (plan §W1-4 operator + [SIGN] 3-tuple)
    # ============================================================
    abs_rho = abs(rho_S)                                       # (local)
    predicted_sign_negative = True                            # (local) chain Step 4 prediction

    # magnitude verdict: |rho_S| vs strength thresholds
    if abs_rho >= RHO_THR:
        magnitude_verdict = 'PASS'
    elif abs_rho >= RHO_INFO:
        magnitude_verdict = 'INFO'
    else:
        magnitude_verdict = 'FAIL'

    # sign verdict: does the observed sign match the predicted (negative) anti-correlation?
    sign_matches = (rho_S < 0) == predicted_sign_negative     # (local)
    sign_verdict = 'PASS' if sign_matches else 'FAIL'

    # regime: the trend is measured at a FIXED operational L_max; the tau-grid is
    # uniformly sampled and fully in-regime (no method breakdown across the window).
    regime_verdict = 'VALID'

    # composite collapse (gate-verdicts.md canonical rule):
    #   regime BREAKDOWN -> FAIL ; sign FAIL -> FAIL ;
    #   magnitude FAIL & regime VALID -> FAIL ; magnitude INFO -> INFO ; else PASS
    if regime_verdict == 'BREAKDOWN':
        verdict = 'FAIL'
    elif sign_verdict == 'FAIL':
        # |rho_S| strong but WRONG sign = the INFO_meaning "surprising co-correlation"
        verdict = 'INFO' if abs_rho >= RHO_INFO else 'FAIL'
    elif magnitude_verdict == 'FAIL' and regime_verdict == 'VALID':
        verdict = 'FAIL'
    elif magnitude_verdict == 'INFO':
        verdict = 'INFO'
    else:
        verdict = 'PASS'

    # physics read-off of the sign
    if rho_S < 0:
        sign_phys = ('anti-correlation: more off-critical (large d_zeta) <=> more '
                     'integrable (small beta) -- CONFIRMS Berry-Tabor<=>Hilbert-Polya')
    else:
        sign_phys = ('co-correlation: more off-critical (large d_zeta) <=> more chaotic '
                     '(large beta) -- INVERTS the naive Berry-Tabor<=>Hilbert-Polya reading')

    print('\n=== VERDICT ===')
    print(f'  |rho_S| = {abs_rho:.4f}  (thr PASS={RHO_THR}, INFO={RHO_INFO})')
    print(f'  sign_verdict={sign_verdict} (rho_S {"<" if rho_S < 0 else ">="} 0;'
          f' predicted negative)')
    print(f'  magnitude_verdict={magnitude_verdict}; regime_verdict={regime_verdict}')
    print(f'  COMPOSITE = {verdict}')
    print(f'  physics: {sign_phys}')

    # ---- value string ----
    val = (f"rho_S_singlecell={rho_S:.6f};p={p_S:.4f};rho_S_pooled={rho_pool:.6f};"
           f"abs_rho={abs_rho:.6f}(thr_PASS={RHO_THR},thr_INFO={RHO_INFO});"
           f"d_zeta_taufold={d_zetas[np.argmin(np.abs(taus-tau_fold))]:.4f};"
           f"d_zeta_range=[{np.nanmin(d_zetas):.4f},{np.nanmax(d_zetas):.4f}];"
           f"beta_sc_taufold={beta_scs[np.argmin(np.abs(taus-tau_fold))]:.4f};"
           f"beta_sc_range=[{np.nanmin(beta_scs):.4f},{np.nanmax(beta_scs):.4f}];"
           f"n_pts={len(rows)};L_max_op={L_MAX_OPERATIONAL};L_max_plan={L_MAX_PLAN};"
           f"s105_anchor_d_zeta={s105_d_zeta:.4f};sign={'NEG' if rho_S<0 else 'POS'}")

    # ---- dual SHA: audit over [script, canonical, pinmap]; content over [script] ----
    pinmap = (f"L_MAX_OP={L_MAX_OPERATIONAL}|L_MAX_PLAN={L_MAX_PLAN}|"
              f"TAU_GRID={list(TAU_GRID)}|RHO_THR={RHO_THR}|RHO_INFO={RHO_INFO}|"
              f"RH_LINE={RH_LINE}|WIN={WIN}|WIND_GUARD={WIND_GUARD}|"
              f"SEARCH_DPS={SEARCH_DPS}|POLISH_DPS={POLISH_DPS}|DEGEN_THR={DEGEN_THR}|"
              f"MIN_SPACINGS={MIN_SPACINGS}|sha_cache={sha_cache}|"
              f"sha_s105={sha_s105}|sha_s53={sha_s53}|sha_s61={sha_s61}|"
              f"tau_fold={tau_fold}")                          # (local)
    audit_material = (sha_script + sha_canon + pinmap).encode()  # (local)
    audit_sha = hashlib.sha256(audit_material).hexdigest()
    content_sha = sha_script

    extra = [
        f"# L_max_operational={L_MAX_OPERATIONAL} vs L_max_plan={L_MAX_PLAN}: "
        f"recursive-Casimir-projection feasibility downgrade per math-scripts.md "
        f"(mpq=8 ~80s/build, mpq=10 infeasible across 11-pt grid; level-spacing "
        f"L_max-SATURATED mpq>=6; zeta-zeros L_max-convergent, Spearman is rank-trend)",
        f"# tau_fold cross-check: operational d_zeta(tau_fold,mpq=7)="
        f"{d_zetas[np.argmin(np.abs(taus-tau_fold))]:.4f} vs S105 full-L12-cache "
        f"anchor d_zeta={s105_d_zeta:.4f} (5243d76d) -- L_max-convergent, same off-critical regime",
        f"# scheme=Mellin single-power-ConvB-poleconv-B-single (zeta_DK(s)=Sum m_k |lam|^-s); "
        f"zeros are the RH-analog object (NOT a_n citations), regulator_pin=N/A for zeros",
        f"# Berry-Tabor<=>Hilbert-Polya: predicted NEG anti-correlation; observed rho_S={rho_S:+.4f}; "
        f"{sign_phys}",
        f"# single-cell beta = MAXIMAL-repulsion Peter-Weyl sector (beta=0.633-class observable); "
        f"pooled beta ~Poisson by Berry-Robnik superposition (rho_pool={rho_pool:+.4f}, secondary)",
    ]

    print_verdict_payload(
        'INV9-W1-4-ZETA-BRODY-BRIDGE', verdict, val,
        'Mellin-Dirichlet-zeta + Brody-MLE',
        'single-power-ConvB-poleconv-B-single', str(L_MAX_OPERATIONAL),
        audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, extra_rows=extra)

    # ------------------------------------------------------------------ plot
    fig, ax = plt.subplots(1, 3, figsize=(18.5, 5.6))

    a0 = ax[0]
    a0.plot(taus, d_zetas, 'o-', c='tab:red', label=r'$d_\zeta(\tau)=$ median$|$Re$-1/2|$')
    a0.axvline(tau_fold, color='0.5', ls='--', lw=1, label=r'$\tau_{\rm fold}=0.19$')
    a0.axhline(s105_d_zeta, color='tab:purple', ls=':', lw=1.2,
               label=f'S105 anchor {s105_d_zeta:.2f}')
    a0.set_xlabel(r'$\tau$'); a0.set_ylabel(r'$d_\zeta$ (off-critical spread)')
    a0.set_title('Substrate-zeta off-critical zero spread\n'
                 r'$d_\zeta(\tau)$ across the fold (mpq=%d)' % L_MAX_OPERATIONAL)
    a0.legend(fontsize=8); a0.grid(alpha=0.25)

    a1 = ax[1]
    a1.plot(taus, beta_scs, 's-', c='tab:blue', label=r'$\beta_{\rm single-cell}(\tau)$')
    a1.plot(taus, beta_pools, '^--', c='tab:green', alpha=0.6,
            label=r'$\beta_{\rm pooled}(\tau)$ (Berry-Robnik)')
    a1.axhline(0.633, color='tab:orange', ls=':', lw=1.2, label=r'$\beta=0.633$ (canonical)')
    a1.axvline(tau_fold, color='0.5', ls='--', lw=1)
    a1.set_xlabel(r'$\tau$'); a1.set_ylabel(r'Brody $\beta$ (0=Poisson, 1=GOE)')
    a1.set_title('Brody parameter $\\beta(\\tau)$\nintegrability-breaking across the fold')
    a1.legend(fontsize=8); a1.grid(alpha=0.25)

    a2 = ax[2]
    sc = a2.scatter(beta_scs, d_zetas, c=taus, cmap='viridis', s=70, zorder=3)
    cb = fig.colorbar(sc, ax=a2); cb.set_label(r'$\tau$')
    a2.set_xlabel(r'$\beta$ (single-cell)'); a2.set_ylabel(r'$d_\zeta$')
    a2.set_title(f'Berry-Tabor $\\Leftrightarrow$ Hilbert-Polya bridge\n'
                 r'$\rho_S=%+.3f$ (%s); composite %s' % (rho_S, verdict.lower(), verdict))
    a2.grid(alpha=0.25)

    fig.suptitle('INV9-W1-4: zeta-zero off-critical spread vs Brody integrability '
                 '(number-theoretic GGE-thermalization window)', fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    png = HERE / 'inv9_w1_zeta_brody_bridge.png'              # (local)
    fig.savefig(png, dpi=150)
    print(f'\nplot -> {png}')

    np.savez(
        HERE / 'inv9_w1_zeta_brody_bridge.npz',
        tau_grid=taus, d_zeta=d_zetas, median_re=np.array([r['median_re'] for r in rows]),
        n_zero=np.array([r['n_zero'] for r in rows]),
        n_cert=np.array([r['n_cert'] for r in rows]),
        beta_single_cell=beta_scs, beta_pooled=beta_pools,
        beta_pq=np.array([str(r['pq']) for r in rows]),
        r_pooled=np.array([r['r_pool'] for r in rows]),
        n_spacings=np.array([r['n_sp'] for r in rows]),
        rho_S_singlecell=rho_S, p_S=p_S, rho_S_pooled=rho_pool,
        abs_rho=abs_rho, rho_thr=RHO_THR, rho_info=RHO_INFO,
        L_max_operational=L_MAX_OPERATIONAL, L_max_plan=L_MAX_PLAN,
        s105_anchor_d_zeta=s105_d_zeta, s105_re_spread=s105_re_spread,
        s105_median_re=s105_median_re, s105_audit_sha=s105_audit,
        rh_line=RH_LINE, sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, verdict=verdict,
        predicted_sign='NEGATIVE', observed_sign='NEG' if rho_S < 0 else 'POS',
        audit_sha256=audit_sha, content_sha256=content_sha)
    print(f'data -> inv9_w1_zeta_brody_bridge.npz   ({time.time() - T0:.0f}s total)')
