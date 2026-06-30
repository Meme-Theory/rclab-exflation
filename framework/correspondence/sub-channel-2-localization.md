# Mellin-Cone Live Infrastructure Sub-Channel-2 Localization Theorem

**Status**: NEEDS-DECISION (T10-28: standalone framework note vs annex to cutoff-sqrt-adjudication.md) → **STANDALONE NOTE INSTALLED** 2026-04-27 (S86 Level-10 housekeeping T10-28).
**Source**: S86 W-8 workshop `s86-cutoff-sqrt-gate-abc-trio.md` lines 1846-1880 (theorem) + lines 1985-1992 (Wrap-Up confirmation) + Verdict row 10 (line 1939).
**Recommending agent**: gen-physicist (extract); lizzi (R2-EM-2 originator).
**Cross-references**: `sessions/framework/registry/cutoff-sqrt-adjudication.md` (parent file; T10-27 install for §3.1/§3.2/§3.3 PASS/FAIL/INFO branches); `sessions/framework/registry/propagator-class-taxonomy.md` (T10-8 install; Class IV K-running falsifier signature); §VII.K-PROP 4-Channel-LAYER-2-Sub-Decomposition (S86 W-8 candidate registry entry).

This entry is the structural lemma supporting GATE A FAIL robustness in the S86 W-8 cutoff_sqrt adjudication. The theorem clarifies WHY the GATE A FAIL is robust against any S87+ infrastructure refinement: there is no architectural slot for the Mellin-cone live infrastructure (W2 C9/C10) to enter the s=0 a_0 anchor.

---

## §1 — Theorem statement

**Mellin-Cone Live Infrastructure Sub-Channel-2 Localization Theorem** (workshop §"Emerged" #10, lines 1939):

```
The S86 Mellin-cone live infrastructure (W2 C9/C10) plays a SUB-CHANNEL-2 role
under the §VII.K-PROP 4-channel framework. It refines n ≥ 1 Mellin residues
entering the Σ_n f_n a_n COUPLING product but does NOT enter:
  - GATE A (uses a_0 directly, not the n ≥ 1 sum)
  - GATE B (logical CCM-2007 axiom invocation, no Mellin sum)
  - GATE C (prescribed (f_0, f_2, f_4, f_6) Mellin vector + reconstruction)

Therefore the live infrastructure occupies channel-2 (coupling-routing) ONLY,
and no channel-1, channel-3, or channel-4 verdict is sensitive to its status.
```

---

## §2 — Substitution chain (workshop verbatim, lines 1853-1875)

```
Step 1 (def):    Mellin-cone live := for each spectral-action moment Σ f_n a_n,
                  evaluate f_n via residue-at-pole structure on the Mellin
                  contour, NOT via direct heat-kernel truncation.

Step 2 (sub):    GATE A uses a_0(L) directly (s=0 Mellin residue, integer-exact).
                  GATE B uses CCM-2007 axiom invocation (logical, not Mellin).
                  GATE C uses prescribed (f_0, f_2, f_4, f_6) Mellin vector
                  + 4-atom sum-of-exp inversion (NOT live Mellin-cone integration).

Step 3 (simp):   The Mellin-cone live infrastructure refines the n ≥ 1 Mellin
                  residues that enter the Σ_n f_n a_n COUPLING product. It
                  does NOT enter:
                  - GATE A (uses a_0 directly, not the n ≥ 1 sum)
                  - GATE B (logical axiom invocation, no Mellin sum)
                  - GATE C (prescribed Mellin vector + reconstruction)
                  Therefore it lives at channel-2 (coupling-routing) ONLY.

Step 4 (dir):    No channel-1, channel-3, or channel-4 verdict is sensitive
                  to the Mellin-cone live infrastructure status. Only channel-2's
                  Λ-rescaling absorption mechanism could (counterfactually) be
                  refined by it — and the Peter-Weyl L^8/960 leading is integer-
                  combinatorial, so the refinement would have to enter via
                  a different a_0(L) definition (which is precluded by the
                  R-protected Peter-Weyl identity).
```

---

## §3 — GATE A FAIL robustness consequence (workshop lines 1877-1880)

The localization theorem MEANS the GATE A FAIL is robust against any S87+ infrastructure refinement. There is no architectural slot for the live infrastructure to enter the `s = 0` `a_0` anchor:

```
GATE A FAIL anchor: α_star(L) ∈ [−1.5893, −1.0158] across L ∈ {3, 5, 7, 10};
                    α_star(40) = −1.8816 (first crossing of 7.5 in k_eff);
                    α_star → −2 from L^8/960 leading (Peter-Weyl integer-exact).

Mellin-cone live infrastructure (counterfactual refinement attempt):
                    Could ONLY enter via a different a_0(L) definition.
                    Precluded by the R-protected Peter-Weyl identity.

Direction:          GATE A FAIL is structurally robust against ANY infrastructure
                    refinement that does not violate the R-protected Peter-Weyl
                    identity. The cutoff_AL2010 atlas-cardinality cascade
                    A_5 → A_4 is locked by GATE A FAIL.
```

---

## §4 — Channel-by-channel sensitivity table

The 4-channel LAYER-2 sub-decomposition (S86 W-8 §VII.K-PROP candidate registry entry) provides the structural framework for the localization theorem. Each channel's sensitivity to the Mellin-cone live infrastructure is:

| Channel | Definition | Live-infrastructure sensitivity | Reason |
|:--------|:------------|:---------------------------------|:--------|
| **1 (axiom-sourcing)** | Verifies that a regulator's `a_0` is sourced from a CCM-2007 axiomatic prescription (e.g., GLOBAL-TRACE `Tr_H(1) / Vol_F` for cutoff_AL2010 PASS) | INSENSITIVE | Logical axiom invocation; no Mellin sum |
| **2 (coupling-routing)** | Verifies that the regulator's coupling vector `(f_0, f_2, f_4, f_6, ...)` produces bounded Σ_n f_n a_n at substrate pivot | SENSITIVE (sub-channel-2 ONLY) | Live infrastructure refines the n ≥ 1 Mellin residues entering Σ_n f_n a_n |
| **3 (functional-class)** | Verifies that the regulator's profile is HBW⁺-class or has a classified non-HBW⁺ sub-class (3a sign-change, 3b compact-support, 3c CM PASS, 3d Mellin-divergent, 3e Hamburger-violating) | INSENSITIVE | Prescribed Mellin vector + reconstruction; no live integration |
| **4 (anomaly-gauge)** | Verifies that the regulator's `f_0` matches anomaly-cancellation prescription | INSENSITIVE | Logical anomaly-cancellation axiom; no Mellin sum |

The localization theorem MEANS channel-2 is the ONLY architectural slot where the live infrastructure can produce verdict effects. Channels 1, 3, 4 are insensitive by construction.

---

## §5 — Counterfactual stress test (Peter-Weyl precluded)

The localization theorem includes an explicit counterfactual stress test: COULD the live infrastructure refine GATE A by entering through a different `a_0(L)` definition? The answer is NO, by the R-protected Peter-Weyl identity:

```
Definition 1: Peter-Weyl identity for SU(3) eigenvalue spectrum at L_max:
              N(L) = ∑_{(p,q): p+q ≤ L} dim_{(p,q)}^2
                   = L^8 / 960 + L^7 · O(1) + ... (leading + sub-leading)

Definition 2: a_0(L) = N(L) at s=0 Mellin residue (s=0 anchor)

Step 1 (sub):  R-protected Peter-Weyl identity: N(L) at leading order is
              determined by integer combinatorics of (p, q) Casimir tower;
              the L^8 / 960 coefficient is INTEGER-EXACT (not regulator-
              dependent).

Step 2 (sub):  Any "different a_0(L) definition" that the live infrastructure
              could refine would have to violate the R-protected Peter-Weyl
              identity.

Step 3 (deriv): The R-protected Peter-Weyl identity is structurally protected
              (ANISO-JOSEPHSON-63 PASS + S77 R-protection-universal claim).
              No NCG-compatible regulator can violate it without falsifying
              the substrate's S_3-subgroup structure.

Direction:    The counterfactual refinement attempt fails by R-protection.
              Live infrastructure cannot enter the s=0 a_0 anchor through any
              architectural slot.
```

This is why the GATE A FAIL is REGULATOR-CLASS-WIDE: any regulator whose `a_0` sourcing routes through GLOBAL-TRACE Peter-Weyl (which is ALL NCG-compatible regulators) inherits the FAIL.

---

## §6 — Carry-forward verification gate

The localization theorem is verified as a carry-forward gate at S87:

**`S87-MELLIN-CONE-LIVE-CHANNEL-2-LOCALIZATION-VERIFY`** (S87 carry-forward CF-51 in `_housekeeping-install-queue.md`; W-8 CF-5):

- **What**: dispatch a 4-channel test of Mellin-cone live infrastructure at each channel; verify infrastructure modifications affect ONLY channel-2 (coupling-routing) and produce no shifts at channel-1, 3, or 4. Specifically: re-run GATE A α-scan with `--mellin-cone-live` True/False; verify `k_eff_asymptotic` unchanged within machine epsilon (channel-1 invariance); re-run GATE C-style HBW probe with both settings; verify `M_6` unchanged within machine epsilon (channel-3 invariance).
- **Inputs**: `computations/s86_w8_gate_a_lmax_finiteness.py` (modified to accept `--mellin-cone-live` flag); W2 C9/C10 infrastructure module (`sessions/archive/session-86/session-86-w4-workingpaper.md` cite); §VII.K-PROP registry entry (S87 carry-forward CF-47 `S87-CUTOFF-SQRT-ATLAS-PROPAGATION`).
- **Gate**: PASS = channel-1, 3, 4 outcomes invariant under Mellin-cone live toggle (rel-shift < 1e-13); only channel-2 outcomes responsive. INFO = channel-2 responds + ≤ 1 other channel responds at < 1e-10. FAIL = > 1 channel responds at > 1e-10 (theorem disproved; §VII.K-PROP needs revision).
- **Effort**: ~4 hours; toggling existing scripts; no GPU.

---

## §7 — Cross-references

- **Parent file**: `sessions/framework/registry/cutoff-sqrt-adjudication.md` (T10-27 install records §3.1/§3.2/§3.3 GATE A/B/C PASS/FAIL/INFO branches with audit_sha256 / content_sha256 dual-SHA pins).
- **S86 W-8 workshop**: `sessions/archive/session-86/workshops/s86-cutoff-sqrt-gate-abc-trio.md` lines 1846-1880 (theorem); lines 1985-1992 (Wrap-Up confirmation); Verdict row 10 (line 1939).
- **§VII.K-PROP 4-Channel-LAYER-2-Sub-Decomposition** (S87 carry-forward landing): S87 carry-forward CF-47 (`S87-CUTOFF-SQRT-ATLAS-PROPAGATION`); landing at unique slot via append-only writer per `.claude/rules/epistemic-discipline.md` Registry-Write Hygiene.
- **§VII.M Three-Layer Regulator Theorem (S84 W2a-11)**: `sessions/permanent-results-registry.md` (Connes + Lizzi + VdD signature); composition with §VII.K-PROP produces L2-FULLY-ADMISSIBLE iff layer match + all 4 channels PASS.
- **R-protected Peter-Weyl identity**: `permanent-theorems.md`; structurally protected by ANISO-JOSEPHSON-63 PASS + S77 R-protection-universal claim.
- **Class IV K-running falsifier signature**: `sessions/framework/registry/propagator-class-taxonomy.md` §5 (T10-8 install) — the K-running shape `δα(K) / α_FW ~ w_optical(K) · structural_coefficient` IS a counterfactual stress test in the same family as this localization theorem (regulator-class transition under K-scaling).
- **Sub-channel-2 localization theorem carry-forward**: `S87-MELLIN-CONE-LIVE-CHANNEL-2-LOCALIZATION-VERIFY` (CF-51 in `_housekeeping-install-queue.md`); ~4 hours.
- **Mellin-cone live infrastructure (W2 C9/C10)**: `sessions/archive/session-86/session-86-w4-workingpaper.md` §P5 line ~470-490 + S85 W2-5 direct-heat-kernel-truncation fallback.
- **GATE A FAIL anchor SHAs**: `s86_gate_verdicts.txt` line 239 (canonical) + line 240 (companion row with `atlas_cardinality_after=A_4 structural_pre_determination=R3-C-E3-C`); audit_sha256 `a289004bff9ac728dd25f001cd65fc8df5fac2ac146897185f1b6ceeb569d270`; content_sha256 `8ef1bc07c8c2ecba6c2fdba349856d606dea6526fe63e6b319d4fb2a0282d260`.

---

## §8 — Closing

The Mellin-cone live infrastructure sub-channel-2 localization theorem is the structural lemma supporting GATE A FAIL robustness in the S86 W-8 cutoff_sqrt adjudication. It establishes that the live infrastructure (W2 C9/C10) has NO architectural slot to enter the GATE A FAIL via channel-1, channel-3, or channel-4; it occupies channel-2 (coupling-routing) ONLY. The counterfactual stress test (live infrastructure refining `a_0(L)` to escape FAIL) fails by the R-protected Peter-Weyl identity. The atlas-cardinality cascade A_5 → A_4 is therefore LOCKED at S86 W-8 close, and the localization theorem is a forward-looking sanity check verified at S87 carry-forward `S87-MELLIN-CONE-LIVE-CHANNEL-2-LOCALIZATION-VERIFY` (CF-51).
