"""
Session 29Ba — re-run: PMNS Mixing Angle Extraction from Tridiagonal Kosmann
===============================================================================

T3 canonical re-run of s29b_pmns_extraction.py under S81 standards:
  - `from canonical_constants import *` (no framework constants hardcoded)
  - All intermediates tagged `# (local)`
  - PDG reference values remain local with citation
  - SHA-256 pin of all inputs (FULL 64-char hex) logged before compute
  - Closure SHA-256 of JSON-sorted pin map emitted at the end
  - 3x3 PMNS angle extraction (CPU, OMP capped to 8)

Classification: PARTICLE — mixing-angle extraction from singlet sector of D_K.

Gate: S29B-PMNS-EXTRACTION
  Pre-registered pass/fail: the gate reports the value of sin^2(theta_13)
  obtained from Method B (degenerate PT -> 3x3 tridiagonal) at the tau
  closest to the fold (tau_fold). Because the S29b source gate was a
  computation gate (report value, not PASS/FAIL against an observational
  window), the re-run faithfully reproduces that verdict: INFO with
  the numerical value logged in canonical form.

Input:  s23a_kosmann_singlet.npz (SHA-256 pinned below, FULL 64-char hex)
Output: s29b_pmns_extraction.npz + s29b_pmns_extraction_verdict.txt
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import numpy as np

# Canonical constants (mandatory, S34+). Nothing here is hardcoded from the
# framework — PDG PMNS reference values remain local (citation-only).
sys.path.insert(0, "C:/sandbox/Ainulindale Exflation/computations")
from canonical_constants import *  # noqa: F401,F403

# =====================================================================
# FILE PATHS + SHA-256 PIN MAP (FULL 64-char hex)
# =====================================================================
base_archive = "C:/sandbox/Ainulindale Exflation/computations/_shared"          # (local)
base_compute = "C:/sandbox/Ainulindale Exflation/computations"      # (local)
base_intake  = f"{base_compute}/t3-intake"                               # (local)
input_path   = f"{base_archive}/s23a_kosmann_singlet.npz"                # (local)
output_npz   = f"{base_intake}/s29b_pmns_extraction.npz"              # (local)
verdict_path = f"{base_intake}/s29b_pmns_extraction_verdict.txt"      # (local)

def sha256_file(path):
    """Return the FULL 64-char SHA-256 hex digest of a file."""
    h = hashlib.sha256()                          # (local)
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()

pin_map = {                                                              # (local)
    "s23a_kosmann_singlet.npz": sha256_file(input_path),
}

print("=" * 70)
print("S29B-PMNS-EXTRACTION  (re-run of s29b_pmns_extraction.py)")
print("=" * 70)
print("Input SHA-256 pins (FULL 64-char hex):")
for name, sha in pin_map.items():
    print(f"  {name}: {sha}")

# =====================================================================
# LOAD DATA
# =====================================================================
try:
    d = np.load(input_path, allow_pickle=True)
except FileNotFoundError:
    print(f"ERROR: {input_path} not found")
    sys.exit(1)

tau_values = d['tau_values']                                             # (local) tau grid from source npz
n_tau = len(tau_values)                                                  # (local)

# PDG reference values (PDG 2024). Local by instruction — not framework constants.
PDG = {                                                                  # (local)
    'sin2_theta13': 0.0220,         # PDG 2024
    'sin2_theta13_err': 0.0007,     # PDG 2024
    'theta12_deg': 33.44,           # PDG 2024
    'theta12_deg_err': 0.77,        # PDG 2024
    'theta23_deg': 49.1,            # PDG 2024
    'theta23_deg_err': 1.0,         # PDG 2024 approximate
    'sin2_2theta13': 0.0851,        # PDG 2024
    'R_target': 32.6,               # PDG 2024 Delta m^2_32 / Delta m^2_21
}

print(f"\ntau values: {tau_values}")
print(f"PDG reference (2024):")
print(f"  sin^2(theta_13) = {PDG['sin2_theta13']} +/- {PDG['sin2_theta13_err']}")
print(f"  theta_12 = {PDG['theta12_deg']} +/- {PDG['theta12_deg_err']} deg")
print(f"  theta_23 = {PDG['theta23_deg']} +/- {PDG['theta23_deg_err']} deg")
print(f"  R = Delta m^2_32/Delta m^2_21 = {PDG['R_target']}")

# =====================================================================
# HELPER: Extract PMNS angles from 3x3 unitary matrix
# =====================================================================
def extract_pmns(U):
    """Convention: U[alpha, i], alpha = flavor (e,mu,tau), i = mass (1,2,3).
    Eigenvalues sorted ascending -> column 0 = lightest mass state.
    """
    sin2_13 = abs(U[0, 2]) ** 2                                          # (local)
    theta_13 = np.degrees(np.arcsin(np.sqrt(sin2_13)))                   # (local)
    if abs(U[0, 0]) > 1e-15:
        tan2_12 = abs(U[0, 1]) ** 2 / abs(U[0, 0]) ** 2                  # (local)
        theta_12 = np.degrees(np.arctan(np.sqrt(tan2_12)))               # (local)
    else:
        theta_12 = 90.0                                                  # (local) degenerate fallback
    if abs(U[2, 2]) > 1e-15:
        tan2_23 = abs(U[1, 2]) ** 2 / abs(U[2, 2]) ** 2                  # (local)
        theta_23 = np.degrees(np.arctan(np.sqrt(tan2_23)))               # (local)
    else:
        theta_23 = 90.0                                                  # (local) degenerate fallback
    J = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])) # (local) Jarlskog (0 for real U)
    return {
        'sin2_13': sin2_13,
        'theta_13': theta_13,
        'theta_12': theta_12,
        'theta_23': theta_23,
        'J': J,
    }

# =====================================================================
# METHOD A: Full 16x16 H_eff diagonalization
# =====================================================================
print("\n" + "=" * 70)
print("METHOD A: Full 16x16 H_eff diagonalization")
print("=" * 70)

results_A = []                                                           # (local)
for t_idx in range(n_tau):
    tau = tau_values[t_idx]                                              # (local)
    evals = d[f'eigenvalues_{t_idx}']                                    # (local)
    V = d[f'V_pairing_{t_idx}']                                          # (local)
    H_eff = np.diag(evals) + V                                           # (local)
    H_evals, H_evecs = np.linalg.eigh(H_eff)                             # (local) 16x16 — numpy OK
    pos_mask = H_evals > 0                                               # (local)
    pos_evals = H_evals[pos_mask]                                        # (local)
    pos_evecs = H_evecs[:, pos_mask]                                     # (local)
    if len(pos_evals) < 3:
        print(f"  tau={tau:.2f}: < 3 positive eigenvalues, skip")
        results_A.append(None)
        continue
    sort_idx = np.argsort(pos_evals)                                     # (local)
    m = pos_evals[sort_idx[:3]]                                          # (local) 3 lightest positive
    U_3 = pos_evecs[:, sort_idx[:3]]                                     # (local) 16x3
    denom = m[1] ** 2 - m[0] ** 2                                        # (local)
    R = (m[2] ** 2 - m[1] ** 2) / denom if abs(denom) > 1e-30 else float('inf')  # (local)
    if tau > 0:
        overlap_L1 = np.abs(U_3[8, :]) ** 2                              # (local)
        overlap_L2 = np.sum(np.abs(U_3[9:13, :]) ** 2, axis=0)           # (local)
        overlap_L3 = np.sum(np.abs(U_3[13:16, :]) ** 2, axis=0)          # (local)
        overlap_neg = np.sum(np.abs(U_3[:8, :]) ** 2, axis=0)            # (local)
    else:
        overlap_L1 = np.zeros(3)                                         # (local)
        overlap_L2 = np.zeros(3)                                         # (local)
        overlap_L3 = np.zeros(3)                                         # (local)
        overlap_neg = np.zeros(3)                                        # (local)
    print(f"\n  tau={tau:.2f}:")
    print(f"    m1={m[0]:.8f}, m2={m[1]:.8f}, m3={m[2]:.8f}")
    print(f"    R = {R:.4f}  (target: {PDG['R_target']})")
    if tau > 0:
        print(f"    Overlap with L1: {overlap_L1}")
        print(f"    Overlap with L2: {overlap_L2}")
        print(f"    Overlap with L3: {overlap_L3}")
        print(f"    Overlap with neg: {overlap_neg}")
        print(f"    Sum per state: {overlap_L1 + overlap_L2 + overlap_L3 + overlap_neg}")
    results_A.append({'tau': tau, 'm': m, 'R': R, 'H_evals': H_evals})

# =====================================================================
# METHOD B: Degenerate Perturbation Theory -> 3x3 (canonical scheme)
# =====================================================================
print("\n" + "=" * 70)
print("METHOD B: Degenerate Perturbation Theory (3x3) — canonical scheme")
print("=" * 70)

results_B = []                                                           # (local)
for t_idx in range(n_tau):
    tau = tau_values[t_idx]                                              # (local)
    if tau == 0:
        results_B.append(None)
        continue
    evals = d[f'eigenvalues_{t_idx}']                                    # (local)
    V = d[f'V_pairing_{t_idx}']                                          # (local)
    E1 = evals[8]                                                        # (local) L1 singlet
    E2 = evals[9]                                                        # (local) L2 quadruplet
    E3 = evals[13]                                                       # (local) L3 triplet
    v_L1_L2 = V[8, 9:13]                                                 # (local) 4-vector
    norm_12 = np.linalg.norm(v_L1_L2)                                    # (local)
    if norm_12 > 1e-15:
        L2_eff = v_L1_L2 / norm_12                                       # (local) dominant L2 linear combination
    else:
        L2_eff = np.array([0.5, 0.5, 0.5, 0.5])                          # (local) fallback
    V_L2_L3 = V[9:13, 13:16]                                             # (local) 4x3 block
    v_eff_L3 = L2_eff @ V_L2_L3                                          # (local) 3-vector
    norm_23 = np.linalg.norm(v_eff_L3)                                   # (local)
    H_3x3 = np.array([                                                   # (local)
        [E1,      norm_12, 0.0    ],
        [norm_12, E2,      norm_23],
        [0.0,     norm_23, E3     ],
    ])
    m_evals, U = np.linalg.eigh(H_3x3)                                   # (local) 3x3 — numpy
    pmns = extract_pmns(U)                                               # (local)
    denom = m_evals[1] ** 2 - m_evals[0] ** 2                            # (local)
    R = (m_evals[2] ** 2 - m_evals[1] ** 2) / denom if abs(denom) > 1e-30 else float('inf')  # (local)
    print(f"\n  tau={tau:.2f}:")
    print(f"    H_3x3 diagonal: [{E1:.6f}, {E2:.6f}, {E3:.6f}]")
    print(f"    V_12 = {norm_12:.6f}, V_23 = {norm_23:.6f}, V_13 = 0 (exact)")
    print(f"    Eigenvalues: [{m_evals[0]:.8f}, {m_evals[1]:.8f}, {m_evals[2]:.8f}]")
    print(f"    sin^2(theta_13) = {pmns['sin2_13']:.6f}  (PDG: {PDG['sin2_theta13']})")
    print(f"    theta_13 = {pmns['theta_13']:.2f} deg  (PDG: 8.54)")
    print(f"    theta_12 = {pmns['theta_12']:.2f} deg  (PDG: {PDG['theta12_deg']})")
    print(f"    theta_23 = {pmns['theta_23']:.2f} deg  (PDG: {PDG['theta23_deg']})")
    print(f"    R = {R:.4f}  (target: {PDG['R_target']})")
    results_B.append({
        'tau': tau,
        'E1': E1, 'E2': E2, 'E3': E3,
        'V_12': norm_12, 'V_23': norm_23,
        'H_3x3': H_3x3,
        'eigenvalues': m_evals,
        'U': U,
        'sin2_13': pmns['sin2_13'],
        'theta_13': pmns['theta_13'],
        'theta_12': pmns['theta_12'],
        'theta_23': pmns['theta_23'],
        'R': R,
    })

# =====================================================================
# METHOD C: Single-mode 3x3 (cross-check)
# =====================================================================
print("\n" + "=" * 70)
print("METHOD C: Single-mode 3x3 (V_12 individual, V_23 average)")
print("=" * 70)

results_C = []                                                           # (local)
for t_idx in range(n_tau):
    tau = tau_values[t_idx]                                              # (local)
    if tau == 0:
        results_C.append(None)
        continue
    evals = d[f'eigenvalues_{t_idx}']                                    # (local)
    V = d[f'V_pairing_{t_idx}']                                          # (local)
    E1 = evals[8]                                                        # (local)
    E2 = evals[9]                                                        # (local)
    E3 = evals[13]                                                       # (local)
    v12_individual = abs(V[8, 9])                                        # (local)
    V_L2_L3 = V[9:13, 13:16]                                             # (local)
    v23_avg = np.mean(np.abs(V_L2_L3))                                   # (local)
    H_3x3 = np.array([                                                   # (local)
        [E1,              v12_individual, 0.0    ],
        [v12_individual,  E2,             v23_avg],
        [0.0,             v23_avg,        E3     ],
    ])
    m_evals, U = np.linalg.eigh(H_3x3)                                   # (local)
    pmns = extract_pmns(U)                                               # (local)
    denom = m_evals[1] ** 2 - m_evals[0] ** 2                            # (local)
    R = (m_evals[2] ** 2 - m_evals[1] ** 2) / denom if abs(denom) > 1e-30 else float('inf')  # (local)
    print(f"\n  tau={tau:.2f}:")
    print(f"    V_12 = {v12_individual:.6f}, V_23 = {v23_avg:.6f}")
    print(f"    sin^2(theta_13) = {pmns['sin2_13']:.6f}")
    print(f"    theta_13 = {pmns['theta_13']:.2f} deg")
    print(f"    theta_12 = {pmns['theta_12']:.2f} deg")
    print(f"    theta_23 = {pmns['theta_23']:.2f} deg")
    print(f"    R = {R:.4f}")
    results_C.append({
        'tau': tau,
        'V_12': v12_individual, 'V_23': v23_avg,
        'sin2_13': pmns['sin2_13'],
        'theta_13': pmns['theta_13'],
        'theta_12': pmns['theta_12'],
        'theta_23': pmns['theta_23'],
        'R': R,
    })

# =====================================================================
# T3 VERDICT EXTRACTION (Method B at tau closest to tau_fold)
# =====================================================================
print("\n" + "=" * 70)
print("T3 VERDICT EXTRACTION (Method B @ tau closest to tau_fold)")
print("=" * 70)

# tau_fold comes from canonical_constants; pick closest tau on the grid.
tau_target = tau_fold                                                    # imported canonical
tau_dists = np.abs(np.asarray(tau_values) - tau_target)                  # (local)
t_idx_best = int(np.argmin(tau_dists))                                   # (local)
# Method B at tau=0 is None (no coupling), so fall back to next closest positive tau.
if results_B[t_idx_best] is None:
    # Move to the smallest non-zero tau that produced Method-B output
    for k in np.argsort(tau_dists):
        if results_B[int(k)] is not None:
            t_idx_best = int(k)                                          # (local)
            break

rb = results_B[t_idx_best]                                               # (local)
tau_used = rb['tau']                                                     # (local)
sin2_13_fit = float(rb['sin2_13'])                                       # (local) best-fit value (report)
theta_12_fit = float(rb['theta_12'])                                     # (local)
theta_23_fit = float(rb['theta_23'])                                     # (local)
R_fit = float(rb['R'])                                                   # (local)

# --- Substitution chain (best-fit vs PDG direction for sin^2(theta_13)) ---
# Step 1 (definition): sin^2(theta_13) = |U_e3|^2 (PMNS element, squared).
# Step 2 (reference):  PDG_sin2_theta13 = 0.0220 (PDG 2024).
# Step 3 (substitution): delta = sin2_13_fit - PDG_sin2_theta13
# Step 4 (canonical simplification):
#        sign(delta) > 0  <=>  sin2_13_fit > PDG   [best-fit ABOVE PDG]
#        sign(delta) < 0  <=>  sin2_13_fit < PDG   [best-fit BELOW PDG]
# Step 5 (direction): direction is taken directly from sign(delta), no
#        further algebra. The claim is purely quantitative: we record
#        sin2_13_fit and the signed difference, then verify via Python.
delta_sin2_13 = sin2_13_fit - PDG['sin2_theta13']                        # (local) signed residual
if delta_sin2_13 > 0:
    direction_label = "ABOVE_PDG"                                        # (local)
elif delta_sin2_13 < 0:
    direction_label = "BELOW_PDG"                                        # (local)
else:
    direction_label = "EQ_PDG"                                           # (local)

print(f"  tau_fold (canonical):    {tau_target}")
print(f"  tau used (grid-nearest): {tau_used}")
print(f"  sin^2(theta_13) fit:     {sin2_13_fit:.6f}")
print(f"  sin^2(theta_13) PDG:     {PDG['sin2_theta13']:.4f} +/- {PDG['sin2_theta13_err']:.4f}")
print(f"  delta = fit - PDG:       {delta_sin2_13:+.6f}  ({direction_label})")
print(f"  theta_12 fit:            {theta_12_fit:.3f} deg (PDG {PDG['theta12_deg']})")
print(f"  theta_23 fit:            {theta_23_fit:.3f} deg (PDG {PDG['theta23_deg']})")
print(f"  R fit:                   {R_fit:.4f}  (target {PDG['R_target']})")

# Verdict status policy: S29b is a *report-value* gate (measure sin^2_13 from
# tridiagonal structure), not an observational PASS/FAIL window, because the
# downstream observational gate (B-29b / P-29b) lived in the session-layer
# synthesis. For the T3 intake we record the numerical 4-tuple and emit INFO.
verdict_status = "INFO"                                                  # (local)

# =====================================================================
# CLOSURE HASH (SHA-256 of JSON-sorted pin map) — FULL 64 hex
# =====================================================================
pin_json = json.dumps(pin_map, sort_keys=True, separators=(',', ':'))    # (local)
closure_sha = hashlib.sha256(pin_json.encode('utf-8')).hexdigest()       # (local) FULL 64-char

print("\n" + "=" * 70)
print("CLOSURE")
print("=" * 70)
print(f"Pin JSON:      {pin_json}")
print(f"Closure SHA:   {closure_sha}")

# =====================================================================
# SAVE RESULTS NPZ
# =====================================================================
save_dict = {                                                            # (local)
    'tau_values': tau_values,
    'PDG_sin2_theta13': PDG['sin2_theta13'],
    'PDG_theta12_deg': PDG['theta12_deg'],
    'PDG_theta23_deg': PDG['theta23_deg'],
    'PDG_R': PDG['R_target'],
    'tau_used': tau_used,
    'sin2_13_fit': sin2_13_fit,
    'theta_12_fit': theta_12_fit,
    'theta_23_fit': theta_23_fit,
    'R_fit': R_fit,
    'delta_sin2_13': delta_sin2_13,
    'direction_label': direction_label,
    'closure_sha': closure_sha,
    'input_pin_s23a': pin_map["s23a_kosmann_singlet.npz"],
}

for t_idx in range(n_tau):
    rb = results_B[t_idx]
    if rb is None:
        continue
    prefix = f"B_t{t_idx}"                                               # (local)
    save_dict[f'{prefix}_tau'] = rb['tau']
    save_dict[f'{prefix}_E1'] = rb['E1']
    save_dict[f'{prefix}_E2'] = rb['E2']
    save_dict[f'{prefix}_E3'] = rb['E3']
    save_dict[f'{prefix}_V12'] = rb['V_12']
    save_dict[f'{prefix}_V23'] = rb['V_23']
    save_dict[f'{prefix}_eigenvalues'] = rb['eigenvalues']
    save_dict[f'{prefix}_U'] = rb['U']
    save_dict[f'{prefix}_sin2_13'] = rb['sin2_13']
    save_dict[f'{prefix}_theta13'] = rb['theta_13']
    save_dict[f'{prefix}_theta12'] = rb['theta_12']
    save_dict[f'{prefix}_theta23'] = rb['theta_23']
    save_dict[f'{prefix}_R'] = rb['R']

for t_idx in range(n_tau):
    rc = results_C[t_idx]
    if rc is None:
        continue
    prefix = f"C_t{t_idx}"                                               # (local)
    save_dict[f'{prefix}_sin2_13'] = rc['sin2_13']
    save_dict[f'{prefix}_theta12'] = rc['theta_12']
    save_dict[f'{prefix}_theta23'] = rc['theta_23']
    save_dict[f'{prefix}_R'] = rc['R']

np.savez(output_npz, **save_dict)
print(f"\nSaved: {output_npz}")

# =====================================================================
# S81 CANONICAL VERDICT LINE (FIRST LINE, NOT pipe-sep)
# =====================================================================
value_str = (                                                            # (local)
    f"sin2_13={sin2_13_fit:.6f},"
    f"theta12={theta_12_fit:.3f}deg,"
    f"theta23={theta_23_fit:.3f}deg,"
    f"R={R_fit:.4f},"
    f"delta_fit_vs_PDG={delta_sin2_13:+.6f}({direction_label})"
)
scheme_str = "MethodB_degenerate_PT_tridiagonal_3x3_eigh"                # (local)
convention_str = (                                                        # (local)
    "U[alpha,i]_ascending_mass_flavor_basis_"
    "sin2_13=|U_e3|^2_tan2_12=|U_e2|^2/|U_e1|^2_"
    "tan2_23=|U_mu3|^2/|U_tau3|^2"
)
L_max_str = f"singlet_L1L2L3_subspace_0..15_tau_grid_nearest_to_tau_fold={tau_target}_tau_used={tau_used}"  # (local)

canonical_line = (
    f"S29B-PMNS-EXTRACTION: {verdict_status} -- "
    f"value={value_str} "
    f"scheme={scheme_str} "
    f"convention={convention_str} "
    f"L_max={L_max_str} "
    f"sha256={closure_sha}"
)

prose_lines = [                                                          # (local)
    "",
    "# Prose / context (human scan; not parsed by consolidator)",
    "# Gate ID         : S29B-PMNS-EXTRACTION",
    "# Classification  : PARTICLE",
    "# Script          : computations/session-29/s29b_pmns_extraction.py",
    "# Source script   : computations/session-29/s29b_pmns_extraction.py",
    f"# Input SHA-256   : s23a_kosmann_singlet.npz = {pin_map['s23a_kosmann_singlet.npz']}",
    f"# Closure SHA-256 : {closure_sha}  (SHA-256 of JSON-sorted input pin map)",
    f"# tau_fold used   : {tau_target} (canonical_constants)",
    f"# tau_grid_used   : {tau_used} (nearest grid point with Method-B output)",
    f"# Method          : B (degenerate PT -> 3x3 tridiagonal; Frobenius-norm L1->L2 coupling)",
    f"# sin^2(theta_13) : {sin2_13_fit:.6f}   PDG 2024: 0.0220 +/- 0.0007",
    f"# theta_12        : {theta_12_fit:.3f} deg   PDG 2024: 33.44 +/- 0.77 deg",
    f"# theta_23        : {theta_23_fit:.3f} deg   PDG 2024: 49.1 +/- 1.0 deg",
    f"# R=Dm32^2/Dm21^2 : {R_fit:.4f}          PDG target: 32.6",
    f"# delta fit-PDG   : {delta_sin2_13:+.6f}  ({direction_label})",
    "# Substitution    : definition sin^2(theta_13) = |U_e3|^2; PDG = 0.0220;",
    "#                   delta = fit - PDG;  sign(delta) -> ABOVE_PDG / BELOW_PDG.",
    "# Verdict status  : INFO (report-value gate; observational PASS/FAIL was B-29b/P-29b",
    "#                   at the session-synthesis layer, not at the T3 script level).",
]

with open(verdict_path, 'w', encoding='utf-8') as f:
    f.write(canonical_line + "\n")
    for line in prose_lines:
        f.write(line + "\n")

print("\n" + "=" * 70)
print("VERDICT FILE")
print("=" * 70)
print(f"Path: {verdict_path}")
print(f"First line: {canonical_line}")
print("=" * 70)
print("COMPUTATION COMPLETE")
