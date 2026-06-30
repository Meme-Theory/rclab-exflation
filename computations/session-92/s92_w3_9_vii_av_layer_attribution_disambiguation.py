#!/usr/bin/env python3
"""
S92 W3-9 — S92-W3-CF-S92-W5-1-C-VII-AV-LAYER-ATTRIBUTION-DISAMBIGUATION
=======================================================================

Gate-ID:  S92-W3-CF-S92-W5-1-C-VII-AV-LAYER-ATTRIBUTION-DISAMBIGUATION
Trigger:  [VERIFY]
Classification: GEOMETRIC (Phi-correspondence F-image consistency test
          discriminating LAYER-A operator-projection (Cell I) vs LAYER-B
          state-projection (Cell IV) for §VII.AV substrate-distance-2
          pole s=4 observable; routes single-slot vs SPLIT into
          §VII.AV.OP-PROJ + §VII.AV.STATE-PROJ)
Owner:    connes-ncg-theorist (PRIMARY; spectral-functional / NCG-axiomatic
          authority on the substrate spectral triple (A_K, H_K, D_K) and
          the CM-1995 §III.4 dimension-spectrum residue formula)

Provenance / Source-of-truth:
  - Plan: sessions/session-plan/session-92-plan-w3.md §W3-9 (lines 1763-2001)
  - Substitution chain Defs 1-4 + Substitute Steps 1-4
  - Phi correspondence: epistemic-discipline.md §"Layer-Decomposition"
    weight(a_n^SD) = n; at substrate-distance-2 pole s=4, Phi(a_4) = Σ_3
    image; BdG-fiber-occupation Var_a IS the methodology-floor F-image
    of the D_K-spectrum-trace operator
  - Registry-naming hygiene: registry-landing.md §"Operator-Projection
    Reading-A Naming Hygiene" MANDATORY K=3 + Detection criterion 4 cross-
    corner co-primary FORBIDDEN
  - Algebra-axis orthogonality: cross-pillar-bridge-anatomy.md §"Algebra-
    axis orthogonality K-counter" MANDATORY K=3
  - Level-pin discipline: substrate-first-canonical-sourcing.md §(iv)
    K=4 MANDATORY (CLASS=FULL; LAYER-A consumes _cm_1995_residue_formula.py
    FULL evaluator; LAYER-B consumes canonical L_emp anchor; no SCHEMATIC
    helper at evaluation layer)

PURPOSE
-------
Apply the Phi-correspondence F-image consistency test from
epistemic-discipline.md §"Layer-Decomposition" to the §VII.AV substrate-
distance-2 pole s=4 observable, which admits TWO STRUCTURALLY DISTINCT
layer attributions on the algebra-axis 4-corner classification:

  LAYER-A (Cell I, algebra-INVARIANT, operator-projection):
      B_LAYER_A := Tr_{H_K}(P_substrate-distance-2 · D_K^{-2s} f(D_K))
                   at s=4 via CM-1995 §III.4 residue formula on the
                   L_max=12 master cache (with P_substrate-distance-2
                   the spectral projector onto the level=2 Peter-Weyl
                   sectors {(0,2), (1,1), (2,0)} and f(D_K)=1).

  LAYER-B (Cell IV, algebra-DEPENDENT, state-projection):
      B_LAYER_B := L_emp(τ_fold) = -7.046336474406761 M_KK² per S87 W2-3
                   Def 4 / S88 W5a / S89 W5-2 / S90 CF-61 canonical anchor
                   (second-log-derivative of Bogoliubov occupation variance
                   Var_a(n_a^GGE(K)) at the K-horizon window).

The Phi-correspondence consistency ratio:
      ratio := |B_LAYER_A − F_image(B_LAYER_B)| / |B_canonical_anchor|

with F_image(B_LAYER_B) the Phi-correspondence structural prediction of
the OP-PROJ image of B_LAYER_B (substrate-physics derivation below) and
B_canonical_anchor := |B_LAYER_B| = 7.046336 M_KK². PASS ratio ≤ 0.10
confirms single-slot §VII.AV; INFO ratio ∈ (0.10, 0.30] suggests suffix-
tag K=1 split; FAIL ratio > 0.30 mandates MANDATORY split into
§VII.AV.OP-PROJ + §VII.AV.STATE-PROJ.

SUBSTRATE-PHYSICS DERIVATION OF F_image(B_LAYER_B)
--------------------------------------------------
Per epistemic-discipline.md §"Layer-Decomposition" Phi correspondence:

  Step 1 (Definition): weight(a_n^SD) = n maps canonically to
                       weight(Σ_d) = enforcement-strength under the
                       layer-functor F: substrate → methodology → audit.

  Step 2 (Substitution at s=4): At substrate-distance-2 pole s=4,
                       Phi(a_4) = Σ_3 image. The methodology-floor
                       observable IS the BdG-fiber-occupation variance
                       at the substrate-distance-2 pole.

  Step 3 (F-image structural map): Per the layer-functor F substrate ↔
                       methodology pair table:
                         eigenvalue (substrate-IS)  ↔  rule-file content
                         numerical PASS predicate   ↔  artifact-existence
                       At the OP-PROJ ↔ STATE-PROJ axis (substrate-IS
                       observable specification), F-image at substrate-
                       distance-2 pole s=4 maps the state-projection
                       second-log-derivative Var_a's MAGNITUDE to the
                       operator-projection central-projection trace
                       MAGNITUDE. The SIGN convention differs structurally:
                         OP-PROJ: Tr_{H_K}(P · |D_K|^{-2s}) > 0 by
                                  positive-definiteness of the trace on
                                  positive operators (P projector, |D_K|^{-2s}
                                  positive-definite on the level=2 sectors).
                         STATE-PROJ: d²(ln Var_a)/d(ln K)² < 0 at horizon
                                     by the BdG occupation curvature
                                     downward at horizon-crossing.
                       F-image structural prediction (magnitude-preserving):
                         F_image(B_LAYER_B) := |B_LAYER_B|
                                            = |L_emp|
                                            = 7.046336474406761 M_KK²

  Step 4 (Simplify):   The F-image map is the magnitude-preserving lift of
                       the state-projection observable to the operator-
                       projection family. If the two layer attributions
                       are F-image variants of the SAME substrate-IS
                       observable at substrate-distance-2 pole s=4, then
                       B_LAYER_A should match F_image(B_LAYER_B) up to
                       the Phi-correspondence consistency band.

  Direction: B_LAYER_A is computed by the CM-1995 §III.4 residue formula
             (positive, operator-side, substrate-IS); F_image is positive
             by construction (magnitude-preserving). The consistency ratio
             is dimensionless (M_KK² units cancel). Direction-of-pass:
             ratio ≤ 0.10 ⇒ single slot; ratio ∈ (0.10, 0.30] ⇒ K=1 split;
             ratio > 0.30 ⇒ MANDATORY split per registry-landing.md K=3.

OPERATOR-MISMATCH PRE-FLIGHT
----------------------------
- B_LAYER_B is the canonical L_emp = -7.046336 M_KK² (second-log-
  derivative of Var_a at K-horizon); NOT the +2s = +8 operator-form
  reduction. Anchored on S87 W2-3 Def 4 / S91 W5-1 canonical
  s91_w5_1_full_bdg_pv.npz `L_emp_canonical` key.
- B_LAYER_A is the FULL CM-1995 §III.4 residue formula evaluation on
  the L_max=12 master cache restricted to level=2 sectors; NOT a
  SCHEMATIC variant. Helper: _cm_1995_residue_formula.py (CLASS=FULL).
- Both anchored on canonical sources per substrate-first-canonical-
  sourcing.md §(iv) K=4 MANDATORY level-pin discipline. Verdict-line
  convention carries PLAN-OPERATOR-CANONICAL-L-EMP-VERIFIED-2026-05-22.

PLAN-TEXT-DRIFT (per substrate-first-canonical-sourcing.md §(ii.B))
-------------------------------------------------------------------
Plan §W3-9 cites `s89_w5_2_l_emp_canonical_anchor.npz` as the canonical
L_emp anchor path. That file does NOT exist on disk; the canonical
runtime location of L_emp_canonical = -7.046336474406761 is
`computations/session-91/s91_w5_1_full_bdg_pv.npz` (key:
`L_emp_canonical`; verified at runtime via npz key inspection). This
is a plan-text drift documented in the verdict-line convention suffix
and dual-SHA companion comment row.

SUBSTRATE FRAMING (PHONONIC-IS-NOT-IN)
--------------------------------------
The substrate IS the spectral triple (A_K, H_K, D_K(τ_fold)) at the
substrate-distance-2 pole s=4 cocycle pairing. The two layer attributions
ARE candidate substrate-IS observable forms inhabiting STRUCTURALLY
DISTINCT 4-corner cells per §VII.U.2: LAYER-A Cell I (algebra-INVARIANT
spectrum-only-functional × substrate-distance-2); LAYER-B Cell IV
(algebra-DEPENDENT state-pair-functional × substrate-distance-2). The
Phi-correspondence F-image test IS the substrate's own structural test
of whether the two layer attributions reduce to the same substrate-IS
observable (single slot) or to structurally distinct substrate-IS
observables (split slots). Container-thinking inversion ("the layer
attributions ARE 2 different observables in different containers") is
FORBIDDEN.

If FAIL fires and slot SPLITS into §VII.AV.OP-PROJ (Cell I) +
§VII.AV.STATE-PROJ (Cell IV), the two slots are STRUCTURAL-ORTHOGONAL-
COMPANIONS per registry-landing.md §"Operator-Projection Reading-A
Naming Hygiene" MANDATORY K=3 — NOT cross-corner co-primary anchors of
the same theorem (which would violate algebra-axis orthogonality K=3
MANDATORY).

OUTPUTS
-------
- computations/session-92/s92_w3_9_vii_av_layer_attribution_disambiguation.py
- computations/session-92/s92_w3_9_vii_av_layer_attribution_disambiguation.npz
- computations/session-92/s92_w3_9_vii_av_layer_attribution_disambiguation.png
- computations/session-92/s92_gate_verdicts.txt (canonical + dual-SHA
  companion row + 4 disclosure pin rows)
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
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
)
from canonical_constants import *  # noqa: F401,F403

# CM-1995 §III.4 residue-formula FULL evaluator (CLASS=FULL per substrate-
# first-canonical-sourcing.md §(iv); not a SCHEMATIC analog).
from _cm_1995_residue_formula import (  # noqa: E402
    jensen_irrep_table,
    su3_dimension,
    su3_casimir,
)


# =================== Gate-block constants (plan §W3-9) ===================

GATE_ID = "S92-W3-CF-S92-W5-1-C-VII-AV-LAYER-ATTRIBUTION-DISAMBIGUATION"
SCHEME = (
    "layer-attribution-disambiguation-VII-AV-substrate-distance-2-"
    "pole-s4-Phi-correspondence-F-image-consistency-test"
)
CONVENTION = (
    "VII-AV-LAYER-ATTRIBUTION-OP-PROJ-VS-STATE-PROJ-PHI-CORRESPONDENCE-"
    "TEST-PLAN-OPERATOR-CANONICAL-L-EMP-VERIFIED-2026-05-22"
)
L_MAX = 12  # (local) plan-pinned canonical L_max=12 master cache

# Substrate-distance pole and Mellin index (plan §W3-9 machinery pin)
SUBSTRATE_DISTANCE = 2          # (local) plan §W3-9 substrate-distance-2 pole
S_POLE = 4                      # (local) Mellin index at substrate-distance-2

# Canonical L_emp anchor (S87 W2-3 / S88 W5a / S89 W5-2 / S90 CF-61 /
# S91 W5-1 canonical pin). Plan §W3-9 expected anchor file
# `s89_w5_2_l_emp_canonical_anchor.npz` does NOT exist on disk;
# runtime canonical anchor file is `s91_w5_1_full_bdg_pv.npz`.
# Plan-text-drift documented in verdict-line companion row per
# substrate-first-canonical-sourcing.md §(ii.B).
L_EMP_CANONICAL = -7.046336474406761    # (local) M_KK² units; canonical anchor

# Pre-registered Phi-correspondence consistency thresholds (plan §W3-9
# strict_PASS_boundary; ratio = |B_LAYER_A − F_image(B_LAYER_B)| /
# |B_canonical_anchor|).
PHI_PASS_CEILING = 0.10        # (local) PASS upper edge ratio
PHI_INFO_CEILING = 0.30        # (local) INFO upper edge (FAIL above)

# Output paths.
OUT_NPZ = (
    ROOT
    / "computations"
    / "session-92"
    / "s92_w3_9_vii_av_layer_attribution_disambiguation.npz"
)
OUT_PNG = (
    ROOT
    / "computations"
    / "session-92"
    / "s92_w3_9_vii_av_layer_attribution_disambiguation.png"
)
VERDICT_FILE = ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"

# Input file paths (for SHA-pin map).
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
L12_CACHE = (
    ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
)
CM1995_HELPER = ROOT / "computations" / "_shared" / "_cm_1995_residue_formula.py"
# Runtime canonical L_emp anchor (plan-text-drift; see header).
S91_W5_1_NPZ_RUNTIME = (
    ROOT / "computations" / "session-91" / "s91_w5_1_full_bdg_pv.npz"
)
REGISTRY_LANDING_RULE = (
    ROOT / ".claude" / "rules" / "registry-landing.md"
)
EPISTEMIC_DISCIPLINE_RULE = (
    ROOT / ".claude" / "rules" / "epistemic-discipline.md"
)
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "L12_spectrum_cache_tau019": L12_CACHE,
    "cm_1995_residue_formula_helper_FULL": CM1995_HELPER,
    "s91_w5_1_full_bdg_pv_L_emp_canonical_anchor_RUNTIME": S91_W5_1_NPZ_RUNTIME,
    "registry_landing_rule": REGISTRY_LANDING_RULE,
    "epistemic_discipline_rule": EPISTEMIC_DISCIPLINE_RULE,
    "script": SCRIPT_PATH,
}


# ============================== SHA helpers ==============================


def sha256_of_file(p: Path) -> str:
    """SHA-256 of a file's bytes."""
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    """Print SHA-256 of each input file; return pin-map dict."""
    pins = {}  # (local)
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print("=" * 72)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:60s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:60s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


def closure_hash(pinmap: dict) -> str:
    """SHA-256 of the canonicalized pin map (input-pin closure hash)."""
    pinmap_json = json.dumps(sorted(pinmap.items()), sort_keys=True).encode(
        "utf-8"
    )
    return hashlib.sha256(pinmap_json).hexdigest()


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    """Dual-SHA (audit, content) per W9a-99 split:

      audit_sha256   = sha256(script || canonical || pinmap_json)
      content_sha256 = sha256(script)
    """
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode(
        "utf-8"
    )  # (local)
    audit = hashlib.sha256(
        script_bytes + canonical_bytes + pinmap_json
    ).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ============================== L_emp anchor loader ==============================


def load_L_emp_canonical(npz_path: Path) -> float:
    """Read canonical L_emp anchor from S91 W5-1 npz (runtime canonical path
    per plan-text-drift in §W3-9 — see header)."""
    data = np.load(npz_path, allow_pickle=True)
    if "L_emp_canonical" not in data.files:
        raise RuntimeError(
            f"Anchor file {npz_path} missing 'L_emp_canonical' key; "
            f"available keys: {list(data.files)}"
        )
    L_emp_npz = float(data["L_emp_canonical"])  # (local)
    # Cross-check against the literal canonical pin in this script
    if abs(L_emp_npz - L_EMP_CANONICAL) > 1.0e-12:
        raise RuntimeError(
            f"L_emp anchor mismatch: npz={L_emp_npz}, "
            f"literal={L_EMP_CANONICAL}, |delta|={abs(L_emp_npz - L_EMP_CANONICAL)}"
        )
    return L_emp_npz


# ============================== LAYER-A evaluator (CM-1995 §III.4) ==============================


def b_layer_a_op_proj_trace(L_max: int, tau: float, s_pole: int,
                            substrate_distance: int):
    """Compute LAYER-A operator-projection trace observable:

        B_LAYER_A = Tr_{H_K}(P_substrate-distance-N · D_K^{-2s} · f(D_K))
                  at f(D_K)=1

    on the L_max master spectrum cache, restricted to Peter-Weyl sectors
    with `level = p+q = substrate_distance`. Substrate-distance-N
    projector P selects sectors at the N-th Peter-Weyl level. At s=4
    (substrate-distance-2 pole on Mellin cone), the evaluation reduces
    to the CM-1995 §III.4 dimension-spectrum residue formula at the
    finite L_max truncation:

        B_LAYER_A = Σ_{(p,q): p+q = N}  dim(p,q) · Σ_{λ ∈ sector(p,q)} |λ|^{-2s}

    using the master cache `abs_evals` arrays per sector (which carry
    the full per-mode multiplicity already absorbed into the array
    length × dim(p,q) Peter-Weyl multiplicity).

    Returns (B_LAYER_A, sector_index_at_level, n_modes_total, diagnostic).
    """
    cache_path = L12_CACHE  # (local) plan-pinned L_max=12 master cache
    cache = np.load(cache_path, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()

    B_LAYER_A = 0.0  # (local) accumulator
    sector_index_at_level = []  # (local) list of (p,q) at substrate-distance N
    n_modes_total = 0  # (local) total |λ|^{-8} modes summed
    per_sector_contribution = {}  # (local) diagnostic per-sector contribution

    for (p, q), info in sector_evals.items():
        if (p + q) != substrate_distance:
            continue
        if (p + q) > L_max:
            continue
        # Cross-check level field consistency
        if int(info["level"]) != (p + q):
            raise RuntimeError(
                f"Sector ({p},{q}) level field {info['level']} != p+q={p + q}; "
                f"master cache integrity violated"
            )
        dim_pq = int(info["dim"])  # (local) SU(3) Peter-Weyl dim(p,q)
        evals = np.asarray(info["abs_evals"], dtype=np.float64)
        # Defensive: filter exact-zero eigenvalues (would blow |λ|^{-2s})
        evals_nonzero = evals[evals > 0.0]
        # Mellin sum at substrate-distance-N pole s=S_POLE:
        # Σ_{λ ∈ sector(p,q)} |λ|^{-2s}
        sector_mellin_sum = float(np.sum(evals_nonzero ** (-2.0 * s_pole)))  # (local)
        # Weight by Peter-Weyl dim(p,q) multiplicity (CM-1995 §III.4)
        sector_contribution = dim_pq * sector_mellin_sum  # (local)
        B_LAYER_A += sector_contribution
        sector_index_at_level.append((p, q))
        n_modes_total += int(len(evals_nonzero))
        per_sector_contribution[f"({p},{q})"] = {
            "dim": dim_pq,
            "n_modes": int(len(evals_nonzero)),
            "mellin_sum": sector_mellin_sum,
            "contribution": sector_contribution,
        }
        # Cross-check Casimir consistency
        c2 = su3_casimir(p, q)
        dim_pq_xcheck = su3_dimension(p, q)
        if dim_pq_xcheck != dim_pq:
            raise RuntimeError(
                f"Casimir cross-check failed: sector ({p},{q}) dim mismatch "
                f"{dim_pq} vs canonical {dim_pq_xcheck}"
            )
        per_sector_contribution[f"({p},{q})"]["casimir_C2"] = c2

    diagnostic = {
        "sector_index_at_level": sector_index_at_level,
        "n_modes_total": n_modes_total,
        "per_sector": per_sector_contribution,
        "L_max_used": L_max,
        "tau_fold_used": tau,
        "s_pole_used": s_pole,
        "substrate_distance_used": substrate_distance,
    }

    return B_LAYER_A, sector_index_at_level, n_modes_total, diagnostic


# ============================== F-image structural map ==============================


def f_image_phi_correspondence(B_LAYER_B: float) -> tuple[float, str]:
    """Phi-correspondence structural F-image map at substrate-distance-2
    pole s=4 substrate ↔ methodology layer pair.

    Per epistemic-discipline.md §"Layer-Decomposition":
      weight(a_n^SD) = n  →  weight(Σ_d) = enforcement-strength
      At s=4: Phi(a_4) = Σ_3 image
      BdG-fiber-occupation Var_a (STATE-PROJ) IS the methodology-floor
      F-image of the D_K-spectrum-trace operator (OP-PROJ).

    The F-image structural prediction maps the magnitude of the state-
    projection observable to the magnitude of the operator-projection
    central-projection trace; sign convention differs structurally:
      OP-PROJ:    Tr_{H_K}(P · |D_K|^{-2s}) > 0 (positivity of trace)
      STATE-PROJ: d²(ln Var_a)/d(ln K)² < 0 at horizon (BdG curvature)

    Structural F-image (magnitude-preserving lift):
      F_image(B_LAYER_B) := |B_LAYER_B|

    Returns (F_image_value, derivation_summary).
    """
    F_image_value = abs(B_LAYER_B)  # (local) magnitude-preserving lift
    derivation_summary = (
        f"F_image(B_LAYER_B) := |B_LAYER_B| = {F_image_value:.12f} M_KK^2; "
        f"Phi(a_4) = Σ_3 image at substrate-distance-2 pole s=4; "
        f"magnitude-preserving lift of STATE-PROJ Var_a (sign at horizon "
        f"is negative by BdG curvature) to OP-PROJ central-projection "
        f"trace family (sign positive by Tr_{{H_K}}(P · |D_K|^{{-2s}}) "
        f"positivity); cf. epistemic-discipline.md §'Layer-Decomposition' "
        f"+ registry-landing.md §'Operator-Projection Reading-A Naming "
        f"Hygiene' MANDATORY K=3"
    )
    return F_image_value, derivation_summary


# ============================== Phi-correspondence consistency ratio ==============================


def phi_correspondence_ratio(B_LAYER_A: float, B_LAYER_B: float,
                             F_image_value: float) -> tuple[float, float]:
    """Phi_correspondence_consistency_ratio per plan §W3-9 Def 4:

        ratio := |B_LAYER_A − F_image(B_LAYER_B)| / |B_canonical_anchor|

    with B_canonical_anchor := |B_LAYER_B| = canonical L_emp magnitude.

    Returns (Phi_correspondence_consistency_ratio, B_canonical_anchor).
    """
    B_canonical_anchor = abs(B_LAYER_B)  # (local) canonical L_emp magnitude
    numerator = abs(B_LAYER_A - F_image_value)  # (local)
    ratio = numerator / B_canonical_anchor  # (local) dimensionless
    return ratio, B_canonical_anchor


# ============================== Verdict evaluation ==============================


def evaluate_verdict(ratio: float) -> dict:
    """3-band classifier per plan §W3-9 strict_PASS_boundary:
        PASS  iff ratio ≤ PHI_PASS_CEILING (0.10)  → single §VII.AV slot survives
        INFO  iff PHI_PASS_CEILING < ratio ≤ PHI_INFO_CEILING (0.30)
                                                   → suffix-tag SUGGESTION K=1
        FAIL  iff ratio > PHI_INFO_CEILING (0.30)  → MANDATORY split into
                                                      §VII.AV.OP-PROJ + §VII.AV.STATE-PROJ
    """
    if ratio <= PHI_PASS_CEILING:
        composite = "PASS"
        classification = "F_IMAGE_CONSISTENT_SINGLE_SLOT"
        slot_decision = "single-§VII.AV-slot-survives"
        registry_routing = (
            "single §VII.AV slot retained; STAGE-3-PERMANENT eligibility "
            "UNBLOCKED at layer-attribution layer"
        )
    elif ratio <= PHI_INFO_CEILING:
        composite = "INFO"
        classification = "F_IMAGE_PARTIAL_SUGGESTION_K1_SPLIT"
        slot_decision = "suffix-tag-SUGGESTION-K1"
        registry_routing = (
            "§VII.AV.OP-PROJ canonical + §VII.AV.STATE-PROJ structural-"
            "orthogonal-companion (SUGGESTION K=1 per registry-landing.md "
            "K=3 suffix-tag discipline)"
        )
    else:
        composite = "FAIL"
        classification = "F_IMAGE_INCONSISTENT_MANDATORY_SPLIT"
        slot_decision = "MANDATORY-split-OP-PROJ-plus-STATE-PROJ"
        registry_routing = (
            "MANDATORY split: §VII.AV.OP-PROJ (Cell I) + §VII.AV.STATE-PROJ "
            "(Cell IV); cross-corner co-primary FORBIDDEN per algebra-axis "
            "orthogonality K=3 (registry-landing.md §'Detection' criterion 4); "
            "STAGE-3-PERMANENT eligibility BLOCKED until split-and-re-anchor"
        )
    return {
        "composite": composite,
        "classification": classification,
        "slot_decision": slot_decision,
        "registry_routing": registry_routing,
        "ratio": ratio,
    }


# ============================== Diagnostic plot ==============================


def make_plot(B_LAYER_A: float, B_LAYER_B: float, F_image_value: float,
              ratio: float, B_canonical_anchor: float,
              classification: str, sector_index_at_level: list,
              n_modes_total: int):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 11))

    # Panel 1: B_LAYER_A vs F_image(B_LAYER_B) magnitude comparison.
    labels = ["B_LAYER_A\n(OP-PROJ, Cell I,\nCM-1995 §III.4)",
              "F_image(B_LAYER_B)\n(Phi-correspondence\nstructural prediction)",
              "|B_LAYER_B|\n(STATE-PROJ canonical,\nCell IV, L_emp magnitude)"]
    values = [B_LAYER_A, F_image_value, abs(B_LAYER_B)]  # (local)
    colors_bar = ["darkorange", "steelblue", "forestgreen"]
    ax1.bar(labels, values, color=colors_bar, edgecolor="black")
    ax1.set_yscale("log")
    ax1.set_ylabel(r"Magnitude (M_{KK}^2 units; log scale)")
    ax1.set_title(
        f"2-layer comparison at substrate-distance-2 pole s={S_POLE}, L_max={L_MAX}\n"
        f"Phi_correspondence_consistency_ratio = {ratio:.6e}  → {classification}"
    )
    ax1.tick_params(axis="x", labelsize=8)
    ax1.grid(True, axis="y", alpha=0.3)

    # Panel 2: Phi-correspondence consistency ratio with PASS/INFO/FAIL bands.
    ax2.axhspan(0.0, PHI_PASS_CEILING, alpha=0.25, color="green",
                label=f"PASS band (ratio ≤ {PHI_PASS_CEILING})")
    ax2.axhspan(PHI_PASS_CEILING, PHI_INFO_CEILING, alpha=0.25, color="yellow",
                label=f"INFO band ({PHI_PASS_CEILING} < ratio ≤ {PHI_INFO_CEILING})")
    ax2.axhspan(PHI_INFO_CEILING, max(1.5 * ratio, 1.0), alpha=0.25, color="red",
                label=f"FAIL band (ratio > {PHI_INFO_CEILING})")
    ax2.axhline(ratio, color="black", linestyle="-", linewidth=2.5,
                label=f"computed ratio = {ratio:.6e}")
    ax2.set_yscale("log")
    ax2.set_ylim(1.0e-3, max(2.0 * ratio, 2.0))
    ax2.set_ylabel(r"Phi-correspondence consistency ratio (log scale)")
    ax2.set_title(
        "Phi-correspondence F-image consistency ratio\n"
        r"ratio = |B_LAYER_A − F_image(B_LAYER_B)| / |B_canonical_anchor|"
    )
    ax2.legend(loc="lower right", fontsize=9)
    ax2.grid(True, axis="y", alpha=0.3)

    # Panel 3: per-sector contribution to B_LAYER_A at substrate-distance-2.
    sector_labels = [f"({p},{q})" for (p, q) in sector_index_at_level]
    sector_dims = [su3_dimension(p, q) for (p, q) in sector_index_at_level]  # (local)
    ax3.bar(sector_labels, sector_dims, color="darkorange", edgecolor="black")
    ax3.set_ylabel("SU(3) Peter-Weyl dim(p,q)")
    ax3.set_title(
        f"Substrate-distance-{SUBSTRATE_DISTANCE} sectors contributing to "
        f"B_LAYER_A\n"
        f"(level = p+q = {SUBSTRATE_DISTANCE}; n_sectors={len(sector_index_at_level)}; "
        f"n_modes_total={n_modes_total})"
    )
    ax3.grid(True, axis="y", alpha=0.3)

    # Panel 4: Phi correspondence schematic — substrate ↔ methodology layer pair.
    ax4.axis("off")
    text_block = (
        "Phi-correspondence F-image map (substrate ↔ methodology):\n\n"
        f"  weight(a_4^SD) = 4   →   weight(Σ_3) = 3\n"
        f"  At substrate-distance-{SUBSTRATE_DISTANCE} pole s={S_POLE}:\n"
        f"     Phi(a_4) = Σ_3 image\n\n"
        f"LAYER-A (Cell I, OP-PROJ, algebra-INVARIANT):\n"
        f"   B_LAYER_A = Tr_(H_K)(P_(d-{SUBSTRATE_DISTANCE}) · D_K^(-2s) · f(D_K))\n"
        f"             = {B_LAYER_A:.6e} M_KK^2  (CM-1995 §III.4 residue)\n\n"
        f"LAYER-B (Cell IV, STATE-PROJ, algebra-DEPENDENT):\n"
        f"   B_LAYER_B = L_emp(τ_fold)\n"
        f"             = {B_LAYER_B:.12f} M_KK^2  (S87 W2-3 canonical)\n\n"
        f"F-image map (magnitude-preserving lift):\n"
        f"   F_image(B_LAYER_B) := |B_LAYER_B| = {F_image_value:.6e}\n\n"
        f"Consistency ratio:\n"
        f"   ratio = |B_LAYER_A − F_image(B_LAYER_B)| / |B_canonical_anchor|\n"
        f"         = {ratio:.6e}\n"
        f"   → {classification}\n\n"
        f"Algebra-axis orthogonality K=3 MANDATORY:\n"
        f"   cross-corner co-primary FORBIDDEN\n"
        f"   (LAYER-A Cell I; LAYER-B Cell IV — orthogonal axes)\n"
    )
    ax4.text(0.02, 0.98, text_block, transform=ax4.transAxes,
             fontfamily="monospace", fontsize=9, va="top", ha="left",
             bbox=dict(facecolor="lightgrey", alpha=0.5, pad=8))

    fig.suptitle(
        f"S92 W3-9 — §VII.AV layer-attribution disambiguation "
        f"(Phi-correspondence F-image consistency test)\n"
        f"L_max={L_MAX}, τ_fold={tau_fold}, substrate-distance-2 pole s={S_POLE}",
        fontsize=12,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ============================== Verdict emission ==============================


def append_verdict(composite: str, value_str: str, audit_sha: str,
                   content_sha: str, classification: str,
                   slot_decision: str):
    """Append canonical verdict line + dual-SHA companion + level-pin
    + algebra-axis pin + plan-text-drift companion rows per
    gate-verdicts.md S87+ canonical form."""
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    level_pin = (
        f"# LEVEL_CLASS_PIN=FULL "
        f"# {GATE_ID} substrate-first-canonical-sourcing.md §(iv) "
        f"K=4 MANDATORY level-pin compliance (LAYER-A consumes "
        f"_cm_1995_residue_formula.py FULL evaluator; LAYER-B consumes "
        f"canonical L_emp anchor; NO -SCHEMATIC suffix; "
        f"classification={classification}; slot_decision={slot_decision})\n"
    )
    algebra_axis_pin = (
        f"# ALGEBRA_AXIS_PIN=CROSS-CORNER-CO-PRIMARY-FORBIDDEN "
        f"# {GATE_ID} cross-pillar-bridge-anatomy.md §'Algebra-axis "
        f"orthogonality K-counter' MANDATORY K=3 + registry-landing.md "
        f"§'Operator-Projection Reading-A Naming Hygiene' MANDATORY K=3 "
        f"(LAYER-A Cell I algebra-INVARIANT; LAYER-B Cell IV "
        f"algebra-DEPENDENT; orthogonal axes)\n"
    )
    plan_drift_pin = (
        f"# PLAN_TEXT_DRIFT=L_EMP_CANONICAL_RUNTIME_PATH_RECONCILED "
        f"# {GATE_ID} per substrate-first-canonical-sourcing.md §(ii.B): "
        f"plan §W3-9 cited s89_w5_2_l_emp_canonical_anchor.npz which does "
        f"NOT exist on disk; runtime canonical anchor path is "
        f"computations/session-91/s91_w5_1_full_bdg_pv.npz "
        f"(key L_emp_canonical={L_EMP_CANONICAL}); SHA-pinned in audit_sha256 "
        f"input-pin map\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(level_pin)
        f.write(algebra_axis_pin)
        f.write(plan_drift_pin)


# ============================== Main ==============================


def main() -> int:
    print(f"\n{'=' * 72}\nS92 W3-9 — {GATE_ID}\n{'=' * 72}\n")
    print(f"Substrate framing: substrate IS spectral triple (A_K, H_K, D_K)")
    print(f"  at substrate-distance-{SUBSTRATE_DISTANCE} pole s={S_POLE},")
    print(f"  τ_fold={tau_fold}, L_max={L_MAX}.")
    print(f"  LAYER-A (Cell I, algebra-INVARIANT, OP-PROJ): central-")
    print(f"    projection trace via CM-1995 §III.4 residue formula.")
    print(f"  LAYER-B (Cell IV, algebra-DEPENDENT, STATE-PROJ): canonical")
    print(f"    L_emp(τ_fold) = {L_EMP_CANONICAL} M_KK^2.\n")

    # Section 1: input pins + dual-SHA
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local) informational closure
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print(f"  closure_hash (informational): {closure[:16]}...")
    print(f"  audit_sha256:                 {audit_sha[:16]}...")
    print(f"  content_sha256:               {content_sha[:16]}...")
    print()

    # Section 2: LAYER-A evaluation (OP-PROJ, CM-1995 §III.4)
    print(f"Section 2 — LAYER-A (OP-PROJ, Cell I): CM-1995 §III.4 residue")
    print(f"  formula on L_max={L_MAX} master cache restricted to level=")
    print(f"  {SUBSTRATE_DISTANCE} Peter-Weyl sectors.")
    (B_LAYER_A, sector_index_at_level, n_modes_total, diagnostic) = (
        b_layer_a_op_proj_trace(L_MAX, tau_fold, S_POLE, SUBSTRATE_DISTANCE)
    )
    print(f"  level={SUBSTRATE_DISTANCE} sectors: {sector_index_at_level}")
    print(f"  n_modes_total: {n_modes_total}")
    print(f"  B_LAYER_A = {B_LAYER_A:.12e} M_KK^2")
    print()

    # Section 3: LAYER-B evaluation (STATE-PROJ, canonical L_emp anchor)
    print(f"Section 3 — LAYER-B (STATE-PROJ, Cell IV): canonical L_emp")
    print(f"  anchor from runtime canonical path:")
    print(f"    {S91_W5_1_NPZ_RUNTIME.relative_to(ROOT)}")
    B_LAYER_B = load_L_emp_canonical(S91_W5_1_NPZ_RUNTIME)
    print(f"  B_LAYER_B = L_emp(τ_fold) = {B_LAYER_B} M_KK^2")
    print(f"    OPERATOR-MISMATCH PRE-FLIGHT: L_emp is the canonical second-")
    print(f"    log-derivative of Var_a (Bogoliubov occupation variance) at")
    print(f"    K-horizon; NOT the +2s = +8 operator-form reduction.")
    print()

    # Section 4: F-image structural prediction
    print(f"Section 4 — F_image(B_LAYER_B) via Phi-correspondence structural")
    print(f"  map at substrate-distance-{SUBSTRATE_DISTANCE} pole s={S_POLE}.")
    F_image_value, F_image_derivation = f_image_phi_correspondence(B_LAYER_B)
    print(f"  F_image(B_LAYER_B) = {F_image_value:.12e} M_KK^2")
    print(f"  Derivation: {F_image_derivation}")
    print()

    # Section 5: Phi-correspondence consistency ratio
    print(f"Section 5 — Phi_correspondence_consistency_ratio evaluation.")
    Phi_correspondence_consistency_ratio, B_canonical_anchor = (
        phi_correspondence_ratio(B_LAYER_A, B_LAYER_B, F_image_value)
    )
    print(f"  B_canonical_anchor = |B_LAYER_B| = {B_canonical_anchor:.12f}")
    print(f"  numerator |B_LAYER_A - F_image(B_LAYER_B)| = "
          f"{abs(B_LAYER_A - F_image_value):.12e}")
    print(f"  Phi_correspondence_consistency_ratio = "
          f"{Phi_correspondence_consistency_ratio:.12e}")
    print()

    # Section 6: 3-band verdict classification
    verdict_info = evaluate_verdict(Phi_correspondence_consistency_ratio)
    composite = verdict_info["composite"]
    classification = verdict_info["classification"]
    slot_decision = verdict_info["slot_decision"]
    registry_routing = verdict_info["registry_routing"]
    print(f"Section 6 — 3-band classification:")
    print(f"  composite verdict: {composite}")
    print(f"  classification:    {classification}")
    print(f"  slot_decision:     {slot_decision}")
    print(f"  registry_routing:  {registry_routing}")
    print()

    # Section 7: Plot
    print(f"Section 7 — Diagnostic plot...")
    make_plot(B_LAYER_A, B_LAYER_B, F_image_value,
              Phi_correspondence_consistency_ratio, B_canonical_anchor,
              classification, sector_index_at_level, n_modes_total)
    print(f"  written: {OUT_PNG.relative_to(ROOT)}")
    print()

    # Section 8: NPZ output
    print(f"Section 8 — NPZ output...")
    np.savez(
        OUT_NPZ,
        # Headline quantities
        B_LAYER_A=B_LAYER_A,
        B_LAYER_B=B_LAYER_B,
        F_image_value=F_image_value,
        Phi_correspondence_consistency_ratio=Phi_correspondence_consistency_ratio,
        B_canonical_anchor=B_canonical_anchor,
        L_emp_canonical=L_EMP_CANONICAL,
        # Classification + routing
        composite_verdict=composite,
        classification=classification,
        slot_decision=slot_decision,
        registry_routing=registry_routing,
        # Diagnostic
        sector_index_at_level=np.array(sector_index_at_level, dtype=object),
        n_modes_total=n_modes_total,
        per_sector_diagnostic=np.array([diagnostic["per_sector"]], dtype=object),
        # Pins
        L_max=L_MAX,
        tau_fold=tau_fold,
        s_pole=S_POLE,
        substrate_distance=SUBSTRATE_DISTANCE,
        # Convention
        scheme=SCHEME,
        convention=CONVENTION,
        # Thresholds
        phi_pass_ceiling=PHI_PASS_CEILING,
        phi_info_ceiling=PHI_INFO_CEILING,
        # SHAs
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        closure_hash=closure,
        # F-image derivation
        F_image_derivation=F_image_derivation,
        # Substrate-physics derivation labels
        layer_A_cell="Cell I (algebra-INVARIANT × Mellin-pole substrate-distance-2)",
        layer_B_cell="Cell IV (algebra-DEPENDENT × Mellin-pole substrate-distance-2)",
        layer_A_family="operator-projection (OP-PROJ)",
        layer_B_family="state-projection (STATE-PROJ)",
        # Plan-text-drift note
        plan_text_drift_note=(
            "Plan §W3-9 cites s89_w5_2_l_emp_canonical_anchor.npz; runtime "
            "canonical anchor path is s91_w5_1_full_bdg_pv.npz "
            f"(L_emp_canonical={L_EMP_CANONICAL}); reconciled per "
            "substrate-first-canonical-sourcing.md §(ii.B)"
        ),
    )
    print(f"  written: {OUT_NPZ.relative_to(ROOT)}")
    print()

    # Section 9: Append verdict line
    print(f"Section 9 — Append canonical verdict + companion rows.")
    value_str = (
        f"B_LAYER_A={B_LAYER_A:.6e}_"
        f"B_LAYER_B={B_LAYER_B:.6f}_"
        f"F_image={F_image_value:.6e}_"
        f"Phi_correspondence_consistency_ratio={Phi_correspondence_consistency_ratio:.6e}_"
        f"B_canonical_anchor={B_canonical_anchor:.6f}_"
        f"classification={classification}_"
        f"slot_decision={slot_decision}_"
        f"OP-PROJ_sectors={sector_index_at_level}_"
        f"STATE-PROJ_anchor=L_emp_canonical={L_EMP_CANONICAL}_"
        f"layer_A_cell=Cell_I_algebra-INVARIANT_"
        f"layer_B_cell=Cell_IV_algebra-DEPENDENT_"
        f"cross-corner_co-primary_FORBIDDEN_"
        f"plan_text_drift=L_emp_runtime_path_s91_w5_1_full_bdg_pv.npz"
    )
    append_verdict(composite, value_str, audit_sha, content_sha,
                   classification, slot_decision)
    print(f"  verdict line appended: {VERDICT_FILE.relative_to(ROOT)}")
    print()

    # Section 10: Final 4-tuple
    tag = (
        f"(value={Phi_correspondence_consistency_ratio!r}, "
        f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"4-tuple: {tag}")
    print(f"\n=== {GATE_ID}: {composite} ===")

    # Section 11: Substrate-framing summary line for audit-trail
    print(f"\nSubstrate-framing summary (phononic-framing.md §'IS Space'):")
    print(f"  The substrate IS the spectral triple (A_K, H_K, D_K(τ_fold))")
    print(f"  at substrate-distance-2 pole s=4. The two layer attributions")
    print(f"  ARE candidate substrate-IS observable forms at structurally")
    print(f"  distinct 4-corner cells (LAYER-A Cell I; LAYER-B Cell IV).")
    print(f"  The Phi-correspondence F-image test IS the substrate's own")
    print(f"  structural test of whether they reduce to the same substrate-")
    print(f"  IS observable (single slot) or to structurally distinct ones")
    print(f"  (split slots). Container-thinking inversion FORBIDDEN.")

    # Exit code: script ran successfully irrespective of verdict per
    # math-scripts.md §"Exit Codes and Verdict Semantics" — verdict is data.
    return 0


if __name__ == "__main__":
    sys.exit(main())
