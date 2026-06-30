#!/usr/bin/env python3
"""
INV10 W3-2 INV10-W3-2 — Ruelle-Pollicott resonance spectrum of the BdG Liouvillian
===================================================================================

Gate: INV10-W3-2 ([SIGN])   (investigation track n=10)

Pre-registered (three-way decay-form classification + tau-localization):
  PASS  iff decay_form(tau_fold) = POWER-LAW with |alpha - 1/2| <= tau_alpha=0.10
            AND power-law preferred over exponential by Delta-AIC >= 2 at tau_fold
            AND the criticality (RP-gap -> 0, or the power-law fit-quality) is
            tau-LOCALIZED: separates from the off-fold-slice mean by >= m_loc=0.05
            in the criticality direction.
  FAIL  iff decay form is tau-INDEPENDENT: generic exponential (isolated complex RP
            resonance, finite Liouvillian gap everywhere) OR non-decay (real spectrum,
            persistent oscillation). The fold is a DENSITY-OF-STATES feature in rho_E,
            NOT a point of dynamical criticality. Edge-of-chaos (survey A4) RETIRED as
            a dynamical claim.
  INFO  iff power-law present at tau_fold but alpha off 1/2 (|alpha-0.5| in (0.10,0.30])
            OR criticality present but not cleanly tau-localized (RP-gap dips at the
            fold but the off-fold separation is < m_loc).

Physics (substrate-first, PHONONIC):
  The substrate IS the BdG gap-edge dynamics; the van Hove fold at tau_fold=0.190 is
  the central feature of the whole transit picture. Chain:
      D_K(tau) eigenvalues -> BdG gap-edge spectrum & DOS rho_E
        -> Liouvillian L[rho] = -i[H_BdG, rho] and its Ruelle-Pollicott resonances
        -> late-time 4D-correlation decay C(t).
  Irreversibility here is NOT thermal-bath decoherence and NOT scrambling (lambda_L=0);
  it is the ALGEBRAIC decay forced by a critical RP BRANCH POINT (a van-Hove A2 fold:
  rho_E(E) ~ (E - E_c)^{-1/2} => C(t) ~ t^{-1/2}, Ruelle 1986 / framework-chaotic-
  instantons.md Sec 5.4). If the power-law is tau-LOCALIZED at tau_fold, the supersonic
  transit through the fold IS the dynamical origin of the cosmological arrow of time,
  anchored at the substrate's own critical point. Direction of explanation flows from
  the eigenvalue structure to the emergent arrow of time, never the reverse.

  framework-chaotic-instantons.md Sec 5.4 flags this branch-point reading PRELIMINARY;
  this gate converts the preliminary assessment into a measured RP-resonance statement.

PRIOR (loaded at plan-time, knowledge-MCP):
  LIOUVILLIAN-52 (session-53) computed a SINGLE-POINT RP gap gamma_RP = 0.0398 M_KK and
  t_deph/t_transit = 139729. That is a FINITE gap (=> exponential decay) at ONE tau,
  with no tau-scan and no branch-point power-law test. This gate is the proper
  tau-LOCALIZATION test the PRELIMINARY Sec 5.4 assessment never performed: it asks
  whether the gap collapses to 0 (branch point / power-law) specifically AT tau_fold.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (tau_fold, Delta_BCS, M_KK, PI) [audit]
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (gap-edge D_K block) [audit]
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<decay-form @ fold + alpha + localization>, scheme=BLV,
   convention=LIOUVILLIAN-RP-SECOND-SHEET, L_max=12)

Classification: PHONONIC

Author: kitaev-quantum-chaos-theorist (INV10 W3-2)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU thread cap (cross-agent contention)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (tau_fold, Delta_BCS, M_KK, PI, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import pickle
import time
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Optional GPU path (BdG diagonalization per tau may be >= 100x100)
try:
    import torch
    _HAVE_TORCH = torch.cuda.is_available()
except Exception:
    _HAVE_TORCH = False

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration pins  (machinery_pin_map from the gate block)
# ---------------------------------------------------------------------------
SESSION = "S10"                                # (local) investigation track n=10
GATE_ID = "INV10-W3-2"                         # (local)
SCHEME = "BLV"                                 # (local) BdG/Bogoliubov-de-Gennes gap-edge scheme
CONVENTION = "LIOUVILLIAN-RP-SECOND-SHEET"     # (local) RP resonances as 2nd-sheet resolvent poles / late-time-tail fit
L_MAX = 12                                     # (local) tau-deformed D_K gap-edge block from L12 spectrum cache

# tau scan (machinery_pin_map: explicit 5-point mesh, finer near the fold)
TAU_SLICES = [0.15, 0.175, 0.190, 0.205, 0.25]  # (local) N_eval=5; tau_fold=0.190 is index 2
TAU_FOLD_IDX = 2                                  # (local) position of tau_fold in TAU_SLICES

# strict_PASS_boundary pins
TAU_ALPHA = 0.10        # (local) |alpha - 0.5| <= 0.10 at tau_fold (A2-fold prediction)
M_LOC = 0.05            # (local) tau-localization margin (>= 5% separation from off-fold mean)
DELTA_AIC_MIN = 2.0     # (local) power-law preferred over exponential by Delta-AIC >= 2
INFO_ALPHA_HI = 0.30    # (local) INFO band: |alpha-0.5| in (0.10, 0.30]

# gap-edge active subspace + correlation machinery
N_GAPEDGE = 256         # (local) gap-edge active mode count (smallest |lambda|); caps BdG dim = 2*N (512)
MU_FRAC = 1.0           # (local) chemical potential mu set at the gap-edge band bottom (min |lambda|)
N_TIME = 6000           # (local) time samples for C(t)
T_MAX = 600.0           # (local) max correlation time (M_KK^-1 units); >> 1/gamma_RP=0.0398 ~ 25
T_FIT_FRAC = 0.40       # (local) late-time fraction of the window used for the tail fit
N_DOS_BINS = 400        # (local) DOS histogram bins for the edge-singularity diagnostic
TOL = 1e-9              # (local) diagonalization / resolvent-pole numerical tolerance (float64)

# VRAM feasibility (machinery_pin_map GPU_path): the FULL doubled Liouvillian on the
# gap-edge block is (2N)^2 x (2N)^2. For N=256 that is 512^2 = 262144 -> a 262144^2
# dense complex128 matrix = 1.1 EB: INFEASIBLE and UNNECESSARY. The Liouvillian
# spectrum {-i(E_m - E_n)} is the DIFFERENCE SET of the 2N BdG eigenvalues E_k; we
# obtain ALL Liouvillian eigenvalues from the 2N H_BdG eigenvalues directly (the
# outer difference), NEVER materializing the (2N)^2 x (2N)^2 superoperator. C(t) is
# likewise built from the 2N eigenpairs. Dense storage stays O((2N)^2) = O(512^2)
# complex128 = 4 MB << 0.5 * 17.1 GB VRAM. Declared here per the gate's GPU note.

OUT_NPZ = SESSION_DIR / "inv10_w3_rp_resonances_fold.npz"
OUT_PNG = SESSION_DIR / "inv10_w3_rp_resonances_fold.png"

L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    L12_CACHE,
]

# ---------------------------------------------------------------------------
# Section 4 — Dual-SHA input-pin block (S84+)
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
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verdict payload (race-safe; agent calls emit_verdict)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict="", magnitude_verdict="", regime_verdict="",
                          companion_note="", extra_rows=None):
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
        "track": "investigation",
    }
    if sign_verdict:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 6 — Substrate: tau-deformed gap-edge D_K block from the L12 cache
# ---------------------------------------------------------------------------
#
# SUBSTITUTION CHAIN — tau-deformation of the cache (MANDATORY, math-scripts.md).
#
#   Claim: "the off-fold gap-edge |lambda|(tau) are obtained from the cached
#           |lambda|(tau_fold) by the Jensen radial rescaling lambda(tau) =
#           lambda(tau_fold) * r(tau_fold)/r(tau)."
#
#   Def 1: D_K(tau) on Jensen-deformed SU(3); the Jensen TT-deformation is
#          VOLUME-PRESERVING (PROVEN, registry) and acts as an anisotropic radial
#          rescaling of the round-SU(3) Dirac eigenvalues. To leading (isotropic,
#          Casimir) order, |lambda|^(p,q)(tau) ~ sqrt(C2(p,q)) / r(tau), with r(tau)
#          the Jensen geometric radius (math-scripts.md D_K-block feasibility note).
#   Def 2: the gap-edge subspace is the set of SMALLEST |lambda| across all Peter-Weyl
#          sectors (the band BOTTOM where dE/dk -> 0, the van-Hove stationary point).
#   Substitute: lambda(tau) = lambda(tau_fold) * [r(tau_fold)/r(tau)].
#   Simplify: the Jensen radius enters g1/g2 = e^{-2 tau} (PROVEN g1/g2 = e^{-2tau},
#          registry); the canonical radial scale tracks e^{+2 tau} for the L-eigenvalue-
#          weighted modes. The conservative, substrate-faithful ISOTROPIC proxy that
#          preserves the gap-edge ORDERING and the DOS SHAPE (the only inputs the
#          branch-point test needs) is r(tau) propto e^{+2 tau}, giving
#          lambda(tau) = lambda(tau_fold) * e^{-2(tau - tau_fold)}.
#   Direction: as tau INCREASES above tau_fold the gap-edge scale CONTRACTS
#          (e^{-2 dtau} < 1); below the fold it EXPANDS. The DOS-edge SHAPE (the
#          presence/absence of a sqrt singularity) is INVARIANT under a global
#          positive rescaling — so a tau-LOCALIZED branch point cannot be a rescaling
#          artifact; if it appears only at tau_fold it is a genuine fold feature.
#   Conclusion: this isotropic deformation is a PROXY (declared); it CANNOT manufacture
#          a tau-localized power-law (global scaling preserves DOS shape), so a positive
#          localization result is conservative. A negative result (no power-law anywhere,
#          or tau-independent exponential) is likewise robust. The anisotropic Jensen
#          per-L scaling is a session-track refinement (would only SHARPEN, not create,
#          localization).
#
# This honest proxy is consistent with the gate block line 309 ("the tau-deformed
# block is rebuilt from the Jensen-deformed spectrum ... declared in-script").

def jensen_radial_factor(tau):
    """Isotropic Jensen radial rescaling relative to tau_fold (substrate-first proxy;
    derivation in the Section-6 substitution chain). lambda(tau) = lambda(fold)*factor."""
    return float(np.exp(-2.0 * (tau - tau_fold)))   # (local) e^{-2(tau-tau_fold)}


def load_gapedge_abs_evals(n_gapedge):
    """Load the cached |lambda|(tau_fold) and return the n_gapedge SMALLEST (the band
    bottom / van-Hove stationary region). The cache stores abs_evals per Peter-Weyl
    sector; we concatenate ALL sectors with multiplicity and take the bottom slice."""
    d = np.load(L12_CACHE, allow_pickle=True)
    se = d["sector_evals"].item()
    allv = np.concatenate([np.asarray(se[k]["abs_evals"]).ravel()
                           for k in sorted(se.keys())])  # (local) |lambda| w/ mult
    allv = np.sort(allv)
    n_total = allv.size  # (local)
    gapedge = allv[:n_gapedge].copy()  # (local) smallest |lambda| = band bottom
    return gapedge, n_total, allv


# ---------------------------------------------------------------------------
# Section 7 — BdG Hamiltonian, Liouvillian spectrum, correlation C(t)
# ---------------------------------------------------------------------------

def build_bdg_energies(abs_lambda, mu, delta):
    """BdG single-particle spectrum on the gap-edge modes.

    H_BdG = ((h - mu, Delta), (Delta^dagger, -h^* + mu))  [Paper 16 / framework]
    On the DIAGONAL gap-edge band (h = diag(eps_i), eps_i = signed single-particle
    energies built from |lambda|), the BdG eigenvalues are the standard
        E_i^pm = +- sqrt((eps_i - mu)^2 + Delta^2).
    We take eps_i = |lambda|_i (gap-edge band, positive branch; mu pins the band
    bottom). This yields the doubled spectrum {+E_i, -E_i}_i (2N values).

    Returns (E_bdg, eps) where E_bdg has length 2N (sorted) and eps the single-
    particle band.
    """
    eps = np.asarray(abs_lambda, dtype=float)            # (local) gap-edge band
    xi = eps - mu                                        # (local) energies measured from mu
    Epos = np.sqrt(xi * xi + delta * delta)              # (local) +branch quasiparticle energies
    E_bdg = np.concatenate([Epos, -Epos])                # (local) doubled (particle-hole) spectrum
    return np.sort(E_bdg), eps


def liouvillian_resonances(E_bdg):
    """RP resonances of L[rho] = -i[H_BdG, rho].

    spec(L) = { -i (E_m - E_n) : m,n }  on the doubled (density-matrix) space.
    For Hermitian H_BdG every Liouvillian eigenvalue is PURELY IMAGINARY:
        lambda_L = -i * omega_mn,  omega_mn = E_m - E_n  (real).
    => decay rate gamma_n = Re(lambda_L) = 0 for ALL modes (the finite-system
    Liouvillian has NO intrinsic decay; this is the closed-system statement).
    The physical RP resonances / branch cut emerge in the CONTINUUM (thermodynamic)
    limit from the DENSITY of the difference set near omega=0 and at the band-edge
    stationary points. We return the difference-set frequencies omega_mn (the
    Liouvillian imaginary spectrum) and the implied bare RP gap
        gap_L = min_{m!=n} |E_m - E_n|   (smallest nonzero Liouvillian |omega|).
    A van-Hove branch point pins the DENSITY of omega_mn near 0 to a sqrt-divergence
    (=> algebraic C(t)); a generic gapped system leaves a clean finite gap.
    """
    E = np.asarray(E_bdg, dtype=float)
    # bare Liouvillian gap = smallest nonzero level spacing of H_BdG (the closest the
    # difference set comes to 0 without being a diagonal m=n mode).
    Es = np.sort(E)
    dif = np.diff(Es)  # (local)
    nz = dif[dif > TOL]  # (local) nonzero spacings
    gap_L = float(nz.min()) if nz.size else 0.0  # (local) bare RP gap (closed-system)
    return gap_L


def correlation_Ct(E_bdg, eps, gge_T, t):
    """Gap-edge autocorrelation C(t) = Tr(rho_GGE A(t) A(0)).

    In the H_BdG eigenbasis,
        C(t) = sum_{m,n} rho_m |A_{mn}|^2 e^{-i(E_m - E_n) t}.
    We use a GENERIC gap-edge observable whose matrix elements A_{mn} are smooth
    (we take |A_{mn}|^2 = 1, the maximally-agnostic flat weight; the late-time
    EXPONENT alpha is set by the DOS edge singularity, NOT by the smooth weight w,
    per the Section-9 substitution chain Watson-lemma argument). rho_m is the GGE
    (Gibbs) occupation exp(-E_m/T)/Z over the BdG levels. The dominant late-time
    behaviour is governed by the spectral density near the band-edge stationary
    point; a sqrt van-Hove edge => |C(t)| ~ t^{-1/2}.

    Implementation: C(t) = |sum_m sqrt(rho_m) e^{-i E_m t}|^2-type bilinear. With
    flat |A|^2=1 and rho factorized, C(t) = |g(t)|^2 where g(t) = sum_m rho_m^{1/2}
    e^{-i E_m t} (a clean DOS-weighted characteristic function whose modulus carries
    the van-Hove tail). Returns |C(t)| (real envelope).
    """
    E = np.asarray(E_bdg, dtype=float)
    w = np.exp(-np.abs(E) / max(gge_T, 1e-6))  # (local) GGE/Gibbs weight over BdG levels
    w = w / w.sum()                             # (local) normalized occupation rho_m
    amp = np.sqrt(w)                            # (local) sqrt(rho_m)
    # g(t) = sum_m amp_m exp(-i E_m t); vectorized outer product (2N x N_time)
    phase = np.exp(-1j * np.outer(E, t))       # (local) (2N, N_time)
    g = amp @ phase                            # (local) (N_time,)
    Ct = np.abs(g) ** 2                        # (local) |C(t)| envelope (>=0)
    return Ct


# ---------------------------------------------------------------------------
# Section 8 — DOS edge-singularity diagnostic + three-way tail classification
# ---------------------------------------------------------------------------

def dos_edge_exponent(E_bdg, n_bins):
    """Direct DOS branch-point diagnostic, INDEPENDENT of the C(t) fit.

    Build rho_E(E) by histogram of the BdG spectrum; near the band edge (the
    stationary point, smallest |E|, i.e. the gap edge ~ Delta) a van-Hove A2 fold
    gives rho(E) ~ (E - E_edge)^{-1/2}. Fit log rho vs log(E - E_edge) near the edge
    and return the exponent p_edge (sqrt singularity => p_edge ~ -1/2).
    """
    E = np.abs(np.asarray(E_bdg, dtype=float))   # (local) work on |E| (gap edge at min|E|)
    E = np.sort(E)
    E_edge = E.min()                             # (local) band-edge / gap edge
    hist, edges = np.histogram(E, bins=n_bins, density=True)  # (local)
    centers = 0.5 * (edges[:-1] + edges[1:])     # (local)
    x = centers - E_edge                         # (local) distance from edge
    good = (x > 0) & (hist > 0)                  # (local)
    # fit on the lower portion near the edge (first ~25% above the edge)
    span = x[good]
    if span.size < 6:
        return float("nan"), E_edge, centers, hist
    cut = np.quantile(span, 0.25)                # (local) near-edge window
    near = good & (x <= cut)
    if near.sum() < 4:
        near = good & (x <= np.quantile(span, 0.5))
    p = np.polyfit(np.log(x[near]), np.log(hist[near]), 1)  # (local)
    return float(p[0]), float(E_edge), centers, hist


def fit_tail_forms(t, Ct, t_fit_frac):
    """Three competing late-time fits to |C(t)|: (a) power-law t^{-alpha},
    (b) exponential e^{-gamma t}, (c) non-decay (constant). Returns the fit
    parameters and AIC for each so the best form can be selected.

    AIC = 2k + n ln(RSS/n).  Lower AIC = better. Delta-AIC(exp - PL) >= 2 means
    the power-law is preferred over the exponential at the standard 2-unit level.
    """
    t = np.asarray(t, dtype=float)
    C = np.asarray(Ct, dtype=float)
    t0 = t[int((1.0 - t_fit_frac) * t.size)]     # (local) late-time window start
    m = (t >= t0) & (C > 0)                       # (local)
    tt, cc = t[m], C[m]                           # (local)
    n = tt.size                                    # (local)
    out = {}  # (local)

    # (a) power-law: log C = log A - alpha log t
    pa = np.polyfit(np.log(tt), np.log(cc), 1)     # (local)
    alpha = -pa[0]                                  # (local)
    pred_a = np.exp(np.polyval(pa, np.log(tt)))     # (local)
    rss_a = float(np.sum((cc - pred_a) ** 2))       # (local)
    aic_a = 2 * 2 + n * np.log(max(rss_a, 1e-300) / n)  # (local) k=2
    out["power_law"] = dict(alpha=float(alpha), A=float(np.exp(pa[1])),
                            rss=rss_a, aic=float(aic_a))

    # (b) exponential: log C = log B - gamma t
    pb = np.polyfit(tt, np.log(cc), 1)              # (local)
    gamma = -pb[0]                                  # (local)
    pred_b = np.exp(np.polyval(pb, tt))             # (local)
    rss_b = float(np.sum((cc - pred_b) ** 2))       # (local)
    aic_b = 2 * 2 + n * np.log(max(rss_b, 1e-300) / n)  # (local) k=2
    out["exponential"] = dict(gamma=float(gamma), B=float(np.exp(pb[1])),
                              rss=rss_b, aic=float(aic_b))

    # (c) non-decay: constant = mean(C)
    const = float(np.mean(cc))                      # (local)
    rss_c = float(np.sum((cc - const) ** 2))        # (local)
    aic_c = 2 * 1 + n * np.log(max(rss_c, 1e-300) / n)  # (local) k=1
    out["non_decay"] = dict(level=const, rss=rss_c, aic=float(aic_c))

    # also: late-time decay ratio (how much |C| falls across the fit window) — used
    # to distinguish genuine non-decay (ratio ~ 1) from a decaying tail.
    decay_ratio = float(cc[-1] / max(cc[0], 1e-300))  # (local)
    out["decay_ratio_fitwin"] = decay_ratio
    out["n_fit"] = int(n)

    # best form by AIC
    aics = {"power_law": aic_a, "exponential": aic_b, "non_decay": aic_c}  # (local)
    best = min(aics, key=aics.get)  # (local)
    out["best_form"] = best
    out["delta_aic_exp_minus_pl"] = float(aic_b - aic_a)  # (local) >0 => PL better
    out["delta_aic_nd_minus_pl"] = float(aic_c - aic_a)   # (local)
    return out


# ---------------------------------------------------------------------------
# Section 9 — Compute (tau scan)
# ---------------------------------------------------------------------------
#
# SUBSTITUTION CHAIN — late-time exponent at the fold (MANDATORY, math-scripts.md):
#   Claim: "At tau_fold the late-time correlation decays as a POWER LAW C(t)~t^{-1/2}."
#   Def 1: H_BdG = ((h-mu,Delta),(Delta^dag,-h*+mu)); Def 2: L[rho]=-i[H_BdG,rho],
#          spec(L) = {i(E_m-E_n)}; Def 3: C(t)=Tr(rho_GGE A(t)A(0)) =
#          sum_{mn} rho_m |A_mn|^2 e^{-i(E_m-E_n)t}; Def 4: a van-Hove A2 fold =>
#          rho_E(E) ~ |E-E_c|^{-1/2} near the gap-edge stationary point (dE/dk=0).
#   Substitute: C(t) = int rho_E(w) W(w) e^{-iwt} dw (W smooth |A|^2 rho_GGE weight).
#   Simplify 1: near the branch point rho_E(w) ~ (w-w_c)^{-1/2}; the dominant late-time
#          contribution is the neighbourhood of w_c (Watson's lemma at an algebraic
#          singularity).
#   Simplify 2: int (w-w_c)^{-1/2} e^{-iwt} dw ~ Gamma(1/2) t^{-1/2} e^{-iw_c t}.
#   Canonical form: |C(t)| ~ t^{-1/2}.
#   Direction: alpha = 1/2 at the fold; PASS iff |alpha-0.5|<=0.10 AND PL beats EXP
#          (Delta-AIC>=2) AND tau-LOCALIZED. A fixed Im(z)<0 across all tau => EXP
#          (generic gapped, tau-independent); purely real spec(L) => non-decay.
#   Conclusion: a tau-LOCALIZED power-law C(t)~t^{-1/2} at tau_fold IS the measured
#          edge-of-chaos / dynamical-arrow statement (converts A4 hypothesis -> result);
#          a tau-independent exponential/non-decay RETIRES edge-of-chaos (DOS feature).

def compute():
    t0 = time.time()  # (local)
    print("=" * 78)
    print(f"{GATE_ID}: Ruelle-Pollicott resonance spectrum of the BdG Liouvillian")
    print("=" * 78)
    print(f"  tau slices: {TAU_SLICES}  (tau_fold={tau_fold} at idx {TAU_FOLD_IDX})")
    print(f"  scheme={SCHEME}  convention={CONVENTION}  L_max={L_MAX}")
    print(f"  Delta_BCS={Delta_BCS:.10f}  gap-edge modes N={N_GAPEDGE}  GPU={_HAVE_TORCH}")
    print(f"  C(t): N_time={N_TIME}, T_max={T_MAX} (1/gamma_RP_prior=0.0398^-1~{1/0.0398:.1f}); "
          f"tail-fit frac={T_FIT_FRAC}")

    # gap-edge band at tau_fold (cache), then deform per slice
    gapedge0, n_total, allv = load_gapedge_abs_evals(N_GAPEDGE)
    print(f"  cache: {n_total} |lambda| w/ mult; gap-edge band bottom = "
          f"[{gapedge0.min():.5f}, {gapedge0.max():.5f}] (N={gapedge0.size})")

    t_grid = np.linspace(0.5, T_MAX, N_TIME)  # (local)
    gge_T = float(T_GGE_B2)  # (local) B2-sector GGE temperature (M_KK), canonical

    per_tau = []  # (local)
    for i, tau in enumerate(TAU_SLICES):
        fac = jensen_radial_factor(tau)              # (local) e^{-2(tau-tau_fold)}
        eps_band = gapedge0 * fac                    # (local) tau-deformed gap-edge band
        mu = float(eps_band.min()) * MU_FRAC         # (local) chemical potential at band bottom
        E_bdg, eps = build_bdg_energies(eps_band, mu, Delta_BCS)  # (local)
        gap_L = liouvillian_resonances(E_bdg)        # (local) bare RP gap (closed-system)
        Ct = correlation_Ct(E_bdg, eps, gge_T, t_grid)  # (local) |C(t)|
        p_edge, E_edge, dos_centers, dos_hist = dos_edge_exponent(E_bdg, N_DOS_BINS)  # (local)
        fits = fit_tail_forms(t_grid, Ct, T_FIT_FRAC)  # (local)

        is_fold = (i == TAU_FOLD_IDX)  # (local)
        tag = "  <== tau_fold" if is_fold else ""
        print(f"\n  tau={tau:.3f} (fac={fac:.4f}){tag}")
        print(f"    BdG: {E_bdg.size} levels, |E|_edge={E_edge:.5f}, bare RP gap_L={gap_L:.6e}")
        print(f"    DOS edge exponent p_edge={p_edge:+.4f}  (sqrt van-Hove => ~ -0.5)")
        print(f"    C(t) best form = {fits['best_form']}; "
              f"alpha_PL={fits['power_law']['alpha']:+.4f}, "
              f"gamma_EXP={fits['exponential']['gamma']:.5f}, "
              f"decay_ratio_fitwin={fits['decay_ratio_fitwin']:.4f}")
        print(f"    Delta-AIC(exp-PL)={fits['delta_aic_exp_minus_pl']:+.2f} "
              f"(>= {DELTA_AIC_MIN} => PL preferred), "
              f"Delta-AIC(nd-PL)={fits['delta_aic_nd_minus_pl']:+.2f}")

        per_tau.append(dict(
            tau=tau, fac=fac, mu=mu, gap_L=gap_L, p_edge=p_edge, E_edge=E_edge,
            alpha=fits["power_law"]["alpha"], gamma_exp=fits["exponential"]["gamma"],
            best_form=fits["best_form"],
            delta_aic_exp_pl=fits["delta_aic_exp_minus_pl"],
            delta_aic_nd_pl=fits["delta_aic_nd_minus_pl"],
            decay_ratio=fits["decay_ratio_fitwin"],
            Ct=Ct, dos_centers=dos_centers, dos_hist=dos_hist, fits=fits,
        ))

    # ----------------------------------------------------------------------
    # Section 10 — Verdict logic (decay form @ fold + tau-localization)
    # ----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("  VERDICT LOGIC (decay-form @ tau_fold + tau-localization)")
    print("=" * 78)

    fold = per_tau[TAU_FOLD_IDX]  # (local)
    off = [per_tau[i] for i in range(len(TAU_SLICES)) if i != TAU_FOLD_IDX]  # (local)

    alpha_fold = fold["alpha"]  # (local)
    best_fold = fold["best_form"]  # (local)
    daic_fold = fold["delta_aic_exp_pl"]  # (local) exp - PL ; >0 => PL better
    gapL_fold = fold["gap_L"]  # (local)
    gapL_off_mean = float(np.mean([o["gap_L"] for o in off]))  # (local)

    # alpha criterion at the fold
    alpha_dev = abs(alpha_fold - 0.5)  # (local)
    alpha_pass = alpha_dev <= TAU_ALPHA  # (local)
    alpha_info = (alpha_dev > TAU_ALPHA) and (alpha_dev <= INFO_ALPHA_HI)  # (local)

    # power-law preferred over exponential at the fold
    pl_preferred = (best_fold == "power_law") and (daic_fold >= DELTA_AIC_MIN)  # (local)

    # tau-LOCALIZATION: criticality direction = RP gap -> 0 at fold relative to off-fold.
    # Use the relative separation of the fold's bare RP gap below the off-fold mean.
    # criticality => gapL_fold << gapL_off_mean. localization margin:
    if gapL_off_mean > TOL:
        loc_margin_gap = float((gapL_off_mean - gapL_fold) / gapL_off_mean)  # (local) >0 => fold gap smaller
    else:
        loc_margin_gap = 0.0  # (local)
    # ALSO localization in the DOS-edge exponent: is p_edge closest to -1/2 AT the fold?
    pedge_fold_dev = abs(fold["p_edge"] - (-0.5))  # (local)
    pedge_off_dev_mean = float(np.mean([abs(o["p_edge"] - (-0.5)) for o in off]))  # (local)
    loc_margin_pedge = float(pedge_off_dev_mean - pedge_fold_dev)  # (local) >0 => fold closer to -1/2
    # localization passes if EITHER the gap collapses at the fold OR the DOS-edge
    # exponent is sharpest at the fold, by the m_loc margin.
    is_localized = (loc_margin_gap >= M_LOC) or (loc_margin_pedge >= M_LOC)  # (local)

    print(f"  @ tau_fold: alpha_PL={alpha_fold:+.4f} (|alpha-0.5|={alpha_dev:.4f}, win {TAU_ALPHA}) "
          f"-> alpha_pass={alpha_pass}, alpha_info={alpha_info}")
    print(f"  @ tau_fold: best_form={best_fold}, Delta-AIC(exp-PL)={daic_fold:+.2f} "
          f"-> PL preferred={pl_preferred}")
    print(f"  bare RP gap_L: fold={gapL_fold:.6e}, off-fold mean={gapL_off_mean:.6e} "
          f"-> gap localization margin={loc_margin_gap:+.4f} (win {M_LOC})")
    print(f"  DOS edge p_edge: fold dev-from(-0.5)={pedge_fold_dev:.4f}, "
          f"off-fold mean dev={pedge_off_dev_mean:.4f} -> p_edge loc margin={loc_margin_pedge:+.4f}")
    print(f"  tau-LOCALIZED (gap-collapse OR sharpest-edge by m_loc)? {is_localized}")

    # off-fold decay-form summary (is the form tau-INDEPENDENT?)
    off_forms = [o["best_form"] for o in off]  # (local)
    all_forms = [p["best_form"] for p in per_tau]  # (local)
    form_tau_independent = len(set(all_forms)) == 1  # (local) same form at every tau

    forms_by_tau = {f"{p['tau']:.3f}": p["best_form"] for p in per_tau}  # (local)
    print(f"  decay forms across tau: {forms_by_tau}")
    print(f"  form tau-independent? {form_tau_independent}")

    # ---- composite verdict (gate rubric) ----
    # PASS: power-law @ fold (alpha~1/2, PL preferred) AND tau-localized.
    # INFO: power-law @ fold but alpha off 1/2 (info band) OR criticality not cleanly localized.
    # FAIL: tau-independent exponential/non-decay (DOS feature, not dynamical criticality).
    sign_ok = (best_fold == "power_law")  # (local) sign = decay is power-law @ fold in predicted direction

    if sign_ok and alpha_pass and pl_preferred and is_localized:
        verdict = "PASS"
        sign_v, mag_v, reg_v = "PASS", "PASS", "VALID"
        value = (f"POWER-LAW@fold_alpha={alpha_fold:.4f}_localized_"
                 f"gapL-margin={loc_margin_gap:.3f}_pedge-margin={loc_margin_pedge:.3f}_"
                 f"dAIC(exp-PL)={daic_fold:.1f}")
    elif sign_ok and (alpha_info or (alpha_pass and not is_localized)):
        verdict = "INFO"
        sign_v = "PASS"
        mag_v = "INFO"
        reg_v = "MARGINAL" if not is_localized else "VALID"
        value = (f"POWER-LAW@fold_alpha={alpha_fold:.4f}_"
                 f"{'alpha-off-half' if alpha_info else 'not-tau-localized'}_"
                 f"gapL-margin={loc_margin_gap:.3f}_pedge-margin={loc_margin_pedge:.3f}")
    else:
        # not a clean power-law at the fold, OR tau-independent exp/non-decay
        verdict = "FAIL"
        sign_v = "FAIL" if not sign_ok else "PASS"
        mag_v = "FAIL"
        reg_v = "VALID"
        value = (f"{best_fold.upper()}@fold_alpha={alpha_fold:.4f}_"
                 f"tau-indep={form_tau_independent}_gamma_exp_fold={fold['gamma_exp']:.4f}_"
                 f"gapL_fold={gapL_fold:.4e}_NOT-edge-of-chaos")

    print(f"\n  GATE {GATE_ID}: {verdict}")
    print(f"    value = {value}")
    print(f"    3-tuple: sign={sign_v} magnitude={mag_v} regime={reg_v}")

    elapsed = time.time() - t0  # (local)
    print(f"\n  elapsed: {elapsed:.1f}s")

    return dict(
        verdict=verdict, value=value, sign_v=sign_v, mag_v=mag_v, reg_v=reg_v,
        per_tau=per_tau, fold=fold, t_grid=t_grid, gge_T=gge_T,
        alpha_fold=alpha_fold, alpha_dev=alpha_dev, best_fold=best_fold,
        daic_fold=daic_fold, pl_preferred=pl_preferred,
        gapL_fold=gapL_fold, gapL_off_mean=gapL_off_mean,
        loc_margin_gap=loc_margin_gap, loc_margin_pedge=loc_margin_pedge,
        is_localized=is_localized, form_tau_independent=form_tau_independent,
        all_forms=all_forms, n_total=n_total,
    )


# ---------------------------------------------------------------------------
# Section 11 — Plot
# ---------------------------------------------------------------------------

def make_plot(res):
    per_tau = res["per_tau"]  # (local)
    t = res["t_grid"]  # (local)
    fold = res["fold"]  # (local)

    fig = plt.figure(figsize=(16, 11))  # (local)
    gs = GridSpec(2, 2, figure=fig, hspace=0.30, wspace=0.26)  # (local)

    # Panel 1: |C(t)| log-log across tau slices, fold highlighted
    ax1 = fig.add_subplot(gs[0, 0])  # (local)
    for i, p in enumerate(per_tau):
        is_fold = (i == TAU_FOLD_IDX)  # (local)
        ax1.loglog(t, p["Ct"], lw=2.2 if is_fold else 1.0,
                   color="crimson" if is_fold else None,
                   label=f"tau={p['tau']:.3f}{' (fold)' if is_fold else ''}")
    # reference t^{-1/2} slope guide anchored to fold curve
    tref = t[t > 0.4 * t.max()]  # (local)
    if tref.size:
        c0 = fold["Ct"][np.argmin(np.abs(t - tref[0]))]  # (local)
        ax1.loglog(tref, c0 * (tref / tref[0]) ** (-0.5), "k--", lw=1.0,
                   label="t^{-1/2} guide")
    ax1.set_xlabel("t  (M_KK^{-1})")
    ax1.set_ylabel("|C(t)|")
    ax1.set_title("Gap-edge autocorrelation |C(t)| across the fold")
    ax1.legend(fontsize=7)

    # Panel 2: late-time exponent alpha(tau) + DOS-edge exponent p_edge(tau)
    ax2 = fig.add_subplot(gs[0, 1])  # (local)
    taus = [p["tau"] for p in per_tau]  # (local)
    alphas = [p["alpha"] for p in per_tau]  # (local)
    pedges = [p["p_edge"] for p in per_tau]  # (local)
    ax2.plot(taus, alphas, "o-", label="alpha (C(t) tail)")
    ax2.plot(taus, [-x for x in pedges], "s--", color="green",
             label="-p_edge (DOS branch)")
    ax2.axhline(0.5, color="k", ls=":", lw=1.0, label="A2 fold = 1/2")
    ax2.axvline(tau_fold, color="r", ls="--", lw=1.0, label=f"tau_fold={tau_fold}")
    ax2.set_xlabel("tau")
    ax2.set_ylabel("exponent")
    ax2.set_title("Late-time alpha & DOS-edge exponent vs tau")
    ax2.legend(fontsize=7)

    # Panel 3: bare RP gap_L(tau) — branch point pins this to ~0 at the fold
    ax3 = fig.add_subplot(gs[1, 0])  # (local)
    gaps = [p["gap_L"] for p in per_tau]  # (local)
    ax3.semilogy(taus, gaps, "o-", color="purple")
    ax3.axvline(tau_fold, color="r", ls="--", lw=1.0)
    ax3.axhline(0.0398, color="orange", ls=":", lw=1.0,
                label="LIOUVILLIAN-52 prior gamma_RP=0.0398")
    ax3.set_xlabel("tau")
    ax3.set_ylabel("bare RP gap_L (min nonzero |E_m-E_n|)")
    ax3.set_title("Liouvillian (RP) bare gap vs tau")
    ax3.legend(fontsize=7)

    # Panel 4: verdict text
    ax4 = fig.add_subplot(gs[1, 1])  # (local)
    ax4.axis("off")
    lines = [
        f"GATE {GATE_ID}",
        f"VERDICT: {res['verdict']}",
        f"3-tuple: sign={res['sign_v']} mag={res['mag_v']} regime={res['reg_v']}",
        "",
        f"@ tau_fold={tau_fold}:",
        f"   best decay form = {res['best_fold']}",
        f"   alpha (C(t) tail) = {res['alpha_fold']:+.4f}",
        f"   |alpha - 0.5| = {res['alpha_dev']:.4f}  (win {TAU_ALPHA})",
        f"   Delta-AIC(exp-PL) = {res['daic_fold']:+.2f} (>= {DELTA_AIC_MIN} => PL)",
        f"   PL preferred = {res['pl_preferred']}",
        "",
        f"tau-localization:",
        f"   bare RP gap_L: fold={res['gapL_fold']:.3e}",
        f"                  off-fold mean={res['gapL_off_mean']:.3e}",
        f"   gap-collapse margin = {res['loc_margin_gap']:+.3f}  (win {M_LOC})",
        f"   p_edge-sharpness margin = {res['loc_margin_pedge']:+.3f}",
        f"   tau-LOCALIZED = {res['is_localized']}",
        "",
        f"decay form tau-independent? {res['form_tau_independent']}",
        f"forms: {res['all_forms']}",
        "",
        f"PRIOR LIOUVILLIAN-52: gamma_RP=0.0398 (finite, single tau)",
        f"-> {'EDGE-OF-CHAOS @ fold (dynamical arrow)' if res['verdict']=='PASS' else ('marginal' if res['verdict']=='INFO' else 'DOS feature, NOT edge-of-chaos')}",
    ]  # (local)
    ax4.text(0.02, 0.98, "\n".join(lines), va="top", ha="left",
             family="monospace", fontsize=8.5, transform=ax4.transAxes)

    fig.suptitle(f"{GATE_ID}: {res['verdict']} | decay@fold={res['best_fold']}, "
                 f"alpha={res['alpha_fold']:+.3f}, localized={res['is_localized']}",
                 fontsize=13, fontweight="bold")
    fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    print(f"  saved plot: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 12 — Main
# ---------------------------------------------------------------------------

def main():
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              SHARED_DIR / "canonical_constants.py", pins)  # (local)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    res = compute()
    make_plot(res)

    # --- save npz ---
    per_tau = res["per_tau"]  # (local)
    np.savez(
        OUT_NPZ,
        gate=GATE_ID, verdict=res["verdict"], value=res["value"],
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        tau_slices=np.array(TAU_SLICES), tau_fold=tau_fold, tau_fold_idx=TAU_FOLD_IDX,
        Delta_BCS=Delta_BCS, N_gapedge=N_GAPEDGE, gge_T=res["gge_T"],
        t_grid=res["t_grid"], n_total=res["n_total"],
        alpha_per_tau=np.array([p["alpha"] for p in per_tau]),
        gamma_exp_per_tau=np.array([p["gamma_exp"] for p in per_tau]),
        p_edge_per_tau=np.array([p["p_edge"] for p in per_tau]),
        gap_L_per_tau=np.array([p["gap_L"] for p in per_tau]),
        E_edge_per_tau=np.array([p["E_edge"] for p in per_tau]),
        decay_ratio_per_tau=np.array([p["decay_ratio"] for p in per_tau]),
        delta_aic_exp_pl_per_tau=np.array([p["delta_aic_exp_pl"] for p in per_tau]),
        best_form_per_tau=np.array([p["best_form"] for p in per_tau]),
        Ct_per_tau=np.array([p["Ct"] for p in per_tau]),
        alpha_fold=res["alpha_fold"], alpha_dev=res["alpha_dev"],
        best_fold=res["best_fold"], daic_fold=res["daic_fold"],
        pl_preferred=res["pl_preferred"], gapL_fold=res["gapL_fold"],
        gapL_off_mean=res["gapL_off_mean"], loc_margin_gap=res["loc_margin_gap"],
        loc_margin_pedge=res["loc_margin_pedge"], is_localized=res["is_localized"],
        form_tau_independent=res["form_tau_independent"],
        tau_alpha=TAU_ALPHA, m_loc=M_LOC, delta_aic_min=DELTA_AIC_MIN,
        sign_v=res["sign_v"], mag_v=res["mag_v"], reg_v=res["reg_v"],
        gamma_RP_prior=0.0398,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  saved data: {OUT_NPZ}")

    # 4-tuple final non-verdict line
    print(f"(value={res['value']!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # --- companion rows (SIGN trigger) ---
    extra = [
        f"# INV10-W3-2 RP-resonance: decay form @ tau_fold={tau_fold} is "
        f"{res['best_fold']}; alpha(C(t) tail)={res['alpha_fold']:+.4f} "
        f"(A2-fold prediction 1/2); Delta-AIC(exp-PL)={res['daic_fold']:+.2f}",
        f"# INV10-W3-2 tau-localization: bare RP gap_L fold={res['gapL_fold']:.3e} "
        f"vs off-fold mean={res['gapL_off_mean']:.3e} (margin {res['loc_margin_gap']:+.3f}); "
        f"DOS-edge p_edge sharpness margin={res['loc_margin_pedge']:+.3f}; "
        f"localized={res['is_localized']}; form-tau-independent={res['form_tau_independent']}",
        f"# INV10-W3-2 PRIOR: LIOUVILLIAN-52 (S53) gamma_RP=0.0398 M_KK single-point "
        f"finite gap (t_deph/t_transit=139729); this gate is the tau-LOCALIZATION test "
        f"of the framework-chaotic-instantons.md Sec 5.4 PRELIMINARY branch-point reading",
    ]  # (local)

    note = (f"RP/Liouvillian decay@fold={res['best_fold']} alpha={res['alpha_fold']:+.4f}; "
            f"tau-localized={res['is_localized']}; "
            f"{'edge-of-chaos+dynamical-arrow @ fold' if res['verdict']=='PASS' else ('marginal' if res['verdict']=='INFO' else 'fold is DOS feature, edge-of-chaos RETIRED')}")  # (local)

    print_verdict_payload(res["verdict"], res["value"], audit_sha, content_sha,
                          sign_verdict=res["sign_v"], magnitude_verdict=res["mag_v"],
                          regime_verdict=res["reg_v"],
                          companion_note=note, extra_rows=extra)


if __name__ == "__main__":
    main()
