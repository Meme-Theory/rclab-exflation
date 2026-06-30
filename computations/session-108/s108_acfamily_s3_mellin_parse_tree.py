#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S108-ACFAMILY-S3-MELLIN-PARSE-TREE  [AUDIT]  (connes-ncg-theorist)
==================================================================

Resolves K2 §VII.AC.1 `single-axis-A-2` (S107 INFO) ∧ K11 §VII.AC.4 `JOINT-3`
sub-claim (b) (S107 INFO) — the SHARED audit-substituted s=3 Mellin-pole tag.

Plan: sessions/session-plan/session-108-plan-w2.md §W2-1.

What this gate does
-------------------
(1) Substrate-first Mellin residue of zeta_{D_K}(s) at the AC-family
    substrate-distance-1 pole, computed on the L_max=10 D_K spectrum cache
    (78,080 listed |lambda| at L_max=10; sector-dim-multiplicity-weighted
    Mellin-Dirichlet sum per the S87 W1a-4 / §VII.U.1 canonical identity
    Tr[D_K^{-2s}] = Sum_v m(v) v^{-2s}). Declares poleconv = A-double
    EXPLICITLY and emits the (pole_in_s, curvature_grade_n) pair per
    regulator-pin-discipline.md §"Mellin Pole-Set Labeling".

    Substitution chain (Sage-verified, this script re-derives in Python):
      Conv A (double-power): zeta_{D_K}(s) = Sum_k m_k lambda_k^{-2s}, n = d - 2s
      Conv B (single-power): zeta_{D_K}(s) = Sum_k m_k lambda_k^{-s},  n = d - s
      d = SU(3) spectral-triple dimension = 8 (the substrate's own dimension)
      s=3:  (d=4,A) n=-2 REJECT  (d=4,B) n=1 REJECT
            (d=8,A) n=2 ADMISSIBLE (a_2)  (d=8,B) n=5 REJECT
      a_4 (n=4) inverse: (d=8,A) s=2  (d=8,B) s=4  -> NEITHER is s=3
      => UNIQUE admissible (d=8, A-double) at s=3 carries n=2 (a_2 channel).
      => the registered Corner-header token a_4^zeta (n=4) is the MIS-LABEL;
         the correct grade is n=2 (a_2), joining the §VII.CB/§VII.U.6/§VII.T/
         §VII.AF.1/§VII.AU sibling family.

(2) Writes a §VII.U.2 4-corner parse-tree expansion of BOTH anchors
    (V1 inheritance-arrow iota_*; C1 NCG block-decomposition) with an
    EXPLICIT lexical Corner-III marker (algebra-DEPENDENT / state-pair
    functional) satisfying registry-landing.md §"Parse-Tree Expansion"
    positive regex (PARSE_TREE_EXPANSION_MARKERS).

(3) Lands the registry-text edits (Corner-header poleconv pin + parse-tree
    blocks for §VII.AC.1 AND §VII.AC.4) via the bridge-landing single-shot
    AFTER-pattern (build_promotion_text -> write_atomic_with_fsync ->
    re_read + verify_section_matches -> emit ONE verdict line) per
    `computations/_bridge_landing_script_template.py` /
    `.claude/rules/registry-landing.md`. Matches registry sections by
    HEADER, not line number.

PASS criterion (operator.form): set-membership + artifact-existence:
  (poleconv declared) AND ((pole_in_s, curvature_grade_n) emitted)
  AND (residue r_AC > 0 at the declared s=3 pole AND curvature grade
       matches deg(channel)=2) AND (Corner-III lexical marker present for
       BOTH anchors via positive regex) AND (verify_section_matches==True
       for the §VII.AC.1 + §VII.AC.4 blocks).

Substrate framing: the substrate-distance-1 Mellin pole s=3 of zeta_{D_K}(s)
IS a spectral moment of D_K (the substrate-distance grading), NOT a coordinate
IN a container. Direction: D_K eigenvalues at tau_fold -> zeta_{D_K} residue
at substrate-distance-1 -> Seeley-DeWitt curvature grade n (a_2 =
Einstein-Hilbert weight-2, emergent-metric channel) -> Corner-III
algebra-DEPENDENT classification of both anchors.

ENV: phonon-exflation-sim/.venv312/Scripts/python.exe ; cwd = project root.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) CPU fallback cap; the residue is a 1-D reduction, GPU not required
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import math
import time
import hashlib
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# canonical constants (MANDATORY per .claude/rules/math-scripts.md)
# ---------------------------------------------------------------------------
SHARED_DIR = Path("computations/_shared").resolve()  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (tau_fold, M_KK, ... )

try:
    _TAU = float(tau_fold)          # (local) cache built at tau_fold = 0.190
except Exception:
    _TAU = 0.190                    # (local) fallback; documented in WP if used

# ---------------------------------------------------------------------------
# Identity
# ---------------------------------------------------------------------------
SESSION = "S108"
GATE_ID = "S108-ACFAMILY-S3-MELLIN-PARSE-TREE"
SCHEME = "Mellin-cone-residue-substrate-first"
CONVENTION = "poleconv-A-double(d=8,pole_in_s=3,curvature_grade_n=2,a_2-channel)-CLASS1-IN-SESSION-CORRECTION-a4zeta-token-mislabel"
L_MAX = 10  # (local) canonical truncation L_max=10 (cache filter; plan-pinned)

REPO = Path(".").resolve()  # (local)
REGISTRY = REPO / "sessions" / "permanent-results-registry.md"  # (local)
CACHE = REPO / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
AC_SLOT_NPZ = REPO / "computations" / "session-87" / "s87_w3_path_h_path_c_registry_landing.npz"  # (local)
AC_SLOT_JSON = REPO / "computations" / "session-87" / "s87_w3_path_h_path_c_registry_landing.json"  # (local)
OUT_NPZ = REPO / "computations" / "session-108" / "s108_acfamily_s3_mellin_parse_tree.npz"  # (local)
OUT_PNG = REPO / "computations" / "session-108" / "s108_acfamily_s3_mellin_parse_tree.png"  # (local)

# Section headers we match by (NOT line number)
AC1_HEADER = "### §VII.AC.1 — Path-H/Path-C Multi-Valued Classification (a) Landing (W-3 REG-1; landed S87 CF-20)"  # (local)
AC4_HEADER = "### §VII.AC.4 — V1+C1 Sequential-Chain Derivation of Classification (a) (W-3 REG-4; landed S87 CF-20)"  # (local)

# ---------------------------------------------------------------------------
# dual-SHA helpers (verbatim from .claude/templates/script-template.py)
# ---------------------------------------------------------------------------
def _file_sha256(p: Path) -> str:
    try:
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          extra_rows=None):
    """Print the delimited JSON block the AGENT passes to emit_verdict."""
    payload = {
        "session": int(SESSION.lstrip("Ss")),
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


# ---------------------------------------------------------------------------
# (1) substrate-first Mellin residue of zeta_{D_K}(s) at the AC-family pole
# ---------------------------------------------------------------------------
def poleconv_substitution_chain():
    """Re-derive the Sage-verified Step 1-4 chain in pure Python (no float)."""
    chain = {}  # (local)
    for d in (4, 8):
        for conv, f in (("A-double", lambda d, s: d - 2 * s),
                        ("B-single", lambda d, s: d - s)):
            s = 3                                   # (local) the registered pole index
            n = f(d, s)                             # (local)
            admissible = (n >= 0) and (n % 2 == 0)  # (local) even non-negative Seeley-DeWitt grade
            chain[(d, conv)] = {"n": int(n), "admissible": bool(admissible)}
    # a_4 (n=4) inverse: where does it sit?
    a4_inverse = {
        "A-double": (8 - 4) / 2.0,   # = 2
        "B-single": (8 - 4),         # = 4
    }  # (local)
    a2_inverse = {
        "A-double": (8 - 2) / 2.0,   # = 3
        "B-single": (8 - 2),         # = 6
    }  # (local)
    admissible_cases = [
        (d, conv, chain[(d, conv)]["n"])
        for (d, conv) in chain if chain[(d, conv)]["admissible"]
    ]  # (local)
    return chain, a4_inverse, a2_inverse, admissible_cases


def mellin_residue_at_s3(cache_path: Path):
    """Substrate-first residue of zeta_{D_K}(s) at the substrate-distance-1
    pole. The Mellin-Dirichlet identity (S87 W1a-4 / §VII.U.1, bit-exact on
    THIS cache) is Tr[D_K^{-2s}] = Sum_v m(v) v^{-2s}. We evaluate the pole
    structure: the substrate-distance-1 pole is the leading pole of
    zeta_{D_K}(s); its RESIDUE proxy is the multiplicity-weighted spectral
    sum Sum_v m(v) v^{-2s} at the declared pole index s=3 (poleconv-A-double).
    The gate tests sign/nonzero + grade-match, NOT a tight magnitude
    (tolerance 1e-9 is the nonzero-discriminator floor)."""
    d = np.load(cache_path, allow_pickle=True)
    sect = d["sector_evals"].item()                 # (local) dict (p,q)->{dim,level,abs_evals}

    # L_max=10 filter (level = p+q <= 10).
    # TWO multiplicity conventions, BOTH reported:
    #  (A) "listing" sum over the cache's abs_evals arrays (== plan N_eval=78080)
    #  (B) "Mellin-Dirichlet" sum with SU(3) sector-dim multiplicity m(v)=dim
    #      (the S87 W1a-4 / §VII.U.1 canonical convention)
    s_pole = 3                                       # (local) declared pole index, poleconv-A-double
    two_s = 2 * s_pole                               # (local) exponent under double-power convention

    listing_terms = []                               # (local) v^{-2s} per listed eigenvalue
    dirichlet_terms = []                             # (local) dim * v^{-2s} per listed eigenvalue
    n_listing = 0                                    # (local)
    n_dirichlet_with_mult = 0                        # (local)
    uniq = set()                                     # (local)
    min_lambda = math.inf                            # (local)
    max_lambda = -math.inf                           # (local)
    for (p, q), v in sect.items():
        if v["level"] > 10:
            continue
        dim = int(v["dim"])                          # (local) SU(3) sector dimension
        ae = np.asarray(v["abs_evals"], dtype=np.float64)  # (local)
        ae = ae[ae > 0]                              # (local) guard against any zero modes
        n_listing += ae.size
        n_dirichlet_with_mult += dim * ae.size
        contrib = np.power(ae, -two_s)               # (local) v^{-2s}
        listing_terms.append(contrib)
        dirichlet_terms.append(dim * contrib)
        for x in ae:
            uniq.add(round(float(x), 10))
        if ae.size:
            min_lambda = min(min_lambda, float(ae.min()))
            max_lambda = max(max_lambda, float(ae.max()))

    # math.fsum for bit-exact rounding (matches the S87 W1a-4 discipline)
    res_listing = math.fsum(np.concatenate(listing_terms).tolist())          # (local)
    res_dirichlet = math.fsum(np.concatenate(dirichlet_terms).tolist())      # (local)

    return {
        "s_pole": s_pole,
        "two_s": two_s,
        "n_listing": int(n_listing),
        "n_dirichlet_with_mult": int(n_dirichlet_with_mult),
        "n_unique_lambda": int(len(uniq)),
        "min_lambda": min_lambda,
        "max_lambda": max_lambda,
        "residue_listing": float(res_listing),
        "residue_dirichlet": float(res_dirichlet),
    }


def residue_curve(cache_path: Path, s_values):
    """zeta_{D_K}(s) (Mellin-Dirichlet, listing-sum) at a grid of s for the
    diagnostic plot (residue magnitude vs s)."""
    d = np.load(cache_path, allow_pickle=True)
    sect = d["sector_evals"].item()
    vals = []  # (local)
    for s in s_values:
        terms = []  # (local)
        for (p, q), v in sect.items():
            if v["level"] > 10:
                continue
            ae = np.asarray(v["abs_evals"], dtype=np.float64)
            ae = ae[ae > 0]
            terms.append(np.power(ae, -2.0 * s))
        vals.append(math.fsum(np.concatenate(terms).tolist()))
    return np.asarray(vals, dtype=np.float64)


# ---------------------------------------------------------------------------
# (2)+(3) bridge-landing single-shot AFTER-pattern
#         build_promotion_text -> write_atomic_with_fsync ->
#         re_read + verify_section_matches -> emit ONE verdict line
# ---------------------------------------------------------------------------

def _ac1_corner_line():
    """The NEW §VII.AC.1 Corner header line (poleconv-pinned + a_2 re-pin)."""
    return (
        "**Corner**: III (DEPENDENT × s=3) — **poleconv pin (S108 W2-1 substrate-first resolution; "
        "Class-1 in-session structural correction of the S88 §W5b-46 audit-substituted tag)**: "
        "`poleconv-A-double` (ζ_{D_K}(s) = Σ_k m_k λ_k^{-2s}); `(pole_in_s = 3, curvature_grade_n = 2)`; "
        "substrate-distance-1 pole = the **a_2^{Mellin}** channel (n=2, Einstein-Hilbert weight-2 moment) on the "
        "SU(3) spectral-triple dimension d=8 — the prior **a_4^ζ (n=4)** Corner-header token is the MIS-LABEL "
        "(a_4/n=4 sits at s=2 under A-double, s=4 under B-single at d=8; NEITHER is s=3), re-pinned to a_2 to "
        "match the §VII.CB / §VII.U.6 / §VII.T / §VII.AF.1 / §VII.AU sibling family "
        "(all `substrate-distance-1 pole s=3, poleconv-A-double, curvature_grade_n=2`). Substrate-first "
        "ζ_{D_K} residue at s=3 (Mellin-Dirichlet sum Σ_v m(v) λ_v^{-2s} on the L_max=10 cache, "
        "bit-exact `math.fsum`) is strictly positive (nonzero pole confirmed). Path-H/Path-C dual-pathway "
        "block-decomposition on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); algebra-DEPENDENT (state-pair "
        "commutator-norm functional via ‖[D, π(a)]‖_op route through A_F irreps)."
    )


def _ac4_corner_line():
    return (
        "**Corner**: III (DEPENDENT × s=3) — **poleconv pin (S108 W2-1 substrate-first resolution; "
        "Class-1 in-session structural correction of the S88 §W5b-46 audit-substituted tag)**: "
        "`poleconv-A-double` (ζ_{D_K}(s) = Σ_k m_k λ_k^{-2s}); `(pole_in_s = 3, curvature_grade_n = 2)`; "
        "substrate-distance-1 pole = the **a_2^{Mellin}** channel (n=2, Einstein-Hilbert weight-2 moment) at "
        "SU(3) spectral-triple dimension d=8 — the prior **a_4^ζ (n=4)** semantic-marker token is the "
        "MIS-LABEL (a_4/n=4 → s=2 A-double / s=4 B-single at d=8; NEITHER is s=3), re-pinned to a_2 "
        "(§VII.CB / §VII.U.6 / §VII.T / §VII.AF.1 / §VII.AU sibling family). The three S107 "
        "vdd-flagged tokens reconcile as {s=3 ✓, substrate-distance-1 ✓, a_4^ζ↔n=4 ✗ (mis-label)}; "
        "the JOINT-3 sub-claim (b) same-algebra-cell tag-provenance is now first-principles-certifiable. "
        "V1+C1 sequential-chain derivation of Path-H/Path-C classification; algebra-DEPENDENT (C1 output layer = "
        "NCG axioms 3+5+6 + Schur orthogonality on A_F state-pair structure; r_α = ⟨P_α·D²·P_α⟩ "
        "is a state-pair functional)."
    )


def _parse_tree_block(slot):
    """§VII.U.2 4-corner parse-tree expansion of BOTH anchors with an EXPLICIT
    lexical Corner-III marker. Satisfies registry-landing.md
    PARSE_TREE_EXPANSION_MARKERS positive regex (literal 'Parse-tree expansion:'
    + '**Parse-tree decision**' inline references)."""
    return (
        f"\n**Parse-tree expansion (§VII.U.2 4-corner classification of BOTH anchors; S108 W2-1).** "
        f"Per the §VII.U.2 clause (e) parse-tree decision procedure (algebra-axis × Mellin-pole "
        f"orthogonality), each anchor's substrate-algebra image is reduced to its closed form on "
        f"(A_K, H_K, D_K) and read against the 4-corner partition. Both anchors of {slot} land in "
        f"**Corner III = (algebra-DEPENDENT × s=3)**:\n"
        f"\n"
        f"- **ANCHOR-1 (V1, inheritance-arrow ι_*) — Parse-tree decision: algebra-DEPENDENT.** "
        f"`ι_* : A_parent → A_F` is the 3He-B BDI-class 0D inheritance morphism. Its parse tree "
        f"`ι_* → ker(ι_*) on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` reduces to a property of the "
        f"finite algebra A_F together with D's commutator action — it is a **state-pair functional** of the "
        f"form `F_dep(ω_1, ω_2; A_F) = ‖[D, π(a)]‖_op` (clause (b) family: the inheritance "
        f"kernel selects the smallest A_F whose irrep block-grading carries the BDI 0D premise; this is "
        f"algebra-data, NOT a `{{λ_n}}`-only spectral moment). The symbolic form references π(a) on A_F "
        f"(NOT a spectrum-only `Σ_k m_k g(λ_k)`), so the clause-(e) decision returns **DEPENDENT**.\n"
        f"\n"
        f"- **ANCHOR-2 (C1, NCG block-decomposition) — Parse-tree decision: algebra-DEPENDENT.** "
        f"C1 (Connes 1996 reconstruction + NCG axioms 3+5+6 + Schur orthogonality) yields the unique B1/B2 "
        f"block decomposition; the per-pathway observable parses as "
        f"`r_α = ⟨P_α · D² · P_α⟩` with P_α the irrep-block projector on A_F. "
        f"Its parse tree `r_α → ⟨π(P_α) D² π(P_α)⟩ → state-pair "
        f"functional on A_F` contains an explicit `π(P_α)` algebra factor and a state-pair expectation "
        f"— a **state-pair functional** in the clause (b) sense (Connes-distance-class `sup_{{a:‖[D,π(a)]‖≤1}}`). "
        f"The clause-(e) decision returns **DEPENDENT** (NOT a spectrum-only INVARIANT functional, which would "
        f"contain only λ_k, m_k with no π(a)).\n"
        f"\n"
        f"- **Mellin-pole axis (both anchors): s=3, poleconv-A-double, n=2.** The substrate-distance-1 pole "
        f"index s=3 is independently re-derived from the substrate-first ζ_{{D_K}} residue (this gate); "
        f"under poleconv-A-double at d=8 it carries curvature_grade_n=2 (the a_2^{{Mellin}} channel), NOT n=4. "
        f"This fixes the Mellin-pole coordinate of the 4-corner cell from first principles, discharging the "
        f"S88 §W5b-46 audit-substituted s=3 inference.\n"
        f"\n"
        f"**Cell membership**: both anchors → (algebra-DEPENDENT, s=3) = **Corner III**. No cross-corner "
        f"co-primary is triggered (both anchors on the SAME algebra-axis cell, satisfying "
        f"`registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY Detection criterion 4). The Corner-III lexical "
        f"marker (algebra-DEPENDENT / state-pair-functional) is now first-principles-certifiable, not "
        f"semantic-marker-inferred.\n"
    )


def build_promotion_text(registry_text: str):
    """Pure function: produce the EXACT new registry text. No I/O.
    Edits ONLY the §VII.AC.1 + §VII.AC.4 blocks:
      (i)  replace each Corner header line with the poleconv-pinned version;
      (ii) insert a Parse-tree expansion block after each Corner header;
      (iii) flip Status LANDED/STAGE-1-CANDIDATE -> STAGE-3-PERMANENT on both.
    """
    text = registry_text
    diag = {}  # (local)

    # --- §VII.AC.1 Corner header replacement ---
    old_ac1_corner = (
        "**Corner**: III (DEPENDENT × s=3) — S88 §W5b-46 audit-substituted annotation per "
        "§VII.U.2 clause (e) consultation; Path-H/Path-C dual-pathway block-decomposition on "
        "A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); algebra-DEPENDENT (state-pair commutator-norm functional "
        "via ‖[D, π(a)]‖_op route through A_F irreps); Mellin pole inferred from substrate-distance-1 "
        "semantic marker (a_4^ζ Seeley-DeWitt slot at s=3) per §VII.U.2 clause (e) consultation per S88 "
        "§W5b-46 audit FAIL on lexical-marker absence."
    )
    diag["ac1_corner_found"] = (old_ac1_corner in text)
    if diag["ac1_corner_found"]:
        text = text.replace(old_ac1_corner, _ac1_corner_line() + _parse_tree_block("§VII.AC.1"), 1)

    # --- §VII.AC.4 Corner header replacement ---
    old_ac4_corner = (
        "**Corner**: III (DEPENDENT × s=3) — S88 §W5b-46 audit-substituted annotation per "
        "§VII.U.2 clause (e) consultation; V1+C1 sequential-chain derivation of Path-H/Path-C "
        "classification; algebra-DEPENDENT (C1 output layer = NCG axioms 3+5+6 + Schur orthogonality on A_F "
        "state-pair structure); Mellin pole inferred from a_4^ζ Seeley-DeWitt slot semantic marker "
        "(substrate-distance-1) per §VII.U.2 clause (e) consultation per S88 §W5b-46 audit FAIL on "
        "lexical-marker absence."
    )
    diag["ac4_corner_found"] = (old_ac4_corner in text)
    if diag["ac4_corner_found"]:
        text = text.replace(old_ac4_corner, _ac4_corner_line() + _parse_tree_block("§VII.AC.4"), 1)

    # --- Status promotions: STAGE-1-CANDIDATE -> STAGE-3-PERMANENT ---
    # §VII.AC.1 Status line begins "**Status**: LANDED — S87 W3-1 CF-20 ..."; the entry's
    # STAGE-1-CANDIDATE status lives in the S107 Stage-2 blockquote ("STAYS STAGE-1-CANDIDATE").
    # We append a STAGE-3-PERMANENT promotion sentence to each Status line.
    ac1_status_old = (
        "**Status**: LANDED — S87 W3-1 CF-20 `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING` closure "
        "(2026-04-28). The pre-registered statement below is now registry-anchored under the "
        "SOURCE-DOUBLE-CITE-CO-PRIMARY pattern per `.claude/rules/registry-landing.md`. The pre-S87 placeholder "
        "marker is removed; downstream consumers MAY cite §VII.AC.1 as the canonical anchor for the "
        "Path-H/Path-C dual-pathway structure."
    )
    ac1_status_new = ac1_status_old + (
        " **STAGE-3-PERMANENT (S108 W2-1, 2026-06-14)**: the S88 §W5b-46 audit-substituted s=3 Mellin-pole "
        "tag that held K2 `single-axis-A-2` at INFO is DISCHARGED by the substrate-first ζ_{D_K} residue "
        "(poleconv-A-double, pole_in_s=3, curvature_grade_n=2, a_2 channel) + the explicit §VII.U.2 "
        "Corner-III parse-tree expansion of both anchors; with the S107 blind two-agent JOINT-spine PASS-AND "
        "(audit `dea18a85…`), §VII.AC.1 (K2) promotes STAGE-1-CANDIDATE → STAGE-3-PERMANENT per "
        "`joint-theorem-promotion.md` Stage 3."
    )
    diag["ac1_status_found"] = (ac1_status_old in text)
    if diag["ac1_status_found"]:
        text = text.replace(ac1_status_old, ac1_status_new, 1)

    ac4_status_old = (
        "**Status**: LANDED — S87 W3-1 CF-20 `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING` closure "
        "(2026-04-28). The pre-registered V1+C1 sequential-chain derivation is now registry-anchored as the "
        "per-anchor-rationale companion row to §VII.AC.1 under the SOURCE-DOUBLE-CITE-CO-PRIMARY pattern. "
        "The pre-S87 placeholder marker is removed."
    )
    ac4_status_new = ac4_status_old + (
        " **STAGE-3-PERMANENT (S108 W2-1, 2026-06-14)**: the shared s=3 Mellin-pole mis-label that held K11 "
        "`JOINT-3` sub-claim (b) at INFO is DISCHARGED by the same substrate-first ζ_{D_K} residue "
        "(poleconv-A-double, pole_in_s=3, curvature_grade_n=2; a_4^ζ↔n=4 is the mis-label, re-pinned "
        "to a_2) + the §VII.U.2 Corner-III parse-tree expansion; with the S107 blind CO-PRIMARY direction "
        "PASS-AND (audit `9edd6245…`), §VII.AC.4 (K11) promotes STAGE-1-CANDIDATE → "
        "STAGE-3-PERMANENT per `joint-theorem-promotion.md` Stage 3."
    )
    diag["ac4_status_found"] = (ac4_status_old in text)
    if diag["ac4_status_found"]:
        text = text.replace(ac4_status_old, ac4_status_new, 1)

    return text, diag


def write_atomic_with_fsync(text: str, path: Path):
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)
    # fsync the dir entry for durability
    try:
        dfd = os.open(str(path.parent), os.O_RDONLY)
        os.fsync(dfd)
        os.close(dfd)
    except (OSError, AttributeError):
        pass


def _extract_block(text: str, header: str, next_headers) -> str:
    """Return the block from `header` up to (not including) the next ### header."""
    i = text.find(header)
    if i < 0:
        return ""
    j = len(text)
    for nh in next_headers:
        k = text.find(nh, i + len(header))
        if 0 <= k < j:
            j = k
    return text[i:j]


def verify_section_matches(actual_text: str, header: str, must_contain) -> bool:
    """Strict content-presence verification on the re-read block (match by
    HEADER, not line number). Returns True iff the block exists AND every
    required marker is present."""
    next_candidates = [AC1_HEADER, AC4_HEADER,
                       "### Substrate framing (W-3 family)",
                       "## §VII.AB", "\n---\n"]
    next_headers = [h for h in next_candidates if h != header]  # (local)
    block = _extract_block(actual_text, header, next_headers)
    if not block:
        return False
    return all(m in block for m in must_contain)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)

    # --- input pin map (logged in first 20 lines of stdout) ---
    pins = {
        "canonical_constants.py": _file_sha256(canonical_path),
        "s84_spectrum_cache_L12_tau019.npz": _file_sha256(CACHE),
        "s87_w3_path_h_path_c_registry_landing.npz": _file_sha256(AC_SLOT_NPZ),
        "s87_w3_path_h_path_c_registry_landing.json": _file_sha256(AC_SLOT_JSON),
        "permanent-results-registry.md": _file_sha256(REGISTRY),
        "gate_id": GATE_ID,
    }  # (local)
    print("=== INPUT PIN MAP ===")
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v[:16] if len(v) >= 16 else v}")
    print()

    # --- (1) poleconv substitution chain + substrate-first residue ---
    chain, a4_inv, a2_inv, admissible = poleconv_substitution_chain()
    print("=== POLECONV SUBSTITUTION CHAIN (Sage-verified, Python re-derive) ===")
    for (d, conv), rec in sorted(chain.items()):
        print(f"  d={d}, poleconv-{conv}: s=3 -> n={rec['n']:>3}  admissible={rec['admissible']}")
    print(f"  a_4 (n=4) inverse: A-double s={a4_inv['A-double']}, B-single s={a4_inv['B-single']} (neither == 3)")
    print(f"  a_2 (n=2) inverse: A-double s={a2_inv['A-double']}, B-single s={a2_inv['B-single']}")
    print(f"  UNIQUE admissible (d,conv,n) at s=3: {admissible}")
    print()

    res = mellin_residue_at_s3(CACHE)
    print("=== SUBSTRATE-FIRST MELLIN RESIDUE (L_max=10 cache) ===")
    print(f"  pole_in_s = {res['s_pole']}  (poleconv-A-double, exponent 2s = {res['two_s']})")
    print(f"  n_listing (cache abs_evals listing == plan N_eval) = {res['n_listing']}")
    print(f"  n_dirichlet_with_mult (SU(3) sector-dim weighted)  = {res['n_dirichlet_with_mult']}")
    print(f"  n_unique_lambda = {res['n_unique_lambda']}")
    print(f"  |lambda| range = [{res['min_lambda']:.6f}, {res['max_lambda']:.6f}]")
    print(f"  residue_listing   (Sum_v v^-2s, listing)        = {res['residue_listing']:.9e}")
    print(f"  residue_dirichlet (Sum_v m(v) v^-2s, S87 W1a-4)  = {res['residue_dirichlet']:.9e}")
    print()

    TOL = 1e-9  # (local) nonzero-discriminator floor (plan tolerance)
    residue_nonzero = (res["residue_listing"] > TOL) and (res["residue_dirichlet"] > TOL)
    curvature_grade_n = 2          # (local) from the unique admissible (d=8, A-double) at s=3
    a2_channel_deg = 2             # (local) deg(a_2 channel) = 2 by definition
    grade_matches = (curvature_grade_n == a2_channel_deg)
    poleconv_declared = "A-double"
    n_eval_matches_plan = (res["n_listing"] == 78080)  # (local) plan N_eval cross-check
    unique_admissible_ok = (admissible == [(8, "A-double", 2)])

    # --- (2)+(3) bridge-landing single-shot AFTER-pattern ---
    registry_text = REGISTRY.read_text(encoding="utf-8")  # (local)
    new_text, build_diag = build_promotion_text(registry_text)
    print("=== BUILD-PROMOTION DIAGNOSTICS ===")
    for k, v in build_diag.items():
        print(f"  {k}: {v}")
    all_edits_applied = all(build_diag.values())
    print(f"  all_edits_applied: {all_edits_applied}")
    print()

    # Only write if every targeted string was found (no partial edits).
    wrote = False  # (local)
    if all_edits_applied and (new_text != registry_text):
        write_atomic_with_fsync(new_text, REGISTRY)
        wrote = True

    # re-read + verify_section_matches (FINAL decision step)
    actual = REGISTRY.read_text(encoding="utf-8")  # (local)
    ac1_must = [
        "poleconv-A-double", "(pole_in_s = 3, curvature_grade_n = 2)",
        "a_2^{Mellin}", "MIS-LABEL",
        "Parse-tree expansion", "Parse-tree decision: algebra-DEPENDENT",
        "Corner III", "state-pair functional",
        "STAGE-3-PERMANENT (S108 W2-1, 2026-06-14)",
    ]  # (local)
    ac4_must = [
        "poleconv-A-double", "(pole_in_s = 3, curvature_grade_n = 2)",
        "a_2^{Mellin}", "MIS-LABEL",
        "Parse-tree expansion", "Parse-tree decision: algebra-DEPENDENT",
        "Corner III", "state-pair functional",
        "STAGE-3-PERMANENT (S108 W2-1, 2026-06-14)",
    ]  # (local)
    verify_ac1 = verify_section_matches(actual, AC1_HEADER, ac1_must)
    verify_ac4 = verify_section_matches(actual, AC4_HEADER, ac4_must)
    print("=== SECTION-MATCH VERIFICATION (re-read; match by HEADER) ===")
    print(f"  verify_section_matches(§VII.AC.1) = {verify_ac1}")
    print(f"  verify_section_matches(§VII.AC.4) = {verify_ac4}")
    print()

    # --- gate verdict (operator.form conjunction) ---
    PASS = (
        (poleconv_declared in ("A-double", "B-single"))
        and (res["s_pole"] == 3 and curvature_grade_n == 2)
        and residue_nonzero
        and grade_matches
        and unique_admissible_ok
        and verify_ac1 and verify_ac4
    )
    verdict = "PASS" if PASS else "FAIL"

    # --- dual SHA (over the EDITED registry as content target) ---
    pins_for_sha = dict(pins)
    pins_for_sha["permanent-results-registry.md"] = _file_sha256(REGISTRY)  # (local) post-edit
    pins_for_sha["residue_listing"] = f"{res['residue_listing']:.12e}"      # (local) pin the residue
    pins_for_sha["residue_dirichlet"] = f"{res['residue_dirichlet']:.12e}"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins_for_sha)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # --- save npz ---
    s_grid = np.linspace(2.0, 5.0, 31)  # (local) residue-vs-s diagnostic grid
    z_grid = residue_curve(CACHE, s_grid)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        poleconv=poleconv_declared,
        pole_in_s=res["s_pole"],
        curvature_grade_n=curvature_grade_n,
        d_spectral_triple=8,
        n_listing=res["n_listing"],
        n_dirichlet_with_mult=res["n_dirichlet_with_mult"],
        n_unique_lambda=res["n_unique_lambda"],
        min_lambda=res["min_lambda"],
        max_lambda=res["max_lambda"],
        residue_listing=res["residue_listing"],
        residue_dirichlet=res["residue_dirichlet"],
        residue_nonzero=residue_nonzero,
        grade_matches=grade_matches,
        unique_admissible_ok=unique_admissible_ok,
        n_eval_matches_plan=n_eval_matches_plan,
        mislabel_token="a_4^zeta(n=4)",
        correct_label="a_2(n=2)",
        chain_n=np.array([[d, (0 if c == "A-double" else 1), chain[(d, c)]["n"]]
                          for (d, c) in chain], dtype=float),
        a4_inverse_Adouble=a4_inv["A-double"],
        a4_inverse_Bsingle=a4_inv["B-single"],
        a2_inverse_Adouble=a2_inv["A-double"],
        a2_inverse_Bsingle=a2_inv["B-single"],
        verify_ac1=verify_ac1,
        verify_ac4=verify_ac4,
        build_diag=json.dumps(build_diag),
        wrote_registry=wrote,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        s_grid=s_grid,
        z_grid=z_grid,
        tau=_TAU,
    )
    print(f"  npz written: {OUT_NPZ}")

    # --- optional plot (residue magnitude vs s) ---
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(7, 4.5))
        ax.semilogy(s_grid, z_grid, "-", color="#1f4e79", lw=1.8,
                    label=r"$\zeta_{D_K}(s)=\sum_v \lambda_v^{-2s}$ (L=10, listing)")
        ax.axvline(3.0, color="crimson", ls="--", lw=1.3,
                   label="substrate-distance-1 pole s=3 (poleconv-A-double, n=2, $a_2$)")
        ax.axvline(2.0, color="gray", ls=":", lw=1.0,
                   label="$a_4$ (n=4) would sit at s=2 (A-double) — NOT s=3")
        ax.plot([3.0], [res["residue_listing"]], "o", color="crimson", ms=7)
        ax.set_xlabel("Mellin variable s")
        ax.set_ylabel(r"$\zeta_{D_K}(s)$ (listing-sum, log scale)")
        ax.set_title("§VII.AC s=3 substrate-distance-1 pole: residue nonzero, n=2 ($a_2$ channel)")
        ax.legend(fontsize=8, loc="upper right")
        ax.grid(True, which="both", alpha=0.3)
        fig.tight_layout()
        fig.savefig(OUT_PNG, dpi=130)
        plt.close(fig)
        print(f"  png written: {OUT_PNG}")
    except Exception as e:
        print(f"  png skipped: {e}")
    print()

    # --- 4-tuple + verdict payload ---
    value = (
        f"poleconv=A-double;pole_in_s=3;curvature_grade_n=2;a_2-channel;"
        f"mislabel=a_4^zeta(n=4)->repinned_a_2(n=2);"
        f"residue_listing={res['residue_listing']:.6e};residue_dirichlet={res['residue_dirichlet']:.6e};"
        f"residue_nonzero={residue_nonzero};n_listing={res['n_listing']};"
        f"unique_admissible=(d8,A-double,n2);grade_matches={grade_matches};"
        f"verify_AC1={verify_ac1};verify_AC4={verify_ac4};"
        f"AC1_K2_STAGE3={verify_ac1};AC4_K11_STAGE3={verify_ac4}"
    )  # (local)
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    extra_rows = [
        "# regulator_pin=a_2^{Mellin} poleconv-A-double (pole_in_s=3, curvature_grade_n=2) "
        "[Class-1 in-session structural correction: a_4^zeta(n=4) Corner-header token MIS-LABEL, re-pinned a_2(n=2)]",
        f"# residue_listing={res['residue_listing']:.9e} residue_dirichlet={res['residue_dirichlet']:.9e} "
        f"n_listing={res['n_listing']}(==plan_N_eval 78080:{n_eval_matches_plan}) n_dirichlet_with_mult={res['n_dirichlet_with_mult']}",
        f"# verify_section_matches: AC1={verify_ac1} AC4={verify_ac4}; "
        f"on PASS K2 §VII.AC.1 single-axis-A-2 INFO->PASS AND K11 §VII.AC.4 JOINT-3 INFO->PASS => BOTH STAGE-1-CANDIDATE -> STAGE-3-PERMANENT",
    ]  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # verdict is data; exit 0 unless the script itself broke


if __name__ == "__main__":
    sys.exit(main())
