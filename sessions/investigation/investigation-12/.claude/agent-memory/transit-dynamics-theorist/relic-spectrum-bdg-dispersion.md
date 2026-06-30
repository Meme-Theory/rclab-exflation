---
name: relic-spectrum-bdg-dispersion
description: BdG dispersion convention for the relic Bogoliubov spectrum + the S101 pair-band identity (2|lambda| edges), pinned during INV12-W3-1
metadata:
  type: project
---

The relic Bogoliubov spectrum {beta_k} is computed on the D_K eigenvalue fabric with the substrate-canonical BdG quasiparticle dispersion (INV12-W3-1, FOUNDATIONAL gate).

**Dispersion convention (resolved INV12-W3-1):**
`omega_k(tau) = sqrt((lambda_k(tau) - mu)^2 + Delta_k^2)` with **mu = 0** (particle-hole symmetric chemical potential — `s36_multisector_ed_verdict.txt`: `mu = 0.0`; S76 sp-transit-workshop T2.1-T2.3 `omega_B = sqrt(eps_B^2 + Delta_BCS^2)`; S101 oddfloor `E_n(q=0) = |lambda_n|`). The investigation-12-plan-w3 §W3-1 writes `(lambda_k^2 - mu^2)^2` — this is a transcription of the standard BdG band energy `xi = (lambda - mu)`; with mu=0 both reduce to `lambda_k`. Use the canonical `(lambda_k - mu)^2 + Delta_k^2` form. `Delta_k = Delta_BCS = 0.4642547394830737` (aggregate; per-band GL gaps are `Delta_B1=0.371795, Delta_B2=0.732026, Delta_B3=0.176`, S95 W3-3).

**S101 pair-band identity (cross-check anchor):** the relic pair band `[1.6395, 10.8379]` from S101-W1-QEQ-RELIC-ODDFLOOR is `2*E_k` at the relic point where the S101 q-deformation sends Delta->0, so `E_k -> |lambda_k|`. EXACT identity verified against the L12 cache:
- lower edge `2*|lambda|_min = 2*0.819741 = 1.639482 ≈ 1.6395`
- upper edge `2*|lambda|_max(L<=12) = 2*5.418937 = 10.837874 ≈ 10.8379`
The L_max=10 bottom-band subset (78080 unique |lambda|, lam_max=4.670) gives `2*lam_max=9.34`; the 10.8379 upper edge is the L=12 band-top caveat (R1 in S101).

**Construction:** lambda_k(tau) trajectory built per Peter-Weyl (p,q) block via [[dirac-spectrum-gpu-eigvalsh]] (D_K block-diagonal; `jensen_metric(B_ab, s=tau)` -> frame E(tau) -> `dirac_operator_on_irrep`). Irreps are tau-INDEPENDENT and globally cached by `get_irrep`; only the frame/Omega depend on tau. Smooth across the fold: max adjacent-tau jump in sorted bottom-band spectrum = 0.0046 at dtau=0.0025 (no hard crossings corrupting sorted-mode tracking near tau_fold=0.190).

**Validated recipe predecessor:** S100b-BOX-DELTA-BOGOLIUBOV (`computations/session-100b/s100b_box_delta_bogoliubov.py`) — the box+delta SUDDEN-limit case where the transfer matrix IS exact (var_Nseg=1). The entire-function `C=cos(mu L), S=sin(mu L)/mu` (continuation mu->i Lambda for mu^2<0) + BD-in/out extraction + unitarity `|alpha|^2-|beta|^2=1` to TOL=1e-10 are reused. The SMOOTH fold (this gate) contrasts: piecewise-constant TM is artifact-prone (segment reflections), the high-accuracy ODE (Radau/DOP853, rtol<=1e-10) recovers the true squeeze. Prior soft-TM attempts: S64 TRANSFER-BOGOLIUBOV-64 (max/min=1.33), S85-W7-CUSP-BOGOLIUBOV FAIL (-2.019676) — the artifacts this gate retires.

**OUTCOME (INV12-W3-1, verdict INFO; audit_sha256=7915262f5cc74463...):** the INTEGRATOR LOCK is clean — integrator_agreement=7.76e-5, refine_agreement=3.32e-8, unitarity_residual=4.55e-15 (all PASS-level); box+delta sudden xcheck var_Nseg=1.0 EXACT. **INFO** (not PASS) because the relic-CONTENT carries a truncation band: rho_relic=15.41 @p+q<=7 -> 26.85 @p+q<=8 (rel 0.426), truncation_consistent=False. **Substrate-physics reading**: over the smooth fold window [0.14,0.24] the per-mode |beta_k|^2 is uniformly small (~1e-5 to 1e-3) and does NOT decay with |lambda| (the window is NEAR-ADIABATIC, |omega'/omega^2|<<1 because omega_k=sqrt(lambda^2+Delta_BCS^2) has a floor Delta_BCS=0.464 and lambda drifts only ~1% across the window), so summed rho_relic is dominated by the level^2 mode-count growth, NOT a bottom-band concentration. The per-mode {beta_k} IS locked (cutoff-robust); rho_relic over a FIXED band is well-defined but band-dependent. The canonical n_pairs=59.8 (S38) comes from the IMPULSIVE/sudden transit component (box+delta sector), NOT this smooth eigenvalue-drift sweep — consistent with "impulsive transit, not quasi-static". Downstream: W3-2/W3-4 consume per-mode {E_k,omega_k,beta_k} (cutoff-robust); W3-3 consumes rho_relic and MUST carry the band [15.41, 26.85]. npz `computations/investigation-12/inv12_w3_1_relic_spectrum_ode_lock.npz` keys incl. rho_relic_check, rho_trunc_rel for W3-3. Casimir-bounded operational ceiling p+q<=7 (36 sectors), check p+q<=8 (44).
