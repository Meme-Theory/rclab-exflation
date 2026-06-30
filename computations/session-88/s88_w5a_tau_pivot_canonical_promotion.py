#!/usr/bin/env python3
"""
S88 W5a-39 — S88-TAU-PIVOT-CANONICAL-CONSTANT-PROMOTION
=========================================================

Gate: S88-TAU-PIVOT-CANONICAL-CONSTANT-PROMOTION (trigger: AUDIT)
Wave: W5a (METHODOLOGY-class — canonical-constants promotion)
Plan: sessions/session-plan/session-88-plan-w5a.md §W5a-39

Pre-registered threshold (per session-88-plan-w5a.md §W5a-39 Field 9):
  PASS: (a) tau_pivot is in canonical_constants.py with substrate-first
        canonical value + PROVENANCE; (b) update_constant returned success;
        (c) sync audit passes; (d) verdict line appended.
  FAIL: SR Class-(f) D_max ≥ 3.0 detected.
  INFO: D_max ∈ [1.0, 3.0).

Class-(f) D_max evaluation (substitution chain):
  Definition 1: candidate_A = 0.198 (S87 W2-5.6 placeholder; explicit pin
                in computations/session-87/s87_w2_a4_a2_pivot_stationarity_pin.py
                line 33: "placeholder tau_pivot = 0.198 per plan §W2-5.6")
  Definition 2: candidate_B = 0.190 (S86 W4 P5 conservative pin; computations/
                session-86/s86_w4_p5_sector_2_k_invariant.py line 215:
                "tau_pivot is NOT in canonical_constants; we use tau_fold
                as the canonical slice")
  Definition 3: D_max = |log10(candidate_A / candidate_B)|
  Substitute:   D_max = |log10(0.198 / 0.190)| = |log10(1.04211)| = 0.01791
  Direction:    D_max ≈ 0.0179 < 0.1 → NO-ACTION band (within S82-class-(d)
                absorbable per epistemic-discipline.md §"Source Reconciliation")

Substrate-first reasoning (per phononic-framing.md §"IS Space, Not IN Space"):
  The substrate has ONE canonical Jensen-deformation slice — tau_fold = 0.190.
  "Pivot" is a CMB-observational concept (the k_pivot = 0.05 Mpc⁻¹ scale).
  At the substrate level, tau_pivot identifies with tau_fold under the bridge
  map. Therefore canonical = tau_fold = 0.190 (S86 W4 P5 lineage).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py (post-promotion)
  - sessions/session-plan/session-88-plan-w5a.md (plan source)
  - .claude/rules/methodology-wave-allowlist.md (allowlist row pin)
  - computations/session-87/s87_w2_a4_a2_pivot_stationarity_pin.py (candidate-A source)
  - computations/session-86/s86_w4_p5_sector_2_k_invariant.py (candidate-B source)
"""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
import time
from pathlib import Path

T0 = Path(__file__).resolve().parent
PROJECT_ROOT = T0.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# Pin metadata
GATE_ID = "S88-TAU-PIVOT-CANONICAL-CONSTANT-PROMOTION"
SCHEME = "canonical-promotion"
CONVENTION = "substrate-first-pin"
L_MAX = "N/A"  # (local)

# Class-(f) candidate values
CANDIDATE_A = 0.198  # (local) S87 W2-5.6 placeholder
CANDIDATE_B = 0.190  # (local) S86 W4 P5 conservative; = tau_fold
SUBSTRATE_CANONICAL = 0.190  # (local) substrate-first selection (= tau_fold)

# Files
SCRIPT_PATH = T0 / "s88_w5a_tau_pivot_canonical_promotion.py"
NPZ_OUT = T0 / "s88_w5a_tau_pivot_canonical_promotion.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

CANON_PY = SHARED_DIR / "canonical_constants.py"
ALLOWLIST_PATH = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w5a.md"
S87_W2_5_SCRIPT = PROJECT_ROOT / "computations" / "session-87" / "s87_w2_a4_a2_pivot_stationarity_pin.py"
S86_W4_P5_SCRIPT = PROJECT_ROOT / "computations" / "session-86" / "s86_w4_p5_sector_2_k_invariant.py"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def main() -> int:
    t_start = time.time()
    import numpy as np

    # ──────────────────────────────────────────────────────────────────
    # 1 — Substitution chain: D_max evaluation (Class-(f) classification)
    # ──────────────────────────────────────────────────────────────────
    d_max = abs(math.log10(CANDIDATE_A) - math.log10(CANDIDATE_B))
    print(f"[W5a-39] Substitution chain (D_max evaluation):")
    print(f"  Definition 1: candidate_A = {CANDIDATE_A} (S87 W2-5.6 placeholder)")
    print(f"  Definition 2: candidate_B = {CANDIDATE_B} (S86 W4 P5 conservative; = tau_fold)")
    print(f"  Substitute:   D_max = |log10({CANDIDATE_A}/{CANDIDATE_B})|")
    print(f"  Compute:      D_max = |log10({CANDIDATE_A/CANDIDATE_B:.5f})| = {d_max:.5f}")

    # 4-band Class-(f) classification per epistemic-discipline.md
    if d_max >= 3.0:
        d_band = "HARD-HALT"
    elif d_max >= 1.0:
        d_band = "MANDATORY"
    elif d_max >= 0.1:
        d_band = "ADVISORY"
    else:
        d_band = "NO-ACTION"
    print(f"[W5a-39] D_max band: {d_band} (NO-ACTION if < 0.1, ADVISORY ≥ 0.1, MANDATORY ≥ 1.0, HARD-HALT ≥ 3.0)")

    # ──────────────────────────────────────────────────────────────────
    # 2 — Verify post-promotion state in canonical_constants.py
    # ──────────────────────────────────────────────────────────────────
    canon_text = CANON_PY.read_text(encoding="utf-8", errors="replace")
    cc1_constant_present = bool(re.search(r"^tau_pivot\s*=\s*0\.190?\b", canon_text, re.MULTILINE))
    cc2_provenance_present = ("tau_pivot" in canon_text and "S88-TAU-PIVOT-CANONICAL-CONSTANT-PROMOTION" in canon_text)
    print(f"[W5a-39] CC1 tau_pivot = 0.190 in canonical_constants.py: {cc1_constant_present}")
    print(f"[W5a-39] CC2 PROVENANCE entry for S88-TAU-PIVOT-CANONICAL-CONSTANT-PROMOTION: {cc2_provenance_present}")

    # Try import-binding sanity check
    try:
        # Re-import to refresh module-level symbol after update
        import importlib
        import canonical_constants as _cc
        importlib.reload(_cc)
        tau_pivot_imported = _cc.tau_pivot
        cc3_import_works = (abs(tau_pivot_imported - SUBSTRATE_CANONICAL) < 1e-12)
        print(f"[W5a-39] CC3 import canonical_constants.tau_pivot = {tau_pivot_imported}: {cc3_import_works}")
    except Exception as e:
        cc3_import_works = False
        tau_pivot_imported = None
        print(f"[W5a-39] CC3 import canonical_constants.tau_pivot: FAILED ({e})")

    # ──────────────────────────────────────────────────────────────────
    # 3 — Allowlist check
    # ──────────────────────────────────────────────────────────────────
    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")
    cc_allowlist_w5a39 = ("| W5a-39 | S88 |" in allowlist_text
                          and "9dbbd9487253c397d0846e62767ddf8a1555158ffaaf0a54e08d9fa37b8594ac" in allowlist_text)
    print(f"[W5a-39] CC0 methodology-wave-allowlist W5a-39 row present: {cc_allowlist_w5a39}")

    # ──────────────────────────────────────────────────────────────────
    # 4 — Composite verdict per plan §W5a-39 Field 9
    # ──────────────────────────────────────────────────────────────────
    if d_band == "HARD-HALT":
        composite = "FAIL"
        verdict_kind = f"FAIL-D_max-{d_max:.4f}-HARD-HALT-band"
    elif d_band == "MANDATORY":
        composite = "INFO"
        verdict_kind = f"INFO-D_max-{d_max:.4f}-MANDATORY-pending-manual-review"
    elif (cc1_constant_present and cc2_provenance_present and cc3_import_works
          and cc_allowlist_w5a39 and d_band in {"NO-ACTION", "ADVISORY"}):
        composite = "PASS"
        verdict_kind = f"PASS-tau_pivot-{SUBSTRATE_CANONICAL}-canonical-promoted-D_max-{d_max:.4f}-{d_band}"
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-canonical-constants-missing-tau_pivot-or-allowlist-absent"

    print(f"[W5a-39] composite = {composite} (verdict_kind={verdict_kind})")

    # ──────────────────────────────────────────────────────────────────
    # 5 — Compute SHAs
    # ──────────────────────────────────────────────────────────────────
    canon_sha = sha256_file(CANON_PY)
    allowlist_sha = sha256_file(ALLOWLIST_PATH)
    plan_sha = sha256_file(PLAN_PATH)
    s87_w2_5_sha = sha256_file(S87_W2_5_SCRIPT) if S87_W2_5_SCRIPT.exists() else "MISSING"
    s86_w4_p5_sha = sha256_file(S86_W4_P5_SCRIPT) if S86_W4_P5_SCRIPT.exists() else "MISSING"
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "candidate_A": CANDIDATE_A,
        "candidate_B": CANDIDATE_B,
        "substrate_canonical": SUBSTRATE_CANONICAL,
        "d_max": d_max,
        "d_band": d_band,
        "input_canonical_constants_sha256": canon_sha,
        "input_allowlist_sha256": allowlist_sha,
        "input_plan_sha256": plan_sha,
        "input_s87_w2_5_script_sha256": s87_w2_5_sha,
        "input_s86_w4_p5_script_sha256": s86_w4_p5_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # ──────────────────────────────────────────────────────────────────
    # 6 — Save .npz
    # ──────────────────────────────────────────────────────────────────
    np.savez(
        NPZ_OUT,
        candidate_A=np.float64(CANDIDATE_A),
        candidate_B=np.float64(CANDIDATE_B),
        substrate_canonical=np.float64(SUBSTRATE_CANONICAL),
        d_max=np.float64(d_max),
        d_band=d_band,
        cc1_constant_present=np.bool_(cc1_constant_present),
        cc2_provenance_present=np.bool_(cc2_provenance_present),
        cc3_import_works=np.bool_(cc3_import_works),
        cc_allowlist_w5a39=np.bool_(cc_allowlist_w5a39),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    # ──────────────────────────────────────────────────────────────────
    # 7 — Append verdict trio
    # ──────────────────────────────────────────────────────────────────
    elapsed = time.time() - t_start
    value_str = (
        f"tau_pivot_canonical={SUBSTRATE_CANONICAL};"
        f"candidate_A={CANDIDATE_A};candidate_B={CANDIDATE_B};"
        f"d_max={d_max:.5f};d_band={d_band};"
        f"cc1_const={cc1_constant_present};cc2_prov={cc2_provenance_present};"
        f"cc3_import={cc3_import_works};cc_allowlist={cc_allowlist_w5a39};"
        f"verdict_kind={verdict_kind}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    sign_v = "N/A"
    mag_v = composite
    regime_v = "VALID"
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    print(f"[W5a-39] DONE in {elapsed:.2f}s")
    print(f"[W5a-39] audit_sha256   = {audit_sha256}")
    print(f"[W5a-39] content_sha256 = {content_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
