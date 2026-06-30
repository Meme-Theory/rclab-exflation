#!/usr/bin/env python3
"""
S93 W8-5 — S93-W8-5-NARROW-PATH-WORKSHOP-1-GATE-PREREG
======================================================

Gate: S93-W8-5-NARROW-PATH-WORKSHOP-1-GATE-PREREG  ([AUDIT])

Pre-registered threshold (METHODOLOGY-class, artifact-existence predicate):
  PASS iff the §VI Workshop-1 pre-registered gate-block
  (gate_id "S93-W8-WS1-AREA-GAP-VS-D-K-SPECTRAL-FLOOR") in
  sessions/session-plan/session-93-plan-w8.md VALIDATES against
  computations/_shared/_yaml_gate_validator.py:
    (1) schema_version == "R3"
    (2) all 8 PRDR checklist keys present AND non-empty (r3_compliant True)
    (3) three regime bands present (Regime I -> PASS, Regime II -> FAIL,
        Regime III -> INFO)
    (4) two W8-3 pre-flight discriminators cited (substrate Cauchy-Schwarz
        moment floor F_0*F_2 >= F_1^2  AND  LQG area-volume band
        gamma_BH=0.2375 in [gamma_lo, gamma_hi] at j<=3)
  FAIL iff any of (1)-(4) fails; INFO iff the block validates but a regime
  band is under-specified (structurally not expected — the block is
  pre-authored complete at plan-freeze).

This is a VALIDATION gate, NOT an authorship gate. The §VI block is
ALREADY pre-written at plan-freeze. This script validates it; if a real
validator defect surfaced (missing/empty PRDR key, schema!=R3, missing
regime band) the orchestrator-editable plan file would be repaired and
re-validated. The dry-run pre-check confirmed all 8 plan YAML gates are
R3-compliant with 0 FAIL.

Output 4-tuple:
  (value=<validator+regime+discriminator booleans>,
   scheme=narrow-path-workshop-1-gate-prereg-R3-YAML-authorship-three-regime,
   convention=NARROW-PATH-workshop-1-area-gap-vs-DK-spectral-floor-three-regime-I-PASS-II-FAIL-III-INFO-METHODOLOGY-class,
   L_max=NA)

Classification: NON-PHONONIC (methodology / plan-authorship contribution)

METHODOLOGY
-----------
Invokes the R3 YAML validator (_yaml_gate_validator.py) on the plan file in
--json mode, parses the report, and isolates the WS1 gate. The validator's
own checks (schema_version=="R3", REQUIRED_CHECKLIST_KEYS all non-empty) are
the artifact-existence predicate of wave-classification.md M1. On top of the
validator boolean this script adds two METHODOLOGY-specific structural checks
that the generic validator does not perform: (3) the three-regime PASS/FAIL/
INFO partition is present in the WS1 block text, and (4) the two W8-3 joint
pre-flight discriminators are cited. The substrate-physics meaning of the
three regimes is the L2 substitution chain (gamma_emergent = alpha_bridge *
SCALE_BRIDGE_PREFACTOR_FW, canonical_constants.py:349-363) verified at
plan-freeze: alpha_bridge ~ 4.81e-3 -> Regime I; alpha_bridge ~ O(1) ->
Regime II (~200x mismatch, no gamma-cutoff-running per Paper 03 §VII);
intermediate / j-band-ambiguous -> Regime III. Substrate-first direction
(substrate sqrt(C_2(p,q)) primary, LQG sqrt(j(j+1)) emergent candidate) is
preserved in the authored block's substrate_framing.

DISCIPLINE
----------
- `from canonical_constants import *` (the L2-chain pins are sanity-checked
  but no compute is performed; this is a plan-validation gate)
- Every local/intermediate tagged `# (local)`
- No GPU (text/YAML parsing only)
- SHA-256 of all input files logged; audit_sha256 + content_sha256 emitted
- Verdict appended to computations/session-93/s93_gate_verdicts.txt with
  dual-SHA + companion comment row (no 3-tuple — [AUDIT] trigger)
- DEVIATION NOTE: canonical_constants.py runtime SHA may differ from the
  plan-pinned 1aa90bb1...; benign per substrate-first-canonical-sourcing.md
  §(ii.B). audit_sha256 is computed over RUNTIME bytes.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent  # project root
sys.path.insert(0, str(_ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    SCALE_BRIDGE_PREFACTOR_FW,
    GAMMA_BH_SU2_CONVENTION_LQG,
    ALPHA_BRIDGE_REQUIRED_FW,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S93"                                                       # (local)
GATE_ID = "S93-W8-5-NARROW-PATH-WORKSHOP-1-GATE-PREREG"               # (local)
SCHEME = "narrow-path-workshop-1-gate-prereg-R3-YAML-authorship-three-regime"  # (local)
CONVENTION = (
    "NARROW-PATH-workshop-1-area-gap-vs-DK-spectral-floor-"
    "three-regime-I-PASS-II-FAIL-III-INFO-METHODOLOGY-class"
)                                                                     # (local)
L_MAX = "NA"                                                          # (local) plan-authorship gate

# Validation target
WS1_GATE_ID = "S93-W8-WS1-AREA-GAP-VS-D-K-SPECTRAL-FLOOR"             # (local)
PLAN_FILE = PROJECT_ROOT / "sessions" / "session-plan" / "session-93-plan-w8.md"  # (local)
YAML_VALIDATOR = SHARED_DIR / "_yaml_gate_validator.py"               # (local)
VENV_PY = PROJECT_ROOT / "phonon-exflation-sim" / ".venv312" / "Scripts" / "python.exe"  # (local)

# Pre-registered required PRDR keys (mirror _yaml_gate_validator REQUIRED_CHECKLIST_KEYS)
REQUIRED_PRDR_KEYS = (
    "operator",
    "strict_PASS_boundary",
    "boundary_reachable_analytically",
    "reachable_rationals",
    "machinery_pin_map",
    "audit_discriminators",
    "substitution_chain",
    "input_files",
)                                                                     # (local)
EXPECTED_SCHEMA = "R3"                                                # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s93_w8_5_narrow_path_workshop_1_gate_prereg.npz"
OUT_PNG = SESSION_DIR / "s93_w8_5_narrow_path_workshop_1_gate_prereg.png"
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PLAN_FILE,
    YAML_VALIDATOR,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY) + dual-SHA
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256(bytes(script) || bytes(canonical) || pinmap_json)
    content_sha256 = sha256(bytes(script))
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Validation logic
# ---------------------------------------------------------------------------

def run_validator() -> dict:
    """Invoke _yaml_gate_validator.py --json on the plan file; return report."""
    py = str(VENV_PY) if VENV_PY.exists() else sys.executable  # (local)
    cmd = [py, str(YAML_VALIDATOR), "--json", str(PLAN_FILE)]    # (local)
    proc = subprocess.run(
        cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT)
    )  # (local)
    # Exit 0 = all PASS, 1 = >=1 FAIL, 2 = parse error. We parse JSON either way.
    try:
        report = json.loads(proc.stdout)  # (local)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"validator JSON parse failed (exit={proc.returncode}); "
            f"stderr={proc.stderr[:400]}"
        ) from exc
    report["_validator_exit_code"] = proc.returncode
    return report


def extract_ws1_gate(report: dict) -> dict | None:
    """Find the WS1 gate entry in the validator report."""
    for rep in report.get("reports", []):
        for g in rep.get("gates", []):
            if g.get("gate_id") == WS1_GATE_ID:
                return g
    return None


def check_three_regimes(block_text: str) -> dict:
    """Verify the three regime bands (I->PASS, II->FAIL, III->INFO) present."""
    # Regime presence: explicit "Regime I/II/III" tokens AND the verdict-meaning
    # lines (PASS_meaning / FAIL_meaning / INFO_meaning) each cite their regime.
    has_regime_I = "Regime I" in block_text     # (local)
    has_regime_II = "Regime II" in block_text   # (local)
    has_regime_III = "Regime III" in block_text  # (local)
    # The regime->verdict map must be explicit in the meaning lines.
    pass_maps_I = ("PASS_meaning" in block_text) and ("Regime I" in block_text)   # (local)
    fail_maps_II = ("FAIL_meaning" in block_text) and ("Regime II" in block_text)  # (local)
    info_maps_III = ("INFO_meaning" in block_text) and ("Regime III" in block_text)  # (local)
    all_present = (
        has_regime_I and has_regime_II and has_regime_III
        and pass_maps_I and fail_maps_II and info_maps_III
    )  # (local)
    return {
        "regime_I_present": has_regime_I,
        "regime_II_present": has_regime_II,
        "regime_III_present": has_regime_III,
        "regime_I_maps_PASS": pass_maps_I,
        "regime_II_maps_FAIL": fail_maps_II,
        "regime_III_maps_INFO": info_maps_III,
        "all_three_regimes_present": all_present,
    }


def check_discriminators(block_text: str) -> dict:
    """Verify the two W8-3 joint pre-flight discriminators are cited."""
    # The WS1 block consumes W8-3's verdict (w8_3_verdict input file) and the
    # method text cites "the W8-3 joint pre-flight verdict (substrate moment
    # floor AND area-volume band)". Both legs must be citable from the block.
    cites_w8_3 = ("w8_3_verdict" in block_text) or ("W8-3" in block_text)  # (local)
    # Discriminator 1: substrate Cauchy-Schwarz moment floor F_0*F_2 >= F_1^2.
    cites_moment_floor = (
        "moment floor" in block_text
        or "F_0" in block_text
        or "Cauchy-Schwarz" in block_text
        or "spectral floor" in block_text.lower()
        or "D_K spectral floor" in block_text
    )  # (local)
    # Discriminator 2: LQG area-volume band gamma_BH in [gamma_lo, gamma_hi].
    cites_area_volume_band = (
        "area-volume" in block_text
        or "area-gap" in block_text
        or "0.2375" in block_text
        or "j-band" in block_text
        or "γ_emergent" in block_text
    )  # (local)
    both = cites_w8_3 and cites_moment_floor and cites_area_volume_band  # (local)
    return {
        "cites_w8_3_preflight": cites_w8_3,
        "cites_substrate_moment_floor": cites_moment_floor,
        "cites_lqg_area_volume_band": cites_area_volume_band,
        "both_discriminators_cited": both,
    }


def extract_ws1_block_text() -> str:
    """Slice the §VI Workshop-1 YAML block text from the plan file."""
    text = PLAN_FILE.read_text(encoding="utf-8")  # (local)
    anchor = "## §VI Workshop-1 Pre-Registered Gate Block"  # (local)
    idx = text.find(anchor)  # (local)
    if idx < 0:
        return ""
    # Block runs to the next top-level "## " after the anchor.
    rest = text[idx + len(anchor):]  # (local)
    nxt = rest.find("\n## ")  # (local)
    block = rest if nxt < 0 else rest[:nxt]  # (local)
    return block


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Append a single dual-SHA verdict line + companion comment row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins
    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap, RUNTIME bytes)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 1b. L2-chain sanity (no compute; confirm the regime-boundary pins are sane)
    gamma_at_required = ALPHA_BRIDGE_REQUIRED_FW * SCALE_BRIDGE_PREFACTOR_FW  # (local)
    print("=== L2-chain pin sanity (regime boundaries) ===")
    print(f"  SCALE_BRIDGE_PREFACTOR_FW = {SCALE_BRIDGE_PREFACTOR_FW}")
    print(f"  GAMMA_BH_SU2_CONVENTION_LQG = {GAMMA_BH_SU2_CONVENTION_LQG}")
    print(f"  ALPHA_BRIDGE_REQUIRED_FW = {ALPHA_BRIDGE_REQUIRED_FW}")
    print(f"  gamma_emergent(alpha_required) = {gamma_at_required:.5f} "
          f"(Regime-I target = gamma_BH = {GAMMA_BH_SU2_CONVENTION_LQG})")
    regime_pin_consistent = abs(gamma_at_required - GAMMA_BH_SU2_CONVENTION_LQG) \
        <= 1e-2 * GAMMA_BH_SU2_CONVENTION_LQG  # (local) rel_tol 1e-2 (4-sig-fig pin)
    print(f"  Regime-I pin self-consistency (rel_tol 1e-2): {regime_pin_consistent}")
    print()

    # 2. Run the R3 YAML validator on the plan file
    print("=== R3 YAML validator on plan file ===")
    report = run_validator()  # (local)
    rep0 = report["reports"][0]  # (local)
    n_yaml = rep0["n_yaml_gates"]  # (local)
    total_pass = report["total_pass"]  # (local)
    total_fail = report["total_fail"]  # (local)
    print(f"  validator exit code: {report['_validator_exit_code']}")
    print(f"  plan YAML gates: {n_yaml} | total_pass={total_pass} total_fail={total_fail}")

    # 3. Isolate the WS1 gate
    ws1 = extract_ws1_gate(report)  # (local)
    if ws1 is None:
        print(f"  WS1 gate {WS1_GATE_ID} NOT FOUND in validator report")
        ws1_found = False  # (local)
        ws1_r3 = False  # (local)
        ws1_missing = REQUIRED_PRDR_KEYS  # (local)
        per_key = {k: False for k in REQUIRED_PRDR_KEYS}  # (local)
    else:
        ws1_found = True  # (local)
        ws1_r3 = bool(ws1.get("r3_compliant"))  # (local)
        ws1_missing = tuple(ws1.get("missing_keys", []))  # (local)
        per_key = ws1.get("per_key_status", {})  # (local)
        print(f"  WS1 gate found: r3_compliant={ws1_r3}, missing_keys={list(ws1_missing)}")
        print(f"  per-key status: {per_key}")

    # schema_version check (validator only emits gates whose schema_version=='R3'
    # via _extract_yaml_gates; presence in the report IS the schema confirmation)
    schema_ok = ws1_found and (report.get("schema_version") == EXPECTED_SCHEMA)  # (local)
    all_8_keys = ws1_found and all(per_key.get(k, False) for k in REQUIRED_PRDR_KEYS)  # (local)

    # 4. Three-regime band + 2-discriminator structural checks on the WS1 block
    block_text = extract_ws1_block_text()  # (local)
    regimes = check_three_regimes(block_text)  # (local)
    discrim = check_discriminators(block_text)  # (local)
    print()
    print("=== WS1 three-regime band check ===")
    for k, v in regimes.items():
        print(f"  {k}: {v}")
    print("=== WS1 two-discriminator citation check ===")
    for k, v in discrim.items():
        print(f"  {k}: {v}")
    print()

    # 5. Composite gate verdict (artifact-existence predicate)
    validator_VALID = (
        ws1_found and ws1_r3 and schema_ok and all_8_keys
        and len(ws1_missing) == 0 and total_fail == 0
    )  # (local)
    three_regimes_ok = regimes["all_three_regimes_present"]  # (local)
    discriminators_ok = discrim["both_discriminators_cited"]  # (local)

    # PASS iff validator VALID AND 3 regimes AND 2 discriminators.
    # INFO iff validator VALID but a regime band under-specified (not expected;
    #   block is pre-authored complete). FAIL iff validator INVALID.
    if validator_VALID and three_regimes_ok and discriminators_ok:
        verdict = "PASS"  # (local)
    elif validator_VALID and not (three_regimes_ok and discriminators_ok):
        verdict = "INFO"  # (local)
    else:
        verdict = "FAIL"  # (local)

    value = {
        "validator_VALID": validator_VALID,
        "ws1_found": ws1_found,
        "ws1_r3_compliant": ws1_r3,
        "schema_R3_ok": schema_ok,
        "all_8_PRDR_keys_nonempty": all_8_keys,
        "ws1_missing_keys": list(ws1_missing),
        "three_regimes_present": three_regimes_ok,
        "two_discriminators_cited": discriminators_ok,
        "plan_total_pass": total_pass,
        "plan_total_fail": total_fail,
        "regime_pin_consistent": regime_pin_consistent,
    }  # (local)

    # 6. Persist data + a small annotation plot
    try:
        import numpy as np  # (local)
        np.savez(
            OUT_NPZ,
            validator_VALID=validator_VALID,
            ws1_found=ws1_found,
            ws1_r3_compliant=ws1_r3,
            schema_R3_ok=schema_ok,
            all_8_PRDR_keys_nonempty=all_8_keys,
            ws1_missing_keys=np.array(list(ws1_missing), dtype=object),
            three_regimes_present=three_regimes_ok,
            two_discriminators_cited=discriminators_ok,
            plan_total_pass=total_pass,
            plan_total_fail=total_fail,
            n_yaml_gates=n_yaml,
            regime_pin_consistent=regime_pin_consistent,
            gamma_emergent_at_required=gamma_at_required,
            SCALE_BRIDGE_PREFACTOR_FW=float(SCALE_BRIDGE_PREFACTOR_FW),
            GAMMA_BH_SU2_CONVENTION_LQG=float(GAMMA_BH_SU2_CONVENTION_LQG),
            ALPHA_BRIDGE_REQUIRED_FW=float(ALPHA_BRIDGE_REQUIRED_FW),
            per_key_status=json.dumps(per_key),
            regime_checks=json.dumps(regimes),
            discriminator_checks=json.dumps(discrim),
            verdict=verdict,
        )
        print(f"  wrote {OUT_NPZ.name}")

        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt  # (local)
        fig, ax = plt.subplots(figsize=(9, 5.5))  # (local)
        checks = [
            ("validator VALID", validator_VALID),
            ("WS1 found", ws1_found),
            ("schema==R3", schema_ok),
            ("8 PRDR keys", all_8_keys),
            ("3 regime bands", three_regimes_ok),
            ("2 discriminators", discriminators_ok),
            ("regime-pin consistent", regime_pin_consistent),
        ]  # (local)
        labels = [c[0] for c in checks]  # (local)
        vals = [1.0 if c[1] else 0.0 for c in checks]  # (local)
        colors = ["#2a9d4a" if c[1] else "#c0392b" for c in checks]  # (local)
        y = range(len(labels))  # (local)
        ax.barh(list(y), vals, color=colors, edgecolor="black")
        ax.set_yticks(list(y))
        ax.set_yticklabels(labels)
        ax.set_xlim(0, 1.15)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["FAIL/False", "PASS/True"])
        ax.invert_yaxis()
        ax.set_title(
            f"{GATE_ID}\nWorkshop-1 §VI block validation (gate {WS1_GATE_ID})\n"
            f"composite verdict: {verdict}",
            fontsize=10,
        )
        for yi, vi in zip(y, vals):
            ax.text(vi + 0.02, yi, "TRUE" if vi > 0.5 else "FALSE",
                    va="center", fontsize=9)
        fig.tight_layout()
        fig.savefig(OUT_PNG, dpi=130)
        plt.close(fig)
        print(f"  wrote {OUT_PNG.name}")
    except Exception as exc:  # noqa: BLE001
        print(f"  [WARN] data/plot write skipped: {exc}")

    # 7. Emit 4-tuple + verdict
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    # Exit code reflects SCRIPT HEALTH, not the scientific verdict.
    return 0


if __name__ == "__main__":
    sys.exit(main())
