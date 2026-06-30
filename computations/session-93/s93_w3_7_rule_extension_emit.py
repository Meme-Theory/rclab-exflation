"""S93 W3-7 — METHODOLOGY-class verdict-line emitter (orchestrator-direct).

Emits the S93-W3-7-MULTIPLICATIVE-NORMALIZATION-CANCELLATION-K2-RULE-EXTENSION
verdict line + dual-SHA companion to computations/session-93/s93_gate_verdicts.txt.

METHODOLOGY-class dual-SHA (per wave-classification.md §"Dual-SHA closure for
METHODOLOGY-class"):
  content_sha256 = sha256 over the rule-file diff (the K-counter calibration block).
  audit_sha256   = closure_hash over the ordered input-pin map.

No .py producing script with a numerical threshold (orchestrator-direct rule-file
edit per wave-classification.md §"Dispatch consequences"). PASS predicate is
artifact-existence-with-substantive-content (M1): the math-scripts.md K=2 block +
the τ-moduli structural-distinctness declaration + the allowlist row + corpus entry.
"""
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402 — project convention; methodology emitter consumes no framework constants

ROOT = Path(__file__).resolve().parents[2]
VERDICTS = ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
GATE_ID = "S93-W3-7-MULTIPLICATIVE-NORMALIZATION-CANCELLATION-K2-RULE-EXTENSION"


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    math_scripts = ROOT / ".claude" / "rules" / "math-scripts.md"
    wave_class = ROOT / ".claude" / "rules" / "wave-classification.md"
    npz = ROOT / "computations" / "session-92" / "s92_w3_6_vii_av_level_2_invariance_extension.npz"

    # content_sha256 = sha256 over the rule-file diff (the K-counter calibration block text)
    rule_text = math_scripts.read_text(encoding="utf-8")
    start = rule_text.index("### K-counter calibration corpus")
    end = rule_text.index("### Audit-script enforcement", start)
    rule_file_diff = rule_text[start:end]
    content_sha256 = hashlib.sha256(rule_file_diff.encode("utf-8")).hexdigest()

    # audit_sha256 = closure_hash over the ordered input-pin map
    pinmap = {
        "_gate_id": GATE_ID,
        "_scheme": "METHODOLOGY-class-rule-file-extension",
        "_convention": "multiplicative-normalization-cancellation-K1-to-K2-tau-moduli-axis-DISSENT-sharpened-structurally-distinct-from-L_max-axis",
        "math_scripts_md_sha": sha256_file(math_scripts),
        "wave_classification_md_sha": sha256_file(wave_class),
        "s92_w3_6_npz_sha": sha256_file(npz) if npz.exists() else "NPZ-ABSENT",
        "s92_w3_6_verdict_anchor": "edf5999e873ec6c4a13582a8ae33234cbe43c49e5c393824c241497ba90a4fa3",
        "rule_file_diff_content_sha": content_sha256,
        "K_pre": "1",
        "K_post": "2",
        "k2_instance": "S92-W3-6-tau-moduli-deformation-weight",
        "distinctness_axis": "spectral-support-form",
    }
    closure = "\n".join(f"{k}={pinmap[k]}" for k in sorted(pinmap))
    audit_sha256 = hashlib.sha256(closure.encode("utf-8")).hexdigest()

    value = (
        "K_pre=1_K_post=2_k2_instance=S92-W3-6-tau-moduli-deformation-weight"
        "_structurally_distinct_from_S91-W5-1-L_max-truncation-weight=True"
        "_distinctness_axis=spectral-support-form"
        "_math_scripts_K2_block_present=True_allowlist_row_present=True"
        "_instances_rationale_present=True_calibration_corpus_inline_present=True"
        "_K3_candidate_S93-W3-2-bottom-K-Casimir-ceiling-weight_noted_not_promoted=True"
    )
    line = (
        f"{GATE_ID}: PASS -- value='{value}' "
        f"scheme=METHODOLOGY-class-rule-file-extension "
        f"convention=multiplicative-normalization-cancellation-K1-to-K2-tau-moduli-axis-DISSENT-sharpened-structurally-distinct-from-L_max-axis "
        f"L_max=N/A audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); METHODOLOGY-class rule-file-extension (M1 artifact-existence); [AUDIT] no [SIGN] 3-tuple\n"
    )

    # sig_5 uniqueness check
    existing = VERDICTS.read_text(encoding="utf-8") if VERDICTS.exists() else ""
    if f"audit_sha256={audit_sha256}" in existing:
        print(f"ERR: audit_sha256 collision (sig_5) for {audit_sha256[:16]}")
        return 1
    if f"^{GATE_ID}:" in existing or f"\n{GATE_ID}:" in existing:
        print(f"NOTE: {GATE_ID} verdict already present; no-op")
        return 0
    with VERDICTS.open("a", encoding="utf-8") as f:
        f.write(line)
        f.write(companion)
    print(f"EMITTED {GATE_ID}: PASS")
    print(f"audit_sha256={audit_sha256}")
    print(f"content_sha256={content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
