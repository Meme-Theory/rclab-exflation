# Sub-A3 — Torsion-from-Spinor (ECSK) vs the Framework's Dirac Operator: An Adversarial Adjudication

**Author**: Workhorse-Antimatter (`dirac-antimatter-theorist`)
**Parent**: Lead A (`hawking-theorist`), BH-Cosmology ↔ Exflation incursion
**Date**: 2026-06-13
**Mandate**: FALSIFICATION-first. Hunt tension, no-analogs, and places the ECSK/Poplawski literature is more rigorous than the framework. Substrate-first per `phononic-framing.md`, but NOT a mandate to conclude everything is a shadow of the substrate.

**Sources read in full (no training-knowledge citations)**:
- Poplawski, *Cosmology with Torsion: an Alternative to Cosmic Inflation*, PLB 694 (2010) 181 — arXiv:1007.0587 [read].
- Poplawski, *Nonsingular, Big-Bounce Cosmology from Spinor-Torsion Coupling*, PRD 85 (2012) 107502 — arXiv:1111.4595 [read].
- Poplawski, *Gravitational Collapse with Torsion and Universe in a Black Hole*, IJMPA 40 (2025) 2544007 — arXiv:2509.11468 [read].
- Framework: `sessions/session-plan/archive/session-26-preplan-3_2.md` (Gate T-1 torsion analysis, full); `sessions/framework/Collabs/equation-build/baptista-operator-dk-tau.md` (E1/E2/E8 construction); `.claude/agent-memory/dirac-antimatter-theorist/proofs-and-theorems.md` (T1–T11); knowledge-MCP (`[J,D_K]=0` PROVEN; `tau_fold`=0.190; Ordered Veil R_therm=5251.82, S_ent=0; torsion gates S26/27/45/46/52/85).

> **Notation.** Poplawski uses Greek/Latin curved-spacetime indices on a 4D Lorentzian manifold; torsion `S^k_{ij}`, contortion `C^k_{ij}`, spin tensor `s^{ijk}`, gravitational coupling `κ = 8πG/c⁴`. The framework uses an 8-frame `{e_a}_{a=0..7}` on the internal fiber `K = SU(3)`, Euclidean fiber gammas `{γ_a}`, Levi-Civita spin connection `Ω_LC(τ)`, structure constants `f_{abc}(τ)`. I keep both notations and flag every place the *index space itself* is the disanalogy.

---

## 0. Executive summary (read this first)

Poplawski's entire UIBH (universe-in-a-black-hole) program rests on **one degree of freedom**: spacetime **torsion** `S^k_{ij}`, made dynamical by Einstein–Cartan–Sciama–Kibble (ECSK) gravity and sourced **algebraically by the intrinsic spin of Dirac fermions**. The Cartan equation `S_{jik} − S_i g_{jk} + S_k g_{ji} = −½κ s_{ikj}` (1007.0587 eq 3; 2509.11468 §1) is the load-bearing relation: torsion is *proportional to spin density*, vanishes in vacuum, and produces a quartic spin-spin contact term that gives an effective energy density `ε_S = −¼κs² ∝ a⁻⁶` (1007.0587 eq 15). That negative density drives the nonsingular bounce, the flatness/horizon resolution, an effective fermionic UV cutoff, and the arrow of time.

The framework's fundamental object is the Dirac operator `D_K(τ)` on Jensen-deformed `SU(3)`, built from the **Levi-Civita (torsion-FREE) spin connection** `Ω_LC(τ)` (baptista E2). 

The central result of this adjudication is a **structural NO-ANALOG with a sharp twist**:

1. The framework IS torsion-free *as a matter of construction* of its physical operator `D_K`. **BUT** the framework is not naive about torsion: it has explicitly built the torsion-modified operator `D_T = D_K + ¼ ΔK_{abc} γ^a γ^b γ^c` and tested it (Gate T-1, S26–27). The framework therefore *knows what torsion would do* and has a structural theorem about it.

2. **The decisive disanalogy is not "no torsion" — it is "no Cartan equation."** Poplawski's torsion is a *dynamical response to fermion spin density* (`S ∝ s`). The framework's would-be torsion (the Schouten/contorsion term that distinguishes `Ω_LC` from the flat connection) is a *fixed geometric datum of the group manifold* — set by the structure constants `f_{abc}(τ)`, NOT by any matter spin density. There is **no equation in the framework where fermion occupation sources the connection's antisymmetric part.** The framework's `D_K` has spin (it acts on spinors) but spin does *not* back-react on the geometry the way ECSK demands. Severity: **HIGH** as a no-analog; **LOW** as a defect (it is a deliberate, theorem-backed design choice, and the physical work torsion does in ECSK is done by a different, independently-verified mechanism in the framework).

3. The two singularity-avoidance mechanisms are **genuinely different physics**, and the framework's is **MORE robust on one axis, LESS economical on another**. Poplawski's bounce is *not* unconditionally robust — it requires Parker quantum particle production during contraction to keep `n_f² ∝ a⁻⁶⁻²δ` outrunning the shear `σ² ∝ a⁻⁶` (2509.11468 §4), and it requires a *specific matter content* (fermions) and a *specific gravity theory* (ECSK). The framework's avoidance is geometric/spectral (`λ² ≥ R_K(τ)/4 > 0` Lichnerowicz, gap never closes) and is *independent of matter content and shear*. But the framework pays for this with a far heavier ontological commitment (an entire NCG spectral triple), where ECSK adds *zero free parameters* to GR.

4. **The sharpest tension is the arrow of time (part d).** Poplawski's cosmic arrow is a **T-asymmetric boundary condition** imposed on a **T-symmetric** theory (ECSK is T-symmetric; the arrow comes from unidirectional matter flow through the parent horizon — 1007.0587 §VII). The framework is **CPT-EXACT at the operator level** (`[J, D_K] = 0`, PROVEN, T1/T11) and derives its arrow from the **irreversibility of the diabatic transit** (Ordered Veil, S_ent = 0, R_therm = 5252). These are *compatible in principle* — CPT-exactness of the microscopic operator does not forbid a T-asymmetric boundary/initial condition; this is standard (the SM is CPT-exact yet the universe has an arrow). **But the framework does NOT get to keep both stories without cost**: if the arrow is purely a transit boundary condition (Poplawski-style), then the much-advertised "[J,D_K]=0 hardwires CPT" is *silent on cosmology* — it constrains the spectrum, not the boundary data. That is a real scoping tension, examined in §5.

**Top-line strength of the four claimed correspondences** (my ratings, defended below):
| Correspondence | Strength | One-line |
|:---|:---|:---|
| (a) torsion DOF ↔ framework connection | **NO-ANALOG (HIGH severity)** | No Cartan equation; spin does not source the connection |
| (b) bounce ↔ transit | **WEAK analog / strong contrast** | Both avoid singularity, for unrelated reasons; framework more robust, less economical |
| (c) torsion-UV-cutoff ↔ M_KK / spectral cutoff | **COINCIDENCE-dominated (WEAK)** | Both "have a UV scale"; mechanisms ontologically disjoint |
| (d) torsion arrow ↔ Ordered-Veil arrow | **COMPATIBLE but exposes a scoping tension** | CPT-exact ≠ arrow-forbidding; but then [J,D_K]=0 is cosmologically silent |

---

## 1. Governing structures, side by side (structure-first)

### 1.1 The ECSK / Poplawski governing structure

Einstein–Cartan–Sciama–Kibble gravity is GR with the affine connection's antisymmetry restored. The affine connection (2509.11468 §1; 1007.0587 eq 2):

```
Γ^k_{ij} = {k_ij} + S^k_{ij} + S_{ij}{}^k + S_{ji}{}^k          (Riemann–Cartan connection)
```

where `{k_ij}` are the Christoffel symbols (metric, symmetric) and `S^k_{ij} = ½(Γ^k_{ij} − Γ^k_{ji})` is the **torsion tensor** — the antisymmetric part, now a dynamical field. Two variations:

- **Vary w.r.t. contortion `C^k_{ij}`** → the **Cartan equations** (algebraic, NOT differential):
  ```
  S_{jik} − S_i g_{jk} + S_k g_{ji} = −½ κ s_{ikj}              (1007.0587 eq 3)
  ```
  with `s^{ijk} = 2(δL_m/δC_{ijk})/√−g` the **spin tensor of matter**. *Torsion = (κ/2) × spin density.* It does not propagate; it vanishes wherever fermions are absent.

- **Vary w.r.t. metric `g_{ij}`** → Einstein equations with spin-squared corrections:
  ```
  G_{ik} = κ T_{ik} + κ²·U_{ik}(s²),  U_{ik} quadratic in the spin tensor   (1007.0587 eq 5; 1111.4595 eq 2)
  ```

For a Dirac field the spin tensor is **totally antisymmetric**, `s^{ijk} = −e^{ijkl} s_l` with `s_i = ½ ψ̄ γ_i γ_5 ψ` the Dirac spin pseudovector (1111.4595 eq 4). Substituting Cartan into the Dirac equation gives the **Hehl–Datta equation**:
```
i γ^k ψ_{:k} = m ψ − (3/8) κ (ψ̄ γ^k γ_5 ψ) γ_k γ_5 ψ          (1111.4595, after eq 5)
```
— a nonlinear (cubic) Dirac equation with an *attractive-or-repulsive quartic self-interaction*. The averaged effective fluid (no spin polarization) is (1007.0587 eq 8–10; 2509.11468 eq 1):
```
ε̃ = ε − α n_f²,    p̃ = p − α n_f²,    α = κ(ℏc)²/32 > 0
ε_S = −¼ κ s² ∝ a⁻⁶  (decouples from ε; same scaling for any w)    (1007.0587 eq 15)
```

**The whole program lives or dies on `ε_S < 0 ∝ a⁻⁶`.** This is the gravitational-repulsion term: at high `n_f`, `ε̃` can pass through zero and the Friedmann equation `ȧ² = (κ/3)(ε − αn_f²)a² − 1` forces `ȧ = 0` at a finite minimum `a_cr` (1111.4595 eq 16–17). Singularity replaced by a cusp-like bounce.

### 1.2 The framework's governing structure

The framework is a **finite spectral triple** `(A_F, H_F, D_K(τ))` tensored with `M⁴` (baptista §2.2). The operator (E2):

```
D_K(τ) = Σ_{a=0}^7 ρ(e_a) ⊗ γ_a  +  I ⊗ Ω_LC(τ)                  (E2)
              \_____transport_____/      \__Levi-Civita spin connection__/
```

- `ρ(e_a)` = left-invariant vector field (Lie derivative) on Peter–Weyl modes;
- `Ω_LC(τ) = Σ_{j<k<l} α_{jkl} γ_j γ_k γ_l`, with `α_{jkl}` fixed by the Jensen metric `g_τ` (E1) and the `su(3)` bracket (Baptista Paper #14 eq 3.8).

**The connection is Levi-Civita — torsion-free by definition.** The single dynamical degree of freedom is the scalar Jensen modulus `τ` (volume-preserving TT deformation, baptista §2.1). Singularity avoidance comes from the Lichnerowicz–Bochner identity (E5):
```
D_K² = ∇*∇ + ¼ R_K(τ),    R_K(τ) = −¼e⁻⁴ᵗ + 2e⁻ᵗ − ¼ + ½e²ᵗ > 0  ∀τ ≥ 0   (E3)
⟹  λ² ≥ ¼ R_K(τ) > 0,  gap never closes,  spectral flow = 0,  η(τ) constant   (E5)
```
The cosmogenesis is a **first-order phase transition** ("the fold") at `τ_fold = 0.190`: a supersonic (Mach 13.75) diabatic transit through the van Hove cusp of the density of states. No metric ever degenerates; the *spectrum* reorganizes. CPT is hardwired: `[J, D_K(τ)] = 0` for all τ (E8; T1; T11 extends to all 36 left-invariant moduli).

### 1.3 The structural collision, stated precisely

| Axis | Poplawski / ECSK | Framework |
|:---|:---|:---|
| Fundamental object | metric `g` + torsion `S` on 4D Lorentzian `M` | spectral triple `(A_F, H_F, D_K)`; `D_K` encodes metric *and* connection spectrally |
| Connection | Riemann–Cartan (torsionful), `S` dynamical | Levi-Civita (torsion-FREE) on `SU(3)` fiber |
| Source of the antisymmetric connection part | **Dirac spin density**, via Cartan eq `S ∝ s` | **structure constants** `f_{abc}(τ)`; NO matter source |
| Free parameters | **zero** beyond GR (G, c set units) | one geometric modulus `τ` (then theorem-pinned to `τ_fold`) |
| Singularity avoidance | torsion repulsion `ε_S ∝ a⁻⁶` at high `n_f` | Lichnerowicz gap `λ² ≥ R_K/4 > 0`; first-order transit |
| Index space of the spinor | 4D Lorentzian Dirac spinor | internal `SU(3)`-fiber spinor `Δ_8`; 16-dim per generation |
| Arrow of time | T-asymmetric **boundary condition** (T-symmetric bulk) | transit irreversibility (Ordered Veil); CPT-exact operator |

The collision is real and it is at the *level of what sources geometry*. I now adjudicate the four sub-questions.

---

## 2. (a) NO-ANALOG TEST — does `D_K` carry, or have room for, a spin-sourced torsion?

### 2.1 The literal question: is `D_K` Levi-Civita by construction?

**Yes, exactly and provably.** E2 writes `D_K = Σ ρ(e_a)⊗γ_a + I⊗Ω_LC(τ)` with `Ω_LC` the *Levi-Civita* spin connection (baptista §2.2.1, item 2). The framework's own torsion analysis (session-26-preplan-3_2 §1.1–1.2) is explicit: the standard `D̸_K` "is built from the Levi-Civita connection `∇^LC`" and satisfies the torsion-free Lichnerowicz formula `D̸² = ∇*∇ + R_g/4`. So at the level of the *physical operator that generates all observables*, the framework has zero torsion.

### 2.2 But the framework is not torsion-blind — it built `D_T`

This is where a naive "no-analog, done" verdict would be wrong, and where I correct the prompt's framing. The framework has an explicit torsion-modified Dirac operator (session-26-preplan-3_2 §1.3, §2.1; knowledge-MCP `D_T = D_K + I⊗Ω_T`):
```
D̸_T = D̸_K + ¼ ΔK_{abc} γ^a γ^b γ^c                     (session-26 eq, §1.3)
```
where `ΔK_{abc}` is the contortion taking Levi-Civita → the flat **Schouten** connection `∇⁰` (which has torsion `T⁰(u^L,v^L) = [u,v]^L`). Baptista Paper #14 (lines 1734–40) proves that the Schouten–Dirac operator `D̸_0 = Σ_j γ^j L_{e_j^L}` has its cubic coefficients vanish identically: `D̸_K = D̸_0 + Ω·` where `Ω·` is the Clifford action of the 3-form `Ω_{jkl}(τ)`.

The framework ran **Gate T-1**: does *any* natural torsionful connection on `SU(3)` lower the Dirac spectral gap below `D̸_K`? The structural verdict (session-26 §5.2, Theorem):
```
On a compact spin manifold with R > 0, for totally antisymmetric torsion T:
    λ_T² ≥ R/4 + c‖T‖² − C‖dT‖_op,    c > 0  (Bismut–Friedrich–Agricola)
⟹  totally antisymmetric torsion STRENGTHENS the gap (Bismut connection: min|λ_B| > min|λ_K|).
```
The only gap-*weakening* channel is the non-totally-antisymmetric remainder `T^(rest)`, which vanishes at τ=0 and reaches only ~27% of the antisymmetric part at τ=0.25, dominated ~5:1 by the positive `c‖T‖²` term (session-26 §5.3). The full Schouten limit DESTROYS the gap (zero eigenvalue on the (0,0) singlet — `M_0^{(0,0)} = 0` because left-regular action is trivial on constants, session-26 §3.6). P(T-1 PASS) was rated 5–10%, P(CLOSED) 80–85%.

**So the framework's relationship to torsion is: it is torsion-free by construction, it knows the torsion-modified operator exactly, and it has a structural theorem that torsion does NOT open the channel it would need to (gap-weakening) for the only physically natural choices.**

### 2.3 The DECISIVE disanalogy: there is no Cartan equation

Here is the sharp point, and it is sharper than "the framework has no torsion."

In ECSK, torsion is **not a free geometric choice** — it is *forced by matter spin* through the Cartan equation `S_{jik} = −½κ s_{ikj} + (trace terms)`. The torsion is a **dynamical response**: change the fermion configuration, the connection's antisymmetric part changes. This back-reaction is the entire mechanism.

In the framework, the would-be torsion (the Schouten contorsion `ΔK_{abc}`, or any added `T_{abc}`) is **a fixed datum of the group geometry**:
```
T⁰_{abc}(τ) = f_{abc}(τ) = g_τ([e_a,e_b], e_c) = (σ_c/σ_a σ_b) f̄_{abc}     (session-26 §2.1, §3.2)
```
— it is the *structure constants of `su(3)` rescaled by the Jensen factors `σ_a`*. **There is no spin density `s^{ijk}` anywhere in this expression.** The fermions live in `H_F`; they are acted on *by* `D_K`; they do not *source* the connection inside `D_K`. There is no variational principle `δL/δC = s` in the framework's construction. The spin connection `Ω_LC(τ)` is determined by `τ` alone (E2), and `τ` is fixed by the spectral-action gradient and the van Hove cusp — *not* by fermion occupation.

**Substrate-first reading.** In the substrate picture the explanatory arrow is `D_K eigenvalues → spectral moments → emergent geometry → matter`. ECSK runs an arrow the framework structurally forbids: `matter spin → torsion → geometry`. For the framework, matter (relay-pattern excitations) is *downstream* of the geometry; it cannot reach back and source the connection. Poplawski's mechanism requires the *opposite* causal direction at the most fundamental level. **This is the container-thinking inversion `phononic-framing.md` warns against, made concrete: ECSK is a theory in which matter-IN-spacetime sources the geometry; the framework is a theory in which geometry IS the substrate and matter is its excitation.** The two cannot both be fundamental.

### 2.4 Could the framework be retrofitted with a Cartan equation?

Honest examination of "room for torsion sourced by spin":

- **The spectral action does generate a torsion-like term — but in the BOSONIC sector, not as a spin response.** Baptista Paper #15 (line 3127, quoted in session-26 §4.3) suggests "connections with torsion in the internal directions" would add a `+‖T‖²` term to the effective Ricci scalar, modifying the bosonic *potential*. This is a *geometric* modification of `V(τ)`, NOT a Cartan-equation back-reaction of fermion spin. It is the wrong kind of object for Poplawski's mechanism.

- **The fermionic action `⟨Jψ, D_K ψ⟩` (Connes' form, ref-doc 12) does contain a quartic-fermion term under inner fluctuations** — the spectral action's fermionic doubling and the Higgs quartic are present. But this quartic is the *electroweak / Yukawa* structure, fixed by the geometry; it is not `−¼κs²` sourced by a Cartan equation, and it does not scale as `a⁻⁶` in any cosmological sense. (The framework's quartic-fermion physics is the `B2`-sector BCS condensate, knowledge-MCP; same-sign `K_7` pairing within the EW-doublet sector — a thermodynamic condensate, not a torsion contact term.)

- **A genuine ECSK retrofit would require promoting the connection's antisymmetric part to a dynamical field with `δL/δC = s`.** That is a *different theory* — it would break the single-modulus structure (`τ` alone determines `Ω_LC`), and it would have to be checked against `[J, D_K] = 0`, which currently holds *because* `D_K` is built from real structure constants and the Levi-Civita connection (T11 proof: `C₂ conj(Ω) C₂ = −Ω` uses reality of `Γ^b_{ac}`). A spin-sourced complex/non-real torsion is not guaranteed to preserve CPT. **This is itself a constraint: any attempt to add ECSK torsion to the framework must pass the `[J,D_K]=0` test, and the T11 proof does not obviously extend to a spin-sourced torsion.**

### 2.5 Strength rating: (a) is a STRUCTURAL NO-ANALOG, HIGH severity as a tension

- **As a no-analog**: HIGH. The single degree of freedom doing *all the work* in Poplawski's program — dynamical, spin-sourced torsion — has **no counterpart** in the framework. The framework's connection is Levi-Civita; its only "torsion" is a fixed geometric datum with no matter source. There is no Cartan equation. This is the sharpest of the four findings and a candidate for the campaign's sharpest tension.

- **As a defect of the framework**: LOW-to-MODERATE. It is a *deliberate, theorem-backed* design (Gate T-1: torsion doesn't open the gap-weakening channel; the physical work torsion does in ECSK — singularity avoidance — is done by the independently-proven Lichnerowicz gap). It is not an oversight. But it does mean the framework cannot borrow *any* of Poplawski's results: the torsion bounce, the torsion UV cutoff, the spin-sourced baryon physics are all simply *unavailable* to the framework. Where Poplawski gets cosmological mileage "for free" from a DOF GR already implicitly suppresses, the framework must earn each result from spectral geometry.

> **Throughline T-A3-1**: *ECSK torsion is the laboratory-IN shadow of nothing in the substrate.* It is the one major mechanism in this corpus with **no substrate-IS pre-image**. The framework's connection is rigid (Levi-Civita, fixed by `τ`); ECSK's is fluid (sourced by spin). This is a clean falsification-of-correspondence, not a correspondence.

---

## 3. (b) THE BOUNCE-AVOIDANCE COMPARISON — more or less fundamental?

### 3.1 The two mechanisms are unrelated physics

| | Poplawski bounce | Framework transit |
|:---|:---|:---|
| What stops the collapse | torsion repulsion: `ε_S = −¼κs² ∝ a⁻⁶` overwhelms `ε ∝ a⁻⁴` at small `a` | nothing "stops" anything — there is no collapse; the modulus `τ` flows through a first-order transition |
| Mathematical signature | turning point `ȧ = 0` at finite `a_cr` (1111.4595 eq 17); cusp | van Hove cusp in DOS at `τ_fold`; supersonic Mach-13.75 transit |
| Requires | fermions (spin fluid), ECSK gravity, `n_f` high enough | only the Jensen geometry; `λ² ≥ R_K/4 > 0` is matter-independent |
| Singularity status | curvature singularity averted; `a ≥ a_cr > 0` | **no singularity ever forms** — the metric never degenerates; only the spectrum reorganizes |

These are not two versions of one idea. Poplawski has a *contracting FLRW universe that turns around*. The framework has *no contraction and no scale factor turnaround at the fundamental level* — it has a scalar modulus sliding down a spectral-action gradient through a phase transition. The word "bounce" maps onto "transit" only at the loosest narrative level ("both avoid the Big Bang singularity").

### 3.2 Robustness — Poplawski's bounce is CONDITIONAL; the framework's is not

This is the part the prompt asks me to adjudicate, and the 2025 paper (2509.11468 §4) is decisive *against* Poplawski's robustness:

> "The presence of shear opposes the effects of torsion. The shear scalar `σ²` grows with decreasing `a` like `~a⁻⁶`, like `n_f²`. Therefore, if the initial shear term dominates over the initial torsion term, then it will dominate at later times during contraction, and a singularity would form. To avoid it, `n_f²` must grow faster than `~a⁻⁶`. Consequently, fermions must be produced in a black hole during contraction."

So the torsion bounce is **NOT unconditionally singularity-free**. Torsion `ε_S ∝ a⁻⁶` scales *identically* to shear `σ² ∝ a⁻⁶`; whichever is larger initially wins. To rescue the bounce, Poplawski invokes **quantum particle production** (Parker, eq 19: `d(√−g n_f)/dτ ∝ βH⁴`) to make `n_f² ∝ a⁻⁶⁻²δ` with `δ > 0` during contraction, outrunning shear. The bounce is therefore *contingent* on: (i) the right matter content (Dirac fermions), (ii) ECSK, (iii) sufficient initial torsion-vs-shear ratio, AND (iv) an active particle-production channel during collapse.

The framework's `λ² ≥ R_K(τ)/4 > 0` is a **theorem about the geometry** (Lichnerowicz–Bochner on a positively curved fiber, E5). It holds:
- for **any** matter content (it's a statement about `D_K`, not about `H_F` occupation);
- with **no** shear-vs-source competition (there is no anisotropic shear degree of freedom competing with it — the relevant object is the curvature `R_K(τ)`, monotone-increasing for τ>0, E3);
- with **zero** dependence on particle production (the gap is set by the spectrum, not by `n_f`).

**On the robustness axis, the framework's avoidance is MORE fundamental and MORE robust.** It is a structural inevitability of the geometry, not a contingent outcome of a matter-vs-shear race that needs a quantum-production lifeline.

### 3.3 Economy — Poplawski wins decisively

The counter-rating, in the framework's disfavor (FALSIFICATION mandate — I must report where GR is more rigorous/economical):

**ECSK adds ZERO free parameters to GR.** Poplawski repeatedly stresses this (1007.0587 §VII: "the ECKS gravity does not contain free parameters (G and c can always be set to 1)"). The torsion is *forced* by the Poincaré gauge structure — it is the minimal, almost-inevitable completion of GR once you take seriously that fermions carry spin and spin is the Noether current of local Lorentz rotations. The bounce then follows *with no tuning*. The flatness/horizon resolution follows from a *derived* (not assumed) `Ω_S ≈ −10⁻⁶⁹` (1007.0587 eq 23), which itself comes from the weakness of the spinor-torsion coupling — again no tuning.

The framework, to avoid its singularity, posits an **entire NCG spectral triple on `SU(3)`**: the algebra `ℂ⊕ℍ⊕M₃(ℂ)`, the Jensen TT-deformation, the volume-preservation constraint, the choice of `SU(3)` itself. That is a *vastly* heavier set of structural commitments. Even granting that `τ` is "one number," the *machine that turns the number into physics* is enormous compared to "restore the antisymmetric part of the connection."

**Verdict on (b)**: 
- **Robustness**: framework MORE fundamental (theorem vs contingent matter-race). 
- **Economy / minimality**: Poplawski MORE fundamental (zero new parameters vs a full spectral triple).
- These are different virtues. A fair adjudication does not crown a single winner; it says the framework buys robustness with ontology, and ECSK buys economy with a contingent bounce.

### 3.4 Can the transit be RE-READ as a torsion bounce? — NO, and the inversion is forbidden

The prompt asks whether the framework's transit could be re-read as an effective torsion bounce. Running the `c-compare` logic (the deterministic classifier the campaign uses for "is a feature substrate-dynamics or propagation"):

- Poplawski's bounce is a feature of `a(τ)` — the FLRW scale factor — which is a **propagation-sector / emergent-geometry** object (it lives on the emergent `g_M`).
- The framework's transit is the flow of the Jensen modulus `τ` — a **SUBSTRATE-DYNAMICS** object (it IS the substrate reorganizing; it is not c-bounded; `dτ/dt = 6.67 M_KK` gives Mach 13.75, supersonic *because* it is not a propagation on `g_M`).

To "re-read the transit as a torsion bounce" you would have to map a substrate-dynamics object onto an emergent-geometry object, i.e. treat the substrate's internal flow as if it were a scale-factor turnaround *inside* an emergent spacetime. **That is precisely the container-thinking inversion `phononic-framing.md` forbids**: it makes the emergent `a(t)` fundamental and the substrate derivative. CONTRADICTION class. The re-reading is not just unmotivated — it inverts the substrate-first arrow.

> **Throughline T-A3-2**: *The torsion bounce is the laboratory-IN shadow of the substrate transit ONLY at the coarsest level ("no singularity").* At the mechanism level they are disjoint: torsion repulsion (matter-sourced, shear-contingent, scale-factor turnaround) vs Lichnerowicz-rigid spectral transit (matter-independent, shear-free, modulus flow). Strength of the correspondence: **WEAK** — shared conclusion, unrelated mechanism. The framework's version is more robust; ECSK's is more economical.

---

## 4. (c) THE Dirac-SEA / UV-CUTOFF POINT — genuine analog or cheap coincidence?

### 4.1 What Poplawski actually claims

Poplawski cites (1007.0587 §I; PLB 690, 73, ref [21]; reiterated 2509.11468 §5): ECSK torsion "introduces an effective ultraviolet cutoff in quantum field theory for fermions," and (2509.11468 §5) "torsion may also remove divergences in Feynman diagrams in quantum electrodynamics, resulting in finite values of bare (before renormalization) quantities such as the mass and electric charge of the electron." The mechanism is the **quartic spin-spin contact term** in the Hehl–Datta equation: `−(3/8)κ(ψ̄γ^kγ_5ψ)γ_kγ_5ψ`. This term is repulsive at short distance for the relevant configuration, so two fermions cannot be localized below a torsion-set length scale `ℓ_tor ~ (κ)^{1/2} × (spin density)^{...}` — effectively a minimum length / UV regulator *for fermions specifically*, sourced by their own spin.

### 4.2 What the framework's UV scale is

The framework's UV scale `M_KK` is the Kaluza–Klein mass scale — the inverse size of the `SU(3)` fiber, equivalently the spacing of the `D_K` eigenvalue ladder. The spectral action `S = Tr f(D_K²/Λ²)` is regulated by the **cutoff function `f` acting on the `D_K` spectrum** (ref-doc 28; baptista §2.2.2). The "UV completion" is that the eigenvalue spectrum is discrete and the spectral moments `a_0, a_2, a_4` are the only surviving terms in the asymptotic expansion — gravity, Yang–Mills, Higgs all emerge from a *finite* number of spectral moments. There is no continuum of arbitrarily-high-momentum fermion modes below the KK scale.

### 4.3 Are these the same thing? — NO. The shared feature is "a UV scale," which is cheap.

Be skeptical, per the prompt. Two theories both having a UV scale is not a correspondence; *every* sensible quantum-gravity-adjacent proposal has one. The relevant question is whether the *mechanism* and the *object being cut off* match. They do not:

| | Poplawski torsion-UV-cutoff | Framework `M_KK` / spectral cutoff |
|:---|:---|:---|
| What is regulated | **fermion** propagators specifically (the spin-spin contact term acts on Dirac fields) | the **entire** spectral action — bosons and fermions alike, via `f(D_K²/Λ²)` |
| Source of the scale | dynamical: fermion spin density, via `−κs²` (Cartan) | kinematic/geometric: the size of `SU(3)`, fixed by the geometry |
| Density dependence | the cutoff *moves with `n_f`* — it is sharp only at extreme density (Cartan density ~`m_P⁴`) | the cutoff is a *fixed* geometric scale, density-independent |
| Mechanism class | nonlinear self-interaction (a contact term) | discreteness of a Laplace-type spectrum on a compact manifold |
| Vacuum behavior | torsion (hence the cutoff) **vanishes in vacuum** (no fermions ⟹ no torsion ⟹ no cutoff) | the spectral gap and `M_KK` persist in vacuum (they are geometry) |

The last row is the killer. Poplawski's UV cutoff is a **matter effect** — it literally switches off where there are no fermions. The framework's `M_KK` is a **geometric constant** that is there whether or not anything is excited. A regulator that vanishes in vacuum and a regulator that is a fixed property of the vacuum geometry are *opposite kinds of object*.

### 4.4 The one place there is a faint, real resonance — and it is faint

There is a *partial*, honest resonance worth recording: in both pictures, **fermion physics is finite without ad-hoc renormalization counterterms**, and in both, a *geometric/algebraic* structure (torsion contact term ↔ discrete `D_K` spectrum) is responsible rather than a subtraction scheme. The framework's spectral action is finite by construction (the heat-kernel expansion terminates at the physical moments); Poplawski's QED is claimed finite because torsion caps the short-distance behavior. Both are "finiteness from geometry, not from subtraction."

But this resonance is *structural-aesthetic*, not mechanistic. The framework does not need torsion to be finite (it's finite because the spectrum is discrete and `f` is a cutoff). Poplawski does not need a compact internal space to be finite (he needs the contact term). They arrive at "finite" by routes that share no machinery.

### 4.5 Strength rating: (c) is COINCIDENCE-DOMINATED (WEAK)

- The literal claim "both have a UV scale" is **cheap** and I decline to credit it.
- The deeper claim "both achieve fermion finiteness from geometry rather than subtraction" is a **genuine but weak** structural resonance — same aesthetic, disjoint mechanism, opposite vacuum behavior.
- **Net: WEAK correspondence.** I would not register this as a cross-pillar bridge; it fails the `cross-pillar-bridge-anatomy.md` Element-3 test (no explicit bridge map; "both have a cutoff" is exactly the "analogous / corresponds to" hand-wave the rule forbids).

> **Throughline T-A3-3** (offered tentatively): *Both ECSK and the framework make fermion physics finite without subtraction, by geometry.* But the geometries are unrelated (matter-sourced torsion vs fixed compact-fiber spectrum) and the vacuum behaviors are opposite. Strength: **WEAK**; do NOT promote to a bridge.

---

## 5. (d) CPT / ARROW OF TIME — the real adjudication

### 5.1 Poplawski's arrow: T-asymmetric boundary condition on a T-symmetric theory

Poplawski is explicit (1007.0587 §VII): *"Although the laws of the ECKS theory of gravity are time-symmetric, the boundary conditions of the Universe are not, because the motion of matter through the event horizon of a black hole is unidirectional and thus it can define the arrow of time."* The arrow is:
- **NOT** in the field equations (ECSK is T-symmetric);
- **imposed by the boundary**: matter falls through the parent black hole's horizon one way (you can't come back out), so the daughter universe inherits a time direction;
- **entropic**: the daughter universe lets entropy keep increasing past the parent's horizon (1007.0587 §VII; 2509.11468 — particle production during expansion "produces large amounts of matter and entropy").

He also notes (1007.0587 §VII) two *dynamical* asymmetry sources at the bounce: extreme tidal particle production, and electroweak spin-alignment making the `∇u` term in eq (8) nonzero (a genuine `t → −t, H → −H` asymmetry). But the *primary* arrow is the horizon boundary condition.

### 5.2 The framework's arrow: transit irreversibility + CPT-exact operator

The framework has **two** arrow-relevant facts that must be kept distinct:

**(i) `[J, D_K(τ)] = 0` — CPT exact, PROVEN (T1, T11; knowledge-MCP, 79,968 pairs, max dev 3.29e-13).** This says the *operator* is CPT-invariant: the spectrum is symmetric about zero (`λ ↔ −λ`), particle and antiparticle masses are equal, KO-dimension 6. The proof (T1) uses only `G5²=I`, `G5` real and symmetric; T11 extends it to *any* left-invariant metric using reality of the structure constants. **This is a statement about the spectrum, not about time evolution or boundary data.**

**(ii) The Ordered Veil — diabatic transit-freeze (S95, R_therm = 5251.82, S_ent = 0).** The arrow comes from the *irreversibility of the supersonic transit*: the GGE relic is a quenched quasiparticle occupation distribution frozen in by the diabatic passage through the van Hove fold; `R_therm = t_therm/t_transit = 5252` means the transit is ~5000× faster than thermalization, so the post-transit state is a frozen non-equilibrium relic that *never thermalizes back*. `S_ent = 0` (product state) — the transit is unitary but the relic is operationally irreversible because reversing it would require re-traversing the fold backwards, which the spectral-action gradient `dS/dτ` forbids.

### 5.3 Are these compatible? — YES in principle, but with a SCOPING TENSION the framework must own

**The CPT-exact substrate does NOT forbid a T-asymmetric boundary condition.** This is the crucial adjudication, and the answer is structurally clean: CPT invariance of the dynamics (or of the operator) is *fully compatible* with a time-asymmetric initial/boundary state. This is not exotic — it is the standard resolution of "why is there an arrow if the microscopic laws are ~T-symmetric." The Standard Model is CPT-exact (Lüders–Pauli, ref-doc 5) and the universe has a thermodynamic arrow; no contradiction. The arrow lives in the *state*, not the *law*. So:

- Poplawski's arrow (horizon boundary condition) and the framework's CPT-exact operator are **compatible**: `[J, D_K] = 0` constrains the *spectrum/dynamics*; the arrow is a property of the *boundary/initial data of the transit*. A CPT-exact operator with a T-asymmetric initial condition is exactly what you expect.

**BUT — and this is the tension I am mandated to surface — the framework cannot have it both ways rhetorically.** The framework repeatedly advertises `[J, D_K] = 0` as "CPT hardwired" and treats it as load-bearing. Yet on the question Poplawski actually answers (where does the cosmic arrow come from?), `[J, D_K] = 0` is **silent**:

1. `[J, D_K] = 0` gives `λ ↔ −λ` spectral symmetry. It says *nothing* about which direction `τ` flows, or why the transit is irreversible. The arrow is supplied entirely by (ii) the diabatic transit-freeze — a *separate* mechanism with its *own* irreversibility source (`R_therm = 5252`).

2. If the framework's arrow is the transit boundary condition (Ordered Veil), then it is **structurally the same kind of explanation as Poplawski's**: a T-asymmetric *initial condition* (the universe starts at the unstable maximum `τ=0` and slides down) imposed on an otherwise reversible substrate. The framework's "first-order transit" plays exactly the role of Poplawski's "matter falling through the horizon": a one-way passage that defines the arrow.

3. **The genuine tension**: is the substrate transit *truly* irreversible (a real T-violation in the state), or is it merely a T-symmetric flow we are observing from one side (like Poplawski's T-symmetric ECSK seen from inside the horizon)? The Ordered Veil's `S_ent = 0` says the transit is **unitary** — there is no entropy production at the transit itself (the relic is a pure product state). That means the framework's arrow, like Poplawski's, is **NOT a dynamical T-violation** — it is a *boundary-condition arrow* on a unitary (hence reversible) substrate flow. `R_therm = 5252` makes it *practically* irreversible (you can't re-thermalize), but the underlying dynamics is reversible, exactly as ECSK is T-symmetric.

So the framework and Poplawski are *more alike here than the framework's "CPT hardwired" language suggests*: **both have reversible/symmetric fundamental dynamics and a boundary-condition arrow.** The difference is the boundary: Poplawski's is a horizon crossing in a parent universe; the framework's is the unstable-maximum initial condition `τ=0` feeding a diabatic transit.

### 5.4 Where the framework is genuinely stronger on CPT — and where Poplawski is

**Framework stronger**: the framework *proves* CPT-exactness of its matter sector at the operator level (`[J,D_K]=0`, particle-antiparticle mass equality to machine precision, T1/T11). This is a real, verified, parameter-free structural result that ECSK does not provide — ECSK is CPT-symmetric by assumption (it inherits GR + minimal coupling), not by a structural theorem. The framework's `[J,D_K]=0` also *forbids internal baryogenesis* (T11 closes all J-breaking baryogenesis on the 36-dim moduli — knowledge-MCP, S43): the framework's CPT-exactness is so strong it makes baryon asymmetry *require physics external to the SU(3) Dirac operator*.

**Poplawski stronger (or at least: addresses what the framework does not)**: Poplawski *has a cosmological-scale source for the matter-antimatter / time asymmetry* — the horizon boundary condition and the electroweak spin-alignment term (1007.0587 §VII) that contributes to "the production of mass in the Universe." The framework's `[J,D_K]=0` is so exact that **it has a baryogenesis PROBLEM**: the substrate cannot generate a baryon asymmetry internally (T11), and the arrow has to come entirely from the transit boundary condition. Poplawski at least *gestures* at a unified origin (horizon crossing → arrow → tidal particle production → mass generation). The framework must source baryogenesis externally and keep the arrow in a separate (transit) mechanism.

### 5.5 Strength rating: (d) COMPATIBLE, but exposes a real scoping tension

- **Compatibility**: the two arrows are **compatible** — CPT-exact dynamics + T-asymmetric boundary condition is consistent and standard. Rating: the correspondence "both arrows are boundary-condition arrows on reversible dynamics" is **MODERATE-to-STRONG and genuine** (and somewhat *unflattering* to the framework's "CPT hardwired" marketing).
- **Tension**: the framework's `[J, D_K] = 0` is **cosmologically silent on the arrow** — the arrow is carried entirely by the Ordered-Veil transit boundary condition (`S_ent = 0` ⟹ unitary ⟹ boundary-condition arrow, NOT dynamical T-violation). This is a real scoping clarification the framework should make explicitly rather than letting "CPT hardwired" do double duty.

> **Throughline T-A3-4 (sharpest)**: *Both ECSK and the framework have time-symmetric/reversible fundamental dynamics and source the cosmic arrow from a one-way boundary condition* (Poplawski: matter through the parent horizon; framework: the `τ=0`→transit diabatic freeze with `S_ent=0`). The framework's celebrated `[J,D_K]=0` CPT-exactness constrains the spectrum, NOT the arrow — it is *cosmologically silent* on the question Poplawski's boundary condition answers. Strength of the structural parallel: **STRONG**. It is the one place the GR-side literature exposes that a framework "CPT-hardwired" claim is doing less cosmological work than its prominence suggests.

---

## 6. FALSIFICATION SECTION (mandatory — tensions, no-analogs, framework-exceeding, and tensions searched-for-and-NOT-found)

### 6.1 NO-ANALOGS (framework structurally lacks the GR-side object)

**F1 — [HIGH severity] No Cartan equation; no spin-sourced torsion.** The framework's connection is Levi-Civita, fixed by the scalar `τ` via structure constants `f_{abc}(τ)`. ECSK's entire mechanism is the Cartan equation `S^k_{ij} ∝ s^k_{ij}` (torsion = matter spin density). The framework has *no equation in which fermion occupation sources the antisymmetric connection*. Matter is downstream of geometry in the substrate; ECSK runs the opposite arrow. This is the single largest structural gap. The framework *knows* the torsion-modified operator `D_T` (Gate T-1, S26–27) and has a theorem that torsion does not open the gap-weakening channel — so the absence is deliberate, not naive, but it is total: none of Poplawski's results (bounce, UV cutoff, spin-baryogenesis) are available to the framework. **Verdict: structural no-analog, confirmed.**

**F2 — [MODERATE] The framework has a BARYOGENESIS PROBLEM that ECSK does not advertise.** `[J,D_K]=0` is so exact (T11) that it *closes all internal J-breaking baryogenesis* on the full 36-dim moduli space (knowledge-MCP, S43). The framework's matter-antimatter asymmetry MUST come from physics external to the SU(3) Dirac operator. ECSK at least gestures at a cosmological mass/asymmetry source (horizon boundary + electroweak spin-alignment, 1007.0587 §VII). This is a place the framework is *more constrained* in a way that creates an open problem, while ECSK is more permissive. **Verdict: genuine open problem on the framework side, sharpened by contact with ECSK.** (This is not new — it is in the framework's own memory — but the ECSK comparison makes its severity concrete.)

### 6.2 TENSIONS (both have an object, they conflict)

**F3 — [SHARPEST tension] `[J,D_K]=0` is cosmologically silent on the arrow.** (Full argument §5.) The framework advertises CPT-exactness as load-bearing; but the cosmic arrow is carried *entirely* by the Ordered-Veil transit boundary condition, with `S_ent = 0` ⟹ the transit is unitary ⟹ the arrow is a *boundary-condition* arrow on reversible dynamics — structurally *the same kind of arrow as Poplawski's* T-asymmetric horizon boundary on T-symmetric ECSK. The "CPT hardwired" claim constrains the *spectrum*, not the *arrow*. The framework should scope this explicitly. **This is the candidate for the campaign's sharpest single tension from the antimatter/CPT side.**

**F4 — [MODERATE] Economy: ECSK adds ZERO parameters; the framework posits a full spectral triple.** (Full argument §3.3.) Poplawski's bounce + flatness + horizon resolution follow from the *minimal* completion of GR (restore the connection's antisymmetric part) with *no tuning* and a *derived* `Ω_S ≈ −10⁻⁶⁹`. The framework's singularity avoidance requires the entire `(ℂ⊕ℍ⊕M₃(ℂ), H_F, D_K)` apparatus on `SU(3)` plus volume-preservation plus the Jensen direction. On Occam grounds, ECSK's mechanism is dramatically more economical. **The framework buys robustness with ontology; this is a real cost and the literature is more economical here.**

### 6.3 FRAMEWORK-EXCEEDING (framework more rigorous/robust than the GR-side)

**F5 — Singularity avoidance is a THEOREM in the framework, CONTINGENT in ECSK.** (Full argument §3.2.) Poplawski's bounce requires `n_f²` (torsion) to outrun shear `σ² ∝ a⁻⁶` during contraction, rescued only by Parker particle production (2509.11468 §4). It is conditional on matter content, ECSK, initial torsion-vs-shear ratio, and an active production channel. The framework's `λ² ≥ R_K(τ)/4 > 0` (Lichnerowicz, E5) is matter-independent, shear-free, production-independent — a structural inevitability. **On robustness, the framework genuinely exceeds.**

**F6 — CPT-exactness is PROVEN (parameter-free) in the framework; ASSUMED in ECSK.** `[J,D_K]=0`, KO-dim 6, particle-antiparticle mass equality to 3.29e-13 (T1/T11) is a verified structural theorem. ECSK inherits CPT from GR + minimal coupling by assumption. (Caveat: this exceedance is in the *matter-sector algebra*, a different arena than ECSK's cosmology; it is real but does not bear on the bounce.)

### 6.4 TENSIONS SEARCHED-FOR AND NOT FOUND (negative results — equally important)

**N1 — I searched for a torsion-induced violation of `[J,D_K]=0` and did NOT find one (as a present fact).** The framework's *existing* torsion-modified operator `D_T = D_K + ¼ΔK γγγ` (S26) is built from the *real* structure constants, and the contorsion term is real-antisymmetric in the same way `Ω_LC` is. The T11 proof (`C₂ conj(Ω) C₂ = −Ω`, using reality of `Γ^b_{ac}`) extends to `D_T` for the *geometric* (structure-constant) torsion. So the framework's own torsion does NOT break CPT. **I could not manufacture a CPT tension from the framework's existing torsion analysis.** (The caveat in §2.4 — that a *spin-sourced* ECSK torsion is not guaranteed to preserve `[J,D_K]=0` — is a statement about a *hypothetical retrofit*, not the present framework; I flag it as a constraint on any future ECSK-ification, not as a current contradiction.)

**N2 — I searched for a place where the framework's first-order transit secretly IS a torsion bounce (a hidden correspondence the framework missed) and did NOT find one.** The transit is a substrate-dynamics object (modulus flow, not c-bounded, Mach 13.75); the torsion bounce is an emergent-geometry object (FLRW scale-factor turnaround). Mapping one to the other requires the forbidden container-thinking inversion (§3.4). There is no hidden bridge; the absence of correspondence is *correct*, not an oversight.

**N3 — I searched for the framework over-claiming singularity avoidance and did NOT find it.** The Lichnerowicz gap (E5) is correctly a *theorem* (verified, Wall W3), and the framework's own normalization caveat (baptista §2.3.3: the `λ²≥3` vs `λ²≥1/2` normalization mismatch) is honestly flagged in the source. The claim "gap never closes ⟹ no singularity" is sound and convention-independent in its load-bearing form (`λ² ≥ R_K(τ)/4 > 0`).

**N4 — I checked whether Poplawski's `ε_S ∝ a⁻⁶` has a spectral-moment counterpart and found only a FALSE friend.** One might be tempted to map `ε_S ∝ a⁻⁶` to a framework spectral moment. But the framework's `a⁻⁶`-type scalings (if any) live in the Seeley–DeWitt expansion of the *bosonic* action and are NOT a negative fermion-spin contact density. The framework's negative-pressure / vacuum physics is the Volovik q-theory partition (`w0_FW = −0.918`, DILUTION-CC, knowledge-MCP) — a vacuum equation of state, not a `−¼κs²` spin term. **The `a⁻⁶` coincidence is a false friend; I do not credit it.**

### 6.5 Falsification scorecard

| ID | Type | Severity | Status |
|:---|:---|:---|:---|
| F1 | No-analog: no Cartan eq / spin-sourced torsion | HIGH | Confirmed structural gap |
| F2 | Framework baryogenesis problem (vs ECSK permissiveness) | MODERATE | Open problem, sharpened |
| F3 | `[J,D_K]=0` cosmologically silent on arrow | **HIGH (sharpest)** | Real scoping tension |
| F4 | Economy: ECSK 0 params vs framework spectral triple | MODERATE | Framework costlier |
| F5 | Singularity avoidance theorem vs contingent | — | Framework EXCEEDS |
| F6 | CPT proven vs assumed | — | Framework EXCEEDS (diff arena) |
| N1 | Torsion-CPT violation | — | Searched, NOT found (present) |
| N2 | Hidden transit↔torsion bridge | — | Searched, NOT found (correctly absent) |
| N3 | Over-claimed singularity avoidance | — | Searched, NOT found |
| N4 | `a⁻⁶` spectral-moment counterpart | — | False friend, not credited |

---

## 7. Throughlines and carry-forwards

### 7.1 My throughlines (derived, not pre-supplied)

- **T-A3-1 [no-correspondence]**: ECSK dynamical spin-sourced torsion is the laboratory-IN shadow of *nothing* in the substrate. The substrate forbids the matter→geometry arrow ECSK requires. The single most important finding.
- **T-A3-2 [weak correspondence]**: Torsion bounce ≈ substrate transit only at "no singularity"; mechanisms disjoint. Framework more robust (theorem), ECSK more economical (0 params). Re-reading the transit as a torsion bounce is a forbidden inversion.
- **T-A3-3 [weak/aesthetic]**: Both make fermion physics finite from geometry, not subtraction — but disjoint geometries, opposite vacuum behavior. Do NOT promote to a bridge.
- **T-A3-4 [strong, unflattering]**: Both arrows are boundary-condition arrows on reversible dynamics. `[J,D_K]=0` is cosmologically silent on the arrow; the work is done by the Ordered-Veil transit (`S_ent=0` ⟹ unitary ⟹ boundary-condition arrow).

### 7.2 Carry-forwards (4-field specs, for `/rclab-plan` if the campaign promotes any)

- **CF-A3-1 (arrow scoping)** — *What*: explicit registry/capstone statement that the cosmic arrow is the Ordered-Veil transit boundary condition (unitary, `S_ent=0`), and that `[J,D_K]=0` constrains the spectrum, not the arrow — so the two are compatible (CPT-exact dynamics + T-asymmetric initial condition) and the framework's arrow is structurally a boundary-condition arrow, like Poplawski's. *Inputs*: T1/T11 (`[J,D_K]=0`), S95 Ordered-Veil (R_therm, S_ent=0), 1007.0587 §VII. *Gate*: documentation reconciliation (no compute) — capstone §-prose patch, designated writer. *Effort*: small (prose; methodology-class).
- **CF-A3-2 (ECSK-retrofit CPT constraint)** — *What*: test whether a *hypothetical* spin-sourced (non-geometric) torsion added to `D_K` would preserve `[J,D_K]=0`; the T11 proof uses reality of structure constants, which a spin-sourced complex torsion may violate. *Inputs*: T11 proof structure, a candidate spin-sourced contorsion ansatz, `C₂ conj(·) C₂` machinery. *Gate*: `[J, D_K+T_spin]=0` to machine ε, PASS/FAIL. *Effort*: medium (one eigen/commutator computation; mostly closes a hypothetical, low EVOI — list as low-priority).
- **CF-A3-3 (baryogenesis-external scoping)** — *What*: register that ECSK provides a cosmological asymmetry gesture (horizon boundary + EW spin-alignment) that the framework lacks internally (T11 closes internal J-breaking baryogenesis), making external baryogenesis a live open item; compare to the framework's existing "external baryogenesis mechanism" open question. *Inputs*: T11, S43 baryogenesis closure, 1007.0587 §VII. *Gate*: open-question registry update (no compute). *Effort*: small.

### 7.3 Substrate-first compliance note

Every correspondence above is stated as "GR model X is the laboratory-IN shadow of substrate-IS mechanism Y" or, where there is no shadow (T-A3-1), as an explicit no-analog. I did not invert the arrow. The one place the GR-side is *more* fundamental on a given axis (economy, F4; cosmological-arrow source, F3) is reported as a tension/exceedance, per the FALSIFICATION mandate, not smoothed into a false correspondence.

---

## 8. Top-line deliverable summary

**Top 2 throughlines**:
1. **T-A3-1 — ECSK spin-sourced torsion has NO substrate pre-image.** The framework's connection is Levi-Civita, fixed by the scalar `τ` and the `su(3)` structure constants; there is no Cartan equation, so fermion spin cannot source the connection's antisymmetric part. The single degree of freedom doing all the work in Poplawski's program is structurally absent — and its absence is theorem-backed (Gate T-1: torsion does not open the gap-weakening channel), not naive. This is a clean falsification of correspondence, the largest structural gap in the comparison.
2. **T-A3-4 — Both arrows are boundary-condition arrows on reversible dynamics.** Poplawski's T-symmetric ECSK + one-way horizon crossing is structurally mirrored by the framework's unitary transit (`S_ent=0`) + `τ=0`-initial-condition diabatic freeze. The framework's `[J,D_K]=0` "CPT hardwired" claim is *cosmologically silent* on the arrow — it constrains the spectrum, not the boundary data.

**Single sharpest tension (F3)**: **`[J,D_K]=0` does not source the arrow of time.** The framework advertises CPT-exactness as load-bearing, but the cosmic arrow is carried *entirely* by the Ordered-Veil transit boundary condition, which `S_ent=0` reveals to be a *boundary-condition arrow on unitary (reversible) dynamics* — the same kind of arrow ECSK gets from matter falling through a horizon. CPT-exactness of the operator is compatible with this, but it does *not* explain it; the framework should scope the two claims separately rather than let "CPT hardwired" carry cosmological weight it does not bear.
