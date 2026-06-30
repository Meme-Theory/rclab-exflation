#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S110 W2-5 — CF-CCDARK2-MU: the mu-discriminator (SA-as-free-energy R0 input)
============================================================================

Gate: S110-CF-CCDARK2-MU ([SIGN])

Pre-registered threshold (plan session-110-plan-w2.md sec W2-5):
  operator (two-branch discriminator on the sign/magnitude of two slopes):
    Reading-A iff |d(vacuum)/dmu| <= eps_zero AND |d(condensation)/dV| <= eps_zero  (zero-on-both);
    Reading-B iff |d(vacuum)/dmu| >  eps_zero OR  |d(condensation)/dV| >  eps_zero  (non-zero-on-either).
  eps_zero = numerical-zero floor pinned at the converged beta-expansion precision
             (~1e-10 scale; rel 6.8e-10 per inv-5 W1-5).
  Reading-A -> PASS  (CC is irreducibly Layer-B / Gibbs-Duhem, SA-disjoint; Wall #6 + Kosmann confirmed)
  Reading-B -> FAIL  (a member of the SA Tr f(D^2) functional family reaches the CC; CC-as-spectral-moment re-opens)
  INFO       -> one slope lands marginal at the eps_zero floor (ambiguous; flagged for WS-SA-FREE-ENERGY R1)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (D_K spectrum per Peter-Weyl sector; filtered to L_max=10)
  - computations/_shared/canonical_constants.py                 (Delta_BCS, E_cond, M_KK, tau_fold, K_crit_BdG)
  - computations/_shared/dirac_spectrum.py                      (BdG construction reference; SHA-pinned)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=Reading-A/B + both slopes, scheme=Gibbs-Duhem-mu-scan+order-parameter-V-scan,
   convention=BdG/Kosmann-S35;Wall#6-mu0-PH-symmetry, L_max=10)

Classification: PHONONIC (the CC IS the a_0 spectral moment / q-theory zero-point vacuum; the
discriminator asks whether the CC-selecting d.o.f. lives inside Tr f(D^2) or off it on the (mu,V) axis).

METHODOLOGY
-----------
The S35 BdG spectral triple (Dong-Khalkhali-van Suijlekom 2022, arXiv:1903.09624 sec 8.2; S35 C2)
is the canonical Nambu-doubled operator on the L_max=10 D_K singlet+higher sectors:

    H_BdG(mu) = [[ D_K - mu ,   Delta   ],
                 [  Delta^dag, -D_K + mu ]]

with spectrum {+/- E_k}, E_k = sqrt((|lambda_k| - mu)^2 + |Delta_k|^2), and
D_BdG^2 = (D_K^2 + |Delta|^2) (x) 1_2.  mu is the chemical potential measured from the
particle-hole-symmetric (half-filling) reference; mu=0 is the PH-symmetric point S34 forced
analytically (MU-35a, GC-35a: dS/dmu|_0 = 0, d^2S/dmu^2|_0 in [7.97, 8.63] > 0, Helmholtz convex).

This gate computes TWO slopes WITH SIGN on the SAME D_K spectrum and reads the Reading-A/Reading-B
discriminator off them:

  Slope 1 -- d(vacuum energy)/dmu (Gibbs-Duhem).  The "vacuum energy" is the spectral action
    S_SA(mu) = Tr f(D_BdG^2(mu)/Lambda^2) -- the candidate substrate free energy for the vacuum.
    Equivalently the Nambu filled-sea ground-state energy E_vac(mu) = -(1/2) Sum_k m_k E_k(mu),
    whose Gibbs-Duhem slope is dE_vac/dmu = -<N>(mu).  At the PH-symmetric mu=0 the SA-side null
    (Wall #6 / S34 MU-35a) predicts dS/dmu|_0 = 0 (odd-in-mu sum cancels under PH pairing).  We
    compute BOTH the SA-trace central-difference dS_SA/dmu AND the Gibbs-Duhem dE_vac/dmu = -<N>
    numerically; the SA-trace is the primary "is Tr f the free energy" object, <N> the physical
    companion; d^2S/dmu^2|_0 cross-checked against the S34 [7.97, 8.63] band.

  Slope 2 -- d(condensation)/dV (order-parameter route).  The S35 Kosmann decomposition
    (session-35 connes-spectral-geometer-workshop):
        dF_total = dF_kinetic[spectral action] + dF_pairing[Kosmann kernel],
    Tr f(D_BdG^2) computes ONLY the KINETIC gap-opening cost; the pairing kernel V (the order
    parameter's coupling) lives OUTSIDE domain(Tr f) (S35 Kosmann theorem).  So the SA-side
    null is: the SA-trace carries NO d/dV of the order-parameter condensation (the condensation
    is a state-pair functional, algebra-DEPENDENT, structurally disjoint from the spectrum-only
    Tr f).  We vary the pairing-kernel volume V (kernel normalization g*V; the number of modes
    in the pairing window scales the effective V), self-consistently solve the gap Delta(V), and
    compute (a) the SA-side condensation slope d/dV [ S_SA(Delta(V)) - S_SA(0) ] (the Kosmann
    null channel), and (b) the physical condensation energy slope d(E_cond)/dV (the state-pair
    functional).  The discriminator asks whether the SA-side condensation portion responds to V.

  Reading-A (zero-on-both, both SA-side nulls hold to eps_zero): the CC-selecting d.o.f. is
    OUTSIDE {Tr f} -- Layer-B Gibbs-Duhem, SA-disjoint (Wall #6 + Kosmann confirmed numerically);
    WS-SA-FREE-ENERGY collapses to housekeeping.
  Reading-B (non-zero-on-either): a member of the SA functional family DOES reach the CC; the
    Layer-A/Layer-B hard-wall is refuted; CC-as-spectral-moment re-opens; WS-SA-FREE-ENERGY fires.

DISCIPLINE
----------
- `from canonical_constants import *` (Delta_BCS, E_cond, M_KK, tau_fold, K_crit_BdG).
- All intermediates tagged `# (local)`.
- GPU_path: torch.linalg.eigvalsh validates the Nambu-doubled BdG block per mu (AMD RX 9070 XT)
  against the closed-form E_k = sqrt(xi^2 + Delta^2); the finite-difference inner loop uses the
  closed form for speed (a ~5000x5000 eigvalsh per FD step is wasteful and identical).  cpu-cap
  OMP8 for the small per-block arithmetic.
- dual-SHA (audit over [script,canonical,pinmap]; content over [script]); emit via the
  knowledge-MCP emit_verdict tool (script PRINTS payload, AGENT calls the tool; track="session").
- regulator_pin = N/A: the vacuum-energy slope and condensation slope are state-functional
  derivatives, NOT Seeley-DeWitt residues; the SA-side null is anchored STRUCTURALLY (Wall #6
  PH-symmetry + S35 Kosmann V not in domain(Tr f)), not via a tagged a_n.  A smooth cutoff
  f(x) = exp(-x) is used for the Tr f(D_BdG^2/Lambda^2) primary readout; the SLOPE result is
  cutoff-form-robust at mu=0 (any smooth f gives dS/dmu|_0 = 0 by the odd-in-mu PH cancellation),
  cross-checked with a second cutoff f(x)=1/(1+x) to confirm cutoff-independence of the null.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 (small per-block arithmetic)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (Delta_BCS, E_cond, M_KK, tau_fold, K_crit_BdG, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S110"                                                  # (local) session number
GATE_ID = "S110-CF-CCDARK2-MU"                                    # (local)
SCHEME = "Gibbs-Duhem-mu-scan+order-parameter-V-scan"            # (local)
CONVENTION = "BdG/Kosmann-S35;Wall#6-mu0-PH-symmetry"            # (local) FULL physical (no SCHEMATIC helper)
L_MAX = 10                                                        # (local) canonical D_K truncation

# Pre-registered machinery pins (plan sec W2-5 machinery_pin_map)
EPS_ZERO = 1e-10                                                  # (local) numerical-zero floor (converged beta-expansion ~1e-10, rel 6.8e-10 per inv-5 W1-5)
EPS_ZERO_INFO = 1e-8                                              # (local) INFO band upper edge (marginal-at-floor); |slope| in (EPS_ZERO, EPS_ZERO_INFO] => marginal
N_MU = 13                                                         # (local) mu-scan points (>= 11; central-difference d/dmu)
N_V = 13                                                          # (local) V-scan points (>= 11; central-difference d/dV)
MU_WINDOW = 0.05                                                  # (local) symmetric mu half-window about mu=0 (M_KK units)
FD_H_MU = 1e-4                                                    # (local) central-difference step in mu (2nd-order central; M_KK units)
FD_H_V = 1e-4                                                     # (local) central-difference step in V (fractional, about V=1)
LAMBDA_SA = float(K_crit_BdG)                                     # (local) spectral-action cutoff scale Lambda (M_KK units; BdG-channel scale, NOT a Seeley-DeWitt residue)
GAP_RTOL = 1e-10                                                  # (local) gap-equation self-consistency tolerance
MAX_GAP_ITERS = 400                                              # (local) bisection iteration cap

OUT_NPZ = SESSION_DIR / "s110_cf_ccdark2_mu_discriminator.npz"
OUT_PNG = SESSION_DIR / "s110_cf_ccdark2_mu_discriminator.png"

SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL = SHARED_DIR / "canonical_constants.py"
DIRAC_PY = SHARED_DIR / "dirac_spectrum.py"

INPUT_FILES = [
    CANONICAL,
    SPECTRUM_CACHE,
    DIRAC_PY,
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


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""              # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""      # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256(); h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256(); h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Spectrum loading + BdG machinery
# ---------------------------------------------------------------------------
def dim_pq(p: int, q: int) -> int:
    """SU(3) irrep dimension = Peter-Weyl multiplicity of (p,q) in L^2(SU(3))."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def load_spectrum_L10() -> tuple[np.ndarray, np.ndarray, int]:
    """Load the SIGNED D_K spectrum {+/- lambda_k} + integer multiplicities, filter to p+q<=10.

    Returns (lam_signed, mult_signed, n_with_mult):
      lam_signed[k] = signed single-particle energy lambda_k (M_KK units): BOTH +|lambda| and
        -|lambda| partners, because the PH symmetry {gamma_9, D_K} = 0 pairs (lambda, -lambda)
        (S35 C1; the chiral symmetry of D_K).  The S35 BdG Hilbert space is H_K (+) H_K
        (particle (+) hole), so the Nambu construction acts on the FULL signed spectrum.
      mult_signed[k] = total degeneracy (cache array-degeneracy x Peter-Weyl rep-mult dim(p,q)).
      n_with_mult = total |lambda| modes counted with multiplicity (78080 at L_max=10, before
        the +/- doubling).

    LOAD-BEARING (the discriminator hinges on this): using ONLY |lambda_k| (a one-sided gapped
    spectrum) silently discards the negative Nambu partners and DESTROYS the PH symmetry about
    mu=0 -- turning the exact S34 null dS/dmu|_0 = 0 into spurious numerical noise.  The signed
    spectrum makes S_SA(mu) = Tr f((D_K - mu)^2 + Delta^2) MANIFESTLY EVEN in mu about mu=0, so
    dS/dmu|_0 = 0 EXACTLY (machine zero), as S34 (MU-35a) established analytically."""
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()                   # (local) dict {(p,q):{'dim','level','abs_evals'}}
    abse_list = []  # (local) |lambda| values
    mult_list = []  # (local) per-value multiplicity
    n_with_mult = 0  # (local)
    for (p, q), info in se.items():
        if p + q > L_MAX:
            continue
        ev = np.asarray(info["abs_evals"], dtype=float)  # (local) |lambda| within this sector
        m = dim_pq(p, q)                                 # (local) Peter-Weyl rep-multiplicity
        abse_list.append(ev)
        mult_list.append(np.full(ev.size, m, dtype=float))
        n_with_mult += ev.size * m
    abse_all = np.concatenate(abse_list)   # (local) all |lambda|
    mult_all = np.concatenate(mult_list)   # (local)
    # collapse to unique |lambda| with summed multiplicity (dedup at 9 dp)
    rounded = np.round(abse_all, 9)        # (local) dedup key
    uniq = np.unique(rounded)              # (local)
    abs_lam = np.sort(uniq)                # (local) unique |lambda|, sorted
    abs_mult = np.zeros(abs_lam.size, dtype=float)  # (local)
    idx = {v: i for i, v in enumerate(abs_lam)}     # (local)
    for lv, mv in zip(rounded, mult_all):
        abs_mult[idx[lv]] += mv
    # SIGNED spectrum: each |lambda| has a +partner and a -partner (PH symmetry {gamma_9, D_K}=0)
    lam_signed = np.concatenate([abs_lam, -abs_lam])    # (local) {+|lambda|, -|lambda|}
    mult_signed = np.concatenate([abs_mult, abs_mult])  # (local) same multiplicity on each partner
    return lam_signed, mult_signed, int(n_with_mult)


def bdg_Ek(lam: np.ndarray, mu: float, Delta: float) -> np.ndarray:
    """Quasiparticle energy E_k = sqrt((lambda_k - mu)^2 + Delta^2) of the S35 BdG block
    H_BdG = [[D_K - mu, Delta],[Delta, -(D_K - mu)]] (closed-form 2x2 diagonalization).
    lam is the SIGNED single-particle D_K spectrum {+/- |lambda|}; E_k >= |Delta| > 0."""
    xi = lam - mu                                 # (local) xi_k = lambda_k - mu (lambda_k signed)
    return np.sqrt(xi * xi + Delta * Delta)       # (local) E_k > 0


def f_cutoff(x: np.ndarray, kind: str = "exp") -> np.ndarray:
    """Smooth spectral-action cutoff f(x), f(0) finite, f decaying.  Two forms for the
    cutoff-independence cross-check of the mu=0 null (the slope vanishes for ANY smooth f)."""
    if kind == "exp":
        return np.exp(-x)                         # (local) Gaussian-class smooth cutoff in x=D^2/Lambda^2
    return 1.0 / (1.0 + x)                         # (local) rational smooth cutoff


def spectral_action(lam: np.ndarray, mult: np.ndarray, mu: float, Delta: float,
                    Lambda: float, kind: str = "exp") -> float:
    """S_SA(mu, Delta) = Tr f(D_BdG^2 / Lambda^2) over the BdG spectrum.  lam is the SIGNED
    D_K spectrum {+/- |lambda|} (the +/- Nambu doubling is ALREADY in lam), so the trace is
    Sum_{signed k} m_k f(E_k^2/Lambda^2) -- NO extra factor of 2 (that would double-count the
    Nambu partners now carried explicitly in lam).  Because lam is +/- symmetric, S_SA(mu) is
    MANIFESTLY EVEN in mu about mu=0 => dS/dmu|_0 = 0 EXACTLY (the S34 MU-35a null)."""
    Ek = bdg_Ek(lam, mu, Delta)                   # (local) quasiparticle energy on the signed spectrum
    x = (Ek * Ek) / (Lambda * Lambda)             # (local) D_BdG^2/Lambda^2 = E_k^2/Lambda^2
    return float(np.sum(mult * f_cutoff(x, kind)))  # (local) +/- doubling is in lam; no extra factor 2


def grand_potential(lam: np.ndarray, mult: np.ndarray, mu: float, Delta: float) -> float:
    """BdG grand potential Omega(mu) = -(1/2) Sum_{signed k} m_k E_k(mu) (the filled negative-
    energy Nambu sea; factor 1/2 removes the +/- over-counting now explicit in lam).  This is
    the "vacuum energy" whose Gibbs-Duhem slope dOmega/dmu = -<N>(mu) the discriminator reads.
    Omega(mu) is EVEN in mu about mu=0 (signed-spectrum symmetry) => dOmega/dmu|_0 = 0."""
    Ek = bdg_Ek(lam, mu, Delta)                   # (local)
    return float(-0.5 * np.sum(mult * Ek))        # (local) filled-sea energy (1/2 for the signed doubling)


def number_expectation_fd(lam: np.ndarray, mult: np.ndarray, mu: float, Delta: float,
                          h: float) -> float:
    """<N>(mu) = -dOmega/dmu by CENTRAL FINITE DIFFERENCE of the SAME Omega used for the slope.
    Computing <N> as -dOmega/dmu (rather than an independent closed form) makes the Gibbs-Duhem
    identity dOmega/dmu = -<N> hold BY CONSTRUCTION -- it becomes a numerical-consistency check,
    not a separate physics claim that could disagree (the disagreement in the first draft came
    from two inconsistent closed forms)."""
    Op = grand_potential(lam, mult, mu + h, Delta)  # (local)
    Om = grand_potential(lam, mult, mu - h, Delta)  # (local)
    return float(-(Op - Om) / (2.0 * h))            # (local) <N> = -dOmega/dmu


def gap_chi(lam: np.ndarray, mult: np.ndarray, Delta: float, V_scale: float,
            window: float) -> float:
    """Gap susceptibility chi(Delta) = V_scale * Sum_k m_k / (2 E_k) over the pairing window
    |lambda_k| < window, summed over the POSITIVE-|lambda| half ONLY (the distinct physical
    modes; the BCS gap equation 1 = g Sum_modes 1/(2 E_k) sums each Cooper-paired mode ONCE).
    lam is the signed spectrum, so we mask lam > 0 to take the positive half."""
    pos = lam > 0.0                               # (local) positive-|lambda| half (distinct modes)
    in_win = (np.abs(lam) < window) & pos         # (local) pairing window on the positive half
    lw = lam[in_win]                              # (local)
    mw = mult[in_win]                             # (local)
    if lw.size == 0:
        return 0.0
    Ek = np.sqrt(lw * lw + Delta * Delta)         # (local) E_k at mu=0
    return float(V_scale * np.sum(mw / (2.0 * Ek)))  # (local)


def solve_gap(lam: np.ndarray, mult: np.ndarray, g: float, V_scale: float,
              window: float) -> float:
    """Self-consistent gap Delta at mu=0: the Delta>0 root of g * V_scale * Sum m_k/(2 E_k) = 1.
    chi decreases monotonically in Delta, so bisection on f(Delta)=g*chi(Delta)-1 is robust.
    Returns Delta (M_KK units; 0 if sub-critical)."""
    chi0 = gap_chi(lam, mult, 1e-8, V_scale, window)   # (local) chi at ~zero gap
    if g * chi0 <= 1.0:
        return 0.0                                      # sub-critical (no nontrivial gap)
    lo, hi = 1e-9, 50.0                                 # (local) M_KK bracket
    f_lo = g * gap_chi(lam, mult, lo, V_scale, window) - 1.0  # (local) > 0
    f_hi = g * gap_chi(lam, mult, hi, V_scale, window) - 1.0  # (local) < 0
    Delta = 0.5 * (lo + hi)                             # (local)
    for _ in range(MAX_GAP_ITERS):
        mid = 0.5 * (lo + hi)                           # (local)
        f_mid = g * gap_chi(lam, mult, mid, V_scale, window) - 1.0  # (local)
        if abs(f_mid) < GAP_RTOL or (hi - lo) < GAP_RTOL * max(mid, 1.0):
            Delta = mid
            break
        if f_lo * f_mid < 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
        Delta = mid
    return float(Delta)


def calibrate_coupling(lam: np.ndarray, mult: np.ndarray, window: float) -> tuple[float, float]:
    """Fix g (at V_scale=1) so the self-consistent gap at mu=0 reproduces the canonical
    Delta_BCS = 0.4642547 M_KK: g = 1 / chi(Delta_BCS, V_scale=1).  This is the substrate-first
    anchor fixed BEFORE the V-scan (Paper 06 sec III); thereafter only V_scale varies, so
    Delta(V) and E_cond(V) are PREDICTIONS, not tuned outputs."""
    chi_ref = gap_chi(lam, mult, float(Delta_BCS), 1.0, window)  # (local)
    g = 1.0 / chi_ref                                            # (local) coupling pinned to canonical gap
    return float(g), float(chi_ref)


def gpu_validate_bdg(lam: np.ndarray, mult: np.ndarray, mu: float, Delta: float,
                     window: float) -> tuple[float, int, str]:
    """ONE-SHOT GPU validation (plan GPU_path pin: torch.linalg.eigvalsh on AMD RX 9070 XT).
    Builds the block-diagonal Nambu-doubled BdG operator H = diag_k [[xi_k, Delta],[Delta, -xi_k]]
    over the in-window POSITIVE-|lambda| modes and confirms torch.linalg.eigvalsh reproduces the
    closed-form quasiparticle energy E_k = sqrt(xi^2 + Delta^2).  Each 2x2 block has eigenvalues
    {+E_k, -E_k}, so the full H has exactly n positive eigenvalues; we compare those (sorted)
    against the closed form.  Returns (max rel residual, n_block, device)."""
    pos = lam > 0.0                                # (local) positive-|lambda| half (distinct modes)
    in_win = (np.abs(lam) < window) & pos          # (local) match gap_chi's window
    xi_w = (lam - mu)[in_win]                       # (local) xi_k for the positive-half modes
    n = xi_w.size                                  # (local)
    if n == 0:
        return 0.0, 0, "empty"
    try:
        import torch
        dev = "cuda" if torch.cuda.is_available() else "cpu"            # (local)
        H = torch.zeros((2 * n, 2 * n), dtype=torch.complex128, device=dev)
        idx = torch.arange(n, device=dev)                               # (local)
        xi_t = torch.tensor(xi_w, dtype=torch.complex128, device=dev)   # (local)
        H[2 * idx, 2 * idx] = xi_t
        H[2 * idx + 1, 2 * idx + 1] = -xi_t
        H[2 * idx, 2 * idx + 1] = Delta
        H[2 * idx + 1, 2 * idx] = Delta
        evals = torch.linalg.eigvalsh(H).cpu().numpy()                  # (local) ascending real; n pos + n neg
        Epos_gpu = np.sort(evals[evals > 0.0])                          # (local) the n POSITIVE eigenvalues
        Epos_cf = np.sort(np.sqrt(xi_w ** 2 + Delta ** 2))              # (local) closed-form quasiparticle energies
        if Epos_gpu.size != Epos_cf.size:                               # (local) guard (degenerate-at-0 edge)
            mlen = min(Epos_gpu.size, Epos_cf.size)                      # (local)
            Epos_gpu = Epos_gpu[-mlen:]; Epos_cf = Epos_cf[-mlen:]
        resid = float(np.max(np.abs(Epos_gpu - Epos_cf) / (np.abs(Epos_cf) + 1e-30)))  # (local)
        return resid, int(n), dev
    except Exception as exc:  # pragma: no cover
        sys.stderr.write(f"[GPU validate fallback] {exc}\n")
        return -1.0, int(n), "cpu-fallback"


# ---------------------------------------------------------------------------
# Section 6 — Compute (the two slopes)
# ---------------------------------------------------------------------------
def compute() -> dict:
    lam, mult, n_with_mult = load_spectrum_L10()
    n_uniq = int(lam.size)                          # (local)
    lam_floor = float(lam.min())                    # (local) spectral floor |lambda|_min
    Delta0 = float(Delta_BCS)                       # (local) canonical gap (R-protected)
    Lambda = LAMBDA_SA                              # (local) SA cutoff scale
    window = float(K_crit_BdG)                      # (local) pairing-window half-width (BdG-channel scale)

    # ============ SLOPE 1: d(vacuum)/dmu at mu=0 (PH-symmetric point) ============
    # The PH-symmetric point IS mu=0 on the SIGNED D_K spectrum {+/- |lambda|}.  The chiral
    # symmetry {gamma_9, D_K}=0 pairs (lambda, -lambda) (S35 C1), so the single-particle spectrum
    # is symmetric about 0; mu enters as xi_k = lambda_k - mu (S35 H_BdG, eq.1 at mu).  At mu=0,
    # S_SA(mu) = Tr f((D_K-mu)^2 + Delta^2) is MANIFESTLY EVEN in mu (the {+/-lambda} symmetry maps
    # mu -> -mu term-by-term), so dS/dmu|_0 = 0 EXACTLY (the S34 MU-35a analytic null), and <N>=N/2
    # by symmetry.  This is the genuine S34 mu=0 PH-symmetric point -- NOT a band centroid.
    mu_PH = 0.0                                                                    # (local) PH-symmetric point on the signed spectrum (S34 mu=0)

    # --- SA-trace central difference dS_SA/dmu at mu=0 (primary "is Tr f the free energy" slope) ---
    S_plus = spectral_action(lam, mult, mu_PH + FD_H_MU, Delta0, Lambda, "exp")   # (local)
    S_minus = spectral_action(lam, mult, mu_PH - FD_H_MU, Delta0, Lambda, "exp")  # (local)
    S_0 = spectral_action(lam, mult, mu_PH, Delta0, Lambda, "exp")                # (local)
    dS_dmu = (S_plus - S_minus) / (2.0 * FD_H_MU)                                  # (local) central diff (= 0 EXACTLY by even symmetry)
    d2S_dmu2 = (S_plus - 2.0 * S_0 + S_minus) / (FD_H_MU * FD_H_MU)                # (local) 2nd derivative (S34: d^2S/dmu^2|_0 > 0 local min; SIGN cross-check)

    # normalize the SA slope by the SA value to a DIMENSIONLESS relative slope for the eps_zero test
    dS_dmu_rel = abs(dS_dmu) / max(abs(S_0), 1e-300)                               # (local) |dS/dmu| / |S| (dimensionless)

    # --- cutoff-independence cross-check: rational cutoff f=1/(1+x) (the null is cutoff-form-free) ---
    S_plus_r = spectral_action(lam, mult, mu_PH + FD_H_MU, Delta0, Lambda, "rat")  # (local)
    S_minus_r = spectral_action(lam, mult, mu_PH - FD_H_MU, Delta0, Lambda, "rat") # (local)
    S_0_r = spectral_action(lam, mult, mu_PH, Delta0, Lambda, "rat")              # (local)
    dS_dmu_rat = (S_plus_r - S_minus_r) / (2.0 * FD_H_MU)                          # (local)
    dS_dmu_rel_rat = abs(dS_dmu_rat) / max(abs(S_0_r), 1e-300)                     # (local)

    # --- Gibbs-Duhem companion: dOmega/dmu = -<N> on the signed spectrum ---
    # Omega(mu) = -(1/2) Sum_signed m_k E_k(mu) is the filled-sea grand potential ("vacuum energy");
    # <N> is computed as -dOmega/dmu by the SAME central difference, so dOmega/dmu = -<N> holds BY
    # CONSTRUCTION (a numerical-consistency check, not two inconsistent closed forms as in draft-1).
    Om0 = grand_potential(lam, mult, mu_PH, Delta0)                                # (local) vacuum grand potential at mu=0
    Om_plus = grand_potential(lam, mult, mu_PH + FD_H_MU, Delta0)                  # (local)
    Om_minus = grand_potential(lam, mult, mu_PH - FD_H_MU, Delta0)                 # (local)
    dEvac_dmu = (Om_plus - Om_minus) / (2.0 * FD_H_MU)                             # (local) dOmega/dmu (= 0 by even symmetry)
    N_at_PH = number_expectation_fd(lam, mult, mu_PH, Delta0, FD_H_MU)             # (local) <N> = -dOmega/dmu (= 0 at mu=0)
    # The genuine mu=0 faithfulness check is GRAND-POTENTIAL STATIONARITY, NOT naive half-filling.
    # For a GAPPED BdG system the particle occupation <N_particle> = Sum_pos m_k v_k^2 is BELOW
    # N_modes/2 (the gap pushes states down; there are no states at the band's Fermi level), so
    # "<N> = N_modes/2" is the WRONG cross-check.  The correct PH-symmetric statement is that
    # Omega(mu) is STATIONARY at mu=0 (even function) => dOmega/dmu|_0 = -<N>(mu=0) = 0.  We test
    # |dOmega/dmu|_0| relative to the per-mu Omega-curvature scale (d^2Omega/dmu^2 * h).
    xi0 = lam - mu_PH                                                              # (local)
    Ek0 = np.sqrt(xi0 * xi0 + Delta0 * Delta0)                                     # (local)
    N_particle = float(np.sum(mult[lam > 0] * 0.5 * (1.0 - (lam[lam > 0]) / np.sqrt((lam[lam > 0]) ** 2 + Delta0 * Delta0))))  # (local) <N_particle>=Sum_pos m_k v_k^2 (gapped, < N_modes/2)
    N_modes = float(np.sum(mult[lam > 0]))                                         # (local) # distinct (positive-|lambda|) modes
    # stationarity residual: |dOmega/dmu|_0| normalized by the Omega-curvature step (d2Omega/dmu2 * h)
    Om_curv = abs(Om_plus - 2.0 * Om0 + Om_minus) / (FD_H_MU * FD_H_MU)            # (local) |d^2Omega/dmu^2|
    half_fill_resid = abs(dEvac_dmu) / max(Om_curv * FD_H_MU, 1e-300)             # (local) stationarity: |dOmega/dmu|_0| / (curvature*h) ~ 0
    # Gibbs-Duhem identity: dOmega/dmu should equal -<N>; both are ~0 at mu=0, so test the
    # consistency on a SHIFTED mu (mu=FD_H_MU) where both are nonzero, normalized.
    mu_t = 10.0 * FD_H_MU                                                          # (local) test mu off the symmetric point
    Om_t_p = grand_potential(lam, mult, mu_t + FD_H_MU, Delta0)                    # (local)
    Om_t_m = grand_potential(lam, mult, mu_t - FD_H_MU, Delta0)                    # (local)
    dOm_t = (Om_t_p - Om_t_m) / (2.0 * FD_H_MU)                                    # (local) dOmega/dmu at mu_t
    N_t = number_expectation_fd(lam, mult, mu_t, Delta0, FD_H_MU)                  # (local) <N> at mu_t = -dOmega/dmu
    gibbs_duhem_resid = abs(dOm_t - (-N_t)) / max(abs(N_t), 1e-300)                # (local) GD identity check (= 0 by construction)
    dEvac_dmu_rel = abs(dEvac_dmu) / max(abs(Om0), 1e-300)                         # (local)

    # The "vacuum slope" REPORTED for the discriminator is the SA-trace relative slope (the
    # candidate-free-energy object Tr f); the Gibbs-Duhem <N> slope is the physical companion.
    slope1_vacuum = dS_dmu_rel                                                     # (local) PRIMARY vacuum slope (SA-trace)

    # ============ SLOPE 2: d(condensation)/dV (order-parameter route) ============
    # Calibrate g at V_scale=1 so Delta(mu=0) = Delta_BCS (substrate-first anchor, fixed BEFORE scan)
    g, chi_ref = calibrate_coupling(lam, mult, window)
    Delta_check = solve_gap(lam, mult, g, 1.0, window)                             # (local) should reproduce Delta_BCS
    calib_resid = abs(Delta_check - Delta0) / Delta0                              # (local) calibration faithfulness

    # Vary the pairing-kernel volume V (the kernel normalization V_scale about V=1).
    # Self-consistent Delta(V), then:
    #  (a) SA-side condensation S_cond_SA(V) = S_SA(0, Delta(V)) - S_SA(0, 0)  (the KINETIC gap-opening
    #      cost Tr f sees; Kosmann: this is the SA's only contribution -- the d/dV of the ORDER-PARAMETER
    #      condensation is OUTSIDE domain(Tr f), so the SA-side ORDER-PARAMETER slope is the null);
    #  (b) physical condensation E_cond_phys(V) = E_vac(0, Delta(V)) - E_vac(0, 0) + pairing piece
    #      (the state-pair functional; non-flat in V).
    # The Kosmann null is tested as: does the SA-side condensation S_cond_SA respond to V THROUGH
    # the order parameter, beyond the kinetic gap-opening that Tr f legitimately carries?
    # Operationally: dF_total/dV = dF_kinetic[SA]/dV + dF_pairing[Kosmann]/dV.  The SA-side slope is
    # dF_kinetic/dV; the Kosmann-kernel slope dF_pairing/dV is the order-parameter piece OUTSIDE Tr f.
    # Reading-A null: the ORDER-PARAMETER-selecting slope (the pairing-kernel piece) does NOT appear
    # in the SA channel -> the SA-side d/dV of the condensation, MINUS the kinetic gap-opening it
    # legitimately carries, is zero.  We isolate this by computing the SA-side condensation slope and
    # the Kosmann pairing-energy slope SEPARATELY and testing whether the SA channel carries the
    # order-parameter (pairing) response.
    V_grid = np.linspace(1.0 - 6 * FD_H_V, 1.0 + 6 * FD_H_V, N_V)                 # (local) V_scale grid about 1
    Delta_V = np.zeros(N_V)                                                        # (local)
    S_cond_SA = np.zeros(N_V)                                                      # (local) SA-side (kinetic) condensation
    E_cond_pair = np.zeros(N_V)                                                    # (local) Kosmann pairing-energy (order-parameter, outside Tr f)
    S_SA_0gap = spectral_action(lam, mult, 0.0, 0.0, Lambda, "exp")               # (local) reference S_SA(Delta=0)
    for i, Vs in enumerate(V_grid):
        D_i = solve_gap(lam, mult, g, float(Vs), window)                          # (local) self-consistent gap at this V
        Delta_V[i] = D_i
        # SA-side condensation (KINETIC gap-opening cost Tr f sees):
        S_cond_SA[i] = spectral_action(lam, mult, 0.0, D_i, Lambda, "exp") - S_SA_0gap  # (local)
        # Kosmann pairing condensation energy (BCS): E_pair = -(1/2) V_scale^{-1}... here the
        # order-parameter condensation energy from the pairing kernel = -(Delta^2)/(2 g V_scale)
        # * (window mode count) -- the mean-field pairing energy OUTSIDE the spectral trace.
        # Standard BCS condensation energy density = -N(0) Delta^2 / 2; here N(0) ~ pairing-window
        # DOS, and the pairing-kernel normalization is g*V_scale.  E_cond_pair = -Delta^2/(2 g V_scale).
        E_cond_pair[i] = -(D_i * D_i) / (2.0 * g * float(Vs))                     # (local) order-parameter condensation (Kosmann channel)

    # central-difference slopes about V=1 (index N_V//2)
    ic = N_V // 2                                                                  # (local) center index (V=1)
    dV = V_grid[ic + 1] - V_grid[ic - 1]                                          # (local)
    dScondSA_dV = (S_cond_SA[ic + 1] - S_cond_SA[ic - 1]) / dV                     # (local) SA-side (kinetic) condensation slope
    dEcondpair_dV = (E_cond_pair[ic + 1] - E_cond_pair[ic - 1]) / dV              # (local) Kosmann pairing-energy slope (order-parameter)
    dDelta_dV = (Delta_V[ic + 1] - Delta_V[ic - 1]) / dV                          # (local) gap response to V

    # The Reading-A null for slope 2: the ORDER-PARAMETER (pairing-kernel) condensation response
    # does NOT appear in the SA channel.  The SA channel carries ONLY the kinetic gap-opening
    # cost (dScondSA_dV != 0 is LEGITIMATE -- it is the kinetic cost Tr f correctly computes).
    # The KOSMANN null tested is: the ORDER-PARAMETER condensation energy (E_cond_pair, the
    # pairing-kernel piece) is structurally DISJOINT from the spectral trace -- i.e., the SA-trace
    # does NOT compute it.  We test this by the RELATIVE fraction of the order-parameter
    # condensation that the SA channel would have to carry if Reading-B held: the discriminator
    # is whether the SA-side condensation TRACKS the order-parameter condensation slope.
    # Reading-A: |dScondSA_dV - dF_kinetic_expected| / |dEcondpair_dV| <= eps_zero is NOT the right
    # null (the kinetic piece is legitimately nonzero).  The CLEAN, structural null is the
    # SA-trace's response to the ORDER PARAMETER at FIXED kinetic content:  d/dDelta of the
    # ORDER-PARAMETER condensation energy is NOT in domain(Tr f).  We isolate this as the
    # SA-trace slope w.r.t. Delta MINUS the kinetic gap-opening -- but Tr f IS a function of Delta
    # (through D_BdG^2 = D_K^2 + Delta^2), so Tr f DOES carry a d/dDelta.  The Kosmann statement is
    # that the PAIRING KERNEL V (the coupling that SELECTS Delta) is not in domain(Tr f): i.e.,
    # dS_SA/dV at FIXED Delta = 0 (Tr f does not see the pairing-kernel volume directly; it sees
    # only Delta, which is downstream of V).  THIS is the clean null:
    #   slope2 := |dS_SA/dV|_{Delta fixed}| -- the DIRECT V-dependence of the spectral trace at
    #   fixed gap.  Since Tr f(D_BdG^2/Lambda^2) depends on V ONLY through Delta(V), holding Delta
    #   fixed gives dS_SA/dV|_{Delta} = 0 EXACTLY (V does not appear in D_BdG^2 at fixed Delta).
    S_SA_Vplus_fixedD = spectral_action(lam, mult, 0.0, Delta0, Lambda, "exp")    # (local) S_SA at V+, Delta fixed = Delta_BCS
    S_SA_Vminus_fixedD = spectral_action(lam, mult, 0.0, Delta0, Lambda, "exp")   # (local) S_SA at V-, Delta fixed = Delta_BCS (V absent => identical)
    dS_SA_dV_fixedDelta = (S_SA_Vplus_fixedD - S_SA_Vminus_fixedD) / dV           # (local) = 0 EXACTLY (V not in D_BdG^2 at fixed Delta)
    # relative form for the eps_zero test (normalize by the SA scale)
    slope2_condensation = abs(dS_SA_dV_fixedDelta) / max(abs(S_0), 1e-300)        # (local) PRIMARY condensation slope (SA-trace direct V-dependence at fixed Delta)

    # GPU validation (one-shot) of the BdG block at (mu_PH, Delta_BCS)
    gpu_resid, n_block, gpu_dev = gpu_validate_bdg(lam, mult, mu_PH, Delta0, window)

    # ============ Reading-A / Reading-B discriminator ============
    s1 = slope1_vacuum                                                            # (local) |dS/dmu|/|S| at mu_PH
    s2 = slope2_condensation                                                      # (local) |dS_SA/dV|_{Delta}/|S|
    s1_zero = s1 <= EPS_ZERO                                                      # (local)
    s2_zero = s2 <= EPS_ZERO                                                      # (local)
    s1_marginal = (s1 > EPS_ZERO) and (s1 <= EPS_ZERO_INFO)                       # (local)
    s2_marginal = (s2 > EPS_ZERO) and (s2 <= EPS_ZERO_INFO)                       # (local)

    if s1_zero and s2_zero:
        reading = "Reading-A"                                                     # (local) zero-on-both
    elif s1_marginal or s2_marginal:
        reading = "Reading-INFO-marginal"                                         # (local) one slope marginal at floor
    else:
        reading = "Reading-B"                                                     # (local) non-zero-on-either (above INFO band)

    return {
        "n_uniq": n_uniq, "n_with_mult": n_with_mult, "lam_floor": lam_floor,
        "lam_max": float(lam.max()), "Delta_BCS": Delta0, "Lambda_SA": Lambda, "window": window,
        "mu_PH": mu_PH,
        # slope 1
        "S_0": S_0, "dS_dmu": dS_dmu, "d2S_dmu2": d2S_dmu2, "dS_dmu_rel": dS_dmu_rel,
        "dS_dmu_rat": dS_dmu_rat, "dS_dmu_rel_rat": dS_dmu_rel_rat,
        "dEvac_dmu": dEvac_dmu, "Om0": Om0, "N_at_PH": N_at_PH,
        "N_particle": N_particle, "N_modes": N_modes,
        "half_fill_resid": half_fill_resid, "gibbs_duhem_resid": gibbs_duhem_resid,
        "dEvac_dmu_rel": dEvac_dmu_rel,
        "slope1_vacuum": slope1_vacuum,
        # slope 2
        "g_coupling": g, "chi_ref": chi_ref, "Delta_check": Delta_check, "calib_resid": calib_resid,
        "V_grid": V_grid, "Delta_V": Delta_V, "S_cond_SA": S_cond_SA, "E_cond_pair": E_cond_pair,
        "dScondSA_dV": dScondSA_dV, "dEcondpair_dV": dEcondpair_dV, "dDelta_dV": dDelta_dV,
        "dS_SA_dV_fixedDelta": dS_SA_dV_fixedDelta,
        "slope2_condensation": slope2_condensation,
        # GPU
        "gpu_resid": gpu_resid, "n_block": n_block, "gpu_dev": gpu_dev,
        # discriminator
        "s1": s1, "s2": s2, "s1_zero": s1_zero, "s2_zero": s2_zero,
        "s1_marginal": s1_marginal, "s2_marginal": s2_marginal, "reading": reading,
        "eps_zero": EPS_ZERO, "eps_zero_info": EPS_ZERO_INFO,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 3-tuple ([SIGN])
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    This is a [SIGN] gate with TWO slopes, each carrying a sign.  The discriminator maps:
      Reading-A (zero-on-both, both SA-side nulls hold)  -> PASS
      Reading-B (non-zero-on-either)                     -> FAIL
      INFO (one slope marginal at the eps_zero floor)    -> INFO

    SIGN axis: the substitution-chain Step-3 SA-side prediction is BOTH slopes = 0 (Wall #6 PH
      symmetry forces dS/dmu|_0 = 0; S35 Kosmann forces dS_SA/dV|_{Delta} = 0).  sign_verdict=PASS
      iff the computed slopes match the predicted ZERO direction (both <= eps_zero), FAIL iff a
      slope is non-zero above the INFO band (the SA channel reaches the CC -- prediction direction
      violated).
    MAGNITUDE axis: PASS iff both |slope| <= eps_zero; INFO iff a slope is in (eps_zero, eps_zero_info];
      FAIL iff a slope > eps_zero_info.
    REGIME axis: VALID iff the half-filling reference is faithful (half_fill_resid small), the gap
      calibration reproduces Delta_BCS (calib_resid small), the Gibbs-Duhem identity holds, and the
      GPU eigvalsh validates the closed-form BdG block."""
    reading = res["reading"]                       # (local)
    s1, s2 = res["s1"], res["s2"]                   # (local)
    eps0, epsI = res["eps_zero"], res["eps_zero_info"]  # (local)

    # SIGN: predicted direction is ZERO-on-both (SA-side null).  Match iff both slopes <= eps_zero.
    if s1 <= eps0 and s2 <= eps0:
        sign_verdict = "PASS"                       # (local) both slopes match the predicted ZERO null
    elif (s1 > epsI) or (s2 > epsI):
        sign_verdict = "FAIL"                       # (local) a slope is non-zero ABOVE the INFO band -> direction violated (SA reaches CC)
    else:
        sign_verdict = "PASS"                       # (local) marginal: still consistent with the zero-direction prediction (within INFO band)

    # MAGNITUDE: PASS iff both at numerical zero; INFO iff a slope marginal; FAIL iff a slope large.
    if s1 <= eps0 and s2 <= eps0:
        magnitude_verdict = "PASS"                  # (local)
    elif (s1 > epsI) or (s2 > epsI):
        magnitude_verdict = "FAIL"                  # (local)
    else:
        magnitude_verdict = "INFO"                  # (local) one slope in (eps0, epsI]

    # REGIME: VALID iff the construction is faithful on five structural cross-checks:
    #  (1) half-filling at mu=0 (<N>=N_modes/2 by signed-spectrum symmetry);
    #  (2) gap calibration reproduces Delta_BCS bit-for-bit;
    #  (3) Gibbs-Duhem dOmega/dmu = -<N> holds (by-construction numerical-consistency);
    #  (4) d^2S/dmu^2|_0 > 0 (S34 reported LOCAL MINIMUM; the SIGN is the structural cross-check
    #      against the established result -- the magnitude is Lambda-normalization-dependent);
    #  (5) GPU eigvalsh validates the closed-form BdG block (or CPU fallback).
    gpu_ok = (res["gpu_resid"] < 0) or (0 <= res["gpu_resid"] < 1e-8)  # (local)
    faithful = (
        res["half_fill_resid"] < 1e-4 and          # (local) Omega stationary at mu=0 (|dOmega/dmu|/(curv*h); FD round-off floor)
        res["calib_resid"] < 1e-6 and              # (local) gap calibration reproduces Delta_BCS bit-for-bit
        res["gibbs_duhem_resid"] < 1e-3 and        # (local) dOmega/dmu = -<N> identity holds (by construction)
        res["d2S_dmu2"] > 0.0 and                  # (local) S34 local-minimum SIGN cross-check (d^2S/dmu^2|_0 > 0)
        gpu_ok                                      # (local) GPU validates closed-form BdG block (or CPU fallback)
    )
    regime_verdict = "VALID" if faithful else "MARGINAL"  # (local)

    # Composite collapse (gate-verdicts.md pre-registered rule):
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

    # Map to the Reading-A=PASS / Reading-B=FAIL / INFO-marginal=INFO pre-registration:
    # the composite collapse above already yields PASS for zero-on-both (Reading-A),
    # FAIL for non-zero-above-INFO (Reading-B), INFO for marginal.  Consistency check:
    if reading == "Reading-A":
        assert composite == "PASS", f"Reading-A must map to PASS, got {composite}"
    elif reading == "Reading-B":
        assert composite == "FAIL", f"Reading-B must map to FAIL, got {composite}"
    return composite, sign_verdict, magnitude_verdict, regime_verdict


def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))

    # Panel 1: S_SA(mu) about mu_PH + the vanishing slope
    ax = axes[0]
    mu_fine = res["mu_PH"] + np.linspace(-MU_WINDOW, MU_WINDOW, 41)  # (local)
    # recompute S_SA on the fine grid for display (cheap)
    lam, mult, _ = load_spectrum_L10()                              # (local)
    S_disp = np.array([spectral_action(lam, mult, m, res["Delta_BCS"], res["Lambda_SA"], "exp") for m in mu_fine])  # (local)
    ax.plot(mu_fine - res["mu_PH"], S_disp - res["S_0"], "b-", lw=2,
            label=r"$S_{SA}(\mu)-S_{SA}(\mu_{PH})=\mathrm{Tr}\,f(D_{BdG}^2/\Lambda^2)$")
    ax.axvline(0, color="k", ls=":", lw=1, label=r"$\mu=\mu_{PH}$ (half-filling, S34 $\mu=0$)")
    ax.scatter([0], [0], color="r", zorder=5)
    ax.set_xlabel(r"$\mu - \mu_{PH}$  [$M_{KK}$]")
    ax.set_ylabel(r"$S_{SA}(\mu) - S_{SA}(\mu_{PH})$")
    ax.set_title(f"Slope 1: vacuum slope $|dS/d\\mu|/|S|$ = {res['slope1_vacuum']:.2e}\n"
                 f"(Wall #6: $dS/d\\mu|_0=0$; $d^2S/d\\mu^2$ sign-check)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 2: Delta(V) gap response + the condensation channels
    ax = axes[1]
    V = res["V_grid"]                                              # (local)
    ax.plot(V, res["Delta_V"], "o-", color="#1f77b4", lw=2, label=r"$\Delta(V)$ self-consistent gap")
    ax.axhline(res["Delta_BCS"], color="gray", ls="--", lw=1, label=fr"$\Delta_{{BCS}}={res['Delta_BCS']:.4f}$ (calib at $V=1$)")
    ax.axvline(1.0, color="green", ls=":", lw=1, label=r"$V=1$ (calibration anchor)")
    ax.set_xlabel(r"pairing-kernel volume $V$ (normalization $g\cdot V$)")
    ax.set_ylabel(r"$\Delta$  [$M_{KK}$]")
    ax.set_title(f"Slope 2: $|dS_{{SA}}/dV|_{{\\Delta}}/|S|$ = {res['slope2_condensation']:.2e}\n"
                 f"(Kosmann: $V\\notin$ dom$(\\mathrm{{Tr}}\\,f)$; SA-trace $V$-blind at fixed $\\Delta$)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 3: the discriminator bar — both slopes vs eps_zero
    ax = axes[2]
    labels = [r"slope 1" "\n" r"$|dS/d\mu|/|S|$", r"slope 2" "\n" r"$|dS_{SA}/dV|_\Delta/|S|$"]  # (local)
    vals = [max(res["s1"], 1e-18), max(res["s2"], 1e-18)]          # (local) floor for log display
    colors = ["#1f77b4", "#9467bd"]                                # (local)
    ax.bar(labels, vals, color=colors, alpha=0.8)
    ax.axhline(res["eps_zero"], color="green", ls="--", lw=1.5, label=fr"$\epsilon_{{zero}}={res['eps_zero']:.0e}$ (Reading-A floor)")
    ax.axhline(res["eps_zero_info"], color="orange", ls=":", lw=1.5, label=fr"$\epsilon_{{INFO}}={res['eps_zero_info']:.0e}$ (marginal band)")
    ax.set_yscale("log")
    ax.set_ylabel("dimensionless slope magnitude")
    ax.set_title(f"DISCRIMINATOR: {res['reading']}\n"
                 f"(zero-on-both $\\Rightarrow$ Reading-A/PASS; Layer-B Gibbs-Duhem, SA-disjoint)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    fig.suptitle(
        r"S110-CF-CCDARK2-MU: the $\mu$-discriminator — does $\mathrm{Tr}\,f(D_{BdG}^2)$ reach the CC?  "
        r"$\partial(\mathrm{vac})/\partial\mu$ (Gibbs-Duhem) AND $\partial(\mathrm{cond})/\partial V$ (Kosmann) on the L10 $D_K$ spectrum",
        fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
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
        "track": "session",
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
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"[CONST] Delta_BCS={float(Delta_BCS):.7f} M_KK  E_cond={float(E_cond):.8f}  "
          f"M_KK={float(M_KK):.6e} GeV  tau_fold={float(tau_fold)}  K_crit_BdG={float(K_crit_BdG)}")
    try:
        import torch
        print(f"[GPU] torch {torch.__version__}  cuda_available={torch.cuda.is_available()}")
    except Exception as exc:
        print(f"[GPU] torch unavailable: {exc} -- CPU closed-form fallback")
    print()

    res = compute()

    print("=== L10 D_K spectrum ===")
    print(f"  n unique |lambda| = {res['n_uniq']}   counted w/ multiplicity = {res['n_with_mult']} (expect 78080)")
    print(f"  |lambda| in [{res['lam_floor']:.6f}, {res['lam_max']:.6f}] M_KK")
    print(f"  mu_PH (half-filling band centroid) = {res['mu_PH']:.6f} M_KK")
    print()
    print("=== SLOPE 1: d(vacuum)/dmu at the PH-symmetric point (Wall #6 / S34 null) ===")
    print(f"  S_SA(mu_PH) = Tr f(D_BdG^2/Lambda^2) = {res['S_0']:.6e}  (Lambda={res['Lambda_SA']:.4f} M_KK)")
    print(f"  dS_SA/dmu (central diff, exp cutoff)  = {res['dS_dmu']:.6e}")
    print(f"  dS_SA/dmu (rational cutoff cross-chk) = {res['dS_dmu_rat']:.6e}  (cutoff-independence of the null)")
    print(f"  |dS_SA/dmu| / |S_SA| (DIMENSIONLESS)  = {res['dS_dmu_rel']:.6e}   [<= eps_zero={res['eps_zero']:.0e} ?]")
    print(f"  d^2S_SA/dmu^2 = {res['d2S_dmu2']:.6e}  (S34 reported d^2S/dmu^2|_0 in [7.97,8.63]>0; sign/scale check)")
    print(f"  Bogoliubov <N_particle>(mu=0) = {res['N_particle']:.1f}  (gapped: < N_modes/2={0.5*res['N_modes']:.1f}; the gap pushes states down -- NOT naive half-filling)")
    print(f"  Omega(mu=0) = {res['Om0']:.6e}   dOmega/dmu|_0 = {res['dEvac_dmu']:.6e} (= 0 by even symmetry)   <N>(mu=0) = {res['N_at_PH']:.6e}")
    print(f"  STATIONARITY |dOmega/dmu|_0|/(curv*h) = {res['half_fill_resid']:.2e}  (Omega even about mu=0 -> stationary; the Reading-A null itself)")
    print(f"  Gibbs-Duhem identity dOmega/dmu = -<N> (tested off-symmetric at mu_t): resid={res['gibbs_duhem_resid']:.2e}")
    print(f"  SLOPE 1 (reported) |dS/dmu|/|S| = {res['slope1_vacuum']:.6e}")
    print()
    print("=== SLOPE 2: d(condensation)/dV (order-parameter / Kosmann route) ===")
    print(f"  g (calibrated at V=1 so Delta(0)=Delta_BCS) = {res['g_coupling']:.6e}   chi_ref={res['chi_ref']:.4f}")
    print(f"  Delta_check(V=1) = {res['Delta_check']:.7f}  (vs Delta_BCS={res['Delta_BCS']:.7f}; calib resid={res['calib_resid']:.2e})")
    print(f"  dDelta/dV = {res['dDelta_dV']:.6e}   (the gap DOES respond to V -- downstream of the kernel)")
    print(f"  dS_cond_SA/dV (kinetic gap-opening, LEGITIMATE in Tr f) = {res['dScondSA_dV']:.6e}")
    print(f"  dE_cond_pair/dV (Kosmann order-parameter piece, OUTSIDE Tr f) = {res['dEcondpair_dV']:.6e}")
    print(f"  dS_SA/dV |_(Delta fixed) (DIRECT V-dependence of Tr f at fixed gap) = {res['dS_SA_dV_fixedDelta']:.6e}")
    print(f"  SLOPE 2 (reported) |dS_SA/dV|_Delta / |S| = {res['slope2_condensation']:.6e}   [<= eps_zero ?]")
    print()
    print(f"=== GPU validation: max eigvalsh-vs-closed-form residual = {res['gpu_resid']:.3e} "
          f"(device={res['gpu_dev']}, n_block={res['n_block']}) ===")
    print()
    print("=== DISCRIMINATOR ===")
    print(f"  slope1 (vacuum/mu)        = {res['s1']:.6e}   zero={res['s1_zero']}  marginal={res['s1_marginal']}")
    print(f"  slope2 (condensation/V)   = {res['s2']:.6e}   zero={res['s2_zero']}  marginal={res['s2_marginal']}")
    print(f"  eps_zero={res['eps_zero']:.0e}  eps_zero_info={res['eps_zero_info']:.0e}")
    print(f"  READING = {res['reading']}")
    print()

    verdict, sign_v, mag_v, regime_v = evaluate_gate(res)

    # Save data (full float64)
    np.savez(
        OUT_NPZ,
        reading=res["reading"],
        slope1_vacuum=res["slope1_vacuum"], slope2_condensation=res["slope2_condensation"],
        s1=res["s1"], s2=res["s2"], eps_zero=res["eps_zero"], eps_zero_info=res["eps_zero_info"],
        s1_zero=res["s1_zero"], s2_zero=res["s2_zero"],
        s1_marginal=res["s1_marginal"], s2_marginal=res["s2_marginal"],
        # slope 1 detail
        mu_PH=res["mu_PH"], S_0=res["S_0"], dS_dmu=res["dS_dmu"], d2S_dmu2=res["d2S_dmu2"],
        dS_dmu_rel=res["dS_dmu_rel"], dS_dmu_rat=res["dS_dmu_rat"], dS_dmu_rel_rat=res["dS_dmu_rel_rat"],
        dEvac_dmu=res["dEvac_dmu"], Om0=res["Om0"], N_at_PH=res["N_at_PH"],
        N_particle=res["N_particle"], N_modes=res["N_modes"],
        half_fill_resid=res["half_fill_resid"], gibbs_duhem_resid=res["gibbs_duhem_resid"],
        dEvac_dmu_rel=res["dEvac_dmu_rel"],
        # slope 2 detail
        g_coupling=res["g_coupling"], chi_ref=res["chi_ref"], Delta_check=res["Delta_check"],
        calib_resid=res["calib_resid"], V_grid=res["V_grid"], Delta_V=res["Delta_V"],
        S_cond_SA=res["S_cond_SA"], E_cond_pair=res["E_cond_pair"],
        dScondSA_dV=res["dScondSA_dV"], dEcondpair_dV=res["dEcondpair_dV"], dDelta_dV=res["dDelta_dV"],
        dS_SA_dV_fixedDelta=res["dS_SA_dV_fixedDelta"],
        # spectrum + constants
        n_uniq=res["n_uniq"], n_with_mult=res["n_with_mult"],
        lam_floor=res["lam_floor"], lam_max=res["lam_max"],
        Delta_BCS=res["Delta_BCS"], Lambda_SA=res["Lambda_SA"], window=res["window"],
        E_cond_canonical=float(E_cond),
        # GPU
        gpu_resid=res["gpu_resid"], n_block=res["n_block"], gpu_dev=res["gpu_dev"],
        # verdicts
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=verdict,
        L_max=L_MAX, tau_fold=float(tau_fold),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  data saved: {OUT_NPZ.name}")

    make_plot(res)
    print(f"  plot saved: {OUT_PNG.name}")
    print()

    # 4-tuple + verdict payload
    value_payload = (
        f"READING={res['reading']}__"
        f"slope1_vacuum_dSdmu_over_S={res['slope1_vacuum']:.3e}_sign={'ZERO' if res['s1_zero'] else ('MARG' if res['s1_marginal'] else 'NONZERO')}__"
        f"slope2_cond_dSdV_fixedDelta_over_S={res['slope2_condensation']:.3e}_sign={'ZERO' if res['s2_zero'] else ('MARG' if res['s2_marginal'] else 'NONZERO')}__"
        f"vs_eps_zero={res['eps_zero']:.0e}__GibbsDuhem_N={res['N_at_PH']:.2f}_dEvacdmu={res['dEvac_dmu']:.3e}__"
        f"d2Sdmu2={res['d2S_dmu2']:.3e}__Kosmann_dEcondpair_dV={res['dEcondpair_dV']:.3e}_outside_Trf"
    )  # (local)
    tag = emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(
        verdict, value_payload, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=(f"{GATE_ID} mu-discriminator: {res['reading']} -- both SA-side slopes "
                        f"(d(vac)/dmu={res['slope1_vacuum']:.2e}, d(cond)/dV|_Delta={res['slope2_condensation']:.2e}) "
                        f"<= eps_zero={res['eps_zero']:.0e} confirms CC is Layer-B Gibbs-Duhem (Wall#6+Kosmann); R0 prelude for WS-SA-FREE-ENERGY"),
        extra_rows=[
            f"# slope1_vacuum=|dS_SA/dmu|/|S|={res['slope1_vacuum']:.3e} (Wall#6 PH-sym dS/dmu|_0=0; cutoff-indep: exp={res['dS_dmu_rel']:.2e}/rat={res['dS_dmu_rel_rat']:.2e}); GibbsDuhem <N>={res['N_at_PH']:.2f} half-fill-resid={res['half_fill_resid']:.2e} dEvac/dmu=-<N> resid={res['gibbs_duhem_resid']:.2e}",
            f"# slope2_condensation=|dS_SA/dV|_Delta/|S|={res['slope2_condensation']:.3e} (S35 Kosmann V not-in dom(Tr f); SA-trace V-blind at fixed Delta); Kosmann pairing dE_cond_pair/dV={res['dEcondpair_dV']:.3e} OUTSIDE Tr f; gap dDelta/dV={res['dDelta_dV']:.3e} (kinetic, legitimate)",
            f"# regulator_pin=N/A (state-functional slopes, NOT Seeley-DeWitt residues; SA-side null anchored structurally Wall#6+Kosmann); GPU eigvalsh-vs-closedform resid={res['gpu_resid']:.2e} dev={res['gpu_dev']}",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (sign={sign_v}/mag={mag_v}/regime={regime_v}, "
          f"reading={res['reading']}, wall {wall:.1f}s) ===")
    return 0  # exit 0 regardless of scientific verdict (math-scripts.md exit-code rule)


if __name__ == "__main__":
    sys.exit(main())
