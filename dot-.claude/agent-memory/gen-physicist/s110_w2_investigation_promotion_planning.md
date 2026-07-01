---
name: s110-w2-investigation-promotion-planning
description: Planning a compute wave that session-promotes investigation-track builds — inputs are inv{n}_*.npz (static-SHA pin), substrate-first sourcing bites on non-canonical pins, dedup flags, npz-grounded thresholds
metadata:
  type: feedback
---

Authoring a per-wave compute plan whose gates SESSION-PROMOTE investigation-track results (inv-10/11/12/13 builds → `s110_*` session gates).

**Why:** investigation verdict files under `computations/investigation-*/` are NOT swept into the knowledge index (`gate-verdicts.md §"Investigation-Track"` track-local boundary); a result becomes permanent ONLY when re-computed under a `session-N` gate. So the gate's job is a migration wrapper, NOT a fresh derivation. The producing investigation npz becomes a STATIC input-SHA pin (pre-compute it at plan-freeze, the file is frozen).

**How to apply:**
- **Ground every threshold in the producing npz, not the rollup prose.** Load the inv npz with the venv python and read the exact stored values. S110 W2 examples where prose ≠ npz: CCDARK1 rollup said "target ρ_vac/ρ_rad<0.2" but `inv11_w4_*.npz` carries the substrate-DERIVED `bbn_bound=0.22710731766023898` + `g_eff_needed_for_bound=0.016153589843546128` + `factor_short=53.845`. Pin the exact derived value; the round 0.2 is a Class-(f) PIN-PLACEHOLDER if pinned over the existing substrate canonical. CV2A: `oom_distance=0.7201655350546652`, `frac_uncert_gap_term=0.8297912902304105` (gate = OOM≤1.0 AND frac_gap≥0.5, reproduce bit-for-bit).
- **Non-canonical pins are the substrate-first trap.** `get_constant('rho_relic')` and `get_constant('lambda_min')` both returned NULL — these (ρ_relic=26.553854 M_KK, λ_min(τ)=0.790) come from the session source (S17a) or the input npz, NEVER hardcoded as if canonical. Cite the npz/session, mark `<computed-at-runtime>` SHA.
- **Apply the triage dedup flags at gate-block authoring:** (i) TRANSIT-PS-67 = ONE promotion, shape+amplitude land together (CF-B1 must NOT be planned shape-only); (ii) finite-μ CFL = ONE gate (CF-CO1, not duplicated); (iii) deg(T_{BZ→pivot}) derived ONCE on the M⁴ summand (CF-CV6B); (iv) WS-FLOQUET before WS-AS-1.
- **deg(T_{BZ→pivot})=+2 NON-SCALAR is CANONICAL** (S93 W7-1 `factorization_holds=False, formulation=T4-non-scalar`; 54.04 decades). The BZ-leaf is k³-BLUE n_s≈3 (2.9998); the red n_s=0.9561 lives ONLY at the Goldstone-pivot leaf via Mode-Independent Occupation Theorem (S57/S62 PROVEN). Carry the scale-tag in CF-B1 explicitly.
- **CF1 minisuperspace MUST cite `V_spec monotone` (S24a closed: a_4/a_2=1000:1, no Starobinsky minimum) in its substitution chain with a same-object-or-distinct declaration.** The a(t) rollup §3 flags the minisuperspace a₄-sign (the open knob) may already be settled by V_spec; without the citation the gate risks silently re-deriving or contradicting a closed result (the `p_S75 ≠ p_cosmo` potential-landscape-vs-Friedmann-reduction lesson — different functionals of the same a₄).
- a_n_FW_zeta canonical triple: a_0=6440, a_2=2776.165389, a_4=1350.7216 (zeta-scheme, Gilkey-normalized); S_SA = a_0 − a_2 + a_4 (E7 combination). Tag `a_n^{ζ}` (regulator-pin-discipline).
- canonical_constants.py SHA at S110 plan-freeze: e5a7587f8326c9cc90cb720197a3ace824b3f89c5bbea17cfd659b27f607568a.
- Spectrum cache lives at `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (NOT `_shared/`).
