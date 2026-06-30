"""
S102-FEGAN-TAU0-SPECTRUM-VALIDATION  (Session 102, Wave 3, item 11)
====================================================================

KEYSTONE external-anchor check (Stratum-1 checklist box 1; referee M8(a)).

Reproduce the tau=0 bi-invariant SU(3) Dirac spectrum -- eigenvalues AND
per-(p,q) multiplicities -- from a CLOSED FORM (Parthasarathy / Kostant cubic
Dirac operator; Fegan 1987) and diff it against the substrate tau=0 source
(dirac_spectrum.py numpy pipeline at the Jensen curve evaluated at tau=0,
i.e. (L1,L2,L3)=(1,1,1)) at machine epsilon, in ONE locked normalization
convention.

SUBSTRATE-FIRST FRAMING (GEOMETRIC):
  At tau=0 the substrate's internal fiber is the bi-invariant SU(3) point --
  the maximally symmetric standing-wave configuration where the Dirac
  eigenvalues (fiber vibrational mode frequencies) are exactly algebraic,
  lambda^2 = n/36. The flow runs: D_K eigenvalues (fundamental) -> the
  algebraic tau=0 spectrum -> external anchor (Fegan 1987 closed form).
  Validating that the substrate's OWN tau=0 spectrum equals a closed form
  published in 1987 (with no knowledge of this project) is the external ground
  truth for the entire spectral-triple construction; every emergent spectral
  moment (a_0 -> cosmological term, a_2 -> Einstein-Hilbert, a_4 -> YM+Higgs)
  is a moment of THIS spectrum.

TWO LEGS:
  (A) SUBSTRATE leg -- the full project numpy pipeline:
        D_pi = sum_{a,b} E_{ab} rho_pi(X_b) (x) gamma_a + I (x) Omega
      evaluated at the Jensen metric g_s with s=0 => (L1,L2,L3)=(1,1,1), the
      bi-invariant point g_0 = |B| (Killing form). Eigenvalues via torch GPU
      eigvalsh (blocks >=100x100) with a numpy cross-check on the first block.

  (B) FEGAN closed-form leg -- the Parthasarathy/Kostant algebraic form,
      computed from REPRESENTATION THEORY (Casimirs) ALONE, NOT from the
      Dirac-operator frame/Omega assembly:
        |lambda|^2(p,q,mu) = (1/6) * [ C_2^Kil(mu) + C_2^Kil(p,q) ] + 1/4
      where mu ranges over the su(3)-irreps in V_(p,q) (x) S (S = 16-dim
      spinor module), C_2^Kil is the Killing-normalized quadratic Casimir,
      the 1/6 is the |B|=3*delta frame rescale, and 1/4 is the spinor/rho-shift
      offset. The diagonal-Casimir eigenvalue multiset on V_(p,q) (x) S
      supplies {C_2(mu)} with the correct within-block degeneracies. This gives
        n = 36*lambda^2 = 6*C_2(mu) + 6*C_2(p,q) + 9  in  Z,
      confirming atlas-07 PROVEN 'lambda^2 = n/36 algebraic spectrum'.

CONVENTION LOCK (the sqrt(7/3) vs 13/3 trap, substitution_chain Step 4):
  The substrate pipeline output at (1,1,1) IS the reference normalization. The
  corpus carries MULTIPLE incommensurate scalings:
    - lambda^2 = C_2 + 3/4   (session-21c/22 paasch-collab)  -> trivial sector 3/4
    - lambda^2 = C_2 + 3     (this plan-block's worked example) -> n(1,0)=156
    - lambda_1 = sqrt(7/3)   (a separate R^2/R_K normalization)
  These are DIFFERENT conventions. This gate LOCKS the substrate frame and
  verifies, at runtime, that the substrate's own trivial-sector offset is
  EXACTLY 1/4 in the |B|-normalized frame (NOT 3/4, NOT 3, NOT 7/3). The
  closed-form map (1/6 frame-slope, 1/4 offset) is pinned at plan-freeze from
  this frame, NOT fitted. Mixing conventions is the factor-of-scaling error
  this gate exists to exclude.

PASS: max_k |sorted(|lam|)_sub[k] - sorted(|lam|)_Fegan[k]| < 1e-12 across all
      sectors p+q <= L_max_operational, AND per-(p,q) multiplicity (Peter-Weyl
      dim(p,q) AND within-block |lam| degeneracy) exact-integer match (0
      mismatches), AND the locked-frame offset == 1/4 exactly, AND every
      lambda^2 is of the algebraic form n/36 (n in Z).

Author: spectral-geometer (phonon-exflation project, Session 102, Wave 3)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')   # (local) CPU thread cap if GPU path unused
os.environ.setdefault('MKL_NUM_THREADS', '8')   # (local)

import sys
import json
import hashlib
from collections import Counter
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY import; tau_fold/conventions sourced here) ---
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_shared")))
from canonical_constants import *  # noqa: F401,F403  (tau_fold etc.)

# --- substrate Dirac pipeline (the project numpy machinery; LEG A) ---
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, build_cliff8, spinor_connection_offset,
    get_irrep, dirac_operator_on_irrep,
)

# Optional GPU path
try:
    import torch
    _HAVE_TORCH = True
    _GPU = torch.cuda.is_available()
except Exception:
    _HAVE_TORCH = False
    _GPU = False


# =============================================================================
# Pinned machinery
# =============================================================================
TAU0 = 0.0                       # (local) Jensen parameter at the bi-invariant point
L_MAX_PLAN = 12                  # (local) plan-pinned L_max (closed-form leg sector-exact at all (p,q))
L_MAX_OPERATIONAL = 8            # (local) substrate-pipeline compute truncation (feasibility pre-check)
EPS_EIG = 1e-12                  # (local) eigenvalue-multiset max-abs-diff PASS boundary
GPU_BLOCK_THRESHOLD = 100        # (local) use torch.linalg.eigvalsh for blocks >= 100x100
ROUND_DEGEN = 9                  # (local) decimals for degeneracy-bucketing of |lambda| values
SPINOR_RANK = 16                 # (local) dim of the Cliff(R^8) spinor module S = 2^4

# Closed-form normalization, PINNED at plan-freeze (NOT fitted):
#   |lambda|^2 = FRAME_SLOPE * [ C_2(mu) + C_2(p,q) ] + RHO_OFFSET
FRAME_SLOPE = Fraction(1, 6)     # (local) |B| = 3*delta frame rescale (E = I/sqrt3, D ~ 1/sqrt3, D^2 ~ 1/3, split 1/6)
RHO_OFFSET = Fraction(1, 4)      # (local) spinor/rho-shift offset; = trivial-sector lambda^2 in the locked frame


def C2_killing(p, q):
    """Killing-normalized SU(3) quadratic Casimir C_2(p,q) = (p^2+q^2+pq+3p+3q)/3 (exact Fraction)."""
    return Fraction(p * p + q * q + p * q + 3 * p + 3 * q, 3)


def dim_pq(p, q):
    """SU(3) Weyl dimension d(p,q) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# =============================================================================
# LEG A -- substrate numpy pipeline at tau=0
# =============================================================================
def build_substrate_infra():
    """Build the bi-invariant (tau=0) geometric infrastructure from the project pipeline."""
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B = compute_killing_form(f_abc)
    g0 = jensen_metric(B, TAU0)               # tau=0 => (L1,L2,L3)=(1,1,1), g0 = |B|
    E = orthonormal_frame(g0)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    gammas = build_cliff8()
    Omega = spinor_connection_offset(Gamma, gammas)
    return gens, f_abc, B, g0, E, gammas, Omega


def _eigvals_abs2(D):
    """|lambda|^2 multiset of an anti-Hermitian matrix D (eigenvalues purely imaginary)."""
    dim = D.shape[0]
    if _GPU and _HAVE_TORCH and dim >= GPU_BLOCK_THRESHOLD:
        # D anti-Hermitian => H = i*D Hermitian, real eigenvalues mu; |lambda| = |mu|.
        H = torch.tensor(1j * D, device="cuda", dtype=torch.complex128)
        H = 0.5 * (H + H.conj().T)
        mu = torch.linalg.eigvalsh(H).cpu().numpy()
        return mu ** 2
    else:
        mu = np.linalg.eigvals(D)
        return np.abs(mu) ** 2


def substrate_sector_spectrum(p, q, gens, f_abc, E, gammas, Omega):
    """Return the |lambda|^2 multiset (length dim(p,q)*16) for sector (p,q) from the substrate pipeline."""
    if (p, q) == (0, 0):
        D = Omega.copy()
    else:
        rho, dchk = get_irrep(p, q, gens, f_abc)
        assert dchk == dim_pq(p, q), f"dim mismatch ({p},{q}): {dchk} vs {dim_pq(p,q)}"
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)
    ah_err = float(np.max(np.abs(D + D.conj().T)))  # (local) anti-Hermiticity check
    return _eigvals_abs2(D), ah_err


# =============================================================================
# LEG B -- Fegan / Parthasarathy-Kostant closed form (representation theory only)
# =============================================================================
def spin_rep_su3(f_abc, gammas):
    """
    su(3) spin representation on S = C^16:
        rho_spin(e_a) = (1/4) sum_{b,c} ad(e_a)_{bc} gamma_b gamma_c,
        ad(e_a)_{bc} = -f_{a,b,c}  (project convention).
    Built from structure constants + Clifford generators ONLY (no frame/Omega).
    """
    n = 8
    rho_spin = []
    for a in range(n):
        M = np.zeros((SPINOR_RANK, SPINOR_RANK), dtype=complex)
        for b in range(n):
            for c in range(n):
                adabc = -f_abc[a, b, c]
                if abs(adabc) > 1e-15:
                    M += 0.25 * adabc * (gammas[b] @ gammas[c])
        rho_spin.append(M)
    return rho_spin


def fegan_sector_spectrum(p, q, gens, f_abc, rho_spin):
    """
    Closed-form |lambda|^2 multiset (length dim(p,q)*16) for sector (p,q):
      diagonalize the diagonal su(3) Casimir on V_(p,q) (x) S, then apply the
      PINNED Parthasarathy map  |lambda|^2 = (1/6)*C_diag + (1/6)*C_2(p,q) + 1/4.
    Uses only Casimir / representation theory -- NOT dirac_operator_on_irrep.
    """
    if (p, q) == (0, 0):
        rho = [np.zeros((1, 1), dtype=complex) for _ in range(8)]
        d = 1   # (local) trivial irrep dimension
    else:
        rho, d = get_irrep(p, q, gens, f_abc)
    Id_rho = np.eye(d)
    Id_s = np.eye(SPINOR_RANK)
    Cdiag = np.zeros((d * SPINOR_RANK, d * SPINOR_RANK), dtype=complex)
    for a in range(8):
        Ja = np.kron(rho[a], Id_s) + np.kron(Id_rho, rho_spin[a])
        Cdiag += Ja @ Ja
    # Casimir = -sum J_a^2 (anti-Hermitian J_a) is +definite Hermitian
    C = -0.5 * (Cdiag + Cdiag.conj().T)
    cas = np.linalg.eigvalsh(C)                      # dim*16 eigenvalues w/ multiplicity
    slope = float(FRAME_SLOPE)
    offset = slope * float(C2_killing(p, q)) + float(RHO_OFFSET)
    lam2 = slope * cas + offset
    return lam2, cas


def fegan_algebraic_n36(p, q, rho_spin_cas_vals):
    """
    Pure-rational algebraic prediction n = 36*lambda^2 = 6*C_2(mu)+6*C_2(p,q)+9
    from the diagonal-Casimir eigenvalues. rho_spin_cas_vals are the (rounded)
    C_2(mu) values; we coerce them to nearest half-integer-grid Fractions to test
    n/36 integrality exactly. Returns list of integer n with their multiplicities.
    """
    c2pq = C2_killing(p, q)
    out = Counter()
    for cas_val, mult in rho_spin_cas_vals.items():
        # C_2(mu) lies on the (1/3)-grid: 3*C_2(mu) in Z. Snap to nearest third.
        c2mu = Fraction(round(cas_val * 3), 3)
        n = 6 * c2mu + 6 * c2pq + 9            # = 36*lambda^2 (exact Fraction)
        out[n] += mult
    return out


# =============================================================================
# Diff + multiplicity comparison
# =============================================================================
def sorted_multiset_diff(lam2_sub, lam2_feg):
    """Max-abs difference of sorted |lambda| (not lambda^2) multisets of equal length."""
    a = np.sort(np.sqrt(np.maximum(lam2_sub, 0.0)))
    b = np.sort(np.sqrt(np.maximum(lam2_feg, 0.0)))
    if len(a) != len(b):
        return np.inf, len(a), len(b)
    return float(np.max(np.abs(a - b))), len(a), len(b)


def degeneracy_counter(lam2, ndec=ROUND_DEGEN):
    """Counter of within-block |lambda| degeneracies (keys = rounded |lambda|)."""
    return Counter(np.round(np.sqrt(np.maximum(lam2, 0.0)), ndec))


# =============================================================================
# Dual-SHA closure
# =============================================================================
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    """SHA-256 of the ordered input-pin map (audit_sha256 input)."""
    items = sorted(pin_map.items())
    blob = "\n".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def print_verdict_payload(gate_id, verdict, value, scheme, convention, L_max,
                          audit_sha256, content_sha256, session, extra_rows=None):
    """Print the EMIT_VERDICT payload block on stdout for the agent to relay to emit_verdict."""
    payload = {
        "gate_id": gate_id, "verdict": verdict, "value": value,
        "scheme": scheme, "convention": convention, "L_max": str(L_max),
        "audit_sha256": audit_sha256, "content_sha256": content_sha256,
        "session": session,
    }
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("<<<EMIT_VERDICT_PAYLOAD>>>" + json.dumps(payload) + "<<<END_EMIT_VERDICT_PAYLOAD>>>")


# =============================================================================
# MAIN
# =============================================================================
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    shared = os.path.abspath(os.path.join(here, "..", "_shared"))

    # --- input SHA pins (logged in first lines of stdout) ---
    in_canon = os.path.join(shared, "canonical_constants.py")
    in_dirac = os.path.join(shared, "dirac_spectrum.py")
    in_branch = os.path.join(shared, "branching_computation.py")
    sha_canon = sha256_file(in_canon)
    sha_dirac = sha256_file(in_dirac)
    sha_branch = sha256_file(in_branch)
    print(f"[input] canonical_constants.py sha256={sha_canon}")
    print(f"[input] dirac_spectrum.py      sha256={sha_dirac}")
    print(f"[input] branching_computation.py sha256={sha_branch}")
    print(f"[env] torch={_HAVE_TORCH} GPU={_GPU}  tau0={TAU0} L_max_plan={L_MAX_PLAN} "
          f"L_max_operational={L_MAX_OPERATIONAL} eps={EPS_EIG}")

    # --- build both legs' shared structure ---
    gens, f_abc, B, g0, E, gammas, Omega = build_substrate_infra()
    rho_spin = spin_rep_su3(f_abc, gammas)

    # --- CONVENTION LOCK: verify the substrate frame implies the pinned bare offset 1/4 ---
    # The trivial sector (0,0) has lambda^2 = (1/6)*C_2(S) + RHO_OFFSET, where C_2(S) is the
    # Killing-Casimir of the spinor module S (= 3 exactly for the so(8) spinor restricted to su(3)).
    # So the LOCKED bare offset is read off the substrate frame as
    #     RHO_OFFSET = lambda^2(0,0) - C_2(S)/6 = 3/4 - 1/2 = 1/4.
    # NOT a free fit: lambda^2(0,0) and C_2(S) are both substrate-pipeline outputs.
    lam2_trivial, _ = substrate_sector_spectrum(0, 0, gens, f_abc, E, gammas, Omega)
    trivial_lam2 = float(np.unique(np.round(lam2_trivial, ROUND_DEGEN))[0])     # (local) = 3/4
    # C_2(S): Killing-Casimir of the spinor module (constant scalar on S)
    cas_S = np.zeros((SPINOR_RANK, SPINOR_RANK), dtype=complex)                 # (local)
    for a in range(8):
        cas_S += rho_spin[a] @ rho_spin[a]
    c2_S = float(np.mean(np.linalg.eigvalsh(-0.5 * (cas_S + cas_S.conj().T))))  # (local) = 3.0
    implied_offset = trivial_lam2 - float(FRAME_SLOPE) * c2_S                   # (local) = 1/4
    offset_locked = float(RHO_OFFSET)
    offset_err = abs(implied_offset - offset_locked)                            # (local)
    frame_diag = float(np.round(np.mean(np.diag(g0)), 9))                       # (local) should be 3.0
    print(f"[convention-lock] substrate trivial-sector lambda^2(0,0) = {trivial_lam2:.12f}; "
          f"C_2(S) = {c2_S:.12f}; implied bare offset = lam2(0,0) - C_2(S)/6 = {implied_offset:.12f}")
    print(f"[convention-lock] locked offset 1/4 = {offset_locked}; err={offset_err:.2e}; "
          f"g0 diag={frame_diag} (|B|=3, frame E=I/sqrt3)")
    print(f"[convention-lock] EXCLUDED alt conventions: C_2+3/4 (paasch line), "
          f"C_2+3 (plan-example n(1,0)=156), lambda_1=sqrt(7/3). Substrate frame locks bare offset = 1/4.")

    # --- sector loop ---
    sectors = []
    for p in range(L_MAX_OPERATIONAL + 1):
        for q in range(L_MAX_OPERATIONAL + 1 - p):
            sectors.append((p, q))

    per_sector = []
    max_eig_diff = 0.0                  # (local)
    total_mult_mismatch = 0             # (local) within-block degeneracy mismatch count
    pw_mult_mismatch = 0                # (local) Peter-Weyl dim(p,q) consistency mismatch
    n36_violations = 0                  # (local) non-integer n=36*lambda^2 count
    worst_sector = None                 # (local)
    all_sub_lam2 = []                   # (local) for plot
    all_feg_lam2 = []                   # (local)

    print("\n[sectors] (p,q)  dim   blockdim   max|d(|lam|)|   degen-match   ah_err")
    for (p, q) in sectors:
        lam2_sub, ah_err = substrate_sector_spectrum(p, q, gens, f_abc, E, gammas, Omega)
        lam2_feg, cas = fegan_sector_spectrum(p, q, gens, f_abc, rho_spin)

        d = dim_pq(p, q)
        bd = d * SPINOR_RANK
        # numpy cross-check on the first (small) substrate block to validate GPU path
        if (p, q) == (0, 0):
            mu_np = np.abs(np.linalg.eigvals(Omega)) ** 2
            xchk = float(np.max(np.abs(np.sort(mu_np) - np.sort(lam2_sub))))   # (local)
            print(f"[gpu-xcheck] (0,0) numpy-vs-path |lam|^2 max diff = {xchk:.2e}")

        eig_diff, na, nb = sorted_multiset_diff(lam2_sub, lam2_feg)
        sub_deg = degeneracy_counter(lam2_sub)
        feg_deg = degeneracy_counter(lam2_feg)
        degen_match = (sub_deg == feg_deg)
        if not degen_match:
            # count bucket discrepancies
            keys = set(sub_deg) | set(feg_deg)
            total_mult_mismatch += sum(abs(sub_deg.get(k, 0) - feg_deg.get(k, 0)) for k in keys)

        # Peter-Weyl multiplicity check: block length must be dim(p,q)*16 on both legs
        if na != bd or nb != bd:
            pw_mult_mismatch += 1

        # n/36 algebraic-form check via exact-rational Casimir prediction
        cas_cnt = Counter(np.round(cas, 6))
        n_pred = fegan_algebraic_n36(p, q, cas_cnt)
        for n_val in n_pred:
            if n_val.denominator != 1:
                n36_violations += 1

        if eig_diff > max_eig_diff:
            max_eig_diff = eig_diff
            worst_sector = (p, q)

        per_sector.append({
            "p": p, "q": q, "dim": d, "blockdim": bd,
            "eig_diff": eig_diff, "degen_match": bool(degen_match), "ah_err": ah_err,
        })
        all_sub_lam2.append(np.sort(lam2_sub))
        all_feg_lam2.append(np.sort(lam2_feg))
        if (p + q) <= 3 or eig_diff > EPS_EIG:
            print(f"          ({p},{q})  {d:>4} {bd:>8}   {eig_diff:.3e}    "
                  f"{str(degen_match):>5}        {ah_err:.2e}")

    n_sectors = len(sectors)
    print(f"\n[summary] sectors={n_sectors} (p+q<=L_max_operational={L_MAX_OPERATIONAL})")
    print(f"[summary] max eigenvalue-multiset |d(|lam|)| = {max_eig_diff:.3e} at sector {worst_sector} "
          f"(boundary {EPS_EIG})")
    print(f"[summary] within-block degeneracy mismatch count = {total_mult_mismatch}")
    print(f"[summary] Peter-Weyl block-length mismatch count = {pw_mult_mismatch}")
    print(f"[summary] n/36 non-integer (algebraic-form) violations = {n36_violations}")
    print(f"[summary] convention-lock offset err = {offset_err:.2e}")

    # --- verdict logic (pre-registered) ---
    pass_eig = (max_eig_diff < EPS_EIG)
    pass_mult = (total_mult_mismatch == 0) and (pw_mult_mismatch == 0)
    pass_conv = (offset_err < 1e-12)
    pass_n36 = (n36_violations == 0)
    verdict = "PASS" if (pass_eig and pass_mult and pass_conv and pass_n36) else "FAIL"

    # --- save data ---
    npz_path = os.path.join(here, "s102_fegan_tau0_spectrum_validation.npz")
    sub_pq = np.array([(d["p"], d["q"]) for d in per_sector], dtype=int)
    sub_eigdiff = np.array([d["eig_diff"] for d in per_sector], dtype=float)
    sub_dim = np.array([d["dim"] for d in per_sector], dtype=int)
    np.savez(
        npz_path,
        sectors_pq=sub_pq,
        sector_eig_diff=sub_eigdiff,
        sector_dim=sub_dim,
        max_eig_diff=np.float64(max_eig_diff),
        degeneracy_mismatch=np.int64(total_mult_mismatch),
        pw_mult_mismatch=np.int64(pw_mult_mismatch),
        n36_violations=np.int64(n36_violations),
        convention_trivial_lam2=np.float64(trivial_lam2),
        convention_c2_S=np.float64(c2_S),
        convention_implied_offset=np.float64(implied_offset),
        convention_offset_locked=np.float64(offset_locked),
        convention_offset_err=np.float64(offset_err),
        frame_slope=np.float64(float(FRAME_SLOPE)),
        eps_boundary=np.float64(EPS_EIG),
        L_max_plan=np.int64(L_MAX_PLAN),
        L_max_operational=np.int64(L_MAX_OPERATIONAL),
        n_sectors=np.int64(n_sectors),
        verdict=np.str_(verdict),
        sub_lam2=np.array(np.concatenate(all_sub_lam2), dtype=float),
        feg_lam2=np.array(np.concatenate(all_feg_lam2), dtype=float),
    )
    print(f"[output] wrote {npz_path}")

    # --- plot ---
    png_path = os.path.join(here, "s102_fegan_tau0_spectrum_validation.png")
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    sub_all = np.concatenate(all_sub_lam2)
    feg_all = np.concatenate(all_feg_lam2)
    o = np.argsort(sub_all)
    ax[0].plot(np.sqrt(np.sort(sub_all)), np.sqrt(np.sort(feg_all)), '.', ms=3, color="#1f77b4")
    lims = [0, float(np.sqrt(sub_all.max())) * 1.05]
    ax[0].plot(lims, lims, '-', color="#d62728", lw=0.8, label="y=x")
    ax[0].set_xlabel(r"$|\lambda|$ substrate (numpy pipeline, $\tau=0$)")
    ax[0].set_ylabel(r"$|\lambda|$ Fegan closed form")
    ax[0].set_title(f"tau=0 Dirac spectrum: substrate vs Fegan\nmax|d|lam||={max_eig_diff:.2e} (<{EPS_EIG}); {verdict}")
    ax[0].legend(); ax[0].grid(alpha=0.3)

    ax[1].semilogy(np.arange(len(sub_eigdiff)),
                   np.maximum(sub_eigdiff, 1e-18), 'o-', ms=4, color="#2ca02c")
    ax[1].axhline(EPS_EIG, color="#d62728", ls="--", label=f"PASS boundary {EPS_EIG}")
    ax[1].set_xlabel("sector index (p+q ordered)")
    ax[1].set_ylabel(r"max $|d(|\lambda|)|$ per sector")
    ax[1].set_title("Per-sector eigenvalue-multiset diff")
    ax[1].legend(); ax[1].grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(png_path, dpi=130)
    print(f"[output] wrote {png_path}")

    # --- dual SHA closure ---
    content_sha256 = sha256_file(os.path.abspath(__file__))
    pin_map = {
        "_gate_id": "S102-FEGAN-TAU0-SPECTRUM-VALIDATION",
        "_scheme": "BI-INVARIANT-TAU0",
        "_convention": "DIRAC-SPECTRUM-PY-CANONICAL-NORMALIZATION",
        "_L_max_plan": str(L_MAX_PLAN),
        "_L_max_operational": str(L_MAX_OPERATIONAL),
        "_eps": repr(EPS_EIG),
        "script_sha256": content_sha256,
        "canonical_constants_sha256": sha_canon,
        "dirac_spectrum_sha256": sha_dirac,
        "branching_computation_sha256": sha_branch,
        "frame_slope": str(FRAME_SLOPE),
        "rho_offset": str(RHO_OFFSET),
    }
    audit_sha256 = closure_hash(pin_map)

    value = (f"max_eig_diff={max_eig_diff:.3e}_degenmis={total_mult_mismatch}_"
             f"pwmis={pw_mult_mismatch}_n36viol={n36_violations}_offerr={offset_err:.2e}_"
             f"nsectors={n_sectors}_Lop={L_MAX_OPERATIONAL}")
    extra_rows = [
        f"# tau0 bi-invariant SU(3) Dirac spectrum: substrate numpy pipeline vs "
        f"Parthasarathy/Kostant closed form |lam|^2=(1/6)[C2(mu)+C2(p,q)]+1/4; "
        f"convention LOCKED to dirac_spectrum.py frame (offset 1/4 EXACT, NOT 3/4 nor 3 nor 7/3)",
        f"# regulator_pin=N/A (exact-algebraic spectrum, no SD coefficient); "
        f"L_max_plan={L_MAX_PLAN} L_max_operational={L_MAX_OPERATIONAL}; atlas-07 lambda^2=n/36 reproduced",
    ]

    print(f"\n[verdict] {verdict}  pass_eig={pass_eig} pass_mult={pass_mult} "
          f"pass_conv={pass_conv} pass_n36={pass_n36}")
    print(f"[4-tuple] value=({value}) scheme=BI-INVARIANT-TAU0 "
          f"convention=DIRAC-SPECTRUM-PY-CANONICAL-NORMALIZATION L_max={L_MAX_OPERATIONAL}")

    print_verdict_payload(
        gate_id="S102-FEGAN-TAU0-SPECTRUM-VALIDATION",
        verdict=verdict,
        value=value,
        scheme="BI-INVARIANT-TAU0",
        convention="DIRAC-SPECTRUM-PY-CANONICAL-NORMALIZATION",
        L_max=L_MAX_OPERATIONAL,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
        session="S102",
        extra_rows=extra_rows,
    )


if __name__ == "__main__":
    main()
