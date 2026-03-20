## Wave 3b: Phi_Paasch Under BdG Quasiparticle Dressing (1 task)

W3-1 established that the bare Dirac spectrum has no Paasch sequence structure (FAIL, p=0.70). But the bare spectrum is not what a 4D observer sees — the BCS condensate dresses the eigenvalues into BdG quasiparticle energies E_qp = sqrt(xi^2 + Delta^2). The phi_paasch ratio m_{(3,0)}/m_{(0,0)} = 1.531580 was found in the BARE spectrum at tau=0.15. Under BCS dressing with tau-dependent gaps, this ratio shifts. Does it cross phi at a different tau? Does BCS dressing CREATE or DESTROY the phi relationship?

This is computable from existing data: sector-resolved gaps Delta(tau) from s46_qtheory_selfconsistent.npz and eigenvalues from s44_dos_tau.npz.

---

### W3-2: BdG-Dressed Phi Ratio Across Tau (PHI-BDG-47)

**Agent**: `paasch-mass-quantization-analyst`
**Model**: opus
**Cost**: LOW (algebraic evaluation of existing data)

**Prompt**:

Your W3-1 result showed the bare Dirac spectrum has no global Paasch sequence structure. But the ratio phi_paasch = m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15 IS real in the bare spectrum. Now you're asking: what happens to this ratio when BCS dressing is applied?

**The physics**: The BCS condensate turns bare eigenvalues lambda_k into BdG quasiparticle energies:

  E_qp(k) = sqrt(xi_k^2 + Delta_sector(k)^2)

where xi_k = |lambda_k| - mu (with mu=0 forced by PH symmetry, so xi_k = |lambda_k|) and Delta_sector(k) is the BCS gap in the sector containing mode k.

The key: B1 and B3 have DIFFERENT gaps. Delta_B1 = 0.372 (proximity-induced via V(B1,B2)), Delta_B3 = 0.084 (proximity-induced via V(B2,B3)). These gaps are tau-dependent. So:

  R_dressed(tau) = E_qp(3,0) / E_qp(0,0)
                 = sqrt(lambda_{(3,0)}^2 + Delta_B3(tau)^2) / sqrt(lambda_{(0,0)}^2 + Delta_B1(tau)^2)

This ratio differs from the bare ratio R_bare(tau) = lambda_{(3,0)} / lambda_{(0,0)} because the gaps add differently in quadrature — the smaller eigenvalue (B1) gets a proportionally larger BCS correction than the larger eigenvalue (B3).

**Context from prior sessions**:
- S24a: phi is inter-sector only, zero crossings in (0,0) singlet at fixed tau without BCS
- S27: BCS exp(-1/M) destroys phi structure in the gap-dressed spectrum (but this was for the full spectrum, not the specific B3/B1 ratio)
- S46: B3 gap is proximity-induced by B2 through V(B2,B3) = 0.029, not self-consistent
- W3-1: bare spectrum has no global sequence structure, but the (0,0) singlet phi ratio is a structural fact of that sector

**Verified data locations**:

- `tier0-computation/s44_dos_tau.npz`:
  - `tau0.XX_all_omega: shape=(992,)` at tau = 0.00, 0.05, 0.10, 0.15, 0.19
  - Contains the (0,0) sector eigenvalues at each tau (the first 16 of the 992, or identifiable by dim²=1)

- `tier0-computation/s46_qtheory_selfconsistent.npz`:
  - `Delta_B1_sc: shape=(60,)` — self-consistent B1 gap vs tau
  - `Delta_B2_sc: shape=(60,)` — self-consistent B2 gap vs tau
  - `Delta_B3_sc: shape=(60,)` — self-consistent B3 gap vs tau
  - `tau_scan: shape=(60,)` — tau values for the gap scan
  - `Delta_B1_fold: 0.3718`, `Delta_B2_fold: 0.7320`, `Delta_B3_fold: 0.0842`

- `tier0-computation/s46_number_projected_bcs.npz`:
  - `Delta_bcs_fold: shape=(3,)` — [0.372, 0.732, 0.084]
  - `v2_bcs: shape=(3,)` — [0.045, 0.122, 0.002]

- `tier0-computation/canonical_constants.py`

**Computation Steps**:

1. **Extract the (0,0) sector eigenvalues at each tau.** From s44_dos_tau, the (0,0) rep has 16 eigenvalues (dim²=1 in tau0.XX_all_dim2). At each tau, extract the 3 unique |eigenvalue| magnitudes: lambda_B1 (smallest), lambda_B2 (middle), lambda_B3 (largest). These are the (0,0) sector eigenvalues.

   At tau=0.19 (fold), from s35_k7_dphys: lambda_B1 = 0.8197, lambda_B2 = 0.8452, lambda_B3 = 0.9714.

2. **Compute the bare ratio R_bare(tau).** R_bare = lambda_B3 / lambda_B1 at each of the 5 available tau values. Verify R_bare(0.15) ≈ 1.5316 (the original phi_paasch).

3. **Interpolate the BCS gaps to the 5 tau values.** From s46_qtheory_selfconsistent: Delta_B1_sc(tau), Delta_B2_sc(tau), Delta_B3_sc(tau) are given on a 60-point tau_scan grid. Interpolate to the 5 tau values where eigenvalues are available.

4. **Compute the dressed ratio R_dressed(tau).** At each tau:

   R_dressed = sqrt(lambda_B3^2 + Delta_B3^2) / sqrt(lambda_B1^2 + Delta_B1^2)

5. **Find crossings.** Does R_dressed(tau) = phi_paasch = 1.53158 at any tau? If so, at what tau? Does it cross at a DIFFERENT tau than the bare crossing (tau ≈ 0.15)?

6. **Also compute on a finer grid.** Use the 60-point tau_scan from s46 to get the gap data, but you'll need eigenvalues at those tau values too. If eigenvalues are only available at 5 tau values, interpolate the eigenvalue ratios (they should vary smoothly).

   Better: the eigenvalue ratio lambda_B3/lambda_B1 in the (0,0) sector can be computed analytically from the Jensen metric. The Dirac operator on the (0,0) sector is a 16×16 matrix whose eigenvalues depend on tau through the metric. If canonical_constants.py or existing scripts provide the functional form, use it.

7. **Assess the BCS correction magnitude.** How much does BCS dressing shift the crossing tau? Report:
   - tau_crossing_bare (where R_bare = phi)
   - tau_crossing_dressed (where R_dressed = phi)
   - Delta_tau = tau_dressed - tau_bare
   - The fractional shift: does BCS pull the crossing toward or away from the fold?

8. **Check whether BCS creates NEW phi crossings.** The dressed ratio involves sqrt(lambda^2 + Delta^2), which is a nonlinear function. It's possible that R_dressed(tau) crosses phi_paasch at tau values where R_bare does NOT, or vice versa.

9. **Visualize.**
   - **Plot**: R_bare(tau) and R_dressed(tau) on the same axes, with a horizontal line at phi_paasch = 1.53158. Mark crossing points. Shade the region between bare and dressed curves to show the BCS correction magnitude.

**Pre-registered gate PHI-BDG-47**:
- PASS: R_dressed crosses phi at some tau in [0.05, 0.40]. Report the crossing tau.
- INFO: R_dressed crosses phi at the same tau as R_bare (BCS correction negligible).
- FAIL: R_dressed never crosses phi — BCS dressing destroys the phi relationship entirely.

**Output files**:
- Script: `tier0-computation/s47_phi_bdg.py`
- Data: `tier0-computation/s47_phi_bdg.npz`
- Plot: `tier0-computation/s47_phi_bdg.png`

**Working paper section**: W3-2

**Critical notes**:
- mu = 0 is forced by PH symmetry (S34). So xi_k = |lambda_k|, not |lambda_k| - mu.
- The B1 gap is PROXIMITY-INDUCED through V(B1,B2). It vanishes if V(B1,B2) → 0. The B3 gap is also proximity-induced through V(B2,B3).
- Delta_B1 > Delta_B3 (0.372 vs 0.084) despite V(B1,B1) = 0, because V(B1,B2) = 0.130 > V(B2,B3) = 0.029.
- The dressed ratio R_dressed < R_bare whenever Delta_B1 > Delta_B3 (the larger gap on the denominator pulls the ratio down). So BCS dressing should REDUCE the ratio, potentially shifting the crossing to larger tau.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
