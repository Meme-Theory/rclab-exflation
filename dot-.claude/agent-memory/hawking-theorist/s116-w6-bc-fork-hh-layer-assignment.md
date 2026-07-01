---
name: s116-w6-bc-fork-hh-layer-assignment
description: S116-W6 Ψ(τ=0) BC fork — HH is the WDW-constraint parent, "Vilenkin" the decohered outgoing branch (layer assignment); reflecting τ=0 datum forces J≡0 (Wronskian); e-fold gap BC-invariant; residual = Q45 operator canonicity
metadata:
  type: project
---

S116-W6-BC-FORK (`sessions/session-116/workshops/s116-w6-bc-fork.md`): adversarial adjudication of the substrate's Ψ(τ) boundary condition at the τ=0 unstable maximum — Hartle-Hawking no-boundary (my side) vs Vilenkin tunneling (quantum-foam). My R3 position on record; quantum-foam writes Turn-B Structural Verdict. Tight convergence to a LAYER ASSIGNMENT, not a 50/50 standoff.

**Resolution (GEOMETRIC, Level-2 moduli-deformation): HH is the WDW-CONSTRAINT parent; "Vilenkin" is a layer label** for the decohered outgoing WKB branch of Ψ_HH's classical limit (Layers 1-2), NOT a fundamental alternative constraint BC.
- **Layer 0 (constraint)**: potential = S(τ) (S36 monotone spectral action); τ=0 an S-MINIMUM / regular South Pole; BC = HH, Neumann/reflecting ∂_τΨ(0)=0 (master-collab HT-2 l.943); weight e^{−S(τ)}=Z_fiber, FINITE.
- **Layer 1 (emergent dynamics)**: V_eff=−S+const (instanton inversion sign(V_eff'')=−sign(S''), d²S/dτ²|₀=+3.0e5); τ=0 a V_eff-MAXIMUM; cascade = WKB integral curves rolling away.
- **Layer 2 (realized history)**: decoherence + DNP arrow select the OUTGOING branch = "Vilenkin"-like, irreversible.

**Decisive argument — Eq. H-R3-1 (Sage-verified, `mcp__sage__sage_eval`):** real-coefficient WDW op [−(1/2G_DeWitt)∂_τ²+(V−E)]Ψ=0 ⇒ current J=Im(Ψ*∂_τΨ)=uv'−vu' (Wronskian of the two real solutions u,v); ∂_τJ=W(uv−vu)=0 ⇒ J GLOBAL CONSTANT (conserved in the s2 allowed region too). Reflecting τ=0 datum (Neumann ∂_τΨ(0)=0 OR Dirichlet Ψ(0)=0) ⇒ J(0)=0 ⇒ **J≡0 everywhere** ⇒ s2 oscillatory solution is a REAL STANDING WAVE (HH-parent), NOT an outgoing complex wave. A real τ=0 anchor forces real Ψ forces J≡0 — on s1 AND s2. Fundamental J≠0 needs the holonomy op to REMOVE the τ=0 reflecting wall + anchor outgoing-only at the far edge = answer-shopping + itself a Q45 choice. DNP instability does NOT source J (would violate homogeneous ĤΨ=0); it lives on Layer-1 V_eff, realized as the Layer-2 decohered branch (J≠0 for the branch, J=0 for the parent).

**HT corrections (load-bearing, prevents re-derivation):** Z_fiber(τ)=e^{−S(τ)}, S=Tr f(D_K²(τ)/Λ²) at FIXED τ (FINITE ∀τ) ≠ Z_mod=Tr e^{−βH_mod} (DIVERGENT, no bound state, HT-1 l.925: ½ω₀/ΔV=183). HT-1's no-bound-state result fixes the GEOMETRY (half-line scattering), NOT the contour. HT-3: condensate restores a self-consistent locking MINIMUM at τ₀ (HH retained, never Vilenkin); irreversibility lives at the τ=0 DEPARTURE, not the τ₀ lock.

**Track B (BC-robust):** N_e=0.1734 BC-INVARIANT — BC flips exp(±B) sign, not |B|=22.2552 (B_WKB(fold)); efold_ratio=1.0; N_e_WKB=N_e_classical·(B_traj/B_class). EFOLD-MAPPING-52 (FAIL-structural, IC-INDEPENDENT) is HH's no-boundary-side CONFIRMATION — a BC is the prototypical IC-type datum — but SCOPED to s1 (the s2 allowed-region ∫H dt is a DISTINCT functional). S70 (WKB inapplicable to Mach-13.75 van-Hove transit; sudden approx mandatory): the count is set AT τ_fold by the sudden transit → TRANSIT-PS-67; the BC reaches only the adiabatic cap (τ<τ_fold). IC-independence = structural shadow of the adiabatic/sudden partition.

**Residual = Q45 OPERATOR canonicity, NOT a BC fork:** S110-CF1-AT-MINISUPERSPACE schemes_agree=False (s1 monotone-S regular-min vs s2 holonomy turning surface ρ_c≈13.41 = s2_turning_rho, IN-window). Two-stage **CF-S117-Q45-TAU0-OPERATOR-CANONICITY**: Stage-1 resolve s1-vs-s2 (does ρ_c survive; does τ=0 stay reflecting or become a transparent bounce?); Stage-2 conditional-on-s2 measure **J at ρ_c under -BOTH** (J≡0 → HH-parent lifted; J≠0 → fundamental outgoing). s1 → J≡0 trivial → HH unconditional. On s2 the discriminator goes LIVE (only there) and Track A becomes reachable via the allowed-region integral.

**Compute convention pins:** S116-W6-WDW-IC-REFINE → **-HH** canonical cap weight, **-BOTH** as the mandatory BC-invariance diagnostic (demonstrates efold_ratio=1.0 both branches), NOT co-canonical fundamental BCs.

Connects to [[s115-w3-3-b5a-tfd-qes-overshoots-2a4]] (HH Euclidean methods on the substrate) and the no-boundary retraction in MEMORY.md permanent-retractions (HP no-boundary at the fold was retracted S26-39 — THIS finding scopes HH to the WDW CONSTRAINT cap τ<τ_fold, OFF the van-Hove fold, consistent with that retraction via the adiabatic/sudden partition).
