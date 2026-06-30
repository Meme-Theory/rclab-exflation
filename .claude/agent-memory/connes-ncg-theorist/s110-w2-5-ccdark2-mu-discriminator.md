---
name: s110-w2-5-ccdark2-mu-discriminator
description: S110-CF-CCDARK2-MU PASS (Reading-A) — both SA-side slopes ∂(vac)/∂μ and ∂(cond)/∂V|_Δ = 0 EXACTLY on L10 signed D_K spectrum; CC is Layer-B Gibbs-Duhem (Wall #6 + Kosmann numerically confirmed). Signed-Nambu-spectrum requirement.
metadata:
  type: project
---

# S110-CF-CCDARK2-MU — the μ-discriminator (Reading-A, PASS)

**Result.** On the L_max=10 D_K cache, the S35 BdG spectral triple `H_BdG(μ)=[[D_K−μ,Δ],[Δ†,−(D_K−μ)]]` gives BOTH SA-side slopes EXACTLY zero at the PH-symmetric μ=0:
- `∂(vacuum)/∂μ`: `dS_SA/dμ|_0 = 0.000` exact (S_SA = Tr f(D²_BdG/Λ²) even in μ about μ=0 by the {±λ} symmetry); cutoff-independent (exp AND rational f both 0).
- `∂(condensation)/∂V`: `dS_SA/dV|_{Δ fixed} = 0.000` exact (S35 Kosmann: V ∉ domain(Tr f); the trace depends on V only through Δ(V), so V-blind at fixed Δ).

⇒ **Reading-A**: the CC-selecting d.o.f. is OUTSIDE {Tr f} — Layer-B Gibbs-Duhem, SA-disjoint. Wall #6 (μ=0 PH-symmetry, S34) + S35 Kosmann CONFIRMED NUMERICALLY. Maps to PASS (the gate's pre-registered Reading-A branch).
audit_sha256 `34b030416b927a7a95768525ce44dbcc58455fc7a56f5fd294d6e5dc23967db4`.

**Cross-checks (all PASS):** d²S/dμ² = +2.38e6 > 0 (S34 local-minimum SIGN matched; magnitude is Λ-normalization-dependent); Gibbs-Duhem `dΩ/dμ = −⟨N⟩` resid 0.00; Ω stationarity at μ=0 = 6.4e-6; gap calib reproduces Δ_BCS to 4.4e-11; GPU `torch.linalg.eigvalsh` vs closed-form `E_k=√(ξ²+Δ²)` = 2.66e-16.

**Consequence.** WS-SA-FREE-ENERGY (the R0-gated workshop, task #9) COLLAPSES TO HOUSEKEEPING — the functional channel does NOT reach the CC. atlas-04 S3 CORE cell (open since S6): Layer-A down-scope confirmed. The S6 question "does spectral action = phonon free energy?" is answered for the VACUUM: SA is the Layer-A effective action; Layer B (the CC) sits OFF it on the (μ,V) order-parameter axis. Connects to [[s65-connes-collab]] (a_0/a_2=C_Q/R universal; CC functional-not-geometric) and [[s63-cc-path-e]].

**Why this matters / how to apply:** confirms the CC-as-spectral-moment route stays CLOSED at the functional level — consistent with the standing "all SA routes CLOSED; CC is functional not geometric" (MEMORY.md Open Tension #3). The CC problem is NOT reachable by Tr f(D²); the order parameter (Gibbs-Duhem (μ,V) axis) is the only channel that carries the vacuum selection.

## REUSABLE METHODOLOGICAL LESSON — signed Nambu spectrum (load-bearing)

Any BdG μ-scan / V-scan / PH-symmetry computation on the D_K cache MUST use the **signed single-particle spectrum {±|λ_k|}**, NOT `|λ_k|` alone. The S35 BdG Hilbert space is `H_K ⊕ H_K` (particle ⊕ hole); the chiral symmetry `{γ₉, D_K}=0` pairs `(λ,−λ)`. Loading only `abs_evals` from the cache (a one-sided gapped spectrum) silently DESTROYS the PH symmetry and produces a FALSE Reading-B: in draft-1 it gave `dS/dμ=4.8e-3≠0`, NEGATIVE `d²S/dμ²` (contradicting S34's local-minimum sign), broken Gibbs-Duhem (resid ~1.0), failed GPU validation (resid 0.50). The four contradictions-with-S34 are the tell. Fix: `lam_signed = concat([abs_lam, -abs_lam])`, drop the explicit ×2 factor in Tr f (the doubling is now in the spectrum), restrict the gap-equation sum to the positive half (`lam>0`) to avoid double-counting distinct modes. See also Debugging Note "V matrix (S34): Frame vs spinor" — same class of "which basis" trap.

**Construction pins** (canonical for re-use): Δ_BCS=0.4642547 (R-protected), Λ=K_crit_BdG=2.035 (SA cutoff scale), pairing window = K_crit_BdG, ε_zero=1e-10 (numerical-zero floor), central-diff h=1e-4. Cache: `s84_spectrum_cache_L12_tau019.npz` filtered to p+q≤10 (78,080 |λ| modes, 7,538 unique signed values, |λ|∈[0.8197,4.6702] M_KK).
