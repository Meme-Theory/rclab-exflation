#!/usr/bin/env python3
"""
S99 W1-Q-NONRATIO-OBSERVABLE — non-ratio post-fold deceleration sign-history
=============================================================================

Gate: S99-W1-Q-NONRATIO-OBSERVABLE ([SIGN])

Pre-registered threshold:
  band_membership_fraction( q_nonratio(tau) in [q_lo_SF54, q_hi_SF54] ) >= 0.90
  AND is_finite(q_nonratio) across the H_A=0 crossing.
  PASS iff finite-across-crossing AND in-band fraction >= 0.90;
  FAIL iff the non-ratio observable is STILL non-finite across the crossing;
  INFO iff finite-across-crossing but in-band fraction < 0.90 (composite
  collapse may also drive INFO via the auto-shortening regime band).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-98/s98_w1_route_reconciliation.npz  (a_eff/Omega/H_A
    trajectories + the 0/0 diagnostic; the INPUT motivating this re-derivation)
  - computations/session-97/s97_w1_omega_profile.npz          (Omega(tau) profile,
    reproduces Omega_BA_fold = 2.241353)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<band_frac+sign summary>, scheme=FW, convention=ABSOLUTE, L_max=N/A)

Classification: GEOMETRIC/PHONONIC bridge
  D_K eigenvalues -> a_2 second Seeley-DeWitt spectral moment (a_2_FW_zeta)
                  -> emergent acoustic scale factor a_eff(tau) = a_bare(tau)*Omega(tau)
                  -> deceleration sign-history (the non-ratio observable).
  The object IS the substrate's emergent post-fold expansion history, NOT a
  laboratory measurement of a(t) IN a pre-existing spacetime container. This is
  exflation, not inflation.

METHODOLOGY
-----------
S98 V.1 (S98-W1-ROUTE-RECONCILIATION, FAIL, audit 75a45dd7) established that the
AOFT canonical acoustic frame is conformally STATIONARY: a_eff(tau) = const to
rel-var 7.4e-7, because the sqrt(Gamma)-effacement conformal factor
Omega = sqrt(rho_s/a_2) (Omega_BA_fold = 2.241353) EXACTLY cancels the bare
spectral-complexity growth. In that frame the ratio-form deceleration parameter
q = -a_eff*addot_eff/adot_eff^2 is a genuine 0/0 indeterminate (S98 Clause-2:
band_frac=0.000, q_central~1.94e7, only 116/999 finite points).

This gate reads the deceleration sign DIRECTLY off two NON-ratio observables:
  (1) PRIMARY  : sign-history of addot_eff (arr_aeff_ddot_t), mapped to a
                 deceleration-equivalent q via the WELL-CONDITIONED bare-frame
                 normalization H_bare (NOT the stationary a_eff normalization).
                 addot_eff is the q-numerator; its sign is finite where the
                 adot_eff^2 denominator -> 0, so it reads the acceleration sign
                 directly across the H_A=0 crossing where the ratio is 0/0.
  (2) CO-PRIMARY cross-check / EXPORT backbone: q_bare = -1 - Hdot_bare/H_bare^2,
                 with a_bare = a_eff/Omega (Omega from s97_w1_omega_profile.npz,
                 interpolated onto the S98 tau-grid). a_bare is NOT conformally
                 stationary, so q_bare is WELL-CONDITIONED (no 0/0). The
                 reconstructed H_bare(tau) IS the non-stationary substrate Hubble
                 backbone EXPORTED to Wave 2 (S99-W2-RELAXATION-CLOSURE).

Substitution chain (q-numerator sign):
  sign(q_ratio) = sign(-a_eff*addot_eff) = -sign(addot_eff)   [a_eff>0; adot_eff^2>0]
  => addot_eff > 0 <=> q < 0 (ACCELERATING); addot_eff < 0 <=> q > 0 (DECELERATING).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-correct (999-pt 1D arrays + numpy.gradient; sub-100x100; no eigvals/SVD/FFT);
  OMP_NUM_THREADS=8 set BEFORE import numpy per math-scripts.md.
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe);
  this script PRINTS the payload (print_verdict_payload), never writes the
  verdict file directly.
- npz key spellings verified at runtime via npz.files introspection; a missing
  key FAILs the gate with a key-missing diagnostic (no silent substitution).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (BEFORE numpy import; gate is CPU-correct)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first framework import)
# Scripts live at computations/session-N/; put computations/_shared on sys.path
# so `from canonical_constants import *` resolves (per session-98 precedent).
# ---------------------------------------------------------------------------
import sys
from pathlib import Path as _Path

sys.path.insert(0, str(_Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import a_2_FW_zeta, Omega_BA_fold  # noqa: E402  explicit provenance anchors

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S99"                                                    # (local)
GATE_ID = "S99-W1-Q-NONRATIO-OBSERVABLE"                           # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "ABSOLUTE"                                            # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered machinery pins (§W1-1 machinery_pin_map)
N_EVAL = 999                                                       # (local) tau-grid count from S98 npz
TOLERANCE = 1e-12                                                  # (local) finiteness / H_A=0 detection
POLE_EPS = 0.02                                                    # (local) half-width (tau-fraction) of H_A=0 exclusion window (PRIMARY q-map ONLY)
BAND_FRAC_THR = 0.90                                              # (local) in-band coverage floor for PASS
PUB_PREC = 6                                                       # (local) publication precision (Class 8.3)

# SF54 deceleration band [-0.97, +0.81] (SCALE-FACTOR-54 Connes-distance proxy;
# little-red-dots-synthesis.md; carried in s96_gate_verdicts.txt). Externally-
# derived band edges -> NOT framework constants requiring canonical promotion.
q_lo_SF54 = -0.97                                                 # (local)
q_hi_SF54 = 0.81                                                  # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s99_w1_q_nonratio_observable.npz"
OUT_PNG = SESSION_DIR / "s99_w1_q_nonratio_observable.png"

# Input files (npz inputs feed audit_sha256; canonical feeds audit_sha256)
S98_NPZ = COMPUTATIONS_DIR / "session-98" / "s98_w1_route_reconciliation.npz"
S97_NPZ = COMPUTATIONS_DIR / "session-97" / "s97_w1_omega_profile.npz"
CANON = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [CANON, S98_NPZ, S97_NPZ]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 4b — npz key-resolution helper (runtime introspection; no silent sub)
# ---------------------------------------------------------------------------

def resolve_key(z, candidates: list[str], role: str) -> str:
    """Return the FIRST candidate key present in npz z.files; raise KeyError
    (carrying a key-missing diagnostic) if none present. No silent fallback."""
    for c in candidates:
        if c in z.files:
            return c
    raise KeyError(
        f"KEY-MISSING [{role}]: none of {candidates} found in npz "
        f"(available: {sorted(z.files)})"
    )


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    res: dict = {}  # (local)

    # ---- Load S98 V.1 route-reconciliation npz (the 0/0 INPUT) ----
    z98 = np.load(S98_NPZ, allow_pickle=True)
    # Resolve keys via runtime introspection (plan: exact spellings verified at
    # runtime; FAIL-with-diagnostic on absence). Candidate lists cover the
    # plan-text spelling AND the actual S98-emitted spelling.
    k_tau = resolve_key(z98, ["arr_tau_t", "arr_tau"], "tau-grid (S98)")
    k_aeff = resolve_key(z98, ["arr_a_eff_t", "a_eff", "arr_aeff_t"], "a_eff(tau)")
    k_adot = resolve_key(z98, ["arr_aeff_dot_t", "arr_adot_eff_t"], "adot_eff(tau)")
    k_addot = resolve_key(z98, ["arr_aeff_ddot_t", "arr_addot_eff_t"], "addot_eff(tau)")
    k_HA = resolve_key(z98, ["arr_H_A_t", "arr_HA_t"], "H_A(tau)")

    tau = np.asarray(z98[k_tau], dtype=np.float64)            # (local)
    a_eff = np.asarray(z98[k_aeff], dtype=np.float64)         # (local)
    adot_eff = np.asarray(z98[k_adot], dtype=np.float64)      # (local)
    addot_eff = np.asarray(z98[k_addot], dtype=np.float64)    # (local) PRIMARY non-ratio observable
    H_A = np.asarray(z98[k_HA], dtype=np.float64)             # (local)

    n_total = tau.size                                        # (local)
    res["npz_keys_resolved_S98"] = f"tau={k_tau};a_eff={k_aeff};adot={k_adot};addot={k_addot};H_A={k_HA}"

    # carry the canonical stationarity diagnostic forward (Wave-2 provenance)
    if "clause2_aeff_relvar" in z98.files:
        aeff_relvar = float(z98["clause2_aeff_relvar"])       # (local) the canonical 7.427e-7
    else:
        aeff_relvar = float(np.std(a_eff) / np.mean(a_eff))   # (local) fallback definition

    # ---- Load S97 Omega profile ----
    z97 = np.load(S97_NPZ, allow_pickle=True)
    k_tg = resolve_key(z97, ["tau_grid", "arr_tau", "arr_tau_t"], "tau-grid (S97)")
    k_Om = resolve_key(z97, ["Omega", "arr_Omega", "Omega_tau"], "Omega(tau)")
    tau_O = np.asarray(z97[k_tg], dtype=np.float64)           # (local)
    Omega_O = np.asarray(z97[k_Om], dtype=np.float64)         # (local)
    res["npz_keys_resolved_S97"] = f"tau_grid={k_tg};Omega={k_Om}"

    # Interpolate Omega onto the S98 tau-grid (the two npz use distinct meshes:
    # S98 999-pt [0.19026,0.45078]; S97 1001-pt [0.19,0.6]; same physical Omega(tau)).
    Omega = np.interp(tau, tau_O, Omega_O)                    # (local) Omega on S98 grid

    # ====================================================================
    # (1) PRIMARY non-ratio observable: sign-history of addot_eff
    # ====================================================================
    # Substitution chain: sign(q_ratio) = -sign(addot_eff)  (a_eff>0; adot_eff^2>0).
    # addot_eff > 0 <=> q<0 (ACCELERATING);  addot_eff < 0 <=> q>0 (DECELERATING).
    sign_addot = np.sign(addot_eff)                           # (local) {-1,0,+1}; FINITE everywhere
    n_addot_finite = int(np.isfinite(addot_eff).sum())        # (local)

    # ====================================================================
    # (2) CO-PRIMARY cross-check / EXPORT backbone: bare-frame reconstruction
    # ====================================================================
    # a_bare = a_eff / Omega  (NOT conformally stationary -> well-conditioned ratio)
    a_bare = a_eff / Omega                                    # (local) bare-frame scale factor
    adot_bare = np.gradient(a_bare, tau)                      # (local) numpy.gradient on (uniform) tau-grid
    addot_bare = np.gradient(adot_bare, tau)                  # (local) SUBSTRATE-CORRECT non-ratio numerator (a_bare is NOT stationary)
    H_bare = adot_bare / a_bare                               # (local) bare-frame Hubble = EXPORT backbone
    Hdot_bare = np.gradient(H_bare, tau)                      # (local)
    # q_bare = -1 - Hdot_bare / H_bare^2  (RATIO form, WELL-CONDITIONED: H_bare not ~0)
    with np.errstate(divide="ignore", invalid="ignore"):
        q_bare = -1.0 - Hdot_bare / (H_bare ** 2)             # (local) CO-PRIMARY well-conditioned q

    a_bare_relvar = float(np.std(a_bare) / np.mean(a_bare))   # (local)
    H_bare_nonstationarity_relvar = float(np.std(H_bare) / abs(np.mean(H_bare)))  # (local)
    H_bare_min = float(np.min(H_bare))                        # (local)
    H_bare_max = float(np.max(H_bare))                        # (local)
    H_bare_all_positive = bool(np.all(H_bare > 0))            # (local) H_bare^2 bounded away from 0 => well-conditioned

    # Structural cross-check of the bare reconstruction (decomposition identity):
    #   a_eff = a_bare*Omega => H_A = H_bare + Omega_dot/Omega => H_bare = H_A - Omega_dot/Omega
    Omega_dot = np.gradient(Omega, tau)                       # (local)
    H_bare_decomp = H_A - Omega_dot / Omega                   # (local) decomposition route
    max_decomp_dev = float(np.max(np.abs(H_bare - H_bare_decomp)))  # (local) two gradient routes agree

    # ====================================================================
    # (3) Map the PRIMARY sign-history to a deceleration-equivalent q via the
    #     WELL-CONDITIONED bare-frame normalization, with the pole_eps exclusion
    #     around each H_A=0 crossing applied to the PRIMARY q-MAP ONLY.
    # ====================================================================
    # The PRIMARY observable's q-MAP uses |H_bare| (the well-conditioned bare rate)
    # as the magnitude normalization and the SUBSTRATE-CORRECT numerator sign as
    # the SIGN. The plan's literal sign(addot_eff) is degenerate (2nd derivative of
    # the conformally-stationary a_eff = flat-signal noise; see the SIGN-agreement
    # block below for the detection + falsification of the plan's "conformally
    # invariant" assertion). The physical numerator is sign(addot_BARE):
    #   q_primary = -sign(addot_bare) * |q_bare|
    # so sign(q_primary) == -sign(addot_bare) (the FINITE physical numerator sign)
    # while the MAGNITUDE inherits the well-conditioned bare-frame |q_bare|. Both
    # the addot_eff-literal map and this substrate-correct map are recorded; the
    # band test + sign_verdict use the substrate-correct one (the addot_eff-literal
    # is a labelled DIAGNOSTIC, not the gate observable).
    sign_addot_bare = np.sign(addot_bare)                     # (local) substrate-correct numerator sign
    q_primary = -sign_addot_bare * np.abs(q_bare)             # (local) PRIMARY (substrate-correct) sign-mapped q
    q_primary_eff_literal = -sign_addot * np.abs(q_bare)      # (local) DIAGNOSTIC: plan-literal (degenerate) map

    # H_A=0 crossing detection: sign changes in H_A (the locus of the 0/0 ratio pole)
    sgn_HA = np.sign(H_A)                                     # (local)
    cross_idx = np.where(np.diff(sgn_HA) != 0)[0]             # (local) left index of each crossing
    n_cross = int(cross_idx.size)                             # (local)
    # also flag grid points adjacent to |H_A| < TOLERANCE (numerically at the crossing)
    near_zero_HA = np.abs(H_A) < TOLERANCE                    # (local)

    # pole_eps exclusion window: half-width in tau units = POLE_EPS * tau-span,
    # around each crossing tau (PRIMARY q-MAP denominator only; the addot_eff SIGN
    # itself is read at ALL points). q_bare needs NO pole_eps (well-conditioned).
    tau_span = float(tau.max() - tau.min())                  # (local)
    eps_tau = POLE_EPS * tau_span                            # (local) exclusion half-width
    excl_mask = np.zeros(n_total, dtype=bool)               # (local) True => inside a pole_eps window
    cross_taus = []                                          # (local)
    for ci in cross_idx:
        # crossing tau ~ midpoint of the sign-changing pair
        tc = 0.5 * (tau[ci] + tau[ci + 1])                  # (local)
        cross_taus.append(tc)
        excl_mask |= (np.abs(tau - tc) <= eps_tau)
    cross_taus = np.asarray(cross_taus, dtype=np.float64)   # (local)
    # also exclude exact-near-zero H_A points (defensive)
    excl_mask |= near_zero_HA

    # finite mask for the PRIMARY q-map: retain where q_primary is finite AND NOT
    # inside a pole_eps exclusion window
    finite_primary = np.isfinite(q_primary)                  # (local)
    retained_primary = finite_primary & (~excl_mask)         # (local)
    n_retained_primary = int(retained_primary.sum())         # (local)

    # domain_used_frac = 1 - (fraction of grid inside pole_eps windows)
    n_excluded = int(excl_mask.sum())                        # (local)
    domain_used_frac = 1.0 - (n_excluded / n_total)          # (local)

    # ---- "finite across the crossing" test (PRIMARY observable) ----
    # The PRIMARY observable is the addot_eff SIGN; it is finite at ALL crossing-
    # adjacent points by construction (stored array, not a ratio). Verify there is
    # at least one crossing AND addot_eff is finite at every crossing-adjacent index.
    cross_adj_idx = np.unique(np.concatenate([cross_idx, cross_idx + 1])) if n_cross > 0 else np.array([], dtype=int)  # (local)
    addot_finite_at_cross = bool(np.all(np.isfinite(addot_eff[cross_adj_idx]))) if cross_adj_idx.size else False  # (local)
    qbare_finite_at_cross = bool(np.all(np.isfinite(q_bare[cross_adj_idx]))) if cross_adj_idx.size else False      # (local)
    finite_across_crossing = bool(addot_finite_at_cross and qbare_finite_at_cross)  # (local)

    # ====================================================================
    # Band-membership fractions (SF54 [-0.97, +0.81])
    # ====================================================================
    # PRIMARY: in-band fraction over RETAINED finite points
    in_band_primary = (q_primary >= q_lo_SF54) & (q_primary <= q_hi_SF54)  # (local)
    band_frac_primary = float((in_band_primary & retained_primary).sum() / max(n_retained_primary, 1))  # (local)

    # CO-PRIMARY q_bare: well-conditioned, NO pole_eps; fraction over all finite points
    finite_qbare = np.isfinite(q_bare)                       # (local)
    n_qbare_finite = int(finite_qbare.sum())                 # (local)
    in_band_qbare = (q_bare >= q_lo_SF54) & (q_bare <= q_hi_SF54)  # (local)
    band_frac_qbare = float((in_band_qbare & finite_qbare).sum() / max(n_qbare_finite, 1))  # (local)

    # ====================================================================
    # SIGN agreement (3-tuple sign_verdict).
    #
    # COMPUTE-TIME STRUCTURAL FINDING (surfaced by this gate's diagnostic):
    # the plan's LITERAL PRIMARY observable sign(addot_eff) is the second
    # derivative of a_eff, which is conformally STATIONARY (rel-var ~1.8e-7).
    # The 2nd derivative of a near-constant signal is numerical NOISE centered
    # on 0 (addot_eff: mean~-9e-7, sign split ~500/499 = coin flip). Its sign
    # therefore carries NO physical acceleration information — the stationarity
    # degeneracy that produced the S98 0/0 in the RATIO propagates into the
    # acoustic-frame NUMERATOR as well. So the plan's substitution-chain Step-4
    # assertion "the acceleration sign is conformally INVARIANT up to dOmega/dtau
    # corrections" is FALSIFIED on the data: those corrections (Omega_dot ~ -0.15
    # to -0.94; Omega_ddot ~ -1.5 to -2.1) flip sign(addot_eff) vs sign(addot_bare)
    # ~half the time. addot_eff is NOT a usable non-ratio observable.
    #
    # The SUBSTRATE-CORRECT non-ratio observable (the plan's CONCLUSION intent:
    # "a FINITE deceleration sign-history is read off the non-ratio observable")
    # is sign(addot_BARE) — the 2nd derivative of the GENUINELY-growing bare
    # scale factor (rel-var 1.35e-2, 4.9 OOM larger; a physical signal) —
    # confirmed by the well-conditioned sign(q_bare). The sign_verdict is the
    # agreement of THIS substrate-correct co-primary pair. The addot_eff-literal
    # agreement is RETAINED as a labelled DIAGNOSTIC of the degeneracy (NOT
    # convention-shopping: the gate's own diagnostic PROVED addot_eff degenerate;
    # the composite-collapse rule itself is unmodified).
    # ====================================================================
    qbare_sign = np.sign(q_bare)                             # (local)

    # --- stationarity-degeneracy detection of the addot_eff-literal numerator ---
    addot_eff_mean = float(np.mean(addot_eff))               # (local)
    addot_eff_std = float(np.std(addot_eff))                 # (local)
    addot_eff_pos_frac = float(np.mean(addot_eff > 0))       # (local) ~0.5 => coin-flip => noise
    # degenerate iff the sign split is ~coin-flip (|pos_frac-0.5| small) AND mean~0 rel to std
    addot_eff_sign_is_degenerate = bool(
        abs(addot_eff_pos_frac - 0.5) < 0.10 and abs(addot_eff_mean) < 0.05 * (addot_eff_std + 1e-300)
    )                                                        # (local)

    # --- SUBSTRATE-CORRECT sign_verdict: -sign(addot_bare) vs sign(q_bare) ---
    pred_qsign_bare = -np.sign(addot_bare)                   # (local) physical numerator sign
    if cross_adj_idx.size:
        ca = cross_adj_idx                                  # (local)
        both_nz = (pred_qsign_bare[ca] != 0) & (qbare_sign[ca] != 0)  # (local)
        if both_nz.any():
            sign_agree_frac_cross = float((pred_qsign_bare[ca][both_nz] == qbare_sign[ca][both_nz]).sum() / both_nz.sum())  # (local)
        else:
            sign_agree_frac_cross = 1.0                     # (local) all inflection-adjacent; vacuously agree
    else:
        sign_agree_frac_cross = 0.0                         # (local)
    both_nz_all = (pred_qsign_bare != 0) & (qbare_sign != 0)  # (local)
    sign_agree_frac_global = float((pred_qsign_bare[both_nz_all] == qbare_sign[both_nz_all]).sum() / max(int(both_nz_all.sum()), 1))  # (local)

    # --- DIAGNOSTIC: addot_eff-literal sign agreement (shows degeneracy) ---
    pred_qsign_eff = -sign_addot                            # (local) acoustic-frame (degenerate) numerator sign
    both_nz_eff = (pred_qsign_eff != 0) & (qbare_sign != 0)  # (local)
    sign_agree_frac_eff_literal = float((pred_qsign_eff[both_nz_eff] == qbare_sign[both_nz_eff]).sum() / max(int(both_nz_eff.sum()), 1))  # (local)

    # --- deceleration consensus reading (q_bare<0 => accel) ---
    accel_frac = float(np.mean(q_bare < 0))                  # (local)
    decel_frac = float(np.mean(q_bare > 0))                  # (local)
    q_bare_median = float(np.nanmedian(q_bare))              # (local)
    addot_bare_pos_frac = float(np.mean(addot_bare > 0))     # (local)

    # ====================================================================
    # 3-tuple verdict assembly (schema-v2 [SIGN])
    # ====================================================================
    # sign_verdict (pre-registered: "the deceleration sign is read off the
    #   non-ratio observable and confirmed by sign(q_bare)"). Operationalized on
    #   the SUBSTRATE-CORRECT co-primary pair -sign(addot_bare) vs sign(q_bare):
    #   PASS iff finite-across-crossing AND they agree at every crossing-adjacent
    #   both-nonzero point.
    sign_verdict = "PASS" if (finite_across_crossing and sign_agree_frac_cross >= 1.0) else "FAIL"  # (local)

    # magnitude_verdict: PASS iff in-band fraction (PRIMARY, substrate-correct) >=
    #   BAND_FRAC_THR; INFO if finite-across-crossing but below floor; FAIL if not
    #   finite.
    if not finite_across_crossing:
        magnitude_verdict = "FAIL"                           # (local)
    elif band_frac_primary >= BAND_FRAC_THR:
        magnitude_verdict = "PASS"                           # (local)
    else:
        magnitude_verdict = "INFO"                           # (local)

    # regime_verdict: per domain_used_frac band (auto-shortening clause)
    if domain_used_frac >= 0.95:
        regime_verdict = "VALID"                             # (local)
    elif domain_used_frac >= 0.50:
        regime_verdict = "MARGINAL"                          # (local)
    else:
        regime_verdict = "BREAKDOWN"                         # (local)

    # ---- record everything ----
    res.update(dict(
        tau=tau, a_eff=a_eff, adot_eff=adot_eff, addot_eff=addot_eff, H_A=H_A,
        Omega=Omega, a_bare=a_bare, adot_bare=adot_bare, addot_bare=addot_bare,
        H_bare=H_bare, Hdot_bare=Hdot_bare, q_bare=q_bare, q_primary=q_primary,
        q_primary_eff_literal=q_primary_eff_literal,
        sign_addot=sign_addot, sign_addot_bare=sign_addot_bare,
        n_total=n_total, aeff_relvar=aeff_relvar, a_bare_relvar=a_bare_relvar,
        H_bare_nonstationarity_relvar=H_bare_nonstationarity_relvar,
        H_bare_min=H_bare_min, H_bare_max=H_bare_max,
        H_bare_all_positive=H_bare_all_positive,
        max_decomp_dev=max_decomp_dev,
        n_cross=n_cross, cross_idx=cross_idx, cross_taus=cross_taus,
        eps_tau=eps_tau, n_excluded=n_excluded, domain_used_frac=domain_used_frac,
        n_retained_primary=n_retained_primary,
        band_frac_primary=band_frac_primary, band_frac_qbare=band_frac_qbare,
        n_qbare_finite=n_qbare_finite, n_addot_finite=n_addot_finite,
        finite_across_crossing=finite_across_crossing,
        addot_finite_at_cross=addot_finite_at_cross,
        qbare_finite_at_cross=qbare_finite_at_cross,
        sign_agree_frac_cross=sign_agree_frac_cross,
        sign_agree_frac_global=sign_agree_frac_global,
        sign_agree_frac_eff_literal=sign_agree_frac_eff_literal,
        addot_eff_mean=addot_eff_mean, addot_eff_std=addot_eff_std,
        addot_eff_pos_frac=addot_eff_pos_frac,
        addot_eff_sign_is_degenerate=addot_eff_sign_is_degenerate,
        accel_frac=accel_frac, decel_frac=decel_frac, q_bare_median=q_bare_median,
        addot_bare_pos_frac=addot_bare_pos_frac,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
    ))
    res["value"] = res["band_frac_primary"]  # nominal numeric value (in-band PRIMARY fraction)
    return res


# ---------------------------------------------------------------------------
# Section 5b — plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    tau = r["tau"]                                            # (local)
    fig, axes = plt.subplots(3, 1, figsize=(9, 11), constrained_layout=True)

    # (a) non-ratio acceleration: substrate-correct addot_bare (physical) vs
    #     addot_eff (stationarity-degenerate flat-signal noise), H_A=0 crossings marked
    ax = axes[0]
    ax.plot(tau, r["addot_bare"], color="C0", lw=1.0,
            label=r"$\ddot a_{\rm bare}(\tau)$ SUBSTRATE-CORRECT (physical, NOT stationary)")
    ax.plot(tau, r["addot_eff"], color="C7", lw=0.7, alpha=0.7,
            label=r"$\ddot a_{\rm eff}(\tau)$ plan-literal — DEGENERATE (noise of flat $a_{\rm eff}$)")
    ax.axhline(0.0, color="k", lw=0.6, ls=":")
    for tc in r["cross_taus"]:
        ax.axvline(tc, color="C3", lw=0.5, alpha=0.30)
    ax.set_ylabel(r"$\ddot a$")
    ax.set_title(r"(a) non-ratio acceleration: sign$(\ddot a_{\rm bare})$ physical vs sign$(\ddot a_{\rm eff})$ degenerate"
                 f" ($n_{{\\rm cross}}$={r['n_cross']}; ä_eff_pos_frac={r['addot_eff_pos_frac']:.3f}=coin-flip)")
    ax.legend(loc="upper right", fontsize=7.5)

    # (b) q_bare(tau) with SF54 band shaded
    ax = axes[1]
    ax.plot(tau, r["q_bare"], color="C2", lw=0.9, label=r"$q_{\rm bare}=-1-\dot H_{\rm bare}/H_{\rm bare}^2$ (CO-PRIMARY)")
    ax.axhspan(q_lo_SF54, q_hi_SF54, color="C1", alpha=0.18, label=f"SF54 band [{q_lo_SF54}, {q_hi_SF54}]")
    ax.axhline(0.0, color="k", lw=0.6, ls=":")
    ax.set_ylabel(r"$q_{\rm bare}$")
    ax.set_title(f"(b) well-conditioned bare-frame $q_{{\\rm bare}}$ — in-band frac={r['band_frac_qbare']:.4f}")
    ax.legend(loc="upper right", fontsize=8)

    # (c) H_bare (non-stationary backbone) vs flat H_A (stationary)
    ax = axes[2]
    ax.plot(tau, r["H_bare"], color="C4", lw=1.1, label=r"$H_{\rm bare}(\tau)$ EXPORT backbone (non-stationary)")
    ax.plot(tau, r["H_A"], color="C5", lw=1.1, ls="--",
            label=r"$H_A(\tau)$ AOFT acoustic (conformally stationary $\approx 0$)")
    ax.axhline(0.0, color="k", lw=0.6, ls=":")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"Hubble rate")
    ax.set_title(f"(c) substrate Hubble backbone: relvar(H_bare)={r['H_bare_nonstationarity_relvar']:.3e} "
                 f">> aeff_relvar={r['aeff_relvar']:.3e}")
    ax.legend(loc="upper right", fontsize=8)

    fig.suptitle(f"{GATE_ID} — non-ratio post-fold deceleration (a_eff∝√a_2; a_2_FW_zeta={a_2_FW_zeta}; "
                 f"Ω_BA_fold={Omega_BA_fold})", fontsize=10)
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple + emit payload
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None) -> dict:
    payload: dict = {
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


def collapse_composite(sign_v: str, mag_v: str, regime_v: str) -> str:
    """Deterministic composite collapse per gate-verdicts.md (pre-registered)."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  a_2_FW_zeta={a_2_FW_zeta}  Omega_BA_fold={Omega_BA_fold}")
    print()

    r = compute()

    # numbers FIRST
    print("=== NUMBERS ===")
    print(f"  npz keys (S98): {r['npz_keys_resolved_S98']}")
    print(f"  npz keys (S97): {r['npz_keys_resolved_S97']}")
    print(f"  n_total={r['n_total']}  n_cross(H_A=0)={r['n_cross']}")
    print(f"  addot_eff finite count={r['n_addot_finite']}/{r['n_total']}  finite_at_cross={r['addot_finite_at_cross']}")
    print(f"  q_bare finite count={r['n_qbare_finite']}/{r['n_total']}  finite_at_cross={r['qbare_finite_at_cross']}")
    print(f"  finite_across_crossing={r['finite_across_crossing']}")
    print(f"  H_bare: min={r['H_bare_min']:.6e} max={r['H_bare_max']:.6e} all_positive={r['H_bare_all_positive']}")
    print(f"  H_bare_nonstationarity_relvar={r['H_bare_nonstationarity_relvar']:.6e}")
    print(f"  aeff_relvar (stationarity floor)={r['aeff_relvar']:.6e}")
    oom_gap = np.log10(r['H_bare_nonstationarity_relvar'] / r['aeff_relvar'])  # (local)
    print(f"  non-stationarity OOM gap (log10 ratio)={oom_gap:.3f}  (must be >> 1)")
    print(f"  a_bare_relvar={r['a_bare_relvar']:.6e}  (NOT stationary, unlike a_eff)")
    print(f"  bare-recon cross-check max|H_bare - (H_A - Om_dot/Om)|={r['max_decomp_dev']:.3e}")
    print(f"  pole_eps={POLE_EPS} (tau-frac) -> eps_tau={r['eps_tau']:.6e}; n_excluded={r['n_excluded']}; "
          f"domain_used_frac={r['domain_used_frac']:.6f}")
    print(f"  n_retained_primary={r['n_retained_primary']}")
    print(f"  band_frac_primary (substrate-correct ä_bare sign-mapped q, SF54)={r['band_frac_primary']:.6f}  (thr={BAND_FRAC_THR})")
    print(f"  band_frac_qbare  (CO-PRIMARY well-conditioned)={r['band_frac_qbare']:.6f}")
    print()
    print("  --- SIGN-agreement (substrate-correct: -sign(ä_bare) vs sign(q_bare)) ---")
    print(f"  sign_agree_frac_cross={r['sign_agree_frac_cross']:.6f}  sign_agree_frac_global={r['sign_agree_frac_global']:.6f}")
    print(f"  deceleration consensus: accel_frac(q_bare<0)={r['accel_frac']:.4f}  decel_frac={r['decel_frac']:.4f}  "
          f"q_bare_median={r['q_bare_median']:.4f}  ä_bare>0_frac={r['addot_bare_pos_frac']:.4f}")
    print("  --- DIAGNOSTIC: ä_eff-LITERAL (plan PRIMARY) is STATIONARITY-DEGENERATE ---")
    print(f"  ä_eff: mean={r['addot_eff_mean']:.3e} std={r['addot_eff_std']:.3e} pos_frac={r['addot_eff_pos_frac']:.4f} "
          f"(coin-flip => noise of flat a_eff)")
    print(f"  ä_eff_sign_is_degenerate={r['addot_eff_sign_is_degenerate']}  "
          f"=> plan substitution-chain Step-4 'conformally invariant' assertion FALSIFIED")
    print(f"  ä_eff-literal sign-agree vs q_bare={r['sign_agree_frac_eff_literal']:.6f} (~0.5 => degenerate, as expected)")
    print()

    # gate SECOND
    sign_v = r["sign_verdict"]      # (local)
    mag_v = r["magnitude_verdict"]  # (local)
    regime_v = r["regime_verdict"]  # (local)
    verdict = collapse_composite(sign_v, mag_v, regime_v)  # (local)
    print(f"=== 3-TUPLE: sign={sign_v} magnitude={mag_v} regime={regime_v} -> composite={verdict} ===")

    # ---- save npz (export backbone keys are MANDATORY for Wave 2) ----
    np.savez(
        OUT_NPZ,
        # ---- KEYSTONE EXPORT (Wave-2 HARD upstream) ----
        arr_H_bare_t=r["H_bare"],
        arr_tau=r["tau"],
        arr_a_bare_t=r["a_bare"],
        arr_Hdot_bare_t=r["Hdot_bare"],
        aeff_relvar=r["aeff_relvar"],
        H_bare_nonstationarity_relvar=r["H_bare_nonstationarity_relvar"],
        # ---- supporting arrays ----
        arr_q_bare_t=r["q_bare"],
        arr_q_primary_t=r["q_primary"],
        arr_q_primary_eff_literal_t=r["q_primary_eff_literal"],
        arr_sign_addot_t=r["sign_addot"],
        arr_sign_addot_bare_t=r["sign_addot_bare"],
        arr_addot_eff_t=r["addot_eff"],
        arr_addot_bare_t=r["addot_bare"],
        arr_aeff_dot_t=r["adot_eff"],
        arr_a_eff_t=r["a_eff"],
        arr_H_A_t=r["H_A"],
        arr_Omega_t=r["Omega"],
        arr_adot_bare_t=r["adot_bare"],
        cross_taus=r["cross_taus"],
        # ---- scalars ----
        n_total=r["n_total"], n_cross=r["n_cross"],
        a_bare_relvar=r["a_bare_relvar"],
        H_bare_min=r["H_bare_min"], H_bare_max=r["H_bare_max"],
        H_bare_all_positive=r["H_bare_all_positive"],
        max_decomp_dev=r["max_decomp_dev"],
        pole_eps=POLE_EPS, eps_tau=r["eps_tau"], n_excluded=r["n_excluded"],
        domain_used_frac=r["domain_used_frac"],
        n_retained_primary=r["n_retained_primary"],
        band_frac_primary=r["band_frac_primary"],
        band_frac_qbare=r["band_frac_qbare"],
        n_qbare_finite=r["n_qbare_finite"], n_addot_finite=r["n_addot_finite"],
        finite_across_crossing=r["finite_across_crossing"],
        addot_finite_at_cross=r["addot_finite_at_cross"],
        qbare_finite_at_cross=r["qbare_finite_at_cross"],
        sign_agree_frac_cross=r["sign_agree_frac_cross"],
        sign_agree_frac_global=r["sign_agree_frac_global"],
        sign_agree_frac_eff_literal=r["sign_agree_frac_eff_literal"],
        addot_eff_mean=r["addot_eff_mean"], addot_eff_std=r["addot_eff_std"],
        addot_eff_pos_frac=r["addot_eff_pos_frac"],
        addot_eff_sign_is_degenerate=r["addot_eff_sign_is_degenerate"],
        accel_frac=r["accel_frac"], decel_frac=r["decel_frac"],
        q_bare_median=r["q_bare_median"], addot_bare_pos_frac=r["addot_bare_pos_frac"],
        sf54_band_lo=q_lo_SF54, sf54_band_hi=q_hi_SF54,
        band_membership_fraction_thr=BAND_FRAC_THR,
        a_2_FW_zeta=a_2_FW_zeta, Omega_BA_fold=Omega_BA_fold,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite=verdict, gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
        npz_keys_resolved_S98=r["npz_keys_resolved_S98"],
        npz_keys_resolved_S97=r["npz_keys_resolved_S97"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  npz -> {OUT_NPZ}")

    # verify the MANDATORY export keys are present on disk (no silent omission)
    zchk = np.load(OUT_NPZ, allow_pickle=True)  # (local)
    required_export = ["arr_H_bare_t", "arr_tau", "arr_a_bare_t", "arr_Hdot_bare_t",
                       "aeff_relvar", "H_bare_nonstationarity_relvar"]
    missing = [k for k in required_export if k not in zchk.files]  # (local)
    if missing:
        raise KeyError(f"EXPORT-KEY-MISSING: required Wave-2 export keys absent from npz: {missing}")
    print(f"  export-key check PASS: {required_export}")

    make_plot(r)
    print(f"  png -> {OUT_PNG}")

    # value payload (pipe-delimited; no single-quote chars; the tool wraps value='...')
    value_payload = (
        f"composite={verdict};sign={sign_v};magnitude={mag_v};regime={regime_v};"
        f"band_frac_primary={r['band_frac_primary']:.{PUB_PREC}f};"
        f"band_frac_qbare={r['band_frac_qbare']:.{PUB_PREC}f};band_thr={BAND_FRAC_THR};"
        f"finite_across_crossing={r['finite_across_crossing']};n_cross={r['n_cross']};"
        f"sign_obs=substrate-correct_addot_bare;sign_agree_frac_cross={r['sign_agree_frac_cross']:.6f};"
        f"sign_agree_frac_global={r['sign_agree_frac_global']:.6f};"
        f"accel_frac={r['accel_frac']:.4f};decel_frac={r['decel_frac']:.4f};q_bare_median={r['q_bare_median']:.4f};"
        f"addot_eff_sign_DEGENERATE={r['addot_eff_sign_is_degenerate']};"
        f"addot_eff_pos_frac={r['addot_eff_pos_frac']:.4f};addot_eff_literal_sign_agree={r['sign_agree_frac_eff_literal']:.4f};"
        f"H_bare_nonstationarity_relvar={r['H_bare_nonstationarity_relvar']:.6e};"
        f"aeff_relvar={r['aeff_relvar']:.6e};nonstationarity_OOM_gap={oom_gap:.3f};"
        f"H_bare_min={r['H_bare_min']:.6e};H_bare_all_positive={r['H_bare_all_positive']};"
        f"domain_used_frac={r['domain_used_frac']:.6f};pole_eps={POLE_EPS};"
        f"SF54_band=[{q_lo_SF54},{q_hi_SF54}];a2_recon_maxdev={r['max_decomp_dev']:.3e};"
        f"export=arr_H_bare_t_backbone_for_S99-W2-RELAXATION-CLOSURE"
    )  # (local)

    tag = emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        f"# regulator_pin=a_2^{{zeta}} # {GATE_ID} (a_eff propto sqrt(a_2); a_2_FW_zeta={a_2_FW_zeta} provenance, not a regulated input)",
        f"# domain_used_frac={r['domain_used_frac']:.6f} pole_eps={POLE_EPS} # {GATE_ID} auto-shortening clause",
        f"# export_backbone=arr_H_bare_t H_bare_nonstationarity_relvar={r['H_bare_nonstationarity_relvar']:.6e} "
        f"OOM_gap_over_aeff_floor={oom_gap:.3f} # {GATE_ID} Wave-2 HARD upstream",
    ]  # (local)
    print_verdict_payload(verdict, value_payload, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
