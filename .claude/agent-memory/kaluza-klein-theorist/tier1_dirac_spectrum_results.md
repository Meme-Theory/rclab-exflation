# Tier 1: Dirac Spectrum on (SU(3), g_s) (compressed)

## Script & Conventions
- `tier0-computation/tier1_dirac_spectrum.py` (~1573 lines). Runtime: ~30s full s-sweep.
- Anti-Hermitian generators: e_a = -i/2 * lambda_a, Tr(e_a e_b) = -1/2 delta_{ab}
- Structure constants: [e_a, e_b] = f_{abc} e_c. Killing form: B_{ab} = -3*delta_{ab}.
- D_K is ANTI-Hermitian (math convention). Report |eigenvalue| as magnitudes.
- Reductive: u(2) = {lambda_1,2,3,8}, m = {lambda_4,5,6,7}
- Jensen: g_s|_{u(2)} = g_0, g_s|_m = e^{2s} g_0 (one-parameter simplification)

## Bi-invariant Spectrum (s=0)
All lambda^2 = n/36: {25,27,37,45,49,61,63,73,75,79,81,91,93,97,109,117}/36
- 16 distinct positive eigenvalues from 9 irreps (p+q<=3)
- Connection Gamma = f/2. Omega anti-Hermitian, max |entry| = sqrt(3)/2.

## Phi Search: Sector-Specific MATCH
- Pooled analysis: NEGATIVE. No systematic phi-clustering at any s.
- **SECTOR-SPECIFIC**: (3,0)/(0,0) ratio = 1.531588 at s=0.15 (0.0005% from phi=1.53158)
- At s=0: sqrt(7/3) = 1.5275 (0.26% low). Peak 1.5374 at s~0.08. Crosses phi descending at s~0.15.
- IVT margin: 0.38% (max exceeds phi by only this much).
- (3,0) UNIQUELY saturates Parthasarathy bound: lambda^2*36 = 63 = pred 63.

## Eigenvalue Data (s=0, lambda^2*36)
- (0,0): {27}. (1,0): {25,37,49}. (1,1): {27,45,63,75}. (2,0): {37,49,61,79}.
- (2,1): {49,61,73,91,97,109}. (3,0): {63,81,93,117}.
- Parthasarathy match: ONLY (3,0) at minimum eigenvalue.

## Physical Meaning
- (0,0) = trivial rep (pure spinor curvature) -> lightest mass
- (3,0) = Sym^3(C^3), dim=10 -> heavy species
- Ratio is SECTOR-SPECIFIC: lowest mass from each species

## Bug History (RESOLVED)
- Initial script had wrong metric (uniform m-stretch). Corrected to 3-scale Jensen.
