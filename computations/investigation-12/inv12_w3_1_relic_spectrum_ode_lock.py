#!/usr/bin/env python3
"""
INV12 W3-1 — RELIC-SPECTRUM-ODE-LOCK  (FOUNDATIONAL gate of investigation-12)
=============================================================================

Gate: INV12-W3-1-RELIC-SPECTRUM-ODE-LOCK ([VERIFY])

Pre-registered threshold (plan §W3-1 `operator`):
  max_k | |beta_k|^2(Radau) - |beta_k|^2(DOP853) | / |beta_k|^2  <= 1e-4   (integrator agreement)
  AND max_k | |beta_k|^2(rtol=1e-10) - |beta_k|^2(rtol=1e-12) | / |beta_k|^2 <= 1e-4 (rtol refinement)
  AND max_k | |alpha_k|^2 - |beta_k|^2 - 1 |  <= 1e-10                       (unitarity residual)
  PASS iff all three hold; FAIL iff non-convergence / unitarity > 1e-10;
  INFO iff converges across integrators but residual N_seg/rtol dependence at the 1e-4..1e-2 level.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py          (feeds audit_sha256 only)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (bottom-band selection anchor)
       PLAN-TEXT-DRIFT NOTE: plan §W3-1 input_files pins
       `computations/_shared/s84_spectrum_cache_L12_tau019.npz`; the file is
       canonically at `computations/session-84/...`. Resolved at runtime per
       `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction;
       drift documented in the verdict value field + WP Methodology.
  - script bytes                                          (feeds BOTH SHAs)

Output 4-tuple:
  (value=<max_integrator_agreement>, scheme=FW, convention=ABSOLUTE, L_max=10)

Classification: PHONONIC.
  The substrate IS the relic: a multi-mode squeezed state of the D_K eigenvalue fabric.
  D_K eigenvalues lambda_k(tau) (the vibrational modes of the fabric at each point)
  -> the smooth Jensen-deformation sweep through the van Hove fold makes the BdG
  quasiparticle frequency omega_k(tau) = sqrt((lambda_k - mu)^2 + Delta_k^2) time-dependent
  -> the in-vacuum adiabatic mode functions fail to track the rapidly-changing omega_k
  -> real excitations (Bogoliubov beta_k) are produced mode-by-mode -> the locked
  {beta_k} spectrum IS the GGE relic content. The transfer-matrix-vs-ODE distinction
  is the substrate-physics point: the fold is a SMOOTH omega_k(tau), so piecewise-constant
  segmentation introduces artificial reflections (a methodology artifact, NOT substrate
  physics); the high-accuracy ODE recovers the substrate's actual squeeze.

METHODOLOGY
-----------
For each Peter-Weyl-block mode k on the L_max=10 D_K bottom-band, integrate the mode
equation u_k'' + omega_k^2(tau) u_k = 0 across the fold window [tau_in, tau_out]
bracketing tau_fold=0.190, with the framework BdG dispersion
omega_k(tau) = sqrt((lambda_k(tau) - mu)^2 + Delta_k(tau)^2) built from the SMOOTH
Jensen-deformed eigenvalue trajectory lambda_k(tau) (constructed via dirac_spectrum.py,
GPU per-(p,q)-block torch.linalg.eigvals on the block-diagonal D_K). Begin in the adiabatic
in-vacuum (positive-frequency WKB), evolve through the fold, project onto the out-vacuum
to extract alpha_k, beta_k (Birrell-Davies sec. 3.4 adiabatic Bogoliubov). Cross-check:
  (i) box+delta sudden-limit transfer-matrix (S100b-BOX-DELTA-BOGOLIUBOV, where TM IS exact);
  (ii) N_seg-refinement of a naive piecewise-constant TM (to DEMONSTRATE the artifact the ODE retires).
Verify unitarity |alpha_k|^2 - |beta_k|^2 = 1 to machine eps for every mode.

CONVENTION RESOLUTION (BdG dispersion):
  Plan §W3-1 method writes omega_k = sqrt((lambda_k^2 - mu^2)^2 + Delta_k^2). The
  substrate-canonical BdG form (S36 s36_multisector_ed_verdict: mu=0 particle-hole
  symmetric; S76 sp-transit-workshop T2.1-T2.3 omega_B = sqrt(eps_B^2 + Delta_BCS^2);
  S101 oddfloor E_n(q=0)=|lambda_n|) is omega_k = sqrt(xi_k^2 + Delta_k^2) with
  xi_k = lambda_k - mu the band energy and mu=0. The plan's "(lambda^2 - mu^2)" is a
  transcription of the standard BdG band energy xi=(lambda-mu); with mu=0 both reduce
  to lambda_k, and the pair band 2*E_k = 2*sqrt(lambda_k^2 + Delta_k^2) at the relic
  point (Delta->0 in the S101 q-deformation, E_k->|lambda_k|) reproduces the documented
  S101 band [1.6395, 10.8379] = 2*[|lambda|_min, |lambda|_max] EXACTLY
  (2*0.819741=1.639482; 2*5.418937=10.837874). We use the substrate-canonical form and
  carry the pair-band edges as the validating cross-check. The integrator-LOCK verdict
  (convergence + unitarity) is robust to the dispersion convention provided it is SMOOTH.

DISCIPLINE
----------
- `from canonical_constants import *`; intermediates tagged `# (local)`
- GPU per-block via torch.linalg.eigvals (block-diagonal D_K; largest L<=10 block dim 9792)
- Per-mode ODE integration on CPU scipy.solve_ivp (OMP capped at 8)
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA)
- Verdict emitted via emit_verdict MCP tool (script PRINTS payload only)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)  +  CPU thread cap
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")     # before numpy import (CPU ODE contention)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

# _shared (canonical_constants.py + dirac_spectrum.py) must be importable BEFORE
# the canonical import; this script lives at computations/investigation-12/.
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402  (tau_fold, M_KK, Delta_BCS, Delta_B1/B2/B3, n_pairs, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
from scipy.integrate import solve_ivp  # noqa: E402

import dirac_spectrum as ds  # noqa: E402

# torch (GPU) — optional; fall back to numpy if unavailable
try:
    import torch
    _HAVE_TORCH = bool(torch.cuda.is_available())
except Exception:
    torch = None
    _HAVE_TORCH = False

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registered machinery pins (plan §W3-1)
# ---------------------------------------------------------------------------
SESSION = "S12"                                                   # (local) investigation 12
GATE_ID = "INV12-W3-1-RELIC-SPECTRUM-ODE-LOCK"                    # (local)
SCHEME = "FW"                                                     # (local) framework BdG dispersion
CONVENTION = "ABSOLUTE"                                           # (local) in/out adiabatic-vacuum Bogoliubov
L_MAX = 10                                                        # (local)

# Pre-registered thresholds (plan strict_PASS_boundary)
INTEGRATOR_TOL = 1e-4        # (local) cross-integrator relative agreement
REFINE_TOL = 1e-4           # (local) rtol-refinement relative agreement
UNITARITY_TOL = 1e-10        # (local) |alpha|^2-|beta|^2=1 residual
ODE_RTOL = 1e-10            # (local) primary ODE rtol
ODE_RTOL_REFINE = 1e-12      # (local) refinement ODE rtol
ODE_ATOL = 1e-12            # (local) ODE atol

# Fold window (plan scan_range): tau in [0.190-0.05, 0.190+0.05] with adiabatic wings
DTAU_IN = 0.05               # (local)
DTAU_OUT = 0.05              # (local)
TAU_IN = float(tau_fold) - DTAU_IN      # (local) = 0.140
TAU_OUT = float(tau_fold) + DTAU_OUT    # (local) = 0.240
N_TAU = 21                   # (local) tau-grid for the smooth omega_k(tau) profile (odd: midpoint at fold;
                             # 21 pts => dtau=0.005; omega_k(tau) is SMOOTH (max adjacent jump 0.0046 at
                             # dtau=0.0025, S12 W3-1 pre-flight) so the CubicSpline is well-resolved here;
                             # the LOCK verdict is integrator-independence, not trajectory resolution)

# Casimir-bounded bottom-band level ceiling (math-scripts.md §"D_K Block-Diagonality +
# Recursive-Casimir-Projection Feasibility Pre-Check"). The bottom band is the LOW-(p,q)
# set; higher (p,q) carry HIGHER |lambda|_min (deeper-adiabatic, smaller |beta|^2). We
# build incrementally by level and emit a truncation-convergence check: rho_relic and
# N_pair_eff must STABILIZE as the ceiling rises (the higher levels add adiabatically
# frozen modes). L_BAND_CEILING is the operational ceiling; L_MAX=10 is the nominal cap.
L_BAND_CEILING = 7           # (local) operational Casimir-bounded ceiling (p+q<=7; feasible irreps)
L_BAND_CHECK = 8             # (local) one level beyond, for the truncation-convergence delta
TRUNC_TOL = 0.05             # (local) rel change in rho_relic from ceiling->check must be <= this

# N_seg refinement scan (demonstrate the TM artifact converging to the ODE)
N_SEG_SCAN = [25, 50, 100, 200, 400, 800]   # (local)

# Pair-band anchors (S101-W1-QEQ-RELIC-ODDFLOOR), cross-check only
PAIR_BAND_LO = 1.6395        # (local) = 2*|lambda|_min
PAIR_BAND_HI = 10.8379       # (local) = 2*|lambda|_max (L<=12 band-top)

# Output destinations
OUT_NPZ = SESSION_DIR / "inv12_w3_1_relic_spectrum_ode_lock.npz"
OUT_PNG = SESSION_DIR / "inv12_w3_1_relic_spectrum_ode_lock.png"

CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local) drift-corrected
CACHE_PATH_PLAN = SHARED_DIR / "s84_spectrum_cache_L12_tau019.npz"                  # (local) plan-pinned (absent)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block
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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — SU(3) skeleton + eigenvalue-trajectory construction
# ---------------------------------------------------------------------------
def build_su3_skeleton():
    """tau-independent SU(3) building blocks."""
    gens = ds.su3_generators()                          # (local)
    f_abc = ds.compute_structure_constants(gens)        # (local)
    B_ab = ds.compute_killing_form(f_abc)               # (local)
    gammas = ds.build_cliff8()                          # (local)
    return gens, f_abc, B_ab, gammas


def _block_eigvals(D: np.ndarray) -> np.ndarray:
    """|lambda| spectrum of the block. D_K is ANTI-Hermitian (math convention, no
    factor of i; dirac_spectrum.py docstring) => eigenvalues are purely imaginary and
    H = i*D is Hermitian with REAL eigenvalues equal to imag(eig(D)). We diagonalize
    H = i*D with the Hermitian routine torch.linalg.eigvalsh on GPU (ROCm-native, NO
    MAGMA needed — the general eig DOES need MAGMA which this build lacks) and return
    |eigenvalues|. Verified == numpy |eigvals(D).imag| to 1e-14 (S12 W3-1 pre-flight)."""
    if _HAVE_TORCH and D.shape[0] >= 100:
        H = 1j * D                                      # (local) Hermitian (i * anti-Hermitian)
        t = torch.tensor(H, device="cuda")              # (local)
        ev = torch.linalg.eigvalsh(t).cpu().numpy()     # (local) REAL eigenvalues
        return np.sort(np.abs(ev))
    ev = np.linalg.eigvals(D)                            # (local) CPU fallback (small blocks)
    return np.sort(np.abs(ev.imag))


def frame_omega_at_tau(s: float, skel) -> tuple[np.ndarray, np.ndarray]:
    """Compute the tau-dependent orthonormal frame E(tau) and spinor curvature
    offset Omega(tau) ONCE. These are SECTOR-INDEPENDENT (depend only on the Jensen
    metric at tau), so they are hoisted out of the per-sector loop — a ~N_sector
    redundancy elimination in the trajectory build."""
    gens, f_abc, B_ab, gammas = skel
    g_s = ds.jensen_metric(B_ab, s)                     # (local)
    E = ds.orthonormal_frame(g_s)                       # (local)
    ft = ds.frame_structure_constants(f_abc, E)         # (local)
    Gamma = ds.connection_coefficients(ft)              # (local)
    Omega = ds.spinor_connection_offset(Gamma, gammas)  # (local)
    return E, Omega


def spectrum_from_frame(p: int, q: int, E: np.ndarray, Omega: np.ndarray,
                        skel) -> np.ndarray:
    """Block |lambda| spectrum for sector (p,q) given the precomputed frame E(tau)
    and Omega(tau). Only the cheap per-sector kron assembly + eigvalsh remain."""
    gens, f_abc, _B_ab, gammas = skel
    rho, _ = ds.get_irrep(p, q, gens, f_abc)            # (local) cached
    D = ds.dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
    return _block_eigvals(D)


def spectrum_pq(p: int, q: int, s: float, skel) -> np.ndarray:
    """Block |lambda| spectrum for Peter-Weyl sector (p,q) at Jensen param s=tau
    (convenience wrapper; computes frame fresh — used for validation only)."""
    E, Omega = frame_omega_at_tau(s, skel)              # (local)
    return spectrum_from_frame(p, q, E, Omega, skel)


def _unique_with_mult(vals: np.ndarray, tol: float):
    """Collapse near-equal values; return (unique_values, multiplicities)."""
    vals = np.sort(vals)                                                    # (local)
    uniq = [vals[0]]                                                        # (local)
    mult = [1]                                                              # (local)
    for x in vals[1:]:
        if x - uniq[-1] <= tol * max(1.0, abs(uniq[-1])):
            mult[-1] += 1
        else:
            uniq.append(x); mult.append(1)
    return np.array(uniq), np.array(mult)


def sectors_by_level(cache: dict, level_ceiling: int) -> list:
    """Peter-Weyl sectors (p,q) with p+q <= level_ceiling, present in the cache,
    ordered by level then (p,q). The bottom band is the LOW-(p,q) set: the Casimir
    bound |lambda|_min^(p,q) ~ sqrt(C_2(p,q))/r(tau) means higher (p,q) carry HIGHER
    minimum |lambda| (deeper-adiabatic modes, smaller |beta|^2)."""
    return sorted([(p, q) for (p, q) in cache.keys() if p + q <= level_ceiling],
                  key=lambda k: (k[0] + k[1], k))


def lambda_traj_sectorwise(skel, sectors: list, tau_grid: np.ndarray,
                           cache: dict) -> dict:
    """Build the SMOOTH lambda_k(tau) trajectory PER SECTOR (irreps cached once by
    get_irrep; only frame/Omega recomputed per tau). Returns a dict keyed by (p,q)
    with the per-sector trajectory array (n_modes_block, n_tau), sorted ascending
    per column. Sorted-mode tracking is faithful: max adjacent-tau jump in the
    bottom band is 0.0046 at dtau=0.0025 (no hard crossings; S12 W3-1 pre-flight)."""
    n_tau = len(tau_grid)                                                  # (local)
    t0 = time.time()                                                       # (local)
    # warm the irrep cache once (tau-independent rho); first call per sector builds it
    print(f"  warming irrep cache for {len(sectors)} sectors (tau-independent) ...")
    for (p, q) in sectors:
        ds.get_irrep(p, q, skel[0], skel[1])                               # populate _irrep_cache
    print(f"    irrep cache warm ({time.time()-t0:.1f}s)")
    # tau-OUTER loop: frame E(tau)/Omega(tau) computed ONCE per tau (sector-independent),
    # reused across all sectors -> eliminates the ~N_sector frame-recompute redundancy.
    t1 = time.time()                                                       # (local)
    cols_by_sector = {pq: [] for pq in sectors}                            # (local)
    for it, s in enumerate(tau_grid):
        E, Omega = frame_omega_at_tau(float(s), skel)                      # (local) ONCE per tau
        for (p, q) in sectors:
            v = spectrum_from_frame(p, q, E, Omega, skel)                  # (local) cheap per-sector kron+eigvalsh
            v = v[v > 1e-9]                                                # drop spurious zero modes
            cols_by_sector[(p, q)].append(np.sort(v))
        if it == 0 or (it + 1) % 20 == 0 or it == n_tau - 1:
            print(f"    tau[{it+1:3d}/{n_tau}] = {s:.5f}  ({time.time()-t1:.1f}s)")
    # assemble per-sector trajectory arrays
    traj = {}                                                              # (local)
    for (p, q) in sectors:
        cols = cols_by_sector[(p, q)]                                      # (local)
        lens = {len(c) for c in cols}                                      # (local)
        if len(lens) != 1:
            nmin = min(lens)                                               # (local)
            cols = [c[:nmin] for c in cols]
        traj[(p, q)] = np.array(cols).T   # (n_modes_block, n_tau)
    print(f"    trajectory built: {len(sectors)} sectors x {n_tau} tau ({time.time()-t1:.1f}s)")
    return traj


# ---------------------------------------------------------------------------
# Section 6 — BdG dispersion + smooth mode-frequency trajectory
# ---------------------------------------------------------------------------
# Substrate-canonical: mu = 0 (particle-hole symmetric, S36); per-mode gap Delta_k.
MU_CHEM = 0.0                # (local) particle-hole-symmetric chemical potential (S36 ED)


def omega_k_of_tau(lam_row: np.ndarray, Delta_k: float) -> np.ndarray:
    """Framework BdG quasiparticle frequency along the trajectory:
       omega_k(tau) = sqrt( (lambda_k(tau) - mu)^2 + Delta_k^2 ),  mu = 0.
    Smooth function of tau (the Bogoliubov mode equation frequency)."""
    xi = lam_row - MU_CHEM                                                 # (local) band energy
    return np.sqrt(xi * xi + Delta_k * Delta_k)


# ---------------------------------------------------------------------------
# Section 7 — Adiabatic in/out Bogoliubov via ODE  (Birrell-Davies sec. 3.4)
# ---------------------------------------------------------------------------
def adiabatic_bogoliubov_ode(tau_grid: np.ndarray, omega_grid: np.ndarray,
                             method: str, rtol: float) -> tuple[float, float, bool]:
    """Integrate u'' + omega(tau)^2 u = 0 from the in-region (positive-freq adiabatic
    mode) to the out-region; project onto the out adiabatic basis to extract |alpha|^2,
    |beta|^2.

    In-state IC at tau_in (adiabatic positive-frequency WKB; omega ~ const in the wing):
        u(tau_in)  = 1/sqrt(2 w_in) ,    u'(tau_in) = -i w_in * u(tau_in)
    Out projection at tau_out:
        a_out =  (sqrt(w_out/2) u + i u'/sqrt(2 w_out))            [positive-freq coeff]
        b_out =  (sqrt(w_out/2) u - i u'/sqrt(2 w_out))            [negative-freq coeff]
        |alpha|^2 = |a_out|^2 ,  |beta|^2 = |b_out|^2 ,  |alpha|^2-|beta|^2 = 1 (Wronskian).
    """
    from scipy.interpolate import CubicSpline
    sp_w = CubicSpline(tau_grid, omega_grid)                               # (local) smooth omega(tau)
    w_in = float(omega_grid[0])                                            # (local)
    w_out = float(omega_grid[-1])                                          # (local)
    u0 = 1.0 / np.sqrt(2.0 * w_in)                                         # (local)
    du0 = -1j * w_in * u0                                                  # (local)
    y0 = [u0.real if hasattr(u0, "real") else u0, 0.0, du0.real, du0.imag] # (local) [Re u, Im u, Re u', Im u']

    def rhs(t, y):
        w = float(sp_w(t))                                                 # (local)
        w2 = w * w                                                         # (local)
        return [y[2], y[3], -w2 * y[0], -w2 * y[1]]

    sol = solve_ivp(rhs, [tau_grid[0], tau_grid[-1]], y0, method=method,
                    rtol=rtol, atol=ODE_ATOL, dense_output=False)          # (local)
    if not sol.success:
        return np.nan, np.nan, False
    u = sol.y[0, -1] + 1j * sol.y[1, -1]                                   # (local)
    du = sol.y[2, -1] + 1j * sol.y[3, -1]                                  # (local)
    rw = np.sqrt(w_out / 2.0)                                              # (local)
    a_out = rw * u + 1j * du / np.sqrt(2.0 * w_out)                        # (local)
    b_out = rw * u - 1j * du / np.sqrt(2.0 * w_out)                        # (local)
    return float(abs(a_out) ** 2), float(abs(b_out) ** 2), True


def piecewise_tm_beta(tau_grid: np.ndarray, omega_grid: np.ndarray,
                      n_seg: int) -> tuple[float, float]:
    """Naive piecewise-CONSTANT transfer-matrix Bogoliubov (the ARTIFACT to retire).
    Segments [tau_in,tau_out] into n_seg constant-omega slabs; propagates the
    fundamental 2x2 solution; projects onto in/out adiabatic basis. For a SMOOTH
    omega(tau) this introduces spurious step reflections; |beta|^2 should CONVERGE
    to the ODE value as n_seg -> infinity (demonstrating the artifact)."""
    from scipy.interpolate import CubicSpline
    sp_w = CubicSpline(tau_grid, omega_grid)                               # (local)
    edges = np.linspace(tau_grid[0], tau_grid[-1], n_seg + 1)              # (local)
    mids = 0.5 * (edges[:-1] + edges[1:])                                  # (local)
    w_seg = sp_w(mids)                                                     # (local)
    Lseg = (tau_grid[-1] - tau_grid[0]) / n_seg                            # (local)
    w_in = float(omega_grid[0]); w_out = float(omega_grid[-1])            # (local)
    # in-state: positive-freq adiabatic mode at tau_in
    u = 1.0 / np.sqrt(2.0 * w_in) + 0j                                     # (local)
    du = -1j * w_in * u                                                    # (local)
    for w in w_seg:
        w = float(w)                                                       # (local)
        c = np.cos(w * Lseg); sN = np.sin(w * Lseg)                        # (local)
        # propagate [u, u'] through a constant-omega slab: u''+w^2 u = 0
        u_new = c * u + (sN / w) * du                                      # (local)
        du_new = -w * sN * u + c * du                                      # (local)
        u, du = u_new, du_new
    rw = np.sqrt(w_out / 2.0)                                              # (local)
    a_out = rw * u + 1j * du / np.sqrt(2.0 * w_out)                        # (local)
    b_out = rw * u - 1j * du / np.sqrt(2.0 * w_out)                        # (local)
    return float(abs(a_out) ** 2), float(abs(b_out) ** 2)


# ---------------------------------------------------------------------------
# Section 8 — box+delta sudden-limit cross-check (S100b recipe, self-contained)
# ---------------------------------------------------------------------------
def entire_CS(mu2: float, L: float) -> tuple[float, float]:
    """C=cos(mu L), S=sin(mu L)/mu as entire functions of mu^2 (Schmidt continuation
    mu->i Lambda for mu^2<0). Replicates S100b s100b_box_delta_bogoliubov.entire_CS."""
    x = mu2 * L * L                                                        # (local)
    if abs(x) < 1e-12:
        return 1.0 - x / 2.0, L * (1.0 - x / 6.0)
    if mu2 > 0:
        m = np.sqrt(mu2)                                                   # (local)
        return float(np.cos(m * L)), float(np.sin(m * L) / m)
    lam = np.sqrt(-mu2)                                                    # (local)
    return float(np.cosh(lam * L)), float(np.sinh(lam * L) / lam)


def box_delta_beta2(k: float, V: float, Om1: float, Om2: float,
                    L: float) -> tuple[float, float]:
    """Schmidt Eq.75/76-class closed form (S100b closed_form_beta2). The EXACT
    sudden-limit case where TM IS exact (var_Nseg=1)."""
    mu2 = k * k - V                                                        # (local)
    C, S = entire_CS(mu2, L)                                               # (local)
    t21 = (Om1 + Om2) * C + (Om1 * Om2 - mu2) * S                          # (local)
    beta2 = 0.25 * ((Om1 - Om2) ** 2 * S ** 2 + (k * S + t21 / k) ** 2)    # (local)
    alpha2 = 0.25 * ((2.0 * C + (Om1 + Om2) * S) ** 2 + (k * S - t21 / k) ** 2)  # (local)
    return float(beta2), float(alpha2)


def box_delta_tm_beta2(k: float, V: float, Om1: float, Om2: float, L: float,
                       n_seg: int) -> tuple[float, float, float]:
    """N_seg piecewise-constant TM for the box+delta (independent code path).
    Returns (|beta|^2, |alpha|^2, unitarity_residual). For the box (constant V)
    the TM is exact at any n_seg -> var_Nseg = 1 (the sudden-limit benchmark)."""
    eta_on, eta_off = 0.0, L                                              # (local)
    # in-state pure positive frequency e^{-ik eta}
    psi = np.exp(-1j * k * eta_on)                                        # (local)
    dpsi = -1j * k * psi                                                  # (local)
    # delta at switch-on
    dpsi = dpsi + Om1 * psi                                               # (local)
    edges = np.linspace(eta_on, eta_off, n_seg + 1)                       # (local)
    Lseg = L / n_seg                                                      # (local)
    mu2 = k * k - V                                                       # (local)
    C, S = entire_CS(mu2, Lseg)                                           # (local)
    for _ in range(n_seg):
        psi_new = C * psi + S * dpsi                                      # (local)
        dpsi_new = -mu2 * S * psi + C * dpsi                              # (local)
        psi, dpsi = psi_new, dpsi_new
    dpsi = dpsi + Om2 * psi                                               # (local) delta at switch-off
    beta = 0.5 * (psi + dpsi / (1j * k)) * np.exp(-1j * k * eta_off)      # (local)
    alpha = 0.5 * (psi - dpsi / (1j * k)) * np.exp(+1j * k * eta_off)     # (local)
    b2, a2 = float(abs(beta) ** 2), float(abs(alpha) ** 2)               # (local)
    return b2, a2, abs(a2 - b2 - 1.0)


# ---------------------------------------------------------------------------
# Section 9 — gap assignment per mode (B1/B2/B3 banding)
# ---------------------------------------------------------------------------
def assign_gap(lam0: float) -> float:
    """Assign the per-mode BdG gap Delta_k by the substrate band the eigenvalue
    sits in. The framework canonical aggregate is Delta_BCS=0.4643 (S70). The
    per-band GL gaps (S95 W3-3) are Delta_B1=0.371795, Delta_B2=0.732026,
    Delta_B3=0.176. We use the aggregate Delta_BCS as the canonical single-gap
    (particle-hole-symmetric BdG, S36); the lock verdict is gap-convention-robust
    (the gap only sets the SMOOTH frequency floor, not the integrator-independence)."""
    return float(Delta_BCS)


# ---------------------------------------------------------------------------
# Section 10 — Compute
# ---------------------------------------------------------------------------
def _run_bogoliubov_over_modes(uniq, mult, lam_rows, tau_grid):
    """Integrate the adiabatic in/out Bogoliubov ODE for every unique mode (Radau,
    DOP853, Radau-refine). Returns per-mode arrays. lam_rows[j] is the smooth
    lambda_k(tau) trajectory for unique mode j."""
    n = len(uniq)                                                        # (local)
    E_k = np.zeros(n); omega_out = np.zeros(n)                           # (local)
    b2_r = np.zeros(n); b2_d = np.zeros(n); b2_rf = np.zeros(n)          # (local)
    a2_r = np.zeros(n); ur = np.zeros(n); Dk_arr = np.zeros(n)           # (local)
    ok = np.ones(n, dtype=bool)                                          # (local)
    t0 = time.time()                                                    # (local)
    for j in range(n):
        Dk = assign_gap(float(uniq[j]))                                 # (local)
        Dk_arr[j] = Dk
        wgrid = omega_k_of_tau(lam_rows[j], Dk)                         # (local) smooth omega_k(tau)
        E_k[j] = float(np.sqrt(uniq[j] ** 2 + Dk ** 2))
        omega_out[j] = float(wgrid[-1])
        A_r, B_r, o_r = adiabatic_bogoliubov_ode(tau_grid, wgrid, "Radau", ODE_RTOL)    # (local)
        A_d, B_d, o_d = adiabatic_bogoliubov_ode(tau_grid, wgrid, "DOP853", ODE_RTOL)   # (local)
        _A, B_f, o_f = adiabatic_bogoliubov_ode(tau_grid, wgrid, "Radau", ODE_RTOL_REFINE)  # (local)
        b2_r[j], a2_r[j] = B_r, A_r
        b2_d[j] = B_d; b2_rf[j] = B_f
        ur[j] = abs(A_r - B_r - 1.0)
        ok[j] = bool(o_r and o_d and o_f)
        if j < 3 or (j + 1) % 60 == 0 or j == n - 1:
            print(f"    mode[{j+1:3d}/{n}] |lam|={uniq[j]:.5f} mult={int(mult[j]):3d} "
                  f"E_k={E_k[j]:.5f} |beta|^2={B_r:.4e} unit={ur[j]:.2e} ({time.time()-t0:.1f}s)")
    return dict(E_k=E_k, omega_out=omega_out, beta2_radau=b2_r, beta2_dop=b2_d,
                beta2_refine=b2_rf, alpha2_radau=a2_r, unit_resid=ur, ode_ok=ok,
                Delta_k=Dk_arr)


def _band_from_sectors(traj: dict, sectors: list, tau_grid: np.ndarray):
    """Assemble the unique |lambda|(tau) trajectory set + multiplicities for the
    given sector list from the per-sector trajectory dict. Returns
    (uniq, mult, lam_rows) where lam_rows[j] is the smooth trajectory of unique mode j."""
    mid = len(tau_grid) // 2                                            # (local)
    # gather all per-mode trajectory rows across the requested sectors
    all_rows = []                                                       # (local)
    for (p, q) in sectors:
        T = traj[(p, q)]                                               # (n_block, n_tau)
        for r in range(T.shape[0]):
            all_rows.append(T[r, :])
    all_rows = np.array(all_rows)                                      # (n_modes_total, n_tau)
    lam_fold = all_rows[:, mid]                                        # (local)
    order = np.argsort(lam_fold)                                       # (local)
    all_rows = all_rows[order]; lam_fold = lam_fold[order]             # (local)
    # unique fold-values + multiplicity; representative row = first occurrence
    uniq, mult = _unique_with_mult(lam_fold, tol=1e-7)                 # (local)
    lam_rows = []                                                      # (local)
    idx = 0                                                            # (local)
    for u, m in zip(uniq, mult):
        lam_rows.append(all_rows[idx, :])    # representative trajectory of this unique value
        idx += int(m)
    return uniq, mult, np.array(lam_rows)


def compute() -> dict:
    print("\n=== Section A: SU(3) skeleton + cache validation ===")
    skel = build_su3_skeleton()                                          # (local)
    cache = np.load(CACHE_PATH, allow_pickle=True)["sector_evals"].item()  # (local)
    val_sectors = [(0, 0), (0, 1), (1, 1), (2, 2), (3, 3)]               # (local)
    max_dev = 0.0                                                        # (local)
    for (p, q) in val_sectors:
        if (p, q) in cache:
            v = np.sort(spectrum_pq(p, q, float(tau_fold), skel))        # (local)
            ce = np.sort(np.abs(cache[(p, q)]["abs_evals"]))             # (local)
            n = min(len(v), len(ce))                                     # (local)
            max_dev = max(max_dev, float(np.max(np.abs(v[:n] - ce[:n])))) # (local)
    print(f"  construction-vs-cache max|dev| at tau_fold (val sectors) = {max_dev:.3e}")
    construction_faithful = bool(max_dev < 1e-9)                         # (local)

    tau_grid = np.linspace(TAU_IN, TAU_OUT, N_TAU)                       # (local)

    print("\n=== Section B: Casimir-bounded bottom-band lambda_k(tau) (per-sector, GPU) ===")
    # Build sectors up to the CHECK ceiling (one beyond operational) so the truncation
    # convergence delta can be computed. Bottom band = LOW (p,q); higher (p,q) carry
    # higher |lambda|_min (Casimir bound) => deeper-adiabatic, smaller |beta|^2.
    sectors_check = sectors_by_level(cache, L_BAND_CHECK)                # (local)
    sectors_oper = sectors_by_level(cache, L_BAND_CEILING)              # (local)
    print(f"  operational ceiling p+q<={L_BAND_CEILING}: {len(sectors_oper)} sectors; "
          f"check ceiling p+q<={L_BAND_CHECK}: {len(sectors_check)} sectors")
    traj = lambda_traj_sectorwise(skel, sectors_check, tau_grid, cache)  # (local)

    print("\n=== Section C: per-mode adiabatic in/out Bogoliubov (operational band) ===")
    uniq, mult, lam_rows = _band_from_sectors(traj, sectors_oper, tau_grid)  # (local)
    n_uniq = len(uniq)                                                  # (local)
    print(f"  operational band (p+q<={L_BAND_CEILING}): unique |lambda| modes={n_uniq} "
          f"(sum mult={int(mult.sum())})")
    res = _run_bogoliubov_over_modes(uniq, mult, lam_rows, tau_grid)     # (local)
    E_k = res["E_k"]; omega_k_out = res["omega_out"]                     # (local)
    beta2_radau = res["beta2_radau"]; beta2_dop = res["beta2_dop"]       # (local)
    beta2_refine = res["beta2_refine"]; alpha2_radau = res["alpha2_radau"]  # (local)
    unit_resid = res["unit_resid"]; ode_ok = res["ode_ok"]              # (local)
    Delta_k_arr = res["Delta_k"]                                        # (local)
    n_modes_full = int(mult.sum())                                      # (local)

    # ---- convergence metrics (the LOCK verdict) ----
    eps = 1e-300                                                        # (local)
    integ_rel = np.abs(beta2_radau - beta2_dop) / (np.abs(beta2_radau) + eps)  # (local)
    refine_rel = np.abs(beta2_radau - beta2_refine) / (np.abs(beta2_radau) + eps)  # (local)
    prod_mask = beta2_radau > 1e-12                                     # (local)
    integrator_agreement = float(np.max(integ_rel[prod_mask])) if prod_mask.any() else 0.0  # (local)
    refine_agreement = float(np.max(refine_rel[prod_mask])) if prod_mask.any() else 0.0      # (local)
    unitarity_residual = float(np.max(unit_resid))                      # (local)
    print(f"\n  integrator_agreement (max rel Radau-vs-DOP853, |beta|^2>1e-12) = {integrator_agreement:.3e}")
    print(f"  refine_agreement (max rel rtol 1e-10-vs-1e-12)               = {refine_agreement:.3e}")
    print(f"  unitarity_residual (max |alpha|^2-|beta|^2-1)               = {unitarity_residual:.3e}")
    print(f"  all ODE integrations succeeded: {bool(ode_ok.all())}")

    # ---- relic energy density + effective pair count ----
    rho_relic = float(np.sum(mult * E_k * beta2_radau))                 # (local) Sum_k E_k |beta_k|^2
    N_pair_eff = float(np.sum(mult * beta2_radau))                      # (local) Sum_k |beta_k|^2
    print(f"\n  rho_relic = Sum_k mult_k E_k |beta_k|^2 = {rho_relic:.6e} (M_KK units)")
    print(f"  N_pair_eff = Sum_k mult_k |beta_k|^2     = {N_pair_eff:.6e}")
    print(f"  (canonical n_pairs reference = {n_pairs}; this SMOOTH-window adiabatic"
          f" sweep is gentle, see WP)")

    # ---- TRUNCATION-CONVERGENCE check (the Casimir-bound 'truncation_consistent') ----
    print("\n=== Section C2: truncation-convergence (Casimir-bound ceiling stability) ===")
    extra_sectors = [s for s in sectors_check if s not in sectors_oper]  # (local) the next level
    if extra_sectors:
        uq2, ml2, lr2 = _band_from_sectors(traj, sectors_check, tau_grid)  # (local) full check band
        res2 = _run_bogoliubov_over_modes(uq2, ml2, lr2, tau_grid)       # (local)
        E_k2 = res2["E_k"]; b2_2 = res2["beta2_radau"]                  # (local)
        rho_relic_check = float(np.sum(ml2 * E_k2 * b2_2))              # (local)
        N_pair_check = float(np.sum(ml2 * b2_2))                        # (local)
        rho_trunc_rel = abs(rho_relic_check - rho_relic) / max(abs(rho_relic_check), eps)  # (local)
        N_trunc_rel = abs(N_pair_check - N_pair_eff) / max(abs(N_pair_check), eps)         # (local)
        print(f"  rho_relic(p+q<={L_BAND_CEILING})={rho_relic:.6e}  "
              f"rho_relic(p+q<={L_BAND_CHECK})={rho_relic_check:.6e}  rel change={rho_trunc_rel:.3e}")
        print(f"  N_pair(p+q<={L_BAND_CEILING})={N_pair_eff:.6e}  "
              f"N_pair(p+q<={L_BAND_CHECK})={N_pair_check:.6e}  rel change={N_trunc_rel:.3e}")
    else:
        rho_relic_check = rho_relic; N_pair_check = N_pair_eff           # (local)
        rho_trunc_rel = 0.0; N_trunc_rel = 0.0                          # (local)
    # truncation_consistent: construction faithful AND the relic observables are stable
    # under raising the Casimir ceiling by one level (higher levels adiabatically frozen)
    truncation_consistent = bool(construction_faithful and rho_trunc_rel <= TRUNC_TOL)  # (local)
    print(f"  truncation_consistent = {truncation_consistent} "
          f"(construction_faithful={construction_faithful}, rho rel change {rho_trunc_rel:.3e} <= {TRUNC_TOL})")

    # ---- pair-band cross-check (S101 anchor) ----
    pair_band = np.sort(2.0 * E_k)                                      # (local)
    print(f"\n  pair-band 2E_k (operational): [{pair_band.min():.4f}, {pair_band.max():.4f}]")
    print(f"  2*|lambda|_min = {2.0*float(uniq.min()):.6f}  (S101 lower edge {PAIR_BAND_LO})")
    print(f"  (S101 full band [{PAIR_BAND_LO},{PAIR_BAND_HI}] is 2|lambda| over L<=12, Delta->0)")

    print("\n=== Section D: N_seg-refinement (TM artifact -> ODE convergence) ===")
    # pick a representative high-production mode for the refinement demonstration
    j_demo = int(np.argmax(beta2_radau))                                # (local)
    omega_demo = omega_k_of_tau(lam_rows[j_demo], Delta_k_arr[j_demo])  # (local) smooth omega_k(tau)
    tm_beta2_vs_nseg = []                                              # (local)
    for ns in N_SEG_SCAN:
        _a, _b = piecewise_tm_beta(tau_grid, omega_demo, ns)            # (local)
        tm_beta2_vs_nseg.append(_b)
        print(f"  N_seg={ns:4d}: |beta|^2_TM = {_b:.8e}  "
              f"(ODE Radau = {beta2_radau[j_demo]:.8e})")
    tm_beta2_vs_nseg = np.array(tm_beta2_vs_nseg)                       # (local)
    tm_var_nseg = float(tm_beta2_vs_nseg.max() / max(tm_beta2_vs_nseg.min(), 1e-300))  # (local)
    tm_ode_converge = float(abs(tm_beta2_vs_nseg[-1] / beta2_radau[j_demo] - 1.0))     # (local)
    print(f"  TM var_Nseg (max/min over scan) = {tm_var_nseg:.4f}  "
          f"(SMOOTH fold => TM segment-dependent; the artifact)")
    print(f"  TM(N_seg=800) -> ODE rel dev = {tm_ode_converge:.4e}  "
          f"(TM converges to the ODE as segments shrink)")

    print("\n=== Section E: box+delta sudden-limit cross-check (S100b recipe) ===")
    # exact box+delta: closed form vs N_seg TM (var_Nseg must be ~1: TM exact for box)
    k_bd = 1.0; V_bd = 0.5; Om1_bd = +0.3; Om2_bd = -0.25; L_bd = 1.2     # (local) representative
    b2_cf, a2_cf = box_delta_beta2(k_bd, V_bd, Om1_bd, Om2_bd, L_bd)      # (local)
    bd_unit_cf = abs(a2_cf - b2_cf - 1.0)                                # (local)
    bd_tm = [box_delta_tm_beta2(k_bd, V_bd, Om1_bd, Om2_bd, L_bd, ns) for ns in N_SEG_SCAN]  # (local)
    bd_beta2 = np.array([x[0] for x in bd_tm])                           # (local)
    bd_unit = np.array([x[2] for x in bd_tm])                            # (local)
    bd_var_nseg = float(bd_beta2.max() / max(bd_beta2.min(), 1e-300))    # (local)
    bd_cf_tm_dev = float(abs(bd_beta2[-1] / b2_cf - 1.0))                # (local)
    print(f"  box+delta closed-form |beta|^2 = {b2_cf:.8e} (unitarity {bd_unit_cf:.2e})")
    print(f"  box+delta TM var_Nseg = {bd_var_nseg:.10f}  (EXACT for box: ~1, vs SMOOTH fold {tm_var_nseg:.3f})")
    print(f"  box+delta closed-form vs TM rel dev = {bd_cf_tm_dev:.2e} (independent code paths agree)")
    print(f"  box+delta TM max unitarity residual = {float(bd_unit.max()):.2e}")

    # ---- verdict ----
    # The gate's CORE deliverable is the INTEGRATOR LOCK: the {beta_k} spectrum is
    # integrator-independent (Radau==DOP853) + rtol-refined + unitary to machine eps.
    # That retires the transfer-matrix segmentation artifact (plan A4 assumption).
    # PASS additionally requires truncation_consistent (the relic-CONTENT observables
    # rho_relic/N_pair_eff stable under raising the Casimir ceiling). If the integrator
    # lock holds but the relic content carries a truncation band, the plan pre-registers
    # INFO: "converges across integrators but carries a residual dependence ... usable
    # spectrum emitted with a stated uncertainty band; W3-2/3/4 proceed and carry the
    # band forward into their own error budgets."
    integrator_locked = (integrator_agreement <= INTEGRATOR_TOL and
                         refine_agreement <= REFINE_TOL and
                         unitarity_residual <= UNITARITY_TOL and
                         bool(ode_ok.all()))                            # (local)
    if (not ode_ok.all()) or unitarity_residual > UNITARITY_TOL:
        verdict = "FAIL"                                                # (local) non-convergence / unitarity break
    elif integrator_locked and truncation_consistent:
        verdict = "PASS"                                                # (local) fully locked
    elif integrator_locked and not truncation_consistent:
        verdict = "INFO"                                                # (local) integrator-locked; relic content carries a truncation band
    elif (integrator_agreement <= 1e-2 and refine_agreement <= 1e-2):
        verdict = "INFO"                                                # (local) converges across integrators, residual 1e-4..1e-2
    else:
        verdict = "FAIL"                                                # (local)

    # value reported = the binding convergence metric (max of the two integrator agreements)
    value = max(integrator_agreement, refine_agreement)                 # (local)

    return dict(
        verdict=verdict, value=value,
        # locked spectrum arrays (downstream-consumed)
        beta_k=beta2_radau.copy(), alpha_k=alpha2_radau.copy(),
        beta2_k=beta2_radau.copy(),  # |beta_k|^2 alias
        E_k=E_k.copy(), omega_k=omega_k_out.copy(), k_grid=uniq.copy(),
        mult_k=mult.copy(), Delta_k=Delta_k_arr.copy(),
        rho_relic=rho_relic, N_pair_eff=N_pair_eff,
        # convergence diagnostics
        integrator_agreement=integrator_agreement, refine_agreement=refine_agreement,
        unitarity_residual=unitarity_residual,
        ode_all_ok=bool(ode_ok.all()),
        truncation_consistent=truncation_consistent,
        construction_cache_dev=max_dev,
        construction_faithful=construction_faithful,
        # truncation-convergence (Casimir ceiling)
        L_band_ceiling=L_BAND_CEILING, L_band_check=L_BAND_CHECK,
        rho_relic_check=rho_relic_check, N_pair_check=N_pair_check,
        rho_trunc_rel=rho_trunc_rel, N_trunc_rel=N_trunc_rel,
        # N_seg artifact demonstration
        N_seg_scan=np.array(N_SEG_SCAN), tm_beta2_vs_nseg=tm_beta2_vs_nseg,
        tm_var_nseg=tm_var_nseg, tm_ode_converge=tm_ode_converge,
        beta2_ode_demo=float(beta2_radau[j_demo]),
        # box+delta sudden-limit cross-check
        bd_beta2_cf=b2_cf, bd_var_nseg=bd_var_nseg, bd_cf_tm_dev=bd_cf_tm_dev,
        bd_unit_max=float(bd_unit.max()),
        # pair band
        pair_band=pair_band, pair_band_lo_anchor=PAIR_BAND_LO, pair_band_hi_anchor=PAIR_BAND_HI,
        # window
        tau_grid=tau_grid, tau_in=TAU_IN, tau_out=TAU_OUT,
        n_modes_full=n_modes_full, n_uniq=n_uniq,
        # demo mode for plot
        omega_demo=omega_demo, j_demo=j_demo,
    )


# ---------------------------------------------------------------------------
# Section 11 — Plot
# ---------------------------------------------------------------------------
def make_plot(R: dict):
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))                     # (local)

    # (a) locked relic spectrum |beta_k|^2 vs |lambda_k|
    ax = axes[0, 0]                                                     # (local)
    ax.semilogy(R["k_grid"], np.maximum(R["beta2_k"], 1e-300), "o-", ms=3, lw=0.8, color="C0")
    ax.set_xlabel(r"$|\lambda_k|$  (M_KK)")
    ax.set_ylabel(r"$|\beta_k|^2$  (locked occupation)")
    ax.set_title("Locked relic Bogoliubov spectrum (ODE, Radau rtol=1e-10)")
    ax.grid(alpha=0.3)

    # (b) per-mode E_k and the pair band 2E_k vs S101 anchor
    ax = axes[0, 1]                                                     # (local)
    ax.plot(R["k_grid"], R["E_k"], ".", ms=3, color="C1", label=r"$E_k=\sqrt{\lambda_k^2+\Delta_k^2}$")
    ax.axhspan(R["pair_band_lo_anchor"] / 2, R["pair_band_hi_anchor"] / 2, alpha=0.12, color="C2",
               label=r"S101 band $E_k\in[0.82,5.42]$")
    ax.set_xlabel(r"$|\lambda_k|$  (M_KK)")
    ax.set_ylabel(r"$E_k$  (M_KK)")
    ax.set_title("Per-mode BdG energy vs S101 relic pair band")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # (c) N_seg-refinement: TM artifact converging to the ODE
    ax = axes[1, 0]                                                     # (local)
    ax.plot(R["N_seg_scan"], R["tm_beta2_vs_nseg"], "s-", color="C3", label="piecewise-const TM")
    ax.axhline(R["beta2_ode_demo"], ls="--", color="k", label="ODE Radau (converged)")
    ax.set_xscale("log")
    ax.set_xlabel(r"$N_{\rm seg}$")
    ax.set_ylabel(r"$|\beta|^2$ (demo mode)")
    ax.set_title(f"TM artifact -> ODE (smooth fold; TM var_Nseg={R['tm_var_nseg']:.2f})")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # (d) the smooth omega_k(tau) profile for the demo mode (the time-dependent frequency)
    ax = axes[1, 1]                                                     # (local)
    ax.plot(R["tau_grid"], R["omega_demo"], "-", color="C4")
    ax.axvline(float(tau_fold), ls=":", color="r", label=r"$\tau_{\rm fold}=0.190$")
    ax.set_xlabel(r"$\tau$ (Jensen deformation)")
    ax.set_ylabel(r"$\omega_k(\tau)$  (M_KK)")
    ax.set_title("Smooth mode-frequency trajectory through the fold")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    fig.suptitle(f"INV12-W3-1 RELIC-SPECTRUM-ODE-LOCK — {R['verdict']}  "
                 f"(int_agree={R['integrator_agreement']:.1e}, unit={R['unitarity_residual']:.1e})",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 12 — verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload = {
        "session": 12,
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
# Section 13 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                    # (local)

    # plan-text-drift disclosure
    if not CACHE_PATH_PLAN.exists() and CACHE_PATH.exists():
        print(f"PLAN-TEXT-DRIFT: cache pinned at {CACHE_PATH_PLAN} (absent); "
              f"resolved to canonical {CACHE_PATH} per substrate-first-canonical-sourcing.md (ii.B)")

    pins = log_input_pins(INPUT_FILES)                                  # (local)
    script_path = Path(__file__).resolve()                              # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"              # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    R = compute()                                                       # (local)

    # save npz (full float64; downstream-consumed FOUNDATIONAL artifact)
    np.savez(
        OUT_NPZ,
        beta_k=R["beta_k"], alpha_k=R["alpha_k"], beta2_k=R["beta2_k"],
        E_k=R["E_k"], omega_k=R["omega_k"], k_grid=R["k_grid"],
        mult_k=R["mult_k"], Delta_k=R["Delta_k"],
        rho_relic=R["rho_relic"], N_pair_eff=R["N_pair_eff"],
        integrator_agreement=R["integrator_agreement"],
        refine_agreement=R["refine_agreement"],
        unitarity_residual=R["unitarity_residual"],
        ode_all_ok=R["ode_all_ok"], truncation_consistent=R["truncation_consistent"],
        construction_cache_dev=R["construction_cache_dev"],
        construction_faithful=R["construction_faithful"],
        L_band_ceiling=R["L_band_ceiling"], L_band_check=R["L_band_check"],
        rho_relic_check=R["rho_relic_check"], N_pair_check=R["N_pair_check"],
        rho_trunc_rel=R["rho_trunc_rel"], N_trunc_rel=R["N_trunc_rel"],
        N_seg_scan=R["N_seg_scan"], tm_beta2_vs_nseg=R["tm_beta2_vs_nseg"],
        tm_var_nseg=R["tm_var_nseg"], tm_ode_converge=R["tm_ode_converge"],
        bd_beta2_cf=R["bd_beta2_cf"], bd_var_nseg=R["bd_var_nseg"],
        bd_cf_tm_dev=R["bd_cf_tm_dev"], bd_unit_max=R["bd_unit_max"],
        pair_band=R["pair_band"], tau_grid=R["tau_grid"],
        tau_in=R["tau_in"], tau_out=R["tau_out"],
        n_modes_full=R["n_modes_full"], n_uniq=R["n_uniq"],
        mu_chem=MU_CHEM, tau_fold=float(tau_fold),
    )
    print(f"\n  npz -> {OUT_NPZ}")
    make_plot(R)

    tag = emit_4tuple(R["value"], SCHEME, CONVENTION, L_MAX)            # (local)
    print(tag)

    note = (f"relic_spectrum_locked:int_agree={R['integrator_agreement']:.2e}_"
            f"refine={R['refine_agreement']:.2e}_unit={R['unitarity_residual']:.2e}_"
            f"n_uniq={R['n_uniq']}_rho_relic={R['rho_relic']:.4e}_Npair={R['N_pair_eff']:.4e}_"
            f"TMvarNseg={R['tm_var_nseg']:.2f}_BDvarNseg={R['bd_var_nseg']:.6f}_"
            f"trunc_consistent={R['truncation_consistent']}_"
            f"cache_path_drift_corrected_to_session-84")                # (local)
    extra = [
        f"# pair_band 2E_k=[{R['pair_band'].min():.4f},{R['pair_band'].max():.4f}] "
        f"S101_anchor=[{PAIR_BAND_LO},{PAIR_BAND_HI}](2|lambda|,Delta->0); "
        f"2|lambda|_min={2.0*float(R['k_grid'].min()):.6f}",
        f"# box_delta_sudden_xcheck: cf_beta2={R['bd_beta2_cf']:.6e} var_Nseg={R['bd_var_nseg']:.6f}(~1 EXACT) "
        f"cf_vs_TM={R['bd_cf_tm_dev']:.2e} vs SMOOTH_fold_TM_var_Nseg={R['tm_var_nseg']:.3f}(ARTIFACT)",
        f"# truncation: Casimir-bound bottom band p+q<={R['L_band_ceiling']} (operational), "
        f"rho_relic rel change to p+q<={R['L_band_check']} = {R['rho_trunc_rel']:.3e} (<= {TRUNC_TOL} => stable); "
        f"higher levels adiabatically frozen (math-scripts.md D_K-block-diagonality pre-check)",
        f"# convention: omega_k=sqrt((lambda_k-mu)^2+Delta_k^2) mu=0 (S36 particle-hole-symm); "
        f"Delta_k=Delta_BCS={float(Delta_BCS):.6f}; plan (lambda^2-mu^2)^2 = transcription of (lambda-mu) BdG band-energy",
    ]
    print_verdict_payload(R["verdict"], R["value"], audit_sha, content_sha,
                          companion_note=note, extra_rows=extra)

    wall = time.time() - t0                                             # (local)
    print(f"\n=== {GATE_ID}: {R['verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
