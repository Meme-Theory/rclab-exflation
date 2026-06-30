#!/usr/bin/env python3
"""
S102 W2-4 CF-S102-VIIAM-L2L3-RECON — §VII.AM Level-2/Level-3 envelope-row reconciliation
=======================================================================================

Gate: CF-S102-VIIAM-L2L3-RECON ([VERIFY])

Pre-registered threshold (cross-pillar-bridge-anatomy.md Registry-PASS criterion):
  PASS iff Level3_reconciled < Level2_reconciled at L_max=10, under the PRE-REGISTERED
       comparator candidate (decision frozen at plan-freeze BEFORE compute), AND the
       reconciliation is independently motivated by the envelope-is-a-bound substitution
       chain (NOT comparator-shopped).
  FAIL iff even under the structurally-correct PREFACTORED comparator, Level3 >= Level2
       at true alpha=4.6905 (envelope ROW genuinely fails; theorem-STRUCTURE untouched,
       STAGE-3-PERMANENT).
  INFO iff the (i)/(ii) x (Q3a)/(Q3b) choice is genuinely ambiguous after the substitution
       chain (outcome flips with the choice) -> route to 2-agent workshop.

PRE-REGISTERED DECISION (plan §W2-4 machinery_pin_map.PRE_REGISTERED_comparator_decision):
  Level-2 envelope = candidate (ii) PREFACTORED  C * L^{-alpha},  C = exp(intercept).
    Reason (from DEFINITION, not outcome): the Level-2 envelope is the convergence-rate
    BOUND ‖HKR(c_L) - c_continuum‖ <= C * L^{-alpha}; a bound carries its fitted amplitude
    C. The bare L^{-alpha} asserts unit amplitude, which is NOT what the W1-4 fit produced.
  Level-3 quantity = candidate (Q3a) BARE deviation  3.0e-4 = 1 - Gamma_effacement
    (Gamma_effacement = 0.9997 canonical; §VII.AM clause (b) A(∂R)/(4 G_N A_universal)=3.0e-4).
  This decision is FIXED HERE; the compute only EVALUATES the inequality on the pinned
  (alpha, intercept) values -- it does NOT search for the PASS-yielding choice.

Scope: ENVELOPE-ROW reconciliation ONLY. The §VII.AM 3-clause joint theorem (Level-1
  structural identity) is STAGE-3-PERMANENT and is NOT in scope here -- only the Element-4 /
  Level-2-vs-Level-3 Registry-PASS ROW is re-evaluated.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-101/s101_viiam_alpha_envelope_pin.npz  (alpha, intercept,
        env_at_Lmax10, level3_anchor, dGamma_over_Gamma, L_fit; W1-4 pin, audit 251141bc;
        plan-pinned file SHA 3ea82a00b375e344ac3cdaf2f5aa75e84a70e21adb28a1e8b50b5fa25cc8f423)
  - computations/_shared/canonical_constants.py  (Gamma_effacement = 0.9997; feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

PLAN-TEXT-DRIFT NOTE (substrate-first-canonical-sourcing.md §(ii.B)):
  The plan substitution_chain (line 756) equates the npz `env_at_Lmax10` field with the
  PREFACTORED form exp(intercept)*10^{-alpha}. That is a documentation MIS-LABEL: the W1-4
  producing script (s101_viiam_alpha_envelope_pin.py:556) computed
  `env_Lmax10 = 10.0 ** (-fit["alpha"])` -- the BARE form. The npz `env_at_Lmax10`
  (2.0392e-05) is therefore the BARE candidate (i), NOT prefactored. This script computes the
  TRUE prefactored value exp(intercept)*10^{-alpha} = 3.7974e-05 from first principles and
  documents the drift in the verdict value string + npz. The OUTCOME is robust to the
  mis-label: 3.0e-4 > BOTH the bare (2.04e-05) AND the prefactored (3.80e-05) envelope at
  L_max=10, so Registry-PASS does not restore under EITHER candidate -> FAIL, not INFO.

Output 4-tuple:
  (value=<Level3-vs-Level2-prefac inequality>, scheme=cross-pillar-bridge-anatomy-Registry-PASS,
   convention=envelope-comparator-PRE-REGISTERED-prefactored-ii/alpha=4.6905, L_max=10)

Classification: GEOMETRIC (algebraic-convergence-envelope row adjudication on a pinned fit;
  substrate-IS spectral-action effacement-moment convergence bound).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os  # noqa: E402
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 (closed-form; no linalg)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys  # noqa: E402
from pathlib import Path  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S102"                                                        # (local)
GATE_ID = "CF-S102-VIIAM-L2L3-RECON"                                    # (local)
SCHEME = "cross-pillar-bridge-anatomy-Registry-PASS-criterion"         # (local)
CONVENTION = "envelope-comparator-PRE-REGISTERED-prefactored-ii/alpha=4.6905"  # (local)
L_MAX = 10                                                              # (local)

ENVELOPE_PIN_NPZ = COMPUTATIONS_DIR / "session-101" / "s101_viiam_alpha_envelope_pin.npz"  # (local)
# Plan-pinned static SHA of the W1-4 envelope-pin npz (machinery feasibility / audit).
PLAN_PINNED_NPZ_SHA = (
    "3ea82a00b375e344ac3cdaf2f5aa75e84a70e21adb28a1e8b50b5fa25cc8f423"
)  # (local)

# The canonical Level-3 anchor = 1 - Gamma_effacement (imported from canonical_constants).
# Gamma_effacement = 0.9997 (MCP get_constant confirmed; §VII.AM clause (b) anchor).
LEVEL3_ANCHOR = 1.0 - Gamma_effacement                                 # (local) = 3.0e-4

OUT_NPZ = SESSION_DIR / "s102_w2_viiam_l2l3_recon.npz"                  # (local)
OUT_PNG = SESSION_DIR / "s102_w2_viiam_l2l3_recon.png"                  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    ENVELOPE_PIN_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    """Adjudicate the §VII.AM Level-2/Level-3 envelope-row comparator at L_max=10.

    Loads the SHA-pinned W1-4 envelope-pin npz, recomputes BOTH comparator candidates
    in closed form from the pinned (alpha, intercept), and evaluates the strict-<
    Registry-PASS inequality under the PRE-REGISTERED candidate (ii) PREFACTORED.
    """
    d = np.load(ENVELOPE_PIN_NPZ, allow_pickle=True)  # (local)

    alpha = float(d["alpha"])              # (local) 4.690533158119443  (W1-4 pin)
    intercept = float(d["intercept"])      # (local) 0.6217547500863554 = ln C
    env_field_npz = float(d["env_at_Lmax10"])   # (local) the npz-stored env field (BARE per W1-4 src)
    level3_npz = float(d["level3_anchor"])      # (local) 3.0e-4 stored in W1-4 npz (cross-check)
    upstream_registry_pass = bool(d["registry_pass_at_Lmax10"])  # (local) False (W1-4)
    l2_subclass = str(d["level_2_subclass"])     # (local) 'Level-2-binding'

    # --- The two PRE-REGISTERED comparator candidates, recomputed from first principles ---
    C = np.exp(intercept)                                # (local) envelope amplitude
    env_bare_Lmax10 = 10.0 ** (-alpha)                   # (local) candidate (i)  BARE L^{-alpha}
    env_prefac_Lmax10 = C * 10.0 ** (-alpha)             # (local) candidate (ii) PREFACTORED C*L^{-alpha}

    # --- Level-3 anchor (Q3a) = 1 - Gamma_effacement (canonical) ---
    level3 = LEVEL3_ANCHOR                               # (local) 3.0e-4 = 1 - 0.9997

    # --- PLAN-TEXT-DRIFT detection: the plan equates env_at_Lmax10 with the PREFACTORED
    #     form; verify which candidate the stored npz field actually equals. ---
    npz_field_is_bare = abs(env_field_npz - env_bare_Lmax10) < 1e-15       # (local)
    npz_field_is_prefac = abs(env_field_npz - env_prefac_Lmax10) < 1e-15   # (local)
    plan_text_drift = (npz_field_is_bare and not npz_field_is_prefac)      # (local)

    # --- PRE-REGISTERED inequality: PASS iff level3 < env_prefac (candidate (ii) x Q3a) ---
    level2_reconciled = env_prefac_Lmax10                # (local) PRE-REGISTERED Level-2
    level3_reconciled = level3                           # (local) PRE-REGISTERED Level-3
    signed_margin = level2_reconciled - level3_reconciled   # (local) <0 => FAIL
    registry_pass_prefac = level3_reconciled < level2_reconciled  # (local) strict <

    # --- Robustness: outcome under the OTHER candidate (i) BARE, for INFO-vs-FAIL test ---
    registry_pass_bare = level3 < env_bare_Lmax10        # (local)
    # INFO iff the two candidates DISAGREE (outcome flips with the (i)/(ii) choice).
    outcome_ambiguous = (registry_pass_prefac != registry_pass_bare)      # (local)

    # --- Verdict ---
    if outcome_ambiguous:
        verdict = "INFO"   # genuinely ambiguous (i)/(ii) -> 2-agent workshop
    elif registry_pass_prefac:
        verdict = "PASS"
    else:
        verdict = "FAIL"

    # --- Ratios for reporting ---
    ratio_l3_over_l2_prefac = level3_reconciled / level2_reconciled       # (local)
    ratio_l2_over_l3_prefac = level2_reconciled / level3_reconciled       # (local)

    print()
    print(f"{'='*72}")
    print("§VII.AM Level-2/Level-3 envelope-row reconciliation @ L_max=10")
    print(f"{'='*72}")
    print(f"  alpha (W1-4 pin)           = {alpha:.15f}")
    print(f"  intercept = ln C           = {intercept:.15f}")
    print(f"  C = exp(intercept)         = {C:.15f}")
    print(f"  Level-2 candidate (i)  BARE      10^(-alpha)        = {env_bare_Lmax10:.6e}")
    print(f"  Level-2 candidate (ii) PREFACTORED C*10^(-alpha)   = {env_prefac_Lmax10:.6e}  <- PRE-REGISTERED")
    print(f"  npz env_at_Lmax10 field          = {env_field_npz:.6e}")
    print(f"    npz field == BARE?   {npz_field_is_bare}   npz field == PREFAC?  {npz_field_is_prefac}")
    print(f"    PLAN-TEXT-DRIFT (plan calls npz field 'prefactored'; it is BARE) = {plan_text_drift}")
    print(f"  Level-3 anchor (Q3a) = 1 - Gamma_effacement        = {level3:.6e}")
    print(f"    cross-check vs W1-4 npz level3_anchor {level3_npz:.6e}: "
          f"match={abs(level3 - level3_npz) < 1e-12}")
    print(f"  l2_subclass (W1-4)         = {l2_subclass}")
    print()
    print("  --- PRE-REGISTERED inequality (candidate (ii) PREFACTORED x Q3a) ---")
    print(f"    PASS <=> Level-3 ({level3_reconciled:.6e}) < Level-2_prefac ({level2_reconciled:.6e})")
    print(f"    signed margin (L2_prefac - L3) = {signed_margin:.6e}  ({'>=0' if signed_margin >= 0 else '<0'})")
    print(f"    Level-3 / Level-2_prefac = {ratio_l3_over_l2_prefac:.6f}  "
          f"(> 1 => Level-3 above the envelope => FAIL)")
    print(f"    registry_pass (prefac)   = {registry_pass_prefac}")
    print(f"    registry_pass (bare)     = {registry_pass_bare}  [robustness]")
    print(f"    outcome_ambiguous (i!=ii)= {outcome_ambiguous}")
    print(f"    upstream W1-4 registry_pass_at_Lmax10 = {upstream_registry_pass}")
    print()
    print(f"  VERDICT = {verdict}")
    print(f"{'='*72}")

    value_str = (
        f"L3={level3_reconciled:.6e}_vs_L2prefac={level2_reconciled:.6e}@Lmax10;"
        f"ratio_L3/L2={ratio_l3_over_l2_prefac:.4f}(>1=>FAIL);"
        f"alpha={alpha:.4f};C=exp({intercept:.4f})={C:.4f};"
        f"L2bare={env_bare_Lmax10:.6e}(=npz_env_field);"
        f"registry_pass_prefac={registry_pass_prefac};registry_pass_bare={registry_pass_bare};"
        f"ambiguous={outcome_ambiguous};"
        f"PLAN-TEXT-DRIFT=npz_env_at_Lmax10_is_BARE_not_prefac({plan_text_drift});"
        f"theorem-STRUCTURE=STAGE-3-PERMANENT(out-of-scope)"
    )  # (local)

    return {
        "value": value_str,
        "verdict": verdict,
        "alpha": alpha,
        "intercept": intercept,
        "C": C,
        "env_bare_Lmax10": env_bare_Lmax10,
        "env_prefac_Lmax10": env_prefac_Lmax10,
        "env_field_npz": env_field_npz,
        "level3": level3,
        "level3_npz": level3_npz,
        "level2_reconciled": level2_reconciled,
        "level3_reconciled": level3_reconciled,
        "signed_margin": signed_margin,
        "ratio_l3_over_l2_prefac": ratio_l3_over_l2_prefac,
        "ratio_l2_over_l3_prefac": ratio_l2_over_l3_prefac,
        "registry_pass_prefac": registry_pass_prefac,
        "registry_pass_bare": registry_pass_bare,
        "outcome_ambiguous": outcome_ambiguous,
        "npz_field_is_bare": npz_field_is_bare,
        "npz_field_is_prefac": npz_field_is_prefac,
        "plan_text_drift": plan_text_drift,
        "upstream_registry_pass": upstream_registry_pass,
        "l2_subclass": l2_subclass,
        "gamma_effacement": float(Gamma_effacement),
    }


def make_plot(res: dict) -> None:
    """Level-3 anchor vs BOTH comparator-candidate Level-2 envelopes across L."""
    d = np.load(ENVELOPE_PIN_NPZ, allow_pickle=True)  # (local)
    L_fit = np.asarray(d["L_fit"], dtype=float)        # (local) [8,9,10,11]
    alpha = res["alpha"]                               # (local)
    C = res["C"]                                       # (local)

    L = np.linspace(7.5, 12.5, 200)                    # (local)
    env_bare = L ** (-alpha)                           # (local) candidate (i)
    env_prefac = C * L ** (-alpha)                     # (local) candidate (ii) PRE-REGISTERED
    level3 = res["level3"]                             # (local)

    fig, ax = plt.subplots(figsize=(8.0, 5.4))
    ax.loglog(L, env_prefac, "-", color="#c62828", lw=2.2,
              label=r"Level-2 (ii) PREFACTORED $C\,L^{-\alpha}$  [PRE-REGISTERED]")
    ax.loglog(L, env_bare, "--", color="#1565c0", lw=1.8,
              label=r"Level-2 (i) BARE $L^{-\alpha}$  (= npz env field)")
    ax.axhline(level3, color="black", ls=":", lw=2.0,
               label=fr"Level-3 anchor $1-\Gamma_{{\rm eff}}={level3:.1e}$")
    ax.axvline(10.0, color="gray", ls="-.", lw=1.2, alpha=0.7,
               label=r"$L_{\max}=10$ (Registry-PASS point)")

    # Mark the L_max=10 evaluation points.
    ax.plot([10.0], [res["env_prefac_Lmax10"]], "o", color="#c62828", ms=9, zorder=5)
    ax.plot([10.0], [res["env_bare_Lmax10"]], "s", color="#1565c0", ms=8, zorder=5)
    ax.plot([10.0], [level3], "D", color="black", ms=8, zorder=5)

    ax.annotate(
        f"Level-3 ({level3:.2e}) > Level-2_prefac ({res['env_prefac_Lmax10']:.2e})\n"
        f"=> ratio {res['ratio_l3_over_l2_prefac']:.2f} > 1  =>  envelope ROW FAIL\n"
        f"(theorem-STRUCTURE STAGE-3-PERMANENT, out of scope)",
        xy=(10.0, level3), xytext=(8.2, 6e-4),
        fontsize=8.4, color="black",
        bbox=dict(boxstyle="round", fc="#fff8e1", ec="gray", alpha=0.95))

    ax.set_xlabel(r"$L_{\max}$ (regulator-axis truncation)")
    ax.set_ylabel(r"$\delta\Gamma_{\rm eff}/\Gamma_{\rm eff}$  /  Level-2 envelope")
    ax.set_title(r"§VII.AM Level-2/Level-3 envelope-row reconciliation ($\alpha=4.6905$ pinned)")
    ax.legend(loc="lower left", fontsize=8.0)
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot written: {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict: str | None = None,
                          magnitude_verdict: str | None = None,
                          regime_verdict: str | None = None,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout) + plan-pin feasibility check
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    npz_rel = str(ENVELOPE_PIN_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    npz_sha_now = pins.get(npz_rel, "")  # (local)
    print(f"  W1-4 envelope-pin npz SHA: {npz_sha_now[:16]}... "
          f"(plan pin {PLAN_PINNED_NPZ_SHA[:16]}...; "
          f"match={npz_sha_now == PLAN_PINNED_NPZ_SHA})")
    if npz_sha_now != PLAN_PINNED_NPZ_SHA:
        print("  WARNING: envelope-pin npz SHA differs from plan-pinned value.")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    res = compute()
    verdict = res["verdict"]

    # 3. Plot
    make_plot(res)

    # 4. Persist npz
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        value=res["value"],
        alpha=res["alpha"],
        intercept=res["intercept"],
        C=res["C"],
        env_bare_Lmax10=res["env_bare_Lmax10"],
        env_prefac_Lmax10=res["env_prefac_Lmax10"],
        env_field_npz=res["env_field_npz"],
        level3=res["level3"],
        level3_npz=res["level3_npz"],
        level2_reconciled=res["level2_reconciled"],
        level3_reconciled=res["level3_reconciled"],
        signed_margin=res["signed_margin"],
        ratio_l3_over_l2_prefac=res["ratio_l3_over_l2_prefac"],
        ratio_l2_over_l3_prefac=res["ratio_l2_over_l3_prefac"],
        registry_pass_prefac=res["registry_pass_prefac"],
        registry_pass_bare=res["registry_pass_bare"],
        outcome_ambiguous=res["outcome_ambiguous"],
        npz_field_is_bare=res["npz_field_is_bare"],
        npz_field_is_prefac=res["npz_field_is_prefac"],
        plan_text_drift=res["plan_text_drift"],
        upstream_registry_pass=res["upstream_registry_pass"],
        l2_subclass=res["l2_subclass"],
        gamma_effacement=res["gamma_effacement"],
        comparator_decision="PRE-REGISTERED:Level-2=prefactored(ii)C*L^-alpha;Level-3=Q3a(1-Gamma_eff=3.0e-4)",
        scope="envelope-ROW-only;theorem-STRUCTURE=STAGE-3-PERMANENT-out-of-scope",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        plan_pinned_npz_sha=PLAN_PINNED_NPZ_SHA,
        npz_sha_at_runtime=npz_sha_now,
    )
    print(f"  npz written: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 5. Emit 4-tuple + PRINT the emit_verdict payload (agent calls emit_verdict).
    #    [VERIFY] trigger with a directional (threshold) prediction -> emit the 3-tuple
    #    so the SIGN of the envelope-vs-anchor inequality is pinned for downstream.
    #    sign     = direction of (Level-2_prefac - Level-3) matches the pre-registered
    #               PASS direction (predicted >0 for PASS); computed <0 => sign FAIL.
    #    magnitude= |Level-3 - Level-2_prefac| vs the strict-< criterion (no band) => FAIL.
    #    regime   = closed-form evaluation on the full pinned (alpha, intercept); VALID.
    sign_v = "PASS" if res["signed_margin"] > 0 else "FAIL"  # (local)
    mag_v = "PASS" if res["registry_pass_prefac"] else "FAIL"  # (local)
    regime_v = "VALID"  # (local) closed-form; no truncation/expansion window to breach
    extra = [
        ("# regulator_pin: Level-2 envelope delta_Gamma_eff/Gamma_eff ~ C*L^{-alpha}, "
         "alpha=4.6905 (Pauli-Villars-class S58 effacement L-scan, Lref=12); "
         "Level-2-binding sub-class (HKR-image convergence-rate bound)"),
        ("# comparator-decision PRE-REGISTERED (plan §W2-4, frozen before compute): "
         "Level-2=(ii)PREFACTORED C*L^-alpha (envelope-is-a-bound carries amplitude C); "
         "Level-3=(Q3a) 1-Gamma_effacement=3.0e-4; anti-comparator-shopped: prefac is the "
         "MORE-favorable candidate (3.80e-05 > bare 2.04e-05) yet STILL < Level-3 3.0e-4 => FAIL"),
        ("# PLAN-TEXT-DRIFT (substrate-first-canonical-sourcing §(ii.B)): plan line 756 "
         "mislabels npz env_at_Lmax10 as prefactored; it is BARE 10^-alpha (W1-4 src line 556). "
         "True prefactored recomputed here = 3.7974e-05. Outcome FAIL robust to the mislabel."),
        ("# scope: §VII.AM 3-clause joint theorem (Level-1) STAGE-3-PERMANENT, OUT OF SCOPE; "
         "only Element-4 / Level-2-vs-Level-3 Registry-PASS ROW re-evaluated. "
         "dual_prior: FAIL => 0.9 to Track B (envelope ROW fails, theorem-STRUCTURE intact)"),
    ]  # (local)
    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(
        verdict, res["value"], audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note="VIIAM envelope-ROW reconciliation; theorem-STRUCTURE out of scope",
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # verdict is data; FAIL is a valid scientific result (exit 0)


if __name__ == "__main__":
    sys.exit(main())
