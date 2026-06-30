---
name: inv11-w2-majorana-moment
description: INV11-W2-3 PASS — Majorana transition magnetic moment; diagonal μ=0 EXACT, texture-fixed μ_23/μ_13=0.998 (investigation-track, not yet session-promoted)
metadata:
  type: project
---

INV11-W2-3-MAJORANA-TRANSITION-MU — PASS (investigation track n=11, 2026-06-16).

**Result**: Two structurally-distinct claims, two confidence levels.
- Diagonal μ_ii = 0 EXACT (max|μ_ii|=0.0, antisym residual 0.0). Textbook Majorana-vertex selection rule (Schechter-Valle 1981 / Nieves 1982: self-conjugate field ⇒ moment matrix antisymmetric ⇒ 2μ_ii=0), here anchored to PROVEN [J,D_K]=0 / KO-dim=6. A DIAGONAL-μ detection FALSIFIES Majorana — a 2nd self-conjugacy channel beyond 0νββ (which tests lepton-number; this tests self-conjugacy directly).
- Transition ratio μ_23/μ_13 = 0.9979 (texture-fixed, zero-free-parameter; scale-cancel residual = 0.0 EXACT). μ_12/μ_13 = 0.0994. Magnitudes from the S60 M₃(ℂ) V_B3 texture off-diagonals (V12=0.007335, V13=0.073789, V23=0.073636 — loaded from s60_lepto_cp.npz). Near-unity μ_23/μ_13 reflects quasi-degenerate B3 texture (V23≈V13); μ_12 suppressed ~10× (V12 is the weak 1-2 coupling).

**Key structural insight** (re-usable): the Majorana MASS texture V_B3 is SYMMETRIC (Fermi statistics, S60 line 43) but the magnetic-MOMENT matrix is ANTISYMMETRIC (self-conjugacy selection rule) — OPPOSITE symmetry, DISTINCT objects. The texture supplies magnitudes |μ_ij|=V_ij; the selection rule supplies the antisymmetric sign structure. Don't conflate them.

**Provenance / inputs**: magneton μ_natural = 1/(2 M_KK) from MOMENT-46 (s46_phonon_magnetic_moment.py Eq.(3)/(5)); V_B3 from S60 s60_lepto_cp.npz (log SHA 49fdadc5… matches plan pin). M_KK_gravity=7.42866e16 GeV. Script `computations/investigation-11/inv11_w2_majorana_transition_mu.py`; verdict `computations/investigation-11/inv11_gate_verdicts.txt` (audit_sha256 bcb17a746cd2813f…).

**Status**: investigation-track ONLY — NOT yet session-promoted, NOT canonical anywhere. The μ_23/μ_13 ratio would become a `falsifier-master-inventory.md` row (mack sole-writer) ONLY at investigation-close session-promotion. Do NOT cite as canonical until promoted. Complements the J-forced δ_CP ∈ {0,π} [[s52_offjensen_pmns]] channel — both are self-conjugacy tests from [J,D_K]=0.
