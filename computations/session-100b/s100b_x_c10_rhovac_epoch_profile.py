#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S100b-X-C10-RHOVAC-EPOCH-PROFILE — rho_vac epoch profile (C10 dark-energy arm).

DPP ROUTE (R2) CONDITIONAL-SKIP-as-INFO closure script.

Plan: sessions/session-plan/session-100b-plan-w1.md §W1-2 (CONDITIONAL /
trigger-first block, pre-registered at plan-freeze; item-1-clean per
mechanical-closure-discipline.md §"When mechanical closure IS acceptable").

Trigger predicate (pre-registered): the gate FIRES (R3) iff
S100a-W1-2-QEQ-DRIVE in {PASS, INFO-with-non-tracking-trajectory}.
On-disk state: S100a-W1-2-QEQ-DRIVE = FAIL (no slope-1-capable substrate
drive; the tracking law q_eq = c*H stays an IMPOSED closure) ->
route (R2): verdict INFO with the pre-registered value string
  CONDITIONAL-SKIP_qeq_drive_FAIL_tracking_law_stays_imposed_radiation-like_reading_stands
npz/png WAIVED per plan output_artifacts (optional: true under R1/R2).
Mode-A / mode-B compute is (R3)-only and is NOT run here.

This script:
  1. verifies the trigger predicate from the S100a verdict file (latest
     non-superseded canonical line per gate-verdicts.md Option-A reading);
  2. records W1-1's outcome (interpretation dependency only) + the
     "# constraint_scope(W1-2):" companion row;
  3. recomputes the STANDING exceedance record from canonical pins
     (NUMBERS only — nothing re-adjudicated; the record is S98-canonical);
  4. computes the dual SHA (audit = closure over script + canonical_constants
     + ordered pin map; content = script bytes);
  5. updates WP §W1-2 IN THE SAME RUN (mechanical-closure-discipline item 5;
     single-shot build -> atomic write -> re-read verify);
  6. PRINTS the verdict payload for the dispatching agent to pass to the
     race-safe knowledge-MCP `emit_verdict` tool (the script never writes
     the verdict file itself — gate-verdicts.md §"Race-Safe Emission").

[SIGN] trigger, schema_v2_3tuple_required on ALL outcomes:
  sign_verdict=N/A (gate did not fire; per plan R1/R2 prescription),
  magnitude_verdict=INFO, regime_verdict=VALID.
Composite collapse (pre-registered, gate-verdicts.md): regime VALID and
sign != FAIL and magnitude INFO  =>  composite INFO.  Closure emits a
non-PASS verdict (INFO is the pre-registered R2 shape; never PASS).

Verdict semantics: exit 0 = script ran and produced a valid verdict
(INFO included); exit != 0 = script breakage only.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 per machinery pin
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import re
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "computations" / "_shared"))

from canonical_constants import (  # noqa: E402
    T_BBN_GeV,                              # 1e-3 GeV   (BBN epoch pin)
    z_BBN,                                  # 4e8        (BBN redshift pin)
    N_eff_SM,                               # 3.044
    a_0_FW_zeta,                            # 6440.0  (zeta-regulated a_0^{zeta}; regulator pin)
    rho_vac_over_rho_rad_BBN_below,         # 0.474049 (S98-MK3-2 standing record)
    delta_N_eff_vacuum_BBN_below,           # 2.0873   (S98-MK3-2 standing record)
    delta_N_eff_budget_GoldsteinHill_2026,  # 0.107    (EXTERNAL budget; landed S100b W1-1)
)

# ---------------------------------------------------------------------------
# Identity (gate-identity keys -> per-gate-distinct audit SHA;
# mechanical-closure-discipline.md item 3)
# ---------------------------------------------------------------------------
SESSION = "100b"            # letter-suffixed sub-session; emit_verdict resolves the path
GATE_ID = "S100b-X-C10-RHOVAC-EPOCH-PROFILE"
WP_ID = "W1-2"
SCHEME = "FW"
CONVENTION = "ABSOLUTE"     # plan: mode tag MODE-A|MODE-B is (R3)-only; none under R2
L_MAX = "N/A"
DPP_ROUTE = "R2-CONDITIONAL-SKIP-as-INFO"
VALUE_STRING = ("CONDITIONAL-SKIP_qeq_drive_FAIL_tracking_law_stays_imposed_"
                "radiation-like_reading_stands")   # pre-registered VERBATIM (plan R2)

TRIGGER_GATE = "S100a-W1-2-QEQ-DRIVE"
W11_GATE = "S100b-X-C10-BBN-CONSTRAINT-RECONCILE"

# ---------------------------------------------------------------------------
# Input files (plan §W1-2 input_files; static pins verified EXACT)
# ---------------------------------------------------------------------------
F_CANON = REPO / "computations" / "_shared" / "canonical_constants.py"
F_S100A_VERDICTS = REPO / "computations" / "session-100a" / "s100a_gate_verdicts.txt"
F_S100A_QEQ_NPZ = REPO / "computations" / "session-100a" / "s100a_w1_qeq_drive.npz"
F_S99_RELAX = REPO / "computations" / "session-99" / "s99_w2_relaxation_closure.npz"
F_S99_NONRATIO = REPO / "computations" / "session-99" / "s99_w1_q_nonratio_observable.npz"
F_S98_MK32 = REPO / "computations" / "session-98" / "s98_mk3_2_bbn_vacuum_fraction.npz"
F_S100B_VERDICTS = REPO / "computations" / "session-100b" / "s100b_gate_verdicts.txt"
F_WP = REPO / "sessions" / "session-100b" / "session-100b-w1-workingpaper.md"

PLAN_PINS_STATIC = {
    "s99_relaxation_npz": "6d8d488a2fd726237c922f33883a7420e864ddb9fd52f0bf42bcebb5198ed42b",
    "s99_nonratio_npz": "1fdfe2eb34464461bab7c4dd6ea35a5100cb77e911745d1719055cc871ee71ec",
    "s98_mk3_2_npz": "c153d8d6f859a36d11a7bce0fd9e46e152c9989f7b12e0efc82b98f73d3bf8f7",
}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def fail(msg: str) -> None:
    print(f"SCRIPT-BREAKAGE: {msg}", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Verdict-file parsing (Option-A supersession-chain reading discipline)
# ---------------------------------------------------------------------------
CANON_RE = re.compile(
    r"^(?P<gate>[A-Za-z0-9._-]+):\s+(?P<verdict>PASS|FAIL|INFO|PRE-REG-INC)\s+--\s+"
    r"value='(?P<value>[^']*)'.*?audit_sha256=(?P<audit>[a-f0-9]{64})"
)


def latest_non_superseded(text: str, gate_id: str):
    """All canonical lines for gate_id; drop lines named in any supersedes= token;
    return the last surviving (line_text, match)."""
    lines = []  # (local)
    superseded = set()  # (local)
    for ln in text.splitlines():
        m = CANON_RE.match(ln)
        if m and m.group("gate") == gate_id:
            lines.append((ln, m))
        for sm in re.finditer(r"supersedes=([a-f0-9]{64})", ln):
            superseded.add(sm.group(1))
    survivors = [(ln, m) for (ln, m) in lines if m.group("audit") not in superseded]  # (local)
    return survivors[-1] if survivors else None


# ---------------------------------------------------------------------------
# Working-paper section text (R2 routing record; tokens filled at runtime)
# ---------------------------------------------------------------------------
WP_SECTION = """### §W1-2. S100b-X-C10-RHOVAC-EPOCH-PROFILE (volovik-superfluid-universe-theorist)

**Status**: COMPLETED (2026-06-07) — DPP route **(R2) CONDITIONAL-SKIP-as-INFO** (pre-registered closure; the gate did NOT fire; mode-A/mode-B compute is (R3)-only and was not run)
**Gate ID**: `S100b-X-C10-RHOVAC-EPOCH-PROFILE`
**Trigger**: `[SIGN]` (schema-v2 3-tuple emitted on this closure with `sign_verdict=N/A` per the plan's R1/R2 prescription)
**Classification**: **PHONONIC**
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: The radiation-era gravitating ρ_vac(a) implied by the S100a QEQ-DRIVE output departs from the tracking baseline (fraction ∝ a^{+0.0438}) in the relief direction — eps_BBN > +0.5 — and the epoch-resolved ΔN_eff clears ≤ 1 at both BBN and recombination, against the register's tracking-class FAIL prediction.
**Plan reference**: `sessions/session-plan/session-100b-plan-w1.md` §W1-2 (DPP routing R1/R2/R3, mode-A/mode-B machinery, ODE + k_curv npz pins, class separators, forward-pinned overlay M1′–M4′, substitution chain).

**Verdict**: **INFO** — pre-registered (R2) closure shape CONDITIONAL-SKIP-as-INFO (one of the three INFO shapes distinguished in the plan's `INFO_meaning`; the value string identifies it). 4-tuple: (value=`@@VALUE@@`, scheme=FW, convention=ABSOLUTE, L_max=N/A). Canonical line + dual-SHA companion + schema-v2 `[SIGN]` 3-tuple row (`sign_verdict=N/A`, `magnitude_verdict=INFO`, `regime_verdict=VALID`; composite collapse: regime VALID ∧ sign ≠ FAIL ∧ magnitude INFO ⇒ **INFO**) emitted via the race-safe `emit_verdict` tool: audit_sha256 `@@AUDIT@@`, content_sha256 `@@CONTENT@@`, schema_version S84+. npz/png **WAIVED** per the plan `output_artifacts` (`optional: true`, "WAIVED under R1 PRE-REG-INC and R2 CONDITIONAL-SKIP closures").

**MCP Pre-Compute Audit** (per plan `mcp_pre_compute_audit`, executed before the closure script was written):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("rhovac epoch profile radiation era")` | No prior epoch-profile gate exists; hits are the S99 litreview source (`session-99-litrev-x-c10-vacuum-profile-mack.md`, structural-baseline pin + the "Magnitude — epoch-dependent α_V" channel CLOSED) and the S97 ω_DM/ρ_vac pins (CC-66 observable, different gate) |
| `search_knowledge("QEQ-DRIVE q_eq substrate")` | Open channel "Upstream — substrate q_eq(H) drive" = "OPEN (the live successor)" (S99) — exactly the channel `S100a-W1-2-QEQ-DRIVE` closed as FAIL; no follow-up epoch profile computed |
| `get_constant("rho_vac_over_rho_rad_BBN_below")` | 0.474049 (S98, gate S98-MK3-2-BBN-VACUUM-FRACTION; standing FAIL-side falsifier value) — NOT re-adjudicated here |
| `get_constant("delta_N_eff_vacuum_BBN_below")` | 2.0873 (S98, same gate; companion pin) — NOT re-adjudicated here |
| `get_constant("T_BBN_GeV")` / `get_constant("z_BBN")` / `get_constant("N_eff_SM")` | 1e-3 GeV / 4e8 / 3.044 (epoch + SM pins; under R2 carried in the audit pin map only) |

No S100a follow-up computed the epoch profile — confirmed. W1-1's canonical verdict line exists and its outcome class is recorded for the interpretation clause below: **PASS**, outcome **@@W11_OUTCOME@@** (audit `@@W11_AUDIT16@@…`), with the `# constraint_scope(W1-2):` companion row present in `computations/session-100b/s100b_gate_verdicts.txt`.

**Output Artifacts**:

| Artifact | Path | Check |
|:---------|:-----|:------|
| script | `computations/session-100b/s100b_x_c10_rhovac_epoch_profile.py` | contains `from canonical_constants import` + `print_verdict_payload`; (R2) closure script — trigger-predicate verification, standing-record recompute from canonical pins, dual-SHA closure, WP §W1-2 update in the same run; cpu-cap-OMP8 |
| data (npz) | — | **WAIVED** under (R2) per plan `output_artifacts.data.optional: true` |
| plot (png) | — | **WAIVED** under (R2) per plan `output_artifacts.plot.optional: true` |
| verdict line | `computations/session-100b/s100b_gate_verdicts.txt` | canonical INFO line + dual-SHA companion + schema-v2 3-tuple row + companion rows (dpp_route / standing_record / regulator_pin / reopen_condition) via `emit_verdict` (lock-serialized, sig_5-unique) |
| WP section | this §W1-2 | updated IN THE SAME RUN as the closure (mechanical-closure-discipline item 5) |

Input pins: plan-static SHA-256 pins verified EXACT for `s99_w2_relaxation_closure.npz` (`6d8d488a…`), `s99_w1_q_nonratio_observable.npz` (`1fdfe2eb…`), `s98_mk3_2_bbn_vacuum_fraction.npz` (`c153d8d6…`) — all three are (R3)-machinery inputs, pinned-but-unexercised under (R2). Runtime SHAs captured for `canonical_constants.py` (`@@CANON16@@…`), `s100a_gate_verdicts.txt` (`@@S100AV16@@…`, the trigger source), and `s100a_w1_qeq_drive.npz` (`@@S100ANPZ16@@…`, the trigger-side artifact; its trajectory is NOT consumed under R2). Gate-identity keys + route tag + budget set + epoch pins + class separators enter the audit closure per the plan's `audit_discriminators`.

**Results**:

**(1) Numbers first — the trigger predicate (the (R2) routing record).** Pre-registered predicate: the gate FIRES iff `S100a-W1-2-QEQ-DRIVE` ∈ {PASS, INFO-with-non-tracking-trajectory}. The canonical line on disk (`computations/session-100a/s100a_gate_verdicts.txt`, latest non-superseded line for the gate-ID per the Option-A reading discipline):

> `S100a-W1-2-QEQ-DRIVE: FAIL` — value carries `slope_GDtilt_H2=2.055551`, `exp_locked_EVEN_in_H_kappa_inv=True`, `slope_imposed_cH=1.008273`, `domfrac=1.0000`, `kcurv=+3586.53`, `no_slope1_capable_substrate_drive`, `C10-ObjectC-STRUCTURALLY-CONDITIONAL` (audit `@@TRIG_AUDIT16@@…`; 3-tuple sign=PASS / magnitude=FAIL / regime=VALID; domain_used_frac=1.0000).

Verdict token = **FAIL** ⇒ trigger predicate FALSE ⇒ route **(R2) CONDITIONAL-SKIP-as-INFO** fires exactly as pre-registered at plan-freeze (no npz trajectory inspection required: the INFO-with-non-tracking-trajectory branch is reachable only from an INFO verdict). The S100a physics behind the routing: the substrate's own Gibbs-Duhem drive is exponent-LOCKED at q_eq = κ₂H² (slope d ln q/d ln H = 2.0556 on the bare backbone; κ₂-invariance 7.6e-8 — log-derivative slopes are coefficient-blind), the |H|-EVEN parity theorem forbids any equilibrium-sector potential term linear in H, and the slope-1 tracking leg reproduces q_eq = c·H only when IMPOSED (slope_imposed_cH = 1.008273). The tracking law therefore stays an IMPOSED closure — there is no substrate-derived ρ_vac(a) epoch profile for this gate to read off.

**(2) Verdict emission.** Pre-registered value string, VERBATIM: `@@VALUE@@`. Emitted INFO with the schema-v2 3-tuple (`sign_verdict=N/A` — the sign leg eps_BBN ≷ +0.5 was NOT evaluated because the gate did not fire; `magnitude_verdict=INFO` — the pre-registered closure shape; `regime_verdict=VALID` — the routing predicate evaluated unambiguously on an on-disk canonical line). Mode tag: none (MODE-A/MODE-B are (R3)-only).

**(3) The standing 2.0873 / 19.51× exceedance record — what it means under the radiation-like reading.** Recomputed in-script from the canonical pins (arithmetic only; NOTHING re-adjudicated — the record is S98-canonical and W1-1-scoped): fraction (ρ_vac/ρ_rad)_BBN = 0.474049; bound factor (7/8)(4/11)^{4/3} = @@BOUND@@ (exact in-script); ΔN_eff(BBN) = 2.0873 (consistency 0.474049/bound = @@DNEFF_CHECK@@, within the pin's Class-8.3 publication precision). Exceedances: **@@EXC_CANON@@×** the canonical ΔN_eff ≤ 1 budget; **@@EXC_GH@@×** the external Goldstein-Hill 2026 budget 0.107 (EXTERNAL, non-canonical); @@EXC_GEFF@@× the W1-1-derived tightest budget ΔN_eff ≤ @@DNEFF_GEFF@@ (G_eff-2% ⟺ f < 1/49 exact). Under (R2) this record is **UNCHANGED** — no new ΔN_eff was computed because no derived profile exists to compute it from. Its meaning is now jointly sharpened by the two upstream verdicts: (a) **W1-1 (PASS, @@W11_OUTCOME@@)** fixed the operative falsifier as the **z0-anchored lever** f = frac_base·exp((n_eff−2)·X) — the S66 from-above escape (n_eff = 2.3) is unavailable at ≥ 7.29 OOM present-day-CC cost, so the exceedance cannot be re-scoped away on the normalization-anchor axis; (b) **S100a QEQ-DRIVE (FAIL)** showed the linear tracking law q_eq = c·H is an IMPOSED closure, not a substrate derivation — the equilibrium sector is |H|-EVEN and cannot supply it. Jointly: the **radiation-like reading** (fraction ∝ a^{2(2−n_eff)} = a^{+@@EPS_BASE@@} at the pinned n_eff = @@NEFF@@, i.e. |eps_BBN| ≪ 0.5 by construction, near-flat across the radiation era) is the register's standing prediction, and ON THAT READING the C10/BBN arm is robustly falsified against the operative falsifier — at BBN the gravitating tracking vacuum overshoots every budget in the W1-1 scope statement (n_eff = 1.978111 exceeds all three crossings 1.959839 / 1.904348 / 1.900014). What (R2) does NOT do: it neither realizes nor excludes the time-profile relief corridor (eps_BBN > +0.5, EDE-class). That corridor was not measured — the substrate drive that would have produced a derived profile does not exist in the equilibrium sector. C10 Object-C therefore stays **STRUCTURALLY-CONDITIONAL** (the S100a tag): discharge of the BBN arm is strictly conditional on replacing the imposed tracking closure with a derived non-tracking profile, not on re-reading the standing record.

**(4) Dual-prior resolution (pre-registered).** `CONDITIONAL-SKIP (R2) → track_A ~0.85 by the trigger's own failure (tracking law stays imposed)` — the radiation-like register reading persists, with the elevated posterior reflecting that the one candidate substrate drive evaluated so far (Gibbs-Duhem equilibrium response) came back exponent-locked at H², i.e., the DRIVE route to a non-tracking profile is closed durably (H-parity theorem), leaving only the back-reaction route below.

**(5) Forward condition for re-opening (pre-registered re-fire routing).** This gate re-fires under **(R3)** — with the mode-B machinery pins UNCHANGED (friction ODE q″ + 3Hq′ + k_curv(q − q_eq(H)) = 0; k_curv = +3586.5 npz-loaded from `s99_w2_relaxation_closure.npz`; RK45 rtol 1e-8 / atol 1e-10; backbone `arr_H_bare_t` + emergent-FRW continuation; epochs z_BBN = 4e8 and z_rec = 1100; class separators ±0.5; regression check reproducing the independent S98-MK3-2 anchor 0.474049 within 1% under an imposed tracking closure) — iff a FUTURE substrate q_eq derivation lands a non-tracking q_eq(H) or self-consistent ρ_vac(H): a successor QEQ-class gate returning PASS, or INFO with a non-tracking trajectory in its npz. The structurally open route is NOT another equilibrium-potential drive (the |H|-EVEN parity theorem closes that class: T and s are |H|-odd ⇒ ∫s dT is |H|-even ⇒ no equilibrium thermodynamic potential carries a term linear in H): it is the Volovik-corpus-faithful **KV self-consistent back-reaction** (Papers 25 §V / 35 — q-oscillation energy dominating the Friedmann closure, amplitude ∝ a^{−3/2} ∝ H on the self-consistent background), which requires re-deriving H from the q-oscillation energy (the §6.3 closure) instead of pinning the H backbone. That compute is the CF candidate already logged in the S100a WP §W1-2 — no duplicate carry-forward is opened here.

**Substrate framing** (PHONONIC): the gravitating early vacuum IS the deviation of the a_0-channel q-variable from Gibbs-Duhem equilibrium (ρ_V = ε − q dε/dq; the equilibrium theorem is the wall, the deviation is the gravitating part; regulator pin a_0^{ζ} = 6440.0, cited via the standing record only — no fresh regulated moment is computed under R2). What this closure establishes substrate-first: the substrate's OWN equilibrium thermodynamics is |H|-even, so it cannot drive the linear-in-H tracking that the radiation-like reading presumes — that reading is a laboratory-IN transport-frame closure IMPOSED on the substrate, not derived from it; and on that imposed reading the BBN-epoch shadow (ΔN_eff = 2.0873) exceeds every budget in the W1-1 operative scope. The flow D_K eigenfrequencies (992-mode well, k_curv = +3586.5) → q-relaxation → gravitating ρ_vac(a) → laboratory-IN ΔN_eff shadows is intact, but its drive leg is open at the SELF-CONSISTENCY (back-reaction) node, not at the potential node. The fold transit (τ_fold = 0.190, Mach 13.75) completes ~18 OOM above T_BBN; whether the substrate holds the gravitating vacuum at the tracking worst-case at nucleosynthesis is now strictly a back-reaction question — substrate dynamics here are NOT c-limited (the q-relaxation is substrate-internal; c bounds only the emergent-metric propagation the BBN observables ride on).

**Carry-forward**: none new from this gate (the re-open compute — KV self-consistent back-reaction with H re-derived from q-oscillation energy — is the CF candidate already logged in the S100a WP §W1-2; this closure adds only the pre-registered (R3) re-fire routing, which is already plan text)."""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} — DPP route check + (R2) closure ===")

    # --- input SHAs (logged in the first ~20 stdout lines per gate-verdicts.md) ---
    for f in (F_CANON, F_S100A_VERDICTS, F_S100A_QEQ_NPZ, F_S99_RELAX,
              F_S99_NONRATIO, F_S98_MK32, F_S100B_VERDICTS):
        if not f.exists():
            fail(f"missing input file: {f}")
    sha_canon = sha256_file(F_CANON)            # (local)
    sha_s100a_v = sha256_file(F_S100A_VERDICTS)  # (local)
    sha_s100a_npz = sha256_file(F_S100A_QEQ_NPZ)  # (local)
    sha_s99_relax = sha256_file(F_S99_RELAX)    # (local)
    sha_s99_nonratio = sha256_file(F_S99_NONRATIO)  # (local)
    sha_s98 = sha256_file(F_S98_MK32)           # (local)
    print(f"sha256 canonical_constants.py          = {sha_canon}")
    print(f"sha256 s100a_gate_verdicts.txt         = {sha_s100a_v}")
    print(f"sha256 s100a_w1_qeq_drive.npz          = {sha_s100a_npz}")
    print(f"sha256 s99_w2_relaxation_closure.npz   = {sha_s99_relax}")
    print(f"sha256 s99_w1_q_nonratio_observable.npz= {sha_s99_nonratio}")
    print(f"sha256 s98_mk3_2_bbn_vacuum_fraction   = {sha_s98}")

    # --- plan-static pin verification (R3 machinery inputs; pinned-but-unexercised) ---
    if sha_s99_relax != PLAN_PINS_STATIC["s99_relaxation_npz"]:
        fail("s99_w2_relaxation_closure.npz SHA != plan pin")
    if sha_s99_nonratio != PLAN_PINS_STATIC["s99_nonratio_npz"]:
        fail("s99_w1_q_nonratio_observable.npz SHA != plan pin")
    if sha_s98 != PLAN_PINS_STATIC["s98_mk3_2_npz"]:
        fail("s98_mk3_2_bbn_vacuum_fraction.npz SHA != plan pin")
    print("plan-static SHA pins: all EXACT")

    # --- trigger predicate (R1/R2/R3 routing) ---
    s100a_text = F_S100A_VERDICTS.read_text(encoding="utf-8", errors="replace")  # (local)
    hit = latest_non_superseded(s100a_text, TRIGGER_GATE)  # (local)
    if hit is None:
        # would be route (R1) PRE-REG-INC — not the verified on-disk state; treat as breakage
        fail(f"no canonical line for {TRIGGER_GATE} (R1 state?) — orchestrator said R2")
    trig_line, trig_m = hit  # (local)
    trig_verdict = trig_m.group("verdict")   # (local)
    trig_value = trig_m.group("value")       # (local)
    trig_audit = trig_m.group("audit")       # (local)
    print(f"trigger line: {TRIGGER_GATE} verdict={trig_verdict} audit={trig_audit[:16]}…")
    fired = (trig_verdict == "PASS") or (trig_verdict == "INFO")  # (local) INFO would need npz non-tracking check
    if fired:
        fail(f"trigger predicate TRUE (verdict={trig_verdict}) — (R3) compute required; "
             "this closure script does not implement mode-A/mode-B. Re-dispatch the fired path.")
    if trig_verdict != "FAIL":
        fail(f"unexpected trigger verdict {trig_verdict}")
    # audit-trail item (ii): the closure value string's assertions match the upstream line
    if "no_slope1_capable_substrate_drive" not in trig_value:
        fail("upstream value lacks the no-slope-1 token the R2 value string asserts")
    if "slope_imposed_cH" not in trig_value:
        fail("upstream value lacks the imposed-closure token the R2 value string asserts")
    print("route selected: (R2) CONDITIONAL-SKIP-as-INFO  [QEQ-DRIVE=FAIL; tracking law stays imposed]")

    # --- W1-1 outcome (interpretation dependency only) + constraint-scope row ---
    s100b_text = F_S100B_VERDICTS.read_text(encoding="utf-8", errors="replace")  # (local)
    w11 = latest_non_superseded(s100b_text, W11_GATE)  # (local)
    if w11 is None:
        fail(f"W1-1 canonical line absent ({W11_GATE}) — wave-internal HARD order violated")
    w11_line, w11_m = w11  # (local)
    w11_verdict = w11_m.group("verdict")  # (local)
    w11_audit = w11_m.group("audit")      # (local)
    mo = re.search(r"outcome=([^;']+)", w11_m.group("value"))  # (local)
    w11_outcome = mo.group(1) if mo else "UNPARSED"  # (local)
    mn = re.search(r"n_eff_pin=([0-9.]+)", w11_m.group("value"))  # (local)
    if mn is None:
        fail("n_eff_pin not found in W1-1 value field")
    n_eff_pin = float(mn.group(1))  # (local) 1.978111
    scope_row_present = ("# constraint_scope(W1-2):" in s100b_text)  # (local)
    if not scope_row_present:
        fail("constraint_scope(W1-2) companion row absent from s100b verdict file")
    print(f"W1-1: verdict={w11_verdict} outcome={w11_outcome} n_eff_pin={n_eff_pin} "
          f"audit={w11_audit[:16]}… constraint_scope_row=PRESENT")

    # --- standing record (NUMBERS; recomputed from canonical pins, NOT re-adjudicated) ---
    bound_exact = (7.0 / 8.0) * (4.0 / 11.0) ** (4.0 / 3.0)        # (local) 0.22710732
    dneff_check = rho_vac_over_rho_rad_BBN_below / bound_exact     # (local) consistency image
    # Class-8.3: the 2.0873 pin publishes 5 sig figs -> verifier rel_tol >= 1e-4
    rel = abs(dneff_check - delta_N_eff_vacuum_BBN_below) / delta_N_eff_vacuum_BBN_below  # (local)
    if rel > 1e-4:
        fail(f"standing-record consistency broken: fraction/bound={dneff_check} vs pin "
             f"{delta_N_eff_vacuum_BBN_below} (rel={rel:.2e})")
    exc_canon = delta_N_eff_vacuum_BBN_below / 1.0                              # (local) 2.0873
    exc_gh = delta_N_eff_vacuum_BBN_below / delta_N_eff_budget_GoldsteinHill_2026  # (local) 19.51
    dneff_geff = (1.0 / 49.0) / bound_exact                                     # (local) 0.089861
    exc_geff = delta_N_eff_vacuum_BBN_below / dneff_geff                        # (local) 23.23
    eps_base = 2.0 * (2.0 - n_eff_pin)                                          # (local) +0.043778
    print(f"standing record: fraction={rho_vac_over_rho_rad_BBN_below}  "
          f"dNeff={delta_N_eff_vacuum_BBN_below}  bound={bound_exact:.8f}")
    print(f"exceedances: {exc_canon:.4f}x canonical<=1 | {exc_gh:.4f}x GH-2026 0.107 | "
          f"{exc_geff:.4f}x Geff-2pct {dneff_geff:.6f}")
    print(f"radiation-like baseline: eps_BBN = 2*(2-n_eff) = +{eps_base:.6f}  (|eps|<<0.5)")
    if abs(exc_gh - 19.51) > 0.01:
        fail(f"19.51x pre-registered record image not reproduced: {exc_gh:.4f}")

    # --- audit pin map (per plan audit_discriminators; gate-identity keys included) ---
    pins = {
        "_gate_id": GATE_ID, "_session": "S" + SESSION, "_wp_id": WP_ID,
        "_scheme": SCHEME, "_convention": CONVENTION,
        "_dpp_route": DPP_ROUTE,
        "_mode_tag": "N/A (MODE-A/MODE-B are R3-only; not run)",
        "trigger_gate": TRIGGER_GATE,
        "trigger_verdict": trig_verdict,
        "trigger_audit_sha256": trig_audit,
        "trigger_line_sha256": hashlib.sha256(trig_line.encode("utf-8")).hexdigest(),
        "s100a_verdicts_sha256": sha_s100a_v,
        "s100a_qeq_drive_npz_sha256": sha_s100a_npz,
        "w1_1_gate": W11_GATE,
        "w1_1_verdict": w11_verdict,
        "w1_1_outcome": w11_outcome,
        "w1_1_audit_sha256": w11_audit,
        "w1_1_line_sha256": hashlib.sha256(w11_line.encode("utf-8")).hexdigest(),
        "w1_1_constraint_scope_row": "PRESENT",
        "s99_relaxation_npz_sha256": sha_s99_relax,
        "s99_nonratio_npz_sha256": sha_s99_nonratio,
        "s98_mk3_2_npz_sha256": sha_s98,
        "canonical_constants_sha256": sha_canon,
        # (R3) machinery — plan-pinned, NOT exercised under R2:
        "r3_ode_form": "q''+3*H*q'+k_curv*(q-q_eq(H))=0; rho_vac=V(q) prop q^2",
        "r3_k_curv": "+3586.5 npz-loaded from s99_w2_relaxation_closure.npz (NOT exercised)",
        "r3_rk45": "rtol=1e-8 atol=1e-10 (NOT exercised)",
        "r3_backbone": "arr_H_bare_t + emergent-FRW continuation (NOT exercised)",
        "epoch_pins": f"z_BBN={z_BBN:.6g}; z_rec=1100; T_BBN_GeV={T_BBN_GeV:.6g}",
        "class_separator": "eps_BBN = +/-0.5",
        "budget_set": (f"dNeff<=1 canonical; <=0.107 GH-2026 EXTERNAL; "
                       f"<={dneff_geff:.6f} Geff-2pct EXTERNAL-derived"),
        "N_eff_SM": f"{N_eff_SM:.4g}",
        "regulator_pin": f"a_0^zeta (a_0_FW_zeta={a_0_FW_zeta:.6g}); standing record only",
        "record_fraction_BBN": f"{rho_vac_over_rho_rad_BBN_below:.6f}",
        "record_dNeff_BBN": f"{delta_N_eff_vacuum_BBN_below:.4f}",
        "record_exceed_canonical": f"{exc_canon:.4f}",
        "record_exceed_GH2026": f"{exc_gh:.4f}",
        "record_eps_BBN_baseline": f"+{eps_base:.6f} (radiation-like; n_eff={n_eff_pin})",
        "value_string": VALUE_STRING,
    }

    # --- dual SHA (template closure pattern: script + canonical_constants + pin map) ---
    script_bytes = Path(__file__).read_bytes()  # (local)
    pin_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                          sort_keys=True).encode("utf-8")  # (local)
    h = hashlib.sha256(); h.update(script_bytes); h.update(F_CANON.read_bytes()); h.update(pin_json)
    audit_sha = h.hexdigest()       # (local)
    content_sha = hashlib.sha256(script_bytes).hexdigest()  # (local)
    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")

    # --- WP §W1-2 update (single-shot: build -> atomic write -> re-read verify) ---
    section = (WP_SECTION
               .replace("@@VALUE@@", VALUE_STRING)
               .replace("@@AUDIT@@", audit_sha)
               .replace("@@CONTENT@@", content_sha)
               .replace("@@W11_OUTCOME@@", w11_outcome)
               .replace("@@W11_AUDIT16@@", w11_audit[:16])
               .replace("@@TRIG_AUDIT16@@", trig_audit[:16])
               .replace("@@CANON16@@", sha_canon[:16])
               .replace("@@S100AV16@@", sha_s100a_v[:16])
               .replace("@@S100ANPZ16@@", sha_s100a_npz[:16])
               .replace("@@BOUND@@", f"{bound_exact:.8f}")
               .replace("@@DNEFF_CHECK@@", f"{dneff_check:.5f}")
               .replace("@@EXC_CANON@@", f"{exc_canon:.4f}")
               .replace("@@EXC_GH@@", f"{exc_gh:.2f}")
               .replace("@@EXC_GEFF@@", f"{exc_geff:.2f}")
               .replace("@@DNEFF_GEFF@@", f"{dneff_geff:.6f}")
               .replace("@@EPS_BASE@@", f"{eps_base:.6f}")
               .replace("@@NEFF@@", f"{n_eff_pin:.6f}"))  # (local)
    if "@@" in section:
        fail("unfilled @@token@@ in WP section text")

    wp_text = F_WP.read_text(encoding="utf-8")  # (local)
    hdr = "### §W1-2. S100b-X-C10-RHOVAC-EPOCH-PROFILE"  # (local)
    i0 = wp_text.find(hdr)  # (local)
    i1 = wp_text.find("### §W1-3.", i0)  # (local)
    if i0 < 0 or i1 < 0:
        fail("WP §W1-2 / §W1-3 anchors not found")
    isep = wp_text.rfind("\n---\n", i0, i1)  # (local) separator before §W1-3
    if isep < 0:
        fail("WP separator before §W1-3 not found")
    new_wp = wp_text[:i0] + section + wp_text[isep:]  # (local)
    tmp = F_WP.with_suffix(".md.tmp_w12")  # (local)
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(new_wp)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, F_WP)

    verify = F_WP.read_text(encoding="utf-8")  # (local)
    must = [r"\*\*Status\*\*:.*COMPLETED",
            r"\*\*Verdict\*\*:.*(PASS|FAIL|INFO|PRE-REG-INC)",
            r"\*\*Output Artifacts\*\*",
            r"\*\*MCP Pre-Compute Audit\*\*"]  # (local)
    seg0 = verify.find(hdr); seg1 = verify.find("### §W1-3.", seg0)  # (local)
    seg = verify[seg0:seg1]  # (local)
    for pat in must:
        if not re.search(pat, seg):
            fail(f"WP §W1-2 must_contain pattern missing post-write: {pat}")
    for anchor in ("### §W1-1.", "### §W1-3.", "### §W1-4."):
        if anchor not in verify:
            fail(f"neighbor section lost in splice: {anchor}")
    if VALUE_STRING not in seg:
        fail("pre-registered value string missing from WP section")
    print("WP §W1-2 updated + verified (must_contain x4, neighbors intact, value string present)")

    # --- verdict payload (FINAL act; agent passes it to mcp emit_verdict) ---
    payload = print_verdict_payload(
        verdict="INFO",
        value=VALUE_STRING,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_verdict="N/A",
        magnitude_verdict="INFO",
        regime_verdict="VALID",
        companion_note=("R2 CONDITIONAL-SKIP closure: trigger S100a-W1-2-QEQ-DRIVE=FAIL "
                        f"(audit {trig_audit[:16]}); npz/png WAIVED per plan; mode-A/B not run"),
        extra_rows=[
            (f"# dpp_route=R2 CONDITIONAL-SKIP-as-INFO; trigger={TRIGGER_GATE} FAIL "
             f"(audit_short={trig_audit[:16]}, computations/session-100a/s100a_gate_verdicts.txt); "
             f"npz/png WAIVED per plan output_artifacts # {GATE_ID}"),
            (f"# standing_record: dNeff_BBN={delta_N_eff_vacuum_BBN_below} "
             f"({exc_canon:.4f}x canonical<=1; {exc_gh:.2f}x GH-2026 0.107; "
             f"{exc_geff:.2f}x Geff-2pct {dneff_geff:.6f}); fraction={rho_vac_over_rho_rad_BBN_below}; "
             f"eps_BBN_baseline=+{eps_base:.6f} radiation-like; W1-1 scope={w11_outcome} "
             f"(audit_short={w11_audit[:16]}) # {GATE_ID}"),
            (f"# regulator_pin=a_0^zeta (a_0_FW_zeta={a_0_FW_zeta:.6g}) R2-closure: rho_vac cited "
             f"via standing a_0-channel record only; no fresh regulated moment # {GATE_ID}"),
            (f"# reopen_condition: substrate-derived non-tracking q_eq(H) respecting H-parity "
             f"(equilibrium sector |H|-EVEN; KV self-consistent back-reaction route, Volovik "
             f"Papers 25 SecV / 35; H re-derived from q-oscillation energy); on landing re-fires "
             f"R3 with mode-B pins unchanged # {GATE_ID}"),
        ],
        three_tuple_note=("R2 closure: sign leg NOT evaluated (gate did not fire); "
                          "magnitude=INFO pre-registered closure shape; regime=VALID"),
    )
    print(f"[done in {time.time()-t0:.2f}s] composite=INFO route=R2 value={payload['value']}")
    return 0


# ---------------------------------------------------------------------------
# Verdict payload printer (script prints; the AGENT calls mcp emit_verdict —
# the script never writes the verdict file; gate-verdicts.md Race-Safe Emission)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None, three_tuple_note=""):
    payload = {
        "session": SESSION,            # "100b" (letter-suffixed; tool resolves the path)
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
    if three_tuple_note:
        payload["three_tuple_note"] = three_tuple_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


if __name__ == "__main__":
    sys.exit(main())
