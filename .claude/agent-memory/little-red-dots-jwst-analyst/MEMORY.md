# Little-Red-Dots-JWST-Analyst Agent Memory

## Operating Principles
- **No probability estimation.** Sagan owns probabilities. This agent delivers structural truths, observational constraints, surviving solution space.
- **Evaluate numerically before classifying.** Signals above detection threshold are detections. Do not default to "marginal" or "observational degeneracy" without quantitative justification.
- **Pre-registered evidence only.** Only new computational results against pre-registered gates change knowledge state.
- **Three competing LRD interpretive frameworks** (use as triage in any LRD analysis):
  1. Super-Eddington BH in dense gas envelope (Papers 11, 15, 24)
  2. Accreting DCBH (Papers 08, 16, 17)
  3. Compact star-forming galaxies (Paper 23: BIC prefers galaxy-only for 75%)

## Paper Corpus
- Location: `researchers/Little-Red-Dots/` (66 papers + AGENTS.md + index.md)
- Index: `researchers/Little-Red-Dots/index.md`

## AMRI-Promoted Registries (project-level, query these first)
All LRD watchlist + framework-prediction tables are AMRI-promoted (2026-04-23, retained clean as of 2026-04-28). Cite registry, not memory:

- **LRD observational constraints**: `sessions/framework/registry/lrd-observational-constraints.md`
- **Live falsifier watchlist (6-channel)**: `sessions/framework/registry/falsifier-watchlist.md` (cited as Input-SHA by S85-W4-4 / S85-W4-8 historically)
- **Framework DM properties** (f_DM = 0.209 partition bottleneck): `sessions/framework/framework-dm-properties.md`
- **Closed GW channels**: `sessions/framework/registry/closed-gw-channels.md` (cosmic strings / domain walls / Kibble-Zurek)
- **CASCADE-DYN-37 (Open Avenue)**: `sessions/framework/framework-bbn-hypothesis.md` (line 169 row) and `sessions/evoi-framework.md`

## Agent-Private Notes

### Math errors I have made (do not repeat)
- **L_Edd**: use `1.3e38 * (M / M_sun)`, NOT `1.3e38 * (M / 10^8)`
- **G-cancellation trap (S100b W7-2)**: under a borrowed-(H_0, Omega, sigma_8) baseline, an "emergent-G vs G_N" halo-abundance comparison above a fixed-T_vir threshold is EXACTLY zero by structural identity (M_ACH ~ 1/G and rho_m0 ~ 1/G cancel; with m = M/rho_m0 every mass-function factor is G-free). Never present the 0-dex residual as empirical chain evidence — the content is the G_eff/G_N head diagnostic + the ABSOLUTE abundance level. Declare per math-scripts.md multiplicative-cancellation discipline.
- **Emergent-G reconstruction that works (non-circular)**: 1/(16π G_eff) = f2_dict_CC(92.0) × M_KK_gravity² × a_2_FW_zeta/(48π²) → G_eff/G_N = 0.996729 (0.33% = f2~92 dictionary rounding); three independent lineages (S42 anchor, S88 a_2, S95 dictionary) vs CODATA M_Pl.
- **GW peak frequency**: `f_0 ~ T_ann * T_0 / M_Pl`. LISA (mHz) needs `T_ann ~ TeV`; PTA (nHz) needs `T_ann ~ MeV`; GUT-scale gives GHz. Always derive from `H(T) * a(T) / a_0`.
- **S58 Addendum 1 self-error**: Eq. A1 coefficient was wrong by 10.6 OOM. Never trust transcribed formulas without independent derivation.

### Session-history (compressed, no longer load-bearing)
- S34-S42: observational degeneracy established; CDM-like DM; 24-order gap permanent
- S49: w_0 detaches from LCDM (B_1D = 20.9 later overturned S50)
- S50: BAO excludes w_0 in [-0.43, -0.59]
- S56-S57: Fabric adiabatic-protection concern resolved (P_exc = 1.000 at physical quench rate)
- S58: Volovik partition moves w_0 to -0.918 (LIVE test); f_DM = 0.209 sole bottleneck; w_0 + w_a are surviving cosmological discriminants
