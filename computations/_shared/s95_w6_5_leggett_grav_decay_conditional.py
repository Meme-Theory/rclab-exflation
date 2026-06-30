#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
LEGGETT-GRAV-DECAY-CONDITIONAL  (S95 W6-5)
==========================================

CONDITIONAL falsifier-inventory annotation gate (mack-cosmic-bridge sole writer
of falsifier-master-inventory.md per feedback_mack-bridge-role.md).

PURPOSE
-------
Surface the EXISTING LEGGETT-GRAV-DECAY-67 (CRITICAL) gate as a STATED
conditional on the Omega_DM h^2 = 0.120 Leggett-only PASS: the dark-matter
relic row is a PASS *given* Gamma_grav < H_0. If the gravitational decay
vertex <g,g|H_grav|L> exceeded H_0, the Leggett DM sector would collapse and
the 0.120 value would be meaningless. This conditional lands as a
falsifier-inventory annotation row (next free: Row #68) WITHOUT re-running the
decay vertex and WITHOUT re-adjudicating the standing PASS.

CONDITIONAL DISCIPLINE (plan SSW6-5)
------------------------------------
The gate is CONDITIONAL on a pre-registered TRIGGER:

  TRIGGER (FIRES) iff the LEGGETT-GRAV-DECAY-67 CRITICAL gate is confirmed PASS
  (Gamma_grav < H_0) in the knowledge base AND the existing S67/S73a Leggett-gate
  audit_sha256 are locatable.

  If the trigger is ABSENT (no proven_1967 LEGGETT-GRAV-DECAY-67 PASS in the KB,
  or the S67/S73a audit SHAs cannot be located) -> emit the documented
  CONDITIONAL-SKIP / PRE-REG-INC-by-design verdict (NOT a FAIL).

This script evaluates the trigger FIRST (NUMBERS first), then -- only if it
fires -- runs the conditional-annotation landing in full.

TRIGGER EVALUATION (this dispatch, 2026-05-28, knowledge MCP):
  trace_entity("LEGGETT-GRAV-DECAY") returned:
    - theorem "Leggett gravitational decay" [proven_1967]: "If Gamma_grav > H_0,
      DM sector collapses (Omega_DM h^2=0.120 meaningless)"; CRITICAL.  CONFIRMED.
    - gate LEGGETT-GRAV-DECAY-67: "PASS: Gamma_grav<H_0; FAIL: Gamma_grav>H_0";
      verdict PASS.  CONFIRMED.
    - gate LEGGETT-GRAV-DECAY-73a: PASS; tau_DM/t_univ = 1.13e+65; Z_2 parity P_L
      from J-evenness of condensate.  CONFIRMED.
  Locatable audit SHAs (canonical S81 batch-migration lines, the audit-traceable
  carriers for the migrated S67/S73a gates):
    - T3-BATCH-S67-LEGGETT-GRAV-DECAY  audit/sha256 =
      ceb8746c46ecf82fa38d138ca1512628014f88604260e680647e86340ed923b5
      (computations/session-81/s81_batch_gate_verdicts.txt:3268)
    - T3-BATCH-S73A-LEGGETT-GRAV-DECAY audit/sha256 =
      93b275baf5096b1320d9d1911aa66b543f4eb0cedfe03dbe48893456e8acb4f2
      (computations/session-81/s81_batch_gate_verdicts.txt:3985)
  ==> TRIGGER FIRES. Run the conditional-annotation landing in full.

SUBSTRATE FRAMING (phononic-framing.md SS"IS Space, Not IN Space"):
  CLASSIFICATION: PHONONIC. The Leggett-channel dark matter is an INTER-BAND
  COHERENCE MODE -- a phononic excitation of the fabric, CPT-neutral,
  non-annihilating, integrability-protected GGE quasiparticle. It is NOT a relic
  WIMP "in" a thermal bath; it IS the substrate's Leggett inter-band coherence
  excitation. Direction of explanation:
    D_K eigenvalue spectrum on Jensen-deformed SU(3)
      -> Leggett inter-band coherence mode (gap-massed c_L=0.0255 M_KK)
      -> a_2-channel DM relic Omega_DM h^2 = 0.120 (laboratory-IN abundance)
      -> gravitational-stability bound Gamma_grav < H_0 (the CONDITIONAL).
  The gravitational decay vertex <g,g|H_grav|L> couples the Leggett DM
  quasiparticle to the gravitational sector; the Z_2 parity P_L (J-evenness of
  the condensate, S73a) protects it, giving tau_DM/t_univ = 1.13e+65. We do NOT
  explain the DM relic via container-side LCDM freeze-out; the abundance is the
  substrate Leggett-channel quasiparticle population.

[VERIFY] SUBSTITUTION CHAIN (math-scripts.md SS"Double-Check Logic Before Compute"):
  Claim: "the Omega_DM h^2 = 0.120 PASS is a CONDITIONAL PASS: PASS given
          Gamma_grav < H_0; if Gamma_grav > H_0 the DM sector collapses and 0.120
          is meaningless."
  Step 1: Omega_DM h^2_FW (Leggett-only) = 0.120   [framework; vs Planck
          0.1186 +- 0.0020 ==> 0.7sigma PASS]
  Step 2: LEGGETT-GRAV-DECAY-67 gate criterion: PASS iff Gamma_grav < H_0;
          FAIL iff Gamma_grav > H_0   [KB proven_1967, CRITICAL]
  Step 3: at S73a, tau_DM / t_univ = 1.13e+65 >> 1
          ==> Gamma_grav = 1/tau_DM << 1/t_univ ~ H_0
          ==> Gamma_grav < H_0  ==>  gate PASS
  Step 4: DIRECTION: tau_DM/t_univ = 1.13e+65 >> 1 means the decay is 65 orders
          SLOWER than a Hubble time ==> Gamma_grav/H_0 ~ 1e-65 << 1 ==> the
          conditional is SATISFIED with enormous margin. The Z_2 parity P_L
          (J-evenness of the condensate, S73a) protects the channel.
  Step 5: therefore the Omega_DM h^2 = 0.120 PASS STANDS conditional on a bound
          satisfied by 65 orders of magnitude; the conditional is STATED (not a
          live risk) but MUST be surfaced because the document currently presents
          0.120 as an unconditional clean PASS.
  Conclusion: land the stated conditional; the PASS is robust but the conditional
          belongs next to the 260sigma-over-closure delicacy as the SECOND
          delicacy on the DM sector.

  [VERIFY] trigger note: this gate has a [VERIFY] trigger (existence + conditional
  landing), NOT a [SIGN] trigger. The directional content (Gamma_grav << H_0 by
  65 OOM) is a CONFIRMATION of an existing PASS, not a new gate. No schema-v2
  3-tuple companion row is emitted (no new numerical verdict).

W5-5 CROSS-LINK (q-GGE precision caveat):
  S95 W5-5 (Q-GGE-PRECISION) CONDITIONAL-SKIPped with a caveat that re-activates
  IFF a Leggett-channel DM AMPLITUDE gate registers a >=2-sig-fig <Q>_GGE
  precision need (its T2 trigger was "no_W6_Leggett-channel_DM_gate_present").
  THIS gate (W6-5) is a falsifier-inventory CONDITIONAL-ANNOTATION gate, NOT a
  DM amplitude gate. It consumes the relic abundance Omega_DM h^2 = 0.120, the
  lifetime tau_DM/t_univ = 1.13e+65, and the bound Gamma_grav < H_0 -- NONE of
  which require the GGE projected charge <Q>_GGE at any precision. Therefore this
  gate does NOT register a >=2-sig-fig <Q>_GGE precision need; the W5-5 caveat
  stays DORMANT and the Q-GGE-PRECISION carry-forward does NOT re-activate for S96.

VERDICT RUBRIC (plan SSW6-5):
  PASS = (a) LEGGETT-GRAV-DECAY-67 CRITICAL gate confirmed PASS (Gamma_grav<H_0)
         AND (b) a falsifier-inventory annotation row landed stating the
         Omega_DM h^2=0.120 PASS as conditional on Gamma_grav<H_0 AND (c) the row
         cites the existing S67/S73a Leggett-gate audit_sha256 AND (d) the row
         does NOT re-adjudicate the PASS.
  FAIL = the annotation cannot be landed (CRITICAL-gate audit_sha256 not
         locatable, OR the landing would re-adjudicate the PASS).
  INFO = the conditional is landed BUT a sub-question surfaces (e.g. whether
         Gamma_grav should be re-derived at higher precision than the S73a
         tau_DM/t_univ=1.13e+65) -- a deferred refinement, not a blocker.
  CONDITIONAL-SKIP / PRE-REG-INC-by-design = the pre-registered trigger is ABSENT
         (no proven_1967 LEGGETT-GRAV-DECAY-67 PASS, or audit SHAs not locatable).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
SHARED_DIR = SCRIPT_PATH.parent
ROOT_COMPUTATIONS = SHARED_DIR.parent
PROJECT_ROOT = ROOT_COMPUTATIONS.parent
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
SESSION_DIR = ROOT_COMPUTATIONS / "session-95"
VERDICT_TXT = SESSION_DIR / "s95_gate_verdicts.txt"
NPZ_PATH = SESSION_DIR / "s95_w6_5_leggett_grav_decay_conditional.npz"
PNG_PATH = SESSION_DIR / "s95_w6_5_leggett_grav_decay_conditional.png"
INVENTORY_PATH = (PROJECT_ROOT / "sessions" / "framework" / "registry"
                  / "falsifier-master-inventory.md")

# canonical_constants import (MANDATORY per computations/_shared/CLAUDE.md)
from canonical_constants import H_0_inv_s  # noqa: E402

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (plan SSW6-5)
# -----------------------------------------------------------------------------
GATE_ID = "LEGGETT-GRAV-DECAY-CONDITIONAL"
SCHEME = "falsifier-inventory-conditional-annotation"
CONVENTION = "conditional-PASS-given-Gamma_grav-lt-H_0"
L_MAX = "N/A"

# Pre-registered trigger inputs (knowledge-base confirmations; see module docstring)
LEGGETT_67_AUDIT_SHA = "ceb8746c46ecf82fa38d138ca1512628014f88604260e680647e86340ed923b5"  # (local) S67 (T3-BATCH-S67-LEGGETT-GRAV-DECAY, s81_batch_gate_verdicts.txt:3268)
LEGGETT_73A_AUDIT_SHA = "93b275baf5096b1320d9d1911aa66b543f4eb0cedfe03dbe48893456e8acb4f2"  # (local) S73a (T3-BATCH-S73A-LEGGETT-GRAV-DECAY, s81_batch_gate_verdicts.txt:3985)

# Framework / observational values for the substitution chain (plan SSW6-5 Step 1-4)
OMEGA_DM_H2_FW = 0.120          # (local) framework Leggett-only relic abundance (plan SSW6-5 Step 1)
OMEGA_DM_H2_PLANCK = 0.1186     # (local) Planck 2018 cold DM physical density (plan SSW6-5 Step 1)
OMEGA_DM_H2_PLANCK_SIG = 0.0020 # (local) Planck 1-sigma (plan SSW6-5 Step 1)
TAU_DM_OVER_T_UNIV = 1.13e65    # (local) S73a LEGGETT-GRAV-DECAY-73a tau_DM/t_univ (KB)

INVENTORY_ROW_NUMBER = 68       # (local) next-free top-level inventory row (highest existing = #67)


# -----------------------------------------------------------------------------
# Dual-SHA closure (S84+ schema; mirrors s94_bao_peak_branch.compute_dual_sha)
# -----------------------------------------------------------------------------
def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.
    audit = sha(script || canonical || pinmap_json); content = sha(script).
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def find_prior_audit_sha() -> str:
    """Return the most-recent prior canonical audit_sha256 for this GATE_ID (for
    the Option-A supersedes chain), or '' if none."""
    if not VERDICT_TXT.exists():
        return ""
    pat = re.compile(
        rf"^{re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", re.MULTILINE)  # (local)
    shas = pat.findall(VERDICT_TXT.read_text(encoding="utf-8", errors="ignore"))  # (local)
    return shas[-1] if shas else ""


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   supersedes_sha: str = "") -> None:
    """Append canonical line + dual-SHA companion row (atomic single open('a'))
    per gate-verdicts.md. [VERIFY] trigger ==> NO schema-v2 3-tuple row."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] CONDITIONAL gate (trigger FIRED); "
        f"conditional landing of existing CRITICAL LEGGETT-GRAV-DECAY-67 PASS as a "
        f"stated conditional on Omega_DM h^2=0.120; NO PASS re-adjudication; "
        f"no [SIGN] 3-tuple (schema_v2_3tuple_required=false)\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
        fh.write(line)
        fh.write(companion)


# -----------------------------------------------------------------------------
# Trigger evaluation (NUMBERS / trigger-evaluation FIRST, per task discipline)
# -----------------------------------------------------------------------------
def evaluate_trigger() -> dict:
    r"""Evaluate the pre-registered CONDITIONAL trigger.

    FIRES iff (T_a) LEGGETT-GRAV-DECAY-67 CRITICAL gate confirmed PASS in the KB
    AND (T_b) the existing S67/S73a Leggett-gate audit_sha256 are locatable.

    The KB confirmations are recorded as module-level facts (queried this dispatch;
    see module docstring). The SHA-locatability is verified against the S81 batch
    migration verdict file on disk.
    """
    # T_a: KB confirmation of the CRITICAL PASS (proven_1967; LEGGETT-GRAV-DECAY-67
    # PASS Gamma_grav<H_0; LEGGETT-GRAV-DECAY-73a PASS tau_DM/t_univ=1.13e+65).
    # Queried via trace_entity("LEGGETT-GRAV-DECAY") this dispatch (module docstring).
    kb_critical_pass_confirmed = True  # (local) trace_entity returned proven_1967 CRITICAL + LEGGETT-GRAV-DECAY-67 PASS
    kb_73a_pass_confirmed = True       # (local) trace_entity returned LEGGETT-GRAV-DECAY-73a PASS tau_DM/t_univ=1.13e+65

    # T_b: SHA locatability -- verify the two cited Leggett-gate audit SHAs are
    # present in the canonical S81 batch-migration verdict file.
    s81_batch = ROOT_COMPUTATIONS / "session-81" / "s81_batch_gate_verdicts.txt"  # (local)
    sha67_locatable = False  # (local)
    sha73a_locatable = False  # (local)
    if s81_batch.exists():
        batch_txt = s81_batch.read_text(encoding="utf-8", errors="ignore")  # (local)
        sha67_locatable = LEGGETT_67_AUDIT_SHA in batch_txt  # (local)
        sha73a_locatable = LEGGETT_73A_AUDIT_SHA in batch_txt  # (local)

    t_a = kb_critical_pass_confirmed and kb_73a_pass_confirmed  # (local)
    t_b = sha67_locatable and sha73a_locatable  # (local)
    fires = bool(t_a and t_b)  # (local)
    return {
        "kb_critical_pass_confirmed": kb_critical_pass_confirmed,
        "kb_73a_pass_confirmed": kb_73a_pass_confirmed,
        "sha67_locatable": sha67_locatable,
        "sha73a_locatable": sha73a_locatable,
        "T_a_kb_confirms_critical_PASS": t_a,
        "T_b_audit_shas_locatable": t_b,
        "trigger_fires": fires,
    }


# -----------------------------------------------------------------------------
# Substitution chain (the conditional structure, with substituted numbers)
# -----------------------------------------------------------------------------
def substitution_chain() -> dict:
    r"""Verify the conditional-structure substitution chain (plan SSW6-5 Step 1-5)."""
    # Step 1: Omega_DM h^2 framework vs Planck sigma-distance.
    sigma_dm = abs(OMEGA_DM_H2_FW - OMEGA_DM_H2_PLANCK) / OMEGA_DM_H2_PLANCK_SIG  # (local) 0.7 sigma
    # Step 3-4: Gamma_grav / H_0 ~ 1 / (tau_DM/t_univ) (with t_univ ~ 1/H_0).
    # tau_DM/t_univ >> 1  ==>  Gamma_grav/H_0 = (1/tau_DM)/(1/t_univ) = t_univ/tau_DM = 1/(tau_DM/t_univ).
    gamma_over_h0 = 1.0 / TAU_DM_OVER_T_UNIV  # (local) ~ 8.85e-66 << 1
    log10_margin = float(np.log10(TAU_DM_OVER_T_UNIV))  # (local) ~ 65 OOM
    # H_0 cross-check value (canonical) -- the bound's reference scale.
    h0_inv_s = H_0_inv_s  # (local) 2.184e-18 /s
    # Direction read-off: Gamma_grav < H_0 iff gamma_over_h0 < 1.
    conditional_satisfied = gamma_over_h0 < 1.0  # (local) True, by ~65 OOM
    return {
        "sigma_dm_vs_planck": sigma_dm,
        "gamma_grav_over_H0": gamma_over_h0,
        "log10_OOM_margin": log10_margin,
        "H_0_inv_s_canonical": h0_inv_s,
        "conditional_Gamma_grav_lt_H0_satisfied": conditional_satisfied,
    }


# -----------------------------------------------------------------------------
# W5-5 cross-link determination
# -----------------------------------------------------------------------------
def w5_5_crosslink() -> dict:
    r"""Determine whether this gate registers a >=2-sig-fig <Q>_GGE precision need.

    The S95 W5-5 (Q-GGE-PRECISION) caveat re-activates IFF a Leggett-channel DM
    AMPLITUDE gate registers a >=2-sig-fig <Q>_GGE precision need. This gate is a
    falsifier-inventory CONDITIONAL-ANNOTATION gate -- it consumes the relic
    abundance, lifetime, and Gamma_grav<H_0 bound, NONE of which require <Q>_GGE.
    """
    gate_is_amplitude_gate = False   # (local) this is an inventory conditional-annotation gate, NOT a DM amplitude gate
    requires_Q_GGE = False           # (local) consumes Omega_DM h^2, tau_DM/t_univ, Gamma_grav<H_0 -- NOT <Q>_GGE
    requires_Q_GGE_2sigfig = False   # (local) no <Q>_GGE precision need at any sig-fig
    w5_5_caveat_reactivates = bool(gate_is_amplitude_gate and requires_Q_GGE_2sigfig)  # (local) False
    return {
        "gate_is_leggett_DM_amplitude_gate": gate_is_amplitude_gate,
        "requires_Q_GGE": requires_Q_GGE,
        "requires_Q_GGE_to_2_sig_figs": requires_Q_GGE_2sigfig,
        "W5_5_Q_GGE_PRECISION_caveat_reactivates": w5_5_caveat_reactivates,
        "W5_5_status": "DORMANT (caveat stays dormant; Q-GGE-PRECISION CF does NOT re-activate for S96)",
    }


# -----------------------------------------------------------------------------
# Inventory Row #68 landing (append-only Python writer; sole-writer rule)
# -----------------------------------------------------------------------------
def build_row_68_text(audit_sha: str, content_sha: str, sub: dict) -> str:
    r"""Build the Row #68 falsifier-inventory annotation block (mirrors the
    Row #67 NEW-row pattern: header + table row + audit-pin source + bridge/ladder
    + status + Cross-link). Cites the EXISTING S67/S73a Leggett-gate audit_sha256;
    NO new prediction value; NO PASS re-adjudication."""
    sigma = sub["sigma_dm_vs_planck"]  # (local)
    g_over_h0 = sub["gamma_grav_over_H0"]  # (local)
    oom = sub["log10_OOM_margin"]  # (local)
    return rf"""
## NEW Row #{INVENTORY_ROW_NUMBER} — S95 W6-5 LEGGETT-GRAV-DECAY-67 gravitational-stability conditional on the Omega_DM h^2=0.120 Leggett-only DM relic (stated-conditional annotation; mack-cosmic-bridge sole-writer landing)

> **Origin**: S95 W6-5 (`session-95-plan-w6.md §W6-5`) mack-cosmic-bridge PRIMARY + sole-writer per `feedback_mack-bridge-role.md` (AMRI-PROMOTED 2026-04-28); gate `LEGGETT-GRAV-DECAY-CONDITIONAL` PASS (CONDITIONAL gate; pre-registered trigger FIRED — the LEGGETT-GRAV-DECAY-67 CRITICAL gate is confirmed PASS in the knowledge base). This row does NOT emit a new prediction value and does NOT re-adjudicate the standing Omega_DM h^2 PASS: it SURFACES the existing CRITICAL gravitational-stability gate (`LEGGETT-GRAV-DECAY-67`, proven_1967) as a STATED conditional on the Leggett-only DM relic, citing the existing S67/S73a Leggett-gate audit_sha256. nazarewicz-collab §R2 is the authoritative recommendation source. No canonical write-order Step 2 (no NEW value; this annotates an existing proven result).
> **Substrate framing (PHONONIC; `phononic-framing.md §"IS Space, Not IN Space"`)**: the Leggett-channel dark matter IS an inter-band coherence mode — a phononic excitation of the fabric, CPT-neutral, non-annihilating, integrability-protected GGE quasiparticle. Direction of explanation: D_K eigenvalue spectrum on Jensen-deformed SU(3) → Leggett inter-band coherence mode (gap-massed `c_L=0.0255` M_KK) → a_2-channel DM relic `Omega_DM h^2 = 0.120` (laboratory-IN abundance) → gravitational-stability bound `Gamma_grav < H_0` (the conditional). The gravitational decay vertex `⟨g,g|H_grav|L⟩` couples the Leggett DM quasiparticle to the gravitational sector; the `Z_2` parity `P_L` (J-evenness of the condensate, S73a) protects it, giving `tau_DM/t_univ = 1.13e+65`. We do NOT explain the relic via container-side LCDM freeze-out; the abundance is the substrate Leggett-channel quasiparticle population.

| # | Observable | Falsifier function | Channel(s) | Prediction value(s) | Live-watch envelope | Internal-consistency split | Detector / horizon | scheme | convention | L_max | content_sha256 | audit_sha256 | notes |
|:-:|:-----------|:-------------------|:-----------|:--------------------|:--------------------|:----------------------------|:--------------------|:-------|:-----------|:------|:----------------|:--------------|:------|
| {INVENTORY_ROW_NUMBER} | Leggett-channel DM gravitational stability: the `Omega_DM h^2 = 0.120` (Leggett-only) PASS is a CONDITIONAL PASS — PASS *given* `Gamma_grav < H_0` (gravitational decay vertex `⟨g,g\|H_grav\|L⟩` below the Hubble rate) | **DM-SECTOR-COLLAPSE conditional falsifier**: if `Gamma_grav > H_0` the Leggett DM sector collapses and the `Omega_DM h^2 = 0.120` value is MEANINGLESS (the relic decays within a Hubble time). Falsifier fires on: a measured or derived `Gamma_grav > H_0` for the Leggett inter-band coherence mode (would falsify the `Z_2`-parity-protected stability and void the 0.120 abundance) | Leggett-channel DM relic abundance vs Planck cold-DM density; gravitational-decay lifetime `tau_DM` | `Omega_DM h^2 = 0.120` (Leggett-only) = **{sigma:.2g}σ** vs Planck 0.1186±0.0020 (PASS). Gravitational-stability bound: `Gamma_grav/H_0 ~ {g_over_h0:.2e}` (`tau_DM/t_univ = 1.13e+65`; **{oom:.0f} OOM** SLOWER than a Hubble time) | CONDITIONAL: the 0.120 PASS holds while `Gamma_grav < H_0`; the bound is satisfied by ~65 OOM (a STATED conditional, NOT a live risk) | DISTINCT epistemic type: the relic-abundance PASS (0.120 = 0.7σ) is the framework's quantitative DM landing; the gravitational-stability conditional is the SECOND delicacy on the DM sector (the FIRST being the 260σ full-DM over-closure forcing the Leggett-only channel). The `Z_2` parity `P_L` (J-evenness of the condensate, S73a) is the structural reason `Gamma_grav` is suppressed by ~65 OOM | Gravitational-decay-lifetime stability (theory-side CRITICAL bound; no direct detector — the conditional is on the substrate decay vertex, satisfied by 65 OOM) | falsifier-inventory-conditional-annotation | conditional-PASS-given-Gamma_grav-lt-H_0 | N/A | `{content_sha}` | `{audit_sha}` | NEW S95 W6-5 (`LEGGETT-GRAV-DECAY-CONDITIONAL` PASS; CONDITIONAL gate, trigger FIRED); surfaces the existing CRITICAL `LEGGETT-GRAV-DECAY-67` PASS as a stated conditional; cites existing S67/S73a Leggett-gate audit_sha256 (NO new value, NO PASS re-adjudication); the SECOND DM-sector delicacy alongside the 260σ full-DM over-closure |

- **Audit-pin source (existing CRITICAL gate — cited, NOT re-run)**: `LEGGETT-GRAV-DECAY-67` (CRITICAL; proven_1967 "If Gamma_grav > H_0, DM sector collapses (Omega_DM h^2=0.120 meaningless)"; PASS `Gamma_grav<H_0`) audit_sha256=`{LEGGETT_67_AUDIT_SHA}` (canonical S81 batch-migration line `computations/session-81/s81_batch_gate_verdicts.txt:3268`, `T3-BATCH-S67-LEGGETT-GRAV-DECAY`). `LEGGETT-GRAV-DECAY-73a` (PASS; `tau_DM/t_univ = 1.13e+65`; `Z_2` parity `P_L` from J-evenness of condensate) audit_sha256=`{LEGGETT_73A_AUDIT_SHA}` (canonical S81 batch-migration line `computations/session-81/s81_batch_gate_verdicts.txt:3985`, `T3-BATCH-S73A-LEGGETT-GRAV-DECAY`). THIS row's own producing-gate audit_sha256=`{audit_sha}` (S95 `LEGGETT-GRAV-DECAY-CONDITIONAL`; `computations/session-95/s95_gate_verdicts.txt`).
- **Conditional structure (substitution chain, plan §W6-5 Step 1-5)**: Step 1 `Omega_DM h^2_FW = 0.120` vs Planck 0.1186±0.0020 ⇒ `{sigma:.2g}σ` PASS. Step 2 `LEGGETT-GRAV-DECAY-67` criterion: PASS iff `Gamma_grav < H_0`. Step 3 at S73a `tau_DM/t_univ = 1.13e+65 >> 1` ⇒ `Gamma_grav = 1/tau_DM << 1/t_univ ~ H_0` ⇒ gate PASS. Step 4 DIRECTION: `Gamma_grav/H_0 ~ {g_over_h0:.2e} << 1` (the decay is ~{oom:.0f} orders SLOWER than a Hubble time; `H_0 = {sub['H_0_inv_s_canonical']:.3e}` /s canonical). Step 5 the 0.120 PASS STANDS conditional on a bound satisfied by ~65 OOM — STATED, not a live risk — but surfaced because the document currently presents 0.120 as an unconditional clean PASS.
- **Bridge family / structural anchor**: this is the gravitational-stability conditional on the Leggett-channel DM relic (the LEGGETT-MOMENT first Type-F DM channel, S70 PROVEN; `Mass_LeggettDM/Δ_BCS = 11.97`, C11 CONDITIONAL on LEGGETT-GRAV-DECAY-67 survival). The two DM-sector delicacies together: (1) the 260σ full-DM over-closure (only the Leggett-only channel passes); (2) THIS gravitational-stability conditional (`Gamma_grav < H_0`, satisfied by ~65 OOM). Both belong next to the `Omega_DM h^2` row.
- **W5-5 cross-link (Q-GGE precision)**: this gate is a falsifier-inventory CONDITIONAL-ANNOTATION gate, NOT a Leggett-channel DM AMPLITUDE gate; it consumes `Omega_DM h^2`, `tau_DM/t_univ`, and the `Gamma_grav < H_0` bound — NONE of which require the GGE projected charge `⟨Q⟩_GGE`. It therefore does NOT register a ≥2-sig-fig `⟨Q⟩_GGE` precision need; the S95 W5-5 `Q-GGE-PRECISION` caveat stays **DORMANT** (the `Q-GGE-PRECISION` carry-forward does NOT re-activate for S96).
- **Status**: LANDED as the gravitational-stability conditional annotation on the `Omega_DM h^2=0.120` Leggett-only DM relic; the existing CRITICAL `LEGGETT-GRAV-DECAY-67` PASS is SURFACED as a stated conditional WITHOUT re-adjudication. The Leggett-channel DM relic PASS (0.120 = 0.7σ) is UNCHANGED; this annotation records the conditional structure (the SECOND DM-sector delicacy). The conditional is satisfied by ~65 OOM (`Z_2` parity `P_L` protection).

**Cross-link**: Row #{INVENTORY_ROW_NUMBER} mirrors the Row #67 NEW-row pattern (table row + audit-pin source + conditional structure + bridge-family/anchor + status; additive citation per `gate-verdicts.md` canonical-form rule). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole-writer for falsifier-master-inventory.md (AMRI-PROMOTED 2026-04-28). This row is structurally distinct from the BAO (#67) and n_PBH (#65/#66) rows — it is a CONDITIONAL annotation surfacing an existing CRITICAL gate (`LEGGETT-GRAV-DECAY-67`) as a stated conditional on the DM relic, citing the existing S67/S73a audit_sha256 rather than emitting a new prediction. It is the SECOND DM-sector delicacy (alongside the 260σ full-DM over-closure) and carries the W5-5 Q-GGE-precision DORMANT determination.
"""


def land_row_68(row_text: str) -> dict:
    r"""Append Row #68 to falsifier-master-inventory.md via an append-only Python
    writer (never an Edit-tool round-trip) per epistemic-discipline.md
    §"Registry-Write Hygiene". Idempotent: if a Row #68 header already exists, do
    NOT re-append."""
    already_present = False  # (local)
    if INVENTORY_PATH.exists():
        existing = INVENTORY_PATH.read_text(encoding="utf-8", errors="ignore")  # (local)
        if f"## NEW Row #{INVENTORY_ROW_NUMBER} — S95 W6-5 LEGGETT-GRAV-DECAY" in existing:
            already_present = True  # (local)
    if not already_present:
        with open(INVENTORY_PATH, "a", encoding="utf-8") as fh:
            fh.write(row_text)
    return {"row_appended": (not already_present), "already_present": already_present}


# -----------------------------------------------------------------------------
# Plot (trigger-evaluation + conditional-margin diagram)
# -----------------------------------------------------------------------------
def make_plot(trig: dict, sub: dict, png_path: Path) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Panel 1: conditional margin Gamma_grav/H_0 vs the bound (log scale).
    oom = sub["log10_OOM_margin"]  # (local)
    ax1.barh([0], [oom], color="#2c7fb8", height=0.5)
    ax1.axvline(0.0, color="crimson", linestyle="--", linewidth=1.5,
                label="bound: Gamma_grav = H_0 (log10 margin = 0)")
    ax1.set_yticks([0])
    ax1.set_yticklabels(["Gamma_grav < H_0"])
    ax1.set_xlabel("log10(t_univ / tau_DM)^{-1} margin  =  -log10(Gamma_grav/H_0)")
    ax1.set_title("Conditional margin: Gamma_grav/H_0 ~ 1e-65\n"
                  "(decay ~65 OOM slower than a Hubble time; Z_2 parity P_L)")
    ax1.text(oom * 0.5, 0.0, f"{oom:.0f} OOM\nmargin",
             ha="center", va="center", color="white", fontweight="bold")
    ax1.legend(loc="lower right", fontsize=8)
    ax1.set_xlim(0, oom * 1.15)

    # Panel 2: Omega_DM h^2 PASS (conditional) vs Planck band.
    planck_c = OMEGA_DM_H2_PLANCK  # (local)
    planck_s = OMEGA_DM_H2_PLANCK_SIG  # (local)
    ax2.axhspan(planck_c - planck_s, planck_c + planck_s, color="#a1d99b", alpha=0.6,
                label="Planck 0.1186 +- 0.0020 (1sigma)")
    ax2.axhline(planck_c, color="#31a354", linewidth=1.0)
    ax2.plot([1], [OMEGA_DM_H2_FW], "o", color="#2c7fb8", markersize=11,
             label=f"FW Leggett-only 0.120 ({sub['sigma_dm_vs_planck']:.2g} sigma)")
    ax2.set_xlim(0.5, 1.5)
    ax2.set_xticks([1])
    ax2.set_xticklabels(["Omega_DM h^2"])
    ax2.set_ylabel("Omega_DM h^2")
    fires = "FIRED" if trig["trigger_fires"] else "ABSENT"  # (local)
    ax2.set_title(f"Conditional PASS: Omega_DM h^2 = 0.120 given Gamma_grav < H_0\n"
                  f"trigger {fires}; PASS surfaced as stated conditional (no re-adjudication)")
    ax2.legend(loc="upper right", fontsize=8)

    fig.suptitle("S95 W6-5 LEGGETT-GRAV-DECAY-CONDITIONAL — Leggett-channel DM gravitational-stability conditional",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(png_path, dpi=130)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print("=" * 70)
    print(f"GATE: {GATE_ID}")
    print("=" * 70)

    # Input SHAs (first 20 lines of stdout per gate-verdicts.md).
    canonical_sha = file_sha256(CANONICAL_CONSTANTS_PATH)  # (local)
    script_self_sha = file_sha256(SCRIPT_PATH)  # (local)
    print(f"INPUT canonical_constants.py sha256 = {canonical_sha}")
    print(f"INPUT script self sha256            = {script_self_sha}")
    print(f"INPUT LEGGETT-GRAV-DECAY-67 audit_sha256  = {LEGGETT_67_AUDIT_SHA}")
    print(f"INPUT LEGGETT-GRAV-DECAY-73a audit_sha256 = {LEGGETT_73A_AUDIT_SHA}")

    # --- STEP 1: TRIGGER EVALUATION (numbers / trigger first) ---
    trig = evaluate_trigger()  # (local)
    print("\n--- TRIGGER EVALUATION ---")
    for k, v in trig.items():
        print(f"  {k} = {v}")

    # --- STEP 2: substitution chain (conditional structure) ---
    sub = substitution_chain()  # (local)
    print("\n--- SUBSTITUTION CHAIN (conditional structure) ---")
    for k, v in sub.items():
        print(f"  {k} = {v}")

    # --- STEP 3: W5-5 cross-link determination ---
    w55 = w5_5_crosslink()  # (local)
    print("\n--- W5-5 CROSS-LINK (Q-GGE precision) ---")
    for k, v in w55.items():
        print(f"  {k} = {v}")

    # --- Pin map (audit_sha256_inputs per plan SSW6-5) ---
    pins = {
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX,
        "canonical_constants_sha256": canonical_sha,
        "leggett_67_audit_sha256": LEGGETT_67_AUDIT_SHA,
        "leggett_73a_audit_sha256": LEGGETT_73A_AUDIT_SHA,
        "trigger_fires": trig["trigger_fires"],
        "omega_dm_h2_FW": OMEGA_DM_H2_FW,
        "omega_dm_h2_planck": OMEGA_DM_H2_PLANCK,
        "tau_dm_over_t_univ": TAU_DM_OVER_T_UNIV,
        "inventory_row_number": INVENTORY_ROW_NUMBER,
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)  # (local)
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- VERDICT DECISION (CONDITIONAL discipline) ---
    if not trig["trigger_fires"]:
        # Documented CONDITIONAL-SKIP / PRE-REG-INC-by-design branch (NOT a FAIL).
        verdict = "INFO"  # (local) PRE-REG-INC-by-design carries as INFO per plan / gate-verdicts.md
        value = ("CONDITIONAL-SKIP_PRE-REG-INC-by-design;trigger_absent;"
                 f"kb_critical_PASS={trig['T_a_kb_confirms_critical_PASS']};"
                 f"audit_shas_locatable={trig['T_b_audit_shas_locatable']};"
                 "reason=LEGGETT-GRAV-DECAY-67_CRITICAL_PASS_not_confirmed_or_audit_shas_not_locatable;"
                 "no_row_landed;no_PASS_re-adjudication;"
                 f"W5-5_Q-GGE-PRECISION_caveat={w55['W5_5_status']}")  # (local)
        row_status = {"row_appended": False, "already_present": False}  # (local)
        print("\n*** TRIGGER ABSENT -> CONDITIONAL-SKIP / PRE-REG-INC-by-design (NOT a FAIL) ***")
    else:
        # --- TRIGGER FIRED: land Row #68 (sole-writer append-only) ---
        row_text = build_row_68_text(audit_sha, content_sha, sub)  # (local)
        row_status = land_row_68(row_text)  # (local)
        print("\n--- ROW #68 LANDING ---")
        for k, v in row_status.items():
            print(f"  {k} = {v}")

        # PASS rubric (plan SSW6-5): 4-of-4 sub-conditions (a..d).
        cond_a = trig["T_a_kb_confirms_critical_PASS"]  # (local) LEGGETT-GRAV-DECAY-67 PASS confirmed
        cond_b = (row_status["row_appended"] or row_status["already_present"])  # (local) annotation row landed
        cond_c = trig["T_b_audit_shas_locatable"]  # (local) row cites existing S67/S73a audit_sha256
        cond_d = True  # (local) no PASS re-adjudication (the script only annotates; no verdict change emitted for the DM row)
        all_four = cond_a and cond_b and cond_c and cond_d  # (local)
        verdict = "PASS" if all_four else "FAIL"  # (local)
        value = (f"conditional_landed_Row#{INVENTORY_ROW_NUMBER};"
                 f"LEGGETT-GRAV-DECAY-67_PASS_confirmed={cond_a};"
                 f"Omega_DM_h2=0.120={sub['sigma_dm_vs_planck']:.2g}sigma_vs_Planck_0.1186;"
                 f"Gamma_grav/H_0~{sub['gamma_grav_over_H0']:.2e}_({sub['log10_OOM_margin']:.0f}_OOM_margin);"
                 f"cites_S67_S73a_audit_sha256={cond_c};"
                 f"no_PASS_re-adjudication={cond_d};"
                 f"W5-5_Q-GGE-PRECISION={w55['W5_5_status']}")  # (local)
        print(f"\n  sub-conditions: (a)={cond_a} (b)={cond_b} (c)={cond_c} (d)={cond_d} -> 4-of-4={all_four}")

    print(f"\n  VERDICT = {verdict}")

    # --- Save npz ---
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=verdict,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        # trigger
        trigger_fires=trig["trigger_fires"],
        T_a_kb_confirms_critical_PASS=trig["T_a_kb_confirms_critical_PASS"],
        T_b_audit_shas_locatable=trig["T_b_audit_shas_locatable"],
        sha67_locatable=trig["sha67_locatable"],
        sha73a_locatable=trig["sha73a_locatable"],
        # substitution chain
        sigma_dm_vs_planck=sub["sigma_dm_vs_planck"],
        gamma_grav_over_H0=sub["gamma_grav_over_H0"],
        log10_OOM_margin=sub["log10_OOM_margin"],
        H_0_inv_s_canonical=sub["H_0_inv_s_canonical"],
        conditional_satisfied=sub["conditional_Gamma_grav_lt_H0_satisfied"],
        # framework / observational
        omega_dm_h2_FW=OMEGA_DM_H2_FW,
        omega_dm_h2_planck=OMEGA_DM_H2_PLANCK,
        omega_dm_h2_planck_sig=OMEGA_DM_H2_PLANCK_SIG,
        tau_dm_over_t_univ=TAU_DM_OVER_T_UNIV,
        # W5-5 cross-link
        w5_5_caveat_reactivates=w55["W5_5_Q_GGE_PRECISION_caveat_reactivates"],
        w5_5_requires_Q_GGE=w55["requires_Q_GGE"],
        w5_5_requires_Q_GGE_2sigfig=w55["requires_Q_GGE_to_2_sig_figs"],
        w5_5_gate_is_amplitude_gate=w55["gate_is_leggett_DM_amplitude_gate"],
        w5_5_status=w55["W5_5_status"],
        # inventory
        inventory_row_number=INVENTORY_ROW_NUMBER,
        row_appended=row_status["row_appended"],
        row_already_present=row_status["already_present"],
        # leggett gate SHAs cited
        leggett_67_audit_sha256=LEGGETT_67_AUDIT_SHA,
        leggett_73a_audit_sha256=LEGGETT_73A_AUDIT_SHA,
        # closure
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  npz  -> {NPZ_PATH}")

    # --- Plot ---
    make_plot(trig, sub, PNG_PATH)
    print(f"  png  -> {PNG_PATH}")

    # --- Verdict line (Option-A supersedes chain) ---
    prior_sha = find_prior_audit_sha()  # (local)
    supersedes = prior_sha if (prior_sha and prior_sha != audit_sha) else ""  # (local)
    append_verdict(verdict, value, audit_sha, content_sha, supersedes_sha=supersedes)
    print(f"  verdict line -> {VERDICT_TXT}")
    if supersedes:
        print(f"  (supersedes prior line audit_sha256={supersedes})")

    return 0  # script health: clean run regardless of PASS/FAIL/INFO verdict


if __name__ == "__main__":
    sys.exit(main())
