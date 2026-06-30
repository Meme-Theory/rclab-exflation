"""S98 verdict-file recovery merge (orchestrator-only, single-writer, race-free).

Context: a Windows cross-process O_APPEND race on s98_gate_verdicts.txt during the
8-concurrent-agent Batch-1 dispatch clobbered 5 gates' verdict rows (V.5/V.7/V.8/
V.9/V.11), leaving only V.1/V.3/V.6. Each clobbered agent was resumed by agentId and
re-emitted its EXACT original rows (verbatim bytes, original SHAs — no recompute) to a
private _recover_<gate>.txt file (race-free). This script merges those 5 private files
back into the canonical verdict file as a SINGLE serial write (the only writer now that
all agents are done), then audits all-8-present + sig_5 (audit_sha256 uniqueness).

This is verdict-RESTORATION (recovering agent-authored bytes lost to infrastructure),
NOT verdict-authoring: every audit_sha256/content_sha256 is the agent's original.
"""
import sys
from pathlib import Path
import re

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403 — registry-merge utility consumes no framework constants (project convention per computations/_shared/CLAUDE.md; mirrors s93_allowlist_append_helper.py)

BASE = Path(__file__).resolve().parent           # computations/session-98
MAIN = BASE / "s98_gate_verdicts.txt"

# All 8 Batch-1 gates + their original audit_sha256 (cross-validation pins).
EXPECTED = {
    "S98-W1-ROUTE-RECONCILIATION":        "75a45dd730aca2f94be4040ed6a69120dceb1efa893a5bd62659ea981c79e1b5",
    "S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN": "b8487bc838683800c96d0d9b16de327eaaafb54a29b5294f722f216c71315cb7",
    "S98-W4-4-OQ3-COVARIANCE":            "0814c57fe01d6aa85ffb0497e6c850f6af095d451d716fb99282d4277bc32fe1",
    "S98-HK-SIGMA8-CHANNEL-KEYED-PINS":   "e5e45620c3ff0b0fe524d9e3a15a3591b3010ecac941546f484774f77dfa9a79",
    "S98-W3-2-BARYOGEN-UNIQUENESS":       "3be22b8a1b9736dbd85dbd0c31fe83a68a805f3e15082573de7c5799c5c3875f",
    "S98-KAPPA-INDEP-FROM-CGWB-FREQ":     "10d31d0e8975bb866c13063c65d29652b94e67f1b7f030d5b60a42387912ac83",
    "S98-A0A2-TIER2-PV-INVARIANCE":       "4522ea7e56287415c925d6c2995fb9b4f38b01b5ee67f216417cf62540bc6306",
    "S98-MK3-1-C10-SUBLEADING-SIGN":      "0870e1a394e7f3240b5f982526eb5b455f6f6155411252b27532c70396246a83",
}

# The 5 private recovery files (the clobbered gates), with expected (gate_id, audit_sha).
RECOVERY = [
    ("_recover_v11_sigma8.txt",  "S98-HK-SIGMA8-CHANNEL-KEYED-PINS",   EXPECTED["S98-HK-SIGMA8-CHANNEL-KEYED-PINS"]),
    ("_recover_v5_baryogen.txt", "S98-W3-2-BARYOGEN-UNIQUENESS",       EXPECTED["S98-W3-2-BARYOGEN-UNIQUENESS"]),
    ("_recover_v7_kappa.txt",    "S98-KAPPA-INDEP-FROM-CGWB-FREQ",     EXPECTED["S98-KAPPA-INDEP-FROM-CGWB-FREQ"]),
    ("_recover_v8_pvinv.txt",    "S98-A0A2-TIER2-PV-INVARIANCE",       EXPECTED["S98-A0A2-TIER2-PV-INVARIANCE"]),
    ("_recover_v9_c10sign.txt",  "S98-MK3-1-C10-SUBLEADING-SIGN",      EXPECTED["S98-MK3-1-C10-SUBLEADING-SIGN"]),
]

CANON_RE = re.compile(r"^(S98-[A-Z0-9-]+): (PASS|FAIL|INFO) .* audit_sha256=([a-f0-9]{64})", re.M)


def main() -> int:
    main_txt = MAIN.read_text(encoding="utf-8")
    present_before = {m[0] for m in CANON_RE.findall(main_txt)}
    print("Gates present BEFORE merge:", sorted(present_before))

    to_append = []  # (local)
    for fname, gid, exp_audit in RECOVERY:
        blk = (BASE / fname).read_text(encoding="utf-8")
        if not blk.startswith(gid + ":"):
            raise SystemExit(f"FATAL: {fname} first line is not the {gid} canonical line")
        if f"audit_sha256={exp_audit}" not in blk:
            raise SystemExit(f"FATAL: {fname} missing expected audit_sha256={exp_audit[:16]}...")
        if gid in present_before:
            print(f"  SKIP {gid}: already in main (idempotent re-run)")
            continue
        if not blk.endswith("\n"):
            blk += "\n"
        to_append.append(blk)
        print(f"  QUEUED {gid} from {fname} (audit {exp_audit[:16]}..., {len(blk.splitlines())} rows)")

    if to_append:
        if not main_txt.endswith("\n"):
            main_txt += "\n"
        MAIN.write_text(main_txt + "".join(to_append), encoding="utf-8")  # single serial writer
        print(f"MERGED {len(to_append)} recovery blocks into {MAIN.name}")
    else:
        print("Nothing to merge (all gates already present).")

    # ---- Audit the merged file ----
    v = MAIN.read_text(encoding="utf-8")
    canon = CANON_RE.findall(v)
    gates_after = [c[0] for c in canon]
    shas = [c[2] for c in canon]

    print("\n==== POST-MERGE AUDIT ====")
    print("Canonical verdict lines:", len(canon))
    print("Distinct gates:", len(set(gates_after)))
    for gid, verdict, sha in canon:
        ok = "OK" if EXPECTED.get(gid) == sha else "SHA-MISMATCH"
        print(f"  {gid:38s} {verdict:5s} audit={sha[:16]}... [{ok}]")

    dupes = sorted({s for s in shas if shas.count(s) > 1})
    missing = sorted(set(EXPECTED) - set(gates_after))
    print("\nsig_5 (audit_sha256 uniqueness):", "CLEAN — no duplicates" if not dupes else f"VIOLATION: {dupes}")
    print("All-8-present:", "YES" if not missing else f"MISSING: {missing}")
    status = "RECOVERY-COMPLETE" if (not dupes and not missing) else "RECOVERY-INCOMPLETE"
    print(f"\nVERDICT-FILE-RECOVERY: {status}")
    return 0 if status == "RECOVERY-COMPLETE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
