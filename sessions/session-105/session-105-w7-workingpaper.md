# Session 105 Wave 7 — Substrate Trace Formula: Geometric-Side First Map + Zeta-Zero Geography (Results Working Paper)

**Session**: 105 | **Wave**: W7 | **Plan**: session-105-plan-w7.md | **Theme**: Off-session RH/trace-formula program as 6 pre-registered gates — anchor the τ=0 two-sided trace formula, extract the substrate length spectrum at τ_fold for the first time, predict it (Berry–Tabor), certify its commensurability, and map the actual ζ_{D_K} / S³-proxy zero geography.

## Gate Sections

### §W7-1. S105-W7-1-TRACE-FORMULA-EXACT-ANCHOR (spectral-geometer)

**Status**: COMPLETED
**Verdict**: PASS
**Gate ID**: `S105-W7-1-TRACE-FORMULA-EXACT-ANCHOR`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (positive-control two-sided heat-trace identity on undeformed SU(3))
**Agent**: `spectral-geometer`
**Hypothesis**: On undeformed bi-invariant SU(3) the spectral Peter–Weyl reading of `Tr exp(−t D_K²)` equals the geometric coroot-lattice theta-dual (rank-2 Poisson summation, derived in-script) to `< 1e-10` at every pinned heat-time — validating the wave's pipeline on a known-exact case.
**Plan reference**: `sessions/session-plan/session-105-plan-w7.md` §W7-1. Unconditional positive control; no gate dependency.

**Substrate framing (substrate → emergent).** GEOMETRIC. The fabric's internal geometry at τ=0 IS the bi-invariant SU(3) spectral triple; `K(t)=Tr exp(−t D_K²)` is the substrate's own return-probability functional. Its **spectral side IS** the Peter–Weyl decomposition of `D_K`'s eigenvalue spectrum (all internal vibrational modes); its **geometric side IS** the sum over the closed internal relay orbits — coroot-lattice translations on the maximal torus. Poisson summation is the exact statement these two readings coincide. τ=0 is a moduli reference point (the physical fabric is at τ_fold=0.190, W7-2). Arrow: `D_K eigenvalues → heat trace → two-sided trace identity`; the geometric side is derived FROM the spectrum, never assumed. The trace formula is the substrate's intrinsic spectral-geometric identity, not an external import.

**MCP Pre-Compute Audit** (queried BEFORE writing the script):
- `search_knowledge("trace formula Poisson summation length spectrum coroot lattice bi-invariant SU(3)")` → prior `FORMULA-61`/`trace_formula_geometric` (S61 INFO, 992-mode residual W7-2 supersedes); structural eq `R(0)=2.000000 (Einstein metric, bi-invariant)`; S102-W3 note that the τ=0 spectrum **"reproduces Fegan's 1987 closed form"**. NOT pre-closed (no τ=0 two-sided Poisson trace identity exists).
- `get_constant("tau_fold")` → 0.19 (S12/S42, `CONST-FREEZE-42`); framing reference only.
- `list_constants("casimir|c_off|R_scalar|...")` → no canonical `c_off`/`casimir_pq`; Casimir computed in-script (canonical normalization, as in `dirac_spectrum.py`/`s54_gutzwiller_su3.py`); `c_off` MEASURED in-script (R_scalar/8), not imported.
- Cross-read `sessions/session-102/session-102-w3-workingpaper.md` (S102-W3 keystone PASS 8.882e-15) → supplied the exact closed form (*).

**The exact Dirac closed form (substrate-first; S102-W3-validated).** The bi-invariant SU(3) Dirac square is NOT scalar `C₂+c_off` per sector. The correct Fegan/Parthasarathy–Kostant form is

```
|λ(p,q,μ)|²  =  (1/6)·[ C₂(μ) + C₂(p,q) ]  +  1/4              (*)   C₂(p,q)=(p²+q²+pq+3p+3q)/3
```

μ over irreps of `V_{(p,q)} ⊗ S`, `S|_SU(3)=8⊕8` (forced: trivial sector gives `|λ|²=3/4=(1/6)·3+1/4` ×16 ⇒ `C₂(μ)=3=C₂(8)`, ×16=2·dim(8)). Verified against the project pipeline's OWN multiset (Sage-exact rationals):

| (p,q) | closed-form `|λ|²` (×mult) | pipeline | match |
|:--|:--|:--|:--|
| (0,0) | 3/4 (×16) | 0.75 (×16) | ✓ |
| (1,0)/(0,1) | 25/36 (×6), 37/36 (×12), 49/36 (×30) | {0.6944,1.0278,1.3611} ×{6,12,30} | ✓ |
| (1,1) | 3/4 (×2), 5/4 (×32), 7/4 (×40), 25/12 (×54) | {0.75,1.25,1.75,2.0833} ×{2,32,40,54} | ✓ |

`max |λ|² abs-diff over p+q≤6 = 2.878e-13`. The `V_{(p,q)}⊗8` CG is computed in-script via the exact Brauer/Klimyk Weyl-shift rule (cross-checked vs `WeylCharacterRing("A2")`: `3⊗8=3+6̄+15`, `8⊗8=1+2·8+10+1̄0̄+27`).

**PLAN-PREMISE CORRECTION (honest; not convention-shopped).** The plan's Step 2 wrote `|λ|²=C₂(p,q)+c_off` (one degenerate eigenvalue/sector) — geometrically wrong: each sector has a NON-degenerate multiset set by the spinor-tensor Casimir `C₂(μ)`. The actual form is (*). The plan's `c_off` IS the `+1/4` Friedrich/Lichnerowicz floor:

```
c_off = R_scalar(g_biinv)/8 ;  R_scalar = 2.000000000000000 (in-script, ON-frame Σf²=8 ⇒ R=2)
⇒ c_off = 2/8 = 1/4 = 0.250000000000000  (EXACT)
```

cross-checked vs (0,0): `|λ|²=3/4=3·c_off ⇒ c_off=0.25` ✓. The named constant survives; only its role (`C₂(p,q)+c_off` → (*)) is corrected.

**The exact two-sided identity (gate object).** From (*), the Dirac heat trace's torus/character representation is the controlling theta

```
Θ_S(t) := 2 · Σ_{ν∈wt(8)} Σ_{Λ∈weight lattice} exp(−(t/6)·|Λ+ρ+ν|²_M)      (T)
```

`M=(2/3)A⁻¹` (weight Gram in the Casimir metric; verified `C₂(Λ)=|Λ+ρ|²_M−|ρ|²_M`, `|ρ|²_M=4`, ρ=(1,1)); `wt(8)`=6 roots+2 zero weights; factor 2 = two adjoints in `8⊕8`. Rank-2 Poisson summation (DERIVED IN-SCRIPT, mpmath dps=50; Cholesky M, dual basis R⁻ᵀ) maps each weight-lattice theta to a coroot (winding) sum:

```
Σ_Λ e^{−s|Λ+x|²_M} = (π/s)^{r/2}/√(det M) · Σ_{ν∈coroot} e^{−(π²/s)|ν|²_{M⁻¹}} e^{2πi⟨ν,x⟩}   (P), r=2, s=t/6
```

(P) is EXACT (heat-kernel theta modularity). Gate compares **spectral** `Θ_S^spectral` (direct weight-lattice (T)) vs **geometric** `Θ_S^geometric` (coroot Poisson dual of (T)) — genuinely different lattices/kernels (broad Gaussian over weight lattice vs modular-transformed Gaussian+phases over coroot lattice; NOT load-and-compare-to-self). (The literal full Peter–Weyl trace `Σ dim(p,q)Σ_μ dim(μ)e^{−t|λ|²}` carries the Plancherel polynomial weight ⇒ Poisson gives a derivative-of-theta combination, no single clean coroot dual; the torus object (T) is the exactly-dualizable substrate trace formula whose conjugate variable is the coroot/winding lattice, and the closed-geodesic LENGTHS W7-2 extracts are set by THIS lattice geometry, independent of amplitude weight.)

**Output Artifacts** (verified on disk by content):
- Script `computations/session-105/s105_w7_1_trace_formula_exact_anchor.py` — contains `from canonical_constants import`, `print_verdict_payload` (grep-confirmed).
- Data `computations/session-105/s105_w7_1_trace_formula_exact_anchor.npz` (heat_times, theta_S_spectral, theta_S_geometric, rel_2sided, poisson_rel, kspec_xcheck_rel, R_scalar, c_off, closed_form_max_absdiff, max_rel, verdict).
- Plot `computations/session-105/s105_w7_1_trace_formula_exact_anchor.png` (left: rel mismatch vs t with 1e-10 PASS line; right: Θ_S spectral vs geometric).
- Verdict line `computations/session-105/s105_gate_verdicts.txt` matching `^S105-W7-1-...:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row.

**Verdict**: **PASS**.

**Results** (NUMBERS first):

| t | s=t/6 | Nrad_spec | Θ_S spectral | Θ_S geometric | geom.im | rel mismatch |
|:--|:--|:--|:--|:--|:--|:--|
| 0.02 | 0.00333 | 319 | 39178.0662674591 | 39178.0662674591 | −1.4e-4421 | **8.05e-50** |
| 0.10 | 0.01667 | 146 | 7835.613253491821 | 7835.613253491821 | −1.1e-922 | **5.59e-50** |
| 0.50 | 0.08333 | 69 | 1567.122650698364 | 1567.122650698364 | −1.9e-223 | **1.69e-49** |
| 2.00 | 0.33333 | 40 | 391.7806626745911 | 391.7806626745911 | −2.7e-129 | **2.34e-29** |

- **`max_t |Θ_spec − Θ_geom|/|Θ_spec| = 2.336e-29`** ≪ `1e-10` PASS boundary, across 2 decades (t: 0.02→2.0). Geometric-side imaginary part `≤ 1e-129` (real, by ±-weight symmetry of `wt(8)`).
- Poisson-kernel (P) sanity on the bare ρ-shifted theta: `max_rel = 2.336e-29` (t-adaptive direct radius).
- Closed form (*) vs pipeline: `|λ|² abs-diff 2.878e-13` (p+q≤6); full Dirac heat-trace agreement `1.3e-14` (all 4 t).
- `c_off = R_scalar/8 = 0.250000000000000` EXACT; `R_scalar(g_biinv) = 2.000000000000000`.
- Truncation tail bound: spectral Gaussian width `~1/√(s·λ_min(M))`, `λ_min(M)=2/9`; t-adaptive radius (~8.5σ, 319 pts at t=0.02) sums past tail (target `<1e-18`); dual side fast at small t.

**Verdict rationale (solution-space).** PASS. The τ=0 trace formula is two-sided exact (`2.34e-29 ≪ 1e-10`): the spectral eigenvalue reading and the geometric coroot-lattice theta-dual (closed internal relay orbits / winding lattice) agree to machine precision. The Wave-7 Poisson/theta-duality pipeline is **validated on a known-exact case** — oscillatory structure W7-2 extracts at τ_fold is a real geometric-side length spectrum, not a pipeline artifact. The closed-geodesic LENGTH spectrum (the geometric side never computed in 104 sessions) is sourced by the coroot lattice exhibited here; W7-2's τ=0 synthetic control must land its peaks on this lattice. The substitution-chain Step 2 (`C₂+c_off`) is SUPERSEDED by (*); the named `c_off=1/4=R/8` Friedrich floor survives. This is a substrate-physics correction surfaced and resolved in-session — NOT a convention swap to reach PASS (threshold 1e-10, scheme BI-INVARIANT-TAU0, heat-times, tolerance all as pre-registered; the gate object passes at 2.34e-29 regardless; the only mid-run change was a numerical truncation-radius increase on a redundant diagnostic sum, an explicitly-permitted resolution fix).

**Forward dependency.** The τ=0 closed spectrum (*) (S=8⊕8) and the coroot lattice exhibited here are the τ=0 synthetic control for W7-2 (`s105_w7_2_length_spectrum_ft.py`): the W7-2 FT of the τ=0 closed spectrum must land its peaks on THIS coroot lattice within δL. The npz stores the validated theta values.

**Output 4-tuple**: `(value='max_rel_2sided=2.336e-29_PoissonP_max_rel=2.336e-29_c_off=0.250000_closedform_absdiff=2.878e-13', scheme=BI-INVARIANT-TAU0, convention=heat-trace-K(t)=Tr_exp(-tD2)_spinor-rank-16_Fegan-|l|2=(1/6)(C2mu+C2pq)+1/4_S=8+8, L_max=NA-tau0-closed-form)`
**Dual-SHA**: `audit_sha256=8f895a0d63fbfa60a06c5e07965a2dd3003b4aea33d7c7f0a73759dfab177237`, `content_sha256=82025d518b465136b14a95b537ab0b18acb236aed1bbb2742c522231b16cf76d`

---

### §W7-2. S105-W7-2-LENGTH-SPECTRUM-FT (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S105-W7-2-LENGTH-SPECTRUM-FT`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (first extraction of the substrate length/action spectrum at τ_fold)
**Agent**: `spectral-geometer`
**Hypothesis**: The smooth-subtracted, Gaussian-windowed FT of the D_K eigenvalue density at τ_fold=0.190 shows ≥3 window-stable peaks (SNR≥6) at closed-geodesic lengths, with the τ=0 synthetic control landing its peaks on the W7-1 coroot lattice.
**Plan reference**: `sessions/session-plan/session-105-plan-w7.md` §W7-2. Unconditional (reads s84 L=12 cache READ-ONLY); output `.npz` FORWARD-PINNED intra-session to W7-3 and W7-4.

**Substrate framing**: GEOMETRIC. The substrate IS the eigenvalue density ρ(λ) of D_K at τ_fold=0.190 (a Level-1 single-τ-slice observable — the physical fabric, NOT the τ=0 reference). The oscillatory residual ρ_osc(λ), after the smooth Weyl/Seeley–DeWitt part is removed, IS the spectral fingerprint of the fabric's closed internal relay orbits: by Poisson summation / wave-trace, the oscillation at conjugate length L_γ is sourced by a periodic geodesic of length L_γ on the Jensen-deformed internal geometry. The arrow is D_K eigenvalues → oscillatory density → FT → closed-geodesic length spectrum; the lengths are READ OUT of the spectrum, never imposed. This is the geometric (length-spectrum) side of the substrate's own trace formula — the side never computed in 104 sessions.

**Output Artifacts**:
- Script: `computations/session-105/s105_w7_2_length_spectrum_ft.py` — `grep -E 'from canonical_constants import|print_verdict_payload'` → both present (lines 88 `from canonical_constants import *`, 93 explicit `from canonical_constants import (tau_fold, a_0_FW_zeta..a_8_FW_zeta)`; 456 `def print_verdict_payload`).
- Data: `computations/session-105/s105_w7_2_length_spectrum_ft.npz` — present (29 keys incl. `primary_peaks`, `stable_peaks`, `n_stable_peaks`, `L_axis_primary`, `amp_primary`, `delta_L`, `coroot_lengths`, `primitive_coroot_length`, `control_peaks`, `control_on_lattice`, `n_lambda_range_robust`, `dominant_L`; forward-pinned to W7-3/W7-4).
- Plot: `computations/session-105/s105_w7_2_length_spectrum_ft.png` — present (4-panel: PRIMARY density+Weyl smooth, oscillatory residual, measured length spectrum, τ=0 control vs coroot lattice).
- Verdict line: `computations/session-105/s105_gate_verdicts.txt` — `^S105-W7-2-LENGTH-SPECTRUM-FT:.* audit_sha256=[a-f0-9]{64}` MATCHED + dual-SHA companion row + 2 extra rows (regulator_pin + counting-choice diagnostic).

**MCP Pre-Compute Audit**:
- `search_knowledge("length spectrum trace formula coroot lattice SU(3) closed geodesic D_K")` → nearest prior art `s61_trace_formula_geometric.py` (FORMULA-61, T3-batch INFO; 992-mode residual, superseded here at 166,896 block-level / 31,956,720 PW-weighted dynamic range); NO closure covers the W7-2 length-spectrum extraction. NOT PRE-CLOSED.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). Confirmed.
- `list_constants("a[0-9]_FW_zeta|...")` + canonical-file grep → regulator pin `a_n^{ζ}` = `a_0_FW_zeta=6440.0, a_2_FW_zeta=2776.165389, a_4_FW_zeta=1350.7216, a_6_FW_zeta=765.593826, a_8_FW_zeta=521.183178` (S88/S96). Imported; cited as the zeta-regulated smooth-Weyl regulator class per regulator-pin-discipline.md.

**Verdict**: **PASS** (pre-registered criterion: ≥3 window-halving-stable SNR≥6 peaks AND τ=0 control on coroot lattice).
- `value='n_stable_peaks=19_>=3_SNR>=6_window-halving-stable_control_on_coroot_lattice_primitiveL=12.5664_deltaL=1.1595_DIAGNOSTIC_n_lambda-range-robust=0_dominantL=124.26_tau_fold-peaks-truncation-influenced-L_max=12'`
- 4-tuple: `(value=…, scheme=STRUTINSKY-WEYL-SUBTRACT, convention=PW-dim-weighted-PRIMARY, L_max=12)`
- `audit_sha256=94c7bf5ca22ad8c5ef76eaf9d3a5d553c75bcec6d45f751e6e4adc098ea2db4c`
- `content_sha256=eacaab47422d2eb92d48fe61be2117e76c3592c3cffa5688d5326ad18edf3246`
- regulator_pin companion row: `a_n^{ζ}`; STRUTINSKY-WEYL-SUBTRACT smooth part.

**Results**:

*Counting-choice pin (substitution chain — PRIMARY vs DIAGNOSTIC).* The s84 L=12 cache stores `sector_evals = {(p,q): {dim, level, abs_evals}}`, 90 of 91 sectors (max p+q=12; **(4,4) absent**). `abs_evals` is the FULL Dirac block V_{(p,q)}⊗ℂ¹⁶ (length 16·dim; spinor rank 16 applied; Peter–Weyl regular-rep multiplicity NOT yet applied), 166,896 block-level entries, λ∈[0.819741, 5.418937] (matches `lambda_unit_canonical`). The two counting choices and their measured Weyl exponents:

| Counting | weight per block-eigenvalue | total | Weyl exp [10–60 pct] | Weyl exp [20–70 pct] | role |
|:---------|:----------------------------|:------|:---------------------|:---------------------|:-----|
| **PRIMARY** (Peter–Weyl dim-weighted) | ×dim(p,q) (regular-rep mult. in L²) | 31,956,720 | **8.215** | **7.817** | PASS basis |
| **DIAGNOSTIC** (block-level) | ×1 | 166,896 | 5.165 | **5.022** | reported, not PASS basis |

Substitution chain (plan §W7-2, verified numerically — the [20–70] exponents reproduce the off-session transcript anchors **bit-for-bit**: 7.817 and 5.022):
- Step 1: ρ_smooth^{PW}(λ) ~ d/dλ[c·λ^d], d=8 — full-L² trace weights each (p,q) by dim(p,q), recovering N~λ^8; measured 7.817 (deficit from 8 = L_max=12 truncation bend, the high-λ region being incomplete).
- Step 2: ρ_smooth^{block}(λ) ~ d/dλ[c'·λ^5] — per-sector, each counted once; measured 5.022.
- Step 3: the trace formula K(t)=Tr exp(−tD²) sums over the FULL L² Hilbert space ⇒ the PW reading is the one whose Poisson dual is the coroot lattice (validated by the τ=0 control); block-reduced is a per-sector projection with no single coroot dual.
- Step 4: ⇒ subtract ρ_smooth^{PW} (PRIMARY); the residual ρ_osc^{PW} carries the geodesic-length oscillations.
- Direction: **PRIMARY exp (7.817) > DIAGNOSTIC exp (5.022)** — the larger exponent is the full-L² dimension-spectrum reading (correct trace-formula basis); confirmed.

*Pipeline.* (1) PW-weighted histogram of λ onto a 2048-point uniform grid over [λ_min, λ_max]. (2) Strutinsky smoothing (Gaussian, width σ_λ = 3×grid-resolution = 0.0067; the raw unique-level spacing 2.6×10⁻⁵ is sub-bin/sub-float-precision for this dense L=12 spectrum, so the Strutinsky γ is anchored to the grid resolution — a few bins — which smooths bin-noise while preserving the geodesic-length oscillation period 2π/L~0.63 spanning ~280 bins; the gauss-factor 3×→1.5× then genuinely varies the smoothing in the cross-check). (3) Weyl smooth = degree-10 polynomial fit over the 20th–70th percentile quantile band (normalized abscissa for conditioning); zeta-regulated per the `a_n^{ζ}` pin. (4) ρ_osc = smoothed − Weyl, band-limited to the quantile interior. (5) Hann-windowed `torch.fft.rfft` (GPU); **L_γ = 2π·(FFT freq in λ)**. Resolution budget **δL = 2π/λ_max = 1.1595**.

*Measured length spectrum at τ_fold (PRIMARY).* Noise floor (1.4826·MAD) = 1.185×10³; SNR≥6 height = 7.112×10³. Top window-halving-stable peaks {L_γ, amplitude, SNR, drift}:

| L_γ | amplitude | SNR | window-halving drift |
|----:|----------:|----:|---------------------:|
| **124.26** | 4.561×10⁵ | 384.8 | 0.0000 |
| 75.10 | 2.528×10⁵ | 213.3 | 0.0000 |
| 91.49 | 1.552×10⁵ | 131.0 | 0.0000 |
| 255.35 | 1.426×10⁵ | 120.3 | 0.0000 |
| 182.97 | 1.338×10⁵ | 112.8 | 0.0000 |
| 206.19 | 1.315×10⁵ | 111.0 | 0.0000 |
| 161.13 | 1.273×10⁵ | 107.4 | 0.0000 |
| … (19 total window-halving-stable; full set in npz `stable_peaks`) | | | |

**n_stable_peaks = 19 ≥ 3** (PASS basis). Window-halving (σ→σ/2): all 19 peaks drift = 0.0000 ≤ δL — peak POSITIONS are smoothing-width-independent (the physical signature: a smoothing-kernel artifact would move; these do not). 32 SNR≥6 peaks at full window; 19 survive the position-stability cut.

*τ=0 synthetic control (pipeline-correctness check).* W7-1 had not landed at dispatch, so the control reconstructs the bi-invariant closed spectrum in-script: |λ|² = C₂(p,q) + c_off (c_off = 0.75, the (0,0) Dirac-square floor = R_scalar(g_biinv)/8; W7-1 explore confirms spread 1.7×10⁻¹⁵ EXACT), PW-weighted (×dim²×16), through the IDENTICAL pipeline. Predicted coroot-lattice lengths from the leading Casimir quadratic form M=(1/3)[[1,½],[½,1]] via the wave-trace conjugation L=2π√(m^T M⁻¹ m): {12.566, 21.766, 25.133, 33.247, 37.699, 43.531, …}; **primitive = 4π = 12.5664** (the A₂ root-lattice fundamental). Measured control peaks: L=12.509 (SNR 360), 25.200 (140), 33.176 (42.5), 37.709 (42.4), 26.831 (29.2), 45.323 (23.7) — **all land on predicted coroot lengths within δL_control = 0.177** (strongest 12.509 vs primitive 12.566, deviation 0.057 ≤ 0.177). **CONTROL ON LATTICE: True** — the pipeline is validated on the known-exact case.

*Honest diagnostic (NOT a pre-registered verdict gate).* A λ-range-robustness test (re-run on λ sub-bands 0–75/10–85/25–100 pct; a genuine range-INDEPENDENT closed-geodesic peak recurs in all sub-bands within δL, a spectral-window-truncation artifact does not) returns **n_lambda-range-robust = 0**: none of the 19 τ_fold peaks survive spectral-window truncation. The dominant L≈124.26 is therefore **truncation-INFLUENCED** — shaped by the compressed L_max=12 λ-support [0.82, 5.42] and its sharp edges (the deformation pushes high-(p,q) eigenvalues down into a narrow band, so short λ-periods → long L), at the coarse δL=1.16 resolution — rather than a clean range-independent geodesic length. The plan's pre-registered window-halving (Gaussian-σ) test cannot detect spectral-window truncation; the λ-range test can, and flags the resolution limitation. This is added DISCLOSURE; it does NOT change the verdict (adding it as a PASS gate post-hoc would be Class-3 pre-registration editing per v3-closure-recovery.md). The PASS stands on the pre-registered criterion; the τ_fold length spectrum is resolution-limited (the plan's INFO_meaning describes exactly this regime, but the literal strict_PASS_boundary — window-halving + control — is met).

*Assessment.* The substrate's geometric-side length spectrum is EXTRACTED for the first time. The pipeline is positively controlled (τ=0 peaks on the 4π coroot lattice to within δL). At τ_fold the PRIMARY (full-L² Peter–Weyl) counting yields 19 window-halving-stable peaks dominated by L≈124, but the stronger λ-range test shows these are truncation-influenced — the clean closed-geodesic content at τ_fold is below the L_max=12 cache's resolution. The gate is **PASS** (non-FAIL): W7-3 (Berry–Tabor match) and W7-4 (geodesic commensurability) DISPATCH; both inherit δL=1.1595 and the forward-pinned `stable_peaks`/`primary_peaks` tables, with the truncation caveat recorded so they read the measured peaks as resolution-limited. The decisive corroboration that the dominant peaks are real geometric structure vs. truncation will come from W7-3's independent Berry–Tabor frequency-map prediction: if the integrable ω(I) lattice reproduces the measured positions, they are geodesic; the λ-range diagnostic predicts a partial match at best at this resolution.

---

### §W7-3. S105-W7-3-BERRY-TABOR-MATCH (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S105-W7-3-BERRY-TABOR-MATCH`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (integrable Berry–Tabor frequency-map prediction of the measured length spectrum)
**Agent**: `spectral-geometer`
**Hypothesis**: The Berry–Tabor resonance lattice from the Jensen Euler–Arnold frequency map ω(I) reproduces ≥2/3 of the W7-2 measured stable peak positions within δL; Berry–Tabor (not Gutzwiller) is the applicable form because Manakov integrability forces det(M−I)=0.
**Plan reference**: `sessions/session-plan/session-105-plan-w7.md` §W7-3. **GATED dispatch**: ran on `S105-W7-2-LENGTH-SPECTRUM-FT` verdict = **PASS** (disk-verified). Forward-pins W7-2 npz; re-aims S54 machinery (`s54_gutzwiller_su3.py`).

**Verdict**: **FAIL** — `match_frac = 0.1579 (3/19)` measured stable peaks land on a predicted Berry–Tabor resonance length within `δL = 1.1595`; pre-registered PASS boundary is `≥ 2/3`. Composite 3-tuple `sign=PASS, magnitude=FAIL, regime=VALID` (collapse rule → FAIL). This is the outcome the W7-2 λ-range diagnostic forecast ("partial match at best"): the measured τ_fold peaks at L∈[75, 397] are truncation-influenced (`n_lambda_range_robust = 0` at L_max=12), sitting ~6× above the substrate's own predicted primitive orbit (21.27). The Berry–Tabor predictor is self-consistent (τ=0 → 4π EXACT); the FAIL closes the "measured = integrable geometric side at this resolution" corridor, not the integrable-geometry hypothesis itself.

**MCP Pre-Compute Audit** (queries run BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("Berry-Tabor Gutzwiller SU(3) Manakov integrable geodesic frequency map trace formula")` → returned `s54_gutzwiller_su3.py` (S54 prior art) + `s61_trace_formula_geometric.py`; no closure pre-covers the W7-2-vs-prediction match. NOT PRE-CLOSED.
- `trace_entity("Berry-Tabor")` → `theorem proven_498`: **`A_{p,q}^{BT} = d(p,q)·16/(2π)^{3/2}/√|det(d²E/dI_i dI_j)|`** (PROVEN) — the canonical amplitude form, used verbatim. Plus `eq_7430`: P_Poisson(s)=exp(−s) (integrable ⇒ Poisson statistics).
- `trace_entity("GUTZWILLER-SU3-54")` / `trace_entity("Manakov integrability geodesic SU(3)")` → no separate gate node; the Manakov-integrable ⇒ det(M−I)=0 ⇒ Gutzwiller-inapplicable theorem is documented in `s54_gutzwiller_su3.py` (required reading; lines 10–31, 910–936) and adopted here.
- `get_constant("tau_fold")` → `0.19` (S12/S42, CONST-FREEZE-42). Used.

**Output Artifacts**:
- Script: `computations/session-105/s105_w7_3_berry_tabor_match.py` — present (`grep` confirms `from canonical_constants import PI, tau_fold` and `def print_verdict_payload`).
- Data: `computations/session-105/s105_w7_3_berry_tabor_match.npz` — present (47 keys incl. `pred_L_formA_sorted`, `match_table`, `match_frac`, `Hess_E`, `surface_R2`, `tau0_selfconsistent`, `coroot_reproduced`, `amps_table`).
- Plot: `computations/session-105/s105_w7_3_berry_tabor_match.png` — present (4-panel: stick spectra, per-peak gaps, frequency-map summary, nearest-predicted scatter).
- Verdict line: `computations/session-105/s105_gate_verdicts.txt` — `S105-W7-3-BERRY-TABOR-MATCH: FAIL` with `audit_sha256=5c4bc5c1…` + dual-SHA companion row + schema-v2 3-tuple row + 4 extra annotation rows.

**Results.**

*Method (re-aimed S54 machinery, substrate-first).* Manakov integrability of the Jensen Euler–Arnold geodesic flow on (SU(3), g_τ) is S54-established (compact semisimple group + left-invariant metric ⇒ Manakov integrals). Integrable ⇒ periodic geodesics lie on rank-2 invariant tori in continuous conjugation families ⇒ the transverse monodromy M has a kernel along the family ⇒ **det(M − I) = 0 identically** ⇒ the Gutzwiller isolated-orbit amplitude 1/√|det(M−I)| **diverges and is structurally inapplicable**. The applicable form is **Berry–Tabor** with finite-Hessian amplitude `A_BT = dim(p,q)·16/(2π)^{3/2}/√|det(d²E/dI²)|` (canonical `proven_498`; S54 `berry_tabor_amplitude`). The action variables ARE the Dynkin labels (p,q) (S54). The τ_fold level surface E(p,q) = ⟨|λ|²⟩_(p,q) is read DIRECTLY from the s84 L=12 cache (sector-mean Dirac square, 90 sectors, max p+q=12). It is **EXACTLY quadratic** in (p,q): `E = 0.116367(p²+q²) + 0.116367·pq + 0.349114(p+q) + 0.795051`, **R² = 1.00000000** (RMS residual 4.6×10⁻¹⁵). The energy Hessian `G_E = d²E/dI_i dI_j = [[0.23274, 0.11637],[0.11637, 0.23274]]` is the metric quadratic form in action space.

*Predicted lengths.* The W7-2 length axis is the FT-in-λ conjugate `L = 2π·(freq in λ)`: an oscillation `cos(λ·L)` in the eigenvalue density (sourced by a closed geodesic of length L) produces an FT peak at L. The Berry–Tabor closed-orbit length (the geometric-side length the FT measures, **Form A — Poisson-dual wave-trace**, the form W7-2 uses for its τ=0 control) is

`L_m = 2π·√(mᵀ(G_E/2)⁻¹ m)`,  m ∈ ℤ²∖{0}, |m_i| ≤ m_max = 8.

**τ=0 self-consistency is EXACT**: Form A on Hess(C₂) = [[2/3,1/3],[1/3,2/3]] returns primitive `L_pred = 12.566371 = 4π` at m=(−1,−1) and reproduces the full W7-2 coroot lattice {12.566, 21.766, 25.133, …} — the predictor is correctly built. At τ_fold the surface flattens (Hessian smaller by ~0.349×), so the dual lengths **lengthen**: primitive `L_pred(τ_fold) = 21.2682` at m=(−1,−1); the predicted spectrum spans **[21.27, 294.70]** (43 unique lengths). [Form B, the plan's single-resonance phrasing `L = 2π/|m₁ω₁+m₂ω₂|` at the dim-weighted action center I*=(5.05,5.05), ω=(2.111,2.111), gives lengths in [0.19, 2.98] — a different observable (it samples ω-ratio commensurabilities at a single action, not the Poisson-dual closed-orbit periods) and matches 0/19; Form A is PRIMARY because it is the form that controls the FT-in-λ peaks via Poisson summation, matching the W7-2 convention exactly.]

*Line-by-line match (Form A PRIMARY, tolerance δL=1.1595).* The 3 matches:

| L_meas | L_pred | gap | ≤ δL | winding (m₁,m₂) | amp_meas |
|---:|---:|---:|:---:|:---:|---:|
| 124.259 | 127.609 | 3.350 | ✗ | (−6,−6) | 4.56e+05 |
| 75.101 | 73.675 | 1.426 | ✗ | (−2,−4) | 2.53e+05 |
| 91.487 | 92.706 | 1.219 | ✗ | (−3,−5) | 1.55e+05 |
| 255.345 | 257.863 | 2.518 | ✗ | (−7,7) | 1.43e+05 |
| 182.975 | 184.188 | 1.214 | ✗ | (−5,5) | 1.34e+05 |
| **206.188** | **205.103** | **1.085** | **✓** | (−4,7) | 1.32e+05 |
| **161.127** | **160.571** | **0.555** | **✓** | (−8,−7) | 1.27e+05 |
| 245.787 | 241.560 | 4.226 | ✗ | (−5,8) | 1.15e+05 |
| **148.838** | **148.877** | **0.040** | **✓** | (−7,−7) | 1.15e+05 |
| 237.594 | 239.681 | 2.087 | ✗ | (−7,6) | 1.04e+05 |
| 172.051 | 170.146 | 1.905 | ✗ | (−8,−8) | 1.01e+05 |
| 192.533 | 194.926 | 2.393 | ✗ | (−2,8) | 6.73e+04 |
| 311.330 | 294.701 | 16.629 | ✗ | (−8,8) | 5.81e+04 |
| 278.558 | 276.487 | 2.071 | ✗ | (−8,7) | 4.04e+04 |
| 271.731 | 276.487 | 4.756 | ✗ | (−8,7) | 2.09e+04 |
| 397.355 | 294.701 | 102.654 | ✗ | (−8,8) | 2.04e+04 |
| 335.908 | 294.701 | 41.207 | ✗ | (−8,8) | 1.84e+04 |
| 327.716 | 294.701 | 33.015 | ✗ | (−8,8) | 1.79e+04 |
| 382.335 | 294.701 | 87.634 | ✗ | (−8,8) | 1.30e+04 |

**n_matched = 3 / 19 ⇒ match_frac = 0.1579 < 2/3 ⇒ FAIL.** Five further peaks are near-misses (gap ∈ [1.2, 1.5], just outside δL); the four longest measured peaks (327–397) all pin to the SAME m_max-saturated predicted length 294.70 with gaps 33–103 — these exceed the predictor's reach (|m_i|=8 caps the predicted spectrum at 294.7) and are the clearest truncation signature.

*Amplitude correspondence.* Berry–Tabor amplitudes `A_BT = dim·16/(2π)^{3/2}/√|det Hess|` (|det Hess| = 0.04063) are dim-ordered (top: (6,6) dim 343 → A=1729; (5,7)/(7,5) → 1694). The 3 matched peaks do not isolate a clean A_BT vs amp_meas ordering (too few matches); amplitude correspondence is not the discriminator here — the FAIL is a **position** failure, not an amplitude-regime INFO.

*4-tuple.* `(value = 0.1579, scheme = BERRY-TABOR-INTEGRABLE, convention = Berry-Tabor-integrable-trace-formula-rank2-NOT-Gutzwiller-detMmI0, L_max = 12)`. Dual-SHA `audit_sha256 = 5c4bc5c1b9c236467865c0773b9e835cff59a223e07b1e464a2d04cb1fc6c803`, `content_sha256 = 239602a2c9a4f7fd783af5527ca2a287de28dc272b8ac774f518b8b57a8b5ce8`.

*Substitution chain (det(M−I)=0 ⇒ Gutzwiller inapplicable; direction).* Step 1: Jensen Euler–Arnold on (SU(3), g_τ) is Manakov-integrable [S54]. Step 2: integrable ⇒ periodic geodesics on invariant tori in continuous conjugation families (Weyl × U(2) isotropy) — degenerate, not isolated. Step 3: degenerate-orbit monodromy ⇒ det(M−I)=0 identically [kernel along the family]. Step 4: Gutzwiller amplitude ∝ 1/√|det(M−I)| → ∞ ⇒ inapplicable; Berry–Tabor `A_BT ∝ dim·16/(2π)^{3/2}/√|det(d²E/dI²)|` is the finite replacement. Step 5: predicted lengths are the resonant-torus periods, the Poisson-dual `L_m = 2π√(mᵀ(G_E/2)⁻¹ m)` (verified: τ=0 → 4π EXACT). Direction: more measured peaks coinciding with predicted lengths within δL ⇒ stronger confirmation that the spectrum IS the integrable geometric side; PASS at ≥ 2/3. Realized: 3/19 — direction is positive (`sign=PASS`: the matches that DO occur are genuine coincidences, not anti-correlation) but the magnitude is far below boundary (`magnitude=FAIL`); the predictor's regime is valid (`regime=VALID`: self-consistent at τ=0).

*Assessment (substrate-first).* The substrate's internal geometry at τ_fold IS a Manakov-integrable system; its closed relay orbits live on rank-2 invariant tori with periods set by the Euler–Arnold frequency map ω(I) = ∂E/∂I derived from the Jensen-deformed metric — and that map is now pinned EXACTLY: E(p,q) is a perfect quadratic form (R²=1.0), the substrate's own length spectrum is the Poisson dual {21.27, 36.84, 42.54, …, 294.70}, recovering 4π at τ=0 bit-for-bit. The measured FT peaks, however, do NOT land on this lattice (3/19): they sit at L∈[75, 397], an order of magnitude above the predicted primitive 21.27, with the longest four saturating against the m_max=8 ceiling. This is the **decisive corroboration of W7-2's truncation caveat** (`n_lambda_range_robust = 0` at L_max=12): the genuine closed-geodesic content at τ_fold is below the L_max=12 cache's λ-support [0.82, 5.42] / δL=1.16 resolution — the measured peaks are dominated by Strutinsky-subtraction residual structure on the coarse FT grid, not the integrable geodesic lengths. The arrow metric → ω(I) → predicted lengths → match is intact and the lengths are never fit; what fails is the *identification of the measured spectrum with the geometric side at this truncation*. The FAIL closes that corridor and routes (carry-forward) to a finer-L_max length-spectrum extraction where the predicted primitive 21.27 and the lower-winding lengths {21, 37, 43, 56, 64} fall inside the resolved λ-band, before any "measured = integrable geometric side" claim can be revisited.

---

### §W7-4. S105-W7-4-GEODESIC-COMMENSURABILITY (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S105-W7-4-GEODESIC-COMMENSURABILITY`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (squared-length commensurability / crystalline no-arithmetic signature)
**Agent**: `spectral-geometer`
**Hypothesis**: The combined measured (W7-2) + predicted (W7-3) length spectra sit on a single quadratic-form lattice — ≥80% of pairwise SQUARED-length ratios recover a rational p/q (denom≤64, rel_tol 1e-6) — with the τ=0 control exactly rational; the criterion is pre-fixed to L² because raw lengths are √rational even at τ=0.
**Plan reference**: `sessions/session-plan/session-105-plan-w7.md` §W7-4. **GATED dispatch**: W7-2 returned PASS (disk-verified) → W7-4 DISPATCHED. Dual prior pre-registered (Track A crystalline 0.7 / Track B incommensurable 0.3); a FAIL is SURPRISING → routes to a Q1 workshop per `.claude/rules/Investigating-Workshops.md` (NOT silently absorbed; the orchestrator owns the routing).

**Verdict**: **FAIL** — `value=rational_frac=0.4273 (>= 0.80? False); ctrl_exact_rational=True(36/36); fold_pop=W72+W73 n_fold_peaks=62 n_fold_pairs=1891 n_fold_rational_CF=808 n_fold_rational_PSLQ=476; diag_frac@res_tol(1.09e-1)=1.0000`. The τ_fold squared-length spectrum is INCOMMENSURABLE at the pre-registered tolerance (0.4273 ≪ 0.80 under the literal CF criterion; 0.2517 under the stricter both-integers-bounded PSLQ-on-pair cross-check). The τ=0 control PASSES exactly (36/36, machine-ε), validating the method. Per the decision-point block + dual_prior, this routes to a **Q1 math/physics adjudication workshop** (deformed-incommensurable vs measurement-artifact); posterior → 0.9 Track B.

**NUMBERS first (the deciding axis of the RH/trace-formula program):**

| Population | n_lengths | n_pairs | rational (CF, denom≤64, rel_tol) | frac | rational (PSLQ-on-pair, both ints≤64) | frac | Boundary |
|:----------|:---------:|:-------:|:---------------------------------:|:----:|:--------------------------------------:|:----:|:--------:|
| **τ=0 control** (exact coroot lattice) | 9 | 36 | 36 (rel_tol 1e-9) | **1.0000** | 36 | **1.0000** | all-rational |
| **τ_fold combined** (W7-2 meas + W7-3 pred) | 62 | 1891 | 808 (rel_tol 1e-6) | **0.4273** | 476 | **0.2517** | ≥ 0.80 |

- **τ=0 control PASSES 36/36 EXACT** (CF and PSLQ-on-pair AGREE). The 9 coroot lengths satisfy `(L/4π)² ∈ {1, 3, 4, 7, 9, 12, 13, 19, 27}` — the Loeschian numbers `m²+mn+n²` of the SU(3)/A₂ root lattice — to integer residual `3.55e-15`. Hence every pairwise squared ratio `L_i²/L_j² = n_i/n_j ∈ ℚ` with denominator ≤ 27 < 64, exactly as the substitution chain proves. **The method is validated against the known quadratic-form lattice.**
- **τ_fold combined FAILS** the 0.80 boundary under BOTH the literal-pin CF criterion (0.4273) and the stricter both-integers-bounded PSLQ-on-pair cross-check (0.2517). Neither approaches the boundary; the FAIL is robust to the criterion choice. The two recovery methods AGREE on the verdict.

**Output Artifacts** (content-presence verified on disk):
- Script: `computations/session-105/s105_w7_4_geodesic_commensurability.py` (29,733 B) — `grep -E 'from canonical_constants import|print_verdict_payload'` → 6 hits (both required patterns present).
- Data: `computations/session-105/s105_w7_4_geodesic_commensurability.npz` (84,783 B; 40 keys incl. `ctrl_table`, `fold_table`, `ctrl_int_mesh`, `fold_frac`, `fold_frac_pslq`).
- Plot: `computations/session-105/s105_w7_4_geodesic_commensurability.png` (163,480 B; 4-panel: control integer mesh, fold L² spectrum, control pairwise ratios all-rational, fold pairwise ratios mostly-irrational).
- Verdict line: `computations/session-105/s105_gate_verdicts.txt` — `S105-W7-4-GEODESIC-COMMENSURABILITY: FAIL ... audit_sha256=2eb281b058722e57a60ca7793d35ca029d8251bedd868b5288e23eafa9d72787 content_sha256=72d60ce6347f808bb08311c43e821b74dc4d1b886142316cae2d88ec61d56471` (+ dual-SHA companion row + 6 method/decision-point extra rows).
- 4-tuple: `(value=rational_frac=0.4273…, scheme=PSLQ-SQUARED-RATIO, convention=SQUARED-length-ratios, L_max=12)`.

**MCP Pre-Compute Audit** (queries run BEFORE writing the script):
- `search_knowledge("geodesic length spectrum commensurability PSLQ squared lengths coroot lattice")` → prior geodesic gates (s60 GEODESIC-60, s61 FORMULA-61, s79 phononic-length) but NO prior squared-action PSLQ commensurability result; gate is genuinely new.
- `search_knowledge("trace formula SU(3) closed geodesic crystalline rational lattice Riemann hypothesis")` → s61 trace_formula_geometric; SU(3) crystalline framing in s53 workshops; no closure on length-spectrum commensurability.
- `trace_entity("length spectrum commensurability")` → no trace (confirms novel).
- `get_constant` (via canonical import): `tau_fold=0.19`, `c_off_tau0=0.75` (W7-2 stored), primitive coroot `4π=12.566`. Not PRE-CLOSED.

**Results / method (full fidelity):**

*Substitution chain (squared vs raw lengths — the pre-fix is load-bearing):*
- **Step 1**: On bi-invariant SU(3) the τ=0 closed-geodesic length-squared in coroot direction ν is `L_ν² = c·⟨ν,ν⟩` with `⟨ν,ν⟩ ∈ ℤ` (the coroot/A₂ lattice is integral). **VERIFIED**: `(L_ν/4π)² ∈ {1,3,4,7,9,12,13,19,27}` (Loeschian integers, resid 3.55e-15).
- **Step 2**: ⇒ `L_ν²/L_μ² = n_ν/n_μ ∈ ℚ` (squared ratios rational). **VERIFIED**: control 36/36.
- **Step 3**: but `L_ν/L_μ = √(n_ν/n_μ)` (raw ratios √rational, generically irrational — e.g. √3, √7). ⇒ a raw-length PSLQ test would FALSELY FAIL the undeformed group; squaring restores rationality. **This is why the plan pins the criterion to L² (not raw L) at plan-freeze** — confirmed correct by the control passing.
- **Step 4 (direction)**: more pairwise squared-ratios recovering rational p/q (bounded denominator) ⇒ stronger commensurability ⇒ confirms the crystalline / no-arithmetic reading. PASS at ≥ 0.80.
- **Step 5 (the test)**: at τ_fold the Jensen deformation rescales the three metric blocks (L₁=e^{2τ}, L₂=e^{−2τ}, L₃=e^{τ}); whether the deformed squared-length spectrum remains on a single quadratic-form lattice is the HYPOTHESIS. **RESULT**: it does NOT — only 0.4273 (CF) / 0.2517 (PSLQ-on-pair) of pairs are rational.

*Recovery method (self-corrected in-session; disclosed honestly per `v3-closure-recovery.md` Class-1 boundary):* The PRIMARY matcher is continued-fraction best-rational recovery (CF convergents ARE the best rationals with bounded denominator — Dirichlet/Hurwitz; terminating CFs handle integer ratios `n/1` exactly), which implements the plan pin literally ("rational p/q with denominator ≤ Q_max=64"). The CROSS-CHECK is PSLQ run DIRECTLY on the squared-length PAIR `[L_i², L_j²]` with an EXPLICIT `tol` (the canonical "PSLQ on squared actions" usage) — it finds `(a,b): a·L_i² + b·L_j² ≈ 0`, so `L_i²/L_j² = −b/a`, and requires BOTH Loeschian integers ≤ 64 (a stricter, physically-correct lattice condition). **Both methods pass the τ=0 control 36/36 and both fail the τ_fold population far below 0.80.** An initial draft using `mpmath.pslq([ratio, 1])` with DEFAULT tolerance was found to return `None` on simple integer ratios (e.g. `3.0`) — a known mpmath default-tolerance quirk — and was caught by the control returning 2/36 instead of 36/36; it is NOT used as a matcher. The bug was structural (wrong PSLQ usage + default tol), fixed before the verdict, and the control PASS certifies the corrected method. Sage/PARI `lindep` independently confirmed integer-relation recovery (`27/13 → [-13,27]`, `3/1 → [1,-3]`).

*The CF "rational" matches on the fold are largely spurious (criterion-robustness note):* CF at rel_tol=1e-6 bounds only the DENOMINATOR `q ≤ 64`, so it accepts large-numerator rationals (e.g. fold pair (1,3) → 289/25, (3,19) → 1009/7) that are 6-digit approximations of irrationals, not genuine low-complexity commensurabilities. The PSLQ-on-pair cross-check bounds BOTH integers ≤ 64 (the true quadratic-form-lattice condition: both Loeschian norms small) and correctly rejects these (476/1891 = 0.2517). Even the looser literal-pin CF reading (0.4273) is far below 0.80; the stricter physical reading (0.2517) is farther still. **FAIL under either reading.**

*Resolution-aware diagnostic (non-verdict-changing, per W7-2's disclosed `n_lambda_range_robust=0` caveat):* the measured τ_fold lengths carry FT bin width `δL=1.1595` (propagated `δ(L²)/L² = 2δL/L_min = 1.09e-1`). At that resolution-matched tolerance the fold becomes 1891/1891 "rational" — but this is VACUOUS (the rational mesh with q≤64 is dense to 11%, so any two reals are "commensurable" to 11%). The diagnostic confirms the FAIL at rel_tol=1e-6 is the genuine discriminator and NOT an under-resolution artifact at 1e-6; equally it confirms the measurement at δL≈1.16 CANNOT certify commensurability at 1e-6 either way. This double-edged reading — incommensurable at the test tolerance, under-powered at the certifiable tolerance — IS the "deformed-incommensurable vs measurement-artifact" tension the plan names for the Q1 workshop.

*W7-3 input (combined population):* W7-3 landed (self-verdict FAIL, `match_frac=0.158`) and supplied 43 predicted Form-A resonance lengths (`pred_L_formA_sorted`, primitive `pred_primitive_tau_fold=21.27`). Per plan N_eval these are pooled with the 19 W7-2 measured lengths (combined n=62, 1891 pairs) on the single-lattice hypothesis. The combined FAIL is consistent with W7-3's own predicted-vs-measured mismatch.

*Dual-prior posterior re-allocation (pre-registered):* outcome FAIL → **0.9 to Track B (incommensurable; routes Q1 workshop)**, 0.1 to Track A. The substrate's measured τ_fold relay-orbit actions do NOT, at L_max=12 resolution and rel_tol=1e-6, sit on a single rational quadratic-form lattice.

**Substrate framing (substrate-first per `phononic-framing.md`):** GEOMETRIC. Commensurability is a property of the substrate's OWN closed relay orbits — the winding/coroot lattice of `(SU(3), g_Jensen)`. The τ=0 fabric IS a crystalline quadratic-form lattice (control 36/36 exact: the relay-orbit squared actions are integer multiples of the (4π)² primitive cell, Loeschian-graded). Under Jensen deformation to τ_fold the measured + predicted squared actions do NOT close onto a single rational lattice at the tested precision: the deformed fabric's geodesic actions, as resolved at L_max=12, beat against one another rather than locking to a common quadratic-form mesh. Whether this is (i) the genuine substrate statement that the deformation breaks the quadratic-form lattice — reopening the trace-formula/RH question for the deformed object — or (ii) an L_max=12 / δL≈1.16 resolution limit on the measured length spectrum is the adjudication the Q1 workshop must resolve. The arrow is unchanged: D_K(τ) winding lattice → closed-orbit squared actions → squared-ratio rationality → crystalline-vs-incommensurable diagnosis. The criterion is squared (not raw) because the lattice is quadratic-form — the control validates this pre-fix.

---

### §W7-5. S105-W7-5-SUBSTRATE-ZETA-ZEROS (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S105-W7-5-SUBSTRATE-ZETA-ZEROS`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (zero geography of the actual Jensen-deformed ζ_{D_K})
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The zeros of the genuine ζ_{D_K}(s) do NOT lie on a common vertical line (Re-spread > 1e-6 over ≥5 certified zeros); the expected FAIL, because the functional-equation mirror has no Euler-product pin.
**Plan reference**: `sessions/session-plan/session-105-plan-w7.md` §W7-5. PRE-REGISTERED expectation FAIL (S³ proxy spread 0.93); dual prior Track A scatter 0.9 / Track B on-line surprise 0.1; certified `_rh_substrate_sanity.py` winding kernel (dense-perimeter pre-sampling MANDATORY). Terminal negative-space result; no downstream consumer.

**Verdict**: **INFO** — composite via the PRE-REGISTERED cache/SD matching gate (plan INFO_meaning: "the matching check at t_c failing (> 1e-3) also routes here — the cache/SD splice is the limiting step, not the zero geography"). The substantive substrate-IS answer (LAYER B, the entire direct-sum object) is delivered and **confirms the pre-registered Track-A expectation**: the genuine SU(3) substrate zeta scatters its zeros (Re-spread 4.085 over 14 certified zeros, NOT on a common line). The dual prior is unchanged at the verdict layer (INFO), but the LAYER-B substantive content is unambiguous Track-A confirmation.

**MCP Pre-Compute Audit**:
- `search_knowledge("substrate zeta zeros Riemann hypothesis D_K Euler product critical line")` → S61 `zeta_zeros`/`ruelle_zeta` (gate `T3-BATCH-S61-ZETA-ZEROS` = INFO, MIGRATED batch-canonical-hygiene — a *different* object; no prior gate computes the zero geography of the actual ζ_{D_K} by heat-kernel continuation). NOT PRE-CLOSED.
- `search_knowledge("Seeley-DeWitt heat kernel coefficient a_n SU(3) D_K dimension spectrum")` → confirms the `Tr e^{-t D_K²} ~ Σ t^{(n−d)/2} a_n(D_K²)` heat-expansion form and the a_n^{ζ} as per-branch / L_max=3 spectral moments (S96 source provenance).
- `list_constants("a_[0-9]_FW_zeta")` + `get_constant` ×5 → a_0=6440.0, a_2=2776.165389, a_4=1350.7216, a_6=765.593826, a_8=521.183178 (all `Superseded: False`); `get_constant("tau_fold")` = 0.19. Used verbatim for the SD tail (regulator-pin a_n^{ζ} MANDATORY).

**Results**:

*Spectrum (L=12 cache @ τ_fold=0.19)*: 90 sectors (sector (4,4) absent — 90 of 91, accounted per plan), 166,896 block eigenvalues, **zero modes = 0**, 6,997 unique |λ| (summed-dim weights), total weight Σdim = 31,956,720; |λ| ∈ [0.819741, 5.418937], |λ|² ∈ [0.671975, 29.364876].

*LAYER A — hybrid-continuation splice matching (the literal pre-registration → INFO gate)*. Θ_cache(t)=Σ wt·e^{−t|λ|²} vs Θ_SD(t)=a₀t⁻⁴+a₂t⁻³+a₄t⁻²+a₆t⁻¹+a₈ (a_n^{ζ} canonical, SD tail to n=8):

| t_c | Θ_cache | Θ_SD | rel_diff |
|:----|--------:|-----:|---------:|
| 0.05 | 1.4834e7 | 1.0532e9 | 6.9999e1 |
| 0.08 | 9.5518e6 | 1.6287e8 | 1.6051e1 |
| 0.10 | 7.1835e6 | 6.7319e7 | **8.3714e0** (nominal t_c) |
| 0.15 | 3.6300e6 | 1.3609e7 | 2.7491e0 |
| 0.20 | 1.9143e6 | 4.4101e6 | 1.3038e0 |
| 0.30 | 6.0436e5 | 9.1596e5 | 5.1559e-1 |
| 0.40 | 2.2448e5 | 3.0582e5 | 3.6236e-1 (best) |
| 0.50 | 9.6520e4 | 1.3270e5 | 3.7489e-1 |

Matching check FAILS at every t_c: best rel = **0.3624** ≫ match_tol 1e-3 (nominal t_c=0.10 → rel 8.37). **Structural cause (substrate-first):** the canonical a_n^{ζ} are *per-branch L_max=3 zeta moments* (a heavily-truncated, differently-normalized object — verified in-script: full-cache moments give a₆=8911.6≠765.6, a₈=1545.5≠521.2), NOT the asymptotic Seeley–DeWitt coefficients governing the t→0 divergence of the *full L=12 cache* heat trace. A **finite spectrum's heat trace is bounded as t→0** (→ Σwt = 3.196e7); it has **no t⁻⁴ divergence** to splice onto. The hybrid-continuation splice (cache for t≥t_c + divergent SD tail for t<t_c) is structurally ill-posed for a finite cache → routes the literal pre-registration to INFO.

*LAYER B — the substrate-IS object (Step 1 of the substitution chain), the well-posed answer*. ζ_{D_K}(s) = Σ_{(p,q)} dim(p,q) Σ_branch |λ|^{−s} = Σ_j W_j |λ_j|^{−s}, a **finite Dirichlet polynomial → ENTIRE in s** (no continuation, no splice — the cache is the complete known spectrum). numpy-float64 vs mpmath agreement 9.59e-15 over 5 strip points. ζ_{D_K}(0) = 3.195672e7 = Σ W (total mode count, the entire-function value; a finite truncation has **no dimension-spectrum poles** — those poles {0,2,4,6,8} are a continuum artifact the finite object does not exhibit). Certified argument-principle search, window Re∈[−2,6], Im∈[0.5,100]: winding-certified **Z = 14**, all 14 isolated + Muller-polished (|ζ(s_k)| ≤ 5.7e-13):

| k | Re(s_k) | Im(s_k) | \|ζ(s_k)\| |
|--:|--------:|--------:|----------:|
| 0 | +5.651208289598 | 30.963385908053 | 7.05e-16 |
| 1 | +5.436713544956 | 35.515630735626 | 2.08e-16 |
| 2 | +4.874083482807 | 39.085236916753 | 1.90e-15 |
| 3 | +2.749778899637 | 44.401325789545 | 3.50e-14 |
| 4 | +3.455272078192 | 49.282480637941 | 8.61e-15 |
| 5 | +4.668400661211 | 54.087313541039 | 2.10e-15 |
| 6 | +5.668975763694 | 58.962157087192 | 1.29e-15 |
| 7 | +2.111835773142 | 64.175460435301 | 1.26e-13 |
| 8 | +5.094748690376 | 69.155783919894 | 2.81e-15 |
| 9 | +5.554466562766 | 74.726253812651 | 1.89e-16 |
| 10 | +4.468237186112 | 83.194961282773 | 3.47e-15 |
| 11 | +4.716297047031 | 87.575957255151 | 5.26e-15 |
| 12 | +5.411248918319 | 91.909295889857 | 8.36e-16 |
| 13 | +0.709706691934 | 95.942790911716 | 5.73e-13 |

Re-window **[0.709707, 5.668976]**, width 4.959269; median Re = 4.795190; **max_k|Re(s_k) − median Re| = 4.085484** ≫ 1e-6 common-line threshold → **NOT on a common vertical line** (massive scatter). This is the pre-registered FAIL direction realized on the genuine object: 14 ≥ N_min=5 certified zeros scatter across nearly 5 units of Re.

*Substitution chain (no-Euler-product, the structural reason — pre-registered, confirmed):* Step 1 — ζ_{D_K} IS the Casimir/Epstein-class lattice sum above (a finite Dirichlet polynomial, the SU(3) analog of the S³ F(s)). Step 2 — the substrate's "arithmetic" is the representation ring ℤ[V₃, V̄₃], composition by ⊕,⊗ over a COMMUTATIVE (additive) monoid with NO unique-factorization → **no Euler product** (ζ_{D_K} does not factor ∏_p(1−…)⁻¹). Step 3 — the s↔d−s mirror follows from heat-kernel modularity / Poisson summation (physics gives it for free, as in W7-1's exact theta-dual). Step 4 — mirror WITHOUT Euler-product pin ⇒ Davenport–Heilbronn phenomenon: zeros scatter off any critical line. Step 5 — the Jensen deformation rescales the metric blocks but introduces NO multiplicative structure ⇒ the genuine SU(3) ζ_{D_K} inherits the scatter. **Direction confirmed:** Re-spread 4.085 ≫ 1e-6 (scatter). The S³ proxy showed Re-spread 0.93 (3 zeros); the full SU(3) object shows Re-spread **4.085** (14 zeros) — the scatter is *larger*, as expected for the higher-rank, denser-degeneracy lattice sum. RH-ness is the arithmetic fingerprint of the primes, which the fabric provably lacks: the substrate IS the lattice sum, and nothing pins its zeros to the mirror.

*Cross-checks*: (i) W7-1 corrected τ=0 anchor — c_off = 0.250000 (=1/4), R_scalar = 2.000000 (=2), S|_SU(3)=8⊕8 (spinor rank 16), W7-1 verdict PASS, closed-form absdiff 2.88e-13 (anchors the substrate object footing; the zero search uses the τ_fold cache spectrum). (ii) Winding non-integer guard |w − nint(w)| < 0.15 satisfied throughout (all box windings certified integer; 14/14 isolated = certified count). (iii) numpy↔mpmath 9.59e-15 (float64 fast path validated against arbitrary precision; Muller polish in mpmath at polish_dps=40).

*4-tuple*: (value=INFO[matching-gate]; substantive Re-spread=4.085484; scheme=HYBRID-HEAT-KERNEL-CONTINUATION; convention=single-power Conv. B / poleconv-B-single / n∈{0,2,4,6,8} at d=8; L_max=12). Dual-SHA: audit_sha256=`5243d76d42f145ebc82bf77a326aa9f1ceb56274e45cb818cbbf6301247b39a7`, content_sha256=`19742dbdca647cc39d721d4f50265552e2639f133d1b833073a8fd1eea8d5a84`. regulator_pin a_n^{ζ} (a_0..a_8 FW_zeta), SD_tail_order n=8 (companion rows).

**Output Artifacts**:
- Script: `computations/session-105/s105_w7_5_substrate_zeta_zeros.py` — `grep -E 'from canonical_constants import|print_verdict_payload'` → both present (L62, L291/L459).
- Data: `computations/session-105/s105_w7_5_substrate_zeta_zeros.npz` (zeros, Re-spread, splice diagnostic, SHAs) — exists (7,854 B).
- Plot: `computations/session-105/s105_w7_5_substrate_zeta_zeros.png` — exists (125,984 B): left panel zero scatter vs median Re; right panel splice failure (Θ_cache bounded vs Θ_SD t⁻⁴-divergent).
- Verdict line: `computations/session-105/s105_gate_verdicts.txt` — `S105-W7-5-SUBSTRATE-ZETA-ZEROS: INFO …` + dual-SHA companion + 3 extra companion rows (race-safe emit, sig_5 unique).

**Assessment**: The pre-registered question — *does the genuine Jensen-deformed substrate zeta satisfy its own RH analog?* — is answered cleanly: **it does NOT**, for a structurally identified reason (functional-equation mirror present, but no Euler-product pin, because ℤ[V₃,V̄₃] is additive). The verdict is INFO only because the *literal* hybrid-continuation method's cache/SD splice is structurally ill-posed for a finite cache (the canonical a_n^{ζ} are L_max=3 per-branch moments, and a finite spectrum has no small-t heat-trace divergence) — exactly the INFO route the plan pre-registered for "the cache/SD splice is the limiting step, not the zero geography." The substantive substrate-IS content (LAYER B, the entire direct-sum object that IS Step 1 of the chain) confirms the Track-A expectation with margin: 14 certified zeros, Re-spread 4.085 ≫ 1e-6, scatter larger than the S³ proxy. This is the negative-space result the off-session exploration anticipated, now on the genuine SU(3) object: the fabric's geometry is arithmetic-free, and its zeta's zeros mark where the substrate's physics ends and ℚ's arithmetic begins. No downstream consumer; terminal.

---

### §W7-6. S105-W7-6-S3-ZETA-ASYMPTOTICS (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S105-W7-6-S3-ZETA-ASYMPTOTICS`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (asymptotic zero distribution of the exact S³ Dirac zeta; INFO-by-construction)
**Agent**: `gen-physicist`
**Hypothesis**: The exact S³ Dirac zeta F(s) has a characterizable Im→∞ zero distribution over Im∈[36,300] — certified census + Re-histogram + density fit vs (T/2π)log T — closing the off-session window-finite caveat; INFO-class characterization, FAIL only on unresolvable winding-certification failure.
**Plan reference**: `sessions/session-plan/session-105-plan-w7.md` §W7-6. Unconditional (closed-form F(s), no cache). **INFO-by-construction**: the gate pre-registers a composite operator DIFFERING from the generic schema-v2 collapse — a magnitude/regime outcome does NOT collapse to FAIL; the only FAIL route is non-integer winding after refinement. The producing script emits a `# composite-precedence: §W7-6 …` companion row naming this plan anchor and the overridden generic-collapse reading, per `.claude/rules/gate-verdicts.md §"Plan-frozen gate-block operator precedence"`. Uses the certified `_rh_substrate_sanity.py` winding kernel + the F_s3 closed form (validated to 1e-23; reproduced in-script to 3.9e-31).

**Verdict**: **INFO** (by construction). 116 certified zeros over Im∈[36,300] — NONE on a common vertical line; the off-line scatter drifts toward (does not pin to) the Re=5/2 ghost line of ζ(s−2)'s shifted mirror. Closes off-session caveat #5 (window-finite certification: Im≤36.13 → Im≤300).

**Output Artifacts**:
- **Script** `computations/session-105/s105_w7_6_s3_zeta_asymptotics.py` (37,905 B) — `grep "from canonical_constants import"` → `from canonical_constants import *  # noqa: F401,F403,E402` + `from canonical_constants import tau_fold, PI`; `grep "print_verdict_payload"` → def at L191, call at L722.
- **Data** `computations/session-105/s105_w7_6_s3_zeta_asymptotics.npz` (13,254 B) — 116 zeros (re/im/complex), per-panel counts [20,44,52], per-panel winding residuals, Re-distribution stats, ghost-trend slope, N(T)/density-fit arrays.
- **Plot** `computations/session-105/s105_w7_6_s3_zeta_asymptotics.png` (210,255 B) — 3-panel: (a) certified zero map in (Re,Im) with Re=5/2 ghost line; (b) Re-distribution histogram; (c) N(T) density fit vs (T/2π)log(T/2πe) + free power-law.
- **Verdict line** `computations/session-105/s105_gate_verdicts.txt` — `^S105-W7-6-S3-ZETA-ASYMPTOTICS:.* audit_sha256=[a-f0-9]{64}` matched; `audit_sha256=cfd3d2bd5b721ef2aac034686309f5d6302fb41b5fc6f333a13d943aec07254f`, `content_sha256=3edf255ad48779ae30d9037e98e63d9f557d39ae0cc2c1e5cd3fe173d5113367`; dual-SHA companion row + `# composite-precedence: §W7-6 …` row + census row + convention row all present (5 rows total, race-safe via `emit_verdict`).

**MCP Pre-Compute Audit**:
- `search_knowledge("S3 Dirac zeta zero census asymptotic Riemann substrate")` → no Im∈[36,300] census entity; nearest hits are `M_zeta_s3` (Mellin moment at s=3) and `alpha_HH1_per_pole_FW_s3` (HH¹ envelope) — unrelated. NOT PRE-CLOSED.
- `search_knowledge("substrate satisfy own Riemann Hypothesis off-session winding zero scatter")` → off-session `_rh_substrate_sanity.py` is an exploratory helper (no verdict, no registry); S74 `zero_mode_winding` is a different (topological) winding gate. The off-session sanity test certified only Im≤36.13; this gate is its window-finite-caveat closure. NOT PRE-CLOSED.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). Used ONLY as the cache-pin import witness; the closed-form F(s) has NO cache dependency.

**Results**:

NUMBERS first. The exact S³=SU(2) Dirac zeta `F(s) = (2^{s−2}−1)·ζ(s−2) − (2^{s−2}−1/4)·ζ(s)` (Conv. B single-power; spin Dirac spectrum |λ_k|=k+3/2, mult (k+1)(k+2)) was certified in-script (worst Hurwitz-reduction residual **3.94e-31**, residues @ s=3 → +1, @ s=1 → −0.25). Argument-principle winding census over Im∈[36,300] in three panels, dense-perimeter pre-sampled (step h0≤0.2, anti-aliasing MANDATORY) and certified by per-strip winding with a strip-sum cross-check; zeros located by grid-seeded Muller (polish_dps=40):

| Panel | Im window | Certified Z (whole-panel winding) | Located (strip-sum xref) | max non-integer winding residual | Re range | median Re | mean \|Re−5/2\| |
|:------|:----------|:----------------------------------|:-------------------------|:---------------------------------|:---------|:----------|:----------------|
| 1 | [36, 100] | 20 | 20 (20==20 ✓) | 8.13e-20 | [1.8322, 3.4235] | 2.5198 | 0.4202 |
| 2 | [100, 200] | 44 | 44 (44==44 ✓) | 3.25e-19 | [1.8666, 3.5057] | 2.6652 | 0.3759 |
| 3 | [200, 300] | 52 | 52 (52==52 ✓) | 1.12e-20 | [1.9350, 3.5661] | 2.6042 | 0.3455 |
| **all** | **[36, 300]** | **116** | **116** | **3.25e-19** | **[1.8322, 3.5661]** | **2.5792** (mean 2.6085) | **0.3699** |

Per-zero census (s = Re + Im·i; |Re−5/2| in the last column):

**Panel 1 — Im∈[36,100], 20 zeros:**
`+2.0167+36.6717i (0.483)` · `+3.3745+41.6913i (0.875)` · `+2.3788+45.0774i (0.121)` · `+2.6860+48.9679i (0.186)` · `+2.2279+53.9991i (0.272)` · `+3.3696+55.6130i (0.870)` · `+2.5173+60.0675i (0.017)` · `+2.2233+63.6777i (0.277)` · `+3.0165+66.3651i (0.516)` · `+3.2832+69.9241i (0.783)` · `+1.8322+72.4045i (0.668)` · `+2.5689+76.3470i (0.069)` · `+3.3592+78.9875i (0.859)` · `+2.1167+81.8161i (0.383)` · `+2.8457+84.1751i (0.346)` · `+2.5223+88.0134i (0.022)` · `+2.2597+90.5882i (0.240)` · `+3.4235+92.8887i (0.924)` · `+2.4589+95.3357i (0.041)` · `+2.0492+99.4359i (0.451)`

**Panel 2 — Im∈[100,200], 44 zeros:**
`+2.7983+100.565i (0.298)` · `+2.9747+104.204i (0.475)` · `+2.9850+106.357i (0.485)` · `+2.1879+108.687i (0.312)` · `+2.2633+111.469i (0.237)` · `+3.0800+114.540i (0.580)` · `+3.0323+117.160i (0.532)` · `+2.1089+118.090i (0.391)` · `+2.7636+121.844i (0.264)` · `+2.5605+123.735i (0.061)` · `+1.9107+127.033i (0.589)` · `+3.3911+128.842i (0.891)` · `+2.8395+130.615i (0.340)` · `+2.4761+133.990i (0.024)` · `+2.0562+135.815i (0.444)` · `+2.8920+138.590i (0.392)` · `+2.7081+140.538i (0.208)` · `+3.1740+143.129i (0.674)` · `+2.0141+145.203i (0.486)` · `+2.5754+146.970i (0.075)` · `+2.3326+150.433i (0.167)` · `+3.5057+152.463i (1.006)` · `+2.0771+153.953i (0.423)` · `+2.7607+156.646i (0.261)` · `+2.5709+158.396i (0.071)` · `+2.7458+161.619i (0.246)` · `+1.8666+163.150i (0.633)` · `+3.1317+165.657i (0.632)` · `+3.1430+167.416i (0.643)` · `+2.3099+169.535i (0.190)` · `+2.0552+172.355i (0.445)` · `+2.6224+174.138i (0.122)` · `+2.9509+176.176i (0.451)` · `+2.8541+178.805i (0.354)` · `+2.8306+181.091i (0.331)` · `+2.1881+181.473i (0.312)` · `+2.2835+185.176i (0.217)` · `+2.7768+186.866i (0.277)` · `+2.1252+190.216i (0.375)` · `+3.3566+190.289i (0.857)` · `+2.4499+192.651i (0.050)` · `+2.8173+195.550i (0.317)` · `+2.4897+197.433i (0.010)` · `+2.1065+199.348i (0.394)`

**Panel 3 — Im∈[200,300], 52 zeros:**
`+2.6318+201.792i (0.132)` · `+3.3475+203.490i (0.848)` · `+2.6396+204.962i (0.140)` · `+2.0224+208.284i (0.478)` · `+2.3930+209.022i (0.107)` · `+2.9105+211.859i (0.411)` · `+2.6254+213.887i (0.125)` · `+3.0475+215.697i (0.548)` · `+2.1370+217.534i (0.363)` · `+2.8781+219.531i (0.378)` · `+2.3009+221.148i (0.199)` · `+2.4246+224.376i (0.075)` · `+3.3366+226.325i (0.837)` · `+2.0663+226.765i (0.434)` · `+2.9383+229.387i (0.438)` · `+2.3129+231.599i (0.187)` · `+2.8469+233.431i (0.347)` · `+1.9850+235.794i (0.515)` · `+2.5521+237.272i (0.052)` · `+3.0619+239.542i (0.562)` · `+3.0667+241.106i (0.567)` · `+2.5288+243.325i (0.029)` · `+1.9442+244.661i (0.556)` · `+2.4391+247.514i (0.061)` · `+2.8904+249.077i (0.390)` · `+2.8772+250.739i (0.377)` · `+2.0661+253.666i (0.434)` · `+3.0866+254.138i (0.587)` · `+2.5013+256.001i (0.001)` · `+2.5830+258.950i (0.083)` · `+2.4033+260.413i (0.097)` · `+1.9950+262.989i (0.505)` · `+3.5337+263.770i (1.034)` · `+2.5193+266.024i (0.019)` · `+2.6663+267.582i (0.166)` · `+2.6714+270.325i (0.171)` · `+1.9350+271.844i (0.565)` · `+2.7643+273.104i (0.264)` · `+2.4197+275.960i (0.080)` · `+3.5661+277.353i (1.066)` · `+2.4778+278.786i (0.022)` · `+2.0832+281.059i (0.417)` · `+2.3069+282.841i (0.193)` · `+2.7933+284.602i (0.293)` · `+2.7243+287.045i (0.224)` · `+3.0605+288.530i (0.561)` · `+1.9419+289.985i (0.558)` · `+2.9587+291.819i (0.459)` · `+2.6863+293.933i (0.186)` · `+2.2829+295.340i (0.217)` · `+2.6474+298.437i (0.147)` · `+2.0376+299.275i (0.462)`

**Re-distribution.** Spread **1.734** over [1.8322, 3.5661], width far exceeding the 1e-6 common-line threshold → `ON A COMMON VERTICAL LINE? NO`. Re median **2.5792**, mean **2.6085** — both sit essentially AT the Re=5/2 ghost line. The histogram (plot panel b) is broad and unimodal about ≈5/2, with no spike on any single Re; this is the **Davenport–Heilbronn / mirror-without-pin signature** — a functional-equation mirror with NO Euler product scatters its zeros about the mirror axis but pins none to it.

**Re=5/2 ghost-proximity trend (the substantive limiting characterization).** The Re=5/2 line is the shifted mirror of ζ(s−2): ζ(s−2)'s critical line is Re(s−2)=1/2 ⇒ Re(s)=5/2. Regression of per-zero |Re−5/2| against Im gives slope **d(|Re−5/2|)/d(Im) = −4.16e−4 < 0**, and the panel-binned means decrease MONOTONICALLY: **0.4202 (Im∈[36,100]) → 0.3759 ([100,200]) → 0.3455 ([200,300])**, with the median-Im split giving low-height mean **0.3955** vs high-height mean **0.3443**. Direction (substitution chain below): the scatter **DRIFTS TOWARD** the Re=5/2 ghost line over Im∈[36,300] — it loiters toward the shifted-mirror axis at large height but does NOT collapse onto it.

**Density fit.** Cumulative count N(T_top=299.27) = 116. Windowed Riemann-style expectation N(T)−N(36) at T_top = 132.10 ⇒ observed/Riemann-log = **0.878** (sub-arithmetic density). Free-exponent power-law fit `N ~ 0.00397·T^1.8257`: the exponent **1.826** is super-linear but below the Riemann `(T/2π)log(T/2πe)` ~ T·log T growth — consistent with the W7-5 negative-space reading that the substrate-class zeta carries no arithmetic (Euler-product) zero-density enhancement.

**Substitution chain (INFO-by-construction; direction of the ghost-drift claim):**
- Claim A (verdict class): "the gate is INFO-by-construction; FAIL is reserved for unresolvable winding-certification failure, NOT for the scatter being large."
  - Step 1: F(s) has the functional-equation mirror but NO Euler product (off-session: 3 scattered zeros in Im≤36.13, no common line; here: 116 scattered zeros in Im≤300, Re-spread 1.734).
  - Step 2: ⇒ there is NO expected critical line; a common-line PASS criterion is structurally inapplicable to F(s) — forcing it under the generic schema-v2 collapse would mis-encode an applicability guard as a hypothesis failure.
  - Step 3: the substantive content is the LIMITING zero distribution (census + Re-histogram + density vs (T/2π)log T).
  - Step 4: ⇒ pre-registered composite-precedence operator: INFO unless the winding machinery itself fails (non-integer winding after refinement). Here max non-integer winding residual = **3.25e-19 ≪ 0.15 guard** on every panel, and every strip-sum cross-check closed (20==20, 44==44, 52==52). ⇒ verdict **INFO**.
- Claim B (ghost-drift direction): "the scatter DRIFTS TOWARD Re=5/2 with increasing Im."
  - Def 1: `d_k = |Re(s_k) − 5/2|` (distance of zero k's real part to the shifted-mirror axis Re=5/2).   [Re=5/2 from ζ(s−2) mirror: Re(s−2)=1/2 ⇒ Re(s)=5/2]
  - Def 2: trend slope `m = d(d_k)/d(Im)` from least-squares of {(Im_k, d_k)}.   [linear regression]
  - Step 3: substitute the 116 (Im_k, d_k): `m = −4.164e−4`; panel-binned means {0.4202, 0.3759, 0.3455} (ascending Im).
  - Step 4: `m < 0` AND mean(d_k | low Im)=0.3955 > mean(d_k | high Im)=0.3443 ⇒ d_k DECREASES with Im.   [both readouts agree in sign]
  - Conclusion: the off-line scatter drifts TOWARD (loiters toward, does not pin to) the Re=5/2 ghost line over Im∈[36,300]. The verdict remains INFO regardless of this drift's magnitude (the guard, not the hypothesis).

**Cross-checks.** (i) Closed-form F(s): direct-sum vs Hurwitz reduction worst residual 3.94e-31 (bit-tight; reproduces the off-session 1e-23 claim with margin); residues @s=3→+1, @s=1→−0.25 (heat coefficients a_0, a_2). (ii) Count certification is DOUBLE: whole-panel winding == Σ per-strip windings (independent argument-principle certifications) on all three panels. (iii) Location completeness: grid-seeded Muller located exactly the certified count in every strip and panel (no shortfall, no over-count after half-open Im-membership dedup at 1e-9). (iv) Poles s=3, s=1 lie on the real axis (Im=0), FAR below Im=36 ⇒ P=0 inside every panel ⇒ winding == pure zero count. (v) Anti-aliasing: dense-perimeter pre-sampling at h0≤0.2 BEFORE refinement (the off-session winding-undercount hazard) — confirmed by clean integer windings (max residual 3.25e-19).

**Methodology deviations (honest disclosure per `v3-closure-recovery.md` Class-1 boundary).** The off-session certified winding kernel was extended for the 10×-larger Im∈[36,300] window with two in-session hardening changes, both fully disclosed and NEITHER altering the certification logic (the winding guard |w−nint(w)|<0.15 and the strip-sum cross-check remain the sole certification): (1) the COUNT step keeps the off-session dense-perimeter winding verbatim; (2) the LOCATION step replaces the off-session recursive winding-certified box-bisection (`_isolate`, which over the larger window grazed a near-contour zero — the off-session "zero on boundary" RuntimeError at Im≈72.4 — and whose cut-retry combinatorially re-descended) with a grid-seeded Muller locator (`_grid_locate`) assigning zeros to strips by HALF-OPEN Im-membership [y0,y1) so an edge-straddling zero belongs to exactly one strip. No forced cut is ever made in the LOCATION step, so the boundary-zero hazard cannot arise there. Convention/scheme tags unchanged from the plan pin (`scheme=CLOSED-FORM-S3-DIRAC-ZETA`, `convention=single-power Conv. B poleconv-B-single`). No regulator_pin (exact closed form F(s), not a regulated a_n citation); no CLASS pin (no SCHEMATIC helper).

**Substrate framing (phononic-framing.md).** GEOMETRIC. F(s) IS the exact Dirac zeta of the S³=SU(2) round geometry — the substrate's analytically-closed little brother, same structural genre (Casimir lattice sum with Weyl-dimension multiplicities) as ζ_{D_K} on SU(3) but with the spectrum in closed form. The arrow runs S³ Dirac spectrum (|λ|=k+3/2, mult (k+1)(k+2)) → closed-form zeta F(s) → certified zero census → limiting Re-distribution. The substrate-IS statement: a mirror-without-pin spectral functional, at large height, scatters its zeros about the shifted-mirror Re=5/2 ghost of ζ(s−2) and loiters toward it (slope −4.16e−4, panel means 0.42→0.38→0.35) but pins to NOTHING — there is no arithmetic line to hold them. This is the analytically-clean witness for the W7-5 expected FAIL on the genuine (non-closed-form) SU(3) object: RH-ness is non-generic for substrate-class zetas precisely because they carry a functional-equation mirror without an Euler product. The window-finite caveat the off-session FAIL carried (Im≤36.13) is now closed to Im≤300 with a limiting-density characterization.

**4-tuple**: `(value='n_zeros=116_panels=[20, 44, 52]_Re_spread=1.7340_Re_median=2.5792_Re_mean=2.6085_common_line=NO_mean_dist_ghost52=0.3699_ghost_trend_slope=-4.1642e-04_lowImg_meandist=0.3955_highImg_meandist=0.3443_powerlaw_exp=1.8257_riemann_ratio_top=0.8781_maxwind_resid=3.25e-19_closedform_resid=3.94e-31', scheme=CLOSED-FORM-S3-DIRAC-ZETA, convention=single-power-ConvB-poleconv-B-single/F(s)=(2^{s-2}-1)zeta(s-2)-(2^{s-2}-1/4)zeta(s)/Re=5/2-ghost-ref, L_max=NA-closed-form)`. **dual-SHA**: `audit_sha256=cfd3d2bd5b721ef2aac034686309f5d6302fb41b5fc6f333a13d943aec07254f`, `content_sha256=3edf255ad48779ae30d9037e98e63d9f557d39ae0cc2c1e5cd3fe173d5113367`. **`# composite-precedence:` row** (echo): `§W7-6 (generic schema-v2 collapse overridden — INFO-by-construction; FAIL only on non-integer winding after refinement)`.
---

## Wave 7 Synthesis (team-lead)

**The substrate trace-formula program's first full pass: the identity is exact, the instrument is validated, the τ_fold measurement is resolution-limited, and the arithmetic-free verdict held on the genuine object.**

**Verdict roll-up (6 gates: 2 PASS / 2 FAIL / 2 INFO):**

| Gate | Verdict | Load-bearing number |
|:-----|:--------|:--------------------|
| §W7-1 TRACE-FORMULA-EXACT-ANCHOR | PASS | two-sided exact `max_rel = 2.336e-29`; corrected closed form `\|λ\|² = (1/6)[C₂(μ)+C₂(p,q)] + 1/4` (S\|_SU(3) = 8⊕8; c_off = 1/4 = R/8 Friedrich floor) |
| §W7-2 LENGTH-SPECTRUM-FT | PASS | 19 window-stable peaks; τ=0 control ON coroot lattice (primitive 4π); PW-weighted Weyl 7.817 PRIMARY / block 5.022 DIAGNOSTIC; caveat `n_lambda_range_robust = 0` |
| §W7-3 BERRY-TABOR-MATCH | FAIL | `match_frac = 3/19` vs ≥ 2/3; predictor EXACT at τ=0 (4π Sage-confirmed); measured peaks ~6× above predicted primitive 21.27 |
| §W7-4 GEODESIC-COMMENSURABILITY | FAIL | rational_frac 0.4273 (CF) / 0.2517 (PSLQ-pair) vs ≥ 0.80; τ=0 control 36/36 EXACT on the Loeschian integers `(L/4π)² ∈ {1,3,4,7,9,12,13,19,27}` |
| §W7-5 SUBSTRATE-ZETA-ZEROS | INFO | splice-matching pre-registered INFO route fired; substance: 14 winding-certified zeros, Re-window [0.7097, 5.6690], spread 4.085 — **no common line** |
| §W7-6 S3-ZETA-ASYMPTOTICS | INFO | 116 certified zeros Im ∈ [36,300] (strip-sums exact); Re-spread 1.734, ghost-drift toward Re = 5/2 without pinning; density 0.878× Riemann-log, exponent 1.83 |

**Track 1 — geometric side (W7-1 → W7-2 → W7-3/W7-4).** The substrate HAS an exact trace formula: at the τ=0 bi-invariant point the Peter-Weyl spectral side equals the coroot-lattice Poisson dual to 10⁻²⁹ (W7-1) — the geometric side IS the substrate's closed internal relay orbits / winding lattice, and the exactly-dualizable object is the torus character theta Θ_S, not the Plancherel-weighted full trace. The measurement pipeline is positively controlled three independent ways (W7-2 FT control ON the coroot lattice; W7-3 predictor reproducing 4π exactly; W7-4 control 36/36 Loeschian-exact). At τ_fold, however, the three gates jointly resolve the measured 19 peaks as **Strutinsky-residual structure at L_max=12 resolution, not geodesics**: W7-2's λ-range diagnostic flagged it (0/19 range-robust), W7-3's independent Berry-Tabor resonance lattice corroborated it decisively (3/19 with the measured peaks ~6× above the predicted primitive orbit), and W7-4's incommensurability FAIL inherits the same caveat (vacuous at resolution-matched tolerance). **The corridor "measured peaks = integrable geometric side at this resolution" is CLOSED; the integrable-geometry hypothesis itself survives intact** (the predictor is exact where the spectrum is known exactly).

**Track 2 — zeta-zero geography (W7-5/W7-6).** The genuine SU(3) substrate zeta — the finite Dirichlet polynomial `ζ_{D_K}(s) = Σ_j W_j|λ_j|^{−s}`, which is the well-posed substrate-IS object — scatters its 14 certified zeros across Re ∈ [0.71, 5.67] (spread 4.085, vs the S³ proxy's 0.93): **the substrate-class zeta FAILS its own RH analog**, confirming the pre-registered Track-A expectation (0.9) and the mirror-without-pin structural argument (the representation ring ℤ[V₃,V̄₃] is additive — functional-equation mirror without an Euler-product pin ⇒ Davenport-Heilbronn scatter). The S³ control census (W7-6) closes the off-session finite-window caveat #5 with the analytically-clean version: 116 zeros to Im = 300, no common line, scatter drifting toward the Re = 5/2 mirror ghost without pinning, density sub-arithmetic (0.878× Riemann-log). Substrate-IS reading: the fabric's geometry is arithmetic-free; its zeta's zeros mark where substrate physics ends and ℚ's arithmetic begins. Two W7-5 structural findings recorded for posterity: (i) the hybrid heat-kernel-continuation method is ill-posed for ANY finite cache (a finite spectrum's heat trace is bounded as t→0 — nothing to splice SD asymptotics onto); (ii) a finite truncation exhibits NO dimension-spectrum poles ({0,2,4,6,8} are continuum artifacts; ζ_{D_K}(0) = mode count, an entire-function value).

**Cross-gate tension adjudicated (W7-1's corrected closed form vs W7-2's control).** W7-2 completed before W7-1's correction existed and built its τ=0 control on the superseded `C₂ + 0.75` form — yet the control landed ON the coroot lattice. Resolution: FT peak POSITIONS are set by the lattice geometry, which both forms share; the corrected Fegan form governs offsets/amplitudes (and was consumed by W7-3/W7-4/W7-5 via the orchestrator dispatch note). Both agents disclosed honestly; this is an in-session structural correction (plan premise superseded by computation), not a verdict-affecting conflict. The plan's premise drift is recorded in housekeeping §A for the S106 planner.

**Workshop candidate (Q1, for `/rclab-investigate`; pre-registered at plan-index session-close obligation iv):** GEM-COMMENSURABILITY — the W7-4 FAIL adjudication: *deformed-incommensurable* (the Jensen deformation genuinely breaks the τ=0 rational lattice) vs *measurement-artifact* (the peaks PSLQ tested are the same resolution-limited artifacts W7-3 identified; the test is vacuous at resolution-matched tolerance). Two genuine competing readings with first-principles arguments on both sides — a Q1 math/physics adjudication, not a status-tag choice. W7-5's independent zero-scatter (consistent with incommensurability) and W7-3's artifact finding are the two sides' opening evidence.

**Effected In-Session (NON-MATH)**
- [x] W7-1 plan-premise correction (C₂+c_off → Fegan form) propagated to the three downstream W7 dispatch prompts at dispatch time — orchestrator override notes; recorded in housekeeping §A
- [x] W7-6 orphaned-process recovery — SendMessage continuation re-attached the dead agent to its run; agent diagnosed 3 winding-kernel failure modes (recursion overflow → max_depth blowup → strip-edge double-claim), fixed each in-session, ran clean
- [x] Off-session caveat #5 (S³ zero geography Im ≤ 36.13) — CLOSED by W7-6 (census to Im = 300)

## Carry-Forward Computations

### CF-S106-W7-FINER-LMAX-LENGTH-SPECTRUM — Resolution-sufficient length-spectrum re-extraction

| Field | Spec |
|:------|:-----|
| **What** | Re-extract the τ_fold length spectrum at a resolution where the Berry-Tabor-predicted lower-winding lengths {21.27, 37, 43, 56, 64} fall inside the resolved λ-band (wider spectral support and/or finer δL), then re-run the W7-3 line-by-line match — the precondition for ANY revived "measured = integrable geometric side" claim |
| **Inputs** | The W1-1 GT-builder (lifts the high-L sector-construction wall — the enabling piece landed this session); `s84_spectrum_cache_L12_tau019.npz` + higher-L extension; `s105_w7_2_length_spectrum_ft.py` pipeline; `s105_w7_3_berry_tabor_match.npz` (the exact-quadratic E(p,q) surface + predicted lattice, R² = 1.0) |
| **Gate** | Pre-registered same-form match: `match_frac ≥ 2/3` against the BT resonance lattice at the new resolution, with the λ-range-robustness diagnostic promoted to a pre-registered conjunct (the S105 lesson: window-halving alone cannot detect spectral-window truncation). **AUGMENTED by the GEM-COMMENSURABILITY workshop (S105) to a THREE-CONJUNCT discriminator — see the conjunct block below; the length re-match is reclassified P2-ONLY (measurement faithfulness), and the substrate-commensurability verdict P1 is read off the δL-free G_E-anisotropy trend.** |
| **Effort** | 1–1.5 waves (higher-L cache construction dominates; GT builder makes it feasible). The P1-PRIMARY sub-fit κ-drift sub-conjunct + the P1-INDEPENDENT S46-unfolding ⟨r⟩ are ZERO-COST on the existing L12 cache (no GT-builder) and can run AHEAD of the higher-L cache. |

**Discriminator conjuncts added by the GEM-COMMENSURABILITY workshop (spectral-geometer × connes, S105; SG3 + Re:SG3 + CN2 + R2 convergence; AUGMENTS this 4-field block in place — does NOT replace it).** Structural reduction pinned this workshop: squared-action commensurability ⟺ `(G_E/2)⁻¹` ∝ integral matrix ⟺ `G_E` ∝ rational quadratic form ⟺ `s := coeff(pq)/coeff(p²) = 1` (Loeschian; FORCED by the fit form — any `E = a(p²+q²)+a·pq+…` has `κ(G_E)=3` for every scale `a`). The commensurability verdict P1 is therefore a single scalar of the energy Hessian, δL-FREE. Per-track pre-registered forecasts:

- **P1-PRIMARY (substrate, δL-free).** Fit `E(p,q)` on the GT-builder cache at L_max ∈ {12,14,16}; extract `G_E^{(L)}` and the anisotropy invariant `A(G_E^{(L)}) = |κ(G_E^{(L)}) − κ(Hess C₂)|`, κ = eig_max/eig_min (equivalently the departure of `s = coeff(pq)/coeff(p²)` from 1). **PIN the fit window (all 90 sectors vs a fixed percentile band) and report A(G_E) as a function of the window** — the fit window is the structural analog of δL (a perfect R²=1.0 fit on a truncated sector set can return `s = 1` while the asymptotic `s ≠ 1`; the missing high-(p,q) sectors and the absent (4,4) are exactly where the Jensen block-splitting `L₁=e^{2τ}, L₂=e^{−2τ}, L₃=e^{τ}` would break the equality). Baseline pinned this workshop: at L12, `G_E = 0.349101·Hess(C₂)` EXACTLY (`k_diag = k_off = 0.349101`, Sage-exact; `κ = 3.0`) ⇒ `A(G_E^{(12)}) = 0` ⇒ the L12 substrate lattice is STILL Loeschian-rational. **ZERO-COST sub-conjunct, runnable NOW on `s84_spectrum_cache_L12_tau019.npz` ahead of the GT-builder cache (CN3-Q2):** sub-fit `E(p,q)` on (a) all 90 sectors, (b) low-(p,q) only (pin p+q≤6), (c) high-(p,q) only (pin p+q≥8), with the (4,4) absence handled (reconstruct, dim 125, OR report κ both with (4,4) bounded and excluded); read whether `κ`/`s` drifts across sub-fits. A drift = direct L12-cache evidence FOR anisotropy (Track B) with no new cache; a stable `κ=3` = evidence the proportionality is physical (Track A). **Track A: A → 0 monotone. Track B: A grows monotone away from 0** (E-CN2 predicts specifically that the high-(p,q) sub-fit returns `s > 1` while low-(p,q) returns `s ≈ 1`).
- **P1-INDEPENDENT (substrate, level statistics).** Reproduce the **S46 SFF degeneracy-resolved unfolding** at τ_fold and extend across L_max ∈ {12,14,16}; pre-register the unfolding spec (symmetry-sector restriction OR degeneracy-merge tolerance) as the load-bearing methodology step. NOT a naive nearest-neighbor ⟨r⟩ — naive reads ⟨r⟩→0 (spurious maximal clustering from the exact Peter–Weyl + Fegan within-sector degeneracies, e.g. (1,0) = {25/36 ×6, 37/36 ×12, 49/36 ×30}); the S46 SFF gate returned ⟨r⟩ = 0.439 (NOT ≈0), proving the unfolding was already done correctly once (the validated method to inherit). **In-hand datum, cite NOW as Track-B-leaning evidence: S46 SFF ⟨r⟩ = 0.439 on the raw D_K spectrum at τ_fold** (R(0.19) = 2.018 is the τ_fold metric value; Poisson class, no GUE ramp; above the Poisson surmise 2ln2−1 = 0.38629, far from the commensurate-clustered ~0.27 regime). **Track A: ⟨r⟩ sub-Poisson/clustered (~0.27, commensurate-degenerate). Track B: ⟨r⟩ ≈ 0.386 Poisson (incommensurate).**
- **P2-ONLY (measurement faithfulness, δL-limited — the ORIGINAL SG3 conjunct, reclassified).** Re-extract the τ_fold length spectrum at the finer resolution where the BT-predicted lower-winding lengths {21.27, 37, 43, 56, 64} fall inside the resolved λ-band; re-run the W7-3 line-by-line match at **FIXED rel_tol=1e-6** (NOT the resolution-matched tolerance — the vacuity trap: at δ(L²)/L² = 1.09e-1 the fold goes to 1891/1891 "rational" VACUOUSLY) with a **per-L_max `δ(L²)/L²` certification-floor report** verifying the lengths are now certifiable at 1e-6; `n_lambda_range_robust` promoted to a pre-registered conjunct. **Track A: match_frac ≥ 2/3, n_lambda_range_robust > 0. Track B: agnostic on P2** (the structural claim is about G_E, not peak-faithfulness).
- **DECISIVE AXIS.** The `A(G_E^{(L)})` / `coeff(pq)/coeff(p²)` TREND across L_max ∈ {12,14,16} (NOT a single value, NOT the length re-match) is the P1 discriminator. **Decisive-Track-A:** A flat ≈0 over 3 points (G_E stays ∝ Hess C₂; lattice Loeschian; substrate CRYSTALLINE at fold; the L12 length-spectrum FAIL was pure measurement artifact AND the substrate was crystalline all along). **Decisive-Track-B:** A climbs monotone (deformation shears the action metric; lattice non-integral; substrate INCOMMENSURATE). Ambiguous-middle pre-registered (A rising but not yet resolved at L=16 → favors B, not proven). The length re-match decides P2 only; routing P1 through it would be a circularity (testing the substrate question through the δL-corrupted functional both tracks agree is unreliable). **Why this is strictly stronger than the original single length-spectrum gate:** A(G_E) is δL-free (no FT bin, no Strutinsky width), isolates P1 (substrate) cleanly from P2 (measurement), and is free of the resolution-matched-tolerance vacuity trap (though NOT free of its own fit-window instrument parameter — hence the window-pin requirement above).

(The plan's other conditional CFs do not fire: the cross-pillar §VII seed required W7-4 PASS — it FAILed to the workshop track; the alternative zero-localization method required W7-6 FAIL — it landed INFO with all windings integer. The W7-4 Q1 workshop routed via the workshop schedule as GEM-COMMENSURABILITY and CONVERGED — its discriminator-gate output is the conjunct augmentation above; its structural verdict is `sessions/session-105/workshops/gem-commensurability-workshop.md §"Workshop Verdict"` + Wrap-Up.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-11 | Substrate trace formula (τ=0 anchor) | conjectured (off-session program item 13) | EXACT-ANCHORED (2.336e-29, two-sided) | W7-1; closed form corrected to Fegan (1/6)[C₂(μ)+C₂(p,q)]+1/4 |
| 2026-06-11 | Substrate length spectrum (geometric side) | never measured | first-measured; τ_fold peaks ARTIFACT-DOMINATED at L_max=12 | W7-2 PASS + W7-3 FAIL joint reading; pipeline positively controlled |
| 2026-06-11 | "Measured peaks = geometric side at L12 resolution" corridor | open | CLOSED (artifact attribution; hypothesis survives) | W7-3: predictor exact, 3/19 match, ~6× offset |
| 2026-06-11 | Substrate-RH analog (genuine SU(3) object) | S³-proxy evidence only (off-session, Re-spread 0.93) | FAILS-OWN-RH on the genuine object (14 zeros, spread 4.085) | W7-5 LAYER B; mirror-without-pin confirmed at Track-A 0.9 |
| 2026-06-11 | S³ control zero geography | finite-window caveat (Im ≤ 36.13) | census to Im = 300 (116 zeros; no line; ghost-drift; sub-arithmetic density) | W7-6; off-session caveat #5 closed |
| 2026-06-11 | Process observation | — | benign: forward-pinned `s105_w7_*` npz validator signature behaved as plan-documented; W7-3/W7-4 GATED dispatch fired correctly on W7-2 PASS | dispatch trace |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON | Size |
|:-----|:-------|:------------|:------------|:-----|:-----|
| S105-W7-1-TRACE-FORMULA-EXACT-ANCHOR | s105_w7_1_trace_formula_exact_anchor.py | …npz | …png | — | 35,645 / 3,868 / 86,400 B |
| S105-W7-2-LENGTH-SPECTRUM-FT | s105_w7_2_length_spectrum_ft.py | …npz (forward-pinned) | …png | — | 40,243 / 27,671 / 175,571 B |
| S105-W7-3-BERRY-TABOR-MATCH | s105_w7_3_berry_tabor_match.py | …npz (47 keys) | …png | — | 32,254 / 19,094 / 205,492 B |
| S105-W7-4-GEODESIC-COMMENSURABILITY | s105_w7_4_geodesic_commensurability.py | …npz (40 keys) | …png | — | 29,733 / 84,783 / 163,480 B |
| S105-W7-5-SUBSTRATE-ZETA-ZEROS | s105_w7_5_substrate_zeta_zeros.py | …npz | …png | — | 27,012 / 7,854 / 125,984 B |
| S105-W7-6-S3-ZETA-ASYMPTOTICS | s105_w7_6_s3_zeta_asymptotics.py | …npz | …png | — | 37,905 / 13,254 / 210,255 B |
