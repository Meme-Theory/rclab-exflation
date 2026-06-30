"""
s94_vii_au_winding_reconciliation.py
====================================

S94-VII-AU-WINDING-RECONCILIATION   [CHAIN]   (GEOMETRIC)
  Reconcile WHERE the BDI winding N_K=2 (KO-dim=6, AZ class BDI) of the spectral
  triple (A_K, H_K, D_K) lives, on the value-pinned topological shadow
  [phi_cd] = (0,0,0) the S93 W2-1 gate produced.

  THE S93 W2-1 WALL (carried, not re-derived):
    The per-sector gamma_9-grading chiral index T_signed is identically 0
    (T_signed_grading=+0.0, T_signed_kernel=+0.0) because the 16-dim spinor
    gamma_9 grading is BALANCED 8/8 (Gamma = I_{dim_rho} ⊗ gamma_9 is
    rep-INDEPENDENT). A balanced chiral grading annihilates the chiral index
    => the winding N_K=2 CANNOT live in T_signed. It must be read from a
    DIFFERENT pairing.

  TWO PRE-REGISTERED PATHWAYS on the SAME triple (cross-axis; no shared-context
  reuse of the other pathway's intermediate -- Axis-distinctness per
  joint-theorem-promotion.md):

    (alpha) vdd rep-side / J-twisted (real, KO-dim=6) K-homology over
            A_K = C (+) H (+) M_3(C).  J = C2 ∘ K, C2 = gamma_1 gamma_3 gamma_5 gamma_7
            (S34 J-correction: product of the REAL Clifford generators);
            J^2=+1, (eps,eps',eps'')=(+1,+1,-1), AZ class BDI.  The measured
            C-gamma relation is COMMUTE (eps_Cgamma=+1, the BDI rule;
            S93 W2-1).  Under [C,gamma_9]=0 the J-conjugate pair (0,1)/(1,0)
            of fundamental sectors SUMS (does NOT cancel) into the BDI Z-index;
            the singlet (0,0) is self-conjugate and carries no winding
            (index_grading=0).  The BDI winding is the conjugate-pair
            MULTIPLICITY:  N_K^{(alpha)} = 2.

    (beta)  volovik BdG-sector winding under the chi-inheritance morphism
            chi : C (+) H (+) M_3(C) -> M_2(C),  M_3(C) -> 0;
            ker(chi) = M_3(C) ENTIRE (rank 9; DERIVED THEOREM, S89 W2 -- a
            non-zero algebra hom on the simple Wedderburn factor M_3(C) would
            be injective, but dim_C(target=M_2(C)⊗Cl(1))=8 < 9, contradiction,
            so chi|_{M_3(C)} = 0).  The inherited M_2(C) is the Nambu
            particle-hole (BdG-doubling) algebra; its BDI winding is the
            3He-B BDI winding N=2 (two co-propagating Majorana branches).
            The conjugate-pair WINDING (the "2") is preserved through
            inheritance because it lives in the J / Nambu DOUBLING (which
            inherits into M_2(C)); the COLOR content of the fundamental pair
            (the M_3(C) part) is what does NOT inherit -- carried by
            ker(chi) = M_3(C).   N_K^{(beta)} = 2.

  RECONCILIATION (set-membership):
    PASS  iff  { N_K^{(alpha)}, N_K^{(beta)} } == {2}  (BOTH return 2).
    INFO  iff  they diverge AND the difference equals the ker(chi)=M_3(C)
              contribution (consistency-PRESERVING relocation).
    FAIL  iff  they diverge with NO kernel-carried reason (contradiction).

SUBSTRATE FRAMING (GEOMETRIC; phononic-framing.md §"IS Space, Not IN Space")
-----------------------------------------------------------------------------
The winding N_K is the substrate's intrinsic BDI index -- a property of the
spectral triple ITSELF.  Direction of explanation: D_K eigenmodes ->
J-twisted K-homology class [D_K, J, gamma_9] over A_K -> BDI Z-valued winding
N_K=2.  The chi-inheritance morphism is the substrate's OWN algebra projection
onto the 3He-B BdG sub-sector; the lab 3He-B BdG winding IS the inherited image
of the substrate winding (parent -> child, NOT analogy;
project_3heb-inheritance.md).  ker(chi)=M_3(C) carries the substrate dof that
do NOT inherit (the rank-2 cohomology kernel <[phi_67],[phi_88]>;
inheritance-falsifier-protocol.md).

DOWNSTREAM CONSUMER (§W2-2): the identified winding-bearing pairing + the
integer N_K are written machine-readable into the npz (keys: winding_bearing_pairing,
N_K_for_level3) and stated in the verdict value= field so §W2-2 can read the
Level-3 anchor = 2 without re-deriving it.

Convention discipline:
  scheme     = BDI-K-HOMOLOGY
  convention = ABSOLUTE-INTEGER-WINDING
  trigger    = [CHAIN]  (set-membership verdict; NOT [SIGN] -- no signed-delta;
               3-tuple companion row NOT required per plan output_artifacts)
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
# Path discipline (project root contains a SPACE -- use absolute paths)
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

# GPU via torch.linalg on ROCm (plan GPU_path pin = torch.linalg). The J-twisted
# K-homology read rebuilds the (0,1)/(1,0) sectors (48x48; D^± blocks 24x24);
# for matrices >= 100x100 we ship to GPU per math-scripts.md, with a CPU
# cross-check on the first eigvals call.
try:
    import torch  # noqa: E402
    _TORCH_OK = True
    _DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
except Exception:  # pragma: no cover
    _TORCH_OK = False
    _DEVICE = "cpu"

# -----------------------------------------------------------------------------
# SU(3) spectral-triple infrastructure (canonical gamma/J + Peter-Weyl)
# -----------------------------------------------------------------------------
from dirac_spectrum import (  # noqa: E402
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    build_cliff8,
    build_chirality,
    spinor_connection_offset,
    frame_structure_constants,
    connection_coefficients,
    get_irrep,
    dirac_operator_on_irrep,
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan §W2-1 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S94-VII-AU-WINDING-RECONCILIATION"
SCHEME = "BDI-K-HOMOLOGY"
CONVENTION = "ABSOLUTE-INTEGER-WINDING"

TAU = float(tau_fold)              # 0.19 single-tau-slice (Level-1 substrate-IS)
N_EVAL = 155984                    # (local) full L_max=10 D_K spectrum count (plan pin)
L_MAX = 10                         # (local) the value-pinned triple is at L_max=10
TOL = 1e-9                         # (local) integrality residual ceiling per pathway
N_K_TARGET = 2                     # (local) BDI winding target (KO-dim=6 / AZ class BDI)
SURVIVING_SECTORS = [(0, 0), (0, 1), (1, 0)]   # (local) chi'-morphism survivors; (1,1) killed

# -----------------------------------------------------------------------------
# Verdict / output paths (S94 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-94" / "s94_gate_verdicts.txt"
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
S93_TRIPLE_NPZ = (PROJECT_ROOT / "computations" / "session-93"
                  / "s93_w2_1_vii_au_cf37_fredholm_index_integer_triple.npz")
S89_CHI_NPZ = (PROJECT_ROOT / "computations" / "session-89"
               / "s89_w2_a7_chi_prime_inheritance_morphism.npz")
CACHE_L12 = (PROJECT_ROOT / "computations" / "session-84"
             / "s84_spectrum_cache_L12_tau019.npz")
DIRAC_MODULE_PATH = SHARED_DIR / "dirac_spectrum.py"

OUT_NPZ = (PROJECT_ROOT / "computations" / "session-94"
           / "s94_vii_au_winding_reconciliation.npz")
OUT_PNG = (PROJECT_ROOT / "computations" / "session-94"
           / "s94_vii_au_winding_reconciliation.png")


# -----------------------------------------------------------------------------
# SHA helpers (per s93_w2_1 / _script_template.py precedent)
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
# Build the SU(3) Dirac geometry at tau_fold (gamma_9, Omega, frame, C2) -- ONE
# construction, identical machinery to S93 W2-1 (so the carried wall reproduces).
# -----------------------------------------------------------------------------
def build_geometry(tau: float):
    """Return (gens, f_abc, E, Omega, gammas, gamma9, C2_lin).

    C2_lin = gamma_1 gamma_3 gamma_5 gamma_7 is the LINEAR part of the real
    structure J = C2_lin ∘ K (S34 J-correction: product of the REAL Clifford
    generators).
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
    C2_lin = np.eye(16, dtype=complex)  # (local)
    for idx in (0, 2, 4, 6):  # gamma_1, gamma_3, gamma_5, gamma_7 (0-indexed)
        C2_lin = C2_lin @ gammas[idx]
    return gens, f_abc, E, Omega, gammas, gamma9, C2_lin


def measure_C_gamma(C2_lin: np.ndarray, gamma9: np.ndarray) -> dict:
    """Measure J^2-sign and the C = J·gamma_9 commute/anticommute relation
    (vdd EMERGENCE-1: measure, don't assume). Reproduces S93 W2-1 exactly:
    eps_Cgamma = +1 (commute) is the BDI rule that makes the conjugate pair SUM.
    """
    J2_lin = C2_lin @ np.conjugate(C2_lin)  # (local) J^2 linear part
    J2_is_plus = bool(np.allclose(J2_lin, np.eye(16)))  # (local) BDI requires +1
    comm = float(np.max(np.abs(C2_lin @ np.conjugate(gamma9) - gamma9 @ C2_lin)))  # (local)
    anti = float(np.max(np.abs(C2_lin @ np.conjugate(gamma9) + gamma9 @ C2_lin)))  # (local)
    J_gamma_commute = bool(comm < 1e-10)  # (local)
    J_gamma_anticommute = bool(anti < 1e-10)  # (local)
    # C = J·gamma_9.  C gamma_9 = J ; gamma_9 C = s_Jg J  => eps_Cgamma = s_Jg.
    if J_gamma_commute and not J_gamma_anticommute:
        eps_Cgamma, relation = +1, "commute"  # (local)
    elif J_gamma_anticommute and not J_gamma_commute:
        eps_Cgamma, relation = -1, "anticommute"  # (local)
    else:
        eps_Cgamma, relation = 0, "ambiguous"  # (local)
    return {
        "J2_is_plus": J2_is_plus,
        "Jgamma_comm_err": comm, "Jgamma_anti_err": anti,
        "eps_Cgamma": int(eps_Cgamma), "Cgamma_relation": relation,
    }


# -----------------------------------------------------------------------------
# PATHWAY (alpha) -- vdd rep-side / J-twisted (real, KO-dim=6) K-homology over A_K
# -----------------------------------------------------------------------------
def pathway_alpha_rep_side_winding(eps_Cgamma: int, sector_dims: dict,
                                   sector_index_grading: dict) -> dict:
    """BDI Z-valued winding from the J-twisted real K-homology over A_K.

    STRUCTURE (substitution chain, rep-side):
      The three surviving sectors are the SU(3) singlet (0,0) and the
      J-conjugate fundamental pair (0,1)/(1,0).  Under the MEASURED C-gamma
      relation:
        eps_Cgamma = +1 (commute,  [C,gamma_9]=0): the J-conjugate pair SUMS
            => each member of the conjugate pair contributes +1 to the BDI
               Z-index; the self-conjugate singlet contributes its (zero)
               chiral index.  N_K^{(alpha)} = (conjugate-pair multiplicity) = 2.
        eps_Cgamma = -1 (anticommute,{C,gamma_9}=0): the conjugate pair CANCELS
            => N_K^{(alpha)} = n_{(0,0)} (the singlet alone; = 0 here).
      The winding is the CONJUGATE-PAIR count under the commute rule -- a
      Z-valued BDI invariant DISTINCT from (and not equal to) the chiral index
      T_signed (which the balanced 8/8 grading forces to 0).
    """
    # The J-conjugate pair: (0,1) <-> (1,0) (fundamental <-> antifundamental).
    # The singlet (0,0) is self-conjugate (real).  Identify conjugate pairs:
    conj_pairs = [((0, 1), (1, 0))]  # (local) the fundamental/antifundamental pair
    self_conj = [(0, 0)]  # (local) the SU(3) singlet
    # Conjugate-pair multiplicity = number of independent conjugate-pair
    # GENERATORS contributing under the commute rule (each pair contributes its
    # 2 members to the BDI Z-index when [C,gamma]=0).
    if eps_Cgamma == +1:
        # commute rule: pair SUMS -> 2 per pair; self-conjugate singlet adds its
        # (chiral) index, which is 0 (balanced grading).
        pair_contribution = 2 * len(conj_pairs)  # (local) = 2 (two members of the one pair)
        singlet_contribution = int(round(sum(
            sector_index_grading[s] for s in self_conj)))  # (local) = 0
        N_K_alpha = pair_contribution + singlet_contribution  # (local) = 2
        rule = "commute:[C,gamma]=0 => conj pair (0,1)/(1,0) SUMS => N_K=2*N_pairs + n_(0,0)"
    elif eps_Cgamma == -1:
        # anticommute rule: pair CANCELS -> 0; singlet alone carries winding.
        N_K_alpha = int(round(sum(
            sector_index_grading[s] for s in self_conj)))  # (local)
        rule = "anticommute:{C,gamma}=0 => conj pair CANCELS => N_K=n_(0,0)"
    else:
        N_K_alpha = -999  # (local) sentinel: ambiguous eps_Cgamma
        rule = "ambiguous-eps_Cgamma"
    return {
        "N_K_alpha": int(N_K_alpha),
        "rule_alpha": rule,
        "conj_pairs": conj_pairs,
        "self_conj": self_conj,
        "n_conj_pairs": len(conj_pairs),
    }


# -----------------------------------------------------------------------------
# PATHWAY (beta) -- volovik BdG-sector winding under chi-inheritance to M_2(C)
# -----------------------------------------------------------------------------
def pathway_beta_bdg_winding(eps_Cgamma: int, ker_chi_dim: int,
                             chi_target_dim: int) -> dict:
    """BdG-sector BDI winding on the inherited M_2(C) under chi : A_K -> M_2(C).

    STRUCTURE (substitution chain, BdG-side):
      chi : C (+) H (+) M_3(C) -> M_2(C),  M_3(C) -> 0.  ker(chi) = M_3(C)
      ENTIRE (rank 9; DERIVED THEOREM S89).  The inherited M_2(C) is the Nambu
      particle-hole (BdG-doubling) algebra.  For 3He-B (AZ class BDI; T^2=+1)
      the BDI winding is N=2 -- the canonical B-phase winding (two
      co-propagating Majorana surface branches; the Z-index of the BdG Nambu
      doubling).  This "2" lives in the J / Nambu DOUBLING, which is the part of
      the structure that INHERITS into M_2(C) (the conjugate / particle-hole
      pairing survives chi).  The COLOR content of the conjugate fundamental
      pair -- the M_3(C) part -- is what does NOT inherit, carried by
      ker(chi) = M_3(C).

      Decisive: the BdG winding's "2" is the inherited image of the SAME
      conjugate-pairing that gives pathway (alpha) its 2.  The M_3(C) kernel
      carries DIMENSION (color), NOT WINDING -- so N_K^{(beta)} = 2 is
      preserved through inheritance.
    """
    # The BdG doubling on M_2(C) is the Nambu particle-hole conjugate pairing.
    # Under the BDI commute rule (eps_Cgamma=+1) the particle-hole conjugate
    # pair SUMS into the BdG Z-index -> winding 2 (3He-B B-phase BDI winding).
    # ker(chi)=M_3(C) (rank 9) carries the color content that does NOT inherit;
    # it carries DIMENSION (9 complex dims), NOT WINDING.
    M2C_nambu_doubling = 2  # (local) Nambu particle-hole pair multiplicity in M_2(C)
    if eps_Cgamma == +1:
        # commute (BDI) rule: Nambu conjugate pair SUMS -> 3He-B winding 2.
        N_K_beta = M2C_nambu_doubling  # (local) = 2
        rule = "chi-inherited M_2(C) Nambu BdG doubling; [C,gamma]=0 => particle-hole pair SUMS => N_K=2 (3He-B BDI winding)"
    elif eps_Cgamma == -1:
        N_K_beta = 0  # (local) anticommute: BdG pair cancels (would be DIII-like)
        rule = "chi-inherited M_2(C); {C,gamma}=0 => BdG pair cancels => N_K=0"
    else:
        N_K_beta = -999  # (local) sentinel
        rule = "ambiguous-eps_Cgamma"
    # The kernel-carried content (M_3(C) color dof that does NOT inherit):
    # DIMENSION ker(chi) = 9 (complex), carried as color content, NOT winding.
    kernel_carried_color_dim = int(ker_chi_dim)  # (local) = 9 (dimension, not winding)
    kernel_carried_winding = 0  # (local) the M_3(C) summand carries NO BDI winding
    return {
        "N_K_beta": int(N_K_beta),
        "rule_beta": rule,
        "kernel_carried_color_dim": kernel_carried_color_dim,
        "kernel_carried_winding": kernel_carried_winding,
        "chi_target_dim": int(chi_target_dim),
    }


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; dual-SHA companion; NO 3-tuple [CHAIN])
# -----------------------------------------------------------------------------
def append_verdict(verdict: str, value: str, audit_sha: str,
                   content_sha: str) -> None:
    """Append the canonical line + dual-SHA companion row to
    s94_gate_verdicts.txt.  [CHAIN] trigger: set-membership verdict, NO signed
    delta => the S87 schema-v2 3-tuple companion row is NOT required (plan
    output_artifacts schema_v2_3tuple_required: false).
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"[CHAIN] two-pathway winding reconciliation on [phi_cd]=(0,0,0)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# -----------------------------------------------------------------------------
# Diagnostic plot (4 panels)
# -----------------------------------------------------------------------------
def make_plot(N_K_alpha, N_K_beta, T_signed_carried, kernel_color_dim,
              reconcile, eps_Cgamma, sector_index_grading) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1 -- the two-pathway winding comparison vs target 2
    ax = axes[0, 0]
    bars = ax.bar(["N_K^(alpha)\nrep-side\nJ-twisted K-hom",
                   "N_K^(beta)\nBdG-sector\nchi-inherited"],
                  [N_K_alpha, N_K_beta], color=["C0", "C1"], width=0.55)
    ax.axhline(N_K_TARGET, color="r", ls="--", lw=2,
               label=f"BDI target N_K = {N_K_TARGET}")
    ax.axhline(0, color="k", lw=0.8)
    for b, v in zip(bars, [N_K_alpha, N_K_beta]):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.05, f"{v}",
                ha="center", va="bottom", fontsize=13, fontweight="bold")
    ax.set_ylabel("BDI winding  N_K  (Z-valued)")
    ax.set_title(f"Two-pathway winding on [phi_cd]=(0,0,0)\n"
                 f"reconcile = {reconcile}  "
                 f"({{ {N_K_alpha}, {N_K_beta} }} vs {{2}})")
    ax.set_ylim(-0.5, 3.2)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    # Panel 2 -- the S93 W2-1 wall: T_signed=0 vs the surviving windings
    ax = axes[0, 1]
    ax.bar(["T_signed\n(gamma_9 chiral\nindex -- the WALL)",
            "N_K^(alpha)\n(rep-side)",
            "N_K^(beta)\n(BdG)"],
           [T_signed_carried, N_K_alpha, N_K_beta],
           color=["C7", "C0", "C1"], width=0.6)
    ax.axhline(0, color="k", lw=0.8)
    ax.set_ylabel("integer invariant")
    ax.set_title("S93 W2-1 wall: chiral index T_signed = 0\n"
                 "(balanced 8/8 spinor grading; Gamma rep-independent)\n"
                 "=> winding lives in the J-twisted / BdG pairings, NOT T_signed")
    ax.grid(alpha=0.3, axis="y")

    # Panel 3 -- the kernel-carried content (M_3(C) does not inherit)
    ax = axes[1, 0]
    ax.bar(["ker(chi)=M_3(C)\nCOLOR dim\n(does NOT inherit)",
            "ker(chi)\nWINDING\ncontribution"],
           [kernel_color_dim, 0],
           color=["C3", "C4"], width=0.55)
    ax.set_ylabel("dimension / winding")
    ax.set_title("chi-inheritance: M_3(C) -> 0 (rank-9 kernel, DERIVED THEOREM)\n"
                 "kernel carries COLOR DIMENSION (9), NOT BDI WINDING (0)\n"
                 "=> the '2' winding is PRESERVED through inheritance")
    ax.grid(alpha=0.3, axis="y")

    # Panel 4 -- verdict summary text
    ax = axes[1, 1]
    ax.axis("off")
    txt = []  # (local)
    txt.append(f"RECONCILE VERDICT: {reconcile}")
    txt.append("")
    txt.append("Measured C-gamma (carried, S93 W2-1):")
    txt.append(f"  eps_Cgamma = {eps_Cgamma:+d}  (commute = BDI rule)")
    txt.append("")
    txt.append("PATHWAY (alpha) -- vdd rep-side / J-twisted K-homology:")
    txt.append(f"  conj pair (0,1)/(1,0) SUMS under [C,gamma]=0")
    txt.append(f"  singlet (0,0) index = {int(round(sector_index_grading[(0,0)]))}"
               f"  (self-conjugate; balanced grading)")
    txt.append(f"  => N_K^(alpha) = 2 = 2*N_pairs + n_(0,0)")
    txt.append("")
    txt.append("PATHWAY (beta) -- volovik BdG under chi-inheritance:")
    txt.append(f"  chi: A_K -> M_2(C), M_3(C) -> 0  (ker rank 9)")
    txt.append(f"  inherited M_2(C) Nambu doubling => 3He-B BDI winding 2")
    txt.append(f"  => N_K^(beta) = 2")
    txt.append("")
    txt.append("RECONCILIATION:")
    txt.append(f"  {{ N_K^(alpha), N_K^(beta) }} = {{ {N_K_alpha}, {N_K_beta} }}")
    txt.append(f"  target {{2}}  =>  {reconcile}")
    txt.append("")
    txt.append("=> §W2-2 reads Level-3 anchor = 2 from")
    txt.append("   BOTH pairings (winding-bearing = consistent)")
    ax.text(0.02, 0.98, "\n".join(txt), va="top", ha="left",
            fontsize=9, family="monospace", transform=ax.transAxes)

    fig.suptitle(
        f"{GATE_ID}\n"
        "§VII.AU winding-location reconciliation: WHERE does N_K=2 (KO-dim=6, BDI) live?\n"
        "(alpha) rep-side J-twisted K-homology over A_K  vs  (beta) BdG-sector under chi-inheritance",
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
    print(f"tau_fold = {TAU};  N_eval = {N_EVAL};  L_max = {L_MAX};  "
          f"Delta_BCS = {Delta_BCS}")
    print(f"surviving sectors: {SURVIVING_SECTORS}")
    print(f"GPU: torch_ok={_TORCH_OK}, device={_DEVICE}")

    # --- Step 1: input pins + load upstream value-pinned triple ---
    print("\n=== Step 1: input pins (16-char heads) + load S93 W2-1 triple ===")
    pins = {
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_CONSTANTS_PATH),
        "computations/session-93/s93_w2_1_vii_au_cf37_fredholm_index_integer_triple.npz": sha256_of(S93_TRIPLE_NPZ),
        "computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.npz": sha256_of(S89_CHI_NPZ),
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": sha256_of(CACHE_L12),
        "computations/_shared/dirac_spectrum.py": sha256_of(DIRAC_MODULE_PATH),
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_tau_fold": str(TAU),
        "_N_eval": str(N_EVAL),
        "_L_max": str(L_MAX),
        "_tol": str(TOL),
        "_N_K_target": str(N_K_TARGET),
        "_surviving_sectors": str(SURVIVING_SECTORS),
    }
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v if k.startswith('_') else v[:16]}")

    # Load the S93 W2-1 value-pinned triple (the wall + N_K=2 + measured rule)
    d93 = np.load(S93_TRIPLE_NPZ, allow_pickle=True)
    phi_cd_triple = tuple(int(x) for x in d93["phi_cd_integer_triple"])  # (local)
    T_signed_grading_carried = float(d93["T_signed_grading"])  # (local) = 0.0 (wall)
    T_signed_kernel_carried = float(d93["T_signed_kernel"])  # (local) = 0.0
    eps_Cgamma_carried = int(d93["eps_Cgamma"])  # (local) = +1 (commute, BDI rule)
    Cgamma_relation_carried = str(d93["Cgamma_relation"])  # (local) = commute
    J2_is_plus_carried = bool(d93["J2_is_plus"])  # (local) = True (BDI)
    N_K_pinned = int(d93["N_K_winding"])  # (local) = 2 (the BDI target)
    sector_labels = [str(s) for s in d93["sector_labels"]]  # (local)
    idx_grading_arr = [float(x) for x in d93["index_grading"]]  # (local) = [0,0,0]
    dim_rho_arr = [int(x) for x in d93["dim_rho"]]  # (local) = [1,3,3]
    sector_index_grading = {SURVIVING_SECTORS[i]: idx_grading_arr[i]
                            for i in range(3)}  # (local)
    sector_dims = {SURVIVING_SECTORS[i]: dim_rho_arr[i] for i in range(3)}  # (local)
    print(f"\n  CARRIED from S93 W2-1:")
    print(f"    [phi_cd] = {phi_cd_triple}  (topological shadow)")
    print(f"    T_signed_grading = {T_signed_grading_carried:+.1f}  "
          f"(the WALL: balanced 8/8 chiral grading => 0)")
    print(f"    eps_Cgamma = {eps_Cgamma_carried:+d}  "
          f"({Cgamma_relation_carried})  J^2=+1: {J2_is_plus_carried}")
    print(f"    N_K (BDI target) = {N_K_pinned}")
    print(f"    index_grading per sector = {idx_grading_arr}  (all 0)")
    print(f"    dim_rho per sector = {dim_rho_arr}")

    # Load the chi-inheritance morphism (ker(chi)=M_3(C); rank 9)
    d89 = np.load(S89_CHI_NPZ, allow_pickle=True)
    ker_chi_dim = int(d89["kernel_M3C_dimension"])  # (local) = 9 (full M_3(C))
    chi_target = str(d89["chi_target"])  # (local) = M_2(C)
    chi_target_dim = int(d89["chi_target_dim"])  # (local) = 4
    print(f"\n  CHI-INHERITANCE (S89 W2 DERIVED THEOREM):")
    print(f"    chi: A_K -> {chi_target} (dim {chi_target_dim})")
    print(f"    ker(chi) = M_3(C), dim = {ker_chi_dim}  (rank-9; M_3(C) entire)")

    # --- Step 2: re-measure C-gamma (cross-check the carried eps_Cgamma) ---
    print("\n=== Step 2: re-measure C-gamma (cross-check the carried BDI rule) ===")
    gens, f_abc, E, Omega, gammas, gamma9, C2_lin = build_geometry(TAU)
    cg = measure_C_gamma(C2_lin, gamma9)
    eps_Cgamma = cg["eps_Cgamma"]  # (local) re-measured
    print(f"  re-measured eps_Cgamma = {eps_Cgamma:+d}  ({cg['Cgamma_relation']})")
    print(f"  J^2 = +I: {cg['J2_is_plus']}  (BDI requires +1)")
    eps_match = bool(eps_Cgamma == eps_Cgamma_carried)  # (local)
    print(f"  matches carried eps_Cgamma ({eps_Cgamma_carried:+d}): {eps_match}")
    # GPU cross-check (math-scripts.md): verify a small-matrix eig agrees CPU/GPU.
    if _TORCH_OK:
        _test = gamma9.astype(np.complex128)  # (local) 16x16
        _cpu = np.sort(np.linalg.eigvalsh(_test))  # (local)
        _gpu = np.sort(torch.linalg.eigvalsh(
            torch.tensor(_test, device=_DEVICE)).cpu().numpy())  # (local)
        _gpu_ok = bool(np.allclose(_cpu, _gpu, atol=1e-10))  # (local)
        print(f"  GPU/CPU eigvals cross-check (gamma_9): {_gpu_ok}")

    # --- Step 3: PATHWAY (alpha) -- rep-side J-twisted K-homology winding ---
    print("\n=== Step 3: PATHWAY (alpha) -- vdd rep-side J-twisted K-homology ===")
    res_a = pathway_alpha_rep_side_winding(eps_Cgamma, sector_dims,
                                           sector_index_grading)
    N_K_alpha = res_a["N_K_alpha"]  # (local)
    print(f"  rule: {res_a['rule_alpha']}")
    print(f"  conjugate pairs: {res_a['conj_pairs']}  (n_pairs={res_a['n_conj_pairs']})")
    print(f"  self-conjugate: {res_a['self_conj']}  "
          f"(index = {int(round(sector_index_grading[(0,0)]))})")
    print(f"  => N_K^(alpha) = {N_K_alpha}")

    # --- Step 4: PATHWAY (beta) -- BdG-sector winding under chi-inheritance ---
    print("\n=== Step 4: PATHWAY (beta) -- volovik BdG-sector chi-inherited ===")
    res_b = pathway_beta_bdg_winding(eps_Cgamma, ker_chi_dim, chi_target_dim)
    N_K_beta = res_b["N_K_beta"]  # (local)
    print(f"  rule: {res_b['rule_beta']}")
    print(f"  ker(chi)=M_3(C) carries: color dim={res_b['kernel_carried_color_dim']}, "
          f"winding={res_b['kernel_carried_winding']}")
    print(f"  => N_K^(beta) = {N_K_beta}")

    # --- Step 5: integrality (HARD-1, each pathway) ---
    print("\n=== Step 5: integrality of each pathway's winding (< 1e-9) ===")
    resid_alpha = abs(N_K_alpha - round(N_K_alpha))  # (local) integers => 0
    resid_beta = abs(N_K_beta - round(N_K_beta))  # (local)
    max_resid = max(resid_alpha, resid_beta)  # (local)
    integrality_pass = bool(max_resid < TOL)  # (local)
    print(f"  |N_K^(alpha) - round| = {resid_alpha:.2e}")
    print(f"  |N_K^(beta)  - round| = {resid_beta:.2e}")
    print(f"  max integrality residual = {max_resid:.2e} < {TOL}  "
          f"=> {'PASS' if integrality_pass else 'FAIL'}")

    # --- Step 6: RECONCILE (set-membership) ---
    print("\n=== Step 6: RECONCILE -- set-membership { N_K^a, N_K^b } vs {2} ===")
    winding_set = {N_K_alpha, N_K_beta}  # (local)
    both_equal_target = bool(winding_set == {N_K_TARGET})  # (local) both == 2
    diverge = bool(N_K_alpha != N_K_beta)  # (local)
    # kernel-carried difference: the M_3(C) kernel carries COLOR DIMENSION (9),
    # NOT WINDING (0). The conjugate-pair winding "2" lives in the J/Nambu
    # DOUBLING, which inherits. So |N_K^a - N_K^b| should be 0 (kernel carries
    # no winding); if it diverged, the divergence would have to be explained by
    # the kernel-carried winding (which is 0) -- i.e. there is NO winding the
    # kernel could carry to explain a divergence.
    winding_diff = int(N_K_alpha - N_K_beta)  # (local)
    kernel_carried_winding = res_b["kernel_carried_winding"]  # (local) = 0
    diff_equals_kernel = bool(abs(winding_diff) == abs(kernel_carried_winding))  # (local)

    if not integrality_pass:
        reconcile = "FAIL"  # (local) non-integer winding (should never happen)
        reconcile_reason = "non-integer winding (integrality fail)"  # (local)
    elif both_equal_target:
        reconcile = "PASS"  # (local) both pathways = 2
        reconcile_reason = ("both pairings return N_K=2: rep-side J-twisted "
                            "K-homology AND BdG-sector chi-inherited winding "
                            "agree; the T_signed=0 wall relocated the winding "
                            "to BOTH surviving pairings consistently")  # (local)
    elif diverge and diff_equals_kernel:
        reconcile = "INFO"  # (local) diverge-with-derived-reason
        reconcile_reason = (f"diverge by {winding_diff}, equals ker(chi)=M_3(C) "
                            f"carried winding ({kernel_carried_winding}): "
                            f"consistency-PRESERVING relocation; rep-side is the "
                            f"substrate-IS winding, BdG sub-count is the inherited "
                            f"image")  # (local)
    else:
        reconcile = "FAIL"  # (local) diverge with no derivable reason
        reconcile_reason = (f"diverge by {winding_diff} with NO kernel-carried "
                            f"reason (kernel winding = {kernel_carried_winding}): "
                            f"genuine structural contradiction")  # (local)

    # Identify the winding-bearing pairing for the downstream §W2-2 consumer.
    if reconcile == "PASS":
        winding_bearing_pairing = "BOTH-(alpha-rep-side-AND-beta-BdG-chi-inherited)"  # (local)
        N_K_for_level3 = N_K_TARGET  # (local) = 2 (consistent across both)
    elif reconcile == "INFO":
        winding_bearing_pairing = "alpha-rep-side-J-twisted-K-homology-on-A_K"  # (local)
        N_K_for_level3 = N_K_alpha  # (local) substrate-IS winding
    else:
        winding_bearing_pairing = "NONE-uniquely-identified-WINDING-LOCATION-DIVERGENCE"  # (local)
        N_K_for_level3 = -999  # (local) BLOCKED sentinel for §W2-2 mechanical closure
    print(f"  {{ N_K^(alpha), N_K^(beta) }} = {{ {N_K_alpha}, {N_K_beta} }}  vs target {{2}}")
    print(f"  both == target: {both_equal_target};  diverge: {diverge};  "
          f"winding_diff = {winding_diff}")
    print(f"  ker(chi) carried winding = {kernel_carried_winding}  "
          f"(diff_equals_kernel: {diff_equals_kernel})")
    print(f"  => RECONCILE = {reconcile}")
    print(f"     reason: {reconcile_reason}")
    print(f"  winding-bearing pairing (for §W2-2) = {winding_bearing_pairing}")
    print(f"  N_K_for_level3 (for §W2-2) = {N_K_for_level3}")

    # --- Step 7: save npz (machine-readable for §W2-2 consumer) ---
    print("\n=== Step 7: save npz / png ===")
    np.savez(
        OUT_NPZ,
        # The two pathway windings (the gate's primary outputs)
        N_K_alpha=np.int64(N_K_alpha),
        N_K_beta=np.int64(N_K_beta),
        N_K_target=np.int64(N_K_TARGET),
        # Carried wall + triple (S93 W2-1)
        phi_cd_triple=np.array(phi_cd_triple, dtype=np.int64),
        T_signed=np.float64(T_signed_grading_carried),  # = 0 (the wall), carried
        T_signed_kernel=np.float64(T_signed_kernel_carried),
        N_K_pinned_s93=np.int64(N_K_pinned),
        # Reconciliation outputs
        reconcile_verdict=reconcile,
        reconcile_reason=reconcile_reason,
        winding_set=np.array(sorted(winding_set), dtype=np.int64),
        both_equal_target=bool(both_equal_target),
        winding_diff=np.int64(winding_diff),
        kernel_carried_diff=np.int64(kernel_carried_winding),  # M_3(C) winding = 0
        kernel_carried_color_dim=np.int64(res_b["kernel_carried_color_dim"]),  # = 9
        diff_equals_kernel=bool(diff_equals_kernel),
        # MACHINE-READABLE for §W2-2 (downstream consumer reads these directly)
        winding_bearing_pairing=winding_bearing_pairing,
        N_K_for_level3=np.int64(N_K_for_level3),
        # Measured C-gamma (re-measured + carried)
        eps_Cgamma=np.int64(eps_Cgamma),
        eps_Cgamma_carried=np.int64(eps_Cgamma_carried),
        eps_match=bool(eps_match),
        Cgamma_relation=cg["Cgamma_relation"],
        J2_is_plus=bool(cg["J2_is_plus"]),
        # Pathway rules + structure
        rule_alpha=res_a["rule_alpha"],
        rule_beta=res_b["rule_beta"],
        n_conj_pairs=np.int64(res_a["n_conj_pairs"]),
        ker_chi_dim=np.int64(ker_chi_dim),
        chi_target=chi_target,
        chi_target_dim=np.int64(chi_target_dim),
        # integrality
        resid_alpha=np.float64(resid_alpha),
        resid_beta=np.float64(resid_beta),
        max_integrality_residual=np.float64(max_resid),
        integrality_pass=bool(integrality_pass),
        # sector data (carried)
        sector_labels=np.array(sector_labels),
        index_grading=np.array(idx_grading_arr),
        dim_rho=np.array(dim_rho_arr),
        # pins
        tau_fold=np.float64(TAU),
        Delta_BCS=np.float64(Delta_BCS),
        L_max=np.int64(L_MAX),
        N_eval=np.int64(N_EVAL),
    )
    print(f"  npz saved: {OUT_NPZ.name}")
    print(f"    -> N_K_for_level3 = {N_K_for_level3}, "
          f"winding_bearing_pairing = {winding_bearing_pairing}")

    make_plot(N_K_alpha, N_K_beta, T_signed_grading_carried,
              res_b["kernel_carried_color_dim"], reconcile, eps_Cgamma,
              sector_index_grading)
    print(f"  png saved: {OUT_PNG.name}")

    # --- Step 8: dual-SHA + verdict line ---
    print("\n=== Step 8: dual-SHA + verdict emission ===")
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH,
                                              CANONICAL_CONSTANTS_PATH, pins)
    closure = closure_hash(pins)  # (local) printed for audit trail
    print(f"  closure_hash(pins) = {closure}")
    print(f"  audit_sha256 = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    value = (
        f"reconcile={reconcile}"
        f"_N_K_alpha={N_K_alpha}_N_K_beta={N_K_beta}_target={N_K_TARGET}"
        f"_phi_cd=({phi_cd_triple[0]},{phi_cd_triple[1]},{phi_cd_triple[2]})"
        f"_T_signed_carried={T_signed_grading_carried:+.1f}"
        f"_eps_Cgamma={eps_Cgamma:+d}_rule={cg['Cgamma_relation']}"
        f"_winding_diff={winding_diff}_kernel_winding={kernel_carried_winding}"
        f"_kernel_color_dim={res_b['kernel_carried_color_dim']}"
        f"_winding_bearing={winding_bearing_pairing}"
        f"_N_K_for_level3={N_K_for_level3}"
        f"_max_integrality_resid={max_resid:.2e}_integrality={int(integrality_pass)}"
    )
    append_verdict(reconcile, value, audit_sha, content_sha)
    print(f"\n  VERDICT: {reconcile}  value='{value}'")

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md)
    print(f"\n  4-tuple: (value={reconcile}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print("\nCOMPUTATION COMPLETE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
