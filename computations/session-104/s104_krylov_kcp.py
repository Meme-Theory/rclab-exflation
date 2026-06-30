#!/usr/bin/env python3
"""
S104 W3-1 — S104-KRYLOV-KCP — Krylov-complexity peak on the (2,1) Peter-Weyl sector of D_K
==========================================================================================

Gate: S104-KRYLOV-KCP ([SIGN])

Pre-registered threshold (operator type = set; two-branch SIGN comparison + bounded residual):
  PASS iff  sign(KCP_fold - KCP_ref) == sign(beta_fold - beta_ref) == +1
        AND |KCP_fold - KCP_ref * R_implied| / (KCP_ref * R_implied) <= 0.15
  INFO  iff  sign holds (+1) but relative residual > 0.15
  FAIL  iff  sign(KCP_fold - KCP_ref) != sign(beta_fold - beta_ref)   (SIGN MISMATCH)

Classification: GEOMETRIC — the Krylov-complexity peak is a spectral functional of the
D_K eigenvalue content (the fabric ITSELF, not its excitations). The flow:
  D_K |lambda| set on the (2,1) Peter-Weyl sector (the substrate's vibrational-mode spectrum
  at the fold)  ->  Delta-channel autocorrelation moment sequence mu_{2n}
  ->  ordinary Lanczos b_n ladder  ->  Krylov-complexity profile K(t)  ->  peak height KCP.

This is a FOURTH spectral-functional diagnostic of the SAME eigenvalue statistics that
CHAOS-1 (<r>=0.321), CHAOS-2 (OTOC C(t)~t^1.9, lambda_L=0), and FACTOR-46 (SFF, no-ramp INFO)
already read. Spectral-functional pluralism: different functionals of the SAME D_K spectrum
must agree on what is structural (the level-statistics class). KCP<->beta tests that agreement
against the Huh (2412.04963) monotone relation, with the pinned anchors:
  beta_fold = 0.633 (single-cell, 63% GOE on sector (2,1) at tau_fold) [INTEG-39, S96 re-confirm]
  beta_ref  = 0     (Poisson, integrable on sector (2,1) at tau=0)     [Fegan-closed reference]

SADDLE GUARD (Bhattacharjee 2203.03534): a LINEAR b_n growth (b_n ~ alpha*n) + early-time
K(t) growth is the textbook chaos signature BUT is produced ENTIRELY as a phase-space-saddle
artifact in INTEGRABLE systems. The substrate transits the van Hove fold tau=0.190 = an
A2-catastrophe SADDLE; the spectrum is PROVEN Poisson (CHAOS-1) and the OTOC PROVEN
sub-exponential (CHAOS-2). ANY linear b_n growth observed here is read as saddle-consistent
(integrable-at-a-saddle), NEVER as a Lyapunov exponent. The KCP<->beta SIGN test compares
peak HEIGHTS, not growth rates, so it is unaffected by the guard.

tau=0 REFERENCE — PRIMARY PATH (no deviation): the (2,1) sector at tau=0 is the bi-invariant
(Jensen s=0, all scale factors = 1) D_K, the canonical Fegan/Kostant closed-form object
(S102 W3-11 PASS). It is built FULL-physical via dirac_spectrum.py on the SAME (2,1) sector
to L_max=12 (get_irrep(2,1) = Sym^p / Casimir projection; dirac_operator_on_irrep at s=0).
A smoke check confirms the SAME pipeline at tau=0.19 reproduces the s84 cache (2,1) sector
bit-for-bit (min/max |lambda| identical), so the fold-from-cache vs tau0-fresh comparison is
like-for-like. The s92_spectrum_cache_L12_tau018/020 bracketing fallback is NOT used (declared:
the Fegan closed form IS directly evaluable at runtime).

Inputs (SHA-256 dual-pinned; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (fold (2,1) level set)
  - computations/_shared/dirac_spectrum.py                      (FULL tau=0 (2,1) build)
  - computations/_shared/canonical_constants.py                 (tau_fold, beta anchors)
  - script bytes

Author: kitaev-quantum-chaos-theorist
Session: S104 W3
Date: 2026-06-10
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # pinned cpu-cap-OMP8 (single-sector Lanczos is small)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.special import gamma as _gamma_fn
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical constants
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import tau_fold  # noqa: E402  (s=0 vs tau_fold=0.19 anchor)
import dirac_spectrum as tds              # noqa: E402  (FULL tau=0 (2,1) build)

SESSION = "S104"                                                    # (local)
GATE_ID = "S104-KRYLOV-KCP"                                         # (local)
SCHEME = "KRYLOV-LANCZOS-ORDINARY"                                  # (local)
CONVENTION = "MOMENT-SEQUENCE-FROM-SINGLE-SECTOR-LEVEL-SET"         # (local)
L_MAX = 12                                                          # (local) cache truncation

# ---- Pinned machinery (PRDR machinery_pin_map) ----
SECTOR_PIN = (2, 1)                                                 # (local) INTEG-39 / BRODY-PARAMETER-53 single-cell sector
N_LANCZOS_MAX_CAP = 200                                            # (local) min(len(abs_evals)-1, 200)
KRYLOV_GRID_N = 4000                                              # (local) linearly-spaced K(t) points
KRYLOV_TMAX_FACTOR = 3.0                                          # (local) t_max = factor / b1_gap
REL_RESIDUAL_BAND = 0.15                                           # (local) Class-8.3 rel_tol floor (qualitative-monotone Huh map)
EVAL_CUTOFF = 1e-6                                                 # (local) IR cutoff (S84 cache pattern)
DOS_FLOOR_FRAC = 1e-6                                              # (local) regularize local DOS at 1e-6 * median spacing
BRODY_CALIB_N = 240                                               # (local) sample size = (2,1)-sector |lambda| count
BRODY_CALIB_REPS = 24                                             # (local) realizations averaged for R_implied
BRODY_CALIB_SEED = 1040                                          # (local) deterministic RNG seed (calibration only)

# ---- Pinned anchors (canonical; NOT recomputed) ----
BETA_FOLD = 0.633                                                 # (local) INTEG-39 (S96 re-confirm); 63% GOE on (2,1) at tau_fold
BETA_REF = 0.0                                                    # (local) tau=0 Fegan-closed integrable reference, Poisson

# Output destinations
OUT_NPZ = SESSION_DIR / "s104_krylov_kcp.npz"
OUT_PNG = SESSION_DIR / "s104_krylov_kcp.png"

S84_FOLD_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "dirac_spectrum.py",
    S84_FOLD_CACHE,
    Path(__file__).resolve(),
]


# ---------------------------------------------------------------------------
# Section 2 — SHA-256 dual-pin block
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
            rel = str(p).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json); content_sha256 = sha256(script)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 3 — Krylov machinery (Delta-channel measure -> Lanczos b_n -> K(t) -> KCP)
# ---------------------------------------------------------------------------
def delta_channel_measure(levels: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Build the Delta-channel autocorrelation spectral function as a discrete measure.

    The operator-O channel is Delta = (Delta_gap + Delta_gap^dag)/sqrt(2), the SAME Hermitian
    BdG gap operator CHAOS-2 used for the OTOC: a DOS-weighted pairing that couples single-
    particle levels i<->j with amplitude |A_ij| ~ sqrt(rho_i rho_j) (rho_i = local DOS at
    level i, the Delta = sum_k sqrt(rho_k) P_k structure of s38_otoc_bcs.py).

    The infinite-temperature autocorrelation spectral function is
        Phi(omega) = sum_{i != j} |A_ij|^2 delta(omega - (lambda_i - lambda_j)),
    a discrete measure with support {omega_ij = lambda_i - lambda_j} and weights |A_ij|^2.
    Its even moments mu_{2n} = integral omega^{2n} Phi(omega) domega are the autocorrelation
    moments the Lanczos algorithm consumes (Phi is symmetric => odd moments vanish).
    """
    L = np.sort(np.asarray(levels, dtype=np.float64))  # (local)
    sp = np.diff(L)  # (local) nearest-neighbour spacings
    pos = sp[sp > 0]  # (local)
    med = np.median(pos) if pos.size else 1.0  # (local)
    sp_full = np.concatenate([[sp[0]], sp]) if sp.size else np.array([1.0])  # (local)
    sp_full = np.maximum(sp_full, DOS_FLOOR_FRAC * med)  # (local) regularize local DOS
    rho = 1.0 / sp_full  # (local) local DOS
    rho = rho / rho.mean()  # (local) normalize mean DOS to 1
    di = L[:, None] - L[None, :]  # (local) level-difference matrix omega_ij
    wij = np.sqrt(rho[:, None] * rho[None, :])  # (local) |A_ij| ~ sqrt(rho_i rho_j)
    w2 = wij ** 2  # (local) |A_ij|^2
    mask = ~np.eye(len(L), dtype=bool)  # (local) exclude diagonal (omega=0)
    return di[mask].flatten(), w2[mask].flatten()


def lanczos_from_measure(freqs: np.ndarray, weights: np.ndarray, n_max: int) -> np.ndarray:
    """Ordinary Lanczos b_n from a discrete spectral measure via the Stieltjes procedure.

    D_K is Hermitian (AZ class BDI) => ORDINARY (not bi-) Lanczos. The Stieltjes recursion
    builds the monic orthogonal polynomials wrt the measure {(omega_i, |A_i|^2)}; the Jacobi
    coefficients beta_n give the Krylov hopping amplitudes b_n = sqrt(beta_n). Terminates at
    numerical breakdown (beta_n -> 0 / orthogonality loss) or n_max, whichever first.
    """
    w = np.asarray(weights, dtype=np.float64)  # (local)
    x = np.asarray(freqs, dtype=np.float64)  # (local)
    sw = w.sum()  # (local)
    if sw <= 0 or not np.isfinite(sw):
        return np.array([0.0])
    w = w / sw  # (local) normalized measure (sum w = 1)
    n = int(n_max)  # (local)
    alpha = np.zeros(n)  # (local) Jacobi diagonal
    bsq = np.zeros(n)  # (local) Jacobi off-diagonal squared (beta_n)
    # ORTHONORMAL three-term recurrence (Lanczos on the measure): keep each polynomial
    # L2(w)-normalized so |q_j| stays O(1) -> NO overflow for clustered/wide measures.
    #   x q_j = b_{j+1} q_{j+1} + a_j q_j + b_j q_{j-1}
    q_prev = np.zeros_like(x)  # (local) q_{-1} = 0
    q_cur = np.ones_like(x) / np.sqrt(np.sum(w))  # (local) q_0 = 1 (already unit-norm since sum w = 1)
    nrm0 = np.sqrt(np.sum(w * q_cur * q_cur))  # (local)
    q_cur = q_cur / nrm0  # (local) enforce <q_0|q_0> = 1 exactly
    alpha[0] = np.sum(w * x * q_cur * q_cur)  # (local) a_0 = <q_0| x |q_0>
    last = n  # (local)
    for j in range(1, n):
        # r = (x - a_{j-1}) q_{j-1} - b_{j-1} q_{j-2}
        b_prev = np.sqrt(bsq[j - 1]) if j >= 2 else 0.0  # (local)
        r = (x - alpha[j - 1]) * q_cur - b_prev * q_prev  # (local)
        bj = np.sqrt(np.sum(w * r * r))  # (local) b_j = ||r||_{L2(w)}
        if (not np.isfinite(bj)) or bj <= 1e-140:
            last = j
            break
        bsq[j] = bj * bj
        q_next = r / bj  # (local) unit-normalized q_j -> magnitudes stay O(1)
        alpha[j] = np.sum(w * x * q_next * q_next)  # (local) a_j
        q_prev = q_cur
        q_cur = q_next
    bsq = bsq[:last]
    return np.sqrt(np.abs(bsq))


def krylov_complexity(bn: np.ndarray, tgrid: np.ndarray) -> np.ndarray:
    """K(t) = sum_n n |phi_n(t)|^2, |phi(t)> = exp(-i L t)|0>, L tridiagonal with b_n off-diagonals.

    The Krylov chain ODE dphi_n/dt = b_n phi_{n-1} - b_{n+1} phi_n is solved exactly via
    eigendecomposition of the (real symmetric) tridiagonal Krylov Liouvillian L.
    """
    Nd = len(bn)  # (local)
    if Nd < 2:
        return np.zeros(len(tgrid))
    Lm = np.zeros((Nd, Nd))  # (local) Krylov Liouvillian (tridiagonal)
    for nn in range(1, Nd):
        Lm[nn, nn - 1] = bn[nn]
        Lm[nn - 1, nn] = bn[nn]
    ev, evec = np.linalg.eigh(Lm)  # (local)
    phi0 = np.zeros(Nd)  # (local)
    phi0[0] = 1.0
    c = evec.T @ phi0  # (local) initial state in eigenbasis
    nvec = np.arange(Nd)  # (local) Krylov-site index
    Karr = np.zeros(len(tgrid))  # (local)
    for it, t in enumerate(tgrid):
        amp = evec @ (c * np.exp(-1j * ev * t))  # (local) phi_n(t)
        Karr[it] = np.sum(nvec * np.abs(amp) ** 2)
    return Karr


def kcp_from_levels(levels: np.ndarray, n_lanczos: int) -> dict:
    """Full pipeline level set -> Delta-channel measure -> b_n -> K(t) -> KCP. Returns a dict."""
    freqs, weights = delta_channel_measure(levels)
    bn = lanczos_from_measure(freqs, weights, n_lanczos)
    b1 = float(bn[1]) if len(bn) > 1 and bn[1] > 0 else 1.0  # (local) first Krylov gap
    tmax = KRYLOV_TMAX_FACTOR / max(b1, 1e-9)  # (local) PINNED grid (not chosen to land a peak)
    tgrid = np.linspace(0.0, tmax, KRYLOV_GRID_N)  # (local)
    Karr = krylov_complexity(bn, tgrid)
    kcp = float(np.max(Karr)) if Karr.size else 0.0  # (local)
    t_peak = float(tgrid[int(np.argmax(Karr))]) if Karr.size else 0.0  # (local)
    return {"bn": bn, "t": tgrid, "K": Karr, "KCP": kcp, "t_peak": t_peak, "b1": b1}


def fit_bn_growth_law(bn: np.ndarray) -> dict:
    """Linear-growth fit b_n ~ slope*n + intercept over the bulk Krylov region (saddle guard).

    A LINEAR growth (slope > 0, well-fit) is the Bhattacharjee saddle / chaos-signature law;
    a SATURATING ladder (slope ~ 0) is the bounded/integrable signature.
    """
    nn = np.arange(len(bn))  # (local)
    if len(bn) < 12:
        return {"slope": float("nan"), "intercept": float("nan"), "r2": float("nan"),
                "linear_growth": False, "n_fit_lo": -1, "n_fit_hi": -1}
    lo = 5  # (local) skip boundary transient
    hi = len(bn) - 5  # (local) skip terminal breakdown
    mask = (nn >= lo) & (nn < hi)  # (local)
    if mask.sum() < 4:
        return {"slope": float("nan"), "intercept": float("nan"), "r2": float("nan"),
                "linear_growth": False, "n_fit_lo": lo, "n_fit_hi": hi}
    coef = np.polyfit(nn[mask], bn[mask], 1)  # (local) [slope, intercept]
    slope, intercept = float(coef[0]), float(coef[1])  # (local)
    pred = slope * nn[mask] + intercept  # (local)
    ss_res = float(np.sum((bn[mask] - pred) ** 2))  # (local)
    ss_tot = float(np.sum((bn[mask] - bn[mask].mean()) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0  # (local)
    # "LINEAR growth" diagnostic: positive slope, well-fit, and growth meaningful vs spread.
    bn_spread = float(bn[mask].max() - bn[mask].min())  # (local)
    rise = slope * (hi - lo)  # (local) predicted rise across the fit window
    linear_growth = (slope > 0.0) and (r2 > 0.90) and (abs(rise) > 0.25 * max(bn_spread, 1e-9))  # (local)
    return {"slope": slope, "intercept": intercept, "r2": r2,
            "linear_growth": bool(linear_growth), "n_fit_lo": lo, "n_fit_hi": hi}


# ---------------------------------------------------------------------------
# Section 4 — R_implied: Huh monotone KCP<->beta height ratio via Brody calibration
# ---------------------------------------------------------------------------
def brody_spacings(beta: float, n: int, rng: np.random.Generator) -> np.ndarray:
    """Sample n spacings from the Brody distribution P(s)=(b+1) a s^b exp(-a s^{b+1}).

    a = Gamma((b+2)/(b+1))^{b+1} normalizes <s>=1. Inverse-CDF sampling:
    F(s)=1-exp(-a s^{b+1}) => s = (-ln(1-u)/a)^{1/(b+1)}.
    """
    a = _gamma_fn((beta + 2.0) / (beta + 1.0)) ** (beta + 1.0)  # (local)
    u = rng.random(n)  # (local)
    return (-np.log(1.0 - u) / a) ** (1.0 / (beta + 1.0))


def kcp_for_beta(beta: float, reps: int, n_levels: int, n_lanczos: int, rng: np.random.Generator) -> tuple[float, float]:
    """Mean +/- std KCP over Brody-distributed synthetic spectra at the given beta.

    This is the substrate-faithful empirical realization of the Huh qualitative-monotone
    KCP(beta) map: build a level set whose level statistics IS Brody-beta, run the SAME
    Delta-channel Krylov pipeline, read KCP. R_implied = KCP(beta_fold)/KCP(beta_ref).
    """
    vals = []  # (local)
    for _ in range(reps):
        s = brody_spacings(beta, n_levels, rng)  # (local)
        L = np.concatenate([[0.0], np.cumsum(s)])  # (local) integrated levels
        res = kcp_from_levels(L, n_lanczos)  # (local)
        if res["KCP"] > 0:
            vals.append(res["KCP"])
    if not vals:
        return float("nan"), float("nan")
    return float(np.mean(vals)), float(np.std(vals))


# ---------------------------------------------------------------------------
# Section 5 — tau=0 (2,1) reference build (PRIMARY Fegan/Sym^p path, FULL physical)
# ---------------------------------------------------------------------------
def build_sector_abs_evals(tau_val: float, pq: tuple[int, int]) -> np.ndarray:
    """Build |lambda| set for Peter-Weyl sector (p,q) of D_K at Jensen parameter tau_val.

    FULL physical path (dirac_spectrum.py), identical pipeline to the s84 / s92 cache builds:
      su3_generators -> structure_constants -> killing_form -> jensen_metric(tau) ->
      orthonormal_frame -> frame_structure_constants -> connection_coefficients ->
      build_cliff8 -> spinor_connection_offset -> get_irrep(p,q) [Sym^p/Casimir] ->
      dirac_operator_on_irrep -> H=i*D (Hermitian) -> eigvalsh -> |lambda| (IR-cut).
    At tau=0 the Jensen metric is bi-invariant (all scale factors = 1) => this IS the
    canonical Fegan/Kostant Dirac operator on round SU(3) (the S102 W3-11 PASS object).
    """
    gens = tds.su3_generators()  # (local)
    f_abc = tds.compute_structure_constants(gens)  # (local)
    B_ab = tds.compute_killing_form(f_abc)  # (local)
    g_s = tds.jensen_metric(B_ab, tau_val)  # (local)
    E_frame = tds.orthonormal_frame(g_s)  # (local)
    ft = tds.frame_structure_constants(f_abc, E_frame)  # (local)
    Gamma_conn = tds.connection_coefficients(ft)  # (local)
    gammas = tds.build_cliff8()  # (local)
    Omega = tds.spinor_connection_offset(Gamma_conn, gammas)  # (local)
    tds._irrep_cache.clear()
    rho, _ = tds.get_irrep(pq[0], pq[1], gens, f_abc)  # (local)
    D = tds.dirac_operator_on_irrep(rho, E_frame, gammas, Omega)  # (local)
    H = 1j * D  # (local) Hermitian form (eigenvalues of D are imaginary)
    H = 0.5 * (H + H.conj().T)  # (local)
    ev = np.linalg.eigvalsh(H)  # (local)
    ab = np.abs(ev)  # (local)
    return ab[ab > EVAL_CUTOFF].astype(np.float64)


# ---------------------------------------------------------------------------
# Section 6 — Gate evaluation + verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None) -> dict:
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
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main() -> int:
    t0 = time.time()  # (local)
    print("=" * 80)
    print(f"{GATE_ID} — Krylov-complexity peak on the (2,1) Peter-Weyl sector of D_K")
    print("=" * 80)

    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  tau_fold (canonical) = {float(tau_fold)} ; reference tau = 0.0 (bi-invariant)")
    print(f"  sector_pin = {SECTOR_PIN} ; beta_fold = {BETA_FOLD} (INTEG-39) ; beta_ref = {BETA_REF} (Fegan-closed)")
    print()

    # ---- (a) FOLD level set: read (2,1) sector from the s84 cache (primary input) ----
    print("--- FOLD tau=0.190: read (2,1) sector |lambda| from s84 cache ---")
    cache = np.load(S84_FOLD_CACHE, allow_pickle=True)  # (local)
    sector_evals = cache["sector_evals"].item()  # (local)
    fold_levels = np.asarray(sector_evals[SECTOR_PIN]["abs_evals"], dtype=np.float64)  # (local)
    fold_dim = int(sector_evals[SECTOR_PIN]["dim"])  # (local)
    print(f"  (2,1) sector: dim={fold_dim}, n_abs={len(fold_levels)}, "
          f"|lambda| range [{fold_levels.min():.5f}, {fold_levels.max():.5f}]")

    # ---- (b) tau=0 REFERENCE level set: FULL Fegan/Sym^p build (PRIMARY path) ----
    print("--- REFERENCE tau=0.0: build (2,1) sector |lambda| via FULL dirac_spectrum.py (Fegan/Sym^p) ---")
    t_ref = time.time()  # (local)
    ref_levels = build_sector_abs_evals(0.0, SECTOR_PIN)  # (local)
    print(f"  (2,1) sector: n_abs={len(ref_levels)}, "
          f"|lambda| range [{ref_levels.min():.5f}, {ref_levels.max():.5f}] "
          f"(built in {time.time()-t_ref:.2f}s; PRIMARY Fegan path, NO s92 fallback)")

    # Cross-check: same pipeline at tau=0.19 reproduces the cache (audit of FULL path fidelity)
    t_xc = time.time()  # (local)
    xcheck_fold = build_sector_abs_evals(float(tau_fold), SECTOR_PIN)  # (local)
    cache_sorted = np.sort(fold_levels)  # (local)
    xc_sorted = np.sort(xcheck_fold)  # (local)
    nmin = min(len(cache_sorted), len(xc_sorted))  # (local)
    fold_reproduction_maxdev = float(np.max(np.abs(cache_sorted[:nmin] - xc_sorted[:nmin]))) if nmin else float("nan")  # (local)
    print(f"  FULL-path fidelity audit: rebuilt (2,1) at tau=0.19 vs cache, "
          f"max|dev|={fold_reproduction_maxdev:.2e} (built in {time.time()-t_xc:.2f}s)")

    # ---- (c) Lanczos depth cap (pinned) ----
    n_lanczos_fold = min(len(fold_levels) - 1, N_LANCZOS_MAX_CAP)  # (local)
    n_lanczos_ref = min(len(ref_levels) - 1, N_LANCZOS_MAX_CAP)  # (local)
    n_lanczos = min(n_lanczos_fold, n_lanczos_ref)  # (local) like-for-like depth
    print(f"\n  Lanczos depth cap: fold={n_lanczos_fold}, ref={n_lanczos_ref} -> using n_lanczos={n_lanczos} (like-for-like)")

    # ---- (d) KCP for both slices ----
    print("\n--- Krylov pipeline: Delta-channel measure -> b_n -> K(t) -> KCP ---")
    fold = kcp_from_levels(fold_levels, n_lanczos)  # (local)
    ref = kcp_from_levels(ref_levels, n_lanczos)  # (local)
    KCP_fold = fold["KCP"]  # (local)
    KCP_ref = ref["KCP"]  # (local)
    print(f"  FOLD:  b1={fold['b1']:.4f}, n_b={len(fold['bn'])}, KCP={KCP_fold:.4f} at t={fold['t_peak']:.4f}")
    print(f"  REF :  b1={ref['b1']:.4f}, n_b={len(ref['bn'])}, KCP={KCP_ref:.4f} at t={ref['t_peak']:.4f}")

    # ---- (e) Saddle guard: b_n growth-law fit ----
    growth_fold = fit_bn_growth_law(fold["bn"])  # (local)
    growth_ref = fit_bn_growth_law(ref["bn"])  # (local)
    print("\n--- SADDLE GUARD: b_n growth-law fit (Bhattacharjee 2203.03534) ---")
    print(f"  FOLD b_n: slope={growth_fold['slope']:.5f}, r2={growth_fold['r2']:.4f}, "
          f"LINEAR_GROWTH={growth_fold['linear_growth']}")
    print(f"  REF  b_n: slope={growth_ref['slope']:.5f}, r2={growth_ref['r2']:.4f}, "
          f"LINEAR_GROWTH={growth_ref['linear_growth']}")
    saddle_guard_triggered = bool(growth_fold["linear_growth"] or growth_ref["linear_growth"])  # (local)
    if saddle_guard_triggered:
        print("  >> SADDLE GUARD ACTIVE: linear b_n growth detected. Read as A2-catastrophe-saddle-consistent")
        print("     (integrable-at-a-saddle), NOT a Lyapunov/chaos verdict. KCP<->beta SIGN test unaffected.")
    else:
        print("  >> b_n ladders SATURATE (no linear growth): bounded/integrable signature; no Lyapunov regime.")

    # ---- (f) R_implied: Huh monotone height ratio via Brody calibration ----
    print("\n--- R_implied: Huh KCP<->beta monotone height ratio (Brody calibration) ---")
    rng = np.random.default_rng(BRODY_CALIB_SEED)  # (local) deterministic calibration RNG
    kcp_beta_fold, sd_fold = kcp_for_beta(BETA_FOLD, BRODY_CALIB_REPS, BRODY_CALIB_N, n_lanczos, rng)  # (local)
    kcp_beta_ref, sd_ref = kcp_for_beta(BETA_REF, BRODY_CALIB_REPS, BRODY_CALIB_N, n_lanczos, rng)  # (local)
    R_implied = kcp_beta_fold / kcp_beta_ref if kcp_beta_ref > 0 else float("nan")  # (local)
    print(f"  KCP(beta={BETA_FOLD}) = {kcp_beta_fold:.4f} +/- {sd_fold:.4f}")
    print(f"  KCP(beta={BETA_REF})  = {kcp_beta_ref:.4f} +/- {sd_ref:.4f}")
    print(f"  R_implied = KCP(beta_fold)/KCP(beta_ref) = {R_implied:.4f}  (monotone-implied height ratio)")

    # ---- (g) Gate evaluation ----
    print("\n--- GATE EVALUATION ---")
    sign_kcp = int(np.sign(KCP_fold - KCP_ref))  # (local)
    sign_beta = int(np.sign(BETA_FOLD - BETA_REF))  # (local)
    sign_product = sign_kcp * sign_beta  # (local)
    kcp_ref_scaled = KCP_ref * R_implied  # (local) monotone-implied fold KCP
    rel_residual = abs(KCP_fold - kcp_ref_scaled) / abs(kcp_ref_scaled) if kcp_ref_scaled != 0 else float("inf")  # (local)
    print(f"  sign(KCP_fold - KCP_ref) = sign({KCP_fold:.4f} - {KCP_ref:.4f}) = {sign_kcp:+d}")
    print(f"  sign(beta_fold - beta_ref) = sign({BETA_FOLD} - {BETA_REF}) = {sign_beta:+d}")
    print(f"  sign_product = {sign_product:+d}  (PASS requires +1)")
    print(f"  KCP_ref * R_implied = {kcp_ref_scaled:.4f} ; rel_residual = {rel_residual:.4f} (band <= {REL_RESIDUAL_BAND})")

    # [SIGN] 3-tuple
    #   sign_verdict     = PASS iff direction matches (sign_product == +1)
    #   magnitude_verdict= PASS iff rel_residual <= band ; INFO iff band < rel_residual < inf with sign held ; FAIL otherwise
    #   regime_verdict   = VALID (the Krylov/Stieltjes method is exact on the discrete measure; no expansion regime to breach)
    sign_verdict = "PASS" if sign_product == 1 else "FAIL"  # (local)
    if sign_product != 1:
        magnitude_verdict = "FAIL"  # (local)
    elif rel_residual <= REL_RESIDUAL_BAND:
        magnitude_verdict = "PASS"  # (local)
    else:
        magnitude_verdict = "INFO"  # (local)
    regime_verdict = "VALID"  # (local) exact tridiagonal evolution on a fixed discrete measure

    # Composite collapse (pre-registered generic rule, gate-verdicts.md)
    if sign_verdict == "FAIL":
        verdict = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"  # (local)
    elif magnitude_verdict == "INFO":
        verdict = "INFO"  # (local)
    else:
        verdict = "PASS"  # (local)

    print(f"  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict} -> composite {verdict}")

    # ---- (h) Save npz ----
    np.savez(
        OUT_NPZ,
        b_n_fold=fold["bn"], b_n_ref=ref["bn"],
        K_t_fold=fold["K"], K_t_ref=ref["K"],
        t_fold=fold["t"], t_ref=ref["t"],
        KCP_fold=KCP_fold, KCP_ref=KCP_ref,
        beta_fold=BETA_FOLD, beta_ref=BETA_REF,
        R_implied=R_implied, rel_residual=rel_residual,
        sign_product=sign_product,
        bn_growth_law_fit=np.array([growth_fold["slope"], growth_fold["intercept"], growth_fold["r2"],
                                    growth_ref["slope"], growth_ref["intercept"], growth_ref["r2"]]),
        sector_pin=np.array(SECTOR_PIN),
        fold_levels=fold_levels, ref_levels=ref_levels,
        kcp_beta_fold=kcp_beta_fold, kcp_beta_ref=kcp_beta_ref,
        saddle_guard_triggered=saddle_guard_triggered,
        fold_reproduction_maxdev=fold_reproduction_maxdev,
        n_lanczos=n_lanczos,
    )
    print(f"\n  npz saved: {OUT_NPZ.name}")

    # ---- (i) Plot: b_n ladders + K(t) profiles + saddle-guard overlay ----
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    ax0 = axes[0]
    nfold = np.arange(len(fold["bn"]))  # (local)
    nref = np.arange(len(ref["bn"]))  # (local)
    ax0.plot(nfold, fold["bn"], "o-", ms=3, color="C3", label=f"fold τ=0.190 (β={BETA_FOLD})")
    ax0.plot(nref, ref["bn"], "s-", ms=3, color="C0", label=f"ref τ=0 (β={BETA_REF})")
    # saddle-guard linear-growth overlay (the law a linear b_n WOULD follow)
    if np.isfinite(growth_fold["slope"]):
        nl = np.arange(growth_fold["n_fit_lo"], growth_fold["n_fit_hi"])  # (local)
        ax0.plot(nl, growth_fold["slope"] * nl + growth_fold["intercept"], "--", color="k", lw=1.2,
                 label=f"fold linear fit (slope={growth_fold['slope']:.3f}, r²={growth_fold['r2']:.2f})")
    ax0.set_xlabel("Krylov index n")
    ax0.set_ylabel(r"$b_n$  (M_KK units)")
    sg = "SADDLE-GUARD ACTIVE" if saddle_guard_triggered else "ladders SATURATE (bounded/integrable)"
    ax0.set_title(f"Lanczos $b_n$ ladders — Δ channel, sector (2,1)\n{sg}")
    ax0.legend(fontsize=8)
    ax0.grid(True, alpha=0.3)

    ax1 = axes[1]
    ax1.plot(fold["t"], fold["K"], color="C3", lw=1.4, label=f"fold τ=0.190  KCP={KCP_fold:.3f}")
    ax1.plot(ref["t"], ref["K"], color="C0", lw=1.4, label=f"ref τ=0  KCP={KCP_ref:.3f}")
    ax1.axhline(KCP_fold, color="C3", ls=":", lw=1.0)
    ax1.axhline(KCP_ref, color="C0", ls=":", lw=1.0)
    ax1.plot(fold["t_peak"], KCP_fold, "*", color="C3", ms=14, markeredgecolor="k")
    ax1.plot(ref["t_peak"], KCP_ref, "*", color="C0", ms=14, markeredgecolor="k")
    ax1.set_xlabel(r"$t$  (M_KK$^{-1}$ units)")
    ax1.set_ylabel(r"$K(t)$  (Krylov complexity)")
    ax1.set_title(f"Krylov complexity K(t) with KCP marked\n"
                  f"sign(ΔKCP)={sign_kcp:+d}, sign(Δβ)={sign_beta:+d}, "
                  f"rel_resid={rel_residual:.3f} → {verdict}")
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3)

    plt.suptitle(f"S104-KRYLOV-KCP — fourth chaos diagnostic of the D_K (2,1) fold spectrum "
                 f"(R_implied={R_implied:.3f})", fontsize=11)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot saved: {OUT_PNG.name}")

    # ---- (j) Verdict payload ----
    value = (f"KCP_fold={KCP_fold:.4f}_KCP_ref={KCP_ref:.4f}_signprod={sign_product:+d}_"
             f"R_implied={R_implied:.4f}_rel_resid={rel_residual:.4f}_band={REL_RESIDUAL_BAND}_"
             f"beta_fold={BETA_FOLD}_beta_ref={BETA_REF}_saddle_guard={'ACTIVE' if saddle_guard_triggered else 'inactive_bn_saturate'}_"
             f"sector_2_1_tau0_ref_FULL_Fegan_primary_foldrepro_maxdev={fold_reproduction_maxdev:.1e}")  # (local)
    extra = [
        f"# saddle_guard: fold b_n slope={growth_fold['slope']:.5f} r2={growth_fold['r2']:.4f} "
        f"linear_growth={growth_fold['linear_growth']}; A2-catastrophe-saddle reading per Bhattacharjee 2203.03534, NOT Lyapunov",
        f"# tau0_reference: FULL dirac_spectrum.py Fegan/Sym^p primary path (NO s92 fallback); "
        f"FULL-path fold-reproduction max|dev| vs s84 cache = {fold_reproduction_maxdev:.2e}",
    ]
    print()
    tag = f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"  # (local)
    print(tag)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (sign={sign_verdict}/mag={magnitude_verdict}/regime={regime_verdict}) "
          f"(wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
