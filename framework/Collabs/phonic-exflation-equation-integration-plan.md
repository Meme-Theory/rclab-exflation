# Phonon-Exflation Equation — Consolidated Review-Integration Plan

**Date**: 2026-05-28
**Synthesized from**: the 10-domain collab panel on `sessions/framework/phonic-exflation-equation.md` (commit 5e5d5fa9) — reviews by hawking, quantum-foam, tesla, einstein, transit, mack, kaku, sp (Schwarzschild–Penrose), volovik, nazarewicz (`Collabs/phonic-exflation-equation-*-collab.md`).
**Purpose**: A complete, deduplicated, cross-referenced list of every review suggestion/recommendation/change, organized by target section of the master, tagged by priority and reviewer, with conflicts and computational carry-forwards separated out.

**Scope note**: No reviewer re-adjudicated any PROVEN/CERTIFIED/PASS/FAIL verdict; all confirmed the document's gate statuses against the knowledge MCP. The einstein/feynman *Round-2* patches are already folded into the master (verification ledger, line 508); the `einstein-collab.md` reviewed here is a **separate, later, full review** and its items are pending.

**Priority key**:
- **REQUIRED** — factual/sourcing/ledger defect; must fix before the doc is cited as canonical.
- **CONFLICT** — reviewers disagree, or a claim conflicts with canon; adjudicate before integrating.
- **STRONG** — closes a seam a referee will predictably probe.
- **STRENGTHEN** — additive; sharpens an already-correct claim (ties a claim to a theorem, names a mechanism). Most items are here.
- **OPTIONAL** — nice-to-have.

"[drop-in text]" = the reviewer supplied exact verbiage; pull it verbatim from the cited review section.

---

## A. The short list — what is NOT optional

| # | Item | Source | Why |
|:--|:-----|:-------|:----|
| **A1** | **§7.1 dark-energy `w₀`/`wₐ` anchors must be sourced to ONE joint `(w₀,wₐ)` posterior with declared provenance** + a "1D-marginal-vs-2D-rectangle" footnote. | mack §2 (the one REQUIRED fix) | The two rows currently cite *different* compilations (`−0.803±0.054` vs `−0.72±0.21`); a `w₀`/`wₐ` pair must come from one fit (`ρ≈−0.85`). Quoting marginals from two fits and reading either σ as a tension is the recurring failure mode. Arithmetic against the printed anchor is internally correct — the **label/sourcing** is the defect. |
| **A2** | **§5.3 Ordered Veil: drop the `t_therm/t_Hubble ∼ 9×10⁻⁴⁸` figure and the "permanent integrability" claim; replace with transit-timescale diabatic freeze-out** (`t_scr/t_transit = 814`; `t_therm/t_transit ≈ 5×10³` from S39 `t_therm≈6 M_KK⁻¹`). | volovik R1 (DECISIVE) + nazarewicz R4 | **Ledger dissonance**: Richardson–Gaudin *integrability permanence* was RETRACTED at S39 (13% non-separable density–density channel, Brody β=0.633); the doc presents it as PROVEN. The surviving claim is the S38 transit-freeze. `t_Hubble` is also the container clock §6.3 forbids, and the ratio is undefined until the `t(τ)` map closes. [drop-in text: volovik R1/R2] |
| **A3** | **§6.2 white-hole structure — adjudicate symmetric-two-horizon vs asymmetric-one-horizon-+-open-exit** (see Conflict C1). | sp III.A/V.3 vs current doc + tesla/transit/hawking | sp (causal-structure specialist) says the current symmetric table conflicts with canonical S74 "Entry Horizon, **Open** Exit" + AUDIT-74. Other reviewers treat the two-horizon reading as given. Must resolve before §6.2 is re-cited. |
| **A4** | **Add PROVENANCE entries for `w0_FW` and `M_KK`** to the knowledge MCP (`update_constant`). | quantum-foam, sp, tesla, mack, volovik, hawking, einstein, nazarewicz (8/10 confirmed independently via MCP) | The document's own verification-ledger flag (line 506) is correct; both constants carry values but "No PROVENANCE entry." `w0_FW` binds Falsifier #1 (DESI DR3). Hygiene, not physics — but route before DESI DR3. (Carry-forward, not a doc edit.) |

---

## B. Conflicts requiring adjudication BEFORE integration

### C1 — §6.2: symmetric two-horizon vs asymmetric white hole (the highest-value physics-structural item)
- **sp (III.A, V.3)**: the canonical S74 result is **"Asymmetric Fold: Entry Horizon, OPEN Exit"** (AUDIT-74). There is ONE sonic horizon (the entry/white-hole surface, `τ≈0.22`, `a₂`-kinematic, `T_H≈72.8 M_KK`); the exit is an **open expulsion region**. The "exit horizon τ∼0.16 (`a₄`)" in the current table conflates a *thermodynamic* BCS-window edge (`τ≈0.235`) and a decoherence scale (`τ∼0.16`) with a second *sonic* horizon that canon says does not exist. sp wants the table redrawn as asymmetric + the ingoing-null-ray direction stated.
- **Counter-weight**: tesla (II.5), transit (II.3), hawking (II.3) all discuss the **two-horizon** (`a₂` entry / `a₄` exit) reading approvingly, treating the current table as given, and offer additions (surface-gravity origins, greybody, Wronskian-licensing) that *presuppose* two horizons.
- **Resolution needed**: Is the exit a second sonic horizon or an open expulsion region with thermodynamic features inside it? sp is the domain owner and cites canon + an audit; the others build on the doc's existing wording. This is a genuine ledger-vs-presentation adjudication (an `/rclab-review` or 2-agent workshop between sp and transit/hawking would settle it). Until resolved, the §6.2 additions (B-C2, and the §6.2 items in §C below) are contingent on which structure wins.

### C2 — §5.3: how much to build on the Ordered Veil's integrability
- **volovik (R1)**: integrability *permanence* is RETRACTED (S39); attribute survival to **diabatic transit-freeze**, not integrability.
- **nazarewicz (R4)**: bridges — the *pairing-channel* (Richardson–Gaudin) integrability survived; only the *full* `D_K` dynamics is weakly chaotic (Brody 0.633). Attribute non-thermalization to the **pairing channel specifically**.
- **hawking (II.2)**: wants to *expand* the Ordered Veil into an "analog information-paradox resolution" paragraph (unitarity + `S_ent=0` + no Page curve) — which rests on the purity/non-scrambling claim.
- **kaku (II.5), quantum-foam (IV.1)**: cite the existing "never thermalizes" form approvingly (non-stringy reheating; topology-survives-dissolution).
- **Resolution**: These are reconcilable. The surviving, correct claim is **`S_ent=0` product state + diabatic transit-freeze + pairing-channel integrability**; what dies is "permanent integrability of the full dynamics" and the `t_Hubble` number. Hawking's info-paradox paragraph **can stand if reworded** to rest on `S_ent=0` + transit-freeze (not permanent integrability). Integrate A2 first, then graft hawking's paragraph onto the corrected base.

---

## C. Suggestions by target section (the integration map)

### §0 — container disarming / pillars
- **STRENGTHEN** (einstein II.1): name the methodology a **"principle theory"** (Einstein 1919 principle-vs-constructive distinction) — short free-parameter ledger is by construction; open inputs (`τ`, `f`, family number) are *permitted*, not defects. [drop-in text: einstein §II.1]
- **STRENGTHEN** (volovik R6, optional): after "Newton's constant carries zero τ-dependence," add the superfluid-compressibility reading (`1/G` = vacuum gradient stiffness; TT/volume-preserving deformation is a pure shear → compressibility, hence `G`, invariant). [drop-in text: volovik R6] — may live in §0 or §8.3.
- **STRENGTHEN** (volovik II.4): surface "`N₃=0` ⇒ q-theory-relaxation, not topological-protection" as an explicit **strength** (the reason the CC is solvable-in-principle), not buried in §0 prose.

### §1 / §1.1 — the equation, "why one functional"
- **STRENGTHEN** (kaku R1): after the "no room for a third term" sentence, **name the genre as matrix-model/IKKT (not string field theory)** and claim the virtue — emergent geometry is bit-computable on a finite triple, *without* the string Hagedorn tower or `10⁵⁰⁰` landscape; the trace+inner-product exhaustion is cleaner than SFT's cubic-vertex completeness. [drop-in text: kaku R1]
- **STRENGTHEN** (kaku II.4): let the KO=6/Pfaffian story claim its positive parallel — "why KO=6" plays the role of "why D=10" (consistency condition on the fermionic sector); the product-KO mismatch does *constructive* work (level-matching analog). Narrative, no new claim.

### §1.3a — bare action / partition weight / no interior saddle
This section is the single biggest convergence of *additive* enrichments (5 reviewers):
- **STRENGTHEN** (kaku R2): make the **landscape contrast** explicit — a monotone weight `e^{−S(τ)}` has no competing interior minima, so the CC problem is vacuum-*subtraction*+adiabaticity, not vacuum-*selection*; "no landscape" and "no stabilizing well" are two faces of E7. [drop-in text: kaku R2]
- **STRENGTHEN** (hawking II.5): add the **GHY boundary-dominated** reading — an action with no interior stationary point is dominated by its boundary configuration (genesis `τ=0`); the transit is the relaxation of that boundary configuration, making "transit not slow-roll" structurally inevitable. [drop-in text: hawking II.5]
- **STRENGTHEN** (quantum-foam II.4): add that the **conformal-factor instability** (which makes the naive Euclidean gravity path integral unbounded below) is a container artifact, absent here because the deformation is volume-preserving TT (G6). [drop-in text: quantum-foam II.4]
- **STRENGTHEN** (hawking II.1): one clause on *whose temperature* — the `F=−T ln Z` face uses the substrate's own inverse-Euclidean-period temperature, not a thermal-bath `T`; there is no Gibbsian `T` until something thermalizes, and nothing does. [drop-in text: hawking II.1]
- **STRENGTHEN** (volovik R3): **distinguish the two monotonicity theorems** — τ-flow (E7, `dS/dτ>0`, geometric modulus, → transit) vs q-flow equilibrium (S62, `dE_ZP/dq>0`, conserved vacuum charge, → the CC layer). Two axes, two theorems, both proven; the CC story rests on the *q-flow* one. [drop-in text: volovik R3] (also touches §5.1, §7.1)
- **STRENGTHEN** (einstein II.2): pin that the boundary-domination reading is a **tree-level / leading-order saddle** statement; the assertion that one loop (`½Tr ln(D_K²/Λ²)`) introduces no interior feature is a separately-defensible claim-with-a-regime, not an identity. (Cross-link to computation E-V.3.)

### §1.4 / §8.4 — free-parameter ledger
- **STRENGTHEN** (kaku IV.2): the matrix-model genre statement *explains why the ledger is short* — field content is read off the algebra, not chosen among vacua; converts the "1→60 collapse" from a counting claim into a structural one.
- **(contingent)** (kaku V.1): if the `t*`-one-loop computation (E-K1) succeeds, drop `t*` from the ledger → `{τ, Λ, f₀, f₂, f₄}` only.

### §2 / §2.2 — operator and modulus
- **STRENGTHEN/OPTIONAL** (nazarewicz R6): note block-diagonality (E6) is the **SU(3) analog of `j`-channel decoupling** in a spherical mean field — which is *why* the §5.3 relic-formation factorizes mode-by-mode *exactly* (not approximately). Lets §5.3 lean harder on E6. [drop-in text: nazarewicz §2]

### §3 / §3.2 / §3.3 — functional `f`, FI/RD partition, convergence cone
- **STRENGTHEN** (nazarewicz R3): name the FI/RD partition as a **marginalization over the nuisance functional `f`** (Bayesian model averaging); cite the framework's own S67 **BMA `n_s = 0.969 ± 0.022`** alongside the three scheme-specific values. The BMA band is the correct UQ object and is *stronger* than three rival points. (Also §7.1.) [drop-in text: nazarewicz §3]
- **STRENGTHEN** (nazarewicz §3 discipline note): state explicitly that the **anomaly family is excluded *structurally* (S67), not because it gave the wrong tilt** — pre-registration protects against the over-fitting charge.
- **STRENGTHEN** (tesla V.3): add the **acoustic-envelope** reading of `f*∼√x` — `f(ω²)∼|ω|` up-weights the low acoustic (B1) modes; this is why the direct sum is acoustic-band-dominated and why the heat-kernel (Gaussian-adapted) series cannot represent it; the Mellin divergence is the signature that the physical envelope is acoustic. [drop-in text: tesla V.3]
- **STRENGTHEN** (quantum-foam II.1): add one substrate-first sentence to §3.3 — the dimension spectrum `S_d={0,2,4,6,8}` makes the cone close after `a₈`; the substrate hands a *finite pole ladder*, not a Wheeler-superspace sum, so the CC freedom is exactly one functional's worth. [drop-in text: quantum-foam II.1]
- **STRENGTHEN** (kaku R3): add a **defensive sentence pinning the silence on spectral-dimension flow** — `S_d` is τ-independent; no CDT-like UV reduction (`d_s∼8` at the gap, S31Aa); apparent low-`d_s` is a windowed-observable artifact (S92). Prevents a future reader reading a string/CDT dimension-flow into §2.2. [drop-in text: kaku R3] (may live in §3.3 or §8.5)

### §4 / §4.2 — Seeley–DeWitt layers, Wronskian
- **STRENGTHEN** (tesla V.2): add the **dispersion-rigidity** reading — `a₀,a₂,a₄` are the 0th/1st/2nd moments of the single curvature scalar `R_K`; `W[{1,R_K,R_K²}] ∝ (R_K′)³` because distinct powers of a *moving* scalar are independent; collapse happens iff the dispersion stops moving (`R_K′=0`, only at `τ=0`) — the same band-lifting §2.4 describes, restated at moment level. [drop-in text: tesla V.2]
- **OPTIONAL** (nazarewicz §4): one sentence tying it to the **Strutinsky smooth/shell-correction** independence (degree-distinct moments are independent functionals; S44/S55/S56). Independent structural concurrence, not evidence.

### §5.1 — the driver / no potential well
- **STRENGTHEN** (transit V.7): inline the **"why `r=16ε` fails"** reason — it is a theorem of the single-clock adiabatic vacuum (`c_s=1`, single-field, slowly-varying); the fold violates all three premises (diabatic, BdG `c_s≠1`, multi-mode squeezed GGE), so the relation's derivation assumptions are *absent*, not merely "gives the wrong number." Pre-empts the most common objection. [drop-in text: transit V.7]
- (volovik R3 τ-flow/q-flow distinction also lands here — see §1.3a.)

### §5.2 — trajectory / transit
- (No new edits beyond the §6.2-adjacent conflation guards, which the doc already handles; tesla/transit/nazarewicz all explicitly endorse keeping the Mach 13.75 vs 421.3 vs 54.3 guard verbatim.)
- **STRENGTHEN** (sp V.1): restate the **genesis-singularity claim (§5.2(i), also §9)** as a **cosmic-censorship** statement — genesis at `τ=0` is regular (no singularity), but the genuine curvature singularity is at `τ→∞`, is anisotropic (timelike in SU(2), spacelike in ℂ²/U(1)), and is *censored* (triple-layer barrier below, COSMIC-CENSORSHIP-49; overshoot turnaround `τ=1.614` above). "No `t=0` singularity" over-sells; the censorship statement is stronger. [drop-in text: sp V.1]

### §5.3 — GGE relic / Ordered Veil  *(the most-targeted section)*
- **REQUIRED** (volovik R1 + nazarewicz R4): **the A2 correction** — replace permanent-integrability + `t_Hubble` with transit-freeze + pairing-channel integrability. See A2 / Conflict C2. [drop-in text: volovik R1]
- **STRONG** (nazarewicz R1): surface the **60% PBCS gap overestimate (S46, B4 CONDITIONAL) and ~225× Richardson–Gaudin condensation-energy overestimate (S63) AT the `N_pair=59.8` count**, not as a trailing parenthetical. State `P_exc=1` (regime-robust) carries the structural claim; `59.8` is a *projected charge* inheriting the BCS-projection caveat, not a literal pair count. [drop-in text: nazarewicz R1]
- **STRONG** (transit V.1, Gap #1): **print BOTH mode equations** — substrate-BdG `u_k″+ω_k²u_k=0` (relic content) AND Mukhanov–Sasaki `v_k″+(k²−z″/z)v_k=0` (emergent curvature, §7's `A_s`); label the layers; state the squeeze is *transduced* from the first into the second at the exit horizon. Prevents attributing `A_s` to the BdG `u_k` (the exact layer-confusion the framing law exists to prevent). [drop-in text: transit V.1]
- **STRENGTHEN** (hawking II.2, MAJOR): add an **information-paradox-resolution paragraph** — the transit is a unitary Bogoliubov transformation; a thermal relic would scramble it (hide the squeeze phase like Hawking flux hides infalling info); the `S_ent=0` GGE retains the phase data → no Page curve, no horizon-entropy debt. [drop-in text: hawking II.2] *(reword to rest on `S_ent=0`+transit-freeze per C2.)*
- **STRENGTHEN** (hawking II.2): one-line **bosonic-normalization footnote** at `N_pair=59.8` — `|α_k|²−|β_k|²=1`, `n_k=|β_k|²`, GGE multipliers conjugate to conserved charges (not energy), diabatic `P_exc→1` is the maximal-mixing regime. [drop-in text: hawking II.2]
- **STRENGTHEN** (sp V.2): add the **extremal-horizon (κ=0, T_H=0) origin** of the Ordered Veil — `τ_fold=0.190` is a double-root extremal Killing horizon; zero Hawking temperature is the *geometric* corroboration of "never thermalizes," independent of the integrability argument. [drop-in text: sp V.2] *(note: this is an independent leg that survives the C2 correction — useful precisely because it does not depend on integrability.)*

### §6.2 — acoustic white-hole causal structure  *(contingent on Conflict C1)*
- **CONFLICT** (sp V.3): redraw as **asymmetric white hole** (one entry horizon + open exit). See C1. [drop-in text: sp V.3]
- **STRONG** (sp V.4): add the **bi-metric / sector-dependence** sentence — by [T3] (Scalar-Tensor Kasparov decoupling, β_T=0 exactly, PERMANENT) the acoustic white hole is a *scalar-sector* structure; the **tensor sector crosses the fold freely** on `g_M`. Exflation carries **two null cones**; the horizon problem is resolved for the observed scalar sector only. Cross-link to §7's scalar (`n_s`,`A_s`) vs tensor (`r`,`n_T`) split. sp calls this the **highest-value causal-structure fix**. [drop-in text: sp V.4]
- **STRENGTHEN** (hawking II.3): **reconcile the three corpus analog temperatures** (`0.112`/`7.578`/`72.8 M_KK`) via the surface-gravity formula `T_a=ħκ/2π`, `κ=½∂_n(c²−v²)`; state each `T` is the SG of its own Mach-1 surface; place or retire the S63 `0.112 M_KK` value. [drop-in text: hawking II.3] (also computation H-V1)
- **STRENGTHEN** (hawking II.3): name the **analog greybody factor** `Γ(ω)` at the exit horizon — escaping `A_s` = produced squeeze × exit greybody. (Explicitly *not* the retracted S73B dispersive-group-velocity mechanism — only the model-independent transmission filter.) [drop-in text: hawking II.3]
- **STRENGTHEN** (transit V.6): cross-link the two-horizon structure to the **Wronskian decoupling theorem** — entry (`a₂`) and exit (`a₄`) horizons are genuinely distinct *because* `a₂`,`a₄` are algebraically independent (§4.2); the structure is licensed, not an accidental double-count. [drop-in text: transit V.6] *(contingent: only if C1 keeps two horizons.)*
- **STRENGTHEN** (transit II.3): add an **"analog/surface-gravity temperature"** guard to the §6.2 table header so `7.578 M_KK` is not misread as a reheating temperature.
- **OPTIONAL** (sp III.C): if a causal-structure/CMPP box is ever added, cite the **a₂-reduced D→G→D Petrov type** (PERMANENT, S84-W8B-95), never the Euclidean-fiber Type II artifact.
- **KEEP** (kaku IV.4.3): retain the **PRELIMINARY** tag on the six-stratum enumeration; the two-horizon (or, per C1, entry+exit) structure is the robust claim, the six-fold partition is narrative.

### §6.3 — the honest `a(t)` gap  *(all reviewers endorse the honesty; all add a complementary lens)*
- **STRENGTHEN (MOST CONSEQUENTIAL — einstein III.2)**: cross-link **frontiers #1 and #8 as ONE gap** — a generally-covariant emergent 4D action for `g_M` is simultaneously (a) the effective Friedmann map, (b) the emergent equivalence principle, (c) the emergent Einstein–Infeld–Hoffmann theorem. The framework already holds EIH on the *internal* `K` geometry; what is owed is its lift to the *emergent* `g_M`. Reduces the open frontier's dimensionality. [drop-in text: einstein III.2] (also §9 frontier #8.)
- **STRENGTHEN** (transit V.5): recast the gap as a **back-reaction-closure gap** — the kinematics (local sweep rate, full Bogoliubov spectrum) are in hand; what is missing is the produced-quanta → global-expansion-rate feedback (`H²=f(ρ_relic, S_SA)`), not "a Friedmann equation." Sharpens *what kind of computation* closes C2/T6. [drop-in text: transit V.5]
- **STRENGTHEN** (hawking II.4): add the **Jacobson (1995) equation-of-state** reading — the Friedmann equation is an equation of state of the emergent metric, derivable from horizon thermodynamics but not fundamental; a substrate theory is *expected* not to contain a fundamental Friedmann equation. Converts the gap from apology to a theorem-backed derivation target. [drop-in text: hawking II.4]
- **STRENGTHEN** (kaku R4): frame the gap as **structural-to-genre** — any background-independent one-functional theory (SFT included) has the same unclosed gap between master action and derived time-dependent background. Not a local failure of effort. [drop-in text: kaku R4]
- **SUPPORT** (nazarewicz §6): the T6 break is **structurally expected** — pairing does not source the bulk geometry, exactly as the nuclear total energy is dominated by the mean field, not the pairing energy. No change needed; corroborates the existing `|E_BCS|/S_fold=3×10⁻⁷` statement.

### §7.1 — the data table + substrate-readings + boxes  *(the most-touched section)*
- **REQUIRED** (mack §2): A1 — joint `(w₀,wₐ)` posterior + provenance + marginal-vs-rectangle footnote. [drop-in text: mack §2]
- **STRONG** (mack §5): **dagger every row that consumes the external FRW `H(t)`** — `w₀†`, `wₐ†`, `σ₈†`, `CC closure†` — with one footnote making §7.1 self-consistent with §6.3 (spectral *value* from `D_K`; *cosmological evaluation* borrows `H(t)`). Bulletproofs against the "you borrowed ΛCDM" referee objection. [drop-in text: mack §5]
- **STRONG** (mack §5): add a caption note that **`n_s`, `r`, `α_s` are quoted at the CMB pivot via the transport map**, not at the substrate/BZ scale (the 54-decade category error the framework has closed but the table doesn't restate).
- **STRONG** (nazarewicz R2): add **LEGGETT-GRAV-DECAY-67 (CRITICAL)** as a stated conditional on the `Ω_DM h²=0.120` PASS — PASS *given* `Γ_grav < H_0`; if exceeded, the DM sector collapses and `0.120` is meaningless. Currently absent. [drop-in text: nazarewicz R2]
- **STRONG** (mack §3.2): promote the **260σ full-DM over-closure + structural `σ/m=0`** from parenthetical to a substrate-readings sentence — the geometry does *not* permit DM-abundance tuning (a stronger Bayesian statement than "0.7σ PASS"). [drop-in text: mack §3.2]
- **STRENGTHEN** (volovik R5): replace Leggett-DM **"integrability-protected"** with **"superselection-protected (`N_pair` conserved, no annihilation channel) and momentum-flux-free (`T^{0i}=0` exact)"** — the mechanism is superselection, not the (S39-broken) integrability. [drop-in text: volovik R5] (same S39 caveat as A2.)
- **STRONG** (mack §3.3) + (kaku R5) + (nazarewicz R5): **α_s row/box** — three convergent edits:
  - mack: change the *table-cell* status from "RESOLVED" to **"RESOLVED-AS-CHANNEL-ARTIFACT; pivot +0.67σ consistent; substrate value −0.0859 → CMB-S4 falsifier"** (don't compress to a checkmark-like word).
  - kaku: pin the substrate-distance value **`−0.08587279` as frozen-now and FI-protected** (regulator-invariant `s=3` Mellin ratio) so it cannot drift to meet CMB-S4. [drop-in text: kaku R5]
  - nazarewicz: state explicitly that **`deg(T_{BZ→pivot})=+2` is *derived, not chosen*** (parallel to the "anomaly family excluded structurally" discipline), inoculating against the channel-selection over-fitting charge.
- **STRENGTHEN** (transit V.2 + nazarewicz R7): **disambiguate the two `N_pair` readings** in the `σ/m` row — change `(N_pair=1)` to `(N_Fock=1; ⟨Q⟩_GGE=59.8, see §5.3)`; nazarewicz adds a one-clause cross-ref that this is the *same* exact reduction carrying the relic charge. The §8.2-style firewall applied to `N_pair`. [drop-in text: transit V.2]
- **STRENGTHEN** (transit V.3): **add an `f_NL` row** — framework `|f_NL|≲1.5` (Bogoliubov-Gaussian, squeezed vacuum Gaussian by Wick) vs Planck `−0.9±5.1`, PASS-class/structural. A computed, zero-parameter consistency result the doc owns but doesn't display. [drop-in text: transit V.3]
- **STRENGTHEN** (transit V.4): **footnote the primordial `α_s=0`** Bogoliubov-saturation origin in the α_s box (`P_exc=1` freezes the spectrum; CMB `α_s` is Phase-2 isocurvature transfer). [drop-in text: transit V.4]
- **STRENGTHEN** (volovik R4 + hawking II.4 + einstein II.4): **CC caveat box** — three convergent additions:
  - volovik: add the **equilibrium-theorem warrant** (`dε/dq=μ ⇒ ρ_Λ=0` at equilibrium; the ground-state energy doesn't gravitate; the 114-OOM catastrophe is a container-EFT artifact — the substrate has its UV completion, so the only question is the non-equilibrium residual). The "vacuum-energy test" the framework passes. [drop-in text: volovik R4]
  - hawking: identify the tracking law `ρ_vac∼M_Pl²H²` as the **de Sitter horizon energy density** (`H/2π=T_dS`) — the substrate tracks its own emergent dS horizon. [drop-in text: hawking II.4]
  - einstein: **separate the CC term's LOCATION (permanent — the `a₀` moment) from its MAGNITUDE (open — relaxation dynamics, SDW gate)**. The 114-OOM problem is a relaxation gap, not an origin gap. [drop-in text: einstein II.4] (may live in §8.5/§9 #6.)
- **STRENGTHEN** (mack §3.1): **σ₈ wording** — change "VIABLE (in the tension gap)" to "VIABLE — sits ~2σ between CMB-primary (0.829) and lensing (~0.76); compatible with the S₈ tension, not a resolution of it." [drop-in text: mack §3.1]
- **STRENGTHEN** (mack §7.1 glossary): add a footnote — **"`α_s` here = scalar spectral-index running `dn_s/d ln k`, NOT the QCD strong coupling"** (the symbol is overloaded 3 ways across the corpus).
- **STRENGTHEN** (mack §7.2): **`n_s` row** — print the per-value σ-distances (`0.9595→1.29σ`, `0.9590→1.40σ`, `0.9561→2.10σ`); recheck the "1.4–2.1σ" range floor (the `0.9595` value is `1.29σ`, below the stated floor — clarify which value the 1.4 refers to). Pairs with the BMA recommendation (nazarewicz R3).
- **STRENGTHEN** (mack §7.3): **`m_H` row** — state the comparison in the framework's ~2% theory error budget, not PDG's 0.17 GeV (else a referee computes a spurious 13σ against a band not claiming 0.17 GeV precision).

### §7.2 — falsifier anchors
- **STRENGTHEN** (kaku R5): see α_s above — pin `−0.08587279` frozen + FI-protected at row #3. [drop-in text: kaku R5]
- **STRENGTHEN** (mack §7.4): **Falsifier #2** — clarify `n_T=−r/8` is the **CMB-transferred** tensor consistency (S66), *not* the slow-roll relation (which is inapplicable at the fold).
- **OPTIONAL/doc-adjacent** (quantum-foam V.3): add an **`α_LIV=0` "NULL-by-construction" row** documenting the framework's structural immunity to LIV/foam-dispersion falsifiers (LHAASO infinite margin, GQuEST-null). → routes to `falsifier-master-inventory.md` (mack sole writer), not the capstone table itself.

### §7.3 — the honest scorecard
- **STRENGTHEN** (mack §6): **tighten the joint-probability argument** — change "product of the individual improbabilities" to "product **across distinct spectral-moment layers** (`a₀×a₂×a₄`, independent by the Decoupling Theorem); within a single layer (`Ω_DM` and `σ₈`, both `a₂`-channel) the observables share a geometric origin and must not be multiplied as independent." Grounds the independence claim in the §4.2 Wronskian theorem. [drop-in text: mack §6]

### §8.3 — derived scales / dictionary
- **STRENGTHEN** (mack §7.5): note `f₂≈92` is **not a free knob** — it is fixed by the `M_Pl/M_KK` ratio once `a₂^ζ` is pinned, so it adds no fitting DOF (can't absorb a `σ₈` or `G_N` discrepancy).
- (einstein IV.4 re-verifies the `f₂≈92` patch and the "don't cite the `f₂=1` match as a gravity prediction (circular)" caveat — already honored; no change.)
- (volovik R6 compressibility reading may land here instead of §0.)

### §8.5 — residual risk / SDW convergence
- **STRENGTHEN** (quantum-foam II.3/V.2): cross-reference so **SDW convergence (frontier #6) is shown as the open gate *underneath* the CC closure (frontier #5)** — the `1.032` PASS is a truncation-robust *ratio* statement; promoting any *absolute* `a₀`-magnitude awaits convergence. One conditional, not two. [drop-in text: quantum-foam II.3] (also §9.)
- (einstein II.4 location-vs-magnitude and kaku R3 spectral-dimension defensive sentence may also land here.)

### §9 — faces table + open frontiers
- **REQUIRED** (volovik R2): **"At τ" face row** — append "the Ordered Veil — *transit-timescale freeze-out*, not integrability permanence; cf. S39 retraction." [drop-in text: volovik R2] (mirror of A2.)
- **STRENGTHEN (MOST CONSEQUENTIAL — einstein III.2)**: **frontier #8** — state it is *not* separate from frontier #1 (one gap: generally-covariant emergent `g_M` action). [drop-in text: einstein III.2]
- **STRENGTHEN** (quantum-foam II.2): **frontier #8** — add a clause on *why* the framework is immune to LIV/foam-dispersion tests (internal discreteness + continuous emergent metric ⇒ `α_LIV=0` exactly; the open item is higher-order emergent isotropy, INFO). Converts silence into stated strength. [drop-in text: quantum-foam II.2]
- **STRENGTHEN** (einstein III.4): **"At time t" summary row** — tighten "τ is a derived monotone clock; C1 postulates τ=cosmic time" to prevent the over-reading "derived cosmic time": "τ is a derived monotone *parameter* (E7); that this parameter *is* cosmic time, and the global rate `τ̇(τ)`, are postulated/undetermined (C1)." [drop-in text: einstein III.4]
- **STRENGTHEN** (sp V.1): mirror the cosmic-censorship restatement of the genesis-singularity claim here (§9 references it). [drop-in text: sp V.1]
- **STRENGTHEN** (quantum-foam V.1): make the **geometry/topology dichotomy** explicit (here or §0) — topological/representation-theoretic outputs (GGE relic, BDI class, CPT, layer-independence, FI ratios) survive spectral-triple continuum dissolution (T3-S43-SPECTRAL-DISSOLUTION, `ε_c∼N⁻⁰·⁴⁵⁷`); absolute geometric magnitudes (CC magnitude, `a_n` absolutes, `a(t)`) are conditional. The deepest available defense of the claim. [drop-in text: quantum-foam IV.1]
- **STRENGTHEN** (einstein II.4): location-vs-magnitude separation at frontier #6 (see §7.1/§8.5).

### Verification ledger
- **REQUIRED/hygiene** (A4): once PROVENANCE for `w0_FW`/`M_KK` is added, update the ledger flag (line 506).

---

## D. Convergence map (independent multi-reviewer agreement)

These are the items where ≥2 reviewers independently landed on the same target — the highest-confidence integration priorities.

| Target | Reviewers | Nature |
|:-------|:----------|:-------|
| **PROVENANCE for `w0_FW`/`M_KK`** | quantum-foam, sp, tesla, mack, volovik, hawking, einstein, nazarewicz (8) | Universal hygiene confirmation |
| **Ordered Veil correction (§5.3)** | volovik (decisive), nazarewicz (pairing-channel) | Ledger fix; +hawking/kaku/QF build on it (C2) |
| **§6.2 white-hole structure** | sp (asymmetric), tesla, transit, hawking (additions) | Conflict C1 + 3 additive |
| **α_s row/box (§7.1)** | mack, kaku, nazarewicz | 3 convergent edits (status word / frozen-FI pin / derived-not-chosen) |
| **CC caveat box (§7.1)** | volovik, hawking, einstein | 3 convergent additions (equilibrium / dS-horizon / location-vs-magnitude) |
| **`a(t)` gap framing (§6.3)** | einstein (decisive), transit, hawking, kaku, nazarewicz (5) | All endorse honesty; 4 complementary lenses |
| **§1.3a enrichments** | kaku, hawking (×2), quantum-foam, volovik, einstein (5) | All additive |
| **`N_pair` disambiguation (§7.1/§5.3)** | transit, nazarewicz | Firewall |
| **FI/RD as BMA / nuisance-functional (§3.2)** | nazarewicz (+tesla, mack on f) | Strengthen rigor |
| **Wronskian dispersion-rigidity (§4.2)** | tesla, nazarewicz, einstein (endorse) | Additive |
| **Genre/methodology naming (§0/§1)** | einstein (principle theory), kaku (matrix-model) | Complementary |

---

## E. Computational carry-forwards — NOT document edits (route to `/rclab-plan`)

These are proposed *new gates*. They do not integrate into the master; they belong in the next compute session's plan. Listed for completeness so they are not lost (per `session-handoffs.md` carry-forward rule).

| ID | What | Source | New gate |
|:---|:-----|:-------|:---------|
| SP-V5 | Conformal embedding modulus-space (Diagram B) → 4D (Diagram A); `Ω(τ)` | sp V.5 | SP-CONFORMAL-EMBED |
| SP-V6 | Anisotropic `τ→∞` singularity + censoring on the full 12D metric | sp V.6 | SP-12D-SINGULARITY-CENSOR |
| TES-V4 | Surface-gravity ↔ Mach cross-table for §6.2 | tesla V.4 | WHITE-HOLE-KINEMATIC-CONSISTENCY |
| TES-V5 | FI-confirm `R₁` truncation-robust at `L_max∈{6,8,10,12}` | tesla V.5 | (feeds §8.5) |
| VOL-V1 | Recompute Ordered Veil freeze-out on substrate clock (`t_transit`) | volovik V.1 | (presentation-correctness for §5.3) |
| VOL-V2 | Registry note: τ-flow (E7) vs q-flow (S62) distinct theorems | volovik V.2 | registry-hygiene (in-session candidate) |
| VOL-V3 | Microscopic equilibrium-theorem chain `dε/dq=μ ⇒ ρ_Λ=0` | volovik V.3 | (warrant for CC box / R4) |
| VOL-V4 | Substrate-compressibility derivation of `G_N` τ-flatness | volovik V.4 | INFO (corroborates G6) |
| HAW-V1 | Analog-temperature ledger reconciliation (3 surfaces) | hawking V.1 | HAWKING-ANALOG-T-LEDGER |
| HAW-V2 | GGE-relic purity / no-Page-curve certification (`Tr ρ²=1`) | hawking V.2 | HAWKING-GGE-PURITY |
| HAW-V3 | Exit-horizon greybody factor `Γ(ω)` for `A_s` | hawking V.3 | HAWKING-GREYBODY-AS |
| HAW-V4 | Tracking law as de Sitter horizon relation (C10 spec) | hawking V.4 | HAWKING-CC-HORIZON-FORM (INFO) |
| EIN-V1 | Two-excitation emergent-EP gedankenexperiment (NLO dispersion) | einstein V.1 | EMERGENT-EP-NLO |
| EIN-V2 | Emergent Bianchi/EIH lift `S_SA(τ)→4D action for g_M` | einstein V.2 | EMERGENT-EIH-LIFT (the load-bearing gap) |
| EIN-V3 | One-loop robustness of the no-well result | einstein V.3 | NO-WELL-ONE-LOOP |
| KAK-V1 | Is `t*` the one-loop threshold coefficient? (de-empiricize `t*`) | kaku V.1 | T-STAR-ONELOOP-ORIGIN (high-leverage) |
| KAK-V2 | Exhaustion falsifier: any `*`-product outside inner-fluctuation orbit? | kaku V.2 | EXHAUSTION-FALSIFIER |
| KAK-V3 | Effective-Friedmann bridge (genre-framed) | kaku V.3 | (feeds C2/T6) |
| NAZ | (optional) VAP/PBCS-projected `⟨Q⟩_GGE` to upgrade 59.8 from "order tens" to a quoted number | nazarewicz §5.3 | (only if a future gate needs the precision) |

**Memory-hygiene (not a doc edit, not a gate)**: kaku V.4 — retract the stale "spectral-dimension flow 12→5.65→4" bridge in kaku's own agent memory (REFUTED by S31Aa/S92).

**Convergent computational theme**: EIN-V2, KAK-V3, transit V.5, HAW-V4 all attack the *same* load-bearing object — the effective-Friedmann / `a(t)` bridge — from four axes (GR/EIH, matrix-model genre, transit back-reaction, dS-horizon). A single multi-axis wave (`/rclab-coordinate`) is the natural structure.

---

## F. Suggested integration sequencing

1. **Adjudicate the two conflicts first** (C1 §6.2 white-hole structure; C2 Ordered Veil scope). C1 in particular gates every §6.2 edit. A short sp-vs-(transit/hawking) workshop settles C1; A2's wording settles C2.
2. **Land the REQUIRED fixes** (A1 w₀/wₐ; A2 Ordered Veil §5.3 + §9 mirror; A4 provenance hygiene).
3. **Land the STRONG items** (mack daggers + LEGGETT-GRAV-DECAY conditional + α_s convergent edits + N_pair firewall + transit mode-equations + nazarewicz BCS-projection caveat).
4. **Batch the STRENGTHENINGS by section** — §1.3a (5 reviewers), §7.1 CC box (3), §6.3 a(t)-framing (5, incl. einstein's #1=#8 unification), §3.2 BMA, §4.2 dispersion-rigidity, §0/§1 genre naming. Most are drop-in text.
5. **Queue the computational carry-forwards** (§E) into the next compute session's plan; the `a(t)`-bridge cluster (EIN-V2/KAK-V3/transit-V5/HAW-V4) as one multi-axis wave.

**Net effect on the document**: every reviewer was explicit that their edits *strengthen* or *sharpen* — none weakens a result. The two genuine corrections (A1 sourcing, A2 ledger) make the document *more* defensible; the bulk are additive enrichments that tie existing correct claims to theorems the framework already owns. The single conflict that needs real adjudication is C1 (the white-hole symmetry).
