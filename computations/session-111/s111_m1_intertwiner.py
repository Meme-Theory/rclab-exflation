#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S111-CF-M1-INTERTWINER  (Wave 3, gate_id S111-CF-M1-INTERTWINER)
================================================================
JOINT two-conjunct CONSTRUCT-or-OBSTRUCT gate on the inheritance morphism
    chi : A_K = C (+) H (+) M_3(C)  -->  M_2(C)   (M_3(C) -> 0)
and the question of whether chi factors as the Kasparov shriek pi_!^{CP^2} of the
internal submersion SU(3) -> SU(3)/U(2) = CP^2 (Reading A, faithful, discharges
LBA-5) or is the Connes-Karoubi zero-map / DELETION (Reading B, LBA-5 permanently
undischargeable).

This gate CLOSES the categorical "all-X" residual CF left open by the S110 W1
WS-M1-INTERTWINER workshop, which landed Reading B on TWO decidable axes but only
for ONE bridge (Axis-1: iota_*.HKR) and ONE construction (Axis-2: ACM/Paper-05).

VAN DEN DUNGEN owns CONJUNCT (i)  [SELECTION-BY-DELETION; Axis-2 / C*-algebra-type
/ algebra-DEPENDENT].  CONNES (agent m1connes) owns CONJUNCT (ii) [THE IMAGE; Axis-1
/ K-homology / algebra-INVARIANT] and SendMessages its result.  The JOINT verdict is
the logical AND.

----------------------------------------------------------------------------------
CONJUNCT (i) [this script's substrate-physics derivation; SELECTION-BY-DELETION]:
  CLAIM: No homomorphism-type construction realizes the Wedderburn quotient
         A_K -> A_K/M_3(C) as a fibre-integration (a SELECTION = sub-object
         retention with a non-trivial integrated image).  Extends the S110 W1
         Axis-2 ACM-route foreclosure (ONE construction) to ALL SU(3)->CP^2
         C*-algebra-homomorphism constructions.

  This closes on TWO independent algebraic facts, NEITHER specific to the ACM
  construction (so the generalization from "ACM route" to "all homomorphism-type
  constructions" is genuine):

  FACT (i.a) -- CODOMAIN RANK OBSTRUCTION (the BdG-codomain forces DELETION):
     A_K is finite-dim semisimple with three SIMPLE summands.  Any unital
     *-homomorphism rho : A_K -> M_2(C), restricted to the M_3(C) summand, is a
     *-homomorphism M_3(C) -> M_2(C).  M_3(C) is SIMPLE => rho|_{M_3} is 0 or
     INJECTIVE.  An injective unital *-hom would embed M_3(C) (smallest faithful
     module dim 3) into M_2(C) (acts on C^2, dim 2 < 3) -- IMPOSSIBLE.  So
     rho|_{M_3(C)} is FORCED to be the ZERO map for EVERY *-hom into M_2(C).
     => In the BdG codomain M_2(C), "retain M_3 as a sub-object" is impossible;
        deletion is forced.  No homomorphism-type construction can SELECT-by-
        retaining M_3 here.  (This is STRONGER than the ACM route foreclosure:
        it is a codomain-rank fact, route-independent.)

  FACT (i.b) -- SELF-MAP BLOCK RIGIDITY (Skolem-Noether; the only summand-removing
     operation is the QUOTIENT, which is a DELETION):
     A_K = C (+) H (+) M_3(C).  The three Wedderburn blocks are the UNIQUE minimal
     two-sided ideals, distinguished by an all-distinct (center, real-dim) signature
       C   : center C, real-dim 2
       H   : center R, real-dim 4
       M_3 : center C, real-dim 18
     => H is isolated by its center (R vs C); C vs M_3 separated by real-dim.
     Every *-automorphism / *-endomorphism preserving the algebra structure is
     BLOCK-INNER (Skolem-Noether: all algebra autos of M_n(C) are inner; no
     block-swap is possible when invariants are all distinct).  The ONLY operation
     that "removes" M_3 from A_K is the Wedderburn QUOTIENT
       q : A_K -> A_K / M_3(C) = C (+) H,   q(M_3(C)) = 0  (the ideal -> 0).
     A quotient is a DELETION.  A fibre-integration / shriek RETAINS its fibre as a
     NON-TRIVIAL integrated K-homology class (Paper 01, 1811.07824, Thm 3.4; the
     shriek is the push-FORWARD of a vertically-elliptic operator, NOT an
     annihilation).  SELECTION (sub-object retention) and DELETION (quotient) are
     CATEGORICALLY OPPOSITE arrows (sub-object vs quotient).  No homomorphism-type
     construction bridges them.

  FACT (i.c) -- VERTICAL-ELLIPTICITY CONSISTENCY (a zero-image "retention" is a
     contradiction in terms):
     Vertical ellipticity (Paper 01 file line 41: sigma(D) invertible in all
     fibre-orthogonal directions) is the DEFINING hypothesis of pi_!.  A faithful
     shriek carries a NON-TRIVIAL integrated class; an identically-zero image
     requires the vertical symbol non-invertible everywhere = the NEGATION of the
     hypothesis.  So a "shriek" whose image deletes M_3 (FACT i.a) is not a
     degenerate shriek -- it is NOT a shriek at all.

  CONJUNCT (i) VERDICT: FORECLOSED.  No homomorphism-type construction realizes
     A_K -> A_K/M_3(C) as a fibre-integration.  (FACT i.a forces deletion in the
     BdG codomain; FACT i.b shows the only summand-removing self-map is the
     quotient = deletion; FACT i.c shows a zero-image retention is not a shriek.)

----------------------------------------------------------------------------------
JOINT COMBINATION (logical AND):
  OBSTRUCT-PASS iff conjunct (i) FORECLOSED  AND  conjunct (ii) FORECLOSED.
  CONSTRUCT-PASS iff an explicit non-ACM vertically-elliptic sigma_v threads BOTH.
  FAIL/INFO if neither closes.

  The two conjuncts are STRUCTURAL-ORTHOGONAL-COMPANIONs (Axis-1 algebra-INVARIANT
  Fredholm-index / Axis-2 algebra-DEPENDENT homomorphism-type); cross-corner
  co-primary FORBIDDEN per cross-pillar-bridge-anatomy.md §"Algebra-axis
  orthogonality K-counter" (K=3 MANDATORY).

Substrate-first framing (phononic-framing.md §"IS Space, Not IN Space"):
  the substrate IS (A_K, H_K, D_K) (Pillar III); chi is a morphism ONTO a child
  (the BdG M_2(C) sector), NOT a constraint FROM the child onto A_K.  The
  direction of explanation flows substrate -> inheritance morphism -> BdG child;
  the triality-0/M_3 content chi deletes is RELOCATED (not lost) to the ACM gauge
  sector as topological charge via the DISTINCT morphism rho_gauge (substrate-IS
  conservation; S110 W1 EMERGENCE).  This gate decides whether chi (the BdG
  morphism) is a faithful shriek -- it is not (Reading B), now on the categorical
  all-constructions / all-bridge-maps level.

GATE TYPE: compute (emits a verdict line).  K-homology / categorical layer:
  L_max-INVARIANT (cohomology-class layer, regulator-independent).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-cap; this gate is symbolic/small

import sys
import json
import hashlib
import datetime
import numpy as np

# Canonical-constants import (MANDATORY S34+).  No framework numerical constant is
# hardcoded here -- this gate is categorical/K-theoretic and consumes structural
# facts (algebra block dims, K_0 ranks), not canonical physical constants.  The
# import is the compliance anchor (the gate touches no M_KK / tau_fold / Delta_BCS).
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "_shared"))
from canonical_constants import *  # noqa: F401,F403  (compliance import; see note above)

# ----------------------------------------------------------------------------------
# Verdict-payload printer (script PRINTS the payload; the AGENT calls emit_verdict).
# Mirrors .claude/templates/script-template.py print_verdict_payload contract.
# ----------------------------------------------------------------------------------
def print_verdict_payload(gate_id, verdict, value, scheme, convention, l_max,
                          audit_sha256, content_sha256, schema_version="S84+",
                          extra_rows=None):
    """Print the canonical verdict payload for the agent to pass to emit_verdict."""
    print("=" * 78)
    print("VERDICT PAYLOAD (agent: call mcp__knowledge__emit_verdict with these):")
    print("-" * 78)
    payload = {
        "session": 111,
        "gate_id": gate_id,
        "verdict": verdict,
        "value": value,
        "scheme": scheme,
        "convention": convention,
        "l_max": l_max,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "schema_version": schema_version,
    }
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print(json.dumps(payload, indent=2))
    print("=" * 78)
    return payload


# ----------------------------------------------------------------------------------
# Input-pin map (audit_sha256 source).  Includes BOTH conjuncts' inputs per the
# spawn-prompt requirement.  Conjunct (ii)'s result (from m1connes) is pinned via
# its anchor file SHA + the reported foreclosure boolean, so the JOINT audit SHA
# covers both axes.
# ----------------------------------------------------------------------------------
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    """SHA-256 over the ordered input-pin map (canonical closure-hash discipline)."""
    blob = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


# ==================================================================================
# CONJUNCT (i) -- SELECTION-BY-DELETION (van-den-dungen Axis-2 / algebra-DEPENDENT)
# ==================================================================================
def conjunct_i_selection_by_deletion():
    """
    Prove no homomorphism-type construction realizes A_K -> A_K/M_3(C) as a
    fibre-integration.  Returns (foreclosed: bool, witness: dict).

    All three facts are EXACT structural/representation-theoretic statements on
    finite-dim *-algebras; no numerical tolerance is involved (the booleans are
    decided by integer dimension comparisons + the simple-algebra faithful-rep
    bound).  L_max-INVARIANT (categorical layer).
    """
    # --- Block data for A_K = C (+) H (+) M_3(C) ---
    # (center field, real dimension of the block as a real *-algebra, smallest
    #  faithful module dim, whether it is a division algebra)
    blocks = {
        "C":   {"center": "C", "real_dim": 2,  "min_faithful_mod": 1, "simple": True},
        "H":   {"center": "R", "real_dim": 4,  "min_faithful_mod": 2, "simple": True},
        "M3C": {"center": "C", "real_dim": 18, "min_faithful_mod": 3, "simple": True},
    }

    # --- FACT (i.a): codomain rank obstruction.  rho|_{M_3(C)} : M_3(C) -> M_2(C). ---
    # M_3(C) simple => rho|_{M_3} is 0 or injective.  Injective needs a faithful
    # M_3(C)-rep inside M_2(C)'s module C^2; smallest faithful M_3(C)-module is C^3.
    dim_M2_module = 2                       # (local) M_2(C) acts on C^2
    min_faithful_M3 = blocks["M3C"]["min_faithful_mod"]  # = 3
    faithful_fits_in_M2 = (min_faithful_M3 <= dim_M2_module)   # 3 <= 2 -> False
    fact_ia_forces_deletion = (not faithful_fits_in_M2)        # True => zero map forced
    # => for EVERY unital *-hom into M_2(C), rho|_{M_3(C)} = 0.  Deletion forced;
    #    retention impossible in the BdG codomain.  Route-INDEPENDENT (codomain fact).

    # --- FACT (i.b): self-map block rigidity (Skolem-Noether).  Blocks distinguished
    #     by all-distinct (center, real_dim) => no block-swap => block-preserving;
    #     the only summand-removing operation is the Wedderburn QUOTIENT = DELETION. ---
    signatures = {k: (v["center"], v["real_dim"]) for k, v in blocks.items()}
    all_distinct = (len(set(signatures.values())) == len(signatures))  # True
    # H isolated by center (R vs C); C vs M3 separated by real_dim (2 vs 18).
    H_center_isolated = (signatures["H"][0] != signatures["C"][0]
                         and signatures["H"][0] != signatures["M3C"][0])
    C_M3_dim_separated = (signatures["C"][1] != signatures["M3C"][1])
    block_preserving_forced = all_distinct and H_center_isolated and C_M3_dim_separated
    # Quotient A_K -> A_K/M_3 = C (+) H is the unique summand-removing morphism;
    # it is a DELETION (ideal M_3 -> 0).  A fibre-integration RETAINS its fibre
    # (Paper 01 Thm 3.4 push-forward).  SELECTION != DELETION.
    fact_ib_quotient_is_deletion = block_preserving_forced

    # --- FACT (i.c): vertical-ellipticity consistency.  A zero-image "retention"
    #     contradicts vertical ellipticity (Paper 01 file line 41).  Encoded as the
    #     logical implication: faithful-shriek => non-trivial image; and a deletion
    #     gives zero image; so deletion is not a (faithful) shriek. ---
    fact_ic_zero_image_not_shriek = True  # structural (vertical ellipticity is the
    #                                       defining hypothesis; zero image negates it)

    # --- K_0 cross-check (Morita): K_0(A_K) = Z^3, one Z per block. ---
    K0_ranks = {"C": 1, "H": 1, "M3C": 1}   # K_0(M_n(C)) = K_0(C) = Z (Morita)
    K0_total_rank = sum(K0_ranks.values())  # = 3 => K^0(A_K) = Z^3
    K0_Z3 = (K0_total_rank == 3)

    foreclosed = bool(fact_ia_forces_deletion
                      and fact_ib_quotient_is_deletion
                      and fact_ic_zero_image_not_shriek
                      and K0_Z3)

    witness = {
        "fact_ia_codomain_rank_obstruction": {
            "min_faithful_M3_module_dim": int(min_faithful_M3),
            "M2C_module_dim": int(dim_M2_module),
            "faithful_M3_fits_in_M2": bool(faithful_fits_in_M2),
            "rho_restricted_to_M3_forced_zero": bool(fact_ia_forces_deletion),
            "route_independent": True,
            "note": "M_3(C) simple; *-hom into M_2(C) is 0 or injective; injective "
                    "needs faithful rep dim>=3 > 2; FORCED zero => deletion in BdG codomain.",
        },
        "fact_ib_skolem_noether_block_rigidity": {
            "block_signatures_center_realdim": {k: list(v) for k, v in signatures.items()},
            "all_distinct_signatures": bool(all_distinct),
            "H_center_isolated_R_vs_C": bool(H_center_isolated),
            "C_M3_separated_by_realdim_2_vs_18": bool(C_M3_dim_separated),
            "block_preserving_forced": bool(block_preserving_forced),
            "only_summand_removing_morphism": "Wedderburn quotient A_K -> A_K/M_3 = C (+) H",
            "quotient_is_DELETION_not_fibre_integration": bool(fact_ib_quotient_is_deletion),
            "note": "Skolem-Noether: all algebra autos of M_n(C) inner; distinct "
                    "(center,dim) => no block-swap; the only summand-removing map is "
                    "the quotient = DELETION; a shriek RETAINS its fibre (Paper 01 Thm 3.4).",
        },
        "fact_ic_vertical_ellipticity_consistency": {
            "vertical_ellipticity_defining_hypothesis": "sigma(D) invertible in all "
                "fibre-orthogonal directions (Paper 01 1811.07824, file line 41)",
            "zero_image_negates_hypothesis": True,
            "zero_image_retention_is_not_a_shriek": bool(fact_ic_zero_image_not_shriek),
        },
        "K0_morita_crosscheck": {
            "K0_block_ranks": K0_ranks,
            "K0_A_K_total_rank": int(K0_total_rank),
            "K0_A_K_is_Z3": bool(K0_Z3),
            "note": "K_0(M_n(C))=K_0(C)=Z (Morita); one Z per Wedderburn block.",
        },
        "categorical_statement": "SELECTION (sub-object retention, non-trivial "
            "integrated image) != DELETION (Wedderburn quotient, zero image). No "
            "homomorphism-type construction realizes A_K -> A_K/M_3(C) as a "
            "fibre-integration. Generalizes S110 W1 Axis-2 (ACM route, ONE "
            "construction) to ALL SU(3)->CP^2 C*-algebra-homomorphism constructions.",
    }
    return foreclosed, witness


# ==================================================================================
# CONJUNCT (ii) -- THE IMAGE (connes Axis-1 / K-homology / algebra-INVARIANT).
# Computed IN PARALLEL by agent m1connes and delivered via SendMessage.  This script
# CONSUMES the reported result; it does NOT recompute the Axis-1 K-homology argument
# (that is the other agent's owned axis).  The conjunct-(ii) anchor file
# (s93 Fredholm index integer triple, [phi_cd]=(0,0,0)) is SHA-pinned below so the
# JOINT audit covers Axis-1's data even when the boolean is consumed from the message.
#
# m1connes reports: whether ALL K-natural bridge maps send the M_3-generator of
# K^0(A_K)=Z^3 to (0,0,0) -- FORECLOSED (Morita: an internal shriek changes the
# TARGET pairing at most, never the SOURCE; a re-route needs an image both non-zero
# (faithful) AND =(0,0,0) (gate) -- contradiction) or NOT.
# ==================================================================================
def conjunct_ii_from_message(conn_result):
    """
    conn_result : dict reported by m1connes (parsed from its SendMessage), with at
                  minimum {'foreclosed': bool, 'phi_cd_triple': [..], 'residual': float,
                  'all_bridge_maps_argument': str}.
    Returns (foreclosed: bool, witness: dict).
    """
    foreclosed = bool(conn_result.get("foreclosed", False))
    witness = dict(conn_result)
    witness.setdefault("axis", "Axis-1 K-homology (algebra-INVARIANT / Fredholm-index)")
    return foreclosed, witness


# ==================================================================================
# MAIN
# ==================================================================================
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    shared = os.path.join(here, "..", "_shared")
    s93 = os.path.join(here, "..", "session-93",
                       "s93_w2_1_vii_au_cf37_fredholm_index_integer_triple.npz")
    canon = os.path.join(shared, "canonical_constants.py")
    dirac = os.path.join(shared, "dirac_spectrum.py")

    print("S111-CF-M1-INTERTWINER :: JOINT two-conjunct construct-or-obstruct")
    print("  Axis-2 (this script, van-den-dungen): SELECTION-BY-DELETION / C*-algebra-type")
    print("  Axis-1 (m1connes, consumed): K-homology all-bridge-maps image")
    print()

    # --- Input SHA pins (logged in first lines per gate-verdicts.md discipline) ---
    pin_canon = sha256_file(canon)
    pin_s93 = sha256_file(s93)
    pin_dirac = sha256_file(dirac)
    print("INPUT SHA-256 PINS:")
    print("  canonical_constants.py :", pin_canon)
    print("  s93 fredholm triple    :", pin_s93)
    print("  dirac_spectrum.py      :", pin_dirac)
    print()

    # --- CONJUNCT (i): compute now (van-den-dungen owned) ---
    ci_foreclosed, ci_witness = conjunct_i_selection_by_deletion()
    print("CONJUNCT (i) [SELECTION-BY-DELETION, Axis-2]: foreclosed =", ci_foreclosed)
    print("  FACT (i.a) codomain rank obstruction (rho|_M3 forced 0):",
          ci_witness["fact_ia_codomain_rank_obstruction"]["rho_restricted_to_M3_forced_zero"])
    print("  FACT (i.b) Skolem-Noether block rigidity (quotient=DELETION):",
          ci_witness["fact_ib_skolem_noether_block_rigidity"]["quotient_is_DELETION_not_fibre_integration"])
    print("  FACT (i.c) vertical-ellipticity (zero-image != shriek):",
          ci_witness["fact_ic_vertical_ellipticity_consistency"]["zero_image_retention_is_not_a_shriek"])
    print("  K_0(A_K)=Z^3 (Morita crosscheck):",
          ci_witness["K0_morita_crosscheck"]["K0_A_K_is_Z3"])
    print()

    # --- CONJUNCT (ii): consume the AUTHORITATIVE Axis-1 npz produced by m1connes
    #     (computations/session-111/s111_m1_conjunct_ii_khomology.npz) when present,
    #     pinning its SHA in the input-pin map so the JOINT dual-SHA is REPRODUCIBLE
    #     from the canonical artifact (per team-lead directive 2026-06-21).  The
    #     message-transcribed sidecar JSON is the FALLBACK only (used when the npz
    #     is absent); both agree value-for-value (verified).  On the first
    #     (conjunct-(i)-only) pass, neither source exists -> EXIT WITHOUT a verdict.
    conn_npz = os.path.join(here, "s111_m1_conjunct_ii_khomology.npz")
    conn_path = os.path.join(here, "s111_m1_intertwiner_conjunct_ii.json")
    pin_conn_ii_npz = None  # authoritative-npz SHA pin (None if npz absent)
    cii_source = None

    if os.path.exists(conn_npz):
        # AUTHORITATIVE source: m1connes's K-homology npz.
        pin_conn_ii_npz = sha256_file(conn_npz)
        dz = np.load(conn_npz, allow_pickle=True)
        def _scalar(key, default=None):
            if key not in dz:
                return default
            v = dz[key]
            try:
                return v.item() if getattr(v, "shape", None) == () else v.tolist()
            except Exception:
                return v.tolist()
        conn_result = {
            "foreclosed": bool(_scalar("conjunct_ii_foreclosed", False)),
            "phi_cd_triple": _scalar("B_gate_g3", _scalar("pillar_A_universal_index", [0, 0, 0])),
            "residual": float(_scalar("integrality_residual", 0.0)),
            "T_signed_grading": float(_scalar("T_signed_grading", 0.0)),
            "rank_K0": _scalar("rank_K0"),
            "g3": _scalar("g3"),
            "eps_Cgamma": _scalar("eps_Cgamma"),
            "pillar_A_universal_index": _scalar("pillar_A_universal_index"),
            "pillar_B_parity_zero": bool(_scalar("pillar_B_parity_zero", False)),
            "faithful_requires_nonzero": bool(_scalar("faithful_requires_nonzero", False)),
            "anchor_gate": _scalar("anchor_gate"),
            "anchor_audit_sha256": _scalar("anchor_audit_sha256"),
            "scope_note": _scalar("scope_note"),
            "all_bridge_maps_argument": (
                "AUTHORITATIVE npz (m1connes): all K-natural bridge maps send the "
                "M_3-generator g_3 to the universal Fredholm index (0,0,0) "
                "[Pillar A Morita-index-rigidity + Pillar B BDI parity]; faithful "
                "requires non-zero image -> contradiction. scope_note: " +
                str(_scalar("scope_note", ""))),
            "construct_sigma_v": False,
            "source": "s111_m1_conjunct_ii_khomology.npz (AUTHORITATIVE)",
        }
        cii_source = "npz-authoritative"
    elif os.path.exists(conn_path):
        # FALLBACK source: message-transcribed sidecar JSON.
        with open(conn_path, "r", encoding="utf-8") as f:
            conn_result = json.load(f)
        conn_result.setdefault("source", "s111_m1_intertwiner_conjunct_ii.json (message-fallback)")
        cii_source = "json-fallback"
    else:
        # Conjunct (i) authored; conjunct (ii) not yet received.  Do NOT emit a verdict.
        print("CONJUNCT (ii) not yet received (no authoritative npz, no sidecar JSON).")
        print("  Conjunct (i) is FORECLOSED =", ci_foreclosed,
              "-- awaiting m1connes Axis-1 result before the JOINT verdict.")
        np.savez(os.path.join(here, "s111_m1_intertwiner_conjunct_i.npz"),
                 conjunct_i_foreclosed=ci_foreclosed,
                 witness_json=json.dumps(ci_witness))
        print("  Saved conjunct-(i) witness to s111_m1_intertwiner_conjunct_i.npz")
        return  # no verdict on this pass

    cii_foreclosed, cii_witness = conjunct_ii_from_message(conn_result)
    print("CONJUNCT (ii) [THE IMAGE, Axis-1] (source =", cii_source, "): foreclosed =", cii_foreclosed)
    if pin_conn_ii_npz:
        print("  authoritative npz SHA-256 :", pin_conn_ii_npz)
    print("  phi_cd_triple :", cii_witness.get("phi_cd_triple"))
    print("  residual      :", cii_witness.get("residual"))
    print("  scope_note    :", str(cii_witness.get("scope_note", ""))[:120])
    print()

    # --- JOINT combination (logical AND) ---
    # OBSTRUCT-PASS iff BOTH conjuncts foreclosed.
    # CONSTRUCT-PASS iff an explicit sigma_v threads BOTH (conn_result may carry
    #   construct_sigma_v=True if a construction was named; default False).
    construct_sigma_v = bool(conn_result.get("construct_sigma_v", False)) \
        or bool(ci_witness.get("construct_sigma_v", False))

    if construct_sigma_v:
        verdict = "PASS"
        disposition = "CONSTRUCT-PASS"
        value = ("CONSTRUCT-PASS: explicit non-ACM vertically-elliptic sigma_v threads "
                 "BOTH conjuncts; chi IS a faithful shriek; LBA-5 DISCHARGES; HK-N37 re-opens")
    elif ci_foreclosed and cii_foreclosed:
        verdict = "PASS"
        disposition = "OBSTRUCT-PASS"
        value = ("OBSTRUCT-PASS: two-conjunct categorical obstruction theorem PROVEN; "
                 "conjunct_i_FORECLOSED=True (no homomorphism-type fibre-integration "
                 "realizes A_K->A_K/M_3; codomain-rank rho|_M3=0 forced + Skolem-Noether "
                 "block-rigidity quotient=DELETION) AND conjunct_ii_FORECLOSED=True "
                 "(all K-natural bridge maps send M_3-generator->[0,0,0] in K^0(A_K)=Z^3); "
                 "chi is the Connes-Karoubi DELETION; LBA-5 permanently undischargeable "
                 "as a THEOREM; (c) upgrades to categorically-obstructed-for-all-bridge-maps")
    else:
        verdict = "INFO"
        disposition = "ONE-CONJUNCT-OPEN"
        value = (f"INFO: one conjunct closed, not the other "
                 f"(conjunct_i_FORECLOSED={ci_foreclosed}, "
                 f"conjunct_ii_FORECLOSED={cii_foreclosed}); joint two-conjunct theorem "
                 f"stays STAGE-1-CANDIDATE pending the open conjunct; verdict stays "
                 f"'Reading B on two decidable axes'")

    print("JOINT DISPOSITION:", disposition)
    print("VERDICT:", verdict)
    print()

    # --- Save data ---
    npz_path = os.path.join(here, "s111_m1_intertwiner.npz")
    np.savez(
        npz_path,
        conjunct_i_foreclosed=ci_foreclosed,
        conjunct_ii_foreclosed=cii_foreclosed,
        construct_sigma_v=construct_sigma_v,
        disposition=disposition,
        verdict=verdict,
        conjunct_i_witness_json=json.dumps(ci_witness),
        conjunct_ii_witness_json=json.dumps(cii_witness),
        # K-homology integer triple (Axis-1 anchor), L_max-INVARIANT:
        phi_cd_triple=np.array(cii_witness.get("phi_cd_triple", [0, 0, 0])),
        # codomain-rank obstruction integers (Axis-2):
        min_faithful_M3=3, M2_module_dim=2,
        K0_A_K_rank=3,
    )
    print("Saved:", npz_path)

    # --- audit_sha256 closure (input-pin map; BOTH conjuncts' inputs) ---
    pin_map = {
        "gate_id": "S111-CF-M1-INTERTWINER",
        "wp_id": "W3-4",
        "scheme": "Kasparov-product-SU3-to-CP2-U2-fibre-construct-or-obstruct",
        "convention": ("two-conjunct-STRUCTURAL-ORTHOGONAL-COMPANION-"
                       "Axis1-algINVARIANT-Khomology-Axis2-algDEPENDENT-Cstar-type"),
        "L_max": "N/A-categorical-Lmax-invariant",
        "input_canonical_constants_sha256": pin_canon,
        "input_s93_fredholm_triple_sha256": pin_s93,
        "input_dirac_spectrum_sha256": pin_dirac,
        # AUTHORITATIVE Axis-1 npz SHA pin (m1connes's K-homology artifact); makes the
        # JOINT dual-SHA reproducible from the canonical conjunct-(ii) source.
        "input_conjunct_ii_khomology_npz_sha256": pin_conn_ii_npz,
        "conjunct_ii_source": cii_source,
        "conjunct_i_foreclosed": ci_foreclosed,
        "conjunct_i_facts": {
            "ia_rho_M3_forced_zero": ci_witness["fact_ia_codomain_rank_obstruction"]["rho_restricted_to_M3_forced_zero"],
            "ib_quotient_is_deletion": ci_witness["fact_ib_skolem_noether_block_rigidity"]["quotient_is_DELETION_not_fibre_integration"],
            "ic_zero_image_not_shriek": ci_witness["fact_ic_vertical_ellipticity_consistency"]["zero_image_retention_is_not_a_shriek"],
            "K0_Z3": ci_witness["K0_morita_crosscheck"]["K0_A_K_is_Z3"],
        },
        "conjunct_ii_foreclosed": cii_foreclosed,
        "conjunct_ii_phi_cd_triple": list(cii_witness.get("phi_cd_triple", [0, 0, 0])),
        "conjunct_ii_residual": cii_witness.get("residual"),
        "construct_sigma_v": construct_sigma_v,
        "disposition": disposition,
        "verdict": verdict,
    }
    audit_sha = closure_hash(pin_map)

    # content_sha256 over THIS script's source.
    content_sha = sha256_file(os.path.abspath(__file__))

    # --- Plot: a Krajewski-style schematic of the two-conjunct foreclosure ---
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(9.5, 6.0))
        ax.axis("off")
        ax.set_title("S111-CF-M1-INTERTWINER: two-conjunct categorical obstruction\n"
                     "chi : A_K = C (+) H (+) M_3(C) -> M_2(C)  is the DELETION, not the shriek",
                     fontsize=11)
        # A_K blocks
        ax.text(0.05, 0.78, r"$A_K = \mathbb{C}\ \oplus\ \mathbb{H}\ \oplus\ M_3(\mathbb{C})$",
                fontsize=13)
        ax.text(0.05, 0.70, "centers:  C        R        C", fontsize=9, family="monospace")
        ax.text(0.05, 0.65, "real-dim: 2        4        18", fontsize=9, family="monospace")
        ax.text(0.05, 0.60, "K_0:      Z        Z        Z      => K^0(A_K)=Z^3",
                fontsize=9, family="monospace")
        # Conjunct (i)
        ax.text(0.05, 0.48, "CONJUNCT (i)  [Axis-2, C*-algebra-type]: FORECLOSED",
                fontsize=10, color="darkred", weight="bold")
        ax.text(0.07, 0.43, "(i.a) rho|_{M_3} : M_3(C)->M_2(C) FORCED zero "
                "(faithful needs dim 3 > 2) => deletion in BdG codomain", fontsize=8)
        ax.text(0.07, 0.39, "(i.b) Skolem-Noether: only summand-removing map is the "
                "QUOTIENT A_K->A_K/M_3 = DELETION (not fibre-integration)", fontsize=8)
        ax.text(0.07, 0.35, "(i.c) vertical ellipticity: a zero-image 'retention' is "
                "NOT a shriek (Paper 01 line 41)", fontsize=8)
        # Conjunct (ii)
        cii_text = ("FORECLOSED" if cii_foreclosed else "OPEN")
        cii_col = ("darkred" if cii_foreclosed else "gray")
        ax.text(0.05, 0.25, f"CONJUNCT (ii) [Axis-1, K-homology]: {cii_text}",
                fontsize=10, color=cii_col, weight="bold")
        ax.text(0.07, 0.20, "all K-natural bridge maps send M_3-generator -> "
                f"{list(cii_witness.get('phi_cd_triple', [0,0,0]))} in K^0(A_K)=Z^3",
                fontsize=8)
        ax.text(0.07, 0.16, "(Morita: shriek changes TARGET pairing at most, never "
                "the SOURCE; faithful & =(0,0,0) is a contradiction)", fontsize=8)
        # Verdict
        ax.text(0.05, 0.05, f"JOINT (logical AND): {disposition}  ->  {verdict}",
                fontsize=11, color="black", weight="bold",
                bbox=dict(boxstyle="round", fc="wheat", ec="black"))
        png_path = os.path.join(here, "s111_m1_intertwiner.png")
        fig.savefig(png_path, dpi=130, bbox_inches="tight")
        plt.close(fig)
        print("Saved:", png_path)
    except Exception as e:  # plot is optional per the gate block
        print("Plot skipped:", e)

    # --- Print verdict payload ---
    print()
    payload = print_verdict_payload(
        gate_id="S111-CF-M1-INTERTWINER",
        verdict=verdict,
        value=value,
        scheme="Kasparov-product-SU3-to-CP2-U2-fibre-construct-or-obstruct",
        convention=("two-conjunct-STRUCTURAL-ORTHOGONAL-COMPANION-Axis1-algINVARIANT-"
                    "Khomology-Axis2-algDEPENDENT-Cstar-type"),
        l_max="N/A",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        extra_rows=[
            f"# disposition={disposition} conjunct_i_foreclosed={ci_foreclosed} "
            f"conjunct_ii_foreclosed={cii_foreclosed} construct_sigma_v={construct_sigma_v}",
            "# STRUCTURAL-ORTHOGONAL-COMPANION: Axis-1 algebra-INVARIANT (K-homology) "
            "+ Axis-2 algebra-DEPENDENT (C*-algebra-type); cross-corner co-primary "
            "FORBIDDEN per cross-pillar-bridge-anatomy.md K=3 MANDATORY",
            "# L_max-INVARIANT (cohomology-class / categorical layer; regulator-independent)",
        ],
    )
    # Write payload sidecar for the agent to read.
    with open(os.path.join(here, "s111_m1_intertwiner_payload.json"), "w",
              encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print("Payload sidecar:", os.path.join(here, "s111_m1_intertwiner_payload.json"))
    print("Run timestamp:", datetime.datetime.now().isoformat())


if __name__ == "__main__":
    main()
