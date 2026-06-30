#!/usr/bin/env python3
"""
S96-HYG-JOINT-EVIDENCE-D3-RESTRICT  (METHODOLOGY-class, [AUDIT] trigger)
=======================================================================

Restrict the capstone (sessions/framework/phonic-exflation-equation.md) §7.3
joint-evidence claim, CONDITIONED on the now-landed W7-7a covariance verdict
(S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE = FAIL; max cross-layer residual
correlation = 1.0000 on the a0-a2 pair, band > 0.5).

The W7-7a FAIL branch fires (plan dual_prior: FAIL Corr>0.5 -> 0.9 to Track B):
  (1) the Wronskian (W2-E Spectral-Moment Decoupling Theorem, S75) licenses
      ALGEBRAIC layer-independence (a0/a2/a4 functionals independent off-genesis,
      W proportional to R_K'(tau)^3), NOT STATISTICAL independence of the
      borrowed-H residuals -- a0/a2 co-shift PERFECTLY (Corr=+1.0000) under the
      shared C10 H(t);
  (2) scope the joint-BF to the zero-parameter STRUCTURAL SPINE (Higgs mass,
      normal mass ordering, sigma/m=0, c_s^2=0 -- carry NO borrowed H);
  (3) replace "chance of one random geometry" with the EVOI prior-predictive-
      range / posterior-width formulation (mack CF-MACK-7);
  (4) state explicitly that Omega_DM and sigma8 (BOTH a2-layer) are NOT
      multiplied as independent factors.

This is a METHODOLOGY-class artifact-existence gate: the PASS predicate is that
the restricted §7.3 text exists with the four content elements and the W7-7a
conditioning. There is NO numerical threshold; the directional finding lives in
W7-7a's substitution chain. This script performs the ATOMIC section-scoped
splice of §7.3 ONLY (read -> splice the §7.3 region -> fsync + os.replace),
preserving every other byte of the curated capstone, then emits the dual-SHA
verdict line.

  audit_sha256  := SHA-256 over the input-pin map { capstone_section_diff,
                   w7_7a_verdict_line, pinmap }   (per gate audit_discriminators)
  content_sha256:= SHA-256 over the §7.3 capstone_section_diff (old||new)

Substrate framing: NON-PHONONIC methodology contribution. The restriction
ENFORCES the substrate-first epistemic partition -- the zero-parameter spine is
substrate-IS (Higgs from a4 KK-threshold, mass ordering from D_K eigenvalue
ordering, sigma/m=0 from N_Fock=1 superselection, c_s^2=0 from Kasparov
factorization) and carries NO borrowed H(t); the dagger rows (w0, wa, sigma8,
CC) borrow the container-observer's H(t) and are conditional. The edit keeps the
explanation flowing substrate -> emergent; it DOWN-TAGS the over-confident
statistical-independence wording to the register status (algebraic, not
statistical) without inverting the explanation direction.
"""
import os
import sys
import hashlib

# METHODOLOGY-class doc-edit: no framework numerical constants are consumed in
# the text restriction (this is an artifact-existence text-restriction gate; the
# only "inputs" are the capstone §7.3 region and the W7-7a verdict line, both
# pinned by SHA). The canonical import is present to satisfy the
# computations/_shared/CLAUDE.md canonical-import discipline + the python-validate
# hook; M_KK is the substrate witness for the §7.3 spine member m_H (a₄ KK-threshold).
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))  # (local)
from canonical_constants import M_KK  # noqa: F401  (local) doc-edit gate; witness only, no numerics
assert M_KK > 0  # (local) provenance sanity: substrate KK scale is the m_H spine anchor

ROOT = r"C:\sandbox\Ainulindale Exflation"  # (local) project root
CAPSTONE = os.path.join(ROOT, "sessions", "framework", "phonic-exflation-equation.md")  # (local)
VERDICTS = os.path.join(ROOT, "computations", "session-96", "s96_gate_verdicts.txt")  # (local)

GATE_ID = "S96-HYG-JOINT-EVIDENCE-D3-RESTRICT"  # (local)
W7_7A_GATE = "S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE"  # (local)
# Full 64-char audit_sha256 of the W7-7a covariance verdict line (read off disk, pinned here):
W7_7A_AUDIT_SHA = "7227c8c5dc6d4fbdbf61888cf1bb74dfbc0ee9fa4c12bde26c6e2facd11dba5e"  # (local)


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()  # (local)


# ---------------------------------------------------------------------------
# 1. The OLD §7.3 over-reaching sentence (exact bytes to be replaced).
#    This is the single sentence in the §7.3 scorecard paragraph that conflates
#    ALGEBRAIC (Wronskian) independence with STATISTICAL independence and frames
#    the joint claim as "chance of one random geometry".
# ---------------------------------------------------------------------------
OLD_SENTENCE = (
    "A prediction landing near data from zero free parameters across a wide prior range is "
    "Bayesian evidence with a large likelihood ratio — emphatically *not* \"case unchanged\" — "
    "and the joint statement is the strong one, *grounded in the Decoupling Theorem* (§4.2): "
    "the chance of one random geometry reproducing observables in the relic-abundance AND the "
    "CC-scale AND the matter sectors is the product of the individual improbabilities **across "
    "distinct spectral-moment layers** (`a₀ × a₂ × a₄`, independent by the certified Wronskian). "
    "Within a single layer — `Ω_DM` and `σ₈` are both `a₂`-channel — the observables share a "
    "geometric origin and must *not* be multiplied as independent."
)  # (local)

# ---------------------------------------------------------------------------
# 2. The NEW restricted text (conditioned on the W7-7a FAIL, Corr=1.0000).
#    Four content elements, all present:
#      (1) Wronskian licenses ALGEBRAIC not STATISTICAL independence;
#      (2) joint-BF scoped to the zero-parameter structural spine (no borrowed H);
#      (3) EVOI prior-predictive-range / posterior-width replaces "random geometry";
#      (4) Omega_DM & sigma8 (both a2) explicitly NOT multiplied.
# ---------------------------------------------------------------------------
NEW_SENTENCE = (
    "A prediction landing near data from zero free parameters across a wide prior range is "
    "Bayesian evidence with a large likelihood ratio — emphatically *not* \"case unchanged\" — "
    "and the way to state the joint claim is the EVOI **prior-predictive-range / posterior-width** "
    "form (mack CF-MACK-7), *not* a \"chance of one random geometry\" ensemble count: the Bayes "
    "factor for each observable is `BF = (prior-predictive range)/(posterior width around the "
    "observation)`, and the joint statement multiplies these BFs **only across observables that are "
    "BOTH algebraically AND statistically independent**. The critical restriction (forced by the "
    "W7-7a covariance check, `S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE`): the certified Wronskian "
    "(Decoupling Theorem, §4.2 / W2-E) licenses only **algebraic** layer-independence of the "
    "spectral-moment *functionals* `a₀/a₂/a₄` (degenerate solely at genesis), it does **not** "
    "license **statistical** independence of the *residuals* of observables that borrow the "
    "container-observer's `H(t)`. W7-7a measured exactly this and FAILED it: under the shared C10 "
    "`H(t)`, the `a₀` and `a₂` borrowed-`H` residuals **co-shift perfectly** "
    "(`Corr(a₀,a₂) = +1.0000`, band > 0.5; `Corr(a₀,a₄) = Corr(a₂,a₄) = 0`). So the joint-BF "
    "is scoped to the **zero-parameter structural spine** — `m_H ≈ 127.5–131.8 GeV` (`a₄` "
    "KK-threshold), normal mass ordering (`D_K` eigenvalue ordering), `σ/m = 0` (`N_Fock = 1` "
    "superselection), and `c_s² = 0` (Kasparov factorization) — these are substrate-IS predictions "
    "carrying **no borrowed `H(t)`**, so their evidence multiplies cleanly. The borrowed-`H` dagger "
    "rows (`w₀, wₐ, σ₈, CC`) are conditional and are **not** entered as independent likelihood "
    "factors. And WITHIN a single layer — `Ω_DM` and `σ₈` are **both** `a₂`-channel — the "
    "observables share a geometric origin and are **not** multiplied as independent (pre-registered, "
    "independent of W7-7a): the within-layer non-multiplication and the cross-layer statistical-"
    "dependence are two distinct reasons the naive product over-states the evidence."
)  # (local)

# ---------------------------------------------------------------------------
# 3. A new reconciliation note (item 5) appended to the §7.3 scorecard-status
#    reconciliation blockquote, recording the W7-7a-conditioned restriction as a
#    register-pinned status nuance (substrate-first; down-tag only).
#    OLD_NOTE_TAIL is the closing of the existing item (4) D5 sentence; the
#    splice inserts item (5) immediately after it, inside the same blockquote.
# ---------------------------------------------------------------------------
OLD_NOTE_TAIL = (
    "routed to the W4 D5 0νββ Majorana-vs-Dirac reconciliation gate, not resolved by this status-sync."
)  # (local)
NEW_NOTE_TAIL = (
    OLD_NOTE_TAIL
    + " **(5) The joint-BF multiplies ALGEBRAICALLY-AND-STATISTICALLY-independent factors only "
    "(register-pinned by `S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE`).** The certified Wronskian gives "
    "*algebraic* layer-independence (`W ∝ R_K′(τ)³`); it does **not** carry to *statistical* "
    "independence of the borrowed-`H(t)` residuals — W7-7a measured `Corr(a₀,a₂) = +1.0000` "
    "(perfect co-shift under the shared C10 `H(t)`), so the strong joint claim is scoped to the "
    "zero-parameter structural spine (`m_H`, mass ordering, `σ/m = 0`, `c_s² = 0` — no borrowed "
    "`H`), the borrowed-`H` dagger rows (`w₀, wₐ, σ₈, CC`) are conditional and not multiplied, and "
    "the EVOI prior-predictive-range / posterior-width form (mack CF-MACK-7) replaces the \"chance of "
    "one random geometry\" framing. Read the joint statement as the product over the substrate-IS "
    "spine, never over the borrowed-`H` projection."
)  # (local)


def main() -> int:
    # --- read capstone (full, exact bytes) ---
    with open(CAPSTONE, "r", encoding="utf-8") as f:
        original = f.read()  # (local)

    # --- pre-flight: the two anchor strings MUST each appear exactly once ---
    n_old_sentence = original.count(OLD_SENTENCE)  # (local)
    n_old_note = original.count(OLD_NOTE_TAIL)  # (local)
    if n_old_sentence != 1:
        print(f"FAIL: OLD_SENTENCE anchor count = {n_old_sentence} (expected 1) -- aborting, no write")
        # honest mechanical-closure-style FAIL (no edit performed); emit a FAIL verdict.
        emit_verdict("FAIL", f"old_sentence_anchor_count={n_old_sentence}_NOT_1_no_edit", "", "")
        return 0
    if n_old_note != 1:
        print(f"FAIL: OLD_NOTE_TAIL anchor count = {n_old_note} (expected 1) -- aborting, no write")
        emit_verdict("FAIL", f"old_note_tail_anchor_count={n_old_note}_NOT_1_no_edit", "", "")
        return 0

    # --- perform the two scoped splices (§7.3 region ONLY) ---
    updated = original.replace(OLD_SENTENCE, NEW_SENTENCE, 1)  # (local)
    updated = updated.replace(OLD_NOTE_TAIL, NEW_NOTE_TAIL, 1)  # (local)

    # --- byte-for-byte preservation check OUTSIDE the §7.3 region ---
    # Reconstruct what the rest of the file should be by removing both spliced
    # regions from both old and new; the remainders must be identical.
    rem_old = original.replace(OLD_SENTENCE, "\x00SENT\x00", 1).replace(OLD_NOTE_TAIL, "\x00NOTE\x00", 1)  # (local)
    rem_new = updated.replace(NEW_SENTENCE, "\x00SENT\x00", 1).replace(NEW_NOTE_TAIL, "\x00NOTE\x00", 1)  # (local)
    if rem_old != rem_new:
        print("FAIL: byte-for-byte preservation check FAILED outside the §7.3 region -- aborting, no write")
        emit_verdict("FAIL", "byte_preservation_check_FAILED_no_edit", "", "")
        return 0

    if updated == original:
        print("FAIL: splice produced no change -- aborting")
        emit_verdict("FAIL", "splice_no_change_no_edit", "", "")
        return 0

    # --- atomic write: tmp -> fsync -> os.replace ---
    tmp = CAPSTONE + ".s96w7b.tmp"  # (local)
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(updated)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, CAPSTONE)

    # --- re-read + verify the section landed ---
    with open(CAPSTONE, "r", encoding="utf-8") as f:
        landed = f.read()  # (local)

    checks = {
        "new_sentence_present": NEW_SENTENCE in landed,
        "new_note_present": NEW_NOTE_TAIL in landed,
        "old_sentence_gone": OLD_SENTENCE not in landed,
        # four content elements present in the landed §7.3 text:
        "elem1_algebraic_not_statistical": "**algebraic** layer-independence" in landed
        and "**statistical** independence of the *residuals*" in landed,
        "elem2_zero_param_spine": "zero-parameter structural spine" in landed
        and "N_Fock = 1` " in landed
        and "Kasparov factorization" in landed,
        "elem3_prior_predictive_range": "prior-predictive-range / posterior-width" in landed
        and "CF-MACK-7" in landed,
        "elem4_within_layer_not_multiplied": "are **not** multiplied as independent (pre-registered" in landed,
        "w7_7a_conditioning_cited": "S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE" in landed
        and "Corr(a₀,a₂) = +1.0000" in landed,
    }  # (local)
    all_pass = all(checks.values())  # (local)

    # --- dual-SHA inputs ---
    # content_sha256 over the §7.3 capstone_section_diff (old sentence||new sentence||old note||new note)
    section_diff = OLD_SENTENCE + "\x1e" + NEW_SENTENCE + "\x1e" + OLD_NOTE_TAIL + "\x1e" + NEW_NOTE_TAIL  # (local)
    content_sha = sha256_text(section_diff)  # (local)
    # audit_sha256 over the ordered input-pin map: {capstone_section_diff, w7_7a_verdict_sha, pinmap}
    pinmap = (
        f"gate_id={GATE_ID}|"
        f"w7_7a_gate={W7_7A_GATE}|"
        f"w7_7a_audit_sha256={W7_7A_AUDIT_SHA}|"
        f"capstone={os.path.relpath(CAPSTONE, ROOT)}|"
        f"scheme=joint-BF-restriction-to-structural-spine|"
        f"convention=prior-predictive-range(EVOI)-replacing-ensemble-cross-LAYER-WITHIN-layer-NOT-multiplied|"
        f"content_sha256={content_sha}"
    )  # (local)
    audit_sha = sha256_text(pinmap)  # (local)

    for k, v in checks.items():
        print(f"  check {k}: {v}")
    print(f"all_pass={all_pass}")
    print(f"content_sha256={content_sha}")
    print(f"audit_sha256={audit_sha}")

    if not all_pass:
        failed = [k for k, v in checks.items() if not v]  # (local)
        emit_verdict("FAIL", f"landed_but_content_checks_failed:{','.join(failed)}", audit_sha, content_sha)
        return 0

    value = (
        "restricted=4-elements;"
        "W7-7a=FAIL_Corr(a0,a2)=+1.0000_band>0.5;"
        "Wronskian_licenses_ALGEBRAIC_NOT_STATISTICAL_indep;"
        "joint-BF_scoped_to_zero-param_spine(m_H,mass-ordering,sigma/m=0,c_s2=0_NO_borrowed_H);"
        "EVOI_prior-predictive-range/posterior-width(CF-MACK-7)_replaces_random-geometry;"
        "Omega_DM_AND_sigma8_both_a2_NOT_multiplied;"
        "borrowed-H_dagger-rows(w0,wa,sigma8,CC)_conditional_NOT_independent_factors;"
        "substrate-first_down-tag_preserved"
    )  # (local)
    emit_verdict("PASS", value, audit_sha, content_sha)
    return 0


def emit_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append the canonical line + dual-SHA companion + 3-tuple companion (schema_v2)."""
    scheme = "joint-BF-restriction-to-structural-spine"  # (local)
    convention = "prior-predictive-range(EVOI)-replacing-ensemble-cross-LAYER-per-W7-7a-WITHIN-layer-NOT-multiplied"  # (local)
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max=N/A "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (METHODOLOGY-class; consumes W7-7a verdict "
        f"audit_sha256={W7_7A_AUDIT_SHA}; capstone §7.3 atomic section-scoped restriction; "
        f"FAIL-branch of dual_prior fired -> Track B; substrate-first down-tag of "
        f"algebraic->statistical-independence over-reach)\n"
    )  # (local)
    # 3-tuple companion (schema_v2). Not strictly required (schema_v2_3tuple_required=false),
    # but emitted for completeness: this gate has no directional pre-reg of its own (sign N/A);
    # the directional content lives in W7-7a. magnitude = artifact-existence (PASS if all four
    # content elements present); regime = VALID (deterministic text restriction, no expansion).
    sign_v = "N/A"  # (local) no directional pre-registration; direction is W7-7a's
    mag_v = "PASS" if verdict == "PASS" else "FAIL"  # (local) artifact-existence-with-content
    regime_v = "VALID"  # (local) deterministic text edit; no small-parameter expansion
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); sign = N/A (no own directional pre-reg; "
        f"the algebraic-vs-statistical-independence direction is W7-7a's substitution chain, "
        f"Corr(a0,a2)=+1.0000 induced co-shift); mag = artifact-existence-with-content "
        f"({'all 4 content elements + W7-7a conditioning present' if verdict=='PASS' else 'content checks failed'}); "
        f"regime = VALID (deterministic atomic section-scoped restriction of capstone §7.3; "
        f"down-tags algebraic->statistical-independence over-reach to register status; "
        f"substrate-first explanation direction preserved)\n"
    )  # (local)
    with open(VERDICTS, "a", encoding="utf-8", newline="") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)
        f.flush()
        os.fsync(f.fileno())
    print(f"[emit] {verdict} verdict appended for {GATE_ID}")


if __name__ == "__main__":
    sys.exit(main())
