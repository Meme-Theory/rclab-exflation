# Off-Session Conversation Transcript — Riemann Hypothesis from the Substrate / Universe as Calculator

**Date**: 2026-06-11
**Status**: OFF-SESSION EXPLORATORY. No gates, no verdict lines, no registry writes.
**Participants**: user (Ryan), orchestrator (Claude)
**Artifacts produced**: `computations/offsession-riemann/_rh_substrate_sanity.py`, `rh_substrate_sanity.npz`, `rh_substrate_sanity.png`
**Purpose of this document**: faithful source transcript for `/rclab-review` solo synthesis. Substantive content reproduced verbatim; tool-call mechanics condensed into bracketed process notes.

---

## Turn 1 — user

> Fun off-session idea that has been in the back of my mind for like 80 sessions - can we project the entire Reimann Hypothosis from the mathmatical substrate, and use the Universe as a literal Universal Sized Calculator to proof it to the Universal Degree?

## Turn 2 — orchestrator

[Process note: before answering, queried the knowledge MCP. `"Hilbert-Polya" OR "Riemann hypothesis" OR "critical line" OR "Euler product"` returned ZERO hits across 104 sessions — virgin territory. Level-statistics search returned gate CHAOS-1: single-particle `⟨r⟩ = 0.321` (sub-Poisson); multi-cell `r_pooled = 0.422`; references Poisson ≈ 0.386, GUE ≈ 0.603; verdict DIAGNOSTIC: ORDERED (scripts s38/s61/s100b/s104 level-spacing lineage).]

### The short version

Your instinct has a name — it's the **Hilbert–Pólya conjecture** (find a self-adjoint operator whose spectrum is the Riemann zeros; self-adjointness forces real spectrum, which forces every zero onto the critical line) — and it is not a crank idea. It is the *only* strategy that has ever actually proven an RH-analog. But there are two hard verdicts: (1) the framework's own PROVEN theorems structurally disqualify D_K as the operator, and (2) "universe as calculator" can *verify* RH to cosmic depth but can never *prove* it — and number theory has a brutal precedent showing why that distinction isn't pedantic.

### Why the instinct is the historically winning one

Every Riemann-Hypothesis-shaped statement humanity has ever closed was closed by **finding its substrate**:

- **RH over function fields** (curves over finite fields): proven by Weil, then Deligne for general varieties — the zeros ARE eigenvalues of the Frobenius operator acting on a cohomology, and a positivity structure pins them. Substrate found → RH proven.
- **Selberg zeta** (hyperbolic surfaces): has an Euler product over closed geodesics ("primes" = prime geodesics) AND a spectral realization — its zeros correspond to eigenvalues of the Laplacian, which is self-adjoint. Its RH is a *theorem*, by exactly the mechanism proposed.
- **The original RH over ℚ**: the one case where nobody has found the substrate. Connes' noncommutative-geometry program — the same Connes whose spectral triples this entire project runs on — is precisely a 25-year hunt for it. His candidate substrate is the **adele class space** A_ℚ/ℚ*, where RH becomes a trace-formula positivity statement (Weil positivity).

So "project RH from a mathematical substrate" is, quite literally, Connes' day job, using the toolbox already in this repo. The pattern is sound. The question is whether *this* substrate is the right one.

### Three walls: why D_K is not the Riemann operator

The conjectural "Riemann dynamics" (Berry–Keating desiderata, from memory) must be: **chaotic, time-reversal-breaking, and effectively one-dimensional**, with periodic orbits of period log p playing the role of primes. The substrate fails all three, and two of the failures are PROVEN registry results:

**Wall 1 — Wrong symmetry class (PROVEN).** The Montgomery–Odlyzko result is that Riemann zeros have GUE pair-correlation statistics — the unitary class, which requires *broken* time-reversal symmetry. The substrate is AZ class **BDI** (PROVEN, registry) — time-reversal symmetric with T² = +1. A BDI operator structurally cannot produce GUE statistics. The fabric's symmetry class excludes it from candidacy before any computation runs.

**Wall 2 — Wrong universality class, measured (CHAOS-1).** Even setting symmetry aside, D_K's block-diagonality by Peter–Weyl (PROVEN) means its spectrum is a superposition of independent sector spectra — and superposed independent spectra give Poisson statistics *by construction*. CHAOS-1 confirms: ⟨r⟩ = 0.321–0.422, ORDERED/integrable, versus GUE's 0.603. The substrate is too *symmetric* to sing the primes. The very theorems the project is proudest of — block-diagonality, integrability, the Ordered Veil — are precisely the disqualifying evidence. The Riemann operator must be chaotic; this fabric is a crystal of order.

**Wall 3 — Wrong Weyl law.** Riemann zeros count as N(T) ~ (T/2π)·log(T/2π) — the signature of a quasi-1D system with a logarithmic correction (this is why Berry–Keating's candidate is the humble H = xp). The substrate's dimension spectrum is {0, 2, 4, 6, 8} — d = 8 leading Weyl growth, N(λ) ~ λ⁸. No truncation, deformation, or regulator choice turns λ⁸ into T·log T; that's a dimension-spectrum invariant, exactly the kind of wall this project treats as permanent.

**The mirror and the pin (structural root cause).** RH needs two ingredients. The *functional equation* (the s ↔ 1−s mirror symmetry defining the critical line) is genuinely physical — it follows from heat-kernel modularity via Poisson summation, the same Mellin-transform machinery as this project's dimension-spectrum poles. Any decent substrate computes the mirror for free; in a real sense the fabric already does. The *Euler product* (the pin that forces zeros ONTO the mirror) is pure arithmetic — unique factorization in ℤ. Davenport–Heilbronn (1936) built a function with a perfect functional equation and no Euler product: it has zeros scattered off the line. Physics supplies the mirror; only the primes supply the pin. ζ_{D_K} is a Casimir lattice sum (Hurwitz/Epstein class) — its "arithmetic" is the representation ring ℤ[V₃, V̄₃], which has no interesting prime structure. SU(3) knows addition; RH is about multiplication.

### The "Universal Calculator" half: verification has a ceiling, and it's too low

Suppose you commandeered every degree of freedom since the transit. Lloyd's estimate (from memory): the observable universe has performed ~10¹²⁰ elementary operations on ~10⁹⁰ bits. Now:

- RH is equivalent (Lagarias 2002) to an elementary ∀-statement: σ(n) ≤ Hₙ + e^(Hₙ)·log Hₙ for every n ≥ 1. It's a Π₁ statement — a specific Turing machine never halts. A calculator, of any size, can only *run* the machine; only a proof shows it never halts.
- **The Mertens precedent is the killer.** The Mertens conjecture (|M(x)| ≤ √x) was verified for every value ever computed — and it *implies* RH. Odlyzko–te Riele disproved it in 1985, non-constructively; to this day no explicit counterexample has ever been exhibited, only bounds placing the first failure at heights like e^(10⁴⁰) and beyond. A universe-sized calculator running its full 10¹²⁰-op budget would have reported "Mertens: TRUE." Mertens is false. The universe's compute budget is finite; RH's quantifier is not, and number theory demonstrably hides its betrayals above 10³¹⁶ (the first π(x) > Li(x) crossing) — heights no physical computation reaches.
- Current status, for calibration: ~10¹³ zeros verified on the line (Gourdon; Platt–Trudgian rigorously to height 3×10¹²), and >41% of all zeros *proven* on the line (Conrey → Pratt et al., from memory). The universe-calculator would add maybe seven orders of magnitude of verification. Against Π₁, seven orders of magnitude is zero progress.
- The one theoretical loophole — Malament–Hogarth spacetimes, where an observer extracts the result of an infinite computation in finite proper time (Etesi–Németi 2002) — requires causal pathologies at the *emergent* GR level (Kerr inner horizons), which strong cosmic censorship plausibly forbids, and which the substrate framing closes locally anyway: the fabric is a finite spectral triple at every point. 155,984 eigenvalues per point at L_max = 10. The universe is a very large but resolutely **finite-rank spreadsheet**, and Π₁ statements don't fit in finite spreadsheets.

So "proof to the Universal Degree" is strictly weaker than proof — *unless* the universe participates not as calculator but as **proof object**: if some physical structure's operator provably has the zeros as its spectrum, then its self-adjointness covers all infinitely many zeros at once, the way [J, D_K] = 0 covers CPT exactly rather than statistically. But note where the work lands: proving the *identification* (spectrum = zeros, exactly, no strays) is itself a pen-and-paper theorem. Nature can witness; it cannot notarize.

### What the universe CAN compute (the honest yes-pile)

- **The functional equation** — heat flow on a circle literally enacts ζ's reflection symmetry (theta-modularity). The mirror is physical.
- **ζ itself, as a partition function**: the *primon gas* (Julia, Spector; from memory) — a free boson gas with energy spectrum ε_p = log p has Z(β) = ζ(β) exactly, because multiset-of-primes occupancy IS unique factorization. The pole at β = 1 is a genuine Hagedorn catastrophe. In this language RH becomes a **Lee–Yang statement**: all complex-temperature zeros of the primon partition function lie on the critical line. Lee–Yang circle theorems prove exactly this *shape* of statement for ferromagnets via positivity — and Weil positivity in Connes–Consani is morally the arithmetic version of that missing positivity. But notice the fine print: you must feed the gas the primes by hand. The arithmetic input never comes for free.
- **The statistics**: GUE level repulsion is realized in actual quantum-chaotic systems all the time, and there are proposals/experiments (Berry–Keating xp regularizations, Bender–Brody–Müller 2017, Floquet trapped-ion schemes — all from-memory anchors, verify before any registry use) realizing the *low* zeros as resonances. Verification theater, but beautiful theater.

### The one genuinely computable thing here

There IS a well-posed, one-gate, this-repo-shaped question hiding in the idea: **does the substrate satisfy its own Riemann Hypothesis?** ζ_{D_K}(s) has a known pole structure (the dimension spectrum) but its **zeros** have never been an observable in 104 sessions; the undeformed case reduces to Hurwitz-zeta combinations that are analytically tractable. Pre-registerable expectation: **FAIL** — Epstein/Hurwitz-class zetas generically scatter zeros off their critical lines (Davenport–Heilbronn class). A FAIL would be a clean negative-space result with actual content: *RH-ness is not generic spectral behavior; it is the arithmetic fingerprint of unique factorization, which the fabric provably lacks.*

**The inversion.** Voronin's universality theorem (1975): in the strip 1/2 < Re s < 1, ζ approximates *any* non-vanishing holomorphic function to arbitrary precision, infinitely often. Any finite dataset — including, in principle, any finite description of this universe's spectral content — already appears inside ζ to any accuracy you like. So the relationship runs backwards: the universe doesn't compute ζ. **ζ computes universes.**

**Verdict, one line:** the universe is a witness, not a notary — brute-force cosmic computation dies on Π₁ (Mertens is the tombstone), the Hilbert–Pólya route is the right shape but needs a substrate whose arithmetic is ℚ's (adele class space, not SU(3) — wrong primes, wrong symmetry class, wrong Weyl law, two of three walls registry-PROVEN), and the most useful thing this framework can contribute to RH is taste in operators, and an honest FAIL showing that the critical line is where physics ends and arithmetic begins.

---

## Turn 3 — user

> ""universe as calculator" can verify RH to cosmic depth but can never prove it " I know; we're in this for hte love of the game; not the prize. Thanks for the write up; still reading it

## Turn 3 — orchestrator (reply)

Take your time with it. For what it's worth, "love of the game, not the prize" is the authentic lineage of this exact problem — Hilbert–Pólya was never published, just Pólya's offhand reply to a question over tea in Göttingen, and the Montgomery–Dyson GUE connection happened by accident in the Princeton tea room when Dyson recognized Montgomery's pair-correlation integral as one he knew from random matrices. The two load-bearing insights of the whole spectral-RH program were both tea-break conversations.

The bit most worth chewing on slowly is the mirror-and-pin decomposition — once you see that the functional equation is physics (heat flow) and the Euler product is arithmetic (primes), most of the spectral-RH literature snaps into a single sentence: everyone has the mirror, nobody has the pin.

---

## Turn 4 — user

> "ζ itself, as a partition function: the primon gas (Julia, Spector; from memory) — a free boson gas with energy spectrum ε_p = log p has Z(β) = ζ(β) exactly, because multiset-of-primes occupancy IS unique factorization. The pole at β = 1 is a genuine Hagedorn catastrophe. In this language RH becomes a Lee–Yang statement: all complex-temperature zeros of the primon partition function lie on the critical line. Lee–Yang circle theorems prove exactly this shape of statement for ferromagnets via positivity — and Weil positivity in Connes–Consani is morally the arithmetic version of that missing positivity. But notice the fine print: you must feed the gas the primes by hand. The arithmetic input never comes for free."
>
> Exactly when this got stuck in my brain, when we were doing early Zeta characterizations, and I turned my head slightly sideways and could almost see the hallway to infinity... (poetic; obviously hyperbole). I would like us to go ahead and do that quick test, just for my own sanity. Also - we do have a structure in our framework that is potentially infinte that I didn't see you evaluate above - the actual spectral action; our clinically monotonous effect that derailed entire sessions.

## Turn 5 — orchestrator (computation + final write-up)

[Process notes — methodology, fidelity-relevant:
1. Test design: exact closed form for the Dirac zeta of S³ = SU(2) (the substrate's exactly solvable little brother, same structural genre as ζ_{D_K}): spectrum |λ_k| = k + 3/2, multiplicity (k+1)(k+2). Substitution chain: m_k = (k+3/2)² − 1/4 ⇒ ζ_D(s) = ζ_H(s−2, 3/2) − (1/4)ζ_H(s, 3/2) ⇒ **F(s) = (2^(s−2)−1)ζ(s−2) − (2^(s−2)−1/4)ζ(s)**. Convention: single-power Conv. B, ζ_{|D|}(s) = Σ m_k |λ_k|^{−s}; poles at s = d−n, d=3, n ∈ {0,2} ⇒ pole set {3,1}, poleconv-B-single.
2. Controls under identical machinery: Riemann ζ(s); L(s,χ₋₃) = 3^{−s}(ζ_H(s,1/3) − ζ_H(s,2/3)). Control choice rationale: the full Epstein zeta of the hexagonal lattice x²+xy+y² equals 6·ζ(s)·L(s,χ₋₃) exactly, and the hexagonal lattice is SU(3)'s own root lattice (Eisenstein integers ℤ[ω], class number 1); substrate |μ+ρ|² values are (x²+xy+y²)/3 with x=p+1, y=q+1 ≥ 1.
3. Zero search: argument-principle winding counts on the window Re ∈ [−3.47, 4.53], Im ∈ [0.41, 36.13], with winding-certified bisection isolation and Muller polish at 35 dps. METHODOLOGY BUG CAUGHT AND FIXED mid-run: the first implementation sampled only edge corners before adaptive phase refinement — a full 2π wrap between corner samples is aliased away, silently undercounting zeros (Riemann control returned 0 zeros in a window provably containing 5, which exposed the bug). Fix: dense perimeter pre-sampling (step ≤ 0.2) before adaptive refinement. Post-fix, controls reproduce known zeros to 12 decimals.
4. Substrate data layer: Weyl counting N(λ) from the actual D_K cache `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (90 Peter-Weyl sectors, levels 0–12, τ_fold = 0.19; 78,080 per-branch block entries at L≤10 matching canonical lore; 166,896 at L≤12), fitted with and without the Peter-Weyl regular-representation weight dim(p,q).
5. Off-session discipline: underscore-prefixed helper script, canonical_constants tau_fold imported and asserted against cache filename, no verdict emission, no registry writes.]

### Script output (verbatim)

```
=== Closed-form verification (S^3 Dirac zeta) ===
  s =          5.0:  |direct sum - closed| = 1.38e-30
  s =          6.3:  |direct sum - closed| = 2.5e-14
  s =   (3.7 + 2.0j):  |Hurwitz combo - closed| = 5.27e-32
  s =  (0.3 + 14.0j):  |Hurwitz combo - closed| = 3.94e-31
  s =  (-1.2 + 5.0j):  |Hurwitz combo - closed| = 4.93e-32
  F( 0) = 0.0   [coefficient zero  <-> zeta_D(0)=0 odd-dim parity]
  F(-2) = 0.0   [double trivial zero]
  F(-4) = 0.0   [double trivial zero]
  F(-6) = 0.0   [double trivial zero]
  residue @ s=3: (1.0 + 0.0j) (expect 1);  @ s=1: (-0.25 + 0.0j) (expect -0.25)
  pole set {3, 1} = {d-0, d-2} at d=3, Conv. B  ->  a_0, a_2 only (odd-n vanish)

=== Complex-zero search, window Re in [-3.47, 4.53], Im in [0.41, 36.13] ===
  [S3_dirac] window [-3.47,4.53]x[0.41,36.13]: certified zero count Z = 3
  [S3_dirac] isolated + polished 3/3 zeros (2s elapsed, 2520 cumulative evals)
  [riemann] window [-3.47,4.53]x[0.41,36.13]: certified zero count Z = 5
  [riemann] isolated + polished 5/5 zeros (3s elapsed, 6236 cumulative evals)
  [L_chi3] window [-3.47,4.53]x[0.41,36.13]: certified zero count Z = 11
  [L_chi3] isolated + polished 11/11 zeros (13s elapsed, 12213 cumulative evals)

=== RESULTS ===

S^3 Dirac zeta (substrate-class, no Euler product): 3 complex zeros
    s = +3.106867127636 + 18.815991219014 i
    s = +2.438858496317 + 26.648379268666 i
    s = +3.369620969341 + 31.791921886511 i
  Re spread: [2.438858, 3.369621]  width = 0.930762
  max |Re - median Re| = 0.668009
  ON A COMMON VERTICAL LINE?  NO
  real-axis zeros found: [-8.0, -6.0, -4.0, -2.0, 0.0] (geometric/trivial family)

Riemann zeta (Euler product): 5 zeros, max |Re - 1/2| = 0.00e+00
    s = +0.500000000000 + 14.134725141735 i
    s = +0.500000000000 + 21.022039638772 i
    s = +0.500000000000 + 25.010857580146 i
    s = +0.500000000000 + 30.424876125860 i
    s = +0.500000000000 + 32.935061587739 i

L(s, chi_-3) (Euler product): 11 zeros, max |Re - 1/2| = 0.00e+00
    s = +0.500000000000 + 8.039737155681 i
    s = +0.500000000000 + 11.249206207773 i
    s = +0.500000000000 + 15.704619176722 i
    s = +0.500000000000 + 18.261997495693 i
    s = +0.500000000000 + 20.455770807742 i
    s = +0.500000000000 + 24.059414856493 i
    s = +0.500000000000 + 26.577868735775 i
    s = +0.500000000000 + 28.218164506233 i
    s = +0.500000000000 + 30.745040261382 i
    s = +0.500000000000 + 33.897388927259 i
    s = +0.500000000000 + 35.608412653939 i

  hexagonal-lattice Epstein zeta = 6 * zeta(s) * L(s,chi_-3): zeros = union of
  the two lists above -> ALL on Re = 1/2. SU(3) root lattice, full-lattice sum,
  Euler product intact. The chamber restriction + Weyl weights are what break it.

=== Substrate Weyl counting (L=12 cache @ tau_fold=0.19) ===
  eigenvalues loaded: 166896 block-level entries; zero modes excluded: 0
  fitted counting exponent, block-reduced:      N ~ lambda^5.022
  fitted counting exponent, Peter-Weyl weighted: N ~ lambda^7.817
  Riemann zeros count as N(T) = (T/2pi) log(T/2pi e) + 7/8  (slope -> 1, log-corrected)
```

### Final write-up (verbatim)

**Verdict: the substrate-class zeta fails its own Riemann Hypothesis — and the controls make the *why* sharper than expected.**

All zero counts are argument-principle certified. The machinery's credibility check: it reproduced the known Riemann zeros and the first eleven zeros of L(s,χ₋₃) to twelve decimals, every one at Re = 1/2 to machine zero. The substrate-class object came back with three complex zeros scattered across a band nearly a full unit wide — loitering near the ghost of ζ(s−2)'s shifted mirror at Re = 5/2 but pinned to nothing. Plus a real-axis "trivial family" at s = 0, −2, −4, −6, −8, all exactly zero, all purely geometric (heat-kernel parity — the s = 0 zero is the classic odd-dimension ζ_D(0) = 0). The pole set {3, 1} landed exactly on the a₀/a₂ dimension-spectrum reading, residues 1 and −1/4 on the nose. **Mirror without pin ⇒ zeros scatter.** RH-ness is not generic spectral behavior. It is the fingerprint of the primes.

**The control choice makes this brutal for the substrate, in the best way.** L(s,χ₋₃) wasn't arbitrary: the full Epstein zeta of the hexagonal lattice x²+xy+y² is *exactly* 6·ζ(s)·L(s,χ₋₃) — and the hexagonal lattice is **SU(3)'s own root lattice** (the Eisenstein integers ℤ[ω], class number 1). The substrate's |μ+ρ|² values literally live on this lattice: (x²+xy+y²)/3. So the substrate is *one step from arithmetic* — the unweighted full-lattice sum over its own root system has an Euler product and keeps every zero on the line. What destroys it is the physics: restricting to the dominant Weyl chamber and weighting by dim V_(p,q) — the Peter-Weyl multiplicities. The same degeneracy structure that makes the spectrum Poisson-integrable (Wall 1, CHAOS-1's ⟨r⟩ = 0.32–0.42) is what breaks the Euler product (Wall 2). Two walls, one root cause: representation theory is additive; the primes are multiplicative.

The real-cache layer confirmed Wall 3 from the actual D_K spectrum: counting exponent **7.82 ≈ 8** Peter-Weyl-weighted (the d=8 dimension spectrum, with the small deficit being the L_max truncation bend) and 5.02 block-reduced — polynomial either way, versus the zeros' T·log T.

**The spectral action — the user is right, and it's better than "a candidate."** The spectral action is the framework's one genuinely infinite structure, and: **Tr f(D/Λ) is already a trace formula, and Weil's explicit formula — the master identity of RH — is also a trace formula. They have the same anatomy.** The Mellin representation the framework uses daily — spectral action = sum over ζ_D's poles giving the Λ^(d−n)·a_n expansion — is the "archimedean side." What's left over, the oscillatory remainder beyond all the Seeley-DeWitt terms, localizes on the **closed geodesics** of the substrate (Poisson summation / wave-trace). Weil's formula has the identical decomposition: Γ-factor and pole terms (archimedean side) + a sum over primes weighted by log p (geometric side) = a sum over the zeros (spectral side). The dictionary is exact: ζ_D poles ↔ Γ-terms, eigenvalues ↔ zeros, closed geodesics ↔ primes. And Connes' RH criterion is literally a positivity statement about this object: RH ⟺ a Weil quadratic trace-functional is ≥ 0 on the right test class — *a spectral-action positivity*. The "clinically monotonous effect" — the S36 bare-action monotonicity — is structurally a baby version of exactly that missing positivity: a proven sign-definiteness of a trace functional under deformation. Right theorem-shape. Wrong space. (Tagged honestly: a structural analogy, organizational insight only — not evidence.)

The deciding axis isn't infinity — the spectral action's infinity is real but **crystalline**. It's the *length spectrum of the geometric side*:

- **Substrate (SU(3))**: closed-geodesic lengths form a commensurable lattice. The oscillations reorganize into theta functions and resolve smoothly — monotonicity is the *signature of the absence of arithmetic*. Nothing in SU(3) beats against anything else irrationally.
- **Riemann side**: the "lengths" are {log p}, ℚ-linearly independent — maximally incommensurable. The oscillations never resolve; that's why π(x) − Li(x) flips sign infinitely often (Littlewood) while the spectral action marches monotonically.
- **The proven middle case**: hyperbolic surfaces, where geodesic lengths are incommensurable logs of algebraic units → an honest Euler product over geodesics → the Selberg zeta, whose RH is a *theorem* because the Laplacian realizes its zeros.

Which yields the one-line answer to "could our spectral action host RH": it already hosts an explicit formula — the only question is ever *whose lengths sit on the geometric side*. To make them Riemann's, the orbit lengths must be {log p}, and that is precisely Connes' adele class space, where each prime is a **place** and its periodic orbit has length log p. In substrate-IS language: **RH's substrate must have the primes as its fibers, not as its phonons.**

**About the hallway.** The critical line does not exist at any finite truncation — partial sums of ζ itself have scattered off-line zeros, and truncated Euler products have *no* zeros at all; the line is an emergent object of the completed limit, exactly the way the framework's dimension-spectrum poles only exist at L_max → ∞. The hallway is infinitely long by construction — the pin lives only at the far end, and the far end is made of primes.

[Offered, not queued: a full-strength one-gate version — zeros of the actual Jensen-deformed ζ_{D_K} via hybrid heat-kernel continuation of the L=12 cache, certified window, pre-registered "common vertical line" criterion.]

---

## Known caveats carried by this transcript (for the reviewer)

1. Literature anchors (Berry–Keating, Montgomery–Odlyzko, Lagarias 2002, Odlyzko–te Riele 1985, Platt–Trudgian, Lloyd bound, Julia/Spector primon gas, Voronin 1975, Etesi–Németi 2002, Bender–Brody–Müller 2017, Davenport–Heilbronn 1936, Fegan/Bär sphere spectra) are **from-memory anchors, not fetched sources** — flagged as such in-conversation per `feedback_research-corpus`. None entered any register.
2. The S³ Dirac spectrum (|λ| = k+3/2, mult (k+1)(k+2)) is textbook-standard but cited from memory; the closed-form reduction was verified numerically at 10⁻³⁰ (integer point) and 10⁻³¹ (complex points, Hurwitz level).
3. The claim "spectral action oscillatory remainder localizes on closed geodesics" (Duistermaat–Guillemin / wave-trace) and "SU(3) closed-geodesic lengths are commensurable" are structural assertions from memory, not computed in-session.
4. The Weyl-slope fit window is quantile-based (20th–70th percentile) on a truncated cache; the 7.82-vs-8 deficit is attributed to the L_max truncation bend without a dedicated convergence study.
5. The zero search window is finite (Im ≤ 36.13); "fails its own RH" is certified within the window only — three scattered zeros suffice for the structural conclusion, but the asymptotic zero distribution of F(s) was not characterized.
6. CHAOS-1 statistics and BDI/block-diagonality/dimension-spectrum claims were cited from the knowledge MCP and rules files as registry-authoritative; per `/rclab-review` rules they are not re-adjudicated here.
