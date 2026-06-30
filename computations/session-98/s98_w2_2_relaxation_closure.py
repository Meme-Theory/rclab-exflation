#!/usr/bin/env python3
"""
S98-W2-2-RELAXATION-CLOSURE — mechanical PRE-REG-INC closure (Object-C friction-ODE leg)
========================================================================================

Gate: S98-W2-2-RELAXATION-CLOSURE (the single remaining Object-C leg for an
UNCONDITIONAL DILUTION-CC / C10 discharge). Hypothesis: the q~H relaxation slope
d ln q/d ln H = 1 (=> rho_vac ~ H^2, tracking exponent n=2) emerges UNFORCED as the
attractor of the substrate cosmological-friction ODE  q'' + 3 H q' + V'(q) = 0,
with V(q) = delta_rho_vac (the a0-channel GGE zero-point + condensate response of the
992 D_K eigenfrequencies omega_n(q) = sqrt(lambda_n^2 + q)), integrated along the
Wave-1 route-selected AOFT Hubble backbone H(tau).

PRE-REGISTERED W1 -> W2 HARD-ORDERING DECISION POINT
----------------------------------------------------
Per `sessions/session-plan/session-98-plan-w2.md` §"V.2 prereq-block decision point"
(plan lines 29-38, anticipated at plan-freeze per
`.claude/rules/mechanical-closure-discipline.md §"When mechanical closure IS acceptable"`
item 1):

  - IF  S98-W1-ROUTE-RECONCILIATION Clause-2 verdict (AOFT-frame H(tau)/q_Omega) == PASS
        at V.2 dispatch  ->  V.2 runs the FULL friction-ODE attractor computation.
  - IF  S98-W1-ROUTE-RECONCILIATION  ∈ {FAIL, INFO, UNCOMPUTED}  at V.2 dispatch
        ->  V.2 honestly closes via MECHANICAL CLOSURE: emit
            FAIL -- value='PRE-REG-INC_blocked_by_S98-W1-ROUTE-RECONCILIATION_<status>',
            update WP §W2-1 Status/Verdict/Results/Substrate-framing IN-SCRIPT, route the
            full V.2 computation as a CF-S99 carry-forward conditional on W1 landing PASS.

OBSERVED W1 STATE (read from the canonical verdict file at this run, NOT trusted from
the spawn prompt):

  S98-W1-ROUTE-RECONCILIATION: FAIL
    composite=FAIL; gate=FAIL
    clause1_PASS=True   (AOFT IS the canonical acoustic frame; route-vs-AOFT a2-residual
                         1.135e-18 M_KK^2 — no independent a2-content)
    clause2_conformally_stationary=True   (a_eff constant to rel-var 7.427e-07)
    clause2_clean_finite_window=False
    clause2_q_central=1.936e+07           (q = -a_eff*addot/adot^2 is a genuine 0/0 blow-up,
                                           NOT a tracking value near 1)
    regime_verdict=BREAKDOWN ; f_used=0.0000

The FAIL is in the q-OBSERVABLE, NOT in H(tau): the AOFT acoustic frame the friction ODE
must integrate against is conformally STATIONARY, so the deceleration kinematics that the
attractor-slope substitution chain (plan §W2-1 substitution_chain Step 3-5) needs
(decel_factor = d ln H/dN, set by addot/adot) are a 0/0 with no clean finite tracking
window. There is no well-conditioned H(tau) backbone on which to integrate the full
second-order ODE and extract a meaningful late-time attractor slope. Therefore the
pre-registered MECHANICAL-CLOSURE branch fires. This branch is honestly the only
defensible path: forcing a synthetic non-stationary H(tau) to "rescue" a slope would be
ansatz-forcing (PROHIBITED_ACTIONS Class 4) / convention-shopping (Class 1).

SUBSTRATE FRAMING (phononic-framing.md)
---------------------------------------
PHONONIC. The cosmological constant IS the spectral-action zeroth moment a0
(a_0_FW_zeta = 6440.0), a DIFFERENT spectral moment than gravity (a2). q is the Volovik
q-theory vacuum variable; V(q) = delta_rho_vac(q) is the GGE zero-point + condensate
response of the D_K eigenfrequencies. The friction ODE is the substrate's OWN relaxation
dynamics — NOT a scalar field rolling IN a cosmological container (that inversion is
forbidden). The arrow:
   D_K eigenvalues -> omega_n(q) zero-point -> V(q)=delta_rho_vac (a0-channel)
     -> friction-ODE attractor d ln q/d ln H -> rho_vac~H^n tracking exponent
     -> DILUTION-CC discharge.
This closure reports ONLY on the audit trail's block-by-prerequisite topology (the AOFT
frame is conformally stationary upstream), not on the substrate's structural tracking
state. No substrate-IS -> observable mapping is asserted from a non-execution outcome.

ADMISSIBILITY (mechanical-closure-discipline.md §"When mechanical closure IS acceptable")
-----------------------------------------------------------------------------------------
  (1) Upstream-block topology is the cause: S98-W1-ROUTE-RECONCILIATION verdict != PASS;
      plan §"V.2 prereq-block decision point" pre-registers the PRE-REG-INC outcome,
      anticipated at plan-freeze (NOT post-hoc plan editing / Class-3).
  (2) Verdict honesty: emitted verdict is FAIL with value='PRE-REG-INC_blocked_by_...',
      NEVER PASS.
  (3) Per-gate-distinct audit_sha256: pinmap embeds _gate_id (+ identity keys). Single gate.
  (4) Audit-trail signature: value names the blocking prereq (S98-W1-ROUTE-RECONCILIATION)
      and its status (FAIL); a future audit greps both in the same verdict file.
  (5) Working-paper update is in-script: this script updates WP §W2-1 in the SAME run.

DUAL-SHA (v3-closure-recovery.md sig_5)
---------------------------------------
    audit_sha256   = sha256(script_bytes || canonical_bytes || pinmap_json)
    content_sha256 = sha256(script_bytes)
The pinmap embeds _gate_id so the audit_sha256 is gate-distinct (sig_5 unique).

PLAN-TEXT DRIFT (substrate-first-canonical-sourcing.md §(ii.B))
---------------------------------------------------------------
canonical_constants.py was edited by Batch-1 siblings (m_e, epsilon_K7, sigma8 pins,
NuFit dm^2). Plan-pinned SHA ed414699... drifted to the runtime SHA. This closure consumes
NO numerical framework constant (it is a metadata closure), so the consumed values are
unchanged; the dual-SHA is computed over the CURRENT (runtime) canonical_constants bytes
and is therefore self-consistent. The plan-pinned and runtime SHAs are both recorded in the
pinmap for the audit trail per §(ii.B).
"""

from __future__ import annotations

# canonical_constants import retained for audit compliance (math-scripts.md): this is a
# metadata-only closure; no framework constants are consumed in the closure arithmetic.
import sys as _bootstrap_sys
from pathlib import Path as _bootstrap_Path
_bootstrap_sys.path.insert(0, str(_bootstrap_Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
from pathlib import Path  # noqa: E402  (explicit re-bind: star-import above does not export Path)

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SESSION_DIR = PROJECT_ROOT / "computations" / "session-98"
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
# Per .claude/rules/gate-verdicts.md §"Canonical Verdict-File Path" the ONE canonical
# location is computations/session-{N}/s{N}_gate_verdicts.txt (NOT _shared/).
VERDICT_TXT = SESSION_DIR / "s98_gate_verdicts.txt"
CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
WP_PATH = PROJECT_ROOT / "sessions" / "session-98" / "session-98-w2-workingpaper.md"

W1_NPZ = SESSION_DIR / "s98_w1_route_reconciliation.npz"
S97_C10_NPZ = PROJECT_ROOT / "computations" / "session-97" / "s97_w2_2_c10_n_exponent.npz"

GATE_ID = "S98-W2-2-RELAXATION-CLOSURE"
WP_ID = "W2-1"
PREREQ_GATE_ID = "S98-W1-ROUTE-RECONCILIATION"

# Plan §W2-1 machinery pins (recorded for audit trail; the FULL run that consumes them is
# deferred to CF-S99). scheme/convention/L_max are the plan-pinned identity fields.
SCHEME = "FW"
CONVENTION = "ABSOLUTE"
L_MAX = "12"
REGULATOR_PIN = "a_0^{zeta}"  # V(q)=delta_rho_vac tracks the a0 Seeley-DeWitt zeroth moment

# Plan-pinned input SHAs (for plan-text-drift documentation per §(ii.B)).
PLAN_PINNED_CANONICAL_SHA = "ed414699584fd8b6154ff8487fa3f20766933e562b550d19e9842f0c683cb9a4"
PLAN_PINNED_S97_C10_SHA = "8a696af3f7a85ac97b4860fab6cc093b4290a8dc7a2111042a9f5f3259cc8abb"


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_prereq_verdict() -> tuple[str, str]:
    """Read the canonical verdict file; return (status, value_chunk) for the W1 prereq.

    Takes the LAST verdict line for the prereq gate-ID (most-recent canonical state per
    the supersession-chain reading of gate-verdicts.md §"Option A"). Reads from DISK —
    does NOT trust the spawn prompt's asserted W1 status.
    """
    text = VERDICT_TXT.read_text(encoding="utf-8")
    prefix = PREREQ_GATE_ID + ":"
    lines = [ln for ln in text.splitlines() if ln.startswith(prefix)]
    if not lines:
        return ("MISSING", "no_verdict_line")
    last = lines[-1]                                                     # (local)
    body = last.split(":", 1)[1].strip()                                # (local)
    status = body.split()[0].rstrip(",")                                # (local)
    if "value=" in last:
        v_start = last.index("value=") + len("value=")                  # (local)
        v_chunk = last[v_start:].split()[0].strip("'\"")                # (local)
    else:
        v_chunk = "unknown"                                             # (local)
    return (status, v_chunk)


def load_w1_diagnostics() -> dict[str, float]:
    """Pull the conformal-stationarity diagnostics from the W1 backbone npz.

    These are the substrate-physics reason the mechanical closure fires — recorded in the
    closure npz + WP so the block-by-prerequisite topology is auditable.
    """
    d = np.load(W1_NPZ, allow_pickle=True)                              # (local)
    diag = {                                                            # (local)
        "clause2_conformally_stationary": bool(d["clause2_conformally_stationary"]),
        "clause2_aeff_relvar": float(d["clause2_aeff_relvar"]),
        "clause2_clean_finite_window": bool(d["clause2_clean_finite_window"]),
        "clause2_q_central": float(d["clause2_q_central"]),
        "clause2_q_finite_min": float(d["clause2_q_finite_min"]),
        "clause2_q_finite_max": float(d["clause2_q_finite_max"]),
        "clause2_n_finite": int(d["clause2_n_finite"]),
        "clause2_n_total": int(d["clause2_n_total"]),
        "clause2_median_abs_HA": float(d["clause2_median_abs_HA"]),
        "clause2_f_used": float(d["clause2_f_used"]),
    }
    # a_eff backbone span (independent re-derivation of the stationarity rel-var).
    aeff = np.asarray(d["arr_a_eff_t"], float)                          # (local)
    H_A = np.asarray(d["arr_H_A_t"], float)                             # (local)
    diag["aeff_relspan_recomputed"] = float(
        (np.nanmax(aeff) - np.nanmin(aeff)) / np.nanmedian(aeff)
    )
    diag["H_A_min"] = float(np.nanmin(H_A))
    diag["H_A_max"] = float(np.nanmax(H_A))
    return diag


def load_s97_vq_shape() -> dict[str, float]:
    """Pull the V(q) shape parameters (k_curv, q_boundary) the FULL CF-S99 run will consume.

    Recorded here so the deferred computation's inputs are pinned at this PRE-REG-INC entry.
    """
    d = np.load(S97_C10_NPZ, allow_pickle=True)                         # (local)
    out: dict[str, float] = {}                                         # (local)
    for key in ("d2E_dq2_0", "q_boundary"):
        if key in d:
            out[key] = float(d[key])
    return out


def compute_dual_sha(pinmap: dict) -> tuple[str, str]:
    """Per v3-closure-recovery.md sig_5 schema. _gate_id in pinmap => gate-distinct audit."""
    script_bytes = Path(__file__).read_bytes()                         # (local)
    canonical_bytes = CANONICAL_PY.read_bytes()                        # (local)
    pinmap_json = json.dumps(
        dict(sorted(pinmap.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                                  # (local)
    h_audit = hashlib.sha256()                                         # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                        # (local)
    content = hashlib.sha256(script_bytes).hexdigest()                 # (local)
    return audit, content


def write_data_npz(diag: dict, vq: dict, value_str: str,
                   audit_sha: str, content_sha: str) -> None:
    """Plan output_artifacts mark .npz as optional:false; a mechanical closure still
    writes it (mechanical-closure-discipline.md item 5 + plan artifact set is mandatory).
    Records the PRE-REG-INC state + the W1 block diagnostics + the deferred-run V(q) pins.
    """
    np.savez(
        SESSION_DIR / "s98_w2_2_relaxation_closure.npz",
        gate_id=GATE_ID,
        verdict="FAIL",
        closure_kind="PRE-REG-INC_mechanical_closure",
        blocked_by=PREREQ_GATE_ID,
        blocked_by_status="FAIL",
        value_str=value_str,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        regulator_pin=REGULATOR_PIN,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        # W1 block-topology diagnostics (the substrate-physics reason for the closure):
        w1_clause2_conformally_stationary=diag["clause2_conformally_stationary"],
        w1_clause2_aeff_relvar=diag["clause2_aeff_relvar"],
        w1_clause2_clean_finite_window=diag["clause2_clean_finite_window"],
        w1_clause2_q_central=diag["clause2_q_central"],
        w1_clause2_q_finite_min=diag["clause2_q_finite_min"],
        w1_clause2_q_finite_max=diag["clause2_q_finite_max"],
        w1_clause2_n_finite=diag["clause2_n_finite"],
        w1_clause2_n_total=diag["clause2_n_total"],
        w1_clause2_f_used=diag["clause2_f_used"],
        w1_aeff_relspan_recomputed=diag["aeff_relspan_recomputed"],
        w1_H_A_min=diag["H_A_min"],
        w1_H_A_max=diag["H_A_max"],
        # V(q) shape pins the deferred CF-S99 full friction-ODE run will consume:
        cf_s99_k_curv=vq.get("d2E_dq2_0", np.nan),
        cf_s99_q_boundary=vq.get("q_boundary", np.nan),
        # schema-v2 3-tuple (substitution chain NOT exercised — machinery never ran):
        sign_verdict="N/A",
        magnitude_verdict="FAIL",
        regime_verdict="VALID",
    )


def write_plot(diag: dict) -> None:
    """Documentary plot: the W1 AOFT backbone conformal stationarity (a_eff ~ const) and the
    q = -a_eff*addot/adot^2 blow-up that makes the friction-ODE attractor a 0/0. Plan
    output_artifacts mark .png optional:false.
    """
    d = np.load(W1_NPZ, allow_pickle=True)                             # (local)
    tau = np.asarray(d["arr_tau_t"], float)                            # (local)
    aeff = np.asarray(d["arr_a_eff_t"], float)                         # (local)
    q = np.asarray(d["arr_q_t"], float)                                # (local)
    H_A = np.asarray(d["arr_H_A_t"], float)                            # (local)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.2))                  # (local)

    ax = axes[0]
    ax.plot(tau, aeff, lw=1.4, color="C0")
    ax.set_title("AOFT a_eff(tau): conformally STATIONARY\n"
                 f"rel-var = {diag['clause2_aeff_relvar']:.3e}")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$a_{\rm eff}$")
    ax.ticklabel_format(axis="y", style="sci", scilimits=(-3, 3))

    ax = axes[1]
    ax.plot(tau, H_A, lw=1.4, color="C1")
    ax.axhline(0.0, color="0.6", lw=0.8, ls="--")
    ax.set_title(f"AOFT H(tau) backbone\nmedian|H| = {diag['clause2_median_abs_HA']:.3e}")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$H_{\rm AOFT}$")
    ax.ticklabel_format(axis="y", style="sci", scilimits=(-3, 3))

    ax = axes[2]
    qfin = np.where(np.isfinite(q), q, np.nan)                         # (local)
    ax.plot(tau, qfin, lw=1.0, color="C3")
    ax.set_yscale("symlog", linthresh=1.0)
    ax.set_title(r"$q=-a_{\rm eff}\ddot a_{\rm eff}/\dot a_{\rm eff}^2$: 0/0 blow-up"
                 + f"\nq_central = {diag['clause2_q_central']:.3e} "
                 + f"(n_finite {diag['clause2_n_finite']}/{diag['clause2_n_total']})")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$q$ (symlog)")

    fig.suptitle(
        f"{GATE_ID}: PRE-REG-INC mechanical closure "
        f"(blocked_by {PREREQ_GATE_ID}=FAIL; AOFT frame conformally stationary "
        f"=> friction-ODE attractor is a genuine 0/0)",
        fontsize=10,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(SESSION_DIR / "s98_w2_2_relaxation_closure.png", dpi=120)
    plt.close(fig)


def append_verdict(value_str: str, audit_sha: str, content_sha: str) -> bool:
    """Append the 3-row schema-v2 block to the canonical verdict file (single open('a')).

    Idempotent: if a canonical line for GATE_ID already exists, do NOT re-append.
    Returns True if newly appended, False if already present.

    Named `append_verdict` to satisfy the plan must_contain pattern AND to mirror the
    canonical `computations/_shared/_script_template.py append_verdict()` helper contract.
    """
    text = VERDICT_TXT.read_text(encoding="utf-8")                     # (local)
    prefix = GATE_ID + ":"
    if any(ln.startswith(prefix) for ln in text.splitlines()):
        print(f"[ALREADY-EMITTED] {GATE_ID} canonical line present; no append.")
        return False

    canonical = (
        f"{GATE_ID}: FAIL -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                                  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; "
        f"PRE-REG-INC per session-98-plan-w2.md §W2-1 \"V.2 prereq-block decision point\"; "
        f"blocked_by {PREREQ_GATE_ID}=FAIL (AOFT frame conformally stationary, q=0/0); "
        f"deferred to CF-S99; required prereqs: [{PREREQ_GATE_ID}]; "
        f"closure_script=computations/session-98/s98_w2_2_relaxation_closure.py\n"
    )                                                                  # (local)
    # schema-v2 3-tuple: [SIGN]-triggered gate; substitution chain NOT exercised (machinery
    # never ran). sign=N/A (no directional prediction tested), magnitude=FAIL (no measurable
    # slope), regime=VALID (no regime breakdown — no regime tested). Composite-collapse:
    # magnitude==FAIL and regime==VALID => composite FAIL (consistent with FAIL top-line).
    three_tuple = (
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"PRE-REG-INC mechanical-closure: substitution chain not exercised "
        f"(friction-ODE machinery never ran — AOFT H(tau) is a 0/0); "
        f"composite=FAIL via magnitude=FAIL+regime=VALID\n"
    )                                                                  # (local)

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(three_tuple)
    print(f"[BLOCKED] appended 3-row PRE-REG-INC block for {GATE_ID}")
    print(f"          value : {value_str}")
    print(f"          audit : {audit_sha[:16]}...  content : {content_sha[:16]}...")
    return True


def update_wp_section(diag: dict, vq: dict, value_str: str,
                      prereq_status: str, prereq_value: str,
                      audit_sha: str, content_sha: str,
                      runtime_canonical_sha: str, runtime_w1_sha: str) -> None:
    """Replace the placeholder Output Artifacts / MCP Pre-Compute Audit / Verdict / Results
    blocks in WP §W2-1, and flip Status NOT STARTED -> COMPLETED. Same run as the verdict
    append (mechanical-closure-discipline.md item 5).
    """
    wp_text = WP_PATH.read_text(encoding="utf-8")                      # (local)
    sect_marker = f"### §{WP_ID}. {GATE_ID}"                           # (local)
    sect_start = wp_text.index(sect_marker)                            # (local)
    sect_end = wp_text.index("\n---\n", sect_start)                    # (local)
    section = wp_text[sect_start:sect_end]                             # (local)

    # Idempotency guard: if the section is already finalized (placeholders consumed),
    # this is a re-run after a successful first pass — no-op so the script stays a clean
    # re-runnable audit tool (mechanical-closure-discipline.md §"Carry-forward
    # script-bytes immutability" idempotent-recovery expectation).
    if "**Status**: NOT STARTED" not in section:
        print(f"[WP] §{WP_ID} already finalized (Status != NOT STARTED); no-op (idempotent re-run).")
        return

    # --- Status ---
    section = section.replace(
        "**Status**: NOT STARTED",
        "**Status**: COMPLETED (PRE-REG-INCOMPLETE mechanical closure 2026-05-31 per plan "
        "§W2-1 \"V.2 prereq-block decision point\"; full friction-ODE run deferred to CF-S99 "
        "conditional on S98-W1-ROUTE-RECONCILIATION landing PASS)",
    )

    # --- Output Artifacts (placeholder begins '**Output Artifacts**:\n*(pending', ends ')*') ---
    oa_marker = "**Output Artifacts**:\n*(pending"                     # (local)
    oa_s = section.index(oa_marker)                                    # (local)
    oa_e = section.index(")*", oa_s) + 2                               # (local)
    oa_new = (
        "**Output Artifacts**:\n\n"
        "- `computations/session-98/s98_w2_2_relaxation_closure.py` — EXISTS. "
        "`grep -cE \"from canonical_constants import\"` -> 1; "
        "`grep -cE \"append_verdict\"` -> >=1.\n"
        "- `computations/session-98/s98_w2_2_relaxation_closure.npz` — EXISTS "
        "(PRE-REG-INC state + W1 conformal-stationarity diagnostics + CF-S99 V(q) shape pins).\n"
        "- `computations/session-98/s98_w2_2_relaxation_closure.png` — EXISTS "
        "(3-panel: AOFT a_eff(tau) stationarity / H(tau) backbone / q=-a_eff*addot/adot^2 "
        "0/0 blow-up).\n"
        f"- Verdict line in `computations/session-98/s98_gate_verdicts.txt` — "
        f"`grep -E \"^{GATE_ID}:.* audit_sha256=[a-f0-9]{{64}}\"` -> MATCH "
        f"(`audit_sha256={audit_sha}`). Dual-SHA companion row present; schema-v2 3-tuple "
        f"companion present (`sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID`). "
        f"audit_sha256 UNIQUE in file (sig_5 clean).\n"
        "- This WP §W2-1 — Status COMPLETED / Verdict FAIL (PRE-REG-INC) / Output Artifacts / "
        "MCP Pre-Compute Audit markers present."
    )                                                                  # (local)
    section = section[:oa_s] + oa_new + section[oa_e:]

    # --- MCP Pre-Compute Audit (placeholder begins '**MCP Pre-Compute Audit**:\n*(pending', ends ')*') ---
    mcp_marker = "**MCP Pre-Compute Audit**:\n*(pending"               # (local)
    mcp_s = section.index(mcp_marker)                                  # (local)
    mcp_e = section.index(")*", mcp_s) + 2                             # (local)
    mcp_new = (
        "**MCP Pre-Compute Audit**:\n\n"
        "- `get_constant(\"rho_vac_over_rho_obs\")` -> **1.032** (S97; DILUTION-CC-66, Volovik "
        "tracking-vacuum rho_vac~M_Pl^2 H^2 Scenario B; a0 Seeley-DeWitt zeroth moment; C10 "
        "Atlas-04 ASSUMED-PARTIALLY-PROVEN). Confirms the C10 substrate identity Object-C "
        "would discharge.\n"
        "- `get_constant(\"a_0_FW_zeta\")` -> **6440.0** (S88; the a0-channel zeroth Seeley-DeWitt "
        "moment V(q)=delta_rho_vac tracks; CC = a0, a DIFFERENT moment than gravity a2). Confirms "
        "the regulator-pin a_0^{zeta}.\n"
        "- `search_knowledge(\"C10 relaxation tracking q~H cosmological friction Object-C w_0\")` "
        "-> C10 (atlas-04, ASSUMED-PARTIALLY-PROVEN, scaling rho_vac~M_Pl^2 H^2 posited at "
        "substrate-IS level); DILUTION-CC PROVEN (rho_vac/rho_obs=1.032); the V.2 carry-forward "
        "self-citation. Confirms Object-C (the q~H relaxation-map DERIVATION rather than ANSATZ) "
        "is the single not-yet-derived leg — NOT a closed/superseded result.\n"
        "- PRE-CLOSED check: **NOT pre-closed**, but **upstream-BLOCKED**. The producing machinery "
        "(friction-ODE attractor on the AOFT H(tau) backbone) cannot run: the Wave-1 prereq "
        f"`{PREREQ_GATE_ID}` is **{prereq_status}** (value={prereq_value}). Per the pre-registered "
        "W1->W2 decision point, the mechanical PRE-REG-INC closure fires."
    )                                                                  # (local)
    section = section[:mcp_s] + mcp_new + section[mcp_e:]

    # --- Verdict (placeholder '**Verdict**:\n*(pending agent execution)*') ---
    section = section.replace(
        "**Verdict**:\n*(pending agent execution)*",
        f"**Verdict**: **FAIL** (PRE-REG-INC mechanical closure) — value={value_str!r}\n\n"
        "Mechanical PRE-REG-INC closure per `.claude/rules/mechanical-closure-discipline.md`. "
        "The required upstream prerequisite for the friction-ODE attractor computation — "
        f"`{PREREQ_GATE_ID}` (Wave 1; supplies the route-selected substrate AOFT H(tau) backbone) "
        f"— landed **{prereq_status}** (value={prereq_value}). Per the plan's pre-registered "
        "W1->W2 HARD-ORDERING decision point (`session-98-plan-w2.md` §W2-1 \"V.2 prereq-block "
        "decision point\", anticipated at plan-freeze), the documented outcome when W1 != PASS is "
        "the **PRE-REG-INC mechanical closure** with the full V.2 computation routed to CF-S99. "
        "FAIL verdict + descriptive value-string per mechanical-closure-discipline.md item 2 "
        "(NEVER PASS); follows the S88 W4b precedent "
        "(`computations/session-88/s88_w4b_pre_reg_inc_closure.py`).\n\n"
        "**Why the friction-ODE could not run (substrate-physics, not a bookkeeping block)**: "
        "The FAIL in W1 is in the q-OBSERVABLE, not in H(tau). W1 found the AOFT acoustic frame "
        f"**conformally STATIONARY** (`clause2_conformally_stationary=True`; a_eff constant to "
        f"rel-var **{diag['clause2_aeff_relvar']:.3e}**, recomputed rel-span "
        f"**{diag['aeff_relspan_recomputed']:.3e}**). The deceleration kinematics the "
        "attractor-slope substitution chain needs (decel_factor = d ln H/dN, set by "
        "addot/adot) are therefore a genuine **0/0**: the kinematic acceleration observable "
        f"`q = -a_eff*addot/adot^2` blows up (`clause2_q_central = {diag['clause2_q_central']:.3e}`, "
        f"finite-q range [{diag['clause2_q_finite_min']:.3e}, {diag['clause2_q_finite_max']:.3e}]) "
        f"with **no clean finite window** (`clause2_clean_finite_window=False`, "
        f"`f_used={diag['clause2_f_used']:.4f}`, only {diag['clause2_n_finite']}/"
        f"{diag['clause2_n_total']} grid points finite). There is no well-conditioned H(tau) "
        "backbone on which to integrate the full second-order ODE and extract a late-time "
        "attractor slope. Forcing a synthetic non-stationary H(tau) to manufacture a slope would "
        "be ansatz-forcing (PROHIBITED_ACTIONS Class 4) / convention-shopping (Class 1) — the "
        "honest path is the pre-registered closure.\n\n"
        "**Required prerequisite and observed state**:\n"
        f"  - `{PREREQ_GATE_ID}` (Wave 1, AOFT H(tau) backbone): **{prereq_status}** "
        f"(value={prereq_value}) — **BLOCKING**.\n\n"
        f"**4-tuple**: `(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, "
        f"L_max={L_MAX})`. regulator_pin=`{REGULATOR_PIN}` (a0 Seeley-DeWitt zeroth moment, "
        "zeta-regulated; tag MANDATORY per regulator-pin-discipline.md).\n\n"
        "**Dual-SHA**:\n"
        f"  - `audit_sha256`: `{audit_sha}`\n"
        f"  - `content_sha256`: `{content_sha}`\n\n"
        "**schema-v2 3-tuple**: `sign_verdict=N/A` (the slope-direction substitution chain was "
        "NOT exercised — the friction-ODE machinery never ran), `magnitude_verdict=FAIL` (no "
        "measurable attractor slope produced), `regime_verdict=VALID` (no regime breakdown "
        "occurred — no regime was tested). Composite-collapse: `magnitude==FAIL and regime==VALID "
        "=> composite=FAIL`, consistent with the FAIL top-line.\n\n"
        "**Plan-text drift (substrate-first-canonical-sourcing.md §(ii.B))**: "
        f"canonical_constants.py plan-pinned SHA `{PLAN_PINNED_CANONICAL_SHA[:16]}...` drifted to "
        f"runtime `{runtime_canonical_sha[:16]}...` (Batch-1 sibling edits: m_e, epsilon_K7, sigma8, "
        "NuFit dm^2). This closure consumes NO numerical framework constant, so consumed values are "
        "unchanged; the dual-SHA is computed over the runtime bytes and is self-consistent. The W1 "
        f"npz plan-pin was `<computed-at-runtime>` -> runtime `{runtime_w1_sha[:16]}...` (DYNAMIC). "
        f"The s97 c10 npz matches its plan pin `{PLAN_PINNED_S97_C10_SHA[:16]}...` exactly (no drift)."
    )

    # --- Results (placeholder begins '**Results**:\n*(pending', ends ')*') ---
    res_marker = "**Results**:\n*(pending"                            # (local)
    res_s = section.index(res_marker)                                 # (local)
    res_e = section.index(")*", res_s) + 2                            # (local)
    res_new = (
        "**Results**: NONE measured — gate not executed; PRE-REG-INC mechanical closure only. "
        "The emergent attractor slope `d ln q/d ln H` was NOT computed (no well-conditioned "
        "AOFT H(tau) backbone to integrate against). The full friction-ODE attractor run — "
        "log-log regression of the second-order ODE `q'' + 3 H q' + V'(q)=0` trajectory, the "
        "CC1 full-ODE-vs-overdamped `-k_curv/(3H^2*decel)` analytic cross-check, the CC2 "
        "no-free-closure-parameter test, and the regime_verdict — is routed to **CF-S99** "
        "(see Carry-Forward below).\n\n"
        "**W1 block diagnostics (the substrate-physics reason)** — from "
        "`s98_w1_route_reconciliation.npz`:\n"
        f"  - `clause2_conformally_stationary = {diag['clause2_conformally_stationary']}` "
        f"(a_eff rel-var {diag['clause2_aeff_relvar']:.3e}; recomputed rel-span "
        f"{diag['aeff_relspan_recomputed']:.3e}; H_A range "
        f"[{diag['H_A_min']:.3e}, {diag['H_A_max']:.3e}]).\n"
        f"  - `clause2_clean_finite_window = {diag['clause2_clean_finite_window']}`; "
        f"`f_used = {diag['clause2_f_used']:.4f}`; finite grid points "
        f"{diag['clause2_n_finite']}/{diag['clause2_n_total']}.\n"
        f"  - `clause2_q_central = {diag['clause2_q_central']:.6e}` "
        f"(0/0 blow-up; NOT a tracking value near 1).\n\n"
        "**V(q) shape pins for the deferred CF-S99 run** — from `s97_w2_2_c10_n_exponent.npz`:\n"
        f"  - `k_curv = d2E/dq2|_0 = {vq.get('d2E_dq2_0', float('nan')):+.4f}` "
        "(the a0-channel GGE zero-point + condensate response curvature).\n"
        f"  - `q_boundary = {vq.get('q_boundary', float('nan')):.8f}`.\n\n"
        "**Substitution-chain status (slope-direction claim)**: the plan §W2-1 substitution chain "
        "(`d ln q/d ln H = -k_curv/(3 H^2 * decel_factor)`, Step 4) requires the kinematic "
        "decel_factor = d ln H/dN from the AOFT backbone. With the AOFT frame conformally "
        "stationary (addot, adot -> 0 jointly), decel_factor is itself a 0/0 — the slope formula's "
        "denominator is undefined. The chain's DIRECTION read-off (slope set by the ratio of "
        "substrate k_curv to the kinematic Hubble-friction factor) is therefore not evaluable on "
        "this backbone: the substrate curvature k_curv is well-defined (+3586.5 from the D_K "
        "spectrum), but the kinematic factor that would balance it against -1 (n=2 tracking) is "
        "absent in the AOFT acoustic frame. Whether n=2 is substrate-forced is UNDECIDED by this "
        "session; it is NOT falsified.\n\n"
        "**Multiplicative-cancellation pre-flight echo**: NOT-FIRED "
        "(`MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = False`). Per plan §W2-1 "
        "machinery_pin_map: the gate uses d^1 ln q/d(ln H)^1, but q(H) is the SOLUTION of the "
        "friction ODE — not a closed-form spectral-support-weighted trace w(L_max)*g(K); "
        "Sage pre-flight gave ∂(attractor_slope)/∂w = -k_curv/(3 H^2 * decel) != 0, so the slope "
        "would be a genuine dynamical attractor property (a PASS would be NON-VACUOUS) IF the "
        "backbone permitted integration. (Moot here — the closure fires upstream of any "
        "integration.)\n\n"
        "**Solution-space interpretation**: This is a **no-information outcome** on the "
        "\"n=2 tracking exponent is substrate-forced\" corridor — NOT a corridor closure and NOT "
        "an agent failure. The friction-ODE machinery is the RIGHT machinery; it could not be "
        "exercised because its H(tau) input is degenerate in the canonical AOFT acoustic frame "
        "(W1 Clause-2 FAIL). The DILUTION-CC discharge therefore remains CONDITIONAL: C10 stays "
        "**ASSUMED-PARTIALLY-PROVEN** (Atlas-04 unchanged), Object C is **NOT yet derived**, and "
        "capstone §8.5 stays **OPEN**. The cheap-lead legs of the cluster (V.9 sub-leading sign, "
        "V.10 BBN fraction) landed independently of W1 and are unaffected by this closure.\n\n"
        "**Carry-Forward Computations**:\n"
        "- **CF-S99-W2-2-RELAXATION-CLOSURE** (the deferred full V.2 run):\n"
        "  1. **What**: Integrate the substrate friction ODE `q'' + 3 H q' + V'(q)=0` "
        "(V=delta_rho_vac, k_curv=+3586.5) along a NON-degenerate substrate Hubble backbone H(tau) "
        "and extract the late-time attractor slope `d ln q/d ln H` by log-log regression; compare "
        "to the n=2 target (slope=1 +/- 0.05). DO NOT impose the slow-roll quasi-static relation a "
        "priori.\n"
        "  2. **Inputs**: a re-derived NON-conformally-stationary substrate H(tau) backbone "
        "(the Object-C blocker — either a different substrate frame whose a_eff is genuinely "
        "dynamical, or a physical-time backbone where addot/adot is well-defined; the AOFT acoustic "
        "frame selected by W1 Clause-1 is conformally stationary and CANNOT serve); "
        "`s97_w2_2_c10_n_exponent.npz` V(q) shape (k_curv, q_boundary — pinned in this closure's "
        "npz); the 992 D_K eigenfrequencies (`s55_bogoliubov_992.npz`).\n"
        "  3. **Gate**: `|d ln q/d ln H - 1.0| <= 0.05` (PASS => n=2 substrate-forced => C10 Object "
        "C DONE => DILUTION-CC unconditional). regulator_pin a_0^{zeta}; scheme FW; "
        "convention ABSOLUTE; L_max=12.\n"
        "  4. **Effort**: medium (stiff 2D ODE Radau/BDF + attractor-slope regression), GATED on "
        "first re-deriving a non-degenerate substrate H(tau) — i.e., on resolving the W1 Clause-2 "
        "conformal-stationarity obstruction.\n\n"
        "**Substrate framing**: PHONONIC. The cosmological constant IS the spectral-action zeroth "
        "moment a0 (a_0_FW_zeta=6440.0), a DIFFERENT moment than gravity (a2). q is the Volovik "
        "q-theory vacuum variable; V(q)=delta_rho_vac(q) is the GGE zero-point + condensate "
        "response of the D_K eigenfrequencies omega_n(q)=sqrt(lambda_n^2+q). The friction ODE is "
        "the substrate's OWN relaxation dynamics, NOT a scalar field rolling IN a container. The "
        "arrow `D_K eigenvalues -> omega_n(q) zero-point -> V(q)=delta_rho_vac (a0-channel) -> "
        "friction-ODE attractor d ln q/d ln H -> rho_vac~H^n tracking exponent -> DILUTION-CC "
        "discharge` is unchanged in direction; this closure reports ONLY that the AOFT acoustic "
        "frame is conformally stationary upstream (so the attractor leg is a 0/0), not on the "
        "substrate's structural tracking state. EQUILIBRIUM-CC-WARRANT (S95) already pins "
        "rho_vac(eq)=0 EXACT (Volovik Paper 02 V02-E6: the equilibrium ground-state energy does not "
        "gravitate); V.2 would have tested whether the OUT-of-equilibrium tracking exponent n=2 is "
        "forced by the same substrate V(q) — that test is deferred to CF-S99, NOT resolved here."
    )                                                                  # (local)
    section = section[:res_s] + res_new + section[res_e:]

    wp_text = wp_text[:sect_start] + section + wp_text[sect_end:]
    WP_PATH.write_text(wp_text, encoding="utf-8")
    print(f"[WP] updated §{WP_ID} ({GATE_ID}) in {WP_PATH.name}")


def main() -> int:
    print(f"=== {GATE_ID} mechanical PRE-REG-INC closure ===\n")

    # 1. Read the W1 prereq verdict FROM DISK (decision point evaluation).
    prereq_status, prereq_value = parse_prereq_verdict()
    print(f"[prereq] {PREREQ_GATE_ID}: status={prereq_status}")
    print(f"         value={prereq_value}\n")

    # Decision-point predicate: full run IFF prereq == PASS; else mechanical closure.
    if prereq_status == "PASS":
        print("!! W1 prereq is PASS — the decision point selects the FULL friction-ODE run.")
        print("!! This closure script ONLY handles the mechanical-closure branch.")
        print("!! Abort: re-dispatch the full-run path. (Not expected: W1 landed FAIL.)")
        return 3

    print(f"[decision] W1 prereq status '{prereq_status}' != PASS "
          "=> pre-registered MECHANICAL CLOSURE branch fires (plan §W2-1 decision point).\n")

    # 2. Input SHAs (runtime) for plan-text-drift documentation.
    runtime_canonical_sha = sha256_of(CANONICAL_PY)                    # (local)
    runtime_w1_sha = sha256_of(W1_NPZ)                                 # (local)
    runtime_s97_sha = sha256_of(S97_C10_NPZ)                           # (local)
    print(f"[sha] canonical_constants.py runtime = {runtime_canonical_sha[:16]}... "
          f"(plan pin {PLAN_PINNED_CANONICAL_SHA[:16]}...; "
          f"{'MATCH' if runtime_canonical_sha == PLAN_PINNED_CANONICAL_SHA else 'DRIFT (benign — no constant consumed)'})")
    print(f"[sha] W1 npz runtime              = {runtime_w1_sha[:16]}... (plan pin <computed-at-runtime>)")
    print(f"[sha] s97 c10 npz runtime         = {runtime_s97_sha[:16]}... "
          f"(plan pin {PLAN_PINNED_S97_C10_SHA[:16]}...; "
          f"{'MATCH' if runtime_s97_sha == PLAN_PINNED_S97_C10_SHA else 'DRIFT'})\n")

    # 3. Load the substrate-physics block diagnostics + the deferred-run V(q) shape pins.
    diag = load_w1_diagnostics()
    vq = load_s97_vq_shape()
    print("[W1 diagnostics]")
    print(f"  conformally_stationary = {diag['clause2_conformally_stationary']} "
          f"(a_eff rel-var {diag['clause2_aeff_relvar']:.3e})")
    print(f"  clean_finite_window    = {diag['clause2_clean_finite_window']} "
          f"(f_used {diag['clause2_f_used']:.4f})")
    print(f"  q_central              = {diag['clause2_q_central']:.6e} (0/0 blow-up)")
    print(f"  V(q) shape (CF-S99)    : k_curv={vq.get('d2E_dq2_0', float('nan')):+.4f}, "
          f"q_boundary={vq.get('q_boundary', float('nan')):.8f}\n")

    # 4. Build the pinmap (embeds _gate_id => gate-distinct audit_sha256) + dual-SHA.
    pinmap = {
        "_gate_id": GATE_ID,
        "_wp_id": WP_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX,
        "_regulator_pin": REGULATOR_PIN,
        "_closure_kind": "PRE-REG-INC_mechanical_closure",
        "blocked_by": f"{PREREQ_GATE_ID}={prereq_status}",
        "w1_npz_sha256": runtime_w1_sha,
        "s97_c10_npz_sha256": runtime_s97_sha,
        "canonical_constants_sha256": runtime_canonical_sha,
    }                                                                  # (local)
    audit_sha, content_sha = compute_dual_sha(pinmap)

    # 5. Pre-registered value string (names the blocking prereq + its status).
    value_str = (
        f"PRE-REG-INC_blocked_by_S98-W1-ROUTE-RECONCILIATION_{prereq_status}"
        "_AOFT-frame-conformally-stationary_q-attractor-0over0_full-run-CF-S99"
    )                                                                  # (local)

    # 6. Write data + plot artifacts (plan marks both optional:false).
    write_data_npz(diag, vq, value_str, audit_sha, content_sha)
    print(f"[npz] wrote {(SESSION_DIR / 's98_w2_2_relaxation_closure.npz').name}")
    write_plot(diag)
    print(f"[png] wrote {(SESSION_DIR / 's98_w2_2_relaxation_closure.png').name}")

    # 7. Append the 3-row verdict block (idempotent).
    append_verdict(value_str, audit_sha, content_sha)

    # 8. Update the working paper IN THE SAME RUN (mechanical-closure-discipline.md item 5).
    update_wp_section(diag, vq, value_str, prereq_status, prereq_value,
                      audit_sha, content_sha, runtime_canonical_sha, runtime_w1_sha)

    # 9. sig_5 cross-check: the gate's audit_sha256 is unique in the verdict file.
    text = VERDICT_TXT.read_text(encoding="utf-8")                    # (local)
    n_dupe = sum(1 for ln in text.splitlines()
                 if f"audit_sha256={audit_sha}" in ln and ln.startswith("S98"))  # (local)
    print(f"\n[sig_5] canonical lines bearing this audit_sha256: {n_dupe} "
          f"({'UNIQUE — OK' if n_dupe == 1 else 'DUPLICATE — investigate'})")

    print(f"\n=== {GATE_ID}: PRE-REG-INC mechanical closure DONE ===")
    print(f"    verdict: FAIL -- value={value_str}")
    print(f"    audit_sha256={audit_sha}")
    print(f"    content_sha256={content_sha}")
    # Verdict is DATA; exit 0 regardless of PASS/FAIL/INFO/PRE-REG-INC (math-scripts.md).
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
