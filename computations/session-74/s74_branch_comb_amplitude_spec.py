#!/usr/bin/env python3
"""
S74 W4-DD: BRANCH-COMB-AMPLITUDE-SPEC-74 -- Spec-Only for S75+
===============================================================

Write the FULL-FIDELITY PROMPT SPECIFICATION for BRANCH-COMB-AMPLITUDE-74
(framework section 10 deferred item, depends on s75_transfer_function.py,
which itself depends on W1-E FRIEDMANN-FROM-A2-74).

This script does NOT execute the physics computation -- it produces
- a ready-to-run S75+ agent prompt (single, complete block),
- the list of canonical inputs the S75+ agent must import,
- the pre-registered gate criteria,
- and the packed .npz artefact the parent skill can dispatch verbatim.

Classification: PHONONIC (branch-comb modulation is the direct LSS imprint
of the 3-branch BCS squeezed vacuum).

Substrate framing (load-bearing for every prompt): the fabric is not IN
space -- space is an emergent description of how the fabric's spectral
weight distributes itself through D_K eigenvalue reorganization. The branch
comb is not "oscillations in space"; it is the structural imprint of the
3-branch BCS mode geometry on the emergent P(k), arising because each
branch contributes a different omega_n(tau), r_n(tau), and v_g,n(tau)
signature through the fold. The direction of explanation is
    D_K eigenvalues -> 8-mode BCS sector -> 3-branch squeezed vacuum
    -> s75 transfer function T_b(k) -> emergent P(k) comb
NOT the reverse.

Pre-registered gate (for this W4-DD spec task):
    BRANCH-COMB-AMPLITUDE-SPEC-74:
        PASS if the S75+ prompt is written in full-fidelity format
             with (a) objective statement, (b) computation steps,
             (c) explicit inputs w/ file paths, (d) explicit outputs,
             (e) pre-registered gate for the S75+ execution, and
             (f) substrate-framing correction preamble.
        INFO if the spec is drafted but missing one of (a-f).
        FAIL if the spec cannot be written (e.g., W1-E FAIL with no
             workaround statement).

Output artefacts:
    s74_branch_comb_amplitude_spec.npz : {prompt, inputs, gate, metadata}
    s74_branch_comb_amplitude_spec.png : (no plot -- spec-only, stub)

Session: S74 | Wave 4 | Agent: quantum-acoustics-theorist
"""

import os
import sys
import time
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    M_KK,
    tau_fold,
    xi_BCS,
    Delta_BCS,
    c_Gold,
    omega_L1,
    omega_L2,
    c_fabric,
    E_B1,
    E_B2_mean,
    E_B3_mean,
    Delta_B3,
    rho_B2_per_mode,
    N_dof_BCS,
)

t_start = time.time()

# ==============================================================================
# SECTION 1: Parent W4-CC SPEC (S75 transfer function) -- dependency statement
# ==============================================================================
# BRANCH-COMB-AMPLITUDE-74 cannot run until s75_transfer_function.py exists
# (W4-CC handoff) AND W1-E FRIEDMANN-FROM-A2-74 has produced the 4D H(z)
# calibration. The S75+ computation below is framed to be dispatchable the
# moment those two dependencies are satisfied.

DEPENDENCIES = {
    "W1-E": "s74_friedmann_from_a2.npz (H_0, tau->a(tau) map, H(z))",
    "W4-CC": "s75_transfer_function.py (s75_transfer_function.npz with T_b(k) for b in {B1, B2, B3})",
    "W2-A":  "s74_branch_nbar_dk.npz (branch-resolved n_bar, r_k, v_g per mode)",
    "S73A W1-A": "s73a_exit_horizon_bog.npz (r_k_bcs, omega_k_entry, per-mode Parker squeezing)",
    "S56":   "s56_gge_fabric.npz (8-mode BCS sector: omega_n(tau), eigenvectors)",
    "S72":   "s72_kappa_delta.npz (Delta(tau) quartic fit through fold)",
}

# ==============================================================================
# SECTION 2: Canonical physics inputs the S75+ agent will need
# ==============================================================================
# These are canonical constants from canonical_constants.py. They are
# numerical inputs the S75+ agent MUST import (not re-derive).

CANONICAL_INPUTS = {
    "M_KK (GeV)":      float(M_KK),
    "tau_fold":        float(tau_fold),
    "xi_BCS (M_KK^-1)": float(xi_BCS),
    "Delta_BCS (M_KK)": float(Delta_BCS),
    "c_Gold (M_KK units)": float(c_Gold),
    "c_BA (M_KK units, local in S73a/S74)": 0.399,  # (local) not yet in canonical_constants.py
    "c_L_group (M_KK units, local)": 0.025,         # (local) Leggett group velocity floor
    "omega_L1 (M_KK)": float(omega_L1),
    "omega_L2 (M_KK)": float(omega_L2),
    "E_B1 (M_KK)":     float(E_B1),
    "E_B2_mean (M_KK)": float(E_B2_mean),
    "E_B3_mean (M_KK)": float(E_B3_mean),
    "Delta_B3 (M_KK)": float(Delta_B3),
    "rho_B2_per_mode": float(rho_B2_per_mode),
    "N_dof_BCS":       int(N_dof_BCS),
    "idx_B1":          [4],
    "idx_B2":          [0, 1, 2, 3],
    "idx_B3":          [5, 6, 7],
}

# ==============================================================================
# SECTION 3: The full-fidelity S75+ prompt
# ==============================================================================
# The prompt below is what the parent skill will feed verbatim to the
# quantum-acoustics-theorist agent in S75+ to execute the branch-comb
# amplitude computation. It is self-contained: substrate framing, objective,
# inputs (with full file paths and canonical constants), computation steps
# (numbered, dimensionally tracked), outputs (script, data, plot, working
# paper section), and pre-registered gate with quantitative thresholds.

PROMPT_TEXT = r"""You are the quantum-acoustics-theorist. You have ONE task. Complete it and stop.

# Substrate Framing (MANDATORY -- read before computing)

The fabric is not IN space. Space is an emergent description of how the
fabric's spectral weight distributes itself through D_K eigenvalue
reorganization. The branch comb is not "oscillations in space"; it is the
structural imprint of the 3-branch BCS mode geometry (B1 acoustic, B2
flat, B3 dispersive) on the emergent 4D matter power spectrum P(k). Each
branch carries a characteristic (omega_n, r_n, v_g,n) triple through the
fold; the s75 transfer function T_b(k) projects these internal mode
signatures onto the observable wavenumber k in h/Mpc. The direction of
explanation is

    D_K eigenvalues -> 8-mode BCS sector -> branch-resolved squeezed vacuum
    -> s75 transfer function T_b(k) -> emergent P(k) comb.

Do not explain this result by invoking LCDM "density perturbations in an
expanding universe". The expanding-universe language is a projection, not
a mechanism. The mechanism is the branch structure of the post-fold
squeezed vacuum; the observable comb is its pullback to 4D through T_b(k).

# Task: BRANCH-COMB-AMPLITUDE-74 -- Amplitude of the 3-branch LSS comb on P(k)

Compute the amplitude Delta P / P of the branch-resolved comb modulation
on the emergent 4D matter power spectrum P(k) at Euclid-accessible scales
(k in [0.01, 0.3] h/Mpc), using the S75 transfer function and the branch
structure of the 8-mode BCS squeezed vacuum.

This feeds Gate 5 (PHASE-COHERENT-PRIMORDIAL-SIGNATURE) of section 9 in
the framework-parametric-amplification.md chapter. The pre-registered
framework expectation is "three overlapping combs of oscillations in
P(k) with amplitude ~2-3 percent set by n_k per mode and phase set by r_k
per mode, with B3 dominance n_k^B3 / n_k^total ~ 0.73". Your task is to
turn that qualitative expectation into numbers.

## Inputs (canonical -- import, do not re-derive)

1. From canonical_constants.py:
   - M_KK (GeV), tau_fold, xi_BCS (M_KK^-1), Delta_BCS (M_KK), c_Gold,
     omega_L1, omega_L2, E_B1, E_B2_mean, E_B3_mean, Delta_B3,
     rho_B2_per_mode, N_dof_BCS.
   - c_BA = 0.399 M_KK tagged (local) until promoted.
   - c_L_group = 0.025 M_KK tagged (local) Leggett floor.

2. From s74_friedmann_from_a2.npz (W1-E output):
   - H(z=0), H(z_eq), H(z_rec)
   - The M_KK -> (Mpc, h/Mpc) calibration chain: M_KK -> GeV -> length
     -> comoving length -> h/Mpc.

3. From s75_transfer_function.npz (W4-CC handoff, required):
   - T_b(k) for b in {B1, B2, B3}, with k sampled on a log-grid covering
     [1e-4, 1e0] h/Mpc (Euclid-Roman-LSST-DESI coverage).
   - Raw internal-to-external mode map tau -> a(tau) -> k(tau).

4. From s74_branch_nbar_dk.npz (W2-A output):
   - labels, idx_B1, idx_B2, idx_B3
   - r_k_bcs (per-mode hyperbolic squeezing, from S73A)
   - omega_k_entry (per-mode frequencies at entry horizon)
   - v_g at entry (per-mode group velocities)
   - n_bar_baseline, n_bar_corrected (per-mode Parker occupation numbers)

5. From s73a_exit_horizon_bog.npz (S73A W1-A):
   - The 8-mode Bogoliubov table (r_k, n_k, omega_k per mode).

6. From s72_kappa_delta.npz:
   - Delta(tau) quartic fit through the fold.

## Computation Steps

1. LOAD all .npz files above. Assert that all three branches have data
   available (|idx_B1|=1, |idx_B2|=4, |idx_B3|=3, total N_modes=8).
   Fail fast if any file is missing (the agent prints the missing file
   and exits with status FAIL).

2. For each branch b in {B1, B2, B3}, compute the branch-aggregated
   squeezed-vacuum signature:

   (a) Branch occupation number:
       n_bar_b = sum_{i in b} n_bar_i
       (NOT mean -- total photon/phonon number in the branch)

   (b) Branch squeezing phase:
       phi_b = arg[ sum_{i in b} (1 + 2 n_bar_i) * exp(i * 2 r_i) ]
       (coherent sum -- this is the vector phase of the branch relative
       to the total squeezed vacuum; use circular mean, NOT linear
       averaging -- phase near +-pi is the S64 PHASE-BOGOLIUBOV lesson.)

   (c) Branch characteristic frequency:
       omega_b = mean_{i in b} omega_i_entry   (M_KK units)

   (d) Branch characteristic wavenumber in internal (PW) units:
       k_b_internal = omega_b / v_g_b  (M_KK units, v_g_b branch-mean
       regularized at c_L_group = 0.025 M_KK for flat B2).

3. Convert k_b_internal to 4D h/Mpc via the s75 transfer function:
   k_b_obs = T_b^{-1}(k_b_internal).
   (i.e., the S75 transfer function defines the internal-to-external
   wavenumber map; invert it on the branch-characteristic k_b.)
   The 3 values k_b_obs for b in {B1, B2, B3} are the 3 comb centres.

4. For each branch, compute the comb amplitude on the 4D power spectrum.
   The branch-comb on the matter power spectrum is

       Delta P_b(k) / P(k) = W_b * cos(k / k_b_obs * 2 pi + phi_b)

   where the weight W_b is fixed by the branch energy content in the
   squeezed vacuum,

       W_b = (2 n_bar_b + 1) / sum_{b'} (2 n_bar_{b'} + 1)   [normalized]

   and the phase phi_b comes from step 2(b). This encodes the framework
   claim "amplitude set by n_k per mode and phase set by r_k per mode".

5. Sum the three branch contributions to produce the TOTAL branch-comb
   modulation on P(k):

       [Delta P(k) / P(k)]_comb = sum_{b in {B1,B2,B3}}
           W_b * A_envelope(k) * cos(k / k_b_obs * 2 pi + phi_b)

   where A_envelope(k) is the Euclid/DESI-relevant envelope (fold
   Gaussian tapered by k_eq -- use the W1-E H(z_eq) output to fix k_eq,
   then multiply by a Gaussian in log(k) with width = 0.5 dec).

6. Extract the 3 key numbers for the gate:
   (a) k_b_obs (3 values, h/Mpc): the comb centres.
   (b) A_b = W_b * max_k |cos(k / k_b_obs * 2 pi + phi_b)| = W_b
       (peak amplitude of the branch-resolved comb).
   (c) A_total = max_k |[Delta P(k) / P(k)]_comb| (peak total comb
       amplitude at the scale where the 3 combs constructively
       interfere, typically the k_B3 centre because of B3 dominance).

7. Cross-check:
   (a) B3 dominance: confirm n_bar_B3 / n_bar_total >= 0.5 (framework
       claim is ~0.73; W2-A baseline gives a specific number).
   (b) Weighted mean k_comb_mean = sum_b W_b * k_b_obs should lie
       inside [0.01, 0.3] h/Mpc (Euclid window).
   (c) A_total in [0.01, 0.05] (1-5% comb amplitude expected from the
       framework).

8. PLOT:
   (a) Panel 1: log-log P(k) smooth + comb overlay, k in [1e-4, 1] h/Mpc
       with the three branch-comb centres marked as vertical lines
       coloured by branch (B1 blue, B2 red, B3 green).
   (b) Panel 2: the per-branch amplitude bar chart W_b vs branch label.
   (c) Panel 3: phase diagram of (phi_B1, phi_B2, phi_B3) on the unit
       circle (polar scatter), with annotation of the inter-branch
       angular spacing.
   (d) Panel 4: the envelope A_envelope(k) times the comb modulation,
       showing constructive and destructive interference regions.

## Outputs

Script: computations/session-75/s75_branch_comb_amplitude.py
Data:   computations/session-75/s75_branch_comb_amplitude.npz
Plot:   computations/session-75/s75_branch_comb_amplitude.png

.npz contents (minimum):
    k_obs_h_per_Mpc : shape (3,)   -- [k_B1_obs, k_B2_obs, k_B3_obs]
    W_branch        : shape (3,)   -- [W_B1, W_B2, W_B3]
    phi_branch      : shape (3,)   -- [phi_B1, phi_B2, phi_B3]
    n_bar_branch    : shape (3,)   -- [n_bar_B1, n_bar_B2, n_bar_B3]
    A_branch        : shape (3,)   -- peak per-branch comb amplitude
    A_total         : scalar       -- peak total comb amplitude
    k_comb_mean     : scalar       -- weighted-mean comb centre (h/Mpc)
    k_grid          : shape (N_k,) -- log-grid k sampling
    DeltaPoverP_comb: shape (N_k,) -- the total comb modulation curve
    gate_verdict    : str          -- PASS / INFO / FAIL
    metadata        : dict of canonical inputs used

Working paper section: W4-DD of sessions/archive/session-75/...  (new section
in S75+ working paper, numbered per that session's plan)

## Pre-Registered Gate (for the S75+ execution)

BRANCH-COMB-AMPLITUDE-74:

    PASS if
        (i) all three k_b_obs are finite and inside [1e-4, 1] h/Mpc,
        (ii) W_B3 / (W_B1 + W_B2 + W_B3) >= 0.40  [framework claim: 0.73],
        (iii) A_total in [0.01, 0.05]  [framework claim: 2-3 percent],
        (iv) at least one k_b_obs lies inside the Euclid window
             [0.01, 0.3] h/Mpc.

    INFO if
        (i-ii) hold but A_total lies in [0.005, 0.01] or [0.05, 0.10],
        OR W_B3 fraction is in [0.30, 0.40] (softer B3 dominance), OR
        all three k_b_obs are finite but none lies inside the Euclid
        window (signature exists but is unobservable at current
        precision).

    FAIL if any k_b_obs is infinite or NaN, OR A_total < 1e-3 (below
        Euclid detection threshold at k in [0.01, 0.3] h/Mpc), OR A_total
        > 0.10 (exceeds the structural smoothness bound on the LCDM
        envelope -- would be visible already in Planck).

## Substrate-framing correction (from project rules)

When you find yourself writing "density perturbations in space" or
"expansion produces the comb", STOP and rewrite. The mechanism is: the
8-mode BCS sector has three inequivalent dispersion branches, each with
its own (omega_b, r_b, n_bar_b, v_g_b) triple. The s75 transfer function
is the pullback from internal tau-modulus to emergent 4D scale factor
a(tau); the comb is a direct image of the branch structure under that
pullback. It is not oscillations IN the expanding space -- it is the
pullback of the branch spectrum ONTO the emergent k-axis. The expanding
universe is emergent from the tau -> a map, not a container.

## Dependencies (fail-fast order)

(1) W1-E: s74_friedmann_from_a2.npz  (for H(z) and the tau -> a map)
(2) W4-CC: s75_transfer_function.py + s75_transfer_function.npz
(3) W2-A: s74_branch_nbar_dk.npz
(4) S73A: s73a_exit_horizon_bog.npz
(5) S56: s56_gge_fabric.npz
(6) S72: s72_kappa_delta.npz

If any of (1)-(6) is missing, print MISSING: <filename> and exit FAIL.
Do not stub, do not mock, do not re-derive.

## Cross-checks against existing framework results

- S66 Leggett-only Omega_DM h^2 = 0.120: the branch comb should NOT
  shift the integrated DM density (it is a modulation on the envelope,
  not the envelope itself). After computing A_total, verify that
  integral [Delta P_comb / P] d ln k over the Euclid window is zero
  (the comb is oscillatory, not additive).
- S73A W1-A r_k_bcs values: B2[0..3] = 1.78566, B1 = 3.57132,
  B3[0..2] = 1.96347. These drive the branch squeezing phases.
- S64 PHASE-BOGOLIUBOV-64: phi_Bog = pi exact for sudden quench. Use
  circular mean for inter-branch phase averaging (linear averaging
  near +-pi gives the WRONG answer).
- S65 BISPECTRUM-65: the Bogoliubov transformation is Gaussian, so the
  comb amplitude is set by the squeezing parameters r_b alone (no
  non-Gaussian contribution to the amplitude).

## Rules

- NUMBERS first. Gate second. Interpretation third.
- Dimensional consistency every step (M_KK to GeV to h/Mpc).
- No hardcoded framework constants -- import from canonical_constants.
- Tag intermediate computed variables with # (local).
- If the result is outside the gate bands, report the numbers and
  classify INFO or FAIL honestly. Do not retune to hit PASS.
- Save the .npz with all branch-resolved quantities so downstream
  sessions can re-use them.
- STOP after writing the W4-DD results section for S75+.
"""

# ==============================================================================
# SECTION 4: Gate verdict for THIS W4-DD spec-writing task
# ==============================================================================

checklist = {
    "objective":          "Compute Delta P / P branch-comb modulation for Gate 5",
    "substrate_framing":  "Included (container-thinking correction + direction)",
    "inputs_enumerated":  len(DEPENDENCIES) >= 3,
    "canonical_constants": len(CANONICAL_INPUTS) >= 10,
    "steps_numbered":     8,
    "outputs_specified":  ("s75_branch_comb_amplitude.py",
                           "s75_branch_comb_amplitude.npz",
                           "s75_branch_comb_amplitude.png"),
    "gate_quantitative":  "PASS/INFO/FAIL with k-range, W_B3 fraction, A_total bands",
    "cross_checks":       ["Omega_DM invariance", "S73A r_k values",
                           "S64 pi-phase circular averaging", "S65 Gaussianity"],
    "fail_fast_on_deps":  True,
}

spec_complete = all([
    checklist["inputs_enumerated"],
    checklist["canonical_constants"],
    checklist["steps_numbered"] >= 6,
    len(checklist["outputs_specified"]) == 3,
    checklist["fail_fast_on_deps"],
    PROMPT_TEXT.strip().startswith("You are the quantum-acoustics-theorist"),
    "PRE-REGISTERED" in PROMPT_TEXT.upper() or "Pre-Registered Gate" in PROMPT_TEXT,
    "substrate framing" in PROMPT_TEXT.lower(),
])

gate_verdict = "PASS" if spec_complete else "INFO"

# ==============================================================================
# SECTION 5: Save artefacts
# ==============================================================================

out_dir = os.path.dirname(os.path.abspath(__file__))
npz_path = os.path.join(out_dir, "s74_branch_comb_amplitude_spec.npz")

np.savez(
    npz_path,
    prompt_text=PROMPT_TEXT,
    dependencies=np.array(list(DEPENDENCIES.items()), dtype=object),
    canonical_inputs=np.array(list(CANONICAL_INPUTS.items()), dtype=object),
    checklist=np.array(list(checklist.items()), dtype=object),
    gate_verdict=gate_verdict,
    gate_id="BRANCH-COMB-AMPLITUDE-SPEC-74",
    session="S74",
    wave="W4-DD",
    agent="quantum-acoustics-theorist",
    classification="PHONONIC",
    framework_section="10 (deferred carry-forward)",
    feeds_gate="Gate 5 PHASE-COHERENT-PRIMORDIAL-SIGNATURE",
    execution_session="S75+",
    runtime_s=float(time.time() - t_start),
)

# ==============================================================================
# SECTION 6: Console report (no plot -- spec-only)
# ==============================================================================

print("=" * 72)
print("S74 W4-DD: BRANCH-COMB-AMPLITUDE-SPEC-74")
print("=" * 72)
print(f"Gate:        BRANCH-COMB-AMPLITUDE-SPEC-74")
print(f"Verdict:     {gate_verdict}")
print(f"Session:     S74 Wave 4 (spec-only)")
print(f"Executes in: S75+ (after W1-E + W4-CC complete)")
print(f"Feeds:       Gate 5 PHASE-COHERENT-PRIMORDIAL-SIGNATURE")
print(f"Output npz:  {os.path.basename(npz_path)}")
print()
print("Spec checklist:")
for k, v in checklist.items():
    print(f"  {k:24s} : {v}")
print()
print(f"Prompt length: {len(PROMPT_TEXT)} chars, {PROMPT_TEXT.count(chr(10))} newlines")
print(f"Dependencies : {len(DEPENDENCIES)} upstream artefacts")
print(f"Canonical in : {len(CANONICAL_INPUTS)} framework constants")
print()
print(f"Runtime: {time.time() - t_start:.3f} s")
