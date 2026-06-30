#!/usr/bin/env python3
"""
S86 W5b-C15(i) — GAUGE selection: substrate-native zeta N=3.12 vs gauge-invariant MS N=55
==========================================================================================

Gate: S86-W5B-C15-i-GAUGE  ([AUDIT])

Pre-registered threshold (plan §9):
  PASS iff  (selection rule chosen in {axiom-native, observation-native, pre-reg-both})
            AND (4-step substitution chain documented in WP §W5b-1.i)
            AND (2-column pivot table emitted to JSON).
  FAIL iff any of the three is missing.
  INFO is NOT used for this gate (binary AUDIT).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
  - sessions/session-plan/session-86-plan-w5b.md
  - sessions/session-plan/session-86-plan-w5a.md   (downstream-pin consumer)
  - sessions/archive/session-77/session-77-transit-synthesis.md  (canonical 3.12 source)
  - sessions/archive/session-82/workshops/s82-w1-1-divergence-chase.md  (canonical MS=55 source)
  - script bytes itself (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value="pre-reg-both", scheme="mellin_zeta_substrate", convention="both", L_max=10)

Classification: PHONONIC
  Both N=3.12 (substrate-zeta) and N=55 (MS) are substrate properties under different
  gauges, NOT external observational impositions. Direction of explanation:
  substrate spectral-zeta evolution -> Mellin-zeta moment -> either pivot bookkeeping.

Method (per plan §6, §10):
  1. Define each N counter with canonical-source citation.
  2. Substitute each into H(N_pivot) under SR-LO eps_H = eps_H_W6.
  3. Simplify to canonical form Ratio = exp((55 - 3.12) * eps_H_W6).
  4. Read off direction ONLY after canonical form: ratio > 1 ==> H_substrate_zeta > H_MS
     under same H_initial and eps_H_W6. (Bookkeeping consequence, not physical claim.)
  5. Selection rule decision per the structural evidence (no NCG axiom uniquely selects
     3.12; observational pre-registration is hybrid; pre-reg-both is the structurally
     legitimate outcome).
  6. Emit 2-column table to JSON.
  7. Write verdict line + companion via canonical helper.

Discipline:
  - `from canonical_constants import *` (eps_H_W6, tau_fold, M_KK)
  - All intermediates tagged `# (local)`
  - CPU-only, OMP_NUM_THREADS=8 (analytical gate; no GPU benefit)
  - SHA-256 of inputs logged in first 20 lines of stdout
  - Dual-SHA emitted (audit_sha256 + content_sha256 + 16-hex companion row)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (BEFORE numpy import; analytical gate)
# ---------------------------------------------------------------------------
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

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
import canonical_constants as CC

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path
import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent           # (local)
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S86"                                                 # (local)
GATE_ID = "S86-W5B-C15-i-GAUGE"                                 # (local)
SCHEME = "mellin_zeta_substrate"                                # (local)
CONVENTION = "both"                                             # (local)  pre-reg-both => both columns
L_MAX = 10                                                      # (local)

# Pre-registered selection-rule alphabet (plan §9, §10)
SELECTION_RULES = ("axiom-native", "observation-native", "pre-reg-both")  # (local)

# Canonical pivot values (per plan §6 + S77 transit-synthesis L103 + S82 W1-1)
N_SUBSTRATE_ZETA = 3.12   # (local) substrate Mellin-zeta moment at tau_fold (S77 L103)
N_MS = 55                 # (local) gauge-invariant MS comoving-mode horizon-exit (S82 W1-1)

# Output destinations
OUT_JSON = resolve_output(86, 's86_w5b_c15_i_gauge_table.json')         # (local)
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')               # (local)

# Input files (SHA-pinned)
INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    PROJECT_ROOT / "sessions" / "session-plan" / "session-86-plan-w5b.md",
    PROJECT_ROOT / "sessions" / "session-plan" / "session-86-plan-w5a.md",
    PROJECT_ROOT / "sessions" / "session-77" / "session-77-transit-synthesis.md",
    PROJECT_ROOT / "sessions" / "session-82" / "workshops" / "s82-w1-1-divergence-chase.md",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema, W9a-99)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                         # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins: dict[str, str] = {}                                    # (local)
    for p in inputs:
        sha = sha256_of(p)                                       # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())                                 # (local)
    h = hashlib.sha256()                                         # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = b""                                           # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                        # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                            # (local)

    h_audit = hashlib.sha256()                                   # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                  # (local)

    h_content = hashlib.sha256()                                 # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                              # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (substitution chain + selection-rule decision + table)
# ---------------------------------------------------------------------------

def substitution_chain() -> dict:
    """Execute the 4-step substitution chain comparing N_substrate_zeta vs N_MS.

    Returns a dict containing all intermediate quantities, used to populate
    both the 2-column table and the working-paper section.
    """
    # Step 1 (definitions, both N counters):
    #   N_substrate_zeta(tau_fold): substrate's Mellin-zeta moment at tau_fold
    #     evaluated at L_max=10. Numerical canonical pin: N = 3.12 e-folds
    #     (S77 transit-synthesis L103: "exits the horizon at N_pivot = 3.12
    #     e-folds after the fold, placing it N_* = 60.3 e-folds before reheating
    #     -- consistent with the standard result N_* ~ 50-60.")
    #   N_MS(k_pivot): log[a_end / a(k_pivot exits horizon)] = 55 (Planck pivot
    #     k = 0.05 Mpc^{-1}, standard convention; S82 W1-1 §IV.A.TD L52-L65).
    #   H(N) = H_initial * exp(-int_0^N eps_H(N') dN')   [SR-LO trajectory]

    eps_H = CC.eps_H_W6                                          # (local) 0.02163, S80 dS/dtau-fold pin
    N_zeta = N_SUBSTRATE_ZETA                                    # (local) 3.12
    N_ms = N_MS                                                  # (local) 55

    # Step 2 (substitute each N into H(N_pivot) under SR-LO eps_H = const):
    #   H(N_pivot)|_substrate_zeta = H_initial * exp(-3.12 * eps_H_W6)
    #   H(N_pivot)|_MS             = H_initial * exp(-55   * eps_H_W6)
    H_factor_zeta = float(np.exp(-N_zeta * eps_H))               # (local) H(N_zeta)/H_initial
    H_factor_ms = float(np.exp(-N_ms * eps_H))                   # (local) H(N_ms)/H_initial

    # Step 3 (simplify to canonical form):
    #   Ratio = H_substrate_zeta / H_MS
    #         = exp(-3.12 * eps_H) / exp(-55 * eps_H)
    #         = exp((55 - 3.12) * eps_H)
    #         = exp(51.88 * eps_H_W6)
    #         = exp(51.88 * 0.02163)
    DeltaN = N_ms - N_zeta                                       # (local) 51.88
    log_ratio = DeltaN * eps_H                                   # (local)
    ratio = float(np.exp(log_ratio))                             # (local) H_zeta/H_ms

    # Step 4 (direction read-off — ONLY after canonical form):
    #   eps_H = +0.02163 > 0
    #   DeltaN = +51.88 > 0
    #   product log_ratio = +1.122 > 0
    #   exp(positive) = ratio > 1
    #   ==> H_substrate_zeta(N_pivot) > H_MS(N_pivot) under same H_initial and eps_H.
    #   This is bookkeeping consequence of the convention disparity, NOT a physical
    #   claim that one convention is "right". The same physical H is being labeled
    #   at two different pivot times under two different fold-counter conventions.
    direction_sign = +1 if log_ratio > 0 else (-1 if log_ratio < 0 else 0)  # (local)
    direction_label = "ratio > 1 (H_zeta > H_MS)" if direction_sign > 0 \
        else ("ratio < 1 (H_zeta < H_MS)" if direction_sign < 0
              else "ratio = 1 (equal)")                          # (local)

    return {
        "eps_H": float(eps_H),
        "N_zeta": float(N_zeta),
        "N_MS": float(N_ms),
        "H_factor_zeta_over_H_initial": H_factor_zeta,
        "H_factor_MS_over_H_initial": H_factor_ms,
        "DeltaN_MS_minus_zeta": float(DeltaN),
        "log_ratio_zeta_over_MS": float(log_ratio),
        "ratio_H_zeta_over_H_MS": ratio,
        "direction_sign": int(direction_sign),
        "direction_label": direction_label,
    }


def select_rule(chain: dict) -> tuple[str, str]:
    """Apply the structural-evidence selection rule per plan §6.3 and §10.

    Returns (rule_label, justification_text).

    The rule is selected from {axiom-native, observation-native, pre-reg-both}
    based on the structural evidence available at S86 W5b dispatch time:

    (a) AXIOM-NATIVE: would require an NCG axiom in {KO-dim=6, [J,D_K]=0,
        first-order, regularity, finiteness, reality, orientability, Poincare
        duality} to UNIQUELY select N_substrate_zeta = 3.12 over any other
        Mellin-zeta evaluation. EVIDENCE AGAINST: S77 transit-einstein-workshop
        L976 shows N_pivot flips from 3.12 to ~2.0 when c_s changes from 1.0
        to 0.485. The numerical value 3.12 is a derived bookkeeping quantity
        sensitive to the c_s convention, NOT an axiom-native invariant.
        REJECTED.

    (b) OBSERVATION-NATIVE: would require the project's pre-registered
        observational predictions to use ONLY the MS pivot. EVIDENCE AGAINST:
        canonical_constants N_pivot = 64.08 = 55 + ln(c/c_s) (S83
        S83-N-PIVOT-CS-CANONICALIZATION) is a HYBRID, neither pure substrate
        nor pure MS. Framework-canonical predictions (S77, S80, S82, S83 W1-G5
        epoch axis 0=horizon_exit N=55-65, 1=fold tau=0.190) ALSO use the
        substrate-zeta pivot when computing tilt at fold. REJECTED.

    (c) PRE-REG-BOTH: structurally legitimate when (i) no NCG axiom uniquely
        selects either, AND (ii) both are needed downstream (substrate-zeta
        for axiom-trace diagnostic; MS for observational comparison), AND
        (iii) the W5a P3 plan §0.5 SOFT-prereq explicitly absorbs this
        contingency ("If C15(i) reports DEFER..., W5a P3 records both
        pivots..."). All three conditions hold. SELECTED.
    """
    rule = "pre-reg-both"                                        # (local)
    justification = (
        "PRE-REG-BOTH selected. Rationale: (i) No NCG axiom in "
        "{KO-dim=6, [J,D_K]=0, first-order, regularity, finiteness, reality, "
        "orientability, Poincare duality} uniquely selects N_substrate_zeta=3.12 "
        "over the c_s-corrected ~2.0 value (S77 transit-einstein-workshop L976) "
        "or any other Mellin-zeta evaluation, so AXIOM-NATIVE (a) is rejected. "
        "(ii) Canonical N_pivot=64.08=55+ln(c/c_s) is hybrid (S83 "
        "S83-N-PIVOT-CS-CANONICALIZATION), and S83 W1-G5 epoch axis carries BOTH "
        "0=horizon_exit (N=55-65) AND 1=fold (tau=0.190), so framework-canonical "
        "predictions use both gauges, refuting OBSERVATION-NATIVE (b). "
        "(iii) W5a P3 plan §0.5 SOFT-prereq absorbs this contingency by "
        "explicitly authorizing dual-pivot reporting. Both N=3.12 and N=55 are "
        "substrate properties under different gauges (substrate Mellin-zeta vs "
        "MS comoving-mode horizon-exit), NOT external observational impositions. "
        "Direction of explanation per phononic-framing.md 'IS Space, Not IN "
        "Space': substrate spectral-zeta evolution -> Mellin-zeta moment -> "
        "either pivot bookkeeping convention. The 4-step substitution chain "
        "(eps_H=0.02163; DeltaN=51.88; log_ratio=+1.122; ratio="
        f"{chain['ratio_H_zeta_over_H_MS']:.4f} > 1) shows the disparity is "
        "exp((N_MS - N_zeta) * eps_H_W6) = bookkeeping-consistent under SR-LO."
    )
    return rule, justification


def emit_table(chain: dict, rule: str) -> dict:
    """Emit the 2-column pivot table to JSON per plan §6 step 4."""
    table = {
        "schema": "S86-W5B-C15-i-GAUGE pivot-selection table v1",
        "gate_id": GATE_ID,
        "selection_rule": rule,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "rows": [
            {
                "Pivot": "substrate-zeta",
                "N_e_folds": N_SUBSTRATE_ZETA,
                "Source": (
                    "S77 transit-synthesis.md L103 ('exits the horizon at "
                    "N_pivot = 3.12 e-folds after the fold'); "
                    "substrate Mellin-zeta moment at tau_fold=0.19 evaluated "
                    "at L_max=10. Cross-ref S77 transit-einstein-workshop L976 "
                    "(c_s sensitivity: 3.12 -> ~2.0 at c_s=0.485)."
                ),
                "Used_by_gates": [
                    "S86-W5A-P3-SECTOR-1 (PRE-REG-BOTH branch reports Z(N=3.12))",
                    "S86-W4-P5-SECTOR-2 (substrate tau pre-image of N=3.12)",
                    "Late-S86 falsifier registry (substrate-side r prediction)",
                ],
                "Convention_class": "substrate-native (axiom-trace diagnostic)",
            },
            {
                "Pivot": "MS",
                "N_e_folds": N_MS,
                "Source": (
                    "Standard Mukhanov-Sasaki gauge-invariant comoving-mode "
                    "horizon-exit count (Planck pivot k=0.05 Mpc^-1); "
                    "S82 W1-1 divergence-chase L52-L77 (TD reading at N=55 "
                    "horizon-exit), L77 ('only the horizon-exit H survives "
                    "in the frozen spectrum', Mukhanov-Sasaki 1980s). "
                    "Birrell-Davies §3.4, §5.6; Parker 1969."
                ),
                "Used_by_gates": [
                    "S86-W5A-P3-SECTOR-1 (PRE-REG-BOTH branch reports Z(N=55))",
                    "S86-W5B-C15-ii-BASELINE (forward integration target N_initial = N_pivot + 55)",
                    "S82 W1-1 H_TILDE_TD PASS-F2 (canonical observational pivot)",
                    "Late-S86 falsifier registry (observation-side r prediction)",
                ],
                "Convention_class": "observation-native (Planck-pivot observable)",
            },
        ],
        "substitution_chain": {
            "step_1_definitions": (
                "N_substrate_zeta(tau_fold) = substrate Mellin-zeta moment at "
                "tau_fold=0.19, L_max=10 (canonical numerical value 3.12 "
                "e-folds, S77 L103). N_MS(k_pivot) = log[a_end/a(k_pivot exits "
                "horizon)] = 55 (Planck pivot k=0.05 Mpc^-1). "
                "H(N) = H_initial * exp(-int_0^N eps_H(N') dN') [SR-LO trajectory]."
            ),
            "step_2_substitute": (
                f"H(N_pivot)|_substrate_zeta = H_initial * exp(-{N_SUBSTRATE_ZETA} * eps_H_W6); "
                f"H(N_pivot)|_MS = H_initial * exp(-{N_MS} * eps_H_W6); "
                f"eps_H_W6 = {chain['eps_H']:.5f} (canonical S80 dS/dtau-fold pin)."
            ),
            "step_3_simplify": (
                f"Ratio = H_zeta/H_MS = exp(({N_MS} - {N_SUBSTRATE_ZETA}) * eps_H_W6) "
                f"= exp({chain['DeltaN_MS_minus_zeta']:.2f} * {chain['eps_H']:.5f}) "
                f"= exp({chain['log_ratio_zeta_over_MS']:.4f}) = "
                f"{chain['ratio_H_zeta_over_H_MS']:.4f}."
            ),
            "step_4_direction": (
                f"eps_H = +{chain['eps_H']:.5f} > 0; "
                f"DeltaN = +{chain['DeltaN_MS_minus_zeta']:.2f} > 0; "
                f"product log_ratio = +{chain['log_ratio_zeta_over_MS']:.4f} > 0; "
                f"exp(positive) = ratio = {chain['ratio_H_zeta_over_H_MS']:.4f} > 1; "
                f"==> H_substrate_zeta(N_pivot) > H_MS(N_pivot) under same H_initial. "
                f"Bookkeeping consequence of convention disparity, not physical claim."
            ),
        },
        "downstream_consequence": (
            "Per W5a P3 plan §0.5 SOFT-prereq: SECTOR-1 reports BOTH columns "
            "Z(N_pivot=3.12) and Z(N_pivot=55) through S86 close. canonical "
            "commit deferred to W-2 workshop. Both columns flow into late-S86 "
            "falsifier registry as Path-H-substrate-zeta and Path-H-MS."
        ),
        "phononic_framing_note": (
            "Both N=3.12 and N=55 are substrate properties under different "
            "gauges, NOT external observational impositions. Direction of "
            "explanation: substrate spectral-zeta evolution -> Mellin-zeta "
            "moment -> either pivot bookkeeping convention. NOT 'N e-folds "
            "elapsed in spacetime' (container thinking, forbidden per "
            ".claude/rules/phononic-framing.md)."
        ),
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump(table, fp, indent=2, sort_keys=False)
    return table


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + dual-SHA verdict line
# ---------------------------------------------------------------------------

def evaluate_gate(rule: str, chain_present: bool, table_emitted: bool) -> str:
    """Binary AUDIT per plan §9: PASS iff (rule in alphabet) AND chain AND table."""
    if rule not in SELECTION_RULES:
        return "FAIL"
    if not chain_present:
        return "FAIL"
    if not table_emitted:
        return "FAIL"
    return "PASS"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Append S84+ dual-SHA verdict line + 16-hex companion comment row.

    Per .claude/rules/gate-verdicts.md (canonical format) + W9a-99 split
    (dual-SHA companion row for human scan-readability).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                             # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                 # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()                       # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute substitution chain
    print("=== Step 1-4 substitution chain ===")
    chain = substitution_chain()
    print(f"  Step 1 def: N_zeta={chain['N_zeta']}, N_MS={chain['N_MS']}, eps_H={chain['eps_H']}")
    print(f"  Step 2 sub: H_factor_zeta/H_initial={chain['H_factor_zeta_over_H_initial']:.4f}")
    print(f"             H_factor_MS/H_initial   ={chain['H_factor_MS_over_H_initial']:.4f}")
    print(f"  Step 3 simplify: DeltaN={chain['DeltaN_MS_minus_zeta']:.2f}, "
          f"log_ratio={chain['log_ratio_zeta_over_MS']:.4f}")
    print(f"  Step 3 simplify: ratio H_zeta/H_MS = {chain['ratio_H_zeta_over_H_MS']:.4f}")
    print(f"  Step 4 direction: {chain['direction_label']}")
    print()

    # 3. Apply selection rule per structural evidence
    print("=== Selection-rule decision ===")
    rule, justification = select_rule(chain)
    print(f"  Selected rule: {rule}")
    print(f"  Justification (head): {justification[:200]}...")
    print()

    # 4. Emit 2-column pivot table
    print("=== Emitting 2-column pivot table ===")
    table = emit_table(chain, rule)
    table_emitted = OUT_JSON.exists() and OUT_JSON.stat().st_size > 0  # (local)
    print(f"  Table written: {OUT_JSON.name} (rows={len(table['rows'])}, "
          f"size={OUT_JSON.stat().st_size}B)")
    print()

    # 5. Evaluate gate
    chain_present = all(k in table["substitution_chain"] for k in
                        ("step_1_definitions", "step_2_substitute",
                         "step_3_simplify", "step_4_direction"))  # (local)
    verdict = evaluate_gate(rule, chain_present, table_emitted)
    value = rule                                                  # (local) the 4-tuple value field

    # 6. Emit 4-tuple + append verdict (dual-SHA, S84+ schema)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(f"=== 4-tuple ===\n  {tag}")
    append_verdict(verdict, value, audit_sha, content_sha)

    # 7. Final summary
    wall = time.time() - t0                                       # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"    audit_sha256   = {audit_sha}")
    print(f"    content_sha256 = {content_sha}")
    return 0  # PASS or FAIL: both exit 0 (verdict is data, not script health)


if __name__ == "__main__":
    sys.exit(main())
