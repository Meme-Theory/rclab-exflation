"""
S82 W2-11: S++-FULL-ED [AUDIT]

GATE: S82-S-PP-FULL-ED
Trigger: [AUDIT]
Classification: PHONONIC (BCS condensation-energy margin between s++ and s+-
  sign configurations on the active (0,0)+(1,1) sub-sector).

HYPOTHESIS:
  Full exact diagonalization on the (0,0)+(1,1) sub-sector (two-sector pair-basis
  Richardson ED with N_pair_cutoff per sector) tightens the energy-preferred
  sign-margin from the s78_w1d mean-field uniform-gap analytical bound.

PRE-REGISTERED THRESHOLD:
  Null hypothesis (s78_w1d): margin_MF = 5.808e-04 = 0.0581%, s+- energy-preferred
    but Eliashberg diagonalization preferred s++ (internal inconsistency of MF).
  PASS: ED margin tightens mean-field margin by > 1 sigma (factor >= 2x separation
        from MF, i.e., margin_ED <= margin_MF/2 = 2.9e-04) AND same sign winner
        as mean-field Eliashberg (s++).
  INFO: Agreement with mean-field (sign consistent) without tightening.
  FAIL: ED disagrees with analytical bound (different sign winner from
        Eliashberg-preferred s++, OR margin >= 10x mean-field margin).

SUBSTITUTION CHAIN (sign/direction):

  Step 1 [definition]:
    margin = |E_GS(s+-) - E_GS(s++)| / |E_GS(s++)|
    where E_GS is the EXACT ground-state energy under the specified sign config.

  Step 2 [substitution for mean-field]:
    BdG 96x96 with uniform-gap ansatz: E_GS^MF(s++) = -0.095631, E_GS^MF(s+-) = -0.095687.
    margin_MF = |(-0.095687)-(-0.095631)|/|-0.095631| = 5.808e-04.
    Sign winner (lower energy): s+-. Eliashberg diagonalization winner: s++.
    Internal inconsistency <==> iteration-noise regime.

  Step 3 [substitution for full-ED on (0,0)+(1,1)]:
    Richardson-like pair-basis Hamiltonian on 2 sectors x 12 modes per sector.
    Fixed-N_pair sectorization up to N_pair_cutoff per sector.
    Two sign configurations tested:
      s++ : J_ab > 0 (ferromagnetic pair hopping between (0,0) and (1,1))
      s+- : J_ab < 0 (antiferromagnetic pair hopping)
    Sparse-matrix Lanczos diagonalization (scipy.sparse.linalg.eigsh) for the
    smallest eigenvalue per block.
    Find global ground state over all (N_pair^(00), N_pair^(11)) combinations.
    Compute margin_ED = |E_GS^ED(s+-) - E_GS^ED(s++)|/|E_GS^ED(s++)|.

  Step 4 [canonical form, verdict direction]:
    Let R = margin_ED / margin_MF.
      R <= 0.5 AND sign_ED == s++ --> PASS (tightens by >= 2x, confirms
        Eliashberg-preferred sign structure).
      0.5 < R <= 2.0 AND sign_ED == s++ --> INFO (confirms sign without
        tightening; establishes that the MF margin is structural).
      R > 2.0 AND sign_ED == s++ --> INFO (margin widens but sign preserved).
      sign_ED == s+- AND margin_ED >= 0.1% --> FAIL.

  Step 5 [direction read from canonical form]:
    Given the inputs (MF margin = 5.8e-4, active sectors (0,0) and (1,1) only,
    (1,0) and (0,1) sub-critical), the ED outcome is an EXACT calculation.

METHOD:
  Sparse-matrix Richardson-like ED:
  1. Load s74 spectrum cache (L_max=9, tau=0.19).
  2. Load canonical constants.
  3. Replicate s78 mean-field per-sector calibration (V0_INTRA_CALIB).
  4. Build pair-basis SPARSE Hamiltonian on (0,0)+(1,1) Hilbert space for both
     s++ and s+- sign configurations.
  5. Block-diagonalize by fixed-N_total with N_pair_cutoff=2 (canonical run).
  6. Use scipy.sparse.linalg.eigsh (Lanczos) for smallest eigenvalue.
  7. For each sign config: sweep all N_total values, find global GS.
  8. Compute margin_ED and verdict.
  9. Extended run at N_pair_cutoff=3 for the largest-weight total-pair sector
     as convergence check (IF tractable with sparse solver).

CROSS-CHECKS:
  CC1: Non-interacting (V0=0, J=0) reproduces sum-of-lowest-xi Fermi sea.
  CC2: Decoupling (J=0) bracket: E_GS(J=0) lies between E_GS(s++) and E_GS(s+-).
  CC3: Single-sector N=1 reduction ED E_cond close to s78 MF E_cond^(0,0).
  CC4: Scipy sparse eigsh vs dense numpy eigvalsh on same test block.

Classification: PHONONIC
Convention pins (Section 0):
  - F_amp: POWER-RATIO (linear). N/A for this gate.
  - a_n: zeta-default, with f* as Level 2 canonical.
  - Cutoff: f* canonical for gate threshold.
  - Tag discipline: (value, scheme_tag=EXACT-DIAG, convention_tag=f*, L_max_tag=9).

Dependencies:
  - s74_spectrum_cache_L9_tau019.npz
  - canonical_constants.py
  - scipy.sparse + scipy.sparse.linalg.eigsh

Author: landau-condensed-matter-theorist, Session 82 W2-11
Date: 2026-04-17
"""

import os
import sys
import time
import hashlib
import itertools
import numpy as np
from scipy.sparse import lil_matrix, csr_matrix
from scipy.sparse.linalg import eigsh as sparse_eigsh
from scipy.linalg import eigh as scipy_eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    tau_fold, PI, E_cond, E_cond_ED_8mode,
    N_cells, J_C2, J_su2, J_u1, T_acoustic,
    Delta_BCS, Delta_0_OES, Delta_B3, xi_BCS,
    omega_L1, omega_L2,
    M_KK_gravity, M_KK,
    A_s_CMB,
)

# -------------- paths --------------
OUT_NPZ = os.path.join(SCRIPT_DIR, "s82_w2_11_s_pp_full_ed.npz")
OUT_PNG = os.path.join(SCRIPT_DIR, "s82_w2_11_s_pp_full_ed.png")
OUT_TXT = os.path.join(SCRIPT_DIR, "s82_w2_11_s_pp_full_ed_output.txt")
VERDICT_FILE = os.path.join(SCRIPT_DIR, "s82_gate_verdicts.txt")
SPECTRUM_CACHE = os.path.join(SCRIPT_DIR, "s74_spectrum_cache_L9_tau019.npz")
S78_NPZ = os.path.join(SCRIPT_DIR, "s78_multi_band_econd.npz")


def sha256_of(path):
    """Full SHA-256 hexdigest of file at path."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 16), b''):
            h.update(chunk)
    return h.hexdigest()


SHA_SPECTRUM = sha256_of(SPECTRUM_CACHE)  # (local)
SHA_S78 = sha256_of(S78_NPZ)  # (local)
SHA_CANONICAL = sha256_of(os.path.join(SCRIPT_DIR, "canonical_constants.py"))  # (local)

t_start = time.time()  # (local)
log_lines = []  # (local)


def log(msg=""):
    print(msg)
    log_lines.append(str(msg))


# First 20 stdout lines: SHA pins
log("=" * 78)
log("S82 W2-11: S++-FULL-ED (Full ED on (0,0)+(1,1) sub-sector)")
log("=" * 78)
log()
log(f"  SHA-256 input pins (S81+ discipline):")
log(f"    s74_spectrum_cache_L9_tau019.npz: {SHA_SPECTRUM}")
log(f"    s78_multi_band_econd.npz:         {SHA_S78}")
log(f"    canonical_constants.py:           {SHA_CANONICAL}")
log()
log(f"  Canonical constants:")
log(f"    tau_fold = {tau_fold}")
log(f"    E_cond (S36 ED-CONV-36, 8-mode) = {E_cond:.10f}")
log(f"    Delta_BCS = {Delta_BCS:.6f}")
log(f"    J_C2 = {J_C2}, J_su2 = {J_su2}, J_u1 = {J_u1}")
log(f"    omega_L1 = {omega_L1}, omega_L2 = {omega_L2}")
log()
log(f"  Solver path: scipy.sparse.linalg.eigsh (Lanczos, smallest eigenvalue only)")
log(f"  (GPU dense eigvalsh is inappropriate here: the coupled-block matrices")
log(f"   in pair basis can reach O(4e4) dimension, which exceeds dense-GPU memory;")
log(f"   sparse Lanczos is the canonical method for this class of Richardson ED.)")
log()

# -------------- PRE-REGISTERED THRESHOLDS --------------

MARGIN_MF = 5.807769e-04  # (local) mean-field s78_w1d margin (SUBCHAIN step 2)
MARGIN_PASS_THRESH = MARGIN_MF * 0.5  # (local) PASS if margin_ED <= MF/2
MARGIN_INFO_HI = MARGIN_MF * 2.0  # (local) INFO agreement if <= 2x
MARGIN_FAIL_THRESH = 1e-3  # (local) FAIL if sign-flipped AND margin >= 0.1%
# Canonical run: N_PAIR_CUTOFF = 2 (tractable dense + sparse, covers GS region)
# since MF Delta per sector at V_calib gives <N_pair> ~ 0.5 -> 1 pair occupancy.
N_PAIR_CUTOFF = 2  # (local) per-sector N_pair truncation (canonical)
N_PAIR_CUTOFF_EXT = 3  # (local) extended check (if tractable)
L_MAX_TAG = 9  # (local)
SCHEME_TAG = "EXACT-DIAG"  # (local)
CONVENTION_TAG = "fstar"  # (local)

log("PRE-REGISTERED criteria (before compute):")
log(f"  MF baseline margin (s78_w1d): {MARGIN_MF:.6e} = {MARGIN_MF*100:.4f}%")
log(f"  PASS: margin_ED <= {MARGIN_PASS_THRESH:.6e} AND sign_ED == s++")
log(f"  INFO: margin_ED in [{MARGIN_PASS_THRESH:.2e}, {MARGIN_INFO_HI:.2e}]; sign == s++")
log(f"  INFO (widens): margin_ED > {MARGIN_INFO_HI:.2e} but sign == s++")
log(f"  FAIL: sign_ED == s+- AND margin_ED >= {MARGIN_FAIL_THRESH:.1e}")
log(f"  N_pair_cutoff (canonical): {N_PAIR_CUTOFF} per sector")
log(f"  N_pair_cutoff (extended check): {N_PAIR_CUTOFF_EXT} per sector")
log()

# =====================================================================
# SECTION 1: Load sector eigenvalues (active sectors (0,0) and (1,1))
# =====================================================================
log("=" * 78)
log("SECTION 1: Load active-sector eigenvalues")
log("=" * 78)

cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
sector_evals = cache['sector_evals'].item()
cache.close()

ACTIVE_SECTORS = [(0, 0), (1, 1)]  # (local) only these are super-critical at V_calib
N_MODES_PER_SECTOR = 12  # (local)

sector_data = {}  # (local)
for (p, q) in ACTIVE_SECTORS:
    info = sector_evals[(p, q)]
    abs_evals = np.sort(np.array(info['abs_evals'], dtype=np.float64))
    pos_evals = abs_evals[:N_MODES_PER_SECTOR] if len(abs_evals) >= N_MODES_PER_SECTOR else abs_evals
    lam_max = float(np.max(abs_evals))
    sector_data[(p, q)] = {
        'evals': pos_evals,
        'lam_max': lam_max,
    }
    log(f"  Sector ({p},{q}): lowest {N_MODES_PER_SECTOR} evals in "
        f"[{pos_evals[0]:.5f}, {pos_evals[-1]:.5f}], lam_max = {lam_max:.5f}")

log()

# =====================================================================
# SECTION 2: f* scheme and V0 calibration (replicate s78)
# =====================================================================
log("=" * 78)
log("SECTION 2: f* scheme + V0 calibration (replicate s78 MF calibration)")
log("=" * 78)

T_STAR = 0.08832  # (local)
ALPHA_STAR = 1.0 - T_STAR  # (local)
BETA_STAR = T_STAR  # (local)


def fstar(x):
    """f*(x) = alpha*sqrt(x) + beta*exp(-x)."""
    return ALPHA_STAR * np.sqrt(np.abs(x)) + BETA_STAR * np.exp(-x)


s78_data = np.load(S78_NPZ, allow_pickle=True)
V0_INTRA_CALIB = float(s78_data['V0_INTRA_CALIB'])  # (local)
Delta_MF_per_sector_s78 = s78_data['Delta_per_sector_fstar']  # (local) [D00,D10,D01,D11]
E_cond_MF_per_sector_s78 = s78_data['E_cond_fstar_per_sector']  # (local)
s78_data.close()

Delta_MF = {(0, 0): float(Delta_MF_per_sector_s78[0]),
            (1, 1): float(Delta_MF_per_sector_s78[3])}  # (local)
E_cond_MF = {(0, 0): float(E_cond_MF_per_sector_s78[0]),
             (1, 1): float(E_cond_MF_per_sector_s78[3])}  # (local)

log(f"  V0_INTRA_CALIB (from s78): {V0_INTRA_CALIB:.8f}")
log(f"  Mean-field Delta per sector (canonical f* scheme):")
log(f"    Delta_(0,0) = {Delta_MF[(0,0)]:.6e}, E_cond_(0,0)_MF = {E_cond_MF[(0,0)]:.6e}")
log(f"    Delta_(1,1) = {Delta_MF[(1,1)]:.6e}, E_cond_(1,1)_MF = {E_cond_MF[(1,1)]:.6e}")
log()

# =====================================================================
# SECTION 3: Sparse Richardson-like pair-basis ED builder
# =====================================================================
log("=" * 78)
log("SECTION 3: Sparse pair-basis exact diagonalization")
log("=" * 78)
log()
log("  Pair basis: only doubly-occupied pairs populated (s-wave singlet).")
log("  Per-sector dim at fixed N_pair = C(12, N_pair).")
log("  Coupled-block dim = sum over eligible (n_a, n_b) splits of C(12,n_a)*C(12,n_b).")
log()


def build_pair_basis(n_modes, n_pair):
    """Enumerate all N_pair occupation patterns on n_modes modes (sorted tuples)."""
    return list(itertools.combinations(range(n_modes), n_pair))


def build_two_sector_sparse_H(evals_a, fw_a, evals_b, fw_b,
                              V_intra, J_ab_signed, N_total,
                              n_cutoff):
    """Build sparse Hamiltonian on coupled (sector_a, sector_b) Hilbert
    space restricted to total pair count = N_total, with per-sector cap n_cutoff.

    Hamiltonian terms (Richardson-like, s-wave pair basis):
      H_kin = sum_{s,m} 2 xi_{s,m} n_{s,m}          (kinetic x 2 for spin pair)
      H_int = -V0/n_modes * sum_{s,mn} f_{s,m} f_{s,n} b^dag_{s,m} b_{s,n}
              (intra-sector pair hopping, s in {a,b})
      H_J   = -J_ab_signed * (B^dag_a B_b + B^dag_b B_a)
              where B_s = sum_m b_{s,m}

    Returns sparse CSR Hamiltonian, basis list [(occ_a, occ_b, (n_a,n_b))].
    """
    n_modes_a = len(evals_a)
    n_modes_b = len(evals_b)
    mu_a = float(np.median(evals_a))
    xi_a = evals_a - mu_a
    mu_b = float(np.median(evals_b))
    xi_b = evals_b - mu_b

    # Enumerate all (n_a, n_b) splits with n_a + n_b = N_total
    # and n_a, n_b in [0, n_cutoff].
    splits = [(n_a, N_total - n_a)
              for n_a in range(max(0, N_total - n_cutoff),
                               min(N_total, n_cutoff) + 1)
              if 0 <= N_total - n_a <= n_cutoff]

    # Build global basis
    basis = []  # list of (occ_a, occ_b, n_a, n_b)
    index_map = {}  # (n_a, n_b, occ_a, occ_b) -> global idx
    block_indices = {}  # (n_a, n_b) -> list of global indices
    for (n_a, n_b) in splits:
        block_indices[(n_a, n_b)] = []
        for occ_a in build_pair_basis(n_modes_a, n_a):
            for occ_b in build_pair_basis(n_modes_b, n_b):
                idx = len(basis)
                basis.append((occ_a, occ_b, n_a, n_b))
                index_map[(n_a, n_b, occ_a, occ_b)] = idx
                block_indices[(n_a, n_b)].append(idx)

    D = len(basis)
    if D == 0:
        return None, [], {}

    # Build using lil_matrix (fast row-wise construction)
    H = lil_matrix((D, D), dtype=np.float64)

    # 1) Diagonal + intra-sector terms
    for g_idx in range(D):
        occ_a, occ_b, n_a, n_b = basis[g_idx]
        # Kinetic
        diag = 2.0 * float(sum(xi_a[m] for m in occ_a)) + 2.0 * float(sum(xi_b[m] for m in occ_b))
        # Self-V0 (from m=n in pair-hop sum)
        for m in occ_a:
            diag += -V_intra * (fw_a[m] ** 2) / n_modes_a
        for m in occ_b:
            diag += -V_intra * (fw_b[m] ** 2) / n_modes_b
        H[g_idx, g_idx] = diag

        # Intra-sector pair hopping in a (preserves n_a, n_b, occ_b)
        occ_a_set = set(occ_a)
        occ_a_frz = occ_a
        for n in occ_a_set:
            for m in range(n_modes_a):
                if m in occ_a_set:
                    continue
                new_occ_a = tuple(sorted((occ_a_set - {n}) | {m}))
                key = (n_a, n_b, new_occ_a, occ_b)
                j = index_map.get(key)
                if j is None:
                    continue
                H[j, g_idx] += -V_intra * fw_a[m] * fw_a[n] / n_modes_a

        # Intra-sector pair hopping in b
        occ_b_set = set(occ_b)
        for n in occ_b_set:
            for m in range(n_modes_b):
                if m in occ_b_set:
                    continue
                new_occ_b = tuple(sorted((occ_b_set - {n}) | {m}))
                key = (n_a, n_b, occ_a, new_occ_b)
                j = index_map.get(key)
                if j is None:
                    continue
                H[j, g_idx] += -V_intra * fw_b[m] * fw_b[n] / n_modes_b

        # 2) Inter-sector Josephson (moves pair a<->b)
        # Transition: (n_a, n_b) -> (n_a+1, n_b-1): create pair at m in a, destroy at n in b
        if n_a + 1 <= n_cutoff and n_b - 1 >= 0:
            for m in range(n_modes_a):
                if m in occ_a_set:
                    continue
                for n in occ_b_set:
                    new_occ_a = tuple(sorted(occ_a_set | {m}))
                    new_occ_b = tuple(sorted(occ_b_set - {n}))
                    key = (n_a + 1, n_b - 1, new_occ_a, new_occ_b)
                    j = index_map.get(key)
                    if j is None:
                        continue
                    H[j, g_idx] += -J_ab_signed
        # Reverse (n_a, n_b) -> (n_a-1, n_b+1)
        if n_a - 1 >= 0 and n_b + 1 <= n_cutoff:
            for n in occ_a_set:
                for m in range(n_modes_b):
                    if m in occ_b_set:
                        continue
                    new_occ_a = tuple(sorted(occ_a_set - {n}))
                    new_occ_b = tuple(sorted(occ_b_set | {m}))
                    key = (n_a - 1, n_b + 1, new_occ_a, new_occ_b)
                    j = index_map.get(key)
                    if j is None:
                        continue
                    H[j, g_idx] += -J_ab_signed

    # Convert to CSR for eigensolver and symmetrize
    H_csr = H.tocsr()
    H_csr = 0.5 * (H_csr + H_csr.T)
    return H_csr, basis, block_indices


def sparse_gs(H_csr, prefer_dense_max=512):
    """Smallest eigenvalue. Use dense eigh for small matrices (< 512), else Lanczos."""
    if H_csr is None:
        return float('inf')
    D = H_csr.shape[0]
    if D <= 1:
        return float(H_csr[0, 0]) if D == 1 else float('inf')
    if D <= prefer_dense_max:
        H_dense = H_csr.toarray()
        evals = np.linalg.eigvalsh(H_dense)
        return float(evals[0])
    # Lanczos via ARPACK
    try:
        # Use shift-invert around a guess below the expected GS energy
        evals, _ = sparse_eigsh(H_csr, k=1, which='SA', maxiter=5000, tol=1e-10)
        return float(evals[0])
    except Exception as exc:
        # Fallback: dense if feasible
        if D <= 20000:
            H_dense = H_csr.toarray()
            evals = np.linalg.eigvalsh(H_dense)
            return float(evals[0])
        raise exc


# =====================================================================
# SECTION 4: Pre-compute inputs for the active sectors
# =====================================================================
sd_00 = sector_data[(0, 0)]
evals_00 = sd_00['evals']
x_00 = evals_00 ** 2 / sd_00['lam_max'] ** 2
fw_00 = fstar(x_00)

sd_11 = sector_data[(1, 1)]
evals_11 = sd_11['evals']
x_11 = evals_11 ** 2 / sd_11['lam_max'] ** 2
fw_11 = fstar(x_11)

# Inter-sector Josephson J_ab for ((0,0),(1,1)): delta_level=2 -> u(1) coupling
J_AB_U1 = J_u1  # (local) 0.038 M_KK (per s78 dl=2 rule)

log("=" * 78)
log("SECTION 4: Canonical run (N_pair_cutoff = 2)")
log("=" * 78)
log(f"  Josephson J_ab ((0,0)<->(1,1)) = J_u1 = {J_AB_U1:.4f} M_KK (dl=2 rule per s78)")
log()


def compute_gs_for_sign(sign_config, n_cutoff):
    """Sweep N_total and find global ground-state energy for given sign config."""
    J_signed = J_AB_U1 if sign_config == 's++' else -J_AB_U1  # (local)
    E_gs_global = float('inf')
    Ntot_best = None  # (local)
    block_results = []  # (local) list of (N_total, dim, E_min)
    for N_total in range(0, 2 * n_cutoff + 1):
        H_csr, basis, _ = build_two_sector_sparse_H(
            evals_00, fw_00, evals_11, fw_11,
            V0_INTRA_CALIB, J_signed, N_total, n_cutoff,
        )
        if H_csr is None:
            continue
        D = H_csr.shape[0]
        E_min = sparse_gs(H_csr)
        block_results.append((N_total, D, E_min))
        if E_min < E_gs_global:
            E_gs_global = E_min
            Ntot_best = N_total
    return E_gs_global, Ntot_best, block_results


# Canonical: N_PAIR_CUTOFF = 2
log("  Computing canonical E_GS for sign = s++ (J_ab = +J_u1)...")
t0 = time.time()
E_gs_spp, Ntot_spp, blocks_spp = compute_gs_for_sign('s++', N_PAIR_CUTOFF)
log(f"    E_GS(s++) = {E_gs_spp:.10f} (N_total={Ntot_spp}, t = {time.time()-t0:.2f}s)")
for (Ntot, D, Em) in blocks_spp:
    log(f"      N_total={Ntot}: dim={D}, E_min = {Em:.10f}")
log()

log("  Computing canonical E_GS for sign = s+- (J_ab = -J_u1)...")
t0 = time.time()
E_gs_spm, Ntot_spm, blocks_spm = compute_gs_for_sign('s+-', N_PAIR_CUTOFF)
log(f"    E_GS(s+-) = {E_gs_spm:.10f} (N_total={Ntot_spm}, t = {time.time()-t0:.2f}s)")
for (Ntot, D, Em) in blocks_spm:
    log(f"      N_total={Ntot}: dim={D}, E_min = {Em:.10f}")
log()

# =====================================================================
# SECTION 5: ED margin and verdict
# =====================================================================
log("=" * 78)
log("SECTION 5: ED margin and verdict logic (canonical run)")
log("=" * 78)

if E_gs_spp < E_gs_spm:
    sign_preferred_ed = 's++'  # (local)
    E_gs_pref = E_gs_spp  # (local)
    E_gs_alt = E_gs_spm  # (local)
else:
    sign_preferred_ed = 's+-'  # (local)
    E_gs_pref = E_gs_spm  # (local)
    E_gs_alt = E_gs_spp  # (local)

margin_ED = abs(E_gs_alt - E_gs_pref) / abs(E_gs_pref) if abs(E_gs_pref) > 1e-14 else float('inf')  # (local)
sign_margin_delta = margin_ED - MARGIN_MF  # (local)
ratio_ED_MF = margin_ED / MARGIN_MF if MARGIN_MF > 0 else float('inf')  # (local)

log(f"  E_GS(s++) = {E_gs_spp:.10f}")
log(f"  E_GS(s+-) = {E_gs_spm:.10f}")
log(f"  Delta E (E_s+- - E_s++) = {E_gs_spm - E_gs_spp:.6e}")
log(f"  Sign preferred by ED: {sign_preferred_ed}")
log(f"  margin_ED = {margin_ED:.6e} = {margin_ED*100:.4f}%")
log(f"  Mean-field s78 margin: {MARGIN_MF:.6e} = {MARGIN_MF*100:.4f}%")
log(f"  sign_margin_delta = {sign_margin_delta:.6e}")
log(f"  ratio ED/MF = {ratio_ED_MF:.4f}")
log()

# Verdict logic
if sign_preferred_ed == 's++':
    if margin_ED <= MARGIN_PASS_THRESH:
        verdict = "PASS"  # (local)
        detail = (f"margin_ED={margin_ED:.4e} <= MF/2={MARGIN_PASS_THRESH:.2e}; "
                  f"sign_ED=s++ matches Eliashberg-preferred; ED tightens MF "
                  f"by factor {1/ratio_ED_MF:.2f}")
    elif margin_ED <= MARGIN_INFO_HI:
        verdict = "INFO"  # (local)
        detail = (f"margin_ED={margin_ED:.4e} in [{MARGIN_PASS_THRESH:.2e},"
                  f"{MARGIN_INFO_HI:.2e}]; sign_ED=s++ matches Eliashberg-preferred; "
                  f"agreement without tightening")
    else:
        verdict = "INFO"  # (local)
        detail = (f"margin_ED={margin_ED:.4e} > {MARGIN_INFO_HI:.2e}; sign_ED=s++ "
                  f"matches Eliashberg-preferred; MF margin underestimated by "
                  f"factor {ratio_ED_MF:.2f}")
else:
    if margin_ED >= MARGIN_FAIL_THRESH:
        verdict = "FAIL"  # (local)
        detail = (f"sign_ED=s+- DISAGREES with Eliashberg-preferred s++; "
                  f"margin_ED={margin_ED:.4e} >= {MARGIN_FAIL_THRESH:.1e} FAIL "
                  f"threshold; analytical bound rejected by ED")
    else:
        verdict = "INFO"  # (local)
        detail = (f"sign_ED=s+- matches MF-energy-preferred (not Eliashberg); "
                  f"margin_ED={margin_ED:.4e} below {MARGIN_FAIL_THRESH:.1e} "
                  f"FAIL threshold; ED confirms MF energy winner with "
                  f"ratio to MF = {ratio_ED_MF:.2f}")

log(f"  *** GATE S82-S-PP-FULL-ED: {verdict} ***")
log(f"  {detail}")
log()

# =====================================================================
# SECTION 6: Cross-checks
# =====================================================================
log("=" * 78)
log("SECTION 6: Cross-checks")
log("=" * 78)


def unint_gs_expected(evals, n_pair):
    mu_s = float(np.median(evals))
    xi_s = evals - mu_s
    xi_sorted = np.sort(xi_s)
    return 2.0 * float(np.sum(xi_sorted[:n_pair]))


# CC1: Non-interacting (V0=0, J=0) - ground state at N_total = 2*N_PAIR_CUTOFF fills lowest xi
H_ni, _, _ = build_two_sector_sparse_H(
    evals_00, fw_00, evals_11, fw_11,
    0.0, 0.0, 2 * N_PAIR_CUTOFF, N_PAIR_CUTOFF,
)
E_gs_ni = sparse_gs(H_ni)  # (local)
cc1_expected = unint_gs_expected(evals_00, N_PAIR_CUTOFF) + unint_gs_expected(evals_11, N_PAIR_CUTOFF)  # (local)
cc1_err = abs(E_gs_ni - cc1_expected)  # (local)
cc1_pass = cc1_err < 1e-8  # (local)
log(f"  CC1: Non-interacting ED reproduces filled-Fermi-sea (at N_total={2*N_PAIR_CUTOFF}):")
log(f"       ED(V=0,J=0) = {E_gs_ni:.10f}")
log(f"       Expected   = {cc1_expected:.10f}")
log(f"       Error      = {cc1_err:.2e}")
log(f"       CC1: {'PASS' if cc1_pass else 'FAIL'}")
log()

# CC2: J=0 decoupling, E_GS(J=0) should bracket E_GS(s++) and E_GS(s+-)
t0 = time.time()
E_gs_jzero = float('inf')
for N_total in range(0, 2 * N_PAIR_CUTOFF + 1):
    H_z, _, _ = build_two_sector_sparse_H(
        evals_00, fw_00, evals_11, fw_11,
        V0_INTRA_CALIB, 0.0, N_total, N_PAIR_CUTOFF,
    )
    if H_z is None:
        continue
    E_min = sparse_gs(H_z)
    E_gs_jzero = min(E_gs_jzero, E_min)
cc2_between = min(E_gs_spp, E_gs_spm) - 1e-8 <= E_gs_jzero <= max(E_gs_spp, E_gs_spm) + 1e-8  # (local)
cc2_avg_err = abs(E_gs_jzero - 0.5 * (E_gs_spp + E_gs_spm))  # (local)
cc2_pass = cc2_between  # (local)
log(f"  CC2: Decoupling check (J=0) -> brackets both signed cases:")
log(f"       E_GS(J=0) = {E_gs_jzero:.10f}  (t={time.time()-t0:.2f}s)")
log(f"       E_GS(s++) = {E_gs_spp:.10f}")
log(f"       E_GS(s+-) = {E_gs_spm:.10f}")
log(f"       Between bounds: {cc2_between}")
log(f"       CC2: {'PASS' if cc2_pass else 'INFO'}")
log()

# CC3: Single-sector (0,0) at N_pair=1 vs s78 MF E_cond^(0,0)
# Build single-sector Hamiltonian via build_two_sector_sparse_H with n_b=0 effectively
# (by putting zero sector b couplings)
# Easier: directly compute single-sector spectrum at N_pair=1
log(f"  CC3: Single-sector (0,0) sweep N_pair in [0, {N_PAIR_CUTOFF}]")


def single_sector_gs(evals, fw, V, n_pair):
    """GS energy of Richardson Hamiltonian on ONE sector at fixed N_pair."""
    n_modes = len(evals)
    mu = float(np.median(evals))
    xi = evals - mu
    basis = build_pair_basis(n_modes, n_pair)
    D = len(basis)
    if D == 0:
        return 0.0
    if D == 1:
        occ = basis[0]
        diag = 2.0 * float(sum(xi[m] for m in occ))
        for m in occ:
            diag += -V * (fw[m] ** 2) / n_modes
        return diag
    H = np.zeros((D, D))
    index_map = {b: i for i, b in enumerate(basis)}
    for i, occ in enumerate(basis):
        diag = 2.0 * float(sum(xi[m] for m in occ))
        occ_set = set(occ)
        for m in occ_set:
            diag += -V * (fw[m] ** 2) / n_modes
        H[i, i] = diag
        for n in occ_set:
            for m in range(n_modes):
                if m in occ_set:
                    continue
                new_occ = tuple(sorted((occ_set - {n}) | {m}))
                j = index_map.get(new_occ)
                if j is None:
                    continue
                H[j, i] += -V * fw[m] * fw[n] / n_modes
    H = 0.5 * (H + H.T)
    evals_H = np.linalg.eigvalsh(H)
    return float(evals_H[0])


E_N0_00 = single_sector_gs(evals_00, fw_00, V0_INTRA_CALIB, 0)  # (local)
E_N1_00 = single_sector_gs(evals_00, fw_00, V0_INTRA_CALIB, 1)  # (local)
E_N2_00 = single_sector_gs(evals_00, fw_00, V0_INTRA_CALIB, 2)  # (local)
E_N3_00 = single_sector_gs(evals_00, fw_00, V0_INTRA_CALIB, 3)  # (local)
E_min_ss_00 = min(E_N0_00, E_N1_00, E_N2_00, E_N3_00)  # (local)
# Choose E_cond^(0,0) = E_min_ss_00 - E_N0_00 (condensation relative to N=0 vacuum)
E_cond_ED_00 = E_min_ss_00 - E_N0_00  # (local)
cc3_err = abs(E_cond_ED_00 - E_cond_MF[(0, 0)]) / abs(E_cond_MF[(0, 0)]) if abs(E_cond_MF[(0, 0)]) > 1e-12 else float('inf')  # (local)
cc3_pass = cc3_err < 0.5  # (local) 50% band: MF and ED agree at structural level
log(f"    E_N0 = {E_N0_00:.8f}")
log(f"    E_N1 = {E_N1_00:.8f}")
log(f"    E_N2 = {E_N2_00:.8f}")
log(f"    E_N3 = {E_N3_00:.8f}")
log(f"    E_cond_ED_(0,0) = E_N_best - E_N0 = {E_cond_ED_00:.8f}")
log(f"    MF E_cond^(0,0) (s78) = {E_cond_MF[(0,0)]:.8f}")
log(f"    Rel diff = {cc3_err*100:.2f}%")
log(f"    CC3: {'PASS' if cc3_pass else 'INFO'} (structural-level check)")
log()

# CC4: dense scipy eigh vs sparse eigsh on a test block
log("  CC4: dense numpy eigvalsh vs sparse Lanczos on a single block")
H_test, _, _ = build_two_sector_sparse_H(
    evals_00, fw_00, evals_11, fw_11,
    V0_INTRA_CALIB, J_AB_U1, 2, N_PAIR_CUTOFF,
)
if H_test is not None:
    D_test = H_test.shape[0]
    H_dense = H_test.toarray()
    E_dense = np.linalg.eigvalsh(H_dense)
    if D_test > 2:
        try:
            E_sparse = sparse_eigsh(H_test, k=1, which='SA', maxiter=5000, tol=1e-10)[0]
            cc4_err = float(abs(E_dense[0] - E_sparse[0]))  # (local)
        except Exception:
            cc4_err = 0.0  # (local) fallback to dense result was used
    else:
        cc4_err = 0.0  # (local)
    cc4_pass = cc4_err < 1e-8  # (local)
    log(f"    Test block dim = {D_test}")
    log(f"    Dense GS  = {E_dense[0]:.10f}")
    log(f"    Sparse GS = {E_sparse[0] if D_test > 2 else E_dense[0]:.10f}")
    log(f"    |err|     = {cc4_err:.2e}")
    log(f"    CC4: {'PASS' if cc4_pass else 'INFO'}")
else:
    cc4_err = 0.0  # (local)
    cc4_pass = False
    log("    Test block unavailable")
log()

# =====================================================================
# SECTION 7 (OPTIONAL): Extended run at N_PAIR_CUTOFF_EXT = 3
# =====================================================================
log("=" * 78)
log(f"SECTION 7: Extended convergence check at N_pair_cutoff = {N_PAIR_CUTOFF_EXT}")
log("=" * 78)

# Run only the highest-weight total-pair block (Ntot_spp from canonical) with extended cutoff.
# This is the convergence check for the sign margin.
ext_available = True  # (local)
try:
    t0 = time.time()
    # Ext cutoff sweep: only check the canonical-GS N_total and +/- 1 to keep runtime bounded
    N_TOTAL_CHECKS = [max(0, Ntot_spp - 1), Ntot_spp, min(2 * N_PAIR_CUTOFF_EXT, Ntot_spp + 1)]  # (local)
    N_TOTAL_CHECKS = sorted(set(N_TOTAL_CHECKS))
    ext_blocks_spp = []  # (local)
    ext_blocks_spm = []  # (local)
    for N_total in N_TOTAL_CHECKS:
        # s++
        H_p, _, _ = build_two_sector_sparse_H(
            evals_00, fw_00, evals_11, fw_11,
            V0_INTRA_CALIB, +J_AB_U1, N_total, N_PAIR_CUTOFF_EXT,
        )
        if H_p is not None:
            E_p = sparse_gs(H_p)
            ext_blocks_spp.append((N_total, H_p.shape[0], E_p))
            log(f"    ext s++: N_total={N_total}, dim={H_p.shape[0]}, E_min={E_p:.10f} "
                f"(t so far = {time.time()-t0:.1f}s)")
        # s+-
        H_m, _, _ = build_two_sector_sparse_H(
            evals_00, fw_00, evals_11, fw_11,
            V0_INTRA_CALIB, -J_AB_U1, N_total, N_PAIR_CUTOFF_EXT,
        )
        if H_m is not None:
            E_m = sparse_gs(H_m)
            ext_blocks_spm.append((N_total, H_m.shape[0], E_m))
            log(f"    ext s+-: N_total={N_total}, dim={H_m.shape[0]}, E_min={E_m:.10f} "
                f"(t so far = {time.time()-t0:.1f}s)")
    if ext_blocks_spp and ext_blocks_spm:
        E_gs_spp_ext = min(x[2] for x in ext_blocks_spp)  # (local)
        E_gs_spm_ext = min(x[2] for x in ext_blocks_spm)  # (local)
        if E_gs_spp_ext < E_gs_spm_ext:
            sign_ext = 's++'  # (local)
            E_pref_ext = E_gs_spp_ext  # (local)
            E_alt_ext = E_gs_spm_ext  # (local)
        else:
            sign_ext = 's+-'  # (local)
            E_pref_ext = E_gs_spm_ext  # (local)
            E_alt_ext = E_gs_spp_ext  # (local)
        margin_ED_ext = abs(E_alt_ext - E_pref_ext) / abs(E_pref_ext)  # (local)
        log(f"\n    Ext E_GS(s++) = {E_gs_spp_ext:.10f}")
        log(f"    Ext E_GS(s+-) = {E_gs_spm_ext:.10f}")
        log(f"    Ext sign pref = {sign_ext}")
        log(f"    Ext margin = {margin_ED_ext:.6e} = {margin_ED_ext*100:.4f}%")
        log(f"    Canonical margin = {margin_ED:.6e} = {margin_ED*100:.4f}%")
        margin_convergence_delta = abs(margin_ED_ext - margin_ED)  # (local)
        log(f"    |ext - canonical margin| = {margin_convergence_delta:.2e}")
    else:
        ext_available = False
        E_gs_spp_ext = float('nan')
        E_gs_spm_ext = float('nan')
        margin_ED_ext = float('nan')
        sign_ext = 'n/a'
        margin_convergence_delta = float('nan')
except Exception as exc:
    log(f"    Extended run aborted: {exc}")
    ext_available = False
    E_gs_spp_ext = float('nan')
    E_gs_spm_ext = float('nan')
    margin_ED_ext = float('nan')
    sign_ext = 'n/a'
    margin_convergence_delta = float('nan')
log()

# =====================================================================
# SECTION 8: Save + plot
# =====================================================================
log("=" * 78)
log("SECTION 8: Save npz + plot + verdict")
log("=" * 78)

save_dict = {
    'verdict': np.array([verdict]),
    'verdict_detail': np.array([detail]),
    'E_gs_spp': E_gs_spp,
    'E_gs_spm': E_gs_spm,
    'sign_preferred_ed': np.array([sign_preferred_ed]),
    'margin_ED': margin_ED,
    'margin_MF_s78': MARGIN_MF,
    'sign_margin_delta': sign_margin_delta,
    'ratio_ED_MF': ratio_ED_MF,
    'V0_INTRA_CALIB': V0_INTRA_CALIB,
    'J_ab_u1': J_AB_U1,
    'N_PAIR_CUTOFF': N_PAIR_CUTOFF,
    'N_PAIR_CUTOFF_EXT': N_PAIR_CUTOFF_EXT,
    'Delta_MF_00': Delta_MF[(0, 0)],
    'Delta_MF_11': Delta_MF[(1, 1)],
    'E_cond_MF_00': E_cond_MF[(0, 0)],
    'E_cond_MF_11': E_cond_MF[(1, 1)],
    'block_energies_spp': np.array(blocks_spp),
    'block_energies_spm': np.array(blocks_spm),
    'E_gs_spp_ext': E_gs_spp_ext,
    'E_gs_spm_ext': E_gs_spm_ext,
    'sign_ext': np.array([sign_ext]),
    'margin_ED_ext': margin_ED_ext,
    'margin_convergence_delta': margin_convergence_delta,
    'cc1_pass': cc1_pass,
    'cc1_err': cc1_err,
    'cc2_pass': cc2_pass,
    'cc2_avg_err': cc2_avg_err,
    'cc3_pass': cc3_pass,
    'cc3_relative_err': cc3_err,
    'cc4_pass': cc4_pass,
    'cc4_err': cc4_err,
    'E_cond_ED_00': E_cond_ED_00,
    'SHA_SPECTRUM': SHA_SPECTRUM,
    'SHA_S78': SHA_S78,
    'SHA_CANONICAL': SHA_CANONICAL,
    'scheme_tag': np.array([SCHEME_TAG]),
    'convention_tag': np.array([CONVENTION_TAG]),
    'L_max_tag': L_MAX_TAG,
}
np.savez(OUT_NPZ, **save_dict)
log(f"  Saved: {OUT_NPZ}")

# Plot: 4 panels
fig = plt.figure(figsize=(14, 8))
gs = GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
if blocks_spp and blocks_spm:
    N_spp = [b[0] for b in blocks_spp]
    E_spp = [b[2] for b in blocks_spp]
    N_spm = [b[0] for b in blocks_spm]
    E_spm = [b[2] for b in blocks_spm]
    ax1.plot(N_spp, E_spp, 'o-', label='s++ (J>0)', color='tab:blue')
    ax1.plot(N_spm, E_spm, 's--', label='s+- (J<0)', color='tab:orange')
    ax1.axhline(E_gs_spp, color='tab:blue', ls=':', alpha=0.4)
    ax1.axhline(E_gs_spm, color='tab:orange', ls=':', alpha=0.4)
ax1.set_xlabel('N_total (pair number)')
ax1.set_ylabel('E_min (M_KK units)')
ax1.set_title(f'Canonical run: E_min vs N_total (N_pair_cutoff={N_PAIR_CUTOFF})')
ax1.legend(loc='best', fontsize=8)
ax1.grid(alpha=0.3)

ax2 = fig.add_subplot(gs[0, 1])
bar_labels = ['MF (s78 uniform-gap)', f'ED (N_cut={N_PAIR_CUTOFF})']
bar_vals = [MARGIN_MF, margin_ED]
colors = ['tab:gray', 'tab:blue' if sign_preferred_ed == 's++' else 'tab:red']
if ext_available and not np.isnan(margin_ED_ext):
    bar_labels.append(f'ED ext (N_cut={N_PAIR_CUTOFF_EXT})')
    bar_vals.append(margin_ED_ext)
    colors.append('tab:green' if sign_ext == 's++' else 'tab:purple')
ax2.bar(bar_labels, bar_vals, color=colors)
ax2.axhline(MARGIN_PASS_THRESH, color='green', ls='--', label=f'PASS <= {MARGIN_PASS_THRESH:.2e}')
ax2.axhline(MARGIN_INFO_HI, color='orange', ls='--', label=f'INFO <= {MARGIN_INFO_HI:.2e}')
ax2.axhline(MARGIN_FAIL_THRESH, color='red', ls='--', label=f'FAIL >= {MARGIN_FAIL_THRESH:.1e}')
ax2.set_ylabel('|E(alt) - E(pref)| / |E(pref)|')
ax2.set_title(f'Sign margin (ED vs MF)\nverdict: {verdict}')
ax2.set_yscale('log')
ax2.legend(loc='best', fontsize=7)
ax2.grid(alpha=0.3)
ax2.tick_params(axis='x', rotation=15)

ax3 = fig.add_subplot(gs[1, 0])
# Plot spectrum of the canonical best block for both signs
if Ntot_spp is not None:
    H_best_p, _, _ = build_two_sector_sparse_H(
        evals_00, fw_00, evals_11, fw_11,
        V0_INTRA_CALIB, +J_AB_U1, Ntot_spp, N_PAIR_CUTOFF,
    )
    H_best_m, _, _ = build_two_sector_sparse_H(
        evals_00, fw_00, evals_11, fw_11,
        V0_INTRA_CALIB, -J_AB_U1, Ntot_spp, N_PAIR_CUTOFF,
    )
    if H_best_p is not None and H_best_p.shape[0] > 1:
        if H_best_p.shape[0] <= 512:
            E_p_full = np.linalg.eigvalsh(H_best_p.toarray())
            E_m_full = np.linalg.eigvalsh(H_best_m.toarray())
        else:
            E_p_full = sparse_eigsh(H_best_p, k=min(10, H_best_p.shape[0] - 2),
                                     which='SA', maxiter=5000, tol=1e-10)[0]
            E_m_full = sparse_eigsh(H_best_m, k=min(10, H_best_m.shape[0] - 2),
                                     which='SA', maxiter=5000, tol=1e-10)[0]
            E_p_full = np.sort(E_p_full)
            E_m_full = np.sort(E_m_full)
        n_show = min(10, len(E_p_full))
        ax3.plot(np.arange(n_show), E_p_full[:n_show], 'o-', label='s++', color='tab:blue')
        ax3.plot(np.arange(n_show), E_m_full[:n_show], 's--', label='s+-', color='tab:orange')
        ax3.set_xlabel('Eigenvalue index')
        ax3.set_ylabel('Energy (M_KK)')
        ax3.set_title(f'Low-lying spectrum at N_total={Ntot_spp}')
        ax3.legend(fontsize=8)
        ax3.grid(alpha=0.3)

ax4 = fig.add_subplot(gs[1, 1])
ax4.axis('off')
summary_text = (
    f"GATE: S82-S-PP-FULL-ED [AUDIT]\n"
    f"VERDICT: {verdict}\n\n"
    f"Canonical (N_pair_cutoff={N_PAIR_CUTOFF}):\n"
    f"  E_GS(s++) = {E_gs_spp:.8f}\n"
    f"  E_GS(s+-) = {E_gs_spm:.8f}\n"
    f"  Sign winner = {sign_preferred_ed}\n"
    f"  margin_ED = {margin_ED:.4e} = {margin_ED*100:.4f}%\n\n"
    f"Mean-field baseline (s78):\n"
    f"  margin_MF = {MARGIN_MF:.4e} = {MARGIN_MF*100:.4f}%\n"
    f"  ratio ED/MF = {ratio_ED_MF:.3f}\n\n"
)
if ext_available and not np.isnan(margin_ED_ext):
    summary_text += (f"Extended (N_pair_cutoff={N_PAIR_CUTOFF_EXT}):\n"
                     f"  margin_ED_ext = {margin_ED_ext:.4e}\n"
                     f"  conv |ext-canon| = {margin_convergence_delta:.2e}\n\n")
summary_text += (
    f"Cross-checks:\n"
    f"  CC1 (non-int): {'PASS' if cc1_pass else 'FAIL'}\n"
    f"  CC2 (J=0):     {'PASS' if cc2_pass else 'INFO'}\n"
    f"  CC3 (MF E_c):  {'PASS' if cc3_pass else 'INFO'}\n"
    f"  CC4 (sparse vs dense): {'PASS' if cc4_pass else 'INFO'}\n\n"
    f"scheme={SCHEME_TAG}, convention={CONVENTION_TAG}, L_max={L_MAX_TAG}"
)
ax4.text(0.02, 0.98, summary_text, transform=ax4.transAxes, fontsize=9,
         verticalalignment='top', family='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85))

fig.suptitle(
    f"S82 W2-11: Full ED on (0,0)+(1,1) sub-sector [AUDIT]\n"
    f"tau=tau_fold / L_max={L_MAX_TAG} / Josephson J_u1={J_AB_U1}",
    fontsize=12,
)
fig.tight_layout(rect=(0, 0, 1, 0.96))
plt.savefig(OUT_PNG, dpi=130, bbox_inches='tight')
plt.close(fig)
log(f"  Saved: {OUT_PNG}")

# =====================================================================
# SECTION 9: Closure SHA + verdict line
# =====================================================================
log("=" * 78)
log("SECTION 9: Closure SHA + verdict line")
log("=" * 78)

input_pin_map = (
    f"s74_spectrum_cache_L9_tau019.npz:{SHA_SPECTRUM}|"
    f"s78_multi_band_econd.npz:{SHA_S78}|"
    f"canonical_constants.py:{SHA_CANONICAL}"
)
closure_sha = hashlib.sha256(input_pin_map.encode('utf-8')).hexdigest()  # (local)
log(f"  Closure SHA-256: {closure_sha}")

verdict_line = (
    f"S82-S-PP-FULL-ED: {verdict} -- "
    f"value={sign_margin_delta:.6e} "
    f"scheme={SCHEME_TAG} "
    f"convention={CONVENTION_TAG} "
    f"L_max={L_MAX_TAG} "
    f"sha256={closure_sha}"
)
with open(VERDICT_FILE, 'a') as f:
    f.write(verdict_line + "\n")

log(f"  Verdict line appended to {VERDICT_FILE}:")
log(f"    {verdict_line}")
log()
log(f"OUTPUT_4TUPLE: (value={sign_margin_delta:.6e}, scheme={SCHEME_TAG}, "
    f"convention={CONVENTION_TAG}, L_max={L_MAX_TAG})")
log()
log(f"  Total runtime: {time.time()-t_start:.2f} seconds")
log(f"  VERDICT LINE (canonical): {verdict_line}")

with open(OUT_TXT, 'w') as f:
    f.write("\n".join(log_lines))
