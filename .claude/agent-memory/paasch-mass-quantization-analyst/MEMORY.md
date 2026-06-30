# Paasch Mass Quantization Analyst - Memory

## Reference Files
- [Paasch Reference](paasch-reference.md) — Numerics, OCR errata, gate registry, structural verdicts, file paths
- [S110 CV2C Ô-interface](s110-cv2c-ointerface-coupled.md) — AGREE→AGREE-COUPLED PASS, but carried by (3,0)/(0,0)→75/49, NOT BCS pairing-window gaps (~4% off)

## Core Status (one-screen verdict map)
- **phi_paasch = bare-spectrum property at tau=0.15**: D_K mathematical property, not physical observable (BCS destroys it; PHI-BDG-47 FAIL).
- **Sole surviving Paasch-NCG bridge**: n3 = dim(3,0) = #sectors(p+q<=3) = 10 (exact SU(3) identity). alpha(n3=10) = 0.9 ppm from CODATA.
- **No spiral structure in NCG eigenvalues**: PAASCH-SPIRAL-47 FAIL (uniform), SIX-SEQUENCE-48 FAIL.
- **No logarithmic potential in NCG**: Casimir potential is POLYNOMIAL (S56). PAASCH-CC CLOSED.
- **27 equilibrium closures** (S40 HESS): linear SA dead, compound nucleus paradigm (transit, not equilibrium).
- **LOG-SIGNED-40 is the ONLY open Paasch gate**. Single-point S_signed(0.19)=+787.773; tau sweep needs Dirac recomputation.

## Quick-Cite Numerics (full table in paasch-reference.md)
| Quantity | Value | Note |
|----------|-------|------|
| phi_paasch | 1.5315844 | from x=e^{-x^2} |
| alpha | 0.007297359 | 0.9 ppm vs CODATA |
| m_proton | 1.67262110e-27 kg | 4.9e-7 vs PDG |
| fN | 1.236068 = 2/golden = sqrt(5)-1 | applies to M-values (NOT 2*golden=3.236; corpus-wide label error, Sage-checked S95 capstone review) |
| sqrt(7/3) | 1.527525 | D_K round-metric (tau=0) |
| phi crossing | tau = 0.1499 | s22a_paasch_curve.npz |
| dump point | tau = 0.190 | s33w3_paasch_dump_point.py |
| n3 = dim(3,0) | 10 (= T_4) | sole Paasch-NCG identity |
| phi_paasch^fN | 1.693734 | S0=phi^fN is a NEAR-MISS not identity: vs S0=1.694153 dev=4.19e-4 (dead band), vs 95/56 dev=2.69e-3 (FAIL). Sage pre-flight INV3-W3 plan-freeze 2026-06-14. UB4 "4 sig figs" is a coincidence, not machine-eps. |
| Koide Foot angle | 44.9997 deg | Q=2/3 <=> cos^2(theta)=1/2 <=> 45 deg EXACT (PDG Q=0.66666051). Casimir-envelope sectors C2=(4/3,3,6) for (1,0)/(1,1)/(3,0). INV3-W3-5 tests Z3-forcing of the 45deg. |
| N(j)=7n vs SU(3) dims | 35,42 ARE dims; 7,98,150 NOT | 7 is not an irrep dim -> 7n likely a mode-MULTIPLICITY unit, not a dimension. N(p)/N(K)=150/98=1.5306 (0.06% from phi). INV3-W3-4 tests Casimir-graded mode count. |

## OCR Errata (cross-check ALL formulas numerically)
- N(j) exponent = 2/3 (NOT 1/2 from OCR)
- phi^{3/2} = 1.895438 (NOT 1.8985 garbled in 30+ docs)
- m_E = sqrt(m_e * m_p) = 21.9 MeV (NOT half muon)
- Paper 04 alpha formula OCR-garbled; only final numerical value reliable

## User Directives
- **S40**: Framework-First-Physics — stop re-gating known results; explore what is DIFFERENT.
- **S36**: "Give me the LAVA, not the tube." Focus on MASS CONTENT inside structures.
- **Scale anchor**: D_K eigenvalues at M_KK ~ 10^16 GeV; physical masses 14 OOM below. Content lives in SPLITTINGS / RATIOS, not absolute eigenvalues.

## Library Notes
- **Washburn (Paper 45)**: Claims zero-free-parameter derivation of 12 fermion masses from golden ratio + 3-cube; Lean 4 verified. To be assessed if tasked.
- **Koide (Paper 47)**: Sumino mechanism — family gauge protects Q=2/3.
- Paasch corpus: 46 papers; 3 critical (02,03,11), 6 high, 5 medium, 2 low priority.

## Cross-Memory Note
phi_paasch + n3=10 are **canonical project results** (live in `canonical_constants.py` and `sessions/permanent-results-registry.md`); other agent memories cite these freely. Not AMRI — they are shared structural-knowledge anchors, not registry overlap.
