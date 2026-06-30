"""
OFF-SESSION EXPLORATORY HELPER — "Does the substrate satisfy its own Riemann Hypothesis?"
=========================================================================================
NOT a session gate. No verdict-line emission, no registry writes, no pre-registered
threshold. Sanity computation requested by user (RH / universe-as-calculator thread).
Underscore-prefixed per helper convention; lives outside s{N} gate namespace.

QUESTION
  Substrate-class spectral zetas (Casimir lattice sums with Weyl-dimension
  multiplicities) vs arithmetic zetas (Euler product): do the substrate-class
  zeros lie on a critical line?

EXACT TEST OBJECT — Dirac zeta of S^3 = SU(2) (the substrate's exactly solvable
little brother; same structural genre as zeta_{D_K} on SU(3)):
  Spin Dirac on round S^3:  |lambda_k| = k + 3/2,  mult m_k = (k+1)(k+2),  k >= 0
  (one chirality branch; full spectrum is +/- symmetric, factor 2 irrelevant to zeros)

  Convention declaration (regulator-pin discipline): single-power Conv. B,
  zeta_{|D|}(s) = sum m_k |lambda_k|^{-s}; poles at s = d - n, d = 3, n in {0,2}
  => pole set {3, 1}. poleconv-B-single.

  Substitution chain (math-scripts double-check discipline):
    Step 1:  m_k = (k+1)(k+2) = (k+3/2)^2 - 1/4                  [algebra]
    Step 2:  zeta_D(s) = sum_{k>=0} [(k+3/2)^{2-s} - (1/4)(k+3/2)^{-s}]
                       = zeta_H(s-2, 3/2) - (1/4) zeta_H(s, 3/2)  [Hurwitz def]
    Step 3:  zeta_H(s, 3/2) = zeta_H(s, 1/2) - 2^s = (2^s - 1) zeta(s) - 2^s
    Step 4:  substitute and simplify (the -2^{s-2} terms cancel exactly):
             F(s) = (2^{s-2} - 1) zeta(s-2) - (2^{s-2} - 1/4) zeta(s)
    Verified numerically against direct truncated sums below.

  Structural expectations (checked, not assumed):
    F(0) = 0 exactly (coefficient zero at s=0)  <-> zeta_{|D|}(0) = 0, odd-dim parity
    F(-2m) = 0 exactly (both zetas at trivial zeros) -> geometric "trivial family"
    Poles only at s = 3 (res 1) and s = 1 (res -1/4)  <-> heat coefficients a_0, a_2

CONTROLS (same zero-search machinery, same window):
  zeta(s)        — Euler product over primes. Expect all zeros on Re = 1/2.
  L(s, chi_-3)   — Euler product; and 6*zeta(s)*L(s,chi_-3) is EXACTLY the Epstein
                   zeta of the hexagonal lattice x^2+xy+y^2 — SU(3)'s root lattice.
                   Computed as L(s) = 3^{-s} (zeta_H(s,1/3) - zeta_H(s,2/3)).
                   Expect all zeros on Re = 1/2.

SUBSTRATE DATA LAYER (actual D_K, L=12 cache @ tau_fold):
  Weyl counting N(lambda) from computations/session-84/s84_spectrum_cache_L12_tau019.npz,
  with and without the Peter-Weyl regular-representation weight dim(p,q);
  contrast against Riemann zero counting N(T) = (T/2pi) log(T/2pi e) + 7/8.

Method: argument-principle winding counts on recursively subdivided boxes
(boundary phase tracking, adaptive refinement), Muller polish at high precision,
global winding total cross-checked against the number of polished roots.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')

import sys
import time
from pathlib import Path

import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SHARED = Path(__file__).resolve().parents[1] / '_shared'      # (local)
sys.path.insert(0, str(SHARED))
from canonical_constants import tau_fold  # noqa: E402  (cache tau pin; import-discipline witness)

T0 = time.time()                                  # (local)
OUT_DIR = os.path.dirname(os.path.abspath(__file__))  # (local)
CACHE = os.path.join(OUT_DIR, '..', 'session-84', 's84_spectrum_cache_L12_tau019.npz')  # (local)
assert abs(tau_fold - 0.19) < 1e-12, 'cache filename tau019 no longer matches canonical tau_fold'

# ----------------------------------------------------------------------------
# Test functions
# ----------------------------------------------------------------------------
def F_s3(s):
    """Exact S^3 Dirac zeta, one chirality branch (Conv. B single-power)."""
    s = mp.mpc(s)
    c = mp.power(2, s - 2)
    return (c - 1) * mp.zeta(s - 2) - (c - mp.mpf(1) / 4) * mp.zeta(s)

def L_chi3(s):
    """Dirichlet L(s, chi_-3) via Hurwitz zetas (chi_-3: 1, -1, 0 mod 3)."""
    s = mp.mpc(s)
    return mp.power(3, -s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))

def Z_riemann(s):
    return mp.zeta(s)

# Poles inside any search box, per function (for winding = Z - P accounting).
POLES = {'S3_dirac': [mp.mpf(3), mp.mpf(1)], 'riemann': [mp.mpf(1)], 'L_chi3': []}

# ----------------------------------------------------------------------------
# Verification of the closed form (substitution-chain numeric check)
# ----------------------------------------------------------------------------
def verify_reduction():
    mp.mp.dps = 30
    print('=== Closed-form verification (S^3 Dirac zeta) ===')
    # Step 2 check (direct sum = Hurwitz combo), real points with comfortable convergence
    for s_test in [mp.mpf(5), mp.mpf('6.3')]:
        direct = mp.nsum(lambda k: (k + 1) * (k + 2) * mp.power(k + mp.mpf(3) / 2, -s_test),
                         [0, mp.inf])
        closed = F_s3(s_test)
        err = abs(direct - closed)                # (local)
        print(f'  s = {mp.nstr(s_test, 8):>12s}:  |direct sum - closed| = {mp.nstr(err, 3)}')
        # nsum Euler-Maclaurin extrapolation delivers ~1e-14 on non-integer exponents;
        # the bit-tight formula check is the exact-vs-exact Hurwitz reduction below.
        assert err < mp.mpf('1e-10'), 'closed form mismatch (direct sum)'
    # Steps 3-4 check (Hurwitz combo = final formula), complex points, both sides exact
    for s_test in [mp.mpc('3.7', '2.0'), mp.mpc('0.3', '14.0'), mp.mpc('-1.2', '5.0')]:
        hurwitz = mp.zeta(s_test - 2, mp.mpf(3) / 2) - mp.zeta(s_test, mp.mpf(3) / 2) / 4  # (local)
        err = abs(hurwitz - F_s3(s_test))         # (local)
        print(f'  s = {mp.nstr(s_test, 8):>14s}:  |Hurwitz combo - closed| = {mp.nstr(err, 3)}')
        assert err < mp.mpf('1e-22'), 'closed form mismatch (Hurwitz reduction)'
    # structural zeros
    for s0, why in [(0, 'coefficient zero  <-> zeta_D(0)=0 odd-dim parity'),
                    (-2, 'double trivial zero'), (-4, 'double trivial zero'),
                    (-6, 'double trivial zero')]:
        v = abs(F_s3(s0))                         # (local)
        print(f'  F({s0:>2d}) = {mp.nstr(v, 3)}   [{why}]')
        assert v < mp.mpf('1e-25')
    # pole residues
    eps = mp.mpf('1e-12')                         # (local)
    r3 = F_s3(3 + eps) * eps                      # (local)
    r1 = F_s3(1 + eps) * eps                      # (local)
    print(f'  residue @ s=3: {mp.nstr(r3, 8)} (expect 1);  @ s=1: {mp.nstr(r1, 8)} (expect -0.25)')
    print(f'  pole set {{3, 1}} = {{d-0, d-2}} at d=3, Conv. B  ->  a_0, a_2 only (odd-n vanish)')

# ----------------------------------------------------------------------------
# Argument-principle zero search
# ----------------------------------------------------------------------------
N_EVALS = [0]                                     # (local) instrumentation

def _edge_phase(f, a, b, fa, fb, depth, max_depth=32):
    """Continuous phase change of f along segment a->b, adaptive bisection."""
    d = mp.arg(fb / fa)                           # (local)
    if abs(d) <= mp.mpf('1.0'):
        return d
    if depth >= max_depth:
        raise RuntimeError(f'phase tracking failed near {mp.nstr((a+b)/2, 6)} (zero on boundary?)')
    m = (a + b) / 2                               # (local)
    fm = f(m); N_EVALS[0] += 1                    # (local)
    return (_edge_phase(f, a, m, fa, fm, depth + 1, max_depth)
            + _edge_phase(f, m, b, fm, fb, depth + 1, max_depth))

def winding_count(f, x0, x1, y0, y1):
    """Winding number around the rectangle. Perimeter is PRE-SAMPLED densely
    (step <= h0) before adaptive refinement — corner-only sampling aliases away
    whole 2*pi wraps between corners, silently undercounting zeros."""
    h0 = max(0.02, min(0.2, min(x1 - x0, y1 - y0) / 4))   # (local)
    pts = []                                      # (local)
    corners = [mp.mpc(x0, y0), mp.mpc(x1, y0), mp.mpc(x1, y1), mp.mpc(x0, y1)]  # (local)
    for a, b in zip(corners, corners[1:] + corners[:1]):
        n_seg = max(1, int(mp.ceil(abs(b - a) / h0)))     # (local)
        for i in range(n_seg):
            pts.append(a + (b - a) * mp.mpf(i) / n_seg)
    pts.append(corners[0])
    vals = [f(p) for p in pts]                    # (local)
    N_EVALS[0] += len(pts)
    total = mp.mpf(0)                             # (local)
    for (a, fa), (b, fb) in zip(zip(pts[:-1], vals[:-1]), zip(pts[1:], vals[1:])):
        total += _edge_phase(f, a, b, fa, fb, 0)
    return total / (2 * mp.pi)

def _int_winding(f, x0, x1, y0, y1):
    w = winding_count(f, x0, x1, y0, y1)          # (local)
    assert abs(w - mp.nint(w)) < mp.mpf('0.15'), f'non-integer winding {w}'
    return int(mp.nint(w))

def _polish(f, x0, x1, y0, y1, polish_dps, search_dps):
    """Muller polish inside a winding-certified box containing exactly one zero."""
    mp.mp.dps = polish_dps
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2         # (local)
    dx, dy = (x1 - x0), (y1 - y0)                 # (local)
    seeds = [mp.mpc(cx, cy), mp.mpc(cx + 0.2 * dx, cy - 0.2 * dy),
             mp.mpc(cx - 0.2 * dx, cy + 0.2 * dy), mp.mpc(cx + 0.1 * dx, cy + 0.25 * dy)]  # (local)
    for sd in seeds:
        try:
            r = mp.findroot(f, sd, solver='muller', tol=mp.mpf('1e-40'))
        except Exception:
            continue
        if (x0 - 0.05 <= r.real <= x1 + 0.05 and y0 - 0.05 <= r.imag <= y1 + 0.05
                and abs(f(r)) < mp.mpf('1e-20')):
            mp.mp.dps = search_dps
            return r
    mp.mp.dps = search_dps
    return None

def _isolate(f, x0, x1, y0, y1, n, polish_dps, search_dps, depth=0):
    """Winding-certified bisection: split until each box holds one zero, polish."""
    if n == 0:
        return []
    if ((x1 - x0) < 0.05 and (y1 - y0) < 0.05) or depth > 70:
        assert n == 1, f'unresolved multiplicity {n} in tiny box at ({x0},{y0})'
        r = _polish(f, x0, x1, y0, y1, polish_dps, search_dps)  # (local)
        if r is not None:
            return [r]
        # winding certifies presence; shrink further until Muller cooperates
    # split the longer side; jitter the cut (relative) to dodge on-cut zeros
    if (x1 - x0) >= (y1 - y0):
        m = (x0 + x1) / 2 + 0.0137 * (x1 - x0)   # (local)
        b1, b2 = (x0, m, y0, y1), (m, x1, y0, y1)  # (local)
    else:
        m = (y0 + y1) / 2 + 0.0137 * (y1 - y0)   # (local)
        b1, b2 = (x0, x1, y0, m), (x0, x1, m, y1)  # (local)
    n1 = _int_winding(f, *b1)                     # (local)
    out = _isolate(f, *b1, n1, polish_dps, search_dps, depth + 1)       # (local)
    out += _isolate(f, *b2, n - n1, polish_dps, search_dps, depth + 1)
    return out

def find_zeros(f, name, x0, x1, y0, y1, polish_dps=35, search_dps=18):
    """Argument-principle zero search: certified count, then certified isolation."""
    mp.mp.dps = search_dps
    # window bottom sits above Im=0, so the real-axis poles are outside; assert it
    assert y0 > 0 and all(p.imag == 0 for p in [mp.mpc(q) for q in POLES[name]])
    n_total = _int_winding(f, x0, x1, y0, y1)     # (local)
    print(f'  [{name}] window [{x0},{x1}]x[{y0},{y1}]: certified zero count Z = {n_total}')
    zeros = sorted(_isolate(f, x0, x1, y0, y1, n_total, polish_dps, search_dps),
                   key=lambda z: float(z.imag))   # (local)
    # dedupe safety (overlapping polish slack)
    out = []                                      # (local)
    for r in zeros:
        if all(abs(r - z) > mp.mpf('1e-6') for z in out):
            out.append(r)
    assert len(out) == n_total, f'{name}: isolated {len(out)} != certified {n_total}'
    print(f'  [{name}] isolated + polished {len(out)}/{n_total} zeros '
          f'({time.time() - T0:.0f}s elapsed, {N_EVALS[0]} cumulative evals)')
    return out, n_total

def real_axis_zeros_F(lo=-9.7, hi=5.7):
    """1D sign-change scan of F on the real axis (F real there), poles excluded."""
    mp.mp.dps = 25
    pts = []                                      # (local)
    x = lo                                        # (local)
    excl = [(0.9, 1.1), (2.9, 3.1)]               # (local) poles
    prev_x, prev_v = None, None                   # (local)
    while x <= hi:
        if not any(a < x < b for a, b in excl):
            v = F_s3(mp.mpf(x))                   # (local)
            if prev_v is not None and mp.sign(v) != mp.sign(prev_v) \
               and not any(a < t < b for a, b in excl for t in (prev_x, x)):
                r = mp.findroot(lambda t: F_s3(t).real, (prev_x + x) / 2)  # (local)
                pts.append(float(r))
            prev_x, prev_v = x, v
        else:
            prev_v = None
        x += 0.02
    return pts

# ----------------------------------------------------------------------------
# Substrate cache: Weyl counting
# ----------------------------------------------------------------------------
def substrate_counting():
    z = np.load(CACHE, allow_pickle=True)
    se = z['sector_evals'].item()                 # (local)
    lam, wts = [], []                             # (local)
    n_zero_modes = 0                              # (local)
    for (p, q), d in se.items():
        ev = np.asarray(d['abs_evals'], dtype=float)  # (local)
        n_zero_modes += int((ev < 1e-12).sum())
        ev = ev[ev > 1e-12]
        lam.append(ev)
        wts.append(np.full(ev.shape, d['dim'], dtype=float))
    lam = np.concatenate(lam); wts = np.concatenate(wts)
    order = np.argsort(lam)                       # (local)
    lam = lam[order]; wts = wts[order]
    N_blk = np.arange(1, lam.size + 1, dtype=float)   # (local) block-reduced count
    N_pw = np.cumsum(wts)                         # (local) Peter-Weyl weighted (full L^2)
    # interior fit windows (quantile-based; avoid IR floor + L_max truncation bend)
    def fit_slope(N):
        i0, i1 = int(0.20 * lam.size), int(0.70 * lam.size)  # (local)
        sl, ic = np.polyfit(np.log(lam[i0:i1]), np.log(N[i0:i1]), 1)  # (local)
        return sl
    s_blk, s_pw = fit_slope(N_blk), fit_slope(N_pw)   # (local)
    print(f'\n=== Substrate Weyl counting (L=12 cache @ tau_fold={tau_fold}) ===')
    print(f'  eigenvalues loaded: {lam.size} block-level entries; zero modes excluded: {n_zero_modes}')
    print(f'  fitted counting exponent, block-reduced:      N ~ lambda^{s_blk:.3f}')
    print(f'  fitted counting exponent, Peter-Weyl weighted: N ~ lambda^{s_pw:.3f}')
    print(f'  Riemann zeros count as N(T) = (T/2pi) log(T/2pi e) + 7/8  (slope -> 1, log-corrected)')
    return lam, N_blk, N_pw, s_blk, s_pw

# ----------------------------------------------------------------------------
# Run
# ----------------------------------------------------------------------------
if __name__ == '__main__':
    verify_reduction()

    WIN = dict(x0=-3.47, x1=4.53, y0=0.41, y1=36.13)   # (local) jittered edges
    print('\n=== Complex-zero search, window Re in [-3.47, 4.53], Im in [0.41, 36.13] ===')
    zF, nF = find_zeros(F_s3, 'S3_dirac', **WIN)
    zZ, nZ = find_zeros(Z_riemann, 'riemann', **WIN)
    zL, nL = find_zeros(L_chi3, 'L_chi3', **WIN)

    rF = real_axis_zeros_F()

    mp.mp.dps = 30
    print('\n=== RESULTS ===')
    print(f'\nS^3 Dirac zeta (substrate-class, no Euler product): {len(zF)} complex zeros')
    for r in zF:
        print(f'    s = {float(r.real):+.12f} + {float(r.imag):.12f} i')
    reF = [float(r.real) for r in zF]             # (local)
    if reF:
        print(f'  Re spread: [{min(reF):.6f}, {max(reF):.6f}]  width = {max(reF)-min(reF):.6f}')
        med = float(np.median(reF))               # (local)
        print(f'  max |Re - median Re| = {max(abs(x - med) for x in reF):.6f}')
        print(f'  ON A COMMON VERTICAL LINE?  {"YES" if max(reF)-min(reF) < 1e-6 else "NO"}')
    print(f'  real-axis zeros found: {[round(x, 6) for x in rF]} (geometric/trivial family)')

    for nm, zs in [('Riemann zeta (Euler product)', zZ), ('L(s, chi_-3) (Euler product)', zL)]:
        dev = max((abs(float(r.real) - 0.5) for r in zs), default=0.0)  # (local)
        print(f'\n{nm}: {len(zs)} zeros, max |Re - 1/2| = {dev:.2e}')
        for r in zs:
            print(f'    s = {float(r.real):+.12f} + {float(r.imag):.12f} i')
    print('\n  hexagonal-lattice Epstein zeta = 6 * zeta(s) * L(s,chi_-3): zeros = union of'
          '\n  the two lists above -> ALL on Re = 1/2. SU(3) root lattice, full-lattice sum,'
          '\n  Euler product intact. The chamber restriction + Weyl weights are what break it.')

    lam, N_blk, N_pw, s_blk, s_pw = substrate_counting()

    # ------------------------------------------------------------------ plot
    fig, ax = plt.subplots(1, 2, figsize=(13.5, 5.6))
    a0 = ax[0]
    a0.axvline(0.5, color='0.55', lw=1.2, ls='--', label='Re s = 1/2 (critical line)')
    a0.scatter([float(r.real) for r in zZ], [float(r.imag) for r in zZ],
               s=42, c='tab:blue', marker='o', label=r'$\zeta(s)$ (Euler product)')
    a0.scatter([float(r.real) for r in zL], [float(r.imag) for r in zL],
               s=42, c='tab:green', marker='s', label=r'$L(s,\chi_{-3})$ (Euler product)')
    a0.scatter(reF, [float(r.imag) for r in zF],
               s=70, c='tab:red', marker='x', label=r'$\zeta_{D,S^3}(s)$ (substrate-class)')
    a0.scatter(rF, [0] * len(rF), s=46, facecolors='none', edgecolors='tab:red',
               marker='o', label='substrate-class real zeros (geometric)')
    a0.scatter([1, 3], [0, 0], s=60, c='k', marker='+', label='poles (dim spectrum)')
    a0.set_xlabel('Re s'); a0.set_ylabel('Im s')
    a0.set_title('The pin: Euler product holds zeros to the line;\n'
                 'Peter-Weyl multiplicities scatter them')
    a0.legend(loc='upper left', fontsize=8); a0.grid(alpha=0.25)

    a1 = ax[1]
    a1.loglog(lam, N_pw, c='tab:red', lw=1.6,
              label=fr'substrate $N(\lambda)$, PW-weighted (slope $\approx$ {s_pw:.2f})')
    a1.loglog(lam, N_blk, c='tab:orange', lw=1.4, ls='--',
              label=fr'substrate $N(\lambda)$, block-reduced (slope $\approx$ {s_blk:.2f})')
    Tg = np.logspace(1, 6, 200)                   # (local)
    a1.loglog(Tg, (Tg / (2 * np.pi)) * np.log(Tg / (2 * np.pi * np.e)) + 7 / 8,
              c='tab:blue', lw=1.6, label=r'Riemann zeros $N(T)$ (slope $\to$ 1, log)')
    a1.set_xlabel(r'$\lambda$  (resp. $T$)'); a1.set_ylabel('counting function')
    a1.set_title('Wall 3 from real substrate data:\npolynomial Weyl growth vs $T\\log T$ zero counting')
    a1.legend(fontsize=8); a1.grid(alpha=0.25, which='both')
    fig.suptitle('Does the substrate satisfy its own Riemann Hypothesis?  (off-session sanity test)',
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    png = os.path.join(OUT_DIR, 'rh_substrate_sanity.png')  # (local)
    fig.savefig(png, dpi=150)
    print(f'\nplot -> {png}')

    np.savez(os.path.join(OUT_DIR, 'rh_substrate_sanity.npz'),
             zeros_s3_dirac=np.array([complex(r) for r in zF]),
             zeros_riemann=np.array([complex(r) for r in zZ]),
             zeros_L_chi3=np.array([complex(r) for r in zL]),
             real_zeros_s3=np.array(rF),
             weyl_slope_pw=s_pw, weyl_slope_block=s_blk,
             window=np.array([WIN['x0'], WIN['x1'], WIN['y0'], WIN['y1']]))
    print(f'data -> rh_substrate_sanity.npz   ({time.time() - T0:.0f}s total)')
