"""
S86 W10-3 — S86-MU-BC-V2-HEAT-KERNEL-DIAGNOSTIC (C39)

Gate: S86-MU-BC-V2-HEAT-KERNEL-DIAGNOSTIC ([AUDIT])
Classification: META (audit-class diagnostic of a prior computation's return value)
Trigger: [AUDIT] — diagnose what numerical value 0.15267 represents in the
         W9-5 V.2 heat-kernel attempt at deriving mu_BC integer-12 exponent.

Source under audit:
    computations/session-85/s85_w0_d_spec_alt_derivations.py
    Verdict line (s85_gate_verdicts.txt:106):
      S85-D_SPEC-ALT-DERIVATION-PATH: FAIL -- value=0.15267275677455985
        scheme=heat-kernel-Seeley-DeWitt convention=MS-bar L_max=8
        audit_sha256=db8e35... content_sha256=22ab12...

Hypothesis (per plan §W10-3 §5):
    V_W95 = 0.15267 is plausibly a normalized Seeley-DeWitt coefficient at
    4D weight with integer prefactor (candidate: 24·1/(4π)² = 0.15198, where
    24 = 2·dim(H_F^quark)). V.2 sampled the wrong substrate-spectral weight.

Method (per plan §W10-3 §6):
    Step 1: Catalogue candidate SD coefficient values (numerical table).
    Step 2: Compare V_W95 against catalogue at rel_err ≤ 1e-3 (PASS-strict)
            and ≤ 1e-2 (PASS-loose / INFO).
    Step 3: Identify substrate-spectral weight n ∈ {2, 4, 6, 8} of the match.
    Step 4: State whether 0.15267 is an SD coefficient at any standard weight.
    Step 5: Pre-register corrected weight for S87 carry-forward.

PASS/FAIL/INFO thresholds (plan §9):
    PASS: unique match at rel_err ≤ 1e-3, weight identified, mismatch with
          integer-12 documented.
    INFO: match in (1e-3, 1e-2], identification plausible but not unique
          OR not at strict precision.
    FAIL: no candidate matches within rel_err ≤ 1e-2.

Substitution chain (plan §10): see SECTION 6 below; verified line-by-line.

Per .claude/rules/regulator-pin-discipline.md: this audit cites a_2 and a_4
under the ζ regulator (a_2^{ζ}, a_4^{ζ}), inheriting from the S85 W0-9
producing script's MS-bar / heat-kernel-Seeley-DeWitt convention.
"""

# ---------------------------------------------------------------------------
# Section 1 — Imports + environment
# ---------------------------------------------------------------------------
from __future__ import annotations

import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

# Canonical constants (MANDATORY per .claude/rules/math-scripts.md)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "computations"))
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_Z,
    M_KK,
)


# ---------------------------------------------------------------------------
# Section 2 — Pre-registration constants (plan §7 machinery pin)
# ---------------------------------------------------------------------------
SESSION = "S86"                                                  # (local)
GATE_ID = "S86-MU-BC-V2-HEAT-KERNEL-DIAGNOSTIC"                  # (local)
SCHEME = "heat-kernel-diagnostic"                                # (local)
CONVENTION = "W9-5-V.2-input-audit"                              # (local)
L_MAX = 10                                                       # (local) plan §7 inherits W9-5 V.2 weight axis
SCHEMA_VERSION = "S84+"                                          # (local)

# V.2 return value (audit input — fixed)
V_W95 = 0.15267275677455985                                      # (local) full precision from S85 verdict
V_W95_ROUND = 0.15267                                            # (local) plan-text-rounded form

# Thresholds (plan §9)
PASS_RATIO_STRICT = 1e-3                                         # (local) PASS-strict
INFO_RATIO_LOOSE = 1e-2                                          # (local) loose / INFO band upper

# Candidate weight axis (plan §7)
CANDIDATE_WEIGHTS = [2, 4, 6, 8]                                 # (local) substrate-spectral weights


# ---------------------------------------------------------------------------
# Section 3 — Output paths
# ---------------------------------------------------------------------------
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
OUT_JSON = resolve_output(86, 's86_w10_mu_bc_heat_kernel_diagnostic.json')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

# Files whose SHA-256 we pin (input audit chain)
V2_SOURCE_SCRIPT = resolve_script(85, 's85_w0_d_spec_alt_derivations.py')
V2_DATA_NPZ = resolve_output(85, 's85_w0_d_spec_alt_derivations.npz')
V2_VERDICT_FILE = resolve_output(85, 's85_gate_verdicts.txt')
CANONICAL_CONSTANTS = resolve_script(None, 'canonical_constants.py')
SCRIPT_PATH = Path(__file__).resolve()


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 pinning utilities (W9a-99 dual-SHA template)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string if missing."""
    if not path.exists():
        return ""
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    """SHA-256 of a UTF-8 string."""
    h = hashlib.sha256()
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def grep_v2_verdict_line(verdict_path: Path) -> tuple[str, str]:
    """Return (full verdict line text, sha256 of just that line)."""
    if not verdict_path.exists():
        return ("", "")
    needle = "S85-D_SPEC-ALT-DERIVATION-PATH"                    # (local)
    for line in verdict_path.read_text(encoding="utf-8").splitlines():
        if line.startswith(needle + ":"):
            return (line, sha256_of_text(line))
    return ("", "")


# ---------------------------------------------------------------------------
# Section 5 — Candidate Seeley-DeWitt coefficient catalogue (plan §10 Def 2)
# ---------------------------------------------------------------------------
# Each candidate is a (label, value, weight_n, normalization_class) tuple.
# weight_n is the substrate-spectral weight (∈ {2, 4, 6, 8} or None for non-SD).
# normalization_class records the (4π)^k denominator structure.
def build_candidate_catalogue() -> list[dict]:
    """Compile the candidate SD coefficient catalogue.

    Includes:
      - Pure normalization constants 1/(4π)^k for k ∈ {1, 2, 4}
      - Integer-prefactor variants n/(4π)^2 for n ∈ {1, 6, 8, 12, 16, 24, 32}
        (the candidate flagged in plan §10 Step A is n=24)
      - Integer-prefactor variants n/(4π)^4 for n ∈ {1, 12, 24}
      - Canonical a_n(fold) values from baseline-findings-s66 (a_2, a_4)
        normalized at 4D and 8D heat-kernel prefactors
      - tau_fold-ratio variants
    """
    cands: list[dict] = []                                       # (local)
    pi4_2 = (4.0 * math.pi) ** 2                                 # (local) (4π)^2
    pi4_4 = (4.0 * math.pi) ** 4                                 # (local) (4π)^4
    pi2_2 = (2.0 * math.pi) ** 2                                 # (local) (2π)^2
    pi4_1 = 4.0 * math.pi                                        # (local) 4π

    # ----- Pure 1/(4π)^k normalizations (NO integer prefactor) -----
    cands.append(dict(label="1/(4π)²", value=1.0 / pi4_2,
                      weight_n=4, norm_class="4D-pure"))
    cands.append(dict(label="1/(2π)²", value=1.0 / pi2_2,
                      weight_n=None, norm_class="alt-2π"))
    cands.append(dict(label="1/(4π)",  value=1.0 / pi4_1,
                      weight_n=None, norm_class="sqrt-coef"))
    cands.append(dict(label="1/(4π)⁴", value=1.0 / pi4_4,
                      weight_n=8, norm_class="8D-pure"))

    # ----- Integer-prefactor n/(4π)² (4D weight) -----
    for n in [1, 6, 8, 12, 16, 24, 32]:
        cands.append(dict(label=f"{n}/(4π)²",
                          value=float(n) / pi4_2,
                          weight_n=4,
                          norm_class=f"4D-int-{n}"))

    # ----- Integer-prefactor n/(4π)⁴ (8D weight, cone-apex) -----
    for n in [1, 12, 24]:
        cands.append(dict(label=f"{n}/(4π)⁴",
                          value=float(n) / pi4_4,
                          weight_n=8,
                          norm_class=f"8D-int-{n}"))

    # ----- Canonical a_n(fold) values (baseline-findings-s66) -----
    a2_fold = 2776.17                                            # (local) a_2^{ζ}(fold)
    a4_fold = 1350.72                                            # (local) a_4^{ζ}(fold)
    cands.append(dict(label="a_2(fold)/(4π)⁴",
                      value=a2_fold / pi4_4,
                      weight_n=8,
                      norm_class="a2-8D"))
    cands.append(dict(label="a_4(fold)/(4π)⁴",
                      value=a4_fold / pi4_4,
                      weight_n=8,
                      norm_class="a4-8D"))
    cands.append(dict(label="a_2(fold)/(4π)²",
                      value=a2_fold / pi4_2,
                      weight_n=4,
                      norm_class="a2-4D-mix"))

    # ----- tau_fold-ratio variants -----
    cands.append(dict(label="tau_fold/(4π)²",
                      value=tau_fold / pi4_2,
                      weight_n=None,
                      norm_class="tau-mix"))

    return cands


# ---------------------------------------------------------------------------
# Section 6 — Substitution chain (plan §10) — explicit per math-scripts.md
# ---------------------------------------------------------------------------
def substitution_chain(V: float) -> dict:
    """Execute the plan §10 substitution chain explicitly.

    Step 1: Definition: Tr exp(-t·D_K^2) ~ Σ a_n·t^{(n-d)/2}
    Step 2: Definition: candidate normalizations 1/(4π)^k
    Step 3: V_W95 / (1/(4π)²) computed; check if integer-prefactor structure
    Step 4: Direction: which n integer best explains V_W95
    """
    pi4_2 = (4.0 * math.pi) ** 2                                 # (local)
    ratioA = V / (1.0 / pi4_2)                                   # (local) Step A: V·(4π)²
    nearest_int_A = round(ratioA)                                # (local)
    delta_A = abs(ratioA - nearest_int_A) / nearest_int_A        # (local) rel dev from integer

    ratioB = V * 12.0 / tau_fold                                 # (local) Step B
    ratioC = V * pi4_2                                           # (local) Step C (== Step A)

    return dict(
        step_A_V_div_inv4pi2=ratioA,
        step_A_nearest_int=int(nearest_int_A),
        step_A_int_dev_rel=delta_A,
        step_B_V_times_12_over_tau=ratioB,
        step_C_V_times_4pi_sq=ratioC,
        narrative=(
            f"V_W95 / (1/(4π)²) = {V}/{1.0/pi4_2:.10f} = {ratioA:.6f}; "
            f"nearest integer = {int(nearest_int_A)}; "
            f"|ratio − {int(nearest_int_A)}|/{int(nearest_int_A)} = {delta_A:.4e}. "
            f"Step B: V·12/tau_fold = {ratioB:.4f} (NOT integer 12). "
            f"Step C: V·(4π)² = {ratioC:.6f} (= Step A)."
        ),
    )


# ---------------------------------------------------------------------------
# Section 7 — Match catalogue against V_W95
# ---------------------------------------------------------------------------
def evaluate_matches(V: float, catalogue: list[dict]) -> list[dict]:
    """Compute rel_err for each candidate; tag matches at strict / loose bands."""
    out: list[dict] = []                                         # (local)
    for c in catalogue:
        rel = abs(V - c["value"]) / V                            # (local)
        match_strict = rel <= PASS_RATIO_STRICT                  # (local)
        match_loose = rel <= INFO_RATIO_LOOSE                    # (local)
        out.append(dict(
            label=c["label"],
            value=c["value"],
            weight_n=c["weight_n"],
            norm_class=c["norm_class"],
            rel_err=rel,
            match_strict=bool(match_strict),
            match_loose=bool(match_loose),
        ))
    out.sort(key=lambda r: r["rel_err"])
    return out


def classify_verdict(matches: list[dict]) -> tuple[str, dict]:
    """Plan §9 PASS / INFO / FAIL classification.

    PASS: unique match at rel_err ≤ 1e-3 AND weight ∈ {2,4,6,8} AND
          weight identified as INCONSISTENT with integer-12 (plan-mandated).
    INFO: match(es) at rel_err ∈ (1e-3, 1e-2]; identification plausible
          but not strict.
    FAIL: no candidate at rel_err ≤ 1e-2.
    """
    strict = [m for m in matches if m["match_strict"]]           # (local)
    loose = [m for m in matches if m["match_loose"]]             # (local)

    if len(strict) == 1:
        m = strict[0]
        weight = m["weight_n"]
        if weight in CANDIDATE_WEIGHTS:
            verdict = "PASS"
            reason = (f"Unique strict match at {m['label']} (rel={m['rel_err']:.3e}); "
                      f"weight n={weight} is INCONSISTENT with integer-12 "
                      f"(integer-12 requires n=8 cone-apex, V.2 sampled n={weight}).")
        else:
            verdict = "INFO"
            reason = (f"Unique strict match at {m['label']}, but weight {weight} "
                      f"is non-standard (not in {CANDIDATE_WEIGHTS}).")
    elif len(strict) > 1:
        verdict = "INFO"
        reason = (f"Hypothesis-exclusivity FAIL at strict band: "
                  f"{len(strict)} candidates match at rel_err ≤ 1e-3.")
    elif len(loose) >= 1:
        verdict = "INFO"
        labels = ", ".join(m["label"] for m in loose)
        reason = (f"No strict match; {len(loose)} candidate(s) match at "
                  f"rel_err ∈ (1e-3, 1e-2]: {labels}. "
                  f"Identification plausible but precision insufficient for PASS.")
    else:
        verdict = "FAIL"
        reason = ("No candidate matches within rel_err ≤ 1e-2 at any standard "
                  "SD weight. V.2 return value is not a substrate SD coefficient.")

    return verdict, dict(strict_count=len(strict), loose_count=len(loose),
                         reason=reason)


# ---------------------------------------------------------------------------
# Section 8 — Dual-SHA closure (W9a-99 template)
# ---------------------------------------------------------------------------
def closure_hash(pin_map: dict) -> str:
    """SHA-256 over deterministic-JSON-sorted pin map (audit_sha256)."""
    payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))   # (local)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def compute_content_sha(payload_dict: dict) -> str:
    """SHA-256 over output payload (content_sha256)."""
    payload = json.dumps(payload_dict, sort_keys=True, separators=(",", ":"),
                        default=str)                                        # (local)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 9 — Driver
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                        # (local)
    print(f"=== {GATE_ID} ===")
    print(f"  V_W95 (audit input) = {V_W95}")
    print(f"  Plan §9 thresholds: PASS ≤ {PASS_RATIO_STRICT}, "
          f"INFO ∈ ({PASS_RATIO_STRICT}, {INFO_RATIO_LOOSE}]")

    # ---------- Pre-existence checks (input pin map) ----------
    sha_canon = sha256_of(CANONICAL_CONSTANTS)                              # (local)
    sha_v2_src = sha256_of(V2_SOURCE_SCRIPT)                                # (local)
    sha_v2_npz = sha256_of(V2_DATA_NPZ)                                     # (local)
    sha_v2_verdicts = sha256_of(V2_VERDICT_FILE)                            # (local)
    sha_self = sha256_of(SCRIPT_PATH)                                       # (local)

    v2_verdict_line, sha_v2_verdict_line = grep_v2_verdict_line(V2_VERDICT_FILE)
    print(f"  W9-5 V.2 source script SHA: {sha_v2_src[:16]}... "
          f"({'present' if sha_v2_src else 'MISSING'})")
    print(f"  W9-5 V.2 data .npz   SHA: {sha_v2_npz[:16]}... "
          f"({'present' if sha_v2_npz else 'MISSING'})")
    print(f"  W9-5 V.2 verdict line SHA: {sha_v2_verdict_line[:16]}...")
    print(f"  V.2 verdict line excerpt: {v2_verdict_line[:120]}")

    # PRE-REG-INC trigger (plan §6 prerequisites)
    if not sha_v2_src:
        print(f"  PRE-REG-INC: V.2 source script absent at {V2_SOURCE_SCRIPT}.")
        return _emit_pre_reg_inc("v2_source_script_missing", sha_canon, sha_self)
    if not sha_v2_verdicts or not v2_verdict_line:
        print(f"  PRE-REG-INC: V.2 verdict line not located in s85_gate_verdicts.txt.")
        return _emit_pre_reg_inc("v2_verdict_line_missing", sha_canon, sha_self)

    # ---------- Catalogue + match ----------
    catalogue = build_candidate_catalogue()
    print(f"  Candidate catalogue: {len(catalogue)} entries enumerated.")

    matches = evaluate_matches(V_W95, catalogue)
    print("\n  Top 8 candidates by rel_err:")
    print(f"  {'label':<22s}  {'value':<16s}  {'rel_err':<10s}  {'n':<4s}  flags")
    for m in matches[:8]:
        flags = []                                                          # (local)
        if m["match_strict"]:
            flags.append("STRICT")
        elif m["match_loose"]:
            flags.append("LOOSE")
        print(f"  {m['label']:<22s}  {m['value']:<16.10f}  {m['rel_err']:<10.4e}  "
              f"{str(m['weight_n']):<4s}  {','.join(flags) if flags else '-'}")

    # ---------- Substitution chain (plan §10) ----------
    sub_chain = substitution_chain(V_W95)
    print(f"\n  --- Substitution chain (plan §10) ---")
    print(f"    {sub_chain['narrative']}")

    # ---------- Verdict classification (plan §9) ----------
    verdict, vinfo = classify_verdict(matches)
    print(f"\n  Verdict: {verdict}")
    print(f"    {vinfo['reason']}")

    # ---------- Identify match weight + S87 carry-forward ----------
    best = matches[0]                                                       # (local)
    n_match: int | str
    if best["match_loose"] and best["weight_n"] in CANDIDATE_WEIGHTS:
        n_match = best["weight_n"]
    elif best["match_loose"]:
        n_match = "non-standard"
    else:
        n_match = "non-identifiable"

    # Plan §13 substrate-framing: integer-12 derivation requires d_spec=8
    # cone-apex; if best match is at n=4, V.2 sampled the wrong weight.
    s87_recommendation = (
        f"S87 carry-forward: re-run heat-kernel route at d_spec=8 cone-apex "
        f"weight (normalization 1/(4π)⁴, not 1/(4π)²) — V.2 sampled weight "
        f"n={n_match} (4D-base subset of substrate-spectral cone) when "
        f"integer-12 derivation requires n=8 (full 8D cone-apex). The "
        f"factor between weights is (4π)² ≈ 158, which would push the "
        f"raw value from O(0.15) to O(10⁻³) at the cone-apex weight, "
        f"making integer-12 plausibly recoverable as a moment-ratio "
        f"rather than a raw heat-kernel return."
    )
    print(f"\n  S87 carry-forward: {s87_recommendation[:120]}...")

    # ---------- Build output payload ----------
    payload = dict(
        gate_id=GATE_ID,
        session=SESSION,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        schema_version=SCHEMA_VERSION,
        verdict=verdict,
        verdict_reason=vinfo["reason"],
        V_W95=V_W95,
        V_W95_round=V_W95_ROUND,
        thresholds=dict(PASS_strict=PASS_RATIO_STRICT,
                        INFO_loose=INFO_RATIO_LOOSE),
        candidate_catalogue=matches,
        substitution_chain=sub_chain,
        n_match=n_match,
        candidate_weights=CANDIDATE_WEIGHTS,
        s87_carry_forward=s87_recommendation,
        v2_source=dict(
            script_path=str(V2_SOURCE_SCRIPT.relative_to(PROJECT_ROOT)),
            script_sha256=sha_v2_src,
            data_npz_path=str(V2_DATA_NPZ.relative_to(PROJECT_ROOT)),
            data_npz_sha256=sha_v2_npz,
            verdict_file_path=str(V2_VERDICT_FILE.relative_to(PROJECT_ROOT)),
            verdict_file_sha256=sha_v2_verdicts,
            verdict_line=v2_verdict_line,
            verdict_line_sha256=sha_v2_verdict_line,
        ),
        machinery_pin=dict(
            L_max=L_MAX,
            scheme=SCHEME,
            convention=CONVENTION,
            n_eval_candidates=CANDIDATE_WEIGHTS,
            scan_range="none (audit; V_W95 is fixed input)",
            tolerance=dict(PASS=PASS_RATIO_STRICT, INFO=INFO_RATIO_LOOSE),
            random_seed=None,
            GPU_path="CPU; OMP_NUM_THREADS=8 (trivial arithmetic)",
            cutoff_axis="spectral",
        ),
        runtime_seconds=time.time() - t0,
    )

    # ---------- Dual-SHA closure ----------
    pin_map = dict(
        canonical_constants_sha256=sha_canon,
        v2_source_script_sha256=sha_v2_src,
        v2_verdict_line_sha256=sha_v2_verdict_line,
        v2_data_npz_sha256=sha_v2_npz,
        self_script_sha256=sha_self,
        L_max=L_MAX,
        scheme=SCHEME,
        convention=CONVENTION,
        V_W95_audit_input=V_W95,
        candidate_weights=CANDIDATE_WEIGHTS,
        threshold_PASS_strict=PASS_RATIO_STRICT,
        threshold_INFO_loose=INFO_RATIO_LOOSE,
    )
    audit_sha = closure_hash(pin_map)                                       # (local)

    # Write JSON BEFORE computing content_sha (so file exists)
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=True, default=str)

    content_sha = compute_content_sha(payload)                              # (local)

    # ---------- Append verdict line + dual-SHA companion (W9a-99) ----------
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={V_W95_ROUND} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"sha256={content_sha}"
    )
    companion = (
        f"# {GATE_ID} dual-SHA: "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(companion + "\n")

    print(f"\n  Verdict line appended: {canonical_line}")
    print(f"  Companion row:          {companion}")
    print(f"  Output JSON: {OUT_JSON}")
    print(f"  Runtime: {time.time() - t0:.3f} s")
    return 0


def _emit_pre_reg_inc(reason_tag: str, sha_canon: str, sha_self: str) -> int:
    """Emit PRE-REG-INC verdict line + companion when a prereq is missing."""
    pin_map = dict(
        canonical_constants_sha256=sha_canon,
        self_script_sha256=sha_self,
        reason=reason_tag,
    )
    audit_sha = closure_hash(pin_map)                                       # (local)
    payload = dict(verdict="PRE-REG-INC", reason=reason_tag, pins=pin_map)
    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=True)
    content_sha = compute_content_sha(payload)                              # (local)
    line = (f"{GATE_ID}: PRE-REG-INC -- value=NA "
            f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
            f"sha256={content_sha}")
    companion = (f"# {GATE_ID} dual-SHA: audit_sha256={audit_sha} "
                 f"content_sha256={content_sha} schema_version={SCHEMA_VERSION}")
    with VERDICT_TXT.open("a", encoding="utf-8") as f:
        f.write(line + "\n")
        f.write(companion + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
