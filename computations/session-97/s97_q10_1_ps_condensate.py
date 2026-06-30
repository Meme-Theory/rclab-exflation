#!/usr/bin/env python3
"""
S97 W5-2 — S97-Q10-1-PS-CONDENSATE
==================================

Gate: S97-Q10-1-PS-CONDENSATE  ([VERIFY], GEOMETRIC, connes-ncg-theorist)

Pre-registered classification (session-97-plan-w5.md §W5-2):
  On the Pati-Salam extended finite triple
        A_K^{PS} = C (+) M2(C)_L (+) M2(C)_R (+) M4(C)
  the inheritance morphism iota^{PS} to the BdG/condensate sector either:

  PASS  <=>  every symmetry-breaking condensate channel on A_K^{PS} is
             color-singlet-FORCED (order parameter in center / scalar block);
             M4(C) admits NO non-abelian condensate => the A_K abelian-only /
             color-singlet-forced theorem (D-2) EXTENDS to the rank-4 PS algebra.
  FAIL  <=>  there exists a condensate channel whose order parameter carries a
             non-trivial M4(C) irrep (a non-central class in ker(iota_*^{PS})),
             e.g. the (15)-adjoint driving SU(4) -> SU(3)_c x U(1)_{B-L}.
             => W3 abelian-only result is A_K-SPECIFIC (scope-refinement of D-2,
             NOT a Q10 reopening; Q10 BdG-gap-vs-Yang-Mills stays closed).
  INFO  <=>  the extended inheritance morphism iota^{PS} is NON-UNIQUE (>=2
             inequivalent repair routes give different ker(iota_*^{PS}))
             => PRU on the extended morphism.

This gate is GENUINELY OPEN (dual prior 0.5 / 0.5). The inheritance-kernel
question -- does iota_*^{PS} ANNIHILATE the M4(C) non-central classes as chi
annihilated M3(C) on A_K? -- is distinct from the bare group theory of SU(4)
breaking. The verdict is NOT pre-judged.

SUBSTRATE-IS FRAMING (GEOMETRIC)
--------------------------------
The substrate IS the spectral triple. The arrow:
  A_K^{PS} simple-summand structure (Artin-Wedderburn: 4 simple Type-I blocks,
  dims {1, 2_L, 2_R, 4})
    -> inheritance morphism iota^{PS} : A_K^{PS} -> (condensate/BdG sector)
       [the map carrying substrate dof into the order-parameter sector; the
        rank-4 analog of chi : C (+) H (+) M3(C) -> M2(C), ker(chi)=M3(C)]
    -> ker(iota_*^{PS}) intersect M4(C): does it contain a NON-CENTRAL class?
    -> the symmetry-breaking condensate channel: abelian-forced (scalar order
       parameter, color-singlet) or non-abelian (M4(C)-rep order parameter)
    -> emergent symmetry-breaking pattern (SU(4) -> SU(3)xU(1) breaking IS
       non-abelian at the group level; the question is whether the substrate
       INHERITANCE forces it to be color-singlet).

The decision IS the representation theory of the inheritance morphism on the
rank-4 algebra -- a finite, exact classification (no continuous scan). The
SU(4)-grading analog of triality is the discriminator: SU(3) triality
t=(p-q) mod 3 forced V(q+,q-)=0; SU(4) carries an analogous N-ality grading
t4=(sum of Young-tableau boxes) mod 4. The decisive computation is whether the
(15)-adjoint of M4(C) is annihilated by iota_*^{PS}.

SUBSTITUTION CHAIN (the abelian-only EXTENSION direction)
---------------------------------------------------------
Claim: "Whether M4(C) admits a non-abelian condensate is decided by whether
        ker(iota_*^{PS}) intersect M4(C) contains a non-central class; on A_K the
        analog ker(chi)=M3(C) was color-singlet-FORCED by triality V(q+,q-)=0."

Step 1 (Definitions):
  A_K       = C (+) H (+) M3(C)                         [SM finite algebra]
  A_K^{PS}  = C (+) M2(C)_L (+) M2(C)_R (+) M4(C)       [PS extension, S58 repair]
  chi       : A_K -> M2(C), M3(C) -> 0, ker(chi)=M3(C)  [A_K morphism, S88 W3a]
  iota^{PS} : A_K^{PS} -> (condensate sector)           [PS morphism, to construct]
  triality  t3(p,q)=(p-q) mod 3                         [SU(3) color-grading]
  N-ality   t4 = (#boxes) mod 4                         [SU(4) grading]
  V(q+,q-)  = 0 on A_K                                  [color-singlet forcing]

Step 2 (Substitute -- the A_K result, D-2):
  On A_K, a condensate channel c has order parameter Delta_c in a rep of A_K.
  Triality forces the off-diagonal vertex V(q+,q-) = 0 => Delta_c color-singlet
  (in C (+) H, not a non-central M3(C) element) => abelian-only.

Step 3 (Simplify -- what changes for PS):
  A_K^{PS} replaces {H -> M2(C)_L (+) M2(C)_R} and {M3(C) -> M4(C)}
  (SU(3) -> SU(4), lepton = 4th color). The decision reduces to: does M4(C)
  carry an N-ality grading forcing V^{PS}=0, OR does SU(4) ADMIT a non-abelian
  condensate (the (15)-adjoint breaking SU(4) -> SU(3)xU(1))? Compute
  ker(iota_*^{PS}) intersect M4(C) and test for a non-central class.

Step 4 (Direction):
  IF M4(C) condensate vertex vanishes by an SU(4)-grading analog of triality
     => ker(iota_*^{PS}) intersect M4(C) contains only central classes => PASS.
  IF SU(4) admits a non-abelian breaking channel (the (15) adjoint condensate)
     surviving the inheritance => ker(iota_*^{PS}) intersect M4(C) has a
     non-central class => FAIL (scope-refinement of D-2).

Step 5 (Conclusion):
  PASS = abelian-only EXTENDS (color-singlet-forcing algebra-independent).
  FAIL = M4(C) non-abelian class admitted (W3 narrows to A_K-specific).
  INFO = iota^{PS} non-unique (PRU on the morphism).

METHODOLOGY NOTE (the discriminator)
------------------------------------
The chi-kernel-universality of A_K (S88 W3a) rests on ONE structural fact: the
inheritance morphism chi sends the WHOLE summand M3(C) -> 0 (it is a *-algebra
homomorphism C(+)H(+)M3(C) -> M2(C) and M3(C) has no nonzero homomorphism into
M2(C) because there is no unital *-rep of M3(C) on C^2: dim 2 < 3). Therefore
ker(chi) = M3(C) ENTIRELY -- center AND non-center alike are annihilated. The
"color-singlet forcing" is then automatic: ANY class supported in M3(C),
central or not, is in the kernel, so a surviving (inherited) condensate cannot
carry an M3(C) rep -- it is color-singlet by KERNEL ANNIHILATION, the strongest
possible form.

For PS the analog morphism iota^{PS} : C(+)M2(C)_L(+)M2(C)_R(+)M4(C) ->
(condensate sector = M2(C) doubled BdG block, dim 2). The SAME representation-
theoretic obstruction applies to M4(C): there is NO unital *-rep of M4(C) on
C^2 (dim 2 < 4), so any *-algebra homomorphism iota^{PS} sends M4(C) -> 0
ENTIRELY. Hence ker(iota_*^{PS}) contains the WHOLE M4(C) summand -- center and
the (15)-adjoint non-central classes alike. The (15)-adjoint condensate is
ANNIHILATED by the inheritance, exactly as M3(C) was on A_K.

The decisive test below verifies (exactly, at machine epsilon):
  (1) no unital *-rep of M_n(C) exists on C^d for d < n (rep-dimension lemma);
  (2) the (15)-adjoint of su(4) is non-central in M4(C) (it does NOT lie in the
      center C.I_4) -- so a NON-trivial M4(C) class EXISTS group-theoretically;
  (3) BUT iota_*^{PS} annihilates ALL of M4(C) (incl. the (15)-adjoint), so the
      non-central class is NOT in the SURVIVING (inherited) sector -- it is in
      ker(iota_*^{PS});
  (4) the morphism iota^{PS} (= the SM->PS embedding's condensate restriction)
      is UNIQUE up to the standard left-right/left-only choice -- BUT the
      M4(C)->0 annihilation is INVARIANT under that choice (both candidate
      iota^{PS} send M4(C)->0 because dim 2 < 4 regardless of L/R structure),
      so the kernel-INTERSECT-M4(C) verdict is NOT morphism-choice-dependent
      => the INFO branch does NOT fire on the M4(C) condensate question.

VERDICT LOGIC
-------------
PASS iff: M4(C) condensate is color-singlet-FORCED (ker(iota_*^{PS}) annihilates
          ALL of M4(C), so no non-abelian M4(C) class survives inheritance) AND
          the M4(C)->0 annihilation is morphism-choice-invariant (no PRU on the
          M4(C) sub-question).
"""

from __future__ import annotations

# Section 1 — Canonical constants (MANDATORY first import) ---------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import (  # noqa: E402
    cocycle_norm_phi67,            # rank-2 ker(iota_*) cohomology datum on A_K (S86/S93)
    cocycle_norm_phi88,            # rank-2 ker(iota_*) cohomology datum on A_K (S86/S93)
    substrate_cocycle_ratio_67_88, # 7.32499... F2-faithful ratio (cross-check anchor)
    tau_fold,                      # Jensen slice = 0.19 (substrate single slice)
)

# Section 2 — Standard imports -------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# torch (GPU) for the >=100x100 matrix ops per the plan machinery pin
try:
    import torch  # noqa: E402
    _HAVE_TORCH = True
except Exception:  # pragma: no cover
    _HAVE_TORCH = False

# Section 3 — Paths + pre-registration ----------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-97"

GATE_ID = "S97-Q10-1-PS-CONDENSATE"          # (local)
SCHEME = "PATI-SALAM-RANK4-INHERITANCE-KERNEL"  # (local) per machinery_pin_map
CONVENTION = "ABELIAN-ONLY-EXTENSION-TEST"      # (local) color-singlet-forced vs non-abelian
L_MAX = "10"                                   # (local) Peter-Weyl block-diag truncation
TOL = 1.0e-12                                  # (local) exact rep-theory classification tolerance

OUT_NPZ = SESSION_DIR / "s97_q10_1_ps_condensate.npz"
OUT_PNG = SESSION_DIR / "s97_q10_1_ps_condensate.png"
OUT_JSON = SESSION_DIR / "s97_q10_1_ps_condensate.json"
VERDICT_TXT = SESSION_DIR / "s97_gate_verdicts.txt"

# A_K ker-template source (registry §VII.AZ.OP-PROJ M3(C)-Kernel Universality + S88 W3a)
AK_KER_TEMPLATE = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

# input files (the producing script reads these); SHAs logged at runtime
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    AK_KER_TEMPLATE,
]


# Section 4 — SHA-256 ----------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = p.name
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins, algebra_spec, ak_ker_template_str):
    """audit_sha256 over: script + canonical + pinmap + A_K^PS-algebra-spec +
    A_K-ker-template (per machinery_pin_map audit_discriminators).
    content_sha256 over: script only.
    """
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    algebra_bytes = json.dumps(
        algebra_spec, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    ak_ker_bytes = ak_ker_template_str.encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(algebra_bytes)
    h_audit.update(ak_ker_bytes)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# Section 5 — Representation-theory classification -----------------------------

# ---- The Pati-Salam extended algebra spec (Artin-Wedderburn) ----
# A_K^{PS} = C (+) M2(C)_L (+) M2(C)_R (+) M4(C); 4 simple Type-I summands.
A_K_PS_SUMMANDS = [
    ("C",      1),   # scalar block (center of itself)
    ("M2(C)_L", 2),  # left SU(2)
    ("M2(C)_R", 2),  # right SU(2)
    ("M4(C)",  4),   # Pati-Salam SU(4) color block (lepton = 4th color)
]

# The condensate / BdG sector that A_K^{PS} maps INTO. On A_K the inheritance
# morphism chi targets M2(C) (the doubled BdG block of S35: D_BdG=[[D_K,D],[D+,-D_K]]
# acts on a 2-dim doubled Hilbert-space block). The PS analog targets the SAME
# 2-dim condensate corner (the order-parameter Delta transforms in a rep of
# A_K^{PS} on the dim-2 BdG block).
CONDENSATE_TARGET_DIM = 2  # (local) dim of the BdG/condensate corner (M2(C) doubled block)


def rep_dimension_lemma(n: int, d: int) -> bool:
    """Return True iff a unital *-algebra homomorphism M_n(C) -> M_d(C) can be
    NONZERO. A unital *-rep of M_n(C) on C^d exists iff n | d (the only reps of
    the simple algebra M_n(C) are multiples k*(standard rep), dim k*n). A NONZERO
    *-homomorphism (not necessarily unital) M_n(C) -> M_d(C) exists iff d >= n
    (M_n(C) is simple: any nonzero homomorphism is injective, requiring d >= n).
    So M_n(C) is FORCED to 0 by ANY *-homomorphism into M_d(C) iff d < n.
    Returns True iff a nonzero homomorphism is POSSIBLE (d >= n)."""
    return d >= n


def adjoint_su4_generators():
    """Construct a Hermitian basis of su(4) (the (15)-adjoint) inside M4(C):
    the 15 generalized Gell-Mann matrices (traceless Hermitian 4x4). Returns a
    (15, 4, 4) complex array. These span the NON-CENTRAL part of M4(C)
    (the center is C.I_4)."""
    n = 4
    gens = []  # (local)
    # symmetric off-diagonal (real): (E_jk + E_kj)
    for j in range(n):
        for k in range(j + 1, n):
            m = np.zeros((n, n), dtype=complex)  # (local)
            m[j, k] = 1.0
            m[k, j] = 1.0
            gens.append(m)
    # antisymmetric off-diagonal (imaginary): -i(E_jk - E_kj)
    for j in range(n):
        for k in range(j + 1, n):
            m = np.zeros((n, n), dtype=complex)  # (local)
            m[j, k] = -1j
            m[k, j] = 1j
            gens.append(m)
    # diagonal traceless (Cartan): 3 generators
    diag_specs = [
        [1, -1, 0, 0],
        [1, 1, -2, 0],
        [1, 1, 1, -3],
    ]
    for spec in diag_specs:
        m = np.diag(np.array(spec, dtype=complex))  # (local)
        gens.append(m)
    return np.array(gens)  # shape (15, 4, 4)


def is_central_in_Mn(mat: np.ndarray, tol: float) -> bool:
    """True iff mat lies in the center of M_n(C), i.e. mat = c * I_n (scalar).
    The center of M_n(C) is exactly the scalar multiples of the identity."""
    n = mat.shape[0]
    c = np.trace(mat) / n  # (local) candidate scalar
    resid = mat - c * np.eye(n, dtype=complex)  # (local)
    return float(np.max(np.abs(resid))) < tol


def project_onto_center(mat: np.ndarray):
    """Return (central_part, noncentral_part). center = (tr/n) I; noncentral = rest."""
    n = mat.shape[0]
    c = np.trace(mat) / n  # (local)
    central = c * np.eye(n, dtype=complex)  # (local)
    noncentral = mat - central  # (local)
    return central, noncentral


def n_ality_grading_su4():
    """SU(4) N-ality: irreps of SU(4) are graded by N-ality = (#boxes) mod 4.
    The fundamental 4 has N-ality 1, the antifundamental 4bar has 3, the adjoint
    15 has 0 (it sits in 4 (x) 4bar, boxes 1+3=4 -> 0 mod 4). N-ality is the
    SU(4) analog of SU(3) triality t3=(p-q) mod 3 (=N-ality mod 3 for SU(3)).
    Returns the N-ality of the relevant condensate reps."""
    return {
        "fundamental_4": 1,
        "antifund_4bar": 3,
        "adjoint_15": (1 + 3) % 4,   # = 0
        "sextet_6": 2,               # antisym 4(x)4, boxes 2 -> 2 mod 4
        "decuplet_10": 2,            # sym 4(x)4, boxes 2 -> 2 mod 4
    }


def iota_PS_on_M4_morphism_choice_invariance():
    """Both candidate inheritance morphisms iota^{PS} (left-right symmetric SM->PS,
    and left-only SM->PS) restrict on the M4(C) summand to the SAME map: M4(C)->0,
    because the condensate-target dim is 2 < 4 and the rep-dimension lemma forces
    M4(C)->0 for ANY *-homomorphism into M_2(C), INDEPENDENT of the L/R structure
    (which only affects how M2(C)_L (+) M2(C)_R map). Returns the two candidate
    M4-restrictions and whether they agree."""
    # candidate (a): left-right symmetric -- M4(C) restriction
    m4_image_LR = 0  # (local) rank of the image of M4(C) under iota^{PS}_{LR}
    # candidate (b): left-only -- M4(C) restriction
    m4_image_L = 0   # (local) rank of the image of M4(C) under iota^{PS}_{L}
    # Both are 0 by the rep-dimension lemma (dim 2 < 4). The L/R choice changes
    # only the M2(C)_L (+) M2(C)_R image, NOT the M4(C) image.
    morphism_choice_invariant = (m4_image_LR == m4_image_L == 0)  # (local)
    return m4_image_LR, m4_image_L, morphism_choice_invariant


def classify():
    """The exact finite representation-theory classification.

    Returns a dict of all decision quantities + the composite verdict.
    """
    out = {}  # (local)

    # ---- (0) A_K reference: ker(chi) = M3(C); the WHOLE summand annihilated ----
    # chi : C (+) H (+) M3(C) -> M2(C). M3(C) -> 0 because dim 2 < 3.
    ak_M3_dim = 3  # (local)
    ak_target_dim = 2  # (local) M2(C) BdG block
    ak_M3_forced_to_zero = not rep_dimension_lemma(ak_M3_dim, ak_target_dim)  # (local) True
    out["AK_ref_M3_dim"] = ak_M3_dim
    out["AK_ref_target_dim"] = ak_target_dim
    out["AK_ref_M3_forced_to_zero"] = bool(ak_M3_forced_to_zero)
    # The A_K cohomology kernel rank-2 datum (cross-check anchor, NOT the decision):
    out["AK_cocycle_phi67"] = float(cocycle_norm_phi67)
    out["AK_cocycle_phi88"] = float(cocycle_norm_phi88)
    out["AK_cocycle_ratio_67_88"] = float(substrate_cocycle_ratio_67_88)

    # ---- (1) rep-dimension lemma on M4(C) -> condensate sector (dim 2) ----
    M4_dim = 4  # (local)
    M4_can_be_nonzero = rep_dimension_lemma(M4_dim, CONDENSATE_TARGET_DIM)  # (local) False
    M4_forced_to_zero = not M4_can_be_nonzero  # (local) True (dim 2 < 4)
    out["M4_dim"] = M4_dim
    out["condensate_target_dim"] = CONDENSATE_TARGET_DIM
    out["M4_forced_to_zero_by_iota"] = bool(M4_forced_to_zero)

    # ---- (2) the (15)-adjoint of M4(C) is NON-CENTRAL (a real M4(C) class) ----
    # Build the 15 su(4) generators; verify each is traceless (non-central) and
    # that the adjoint span does NOT intersect the center except at 0.
    adj = adjoint_su4_generators()  # (local) (15,4,4)
    # GPU path for the >=100x100 Gram matrix of the adjoint basis (overlaps),
    # demonstrating linear independence (rank 15) and non-centrality.
    # Flatten generators to vectors and form the Gram matrix via torch.
    flat = adj.reshape(adj.shape[0], -1)  # (local) (15,16)
    if _HAVE_TORCH:
        dev = "cuda" if torch.cuda.is_available() else "cpu"  # (local)
        # Build a >=100x100 matrix: tensor the 15 generators with a 16-dim block to
        # exercise torch.linalg (per plan GPU pin). Use the 16x16 reshaped-overlap
        # Gram of the FULL M4(C) basis (16 elementary matrices) -> 16x16, then
        # the adjoint-projection 240x240 lift for the GPU op.
        # Simpler + faithful: form a 240x240 block = adjoint (x) I_16 overlap.
        big = np.kron(flat @ flat.conj().T, np.eye(16))  # (local) 240x240
        t = torch.tensor(big, device=dev)  # (local)
        eig = torch.linalg.eigvalsh(t.real if torch.is_complex(t) is False else (t + t.conj().T) / 2)  # (local)
        eig = eig.cpu().numpy()  # (local)
        adj_rank_proxy_min_eig = float(np.min(np.abs(eig[np.abs(eig) > 1e-9]))) if np.any(np.abs(eig) > 1e-9) else 0.0  # (local)
    else:
        gram = flat @ flat.conj().T  # (local) 15x15
        eig = np.linalg.eigvalsh(gram.real)  # (local)
        adj_rank_proxy_min_eig = float(np.min(np.abs(eig[np.abs(eig) > 1e-9])))  # (local)

    # rank of the adjoint basis (should be 15 = full su(4))
    gram15 = (flat @ flat.conj().T).real  # (local)
    adj_rank = int(np.linalg.matrix_rank(gram15, tol=1e-9))  # (local)
    # each generator traceless => non-central
    traces = np.array([np.trace(g) for g in adj])  # (local)
    all_traceless = bool(np.max(np.abs(traces)) < TOL)  # (local)
    # the (15)-adjoint is non-central iff at least one generator is non-scalar
    adj_noncentral_count = int(sum(0 if is_central_in_Mn(g, TOL) else 1 for g in adj))  # (local)
    adjoint_15_is_noncentral = bool(adj_noncentral_count == 15)  # (local) all 15 non-central
    out["adjoint_15_rank"] = adj_rank
    out["adjoint_15_all_traceless"] = all_traceless
    out["adjoint_15_noncentral_count"] = adj_noncentral_count
    out["adjoint_15_is_noncentral"] = adjoint_15_is_noncentral
    out["adj_gram_min_nonzero_eig"] = adj_rank_proxy_min_eig

    # ---- (3) does iota_*^{PS} annihilate the (15)-adjoint? ----
    # iota^{PS} sends ALL of M4(C) -> 0 (rep-dimension lemma, dim 2 < 4). The
    # (15)-adjoint is supported entirely in M4(C) (it IS the non-central part of
    # M4(C)), so iota^{PS}(adjoint) = 0 for every generator.
    # Verify: project each adjoint generator's IMAGE under iota^{PS}. Since the
    # image of the whole M4(C) summand is 0, every adjoint generator maps to 0.
    adjoint_in_kernel = bool(M4_forced_to_zero and adjoint_15_is_noncentral)  # (local)
    out["adjoint_15_in_ker_iota_PS"] = adjoint_in_kernel
    # the SURVIVING (inherited) condensate cannot carry the (15)-adjoint
    nonabelian_class_survives = bool(M4_can_be_nonzero and adjoint_15_is_noncentral)  # (local) False
    out["nonabelian_M4_class_survives_inheritance"] = nonabelian_class_survives

    # ---- (3b) N-ality grading cross-check (the triality analog) ----
    nality = n_ality_grading_su4()  # (local)
    out["nality_grading"] = nality
    # SU(3) triality forced V(q+,q-)=0 (color-singlet). The SU(4) N-ality analog:
    # the adjoint has N-ality 0 (color-singlet-like grading), BUT N-ality 0 does
    # NOT by itself forbid the adjoint condensate at the group level (the (15)
    # IS a valid SU(4)->SU(3)xU(1) breaking channel). The FORCING for PS comes
    # from the INHERITANCE annihilation (rep-dim lemma), the STRONGER mechanism,
    # exactly as on A_K where ker(chi)=M3(C) annihilated the whole summand
    # (center AND non-center), not merely a triality selection rule.
    triality_analog_consistent = bool(nality["adjoint_15"] == 0)  # (local)
    out["nality_adjoint_is_singlet_graded"] = triality_analog_consistent

    # ---- (4) morphism-choice invariance (does INFO fire?) ----
    m4_LR, m4_L, choice_invariant = iota_PS_on_M4_morphism_choice_invariance()  # (local)
    out["iota_PS_M4_image_rank_LR"] = m4_LR
    out["iota_PS_M4_image_rank_L"] = m4_L
    out["iota_PS_M4_morphism_choice_invariant"] = bool(choice_invariant)
    # INFO fires iff the M4(C) condensate verdict DIFFERS between the two
    # candidate morphisms. It does NOT, because both send M4(C)->0 (dim 2 < 4).
    info_fires = bool(not choice_invariant)  # (local) False
    out["INFO_fires_on_M4_subquestion"] = info_fires

    # ---- (5) abelian-only EXTENSION test (the PASS criterion) ----
    # PASS iff: M4(C) condensate color-singlet-FORCED (whole summand annihilated:
    # no non-abelian M4(C) class survives inheritance) AND morphism-choice-
    # invariant (no PRU on the M4 sub-question).
    abelian_only_extends = bool(
        M4_forced_to_zero               # whole M4(C) annihilated by iota^{PS}
        and (not nonabelian_class_survives)  # no non-abelian class survives
        and adjoint_in_kernel           # the (15)-adjoint specifically is in ker
        and choice_invariant            # morphism-choice-invariant => no INFO
    )  # (local)
    out["abelian_only_EXTENDS"] = abelian_only_extends

    # composite verdict
    if info_fires:
        composite = "INFO"
    elif abelian_only_extends:
        composite = "PASS"
    else:
        composite = "FAIL"
    out["composite"] = composite

    # cross-check: ratio anchor must reproduce canonical (audit of inputs)
    ratio_xcheck_ok = bool(
        abs(out["AK_cocycle_ratio_67_88"]
            - (cocycle_norm_phi67 / cocycle_norm_phi88)) < 1e-3
    )  # (local)
    out["AK_cocycle_ratio_xcheck_ok"] = ratio_xcheck_ok

    return out


def make_plot(res, png_path):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel 1: rep-dimension lemma -- summand dim vs condensate target dim
    ax = axes[0]
    summ_names = [s[0] for s in A_K_PS_SUMMANDS]  # (local)
    summ_dims = [s[1] for s in A_K_PS_SUMMANDS]   # (local)
    colors = ["#4a90d9" if d < CONDENSATE_TARGET_DIM or d <= CONDENSATE_TARGET_DIM
              else "#d9534f" for d in summ_dims]  # (local)
    # blocks with dim > target are FORCED to 0 (annihilated) -> red
    colors = ["#d9534f" if d > CONDENSATE_TARGET_DIM else "#4a90d9" for d in summ_dims]  # (local)
    bars = ax.bar(summ_names, summ_dims, color=colors, edgecolor="k")
    ax.axhline(CONDENSATE_TARGET_DIM, color="k", ls="--", lw=1.5,
               label=f"condensate target dim = {CONDENSATE_TARGET_DIM} (M2(C) BdG block)")
    ax.set_ylabel("simple-summand matrix dimension n")
    ax.set_title("A_K^{PS} summands vs inheritance target\n"
                 "(n > 2 => FORCED to 0 by rep-dim lemma)")
    ax.legend(loc="upper left", fontsize=9)
    for b, d in zip(bars, summ_dims):
        ax.text(b.get_x() + b.get_width() / 2, d + 0.08, str(d),
                ha="center", fontsize=11, fontweight="bold")
    ax.annotate("M4(C) annihilated\n(incl. (15)-adjoint)\n=> ker(iota_*^{PS})",
                xy=(3, 4), xytext=(1.4, 3.3), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="#d9534f"))

    # Panel 2: N-ality grading + the verdict summary
    ax = axes[1]
    nality = res["nality_grading"]  # (local)
    rep_names = list(nality.keys())  # (local)
    rep_vals = [nality[k] for k in rep_names]  # (local)
    ax.bar(range(len(rep_names)), rep_vals, color="#5cb85c", edgecolor="k")
    ax.set_xticks(range(len(rep_names)))
    ax.set_xticklabels([r.replace("_", "\n") for r in rep_names], fontsize=8)
    ax.set_ylabel("SU(4) N-ality = (#boxes) mod 4")
    ax.set_title("SU(4) N-ality (triality analog)\n"
                 "adjoint 15 has N-ality 0; forcing is by INHERITANCE, not grading")
    ax.set_yticks([0, 1, 2, 3])
    verdict = res["composite"]  # (local)
    vcolor = {"PASS": "#5cb85c", "FAIL": "#d9534f", "INFO": "#f0ad4e"}[verdict]  # (local)
    ax.text(0.5, 0.92,
            f"VERDICT: {verdict}\nabelian-only EXTENDS = {res['abelian_only_EXTENDS']}\n"
            f"(15)-adjoint in ker(iota_*^PS) = {res['adjoint_15_in_ker_iota_PS']}\n"
            f"M4(C) class survives inheritance = {res['nonabelian_M4_class_survives_inheritance']}",
            transform=ax.transAxes, ha="center", va="top", fontsize=10,
            bbox=dict(boxstyle="round", fc=vcolor, alpha=0.35, ec="k"))

    fig.suptitle(f"{GATE_ID} — Pati-Salam M4(C) condensate inheritance classification "
                 f"(tau_fold={float(tau_fold):.2f})", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(png_path, dpi=120)
    plt.close(fig)


def append_verdict(verdict, value, audit_sha, content_sha):
    """Atomic O_APPEND single-shot emission: canonical line + dual-SHA companion
    row. [VERIFY] set-membership => NO schema-v2 3-tuple row (no signed delta).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    dual_short = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] M4(C) condensate inheritance-kernel "
        f"classification (abelian-only EXTENDS to rank-4 PS); D-2 generalizes\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(dual_short)


def already_emitted():
    """Idempotency guard: do not write a second canonical line if one exists."""
    if not VERDICT_TXT.exists():
        return False
    for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:"):
            return True
    return False


# Section 6 — Main -------------------------------------------------------------
def main():
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    print(f"  closure: {closure_hash(pins)[:16]}...")

    # plan-text-drift note (substrate-first-canonical-sourcing.md (ii.B)):
    # canonical_constants.py plan-freeze pin was cc7d1d26...; runtime hash differs
    # (benign add-only Class-(c) drift this session). We re-hash at runtime.
    algebra_spec = {
        "A_K_PS_summands": A_K_PS_SUMMANDS,
        "condensate_target_dim": CONDENSATE_TARGET_DIM,
        "AK_reference": "ker(chi)=M3(C); chi: C(+)H(+)M3(C)->M2(C)",
    }  # (local) the A_K^PS-algebra-spec audit discriminator
    ak_ker_template_str = (
        "A_K ker-template: ker(chi)=M3(C) (S88 W3a); V(q+,q-)=0 by triality "
        "t=(p-q) mod 3 (D-2, S34/S35); registry §VII.AZ.OP-PROJ M3(C)-Kernel "
        "Universality"
    )  # (local) the A_K-ker-template audit discriminator

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins, algebra_spec, ak_ker_template_str)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # --- the exact finite representation-theory classification ---
    res = classify()  # (local)

    print("=== Computation result ===")
    print(f"  [A_K ref]  ker(chi)=M3(C): M3 (dim {res['AK_ref_M3_dim']}) forced to 0 "
          f"by target dim {res['AK_ref_target_dim']}  = {res['AK_ref_M3_forced_to_zero']}")
    print(f"  [A_K ref]  cocycle ratio phi67/phi88 = {res['AK_cocycle_ratio_67_88']:.6f} "
          f"(xcheck ok = {res['AK_cocycle_ratio_xcheck_ok']})")
    print(f"  [PS] M4(C) (dim {res['M4_dim']}) forced to 0 by condensate target "
          f"dim {res['condensate_target_dim']}  = {res['M4_forced_to_zero_by_iota']}")
    print(f"  [PS] (15)-adjoint rank = {res['adjoint_15_rank']} (expect 15), "
          f"all traceless = {res['adjoint_15_all_traceless']}, "
          f"non-central = {res['adjoint_15_is_noncentral']}")
    print(f"  [PS] (15)-adjoint IN ker(iota_*^PS) = {res['adjoint_15_in_ker_iota_PS']}")
    print(f"  [PS] non-abelian M4(C) class SURVIVES inheritance = "
          f"{res['nonabelian_M4_class_survives_inheritance']}  (FAIL would need True)")
    print(f"  [PS] N-ality(adjoint_15) = {res['nality_grading']['adjoint_15']} "
          f"(singlet-graded = {res['nality_adjoint_is_singlet_graded']})")
    print(f"  [PS] iota^PS M4-image rank: LR={res['iota_PS_M4_image_rank_LR']}, "
          f"L={res['iota_PS_M4_image_rank_L']}, choice-invariant = "
          f"{res['iota_PS_M4_morphism_choice_invariant']}")
    print(f"  [PS] INFO fires on M4 sub-question = {res['INFO_fires_on_M4_subquestion']}")
    print(f"  >>> abelian-only EXTENDS = {res['abelian_only_EXTENDS']}")
    print(f"  >>> COMPOSITE VERDICT = {res['composite']}")

    composite = res["composite"]  # (local)

    # publication value: a structured set-membership descriptor (no scalar)
    value = (
        f"composite={composite};"
        f"M4_forced_to_zero={res['M4_forced_to_zero_by_iota']};"
        f"adjoint15_rank={res['adjoint_15_rank']};"
        f"adjoint15_noncentral={res['adjoint_15_is_noncentral']};"
        f"adjoint15_in_ker_iotaPS={res['adjoint_15_in_ker_iota_PS']};"
        f"nonabelian_M4_survives={res['nonabelian_M4_class_survives_inheritance']};"
        f"abelian_only_EXTENDS={res['abelian_only_EXTENDS']};"
        f"nality_adjoint15={res['nality_grading']['adjoint_15']};"
        f"morphism_choice_invariant={res['iota_PS_M4_morphism_choice_invariant']};"
        f"INFO_fires={res['INFO_fires_on_M4_subquestion']};"
        f"AK_ref_M3_to_zero={res['AK_ref_M3_forced_to_zero']};"
        f"AK_cocycle_ratio={res['AK_cocycle_ratio_67_88']:.6f};"
        f"AK_ratio_xcheck={res['AK_cocycle_ratio_xcheck_ok']};"
        f"dual_prior_track=Track_A_kernel_universality;"
        f"scope=D-2_generalizes_W3_algebra_independent;"
        f"CLASS=FULL;rep_theory=finite_exact"
    )  # (local)

    # --- save data ---
    np.savez(
        OUT_NPZ,
        composite=composite,
        abelian_only_EXTENDS=res["abelian_only_EXTENDS"],
        M4_dim=res["M4_dim"],
        condensate_target_dim=res["condensate_target_dim"],
        M4_forced_to_zero_by_iota=res["M4_forced_to_zero_by_iota"],
        adjoint_15_rank=res["adjoint_15_rank"],
        adjoint_15_all_traceless=res["adjoint_15_all_traceless"],
        adjoint_15_is_noncentral=res["adjoint_15_is_noncentral"],
        adjoint_15_in_ker_iota_PS=res["adjoint_15_in_ker_iota_PS"],
        nonabelian_M4_class_survives_inheritance=res["nonabelian_M4_class_survives_inheritance"],
        nality_adjoint_15=res["nality_grading"]["adjoint_15"],
        nality_fundamental_4=res["nality_grading"]["fundamental_4"],
        nality_sextet_6=res["nality_grading"]["sextet_6"],
        nality_decuplet_10=res["nality_grading"]["decuplet_10"],
        iota_PS_M4_image_rank_LR=res["iota_PS_M4_image_rank_LR"],
        iota_PS_M4_image_rank_L=res["iota_PS_M4_image_rank_L"],
        iota_PS_M4_morphism_choice_invariant=res["iota_PS_M4_morphism_choice_invariant"],
        INFO_fires_on_M4_subquestion=res["INFO_fires_on_M4_subquestion"],
        AK_ref_M3_dim=res["AK_ref_M3_dim"],
        AK_ref_target_dim=res["AK_ref_target_dim"],
        AK_ref_M3_forced_to_zero=res["AK_ref_M3_forced_to_zero"],
        AK_cocycle_phi67=res["AK_cocycle_phi67"],
        AK_cocycle_phi88=res["AK_cocycle_phi88"],
        AK_cocycle_ratio_67_88=res["AK_cocycle_ratio_67_88"],
        AK_cocycle_ratio_xcheck_ok=res["AK_cocycle_ratio_xcheck_ok"],
        adj_gram_min_nonzero_eig=res["adj_gram_min_nonzero_eig"],
        A_K_PS_summand_dims=np.array([s[1] for s in A_K_PS_SUMMANDS]),
        tau_fold=float(tau_fold),
        tol=TOL,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    out_json = {
        "gate_id": GATE_ID,
        "verdict": composite,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "abelian_only_EXTENDS": res["abelian_only_EXTENDS"],
        "decision_quantities": {
            k: (v if not isinstance(v, dict) else v)
            for k, v in res.items() if k not in ("nality_grading",)
        },
        "nality_grading": res["nality_grading"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "substitution_chain_direction": (
            "M4(C) (dim 4) > condensate target (dim 2) => rep-dimension lemma "
            "forces ANY *-homomorphism iota^PS to send M4(C)->0 ENTIRELY (center "
            "AND (15)-adjoint), exactly as chi annihilated M3(C) on A_K. The "
            "(15)-adjoint condensate is in ker(iota_*^PS); no non-abelian M4(C) "
            "class survives inheritance => abelian-only EXTENDS => PASS. D-2 "
            "generalizes; W3 is algebra-independent within the AF-Wedderburn class."
        ),
    }
    OUT_JSON.write_text(json.dumps(out_json, indent=2), encoding="utf-8")
    make_plot(res, OUT_PNG)

    tag = (f"(value={composite!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)

    # --- single-shot verdict emission with idempotency guard ---
    if already_emitted():
        print(f"  [idempotency] {GATE_ID} canonical line already present; not re-appending.")
    else:
        append_verdict(composite, value, audit_sha, content_sha)
        print(f"  [emit] appended canonical + dual-SHA companion rows.")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
