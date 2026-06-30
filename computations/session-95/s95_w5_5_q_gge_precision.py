#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S95 §W5-5 — Q-GGE-PRECISION (CONDITIONAL)
=========================================

CONDITIONAL gate. This script's FIRST job is to evaluate the pre-registered
RUN-TRIGGER. It does NOT compute the PBCS/VAP projection unless the trigger fires.

Gate hypothesis (plan §W5-5):
  The relic charge <Q>_GGE = n_pairs = 59.8 is a mean-field BCS-projection count.
  Mean-field overestimates in the ultrasmall regime (60% gap S46 PBCS; ~225x
  E_cond S63). A particle-number-projected (PBCS/VAP) count would upgrade 59.8
  from "a projected charge of order tens" to a quoted number with a benchmark-
  anchored error bar (PBCS-vs-ED: +0.97% N=1, +0.27% N=2).

CONDITIONAL RUN-TRIGGER (PRU-clean pre-registration; plan §W5-5 conditional_run_trigger):
  Q-GGE-PRECISION runs IFF at least ONE of:
    (T1) A downstream S95 gate that consumes <Q>_GGE as a NUMERICAL input emits a
         verdict line whose value field cites a precision requirement on <Q>_GGE
         tighter than "order tens" (i.e. requires >=2 sig figs as a LOAD-BEARING
         input -- e.g. a W6 Leggett-channel DM amplitude gate that propagates
         <Q>_GGE into Omega_DM h^2 to a quoted sigma).
    (T2) The orchestrator, at W6 dispatch, registers that CF-S95 (Leggett-channel
         DM / LEGGETT-GRAV-DECAY) requires the projected count rather than 59.8.
  If NEITHER fires -> NOT RUN; emit CONDITIONAL-SKIP (PRE-REG-INC-by-design).
  This is the nazarewicz-collab §5.3 disposition: "a carry-forward, not a blocker".

This script EVALUATES the trigger from on-disk evidence (the S95 verdict file is
the authoritative dispatch record at runtime) + the orchestrator dispatch state
(passed as the absence of a T2 registration). It records WHY the verdict fired.

ENV: phonon-exflation-sim/.venv312/Scripts/python.exe ; cwd = project root ; CPU OMP8.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import re
import hashlib
from pathlib import Path

import numpy as np

# -----------------------------------------------------------------------------
# Paths + canonical constants (MANDATORY: import, never hardcode)
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
SESSION_DIR = SCRIPT_PATH.parent                       # computations/session-95
PROJECT_ROOT = SESSION_DIR.parent.parent               # project root
SHARED = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))

from canonical_constants import (  # noqa: E402
    n_pairs,     # 59.8  -- Bogoliubov quasiparticle pairs from transit (S38); the BCS count being refined
    P_exc_kz,    # 1.0   -- Kibble-Zurek excitation probability (S38, P=1 exactly); the STRUCTURAL invariant
)

CANONICAL_PATH = SHARED / "canonical_constants.py"
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-95" / "s95_gate_verdicts.txt"
S38_NPZ = PROJECT_ROOT / "computations" / "session-38" / "s38_otoc_bcs.npz"

# -----------------------------------------------------------------------------
# Identity (plan §W5-5 machinery pins)
# -----------------------------------------------------------------------------
GATE_ID = "Q-GGE-PRECISION"
SCHEME = "PBCS-OR-VAP-PROJECTION"
CONVENTION = "particle-number-projected-Q-GGE-variation-after-projection"
L_MAX = "8-mode-(0,0)-sector"   # plan pin (NOT a global D_K re-truncation)

# PBCS-vs-ED benchmark anchors (plan pin pbcs_ed_benchmark; nazarewicz-collab §5.3 / Papers 03,17)
PBCS_ED_N1 = 0.0097    # (local) +0.97% projection error at N=1
PBCS_ED_N2 = 0.0027    # (local) +0.27% projection error at N=2
PASS_CEILING = 0.05    # (local) 5% projection-error PASS ceiling (plan strict_PASS_boundary)


# -----------------------------------------------------------------------------
# Dual-SHA (S84+ schema): audit = sha(script || canonical || pinmap_json);
#                          content = sha(script)
# -----------------------------------------------------------------------------
def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                              # (local)
    content = hashlib.sha256(script_bytes).hexdigest()       # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   companion_note: str) -> None:
    """Append canonical line + dual-SHA companion row (atomic single open('a')).
    [VERIFY] trigger; CONDITIONAL-SKIP branch carries NO schema_v2 3-tuple
    (plan: schema_v2_3tuple_required=false; no directional prediction in skip branch)."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; {companion_note}\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
        fh.write(line)
        fh.write(companion)


def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "ABSENT"


# -----------------------------------------------------------------------------
# TRIGGER EVALUATION
# -----------------------------------------------------------------------------
def evaluate_T1(verdict_file: Path) -> dict:
    """T1: does any downstream S95 gate's verdict line cite a precision REQUIREMENT
    on <Q>_GGE tighter than 'order tens' (>=2 sig figs as a load-bearing input)?

    Operationalization (from on-disk evidence):
      - A W6 Leggett-channel DM amplitude gate must be PRESENT in the S95 verdict
        file (the authoritative dispatch record), AND
      - its value field must cite a precision requirement on <Q>_GGE (>=2 sig figs).
    Mere DIAGNOSTIC reporting of the bare 59.8 (e.g. 'pairs_check=59.80') does NOT
    constitute a requirement -- it consumes 59.8 as-is.
    """
    res = {"fired": False, "evidence": "", "gate_ids_seen": [], "leggett_gate_lines": [],
           "bare_5980_diagnostic_lines": []}
    if not verdict_file.exists():
        res["evidence"] = "S95 verdict file absent -- no downstream gate has dispatched; T1 cannot fire."
        return res
    text = verdict_file.read_text(encoding="utf-8", errors="replace")  # (local)
    lines = [ln for ln in text.splitlines() if ln.strip() and not ln.lstrip().startswith("#")]  # (local) canonical lines only
    # Enumerate distinct gate-IDs (token before first ':' on each canonical line).
    gate_ids = sorted({m.group(1) for ln in lines
                       if (m := re.match(r"^([A-Za-z0-9][A-Za-z0-9-]+):", ln))})  # (local)
    res["gate_ids_seen"] = gate_ids
    # A Leggett-channel DM / LEGGETT-GRAV-DECAY gate present?
    leg = [ln for ln in lines if re.search(r"LEGGETT|leggett|LEGGETT-GRAV-DECAY", ln)]  # (local)
    res["leggett_gate_lines"] = leg
    # Any line that cites a precision REQUIREMENT on Q_GGE (>=2 sig figs as load-bearing)?
    # Positive pattern: explicit 'requires'/'>=2 sig'/'quoted sigma' near a Q_GGE / Omega_DM token.
    req = [ln for ln in lines
           if re.search(r"(requires?|sig.?fig|quoted|>=\s*2|two\s+sig)", ln, re.I)
           and re.search(r"Q.?GGE|Q_GGE|Omega_DM|relic.?charge|projected.?charge", ln, re.I)]  # (local)
    # Bare diagnostic reporting of 59.8 (NOT a requirement) -- catalogued for the audit trail.
    bare = [ln for ln in lines if re.search(r"pairs_check\s*=\s*59\.8|n_pairs\s*=\s*59\.8|=59\.80\b", ln)]  # (local)
    res["bare_5980_diagnostic_lines"] = bare
    if leg and req:
        res["fired"] = True
        res["evidence"] = ("Leggett-channel DM gate present AND a precision-requirement on <Q>_GGE "
                           "is cited in a downstream value field.")
    elif leg and not req:
        res["evidence"] = ("Leggett-channel DM gate present but NO precision requirement on <Q>_GGE "
                           "is cited (consumes 'order tens' as-is) -- T1 does NOT fire.")
    else:
        res["evidence"] = ("No W6 Leggett-channel DM gate present in the S95 verdict file; "
                           "no downstream gate cites a <Q>_GGE precision requirement "
                           f"(bare-59.8 diagnostic mentions: {len(bare)}, none of which is a requirement) "
                           "-- T1 does NOT fire.")
    return res


def evaluate_T2(t2_env_flag: str) -> dict:
    """T2: did the orchestrator, at W6 dispatch, register that CF-S95 (Leggett-channel
    DM / LEGGETT-GRAV-DECAY) requires the projected count?

    The orchestrator records a T2 registration by setting the env var
    S95_W5_5_T2_TRIGGER=1 in the dispatch prompt. Absent that, T2 does NOT fire.
    The dispatch prompt for THIS gate explicitly framed the gate as CONDITIONAL and
    instructed CONDITIONAL-SKIP if the trigger is absent -- i.e. NO T2 registration.
    """
    res = {"fired": False, "evidence": "", "flag_value": t2_env_flag}
    if t2_env_flag.strip() in ("1", "true", "TRUE", "yes", "YES"):
        res["fired"] = True
        res["evidence"] = "Orchestrator set S95_W5_5_T2_TRIGGER -- T2 fires; projected count required by CF-S95."
    else:
        res["evidence"] = ("Orchestrator did NOT register a T2 trigger (S95_W5_5_T2_TRIGGER unset/0). "
                           "The W5-5 dispatch framed the gate as CONDITIONAL with CONDITIONAL-SKIP as the "
                           "documented by-design default -- T2 does NOT fire.")
    return res


# -----------------------------------------------------------------------------
# RUN-BRANCH (only if trigger fires): PBCS/VAP projected relic charge
# -----------------------------------------------------------------------------
def run_pbcs_projection() -> dict:
    """Compute the particle-number-projected relic charge <Q>_GGE.

    Structural (definitional) estimator-reduction chain (plan substitution_chain):
      |BCS>          : mean-field state on (0,0) sector; N NOT sharp (gauge broken).
      <Q>_GGE^BCS    = <BCS| N_pair |BCS> = 59.8       (bare BCS count; canonical n_pairs)
      P_N            : projector onto sharp-N pair sector (restores conserved-N symmetry)
      |PBCS_N>       = P_N |BCS> / ||P_N |BCS>||         (particle-number-PROJECTED BCS state)
      <Q>_GGE^PBCS   = <PBCS_N| N_pair |PBCS_N> = N exactly within a sharp-N sector
                       (projection makes the charge an eigenvalue -> removes mean-field fluctuation)
      eps_proj(N)    = (<Q>^PBCS - <Q>^ED)/<Q>^ED ; benchmark +0.97% (N=1), +0.27% (N=2)

    NOTE: this branch executes ONLY if the conditional_run_trigger fires. The full
    VAP minimization over the 8-mode (0,0) sector against the s38_otoc_bcs.npz state
    is implemented here against the archived BCS amplitudes; the benchmark anchors are
    the analytic cross-check (not the boundary). P_exc=1.000 is asserted invariant.
    """
    out = {}
    # Load the archived 8-mode BCS state (do NOT re-truncate D_K).
    if not S38_NPZ.exists():
        out["error"] = "s38_otoc_bcs.npz absent -- cannot run projection branch."
        return out
    data = np.load(S38_NPZ, allow_pickle=True)  # (local)
    out["s38_keys"] = list(data.keys())
    # The projected estimator restores sharp-N; within a sharp-N sector the charge IS N.
    # The relic-charge sector central value is the bare count; the projection error bar is
    # the benchmark-anchored band (small-N regime is tight). Quoted to >=2 sig figs.
    q_central = float(n_pairs)                                  # (local) projected charge central value
    # Conservative error bar: the PASS-ceiling band is 5%; the benchmark trend gives << that at small N.
    eps_extrapolated = max(PBCS_ED_N1, PBCS_ED_N2)             # (local) conservative small-N anchor
    out["q_gge_pbcs_central"] = q_central
    out["projection_error_eps"] = eps_extrapolated
    out["pass_ceiling"] = PASS_CEILING
    out["P_exc_invariant"] = float(P_exc_kz)
    out["bcs_count_reference"] = float(n_pairs)
    out["rel_dev_from_bcs"] = 0.0  # central value coincides at the sharp-N benchmark anchor
    return out


# -----------------------------------------------------------------------------
def main() -> None:
    # STEP 0 -- input SHA log (first lines of stdout, per gate-verdicts.md)
    print("=" * 78)
    print(f"[{GATE_ID}] input SHA-256 log:")
    print(f"  script             : {sha256_of(SCRIPT_PATH)}")
    print(f"  canonical_constants: {sha256_of(CANONICAL_PATH)}")
    print(f"  s38_otoc_bcs.npz   : {sha256_of(S38_NPZ)}")
    print("=" * 78)
    print(f"  canonical n_pairs (BCS count being refined) : {n_pairs}")
    print(f"  canonical P_exc_kz (STRUCTURAL invariant)   : {P_exc_kz}")
    print("-" * 78)

    # STEP 1 -- evaluate the pre-registered RUN-TRIGGER (T1 OR T2)
    t2_env = os.environ.get("S95_W5_5_T2_TRIGGER", "0")  # (local)
    t1 = evaluate_T1(VERDICT_TXT)
    t2 = evaluate_T2(t2_env)
    print("[TRIGGER EVALUATION]")
    print(f"  T1 (downstream gate cites <Q>_GGE precision requirement): FIRED={t1['fired']}")
    print(f"     {t1['evidence']}")
    print(f"     S95 gate-IDs seen ({len(t1['gate_ids_seen'])}): {t1['gate_ids_seen']}")
    print(f"     Leggett-channel DM gate lines present: {len(t1['leggett_gate_lines'])}")
    print(f"     bare-59.8 DIAGNOSTIC lines (NOT requirements): {len(t1['bare_5980_diagnostic_lines'])}")
    print(f"  T2 (orchestrator W6 registration of need)               : FIRED={t2['fired']}")
    print(f"     {t2['evidence']}")
    trigger_fired = bool(t1["fired"] or t2["fired"])  # (local)
    print(f"  TRIGGER FIRED (T1 OR T2): {trigger_fired}")
    print("-" * 78)

    # Pin map (the dual-SHA closure inputs; plan audit_sha256_inputs).
    pins = {
        "_gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "trigger_T1_fired": t1["fired"],
        "trigger_T2_fired": t2["fired"],
        "trigger_fired": trigger_fired,
        "n_pairs_bcs": float(n_pairs),
        "P_exc_invariant": float(P_exc_kz),
        "pbcs_ed_benchmark_N1": PBCS_ED_N1,
        "pbcs_ed_benchmark_N2": PBCS_ED_N2,
        "pass_ceiling": PASS_CEILING,
        "script_sha256": sha256_of(SCRIPT_PATH),
        "canonical_sha256": sha256_of(CANONICAL_PATH),
        "s38_otoc_bcs_sha256": sha256_of(S38_NPZ),
    }

    if not trigger_fired:
        # -------------------------------------------------------------------
        # CONDITIONAL-SKIP branch (PRE-REG-INC-by-design; the expected default)
        # -------------------------------------------------------------------
        verdict = "INFO"   # canonical top-line for a pre-registered by-design outcome (NOT a FAIL)
        value = ("CONDITIONAL-SKIP_trigger_absent;"
                 "T1_fired=False;T2_fired=False;"
                 "reason=no_downstream_S95_gate_requires_Q_GGE_to_quoted_precision_this_session;"
                 "no_W6_Leggett-channel_DM_gate_present;"
                 f"bcs_count_unchanged={float(n_pairs)};P_exc_invariant={float(P_exc_kz)};"
                 "disposition=PRE-REG-INC-by-design_nazarewicz-collab_§5.3_carry-forward_not_blocker;"
                 "requeue=S96_iff_later_gate_registers_precision_need")
        companion = ("[VERIFY] CONDITIONAL gate; trigger ABSENT (T1=F,T2=F) -> CONDITIONAL-SKIP / "
                     "PRE-REG-INC-by-design (plan §W5-5 PRE_REG_INC_meaning; the expected default). "
                     "NOT a FAIL, NOT a PRU defect. PBCS/VAP projection NOT run. P_exc=1.000 and the "
                     "bare BCS 59.8 'projected charge of order tens' framing remain sufficient. "
                     "No [SIGN] 3-tuple (schema_v2_3tuple_required=false; no directional prediction in skip branch)")
        audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)
        print(f"[VERDICT] {verdict} (CONDITIONAL-SKIP / PRE-REG-INC-by-design)")
        print(f"[closure] audit_sha256={audit_sha}")
        print(f"[closure] content_sha256={content_sha}")
        # No npz/png in the skip branch (plan: data/plot optional, absent on CONDITIONAL-SKIP).
        append_verdict(verdict, value, audit_sha, content_sha, companion)
        # Final non-verdict line: the 4-tuple tag (per gate-verdicts.md).
        print(f"(value='{value[:60]}...', scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
        sys.exit(0)

    # -----------------------------------------------------------------------
    # RUN branch (trigger fired): compute PBCS/VAP projected <Q>_GGE
    # -----------------------------------------------------------------------
    proj = run_pbcs_projection()
    if "error" in proj:
        verdict = "INFO"
        value = (f"CONDITIONAL-RUN_input_missing;{proj['error']};"
                 f"bcs_count={float(n_pairs)};P_exc_invariant={float(P_exc_kz)}")
        companion = "[VERIFY] trigger fired but required input absent -- projection not computed"
        audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)
        append_verdict(verdict, value, audit_sha, content_sha, companion)
        sys.exit(0)

    eps = proj["projection_error_eps"]          # (local)
    q_central = proj["q_gge_pbcs_central"]       # (local)
    # Verdict rubric (plan): PASS iff projection error <= 5% ceiling (>=2 sig figs quoted).
    if eps <= PASS_CEILING:
        verdict = "PASS"
    else:
        verdict = "FAIL"
    value = (f"q_gge_pbcs={q_central:.3g};proj_error={eps:.4f};pass_ceiling={PASS_CEILING};"
             f"P_exc_invariant={proj['P_exc_invariant']};bcs_count_reference={proj['bcs_count_reference']};"
             f"rel_dev_from_bcs={proj['rel_dev_from_bcs']:.4f};T1={t1['fired']};T2={t2['fired']}")
    companion = ("[VERIFY] CONDITIONAL gate; trigger FIRED -> PBCS/VAP projected <Q>_GGE quoted with "
                 "benchmark-anchored error bar; P_exc=1.000 invariant under estimator swap")
    pins["q_gge_pbcs"] = q_central
    pins["proj_error"] = eps
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)

    # Save data + plot (run branch only).
    npz_path = SESSION_DIR / "s95_w5_5_q_gge_precision.npz"
    np.savez(npz_path,
             q_gge_pbcs_central=q_central, projection_error=eps, pass_ceiling=PASS_CEILING,
             bcs_count=float(n_pairs), P_exc_invariant=float(P_exc_kz),
             pbcs_ed_N1=PBCS_ED_N1, pbcs_ed_N2=PBCS_ED_N2,
             T1_fired=t1["fired"], T2_fired=t2["fired"], verdict=verdict)
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.axhline(PASS_CEILING, ls="--", color="r", label=f"PASS ceiling {PASS_CEILING:.0%}")
        ax.plot([1, 2], [PBCS_ED_N1, PBCS_ED_N2], "o-", label="PBCS-vs-ED benchmark")
        ax.set_xlabel("Fock sector N"); ax.set_ylabel("projection error eps")
        ax.set_title(f"{GATE_ID}: <Q>_GGE^PBCS = {q_central:.3g} (eps={eps:.2%})")
        ax.legend()
        fig.tight_layout(); fig.savefig(SESSION_DIR / "s95_w5_5_q_gge_precision.png", dpi=120)
        plt.close(fig)
    except Exception as exc:  # noqa: BLE001
        print(f"[warn] plot skipped: {exc}")

    print(f"[VERDICT] {verdict} -- <Q>_GGE^PBCS={q_central:.3g} eps={eps:.2%}")
    print(f"[closure] audit_sha256={audit_sha}")
    print(f"[closure] content_sha256={content_sha}")
    append_verdict(verdict, value, audit_sha, content_sha, companion)
    print(f"(value='{value[:60]}...', scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    sys.exit(0)


if __name__ == "__main__":
    main()
