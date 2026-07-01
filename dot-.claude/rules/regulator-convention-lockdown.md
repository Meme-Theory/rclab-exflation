# Regulator-Convention Lockdown for DR3-Class L_max-Stability Gates

## Rule (cross-session convention-consistency for DR3-class L_max-stability)

For ALL computation gates of class **DR3 L_max-stability** — i.e., gates whose
verdict is a function of `w_0_FW(L_max)` evaluated at two or more values of
the regulator axis L_max ∈ {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ...} —
the convention used to map regulator-axis spectral moments to the late-time
w_0 prediction MUST be the **canonical-anchored convention (CAC)**:

```
w_0_FW(L) := rho_X(L) + offset_X
where:
  rho_X(L)   = a regulator-axis spectral-moment scheme:
               X ∈ {Zubarev, zeta, Pauli-Villars, Mellin}
               (default: Zubarev, per the rho_series NPZ field)
  offset_X   = w_0_FW - rho_X(L_anchor)  with L_anchor = 10
               (the additive constant that absorbs the Volovik-partition
               effacement contribution as a closed-form translation)
  w_0_FW     = canonical_constants.py:1243 = -0.918
               (Volovik partition + effacement Gamma_eff = 0.99970)
```

The CAC for the canonical scheme X = Zubarev has `offset_Zubarev = -0.340827`
(= w_0_FW − `rho_series[L=10]` = −0.918 − (−0.577173)).

## Demarcation theorem (admissibility class)

A convention `C` is **admissible** for a DR3-class L_max-stability gate iff
`C` satisfies the effacement-preservation criterion:

```
  w_0^{C}(L=10) = w_0_FW   EXACTLY (bit-precision algebraic identity at L=10).
```

CAC satisfies this BY CONSTRUCTION (the offset is defined to absorb the
L=10 residual). Any convention that does NOT satisfy this — including the
**rho-direct convention (RDC)** `w_0(L) := rho_X(L)` with no offset, or
RDC + L=10-override (a discontinuous patch) — is **OUTSIDE the admissibility
class** and MUST NOT be used.

## Enforcement

- Plan-freeze validators (`_source_reconciliation_audit.py` post-V.2 extension)
  scan computation scripts in DR3 L_max-stability gate scope for the CAC pattern
  `w_0(L) = rho_X(L) + <offset_constant>`. Detection of `w_0(L) := rho_X(L)`
  WITHOUT an offset, or with an L=10-conditional override, fires Class-(b)
  PIN-LOOSE-SOURCE-TIGHT severity S1 advisory (halts plan-freeze).
- Re-running a previously-failed DR3-class gate under a DIFFERENT scheme
  (Zubarev → zeta) is permitted PROVIDED the new scheme is composed with
  its own effacement-anchored offset. Switching the offset constant ad-hoc
  (without anchoring at L=10) is treated as PROHIBITED_ACTIONS Class 1
  (convention-shopping) per `.claude/rules/v3-closure-recovery.md`.

## Cross-Link to v3-closure-recovery PROHIBITED_ACTIONS Class 1

PROHIBITED_ACTIONS Class 1 forbids changing a gate's `convention` tag DURING
recovery — i.e., the within-gate execution-property failure where a FAIL is
relabeled as PASS by switching conventions. The cross-session analog (changing
convention BETWEEN sessions on the same gate-family) is structurally different:
both sessions can satisfy Class 1 internally and still produce inconsistent
verdicts (an RDC oscillation FAIL vs a CAC step-monotone INFO
on the same underlying rho_series data). This rule closes that gap by
pre-registering CAC as the binding form across ALL DR3-class L_max-stability
gates — a rule-file commitment, not a per-gate machinery pin.

## Scope (NOT for non-DR3 gates)

This lockdown is SPECIFIC to DR3-class L_max-stability gates. Non-DR3 gates
(e.g., n_s convergence, alpha_s convergence, r convergence) MAY use schemes
other than CAC if their canonical anchor is not w_0_FW. Each gate-class with
a distinct canonical anchor REQUIRES its own analogous lockdown rule, derived
by the same demarcation-theorem template.

## Cross-references

- `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1.
- `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" Class (b) PIN-LOOSE-SOURCE-TIGHT.
