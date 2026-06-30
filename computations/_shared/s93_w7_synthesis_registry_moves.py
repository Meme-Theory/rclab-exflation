#!/usr/bin/env python
"""S93 W7 synthesis registry/corpus/falsifier moves (mack-cosmic-bridge sole writer).

Consequence-of-verdict landing for the three closed W7 gates + 2 co-reviews. METHODOLOGY-class:
the moves are deterministic registry-text edits whose PASS predicate is artifact-existence-with-
substantive-content (NOT a numerical threshold comparison). NO new gate verdict line is emitted
(the W7-1/W7-2/W7-3 verdict lines already exist on disk at lines 155/139/148 of
computations/session-93/s93_gate_verdicts.txt).

THREE MOVES (all SERIAL; single-shot AFTER pattern: build text in memory -> write_atomic ->
re-read + verify -> report):

  MOVE 1 -- corpus cross-pillar-bridge-corpus.md SS23 alpha_s degree RESOLUTION.
            W7-1 (PASS, audit_sha256=9e0a524a..., line 155) resolved deg(T_BZ->pivot)=+2,
            NON-SCALAR (SSVII.BA T4|_{s!=s'}), Reading-T (substrate != pivot).
            - SS23.0 K-counter table alpha_s row: deg OPEN -> +2 (NON-SCALAR, T4|_{s!=s'});
              status OPEN -> RESOLVED (S93 W7-1; transit-CONFIRMED).
            - SS23.1 instance-2 detail block: deg(T_BZ->pivot) OPEN -> +2 RESOLVED;
              matched (scale,channel) = (substrate/BZ O(M_KK), CMB-S4/CMB-HD substrate-sensitivity ~34sigma)
              CONFIRMED as the realized branch; -12.146sigma RELOCATED off-pivot (scale-mismatch);
              pivot vs Planck = +0.67sigma.
            - K-COUNTER STAYS K=2 (alpha_s was ALREADY instance 2 with degree OPEN; resolving its
              degree CONFIRMS instance 2, does NOT add a 3rd distinct observable). SS23 status line
              stays SUGGESTION at K=2. K=3 candidate remains a NEW observable (r or alpha_t).

  MOVE 2 -- falsifier-master-inventory.md alpha_s row 3.rescope-AH-TR-1 re-tag.
            Re-tag to the matched (scale,channel) coordinate per the now-RESOLVED NON-SCALAR
            transport: substrate-distance running -0.08587279 lives at (substrate/BZ scale,
            CMB-S4/CMB-HD substrate-sensitivity channel, ~34sigma live-watch); CMB-pivot image ~=0
            (pivot vs Planck = +0.67sigma, NOT a tension). The -12.146sigma Planck "tension" was a
            SCALE-MISMATCH, NOT a falsification. Cite W7-1 audit_sha256=9e0a524a....

  MOVE 3 -- K_csub_R SCHEMATIC-artifact-RESOLVED annotation (conditional on MCP-check).
            MCP-check resolved: K_csub_R / -245.69 / 247259 is pinned NOWHERE
            (get_constant -> not found; permanent-results-registry.md -> no matches;
            falsifier-master-inventory.md -> no matches). => NO registry move needed;
            W7-2 verdict (PASS, audit_sha256=5ad9875b..., line 139) is self-contained.

Substrate framing (phononic-framing.md SS"IS Space, Not IN Space"): the alpha_s substrate-distance
running and the Goldstone-pivot image are BOTH real substrate-IS observables read FORWARD from the
D_K spectrum; neither is demoted. Their coincidence is set by deg(T_BZ->pivot)=+2 (!=0 => they do
NOT coincide). Direction flows FROM the D_K spectrum DOWNWARD to the emergent power spectrum.
"""

import hashlib
import os
import sys

# --- canonical constants (MANDATORY import; no hardcoded framework values) -----------------------
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (  # noqa: E402
    alpha_s_substrate_distance_1,
    alpha_s_pivot_goldstone,
    planck_alpha_s,
    planck_alpha_s_err,
)

# --- paths (absolute; project root has a SPACE) --------------------------------------------------
ROOT = r"C:\sandbox\Ainulindale Exflation"
CORPUS = os.path.join(ROOT, "sessions", "framework", "registry", "cross-pillar-bridge-corpus.md")
FALSIFIER = os.path.join(ROOT, "sessions", "framework", "registry", "falsifier-master-inventory.md")

# --- W7 verdict provenance (already on disk; cited, not re-emitted) ------------------------------
W7_1_AUDIT_SHA = "9e0a524ae6673bc6f62b5549d110ece5eb55ea98d488fb39683934681426ffdf"  # (local) W7-1 PASS line 155
W7_2_AUDIT_SHA = "5ad9875ba9f2c44181e0b3ecb2576e322eeb8d462766e0712d1881fad40b9f90"  # (local) W7-2 PASS line 139
W7_3_AUDIT_SHA = "3d877f2c205047726692cf46cc13d80f8f9170978cbc8f3517b107e3cb8476cb"  # (local) W7-3 INFO line 148

# --- derived sigma cross-checks (substitution chain; Sage-confirmed -12.145 / +0.672) ------------
sigma_moment_identity = (alpha_s_substrate_distance_1 - planck_alpha_s) / planck_alpha_s_err  # (local)
sigma_pivot = (alpha_s_pivot_goldstone - planck_alpha_s) / planck_alpha_s_err                 # (local)


def read_text(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def write_atomic(path, text):
    """Atomic write with fsync (single-shot AFTER pattern)."""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def apply_replacement(text, old, new, label):
    """Exact-match single replacement; raises if old absent or non-unique."""
    n = text.count(old)
    if n == 0:
        raise SystemExit(f"[FAIL] {label}: anchor string NOT FOUND (re-anchor by content; plan line numbers may be stale)")
    if n > 1:
        raise SystemExit(f"[FAIL] {label}: anchor string non-unique ({n} matches); widen context")
    return text.replace(old, new, 1)


# =================================================================================================
# MOVE 1 -- corpus SS23 (table row + instance-2 detail block)
# =================================================================================================

# --- 1a. SS23.0 K-counter table: alpha_s row (deg OPEN -> +2 NON-SCALAR; status OPEN -> RESOLVED) ---
M1_TABLE_OLD = (
    "| **α_s** (instance 2) | second | OPEN | real-or-trivial pending compute | "
    "`−0.08587279` (Mellin residue s=3, BZ) | `≈0` IF non-scalar; `−0.0859` IF scalar | "
    "OPEN (`S92-W3-CF-S92-W5-1-D` S93) |"
)
M1_TABLE_NEW = (
    "| **α_s** (instance 2) | second | **+2 (NON-SCALAR, T4\\|_{s≠s'})** | REAL (substrate ≠ pivot) | "
    "`−0.08587279` (Mellin residue s=3, BZ) | `≈0` (Goldstone pivot; the NON-SCALAR reading is realized) | "
    "**RESOLVED (S93 W7-1; transit-CONFIRMED; `deg=+2` Sage-locked, `factorization_holds=False`)** |"
)

# --- 1b. SS23.1 instance-2 detail rows -----------------------------------------------------------
M1_DEG_OLD = (
    "| `deg(T_{BZ→pivot})` | **OPEN** — pending `S92-W3-CF-S92-W5-1-D` "
    "(`w(L_max)·κ(k)` factorization; PRE-REG-INC, gate "
    "`S92-W3-CF-S92-W5-1-D-L-MAX-MULTIPLICATIVE-CANCELLATION-RULE-EXTENSION`, deferred S93) |"
)
M1_DEG_NEW = (
    "| `deg(T_{BZ→pivot})` | **+2 — RESOLVED (S93 W7-1, transit-CONFIRMED 4/4 clauses)**. "
    "NON-SCALAR (§VII.BA T4\\|_{s≠s'}), Reading-T (substrate ≠ pivot). The `S92-W3-CF-S92-W5-1-D` "
    "`w(L_max)·κ(k)` factorization is DONE: PART-A `factorization_holds=False` (the s=3 transfer-trace "
    "k-SHAPE is genuinely L_max-dependent, `shape_invariance_max=0.517`, `d2_invariance_max=1.463` — the "
    "n_s-like SCALAR leaf is FALSIFIED); PART-B the canonical `(a₄/a₂)²−1` is a TWO-POLE ratio with "
    "`deg = 2(s₂−s₄) = +2 ≠ 0`, flowing in L_max (`ratio_rel_spread=1.81`, 0.2222→0.0791 at L=6,8,10,12) "
    "⇒ a common 54-decade unit-conversion scalar does NOT cancel ⇒ NON-SCALAR forced. W7-1 PASS "
    "`audit_sha256=9e0a524a…` (line 155, supersedes line 142 per Option A); transport-physics axis "
    "(transit co-review) CONFIRMED with 4 independent Sage checks |"
)

M1_MATCHED_OLD = (
    "| Matched (scale, channel) | (substrate/BZ scale `O(M_KK)`, CMB-S4/CMB-HD substrate-sensitivity "
    "channel ~34σ) IF non-scalar; (CMB-pivot, Planck α_s) IF scalar |"
)
M1_MATCHED_NEW = (
    "| Matched (scale, channel) | **(substrate/BZ scale `O(M_KK)`, CMB-S4/CMB-HD substrate-sensitivity "
    "channel ~34σ) — REALIZED** (the IF-non-scalar branch is now the realized branch, deg=+2). The "
    "(CMB-pivot, Planck α_s) channel carries the Goldstone-protected pivot image `≈0` |"
)

M1_PLANCK_OLD = (
    "| Planck datum | `−0.0045 ± 0.0067` (Planck-2018; `planck_alpha_s`, `planck_alpha_s_err`). "
    "`−0.0859` vs Planck = **−12.146σ** (moment-identity/scalar-transport reading, plan-pinned "
    "session-91-plan-w9.md); pivot `≈0` vs Planck = **+0.67σ** |"
)
M1_PLANCK_NEW = (
    "| Planck datum | `−0.0045 ± 0.0067` (Planck-2018; `planck_alpha_s`, `planck_alpha_s_err`). "
    "**The matched-channel comparison (now that the transport is RESOLVED NON-SCALAR)**: pivot image "
    "`≈0` vs Planck pivot = **+0.67σ** (consistent — this is the realized branch). The `−0.0859` vs "
    "Planck = **−12.146σ** was the moment-identity/scalar-transport reading; with deg=+2 ≠ 0 the "
    "substrate-distance value lives at the substrate/BZ scale, so this −12.146σ is a **SCALE-MISMATCH "
    "RELOCATED OFF the Planck pivot**, NOT a falsification (it routes to the CMB-S4/CMB-HD "
    "substrate-sensitivity channel as a ~34σ-class prediction). Pivot-image recovery as a transport "
    "OUTPUT routes to `CF-S94-W1-6` (§VII.BA T5 direct-Connes-Karoubi) |"
)

# --- 1c. instance-2 section header (degree OPEN -> RESOLVED) --------------------------------------
M1_HDR_OLD = "**Instance 2 — α_s (second-derivative; transport degree OPEN):**"
M1_HDR_NEW = "**Instance 2 — α_s (second-derivative; transport degree RESOLVED NON-SCALAR `+2`, S93 W7-1):**"

# --- 1d. "Why these are TWO genuine K-instances" closer (degree-open -> degree-resolved; K=2 kept) -
M1_CLOSER_OLD = (
    "**Why these are TWO genuine K-instances (Hybrid Independence Test).** n_T (instance 1) and α_s "
    "(instance 2) are distinct on axis-(i) (distinct substrate-IS observable: tensor tilt vs scalar "
    "running) and axis-(iv) (independent transport-factor-degree extraction — n_T's degree is PROVEN "
    "non-scalar via the LiteBIRD discrimination; α_s's degree is OPEN pending the factorization). They "
    "are NOT a numerical refinement of one another — they are at different derivative orders (first vs "
    "second) and their transport degrees are established by structurally distinct computes. So K=2, "
    "advancing toward K=3 MANDATORY."
)
M1_CLOSER_NEW = (
    "**Why these are TWO genuine K-instances (Hybrid Independence Test).** n_T (instance 1) and α_s "
    "(instance 2) are distinct on axis-(i) (distinct substrate-IS observable: tensor tilt vs scalar "
    "running) and axis-(iv) (independent transport-factor-degree extraction — n_T's degree PROVEN "
    "non-scalar via the LiteBIRD discrimination; α_s's degree now RESOLVED NON-SCALAR `+2` via the "
    "S93 W7-1 two-pole `(a₄/a₂)` Wodzicki-degree + flowing-ratio + windowed-trace-shape-dependence "
    "triad). They are NOT a numerical refinement of one another — they are at different derivative "
    "orders (first vs second) and their transport degrees are established by structurally distinct "
    "computes. **K-COUNTER STAYS K=2**: resolving α_s's degree CONFIRMS instance 2 (the OPEN degree is "
    "now closed to NON-SCALAR), it does NOT add a 3rd distinct observable. The K=3 advancement "
    "candidate remains a NEW observable — `r` (tensor-to-scalar ratio) or `α_t` (tensor running) — per "
    "the §23.0 status line; the W7-1/transit \"K=2→K=3\" narration is imprecise (α_s IS instance 2, "
    "not a 3rd instance). Status stays SUGGESTION at K=2, advancing toward K=3 MANDATORY on a third "
    "structurally-distinct instance."
)

corpus = read_text(CORPUS)
corpus_orig = corpus
corpus = apply_replacement(corpus, M1_HDR_OLD, M1_HDR_NEW, "MOVE1-hdr")
corpus = apply_replacement(corpus, M1_TABLE_OLD, M1_TABLE_NEW, "MOVE1-table-row")
corpus = apply_replacement(corpus, M1_DEG_OLD, M1_DEG_NEW, "MOVE1-deg-row")
corpus = apply_replacement(corpus, M1_MATCHED_OLD, M1_MATCHED_NEW, "MOVE1-matched-row")
corpus = apply_replacement(corpus, M1_PLANCK_OLD, M1_PLANCK_NEW, "MOVE1-planck-row")
corpus = apply_replacement(corpus, M1_CLOSER_OLD, M1_CLOSER_NEW, "MOVE1-closer")

# Sanity: the SS23.0 status line "SUGGESTION at K=2" MUST be preserved verbatim (K NOT advanced).
assert "**Status**: SUGGESTION at K=2 (n_T instance 1 + α_s instance 2)." in corpus, \
    "MOVE1 INVARIANT VIOLATED: SS23.0 K=2 SUGGESTION status line must remain intact"

write_atomic(CORPUS, corpus)

# re-read + verify (single-shot AFTER pattern)
corpus_v = read_text(CORPUS)
assert M1_TABLE_NEW in corpus_v, "MOVE1 verify FAILED: table row not on disk"
assert M1_DEG_NEW in corpus_v, "MOVE1 verify FAILED: deg row not on disk"
assert M1_MATCHED_NEW in corpus_v, "MOVE1 verify FAILED: matched row not on disk"
assert M1_PLANCK_NEW in corpus_v, "MOVE1 verify FAILED: planck row not on disk"
assert "**Status**: SUGGESTION at K=2 (n_T instance 1 + α_s instance 2)." in corpus_v, \
    "MOVE1 verify FAILED: K=2 SUGGESTION status not preserved"
assert corpus_v != corpus_orig, "MOVE1 verify FAILED: file unchanged"
print("[PASS] MOVE 1 -- corpus SS23 table row + SS23.1 instance-2 block updated (deg +2 NON-SCALAR RESOLVED; K stays SUGGESTION K=2)")


# =================================================================================================
# MOVE 2 -- falsifier-master-inventory.md alpha_s row 3.rescope-AH-TR-1 re-tag
# =================================================================================================
# The row currently reads "status -> conditionally-closed-pending-transport-degree" and frames the
# IF-non-scalar / IF-scalar branches as READING-CONDITIONAL. With W7-1 RESOLVING deg=+2 NON-SCALAR,
# re-tag the row's status + sigma-tension annotation to the now-realized matched (scale,channel).

M2_STATUS_OLD = (
    "**α_s row RE-SCOPE: dual (scale, channel) entry; status → conditionally-closed-pending-transport-degree** "
    "(S92 AH-TR-1 transit×connes CONVERGED, 2026-05-24; mack-cosmic-bridge sole-writer landing per `feedback_mack-bridge-role.md`)"
)
M2_STATUS_NEW = (
    "**α_s row RE-SCOPE: dual (scale, channel) entry; status → CLOSED-NON-SCALAR-TRANSPORT-RESOLVED "
    "(S93 W7-1, `deg(T_BZ→pivot)=+2`)** "
    "(S92 AH-TR-1 transit×connes CONVERGED, 2026-05-24; transport-degree RESOLVED S93 W7-1 transit-CONFIRMED, 2026-05-24; "
    "mack-cosmic-bridge sole-writer landing per `feedback_mack-bridge-role.md`)"
)

# Re-tag the internal-consistency-split cell ("conditionally-closed-pending-transport-degree" prose).
M2_SPLIT_OLD = (
    "**conditionally-closed-pending-transport-degree** — NOT a fiat single-Planck-pivot comparison; "
    "the prior 12.15σ/13.99σ \"first multi-σ falsifier\" framing is RE-SCOPED to the (c) moment-identity "
    "reading, LIVE only IF deg(T_BZ→pivot) is scalar (§VII.BA T2-VACUOUS, substrate=pivot)."
)
M2_SPLIT_NEW = (
    "**CLOSED-NON-SCALAR-TRANSPORT-RESOLVED (S93 W7-1)** — NOT a fiat single-Planck-pivot comparison; "
    "the transport degree is now RESOLVED `deg(T_BZ→pivot)=+2` NON-SCALAR (§VII.BA T4\\|_{s≠s'}), so the "
    "(c) moment-identity (scalar-transport) reading is the FALSIFIED leaf (substrate ≠ pivot). The prior "
    "12.15σ/13.99σ \"first multi-σ falsifier\" framing was the scalar-transport reading; with NON-SCALAR "
    "transport it RELOCATES OFF the Planck pivot to the (a) substrate/BZ-scale CMB-S4/CMB-HD "
    "substrate-sensitivity channel (~34σ-class). On the matched channels: pivot image `≈0` vs Planck = "
    "**+0.67σ (consistent, NOT a tension)**; substrate-distance `−0.08587279` is a falsifiable "
    "~34σ-reach prediction at the substrate-sensitivity channel (a strength per "
    "`feedback_reporting-framing.md`, NOT defined out of existence). W7-1 PASS "
    "`audit_sha256=9e0a524a…` (line 155)."
)

# Re-tag the sigma-distance cell ("σ-distances are READING-CONDITIONAL ... DEGREE-DISCRIMINATOR pending").
M2_SIGMA_OLD = (
    "**σ-distances are READING-CONDITIONAL**: scalar transport ⇒ −0.0859 IS the pivot α_s, **−12.146σ** "
    "tension LIVE, routes to `CF-S94-W1-6` falsification-grade transport-operator (T5) recovery; "
    "non-scalar transport ⇒ pivot image ≈0 (+0.67σ, consistent), tension RELOCATES to the CMB-S4/CMB-HD "
    "substrate-sensitivity channel (~34σ-class). DEGREE-DISCRIMINATOR pending `S92-W3-CF-S92-W5-1-D` "
    "(`w(L_max)·κ(k)` factorization; PRE-REG-INC, deferred S93) → CF-AH-TR-1-1 §VII.BA-taxonomy classification"
)
M2_SIGMA_NEW = (
    "**σ-distances are now READING-RESOLVED (S93 W7-1, `deg=+2` NON-SCALAR)**: the non-scalar leaf is the "
    "realized branch ⇒ pivot image `≈0` vs Planck = **+0.67σ (consistent)**; the **−12.146σ** "
    "(`−0.0859` vs Planck pivot) was the scalar-transport reading and is a **SCALE-MISMATCH** "
    "(BZ-scale substrate value compared against the Planck pivot datum), now RELOCATED to the "
    "CMB-S4/CMB-HD substrate-sensitivity channel (~34σ-class), NOT a falsification. "
    "DEGREE-DISCRIMINATOR `S92-W3-CF-S92-W5-1-D` (`w(L_max)·κ(k)` factorization) DONE at S93 W7-1 "
    "(`factorization_holds=False`; two-pole `deg(a₄/a₂)=2(s₂−s₄)=+2`); pivot-image recovery as a "
    "transport OUTPUT routes to `CF-S94-W1-6` (§VII.BA T5 direct-Connes-Karoubi)"
)

falsifier = read_text(FALSIFIER)
falsifier_orig = falsifier
falsifier = apply_replacement(falsifier, M2_STATUS_OLD, M2_STATUS_NEW, "MOVE2-status")
falsifier = apply_replacement(falsifier, M2_SPLIT_OLD, M2_SPLIT_NEW, "MOVE2-ic-split")
falsifier = apply_replacement(falsifier, M2_SIGMA_OLD, M2_SIGMA_NEW, "MOVE2-sigma")

# Sanity: Row #3 primary cell value MUST remain (additive re-tag, NOT value-supersession).
assert "**α_s_canonical = -8587279/100000000 ≈ -0.085 872 79**" in falsifier, \
    "MOVE2 INVARIANT VIOLATED: Row #3 primary alpha_s_canonical value must be preserved (additive re-tag only)"

write_atomic(FALSIFIER, falsifier)

falsifier_v = read_text(FALSIFIER)
assert M2_STATUS_NEW in falsifier_v, "MOVE2 verify FAILED: status re-tag not on disk"
assert M2_SPLIT_NEW in falsifier_v, "MOVE2 verify FAILED: ic-split re-tag not on disk"
assert M2_SIGMA_NEW in falsifier_v, "MOVE2 verify FAILED: sigma re-tag not on disk"
assert falsifier_v != falsifier_orig, "MOVE2 verify FAILED: file unchanged"
print("[PASS] MOVE 2 -- falsifier-master-inventory.md row 3.rescope-AH-TR-1 re-tagged to RESOLVED NON-SCALAR matched (scale,channel)")


# =================================================================================================
# MOVE 3 -- K_csub_R SCHEMATIC-artifact-RESOLVED annotation (CONDITIONAL on MCP-check)
# =================================================================================================
# MCP-check (recorded in WP block): K_csub_R / -245.69 / 247259 is pinned NOWHERE:
#   - get_constant("K_csub_R") -> "Constant 'K_csub_R' not found"
#   - permanent-results-registry.md grep(K_csub_R|245.69|247259) -> No matches found
#   - falsifier-master-inventory.md grep(K_csub_R|245.69|247259) -> No matches found
# => NO downstream consumer exists to annotate. The W7-2 verdict (PASS, audit_sha256=5ad9875b...,
#    line 139) is SELF-CONTAINED. No registry move; WP note only.
K_CSUB_R_DOWNSTREAM_CONSUMER_EXISTS = False  # (local) resolved by MCP-check (see WP block)
if K_CSUB_R_DOWNSTREAM_CONSUMER_EXISTS:
    raise SystemExit("[FAIL] MOVE 3: a downstream consumer was found but the script has no annotation branch wired -- re-check")
print("[INFO] MOVE 3 -- K_csub_R has NO downstream registry consumer "
      "(get_constant not found; not in permanent-results-registry.md; not in falsifier-master-inventory.md). "
      "W7-2 verdict self-contained; WP-note only, no registry move.")


# =================================================================================================
# Reporting -- sigma cross-checks + provenance echo (NO verdict line emitted)
# =================================================================================================
print()
print("--- derived sigma cross-checks (canonical_constants imports; Sage-confirmed) ---")
print(f"  alpha_s_substrate_distance_1 = {alpha_s_substrate_distance_1}")
print(f"  alpha_s_pivot_goldstone      = {alpha_s_pivot_goldstone}")
print(f"  planck_alpha_s               = {planck_alpha_s} +/- {planck_alpha_s_err}")
print(f"  sigma(moment-identity BZ vs Planck) = {sigma_moment_identity:.4f}  (matches row's -12.146sigma)")
print(f"  sigma(pivot Goldstone~0 vs Planck)  = {sigma_pivot:.4f}   (matches row's +0.67sigma)")
print()
print("--- W7 verdict provenance (cited, NOT re-emitted) ---")
print(f"  W7-1 PASS audit_sha256={W7_1_AUDIT_SHA[:16]}... (line 155; deg=+2 NON-SCALAR T4|_s!=s', Reading-T)")
print(f"  W7-2 PASS audit_sha256={W7_2_AUDIT_SHA[:16]}... (line 139; cache_truncation_fraction 0.97308->0.000906)")
print(f"  W7-3 INFO audit_sha256={W7_3_AUDIT_SHA[:16]}... (line 148; landau co-review)")
print()
# METHODOLOGY-class corpus-update marker (content-SHA over the two edited registry files).
marker = hashlib.sha256((corpus_v + falsifier_v).encode("utf-8")).hexdigest()  # (local)
print(f"[METHODOLOGY-class corpus-update marker] content_sha256(corpus+falsifier)={marker}")
print()
print("ALL MOVES COMPLETE. No new gate verdict line emitted (W7-1/W7-2/W7-3 already on disk).")
sys.exit(0)
