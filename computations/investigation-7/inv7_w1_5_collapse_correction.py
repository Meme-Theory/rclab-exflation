#!/usr/bin/env python3
"""
INV7-W1-5 collapse-consistency correction (Option-A supersede emission)
=======================================================================

The original INV7-W1-5 verdict line emitted composite=PASS on top of the 3-tuple
sign_verdict=FAIL / magnitude_verdict=PASS / regime_verdict=VALID. Per the pre-registered
deterministic collapse rule (gate-verdicts.md §"Composite-collapse rule"):

    elif sign_verdict == FAIL:
        composite = FAIL

so sign=FAIL forces composite=FAIL. The composite=PASS line violated the collapse contract.

PHYSICS CALL (per plan §W1-5 substitution-chain Step 4 + Operator-1 + Step 3): the pre-registered
sign-evaluation LOCUS is nu_r1 (the field-agnostic ring-scale threshold; Operator-1 reads
beta_2_FW(nu_r1) and Step 3 pre-registers the beta_2 EXCESS / Z>0 direction AT nu_r1 as the physical
content of the ring being real). At the computed nu_r1=+1.205 sigma the direction is NEGATIVE
(beta_2_FW=1 vs <beta_2_GRF>=561998; the framework field's strong f_NL skew has PERCOLATED the
sublevel set, beta_0_FW=1). That is a FAIL of the DIRECTIONAL pre-registration. Relocating the
sign-evaluation to the void-wall threshold nu=+0.685 (where the +1316 sigma excess IS the predicted
direction) to rescue a PASS would be a Class-3 post-hoc-semantics edit — DECLINED. The gate FAILs its
directional pre-registration; the Z=620.80 sigma magnitude (discriminating power), the f_NL=1.505-driven
distinctness, and the S43-distinctness ALL stand as the informative content (magnitude=PASS,
regime=VALID UNCHANGED).

This script recomputes a DISTINCT audit_sha256 (over its own bytes + canonical_constants +
the correction pinmap, which includes the superseded SHA) so the corrective line carries a fresh,
unique audit_sha256 per the Option-A protocol (v3-closure-recovery.md sig_5; the superseding line
MUST NOT reuse the superseded SHA). The original line is RETAINED on disk per absolute verdict
permanence.
"""
from __future__ import annotations

import sys
import json
import hashlib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
INV7_DIR = PROJECT_ROOT / "computations" / "investigation-7"

# canonical_constants import for compliance (this is a SHA-bookkeeping helper; no constants consumed)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import r1_first_sound_ring_Mpc as _r1_unused  # noqa: E402,F401  # (local) compliance-only

GATE_ID = "INV7-W1-5"
SUPERSEDED_AUDIT = "803abfbc6315166e452539ada9dfe7fd45e36f56122555f1d2e1d654dc3e4d2c"  # composite=PASS line
SUPERSEDED_CONTENT = "cf1969c735f3fbaf83db153f3009c13e6d53616602628eb437b450cf381f3590"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def main() -> int:
    script_path = Path(__file__).resolve()                  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    original_npz = INV7_DIR / "inv7_w1_5_persistent_homology_ring.npz"  # (local)

    # input-pin map for the CORRECTION (distinct from the original gate's pinmap because it pins the
    # superseded SHA + the correction script bytes) -> yields a DISTINCT audit_sha256.
    pins = {  # (local)
        "computations/_shared/canonical_constants.py": sha256_of(canonical_path),
        "computations/investigation-7/inv7_w1_5_persistent_homology_ring.npz": sha256_of(original_npz),
        "computations/investigation-7/inv7_w1_5_collapse_correction.py": sha256_of(script_path),
        "supersedes_audit_sha256": SUPERSEDED_AUDIT,
        "correction_reason": "collapse-rule: sign_verdict==FAIL => composite=FAIL (was PASS)",
    }
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_path.read_bytes())
    h_audit.update(canonical_path.read_bytes())
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_path.read_bytes())
    content_sha = h_content.hexdigest()  # (local)

    print(f"=== {GATE_ID} collapse-correction SHAs ===")
    print(f"  superseded audit_sha256:  {SUPERSEDED_AUDIT}")
    print(f"  NEW corrective audit_sha256:   {audit_sha}")
    print(f"  NEW corrective content_sha256: {content_sha}")
    print(f"  distinct from superseded? audit={audit_sha != SUPERSEDED_AUDIT} "
          f"content={content_sha != SUPERSEDED_CONTENT}")

    payload = {  # (local)
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    print("<<<CORRECTION_SHAS>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_CORRECTION_SHAS>>>")
    return 0


if __name__ == "__main__":
    sys.exit(main())
