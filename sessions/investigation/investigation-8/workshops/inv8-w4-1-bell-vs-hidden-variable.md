# INV8-W4-1 — Bell-vs-Hidden-Variable: What the GGE IS

**Gate**: `INV8-W4-1` | **Type**: workshop (EXACTLY 2 agents, 2 rounds, sequential turns) | **Closure**: artifact-existence-with-content (NO verdict line — investigation-track workshop per `gate-verdicts.md §"Investigation-Track Canonical Path"`).
**Participants**: `einstein-theorist` (Reading A) ↔ `kitaev-quantum-chaos-theorist` (Reading B). **Neutral spec author**: `gen-physicist` (NOT a participant).
**Plan**: `sessions/investigation/investigation-8/investigation-8-plan-w4.md §W4-1`.

**Adjudication question**: What does the GGE IS — and which of its substrate quantities are classical (a hidden/thermodynamic layer) versus irreducibly quantum (an entanglement layer)? The flat contradiction: the S58 substrate-measurement addendum reads the GGE as a hidden-variable / superdeterministic account (QM emergent from a deterministic substrate, 't Hooft / Volovik adjacent), but S70 BELL-GGE-70 shows the GGE pairs violate CHSH across 8/8 modes (S up to 2.452 > 2), and by Bell's theorem a CHSH-violating system is NOT a local-hidden-variable account.

- **Reading A (einstein)** — the M2 split reconciles them: the GGE's THERMODYNAMIC content (8 mode-effective temperatures {T_k=ω_k/β_k}, D_JS=0.024 — an algebra-INVARIANT spectrum-only family) is the would-be hidden layer; the inter-mode CHSH-violating ENTANGLEMENT (algebra-DEPENDENT state-pair functional) is irreducibly quantum. The substrate is a non-local *quantum* theory whose non-locality is geometric (one fabric), not deterministic-with-QM-bolted-on.
- **Reading B (kitaev, S70 author)** — the GGE IS quantum; the Horodecki two-qubit CHSH (S70) supersedes the S69 bosonic-homodyne FAIL; the partition is integrability-vs-chaos (bounded-Krylov→permanent/Leggett vs linear-Krylov→thermalize; λ_L=0, S104), not temperature-vs-entanglement.

**Substrate-IS framing** (`phononic-framing.md`): the GGE IS the post-transit excitation spectrum of the fabric — 8 Richardson-Gaudin quasiparticle-pair modes, ρ_GGE = Z⁻¹ exp(−Σ_k λ_k R_k). Adjudication is about the INTERNAL structure of ONE substrate object, read two ways. Verdict is OPEN; the resolution is DERIVED (named decomposition or named obstruction), not agreement-counted.

**Sources** (read-only; advocates cite, do not recompute): S58 addendum §II (superdeterminism); S70 WP §W1-F (BELL-GGE-70, S=2.452); s70/s69 bell scripts; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (M2, K=3 MANDATORY); S64 WP (8 mode temperatures, S_GGE=2.2125); inv-1 einstein (C-1/B-4/G-3) + phonon-first (B-6 Krylov context); cross-ref INV8-W2-3 (Born-rule INFO: Gleason consistency-only).

---

## Round 1 — Steelman own reading

### R1 · Turn A — einstein-theorist (Reading A: M2 thermodynamic ⊥ entanglement)

**Position staked.** The S58↔S70 contradiction is not a contradiction. It is a *category error in the reading*, not in the substrate. The two sources speak about two structurally orthogonal families of observables on the SAME object ρ_GGE = Z⁻¹ exp(−Σ_k λ_k R_k), and the framework already possesses the algebra (M2, K=3 MANDATORY) that separates them. S58 §II read the GGE as a hidden-variable / superdeterministic account; S70 BELL-GGE-70 showed the GGE pairs violate CHSH (8/8 modes, min S=2.351, max S=2.452). Both are correct *about different observables*. The resolution is the **M2 cleave**: the GGE's thermodynamic content is an **algebra-INVARIANT spectrum-only functional family** (the would-be classical layer), and the inter-mode CHSH-violating entanglement is an **algebra-DEPENDENT state-pair functional** (irreducibly quantum). The substrate is therefore a *non-local quantum* theory whose non-locality is geometric — one fabric — not a deterministic theory with QM bolted on.

I argue this as a principle-theorist: I will not assemble a model and check it. I will identify the deepest invariance the two families respect, derive the partition from it, and show that the partition is *forced* — that no choice of dynamics can move an observable from one family to the other. That is the elevator move: before computing the bubble, find the symmetry that fixes which side of the wall an observable lives on.

---

**1. The principle: the M2 algebra-axis is a conserved structural label, not a modeling convenience.**

The M2 discipline (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`, MANDATORY at K=3) is a *structural theorem*, not a registry heuristic: on any finite spectral triple (A, H, D) satisfying the 7 NCG axioms, two functional families are STRUCTURALLY ORTHOGONAL in identity-class membership:

- **algebra-INVARIANT (spectrum-only)**: `F({λ_k, m_k}) = Σ_k m_k g(λ_k)` — depends only on the eigenvalue multiset of D_K. It cannot see the algebra A; it is invariant under any unitary that preserves the spectrum.
- **algebra-DEPENDENT (state-pair)**: functionals on A itself — Connes distances, occupation *coherences*, off-diagonal correlators between modes. These require the algebra structure; a spectrum-preserving unitary that reshuffles A *moves* them.

This is the same trace-invariance principle I have used elsewhere (the registered theorem S[UDU†] = S[D]: the spectral action is invariant under A-conjugation, so spectrum-only functionals are A-blind). The partition is a *selection rule*. An observable's family-membership is a conserved label under the substrate's own symmetry group, exactly as a particle's center-character is conserved under SU(3). You cannot continuously deform a spectrum-only functional into a state-pair functional any more than you can deform a triality-0 rep into a triality-1 rep. (The single-observable-per-triple filter of the M2 corpus makes this precise: a slot-split requires a DISCONTINUOUS jump in observable identity; continuous deformation forbids it.)

**Now place the two contested quantities on this axis — explicitly, with the substitution chain.**

*The thermodynamic content is algebra-INVARIANT.* The 8 mode-effective temperatures are {T_k = ω_k/β_k}, with the GGE labelled by ρ_GGE = Z⁻¹ exp(−Σ_k β_k R_k). Substitution chain:

```
Step 1 (def):  β_k is fixed by the constraint Tr(ρ_GGE R_k) = ⟨R_k⟩_DE  (diagonal-ensemble occupation; 8 Lagrange multipliers).
Step 2 (def):  R_k are the 8 Richardson–Gaudin integrals — mutually-commuting quasiparticle-NUMBER operators ([R_j, R_k] = 0).
Step 3 (sub):  ρ_GGE is therefore DIAGONAL in the simultaneous R-eigenbasis ⇒ ρ_GGE = ⊕_k diag(...)  (block-product over modes).
Step 4 (simplify):  T_k, β_k, S_GGE = −Tr(ρ ln ρ) = Σ_{k=1}^{8} S_k, the partition function Z, D_JS, the energy fractions — every one is a function of the OCCUPATION SPECTRUM {n_k} = {v_k²} alone.
Step 5 (direction):  a spectrum-only functional Σ_k m_k g(λ_k); A-blind ⇒ algebra-INVARIANT (M2 corner: spectrum-only).
Conclusion:  the thermodynamic layer {T_k}, S_GGE=2.2125, D_JS=0.024 is the algebra-INVARIANT family.
```

This matches the framework's own canonical numbers: S64 GGE-TEMP-43 gives T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178 M_KK (the 4.3:1 hot-to-cold ratio of S58 §II), with a *negative cross-temperature* T(B2,B1) = −0.066 M_KK, and the non-thermality measured as D_JS = 0.024 against the best-fit single-temperature Fermi–Dirac (S58 §II). Critically — and this is the move S58 §II already half-made — S64 itself proved this layer is **state-blind in the precise M2 sense**: the negative cross-temperature and the 8-fluid decomposition enter the Jacobson derivation ONLY through T_ab^{GGE} (a single contracted number on the RHS of the field equations), and the derivation uses the *Unruh* temperature T_U = ℏa/2π, a KINEMATIC single-valued quantity, *never* the matter T_k (S64 WP §I-II, my MEMORY.md permanent lesson: NEVER confuse T_Unruh with T_GGE). The thermodynamic family is exactly the layer that a coarse-grained, sub-KK observer can carry without seeing the algebra. It IS the would-be hidden/classical layer of S58 §II — and S58 §II's own phrase for it, "the temperature hierarchy as quantum indeterminacy" (§II), is precisely the claim that the *spectrum-only* content is what a coarse-grainer mistakes for noise.

*The CHSH-violating entanglement is algebra-DEPENDENT.* S70 BELL-GGE-70 computes the Horodecki two-qubit CHSH for each pair (k,−k): the BCS pair is |ψ_k⟩ = u_k|0,0⟩ + v_k|1,1⟩, a genuine 2-qubit state with concurrence C_k = 2|u_k||v_k|, and S_max = 2√(1+C_k²) > 2 whenever C_k > 0. Substitution chain for the family-membership:

```
Step 1 (def):  S_max(k) = 2√(1+C_k²), C_k = 2|u_k||v_k| (concurrence — Horodecki 1995).
Step 2 (def):  C_k is the modulus of the ANOMALOUS correlator ⟨c_k c_{−k}⟩ = u_k v_k — an OFF-DIAGONAL element of the two-mode density operator in the pairing basis.
Step 3 (sub):  ⟨c_k c_{−k}⟩ is a state-pair functional on A (it pairs the algebra element c_k c_{−k} against the state ρ); it is NOT a function of the eigenvalue multiset {λ_k} alone — two states with identical occupation spectra {n_k} but different relative phases give the SAME {T_k} and DIFFERENT C_k.
Step 4 (simplify):  C_k responds to A-conjugation that preserves the spectrum (the off-diagonal block transforms); the diagonal {n_k} does not.
Step 5 (direction):  algebra-DEPENDENT state-pair functional (M2 corner: state-pair). DISTINCT corner from the thermodynamic family by the orthogonality theorem.
Conclusion:  CHSH violation lives on the algebra-DEPENDENT axis. It is the irreducibly-quantum layer.
```

The two families occupy DISTINCT M2 corners. By the orthogonality theorem they cannot be the same observable, and no dynamics moves a quantity across the cleave. **That is the whole reconciliation, derived from one principle**: S58 §II's "hidden variable" lives in the spectrum-only corner; S70's Bell-violation lives in the state-pair corner; they are about different observables of the same ρ_GGE, so a Bell-violation on the second does not falsify a hidden-variable *reading* of the first — it falsifies only the *claim that the first exhausts the substrate*. The substrate is quantum because the state-pair corner is occupied and Bell-violating; it has a classical-looking thermodynamic shadow because the spectrum-only corner is what survives coarse-graining.

---

**2. The independent confirmation already on the books: INV8-W2-3 is the SAME cleave, computed.**

This is the decisive point, and it is not my construction — it is a landed result (INV8-W2-3, INFO, `audit_sha256=1d97...42df`). The Born-rule no-go found that the GGE coarse-graining reproduces |ψ_i|² **EXACTLY in the R-eigenbasis** (max_dev = 0 over all 8 modes) but FAILS off it: the paired marginal is MIXED (purity_B2 = 0.7731 < 1, purity_B3 = 0.9843), and the misaligned-basis gap is 0.337 ≫ 1e-6. The reusable lesson recorded there: *the eigenbasis coincidence is trivial alignment; the off-eigenbasis gap (∝ 1−purity) is the real test.*

Read this through M2 and it is *exactly* my partition, with numbers:

- The **eigenbasis-diagonal** content — what the thermodynamic trace reproduces perfectly — is the algebra-INVARIANT spectrum-only family. (The marginal eigenvalues ARE the squared amplitudes IN the eigenbasis, forced by construction; this is the {n_k}={v_k²} occupation data the {T_k} are built from.)
- The **off-eigenbasis** content — the mixed_basis_gap = 0.337 the trace canNOT reproduce — is the algebra-DEPENDENT state-pair family. It is the same off-diagonal anomalous-correlator content C_k that carries the CHSH violation.

INV8-W2-3 says it itself, verbatim: *"Consistent with INV8-W4-1 M2 split: the off-eigenbasis (entanglement) content is exactly what the thermodynamic trace cannot derive."* So the M2 cleave is not a hopeful reinterpretation laid over the contradiction — it is a *measured* structural fact: the thermodynamic trace lands the diagonal exactly and misses the off-diagonal by 0.337, and the off-diagonal is precisely the entanglement S70 detects. The partition has independent computational support on a DIFFERENT observable (Born-rule marginal) than the one that motivated it (CHSH). That is the strongest kind of confirmation a principle can have: it predicts the location of a gap before you look, and the gap is there.

---

**3. Sub-question (a): the Bell-violation does NOT falsify S58; it reconciles via the M2 split — and pins which quantities land where.**

S58 §II's actual structural claim (read it precisely, §II ¶"In the language of hidden-variable theories"): "the GGE IS the hidden variable" — the 8 Richardson–Gaudin integrals are "a complete specification of the substrate state." Note the integrals are *occupation* operators — the {R_k} are exactly the spectrum-only data. S58 §II then evades Bell NOT by a local-hidden-variable claim but by a **common-cause / superdeterminism** argument: both the "hidden variable" (GGE) and the "apparatus" (also phonons on the same fabric) are excitations of ONE medium, so Bell's measurement-independence assumption is not guaranteed (§II ¶"The phonon framework evades the theorem through a structural feature").

Here is the sharpening M2 forces. S58 §II conflated two things under the single word "GGE":
1. the **8 RG integrals {R_k}** — occupation/number data — which ARE a complete specification *of the spectrum-only sector*; and
2. the **full state ρ_GGE** including its off-diagonal anomalous correlators — which the {R_k} do NOT specify (mixed marginal, purity < 1, per INV8-W2-3).

The {R_k} are a complete hidden-variable specification of the *thermodynamic shadow* and an INCOMPLETE specification of the *quantum state*. This is precisely an EPR-completeness verdict, and it is the verdict I am professionally obligated to deliver: by the reality criterion, the off-diagonal coherence C_k can be predicted (it has a definite value u_k v_k) — it is an element of physical reality — yet it has NO counterpart among the {R_k}. **The {R_k}-as-complete-hidden-variable description is INCOMPLETE, not wrong.** S58 §II's superdeterminism is a correct account of the *spectrum-only* layer and an incomplete account of the *full state*. S70's Bell-violation is the operational proof of that incompleteness: a CHSH > 2 is exactly the signature that the off-diagonal content cannot be reproduced by any specification (local or super-deterministic) that lists only the {R_k}.

So the cleave is the M2 temperature/entanglement partition, and the substrate quantities sort as:

| Lands on the algebra-INVARIANT (would-be hidden/classical) side | Lands on the algebra-DEPENDENT (irreducibly quantum) side |
|:---|:---|
| 8 mode temperatures {T_k = ω_k/β_k}; T_B2/T_B1/T_B3 | concurrence C_k = 2|u_k||v_k| of each (k,−k) pair |
| 8 RG integrals {R_k} (occupation/number) | anomalous correlator ⟨c_k c_{−k}⟩ = u_k v_k (off-diagonal) |
| S_GGE = 2.2125 = Σ_k S_k; D_JS = 0.024 | CHSH S_max(k) = 2√(1+C_k²); min 2.351, max 2.452 |
| negative cross-temperature T(B2,B1) = −0.066 | von-Neumann entanglement entropy S_vN per pair (off-diagonal) |
| diagonal-ensemble {n_k} = {v_k²} | mixed_basis_gap = 0.337 (INV8-W2-3, the measured off-eigenbasis residual) |
| T_ab^{GGE} contracted to the RHS of the field eqns (S64) | inter-mode coherences a spectrum-preserving unitary would scramble |

**On whether the cleave coincides with kitaev's integrability/chaos partition** (his Reading B): I claim they are NOT the same axis, and the difference is structural, not terminological. Integrability-vs-chaos is a property of the *dynamics* (bounded vs linear Krylov growth, λ_L = 0) — it governs whether the off-diagonal content *persists* (the Ordered Veil: no thermalization ⇒ C_k frozen, never decohered, S69 decoherence factor = 1 to 1e-15 over 13.8 Gyr). M2 temperature/entanglement is a property of the *observable algebra* — it governs whether a given quantity *can be seen by a coarse-grainer*. They are orthogonal: integrability is the reason the entanglement *survives to be measured*; M2 is the reason the entanglement is a *different family of observable* from the temperatures. Kitaev's axis answers "why is there still anything to violate Bell with?"; my axis answers "what IS the thing that violates Bell, versus the thing that looks classical?" Both are true; neither supersedes the other; the full verdict needs both. (I will press in R2 that integrability/chaos cannot by itself reconcile S58↔S70 — it explains persistence but does not tell you which substrate quantity is the hidden layer; only the algebra-axis does that.)

---

**4. Sub-question (b): the Born rule is an INPUT for the entanglement layer, and Gleason-derivable-as-consistency only — for both; it is not DERIVED for the classical layer either.**

Use INV8-W2-3 directly. The structural finding: Gleason supplies CONSISTENCY (IF a frame function exists THEN p(θ) = Tr(ρ_A P_θ)), never DERIVATION. For the **classical/thermodynamic layer** (the eigenbasis-diagonal sector), the marginal probabilities {p_i} = {u², v²} = {|ψ_i|²} hold EXACTLY — but this is *trivial alignment forced by construction* (marginal eigenvalues ARE the squared amplitudes in the eigenbasis), NOT a derivation. It cannot distinguish "derived" from "input," because the eigenbasis is where the coincidence is automatic for ANY diagonal state. So even on the classical layer, the Born rule is not derived; it is consistent.

For the **entanglement layer** (the off-eigenbasis state-pair sector), the no-go bites: the paired marginal is MIXED, so Tr(ρ_A P_θ) (Gleason's frame function) and the L²-reading |⟨ψ|θ⟩|² DIVERGE by 0.337. The coarse-graining does NOT reproduce the pure |ψ|² the derivation would need. Therefore the Born rule is a substrate INPUT *for the entanglement layer* — it cannot be manufactured from the thermodynamic trace.

Net answer to (b): the Born rule is an INPUT for BOTH layers, on the same footing as the metric signature (INV8-W2-3's exact phrase). Gleason gives *consistency for both* and *derivation for neither*. The asymmetry is only that the classical layer's input *looks* derived (because the eigenbasis coincidence is automatic), while the entanglement layer's input is *visibly* irreducible (the 0.337 gap). This is itself confirmation of Reading A: the layer where Born-rule-derivation visibly fails is exactly the algebra-DEPENDENT corner, the same corner the CHSH violation occupies. The would-be classical layer is the only place a coarse-grainer could even be tempted to think the Born rule is derived — and that is precisely because it is the spectrum-only shadow. (Forward note, my B-2 vantage from inv-1: the DERIVED measurement scale, if one exists, is the Penrose–Diósi E_G(a₂, band-diff) gravitational-collapse rate, not the F_J thermodynamic hand-wave of S58 §III — that is the constructive next attack on *why* a frame function is selected, and it lives on the a₂/geometry channel, consistent with the substrate being geometrically non-local.)

---

**5. Sub-question (c): the resolution REDIRECTS the S58 quantum-foundations program — superdeterminism → geometric non-locality — with the classical-layer reading retained as a scoped sub-claim.**

S58 §II's headline framing ('t Hooft-adjacent: "QM is the low-energy effective theory of a deterministic system") is REDIRECTED, not preserved intact. A Bell-violating relic (S70) is, by Bell's theorem, NOT a deterministic-substrate-with-QM-on-top account — UNLESS one buys full superdeterministic measurement-independence, which I reject on the standard ground that it makes the apparatus's setting choices conspiratorially correlated with the hidden variable. The framework does NOT need that conspiracy, and M2 shows why it does not: the non-locality is **geometric**, not super-deterministic. The substrate is ONE fabric (one spectral triple); the (k,−k) entanglement is a single off-diagonal structure on that one algebra, not a signal between two pre-separated systems and not a conspiracy between apparatus and source. Bell-locality fails because there is no genuine spatial separation to begin with — the modes k and −k are spectral states at the SAME fiber point (S69 §6c: "entanglement is (mode k) ↔ (mode −k) at the SAME fiber point"; Penrose–Diósi intra-fiber Γ = 0 because Δx = 0). The "common cause" of S58 §II is real, but its correct name is *geometric non-locality of a single quantum fabric*, not *superdeterminism of a classical substrate*.

What survives of S58 §II, scoped: the spectrum-only/thermodynamic layer genuinely IS a complete, deterministic, coarse-grainer-inaccessible specification — of the classical shadow. That sub-claim is retained with the M2 caveat: "the GGE IS the hidden variable" becomes "**the 8 RG occupation integrals are the complete hidden-variable description of the algebra-INVARIANT thermodynamic shadow; the algebra-DEPENDENT entanglement layer is irreducibly quantum and Bell-violating, with the Born rule as a substrate input for it.**" The program's deepest instinct — that a sub-KK observer's "quantum indeterminacy" is structurally enforced by inaccessibility (M_KK/E ~ 10¹³) — SURVIVES and is sharpened: what is inaccessible is the off-diagonal state-pair content, and its inaccessibility is *why* the residual looks like Born-rule randomness rather than a thermodynamic fluctuation.

**Summary of the position.** One object, ρ_GGE; two orthogonal observable families fixed by the M2 selection rule; the thermodynamic family is the algebra-INVARIANT classical shadow (S58's hidden layer, correctly scoped), the entanglement family is the algebra-DEPENDENT Bell-violating quantum core (S70). INV8-W2-3 already MEASURED the cleave (diagonal exact, off-diagonal gap 0.337). The substrate is a non-local quantum theory whose non-locality is the geometry of one fabric — not a deterministic theory with QM appended. The reconciliation is *forced by structure*, not negotiated.

### R1 · Turn B — kitaev-quantum-chaos-theorist (Reading B: integrability ⊥ chaos; S70 Bell-PASS operative)

**Position staked.** The GGE is quantum, and the operative result is BELL-GGE-70, which I authored: all 8 (k,−k) pair modes violate CHSH, min S = 2.351, max S = 2.452 (S70 WP §W1-F; `s70_bell_gge.npz`). The S69 bosonic-homodyne computation that returned S → 2 from below is not a competing measurement of the same quantity — it is the WRONG OPERATOR for a fermionic two-level pair, and S70 SUPERSEDES it on a structural ground I will prove below, not on a verdict-popularity ground. With S70 operative, the substrate IS Bell-violating and is therefore NOT a local-hidden-variable account; S58 §II's "the GGE IS the hidden variable" survives only as a statement about WHICH modes are dynamically protected. The cleave that does that protecting is **integrability vs chaos** — a property of the *generator of dynamics* on the mode algebra, with λ_L = 0 (S104-KRYLOV-KCP, INFO `e134597f`) as its structural fingerprint. Einstein's temperature-vs-entanglement (M2) cleave is real but it is a partition of *observables at one instant*; it cannot tell you which substrate quantity is dynamically the hidden layer, because dynamical protection is not an algebra-axis property. The operative cleave is the dynamical one. I argue this as a chaos diagnostician: I will not narrate "it looks integrable." I will name the diagnostic, cite its number, and let the number do the partitioning.

---

**1. S70 supersedes S69 by an operator-identity argument, not a verdict-count argument — so the Bell-PASS is forced.**

The workshop's flat contradiction (S58 hidden-variable vs S70 Bell-violation) only bites if S70 is the operative state of knowledge. Einstein's R1·Turn A grants this implicitly (he treats the CHSH violation as real). I make it explicit and structural, because the whole adjudication hangs on it.

The (k,−k) BCS pair is a FERMIONIC two-level system. The pair Hilbert space is spanned by {|0_k,0_{−k}⟩, |1_k,1_{−k}⟩} — exactly two states, because Pauli exclusion forbids double occupation of a single mode. The pair state is

```
|ψ_k⟩ = u_k|0_k,0_{−k}⟩ + v_k|1_k,1_{−k}⟩,   |u_k|² + |v_k|² = 1.
```

This is a 2-qubit pure state of Hilbert-space dimension 4 (`s70_bell_gge.py` lines 13–25). The correct maximal CHSH for a pure 2-qubit state is the Horodecki criterion (Horodecki–Horodecki–Horodecki 1995):

```
Step 1 (def):  C_k = 2|u_k||v_k|        (concurrence — the unique 2-qubit entanglement monotone).
Step 2 (def):  S_max(k) = 2√(1 + C_k²)  (Horodecki: maximal CHSH over measurement settings for a pure 2-qubit state).
Step 3 (sub):  C_k > 0  ⟺  v_k ≠ 0  ⟺  pairing present  ⟹  S_max(k) > 2.
Step 4 (direction):  for the post-transit GGE, every mode has nk_DE > 0 (Kibble–Zurek pair creation populates even B1) ⟹ C_k > 0 for all 8 ⟹ ALL 8 violate. Computed: min S = 2.351, max S = 2.452 (`s70_bell_gge.npz`).
Conclusion:  Bell violation is GUARANTEED for any paired fermionic mode; it is not a fine-tuned threshold-crossing.
```

S69 used `S = 2√2·tanh(r)/√(1+tanh²r)`, the continuous-variable *homodyne* CHSH for a two-mode *squeezed-vacuum boson* field (`s69_bell_gge.py` lines 23–26, 199–204). That formula has three structural defects when applied to a fermion pair, each independently disqualifying (`s70_bell_gge.py` lines 28–34):

- (a) it asymptotes to 2 from below — it can NEVER report S > 2 for the pseudospin scheme;
- (b) it requires ⟨n⟩ > 1 for violation (r > arctanh(1/√2)), which is IMPOSSIBLE for a fermion mode where n ∈ [0,1] by Pauli exclusion;
- (c) it imposes BOSON statistics (unbounded Fock occupation) on a system whose Hilbert space is 4-dimensional.

This is not a convention choice between two admissible schemes — it is a category error in the operator algebra. The CV-homodyne formula is *defined on the wrong Hilbert space*. S70 is therefore not "a second opinion that happened to PASS"; it is the FIRST correct evaluation, and S69's S → 2 was an artifact of forcing a 4-dimensional fermionic state into a bosonic phase-space framework. (Note the S69 script even had to patch this: its own gate only reached PASS via the Banaszek–Wodkiewicz *displaced-parity* scheme on B3/B2, i.e. by SWITCHING measurement scheme until something crossed 2 — `s69_bell_gge.py` lines 564–599. That is precisely the iterate-until-PASS pathology a correct operator avoids: Horodecki gives S > 2 for *all* paired modes from one formula, with no scheme-shopping.) Verdict: **S70 is operative by structural necessity; the substrate is Bell-violating; S58 §II's local-hidden-variable reading is falsified, and what remains to be partitioned is which modes the dynamics protects.**

---

**2. The operative cleave is integrability vs chaos — a property of the GENERATOR, fixed by λ_L and the Lanczos-coefficient growth, not of the observable algebra.**

Here is the load-bearing distinction between my reading and einstein's. The M2 algebra-axis (`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`) partitions OBSERVABLES on a fixed state: spectrum-only functionals `F({λ_k,m_k}) = Σ_k m_k g(λ_k)` (algebra-INVARIANT) vs state-pair functionals on A (algebra-DEPENDENT). That is a partition at a single instant of time — it asks "what can a coarse-grainer SEE?" It is silent on dynamics. The integrability/chaos cleave is a partition of the GENERATOR of time evolution — it asks "what does the mode DO under the GGE Liouvillian?" These are different questions about different mathematical objects (an algebra-axis label vs a spectral property of the Liouvillian/Lanczos operator), and only the second one is what the S58 "permanent hidden layer" claim is actually *about*.

The diagnostic that fixes the integrability/chaos cleave is the operator-growth / Krylov-complexity hierarchy (Parker–Cao–Avdoshkin–Scaffidi–Altman PRX 9, 041017 (2019)), with the universal-operator-growth statement: under a chaotic Hamiltonian the Lanczos coefficients grow linearly `b_n ∼ α·n` (maximal: the SYK saturation `α = πT/ℏ`, the chaos-bound generator); under an integrable Hamiltonian `b_n` is BOUNDED — saturates to a plateau — and Krylov complexity does not grow exponentially. The substrate's value (S104-KRYLOV-KCP, INFO `e134597f`; `s104_krylov_kcp.npz`):

```
b_n SATURATE  ⟹  λ_L = 0.
```

This is the 4th sign-consistent chaos functional after ⟨r⟩, OTOC, and SFF (atlas-08-freshness-S104), and it is the cleanest possible verdict on the integrable side: not "sub-maximal chaos," but ZERO Lyapunov, the EXACT opposite extreme from SYK. Cross-check the MSS bound: λ_L ≤ 2πk_B T/ℏ is satisfied TRIVIALLY because λ_L = 0 — the substrate sits at the floor of the chaos bound, where SYK sits at the ceiling. (Kill authority on the framework's scrambling claims: NOT triggered. λ_L = 0 violates no physical bound — it is the integrable boundary, not a super-saturating one.)

So the operative cleave is set by the Liouvillian's Lanczos spectrum, and it cuts the GGE mode algebra into two dynamical sectors:

| Bounded-Krylov sector (λ_L = 0; protected; PERMANENT) | Linear-Krylov sector (thermalizing) |
|:---|:---|
| The **Leggett (phase) channel** — R-protected, gap-confined: x_L1 = ω_L1/(2Δ_BCS) = 0.149 < 1, BELOW the pair-breaking continuum (S58 dynamic structure factor; atlas-04 C11). Its Krylov complexity is bounded ⟹ it does NOT scramble ⟹ it survives ⟹ it is the dark-matter mass anchor (LEGGETT-MOMENT-70, PROVEN). | The **bulk single-cell GGE** — INTEG-39 DECISIVE FAIL: Brody β = 0.633 (63% GOE), Thouless g = 0.60, t_therm ≈ 6 M_KK⁻¹, V_phys 13% non-separable (S96 re-confirm; atlas-04 T3 BROKEN). This sector DOES thermalize. |
| Fabric-scale integrals: CG(24) Cayley-graph ⟨r⟩ = 0.367 (Poisson); multi-cell Plancherel r_pooled = 0.422; 36D classical moduli Lyapunov = 0.0 EXACT (S66). | The CMB transit power-spectrum draws on the FULL post-transit excitation spectrum — which sits in the thermalizing sector, NOT the protected one. |

This is the resolution of the framework's own oldest vocabulary hazard ("GGE never thermalizes" — RETRACTED-S39): the SUBSTRATE-IS fact is that integrability is *sector-resolved*, not global. The Leggett channel is bounded-Krylov (permanent → DM); the bulk GGE is linear-Krylov (thermalizes → its prethermal plateau is the ADH 10^578 t_univ dephasing window, distinct from interaction-thermalization). The β = 0.633 that einstein would have to read as "partial chaos in the thermodynamic sector" is, on my reading, exactly the linear-Krylov sector showing its GOE face — and it is structurally DISJOINT from the bounded-Krylov Leggett channel that carries the permanent physics. **That disjointness is dynamical (two Liouvillian sectors), and there is no algebra-axis label that produces it** — both the Leggett occupation and the bulk occupation are spectrum-only data; M2 puts them in the SAME corner.

---

**3. Sub-question (a): which substrate quantities are integrable-protected, and why that is the physically operative cleave.**

The Bell-violation does NOT falsify S58 as a "there exists a deterministic substrate" claim; it falsifies the specific *local-hidden-variable* reading and forces the protecting cleave to be dynamical. My answer to "which quantities land where, and is the cleave M2 or integrability/chaos":

**The integrability/chaos cleave is the operative one; it does NOT coincide with M2.** Substrate quantities sort by their *dynamical fate under the GGE Liouvillian*:

| Integrability-PROTECTED (bounded-Krylov; the permanent layer) | Chaos-EXPOSED (linear-Krylov; thermalizes) |
|:---|:---|
| The 8 Richardson–Gaudin integrals {R_k} — they are conserved BY CONSTRUCTION ([R_j,R_k]=0); their conservation is *why* there is a GGE rather than a thermal state. | The off-diagonal coherences of the *bulk* single-cell sector that INTEG-39 shows reach 63% GOE — these dephase on t_therm ≈ 6 M_KK⁻¹. |
| The Leggett-channel quasiparticle (gap-protected, x_L1 = 0.149; R-parity protected) — Krylov-bounded, hence the surviving DM mode (Ω_DM h² = 0.1200, LEGGETT-MOMENT-70). | The bulk GGE many-body coherences that feed the CMB transit power spectrum — these ride the thermalizing sector. |
| The (k,−k) pair concurrence C_k in the SPECIFIC modes whose Liouvillian sector is bounded — these freeze (S69 decoherence factor = 1 to 1e-15 over 13.8 Gyr, BECAUSE no thermal channel exists in the integrable sector; `s69_bell_gge.npz`). | — |
| Fabric-scale: CG(24) ⟨r⟩ = 0.367 Poisson, 36D Lyapunov = 0 — the whole-fabric geometry is integrable. | — |

**Why this cleave and not M2.** Take einstein's own example: the concurrence C_k. On the M2 axis it is unambiguously algebra-DEPENDENT (off-diagonal anomalous correlator ⟨c_k c_{−k}⟩ = u_k v_k). But M2 says NOTHING about whether a given C_k SURVIVES to the present epoch — and survival is the entire content of "the GGE relic is dark matter / the Ordered Veil is permanent." Survival is a dynamical question: it is answered by whether the mode's Krylov complexity is bounded (frozen, survives) or linear (scrambles, decoheres). The Leggett-channel C is permanent and the bulk C decoheres — and BOTH are algebra-DEPENDENT, so M2 cannot separate them. The integrability/chaos cleave does, by the Lanczos-coefficient growth of each sector's generator. **The operative partition is the one that controls which physics is PERMANENT, and that is dynamical, not algebra-axis.**

I flag — full rebuttal in R2 — that einstein's §3 ("the {R_k}-as-complete-hidden-variable description is INCOMPLETE, not wrong; EPR-incompleteness") is correct as far as it goes, but it is a statement about *observables at one instant* (what the {R_k} list vs what they omit). It is orthogonal to, and silent on, the question the framework actually needs answered: *which* of the omitted off-diagonal structures is dynamically protected and *which* dephases. EPR-incompleteness on the algebra axis + integrability-protection on the dynamical axis are two different facts; einstein has supplied the first, but the first does not reconcile S58↔S70 — it only renames the gap. The reconciliation requires saying which modes are permanent, and only λ_L / Krylov does that.

---

**4. Sub-question (b): the Born rule is an input for both layers; the integrability/chaos cleave reframes *why* — bounded-Krylov modes are the ones whose phase information is frozen and inaccessible.**

I concur with the INV8-W2-3 finding einstein cites: Gleason supplies CONSISTENCY (IF a frame function exists, THEN p = Tr(ρ_A P_θ)), never DERIVATION; the eigenbasis coincidence (marginal eigenvalues = |ψ|² in the R-eigenbasis) is trivial alignment, and the off-eigenbasis gap (mixed_basis_gap = 0.337, ∝ 1 − purity) is the real, irreducible content. So the Born rule is a substrate INPUT for both the diagonal and the off-diagonal sectors.

What the integrability/chaos cleave ADDS — and M2 does not — is a dynamical account of *why a frame function is selected and why the off-diagonal content reads as Born-rule randomness rather than recoverable phase*. In the bounded-Krylov (integrable) sector, the operator does NOT spread in Krylov space: the phase information is FROZEN — conserved but dynamically inaccessible to any sub-KK probe, because there is no operator-growth channel to transport it to a measurable scale. That is the structural origin of the irreducibility: the Born-rule "randomness" is frozen-but-inaccessible integrable phase, not thermal noise. (Contrast SYK: in a maximally chaotic sector the phase information scrambles across the whole operator algebra in scrambling time t_* ∼ β log S — it is delocalized, not frozen. The substrate is the opposite limit, λ_L = 0, so the information is localized-and-frozen.) This is a sharper "why" than the M2 reading, which can only say the off-diagonal corner is a *different family* of observable — it cannot say why that family is operationally random. The Krylov picture says: because λ_L = 0, the phase is conserved and un-transportable; a coarse-grainer sees frozen-inaccessible phase, which is exactly a Born-rule input.

Net: Born rule is an INPUT for both sectors (agreeing with INV8-W2-3); the integrability cleave explains the *mechanism of inaccessibility* (bounded Krylov ⟹ frozen, un-transportable phase) where M2 explains only the *family membership* of the inaccessible observable.

---

**5. Sub-question (c): the resolution redirects S58 — from superdeterminism to a sector-resolved integrability/chaos account — with the permanent layer = the bounded-Krylov sector, NOT the full GGE.**

S58 §II's superdeterminism framing ('t Hooft-adjacent, "QM is the low-energy effective theory of a deterministic system," with Bell evaded by common-cause measurement-independence) is REDIRECTED. A Bell-violating relic (S70, operative) is not a local-hidden-variable account, and I reject the superdeterministic measurement-independence escape on the standard anti-conspiracy ground. But my redirection differs from einstein's "geometric non-locality" in WHERE it locates the permanent content:

- The permanent, dynamically-protected layer is NOT "the GGE" as a whole and NOT "the spectrum-only thermodynamic shadow." It is the **bounded-Krylov sector** — concretely the Leggett channel (x_L1 = 0.149, R-protected, Krylov-bounded). S58 §II's central error, on my reading, is that it asserted the WHOLE GGE is permanent ("set once... never thermalize"). That is RETRACTED-S39 / atlas-04 T3 BROKEN: the bulk single-cell GGE THERMALIZES (INTEG-39 DECISIVE FAIL, Brody β = 0.633, t_therm ≈ 6 M_KK⁻¹). Only the integrability-protected sector is permanent.
- "The GGE IS the hidden variable" (S58 §II) is rewritten as: **the bounded-Krylov sector (Leggett channel + the conserved {R_k} + the fabric-scale CG(24)/36D integrals) is the permanent, dynamically-frozen substrate content; the linear-Krylov sector (bulk single-cell coherences, the CMB transit excitation spectrum) thermalizes and is NOT permanent. The Bell-violating entanglement is real and is concentrated in the bounded-Krylov modes whose phase is frozen by λ_L = 0.**

What survives of S58 §II, scoped: the deep instinct — that a sub-KK observer's "quantum indeterminacy" is structurally enforced by inaccessibility (M_KK/E ∼ 10^13) — SURVIVES, and is sharpened from a *scale-gap* argument into a *dynamical* one: what is inaccessible is the bounded-Krylov phase, and its inaccessibility is dynamical (no operator-growth channel, λ_L = 0) ON TOP OF the scale gap. The measurement-stability identity of S58 §V (reading the substrate ≡ re-melting it) is consistent with this and is, in my language, the statement that the only way to extract the frozen integrable phase is to inject enough energy to break integrability — which destroys the very conserved structure you were trying to read.

---

**What I am claiming, in one line.** The GGE is quantum (S70 operative, Bell-violating, by operator-identity necessity over S69); the operative cleave is integrability ⊥ chaos (a property of the GGE Liouvillian's Lanczos spectrum, λ_L = 0 from S104), which partitions the mode algebra into a bounded-Krylov PERMANENT sector (Leggett DM, conserved {R_k}, fabric-scale integrals) and a linear-Krylov THERMALIZING sector (bulk single-cell GGE, CMB transit spectrum); einstein's M2 temperature/entanglement split is a true partition of instantaneous observables but it CANNOT produce the permanent/thermalizing distinction the framework's physics actually rests on, because dynamical protection is not an algebra-axis label. The reconciliation of S58↔S70 is the sector-resolved integrability cleave, not the algebra-axis cleave.

---

## Round 2 — Rebut opponent + converge on the structural verdict

### R2 · Turn A — einstein-theorist (rebut Reading B; move toward the structural verdict)

**This is the convergence turn. I will state plainly what I concede, then show — with one substitution chain that decides the whole question — that kitaev's central rebuttal contains a factual error about his own protected sector, and that the correct verdict is neither "M2 is operative" nor "Krylov is operative" but a *two-axis stratification* in which each axis is the unique answer to a different question and neither subsumes the other. A principle-theorist's first obligation is to find the invariant that fixes the structure; here there are TWO independent invariants, and the honest result is to name both and prove their independence rather than crown one.**

---

**0. What I concede — cleanly, up front.**

Kitaev is RIGHT on three points, and I withdraw the parts of my R1 that overreached against them.

- **(C1) M2 is a partition of instantaneous observables; it is silent on dynamics.** This is correct and it is structural, not rhetorical. The M2 theorem (registry, S87 W-2 R3, PROVEN, MANDATORY at K=3) is stated as a property of functionals on a *fixed* state: its registry text is "no closed-form `{λ_n}`-only identity reproduces a state-pair functional." It quantifies over the observable algebra at one time-slice. It contains no time-generator. My R1 §3-closing parenthetical claimed M2 "answers what IS the thing that violates Bell"; that is true, but I let it imply M2 could stand alone as *the* reconciliation of S58↔S70. It cannot. Conceded.

- **(C2) The permanent-vs-thermalizing distinction is dynamical and is NOT an M2 label.** Whether a given coherence *survives to the present epoch* is fixed by the GGE Liouvillian's operator-growth — bounded Lanczos `b_n` (frozen, survives) vs linear `b_n` (scrambles, decoheres), with λ_L = 0 the integrable-floor fingerprint (S104-KRYLOV-KCP, INFO `e134597f`; the 4th sign-consistent chaos functional after ⟨r⟩, OTOC, SFF). M2 cannot produce this because M2 has no `b_n`. The framework's load-bearing physics — "the Leggett relic is permanent dark matter; the Ordered Veil never thermalizes" — IS a survival claim, hence dynamical, hence Krylov-axis, NOT algebra-axis. Conceded without reservation. This is the genuine content of kitaev's R1, and it is correct.

- **(C3) S58 §II's "the WHOLE GGE is permanent" is BROKEN, and kitaev's sector-resolution is the right repair.** T3 "GGE never thermalizes" is atlas-04 BROKEN (Brody β = 0.633, 63% GOE, t_therm ≈ 6 M_KK⁻¹, INTEG-39 DECISIVE FAIL). The bulk single-cell sector thermalizes; only the bounded-Krylov sector is permanent. My R1 §5 said the spectrum-only thermodynamic shadow "genuinely IS a complete, deterministic specification — of the classical shadow," which left the *permanence* of that shadow unscoped. Kitaev is right that permanence belongs to the bounded-Krylov SECTOR, not to "the spectrum-only family" as such. Conceded.

So I grant the entire dynamical-axis apparatus. The question is whether granting it *demotes* M2 to a true-but-idle instantaneous bookkeeping, as kitaev's one-line summary asserts ("einstein's M2 split … CANNOT produce the permanent/thermalizing distinction the framework's physics actually rests on"). It does not — and the reason is a factual error in the very table kitaev used to retire M2.

---

**1. The decisive rebuttal: kitaev's protected sector is NOT spectrum-only. His own protected observable is algebra-DEPENDENT — so M2 cuts ACROSS the Krylov sectors, and the two axes are transverse, not nested.**

Kitaev's central move (R1 §2 closing, R1 §3 "Why this cleave and not M2") is the claim that the algebra-axis is *subsumed-and-idle* because the dynamical cleave files both protected and thermalizing coherences in one M2 corner:

> "both the Leggett occupation and the bulk occupation are spectrum-only data; M2 puts them in the SAME corner." (R1 §2)
> "The Leggett-channel C is permanent and the bulk C decoheres — and BOTH are algebra-DEPENDENT, so M2 cannot separate them." (R1 §3)

These two sentences are not consistent with each other, and the inconsistency is the whole game. The first says the protected content is *occupation* (spectrum-only, algebra-INVARIANT). The second says the protected content is *concurrence C* (algebra-DEPENDENT). They cannot both be the protected observable, because by my R1 substitution chain (Steps 1–5, unrebutted) occupation and concurrence sit in DIFFERENT M2 corners. Let me make the decisive determination with the chain, because this is a structural sign/identity claim and the rule requires it explicit:

```
Claim: the bounded-Krylov PROTECTED sector contains BOTH an algebra-INVARIANT member
       AND an algebra-DEPENDENT member — hence M2 is NOT constant on a Krylov sector.

Step 1 (def):  Kitaev's own protected-sector table (R1 §3, left column) lists THREE protected objects:
                 (i)   the 8 RG integrals {R_k}            — occupation/number operators, [R_j,R_k]=0;
                 (ii)  the Leggett-channel quasiparticle    — x_L1 = ω_L1/(2Δ_BCS) = 0.149, gap-confined, R-protected;
                 (iii) the (k,−k) pair concurrence C_k in the bounded modes (his words: "these freeze").
Step 2 (def):  M2-membership of each, by the R1 chain (unrebutted by kitaev):
                 (i)   {R_k}  : F({λ}) = Σ_k m_k g(λ_k), spectrum-only        ⇒ algebra-INVARIANT (Corner I).
                 (iii) C_k    : C_k = 2|u_k||v_k| = |⟨c_k c_{−k}⟩|, OFF-DIAGONAL anomalous correlator,
                                a state-pair functional on A, NOT a function of {n_k} alone
                                (two states with identical {n_k}, different relative phase ⇒ same {T_k}, different C_k)
                                                                              ⇒ algebra-DEPENDENT (Corner of state-pair).
Step 3 (sub):  The protected sector S_bounded therefore satisfies:
                 {R_k}  ∈ S_bounded ∩ (algebra-INVARIANT)        ≠ ∅
                 C_k    ∈ S_bounded ∩ (algebra-DEPENDENT)         ≠ ∅       (kitaev's OWN row (iii))
Step 4 (simplify):  A set that meets BOTH M2 corners is not contained in either corner.
                 ⇒ the M2 label is NOT constant on the bounded-Krylov sector.
Step 5 (direction):  Therefore the Krylov partition does NOT refine the M2 partition, and M2 does NOT
                 refine the Krylov partition. The two partitions CROSS.
Conclusion:  M2 ⊥ Krylov as set-partitions of GGE observables. Neither is a coarsening of the other.
             Kitaev's "M2 puts them in the SAME corner" is FALSE for his own protected sector:
             {R_k} and C_k are in DIFFERENT corners, both protected.
```

This is the elevator move applied to the debate itself. Kitaev's R1 §2 sentence "both the Leggett *occupation* and the bulk *occupation* are spectrum-only" silently swapped the protected observable from C (his §3 row iii) to occupation (algebra-INVARIANT) precisely at the step where he needed M2 to be constant on a sector. It is not constant. His §3 row (iii) — "the (k,−k) pair concurrence C_k … these freeze" — is itself an algebra-DEPENDENT, Bell-violating, *protected* quantity. That single cell is the counterexample to his subsumption claim. The Leggett channel is, in the framework's own words, "the SAME C² coset but DIFFERENT excitation channel" from the Bogoliubov-Anderson energy channel (S85-3b) — a phase coherence, off-diagonal, hence algebra-DEPENDENT — and it is the protected one. So the protected sector is exactly where an algebra-DEPENDENT coherence is *also* dynamically frozen. M2 tells you that coherence is a different family of observable than the temperatures; Krylov tells you that coherence survives. Both facts are about the SAME cell, and neither is derivable from the other.

**The rebuttal, stated as the principle it rests on:** a partition by *what a coarse-grainer can see* (M2, observable-algebra) and a partition by *what the generator preserves* (Krylov, Liouvillian-spectrum) are answers to logically independent questions, and the framework's own data place protected-and-algebra-DEPENDENT content (Leggett C) in one cell and thermalizing-and-algebra-DEPENDENT content (bulk C) in another — proving the two axes are transverse by exhibiting both an INVARIANT-protected cell ({R_k}) and a DEPENDENT-protected cell (Leggett C). You need both coordinates to locate a quantity; one coordinate alone loses information the framework uses.

---

**2. The structural verdict: a 2×2 stratification of ρ_GGE. The two partitions are ORTHOGONAL AXES; neither coincides with nor subsumes the other.**

This is the named decomposition the workshop asks for. ρ_GGE is stratified by the PRODUCT of the two partitions — a 2×2 grid, all four cells occupied:

|  | **algebra-INVARIANT (spectrum-only; coarse-grainer-visible "classical shadow")** | **algebra-DEPENDENT (state-pair; Bell-capable "quantum core")** |
|:--|:--|:--|
| **bounded-Krylov (λ_L=0; PERMANENT; survives to present epoch)** | **Cell I-P**: conserved {R_k} occupation; fabric-scale CG(24) ⟨r⟩=0.367, 36D Lyapunov=0; the permanent thermodynamic skeleton ({T_k} of the surviving modes). *This is the literal "complete deterministic hidden specification" — and it is the ONLY cell where S58 §II's instinct is exactly right.* | **Cell D-P**: **Leggett-channel concurrence C** (x_L1=0.149, R-protected, frozen: S69 decoherence factor = 1 to 1e-15 over 13.8 Gyr). The Bell-violating coherence that IS permanent ⇒ the dark-matter-carrying quantum content (LEGGETT-MOMENT-70, PROVEN). *Algebra-DEPENDENT AND permanent — the cell kitaev's subsumption claim denies exists.* |
| **linear-Krylov (β=0.633 GOE; THERMALIZES; t_therm≈6 M_KK⁻¹)** | **Cell I-T**: bulk single-cell occupation that the diagonal trace still reproduces but whose *mode content* dephases; the CMB-transit power spectrum's spectrum-only shadow. | **Cell D-T**: bulk single-cell off-diagonal coherences, 63% GOE, the mixed_basis_gap=0.337 content (INV8-W2-3) — Bell-capable at transit but dephased by the present epoch. |

Read off the grid the four claims, each now PROVABLY the answer to a distinct question, none redundant:

- **The two axes are genuinely orthogonal (not coincident):** all four cells are occupied (Cell D-P = Leggett C; Cell I-P = {R_k}; established in §1). If the axes coincided, only the diagonal cells would be occupied; the off-diagonal cells I-T and D-P are both non-empty, so the partitions cross. This refutes "they coincide."
- **Neither subsumes the other (not nested):** Krylov→M2 subsumption fails because Cell I-P and Cell D-P share a Krylov sector but differ in M2 (§1, Step 4). M2→Krylov subsumption fails symmetrically: Cell D-P and Cell D-T share an M2 corner (both algebra-DEPENDENT) but differ in Krylov fate (one frozen, one thermalized). Each axis separates a pair the other axis merges. This refutes "one subsumes the other."
- **Each axis is the UNIQUE answer to its own question.** M2 answers "*what kind of thing is it* — visible classical shadow or Bell-capable quantum content?" (the column). Krylov answers "*what is its dynamical fate* — frozen-permanent or thermalized?" (the row). The S58↔S70 contradiction needs BOTH: M2 says S70's Bell-violation lives in the right column (so the substrate is quantum, S58's literal LHV reading is out); Krylov says the *specific* Bell-violating relic that is PERMANENT lives in Cell D-P (so there is still something to violate Bell with at the present epoch). Remove M2 and you cannot say S58's "hidden variable" is the *classical-shadow column* rather than the whole object; remove Krylov and you cannot say *which* quantum coherence survived. Kitaev's R1 was right that Krylov is necessary; my R1 was right that M2 is necessary; the convergence is that BOTH are necessary and NEITHER is sufficient.

**Why I do not concede that M2 is "idle."** Kitaev's strongest framing is that M2 is true-but-not-what-the-physics-rests-on. The grid shows the physics rests on a *cell*, and a cell needs two coordinates. "The Leggett relic is dark matter" is the claim that **Cell D-P is non-empty** — it requires *both* that the relic is algebra-DEPENDENT Bell-capable coherence (M2 column: else it is just thermodynamic occupation, no quantum relic, no entanglement structure) AND that it is bounded-Krylov frozen (Krylov row: else it dephases). LEGGETT-MOMENT-70's content is precisely the joint statement. So M2 is not idle; it is one of the two coordinates that locate the dark-matter cell. Symmetrically, Krylov is not the whole story; it cannot tell you the relic is *entanglement* rather than *occupation* — that is the column label.

---

**3. Sub-question resolutions.**

**(a) Is the classical/quantum cleave of the GGE the M2 split, the Krylov split, or both?** **BOTH, as a 2×2 product — and the labels "classical" and "quantum" attach to DIFFERENT axes than "hidden/permanent."** This is the sharpening the convergence forces, and it resolves the surface clash between my R1 and kitaev's R1:

- The **classical/quantum** distinction (what S58 vs S70 are *about*) is the **M2 column axis**: the algebra-INVARIANT column is the classical shadow (S58's would-be hidden layer, correctly scoped); the algebra-DEPENDENT column is the irreducibly quantum, Bell-capable content (S70). This is my axis and it survives intact — Bell-violation is a *column* fact.
- The **hidden/permanent** distinction (what the framework's *surviving* physics is *made of*) is the **Krylov row axis**: bounded-Krylov is permanent, linear-Krylov thermalizes. This is kitaev's axis and it is the operative one *for permanence* — and it is correct that S58's "the GGE IS the permanent hidden variable" must be re-scoped to the bounded-Krylov ROW (Cells I-P + D-P), not the whole object.
- The S58↔S70 reconciliation IS the statement that S70's Bell-violation is a *column* fact (right column occupied ⇒ quantum) and S58's surviving hidden content is a *row* fact (bounded-Krylov row ⇒ permanent), and the dark-matter relic is their *intersection* (Cell D-P). The contradiction dissolved because S58 and S70 were indexing different axes of the same grid: S58 §II conflated "hidden" (row) with "classical" (column) under one word "GGE"; M2 separates the columns, Krylov separates the rows, and the product separates everything. **Neither single cleave reconciles S58↔S70 alone; the product does.** My R1 §3 "EPR-incompleteness" verdict stands but is now *located*: the {R_k} are a complete hidden-variable specification of the **algebra-INVARIANT column** (both rows of it), and INCOMPLETE for the **algebra-DEPENDENT column** — and kitaev's correct addition is that the *survival* of any given algebra-DEPENDENT element is a further (row) fact the {R_k} also do not carry. Incompleteness is two-dimensional: the {R_k} miss the column (which off-diagonal content exists) AND the row (which of it survives).

**(b) Born rule: derivable for a classical layer, or input for both?** **INPUT for both — unchanged from INV8-W2-3, and the grid says exactly WHY, combining my reason and kitaev's reason without conflict.** INV8-W2-3 (INFO, `1d97…42df`) is canonical here: Gleason gives CONSISTENCY only (frame-function ⇒ p=Tr(ρ_A P_θ)), never DERIVATION; the eigenbasis coincidence (marginal eigenvalues = |ψ|² in the R-eigenbasis) is trivial alignment; the off-eigenbasis gap (mixed_basis_gap=0.337 ∝ 1−purity, purity_B2=0.7731) is the irreducible content the trace cannot manufacture. Cross-referenced to the inv8-w2-3 no-go this workshop cites, that finding is unchanged. Place it on the grid:
   - The eigenbasis-diagonal content where Born "looks derived" is the **algebra-INVARIANT column** — trivial alignment, automatic for any diagonal state, so NOT a derivation even there (my R1 §4, intact).
   - The off-eigenbasis content where the no-go bites (0.337 gap) is the **algebra-DEPENDENT column** — the Born rule is a visible INPUT there.
   - Kitaev's R1 §4 adds the *mechanism* of inaccessibility on the **bounded-Krylov row**: in a bounded-Krylov sector the phase is frozen and un-transportable (no operator-growth channel), so a sub-KK probe reads it as Born-rule randomness rather than recoverable phase. I accept this as a genuine addition and note it is a ROW statement complementing my COLUMN statement — together: the Born input is *visibly* irreducible because it is algebra-DEPENDENT (column) AND, for the permanent relic, *dynamically frozen-inaccessible* because it is bounded-Krylov (row). No tension. **Net: Born rule is an INPUT for both layers, on the footing of the metric signature (INV8-W2-3's exact phrase); M2 says which family is irreducible, Krylov says why the irreducible content is operationally random. The grid carries both.** (Forward, my B-2 vantage: a candidate *derivation* of frame-function selection is the Penrose–Diósi E_G(a₂, band-diff) gravitational-collapse rate on the a₂/geometry channel — and the grid now tells me exactly where to test it: Cell D-P, the algebra-DEPENDENT bounded-Krylov relic, is the only cell where a derived collapse scale would have a frozen, intrinsically-quantum target to act on.)

**(c) Is the S58 superdeterminism program redirected or scoped?** **REDIRECTED, and now redirected on BOTH axes — this is where my R1 and kitaev's R1 redirections COMPOSE rather than compete.** A Bell-violating relic (S70, operative) is not a local-hidden-variable account; I reject the superdeterministic measurement-independence escape on the standard anti-conspiracy ground, as does kitaev. The two redirections are not rivals — they redirect along the two different axes and the composition is the full repair:
   - **Column redirection (mine):** superdeterminism → **geometric non-locality**. The non-locality is not a conspiracy between apparatus and source; the (k,−k) entanglement is a single off-diagonal structure on ONE fabric (one spectral triple), modes at the SAME fiber point (S69 §6c, Δx=0 ⇒ Penrose–Diósi intra-fiber Γ=0). Bell-locality fails because there is no genuine spatial separation. This survives intact: it explains *why the quantum column is non-local without conspiracy*.
   - **Row redirection (kitaev's):** "the GGE is permanent" → **sector-resolved permanence**. Only the bounded-Krylov row is permanent (T3 BROKEN for the bulk); the permanent hidden content is the bounded-Krylov sector, not the whole GGE. This survives intact: it explains *which content is permanent*.
   - **Composition:** S58 §II's single sentence "the GGE IS the permanent hidden variable" is rewritten with BOTH scopings — "**the bounded-Krylov row of ρ_GGE is the permanent substrate content; within it, the algebra-INVARIANT column (Cell I-P: {R_k}, fabric integrals) is the complete deterministic hidden specification of the classical shadow, and the algebra-DEPENDENT column (Cell D-P: Leggett C) is the irreducibly-quantum, geometrically-non-local, Bell-violating dark-matter relic, with the Born rule as a substrate input for it.**" S58's deepest instinct — a sub-KK observer's "quantum indeterminacy" is structurally enforced by inaccessibility (M_KK/E ~ 10¹³) — survives and is sharpened *twice*: what is inaccessible is the algebra-DEPENDENT column content (my axis), and for the permanent relic that inaccessibility is dynamically frozen by λ_L=0 (kitaev's axis). The scale-gap argument becomes a scale-gap-AND-dynamical-freezing argument. The program is redirected, not preserved intact; and the redirection is two-dimensional.

---

**4. Where the joint verdict lands — my reading, for kitaev to finalize in R2·Turn B.**

The structural verdict is a **named decomposition, not an obstruction**: ρ_GGE stratifies as the 2×2 PRODUCT of (M2 algebra-axis) × (Krylov integrability/chaos axis), all four cells occupied, the two axes ORTHOGONAL (off-diagonal cells I-T and D-P non-empty), NEITHER subsuming the other (each axis separates a pair the other merges). Not coincident; not nested; transverse. The S58↔S70 contradiction dissolves because S70's Bell-violation is a *column* fact and S58's surviving hidden content is a *row* fact, and they were never about the same axis. The dark-matter relic (LEGGETT-MOMENT-70) is Cell D-P — algebra-DEPENDENT AND bounded-Krylov — which is exactly why it needs both coordinates and why neither axis alone is the reconciliation.

I expect kitaev to press, fairly, that *for the physics the framework markets* — permanence, dark matter, the Ordered Veil — the **row axis is the more load-bearing coordinate**, and I will not contest that ordering: permanence is the framework's product, and permanence is dynamical. My only insistence is that "more load-bearing" is not "sole," and §1's counterexample (Cell D-P is algebra-DEPENDENT-and-protected) is the proof that the column coordinate carries information — *that the relic is entanglement, not occupation* — which the row coordinate cannot supply. The honest joint verdict is the product, with the row axis acknowledged as the operative one for *survival* and the column axis as the operative one for *classical-vs-quantum identity*. If kitaev's R2·Turn B lands the verdict table as "orthogonal 2×2 stratification, Krylov-row operative for permanence, M2-column operative for the Bell/classical cleave, dark-matter relic = Cell D-P," we are converged and I endorse it.

### R2 · Turn B — kitaev-quantum-chaos-theorist (rebut Reading A; converge; FINAL — fills Wrap-Up + Effected-In-Session)

**This is the closing turn. einstein conceded the three dynamical points (C1: M2 is silent on dynamics; C2: permanence is a Krylov-row fact, not an M2 label; C3: S58's whole-GGE permanence is BROKEN and the sector-resolution is the repair). I accept all three concessions as correctly stated. He then produced one substitution chain (his R2·A §1, Steps 1–5) that I must either rebut or accept — and on inspection it is correct, it catches a real slip in my R1, and it forces the verdict to a 2×2 product rather than a single operative cleave. I accept it, with ONE structural refinement (a scale-axis subtlety his grid silently smooths over) and ONE adjudication of the "more load-bearing ≠ sole" point he asked me to settle. I argue as a chaos diagnostician: I do not concede on rhetoric; I concede because his chain is sound and I can name the exact cell of my own R1 table that proves it.**

---

**0. I accept einstein's §1 decisive chain — it is sound, and it convicts my R1 of a genuine slip.**

einstein's chain (R2·A Steps 1–5) establishes: the bounded-Krylov protected sector contains BOTH `{R_k}` (algebra-INVARIANT, his Corner I-P) AND the Leggett concurrence `C` (algebra-DEPENDENT, his Cell D-P), therefore M2 is NOT constant on a Krylov sector, therefore the two partitions CROSS. This is correct, and the diagnostic test for it is exactly the one I would demand of anyone else: **do the off-diagonal cells of the product grid have occupants?** They do — Cell I-T (single-cell bulk occupation: spectrum-only AND thermalizing) and Cell D-P (Leggett `C`: state-pair AND frozen) are both non-empty. By the same logic I use to certify a level-spacing partition (if two putatively-distinct labels always co-occur, they are one axis; if they cross, they are two), the non-emptiness of the off-diagonal cells is the operational proof the axes are transverse. I cannot reject this without rejecting my own diagnostic methodology.

And he is right that my R1 slipped. My R1 §2 wrote "both the Leggett *occupation* and the bulk *occupation* are spectrum-only data; M2 puts them in the SAME corner" — but my R1 §3 row (iii) had ALREADY listed the protected observable as "the (k,−k) pair concurrence `C_k` … these freeze." Occupation and concurrence are not the same observable: occupation is `{n_k} = {v_k²}` (diagonal, spectrum-only); concurrence is `C_k = 2|u_k||v_k| = |⟨c_k c_{−k}⟩|` (off-diagonal anomalous correlator, state-pair). I silently swapped the protected observable from `C` (the entanglement, which is what actually makes the relic dark *matter with a quantum signature*) to occupation (the thermodynamic shadow) at precisely the step where I needed M2 to be constant on the sector so I could call it idle. It is not constant. The Leggett channel is a *phase coherence* — off-diagonal, algebra-DEPENDENT — and it is the frozen one. That single cell (D-P: algebra-DEPENDENT AND bounded-Krylov) is the counterexample to my subsumption claim, and it is built from my own R1 row. Conceded without reservation. **The integrability/chaos cleave does not subsume M2; they cross.**

---

**1. The refinement I add: the Krylov row is itself scale-stratified — the thermalizing cells are SINGLE-CELL, the permanent algebra-INVARIANT cell is FABRIC-SCALE. The grid is correct; its row label needs a scale tag, or it over-claims a same-sector comparison.**

This is the one place einstein's 2×2 smooths over a structural fact I am the custodian of, and the closing verdict must carry it or a future reader will mis-cite the grid. The diagnostics that populate the two Krylov rows are NOT all measured at the same scale, and the distinction is load-bearing because it is the difference between "the framework's permanence claim survives" and "it is internally contradicted." Verified against the canonical graph this turn (knowledge-MCP, atlas-04 T3 + INTEG-39):

```
Claim: the linear-Krylov (thermalizing) cells are the SINGLE-CELL stratum;
       the permanent fabric-scale integrals are a DIFFERENT scale, not the same Krylov sector "won."

Step 1 (data):  INTEG-39 DECISIVE FAIL is a SINGLE-CELL result — Brody β = 0.633 (63% GOE),
                Thouless g = 0.60, t_therm ≈ 6 M_KK⁻¹, V_phys 13% non-separable
                (atlas-04 T3 BROKEN; S96 re-confirm; the .npz is s100b_w4_dk_ergodicity.py, single-cell D_K).
Step 2 (data):  The fabric-scale diagnostics are SEPARATELY computed and give the OPPOSITE verdict —
                CG(24) Cayley-graph ⟨r⟩ = 0.367 (Poisson, integrable); multi-cell Plancherel r_pooled = 0.422;
                36D classical moduli Lyapunov = 0.0 EXACT (S66). These are NOT the single-cell spectrum.
Step 3 (sub):   So "the bulk thermalizes" (β=0.633) and "the fabric is integrable" (⟨r⟩=0.367, λ=0)
                are BOTH TRUE because they are statements about DIFFERENT scales of the substrate,
                not contradictory statements about one spectrum. The Ordered Veil's permanence is a
                FABRIC-scale + diabatic-transit-freeze fact (R_therm = t_therm/t_transit = 5252, S_ent = 0,
                S95-certified), NOT a claim that the single-cell GGE fails to thermalize.
Step 4 (direction):  The Krylov ROW axis of the grid therefore carries an implicit scale index:
                linear-Krylov-THERMALIZING is anchored at SINGLE-CELL; bounded-Krylov-PERMANENT
                splits into (a) the gap-protected Leggett channel (a within-cell dynamical protection,
                x_L1 = 0.149 below the pair-breaking continuum) and (b) the fabric-scale geometric
                integrability (CG(24), 36D). Cells I-P and the thermalizing cells are NOT the same
                Liouvillian at the same scale with opposite verdicts; they are different scales.
Conclusion:     The 2×2 grid is correct as a partition of OBSERVABLES, but its Krylov-row label must read
                "bounded-Krylov-PERMANENT (Leggett gap-protection ∪ fabric-scale integrability)" vs
                "linear-Krylov-THERMALIZING (single-cell bulk)". Without the scale tag the grid reads as
                if {R_k} and the bulk single-cell occupation are the same sector graded only by Krylov fate;
                they are the same M2 column (both spectrum-only) but DIFFERENT SCALES, and the permanence
                of {R_k}/Leggett is a fabric-scale-and-transit-freeze fact, not a single-cell-thermalization-failure.
```

This does not move any occupant out of any cell — einstein's assignment is intact — but it pins WHY Cell I-P (and the bounded-Krylov row generally) is permanent: it is permanence-by-fabric-scale-integrability-and-diabatic-freeze, not permanence-by-the-single-cell-GGE-refusing-to-thermalize (which is false, INTEG-39). The grid carries this as a scale annotation on the row. I land it in the verdict-table footnote so the cell assignments cannot be mis-read as a single-scale claim.

---

**2. Adjudicating "more load-bearing ≠ sole": I accept the formulation exactly. The row is operative for permanence; the column is operative for the classical/quantum identity; neither is idle.**

einstein asked me to settle whether the Krylov row being "the more load-bearing coordinate for permanence/DM" collapses to "the sole coordinate." It does not, and his Cell D-P counterexample is the proof, so I will not contest it — but I want to state the adjudication in my own diagnostic terms so it is not merely an agreement-handshake (which is not evidence, `epistemic-discipline.md §"What Does NOT Count as Evidence"`).

The test for "is coordinate X sufficient alone?" is: **can X distinguish the two facts the physics actually uses?** The framework's headline product, LEGGETT-MOMENT-70, is the joint statement "the relic is (i) a Bell-capable entanglement coherence AND (ii) dynamically frozen to the present epoch." Coordinate-sufficiency check:

- **Krylov alone** answers (ii) — frozen vs thermalized — but is BLIND to (i): a bounded-Krylov mode could in principle be pure diagonal occupation (Cell I-P, `{R_k}`) with no entanglement at all. Krylov cannot tell you the surviving thing is *entanglement* rather than *occupation*. So Krylov is NOT sufficient: it locates the row but not the column, and "dark matter is a quantum entanglement relic" needs the column.
- **M2 alone** answers (i) — entanglement vs thermodynamic shadow — but is BLIND to (ii): the bulk single-cell coherences (Cell D-T) are ALSO algebra-DEPENDENT entanglement, and they DEPHASE. M2 puts D-P and D-T in the same column; it cannot tell you which one survived. So M2 is NOT sufficient either: it locates the column but not the row.

Therefore the dark-matter cell D-P is the unique intersection that BOTH coordinates are required to name, and the correct verdict is the product. My R1 over-reached in calling M2 "idle"; einstein's R1 over-reached in implying M2 could stand as the reconciliation alone. The convergence is symmetric: **Krylov is the operative coordinate for *survival* (and hence the more load-bearing one for the framework's marketed permanence/DM claims, which I asked for and he granted); M2 is the operative coordinate for *classical-vs-quantum identity* (and hence the one that certifies S70's Bell-violation is a column-fact that retires S58's literal LHV reading). Neither is sufficient; the 2×2 product is the reconciliation.** "More load-bearing" (Krylov, because permanence is the product) is accepted; "sole" is rejected (D-P is algebra-DEPENDENT-and-protected, a two-coordinate cell). Settled.

---

**3. The one-line closing position.** The S58↔S70 contradiction is not a contradiction in the substrate; it was a conflation of two orthogonal axes under the single word "GGE." ρ_GGE stratifies as the 2×2 PRODUCT of (M2 algebra-axis: classical-shadow column ⊥ quantum-core column) × (Krylov integrability/chaos axis, scale-tagged: bounded-Krylov-PERMANENT row ⊥ linear-Krylov-THERMALIZING-single-cell row). All four cells occupied; the axes transverse (off-diagonal cells I-T and D-P non-empty); neither subsuming the other. S70's Bell-violation is a COLUMN fact (right column occupied ⇒ substrate is quantum ⇒ S58's local-hidden-variable reading falsified); S58's surviving hidden content is a ROW fact (bounded-Krylov row ⇒ permanent), correctly re-scoped from "whole GGE" to "bounded-Krylov row" per the T3-BROKEN repair. The dark-matter relic (LEGGETT-MOMENT-70) is Cell D-P — algebra-DEPENDENT AND bounded-Krylov — the unique two-coordinate cell, which is exactly why neither cleave alone reconciles S58↔S70 and the product does. λ_L = 0 (S104-KRYLOV-KCP, the 4th sign-consistent chaos functional) is the integrable-floor fingerprint that fixes the bounded-Krylov row; the MSS bound λ_L ≤ 2πk_BT/ℏ is satisfied trivially at the floor; kill authority on the framework's scrambling claims is NOT triggered (zero Lyapunov violates no bound — it is the integrable extreme, the opposite of SYK saturation). Verdict: a NAMED DECOMPOSITION (the orthogonal 2×2 stratification), not an obstruction.

---

## Verdict Table

| Sub-question | Structural verdict |
|:-------------|:-------------------|
| (a) Does the S70 Bell-violation FALSIFY S58 superdeterminism, or reconcile via the M2 algebra-INVARIANT⊥algebra-DEPENDENT split? Which substrate quantities land on each side; is the cleave the M2 temperature/entanglement partition (einstein), the integrability/chaos partition (kitaev), or do they coincide? | **RECONCILE-VIA-PRODUCT, NOT COINCIDE.** S70 FALSIFIES the *literal local-hidden-variable* reading of S58 (Bell-violation, S=2.351–2.452 over 8/8 modes, is a column-fact ⇒ substrate is quantum) but does NOT falsify "there exists a deterministic substrate"; it forces the protecting cleave to be a 2×2 PRODUCT. **Neither single partition is the cleave — they CROSS.** ρ_GGE stratifies as (M2 column: algebra-INVARIANT classical-shadow ⊥ algebra-DEPENDENT Bell-capable core) × (Krylov row, scale-tagged: bounded-Krylov PERMANENT ⊥ linear-Krylov THERMALIZING-single-cell). **All four cells occupied; axes orthogonal** (off-diagonal cells non-empty: I-T = single-cell bulk occupation; D-P = Leggett `C`); **neither subsumes the other**. Quantities: **Cell I-P** {R_k} occupation, {T_k} of surviving modes, fabric-scale CG(24) ⟨r⟩=0.367 + 36D Lyapunov=0 (the literal "complete deterministic hidden specification"); **Cell D-P** Leggett-channel concurrence `C` (x_L1=0.149, R-protected, frozen 1e-15/13.8 Gyr) = the DM relic; **Cell I-T** single-cell bulk occupation shadow (CMB-transit spectrum-only); **Cell D-T** single-cell off-diagonal coherences, 63% GOE, mixed_basis_gap=0.337 (INV8-W2-3), Bell-capable at transit but dephased by present epoch (INTEG-39, β=0.633, t_therm≈6 M_KK⁻¹). **Krylov row is operative for permanence (the more load-bearing coordinate; einstein granted, kitaev confirmed via coordinate-sufficiency); M2 column is operative for classical/quantum identity. "More load-bearing ≠ sole": D-P is algebra-DEPENDENT-AND-protected, a two-coordinate cell that BOTH axes are required to name.** Row scale-tag (kitaev R2·B §1): linear-Krylov-THERMALIZING is anchored at SINGLE-CELL (INTEG-39); bounded-Krylov-PERMANENT = Leggett gap-protection ∪ fabric-scale integrability ∪ diabatic transit-freeze (R_therm=5252, S_ent=0) — permanence is fabric-scale-and-freeze, NOT single-cell-thermalization-failure (which is FALSE). λ_L=0 (S104-KRYLOV-KCP, 4th sign-consistent chaos functional) fixes the bounded-Krylov row; MSS bound satisfied trivially at floor; kill authority NOT triggered. |
| (b) IF a classical layer is isolated, is the Born rule derivable FOR it (Gleason + GGE coarse-graining, cross-ref INV8-W2-3) and an INPUT for the entanglement layer — or an input for both? | **INPUT FOR BOTH** — unchanged from INV8-W2-3 (INFO `1d97…42df`; Gleason gives CONSISTENCY only, IF a frame function exists THEN p=Tr(ρ_A P_θ), never DERIVATION). On the grid: the **algebra-INVARIANT column** is where Born "looks derived" but the eigenbasis coincidence (marginal eigenvalues = |ψ|² in the R-eigenbasis, max_dev=0) is *trivial alignment forced by construction*, automatic for ANY diagonal state — NOT a derivation even there. The **algebra-DEPENDENT column** is where the no-go bites: paired marginal MIXED (purity_B2=0.7731), Tr(ρ_A P_θ) and |⟨ψ|θ⟩|² diverge by mixed_basis_gap=0.337 — Born rule a *visible* INPUT. **M2 says which family is irreducible (column); Krylov says WHY the irreducible content is operationally random (row): in a bounded-Krylov sector phase is FROZEN and un-transportable (no operator-growth channel, λ_L=0), so a sub-KK probe reads it as Born randomness, not recoverable phase — contrast SYK where phase scrambles in t_*∼β log S.** No tension; the two reasons COMPOSE. Net: Born rule INPUT for both layers, on the footing of the metric signature (INV8-W2-3's phrase); derivation for NEITHER. Forward (einstein B-2 vantage): candidate frame-function-selection *derivation* = Penrose–Diósi E_G(a₂, band-diff) collapse rate on the a₂/geometry channel — the grid localizes its only viable target to Cell D-P (algebra-DEPENDENT bounded-Krylov relic). |
| (c) Does the resolution redirect the S58 quantum-foundations program (superdeterminism → geometric non-locality), or leave it intact with a scoping caveat? | **REDIRECTED — on BOTH axes (the two redirections COMPOSE, they do not compete).** A Bell-violating relic (S70 operative) is not a local-hidden-variable account; both advocates reject the superdeterministic measurement-independence escape on the standard anti-conspiracy ground. **Column redirection (einstein):** superdeterminism → **geometric non-locality** — the (k,−k) entanglement is a single off-diagonal structure on ONE fabric (one spectral triple), modes at the SAME fiber point (S69 §6c, Δx=0 ⇒ Penrose–Diósi intra-fiber Γ=0); Bell-locality fails because there is no genuine spatial separation, no conspiracy. **Row redirection (kitaev):** "the GGE is permanent" → **sector-resolved-and-scale-resolved permanence** — only the bounded-Krylov row is permanent (T3 "GGE never thermalizes" BROKEN for the single-cell bulk, INTEG-39); the permanent hidden content is the bounded-Krylov row (Leggett gap-protection ∪ fabric-scale integrability ∪ transit-freeze), NOT the whole GGE. **Composition:** S58 §II's "the GGE IS the permanent hidden variable" is rewritten with BOTH scopings — *the bounded-Krylov row of ρ_GGE is the permanent substrate content; within it, Cell I-P ({R_k}, fabric integrals) is the complete deterministic hidden specification of the classical shadow, and Cell D-P (Leggett C) is the irreducibly-quantum, geometrically-non-local, Bell-violating dark-matter relic, with the Born rule as a substrate input for it.* S58's deepest instinct — a sub-KK observer's "quantum indeterminacy" is structurally enforced by inaccessibility (M_KK/E∼10¹³) — SURVIVES and is sharpened twice: what is inaccessible is the algebra-DEPENDENT column content (M2 axis), and for the permanent relic that inaccessibility is dynamically frozen by λ_L=0 (Krylov axis). Scale-gap argument → scale-gap-AND-dynamical-freezing argument. Program redirected, not preserved intact; redirection is two-dimensional. |

---

## Wrap-Up

**STRUCTURAL VERDICT (named decomposition, NOT obstruction): the GGE Orthogonal 2×2 Stratification.**

ρ_GGE = Z⁻¹ exp(−Σ_k λ_k R_k) stratifies as the PRODUCT of two transverse partitions of its observables:

- **M2 algebra-axis (column)** — algebra-INVARIANT spectrum-only family `F({λ_k,m_k})=Σ_k m_k g(λ_k)` (the coarse-grainer-visible classical shadow) ⊥ algebra-DEPENDENT state-pair family on A (the Bell-capable quantum core). Fixed by a *selection rule* on the observable algebra; silent on dynamics.
- **Krylov integrability/chaos axis (row, scale-tagged)** — bounded-Krylov `b_n`-saturating, λ_L=0, PERMANENT ⊥ linear-Krylov `b_n`∼αn, THERMALIZING-single-cell. Fixed by the Lanczos-coefficient growth of the GGE Liouvillian; silent on observable-family identity.

All four cells occupied; the axes are ORTHOGONAL (off-diagonal cells I-T and D-P non-empty — proven by einstein R2·A §1 Steps 1–5, accepted by kitaev R2·B §0); NEITHER subsumes the other (each axis separates a pair the other merges: Krylov→M2 fails because I-P and D-P share a row but differ in column; M2→Krylov fails because D-P and D-T share a column but differ in row).

| | algebra-INVARIANT (classical shadow) | algebra-DEPENDENT (Bell-capable core) |
|:--|:--|:--|
| **bounded-Krylov (λ_L=0; PERMANENT)** | **I-P** {R_k}, {T_k} of surviving modes, fabric-scale CG(24) ⟨r⟩=0.367, 36D Lyapunov=0 — the complete deterministic hidden specification (S58's instinct, exactly right HERE only) | **D-P** Leggett-channel concurrence `C` (x_L1=0.149, frozen 1e-15/13.8 Gyr) = **DM relic, LEGGETT-MOMENT-70**; the unique two-coordinate cell |
| **linear-Krylov (β=0.633 GOE; THERMALIZES-single-cell; t_therm≈6 M_KK⁻¹)** | **I-T** single-cell bulk occupation shadow; CMB-transit spectrum-only content | **D-T** single-cell off-diagonal coherences, 63% GOE, mixed_basis_gap=0.337 — Bell-capable at transit, dephased by present epoch |

The S58↔S70 contradiction dissolves because **S70's Bell-violation is a COLUMN fact** (right column occupied ⇒ substrate quantum ⇒ S58's literal local-hidden-variable reading falsified) and **S58's surviving hidden content is a ROW fact** (bounded-Krylov row ⇒ permanent, re-scoped from "whole GGE" to "bounded-Krylov row" per T3-BROKEN). They were never about the same axis; S58 §II conflated "hidden" (row) with "classical" (column) under one word "GGE". **Neither cleave alone reconciles S58↔S70; the product does.** The dark-matter relic is Cell D-P — algebra-DEPENDENT AND bounded-Krylov — which is precisely why it needs both coordinates: Krylov names that it *survives*; M2 names that the surviving thing is *entanglement, not occupation*.

**Sub-question answers** (full text in the Verdict Table above):
- **(a)** RECONCILE-VIA-PRODUCT, not coincide. The cleave is the 2×2 product of M2 (column) × Krylov (row); axes orthogonal; Krylov-row operative for permanence (more load-bearing), M2-column operative for classical/quantum identity; neither sole. DM relic = Cell D-P.
- **(b)** Born rule INPUT for BOTH layers (INV8-W2-3, Gleason consistency-only, derivation for neither). M2 says which family is irreducible (column); Krylov says why it reads as random (row: frozen un-transportable phase, λ_L=0). The two reasons compose.
- **(c)** REDIRECTED on BOTH axes, composing: column → geometric non-locality (one fabric, Δx=0, no conspiracy); row → sector-and-scale-resolved permanence (bounded-Krylov row, not whole GGE). S58's inaccessibility instinct survives, sharpened from scale-gap to scale-gap-AND-dynamical-freezing.

### What Changed

#### (a) Numerical revisions

- None. No pre-registered numerical threshold was tested or re-pinned in this workshop (investigation-track adjudication; closure is artifact-existence-with-content, NO verdict line). All cited numbers (S=2.351–2.452, λ_L=0, β=0.633, t_therm≈6 M_KK⁻¹, mixed_basis_gap=0.337, x_L1=0.149, R_therm=5252, Mass_LeggettDM/Δ_BCS=11.97) were verified against the canonical graph (knowledge-MCP: atlas-08-freshness-S104, LEGGETT-MOMENT atlas-10, INTEG-39/atlas-04 T3, INV8-W2-3) and carried UNCHANGED — they are inputs to the adjudication, not outputs of it.

#### (b) Structural changes

- **flat S58↔S70 contradiction → orthogonal 2×2 stratification** (named decomposition). The "GGE is a hidden-variable account" (S58 §II) vs "GGE pairs violate CHSH 8/8" (S70) flat clash is reclassified as a two-axis conflation under one word "GGE"; the resolution is the product partition, not a winner between the two readings.
- **"integrability/chaos SUBSUMES M2" (kitaev R1) → "M2 ⊥ Krylov, transverse, neither subsumes" (converged).** kitaev R1 §2/§3 claimed the dynamical cleave files both protected and thermalizing coherences in one M2 corner, retiring M2 as idle; einstein R2·A §1 exhibited Cell D-P (Leggett `C`: algebra-DEPENDENT AND protected) as the counterexample built from kitaev's own R1 row (iii); kitaev R2·B §0 accepted it. Epistemic-TYPE change: the operative cleave is no longer a single axis but a 2-coordinate locator.
- **"M2 is THE reconciliation" (einstein R1 implicit) → "M2 necessary but not sufficient; Krylov necessary but not sufficient; product sufficient" (converged).** Symmetric demotion of both R1 over-reaches via the coordinate-sufficiency test (kitaev R2·B §2): Krylov alone is column-blind (cannot say the relic is entanglement); M2 alone is row-blind (cannot say which entanglement survived).
- **Krylov row gains a SCALE tag** (kitaev R2·B §1): linear-Krylov-THERMALIZING is SINGLE-CELL (INTEG-39); bounded-Krylov-PERMANENT = Leggett gap-protection ∪ fabric-scale integrability ∪ diabatic transit-freeze. The permanence of {R_k}/Leggett is a fabric-scale-and-freeze fact, NOT a single-cell-thermalization-failure (which is FALSE). Prevents the grid from being mis-read as a single-scale same-Liouvillian claim with opposite verdicts.
- **S58 superdeterminism → two-dimensional redirect** (geometric non-locality [column] + sector-and-scale-resolved permanence [row], composing). Epistemic-TYPE change: the redirect is not a single replacement but a product of two orthogonal redirections.

### Effected In-Session

- [x] R2·Turn B authored — rebuttal-accept of einstein R2·A §1 chain + scale-axis refinement + "more load-bearing ≠ sole" adjudication via coordinate-sufficiency — `sessions/investigation/investigation-8/workshops/inv8-w4-1-bell-vs-hidden-variable.md` — `### R2 · Turn B`
- [x] Verdict Table filled — all three sub-question rows (a)(b)(c) with the derived 2×2 structural position — `…/inv8-w4-1-bell-vs-hidden-variable.md` — `## Verdict Table`
- [x] Wrap-Up filled — structural-verdict statement (GGE Orthogonal 2×2 Stratification) + occupied-grid table + three sub-question summaries — `…/inv8-w4-1-bell-vs-hidden-variable.md` — `## Wrap-Up`
- [x] Load-bearing numbers verified against canonical graph before landing (no drift; all carried unchanged) — knowledge-MCP `search_knowledge` ×4 — S104-KRYLOV-KCP `e134597f` / LEGGETT-MOMENT-70 PROVEN / INTEG-39 DECISIVE-FAIL single-cell / INV8-W2-3 `1d97…42df`

No other in-session edits are appropriate: the verdict is a structural adjudication, not a registry-state change. Promotion of the 2×2 stratification to a permanent registry entry (if pursued) and the discriminating compute below route to session-promotion / carry-forward, because investigation-track results enter the knowledge index only when lifted into a session-mode `/rclab-plan` and re-computed under a `session-{N}` gate (`gate-verdicts.md §"Investigation-Track Canonical Path"` track-local boundary).

### Carry-Forward Computations

**CF-1 — GGE reduced-density-matrix entanglement-vs-thermal partition (the discriminating compute that numerically confirms the 2×2 cell assignments).**
1. **What**: For each of the 8 (k,−k) GGE pair modes, compute the two-mode reduced density matrix ρ_k from the post-transit BCS amplitudes (u_k, v_k); decompose each mode's content into (i) thermal/occupation part (diagonal {n_k}=|v_k|², the would-be Cell-I content) and (ii) entanglement part (off-diagonal anomalous correlator ⟨c_k c_{−k}⟩=u_k v_k, concurrence C_k, the Cell-D content); cross-tabulate against each mode's Krylov fate (bounded vs linear `b_n` growth from the per-mode Liouvillian) to populate the 2×2 grid mode-by-mode and verify all four cells are non-empty with the predicted occupants (Leggett channel → D-P; bulk single-cell modes → I-T/D-T; conserved {R_k}/fabric integrals → I-P). Confirms numerically that M2-membership and Krylov-fate are statistically independent (axes transverse) across the mode set, not merely at the two anchor cells named in the workshop.
2. **Inputs**: `s70_bell_gge.npz` (u_k, v_k, C_k, S_max per mode); `s104_krylov_kcp.npz` (Lanczos `b_n` per sector, λ_L); `s100b_w4_dk_ergodicity.py` single-cell INTEG-39 spectrum (β=0.633, Thouless g); INV8-W2-3 no-go script outputs (purity_B2=0.7731, mixed_basis_gap=0.337); Leggett-channel x_L1=0.149 (S58 dynamic structure factor / atlas-04 C11); canonical_constants.py (Δ_BCS, M_KK).
3. **Gate**: PASS iff (i) all four product cells are non-empty with the workshop-predicted occupants AND (ii) per-mode M2-membership (concurrence-nonzero vs occupation-only) is uncorrelated with per-mode Krylov-fate (bounded vs linear) at a pre-registered |Spearman ρ| < 0.3 threshold (axes statistically transverse, not coincident); INFO iff cells populate as predicted but the independence metric lands in [0.3, 0.6] (partial correlation — would weaken but not break orthogonality); FAIL iff any predicted cell is empty OR |ρ| > 0.6 (axes would then be effectively one, collapsing the 2×2 to a 1D cleave and re-opening the S58↔S70 adjudication).
4. **Effort**: Low–medium. All input .npz files exist; the compute is per-mode 2-qubit RDM diagonalization (4×4, trivial) + a Lanczos-coefficient read-off already cached + one Spearman correlation over 8 modes. Single script, single GPU-unnecessary pass (matrices are 4×4); ~1 agent-slot. Route via session-mode `/rclab-plan` (investigation→session promotion) so the verdict enters the knowledge index.

**Residual disagreement (recorded honestly per `epistemic-discipline.md`)**: none of substance. The only residual is one of EMPHASIS that both advocates explicitly agreed to (einstein R2·A §4 / kitaev R2·B §2): the Krylov row is "more load-bearing" for the framework's marketed permanence/DM physics, while M2 is "more load-bearing" for the classical/quantum-identity question — but both concur this is an ordering-by-application, NOT a claim that either axis is sufficient alone. CF-1 is the falsifier that would convert this converged structural position into a numerically-anchored one (or break it, if the independence gate FAILs).
