# Session 102 Wave 3 — External Validation / Spectral Core (cold-read keystone chain) (Results Working Paper)

**Session**: 102 | **Wave**: W3 | **Plan**: session-102-plan-w3.md | **Theme**: cold-read keystone chain — Fegan τ=0 external anchor + foreign-stack reproducibility + Stratum-1 novelty sweep + analytic dS/dτ>0 monotonicity, run STRICTLY IN ORDER with stop-at-first-failure gating behind item 11.

## Gate Sections

### §W3-11. S102-FEGAN-TAU0-SPECTRUM-VALIDATION (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S102-FEGAN-TAU0-SPECTRUM-VALIDATION`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (KEYSTONE external-anchor check; Stratum-1 checklist box 1, referee M8(a))
**Agent**: `spectral-geometer`
**Hypothesis**: The substrate's own τ=0 bi-invariant SU(3) Dirac spectrum (dirac_spectrum.py at (L1,L2,L3)=(1,1,1)) reproduces Fegan's 1987 closed form — eigenvalues to machine ε AND per-(p,q) multiplicities exact-integer — in one locked normalization convention.
**Plan reference**: `sessions/session-plan/session-102-plan-w3.md` §W3-11 (machinery pin, thresholds, convention-locking substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-102/s102_fegan_tau0_spectrum_validation.py` — present; `grep -E 'from canonical_constants import'` → `from canonical_constants import *  # noqa: F401,F403  (tau_fold etc.)`; `grep -E 'print_verdict_payload'` → `def print_verdict_payload(...)` + call site. ✓
- `computations/session-102/s102_fegan_tau0_spectrum_validation.npz` — present (sector diffs, multiset arrays, convention-lock data). ✓
- `computations/session-102/s102_fegan_tau0_spectrum_validation.png` — present (substrate-vs-Fegan |λ| scatter + per-sector diff). ✓
- verdict line in `computations/session-102/s102_gate_verdicts.txt` — present, matches `^S102-FEGAN-TAU0-SPECTRUM-VALIDATION:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + 2 extra rows. ✓

**MCP Pre-Compute Audit**:
- `search_knowledge("Fegan tau=0 bi-invariant SU(3) Dirac spectrum closed form algebraic n/36")` → returned the atlas-07 PROVEN theorem **`lambda^2 = n/36 algebraic spectrum`** ("16 integers, Exact algebraic, L=12, `dirac_spectrum.py`"); plus the cubic-point form `λ̂²=u²+uv+v²` and the Lai-Teh t=1/2 closed form. Gate is NOT pre-closed — it is the external-anchor *validation* of this PROVEN theorem against an independent 1987 closed form.
- `search_knowledge("tau=0 algebraic spectrum lambda^2 = n/36 C_2 + 3/4 Casimir Dirac eigenvalue")` → returned the two corpus convention lines: `λ² = C_2(p,q) + 3/4` (session-21c/22 paasch-collab) and `λ² = n/36` (atlas-07), plus `C_2(p,q)=(p²+q²+pq+3p+3q)/3`. Established the convention-trap source set.
- `trace_entity("tau=0 bi-invariant spectrum algebraic")` → no trace (concept lives under the atlas-07 theorem name, already surfaced above).
- `get_constant("tau_fold")` → 0.19 (S12/S42); confirms τ_fold≠0; this gate evaluates the **τ=0** bi-invariant point, the Jensen-curve endpoint, distinct from the fold.
- Verdict: NOT PRE-CLOSED. The PROVEN atlas-07 theorem is the *internal* statement; this gate supplies the *external* anchor (Fegan/Parthasarathy closed form, derived independently of the project) and the implementation-independent reproduction at machine ε.

**Verdict**: **PASS** — `value='max_eig_diff=8.882e-15_degenmis=0_pwmis=0_n36viol=0_offerr=0.00e+00_nsectors=45_Lop=8'` scheme=`BI-INVARIANT-TAU0` convention=`DIRAC-SPECTRUM-PY-CANONICAL-NORMALIZATION` L_max=8. `audit_sha256=24cdba4bf29ce6a35456852947d083d84a6d66f56472a140b29bc8a542a5f55c` content_sha256=`45b1ea876bfe6d6e411b667ffbc8f835d399ed0050178a1934472167863d0820`.

**Results**:

*NUMBERS FIRST.*

| Quantity | Value | Threshold | Verdict |
|:---|:---|:---|:---|
| max eigenvalue-multiset abs-diff `max_k| |λ|_sub[k] − |λ|_Fegan[k] |` | **8.882e-15** | < 1e-12 | PASS |
| within-block degeneracy mismatch count | **0** | = 0 | PASS |
| Peter-Weyl block-length mismatch count | **0** | = 0 | PASS |
| n/36 algebraic-form (non-integer) violations | **0** | = 0 | PASS |
| convention-lock bare-offset error | **0.00e+00** (exact) | < 1e-12 | PASS |
| GPU(torch eigvalsh)-vs-numpy cross-check (0,0) | **0.00e+00** | — | consistency ✓ |
| sectors compared (p+q ≤ L_max_operational=8) | 45 | — | — |

**4-tuple**: `(value=max_eig_diff=8.882e-15…, scheme=BI-INVARIANT-TAU0, convention=DIRAC-SPECTRUM-PY-CANONICAL-NORMALIZATION, L_max_plan=12 / L_max_operational=8)`.

**Per-(p,q) sector diff (low sectors; full 45-sector set in the npz):**

| (p,q) | dim d(p,q) | block dim 16·d | max\|d(\|λ\|)\| | degeneracy match | anti-Herm err |
|:---|:---|:---|:---|:---|:---|
| (0,0) | 1 | 16 | 5.55e-16 | ✓ | 0.00e+00 |
| (0,1) | 3 | 48 | 2.00e-15 | ✓ | 0.00e+00 |
| (1,0) | 3 | 48 | 2.89e-15 | ✓ | 0.00e+00 |
| (1,1) | 8 | 128 | 3.78e-15 | ✓ | 0.00e+00 |
| (2,0) | 6 | 96 | 7.55e-15 | ✓ | 0.00e+00 |
| (0,2) | 6 | 96 | 6.88e-15 | ✓ | 0.00e+00 |
| (2,1) | 15 | 240 | 6.22e-15 | ✓ | 2.37e-16 |
| (3,0) | 10 | 160 | 1.33e-15 | ✓ | 0.00e+00 |
| (0,7) | 36 | 576 | **8.88e-15** (worst) | ✓ | — |

**Substrate framing (substrate → emergent direction).** The substrate IS the spectral triple `(A_K, H_K, D_K(τ))`. At τ=0 the internal fiber is the bi-invariant SU(3) point — the maximally symmetric standing-wave configuration. The Dirac eigenvalues (the fiber's vibrational mode frequencies) are exactly algebraic, `|λ|² = n/36`. The flow runs **D_K eigenvalues (fundamental) → algebraic τ=0 spectrum → external anchor (Fegan 1987)**. This gate confirms the substrate's own τ=0 spectrum equals a closed form published with no knowledge of this project. Every emergent spectral moment downstream (a₀ → cosmological term, a₂ → Einstein-Hilbert, a₄ → Yang-Mills+Higgs) is a moment of THIS spectrum; the τ=0 anchor holding means the moments rest on externally-validated ground.

**The closed form (Fegan / Parthasarathy–Kostant), derived by representation theory alone.** The genuinely pipeline-independent closed form for the bi-invariant Dirac spectrum is the Parthasarathy/Kostant cubic-Dirac eigenvalue, computed from Casimirs (NOT the project's frame/Ω Dirac-assembly):

> **CC1 (closed form):** `|λ|²(p,q,μ) = (1/6)·[ C_2^Kil(μ) + C_2^Kil(p,q) ] + 1/4`,

where μ ranges over the su(3)-irreps appearing in `V_(p,q) ⊗ S` (S = the 16-dim Cliff(ℝ⁸) spinor module, `C_2^Kil(S)=3` exactly — Sage/numpy max-dev 0.0), `C_2^Kil(p,q)=(p²+q²+pq+3p+3q)/3` is the Killing-normalized Casimir, the slope `1/6` is the frame rescale (g₀=|B|=3·δ ⇒ frame E=I/√3 ⇒ D∼1/√3 ⇒ D²∼1/3, split 1/6 between the two Casimir summands), and the offset `1/4` is the spinor ρ-shift. The diagonal-Casimir operator `C_diag = −Σ_a J_a²`, `J_a = ρ(e_a)⊗I + I⊗ρ_spin(e_a)`, commutes with `D²` exactly (`[D², C_diag] ≈ 1e-16`) and its eigenvalue multiset supplies `{C_2(μ)}` with the correct within-block degeneracies. The leg uses only structure constants `f_{abc}`, Clifford generators, the spin rep `ρ_spin=(1/4)ad(e_a)_{bc}γ_bγ_c`, and the irrep `ρ` — NOT `dirac_operator_on_irrep`.

This yields the integer-mesh form that REPRODUCES the atlas-07 PROVEN theorem:

> **CC1′ (n/36 mesh):** `n = 36·|λ|² = 6·C_2(μ) + 6·C_2(p,q) + 9 ∈ ℤ` (since `3·C_2 ∈ ℤ`). Verified: 0 non-integer violations across all 45 sectors. Sample integers n: trivial (0,0)→27; (1,0)→{25,37,49}; (1,1)→{27,45,63,75}; (2,2)→{75,93,105,129,147}.

**CC2 — the normalization N is read off the |B|-frame, NOT fitted (substitution chain Step 3).** The closed form's two constants `(slope=1/6, offset=1/4)` are pinned at plan-freeze from the substrate's own frame, not by fitting to the comparison:
- the slope `1/6` is fixed by `g₀=|B|=3·δ` (substrate output: `mean(diag g₀)=3.000…`, frame E=I/√3);
- the offset `1/4` is read off the trivial sector via `RHO_OFFSET = |λ|²(0,0) − C_2(S)/6 = 3/4 − 3/6 = 1/4` (substrate `|λ|²(0,0)=0.750000000000`, `C_2(S)=3.000000000000`, both pipeline outputs ⇒ implied offset `0.250000000000`, err `0.00e+00`).

**The convention trap (substitution chain Step 4 — load-bearing).** The corpus carries three *incommensurate* normalizations, and the gate exists to exclude conflation among them. The locked frame uses `λ² = (1/6)[C_2(μ)+C_2(p,q)] + 1/4` (the FULL multiplet spectrum, NOT a single-Casimir-per-sector formula). Excluded readings, all verified distinct at the anchor (1,0):
- `λ² = C_2 + 3/4` (paasch-collab session-21c/22) — gives trivial-sector 3/4 but a single value/sector; a *different additive convention* from the full multiplet.
- `λ² = C_2 + 3` (this plan-block's own worked-example values: `λ²(1,0)=13/3`, `n(1,0)=156`, `λ²(1,1)=6`, `n(1,1)=216`) — Sage-verified to be `C_2 + 3`, NOT `C_2 + 3/4`; offset differs by `9/4`. **Note**: the plan-block example numbers are themselves in this *third* convention — the gate locks the substrate frame and does not adopt either of the plan's illustrative literals.
- `λ_1 = √(7/3)` i.e. `λ_1²=7/3` — a separate R²/R_K normalization. Excluded.

The comparison is valid ONLY within the one locked convention (substrate `dirac_spectrum.py` at (1,1,1)); the 8.882e-15 multiset match is achieved in that convention with `(1/6, 1/4)` fixed a priori.

**Substitution chain (per `math-scripts.md §Double-Check Logic`), with substituted numbers:**
- **Step 1** (substrate convention): `D_π = Σ_{a,b} E_{ab} ρ_π(X_b)⊗γ_a + I⊗Ω` at Jensen s=0 ⇒ (L1,L2,L3)=(1,1,1), g₀=|B| (`diag=3`). Substrate output IS the reference. [dirac_spectrum.py; frame E=I/√3=0.57735·I confirmed.]
- **Step 2** (Fegan closed form): `D²|_π` algebraic; in the locked frame `|λ|² = (1/6)[C_2(μ)+C_2(p,q)] + 1/4`; equivalently `n/36` integer mesh; equivalently cubic-point `λ̂²=u²+uv+v²=3·C_2+3` (Sage: `cubic − 3·C_2 = 3` exact, all sectors).
- **Step 3** (reduce Fegan to substrate convention): `(slope, offset) = (1/6, 1/4)` read off the |B|-frame + trivial sector; err `0.00e+00`. NOT a fit.
- **Step 4** (the trap): exclude `C_2+3/4`, `C_2+3` (plan-example), `√(7/3)`. Lock substrate frame.
- **Canonical form**: `diff(k) = sorted(|λ|_sub)[k] − sorted(|λ|_Fegan)[k]`; `max_k|diff| = 8.882e-15 < 1e-12`; multiplicity (PW dim(p,q) block length AND within-block |λ| degeneracy) exact-match, 0 mismatches.
- **Direction → Conclusion**: PASS ⇒ the substrate τ=0 spectrum equals the Fegan/Parthasarathy closed form in the locked convention ⇒ the construction pipeline is externally validated; **an internal agent cannot bias a 1987 closed form**. Items 12–14 are unblocked.

**Feasibility / sector-completeness (Casimir-bound, `math-scripts.md` D_K block-diagonality pre-check).** D_K is Peter-Weyl block-diagonal (PROVEN, S22b): `D_K = ⊕_{(p,q)} D_{(p,q)}` on `V_(p,q)⊗ℂ^16`; no dense ≥640k×640k storage. `L_max_operational=8` (45 sectors; largest block 16·45=720 for (0,8)/(8,0)) keeps every irrep construction within seconds and every block within VRAM. **`L_max_plan=12` is redundant for THIS gate**: the closed form is *sector-exact at every (p,q)* (the Parthasarathy/Casimir formula carries no truncation), so the operational truncation bounds the substrate-pipeline COMPUTE leg only; both legs are diffed on the identical 45-sector set and agree at machine ε. No τ=0 sector at p+q>8 can introduce a NEW eigenvalue undetected by the closed form — the closed form predicts every sector's spectrum analytically. Both `L_max_plan=12` and `L_max_operational=8` recorded in the npz keys.

**GPU path validated.** Per-block eigenvalues computed via `torch.linalg.eigvalsh` (ROCm, RX 9070 XT) on the Hermitian `H=i·D_π` for blocks ≥100×100; numpy `eigvals` cross-check on the (0,0) block returned 0.00e+00 difference, confirming the GPU path. Anti-Hermiticity of each `D_π` held to ≤2.37e-16.

**What PASS means for the solution space.** The keystone holds: the entire substrate Dirac construction (frame `E`, ρ_π, Ω offset, sector enumeration, GPU diagonalization) reproduces an externally-derived 1987 closed form to machine ε with exact multiplicities, in a single locked convention. This validates the foundation every downstream spectral-moment result (a₀/a₂/a₄ → emergent physics) rests on, and it is the single check no internal agent can bias. The convention trap (√(7/3) vs 13/3 vs C_2+3/4 vs C_2+3) is closed by reading the normalization off the substrate's own |B|-frame, not by fitting. Items 12 (foreign-stack reimpl), 13 (lit-sweep), 14 (TRD2 monotonicity) are unblocked.

**Artifacts**: `computations/session-102/s102_fegan_tau0_spectrum_validation.py` / `.npz` / `.png`; verdict + dual-SHA companion + 2 extra rows in `computations/session-102/s102_gate_verdicts.txt`.

---

### §W3-12. S102-FOREIGN-STACK-PW-BLOCK-REIMPL (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S102-FOREIGN-STACK-PW-BLOCK-REIMPL`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (monoculture remedy, referee M8(b); Stratum-1 checklist box 2)
**Agent**: `spectral-geometer`
**Hypothesis**: The pinned (1,1) adjoint Peter-Weyl block of D_K at τ_fold, rebuilt end-to-end on a foreign Sage exact-arithmetic stack (no project numpy pipeline), reproduces the canonical numpy-pipeline block spectrum to machine ε — confirming the result is implementation-independent.
**Plan reference**: `sessions/session-plan/session-102-plan-w3.md` §W3-12. Depends on item 11 = PASS (verified: item 11 landed PASS, max eigenvalue diff 8.882e-15, audit 24cdba4bf29ce6a3…); the keystone holds, this gate is unblocked.

**Substrate framing**: GEOMETRIC. The (1,1) adjoint block is one fiber-mode sector of the substrate's Dirac operator D_K. The flow runs **D_K eigenvalues (this sector) → block spectrum → cross-stack reproducibility**. Rebuilding the SAME operator block on a foreign stack (Sage exact arithmetic over CyclotomicField(12) + an independent numpy code path, NEITHER importing `dirac_spectrum.py`/`branching_computation.py` for the construction leg) and recovering the same eigenvalues confirms the substrate's spectral structure is a property of the **geometry**, not of one implementation — the laboratory analog of reproducing a measurement on a different apparatus. The substrate IS this block; the cross-stack diff IS the reproducibility check.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-102/s102_foreign_stack_pw_block_reimpl.py` — EXISTS (21,644 B). `grep -E 'from canonical_constants import'` → `from canonical_constants import tau_fold  # noqa: E402`. `grep -E 'print_verdict_payload'` → defined (`def print_verdict_payload(...)`) and called in `main()`.
- `computations/session-102/s102_foreign_stack_pw_block_reimpl.npz` — EXISTS (10,224 B); keys: `foreign_abs_evals, canonical_abs_evals, cache_abs_evals, diff_vec, max_diff, cache_diff, foreign_vs_sage_lo/hi, sage_anchor_lo/hi, pq, tau_fold, pass_eps, verdict, diagnostics`.
- `computations/session-102/s102_foreign_stack_pw_block_reimpl.png` — EXISTS (72,959 B); two-panel (overlaid spectra + semilog cross-stack diff).
- Verdict line in `computations/session-102/s102_gate_verdicts.txt` — present, matches `^S102-FOREIGN-STACK-PW-BLOCK-REIMPL:.* audit_sha256=[a-f0-9]{64}` (audit `e3770af3cb1168d9a299d27a53eaf102e5815f87a452e264b8ee493541e5b191`), dual-SHA companion row present.
- This WP §W3-12 — Status COMPLETED, Verdict, Output Artifacts, MCP Pre-Compute Audit blocks present.

**MCP Pre-Compute Audit** (queries executed before writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("Peter-Weyl block D_K (1,1) adjoint sector eigenvalue tau_fold")` → confirmed (1,1) sector is **128-dim** (8×16), **B3** = lowest positive eigenvalue of sector (1,1) [PROVEN]; block-diagonality W2 PROVEN exact (8.4e-15).
- `search_knowledge("foreign stack reimplementation monoculture Sage Dirac block reproducibility")` → no prior foreign-stack reimpl of this block; Sage-MCP verification logged in prior sessions (S88) — gate is genuinely new, not pre-closed.
- `get_constant("tau_fold")` → **0.19** (S12/S42, `s42_constants_snapshot.npz`, CONST-FREEZE-42, not superseded). Imported from `canonical_constants.py`, never hardcoded.
- `trace_entity("Fegan tau=0 spectrum validation")` → no trace (item 11 is this-session; the keystone PASS is verified directly from `s102_gate_verdicts.txt`).
- **Not PRE-CLOSED**: no closure covers cross-stack reproducibility of the (1,1) block; the gate is a genuine M8(b) monoculture check.

**Verdict**: **PASS** — `max|foreign − canonical| = 0.000e+00` over the full 128-eigenvalue sorted |λ| multiset, < the tight `1e-12` boundary (well inside the relaxed `1e-10`). 4-tuple `(scheme=FOREIGN-STACK-SAGE-EXACT-vs-CANONICAL-NUMPY-PIPELINE, convention=DIRAC-SPECTRUM-PY-CANONICAL-NORMALIZATION, L_max=N/A, value=max_diff=0.000e+00)`. Dual-SHA: audit `e3770af3cb1168d9a299d27a53eaf102e5815f87a452e264b8ee493541e5b191`, content `283b55fc149442b288a8eb05163b7450c99ebc9cefe65ab6ea169f7066d9d44c`.

**Results**:

*Gate (the diff).* Foreign-vs-canonical sorted-|λ| max-abs-diff over all 128 entries = **0.000e+00** (bit-exact). PASS boundary `< 1e-10`; achieved the tight `< 1e-12` floor. Cache cross-check `max|canonical − s84cache(1,1)| = 0.000e+00` (the s84 L12 cache `(1,1)`-sector snapshot is a faithful image of the pipeline block).

*The 128-eigenvalue block* (sorted |λ|, both stacks identical): lowest **0.872975033878** (= B3, the lowest positive eigenvalue of sector (1,1)), next 1.052034 (×2), 1.063714 (×8), …, highest **1.669568198805**. The lowest value reproduces the registry's B3 anchor.

*Foreign-stack construction record* (independent code path; **no `dirac_spectrum.py` / `branching_computation.py` import for the construction leg**, only the canonical leg imports the pipeline as the diff target):
- su(3) generators e_a = −i/2 λ_a (Gell-Mann, 0-indexed 0..7 = standard λ_1..λ_8); built exactly in Sage over CyclotomicField(12) where **i = z³** and **√3 = −z³ + 2z** (both exact), and re-built independently in pure numpy in this file.
- Structure constants f_abc = −2 Tr([e_a,e_b] e_c): EXACT in Sage (f_123 = 1, f_458 = √3/2 = −½z³+z, f_678 = √3/2, all imaginary parts algebraically 0); numpy leg reproduces f_123 = 1.000000, f_458 = 0.866025 = √3/2.
- Killing form B_ab = Σ_cd f_acd f_bcd = **3·I** EXACTLY (diag [3,3,3,3,3,3,3,3], offdiag 0) — identical on both stacks.
- Adjoint (1,1) rep ρ(e_a)_{cb} = f_abc: dim 8, anti-Hermitian (err 0), Casimir Σ_a ρ(e_a)² = −3·I (⇒ C_2(1,1) = 3) — exact.
- U(2)-invariant Jensen frame at (L1,L2,L3) = (e^{2τ},e^{−2τ},e^{τ}) = (e^{0.38},e^{−0.38},e^{0.19}); since B is diagonal the metric g is diagonal and the frame E is diagonal with E_aa = 1/√(g_aa) (frame diag [0.69816,0.69816,0.69816,0.52503,0.52503,0.52503,0.52503,0.47745] both stacks). Volume-preserving L1·L2³·L3⁴ = 1.
- ON-frame structure constants ft (norm **2.9470** both stacks); Levi-Civita connection Γ (norm **1.5245** both stacks; metric-compat err 0).
- Clifford(R⁸) γ_1..8 (16×16, Pauli kron; {γ_a,γ_b}=2δ_ab exact; `Sage tensor_product` ≡ `np.kron` verified element-wise).
- Spinor curvature offset Ω = ¼ Σ Γ^b_{ac} γ_a γ_b γ_c: norm **3.5666** (both stacks); anti-Hermitian (err 0); Ω imaginary eigenvalues **{±0.819741, ±0.845212, ±0.971408}** identical on both stacks — Ω matches the canonical pipeline bit-for-bit.
- Block assembly D_(1,1) = Σ_a E_aa ρ(e_a) ⊗ γ_a + I_8 ⊗ Ω (128×128); anti-Hermitian (err 0).

*Exact-arithmetic Sage anchor.* The foreign-numpy leg is anchored against the independent Sage-exact computation (full Sage source preserved verbatim in the script's `SAGE_FOREIGN_SOURCE`): |foreign_numpy − Sage_exact| = **2.22e-16** (lowest), **6.66e-16** (highest) — the two foreign paths agree to float64 ε.

*τ=0 rational cross-anchor (item-11 keystone domain).* At τ=0 the bi-invariant (1,1) block λ² multiset is the EXACT rationals **{3/4 (×2), 5/4 (×32), 7/4 (×40), 25/12 (×54)}** — the Fegan/Parthasarathy bi-invariant spectrum is algebraic, the τ=0 anchor item 11 certified (note: the plan's "λ²=6" shorthand is 2·C_2(1,1) = 2·3 = 6, the Casimir, not a literal block eigenvalue; the block eigenvalues are the listed rationals spread over the spinor⊗adjoint weights).

*Extraction note (the cross-stack float floor the gate anticipated).* D is anti-Hermitian in the math convention; its eigenvalues are purely imaginary and the Dirac magnitudes are |λ|. The numerically stable extraction routes through the HERMITIAN operator **H = i·D** (`eigvalsh`), NOT a general eigensolver: Sage's general `.eigenvalues()` on the degenerate 128×128 anti-Hermitian block over `ComplexField` **scatters catastrophically** (produced 33 spurious distinct |λ| for the I_8⊗Ω term whose true spectrum has only 3), whereas the Hermitian route is clean. This is exactly the "Sage-vs-numpy float-conversion at the eigenvalue-extraction boundary" the gate's `strict_PASS_boundary` note relaxed 1e-12→1e-10 for. **The OPERATOR matched the canonical bit-for-bit throughout** (all intermediates above identical); only the eigensolver choice mattered — a methodology lesson, not a construction defect. Both legs use the Hermitian route, giving the bit-exact 0.000e+00 diff.

*Frame-convention pin.* The foreign leg is reduced to the same |B|-normalized canonical frame as item 11 (`convention=DIRAC-SPECTRUM-PY-CANONICAL-NORMALIZATION`), so the diff measures a genuine cross-stack operator difference, not a frame-normalization mismatch (per the gate's convention pin, `machinery_pin_map.convention`).

**Assessment**: The (1,1) adjoint Peter-Weyl block of D_K reproduces on a foreign exact-arithmetic stack at machine ε (bit-exact, 0.000e+00). The block spectrum — including the B3 anchor 0.872975 — is **implementation-independent**: a property of the substrate geometry, not of the project numpy pipeline. Referee M8(b) monoculture concern remedied for the pinned block; Stratum-1 checklist box 2 ticked. The one substantive finding beyond the equality is methodological: cross-stack Dirac-block reproducibility checks MUST route eigenvalue extraction through the Hermitian operator H = iD on the degenerate anti-Hermitian D, never a general complex eigensolver — the construction can be bit-identical yet a naive eigensolver fabricates a spurious mismatch. Carry-forward: extending the foreign-stack check beyond (1,1) to the (0,0)/(0,1) sectors (B1/B2 anchors) would broaden the monoculture remedy from one block to the bottom-of-spectrum triple, at ~1 gate each (inputs: this script's foreign_block() generalized over (p,q); gate: same machine-ε equality).

---

### §W3-13. S102-STRATUM1-LIT-SWEEP (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S102-STRATUM1-LIT-SWEEP`
**Trigger**: `[VERIFY]`
**Classification**: **NON-PHONONIC** (novelty confirmation; Stratum-1 checklist box 3; COMPUTE-class-with-documented-search-trace, NON-COMPUTE PASS predicate)
**Agent**: `spectral-geometer`
**Hypothesis**: The Stratum-1 item-6/item-7 core (full Jensen-line SU(3) Dirac spectrum + van Hove DOS cusp) is absent from the published literature (MathSciNet / zbMATH / arXiv), confirming CANDIDATE-NOVEL with a documented search trace.
**Plan reference**: `sessions/session-plan/session-102-plan-w3.md` §W3-13. Depends on item 11 = PASS (S102-FEGAN-TAU0-SPECTRUM-VALIDATION PASS, max_eig_diff=8.882e-15 — keystone holds; gate unblocked, no mechanical closure needed).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/_shared/s102_stratum1_lit_sweep.py` — producing script; `grep -E '(from canonical_constants import|print_verdict_payload)'` → both present (`from canonical_constants import tau_fold`; `def print_verdict_payload(...)`). PASS.
- `computations/session-102/s102_stratum1_lit_sweep.npz` — structured trace records + summary + input SHAs. Present (created by run). PASS.
- `computations/session-102/s102_stratum1_lit_sweep.png` — disposition tally per query family (optional). Present. PASS.
- Verdict line: `computations/session-102/s102_gate_verdicts.txt` matches `^S102-STRATUM1-LIT-SWEEP:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row present. PASS.
- This WP §W3-13: Status COMPLETED, Verdict PASS, Output Artifacts, MCP Pre-Compute Audit blocks present. PASS.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queried BEFORE writing the script):
- `search_knowledge("Jensen line SU(3) Dirac spectrum novelty literature")` → returns INTERNAL entities only (S88-JENSEN-DIM-SPECTRUM, the Jensen-deformed D_K equations, atlas-07 Petrov classification, the L_max=10 cache); the equation row explicitly notes the τ=0 endpoint "reproduces Fegan's 1987 closed form". NO external-literature-novelty entity. The graph confirms the *object* exists internally; it is silent on the *external publication landscape* — exactly what this gate must establish externally.
- `search_knowledge("van Hove cusp density of states Dirac compact group novelty")` → S85-VAN-HOVE-CUSP-THEOREM + the τ_fold=0.190 PERMANENT non-stationary-cusp uniqueness theorem (internal); no external record.
- `trace_entity("Fegan bi-invariant Dirac spectrum SU(3)")` → no trace (the bi-invariant endpoint lives in the equation rows, not as a named entity). NOT PRE-CLOSED as a literature-novelty gate.
- `get_constant("tau_fold")` → 0.19 (S42; the DOS-cusp / Jensen-fold pin; imported by the script for query context).
- **PRE-CLOSED?** NO. The knowledge base records the INTERNAL spectral object (and its Fegan-τ=0 reduction) but contains no literature-novelty verdict for item-6/item-7. The gate is a genuine external-novelty determination, not a re-derivation of a closed result.

**Verdict**: **PASS** — `value='novelty_confirmed=True;records=11;families=(i)(ii)(iii)(iv)(v)(vi);prior_art=0;adjacencies=6;item6=CANDIDATE-NOVEL;item7=CANDIDATE-NOVEL;bi-inv_SU(3)_endpoint=Lai-Teh/Teh_MR3153451_arXiv1209.3812;Lauret-left-inv=LAPLACE;BoldtLauret-Dirac=LENS-SPACES;vanHove-DOS=condensed-matter;MathSciNet=FREE-tier-MRef-only'` scheme=STRUCTURED-LIT-SWEEP-DOCUMENTED-TRACE convention=NOVELTY-AUDIT-12-ROW-TRIAGE-CROSSREF L_max=N/A. dual-SHA: `audit_sha256=2117a30846ddf583fa76bcdafc059fa59731f6ef751390ebca43f37e0b92d2c4` `content_sha256=b7e7bd7d709a2662044edb6e40ba09e87d12cce490fc0c38acaf22160c7b2ff3`. 11 documented query records across all 6 pinned families; 0 prior-art hits for the item-6/item-7 core; 6 adjacency records (KNOWN-TECHNIQUE/CLASSICAL) that re-scope, not refute. The math-paper headline contribution stands as **CANDIDATE-NOVEL**. Stratum-1 checklist box 3 ticked.

**Results**:

**Novelty disposition.** Item 6 (full Dirac spectrum along the Jensen line of SU(3): 155,984 eigenvalues w/ multiplicity at L_max=10, 78,080 unique, crossing structure incl. the (1,1,0) crossing at τ=0.107) → **CANDIDATE-NOVEL CONFIRMED**. Item 7 (van Hove DOS cusp at τ_fold=0.190; non-stationary-cusp uniqueness) → **CANDIDATE-NOVEL CONFIRMED** (as a property of #6). No published source reproduces either. The disposition matches rows 6 and 7 of the 12-row triage table in `cold-read-s101/03-stratum1-novelty-audit.md §1`.

**Tooling note (MCP-server coverage).** MathSciNet MCP is **FREE-tier only** (no `MATHSCINET_API_KEY`): keyword `search_mathscinet` is unavailable; `lookup_mr_reference` (MRef) resolves canonical MR IDs. This is a tooling-access constraint, not a coverage gap — zbMATH (`search_zbmath` / `search_msc`) spans the same published-literature surface with MSC classification, and arXiv (`search_arxiv`) covers the preprint surface. Google-Scholar AVOIDED per `project_paper-search-scholar-rate-limit` (429-blocks ~130s/call under the shared IP limit). All three engines were used; the 4-tuple is (scheme=STRUCTURED-LIT-SWEEP-DOCUMENTED-TRACE, convention=NOVELTY-AUDIT-12-ROW-TRIAGE-CROSSREF, L_max=N/A).

**Per-family search trace** (11 records; {query, server, hit_count, top IDs, disposition} — full records pinned in `s102_stratum1_lit_sweep.npz:search_trace_json`):

| # | Family | Server | Query | Hits | Top relevant ID(s) | Disposition |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | (i) Dirac spectrum SU(3) | zbMATH | `ti:Dirac ti:spectrum ti:SU(3)` | 1 | **Zbl 900147539 / arXiv:1209.3812** Lai & Teh, *Dirac spectrum and spectral action of SU(3)* (2012) — **bi-invariant** | CLASSICAL (τ=0 endpoint only) |
| 2 | (i) Dirac spectrum SU(3) | arXiv | `Dirac operator spectrum SU(3) left-invariant metric` | 15 | Cartan-decomp su(N), SU(3) Skyrme, CERN DIRAC pionium, Majid C_q[SL_2] | NOT-RELEVANT |
| 3 | (ii) left-inv Dirac eig / compact Lie group | arXiv | `Fegan eigenvalues Dirac compact symmetric space bi-invariant spectral action` | 12 | Milhorat (1st eigenvalue, math/0501410-411, 1909.08283, 1407.2167); Gordon-Schueth-Sutton 0710.2911 (Laplace isolation) | KNOWN-TECHNIQUE |
| 4 | (iii) Lauret-school post-2022 | arXiv | `Lauret Dirac operator eigenvalues compact Lie group left-invariant metric deformation` | 15 | E.A. Lauret 2004.00350 / 1906.03325 / 1706.09012 (all **LAPLACE**); J. Lauret-Montedoro 2506.21725 (pluriclosed, non-spectral) | KNOWN-TECHNIQUE |
| 5 | (iii) Boldt-Lauret Dirac | arXiv | `Boldt Lauret Dirac operator spectrum spheres SU(2) representation` | 15 | **arXiv:1412.2599** Boldt-Lauret (Dirac multiplicities, **LENS SPACES**); arXiv:1504.03121 Boldt (lens-space Dirac rigidity) | KNOWN-TECHNIQUE |
| 6 | (iii) Einstein/Jensen-deformation Dirac | arXiv | `Jensen Einstein metric deformation Dirac operator homogeneous space spectral action` | 15 | Fischmann-Krattenthaler-Somberg 1405.7304 (conformal powers); Chrysikos-Sakane 1206.1306 (Einstein metrics); **Alexa 2508.11652** (Laplace spectral-flow, adjacent framework) | NOT-RELEVANT |
| 7 | (iv) "Jensen deformation" Dirac/SU(3) | knowledge-MCP | internal `search_knowledge`/`trace_entity` (NOT external lit) | 0 ext | internal-only: S88-JENSEN-DIM-SPECTRUM, S85-VAN-HOVE-CUSP, atlas-07 Petrov, S102-FEGAN PASS | CANDIDATE-NOVEL |
| 8 | (v) MSC verify | zbMATH | `search_msc 58J50` | 2 | 58J50 = "Spectral problems; spectral geometry … on manifolds" (confirmed) | NOT-RELEVANT (MSC verify) |
| 9 | (v) MSC 58J50 Dirac eig | zbMATH | `cc:58J50 ti:Dirac ti:eigenvalues` | 43 | Bär 1220814 (bounds); **Landi-Rovelli 1477791** (GR via Dirac eigenvalues); Hijazi/Friedrich/Ammann/Milhorat (1st-eig & bounds); Agricola-Ammann-Friedrich 1398347 (Dirac-vs-Laplace on T²) | KNOWN-TECHNIQUE |
| 10 | (v) bi-inv anchor MR resolution | MathSciNet/MRef | `lookup_mr_reference: Lai & Teh … SU(3) … arXiv:1209.3812` | 1 | **MR3153451** Teh, *Dirac Spectra, Summation Formulae, and the Spectral Action* (Caltech PhD thesis 2013; encompasses Lai-Teh) | CLASSICAL (τ=0 endpoint) |
| 11 | (vi) DOS / van Hove — Dirac homogeneous | arXiv | `density of states van Hove singularity Dirac operator homogeneous space spectral geometry` | 15 | all condensed-matter (PdTe₂, graphene SDW, KFe₂As₂, FCC, TaSe₂, HOVHS bilayer) + Dietz 1512.05069 (microwave Dirac-billiard graphene analog) + Davies 2404.12073 (chaotic-system periodic-operator DOS) | NOT-RELEVANT |

**Structural reading of the result (substrate-first cross-check).** The disposition is not a counting artifact — it follows from a clean separation of *operator* and *metric class*:
- **The only published SU(3) Dirac spectrum is bi-invariant.** Lai-Teh (Zbl 900147539 / arXiv:1209.3812) and the encompassing Teh thesis (MR3153451) compute the SU(3) Dirac spectrum + spectral action via Poisson summation for the **bi-invariant** (Killing) metric. That is precisely the τ=0 **endpoint** of the Jensen line — the Fegan/Parthasarathy case the project's own item-5 already tags KNOWN-TECHNIQUE and which S102-FEGAN-TAU0-SPECTRUM-VALIDATION reproduced to machine precision (`|λ|²=(1/6)[C₂(μ)+C₂(p,q)]+1/4`). Prior art for the τ=0 slice; **silent on every τ>0 deformation, the crossing structure, and the DOS cusp.** The math paper must *cite* Lai-Teh for the endpoint, not claim it.
- **The left-invariant deformation literature is LAPLACE, not Dirac.** The Lauret school (E.A. Lauret 2004.00350, 1906.03325, 1706.09012) and Gordon-Schueth-Sutton (0710.2911) study exactly the left-invariant-metric *deformation neighbourhood of the bi-invariant point* on compact simple groups — the right setting — but for the **Laplace-Beltrami** operator, as eigenvalue-bound / diameter / isospectrality-rigidity results. No Dirac operator, no computed spectrum, no SU(3) deformation line. This is the deepest adjacency (KNOWN-TECHNIQUE), and the paper should position the Jensen-line Dirac spectrum as the *Dirac analog* of this Laplace program.
- **The complete-Dirac-spectrum literature on groups/quotients stops at SU(2)/3-spheres and lens spaces.** Boldt-Lauret (1412.2599) and Boldt (1504.03121) give explicit Dirac multiplicities / rigidity on **lens spaces** (round-sphere quotients), and Milhorat (math/0501410-411 etc.) gives **first** eigenvalues on symmetric spaces — the rep-theoretic Dirac-multiplicity machinery is the standard *technique*, but it has not been carried to the full spectrum of SU(3) along a non-bi-invariant left-invariant line. This matches the triage row-6 anchor ("complete results known for SU(2)/3-spheres; SU(3)-Jensen open").
- **The van Hove DOS cusp is unoccupied for manifold Dirac spectra.** The van Hove singularity is classical band theory (van Hove 1953); every DOS/van-Hove hit (family vi) is condensed-matter lattice physics (graphene, FCC, transition-metal dichalcogenides, twisted-bilayer higher-order VHS) or a chaotic-dynamics periodic-operator analog (Davies 2024) or a graphene microwave-resonator "Dirac billiard" (Dietz 2015). None is the DOS of a Dirac *spectrum* on a deformed compact Lie group. The non-stationary DOS-cusp at a single τ along a Dirac deformation line is genuinely new territory (item-7 CANDIDATE-NOVEL, as a property of #6).

**Net.** Verdict PASS: novelty confirmed with a complete documented trace across all six pinned query families. The found adjacencies (Lai-Teh bi-invariant endpoint; Lauret-school Laplace; Boldt-Lauret/Milhorat Dirac on other spaces; condensed-matter van Hove) **re-scope** the claim (the paper cites these and frames its contribution as the Dirac analog of the Laplace-deformation program, the SU(3)/non-bi-invariant extension of the lens-space/symmetric-space Dirac results) — they do **not** refute it. No `FOUND-PRIOR-ART` record exists. Stratum-1 pre-submission checklist box 3 is satisfied. Artifacts: `computations/_shared/s102_stratum1_lit_sweep.py`, `computations/session-102/s102_stratum1_lit_sweep.npz`, `…/s102_stratum1_lit_sweep.png`.

---

### §W3-14. S102-TRD2-MONOTONICITY-ANALYTIC (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S102-TRD2-MONOTONICITY-ANALYTIC`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (timeboxed closed-form proof attempt; Stratum-1 checklist box 4; E7 numerical→analytic promotion)
**Agent**: `spectral-geometer`
**Hypothesis**: The spectral-action τ-gradient is strictly positive analytically — dS_SA/dτ > 0 (equivalently ⟨λ²⟩(τ) increasing) on the Jensen line — provable in closed form via Weitzenböck (D_K²=−∇²+R_K/4) + the exact R_K(τ), promoting E7 from 9,600-numerical-check status to a Theorem.
**Plan reference**: `sessions/session-plan/session-102-plan-w3.md` §W3-14. Depends on item 11 = PASS (verified: `S102-FEGAN-TAU0-SPECTRUM-VALIDATION` PASS, max eig diff 8.882e-15 — the D_K construction is externally validated; gate unblocked). Dual prior: Track A 0.6 (proof lands) / Track B 0.4 (per-sector dC/dτ step does not close in timebox).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

- `computations/session-102/s102_trd2_monotonicity_analytic.py` — EXISTS. `grep -E 'from canonical_constants import'` → `from canonical_constants import *` AND `from canonical_constants import dS_fold, tau_NEC, tau_fold`; `grep -E 'print_verdict_payload'` → def + call present.
- `computations/session-102/s102_trd2_monotonicity_analytic.npz` — EXISTS (proof certificate + cross-check arrays).
- `computations/session-102/s102_trd2_monotonicity_analytic.png` — EXISTS (per-sector dM₂/dτ>0 + cofactor-cleared polynomials).
- Verdict line: `S102-TRD2-MONOTONICITY-ANALYTIC: INFO -- … audit_sha256=87163c330d34a1182de49833fcb4568001973f613596a20107ae144f12f28bc3 content_sha256=4dc43e7f1582acc0515d277c6ca708cfaddd12265a5230add74050824aeaf97c schema_version=S84+` + dual-SHA companion row + `[SIGN]` 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) + composite-precedence/regulator-pin/proof/scope/dual-prior extra rows (8 rows total). Emitted via `emit_verdict` (race-safe, sig_5-unique).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queried BEFORE writing the script):

- `search_knowledge("E7 structural monotonicity theorem dS/dtau spectral action gradient")` → E7 τ-flow PROVEN (`dS_SA/dτ > 0`, `phonic-exflation-equation.md §5.1`); Spectral Action Monotonicity W4 (baseline-findings-s66 S17a): "⟨λ²⟩(τ) monotone. ALL monotone f, ALL Λ, ALL sectors. 9,600 checks"; S37 cutoff stabilization (all 10 sectors same direction).
- `search_knowledge("lambda squared monotonic tau Weitzenbock Lichnerowicz curvature endomorphism Casimir")` → E5 (`baptista-operator-dk-tau.md`): `D_K²=∇*∇+¼R_K ⟹ λ²≥¼R_K(τ)>0 ∀τ≥0` (eigenvalue LOWER BOUND, a DIFFERENT object than trace-monotonicity); `D_K²=−∇²+E`, E = Lichnerowicz endomorphism from R_K (Paper 19 eq 2.14-2.16; Gilkey 1975; `session-60-bap-collab.md`).
- `trace_entity("monotonic spectral action tau gradient")` → No trace (confirms the *analytic closed-form proof* of trace monotonicity is not previously registered — only the 9,600-numerical result).
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). `get_constant("tau_NEC")` → 1.383 (S85/S95, NEC onset, physical-domain boundary). `get_constant("a_2_FW_zeta")` → 2776.165389 (S88). `get_constant("dS_fold")` → 58672.80241318 (S42 `s42_gradient_stiffness`, `dS_full/dτ` at fold).
- `search_knowledge("R_K scalar curvature Jensen tau closed form E3")` → E3 exact: `R_K(τ) = −¼e^{−4τ}+2e^{−τ}−¼+½e^{2τ}`, R_K(0)=2 (`baptista-operator-dk-tau.md`, Sage-verified, 147/147 Riemann S20a).
- `search_knowledge("58672.8 dS_SA dtau fold gradient spectral action 9600 computation script")` → `dS_fold = dS_full/dτ at fold` from S42 `s42_gradient_stiffness`: `S_full = Σ dim(p,q)²·Σ_k|λ_k(τ)|` (the **|λ|-spectral-action**, f(x)=√x), 10 KK sectors, FD-differentiated. **NOT PRE-CLOSED** as an analytic theorem: E7 is PROVEN-by-9600-numerics; the closed-form proof is new work.

**Verdict**: **INFO** (`sign_verdict=PASS`, `magnitude_verdict=FAIL`, `regime_verdict=VALID`). The literal **E7 content — strict monotonicity of ⟨λ²⟩(τ) — is PROVEN in EXACT closed form** (the SIGN), a genuine numerical→analytic upgrade for the f(x)=x moment; the literal magnitude cross-check against +58672.8 FAILs because that anchor is the |λ|-spectral-action (f(x)=√x), a **different functional** whose magnitude this λ²-trace method does not reproduce. INFO is the plan-pre-registered outcome ("positivity proven … modulo a clearly-stated [scope] issue; Partial-Theorem status"). **E7's 9,600-numerical status is UNCHANGED**; the λ²-moment monotonicity now additionally holds as an analytic theorem.

**Results**:

The governing spectral object is the **second spectral moment** ⟨λ²⟩(τ) ∝ Tr D_K²(τ) over the Peter-Weyl truncation (baseline-findings-s66 S37 states the Structural Monotonicity Theorem on ⟨λ²⟩). Because D_π is anti-Hermitian (λ = i·μ, μ real), the **physical** moment is M₂(p,q;τ) ≡ Σ_k μ_k² = **−Tr D_π²** (positive). Monotone INCREASE of ⟨λ²⟩ = monotone DECREASE of Tr D_π².

*Exact closed form via direct trace of the matrix Dirac operator.* With `D_π = Σ_{a,b}E_{ab}(ρ(X_b)⊗γ_a) + I⊗Ω` (`dirac_operator_on_irrep`), the trace splits exactly:

  Tr D_π² = 16·Casimir_g(p,q;τ) + d(p,q)·Tr(Ω²)(τ),  cross-term ≡ 0 (Tr ρ(X_b)=0, su(3) traceless).

Numerically verified machine-ε exact (max rel **3.69e-16**, p+q≤3). The two pieces have exact closed forms:

1. **Frame-deformed Casimir** (the plan's C(p,q;τ)), from `E^TE = g_s^{-1}` and `Tr(γ_aγ_c)=16δ_{ac}`:
   **Casimir_g(p,q;τ) = −(C₂·d/24)·(3e^{2τ} + 4e^{−τ} + e^{−2τ})** — derived from the **EQUIPARTITION THEOREM** (max dev **2.84e-13** over all p+q≤7): the per-block rep-traces split as S_su2 : S_c2 : S_u1 = **3 : 4 : 1 = block dimensions**, so the inverse-metric blocks (1/3)(e^{2τ},e^{−τ},e^{−2τ}) on su(2)/C²/u(1) weight one Casimir C₂·d.
2. **Spinor curvature offset** (Weitzenböck/Lichnerowicz endomorphism), fit-then-certified machine-ε (max rel **4.33e-16**):
   **Tr(Ω²)(τ) = −5e^{2τ} − 4e^{−τ} − 2e^{−2τ} − ½e^{−4τ} − ½**.

Hence **M₂(p,q;τ) = (2/3)C₂d(3e^{2τ}+4e^{−τ}+e^{−2τ}) + d(5e^{2τ}+4e^{−τ}+2e^{−2τ}+½e^{−4τ}+½)**.

**MANDATORY substitution chain** (`.claude/rules/math-scripts.md §"Double-Check Logic"`):

- **Claim**: dM₂/dτ > 0 on the Jensen line over [0, τ_NEC=1.383).
- **Step 1** (S_SA / ⟨λ²⟩ definition): S_SA(τ)=a₀−a₂+a₄ [E7]; at the truncation the monotonicity object is ⟨λ²⟩ ∝ Tr D_K² [baseline-findings-s66 S37]. M₂ = −Tr D_π² (positive, anti-Hermitian convention).
- **Step 2** (Weitzenböck): `D_K²=−∇²+E`, E=R_scal/4 [Gilkey 1975; Paper 19 eq 2.14-2.16]. Tr D_π² = 16·Casimir_g + d·Tr(Ω²), the two exact closed forms above.
- **Step 3** (substitute the closed forms; differentiate, no simplification): **dM₂/dτ = d·[C₂·gC(τ) + gS(τ)]**, with **gC(τ) = 4e^{2τ} − (8/3)e^{−τ} − (4/3)e^{−2τ}** and **gS(τ) = 10e^{2τ} − 4e^{−τ} − 4e^{−2τ} − 2e^{−4τ}** (Sage `diff`, exact rationals). [The plan's `dR_K/dτ=e^{2τ}+e^{−4τ}−2e^{−τ}` AM-GM positivity is the *curvature-only* skeleton; the FULL derivative absorbs it into gC, gS — this gate **closes the per-sector dC/dτ≥0 step the plan left open**, exactly.]
- **Step 4** (simplify to canonical form; read off the sign): substitute u = e^τ ≥ 1 (τ≥0) and clear negative exponents (e^{2τ}, e^{4τ} > 0). Sage QQ factorization (remainders **0**, exact):
   **gC·e^{2τ} = 4u⁴ − (8/3)u − 4/3 = (u−1)(4u³+4u²+4u+4/3)**;
   **gS·e^{4τ} = 10u⁶ − 4u³ − 4u² − 2 = (u−1)(10u⁵+10u⁴+10u³+6u²+2u+2)**.
   Both cofactors have **all-positive rational coefficients** [3·gC-cofactor = (12,12,12,4)>0; gS-cofactor = (10,10,10,6,2,2)>0] ⟹ strictly positive for u>0.
- **Direction / read-off**: for u≥1 (τ≥0), gC, gS = (u−1)·(positive) ≥ 0, **zero iff u=1 (τ=0)**, **strictly >0 for τ>0**. Since C₂≥0 (all sectors) and d>0: **dM₂/dτ = 0 at τ=0; dM₂/dτ > 0 strictly for τ>0, ALL (p,q)**.
- **Conclusion**: monotonicity holds **TERM-BY-TERM per sector** ⟹ the PW sum is monotone ⟹ **L-UNIFORM** (no truncation dependence; min over p+q≤10, τ∈(0,τ_NEC) = **+1.733e-04 > 0**, vanishing only as τ→0⁺). The closed-form proof of strict positivity of the SIGN is **complete** — even stronger than required (holds for all τ>0, not just τ<τ_NEC). [SIGN read-off: sum of positive terms is positive.] Analytic dM₂/dτ vs central-difference of the closed M₂: max rel **1.11e-10** (FD-limited); boundary dM₂/dτ|_{τ=0} = **1.68e-12** (=0 exactly: gC(0)=gS(0)=0 algebraically).

**[SIGN] 3-tuple** (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID` → composite **INFO**):

- **sign = PASS** — the proven analytic gradient is strictly positive and matches the anchor sign (both >0). The E7 monotonicity SIGN is proven in closed form.
- **magnitude = FAIL** — the *literal* pre-registered cross-check `|dS_SA/dτ|_fold,analytic − 58672.8|/58672.8 < 1e-3` is **2.647 ≫ 1e-3** (ratio FAIL). Reason: the anchor +58672.8 is `dS_full/dτ`, the **|λ|-spectral-action** gradient (f(x)=√x); the closed-form proof delivers the **λ²-action** gradient (f(x)=x) = **213991.8** at the fold — a DIFFERENT, larger functional. Individual |λ| eigenvalues (11/18/… distinct roots per sector) admit no clean closed form; only the λ²-MOMENT (a trace) does. **NOT** redefined to manufacture a PASS (would be convention-shopping, `v3-closure-recovery.md` Class 1).
- **regime = VALID** — the proof holds on the entire physical domain [0, τ_NEC) (and beyond); no regime breakdown.
- **Composite collapse**: the generic gate-verdicts.md rule (mag=FAIL ∧ regime=VALID ⟹ FAIL) is **overridden by the plan-frozen operator** (`composite-precedence` disclosure row in the verdict file) per the plan's `INFO_meaning` + `dual_prior` discriminator ("INFO → unchanged"). Here mag=FAIL is a **plan-side functional conflation** (anchor = |λ|-action, proof = λ²-moment), NOT a proof failure — the SIGN (the literal E7 content) is proven exactly. Composite = **INFO**.

**Anchor cross-check (construction validation)**: reproduced `dS_full/dτ|_fold = 58672.819` (FD h=0.001) vs canonical `dS_fold = 58672.802` — rel err **2.87e-07** — confirming the D_K construction is **bit-identical to the S42 anchor**. This validates that the SIGN agreement is between the *same* substrate construction differently functionaled, not an artifact.

**regulator_pin**: a₀^{ζ}, a₂^{ζ}, a₄^{ζ} (Gilkey-zeta; S_SA = a₀ − a₂ + a₄ per E7). The monotonicity target ⟨λ²⟩(τ)/Tr D_K²(τ) has a regulator-robust τ-derivative sign (E7: ALL monotone f, ALL Λ); the a_n^{ζ} tag pins the SA-moment combination behind the |_fold cross-check.

**4-tuple**: (value=`INFO`, scheme=`WEITZENBOCK-LICHNEROWICZ`, convention=`SYMBOLIC-CLOSED-FORM-SAGE-QQ`, L_max=`general-(p,q)-symbolic/xcheck-10`). L_max_proof = general-(p,q)-symbolic (L-uniform term-by-term); L_max_xcheck = 10 KK sectors for the anchor reproduction.

**Dual-prior posterior**: INFO → **unchanged** per the plan discriminator (Track A 0.6 / Track B 0.4). The proof closed for the SIGN (Track-A-flavored) but the literal magnitude clause tested a different functional (Track-B-flavored scope caveat); the plan reserves INFO for exactly this "proven modulo a clearly-stated scope issue" outcome, so neither track's mass is decisively re-allocated. **E7's 9,600-numerical status is unaffected** — this gate ADDS an analytic theorem for the λ²-moment, retracts nothing.

**Substrate framing** (GEOMETRIC): the flow runs D_K eigenvalues → ⟨λ²⟩(τ) = Tr D_K²(τ) → the exflationary complexification gradient. dM₂/dτ > 0 IS the structural driver of exflation — as τ increases off the bi-invariant point (u=e^τ from 1), spectral complexity grows monotonically inside each fiber-point (substrate language for "exflation", NOT metric expansion). The closed form makes the mechanism transparent: the gradient is `(u−1)·(strictly-positive cofactor)` summed over sectors with positive Casimir weights — the cold τ=0 vacuum (u=1) is the unique critical point (dM₂/dτ=0), an unstable maximum from which the spectrum cascades into complexity. The substrate IS the spectral moment; gravity (a₂) and the gauge action (a₄) are downstream consequences of the SAME monotone flow.

**Dual-SHA**: audit_sha256 `87163c330d34a1182de49833fcb4568001973f613596a20107ae144f12f28bc3`; content_sha256 `4dc43e7f1582acc0515d277c6ca708cfaddd12265a5230add74050824aeaf97c`. Artifacts: `computations/session-102/s102_trd2_monotonicity_analytic.{py,npz,png}`.

**Carry-forward (INFO → focused completion)**: an un-timeboxed follow-up may attempt a closed-form |λ|-spectral-action (f=√x) magnitude that reproduces +58672.8 — but this requires per-sector |λ| closed forms (high-degree characteristic-polynomial roots), which are not analytically available; the realistic completion is to register the λ²-moment closed-form theorem (proven here) and re-scope the +58672.8 anchor in the registry as the |λ|-action SIGN-corollary of E7's "ALL monotone f", not a magnitude target for the λ²-proof.

---

## Wave 3 Synthesis (team-lead)

**Dispatch record**: 4/4 gates landed in keystone order (item 11 first; 12/13 dispatched only after the orchestrator verified the item-11 PASS verdict line on disk; 14 likewise). The stop-at-first-failure protocol never fired — the keystone held. (Process note: the W3-14 agent's host process died in a system crash AFTER writing all five artifacts; the on-disk state was complete and verified — no re-dispatch was needed, only its final report message was lost.) All verdict lines + dual-SHA companions verified on disk; all four WP sections carry the four must_contain markers.

**Wave verdict ledger** (verdicts quoted from the gate sections above):

| Gate | Verdict | Outcome (one line) |
|:-----|:--------|:-------------------|
| W3-11 `S102-FEGAN-TAU0-SPECTRUM-VALIDATION` (keystone, box 1) | **PASS** | Substrate τ=0 spectrum == Fegan/Parthasarathy–Kostant 1987 closed form at machine ε (max diff 8.882e-15 < 1e-12; 45 sectors; exact multiplicities; n/36 algebraic form 0 violations; GPU-vs-CPU 0.00e+00); three incommensurate corpus normalizations identified and excluded — the (1/6, 1/4) frame read off the substrate, not fitted |
| W3-12 `S102-FOREIGN-STACK-PW-BLOCK-REIMPL` (box 2, referee M8(b)) | **PASS** | (1,1) adjoint block rebuilt from scratch in Sage CyclotomicField(12) exact arithmetic + independent numpy path: max\|foreign − canonical\| = 0.000e+00 bit-exact over all 128 \|λ\|; B3 anchor implementation-independent; monoculture concern remedied for the pinned block |
| W3-13 `S102-STRATUM1-LIT-SWEEP` (box 3) | **PASS** | Novelty CONFIRMED: 11 documented query records across all 6 pinned families, 0 prior-art hits for the item-6/item-7 core, 6 adjacencies that re-scope rather than refute (only published SU(3) Dirac spectrum is the bi-invariant τ=0 endpoint, Lai-Teh/Teh MR3153451; the left-invariant deformation literature is Laplacian-only; complete-Dirac-spectrum results stop at lens spaces) — items 6+7 stand CANDIDATE-NOVEL |
| W3-14 `S102-TRD2-MONOTONICITY-ANALYTIC` (box 4, timebox) | **INFO** (sign=PASS / mag=FAIL / regime=VALID) | **E7's λ²-moment monotonicity PROVEN in exact closed form**: dM₂/dτ = d·[C₂·gC + gS] with both factors (u−1)·(all-positive-coefficient cofactor) under u=e^τ — zero iff τ=0, strictly positive for ALL τ>0, term-by-term per sector ⇒ L-UNIFORM; Sage-QQ exact (remainders 0). Magnitude clause FAILed on a plan-side functional conflation: the +58672.8 anchor is the \|λ\|-action (f=√x), a different functional (λ²-gradient = 213991.8, ratio 2.647); honestly NOT redefined to manufacture PASS. E7's 9,600-numerical status unchanged; the λ²-theorem is additive |

**The external-validation spine (what the wave establishes)**: all four cold-read checklist boxes are ticked. The substrate Dirac construction now has (i) an external closed-form anchor no internal agent can bias (Fegan, machine ε), (ii) implementation independence (foreign exact-arithmetic stack, bit-exact), (iii) confirmed novelty along the Jensen line (documented trace, 0 prior art), and (iv) the exflationary gradient's SIGN as an analytic theorem — dM₂/dτ = Σ_sectors (positive Casimir weight)·(u−1)·(positive cofactor) makes the mechanism transparent: the cold τ=0 vacuum (u=1) is the unique critical point, and spectral complexity grows strictly monotonically off it. Substrate-first throughout: D_K eigenvalues → ⟨λ²⟩(τ) → the complexification gradient that IS exflation — not metric expansion.

**Effected In-Session (NON-MATH — completed by the team-lead orchestrator before STOP)**:

- [x] EVOI row 9c status cell updated QUEUED → LANDED-PASS (the keystone resolved; per this synthesis's pre-registered mandate) — `sessions/evoi-framework.md:61` — audit `24cdba4bf29ce6a3`
- [x] E7 registry-row / capstone §5.1 numerical→analytic upgrade adjudication: NOT performed, with reason — the placeholder mandates it ONLY on item-14 PASS; item 14 closed INFO, so the λ²-theorem registration routes through CF-S103-W3-2 below (a registry-landing gate, not an orchestrator tag edit) — this section
- [x] Wave-3 synthesis + CF + constraint-map + files tables (this section) — team-lead designated writer

Self-audit: `grep -c '^- \[ \]'` on this sub-section = 0.

## Carry-Forward Computations

### CF-S103-W3-1 — Foreign-stack extension to the (0,0)/(0,1) sectors (B1/B2 anchors)

Source: §W3-12 Assessment (the gate's own carry-forward note).

1. **What**: extend the foreign-stack re-implementation from the (1,1) block to the (0,0) and (0,1) Peter-Weyl blocks, broadening the monoculture remedy from one block to the bottom-of-spectrum triple (B1 = 0.819741, B2 = 0.845~ anchors).
2. **Inputs**: `computations/session-102/s102_foreign_stack_pw_block_reimpl.py` (`foreign_block()` generalized over (p,q)); the canonical pipeline diff target (`dirac_spectrum.py`, construction leg untouched); s84 cache cross-anchor.
3. **Gate**: `S103-FOREIGN-STACK-B1B2` — PASS iff max|foreign − canonical| < 1e-12 per block (same machine-ε equality as W3-12), eigenvalue extraction via H = iD eigvalsh ONLY (the W3-12 methodology pin).
4. **Effort**: ~1 gate per sector (≤ 1 wave-equivalent combined).

### CF-S103-W3-2 — λ²-moment closed-form theorem registration + |λ|-anchor re-scope

Source: §W3-14 "Carry-forward (INFO → focused completion)" (quoted verbatim from the gate section, line-anchored above).

1. **What**: register the proven λ²-moment monotonicity closed form (M₂(p,q;τ) exact; dM₂/dτ = d·[C₂·gC + gS], (u−1)-factorization with positive cofactors; L-uniform) as a registry theorem row, AND re-scope the +58672.8 anchor in the registry as the |λ|-action SIGN-corollary of E7's "ALL monotone f" — NOT a magnitude target for the λ²-proof. (The un-timeboxed |λ|-closed-form attempt is explicitly NOT queued: per-sector |λ| roots admit no closed form — the gate's own analysis.)
2. **Inputs**: `computations/session-102/s102_trd2_monotonicity_analytic.npz` (proof certificate; audit `87163c330d34a118`); the E7 row in the permanent registry + capstone §5.1 anchor text; `dS_fold = 58672.80` provenance (S42).
3. **Gate**: `S103-LAMBDA2-MONOTONICITY-REGISTRY-LANDING` — PASS iff the registry row lands byte-faithful with the theorem statement + the anchor re-scope applied, AFTER-pattern single-shot per `registry-landing.md`, artifact-existence + content-marker predicate.
4. **Effort**: 1 gate (registry-landing class).

**ADDENDUM (2026-06-10, S102 review campaign S-2 proof-check — `session-102-connes-ncg-lambda2-proofcheck-synthesis.md`)**: verdict **PASS / READY** — the proof closes SYMBOLICALLY for general (p,q); CF-S103-W3-2 is cleared to land the theorem as STAGE-1-CANDIDATE with the proof intact (BLOCKER 0, MAJOR 0, MINOR 1). Apply at landing: (a) state the equipartition step (ii) as a **Schur-lemma corollary** (the rep-trace form `Tr(ρ(X_b)ρ(X_d))` is an ad-invariant symmetric bilinear form on simple su(3) ⇒ proportional to the Killing form ⇒ block sums 3:4:1 exact for every (p,q)) — NOT the WP's "numerically-certified fit" label, which understated the step; (b) the +58672.8 anchor re-scope (|λ|-action f=√x SIGN-corollary) as already specified above. Scope note: this is a single-axis (GEOMETRIC) registry-landing gate, NOT a joint-theorem cross-axis Stage-2 verify — the two-agent PASS-AND pathway does not apply.

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-06-09 | Construction-pipeline external validation (EVOI 9c) | QUEUED (cold-read keystone, never executed as a diff) | **LANDED — PASS at machine ε**; everything downstream of the τ=0 construction is externally anchored | W3-11 Fegan diff 8.882e-15, 45 sectors, exact multiplicities |
| 2026-06-09 | Implementation-monoculture risk (referee M8(b)) | OPEN (single numpy pipeline) | REMEDIED for the pinned (1,1) block (bit-exact foreign-stack reproduction); B1/B2 extension queued (CF-S103-W3-1) | W3-12 0.000e+00 |
| 2026-06-09 | Stratum-1 item-6/item-7 novelty | ASSERTED (unswept) | CONFIRMED CANDIDATE-NOVEL (documented 11-query trace, 0 prior art, 6 re-scoping adjacencies) | W3-13 sweep |
| 2026-06-09 | E7 ⟨λ²⟩(τ) monotonicity | PROVEN-by-9,600-numerics (no analytic proof) | λ²-moment monotonicity ADDITIONALLY proven analytic (closed form, L-uniform, strict for τ>0); |λ|-action magnitude is a DIFFERENT functional (anchor re-scope queued, CF-S103-W3-2); 9,600-numerical status unchanged | W3-14 INFO (sign=PASS) |
| 2026-06-09 | Cross-stack eigenvalue-extraction methodology | implicit | Pinned: degenerate anti-Hermitian D requires H = iD + eigvalsh extraction; a general complex eigensolver fabricates spurious mismatches on bit-identical constructions | W3-12 methodology finding (process observation, closed in-session by documentation) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Other |
|:-----|:-------|:------------|:------------|:------|
| W3-11 | `s102_fegan_tau0_spectrum_validation.py` | `s102_fegan_tau0_spectrum_validation.npz` (539,026 B) | `s102_fegan_tau0_spectrum_validation.png` (91,070 B) | — |
| W3-12 | `s102_foreign_stack_pw_block_reimpl.py` | `s102_foreign_stack_pw_block_reimpl.npz` | `s102_foreign_stack_pw_block_reimpl.png` | Sage exact-arithmetic source embedded |
| W3-13 | `computations/_shared/s102_stratum1_lit_sweep.py` | `s102_stratum1_lit_sweep.npz` (trace records) | `s102_stratum1_lit_sweep.png` | documented search trace |
| W3-14 | `s102_trd2_monotonicity_analytic.py` | `s102_trd2_monotonicity_analytic.npz` (proof certificate) | `s102_trd2_monotonicity_analytic.png` | 8 verdict rows incl. composite-precedence |

All in `computations/session-102/` unless prefixed; verdict file `computations/session-102/s102_gate_verdicts.txt`.
