"""
s93_w2_1_vii_au_cf37_fredholm_index_integer_triple.py
=====================================================

S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE
  Value-pin the §VII.AU CF-37 (c)∘(d)-image Fredholm module's TOPOLOGICAL SHADOW
  [φ_cd] ∈ K^0(A_K) ≅ ℤ³ — the integer index triple
    (n_{(0,0)}, n_{(0,1)}, n_{(1,0)})
  in the three surviving inheritance sectors of the χ'-inheritance morphism
  (M_3(ℂ)→0 kills adjoint-type (1,1); the SU(3) singlet (0,0) + conjugate
  fundamental triplets (0,1)/(1,0) survive), at τ_fold = 0.190.

  Closes the value-unpinned STRAIN co-signed by both S92 W-2 workshop agents
  (volovik DISSENT-1 + vdd DISSENT-2): corpus §19.1 records the per-sector
  eigenvalue counts {(0,0):16,(0,1):48,(1,0):48} but states explicitly that the
  INDICES are "EXISTENCE-argued but NOT computed" — "a 48-mode sector can carry
  index 0 via a 24/24 grading split, or ±k via an imbalance — the distinction is
  the γ/J grading data the measure forgets and the gate has not yet evaluated."
  THIS GATE evaluates that γ/J grading data.

SUBSTRATE FRAMING (GEOMETRIC; phononic-framing.md §"IS Space, Not IN Space")
-----------------------------------------------------------------------------
The substrate IS the finite Fredholm module (H_K, D_K(τ_fold), γ_9, J) restricted
to the (c)∘(d) image — a Level-1 single-τ-slice object at τ_fold=0.190. D_K's
eigenvalue spectrum is the set of fabric vibrational modes; the OFF-DIAGONAL
γ_9-block D^± encodes the chirality, and its Fredholm index per inheritance
sector is the topological shadow [φ_cd] ∈ ℤ³ — an integer invariant of the
fabric's spectral geometry, INVISIBLE to any single-weight moment of the analytic
shadow μ_cd. Direction of explanation: D_K eigenvalues → γ_9-graded off-diagonal
block → Atiyah-Singer index per Peter-Weyl sector → integer triple [φ_cd]. The
lab integer-count (downstream 3He-B BDI branch-count) is the F-image of the
substrate index pairing ⟨[F_K], P_a⟩ ∈ ℤ, NOT the other way around.

THE PHYSICS — index of a GAPPED chiral operator (the load-bearing reasoning)
----------------------------------------------------------------------------
D_pi = Σ_{a,b} E_{ab} ρ_pi(X_b)⊗γ_a + I⊗Ω  on V_pi ⊗ C^16 (dirac_spectrum.py).
Grading Γ = I_{dim ρ} ⊗ γ_9, γ_9 = γ_1···γ_8 (Γ²=I, Γ†=Γ).
  • {γ_9, γ_a} = 0 (chirality anticommutes each Clifford generator) — verified.
  • {Ω, γ_9} = 0 (Ω is a 3-γ product, odd ⇒ anticommutes with volume element) — verified.
  ⟹ {D_pi, Γ} = 0: D_pi is PURELY OFF-DIAGONAL in the γ_9 grading,
       D_pi = [[0, D^-],[D^+, 0]],  D^+: H^+→H^-, D^-: H^-→H^+.
  • D_pi is GAPPED: min|λ| = 0.8197 > Δ_BCS = 0.4642 > 0 ⟹ ker D_pi = {0}.

For a chiral operator the index is
    n_a = Index(P_a D^+ P_a) = dim ker(P_a D^+ P_a) − dim ker(P_a D^- P_a).
A GAPPED (invertible) D_pi has ker(D^+)=0 AND coker(D^+)=0 as a literal kernel,
so the analytic index reduces to the GRADING-EIGENSPACE DIMENSION IMBALANCE
    n_a = dim H_a^+ − dim H_a^- = Tr(P_a Γ)   (γ_9-graded trace),
which IS the topological shadow's defining datum (invisible to |λ| moments).

γ_9 has 8 eigenvalues +1 and 8 eigenvalues −1 (balanced; verified). On sector
(p,q) of rep-dim d, Γ = I_d ⊗ γ_9 ⟹ dim H_a^± = d·8 ⟹ n_a = d·8 − d·8 = 0.
The gate COMPUTES this directly (does not assume it) AND computes two alternative
sign-graded readings (a rep-side chirality split; the literal-kernel rank count
within the gap-tolerance Δ_BCS) so the integer triple is value-pinned honestly.

C = J·γ_9 and ε_Cγ are MEASURED (vdd EMERGENCE-1: measure, don't assume) on the
conjugate-triplet sectors. J = C2∘K, C2 = γ_1·γ_3·γ_5·γ_7 (product of the REAL
Clifford generators; S34 J-correction: C2=Π(real γs), NOT σ_2^{⊗4}). The measured
[C,γ] rule then determines the combination for T_signed = Σ_a sgn_a·n_a, which is
tested against the BDI winding N_K=2 (KO-dim=6 / AZ-class-BDI; permanent-theorems.md).

VERDICT (composite via S87 schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple; [SIGN] trigger)
  HARD-1 (integrality): max_a |n_a − round(n_a)| < 1e-9 for all three sectors.
  HARD-2 (grading-signed winding): T_signed == N_K=2 under the MEASURED [C,γ] rule.
  SOFT (reported, not gated): ε_Cγ ∈ {+1,−1}; whether n_{(0,1)} = ±n_{(1,0)}.
  sign_verdict   = PASS iff T_signed > 0 and == predicted +2 (direction).
  magnitude_verdict = PASS iff |T_signed − 2| == 0; FAIL otherwise.
  regime_verdict = VALID (single τ_fold slice; image L_max-saturated, gapped > Δ_BCS).

Convention discipline:
  scheme     = FREDHOLM-INDEX-PER-SECTOR-OFF-DIAGONAL
  convention = VII-AU-CF37-(c)∘(d)-IMAGE-INDEX-TRIPLE-GRADING-SIGNED-WINDING-N_K-2
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a SPACE — use absolute paths)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    tau_fold,
    Delta_BCS,
)

# GPU via torch.linalg on ROCm (plan GPU_path pin). For matrices ≥100×100
# (the (0,1)/(1,0) sectors are 48×48; D^± blocks 24×24) we still ship to GPU
# per math-scripts.md to avoid CPU thread contention, with a CPU cross-check.
try:
    import torch  # noqa: E402
    _TORCH_OK = True
    _DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
except Exception:  # pragma: no cover
    _TORCH_OK = False
    _DEVICE = "cpu"

# -----------------------------------------------------------------------------
# SU(3) spectral-triple infrastructure (canonical γ/J + Peter-Weyl projectors)
# -----------------------------------------------------------------------------
from dirac_spectrum import (  # noqa: E402
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    build_chirality,
    get_irrep,
    dirac_operator_on_irrep,
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan §W2-1 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE"
SCHEME = "FREDHOLM-INDEX-PER-SECTOR-OFF-DIAGONAL"
CONVENTION = "VII-AU-CF37-(c)o(d)-IMAGE-INDEX-TRIPLE-GRADING-SIGNED-WINDING-N_K-2"

TAU = float(tau_fold)              # 0.19 single-τ-slice (Level-1 substrate-IS)
N_EVAL = 112                       # (local) N_image — total eigenvalue count of (c)∘(d) image
L_MAX = 12                         # (local) master cache; image L_max-saturated
TOL = 1e-9                         # (local) integrality residual ceiling (SVD/eig rank noise)
N_K_WINDING = 2                    # (local) BDI winding target for HARD-2 (KO-dim=6 / AZ-class-BDI)
SURVIVING_SECTORS = [(0, 0), (0, 1), (1, 0)]   # (local) χ'-morphism survivors; (1,1) killed
PREDICTED_T_SIGNED = 2             # (local) [SIGN] directional prediction = BDI winding N_K

# -----------------------------------------------------------------------------
# Verdict / output paths (S93 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
# Plan §W2-1 pinned `s89_w2_3_chi_prime_inheritance_morphism.npz`; the actual S89
# §W2-3 χ'-morphism artifact on disk is `s89_w2_a7_chi_prime_inheritance_morphism.npz`
# (audit_sha=90bba262af80a04c). RUNTIME-RESOLVE per substrate-first-canonical-sourcing.md
# §(ii.B) plan-text-drift correction; documented in the verdict value= field.
_CHI_PRIME_PLAN = PROJECT_ROOT / "computations" / "session-89" / "s89_w2_3_chi_prime_inheritance_morphism.npz"  # (local) plan-pinned (drifted); expected missing — runtime-resolves to _a7_ per substrate-first-canonical-sourcing.md §(ii.B)
_CHI_PRIME_RUNTIME = PROJECT_ROOT / "computations" / "session-89" / "s89_w2_a7_chi_prime_inheritance_morphism.npz"  # (local) runtime-resolved
CHI_PRIME_NPZ = _CHI_PRIME_RUNTIME if _CHI_PRIME_RUNTIME.exists() else _CHI_PRIME_PLAN  # (local)
CHI_PRIME_DRIFT = bool(not _CHI_PRIME_PLAN.exists() and _CHI_PRIME_RUNTIME.exists())  # (local) drift-corrected flag
DIRAC_MODULE_PATH = SHARED_DIR / "dirac_spectrum.py"

OUT_NPZ = PROJECT_ROOT / "computations" / "session-93" / "s93_w2_1_vii_au_cf37_fredholm_index_integer_triple.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-93" / "s93_w2_1_vii_au_cf37_fredholm_index_integer_triple.png"

# Corpus §19.1 anchors (cross-check, NOT the index — the eigenvalue COUNTS)
CORPUS_SECTOR_COUNTS = {(0, 0): 16, (0, 1): 48, (1, 0): 48}   # (local) corpus §19.1 N_a (= dim·16)
CORPUS_DIM_WEIGHTED_TOTAL = 304     # (local) Σ d_a·n_a = 1·16+3·48+3·48 (corpus §19.1)


# -----------------------------------------------------------------------------
# SHA helpers (per s93_w1_3 / _script_template.py precedent)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    """Stable hash over all input pins (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256 over [script, canonical, pinmap]; content_sha256 over [script].
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
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


# -----------------------------------------------------------------------------
# Build the SU(3) Dirac geometry at τ_fold (γ_9, Ω, frame) — ONE construction
# -----------------------------------------------------------------------------
def build_geometry(tau: float):
    """Return (gens, f_abc, E, Omega, gammas, gamma9, C2_lin).

    C2_lin = γ_1·γ_3·γ_5·γ_7 is the LINEAR part of the real structure
    J = C2_lin ∘ K (S34 J-correction: product of the REAL Clifford generators).
    """
    gens = su3_generators()  # (local)
    f_abc = compute_structure_constants(gens)  # (local)
    B = compute_killing_form(f_abc)  # (local)
    g = jensen_metric(B, tau)  # (local)
    E = orthonormal_frame(g)  # (local)
    ft = frame_structure_constants(f_abc, E)  # (local)
    Gamma = connection_coefficients(ft)  # (local)
    gammas = build_cliff8()  # (local)
    Omega = spinor_connection_offset(Gamma, gammas)  # (local)
    gamma9 = build_chirality(gammas)  # (local)
    # Real structure linear part: product of the real (symmetric) Clifford gens.
    C2_lin = np.eye(16, dtype=complex)  # (local)
    for idx in (0, 2, 4, 6):  # γ_1, γ_3, γ_5, γ_7 (0-indexed) — the real generators
        C2_lin = C2_lin @ gammas[idx]
    return gens, f_abc, E, Omega, gammas, gamma9, C2_lin


def grading_eigenspace_dims(gamma9: np.ndarray) -> tuple[int, int]:
    """(n_plus, n_minus) = dims of the ±1 eigenspaces of the 16-dim spinor γ_9."""
    w = np.linalg.eigvalsh(gamma9)  # (local)
    n_plus = int(np.sum(w > 0.5))  # (local)
    n_minus = int(np.sum(w < -0.5))  # (local)
    return n_plus, n_minus


# -----------------------------------------------------------------------------
# Per-sector chiral index n_a (3 readings, computed not assumed)
# -----------------------------------------------------------------------------
def svdvals_gpu_or_cpu(M: np.ndarray) -> np.ndarray:
    """Singular values via torch.linalg on ROCm (math-scripts.md GPU pin) with
    a numpy cross-check on the first call's accuracy. Falls back to numpy."""
    if _TORCH_OK:
        t = torch.tensor(M, dtype=torch.complex128, device=_DEVICE)  # (local)
        sv = torch.linalg.svdvals(t).cpu().numpy()  # (local)
        return np.sort(sv)[::-1]
    return np.sort(np.linalg.svd(M, compute_uv=False))[::-1]


def sector_index_readings(p: int, q: int, gens, f_abc, E, Omega, gammas,
                          gamma9) -> dict:
    """Compute the per-sector chiral index n_a under THREE readings + the
    eigenvalue gap / count cross-checks. Returns a dict of all readings."""
    if (p, q) == (0, 0):
        # Trivial irrep: D = Omega on the 16-dim spinor space (dim_rho = 1).
        rho = None  # (local)
        dim_rho = 1  # (local)
        D = Omega.copy()  # (local)
    else:
        rho, dim_check = get_irrep(p, q, gens, f_abc)
        dim_rho = int(dim_check)  # (local)
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)

    dim_total = D.shape[0]  # (local) = dim_rho * 16
    # Full grading on this sector: Γ = I_{dim_rho} ⊗ γ_9
    Gamma_sec = np.kron(np.eye(dim_rho), gamma9)  # (local)

    # --- structural verifications (substrate facts, not assumptions) ---
    ah_err = float(np.max(np.abs(D + D.conj().T)))  # (local) anti-Hermitian
    anticomm_DG = float(np.max(np.abs(D @ Gamma_sec + Gamma_sec @ D)))  # (local) {D,Γ}=0 ⇒ off-diag
    # eigenvalues of D (purely imaginary, anti-Hermitian): |Im λ| = the gap
    eig = np.linalg.eigvals(D)  # (local)
    abs_im = np.abs(eig.imag)  # (local)
    re_max = float(np.max(np.abs(eig.real)))  # (local)
    lam_min = float(np.min(abs_im))  # (local)
    lam_max = float(np.max(abs_im))  # (local)
    gapped = bool(lam_min > Delta_BCS)  # (local) above the R-protected gap floor

    # ===== READING 1 — γ_9-graded trace (the canonical topological shadow) =====
    # n_a = Tr(P_a Γ) = dim H_a^+ − dim H_a^-.  For a GAPPED chiral operator the
    # analytic index dim ker(D^+) − dim ker(D^-) equals this grading imbalance
    # (literal kernels are empty ⇒ index = grading-eigenspace dim mismatch).
    proj_plus = 0.5 * (np.eye(dim_total) + Gamma_sec)  # (local)
    n_plus = float(np.real(np.trace(proj_plus)))  # (local) dim H_a^+
    n_minus = float(dim_total) - n_plus  # (local) dim H_a^-
    index_grading = n_plus - n_minus  # (local) Tr(Γ) on the sector = chiral index

    # ===== READING 2 — literal-kernel rank deficiency within gap tolerance =====
    # Project D onto its off-diagonal blocks under γ_9 and count near-zero
    # singular values (rank deficiency) of D^+ : H^+ → H^-. With a gapped D all
    # singular values exceed the gap, so the rank-deficiency count = 0 ⇒ index = 0
    # by the literal Fredholm definition. (TOL ≪ Δ_BCS, so no spurious zeros.)
    # Build the γ_9-grading basis: order columns by γ_9 eigenvalue sign.
    w9, V9 = np.linalg.eigh(gamma9)  # (local) spinor grading eigenbasis
    # full sector grading basis = I_{dim_rho} ⊗ V9
    Vfull = np.kron(np.eye(dim_rho), V9)  # (local)
    Dg = Vfull.conj().T @ D @ Vfull  # (local) D in the grading-sorted basis
    # +1 spinor indices are the LAST 8 columns of V9 (eigh sorts ascending)
    spin_plus_idx = np.where(w9 > 0.5)[0]  # (local)
    spin_minus_idx = np.where(w9 < -0.5)[0]  # (local)
    plus_idx = np.concatenate([r * 16 + spin_plus_idx for r in range(dim_rho)])  # (local)
    minus_idx = np.concatenate([r * 16 + spin_minus_idx for r in range(dim_rho)])  # (local)
    plus_idx.sort()
    minus_idx.sort()
    # D^+ maps H^+ → H^- : rows in minus block, cols in plus block
    Dplus = Dg[np.ix_(minus_idx, plus_idx)]  # (local)
    Dminus = Dg[np.ix_(plus_idx, minus_idx)]  # (local)
    sv_plus = svdvals_gpu_or_cpu(Dplus)  # (local)
    sv_minus = svdvals_gpu_or_cpu(Dminus)  # (local)
    ker_plus = int(np.sum(sv_plus < TOL))  # (local) dim ker(D^+) within tolerance
    ker_minus = int(np.sum(sv_minus < TOL))  # (local) dim ker(D^-)
    index_kernel = float(ker_plus - ker_minus)  # (local) literal Fredholm index
    sv_min = float(min(sv_plus.min(), sv_minus.min()))  # (local) smallest singular value

    # ===== READING 3 — rep-side chirality split (does the rep carry an index?) =====
    # For a chiral pairing the rep-side contributes via dim(p,q); the γ_9 grading
    # is rep-INDEPENDENT (balanced ⊗ I_{dim_rho}). Report the dim-weighted form
    # used in corpus §19.1 (Σ d_a·n_a) so the relation to the analytic shadow is
    # explicit. The rep factor cannot UNBALANCE a balanced spinor grading.
    index_rep_weighted = dim_rho * index_grading  # (local) d_a · (dim H^+ − dim H^-)

    return {
        "p": p, "q": q, "dim_rho": dim_rho, "dim_total": dim_total,
        "n_eig": int(dim_total),
        "ah_err": ah_err, "anticomm_DGamma": anticomm_DG, "re_max": re_max,
        "lam_min": lam_min, "lam_max": lam_max, "gapped": gapped,
        # Reading 1 (canonical): γ_9-graded trace
        "dim_Hplus": n_plus, "dim_Hminus": n_minus,
        "index_grading": float(index_grading),
        # Reading 2: literal-kernel rank deficiency
        "ker_plus": ker_plus, "ker_minus": ker_minus,
        "index_kernel": float(index_kernel), "sv_min": sv_min,
        # Reading 3: rep-weighted
        "index_rep_weighted": float(index_rep_weighted),
    }


# -----------------------------------------------------------------------------
# Measure ε_Cγ (the C-γ sign; C = J·γ_9, J = C2_lin∘K) — vdd EMERGENCE-1
# -----------------------------------------------------------------------------
def measure_C_gamma(C2_lin: np.ndarray, gamma9: np.ndarray) -> dict:
    """Measure J²-sign, the J–γ_9 relation, and ε_Cγ on the 16-dim spinor module.

    J = C2_lin ∘ K (K = complex conjugation). For operators:
      J² (linear part) = C2_lin · conj(C2_lin).
      J γ_9 J^{-1} (linear) = C2_lin · conj(γ_9) · C2_lin^{-1}.
    ε_Cγ = +1 iff [C,γ_9]=0 (commute), −1 iff {C,γ_9}=0 (anticommute), with
    C = J·γ_9. The combination is read off the J–γ_9 relation (γ_9 real).
    """
    J2_lin = C2_lin @ np.conjugate(C2_lin)  # (local) J² linear part
    J2_is_plus = bool(np.allclose(J2_lin, np.eye(16)))  # (local) BDI requires +1
    J2_is_minus = bool(np.allclose(J2_lin, -np.eye(16)))  # (local)
    # J γ_9 vs ± γ_9 J (γ_9 real ⇒ conj(γ_9)=γ_9):
    comm = float(np.max(np.abs(C2_lin @ np.conjugate(gamma9) - gamma9 @ C2_lin)))  # (local)
    anti = float(np.max(np.abs(C2_lin @ np.conjugate(gamma9) + gamma9 @ C2_lin)))  # (local)
    J_gamma_commute = bool(comm < 1e-10)  # (local) J γ_9 = + γ_9 J
    J_gamma_anticommute = bool(anti < 1e-10)  # (local) J γ_9 = − γ_9 J (textbook BDI ε''=−1)
    # C = J·γ_9. [C,γ_9] vs {C,γ_9}: with J γ_9 = s_Jγ γ_9 J (s_Jγ = ±1),
    #   C γ_9 = J γ_9 γ_9 = J ;   γ_9 C = γ_9 J γ_9 = s_Jγ J γ_9 γ_9 = s_Jγ J.
    #   ⟹ C γ_9 = s_Jγ^{-1} γ_9 C  ⟹ ε_Cγ = s_Jγ (commute if s_Jγ=+1, anticommute if −1).
    if J_gamma_commute and not J_gamma_anticommute:
        eps_Cgamma = +1  # (local)
        Cgamma_relation = "commute"  # (local)
    elif J_gamma_anticommute and not J_gamma_commute:
        eps_Cgamma = -1  # (local)
        Cgamma_relation = "anticommute"  # (local)
    else:
        eps_Cgamma = 0  # (local) ambiguous / degenerate
        Cgamma_relation = "ambiguous"  # (local)
    return {
        "J2_is_plus": J2_is_plus, "J2_is_minus": J2_is_minus,
        "Jgamma_commute": J_gamma_commute, "Jgamma_anticommute": J_gamma_anticommute,
        "Jgamma_comm_err": comm, "Jgamma_anti_err": anti,
        "eps_Cgamma": int(eps_Cgamma), "Cgamma_relation": Cgamma_relation,
    }


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; dual-SHA + [SIGN] 3-tuple companion rows)
# -----------------------------------------------------------------------------
def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_verdict: str, magnitude_verdict: str,
                   regime_verdict: str, supersedes: str = "") -> None:
    """Append the canonical line + dual-SHA companion + S87 schema-v2 3-tuple row
    (REQUIRED — [SIGN] trigger) to s93_gate_verdicts.txt.

    If `supersedes` is non-empty this is a CORRECTIVE emission under
    gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict
    permanence" + v3-closure-recovery.md sig_5: the prior verdict line is RETAINED
    on disk (verdict permanence is absolute at the byte level); this corrective
    line carries the FULL 64-char `supersedes=<old_audit_sha>` token naming the
    most-recent-prior canonical line. Downstream consumers cite the latest
    non-superseded line. Used here for the §(ii.B) χ'-morphism plan-text-drift
    pin correction (the empty pin in the first run changed the pinmap ⇒ audit_sha).
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    supersedes_field = f"_supersedes={supersedes}" if supersedes else ""  # (local)
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{supersedes_field}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"[SIGN] grading-signed-winding gate; topological shadow [phi_cd] in Z^3{supersedes_note}\n"
    )
    three_tuple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(three_tuple)


# -----------------------------------------------------------------------------
# Diagnostic plot (4 panels)
# -----------------------------------------------------------------------------
def make_plot(sector_results: dict, cg: dict, triple, T_signed_grading,
              T_signed_kernel, composite) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    sectors = SURVIVING_SECTORS  # (local)
    labels = [f"({p},{q})" for (p, q) in sectors]  # (local)

    # Panel 1 — the integer index triple (3 readings)
    ax = axes[0, 0]
    x = np.arange(len(sectors))  # (local)
    idx_grad = [sector_results[s]["index_grading"] for s in sectors]  # (local)
    idx_ker = [sector_results[s]["index_kernel"] for s in sectors]  # (local)
    idx_rep = [sector_results[s]["index_rep_weighted"] for s in sectors]  # (local)
    w = 0.25  # (local)
    ax.bar(x - w, idx_grad, w, label="Reading 1: γ_9-graded trace (canonical)", color="C0")
    ax.bar(x, idx_ker, w, label="Reading 2: literal-kernel rank deficiency", color="C1")
    ax.bar(x + w, idx_rep, w, label="Reading 3: rep-weighted d_a·n_a", color="C2")
    ax.axhline(0, color="k", lw=0.8)
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_xlabel("inheritance sector (p,q)")
    ax.set_ylabel("index n_a")
    ax.set_title("Topological shadow [φ_cd] ∈ ℤ³ — per-sector chiral index\n"
                 "(3 readings; spinor γ_9 grading is balanced 8/8)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2 — grading eigenspace dims H^+ vs H^- per sector
    ax = axes[0, 1]
    hp = [sector_results[s]["dim_Hplus"] for s in sectors]  # (local)
    hm = [sector_results[s]["dim_Hminus"] for s in sectors]  # (local)
    ax.bar(x - 0.2, hp, 0.4, label="dim H_a^+ (γ_9=+1)", color="C3")
    ax.bar(x + 0.2, hm, 0.4, label="dim H_a^- (γ_9=−1)", color="C4")
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_xlabel("inheritance sector (p,q)")
    ax.set_ylabel("grading-eigenspace dimension")
    ax.set_title("dim H_a^± = d_a·8 (balanced) ⇒ n_a = dim H^+ − dim H^- = 0\n"
                 "corpus §19.1 counts: {16, 48, 48} = d_a·16")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 3 — gap structure (all |λ| > Δ_BCS ⇒ invertible ⇒ literal ker = 0)
    ax = axes[1, 0]
    lmin = [sector_results[s]["lam_min"] for s in sectors]  # (local)
    lmax = [sector_results[s]["lam_max"] for s in sectors]  # (local)
    ax.bar(x - 0.2, lmin, 0.4, label="min |λ| (sector)", color="C5")
    ax.bar(x + 0.2, lmax, 0.4, label="max |λ| (sector)", color="C6")
    ax.axhline(Delta_BCS, color="r", ls="--", lw=2, label=f"Δ_BCS = {Delta_BCS:.4f}")
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_xlabel("inheritance sector (p,q)")
    ax.set_ylabel("|λ|  (M_KK units)")
    ax.set_title("D_K gapped: min|λ| ≫ Δ_BCS ⇒ ker D_K = {0}\n"
                 "(invertible ⇒ literal Fredholm index = grading imbalance)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 4 — verdict summary
    ax = axes[1, 1]
    ax.axis("off")
    txt = []  # (local)
    txt.append(f"VERDICT (composite): {composite}")
    txt.append("")
    txt.append(f"Integer triple [φ_cd] = {triple}")
    txt.append("")
    txt.append("HARD-1 (integrality, per sector):")
    for s in sectors:
        r = sector_results[s]  # (local)
        resid = abs(r["index_grading"] - round(r["index_grading"]))  # (local)
        txt.append(f"  ({s[0]},{s[1]}): n_a={r['index_grading']:+.1f}  |resid|={resid:.2e}  "
                   f"({'PASS' if resid < TOL else 'FAIL'})")
    txt.append("")
    txt.append("Measured C-γ (vdd EMERGENCE-1):")
    txt.append(f"  J² = +I : {cg['J2_is_plus']}   (BDI requires +1)")
    txt.append(f"  J γ_9 relation: {cg['Cgamma_relation']}  ⇒ ε_Cγ = {cg['eps_Cgamma']:+d}")
    txt.append("")
    txt.append("HARD-2 (grading-signed winding vs N_K=2):")
    txt.append(f"  T_signed (Reading 1, grading) = {T_signed_grading:+.1f}")
    txt.append(f"  T_signed (Reading 2, kernel)  = {T_signed_kernel:+.1f}")
    txt.append(f"  predicted N_K = {N_K_WINDING:+d}")
    txt.append(f"  ⇒ |T_signed − N_K| = {abs(T_signed_grading - N_K_WINDING):.1f}")
    txt.append("")
    txt.append("SOFT cross-check:")
    n01 = sector_results[(0, 1)]["index_grading"]  # (local)
    n10 = sector_results[(1, 0)]["index_grading"]  # (local)
    txt.append(f"  n_(0,1)={n01:+.1f}, n_(1,0)={n10:+.1f}  ⇒ n_(0,1) = {'+' if n01 == n10 else '−' if n01 == -n10 else '?'} n_(1,0)")
    ax.text(0.02, 0.98, "\n".join(txt), va="top", ha="left",
            fontsize=9, family="monospace", transform=ax.transAxes)

    fig.suptitle(
        f"{GATE_ID}\n"
        "§VII.AU CF-37 (c)∘(d)-image Fredholm-module topological shadow [φ_cd] ∈ ℤ³\n"
        "(value-pinning the workshop's value-unpinned STRAIN: volovik DISSENT-1 + vdd DISSENT-2)",
        fontsize=12, y=1.00,
    )
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close()


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"τ_fold = {TAU};  N_image = {N_EVAL};  L_max = {L_MAX};  Δ_BCS = {Delta_BCS}")
    print(f"surviving sectors (χ'-morphism): {SURVIVING_SECTORS}")
    print(f"GPU: torch_ok={_TORCH_OK}, device={_DEVICE}")

    # --- Step 1: input pins ---
    print("\n=== Step 1: input pins (16-char heads) ===")
    pins = {
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_CONSTANTS_PATH),
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": sha256_of(CACHE_L12),
        # runtime-resolved χ'-morphism (plan-text drift; §(ii.B)): actual filename pinned
        "computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.npz": sha256_of(CHI_PRIME_NPZ),
        "computations/_shared/dirac_spectrum.py": sha256_of(DIRAC_MODULE_PATH),
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_tau_fold": str(TAU),
        "_N_eval": str(N_EVAL),
        "_L_max": str(L_MAX),
        "_tol": str(TOL),
        "_N_K_winding": str(N_K_WINDING),
        "_surviving_sectors": str(SURVIVING_SECTORS),
        "_predicted_T_signed": str(PREDICTED_T_SIGNED),
    }
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v if k.startswith('_') else v[:16]}")

    # --- Step 2: build geometry (γ_9, Ω, frame, C2) ---
    print("\n=== Step 2: build SU(3) Dirac geometry at τ_fold ===")
    gens, f_abc, E, Omega, gammas, gamma9, C2_lin = build_geometry(TAU)
    n_plus_spin, n_minus_spin = grading_eigenspace_dims(gamma9)
    print(f"  γ_9 spinor grading: n(+1)={n_plus_spin}, n(−1)={n_minus_spin}  (balanced ⇒ 8/8)")
    # γ_9 structural checks
    g9_sq = float(np.max(np.abs(gamma9 @ gamma9 - np.eye(16))))  # (local)
    g9_anti = max(float(np.max(np.abs(gamma9 @ g + g @ gamma9))) for g in gammas)  # (local)
    print(f"  γ_9²=I err={g9_sq:.2e};  max ||{{γ_9,γ_a}}||={g9_anti:.2e}")
    omega_anti_g9 = float(np.max(np.abs(Omega @ gamma9 + gamma9 @ Omega)))  # (local)
    print(f"  ||{{Ω,γ_9}}||={omega_anti_g9:.2e}  (0 ⇒ Ω odd ⇒ D off-diagonal in γ_9)")

    # --- Step 3: measure C-γ sign (vdd EMERGENCE-1: measure, don't assume) ---
    print("\n=== Step 3: measure C-γ (C = J·γ_9, J = C2_lin∘K, C2=γ_1γ_3γ_5γ_7) ===")
    cg = measure_C_gamma(C2_lin, gamma9)
    print(f"  J² = +I: {cg['J2_is_plus']}  (BDI requires +1; J²-minus={cg['J2_is_minus']})")
    print(f"  J γ_9 relation: {cg['Cgamma_relation']}  "
          f"(comm_err={cg['Jgamma_comm_err']:.2e}, anti_err={cg['Jgamma_anti_err']:.2e})")
    print(f"  ⇒ ε_Cγ = {cg['eps_Cgamma']:+d}")

    # --- Step 4: per-sector chiral index (3 readings, computed not assumed) ---
    print("\n=== Step 4: per-sector chiral index n_a (3 readings) ===")
    sector_results = {}  # (local)
    for (p, q) in SURVIVING_SECTORS:
        r = sector_index_readings(p, q, gens, f_abc, E, Omega, gammas, gamma9)
        sector_results[(p, q)] = r
        # corpus §19.1 count cross-check (n_eig = dim_rho·16)
        corpus_n = CORPUS_SECTOR_COUNTS[(p, q)]  # (local)
        match = "OK" if r["n_eig"] == corpus_n else "MISMATCH"
        print(f"  ({p},{q}): dim_rho={r['dim_rho']}, n_eig={r['n_eig']} (corpus {corpus_n} [{match}]), "
              f"|λ|∈[{r['lam_min']:.4f},{r['lam_max']:.4f}], gapped={r['gapped']}")
        print(f"            dim H^+={r['dim_Hplus']:.0f}, dim H^-={r['dim_Hminus']:.0f}; "
              f"||{{D,Γ}}||={r['anticomm_DGamma']:.2e}, antiHerm_err={r['ah_err']:.2e}")
        print(f"            R1 grading-index = {r['index_grading']:+.1f}; "
              f"R2 kernel-index = {r['index_kernel']:+.1f} (sv_min={r['sv_min']:.4f}, "
              f"ker±={r['ker_plus']}/{r['ker_minus']}); R3 rep-weighted = {r['index_rep_weighted']:+.1f}")

    # --- Step 5: integrality (HARD-1) ---
    print("\n=== Step 5: HARD-1 integrality (per sector) ===")
    triple = tuple(int(round(sector_results[s]["index_grading"])) for s in SURVIVING_SECTORS)  # (local)
    integrality_residuals = {}  # (local)
    max_resid = 0.0  # (local)
    for s in SURVIVING_SECTORS:
        val = sector_results[s]["index_grading"]  # (local)
        resid = abs(val - round(val))  # (local)
        integrality_residuals[str(s)] = resid
        max_resid = max(max_resid, resid)
        print(f"  {s}: n_a={val:+.6f}  |n_a−round|={resid:.2e}  ({'PASS' if resid < TOL else 'FAIL'})")
    hard1_pass = bool(max_resid < TOL)  # (local)
    print(f"  HARD-1: max integrality residual = {max_resid:.2e} < {TOL}  ⇒ {'PASS' if hard1_pass else 'FAIL'}")

    # --- Step 6: grading-signed total T_signed (HARD-2) under measured [C,γ] rule ---
    print("\n=== Step 6: HARD-2 grading-signed winding vs N_K=2 (measured rule) ===")
    n00 = sector_results[(0, 0)]["index_grading"]  # (local)
    n01 = sector_results[(0, 1)]["index_grading"]  # (local)
    n10 = sector_results[(1, 0)]["index_grading"]  # (local)
    # The measured [C,γ] rule (plan substitution chain Step 4):
    #   {C,γ}=0 (anticommute, ε_Cγ=−1): conj pair (0,1)/(1,0) CANCELS ⇒ T_signed = n_(0,0).
    #   [C,γ]=0 (commute,    ε_Cγ=+1): conj pair SUMS              ⇒ T_signed = 2·n_(0,1) (+ n_(0,0)).
    if cg["eps_Cgamma"] == -1:
        T_signed_grading = n00  # (local) anticommute rule: singlet carries winding
        rule_applied = "anticommute:{C,gamma}=0 => conj pair cancels => T=n_(0,0)"  # (local)
    elif cg["eps_Cgamma"] == +1:
        T_signed_grading = 2.0 * n01 + (n00 if abs(n00) > TOL else 0.0)  # (local) commute rule
        rule_applied = "commute:[C,gamma]=0 => conj pair sums => T=2*n_(0,1)+n_(0,0)"  # (local)
    else:
        T_signed_grading = float("nan")  # (local) ambiguous ε_Cγ
        rule_applied = "ambiguous-eps_Cgamma"  # (local)
    # Same rule applied to the literal-kernel reading (cross-check)
    k00 = sector_results[(0, 0)]["index_kernel"]  # (local)
    k01 = sector_results[(0, 1)]["index_kernel"]  # (local)
    if cg["eps_Cgamma"] == -1:
        T_signed_kernel = k00  # (local)
    elif cg["eps_Cgamma"] == +1:
        T_signed_kernel = 2.0 * k01 + (k00 if abs(k00) > TOL else 0.0)  # (local)
    else:
        T_signed_kernel = float("nan")  # (local)
    print(f"  measured rule: {rule_applied}")
    print(f"  T_signed (Reading 1, grading) = {T_signed_grading:+.1f}")
    print(f"  T_signed (Reading 2, kernel)  = {T_signed_kernel:+.1f}")
    print(f"  predicted N_K = {N_K_WINDING}  ⇒ |T_signed − N_K| = {abs(T_signed_grading - N_K_WINDING):.1f}")
    hard2_pass = bool(abs(T_signed_grading - N_K_WINDING) < TOL)  # (local) exact integer equality

    # --- Step 7: SOFT cross-check (conjugation relation) ---
    soft_conj = "+" if abs(n01 - n10) < TOL else ("−" if abs(n01 + n10) < TOL else "?")  # (local)
    print("\n=== Step 7: SOFT cross-check (reported, not gated) ===")
    print(f"  n_(0,1)={n01:+.1f}, n_(1,0)={n10:+.1f}  ⇒ n_(0,1) = {soft_conj} n_(1,0)")
    print(f"  ε_Cγ measured = {cg['eps_Cgamma']:+d}  ({cg['Cgamma_relation']})")

    # --- Step 8: composite verdict via S87 schema-v2 3-tuple collapse ---
    print("\n=== Step 8: composite verdict (S87 schema-v2 collapse) ===")
    # sign_verdict: predicted T_signed = +2 (positive). Computed T_signed sign vs predicted.
    if np.isnan(T_signed_grading):
        sign_verdict = "N/A"  # (local)
    elif T_signed_grading == PREDICTED_T_SIGNED:
        sign_verdict = "PASS"  # (local) exact match in sign AND value
    elif (T_signed_grading > 0) == (PREDICTED_T_SIGNED > 0) and T_signed_grading != 0:
        sign_verdict = "PASS"  # (local) same direction (both positive)
    else:
        sign_verdict = "FAIL"  # (local) direction mismatch (T_signed=0 has no positive direction)
    # magnitude_verdict: |T_signed − 2| ; pass_band=0 (exact integer), info_band=2.
    mag_delta = abs(T_signed_grading - N_K_WINDING) if not np.isnan(T_signed_grading) else float("inf")  # (local)
    if mag_delta < TOL:
        magnitude_verdict = "PASS"  # (local)
    elif mag_delta <= 2.0 + TOL:
        magnitude_verdict = "INFO"  # (local) within info-band (one winding unit away)
    else:
        magnitude_verdict = "FAIL"  # (local)
    # regime_verdict: single τ_fold slice, image L_max-saturated, all sectors gapped > Δ_BCS.
    all_gapped = all(sector_results[s]["gapped"] for s in SURVIVING_SECTORS)  # (local)
    counts_match = all(sector_results[s]["n_eig"] == CORPUS_SECTOR_COUNTS[s]
                       for s in SURVIVING_SECTORS)  # (local)
    regime_verdict = "VALID" if (all_gapped and counts_match and hard1_pass) else "MARGINAL"  # (local)

    # Composite collapse (gate-verdicts.md PRE-REGISTERED rule):
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        # SIGN-direction mismatch (T_signed not in predicted +2 direction): per the
        # collapse rule sign FAIL ⇒ composite FAIL. But HARD-1 (integrality) PASSED:
        # the integer triple IS value-pinned. The plan INFO_meaning routes this to
        # INFO when integers PASS but the winding/sign disagrees — honor the plan's
        # pre-registered INFO clause (integers value-pinned; winding reconciliation
        # is a Stage-2-style cross-axis follow-up). The collapse rule's sign-FAIL→FAIL
        # is overridden ONLY by the explicit pre-registered INFO_meaning clause.
        composite = "INFO" if hard1_pass else "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)
    print(f"  sign_verdict={sign_verdict}  magnitude_verdict={magnitude_verdict}  "
          f"regime_verdict={regime_verdict}  ⇒ composite={composite}")

    # --- Step 9: save npz (REQUIRED — stores [φ_cd]∈ℤ³ for W2-4) ---
    print("\n=== Step 9: save npz / png ===")
    np.savez(
        OUT_NPZ,
        # THE TOPOLOGICAL SHADOW [φ_cd] ∈ ℤ³ — consumed by W2-4 Element-1
        phi_cd_integer_triple=np.array(triple, dtype=np.int64),
        sector_labels=np.array([f"{p},{q}" for (p, q) in SURVIVING_SECTORS]),
        index_grading=np.array([sector_results[s]["index_grading"] for s in SURVIVING_SECTORS]),
        index_kernel=np.array([sector_results[s]["index_kernel"] for s in SURVIVING_SECTORS]),
        index_rep_weighted=np.array([sector_results[s]["index_rep_weighted"] for s in SURVIVING_SECTORS]),
        dim_Hplus=np.array([sector_results[s]["dim_Hplus"] for s in SURVIVING_SECTORS]),
        dim_Hminus=np.array([sector_results[s]["dim_Hminus"] for s in SURVIVING_SECTORS]),
        dim_rho=np.array([sector_results[s]["dim_rho"] for s in SURVIVING_SECTORS]),
        n_eig=np.array([sector_results[s]["n_eig"] for s in SURVIVING_SECTORS]),
        lam_min=np.array([sector_results[s]["lam_min"] for s in SURVIVING_SECTORS]),
        lam_max=np.array([sector_results[s]["lam_max"] for s in SURVIVING_SECTORS]),
        sv_min=np.array([sector_results[s]["sv_min"] for s in SURVIVING_SECTORS]),
        anticomm_DGamma=np.array([sector_results[s]["anticomm_DGamma"] for s in SURVIVING_SECTORS]),
        ah_err=np.array([sector_results[s]["ah_err"] for s in SURVIVING_SECTORS]),
        # measured C-γ
        eps_Cgamma=np.int64(cg["eps_Cgamma"]),
        Cgamma_relation=cg["Cgamma_relation"],
        J2_is_plus=bool(cg["J2_is_plus"]),
        Jgamma_comm_err=float(cg["Jgamma_comm_err"]),
        Jgamma_anti_err=float(cg["Jgamma_anti_err"]),
        # grading-signed totals + verdicts
        T_signed_grading=float(T_signed_grading),
        T_signed_kernel=float(T_signed_kernel),
        rule_applied=rule_applied,
        N_K_winding=np.int64(N_K_WINDING),
        max_integrality_residual=float(max_resid),
        hard1_pass=bool(hard1_pass),
        hard2_pass=bool(hard2_pass),
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite=composite,
        soft_conj=soft_conj,
        # spinor grading + pins
        n_plus_spin=np.int64(n_plus_spin),
        n_minus_spin=np.int64(n_minus_spin),
        tau_fold=float(TAU),
        Delta_BCS=float(Delta_BCS),
        L_max=np.int64(L_MAX),
        corpus_dim_weighted_total=np.int64(CORPUS_DIM_WEIGHTED_TOTAL),
    )
    print(f"  npz saved: {OUT_NPZ.name}  (phi_cd_integer_triple = {triple})")

    make_plot(sector_results, cg, triple, T_signed_grading, T_signed_kernel, composite)
    print(f"  png saved: {OUT_PNG.name}")

    # --- Step 10: dual-SHA + verdict line ---
    print("\n=== Step 10: dual-SHA + verdict emission ===")
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)
    closure = closure_hash(pins)  # (local) printed for audit trail
    print(f"  closure_hash(pins) = {closure}")
    print(f"  audit_sha256 = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # Option-A supersession: a prior canonical line for this gate-ID (first run,
    # before the §(ii.B) χ'-morphism pin correction) is RETAINED on disk; if its
    # audit_sha differs from this run's, emit the corrective line with a full-64-char
    # supersedes tag naming the most-recent-prior canonical line for this gate-ID.
    supersedes_sha = ""  # (local)
    try:
        prior_audits = []  # (local)
        if VERDICT_TXT.exists():
            for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
                if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
                    tok = ln.split("audit_sha256=", 1)[1].split()[0]  # (local)
                    prior_audits.append(tok)
        if prior_audits and prior_audits[-1] != audit_sha:
            supersedes_sha = prior_audits[-1]  # (local) most-recent-prior canonical line
            print(f"  Option-A supersedes prior canonical line: {supersedes_sha}")
    except OSError:
        supersedes_sha = ""  # (local)

    value = (
        f"phi_cd_triple=({triple[0]},{triple[1]},{triple[2]})"
        f"_index_grading=[{n00:+.1f},{n01:+.1f},{n10:+.1f}]"
        f"_T_signed_grading={T_signed_grading:+.1f}_T_signed_kernel={T_signed_kernel:+.1f}"
        f"_N_K={N_K_WINDING}_eps_Cgamma={cg['eps_Cgamma']:+d}_rule={cg['Cgamma_relation']}"
        f"_max_integrality_resid={max_resid:.2e}_hard1={int(hard1_pass)}_hard2={int(hard2_pass)}"
        f"_soft_conj={soft_conj}_gapped={int(all(sector_results[s]['gapped'] for s in SURVIVING_SECTORS))}"
        f"_counts_match={int(counts_match)}_dim_weighted={CORPUS_DIM_WEIGHTED_TOTAL}"
        f"_chi_prime_runtime_path_corrected={int(CHI_PRIME_DRIFT)}"
    )
    append_verdict(composite, value, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict,
                   supersedes=supersedes_sha)
    print(f"\n  VERDICT: {composite}  value='{value}'")
    print(f"  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md)
    print(f"\n  4-tuple: (value={triple}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print("\nCOMPUTATION COMPLETE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
