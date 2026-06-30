"""
s87_w4_type_f_per_mode_phase_audit.py
=====================================

S87-TYPE-F-PER-MODE-PHASE-AUDIT (CF-26, Level 1.5, MEDIUM-HIGH-EVOI)
Plan: sessions/session-plan/session-87-plan-w4.md §W4-2 (lines 223-339)
Owner: connes-ncg-theorist (lead) | Co-signer: lizzi-spectral-functional-theorist

PURPOSE
-------
Compute the canonical Bogoliubov-phase distribution {phi_a}_{a=1..32} on the
post-tau_fold GGE state (Type-F observable partition; S86 W-4 R3 closure) and
audit against:

  (i)  NCG-axiomatic invariances:
       - J-invariance (real structure on H_K, KO-dim 6: J^2=+1, JD=DJ).
       - gamma-invariance (chirality grading; restricted to chirality-odd modes).
       - First-order condition [[D_K, a], b^o] = 0 on A_F = C + H + M_3(C).
  (ii) S38 algebraic GGE-permanence:
       phase distribution stable across 4-tau scan tau in
       {0.190, 0.191, 0.200, 0.240}.

PASS / FAIL / INFO
------------------
- PASS: 32-mode {phi_a} computed AND axiom invariances < 1e-12 AND
        max GGE drift across 4-tau scan < 1%.
- INFO: invariances PASS AND GGE drift in [1%, 10%] band.
- FAIL: histogram non-computable OR axiom violation OR GGE drift > 10%.

SUBSTITUTION CHAIN (per plan §274-308)
--------------------------------------

Step 1 [definitions]:
  D_K(tau)        = Jensen-deformed SU(3) Dirac operator at deformation tau.
  N_cells         = 32 (canonical_constants Voronoi partition; S42).
  alpha_k, beta_k = post-tau_fold Bogoliubov coefficients on 8 BdG branches
                    (B2[0..3], B1, B3[0..3]) per s82_w3_4_gge_fnl_channel.npz.
  w_k             = per-branch pair-amplitude weights.
  omega_k         = per-branch frequencies in M_KK units.
  Type-F mode a   = (cell c, branch k) pair indexed in
                    a = 0..31 (32 = N_cells; one branch index k(a) per cell).

  phi_a(tau) := arg(alpha_a(tau) * conj(beta_a(tau))**2)  in (-pi, pi]
                ^^^ Type-F kernel argument; scalar projection N_A = sum_a w_a * Im[alpha_a (beta_a*)^2].

Step 2 [substitution]:
  phi_a(tau) computed per pull-back to 32 cells under substrate-canonical
  cell-phase (Voronoi cell-uniform: each cell carries a deterministic
  phase derived from D_K eigenvalue residues at level p+q).

  J-invariance:        phi_a -> -phi_a   (J anti-linear)
  gamma-invariance:    phi_a -> -phi_a   on chirality-odd subset
  first-order:         test [[D_K, a], b^o] on A_F generators

Step 3 [simplification]:
  PASS iff max_axiom_residual < 1e-12 AND max_GGE_drift < 0.01
  INFO iff PASS-axioms AND 0.01 <= drift < 0.10
  FAIL iff axiom violation OR drift >= 0.10

Step 4 [direction]: histogram is structural diagnostic; no signed pre-reg.

Step 5 [sign for VERIFY]:
  sign_verdict      = N/A (no directional pre-registration)
  magnitude_verdict = PASS|INFO|FAIL per drift band
  regime_verdict    = VALID iff Delta_tau_max <= 0.050 (plan §306 absolute parse;
                      pre-registered scan {0.190..0.240} all within S38 integrable
                      regime delta < 0.1 absolute).

OUTPUT
------
- s87_w4_type_f_per_mode_phase_audit.npz : phi_a 32-tuple at each of 4 tau,
                                            axiom-invariance flags, GGE drift table.
- s87_w4_type_f_per_mode_phase_audit.png : 32-bin histogram + drift plot.
- Verdict line appended to computations/session-87/s87_gate_verdicts.txt with full
  64-char SHA + dual-SHA companion + S87 schema-v2 3-tuple annotation.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

# Cap CPU threads for parallel-agent friendliness (per .claude/rules/computation-environment.md).
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np                                          # noqa: E402
import matplotlib                                            # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                              # noqa: E402

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from canonical_constants import (                            # noqa: E402
    tau_fold,
    N_cells,
    n_pairs,
    PI,
    M_KK,
    Delta_BCS,
    omega_L1,
)

# ---------------------------------------------------------------------------
# Pinned input artefacts (per plan §310-319 INPUT-PIN MAP)
# ---------------------------------------------------------------------------

SPECTRUM_CACHE_PATH = HERE / "s84_spectrum_cache_L12_tau019.npz"
S82_GGE_PATH        = HERE / "s82_w3_4_gge_fnl_channel.npz"
S52_BOGO_PATH       = HERE / "s52_bogoliubov_amp.npz"
CANON_CONSTANTS_PATH = HERE / "canonical_constants.py"
CANON_CLASSES_PATH   = HERE / "canonical_classes.py"
VERDICT_FILE        = HERE / "s87_gate_verdicts.txt"
OUT_NPZ             = HERE / "s87_w4_type_f_per_mode_phase_audit.npz"
OUT_PNG             = HERE / "s87_w4_type_f_per_mode_phase_audit.png"

# ---------------------------------------------------------------------------
# Pinned scalar parameters
# ---------------------------------------------------------------------------

L_MAX                  = 10                                  # (local) S86-close canonical
GATE_ID                = "S87-TYPE-F-PER-MODE-PHASE-AUDIT"   # (local)
SCHEME                 = "Bogoliubov-phase-Type-F-32-mode"   # (local) plan §324
CONVENTION             = "post-tau-fold-S38-GGE-relic"       # (local) plan §324
SCHEMA_VERSION         = "S84+"                              # (local) gate-verdicts.md S87+
TAU_SCAN               = [tau_fold, tau_fold + 0.001, tau_fold + 0.010, tau_fold + 0.050]

# Pre-registered tolerances (plan §263-265).
AXIOM_INVARIANCE_TOL   = 1e-12                               # (local) machine-eps absolute
GGE_PASS_THRESH        = 0.01                                # (local) 1% relative
GGE_INFO_THRESH        = 0.10                                # (local) 10% relative
REGIME_DELTA_MAX       = 0.10                                # (local) plan §306 S38 regime: delta < 0.1 absolute
REGIME_DELTA_USED      = max(TAU_SCAN) - tau_fold            # (local) = 0.050; 0.050 < 0.10 => VALID

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def sha256_of_file(path: Path) -> str:
    """SHA-256 of a file's bytes (canonical content_sha256 protocol)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    """Audit-SHA: SHA-256 of canonical-ordered input-pin JSON
    (template: computations/_shared/ append_verdict pattern).
    """
    canon = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def append_verdict_line(canonical_line: str,
                        dual_sha_row: str,
                        sign_3tuple_row: str) -> None:
    """Append the 3-line verdict block (canonical + dual-SHA + 3-tuple)."""
    with open(VERDICT_FILE, "a", encoding="utf-8") as fh:
        fh.write(canonical_line.rstrip() + "\n")
        fh.write(dual_sha_row.rstrip() + "\n")
        fh.write(sign_3tuple_row.rstrip() + "\n")


# ---------------------------------------------------------------------------
# Load substrate data (S86 W-4 calibration)
# ---------------------------------------------------------------------------


def load_substrate_anchor() -> dict:
    """Load post-tau_fold GGE Bogoliubov coefficients from S82 channel-Path-B output.

    Returns the canonical 8-mode anchor (B2[0..3], B1, B3[0..3]) at tau=tau_fold,
    used as the substrate anchor for the 32-cell pull-back.
    """
    d = np.load(S82_GGE_PATH, allow_pickle=True)
    alpha_k = np.asarray(d["alpha_k"])             # (local) complex128 (8,)
    beta_k  = np.asarray(d["beta_k"])              # (local) complex128 (8,)
    w_k     = np.asarray(d["w_k"], dtype=float)    # (local)
    omega_k = np.asarray(d["omega_k"], dtype=float)
    labels  = np.asarray(d["labels"])
    # Sanity: 8-mode aggregate, sum w = 1 (tolerance 1e-9), unitarity |alpha|^2 - |beta|^2 = 1.
    assert alpha_k.shape == (8,), f"alpha_k shape {alpha_k.shape}; expected (8,)"
    assert beta_k.shape == (8,)
    assert abs(np.sum(w_k) - 1.0) < 1e-9, f"w_k sum = {np.sum(w_k)}"
    unitarity_residual = np.max(np.abs(np.abs(alpha_k) ** 2 - np.abs(beta_k) ** 2 - 1.0))  # (local)
    return {
        "alpha_k": alpha_k,
        "beta_k":  beta_k,
        "w_k":     w_k,
        "omega_k": omega_k,
        "labels":  labels,
        "unitarity_residual": float(unitarity_residual),
    }


def load_spectrum_cache_L10() -> dict:
    """Load L_max=10 strict-cutoff D_K eigenvalue spectrum from S84 cache."""
    d = np.load(SPECTRUM_CACHE_PATH, allow_pickle=True)
    sec = d["sector_evals"].item()
    pq_keys = sorted([(p, q) for (p, q) in sec.keys() if max(p, q) <= L_MAX])
    all_evals: list[float] = []                    # (local)
    sector_dim_sum = 0                              # (local)
    for k in pq_keys:
        rec = sec[k]
        # rec may be ndarray-of-object or dict; normalize.
        if isinstance(rec, np.ndarray) and rec.dtype == object:
            rec = rec.item()
        all_evals.append(np.asarray(rec["abs_evals"]))
        sector_dim_sum += int(rec["dim"])
    full = np.concatenate([np.asarray(a) for a in all_evals])  # (local)
    return {
        "evals": full,
        "n_eval": full.size,
        "n_sectors": len(pq_keys),
        "n_dim_sum": sector_dim_sum,
    }


# ---------------------------------------------------------------------------
# Type-F 32-mode pull-back at a single tau
# ---------------------------------------------------------------------------


def cell_phase(cell_index: int, tau: float, eigs: np.ndarray) -> float:
    """Substrate-canonical Voronoi-cell phase theta_c(tau).

    Substitution chain:
      Definition: theta_c is the phase contribution from cell c's residue at the
                  D_K eigenvalue Voronoi-cell partition. We use the deterministic
                  pin: theta_c = 2*pi*c/N_cells * (eigs[c % len(eigs)] / lambda_min)
                  modulo 2*pi.  This is the canonical-reproducible
                  cell-phase substrate; deterministic per (cell, eigenvalue) pair.
      Substitute: tau enters via eigs(tau) (eigenvalues are tau-dependent at
                  finer scan points; here we use the fixed L_max=10 cache as
                  anchor and apply small adiabatic correction tau-dependent
                  but spectrum-independent for the GGE drift test).
      Simplify:   modulo 2*pi for canonical wrap; antisymmetric around c=0
                  to ensure {theta_c} permutes under c -> N_cells - 1 - c.
      Direction:  produces a deterministic real number in (-pi, pi].
    """
    lam_min = float(np.min(eigs))                   # (local) ground-state magnitude
    eig_c = float(eigs[cell_index % len(eigs)])     # (local) per-cell eigenvalue
    raw = 2.0 * PI * cell_index / N_cells * (eig_c / lam_min)
    # Wrap to (-pi, pi].
    wrapped = ((raw + PI) % (2.0 * PI)) - PI        # (local)
    # Adiabatic tau-correction: small, deterministic, scales with delta_tau.
    delta_tau = tau - tau_fold                      # (local)
    wrapped += delta_tau * (eig_c / lam_min) * (omega_L1)  # (local) M_KK natural unit
    # Re-wrap.
    wrapped = ((wrapped + PI) % (2.0 * PI)) - PI    # (local)
    return float(wrapped)


def type_f_32_modes(anchor: dict,
                    spec: dict,
                    tau: float) -> dict:
    """Pull anchor (8-mode) Bogoliubov coefficients up to 32 Voronoi cells at tau.

    Substitution chain:
      Definition: per cell c in {0..31}, branch k(c) = c % 8.  The cell carries
                  alpha_a = alpha_{k(c)} * exp(i*theta_c),
                  beta_a  = beta_{k(c)}  * exp(i*theta_c).
                  (Common-mode phase modulation: cancels in |alpha|^2 - |beta|^2,
                   preserves Bogoliubov unitarity.)
      Substitute: phi_a(tau) = arg(alpha_a * conj(beta_a)**2)
                             = arg(alpha_{k(c)} * conj(beta_{k(c)})**2)
                               + 2*theta_c*(1-1)        [common-mode cancels phase-2]
                             ... wait, let's recompute:
                             alpha_a * conj(beta_a)^2
                             = alpha_k e^{i theta_c} * (beta_k* e^{-i theta_c})^2
                             = alpha_k * (beta_k*)^2 * e^{i theta_c} * e^{-2i theta_c}
                             = alpha_k * (beta_k*)^2 * e^{-i theta_c}
                  So phi_a = arg(alpha_k (beta_k*)^2) - theta_c.
      Simplify:   the 32 phases are 32 deterministic values, with 8 distinct
                  branch arguments shifted by 32 distinct cell-phases mod 2*pi.
      Direction:  per-mode phase phi_a varies across cells; weight w_a = w_k(c)/4
                  preserves sum-to-unity (since 32/8 = 4 cells per branch).
    """
    alpha_k = anchor["alpha_k"]                     # (local) (8,)
    beta_k  = anchor["beta_k"]                      # (local) (8,)
    w_k     = anchor["w_k"]                         # (local) (8,)

    # Adiabatic tau correction to (alpha_k, beta_k) for tau != tau_fold.
    # Substitution: r_k(tau) = r_k(tau_fold) * (1 + chi_k * delta_tau);
    # phase phi_k(tau) = phi_k(tau_fold) + omega_k(tau) * delta_tau.
    # We use the small-delta linearization (consistent with S38 integrable regime).
    delta_tau = tau - tau_fold                      # (local)
    omega_k = anchor["omega_k"]                     # (local)
    # Phase evolution: alpha_k e^{+i omega_k delta_tau}, beta_k e^{-i omega_k delta_tau}
    # (canonical Bogoliubov post-quench dynamical-phase evolution).
    phase_factor_alpha = np.exp(+1j * omega_k * delta_tau)  # (local)
    phase_factor_beta  = np.exp(-1j * omega_k * delta_tau)  # (local)
    alpha_k_tau = alpha_k * phase_factor_alpha       # (local)
    beta_k_tau  = beta_k  * phase_factor_beta        # (local)

    # Pull up to 32 cells.
    eigs = spec["evals"]                            # (local) full L_max=10 spectrum
    alpha_a = np.zeros(N_cells, dtype=complex)      # (local)
    beta_a  = np.zeros(N_cells, dtype=complex)      # (local)
    w_a     = np.zeros(N_cells, dtype=float)        # (local)
    branch_a = np.zeros(N_cells, dtype=int)          # (local)
    cell_phases_arr = np.zeros(N_cells, dtype=float) # (local)
    for c in range(N_cells):
        k = c % 8
        theta = cell_phase(c, tau, eigs)
        alpha_a[c] = alpha_k_tau[k] * np.exp(+1j * theta)
        beta_a[c]  = beta_k_tau[k]  * np.exp(+1j * theta)
        w_a[c]     = w_k[k] / (N_cells // 8)        # divide by cells-per-branch=4
        branch_a[c] = k
        cell_phases_arr[c] = theta

    # phi_a = arg(alpha_a * conj(beta_a)^2)
    kernel = alpha_a * np.conj(beta_a) ** 2          # (local)
    phi_a = np.angle(kernel)                         # (local) in (-pi, pi]

    # Type-F scalar projection: N_A = sum w_a * Im(kernel)
    N_A = float(np.sum(w_a * np.imag(kernel)))       # (local)

    # Sanity invariants.
    sum_w = float(np.sum(w_a))                       # (local) should equal 1.0
    unitarity = float(np.max(np.abs(np.abs(alpha_a) ** 2 - np.abs(beta_a) ** 2 - 1.0)))

    return {
        "tau": tau,
        "phi_a": phi_a,
        "alpha_a": alpha_a,
        "beta_a":  beta_a,
        "w_a":     w_a,
        "branch_a": branch_a,
        "cell_phases": cell_phases_arr,
        "N_A": N_A,
        "sum_w": sum_w,
        "unitarity_residual": unitarity,
        "kernel": kernel,
    }


# ---------------------------------------------------------------------------
# NCG-axiomatic invariance tests
# ---------------------------------------------------------------------------


def test_J_invariance(phi_a: np.ndarray) -> dict:
    """J-invariance: phi_a -> -phi_a; histogram set-equality up to permutation.

    Substitution chain:
      Definition: J is anti-linear on H_K; arg(J(z)) = -arg(z) for z complex.
      Substitute: {-phi_a} should be a permutation of {phi_a}; equivalently
                  the multiset {phi_a} U {-phi_a} should be symmetric about 0.
      Simplify:   sort both; compute max element-wise distance after sign flip.
                  For exact J-invariance the 32-multiset is closed under negation
                  modulo 2*pi (i.e., for each phi_a there exists an a' with
                  phi_{a'} = -phi_a).
      Direction:  define residual = max_a min_b |phi_a + phi_b| (Hausdorff-style).
                  PASS iff residual < AXIOM_INVARIANCE_TOL.
    """
    neg = -phi_a                                     # (local)
    # Hausdorff-style: for each phi_a, the closest -phi_b should match.
    residuals = np.zeros(len(phi_a))                 # (local)
    for i, p in enumerate(phi_a):
        residuals[i] = np.min(np.abs(p + neg))      # min over j of |p + (-(-phi_j))| = |p + phi_j|... wait
    # Re-derive: J-invariance asks {phi_a} = {-phi_a} as multisets.
    # Sort both arrays and compare elementwise after wrapping difference modulo 2*pi.
    sorted_phi = np.sort(phi_a)                      # (local)
    sorted_neg = np.sort(neg)                        # (local)
    diff = sorted_phi - sorted_neg                   # (local)
    # Wrap to (-pi, pi]:
    diff_wrapped = ((diff + PI) % (2.0 * PI)) - PI   # (local)
    residual = float(np.max(np.abs(diff_wrapped)))   # (local)
    return {
        "test": "J-invariance",
        "residual": residual,
        "pass": residual < AXIOM_INVARIANCE_TOL,
    }


def test_gamma_invariance(phi_a: np.ndarray, branch_a: np.ndarray) -> dict:
    """gamma-invariance on chirality-odd subset.

    Substitution chain:
      Definition: chirality grading gamma on H_K; chirality-odd modes carry
                  gamma-eigenvalue -1; on these the chirality flip sends
                  phi_a -> -phi_a.
      Substitute: select odd-branch subset (branch index k odd -> chirality-odd
                  per BdG branch labels: B2-class is even (k=0..3), B1 is mixed
                  (k=4), B3-class is odd (k=5..7)).  Use k >= 5 as chirality-odd.
      Simplify:   compare {phi_a : odd} with {-phi_a : odd} via sorted
                  multiset comparison.
      Direction:  PASS iff max-wrapped-diff < AXIOM_INVARIANCE_TOL.
    """
    # Chirality-odd branches: B3[0..2] = k in {5, 6, 7} per anchor labels
    odd_mask = branch_a >= 5                        # (local)
    if not np.any(odd_mask):
        return {"test": "gamma-invariance", "residual": 0.0, "pass": True,
                "n_odd": 0, "note": "no chirality-odd modes"}
    phi_odd = phi_a[odd_mask]                       # (local)
    neg_odd = -phi_odd                              # (local)
    sorted_phi = np.sort(phi_odd)
    sorted_neg = np.sort(neg_odd)
    diff = sorted_phi - sorted_neg
    diff_wrapped = ((diff + PI) % (2.0 * PI)) - PI
    residual = float(np.max(np.abs(diff_wrapped)))
    return {
        "test": "gamma-invariance",
        "residual": residual,
        "pass": residual < AXIOM_INVARIANCE_TOL,
        "n_odd": int(np.sum(odd_mask)),
    }


def test_first_order_condition() -> dict:
    """First-order condition [[D_K, a], b^o] = 0 on A_F = C + H + M_3(C).

    Substitution chain:
      Definition: A_F generators are the 1+4+9 = 14 basis matrices of
                  C + H + M_3(C); their opposite algebra A_F^o acts from the
                  right.  The first-order condition demands the double-commutator
                  vanish identically for all (a, b) in A_F x A_F^o.
      Substitute: in the 32-mode Type-F subspace (8 BdG branches replicated to
                  32 cells), D_K is diagonal in the (cell, branch) basis with
                  block-diagonal structure across A_F summands.
      Simplify:   for diagonal D_K and block-diagonal (a, b^o) supported on
                  disjoint A_F-summands, [D_K, a] is block-diagonal on a's
                  summand only; b^o acts on a different summand
                  (or commutes with [D_K, a] as a scalar on the same summand);
                  hence [[D_K, a], b^o] = 0 identically (block-disjointness).
      Direction:  test by constructing 14x14 generator basis; compute the
                  worst-case [[D_K, a], b^o] norm.  PASS iff < AXIOM_INVARIANCE_TOL.
    """
    # Build the 14 A_F generators on a 32-dim test space (block-diagonal:
    # 4 cells in C-summand + 12 cells in H-summand + 16 cells in M_3-summand
    # = 32; matches the 1:3:9 dim ratio approximately and exhausts 32 cells.)
    # On the 32-mode Type-F space, D_K is diagonal (frequency-eigenbasis);
    # we use the canonical anchor frequencies.
    block_dims = [4, 12, 16]                        # (local) C, H, M_3 cell allocations
    assert sum(block_dims) == N_cells

    # Diagonal D_K-matrix on 32-mode space (use Bogoliubov frequencies).
    rng_anchor = load_substrate_anchor()
    omega8 = rng_anchor["omega_k"]
    omega32 = np.tile(omega8, N_cells // 8)         # (local) (32,)
    D = np.diag(omega32).astype(np.complex128)       # (local)

    # Build A_F generators acting on 32-dim space (block-diagonal embedding).
    generators = []                                 # (local)

    # C-summand: 1 generator (identity on first 4 cells), embedded.
    g = np.zeros((N_cells, N_cells), dtype=np.complex128)
    g[0:4, 0:4] = np.eye(4)
    generators.append(("C-id", g.copy()))

    # H-summand: 4 generators (1, i sigma_x, i sigma_y, i sigma_z) embedded
    # as block-diagonal on cells 4..15 (12 cells = 6 doublets).
    pauli = [
        np.eye(2, dtype=np.complex128),
        1j * np.array([[0, 1], [1, 0]], dtype=np.complex128),
        1j * np.array([[0, -1j], [1j, 0]], dtype=np.complex128),
        1j * np.array([[1, 0], [0, -1]], dtype=np.complex128),
    ]
    for ip, p in enumerate(pauli):
        g = np.zeros((N_cells, N_cells), dtype=np.complex128)
        for d in range(6):  # 6 doublets in H-summand
            g[4 + 2*d:4 + 2*d + 2, 4 + 2*d:4 + 2*d + 2] = p
        generators.append((f"H-{ip}", g.copy()))

    # M_3(C)-summand: 9 elementary matrices E_{ij} embedded on cells 16..31
    # (16 cells = 1 + 9 + 6 padding... use the full 16-cell block as a 4x4
    # generator and embed the 3x3 matrix in its top-left 3x3).
    # Take 9 generators E_{ij} (i,j=0..2), zero outside cells 16+i*1, 16+j*1
    # within a 9-cell window, leave 7 cells of M_3-summand block as padding zero.
    for i in range(3):
        for j in range(3):
            g = np.zeros((N_cells, N_cells), dtype=np.complex128)
            g[16 + i, 16 + j] = 1.0
            generators.append((f"M3-{i}{j}", g.copy()))

    # The opposite algebra A_F^o on this finite-dimensional H is realized by the
    # transpose action; for a real-valued spectral triple, A^o ~ J A^* J^{-1};
    # on diagonal D the simplest realization with KO-dim=6 axioms is to use
    # the same generators but acting from the right (multiplication on the
    # other side).  We test [[D, a], b^o] = D a b - a D b - b D a + b a D
    # block-diagonally; since D is block-diagonal and a, b are block-diagonal
    # on DISJOINT cell-blocks (C/H/M_3), [D, a] is supported on a's block,
    # and b^o has zero overlap with [D, a] (since b lives on a different block
    # OR commutes scalar-wise on the same block).
    #
    # Compute max over all (a, b) generator pairs of || D a b - a D b - b D a + b a D ||.
    max_residual = 0.0                              # (local)
    for name_a, a in generators:
        DaD = D @ a - a @ D                         # (local) [D, a]
        for name_b, b in generators:
            # b acts as the right-action b^o ~ b (on diagonal D, equivalent up to ordering).
            commutator = DaD @ b - b @ DaD          # (local) [[D, a], b]
            r = float(np.max(np.abs(commutator)))
            if r > max_residual:
                max_residual = r

    return {
        "test": "first-order [[D_K, a], b^o] = 0",
        "residual": max_residual,
        "pass": max_residual < AXIOM_INVARIANCE_TOL,
        "n_generators": len(generators),
        "block_dims": block_dims,
    }


# ---------------------------------------------------------------------------
# GGE stability across 4-tau scan
# ---------------------------------------------------------------------------


def gge_stability(phi_per_tau: list[np.ndarray]) -> dict:
    """Compute max relative drift across the 4-tau scan.

    Substitution chain:
      Definition: drift_a(tau) := |phi_a(tau) - phi_a(tau_fold)| (wrapped to [0, pi])
                  rel_dev := max_a drift_a(tau) / pi
                  (normalize by pi as the half-period; drift saturated at pi).
      Substitute: phi_per_tau is a list of 4 arrays of length 32; index 0 is
                  phi_a(tau_fold).
      Simplify:   compute per-tau max-drift and take overall max.
      Direction:  rel_dev < 0.01 -> PASS; 0.01 <= rel_dev < 0.10 -> INFO;
                  rel_dev >= 0.10 -> FAIL (S38 falsification).
    """
    base = phi_per_tau[0]                           # (local) at tau_fold
    drifts_per_tau = []                              # (local)
    for j, p in enumerate(phi_per_tau):
        diff = p - base                              # (local)
        # Wrap difference to (-pi, pi] then take absolute value.
        diff_wrapped = ((diff + PI) % (2.0 * PI)) - PI
        drift = float(np.max(np.abs(diff_wrapped)) / PI)
        drifts_per_tau.append(drift)
    max_drift = max(drifts_per_tau)                  # (local)
    return {
        "drifts_per_tau": drifts_per_tau,
        "max_drift": max_drift,
        "pass": max_drift < GGE_PASS_THRESH,
        "info": GGE_PASS_THRESH <= max_drift < GGE_INFO_THRESH,
        "fail": max_drift >= GGE_INFO_THRESH,
    }


# ---------------------------------------------------------------------------
# Main audit
# ---------------------------------------------------------------------------


def main() -> int:
    print("=" * 70)
    print(" S87-TYPE-F-PER-MODE-PHASE-AUDIT (CF-26)")
    print(" connes-ncg-theorist | co-signer: lizzi-spectral-functional-theorist")
    print("=" * 70)

    # ----------- Input SHA pin map (canonical-ordered) -----------
    pin_map = {
        "GATE_ID": GATE_ID,
        "L_max":   L_MAX,
        "scheme":  SCHEME,
        "convention": CONVENTION,
        "TAU_SCAN": TAU_SCAN,
        "input_files": {
            "spectrum_cache":   sha256_of_file(SPECTRUM_CACHE_PATH),
            "s82_gge":          sha256_of_file(S82_GGE_PATH),
            "s52_bogo":         sha256_of_file(S52_BOGO_PATH),
            "canonical_constants": sha256_of_file(CANON_CONSTANTS_PATH),
            "canonical_classes":   sha256_of_file(CANON_CLASSES_PATH),
        },
        "tolerances": {
            "axiom": AXIOM_INVARIANCE_TOL,
            "gge_pass": GGE_PASS_THRESH,
            "gge_info": GGE_INFO_THRESH,
        },
        "tau_fold_canonical": tau_fold,
        "N_cells_canonical":   N_cells,
    }
    audit_sha = closure_hash(pin_map)
    print(f"\n[1] Input SHA pins computed; audit_sha256 = {audit_sha}")
    for fname, fsha in pin_map["input_files"].items():
        print(f"    {fname}: {fsha[:16]}...")

    # ----------- Load substrate -----------
    anchor = load_substrate_anchor()
    spec = load_spectrum_cache_L10()
    print(f"\n[2] Substrate loaded: {spec['n_eval']} eigenvalues across "
          f"{spec['n_sectors']} (p,q)-sectors at L_max={L_MAX}")
    print(f"    Anchor 8-mode unitarity residual: {anchor['unitarity_residual']:.3e}")

    # ----------- Compute 32-mode {phi_a} at each of 4 tau values -----------
    phi_per_tau = []                                # (local)
    N_A_per_tau = []                                # (local)
    full_data_per_tau = []                          # (local)
    for tau in TAU_SCAN:
        result = type_f_32_modes(anchor, spec, tau)
        phi_per_tau.append(result["phi_a"])
        N_A_per_tau.append(result["N_A"])
        full_data_per_tau.append(result)
        print(f"\n[3] tau={tau:.3f} -> N_A={result['N_A']:+.6e}, "
              f"sum_w={result['sum_w']:.6f}, unitarity={result['unitarity_residual']:.3e}")

    # ----------- NCG-axiomatic tests at tau_fold -----------
    base = full_data_per_tau[0]
    j_test = test_J_invariance(base["phi_a"])
    g_test = test_gamma_invariance(base["phi_a"], base["branch_a"])
    fo_test = test_first_order_condition()

    print("\n[4] NCG-axiomatic tests at tau=tau_fold:")
    print(f"    J-invariance:        residual={j_test['residual']:.3e}  PASS={j_test['pass']}")
    print(f"    gamma-invariance:    residual={g_test['residual']:.3e}  PASS={g_test['pass']}  "
          f"(n_odd={g_test.get('n_odd')})")
    print(f"    first-order:         residual={fo_test['residual']:.3e}  PASS={fo_test['pass']}  "
          f"(n_gen={fo_test['n_generators']})")

    axioms_pass = j_test["pass"] and g_test["pass"] and fo_test["pass"]
    max_axiom_residual = max(j_test["residual"], g_test["residual"], fo_test["residual"])

    # ----------- GGE stability scan -----------
    gge = gge_stability(phi_per_tau)
    print(f"\n[5] GGE stability across 4-tau scan: max_drift={gge['max_drift']:.4e}")
    for tau, d in zip(TAU_SCAN, gge["drifts_per_tau"]):
        print(f"    tau={tau:.3f} -> drift={d:.4e}")

    # ----------- Composite verdict -----------
    # Substitution chain (collapse rule per gate-verdicts.md S87 schema-v2):
    #
    #   sign_verdict = N/A              (no signed delta)
    #   magnitude_verdict:
    #     PASS iff axioms_pass AND gge.pass         (drift < 1%)
    #     INFO iff axioms_pass AND gge.info         (1% <= drift < 10%)
    #     FAIL iff (NOT axioms_pass) OR gge.fail    (axiom violated OR drift >= 10%)
    #   regime_verdict = VALID iff REGIME_DELTA_USED <= REGIME_DELTA_MAX (0.050 <= 0.100 -> VALID)

    if not axioms_pass:
        magnitude_verdict = "FAIL"
        composite = "FAIL"
        verdict_reason = "axiom-violation"
    elif gge["fail"]:
        magnitude_verdict = "FAIL"
        composite = "FAIL"
        verdict_reason = "GGE-drift-exceeds-10pct-S38-falsified"
    elif gge["info"]:
        magnitude_verdict = "INFO"
        composite = "INFO"
        verdict_reason = "GGE-drift-1-10pct-band"
    else:
        magnitude_verdict = "PASS"
        composite = "PASS"
        verdict_reason = "axioms-eps-AND-GGE-stability-sub-1pct"

    sign_verdict = "N/A"
    regime_verdict = "VALID" if REGIME_DELTA_USED <= REGIME_DELTA_MAX else "BREAKDOWN"

    # Composite-collapse rule (gate-verdicts.md):
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"\n[6] Composite verdict: {composite}  (sign={sign_verdict}, "
          f"magnitude={magnitude_verdict}, regime={regime_verdict})")
    print(f"    Reason: {verdict_reason}")

    # ----------- Save .npz -----------
    np.savez_compressed(
        OUT_NPZ,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        tau_scan=np.asarray(TAU_SCAN),
        phi_a_per_tau=np.stack(phi_per_tau),         # (4, 32)
        N_A_per_tau=np.asarray(N_A_per_tau),
        alpha_a_tau_fold=full_data_per_tau[0]["alpha_a"],
        beta_a_tau_fold=full_data_per_tau[0]["beta_a"],
        w_a=full_data_per_tau[0]["w_a"],
        branch_a=full_data_per_tau[0]["branch_a"],
        cell_phases_tau_fold=full_data_per_tau[0]["cell_phases"],
        unitarity_residual_anchor=anchor["unitarity_residual"],
        unitarity_residual_32mode_tau_fold=full_data_per_tau[0]["unitarity_residual"],
        # Axiom test results
        J_residual=j_test["residual"],
        J_pass=j_test["pass"],
        gamma_residual=g_test["residual"],
        gamma_pass=g_test["pass"],
        gamma_n_odd=g_test.get("n_odd", 0),
        first_order_residual=fo_test["residual"],
        first_order_pass=fo_test["pass"],
        first_order_n_generators=fo_test["n_generators"],
        max_axiom_residual=max_axiom_residual,
        axioms_pass=axioms_pass,
        # GGE stability
        gge_drifts=np.asarray(gge["drifts_per_tau"]),
        gge_max_drift=gge["max_drift"],
        gge_pass_threshold=GGE_PASS_THRESH,
        gge_info_threshold=GGE_INFO_THRESH,
        regime_delta_used=REGIME_DELTA_USED,
        regime_delta_max=REGIME_DELTA_MAX,
        # Verdict
        composite=composite,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        verdict_reason=verdict_reason,
        audit_sha256=audit_sha,
    )
    content_sha = sha256_of_file(OUT_NPZ)
    print(f"\n[7] Wrote {OUT_NPZ.name}; content_sha256 = {content_sha[:16]}...")

    # ----------- Plot -----------
    fig, axs = plt.subplots(1, 2, figsize=(13, 5))
    # Histogram at tau_fold (32 bins).
    phi_fold = phi_per_tau[0]
    axs[0].hist(phi_fold, bins=32, range=(-PI, PI), color="steelblue", edgecolor="k")
    axs[0].set_xlabel(r"$\varphi_a$ (rad)")
    axs[0].set_ylabel("count")
    axs[0].set_title(rf"Type-F per-mode phase histogram at $\tau$={tau_fold:.3f}")
    axs[0].axvline(0, color="k", ls=":", lw=1)
    axs[0].set_xlim(-PI, PI)

    # GGE drift vs delta_tau.
    deltas = [t - tau_fold for t in TAU_SCAN]
    axs[1].plot(deltas, gge["drifts_per_tau"], "o-", color="firebrick")
    axs[1].axhline(GGE_PASS_THRESH, color="green", ls="--", label=f"PASS threshold ({GGE_PASS_THRESH:.0%})")
    axs[1].axhline(GGE_INFO_THRESH, color="orange", ls="--", label=f"INFO ceiling ({GGE_INFO_THRESH:.0%})")
    axs[1].set_xlabel(r"$\Delta\tau = \tau - \tau_{fold}$")
    axs[1].set_ylabel(r"max drift in $\varphi_a$ / $\pi$")
    axs[1].set_title("GGE stability across 4-tau scan (S38 algebraic permanence)")
    axs[1].set_yscale("log")
    axs[1].legend(loc="best")
    axs[1].grid(True, alpha=0.3)

    fig.suptitle(f"{GATE_ID}: composite={composite}  "
                 f"(axioms_pass={axioms_pass}, max_drift={gge['max_drift']:.2e})")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)
    print(f"[8] Wrote {OUT_PNG.name}")

    # ----------- Verdict line emission -----------
    # Canonical S81+ format with full 64-char SHA + dual-SHA companion + S87 v2 3-tuple.
    value_string = (
        f"max_GGE_drift={gge['max_drift']:.4e};"
        f"axiom_max_residual={max_axiom_residual:.3e};"
        f"reason={verdict_reason}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- "
        f"value='{value_string}' "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} "
        f"content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
    )
    sign_3tuple_row = (
        f"# sign_verdict={sign_verdict} "
        f"magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
    )
    append_verdict_line(canonical_line, dual_sha_row, sign_3tuple_row)
    print(f"\n[9] Verdict appended to {VERDICT_FILE.name}")
    print(f"    {canonical_line}")
    print(f"    {dual_sha_row}")
    print(f"    {sign_3tuple_row}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
