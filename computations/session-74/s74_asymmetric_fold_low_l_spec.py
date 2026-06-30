"""
S74 W4-EE: ASYMMETRIC-FOLD-LOW-L-SPEC-74 — Spec-Only for S75+

Task: Draft the full-fidelity prompt specification for
ASYMMETRIC-FOLD-LOW-L-74 (framework §10 deferred, Gate 4 sharpening).

Framework context:
------------------
The asymmetric fold is a Jensen-SU(3) deformation that breaks C^2-parity
between sectors of the internal fiber. The internal geometry at the fold
has the u(2) Killing block plus the 4 non-Killing C^2 coset directions
(e_3, e_4, e_5, e_6), which on the Jensen line form a 4-fold degenerate
orbit of U(2). Breaking this U(2)-degeneracy at the fold via
tau -> tau + delta_tau * chi(C^2-parity) produces a sector-asymmetric
Bogoliubov amplification which imprints on the low-l CMB TT spectrum
through the three-branch (B1/B2/B3) block-decoherence channel.

This script writes a full-fidelity S75+ prompt for executing the
asymmetric-fold low-l TT computation. It is SPEC-ONLY (no physics
computation is performed here).

Pre-registered gate:
    ASYMMETRIC-FOLD-LOW-L-SPEC-74: PASS if spec is complete. FAIL if missing.

Output:
    s74_asymmetric_fold_low_l_spec.npz  — spec payload (string + metadata)

Framework dependencies upstream:
    §3a (asymmetric fold geometry: Mach 20.7, entry horizon n_bar=85.2, open exit)
    §7c / §9 Gate 4 (BOUNCE-SYMMETRY-DISTINGUISH pre-registration)
    §10 carry-forward (deferred two sessions out, depends on s75_transfer_function.py)

Framework dependencies downstream:
    s75_transfer_function.py (W4-CC spec) must be in place to map fiber
    P(k) to CMB C_l; this ASYMMETRIC-FOLD-LOW-L-74 computation inherits
    that transfer function and perturbs its asymmetric channel.
"""

import sys
from pathlib import Path
import numpy as np

# Local guard: computations on sys.path so canonical_constants imports
THIS = Path(__file__).resolve()  # (local)
SCRIPT_DIR = THIS.parent  # (local)
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    tau_fold,
    M_KK,
    Vol_SU3_Haar,
    S_fold,
    dS_fold,
    d2S_fold,
    dt_transit,
    J_C2,
    omega_L1,
    Delta_BCS,
)

# ----------------------------------------------------------------------
# FULL-FIDELITY S75+ PROMPT: ASYMMETRIC-FOLD-LOW-L-74
# ----------------------------------------------------------------------

PROMPT = r"""
You are computing the low-l CMB TT signature from the asymmetric fold
(ASYMMETRIC-FOLD-LOW-L-74). This is the Gate 4 (BOUNCE-SYMMETRY-DISTINGUISH)
sharpening of framework-parametric-amplification.md §9, the framework §10
deferred item queued "two sessions out" after s75_transfer_function.py.

The computation takes the asymmetric Jensen deformation — tau differs
slightly between C^2-parity sectors of the internal fiber — and propagates
the resulting sector-asymmetric Bogoliubov amplification through the
transfer function to the CMB TT angular power spectrum at low multipoles
(l in [2, 30]). The output is a quantitative C_l^TT,substrate / C_l^TT,LCDM
ratio at l ~ 10 with an error budget, pre-registered against the Planck
low-l power deficit.

Substrate framing: The fabric is not IN space. Space is an emergent
description of how spectral weight distributes through the Dirac operator
D_K on Jensen-deformed SU(3). An asymmetric fold is a small sector-
dependent shift delta_tau_s in the Jensen parameter between C^2-parity
sectors s in {+, -} of the internal fiber; it does not modify a
pre-existing 4D background but deforms D_K(tau), whose eigenvalue
reorganization at the fold produces a sector-asymmetric Bogoliubov
spectrum. The imprint on the CMB TT at low l is downstream of the same
spectral action moments that generate the Einstein-Hilbert and Yang-Mills
actions — the asymmetry lives at the level of the fabric, and the C_l
signature is the observational shadow of the fabric's sector-asymmetric
spectral amplification.

REGIME OF VALIDITY

This computation lives in the perturbative asymmetric regime:
  |delta_tau| / tau_fold <= 0.10
where tau_fold = 0.19 (canonical S42). Beyond |delta_tau|/tau_fold = 0.10
the fold structure itself changes nontrivially (the van Hove profile
separates into two distinct fold surfaces per sector), and the single-
pulse description in framework §4 fails. Report explicitly if the inferred
delta_tau ever exceeds this bound; if it does, flag NONPERTURBATIVE and
do not extrapolate.

GEOMETRIC DESCRIPTION OF THE ASYMMETRIC FOLD

The internal fiber is SU(3) with a left-invariant Jensen-family metric.
The Jensen line parametrizes U(2)-invariant deformations. At the fold
tau = tau_fold = 0.19 the u(2) block (4 Killing directions) is
undeformed; the 4 non-Killing C^2 coset directions (e_3, e_4, e_5, e_6)
carry the deformation and are 4-fold degenerate on the Jensen line
(S65 YUKAWA-TEXTURE: Y = 345.2 * I_4, U(2) orbit on C^2 acts
transitively).

C^2-parity is the Z_2 subgroup of U(2) that exchanges the two complex
coordinates of C^2 — equivalently, the diagonal Weyl reflection in
the SU(3) root system that flips the two simple roots other than the
U(2) highest root. A C^2-parity breaking deformation is the minimal
symmetry breaking that splits the 4-fold C^2 orbit into two 2-fold
sub-orbits labelled by parity eigenvalue s in {+, -}.

The asymmetric Jensen deformation is:
    tau_s = tau_fold + delta_tau_s,     s in {+, -}
with the constraint delta_tau_+ + delta_tau_- = 0 (no net shift of
the fold position along the Jensen line), and the amplitude controlled
by one scalar parameter:
    delta_tau_+ = + delta_tau_asym / 2
    delta_tau_- = - delta_tau_asym / 2.

Under this deformation the Dirac operator splits:
    D_K^s(tau) = D_K(tau_s),     s in {+, -}
and the fold surface becomes two sheets separated by delta_tau_asym in
the tau direction.

SECTOR-ASYMMETRIC BOGOLIUBOV AMPLIFICATION

Each sector s has its own transit velocity v_tau^s(tau), its own BCS
gap profile Delta_BCS^s(tau), and its own Mach number Ma_BA^s. The
asymmetric Bogoliubov coefficient for mode k in sector s is:
    beta_k^s = < out_{tau=tau_s+}, k | in_{tau=tau_s-}, k >
computed from the time-dependent quench across the sector-specific
fold.

The three-branch decomposition (B1, B2, B3 from framework §7 and
OVERLAP-MATRIX-74, 8 BCS modes splitting as 1+4+3) inherits the
asymmetry through the overlap coefficients M_ib^s = < B_i | branch_b >_s.
The key quantities are:
    n_k^s = |beta_k^s|^2        — sector-s pair occupation per mode
    r_k^s = arctanh(|beta_k^s / alpha_k^s|)  — sector-s squeezing
    phi_k^s                     — sector-s Bogoliubov phase
    <n_k>_{B_i}^s = sum_k M_ib^s n_k^s   — branch-projected per sector

The sector-asymmetric inter-branch covariance is:
    C(B_i, B_j; s) = <n_{B_i} n_{B_j}>_s - <n_{B_i}>_s <n_{B_j}>_s
The sum over sectors produces the composite branch covariance
    C_total(B_i, B_j) = (1/2) sum_s C(B_i, B_j; s)
and the block-decoherence contrast is:
    Delta C_sym(B_i, B_j) = C(B_i, B_j; +) - C(B_i, B_j; -)

At the symmetric fold (delta_tau_asym = 0) this Delta C is identically
zero and the framework §9 Gate 4 prediction reduces to the three-branch
block-decoherence signature C(B2, B3) = 2.3e-6 and the intra-branch
variance (3.6e-8, 8.5e-8) as reported for the symmetric fold. The
asymmetric correction is FIRST-ORDER in delta_tau_asym and enters
through:
    Delta C_sym = 2 * (dC/d(tau)) * (delta_tau_asym / 2) + O(delta_tau^2)
                = (dC/d tau) * delta_tau_asym.

The derivative dC/dtau is computed by taking W2-A (compound_ns) and/or
W1-A (transfer function) outputs as a function of tau and finite-
differencing near tau = tau_fold.

LOW-L CMB TT SIGNATURE

The transfer function T(k -> l) from s75_transfer_function.py (W4-CC
spec) maps fiber P(k) onto the CMB C_l^TT. Under the asymmetric fold,
the fiber P^s(k) acquires a sector-asymmetric correction, and the
composite C_l is:
    C_l^TT = (1/2) * sum_s integral dk / k * T^2(k, l) * P^s(k)
Write Delta P(k) = P^+(k) - P^-(k). The leading-order correction to
C_l is:
    C_l^TT,substrate / C_l^TT,sym = 1 + (1/2) * R_l(delta_tau_asym)
where R_l captures the l-dependent weight:
    R_l = integral dk / k * T^2(k, l) * (Delta P / P_sym) /
          integral dk / k * T^2(k, l).

Because B3 dominates the inter-branch compound phase split (n_k^B3 /
n_k^total ~ 0.73, framework §9 Gate 5), the asymmetric correction is
MOST visible at low l where T(k, l) projects onto modes that left the
fiber just after the fold with the largest r_k. Concretely:
    l < 30: R_l linear in delta_tau_asym, amplitude ~ few percent
    l ~ 10: the peak of the low-l projection, cosmic variance limited

COMPARISON TO PLANCK LOW-L DATA

The observed Planck low-l TT deficit relative to the best-fit LCDM is:
    C_l^TT,Planck / C_l^TT,LCDM ~ 0.85 at l = 10 (Planck 2018 A1)
with the l = 2 quadrupole suppressed at ~ 0.7 of LCDM at ~ 1-2 sigma
(cosmic-variance-limited). Gate 4 PASS requires:
    - substrate C_l^TT,substrate / C_l^TT,LCDM at l ~ 10 differs from
      LCDM by > 2-sigma (cosmic variance) AND
    - the sign and magnitude of the deviation match the measured anomaly.

COMPUTATION STEPS

1. Import all constants from canonical_constants.py:
     tau_fold, M_KK, Vol_SU3_Haar, S_fold, dS_fold, d2S_fold,
     dt_transit, J_C2, omega_L1, Delta_BCS.

2. Load upstream inputs:
     - computations/session-75/s75_transfer_function.npz (W4-CC S75 spec output)
       -> T(k, l) transfer function on grid (k, l).
     - computations/session-56/s56_gge_fabric.npz
       -> 8 BCS mode frequencies omega_k(tau) and their 3-branch
          decomposition B1(1) + B2(4) + B3(3).
     - computations/session-74/s74_transit_ps.npz (if present) OR
       computations/session-73/s73b_transit_ps.npz
       -> r_k, n_k, phi_k at the symmetric fold.
     - computations/session-74/s74_overlap_matrix.npz (W1-K output)
       -> 3x3 overlap M_ib = < B_i | branch_b >.
     - computations/session-74/s74_compound_ns.npz (W2-A) or the S73A variant
       -> alpha_k, beta_k and their tau-derivatives.
     - computations/session-65/s65_yukawa_texture.npz
       -> confirmation of 4-fold C^2 degeneracy on the Jensen line
          (needed to define the C^2-parity sector projection).

3. Construct the C^2-parity projection operators:
     P_+ = projector onto {e_3 + e_5, e_4 + e_6}   (parity-even)
     P_- = projector onto {e_3 - e_5, e_4 - e_6}   (parity-odd)
   verify Tr(P_+) = Tr(P_-) = 2 and P_+ + P_- = I_{C^2}.

4. Sector-asymmetric Jensen deformation:
     tau_s = tau_fold + s * delta_tau_asym / 2    for s in {+1, -1}
   Scan delta_tau_asym over {0, 0.005, 0.010, 0.019} where 0.019
   corresponds to a 10% asymmetry (|delta_tau|/tau_fold = 0.10 — the
   upper bound of the perturbative regime).

5. For each sector s and each delta_tau_asym value, compute the
   sector-s Bogoliubov coefficients:
     beta_k^s(delta_tau_asym) = beta_k(tau_fold) +
         (d beta_k / d tau) * (s * delta_tau_asym / 2)
     alpha_k^s(delta_tau_asym) = alpha_k(tau_fold) +
         (d alpha_k / d tau) * (s * delta_tau_asym / 2)
   The derivatives (d beta_k / d tau) and (d alpha_k / d tau) at tau_fold
   are available from W2-A compound_ns (finite-difference its alpha/beta
   tables across the fold neighborhood).

6. Project onto branches using M_ib^s (from S65 YUKAWA-TEXTURE the
   overlap matrix is diagonal on the Jensen line, so M_ib^s = M_ib to
   leading order; the C^2-parity breaking enters the next order via the
   branch eigenvalue shifts):
     n_{B_i}^s = sum_k M_ib * n_k^s

7. Compute the sector-s fiber power spectrum:
     P^s(k) = sum_i (H(tau_cross^i)/(2 pi))^2 * (1 + 2 n_{B_i}^s) *
              |cosh(r_{B_i}^s(k)) + sinh(r_{B_i}^s(k)) * exp(i phi_{B_i}^s)|^2
   where r_{B_i}^s, phi_{B_i}^s are the branch-averaged squeezing and
   phase in sector s, inherited from the W1-A transfer function.

8. Compose the composite fiber power spectrum:
     P_composite(k) = (1/2) * (P^+(k) + P^-(k))
     Delta P(k) = P^+(k) - P^-(k)

9. Apply the transfer function T(k, l) from s75_transfer_function.npz:
     C_l^TT,substrate = integral dk/k * T^2(k, l) * P_composite(k)
     Delta C_l^TT = (1/2) * integral dk/k * T^2(k, l) * Delta P(k)
   on a logarithmic k-grid covering at least [1e-5, 1e-1] h/Mpc, at
   least 200 points per decade.

10. Compute the LCDM reference C_l^TT,LCDM at the same multipoles
    (l in [2, 30]) using the Planck 2018 best-fit parameters. The LCDM
    reference is produced via the standard recipe:
    C_l^TT,LCDM from Planck 2018 TT, TE, EE + lowE + lensing best-fit
    parameters at l in [2, 30]; either use camb/class (if present in the
    venv) or interpolate the tabulated Planck 2018 A1 low-l C_l from
    sessions/data/planck_2018_low_l.dat. Record the source explicitly.

11. Compute the ratio:
     R(l) = C_l^TT,substrate(delta_tau_asym) / C_l^TT,LCDM
    for each delta_tau_asym and each l in [2, 30].

12. Invert for the best-fit delta_tau_asym: the value of
    delta_tau_asym that minimizes the chi^2 between R(l) and the
    Planck-observed low-l deficit, using the Planck low-l TT covariance
    matrix (cosmic-variance-limited diagonal for l < 30).

13. Compute the pre-registered gate quantities:
     R(l = 10) at best-fit delta_tau_asym
     chi^2 of the substrate fit
     delta sigma = (R_substrate - R_LCDM) / sigma_Planck,cosmic-var at l = 10

14. Cross-checks:
     (a) At delta_tau_asym = 0, verify R(l) = 1 for all l (reduces to
         symmetric fold).
     (b) C^2-parity charge conservation: sum_s delta_tau_s = 0 enforced
         throughout (no net Jensen drift).
     (c) |delta_tau_asym| / tau_fold < 0.10: stay in perturbative regime.
     (d) |Delta C_sym(B2, B3) / C(B2, B3)| < 1: asymmetric correction
         remains a perturbation on top of the symmetric inter-branch
         covariance C(B2, B3) = 2.3e-6 reported in framework §9 Gate 4.
     (e) At delta_tau_asym = 0.019 (10% asymmetry upper bound), verify
         Delta P / P at the fiber peak scale is monotonic in |delta_tau_asym|
         (linearity check; first-order theory valid).

OUTPUT FILES

Script: computations/session-75/s75_asymmetric_fold_low_l.py
Data: computations/session-75/s75_asymmetric_fold_low_l.npz containing:
    - delta_tau_asym_grid: scanned values
    - C_l_TT_substrate: array (n_delta, n_l)
    - C_l_TT_LCDM: array (n_l,)
    - R_l: ratio array (n_delta, n_l)
    - best_fit_delta_tau: scalar
    - chi2_best_fit: scalar
    - delta_sigma_l10: scalar (signal-to-cosmic-variance at l=10)
    - gate_verdict: string PASS/INFO/FAIL
Plot: computations/session-75/s75_asymmetric_fold_low_l.png with panels:
    Panel A: R(l) vs l for 4 values of delta_tau_asym
    Panel B: chi^2 vs delta_tau_asym
    Panel C: best-fit R(l) overlaid on Planck low-l data with 2-sigma band
    Panel D: Delta P(k) / P_sym(k) fiber spectrum at best-fit

Working paper section: W5-? (assigned by S75+ planner)

PRE-REGISTERED GATE

ASYMMETRIC-FOLD-LOW-L-74:
    PASS  if delta_sigma(l=10) > 2.0 AND sign(R - 1) matches Planck
          (i.e., R < 1 and the substrate explains the low-l deficit)
          AND delta_tau_asym is within the perturbative regime
          (|delta_tau|/tau_fold < 0.10) AND chi^2/dof < 2.
    INFO  if delta_sigma(l=10) in [1, 2] OR sign matches but delta_tau_asym
          saturates 10% (points toward nonperturbative regime, needs
          retry with exact sector D_K^s recomputation).
    FAIL  if delta_sigma(l=10) < 1 (substrate asymmetric fold does not
          produce detectable low-l anomaly at the Planck precision) OR
          sign(R - 1) is wrong (substrate predicts excess, observed is
          deficit) OR the inverted delta_tau_asym lies outside the
          perturbative regime with no physical justification.

DEPENDENCIES

UPSTREAM (must be complete before this computation runs):
  - s75_transfer_function.py (W4-CC spec) — provides T(k, l)
  - s74_overlap_matrix.npz (S74 W1-K) — provides M_ib
  - s74_compound_ns.npz OR s73a_compound_ns.npz (S74 W2-A) — provides
    alpha_k, beta_k and their tau derivatives
  - s56_gge_fabric.npz — provides BCS mode frequencies
  - Planck 2018 low-l TT data (either from camb/class or tabulated)

If s75_transfer_function.py is unavailable when this computation runs,
FALL BACK to a heuristic transfer function T(k, l) = delta(l - l(k))
with l(k) from the standard flat-sky projection l = k * D_A(z_lss)
using Planck 2018 D_A(z_lss) = 13870 Mpc. The fallback gives an
order-of-magnitude R(l) but not a gate-decisive number; tag the run as
FALLBACK and redispatch once the full transfer function is available.

SIZE & RUNTIME

- k-grid: 200 points per decade on [1e-5, 1e-1] h/Mpc -> ~800 points
- l-grid: 29 points (l in [2, 30])
- delta_tau_asym-grid: 4 values
- sector-s loop: 2 values
- branch loop: 3 values (B1, B2, B3)
- total inner work: ~60,000 evaluations, each O(1 ms)
- expected runtime: 30 - 120 seconds on the venv312 CPU

Use numpy vectorized arithmetic; no need for GPU.

CANONICAL CONSTANTS REFERENCE

This computation uses the following canonical constants (all imported
from computations/_shared/canonical_constants.py; no hardcodes):
    tau_fold       = 0.19              — Jensen fold position
    M_KK           = M_KK_gravity      — 7.4287e16 GeV (gravity route)
    Vol_SU3_Haar   = 1349.74           — S44 corrected SU(3) Haar volume
    S_fold         = 250360.68         — spectral action at fold
    dS_fold        = 58672.80          — dS/dtau at fold
    d2S_fold       = 317862.85         — d^2 S/dtau^2 at fold
    dt_transit     = 0.00113016        — transit duration (1/M_KK)
    J_C2           = 0.933             — C^2 coset bond strength
    omega_L1       = 0.138              — Leggett-1 frequency (M_KK)
    Delta_BCS      = Delta_0_OES       — canonical BCS gap

Any intermediate value (k-grid points, l-grid points, sector projector
matrix elements, finite-difference spacings, best-fit residuals) must
be tagged # (local) per the math-scripts rule.

END OF FULL-FIDELITY S75+ PROMPT.
"""

# ----------------------------------------------------------------------
# Metadata for the spec payload
# ----------------------------------------------------------------------

gate_name = "ASYMMETRIC-FOLD-LOW-L-SPEC-74"  # (local)
gate_pass_criterion = "Spec is complete and full-fidelity."  # (local)
gate_verdict = "PASS"  # (local)

upstream_deps = [  # (local)
    "s75_transfer_function.py (W4-CC S75 spec)",
    "s74_overlap_matrix.npz (S74 W1-K)",
    "s74_compound_ns.npz or s73a_compound_ns.npz (S74 W2-A)",
    "s56_gge_fabric.npz",
    "Planck 2018 low-l TT data (camb/class or tabulated)",
]

downstream_uses = [  # (local)
    "framework §9 Gate 4 (BOUNCE-SYMMETRY-DISTINGUISH) quantitative threshold",
    "framework §10 carry-forward closure (two sessions out from §10.1)",
    "Planck low-l TT anomaly resolution (falsification gate)",
]

target_script = "computations/session-75/s75_asymmetric_fold_low_l.py"  # (local)
target_data = "computations/session-75/s75_asymmetric_fold_low_l.npz"  # (local)
target_plot = "computations/session-75/s75_asymmetric_fold_low_l.png"  # (local)

regime_of_validity = "|delta_tau_asym| / tau_fold <= 0.10"  # (local)

canonical_constants_used = [  # (local)
    f"tau_fold = {tau_fold}",
    f"M_KK = {M_KK}",
    f"Vol_SU3_Haar = {Vol_SU3_Haar:.4f}",
    f"S_fold = {S_fold}",
    f"dS_fold = {dS_fold}",
    f"d2S_fold = {d2S_fold}",
    f"dt_transit = {dt_transit}",
    f"J_C2 = {J_C2}",
    f"omega_L1 = {omega_L1}",
    f"Delta_BCS = {Delta_BCS}",
]

prompt_n_chars = len(PROMPT)  # (local)
prompt_n_lines = PROMPT.count("\n")  # (local)

# ----------------------------------------------------------------------
# Spec completeness check
# ----------------------------------------------------------------------

required_sections = [  # (local)
    "REGIME OF VALIDITY",
    "GEOMETRIC DESCRIPTION",
    "SECTOR-ASYMMETRIC BOGOLIUBOV AMPLIFICATION",
    "LOW-L CMB TT SIGNATURE",
    "COMPARISON TO PLANCK LOW-L DATA",
    "COMPUTATION STEPS",
    "OUTPUT FILES",
    "PRE-REGISTERED GATE",
    "DEPENDENCIES",
    "CANONICAL CONSTANTS REFERENCE",
]

missing_sections = [s for s in required_sections if s not in PROMPT]  # (local)
spec_complete = (len(missing_sections) == 0)  # (local)

if not spec_complete:
    gate_verdict = "FAIL"
    print(f"[S74 W4-EE] SPEC INCOMPLETE: missing sections {missing_sections}")
else:
    print(f"[S74 W4-EE] Spec complete: all {len(required_sections)} required sections present.")
    print(f"[S74 W4-EE] Prompt size: {prompt_n_chars} chars, {prompt_n_lines} lines.")
    print(f"[S74 W4-EE] Gate {gate_name}: {gate_verdict}")

# ----------------------------------------------------------------------
# Save spec payload to NPZ
# ----------------------------------------------------------------------

out_npz = SCRIPT_DIR / "s74_asymmetric_fold_low_l_spec.npz"  # (local)

np.savez(
    out_npz,
    prompt=np.array([PROMPT], dtype=object),
    gate_name=np.array([gate_name], dtype=object),
    gate_pass_criterion=np.array([gate_pass_criterion], dtype=object),
    gate_verdict=np.array([gate_verdict], dtype=object),
    upstream_deps=np.array(upstream_deps, dtype=object),
    downstream_uses=np.array(downstream_uses, dtype=object),
    target_script=np.array([target_script], dtype=object),
    target_data=np.array([target_data], dtype=object),
    target_plot=np.array([target_plot], dtype=object),
    regime_of_validity=np.array([regime_of_validity], dtype=object),
    canonical_constants_used=np.array(canonical_constants_used, dtype=object),
    prompt_n_chars=prompt_n_chars,
    prompt_n_lines=prompt_n_lines,
    spec_complete=spec_complete,
    required_sections=np.array(required_sections, dtype=object),
    missing_sections=np.array(missing_sections, dtype=object),
)

print(f"[S74 W4-EE] Wrote spec to {out_npz}")
print(f"[S74 W4-EE] Upstream deps: {len(upstream_deps)}")
print(f"[S74 W4-EE] Downstream uses: {len(downstream_uses)}")
