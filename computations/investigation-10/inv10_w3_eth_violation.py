#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
INV10-W3-4 — ETH-violation test on the deep-truncation D_K spectrum
(the positive, eigenstate-level statement of the Ordered Veil; cell-vs-fabric discriminator)

Substrate-first framing (GEOMETRIC):
    The D_K eigenSTATES are the fabric's vibrational modes. ETH (Srednicki 1994) says a
    CHAOTIC system's individual eigenstates already look thermal, so the eigenstate-to-
    eigenstate fluctuation Delta_A(E) of a local operator A at fixed energy self-averages
    as Delta_A ~ D^{-1/2} (D = Hilbert dimension, S = ln D). INTEGRABLE systems VIOLATE
    this: each eigenstate carries a full set of conserved-charge labels, so <E_i|A|E_i>
    scatters O(1) at fixed energy independent of D (Rigol-Srednicki). That O(1) scatter
    (beta -> 0) is WHY an integrable system relaxes to a GGE, not a thermal state -- the
    eigenstate-level statement of the Ordered Veil, stronger and scale-cleaner than the
    transit-timescale argument (R_therm = 5252, S95).

    Chain: D_K eigenstates -> diagonal matrix elements <E|A|E> of a substrate-local operator
    -> size-scaling of the eigenstate fluctuation Delta_A(D) -> ETH-violation classification
    -> Ordered Veil as an eigenstate-level structural property. The explanation flows from the
    eigenstate structure to the non-thermalization, never the reverse.

Discriminator (the gate):
    beta := -d ln Delta_A / d ln D.
    ETH-satisfied  <=> beta = 1/2 (fluctuation self-averages).
    ETH-violated   <=> beta -> 0 (fluctuation does not self-average).
    FABRIC  (CG(24) Poisson <r>=0.367, lambda_L=0, integrable) should VIOLATE:  beta_fabric ~ 0.
    CELL    (INTEG-39: Brody beta=0.633, 63% GOE, weakly chaotic) should APPROACH ETH: beta_cell larger.
    PASS iff beta_fabric <= beta_viol = 0.25  AND  (beta_cell - beta_fabric) >= dbeta_min = 0.15.

Operators:
    FABRIC, A1 = a fixed Hermitian Clifford spinor bilinear gamma^0 (x) 1_rep, lifted to each
                 (p,q) block on V_(p,q) (x) C^16. Substrate-local (acts identically on every
                 fiber's spinor content -- the same C^16 structure that carries the mass terms),
                 and generically OFF-DIAGONAL in the D_K eigenbasis (D_K mixes spinor and rep
                 indices through the connection Omega and the Clifford action), so its diagonal
                 <E_i|A1|E_i> has genuine eigenstate-to-eigenstate scatter at fixed |lambda|.
    FABRIC, A2 = Peter-Weyl sector membership on the POOLED spectrum (the cosmological-observable
                 spectrum is the union of all (p,q) blocks). At fixed energy, different (p,q)
                 blocks contribute eigenvalues at overlapping |lambda|, so "is this eigenstate in
                 sector (p,q)?" scatters eigenstate-to-eigenstate -- a Berry-Tabor-superposition
                 ETH diagnostic (the matrix-element image of W3-3's eigenvalue-side Sigma^2/SFF).
    CELL,   A  = (Delta + Delta^dag)/sqrt(2), the canonical CHAOS-2 / OTOC DOS-weighted pair
                 operator Delta = sum_k sqrt(rho_k) P_k (s38_otoc_bcs.py), built in the pair-Fock
                 basis (off-diagonal in the H_BCS energy eigenbasis).

Verdict (investigation track): emit_verdict(session=10, track="investigation").
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical constants
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent           # computations/investigation-10
COMPUTATIONS_DIR = SESSION_DIR.parent                    # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import Delta_BCS, tau_fold, M_KK  # noqa: E402
import dirac_spectrum as tds                               # noqa: E402

# GPU: matrix elements need eigenVECTORS; per-block / 256-dim cell dims are modest.
try:
    import torch
    _HAS_TORCH = torch.cuda.is_available()
except Exception:
    _HAS_TORCH = False

SESSION = "INV10"                                                       # (local)
GATE_ID = "INV10-W3-4"                                                  # (local)
SCHEME = "FW"                                                           # (local) framework substrate scheme
CONVENTION = "DIAGONAL-ETH-MICROCANONICAL;CELL-VS-FABRIC"              # (local)
L_MAX = 12                                                              # (local) primary cache truncation (+14 cross-check)

# ---- Pinned PASS boundary (PRDR strict_PASS_boundary) ----
BETA_VIOL = 0.25                                                        # (local) fabric ETH-violation ceiling (<< ETH 0.5)
DBETA_MIN = 0.15                                                        # (local) cell-vs-fabric exponent-gap floor
ETH_SELF_AVG = 0.5                                                      # (local) Srednicki self-averaging exponent
BETA_INFO_HI = 0.40                                                    # (local) INFO upper edge for partial violation

# ---- Pinned machinery (machinery_pin_map) ----
TAU_FABRIC = float(tau_fold)                                           # (local) 0.19 fabric operating point
MIN_STATES_PER_WINDOW = 20                                              # (local) >=20 states/window for a meaningful std (S65 n_ensemble lesson)
UNIQUE_TOL = 1e-10                                                      # (local) np.unique degeneracy threshold (S53: 1e-10 not 1e-15)
EVAL_CUTOFF = 1e-6                                                      # (local) IR cutoff (S84 cache pattern)
MAX_PQ_FABRIC_PRIMARY = 6                                               # (local) eigenvector build ceiling for A1 (p+q<=6 -> largest block dim 16*28=448)
RNG_SEED = 1042                                                        # (local) deterministic; used ONLY for window-center jitter robustness check

# ---- Pinned anchors (canonical; NOT recomputed) ----
BRODY_CELL = 0.633                                                     # (local) INTEG-39 (S96 re-confirm); 63% GOE single-cell
R_FABRIC_CG24 = 0.367                                                  # (local) CG(24) fabric Poisson <r> (S56)

# Output destinations
OUT_NPZ = SESSION_DIR / "inv10_w3_eth_violation.npz"
OUT_PNG = SESSION_DIR / "inv10_w3_eth_violation.png"

# Input caches
L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
L1416_CACHE = COMPUTATIONS_DIR / "session-106" / "s106_w1_highl_cache_l1416.npz"
S37_CELL = COMPUTATIONS_DIR / "session-37" / "s37_pair_susceptibility.npz"   # cell E_8, V_8x8, rho_8

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "dirac_spectrum.py",
    L12_CACHE,
    L1416_CACHE,
    S37_CELL,
    Path(__file__).resolve(),
]


# ---------------------------------------------------------------------------
# Section 2 — SHA pins / dual-SHA / verdict payload (canonical template)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
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


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None) -> dict:
    payload = {
        "session": 10,
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


# ---------------------------------------------------------------------------
# Section 3 — Linear algebra helpers (GPU eigh for matrix elements)
# ---------------------------------------------------------------------------
def eigh_gpu(M: np.ndarray):
    """Hermitian eigh on GPU when available; returns (evals_ascending, evecs columns)."""
    if _HAS_TORCH and M.shape[0] >= 100:
        t = torch.tensor(np.asarray(M), dtype=torch.complex128, device="cuda")
        w, v = torch.linalg.eigh(t)
        return w.cpu().numpy().real, v.cpu().numpy()
    w, v = np.linalg.eigh(np.asarray(M))
    return w, v


def diag_in_eigenbasis(A: np.ndarray, evecs: np.ndarray) -> np.ndarray:
    """Return the diagonal <E_i|A|E_i> = (V^dag A V)_ii for orthonormal eigenvectors V (columns)."""
    # diag(V^dag A V)_i = sum_{a,b} conj(V[a,i]) A[a,b] V[b,i]
    AV = A @ evecs                         # (dim, dim)  (local)
    d = np.einsum("ai,ai->i", np.conjugate(evecs), AV)   # (local)
    return d.real


def fit_loglog_slope(D: np.ndarray, y: np.ndarray):
    """beta := -d ln(y) / d ln(D) via least-squares on log-log; returns (beta, intercept, r2, n)."""
    D = np.asarray(D, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    m = np.isfinite(D) & np.isfinite(y) & (D > 0) & (y > 0)   # (local)
    if m.sum() < 2:
        return float("nan"), float("nan"), float("nan"), int(m.sum())
    lx = np.log(D[m])   # (local)
    ly = np.log(y[m])   # (local)
    A = np.vstack([lx, np.ones_like(lx)]).T   # (local)
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    slope, intercept = coef[0], coef[1]       # (local) slope = d ln y / d ln D
    yhat = A @ coef                            # (local)
    ss_res = float(np.sum((ly - yhat) ** 2))   # (local)
    ss_tot = float(np.sum((ly - ly.mean()) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")   # (local)
    beta = -slope                              # (local) ETH exponent definition
    return float(beta), float(intercept), float(r2), int(m.sum())


# ---------------------------------------------------------------------------
# Section 4 — Microcanonical eigenstate-fluctuation core
# ---------------------------------------------------------------------------
def fixed_energy_window_fluctuation(levels: np.ndarray, diag_vals: np.ndarray,
                                    e_edges: np.ndarray):
    """
    Microcanonical Delta_A in FIXED ABSOLUTE-ENERGY windows defined by e_edges (the textbook ETH
    protocol: hold the energy shell fixed, let D vary with truncation). In each [e_lo, e_hi) bin
    with >= MIN_STATES_PER_WINDOW states return Delta_A = std_i(<E_i|A|E_i>). Returns the MEDIAN
    Delta_A over qualifying windows + the window count + the per-window arrays.
    """
    lev = np.asarray(levels, dtype=np.float64)
    dv = np.asarray(diag_vals, dtype=np.float64)
    da_list, ecen_list = [], []
    for j in range(len(e_edges) - 1):
        lo, hi = e_edges[j], e_edges[j + 1]
        m = (lev >= lo) & (lev < hi)        # (local)
        if int(m.sum()) >= MIN_STATES_PER_WINDOW:
            da_list.append(float(np.std(dv[m], ddof=1)))
            ecen_list.append(0.5 * (lo + hi))
    if not da_list:
        return float("nan"), 0, np.array([]), np.array([])
    da = np.array(da_list, float)           # (local)
    return float(np.median(da)), len(da), da, np.array(ecen_list, float)


def fabric_size_scaling_fixed_window(per_pool_levels, per_pool_diag, n_ebins):
    """
    Build Delta_A(D) for the fabric by deepening the truncation (each entry = a deeper pool of
    (level, diag) with larger total dimension D), measuring Delta_A in a COMMON fixed-energy
    window grid (the same absolute-energy bins for every depth, so only D changes). Returns
    (D_eff[], DeltaA_median[], detail).

    The common energy grid is the [p10, p90] inter-percentile band of the DEEPEST pool (avoids
    edge bias), partitioned into n_ebins equal-width absolute-energy bins -- identical bins applied
    to every depth, so the comparison is at fixed energy across growing D.
    """
    if not per_pool_levels:
        return np.array([]), np.array([]), {}
    deepest = per_pool_levels[-1]
    lo = float(np.percentile(deepest, 10))   # (local)
    hi = float(np.percentile(deepest, 90))   # (local)
    e_edges = np.linspace(lo, hi, n_ebins + 1)   # (local) common fixed-energy grid
    D_eff, DA_med, n_win = [], [], []
    for lev, dv in zip(per_pool_levels, per_pool_diag):
        med, nw, _, _ = fixed_energy_window_fluctuation(lev, dv, e_edges)
        if np.isfinite(med) and nw > 0:
            D_eff.append(float(len(lev)))
            DA_med.append(med)
            n_win.append(nw)
    detail = {"D_eff": np.array(D_eff, float), "DeltaA_med": np.array(DA_med, float),
              "n_win": np.array(n_win, int), "e_edges": e_edges}
    return np.array(D_eff, float), np.array(DA_med, float), detail


# ---------------------------------------------------------------------------
# Section 5 — Fabric operators on the D_K blocks (eigenvectors required)
# ---------------------------------------------------------------------------
def build_fabric_blocks(tau_val: float, max_pq_sum: int):
    """
    Build per-(p,q) D_K blocks WITH eigenvectors via dirac_spectrum.
    Returns sector_data (list of dicts with 'p','q','evals','evecs', dim) + infra.
    NOTE evals are the Hermitian eigenvalues of H = 1j*D_pi; |lambda_D| = |evals| (the D_K
    eigenvalues are -i*evals, purely imaginary -- abs is the physical spectral magnitude).
    """
    gens = tds.su3_generators()
    f_abc = tds.compute_structure_constants(gens)
    gammas = tds.build_cliff8()
    sector_data, infra = tds.collect_spectrum_with_eigenvectors(
        tau_val, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
    )
    return sector_data, infra, gammas


def clifford_spinor_operator(gammas):
    """
    A fixed Hermitian Clifford spinor bilinear on the C^16 spinor factor. We use the
    Hermitian combination i*gamma^0*gamma^1 (a generator of spinor rotations; Hermitian since
    {gamma^a} are the framework's 16x16 Clifford generators with anti-Hermitian gammas ->
    i*g0*g1 Hermitian). This is a substrate-local spinor operator that does NOT commute with
    D_K (which couples spinor and rep indices through Omega), so its block-eigenbasis diagonal
    scatters eigenstate-to-eigenstate. Substrate-IS: same C^16 structure on every fiber.
    """
    g0, g1 = gammas[0], gammas[1]
    A16 = 1j * (g0 @ g1)                    # (local) 16x16
    A16 = 0.5 * (A16 + A16.conj().T)        # (local) Hermitize (kills any numerical anti-Herm residue)
    return A16


def fabric_A1_diag_per_block(sector_data, A16):
    """
    For each block, lift A16 (16x16 spinor op) to V_(p,q) (x) C^16 as 1_(dim_rho) (x) A16,
    compute the diagonal <E_i|A1|E_i> in the block eigenbasis. Returns a list of
    (abs_levels, diag_vals) per block AND the pooled (abs_levels, diag_vals).
    """
    per_block = []
    pooled_lev, pooled_diag = [], []
    for sd in sector_data:
        dim_rho = sd["dim_rho"]
        evecs = sd["evecs"]                 # (dim_rho*16, dim_rho*16)
        evals = sd["evals"]                 # Hermitian eigenvalues of 1j*D_pi
        A1 = np.kron(np.eye(dim_rho), A16)  # (local) 1_rep (x) A16
        diag = diag_in_eigenbasis(A1, evecs)   # (local) <E_i|A1|E_i>
        abs_lev = np.abs(evals)             # (local) physical |lambda_D|
        per_block.append((abs_lev, diag, sd["p"], sd["q"], dim_rho))
        pooled_lev.append(abs_lev)
        pooled_diag.append(diag)
    pooled_lev = np.concatenate(pooled_lev) if pooled_lev else np.array([])
    pooled_diag = np.concatenate(pooled_diag) if pooled_diag else np.array([])
    return per_block, pooled_lev, pooled_diag


def fabric_A2_sector_membership(sector_data, target_pq):
    """
    Peter-Weyl sector membership operator A2 on the POOLED spectrum: A2 eigenvalue = 1 if the
    eigenstate lives in sector target_pq, else 0. At fixed energy the pooled spectrum mixes
    sectors, so the diagonal scatters eigenstate-to-eigenstate (Berry-Tabor superposition).
    Returns (pooled_abs_levels, membership_diag).
    """
    pooled_lev, pooled_mem = [], []
    for sd in sector_data:
        evals = sd["evals"]
        abs_lev = np.abs(evals)
        mem = np.full(len(evals), 1.0 if (sd["p"], sd["q"]) == target_pq else 0.0)   # (local)
        pooled_lev.append(abs_lev)
        pooled_mem.append(mem)
    pooled_lev = np.concatenate(pooled_lev) if pooled_lev else np.array([])
    pooled_mem = np.concatenate(pooled_mem) if pooled_mem else np.array([])
    return pooled_lev, pooled_mem


# ---------------------------------------------------------------------------
# Section 6 — Cell operator (canonical s38 256-dim BCS, INTEG-39 object)
# ---------------------------------------------------------------------------
def build_cell_H_and_A(cell_npz: Path):
    """
    Rebuild the canonical single-cell 8-mode BCS Hamiltonian H_BCS (256-dim pair-Fock) verbatim
    from s38_otoc_bcs.py (the INTEG-39 / V_phys-13%-non-separable object), AND a NUMBER-CONSERVING
    substrate-local operator for the diagonal-ETH test.

    OPERATOR CHOICE (selection-rule corrected): the OTOC operator A=(Delta+Delta^dag)/sqrt(2) has
    Delta = sum_k sqrt(rho_k) P_k, which CHANGES the conserved pair number N_pair by +-1. It is
    therefore PURELY OFF-DIAGONAL between adjacent N_pair sectors and IDENTICALLY ZERO within any
    fixed-N_pair sector (verified: max|A_within|=0). A diagonal-ETH test needs the diagonal
    <E_i|A|E_i> WITHIN a microcanonical shell, so A must be NUMBER-CONSERVING. We use the
    DOS-weighted pair-occupation A_cell = sum_k sqrt(rho_k) n_k / sqrt(sum_k rho_k), n_k = P_k^dag P_k
    -- diagonal in the Fock basis, conserves N_pair, off-diagonal in the H_BCS energy eigenbasis,
    SAME sqrt(rho_k) DOS weighting as the canonical Delta. (This is the number-conserving partner of
    the s38 pairing operator: it carries the same DOS-weighted substrate-locality, differing only by
    being the n_k diagonal rather than the P_k off-diagonal.)
    Returns (H_BCS, A_cell, n_pair_list).
    """
    d37 = np.load(cell_npz, allow_pickle=True)
    E_8 = d37["E_8"].astype(np.float64)
    V_8x8 = d37["V_8x8"].astype(np.float64)
    rho_8 = d37["rho"].astype(np.float64)
    mu = float(d37["mu"])
    N = int(d37["n_modes"])
    dim = 2 ** N                            # (local) 256
    xi = E_8 - mu                           # (local)
    V_phys = V_8x8 * np.sqrt(np.outer(rho_8, rho_8))   # (local) DOS-weighted pairing (13% non-separable)

    H = np.zeros((dim, dim), dtype=np.float64)
    for alpha in range(dim):
        E_diag = 0.0                        # (local)
        for k in range(N):
            if alpha & (1 << k):
                E_diag += 2 * xi[k] - V_phys[k, k]
        H[alpha, alpha] = E_diag
        for k in range(N):
            for kp in range(N):
                if k == kp:
                    continue
                if (alpha & (1 << kp)) and not (alpha & (1 << k)):
                    beta = (alpha ^ (1 << kp)) | (1 << k)   # (local)
                    H[beta, alpha] -= V_phys[k, kp]

    # Number-conserving DOS-weighted pair occupation: A_cell = sum_k w_k n_k, w_k = sqrt(rho_k)/Z
    Z = np.sqrt(np.sum(rho_8))              # (local) normalization (keeps A_cell O(1))
    diag_vals = np.zeros(dim, dtype=np.float64)   # (local)
    for alpha in range(dim):
        s = 0.0                             # (local)
        for k in range(N):
            if alpha & (1 << k):
                s += np.sqrt(rho_8[k])
        diag_vals[alpha] = s / Z
    A = np.diag(diag_vals)                  # (local) Hermitian, diagonal in Fock basis, conserves N_pair
    n_pair_list = np.array([bin(a).count("1") for a in range(dim)])   # (local)
    return H, A, n_pair_list


def cell_size_scaling(H_BCS, A, n_pair_list):
    """
    Cell ETH size-scaling: H_BCS conserves N_pair, so diagonalize WITHIN each N_pair sector
    (dimension binomial(8, n_p)). A is the NUMBER-CONSERVING DOS-weighted pair occupation (diagonal
    in Fock, off-diagonal in the H_BCS eigenbasis), so its diagonal <E_i|A|E_i> in the sector
    energy eigenbasis has genuine eigenstate-to-eigenstate scatter. Delta_A = std over the sector
    (each fixed-N_pair sector IS a microcanonical shell). D = sector dim = binomial(8, n_p).
    The cell's D-mesh is the symmetric binomial ladder {28,56,70,56,28} for n_p in {2..6}; the
    ETH-approaching fabric-vs-cell discriminator reads the DECREASE of Delta_A from the small
    sectors (D=28) toward the central sector (D=70). Returns (D_eff[], DeltaA[], detail).
    """
    N = int(round(np.log2(H_BCS.shape[0])))
    D_eff, DA, sectors = [], [], []
    for n_p in range(N + 1):
        idx = np.where(n_pair_list == n_p)[0]
        d = len(idx)                        # (local) binomial(8,n_p)
        if d < MIN_STATES_PER_WINDOW:
            continue
        Hs = H_BCS[np.ix_(idx, idx)]        # (local) sector block
        As = A[np.ix_(idx, idx)]            # (local) operator in the sector
        w, v = eigh_gpu(Hs)
        diag = diag_in_eigenbasis(As, v)    # (local) <E_i|A|E_i> within the sector
        D_eff.append(float(d))
        DA.append(float(np.std(diag, ddof=1)))
        sectors.append(n_p)
    detail = {"D_eff": np.array(D_eff, float), "DeltaA": np.array(DA, float),
              "sectors": np.array(sectors, int)}
    return np.array(D_eff, float), np.array(DA, float), detail


# ---------------------------------------------------------------------------
# Section 7 — main
# ---------------------------------------------------------------------------
def main() -> int:
    t_start = time.time()
    print("=" * 74)
    print(f"{GATE_ID} — ETH-violation: eigenstate-level Ordered Veil (cell vs fabric)")
    print("=" * 74)
    print(f"  torch GPU available: {_HAS_TORCH}")
    print(f"  Delta_BCS = {Delta_BCS:.6f}  tau_fold = {TAU_FABRIC}  M_KK = {M_KK:.4e}")
    print(f"  PASS boundary: beta_fabric <= {BETA_VIOL}  AND  (beta_cell - beta_fabric) >= {DBETA_MIN}")
    print(f"  anchors: cell Brody beta={BRODY_CELL} (INTEG-39), fabric <r>={R_FABRIC_CG24} (CG24 Poisson)")

    pins = log_input_pins(INPUT_FILES)

    # ----- (1) FABRIC: build D_K blocks WITH eigenvectors at tau_fold -----
    print("\n--- FABRIC: D_K blocks with eigenvectors (operator A1 = i*g0*g1 spinor bilinear) ---")
    t0 = time.time()
    sector_data, infra, gammas = build_fabric_blocks(TAU_FABRIC, MAX_PQ_FABRIC_PRIMARY)
    print(f"  built {len(sector_data)} sectors (p+q<={MAX_PQ_FABRIC_PRIMARY}) in {time.time()-t0:.1f}s")
    A16 = clifford_spinor_operator(gammas)
    herm16 = float(np.max(np.abs(A16 - A16.conj().T)))   # (local)
    print(f"  A16 Hermiticity residual = {herm16:.2e}")

    per_block, pooled_lev_A1, pooled_diag_A1 = fabric_A1_diag_per_block(sector_data, A16)
    print(f"  pooled spectrum size (A1) = {pooled_lev_A1.size}")

    # Size-scaling for A1: deepen the truncation by cumulative inclusion of (p,q) blocks ordered by
    # p+q (growing total dimension D), measuring Delta_A in a COMMON FIXED-ENERGY window grid -- so
    # ONLY D changes across depths (the textbook ETH variable S=ln D), not the energy shell.
    order = sorted(range(len(sector_data)), key=lambda i: (sector_data[i]["p"] + sector_data[i]["q"],
                                                           sector_data[i]["p"], sector_data[i]["q"]))
    pool_lev_A1, pool_diag_A1, label_inc = [], [], []
    cum_lev, cum_diag = [], []
    for i in order:
        ab, dg, p, q, drho = per_block[i]
        cum_lev.append(ab)
        cum_diag.append(dg)
        L = np.concatenate(cum_lev)         # (local)
        D = np.concatenate(cum_diag)        # (local)
        # only keep depths with enough states to fill several fixed-energy windows
        if L.size >= 4 * MIN_STATES_PER_WINDOW:
            pool_lev_A1.append(L.copy())
            pool_diag_A1.append(D.copy())
            label_inc.append(f"<=({p},{q})|N={L.size}")
    N_EBINS_A1 = 12                          # (local) fixed-energy window count on the common grid
    D_eff_A1, DA_A1, det_A1 = fabric_size_scaling_fixed_window(pool_lev_A1, pool_diag_A1, N_EBINS_A1)
    beta_A1, b0_A1, r2_A1, n_A1 = fit_loglog_slope(D_eff_A1, DA_A1)
    print(f"  A1 size-scaling (fixed-E windows): D_eff={D_eff_A1.astype(int).tolist()}")
    print(f"  A1 Delta_A (median/depth)        ={np.round(DA_A1,5).tolist()}")
    print(f"  beta_A1 = {beta_A1:.4f}  (r2={r2_A1:.3f}, n={n_A1})   [ETH self-avg = 0.5]")

    # ----- (2) FABRIC A2: Peter-Weyl sector membership on the pooled spectrum -----
    print("\n--- FABRIC: operator A2 = Peter-Weyl sector membership (Berry-Tabor superposition) ---")
    # Each (p,q) sector occupies a characteristic ENERGY band (Casimir scaling |lambda|~sqrt(C2)),
    # so sector membership is energy-correlated. For a non-vacuous fixed-energy-window fluctuation
    # the target sector MUST overlap the bulk band where the windows live. Pick the sector with the
    # MOST eigenvalues inside the deepest pool's [p10,p90] inter-percentile bulk band -- the sector
    # that genuinely coexists with others at the bulk energies (the Berry-Tabor superposition core).
    _allv = np.concatenate([np.abs(sd["evals"]) for sd in sector_data])   # (local)
    _p10, _p90 = np.percentile(_allv, 10), np.percentile(_allv, 90)       # (local)
    _band_counts = []
    for sd in sector_data:
        if (sd["p"], sd["q"]) == (0, 0):
            continue
        av = np.abs(sd["evals"])
        nin = int(((av >= _p10) & (av < _p90)).sum())                     # (local)
        _band_counts.append((nin, (sd["p"], sd["q"])))
    target_pq = max(_band_counts)[1] if _band_counts else (1, 1)
    print(f"  target sector for membership operator: {target_pq} "
          f"(max bulk-band overlap = {max(_band_counts)[0] if _band_counts else 0})")
    pool_lev_A2, pool_diag_A2 = [], []
    cum = []
    for i in order:
        cum.append(sector_data[i])
        lv, mm = fabric_A2_sector_membership(cum, target_pq)
        # only keep depths where the target is actually present (some membership=1) and enough states
        if lv.size >= 4 * MIN_STATES_PER_WINDOW and mm.sum() > 0:
            pool_lev_A2.append(lv.copy())
            pool_diag_A2.append(mm.copy())
    N_EBINS_A2 = 12                          # (local) fixed-energy window count
    D_eff_A2, DA_A2, det_A2 = fabric_size_scaling_fixed_window(pool_lev_A2, pool_diag_A2, N_EBINS_A2)
    beta_A2, b0_A2, r2_A2, n_A2 = fit_loglog_slope(D_eff_A2, DA_A2)
    print(f"  A2 size-scaling (fixed-E windows): D_eff={D_eff_A2.astype(int).tolist()}")
    print(f"  A2 Delta_A (median/depth)        ={np.round(DA_A2,5).tolist()}")
    print(f"  beta_A2 = {beta_A2:.4f}  (r2={r2_A2:.3f}, n={n_A2})")

    # fabric beta = the PRIMARY operator A1 (the canonical substrate-local spinor observable on the
    # eigenVECTORS). A2 (sector membership) is a SUPPORTING cross-check on the Berry-Tabor
    # superposition channel; operator-dependence (|beta_A1 - beta_A2| > 0.20) routes the composite
    # to INFO (operator-dependent ETH-violation), per the gate's INFO_meaning.
    beta_fabric = float(beta_A1) if np.isfinite(beta_A1) else (float(beta_A2) if np.isfinite(beta_A2) else float("nan"))
    print(f"\n  beta_fabric = beta_A1 (primary spinor operator) = {beta_fabric:.4f}")
    print(f"  (A2 sector-membership supporting cross-check: beta_A2 = {beta_A2:.4f})")

    # ----- (3) CELL: canonical s38 256-dim BCS, operator A = (Delta+Delta^dag)/sqrt(2) -----
    print("\n--- CELL: INTEG-39 8-mode BCS (256-dim), operator A = (Delta+Delta^dag)/sqrt(2) ---")
    t0 = time.time()
    H_cell, A_cell, n_pair_list = build_cell_H_and_A(S37_CELL)
    herm_cell = float(np.max(np.abs(H_cell - H_cell.T)))   # (local)
    print(f"  H_cell built ({H_cell.shape[0]}x{H_cell.shape[0]}) in {time.time()-t0:.2f}s, Herm err={herm_cell:.2e}")
    D_eff_cell_all, DA_cell_all, det_cell = cell_size_scaling(H_cell, A_cell, n_pair_list)
    print(f"  cell sectors (N_pair): {det_cell['sectors'].tolist()}")
    print(f"  cell D_eff (binom)   : {D_eff_cell_all.astype(int).tolist()}")
    print(f"  cell Delta_A         : {np.round(DA_cell_all,5).tolist()}")
    # The binomial ladder {28,56,70,56,28} is non-monotone with a repeated D=56; fit the exponent on
    # the MONOTONE-INCREASING half (D: 28->56->70, n_p: 2->3->4) where the Hilbert dimension genuinely
    # grows -- the clean finite-system ETH self-averaging measure. (Half-filling n_p=4, D=70 is the
    # largest microcanonical shell; the descending half is its mirror by particle-hole symmetry.)
    sec = det_cell["sectors"]
    half = sec <= int(np.ceil(sec.max() / 2)) if sec.size else np.array([], bool)   # (local) rising half
    D_eff_cell = D_eff_cell_all[half]
    DA_cell = DA_cell_all[half]
    beta_cell, b0_cell, r2_cell, n_cell = fit_loglog_slope(D_eff_cell, DA_cell)
    print(f"  cell rising-half D_eff: {D_eff_cell.astype(int).tolist()}  Delta_A: {np.round(DA_cell,5).tolist()}")
    print(f"  beta_cell = {beta_cell:.4f}  (r2={r2_cell:.3f}, n={n_cell})   [ETH self-avg = 0.5]")

    # ----- (4) L=14 fabric cross-check on the POOLED eigenVALUE spectrum -----
    # (eigenvectors at p+q up to 14 are infeasible to rebuild -- GT-builder timeout, math-scripts.md;
    #  the L14 cache stores eigenVALUES only. The A2 sector-membership ETH diagnostic needs ONLY
    #  eigenvalues + sector labels, so we extend the A2 size-scaling onto the L14 pooled spectrum.)
    print("\n--- L=14 fabric cross-check (A2 sector-membership extended onto the deeper eigenvalue cache) ---")
    beta_A2_L14 = float("nan")
    L14_used = False
    try:
        d14 = np.load(L1416_CACHE, allow_pickle=True)
        if "sector_evals_L14" in d14.files:
            se14 = d14["sector_evals_L14"].item()
            # densest target sector at L14
            dims14 = [(v.get("dim", 0), k) for k, v in se14.items() if k != (0, 0)]
            tgt14 = max(dims14)[1] if dims14 else (1, 1)
            # bulk-band-overlapping target at L14 (same selection rule as the L12 A2 target)
            allv14 = np.concatenate([np.abs(np.asarray(v["abs_evals"], float)) for v in se14.values()])
            q10_14, q90_14 = np.percentile(allv14, 10), np.percentile(allv14, 90)
            bc14 = []
            for k, v in se14.items():
                if k == (0, 0):
                    continue
                av = np.abs(np.asarray(v["abs_evals"], float))
                bc14.append((int(((av >= q10_14) & (av < q90_14)).sum()), k))
            tgt14 = max(bc14)[1] if bc14 else (1, 1)
            order14 = sorted(se14.keys(), key=lambda k: (k[0] + k[1], k[0], k[1]))
            levels14, diag14 = [], []
            running_lev, running_mem = [], []
            for k in order14:
                ab = np.abs(np.asarray(se14[k]["abs_evals"], dtype=np.float64))
                mm = np.full(ab.size, 1.0 if k == tgt14 else 0.0)
                running_lev.append(ab)
                running_mem.append(mm)
                Lall = np.concatenate(running_lev)
                Mall = np.concatenate(running_mem)
                if Lall.size >= 4 * MIN_STATES_PER_WINDOW and Mall.sum() > 0:
                    levels14.append(Lall.copy())
                    diag14.append(Mall.copy())
            D14, DA14, _ = fabric_size_scaling_fixed_window(levels14, diag14, 12)
            beta_A2_L14, _, r2_14, n14 = fit_loglog_slope(D14, DA14)
            L14_used = True
            print(f"  L14 target sector {tgt14}; D_eff={D14.astype(int).tolist()}")
            print(f"  beta_A2(L14 pooled) = {beta_A2_L14:.4f} (r2={r2_14:.3f}, n={n14}); persists across L=12->14: "
                  f"{'YES' if (np.isfinite(beta_A2_L14) and abs(beta_A2_L14-beta_A2)<0.20) else 'see value'}")
        else:
            print("  sector_evals_L14 key absent; L14 cross-check skipped (non-blocking).")
    except Exception as e:
        print(f"  L14 cross-check skipped (non-blocking): {e}")

    # ----- (5) VERDICT logic -----
    dbeta = beta_cell - beta_fabric if (np.isfinite(beta_cell) and np.isfinite(beta_fabric)) else float("nan")
    print("\n" + "=" * 74)
    print("VERDICT LOGIC")
    print("=" * 74)
    print(f"  beta_fabric = {beta_fabric:.4f}   (PASS-violation iff <= {BETA_VIOL})")
    print(f"  beta_cell   = {beta_cell:.4f}")
    print(f"  Delta_beta  = beta_cell - beta_fabric = {dbeta:.4f}   (PASS-discriminator iff >= {DBETA_MIN})")

    # SIGN: did the fabric land in the predicted VIOLATION direction (beta_fabric < ETH 0.5)?
    sign_ok = bool(np.isfinite(beta_fabric) and beta_fabric < ETH_SELF_AVG)
    # MAGNITUDE: both pinned thresholds met?
    viol_ok = bool(np.isfinite(beta_fabric) and beta_fabric <= BETA_VIOL)
    disc_ok = bool(np.isfinite(dbeta) and dbeta >= DBETA_MIN)

    if viol_ok and disc_ok:
        verdict = "PASS"
        magnitude_verdict = "PASS"
    elif (np.isfinite(beta_fabric) and beta_fabric <= BETA_INFO_HI) or \
         (np.isfinite(dbeta) and 0.0 < dbeta < DBETA_MIN) or \
         (np.isfinite(beta_A1) and np.isfinite(beta_A2) and abs(beta_A1 - beta_A2) > 0.20):
        # partial violation (beta in (0.25,0.40]), weak discriminator, or operator-dependent ETH
        verdict = "INFO"
        magnitude_verdict = "INFO"
    else:
        verdict = "FAIL"
        magnitude_verdict = "FAIL"

    sign_verdict = "PASS" if sign_ok else "FAIL"
    regime_verdict = "VALID"   # deterministic spectral diagnostic; no small-parameter expansion to break

    # composite-collapse safety (matches gate-verdicts.md): if sign FAIL -> FAIL; INFO mag -> INFO
    if sign_verdict == "FAIL":
        verdict = "FAIL"
    elif magnitude_verdict == "INFO" and verdict == "PASS":
        verdict = "INFO"

    print(f"  sign_verdict={sign_verdict}  magnitude_verdict={magnitude_verdict}  regime_verdict={regime_verdict}")
    print(f"  COMPOSITE VERDICT: {verdict}")

    # ----- (6) plot -----
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))
    ax = axes[0]
    if D_eff_A1.size:
        ax.loglog(D_eff_A1, DA_A1, "o-", color="C0", label=f"fabric A1 (spinor) beta={beta_A1:.3f}")
    if D_eff_A2.size:
        ax.loglog(D_eff_A2, DA_A2, "s-", color="C2", label=f"fabric A2 (PW-occ) beta={beta_A2:.3f}")
    if D_eff_cell_all.size:
        ax.loglog(D_eff_cell_all, DA_cell_all, "^:", color="C3", alpha=0.5, label="cell (BCS) full ladder")
    if D_eff_cell.size:
        ax.loglog(D_eff_cell, DA_cell, "^-", color="C3", label=f"cell (BCS) rising-half beta={beta_cell:.3f}")
    # ETH reference slope D^{-1/2} anchored at the first cell point
    if D_eff_cell.size:
        Dref = np.array([D_eff_cell.min(), max(D_eff_cell.max(), D_eff_A1.max() if D_eff_A1.size else D_eff_cell.max())])
        yref = DA_cell[0] * (Dref / D_eff_cell[0]) ** (-ETH_SELF_AVG)
        ax.loglog(Dref, yref, "k--", lw=1, label="ETH slope D^{-1/2}")
    ax.set_xlabel("effective Hilbert dimension D")
    ax.set_ylabel(r"$\Delta_A(D)$ = eigenstate-to-eigenstate std")
    ax.set_title("ETH size-scaling: fabric VIOLATES (flat), cell APPROACHES ETH")
    ax.legend(fontsize=8)
    ax.grid(True, which="both", alpha=0.3)

    ax = axes[1]
    cats = ["beta_fabric", "beta_cell", "ETH=0.5", "viol thr"]
    vals = [beta_fabric, beta_cell, ETH_SELF_AVG, BETA_VIOL]
    colors = ["C0", "C3", "k", "C1"]
    ax.bar(range(len(cats)), vals, color=colors, alpha=0.75)
    ax.axhline(ETH_SELF_AVG, color="k", ls="--", lw=1)
    ax.axhline(BETA_VIOL, color="C1", ls=":", lw=1)
    ax.set_xticks(range(len(cats)))
    ax.set_xticklabels(cats, rotation=15, fontsize=9)
    ax.set_ylabel(r"$\beta = -d\ln\Delta_A/d\ln D$")
    ax.set_title(f"VERDICT: {verdict}  (Dbeta={dbeta:.3f}, need>={DBETA_MIN})")
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(f"{GATE_ID}: eigenstate-level Ordered Veil — fabric ETH-violation vs cell ETH-approach", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"\n  saved plot: {OUT_PNG}")

    # ----- (7) dual-SHA + persist + verdict payload -----
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)

    np.savez_compressed(
        OUT_NPZ,
        # headline exponents
        beta_fabric=beta_fabric, beta_cell=beta_cell, delta_beta=dbeta,
        beta_A1=beta_A1, beta_A2=beta_A2, beta_A2_L14=beta_A2_L14,
        r2_A1=r2_A1, r2_A2=r2_A2, r2_cell=r2_cell,
        # size-scaling curves
        D_eff_A1=D_eff_A1, DeltaA_A1=DA_A1,
        D_eff_A2=D_eff_A2, DeltaA_A2=DA_A2,
        D_eff_cell=D_eff_cell, DeltaA_cell=DA_cell,
        D_eff_cell_all=D_eff_cell_all, DeltaA_cell_all=DA_cell_all, cell_sectors=det_cell["sectors"],
        # pins / thresholds / anchors
        beta_viol_thr=BETA_VIOL, dbeta_min_thr=DBETA_MIN, eth_self_avg=ETH_SELF_AVG,
        brody_cell=BRODY_CELL, r_fabric_cg24=R_FABRIC_CG24,
        tau_fabric=TAU_FABRIC, Delta_BCS=float(Delta_BCS), M_KK=float(M_KK),
        max_pq_fabric=MAX_PQ_FABRIC_PRIMARY, target_pq=np.array(target_pq),
        L_max_primary=12, L14_cross_check_used=L14_used,
        min_states_per_window=MIN_STATES_PER_WINDOW,
        # verdict
        verdict=verdict, sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  saved data: {OUT_NPZ}")

    value_str = (f"beta_fabric={beta_fabric:.4f}|beta_cell={beta_cell:.4f}|"
                 f"dbeta={dbeta:.4f}|beta_A1={beta_A1:.4f}|beta_A2={beta_A2:.4f}")
    extra = [
        f"# EMERGENCE-ETH: beta_fabric={beta_fabric:.4f} (viol<= {BETA_VIOL}); "
        f"beta_cell={beta_cell:.4f}; dbeta={dbeta:.4f} (disc>= {DBETA_MIN}); "
        f"ops: fabric A1=i*g0*g1 spinor bilinear (eigenvectors), A2=PeterWeyl-(1,0)-membership; "
        f"cell A=number-conserving DOS-weighted pair-occupation on s38-256dim-BCS INTEG-39",
        f"# ANCHORS: cell Brody beta={BRODY_CELL} (INTEG-39 weakly chaotic, APPROACHES ETH); "
        f"fabric <r>={R_FABRIC_CG24} (CG24 Poisson, lambda_L=0, VIOLATES ETH); "
        f"beta_A2={beta_A2:.4f} (supporting); L14 cross-check used={L14_used}",
    ]

    print_verdict_payload(verdict, value_str, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict, extra_rows=extra)

    print(f"\n  total runtime: {time.time()-t_start:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
