## Wave 1: BCS-Accessible Pi-Phase Ratio (3 tasks)

S46 reported 131 PW-weighted pi-phase states / 59.8 quasiparticle pairs = 2.19x and called this "topologically available / dynamically realized." The ratio is wrong because the numerator includes ALL pi-phase states — B1 states that cannot pair (Trap 1: V(B1,B1)=0), B3 states that may lack K₇-compatible partners, and B2 states that may be K₇-blocked. The correct numerator is the BCS-ACCESSIBLE pi-phase count after applying all established selection rules. This wave computes it.

**User hypothesis**: the 2.19x discrepancy comes from inflating the numerator with inert channels. The true ratio may be close to 1 within the active sector.

---

### W1-1: Sector Classification of Pi-Phase States (PI-SECTOR-47)

**Agent**: `spectral-geometer`
**Model**: opus
**Cost**: LOW (data extraction + eigenvalue clustering)

**Prompt**:

You are classifying each of the 13 unweighted (131 PW-weighted) pi-phase states from S46 by their B1/B2/B3 sector membership. The S46 berry phase computation tracked eigenvalue flow across tau but never assigned sectors. Without this assignment, the pi-phase count is an undifferentiated bulk number that mixes active and inert channels.

**Verified data locations** (all keys confirmed to exist):

- `tier0-computation/s46_berry_phase.npz`:
  - `sXY_berry_phases: shape=(N,)` — berry phase per spinor eigenvalue for rep (X,Y)
  - `sXY_evals: shape=(40, N)` — eigenvalue trajectory, 40 tau values × N spinor components
  - `sXY_n_pi` — integer count of pi-phases in rep (X,Y)
  - `tau_grid: shape=(40,)` — the 40 tau values used
  - Reps with pi-phases: s01(1), s02(1), s03(2), s10(1), s11(1), s20(1), s21(5), s30(1)
  - Reps with zero pi-phases: s00(0)

- `tier0-computation/s44_dos_tau.npz`:
  - `tau0.19_all_omega: shape=(992,)` — full eigenvalue spectrum at fold (for cluster boundary calibration)
  - `tau0.19_all_dim2: shape=(992,)` — PW degeneracies per eigenvalue

- `tier0-computation/s35_k7_dphys.npz`:
  - `evals_DK: shape=(16,)` — (0,0) rep eigenvalues at fold. Unique |values|: 0.8197 (B1), 0.8452 (B2), 0.9714 (B3)

- `tier0-computation/s46_rg_pair_transfer.npz`:
  - `mode_eps: shape=(8,)` — 8-mode eigenvalues: [0.819, 0.833, 0.841, 0.849, 0.857, 0.973, 0.978, 0.983]
  - `mode_sector: shape=(8,)` — ['B1','B2','B2','B2','B2','B3','B3','B3']

**Computation Steps**:

1. **Establish cluster boundaries.** Load `tau0.19_all_omega` (992 eigenvalues at fold). Histogram them. Identify the three clusters (B1, B2, B3) and the gaps between them. The 8-mode model gives reference points: B1 ≈ 0.819, B2 ≈ 0.833–0.857, B3 ≈ 0.973–0.983. Find the natural gaps in the full 992-mode spectrum that separate these clusters. Report the cluster boundaries (e.g., B1 < 0.83, 0.83 < B2 < 0.92, B3 > 0.92).

2. **For each rep with pi-phases**, load `sXY_evals` and `sXY_berry_phases`. Find the tau index closest to 0.19 (the fold) in `tau_grid`. At that tau, extract the eigenvalues |sXY_evals[tau_idx, :]|. For each eigenvalue with berry_phase ≈ ±π (|phase| > 2.8), record its |eigenvalue| at the fold.

3. **Assign sectors.** Using the cluster boundaries from step 1, classify each pi-phase eigenvalue as B1, B2, or B3.

4. **Build the sector-resolved pi-phase table.**

   | Rep (p,q) | dim(p,q) | n_pi | Pi-phase eigenvalue(s) | Sector(s) | PW-weighted count |
   |:----------|:---------|:-----|:-----------------------|:----------|:------------------|
   | (0,1)     | 3        | 1    | ?                      | ?         | 3                 |
   | (0,2)     | 6        | 1    | ?                      | ?         | 6                 |
   | ...       | ...      | ...  | ...                    | ...       | ...               |
   | Total     |          | 13   |                        |           | 131               |

   Then sum PW-weighted counts by sector: PW_pi(B1), PW_pi(B2), PW_pi(B3).

**Pre-registered gate PI-SECTOR-47**:
- PASS: All 13 pi-phases classifiable. Report sector distribution.
- FAIL: Any pi-phase eigenvalue falls in a gap between clusters (ambiguous assignment).

**Output files**:
- Script: `tier0-computation/s47_pi_sector.py`
- Data: `tier0-computation/s47_pi_sector.npz`

**Working paper section**: W1-1

**Critical notes**:
- The `sXY_evals` arrays contain SIGNED eigenvalues. Take absolute values for clustering (B1/B2/B3 are defined by |λ|).
- The (2,1) rep has 5 pi-phases — the most of any rep. Its 240 spinor eigenvalues span a wide range. Some may be in B2, others in B3. Do NOT assume all pi-phases from one rep are in the same sector.
- dim(p,q) = (p+1)(q+1)(p+q+2)/2. Verified: (0,1)→3, (0,2)→6, (0,3)→10, (1,0)→3, (1,1)→8, (2,0)→6, (2,1)→15, (3,0)→10.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.

---

### W1-2: K₇ Selection Filter on Pi-Phase States (K7-FILTER-47)

**Agent**: `dirac-antimatter-theorist`
**Model**: opus
**Cost**: LOW–MEDIUM (K₇ eigenvalue computation for higher reps)
**Depends**: W1-1

**Prompt**:

You are applying the K₇ selection rules to the sector-classified pi-phase states from W1-1. Established results:

- `[iK₇, D_K] = 0` at all tau (S34). K₇ is an exact quantum number.
- Cooper pairs carry K₇ charge ±1/2 (S35). V(q+, q-) = 0 exactly — cross-charge pairing is forbidden.
- At tau > 0, K₇ charges quantize to ±1/4 in the (0,0) rep (s35_k7_thouless: `q_vals_pos_all` and `q_vals_neg_all` are all ±0.25 for tau > 0).
- V(B1,B1) = 0 exact (Trap 1, S34). B1 pi-phases are inert regardless of K₇.

The question: for the pi-phase states classified as B2 and B3 in W1-1, do their K₇ charges allow Cooper pairing?

**Verified data locations**:

- `tier0-computation/s47_pi_sector.npz` (from W1-1): sector assignments per pi-phase state
- `tier0-computation/s35_k7_thouless.npz`:
  - `q_vals_pos_all: shape=(9,4)` — K₇ charges for positive eigenvalues at 9 tau values. At tau > 0: all ±0.25
  - `q_vals_neg_all: shape=(9,4)` — same for negative eigenvalues
  - `V_pm_max: shape=(9,)` — cross-charge V. Machine zero (~10⁻²⁹) at tau > 0
  - `V_B2_charge_all: shape=(9,4,4)` — V matrix resolved by K₇ charge
  - `q7_conserved_through_fold: True`
- `tier0-computation/s35_k7_dphys.npz`:
  - `evals_DK: shape=(16,)` — eigenvalues for (0,0) rep
  - K₇ charge data is for (0,0) rep ONLY

**Computation Steps**:

1. **K₇ charges for (0,0) rep are known.** From s35_k7_thouless: at the fold (tau=0.2, index 3), q_vals_pos = [-0.25, -0.25, 0.25, 0.25] and q_vals_neg = [-0.25, -0.25, 0.25, 0.25]. Each eigenvalue has K₇ = ±1/4. Pairing requires same charge: (+1/4, +1/4) → total K₇ = +1/2, or (-1/4, -1/4) → total K₇ = -1/2.

2. **K₇ charges for higher (p,q) reps.** The s35 data covers only (0,0). For reps with pi-phases [(0,1), (0,2), (0,3), (1,0), (1,1), (2,0), (2,1), (3,0)], compute the K₇ eigenvalues from representation theory:
   - K₇ = iλ₇ acts on the (p,q) rep of SU(3)
   - In the (p,q) rep tensored with the spinor, the K₇ eigenvalues are sums of the rep weight's K₇ component and the spinor K₇ eigenvalue
   - Alternatively: compute [K₇, D_K] = 0 implies D_K is block-diagonal in K₇ eigenspaces. The eigenvalues of K₇ on the spinor bundle over SU(3) in the (p,q) sector determine which modes can pair.
   - If this computation is too expensive, use the STRUCTURAL ARGUMENT: since [iK₇, D_K] = 0 at all tau, every eigenvalue of D_K has a definite K₇ charge. Since V(q+, q-) = 0, pairing can only occur between modes with the same K₇. The pi-phase is a property of eigenvalue flow, which preserves K₇ charge (since K₇ is conserved). Therefore, a pi-phase state has a definite K₇ charge and can pair with any other state of the same charge in its sector — provided V(sector, sector) ≠ 0.

3. **Apply the filter.**
   - B1 pi-phases: REMOVE (V(B1,B1) = 0, Trap 1)
   - B2 pi-phases with K₇ = +1/4: CAN pair with other B2 states at +1/4 (V(B2,B2) = 0.256, nonzero)
   - B2 pi-phases with K₇ = -1/4: CAN pair with other B2 states at -1/4
   - B3 pi-phases: CAN pair within B3 (V(B3,B3) = 0.0034, small but nonzero) or with B2 (V(B2,B3) = 0.029)
   - NET: B2 + B3 pi-phases are BCS-accessible. Only B1 is removed.

4. **Report the BCS-accessible pi-phase count.**
   - PW_accessible = PW_pi(B2) + PW_pi(B3) from W1-1
   - PW_inert = PW_pi(B1) from W1-1
   - Verify: PW_accessible + PW_inert = 131

**Pre-registered gate K7-FILTER-47**:
- PASS: PW_accessible < 131 (some channels filtered). Report the number.
- INFO: If PW_accessible = 131 (no B1 pi-phases exist), then the 2.19x discrepancy is NOT from base-mixing. Escalate.
- KILL: If structural argument fails and K₇ charges cannot be determined, flag data gap.

**Output files**:
- Script: `tier0-computation/s47_k7_filter.py`
- Data: `tier0-computation/s47_k7_filter.npz`

**Working paper section**: W1-2

**Critical notes**:
- The K₇ charge computation for higher reps may require building the K₇ matrix in the (p,q) ⊗ spinor representation. Use the structure constants of su(3) and the (p,q) weight system. The canonical_constants.py module has the structure constants.
- If the structural argument (step 2, last bullet) suffices, the computation is trivial: just check whether each pi-phase is in B1 (remove) or B2/B3 (keep).
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.

---

### W1-3: Corrected Ratio and S46 Audit (RATIO-CORRECT-47)

**Agent**: `feynman-theorist`
**Model**: opus
**Cost**: LOW (arithmetic on W1-1 and W1-2 results)
**Depends**: W1-1, W1-2

**Prompt**:

You are constructing the corrected ratio using BCS-accessible pi-phase counts from W1-2 and sector-resolved pair counts from existing data. The S46 claim of 2.19x used the FULL pi-phase count (131) as numerator. You are replacing it with the BCS-ACCESSIBLE count and computing sector-matched ratios.

**Verified data locations**:

- `tier0-computation/s47_pi_sector.npz` (from W1-1): sector-resolved PW-weighted pi-phase counts
- `tier0-computation/s47_k7_filter.npz` (from W1-2): BCS-accessible PW-weighted count
- `tier0-computation/s46_number_projected_bcs.npz`:
  - `v2_bcs: shape=(3,)` — [0.045, 0.122, 0.002] BCS v² per sector (B1, B2, B3)
  - `n_sector_ed_N1: shape=(3,)` — [0.094, 0.224, 0.003] ED sector occupations
  - `Delta_bcs_fold: shape=(3,)` — [0.372, 0.732, 0.084] BCS gaps
  - `V_mat_constrained: shape=(3,3)` — sector V matrix
- `tier0-computation/s46_rg_pair_transfer.npz`:
  - `n_pairs_gs: 1.0` — total pairs in 8-mode ED
  - `n_occ: shape=(8,)` — per-mode occupation [0.494, 0.126, 0.124, 0.122, 0.120, 0.005, 0.005, 0.005]
  - `mode_sector: ['B1','B2','B2','B2','B2','B3','B3','B3']`
- `tier0-computation/s38_cc_instanton.npz`:
  - `mult_k: shape=(3,)` — [1, 4, 3] sector multiplicities in 992-mode system

**Computation Steps**:

1. **Sector-resolved pair counts.** Two bases exist:
   - **8-mode ED**: n_occ by sector: B1=0.494, B2=0.492 (sum of 4 modes), B3=0.015 (sum of 3 modes). Total = 1.000 pairs.
   - **992-mode BCS**: v2_bcs × PW degeneracy per sector. The v2_bcs values are per-representative-mode. Scale by the number of PW-degenerate modes in each sector (from `tau0.19_all_omega` or from the sector multiplicities in the full spectrum).

   Report both bases. DO NOT MIX.

2. **Compute three ratios.**

   | Label | Numerator | Denominator | Interpretation |
   |:------|:----------|:------------|:---------------|
   | R_raw (S46) | 131 (all pi-phases) | 59.8 (all pairs, 992-mode) | WRONG — mixed bases |
   | R_accessible | PW_accessible (from W1-2) | 59.8 | Partially corrected — accessible only |
   | R_B2 | PW_pi(B2) (from W1-1) | N_pairs(B2, same system) | Sector-matched — the RIGHT ratio |

3. **Interpret R_B2.**
   - R_B2 ≈ 1 → topology and dynamics are matched within the active sector. The 2.19x was entirely base-mixing artifact.
   - R_B2 ≈ 2 → one topological channel per mode pair. Structural BDI result.
   - R_B2 >> 2 → genuine topological selectivity within B2.
   - R_B2 << 0.5 → more pairing than topology predicts. Non-topological channels active.

4. **S46 audit.** Write a correction notice:
   - What was wrong: the 131 included B1 and possibly B3 channels that cannot participate in BCS pairing
   - What survives: the narrative that "topology provides a menu, dynamics selects from it" may survive, but the quantitative ratio retracts
   - The corrected number: state R_accessible and R_B2 explicitly

5. **Denominator consistency check.** The 59.8 pairs (992-mode quench, S38) and the 1.000 pairs (8-mode ED, S46) are different systems. The ratio should compare like with like. If PW-weighted pi-phases come from the 992-mode system (they do — max_pq_sum=3 covers all 992 modes), then the denominator must also be 992-mode. Report whether this is achievable from existing data or whether a new 992-mode BCS pair count is needed.

**Pre-registered gate RATIO-CORRECT-47**:
- PASS: R_B2 computable and finite. Report value.
- INFO: If R_B2 ≈ 1 (within factor 2), the S46 discrepancy is resolved as base-mixing.
- ESCALATE: If R_B2 > 5 or < 0.1, the topology-dynamics relationship needs reexamination.

**Output files**:
- Script: `tier0-computation/s47_ratio_correct.py`
- Data: `tier0-computation/s47_ratio_correct.npz`

**Working paper section**: W1-3

**Critical notes**:
- The S46 2.19x was computed as total_pi_weighted (131) / n_pairs from S38 quench (59.8). Both numbers are individually correct. The error is that the numerator counts channels the denominator's dynamics cannot access.
- The v2_bcs values in s46_number_projected_bcs are per-representative-mode in the 8-mode model. To get 992-mode pair counts, you need to scale by the PW degeneracies. The `tau0.19_all_dim2: shape=(992,)` in s44_dos_tau gives these.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
