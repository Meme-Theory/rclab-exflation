# Session 27 Plan: Honest Redux of Session 26 Findings

## Context

Session 26 produced three major computations (P1 BCS, P2 cooling, P3 a₆) but the Baptista audit identified two categories of problems:

1. **The "Seeley-DeWitt monotonicity theorem"** — claimed for ALL orders but only proven through a₆. The induction argument fails because Gilkey coefficients have mixed signs at higher orders. This is a **conjecture**, not a theorem.

2. **Gate T-1 (torsion gap)** — was never actually tested. The scripts computed an interpolation `D(t) = M_Lie + (1-t)M_Ω` (removing pieces of D_K), NOT the gate-defined `D_T = D_K + (1/4)K_abc·γᵃγᵇγᶜ` (adding contorsion). The gate remains PENDING.

Additionally, multi-sector BCS was identified as the #1 priority but never computed, and the "structural floor" claim at 3-5% was premature given this gap.

Session 27 corrects these by running the computations that should have been run.

---

## Priorities (3 total, no scope creep)

### Priority 1: T-1 Torsion Gap Gate (THE ACTUAL TEST)

**Goal**: Directly compute `D_T = D_K + (1/4) K_abc γᵃγᵇγᶜ` and compare its spectral gap to D_K.

**Why this matters**: T-1 is the only untested gate from the preplan. Session 26 computed torsion diagnostics (norms, decomposition ratios, interpolation) but never built the actual torsion-modified Dirac operator. The Bismut-Friedrich-Agricola theorem (totally antisymmetric torsion strengthens gaps) provides headwind, but 27% of SU(3)'s Schouten torsion is NOT totally antisymmetric — that 27% could weaken the gap.

**What to compute**:

1. **Implement contorsion tensor** from Schouten torsion:
   ```
   K_abc = (1/2)(T_abc - T_bac + T_cab)
   ```
   where T⁰_abc = ft[a,b,c] (ON-frame structure constants, already computed in s26_torsion_diagnostics.py).

   NOTE on convention: The torsion of the canonical (Cartan) connection on a Lie group is T(X,Y) = -[X,Y]. In the ON frame this becomes T⁰_abc = -ft[a,b,c]. The contorsion is:
   ```
   K^c_ab = (1/2)(T^c_ab + g^{cd}g_{ae}T^e_db + g^{cd}g_{be}T^e_da)
   ```
   In ON frame (g=delta): K_abc = (1/2)(T_abc + T_bac - T_cab) ... BUT we must be careful with index placement. The standard reference (Nakahara Ch 7.4) gives:
   ```
   K^c_ab = (1/2)(T^c_ab + T_a^c_b + T_b^c_a)
   ```
   Verify against known result: for bi-invariant metric (tau=0), the canonical connection has Gamma_canon = 0, so K = -Gamma_LC. Check that Omega_torsion = -Omega_LC at tau=0 (D_T = D_K - 2*Omega should give the "flat" Dirac operator on the group).

2. **Construct torsion spinor offset**:
   ```
   Omega_T = (1/4) sum_{a,b,c} K^b_ac * gamma_a @ gamma_b @ gamma_c
   ```
   Using the SAME `spinor_connection_offset()` function with K instead of Gamma_LC.

3. **Build torsion-modified Dirac operator**:
   ```
   D_T = D_K + I ⊗ Omega_T
   ```
   This adds the contorsion to the existing Levi-Civita Dirac operator.

4. **Sweep tau ∈ [0, 0.50] at 21 points** (matching existing grid). For each tau and each sector (0,0), (1,0), (0,1), (1,1):
   - Compute eigenvalues of D_K (already cached in .npz files)
   - Compute eigenvalues of D_T
   - Record gap_K = min|λ_K| and gap_T = min|λ_T|

5. **Gate T-1 verdict**:
   - PASS: gap_T < gap_K at any tau ∈ [0, 0.5] → torsion weakens the gap
   - CLOSED: gap_T ≥ gap_K at all tau → torsion strengthens/preserves gap everywhere

**Validation cross-checks**:
- At tau=0 (bi-invariant): K_abc should equal -Gamma^LC_abc (canonical connection is flat). D_T should equal D_0 (Lie algebra piece only). Verify eigenvalues match.
- Omega_T should be anti-Hermitian (same as Omega_LC).
- D_T should have purely imaginary eigenvalues at all tau.

**Script**: `tier0-computation/s27_torsion_gap_gate.py`
**Output**: `tier0-computation/s27_torsion_gap_gate.npz`
**Time estimate**: ~2 hrs (21 tau values × 4 sectors × eigenvalue solve)

**Files to modify/create**:
- NEW: `tier0-computation/s27_torsion_gap_gate.py`
- READ: `tier0-computation/tier1_dirac_spectrum.py` (import infrastructure)
- READ: `tier0-computation/s26_torsion_diagnostics.py` (reuse `compute_torsion_from_code()`)

---

### Priority 2: Correct the a₆ "Theorem" Claim

**Goal**: Downgrade the "Seeley-DeWitt monotonicity theorem for all orders" to a properly scoped conjecture, and document exactly what IS proven vs what is conjectured.

**What IS proven** (and stays proven):
- a₂(tau) monotonically increasing ✓ (Session 20)
- a₄(tau) monotonically increasing ✓ (Session 20)
- a₆(tau) monotonically increasing ✓ (Session 26, 6 cross-checks at machine epsilon)
- V_spec^(6)(tau; rho, sigma) has no minimum for sigma ≥ 0 ✓ (10,100-point scan)
- B-1 minimum at a₄ truncation is destroyed by a₆ ✓

**What is NOT proven** (and should not be called a theorem):
- "All a_{2n}(tau) monotonically increasing" — CONJECTURE
- The induction step claims: "all Riemann tensor components increase monotonically, therefore degree-n polynomials in them increase monotonically." This fails because:
  - I₇ and I₈ are NEGATIVE (-1/8 and -1/32 at tau=0)
  - Gilkey coefficients at order n ≥ 4 have mixed signs
  - A polynomial with mixed-sign coefficients on mixed-sign inputs CAN be non-monotonic

**What to write**: A corrections section in the session-27 wrapup that:
1. States the three proven monotonicity results (a₂, a₄, a₆) as individual facts
2. Labels "all orders" as the **SDW monotonicity conjecture** (not theorem)
3. Notes the Omega³ coefficient uncertainty (35 ± ~7, from Avramidi vs Vassilevich conventions)
4. Documents that the B-1 destruction is independent of the "all orders" claim — it only needs a₆

**No new computation needed.** This is a documentation correction.

**File to create**: Corrections section in `sessions/session-27/session-27-wrapup.md`

---

### Priority 3: Multi-Sector BCS (the uncomputed #1 priority)

**Goal**: Extend the singlet (0,0) BCS computation to 9 sectors with p+q ≤ 3.

**Why this matters**: Session 26 computed BCS only in the 16-mode (0,0) singlet. The wrapup correctly identified multi-sector BCS as the highest-priority remaining computation. The "structural floor" at 3-5% was declared prematurely — if ANY sector shows F_cond with a minimum at finite tau, the locking game reopens.

**What to compute**:

1. For each sector (p,q) with p+q ≤ 3 (9 sectors total):
   - **(0,0)**: 16 modes — regression test against s26_multimode_bcs.py
   - **(1,0)**: 48 modes (fundamental, dim=3)
   - **(0,1)**: 48 modes (anti-fundamental, dim=3)
   - **(1,1)**: 128 modes (adjoint, dim=8)
   - **(2,0)**: 96 modes (symmetric, dim=6)
   - **(0,2)**: 96 modes (anti-symmetric, dim=6)
   - **(3,0)**: 160 modes (dim=10)
   - **(0,3)**: 160 modes (dim=10)
   - **(2,1)**: 240 modes (dim=15)
   — NOTE: (1,2) is conjugate to (2,1) and will have identical |F_cond|. Compute (2,1) only, note symmetry.

   For each sector:
   - Load D_K eigenvalues from existing tier1 data (or compute fresh)
   - Compute Kosmann K_a matrices in that sector (extending s23a methodology)
   - Build V_nm pairing matrix: V_nm = sum_{a=3,4,5,6} |<n|K_a|m>|²
   - Run BCS self-consistent iteration at mu = {0, 0.5, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2, 1.5, 2.0, 3.0} × lambda_min
   - Record: M_max(tau, mu), Delta(tau, mu), F_cond(tau, mu)

2. Compute TOTAL condensation energy:
   ```
   F_total(tau) = sum_{(p,q)} mult(p,q) × F_cond^{(p,q)}(tau)
   ```
   where mult(p,q) = dim(p,q)² counts the multiplicity of sector (p,q) in the Peter-Weyl decomposition.

3. **Check tau profile**: Does F_total(tau) have a minimum at some tau > 0? Or does it peak at tau=0 like the singlet?

**Gate**: If F_total has a minimum at tau_0 ∈ (0, 0.5]: **RESCUE** (multi-sector BCS locks tau).
If F_total is monotonically decreasing from tau=0: **CLOSED** (multi-sector BCS doesn't help).

**Prerequisite**: Need Kosmann matrices per sector. The s23a computation only generated them for (0,0). The `tier1_dirac_spectrum.py` infrastructure supports arbitrary (p,q) via `get_irrep()` and `dirac_operator_on_irrep()`, but the Kosmann derivative computation needs to be extended.

**Key consideration for large sectors**: (2,1) has 240 modes → 240×240 BCS kernel. Self-consistent iteration may need 10-50k steps. Budget ~30 min per sector per tau value for the largest sectors.

**Script**: `tier0-computation/s27_multisector_bcs.py`
**Output**: `tier0-computation/s27_multisector_bcs.npz`
**Time estimate**: ~12-20 hrs (9 sectors × 9 tau × 12 mu values, sector sizes 16-240 modes)

**Files to modify/create**:
- NEW: `tier0-computation/s27_multisector_bcs.py`
- READ: `tier0-computation/s26_multimode_bcs.py` (reuse BCS iteration logic)
- READ: `tier0-computation/s23a_kosmann_singlet.npz` (reference for (0,0) validation)
- READ: `tier0-computation/tier1_dirac_spectrum.py` (sector infrastructure)

---

## What is NOT in this plan (and why)

| Excluded Item | Reason |
|:---|:---|
| Cooling trajectory re-run | P2 closure is qualitatively valid for singlet. Re-run only if P3 (multi-sector) changes the F_cond profile. |
| Paper 18 modified Lie derivative | Important but theoretical — requires reading Paper 18 carefully first, not a computation priority. |
| Exact V_spec at B-1 parameters | Session 24a already showed exact eigenvalue sums are monotone. B-1 was always Seeley-DeWitt only. |
| Resonant cavity interpretation | Gain profile wrong shape in singlet. Wait for multi-sector results. |
| GSL balance / No-boundary mu | Retracted by their proponent (Hawking). Closed. |
| (1,2) sector BCS | Conjugate to (2,1) — identical |F_cond| by CPT. Compute (2,1) only. |

---

## Execution Order

1. **P1 (T-1 gate)** — Independent of everything else. Can run immediately. ~2 hrs.
2. **P2 (a₆ correction)** — Documentation only. Write after P1 finishes. ~30 min.
3. **P3 (multi-sector BCS)** — Largest computation. 9 sectors, p+q ≤ 3. Start after P1 validates infrastructure. ~12-20 hrs.

P1 and P3 are independent and can run in parallel. P1 uses the Dirac operator infrastructure for torsion; P3 uses it for Kosmann matrices per sector. No shared state beyond tier1_dirac_spectrum.py imports.

**If P1 reveals torsion weakens the gap**: Re-run P3 with torsion-modified spectrum (D_T eigenvalues as BCS input instead of D_K). This is a contingent P3b that only triggers on T-1 PASS.

---

## Verification Plan

### P1 Verification:
1. At tau=0: D_T eigenvalues should match the "flat" canonical-connection Dirac operator (Omega_T = -Omega_LC → D_T = D_K - 2*I⊗Omega)
2. Omega_T should be anti-Hermitian at all tau
3. D_T eigenvalues should be purely imaginary at all tau (max real part < 1e-12)
4. Compare gap_T vs gap_K numerically — tabulate all 21 tau values
5. Cross-check: at tau=0, the canonical connection on SU(3) is flat, so D_T should be the "Lie algebra Dirac operator" M_Lie. Compare eigenvalues against Session 26's `D(t=1)` from `s26_torsion_resonance_detail.py`.

### P2 Verification:
- Read the corrected wrapup section and confirm it accurately distinguishes proven facts from conjectures

### P3 Verification:
1. (0,0) sector results should reproduce s26_multimode_bcs.py exactly (regression test)
2. Kosmann matrices K_a in each sector should satisfy: K_a = -K_a^T (antisymmetric in mode indices) — this is the Lie derivative antisymmetry
3. V_nm = sum_a |<n|K_a|m>|² should be symmetric positive semi-definite
4. BCS convergence to tolerance 1e-13 in all sectors
5. F_total(tau) profile: plot and inspect for minima
