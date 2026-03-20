# Session 31Ca: Bulk BCS Closure Computations (2026-03-02)

All results reinforce K-1e closure. No BCS escape route in BULK.

## N-31Ca: Density-dependent pairing = FAIL
- 11 envelopes (exp/gauss/hard) at 9 tau x 8 mu. ZERO enhancement over constant.
- max|eig(V_eff)| = 0.275 (3.6x below threshold). V_matrix ALREADY gap-edge concentrated.
- Nuclear surface pairing analogy BREAKS: no "volume" component exists to remove.
- Problem is ABSOLUTE SCALE of Kosmann elements (||V||~0.1-0.28), not distribution.

## N-31Cb: BCS convergence = FAIL
- N_eff = {2, 10, 16}: M_max(mu=0) monotonically increasing at all tau.
- N_eff=2: M_max=0 for tau>0 (V(gap,gap)=0 selection rule confirmed).
- Convergence decelerating: (M_16-M_10)/(M_10-M_2) = 0.01-0.10.
- M_inf(mu=0) ~ 0.107-0.155. Factor 7-10x below threshold even at N->inf.

## N-31Cf/Ci: No signal
- Odd-even staggering: featureless. Bayesian 3-fold convergence: BF=2.17 (below threshold 10).

## Output Files
- `tier0-archive/s31C{a,b,f,i}_*.{py,npz,png}`
