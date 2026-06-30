"""
S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE
============================================

Owner: mack-cosmic-bridge (S87 W2-3, lead)
Co-signer: connes-ncg-theorist (NCG-axiomatic moment-computation cross-check)
Plan: sessions/session-plan/session-87-plan-w2.md §W2-3
Trigger: [VERIFY] (substitution chain pre-registers sign(alpha_s_route_3) = -1)

Direct numerical computation of alpha_s from GGE-relic Bogoliubov occupation-
number variance at horizon crossing, INDEPENDENT of the single-pole Mellin
moment assumption (S82 W3-9 alpha_s_canonical = n_s^2 - 1 = -0.085873).

==== SUBSTITUTION CHAIN (substrate-physics direction prediction) ====

Definition 1 (substrate-IS observable):
   n_a^GGE := |v_a|^2  =  (Bogoliubov occupation number; mode a; B1+B2+B3 branches)
            evaluated on (A_K^{<=10}, H_K^{<=10}, D_K^{<=10}) post-tau_fold.

Definition 2 (multi-mode population variance, K-dependent):
   For each K in the horizon-crossing window K in [0.95 K_h, 1.05 K_h]:
     v_a(K)^2 = (1/2) * (1 - xi_a(K)/E_a(K))
     where xi_a(K) = (xi_a^(0)) * (K / K_horizon)^2  (acoustic dispersion;
       single-particle energy scales as K^2 in the BdG long-wavelength regime)
     and  E_a(K) = sqrt(xi_a(K)^2 + |Delta_a|^2).
   The static frozen amplitudes from s52_bogoliubov_amp.npz are recovered
   exactly at K = K_horizon (BY CONSTRUCTION via the K-rescaling above).

Definition 3 (substrate-IS occupation variance):
   P_GGE(K) := <(delta n_a^GGE(K))^2>_a  =  Var_a (n_a^GGE(K))
            = (1/N_modes) * sum_a (n_a^GGE(K))^2  - ((1/N_modes) sum_a n_a^GGE(K))^2

Definition 4 (substrate-IS spectral tilt of the variance — running-of-running route):
   alpha_s_route_3 := d^2 ln P_GGE / d (ln K)^2  evaluated at K = K_horizon.
   (Numerical second derivative via central 5-point finite difference on the
   K-window with dlnK = 0.001 — DOUBLY differentiable.)

Definition 5 (S82 W3-9 single-pole canonical):
   alpha_s_canonical := n_s_framework^2 - 1
                     = 0.9561^2 - 1
                     = -0.08587279000000014

Substitute:
   Step 1: n_s_framework = 0.9561  (canonical_constants.py:1558)
   Step 2: 0.9561**2 = 0.91412721
   Step 3: 0.91412721 - 1 = -0.08587279
   Step 4: sign(alpha_s_canonical) = -1  (NEGATIVE; red running-of-running)

Direction prediction (substrate-physics):
   The post-tau_fold GGE is a non-thermal occupation distribution with permanent
   red-running structure inherited from the supersonic transit through the van Hove
   fold (S38 GGE permanence + S82 single-pole Mellin reading at s=3). The Bogoliubov
   occupation-variance route MUST inherit this red-running sign IFF the single-pole
   assumption is not load-bearing.

   PREDICTED: sign(alpha_s_route_3) = -1 (NEGATIVE; matches alpha_s_canonical).

PASS/FAIL/INFO criteria (per plan §W2-3.5):
   delta_alpha_s := alpha_s_route_3 - alpha_s_canonical
   composite from 3-tuple (sign, magnitude, regime):
     sign_verdict = PASS iff sign(alpha_s_route_3) == -1
     magnitude_verdict = PASS iff |delta_alpha_s| < 0.01 (ABSOLUTE)
                       = INFO iff 0.01 <= |delta_alpha_s| < 0.05
                       = FAIL iff |delta_alpha_s| >= 0.05
     regime_verdict = VALID iff K-window fully within BdG-non-singular regime
                                AND f_used >= 0.95 of K-window covered
   composite collapse per gate-verdicts.md S87+ schema-v2.

==== INPUTS ====
- s52_bogoliubov_amp.npz  (post-tau_fold Bogoliubov u_k, v_k, E_qp, Delta_per_mode;
                           8-mode B1+B2+B3 branch index)
- s84_spectrum_cache_L12_tau019.npz  (D_K eigenvalue cache, L_max=12; truncated to
                                       L_max=10 for the canonical-pin sub-block)
- s82_w3_9_alpha_s_scheme_identity_pin.npz  (canonical pin; soft-prereq — fall back
                                              to direct n_s_framework**2 - 1 if absent)
- s86_w11_eta_gv_residual.npz  (CF-65 anchor; soft-prereq — bypass if absent)

==== OUTPUTS ====
- s87_w2_alpha_s_direct_moment_independent_route.npz  (alpha_s_route_3 trajectory,
                                                        n_a^GGE(K) trajectory,
                                                        delta_alpha_s)
- s87_w2_alpha_s_direct_moment_independent_route.png  (alpha_s_route_3 vs K + canonical pin)
- canonical verdict line + W9a-99 dual-SHA companion + S87+ schema-v2 3-tuple
  annotation row appended to computations/session-87/s87_gate_verdicts.txt
- working-paper section sessions/archive/session-87/session-87-results-workingpaper.md §W2-3

Author: mack-cosmic-bridge (S87 W2-3)
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

os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-cap before numpy

import hashlib  # noqa: E402
import json     # noqa: E402
import sys      # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

# Random seed pin per plan §W2-3.6
RANDOM_SEED = 42  # (local) canonical pin per plan §W2-3.6
np.random.seed(RANDOM_SEED)

# Canonical-constants compliance per .claude/rules/math-scripts.md
from canonical_constants import (  # noqa: E402
    n_s_framework, tau_fold, Delta_BCS, K_base,
)

# ---------------------------------------------------------------- paths

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
# X2-removed: alias 'T0' = ... 'computations' (replaced by tools.computation_root.resolve_*)
BOG_PATH     = resolve_output(52, 's52_bogoliubov_amp.npz')
CACHE_PATH   = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')
S82_PIN_PATH = resolve_output(82, 's82_w3_9_alpha_s_scheme_identity_pin.npz')  # soft-prereq
ETA_GV_PATH  = resolve_output(86, 's86_w11_eta_gv_residual.npz')               # soft-prereq
NPZ_OUT      = resolve_output(87, 's87_w2_alpha_s_direct_moment_independent_route.npz')
PNG_OUT      = resolve_output(87, 's87_w2_alpha_s_direct_moment_independent_route.png')
JSON_OUT     = resolve_output(87, 's87_w2_alpha_s_direct_moment_independent_route.json')
VERDICT_OUT  = resolve_output(87, 's87_gate_verdicts.txt')
SCRIPT_PATH  = resolve_script(87, 's87_w2_alpha_s_direct_moment_independent_route.py')
WP_PATH      = PROJECT_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"

# ---------------------------------------------------------------- gate pins

GATE_ID    = "S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE"
SCHEME     = "GGE-Bogoliubov-occupation-variance"
CONVENTION = "horizon-crossing-K-window-canonical"
L_MAX      = 10  # (local) plan §W2-3.6 canonical truncation; declared as a_n^{Mellin} pin

# K-window pins per plan §W2-3.6
# K_horizon: per s52_bogoliubov_amp.npz horizon-crossing pin convention
# (we use K_base = 2.035 as the substrate-natural horizon scale per S82 W2-4
#  R3 band-weighted squeezing anchor; canonical_constants.py:206)
K_HORIZON_FRAC = (0.95, 1.05)   # (local) 5% window around horizon crossing
DLNK           = 0.001          # (local) step in ln K
PASS_BAND      = 0.01           # (local) ABSOLUTE PASS tolerance (plan §5)
INFO_BAND      = 0.05           # (local) ABSOLUTE INFO ceiling (plan §5)

# ---------------------------------------------------------------- helpers

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def k_dependent_bogoliubov(v_static: np.ndarray, u_static: np.ndarray,
                            E_static: np.ndarray, delta_static: np.ndarray,
                            K_ratio: float) -> np.ndarray:
    """K-dependent Bogoliubov occupation n_a^GGE(K) = |v_a(K)|^2.

    From the static post-tau_fold cache, recover xi_a^(0) and rescale:
        xi_a(K) = xi_a^(0) * (K / K_horizon)^2   [acoustic K^2 dispersion]
        E_a(K)  = sqrt(xi_a(K)^2 + |Delta_a|^2)
        v_a(K)^2 = 0.5 * (1 - xi_a(K) / E_a(K))

    At K = K_horizon (K_ratio = 1.0) we recover the static v_a exactly.

    Substitution chain (Bogoliubov inversion at K_ratio = 1):
        v_static^2 = 0.5 * (1 - xi^(0)/E^(0))
        => xi^(0)/E^(0) = 1 - 2 v_static^2 = u_static^2 - v_static^2
        => xi^(0) = (u_static^2 - v_static^2) * E_static
    """
    # (local) Recover static xi_a^(0) from static u, v, E
    xi0 = (u_static ** 2 - v_static ** 2) * E_static  # (local)

    # (local) K-rescaling — acoustic dispersion epsilon ~ K^2 in the BdG
    # long-wavelength regime; |Delta| is K-independent (BCS gap).
    xi_K = xi0 * (K_ratio ** 2)  # (local)
    E_K  = np.sqrt(xi_K ** 2 + np.abs(delta_static) ** 2)  # (local)
    # protect E_K against zero (gapless modes: B1 has Delta=0)
    eps_floor = 1e-30  # (local)
    E_K_safe = np.where(E_K < eps_floor, eps_floor, E_K)  # (local)

    v_K2 = 0.5 * (1.0 - xi_K / E_K_safe)  # (local) Bogoliubov occupation
    # numerical clamping to [0,1] to handle floating noise on the gapless mode
    v_K2 = np.clip(v_K2, 0.0, 1.0)  # (local)
    return v_K2


def compute_route_3_alpha_s(v_static: np.ndarray, u_static: np.ndarray,
                             E_static: np.ndarray, delta_static: np.ndarray,
                             k_ratios: np.ndarray, use_gpu: bool):
    """Compute alpha_s_route_3 from Var(n_a^GGE(K)) over the K-window.

    Returns (alpha_s_route_3, P_GGE_K, n_a_K_grid, regime_valid_frac).
    """
    n_K = len(k_ratios)  # (local)
    n_modes = len(v_static)  # (local)
    n_a_grid = np.zeros((n_K, n_modes))  # (local)
    P_GGE = np.zeros(n_K)  # (local)

    if use_gpu:
        try:
            import torch
            device = torch.device("cuda")
            u_t = torch.tensor(u_static, device=device, dtype=torch.float64)
            v_t = torch.tensor(v_static, device=device, dtype=torch.float64)
            E_t = torch.tensor(E_static, device=device, dtype=torch.float64)
            d_t = torch.tensor(np.abs(delta_static), device=device, dtype=torch.float64)
            xi0_t = (u_t ** 2 - v_t ** 2) * E_t
            for i, kr in enumerate(k_ratios):
                xi_K = xi0_t * (kr ** 2)
                E_K  = torch.sqrt(xi_K ** 2 + d_t ** 2)
                E_K_safe = torch.where(E_K < 1e-30, torch.full_like(E_K, 1e-30), E_K)
                v_K2 = 0.5 * (1.0 - xi_K / E_K_safe)
                v_K2 = torch.clamp(v_K2, 0.0, 1.0)
                n_a_grid[i] = v_K2.cpu().numpy()
                # variance over modes — population statistic over the GGE state
                P_GGE[i] = (v_K2.var(unbiased=False)).item()
            print(f"  [GPU] K-window computed via torch.cuda on AMD RX 9070 XT")
        except Exception as e:
            print(f"  [GPU FAILURE — fallback to CPU] {e}", file=sys.stderr)
            use_gpu = False

    if not use_gpu:
        for i, kr in enumerate(k_ratios):
            v_K2 = k_dependent_bogoliubov(v_static, u_static, E_static, delta_static, kr)
            n_a_grid[i] = v_K2
            P_GGE[i] = float(np.var(v_K2))
        print("  [CPU] K-window computed via numpy")

    # regime-validity audit: P_GGE > 0 throughout (variance non-degenerate)
    regime_valid_mask = P_GGE > 0  # (local)
    regime_valid_frac = float(regime_valid_mask.sum()) / n_K  # (local)

    # Guard: if P_GGE has zeros (degenerate variance) the second log-derivative
    # is undefined; mark regime BREAKDOWN
    if P_GGE.min() <= 0:
        return None, P_GGE, n_a_grid, regime_valid_frac

    ln_P = np.log(P_GGE)  # (local)
    ln_K = np.log(k_ratios)  # (local)

    # Substitution chain for the second log-derivative:
    #   n_s_route_3(K) - 1 = d ln P_GGE / d ln K        [first log-derivative]
    #   alpha_s_route_3   = d^2 ln P_GGE / d (ln K)^2   [second log-derivative]
    # Numerical method: 5-point central finite difference on uniform-in-ln-K grid
    # at the index closest to ln K = 0 (K = K_horizon).
    # The grid IS uniform in ln K by construction (k_ratios = exp(arange * dlnK)).
    h = ln_K[1] - ln_K[0]  # (local) grid step in ln K

    # find index closest to ln K = 0 (i.e. K = K_horizon)
    i0 = int(np.argmin(np.abs(ln_K)))  # (local)

    # 5-point central second derivative:  f''(x0) approx
    #   (-f(x-2h) + 16 f(x-h) - 30 f(x0) + 16 f(x+h) - f(x+2h)) / (12 h^2)
    # Need indices i0-2, i0-1, i0, i0+1, i0+2 all in range.
    if i0 < 2 or i0 > n_K - 3:
        # reduce to 3-point
        d2 = (ln_P[i0+1] - 2 * ln_P[i0] + ln_P[i0-1]) / (h ** 2)  # (local)
    else:
        d2 = (-ln_P[i0-2] + 16 * ln_P[i0-1] - 30 * ln_P[i0]
              + 16 * ln_P[i0+1] - ln_P[i0+2]) / (12.0 * h ** 2)  # (local)

    return float(d2), P_GGE, n_a_grid, regime_valid_frac


def render_plot(k_ratios: np.ndarray, P_GGE: np.ndarray,
                alpha_s_route_3: float, alpha_s_canonical: float,
                delta_alpha_s: float, regime_valid_frac: float,
                composite: str) -> None:
    """alpha_s_route_3 vs K-window plot with canonical pin overlay."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 1, figsize=(8.0, 7.5),
                              gridspec_kw={"hspace": 0.35})

    # Top: ln P_GGE vs ln K
    ax = axes[0]
    ln_K = np.log(k_ratios)  # (local)
    ln_P = np.log(np.maximum(P_GGE, 1e-300))  # (local) numerical guard
    ax.plot(ln_K, ln_P, color="#1f77b4", lw=1.5,
            label="ln P_GGE(K) substrate-IS occupation variance")
    ax.axvline(0.0, color="k", ls="--", lw=0.8, alpha=0.6,
               label="K = K_horizon")
    ax.set_xlabel("ln(K / K_horizon)")
    ax.set_ylabel("ln P_GGE")
    ax.set_title(f"{GATE_ID}\nGGE-Bogoliubov occupation-variance route — substrate-IS observable on (A_K^{{<=10}}, H_K^{{<=10}}, D_K^{{<=10}})")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3)

    # Bottom: comparison bar with canonical pin
    ax = axes[1]
    routes = ["alpha_s_route_3\n(GGE-Bogoliubov-variance)", "alpha_s_canonical\n(n_s^2 - 1, S82 W3-9)"]
    values = [alpha_s_route_3, alpha_s_canonical]
    colors = ["#2ca02c" if composite == "PASS" else
              "#d62728" if composite == "FAIL" else
              "#ff7f0e", "#888888"]
    ax.bar(routes, values, color=colors, edgecolor="k", lw=1.0)
    ax.axhline(0.0, color="k", lw=0.8)
    ax.axhline(alpha_s_canonical + PASS_BAND, color="green", ls=":", lw=0.8,
               label=f"PASS band ±{PASS_BAND}")
    ax.axhline(alpha_s_canonical - PASS_BAND, color="green", ls=":", lw=0.8)
    ax.axhline(alpha_s_canonical + INFO_BAND, color="orange", ls=":", lw=0.8,
               label=f"INFO ceiling ±{INFO_BAND}")
    ax.axhline(alpha_s_canonical - INFO_BAND, color="orange", ls=":", lw=0.8)
    ax.set_ylabel("alpha_s")
    ax.set_title(f"Two-route comparison: delta = {delta_alpha_s:+.4e}; "
                 f"regime_valid_frac = {regime_valid_frac:.3f}; composite = {composite}")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3, axis="y")

    fig.savefig(PNG_OUT, dpi=140, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    print("=" * 72)
    print(f"GATE: {GATE_ID}")
    print(f"  scheme:     {SCHEME}")
    print(f"  convention: {CONVENTION}")
    print(f"  L_max:      {L_MAX}")
    print(f"  random seed: {RANDOM_SEED}")
    print("=" * 72)

    # ------------------------------------------------------------- inputs
    if not BOG_PATH.exists():
        print(f"FATAL: required input missing: {BOG_PATH}", file=sys.stderr)
        return 2
    if not CACHE_PATH.exists():
        print(f"FATAL: required input missing: {CACHE_PATH}", file=sys.stderr)
        return 2

    bog_sha    = sha256_file(BOG_PATH)
    cache_sha  = sha256_file(CACHE_PATH)
    s82_present = S82_PIN_PATH.exists()
    eta_present = ETA_GV_PATH.exists()
    s82_sha = sha256_file(S82_PIN_PATH) if s82_present else "<absent-soft-prereq>"
    eta_sha = sha256_file(ETA_GV_PATH) if eta_present else "<absent-soft-prereq>"
    script_sha = sha256_file(SCRIPT_PATH) if SCRIPT_PATH.exists() else "<runtime-pending>"

    print(f"  s52 input sha256:  {bog_sha}")
    print(f"  s84 cache sha256:  {cache_sha}")
    print(f"  s82 pin sha256:    {s82_sha}  (soft-prereq present={s82_present})")
    print(f"  eta-GV sha256:     {eta_sha}  (soft-prereq present={eta_present})")
    print(f"  script sha256:     {script_sha}")

    # ------------------------------------------------------- input load
    bog = np.load(BOG_PATH, allow_pickle=True)
    u_static = bog["u_k"].astype(np.float64)            # (8,) Bogoliubov u
    v_static = bog["v_k"].astype(np.float64)            # (8,) Bogoliubov v
    E_static = bog["E_qp"].astype(np.float64)           # (8,) quasiparticle energies (positive branch)
    delta_static = bog["Delta_per_mode"].astype(np.complex128)  # (8,)

    print(f"\n  Static cache: {len(v_static)} modes (B1+B2+B3)")
    print(f"  E_qp range: [{E_static.min():.6f}, {E_static.max():.6f}] M_KK")
    print(f"  v_k range:  [{v_static.min():.6f}, {v_static.max():.6f}]")
    print(f"  Delta_per_mode (abs): {np.abs(delta_static)}")

    # truncate s84 cache to L_max=10 sub-block (level <= 10 in (p,q) sector keys)
    cache = np.load(CACHE_PATH, allow_pickle=True)
    sectors = cache["sector_evals"].item()
    n_eigs_L10_truncated = sum(  # (local) plan §W2-3.6 documents N_eval = 155984
        len(info["abs_evals"]) * info["dim"]
        for sec, info in sectors.items()
        if max(sec) <= L_MAX
    )
    print(f"  L_max={L_MAX} sub-block weighted eigenvalue count: {n_eigs_L10_truncated}")
    print(f"  (plan §W2-3.6 N_eval pin: 155984 — sub-block multiplicity-weighted truncation)")

    # ------------------------------------------------- canonical alpha_s
    # Substitution per definition 5: alpha_s_canonical = n_s_framework^2 - 1
    # canonical_constants.py:1558 pins n_s_framework = 0.9561
    alpha_s_canonical = n_s_framework ** 2 - 1.0  # (local) -0.08587279
    print(f"\n  n_s_framework            = {n_s_framework}")
    print(f"  alpha_s_canonical        = n_s_framework**2 - 1 = {alpha_s_canonical:.10f}")
    print(f"  predicted sign           = -1 (NEGATIVE; red running-of-running)")

    # if S82 pin file exists, cross-check the canonical value
    canonical_consistent = True  # (local)
    canonical_audit_note = "S82 W3-9 pin file absent — fallback to in-script canonical"  # (local)
    if s82_present:
        try:
            s82d = np.load(S82_PIN_PATH, allow_pickle=True)
            for k in ("alpha_s_id", "alpha_s_canonical", "alpha_s_scheme_identity"):
                if k in s82d.files:
                    val = float(s82d[k])
                    diff = abs(val - alpha_s_canonical)
                    if diff < 1e-3:
                        canonical_audit_note = (
                            f"S82 W3-9 pin {k} = {val:.6f}; agrees with in-script canonical "
                            f"to {diff:.2e}")
                    else:
                        canonical_consistent = False
                        canonical_audit_note = (
                            f"S82 W3-9 pin {k} = {val:.6f}; DEVIATES from in-script canonical by {diff:.2e}")
                    break
        except Exception as e:
            canonical_audit_note = f"S82 pin load failed: {e}; using in-script canonical"
    print(f"  S82 canonical audit:     {canonical_audit_note}")

    # ----------------------------------------------------- K-window scan
    # ln_K grid uniform in ln K: k_ratios = exp(linspace(ln(0.95), ln(1.05), N))
    # with step DLNK = 0.001 in ln K
    ln_min = np.log(K_HORIZON_FRAC[0])  # (local)
    ln_max = np.log(K_HORIZON_FRAC[1])  # (local)
    n_K_pts = int(round((ln_max - ln_min) / DLNK)) + 1  # (local) ~98 points
    ln_K_grid = np.linspace(ln_min, ln_max, n_K_pts)  # (local)
    k_ratios = np.exp(ln_K_grid)  # (local)
    print(f"\n  K-window: K/K_horizon in [{K_HORIZON_FRAC[0]}, {K_HORIZON_FRAC[1]}]")
    print(f"  dlnK = {DLNK}; N_K = {n_K_pts}")

    # GPU detection
    try:
        import torch
        use_gpu = bool(torch.cuda.is_available())
    except Exception:
        use_gpu = False
    print(f"  GPU enabled: {use_gpu}")

    # --------------------------- compute alpha_s_route_3 (GPU + CPU CC)
    print("\n  -- GPU route --")
    alpha_gpu, P_GPU, n_a_GPU, regime_valid_frac_gpu = compute_route_3_alpha_s(
        v_static, u_static, E_static, delta_static, k_ratios, use_gpu=use_gpu)

    print("\n  -- CPU route (CC2 cross-check) --")
    alpha_cpu, P_CPU, n_a_CPU, regime_valid_frac_cpu = compute_route_3_alpha_s(
        v_static, u_static, E_static, delta_static, k_ratios, use_gpu=False)

    # CC2 GPU vs CPU bit-identity audit
    if alpha_gpu is None or alpha_cpu is None:
        cc2_diff = float("nan")
        cc2_pass = False
    else:
        cc2_diff = abs(alpha_gpu - alpha_cpu)  # (local)
        cc2_pass = cc2_diff < 1e-10  # (local) bit-identity floor

    # canonical alpha_s_route_3 = GPU (or CPU if GPU failed)
    if alpha_gpu is not None:
        alpha_s_route_3 = alpha_gpu  # (local)
        P_GGE = P_GPU  # (local)
        n_a_K_grid = n_a_GPU  # (local)
        regime_valid_frac = regime_valid_frac_gpu  # (local)
    else:
        alpha_s_route_3 = alpha_cpu  # (local)
        P_GGE = P_CPU  # (local)
        n_a_K_grid = n_a_CPU  # (local)
        regime_valid_frac = regime_valid_frac_cpu  # (local)

    # If both routes returned None, regime is BREAKDOWN
    if alpha_s_route_3 is None:
        print("  REGIME BREAKDOWN: P_GGE non-positive across K-window; "
              "second log-derivative undefined.")
        # emit FAIL with diagnostic
        alpha_s_route_3 = float("nan")
        delta_alpha_s = float("nan")
        sign_verdict = "N/A"
        magnitude_verdict = "FAIL"
        regime_verdict = "BREAKDOWN"
        composite = "FAIL"
    else:
        delta_alpha_s = alpha_s_route_3 - alpha_s_canonical  # (local)

        # ---- 3-tuple verdict per S87+ schema-v2 (gate-verdicts.md) ----
        # sign verdict: predicted sign(alpha_s_route_3) == -1
        if alpha_s_route_3 < 0:
            sign_verdict = "PASS"
        elif alpha_s_route_3 > 0:
            sign_verdict = "FAIL"
        else:
            sign_verdict = "FAIL"  # zero is not the predicted negative sign

        # magnitude verdict
        if abs(delta_alpha_s) < PASS_BAND:
            magnitude_verdict = "PASS"
        elif abs(delta_alpha_s) < INFO_BAND:
            magnitude_verdict = "INFO"
        else:
            magnitude_verdict = "FAIL"

        # regime verdict — fraction of K-window with non-degenerate variance
        if regime_valid_frac >= 0.95:
            regime_verdict = "VALID"
        elif regime_valid_frac >= 0.50:
            regime_verdict = "MARGINAL"
        else:
            regime_verdict = "BREAKDOWN"

        # composite collapse rule (PRE-REGISTERED — Class-3 PROHIBITED to modify)
        if regime_verdict == "BREAKDOWN":
            composite = "FAIL"
        elif sign_verdict == "FAIL":
            composite = "FAIL"
        elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
            composite = "FAIL"
        elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
            composite = "INFO"
        elif magnitude_verdict == "INFO":
            composite = "INFO"
        else:
            composite = "PASS"

    # ----- print results -----
    print("\n" + "=" * 72)
    print(f"  alpha_s_route_3      = {alpha_s_route_3}")
    print(f"  alpha_s_canonical    = {alpha_s_canonical}")
    print(f"  delta_alpha_s        = {delta_alpha_s}")
    print(f"  P_GGE at K_horizon   = {P_GGE[len(P_GGE)//2] if len(P_GGE) > 0 else 'NA'}")
    print(f"  P_GGE min/max        = {P_GGE.min()}, {P_GGE.max()}")
    print(f"  regime_valid_frac    = {regime_valid_frac}")
    print(f"  cc2_gpu_vs_cpu_diff  = {cc2_diff}  (cc2 PASS={cc2_pass})")
    print(f"  sign_verdict         = {sign_verdict}")
    print(f"  magnitude_verdict    = {magnitude_verdict}")
    print(f"  regime_verdict       = {regime_verdict}")
    print(f"  composite verdict    = {composite}")
    print("=" * 72)

    # ---------------------------------------------------- data + plot
    np.savez(
        NPZ_OUT,
        # core results
        alpha_s_route_3=np.float64(alpha_s_route_3),
        alpha_s_canonical=np.float64(alpha_s_canonical),
        delta_alpha_s=np.float64(delta_alpha_s),
        # K-window arrays
        ln_K_over_K_horizon=ln_K_grid,
        K_over_K_horizon=k_ratios,
        P_GGE_K=P_GGE,
        n_a_K_grid=n_a_K_grid,
        # 8-mode static cache (input echo)
        v_static=v_static,
        u_static=u_static,
        E_static=E_static,
        delta_static=delta_static,
        # CC2 cross-check
        alpha_gpu=np.float64(alpha_gpu if alpha_gpu is not None else np.nan),
        alpha_cpu=np.float64(alpha_cpu if alpha_cpu is not None else np.nan),
        cc2_diff=np.float64(cc2_diff),
        cc2_pass=np.bool_(cc2_pass),
        # verdicts
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite=composite,
        regime_valid_frac=np.float64(regime_valid_frac),
        # pins
        n_s_framework=np.float64(n_s_framework),
        tau_fold=np.float64(tau_fold),
        Delta_BCS=np.float64(Delta_BCS),
        K_base=np.float64(K_base),
        random_seed=np.int64(RANDOM_SEED),
        n_eigs_L10_truncated=np.int64(n_eigs_L10_truncated),
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=np.int64(L_MAX),
        gate_id=GATE_ID,
    )
    print(f"\n  Data: {NPZ_OUT.name}")

    if not np.isnan(alpha_s_route_3):
        render_plot(k_ratios, P_GGE, alpha_s_route_3, alpha_s_canonical,
                    delta_alpha_s, regime_valid_frac, composite)
        print(f"  Plot: {PNG_OUT.name}")

    # ------------------------------------------------ closure SHA pin map
    pin_map = {
        "gate_id":           GATE_ID,
        "scheme":            SCHEME,
        "convention":        CONVENTION,
        "L_max":             L_MAX,
        "K_horizon_frac":    list(K_HORIZON_FRAC),
        "dlnK":              DLNK,
        "PASS_BAND_abs":     PASS_BAND,
        "INFO_BAND_abs":     INFO_BAND,
        "random_seed":       RANDOM_SEED,
        "n_s_framework":     n_s_framework,
        "tau_fold":          tau_fold,
        "Delta_BCS":         Delta_BCS,
        "K_base":            K_base,
        "alpha_s_canonical": alpha_s_canonical,
        "alpha_s_route_3":   None if np.isnan(alpha_s_route_3) else alpha_s_route_3,
        "delta_alpha_s":     None if np.isnan(delta_alpha_s) else delta_alpha_s,
        "regime_valid_frac": regime_valid_frac,
        "cc2_diff":          cc2_diff,
        "sign_verdict":      sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict":    regime_verdict,
        "composite":         composite,
        "n_eigs_L10":        n_eigs_L10_truncated,
        "bog_sha256":        bog_sha,
        "cache_sha256":      cache_sha,
        "s82_pin_sha256":    s82_sha,
        "eta_gv_sha256":     eta_sha,
        "script_sha256":     script_sha,
    }
    audit_sha = closure_hash(pin_map)

    # ----------------------------------------------------- JSON sidecar
    sidecar = dict(pin_map)
    sidecar["audit_sha256"] = audit_sha
    sidecar["substitution_chain_ref"] = "sessions/session-plan/session-87-plan-w2.md §W2-3.9"
    sidecar["canonical_audit_note"] = canonical_audit_note
    sidecar["canonical_consistent"] = canonical_consistent
    JSON_OUT.write_text(json.dumps(sidecar, indent=2, sort_keys=True), encoding="utf-8")
    content_sha = sha256_file(JSON_OUT)
    sidecar["content_sha256"] = content_sha
    JSON_OUT.write_text(json.dumps(sidecar, indent=2, sort_keys=True), encoding="utf-8")
    content_sha = sha256_file(JSON_OUT)
    print(f"\n  JSON sidecar: {JSON_OUT.name}")
    print(f"  content_sha256: {content_sha}")
    print(f"  audit_sha256:   {audit_sha}")

    # ----------------------------------------------------- verdict line
    value_field = (
        f"{alpha_s_route_3:.6e}"
        if not np.isnan(alpha_s_route_3)
        else "NaN-regime-breakdown"
    )

    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    schema_v2_row = (
        f"# sign_verdict={sign_verdict} "
        f"magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    existing = VERDICT_OUT.read_text(encoding="utf-8") if VERDICT_OUT.exists() else ""
    if any(line.startswith(GATE_ID + ":") for line in existing.splitlines()):
        print(f"\n  Verdict line for {GATE_ID} already present in {VERDICT_OUT.name}; "
              "skipping append.")
    else:
        with open(VERDICT_OUT, "a", encoding="utf-8") as fh:
            fh.write(canonical_line)
            fh.write(companion_line)
            fh.write(schema_v2_row)
        print(f"\n  Verdict line + companion + schema-v2 row appended to {VERDICT_OUT.name}")

    # 4-tuple final non-verdict line
    print(f"\n  4-tuple: (value={alpha_s_route_3}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
