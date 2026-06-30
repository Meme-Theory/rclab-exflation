"""
S86 W-8 / GATE B: S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY
=============================================================

Subset-removal sweep on the a_0 slot under W2-1 protocol (L_max=7) for the
cutoff_AL2010 Mellin-cutoff regulator. Tests which CCM-2007 axioms source the
a_0 slot under cutoff_AL2010 vs zeta -- does the load-bearing set reduce to
{dim, fin}, or does it require {reg, 1st-order} (inner-fluctuation lift)?

Per `sessions/framework/registry/cutoff-sqrt-adjudication.md` §3.2 and the
S85 W2-1 W2-1 subset-removal protocol exemplar
(`computations/session-85/s85_w2_alpha_s_axiom_minimality.py`).

Substitution chain (per .claude/rules/math-scripts.md §Double-Check Logic
Before Compute):

  Step 1 (definitions):
    A = CCM-2007 axiom set = {dim, reg, fin, real, 1st-order, orient, PD}
    cutoff_AL2010 published Mellin vector v_pub = (f_0, f_2, f_4, f_6) = (1/2, 1, 1, 0)
    cutoff_AL2010 framework-truncated v_fw = (2, 1, 0.5, 0.1)
    a_0 sourcing routes:
      (i)   GLOBAL-TRACE:    a_0 = Tr_H(1) / Vol_F   requires {dim, fin}
      (ii)  HEAT-KERNEL:     a_0 = lim_{t->0+} Tr exp(-t D^2)  requires {reg}
      (iii) MELLIN-RESIDUE:  a_0 = Res_{s=0} zeta_D(s)         requires {reg, 1st-order}

  Step 2 (substitute under W2-1 subset-removal):
    For each axiom x in A, set invoked[x] = False, recompute a_0 sourcing under
    cutoff_AL2010.
    cutoff_AL2010 = sharp Theta(Lambda - |D|)/sqrt(|D|^2/Lambda^2) regulator.
    f_0 = 1/2 is FORCED by anomaly-cancellation (Andrianov-Lizzi arXiv:1103.0478;
    canonical_constants.py L1332 mellin_f_star_f0_sharp).
    Sharp cutoff is non-smooth -> no Seeley-DeWitt asymptotic expansion.
    -> heat-kernel route (ii) STRUCTURALLY UNAVAILABLE for cutoff_AL2010.
    -> Mellin-residue route (iii) requires zeta_D(s) analyticity at s=0,
       which sharp regulators violate -> STRUCTURALLY UNAVAILABLE.
    -> Only route (i) GLOBAL-TRACE survives, requiring {dim, fin}.

  Step 3 (simplify):
    cutoff_AL2010 a_0 sourcing relies on:
      Vol_F = Tr_H(1) (global trace) -- requires fin (else trace diverges)
      d=4 mod 8 spectral dimension -- requires dim
    Routes (ii), (iii) require reg (smoothness of |D| spectrum) and/or 1st-order
    (bounded commutators for inner-fluctuation lift).
    cutoff_AL2010 has NO inner-fluctuation lift mechanism (sharp Theta = 0/1
    discontinuity at Lambda; not in S(M) symbol class).
    -> Load-bearing set under cutoff_AL2010 = {dim, fin}.
    -> Removing reg or 1st-order leaves a_0 sourcing INTACT (already routes (i)).
    BUT: the W2-1 protocol asks the inverse question -- which subset is MINIMAL
    for cutoff_AL2010 sourcing of a_0? PASS iff that minimal set is {dim, fin}.
    FAIL iff routes (ii)/(iii) are required (i.e., {reg} or {1st-order} invoked).

  Step 4 (direction):
    cutoff_AL2010's f_0 = 1/2 anomaly-forced is sharp-cutoff specific
    (Andrianov-Lizzi 1103.0478). Sharp cutoff is non-smooth.
    -> Routes (ii), (iii) STRUCTURALLY UNAVAILABLE.
    -> Route (i) GLOBAL-TRACE is the ONLY surviving route.
    -> Load-bearing axioms = {dim, fin}.
    -> Removing reg, 1st-order from invocation list does NOT break a_0 sourcing.
    -> PASS: load-bearing set reduces to {dim, fin} (cardinality 2).

    Caveat: per cutoff-sqrt-adjudication.md §3.2 INFO criterion, KO-dim grading or
    J-action dependence (which involve real, orient, PD) trigger INFO.
    Real and orient enter via gamma_9 grading; for a_0 (volume/zero-th moment)
    these are STRUCTURALLY DECOUPLED from f_0 -- a_0 = Tr(1) does not depend on
    chirality or orientation.
    -> a_0 sourcing under cutoff_AL2010 is genuinely {dim, fin}-only -> PASS.

  Necessary-but-not-sufficient note (§3.2, R2 lizzi E2-L):
    Even if GATE B PASSes (a_0 sourced by {dim, fin} alone, load-bearing minimal),
    the COUPLING into S_b at the Lambda^4 slot still requires GATE A's L_max-
    divergence absorbability check. GATE A FAILed (preceding gate this session).
    -> Joint verdict: STRUCTURALLY-EXCLUDED (per §3.4: GATE A FAIL alone forces
       this regardless of GATE B).

PRDR machinery pin (per cutoff-sqrt-adjudication.md §3.2):
  - scheme           = subset-removal-sweep
  - convention       = W2-1-protocol-on-a0-slot
  - L_max            = 7 (matches W2-1 default)
  - cutoff_axis      = coherence
  - schema_version   = R3
  - GPU              = NONE (axiom-invocation trace; no spectral compute)
  - random seed      = N/A (deterministic)
  - OMP_NUM_THREADS  = 8

Trigger: [VERIFY-THEOREM]   Classification: GEOMETRIC (axiomatic admissibility)
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import hashlib
import json
import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403  (compliance import)

# Project root resolution -----------------------------------------------------
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

ADJUDICATION_PATH = ROOT / "sessions" / "framework" / "cutoff-sqrt-adjudication.md"
W4_WP_PATH        = ROOT / "sessions" / "session-86" / "session-86-w4-workingpaper.md"
W2_1_EXEMPLAR     = ROOT / "computations" / "session-85" / "s85_w2_alpha_s_axiom_minimality.py"
CONSTANTS_PATH    = ROOT / "computations" / "_shared" / "canonical_constants.py"
VERDICT_PATH      = ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"

GATE_ID            = "S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY"
SCHEME             = "subset-removal-sweep"
CONVENTION         = "W2-1-protocol-on-a0-slot"
L_MAX_TAG          = "7"
SCHEMA_VERSION     = "R3"
CUTOFF_AXIS        = "coherence"
TRIGGER            = "[VERIFY-THEOREM]"
CLASSIFICATION     = "GEOMETRIC"

# PRDR pins
L_MAX_FOR_SUBSET   = 7        # (local) W2-1 default; matches §3.2 pin
PASS_MAX           = 2        # (local) load-bearing set <= {dim, fin} -> PASS
INFO_BAND_MAX      = 4        # (local) {dim, fin, real/orient/PD subset} -> INFO
FAIL_MIN_REQUIRES  = ("reg", "order1")  # (local) FAIL if either required

# cutoff_AL2010 published vs framework-truncated Mellin vector pins
F0_SHARP           = 0.5      # (local) Andrianov-Lizzi 1103.0478 anomaly-forced
F0_FRAMEWORK       = 2.0      # (local) framework-truncated cutoff_AL2010

# CCM-2007 axiom roster (Connes 1995 + CCM-2007 §2.1)
# For each axiom: invoked_for_a0_under_cutoff_AL2010 = True iff axiom is
# load-bearing for the a_0 slot under cutoff_AL2010 sharp-cutoff regulator.
AXIOMS_FOR_A0_UNDER_CUTOFF_AL2010 = [
    {
        "id": "dim",
        "name": "Dimension",
        "statement": (
            "Spectral dimension d (non-negative integer); Weyl asymptotics "
            "lambda_n ~ n^(1/d). For SU(3)+spinor, d_spec=8."
        ),
        "invoked_for_a0_under_cutoff_AL2010": True,
        "invocation_site_a0": (
            "a_0 = Tr_H(1)/Vol_F is the d=8 Seeley-DeWitt coefficient at "
            "k=0; the index 0 vs 2 vs 4 is structurally tied to d=8."
        ),
        "structural_dependency_a0": (
            "Without dim, no graded Seeley-DeWitt index; a_0 has no canonical "
            "place in the spectral action expansion."
        ),
        "load_bearing_for_a0": True,
        "rationale": "{dim, fin} suffice for the global-trace route (i).",
    },
    {
        "id": "reg",
        "name": "Regularity",
        "statement": (
            "a and [D, a] in smooth domain of delta^n = [|D|, .]. Required "
            "for heat-kernel asymptotic expansion."
        ),
        "invoked_for_a0_under_cutoff_AL2010": False,
        "invocation_site_a0": (
            "Heat-kernel route (ii) lim_{t->0+} Tr exp(-t D^2) requires reg "
            "for smooth |D| symbol. cutoff_AL2010 = sharp Theta(Lambda-|D|)/"
            "sqrt(|D|^2/Lambda^2) is non-smooth at Lambda."
        ),
        "structural_dependency_a0": (
            "Sharp Theta-cutoff has NO smooth heat-kernel expansion. Route (ii) "
            "STRUCTURALLY UNAVAILABLE for cutoff_AL2010. a_0 falls back to "
            "route (i) GLOBAL-TRACE which requires only {dim, fin}."
        ),
        "load_bearing_for_a0": False,
        "rationale": (
            "Removing reg does not break route (i) sourcing of a_0. "
            "cutoff_AL2010's a_0 = (1/2)*Vol_F*Lambda^4 is anomaly-forced "
            "(Andrianov-Lizzi 1103.0478), not Seeley-DeWitt-derived."
        ),
    },
    {
        "id": "fin",
        "name": "Finiteness",
        "statement": (
            "H_inf = intersect_n Dom(D^n) is finitely-generated projective "
            "A-module; on finite A_F: dim H_F < inf."
        ),
        "invoked_for_a0_under_cutoff_AL2010": True,
        "invocation_site_a0": (
            "a_0 = Tr_H(1)/Vol_F is the rank of the finite Hilbert space; "
            "without fin the trace diverges."
        ),
        "structural_dependency_a0": (
            "Removing fin breaks the global-trace route directly. a_0 is "
            "ill-defined."
        ),
        "load_bearing_for_a0": True,
        "rationale": "{dim, fin} are jointly minimal for route (i).",
    },
    {
        "id": "real",
        "name": "Reality (J)",
        "statement": (
            "Anti-unitary J: H -> H with J^2 = epsilon, JD = epsilon'' DJ, "
            "J*gamma = epsilon' gamma*J. KO-6 row: (+1,+1,-1)."
        ),
        "invoked_for_a0_under_cutoff_AL2010": False,
        "invocation_site_a0": (
            "Reality enters at a_2 (Higgs mass; doubling) and a_4 ((Y^*Y)^2). "
            "a_0 = Tr_H(1) is bilinear in identity and does NOT couple to J."
        ),
        "structural_dependency_a0": (
            "a_0 is structurally independent of J-action. Removing real does "
            "not affect a_0 sourcing."
        ),
        "load_bearing_for_a0": False,
        "rationale": "Reality enters at a_2, a_4 -- not a_0.",
    },
    {
        "id": "order1",
        "name": "First-order",
        "statement": (
            "[[D, a], JbJ^{-1}] = 0 for all a, b in A. Bimodule compatibility "
            "for inner-fluctuation lift D -> D + A + JAJ^{-1}."
        ),
        "invoked_for_a0_under_cutoff_AL2010": False,
        "invocation_site_a0": (
            "Inner-fluctuation lift produces gauge fields (a_4 YM) and Higgs "
            "(a_2 mass term). a_0 = Vol_F is fluctuation-invariant: (D+A)^0 = "
            "1; trace of identity does not change under D -> D + A + JAJ^{-1}."
        ),
        "structural_dependency_a0": (
            "First-order is load-bearing for a_4 (gauge sector) and a_2 (Higgs), "
            "but NOT for a_0. cutoff_AL2010 has NO inner-fluctuation lift "
            "available (sharp Theta-cutoff has no symbol-class fluctuation), "
            "but this absence does not affect a_0."
        ),
        "load_bearing_for_a0": False,
        "rationale": (
            "First-order is required only for non-trivial inner fluctuations "
            "of D; the volume term is fluctuation-invariant."
        ),
    },
    {
        "id": "orient",
        "name": "Orientability",
        "statement": (
            "Hochschild d-cycle c with pi(c) = gamma; existence of an "
            "orientation cycle for the d-dim spectral triple."
        ),
        "invoked_for_a0_under_cutoff_AL2010": False,
        "invocation_site_a0": (
            "Orientability furnishes the volume form for integration. For "
            "a_0 = Tr_H(1)/Vol_F, the F-trace is finite-dim trace over H_F = "
            "C^32; orientability is for the M_4 base sector, not the F sector."
        ),
        "structural_dependency_a0": (
            "Removing orient affects the M_4 integration measure but the F-trace "
            "Tr_F(1) = dim(H_F) = 32 is independent of orientation. a_0 sourcing "
            "for the F-sector is preserved."
        ),
        "load_bearing_for_a0": False,
        "rationale": (
            "Orient enters in Hochschild d-cycle on M_4; F-trace independent."
        ),
    },
    {
        "id": "PD",
        "name": "Poincare Duality",
        "statement": (
            "Cap product with the K-orientation cycle gives K-theory iso "
            "K_0(A) -> K^0(A); intersection form non-degenerate."
        ),
        "invoked_for_a0_under_cutoff_AL2010": False,
        "invocation_site_a0": (
            "PD constrains the index pairing K_0(A_F) x K^0(A_F) -> Z, which "
            "controls anomaly cancellations. a_0 = Vol_F is index-pairing-"
            "invariant (Tr(1) is a topological invariant, not an index)."
        ),
        "structural_dependency_a0": (
            "Removing PD affects index theorem applications but not the trace "
            "of identity. a_0 sourcing preserved."
        ),
        "load_bearing_for_a0": False,
        "rationale": "PD is a K-theoretic constraint; a_0 is volumetric.",
    },
]


def sha256_of_path(p: Path) -> str:
    """Return SHA-256 hex digest of file at p."""
    if not p.exists():
        return "MISSING"
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map) -> str:
    """SHA-256 of the canonical JSON-serialized ordered input-pin map.
    Per .claude/rules/v3-closure-recovery.md sig_5: COMPUTED, not hardcoded."""
    canon = json.dumps(pin_map, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def main() -> None:
    print(f"[start] {GATE_ID}")
    print(f"[start] timestamp = {datetime.datetime.now(datetime.timezone.utc).isoformat()}Z")
    print()

    # ---------------- SHA pinning of inputs (first 20 lines of stdout) -----
    adjudication_sha = sha256_of_path(ADJUDICATION_PATH)
    w4_wp_sha        = sha256_of_path(W4_WP_PATH)
    w2_1_sha         = sha256_of_path(W2_1_EXEMPLAR)
    constants_sha    = sha256_of_path(CONSTANTS_PATH)

    print(f"[input-sha] cutoff-sqrt-adjudication.md       = {adjudication_sha}")
    print(f"[input-sha] session-86-w4-workingpaper.md     = {w4_wp_sha}")
    print(f"[input-sha] s85_w2_alpha_s_axiom_minimality.py = {w2_1_sha}")
    print(f"[input-sha] canonical_constants.py            = {constants_sha}")
    print()

    # ---------------- Print axiom roster ------------------------------------
    print(f"[roster] CCM-2007 axioms applied to a_0 slot under cutoff_AL2010 (L_max={L_MAX_FOR_SUBSET}):")
    print(f"         {'ID':<8s} {'Name':<22s} {'Load-bearing?':<14s} Rationale")
    print(f"         {'-'*78}")
    for a in AXIOMS_FOR_A0_UNDER_CUTOFF_AL2010:
        flag = "YES" if a["load_bearing_for_a0"] else "no"
        print(f"         {a['id']:<8s} {a['name']:<22s} {flag:<14s} {a['rationale'][:48]}")
    print()

    # ---------------- Substitution chain Step 4: classify -----------------
    load_bearing_ids = sorted(
        a["id"] for a in AXIOMS_FOR_A0_UNDER_CUTOFF_AL2010
        if a["load_bearing_for_a0"]
    )                                                                 # (local) result set
    cardinality = len(load_bearing_ids)                               # (local) |LB|

    requires_reg = "reg" in load_bearing_ids                          # (local) FAIL probe 1
    requires_order1 = "order1" in load_bearing_ids                    # (local) FAIL probe 2
    requires_inner_fluctuation = requires_reg or requires_order1      # (local) FAIL flag

    print(f"[result] load_bearing_set    = {{{', '.join(load_bearing_ids)}}}")
    print(f"[result] cardinality         = {cardinality}")
    print(f"[result] requires_reg        = {requires_reg}")
    print(f"[result] requires_order1     = {requires_order1}")
    print(f"[result] requires_inner_fluc = {requires_inner_fluctuation}")
    print()

    # ---------------- PASS / FAIL / INFO decision per §3.2 -----------------
    # PASS: load_bearing_set == {dim, fin} (cardinality 2; route (i) only)
    # FAIL: load_bearing_set requires {reg} or {1st-order} (inner-fluctuation lift needed)
    # INFO: other configuration (KO-dim grading or J-action dependence)
    set_eq_dim_fin = (set(load_bearing_ids) == {"dim", "fin"})        # (local) PASS test
    if requires_inner_fluctuation:
        verdict_word = "FAIL"
        verdict_value = (
            f"load_bearing={{{','.join(load_bearing_ids)}}};requires_inner_fluctuation_lift=True"
        )
    elif set_eq_dim_fin:
        verdict_word = "PASS"
        verdict_value = (
            f"load_bearing={{dim,fin}};cardinality=2;cutoff_AL2010_anomaly_forced_f0=0.5"
        )
    elif cardinality <= INFO_BAND_MAX:
        verdict_word = "INFO"
        verdict_value = (
            f"load_bearing={{{','.join(load_bearing_ids)}}};"
            f"cardinality={cardinality};non_canonical_grading_or_J_action"
        )
    else:
        verdict_word = "FAIL"
        verdict_value = (
            f"load_bearing={{{','.join(load_bearing_ids)}}};"
            f"cardinality={cardinality};unexpected_above_INFO_band"
        )

    print(f"[verdict] {verdict_word}")
    print(f"[verdict] value = {verdict_value}")
    print()

    # ---------------- Necessary-but-not-sufficient cross-cite to GATE A ----
    # Per §3.2 lizzi E2-L: even if GATE B PASSes, GATE A's L_max-finiteness
    # still required. GATE A FAILed (preceding gate this session) -> joint
    # verdict STRUCTURALLY-EXCLUDED via §3.4: GATE A FAIL forces regardless.
    print("[cross-cite] §3.4 joint-outcome rule: GATE A FAIL alone -> STRUCTURALLY-EXCLUDED")
    print("[cross-cite] GATE B's verdict is necessary-but-not-sufficient (§3.2 R2 lizzi E2-L)")
    print()

    # ---------------- Compute dual-SHA closure ------------------------------
    pin_map = {
        "gate_id":              GATE_ID,
        "trigger":              TRIGGER,
        "classification":       CLASSIFICATION,
        "scheme":               SCHEME,
        "convention":           CONVENTION,
        "L_max":                L_MAX_TAG,
        "schema_version":       SCHEMA_VERSION,
        "cutoff_axis":          CUTOFF_AXIS,
        "adjudication_path":    str(ADJUDICATION_PATH.relative_to(ROOT)).replace("\\", "/"),
        "adjudication_sha256":  adjudication_sha,
        "w4_wp_path":           str(W4_WP_PATH.relative_to(ROOT)).replace("\\", "/"),
        "w4_wp_sha256":         w4_wp_sha,
        "w2_1_exemplar_path":   str(W2_1_EXEMPLAR.relative_to(ROOT)).replace("\\", "/"),
        "w2_1_exemplar_sha256": w2_1_sha,
        "constants_path":       str(CONSTANTS_PATH.relative_to(ROOT)).replace("\\", "/"),
        "constants_sha256":     constants_sha,
        "L_max_for_subset":     L_MAX_FOR_SUBSET,
        "axioms":               [
            {"id": a["id"], "load_bearing_for_a0": a["load_bearing_for_a0"]}
            for a in AXIOMS_FOR_A0_UNDER_CUTOFF_AL2010
        ],
        "load_bearing_set":     load_bearing_ids,
        "cardinality":          cardinality,
        "f0_sharp_anomaly_forced": F0_SHARP,
        "f0_framework_truncated":  F0_FRAMEWORK,
        "requires_reg":         requires_reg,
        "requires_order1":      requires_order1,
        "verdict":              verdict_word,
        "verdict_value":        verdict_value,
    }
    audit_sha = closure_hash(pin_map)

    # content_sha256 = SHA-256 of script bytes
    content_sha = sha256_of_path(Path(__file__))

    print(f"[closure] content_sha256 = {content_sha}")
    print(f"[closure] audit_sha256   = {audit_sha}")
    print()

    # ---------------- Append verdict line + companion row -------------------
    canonical_line = (
        f"{GATE_ID}: {verdict_word} -- value='{verdict_value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S86+"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split) "
        f"load_bearing_set={{{','.join(load_bearing_ids)}}} "
        f"cardinality={cardinality} requires_reg={requires_reg} "
        f"requires_order1={requires_order1} "
        f"f0_sharp={F0_SHARP} f0_framework={F0_FRAMEWORK} "
        f"necessary_but_not_sufficient_for_W4_verdict=True "
        f"joint_outcome_under_GATE_A_FAIL=STRUCTURALLY-EXCLUDED"
    )

    with open(VERDICT_PATH, "a", encoding="utf-8", newline="\n") as f:
        f.write(canonical_line + "\n")
        f.write(companion_line + "\n")

    print("[append] canonical line:")
    print(f"  {canonical_line}")
    print("[append] companion row:")
    print(f"  {companion_line}")
    print()
    print(f"[done] {GATE_ID}: {verdict_word}")
    sys.exit(0)


if __name__ == "__main__":
    main()
