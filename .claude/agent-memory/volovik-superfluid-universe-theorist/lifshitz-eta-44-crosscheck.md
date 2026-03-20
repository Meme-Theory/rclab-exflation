---
name: lifshitz-eta-44-crosscheck
description: S44 LIFSHITZ-ETA-44 cross-check results. FAIL ENDORSED with 5 flags. eta_eff is Weyl's law, not Lifshitz eta. True Lifshitz eta=0 (mean-field). Missing (1,2) sector in upstream data.
type: project
---

S44 LIFSHITZ-ETA-44 Cross-Check by Volovik (W1-3 review):

**Verdict**: ENDORSED (FAIL stands, with caveats)

**Key findings**:
1. All Landau numbers confirmed to machine precision (derivatives, stiffness, P(k))
2. eta_eff = 3.77 (Landau) or 4.22 (with (1,2) sector correction) -- both >> 0.1 threshold
3. Five flags raised: (F1) eta_eff is Weyl's law not Lifshitz eta; (F2) P=1/K wrong for sudden quench; (F3) 5-point power law unreliable; (F4) only tau mode computed; (F5) missing (1,2) sector in upstream data
4. True Lifshitz eta = 0 (mean-field, d=8 >> d_uc=3), giving n_s = 1 (also fails)
5. n_s is a 4D dynamical quantity (quench rate), not internal geometry property

**Upstream bug found**: Sector (1,2) missing from s43_phonon_dos.npz. Conjugate to (2,1), has same eigenvalues, dim=15, C_2=5.333. Should double n_phys at C_2=5.333. Makes FAIL worse (eta goes from 3.77 to 4.22).

**Physical conclusion**: n_s requires Friedmann-BCS coupled dynamics or DIMFLOW route. Internal geometry alone is structurally excluded for n_s.

**Why:** The Lifshitz transition on SU(3) has d=8 >> d_uc, so mean-field is exact. The stiffness scaling from Weyl's law is geometric, not a critical exponent.

**How to apply:** Any future n_s computation should use Bogoliubov coefficients from the quench dynamics, not spectral action stiffness. The DIMFLOW-44 route is the remaining path.

Files:
- `tier0-archive/s44_lifshitz_eta_crosscheck.py` (verification script)
- `tier0-archive/s44_lifshitz_eta_crosscheck.npz` (results)
- `sessions/archive/session-44/session-44-results-workingpaper.md` (review in W1-3 section)
