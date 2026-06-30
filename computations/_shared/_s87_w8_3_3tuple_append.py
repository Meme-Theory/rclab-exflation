"""One-shot append-only writer for S87-C45-SIXTH-REGULATOR-PROMOTION 3-tuple annotation.

Appends the required SIGN/MAGNITUDE/REGIME 3-tuple companion row per
`.claude/rules/gate-verdicts.md` §"S87+ canonical form" lines 102-107.

Rule excerpt (verbatim):
    # sign_verdict=PASS|FAIL|N/A magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN # {GATE_ID} 3-tuple annotation (S87 schema-v2)

Per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under
Parallel-Writer Race" item (2): use a one-shot Python writer (open in 'a'
mode, append, close) to avoid Edit-tool mtime races on shared-write
verdict files.

Field semantics (per gate-verdicts.md lines 110-134):

  sign_verdict = PASS  -- per substitution chain Step 4 evaluation:
      Plan §9 Step 4 predicted (a) CM-Hopf is the prime channel-2 PASS
      candidate (deterministic); (b) Schwinger and dim-reg are channel-2
      FAIL likely (a_0-direct reading defect); (c) Borel and Lorentz
      "may PASS" channel-2 (hedge). Empirically:
        - CM-Hopf: ch-2 PASS  (deterministic prediction MATCHED)
        - Schwinger: ch-2 FAIL (deterministic prediction MATCHED)
        - dim-reg:   ch-2 FAIL (deterministic prediction MATCHED)
        - Borel:     ch-2 FAIL (consistent with may-PASS hedge — not falsified)
        - Lorentz:   ch-2 FAIL (consistent with may-PASS hedge — not falsified)
      The LOAD-BEARING structural prediction (channel-2 FAIL ⇒ channel-4
      FAIL one-way implication, and CM-Hopf-vs-others bifurcation) HELD
      empirically: 4 candidates with channel-2 FAIL also FAIL channel-4;
      CM-Hopf is the unique channel-2 PASS. NO prediction was contradicted.
      sign_verdict = PASS.

  magnitude_verdict = INFO -- composite top-line is INFO (n_PASS=0/5 with
      3 PARTIAL-INFO eligible candidates per plan §5 INFO predicate);
      gate-verdicts.md collapse rule line 150-151:
      magnitude_verdict == INFO ⇒ composite = INFO.

  regime_verdict = VALID -- 4-channel chain test executed within pre-
      registered scope: α-scan [-2, +2] step 0.05 (full 81-grid); channel-2
      Sage symbolic algebra evaluated to closed-form on all 5 candidates
      (no domain shortening); channel-3 HBW MP-abs-conv at s ∈ {2, 4, 6}
      on f_2/f_4/f_6 truncation as pre-registered; no regime-of-validity
      breach within the integration window; no auto-shortening clause
      activated. regime_verdict = VALID.

Composite-collapse check (gate-verdicts.md lines 138-154 deterministic rule):
  regime_verdict=VALID (not BREAKDOWN)
  sign_verdict=PASS (not FAIL)
  magnitude_verdict=INFO (not FAIL)
  → composite = INFO (line 150-151 branch).
This MATCHES the existing canonical line's INFO verdict; no consistency
violation; the 3-tuple is concordant with the composite.

Append-only discipline:
  - Lines 237 (canonical) and 238 (dual-SHA companion) are NOT modified.
  - The 3-tuple row is appended at end-of-file; a trailing newline is
    ensured.
  - The gate-id token in the comment row is the unique identifier; future
    consumers can grep for it.
"""
from __future__ import annotations

from pathlib import Path

VERDICT_PATH = (
    Path(__file__).resolve().parent.parent
    / "computations"
    / "s87_gate_verdicts.txt"
)

GATE_ID = "S87-C45-SIXTH-REGULATOR-PROMOTION"
SIGN_VERDICT = "PASS"
MAGNITUDE_VERDICT = "INFO"
REGIME_VERDICT = "VALID"

LINE = (
    f"# sign_verdict={SIGN_VERDICT} "
    f"magnitude_verdict={MAGNITUDE_VERDICT} "
    f"regime_verdict={REGIME_VERDICT} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
)


def main() -> int:
    # Pre-flight: confirm the existing canonical + dual-SHA companion are present
    text = VERDICT_PATH.read_text(encoding="utf-8")
    canonical_present = (
        f"{GATE_ID}: INFO -- value=(0, None) scheme=4-channel-chain-test" in text
    )
    dual_sha_present = (
        f"{GATE_ID} dual-SHA companion row" in text
    )
    if not canonical_present:
        print(f"ERROR: canonical {GATE_ID} line not found; aborting append.")
        return 1
    if not dual_sha_present:
        print(f"ERROR: dual-SHA companion for {GATE_ID} not found; aborting append.")
        return 1
    if LINE in text:
        print(f"NOOP: 3-tuple annotation for {GATE_ID} already present; not appending.")
        return 0

    # Atomic append (POSIX O_APPEND semantics; safe under parallel writers).
    # Ensure the file ends with a newline before appending.
    needs_leading_newline = not text.endswith("\n")
    with VERDICT_PATH.open("a", encoding="utf-8") as fp:
        if needs_leading_newline:
            fp.write("\n")
        fp.write(LINE)

    print(f"OK: appended 3-tuple annotation for {GATE_ID}")
    print(f"  sign_verdict={SIGN_VERDICT}  magnitude_verdict={MAGNITUDE_VERDICT}  regime_verdict={REGIME_VERDICT}")
    print(f"  composite-collapse check: regime=VALID, sign=PASS, magnitude=INFO -> composite=INFO (matches canonical line)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
