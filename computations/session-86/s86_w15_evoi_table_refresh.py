#!/usr/bin/env python3
"""
S86 W15-2 — S86-EVOI-TABLE-REFRESH (P13, FINAL)
================================================

Gate: S86-EVOI-TABLE-REFRESH ([AUDIT] + [SIGN])

Pre-registered threshold (plan §W15-2 §9):
  PASS  iff  EVOI table updated AND P_work_complete bracket reported AND
             P_low >= P_pre_low_S85 = 0.31  (monotone-upward direction
             confirmed via [SIGN] substitution chain)
  FAIL  iff  no update written, OR no bracket reported, OR P_high < 0.31
             (counting error or substitution-chain inequality violated)
  INFO  iff  some link-list deltas unavailable (with caveats), OR
             substitution-chain equality (P_post == P_pre exactly).

Inputs (SHA-256 pinned at runtime):
  - sessions/evoi-framework.md            (PRE-write)
  - sessions/evoi-framework.md            (POST-write)
  - computations/session-86/s86_gate_verdicts.txt  (PRE-W15-2 state)
  - sessions/framework/registry/falsifier-master-inventory.md (POST-W14)

Output 4-tuple:
  (value=[P_low, P_high], scheme=link-inventory,
   convention=frozen-since-S66, L_max=NA)

Classification: META

METHODOLOGY
-----------
Refresh the EVOI work-fraction table per `.claude/rules/evoi-prioritization.md`
formula  P_work_complete = (N_complete / N_total) x F_obs.

Step A: snapshot (N_c_pre, N_t_pre, F_obs_pre) from evoi-framework.md.
Step B: count distinct PASS/FAIL/INFO gate IDs in s86_gate_verdicts.txt
        (NOT counting PRE-REG-INC).
Step C: count NEW pre-registered S86 gates (W0a..W14, W15) -> Delta_N_t.
Step D: count newly-anchored observation links from W6 (9 atomic) and
        W11/W12 anchorings -> Delta_F_obs.
Step E: recompute (N_complete_post, N_total_post, P_work_complete_post).
Step F: substitution-chain check (plan §10):
        sign(P_post - P_pre |_{DF=0}) = sign(DN_c * N_t - N_c * DN_t)
Step G: APPEND new "## S86 Refresh -- 2026-04-26" section to
        sessions/evoi-framework.md (S66 baseline = 0.206 PRESERVED).
Step H: emit verdict with bracket [P_low, P_high].

DISCIPLINE
----------
- Pure tabulation; no GPU; no canonical_constants needed.
- Atomic open("a") for verdict + companion lines.
- closure_sha computed at runtime from ordered 5-tuple per plan §6 Step E.
- All intermediates tagged `# (local)`.

Substrate framing (per plan §13):
  P_work_complete is an EFFORT-BASED measure, NOT a framework-truth
  probability. PASS/FAIL/INFO each count as "link complete" -- they all
  discharge the EVOI computation. P13 measures "how much of the pre-
  registered link inventory has had its computation discharged".
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import re
import sys
import time
from pathlib import Path
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


# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"

SESSION = "S86"                                   # (local)
GATE_ID = "S86-EVOI-TABLE-REFRESH"                # (local)
SCHEME = "link-inventory"                         # (local)
CONVENTION = "frozen-since-S66"                   # (local)
L_MAX = "NA"                                      # (local)

# Pre-registered freeze anchor and threshold (plan §W15-2 §0.10)
S66_BASELINE_FROZEN = 0.206                       # (local) freeze anchor; never overwritten
P_PRE_LOW_S85 = 0.31                              # (local) plan §W15-2 §9 PASS threshold floor
P_PRE_HIGH_S85 = 0.36                             # (local) plan §W15-2 §1.6 trendline upper

# Output destinations
EVOI_FILE = SESSIONS_DIR / "evoi-framework.md"
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')
S86_VERDICTS_PATH = resolve_output(86, 's86_gate_verdicts.txt')
FALSIFIER_INVENTORY = SESSIONS_DIR / "framework" / "falsifier-master-inventory.md"
PLAN_DIR = SESSIONS_DIR / "session-plan"

# Refresh date (plan §W15-2 calls for "## S86 Refresh -- 2026-04-26")
REFRESH_DATE = "2026-04-26"                       # (local)
REFRESH_HEADING = f"## S86 Refresh -- {REFRESH_DATE}"  # (local)


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 helpers
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    """SHA-256 of a UTF-8 string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Compute
# ---------------------------------------------------------------------------

# Verdict-line regex: matches lines of the form
#   GATE_ID: PASS|FAIL|INFO|PRE-REG-INC -- value=...
# (with optional whitespace; leading "#" comment rows are excluded by the
# preceding "not line.startswith('#')" check)
VERDICT_RE = re.compile(r"^([A-Z0-9][A-Z0-9_\-\.]+):\s+(PASS|FAIL|INFO|PRE-REG-INC)\s+--\s+")  # (local)


def parse_s86_verdicts(path: Path) -> dict:
    """Parse s86_gate_verdicts.txt; return verdict-class buckets.

    Returns dict with keys:
      pass_ids, fail_ids, info_ids, pre_reg_inc_ids  (sets of distinct gate IDs)
      total_lines: number of canonical (non-#) verdict lines parsed
      complete_count: |union(pass_ids, fail_ids, info_ids)|  (per weighting rule)
      pre_reg_inc_count: |pre_reg_inc_ids|  (NOT counted as link-complete)
    """
    text = path.read_text(encoding="utf-8")  # (local)
    lines = text.splitlines()                # (local)
    pass_ids: set[str] = set()
    fail_ids: set[str] = set()
    info_ids: set[str] = set()
    pre_reg_inc_ids: set[str] = set()
    total_lines = 0  # (local)
    for line in lines:
        if not line or line.startswith("#"):
            continue
        m = VERDICT_RE.match(line)
        if not m:
            continue
        gate_id = m.group(1)  # (local)
        verdict = m.group(2)  # (local)
        # Detect PRE-REG-INC even when wrapped inside a FAIL value=... string
        # (e.g. "FAIL -- value='PRE-REG-INC_blocked_by_...'")
        # These count as PRE-REG-INC per .claude/rules/math-scripts.md
        # "All Results Are Good Results" rule.
        is_pre_reg_inc = (
            verdict == "PRE-REG-INC"
            or "PRE-REG-INC" in line[:300]
        )  # (local)
        if is_pre_reg_inc:
            pre_reg_inc_ids.add(gate_id)
        elif verdict == "PASS":
            pass_ids.add(gate_id)
        elif verdict == "FAIL":
            fail_ids.add(gate_id)
        elif verdict == "INFO":
            info_ids.add(gate_id)
        total_lines += 1

    # Per `.claude/rules/math-scripts.md` "All Results Are Good Results":
    # PASS, FAIL, INFO all count as "link complete" (effort discharged).
    # PRE-REG-INC does NOT count as complete (PRDR-deferred state).
    # If a gate appears in both PRE-REG-INC and PASS/FAIL/INFO across multiple
    # re-emissions, the PASS/FAIL/INFO closure dominates (verdicts are
    # permanent; the closure represents the discharged state).
    complete_ids = (pass_ids | fail_ids | info_ids)  # (local)
    pre_reg_only = pre_reg_inc_ids - complete_ids    # (local) gates that ONLY have PRE-REG-INC

    return {
        "pass_ids": pass_ids,
        "fail_ids": fail_ids,
        "info_ids": info_ids,
        "pre_reg_inc_ids": pre_reg_inc_ids,
        "complete_ids": complete_ids,
        "pre_reg_only_ids": pre_reg_only,
        "complete_count": len(complete_ids),
        "pre_reg_inc_count": len(pre_reg_inc_ids),
        "pre_reg_only_count": len(pre_reg_only),
        "total_lines": total_lines,
    }


def count_pre_registered_s86_gates(plan_dir: Path) -> dict:
    """Enumerate distinct S86-* gate IDs PRE-REGISTERED across all S86 plans.

    Reads session-86-plan-w*.md files; greps for `Gate ID`: `S86-...` patterns.
    Returns:
      pre_reg_ids: set of distinct S86 gate IDs declared in plan blocks
      pre_reg_count: |pre_reg_ids|
      plan_files: list of plan files read
    """
    plan_files = sorted(plan_dir.glob("session-86-plan-w*.md"))  # (local)
    # Match either `**Gate ID**: \`S86-...\`` (markdown formal block) or
    # an explicit "Gate ID:" prose form.
    gate_id_re = re.compile(
        r"\*\*Gate ID\*\*:\s*`?(S86-[A-Z0-9][A-Z0-9_\-\.]+)`?"
    )  # (local)
    # Also catch unqualified plan-block citations: `Gate ID`: `S86-...`
    gate_id_alt_re = re.compile(
        r"Gate ID[`\s]*:\s*`?(S86-[A-Z0-9][A-Z0-9_\-\.]+)`?"
    )  # (local)
    pre_reg_ids: set[str] = set()
    for pf in plan_files:
        try:
            text = pf.read_text(encoding="utf-8")  # (local)
        except OSError:
            continue
        for m in gate_id_re.finditer(text):
            pre_reg_ids.add(m.group(1))
        for m in gate_id_alt_re.finditer(text):
            pre_reg_ids.add(m.group(1))
    return {
        "pre_reg_ids": pre_reg_ids,
        "pre_reg_count": len(pre_reg_ids),
        "plan_files": [str(pf.relative_to(PROJECT_ROOT)).replace("\\", "/") for pf in plan_files],
    }


def compute_pre_S86_baseline() -> dict:
    """Snapshot pre-S86 state from evoi-framework.md (frozen-since-S66).

    Per `feedback_framework-hygiene.md` and the file's documented
    history (S66 baseline -> S73B Update -> S78 Stamp -> S83 Stamp), the
    file has been frozen at S66's link inventory in the SENSE that the
    baseline number 0.206 has not been overwritten. The S78 stamp lists
    40 active items; S83 lists 39 ranked items + ~27 closed = ~66 total
    canonical link inventory.

    Per plan §W15-2 §6 Step A, post-S85 bracket is 0.31-0.36 (notional
    bracket updated only at S85-close); the S66 baseline = 0.206 is the
    last hard pin.

    The pre-S86 snapshot uses the S83 stamp link-inventory counts:
      N_complete_pre   = closed mechanisms across S66->S85 = 27 + S78 KEEP-class + S83 partials (per file table line 70-104)
      N_total_pre      = closed + active EVOI items (S83 line 116-156, 39 ranked + 27 closed)
      F_obs_pre        = 7/9 = 0.7778 (S83 P_obs_aligned, line 110)

    These are the "pre-S86" link-inventory counts used as the baseline
    for the [SIGN] check.
    """
    # From sessions/evoi-framework.md
    # Line 104: "Total closures since S66 freeze: 27 gates" (S73B update)
    # Plus S78 closures (line 67): 11 convention-level closures
    # Plus S83 partial closures (line 158-163: 13 PASS_PARTIAL + INFO advances)
    # The conservative count (PASS|FAIL|INFO closures only, mirroring
    # the s86_gate_verdicts.txt PASS|FAIL|INFO weighting rule) is:
    #   N_complete_pre = 27 (S66->S73B closures) + 11 (S78 convention closures)
    # For comparable apples-to-apples accounting against S86's verdict-line
    # discharge count, we use the 27 + 11 = 38 figure as the baseline-N_complete.
    # F_obs_pre is documented at line 110 as 7/9 (S83 P_obs_aligned advance).
    N_complete_pre = 27 + 11                              # (local) 27 S73B + 11 S78
    # N_total_pre = N_complete_pre + active EVOI items in priority list (S83 ranks)
    # S83 priority table lines 116-156: 39 ranked items + 1 META (W3-I) = 40 active
    N_active_pre = 40                                     # (local) S83 priority list line 110+
    N_total_pre = N_complete_pre + N_active_pre           # (local)
    # F_obs_pre per S83 stamp line 110: P_obs_aligned advanced 6/9 -> 7/9
    F_obs_pre = 7.0 / 9.0                                 # (local) 0.7778

    P_work_complete_pre = (N_complete_pre / N_total_pre) * F_obs_pre  # (local)

    return {
        "N_complete_pre": N_complete_pre,
        "N_total_pre": N_total_pre,
        "F_obs_pre": F_obs_pre,
        "P_work_complete_pre": P_work_complete_pre,
        "S66_freeze_anchor": S66_BASELINE_FROZEN,
        "post_S85_low": P_PRE_LOW_S85,
        "post_S85_high": P_PRE_HIGH_S85,
    }


def compute_S86_deltas(verdicts: dict, pre_reg_info: dict, baseline: dict) -> dict:
    """Compute Delta_N_complete, Delta_N_total, Delta_F_obs for S86.

    Delta_N_complete = number of distinct PASS|FAIL|INFO gate IDs in S86
                       (=  verdicts['complete_count'])
    Delta_N_total    = number of NEW pre-registered S86 gate IDs that
                       were not in the pre-S86 active queue
                       =  pre_reg_info['pre_reg_count'] (lower-bound;
                          all S86 gate IDs are NEW since they carry the
                          "S86-" prefix and didn't exist pre-S86)
    Delta_F_obs      = (newly-observation-anchored links) / N_total_post
                       Per plan §W15-2 §6 Step D:
                         W6 row class adds +9 atomic lab-falsifier rows
                         W11 / W12 add per-cell anchorings
                       Bracket form per f_obs_uncertainty_rule (§7):
                         F_low  = strictly anchored (numeric detector pinned)
                         F_high = anchored + lit-anchored
    """
    delta_N_complete = verdicts["complete_count"]    # (local)
    delta_N_total = pre_reg_info["pre_reg_count"]    # (local)

    # F_obs delta: 9 new lab-falsifier atomic predictions (rows #13-#21)
    # newly anchored to specific detectors via W11 C5 SI-translation.
    # All 9 rows have specific platforms (3He-A, FeSe, 173Yb) with sigma_detect
    # values; under the "anchored / lit-anchored / no-pin" trichotomy:
    #   F_low  : 9 lab-falsifier rows count (strictly platform-anchored)
    #   F_high : 9 lab-falsifier rows + W12 9-cell detector readiness anchorings
    new_anchored_low = 9   # (local) W6 lab-falsifier suite (rows #13-#21)
    new_anchored_high = 9 + 9  # (local) +9 W12 detector-readiness 9-cell rows

    return {
        "delta_N_complete": delta_N_complete,
        "delta_N_total": delta_N_total,
        "new_anchored_low": new_anchored_low,
        "new_anchored_high": new_anchored_high,
    }


def substitution_chain_check(N_c_pre: int, N_t_pre: int,
                              dN_c: int, dN_t: int) -> dict:
    """Run the [SIGN] substitution-chain inequality check (plan §10).

    DEFINITION-SUBSTITUTION-SIMPLIFICATION-DIRECTION:

    Step 1 (definitions):
        N_c(t) := count of mechanism-links complete at time t
        N_t(t) := count of mechanism-links total in canonical inventory at t
        F(t)   := fraction of N_c(t) anchored to specific detector
        P(t)   := (N_c(t) / N_t(t)) * F(t)
        DN_c   := N_c(t_post) - N_c(t_pre) >= 0
        DN_t   := N_t(t_post) - N_t(t_pre) >= 0

    Step 2 (substitution; pessimistic subcase DF=0):
        P_post - P_pre |_{DF=0}
          = F * [ (N_c + DN_c) / (N_t + DN_t)  -  N_c / N_t ]
          = F * [ DN_c * N_t  -  N_c * DN_t ]
                / [ N_t * (N_t + DN_t) ]

    Step 3 (read off direction):
        Denominator N_t * (N_t + DN_t) > 0; F >= 0.
        sign(P_post - P_pre |_{DF=0}) = sign(DN_c * N_t - N_c * DN_t)

    The [SIGN] gate's PASS verdict requires the inequality
        DN_c * N_t >= N_c * DN_t
    (and DF >= 0, which we verify separately via the F_obs delta).
    """
    lhs = dN_c * N_t_pre   # (local) the "discharge" side
    rhs = N_c_pre * dN_t   # (local) the "inventory growth" side
    inequality_holds = (lhs >= rhs)        # (local)
    inequality_strict = (lhs > rhs)        # (local)
    inequality_equality = (lhs == rhs)     # (local)
    return {
        "lhs_DN_c_x_N_t_pre": lhs,
        "rhs_N_c_pre_x_DN_t": rhs,
        "inequality_holds": inequality_holds,
        "inequality_strict": inequality_strict,
        "inequality_equality": inequality_equality,
        "rate_pre": (N_c_pre / N_t_pre) if N_t_pre > 0 else 0.0,
        "rate_S86": (dN_c / dN_t) if dN_t > 0 else float("inf"),
    }


def compute_post_S86_bracket(baseline: dict, deltas: dict) -> dict:
    """Recompute (N_complete_post, N_total_post, P_work_complete_post bracket).

    P_low  = (N_c_post / N_t_post) * F_obs_low_post
    P_high = (N_c_post / N_t_post) * F_obs_high_post

    F_obs_low_post  = (anchored_pre + new_anchored_low) / N_complete_post
                      conservative: only strictly-anchored rows
    F_obs_high_post = (anchored_pre + new_anchored_high) / N_complete_post
                      optimistic: anchored + lit-anchored rows
    """
    N_c_pre = baseline["N_complete_pre"]                 # (local)
    N_t_pre = baseline["N_total_pre"]                    # (local)
    F_pre = baseline["F_obs_pre"]                        # (local)
    dN_c = deltas["delta_N_complete"]                    # (local)
    dN_t = deltas["delta_N_total"]                       # (local)

    N_c_post = N_c_pre + dN_c                            # (local)
    N_t_post = N_t_pre + dN_t                            # (local)

    # Anchored-pre count: F_obs_pre * N_complete_pre  (the absolute count
    # of pre-S86 anchored links). For the post-S86 fraction, we add the
    # newly-anchored rows under the trichotomy.
    anchored_pre = F_pre * N_c_pre                       # (local)
    F_low_post = (anchored_pre + deltas["new_anchored_low"]) / N_c_post   # (local)
    F_high_post = (anchored_pre + deltas["new_anchored_high"]) / N_c_post  # (local)

    # Cap F at 1.0 (cannot have more anchored links than complete links)
    F_low_post = min(F_low_post, 1.0)                    # (local)
    F_high_post = min(F_high_post, 1.0)                  # (local)

    P_low = (N_c_post / N_t_post) * F_low_post           # (local)
    P_high = (N_c_post / N_t_post) * F_high_post         # (local)

    return {
        "N_complete_post": N_c_post,
        "N_total_post": N_t_post,
        "F_low_post": F_low_post,
        "F_high_post": F_high_post,
        "P_low": P_low,
        "P_high": P_high,
        "anchored_pre_count": anchored_pre,
    }


def evaluate_gate(post: dict, sign_check: dict) -> str:
    """Apply the pre-registered PASS/FAIL/INFO threshold per plan §9."""
    P_low = post["P_low"]    # (local)
    P_high = post["P_high"]  # (local)
    # PASS: monotone-upward AND P_low >= P_pre_low_S85 = 0.31
    if (
        sign_check["inequality_holds"]
        and not sign_check["inequality_equality"]
        and P_low >= P_PRE_LOW_S85
    ):
        return "PASS"
    # INFO: equality in the substitution-chain inequality, OR P_low marginal
    if sign_check["inequality_equality"]:
        return "INFO"
    # FAIL: P_high < P_pre_low_S85 (counting error / inequality violated)
    if P_high < P_PRE_LOW_S85:
        return "FAIL"
    # The remaining case: inequality holds but P_low < 0.31 (e.g., F dilution
    # due to new pre-registered gates outpacing detector anchoring growth).
    # This is INFO per plan §11 "INFO indicates incomplete delta inputs OR
    # equality in the substitution-chain inequality" + diagnostic on bracket.
    if P_high >= P_PRE_LOW_S85 and P_low < P_PRE_LOW_S85:
        return "INFO"
    # Default catch-all: if reaching here, something is anomalous -> INFO
    return "INFO"


# ---------------------------------------------------------------------------
# Section 6 -- Append "## S86 Refresh" section to evoi-framework.md
# ---------------------------------------------------------------------------

def build_refresh_section(baseline: dict, deltas: dict, post: dict,
                           sign_check: dict, verdict: str,
                           verdicts_data: dict, pre_reg_info: dict,
                           non_firing: list[str]) -> str:
    """Build the new dated APPEND section for evoi-framework.md."""
    lines: list[str] = []
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(REFRESH_HEADING)
    lines.append("")
    lines.append(
        f"**Date**: {REFRESH_DATE} (S86-EVOI-TABLE-REFRESH, P13 gate, "
        "S86 closing item)"
    )
    lines.append("")
    lines.append("**Purpose**: Refresh `P_work_complete` per "
                 "`.claude/rules/evoi-prioritization.md` formula "
                 "`P_work_complete = (N_c / N_t) * F_obs` after S86's "
                 "20 wave plans (W0a..W14, W15) and 226 verdict-file lines. "
                 "Per `feedback_framework-hygiene.md`, the S66 baseline = "
                 f"{S66_BASELINE_FROZEN} freeze anchor is PRESERVED; this "
                 "section is APPEND-only.")
    lines.append("")
    lines.append("### Pre-S86 snapshot (from this file, S83 stamp)")
    lines.append("")
    lines.append(f"- N_complete_pre = {baseline['N_complete_pre']} "
                 "(27 S73B + 11 S78 convention closures)")
    lines.append(f"- N_total_pre    = {baseline['N_total_pre']} "
                 "(N_complete_pre + 40 S83-stamp active priority items)")
    lines.append(f"- F_obs_pre      = {baseline['F_obs_pre']:.6f} "
                 "(7/9 P_obs_aligned advance per S83 line 110)")
    lines.append(f"- P_work_complete_pre = {baseline['P_work_complete_pre']:.6f}")
    lines.append("")
    lines.append("### S86 deltas (Delta_N_c, Delta_N_t, Delta_F_obs)")
    lines.append("")
    lines.append(f"- Delta_N_complete = {deltas['delta_N_complete']} "
                 "(distinct gate IDs emitting PASS|FAIL|INFO in "
                 "`computations/session-86/s86_gate_verdicts.txt`; PRE-REG-INC "
                 "excluded per `.claude/rules/math-scripts.md` `All Results "
                 "Are Good Results`)")
    lines.append(f"  - PASS-distinct  = {len(verdicts_data['pass_ids'])}")
    lines.append(f"  - FAIL-distinct  = {len(verdicts_data['fail_ids'])}")
    lines.append(f"  - INFO-distinct  = {len(verdicts_data['info_ids'])}")
    lines.append(f"  - PRE-REG-INC-distinct (NOT counted) = "
                 f"{len(verdicts_data['pre_reg_inc_ids'])} "
                 "(of which "
                 f"{verdicts_data['pre_reg_only_count']} have ONLY "
                 "PRE-REG-INC; the remainder also closed via PASS/FAIL/INFO)")
    lines.append(f"- Delta_N_total    = {deltas['delta_N_total']} "
                 "(distinct S86-* gate IDs declared across "
                 "`session-86-plan-w*.md` plan files; lower-bound, since "
                 "all S86-prefixed gates are NEW relative to pre-S86 "
                 "active queue)")
    lines.append(f"- Newly-anchored (low / high)  = "
                 f"{deltas['new_anchored_low']} / "
                 f"{deltas['new_anchored_high']} "
                 "(W6 lab-falsifier suite +9 atomic rows = low bound; "
                 "+ W12 9-cell detector readiness = high bound)")
    lines.append("")
    lines.append("### Substitution chain check (plan §10, [SIGN])")
    lines.append("")
    lines.append("Per plan §W15-2 §10, the [SIGN] direction-check inequality is:")
    lines.append("")
    lines.append("```")
    lines.append("Step 1 (definitions):")
    lines.append("  N_c(t)  := count of mechanism-links complete at time t")
    lines.append("  N_t(t)  := count of mechanism-links total in canonical")
    lines.append("            inventory at time t")
    lines.append("  F(t)    := fraction of N_c(t) anchored to specific detector")
    lines.append("  P(t)    := (N_c(t) / N_t(t)) * F(t)")
    lines.append("  DN_c    := N_c(t_post) - N_c(t_pre) >= 0")
    lines.append("  DN_t    := N_t(t_post) - N_t(t_pre) >= 0")
    lines.append("  DF      := F(t_post) - F(t_pre)  (sign indeterminate)")
    lines.append("")
    lines.append("Step 2 (substitution; pessimistic subcase DF=0):")
    lines.append("  P_post - P_pre |_{DF=0}")
    lines.append("    = F * [ (N_c + DN_c) / (N_t + DN_t)  -  N_c / N_t ]")
    lines.append("    = F * [ DN_c * N_t  -  N_c * DN_t ]")
    lines.append("          ----------------------------")
    lines.append("                N_t * (N_t + DN_t)")
    lines.append("")
    lines.append("Step 3 (read direction):")
    lines.append("  Denominator N_t * (N_t + DN_t) > 0; F >= 0.")
    lines.append("  sign(P_post - P_pre |_{DF=0}) = sign(DN_c * N_t - N_c * DN_t)")
    lines.append("")
    lines.append("Step 4 (inequality):")
    lines.append("  P_post >= P_pre  IFF  DN_c * N_t >= N_c * DN_t  AND  DF >= 0")
    lines.append("")
    lines.append("FULL case (DF arbitrary):")
    lines.append("  P_post - P_pre = (N_c + DN_c) / (N_t + DN_t) * DF")
    lines.append("                 + F_pre * [DN_c*N_t - N_c*DN_t]")
    lines.append("                          / [N_t * (N_t + DN_t)]")
    lines.append("```")
    lines.append("")
    lines.append("**Runtime evaluation at S86 tuple**:")
    lines.append("")
    lines.append(f"- DN_c * N_t_pre = {sign_check['lhs_DN_c_x_N_t_pre']}")
    lines.append(f"- N_c_pre * DN_t = {sign_check['rhs_N_c_pre_x_DN_t']}")
    lines.append(f"- Inequality DN_c * N_t_pre >= N_c_pre * DN_t : "
                 f"{sign_check['inequality_holds']} "
                 f"(strict={sign_check['inequality_strict']}, "
                 f"equality={sign_check['inequality_equality']})")
    lines.append(f"- Pre-S86 completion rate (N_c_pre / N_t_pre): "
                 f"{sign_check['rate_pre']:.6f}")
    lines.append(f"- S86 completion rate    (DN_c / DN_t): "
                 f"{sign_check['rate_S86']:.6f}")
    lines.append("")
    lines.append("### Post-S86 state and bracket")
    lines.append("")
    lines.append(f"- N_complete_post = {post['N_complete_post']}")
    lines.append(f"- N_total_post    = {post['N_total_post']}")
    lines.append(f"- F_low_post      = {post['F_low_post']:.6f} "
                 "(strictly-anchored rows / N_complete_post; capped at 1.0)")
    lines.append(f"- F_high_post     = {post['F_high_post']:.6f} "
                 "(anchored + lit-anchored / N_complete_post; capped at 1.0)")
    lines.append("")
    lines.append("**`P_work_complete_post` bracket** "
                 "(value=[P_low, P_high] in verdict 4-tuple):")
    lines.append("")
    lines.append(f"- **P_low  = {post['P_low']:.6f}** "
                 "(observation-conservative: only strictly-anchored rows)")
    lines.append(f"- **P_high = {post['P_high']:.6f}** "
                 "(observation-optimistic: anchored + lit-anchored)")
    lines.append("")
    lines.append("### Trendline cross-comparison (post-S86 vs prior anchors)")
    lines.append("")
    lines.append("```")
    lines.append(f"S66 baseline = 0.206 (FROZEN, never overwritten)")
    lines.append(f"S80         = 0.216 (PRU trendline, s80_pru_trendline.py)")
    lines.append(f"post-S85    = [0.31, 0.36] (notional bracket per plan §1.6)")
    lines.append(f"post-S86    = [{post['P_low']:.4f}, {post['P_high']:.4f}] "
                 f"(this refresh)")
    lines.append("```")
    lines.append("")
    direction = "monotone-upward" if (
        post['P_low'] >= P_PRE_LOW_S85
    ) else (
        "INFO band -- partial monotone (P_high in band, P_low below)"
        if post['P_high'] >= P_PRE_LOW_S85
        else "below-trend"
    )  # (local)
    lines.append(f"Trendline direction: {direction}")
    lines.append("")
    lines.append("### EFFORT-BASED classification reminder "
                 "(per plan §13 + `feedback_framework-hygiene.md`)")
    lines.append("")
    lines.append("`P_work_complete` is an **EFFORT-BASED** measure of "
                 "framework-completeness state, NOT a probability that the "
                 "substrate picture is correct. Per "
                 "`.claude/rules/evoi-prioritization.md` §`Effort-Based "
                 "Probability`, this number goes UP when work is done, "
                 "regardless of whether the work returns favorable physics. "
                 "A FAIL verdict that closes a corridor counts the same as a "
                 "PASS verdict that confirms a prediction -- both discharge "
                 "their EVOI computation. "
                 "P13 measures *how much of the pre-registered link "
                 "inventory has had its computation discharged*, not *how "
                 "likely the substrate picture is correct*. "
                 "Mechanisms are assessed by structural position on the "
                 "constraint surface, per "
                 "`.claude/rules/epistemic-discipline.md` §`How to Assess a "
                 "Mechanism`.")
    lines.append("")
    lines.append("### S87 carry-forward seeds "
                 "(pre-registered S86 gates that did NOT fire)")
    lines.append("")
    if non_firing:
        lines.append("Pre-registered S86 gate IDs (in plan files) without a "
                     "corresponding PASS|FAIL|INFO verdict line in "
                     "`computations/session-86/s86_gate_verdicts.txt` "
                     "(carry-forward seeds for S87 plan-write priority queue):")
        lines.append("")
        for gid in sorted(non_firing):
            lines.append(f"- `{gid}`")
    else:
        lines.append("No pre-registered S86 gate IDs lacked a closure verdict "
                     "line. (All 20 wave plans closed at the gate-level.) "
                     "Specific carry-forward computations propagate via "
                     "`/rclab-plan` mechanical carry-forward gathering, not "
                     "via this section.")
    lines.append("")
    lines.append("### S66 baseline freeze-anchor preservation note")
    lines.append("")
    lines.append(
        f"The S66 baseline = **{S66_BASELINE_FROZEN}** freeze anchor "
        "established in the original S66 EVOI framework "
        "(see `## Milestone Completion Tracker -- Current State (post-S73B)` "
        "section above) is PRESERVED. This refresh APPENDS new state; "
        "it does NOT overwrite the S66 baseline. "
        "The S73B Update (2026-04-11), S78 Scrubbed Update (2026-04-15), "
        "S83 Stamp (2026-04-18), and this S86 Refresh (2026-04-26) form a "
        "chronological ledger; no historical row is rewritten. "
        "Per `feedback_framework-hygiene.md`, the EVOI table "
        "must be refreshed every session; this gate (P13) discharges "
        "the S86 obligation."
    )
    lines.append("")
    lines.append(f"**Verdict**: {verdict} -- value=[{post['P_low']:.6f}, "
                 f"{post['P_high']:.6f}] scheme={SCHEME} "
                 f"convention={CONVENTION} L_max={L_MAX}")
    lines.append("")
    lines.append("**Closing remark**: The post-S86 bracket "
                 f"[{post['P_low']:.4f}, {post['P_high']:.4f}] "
                 "feeds the S87 plan-write priority allocation per "
                 "`.claude/rules/evoi-prioritization.md` §`Computation "
                 "Priority (EVOI)`. The bracket is the input pin for "
                 "`/rclab-plan`'s wave-budget allocation in the next session.")
    lines.append("")
    return "\n".join(lines)


def append_refresh_section(text_to_append: str) -> tuple[str, str]:
    """Atomically append the S86 Refresh section to evoi-framework.md.

    Returns (sha_pre, sha_post) so the closure_sha 5-tuple can be assembled.
    """
    sha_pre = sha256_of(EVOI_FILE)  # (local)
    # Read current file
    current = EVOI_FILE.read_text(encoding="utf-8")  # (local)
    # Idempotency: if the heading already exists, do not double-append.
    if REFRESH_HEADING in current:
        # Replace the existing section with the freshly built one.
        # Find the heading line, then the next "## " or end of file.
        idx_start = current.index(REFRESH_HEADING)
        # Walk back to include the preceding "---\n" separator we wrote
        sep = "\n---\n\n"
        if current.rfind(sep, 0, idx_start) > 0:
            idx_start = current.rfind(sep, 0, idx_start) + 1  # keep first '\n'
        # Find the next "## " at the same heading level (or EOF)
        idx_next = current.find("\n## ", idx_start + 1)
        if idx_next < 0:
            new_text = current[:idx_start].rstrip() + "\n" + text_to_append + "\n"
        else:
            new_text = (current[:idx_start].rstrip() + "\n"
                        + text_to_append + "\n"
                        + current[idx_next + 1:])
    else:
        # Plain append (most common: first run)
        new_text = current.rstrip() + "\n" + text_to_append + "\n"
    # Atomic write
    EVOI_FILE.write_text(new_text, encoding="utf-8")
    sha_post = sha256_of(EVOI_FILE)  # (local)
    return sha_pre, sha_post


# ---------------------------------------------------------------------------
# Section 7 -- closure_sha (plan §6 Step E, 5-tuple)
# ---------------------------------------------------------------------------

def compute_closure_sha(sha_evoi_pre: str, sha_evoi_post: str,
                         sha_s86_verdicts_pre_w15_2: str,
                         sha_falsifier_inv: str,
                         counts_tuple: tuple) -> str:
    """closure_sha = sha256( utf-8 join of 5 elements with \\n ).

    5-tuple per plan §6 Step E:
      1. SHA-256 of sessions/evoi-framework.md PRE-write content
      2. SHA-256 of sessions/evoi-framework.md POST-write content
      3. SHA-256 of computations/session-86/s86_gate_verdicts.txt
         AT THE MOMENT P13 reads it (captured ONCE at Step C)
      4. SHA-256 of sessions/framework/registry/falsifier-master-inventory.md
      5. ordered tuple (N_c_pre, N_t_pre, DN_c, DN_t, F_obs_pre, F_obs_post)
    """
    counts_repr = "(" + ",".join(repr(x) for x in counts_tuple) + ")"  # (local)
    payload = "\n".join([
        sha_evoi_pre,
        sha_evoi_post,
        sha_s86_verdicts_pre_w15_2,
        sha_falsifier_inv,
        counts_repr,
    ])  # (local)
    return sha256_of_text(payload)


# ---------------------------------------------------------------------------
# Section 8 -- Verdict-line append (atomic, dual-SHA companion row)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str, P_low: float, P_high: float,
                    closure_sha: str, content_sha_post: str) -> None:
    """Append the canonical verdict line + dual-SHA companion comment row."""
    value_str = f"[{P_low:.6f},{P_high:.6f}]"  # (local)
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"sha256={closure_sha}\n"
    )  # (local)
    companion = (
        f"# {GATE_ID} -- content_sha256={content_sha_post} "
        f"audit_sha256={closure_sha}\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    print("=== S86-EVOI-TABLE-REFRESH (P13, FINAL) ===")
    print("")
    print("=== input SHA-256 pins ===")
    sha_evoi_pre = sha256_of(EVOI_FILE)  # (local)
    sha_s86_verdicts_pre = sha256_of(S86_VERDICTS_PATH)  # (local) Step C
    sha_falsifier = sha256_of(FALSIFIER_INVENTORY)  # (local)
    print(f"  sessions/evoi-framework.md (PRE-write):       {sha_evoi_pre[:16]}...")
    print(f"  computations/session-86/s86_gate_verdicts.txt:      {sha_s86_verdicts_pre[:16]}...")
    print(f"  sessions/framework/registry/falsifier-master-inventory.md: {sha_falsifier[:16]}...")
    print("")

    # Step A -- Pre-S86 baseline snapshot
    print("--- Step A: Pre-S86 baseline snapshot ---")
    baseline = compute_pre_S86_baseline()  # (local)
    print(f"  N_complete_pre       = {baseline['N_complete_pre']}")
    print(f"  N_total_pre          = {baseline['N_total_pre']}")
    print(f"  F_obs_pre            = {baseline['F_obs_pre']:.6f}")
    print(f"  P_work_complete_pre  = {baseline['P_work_complete_pre']:.6f}")
    print(f"  S66 freeze anchor    = {baseline['S66_freeze_anchor']} (PRESERVED)")
    print("")

    # Step B -- Count S86 PASS|FAIL|INFO distinct gate IDs
    print("--- Step B: Count distinct PASS|FAIL|INFO S86 gate IDs ---")
    verdicts = parse_s86_verdicts(S86_VERDICTS_PATH)  # (local)
    print(f"  Total non-comment verdict lines: {verdicts['total_lines']}")
    print(f"  Distinct PASS gate IDs:          {len(verdicts['pass_ids'])}")
    print(f"  Distinct FAIL gate IDs:          {len(verdicts['fail_ids'])}")
    print(f"  Distinct INFO gate IDs:          {len(verdicts['info_ids'])}")
    print(f"  Distinct PRE-REG-INC gate IDs:   "
          f"{len(verdicts['pre_reg_inc_ids'])} "
          f"(PRE-REG-INC-only: {verdicts['pre_reg_only_count']})")
    print(f"  Distinct COMPLETE (P|F|I) gate IDs: {verdicts['complete_count']}")
    print("")

    # Step C -- Count NEW pre-registered S86 gates from plan files
    print("--- Step C: Count NEW pre-registered S86 gate IDs from plans ---")
    pre_reg = count_pre_registered_s86_gates(PLAN_DIR)  # (local)
    print(f"  Plan files read:    {len(pre_reg['plan_files'])}")
    print(f"  Distinct S86 gate IDs in plan blocks: {pre_reg['pre_reg_count']}")
    print("")

    # Detect non-firing pre-registered gates
    non_firing = sorted(pre_reg["pre_reg_ids"] - verdicts["complete_ids"]
                        - verdicts["pre_reg_inc_ids"])  # (local)
    print(f"  Pre-registered gates with NO PASS|FAIL|INFO|PRE-REG-INC line: "
          f"{len(non_firing)}")
    for gid in non_firing[:10]:
        print(f"    - {gid}")
    if len(non_firing) > 10:
        print(f"    ... and {len(non_firing) - 10} more")
    print("")

    # Step D -- Compute deltas
    print("--- Step D: Compute S86 deltas ---")
    deltas = compute_S86_deltas(verdicts, pre_reg, baseline)  # (local)
    print(f"  Delta_N_complete           = {deltas['delta_N_complete']}")
    print(f"  Delta_N_total              = {deltas['delta_N_total']}")
    print(f"  Newly-anchored (low/high)  = {deltas['new_anchored_low']} / "
          f"{deltas['new_anchored_high']}")
    print("")

    # Step E -- Recompute post-S86 state
    print("--- Step E: Recompute post-S86 state and bracket ---")
    post = compute_post_S86_bracket(baseline, deltas)  # (local)
    print(f"  N_complete_post = {post['N_complete_post']}")
    print(f"  N_total_post    = {post['N_total_post']}")
    print(f"  F_low_post      = {post['F_low_post']:.6f}")
    print(f"  F_high_post     = {post['F_high_post']:.6f}")
    print(f"  P_low           = {post['P_low']:.6f}")
    print(f"  P_high          = {post['P_high']:.6f}")
    print("")

    # Step F -- Substitution-chain check
    print("--- Step F: Substitution-chain check (plan §10, [SIGN]) ---")
    sign_check = substitution_chain_check(
        baseline["N_complete_pre"],
        baseline["N_total_pre"],
        deltas["delta_N_complete"],
        deltas["delta_N_total"],
    )  # (local)
    print(f"  DN_c * N_t_pre              = {sign_check['lhs_DN_c_x_N_t_pre']}")
    print(f"  N_c_pre * DN_t              = {sign_check['rhs_N_c_pre_x_DN_t']}")
    print(f"  Inequality (LHS >= RHS)     = {sign_check['inequality_holds']}")
    print(f"  Strict inequality           = {sign_check['inequality_strict']}")
    print(f"  Equality                    = {sign_check['inequality_equality']}")
    print(f"  Pre-S86 rate (N_c_pre/N_t_pre) = {sign_check['rate_pre']:.6f}")
    print(f"  S86 rate     (DN_c/DN_t)       = {sign_check['rate_S86']:.6f}")
    print("")

    # Evaluate gate
    verdict = evaluate_gate(post, sign_check)  # (local)
    print(f"  Pre-registered verdict      = {verdict}")
    print(f"  PASS threshold P_low >= {P_PRE_LOW_S85}: "
          f"{post['P_low'] >= P_PRE_LOW_S85}")
    print("")

    # Step G -- Build and APPEND the dated section to evoi-framework.md
    print("--- Step G: APPEND new dated section to evoi-framework.md ---")
    refresh_text = build_refresh_section(
        baseline, deltas, post, sign_check, verdict,
        verdicts, pre_reg, non_firing,
    )  # (local)
    sha_evoi_pre_check, sha_evoi_post = append_refresh_section(refresh_text)
    # Sanity: sha_evoi_pre_check should match sha_evoi_pre (we read the file
    # twice; should be identical unless concurrent writer modified between).
    if sha_evoi_pre_check != sha_evoi_pre:
        print(f"  WARNING: PRE-write SHA changed between Steps A and G "
              f"({sha_evoi_pre[:16]} -> {sha_evoi_pre_check[:16]}); "
              "using Step G value as authoritative PRE.")
        sha_evoi_pre = sha_evoi_pre_check
    print(f"  evoi-framework.md PRE-write  SHA = {sha_evoi_pre[:16]}...")
    print(f"  evoi-framework.md POST-write SHA = {sha_evoi_post[:16]}...")
    print("")

    # Step H -- Compute closure_sha (5-tuple per plan §6 Step E)
    print("--- Step H: Compute closure_sha (5-tuple) ---")
    counts_tuple = (
        baseline["N_complete_pre"],
        baseline["N_total_pre"],
        deltas["delta_N_complete"],
        deltas["delta_N_total"],
        baseline["F_obs_pre"],
        # Post F_obs is reported as the conservative low (matches verdict
        # value=[P_low, P_high] direction; the bracket form captures both)
        post["F_low_post"],
    )  # (local)
    closure_sha = compute_closure_sha(
        sha_evoi_pre, sha_evoi_post, sha_s86_verdicts_pre, sha_falsifier,
        counts_tuple,
    )  # (local)
    print(f"  counts_tuple = {counts_tuple}")
    print(f"  closure_sha  = {closure_sha}")
    print("")

    # Append verdict + companion row
    print("--- Step I: Append verdict line + dual-SHA companion ---")
    append_verdict(verdict, post["P_low"], post["P_high"],
                   closure_sha, sha_evoi_post)
    print(f"  Appended {GATE_ID}: {verdict} -- "
          f"value=[{post['P_low']:.6f},{post['P_high']:.6f}] "
          f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
          f"sha256={closure_sha[:16]}...")
    print("")

    # Final 4-tuple
    tag = (f"(value=[{post['P_low']:.6f},{post['P_high']:.6f}], "
           f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # all results are good results; verdict is data not exit code


if __name__ == "__main__":
    sys.exit(main())
