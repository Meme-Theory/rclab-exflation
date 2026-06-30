"""S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION  (path-B cross-link emission).

Plan §W8-98 — gate `S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION`.

Pre-registered method (plan §W8-98 step 1):

    1. At runtime, check trigger conditions on s88_gate_verdicts.txt:
       - If §W8-93 PASS  -> path-A: re-run CF-29 partition test using cell-phase
                            realisation output from #93.
       - Else if §W8-89 PASS + §W8-90 PASS -> path-B: CF-29 already classified
                            via partition criterion at #90; emit verdict
                            cross-link to #90.
       - Else -> PRE-REG-INC (both pathways blocked).
    2. Producing script: this file. Branches on trigger condition.
    3. Path-A: not executed in this run.
    4. Path-B: emit cross-link verdict citing #90 partition tags directly.

UPSTREAM TRIGGER MAP (verified on disk by trigger-validation step):

    §W8-93  S88-TYPE-F-ANTISYMMETRIC-CELL-PHASE-RETRY              FAIL  (drift 14.11% > 1%)
    §W8-89  S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE
                                                                   PASS canonical
                                                                   (audit_sha 1ebc28f3ab71fba3...)
    §W8-90  S88-CF-29-SUBSTANTIVE-RUN-VIA-PARTITION-CRITERION-ONLY PASS canonical (post-Option-A)
                                                                   (audit_sha dfff27f73a658ae5...)
                                                                   tags = (Type-F-M3, Type-S, Type-F-C)

    Substitution chain for path selection:
      T_A   := §W8-93 verdict       = FAIL  -> path-A CLOSED
      T_B   := §W8-89 PASS AND §W8-90 PASS  = PASS -> path-B ACTIVATED
      branch -> path-B  (per plan §W8-98 step 1 second branch)

Carve-out invocation (inherited from #90 per `mechanical-closure-discipline.md`
§"Layer-separability carve-out (admissible-with-conditions)"):
  - L1 layer-decomposition       : structurally inherited from #90
  - L2 closed-form mechanical    : inherited (single-pass Tr_alpha at bit precision)
  - L3 algebra-axis orthogonality: inherited (K=3 MANDATORY at S87 W-2 close)
  - L4 in-script honesty         : convention tag carries the
                                   `LAYER-SEPARABLE-CARVE-OUT-TYPE-F` suffix on
                                   the canonical verdict line (this script).

ENVIRONMENT
-----------
Python: phonon-exflation-sim/.venv312/Scripts/python.exe
GPU   : NOT USED (path-B is a cross-link emission; no linear algebra).
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

# Add the canonical_constants module to path BEFORE importing it.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    Delta_BCS,
    Vol_SU3_Haar,
    c_sub_baseline,
    r_PathH,
)


# =============================================================================
# Pinned identifiers (PRE-REGISTERED at plan-freeze; read-only)
# =============================================================================
GATE_ID = "S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION"
WP_ID = "W8-98"
SCHEME = "trigger-conditional-path-A-cell-phase-or-path-B-substantive-carve-out"
CONVENTION = (
    "Type-F-tag-emission-on-three-observables-LAYER-SEPARABLE-CARVE-OUT-TYPE-F"
)
L_MAX_PIN = 10  # (local) inherited from §W8-90 plan §W8-98 ref pin
PARTITION_TOL = 1e-12  # (local) inherited reference value from #90

VERDICT_PATH = (
    PROJECT_ROOT / "computations" / "session-88" / "s88_gate_verdicts.txt"
)
NPZ_OUT = (
    PROJECT_ROOT / "computations" / "session-88" / "s88_w8_cf29_resume.npz"
)
WP_PATH = (
    PROJECT_ROOT
    / "sessions"
    / "session-88"
    / "session-88-w8-workingpaper.md"
)
UPSTREAM_NPZ = (
    PROJECT_ROOT
    / "computations"
    / "session-88"
    / "s88_w8_cf29_partition_classify.npz"
)


# =============================================================================
# SHA helpers
# =============================================================================
def sha256_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def closure_hash(pinmap: dict) -> str:
    canon = json.dumps(pinmap, sort_keys=True, separators=(",", ":"))
    return sha256_str(canon)


# =============================================================================
# Trigger-condition validation (grep on disk; the PRE-REGISTERED branch decision)
# =============================================================================
W8_93_GATE_ID = "S88-TYPE-F-ANTISYMMETRIC-CELL-PHASE-RETRY"
W8_89_GATE_ID = (
    "S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE"
)
W8_90_GATE_ID = "S88-CF-29-SUBSTANTIVE-RUN-VIA-PARTITION-CRITERION-ONLY"


def _parse_canonical_lines(verdict_text: str, gate_id: str) -> list[dict]:
    """Return all canonical verdict-line records for the named gate_id.

    Companion comment rows (lines beginning '#') are filtered out.
    """
    out: list[dict] = []
    for ln in verdict_text.splitlines():
        if not ln.startswith(gate_id + ":"):
            continue
        verdict_match = re.match(
            rf"^{re.escape(gate_id)}:\s+(PASS|FAIL|INFO)\s+--\s+(.*)$", ln
        )
        if verdict_match is None:
            continue
        verdict = verdict_match.group(1)
        rest = verdict_match.group(2)
        audit_match = re.search(r"audit_sha256=([0-9a-fA-F]{64})", rest)
        content_match = re.search(r"content_sha256=([0-9a-fA-F]{64})", rest)
        out.append(
            {
                "line_text": ln,
                "verdict": verdict,
                "audit_sha256": audit_match.group(1) if audit_match else None,
                "content_sha256": (
                    content_match.group(1) if content_match else None
                ),
            }
        )
    return out


def _canonical_record_for(verdict_text: str, gate_id: str) -> dict:
    """Return the canonical (latest non-superseded) record for gate_id.

    For pre-W8-100 corrective emissions the latest PASS line is canonical
    per `gate-verdicts.md` Option A rule (6) retroactive canonicalization.
    """
    records = _parse_canonical_lines(verdict_text, gate_id)
    if not records:
        return {"verdict": None, "audit_sha256": None, "content_sha256": None}
    # Pre-W8-100 corrective-emission convention: latest PASS line is canonical.
    pass_records = [r for r in records if r["verdict"] == "PASS"]
    if pass_records:
        return pass_records[-1]
    return records[-1]


def validate_trigger_conditions() -> dict:
    """Validate plan §W8-98 step 1 trigger conditions on disk."""
    verdict_text = VERDICT_PATH.read_text(encoding="utf-8")

    rec_93 = _canonical_record_for(verdict_text, W8_93_GATE_ID)
    rec_89 = _canonical_record_for(verdict_text, W8_89_GATE_ID)
    rec_90 = _canonical_record_for(verdict_text, W8_90_GATE_ID)

    # Path-A predicate: §W8-93 PASS
    path_a_active = rec_93["verdict"] == "PASS"
    # Path-B predicate: §W8-89 PASS AND §W8-90 PASS (canonical)
    path_b_active = (
        rec_89["verdict"] == "PASS" and rec_90["verdict"] == "PASS"
    )

    if path_a_active:
        branch = "path-A"
    elif path_b_active:
        branch = "path-B"
    else:
        branch = "PRE-REG-INC"

    return {
        "branch": branch,
        "path_a_active": path_a_active,
        "path_b_active": path_b_active,
        "rec_W8_93": rec_93,
        "rec_W8_89": rec_89,
        "rec_W8_90": rec_90,
    }


# =============================================================================
# Path-B cross-link emission
# =============================================================================
def main() -> int:
    print(f"[gate]   {GATE_ID}")
    print(f"[plan]   sessions/session-plan/session-88-plan-w8.md §W8-98")
    print(f"[wp]     sessions/archive/session-88/session-88-w8-workingpaper.md")
    print(f"[utc]    {datetime.now(timezone.utc).isoformat()}")
    print()

    # ---- Step 1: validate trigger conditions on disk -----------------------
    trig = validate_trigger_conditions()
    print("[trigger-condition validation]")
    print(
        f"  §W8-93  ({W8_93_GATE_ID}): "
        f"{trig['rec_W8_93']['verdict']}  "
        f"audit_sha={trig['rec_W8_93']['audit_sha256']}"
    )
    print(
        f"  §W8-89  ({W8_89_GATE_ID}): "
        f"{trig['rec_W8_89']['verdict']}  "
        f"audit_sha={trig['rec_W8_89']['audit_sha256']}"
    )
    print(
        f"  §W8-90  ({W8_90_GATE_ID}): "
        f"{trig['rec_W8_90']['verdict']}  "
        f"audit_sha={trig['rec_W8_90']['audit_sha256']}"
    )
    print(f"  -> branch: {trig['branch']}")
    print()

    # Plan §W8-98 step 1 second branch: path-B activated when §W8-89 PASS AND
    # §W8-90 PASS. The orchestrator-verified trigger map (FAIL, PASS, PASS)
    # selects path-B by construction; if any other branch is observed at
    # runtime, abort with FAIL -- not because of physics but because the
    # trigger map this dispatch was authorized for is no longer the same.
    if trig["branch"] != "path-B":
        print(f"[ERROR] expected branch=path-B; got branch={trig['branch']}")
        print("        this dispatch is authorized only for path-B emission.")
        sys.exit(2)

    # ---- Step 2: load upstream §W8-90 NPZ canonical row --------------------
    upstream_data = np.load(UPSTREAM_NPZ, allow_pickle=True)
    obs_arr = upstream_data["observables"]
    tags_arr = upstream_data["per_observable_tag"]
    composite_str = str(upstream_data["composite"])
    upstream_verdict = str(upstream_data["verdict"])
    upstream_scheme = str(upstream_data["scheme"])
    upstream_convention = str(upstream_data["convention"])
    upstream_L_max = int(upstream_data["L_max"])
    upstream_partition_tol = float(upstream_data["partition_tol"])
    upstream_cache_sha = str(upstream_data["cache_sha256"])
    upstream_n_eig = int(upstream_data["n_eigenvalues"])
    upstream_n_sectors = int(upstream_data["n_sectors_kept"])

    print("[upstream §W8-90 canonical row]")
    print(f"  npz       : {UPSTREAM_NPZ.relative_to(PROJECT_ROOT)}")
    print(f"  npz_sha256: {sha256_file(UPSTREAM_NPZ)}")
    print(f"  L_max     : {upstream_L_max}")
    print(f"  scheme    : {upstream_scheme}")
    print(f"  convention: {upstream_convention}")
    print(f"  observables: {list(obs_arr)}")
    print(f"  tags      : {list(tags_arr)}")
    print(f"  composite : {composite_str}")
    print(f"  verdict   : {upstream_verdict}")
    print()

    # The post-Option-A canonical record on disk for §W8-90 is the second
    # PASS line (BCS=Type-S). Verify the upstream NPZ matches that canonical
    # record's audit_sha by direct cross-link.
    canonical_w8_90_audit_sha = trig["rec_W8_90"]["audit_sha256"]
    canonical_w8_90_content_sha = trig["rec_W8_90"]["content_sha256"]
    print("[cross-link to canonical §W8-90 verdict-line]")
    print(f"  audit_sha256   : {canonical_w8_90_audit_sha}")
    print(f"  content_sha256 : {canonical_w8_90_content_sha}")
    print()

    # ---- Step 3: build per-observable cross-link tag map -------------------
    per_observable_tag_xlink = {}
    for obs, tag in zip(obs_arr, tags_arr):
        per_observable_tag_xlink[str(obs)] = str(tag)

    expected_tags = {
        "LEGGETT_MOMENT_S70": "Type-F-M3",
        "PILLAR_III_BCS": "Type-S",
        "PILLAR_VI_As_ns": "Type-F-C",
    }
    cross_link_consistent = (
        per_observable_tag_xlink == expected_tags
        and upstream_verdict == "PASS"
        and canonical_w8_90_audit_sha
        == "dfff27f73a658ae595215b6b9e6c284b2c4f750d149814c25106d759f20d5137"
    )
    print(f"[cross-link consistency check] {cross_link_consistent}")
    print(
        f"  expected tags  : LEGGETT_MOMENT_S70=Type-F-M3, "
        f"PILLAR_III_BCS=Type-S, PILLAR_VI_As_ns=Type-F-C"
    )
    print(f"  observed tags  : {per_observable_tag_xlink}")
    print()

    # Plan §W8-98 PASS predicate (path-B branch):
    #   "cross-link verdict consistent with #90 tags"
    if cross_link_consistent:
        verdict = "PASS"
    else:
        verdict = "FAIL"

    # ---- Step 4: emit cross-link composite value ---------------------------
    composite_value = (
        f"trigger-branch=path-B;"
        f"xlink_W8_90_audit_sha={canonical_w8_90_audit_sha};"
        f"Type-F-tag(LEGGETT)={per_observable_tag_xlink['LEGGETT_MOMENT_S70']};"
        f"Type-F-tag(BCS)={per_observable_tag_xlink['PILLAR_III_BCS']};"
        f"Type-F-tag(A_s_n_s)={per_observable_tag_xlink['PILLAR_VI_As_ns']}"
    )

    # ---- Step 5: dual-SHA + verdict line append ----------------------------
    pinmap = {
        "_gate_id": GATE_ID,
        "_wp_id": WP_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX_PIN,
        "trigger_branch": "path-B",
        "upstream_W8_93_verdict": trig["rec_W8_93"]["verdict"],
        "upstream_W8_93_audit_sha": trig["rec_W8_93"]["audit_sha256"],
        "upstream_W8_89_verdict": trig["rec_W8_89"]["verdict"],
        "upstream_W8_89_audit_sha": trig["rec_W8_89"]["audit_sha256"],
        "upstream_W8_90_verdict": trig["rec_W8_90"]["verdict"],
        "upstream_W8_90_audit_sha": trig["rec_W8_90"]["audit_sha256"],
        "upstream_W8_90_content_sha": trig["rec_W8_90"]["content_sha256"],
        "upstream_npz_sha256": sha256_file(UPSTREAM_NPZ),
        "upstream_cache_sha256": upstream_cache_sha,
        "upstream_n_eigenvalues": upstream_n_eig,
        "upstream_n_sectors_kept": upstream_n_sectors,
        "upstream_partition_tol": upstream_partition_tol,
        "upstream_scheme": upstream_scheme,
        "upstream_convention": upstream_convention,
        "M_KK": M_KK,
        "tau_fold": tau_fold,
        "Delta_BCS": Delta_BCS,
        "Vol_SU3_Haar": Vol_SU3_Haar,
        "c_sub_baseline": c_sub_baseline,
        "r_PathH": r_PathH,
        "tag_LEGGETT": per_observable_tag_xlink["LEGGETT_MOMENT_S70"],
        "tag_BCS": per_observable_tag_xlink["PILLAR_III_BCS"],
        "tag_AS_NS": per_observable_tag_xlink["PILLAR_VI_As_ns"],
        "cross_link_consistent": bool(cross_link_consistent),
        "verdict": verdict,
    }
    audit_sha = closure_hash(pinmap)
    content_payload = json.dumps(
        {
            "gate_id": GATE_ID,
            "trigger_branch": "path-B",
            "tags_xlink": per_observable_tag_xlink,
            "xlink_W8_90_audit_sha": canonical_w8_90_audit_sha,
            "xlink_W8_90_content_sha": canonical_w8_90_content_sha,
            "cross_link_consistent": bool(cross_link_consistent),
            "composite": composite_value,
            "verdict": verdict,
        },
        sort_keys=True,
    )
    content_sha = sha256_str(content_payload)

    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{composite_value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_PIN} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+"
    )
    companion_line = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]} "
        f"# path-B cross-link to §W8-90 canonical "
        f"(audit_sha256={canonical_w8_90_audit_sha[:16]}...); "
        f"trigger_branch=path-B; "
        f"upstream §W8-93 FAIL (drift 14.11%) -> path-A CLOSED; "
        f"upstream §W8-89 PASS + §W8-90 PASS -> path-B activated; "
        f"computed by computations/session-88/s88_w8_cf29_resume.py"
    )

    VERDICT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not VERDICT_PATH.exists():
        VERDICT_PATH.write_text("", encoding="utf-8")
    with VERDICT_PATH.open("a", encoding="utf-8") as fh:
        fh.write(canonical_line + "\n")
        fh.write(companion_line + "\n")

    print("[verdict emission]")
    print(f"  verdict        : {verdict}")
    print(f"  audit_sha256   : {audit_sha}")
    print(f"  content_sha256 : {content_sha}")
    print(f"  canonical_line : {canonical_line}")
    print(f"  companion_line : {companion_line}")
    print()

    # ---- Step 6: emit npz sidecar -----------------------------------------
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        wp_id=WP_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX_PIN,
        trigger_branch="path-B",
        path_a_active=trig["path_a_active"],
        path_b_active=trig["path_b_active"],
        upstream_W8_93_audit_sha=str(trig["rec_W8_93"]["audit_sha256"]),
        upstream_W8_89_audit_sha=str(trig["rec_W8_89"]["audit_sha256"]),
        upstream_W8_90_audit_sha=str(trig["rec_W8_90"]["audit_sha256"]),
        upstream_W8_93_verdict=str(trig["rec_W8_93"]["verdict"]),
        upstream_W8_89_verdict=str(trig["rec_W8_89"]["verdict"]),
        upstream_W8_90_verdict=str(trig["rec_W8_90"]["verdict"]),
        observables=np.array(list(obs_arr), dtype="U32"),
        per_observable_tag_xlink=np.array(
            [
                per_observable_tag_xlink["LEGGETT_MOMENT_S70"],
                per_observable_tag_xlink["PILLAR_III_BCS"],
                per_observable_tag_xlink["PILLAR_VI_As_ns"],
            ],
            dtype="U16",
        ),
        composite=composite_value,
        cross_link_consistent=bool(cross_link_consistent),
        verdict=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        upstream_npz_sha256=sha256_file(UPSTREAM_NPZ),
        upstream_cache_sha256=upstream_cache_sha,
        upstream_n_eigenvalues=upstream_n_eig,
        upstream_n_sectors_kept=upstream_n_sectors,
        upstream_partition_tol=upstream_partition_tol,
        M_KK=M_KK,
        tau_fold=tau_fold,
        Delta_BCS=Delta_BCS,
        Vol_SU3_Haar=Vol_SU3_Haar,
        c_sub_baseline=c_sub_baseline,
        r_PathH=r_PathH,
    )
    print(f"  npz -> {NPZ_OUT.relative_to(PROJECT_ROOT)}")
    print()

    print("[done] path-B cross-link emission complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
