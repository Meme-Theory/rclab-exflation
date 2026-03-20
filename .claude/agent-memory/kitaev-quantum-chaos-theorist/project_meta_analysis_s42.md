---
name: S42 Meta-Analysis Library Audit
description: Results of meta-analysis audit of researchers/Kitaev/ folder, identifying critical gaps in integrability/GGE literature
type: project
---

## Library Audit (2026-03-13)

14 papers on file, well-covered on chaos (SYK, MSS, BGS, Berry-Tabor, OTOCs). Critical gaps in integrability/GGE/prethermalization -- the regime the framework ACTUALLY operates in (S38 verdict: integrable at all levels).

**Why:** S38 proved system is integrable, so the chaos library is over-indexed. The missing physics is: Richardson-Gaudin integrability (the BCS model IS one), GGE construction/exactness (the post-transit state IS one), and weak integrability breaking (the fabric coupling MAY be one).

**How to apply:** Priority A papers (Dukelsky RMP 2004, Rigol PRL 2007 + Nature 2008, Claeys thesis 2018, Yuzbashyan PRB 2005, D'Alessio review 2016) should be acquired and read before any future chaos computation. The key open question is GGE permanence in the extended fabric -- requires Bertini-Essler prethermalization analysis with lambda_eff from Z(tau)=74,731 and m_tau=2.062.

## Key Connection: S42 Fabric Stiffness

Z(tau) = 74,731 is the integrability-breaking perturbation strength for the fabric. But m_tau = 2.062 M_KK means the coupling is exponentially suppressed at distances >> 1/m_tau ~ 10^{-25} m. Expected: lambda_eff ~ exp(-m_tau * d) -> astronomically small -> t_therm >> t_Hubble -> GGE permanence protected by mass gap.

## Output
Written to: `agent-requests/kitaev-request.md`
