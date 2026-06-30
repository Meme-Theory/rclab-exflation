# S114 W3-3 — §VII.CK SHAPE-wall landing (VERIFY-THEOREM, per-block supertrace identity + pure-symmetric Casimir wall)

Cross-domain recipe for a [VERIFY-THEOREM] §VII registry-landing gate whose COMPUTE leg is a
McKean-Singer supertrace ZERO-IDENTITY, where the canonical L_max enumeration hits the
recursive-Casimir construction wall.

## The gate shape
CF-S114-YUK-SHAPE-WALL-VII-LANDING: register the SHAPE-Branch Homogeneity Obstruction (D1-D3
closed-class) as a §VII STAGE-1-CANDIDATE + reproduce D1 `Tr[γ₉ D_K^{odd}] ≡ 0` machine-exact.
Source = a frozen workshop §4a Stage-0 text (ws-s113-7-yukshape-verdict.md), transcribed VERBATIM.
Landed PASS at §VII.CK (frontier was §VII.CJ; matched plan pin, NO reroute).

## Load-bearing lessons (the parts that bit / would have bitten)

1. **D1 is a PER-BLOCK exact-zero, so the L_max enumeration is FAITHFUL under truncation.**
   `{γ₉, D_K} = 0` (Cl(8) `{γ₉,γ_a}=0` ∧ spin-offset `{γ₉,Ω}=0`, both EXACTLY 0) ⇒
   `Tr[(I⊗γ₉) D_pi^{2k+1}] = 0` for EACH Peter-Weyl sector `(p,q)` INDEPENDENTLY (trace =
   its own negative by cyclicity). The full-spectrum supertrace is the PW-multiplicity-weighted
   SUM, so there is NO cross-sector cancellation to verify — every block contributes exactly 0.
   This is what licenses an operational-L downgrade: unconstructed sectors contribute 0 by the
   SAME argument. Result was `0.0` exactly (not 1e-16) at every block + Sage-QQ exact-ring proof.

2. **The recursive-Casimir wall is the PURE-SYMMETRIC (n,0)/(0,n) sectors, NOT high p+q in general.**
   Probe timing at τ_fold: ALL mixed sectors (1,8)/(2,7)/(3,7)/(8,1) build in <1 s even at dim>150;
   but `(0,8)`/`(8,0)` take ~29-35 s (they use `irrep_symmetric_power`), and `(0,9)/(0,10)/(9,0)/(10,0)`
   are infeasible within an agent timeslot. A naive L=10 full run STALLS building (0,9)/(0,10) and
   blows the agent budget (first run hit 644 s before I added the guard; the stall was the 4 corners).
   FIX: a corner-skip guard `if dim>=60 and (p==0 or q==0) and p+q>=9: skip` constructs 62/66 sectors
   (L_max_operational=10, all mixed + (0,8)/(8,0)) in ~10 min; the 4 corners skip instantly and
   contribute 0 by lesson 1. This is math-scripts.md §"D_K Block-Diagonality" operational-L downgrade
   with honest disclosure (in-session structural correction, NOT convention-shopping — convention tag
   UNCHANGED, deviation disclosed in verdict value + companion + WP §Methodology).

3. **The Bash 5-min tool ceiling ≠ the background-script ceiling.** My `until`-loop waiters timed out
   at 5 min (exit 143) repeatedly while the `run_in_background` Python kept running fine (644 s wall).
   Do NOT mistake the waiter timeout for a script crash — verify via (a) live `ps -W | grep .venv312`,
   (b) the npz/registry on disk, (c) the dedicated log. The registry SHA staying == dispatch-pin proved
   no partial landing across all the waiter timeouts.

4. **Two-surface landing, LF-only registry.** permanent-results-registry.md is LF-ONLY (0 CRLF) — both
   the master-index table AND the body. NO char-vs-byte CRLF trap (contrast S111 W1-5 where the table
   was CRLF). Two surfaces: (a) master-index TABLE ROW inserted immediately after the frontier row
   `| §VII.CJ | THM |` (keeps the sorted-frontier prefix CA→CJ→CK; the table breaks into an unsorted
   legacy tail AFTER the frontier — insert BEFORE that tail), (b) BODY section appended at EOF with a
   blank-line separator. verify_section_matches checks BOTH present + all markers, re-read from disk.

5. **VERIFY-THEOREM ⇒ NO 3-tuple** (the zero-identity is not a directional band). The plan said so;
   emit_verdict with no sign/magnitude/regime.

6. **Auditor disposition for an intra-pillar obstruction = `FAIL [legitimately-pending]`, NOT HARD-HALT.**
   `_cross_pillar_bridge_audit.py` reports "Missing anatomy: 1_substrate_IS_observable / Missing tiers:
   Level 2" but buckets it `legitimately-pending` — identical to §VII.BL (STAGE-3-PERMANENT MAGNITUDE
   companion) and §VII.BG/§VII.BK/§VII.AM. The 5-anatomy + 3-level ladder is MANDATORY only for
   CONVERGENCE bridges (substrate-IS→lab-IN HKR/K-theory); an obstruction theorem declares
   "5-anatomy N/A-with-reason" + "NON-BINDING Level-2" and clears. No in-session fix owed.

7. **Companion citation:** STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BV (SIGN axis) + §VII.BL (MAGNITUDE
   axis) on a THIRD γ₉/orientation axis; cross-observable co-primary FORBIDDEN (algebra-axis orthogonality
   K=3). NON-PROMOTION-BY-HELD-NUMBER, **sign-lock** differentia (held quantity is a sign-PATTERN, uniform
   sign forced — NOT dimensionful-slot-collision, NOT undischarged-magnitude-bound). Mirror §VII.BL's
   exact NON-BINDING-Level-2 / NON-PROMOTION framing (line 21117-21123).

8. **Runtime canonical SHA drift** (sibling S114 gate promoted a constant mid-session): plan-pinned
   `9ee1a113…` → runtime `a4b8b679…`. Captured RUNTIME state in the dual-SHA per
   substrate-first-canonical-sourcing.md §(ii.B); disclosed in convention/companion. Audit-correct,
   NOT a defect. Registry landing-target SHA pinned at dispatch (`1d113a6b…`, in the pinmap → audit_sha).

Links: [[register_sourced_gate_machinery_recovery]] (the companion case where the machinery is recovered
from a prior script); [[verbatim_extraction_registry_landing]] + [[joint_theorem_clause_formalization_landing]]
(the two-surface / single-shot AFTER-pattern landing recipes this extends).
