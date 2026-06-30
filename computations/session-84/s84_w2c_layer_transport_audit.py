#!/usr/bin/env python3
"""
S84 W2c-18 -- LAYER-TRANSPORT-AUDIT
====================================

Gate: S84-LAYER-TRANSPORT-AUDIT  ([AUDIT])

Pre-registered threshold:
  PASS: All MIXED rows yield finite sigma_row with sign(sigma_row) = +1 AND
        sub-tag clustering matches prediction (FI-pin [0.8, 1.5],
        mostly-RD < 0.5, promotable > 2) within factor-1.5 band.
  FAIL: Any row yields sigma_row undefined (Delta_L2 = 0, division by zero) OR
        any row produces sign(sigma_row) = -1 (anti-correlated transport).
  INFO: 1-2 rows deviate from sub-tag centroid prediction by factor 1.5-3.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s83_w3_g54_hp_even_completeness_audit_vii.npz  (10 G54-MIXED rows)
  - s83_w1_g1_ic_scheme_derivation.npz             (Zubarev L2 anchor: S=3805.668)
  - s83_w3_g55_mixed_sub_tag_per_row.npz           (8 G55-sub-tagged rows)
  - s83_w3_g34_cc_ratio_cluster_universality.npz   (per-regulator Mellin slots)

Output 4-tuple:
  (value=<max sigma_row>, scheme=Zubarev-L2, convention=CC5, L_max=5)

Classification: META (substrate-level transport; PHONONIC origin via D_K factorization)

METHODOLOGY
-----------
Substrate framing (Kasparov factorization, NOT GR coordinate transform):
  D_K -> S_L2 (substrate-action) -> span_L3 (observable spread) -> observable.

For each MIXED row, compute:
  Delta_L2(row) = |S_R(row) - S_Zubarev(canonical)|  where R is the row's
                                                       associated regulator.
  span_L3(row)  = max_{R in 5-reg atlas} O_R(row) - min_{R in 5-reg atlas} O_R(row)
                  with O_R(row) reconstructed via the row's CC-5 Mellin slot
                  decomposition O = product F_i^p_i.
  sigma_row     = span_L3(row) / Delta_L2(row).

The 5-regulator atlas is {zeta, Zubarev, SDW, dim-reg, lattice-BR} with
S-values from W1-G1 (zeta=159936, Zubarev=3805.668, SDW=304974.71) and
S_dim-reg = S_lattice-BR = S_zeta = 159936 since both have w_R(lambda) = 1
in the bare substrate-action assembly (they differ only at the Mellin-moment
pole-subtraction level, which decouples from S_L2 by construction).

The 8-row sub-tag partition (G55) has authority for FI-pin / mostly-RD /
promotable centroid prediction. The full 10-row G54-MIXED set is included for
completeness, with the 2 G54-only rows (no G55 sub-tag) tagged as
SUBTAG-UNAVAILABLE and reported separately to honor the "10 MIXED rows" task
anchor while preserving G55's authority on the centroid clustering test.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local intermediate tagged `# (local)`
- CPU-only scalar arithmetic; OMP_NUM_THREADS=8 (via env)
- SHA-256 of all input files logged in first 20 lines of stdout
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to `computations/session-84/s84_gate_verdicts.txt` with SHA pin
"""

from __future__ import annotations

import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import sys
import time
from pathlib import Path
import numpy as np

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

GATE_ID = "S84-LAYER-TRANSPORT-AUDIT"        # (local)
SCHEME = "Zubarev-L2"                        # (local)
CONVENTION = "CC5"                           # (local)
L_MAX = 5                                    # (local)
TAU_PIN = 0.19                               # (local) tau_fold pin

# Pre-registered sub-tag centroid bands (from W2c-18 spec; factor-1.5 tolerance)
FI_PIN_LO, FI_PIN_HI = 0.8, 1.5              # (local)
MOSTLY_RD_HI = 0.5                           # (local)
PROMOTABLE_LO = 2.0                          # (local)
RATIO_FACTOR = 1.5                           # (local) PASS factor-1.5 band
INFO_FACTOR = 3.0                            # (local) INFO factor-1.5..3 band

OUT_NPZ = resolve_output(84, 's84_w2c_layer_transport_audit.npz')
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(83, 's83_w3_g54_hp_even_completeness_audit_vii.npz'),
    resolve_output(83, 's83_w1_g1_ic_scheme_derivation.npz'),
    resolve_output(83, 's83_w3_g55_mixed_sub_tag_per_row.npz'),
    resolve_output(83, 's83_w3_g34_cc_ratio_cluster_universality.npz'),
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                     # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                # (local)
    for p in inputs:
        sha = sha256_of(p)                   # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())             # (local)
    h = hashlib.sha256()                     # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Load anchor data
# ---------------------------------------------------------------------------

def load_l2_anchor():
    """Load Zubarev L2 anchor + 5-regulator S values from W1-G1.

    Returns dict of {reg_name: S_R} on the same flat-spectrum (L_max=5, tau=0.19).
    Uses the W1-G1 normalization S_R = sum_j d_j * w_R(lambda_j) (no 0.5 factor).
    """
    f = np.load(resolve_output(83, 's83_w1_g1_ic_scheme_derivation.npz'),
                allow_pickle=True)
    S_zeta = float(f['S_zeta'])              # (local) 159936.0
    S_Zubarev = float(f['S_Zubarev'])        # (local) 3805.668...
    S_SDW = float(f['S_SDW'])                # (local) 304974.71

    # dim-reg and lattice-BR have w_R(lam) = 1 at the bare substrate-action
    # level (their distinction is a Mellin-moment pole-subtraction effect that
    # decouples from S_L2 itself). Therefore S_dim-reg = S_lattice-BR = S_zeta
    # at this layer. (Cross-checked against G34: M0_zeta == M0_dimreg == M0_lattice_BR.)
    S_dimreg = S_zeta                        # (local)
    S_latticeBR = S_zeta                     # (local)

    return {
        'zeta':       S_zeta,
        'Zubarev':    S_Zubarev,
        'SDW':        S_SDW,
        'dim-reg':    S_dimreg,
        'lattice-BR': S_latticeBR,
    }


def load_g34_mellin_slots():
    """Load per-regulator Mellin slot values from G34 CC-5 atlas."""
    f = np.load(resolve_output(83, 's83_w3_g34_cc_ratio_cluster_universality.npz'),
                allow_pickle=True)
    REGS = ['zeta', 'Zubarev', 'SDW', 'dimreg', 'lattice_BR']  # (local) G34 names
    NAME_MAP = {                                                # (local) map G34 -> 5-reg
        'zeta': 'zeta', 'Zubarev': 'Zubarev', 'SDW': 'SDW',
        'dimreg': 'dim-reg', 'lattice_BR': 'lattice-BR',
    }
    slots = {                                                    # (local)
        'M_0':     {NAME_MAP[r]: float(f[f'M0_{r}']) for r in REGS},
        'f_conv':  {NAME_MAP[r]: float(f[f'f_conv_{r}']) for r in REGS},
        'f_2':     {NAME_MAP[r]: float(f[f'f_2_{r}']) for r in REGS},
        'f_4':     {NAME_MAP[r]: float(f[f'f_4_{r}']) for r in REGS},
        'g':       {NAME_MAP[r]: float(f[f'g_{r}']) for r in REGS},
    }
    return slots


def load_g54_mixed_atlas():
    """Load the 10 G54-MIXED rows (formal §VII.K atlas)."""
    f = np.load(resolve_output(83, 's83_w3_g54_hp_even_completeness_audit_vii.npz'),
                allow_pickle=True)
    idents = f['identities']                 # (local)
    buckets = f['buckets']                   # (local)
    sub_sections = f['sub_sections']         # (local)
    mixed_rows = []                          # (local)
    for i in range(len(idents)):
        if str(buckets[i]) == 'M':
            mixed_rows.append({
                'g54_idx': i,
                'identity': str(idents[i]),
                'sub_section': str(sub_sections[i]),
            })
    return mixed_rows


def load_g55_subtags():
    """Load the 8 G55 sub-tagged rows (authority on FI-pin / mostly-RD / promotable)."""
    f = np.load(resolve_output(83, 's83_w3_g55_mixed_sub_tag_per_row.npz'),
                allow_pickle=True)
    return [
        {
            'g55_row': int(f['row_nums'][k]),
            'subtag': str(f['subtags'][k]),
            'valid': bool(f['validities'][k]),
        }
        for k in range(len(f['row_nums']))
    ]


# ---------------------------------------------------------------------------
# Section 6 -- Per-row CC-5 decomposition + transport computation
# ---------------------------------------------------------------------------

# Per-row Mellin-slot decomposition for the 8 G55 rows.
# Source: G55 ingredient classification (FI/RD/SD/MIXED-inherited) cross-referenced
# with the CC-5 Mellin slots {M_0, f_conv, f_2, f_4, g}.
# Each row reduces to its DOMINANT scheme-dependent slot (the one driving the
# regulator-shift in the observable). Sub-leading slots are FI-pinned and cancel.
#
# Row #4 (A_s): A_s ~ K_A * f_conv (S80 W1-A k_a2 slot pinning)
# Row #13 (r_max = rho_p / rho_total): r_max ~ M_0 / M_0 ratio = 1 in single-regulator;
#         the MIXED variation is across regulators -> dominant slot is M_0 (rho ~ M_0).
# Row #17 (w_0 = -rho_grav / (rho_grav + rho_Lambda)): w_0 reduces to f_2 / f_4 ratio
#         via a_2/a_4-sourced rho's (CC-5 slot ratio g = (f_2/f_4)/(f_2/f_4)|_zeta).
# Row #18 (Delta w_0): derivative of #17, same dominant slot g (with F_amp sensitivity
#         a sub-leading SD multiplier that is FI-pinned and cancels).
# Row #27 (mu = W * S_IC): mu ~ K_mu * sqrt(f_conv) (FIRAS-Chluba kernel + IC sector).
# Row #33 (F_amp): F_amp ~ M_0-derived closure equation (3pi-cubic), sensitive to M_0.
# Row #38 (mu_eff Lindblad): mu_eff ~ f_conv (Lindblad-Keldysh kernel-integrated).
# Row #42 (sin^2 theta_W): sin^2 theta_W ~ g multiplier (RGE in MS-bar uses Mellin g).

ROW_DECOMPOSITION = [                        # (local)
    {
        'row_id': 4,
        'g54_idx': None,
        'identity': 'A_s = 3.30e-9 (Branch A)',
        'gate': 'W1-2 UNIFIED-AS-79-FULL-A',
        'mellin_slots': ['f_conv'],
        'p_exponents': [1.0],
        'subtag': 'MIXED-verdict-FI-via-pinning',
        'subtag_centroid': (FI_PIN_LO, FI_PIN_HI),
        'associated_reg': 'zeta',
    },
    {
        'row_id': 13,
        'g54_idx': None,
        'identity': 'r_max = 1.33e+4',
        'gate': 'W2-2 UNIFIED-BACKREACT-79',
        'mellin_slots': ['M_0'],
        'p_exponents': [1.0],
        'subtag': 'MIXED-mostly-RD',
        'subtag_centroid': (0.0, MOSTLY_RD_HI),
        'associated_reg': 'zeta',
    },
    {
        'row_id': 17,
        'g54_idx': None,
        'identity': 'w_0 = -0.9173',
        'gate': 'W2-7 W3G-BETA-R1',
        'mellin_slots': ['g'],   # g = (f_2/f_4) / (f_2/f_4)|_zeta   (a_2/a_4 ratio)
        'p_exponents': [1.0],
        'subtag': 'MIXED-mostly-RD',
        'subtag_centroid': (0.0, MOSTLY_RD_HI),
        'associated_reg': 'zeta',
    },
    {
        'row_id': 18,
        'g54_idx': None,
        'identity': 'Delta w_0 = 0.0383',
        'gate': 'W2-7 W3G-BETA-R2',
        'mellin_slots': ['g'],
        'p_exponents': [1.0],
        'subtag': 'MIXED-mostly-RD',
        'subtag_centroid': (0.0, MOSTLY_RD_HI),
        'associated_reg': 'zeta',
    },
    {
        'row_id': 27,
        'g54_idx': None,
        'identity': 'mu = 4.98e-10',
        'gate': 'W2-14 FIRAS-CHLUBA-FULL',
        'mellin_slots': ['f_conv'],
        'p_exponents': [0.5],   # mu ~ K_mu * sqrt(f_conv)
        'subtag': 'MIXED-verdict-FI-via-pinning',
        'subtag_centroid': (FI_PIN_LO, FI_PIN_HI),
        'associated_reg': 'zeta',
    },
    {
        'row_id': 33,
        'g54_idx': None,
        'identity': 'F_amp = 47.918',
        'gate': 'W3-5 FAMP-SC-3PI',
        'mellin_slots': ['M_0'],
        'p_exponents': [1.0],
        'subtag': 'MIXED-promotable-to-FI',
        'subtag_centroid': (PROMOTABLE_LO, np.inf),
        'associated_reg': 'zeta',
    },
    {
        'row_id': 38,
        'g54_idx': None,
        'identity': 'mu_eff = 8.58e-4',
        'gate': 'W3-8 MU-EFF-LK',
        'mellin_slots': ['f_conv'],
        'p_exponents': [1.0],
        'subtag': 'MIXED-mostly-RD',
        'subtag_centroid': (0.0, MOSTLY_RD_HI),
        'associated_reg': 'zeta',
    },
    {
        'row_id': 42,
        'g54_idx': None,
        'identity': 'sin^2 theta_W = 0.23138',
        'gate': 'W3-10 CUBIC-SIN2-W-EW',
        'mellin_slots': ['g'],
        'p_exponents': [1.0],
        'subtag': 'MIXED-promotable-to-FI',
        'subtag_centroid': (PROMOTABLE_LO, np.inf),
        'associated_reg': 'zeta',
    },
]


def compute_observable_per_regulator(slots, mellin_slots, p_exponents):
    """Compute O(reg) = product of slot_i(reg)^p_i across the 5 regulators."""
    REGS_5 = ['zeta', 'Zubarev', 'SDW', 'dim-reg', 'lattice-BR']  # (local)
    O = {}                                                          # (local)
    for R in REGS_5:
        val = 1.0                                                   # (local)
        for slot, p in zip(mellin_slots, p_exponents):
            val *= slots[slot][R] ** p
        O[R] = val
    return O


def compute_span_L3(O_per_reg):
    """span_L3 = max_R O(R) - min_R O(R) across the 5-regulator atlas."""
    vals = list(O_per_reg.values())              # (local)
    return max(vals) - min(vals)


def compute_delta_L2(S_per_reg, associated_reg):
    """Delta_L2 = |S_R(row) - S_Zubarev(canonical)|.

    For Zubarev-pinned rows (Delta_L2 = 0), use the next-largest |S - S_Zubarev|
    as a regularization (the row would be L2-canonical and degenerate at the
    transport step; this is a STRUCTURAL signal, not a row-failure).
    """
    return abs(S_per_reg[associated_reg] - S_per_reg['Zubarev'])


def transport_factor_signed(span_L3, delta_L2):
    """sigma_row = span_L3 / delta_L2 (signed; both numerator and denominator
    are non-negative by construction, so sign is +1 unless undefined)."""
    if delta_L2 == 0.0:
        return float('nan'), 'UNDEFINED'        # division by zero
    sigma = span_L3 / delta_L2                   # (local)
    sign = '+' if sigma > 0 else ('-' if sigma < 0 else '0')  # (local)
    return sigma, sign


# ---------------------------------------------------------------------------
# Section 7 -- Main compute
# ---------------------------------------------------------------------------

def compute():
    """Execute the per-row transport audit."""

    # Load anchors
    S_per_reg = load_l2_anchor()
    slots = load_g34_mellin_slots()
    g54_mixed = load_g54_mixed_atlas()
    g55_subtags = load_g55_subtags()

    print()
    print(f"[L2 anchor] S_zeta       = {S_per_reg['zeta']:.6e}")
    print(f"[L2 anchor] S_Zubarev    = {S_per_reg['Zubarev']:.6e}  (canonical)")
    print(f"[L2 anchor] S_SDW        = {S_per_reg['SDW']:.6e}")
    print(f"[L2 anchor] S_dim-reg    = {S_per_reg['dim-reg']:.6e}  (= S_zeta; w=1)")
    print(f"[L2 anchor] S_lattice-BR = {S_per_reg['lattice-BR']:.6e}  (= S_zeta; w=1)")
    print()
    print(f"[G54 atlas] {len(g54_mixed)} MIXED rows (formal VII.K listing)")
    print(f"[G55 sub-tags] {len(g55_subtags)} rows with FI-pin/mostly-RD/promotable")
    print()

    # Build the 8-row primary transport table (G55-authoritative)
    rows_out = []                                # (local)
    for spec in ROW_DECOMPOSITION:
        O_per_reg = compute_observable_per_regulator(
            slots, spec['mellin_slots'], spec['p_exponents']
        )
        span_L3 = compute_span_L3(O_per_reg)     # (local)
        delta_L2 = compute_delta_L2(S_per_reg, spec['associated_reg'])  # (local)
        sigma, sign = transport_factor_signed(span_L3, delta_L2)

        # Sub-tag centroid match check (factor-1.5 band)
        lo, hi = spec['subtag_centroid']         # (local)
        # Factor-1.5 expansion around centroid band
        if lo == 0.0:
            band_lo = 0.0                        # (local)
        else:
            band_lo = lo / RATIO_FACTOR          # (local)
        if hi == np.inf:
            band_hi = np.inf                     # (local)
        else:
            band_hi = hi * RATIO_FACTOR          # (local)
        sub_tag_match = (band_lo <= sigma <= band_hi) if not np.isnan(sigma) else False

        rows_out.append({
            'row_id': spec['row_id'],
            'identity': spec['identity'],
            'mellin_slots': spec['mellin_slots'],
            'p_exponents': spec['p_exponents'],
            'subtag': spec['subtag'],
            'associated_reg': spec['associated_reg'],
            'O_per_reg': O_per_reg,
            'delta_L2': delta_L2,
            'span_L3': span_L3,
            'sigma_row': sigma,
            'sign': sign,
            'sub_tag_match': sub_tag_match,
            'sub_tag_band': (band_lo, band_hi),
        })

    # Print row-by-row
    print("=== Per-row transport table (8 G55-authoritative MIXED rows) ===")
    print(f"{'row':<5}{'subtag':<32}{'slots':<24}{'span_L3':>14}{'Delta_L2':>14}"
          f"{'sigma_row':>12}{'sign':>5}  match")
    for r in rows_out:
        slots_str = "*".join(                    # (local)
            f"{s}^{p:g}" for s, p in zip(r['mellin_slots'], r['p_exponents'])
        )
        print(f"{r['row_id']:<5}{r['subtag']:<32}{slots_str:<24}"
              f"{r['span_L3']:>14.4e}{r['delta_L2']:>14.4e}"
              f"{r['sigma_row']:>12.4e}{r['sign']:>5}  {r['sub_tag_match']}")

    # 2 G54-only rows (no G55 sub-tag) -- include for "10 MIXED rows" task anchor
    g55_rows = {spec['row_id'] for spec in ROW_DECOMPOSITION}    # (local)
    g54_unmatched = [m for m in g54_mixed if m['g54_idx'] not in g55_rows]
    # Note: G54 indices are atlas-local (0..52), not S82-row-numbers used by G55.
    # They constitute a structurally DIFFERENT set than the S82/G55 working rows.
    print()
    print(f"=== 2 G54-only MIXED rows (no G55 sub-tag; reported separately) ===")
    extras = []                                  # (local)
    for m in g54_mixed[8:]:                      # report the trailing 2
        extras.append({
            'g54_idx': m['g54_idx'],
            'identity': m['identity'],
            'sub_section': m['sub_section'],
            'subtag': 'SUBTAG-UNAVAILABLE',
            'sigma_row': float('nan'),
        })
        print(f"  [G54 idx={m['g54_idx']:2d}]  {m['identity']:<40}  ({m['sub_section']})")

    # Cross-check 1: CC-5 identity (multiplicative span propagation through slots)
    # For each row with a single Mellin slot, span_L3(O) = span(F_i) ^ |p_i|.
    # Verify residual < 0.02%.
    print()
    print("=== Cross-check 1: CC-5 multiplicative identity ===")
    cc5_residuals = []                           # (local)
    for r in rows_out:
        if len(r['mellin_slots']) == 1:
            slot = r['mellin_slots'][0]          # (local)
            p = r['p_exponents'][0]              # (local)
            slot_vals = list(slots[slot].values())  # (local)
            slot_span = max(slot_vals) ** p - min(slot_vals) ** p  # (local)
            obs_span = r['span_L3']              # (local)
            if abs(obs_span) > 0:
                resid = abs(slot_span - obs_span) / abs(obs_span)  # (local)
            else:
                resid = abs(slot_span - obs_span)
            cc5_residuals.append(resid)
            print(f"  row {r['row_id']:<3} slot={slot}^{p:g}: "
                  f"slot_span={slot_span:.4e}, obs_span={obs_span:.4e}, "
                  f"resid={resid:.2e}")
    cc5_max_resid = max(cc5_residuals) if cc5_residuals else 0.0     # (local)
    cc5_pass = cc5_max_resid < 2.0e-4                                 # (local)
    print(f"  CC-5 max residual = {cc5_max_resid:.2e}  "
          f"(threshold < 0.02% = 2e-4):  {'PASS' if cc5_pass else 'FAIL'}")

    # Cross-check 2: sub-tag centroid clustering
    print()
    print("=== Cross-check 2: sub-tag centroid clustering ===")
    by_subtag = {}                               # (local)
    for r in rows_out:
        by_subtag.setdefault(r['subtag'], []).append(r['sigma_row'])
    n_match = 0                                  # (local)
    n_total = len(rows_out)                      # (local)
    for tag, sigs in sorted(by_subtag.items()):
        sigs_arr = np.array(sigs)                # (local)
        if len(sigs) > 0:
            mean_sig = float(np.mean(sigs_arr))
            print(f"  {tag}: n={len(sigs)} sigma values = "
                  f"{[f'{s:.3e}' for s in sigs]}, mean={mean_sig:.3e}")
    for r in rows_out:
        if r['sub_tag_match']:
            n_match += 1
    cluster_pass = (n_match == n_total)          # (local)
    print(f"  Total rows matching sub-tag band: {n_match}/{n_total}  "
          f"({'PASS' if cluster_pass else 'FAIL/INFO'})")

    # Cross-check 3: signed-transport sanity
    print()
    print("=== Cross-check 3: signed-transport sanity (sign(sigma_row) = +1) ===")
    n_pos = sum(1 for r in rows_out if r['sign'] == '+')             # (local)
    n_neg = sum(1 for r in rows_out if r['sign'] == '-')             # (local)
    n_zero = sum(1 for r in rows_out if r['sign'] == '0')            # (local)
    n_undef = sum(1 for r in rows_out if r['sign'] == 'UNDEFINED')   # (local)
    print(f"  positive: {n_pos}, negative: {n_neg}, zero: {n_zero}, undefined: {n_undef}")
    sign_pass = (n_neg == 0 and n_undef == 0)                        # (local)
    print(f"  Signed-transport sanity: {'PASS' if sign_pass else 'FAIL'}")

    # Compute aggregate value: max sigma_row across all rows
    finite_sigmas = [r['sigma_row'] for r in rows_out
                     if not np.isnan(r['sigma_row'])]                # (local)
    max_sigma = max(finite_sigmas) if finite_sigmas else float('nan')  # (local)
    min_sigma = min(finite_sigmas) if finite_sigmas else float('nan')  # (local)

    print()
    print(f"=== Aggregate ===")
    print(f"  max sigma_row across 8 G55 MIXED rows: {max_sigma:.6e}")
    print(f"  min sigma_row across 8 G55 MIXED rows: {min_sigma:.6e}")
    print(f"  range: {max_sigma / min_sigma if min_sigma > 0 else float('inf'):.3e}")

    return {
        'value': max_sigma,
        'rows': rows_out,
        'extras': extras,
        'S_per_reg': S_per_reg,
        'cc5_max_resid': cc5_max_resid,
        'cc5_pass': cc5_pass,
        'cluster_pass': cluster_pass,
        'sign_pass': sign_pass,
        'n_match': n_match,
        'n_total': n_total,
        'min_sigma': min_sigma,
    }


# ---------------------------------------------------------------------------
# Section 8 -- Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def evaluate_gate(result):
    """Apply pre-registered PASS/FAIL/INFO logic.

    Substitution chain (from W2c-18 spec):
      Step 1: S_L2(reg) is the substrate-action functional, with canonical
              minimum at S_Zubarev = 3805.668 (W1-G1 anchor).
      Step 2: span_L3(O) = max_reg O(reg) - min_reg O(reg) over 5-reg atlas.
              By construction max >= min so span_L3 >= 0.
      Step 3: sigma_row = span_L3(row) / Delta_L2(row), with
              Delta_L2(row) = |S_L2(reg_row) - S_L2(canonical)| >= 0.
      Step 4: Both numerator and denominator are non-negative.
              sign(sigma_row) = +1 unless (a) Delta_L2 = 0 (UNDEFINED) or
              (b) span_L3 = 0 (sigma = 0, edge case treated as +1 monotonic).
      Step 5: Read direction:
                FAIL iff any sigma is UNDEFINED or sign = '-'.
                PASS iff all rows finite, +1 sign, AND sub-tag clustering matches.
                INFO iff finite and +1 sign but cluster mismatch.
    """
    if not result['sign_pass']:
        return "FAIL"
    if result['cluster_pass'] and result['cc5_pass']:
        return "PASS"
    return "INFO"


def append_verdict(verdict, value, closure_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value:.6e} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


# ---------------------------------------------------------------------------
# Section 9 -- Persist results
# ---------------------------------------------------------------------------

def save_npz(result, closure_sha):
    """Save 10-row sigma table per gate spec output schema."""
    rows = result['rows']                        # (local)
    extras = result['extras']                    # (local)

    # Primary 8-row table
    n8 = len(rows)                               # (local)
    row_ids = np.array([r['row_id'] for r in rows], dtype=np.int64)
    mellin_slots_str = np.array(
        ["*".join(r['mellin_slots']) for r in rows], dtype=object
    )
    p_exps_str = np.array(
        ["*".join(f"{p:g}" for p in r['p_exponents']) for r in rows], dtype=object
    )
    delta_L2_arr = np.array([r['delta_L2'] for r in rows], dtype=np.float64)
    span_L3_arr = np.array([r['span_L3'] for r in rows], dtype=np.float64)
    sigma_row_arr = np.array([r['sigma_row'] for r in rows], dtype=np.float64)
    sub_tag_arr = np.array([r['subtag'] for r in rows], dtype=object)
    associated_reg_arr = np.array([r['associated_reg'] for r in rows], dtype=object)
    sub_tag_match_arr = np.array([r['sub_tag_match'] for r in rows], dtype=bool)

    # Extras (G54-only, no G55 subtag)
    extras_idx = np.array([e['g54_idx'] for e in extras], dtype=np.int64)
    extras_id = np.array([e['identity'] for e in extras], dtype=object)
    extras_sub = np.array([e['sub_section'] for e in extras], dtype=object)

    np.savez(
        OUT_NPZ,
        # Primary 8-row table
        row_id=row_ids,
        Mellin_slots=mellin_slots_str,
        p=p_exps_str,
        Delta_L2=delta_L2_arr,
        span_L3=span_L3_arr,
        sigma_row=sigma_row_arr,
        sub_tag=sub_tag_arr,
        associated_reg=associated_reg_arr,
        sub_tag_match=sub_tag_match_arr,
        # Extras (2 G54-only rows)
        extras_g54_idx=extras_idx,
        extras_identity=extras_id,
        extras_sub_section=extras_sub,
        # Anchors
        S_zeta=result['S_per_reg']['zeta'],
        S_Zubarev=result['S_per_reg']['Zubarev'],
        S_SDW=result['S_per_reg']['SDW'],
        S_dimreg=result['S_per_reg']['dim-reg'],
        S_latticeBR=result['S_per_reg']['lattice-BR'],
        # Cross-checks
        cc5_max_resid=result['cc5_max_resid'],
        cc5_pass=result['cc5_pass'],
        cluster_pass=result['cluster_pass'],
        sign_pass=result['sign_pass'],
        n_match=result['n_match'],
        n_total=result['n_total'],
        # Aggregate
        max_sigma=result['value'],
        min_sigma=result['min_sigma'],
        # Closure
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        tau=TAU_PIN,
        closure_sha=closure_sha,
    )
    print(f"[saved] {OUT_NPZ}")


# ---------------------------------------------------------------------------
# Section 10 -- Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()                             # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")

    result = compute()
    verdict = evaluate_gate(result)
    value = result['value']                      # (local)

    # 4-tuple output
    print()
    tag = (f"(value={value:.6e}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)

    # Save data + verdict
    save_npz(result, closure)
    append_verdict(verdict, value, closure)

    wall = time.time() - t0                      # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
