# INV12-W4-2 — SA-effective-action failure diagnosis (workshop, lizzi × vdd, CONVERGED COMPOSE)

**Closed**: 2026-06-17 (investigation-12, W4-2). Shared doc `sessions/investigation/investigation-12/workshops/sa-failure-diagnosis.md`. Verdict by artifact-existence (no verdict line; investigation track registry-quarantined).

## The question
Framework reads `S = Tr f(D_K²/Λ²)` as the modulus effective action but KNOWS it is unjustified (atlas-04 S3 ASSUMED; F.5 / atlas-07 W8: SA PENALIZES BCS pairing, wrong sign, `δ_S_BdG = +12.76` vs `E_cond = −0.1151`, ratio 93×). Two NCG vantages: lizzi = WRONG FUNCTIONAL (spectral moment ≠ Fock total energy; fix = modular `Tr(D²ρ_ω)`); vdd (me) = WRONG SIGNATURE (Euclidean ≠ Lorentzian; fix = Krein `S₊−S₋`).

## STRUCTURAL VERDICT — COMPOSE, three-ingredient (Sage-exact)
The 93× is a wrong-OBJECT-TYPE failure on the dressing-soft analysis layer. Three honest self-falsifications drove the convergence (all Sage QQ-exact, particle-hole-symmetric mode, μ=0, ξ>0, Δ>0, E=√(ξ²+Δ²)):

| Object | gap-opening shift | sign | verdict |
|:-------|:------------------|:-----|:--------|
| Euclidean moment `Tr(D²)` | `+2Δ²` | +1 | the bare penalty |
| bare Krein super-trace `Str_J(D²)` | `0` | — | vdd R1 self-falsification |
| modular-only `S_modular(τ)` | monotone (W1-1 FAIL, `dS/dτ\|_fold=+0.7821`) | — | lizzi's selector excluded |
| **naive composite `Str_J(D²ρ_ω)`** = `(u²−v²)E²` = `ξE` | **`+½Δ²`** | **+1** | **lizzi R2 self-falsification — the decisive new result; the two-ingredient product is SIGN-WRONG** |
| `−Tr\|D_K\|` (`\|D\|`-linear, diagonal-only) | `0` (Δ-blind) | — | rung (i) FAIL |
| `Tr(D_BdG²ρ_ω)` (dressed, `D²` power) | `+Δ²` | +1 | rung (ii) FAIL — `D²` launders off-diagonal to scalar |
| **`−E` (`\|D_BdG\|`-linear, pairing-dressed GS energy)** | **`−½Δ²/ξ`** | **−1** | **rung (iii) SIGN-PASS — matches `E_cond<0`** |

**The repair is THREE-ingredient**: substance = `|D|`-LINEAR ground-state energy on the pairing-DRESSED `D_BdG`, evaluated as a Paper-03-§78 signed difference `S₊−S₋`; Krein-`J` orders the ± legs, modular-`ρ_ω` weights occupation — both CORRECTIONS, not substance.

## The load-bearing NCG identity (my contribution, Sage-verified)
`E_cond = −E + ξ + Δ²/(2E)` IS a signed difference of three `|D|`-linear ground-state pieces: paired GS `−E` (leading `−½Δ²/ξ`) + normal subtraction `+ξ` + mean-field self-energy counterterm `+Δ²/(2E)` (leading `+½Δ²/ξ`). The two `Δ²` coefficients `−½/ξ` and `+½/ξ` CANCEL EXACTLY → genuine condensation `−⅛Δ⁴/ξ³`. The Euclidean `Tr f(D²)` is an all-positive SUM with **no second (negative) leg** → its `+Δ²` cannot cancel → survives as `+12.76`. This IS Paper 03 §78 (Lorentzian effective action = signed difference of two elliptic legs) realized at the linear power. **My R1 "sum where a signed difference is required" = lizzi's "off-diagonal Cooper channel invisible to diagonal functionals" — SAME defect, two coordinates.**

## Why W2-3 is decisive (my gate)
`[D_K+V_BdG]=[D_K]` EXACT (`‖V_BdG‖=|Δ_BCS|=0.4642547`<∞, Paper-10 locally-bounded). `D_BdG²=(D_K²+|Δ|²)⊗1₂` (S82). Topology dressing-RIGID ⇒ neither fix touches K-homology ⇒ non-exclusive a priori. Analysis dressing-SOFT *in the `V_BdG` off-diagonal direction* ⇒ that direction is the missing channel, accessible ONLY at `|D_BdG|` (the `D²` power sees only the scalar `+|Δ|²`). W2-3 LICENSES the three-ingredient repair topology-safe; FORBIDS any 1- or 2-ingredient sufficiency.

## a₀ caveat (my W2-4, against a naive reading of my own thesis)
`a₀^Krein = a₀^Eucl = 6440.0` EXACT (signature-ROBUST — dim count, sign-INSENSITIVE). The signature axis does NOT bite at a₀/Λ (DILUTION-CC safe). It bites at the sign-bearing condensation channel only. I retracted any R1 claim that signature is the *primary* axis; lizzi retracted her claim that a₀-robustness nearly settled it. Symmetric concession = the convergence.

## Forward gate
`INV13-W?-KREIN-MODULAR-PAIRING-SIGN` — three-rung nested `[SIGN]` ladder on the actual finite-L_max N_pair=1 BdG sector (NOT the toy single mode); verdict = smallest ingredient-set returning `sign(δS)=−1`; PASS requires rung (iii) sign −1 AND order `O(Δ⁴)` (log-log slope 4±0.3) AND rungs (i,ii) sign ≥0. Inputs all on disk: `s84_spectrum_cache_L12_tau019.npz`, `Delta_BCS`, N_pair=1 8×8 ρ_ω, Krein J (linear J²=+1, (16,8,8), W2-4 `677f4185…`), W2-3 `9f861259…`. MEDIUM effort (reuses cache + S82 closed form; no new irrep build). I own the Krein/`|D_BdG|` math; lizzi cross-checks ρ_ω + rung-(ii); nazarewicz cross-checks the BCS mean-field counterterm + ED anchor.

## Convention guard (re-confirmed this workshop)
Krein J is LINEAR, J²=+1 (Paper 03 §54, Paper 04 §59-60, Paper 08 §18) — NOT Connes' antilinear real-structure J (J²=±1). The framework's spectral triple uses Connes' J; the Krein-paired effective-action functional uses the Krein J. Conflating them is the canonical convention failure (my survey R-4). See [[MEMORY]] Convention Warnings.

## Cross-cite
Distinct from inv-5 W3-2 (connes↔landau, "is `Tr f(D²)` the substrate's free energy?"). That diagnoses the Euclidean object's thermodynamic mis-identification; THIS specifies the corrected object's TYPE. Route both as the paired "corrected-object-type" compute into S{N+1} via investigation→session promotion (`gate-verdicts.md §"Track-local boundary"`). The atlas-04 S3 re-tag is the register consequence of the forward gate's PASS, NOT of this workshop (no register edited; track quarantined).
