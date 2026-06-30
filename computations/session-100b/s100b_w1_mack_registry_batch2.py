# -*- coding: utf-8 -*-
"""
S100b Wave-1 mack-cosmic-bridge sole-writer registry batch 2 (registry-only, no compute).

Lands the two completed-gate routings per feedback_mack-bridge-role.md:

  1. Row #76 constraint-scope adjudication annotation (from W1-1
     S100b-X-C10-BBN-CONSTRAINT-RECONCILE: PASS, audit 26553084db8a42cd...) --
     appended to Row #76's annotation chain (after the S99 W2-2 stays-LIVE block),
     per WP s"W1-1 (7) Registration" Step 3 + the (5) constraint-scope statement.
  2. Row #1 SECONDARY-cell caveat (from W1-4 S100b-W0-BRANCH-RESOLUTION: INFO,
     audit c8ab70a1833f5602...) -- additive in-cell tag on the branch-iv entry
     (PRIMARY = A = -0.918 text untouched; leg-1 re-verified it clean) + full
     sub-row `1.w0-branch-resolution-s100b` after `1.wa-robust-s100b`, per the
     WP s"W1-4 Empirical assessment (3)" mack-routing sentence.

All numbers/SHAs are transcribed from the verdict file canonical+companion rows
and the WP s"W1-1"/s"W1-4" sections (no new computation). Idempotency-guarded
per edit; single read-modify-write (sole-writer file, no parallel-writer race).
NOT a computation gate: no verdict line is emitted.
"""

import io
import sys

INVENTORY = r"C:\sandbox\Ainulindale Exflation\sessions\framework\registry\falsifier-master-inventory.md"  # (local)

AUDIT_W11 = "26553084db8a42cd1ca887e14c59dd8a7e795cea7b3c378d868afcafcc00e87e"  # (local)
CONTENT_W11 = "34aee687cd5137dbea0f5839b070f28b56ffa64ade0cf59dbf209fe2ab938541"  # (local)
AUDIT_W14 = "c8ab70a1833f56029452a3ae00587f96e41bbb64bd9b067092f491c14f36ed1b"  # (local)
CONTENT_W14_16 = "ebe9bbd0072226ba"  # (local)

MARKER_76 = "Constraint-scope adjudication annotation (S100b W1-1"  # (local)
MARKER_SUBROW = "| 1.w0-branch-resolution-s100b |"  # (local)
CELL_TARGET = "L=12 upper: -0.842454 (W10-2 branch-iv)"  # (local)
CELL_REPLACEMENT = (
    "L=12 upper: -0.842454 (W10-2 branch-iv; **stability UNVERIFIED** -- both w_0(L) "
    "evaluator routes NOT RECOVERABLE post-S86 R_JE retirement, S100b W1-4 INFO "
    f"audit_sha256={AUDIT_W14}; see sub-row 1.w0-branch-resolution-s100b)"
)  # (local)

ANNOT_76 = f"""
**Constraint-scope adjudication annotation (S100b W1-1 `S100b-X-C10-BBN-CONSTRAINT-RECONCILE`: PASS — the S66-vs-S98/S99 two-route BBN adjudication; mack-cosmic-bridge sole-writer landing per the gate's WP §W1-1 registration record Step 3).** Gate `S100b-X-C10-BBN-CONSTRAINT-RECONCILE` (S100b W1-1, PASS, `[VERIFY]`, gen-physicist; `audit_sha256={AUDIT_W11}`, `content_sha256={CONTENT_W11}`; canonical line 23 + companion rows `# constraint_scope(W1-2):` / `# anchor_evidence:` lines 26–27 of `computations/session-100b/s100b_gate_verdicts.txt`) adjudicated the standing direction conflict between the S66 G_eff(BBN) route and the S98/S99 ΔN_eff lever. **Outcome = OPERATIVE-LEVER+G_EFF-RESCOPED**:

- **Same-observable theorem (EXACT)**: the S66 "G-renormalization" form and the additive ΔN_eff form are ONE observable — `1 + f ≡ 1/(1 − α)` for `α = f/(1+f)` (Sage symbolic 0; numerical deviation 1.3e-46). The published OPPOSITE n_eff relief directions are OPPOSITE NORMALIZATION ANCHORS, not a contradiction: `d ln f/d n_eff = ln(H_BBN/H_anchor)` = +40.2756 at the z0 anchor (relief from BELOW) vs < 0 at the S66 fold-side/upstream anchor (relief from ABOVE); the S66 table mixes anchors across rows (its n=2 row is anchor-degenerate).
- **Operative falsifier for this row's BBN cross-cut (constraint-scope statement, cited by W1-2 and any S101 corridor gate)**: the z0-anchored lever `f = frac_base·exp((n_eff−2)·X)` with `ΔN_eff = f/0.22710732` (exact), `X = ln(H_BBN/H_0) = 40.2756`. Budgets: `ΔN_eff ≤ {{1 (canonical), 0.107 (GH-2026 EXTERNAL, arXiv:2603.13226), 0.0899 (Cyburt-2016 G_eff-2% EXTERNAL — the TIGHTEST)}}` ⟺ `n_eff ≤ {{1.959839, 1.904348, 1.900014}}`. The substrate pin `n_eff = 1.978111` (HARD from-below, S98-MK3-1) exceeds ALL three crossings ⇒ the standing S98/S99 FAILs are CONFIRMED at their proper scope (`ΔN_eff = 2.0873`: 2.09× the canonical budget, 19.51× the external 0.107). Relief inside the tracking family is not substrate-justified (S99-W2-BBN-RELIEF); the remaining relief route is a NON-TRACKING epoch profile — exactly the W1-2 question (`S100b-X-C10-RHOVAC-EPOCH-PROFILE`, CONDITIONAL on S100a QEQ-DRIVE).
- **S66 G_eff route RESCOPED, not retired**: its FORM is retained as the exact unit-conversion of the same observable, and its 2% bound maps to the TIGHTEST ΔN_eff budget (0.0899 < 0.107 < 1); its three-row n_eff TABLE is rescoped as a fold-anchored boundary-value question (anchor-mixed as published). The S66 from-above escape (`n_eff = 2.3`) is NOT available to DILUTION-CC: it undershoots the present-day CC by 7.29 OOM (`α_V` ratio 4.94e-8), and the exact identity `disc(BBN) × cc_ratio(z=0) = 1.0320000000000000000` (Sage QQ) shows the inter-route BBN discrepancy IS the z=0 CC-miss factor — one number measured at two ends. Solving BBN that way un-solves the CC.
- **Window-8 / BBN-VOLOVIK-67 status: UNCHANGED (STAYS LIVE, Track-B structural sub-threshold tension per the S99 W2-2 annotation immediately above, now confirmed at its proper scope).** This annotation fixes WHICH lever is the operative falsifier and at WHAT budgets; it moves no tension and no Atlas-04 tag (C10 stays `ASSUMED-PARTIALLY-PROVEN`).

**Cross-references**: WP `sessions/session-100b/session-100b-w1-workingpaper.md` §W1-1 (Chains A/B/C with substituted numbers, 4-class adjudication rubric, constraint-scope statement (5), registration record (7)); `canonical_constants.py` (`delta_N_eff_budget_GoldsteinHill_2026 = 0.107` EXTERNAL-NON-CANONICAL + `T_RH_GeV = 1.70e15`, both landed by W1-1 Step 2); the S97 W-1 / S98 CF-MK3-2 / S99 W2-2 annotation chain above (all confirmed at their proper scopes); Atlas-04 C10 row (tag UNMOVED). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole writer for `falsifier-master-inventory.md` (AMRI-PROMOTED 2026-04-28).
"""  # (local)

SUBROW = (
    "| 1.w0-branch-resolution-s100b | audit pins (Row #1 SECONDARY-cell stability caveat; S100b W1-4 "
    "`S100b-W0-BRANCH-RESOLUTION` sagan-empiricist leg-1/leg-2; mack sole-writer landing per the WP "
    "§W1-4 routing sentence) | §5 DR3 reversal-protocol SECONDARY caveat: branch-iv w_0_B = -0.842454 "
    "L_max stability **UNVERIFIED** — both candidate w_0(L) evaluator routes NOT RECOVERABLE post-S86 "
    "R_JE retirement (route-α: the post-S86 formulation defines NO w_0 evaluator, R_JE slot vacant; "
    "route-β: no w_0-unit mapping in the S85-W10 anchor script); spread honestly UNCOMPUTABLE, "
    "pre-registered INFO shape (ii) — a formulation-gap record, NOT a drift verdict | leg-2 route "
    "ladder RA-1..RA-4 + RB-1..RB-2 (WP §W1-4 evidence table); diagnostic-only candidates C1-C4 + "
    "archaeology row C0 | **PRIMARY = A = -0.918 re-confirmed CLEAN** (leg-1 mechanical re-execution "
    "of `w0-primary-decision-rule.md` §3 on current registry state; data-proximity exclusion honored; "
    "§5 reversal protocol ARMED UNMODIFIED, decision-rule file SHA bit-identical to the S86 freeze "
    "`da2ba36cc861ddf3...`). SECONDARY = -0.842454 remains L=5-anchored (SV1 `6c0063d22c520da9...`); "
    "rho_B(L) UNDEFINED post-S86 ⇒ CAC spread UNCOMPUTABLE; NO `w0_FW_R842` promotion (Step-2 "
    "write-order fires on PASS only) | diagnostic sensitivity span (0.000830, 0.036327) across "
    "unpinned recombination candidates CROSSES the 0.025 PASS/INFO boundary ⇒ the recombination "
    "freedom is DECISION-RELEVANT (executing any one choice would set the verdict by execution-time "
    "convention selection — the pre-registered INFO-(ii) closure is the honest outcome); archaeology "
    "C0: the retired legacy evaluator's own L=10 value sits 6.2σ_DR3 from the registered anchor "
    "(-0.842454 is NOT the large-L limit of its own retired evaluator) | n/a (audit-pin sub-row; "
    "leg-1 PRIMARY-clean and leg-2 SECONDARY-unverified are separate legs; the 0.731σ post-Dovekie "
    "branch-iv proximity stays citable only WITH the branch-shopping caveat) | inherited Row #1 "
    "(DESI DR3, window open 2026-04-23, data ~2027): a DR3 hit inside the §5 reversal band "
    "[-0.86, -0.83] would re-pin to a value whose truncation convergence is an OPEN derivation item "
    "— queued fix `CF-S101-W0-BRANCH-IV-EVALUATOR` (derive the post-S86 branch-iv evaluator with "
    "zero free normalization, then re-run the CAC spread test at unchanged thresholds) | zeta "
    "(SV1-anchored) | CAC-branch-iv-anchored-L10 | mixed | `" + CONTENT_W14_16 + "` | `" + AUDIT_W14 +
    "` (full 64-hex; gate INFO; verdict line 19 + companion rows 20-22 of "
    "computations/session-100b/s100b_gate_verdicts.txt) |\n"
)  # (local)


def main():
    with io.open(INVENTORY, "r", encoding="utf-8") as f:
        text = f.read()  # (local)
    lines = text.splitlines(keepends=True)  # (local)
    changed = False  # (local)

    # ---- Edit 1: Row #76 annotation block ----
    if MARKER_76 in text:
        print("  [1] Row #76 W1-1 annotation already present -- skipping (idempotent)")
    else:
        # insertion anchor: the S99 W2-2 block's Cross-references line (starts with
        # "**Cross-references**: Row #76 primary cell + the S98 CF-MK3-2")
        idx = None  # (local)
        for i, ln in enumerate(lines):
            if ln.startswith("**Cross-references**: Row #76 primary cell + the S98 CF-MK3-2"):
                idx = i
                break
        if idx is None:
            print("FATAL: S99-block cross-references anchor not found")
            return 2
        lines.insert(idx + 1, ANNOT_76)
        changed = True
        print(f"  [1] Row #76 W1-1 constraint-scope annotation inserted after line {idx + 1}")

    # ---- Edit 2a: Row #1 in-cell SECONDARY caveat tag (additive) ----
    text2 = "".join(lines)  # (local)
    n_target = text2.count(CELL_TARGET)  # (local)
    if "stability UNVERIFIED** -- both w_0(L)" in text2:
        print("  [2a] Row #1 in-cell caveat already present -- skipping (idempotent)")
    elif n_target != 1:
        print(f"FATAL: Row #1 cell target string count = {n_target} (expected 1) -- aborting in-cell edit")
        return 2
    else:
        text2 = text2.replace(CELL_TARGET, CELL_REPLACEMENT)
        changed = True
        print("  [2a] Row #1 SECONDARY-cell caveat tag applied (additive; PRIMARY -0.918 text untouched)")

    # ---- Edit 2b: sub-row 1.w0-branch-resolution-s100b ----
    if MARKER_SUBROW in text2:
        print("  [2b] sub-row 1.w0-branch-resolution-s100b already present -- skipping (idempotent)")
    else:
        lines2 = text2.splitlines(keepends=True)  # (local)
        idx = None  # (local)
        for i, ln in enumerate(lines2):
            if ln.startswith("| 1.wa-robust-s100b |"):
                idx = i
                break
        if idx is None:
            print("FATAL: 1.wa-robust-s100b anchor sub-row not found")
            return 2
        lines2.insert(idx + 1, SUBROW)
        text2 = "".join(lines2)
        changed = True
        print(f"  [2b] sub-row 1.w0-branch-resolution-s100b inserted after line {idx + 1}")

    if changed:
        with io.open(INVENTORY, "w", encoding="utf-8", newline="") as f:
            f.write(text2)
        print("  inventory written.")
    print("Wave-1 registry batch 2 complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
