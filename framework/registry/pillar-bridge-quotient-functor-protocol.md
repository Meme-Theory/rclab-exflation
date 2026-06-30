# Pillar-Bridge Quotient-Functor Protocol Pre-Registration

**Status**: NEEDS-DECISION (UD pending: rule-vs-protocol location for the universality claim) → **PROTOCOL DOCUMENT INSTALLED** 2026-04-27 (S86 Level-10 housekeeping T10-22).
**Source**: S86 W-6 workshop `_housekeeping-extract-w6.md` OFW-1 (lines 188-192) + REG-3 (lines 27-30) + RULE-1 (lines 48-52) + workshop §E-V-R3-2 lines 2079-2112 + Wrap-Up §"What Breaks or Strains" line 2244.
**Recommending agent**: gen-physicist (extract); lizzi + volovik (workshop sponsors).
**Cross-references**: T7 ↔ S67 PASS-quotient-isomorphism (workshop S86 W-6); CF-LZ-VV-S86-CYCLIC-FOLD-MELLIN-SPECTROSCOPY (REG-1 of S86 W-6); §VII.M Three-Layer Regulator Theorem (S84 W2a-11); `sessions/framework/correspondence/correspondence-table-registry.md` (T6 ↔ T7 ↔ S67 three-wall correspondence).

This entry is the pre-registration discipline for cross-pillar bridge candidates connecting an ∞-dim spectral-action wall (Pillar-VII) and a finite-rank obstruction wall (Pillar-V or analogous). The protocol mandates that any such bridge MUST be declared as a quotient-functor lift, NOT a full-functor isomorphism — by the dimensional-impossibility necessity of `∞ ↔ finite`.

---

## §1 — Universality claim (REG-3 statement)

**Pillar-Bridge Quotient-Functor Universality Claim**:

```
For all candidate bridge theorems connecting an ∞-dim spectral-action wall (Pillar-VII) and a
finite-rank obstruction wall (Pillar-V or analogous), the bridge REQUIRES a quotient-functor lift
by ∞-dim ↔ finite-rank dimensional-impossibility necessity. Faithful (full-functor) lift is
impossible by ∞ ↔ finite; quotient-functor lift through cyclic-fold (or its analog for the
specific bridge) is necessary.
```

**Methodological consequence**: pre-registration discipline must declare the quotient relation, verify the rank match at the quotient level, and accept residual cokernel content as quotient-killed.

**Universality status** (per workshop Wrap-Up line 2244): the claim is registered as a UNIVERSAL CLAIM but the universality remains a GENERALIZATION CLAIM rather than a proven theorem. Promotion to theorem requires `S87-CYCLIC-FOLD-CLASS-SURVEY` (W-6 CF-39, QUATERNARY) producing 1+ additional confirming instances beyond T7 ↔ S67. Until then, the universality is a CONJECTURE-WITH-ONE-CONFIRMING-INSTANCE.

---

## §2 — Pre-registration discipline (RULE-1 specification)

When a candidate bridge theorem connects an ∞-dim spectral-action wall (Pillar-VII) and a finite-rank obstruction wall (Pillar-V or analogous), the plan MUST pre-register the quotient relation under which the bridge is claimed. Required fields:

### (a) Quotient-equivalence specification

Specify the quotient relation under which the ∞-dim and finite-rank objects are claimed equivalent. Examples:
- **Cyclic-fold quotient**: `N`-conjunct categorical structure → `N/2`-axes via folding. The T7 ↔ S67 bridge uses cyclic-fold pairing on N-conjunct categorical structure (REG-1 of S86 W-6).
- **Group-theoretic quotient**: `G/H` for some group `G` acting on the ∞-dim object, with `H` the stabilizer projecting to the finite-rank target.
- **Topological quotient**: `X/∼` for some equivalence relation `∼` collapsing ∞-dim fibers to finite-dim points.

### (b) Rank-match check at the quotient level

Verify that the kernel/cokernel at the quotient level matches the finite-rank Pillar-V observable. Format:

```
Definition 1: Q : (∞-dim spectral-action wall) → (∞-dim spectral-action wall / quotient_relation)
Definition 2: ι : (Pillar-V finite-rank wall) → (∞-dim spectral-action wall / quotient_relation)
Definition 3: ker(Q ∘ ι) = (Pillar-V finite-rank object) by quotient-kernel match
Definition 4: coker(Q) = (residual cokernel content) — must be DECLARED as quotient-killed
```

The rank-match check produces a numerical residual at the quotient level (e.g., `0.0095%` for T7 ↔ S67 PASS-quotient-isomorphism).

### (c) Residual cokernel declaration

Explicitly declare the residual cokernel content killed by the quotient. The bridge theorem cannot be promoted to a full-isomorphism claim if the cokernel is non-empty; instead, the claim is a PASS-QUOTIENT-ISOMORPHISM:

```
Bridge claim: T_∞ ≅_{quotient} T_finite     [PASS-QUOTIENT-ISOMORPHISM]
```

NOT:

```
Bridge claim: T_∞ ≅ T_finite                [PASS-FULL-ISOMORPHISM, forbidden by ∞ ↔ finite]
```

### Plan-freeze validation

Bridges declared as full-functor isomorphisms when an ∞-dim ↔ finite-rank disparity exists are dimensional-impossibility-violating and must be re-classified as quotient-functor or REJECTED at plan-freeze. The `_source_reconciliation_audit.py` (or analog plan-freeze validator) must check the bridge claim's quotient-relation field is non-empty AND the cokernel is explicitly declared.

---

## §3 — Calibration corpus (one confirming instance: T7 ↔ S67)

The single confirming instance at S86 close is the T7 ↔ S67 PASS-quotient-isomorphism (workshop S86 W-6). Substitution chain (verbatim from workshop §"Wrap-Up" lines 2192-2203):

```
Definition 1: T7 = Two-Layer Obstruction (Pillar-VII spectral-action wall, §VII-B; ∞-dim)
Definition 2: S67 = Frustration Triangle (`proven_1738`; Pillar-V finite-rank obstruction wall;
              S_3 fundamental cell with n_frust ∈ {0, 2}; Z_3 cyclic gauge sector)
Definition 3: cyclic-fold quotient Q maps N-conjunct categorical structure → N/2-axes
Definition 4: ι : S67 → T7/Q via Mellin-residue / heat-kernel-column duality (registry §VII.T)
              + sub-cluster near-identity lifts (F_4 OR M sub-cluster Wick-induced a_0 vanishing)

Step 1 (sub):  HP^1 norm magnitude of regulator-class cluster:
               ‖[ε_H]‖_{HP^1}(cluster) ≈ k_link(cluster) × (1 − δ_pull-back(cluster))
               where k_link = 3 (triangular F_4 tile) or 6 (hexagonal M tile)
               and δ_pull-back = δ_SDW = 0.029976 for F_4 (SDW wavelet truncation)
                                 ≈ 0 for M (hexagonal extension)
Step 2 (sub):  r_HP1_predicted = k_link_M / k_link_F4 × (1 − δ_SDW)
                              = 6/3 × (1 − 0.029976)
                              = 2 × 0.970024
                              = 1.940048
Step 3 (sub):  r_HP1_observed = 2.0 / 1.031 = 1.939864 (S86 W1b T6 LOOSE/STRICT)
Step 4 (sub):  residual = |1.939864 − 1.940048| / 1.939864 = 0.000184 / 1.939864
                       = 0.00948% (Python-verified; below 0.05% threshold; 50× tighter)
Direction:    PASS-QUOTIENT-ISOMORPHISM at residual 0.0095%. Cokernel declaration:
              cyclic-fold collapses 6-link hexagonal → 3-link triangular for amplitude;
              residual cokernel content is the cross-cluster gap (D-L-R3-1) which is
              quotient-killed. Bridge cannot be promoted to full-isomorphism because
              the cross-cluster gap is structurally explicit.
```

The T7 ↔ S67 instance demonstrates the protocol's three required fields (quotient-equivalence specification, rank-match check, residual cokernel declaration) all hold simultaneously. This is the calibration corpus for plan-freeze validation: future bridge candidates' pre-registration must show the same three-field structure.

---

## §4 — Application to alpha-s structural-protection (cross-reference)

The protocol applies to the α_s structural-protection bridge between the ∞-dim spectral-action wall (Pillar-VII C1 identity `α_s = n_s² − 1`) and the finite-rank substrate-physical anchor wall (Pillar-V triple-anchor: BDI universality + kinematic suppression + sub-threshold inter-band coupling).

| Field | T7 ↔ S67 (CALIBRATION) | α_s triple-anchor (CROSS-REFERENCE) |
|:------|:------------------------|:-------------------------------------|
| Quotient-equivalence specification | cyclic-fold pairing on N-conjunct categorical structure | single-effective-pole equivalence class on K-homogeneity ODE family |
| Rank-match check (residual) | 0.0095% (Python-verified) | residue ~ 1.9 × 10⁻⁹ absolute (Class IV); ~ 8.65 × 10⁻⁵ absolute (Class V dominant); both << CMB-HD precision |
| Residual cokernel declaration | cross-cluster gap (D-L-R3-1) quotient-killed | independent multi-pole sector with distinct (J_i, m_i²) — Class IV — sub-detector-precision leakage |

The α_s structural-protection registry entry (`sessions/framework/registry/alpha-s-structural-protection.md` T10-4) is therefore a SECOND CONFIRMING INSTANCE of the universality claim, supporting (but NOT closing) the universality claim's promotion-to-theorem path.

---

## §5 — Forward-looking template (per W-6 CF-5)

For any future cross-pillar bridge candidate (Pillar I ↔ Pillar II; substrate ↔ cosmology measurement; BdG-spectral-triple ↔ 3He-B observable), the candidate's pre-registration MUST include all five IS-not-IN anatomy elements AND verify all three levels cohere:

1. **Substrate-IS observable** (∞-dim spectral-action object)
2. **Laboratory-IN observable** (finite-rank measurement target)
3. **Bridge map** (the quotient functor Q + injection ι)
4. **Algebraic envelope** (substrate-derived predicted lab-conversion factors)
5. **Empirical anchor** (one prior measurement or pre-registered measurement establishing the rank-match check residual)

**three-level ladder coherence**: level 1 (axiomatic; e.g., NCG axiom-level chain), level 2 (Mellin-level; e.g., spectral-action moment expansion), level 3 (detector-level; e.g., lab-platform measurement). All three levels must cohere for the bridge candidate to be registered.

The template is forward-looking; zero S87 effort. Any future bridge candidate dispatch must pre-register through this template.

---

## §6 — Lab-projection asymmetry (OFW-2 cross-reference)

The PASS-quotient-isomorphism between Pillar-VII (spectral-action) and Pillar-V (superfluid-array) walls is verified at the F_4 sub-projection in BOTH substrate AND lab; the M sub-projection is verified in substrate ONLY (BdG restriction projects out hexagonal-tiling content with `d_spec ≥ 2`). Full cross-cluster bridge testability requires a 2-component-superconductor lab realization (FeSe-like multiband or triplet-coupled bilayer) that lifts BdG restriction.

This is the lab-projection asymmetry framing for cross-cluster bridges (W-6 OFW-2). It is captured in the W-6 install of `framework-3heb-comparison.md` (T10-23).

---

## §7 — Bridge-registry rows (current + queued)

| Bridge | Pillar pair | Quotient operator | Residual | Status | Registry slot |
|:--------|:-------------|:-------------------|:----------|:--------|:---------------|
| **T7 ↔ S67** | VII (T7 Two-Layer Obstruction) ↔ V (S67 Frustration Triangle) | cyclic-fold quotient on N-conjunct categorical structure | 0.0095% (Python-verified) | PASS-QUOTIENT-ISOMORPHISM (LOCKED at S86 W-6) | §VII-X (S87 carry-forward CF-36 `S87-T7-S67-ISOMORPHISM-LANDING`) |
| **α_s C1 ↔ triple-anchor** | VII (α_s = n_s² − 1 single-pole identity) ↔ V (BDI universality + kinematic suppression + sub-threshold inter-band coupling) | single-effective-pole equivalence class | residue ~ 1.9 × 10⁻⁹ Class IV; ~ 8.65 × 10⁻⁵ Class V | PASS-QUOTIENT-ISOMORPHISM (LOCKED at S86 W-2) | `sessions/framework/registry/alpha-s-structural-protection.md` (T10-4) |
| **§VII-Y** | TBD | TBD | TBD | candidate slot for `S87-CYCLIC-FOLD-CLASS-SURVEY` survey output | §VII-Y (S87 carry-forward CF-39, QUATERNARY) |

The bridge-registry tracks current confirming instances (2) and queued candidates (1). Promotion of REG-3 universality claim to theorem requires `S87-CYCLIC-FOLD-CLASS-SURVEY` producing additional confirming instances.

---

## §8 — Cross-references

- **T7 ↔ S67 PASS-quotient-isomorphism** (REG-1 of S86 W-6): workshop `s86-two-layer-obstruction-s67-frustration.md`; primary S87 gate `S87-T7-S67-ISOMORPHISM-LANDING` (CF-36 in `_housekeeping-install-queue.md`).
- **α_s structural-protection registry entry** (second confirming instance): `sessions/framework/registry/alpha-s-structural-protection.md` (T10-4).
- **§VII.M Three-Layer Regulator Theorem (S84 W2a-11)**: `sessions/permanent-results-registry.md` (Connes + Lizzi + VdD signature); regulator-class layer membership (L1 zeta ↔ Path-H, L3 per-Q span ↔ Path-C, L2 Zubarev ↔ singleton).
- **Cyclic-fold operator**: workshop §C-V-R3-1 + §E-V-R3-3 + §E-L-R3-1; substrate's natural symmetry under which T6 (HP^1 Near-Invariance, AMPLITUDE face), T7 (Two-Layer Obstruction, COUNT face), and S67 (Frustration Triangle, HALF-QUANTUM face) are co-variant readouts of a single dual-hex Josephson-array plaquette-cycle structure.
- **`framework-3heb-comparison.md` lab-projection asymmetry framing** (OFW-2 of S86 W-6): T10-23 install.
- **3-wall correspondence** (T6 ↔ T7 ↔ S67): `sessions/framework/correspondence/correspondence-table-registry.md` CORR-1 (T10-7 install via parallel agent).
- **Connes-Chamseddine A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) ↔ three-edge-class triangular Josephson array** (CORR-3 of S86 W-6): forced-solution-class by 4-constraint intersection; weight-match `m_M_3 / m_ℍ = 243/16 = 15.1875` is STRUCTURAL forward gate to S87 (`S87-V2-WEIGHT-MATCH-FORWARD-GATE`, CF-37); FAIL is real possibility per D-V-R3-1 algebraic inconsistency.
- **`S87-CYCLIC-FOLD-CLASS-SURVEY`** (W-6 CF-39, QUATERNARY): forward-looking survey for additional confirming instances.
- **CF-5 forward-looking template** (W-6 R2-A Q-CN-1 Q7): five IS-not-IN anatomy elements + three-level ladder coherence (axiomatic / Mellin-level / detector-level).
- **Half-structural cyclic fold framing** (MEM-4 of S86 W-6): cyclic fold N-axes → N/2-axes is HALF-STRUCTURAL when one pair (typically Mellin-residue / heat-kernel-column duality) is forced by analytic structure but the remaining pairs are causal links or sub-cluster-restricted near-identities.

---

## §9 — Open user decisions (BLOCKERS)

- **UD pending** (between RULE-1 and OFW-1 location): the universality claim's CANONICAL location — is it (a) `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" extension (RULE-1; rule-file location); or (b) `sessions/framework/registry/pillar-bridge-quotient-functor-protocol.md` (OFW-1; this file; framework-level protocol document)? Plan-author choice affects whether the protocol is enforced as a plan-freeze validator (rule) or a documentation reference (framework).

This file is the OFW-1 location (option b). If UD chooses option a, this file's content is migrated to the rule file and this file is closed; the cross-references above point to the rule file location.

---

## §10 — Closing

The pillar-bridge quotient-functor protocol pre-registration discipline mandates that any candidate bridge connecting an ∞-dim spectral-action wall (Pillar-VII) and a finite-rank obstruction wall (Pillar-V or analogous) MUST declare its quotient relation, verify the rank match at the quotient level, and accept residual cokernel content as quotient-killed. Full-functor isomorphism claims are dimensional-impossibility-violating by `∞ ↔ finite` and rejected at plan-freeze. The protocol has ONE confirming instance at S86 close (T7 ↔ S67 PASS-QUOTIENT-ISOMORPHISM at residual 0.0095%); the α_s structural-protection registry entry (T10-4) is a second confirming instance. Promotion of the universality claim to theorem requires `S87-CYCLIC-FOLD-CLASS-SURVEY` (W-6 CF-39) producing additional confirming instances.
