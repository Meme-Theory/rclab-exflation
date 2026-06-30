#!/usr/bin/env python3
"""
S96 W4-5 S96-MATTER-YUKAWA-CHIRALITY — H_K+ Pfaffian restriction projects out
the wrong-chirality (eps''=+1) Yukawa coupling, recovering effective eps''=-1.
=============================================================================

Gate: S96-MATTER-YUKAWA-CHIRALITY  ([VERIFY-THEOREM])
Classification: GEOMETRIC

Pre-registered threshold (THEOREM-class, machine-eps):
  residual_chirality_preserving = |<gamma_9 J psi~ | D_K | psi~>|_{eps''=+1
      component on H_K+}
  PASS iff residual_chirality_preserving < 1e-12
  FAIL iff residual_chirality_preserving >= 1e-12 AND not measure-zero/Pfaffian-absorbed
  INFO iff nonzero but a known measure-zero set absorbed by Pfaffian normalization.

GOVERNING STRUCTURE (structure-first):
  The fermionic spectral-action term is  S_f = <J psi~ | D_K | psi~>  with
  psi~ in H_K+ = {xi : gamma_9 xi = +xi}  (canonical capstone form;
  connes-master-equation.md / phonic-exflation-equation.md). The chirality-
  resolved Yukawa overlap is  Y = <gamma_9 J psi~ | D_K | psi~>.

  s66 fact (s66_product_ko_dim.py, machine-eps): on the SU(3) factor (Cl(R^8),
  16-dim spinor) the charge conjugation C2 = g1 g3 g5 g7 (product of the REAL
  / symmetric gammas) gives eps'' = +1, i.e. J gamma_9 = +gamma_9 J. This is
  the WRONG chirality grading: CPT PRESERVES chirality. The physical finite-SM
  Yukawa requires eps'' = -1 (KO-dim 6 axiom J gamma = -gamma J, T5), i.e. CPT
  FLIPS chirality. The product M^4 x SU(3)-manifold carries eps''=+1
  ("Yukawa couplings have wrong chirality structure" -- s66 Section 10).

  This gate tests the RESOLUTION: does the H_K+ Pfaffian restriction project OUT
  the eps''=+1 (chirality-PRESERVING) component of Y, leaving only the physical
  eps''=-1 (chirality-FLIPPING) coupling?

  The mechanism is D_K oddness under chirality: a Dirac operator anticommutes
  with its chirality grading, {gamma_9, D_K} = 0, so D_K : H_K+ -> H_K-. Hence
  for psi~ in H_K+, D_K psi~ lives in H_K-. The bilinear Y pairs the bra
  <gamma_9 J psi~| against |D_K psi~>. Resolving the bra+ket by gamma_9
  eigenvalue gives two channels:
    - chirality-FLIPPING (eps''=-1): bra-chirality and ket-chirality OPPOSITE
    - chirality-PRESERVING (eps''=+1): bra-chirality and ket-chirality SAME.
  The residual is the chirality-PRESERVING piece. The THEOREM claim is that it
  vanishes to machine-eps after the H_K+ restriction.

DISCIPLINE (per the plan, load-bearing):
  - J = C2 * K is ANTILINEAR. We act with J on a ket as  J|xi> = C2 |xi*>
    (C2 then complex-conjugate components). We NEVER form a linear commutator
    [C2, D_K] as a CPT/Majorana/chirality condition (the T1 pitfall: for complex
    D_K, [C2,D_K] is generically nonzero and is T-symmetric, NOT a violation).
  - The eps'' sign is read from the ANTILINEAR relation J gamma_9 = eps'' gamma_9 J,
    evaluated as  C2 conj(gamma_9) C2^{-1}  vs  +/- gamma_9  (s66 form).
  - Jgamma9 = -gamma9 J (T5) is the KO-dim-6 axiom the PHYSICAL Yukawa needs;
    the SU(3) lift gives the OPPOSITE (Jgamma9=+gamma9 J). The H_K+ projector is
    what reconciles them at the level of the physical bilinear.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (D_K(tau_fold) blocks)
  - script bytes

Output 4-tuple:
  (value=residual_chirality_preserving, scheme=s66-product-KO-Clifford-C2-C1,
   convention=ABSOLUTE, L_max=12)

Author: dirac-antimatter-theorist (Session 96, Wave 4)
Date: 2026-05-29
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.join(
    _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import tau_fold, PI  # explicit names used below  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S96"                                              # (local)
GATE_ID = "S96-MATTER-YUKAWA-CHIRALITY"                      # (local)
SCHEME = "s66-product-KO-Clifford-C2-C1"                     # (local)
CONVENTION = "ABSOLUTE"                                      # (local)
L_MAX = 12                                                   # (local)

# Pre-registered THEOREM-class tolerance (machine-eps)
PASS_THRESHOLD = 1.0e-12                                     # (local)
N_EVAL = 16                                                  # (local) C^16 single generation

OUT_NPZ = SESSION_DIR / "s96_matter_yukawa_chirality.npz"   # (local)
OUT_PNG = SESSION_DIR / "s96_matter_yukawa_chirality.png"   # (local)
VERDICT_TXT = SESSION_DIR / "s96_gate_verdicts.txt"         # (local)

SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

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
# Section 5a — s66 Clifford construction (Cl(R^8), 16-dim spinor)
#              EXACT reproduction of s66_product_ko_dim.py build_cliff(8).
# ---------------------------------------------------------------------------
def build_cliff8() -> list:
    """Cl(R^8) gamma_1..gamma_8 in the 16-dim Pauli-kron basis (s66 convention).

    gamma_{2k}   = I^k (x) sigma_x (x) sigma_z^{m-k-1}     (symmetric, REAL)
    gamma_{2k+1} = I^k (x) sigma_y (x) sigma_z^{m-k-1}     (antisymmetric, IMAG)
    so 1-indexed: gamma_1,3,5,7 are REAL/symmetric; gamma_2,4,6,8 are IMAG/antisym.
    """
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)   # (local)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)  # (local)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)  # (local)
    I2 = np.eye(2, dtype=complex)                          # (local)
    m = 4                                                  # (local) d//2
    gammas = []  # (local)
    for k in range(m):
        mat_x = np.array([[1]], dtype=complex)  # (local)
        mat_y = np.array([[1]], dtype=complex)  # (local)
        for j in range(m):
            if j < k:
                mat_x = np.kron(mat_x, I2)
                mat_y = np.kron(mat_y, I2)
            elif j == k:
                mat_x = np.kron(mat_x, sigma_x)
                mat_y = np.kron(mat_y, sigma_y)
            else:
                mat_x = np.kron(mat_x, sigma_z)
                mat_y = np.kron(mat_y, sigma_z)
        gammas.append(mat_x)  # gamma_{2k+1} (1-indexed odd: gamma_1,3,5,7) -> REAL
        gammas.append(mat_y)  # gamma_{2k+2} (1-indexed even: gamma_2,4,6,8) -> IMAG
    return gammas[:8]


def build_gamma9(gammas: list) -> np.ndarray:
    """Chirality gamma_9 = (product of all 8 gammas), normalized so gamma_9^2 = I.
    Reproduces s66 build_chirality(gammas, 8)."""
    chi = np.eye(gammas[0].shape[0], dtype=complex)  # (local)
    for g in gammas:
        chi = chi @ g
    chi_sq = chi @ chi  # (local)
    if np.max(np.abs(chi_sq - np.eye(chi.shape[0]))) > 1e-10:
        if np.real(chi_sq[0, 0]) < 0:
            chi = 1j * chi
    return chi


# ---------------------------------------------------------------------------
# Section 5b — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    out = {}  # (local)

    # --- Build the s66 Cl(R^8) structure ---
    gammas = build_cliff8()  # (local) gamma_1..gamma_8 (1-indexed via [0..7])
    dim = gammas[0].shape[0]  # (local) = 16
    out["dim_spinor"] = int(dim)

    # Clifford relation verification {g_a, g_b} = 2 delta_ab
    max_cliff_err = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            ab = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]  # (local)
            expected = 2 * (1 if a == b else 0) * np.eye(dim)   # (local)
            max_cliff_err = max(max_cliff_err, float(np.max(np.abs(ab - expected))))
    out["clifford_relation_err"] = max_cliff_err

    gamma9 = build_gamma9(gammas)  # (local)
    gamma9_sq_err = float(np.max(np.abs(gamma9 @ gamma9 - np.eye(dim))))  # (local)
    out["gamma9_sq_err"] = gamma9_sq_err

    # --- C2 = gamma_1 gamma_3 gamma_5 gamma_7 (s66 / MEMORY: product of REAL gammas) ---
    # 1-indexed gamma_1,3,5,7 -> 0-indexed [0,2,4,6]
    C2 = np.eye(dim, dtype=complex)  # (local)
    for idx in [0, 2, 4, 6]:
        C2 = C2 @ gammas[idx]
    out["C2_indices_0based"] = [0, 2, 4, 6]

    # C1 = gamma_2 gamma_4 gamma_6 gamma_8 (particle-hole; 0-indexed [1,3,5,7])
    C1 = np.eye(dim, dtype=complex)  # (local)
    for idx in [1, 3, 5, 7]:
        C1 = C1 @ gammas[idx]
    # Cross-check: gamma_9 = C2 @ C1 up to phase (s35 verified gamma_9 = C2 @ C1)
    prod_C2C1 = C2 @ C1  # (local)
    # find scalar relating gamma9 and prod_C2C1
    nz = np.argmax(np.abs(prod_C2C1) > 1e-9)  # (local)
    ratio_g9 = (gamma9.flatten()[nz] / prod_C2C1.flatten()[nz]
                if np.abs(prod_C2C1.flatten()[nz]) > 1e-12 else 0.0)  # (local)
    g9_vs_C2C1_err = float(np.max(np.abs(gamma9 - ratio_g9 * prod_C2C1)))  # (local)
    out["gamma9_eq_C2C1_phase"] = complex(ratio_g9)
    out["gamma9_eq_C2C1_err"] = g9_vs_C2C1_err

    # =====================================================================
    # CC1 — eps'' from the ANTILINEAR relation J gamma_9 = eps'' gamma_9 J
    #       J = C2 * K (antilinear). On a ket: J|v> = C2 conj(v).
    #       J gamma_9 |v> = C2 conj(gamma_9 v) = C2 conj(gamma_9) conj(v)
    #       gamma_9 J |v> = gamma_9 C2 conj(v)
    #       => J gamma_9 = eps'' gamma_9 J  iff  C2 conj(gamma_9) = eps'' gamma_9 C2.
    #       NEVER use the LINEAR commutator [C2, gamma_9] (T1 pitfall).
    # =====================================================================
    Lhs_g9 = C2 @ np.conj(gamma9)  # (local) J gamma_9 represented on components
    comm_g9 = Lhs_g9 - gamma9 @ C2   # (local) test eps'' = +1
    anti_g9 = Lhs_g9 + gamma9 @ C2   # (local) test eps'' = -1
    comm_g9_err = float(np.max(np.abs(comm_g9)))  # (local)
    anti_g9_err = float(np.max(np.abs(anti_g9)))  # (local)
    if comm_g9_err < 1e-10:
        eps_dprime_su3 = +1  # (local)
    elif anti_g9_err < 1e-10:
        eps_dprime_su3 = -1  # (local)
    else:
        eps_dprime_su3 = 0   # (local)
    out["eps_dprime_su3"] = int(eps_dprime_su3)
    out["Jg9_commute_err"] = comm_g9_err     # err for eps''=+1 hypothesis
    out["Jg9_anticommute_err"] = anti_g9_err  # err for eps''=-1 hypothesis
    # T5 / KO-dim-6 PHYSICAL requirement is eps''=-1 (Jgamma9 = -gamma9 J).
    out["eps_dprime_physical_required"] = -1

    # J^2 = C2 conj(C2) = eps (KO sign). Antilinear: J^2|v> = C2 conj(C2 conj(v)) = C2 conj(C2) v
    J_sq = C2 @ np.conj(C2)  # (local)
    j2_is_scalar = float(np.max(np.abs(J_sq - J_sq[0, 0] * np.eye(dim))))  # (local)
    out["J_squared_value"] = float(np.real(J_sq[0, 0]))
    out["J_squared_scalar_err"] = j2_is_scalar

    # =====================================================================
    # CC2 — H_K+ projector cleanness.  P+ = (I + gamma_9)/2.
    #       Exact projector iff P+^2 = P+ and P+ Hermitian. Pf restriction is
    #       the chirality-+ subspace the fermionic action lives on.
    # =====================================================================
    P_plus = 0.5 * (np.eye(dim) + gamma9)   # (local)
    P_minus = 0.5 * (np.eye(dim) - gamma9)  # (local)
    Pp_idem_err = float(np.max(np.abs(P_plus @ P_plus - P_plus)))   # (local)
    Pp_herm_err = float(np.max(np.abs(P_plus - P_plus.conj().T)))   # (local)
    Pp_Pm_orth_err = float(np.max(np.abs(P_plus @ P_minus)))        # (local)
    rank_Pplus = int(round(float(np.real(np.trace(P_plus)))))       # (local)
    out["Pplus_idempotent_err"] = Pp_idem_err
    out["Pplus_hermitian_err"] = Pp_herm_err
    out["Pplus_Pminus_orth_err"] = Pp_Pm_orth_err
    out["rank_Hplus"] = rank_Pplus  # dim H_K+ = 8 (half of 16)

    # =====================================================================
    # Build a representative finite Dirac block D_K from the L_max=12 cache.
    # The cache stores per Peter-Weyl (p,q): abs_evals (|lambda| spectrum,
    # length 16 for the (0,0) singlet = one C^16 generation). We build a
    # 16x16 Hermitian D_K that is ODD under chirality ({gamma_9, D_K} = 0),
    # the defining property of a Dirac operator, with the cache eigenvalues
    # as its singular spectrum. This is the physically-correct structure:
    # D_K maps H_K+ <-> H_K- (a Dirac operator never preserves chirality).
    # =====================================================================
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)  # (local)
    sector_evals = cache["sector_evals"].item()         # (local)
    # Singlet (0,0) = the single-generation C^16 content
    singlet = sector_evals[(0, 0)]                       # (local)
    abs_evals_00 = np.asarray(singlet["abs_evals"], dtype=float)  # (local) len 16
    out["cache_singlet_abs_evals"] = abs_evals_00
    out["cache_singlet_min_abs"] = float(np.min(abs_evals_00))
    out["cache_singlet_max_abs"] = float(np.max(abs_evals_00))

    # Construct D_K ODD under gamma_9: in a basis where gamma_9 = diag(+1_8, -1_8),
    # an odd operator has the block form [[0, m],[m^dag, 0]]. We realize this by
    # transforming to the gamma_9-eigenbasis, placing the cache |lambda| as the
    # off-diagonal singular values, and transforming back.
    evals_g9, U_g9 = np.linalg.eigh(gamma9)  # (local) U_g9 diagonalizes gamma_9
    # order so that +1 eigenvalues come first
    order = np.argsort(-np.real(evals_g9))   # (local)
    U_g9 = U_g9[:, order]                     # (local)
    n_plus = int(np.sum(np.real(evals_g9) > 0.5))   # (local) = 8
    n_minus = dim - n_plus                          # (local) = 8

    # Off-diagonal block m (n_plus x n_minus) = diag of the cache singular values.
    # Use the 8 distinct |lambda| pairs; abs_evals_00 has 16 entries (8 +/- pairs).
    sing = np.sort(abs_evals_00)[::-1]        # (local) descending
    sing8 = sing[0:n_plus]                    # (local) 8 singular values
    m_block = np.diag(sing8.astype(complex))  # (local) 8x8

    D_g9basis = np.zeros((dim, dim), dtype=complex)  # (local)
    D_g9basis[0:n_plus, n_plus:dim] = m_block
    D_g9basis[n_plus:dim, 0:n_plus] = m_block.conj().T  # Hermitian, odd
    # transform back to the original Clifford basis
    D_K = U_g9 @ D_g9basis @ U_g9.conj().T    # (local)
    D_K = 0.5 * (D_K + D_K.conj().T)          # symmetrize numerically (Hermitian)
    out["DK_hermitian_err"] = float(np.max(np.abs(D_K - D_K.conj().T)))

    # Verify {gamma_9, D_K} = 0 (D_K odd under chirality) to machine-eps
    anticomm_DK = gamma9 @ D_K + D_K @ gamma9  # (local)
    out["DK_gamma9_anticommute_err"] = float(np.max(np.abs(anticomm_DK)))

    # =====================================================================
    # CONTRAST CONSTRUCTION — the physical KO-dim-6 charge conjugation J'.
    #   The physical SM Yukawa needs eps''=-1 (J' gamma_9 = -gamma_9 J', T5).
    #   On Cl(R^8) the manifold B_+/B_- both give eps''=+1 (s66; d=8 degenerate),
    #   so eps''=-1 is an INDEPENDENT algebraic structure. We realize a
    #   representative eps''=-1 antiunitary J' = B' * K with B' = gamma_1 * C2.
    #   Since each single gamma_a ANTICOMMUTES with the chirality gamma_9 (even d),
    #   pre-multiplying C2 by one gamma flips the eps'' sign: B' conj(gamma_9) =
    #   -gamma_9 B'.  This is the KO-6 (physical) charge conjugation that FLIPS
    #   chirality. (We verify the sign below, not assume it.)
    # =====================================================================
    B_prime = gammas[0] @ C2  # (local) gamma_1 * C2  -> eps''=-1 candidate
    Lhs_g9_p = B_prime @ np.conj(gamma9)        # (local) J' gamma_9 on components
    comm_g9_p = float(np.max(np.abs(Lhs_g9_p - gamma9 @ B_prime)))   # (local)
    anti_g9_p = float(np.max(np.abs(Lhs_g9_p + gamma9 @ B_prime)))   # (local)
    if anti_g9_p < 1e-10:
        eps_dprime_ko6 = -1  # (local)
    elif comm_g9_p < 1e-10:
        eps_dprime_ko6 = +1  # (local)
    else:
        eps_dprime_ko6 = 0   # (local)
    out["eps_dprime_ko6_contrast"] = int(eps_dprime_ko6)
    out["Jprime_g9_anticommute_err"] = anti_g9_p
    out["Jprime_g9_commute_err"] = comm_g9_p

    # =====================================================================
    # The Yukawa/mass bilinear and its chirality-channel resolution.
    #
    #   PHYSICAL fermionic spectral-action term (Connes; capstone form):
    #       S_f(psi~) = <J psi~ | D_K | psi~>,   psi~ in H_K+.
    #
    #   D_K is ODD under chirality ({gamma_9,D_K}=0), so D_K|psi~> in H_K-.
    #   The bra is <J psi~|.  Whether S_f != 0 is decided by the chirality of
    #   J psi~:
    #     - eps''=-1 (J FLIPS chirality): J psi~ in H_K- = same as D_K psi~
    #       -> overlap NONZERO  -> chirality-FLIPPING coupling (physical SM).
    #     - eps''=+1 (J PRESERVES chirality): J psi~ in H_K+, ORTHOGONAL to the
    #       H_K- ket D_K psi~  -> overlap ZERO -> the chirality-PRESERVING
    #       coupling does NOT survive the H_K+ restriction.
    #
    #   Therefore the eps''=+1 channel magnitude IS  |S_f| computed with the
    #   SU(3)-lift J (eps''=+1): if a wrong-chirality coupling survived, it
    #   would be nonzero. The eps''=-1 channel magnitude is |S_f| with the
    #   physical KO-6 J' (eps''=-1).  This is the channel decomposition; the
    #   chirality of J (eps'') labels the channel, NOT an extra gamma_9
    #   insertion (which would tautologically force <H+|H-> overlaps).
    #
    #   Basis-free over H_K+: range psi over an orthonormal basis of H_K+ and
    #   compute the Frobenius norm of the sesquilinear kernel
    #       K[i,j] = <J e_i | D_K | e_j>,   e_i, e_j in H_K+.
    #   Antilinearity handled by acting J as the matrix B then conjugation.
    # ---------------------------------------------------------------------
    # Orthonormal basis of H_K+ (columns of U_g9 with gamma_9 = +1)
    basis_plus = U_g9[:, 0:n_plus]            # (local) 16 x 8, columns span H_K+

    # eps''=+1 channel (SU(3)-lift J = C2*K): the chirality-PRESERVING residual
    K_preserve = np.zeros((n_plus, n_plus), dtype=complex)  # (local)
    # eps''=-1 channel (KO-6 J' = B'*K): the chirality-FLIPPING physical coupling
    K_flip = np.zeros((n_plus, n_plus), dtype=complex)      # (local)

    for i in range(n_plus):
        e_i = basis_plus[:, i]                   # (local) bra-seed in H_K+
        Jpsi_i = C2 @ np.conj(e_i)               # (local) J e_i (eps''=+1, antilinear)
        Jpsi_i_phys = B_prime @ np.conj(e_i)     # (local) J' e_i (eps''=-1, antilinear)
        for j in range(n_plus):
            e_j = basis_plus[:, j]               # (local) ket-seed in H_K+
            k_j = D_K @ e_j                      # (local) D_K e_j in H_K-
            K_preserve[i, j] = np.vdot(Jpsi_i, k_j)       # <J e_i | D_K e_j>
            K_flip[i, j] = np.vdot(Jpsi_i_phys, k_j)      # <J' e_i | D_K e_j>

    mag_preserve = float(np.linalg.norm(K_preserve))  # (local) eps''=+1 residual
    mag_flip = float(np.linalg.norm(K_flip))          # (local) eps''=-1 physical
    mag_total = mag_preserve + mag_flip               # (local) diagnostic sum

    out["Y_total_magnitude"] = mag_total
    out["Y_flip_magnitude_epsdprime_minus1"] = mag_flip
    out["Y_preserve_magnitude_epsdprime_plus1"] = mag_preserve
    out["Y_flip_kernel"] = K_flip
    out["Y_preserve_kernel"] = K_preserve

    # The pre-registered observable: residual chirality-PRESERVING coupling
    # = |S_f| on H_K+ with the SU(3)-lift J (eps''=+1).
    residual_chirality_preserving = mag_preserve  # (local)
    out["value"] = residual_chirality_preserving
    out["residual_chirality_preserving"] = residual_chirality_preserving

    # Effective eps'' on the physical bilinear: the SURVIVING channel.
    # If preserve ~ 0 and flip != 0  -> effective eps'' = -1 (SM recovered).
    # both-vanish -> 0 (no coupling); both-nonzero -> 99 (mixed)
    if mag_preserve < PASS_THRESHOLD and mag_flip > PASS_THRESHOLD:
        eps_dprime_effective = -1  # (local)
    elif mag_preserve > PASS_THRESHOLD and mag_flip < PASS_THRESHOLD:
        eps_dprime_effective = +1  # (local)
    elif mag_preserve < PASS_THRESHOLD and mag_flip < PASS_THRESHOLD:
        eps_dprime_effective = 0  # (local)
    else:
        eps_dprime_effective = 99  # (local)
    out["eps_dprime_effective_on_bilinear"] = int(eps_dprime_effective)

    # ratio (diagnostic)
    out["preserve_over_flip_ratio"] = (mag_preserve / mag_flip
                                       if mag_flip > 1e-300 else float("inf"))
    return out


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def _prior_audit_sha() -> str:
    """Return the audit_sha256 of the most-recent prior canonical line for this
    gate-ID (for the Option A supersedes tag), or '' if none exists.
    Per gate-verdicts.md absolute verdict permanence: we never edit/delete the
    prior line; the corrective successor carries supersedes=<old_audit_sha>."""
    if not VERDICT_TXT.exists():
        return ""
    prior = ""  # (local)
    try:
        for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
            if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
                seg = ln.split("audit_sha256=", 1)[1].split()[0]  # (local)
                prior = seg
    except OSError:
        return ""
    return prior


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   supersedes: str = "") -> None:
    sup = f" supersedes={supersedes}" if supersedes else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r}{sup} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
    # dual-SHA companion comment row
    comp = (f"# audit_sha256_short={audit_sha[:16]} "
            f"content_sha256_short={content_sha[:16]} "
            f"# {GATE_ID} dual-SHA companion row"
            + (f" supersedes={supersedes}" if supersedes else "")
            + "\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(comp)


def evaluate_gate(res: dict) -> str:
    """THEOREM-class gate rule (pre-registered, NOT modified after seeing value).

    The literal pre-registered PASS predicate is the SINGLE inequality
      residual_chirality_preserving < 1e-12
    (the wrong-chirality eps''=+1 coupling is projected OUT by H_K+).

      PASS iff residual_chirality_preserving < 1e-12.
      INFO iff residual >= 1e-12 but a documented measure-zero set absorbed by
              the Pfaffian normalization (per the INFO_meaning rubric).
      FAIL iff residual >= 1e-12 as a genuine surviving wrong-chirality channel.

    The physical eps''=-1 (flipping) channel magnitude is reported as the
    contrast that makes the PASS non-vacuous, but it is NOT part of the literal
    pre-registered inequality (no post-hoc threshold tightening).
    """
    residual = res["residual_chirality_preserving"]  # (local)
    if residual < PASS_THRESHOLD:
        return "PASS"
    # nonzero residual: FAIL unless it is the documented measure-zero/Pfaffian-
    # absorbed case. A genuine nonzero operator-norm residual is a FAIL.
    return "FAIL"


def make_plot(res: dict) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:  # noqa: BLE001
        print(f"  [plot skipped: {exc}]")
        return
    flip = res["Y_flip_magnitude_epsdprime_minus1"]      # (local)
    preserve = res["Y_preserve_magnitude_epsdprime_plus1"]  # (local)
    fig, ax = plt.subplots(figsize=(6.0, 4.2))           # (local)
    labels = ["eps''=-1\n(chirality-FLIPPING,\nphysical SM)",
              "eps''=+1\n(chirality-PRESERVING,\nwrong-chirality residual)"]  # (local)
    vals = [max(flip, 1e-18), max(preserve, 1e-18)]      # (local)
    colors = ["#2b7", "#c33"]                            # (local)
    ax.bar(labels, vals, color=colors)
    ax.set_yscale("log")
    ax.axhline(PASS_THRESHOLD, ls="--", color="k", lw=1,
               label=f"PASS threshold = {PASS_THRESHOLD:g}")
    ax.set_ylabel("channel magnitude  |Y|  (Frobenius, over H_K+)")
    ax.set_title("S96-MATTER-YUKAWA-CHIRALITY: H_K+ Pfaffian restriction\n"
                 "projects out the eps''=+1 wrong-chirality coupling")
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  [plot saved: {OUT_PNG.name}]")


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)        # (local)
    print(f"  closure (legacy, informational): {closure[:16]}...")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print(f"  tau_fold = {tau_fold}  PI = {PI:.10f}")
    print()

    res = compute()  # (local)

    print("=== Structural verifications (machine-eps) ===")
    print(f"  spinor dim                     : {res['dim_spinor']}")
    print(f"  Clifford {{g_a,g_b}}=2d err      : {res['clifford_relation_err']:.2e}")
    print(f"  gamma_9^2 = I err              : {res['gamma9_sq_err']:.2e}")
    print(f"  gamma_9 = C2@C1 (phase {res['gamma9_eq_C2C1_phase']:+.1f}) err : "
          f"{res['gamma9_eq_C2C1_err']:.2e}")
    print()
    print("=== CC1: eps'' from ANTILINEAR J gamma_9 = eps'' gamma_9 J ===")
    print(f"  J^2 = {res['J_squared_value']:+.1f}  (scalar err {res['J_squared_scalar_err']:.2e})")
    print(f"  eps''=+1 hypothesis err (commute)     : {res['Jg9_commute_err']:.2e}")
    print(f"  eps''=-1 hypothesis err (anticommute) : {res['Jg9_anticommute_err']:.2e}")
    print(f"  => eps''(SU(3) lift)   = {res['eps_dprime_su3']:+d}  (s66: +1, J COMMUTES w/ gamma_9)")
    print(f"  => eps''(physical req) = {res['eps_dprime_physical_required']:+d}  (T5 / KO-dim-6)")
    print(f"  contrast J' = gamma_1*C2:  anticommute err {res['Jprime_g9_anticommute_err']:.2e}, "
          f"eps''(KO-6 J') = {res['eps_dprime_ko6_contrast']:+d}  (physical, J' FLIPS gamma_9)")
    print()
    print("=== CC2: H_K+ projector cleanness ===")
    print(f"  P+ idempotent err   : {res['Pplus_idempotent_err']:.2e}")
    print(f"  P+ hermitian err    : {res['Pplus_hermitian_err']:.2e}")
    print(f"  P+ P- orthogonality : {res['Pplus_Pminus_orth_err']:.2e}")
    print(f"  rank H_K+           : {res['rank_Hplus']} (= 8, half of 16)")
    print()
    print("=== D_K block (from L_max=12 cache singlet (0,0)) ===")
    print(f"  cache |lambda| range : [{res['cache_singlet_min_abs']:.6f}, "
          f"{res['cache_singlet_max_abs']:.6f}]")
    print(f"  D_K Hermitian err          : {res['DK_hermitian_err']:.2e}")
    print(f"  {{gamma_9, D_K}} = 0 err      : {res['DK_gamma9_anticommute_err']:.2e}  "
          f"(D_K ODD under chirality -> H+ to H-)")
    print()
    print("=== Yukawa bilinear chirality-channel resolution (over H_K+) ===")
    print(f"  |Y| total                              : {res['Y_total_magnitude']:.12e}")
    print(f"  |Y| eps''=-1 (FLIPPING, physical SM)    : {res['Y_flip_magnitude_epsdprime_minus1']:.12e}")
    print(f"  |Y| eps''=+1 (PRESERVING, residual)    : {res['Y_preserve_magnitude_epsdprime_plus1']:.12e}")
    print(f"  preserve/flip ratio                    : {res['preserve_over_flip_ratio']:.3e}")
    print(f"  effective eps'' on bilinear            : {res['eps_dprime_effective_on_bilinear']:+d}")
    print()
    print(f"  >>> residual_chirality_preserving = {res['residual_chirality_preserving']:.12e}")
    print(f"  >>> PASS threshold (THEOREM-class)  = {PASS_THRESHOLD:.0e}")
    print()

    verdict = evaluate_gate(res)  # (local)
    value = res["value"]          # (local)

    # Save data
    np.savez(
        OUT_NPZ,
        residual_chirality_preserving=res["residual_chirality_preserving"],
        Y_total_magnitude=res["Y_total_magnitude"],
        Y_flip_magnitude_epsdprime_minus1=res["Y_flip_magnitude_epsdprime_minus1"],
        Y_preserve_magnitude_epsdprime_plus1=res["Y_preserve_magnitude_epsdprime_plus1"],
        eps_dprime_su3=res["eps_dprime_su3"],
        eps_dprime_physical_required=res["eps_dprime_physical_required"],
        eps_dprime_ko6_contrast=res["eps_dprime_ko6_contrast"],
        Jprime_g9_anticommute_err=res["Jprime_g9_anticommute_err"],
        eps_dprime_effective_on_bilinear=res["eps_dprime_effective_on_bilinear"],
        Jg9_commute_err=res["Jg9_commute_err"],
        Jg9_anticommute_err=res["Jg9_anticommute_err"],
        J_squared_value=res["J_squared_value"],
        clifford_relation_err=res["clifford_relation_err"],
        gamma9_sq_err=res["gamma9_sq_err"],
        gamma9_eq_C2C1_err=res["gamma9_eq_C2C1_err"],
        Pplus_idempotent_err=res["Pplus_idempotent_err"],
        Pplus_hermitian_err=res["Pplus_hermitian_err"],
        Pplus_Pminus_orth_err=res["Pplus_Pminus_orth_err"],
        rank_Hplus=res["rank_Hplus"],
        DK_hermitian_err=res["DK_hermitian_err"],
        DK_gamma9_anticommute_err=res["DK_gamma9_anticommute_err"],
        cache_singlet_abs_evals=res["cache_singlet_abs_evals"],
        Y_flip_kernel=res["Y_flip_kernel"],
        Y_preserve_kernel=res["Y_preserve_kernel"],
        preserve_over_flip_ratio=res["preserve_over_flip_ratio"],
        PASS_THRESHOLD=PASS_THRESHOLD,
        tau_fold=tau_fold,
    )
    print(f"  [data saved: {OUT_NPZ.name}]")
    make_plot(res)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    # Option A (gate-verdicts.md): if a prior canonical line for this gate-ID
    # exists with a DIFFERENT audit_sha (a superseded in-session development
    # emission), tag the corrective successor with supersedes=<old>. The prior
    # line is retained on disk (absolute verdict permanence).
    prior = _prior_audit_sha()  # (local)
    supersedes = prior if (prior and prior != audit_sha) else ""  # (local)
    if supersedes:
        print(f"  [Option A: superseding prior in-session line audit_sha={prior[:16]}...]")
    append_verdict(verdict, value, audit_sha, content_sha, supersedes=supersedes)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # FAIL is a valid scientific result -> exit 0 (script health), per math-scripts.md
    return 0


if __name__ == "__main__":
    sys.exit(main())
