#!/usr/bin/env python3
"""
S105 W7-6 — S105-W7-6-S3-ZETA-ASYMPTOTICS — S^3 Dirac zeta high-t zero census
============================================================================

Gate: S105-W7-6-S3-ZETA-ASYMPTOTICS ([VERIFY])
Classification: GEOMETRIC

INFO-by-construction (composite-precedence override of the generic schema-v2
collapse): the deliverable is a CERTIFIED zero census of the exact S^3=SU(2)
Dirac zeta F(s) over Im in [36, 300] (three panels), a Re-distribution
histogram, and a zero-density fit N(T) vs (T/2pi) log(T/2pi e). There is NO
expected critical line for F(s) (it has the functional-equation mirror but no
Euler product). FAIL is reserved for unresolvable machinery failure ONLY: a
non-integer argument-principle winding count that survives full adaptive
refinement on some panel. The scatter being large is NOT a FAIL — it is the
substrate-IS finding.

This CLOSES the off-session caveat #5 (window-finite certification): the
off-session sanity test (`computations/offsession-riemann/_rh_substrate_sanity.py`)
certified 3 scattered zeros in Im <= 36.13 with Re-spread 0.93 on no common
line; this gate extends that certification to Im <= 300 with a limiting-density
characterization (does the scatter persist / drift / asymptote toward the
Re = 5/2 ghost line of zeta(s-2)'s shifted mirror?).

SUBSTRATE FRAMING (phononic-framing.md): F(s) is the exact Dirac zeta of the
S^3=SU(2) round geometry — the substrate's analytically closed little brother,
same structural genre (Casimir lattice sum with Weyl-dimension multiplicities)
as zeta_{D_K} on SU(3). The arrow is:
  S^3 Dirac spectrum (|lambda|=k+3/2, mult (k+1)(k+2))
    -> closed-form zeta F(s)
    -> certified zero census over Im in [36,300]
    -> limiting Re-distribution
It is the analytically clean witness for the W7-5 expected FAIL on the genuine
(non-closed-form) SU(3) object: a mirror-without-pin spectral functional
scatters its zeros at large height and pins to nothing.

CLOSED FORM (Conv. B single-power; Sage-verified to 1e-23 off-session,
reproduced here):
  Step 1:  m_k = (k+1)(k+2) = (k+3/2)^2 - 1/4
  Step 2:  zeta_D(s) = zeta_H(s-2, 3/2) - (1/4) zeta_H(s, 3/2)
  Step 3:  zeta_H(s, 3/2) = (2^s - 1) zeta(s) - 2^s
  Step 4:  F(s) = (2^{s-2} - 1) zeta(s-2) - (2^{s-2} - 1/4) zeta(s)
  poles only at s=3 (res 1) and s=1 (res -1/4); both on the real axis, FAR
  below Im=36, so EVERY panel's winding count is pure zero count (Z - P, P=0).

WINDING HAZARD (the off-session prototype's load-bearing fix, retained here):
  corner-only perimeter sampling aliases away whole 2*pi wraps between corners,
  silently undercounting zeros. The perimeter is PRE-SAMPLED DENSELY (step
  h0 <= 0.2) BEFORE adaptive refinement, and zero counts are certified by
  winding-certified bisection with a per-box non-integer guard
  |w - nint(w)| < 0.15.

DISCIPLINE
----------
- `from canonical_constants import *` (tau_fold imported as the cache-pin
  witness only; this gate is closed-form F(s) with NO cache dependency).
- Every local/intermediate tagged `# (local)`.
- Pure mpmath arbitrary precision; cpu-cap-OMP8 (no GPU / matrix / cache work).
- audit_sha256 + content_sha256 (S84+ dual-SHA schema).
- Verdict emitted via the `emit_verdict` knowledge-MCP tool: this script PRINTS
  the payload (print_verdict_payload), the dispatching agent calls emit_verdict.
- A mandatory `# composite-precedence:` companion row is carried in the payload
  extra_rows per gate-verdicts.md §"Plan-frozen gate-block operator precedence".
"""

from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[1] / "_shared"))  # _shared on path
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold, PI  # noqa: E402  explicit witnesses

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Safety margin: winding-certified bisection of a coarse strip can stack ~depth
# 72; raise the limit well above so an unexpectedly deep box never overflows the
# Python stack before the depth-72 guard in _isolate trips.
sys.setrecursionlimit(20000)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
OFFSESSION_DIR = COMPUTATIONS_DIR / "offsession-riemann"

SESSION = "S105"                                                   # (local)
GATE_ID = "S105-W7-6-S3-ZETA-ASYMPTOTICS"                          # (local)
SCHEME = "CLOSED-FORM-S3-DIRAC-ZETA"                               # (local)
CONVENTION = ("single-power-ConvB-poleconv-B-single_"
              "F(s)=(2^{s-2}-1)zeta(s-2)-(2^{s-2}-1/4)zeta(s)_"
              "Re=5/2-ghost-ref")                                  # (local)
L_MAX = "NA-closed-form"                                           # (local)

# Pre-registered machinery pins (PRDR; from the plan machinery_pin_map)
H0_MAX = mp.mpf('0.2')          # (local) dense-perimeter anti-aliasing step ceiling
WIND_GUARD = mp.mpf('0.15')     # (local) non-integer winding guard (FAIL route)
SEARCH_DPS = 20                 # (local) >= 18 per pin
POLISH_DPS = 40                 # (local) >= 35 per pin
RE_GHOST = mp.mpf('2.5')        # (local) Re=5/2 ghost line (mirror of zeta(s-2): Re(s-2)=1/2)

# Panel windows: Im in [36,100],[100,200],[200,300]; Re window brackets the
# scatter band + the Re=5/2 ghost with margin. Edges jittered to dodge on-edge
# zeros (off-session prototype convention). Poles at s=3,s=1 are on the real
# axis, FAR below Im=36 -> outside every panel -> winding == zero count.
RE_LO = mp.mpf('-4.53')         # (local) jittered left edge
RE_HI = mp.mpf('5.47')          # (local) jittered right edge (brackets Re=5/2 ghost + scatter)
PANELS = [                      # (local) (im_lo, im_hi) per panel, edges jittered
    (mp.mpf('36.07'), mp.mpf('100.13')),
    (mp.mpf('100.13'), mp.mpf('200.11')),
    (mp.mpf('200.11'), mp.mpf('300.17')),
]

OUT_NPZ = SESSION_DIR / "s105_w7_6_s3_zeta_asymptotics.npz"
OUT_PNG = SESSION_DIR / "s105_w7_6_s3_zeta_asymptotics.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    OFFSESSION_DIR / "_rh_substrate_sanity.py",   # certified winding kernel + F_s3 closed form (reused asset)
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    """Print the verdict PAYLOAD (delimited JSON) for the dispatching AGENT to
    pass to the knowledge-MCP `emit_verdict` tool. Mirrors
    `.claude/templates/script-template.py` print_verdict_payload (lines 226-279):
    the script does NOT write the verdict file (the race-safe lock-serialized
    write is owned by `emit_verdict`); it only PRINTS the payload, which the
    agent extracts from stdout and passes to emit_verdict(**payload)."""
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
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 5 — Closed-form F(s) and reduction verification
# ---------------------------------------------------------------------------
def F_s3(s):
    """Exact S^3 Dirac zeta, one chirality branch (Conv. B single-power).
    Identical to the off-session certified kernel's F_s3."""
    s = mp.mpc(s)
    c = mp.power(2, s - 2)  # (local)
    return (c - 1) * mp.zeta(s - 2) - (c - mp.mpf(1) / 4) * mp.zeta(s)


# Poles inside a search box (for winding = Z - P accounting). At Im>=36 there
# are NONE (poles at s=3,s=1 are on the real axis).
POLES_REAL = [mp.mpf(3), mp.mpf(1)]   # (local)


def verify_reduction():
    """Reproduce the off-session substitution-chain numeric check (closed form
    validated to 1e-23). Returns the worst Hurwitz-reduction residual."""
    mp.mp.dps = 30
    print('=== Closed-form verification (S^3 Dirac zeta), reproduced in-script ===')
    worst = mp.mpf(0)  # (local)
    # Step 2 check: direct sum == Hurwitz combo, real points.
    for s_test in [mp.mpf(5), mp.mpf('6.3')]:
        direct = mp.nsum(lambda k: (k + 1) * (k + 2) * mp.power(k + mp.mpf(3) / 2, -s_test),
                         [0, mp.inf])  # (local)
        err = abs(direct - F_s3(s_test))  # (local)
        print(f'  s = {mp.nstr(s_test, 8):>12s}:  |direct sum - closed| = {mp.nstr(err, 3)}')
        assert err < mp.mpf('1e-10'), 'closed form mismatch (direct sum)'
    # Steps 3-4 check: Hurwitz combo == final formula, complex points, exact.
    for s_test in [mp.mpc('3.7', '2.0'), mp.mpc('0.3', '14.0'), mp.mpc('-1.2', '5.0'),
                   mp.mpc('2.5', '120.0')]:
        hurwitz = mp.zeta(s_test - 2, mp.mpf(3) / 2) - mp.zeta(s_test, mp.mpf(3) / 2) / 4  # (local)
        err = abs(hurwitz - F_s3(s_test))  # (local)
        print(f'  s = {mp.nstr(s_test, 10):>16s}:  |Hurwitz combo - closed| = {mp.nstr(err, 3)}')
        worst = max(worst, err)
        assert err < mp.mpf('1e-22'), 'closed form mismatch (Hurwitz reduction)'
    # Pole residues (sanity).
    eps = mp.mpf('1e-12')  # (local)
    r3 = F_s3(3 + eps) * eps  # (local)
    r1 = F_s3(1 + eps) * eps  # (local)
    print(f'  residue @ s=3: {mp.nstr(r3, 6)} (expect 1);  @ s=1: {mp.nstr(r1, 6)} (expect -0.25)')
    print(f'  worst Hurwitz-reduction residual = {mp.nstr(worst, 3)} (closed form bit-tight to ~1e-22)')
    return worst


# ---------------------------------------------------------------------------
# Section 6 — Argument-principle certified zero search (certified winding kernel)
# Reproduced from `_rh_substrate_sanity.py` (dense-perimeter pre-sampling
# MANDATORY; winding-certified bisection; Muller polish).
# ---------------------------------------------------------------------------
N_EVALS = [0]   # (local) instrumentation


class _BoundaryZero(RuntimeError):
    """Signals a zero grazing (or on) the integration contour — the caller
    re-cuts at a different jitter offset (the on-contour set is measure-zero)."""


def _edge_phase(f, a, b, fa, fb, depth, max_depth=38):
    """Continuous phase change of f along segment a->b, adaptive bisection.

    max_depth = 38 (off-session kernel used 34): a zero at distance δ from the
    contour produces a phase swing resolvable in ~log2(seg/δ) bisections
    (~31 levels at δ~1e-10, seg~h0=0.2), so 38 keeps a margin for the larger
    window's legitimately-close zeros WITHOUT exponential blowup. A zero closer
    than ~1e-11 to the contour is effectively ON it (measure-zero); _edge_phase
    raises _BoundaryZero FAST (≤2^4× the off-session cost) and the caller's
    cut-retry dodges it with a fresh jitter offset. Deeper tracking (the earlier
    max_depth=60 attempt) is WRONG: it costs 2^(60-34) evals per on-contour zero
    before aborting — the cut-retry, not deeper tracking, is the right fix."""
    d = mp.arg(fb / fa)  # (local)
    if abs(d) <= mp.mpf('1.0'):
        return d
    if depth >= max_depth:
        raise _BoundaryZero(f'phase tracking failed near {mp.nstr((a + b) / 2, 6)} (zero on contour)')
    m = (a + b) / 2  # (local)
    fm = f(m); N_EVALS[0] += 1  # (local)
    return (_edge_phase(f, a, m, fa, fm, depth + 1, max_depth)
            + _edge_phase(f, m, b, fm, fb, depth + 1, max_depth))


def winding_count(f, x0, x1, y0, y1):
    """Winding number around the rectangle. Perimeter PRE-SAMPLED densely
    (step <= h0 <= 0.2) before adaptive refinement — corner-only sampling
    aliases away whole 2*pi wraps between corners, silently undercounting."""
    h0 = max(mp.mpf('0.02'), min(H0_MAX, min(x1 - x0, y1 - y0) / 4))  # (local)
    pts = []  # (local)
    corners = [mp.mpc(x0, y0), mp.mpc(x1, y0), mp.mpc(x1, y1), mp.mpc(x0, y1)]  # (local)
    for a, b in zip(corners, corners[1:] + corners[:1]):
        n_seg = max(1, int(mp.ceil(abs(b - a) / h0)))  # (local)
        for i in range(n_seg):
            pts.append(a + (b - a) * mp.mpf(i) / n_seg)
    pts.append(corners[0])
    vals = [f(p) for p in pts]  # (local)
    N_EVALS[0] += len(pts)
    total = mp.mpf(0)  # (local)
    for (a, fa), (b, fb) in zip(zip(pts[:-1], vals[:-1]), zip(pts[1:], vals[1:])):
        total += _edge_phase(f, a, b, fa, fb, 0)
    return total / (2 * mp.pi)


def _int_winding(f, x0, x1, y0, y1):
    w = winding_count(f, x0, x1, y0, y1)  # (local)
    assert abs(w - mp.nint(w)) < WIND_GUARD, f'non-integer winding {w}'  # the ONLY FAIL route
    return int(mp.nint(w))


# ---------------------------------------------------------------------------
# Locator: grid-seeded Muller (robust replacement for recursive box-isolation).
# The off-session kernel located zeros by winding-certified RECURSIVE BISECTION
# (_isolate). Over the 10x-larger Im in [36,300] window that is fragile + slow:
# a forced bisection cut can graze a zero (the off-session "zero on boundary"
# RuntimeError), and a cut-retry re-descends the whole subtree -> combinatorial
# blowup near a near-contour zero. The COUNT certification (dense-perimeter
# winding) is robust and is KEPT; only the LOCATION step is replaced. A zero is
# located by seeding mpmath Muller from a dense (Re x Im) grid over the strip —
# Muller from many seeds reliably converges to well-separated zeros with NO
# forced cuts, so there is nothing for a zero to graze. Completeness is
# cross-checked against the strip's certified winding count; an under-count
# densifies the seed grid (bounded retries).
# ---------------------------------------------------------------------------
def _grid_locate(f, x0, x1, y0, y1, n_expect, polish_dps, search_dps,
                 nx0=9, ny0=7, max_refine=4):
    """Locate the n_expect zeros in the box by Muller from a (Re x Im) seed grid.

    Returns the distinct polished zeros whose Im lies in the HALF-OPEN strip
    [y0, y1) (with a tiny polish-drift tolerance) — strip membership by the
    half-open Im interval makes each zero belong to EXACTLY ONE strip, so an
    edge-straddling zero is never claimed by both neighbours. Re must be inside
    [x0, x1] with a tiny pad. The grid is densified up to max_refine times and
    ALL grid-found roots are collected (no early-stop) before the count check —
    early-stopping at n_expect could return a neighbour's edge-zero and miss
    this strip's own root."""
    if n_expect == 0:
        return []
    mp.mp.dps = polish_dps
    eps_drift = mp.mpf('1e-7')  # (local) polish drift only (NOT a band-widening pad)
    found = []  # (local)
    nx, ny = nx0, ny0  # (local)
    for _ref in range(max_refine + 1):
        xs = [x0 + (x1 - x0) * (mp.mpf(2 * i + 1) / (2 * nx)) for i in range(nx)]  # (local)
        ys = [y0 + (y1 - y0) * (mp.mpf(2 * j + 1) / (2 * ny)) for j in range(ny)]  # (local)
        for sx in xs:
            for sy in ys:
                seed = mp.mpc(sx, sy)  # (local)
                try:
                    r = mp.findroot(f, seed, solver='muller', tol=mp.mpf('1e-44'))  # (local)
                except Exception:
                    continue
                # Re strictly inside [x0,x1]; Im in the HALF-OPEN strip [y0,y1)
                # (so an edge zero belongs to exactly one strip, never both).
                if not (x0 - eps_drift <= r.real <= x1 + eps_drift):
                    continue
                if not (y0 - eps_drift <= r.imag < y1 - eps_drift):
                    continue
                if abs(f(r)) > mp.mpf('1e-18'):
                    continue
                if all(abs(r - z) > mp.mpf('1e-9') for z in found):
                    found.append(r)
        N_EVALS[0] += nx * ny
        if len(found) >= n_expect:
            break
        nx, ny = nx * 2 - 1, ny * 2 - 1  # densify and retry
    mp.mp.dps = search_dps
    return found


STRIP_H = mp.mpf('2.5')   # (local) fine Im-strip height: each holds 0-2 zeros for tight winding xref


def find_zeros_panel(f, panel_idx, x0, x1, y0, y1, polish_dps=POLISH_DPS, search_dps=SEARCH_DPS):
    """Certified count (dense-perimeter winding), then grid-seeded Muller location.

    (a) The panel is certified as a whole (one winding count = the headline
        certification). (b) It is partitioned into fine Im-strips of height
        <= STRIP_H; each strip's count is independently winding-certified
        (dense-perimeter anti-aliasing on every strip boundary). The SUM of
        per-strip counts MUST equal the whole-panel count (an independent
        second argument-principle certification). (c) Each strip's zeros are
        located by grid-seeded Muller (_grid_locate) and cross-checked against
        the strip's certified count. No recursive bisection cut is ever made,
        so the off-session 'zero on boundary' hazard cannot arise in the
        LOCATION step; the COUNT step's winding guard |w-nint(w)|<0.15 is the
        sole FAIL route (a residual non-integer winding after dense sampling).
    """
    mp.mp.dps = search_dps
    # window bottom sits above Im=0 -> real-axis poles outside; assert it.
    assert y0 > 0 and all(p.imag == 0 for p in [mp.mpc(q) for q in POLES_REAL])
    # (a) whole-panel certified count (the headline certification)
    w_raw = winding_count(f, x0, x1, y0, y1)  # (local) raw (pre-rounding) winding
    nonint_panel = abs(w_raw - mp.nint(w_raw))  # (local) residual
    n_total = int(mp.nint(w_raw))  # (local)
    assert nonint_panel < WIND_GUARD, f'panel {panel_idx}: non-integer panel winding {w_raw}'  # FAIL route
    print(f'  [panel {panel_idx}] Re[{mp.nstr(x0,5)},{mp.nstr(x1,5)}] x '
          f'Im[{mp.nstr(y0,6)},{mp.nstr(y1,6)}]: '
          f'certified Z = {n_total} (raw winding {mp.nstr(w_raw, 12)}, residual {mp.nstr(nonint_panel, 3)})')
    # (b) fine Im-strip partition (jittered edges); certify each strip
    n_strips = max(1, int(mp.ceil((y1 - y0) / STRIP_H)))  # (local)
    edges = [y0 + (y1 - y0) * mp.mpf(i) / n_strips for i in range(n_strips + 1)]  # (local)
    for i in range(1, n_strips):  # jitter interior edges only
        edges[i] += mp.mpf('0.0091') * (y1 - y0) / n_strips
    out = []  # (local) polished zeros
    strip_sum = 0  # (local) cross-check accumulator
    max_strip_resid = float(nonint_panel)  # (local)
    for i in range(n_strips):
        sy0, sy1 = edges[i], edges[i + 1]  # (local)
        w_s = winding_count(f, x0, x1, sy0, sy1)  # (local)
        r_s = abs(w_s - mp.nint(w_s))  # (local)
        assert r_s < WIND_GUARD, f'panel {panel_idx} strip {i}: non-integer winding {w_s}'  # FAIL route
        max_strip_resid = max(max_strip_resid, float(r_s))
        n_s = int(mp.nint(w_s))  # (local)
        strip_sum += n_s
        zs = _grid_locate(f, x0, x1, sy0, sy1, n_s, polish_dps, search_dps)  # (local)
        # per-strip completeness: grid-Muller must find exactly the certified count
        assert len(zs) == n_s, (f'panel {panel_idx} strip {i+1}: grid-located {len(zs)} '
                                f'!= winding-certified {n_s} (densify grid)')
        out.extend(zs)
        print(f'    [panel {panel_idx} strip {i+1}/{n_strips}] '
              f'Im[{mp.nstr(sy0,7)},{mp.nstr(sy1,7)}]: Z_strip = {n_s} '
              f'(located {len(zs)}; {time.time() - T0:.0f}s, {N_EVALS[0]} evals)')
    # structural cross-check: strip-sum == panel total (second independent certification)
    assert strip_sum == n_total, \
        f'panel {panel_idx}: strip-sum {strip_sum} != whole-panel {n_total} (winding inconsistency)'
    out = sorted(out, key=lambda z: float(z.imag))
    # Dedup at 1e-9: a SAME zero found in two adjacent strips straddling it
    # polishes to ~1e-30 agreement (merged); the closest pair of DISTINCT zeros
    # in this object is O(0.5) apart in Re and O(1.6) in Im (never within 1e-9),
    # so distinct zeros are never merged. (The 1e-6 used during the off-session
    # single-window search was too loose for the dense high-Im census — it could
    # merge two genuinely-distinct close zeros.)
    dedup = []  # (local)
    for r in out:
        if all(abs(r - z) > mp.mpf('1e-9') for z in dedup):
            dedup.append(r)
    assert len(dedup) == n_total, \
        (f'panel {panel_idx}: deduped-located {len(dedup)} != certified {n_total} '
         f'(strip_sum={strip_sum}); a zero near a strip edge was double-counted or lost')
    print(f'  [panel {panel_idx}] located + polished {len(dedup)}/{n_total} zeros; '
          f'strip-sum cross-check {strip_sum}=={n_total} OK '
          f'({time.time() - T0:.0f}s elapsed, {N_EVALS[0]} cumulative evals)')
    return dedup, n_total, max_strip_resid


# ---------------------------------------------------------------------------
# Section 7 — Density fits
# ---------------------------------------------------------------------------
def riemann_log_count(T):
    """Riemann-style log-corrected zero count N(T) = (T/2pi) log(T/2pi e)."""
    T = np.asarray(T, dtype=float)  # (local)
    return (T / (2 * np.pi)) * np.log(T / (2 * np.pi * np.e))


def fit_power_law(T, N):
    """Free-exponent power-law N ~ A * T^p (log-log least squares)."""
    T = np.asarray(T, dtype=float)
    N = np.asarray(N, dtype=float)
    m = (T > 0) & (N > 0)  # (local)
    p, lnA = np.polyfit(np.log(T[m]), np.log(N[m]), 1)  # (local)
    return float(p), float(np.exp(lnA))


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
T0 = time.time()  # (local) module-level start (used by find_zeros_panel prints)


def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins + dual SHA
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  tau_fold (cache-pin witness, unused by closed form) = {tau_fold}; PI = {mp.nstr(PI,8)}")
    print()

    # 2. Verify closed form
    worst_resid = verify_reduction()
    print()

    # 3. Certified zero census over the three Im panels
    print('=== Certified zero census: Im in [36,300], three panels ===')
    all_zeros = []         # (local) flat list of polished complex zeros
    panel_counts = []      # (local)
    panel_nonint = []      # (local) max non-integer winding residual per panel
    panel_bounds = []      # (local)
    machinery_fail = False  # (local) set True only if a panel winding stays non-integer
    fail_detail = ""        # (local)
    for idx, (im_lo, im_hi) in enumerate(PANELS, start=1):
        try:
            zs, n_tot, nonint = find_zeros_panel(F_s3, idx, RE_LO, RE_HI, im_lo, im_hi)
        except (AssertionError, _BoundaryZero) as exc:
            # FAIL route: non-integer winding after dense sampling (AssertionError
            # from the winding guard / strip-sum xref), OR a genuine on-contour
            # zero during the COUNT step that survives dense perimeter sampling
            # (_BoundaryZero). Both are unresolvable winding-certification failures.
            machinery_fail = True
            fail_detail = f"panel {idx}: {exc}"
            print(f"  [panel {idx}] MACHINERY FAILURE: {exc}")
            break
        all_zeros.extend(zs)
        panel_counts.append(n_tot)
        panel_nonint.append(nonint)
        panel_bounds.append((float(RE_LO), float(RE_HI), float(im_lo), float(im_hi)))

    mp.mp.dps = 30

    # 4. Census table + Re-distribution
    print('\n=== ZERO CENSUS (Im in [36,300]) ===')
    reF = [float(r.real) for r in all_zeros]  # (local)
    imF = [float(r.imag) for r in all_zeros]  # (local)
    n_zeros = len(all_zeros)  # (local)
    print(f'  total certified zeros: {n_zeros}  (panel counts: {panel_counts})')
    for r in all_zeros:
        print(f'    s = {float(r.real):+.10f} + {float(r.imag):.10f} i'
              f'   |Re - 5/2| = {abs(float(r.real) - 2.5):.6f}')

    re_spread = (max(reF) - min(reF)) if reF else 0.0  # (local)
    re_median = float(np.median(reF)) if reF else 0.0  # (local)
    re_mean = float(np.mean(reF)) if reF else 0.0       # (local)
    on_common_line = (re_spread < 1e-6)  # (local)
    # distance of each zero's Re to the Re=5/2 ghost line
    dist_ghost = [abs(x - 2.5) for x in reF]  # (local)
    mean_dist_ghost = float(np.mean(dist_ghost)) if dist_ghost else 0.0  # (local)

    print(f'\n  Re spread: [{min(reF):.6f}, {max(reF):.6f}]  width = {re_spread:.6f}' if reF else '  (no zeros)')
    print(f'  Re median = {re_median:.6f}; Re mean = {re_mean:.6f}')
    print(f'  ON A COMMON VERTICAL LINE? {"YES" if on_common_line else "NO"} '
          f'(common-line PASS structurally inapplicable to F(s): no Euler product)')
    print(f'  mean |Re - 5/2 ghost| = {mean_dist_ghost:.6f}')

    # 5. Re=5/2 ghost-proximity TREND: does the scatter drift toward Re=5/2 with
    #    increasing height? Compare the per-zero |Re-5/2| against Im (Spearman-ish
    #    sign via a linear regression slope of dist_ghost vs Im).
    ghost_trend_slope = 0.0   # (local)
    low_band_mean = high_band_mean = 0.0  # (local)
    if n_zeros >= 4:
        slope, _ = np.polyfit(np.asarray(imF), np.asarray(dist_ghost), 1)  # (local)
        ghost_trend_slope = float(slope)
        # split low vs high height at the median Im
        med_im = float(np.median(imF))  # (local)
        lo = [d for d, t in zip(dist_ghost, imF) if t <= med_im]  # (local)
        hi = [d for d, t in zip(dist_ghost, imF) if t > med_im]   # (local)
        low_band_mean = float(np.mean(lo)) if lo else 0.0
        high_band_mean = float(np.mean(hi)) if hi else 0.0
        trend_word = ("DRIFTS TOWARD" if ghost_trend_slope < -1e-4
                      else "DRIFTS AWAY FROM" if ghost_trend_slope > 1e-4
                      else "PERSISTS (no drift) relative to")
        print(f'\n  Re=5/2 ghost-proximity trend: d(|Re-5/2|)/d(Im) slope = {ghost_trend_slope:+.6e}')
        print(f'    low-height (<= median Im) mean |Re-5/2| = {low_band_mean:.6f}; '
              f'high-height mean = {high_band_mean:.6f}')
        print(f'    => scatter {trend_word} the Re=5/2 ghost line over Im in [36,300]')

    # 6. Density fit N(T) vs (T/2pi)log(T/2pi e) AND free power law
    Tsorted = np.sort(np.asarray(imF))  # (local)
    Ncum = np.arange(1, Tsorted.size + 1, dtype=float)  # (local) cumulative count
    N_riemann_pred = riemann_log_count(Tsorted) if Tsorted.size else np.array([])  # (local)
    # offset the Riemann prediction to the census window start (counts from Im=36)
    if Tsorted.size:
        # N(T) - N(T_min) form for fair comparison to the windowed cumulative count
        N_riemann_windowed = N_riemann_pred - riemann_log_count(np.array([float(PANELS[0][0])]))[0]  # (local)
    else:
        N_riemann_windowed = np.array([])
    plaw_exp, plaw_amp = (fit_power_law(Tsorted, Ncum) if Tsorted.size >= 3 else (0.0, 0.0))  # (local)
    # ratio of observed count to Riemann-log expectation at the top of the window
    riemann_ratio_top = (float(Ncum[-1] / N_riemann_windowed[-1])
                         if Tsorted.size and N_riemann_windowed[-1] > 0 else 0.0)  # (local)

    print(f'\n=== DENSITY FIT ===')
    print(f'  cumulative zero count N(T_top={float(Tsorted[-1]):.2f}) = {int(Ncum[-1])}'
          if Tsorted.size else '  (no zeros to fit)')
    if Tsorted.size:
        print(f'  Riemann-style windowed expectation N(T)-N(36) at T_top = {N_riemann_windowed[-1]:.3f}')
        print(f'  observed / Riemann-log expectation (at T_top) = {riemann_ratio_top:.4f}')
        print(f'  free power-law fit: N ~ {plaw_amp:.4g} * T^{plaw_exp:.4f}')
        print(f'  (Riemann log-corrected count grows ~ T log T, i.e. super-linear slope -> 1+; '
              f'a sub-linear power-law exponent => sparser-than-arithmetic zero density)')

    # 7. Verdict — INFO-by-construction (composite-precedence override).
    if machinery_fail:
        verdict = "FAIL"
        value = (f"MACHINERY-FAIL_non-integer-winding_{fail_detail.replace(chr(39),'')}"
                 f"_guard={float(WIND_GUARD)}")
    else:
        verdict = "INFO"
        value = (f"n_zeros={n_zeros}_panels={panel_counts}_"
                 f"Re_spread={re_spread:.4f}_Re_median={re_median:.4f}_Re_mean={re_mean:.4f}_"
                 f"common_line={'NO' if not on_common_line else 'YES'}_"
                 f"mean_dist_ghost52={mean_dist_ghost:.4f}_"
                 f"ghost_trend_slope={ghost_trend_slope:+.4e}_"
                 f"lowImg_meandist={low_band_mean:.4f}_highImg_meandist={high_band_mean:.4f}_"
                 f"powerlaw_exp={plaw_exp:.4f}_riemann_ratio_top={riemann_ratio_top:.4f}_"
                 f"maxwind_resid={max(panel_nonint) if panel_nonint else 0.0:.2e}_"
                 f"closedform_resid={mp.nstr(worst_resid,3)}")

    # 8. Plot
    fig, ax = plt.subplots(1, 3, figsize=(18.5, 5.8))

    # (a) zero map in the (Re, Im) plane with the Re=5/2 ghost line
    a0 = ax[0]
    a0.axvline(2.5, color='tab:purple', lw=1.4, ls='--',
               label=r'Re $s = 5/2$ (ghost of $\zeta(s-2)$ mirror)')
    a0.axvline(0.5, color='0.6', lw=1.0, ls=':', label=r'Re $s = 1/2$ (arithmetic line, ref)')
    if reF:
        sc = a0.scatter(reF, imF, c=imF, cmap='viridis', s=46, marker='x')
        a0.scatter([re_median], [np.mean(imF)], s=120, facecolors='none',
                   edgecolors='tab:red', marker='o', label=f'Re median = {re_median:.3f}')
    for (_, _, ylo, _yhi) in panel_bounds:
        a0.axhline(ylo, color='0.85', lw=0.8)
    a0.set_xlabel('Re s'); a0.set_ylabel('Im s')
    a0.set_title('S$^3$ Dirac zeta F(s): certified zero map\nIm $\\in$ [36, 300] (no Euler product)')
    a0.legend(loc='upper left', fontsize=8); a0.grid(alpha=0.25)

    # (b) Re-distribution histogram
    a1 = ax[1]
    if reF:
        a1.hist(reF, bins=max(6, int(np.sqrt(n_zeros)) + 2), color='tab:red', alpha=0.7,
                edgecolor='k', orientation='vertical')
        a1.axvline(2.5, color='tab:purple', lw=1.6, ls='--', label='Re = 5/2 ghost')
        a1.axvline(re_median, color='tab:blue', lw=1.4, label=f'median = {re_median:.3f}')
        a1.axvline(re_mean, color='tab:green', lw=1.2, ls=':', label=f'mean = {re_mean:.3f}')
    a1.set_xlabel('Re s'); a1.set_ylabel('count')
    a1.set_title(f'Re-distribution of {n_zeros} certified zeros\n'
                 f'spread = {re_spread:.3f}, on common line: {"NO" if not on_common_line else "YES"}')
    a1.legend(fontsize=8); a1.grid(alpha=0.25)

    # (c) density fit N(T) vs (T/2pi) log(T/2pi e)
    a2 = ax[2]
    if Tsorted.size:
        a2.plot(Tsorted, Ncum, 'o-', c='tab:red', ms=4, lw=1.3,
                label=f'measured N(T) (count={int(Ncum[-1])})')
        Tgrid = np.linspace(float(PANELS[0][0]), float(Tsorted[-1]), 200)  # (local)
        Nrg = riemann_log_count(Tgrid) - riemann_log_count(np.array([float(PANELS[0][0])]))[0]  # (local)
        a2.plot(Tgrid, Nrg, c='tab:blue', lw=1.6,
                label=r'$(T/2\pi)\log(T/2\pi e)$ windowed')
        a2.plot(Tgrid, plaw_amp * np.power(Tgrid, plaw_exp), c='tab:orange', lw=1.2, ls='--',
                label=fr'free power law $T^{{{plaw_exp:.2f}}}$')
    a2.set_xlabel('T = Im s'); a2.set_ylabel('cumulative zero count N(T)')
    a2.set_title('Zero-density fit\n(Weyl polynomial growth vs $T\\log T$ arithmetic)')
    a2.legend(fontsize=8); a2.grid(alpha=0.25)

    fig.suptitle('S105-W7-6 — S$^3$ Dirac zeta asymptotic zero census (Im $\\in$ [36, 300]): '
                 'mirror-without-pin scatter (INFO-by-construction)', fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=150)
    print(f'\nplot -> {OUT_PNG}')

    # 9. Save data
    np.savez(
        OUT_NPZ,
        zeros_re=np.asarray(reF, dtype=float),
        zeros_im=np.asarray(imF, dtype=float),
        zeros_complex=np.asarray([complex(r) for r in all_zeros]),
        panel_counts=np.asarray(panel_counts, dtype=int),
        panel_nonint_resid=np.asarray(panel_nonint, dtype=float),
        panel_bounds=np.asarray(panel_bounds, dtype=float) if panel_bounds else np.zeros((0, 4)),
        re_spread=re_spread, re_median=re_median, re_mean=re_mean,
        on_common_line=on_common_line,
        mean_dist_ghost52=mean_dist_ghost,
        ghost_trend_slope=ghost_trend_slope,
        low_height_mean_dist=low_band_mean, high_height_mean_dist=high_band_mean,
        powerlaw_exp=plaw_exp, powerlaw_amp=plaw_amp,
        riemann_ratio_top=riemann_ratio_top,
        T_sorted=Tsorted, N_cumulative=Ncum,
        N_riemann_windowed=N_riemann_windowed,
        re_ghost_line=float(RE_GHOST),
        worst_closedform_resid=float(worst_resid),
        machinery_fail=machinery_fail,
        re_window=np.asarray([float(RE_LO), float(RE_HI)], dtype=float),
        im_window=np.asarray([36.0, 300.0], dtype=float),
    )
    print(f'data -> {OUT_NPZ}   ({time.time() - t0:.0f}s total)')

    # 10. 4-tuple + verdict payload
    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    # composite-precedence companion row (MANDATORY per plan + gate-verdicts.md
    # §"Plan-frozen gate-block operator precedence").
    composite_row = ("# composite-precedence: §W7-6 (generic schema-v2 collapse overridden "
                     "— INFO-by-construction; FAIL only on non-integer winding after refinement)")  # (local)
    census_row = (f"# census: {n_zeros} certified zeros Im in [36,300]; panel_counts={panel_counts}; "
                  f"Re_spread={re_spread:.4f} on_common_line={'NO' if not on_common_line else 'YES'}; "
                  f"mean|Re-5/2|={mean_dist_ghost:.4f}; ghost_trend_slope={ghost_trend_slope:+.3e}; "
                  f"closes off-session caveat #5 (window-finite certification, Im<=36.13 -> Im<=300)")  # (local)
    convention_row = ("# convention: single-power Conv. B poleconv-B-single; "
                      "F(s)=(2^{s-2}-1)zeta(s-2)-(2^{s-2}-1/4)zeta(s); "
                      "Re=5/2 = shifted-mirror ghost of zeta(s-2) [Re(s-2)=1/2]; "
                      "poles s=3,s=1 on real axis (P=0 in every Im>=36 panel); "
                      "NO regulator_pin (exact closed form), NO CLASS pin (no SCHEMATIC helper)")  # (local)

    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        extra_rows=[composite_row, census_row, convention_row],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
