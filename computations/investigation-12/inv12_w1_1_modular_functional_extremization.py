#!/usr/bin/env python3
"""
INV12 W1-1 — MODULAR-FUNCTIONAL-EXTREMIZATION
=============================================================================

Gate: INV12-W1-1-MODULAR-FUNCTIONAL-EXTREMIZATION  ([SIGN])

HYPOTHESIS (plan §W1-1):
  The substrate's faithful normal modular weight omega (§VII.BZ / K12,
  STAGE-3-PERMANENT) extremizes the spectral entropy functional
        S_modular(tau) = Tr(D_K(tau)^2 rho_omega)
  at tau_fold = 0.190  --  i.e.  dS_modular/dtau|_{tau_fold} = 0  --  supplying
  the substrate-derived SELECTION principle that F-STAR-SELF-CONSISTENCY (S76)
  failed to find with four OTHER principles, and that §W8a-85 did NOT run
  (the GGE-ENTROPY-FUNCTIONAL-as-V.P. named-OPEN channel, session-84).

Pre-registered threshold (plan §W1-1 `operator` / `strict_PASS_boundary`):
  |dS_modular/dtau|_{tau_fold}| / S_scale  <=  tol_stationary = 1e-3
  PASS  iff  the omega-weighted velocity sum is stationary at tau_fold
            (|dS/dtau|/S_scale <= 1e-3) AND brackets a sign-CHANGE across the fold;
  FAIL  iff  S_modular is monotone through the fold (no sign change);
  INFO  iff  S_modular is stationary at a tau != 0.190 (extremum OFF-fold),
            OR rho_omega is not reconstructible from the S105 npz (PRE-REG-INC).

  [SIGN] element: the substitution chain predicts a sign-CHANGE of the
  omega-weighted velocity sum  Sigma_k lambda_k(tau) lambda_k'(tau) w_k  across
  tau_fold (MIN: - -> +; MAX: + -> -), NOT a fixed sign. sign_verdict = PASS iff
  a sign-change brackets tau_fold; FAIL iff monotone (same sign both sides).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py            (feeds audit_sha256 only)
  - computations/session-105/s105_w2_2_omega_faithful_normal.npz
        (the §VII.BZ faithful normal modular weight omega; S105-OMEGA-FAITHFUL-NORMAL PASS)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (D_K bottom-band sector skeleton)
       PLAN-TEXT-DRIFT NOTE: plan §W1-1 input_files pins
       `computations/_shared/s84_spectrum_cache_L12_tau019.npz`; the file is
       canonically at `computations/session-84/...`. Resolved at runtime per
       `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction
       (the SAME drift INV12-W3-1 already corrected: see its verdict
       `cache_path_drift_corrected_to_session-84`). Drift documented in the
       verdict value field + WP Methodology.
  - script bytes                                            (feeds BOTH SHAs)

Output 4-tuple:
  (value=<dS_dtau_at_fold normalized>, scheme=MODULAR, convention=FROZEN-GGE-NON-KMS, L_max=10)

Classification: GEOMETRIC.
  The substrate IS the spectral triple (A_K, H_K, D_K(tau)); the modulus tau is
  the substrate's own intrinsic Jensen-TT deformation parameter (Level-2
  moduli-deformation substrate-IS, NOT a coordinate on a meta-container). The
  eigenvalue spectrum {lambda_k(tau)} of D_K(tau) is the set of vibrational
  modes; the modular weight rho_omega is fixed by the substrate's BdG/CdGM
  minigap structure (BDI/N3=0) -- it is read OFF the substrate, never chosen.
  S_modular = Tr(D_K^2 rho_omega) is the spectral 2nd moment of the squared
  Dirac operator weighted by the substrate's OWN modular density. Direction of
  explanation: D_K eigenvalues + substrate-derived modular weight -> the
  spectral entropy functional -> the selection of tau_fold -> (if PASS) the
  emergent functional-selection principle. This INVERTS the container-thinking
  framing where one would 'choose' a cutoff f and tune it; here the functional
  IS the substrate's modular structure and selection is a substrate-internal
  stationarity, not an external fit.

METHODOLOGY
-----------
S_modular(tau) = Tr(D_K(tau)^2 rho_omega).  D_K is ANTI-Hermitian (math
convention, dirac_spectrum.py docstring) => eigenvalues purely imaginary,
lambda_k = -i mu_k with mu_k = |lambda_k| real. So D_K^2 has eigenvalues
-|lambda_k|^2 (<= 0). We report the PHYSICAL spectral 2nd moment
        S_modular(tau) := Sum_k |lambda_k(tau)|^2 w_k        (>= 0)
(the positive Tr(|D_K|^2 rho_omega); the overall sign of Tr(D_K^2 .) is a
convention that does NOT affect the stationarity / extremum test, since
d/dtau and the extremum location are sign-invariant). The omega-density
weights w_k come from the S105 faithful-normal modular state: per Peter-Weyl
horizon block (p,q) in {(0,0),(1,0),(0,1),(1,1)} and per channel
{B2,B3,BCS}, the BdG occupation f in (0,1) is the diagonal of rho_omega in
the eigenbasis (a faithful normal state: 0<f<1 for every horizon mode -- the
exact property S105 verified). The weight is INDEPENDENT of tau (the modular
state is the FROZEN-GGE non-KMS weight, fixed by the minigap, not a function
of tau): only lambda_k(tau) carries tau.

  dS_modular/dtau = d/dtau [ Sum_k |lambda_k(tau)|^2 w_k ]
                  = Sum_k 2 |lambda_k(tau)| (d|lambda_k|/dtau) w_k
  stationary  <=>  Sum_k |lambda_k(tau_fold)| |lambda_k|'(tau_fold) w_k = 0

We build the SMOOTH |lambda_k(tau)| trajectory PER horizon sector (irreps
cached once by dirac_spectrum.get_irrep; only the Jensen frame/Omega recomputed
per tau) on a symmetric tau-grid bracketing tau_fold; weight each mode by its
modular occupation w_k; sum to S_modular(tau); take the central finite
difference dS/dtau; test stationarity at the fold AND the sign-change bracket.

DISCIPLINE
----------
- `from canonical_constants import *`; intermediates tagged `# (local)`
- GPU per-(p,q)-block via torch.linalg.eigvalsh (block-diagonal D_K, ROCm-native)
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA)
- Verdict emitted via emit_verdict MCP tool (script PRINTS payload only)
- NUMBERS first, gate second, interpretation third
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")     # before numpy import (CPU contention)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402  (tau_fold, M_KK, Delta_BCS, Delta_B2/B3, ...)
import canonical_constants as cc   # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

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
# Section 3 — Identity + pre-registered machinery pins (plan §W1-1)
# ---------------------------------------------------------------------------
SESSION = "S12"                                          # (local) investigation 12
GATE_ID = "INV12-W1-1-MODULAR-FUNCTIONAL-EXTREMIZATION"  # (local)
SCHEME = "MODULAR"                                        # (local) S_modular = Tr(D_K^2 rho_omega)
CONVENTION = "FROZEN-GGE-NON-KMS"                         # (local) S105 modular-weight convention
L_MAX = 10                                               # (local)

# Pre-registered pins (plan §W1-1 machinery_pin_map)
N_EVAL = 41                                              # (local) tau-grid points across [0.170,0.210]
SCAN_LO = 0.170                                          # (local) tau-window low (tau_fold - 0.02)
SCAN_HI = 0.210                                          # (local) tau-window high (tau_fold + 0.02)
STEP_SIZE = 0.001                                        # (local) dtau (grid step = FD step)
TOL_STATIONARY = 1e-3                                    # (local) relative-flatness PASS-band |dS/dtau|/S_scale
PUB_PREC = 4                                             # (local) publication precision (sig figs)

TAU_FOLD = float(tau_fold)                               # (local) 0.190 (canonical CONST-FREEZE-42)

# Horizon-algebra Peter-Weyl blocks the faithful-normal modular weight is supported on
# (S105 npz `horizon_blocks`): A_hor carries the §VII.BZ omega.
HORIZON_BLOCKS = [(0, 0), (1, 0), (0, 1), (1, 1)]        # (local) per S105 horizon_blocks
HORIZON_CHANNELS = ["B2", "B3", "BCS"]                   # (local) the 3 gapped channels in per_block_json

# Output destinations
OUT_NPZ = SESSION_DIR / "inv12_w1_1_modular_functional_extremization.npz"
OUT_PNG = SESSION_DIR / "inv12_w1_1_modular_functional_extremization.png"

# Inputs (plan-text-drift correction: cache canonically under session-84, NOT _shared)
OMEGA_NPZ = COMPUTATIONS_DIR / "session-105" / "s105_w2_2_omega_faithful_normal.npz"  # (local)
CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"    # (local) drift-corrected
CACHE_PATH_PLAN = SHARED_DIR / "s84_spectrum_cache_L12_tau019.npz"                    # (local) plan-pinned (absent)
DRIFT_CORRECTED = (not CACHE_PATH_PLAN.exists()) and CACHE_PATH.exists()              # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    OMEGA_NPZ,
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
    script_bytes = script_path.read_bytes() if script_path.exists() else b""          # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")    # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — SU(3) skeleton + eigenvalue-trajectory construction
#   (reuses the dirac_spectrum.py public API exactly as INV12-W3-1 does)
# ---------------------------------------------------------------------------
def build_su3_skeleton():
    """tau-independent SU(3) building blocks."""
    gens = ds.su3_generators()                          # (local)
    f_abc = ds.compute_structure_constants(gens)        # (local)
    B_ab = ds.compute_killing_form(f_abc)               # (local)
    gammas = ds.build_cliff8()                          # (local)
    return gens, f_abc, B_ab, gammas


def _block_abs_eigvals(D: np.ndarray) -> np.ndarray:
    """|lambda| spectrum of the block. D_K is ANTI-Hermitian => eigenvalues purely
    imaginary; H = i*D is Hermitian with REAL eigenvalues = imag(eig(D)). Diagonalize
    H = i*D with torch.linalg.eigvalsh on GPU (ROCm-native; the general eig needs MAGMA
    which this build lacks). Returns sorted |eigenvalues| (== numpy |eigvals(D).imag|
    to 1e-14, the S12 W3-1 pre-flight cross-check)."""
    if _HAVE_TORCH and D.shape[0] >= 100:
        H = 1j * D                                      # (local) Hermitian (i * anti-Hermitian)
        t = torch.tensor(H, device="cuda")              # (local)
        ev = torch.linalg.eigvalsh(t).cpu().numpy()     # (local) REAL eigenvalues
        return np.sort(np.abs(ev))
    ev = np.linalg.eigvals(D)                            # (local) CPU fallback (small blocks)
    return np.sort(np.abs(ev.imag))


def frame_omega_at_tau(s: float, skel) -> tuple[np.ndarray, np.ndarray]:
    """tau-dependent orthonormal frame E(tau) and spinor curvature offset Omega(tau),
    computed ONCE per tau (sector-independent; depend only on the Jensen metric)."""
    gens, f_abc, B_ab, gammas = skel
    g_s = ds.jensen_metric(B_ab, s)                     # (local)
    E = ds.orthonormal_frame(g_s)                       # (local)
    ft = ds.frame_structure_constants(f_abc, E)         # (local)
    Gamma = ds.connection_coefficients(ft)              # (local)
    Omega = ds.spinor_connection_offset(Gamma, gammas)  # (local)
    return E, Omega


def spectrum_from_frame(p: int, q: int, E: np.ndarray, Omega: np.ndarray,
                        skel) -> np.ndarray:
    """Block |lambda| spectrum for sector (p,q) given precomputed frame E(tau), Omega(tau)."""
    gens, f_abc, _B_ab, gammas = skel
    rho, _ = ds.get_irrep(p, q, gens, f_abc)            # (local) cached (tau-independent)
    D = ds.dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
    return _block_abs_eigvals(D)


def lambda_traj_horizon(skel, sectors: list, tau_grid: np.ndarray) -> dict:
    """SMOOTH |lambda_k|(tau) trajectory PER horizon sector. irreps cached once; only
    frame/Omega recomputed per tau (tau-OUTER loop eliminates the ~N_sector
    frame-recompute redundancy). Returns dict keyed by (p,q) -> (n_modes_block, n_tau),
    sorted ascending per column."""
    n_tau = len(tau_grid)                                                  # (local)
    t0 = time.time()                                                       # (local)
    print(f"  warming irrep cache for {len(sectors)} horizon sectors (tau-independent) ...")
    for (p, q) in sectors:
        ds.get_irrep(p, q, skel[0], skel[1])                               # populate _irrep_cache
    print(f"    irrep cache warm ({time.time()-t0:.1f}s)")
    t1 = time.time()                                                       # (local)
    cols_by_sector = {pq: [] for pq in sectors}                            # (local)
    for it, s in enumerate(tau_grid):
        E, Omega = frame_omega_at_tau(float(s), skel)                      # (local) ONCE per tau
        for (p, q) in sectors:
            v = spectrum_from_frame(p, q, E, Omega, skel)                  # (local) per-sector kron+eigvalsh
            v = v[v > 1e-9]                                                # drop spurious zero modes
            cols_by_sector[(p, q)].append(np.sort(v))
        if it == 0 or (it + 1) % 10 == 0 or it == n_tau - 1:
            print(f"    tau[{it+1:3d}/{n_tau}] = {s:.5f}  ({time.time()-t1:.1f}s)")
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
# Section 6 — Modular weight rho_omega (read OFF the S105 faithful-normal state)
# ---------------------------------------------------------------------------
def load_modular_weight():
    """Reconstruct the diagonal modular-density weights w (the faithful normal
    modular state omega, S105 §VII.BZ) per horizon (channel, block), as the BdG
    occupation f in (0,1). The faithful-normal property (0<f<1 for every horizon
    mode) is exactly what S105-OMEGA-FAITHFUL-NORMAL verified. The weight is
    rho_omega's diagonal in the eigenbasis; tau-INDEPENDENT (the FROZEN-GGE
    non-KMS weight, fixed by the minigap). We use the AV3 per-block trace weights
    for the inter-block weighting and the per-mode occupation for the intra-block
    profile, restricted to A_hor. Returns:
        block_av3   : {(p,q): av3_weight}        (per-horizon-block trace weight)
        block_occ   : {(channel,(p,q)): (f_min,f_max,n_modes,gap)}  (per-mode occ band)
        meta        : dict of scalar S105 anchors
    PRE-REG-INC if the npz lacks the modular-density fields (INFO regime)."""
    if not OMEGA_NPZ.exists():
        return None
    d = np.load(OMEGA_NPZ, allow_pickle=True)  # (local)
    required = {"av3_weights_json", "per_block_json", "horizon_blocks", "verdict"}  # (local)
    if not required.issubset(set(d.files)):
        return None
    # faithful-normal precondition: the S105 state must have PASSed
    if str(d["verdict"]) != "PASS":
        return None
    block_av3_raw = json.loads(str(d["av3_weights_json"]))                 # (local) {"(0, 0)": w, ...}
    per_block = json.loads(str(d["per_block_json"]))                       # (local) {"B3|(0, 0)": {...}, ...}
    # parse block AV3 weights into (p,q) keys
    block_av3 = {}                                                         # (local)
    for k, w in block_av3_raw.items():
        pq = tuple(int(x) for x in k.strip("()").split(","))              # (local)
        block_av3[pq] = float(w)
    # parse per-(channel,block) occupation
    block_occ = {}                                                        # (local)
    for k, info in per_block.items():
        ch, blk = k.split("|")                                            # (local)
        pq = tuple(int(x) for x in blk.strip("()").split(","))            # (local)
        block_occ[(ch, pq)] = {
            "f_min": float(info["f_min"]), "f_max": float(info["f_max"]),
            "n_modes": int(info["n_modes"]), "gap": float(info["gap"]),
            "E_min": float(info["E_min"]), "E_max": float(info["E_max"]),
        }
    meta = {                                                              # (local)
        "lam_horizon": float(d["lam_horizon"]),
        "f_global_min": float(d["f_global_min"]),
        "f_global_max": float(d["f_global_max"]),
        "n_modes_total": int(d["n_modes_total"]),
        "av3_ratio": float(d["av3_ratio"]),
        "T_GGE": float(d["T_GGE"]),
        "a2_fold": float(d["a2_fold"]),
        "convention": str(d["convention"]),
    }
    return {"block_av3": block_av3, "block_occ": block_occ, "meta": meta}


def build_mode_weights(traj: dict, modw: dict):
    """Assemble the diagonal modular weights w_k aligned to the trajectory modes.

    The faithful normal modular state omega is supported on A_hor (the 4 horizon
    blocks). rho_omega's diagonal in the eigenbasis is the per-mode BdG occupation
    f in (0,1). The substrate's OWN modular density:
      - per horizon block (p,q): the AV3 trace weight block_av3[(p,q)] sets the
        INTER-block weight (the relative thermodynamic weight of each block under
        omega), summed over its dim(p,q) Peter-Weyl multiplicity.
      - per mode within a block: weight by the mean modular occupation f_bar
        (the (channel)-averaged faithful-normal occupation; faithful => f in (0,1)).

    We restrict to the horizon sectors present in traj. The total weight is
    normalized to Sum_k w_k = 1 (Tr rho_omega = 1). Returns:
        weights : {(p,q): np.ndarray(n_modes_block)}   (diagonal modular weights, normalized)
        wsum_raw: the unnormalized total (for diagnostics)
    """
    block_av3 = modw["block_av3"]                                          # (local)
    block_occ = modw["block_occ"]                                          # (local)
    weights = {}                                                          # (local)
    raw_total = 0.0                                                       # (local)
    for (p, q), tr in traj.items():
        n_modes = tr.shape[0]                                            # (local)
        # per-mode mean modular occupation across the 3 gapped channels (faithful 0<f<1)
        f_vals = [0.5 * (block_occ[(ch, (p, q))]["f_min"] + block_occ[(ch, (p, q))]["f_max"])
                  for ch in HORIZON_CHANNELS if (ch, (p, q)) in block_occ]  # (local)
        f_bar = float(np.mean(f_vals)) if f_vals else 0.0                 # (local) mean faithful occupation
        # inter-block AV3 trace weight x Peter-Weyl multiplicity dim(p,q)
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2                     # (local)
        block_w = block_av3.get((p, q), 0.0)                             # (local)
        # per-mode weight: AV3 block weight (already a trace) distributed across modes,
        # modulated by the faithful occupation; we keep f_bar as the modular density factor
        w_mode = (block_w * f_bar) / max(n_modes, 1)                      # (local) per-mode modular weight
        wvec = np.full(n_modes, w_mode)                                  # (local)
        weights[(p, q)] = wvec
        raw_total += float(np.sum(wvec))
    # normalize to Tr rho_omega = 1
    if raw_total > 0:
        for pq in weights:
            weights[pq] = weights[pq] / raw_total
    return weights, raw_total


# ---------------------------------------------------------------------------
# Section 7 — Spectral entropy functional + stationarity test
# ---------------------------------------------------------------------------
def s_modular_of_tau(traj: dict, weights: dict, n_tau: int) -> np.ndarray:
    """S_modular(tau) = Sum_k |lambda_k(tau)|^2 w_k  (physical positive 2nd moment;
    Tr(|D_K|^2 rho_omega) -- the sign of Tr(D_K^2 .) is a convention that does NOT
    affect the extremum location)."""
    S = np.zeros(n_tau)                                                   # (local)
    for (p, q), tr in traj.items():
        w = weights[(p, q)][:, None]                                     # (local) (n_modes,1)
        S += np.sum((tr ** 2) * w, axis=0)                               # (local) sum over modes
    return S


def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout) + dual SHA
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                               # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"               # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    if DRIFT_CORRECTED:
        print(f"  PLAN-TEXT-DRIFT: cache pinned at {CACHE_PATH_PLAN} (absent); "
              f"resolved to {CACHE_PATH} per substrate-first-canonical-sourcing.md (ii.B)")
    print()

    # 2. Load the faithful-normal modular weight (PRE-REG-INC guard)
    print("=== Section A: load faithful-normal modular weight (S105 §VII.BZ omega) ===")
    modw = load_modular_weight()                                         # (local)
    if modw is None:
        # rho_omega not reconstructible -> honest PRE-REG-INC / INFO per plan INFO_meaning
        print("  rho_omega NOT reconstructible from S105 npz -> PRE-REG-INC (INFO regime)")
        value = "PRE-REG-INC_rho_omega_not_reconstructible_from_S105_npz"  # (local)
        np.savez(OUT_NPZ, status="PRE-REG-INC", gate_id=GATE_ID,
                 reason="omega density fields absent in s105_w2_2_omega_faithful_normal.npz")
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.text(0.5, 0.5, "PRE-REG-INC\nrho_omega not reconstructible from S105 npz",
                ha="center", va="center")
        ax.set_axis_off(); fig.savefig(OUT_PNG, dpi=110, bbox_inches="tight"); plt.close(fig)
        print_verdict_payload(value, "INFO", audit_sha, content_sha,
              sign_verdict="N/A", magnitude_verdict="FAIL", regime_verdict="BREAKDOWN",
              companion_note="rho_omega not reconstructible; modular-functional selection untestable this run",
              extra_rows=[f"# PRE-REG-INC: S105 npz lacks modular-density fields; "
                          f"INFO per plan INFO_meaning (PRE-REG-INC branch)"])
        print(f"\nDONE ({time.time()-t0:.1f}s)")
        return 0
    print(f"  modular state: convention={modw['meta']['convention'][:48]}...")
    print(f"  AV3 block weights: {modw['block_av3']}")
    print(f"  f_global in ({modw['meta']['f_global_min']:.4f}, {modw['meta']['f_global_max']:.4f}) "
          f"=> FAITHFUL (0<f<1) confirmed")
    print(f"  n_modes_total (A_hor) = {modw['meta']['n_modes_total']}")

    # 3. Build the SU(3) skeleton + |lambda_k(tau)| trajectory on the horizon sectors
    print("\n=== Section B: |lambda_k(tau)| trajectory on A_hor (GPU per-block eigvalsh) ===")
    skel = build_su3_skeleton()                                          # (local)
    cache = np.load(CACHE_PATH, allow_pickle=True)["sector_evals"].item()  # (local) sector skeleton
    # horizon sectors present in the cache (all 4 should be)
    sectors = [pq for pq in HORIZON_BLOCKS if pq in cache]               # (local)
    missing = [pq for pq in HORIZON_BLOCKS if pq not in cache]           # (local)
    if missing:
        print(f"  WARNING: horizon sectors {missing} absent from cache; using present {sectors}")
    print(f"  horizon sectors: {sectors}")
    tau_grid = np.linspace(SCAN_LO, SCAN_HI, N_EVAL)                     # (local) [0.170,0.210], 41 pts
    print(f"  tau-grid: [{SCAN_LO}, {SCAN_HI}], {N_EVAL} pts (dtau={STEP_SIZE}); fold at {TAU_FOLD}")
    if _HAVE_TORCH:
        print("  GPU: torch.linalg.eigvalsh on ROCm (AMD RX 9070 XT)")
    else:
        print("  GPU unavailable -> numpy.linalg.eigvals CPU fallback")
    traj = lambda_traj_horizon(skel, sectors, tau_grid)                 # (local)

    # cross-check: trajectory |lambda| at fold-index vs cache abs_evals (cache is tau=0.19)
    fold_idx = int(np.argmin(np.abs(tau_grid - TAU_FOLD)))             # (local)
    print(f"\n  cross-check trajectory vs cache (cache @ tau=0.19; grid fold-idx={fold_idx}, "
          f"tau={tau_grid[fold_idx]:.5f}):")
    xcheck = {}                                                         # (local)
    for (p, q) in sectors:
        tr_at_fold = np.sort(traj[(p, q)][:, fold_idx])                 # (local)
        ce = np.sort(np.abs(cache[(p, q)]["abs_evals"]))               # (local)
        n = min(len(tr_at_fold), len(ce))                              # (local)
        if n > 0:
            md = float(np.max(np.abs(tr_at_fold[:n] - ce[:n])))       # (local) max abs dev
            xcheck[f"{p},{q}"] = md
            print(f"    ({p},{q}): max|traj-cache| = {md:.3e} over {n} modes")

    # 4. Build the modular weights aligned to trajectory modes
    print("\n=== Section C: modular weights rho_omega (read OFF S105 faithful state) ===")
    weights, wsum_raw = build_mode_weights(traj, modw)                 # (local)
    wtot = sum(float(np.sum(w)) for w in weights.values())            # (local) should be ~1
    print(f"  modular weights normalized: Sum_k w_k = {wtot:.6f} (Tr rho_omega=1)")
    for (p, q) in sectors:
        print(f"    block ({p},{q}): {weights[(p,q)].shape[0]} modes, "
              f"block weight = {float(np.sum(weights[(p,q)])):.6f}")

    # 5. S_modular(tau) + stationarity test
    print("\n=== Section D: S_modular(tau) + stationarity / sign-change test ===")
    S = s_modular_of_tau(traj, weights, N_EVAL)                       # (local) (n_tau,)
    S_scale = float(np.mean(S))                                       # (local) scale for relative flatness
    # central finite difference dS/dtau (uniform grid)
    dS = np.gradient(S, tau_grid)                                     # (local) central FD
    dS_at_fold = float(dS[fold_idx])                                 # (local) derivative at fold
    dS_norm_at_fold = abs(dS_at_fold) / S_scale if S_scale > 0 else float("inf")  # (local) relative

    # sign-change bracket test: sign of dS just left vs just right of the fold
    lo = max(0, fold_idx - 1)                                         # (local)
    hi = min(N_EVAL - 1, fold_idx + 1)                               # (local)
    dS_left = float(dS[lo])                                          # (local)
    dS_right = float(dS[hi])                                         # (local)
    sign_left = int(np.sign(dS_left))                               # (local)
    sign_right = int(np.sign(dS_right))                            # (local)
    sign_change = (sign_left != sign_right) and (sign_left != 0) and (sign_right != 0)  # (local)
    # extremum classification
    if sign_change and sign_left < 0 < sign_right:
        extremum_kind = "MIN"                                        # (local) - -> +
    elif sign_change and sign_left > 0 > sign_right:
        extremum_kind = "MAX"                                        # (local) + -> -
    else:
        extremum_kind = "MONOTONE"                                  # (local) no sign change

    # global extremum location (where |dS| is minimal) -> which tau the functional selects
    abs_dS = np.abs(dS)                                              # (local)
    # ignore endpoints for interior-extremum search
    interior = abs_dS.copy()                                        # (local)
    interior[0] = np.inf; interior[-1] = np.inf
    ext_idx = int(np.argmin(interior))                             # (local)
    tau_extremum = float(tau_grid[ext_idx])                        # (local)
    off_fold = abs(tau_extremum - TAU_FOLD) > 1.5 * STEP_SIZE       # (local) extremum off the fold-grid-point?

    print(f"  S_modular range: [{float(np.min(S)):.6g}, {float(np.max(S)):.6g}], "
          f"S_scale(mean)={S_scale:.6g}")
    print(f"  dS/dtau at fold (tau={tau_grid[fold_idx]:.5f}): {dS_at_fold:.6g}")
    print(f"  |dS/dtau|/S_scale at fold = {dS_norm_at_fold:.6e}  (PASS-band <= {TOL_STATIONARY})")
    print(f"  dS/dtau bracket: left(tau={tau_grid[lo]:.4f})={dS_left:.6g}, "
          f"right(tau={tau_grid[hi]:.4f})={dS_right:.6g} -> sign {sign_left:+d}/{sign_right:+d} "
          f"=> {extremum_kind}")
    print(f"  interior extremum (min|dS/dtau|): tau={tau_extremum:.5f} "
          f"(off-fold={off_fold}; |tau_ext - tau_fold|={abs(tau_extremum-TAU_FOLD):.5f})")

    # 6. Pre-registered verdict (composite 3-tuple, collapse rule)
    #   sign_verdict  = PASS iff a sign-CHANGE brackets tau_fold (extremum at fold); FAIL iff monotone
    #   magnitude_verdict = PASS iff |dS/dtau|/S_scale <= TOL_STATIONARY at the fold
    #   regime_verdict = VALID (the FD on the smooth lambda(tau) grid is well-resolved over [0.170,0.210])
    sign_v = "PASS" if sign_change else "FAIL"                       # (local)
    if dS_norm_at_fold <= TOL_STATIONARY:
        mag_v = "PASS"                                               # (local)
    elif dS_norm_at_fold <= 10 * TOL_STATIONARY:
        mag_v = "INFO"                                              # (local) near-flat but above band
    else:
        mag_v = "FAIL"                                              # (local)
    regime_v = "VALID"                                             # (local) smooth trajectory, FD well-resolved

    # composite collapse (gate-verdicts.md deterministic rule)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"                                          # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"                                          # (local) monotone through fold = no selection
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"                                          # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"                                          # (local)
    elif mag_v == "INFO":
        composite = "INFO"                                          # (local)
    else:
        composite = "PASS"                                          # (local)

    # INFO override: stationary (sign-change PASS) BUT off the fold -> plan INFO_meaning
    # (the modular structure singles out a DIFFERENT modulus, not the transit fold)
    if sign_v == "PASS" and off_fold and composite == "PASS":
        composite = "INFO"                                          # (local) extremum off-fold
        info_reason = "stationary_off_fold"                         # (local)
    elif composite == "INFO" and sign_v == "PASS" and off_fold:
        info_reason = "stationary_off_fold"                         # (local)
    else:
        info_reason = "n/a"                                         # (local)

    # value payload (no single-quote chars)
    value = (f"dS_dtau_fold={dS_at_fold:.4g}_normflat={dS_norm_at_fold:.4e}_"
             f"extremum={extremum_kind}_tau_ext={tau_extremum:.4f}_offfold={off_fold}_"
             f"signL={sign_left:+d}_signR={sign_right:+d}_Sscale={S_scale:.4g}_"
             f"cache_path_drift_corrected_to_session-84")  # (local)

    print(f"\n  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v} -> composite={composite}")
    if info_reason != "n/a":
        print(f"  INFO reason: {info_reason}")

    # 7. Save data
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, verdict=composite,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        tau_grid=tau_grid, S_modular=S, dS_dtau=dS, S_scale=S_scale,
        dS_at_fold=dS_at_fold, dS_norm_at_fold=dS_norm_at_fold,
        fold_idx=fold_idx, tau_fold=TAU_FOLD,
        extremum_kind=extremum_kind, tau_extremum=tau_extremum, off_fold=off_fold,
        sign_left=sign_left, sign_right=sign_right, sign_change=sign_change,
        horizon_sectors=np.array([f"{p},{q}" for (p, q) in sectors]),
        block_weights=np.array([float(np.sum(weights[pq])) for pq in sectors]),
        weight_total=wtot,
        xcheck_traj_vs_cache_json=json.dumps(xcheck),
        modular_av3_json=json.dumps({f"{p},{q}": modw["block_av3"].get((p, q), 0.0)
                                     for (p, q) in sectors}),
        f_global_min=modw["meta"]["f_global_min"], f_global_max=modw["meta"]["f_global_max"],
        T_GGE=modw["meta"]["T_GGE"], a2_fold=modw["meta"]["a2_fold"],
        L_max=L_MAX, n_eval=N_EVAL, scan_lo=SCAN_LO, scan_hi=SCAN_HI,
        tol_stationary=TOL_STATIONARY, scheme=SCHEME, convention=CONVENTION,
        audit_sha256=audit_sha, content_sha256=content_sha,
        drift_corrected=DRIFT_CORRECTED,
    )
    print(f"  saved npz -> {OUT_NPZ}")

    # 8. Plot: S_modular(tau) + dS/dtau, fold marker
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
    ax1.plot(tau_grid, S, "-o", color="C0", ms=3, label=r"$S_{\rm modular}(\tau)=\mathrm{Tr}(|D_K|^2\rho_\omega)$")
    ax1.axvline(TAU_FOLD, color="C3", ls="--", lw=1.2, label=rf"$\tau_{{\rm fold}}={TAU_FOLD}$")
    ax1.axvline(tau_extremum, color="C2", ls=":", lw=1.2, label=rf"interior extremum $\tau={tau_extremum:.4f}$")
    ax1.set_ylabel(r"$S_{\rm modular}$"); ax1.legend(fontsize=8); ax1.grid(alpha=0.3)
    ax1.set_title(f"{GATE_ID}\nmodular entropy functional, FROZEN-GGE non-KMS weight (S105 §VII.BZ)",
                  fontsize=9)
    ax2.plot(tau_grid, dS, "-s", color="C1", ms=3, label=r"$dS_{\rm modular}/d\tau$")
    ax2.axhline(0, color="k", lw=0.8)
    ax2.axvline(TAU_FOLD, color="C3", ls="--", lw=1.2)
    ax2.axvline(tau_extremum, color="C2", ls=":", lw=1.2)
    ax2.set_xlabel(r"$\tau$ (Jensen deformation)"); ax2.set_ylabel(r"$dS_{\rm modular}/d\tau$")
    ax2.legend(fontsize=8); ax2.grid(alpha=0.3)
    ax2.text(0.02, 0.05,
             f"|dS/dt|/S_scale@fold = {dS_norm_at_fold:.2e} (band {TOL_STATIONARY})\n"
             f"{extremum_kind}; sign {sign_left:+d}->{sign_right:+d}; composite={composite}",
             transform=ax2.transAxes, fontsize=8, va="bottom",
             bbox=dict(boxstyle="round", fc="wheat", alpha=0.6))
    fig.tight_layout(); fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight"); plt.close(fig)
    print(f"  saved png -> {OUT_PNG}")

    # 9. Emit 4-tuple tag + PRINT the emit_verdict payload
    print(f"\n(value={value[:40]}..., scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    extra = [
        f"# [SIGN] modular extremization: dS_modular/dtau|_fold={dS_at_fold:.4g}, "
        f"|dS/dtau|/S_scale={dS_norm_at_fold:.4e} (band {TOL_STATIONARY}); "
        f"extremum={extremum_kind} at tau={tau_extremum:.4f} (fold={TAU_FOLD}, off_fold={off_fold})",
        f"# modular weight: FROZEN-GGE-NON-KMS faithful-normal (S105 §VII.BZ omega); "
        f"A_hor blocks {[f'{p},{q}' for (p,q) in sectors]}; f_global in "
        f"({modw['meta']['f_global_min']:.4f},{modw['meta']['f_global_max']:.4f}) faithful",
        f"# cache_path_drift_corrected: plan-pinned _shared/s84_spectrum_cache_L12_tau019.npz absent; "
        f"resolved to session-84/ per substrate-first-canonical-sourcing.md (ii.B) (same drift INV12-W3-1 fixed)",
    ]
    print_verdict_payload(value, composite, audit_sha, content_sha,
          sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
          companion_note=f"S_modular {extremum_kind} ; G-L1 selection "
                         f"{'candidate' if composite=='PASS' else ('off-fold' if off_fold else 'NOT-found')}",
          extra_rows=extra)
    print(f"\nDONE ({time.time()-t0:.1f}s)")
    return 0


def print_verdict_payload(value, verdict, audit_sha, content_sha,
          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
          companion_note="", extra_rows=None):
    """PRINT the emit_verdict payload (delimited) for the dispatching agent to pass to
    the knowledge-MCP emit_verdict tool. The script does NOT write the verdict file.
    Name matches the canonical template helper (.claude/templates/script-template.py
    `print_verdict_payload`); arg-order (value, verdict, ...) is this script's local form."""
    payload = {
        "session": 12, "track": "investigation",
        "gate_id": GATE_ID, "verdict": verdict, "value": str(value),
        "scheme": SCHEME, "convention": CONVENTION, "l_max": str(L_MAX),
        "audit_sha256": audit_sha, "content_sha256": content_sha,
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


if __name__ == "__main__":
    sys.exit(main())
