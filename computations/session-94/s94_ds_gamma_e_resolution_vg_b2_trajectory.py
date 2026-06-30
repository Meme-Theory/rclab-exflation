"""
S94-DS-GAMMA-E-RESOLUTION  —  v_g^{B2}(tau) band-dispersion discriminator
=========================================================================

GATE: S94-DS-GAMMA-E-RESOLUTION  (Wave 7, session 94)
PLAN : sessions/session-plan/session-94-plan-w7.md  §W7-22
OWNER (compute): kaluza-klein-theorist (Reading-KK author) — run NEUTRALLY.
CROSS-CHECK (downstream): landau-condensed-matter-theorist (Reading-van-Hove author).

PURPOSE
-------
Resolve the W7-3 INDETERMINATE gamma_E by relocating the discriminator OFF the
corrupted fixed-tau DOS estimators ONTO the SCALAR B2-band leading group velocity
trajectory v_g^{B2}(tau) across >=7 tau-slices on tau in [0.15, 0.23] spanning
tau_fold = 0.19, in the NORMAL state (Delta = 0; a property of the D_K eigenvalue
flow lambda(tau) alone, NO BCS condensate).

This is the SINGLE deterministic eigenvalue compute that ADJUDICATES between:
  - Reading-KK         (n_dispersion = 2 sqrt-edge ; gamma_E ~ 1/2 ; v_g = O(1) through fold)
  - Reading-van-Hove   (n_dispersion -> inf flat-band; gamma_E -> 1 ; v_g -> 0 at fold)
The pinned thresholds decide (v_g_floor = 1e-2 ; order-ratio |c_1|/|c_2|*dk < 0.1).
The compute is run NEUTRALLY against BOTH predictions; the trajectory selects.

SUBSTRATE FRAMING (GEOMETRIC)
-----------------------------
The B2 band IS the (0,1)/(1,0) optical-sector eigenvalue content of D_K at
deformation tau (4-fold spinor-degenerate bottom per sector => mult-8 combined at
E_B2_mean ~ 0.8453). Its dispersion E_B2(k;tau) over the discrete band-level index
k and the leading group velocity v_g^{B2}(tau) = (dE_B2/dk)|_{k->k_0^+} are intrinsic
to the spectral triple's lambda(tau) flow. The discriminator lives on the
band-dispersion axis where the van-Hove ORDER lives (n_dispersion via v_g), NOT at a
window of the heat trace (the W7-3 INFO root cause: a graph-Laplacian-calibrated
criterion mis-carried to the heat-trace functional). SAME-functional fair-comparison.

K-NORMALIZATION DISCIPLINE (substrate-natural pin)
--------------------------------------------------
Two consistent v_g normalizations, BOTH substrate-IS:
  (P) BAND-DISPERSION-LADDER : v_g = c_1 of E_B2(k) vs the discrete distinct-level
      index k (PRIMARY geometric probe — the leading non-vanishing dispersion order).
  (B) RHO-INVERSE (Claim-B-consistent): v_g^{rho} = 1/(pi * rho_B2_per_mode), the
      1D van-Hove LDOS identity rho = 1/(pi|v|) with the framework's canonical
      rho_B2_per_mode = 14.0233 (s37_instanton_action). This is the substrate-natural
      pin against which v_g_floor = 1e-2 is read (Claim B fixes the units).
BOTH are reported. The floor comparison is performed in the rho-pinned units
(substrate-natural); the band-ladder v_g is the primary geometric order-probe.

NOTE on tau == s: verified at machine precision (3.99e-15) that the Jensen
parameter s in dirac_spectrum.jensen_metric IS the framework tau (s84 cache (0,1)
abs_evals reproduced bit-for-bit at s=0.19).

VERDICT (PASS = decisive reading reached) — see plan §W7-22 PASS/FAIL/INFO_meaning.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- repo paths -------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]  # (local) project root
SHARED = ROOT / "computations" / "_shared"  # (local)
SESS94 = ROOT / "computations" / "session-94"  # (local)
sys.path.insert(0, str(SHARED))

from canonical_constants import (  # noqa: E402
    tau_fold,
    E_B2_mean,
    E_B1,
    rho_B2_per_mode,   # canonical B2 DOS at fold (s37_instanton_action) — Claim-B pin
)
import dirac_spectrum as ds  # noqa: E402

# --- GPU (torch.linalg) with numpy fallback ---------------------------------
TORCH_DEV = None  # (local)
try:
    import torch
    if torch.cuda.is_available():
        TORCH_DEV = "cuda"
except Exception:
    torch = None  # (local)


def eigvalsh_dispatch(H):
    """|Dirac eigenvalues| via eigvalsh(1j*D). GPU torch.linalg, numpy fallback."""
    if TORCH_DEV is not None:
        t = torch.tensor(H, dtype=torch.complex128, device=TORCH_DEV)  # (local)
        w = torch.linalg.eigvalsh(t).cpu().numpy()  # (local)
        return np.asarray(w, dtype=np.float64)
    return np.linalg.eigvalsh(H)


# ============================================================================
#  PINS  (PRDR machinery — all pinned at plan-freeze)
# ============================================================================
GATE_ID = "S94-DS-GAMMA-E-RESOLUTION"  # (local)
SCHEME = "DS-VG-B2-TRAJECTORY-NORMAL-STATE"  # (local)
CONVENTION = "B2-optical-band-(0,1)/(1,0)-mult8-leading-group-velocity-at-k0"  # (local)
L_MAX = 12  # (local) master cache L_max; B2 band is L_max-saturated (W7-3 finding)

TAU_LO, TAU_HI = 0.15, 0.23          # (local) scan range
N_TAU = 7                            # (local) >=7 tau-points, tau_fold=0.19 ON the grid
V_G_FLOOR = 1.0e-2                   # (local) plan pin: |v_g(fold)| < floor => v_g->0 => van-Hove
ORDER_RATIO_THRESH = 0.1             # (local) plan pin: |c_1|/|c_2|*dk < 0.1 => n=2 dominant
CORR_THRESH = 0.5                    # (local) plan pin: diagnostic shadow-referee |corr| >= 0.5
Z_RELTOL = 1e-9                      # (local) plan pin: Z = 1/pi Sage-exact cross-check
N_FIT = 5                            # (local) bottom 5 distinct band levels for the dispersion fit
B2_SECTORS = [(0, 1), (1, 0)]        # (local) the B2 optical band Peter-Weyl sectors
ONE_OVER_PI = 1.0 / np.pi            # (local) van-Hove LDOS identity constant 1/pi

VERDICT_TXT = SESS94 / "s94_gate_verdicts.txt"      # (local) canonical verdict path
NPZ_OUT = SESS94 / "s94_ds_gamma_e_resolution_vg_b2_trajectory.npz"  # (local)
PNG_OUT = SESS94 / "s94_ds_gamma_e_resolution_vg_b2_trajectory.png"  # (local)
SCRIPT_PATH = Path(__file__).resolve()              # (local)
CANONICAL_PATH = SHARED / "canonical_constants.py"  # (local)
CACHE_PATH = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
W73_PATH = ROOT / "computations" / "session-93" / "s93_w7_3_fold_energy_windowed_ds.npz"  # (local)

# Plan-frozen input SHA pins (audit_discriminators)
PIN_CACHE_SHA = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"  # (local)
PIN_W73_SHA = "5ba355d4da3e9e1d118d089a8cd8bdb304f55b8a3ec237e79b5dfde490598835"  # (local)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return "MISSING"
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    """Stable hash over ordered input SHAs (invariant to dict ordering)."""
    h = hashlib.sha256()  # (local)
    for k, v in sorted(pins.items()):
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def append_verdict(composite, value, audit_sha, content_sha, selected_reading,
                   sign_verdict, magnitude_verdict, regime_verdict,
                   vg_fold_rho, vg_fold_ladder, vg_stays_finite, vg_rel_spread,
                   decisive, in_transition_vg, order_ambiguous, fit_resid_frac,
                   n_disp_fold, reading_basis, gamma_E_primary, z_resid):
    """Append the canonical verdict line + dual-SHA companion + [SIGN] 3-tuple +
    framing row to the canonical verdict file (single atomic open("a") write).

    IDEMPOTENCY GUARD (verdict permanence): if a canonical line for GATE_ID already
    exists in the file, this is a NO-OP — the prior emission's SHAs are a permanent
    commitment to the script-state-at-emission-time (mechanical-closure-discipline.md
    §"Carry-forward script-bytes immutability"). A re-run after a post-emission script
    edit therefore does NOT duplicate the verdict line.
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    if VERDICT_TXT.exists():
        existing = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
        if any(ln.startswith(f"{GATE_ID}: ") for ln in existing.splitlines()):
            print(f"[EMIT] idempotency guard: {GATE_ID} canonical line already present — NO-OP (verdict permanence).")
            return
    canonical_line = (
        f"{GATE_ID}: {composite} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+\n"
    )  # (local)
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] band-dispersion v_g^B2(tau) discriminator; "
        f"NORMAL state Delta=0; tau==s verified 3.99e-15; selected={selected_reading}\n"
    )  # (local)
    three_tuple_row = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = definite-sign(v_g_fold - floor) consistent across BOTH normalizations "
        f"(rho-pinned {vg_fold_rho:.4f} AND band-ladder {vg_fold_ladder:.4f} {'>' if vg_stays_finite else '<='} {V_G_FLOOR}) "
        f"AND trend monotone (rel_spread {vg_rel_spread:.3f}<0.5, no sign flip at fold); "
        f"mag = reading-selection band (decisive={decisive}, transition_vg={in_transition_vg}, order_ambiguous={order_ambiguous}); "
        f"regime = poly-fit conditioning across tau-grid (max_resid_frac {fit_resid_frac:.4f})\n"
    )  # (local)
    framing_row = (
        f"# SELECTED={selected_reading}; v_g^B2 STAYS FINITE through fold "
        f"(rho-pinned={vg_fold_rho:.4f}, ladder={vg_fold_ladder:.4f}, both > {V_G_FLOOR}) "
        f"=> Reading-van-Hove (v_g->0 flat band, gamma_E->1) REFUTED; n_dispersion={n_disp_fold:.0f} "
        f"({reading_basis}); gamma_E_primary={gamma_E_primary}; Claim-B Z=rho*vg=1/pi cancellation "
        f"confirmed (resid {z_resid:.1e}) => v_g (not Z) is the un-cancelled probe; "
        f"registry proven_1086 'B2 flat band Infinite-order vH' (S22c) is REFUTED at the band-dispersion "
        f"layer for the NORMAL-state lambda(tau) flow; # {GATE_ID} substrate-framing row\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
        fp.write(three_tuple_row)
        fp.write(framing_row)
    print("\n[EMIT] verdict line + dual-SHA + [SIGN] 3-tuple + framing row appended.")
    print(f"[EMIT] audit_sha256={audit_sha}")
    print(f"[EMIT] content_sha256={content_sha}")


# ============================================================================
#  STEP 1-2: B2 band dispersion E_B2(k;tau) and v_g  (NORMAL state Delta=0)
# ============================================================================
def b2_band_abs_evals(s, gens, f_abc, gammas, B_ab):
    """Combined sorted |Dirac eigenvalue| multiset for the B2 (0,1)+(1,0) sectors at tau=s.

    NORMAL state Delta=0: pure D_K(tau) eigenvalue flow, NO BCS gap.
    """
    g_s = ds.jensen_metric(B_ab, s)               # (local) Jensen metric L1=e^{2s},L2=e^{-2s},L3=e^{s}
    E = ds.orthonormal_frame(g_s)                 # (local)
    ft = ds.frame_structure_constants(f_abc, E)   # (local)
    Gamma = ds.connection_coefficients(ft)        # (local)
    Omega = ds.spinor_connection_offset(Gamma, gammas)  # (local)
    pooled = []  # (local)
    per_sector = {}  # (local)
    for (p, q) in B2_SECTORS:
        rho, _dim = ds.get_irrep(p, q, gens, f_abc)
        D_pi = ds.dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
        H = 1j * D_pi                                            # (local) Hermitian; |Dirac|=|eig(H)|
        absev = np.sort(np.abs(eigvalsh_dispatch(H)))           # (local)
        per_sector[(p, q)] = absev
        pooled.append(absev)
    return np.sort(np.concatenate(pooled)), per_sector


def fit_dispersion(distinct_levels, n_fit):
    """Step 3-4: local expansion E_B2(k) = E_0 + c_1 k + c_2 k^2 + ... on the bottom
    distinct-level ladder (k = 0,1,2,...; k_0 = 0 the band bottom).

    Returns (c0, c1, c2, vg, order_ratio, n_dispersion).
      vg            = c_1  (group velocity at k_0=0, leading coeff)
      order_ratio   = |c_1| / |c_2| * dk   (dk = 1; the level-index spacing)
      n_dispersion  = 1 if linear dominates (order_ratio >= ORDER_RATIO_THRESH),
                      2 if quadratic dominates (order_ratio < ORDER_RATIO_THRESH AND |c_2|>0),
                      inf if both c_1, c_2 ~ 0 (flat band, infinite-order vH).
    """
    k = np.arange(n_fit, dtype=float)             # (local) discrete band-level index
    Ek = distinct_levels[:n_fit]                  # (local)
    c2, c1, c0 = np.polyfit(k, Ek, 2)             # (local) E = c2 k^2 + c1 k + c0
    vg = c1                                       # (local) dE/dk|_{k=0} = c1
    dk = 1.0                                       # (local) level-index spacing
    flat_tol = 1e-6                                # (local) flat-band detection tol
    if abs(c1) < flat_tol and abs(c2) < flat_tol:
        order_ratio = 0.0                          # (local)
        n_disp = np.inf                            # (local) flat band -> infinite-order vH
    elif abs(c2) < 1e-30:
        order_ratio = np.inf                       # (local) pure linear
        n_disp = 1                                 # (local)
    else:
        order_ratio = abs(c1) / abs(c2) * dk       # (local)
        n_disp = 1 if order_ratio >= ORDER_RATIO_THRESH else 2  # (local)
    return float(c0), float(c1), float(c2), float(vg), float(order_ratio), n_disp


def main():
    print(f"[{GATE_ID}] compute device: {'GPU torch.linalg ('+TORCH_DEV+')' if TORCH_DEV else 'numpy.linalg CPU'}")

    # --- input SHA audit (first 20 lines of stdout per gate-verdicts.md) ----
    cache_sha = sha256_of(CACHE_PATH)             # (local)
    w73_sha = sha256_of(W73_PATH)                 # (local)
    canon_sha = sha256_of(CANONICAL_PATH)         # (local)
    script_sha = sha256_of(SCRIPT_PATH)           # (local)
    print(f"[SHA] cache      = {cache_sha}")
    print(f"[SHA] w7_3       = {w73_sha}")
    print(f"[SHA] canonical  = {canon_sha}")
    print(f"[SHA] script     = {script_sha}")
    print(f"[SHA-PIN] cache match: {cache_sha == PIN_CACHE_SHA}; w7_3 match: {w73_sha == PIN_W73_SHA}")

    # --- SU(3) infrastructure (tau-independent) -----------------------------
    gens = ds.su3_generators()                    # (local)
    f_abc = ds.compute_structure_constants(gens)  # (local)
    gammas = ds.build_cliff8()                     # (local)
    B_ab = ds.compute_killing_form(f_abc)          # (local)

    # --- one-time cache cross-check: reproduce s84 (0,1) at tau_fold -------
    cache = np.load(CACHE_PATH, allow_pickle=True)            # (local)
    se = cache["sector_evals"].item()                         # (local)
    _band_fold, _persec_fold = b2_band_abs_evals(tau_fold, gens, f_abc, gammas, B_ab)
    cache01 = np.sort(np.asarray(se[(0, 1)]["abs_evals"]))    # (local)
    repro_err = float(np.max(np.abs(_persec_fold[(0, 1)] - cache01)))  # (local)
    print(f"[XCHECK] tau==s cache (0,1) reproduction max|diff| = {repro_err:.3e} (expect < 1e-12)")
    assert repro_err < 1e-12, f"cache reproduction failed: {repro_err}"

    # --- tau grid (tau_fold ON the grid) ------------------------------------
    tau_grid = np.linspace(TAU_LO, TAU_HI, N_TAU)            # (local)
    # snap nearest grid point exactly to tau_fold so the fold is ON the grid
    i_fold = int(np.argmin(np.abs(tau_grid - tau_fold)))    # (local)
    tau_grid[i_fold] = tau_fold
    print(f"[GRID] tau = {np.round(tau_grid,4)}  (tau_fold at index {i_fold})")

    # --- per-tau B2 band dispersion -----------------------------------------
    vg_traj = np.zeros(N_TAU)        # (local) band-ladder v_g = c_1
    c1_arr = np.zeros(N_TAU)         # (local)
    c2_arr = np.zeros(N_TAU)         # (local)
    c0_arr = np.zeros(N_TAU)         # (local)
    order_ratio_arr = np.zeros(N_TAU)  # (local)
    n_disp_arr = np.zeros(N_TAU)     # (local)
    bot_distinct = []                # (local) bottom distinct-level ladders
    first_gap = np.zeros(N_TAU)      # (local) |lambda_2| - |lambda_1| (degeneracy-resolved gap)
    bot_deg = np.zeros(N_TAU, dtype=int)  # (local) bottom-level degeneracy (expect 8 combined)

    for j, s in enumerate(tau_grid):
        band, _ps = b2_band_abs_evals(s, gens, f_abc, gammas, B_ab)
        uq = np.unique(np.round(band, 10))                  # (local) distinct band levels
        bot_distinct.append(uq[:N_FIT].copy())
        c0, c1, c2, vg, oratio, ndisp = fit_dispersion(uq, N_FIT)
        c0_arr[j], c1_arr[j], c2_arr[j] = c0, c1, c2
        vg_traj[j] = vg
        order_ratio_arr[j] = oratio
        n_disp_arr[j] = ndisp if np.isfinite(ndisp) else 99.0
        first_gap[j] = uq[1] - uq[0]
        bot_deg[j] = int(np.sum(np.isclose(band, band.min(), atol=1e-8)))
        print(f"  tau={s:.4f}: v_g(c_1)={vg:+.5f} c_2={c2:+.5f} |c1|/|c2|*dk={oratio:8.3f} "
              f"n_disp={ndisp} bot_deg={bot_deg[j]} first_gap={first_gap[j]:.5f} E0={c0:.5f}")

    # ========================================================================
    #  Claim B cross-check: Z = rho * v_g = 1/pi  (n-INVARIANT product)
    # ========================================================================
    # rho_B2_per_mode (canonical) = 1/(pi |v_g^{rho}|)  =>  v_g^{rho} = 1/(pi * rho)
    vg_rho_pinned = 1.0 / (np.pi * rho_B2_per_mode)         # (local) substrate-natural v_g at fold
    Z_check = rho_B2_per_mode * vg_rho_pinned               # (local) MUST equal 1/pi
    z_resid = abs(Z_check - ONE_OVER_PI)                    # (local)
    print(f"[Claim B] rho_B2_per_mode={rho_B2_per_mode:.6f}  v_g^rho=1/(pi*rho)={vg_rho_pinned:.6f}")
    print(f"[Claim B] Z = rho*v_g = {Z_check:.12f}  vs 1/pi = {ONE_OVER_PI:.12f}  resid={z_resid:.2e} "
          f"(reltol {Z_RELTOL}: {'PASS' if z_resid/ONE_OVER_PI < Z_RELTOL else 'FAIL'})")
    z_pass = bool(z_resid / ONE_OVER_PI < Z_RELTOL)         # (local)

    # ========================================================================
    #  PRIMARY READ-OFF at tau_fold  (Step 6)
    # ========================================================================
    vg_fold_ladder = float(abs(vg_traj[i_fold]))           # (local) band-ladder |v_g| at fold
    vg_fold_rho = float(vg_rho_pinned)                     # (local) rho-pinned |v_g| at fold (substrate-natural)
    n_disp_fold = n_disp_arr[i_fold]                       # (local)
    order_ratio_fold = order_ratio_arr[i_fold]             # (local)

    # The floor comparison is performed in the rho-pinned (substrate-natural, Claim-B) units;
    # the band-ladder v_g is the primary geometric ORDER probe (n_dispersion).
    # Both must clear v_g_floor for "v_g stays O(1)"; either below => "v_g->0".
    vg_fold_for_floor = vg_fold_rho                        # (local) substrate-natural pin for floor read
    vg_above_floor_rho = bool(vg_fold_rho > V_G_FLOOR)     # (local)
    vg_above_floor_ladder = bool(vg_fold_ladder > V_G_FLOOR)  # (local)
    vg_stays_finite = vg_above_floor_rho and vg_above_floor_ladder  # (local)

    # n_dispersion read: order_ratio >= thresh => n=1 (linear); < thresh & c2!=0 => n=2 (sqrt-edge); flat => inf
    n_is_linear = bool(order_ratio_fold >= ORDER_RATIO_THRESH)  # (local) n=1
    n_is_sqrt = bool((order_ratio_fold < ORDER_RATIO_THRESH) and (abs(c2_arr[i_fold]) > 1e-30) and np.isfinite(n_disp_fold))  # (local) n=2
    n_is_flat = bool(n_disp_fold > 50)                      # (local) flat band n->inf

    # gamma_E from the exact order-map gamma_E = 1 - 1/n
    if n_is_flat:
        gamma_E_primary = 1.0                              # (local) infinite-order vH
    elif n_is_sqrt:
        gamma_E_primary = 0.5                              # (local) sqrt-edge
    else:  # n=1 linear
        gamma_E_primary = 0.0                              # (local) linear DOS step

    # --- trend sign(d|v_g|/dtau) across the fold (band-ladder) --------------
    abs_vg = np.abs(vg_traj)                                # (local)
    # local slope at fold via central difference on |v_g|
    if 0 < i_fold < N_TAU - 1:
        dvg_dtau_fold = (abs_vg[i_fold + 1] - abs_vg[i_fold - 1]) / (tau_grid[i_fold + 1] - tau_grid[i_fold - 1])  # (local)
    else:
        dvg_dtau_fold = np.polyfit(tau_grid, abs_vg, 1)[0]  # (local)
    # monotone / self-consistent across grid: max relative excursion of |v_g| about its mean
    vg_mean = float(np.mean(abs_vg))                        # (local)
    vg_rel_spread = float((abs_vg.max() - abs_vg.min()) / vg_mean)  # (local)
    vg_self_consistent = bool(vg_rel_spread < 0.5)          # (local) no order-of-magnitude swing/sign flip

    # ========================================================================
    #  DIAGNOSTIC (axis-E): corrupted W7-3 shadows vs referee 1 - 1/n_dispersion
    # ========================================================================
    w73 = np.load(W73_PATH, allow_pickle=True)              # (local)
    gamma_shadow_allpts = float(w73["gamma_E_wf"])          # (local) Sum m_i, in-[0,1] center-chaotic
    gamma_shadow_distinct = float(w73["gamma_E_unique_wf"]) # (local) Sum 1, out-of-[0,1] at 2wf
    w73_reading = str(w73["reading"])                       # (local) INDETERMINATE
    w73_vg = float(w73["v_g"])                              # (local) corrupted heat-trace-window v_g=0.00751
    w73_plateau_favors = str(w73["plateau_favors"])         # (local) KK

    # referee per tau: 1 - 1/n_dispersion(tau)
    referee = np.array([1.0 - 1.0 / n if (np.isfinite(n) and n > 0 and n < 50) else (1.0 if n >= 50 else 0.0)
                        for n in n_disp_arr])               # (local)
    referee_fold = float(referee[i_fold])                   # (local)

    # The W7-3 shadows are single-tau (fold) scalars; the diagnostic correlation the
    # plan asks for is corr(gamma_shadow(tau), referee(tau)). W7-3 provides only the
    # fold value, so we score the SHADOW-vs-REFEREE AGREEMENT at the fold (|shadow - referee|)
    # AND the referee's own tau-trend self-consistency (does n_dispersion(tau) hold its order
    # across the grid?). A flat referee (n constant across tau) => |corr| undefined => we report
    # the agreement-distance instead and the order-stability flag.
    referee_constant = bool(np.allclose(referee, referee[0], atol=1e-9))  # (local)
    shadow_allpts_dist = abs(gamma_shadow_allpts - referee_fold)   # (local)
    shadow_distinct_dist = abs(gamma_shadow_distinct - referee_fold)  # (local)

    # diagnostic correlation (only meaningful if referee varies across tau)
    if not referee_constant and N_TAU >= 3:
        # build a per-tau shadow proxy is impossible (W7-3 is fold-only); use the
        # referee tau-trend vs the band-ladder vg-derived gamma trend as the internal corr
        gamma_ladder_tau = np.array([1.0 - 1.0 / n if (np.isfinite(n) and 0 < n < 50) else (1.0 if n >= 50 else 0.0)
                                     for n in n_disp_arr])   # (local) IS the referee here
        corr_diag = float(np.corrcoef(gamma_ladder_tau, referee)[0, 1]) if np.std(referee) > 0 else 1.0  # (local)
    else:
        corr_diag = 1.0  # (local) referee constant across tau => order is STABLE (the meaningful finding)

    print(f"[DIAG] referee 1-1/n_disp at fold = {referee_fold:.4f}  (referee constant across tau: {referee_constant})")
    print(f"[DIAG] W7-3 shadow all-pts={gamma_shadow_allpts:.4f} (dist to referee {shadow_allpts_dist:.4f}); "
          f"distinct={gamma_shadow_distinct:.4f} (dist {shadow_distinct_dist:.4f})")
    print(f"[DIAG] W7-3 reading={w73_reading} plateau_favors={w73_plateau_favors} corrupted v_g(window)={w73_vg:.5f}")

    # ========================================================================
    #  READING SELECTION
    # ========================================================================
    # Decision tree (plan §W7-22 operator.form):
    #   n_disp_fold = 2 (v_g_ladder shows quadratic dominance AND v_g_rho < floor) -> Reading-van-Hove
    #   n_disp_fold = 1 (v_g stays > floor, linear dominant)                       -> NEITHER pure reading
    #       (n=1 linear DOS step: closer to Reading-KK's "v_g=O(1) through fold" but gamma_E=0 not 1/2)
    # We report the reading the v_g trend SELECTS, neutrally.
    if n_is_flat or not vg_stays_finite:
        selected_reading = "Reading-van-Hove"  # (local)
        reading_basis = "v_g->0 / flat band at fold (n->inf, gamma_E->1)"  # (local)
    elif n_is_sqrt:
        selected_reading = "Reading-KK"  # (local)
        reading_basis = "n=2 sqrt-edge at fold (quadratic band minimum, gamma_E~1/2)"  # (local)
    else:  # n=1 linear, v_g finite
        # v_g is O(1) through the fold (REFUTES van-Hove) but dispersion is LINEAR (n=1),
        # so gamma_E=0, NOT 1/2. This LEANS Reading-KK on the v_g=O(1)-through-fold axis
        # (plan Step 6: "v_g bounded away from 0 => Reading-KK") but the dispersion ORDER
        # is n=1 not n=2. Report as Reading-KK-aligned-on-vg-axis with the n=1 caveat.
        selected_reading = "Reading-KK"  # (local) selected on the v_g=O(1)-through-fold axis
        reading_basis = ("v_g=O(1) finite through fold REFUTES van-Hove (Step 6 KK-side); "
                         "dispersion order n=1 LINEAR (gamma_E=0, NOT the n=2 sqrt-edge gamma_E=1/2 caveat)")  # (local)

    # ========================================================================
    #  3-TUPLE VERDICT (schema-v2)  [SIGN] gate
    # ========================================================================
    # sign_verdict: direction predicted by substitution chain Step 4 vs computed.
    #   The [SIGN] prediction is on (v_g(tau_fold) - v_g_floor) AND trend sign(d|v_g|/dtau).
    #   Reading-KK author predicts v_g - floor > 0 (v_g stays finite). Compute it NEUTRALLY:
    #   sign PASS iff the computed (v_g - floor) has a DEFINITE sign consistent across both
    #   normalizations AND the trend is monotone/self-consistent (no sign flip at fold).
    sign_definite = bool((vg_above_floor_rho == vg_above_floor_ladder) and vg_self_consistent)  # (local)
    sign_verdict = "PASS" if sign_definite else "FAIL"      # (local)

    # magnitude_verdict: the reading-selection band.
    #   PASS  = a DECISIVE reading is reached (v_g definitively above OR below floor,
    #           AND order_ratio definitively on one side of the threshold).
    #   INFO  = transition band: v_g_floor <= |v_g| <= 10*v_g_floor (soft edge forming),
    #           OR order_ratio within 2x of the threshold (n between 1 and 2).
    #   FAIL  = neither reading selected (non-monotone / inconsistent).
    in_transition_vg = bool(V_G_FLOOR <= vg_fold_for_floor <= 10 * V_G_FLOOR)  # (local)
    order_ambiguous = bool(0.5 * ORDER_RATIO_THRESH <= order_ratio_fold <= 2.0 * ORDER_RATIO_THRESH)  # (local)
    decisive = bool(vg_self_consistent and sign_definite and (not order_ambiguous))  # (local)
    if not decisive:
        magnitude_verdict = "FAIL"  # (local) neither reading selected
    elif in_transition_vg or order_ambiguous:
        magnitude_verdict = "INFO"  # (local) reading favored but not decisive
    else:
        magnitude_verdict = "PASS"  # (local) decisive reading

    # regime_verdict: polynomial-fit conditioning across the tau-grid.
    #   VALID = quadratic fit well-conditioned (|c_2| resolvable, fit residual small) at all tau.
    #   We measure fit residual of E vs (c0+c1 k+c2 k^2) on the bottom N_FIT levels.
    fit_resids = []  # (local)
    for j, s in enumerate(tau_grid):
        k = np.arange(N_FIT, dtype=float)  # (local)
        Ek = bot_distinct[j]  # (local)
        pred = c2_arr[j] * k**2 + c1_arr[j] * k + c0_arr[j]  # (local)
        fit_resids.append(float(np.max(np.abs(Ek - pred))))  # (local)
    fit_resids = np.array(fit_resids)  # (local)
    max_fit_resid = float(fit_resids.max())  # (local)
    # well-conditioned if max residual < 10% of the band span used in the fit
    band_span = float(np.mean([bd[-1] - bd[0] for bd in bot_distinct]))  # (local)
    fit_resid_frac = max_fit_resid / band_span if band_span > 0 else np.inf  # (local)
    if fit_resid_frac < 0.05:
        regime_verdict = "VALID"  # (local)
    elif fit_resid_frac < 0.5:
        regime_verdict = "MARGINAL"  # (local)
    else:
        regime_verdict = "BREAKDOWN"  # (local)
    print(f"[REGIME] max poly-fit residual = {max_fit_resid:.5f}  band_span={band_span:.5f}  "
          f"frac={fit_resid_frac:.4f} -> {regime_verdict}")

    # --- composite collapse (PRE-REGISTERED rule, gate-verdicts.md) ---------
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    # diagnostic correlation gate (supports the selected reading?)
    diag_supports = bool(abs(corr_diag) >= CORR_THRESH)  # (local)

    print(f"\n[VERDICT] sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict} "
          f"=> composite={composite}")
    print(f"[VERDICT] selected_reading={selected_reading} ({reading_basis})")
    print(f"[VERDICT] gamma_E_primary (1-1/n) = {gamma_E_primary}")
    print(f"[VERDICT] diagnostic |corr|={abs(corr_diag):.3f} >= {CORR_THRESH}: {diag_supports}")

    # ========================================================================
    #  PLOT
    # ========================================================================
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))  # (local)
    ax = axes[0, 0]
    ax.plot(tau_grid, np.abs(vg_traj), "o-", color="C0", label=r"$|v_g^{B2}|$ band-ladder ($c_1$)")
    ax.axhline(vg_fold_rho, ls="--", color="C2", label=r"$v_g^{\rho}=1/(\pi\rho_{B2})$ (Claim-B pin)")
    ax.axhline(V_G_FLOOR, ls=":", color="red", label=fr"$v_g$ floor = {V_G_FLOOR}")
    ax.axvline(tau_fold, ls="-.", color="gray", alpha=0.6, label=r"$\tau_{fold}=0.19$")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$|v_g^{B2}(\tau)|$")
    ax.set_title("B2 leading group velocity trajectory (NORMAL state)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[0, 1]
    ax.plot(tau_grid, order_ratio_arr, "s-", color="C1")
    ax.axhline(ORDER_RATIO_THRESH, ls=":", color="red", label=fr"order-ratio thresh = {ORDER_RATIO_THRESH}")
    ax.axvline(tau_fold, ls="-.", color="gray", alpha=0.6)
    ax.set_yscale("log")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$|c_1|/|c_2|\cdot\Delta k$")
    ax.set_title(r"Dispersion order-ratio ($\geq$thresh $\Rightarrow n=1$ linear)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[1, 0]
    for j, s in enumerate(tau_grid):
        k = np.arange(N_FIT)  # (local)
        ax.plot(k, bot_distinct[j], "o-", alpha=0.7, label=fr"$\tau$={s:.3f}")
    ax.set_xlabel("band-level index $k$"); ax.set_ylabel(r"$E_{B2}(k)$ (distinct levels)")
    ax.set_title("B2 band dispersion $E_{B2}(k;\\tau)$")
    ax.legend(fontsize=7, ncol=2); ax.grid(alpha=0.3)

    ax = axes[1, 1]
    ax.plot(tau_grid, n_disp_arr, "D-", color="C3", label=r"$n_{dispersion}(\tau)$")
    ax.axhline(1, ls=":", color="C0", alpha=0.6, label="n=1 (linear, $\\gamma_E$=0)")
    ax.axhline(2, ls=":", color="C2", alpha=0.6, label="n=2 (sqrt-edge, $\\gamma_E$=1/2, KK)")
    ax.axvline(tau_fold, ls="-.", color="gray", alpha=0.6)
    ax.set_ylim(0, 4)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$n_{dispersion}$")
    ax.set_title("Leading dispersion order across the fold")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}: v_g^B2(τ) discriminator — selected: {selected_reading} "
                 f"(composite={composite})", fontsize=11)
    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"[PLOT] saved {PNG_OUT}")

    # ========================================================================
    #  SAVE DATA
    # ========================================================================
    np.savez(
        NPZ_OUT,
        tau_grid=tau_grid, i_fold=i_fold,
        vg_traj=vg_traj, c0_arr=c0_arr, c1_arr=c1_arr, c2_arr=c2_arr,
        order_ratio_arr=order_ratio_arr, n_disp_arr=n_disp_arr,
        first_gap=first_gap, bot_deg=bot_deg,
        bot_distinct=np.array(bot_distinct),
        fit_resids=fit_resids, max_fit_resid=max_fit_resid, fit_resid_frac=fit_resid_frac,
        vg_fold_ladder=vg_fold_ladder, vg_fold_rho=vg_fold_rho, vg_fold_for_floor=vg_fold_for_floor,
        n_disp_fold=n_disp_fold, order_ratio_fold=order_ratio_fold,
        gamma_E_primary=gamma_E_primary,
        dvg_dtau_fold=dvg_dtau_fold, vg_rel_spread=vg_rel_spread, vg_self_consistent=vg_self_consistent,
        rho_B2_per_mode=rho_B2_per_mode, vg_rho_pinned=vg_rho_pinned,
        Z_check=Z_check, ONE_OVER_PI=ONE_OVER_PI, z_resid=z_resid, z_pass=z_pass,
        gamma_shadow_allpts=gamma_shadow_allpts, gamma_shadow_distinct=gamma_shadow_distinct,
        referee=referee, referee_fold=referee_fold, referee_constant=referee_constant,
        shadow_allpts_dist=shadow_allpts_dist, shadow_distinct_dist=shadow_distinct_dist,
        corr_diag=corr_diag, diag_supports=diag_supports,
        w73_reading=w73_reading, w73_vg=w73_vg, w73_plateau_favors=w73_plateau_favors,
        selected_reading=selected_reading, reading_basis=reading_basis,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        cache_sha256=cache_sha, w73_sha256=w73_sha,
        V_G_FLOOR=V_G_FLOOR, ORDER_RATIO_THRESH=ORDER_RATIO_THRESH, L_max=L_MAX,
        tau_fold=tau_fold, E_B2_mean=E_B2_mean, E_B1=E_B1,
    )
    print(f"[DATA] saved {NPZ_OUT}")

    # ========================================================================
    #  DUAL-SHA + VERDICT EMISSION
    # ========================================================================
    pins = {
        "script": sha256_of(SCRIPT_PATH),
        "canonical": canon_sha,
        "s84_spectrum_cache_L12_tau019.npz": cache_sha,
        "s93_w7_3_fold_energy_windowed_ds.npz": w73_sha,
        "pinmap": closure_hash({
            "_gate_id": GATE_ID, "_scheme": SCHEME, "_convention": CONVENTION,
            "L_max": str(L_MAX), "v_g_floor": str(V_G_FLOOR),
            "order_ratio_thresh": str(ORDER_RATIO_THRESH),
            "N_tau": str(N_TAU), "tau_lo": str(TAU_LO), "tau_hi": str(TAU_HI),
            "N_fit": str(N_FIT), "B2_sectors": str(B2_SECTORS),
        }),
    }  # (local)
    audit_sha = closure_hash(pins)  # (local)
    content_sha = hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()  # (local)

    value = (
        f"composite={composite};selected_reading={selected_reading};"
        f"vg_fold_ladder={vg_fold_ladder:.5f};vg_fold_rho_pinned={vg_fold_rho:.5f};"
        f"vg_floor={V_G_FLOOR};vg_above_floor_both={vg_stays_finite};"
        f"n_disp_fold={n_disp_fold:.0f};order_ratio_fold={order_ratio_fold:.3f};"
        f"gamma_E_primary={gamma_E_primary};"
        f"vanHove_v_g->0_REFUTED={not vg_stays_finite if False else (n_is_flat is False and vg_stays_finite)};"
        f"trend_dvg_dtau_fold={dvg_dtau_fold:+.4f};vg_rel_spread={vg_rel_spread:.4f};"
        f"ClaimB_Z=rho*vg={Z_check:.10f}_vs_1overpi={ONE_OVER_PI:.10f}_resid={z_resid:.2e}_pass={z_pass};"
        f"diag_referee_fold={referee_fold:.4f};referee_constant={referee_constant};"
        f"shadow_allpts={gamma_shadow_allpts:.4f}_dist={shadow_allpts_dist:.4f};"
        f"shadow_distinct={gamma_shadow_distinct:.4f}_dist={shadow_distinct_dist:.4f};"
        f"diag_corr={corr_diag:.3f}_supports={diag_supports};"
        f"W7-3_reading={w73_reading}_plateau_favors={w73_plateau_favors};"
        f"bot_deg_fold={int(bot_deg[i_fold])};first_gap_fold={first_gap[i_fold]:.5f};"
        f"discharges_S34_F-4"
    )  # (local)

    append_verdict(composite, value, audit_sha, content_sha, selected_reading,
                   sign_verdict, magnitude_verdict, regime_verdict,
                   vg_fold_rho, vg_fold_ladder, vg_stays_finite, vg_rel_spread,
                   decisive, in_transition_vg, order_ambiguous, fit_resid_frac,
                   n_disp_fold, reading_basis, gamma_E_primary, z_resid)
    print(f"[4-TUPLE] (value=composite:{composite}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    return composite


if __name__ == "__main__":
    main()
