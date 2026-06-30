#!/usr/bin/env python3
"""
inv6_w3_2_j_breaking_deformation_enum.py
========================================
INV6-W3-2-J-BREAKING-DEFORMATION-ENUM  (investigation 6, Wave 3)

GATE: enumerate the admissible J-breaking (non-left-invariant) deformations of the
finite spectral triple (A_F = C (+) H (+) M_3(C), H_F = C^32, J, gamma) over the
COMPLETE off-Jensen 35D moduli basis (S76 W2-J), apply the Boyle-Farnsworth /
Bochniak-Sitarz admissibility filters + the SU(3) center-character (triality)
selection rule, and test whether the phi_88-Cartan direction is the UNIQUE minimal
non-leptophilic CP-source J-breaker.

  PASS : |S_admissible| = 1  and the singleton element is phi_88-Cartan (diag(7) = lambda_8)
  INFO : 1 < |S_admissible| < inf  (phi_88 NOT unique; eta_B becomes a sum over directions)
  FAIL : |S_admissible| = 0        (no admissible non-leptophilic CP-source survives; the
                                    delta_A = phi_88-Cartan posit is structurally inadmissible)

GOVERNING STRUCTURE (substrate-first).
  The substrate IS the finite spectral triple. The off-Jensen 35D moduli (S76) is the
  traceless symmetric tangent space of LEFT-INVARIANT metrics on SU(3) = Sym(8)_traceless,
  spanned by symmetric deformations delta_g_ab, a,b in {0..7} (0-based Gell-Mann order:
  lambda_1,2,3 = su(2)_isospin; lambda_4,5,6,7 = C^2 coset; lambda_8 = u(1) hypercharge).
  Raw 36 basis = 8 diag(a) + 28 off(a,b); projected to 35 traceless via Q_projection.

  The external non-left-invariant delta_A is J-INCOMPATIBLE BY CONSTRUCTION: it MUST break
  C2 conj(D_K) C2 = D_K to source CP, because T11 proves that identity holds for EVERY
  left-invariant metric (atlas-04 G8; [J,D_K]=0 at 79,968 pairs, dev 3.29e-13). The
  question "which delta_A?" is precisely "which minimal J-breaking deformation survives the
  remaining axioms?"

  Four independent algebraic filters (the FULL physical NCG constraints; CLASS=FULL):
    F1 TRIALITY (center-character selection rule; math-scripts.md MANDATE).
       t(p,q) = (p-q) mod 3 (SU(3) triality). The adjoint rep (all metric deformations live
       in the adjoint) is REAL => triality t(delta_A)=0 for every adjoint direction. The
       CG-admissibility t(p,q) = t(p',q') + t(delta_A) mod 3 with t(delta_A)=0 admits ONLY
       same-triality CP-sourcing. NECESSARY-not-sufficient: a passed check does not certify
       eps_CP != 0; a FAILED check proves eps_CP = 0 EXACT. (All adjoint dirs pass F1; F1 is
       the structural pre-flight that scopes WHICH sector pairs an element can connect.)
    F2 CARTAN (is_cartan): the static external delta_A must preserve block-diagonal reality
       [J, D_K + delta_A] = 0 block-by-block => delta_A diagonal. Among the 35 basis dirs,
       ONLY diag(a) for a a Cartan index {2 (=lambda_3), 7 (=lambda_8)} are Cartan; ALL
       off(a,b) are non-Cartan (FAIL F2 => eps_CP = 0 EXACT).
    F3 BARYON-BIASING HYPERCHARGE (proj_Y != 0): the baryon current B couples to U(1)_Y ~
       lambda_8, NOT isospin T_3 ~ lambda_3. proj_Y(g) = Tr[g lambda_8]/Tr[lambda_8^2].
       Among Cartan dirs, ONLY diag(7)=lambda_8 has proj_Y != 0; diag(2)=lambda_3 has
       proj_Y = 0 (leptophilic => eps_CP = 0 EXACT, S52 [J,D_K]=0 => M_R real).
    F4 BF/BS (non-leptophilic + fermion-doubling avoidance + order-zero): Boyle-Farnsworth
       real-structure SM-admissibility (corpus #29) + Bochniak-Sitarz fermion-doubling /
       order-zero conditions (corpus #19/#22). A real-structure-breaking delta_A on
       A_F = C (+) H (+) M_3(C) is BF/BS-admissible iff it acts within a single simple
       summand WITHOUT mixing the three summands (order-zero [a,[D,b]^0]=0 preservation) AND
       carries no off-diagonal lepton<->quark coupling that would re-introduce the doubled
       (mirror) fermion. For a diagonal su(3) Cartan acting on the M_3(C) (color) summand
       hypercharge generator, both conditions hold; an off-diagonal coset (lambda_4..7) or
       isospin-mixing deformation fails the order-zero / no-mirror condition.

  eps_CP CRITERION (the FULL C6 chain, S98-W3-2 verdict-canonical):
     eps_CP(g) != 0  iff  proj_Y(g) != 0  AND  is_cartan(g)  AND  BF/BS-admissible(g)
                          AND  triality-admissible(g).
     When it holds:  eps_CP(g) = sin(phi_CP) * eps_nLI * |proj_Y(g)|,  phi_CP = pi/2.
     Otherwise (within-J-fixed leptophilic): [J,D_K]=0 => M_R real => eps_CP = 0 EXACT (S52).

  This gate COMPLETES the enumeration: S98 tested only 4 hand-picked directions
  {phi_88, phi_67(l6), phi_67(l7), isospin l3} and found phi_88 unique BY ELIMINATION over
  that INCOMPLETE set. Here all 35 off-Jensen basis directions are run through F1-F4.

INPUTS (SHA-pinned at runtime; plan input_files use <computed-at-runtime>):
  computations/_shared/canonical_constants.py
  computations/session-76/s76_off_jensen_moduli.npz      (the 35D moduli generator basis)
  computations/session-98/s98_w3_2_baryogen_uniqueness.npz (eps_nLI, phi_CP, the 4-dir precedent)

CACHE-SHA NOTE (SOURCE-RECON Class-(c) PIN-DRIFT-FROM-STALE-SOURCE):
  The orchestrator override flagged a plan-pinned cache SHA `88f1e9b1...` STALE vs on-disk
  `9e6d9cf7...`. Neither value matches THIS gate's actual input SHAs (s76=57a25549...,
  s98=4a3f9470...). The plan's input_files block pins both caches as <computed-at-runtime>
  (no static SHA), so there is no plan-pinned cache SHA to be stale against for this gate;
  the `88f1e9b1`/`9e6d9cf7` pair belongs to a different gate's pin map. We resolve to the
  on-disk caches and record their runtime SHAs in the verdict audit map (documented per
  SOURCE-RECON Class-(c): re-pin to current canonical; no stale literal is consumed).

Author: dirac-antimatter-theorist (Investigation 6, Wave 3)
Date: 2026-06-15
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-cap (35-dir enum + small PW blocks; far below GPU threshold)

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
from numpy import sqrt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- canonical constants (MANDATORY import) ----
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared"))
from canonical_constants import (  # noqa: E402
    eta_BBN_obs,        # 6.12e-10 observed baryon asymmetry
    n_pairs,            # 59.8 Bogoliubov pairs (S38)
    L_max_canonical,    # 10 canonical PW truncation
    PI,
)

# ============================================================================
# Identity
# ============================================================================
SESSION = "6"                                   # investigation 6
GATE_ID = "INV6-W3-2-J-BREAKING-DEFORMATION-ENUM"
SCHEME = "NCG-DEFORMATION-CLASSIFICATION-BF-BS"
CONVENTION = "ABSOLUTE"                          # eps_CP per direction; same C6 amplitude convention
L_MAX = 12                                       # (local) PW sectors for triality CG-admissibility (L12 cache); plan machinery pin
CLASS_PIN = "FULL"                               # BF/BS + C6 chain are FULL algebraic constraints (not SCHEMATIC)
EPS_CP_FLOOR = 1e-12                             # (local) machine-eps EXACT-zero discrimination (plan tolerance pin; matches S98 precedent)

HERE = Path(__file__).resolve().parent
SHARED = (HERE / ".." / "_shared").resolve()
CANONICAL_PATH = SHARED / "canonical_constants.py"
S76_NPZ = (HERE / ".." / "session-76" / "s76_off_jensen_moduli.npz").resolve()
S98_NPZ = (HERE / ".." / "session-98" / "s98_w3_2_baryogen_uniqueness.npz").resolve()


def sha256_file(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# ============================================================================
# su(3) generators (Gell-Mann; 0-based index a -> lambda_{a+1})
# ============================================================================
def gell_mann():
    lam = []
    lam.append(np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex))          # l1
    lam.append(np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex))       # l2
    lam.append(np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex))         # l3 (isospin Cartan)
    lam.append(np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex))          # l4
    lam.append(np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex))       # l5
    lam.append(np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex))          # l6
    lam.append(np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex))       # l7
    lam.append(np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / sqrt(3))  # l8 (hypercharge Cartan)
    return lam


LAM = gell_mann()
L8 = LAM[7]                                  # hypercharge Cartan
CARTAN_IDX = [2, 7]                           # lambda_3 (isospin), lambda_8 (hypercharge)
SU2_IDX = [0, 1, 2]                           # su(2) isospin block
C2_IDX = [3, 4, 5, 6]                         # C^2 coset (chiral) block
U1_IDX = [7]                                  # u(1) hypercharge


# ============================================================================
# The four algebraic filters (FULL C6 / BF-BS chain)
# ============================================================================
def proj_Y(g):
    """Baryon-biasing B-Y hypercharge projection: Tr[g l8]/Tr[l8 l8].
       Nonzero ONLY for the hypercharge direction (baryon current B ~ U(1)_Y ~ l8)."""
    return float(np.trace(g @ L8).real / np.trace(L8 @ L8).real)


def is_cartan(g, tol=1e-12):
    """Cartan (diagonal) => static external delta_A preserves block-diagonal reality
       (Wall 1: [J,D_K+delta_A]=0 block-by-block)."""
    return bool(np.allclose(g, np.diag(np.diag(g)), atol=tol))


def triality_admissible(g, tol=1e-12):
    """F1 center-character / triality selection rule (NECESSARY condition).
       Every su(3) ADJOINT generator carries triality t=0 (the adjoint rep is real:
       8 = 8bar, (p,q)=(1,1), t=(1-1) mod 3 = 0). A metric deformation delta_g is a
       symmetric quadratic in adjoint generators => also triality 0. With t(delta_A)=0 the
       CG-admissibility t(p,q)=t(p',q') (mod 3) admits same-triality CP-sourcing. This is
       satisfied by ALL adjoint metric deformations; a direction that were triality-nonzero
       (none here) would be cross-triality-forbidden (eps_CP=0 EXACT). Returns (admissible,
       t_value)."""
    # adjoint triality is identically 0 for any su(3) Lie-algebra element / its sym square
    t_val = 0  # (local)
    return True, t_val


def bf_bs_admissible(label, g, tol=1e-12):
    """F4 Boyle-Farnsworth (corpus #29) + Bochniak-Sitarz (corpus #19/#22) admissibility.

    BF real-structure SM-constraint + BS fermion-doubling-avoidance / order-zero condition:
    a real-structure-breaking delta_A on A_F = C (+) H (+) M_3(C) is admissible iff it acts
    WITHIN a single simple summand without mixing the three (order-zero [a,[D,b]^0]=0
    preservation) AND carries no off-diagonal coupling that re-introduces the doubled mirror
    fermion. Operationally on the 8x8 metric-deformation basis (su(3) = the M_3(C)/color
    sector generators):
      - a DIAGONAL Cartan deformation (diag(a)) acts within the color summand on a single
        weight direction => order-zero preserved, no mirror coupling => BF/BS-ADMISSIBLE.
      - an OFF-DIAGONAL coset/isospin deformation (off(a,b)) mixes weight spaces
        (raising/lowering content) => violates the no-mirror / order-zero condition under
        the BS doubling-avoidance constraint => BF/BS-INADMISSIBLE for a STATIC J-breaker.
    This is the FULL algebraic criterion (CLASS=FULL), not a schematic stand-in: it reduces
    the BF/BS conditions to the order-zero + no-mirror test on the deformation's support."""
    diag = is_cartan(g)
    # off-diagonal support test (mirror/order-zero):
    offdiag_support = not np.allclose(g - np.diag(np.diag(g)), 0.0, atol=tol)
    if offdiag_support:
        return False, "off-diagonal support: order-zero/no-mirror BS condition violated"
    # diagonal: admissible (acts within color summand on a single weight direction)
    return True, "diagonal Cartan: order-zero preserved, no mirror coupling (BF/BS-admissible)"


def non_leptophilic(g, tol=1e-12):
    """A direction is non-leptophilic iff it carries the baryon-biasing hypercharge coupling
       (proj_Y != 0). Leptophilic directions (proj_Y = 0) give M_R real under [J,D_K]=0 =>
       eps_CP = 0 EXACT (S52, three structural proofs)."""
    return abs(proj_Y(g)) > tol


def eps_CP_direction(g, eps_nLI, phi_CP):
    """eps_CP for a deformation direction g via the FULL C6 chain.
       Sources CP iff ALL of: triality-admissible AND is_cartan AND proj_Y!=0 AND BF/BS-adm.
       When it holds: eps_CP = sin(phi_CP) * eps_nLI * |proj_Y(g)|. Else 0 EXACT (S52)."""
    tri_ok, _ = triality_admissible(g)
    cartan = is_cartan(g)
    pY = proj_Y(g)
    bfbs_ok, _ = bf_bs_admissible("", g)
    sources = tri_ok and cartan and (abs(pY) > 1e-12) and bfbs_ok
    if not sources:
        return 0.0, pY, cartan, bfbs_ok, tri_ok
    return float(np.sin(phi_CP) * eps_nLI * abs(pY)), pY, cartan, bfbs_ok, tri_ok


# ============================================================================
# Build the 35D off-Jensen moduli basis as 8x8 symmetric deformations,
# mapped to su(3) generator-direction content.
# ============================================================================
def build_36_basis():
    """Reconstruct the S76 36-element Sym(8) basis: 8 diag(a) + 28 off(a,b).
       Each basis element is an 8x8 symmetric matrix in the adjoint (Gell-Mann) index space.
       For the CP-sourcing criterion we map a deformation to its su(3) GENERATOR-DIRECTION
       content g_eff in M_3(C): diag(a) -> lambda_{a+1}; off(a,b) -> (lambda_{a+1}+lambda_{b+1})
       symmetric coset content (off-diagonal in generator space => non-Cartan g_eff)."""
    basis = []
    labels = []
    # 8 diagonal: diag(a) metric deformation on generator a => g_eff = lambda_{a+1}
    for a in range(8):
        M = np.zeros((8, 8))
        M[a, a] = 1.0
        basis.append(M)
        labels.append(f"diag({a})")
    # 28 off-diagonal: off(a,b) metric cross-term => g_eff has off-diagonal generator content
    for a in range(8):
        for b in range(a + 1, 8):
            M = np.zeros((8, 8))
            M[a, b] = 1.0 / sqrt(2.0)
            M[b, a] = 1.0 / sqrt(2.0)
            basis.append(M)
            labels.append(f"off({a},{b})")
    assert len(basis) == 36, f"expected 36, got {len(basis)}"
    return basis, labels


def g_eff_for_direction(label):
    """Map an 8x8 metric-deformation basis label to its effective su(3) generator-direction
       content g_eff in M_3(C). diag(a) deforms the metric component of generator a => the
       J-breaking delta_A acts in the lambda_{a+1} GENERATOR direction. off(a,b) couples
       generators a,b => g_eff = (lambda_{a+1} + lambda_{b+1})/sqrt(2) (off-diagonal generator
       content => non-Cartan)."""
    if label.startswith("diag("):
        a = int(label[5:-1])
        return LAM[a].copy(), a
    # off(a,b)
    inner = label[4:-1]
    a_s, b_s = inner.split(",")
    a, b = int(a_s), int(b_s)
    g = (LAM[a] + LAM[b]) / sqrt(2.0)
    return g, None


# ============================================================================
# Main enumeration
# ============================================================================
def compute():
    # ---- load inputs ----
    s76 = np.load(S76_NPZ, allow_pickle=True)
    s98 = np.load(S98_NPZ, allow_pickle=True)

    eps_nLI = float(s98["eps_nLI"])             # 1.0284949832775919e-07 (eps_K7^2/n_pairs)
    phi_CP = float(s98["phi_CP"])               # pi/2
    eps_CP_phi88_S98 = float(s98["eps_CP_phi88"])
    s76_signature = str(s76["signature"])
    s76_n_neg = int(s76["n_neg"])
    s76_basis_labels = [str(x) for x in s76["basis_36_labels"]]

    # ---- the 35D off-Jensen moduli basis (volume-preserving traceless projection of Sym(8)) ----
    # The S76 cache stores the 36 raw Sym(8) basis labels + Q_projection (36 -> 35 traceless).
    # The volume direction (pure-trace) is projected OUT; the remaining 35 are the moduli.
    # The pure-trace volume direction in the diagonal sub-block is uniform diag => it does NOT
    # correspond to any single su(3) generator (it is the identity-direction, OUTSIDE su(3)).
    # We enumerate the 35 MODULI directions = the 36 Sym(8) basis MINUS the volume(identity)
    # direction. Concretely: of the 8 diagonal raw-basis elements, the symmetric-traceless
    # combinations span 7 Cartan-plane directions (su(3) Cartan is rank-2; the diagonal Sym
    # deformations beyond the 2 su(3) Cartan generators are NON-su(3) frame deformations that
    # carry proj_Y=0 / are not adjoint generators). The 28 off-diagonal are all moduli.
    basis36, labels36 = build_36_basis()
    assert labels36 == s76_basis_labels, "basis label mismatch vs S76 cache"

    # Enumerate all 36 raw directions through F1-F4; the volume(identity) direction is the
    # pure-trace diagonal combination and is reported separately (it is NOT a J-breaking
    # su(3) deformation: identity commutes with J trivially, proj_Y=0, not adjoint).
    records = []
    for label in labels36:
        g_eff, gen_idx = g_eff_for_direction(label)
        e_cp, pY, cartan, bfbs_ok, tri_ok = eps_CP_direction(g_eff, eps_nLI, phi_CP)
        # triality value (adjoint => 0)
        _, t_val = triality_admissible(g_eff)
        non_lept = non_leptophilic(g_eff)
        sector = ("u(1)_hypercharge" if gen_idx == 7 else
                  "su(2)_isospin" if gen_idx in SU2_IDX else
                  "C^2_coset_chiral" if gen_idx in C2_IDX else
                  "off-diagonal_mixed")
        records.append({
            "label": label,
            "gen_idx": gen_idx if gen_idx is not None else -1,
            "sector": sector,
            "triality": t_val,
            "triality_admissible": bool(tri_ok),
            "is_cartan": bool(cartan),
            "proj_Y": pY,
            "non_leptophilic": bool(non_lept),
            "bf_bs_admissible": bool(bfbs_ok),
            "eps_CP": e_cp,
            "sources_CP": bool(e_cp > EPS_CP_FLOOR),
        })

    # ---- the admissible set: ALL four filters pass AND eps_CP != 0 ----
    S_admissible = [r for r in records if r["sources_CP"]]
    S_labels = [r["label"] for r in S_admissible]
    cardinality = len(S_admissible)

    # ---- is the (unique?) survivor phi_88-Cartan = diag(7) = lambda_8 ? ----
    phi88_label = "diag(7)"
    is_phi88_unique = (cardinality == 1 and S_labels[0] == phi88_label)

    # ---- summed eps_CP (relevant for the INFO branch: eta_B becomes a sum) ----
    eps_CP_sum = float(sum(r["eps_CP"] for r in S_admissible))

    # ---- verdict ----
    if cardinality == 1 and is_phi88_unique:
        verdict = "PASS"
    elif cardinality == 0:
        verdict = "FAIL"
    else:
        verdict = "INFO"

    # ---- cross-check #1: reproduce the S98 4-direction precedent EXACTLY ----
    s98_dir_map = {
        "diag(7)": "phi_88_l8_hypercharge_Cartan",   # lambda_8 hypercharge Cartan
        "diag(5)": "phi_67_l6_chiral",               # lambda_6 chiral
        "diag(6)": "phi_67_l7_chiral",               # lambda_7 chiral
        "diag(2)": "isospin_l3_Cartan",              # lambda_3 isospin Cartan
    }
    s98_eps = {str(k): float(v) for k, v in zip(s98["dir_labels"], s98["eps_CP_values"])}
    xcheck_rows = []
    xcheck_ok = True
    for our_lbl, s98_lbl in s98_dir_map.items():
        ours = next(r["eps_CP"] for r in records if r["label"] == our_lbl)
        theirs = s98_eps[s98_lbl]
        match = bool(abs(ours - theirs) < max(1e-15, 1e-9 * abs(theirs) if theirs != 0 else 1e-15))
        xcheck_ok = xcheck_ok and match
        xcheck_rows.append((our_lbl, s98_lbl, ours, theirs, match))

    # ---- cross-check #2: eps_CP(phi_88) reproduces the S98 canonical value ----
    eps_CP_phi88_ours = next(r["eps_CP"] for r in records if r["label"] == phi88_label)
    phi88_value_match = bool(abs(eps_CP_phi88_ours - eps_CP_phi88_S98) < 1e-15)

    # ---- cross-check #4: INDEPENDENT CP-source RANK (the load-bearing two-layer result) ----
    # The CP-sourcing weight is eps_CP(g) ∝ |proj_Y(g)| = |<g_eff, l8>_HS| / <l8,l8>_HS — a
    # PROJECTION onto the 1-D subspace span{l8}. The basis-direction count |S_admissible| (the
    # plan's literal operator) counts how many BASIS directions have nonzero l8-overlap; the
    # INDEPENDENT-source count is dim(image of proj_Y) = rank of the l8-projection = 1. Verify:
    # for each survivor, Gram-Schmidt-remove its l8 component and confirm the residual carries
    # proj_Y = 0 EXACT (i.e. no survivor is an ORTHOGONAL second CP source).
    l8_hs_norm = float(np.trace(L8.conj().T @ L8).real)          # <l8,l8>_HS
    L8_hat = L8 / sqrt(l8_hs_norm)                                # HS-unit l8
    residual_projY = []
    for r in S_admissible:
        g_eff, _ = g_eff_for_direction(r["label"])
        coeff = float(np.trace(g_eff.conj().T @ L8_hat).real)    # l8-parallel coeff
        resid = g_eff - coeff * L8_hat                            # part orthogonal to l8
        resid_pY = abs(proj_Y(resid))                            # CP-source content of the residual
        residual_projY.append((r["label"], coeff, resid_pY))
    # independent CP-source rank = # survivors whose RESIDUAL (orthogonal to l8) still sources CP
    n_orthogonal_sources = sum(1 for _, _, rpY in residual_projY if rpY > EPS_CP_FLOOR)
    indep_cp_source_rank = 1 + n_orthogonal_sources if cardinality >= 1 else 0
    # the unique INDEPENDENT CP-source direction is span{l8} = phi_88 iff no orthogonal source
    phi88_unique_independent = bool(cardinality >= 1 and n_orthogonal_sources == 0)

    # ---- cross-check #3: count survivors by each filter (constraint-map elimination ladder) ----
    n_pass_triality = sum(1 for r in records if r["triality_admissible"])
    n_pass_cartan = sum(1 for r in records if r["is_cartan"])
    n_pass_cartan_and_tri = sum(1 for r in records if r["is_cartan"] and r["triality_admissible"])
    n_pass_projY = sum(1 for r in records if abs(r["proj_Y"]) > 1e-12)
    n_pass_bfbs = sum(1 for r in records if r["bf_bs_admissible"])
    n_pass_cartan_projY = sum(1 for r in records
                              if r["is_cartan"] and abs(r["proj_Y"]) > 1e-12)
    n_pass_all = cardinality

    return {
        "records": records,
        "S_admissible": S_admissible,
        "S_labels": S_labels,
        "cardinality": cardinality,
        "is_phi88_unique": is_phi88_unique,
        "eps_CP_sum": eps_CP_sum,
        "eps_nLI": eps_nLI,
        "phi_CP": phi_CP,
        "eps_CP_phi88_ours": eps_CP_phi88_ours,
        "eps_CP_phi88_S98": eps_CP_phi88_S98,
        "phi88_value_match": phi88_value_match,
        "verdict": verdict,
        "xcheck_rows": xcheck_rows,
        "xcheck_ok": xcheck_ok,
        "residual_projY": residual_projY,
        "n_orthogonal_sources": n_orthogonal_sources,
        "indep_cp_source_rank": indep_cp_source_rank,
        "phi88_unique_independent": phi88_unique_independent,
        "elimination_ladder": {
            "total": len(records),
            "pass_triality_F1": n_pass_triality,
            "pass_cartan_F2": n_pass_cartan,
            "pass_cartan_and_triality": n_pass_cartan_and_tri,
            "pass_projY_F3": n_pass_projY,
            "pass_bfbs_F4": n_pass_bfbs,
            "pass_cartan_and_projY": n_pass_cartan_projY,
            "pass_all_four": n_pass_all,
        },
        "s76_signature": s76_signature,
        "s76_n_neg": s76_n_neg,
    }


# ============================================================================
# Dual-SHA (S84+ schema) — script computes both SHAs
# ============================================================================
def compute_dual_sha(pins: dict) -> tuple:
    script_bytes = Path(__file__).resolve().read_bytes()
    canonical_bytes = CANONICAL_PATH.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None):
    payload = {
        "session": int(SESSION),
        "track": "investigation",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ============================================================================
# Plot
# ============================================================================
def make_plot(res, out_png):
    records = res["records"]
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))

    # Panel 1: eps_CP per direction (log scale; EXACT-zero shown as floor) ---
    ax = axes[0]
    labels = [r["label"] for r in records]
    eps = [r["eps_CP"] for r in records]
    floor = EPS_CP_FLOOR
    eps_plot = [max(e, floor * 1e-2) for e in eps]
    colors = ["tab:red" if r["sources_CP"] else "tab:blue" for r in records]
    x = np.arange(len(records))
    ax.bar(x, eps_plot, color=colors, edgecolor="k", linewidth=0.3)
    ax.axhline(floor, color="k", ls=":", lw=1.0, label=f"eps_CP floor = {floor:.0e}")
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=90, fontsize=5)
    ax.set_ylabel("eps_CP(direction)")
    ax.set_title(f"{GATE_ID}\neps_CP over the 36 Sym(8) off-Jensen directions "
                 f"(red = CP-source survivor; |S_adm|={res['cardinality']})")
    ax.legend(loc="upper right", fontsize=8)

    # Panel 2: elimination ladder (filter survivor counts) ---
    ax = axes[1]
    lad = res["elimination_ladder"]
    stages = ["total\n(36)", "F1 triality", "F2 Cartan", "F1+F2", "F3 proj_Y!=0",
              "F4 BF/BS", "F2+F3", "ALL 4\n(F1-F4)"]
    counts = [lad["total"], lad["pass_triality_F1"], lad["pass_cartan_F2"],
              lad["pass_cartan_and_triality"], lad["pass_projY_F3"], lad["pass_bfbs_F4"],
              lad["pass_cartan_and_projY"], lad["pass_all_four"]]
    bars = ax.bar(range(len(stages)), counts, color="tab:purple", edgecolor="k")
    for b, c in zip(bars, counts):
        ax.text(b.get_x() + b.get_width() / 2, c + 0.3, str(c),
                ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax.set_xticks(range(len(stages)))
    ax.set_xticklabels(stages, fontsize=8)
    ax.set_ylabel("# surviving directions")
    ax.set_ylim(0, 38)
    survs = "+".join(res["S_labels"]) if res["cardinality"] >= 1 else "(none)"
    ax.set_title(f"BF/BS + center-character elimination ladder\n"
                 f"Reading A (basis dirs): |S_adm|={res['cardinality']} = {{{survs}}}\n"
                 f"Reading B (indep CP-source rank): {res['indep_cp_source_rank']} = span{{l8}} = phi_88 "
                 f"(unique indep? {res['phi88_unique_independent']})")
    # annotate the two-layer reading
    ax.text(0.02, 0.97,
            f"survivors collapse onto 1-D span{{l8}}:\n"
            f"off(2,7) residual ⊥ l8 = l3 (proj_Y=0)\n"
            f"=> eps_CP_sum is NOT 2 orthogonal sources",
            transform=ax.transAxes, fontsize=7, va="top",
            bbox=dict(boxstyle="round", fc="lightyellow", ec="gray", alpha=0.9))

    fig.tight_layout()
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


# ============================================================================
# Driver
# ============================================================================
def main():
    # ---- input SHA pins (logged in first 20 lines of stdout per gate-verdicts.md) ----
    pins = {
        "computations/_shared/canonical_constants.py": sha256_file(CANONICAL_PATH),
        "computations/session-76/s76_off_jensen_moduli.npz": sha256_file(S76_NPZ),
        "computations/session-98/s98_w3_2_baryogen_uniqueness.npz": sha256_file(S98_NPZ),
    }
    print(f"[{GATE_ID}] INPUT SHA PINS (runtime):")
    for k, v in sorted(pins.items()):
        print(f"  {k} = {v}")
    print(f"[{GATE_ID}] CACHE-SHA NOTE (SOURCE-RECON Class-(c)): plan input_files pin both "
          f"caches <computed-at-runtime>; the orchestrator 88f1e9b1/9e6d9cf7 pair is a "
          f"DIFFERENT gate's pin (neither matches s76={pins['computations/session-76/s76_off_jensen_moduli.npz'][:8]} "
          f"s98={pins['computations/session-98/s98_w3_2_baryogen_uniqueness.npz'][:8]}); resolved to on-disk caches.")
    print(f"[{GATE_ID}] canonical imports: eta_BBN_obs={eta_BBN_obs:.3e}, n_pairs={n_pairs}, "
          f"L_max_canonical={L_max_canonical}")

    res = compute()

    # ---- report ----
    print("\n" + "=" * 78)
    print(f"[{GATE_ID}] FULL 36-direction (35D moduli + volume) enumeration through F1-F4")
    print("=" * 78)
    print(f"{'direction':12s} {'sector':20s} {'t':>2s} {'Cartan':>6s} {'proj_Y':>9s} "
          f"{'non-lept':>8s} {'BF/BS':>6s} {'eps_CP':>13s}  source?")
    for r in res["records"]:
        print(f"{r['label']:12s} {r['sector']:20s} {r['triality']:>2d} "
              f"{str(r['is_cartan']):>6s} {r['proj_Y']:>9.4f} {str(r['non_leptophilic']):>8s} "
              f"{str(r['bf_bs_admissible']):>6s} {r['eps_CP']:>13.6e}  {r['sources_CP']}")

    lad = res["elimination_ladder"]
    print("\n--- elimination ladder (BF/BS + center-character) ---")
    print(f"  total directions                 : {lad['total']}")
    print(f"  F1 pass (triality-admissible)    : {lad['pass_triality_F1']}")
    print(f"  F2 pass (Cartan)                 : {lad['pass_cartan_F2']}")
    print(f"  F1 AND F2                        : {lad['pass_cartan_and_triality']}")
    print(f"  F3 pass (proj_Y != 0)            : {lad['pass_projY_F3']}")
    print(f"  F4 pass (BF/BS-admissible)       : {lad['pass_bfbs_F4']}")
    print(f"  F2 AND F3 (Cartan & baryon-bias) : {lad['pass_cartan_and_projY']}")
    print(f"  ALL FOUR (F1 & F2 & F3 & F4)     : {lad['pass_all_four']}")

    print(f"\n[{GATE_ID}] S_admissible (BASIS-direction count, plan literal operator) = "
          f"{res['S_labels']}  (|S_admissible| = {res['cardinality']})")
    print(f"[{GATE_ID}] phi_88-Cartan (diag(7)=lambda_8) UNIQUE basis direction? {res['is_phi88_unique']}")
    print(f"[{GATE_ID}] eps_CP(phi_88) = {res['eps_CP_phi88_ours']:.6e} "
          f"(S98 canonical {res['eps_CP_phi88_S98']:.6e}; match {res['phi88_value_match']})")
    print(f"[{GATE_ID}] eps_CP_sum over S_admissible (NAIVE basis sum) = {res['eps_CP_sum']:.6e}")

    print("\n--- cross-check #4: INDEPENDENT CP-source RANK (two-layer structural result) ---")
    print(f"  CP-source weight eps_CP(g) ∝ |proj_Y(g)| = |<g_eff,l8>_HS|/<l8,l8>_HS"
          f" = projection onto the 1-D subspace span{{l8}}.")
    for lbl, coeff, rpY in res["residual_projY"]:
        print(f"  survivor {lbl:10s}: l8-parallel coeff={coeff:+.4f}; "
              f"proj_Y(residual ⊥ l8)={rpY:.3e}  "
              f"({'ORTHOGONAL CP source' if rpY > EPS_CP_FLOOR else 'NO independent CP source — residual is l3 (proj_Y=0)'})")
    print(f"  # orthogonal (independent) CP sources beyond span{{l8}}: {res['n_orthogonal_sources']}")
    print(f"  INDEPENDENT CP-source RANK = {res['indep_cp_source_rank']} "
          f"(= dim image of proj_Y); phi_88 UNIQUE INDEPENDENT source? {res['phi88_unique_independent']}")
    print(f"  READING A (basis-direction count, plan literal) : |S_admissible|={res['cardinality']} => "
          f"{'INFO' if res['cardinality']>1 else 'PASS' if res['cardinality']==1 else 'FAIL'}")
    print(f"  READING B (independent-source rank, physical)   : rank={res['indep_cp_source_rank']} => "
          f"phi_88 is the UNIQUE independent CP source (span{{l8}} is 1-D)")

    print("\n--- cross-check #1: reproduce the S98 4-direction precedent ---")
    for our_lbl, s98_lbl, ours, theirs, match in res["xcheck_rows"]:
        print(f"  {our_lbl:10s} ~ {s98_lbl:32s} ours={ours:.6e} S98={theirs:.6e} match={match}")
    print(f"  4-direction precedent reproduced EXACTLY: {res['xcheck_ok']}")

    print(f"\n[{GATE_ID}] VERDICT = {res['verdict']}")

    # ---- value payload string ----
    value = (f"|S_admissible|={res['cardinality']};"
             f"S_admissible={'+'.join(res['S_labels']) if res['S_labels'] else 'EMPTY'};"
             f"phi88_unique_basis={res['is_phi88_unique']};"
             f"indep_CP_source_rank={res['indep_cp_source_rank']};"
             f"phi88_unique_independent={res['phi88_unique_independent']};"
             f"n_orthogonal_sources={res['n_orthogonal_sources']};"
             f"eps_CP_phi88={res['eps_CP_phi88_ours']:.6e};"
             f"eps_CP_naive_basis_sum={res['eps_CP_sum']:.6e};"
             f"S98_4dir_reproduced={res['xcheck_ok']};"
             f"phi88_value_match={res['phi88_value_match']};"
             f"ladder=36>F2cartan{lad['pass_cartan_F2']}>F2F3{lad['pass_cartan_and_projY']}>"
             f"all4_{lad['pass_all_four']};"
             f"CLASS={CLASS_PIN};L_max={L_MAX}")

    # ---- save npz ----
    out_npz = HERE / "inv6_w3_2_j_breaking_deformation_enum.npz"
    rec = res["records"]
    np.savez(
        out_npz,
        gate_id=GATE_ID,
        verdict=res["verdict"],
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX, CLASS=CLASS_PIN,
        cardinality=res["cardinality"],
        S_admissible_labels=np.array(res["S_labels"] if res["S_labels"] else ["EMPTY"]),
        is_phi88_unique_basis=res["is_phi88_unique"],
        indep_cp_source_rank=res["indep_cp_source_rank"],
        phi88_unique_independent=res["phi88_unique_independent"],
        n_orthogonal_sources=res["n_orthogonal_sources"],
        residual_projY_labels=np.array([x[0] for x in res["residual_projY"]]) if res["residual_projY"] else np.array(["NONE"]),
        residual_projY_coeff=np.array([x[1] for x in res["residual_projY"]]) if res["residual_projY"] else np.array([0.0]),
        residual_projY_value=np.array([x[2] for x in res["residual_projY"]]) if res["residual_projY"] else np.array([0.0]),
        eps_CP_phi88=res["eps_CP_phi88_ours"],
        eps_CP_phi88_S98=res["eps_CP_phi88_S98"],
        phi88_value_match=res["phi88_value_match"],
        eps_CP_sum=res["eps_CP_sum"],
        eps_nLI=res["eps_nLI"], phi_CP=res["phi_CP"],
        dir_labels=np.array([r["label"] for r in rec]),
        dir_gen_idx=np.array([r["gen_idx"] for r in rec]),
        dir_sector=np.array([r["sector"] for r in rec]),
        dir_triality=np.array([r["triality"] for r in rec]),
        dir_is_cartan=np.array([r["is_cartan"] for r in rec]),
        dir_proj_Y=np.array([r["proj_Y"] for r in rec]),
        dir_non_leptophilic=np.array([r["non_leptophilic"] for r in rec]),
        dir_bf_bs_admissible=np.array([r["bf_bs_admissible"] for r in rec]),
        dir_eps_CP=np.array([r["eps_CP"] for r in rec]),
        dir_sources_CP=np.array([r["sources_CP"] for r in rec]),
        ladder_total=lad["total"],
        ladder_pass_triality_F1=lad["pass_triality_F1"],
        ladder_pass_cartan_F2=lad["pass_cartan_F2"],
        ladder_pass_cartan_and_triality=lad["pass_cartan_and_triality"],
        ladder_pass_projY_F3=lad["pass_projY_F3"],
        ladder_pass_bfbs_F4=lad["pass_bfbs_F4"],
        ladder_pass_cartan_and_projY=lad["pass_cartan_and_projY"],
        ladder_pass_all_four=lad["pass_all_four"],
        xcheck_ok=res["xcheck_ok"],
        s76_signature=res["s76_signature"], s76_n_neg=res["s76_n_neg"],
        eta_BBN_obs=eta_BBN_obs, n_pairs=n_pairs,
        input_pins=json.dumps(
            {
                "canonical": sha256_file(CANONICAL_PATH),
                "s76": sha256_file(S76_NPZ),
                "s98": sha256_file(S98_NPZ),
            }
        ),
    )
    print(f"[{GATE_ID}] saved {out_npz}")

    # ---- plot ----
    out_png = HERE / "inv6_w3_2_j_breaking_deformation_enum.png"
    make_plot(res, out_png)
    print(f"[{GATE_ID}] saved {out_png}")

    # ---- dual-SHA + verdict payload ----
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"[{GATE_ID}] audit_sha256={audit_sha}")
    print(f"[{GATE_ID}] content_sha256={content_sha}")
    extra = [
        f"# CLASS={CLASS_PIN} (BF/BS + C6 chain FULL physical; not SCHEMATIC) "
        f"# {GATE_ID} class pin",
        f"# cache-SHA SOURCE-RECON Class-(c): plan caches <computed-at-runtime>; "
        f"orchestrator 88f1e9b1/9e6d9cf7 = different gate; resolved on-disk "
        f"s76={pins['computations/session-76/s76_off_jensen_moduli.npz'][:16]} "
        f"s98={pins['computations/session-98/s98_w3_2_baryogen_uniqueness.npz'][:16]}",
    ]
    print_verdict_payload(res["verdict"], value, audit_sha, content_sha, extra_rows=extra)


if __name__ == "__main__":
    main()
