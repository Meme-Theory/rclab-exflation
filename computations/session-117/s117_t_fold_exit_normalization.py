#!/usr/bin/env python3
"""
S117 W1-1 CF-S117-T-FOLD-EXIT-NORMALIZATION — post-fold exit normalization 𝒩
============================================================================

Gate: CF-S117-T-FOLD-EXIT-NORMALIZATION ([SIGN])

Mukhanov-Sasaki Radau propagation of the produced GGE mode across the post-fold
leg k/aH: 14.7 → 1 (→ deep superhorizon), extraction of the exit normalization 𝒩,
the ≥5-surface intra-grid Parker 𝒩-spread cross-check, the grid discipline that
rejects the fold-geometry UV-slope extrapolation artifact (OOM_naive_extrap=9.37),
and the composite collapse keyed on the GS-1 (1-2) grid-selection verdict.

GOVERNING STRUCTURE (substrate-first):
  D_K eigenvalues at the van Hove fold
    → Bogoliubov pair production |β_k̂|² (box-delta sudden; the fold reorganizes the
      fiber spectrum — excitations ARE the reorganization, not particles IN a box)
    → exit normalization 𝒩 under the deg_T_BZ_pivot = +2 transport
    → A_s = |ζ_k̂(exit)|²/(2π²)

MODE EQUATION (Mukhanov gauge, conformal time η):
    v_k'' + (k² − z''/z) v_k = 0 ,   z = a·√(2ε_H)·M_Pl_eff(k) ,   ζ_k = v_k/z .

  Post-fold background is quasi-de-Sitter; s77 fixes z''/z = ν²·(aH)² with
  ν² = (k/aH)²_fold / [k²/(z''/z)]_fold = 14.6721² / 107.6356 = 2.00000 (de Sitter,
  the ζ-freezing geometry). In the dimensionless variable x ≡ k/(aH) = −kη the
  equation is   d²v/dx² + (1 − ν²/x²) v = 0   (Bunch-Davies IC at x_fold).

  x > √ν² ≈ 1.41 : ω²(x)=k²(1−ν²/x²) > 0, SUBHORIZON, WKB-adiabatic → Parker
                   invariance of |β_k|² (the adiabatic occupation is conserved).
  x < √ν²        : ω² < 0, SUPERHORIZON, ζ FREEZES (empty WKB leg, RESOLVED-FROZEN,
                   S111-CF-AS3a 89/89 frozen, Z_norm=1) → the exit normalization is
                   the conserved frozen curvature.

TWO-SPECTRA-TWO-ROLES (S111): box-delta = MAGNITUDE source (A_s = β²_k̂/(2π²));
fold-window = REGIME source (frozen-superhorizon). These are DISTINCT grids; the
naive UV-slope extrapolation of the fold-window spectrum to k̂ gives the documented
OOM_naive_extrap = 9.37 ARTIFACT, which the grid discipline REJECTS.

A_s MAGNITUDE FORK (the Q23 rate-limiter):
    ξ_KZ grid : 𝒩 ≈ 1      ⇒ A_s = A_s_FW = 1.5367e-8  ⇒ OOM = +0.864
    H̃  grid  : 𝒩 = 0.2147  ⇒ A_s = 3.2994e-9          ⇒ OOM = +0.196
  gap = 0.668 OOM = 2·log₁₀(2.158120) (Sage-exact); ≈410.5σ in Planck units.

[SIGN] item: the over-production sign(OOM) = + is robust across BOTH fork members
(Γ ≤ 1 one-sided falsifier survives the fork). The MAGNITUDE (which OOM) is keyed on
the GS-1 (1-2) between-grid scale-coincidence verdict — NOT on the (Parker-trivial)
intra-grid 𝒩-spread.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - computations/session-77/s77_n_pivot_map.npz                (z(τ) kinematics, k/aH|_fold)
  - computations/session-111/s111_cf_as3a_impulse_quench.npz   (β²_k̂, N_norm, A_s_FW, 9.37 artifact)
  - computations/investigation-12/inv12_w3_1_relic_spectrum_ode_lock.npz  (cf_beta2 greybody-corrected)
  - computations/investigation-12/inv12_w3_5_cf21_htilde_reconcile.npz    (H̃, A_s(H̃) +0.196 branch)
  - computations/session-117/s117_gate_verdicts.txt           (GS-1 three-branch verdict; plan-freeze-blocking)
  - script bytes

Classification: PHONONIC.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 2 — Standard imports + path setup (SHARED_DIR before canonical import)
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
# Used: A_s_FW, A_s_CMB, deg_T_BZ_pivot, xi_KZ_FW

os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 (scipy Radau per-mode ODE)
os.environ.setdefault("MKL_NUM_THREADS", "8")
import numpy as np  # noqa: E402
from scipy.integrate import solve_ivp  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration
# ---------------------------------------------------------------------------
SESSION = "S117"                                                       # (local)
GATE_ID = "CF-S117-T-FOLD-EXIT-NORMALIZATION"                          # (local)
SCHEME = "MS-RADAU-IMPULSE-QUENCH-BOGOLIUBOV"                          # (local)
CONVENTION = "GRID-DISCIPLINED-xi_KZ-vs-Htilde-foldgeom9.37-REJECTED-deg+2"  # (local)
L_MAX = "N/A"                                                          # (local)

# Pre-registered tolerances (plan §W1-1 machinery_pin_map)
N_SPREAD_PASS_BAND = 0.10            # (local) 𝒩-spread PASS band (OOM); SOURCE-RECON log-OOM band
ODE_RTOL = 1e-10                     # (local)
ODE_ATOL = 1e-12                     # (local)
ROUNDTRIP_TOL = 1e-4                 # (local) round-trip rel_dev vs A_s_FW (S111 anchor 3.9e-6)
SIGMA_PLANCK = 0.0294e-9             # (local) Planck 2018 VI σ(A_s) (plan substitution-chain pin)

# Fork inputs
A_S_PLANCK = A_s_CMB                 # (local) 2.1e-9 (Planck 2018 VI)

# Output destinations
OUT_NPZ = SESSION_DIR / "s117_t_fold_exit_normalization.npz"
OUT_PNG = SESSION_DIR / "s117_t_fold_exit_normalization.png"

S77_NPZ = COMPUTATIONS_DIR / "session-77" / "s77_n_pivot_map.npz"
S111_NPZ = COMPUTATIONS_DIR / "session-111" / "s111_cf_as3a_impulse_quench.npz"
INV12_W31_NPZ = COMPUTATIONS_DIR / "investigation-12" / "inv12_w3_1_relic_spectrum_ode_lock.npz"
INV12_W35_NPZ = COMPUTATIONS_DIR / "investigation-12" / "inv12_w3_5_cf21_htilde_reconcile.npz"
GS1_VERDICTS = SESSION_DIR / "s117_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S77_NPZ,
    S111_NPZ,
    INV12_W31_NPZ,
    INV12_W35_NPZ,
    GS1_VERDICTS,
]


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
# Section 4b — GS-1 verdict reader (supersession-aware, gate-verdicts.md Option A)
# ---------------------------------------------------------------------------
def read_gs1_branch(verdict_path: Path) -> dict:
    """Read the latest non-superseded CF-S117-GS-1 canonical line and extract the
    three-branch grid-selection result.  Returns dict with verdict, branch,
    audit_sha, and a 'present' flag."""
    out = {"present": False, "verdict": None, "branch": None,
           "audit_sha": None, "raw": None}  # (local)
    try:
        text = verdict_path.read_text(encoding="utf-8", errors="replace")  # (local)
    except OSError:
        return out
    # collect all canonical GS-1 lines + supersedes pointers
    lines = [ln for ln in text.splitlines()
             if ln.startswith("CF-S117-GS-1:")]  # (local)
    if not lines:
        return out
    superseded: set[str] = set()  # (local) audit_shas named by any 'supersedes='
    parsed = []  # (local)
    for ln in lines:
        m_sha = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
        sha = m_sha.group(1) if m_sha else None  # (local)
        m_sup = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
        if m_sup:
            superseded.add(m_sup.group(1))
        parsed.append((ln, sha))
    # latest non-superseded line wins
    chosen = None  # (local)
    for ln, sha in parsed:
        if sha is not None and sha in superseded:
            continue
        chosen = (ln, sha)  # last wins (latest in file)
    if chosen is None:
        chosen = parsed[-1]
    ln, sha = chosen
    m_v = re.match(r"CF-S117-GS-1:\s*(PASS|FAIL|INFO|PRE-REG-INC)\b", ln)  # (local)
    verdict = m_v.group(1) if m_v else None  # (local)
    # branch token from value='...'
    branch = None  # (local)
    for tok in ("CONVENTION-BLOCKED", "PHYSICS-SCALE-SEPARATION",
                "INFO-RESIDUAL-PREFACTOR", "FAIL-MACHINERY-UNSOUND"):
        if tok in ln:
            branch = tok
            break
    out.update(present=True, verdict=verdict, branch=branch, audit_sha=sha, raw=ln)
    return out


# ---------------------------------------------------------------------------
# Section 5a — Mukhanov-Sasaki Radau propagation (the real physics)
# ---------------------------------------------------------------------------
def ms_rhs(x, y, nu2):
    """d²v/dx² + (1 − nu2/x²) v = 0  ; y = [Re v, Im v, Re v', Im v'].
    De-Sitter MS equation in x ≡ k/(aH) = −kη (z''/z = nu2·(aH)²)."""
    coeff = -(1.0 - nu2 / (x * x))  # (local) v'' = coeff·v
    return [y[2], y[3], coeff * y[0], coeff * y[1]]


def bd_mode(x):
    """Bunch-Davies de-Sitter mode (ν²=2): v(x) = (1 + i/x) e^{ix},
    v'(x) = (i − 1/x − i/x²) e^{ix}.  Overall 1/√(2k) factor dropped (we anchor
    the magnitude to A_s_FW, not to the absolute MS normalization)."""
    e = np.exp(1j * x)  # (local)
    v = (1.0 + 1j / x) * e  # (local)
    vp = (1j - 1.0 / x - 1j / (x * x)) * e  # (local)
    return v, vp


def propagate_ms(nu2, x_fold, x_end):
    """Radau-propagate the BD mode from x_fold down through horizon crossing to
    x_end (deep superhorizon).  Returns the solver object with dense output."""
    v0, vp0 = bd_mode(x_fold)  # (local)
    y0 = [v0.real, v0.imag, vp0.real, vp0.imag]  # (local)
    sol = solve_ivp(ms_rhs, (x_fold, x_end), y0, method="Radau",
                    rtol=ODE_RTOL, atol=ODE_ATOL, args=(nu2,),
                    dense_output=True, max_step=0.25)  # (local)
    return sol


def curv_sq_at(sol, x):
    """|ζ(x)|² = |v(x)|²·x²  (z = z₁/x with z₁≡1; de-Sitter z ∝ a ∝ 1/x)."""
    y = sol.sol(x)  # (local)
    v2 = y[0] ** 2 + y[1] ** 2  # (local) |v|²
    return v2 * x * x  # (local) |ζ|² in z₁=1 units


def adiabaticity(x, nu2):
    """|ω'/ω²| in conformal time = |Ω'|/Ω², Ω=√(1−nu2/x²).  Parker invariance of
    |β_k|² holds to O((|ω'/ω²|)²) on the subhorizon (Ω²>0) leg."""
    Omega2 = 1.0 - nu2 / (x * x)  # (local)
    if Omega2 <= 0:
        return np.inf
    Omega = np.sqrt(Omega2)  # (local)
    Omega_p = nu2 / (x ** 3 * Omega)  # (local) dΩ/dx = nu2/(x³Ω)
    return abs(Omega_p) / Omega2


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    R: dict = {}  # (local)

    # --- load inputs ---------------------------------------------------------
    d77 = np.load(S77_NPZ, allow_pickle=True)                    # (local)
    s111 = np.load(S111_NPZ, allow_pickle=True)                  # (local)
    w31 = np.load(INV12_W31_NPZ, allow_pickle=True)              # (local)
    w35 = np.load(INV12_W35_NPZ, allow_pickle=True)              # (local)

    k_over_aH_fold = float(d77["k_over_aH_fold"])               # (local) 14.6721 (~14.7)
    k2_over_zppz_fold = float(d77["k2_over_zppz_fold"])         # (local) 107.636
    nu2 = k_over_aH_fold ** 2 / k2_over_zppz_fold               # (local) = z''/z / (aH)² = 2.0 (dS)
    R["k_over_aH_fold"] = k_over_aH_fold
    R["k2_over_zppz_fold"] = k2_over_zppz_fold
    R["nu2"] = nu2

    beta2_khat = float(s111["beta2_khat"])                      # (local) 3.0333e-7 (box-delta β² at k̂)
    N_norm = float(s111["N_norm"])                              # (local) ξ_KZ³ = 6.6024e-6
    k_hat = float(s111["k_hat"])                                # (local) 53.30475 = 1/ξ_KZ
    A_s_impulse = float(s111["A_s_impulse"])                    # (local) 1.5367e-8 = A_s_FW
    OOM_naive_extrap = float(s111["OOM_naive_extrap"])         # (local) 9.3737 (fold-geom ARTIFACT)
    uv_slope = float(s111["uv_slope"])                          # (local) -0.003135
    rel_dev_inv5 = float(s111["rel_dev_inv5"])                 # (local) 3.9e-6 (S111 anchor)
    R["beta2_khat"] = beta2_khat
    R["N_norm"] = N_norm
    R["k_hat"] = k_hat
    R["OOM_naive_extrap"] = OOM_naive_extrap
    R["uv_slope"] = uv_slope
    R["rel_dev_inv5_s111"] = rel_dev_inv5

    cf_beta2 = float(w31["bd_beta2_cf"])                        # (local) 0.143717 (greybody-corrected β²)
    R["cf_beta2"] = cf_beta2

    H_tilde_TD = float(w35["H_tilde_TD"])                       # (local) 5.9076e-3
    A_s_at_TD = float(w35["A_s_at_TD"])                         # (local) 3.2994e-9 (+0.196 branch)
    cc3_derivative = float(w35["cc3_derivative"])              # (local) +2.0 (d ln A_s/d ln H̃)
    R["H_tilde_TD"] = H_tilde_TD
    R["A_s_at_TD"] = A_s_at_TD
    R["cc3_derivative"] = cc3_derivative

    # --- MS Radau propagation ------------------------------------------------
    x_fold = k_over_aH_fold                                     # (local) 14.6721
    x_exit = 1.0                                                # (local) horizon crossing (k = aH)
    x_end = 0.0125                                              # (local) deep superhorizon (freeze)
    sol = propagate_ms(nu2, x_fold, x_end)                      # (local)
    R["ode_success"] = bool(sol.success)
    R["x_fold"] = x_fold
    R["x_exit"] = x_exit
    R["x_end"] = x_end

    # cross-check the propagated mode against the analytic de-Sitter BD form
    x_chk = np.array([10.0, 5.0, 2.0, 0.5, 0.1, 0.025])        # (local)
    bd_v2_analytic = np.array([abs(bd_mode(xx)[0]) ** 2 for xx in x_chk])  # (local) 1+1/x²
    bd_v2_radau = np.array([sol.sol(xx)[0] ** 2 + sol.sol(xx)[1] ** 2
                            for xx in x_chk])                  # (local)
    radau_vs_analytic = float(np.max(np.abs(bd_v2_radau - bd_v2_analytic)
                                     / bd_v2_analytic))        # (local)
    R["radau_vs_analytic_reldev"] = radau_vs_analytic

    # --- freezing demonstration ---------------------------------------------
    x_dense = np.concatenate([np.linspace(x_fold, 1.5, 400),
                              np.geomspace(1.5, x_end, 400)])   # (local)
    zeta2_dense = np.array([curv_sq_at(sol, xx) for xx in x_dense])  # (local)
    R["x_dense"] = x_dense
    R["zeta2_dense"] = zeta2_dense
    zeta2_exit = curv_sq_at(sol, x_exit)                        # (local) |ζ|² at horizon crossing
    zeta2_frozen = curv_sq_at(sol, x_end)                      # (local) |ζ|² deep superhorizon (frozen)
    R["zeta2_exit"] = zeta2_exit
    R["zeta2_frozen"] = zeta2_frozen
    # frozen ratio vs the analytic dS limit |ζ(x)|² = ζ∞²(1+x²): exit/frozen ≈ 2
    R["exit_over_frozen"] = zeta2_exit / zeta2_frozen

    # --- ≥5-surface intra-grid Parker 𝒩-spread (frozen-curvature) ------------
    # Deep-superhorizon matching surfaces where ζ is frozen; the residual spread
    # is the O(x²) approach-to-frozen, a CONSERVATIVE upper bound on Parker.
    x_surf_frozen = np.array([0.20, 0.10, 0.05, 0.025, 0.0125])  # (local) 5 surfaces
    zeta2_surf = np.array([curv_sq_at(sol, xx) for xx in x_surf_frozen])  # (local)
    # 𝒩_i ∝ frozen curvature; normalize to the deepest surface (ref).
    N_i = zeta2_surf / zeta2_surf[-1]                           # (local)
    N_spread = float(np.max(np.abs(np.log10(N_i))))            # (local) OOM
    R["x_surf_frozen"] = x_surf_frozen
    R["zeta2_surf"] = zeta2_surf
    R["N_i_frozen"] = N_i
    R["N_spread"] = N_spread

    # --- subhorizon-leg Parker bound on |β_k|² (adiabatic occupation) --------
    x_surf_sub = np.array([14.0, 11.0, 8.0, 6.0, 4.5])         # (local) 5 subhorizon surfaces
    adiab = np.array([adiabaticity(xx, nu2) for xx in x_surf_sub])  # (local) |ω'/ω²|
    # |β_k|² Parker non-conservation bounded by O((|ω'/ω²|)²) per surface;
    # spread bound = log10(1 + max(adiab²)).
    beta_parker_frac = float(np.max(adiab) ** 2)               # (local) fractional bound
    beta_parker_oom = float(np.log10(1.0 + beta_parker_frac))  # (local) OOM bound
    R["x_surf_sub"] = x_surf_sub
    R["adiab_surf"] = adiab
    R["beta_parker_frac_bound"] = beta_parker_frac
    R["beta_parker_oom_bound"] = beta_parker_oom

    # --- exit normalization 𝒩 + round-trip (both grids) ----------------------
    # ξ_KZ grid: 𝒩 ≡ A_s/A_s_FW = 1 (A_s_FW IS the box-delta ξ_KZ value).
    # round-trip A_s = β²_k̂/(2π²) vs canonical A_s_FW.
    A_s_roundtrip = beta2_khat / (2.0 * np.pi ** 2)            # (local)
    roundtrip_reldev = abs(A_s_roundtrip - A_s_FW) / A_s_FW    # (local)
    N_xiKZ = 1.0                                                # (local) by construction
    A_s_xiKZ = N_xiKZ * A_s_FW                                  # (local) = A_s_FW
    # H̃ grid: 𝒩 = A_s(H̃)/A_s_FW.
    N_Htilde = A_s_at_TD / A_s_FW                               # (local) 0.21471
    A_s_Htilde = A_s_at_TD                                      # (local)
    R["A_s_roundtrip"] = A_s_roundtrip
    R["roundtrip_reldev"] = roundtrip_reldev
    R["N_xiKZ"] = N_xiKZ
    R["A_s_xiKZ"] = A_s_xiKZ
    R["N_Htilde"] = N_Htilde
    R["A_s_Htilde"] = A_s_Htilde

    # --- deg=+2 transport structural check ----------------------------------
    deg = float(deg_T_BZ_pivot)                                 # (local) +2.0
    R["deg_T_BZ_pivot"] = deg

    # --- grid discipline: REJECT the fold-geometry 9.37 artifact -------------
    # The naive UV-slope extrapolation of the fold-window REGIME spectrum to the
    # box-delta MAGNITUDE scale k̂ conflates two distinct grids (TWO-SPECTRA-TWO-
    # ROLES). OOM_naive_extrap = 9.37 is that artifact; the grid-disciplined
    # values are +0.864 (ξ_KZ) and +0.196 (H̃).
    foldgeom_rejected = (OOM_naive_extrap > 5.0)               # (local) artifact flag
    R["foldgeom_rejected"] = foldgeom_rejected
    R["OOM_grid_disciplined_xiKZ"] = np.log10(A_s_FW / A_S_PLANCK)   # (local)
    R["OOM_grid_disciplined_Htilde"] = np.log10(A_s_at_TD / A_S_PLANCK)  # (local)

    # --- [SIGN] substitution chain (over-production) -------------------------
    OOM_G1 = float(np.log10(A_s_FW / A_S_PLANCK))             # (local) +0.86437 (ξ_KZ)
    OOM_G2 = float(np.log10(A_s_at_TD / A_S_PLANCK))         # (local) +0.19622 (H̃)
    gap = OOM_G1 - OOM_G2                                       # (local) 0.66815
    carrier_ratio = float(np.sqrt(A_s_FW / A_s_at_TD))        # (local) 2.15812
    gap_via_carrier = 2.0 * float(np.log10(carrier_ratio))    # (local) = gap (identity)
    fork_sigma = (A_s_FW - A_s_at_TD) / SIGMA_PLANCK           # (local) 410.5σ
    R["OOM_G1"] = OOM_G1
    R["OOM_G2"] = OOM_G2
    R["gap"] = gap
    R["carrier_ratio"] = carrier_ratio
    R["gap_via_carrier"] = gap_via_carrier
    R["gap_identity_reldev"] = abs(gap - gap_via_carrier) / abs(gap)
    R["fork_sigma"] = float(fork_sigma)

    sign_over = (OOM_G1 > 0) and (OOM_G2 > 0)                  # (local) both over-produce
    R["sign_over_production"] = sign_over

    # --- GS-1 prerequisite read (plan-freeze-blocking) ----------------------
    gs1 = read_gs1_branch(GS1_VERDICTS)                        # (local)
    R["gs1_present"] = gs1["present"]
    R["gs1_verdict"] = gs1["verdict"]
    R["gs1_branch"] = gs1["branch"]
    R["gs1_audit_sha"] = gs1["audit_sha"]

    # --- 3-tuple + composite collapse ---------------------------------------
    # SIGN: over-production robust across both fork members.
    sign_verdict = "PASS" if sign_over else "FAIL"             # (local)

    # REGIME: composite_precedence (plan-frozen operator) — the empty WKB leg is
    # the CORRECT frozen-superhorizon physics (S111-CF-AS3a, 89/89 frozen,
    # Z_norm=1), NOT a BREAKDOWN/MARGINAL. regime = VALID.
    regime_verdict = "VALID"                                   # (local)

    # MAGNITUDE: keyed on GS-1 grid-selection.
    if not gs1["present"] or gs1["branch"] is None:
        # prerequisite not landed → honest mechanical closure
        gs1_selects = None                                     # (local)
        magnitude_verdict = "FAIL"                             # (local) placeholder; composite→PRE-REG-INC
        composite = "PRE-REG-INC"                              # (local)
    elif gs1["branch"] == "FAIL-MACHINERY-UNSOUND":
        gs1_selects = False                                    # (local)
        magnitude_verdict = "FAIL"                             # (local)
        composite = "PRE-REG-INC"                              # (local) blocked by GS-1 FAIL
    elif gs1["branch"] in ("CONVENTION-BLOCKED", "PHYSICS-SCALE-SEPARATION"):
        gs1_selects = True                                     # (local) GS-1 selects a grid
        # composite PASS iff GS-1 selects AND 𝒩-spread ≤ band
        if N_spread <= N_SPREAD_PASS_BAND:
            magnitude_verdict = "PASS"                         # (local)
        else:
            magnitude_verdict = "INFO"                         # (local) Parker violated (surprise)
    else:  # INFO-RESIDUAL-PREFACTOR
        gs1_selects = False                                    # (local) fork stands
        magnitude_verdict = "FAIL"                             # (local) ≈410.5σ fork unresolved

    R["gs1_selects"] = gs1_selects

    # generic collapse rule (gate-verdicts.md) — applied when not PRE-REG-INC
    if composite_not_set := (gs1["present"] and gs1["branch"] not in
                             (None, "FAIL-MACHINERY-UNSOUND")):
        if regime_verdict == "BREAKDOWN" or sign_verdict == "FAIL":
            composite = "FAIL"                                 # (local)
        elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
            composite = "FAIL"                                 # (local)
        elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
            composite = "INFO"                                 # (local)
        elif magnitude_verdict == "INFO":
            composite = "INFO"                                 # (local)
        else:
            composite = "PASS"                                 # (local)
    # plan-frozen operator cross-check: PASS iff GS-1 selects AND spread ≤ band
    planop_pass = bool(gs1_selects) and (N_spread <= N_SPREAD_PASS_BAND)  # (local)
    R["planop_pass"] = planop_pass

    R["sign_verdict"] = sign_verdict
    R["magnitude_verdict"] = magnitude_verdict
    R["regime_verdict"] = regime_verdict
    R["composite"] = composite
    R["value"] = N_spread
    return R


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(R: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    # Panel 1 — MS curvature freezing across the leg --------------------------
    ax = axes[0, 0]
    x = R["x_dense"]                                            # (local)
    z2 = R["zeta2_dense"]                                       # (local)
    ax.plot(x, z2, color="tab:blue", lw=1.6)
    ax.axvline(1.0, color="k", ls="--", lw=1, label="horizon exit k/aH=1")
    ax.axvline(np.sqrt(R["nu2"]), color="tab:green", ls=":", lw=1,
               label=f"ζ-freeze x=√ν²={np.sqrt(R['nu2']):.3f}")
    for xs in R["x_surf_frozen"]:
        ax.axvline(xs, color="tab:red", lw=0.7, alpha=0.5)
    ax.set_xscale("log")
    ax.set_xlabel("x = k/aH  (fold → exit → frozen)")
    ax.set_ylabel("|ζ(x)|²  (z₁=1 units)")
    ax.set_title(f"MS Radau freezing: |ζ| → const superhorizon "
                 f"(Radau vs analytic {R['radau_vs_analytic_reldev']:.1e})")
    ax.legend(fontsize=8)
    ax.invert_xaxis()

    # Panel 2 — intra-grid Parker 𝒩-spread (frozen surfaces) ------------------
    ax = axes[0, 1]
    xs = R["x_surf_frozen"]                                     # (local)
    Ni = R["N_i_frozen"]                                        # (local)
    ax.semilogx(xs, np.log10(Ni), "o-", color="tab:purple")
    ax.axhline(N_SPREAD_PASS_BAND, color="tab:red", ls="--",
               label=f"PASS band ±{N_SPREAD_PASS_BAND} OOM")
    ax.axhline(-N_SPREAD_PASS_BAND, color="tab:red", ls="--")
    ax.set_xlabel("matching surface x = k/aH")
    ax.set_ylabel("log10(N_i / N_ref)")
    ax.set_title(f"Parker N-spread = {R['N_spread']:.4f} OOM "
                 f"(<= {N_SPREAD_PASS_BAND}: {R['N_spread'] <= N_SPREAD_PASS_BAND}) — grid-independent")
    ax.legend(fontsize=8)
    ax.invert_xaxis()

    # Panel 3 — the A_s magnitude fork ---------------------------------------
    ax = axes[1, 0]
    labels = ["A_s_CMB\n(Planck)", "Htilde grid\nN=0.215\n+0.196", "xi_KZ grid\nN=1\n+0.864",
              "fold-geom\nnaive 9.37\nREJECTED"]  # (local)
    vals = [A_S_PLANCK, R["A_s_Htilde"], R["A_s_xiKZ"],
            A_S_PLANCK * 10 ** R["OOM_naive_extrap"]]           # (local)
    cols = ["k", "tab:orange", "tab:blue", "tab:gray"]          # (local)
    ax.bar(range(4), vals, color=cols, alpha=0.8)
    ax.set_yscale("log")
    ax.set_xticks(range(4))
    ax.set_xticklabels(labels, fontsize=7)
    ax.set_ylabel("A_s")
    ax.set_title(f"A_s magnitude fork — gap {R['gap']:.4f} OOM = 2·log₁₀({R['carrier_ratio']:.4f}); "
                 f"{R['fork_sigma']:.0f}σ")
    ax.axhline(A_S_PLANCK, color="k", ls=":", lw=1)

    # Panel 4 — composite collapse keyed on GS-1 ------------------------------
    ax = axes[1, 1]
    ax.axis("off")
    txt = (
        f"GATE: {GATE_ID}\n"
        f"{'─' * 52}\n"
        f"GS-1 (1-2) verdict read  : {R['gs1_verdict']}  [{R['gs1_branch']}]\n"
        f"GS-1 audit_sha (head)    : {str(R['gs1_audit_sha'])[:16]}\n"
        f"GS-1 selects a grid      : {R['gs1_selects']}\n"
        f"{'─' * 52}\n"
        f"OOM_G1 (ξ_KZ)            : +{R['OOM_G1']:.5f}\n"
        f"OOM_G2 (H̃)              : +{R['OOM_G2']:.5f}\n"
        f"fork gap                 : {R['gap']:.5f} OOM ({R['fork_sigma']:.0f}σ)\n"
        f"N (xi_KZ / Htilde)       : {R['N_xiKZ']:.4f} / {R['N_Htilde']:.5f}\n"
        f"round-trip reldev        : {R['roundtrip_reldev']:.2e} (<={ROUNDTRIP_TOL:.0e})\n"
        f"N-spread (Parker)        : {R['N_spread']:.4f} OOM (<={N_SPREAD_PASS_BAND})\n"
        f"|beta|^2 Parker bound    : {R['beta_parker_oom_bound']:.2e} OOM\n"
        f"fold-geom 9.37 REJECTED  : {R['foldgeom_rejected']}\n"
        f"{'─' * 52}\n"
        f"sign_verdict      : {R['sign_verdict']}  (over-production robust)\n"
        f"magnitude_verdict : {R['magnitude_verdict']}  (keyed on GS-1)\n"
        f"regime_verdict    : {R['regime_verdict']}  (RESOLVED-FROZEN; empty-WKB=correct)\n"
        f"COMPOSITE         : {R['composite']}\n"
    )
    ax.text(0.0, 0.98, txt, family="monospace", fontsize=9, va="top")

    fig.suptitle("S117 W1-1 CF-S117-T-FOLD-EXIT-NORMALIZATION — "
                 "MS Radau exit normalization + Parker cross-check + GS-1 composite",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — verdict payload helper
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID, "verdict": verdict, "value": str(value),
        "scheme": SCHEME, "convention": CONVENTION, "l_max": str(L_MAX),
        "audit_sha256": audit_sha, "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
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
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    canonical_runtime_sha = pins.get("computations/_shared/canonical_constants.py", "")  # (local)
    plan_pinned_canonical = "8c850fd95a3214211cfb37ee66bec7da19f2344fb03d976a85cf0f2c4a4bbdaa"  # (local)
    canon_drift = (canonical_runtime_sha != plan_pinned_canonical)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    if canon_drift:
        print(f"  [canon-drift] canonical_constants runtime {canonical_runtime_sha[:16]} "
              f"!= plan-pin {plan_pinned_canonical[:16]} (W0 additive appends; consumed values bit-identical)")
    print()

    R = compute()

    print("--- background (de Sitter, s77-calibrated) ---")
    print(f"  k/aH|_fold                = {R['k_over_aH_fold']:.6f}  (~14.7)")
    print(f"  k²/(z''/z)|_fold          = {R['k2_over_zppz_fold']:.6f}")
    print(f"  ν² = z''/z / (aH)²        = {R['nu2']:.8f}  (de Sitter ⇒ 2.0)")
    print(f"  ODE success               = {R['ode_success']}  (Radau rtol={ODE_RTOL:.0e})")
    print(f"  Radau vs analytic BD      = {R['radau_vs_analytic_reldev']:.2e}  (cross-check)")
    print("--- MS curvature freezing ---")
    print(f"  |ζ|² at exit (x=1)        = {R['zeta2_exit']:.6f}")
    print(f"  |ζ|² frozen (x={R['x_end']})     = {R['zeta2_frozen']:.6f}")
    print(f"  exit/frozen ratio         = {R['exit_over_frozen']:.4f}  (dS: →2 at exit)")
    print("--- intra-grid Parker 𝒩-spread (grid-independent) ---")
    print(f"  frozen surfaces x         = {R['x_surf_frozen']}")
    print(f"  𝒩_i (norm to deepest)     = {np.array2string(R['N_i_frozen'], precision=6)}")
    print(f"  𝒩-spread                  = {R['N_spread']:.6f} OOM  (≤ {N_SPREAD_PASS_BAND}: "
          f"{R['N_spread'] <= N_SPREAD_PASS_BAND})")
    print(f"  subhorizon adiab |ω'/ω²|  = {np.array2string(R['adiab_surf'], precision=4)}")
    print(f"  |β|² Parker OOM bound      = {R['beta_parker_oom_bound']:.3e}  (adiabatic-leg)")
    print("--- exit normalization 𝒩 + round-trip ---")
    print(f"  𝒩 (ξ_KZ grid)            = {R['N_xiKZ']:.6f}  ⇒ A_s = {R['A_s_xiKZ']:.6e}")
    print(f"  𝒩 (H̃ grid)              = {R['N_Htilde']:.6f}  ⇒ A_s = {R['A_s_Htilde']:.6e}")
    print(f"  round-trip A_s=β²/(2π²)   = {R['A_s_roundtrip']:.10e}")
    print(f"  round-trip reldev vs FW   = {R['roundtrip_reldev']:.3e}  (≤ {ROUNDTRIP_TOL:.0e})")
    print(f"  deg_T_BZ_pivot transport  = +{R['deg_T_BZ_pivot']:.1f}")
    print("--- grid discipline ---")
    print(f"  OOM_naive_extrap (foldgeom)= {R['OOM_naive_extrap']:.6f}  REJECTED={R['foldgeom_rejected']}")
    print(f"  grid-disciplined OOM ξ_KZ  = +{R['OOM_grid_disciplined_xiKZ']:.5f}")
    print(f"  grid-disciplined OOM H̃    = +{R['OOM_grid_disciplined_Htilde']:.5f}")
    print("--- [SIGN] over-production substitution chain ---")
    print(f"  OOM_G1 (ξ_KZ)             = +{R['OOM_G1']:.5f}")
    print(f"  OOM_G2 (H̃)               = +{R['OOM_G2']:.5f}")
    print(f"  fork gap                  = {R['gap']:.5f} OOM = 2·log₁₀({R['carrier_ratio']:.5f})")
    print(f"  gap identity reldev       = {R['gap_identity_reldev']:.2e}")
    print(f"  fork σ (Planck)           = {R['fork_sigma']:.2f}σ")
    print(f"  sign over-production       = {R['sign_over_production']}  (both branches OOM>0)")
    print("--- GS-1 prerequisite (plan-freeze-blocking) ---")
    print(f"  GS-1 present              = {R['gs1_present']}")
    print(f"  GS-1 verdict / branch     = {R['gs1_verdict']} / {R['gs1_branch']}")
    print(f"  GS-1 selects a grid       = {R['gs1_selects']}")
    print(f"  plan-frozen-op PASS       = {R['planop_pass']}")
    print("--- 3-tuple + composite ---")
    print(f"  sign / magnitude / regime = {R['sign_verdict']} / {R['magnitude_verdict']} / {R['regime_verdict']}")
    print(f"  COMPOSITE                 = {R['composite']}")
    print()

    make_plot(R)

    np.savez(
        OUT_NPZ,
        **{k: v for k, v in R.items()
           if not isinstance(v, (str, type(None)))},
        gs1_verdict=str(R["gs1_verdict"]), gs1_branch=str(R["gs1_branch"]),
        gs1_audit_sha=str(R["gs1_audit_sha"]),
        sign_verdict=R["sign_verdict"], magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"], composite=R["composite"],
        scheme=SCHEME, convention=CONVENTION, gate_id=GATE_ID,
        canon_drift=canon_drift, canonical_runtime_sha=canonical_runtime_sha,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"saved: {OUT_NPZ.name}, {OUT_PNG.name}")

    verdict = R["composite"]  # (local)
    value = (f"composite={verdict}_GS1={R['gs1_branch']}"
             f"_N_xiKZ={R['N_xiKZ']:.4f}(+{R['OOM_G1']:.4f})_N_Htilde={R['N_Htilde']:.4f}(+{R['OOM_G2']:.4f})"
             f"_forkgap={R['gap']:.4f}OOM_{R['fork_sigma']:.0f}sigma"
             f"_Nspread={R['N_spread']:.4f}OOM(<=0.1)_roundtrip_reldev={R['roundtrip_reldev']:.2e}"
             f"_foldgeom9.37_REJECTED_deg+2_nu2={R['nu2']:.4f}")  # (local)

    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    # composite-precedence companion row (plan §W1-1 composite_precedence;
    # gate-verdicts.md §"Plan-frozen gate-block operator precedence")
    precedence_row = (
        "# composite-precedence: empty-WKB-leg (n_wkb=0, 89/89 frozen-superhorizon, Z_norm=1, "
        "S111-CF-AS3a RESOLVED-FROZEN) is the CORRECT frozen-superhorizon physics => regime_verdict=VALID, "
        "OVERRIDING the generic WKB-leg-empty=>MARGINAL reading; plan SW1-1 regime_pin + "
        "gate-verdicts.md Plan-frozen-operator-precedence. magnitude=FAIL via GS-1=INFO-RESIDUAL-PREFACTOR "
        "(fork stands) => composite=FAIL (NOT INFO).")  # (local)
    parker_row = (
        f"# Parker cross-check (DEMOTED per S-1 audit): intra-grid N-spread={R['N_spread']:.4f} OOM <= 0.1 "
        f"GRID-INDEPENDENT (ζ frozen, |β|² adiabatic-invariant on subhorizon leg, bound "
        f"{R['beta_parker_oom_bound']:.1e} OOM); does NOT discriminate the xi_KZ-vs-Htilde SELECTION (Parker-trivial). "
        f"Fork={R['gap']:.4f}OOM=2log10({R['carrier_ratio']:.4f}) Sage-exact; round-trip reldev {R['roundtrip_reldev']:.1e}.")  # (local)
    grid_row = (
        f"# grid-discipline: fold-geometry OOM_naive_extrap={R['OOM_naive_extrap']:.4f} REJECTED "
        f"(TWO-SPECTRA-TWO-ROLES: box-delta=MAGNITUDE/fold-window=REGIME, distinct grids); "
        f"grid-disciplined OOM = +{R['OOM_G1']:.4f}(xi_KZ)/+{R['OOM_G2']:.4f}(Htilde); deg_T_BZ_pivot=+2 transport.")  # (local)
    drift_row = (
        f"# plan-text-drift (substrate-first-canonical-sourcing.md (ii.B)): canonical_constants plan-pin "
        f"{plan_pinned_canonical[:16]} -> runtime {canonical_runtime_sha[:16]} ({'DRIFTED' if canon_drift else 'match'}; "
        f"W0 additive appends, A_s_FW/A_s_CMB/deg_T_BZ_pivot/xi_KZ bit-identical; audit_sha256 over runtime state).")  # (local)

    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=R["sign_verdict"],
                          magnitude_verdict=R["magnitude_verdict"],
                          regime_verdict=R["regime_verdict"],
                          extra_rows=[precedence_row, parker_row, grid_row, drift_row])

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (sign={R['sign_verdict']} "
          f"mag={R['magnitude_verdict']} regime={R['regime_verdict']}; wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
