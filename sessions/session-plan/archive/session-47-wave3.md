## Wave 3: Paasch Spiral Test on Full Dirac Spectrum (1 task)

S12 established phi_paasch = m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15 (z=3.65). Paasch's framework organizes particle masses on a logarithmic spiral m(phi) = m_0 * e^{k*phi} with k = (1/2pi) * ln(1.53158). The question has never been asked of the FULL Dirac spectrum: do the 992 eigenvalues (max_pq_sum=3) or 2912 eigenvalues (max_pq_sum=4) accumulate on discrete sequences when mapped onto this spiral?

This is zero-cost — existing eigenvalue data, one logarithmic transformation, pattern check.

---

### W3-1: Paasch Spiral Analysis of Dirac Spectrum (PAASCH-SPIRAL-47)

**Agent**: `paasch-mass-quantization-analyst`
**Model**: opus
**Cost**: LOW (logarithmic mapping of existing eigenvalue data)

**Prompt**:

You are testing whether the full Dirac eigenvalue spectrum on Jensen-deformed SU(3) exhibits the discrete sequence structure predicted by your logarithmic mass quantization framework. This is your question to answer.

**Background**: Your quantization factor phi = 1.53158 was found in the Dirac spectrum at S12: the ratio m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15. But that was a single ratio between two specific eigenvalues. The full spectrum has 992 eigenvalues at max_pq_sum=3 and potentially 2912 at max_pq_sum=4. If your framework is correct, the eigenvalues should organize into discrete sequences when mapped onto the logarithmic spiral.

**Your spiral**: m(phi) = m_0 * e^{k*phi} where k = ln(1.53158) / (2*pi). On this spiral, masses separated by the quantization factor phi sit at angular spacing 2*pi (one full turn). Masses within the SAME sequence sit at integer multiples of some base angular spacing.

**Verified data locations**:

- `tier0-computation/s44_dos_tau.npz`:
  - `tau0.19_all_omega: shape=(992,)` — full eigenvalue spectrum at fold (tau=0.19)
  - `tau0.19_all_dim2: shape=(992,)` — PW degeneracies
  - `tau0.15_all_omega: shape=(992,)` — spectrum at tau=0.15 (where phi was originally found)
  - `tau0.15_all_dim2: shape=(992,)` — PW degeneracies at tau=0.15
  - `tau0.00_all_omega: shape=(992,)` — spectrum at bi-invariant point
  - Available tau values: 0.00, 0.05, 0.10, 0.15, 0.19

- `tier0-computation/s46_max_pq_sum_4.npz` — may contain higher-truncation data (check if it has eigenvalues at max_pq_sum=4)

- `tier0-computation/s47_pi_sector.npz` (from W1-1):
  - Sector assignments (B1/B2/B3) for the 992 modes

- `tier0-computation/s47_spectral_landscape.npz`:
  - Processed spectrum data with sector coloring

- `tier0-computation/canonical_constants.py`:
  - `phi_paasch` if available, or compute from the known value 1.531580

**Computation Steps**:

1. **Load the spectrum.** Get all unique eigenvalues |lambda| at the fold (tau=0.19) from tau0.19_all_omega. There are 992 total but many are degenerate within (p,q) reps — extract the unique values and their multiplicities/degeneracies.

2. **Map onto the Paasch spiral.** For each unique eigenvalue lambda_i:
   - Compute the spiral angle: phi_i = (1/k) * ln(lambda_i / lambda_min) where k = ln(1.53158) / (2*pi) and lambda_min is the smallest eigenvalue
   - Compute the fractional turn: phi_i / (2*pi) — this gives the number of spiral turns from the minimum eigenvalue
   - Compute the phase within one turn: phi_i mod (2*pi) — this is the angular position on the spiral

3. **Check for sequence structure.** If the eigenvalues organize into discrete sequences, the phases (phi_i mod 2*pi) should cluster at specific angular positions rather than being uniformly distributed. Compute:
   - Histogram of (phi_i mod 2*pi) with ~36 bins (10-degree resolution)
   - The Rayleigh test for non-uniformity (circular statistics)
   - The number of distinct clusters (peaks in the angular histogram)
   - For each cluster: how many eigenvalues, from which (p,q) reps, which sectors (B1/B2/B3)

4. **Repeat at tau=0.15.** This is where phi_paasch was originally found. Compare the angular distribution at tau=0.15 vs tau=0.19. Does the sequence structure sharpen or blur as tau changes?

5. **Repeat at tau=0.00** (bi-invariant). At the highest symmetry point, the spectrum is maximally degenerate. How many distinct sequences exist here? This is the baseline.

6. **Check max_pq_sum=4 if available.** If s46_max_pq_sum_4.npz contains eigenvalues at higher truncation, repeat the analysis with 2912 modes. Do new eigenvalues fall INTO existing sequences or create new ones?

7. **Cross-reference with sectors.** Do the sequences align with B1/B2/B3 sectors? If each sequence corresponds to one sector, the spiral structure is just encoding the sector splitting. If sequences cut across sectors, that's more interesting.

8. **The phi ratio test.** For all pairs of eigenvalues (lambda_i, lambda_j) with lambda_j/lambda_i close to phi = 1.53158 (within 1%), count how many such pairs exist. Compare to the expected count from a random spectrum with the same density of states. If the phi ratio is genuinely preferred, there should be a statistically significant excess.

9. **Visualize.**
   - **Plot A**: The Paasch spiral. Polar plot with radius = |lambda|, angle = phi_i mod (2*pi). Each eigenvalue as a dot, colored by sector (B1/B2/B3), sized by PW degeneracy. If sequences exist, they appear as radial lines.
   - **Plot B**: Angular histogram of (phi_i mod 2*pi) at each of the 5 tau values. Shows whether sequence structure emerges, sharpens, or blurs with deformation.
   - **Plot C**: Ratio histogram. For all nearest-neighbor eigenvalue ratios lambda_{i+1}/lambda_i, histogram them. Mark phi = 1.53158. Is there a peak at phi?

**Pre-registered gate PAASCH-SPIRAL-47**:
- PASS: Rayleigh test rejects uniformity at p < 0.01 AND at least 3 distinct angular clusters identified
- INFO: Weak clustering (p < 0.05) or fewer than 3 clusters
- FAIL: Phases consistent with uniform distribution (p > 0.05) — no sequence structure

**Output files**:
- Script: `tier0-computation/s47_paasch_spiral.py`
- Data: `tier0-computation/s47_paasch_spiral.npz`
- Plot: `tier0-computation/s47_paasch_spiral.png`

**Working paper section**: W3-1

**Critical notes**:
- The original phi_paasch = 1.531580 was found at tau=0.15, not at the fold tau=0.19. The ratio may drift with tau. Check both.
- The 992 eigenvalues include massive degeneracies (same eigenvalue appearing dim(p,q)² times in PW counting). Work with UNIQUE eigenvalues for the spiral analysis, but report the PW-weighted version too.
- The spectrum ranges from 0.820 to 2.061 at the fold — only about 1.3 octaves. This means at most ~0.6 full turns of the Paasch spiral. Sequence structure may require more spectral range (higher max_pq_sum) to be visible.
- This is YOUR question. If the answer is negative (uniform distribution), that's a clean result: the Dirac spectrum does not inherit Paasch sequence structure at this truncation level. If positive, it's a discovery.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
