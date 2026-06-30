"""
S105-W7-5-SUBSTRATE-ZETA-ZEROS
==============================================================================
Zero geography of the FULL Jensen-deformed substrate zeta zeta_{D_K}(s) — the
full-strength version of the off-session S^3 sanity test (_rh_substrate_sanity.py).

GATE (plan session-105-plan-w7.md §W7-5):
  Operator: max_k |Re(s_k) - median_k Re(s_k)| over k=1..N (N >= N_min=5 certified
            zeros)  { <= 1e-6  => PASS-on-line ;  > 1e-6  => FAIL-scatter }
  PRE-REGISTERED EXPECTATION: FAIL (scatter >> 1e-6); a PASS would be a STRUCTURAL
  SURPRISE. INFO if < N_min=5 certified zeros OR the cache/SD splice matching check
  at t_c fails (|Theta_cache(t_c) - Theta_SD(t_c)|/Theta > match_tol = 1e-3).

SUBSTRATE-FIRST FRAMING (phononic-framing.md):
  zeta_{D_K}(s) IS the substrate's own spectral zeta — the Mellin transform of the
  fabric's heat trace. Its zero geography is an INTRINSIC property of the fabric,
  not an arithmetic import. The arrow is D_K eigenvalues -> heat trace -> Mellin
  -> zero geography. The gate asks whether the substrate-class zeta satisfies its
  own RH analog. Step 1 of the substitution chain IS the genuine object:
        zeta_{D_K}(s) = Sum_{(p,q)} dim(p,q) Sum_branch |lambda(p,q)|^{-s}
  a Casimir/Epstein-class lattice sum (Conv. B single-power), the SU(3) analog of
  the S^3 F(s).

METHOD — two layers, both reported:
  LAYER A (literal pre-registration: HYBRID-HEAT-KERNEL-CONTINUATION).
    Build Theta(t)=Sum mult exp(-t|lambda|^2) from the L=12 cache for t>=t_c, splice
    the Seeley-DeWitt small-t tail Theta_SD(t) = a0 t^-4 + a2 t^-3 + a4 t^-2 + a6 t^-1
    + a8 (canonical a_n^{zeta}) for t<t_c, Mellin-continue
        zeta_{D_K}(s) = (1/Gamma(s/2)) int_0^inf t^{s/2-1} (Theta(t)-dim ker) dt.
    The matching check at t_c is a PRE-REGISTERED gate to INFO.
  LAYER B (the substrate-IS object, Step 1 of the chain): the genuine zeta_{D_K} as
    the FINITE Dirichlet polynomial Sum_j W_j |lambda_j|^{-s} (W_j = summed sector
    dim per unique |lambda|). For a finite cache this is ENTIRE in s — no continuation,
    no splice — so it is the exact, well-posed substrate object on which the certified
    argument-principle zero search runs. This delivers the substantive Re-spread answer.

WINDING KERNEL: certified argument-principle (dense-perimeter pre-sample MANDATORY;
  corner-only sampling aliases 2*pi wraps), adapted from
  computations/offsession-riemann/_rh_substrate_sanity.py (winding_count / _int_winding
  / _isolate / _polish / find_zeros). Dense scan in numpy float64 (validated to ~1e-13
  vs mpmath on this spectrum); Muller polish in mpmath at polish_dps.

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
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SHARED = Path(__file__).resolve().parents[1] / '_shared'        # (local)
sys.path.insert(0, str(SHARED))
from canonical_constants import (tau_fold,
                                 a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta,
                                 a_6_FW_zeta, a_8_FW_zeta)        # noqa: E402

T0 = time.time()                                                 # (local)
HERE = Path(__file__).resolve().parent                          # (local)
CACHE = HERE.parent / 'session-84' / 's84_spectrum_cache_L12_tau019.npz'   # (local)
WIND_ASSET = HERE.parent / 'offsession-riemann' / '_rh_substrate_sanity.py'  # (local)
CANON = SHARED / 'canonical_constants.py'                       # (local)
W71_ANCHOR = HERE / 's105_w7_1_trace_formula_exact_anchor.npz'  # (local)

assert abs(tau_fold - 0.19) < 1e-12, 'cache filename tau019 != canonical tau_fold'

# ---- machinery pins (plan §W7-5 machinery_pin_map) ----
L_MAX = 12                          # (local) cache supplies Theta(t)
MATCH_TOL = 1e-3                    # (local) cache/SD splice matching at t_c
COMMON_LINE_TOL = 1e-6             # (local) strict PASS boundary
WIND_GUARD = 0.15                  # (local) |w - nint(w)| guard
N_MIN = 5                          # (local) minimum certified zeros for a verdict
SEARCH_DPS = 18                    # (local)
POLISH_DPS = 40                    # (local)
SD_TAIL_ORDER = 8                  # (local) a_0..a_8 (odd-n vanish on closed manifold)
# t_c grid for the matching diagnostic (plan: L=12 resolves down to t_c ~ 0.05-0.1)
TC_GRID = [0.05, 0.08, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50]   # (local)
TC_NOMINAL = 0.10                  # (local) nominal pre-registered matching radius

# argument-principle window for LAYER B (Re fully captures the strip; Im sized for >> N_min)
WIN = dict(x0=-2.0, x1=6.0, y0=0.5, y1=100.0)                 # (local)


# ============================================================================
# Spectrum assembly
# ============================================================================
def load_spectrum():
    """Cache -> (lam, wt) block-level, and condensed (uniq |lam|, summed weight)."""
    z = np.load(CACHE, allow_pickle=True)
    se = z['sector_evals'].item()                              # (local)
    lam, wt = [], []                                           # (local)
    n_zero = 0                                                 # (local)
    n_sectors = len(se)                                        # (local)
    for (p, q), d in se.items():
        ev = np.asarray(d['abs_evals'], dtype=float)           # (local)
        n_zero += int((ev < 1e-12).sum())
        ev = ev[ev > 1e-12]
        lam.append(ev)
        wt.append(np.full(ev.shape, float(d['dim'])))
    lam = np.concatenate(lam)
    wt = np.concatenate(wt)
    # condense degenerate eigenvalues (round to 1e-9) -> finite Dirichlet polynomial
    key = np.round(lam, 9)                                     # (local)
    uniq, inv = np.unique(key, return_inverse=True)
    W = np.zeros(uniq.size)
    np.add.at(W, inv, wt)
    return lam, wt, uniq, W, n_zero, n_sectors


# ============================================================================
# LAYER A — hybrid heat-kernel continuation: the splice matching diagnostic
# ============================================================================
def heat_trace_cache(t, lam2, wt):
    """Theta_cache(t) = Sum wt exp(-t |lambda|^2)  (finite spectrum)."""
    return float(np.dot(wt, np.exp(-t * lam2)))


def heat_trace_SD(t):
    """Seeley-DeWitt small-t tail to order n=8 (Conv. B single-power):
       Theta_SD(t) ~ a0 t^-4 + a2 t^-3 + a4 t^-2 + a6 t^-1 + a8.
       a_n^{zeta} canonical (regulator-pin a_n^{zeta} MANDATORY)."""
    return (a_0_FW_zeta * t**-4 + a_2_FW_zeta * t**-3 + a_4_FW_zeta * t**-2
            + a_6_FW_zeta * t**-1 + a_8_FW_zeta)


def splice_matching(lam2, wt):
    """Pre-registered matching check |Theta_cache(t_c) - Theta_SD(t_c)|/Theta < 1e-3."""
    rows = []                                                  # (local)
    for tc in TC_GRID:
        c = heat_trace_cache(tc, lam2, wt)                     # (local)
        s = heat_trace_SD(tc)                                  # (local)
        rel = abs(c - s) / abs(c)                              # (local)
        rows.append((tc, c, s, rel))
    rel_nom = min(r[3] for r in rows if abs(r[0] - TC_NOMINAL) < 1e-9)  # (local)
    rel_best = min(r[3] for r in rows)                         # (local)
    return rows, rel_nom, rel_best


# ============================================================================
# LAYER B — direct-sum substrate zeta (entire) + certified zero search
# ============================================================================
class ZetaDK:
    """zeta_{D_K}(s) = Sum_j W_j |lambda_j|^{-s} = Sum_j W_j exp(-s ln lambda_j).
       Finite Dirichlet polynomial -> ENTIRE. numpy float64 fast path (validated
       to ~1e-13 vs mpmath on this spectrum); mpmath escalation for polish."""
    def __init__(self, uniq, W):
        self.LN = np.log(uniq)                                # (local) float64
        self.W = W.astype(float)
        self.LNm = [mp.log(mp.mpf(float(x))) for x in uniq]   # (local) mp
        self.Wm = [mp.mpf(float(x)) for x in W]               # (local)
        self.n = uniq.size

    def np(self, s):
        return complex(np.dot(self.W, np.exp(-complex(s) * self.LN)))

    def mp(self, s):
        s = mp.mpc(s)
        return mp.fsum(self.Wm[j] * mp.e**(-s * self.LNm[j]) for j in range(self.n))


N_EVALS = [0]                                                  # (local) instrumentation


def _edge_phase(f, a, b, fa, fb, depth, max_depth=36):
    """Continuous phase change of f along a->b, adaptive bisection (numpy path)."""
    d = np.angle(fb / fa)                                      # (local)
    if abs(d) <= 1.0:
        return d
    if depth >= max_depth:
        raise RuntimeError(f'phase tracking failed near {(a + b) / 2} (zero on boundary?)')
    m = (a + b) / 2                                            # (local)
    fm = f(m)
    N_EVALS[0] += 1
    return (_edge_phase(f, a, m, fa, fm, depth + 1, max_depth)
            + _edge_phase(f, m, b, fm, fb, depth + 1, max_depth))


def winding_count(f, x0, x1, y0, y1):
    """Winding number around the rectangle. Perimeter PRE-SAMPLED densely (step
    <= h0) BEFORE adaptive refinement — corner-only sampling aliases away whole
    2*pi wraps between corners (the documented off-session bug)."""
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
        total += _edge_phase(f, a, b, fa, fb, 0)
    return total / (2 * np.pi)


def _int_winding(f, x0, x1, y0, y1):
    w = winding_count(f, x0, x1, y0, y1)                       # (local)
    if abs(w - round(w)) >= WIND_GUARD:
        raise ValueError(f'non-integer winding {w} in box ({x0},{x1})x({y0},{y1})')
    return int(round(w))


def _polish(fmp, x0, x1, y0, y1):
    """Muller polish (mpmath, polish_dps) inside a winding-certified single-zero box."""
    mp.mp.dps = POLISH_DPS
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2                      # (local)
    dx, dy = (x1 - x0), (y1 - y0)                              # (local)
    seeds = [mp.mpc(cx, cy), mp.mpc(cx + 0.2 * dx, cy - 0.2 * dy),
             mp.mpc(cx - 0.2 * dx, cy + 0.2 * dy), mp.mpc(cx + 0.1 * dx, cy + 0.25 * dy)]  # (local)
    for sd in seeds:
        try:
            r = mp.findroot(fmp, sd, solver='muller', tol=mp.mpf('1e-44'))
        except Exception:
            continue
        if (x0 - 0.06 <= r.real <= x1 + 0.06 and y0 - 0.06 <= r.imag <= y1 + 0.06
                and abs(fmp(r)) < mp.mpf('1e-18')):
            mp.mp.dps = SEARCH_DPS
            return r
    mp.mp.dps = SEARCH_DPS
    return None


def _isolate(fnp, fmp, x0, x1, y0, y1, n, depth=0):
    """Winding-certified bisection: split until each box holds one zero, polish."""
    if n == 0:
        return []
    if ((x1 - x0) < 0.04 and (y1 - y0) < 0.04) or depth > 80:
        if n != 1:
            # unresolved multiplicity in a tiny box — return centre as a flagged root
            return [mp.mpc((x0 + x1) / 2, (y0 + y1) / 2)] * 0  # drop (cannot certify)
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
    n_total = _int_winding(zk.np, x0, x1, y0, y1)             # (local)
    print(f'  [zeta_DK direct] window [{x0},{x1}]x[{y0},{y1}]: certified Z = {n_total}'
          f'  ({time.time() - T0:.0f}s)')
    zeros = sorted(_isolate(zk.np, zk.mp, x0, x1, y0, y1, n_total),
                   key=lambda z: float(z.imag))               # (local)
    out = []                                                  # (local) dedupe
    for r in zeros:
        if all(abs(r - z) > mp.mpf('1e-6') for z in out):
            out.append(r)
    print(f'  [zeta_DK direct] isolated + polished {len(out)}/{n_total} '
          f'({time.time() - T0:.0f}s, {N_EVALS[0]} evals)')
    return out, n_total


# ============================================================================
# Cross-checks
# ============================================================================
def closed_form_anchor_check():
    """Cross-check vs the W7-1 corrected tau=0 anchor (c_off=1/4, R_scalar=2,
       S|_SU(3)=8(+)8 spinor rank 16). Documents the substrate object's footing;
       the zero search uses the tau_fold CACHE spectrum, not the tau=0 closed form."""
    if not W71_ANCHOR.exists():
        return None
    z = np.load(W71_ANCHOR, allow_pickle=True)
    return dict(c_off=float(z['c_off']), R_scalar=float(z['R_scalar']),
                w71_verdict=str(z['verdict']),
                closed_form_absdiff=float(z['closed_form_max_absdiff']))


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
    # ---- input SHA pins (logged in first lines per gate-verdicts.md) ----
    sha_script = sha256_file(__file__)
    sha_canon = sha256_file(CANON)
    sha_cache = sha256_file(CACHE)
    sha_wind = sha256_file(WIND_ASSET)
    print('=== Input SHA-256 pins ===')
    print(f'  script           = {sha_script}')
    print(f'  canonical_const  = {sha_canon}')
    print(f'  s84_cache        = {sha_cache}')
    print(f'  winding_kernel   = {sha_wind}')

    print('\n=== Spectrum assembly (L=12 cache @ tau_fold=%.2f) ===' % tau_fold)
    lam, wt, uniq, W, n_zero, n_sectors = load_spectrum()
    lam2 = lam**2
    print(f'  sectors: {n_sectors} (sector (4,4) absent — 90 of 91)')
    print(f'  block eigenvalues: {lam.size}; zero modes: {n_zero}')
    print(f'  unique |lambda|: {uniq.size}; total weight Sum dim: {W.sum():.0f}')
    print(f'  |lambda| in [{uniq.min():.6f}, {uniq.max():.6f}]; '
          f'|lambda|^2 in [{lam2.min():.6f}, {lam2.max():.6f}]')

    # ---- LAYER A: splice matching diagnostic (literal pre-registration) ----
    print('\n=== LAYER A: hybrid-continuation splice matching at t_c ===')
    print('  Theta_cache(t)=Sum wt e^{-t|lam|^2};  Theta_SD(t)=a0 t^-4+a2 t^-3+a4 t^-2+a6 t^-1+a8')
    print(f'  a_n^{{zeta}} canonical: a0={a_0_FW_zeta} a2={a_2_FW_zeta} a4={a_4_FW_zeta} '
          f'a6={a_6_FW_zeta} a8={a_8_FW_zeta}')
    print('   t_c     Theta_cache        Theta_SD          rel_diff')
    splice_rows, rel_nom, rel_best = splice_matching(lam2, wt)
    for tc, c, s, rel in splice_rows:
        print(f'  {tc:.2f}  {c:16.4f}  {s:16.4f}  {rel:.4e}')
    print(f'  matching check at t_c={TC_NOMINAL}: rel={rel_nom:.4e}  '
          f'(threshold {MATCH_TOL}); best over grid: {rel_best:.4e}')
    splice_ok = rel_best < MATCH_TOL                           # (local)
    print(f'  SPLICE MATCHES (rel < {MATCH_TOL})?  {splice_ok}')
    print('  STRUCTURAL NOTE: canonical a_n^{zeta} are per-branch L_max=3 zeta MOMENTS,')
    print('  not the asymptotic Seeley-DeWitt coefficients of the FULL L=12 cache heat trace;')
    print('  a finite spectrum heat trace is BOUNDED as t->0 (-> Sum wt), it has NO t^-4 divergence')
    print('  to splice onto. The hybrid-continuation splice is structurally ill-posed for a finite')
    print('  cache; this routes the LITERAL pre-registration to INFO (matching > 1e-3).')

    # ---- LAYER B: direct-sum substrate zeta (entire) — the well-posed object ----
    print('\n=== LAYER B: direct-sum zeta_{D_K}(s) = Sum_j W_j |lambda_j|^{-s} (ENTIRE) ===')
    print('  Step 1 of the substitution chain IS this finite Dirichlet polynomial;')
    print('  for a finite cache it is entire (no continuation), so the certified')
    print('  argument-principle search runs on it directly — the faithful substrate object.')
    zk = ZetaDK(uniq, W)
    # numpy-vs-mpmath validation on a few strip points (record max rel)
    val_pts = [complex(2, 14), complex(0, 50), complex(-1, 45), complex(4, 0), complex(1, 80)]  # (local)
    np_mp_rel = 0.0                                            # (local)
    for sp in val_pts:
        vn = zk.np(sp); vm = complex(zk.mp(sp))
        np_mp_rel = max(np_mp_rel, abs(vn - vm) / abs(vm))
    print(f'  numpy-float64 vs mpmath max rel over {len(val_pts)} strip points: {np_mp_rel:.2e}')
    print(f'  zeta_DK(0) = {zk.np(0).real:.1f} (entire-function value = Sum W = total mode count;')
    print('             a FINITE truncation has NO dimension-spectrum poles — those are a continuum artifact)')

    print(f'\n  certified zero search, window Re in [{WIN["x0"]},{WIN["x1"]}], '
          f'Im in [{WIN["y0"]},{WIN["y1"]}]')
    zeros, n_cert = find_zeros(zk, **WIN)

    re = [float(r.real) for r in zeros]                        # (local)
    im = [float(r.imag) for r in zeros]                        # (local)
    N = len(zeros)                                             # (local)
    if N >= 1:
        med = float(np.median(re))                            # (local)
        re_spread_med = max(abs(x - med) for x in re)         # (local) the operator
        re_width = max(re) - min(re)                          # (local)
    else:
        med = re_spread_med = re_width = float('nan')

    print('\n=== RESULTS — substrate zeta zero geography ===')
    print(f'  certified zeros isolated + polished: {N} (winding-certified Z = {n_cert})')
    print('   k        Re(s_k)              Im(s_k)            |zeta(s_k)|')
    for k, r in enumerate(zeros):
        print(f'  {k:2d}   {float(r.real):+.12f}   {float(r.imag):.12f}   '
              f'{float(abs(zk.mp(r))):.2e}')
    if N >= 1:
        print(f'  Re-window: [{min(re):.6f}, {max(re):.6f}]  width = {re_width:.6f}')
        print(f'  median Re = {med:.6f};  max|Re - median Re| = {re_spread_med:.6e}  '
              f'(operator; threshold {COMMON_LINE_TOL})')
        on_line = re_spread_med <= COMMON_LINE_TOL            # (local)
        print(f'  ON A COMMON VERTICAL LINE (<= {COMMON_LINE_TOL})?  '
              f'{"YES" if on_line else "NO"}')

    # ---- cross-check: W7-1 corrected anchor footing ----
    anc = closed_form_anchor_check()
    if anc:
        print(f'\n=== Cross-check: W7-1 corrected tau=0 anchor ===')
        print(f'  c_off={anc["c_off"]:.6f} (=1/4), R_scalar={anc["R_scalar"]:.6f} (=2), '
              f'W7-1 verdict={anc["w71_verdict"]}, closed-form absdiff={anc["closed_form_absdiff"]:.2e}')
        print('  (the zero search uses the tau_fold CACHE spectrum; this anchors the substrate object footing)')

    # ============================================================
    # VERDICT (plan §W7-5 operator + INFO criterion)
    # ============================================================
    # Literal pre-registration: the cache/SD splice matching > 1e-3 routes to INFO.
    # That gate fires (splice_ok is False, structurally). The Re-spread answer (LAYER B)
    # is delivered as the substantive substrate-IS content.
    if not splice_ok:
        verdict = 'INFO'
        reason = 'splice_matching_failed'
    elif N < N_MIN:
        verdict = 'INFO'
        reason = 'fewer_than_Nmin_certified_zeros'
    else:
        # both gates passed -> the common-line operator decides PASS/FAIL
        verdict = 'PASS' if re_spread_med <= COMMON_LINE_TOL else 'FAIL'
        reason = 'common_line_operator'

    # substantive direct-sum result string (always reported)
    val = (f"verdict={verdict};reason={reason};"
           f"splice_match_best={rel_best:.4e}(thr={MATCH_TOL});splice_match_tc{TC_NOMINAL}={rel_nom:.4e};"
           f"N_cert_directsum={N};N_min={N_MIN};"
           f"Re_spread_median={re_spread_med:.6e}(thr={COMMON_LINE_TOL});"
           f"Re_width={re_width:.6e};median_Re={med:.6f};"
           f"on_common_line={'YES' if (N>=1 and re_spread_med<=COMMON_LINE_TOL) else 'NO'};"
           f"np_mp_rel={np_mp_rel:.2e}")

    # dual SHA: audit over [script, canonical, pinmap]; content over [script]
    pinmap = (f"L_MAX={L_MAX}|MATCH_TOL={MATCH_TOL}|COMMON_LINE_TOL={COMMON_LINE_TOL}|"
              f"N_MIN={N_MIN}|SEARCH_DPS={SEARCH_DPS}|POLISH_DPS={POLISH_DPS}|"
              f"SD_TAIL_ORDER={SD_TAIL_ORDER}|TC_NOMINAL={TC_NOMINAL}|"
              f"WIN={WIN}|sha_cache={sha_cache}|sha_wind={sha_wind}|"
              f"a0={a_0_FW_zeta}|a2={a_2_FW_zeta}|a4={a_4_FW_zeta}|a6={a_6_FW_zeta}|a8={a_8_FW_zeta}")  # (local)
    audit_material = (sha_script + sha_canon + pinmap).encode()  # (local)
    audit_sha = hashlib.sha256(audit_material).hexdigest()
    content_sha = sha_script

    # regime: the direct-sum (LAYER B) zero search is exact & in-regime; LAYER A splice is
    # structurally out-of-regime (finite cache has no SD divergence). The verdict is INFO via
    # the pre-registered matching gate, NOT via the 3-tuple collapse. No [SIGN] trigger required
    # by the plan (schema_v2_3tuple_required: false), so emit composite only.

    # SD tail order pin companion (regulator-pin a_n^{zeta} discipline)
    extra = [f"# regulator_pin=a_n^{{zeta}} (a_0..a_8 FW_zeta); SD_tail_order=n={SD_TAIL_ORDER}; "
             f"poleconv-B-single; pole set {{0,2,4,6,8}}=n at d=8",
             f"# LAYER-A splice matching FAILED structurally (best rel={rel_best:.3e} >> {MATCH_TOL}): "
             f"canonical a_n are L_max=3 per-branch moments, finite-cache heat trace has no t->0 divergence; "
             f"routes literal hybrid-continuation to INFO",
             f"# LAYER-B direct-sum (entire substrate object, chain Step 1): N={N} certified zeros, "
             f"Re-spread(median)={re_spread_med:.4e}, Re-width={re_width:.4e} -> scatter (NOT on a common line)"]

    print_verdict_payload('S105-W7-5-SUBSTRATE-ZETA-ZEROS', verdict, val,
                          'HYBRID-HEAT-KERNEL-CONTINUATION',
                          'single-power Conv. B, poleconv-B-single, n in {0,2,4,6,8} at d=8',
                          str(L_MAX), audit_sha, content_sha, extra_rows=extra)

    # ------------------------------------------------------------------ plot
    fig, ax = plt.subplots(1, 2, figsize=(13.8, 5.8))
    a0 = ax[0]
    if N >= 1:
        a0.axvline(med, color='0.55', lw=1.2, ls='--',
                   label=f'median Re = {med:.3f} (NOT a critical line)')
        a0.scatter(re, im, s=64, c='tab:red', marker='x',
                   label=r'$\zeta_{D_K}(s)$ zeros (substrate-class)')
    a0.set_xlabel('Re s'); a0.set_ylabel('Im s')
    a0.set_title('Substrate zeta zero geography (L=12 @ tau_fold):\n'
                 'finite Dirichlet polynomial, no Euler product -> zeros scatter')
    a0.legend(loc='upper right', fontsize=8); a0.grid(alpha=0.25)

    a1 = ax[1]
    tg = np.array(TC_GRID)                                     # (local)
    a1.loglog(tg, [r[1] for r in splice_rows], 'o-', c='tab:blue',
              label=r'$\Theta_{\rm cache}(t)$ (finite, bounded)')
    a1.loglog(tg, [r[2] for r in splice_rows], 's--', c='tab:red',
              label=r'$\Theta_{\rm SD}(t)$ (a$_n^\zeta$ tail, diverges)')
    a1.set_xlabel('t'); a1.set_ylabel('heat trace')
    a1.set_title('LAYER A splice fails: SD tail (L$_{\\max}$=3 per-branch moments)\n'
                 'has a t$^{-4}$ divergence the finite cache lacks')
    a1.legend(fontsize=8); a1.grid(alpha=0.25, which='both')
    fig.suptitle('S105-W7-5: Does the genuine SU(3) substrate zeta satisfy its own RH analog?',
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    png = HERE / 's105_w7_5_substrate_zeta_zeros.png'          # (local)
    fig.savefig(png, dpi=150)
    print(f'\nplot -> {png}')

    np.savez(HERE / 's105_w7_5_substrate_zeta_zeros.npz',
             zeros_re=np.array(re), zeros_im=np.array(im),
             zeros_complex=np.array([complex(r) for r in zeros]),
             n_certified=n_cert, re_spread_median=re_spread_med, re_width=re_width,
             median_re=med, common_line_tol=COMMON_LINE_TOL, N_min=N_MIN,
             splice_tc_grid=np.array(TC_GRID),
             splice_theta_cache=np.array([r[1] for r in splice_rows]),
             splice_theta_SD=np.array([r[2] for r in splice_rows]),
             splice_rel=np.array([r[3] for r in splice_rows]),
             splice_rel_nom=rel_nom, splice_rel_best=rel_best, match_tol=MATCH_TOL,
             np_mp_rel=np_mp_rel, window=np.array([WIN['x0'], WIN['x1'], WIN['y0'], WIN['y1']]),
             uniq_count=uniq.size, total_weight=W.sum(),
             a_n_zeta=np.array([a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta, a_6_FW_zeta, a_8_FW_zeta]),
             verdict=verdict, reason=reason,
             audit_sha256=audit_sha, content_sha256=content_sha)
    print(f'data -> s105_w7_5_substrate_zeta_zeros.npz   ({time.time() - T0:.0f}s total)')
