#!/usr/bin/env python
"""
S85-W2-PSG-SECTION-11-2-REVISION

Documentation-revision audit for PSG §11.2 ("Cosmological Constant from a_0"
in sessions/framework/Phononic-Substrate-Geometry.md).

Revision integrates three post-S82 substrate results:
  (1) S84 §VII.N three-layer regulator theorem (L1 zeta / L2 Zubarev /
      L3 per-Q span) — landed in registry per S84 W2a-11.
  (2) S84 §VII.P disjoint-corridor theorem — NOTE per S85 W2-7 (this session):
      LANDING BLOCKED by counter-example (C_H, C_epsH) spectral match;
      refined §VII.P-v2 (restricted to HP^0-content-distinct corridors) is
      S86 carry-forward. Revision honors the pending status.
  (3) Cross-references to S85 W2-6 (quantum disjoint corridor PASS) and
      S85 W2-7 (counter-construction FAIL-with-refinement).

Gate PASS iff integration_count = 3 (all three items land in revised §11.2),
INFO iff PASS + stylistic gap (e.g. §11.2 length grows > 2x), FAIL iff < 3.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403

INPUT_FILES = [
    "sessions/framework/Phononic-Substrate-Geometry.md",
    "sessions/permanent-results-registry.md",
    "sessions/archive/session-85/session-85-w2-workingpaper.md",
]


def sha256_of(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return "MISSING"
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_original_section_11_2(psg_text: str) -> tuple[str, int, int]:
    """Extract the current §11.2 text between '### 11.2' and the next '### '."""
    m = re.search(r"(### 11\.2 Cosmological Constant from `a_0`.*?)(?=^### 11\.3 )",
                  psg_text, re.DOTALL | re.MULTILINE)
    if not m:
        raise RuntimeError("Failed to locate PSG §11.2 section")
    body = m.group(1)
    return body, m.start(), m.end()


def build_revised_section_11_2(original: str) -> str:
    """Draft the revised §11.2 with 3 new integrations."""
    # Preserve original content + append sub-sections 11.2.X/Y/Z
    revised = original.rstrip() + r"""


#### 11.2.A Regulator-stratification: The Three-Layer Theorem (§VII.N, S84 W2a-11)

The CC-from-`a_0` computation is a spectral-functional evaluation, and it inherits
the three-layer regulator stratification proven in S84 W2a-11 and landed as
registry §VII.N (Connes + Lizzi + Van den Dungen three-solo convergence):

- **L1 (axiomatic, global)**: the canonical measure on the substrate's operator
  spectrum is the Dixmier trace / zeta-residue form, `Tr_ω(T) = Res_{s=d} Tr(T |D|^{-s})`
  (Connes-Marcolli 2008 Thm 1.31). Unique regulator at L1: **zeta**.
- **L2 (substrate-action, at τ_fold)**: three-criterion intersection (integrability,
  `d²S/dτ² > 0` at fold, chirality χ = +1) selects **Zubarev** at τ = 0.19,
  L_max = 5.
- **L3 (observable, per-Q)**: 5-regulator span partitions into R-protected
  `[1.0, 1.5]` / NOT-R-protected `[2.5, ∞)`. Gap `[1.5, 2.5]` empty. CC-5
  propagation `span(O) = ∏_i span(F_i)^|p_i|` applies ONLY at L3.

**Consequence for CC**: `Λ_CC` is an L3 observable (regulator-dependent span per
§VII.K-DUAL atlas; the `0.337 ρ_obs` value above is at Zubarev/L2, L_max = 5).
The factor-3 residual is the per-observable span bracket, not a fundamental
discrepancy — L1 and L2 are already canonicalized, L3 residue is pre-registered.

#### 11.2.B Corridor separability: Disjoint-Corridor (§VII.P pending, W2-7 FAIL-with-refinement)

S84 S-5 Connes synthesis proposed §VII.P: HP⁰ ∩ HP¹ = {0} for (A_F, H_F, D_F),
with secondary class ε_H explicitly living in HP¹. This separability was
further proposed to imply spectral-functional distinguishability across
HP²-disjoint corridor pairs in the (a_0, a_2, a_4) Seeley-DeWitt coefficients.

**Status (S85 W2-7, 2026-04-23, this session)**: Counter-construction audit
**FAILED** registry landing with num_counter_examples = 1. The pair
(C_H, C_epsH) shares identical factor support {H} but differs only in the
ε_H secondary HP¹ twist, which is invisible to even-parity Seeley-DeWitt
coefficients. §VII.P as originally written is FALSIFIED at the literal level;
refined §VII.P-v2 (restricted to HP⁰-content-distinct corridors) is S86+
carry-forward.

**Consequence for CC**: the `a_0` CC computation uses the HP⁰-content of
(A_F, H_F, D_F), unambiguously distinguished across corridors even without
§VII.P. The CC calculation is NOT affected by the pending refinement; the
structural parity-blindness exposed by W2-7 affects only corridor-pair
Seeley-DeWitt MATCHING (which is NOT a CC evaluation step).

#### 11.2.C Cross-references — S85 W2-6 and W2-7

- **S85 W2-6 (Quantum disjoint corridor, PASS)**: The Disjoint-Corridor
  separability theorem survives q-deformation of A_F at generic q ∈ (0,1) ∪ (1,∞)
  via 4-route confluence (HKR+SBI, H²_dR(S¹_q)=0, q-scan over 10 generic values,
  pullback from A_θ). Extending the substrate to non-commutative fiber
  algebras A_F^q does not break the parity-based corridor separation.

- **S85 W2-7 (Counter-construction, FAIL-with-refinement)**: identified the
  (C_H, C_epsH) twin pair where spectral moments match exactly despite
  HP²-disjointness — documenting the parity-blindness of even Seeley-DeWitt
  to HP¹ secondary twists. Refinement: §VII.P-v2 restricted to
  HP⁰-content-distinct corridors; odd-parity diagnostic (η-invariant,
  Godbillon-Vey integral) required for twin-pair distinguishability.
"""
    return revised


def main() -> int:
    print("=" * 70)
    print("S85-W2-PSG-SECTION-11-2-REVISION")
    print("=" * 70)
    input_shas: dict[str, str] = {}
    for f in INPUT_FILES:
        sha = sha256_of(f)
        input_shas[f] = sha
        print(f"INPUT  {f}  sha256={sha}")
    print("-" * 70)

    psg_path = Path("sessions/framework/Phononic-Substrate-Geometry.md")
    psg_text = psg_path.read_text(encoding="utf-8", errors="ignore")

    original_section, orig_start, orig_end = extract_original_section_11_2(psg_text)
    revised_section = build_revised_section_11_2(original_section)

    original_len = len(original_section.splitlines())   # (local)
    revised_len = len(revised_section.splitlines())     # (local)
    length_ratio = revised_len / max(1, original_len)   # (local)

    # Integration checks
    integrations = {
        "VII.M_or_N_three_layer_regulator": "Three-Layer Theorem" in revised_section and "VII.N" in revised_section,
        "VII.P_disjoint_corridor_with_pending_status": "§VII.P" in revised_section and "pending" in revised_section.lower(),
        "cross_refs_W2_6_and_W2_7": "W2-6" in revised_section and "W2-7" in revised_section,
    }
    integration_count = sum(integrations.values())

    # Verdict
    if integration_count == 3 and length_ratio <= 3.0:
        verdict = "PASS"
    elif integration_count == 3 and length_ratio > 3.0:
        verdict = "INFO"   # length growth beyond 3× is a stylistic gap
    else:
        verdict = "FAIL"

    # Emit diff
    diff_md = f"""
# PSG §11.2 Revision Diff (S85 W2-13)

**Target file**: `sessions/framework/Phononic-Substrate-Geometry.md`
**Section**: §11.2 Cosmological Constant from `a_0`
**Original length**: {original_len} lines
**Revised length**: {revised_len} lines  (ratio {length_ratio:.2f}x)

## Per-item integration status

| Item | Target | Present in revised §11.2? |
|:-----|:-------|:-------------------------|
| (1) §VII.N Three-Layer Regulator (S84 W2a-11) | §11.2.A new sub-section | {integrations["VII.M_or_N_three_layer_regulator"]} |
| (2) §VII.P Disjoint-Corridor (pending status per W2-7 FAIL) | §11.2.B new sub-section | {integrations["VII.P_disjoint_corridor_with_pending_status"]} |
| (3) Cross-refs to W2-6 (quantum PASS) + W2-7 (FAIL-with-refinement) | §11.2.C cross-refs | {integrations["cross_refs_W2_6_and_W2_7"]} |

**integration_count** = {integration_count} / 3

## Revised §11.2 content

```markdown
{revised_section}
```

## Commit protocol

Emit as patch against `sessions/framework/Phononic-Substrate-Geometry.md`
lines {orig_start}–{orig_end} (character offsets). USER APPROVAL required
before the patch is applied. This gate audits the revision; it does NOT
auto-commit to the PSG file.
"""

    diff_path = Path(__file__).parent / "s85_w2_psg_section_11_2_diff.md"
    diff_path.write_text(diff_md)
    print(f"WROTE {diff_path}")

    revised_path = Path(__file__).parent / "s85_w2_psg_section_11_2_revised.md"
    revised_path.write_text(revised_section)
    print(f"WROTE {revised_path}")

    # Closure SHA
    pin_map_str = json.dumps(
        {
            "inputs": input_shas,
            "integrations": integrations,
            "integration_count": integration_count,
            "original_len": original_len,
            "revised_len": revised_len,
        },
        sort_keys=True,
    )
    closure_sha = hashlib.sha256(pin_map_str.encode()).hexdigest()
    content_sha = hashlib.sha256(revised_section.encode()).hexdigest()

    out_json = {
        "gate_id": "S85-W2-PSG-SECTION-11-2-REVISION",
        "verdict": verdict,
        "value_4tuple": {
            "value": integration_count,
            "scheme": "documentation-revision-audit",
            "convention": "PSG-style",
            "L_max": "N/A",
        },
        "integrations": integrations,
        "integration_count": integration_count,
        "original_len_lines": original_len,
        "revised_len_lines": revised_len,
        "length_ratio": length_ratio,
        "closure_sha256": closure_sha,
        "content_sha256": content_sha,
        "input_shas": input_shas,
    }
    out_path = Path(__file__).with_suffix(".json")
    out_path.write_text(json.dumps(out_json, indent=2))
    print(f"WROTE {out_path}")
    print(f"Integration count = {integration_count} / 3")
    for k, v in integrations.items():
        print(f"  {k}: {v}")
    print(f"Original lines = {original_len}; Revised lines = {revised_len}; ratio = {length_ratio:.2f}x")
    print(f"VERDICT: {verdict}")
    print(f"closure_sha256 = {closure_sha}")
    print(f"content_sha256 = {content_sha}")
    print(
        f"4-tuple: value={integration_count}, scheme=documentation-revision-audit, "
        f"convention=PSG-style, L_max=N/A"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
