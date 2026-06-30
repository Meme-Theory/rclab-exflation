# Session 100a Workshop: volovik × transit — H-Parity Theorem Scope (W-1)

**Date**: 2026-06-07
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: volovik (volovik-superfluid-universe-theorist — theorem author; equilibrium Gibbs-Duhem / q-theory axis; defends Reading A), transit (transit-dynamics-theorist — diabatic transit-freeze + GGE relic + backbone dynamics axis; steelmans Reading B)
**Source Documents**:
- sessions/session-100a/session-100a-w1-workingpaper.md
- sessions/session-plan/session-100a-plan-w1.md
- computations/session-100a/s100a_gate_verdicts.txt

**Adjudication target**: the SCOPE of the W1-2 H-parity theorem (`S100a-W1-2-QEQ-DRIVE` FAIL, audit `e31d45cf5309b32cde67804d0576467592196b45ea908ec1edfac7f522212ca4`, verdict lines 26-30). The verdict is PERMANENT per gate-verdicts.md — this workshop adjudicates the partition's exhaustiveness, the citation discipline, and the Stage-0 candidate text, never the verdict.

**Focus Topics**:
1. **(a) Partition exhaustiveness** — is potential-vs-friction exhaustive for substrate-internal q-dynamics on the bare backbone? Does the never-equilibrated GGE relic sector (integrability-protected) admit a potential-type odd-in-H term outside the explicit 3Hq′ friction, or is every odd-in-H term structurally dissipative in the 1D q-channel (no transverse Magnus escape route in one dimension)?
2. **(b) dS-equilibrium imports** — do T = H/π and s = 3H/4G (Volovik Paper 11) remain valid on the locally non-adiabatic backbone (ε_ad = 0.897 at the Ḣ = 4.41 spike)? Do Ḣ-corrections (H-even under t→−t) preserve the even-parity conclusion? State the corrected parity claim WITH its regime clause.
3. **(c) Citation form** — which is registry/capstone-correct downstream: the unscoped verdict-string `no_slope1_capable_substrate_drive`, or the scoped "no EQUILIBRIUM-thermodynamic drive can be odd in H"?
4. **(d) Routing** — if the wall survives with its scope clause: draft the Stage-0 joint-theorem candidate text (volovik-side clauses GD-1..GD-5 + parity; transit-side clause: non-equilibrium-sector exclusion boundary; JOINT clause: scope statement + self-consistency carve-out) for Stage-1 registration at S101. If a viable odd-in-H non-equilibrium drive candidate is constructed: emit a 4-field pre-registered gate spec (SIBLING to CF-S101-W1-QEQ-SELFCONS, NOT a replacement). Either way: state the delta (possibly zero) to CF-S101-W1-QEQ-SELFCONS.

**Round structure (pinned)**: R1 = volovik pins theorem + exact scope; transit constructs strongest non-equilibrium counter-candidates. R2 = term-by-term classification/rebuttal + converge on Stage-0 text or gate spec.

**Downstream consumers (state the verdict so they can cite it)**: the S100b w1 closure reading inherits this scope clause; the S100b X-wave C10 gates consume the W1-2 FAIL within the cross-session n_eff triangle {2.3, <2, ~4.11} — triangle coherence adjudication is OWNED by the S100b schedule; this workshop pins only the scope/exhaustiveness verdict those consumers cite.

---

## Round 1 — volovik: Opening Analysis

### V1: (a) Partition Exhaustiveness — Theorem + Exact Scope

**Key finding.** The H-parity theorem survives Reading B's challenge with ONE retraction, ONE sharpening, and ONE declared open boundary. The retraction concerns the WP §W1-2 parenthetical, not the theorem. The sharpening upgrades the theorem's operative content from a parity statement to an ANALYTICITY statement that explains, in one stroke, both the measured GD slope (2.0556) and why the imposed closure (1.0083) is "imposed." The open boundary (non-Markovian memory terms) is where transit's strongest territory genuinely lies, and I pre-build the classification machinery for it here.

**(i) Retraction — what the theorem never was.** The WP §W1-2 parity-theorem text carries "(only the dissipative sector distinguishes expansion from contraction)" and "An H-linear coupling is odd-sector (dissipative)." Both over-claim, and the corpus itself is the witness: **Paper 11 §VI** (`researchers/Volovik/11_2025_Volovik_First_Law_de_Sitter.md`, Key Results 6) assigns the contracting de Sitter state the EQUILIBRIUM values T = H/π < 0 and S = −A/4G < 0 — equilibrium state functions are H-odd and DO distinguish expansion from contraction (the negative entropy is consistent with white-hole tunneling rates as an equilibrium statement, not a dissipative one). Likewise, a hypothetical H-linear potential tilt −c·H·q would be T-odd yet CONSERVATIVE (it does no work at fixed H); "odd ⟹ dissipative" is not a theorem of mechanics. What IS true and load-bearing: the equilibrium POTENTIAL SHIFT ∫s dT built from two H-odd state functions is H-even, and the exclusion of odd-in-H potential terms is SECTOR-BY-SECTOR (items iii–v below), not a single mechanics theorem. The FAIL verdict is untouched — the gate's verdict consumed only the even exponent, which stands.

**(ii) The theorem, with every assumption explicit.** What GD-1..GD-5 + parity actually assume (WP §W1-2; plan §W1-2 Definition 4 candidate (i)):

| Step | Content | Assumes | Corpus anchor |
|:-----|:--------|:--------|:--------------|
| GD-1 | ρ_vac(q\*) = ε − μ₀q\* = 0; interior equilibrium q\* = 0 | the q-channel possesses an equilibrium reference state (self-sustained vacuum) | Paper 25 §II–III, Eqs. (2.11), (2.14) (`researchers/Volovik/25_..._Non_Equilibrium_Vacua.md`); Paper 05; S62 #19 / S95 |
| GD-2 | ρ_vac(q) = ½k_curv q², k_curv = +3586.5312; χ = 1/k_curv | local expansion valid (XC-7: V(q_eq,max)/a_0^{ζ} = 0.1257 < 1) | S99 npz (992-mode ω_n(q) substrate response) |
| GD-3 | T(H) = H/π; s(H) = 3H/(4G) | local state dS-symmetric to leading order in gradients (quantitative regime → V2) | Paper 11 Sec.II + Eq. (5); Paper 35 Eqs. (9), (15) |
| GD-4 | δμ = −(1/n_q)∫₀^T s dT′ at dP = 0 | Markovian quasi-static traversal of local equilibria (Gibbs-Duhem) | Paper 11 Eq. (8) family; Paper 35 §IV.A |
| GD-5 | q_eq = χ·δμ (tilted-well minimum) | adiabatic tracking, ω ≫ drive rate (ε_ad = 0.897 marginal at the spike → V2) | WP §W1-2 XC-1 |
| Parity | T, s are H-odd | the H → −H sign structure of the equilibrium dS state | Paper 11 §VI (T < 0, S = −A/4G for contraction) |

**(iii) Substitution chain A — the core parity claim, executed** (per `math-scripts.md` §"Double-Check Logic Before Compute"):

```
Claim: delta-mu(H), hence q_eq(H), is EVEN under H -> -H; leading power H^2.

Step 1: T(H) = H/pi                      [Paper 11 Sec.II]
        T(-H) = -H/pi = -T(H)  =>  T is H-odd.
        [Physical anchor: Paper 11 §VI — contracting dS has T < 0]
Step 2: s(H) = 3H/(4G)                   [Paper 11 Eq.(5); Paper 35 Eq.(15)]
        s(-H) = -s(H)          =>  s is H-odd.
        [Physical anchor: Paper 11 §VI — S = -A/4G for contraction]
Step 3: Eliminate H: s(T) = (3*pi/4G)*T — an ODD function of T
        (composition of two odd maps).
Step 4: delta-mu(H) = -(1/n_q) * Int_0^{T(H)} s(T') dT'   [GD-4, dP = 0]
                    = -(3*pi/(8G*n_q)) * T^2
                    = -(3/(8*pi*G*n_q)) * H^2.
Step 5 (parity, GENERAL odd s — not only linear):
        F(T) := Int_0^T s(T') dT'.  Substitute T' = -u:
        F(-T) = -Int_0^T s(-u) du = +Int_0^T s(u) du = F(T).
        F is EVEN for ANY odd s(T).
Step 6: q_eq = chi * delta-mu, chi = 1/k_curv (H-independent)
        => q_eq(-H) = q_eq(H); leading power H^2.
Conclusion: no analytic odd-in-H term — in particular no c*H — can arise
from the equilibrium potential route. Late-tail d ln q_eq / d ln H -> 2;
measured 2.0556 = 2 + tracking lag (WP XC-1). The parity conclusion is
independent of the LINEARITY of s(T) (Step 5): it needs only oddness.
```

**(iv) Substitution chain B — the 1-dof gyroscopic-exclusion theorem (the Magnus/Iordanskii concession, and its resolution).** Reading B is RIGHT about the corpus, and I concede the general point without reservation: superfluid dynamics contains velocity-odd NON-dissipative forces — the Magnus force F_M = ρ_s κ × (v_L − v_s) and the Iordanskii force (transverse quasiparticle-scattering force; spectral-flow / axial-anomaly lineage in Paper 08, `researchers/Volovik/08_1998_Volovik_Axial_Anomaly_3He_Baryogenesis.md`; vortex-force taxonomy in Paper 10). "Odd-implies-friction" is NOT a theorem of superfluid dynamics in general. But both forces escape dissipation through TRANSVERSALITY (F ⊥ v ⟹ F·v = 0), and transversality needs room:

```
Claim: in the 1D q-channel, every odd-in-qdot force is structurally in the
       working (dissipative/anti-dissipative) class; the workless odd class
       is EMPTY.

Step 1: in N-dof mechanics every generalized force decomposes as
        F_i = -d_i V(q; lambda) + D_i(q, qdot) + G_ij(q) * qdot_j,
        with G_ij = -G_ji the gyroscopic (workless) part:
        qdot_i G_ij qdot_j == 0 by antisymmetry.
Step 2: the q-channel has N = 1  =>  G is a 1x1 antisymmetric matrix
        =>  G = -G  =>  G == 0.  The gyroscopic class is EMPTY in 1 dof.
Step 3: any remaining qdot-odd 1-dof force F = P(q, qdot^2) * qdot has power
        F * qdot = P * qdot^2 != 0 generically — it does work: dissipative
        class (sign of P sets damping vs pumping; the 3H*qdot member damps
        for H > 0, pumps for H < 0 — T-consistent).
Conclusion: Magnus and Iordanskii have NO image in the 1D q-channel. The
"no transverse Magnus escape route in one dimension" clause is a THEOREM
of 1-dof mechanics, not an assertion.
```

The one honest reopening of this chain: if transit can exhibit a SECOND substrate collective coordinate dynamically paired with q (making the effective system 2-dof, where G_ij ≠ 0 is possible), the gyroscopic route reopens. That is Q-T3 below — and it would be the genuinely new object of this workshop if it exists.

**(v) The GGE relic sector — three-step closure of the potential-type odd-in-H route (argument-grade, not theorem-grade).** The equilibrium theorem is VACUOUS on the relic sector — not violated: no local-equilibrium state functions exist on a sector whose occupations were frozen at the fold (diabatic transit-freeze, R_therm = t_therm/t_transit = 5251.82, S95-certified; fabric-scale CG(24) Poisson integrability is what protects the frozen set). Reading B's strongest candidates live here. The Reading-A case that no potential-type odd-in-H term arises there either:

1. **Frozen occupations ⟹ no instantaneous H-dependence.** The relic IS the integrability-protected occupation set {n_k} (P_exc = 1.000, Parker pair production at the fold). The relic's effective tilt on the q-channel is F_GGE = −∂ρ_GGE/∂q = −Σ_k n_k (∂E_k/∂q) · a^{−3(1+w)}. The ∂E_k/∂q response is REAL — it is the same 992-mode ω_n(q) substrate response that built k_curv — so the tilt exists and I do not deny it. But at fixed (q, a) it carries NO H-dependence whatsoever: the n_k are constants of motion, the E_k(q) are spectral data of the τ-slice, and H enters the relic sector only through evolution (ȧ = aH). Functionally, the relic tilt is H-even trivially (H-independent at fixed state). q-theory itself licenses exactly this and no more: the matter tilt ∂L_M/∂q enters the generalized Maxwell equation (Paper 25 Eq. (4.4)) as a state-dependent, not rate-dependent, term.

2. **Dilution-trajectory slope is structurally 2; slope-1 only by backbone coincidence.** Substitution chain C:

```
q_eq^tilt = F_GGE/k_curv ∝ a^{-3(1+w)}.
Along a local power-law stretch a ∝ t^p:  H = p/t  =>  d ln a / d ln H = -p
=> slope[q_eq^tilt] = d ln q_eq^tilt / d ln H = -3(1+w) * (-p) = 3p(1+w).
Friedmann-consistent single-fluid background: p = 2/(3(1+w))
=> slope = 3 * [2/(3(1+w))] * (1+w) = 2  IDENTICALLY
   (this is Friedmann restated: the dominant rho tracks H^2).
Slope = 1  <=>  p = 1/(3(1+w))  — for the w = 0 Leggett relic, p = 1/3:
a measure-zero local coincidence on a pinned backbone, NOT an attractor.
```

So a GGE dilution tilt is parity-even functionally and slope-2 structurally; it can MIMIC slope 1 only on backbone segments where 3p_local ≈ 1, which is checkable on the pinned npz (Q-T1).

3. **Architecture routes all remaining relic influence through the backbone — i.e., into the carve-out.** Block-diagonal D_K (S22b PERMANENT), V_inter = 0 exact (S60 inter-sector Zubarev), two-layer architecture (S72: the BCS sector communicates with the spectral sector only through the metric moments). Beyond the frozen tilt of item 1, the relic influences the q-channel only through the emergent Friedmann closure — through H itself. But feeding back through H on a q-sourced backbone IS the self-consistency route: the substrate's own block structure COLLAPSES "GGE-sourced effective potential" into the already-carved-out CF-S101-W1-QEQ-SELFCONS channel. Reading B's non-equilibrium drive, pursued to its substrate locus, becomes the back-reaction gate we already pre-registered.

**(vi) The |H| collapse — why "odd-in-H structure the equilibrium argument never sees" mislocates the threat.** On the physical post-fold branch H > 0 throughout the gate domain (tail q > 0, domfrac 1.0000), sign(H) = +1 is CONSTANT: any putative odd form sign(H)·f(H²) is numerically identical to the even form f(H²) on the entire branch. The odd/even dichotomy COLLAPSES on-branch; the operative dichotomy is:

- **analytic in H²** (equilibrium route; chain A): late-tail log-slope → even integers {2, 4, ...} — since slope[c₂H² + c₄H⁴ + ...] = (2c₂H² + 4c₄H⁴ + ...)/(c₂H² + c₄H⁴ + ...) → 2 as H decays on the tail;
- **non-analytic √(H²) = |H|** (slope exactly 1): reachable ONLY through amplitude variables — q_amp ∝ √ρ_osc ∝ |H| — which is the Klinkhamer-Volovik oscillation-energy self-consistency mechanism verbatim (Paper 25 §V, Eqs. (5.5a)-(5.5b): q − q₀ ~ q₀ sin(ωt)/(ωt), ρ_vac ~ E_P²H² — the square root of a Friedmann-even energy).

|H| is EVEN. The slope-1 form is therefore parity-CONSISTENT: the KV carve-out does not evade the parity theorem, it occupies the unique non-analytic-even cell the theorem leaves open. The theorem and the carve-out are two halves of a single **slope-selection rule**: equilibrium analyticity selects even integers; amplitude self-consistency selects 1. The gate measured both halves: 2.0556 (GD drive, even-locked + tracking lag) and 1.0083 (imposed |H|-form closure, reproducing S99 at 4.6e-8).

**Exhaustiveness verdict (Reading A, R1 position).** For substrate-internal q-dynamics on the bare backbone, the complete force taxonomy is **{potential (q̇-independent), q̇-coupled, non-Markovian memory}**. Slot 1: equilibrium-sourced = analytic-even (THEOREM, chain A); GGE-sourced = functionally H-even with dilution-trajectory slope 3p(1+w) (ARGUMENT-grade, checkable via Q-T1); architectural feed-through = the carve-out channel (item v.3). Slot 2: the gyroscopic sub-class is EMPTY in 1 dof (THEOREM, chain B); the remainder is the working/dissipative class, whose model member is 3Hq̇. Slot 3: NOT covered by the partition as stated — the declared open boundary, bounded by the V4 sibling scaffold, not by this theorem. The partition's exhaustiveness claim must be cited as: **exhaustive for Markovian, analytic, 1-dof dynamics; memory terms open; the self-consistency carve-out separate and parity-consistent.**

**Questions for transit:**

- **Q-T1 (dilution-mimic window, computable now):** from `s99_w1_q_nonratio_observable.npz`, compute p_local(τ) = −H²/Ḣ on the regression tail (τ ≥ 0.3205). Does 3·p_local enter [0.95, 1.05] anywhere? If yes, bound the window fraction; if no, the dilution-mimic candidate dies on this backbone. Either way the structural slope is 2 (chain C).
- **Q-T2 (memory kernel, your strongest slot):** construct your best non-Markovian candidate explicitly — which GGE correlation function sources the kernel K(t−t′), and does its Markovian reduction generate any q̇-INDEPENDENT term odd in instantaneous H, or only renormalizations of k_curv and the friction coefficient? My prediction: the kernel is even-graded (GGE correlators of T-even operators over a frozen occupation set), and no odd potential tilt survives the reduction. Exhibit a counter-construction if you have one.
- **Q-T3 (the 2-dof reopening):** do you accept chain B as closing the Magnus/Iordanskii route in 1 dof, or do you contend the q-channel is secretly multi-dof — q dynamically paired with a relic collective coordinate into an effective 2-dof system where G_ij ≠ 0? If the latter: NAME the second coordinate and its substrate channel. That is the one construction that would genuinely reopen the workless-odd class.
- **Q-T4 (on-branch collapse):** the transit DID break time reversal (the relic is a T-asymmetric state — that is the structural license Reading B correctly senses). Exhibit any concrete sign(H)-carrying coupling that is NOT trajectory-equivalent to an even form on the H > 0 branch, or concede the collapse of item (vi).

### V2: (b) dS-Equilibrium Imports + Ḣ-Corrections

**Key finding.** Split the import-validity question into two layers that Reading B's challenge conflates: the QUANTITATIVE layer (the coefficient values T = H/π, s = 3H/4G) is regime-limited and indeed badly violated at the Ḣ-spike — I concede this with numbers below — while the STRUCTURAL layer (the parity grading) is exact order-by-order in the gradient expansion and is the ONLY thing the gate's verdict consumed (XC-5: κ₂-invariance at 7.6e-8; the multiplicative-cancellation identity makes every coefficient slope-irrelevant). Ḣ-corrections preserve the even-parity conclusion AND — independently — transmit slope 2 anyway. The corrected parity claim with its regime clause is stated at the end of this section in citation-grade form.

**(i) The grading argument — parity to all orders.** Define the t → −t involution on backbone trajectories: ã(t) = a(−t). Then:

```
Grading table (substitution chain):
  H    = adot/a          ->  Htilde(t)  = -H(-t)      g(H)    = -1 (odd)
  Hdot = dH/dt           ->  +Hdot(-t)                 g(Hdot) = +1 (even)
  Hddot                  ->  -Hddot(-t)                g(Hddot)= -1 (odd)
  d^n H/dt^n                                            g = (-1)^{n+1}
Dimensionless gradient ratios (the natural expansion variables):
  x1 = Hdot/H^2 :  g(x1) = (+1)/(-1)^2 = +1  (even)
  x2 = Hddot/H^3:  g(x2) = (-1)/(-1)^3 = +1  (even)
  general: (d^n H/dt^n)/H^{n+1}: g = (-1)^{n+1}/(-1)^{n+1} = +1 (even). ALL even.
```

The local-equilibrium state functions of the quasi-dS stratum are gradient expansions around exact dS: T = (H/π)·t̂(x₁, x₂, ...), s = (3H/4G)·ŝ(x₁, x₂, ...), with t̂, ŝ analytic in the all-even ratios and t̂ = ŝ = 1 at exact dS. Their g-parity: odd × even = ODD, to every order — the oddness anchored physically by Paper 11 §VI (contraction: T < 0, S = −A/4G). Then the Gibbs-Duhem shift: at fixed even arguments, dT = t̂ dH, and ∫s dT = ŝ t̂ H²/2 + (terms generated by d(even args), each carrying even grading) — **g-EVEN to all orders**. The conclusion of chain A (V1.iii) is therefore not a leading-order accident: it survives every analytic Ḣ-, Ḧ-, ...-correction. Parity is also preserved by any limit of graded partial sums, so resummation cannot break it; breaking it requires structure that is non-perturbative in gradients — i.e., a sector with NO local-equilibrium description, which is exactly clause (b) of the regime statement below and lands in transit's T1/T2 territory, not in the equilibrium import.

**(ii) The (K,R) gravitational-pair loophole — closed.** Paper 11 Eq. (8) modifies Gibbs-Duhem with the gravitational conjugate pair: Ts = ε + p + KR, K = 1/(16πG), and Paper 35 §IV.A builds the dark-matter pressure P_DM = P_vac − K𝓡 from it. Could the extra pair change the parity bookkeeping? No: R = 12H² (Paper 11 §IV) is g-EVEN; K is H-independent (and in q-theory dK = (dK/dq)dq is a q-sector differential, g-even); so the extended differential form dP = s dT + n_q dμ + R dK at dP = 0 still yields a g-even δμ. The modified-GD route adds only even-graded terms. Loophole closed.

**(iii) Quantitative concession — the leading-order coefficients are NOT reliable at the spike.** Substitution chain for the quasi-dS expansion parameter at the Ḣ-spike (all inputs from WP §W1-2 XC-1):

```
eps_ad = max|2*Hdot/H| / omega = 0.897,  omega = sqrt(k_curv) = 59.888
=> max|2*Hdot/H| = 0.897 * 59.888 = 53.72                      # (local)
At the spike Hdot = 4.41  =>  |H|_spike = 2*4.41/53.72 = 0.164  # (local)
=> |Hdot|/H^2 |_spike = 4.41/(0.164)^2 ~ 1.6e2  >> 1            # (local)
(consistency: 3H <= 0.92 on the tail => H <= 0.307; 0.164 < 0.307 ok)
```

So at the spike the dS-expansion parameter x₁ = Ḣ/H² ≈ 1.6×10²: the local state is FAR from quasi-dS there, and the leading-order coefficients T = H/π, s = 3H/4G are quantitatively unreliable at that point. On the rest of the tail x₁ = 1/p_local ~ O(1) — marginal, never deeply quasi-static. **This concession costs the verdict nothing**: the gate's FAIL consumed only the EXPONENT, which is grading-protected (item i), never the coefficient, which is κ₂-irrelevant by XC-5 (slope shift 7.56e-8 under κ₂ → 10κ₂; `math-scripts.md` §"Multiplicative-normalization cancellation invariants" — the log-derivative annihilates every multiplicative pre-factor). The same is true of the residual conventions disclosed in WP §W1-2 item 3: T = H/π vs H/2π (Gibbons-Hawking vs local; Paper 11 Sec.II fixes the factor 2 but either convention) enters the coefficient only. Where the coefficient DOES matter — a future numerical κ₂ extraction for the n_q charge density — the spike region must be excised or the gradient corrections resummed; flag this for any S101+ κ₂-precision gate.

**(iv) Ḣ-corrections cannot rescue slope 1 even if admitted as drive terms.** Independently of parity: suppose a correction places a term ∝ Ḣ directly into δμ. On any local power-law stretch of the backbone:

```
a ∝ t^p  =>  H = p/t,  Hdot = -p/t^2 = -H^2/p
=>  d ln|Hdot| / d ln H = 2.
```

A Ḣ-drive transmits tail slope 2, not 1 — it is an H²-drive in disguise on every power-law segment. Combined with (i): Ḣ-corrections preserve the even-parity conclusion at the functional level AND reproduce the even slope at the trajectory level. There is no rescue route through gradients.

**(v) The corrected parity claim, WITH its regime clause (citation-grade form).**

> **H-parity theorem (scoped form).** On the q-channel q″ + 3Hq′ + ∂_q V_eff = 0 over a homogeneous backbone, restrict to the local-quasi-equilibrium stratum: wherever the substrate's local-equilibrium state functions exist as t→−t-graded gradient expansions around local dS — T = (H/π)·t̂(Ḣ/H², Ḧ/H³, ...), s = (3H/4G)·ŝ(...), with t̂, ŝ analytic in the (all-even) gradient ratios [Paper 11 §§II, VI; Paper 35 Eqs. (9), (15)] — every Gibbs-Duhem potential shift δμ = −(1/n_q)∫s dT at dP = 0, including the (K,R) gravitational-pair extension [Paper 11 Eq. (8); R = 12H² even], is EVEN under the grading and analytic in H², to all orders in the gradient expansion. Hence every equilibrium-thermodynamic q_eq(H) has late-tail log-slope an even integer (generically 2), and no analytic odd-in-H — in particular no linear-in-H — equilibrium potential term exists.
>
> **Regime clause.** (a) The statement is parity-exact order-by-order, but its leading-order COEFFICIENTS are quantitatively reliable only where |Ḣ|/H² ≪ 1; on the gate's backbone this is violated at the Ḣ-spike (|Ḣ|/H² ≈ 1.6×10² at the ε_ad = 0.897 point) and marginal (O(1)) elsewhere on the tail — limiting κ₂-precision only, never the FAIL (XC-5 coefficient-invariance, 7.6e-8). (b) The theorem is VACUOUS — not violated — on sectors possessing no local-equilibrium state functions: in particular the GGE relic, whose occupation set was frozen at the fold (diabatic transit-freeze, R_therm = 5251.82, S95) and is integrability-protected thereafter; the relic's exclusion from odd-in-H potential sourcing is ARGUMENT-grade (V1.v), not theorem-grade. (c) Non-analytic even forms |H| = √(H²) (amplitude variables — the KV self-consistency route, Paper 25 §V Eqs. (5.5a-b)) and non-Markovian memory terms are OUTSIDE the theorem's domain; routed respectively to CF-S101-W1-QEQ-SELFCONS and the V4 sibling scaffold.

**Question for transit on (b):** do you accept the grading argument at the spike — parity preserved per-order on a marginally-convergent expansion, with any breakdown necessarily landing in clause (b)'s non-equilibrium territory rather than in the equilibrium import itself? If you contend the gradient expansion FAILS to define graded state functions anywhere on the tail (not merely at the spike), state the τ-window and the diagnostic, because that would move part of the tail from "theorem-grade" to "argument-grade" and the Stage-0 clause (e) scope line would need the window written into it.

### V3: (c) Citation Form — Scoped vs Unscoped

**Key finding.** The two ledger forms are both correct IN THEIR REGISTERS, and the discrepancy dissolves under an explicit expansion rule — no verdict-line action exists or is needed (verdict lines are PERMANENT per `gate-verdicts.md`; the FAIL and its value string are untouchable and untouched). What the workshop pins is the DOWNSTREAM CITATION DISCIPLINE.

**(i) Why the verdict string is correct in its register.** `no_slope1_capable_substrate_drive` is the gate-internal compressed payload of: "among substrate-internal DRIVES — q_eq(H) terms entering the potential slot of the friction ODE on a FIXED backbone — none is slope-1-capable." Within the gate's pre-registered design domain (plan §W1-2: drive candidates (i)/(ii), fixed `arr_H_bare_t` backbone) that is exactly what was shown: the equilibrium drive is theorem-locked to even slopes (V1 chain A), and the Klinkhamer-Volovik mechanism is NOT a drive — the WP §W1-2 Assessment says so in terms: "slope 1 from back-reaction, not from a drive," "structurally outside this gate's fixed-backbone design." The token quantifies over drives; back-reaction was never in its quantifier range.

**(ii) Why the scoped sentence is the registry/capstone-correct citation form.** The synthesis (WP "Wave 1 Synthesis" §1) and the constraint-map row 2 already carry the scoped form ("no equilibrium-thermodynamic drive can be odd in H; ... self-consistency route remains"). A downstream reader who meets only the bare token would read "no substrate drive exists, period" — erasing the carve-out that the SAME WP section explicitly preserves, and over-claiming the relic sector where the closure is argument-grade (V1.v), not theorem-grade. That is the ledger discrepancy Reading B correctly flags, and it is a citation-discipline problem, not a verdict problem.

**(iii) The pinned citation text (proposed; to be frozen at R2 and effected in-document by the final agent).**

> **Canonical downstream citation for S100a-W1-2-QEQ-DRIVE (FAIL, audit e31d45cf5309b32cde67804d0576467592196b45ea908ec1edfac7f522212ca4):** On a fixed backbone, no substrate-internal EQUILIBRIUM-THERMODYNAMIC drive q_eq(H) can carry odd-in-H structure: every equilibrium Gibbs-Duhem potential shift is analytic-even in H (H-parity theorem, scoped form per the S100a W-1 workshop; leading power H², transmitted slope 2.0556 measured, κ-invariant at 7.6e-8). The slope-1 leg of the n = 2 tracking law is therefore an imposed-closure INPUT on any fixed backbone. Scope: equilibrium sector — theorem-grade; never-equilibrated GGE relic sector — excluded at argument-grade (frozen occupations + dilution-slope-2 + 1-dof gyroscopic exclusion; S100a W-1 workshop, pending any sibling gate); non-Markovian memory terms — open. The surviving slope-1 route is Klinkhamer-Volovik oscillation-energy self-consistency (back-reaction, not a drive; q_amp ∝ |H|, parity-CONSISTENT non-analytic-even form; Paper 25 §V), pre-registered as CF-S101-W1-QEQ-SELFCONS.

**Expansion rule (the discipline itself):** any downstream citation of the token `no_slope1_capable_substrate_drive` MUST expand it with the three scope qualifiers — (drive-type: potential-slot q_eq(H)), (fixed-backbone), (equilibrium = theorem-grade / relic = argument-grade) — plus the carve-out pointer. Bare-token citation without expansion is a citation-discipline violation.

**(iv) Consumer-specific drafts (for R2 convergence; surface landings ROUTED to sole writers, not self-applied).**

1. **S100b w1 closure reading**: inherits the canonical citation paragraph (iii) verbatim. No additional text.
2. **S100b X-wave C10 gates** (S100b-X-C10-RHOVAC-EPOCH-PROFILE, trigger-first on this gate; S100b-X-C10-BBN-CONSTRAINT-RECONCILE): the n_eff triangle member "~4.11" carries the mandatory tag — *"n ≈ 4.11 = 2 × 2.0556 is the FIXED-BACKBONE equilibrium-GD drive law (corridor-map value), NOT the framework's physical n_eff prediction; the framework's physical route is the self-consistency channel (n = 2 if CF-S101-W1-QEQ-SELFCONS lands PASS)."* Triangle-coherence adjudication {2.3, <2, ~4.11} is OWNED by the S100b schedule; this workshop pins only this tag and the scope clause the members cite.
3. **Capstone §8.5** (designated capstone writer; capstone-hygiene Q3/Q4 apply): §8.5 stays OPEN by design — unchanged status — with the conditionality LOCUS now nameable: *"the q ∝ H closure implicitly assumes the amplitude (square-root-of-energy) mechanism without deriving it; equilibrium thermodynamics cannot supply it (H-parity, S100a-W1-2); derivation attempt = CF-S101-W1-QEQ-SELFCONS."* DRAFTED here, ROUTED to the capstone designated writer.
4. **WP §W1-2 parenthetical**: the landed gate section is NOT retroactively edited (landed-artifact discipline). The corrected statement of record is V2.(v) of this workshop; the synthesis-level citation text (iii) supersedes the parenthetical for all downstream use.

**Question for transit:** does Reading B accept the two-register resolution — token correct within its drive/fixed-backbone quantifier range, scoped sentence mandatory downstream — or does transit contend the token's quantifier range itself was ambiguous at pre-registration (in which case the expansion rule should be strengthened from "MUST expand on citation" to "token deprecated for citation; cite only the scoped sentence")? I am prepared to accept the stronger form if transit shows one realistic mis-citation pathway that the expansion rule fails to block.

### V4: (d) Routing — Stage-0 Candidate Structure

**Key finding.** The wall survives with its scope clause (V1-V2), so the primary route fires: Stage-0 joint-theorem drafting proceeds in this workshop, Stage-1 registration at S101 per `joint-theorem-promotion.md`. Stage-0 authorship = volovik + transit ONLY, deliberately leaving lizzi / connes / gen / kitaev Stage-2-eligible (S99 E1 author-exclusion lesson; the same exclusion discipline S100a already enforced at plan-freeze for the VIIW3LAB and VIIAM Stage-2 verifies — verdict-file reviewer-cleanliness rows). Delta to CF-S101-W1-QEQ-SELFCONS: ZERO to the 4-field spec; one non-gating diagnostic enrichment flagged. Sibling gate: scaffold pre-built below, EMITTED only if transit's R1 constructs a viable candidate that survives R2 classification.

**(i) Stage-0 candidate skeleton (volovik-side R1 draft; clause text freezes only at R2 convergence).**

> **THEOREM CANDIDATE — H-PARITY-DRIVE-EXCLUSION (fixed-backbone q-channel)**
>
> - **Clause (a) [volovik-side]**: The Gibbs-Duhem derivation chain GD-1..GD-5 (assumptions enumerated per workshop V1.ii) yields the parameter-free substrate drive q_eq(H) = κ₂H², κ₂ = 3/(8πG·n_q·k_curv); the exponent is locked by the s ∝ T Gibbs-Duhem integration + the quadratic well; the coefficient is regime-limited per the V2 regime clause (a) and verdict-irrelevant (XC-5, 7.6e-8).
> - **Clause (b) [volovik-side]**: All-orders H-parity grading — equilibrium T and s are t→−t-odd (anchor: Paper 11 §VI, contracting dS with T < 0, S = −A/4G); all dimensionless gradient ratios Ḣ/H², Ḧ/H³, ... are even; every equilibrium Gibbs-Duhem potential shift, including the (K,R)-pair extension (Paper 11 Eq. (8), R = 12H² even), is even-graded and analytic in H², to all orders in the gradient expansion. No analytic odd-in-H equilibrium potential term exists at any order.
> - **Clause (c) [volovik-side]**: Slope-selection corollary — equilibrium analyticity confines late-tail log-slopes to even integers (generically 2); slope 1 requires the non-analytic even form |H| = √(H²), reachable only through amplitude (square-root-of-energy) variables. Numerical instantiation: 2.0556 (GD drive, even-locked + tracking lag) and 1.0083 (imposed |H|-form closure, = S99 at 4.6e-8).
> - **Clause (d) [transit-side — TO BE AUTHORED BY TRANSIT]**: Non-equilibrium-sector exclusion boundary. My proposed content, offered for negotiation, NOT imposed: (d1) the frozen-{n_k} relic tilt is functionally H-independent at fixed (q, a); (d2) dilution-trajectory slope = 3p(1+w) — structurally 2 on Friedmann-consistent backgrounds, slope-1 only on the coincidence window 3p_local ∈ [0.95, 1.05], bounded by the Q-T1 computation; (d3) the 1-dof gyroscopic exclusion (workshop V1 chain B) closes the Magnus/Iordanskii route absent a second collective coordinate; (d4) the non-Markovian memory slot is OPEN — bounded by the sibling gate below, not by this theorem.
> - **Clause (e) [JOINT]**: Scope statement — the wall reads "no slope-1-capable substrate-internal DRIVE on a fixed backbone," where: equilibrium stratum = theorem-grade (clauses a-c); GGE relic sector = argument-grade (clause d, pending sibling); back-reaction = outside the quantifier range (not covered, not violated). Downstream citation per the V3 expansion rule.
> - **Clause (f) [JOINT]**: Self-consistency carve-out — the Klinkhamer-Volovik oscillation-energy amplitude route (Paper 25 §V Eqs. (5.5a-b); two-component exchange dynamics blueprint, Paper 35 §V) is the unique surviving slope-1 mechanism; it is parity-CONSISTENT (|H| is even); pre-registered as CF-S101-W1-QEQ-SELFCONS, spec delta ZERO.

Stage-1: register at S101 with the `STAGE-1-CANDIDATE` tag, joint clauses (e), (f) flagged for Stage-2 PASS-AND. Stage-2 (S101+ when dispatched): Axis-A reviewer from {lizzi-spectral-functional-theorist, connes-ncg-theorist} auditing clauses (a)-(c) + joints from the spectral/NCG side; Axis-B reviewer from {gen-physicist, kitaev-quantum-chaos-theorist} auditing clause (d) + joints from the dynamics side — neither a Stage-0 author, satisfying all three conditions of the Axis-B Selection Protocol (axis-distinctness, authoring-agent exclusion with downstream-inheritance reach, audit-coverage adequacy).

**(ii) Delta to CF-S101-W1-QEQ-SELFCONS: ZERO to the spec, one flagged enrichment.** The 4-field spec (WP "Carry-Forward Computations" block: what / inputs / gate `|slope_selfcons − 1| ≤ 0.05`, domfrac ≥ 0.95 / effort ~1 wave) stands unmodified. The workshop ADDS, without touching the spec: (1) the citation-scope clause its consumers inherit (V3.iii); (2) a NON-GATING diagnostic enrichment for the S101 planner — the self-consistent gate should also regress ln q_amp vs ln |H| directly, because clause (c) makes a sharp prediction: a PASS must realize slope 1 specifically through the amplitude law q_amp ∝ |H| (the non-analytic-even form), and seeing that signature confirms the slope-selection rule rather than merely the slope; (3) the conditional sibling below. Items (1)-(2) are inside the existing effort envelope; neither changes gate, inputs, or threshold.

**(iii) Sibling gate scaffold (pre-built; EMIT at R2 only if transit's R1 constructs a viable odd-in-H or memory-kernel candidate; SIBLING to CF-S101-W1-QEQ-SELFCONS, NOT a replacement).**

1. **What**: Decompose the GGE-relic-induced effective force on the q-channel — the frozen-{n_k} tilt, its dilution modulation, and transit's constructed memory kernel K(t−t′) with its Markovian reduction — under the t→−t grading; test for (A) any q̇-independent term odd in instantaneous H above a floor, and (B) the dilution-mimic window on the pinned backbone.
2. **Inputs**: `computations/session-100a/s100a_w1_qeq_drive.npz` (audit e31d45cf5309b32c); `computations/session-99/s99_w1_q_nonratio_observable.npz` (backbone; p_local(τ) = −H²/Ḣ); GGE occupation artifacts (S38/S95 lineage); the k_curv 992-mode ω_n(q) response machinery (S99); transit's R1 kernel construction (workshop T1).
3. **Gate**: PASS iff |c_odd|/|c_even| ≤ 10⁻³ (odd-coefficient floor on the graded decomposition) AND 3·p_local(τ)·(1+w)|_{w=0} ∉ [0.95, 1.05] on > 95% of the regression tail (no dilution-mimic window). FAIL on either conjunct demotes the wall's relic-sector clause (d) from argument-grade to coincidence-bounded, and the Stage-1 entry text is amended BEFORE any Stage-2 dispatch. INFO band: odd-floor passed but mimic-window present on ≤ 5% of the tail (window documented, clause (d2) carries it).
4. **Effort**: ~1 wave (1D post-processing + GGE correlator assembly on existing caches; no diagonalization).

Thresholds are negotiable at R2 ONLY — before any compute, per plan-freeze discipline. If transit constructs NO viable candidate at R1, the scaffold is NOT emitted and clause (d) carries the argument-grade tag with Q-T1's window check folded into CF-S101 diagnostics instead (zero new gates).

**(iv) Routing summary for the Workshop Verdict table.** Row 4 resolves as: Stage-0 candidate text = drafted (clauses a-c, e, f here; d at transit R1; frozen at R2); sibling = conditional scaffold pre-built; CF-S101-W1-QEQ-SELFCONS delta = 0 (spec), +2 non-gating annotations (citation clause; amplitude-law diagnostic).

**Question for transit:** for clause (d), do you want the dilution-window bound (d2) stated as a backbone-specific numerical fact (your Q-T1 output, frozen into the clause) or as a structural statement with the window check delegated to the sibling/CF diagnostics? I prefer the former if Q-T1 lands at R1 — a Stage-1 entry with a number in it is harder to mis-cite than one with a pointer.

### V5: Cross-Cutting Observations

**1. Laboratory grounding — the partition IS the Landau-Khalatnikov force taxonomy reduced to 0+1 dimensions.** Paper 35 §II (`researchers/Volovik/35_2024_Volovik_Landau_Khalatnikov_Two_Fluid_de_Sitter.md`) names two-fluid hydrodynamics the cornerstone of the corpus's vacuum program. In the laboratory two-fluid system the force classes sort exactly as the theorem requires: thermodynamic POTENTIALS depend on the counterflow evenly (the LK energy carries w² = (v_n − v_s)²; the fountain/thermomechanical pressure is built from ∫ρs dT-type even potentials); the odd-in-velocity forces are EITHER dissipative (mutual friction) OR transverse-gyroscopic (Magnus, Iordanskii — requiring the vorticity vector κ, hence ≥ 2 dimensions). The substrate q-channel IS a 1-dof system — not "like" one — and under the 1-dof reduction the gyroscopic column of the LK taxonomy is structurally empty (V1 chain B). The H-parity theorem is therefore not an ad hoc cosmological assertion: it is the LK force taxonomy's image in 0+1d, with the corpus's own dS thermodynamics (Papers 11, 35) supplying the state functions. The one genuinely cosmological novelty has no laboratory counterpart: the H-odd entropy itself (Paper 11 §VI — the lab has no negative-T contracting branch; the substrate does).

**2. T-covariance bookkeeping (a compact consistency check on the whole structure).** Grade the gate's EOM under t → −t: q̈ (even), 3Hq̇ (odd × odd = even), k_curv(q − κ₂H²) (even, since H² even). The EOM with the GD drive is fully T-COVARIANT — the time-reverse of an expanding-backbone solution solves the contracting-backbone equation; irreversibility is branch selection (damping for H > 0, pumping for H < 0), not equation asymmetry. The imposed closure q_eq = cH makes the EOM T-NON-covariant — it injects T-breaking with no substrate source identified. That is the deepest formulation of why the closure is "imposed": T-covariance of the effective q-channel EOM is equivalent to (even-parity potential drives) + (H-odd friction coefficients), and breaking it honestly requires a T-asymmetric source. The substrate HAS one — the relic state (the transit broke T; P_exc = 1.000) — which is exactly the structural license Reading B senses; V1.v closes its concrete potential-type routes, and the KV carve-out is where its influence legitimately lands (branch selection of the decaying envelope, q_amp ∝ |H|: a T-even law on a T-selected branch).

**3. Drive vs back-reaction, in two-fluid language.** A "drive" q_eq(H) on a fixed backbone is the image of an EXTERNALLY IMPOSED counterflow; the KV self-consistency is the image of letting the normal-component density itself enter the closure. Paper 35 §V's two-component dynamics — vacuum + gravitational stiff matter (w = 1) with ENERGY EXCHANGE, both decaying power-law to correct present-day magnitudes — is the corpus blueprint for the refinement ladder above CF-S101-W1-QEQ-SELFCONS: the CF's two-component design (q + backbone) is the minimal rung; the Paper 35 Eqs. (18)-(19) (K,𝓡)-pair dark-matter pressure is the next rung if the CF lands INFO. Flag for the S101 planner; no spec change now (V4.ii).

**4. n_eff triangle ownership (downstream hygiene).** The cross-session triangle {2.3, <2, ~4.11} mixes values living at DIFFERENT closure levels; its coherence adjudication is OWNED by the S100b schedule. This workshop contributes exactly one pin: the ~4.11 member is the fixed-backbone equilibrium-GD drive law (n = 2 × 2.0556, corridor-map value), tagged per V3.iv.2 — not the framework's physical n_eff prediction, which rides on CF-S101's verdict.

**5. The durable constraint-map object is the slope-selection rule, not the FAIL.** What should enter the permanent record from this gate + workshop is: **equilibrium analyticity selects late-tail slopes in {2, 4, ...}; amplitude self-consistency selects 1; nothing substrate-internal selects anything else on a fixed backbone (Markovian, analytic, 1-dof — scope per V1)**. The FAIL verdict is this rule's fixed-backbone instantiation. Future "substrate q_eq(H) drive" proposals check H-parity and analyticity FIRST — one line of grading before any ODE integration. This converts a closed corridor into a standing pre-filter, which is the correct economy: the gate cost a wave; the rule costs a substitution chain.

**6. Two record-hygiene flags (for the audit trail; effected post-workshop, not here).** (a) My agent memory `qeq-drive-h-parity-100a.md` carries the pre-workshop phrasing "the odd-in-H sector is dissipative" — to be updated to the corrected scoped form (V2.v) after the workshop closes; agent-private housekeeping, flagged for traceability. (b) The knowledge-MCP `R_therm` constant note carries "never thermalizes," a phrasing RETRACTED at S39 (atlas-04 T3 BROKEN; t_therm ≈ 6 M_KK⁻¹ is finite — what survives is the diabatic-freeze ratio R_therm = 5251.82 and fabric-scale integrability protection). The workshop text above already uses the precise form (occupations frozen at the fold; no local-equilibrium description applies); the constant-note touch-up routes to the orchestrator's hygiene pass, not to this workshop.

**7. What I am NOT claiming (pre-empting R2 drift).** I am not claiming the relic sector is theorem-closed (it is argument-closed, three arguments, each falsifiable: Q-T1 numerically, Q-T2 by construction, Q-T3 by exhibiting a second coordinate). I am not claiming the dS coefficients are valid at the spike (conceded, V2.iii, with |Ḣ|/H² ≈ 1.6×10²). I am not claiming odd-in-H terms are impossible in nature — only that the equilibrium route cannot source them (theorem), the identified non-equilibrium routes do not (argument), and the slope-1 target never needed them anyway (|H| is even — the carve-out is parity-consistent). The wall, correctly scoped, is narrower and harder than the verdict string suggests.

---

## Round 1 — transit: Response & Cross-Synthesis

### Part 1: Response to volovik's Sections

#### Re: V1 — Partition Exhaustiveness

**AGREE — retraction (i), chain A, and the |H| collapse (vi) for secular couplings.** The retraction is correctly located: the over-claim was the WP parenthetical "odd ⟹ dissipative," and Paper 11 §VI's contracting-dS equilibrium branch (T < 0, S = −A/4G) is the corpus's own counterexample. Chain A's Step 5 is the load-bearing generalization and I verify it independently (every parity claim I endorse gets its own chain, per `math-scripts.md`):

```
Claim: F(T) = Int_0^T s(T') dT' is EVEN for ANY odd s — not only the linear s = (3pi/4G)T.

Step 1: F(-T) = Int_0^{-T} s(T') dT'                       [definition]
Step 2: substitute T' = -u, dT' = -du; limits T' : 0 -> -T  ==>  u : 0 -> T
        F(-T) = Int_0^{T} s(-u) (-du) = -Int_0^T s(-u) du
Step 3: s odd ==> s(-u) = -s(u)
        F(-T) = -Int_0^T [-s(u)] du = +Int_0^T s(u) du = F(T)
Conclusion: F even. Independent of linearity, coefficients, convention (H/pi vs H/2pi). ✓
```

This is why the theorem-grade core is robust: it consumes only the ODDNESS of (T, s), which the corpus anchors physically (Paper 11 §VI), never the coefficients (κ₂-irrelevant by XC-5 at 7.6e-8).

**Q-T1 — ANSWERED: the dilution-mimic window is EMPTY, fraction 0.0000 EXACT, from documented values alone (no script run).** Full substitution chain:

```
Claim: 3·p_local(tau) never enters [0.95, 1.05] on the regression tail — nor anywhere
       on the 999-point backbone.

Step 1: p_local := -H^2/(dH/dtau)                  [Q-T1 definition; consistency check:
        a ∝ t^p ==> H = p/t, H' = -p/t^2 ==> -H^2/H' = p ✓ recovers the power-law index]
Step 2: deceleration q_dec := -a''a/a'^2 = -1 - H'/H^2     [the W1-1 observable; NOTE the
        naming collision: q_dec = deceleration, q = Volovik vacuum variable — distinct]
        ==> H'/H^2 = -(1 + q_dec)
Step 3: substitute Step 2 into Step 1:  p_local = 1/(1 + q_dec)
Step 4: window condition  3·p_local ∈ [0.95, 1.05]
        <==> p_local ∈ [19/60, 21/60] = [0.31667, 0.35]
        <==> (1 + q_dec) ∈ [60/21, 60/19] = [2.857, 3.158]
        <==> q_dec ∈ [1.857, 2.158]        [stiff-fluid-class deceleration: w = 1 has q_dec = 2]
Step 5 (documented bound): q_dec ≤ +0.81 at ALL 999 backbone points.
        Source: S100a-W1-1 miss_above_band = 0.000000 (verdict line 12; WP §W1-1 —
        "every out-of-band point lies BELOW −0.97"), with q_corrected ≡ q_bare EXACTLY
        (map_0 identity theorem, A ≡ 1, B ≡ 0) and the SAME backbone as W1-2
        (XC-4: arr_H_traj ≡ arr_H_bare_t, max|ΔH| = 0.0).
        0.81 < 1.857  ==>  the window set is EMPTY at every grid point, a fortiori on
        the n_tail = 500 regression tail (a subset).
Step 6 (margin, by q_dec sector):
        q_dec ∈ (−1, 0.81]:  3p_local = 3/(1+q_dec) ≥ 3/1.81 = 1.657 > 1.05  (58% clearance);
        q_dec < −1 (deep-acceleration excursions, incl. the H'-spike where H' = +4.41 > 0):
                    p_local < 0  ==>  3p_local < 0 < 0.95;
        q_dec = −1 exactly (local dS): p_local undefined — no power law, not in the window.
Conclusion: window fraction = 0.0000 EXACT; closest approach from above is 1.657.
The dilution-mimic candidate is DEAD on this backbone — no scan needed, and the result
should be FROZEN into clause (d2) per V4's stated preference.
```

Two riders. (1) The pinned backbone is NOT a single-fluid Friedmann background (it is the substrate's own a₂-channel history), so chain C's "structurally 2" is itself replaced here by the documented transmitted-slope range 3p_local ∈ [1.657, ∞) ∪ (−∞, 0): on THIS backbone a dilution tilt never transmits 1 (window empty, 0.0000 exact), while 3p_local sweeps the band [1.657, 3.000] CONTAINING 2 on the 33.2% decelerating grid mass (pointwise slope-2 transmission realized wherever q_dec = 1/2; the max-q_dec point transmits 1.657, not 2) [corrected R2-B per D-1: the original phrasing "transmits neither 1 nor exactly 2" overstated pointwise] — the window-empty conclusion is what carries. (2) The chain is pointwise; no monotonicity of H is assumed (the tail contains the H′ = +4.41 spike, where H is locally growing — Step 6 covers it: p_local < 0 there).

**DISAGREE — chain B's premise, not its algebra. Q-T3 ANSWERED: the second coordinate exists and is NAMED — it is ln a, the dilution coordinate.** The 1×1-antisymmetric-matrix step is correct; the premise N = 1 is inapplicable to the gate's own design. Pinning the backbone PROMOTES a(τ) to an external slow parameter, and the relevant arena is the 2-parameter slow manifold (q, ln a). This is not exotic: it is the Born-Oppenheimer / geometric-magnetism setting (Berry 1985; Berry-Robbins 1993 — methodological citations per `substrate-first-canonical-sourcing.md §(i)`), where a bath adiabatically dragged by TWO slow parameters exerts on them the gyroscopic force F_i = B_ij λ̇_j with B_ij the bath's Berry curvature 2-form. For λ = (q, ln a):

```
F_q^geo = B_{q,ln a}(q, a) · (d ln a/dtau) = B_{q,ln a} · H            (T-eq.1)
```

— q̇-INDEPENDENT, H-ODD (one power of H), workless on the PAIR (antisymmetry) but work-doing on the q-channel alone, since a is externally pinned. Chain B's Step 2 emptied the gyroscopic class by counting q alone; the fixed-backbone design itself injects the second velocity. And the second coordinate is not "secretly multi-dof" relic structure: with {n_k} frozen, the relic's state manifold is EXACTLY 1-parameter — a is the only coordinate the relic has. So the named pair is (q, ln a), and T-eq.1 is the precise object volovik's Q-T3 asked for.

HAVING reopened the slot, I then close it myself — by bath structure, not dof-counting (this is the sharpening, and it changes the scope line):

```
Claim: B_{q,ln a} = 0 EXACTLY for the diagonal (number-sector) relic bath;
       leakage only through squeeze-phase rotation, bounded and non-secular.

Step 1: each relic mode is a generalized oscillator H_k = (1/2)[X x² + 2Y xp + Z p²]
        with Berry curvature 2-form (Berry 1985)
        V_n ∝ (n + 1/2) · [X dY∧dZ + Y dZ∧dX + Z dX∧dY] / (XZ − Y²)^{3/2}.
Step 2: the substrate relic bath is FREQUENCY-modulated only: X = E_k²(q, a),
        Y = 0, Z = 1 — the (q, a)-parametrization never leaves the Y = 0, Z = const slice
        (BdG anomalous terms b b + b†b† are (x² − p²)-class squeeze generators, i.e.
        X–Z axis; the xp + px generator IS the Y axis).
Step 3: pull back V_n to the slice {Y = 0, dY = 0, dZ = 0}:
        X dY∧dZ → 0 (dY = 0);  Y dZ∧dX → 0 (Y = 0);  Z dX∧dY → 0 (dY = 0).
        Pullback ≡ 0.  ==>  B_{q,ln a} = 0 EXACT for the number sector.       (T-eq.2)
Step 4: the relic is NOT in number states — it is the Bogoliubov-squeezed pair state
        (Parker production at the fold, P_exc = 1.000). Squeeze-AXIS rotation is the
        Y-generator; the documented squeeze phases are REAL to 0.005–0.012 rad
        (S95 W6-6 / S76 W1-C lineage; transit agent-memory record).
        ==> curvature leakage = O(φ_k) ≈ 0.5–1.2% of the already-first-order term,
        AND it rides phases rotating at pair frequencies 2E_k ≥ 2Δ_BCS — non-secular
        off resonance (T2 below quantifies the dephasing stack).
Conclusion: the gyroscopic route is CLOSED, but by (Berry-flatness of frequency-only
modulation) + (squeeze-phase smallness) + (pair-band dephasing) — argument-grade with
ONE computable hostage (the resonance position, T1-C2/T2) — NOT by 1-dof algebra.
```

**MISSED — the substrate anchor that closes Iordanskii independently of dimension-counting.** The Iordanskii force needs a quasiparticle COUNTERFLOW (it is ∝ κ × (v_n − v_L)); the substrate certifies the relic comoving with T^{0i}_4D = 0 EXACT (atlas-04 C7 — the same anchor W1-4 consumed for the DM frame resolution). So the Iordanskii prefactor vanishes by an EXACT substrate identity before any 1-dof argument runs; and the Magnus/Iordanskii class additionally lacks scattering kinematics in the homogeneous k = 0 q-channel (nothing to scatter off — no spatial gradient). Chain B is thus TRIPLY covered for this force class: C7 (exact), homogeneity (kinematic), and — where it applies — the 1-dof algebra. I recommend clause (d3) cite C7 first: an exact identity outranks a structural argument.

**Q-T4 — ANSWERED: conceded for secular couplings, with the constructed witness.** The transit DID break T, and the license Reading B sensed is real — but I have now constructed its strongest carriers and they all fail to reach the secular EOM: the relic's T-asymmetry lives in (a) the squeeze phases φ_k, which rotate at 2E_k ≥ 2Δ_BCS and dephase (candidate C5, T1), and (b) the branch selection of the damping envelope — volovik's own "T-even law on a T-selected branch" (V5.2). Every sign(H)-carrying coupling I constructed is either trajectory-equivalent to its even twin on the H > 0 branch (the (vi) collapse) or non-secular (gap-frequency phases). The on-branch collapse stands FOR SECULAR COUPLINGS; the precise residue is the resonance window where "non-secular" fails (T1-C2, T2).

**EMERGES — the partition needs a FOURTH column, and all of Reading B funnels into ONE number.** V1's exhaustiveness verdict ("Markovian, analytic, 1-dof") should be restated: the operative taxonomy is {potential, q̇-coupled, memory} × {SECULAR, OSCILLATORY}. Everything odd-in-H that the relic sector can source lives in the oscillatory column (pair-band phases), and the secular projection of that column vanishes by T-eq.2 + dephasing — EXCEPT on resonance, 2E_k ≈ ω_q, where oscillatory rectifies into secular. The 1-dof clause in the scope line should be REPLACED by the bath-structure clause: "exhaustive for Markovian-reducible (off-resonant), analytic, frequency-modulated-bath dynamics." Q-T1's window is dead exactly; the resonance window is the single surviving numerical hostage, and it is one unit-conversion check (T3 Q-V2, sibling conjunct C).

#### Re: V2 — dS-Equilibrium Imports

**AGREE — the grading argument, verified, and the layer split it rests on.** The QUANTITATIVE/STRUCTURAL split is the right surgery. I verify the grading table's load-bearing entry independently:

```
Claim: x1 = Hdot/H² is g-EVEN under t → −t.
Step 1: g(H) = −1 (odd; H = ȧ/a with a even, d/dt odd).
Step 2: g(Hdot) = g(d/dt)·g(H) = (−1)(−1) = +1 (even).
Step 3: g(H²) = (−1)² = +1 (even).
Step 4: g(x1) = g(Hdot)/g(H²) = +1/+1 = +1. EVEN. ✓
General: g((d^n H/dt^n)/H^{n+1}) = (−1)^{n+1}/(−1)^{n+1} = +1 for all n. ✓
```

So odd-anchored prefactors (T, s) × even gradient ratios = odd state functions, and ∫s dT even — per order. I also AGREE with V2.iv as a freestanding kill: a Ḣ-sourced drive transmits tail slope d ln|Ḣ|/d ln H = 2 on every power-law stretch (chain verified: Ḣ = −H²/p ⟹ ln|Ḣ| = 2 ln H − ln p). My candidate C6 (T1) lands on exactly this blade — constructed and conceded there.

**ANSWER to V2's question — I accept the per-order grading at the spike, with the strata QUANTIFIED from documented values and one premise-sharpening.** The logic I accept: parity is order-by-order; graded partial sums and their limits preserve it; breaking it requires structure non-perturbative in gradients, i.e. a sector with no local-equilibrium description — which is clause (b) territory by definition, not a failure of the equilibrium import. I do NOT contend the expansion fails to define graded state functions "everywhere on the tail." What the documented values pin about WHERE it is quantitatively reliable:

```
Stratum map from W1-1's own miss histogram (same backbone, XC-4):
Step 1: x1 = −(1 + q_dec)            [Re:V1 Step 2]
Step 2: |x1| < 1  <==>  |1 + q_dec| < 1  <==>  q_dec ∈ (−2, 0).
Step 3 (documented masses, full 999-grid):
        q_dec ∈ (−0.97, 0):   fraction = 0.6677 − 0.4985 = 0.1692
                              [accelerating fraction − miss_below_band, WP §W1-1]
        q_dec < −0.97:        fraction = 0.4985 — this set STRADDLES the strata:
                              q_dec ∈ (−2, −0.97) is still |x1| < 1 (near-dS is the
                              BEST quasi-static region: q_dec → −1 gives x1 → 0),
                              while the deep-acceleration excursions (q_dec ≈ −165 at
                              the spike, −514 at the documented extreme) have x1 ≫ 1.
        q_dec ∈ (0, 0.81]:    in-band decelerating mass; |x1| ∈ (1, 1.81] — volovik's
                              "marginal, O(1)" stratum.
Conclusion: theorem-grade-QUANTITATIVE stratum fraction ∈ [0.169, 0.668] of the grid
(lower bound documented exactly; upper bound over-counts the excursions). The exact
split, and its tail-restriction, need the npz — ONE sibling diagnostic, pre-specified.
```

Note the pleasant inversion this exposes: the miss-set (q_dec < −0.97) is NOT uniformly bad-stratum — it CONTAINS the near-dS points (x₁ ≈ 0, the best quasi-static region) AND the excursions (x₁ ≈ 160–510, the worst). W1-1's miss histogram IS W1-2's regime diagnostic — see EMERGES below.

The premise-sharpening (T3 Q-V4): GD-4 evaluates δμ at dP = 0. The pressure-balance condition is itself an equilibrium premise, and on the excursion set (x₁ ≫ 1) it shares the quantitative unreliability of the coefficients. Parity is unaffected (dP = 0 is g-even as a condition: P is built from even potentials). I propose regime clause (a) carry one added sentence: "the dP = 0 balance premise of GD-4 shares the same quantitative regime restriction as the coefficients."

**MISSED — my domain's quantitative bound on what the spike can DO to the slope.** The ε_ad = 0.897 passage is a Landau-Zener-class single marginal traversal (drive log-rate d ln q_eq/dτ = 2Ḣ/H reaching 0.897·ω at one point). Its secular footprint on the run is ALREADY MEASURED by the gate's own diagnostics: the tracking-lag excess +0.0556 (XC-1: 2.0556 vs the locked 2) and the generic-IC ringing systematic ±0.2 (XC-6). Together these bound the backbone-non-adiabaticity correction budget on this backbone at |Δslope| ≲ 0.26 — a factor ~4 below the |Δslope| = 1.056 needed to carry the GD drive to slope 1. Scope this bound precisely: it bounds DYNAMICAL CORRECTIONS to a given drive's transmitted slope (lag, ringing, spike transients); it does NOT bound a structurally new tilt term, which would change the slope by domination, not perturbation — that is why T1's candidates are constructed as new terms, and why their amplitude question (suppression stack) is separate from this budget. Within its scope, the bound retires a whole sub-family of Reading-B hopes: no amount of "the backbone is locally non-adiabatic" can move 2.0556 to 1 through transmission physics. ε_ad = 0.897 < 1 keeps the q-channel in the adiabatic-with-corrections class — nowhere near the fold's diabatic regime (R_therm = 5251.82 belongs to the TRANSIT, a different process on a different clock; T2 scopes this).

**EMERGES — cross-gate regime cartography.** W1-1 (frame-map gate) and W1-2 (parity gate) ran on the identical backbone (XC-4, max|ΔH| = 0.0), and W1-1's one-sided miss structure doubles as the parity theorem's stratum map at zero additional compute: theorem-grade-quantitative where q_dec ∈ (−2, 0), marginal where q_dec ∈ (0, 0.81], coefficient-dead on the excursion set. The Stage-1 entry can carry the stratum bound [0.169, 0.668] WITH provenance (W1-1 verdict line 12 + XC-4) now, and the sibling tightens it to the exact tail-restricted split. A regime clause with a documented number in it is harder to mis-cite than one with adjectives — same principle volovik invoked for (d2).

#### Re: V3 — Citation Form

**AGREE — the two-register resolution, with the quantifier-range point conceded to Reading A.** The token's quantifier range was NOT ambiguous at pre-registration: plan §W1-2 Definition 4 explicitly enumerated the drive candidates ((i) Gibbs-Duhem μ-tilt, (ii) §6.3 inversion) and the fixed `arr_H_bare_t` backbone; the WP Assessment states the KV mechanism is "structurally outside this gate's fixed-backbone design." Within that register, `no_slope1_capable_substrate_drive` is exactly what was shown. The verdict line is PERMANENT and correct; no verdict-file action exists.

**ANSWER to V3's question — I exhibit the realistic mis-citation pathway, and it selects the MIDDLE strengthening, not full deprecation.** The expansion rule binds citers who read rules. One consumer class does not: **mechanical knowledge-MCP retrieval**. The demonstration is in this wave's own audit trail — the W1-2 MCP Pre-Compute Audit retrieved its predecessor as a bare verdict string: `trace_entity("RELAXATION-CLOSURE")` → "canonical verdict string recovered: slope_bare_UNFORCED=3.415925 … forced_only=True …" (WP §W1-2, MCP audit item 3). A future agent running `search_knowledge("substrate q_eq drive slope")` at S10x plan-freeze will surface `no_slope1_capable_substrate_drive` as an FTS hit STRIPPED of the workshop's scope clause, and a pre-compute audit will conclude "no substrate drive exists — gate pre-closed" — silently retiring the KV carve-out AND the resonance-window sibling. This is precisely the Class-(c) PIN-DRIFT-FROM-STALE-SOURCE mechanism (`regulator-pin-discipline.md` §Class-(c)): a plan threshold citing a pre-supersession view of what a verdict means. The expansion rule cannot block it because the retrieval layer never reads the rule.

The fix is to lodge the scoped sentence WHERE the mechanical retrieval lands, not (only) in a discipline citers must remember:

1. **Token retained** — it is a permanent verdict line and correct in-register; deprecation is both impossible (verdict permanence) and wrong (the register is valid).
2. **Expansion rule adopted as drafted** (V3.iii three qualifiers + carve-out pointer) for human/agent citers.
3. **Retrieval-layer amendment (the strengthening)**: the canonical citation paragraph (V3.iii) must live in the FTS-indexed artifacts adjacent to the verdict string — concretely: (a) this workshop's Workshop Verdict table row carries the scoped one-liner verbatim (the workshop file is extractor-indexed); (b) the S100b w1 closure reading inherits the paragraph verbatim (already volovik's V3.iv.1); (c) a knowledge-MCP entity-note touch-up parallel to volovik's own V5.6b R_therm flag — the gate-entity note gains the one-line scope pointer ("scope: equilibrium sector theorem-grade; relic argument-grade; KV carve-out CF-S101-W1-QEQ-SELFCONS") — routed to the orchestrator hygiene pass, same channel as V5.6b.

With (3), the worst-case mechanical consumer surfaces the scope clause in the SAME query that surfaces the token. That closes the one pathway I can construct; I am satisfied the two-register resolution + retrieval-layer amendment is citation-complete, and I do NOT ask for token deprecation.

**One wording nit on the pinned citation text (V3.iii), for R2 freeze.** "never-equilibrated GGE relic sector — excluded at argument-grade (frozen occupations + dilution-slope-2 + 1-dof gyroscopic exclusion …)" — per my Re:V1/T1, the third item should read "+ bath-structure gyroscopic closure (Berry-flat frequency-modulation; squeeze-phase leakage ≤ 1.2%; C7 zero-counterflow) pending the sibling resonance check" — the 1-dof clause alone is not the operative closure, and "dilution-slope-2" can carry the Q-T1 exact-zero window result parenthetically. Also "never-equilibrated" should be "fold-frozen" (the S39-corrected framing volovik's own V5.6b enforces: t_therm is finite; what is certified is the freeze at transit, R_therm = 5251.82 — verdict file line 82).

#### Re: V4 — Routing

**ANSWER to V4's question — freeze the NUMBER into (d2).** Q-T1 landed at R1 with an exact result and a fully documented provenance chain (Re:V1: window fraction = 0.0000, margin 1.657 > 1.05, from W1-1 `miss_above_band = 0.000000` + the map_0 identity + XC-4 backbone identity). Per volovik's stated preference — which I share, and which Re:V2's stratum bound applies a second time — the Stage-1 clause carries the number with its provenance, not a pointer. A clause with `0.0000 exact (requires q_dec ∈ [1.857, 2.158]; documented max +0.81)` in it cannot be mis-cited into "the window was never checked."

**Clause (d) — transit-authored draft (replacing the V4.i offered content; negotiation deltas marked).**

> **Clause (d) [transit-side]: Non-equilibrium-sector exclusion boundary.** (d1) At adiabatic order ZERO the fold-frozen relic tilt F_GGE = −Σ_k n_k ∂_q E_k(q, a) is functionally H-independent at fixed (q, a) [frozen occupations; diabatic transit-freeze R_therm = 5251.82, S95-certified, verdict-file line 82; the order-zero qualifier is load-bearing — the first-order response LAG does carry H, see (d4)]. (d2) Dilution-trajectory transmission: a relic dilution tilt transmits late-tail slope 3·p_local·(1+w)|_{w=0} = 3p_local with p_local = 1/(1+q_dec); the slope-1 mimic window 3p_local ∈ [0.95, 1.05] requires q_dec ∈ [1.857, 2.158] (stiff-fluid-class deceleration), while the documented backbone maximum is q_dec ≤ +0.81 at all 999 points (S100a-W1-1 miss_above_band = 0.000000; backbone identity XC-4) — **window fraction = 0.0000 EXACT**, closest approach 3p_local = 1.657; the dilution-mimic route is dead on this backbone. (d3) Gyroscopic/geometric route: the fixed-backbone design promotes the dilution coordinate ln a to a second slow parameter — the gyroscopic class on the (q, ln a) pair is NOT emptied by dof-counting; it is closed by bath structure: (i) Berry-flatness — the relic bath is frequency-modulated only (Y = 0 squeeze-axis slice), where the generalized-oscillator Berry curvature pulls back to zero EXACTLY; (ii) squeeze-phase leakage is bounded at O(φ_k) ≈ 0.005–0.012 rad [S95 W6-6 / S76 W1-C lineage] and rotates at pair frequencies ≥ 2Δ_BCS (dephased off-resonance; 59.8-pair incoherent stacking adds ~1/√N ≈ 0.13); (iii) the Magnus/Iordanskii class vanishes independently by zero counterflow, T^{0i}_4D = 0 EXACT [atlas-04 C7], and by homogeneity (no scattering kinematics in the k = 0 channel). (d4) Memory slot (SCOPED, not open-ended): the relic kernel's Markovian reduction is controlled off-resonance and even-graded at SECULAR order (constructive decomposition, workshop T1-C4/T2); its secular outputs are exhausted by {δk_curv(a) even-reactive; δΓ on-shell friction (present only if ω_q lies above the pair threshold — same units check as the resonance); the order-zero adiabatic tilt of (d1)}; the unique surviving odd-channel is parametric rectification at 2E_k ≈ ω_q — bounded by the sibling gate's resonance conjunct (C); absent a tail crossing, the relic sector admits NO secular odd-in-H potential term. (d5) Pincer closure on the freeze premise: if the gate window instead OUTLASTS t_therm ≈ 6 M_KK⁻¹ (S39-corrected finite thermalization), the relic sector acquires local-equilibrium state functions and falls under clauses (a)-(c) directly — frozen ⟹ (d1)-(d4); thermalized ⟹ the parity THEOREM applies; only the transient crossover window escapes both, bounded by t_therm (units-check folded into sibling conjunct C).

Deltas vs volovik's offered (d1)-(d4): (d1) gains the "order zero" qualifier (honesty about where C1 lives); (d2) gains the frozen number; (d3) is RESTRUCTURED — dof-counting demoted from operative closure to corroborating algebra, bath-structure closure (Berry-flat + leakage bound + C7) promoted; (d4) is scoped constructively rather than declared open; (d5) is NEW (the pincer).

**Sibling gate: EMIT, with one amendment.** My R1 candidates (T1) engage and evade the three GGE closure arguments as stated and die only on a FOURTH argument (secularity/Berry-flatness/gap) whose single numerical input — the position of ω_q = √k_curv = 59.888 (backbone units) relative to the pair band [2·min_k E_k, 2·max_k E_k] of the 992-mode ω_n(q) response, in COMMON units — is not resolvable from documented values (the one unit conversion this workshop lacks). That is exactly volovik's emission condition: a constructed candidate not yet classified dead. Amended spec (deltas to the V4.iii scaffold marked):

1. **What**: graded decomposition of the GGE-relic-induced effective force on the q-channel: **(A)** odd-coefficient floor on the t→−t-graded Markovian reduction of the relic kernel (diagonal + anomalous sectors) [unchanged]; **(B)** verification-assert of the analytic dilution-window result — assert max(q_dec) < 1.857 on the tail and report the realized min/max of 3p_local [DOWNGRADED from scan to assert: Q-T1 resolved it analytically]; **(C) [NEW]**: resonance/threshold position — convert ω_q and the 992-mode pair band to common units via the S99 k_curv construction provenance; report Δ_res = min_k |2E_k − ω_q|/ω_q, whether any crossing 2E_k(a(τ)) = ω_q occurs on the tail, and the window-duration vs t_therm check (d5).
2. **Inputs**: volovik's V4.iii list + the S99 k_curv construction script/npz (the unit-conversion provenance) [delta: one input added].
3. **Gate**: PASS iff |c_odd|/|c_even| ≤ 10⁻³ AND the (B) assert holds AND Δ_res ≥ 0.1 with no tail crossing; INFO iff the only miss is Δ_res < 0.1 with no tail crossing (near-resonant — documented, clause (d4) carries it); FAIL iff a tail crossing exists OR the odd-floor is violated [delta: the (B) window-fraction conjunct of the scaffold is replaced by the assert; the Δ_res conjunct added]. Proposed Δ_res floor rationale (negotiable at R2, pre-compute): parametric-resonance half-width ~ (h/2)·ω at modulation depth h; here h ≲ O(φ_k · ∂ln E/∂ln a) ≲ 0.01, so width ≲ 0.5% of ω_q — a 10% clearance is ≥ 20× the width.
4. **Effort**: ~1 wave [unchanged — conjunct C is one unit-conversion + band comparison + two asserts].

FAIL routing as volovik drafted: relic clause demoted argument-grade → coincidence-bounded, Stage-1 text amended BEFORE Stage-2 dispatch.

**Delta to CF-S101-W1-QEQ-SELFCONS: ZERO — confirmed from the consumer side.** The CF spec (WP Carry-Forward block: re-derive H from q-oscillation energy through §6.3; gate |slope_selfcons − 1| ≤ 0.05, domfrac ≥ 0.95; ~1 wave) is untouched. The sibling and the CF are LOGICALLY INDEPENDENT probes of disjoint quantifier ranges: sibling = drive slot on the fixed backbone (can the relic source a tilt?); CF = back-reaction (does the backbone respond?). Both should run; neither's verdict pre-judges the other. I also ENDORSE, specifically from the transit side, volovik's V4.ii non-gating amplitude-law diagnostic: regressing ln q_amp vs ln |H| directly is the right discriminator because it tests the NON-ANALYTIC-EVEN form itself — a PASS realized through q_amp ∝ |H| confirms the slope-SELECTION rule (V5.5), not merely the slope; a PASS realized any other way would be a NEW anomaly worth its own gate. The decaying-envelope physics is squarely my domain: the oscillation amplitude is the adiabatic-invariant carrier (q_amp² ω ≈ const modulo Hubble damping), so the |H|-law is a WKB-grade prediction on the self-consistent background, and the diagnostic costs one regression.

#### Re: V5 — Cross-Cutting

**AGREE (V5.1, LK taxonomy) with the refinement Re:V1 forces.** The 0+1d reduction of the Landau-Khalatnikov force taxonomy is the right laboratory grounding, with one column corrected: the gyroscopic column is emptied not by dimension-counting alone but by bath structure (Berry-flat frequency modulation + C7 zero-counterflow + dephasing) — the (q, ln a) pair gives the gyroscopic class a 2-parameter arena even in the "1-dof" channel. The lab analogy sharpens rather than breaks: in two-fluid hydrodynamics too, the Iordanskii force needs counterflow (v_n − v_L ≠ 0), and the substrate certifies T^{0i}_4D = 0 EXACT — the substrate IS a zero-counterflow two-fluid state, so the lab taxonomy's transverse column is switched off by the state, not the geometry.

**AGREE (V5.2, T-covariance bookkeeping) — and this is where the workshop's deepest joint result sits.** The formulation "T-covariance of the effective q-channel EOM ⟺ (even potential drives) + (H-odd friction coefficients)" plus my constructed witnesses (T1-C5) yields the precise statement of how the relic's genuine T-asymmetry fails to reach the secular EOM: the transit's T-breaking is stored in squeeze phases rotating at pair frequencies ≥ 2Δ_BCS, which dephase (with 1/√59.8 incoherent stacking on top), leaving branch selection as the ONLY surviving T-asymmetric imprint — volovik's "T-even law on a T-selected branch," now with the storage mechanism and its two suppression scales named. EMERGES: the slope-selection rule (V5.5) gains a THIRD selector — equilibrium analyticity selects even integers; amplitude self-consistency selects 1; SECULARITY (phase-averaging over the gapped pair band) suppresses everything else, with its single failure window (resonance) pre-registered in the sibling. That three-selector form is what I propose the permanent record carry.

**AGREE (V5.3, drive vs back-reaction in two-fluid language; V5.4, triangle ownership).** On V5.4 from the transit side: the ~4.11 member is a corridor-map value of the fixed-backbone GD law (n = 2 × 2.0556) — I add only that the 2.0556 itself contains the +0.0556 tracking lag (XC-1), so any S100b consumer comparing n-values at the 0.1 level must use 2 × 2 = 4 (the locked exponent product) for structural comparisons and 4.11 for as-measured comparisons; the tag should say which it carries. Mandatory-tag text as drafted in V3.iv.2 is endorsed with that one clarification.

**AGREE (V5.5) — the durable object is the rule, not the FAIL — with the T1 addendum.** The standing pre-filter ("check H-parity and analyticity FIRST, one grading line before any ODE") extends by one line: "…and check SECULARITY (does the candidate's odd structure ride a gap-frequency phase?) — if oscillatory and off-resonant, it is dead at the same desk." Three of my six constructed candidates (C1, C2, C5) die at exactly that line; pre-filtering them costs a sentence each, which validates the economy claim.

**AGREE (V5.6, hygiene flags) — and (V5.6b) is load-bearing for MY side too.** The S39-corrected framing (fold-frozen occupations, finite t_therm ≈ 6 M_KK⁻¹, R_therm = 5251.82 as the freeze-ratio) is what makes my (d5) pincer well-posed: "never thermalizes" would have made the frozen branch of the pincer unconditional and hidden the crossover window. My own agent memory carries the corrected framing (THE ORDERED VEIL = diabatic transit-freeze, S95-certified); no transit-side memory touch-up needed beyond recording this workshop's outcome.

**On V5.7 (what volovik is NOT claiming)** — the pre-empt list is accurate and I confirm the R1 exchange landed inside it: my candidates attack exactly the three falsifiable joints volovik named (Q-T1 numerically — resolved, window empty; Q-T2 by construction — prediction confirmed at secular order, counter-construction exhibited at oscillatory order; Q-T3 by exhibiting the second coordinate — exhibited, ln a, then closed by bath structure). The wall as scoped is indeed narrower and harder than the verdict string — which is the workshop's whole product.

### Part 2: Original Analysis

#### T1: Strongest Non-Equilibrium Odd-in-H Candidates (Constructed)

Construction discipline: each candidate is built on the GGE-relic / transit-freeze / backbone-dynamics axis, given its explicit mechanism and odd-in-H structure, and tested against volovik's pre-built machinery (closure-1 frozen-occupations; closure-2 dilution-slope; closure-3 architecture-collapse; chain B gyroscopic; V2.i grading; V1.vi on-branch collapse). The Bogoliubov/GGE structure is the one my domain owns: the relic IS the two-mode-squeezed output state of Parker pair production at the fold (P_exc = 1.000, n_pairs = 59.8; deep-sudden regime δt/T_L = 1.25e-5, R_therm = 5251.82 — verdict file line 82), with frozen occupations {n_k}, anomalous correlators σ_k = ⟨b_k b_{−k}⟩, and squeeze phases φ_k real to 0.005–0.012 rad (S95 W6-6 / S76 W1-C lineage). The q-coupling is the SAME ∂_q E_k response that built k_curv (S99 992-mode ω_n(q) machinery) — so every candidate below uses only machinery the gate itself already certified exists.

**C1 — Adiabatic-lag polarization drag (diagonal relic sector).** Mechanism: the order-zero relic force is the adiabatic tilt F⁰ = −Σ_k J_k ∂_q E_k (J_k the frozen action/occupation; volovik's closure-1 object). But the bath response LAGS the instantaneous spectrum: for a mode with slowly varying E_k(t) = E_k(q(t), a(t)), the first correction to the action is oscillatory, δJ_k ~ (J_k/2)(Ė_k/E_k²)·sin(2θ_k + const), θ_k = ∫E_k dt, giving

```
delta-F_k = −(J_k ∂_q E_k) · [ (∂_{ln a}E_k)·H + (∂_q E_k)·q̇ ] / E_k² · sin(2θ_k)   (T-eq.3)
```

The H-piece is q̇-INDEPENDENT and carries exactly ONE power of H — genuinely g-odd (d/dt acting on the g-even E_k(a): odd × even = odd). Dimensional check: [(∂_{ln a}E)·H/E²] = [E·H/E²] = [H/E], dimensionless rate ratio ✓; [J ∂_q E] = force ✓. Against the machinery: **evades closure-1** (the n_k stay frozen; the H-dependence enters through the response lag, not dn/dt — closure-1 as stated holds only at adiabatic order zero); **evades closure-2** (not a dilution tilt; its transmitted slope is NOT 3p(1+w)); **evades closure-3** (it routes through the EXPLICIT time-dependence E_k(a(τ)) on the pinned backbone — a drive in the gate's quantifier range, NOT back-reaction; the architecture-collapse argument conflates "depends on a" with "depends on H-as-Friedmann-closure"). Fate: the sin(2θ_k) factor rotates at pair frequency 2E_k ≥ 2Δ_BCS — NON-SECULAR off resonance; the secular projection of (T-eq.3) is the geometric term, which is C2. Dies by dephasing unless resonant.

**C2 — Geometric magnetism on (q, ln a) [the Q-T3 second coordinate; STRONGEST candidate].** Mechanism: the secular part of the first-order-in-rates bath response on a 2-parameter slow manifold is the Berry-curvature force F_q = B_{q,ln a}·H (T-eq.1, Re:V1) — q̇-independent, H-odd, and the unique force class whose late-tail slope is EXACTLY 1 BY CONSTRUCTION:

```
Slope chain: F ∝ kappa_1(q)·H with a-INDEPENDENT kappa_1
  ==> q_eq^geo = kappa_1·H/k_curv  ==>  d ln q_eq^geo / d ln H = 1 identically.   (T-eq.4)
More generally kappa_1 ∝ a^{−m}: slope = 1 + m·p_local — the only family that can sit AT 1
with m = 0, rather than passing through it by coincidence.
```

That is why this candidate had to be constructed and closed numerically rather than rhetorically. Against the machinery: evades closures 1–3 for the same reasons as C1; **defeats chain B as stated** (the gyroscopic class on (q, ln a) is not emptied by 1-dof algebra — Re:V1). Fate: B_{q,ln a} = 0 EXACT for the number sector (T-eq.2 Berry-flatness: frequency-only modulation lives on the Y = 0 slice); the squeezed-pair sector leaks curvature only at O(φ_k) ≈ 0.005–0.012 AND riding 2E_k phases (dephased off-resonance, 1/√59.8 ≈ 0.13 incoherent stacking). Residual life: parametric rectification iff 2E_k ≈ ω_q somewhere on the tail — the ONE numerical hostage (sibling conjunct C). Suppression stack if off-resonant: O(φ_k) × O(phase-average) × O(N^{−1/2}) ≲ 10⁻³ of an already-first-order-in-(H/E) term.

**C3 — Iordanskii-analog from relic quasiparticle flux.** Mechanism: transverse quasiparticle-scattering force, the corpus's velocity-odd non-dissipative exhibit. Fate: dead THREE ways — (i) zero counterflow: T^{0i}_4D = 0 EXACT (atlas-04 C7) — the Iordanskii prefactor IS the counterflow flux, certified zero by substrate identity; (ii) homogeneity: the q-channel is the k = 0 mode, no spatial structure to scatter off — the force has no kinematic arena; (iii) chain B's algebra where it applies. CONCEDED — and the concession STRENGTHENS clause (d3): an exact identity (C7) outranks dof-counting.

**C4 — Memory-kernel reduction (the Q-T2 constructive answer).** Mechanism: integrate out the relic exactly; the influence kernel on q is

```
K(t,t') = Σ_k (∂_q E_k)² [ (2n_k+1)·cos(2∫_{t'}^t E_k ds)            (diagonal)
          + 2|σ_k|·cos(2∫ E_k ds + φ_k + ...) (anomalous, squeezed-pair) ]  (T-eq.5)
with the causal response χ(t,t') ∝ θ(t−t')·sin(2∫_{t'}^t E_k ds).
```

The ONLY T-breaking structure is the causal θ(t−t′) — causality, not the relic state. Grading of the Markovian/secular reduction: the principal-value (reactive) part → δk_curv(a), g-EVEN; the on-shell (dissipative) part → δΓ·q̇, the friction slot — and for the gapped bath it is PRESENT only if ω_q exceeds the pair-creation threshold 2Δ_BCS (the same units check as the resonance — if below threshold, δΓ = 0 exactly: no on-shell channel); the static polarization → the order-zero tilt (closure-1's object, H-independent). The non-secular remainder is C1. **Volovik's Q-T2 prediction is CONFIRMED at secular order, with its mechanism identified — Berry-flatness (T-eq.2) is WHY the kernel is even-graded at secular order — and the counter-construction exhibited at oscillatory order (T-eq.3).** No odd potential tilt survives the reduction off-resonance; the prediction holds iff ω_q ∉ pair band — a checkable condition, not yet a theorem.

**C5 — Squeeze-phase T-memory (the Q-T4 witness).** Mechanism: the relic state is T-asymmetric — under t → −t the squeeze phases conjugate (φ_k → −φ_k); an effective term Σ_k |σ_k|(∂_q E_k) cos(2∫_{t_fold}^t E_k ds + φ_k) knows the transit direction. Fate: this is a fast-CLOCK term, not a sign(H) term — its time-dependence is at 2E_k ≥ 2Δ_BCS, it dephases across the 59.8-pair spectrum (incoherent 1/√N plus phase rotation), and on the H > 0 branch it has no secular projection distinguishable from its even twin. CONCEDED to V1.vi: the on-branch collapse holds for secular couplings; the relic's T-memory is stored at gap frequencies and cannot be transcribed into a secular sign(H) coupling.

**C6 — Freeze-out boundary drift (Kibble-Zurek class).** Mechanism: the adiabatic-impulse boundary k̂ sweeps as the backbone rate changes; boundary-crossing transfers relic energy at a rate ∝ d(rate)/dt ∝ Ḣ. Fate: Ḣ is g-EVEN (V2.i grading, verified Re:V2) — the candidate is even-parity at birth, and V2.iv transmits it at slope 2 anyway. Dead twice on volovik's own blades; constructed for completeness because it is the one candidate sourced directly by the ε_ad = 0.897 spike. Corroborating context: the fold production itself is RANGE-controlled, not rate-controlled (rate-flat margin 6.43×; transit agent-memory record of S100b W5-2) — there is no rate-sensitive production channel waiting on the tail either.

**Candidate summary table:**

| # | Candidate | Odd-in-H structure | Evades (as stated) | Killed by | Status |
|:--|:----------|:-------------------|:-------------------|:----------|:-------|
| C1 | Adiabatic-lag drag | (∂_{ln a}E_k)H/E_k² lag, q̇-indep | closures 1, 3 | dephasing (non-secular) | dead off-resonance |
| C2 | Geometric magnetism (q, ln a) | B·H, slope ≡ 1 by construction | closures 1–3 + chain B premise | Berry-flatness (T-eq.2) + φ_k ≤ 1.2% + dephasing | dead off-resonance; **resonance = the hostage** |
| C3 | Iordanskii-analog | κ×counterflow class | — | C7 T^{0i}=0 EXACT + homogeneity + chain B | dead (exact) |
| C4 | Memory-kernel odd tilt | causal θ·sin kernel | closure-1 (order zero) | secular reduction even-graded (= T-eq.2) | dead off-resonance |
| C5 | Squeeze-phase T-memory | φ_k → −φ_k under T | — | gap-frequency dephasing; on-branch collapse | conceded |
| C6 | KZ freeze-out drift | ∝ Ḣ | — | Ḣ is g-EVEN + V2.iv slope-2 | dead (grading) |

**Net T1 verdict (Reading B, fully steelmanned):** no constructed candidate survives off-resonance; three (C1, C2, C4) are the SAME object at different orders of description and funnel into ONE pre-registerable check (sibling conjunct C: ω_q vs the pair band, plus the t_therm window assert). A genuine odd-in-H, slope-1-capable drive on this backbone exists ONLY IF that check finds a tail crossing — and if it does, C2 is the workshop's biggest result; if it does not, clause (d) closes the relic sector at argument-grade with every named route dead and the boundary sharpened from three arguments to four (Berry-flatness/secularity added).

#### T2: Backbone Non-Adiabaticity + GGE-Relic Sector Analysis

**(i) Two clocks, two regimes — R_therm scopes the FOLD, ε_ad scopes the TAIL; conflating them was Reading B's original over-reach.** R_therm = t_therm/t_transit = 5251.82 (verdict file line 82; S95-certified) certifies that the FOLD traversal was deep-diabatic: the relic occupations froze because the transit (δt/T_L = 1.25e-5, deep-sudden) outran every internal response. That is transit-freeze physics — my domain's Bogoliubov-saturation regime (P_exc = 1.000). The q-channel relaxation on the POST-FOLD TAIL is a different process on a different clock: ε_ad = max|2Ḣ/H|/ω = 0.897 < 1 with ω = √k_curv = 59.888 and ~2.5 oscillation periods over the window (WP §W1-2). ε_ad < 1 places the q-run in the ADIABATIC-WITH-CORRECTIONS class — a Landau-Zener-grade single marginal passage at the spike, nowhere near diabatic freeze-out. The diabatic credentials of the substrate (R_therm) therefore do NOT transfer to the q-channel run; what they do is freeze the relic state whose response functions my T1 candidates are built from. Reading B's correct content is "the relic SECTOR never equilibrated" (true, S95); its incorrect extrapolation would be "the q-RUN is non-adiabatic" (false at ε_ad = 0.897 except one marginal point).

**(ii) The spike, quantified, and what it already cost the gate.** At the spike: Ḣ = +4.41, H ≈ 0.164 (V2.iii), so x₁ = Ḣ/H² ≈ +164 ⟹ q_dec ≈ −165 — the spike point is INSIDE the W1-1-documented deep-acceleration excursion set (excursions to q_dec ≈ −514). The spike's secular footprint on the q-run is already measured: the +0.0556 tracking-lag excess (XC-1) and the ±0.2 generic-IC ringing envelope (XC-6) — total dynamical-correction budget |Δslope| ≲ 0.26, a factor ~4 short of the 1.056 needed to reach slope 1 by transmission corrections (scope per Re:V2: this bounds corrections-to-a-drive, not new terms). My regime-boundary expertise adds: a single marginal passage (ε_ad ≈ 0.9) excites transient ringing of relative amplitude O(ε_ad-suppressed but O(1)-weak) — consistent with the measured ±0.2 envelope — and ZERO secular parity violation: passage through a marginal-adiabaticity point is a g-even perturbation (it enters through |drive rate|², and Ḣ itself is g-even). The numbers cohere; no anomaly hides in the spike.

**(iii) The memory-kernel territory volovik declared open — now mapped (Q-T2 in full).** Construction in T1-C4 (T-eq.5). The structural findings:

1. **Kernel support**: the relic kernel's memory time is set by pair-beat dephasing across the 992-mode spectrum, τ_mem ~ 1/spread(2E_k) — gap-scale-SHORT relative to backbone timescales IF the unit conversion puts 2Δ_BCS ≫ backbone rates (H ≤ 0.31, ω = 59.9 backbone units). Short kernel ⟹ the Markovian reduction is CONTROLLED, and its secular outputs are exhausted by the even-graded set {δk_curv(a), δΓ (on-shell only above threshold), order-zero tilt}.
2. **Where T-breaking lives in the kernel**: ONLY in the causal θ(t−t′) — the relic state contributes its T-asymmetry through phases (φ_k), which are oscillatory; the frozen n_k and |σ_k| are g-even scalars. So the kernel's grading at secular order is even BY CONSTRUCTION (Berry-flatness, T-eq.2, is the geometric statement of the same fact).
3. **The unique escape**: resonance. If 2E_k(a(τ)) crosses ω_q on the tail, the oscillatory column rectifies into the secular column (parametric coupling), and C1/C2/C4 merge into a live odd-in-H drive with slope ≈ 1 (T-eq.4). One number decides: the position of ω_q = 59.888 (backbone units) within/outside the pair band [2 min E_k, 2 max E_k] in COMMON units. The bottom of the 992-mode response sits at E ≈ 0.82 M_KK (bottom-triple 0.8197/0.8359/0.8730, verdict file line 10), so 2Δ-scale ≈ 0.93–1.7 M_KK; the backbone-unit ↔ M_KK conversion is the one provenance item not in the documented set (the S99 k_curv construction carries it). NOT resolvable here without running scripts — hence sibling conjunct (C), pre-registered with Δ_res ≥ 0.1 clearance (rationale in Re:V4).
4. **Freeze-premise duration check**: both sides' arguments (volovik's closure-1 AND my C1–C5) consume frozen {n_k}; the S39-corrected t_therm ≈ 6 M_KK⁻¹ is finite, so the premise holds only if the tail duration ≪ t_therm in common units — the SAME conversion as item 3. Fold into conjunct (C) as a second assert.

**(iv) The pincer (new structural point, lands as clause (d5)).** The relic sector cannot escape through the thermalization door either: **frozen** ⟹ {n_k} constants ⟹ closure-1 + my T1 analysis (no secular odd term off-resonance); **thermalized** ⟹ local-equilibrium state functions EXIST ⟹ the H-parity THEOREM applies to it directly (it becomes clause (a)-(c) territory). The only escape is the transient crossover (partially thermalized, neither GGE nor Gibbs), which is bounded in duration by t_therm and produces no late-TAIL slope (a transient cannot set an asymptotic log-slope). So Reading B's "the equilibrium argument never sees the relic" is true but toothless: the relic is caught between a freeze that makes it H-blind at fixed (q, a) and a thermalization that hands it back to the parity theorem. This pincer is, to my eye, the single strongest NEW argument the workshop adds to the wall — it converts "the theorem is vacuous on the relic" from a concession into a two-door closure.

**(v) Substrate framing check (per `phononic-framing.md`).** Everything above is substrate-IS: the relic IS the fold-frozen occupation set of the D_K eigenmode spectrum (Parker production at the van Hove fold transit, Mach 13.75); the q-channel IS the substrate's slow vacuum coordinate; the "bath" is not a container environment but the substrate's own frozen spectral sector, coupled through the same ∂_q E_k response that defines k_curv. The arrow runs D_K eigenvalues → ω_n(q) response → (k_curv, kernel K) → q-channel EOM → vacuum-energy history. No candidate above imports container thinking: even C2's "geometric magnetism" is curvature of the substrate's own (q, ln a) deformation manifold — a Level-2 moduli-deformation substrate-IS object in the sense of `phononic-framing.md §Single-τ-slice vs moduli-deformation`.

#### T3: Questions for volovik

- **Q-V1 (the arena swap in clause d3):** Do you accept the (q, ln a) 2-parameter slow manifold as the structurally correct arena — chain B's N = 1 premise replaced, the gyroscopic closure resting on (Berry-flatness T-eq.2) + (squeeze-phase leakage ≤ 1.2%, dephased) + (C7 zero-counterflow for the Iordanskii class) — i.e., argument-grade with the resonance window as the single hostage? If yes, my clause (d3)/(d4)/(d5) draft (Re:V4) replaces your offered (d3)/(d4) and the scope line becomes "exhaustive for Markovian-reducible (off-resonant), analytic, frequency-modulated-bath dynamics" (the 1-dof clause demoted to corroborating algebra). If no, name the step of T-eq.1/T-eq.2 you reject.

- **Q-V2 (the one number — unit conversion for the resonance/threshold check):** From the S99 k_curv construction provenance (the 992-mode ω_n(q) machinery), state the conversion between backbone-τ rate units (where ω_q = √k_curv = 59.888) and M_KK units (where the pair band sits at 2E_k ≳ 2 × 0.82 ≈ 1.64), and therefore whether ω_q lies BELOW the pair threshold (⟹ δΓ = 0 exactly AND no resonance — C1/C2/C4 dead completely, clause (d) upgrades to "argument-grade, window closed"), INSIDE the band (⟹ sibling conjunct C is LIVE and must run before Stage-2 dispatch), or ABOVE it (⟹ no resonance; same upgrade as below-threshold). If the conversion is not recoverable from the S99 artifacts without compute, confirm conjunct (C) as the sibling's first assert and the Stage-1 clause (d4) carries "pending sibling" explicitly.

- **Q-V3 (citation discipline, retrieval layer):** Do you accept the Re:V3 middle strengthening — token retained + expansion rule as drafted + the retrieval-layer amendment (scoped one-liner in the Workshop Verdict row; V3.iii paragraph in the S100b closure reading; gate-entity note touch-up routed with your V5.6b flag) — as closing the one realistic mis-citation pathway (rule-blind knowledge-MCP FTS retrieval, demonstrated by this gate's own MCP audit consuming S99's bare verdict string)? This is acceptance of your two-register resolution WITH one added lodging requirement, not the deprecation alternative.

- **Q-V4 (the dP = 0 premise, minor sharpening to regime clause (a)):** GD-4 evaluates δμ at dP = 0 — itself an equilibrium balance condition. On the excursion set (x₁ ≈ 160–510) it shares the coefficients' quantitative unreliability, though parity is unaffected (P is built from even-graded potentials; the condition is g-even). Do you fold one sentence into regime clause (a): "the dP = 0 balance premise of GD-4 shares the same quantitative regime restriction as the leading-order coefficients"? Cost: one sentence; benefit: no future reviewer can claim an undisclosed premise.

- **Q-V5 (stratum number in the Stage-1 text):** Re:V2 derives the theorem-grade-quantitative stratum bound — fraction ∈ [0.169, 0.668] of the backbone grid (|x₁| < 1 ⟺ q_dec ∈ (−2, 0); lower bound exact from documented W1-1 masses) — at zero compute. Do you want this frozen into regime clause (a) alongside the spike number (my preference, same harder-to-mis-cite logic as (d2)), with the exact tail-restricted split delegated to the sibling's diagnostics?

---

## Round 2 — volovik: Follow-up (term-by-term classification/rebuttal)

### CONVERGENCE

**C-1 — The (q, ln a) arena: RULED IN as the legitimate 2-dof escape shape; B = 0 is the substrate-specific closure.** Reading B found exactly what my chain B's reopening clause (V1.iv) asked for — a second substrate collective coordinate, NAMED — and transit's construction is correct on every step I can check:

(i) **T-eq.1 is the legitimate escape shape.** The fixed-backbone design itself promotes ln a to an external slow parameter; my chain B counted dof on the q-channel alone, and the gate's own design (pinned `arr_H_bare_t`) injects the second velocity d ln a/dτ = H. The N = 1 premise was inapplicable to the arena the gate built; the 1×1-antisymmetry algebra stands, its scope shrinks (item iii below). T-eq.4 verified: F ∝ κ₁(q)·H with a-independent κ₁ gives q_eq^geo = κ₁H/k_curv ⟹ d ln q/d ln H = 1 IDENTICALLY — the unique force family that SITS at slope 1 rather than passing through it by coincidence. That is precisely why C2 had to be constructed and closed numerically rather than rhetorically; transit did both.

(ii) **T-eq.2 (B = 0 exact) verified independently, premise included.** The pullback chain: on the slice {Y ≡ 0, Z ≡ 1} of the generalized-oscillator parameter space, dY = 0 and dZ = 0 along every (q, ln a) direction, so all three terms of the curvature 2-form V_n ∝ [X dY∧dZ + Y dZ∧dX + Z dX∧dY]/(XZ−Y²)^{3/2} vanish term-by-term: X dY∧dZ = 0 (dY = 0), Y dZ∧dX = 0 (Y = 0), Z dX∧dY = 0 (dY = 0). Pullback ≡ 0 ⟹ B_{q,ln a} = 0 EXACT for the number sector. ✓ And the premise — frequency-only modulation — is verified SUBSTRATE-SIDE, which is where my domain bears: the (q, a)-dependence of the relic bath enters through ω_n(q) = √(λ_n² + q) (`s97_w2_2_c10_n_exponent.py` L19/L257 — the SAME machinery that built k_curv), which modulates X = E_k² alone; the xp + px squeeze-generator (the Y axis) is never sourced by the substrate response, exactly as transit's Step 2 states (BdG anomalous terms are (x² − p²)-class, X–Z axis). Y ≡ 0 identically on the (q, ln a) manifold is a property of the substrate's own spectral response, not a modeling choice. The leakage bookkeeping (φ_k = 0.005–0.012 rad, rotating at pair frequencies, 1/√59.8 ≈ 0.13 incoherent stacking) carries the right structure and the documented numbers.

(iii) **Two-class closure map (refinement for the (d3) final wording — not dissent).** The 1-dof antisymmetry algebra REMAINS the operative closure for the {odd-in-q̇, workless} class — forces built on the channel velocity alone, where a 1×1 antisymmetric G vanishes with no bath input needed. The bath-structure closure (Berry-flatness + φ_k bound + dephasing) is operative for the {odd-in-H, q̇-independent} GEOMETRIC class that the (q, ln a) arena opens. transit's "dof-counting demoted to corroborating algebra" is accepted with this precision: demoted for the geometric class, retained as operative for the q̇-odd class. Each class gets exactly one closure; neither argument is redundant. Folded into the final clause (d3) as a parenthetical (landing list iii).

(iv) **C7-first ordering in (d3): accepted without reservation.** T^{0i}_4D = 0 EXACT (atlas-04 C7) is the same substrate identity my own CDM-by-construction records rest on (S43/S44 lineage); an exact identity outranks a structural argument, and the Iordanskii class should die by it FIRST, then homogeneity, then the algebra. transit's Re:V1 "MISSED" paragraph is a genuine catch of an anchor I under-used: the substrate IS a zero-counterflow two-fluid state — the lab taxonomy's transverse column is switched off by the state, not the geometry.

**C-2 — The (d5) thermalization pincer: ACCEPTED, with a double-lock refinement.** The pincer is well-posed precisely BECAUSE of the S39 correction my V5.6b flagged (finite t_therm ≈ 6 M_KK⁻¹; "never thermalizes" retracted) — transit's Re:V5.6 confirms this from its side and I confirm it from mine. Refinement for the final (d5) text: the thermalized door is DOUBLE-locked. If the window outlasts t_therm, the relic acquires local-equilibrium state functions, and then (lock 1) its H-graded equilibrium response falls under clauses (a)–(c) — the parity THEOREM applies directly; (lock 2) its residual matter-sector tilt is an ordinary dilution object — exactly (d2)'s analysis, whose mimic window is EMPTY on this backbone (0.0000 exact). Both doors close on parity-consistent ground. Additionally (EMERGENCE A-V2 Step 7): the pincer BITES the below-band corner of transit's Q-V2 trichotomy through the shared clock normalization — the duration assert and the resonance assert are one two-parameter constraint, not two independent checks.

**C-3 — The fourth column (secular/oscillatory): ACCEPTED, with laboratory grounding.** The {potential, q̇-coupled, memory} × {SECULAR, OSCILLATORY} taxonomy is the correct restatement of V1's exhaustiveness verdict, and it is not ad hoc: it is the 0+1d image of a structure the laboratory two-fluid system exhibits verbatim. In 3He-B, two-fluid hydrodynamics (the secular column) is parity-protected exactly as V5.1 stated; the laboratory's known exception is pair-vibration spectroscopy — sound attenuation acquires sharp features where the probe frequency crosses the collective pair-vibration modes (the real/imaginary squashing modes at √(8/5)Δ and √(12/5)Δ): the oscillatory column rectifying into the secular (attenuation) column exactly at resonance, and nowhere else. [Source-fidelity note: the squashing-mode frequencies are standard 3He-B collective-mode physics in the corpus's review lineage (Paper 26-class), not a numbered equation in the pinned corpus files — engaging beyond the pinned set, flagged per charter.] The substrate's resonance hostage 2E_k ≈ ω_q is the same physics in the child system. The THREE-selector slope rule (transit Re:V5.2: equilibrium analyticity → even integers; amplitude self-consistency → 1; secularity suppresses everything else, failure window = parametric resonance, pre-registered) is endorsed as the durable constraint-map object, superseding my two-selector V5.5 form; transit's pre-filter addendum line ("check SECULARITY — if oscillatory and off-resonant, it is dead at the same desk") goes to the permanent record with it.

**C-4 — Q-T1 frozen into clause (d2): ACCEPTED; chain verified before freezing.** Step-by-step: p_local = 1/(1 + q_dec) ✓ (from q_dec = −1 − H′/H²); window 3p_local ∈ [0.95, 1.05] ⟺ q_dec ∈ [60/21 − 1, 60/19 − 1] = [1.857, 2.158] ✓; documented bound q_dec ≤ +0.81 at all 999 points from `miss_above_band = 0.000000` (W1-1 verdict line 12) + the map_0 identity theorem (A ≡ 1, B ≡ 0 ⟹ q_corrected ≡ q_bare) + XC-4 backbone identity (max|ΔH| = 0.0) ✓; 0.81 < 1.857 ⟹ window EMPTY, fraction 0.0000 EXACT; closest approach 3/1.81 = 1.657 ✓; the q_dec < −1 (3p < 0) and q_dec = −1 (no power law) sectors covered ✓. The number goes into the clause with its provenance — my stated V4 preference, now executed by transit's own computation. transit's (d2) draft text is accepted VERBATIM into the final Stage-0 text (landing list iii): a clause carrying `0.0000 exact (requires q_dec ∈ [1.857, 2.158]; documented max +0.81)` cannot be mis-cited into "the window was never checked."

**C-5 — Remaining clause-(d) deltas, citation nits, and Re:V2/Re:V3 items: ACCEPTED.** Specifically: **(d1)** the "order zero" qualifier — honest about where C1 lives; my closure-1 holds at adiabatic order zero exactly as transit scopes it, and the first-order response lag genuinely carries H (T-eq.3 is a correct construction; its oddness derivation — d/dt acting on g-even E_k(a) gives odd × even = odd — checks out, and its fate by dephasing is correctly assigned). **(d4)** the constructive scoping — the secular-output set {δk_curv(a) even-reactive; threshold-gated δΓ; order-zero tilt} replaces my open-ended "memory terms open" declaration and is STRONGER than what I drafted; one precision fix folded into the final text: δΓ requires ω_q to lie ON the pair band (threshold AND ceiling — band-top caveat per A-V2), not merely above threshold. **Citation nits (both)**: "fold-frozen" replaces "never-equilibrated" (my own V5.6b discipline applied to my own draft — accepted with zero resistance), and the bath-structure item replaces the bare 1-dof item in the relic-exclusion parenthesis. **Re:V2**: the stratum map verified (lower bound 0.1692 = 0.6677 − 0.4985, the (−0.97, 0) mass, a strict subset of the |x₁| < 1 stratum q_dec ∈ (−2, 0) — exact ✓; upper bound 0.6677 over-counts the excursions ✓); the "pleasant inversion" (the miss-set CONTAINS both the best quasi-static points and the worst excursions — W1-1's miss histogram IS W1-2's regime diagnostic at zero compute) is genuine cross-gate cartography; the |Δslope| ≲ 0.26 budget with its honest scope (bounds corrections-to-a-drive, not new terms) retires the "backbone non-adiabaticity rescues slope 1 by transmission" sub-family cleanly; the two-clocks separation (R_therm scopes the FOLD, ε_ad scopes the TAIL — T2.i) is exactly right and is the correct quarantine of my domain's freeze credentials from the q-run's adiabatic class. **Re:V3**: transit's concession that the token's quantifier range was NOT ambiguous at pre-registration (plan Definition 4 enumerated candidates + backbone) completes the two-register resolution — both registers now two-sided agreed. **Sibling**: EMIT condition met (C2 = constructed, not classified dead — exactly my V4.iii trigger); conjunct (B) downgrade scan→assert accepted (Q-T1 resolved it analytically); delta-to-CF-S101-W1-QEQ-SELFCONS = ZERO confirmed from both sides, the two probes logically independent (drive slot vs back-reaction — neither verdict pre-judges the other); the amplitude-law diagnostic endorsement with transit's WKB-grade reasoning (q_amp²ω ≈ adiabatic invariant ⟹ the |H|-law is a prediction on the self-consistent background) is the right physics at the right cost (one regression).

### DISSENT

Near-full convergence. Two items remain, both refinements backed by new evidence, neither touching any landed verdict or any clause text already agreed.

**D-1 — Re:V1 rider (1) overstates pointwise: "a dilution tilt transmits neither 1 nor (at the max-q_dec point) exactly 2."** The window-empty conclusion carries in full; but the rider's phrasing invites the mis-reading "no grid point transmits slope 2," which is false on documented values alone:

```
Claim: 3p_local sweeps THROUGH 2 on the decelerating grid mass; slope-2 dilution
       transmission IS pointwise realized on this backbone.

Step 1: 3p_local = 3/(1 + q_dec)                     [Re:V1 Steps 1-3, verified at C-4]
Step 2: decelerating mass = 1 - accelerating_frac = 1 - 0.6677 = 0.3323,
        all of it within q_dec in [0, +0.81]          [W1-1 verdict line 12:
                                                       miss_above_band = 0.000000]
Step 3: on q_dec in [0, 0.81]: 3p_local in [3/1.81, 3/1.00] = [1.657, 3.000]
Step 4: 2 in [1.657, 3.000], attained at q_dec = 1/2  [3/(1 + 1/2) = 2]
Conclusion: the dilution tilt transmits slope 2 pointwise wherever q_dec = 1/2; on
33.2% of the grid the transmitted slope sweeps a band CONTAINING 2. What is true and
load-bearing: the WINDOW [0.95, 1.05] is empty (0.0000 exact) and the closest
approach is 1.657. Chain C's "structurally 2" also survives as the
Friedmann-consistent-background statement.
```

Resolution: confined to the rider. transit's (d2) clause draft does NOT carry the phrasing and is accepted verbatim (C-4); the final turn simply must not propagate rider (1)'s "neither … exactly 2" wording into any registry or citation text.

**D-2 — The Δ_res ≥ 0.1 floor rationale is keyed to the wrong modulation depth.** transit's Re:V4 width estimate ("h ≲ O(φ_k·∂lnE/∂ln a) ≲ 0.01 ⟹ width ≲ 0.5% of ω_q ⟹ 10% clearance ≥ 20× the width") uses the φ_k-suppressed ODD-channel amplitude as the Mathieu depth. New evidence — the instability bandwidth is set by the FULL parametric depth:

```
Claim: the principal-resonance half-width at 2E_k = omega_q is set by the FULL
       parametric modulation depth h_par (the ringing q-component), NOT by the
       phi_k-suppressed odd amplitude; the ">= 20x clearance" rationale can
       overstate by up to ~an OOM.

Step 1: relic-mode EOM: x'' + omega_k^2(q(tau)) x = 0 with omega_k^2 = lambda_k^2 + q(tau),
        EXACTLY LINEAR in q                  [s97_w2_2_c10_n_exponent.py L19/L257]
        => Mathieu form with depth h_par = q_osc/(lambda_k^2 + q_bar), q_osc = the
        amplitude of the q-component oscillating at omega_q (the ringing), q_bar the
        slow (adiabatic) part.
Step 2: principal parametric resonance at omega_drive = 2*omega_0:
        relative half-width  delta-omega/omega_drive = h_par/4.
Step 3: phi_k enters the AMPLITUDE of the rectified odd force (the Berry-leakage
        factor) — NOT the instability bandwidth. The band is opened by the drive
        depth regardless of which force component is rectified through it.
Step 4 (bound): q_osc <= ringing_frac x q_eq,tail; q_eq,tail <= |q_boundary| = 0.672
        M_KK^2 (the kappa_2_diag construction: q_eq(H_max) = 7.19704 x 0.3056^2 = 0.672);
        lambda_min^2 = 0.672  =>  h_par <= ringing_frac x ~0.5.
        ringing_frac for the PRIMARY (driven-IC) run is NOT documented (XC-6's +-0.2
        slope systematic is the generic-IC case)
        => h_par in [~0.01, ~0.1] is unbounded by documented values alone:
        at h_par = 0.1 the half-width is 2.5% of omega_q and the flat 0.1 floor is
        only 4x clearance — not 20x.
Conclusion: pre-register the width-aware guard NOW (R2 is the negotiation window
transit itself pinned at Re:V4): conjunct (C) additionally REPORTS h_par measured from
the npz (tail ringing amplitude at omega_q divided by (lambda_min^2 + q_bar)), and the
resonance conjunct becomes  Delta_res >= max(0.1, 5*h_par/4)   — i.e. >= 5x the
half-width by construction at ANY h_par.
```

This is the single open spec-text item; it only ADDS a reported diagnostic plus a max() to the threshold, pre-compute (no Class-3 exposure). Fallback acceptable to me: if transit documents a pre-compute bound h_par ≤ 0.02 from the driven-IC run's ringing fraction (making the flat 0.1 floor ≥ 20× by itself), the flat floor stands and h_par stays report-only — Q-F3.

Everything else: full convergence — every other transit R1 item is accepted as stated or refined under C-1..C-5 / A-V1..A-V5.

### EMERGENCE

**A-V1 (Q-V1 answered): YES.** The (q, ln a) 2-parameter slow manifold is the structurally correct arena; chain B's N = 1 premise is replaced; the gyroscopic closure rests on (Berry-flatness T-eq.2, verified C-1.ii) + (squeeze-phase leakage ≤ 1.2%, pair-band dephased) + (C7 zero-counterflow for the Iordanskii class) — argument-grade with the resonance window as the single hostage. transit's (d3)/(d4)/(d5) draft REPLACES my offered (d3)/(d4), with the C-1.iii two-class parenthetical, the C-5 on-band δΓ fix, and the C-2 double-lock + coupling sentences folded in (full merged text: landing list iii). The scope line is accepted in transit's form with one retained clause — final form: *"exhaustive for Markovian-reducible (off-resonant), analytic, frequency-modulated-bath dynamics; the 1-dof antisymmetry algebra independently closes the q̇-odd workless class."* Substrate framing preserved: T-eq.1's geometric force is curvature of the substrate's OWN (q, ln a) deformation manifold — a Level-2 moduli-deformation substrate-IS object (transit T2.v framed this correctly); ruling it IN keeps the explanation arrow substrate-first.

**A-V2 (Q-V2 answered — load-bearing): the resonance window is SIBLING-DEFERRED — and the trichotomy is not three-cornered: the below-band corner is pincer-coupled.** Direct answer first: the backbone-unit ↔ M_KK conversion is NOT recoverable from the S99 artifacts without a new derivation, and I can now say WHY with provenance — which upgrades conjunct (C) from a unit-conversion lookup to a clock-normalization derivation. Full chain per `math-scripts.md`:

```
Claim (A-V2): (1) the backbone-tau <-> M_KK conversion is a single clock normalization
gamma := dt/dtau [M_KK^-1 per unit tau], DELIBERATELY set to unity at construction and
absent from the documented set; (2) every gate slope is EXACTLY gamma-invariant — the
FAIL cannot be touched by any clock choice; (3) the resonance comparison is the C10
lineage's FIRST gamma-DEPENDENT observable; (4) the below-band corner of the Q-V2
trichotomy collides with the freeze premise through the same gamma.

Step 1 (q carries M_KK^2 — eigenvalue-squared units):
        omega_n(q) = sqrt(lambda_n^2 + q)        [s97_w2_2_c10_n_exponent.py L19, L257 —
                                                  the SAME machinery that built k_curv]
        => [q] = [lambda_n^2] = M_KK^2.
        Exact cross-source anchor: q_boundary = -lam_sq_min [s97 L341-343] and the
        documented bottom-triple eigenvalue [verdict file line 10]:
        0.81974111^2 = 0.67197549 = |q_boundary|  — an 8-digit match across two
        independently pinned artifacts. Units CONFIRMED.
Step 2 (k_curv carries M_KK^-3 — cache units):
        k_curv = -d2E_ZP/dq2|_0 = +(1/8) Sum_n w_n/lambda_n^3 = 3586.5312
        [s97 L388-389];  [E_ZP] = M_KK, [q] = M_KK^2  =>  [k_curv] = M_KK^-3.
Step 3 (the ODE runs on a DECLARED arbitrary clock):
        the friction ODE q'' + 3Hq' + k_curv(q - q_eq) = 0 with ' = d/dtau requires
        [k_curv] = tau^-2; Steps 2-3 are reconciled only by an implicit kinetic
        normalization chi_I = 1 in MIXED (cache, tau) units. This is not my inference —
        the S97 construction DISCLOSES it at birth:
            t_relax = 1.0    # (local) sets units; cancels in slope     [s97 L361]
            x-axis label: "H (relaxation-era Hubble rate, arb. units)"  [s97 L722]
        => omega_q = sqrt(3586.5312) = 59.888 per unit tau (period 0.1049; ~2.5 periods
        per window) is a NORMALIZATION-DEPENDENT diagnostic frequency — in the same
        disclosed class as kappa_2_diag = |q_boundary|/H_max^2 = 7.19704 [WP §W1-2
        disclosure 1; consistency: sqrt(0.672/7.197) = 0.3056 = H_max, matching the
        documented 3H <= 0.92].
Step 4 (gamma-invariance of every landed verdict — direction/invariance claim):
        under constant re-clocking t = gamma*tau:  ln H_phys = ln H - ln gamma
        => d ln q / d ln H_phys = d ln q / d ln H   EXACTLY (constant shift kills no
        derivative). All three slopes (2.0556 GD / 1.008273 imposed / 3.4159 bare) are
        gamma-invariant — the TIME-AXIS instance of the multiplicative-normalization
        cancellation identity (math-scripts.md; XC-5's sibling on the clock axis
        instead of the coefficient axis). The S97 disclosure "cancels in slope" IS this
        identity, declared at construction. THE FAIL IS UNTOUCHABLE BY ANY CLOCK
        CHOICE — its permanence is structural here, not merely procedural.
Step 5 (the resonance is gamma-DEPENDENT):
        omega_q^phys = 59.888/gamma  vs  the pair band [2E_min(q), 2E_max] in M_KK.
        gamma appears NOWHERE in the documented set BECAUSE Step 4 meant no prior gate
        ever needed it. The resonance check is the first observable in this lineage
        that does not cancel it. (Band bottom, documented: 2*lambda_min = 1.63948
        M_KK — TIGHTER than the 2*Delta_BCS ~ 0.93 M_KK lower bound transit quoted;
        strengthens every off-resonance dephasing statement.)
Step 6 (corpus prior — why no OOM closure exists):
        KV oscillation dynamics places the q-oscillation at the UV scale [Paper 25 §V,
        Eqs. (5.5a-b): omega ~ E_Planck; substrate image: M_KK-scale]. The
        corpus-faithful expectation omega_q^phys = O(M_KK) sits at the SAME order as
        the pair band 2E_k >= 1.639 M_KK — inside or above by O(1) factors. The window
        genuinely cannot be closed by estimate; it needs the derived gamma
        (equivalently the q-channel inertia chi_I).
Step 7 (pincer coupling — the below-band corner collides with the freeze premise):
        below-band THROUGHOUT the tail requires omega_q^phys < 2E_min(q(tau)) at every
        tail point; binding at the tail END where q -> 0+ and 2E_min -> 2*lambda_min:
            gamma > 59.888/1.63948 = 36.53 M_KK^-1
        (weakest reading, q = 0.672 sustained: gamma > 59.888/(2*sqrt(1.344)) = 25.83).
        Window durations under that clock:
            Delta-t(tail,  Delta-tau = 0.13028) >= 4.76  (weak: 3.37)  M_KK^-1
            Delta-t(full,  Delta-tau = 0.26050) >= 9.52  (weak: 6.73)  M_KK^-1
                                       [full-window figures under the constant-gamma /
                                        window-wide reading; tail-only is the rigorous floor]
        vs t_therm ~ 6 M_KK^-1 [S39-corrected; OOM-grade]:
            full-window ratio 1.12-1.59 (freeze premise BROKEN);
            tail-only ratio 0.56-0.79 (strained, not broken).
Conclusion: BELOW-band forces the gate window to outlast (full-window reading) or
        approach (tail-only floor) t_therm => the (d5) pincer routes the relic toward
        the THERMALIZED branch, where the parity THEOREM applies directly (and the
        residual dilution tilt is (d2)'s window-empty object — the double lock, C-2).
        The below-band corner cannot deliver a frozen relic on this backbone. The
        self-consistent end-states are TWO, not three:
          {ABOVE-band & frozen}:  no resonance, no on-shell delta-Gamma —
                                  clause (d) upgrades to "argument-grade, window closed";
          {IN-band}:              resonance LIVE — C2 becomes the workshop's biggest result.
        RULING: SIBLING-DEFERRED. Conjunct (C) confirmed as the sibling's first assert;
        clause (d4) carries "pending sibling" explicitly; conjunct (C) upgraded from
        unit-conversion lookup to CLOCK-NORMALIZATION DERIVATION (gamma or chi_I from
        substrate inputs) + the COUPLED resonance/duration assert.
```

Two refinements the chain forces on the sibling spec (folded into landing list iv): **(R1) band-top caveat** — the 992-mode working set bounds the band BOTTOM faithfully (bottom-triple documented) but its TOP is truncation-dependent; the above-band verdict must quote E_max from the full L_max=12 cache, not the working set. **(R2) occupied-band refinement** — the rectification needs σ_k ≠ 0 at the resonant k, so the band that matters is the OCCUPATION-WEIGHTED support of the relic set {n_k, σ_k} (readable from the s97 npz keys `w_n`/`n_k_gge`), not the bare spectral range; conjunct (C) reports both.

One framing sentence for the permanent record: the workshop's object-split now has a clean invariance classification — **log-derivative slope observables are clock-blind** (time-axis multiplicative cancellation; XC-5's sibling), while **the resonance position is the unique clock-keyed observable in the C10 lineage**. The FAIL verdict lives entirely in the clock-blind class, which is WHY it is permanent under any future normalization derivation: the sibling can land any γ whatsoever without touching W1-2.

**A-V3 (Q-V3 answered): YES — the middle strengthening is accepted in full.** My V3 question pre-committed me ("prepared to accept the stronger form if transit shows one realistic mis-citation pathway the expansion rule fails to block"); transit showed one, and better than realistic — DEMONSTRATED in this wave's own audit trail (the W1-2 MCP pre-compute audit retrieved RELAXATION-CLOSURE as a bare verdict string; a rule-blind FTS consumer at S10x plan-freeze would surface `no_slope1_capable_substrate_drive` stripped of scope and pre-close the KV carve-out — the Class-(c) PIN-DRIFT-FROM-STALE-SOURCE mechanism, `regulator-pin-discipline.md`). Token retained (verdict permanence + in-register validity); expansion rule as drafted; PLUS the retrieval-layer lodging: (a) the scoped one-liner in the Workshop Verdict row (extractor-indexed); (b) the final citation paragraph verbatim in the S100b w1 closure reading; (c) the gate-entity note touch-up routed WITH my V5.6b R_therm flag to the orchestrator hygiene pass. Final text: landing list (ii).

**A-V4 (Q-V4 answered): YES — fold the sentence in.** Verified before accepting (new parity claim ⟹ chain):

```
Claim: dP = 0 is g-EVEN as a constraint surface; the premise-sharpening costs parity nothing.
Step 1: dP = s dT + n_q dmu + R dK              [Paper 11 Eq. (8) family; workshop V2.ii]
Step 2: g(s dT) = g(s)g(dT) = (-1)(-1) = +1;  g(n_q dmu) = +1 (q-sector differentials
        even);  g(R dK) = (+1)(+1) = +1 (R = 12H^2 even; K H-independent).
Step 3: every term g-even => the surface dP = 0 is a g-even condition; imposing it
        cannot inject odd structure.
Conclusion: the dP = 0 premise shares the COEFFICIENT regime restriction (quantitative,
on the excursion set x_1 ~ 160-510) and carries none of the parity load.
```

Sentence adopted into the regime annex (landing list iii): *"the dP = 0 balance premise of GD-4 shares the same quantitative regime restriction as the leading-order coefficients (parity unaffected: dP = 0 is g-even)."*

**A-V5 (Q-V5 answered): YES — freeze the stratum bound with provenance and a grid-vs-tail scope tag.** Verified: lower bound 0.1692 = 0.6677 − 0.4985 (the (−0.97, 0) mass — a strict subset of the |x₁| < 1 stratum q_dec ∈ (−2, 0)) is exact from documented W1-1 masses ✓; upper bound 0.6677 over-counts the excursions ✓. Adopted into the regime annex as a GRID-mass statement ("of the 999-point backbone") with the tail-restricted split delegated to the sibling diagnostics — the same harder-to-mis-cite logic as (d2), applied twice as transit proposed.

---

**FINAL-TURN LANDING LIST** — exactly what transit's R2-B must land:

**(i) Workshop Verdict cells (topics 1–4)** — proposed entries:

- **Row 1 (a) Partition exhaustiveness — Status: Emerged.** Key insight: "Partition upgraded to {potential, q̇-coupled, memory} × {SECULAR, OSCILLATORY}; equilibrium = theorem-grade analytic-even (all orders); relic closed at argument-grade by FOUR arguments (order-zero frozen tilt; dilution window EMPTY 0.0000 exact, clearance 1.657; Berry-flat bath structure + C7 zero-counterflow; secularity/dephasing); the legitimate 2-dof escape shape (q, ln a) found and closed (B = 0 exact, number sector); ONE numerical hostage: parametric resonance 2E_k ≈ ω_q → sibling conjunct (C). Scope: equilibrium theorem-grade; relic argument-grade pending CF-S101-W1-QEQ-RELIC-ODDFLOOR; KV carve-out CF-S101-W1-QEQ-SELFCONS."
- **Row 2 (b) dS imports — Status: Converged.** Key insight: "Parity exact to all orders of the graded gradient expansion, (K,R) pair included; coefficients regime-limited (spike x₁ ≈ 1.6×10²; theorem-grade-quantitative stratum grid-mass ∈ [0.169, 0.668]; dP = 0 premise shares the restriction); the verdict consumed only the exponent (κ₂-invariance 7.6e-8) — FAIL untouched. Corrected parity claim = V2.v as amended by A-V4 + A-V5."
- **Row 3 (c) Citation form — Status: Converged.** Key insight: "Two-register resolution + retrieval-layer lodging (middle strengthening): token correct in-register and PERMANENT; scoped sentence (landing list ii) mandatory downstream; the scope one-liner lodged where FTS retrieval lands (this row; S100b closure reading; gate-entity note via the orchestrator hygiene pass). Quantifier range unambiguous at pre-registration (transit concession, Re:V3)."
- **Row 4 (d) Routing — Status: Converged.** Key insight: "Stage-0 candidate FINAL text frozen (landing list iii); sibling gate EMITTED (landing list iv — conjunct C = clock-normalization derivation + coupled resonance/duration assert); CF-S101-W1-QEQ-SELFCONS delta ZERO + two non-gating annotations (landing list v)."

**(ii) Final scoped-claim citation text** (two-register resolution, FINAL form — supersedes V3.iii; the S100b w1 closure reading inherits this verbatim):

> **Canonical downstream citation for S100a-W1-2-QEQ-DRIVE (FAIL, audit e31d45cf5309b32cde67804d0576467592196b45ea908ec1edfac7f522212ca4):** On a fixed backbone, no substrate-internal EQUILIBRIUM-THERMODYNAMIC drive q_eq(H) can carry odd-in-H structure: every equilibrium Gibbs-Duhem potential shift is analytic-even in H (H-parity theorem, scoped form per the S100a W-1 workshop; leading power H², transmitted slope 2.0556 measured, κ-invariant at 7.6e-8). The slope-1 leg of the n = 2 tracking law is therefore an imposed-closure INPUT on any fixed backbone. Scope: equilibrium sector — theorem-grade; fold-frozen GGE relic sector — excluded at argument-grade (order-zero frozen occupations + dilution-mimic window EMPTY [0.0000 exact: requires q_dec ∈ [1.857, 2.158], documented backbone max +0.81, closest approach 3p_local = 1.657] + bath-structure gyroscopic closure [Berry-flat frequency-only modulation, B = 0 exact for the number sector; squeeze-phase leakage ≤ 1.2%, pair-band dephased; C7 zero-counterflow T^{0i}_4D = 0 exact] — pending the sibling resonance check CF-S101-W1-QEQ-RELIC-ODDFLOOR); non-Markovian memory terms — SCOPED: secular outputs exhausted off-resonance by {δk_curv even-reactive; on-band-gated δΓ; order-zero tilt}, with parametric rectification at 2E_k ≈ ω_q the unique surviving odd channel (sibling conjunct C). The surviving slope-1 route is Klinkhamer-Volovik oscillation-energy self-consistency (back-reaction, not a drive; q_amp ∝ |H|, parity-CONSISTENT non-analytic-even form; Paper 25 §V Eqs. (5.5a-b)), pre-registered as CF-S101-W1-QEQ-SELFCONS.
>
> **Expansion rule:** any downstream citation of the token `no_slope1_capable_substrate_drive` MUST expand it with the three scope qualifiers — (drive-type: potential-slot q_eq(H)), (fixed-backbone), (equilibrium = theorem-grade / relic = argument-grade pending sibling) — plus the carve-out pointer. **Retrieval-layer lodging:** the one-line scope pointer ("scope: equilibrium sector theorem-grade; relic argument-grade pending CF-S101-W1-QEQ-RELIC-ODDFLOOR; KV carve-out CF-S101-W1-QEQ-SELFCONS") lives in the Workshop Verdict row, the S100b w1 closure reading, and the gate-entity note (orchestrator hygiene pass, routed with the V5.6b R_therm touch-up).

**(iii) Stage-0 joint-theorem candidate — FINAL TEXT** (paste-ready; Stage-1 registration at S101 with `STAGE-1-CANDIDATE` tag; joint clauses (e), (f) flagged for Stage-2 PASS-AND; Stage-0 authors volovik + transit ONLY; Stage-2 reviewer pools preserved per V4.i: Axis-A ∈ {lizzi-spectral-functional-theorist, connes-ncg-theorist}, Axis-B ∈ {gen-physicist, kitaev-quantum-chaos-theorist}):

> **THEOREM CANDIDATE — H-PARITY-DRIVE-EXCLUSION (fixed-backbone q-channel)**
>
> - **Clause (a) [volovik-side]:** The Gibbs-Duhem derivation chain GD-1..GD-5 (assumptions enumerated per workshop V1.ii) yields the parameter-free substrate drive q_eq(H) = κ₂H², κ₂ = 3/(8πG·n_q·k_curv); the exponent is locked by the s ∝ T Gibbs-Duhem integration + the quadratic well; the coefficient is regime-limited per the Regime annex and verdict-irrelevant (XC-5, 7.6e-8).
> - **Clause (b) [volovik-side]:** All-orders H-parity grading — equilibrium T and s are t→−t-odd (anchor: Paper 11 §VI, contracting dS with T < 0, S = −A/4G); all dimensionless gradient ratios Ḣ/H², Ḧ/H³, … are even; every equilibrium Gibbs-Duhem potential shift, including the (K,R)-pair extension (Paper 11 Eq. (8), R = 12H² even), is even-graded and analytic in H², to all orders in the gradient expansion. No analytic odd-in-H equilibrium potential term exists at any order.
> - **Clause (c) [volovik-side]:** Slope-selection corollary — THREE selectors: equilibrium analyticity confines late-tail log-slopes to even integers (generically 2); amplitude self-consistency selects 1 via the unique non-analytic-even form |H| = √(H²); SECULARITY (phase-averaging over the gapped pair band, 2E_k ≥ 2λ_min = 1.639 M_KK, with ~1/√59.8 incoherent stacking) suppresses every other relic-sourced channel off-resonance, with parametric resonance 2E_k ≈ ω_q its pre-registered failure window. Numerical instantiation: 2.0556 (GD drive, even-locked + tracking lag) / 1.008273 (imposed |H|-form closure, = S99 at 4.6e-8) / 3.4159 (bare).
> - **Regime annex (to clauses a–b):** (α) Parity is exact order-by-order; the leading-order COEFFICIENTS are quantitatively reliable only where |Ḣ|/H² ≪ 1: on the gate's backbone this is violated at the Ḣ-spike (|Ḣ|/H² ≈ 1.6×10² at the ε_ad = 0.897 point) and marginal (O(1)) on the in-band decelerating stratum. Theorem-grade-QUANTITATIVE stratum (|Ḣ|/H² < 1 ⟺ q_dec ∈ (−2, 0)): grid-mass fraction ∈ [0.169, 0.668] of the 999-point backbone (lower bound exact from S100a-W1-1 documented masses, 0.6677 − 0.4985, verdict line 12 + XC-4 backbone identity; upper bound over-counts the deep-acceleration excursions; tail-restricted split = sibling diagnostic). The dP = 0 balance premise of GD-4 shares the same quantitative regime restriction as the leading-order coefficients (parity unaffected: dP = 0 is g-even). All of this limits κ₂-precision only, never the FAIL (XC-5 coefficient-invariance, 7.6e-8); any future κ₂-precision extraction must excise the spike region or resum the gradient corrections. (β) The theorem is VACUOUS — not violated — on sectors possessing no local-equilibrium state functions: the fold-frozen GGE relic (diabatic transit-freeze, R_therm = 5251.82, S95-certified, verdict-file line 82; finite t_therm ≈ 6 M_KK⁻¹ per the S39 correction), closed separately at argument-grade by clause (d). (γ) Non-analytic even forms |H| = √(H²) (amplitude variables — the KV self-consistency route, Paper 25 §V Eqs. (5.5a-b)) are OUTSIDE the theorem's domain: routed to CF-S101-W1-QEQ-SELFCONS (clause f).
> - **Clause (d) [transit-side]: Non-equilibrium-sector exclusion boundary.** (d1) At adiabatic order ZERO the fold-frozen relic tilt F_GGE = −Σ_k n_k ∂_q E_k(q, a) is functionally H-independent at fixed (q, a) [frozen occupations; diabatic transit-freeze R_therm = 5251.82, S95-certified, verdict-file line 82; the order-zero qualifier is load-bearing — the first-order response LAG does carry H, see (d4)]. (d2) Dilution-trajectory transmission: a relic dilution tilt transmits late-tail slope 3·p_local·(1+w)|_{w=0} = 3p_local with p_local = 1/(1+q_dec); the slope-1 mimic window 3p_local ∈ [0.95, 1.05] requires q_dec ∈ [1.857, 2.158] (stiff-fluid-class deceleration), while the documented backbone maximum is q_dec ≤ +0.81 at all 999 points (S100a-W1-1 miss_above_band = 0.000000; backbone identity XC-4) — **window fraction = 0.0000 EXACT**, closest approach 3p_local = 1.657; the dilution-mimic route is dead on this backbone. (d3) Gyroscopic/geometric route: the fixed-backbone design promotes the dilution coordinate ln a to a second slow parameter — the gyroscopic class on the (q, ln a) pair is NOT emptied by dof-counting (the 1-dof antisymmetry algebra remains the operative closure for forces odd in q̇ alone; the geometric q̇-independent class is the one needing bath structure); it is closed by bath structure: (i) Berry-flatness — the relic bath is frequency-modulated only (Y = 0 squeeze-axis slice; ω_n(q) = √(λ_n² + q) modulates X = E_k² alone), where the generalized-oscillator Berry curvature pulls back to zero EXACTLY; (ii) squeeze-phase leakage is bounded at O(φ_k) ≈ 0.005–0.012 rad [S95 W6-6 / S76 W1-C lineage] and rotates at pair frequencies ≥ 2λ_min (dephased off-resonance; 59.8-pair incoherent stacking adds ~1/√N ≈ 0.13); (iii) the Magnus/Iordanskii class vanishes independently by zero counterflow, T^{0i}_4D = 0 EXACT [atlas-04 C7], and by homogeneity (no scattering kinematics in the k = 0 channel). (d4) Memory slot (SCOPED, not open-ended): the relic kernel's Markovian reduction is controlled off-resonance and even-graded at SECULAR order (constructive decomposition, workshop T1-C4/T2; Berry-flatness T-eq.2 is the geometric statement of the same fact); its secular outputs are exhausted by {δk_curv(a) even-reactive; δΓ on-shell friction (present only if ω_q lies ON the pair band — threshold AND ceiling, same clock check as the resonance); the order-zero adiabatic tilt of (d1)}; the unique surviving odd channel is parametric rectification at 2E_k ≈ ω_q — bounded by sibling conjunct (C), PENDING SIBLING (CF-S101-W1-QEQ-RELIC-ODDFLOOR); absent a tail crossing, the relic sector admits NO secular odd-in-H potential term. (d5) Pincer closure on the freeze premise: if the gate window instead OUTLASTS t_therm ≈ 6 M_KK⁻¹ (S39-corrected finite thermalization), the relic sector acquires local-equilibrium state functions and the closure DOUBLE-locks — its H-graded equilibrium response falls under clauses (a)–(c) directly (the parity THEOREM), and its residual matter-sector tilt is (d2)'s dilution object (window empty); frozen ⟹ (d1)–(d4); thermalized ⟹ double-locked; only the transient crossover window escapes both, bounded by t_therm. The duration and resonance asserts are COUPLED through the single clock normalization γ = dt/dτ (workshop A-V2 Step 7): holding ω_q below the pair band throughout the tail forces Δt(window) ≳ t_therm (4.8–9.5 M_KK⁻¹ vs ≈ 6), pressing the below-band corner into the thermalized door — sibling conjunct (C) quantifies.
> - **Clause (e) [JOINT — scope statement]:** the wall reads "no slope-1-capable substrate-internal DRIVE on a fixed backbone," where: equilibrium stratum = theorem-grade (clauses a–c + Regime annex); fold-frozen GGE relic sector = argument-grade (clause d: four closure arguments; single numerical hostage = the parametric-resonance window, pending CF-S101-W1-QEQ-RELIC-ODDFLOOR); back-reaction = outside the quantifier range (not covered, not violated). Force-taxonomy register: {potential, q̇-coupled, memory} × {SECULAR, OSCILLATORY}; the exhaustiveness claim is scoped "exhaustive for Markovian-reducible (off-resonant), analytic, frequency-modulated-bath dynamics; the 1-dof antisymmetry algebra independently closes the q̇-odd workless class." Downstream citation per the expansion rule + retrieval-layer lodging (landing list ii).
> - **Clause (f) [JOINT — self-consistency carve-out]:** the Klinkhamer-Volovik oscillation-energy amplitude route (Paper 25 §V Eqs. (5.5a-b); two-component exchange-dynamics blueprint, Paper 35 §V) is the unique surviving slope-1 mechanism; it is parity-CONSISTENT (|H| is even — it occupies the non-analytic-even cell the theorem leaves open, completing the clause-(c) slope-selection rule rather than evading it); pre-registered as CF-S101-W1-QEQ-SELFCONS, spec delta ZERO; a PASS must realize slope 1 specifically through the amplitude law q_amp ∝ |H| (both-sides-endorsed non-gating diagnostic).

**(iv) Sibling gate 4-field spec — FINAL** (EMIT; SIBLING to CF-S101-W1-QEQ-SELFCONS, NOT a replacement; ID proposed `CF-S101-W1-QEQ-RELIC-ODDFLOOR`, Q-F2):

1. **What**: graded decomposition of the GGE-relic-induced effective force on the q-channel: **(A)** odd-coefficient floor on the t→−t-graded Markovian reduction of the relic kernel (diagonal + anomalous sectors; T-eq.5); **(B)** verification-assert of the analytic dilution-window result — assert max(q_dec) < 1.857 on the tail; report the realized min/max of 3p_local; **(C)** clock-normalization + coupled resonance/duration: derive the backbone clock normalization γ = dt/dτ (equivalently the q-channel inertia χ_I) from substrate inputs — the S97/S99 k_curv construction provenance, whose `t_relax = 1.0` (s97 L361, "sets units; cancels in slope") is the disclosed freedom to fix; convert ω_q = 59.888 τ⁻¹ and the pair band to the common clock; report Δ_res = min_k |2E_k − ω_q^{phys}|/ω_q^{phys} over the OCCUPATION-WEIGHTED support of {n_k, σ_k} (s97 npz keys `w_n`/`n_k_gge`) AND the band edges from both the 992-mode working set and the full L_max=12 cache (band-top caveat, A-V2 R1); report any tail crossing 2E_k(q(τ)) = ω_q^{phys}; report the measured parametric depth h_par = q_osc/(λ_min² + q̄) (tail ringing amplitude at ω_q); report Δt(window) vs t_therm ≈ 6 M_KK⁻¹ (the (d5) pincer assert; below-band + frozen is the self-inconsistent corner per A-V2 Step 7).
2. **Inputs**: `computations/session-100a/s100a_w1_qeq_drive.npz` (audit e31d45cf5309b32c); `computations/session-99/s99_w1_q_nonratio_observable.npz` (backbone; p_local); `computations/session-99/s99_w2_relaxation_closure.npz` (K_CURV, q_boundary); `computations/session-97/s97_w2_2_c10_n_exponent.npz` (ω_n(q), `w_n`, `n_k_gge` — the clock-normalization provenance); GGE occupation artifacts (S38/S95 lineage); the T-eq.5 kernel construction (workshop T1-C4).
3. **Gate**: PASS iff |c_odd|/|c_even| ≤ 10⁻³ AND assert (B) holds AND [Δ_res ≥ max(0.1, 5·h_par/4) with no tail crossing] AND the frozen-branch premise is duration-consistent (Δt(window) < t_therm, OR the thermalized hand-off documented per (d5) double-lock). INFO iff the only miss is Δ_res below the guard with no tail crossing (near-resonant — documented, clause (d4) carries it) OR Δt(window) ∈ [0.5, 1.5]·t_therm (crossover window — documented, clause (d5) carries it). FAIL iff a tail crossing exists OR the odd-floor is violated. FAIL routing: relic clause (d) demoted argument-grade → coincidence-bounded; Stage-1 entry text amended BEFORE any Stage-2 dispatch.
4. **Effort**: ~1 wave (the γ/χ_I derivation is the one new element; band comparison, h_par measurement, and asserts are post-processing on existing caches).

[Threshold-negotiation status: pre-compute, R2-legal per transit's own Re:V4 pin. The max(0.1, 5·h_par/4) guard is my D-2 proposal — the single open spec item (Q-F3); everything else in this spec is two-sided agreed.]

**(v) Delta to CF-S101-W1-QEQ-SELFCONS: ZERO** — the 4-field spec (what / inputs / gate `|slope_selfcons − 1| ≤ 0.05`, domfrac ≥ 0.95 / effort ~1 wave; WP "Carry-Forward Computations" block) is untouched; confirmed independently from the volovik side (V4.ii) and the transit side (Re:V4). Two NON-GATING annotations ride along for the S101 planner: (1) consumers inherit the citation-scope clause (landing list ii); (2) the amplitude-law diagnostic — regress ln q_amp vs ln |H| directly; a PASS must realize slope 1 specifically through q_amp ∝ |H| (the non-analytic-even form, clause-(c) three-selector prediction); a PASS realized any other way is a NEW anomaly worth its own gate. The sibling (iv) and the CF are logically independent probes of disjoint quantifier ranges (drive slot on a fixed backbone vs back-reaction); both run; neither pre-judges the other.

**(vi) Downstream-consumer citation texts:**

1. **S100b w1 closure reading**: inherits landing-list (ii) verbatim. No additional text.
2. **S100b X-wave C10 n_eff triangle** (S100b-X-C10-RHOVAC-EPOCH-PROFILE, trigger-first on this gate; S100b-X-C10-BBN-CONSTRAINT-RECONCILE): the ~4.11 member carries the mandatory tag — *"n ≈ 4.11 = 2 × 2.0556 is the FIXED-BACKBONE equilibrium-GD drive law AS-MEASURED (corridor-map value; contains the +0.0556 tracking lag, XC-1). Structural comparisons at the 0.1 level use 2 × 2 = 4 (the locked exponent product); as-measured comparisons use 4.11 — state which is carried. NOT the framework's physical n_eff prediction; the physical route is the self-consistency channel (n = 2 if CF-S101-W1-QEQ-SELFCONS lands PASS)."* [V3.iv.2 merged with transit's Re:V5 structural-vs-as-measured clarification.] Triangle-coherence adjudication {2.3, <2, ~4.11} remains OWNED by the S100b schedule; this workshop pins only the tag and the scope clause the members cite.
3. **Capstone §8.5** (ROUTED to the capstone designated writer; capstone-hygiene Q3/Q4 apply): status unchanged — OPEN by design — with the conditionality locus: *"the q ∝ H closure implicitly assumes the amplitude (square-root-of-energy) mechanism without deriving it; equilibrium thermodynamics cannot supply it (H-parity, S100a-W1-2); derivation attempt = CF-S101-W1-QEQ-SELFCONS; relic-sector exclusion boundary = CF-S101-W1-QEQ-RELIC-ODDFLOOR (pending)."*
4. **Gate-entity note** (knowledge MCP; ROUTED with the V5.6b R_therm touch-up to the orchestrator hygiene pass): the one-line scope pointer exactly as in (ii)'s retrieval-layer lodging.

### QUESTIONS

Only genuine wording choices remain for the final turn; all physics is converged (C-1..C-5, A-V1..A-V5) modulo D-2's guard form.

- **Q-F1 (clause (e) scope-line layout):** the landing-list (iii) clause (e) carries the scope statement and the force-taxonomy register as two sentences in one clause. Acceptable as drafted, or do you want the taxonomy register split into its own labeled sub-line (e.2) for citability? Either is correct; you hold the paste.
- **Q-F2 (sibling gate ID):** `CF-S101-W1-QEQ-RELIC-ODDFLOOR` proposed. Accept or rename — whichever ID lands, land it IDENTICALLY in all three carriers: the Workshop Verdict row 1/4 cells, the Wrap-Up Carry-Forward block, and the (ii) retrieval-layer lodging line (the FTS pathway you exhibited is exactly why the three must not drift).
- **Q-F3 (Δ_res guard form — resolves D-2):** accept `Δ_res ≥ max(0.1, 5·h_par/4)` as drafted in landing-list (iv), OR document a pre-compute bound h_par ≤ 0.02 from the driven-IC run's ringing fraction — at that bound the flat 0.1 floor is ≥ 20× the half-width by itself and h_par drops to report-only. Either resolution is pre-compute-legal under your own Re:V4 negotiation pin; the spec text above carries the max() form pending your call.

---

## Round 2 — transit: Cross-Synthesis (FINAL TURN)

### CONVERGENCE

**Full convergence. The landing list is adopted item-by-item — (i) verdict cells (rows 1–3 verbatim, row 4 updated with the Q-F resolutions), (ii) canonical citation text (frozen at Effected block E1), (iii) Stage-0 candidate (frozen at E2 with the Q-F1 split), (iv) sibling spec (Carry-Forward block, Q-F3 guard adopted + three report-only refinements), (v) delta statement (E4), (vi) consumer texts (E3). Every adoption containing a physics claim got its own verification before adoption.**

**C-T1 — A-V2 verified step-by-step, then adopted (the load-bearing new derivation of volovik's R2).** Before adopting the SIBLING-DEFERRED ruling I checked the chain in my own domain:

- *Step 1 (units)*: [q] = M_KK² via ω_n(q) = √(λ_n² + q); the cross-anchor reproduces by direct multiplication: 0.81974111² = 0.67197549 = |q_boundary| — an 8-digit match between the documented bottom-triple (verdict file line 10) and the s97 q_boundary, two independently pinned artifacts. ✓
- *Step 4 (γ-invariance)*: under t = γτ with CONSTANT γ, ln H_phys = ln H − ln γ ⟹ d ln q/d ln H_phys = d ln q/d ln H exactly — the constant shift kills no derivative. All three landed slopes (2.0556 / 1.008273 / 3.4159) are γ-invariant; the S97 disclosure `t_relax = 1.0 # sets units; cancels in slope` declared this identity at construction. ✓ One precision I add for the record (folded into the sibling as a report line, DISSENT-refinement 2): the theorem as stated is exact for CONSTANT γ; the DERIVED clock will inherit weak q-dependence through χ_I(q) (the kernel-reactive inertia depends on E_n(q) = √(λ_n² + q)), so the physical-clock slope acquires a bounded correction ∝ d ln γ/d ln H wherever χ_I varies. On the late tail q → 0⁺, E_n → λ_n ⟹ χ_I → const: the late-tail slope is asymptotically γ-invariant under the derived clock too. The FAIL's structural permanence survives with this asymptotic qualifier — and the pre-registered observable was in any case the τ-clock slope, which no clock touches.
- *Step 5 (arithmetic + band bottom)*: 59.888/1.63948 = 36.53; 36.53 × 0.13028 = 4.76; 36.53 × 0.26050 = 9.52; weak reading 59.888/(2√1.344) = 25.83 → 3.37/6.73 M_KK⁻¹. All reproduce. ✓ The band-bottom tightening — 2λ_min = 1.63948 M_KK replacing my 2Δ_BCS ≈ 0.93 M_KK quote — is accepted with thanks: it raises the slowest pair phase 1.76× and strengthens every off-resonance dephasing statement in clause (d).
- *Step 7 (pincer coupling)*: verified by substitution — below-band throughout the tail ⟹ γ ≥ 36.53 M_KK⁻¹ (binding at tail end where 2E_min → 2λ_min) ⟹ Δt ≥ 4.76 (tail floor) / 9.52 (full window) M_KK⁻¹ vs t_therm ≈ 6 M_KK⁻¹ ⟹ the freeze premise is broken on the full-window reading (ratio 1.12–1.59) and strained on the tail floor (0.56–0.79); the (d5) pincer routes the corner to the thermalized DOUBLE-locked door. The two self-consistent end-states {ABOVE-band & frozen} / {IN-band: live} stand; my Q-V2 trichotomy is retired. ✓

**ADOPTED**: SIBLING-DEFERRED ruling; conjunct (C) upgraded from unit-conversion lookup to clock-normalization derivation + COUPLED resonance/duration assert; clause (d4) carries "pending sibling" explicitly; refinements R1 (band-top from the full L_max=12 cache) and R2 (occupation-weighted support via `w_n`/`n_k_gge`) into the spec as drafted.

**C-T2 — Q-F1 resolved: SPLIT — clause (e) carries labeled sub-lines (e.1)/(e.2), ONE Stage-2 PASS-AND unit.** Reason (consumer-class separation — the same harder-to-mis-cite logic, applied a third time): (e.1) the scope statement is what every consumer of the FAIL cites (S100b w1 closure, X-C10 gates, capstone §8.5 locus); (e.2) the force-taxonomy register + scoped exhaustiveness line is what the standing pre-filter cites when triaging future drive proposals (the three-line desk check of V5.5/Re:V5.2). Distinct consumer classes get distinct citable anchors; the Stage-2 audit unit is unchanged — clause (e) = (e.1) ∧ (e.2) is audited as ONE joint clause by both reviewers, PASS-AND across axes per `joint-theorem-promotion.md`. Executed in the E2 frozen text.

**C-T3 — Q-F2 resolved: `CF-S101-W1-QEQ-RELIC-ODDFLOOR` CONFIRMED.** Landed identically in all three carriers: the Workshop Verdict rows 1 and 4; the Wrap-Up Carry-Forward block; the retrieval-layer lodging line inside the canonical citation paragraph (E1). Grep-checkable — the ID string appears with zero variants; the FTS pathway I exhibited at Re:V3 is exactly why the three must not drift.

**C-T4 — Q-F3 resolved: volovik's width-aware guard ADOPTED — `Δ_res ≥ max(0.1, 5·h_par/4)` — because D-2 is right on the physics and the fallback bound is not documentable.** Parametric resonance is my own domain, so the concession comes with its derivation rather than by deference:

- *(i) D-2's Mathieu identification verified.* The relic-mode equation x″ + [λ_k² + q̄ + q_osc cos(ω_q τ)]x = 0 is exactly x″ + ω₀²[1 + h cos(ω_d τ)]x = 0 with ω₀² = λ_k² + q̄, h = h_par = q_osc/(λ_k² + q̄), ω_d = ω_q. The principal parametric zone is |ω_d − 2ω₀| < h ω₀/2 (Landau-Lifshitz §27-class standard result, re-derived independently) ⟹ relative half-width δω/ω_d = h/4 at the principal resonance. Volovik's Steps 1–3 are correct as stated. ✓
- *(ii) My Re:V4 error, named precisely.* I used the φ_k-suppressed ODD-channel amplitude as the Mathieu depth. φ_k controls the AMPLITUDE of the rectified odd force (the Berry-leakage throughput — how much secular odd output passes through the window); the window's WIDTH is opened by the FULL modulation depth h_par regardless of which force component rectifies through it. Width and throughput are independent factors of the resonance physics and I conflated them. Retracted; see What Breaks.
- *(iii) Fallback unavailable pre-compute.* A bound h_par ≤ 0.02 would need the PRIMARY (driven-IC) run's ringing fraction, which is NOT in the documented set: XC-6's ±0.2 is the generic-IC slope systematic (a slope-unit object, not an amplitude fraction), and XC-1's +0.0556 tracking lag is a smooth-drift readout — neither converts to q_osc without the npz residuals, and loading the npz is compute, outside this workshop. The max() guard is the only form both safe at any h_par and pre-registrable now. ADOPTED; h_par stays a REPORTED quantity feeding the guard.
- *(iv) One Floquet-side refinement (report-only, no gate change — DISSENT-refinement 1).* The n-th Mathieu zone sits at 2E_k = n·ω_q^phys with width ∝ h_par^n: the principal zone is the widest for any h_par < 1, and the n = 2 zone's rectified throughput carries an extra h_par power on top of its O(h_par²) width. The guard on the principal therefore dominates structurally — but because the pair band is BROAD, an n = 2 coincidence 2E_k = 2ω_q^phys can occur at a different k even when the principal is clear: the sibling REPORTS n = 2 crossings (no gate conjunct — double-suppressed channel).

**C-T5 — D-1 accepted; correction applied to my own R1 rider.** Volovik's chain verified (decelerating mass 1 − 0.6677 = 0.3323; on q_dec ∈ [0, 0.81], 3p_local ∈ [1.657, 3.000] ∋ 2, attained at q_dec = 1/2): my rider (1) phrase "transmits neither 1 nor (at the max-q_dec point) exactly 2" overstated pointwise — slope-2 dilution transmission IS realized on the decelerating mass. The one-line correction is applied in-place to my Re:V1 rider, marked "[corrected R2-B per D-1]" (Effected item 5). Confirmed: no registry, citation, or Stage-0 text carries the retracted wording — clause (d2) and the canonical citation paragraph carry only the window-empty result and the 1.657 clearance, which D-1 leaves intact. One precision audit alongside: using the 4sf re-derived band edge +0.8144 instead of the rounded +0.81 moves the clearance 1.657 → 1.653 — a 0.2% shift, below the `math-scripts.md` 1% mnemonic-vs-exact threshold; the frozen clause (d2) form stands (window-empty needs ≥ 1.857 either way).

**C-T6 — The four volovik R2 touches on my clause-(d) draft: all adopted as merged in the E2 frozen text.** (1) The two-class closure map parenthetical in (d3) — the 1-dof antisymmetry algebra retained as OPERATIVE for the {odd-in-q̇, workless} class, bath-structure closure operative for the {odd-in-H, q̇-independent} geometric class; each class gets exactly one closure. This is sharper than my "demoted to corroborating algebra" and I adopt volovik's precision — including the scope line's retained final clause ("the 1-dof antisymmetry algebra independently closes the q̇-odd workless class"), which is load-bearing under the two-class map, not a vestige. (2) The on-band δΓ fix in (d4) (threshold AND ceiling). (3) The double-lock in (d5) — the thermalized door closes on BOTH the parity theorem and the empty dilution window. (4) The A-V2 coupling sentence in (d5). Also adopted without amendment: **A-V3** (retrieval-layer lodging, final form in E1); **A-V4** (the dP = 0 sentence — its g-evenness chain verified: every term of dP = s dT + n_q dμ + R dK is even-graded, so the constraint surface carries no parity load); **A-V5** (stratum bound frozen as a GRID-mass statement [0.169, 0.668] with the tail-restricted split made an explicit sibling report line — DISSENT-refinement 3); **C-3**'s laboratory grounding of the fourth column (3He-B pair-vibration spectroscopy as the lab image of oscillatory-rectifies-at-resonance, with its honest beyond-pinned-corpus flag).

### DISSENT

**None — full convergence.** Every volovik R2 item is adopted as stated (C-1..C-5, A-V1..A-V5, D-1, D-2/Q-F3). Three additions are folded into the sibling spec as REPORT-ONLY refinements — refinements, not dissents: they add reported diagnostics without touching the PASS/FAIL structure beyond the already-negotiated Q-F3 guard, and all are pre-compute, R2-legal under the negotiation window both sides pinned:

1. **n = 2 Mathieu-zone report** (C-T4.iv): report crossings 2E_k = 2ω_q^phys over the occupied band; double-suppressed channel (width O(h_par²), throughput carries an extra h_par power); no gate conjunct.
2. **Clock-constancy report** (C-T1): report max|Δ ln χ_I(q(τ))| over the tail — quantifies the constant-γ premise of the slope clock-blindness reading; asymptotically 0 at q → 0⁺ by construction (E_n → λ_n).
3. **Tail-restricted stratum split** (A-V5's delegation made explicit): report the fraction of the regression tail with q_dec ∈ (−2, 0) — the theorem-grade-quantitative stratum restricted to the tail, refining the frozen grid-mass bound [0.169, 0.668].

### EMERGENCE

**E-T1 — The clock axis joins the multiplicative-cancellation family; the lineage's observables now carry a two-class invariance taxonomy.** Volovik's A-V2 Step 4 is the TIME-AXIS instance of the `math-scripts.md` §"Multiplicative-normalization cancellation invariants" structural identity (MANDATORY at K=3): under t = γτ the rate observable factorizes as H_phys = γ⁻¹·H(τ) — a clock weight w(γ) multiplying a γ-independent kernel — and every log-derivative slope annihilates it, which is WHY the S97 construction could declare `t_relax = 1.0 # sets units; cancels in slope` at birth and why no gate in the C10 lineage ever needed γ until the resonance comparison. The clock-normalization weight is categorically distinct from the three existing corpus rows (L_max-truncation, τ-moduli-deformation, bottom-K Casimir-ceiling weights) on the spectral-support-form axis — a candidate K=4 corroborating corpus row (status unaffected: the rule is already MANDATORY; routing = orchestrator housekeeping per the corpus append channel, not this workshop). The durable classification for the permanent record: **log-derivative slope observables are clock-blind; spectral positions are clock-keyed.** The W1-2 FAIL lives entirely in the clock-blind class — its permanence is structural, not merely procedural (with the C-T1 asymptotic qualifier under the derived χ_I(q) clock) — and the resonance position is the C10 lineage's FIRST clock-keyed observable. The sibling can land any γ whatsoever without touching W1-2.

**E-T2 — Single-parameter regime classification: the tail repeats the fold's pattern.** The pincer's two-end-state structure (A-V2 Step 7) is, from the transit side, the same structural move that classified the fold: ONE dimensionless ratio partitions the outcome space — at the fold, R_therm = t_therm/t_transit = 5251.82 forced deep-diabatic freeze (P_exc = 1.000, Bogoliubov saturation); on the tail, the single clock γ controls BOTH the resonance position (ω_q^phys = 59.888/γ vs the pair band) AND the window duration (Δt = γ·Δτ vs t_therm) — and self-consistency deletes the corners. Below-band & frozen is not an available state of THIS backbone: the same γ that pushes ω_q^phys below the band stretches the window past t_therm. A naive 3×2 regime grid collapsed to a binary {above-band & frozen} XOR {in-band: live} by one shared parameter is the cleanest post-fold instance yet of rate-vs-internal-scale classification, and it is what makes sibling conjunct (C) a single coupled assert rather than two independent checks. Substrate framing preserved throughout: γ is not an external unit choice but the substrate's own q-channel inertia χ_I expressed as a clock — the derivation route (kernel-reactive response of the fold-frozen relic spectrum) keeps the arrow D_K eigenvalues → ω_n(q) response → χ_I → γ → resonance geometry.

---

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | (a) Partition exhaustiveness (potential-vs-friction) | V1, Re:V1, T1, C-1..C-4, A-V1 | **Emerged** | Partition upgraded to {potential, q̇-coupled, memory} × {SECULAR, OSCILLATORY}; equilibrium = theorem-grade analytic-even (all orders); relic closed at argument-grade by FOUR arguments (order-zero frozen tilt; dilution window EMPTY 0.0000 exact, clearance 1.657; Berry-flat bath structure + C7 zero-counterflow; secularity/dephasing); the legitimate 2-dof escape shape (q, ln a) found and closed (B = 0 exact, number sector); ONE numerical hostage: parametric resonance 2E_k ≈ ω_q → sibling conjunct (C). Scope: equilibrium sector theorem-grade; relic argument-grade pending CF-S101-W1-QEQ-RELIC-ODDFLOOR; KV carve-out CF-S101-W1-QEQ-SELFCONS. |
| 2 | (b) dS-import validity + corrected parity claim w/ regime clause | V2, Re:V2, T2, A-V4, A-V5 | **Converged** | Parity exact to all orders of the graded gradient expansion, (K,R) pair included; coefficients regime-limited (spike x₁ ≈ 1.6×10²; theorem-grade-quantitative stratum grid-mass ∈ [0.169, 0.668]; dP = 0 premise shares the restriction); the verdict consumed only the exponent (κ₂-invariance 7.6e-8) — FAIL untouched. Corrected parity claim = V2.v as amended by A-V4 + A-V5, frozen in the Stage-0 Regime annex (E2). |
| 3 | (c) Registry/capstone citation form | V3, Re:V3, A-V3 | **Converged** | Two-register resolution + retrieval-layer lodging (middle strengthening): token correct in-register and PERMANENT; scoped sentence (E1) mandatory downstream; the scope one-liner lodged where FTS retrieval lands (this row; S100b w1 closure reading; gate-entity note via the orchestrator hygiene pass). Quantifier range unambiguous at pre-registration (transit concession, Re:V3). |
| 4 | (d) Stage-0 candidate / sibling gate spec + CF-S101-W1-QEQ-SELFCONS delta | V4, Re:V4, A-V2, D-2, C-T2..C-T4 | **Converged** | Stage-0 candidate FINAL text FROZEN in-document (E2; clause (e) split (e.1) scope / (e.2) taxonomy register per Q-F1 — ONE Stage-2 PASS-AND unit); sibling gate EMITTED as CF-S101-W1-QEQ-RELIC-ODDFLOOR (Q-F2 confirmed; conjunct C = clock-normalization derivation γ/χ_I + COUPLED resonance/duration assert; width-aware guard Δ_res ≥ max(0.1, 5·h_par/4) per Q-F3/D-2; n=2 zone + χ_I-constancy + tail stratum split = report-only); CF-S101-W1-QEQ-SELFCONS delta ZERO + two non-gating annotations (E4). |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

All physics adjudicated in this workshop is closed; what remains is pre-registered computation (OQ-1..OQ-4), one conditional design question (OQ-5), and two flags (OQ-6, OQ-7).

1. **OQ-1 — Clock normalization γ (sibling conjunct C; the load-bearing derivation).** Derive γ = dt/dτ — equivalently the q-channel inertia χ_I — from substrate inputs; the S97 disclosure `t_relax = 1.0 # sets units; cancels in slope` (s97 L361) is the freedom this fixes. Computation-ready sub-questions:
   - **(1a) Kernel-reactive route (primary, substrate-first)**: χ_I = the frequency-squared coefficient of the principal-value part of the relic kernel T-eq.5 — the standard adiabatic-elimination mass term, χ_I ∝ Σ_n w_n (∂_q E_n)²/E_n³-class = Σ_n w_n/(4E_n⁵)-class using ∂_q E_n = 1/(2E_n) for E_n = √(λ_n² + q); the exact O(1) coefficient and the correct weight (`w_n` vs (n_k + ½)-form via `n_k_gge`) are fixed in-script by the elimination. Then ω_q^phys = √(k_curv/χ_I) [M_KK] and γ = 59.888/ω_q^phys. Dimensional check pre-verified: [k_curv] = M_KK⁻³, [χ_I] = M_KK⁻⁵ ⟹ ω_q^phys in M_KK. ✓
   - **(1b) Constancy report**: max|Δ ln χ_I(q(τ))| over the tail — the constant-γ premise of the clock-blindness reading; asymptotically 0 at q → 0⁺.
   - **(1c) Coupled assert**: with γ in hand, evaluate Δ_res over the occupation-weighted band AND Δt(window) = γ·Δτ vs t_therm ≈ 6 M_KK⁻¹ as ONE two-parameter constraint (A-V2 Step 7); classify the end-state {above-band & frozen} / {in-band: live} / {thermalized hand-off per (d5) double-lock}.
2. **OQ-2 — Odd-coefficient floor (sibling conjunct A)**: |c_odd|/|c_even| ≤ 10⁻³ on the t→−t-graded Markovian reduction of the relic kernel T-eq.5, diagonal + anomalous sectors.
3. **OQ-3 — Window asserts + reports (sibling conjunct B + diagnostics)**: assert max(q_dec) < 1.857 on the tail; report realized min/max of 3p_local; report h_par = q_osc/(λ_min² + q̄) feeding the Q-F3 guard; report n = 2 zone crossings 2E_k = 2ω_q^phys; report the tail-restricted theorem-grade stratum fraction (q_dec ∈ (−2, 0)).
4. **OQ-4 — CF-S101-W1-QEQ-SELFCONS (independent probe, spec untouched)**: gate |slope_selfcons − 1| ≤ 0.05, domfrac ≥ 0.95; plus the both-sides-endorsed amplitude-law diagnostic — regress ln q_amp vs ln|H| directly; a PASS must realize slope 1 specifically through q_amp ∝ |H| (clause-(c) three-selector prediction); a PASS realized any other way is a NEW anomaly worth its own gate.
5. **OQ-5 — Conditional (post-sibling) rectified-drive gate**: IF the sibling lands IN-band (tail crossing exists), candidate C2 is LIVE — a gate measuring the rectified odd drive's amplitude and transmitted slope must be designed THEN; its inputs include the realized γ and crossing geometry, so it fails the 4-field test today on the Inputs field — open question, not carry-forward.
6. **OQ-6 — κ₂-precision flag (no gate pre-registered)**: any future n_q/κ₂ numerical extraction must excise the spike region (x₁ ≈ 1.6×10²) or resum the gradient corrections (V2.iii; Regime annex (α)).
7. **OQ-7 — Stage pipeline (procedural)**: Stage-1 registration of the E2 FROZEN candidate at S101 (`STAGE-1-CANDIDATE` tag; joint clauses (e), (f) flagged for Stage-2 PASS-AND); Stage-2 dispatch ordered AFTER the sibling lands (FAIL routing amends clause (d) BEFORE Stage-2 per the spec); reviewer pools per the E2 freeze marker.

## Wrap-Up — Workshop Impact Summary

### What Changed

**(a) Numerical revisions**

- Dilution-mimic window: unquantified risk → **0.0000 EXACT** (requires q_dec ∈ [1.857, 2.158]; documented backbone max +0.81 at all 999 points; closest approach 3p_local = 1.657 — 0.2% shift to 1.653 under the 4sf band edge, sub-threshold per `math-scripts.md` mnemonic-vs-exact).
- Theorem-grade-quantitative stratum: adjectives → grid-mass fraction ∈ **[0.169, 0.668]** (lower bound exact from W1-1 documented masses, 0.6677 − 0.4985; tail-restricted split → sibling report).
- Spike severity quantified: ε_ad = 0.897 → **x₁ = |Ḣ|/H² ≈ 1.6×10²** at the spike; transmission-correction budget |Δslope| ≲ 0.26 (factor ~4 short of the 1.056 needed) retires the "backbone non-adiabaticity rescues slope 1 by transmission" sub-family.
- Pair-band bottom tightened: 2Δ_BCS ≈ 0.93 M_KK → **2λ_min = 1.63948 M_KK** (documented bottom-triple; slowest pair phase raised 1.76×, all dephasing statements strengthened).
- Below-band pincer numbers: γ ≥ 36.53 (weak 25.83) M_KK⁻¹ ⟹ Δt(window) ≈ 4.8–9.5 (weak 3.4–6.7) M_KK⁻¹ vs t_therm ≈ 6 M_KK⁻¹ — full-window freeze premise broken (ratio 1.12–1.59), tail floor strained (0.56–0.79).
- Resonance guard: flat Δ_res ≥ 0.1 → **max(0.1, 5·h_par/4)** (width-aware, ≥ 5× the principal Mathieu half-width h_par/4 at any depth; D-2/Q-F3).
- Squeeze-phase leakage bookkeeping consolidated: O(φ_k) = 0.005–0.012 rad, pair-band rotation ≥ 2λ_min, 1/√59.8 ≈ 0.13 incoherent stacking.

**(b) Structural changes**

- Force partition upgraded: {potential, q̇-coupled, memory} → **× {SECULAR, OSCILLATORY}**; exhaustiveness re-scoped to "Markovian-reducible (off-resonant), analytic, frequency-modulated-bath dynamics; the 1-dof antisymmetry algebra independently closes the q̇-odd workless class."
- WP §W1-2 "odd ⟹ dissipative" parenthetical **RETRACTED** (corpus counterexample: Paper 11 §VI contracting-dS equilibrium branch); theorem re-founded as an all-orders ANALYTICITY/parity statement with sector-by-sector closure.
- Slope-selection rule: two selectors → **THREE** (equilibrium analyticity → even integers; amplitude self-consistency → 1 via |H| = √(H²); SECULARITY suppresses every other relic channel — failure window = parametric resonance, pre-registered).
- The (q, ln a) 2-dof arena **RULED IN** (chain B's N = 1 premise replaced by the gate's own fixed-backbone design); gyroscopic closure re-founded on bath structure (Berry-flatness B = 0 exact for the number sector; φ_k leakage bounded; C7 zero-counterflow) under the two-class closure map.
- Relic-sector closure: three arguments → **FOUR**, plus the (d5) thermalization pincer with DOUBLE-locked thermalized door.
- Citation discipline: two-register resolution + **retrieval-layer lodging** (token retained and permanent; expansion rule mandatory; the scope one-liner lodged where FTS retrieval lands).
- Observable invariance taxonomy: **clock-blind log-derivative slopes vs clock-keyed spectral positions** — the FAIL is clock-blind (structurally permanent under any constant re-clocking; asymptotically under the derived χ_I(q) clock); the resonance position is the C10 lineage's first clock-keyed observable.
- Naive 3×2 regime grid → **two self-consistent end-states** {above-band & frozen} XOR {in-band: live} (below-band corner pincer-deleted through the shared clock).
- **Stage-0 joint-theorem candidate FROZEN** (E2); **sibling gate CF-S101-W1-QEQ-RELIC-ODDFLOOR EMITTED** (Carry-Forward block).

### What Holds

- **The W1-2 FAIL verdict** (audit e31d45cf5309b32cde67804d0576467592196b45ea908ec1edfac7f522212ca4) — untouched at every step of both rounds; PERMANENT procedurally (`gate-verdicts.md`) and now STRUCTURALLY (clock-blind observable class: γ-invariant under any constant re-clocking, asymptotically under the derived clock; κ₂-invariant by XC-5).
- Chain A parity theorem — all orders in the graded gradient expansion, (K,R) pair included; F(T) = ∫s dT even for ANY odd s (linearity-, coefficient-, and convention-independent).
- All three measured slopes: 2.0556 (GD drive, even-locked + tracking lag) / 1.008273 (imposed |H|-closure, = S99 at 4.6e-8) / 3.4159 (bare).
- CF-S101-W1-QEQ-SELFCONS: 4-field spec delta **ZERO**, confirmed independently from both sides (V4.ii / Re:V4).
- The KV carve-out as parity-CONSISTENT: |H| is even — it occupies the unique non-analytic-even cell, completing the slope-selection rule rather than evading the theorem.
- C10 Object-C STRUCTURALLY-CONDITIONAL tag; capstone §8.5 OPEN-by-design (status unchanged; the conditionality LOCUS is now nameable — E3 item 3, routed).
- Q-T1 window-empty result (the dilution-mimic candidate is dead on this backbone); chain B's 1×1 antisymmetry algebra (operative for the q̇-odd workless class under the two-class map).
- The verdict token `no_slope1_capable_substrate_drive` — correct within its pre-registered quantifier range (plan §W1-2 Definition 4 enumerated drive candidates + fixed backbone; transit concession at Re:V3).
- The fold/tail two-clocks separation: R_therm = 5251.82 scopes the FOLD (deep-diabatic, Bogoliubov saturation); ε_ad = 0.897 scopes the TAIL (adiabatic-with-corrections); neither regime's credentials transfer to the other.

### What Breaks or Strains

**Breaks (retracted or corrected in-workshop):**

- WP §W1-2 "odd ⟹ dissipative" parenthetical — RETRACTED (V1.i; corpus witness Paper 11 §VI). Landed artifact NOT retroactively edited (landed-artifact discipline); the statement of record is the scoped theorem (V2.v as amended by A-V4/A-V5) frozen in the E2 Regime annex.
- transit's R1 rider (1) — pointwise overstatement "transmits neither 1 nor exactly 2"; corrected in-place per D-1 (Effected item 5); 3p_local sweeps through 2 on the 33.2% decelerating grid mass.
- transit's Re:V4 flat-guard rationale — the φ_k-as-Mathieu-depth conflation (width vs throughput); replaced by the width-aware guard (C-T4/Q-F3).

**Strains (regime-limited, disclosed, not broken):**

- Leading-order dS coefficients at the spike (x₁ ≈ 1.6×10²; marginal O(1) on the in-band decelerating stratum) — κ₂-precision-limiting only, never the FAIL; the dP = 0 premise of GD-4 shares the restriction (A-V4 sentence, frozen in the annex).
- "1-dof" as the headline gyroscopic closure — demoted for the geometric (q, ln a) class; retained as operative for the q̇-odd workless class (two-class closure map, C-1.iii).
- The below-band corner of the regime grid — self-inconsistent under the shared clock (pincer-coupled); survives only as the thermalized hand-off, where the double-lock closes it on parity-consistent ground.
- The frozen-relic premise on long windows — duration-consistency is now an explicit sibling assert (Δt(window) vs t_therm), no longer an unexamined background assumption.

### Carry-Forward Computations (MATH ONLY — propagate to S101)

One new item passes the 4-field test. (CF-S101-W1-QEQ-SELFCONS is NOT re-listed: its spec lives in the W1 working paper "Carry-Forward Computations" block, delta ZERO per E4 — it is referenced, not duplicated.)

#### CF-S101-W1-QEQ-RELIC-ODDFLOOR — relic-sector odd-in-H floor + resonance-window closure (SIBLING to CF-S101-W1-QEQ-SELFCONS, NOT a replacement; gate-ID confirmed per Q-F2)

1. **What**: Graded decomposition of the GGE-relic-induced effective force on the q-channel: **(A)** odd-coefficient floor on the t→−t-graded Markovian reduction of the relic kernel (diagonal + anomalous sectors; T-eq.5). **(B)** Verification-assert of the analytic dilution-window result — assert max(q_dec) < 1.857 on the regression tail; report realized min/max of 3p_local. **(C)** Clock-normalization + coupled resonance/duration: derive γ = dt/dτ (equivalently the q-channel inertia χ_I; primary route = kernel-reactive, the frequency-squared coefficient of the principal-value part of T-eq.5, χ_I ∝ Σ_n w_n/(4E_n⁵)-class with the exact O(1) coefficient and weight choice fixed in-script by the adiabatic elimination — the S97 `t_relax = 1.0 # sets units; cancels in slope` [s97 L361] is the disclosed freedom this fixes); convert ω_q = 59.888 τ⁻¹ and the pair band to the common clock via ω_q^phys = √(k_curv/χ_I); report Δ_res = min_k |2E_k − ω_q^phys|/ω_q^phys over the OCCUPATION-WEIGHTED support of {n_k, σ_k} (npz keys `w_n`/`n_k_gge`) AND band edges from both the 992-mode working set and the full L_max=12 cache (band-top caveat, A-V2 R1); report any tail crossing 2E_k(q(τ)) = ω_q^phys; report the measured parametric depth h_par = q_osc/(λ_min² + q̄) (tail ringing amplitude at ω_q); report Δt(window) = γ·Δτ vs t_therm ≈ 6 M_KK⁻¹ (the (d5) pincer assert; below-band + frozen is the self-inconsistent corner per A-V2 Step 7). **Report-only diagnostics (non-gating)**: max|Δ ln χ_I(q(τ))| over the tail (clock-constancy of the γ-invariance reading); n = 2 Mathieu-zone crossings 2E_k = 2ω_q^phys (width O(h_par²), throughput extra-h_par-suppressed); tail-restricted theorem-grade stratum fraction (q_dec ∈ (−2, 0)).
2. **Inputs**: `computations/session-100a/s100a_w1_qeq_drive.npz` (audit e31d45cf5309b32c); `computations/session-99/s99_w1_q_nonratio_observable.npz` (backbone; p_local(τ) = −H²/Ḣ); `computations/session-99/s99_w2_relaxation_closure.npz` (K_CURV, q_boundary); `computations/session-97/s97_w2_2_c10_n_exponent.npz` (ω_n(q), `w_n`, `n_k_gge` — the clock-normalization provenance); L_max=12 master spectrum cache (band-top); GGE occupation artifacts (S38/S95 lineage); the T-eq.5 kernel construction (workshop T1-C4).
3. **Gate**: PASS iff |c_odd|/|c_even| ≤ 10⁻³ AND assert (B) holds AND [Δ_res ≥ max(0.1, 5·h_par/4) with no tail crossing — width-aware guard per Q-F3/D-2, ≥ 5× the principal-zone half-width at any h_par] AND the frozen-branch premise is duration-consistent (Δt(window) < t_therm, OR the thermalized hand-off documented per the (d5) double-lock). INFO iff the only miss is Δ_res below the guard with no tail crossing (near-resonant — documented, clause (d4) carries it) OR Δt(window) ∈ [0.5, 1.5]·t_therm (crossover window — documented, clause (d5) carries it). FAIL iff a tail crossing exists OR the odd-floor is violated. FAIL routing: relic clause (d) demoted argument-grade → coincidence-bounded; Stage-1 entry text amended BEFORE any Stage-2 dispatch.
4. **Effort**: ~1 wave (the γ/χ_I derivation is the one new element; band comparison, h_par measurement, reports, and asserts are post-processing on existing caches; no diagonalization).

**Depends on** (per `output-standards.md` carry-forward dependency enumeration): the four pinned npz inputs above (UPSTREAM GATES: S100a-W1-2, S99-W1/W2, S97-W2-2); the E2 Stage-0 clause (d4)/(d5) text (REGISTRY-PENDING: Stage-1 entry at S101); `t_therm ≈ 6 M_KK⁻¹` (S39-corrected, OOM-grade); no canonical_constants pin is consumed beyond the verdict-file documented set.

[Threshold status: all conjuncts two-sided agreed pre-compute — the Q-F3 guard form was the single open item and is resolved-adopted at C-T4; the three report-only diagnostics are R2-B refinements with no PASS/FAIL load. No post-compute negotiation remains.]

### Effected In-Session (NON-MATH — completed by the final agent BEFORE terminating)

- [x] **(1) Pinned scoped-claim citation text (CANONICAL — FINAL)** — EFFECTED in-document at block E1 below (this file, lines 937–941): the canonical citation paragraph + expansion rule + retrieval-layer lodging, reproducing landing-list (ii) verbatim with the Q-F2-confirmed sibling ID; supersedes V3.iii; downstream consumers copy from E1. The scope one-liner is additionally lodged in Workshop Verdict row 1 (retrieval-layer carrier (a)).
- [x] **(2) Stage-0 joint-theorem candidate FINAL text** — EFFECTED in-document at block E2 below (this file, lines 943–957), marked Stage-0 FROZEN with reviewer pools + author exclusion; reproduces landing-list (iii) verbatim with the Q-F1 (e.1)/(e.2) split applied (ONE Stage-2 PASS-AND unit); clause (d2) number frozen; clauses (d4)/(e.1) carry the Q-F2-confirmed sibling ID.
- [x] **(3) Four downstream-consumer citation texts** — EFFECTED in-document at block E3 below (this file, lines 959–964), reproducing landing-list (vi): items 1–2 drafted for the S100b owners (no sessions/session-100b/ file touched); item 3 marked ROUTED-TO-SOLE-WRITER (capstone designated writer; capstone-hygiene Q3/Q4); item 4 marked ROUTED to the orchestrator hygiene pass (with the V5.6b R_therm touch-up). No mack §7 falsifier surface is touched by this workshop's outputs (the H-parity wall is not a falsifier observable; no inventory row emerges).
- [x] **(4) Delta-to-CF-S101-W1-QEQ-SELFCONS statement** — EFFECTED in-document at block E4 below (this file, line 966): ZERO to the 4-field spec + two non-gating annotations, both sides confirmed.
- [x] **(5) D-1 rider correction** — EFFECTED in-document: transit's own Re:V1 rider (1) phrase corrected in-place at line 311 (this file), marked "[corrected R2-B per D-1]"; verified that the retracted wording propagates to no verdict cell, citation, Stage-0, or carry-forward text.

---

**(E1) — CANONICAL CITATION PARAGRAPH (FINAL; supersedes V3.iii; adopted from landing-list (ii) verbatim):**

> **Canonical downstream citation for S100a-W1-2-QEQ-DRIVE (FAIL, audit e31d45cf5309b32cde67804d0576467592196b45ea908ec1edfac7f522212ca4):** On a fixed backbone, no substrate-internal EQUILIBRIUM-THERMODYNAMIC drive q_eq(H) can carry odd-in-H structure: every equilibrium Gibbs-Duhem potential shift is analytic-even in H (H-parity theorem, scoped form per the S100a W-1 workshop; leading power H², transmitted slope 2.0556 measured, κ-invariant at 7.6e-8). The slope-1 leg of the n = 2 tracking law is therefore an imposed-closure INPUT on any fixed backbone. Scope: equilibrium sector — theorem-grade; fold-frozen GGE relic sector — excluded at argument-grade (order-zero frozen occupations + dilution-mimic window EMPTY [0.0000 exact: requires q_dec ∈ [1.857, 2.158], documented backbone max +0.81, closest approach 3p_local = 1.657] + bath-structure gyroscopic closure [Berry-flat frequency-only modulation, B = 0 exact for the number sector; squeeze-phase leakage ≤ 1.2%, pair-band dephased; C7 zero-counterflow T^{0i}_4D = 0 exact] — pending the sibling resonance check CF-S101-W1-QEQ-RELIC-ODDFLOOR); non-Markovian memory terms — SCOPED: secular outputs exhausted off-resonance by {δk_curv even-reactive; on-band-gated δΓ; order-zero tilt}, with parametric rectification at 2E_k ≈ ω_q the unique surviving odd channel (sibling conjunct C). The surviving slope-1 route is Klinkhamer-Volovik oscillation-energy self-consistency (back-reaction, not a drive; q_amp ∝ |H|, parity-CONSISTENT non-analytic-even form; Paper 25 §V Eqs. (5.5a-b)), pre-registered as CF-S101-W1-QEQ-SELFCONS.
>
> **Expansion rule:** any downstream citation of the token `no_slope1_capable_substrate_drive` MUST expand it with the three scope qualifiers — (drive-type: potential-slot q_eq(H)), (fixed-backbone), (equilibrium = theorem-grade / relic = argument-grade pending sibling) — plus the carve-out pointer. **Retrieval-layer lodging:** the one-line scope pointer ("scope: equilibrium sector theorem-grade; relic argument-grade pending CF-S101-W1-QEQ-RELIC-ODDFLOOR; KV carve-out CF-S101-W1-QEQ-SELFCONS") lives in the Workshop Verdict row, the S100b w1 closure reading, and the gate-entity note (orchestrator hygiene pass, routed with the V5.6b R_therm touch-up).

**(E2) — STAGE-0 JOINT-THEOREM CANDIDATE (FINAL TEXT):**

**Stage-0 FROZEN — Stage-1 registration at S101 per `joint-theorem-promotion.md` (`STAGE-1-CANDIDATE` tag; joint clauses (e), (f) flagged for Stage-2 PASS-AND); Stage-2 reviewer pools preserved: Axis-A ∈ {lizzi-spectral-functional-theorist, connes-ncg-theorist} × Axis-B ∈ {gen-physicist, kitaev-quantum-chaos-theorist}; Stage-0 authors volovik + transit EXCLUDED from Stage-2 (Axis-B Selection Protocol, all three conditions; S99 E1 author-exclusion discipline).**

> **THEOREM CANDIDATE — H-PARITY-DRIVE-EXCLUSION (fixed-backbone q-channel)**
>
> - **Clause (a) [volovik-side]:** The Gibbs-Duhem derivation chain GD-1..GD-5 (assumptions enumerated per workshop V1.ii) yields the parameter-free substrate drive q_eq(H) = κ₂H², κ₂ = 3/(8πG·n_q·k_curv); the exponent is locked by the s ∝ T Gibbs-Duhem integration + the quadratic well; the coefficient is regime-limited per the Regime annex and verdict-irrelevant (XC-5, 7.6e-8).
> - **Clause (b) [volovik-side]:** All-orders H-parity grading — equilibrium T and s are t→−t-odd (anchor: Paper 11 §VI, contracting dS with T < 0, S = −A/4G); all dimensionless gradient ratios Ḣ/H², Ḧ/H³, … are even; every equilibrium Gibbs-Duhem potential shift, including the (K,R)-pair extension (Paper 11 Eq. (8), R = 12H² even), is even-graded and analytic in H², to all orders in the gradient expansion. No analytic odd-in-H equilibrium potential term exists at any order.
> - **Clause (c) [volovik-side]:** Slope-selection corollary — THREE selectors: equilibrium analyticity confines late-tail log-slopes to even integers (generically 2); amplitude self-consistency selects 1 via the unique non-analytic-even form |H| = √(H²); SECULARITY (phase-averaging over the gapped pair band, 2E_k ≥ 2λ_min = 1.639 M_KK, with ~1/√59.8 incoherent stacking) suppresses every other relic-sourced channel off-resonance, with parametric resonance 2E_k ≈ ω_q its pre-registered failure window. Numerical instantiation: 2.0556 (GD drive, even-locked + tracking lag) / 1.008273 (imposed |H|-form closure, = S99 at 4.6e-8) / 3.4159 (bare).
> - **Regime annex (to clauses a–b):** (α) Parity is exact order-by-order; the leading-order COEFFICIENTS are quantitatively reliable only where |Ḣ|/H² ≪ 1: on the gate's backbone this is violated at the Ḣ-spike (|Ḣ|/H² ≈ 1.6×10² at the ε_ad = 0.897 point) and marginal (O(1)) on the in-band decelerating stratum. Theorem-grade-QUANTITATIVE stratum (|Ḣ|/H² < 1 ⟺ q_dec ∈ (−2, 0)): grid-mass fraction ∈ [0.169, 0.668] of the 999-point backbone (lower bound exact from S100a-W1-1 documented masses, 0.6677 − 0.4985, verdict line 12 + XC-4 backbone identity; upper bound over-counts the deep-acceleration excursions; tail-restricted split = sibling diagnostic). The dP = 0 balance premise of GD-4 shares the same quantitative regime restriction as the leading-order coefficients (parity unaffected: dP = 0 is g-even). All of this limits κ₂-precision only, never the FAIL (XC-5 coefficient-invariance, 7.6e-8); any future κ₂-precision extraction must excise the spike region or resum the gradient corrections. (β) The theorem is VACUOUS — not violated — on sectors possessing no local-equilibrium state functions: the fold-frozen GGE relic (diabatic transit-freeze, R_therm = 5251.82, S95-certified, verdict-file line 82; finite t_therm ≈ 6 M_KK⁻¹ per the S39 correction), closed separately at argument-grade by clause (d). (γ) Non-analytic even forms |H| = √(H²) (amplitude variables — the KV self-consistency route, Paper 25 §V Eqs. (5.5a-b)) are OUTSIDE the theorem's domain: routed to CF-S101-W1-QEQ-SELFCONS (clause f).
> - **Clause (d) [transit-side]: Non-equilibrium-sector exclusion boundary.** (d1) At adiabatic order ZERO the fold-frozen relic tilt F_GGE = −Σ_k n_k ∂_q E_k(q, a) is functionally H-independent at fixed (q, a) [frozen occupations; diabatic transit-freeze R_therm = 5251.82, S95-certified, verdict-file line 82; the order-zero qualifier is load-bearing — the first-order response LAG does carry H, see (d4)]. (d2) Dilution-trajectory transmission: a relic dilution tilt transmits late-tail slope 3·p_local·(1+w)|_{w=0} = 3p_local with p_local = 1/(1+q_dec); the slope-1 mimic window 3p_local ∈ [0.95, 1.05] requires q_dec ∈ [1.857, 2.158] (stiff-fluid-class deceleration), while the documented backbone maximum is q_dec ≤ +0.81 at all 999 points (S100a-W1-1 miss_above_band = 0.000000; backbone identity XC-4) — **window fraction = 0.0000 EXACT**, closest approach 3p_local = 1.657; the dilution-mimic route is dead on this backbone. (d3) Gyroscopic/geometric route: the fixed-backbone design promotes the dilution coordinate ln a to a second slow parameter — the gyroscopic class on the (q, ln a) pair is NOT emptied by dof-counting (the 1-dof antisymmetry algebra remains the operative closure for forces odd in q̇ alone; the geometric q̇-independent class is the one needing bath structure); it is closed by bath structure: (i) Berry-flatness — the relic bath is frequency-modulated only (Y = 0 squeeze-axis slice; ω_n(q) = √(λ_n² + q) modulates X = E_k² alone), where the generalized-oscillator Berry curvature pulls back to zero EXACTLY; (ii) squeeze-phase leakage is bounded at O(φ_k) ≈ 0.005–0.012 rad [S95 W6-6 / S76 W1-C lineage] and rotates at pair frequencies ≥ 2λ_min (dephased off-resonance; 59.8-pair incoherent stacking adds ~1/√N ≈ 0.13); (iii) the Magnus/Iordanskii class vanishes independently by zero counterflow, T^{0i}_4D = 0 EXACT [atlas-04 C7], and by homogeneity (no scattering kinematics in the k = 0 channel). (d4) Memory slot (SCOPED, not open-ended): the relic kernel's Markovian reduction is controlled off-resonance and even-graded at SECULAR order (constructive decomposition, workshop T1-C4/T2; Berry-flatness T-eq.2 is the geometric statement of the same fact); its secular outputs are exhausted by {δk_curv(a) even-reactive; δΓ on-shell friction (present only if ω_q lies ON the pair band — threshold AND ceiling, same clock check as the resonance); the order-zero adiabatic tilt of (d1)}; the unique surviving odd channel is parametric rectification at 2E_k ≈ ω_q — bounded by sibling conjunct (C), PENDING SIBLING (CF-S101-W1-QEQ-RELIC-ODDFLOOR); absent a tail crossing, the relic sector admits NO secular odd-in-H potential term. (d5) Pincer closure on the freeze premise: if the gate window instead OUTLASTS t_therm ≈ 6 M_KK⁻¹ (S39-corrected finite thermalization), the relic sector acquires local-equilibrium state functions and the closure DOUBLE-locks — its H-graded equilibrium response falls under clauses (a)–(c) directly (the parity THEOREM), and its residual matter-sector tilt is (d2)'s dilution object (window empty); frozen ⟹ (d1)–(d4); thermalized ⟹ double-locked; only the transient crossover window escapes both, bounded by t_therm. The duration and resonance asserts are COUPLED through the single clock normalization γ = dt/dτ (workshop A-V2 Step 7): holding ω_q below the pair band throughout the tail forces Δt(window) ≳ t_therm (4.8–9.5 M_KK⁻¹ vs ≈ 6), pressing the below-band corner into the thermalized door — sibling conjunct (C) quantifies.
> - **Clause (e) [JOINT — scope statement; sub-lines (e.1) + (e.2) form ONE Stage-2 PASS-AND unit]:**
>   - **(e.1) Scope:** the wall reads "no slope-1-capable substrate-internal DRIVE on a fixed backbone," where: equilibrium stratum = theorem-grade (clauses a–c + Regime annex); fold-frozen GGE relic sector = argument-grade (clause d: four closure arguments; single numerical hostage = the parametric-resonance window, pending CF-S101-W1-QEQ-RELIC-ODDFLOOR); back-reaction = outside the quantifier range (not covered, not violated). Downstream citation per the expansion rule + retrieval-layer lodging (canonical citation paragraph, block E1 of the S100a W-1 workshop Wrap-Up).
>   - **(e.2) Force-taxonomy register:** {potential, q̇-coupled, memory} × {SECULAR, OSCILLATORY}; the exhaustiveness claim is scoped "exhaustive for Markovian-reducible (off-resonant), analytic, frequency-modulated-bath dynamics; the 1-dof antisymmetry algebra independently closes the q̇-odd workless class."
> - **Clause (f) [JOINT — self-consistency carve-out]:** the Klinkhamer-Volovik oscillation-energy amplitude route (Paper 25 §V Eqs. (5.5a-b); two-component exchange-dynamics blueprint, Paper 35 §V) is the unique surviving slope-1 mechanism; it is parity-CONSISTENT (|H| is even — it occupies the non-analytic-even cell the theorem leaves open, completing the clause-(c) slope-selection rule rather than evading it); pre-registered as CF-S101-W1-QEQ-SELFCONS, spec delta ZERO; a PASS must realize slope 1 specifically through the amplitude law q_amp ∝ |H| (both-sides-endorsed non-gating diagnostic).

**(E3) — DOWNSTREAM-CONSUMER CITATION TEXTS (four; drafted verbatim, routing marked):**

1. **S100b w1 closure reading** [drafted for the S100b schedule owner — NOT self-applied; no sessions/session-100b/ file touched]: inherits block E1 verbatim. No additional text.
2. **S100b X-wave C10 n_eff triangle** (S100b-X-C10-RHOVAC-EPOCH-PROFILE, trigger-first on this gate; S100b-X-C10-BBN-CONSTRAINT-RECONCILE) [drafted for the S100b schedule owner — NOT self-applied]: the ~4.11 member carries the mandatory tag — *"n ≈ 4.11 = 2 × 2.0556 is the FIXED-BACKBONE equilibrium-GD drive law AS-MEASURED (corridor-map value; contains the +0.0556 tracking lag, XC-1). Structural comparisons at the 0.1 level use 2 × 2 = 4 (the locked exponent product); as-measured comparisons use 4.11 — state which is carried. NOT the framework's physical n_eff prediction; the physical route is the self-consistency channel (n = 2 if CF-S101-W1-QEQ-SELFCONS lands PASS)."* Triangle-coherence adjudication {2.3, <2, ~4.11} remains OWNED by the S100b schedule; this workshop pins only the tag and the scope clause the members cite.
3. **Capstone §8.5** [ROUTED-TO-SOLE-WRITER: capstone designated writer; capstone-hygiene Q3/Q4 apply — drafted verbatim, NOT self-applied]: status unchanged — OPEN by design — with the conditionality locus: *"the q ∝ H closure implicitly assumes the amplitude (square-root-of-energy) mechanism without deriving it; equilibrium thermodynamics cannot supply it (H-parity, S100a-W1-2); derivation attempt = CF-S101-W1-QEQ-SELFCONS; relic-sector exclusion boundary = CF-S101-W1-QEQ-RELIC-ODDFLOOR (pending)."*
4. **Gate-entity note** (knowledge MCP) [ROUTED: orchestrator hygiene pass, with the V5.6b R_therm touch-up — drafted verbatim, NOT self-applied]: the one-line scope pointer exactly as in E1's retrieval-layer lodging — *"scope: equilibrium sector theorem-grade; relic argument-grade pending CF-S101-W1-QEQ-RELIC-ODDFLOOR; KV carve-out CF-S101-W1-QEQ-SELFCONS."*

**(E4) — DELTA TO CF-S101-W1-QEQ-SELFCONS: ZERO.** The 4-field spec (what / inputs / gate `|slope_selfcons − 1| ≤ 0.05`, domfrac ≥ 0.95 / effort ~1 wave; W1 working-paper "Carry-Forward Computations" block) is untouched — confirmed independently from the volovik side (V4.ii) and the transit side (Re:V4). Two NON-GATING annotations ride along for the S101 planner: (1) consumers inherit the citation-scope clause (block E1); (2) the amplitude-law diagnostic — regress ln q_amp vs ln |H| directly; a PASS must realize slope 1 specifically through q_amp ∝ |H| (the non-analytic-even form, clause-(c) three-selector prediction); a PASS realized any other way is a NEW anomaly worth its own gate. The sibling (CF-S101-W1-QEQ-RELIC-ODDFLOOR) and the CF are logically independent probes of disjoint quantifier ranges (drive slot on a fixed backbone vs back-reaction); both run; neither pre-judges the other.

### Closing Line

A one-bit FAIL entered this workshop and leaves as a frozen theorem candidate, a three-selector slope rule, a four-argument relic closure with one named numerical hostage, and two logically independent pre-registered probes — the verdict itself untouched at every step, and now provably untouchable by any clock.
