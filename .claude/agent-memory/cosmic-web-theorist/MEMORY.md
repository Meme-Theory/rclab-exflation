# Cosmic-Web-Theorist Agent Memory

## Reference Files
- [Anomaly landscape](meta_analysis_anomaly_update.md) -- LSS anomaly snapshot 2026-03-13 + S70 bulk-flow correction. Use as on-ramp to "what's still live."
- Unified constraint map: `../constraint-map.md` (project-wide, not duplicated here).
- Cosmic-web paper corpus: `researchers/Cosmic-Web/` (39 papers, indexed S43). Key citations: V02-E6 (Volovik), BK18-E6/E7, D17-E1/E3/E4, D19 (DESI DR2), Pr28 (persistent Betti), WM37 (skepticism), La38 (SN systematics), V39 (first law dS).
- Canonical numerical predictions live in `computations/_shared/canonical_constants.py` (w0_FW, wa_FW, sigma_8, planck_ns, alpha_s_*). Do NOT duplicate values here -- query canonical and cite.

## Operating Directives
- **Quantitative-first classification (S58 lesson)**: when a computation produces a number, compare to threshold quantitatively before classifying as marginal / confirmed / dismissed. Do not pre-judge new inputs by prior closures.
- **Substrate framing**: framework derives LCDM parameters; LCDM uses them. PASS-by-LCDM-match is evidence (zero free params), not "neutral." See user-memory `feedback_reporting-framing.md`.
- **Domain parochialism trap**: an LSS-domain "no signal" does not undercount a framework with non-LSS observation surfaces. Apply uniqueness criterion: would another model match the prediction?
- **Volovik tracking caveat (S67)**: constant chi reproduces LCDM identically; framework's w_0=-0.918 is the SEPARATE effacement-residual effect, not a "modification of tracking dynamics."

## Closed Tests (one-line ledger)
- Volume-averaged statistics (P(k), xi(r), VSF, Minkowski, genus, persistent Betti): CLOSED S43. k_transition=9.4e23 h/Mpc.
- Tessellation to giant structures: CLOSED S43 at all N_cell.
- Emergent G_eff: triple-closed. Persistent homology from sector-dependent gravity: triple-closed.
- Cosmic strings Gmu~10^-4: EXCLUDED by Planck CMB (S58). Domain-wall GW: GHz frequencies, no detector.
- Substrate compaction w_a (S66): wrong sign +1.121 vs DESI. Ruled out.
- Volovik exact tracking (S67): chi=const is LCDM identically.
- Transit GW for LISA (S69): f_peak~10^12 Hz, Omega(LISA)=8.3e-58. S58 prediction RETRACTED.
- Off-Jensen z''/z for A_s (S69): delta=2.82e-4 << 0.1. Negligible.
- Folded f_NL via Euclid bispectrum (S69): SNR=0.007. Outside reach.
- Bulk-flow discrimination (S70 W4-E): chi_3 SNR=0.064 vs cosmic variance.
- Scheme dependence: n_s sign depends on cutoff function; only sqrt(x) gives red tilt. All P(k)-derived predictions inherit this conditional.

## Live Discriminating Tests
| Observable | Instrument | Timeline |
|:-----------|:-----------|:---------|
| w_0, w_a (DR3 sub-tree) | DESI DR3 | ~2027 |
| n_s, alpha_s, Delta_N_eff | CMB-S4 | ~2030 |
| f*sigma_8 (~4% below LCDM) | DESI 5yr / Euclid | ~2028 |
| c_s^2, f_NL flavors | 21cm intensity (l>30k) | ~2040s |

## Session Pointers (compressed)
- S43 closures: foundation; volume-averaged + tessellation + k_transition all permanent.
- S49 (DELETED detail file): w_0 in [-0.43,-0.59] passed at B_1D=20.9; SUPERSEDED by S50 BAO exclusion.
- S58: Volovik partition pins w_0=-0.918. Cosmic strings excluded.
- S66 (DELETED detail file): w_a wrong-sign closure, Leggett-only DM resolves f_DM bottleneck, alpha_s scheme-dependent live.
- S67-S70: full LSS scorecard; f*sig8 + SNe outperform LCDM; BAO highest tension at LRG2 z=0.706 (-2.26 sigma); transit GW closed; bulk-flow undiscriminating.

For all numerical scorecard values (chi^2/dof, Delta chi^2, residuals, sigma counts), query `sessions/permanent-results-registry.md` or the relevant `s{N}_gate_verdicts.txt`. Do not re-pin values into agent memory.
