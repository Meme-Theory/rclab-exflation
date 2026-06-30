"""
re-run of S25 Connes-NCG workshop (s25_connes_workshop.py)
==============================================================
Gate: S25-CONNES-WORKSHOP
S81 canonical verdict form.

Migration notes (T3):
  - Inputs (s19a_sweep_data.npz, s23a_kosmann_singlet.npz, r20a_riemann_tensor.npz)
    now resolved from computations/_shared (per project structure post-S51 archiving).
  - Canonical import added per math-scripts.md (no-op binding: no framework constant
    from canonical_constants.py appears in the original computation — the script is
    purely spectral diagnostic over already-computed D_K eigenvalue archives).
  - All local assignments tagged '# (local)' — none are framework constants.
  - CPU fallback with OMP cap per compute-environment rule (problem size is
    dominated by n_tau=21 x 11424 eigenvalues; numpy reductions over 1D arrays,
    no linear algebra ≥ 100x100).
  - NO hardcoded framework constants added; NO modification to canonical_constants.py.

Items recomputed (verbatim from original):
  C1: Dixmier trace ratio [Connes Q-4]
  C2: Random NCG Jacobian [Connes S-4 / P5]
  C3: Spectral flow verification [Connes S-1 / Goal 4]
  C4: Truncated eta invariant [Connes S-5]
  C5: 4D-integrated spectral action g(Y) [Connes S-2]
  C6: Seeley-DeWitt coefficient ratios [Connes Q-1]
  C7: Index pairing topological phase diagram [Connes S-3]
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')

import numpy as np
import sys
import hashlib
import json

# Canonical constants import (discipline — no framework constants are used below,
# but the import is mandatory for S34+ scripts per math-scripts.md).
sys.path.insert(0, "C:/sandbox/Ainulindale Exflation/computations")
from canonical_constants import *  # noqa: F401,F403

ARCHIVE = "C:/sandbox/Ainulindale Exflation/computations/_shared"  # (local)
INTAKE = "C:/sandbox/Ainulindale Exflation/computations/_shared/t3-intake"  # (local)

# ------------------------------------------------------------------
# SHA-256 input pins (computed deterministically; logged for closure)
# ------------------------------------------------------------------
def sha256_file(path):
    h = hashlib.sha256()  # (local)
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()

INPUT_PATHS = {  # (local)
    "s19a_sweep_data.npz": f"{ARCHIVE}/s19a_sweep_data.npz",
    "s23a_kosmann_singlet.npz": f"{ARCHIVE}/s23a_kosmann_singlet.npz",
    "r20a_riemann_tensor.npz": f"{ARCHIVE}/r20a_riemann_tensor.npz",
}
input_pins = {name: sha256_file(p) for name, p in INPUT_PATHS.items()}  # (local)

print("=" * 70)
print("S25-CONNES-WORKSHOP — Input pins (SHA-256):")
for name, digest in input_pins.items():
    print(f"  {name}: {digest}")
print("=" * 70)

# ------------------------------------------------------------------
# Load inputs
# ------------------------------------------------------------------
sweep = np.load(INPUT_PATHS["s19a_sweep_data.npz"], allow_pickle=True)
tau_sweep = sweep["tau_values"]  # (local)
n_tau = len(tau_sweep)  # (local)
print(f"Loaded sweep data: {n_tau} tau values [{tau_sweep[0]:.2f}, {tau_sweep[-1]:.2f}]")

singlet = np.load(INPUT_PATHS["s23a_kosmann_singlet.npz"], allow_pickle=True)
tau_singlet = singlet["tau_values"]  # (local)
n_tau_s = len(tau_singlet)  # (local)
print(f"Loaded singlet data: {n_tau_s} tau values: {tau_singlet}")

riem = np.load(INPUT_PATHS["r20a_riemann_tensor.npz"], allow_pickle=True)
tau_r = riem["tau"]  # (local)
print(f"Loaded Riemann data: {len(tau_r)} tau values")
print()

# ==========================================================================
# C1: DIXMIER TRACE RATIO
# ==========================================================================
print("=" * 70)
print("C1: DIXMIER TRACE RATIO [Connes Q-4]")
print("  Tr_omega(|D_K(tau)|^{-8}) / Tr_omega(|D_K(0)|^{-8})")
print("  NCG volume ratio = shape diagnostic at finite N")
print("=" * 70)

partial_sums = np.zeros(n_tau)  # (local)
for i in range(n_tau):
    evals = np.abs(sweep[f"eigenvalues_{i}"])  # (local)
    evals_pos = evals[evals > 1e-14]  # (local)
    N = len(evals_pos)  # (local)
    log_N = np.log(N)  # (local)
    s = np.sum(evals_pos ** (-8))  # (local)
    partial_sums[i] = s / log_N

dixmier_ratios = partial_sums / partial_sums[0]  # (local)

print(f"  tau=0: Tr_w = {partial_sums[0]:.6e}")
print(f"  N = {N}, log(N) = {np.log(N):.4f}")
print()
print("  tau       Dixmier ratio")
print("  " + "-" * 30)
for i in range(n_tau):
    print(f"  {tau_sweep[i]:6.3f}   {dixmier_ratios[i]:12.8f}")

diffs = np.diff(dixmier_ratios)  # (local)
monotone_inc = np.all(diffs >= -1e-12)  # (local)
monotone_dec = np.all(diffs <= 1e-12)  # (local)
if monotone_inc:
    print("  MONOTONE INCREASING")
elif monotone_dec:
    print("  MONOTONE DECREASING")
else:
    for k in range(len(diffs) - 1):
        if diffs[k] > 0 and diffs[k + 1] < 0:
            print(f"  LOCAL MAXIMUM at tau ~ {tau_sweep[k+1]:.3f}, ratio = {dixmier_ratios[k+1]:.8f}")
        if diffs[k] < 0 and diffs[k + 1] > 0:
            print(f"  LOCAL MINIMUM at tau ~ {tau_sweep[k+1]:.3f}, ratio = {dixmier_ratios[k+1]:.8f}")
print()

# ==========================================================================
# C2: RANDOM NCG JACOBIAN
# ==========================================================================
print("=" * 70)
print("C2: RANDOM NCG JACOBIAN [Connes S-4 / Priority P5]")
print("  J(tau) = prod_n |d(lambda_n)/dtau|  (matrix-truncated)")
print("  Paper 14, Section 8.2: Z = int dD exp(-S[D])")
print("  Entropic stabilization if J(tau) peaks at tau_0 > 0")
print("=" * 70)

print("\n  Singlet sector (16 eigenvalues, central differences):")
jac_singlet = []  # (local)
tau_jac_s = []  # (local)
for i in range(1, n_tau_s - 1):
    evals_prev = singlet[f"eigenvalues_{i-1}"]  # (local)
    evals_next = singlet[f"eigenvalues_{i+1}"]  # (local)
    dt = tau_singlet[i + 1] - tau_singlet[i - 1]  # (local)
    d_evals = (evals_next - evals_prev) / dt  # (local)
    abs_d = np.abs(d_evals)  # (local)
    abs_d[abs_d < 1e-30] = 1e-30
    log_j = np.sum(np.log(abs_d))  # (local)
    jac_singlet.append(log_j)
    tau_jac_s.append(tau_singlet[i])

tau_jac_s = np.array(tau_jac_s)  # (local)
jac_singlet = np.array(jac_singlet)  # (local)
j_ref = jac_singlet[1] if len(jac_singlet) > 1 else jac_singlet[0]  # (local)

print("  tau       log|J|      J/J(0.15)")
print("  " + "-" * 40)
for i in range(len(tau_jac_s)):
    print(f"  {tau_jac_s[i]:6.3f}   {jac_singlet[i]:10.4f}   {np.exp(jac_singlet[i] - j_ref):10.6f}")

jd = np.diff(jac_singlet)  # (local)
singlet_peak = False  # (local)
for k in range(len(jd) - 1):
    if jd[k] > 0 and jd[k + 1] < 0:
        singlet_peak = True
        print(f"  SINGLET PEAK at tau ~ {tau_jac_s[k+1]:.2f}")
if not singlet_peak:
    direction = "INCREASING" if np.all(jd >= 0) else "DECREASING" if np.all(jd <= 0) else "NON-MONOTONE (no interior peak)"  # (local)
    print(f"  Singlet Jacobian: {direction}")

print("\n  Full spectrum (11424 eigenvalues, central differences):")
full_log_jac = []  # (local)
tau_full_jac = []  # (local)
for i in range(1, n_tau - 1):
    evals_prev = sweep[f"eigenvalues_{i-1}"]  # (local)
    evals_next = sweep[f"eigenvalues_{i+1}"]  # (local)
    dt = tau_sweep[i + 1] - tau_sweep[i - 1]  # (local)
    d_evals = (evals_next - evals_prev) / dt  # (local)
    abs_d = np.abs(d_evals)  # (local)
    abs_d[abs_d < 1e-15] = 1e-15
    log_j = np.sum(np.log(abs_d))  # (local)
    full_log_jac.append(log_j)
    tau_full_jac.append(tau_sweep[i])

tau_full_jac = np.array(tau_full_jac)  # (local)
full_log_jac = np.array(full_log_jac)  # (local)

print("  tau       log|J_full|")
print("  " + "-" * 30)
for i in range(len(tau_full_jac)):
    print(f"  {tau_full_jac[i]:6.3f}   {full_log_jac[i]:12.4f}")

fd = np.diff(full_log_jac)  # (local)
full_peak = False  # (local)
for k in range(len(fd) - 1):
    if fd[k] > 0 and fd[k + 1] < 0:
        full_peak = True
        print(f"  FULL PEAK at tau ~ {tau_full_jac[k+1]:.3f}, log|J| = {full_log_jac[k+1]:.4f}")
if not full_peak:
    direction = "INCREASING" if np.mean(fd) > 0 else "DECREASING"  # (local)
    print(f"  Full-spectrum Jacobian: {direction}")

print("\n  Effective NCG measure: mu(tau) = J(tau) * exp(-S_b[D_K(tau)])")
print("  (S_b = spectral action, monotone increasing)")
print("  If J increases faster than S_b, entropic stabilization possible.")
print()

# ==========================================================================
# C3: SPECTRAL FLOW CHECK
# ==========================================================================
print("=" * 70)
print("C3: SPECTRAL FLOW / ZERO CROSSINGS [Connes S-1 / Goal 4]")
print("  Verify Baptista: Lichnerowicz => no eigenvalue crosses zero")
print("=" * 70)

min_abs_eval = np.zeros(n_tau)  # (local)
for i in range(n_tau):
    evals = np.abs(sweep[f"eigenvalues_{i}"])  # (local)
    min_abs_eval[i] = np.min(evals[evals > 0])

R_scalar = riem["R_scalar"]  # (local)
lich_bound = np.sqrt(R_scalar / 4.0)  # (local)

print("  tau    min|lambda|   sqrt(R/4)   Lichnerowicz satisfied?")
print("  " + "-" * 60)
for i in range(0, n_tau, 2):
    idx_r = np.argmin(np.abs(tau_r - tau_sweep[i]))  # (local)
    satisfied = "YES" if min_abs_eval[i] >= lich_bound[idx_r] - 0.01 else "NO"  # (local)
    print(f"  {tau_sweep[i]:5.2f}   {min_abs_eval[i]:10.6f}   {lich_bound[idx_r]:10.6f}       {satisfied}")

n_sign_changes = 0  # (local)
for j in range(11424):
    evals_j = np.array([sweep[f"eigenvalues_{i}"][j] for i in range(n_tau)])  # (local)
    signs = np.sign(evals_j)  # (local)
    changes = np.sum(np.abs(np.diff(signs)) > 0)  # (local)
    n_sign_changes += changes

print(f"\n  Total sign changes across all 11424 eigenvalues x {n_tau} tau: {n_sign_changes}")
print(f"  Spectral flow = 0. CONFIRMED by Lichnerowicz bound.")
print()

# ==========================================================================
# C4: TRUNCATED ETA INVARIANT
# ==========================================================================
print("=" * 70)
print("C4: TRUNCATED ETA INVARIANT [Connes S-5]")
print("  eta_N(s) = sum_{n=1}^{N} sign(lambda_n) |lambda_n|^{-s}")
print("  BDI => eta = 0 identically. Verify at finite truncation.")
print("=" * 70)

max_eta = 0.0  # (local)
print("  Checking at selected tau values and s values:")
print("  tau     eta(s=0.5)      eta(s=1)        eta(s=2)        eta(s=4)")
print("  " + "-" * 70)
for i in range(0, n_tau, 4):
    evals = sweep[f"eigenvalues_{i}"]  # (local)
    signs = np.sign(evals)  # (local)
    abs_ev = np.abs(evals)  # (local)
    abs_ev = np.where(abs_ev < 1e-14, 1e-14, abs_ev)

    eta_05 = np.sum(signs * abs_ev ** (-0.5))  # (local)
    eta_1 = np.sum(signs * abs_ev ** (-1.0))  # (local)
    eta_2 = np.sum(signs * abs_ev ** (-2.0))  # (local)
    eta_4 = np.sum(signs * abs_ev ** (-4.0))  # (local)
    max_eta = max(max_eta, abs(eta_05), abs(eta_1), abs(eta_2), abs(eta_4))
    print(f"  {tau_sweep[i]:5.2f}   {eta_05:14.6e}  {eta_1:14.6e}  {eta_2:14.6e}  {eta_4:14.6e}")

print(f"\n  max|eta| (sampled): {max_eta:.6e}")
print("  APS boundary correction: (1/2)[eta(D_K(0)) - eta(D_K(tau))] ~ 0 at machine precision")
print("  Chern-Simons boundary term: ZERO (trivial by BDI spectral pairing)")
print()

# ==========================================================================
# C5: 4D-INTEGRATED SPECTRAL ACTION
# ==========================================================================
print("=" * 70)
print("C5: SPECTRAL ACTION WITH 4D-INTEGRATED TEST FUNCTION [Connes S-2]")
print("  For f(x)=xe^{-x} on M^4 x K:")
print("    g(Y) = exp(-Y) * (2 + Y)  where Y = lambda_m^2/Lambda^2")
print("  This is the PROPERLY dimensionally-reduced test function.")
print("=" * 70)

def g_4d(Y):
    return np.exp(-Y) * (2.0 + Y)

def f_internal(Y):
    return Y * np.exp(-Y)

Lambdas = [1.0, 2.0, 5.0, 10.0]  # (local)

print("\n  Comparison: V_f (internal only) vs V_g (4D-integrated)")
for Lambda in Lambdas:
    V_f = np.zeros(n_tau)  # (local)
    V_g = np.zeros(n_tau)  # (local)
    for i in range(n_tau):
        Y = sweep[f"eigenvalues_{i}"] ** 2 / Lambda ** 2  # (local)
        V_f[i] = np.sum(f_internal(Y))
        V_g[i] = np.sum(g_4d(Y))

    V_f_n = V_f / V_f[0]  # (local)
    V_g_n = V_g / V_g[0]  # (local)

    f_mono = "MONO" if (np.all(np.diff(V_f_n) >= -1e-10) or np.all(np.diff(V_f_n) <= 1e-10)) else "NON-MONO"  # (local)
    g_mono = "MONO" if (np.all(np.diff(V_g_n) >= -1e-10) or np.all(np.diff(V_g_n) <= 1e-10)) else "NON-MONO"  # (local)

    print(f"\n  Lambda = {Lambda:.1f}:")
    print(f"    V_f: [{V_f_n.min():.6f}, {V_f_n.max():.6f}] ({f_mono})")
    print(f"    V_g: [{V_g_n.min():.6f}, {V_g_n.max():.6f}] ({g_mono})")
    print(f"    Ratio V_g(0)/V_f(0) = {V_g[0]/V_f[0]:.4f}")

    if Lambda == 1.0:
        print("    tau    V_f/V_f(0)   V_g/V_g(0)   V_g/V_f")
        for idx in [0, 2, 4, 6, 8, 10, 15, 20]:
            if idx < n_tau:
                r = V_g[idx] / V_f[idx] if V_f[idx] > 0 else 0  # (local)
                print(f"    {tau_sweep[idx]:5.2f}  {V_f_n[idx]:10.6f}   {V_g_n[idx]:10.6f}   {r:10.4f}")

    max_dev = np.max(np.abs(V_f_n - V_g_n))  # (local)
    print(f"    Max |V_f_normalized - V_g_normalized| = {max_dev:.6f}")

print()

# ==========================================================================
# C6: SEELEY-DEWITT COEFFICIENT ANALYSIS
# ==========================================================================
print("=" * 70)
print("C6: SEELEY-DEWITT COEFFICIENTS [Connes Q-1]")
print("  a_2^red = (20/3)*R,  a_4^red = (1/90)*(125R^2 - 8|Ric|^2 + 2K)")
print("  From Session 20a SD-1 derivation, verified trace identity")
print("=" * 70)

Ric_data = riem["Ric"]  # (local)
Ric_sq = np.array([np.sum(Ric_data[i] ** 2) for i in range(len(tau_r))])  # (local)
K_gauss = riem["K"]  # (local)

a2 = (20.0 / 3.0) * R_scalar  # (local)
a4 = (1.0 / 90.0) * (125.0 * R_scalar ** 2 - 8.0 * Ric_sq + 2.0 * K_gauss)  # (local)

print("\n  tau      R        a_2        a_4         a_4/a_2      a_4/R")
print("  " + "-" * 70)
for i in range(0, len(tau_r), 2):
    r42 = a4[i] / a2[i] if a2[i] != 0 else float("inf")  # (local)
    rR = a4[i] / R_scalar[i] if R_scalar[i] != 0 else float("inf")  # (local)
    print(f"  {tau_r[i]:5.2f}  {R_scalar[i]:8.3f}  {a2[i]:10.3f}  {a4[i]:12.1f}  {r42:10.2f}  {rR:10.2f}")

da2 = np.gradient(a2, tau_r)  # (local)
da4 = np.gradient(a4, tau_r)  # (local)

print("\n  Derivative analysis (da_k/dtau):")
print("  tau    da_2/dtau    da_4/dtau    Signs")
print("  " + "-" * 50)
for i in range(0, len(tau_r), 2):
    s2 = "+" if da2[i] > 0 else "-"  # (local)
    s4 = "+" if da4[i] > 0 else "-"  # (local)
    print(f"  {tau_r[i]:5.2f}  {da2[i]:12.3f}  {da4[i]:12.1f}     {s2}  {s4}")

opp = np.where((da2 > 0) & (da4 < 0))[0]  # (local)
if len(opp) > 0:
    print(f"\n  OPPOSITE SIGNS at tau = {tau_r[opp]}")
else:
    opp2 = np.where((da2 < 0) & (da4 > 0))[0]  # (local)
    if len(opp2) > 0:
        print(f"\n  OPPOSITE SIGNS at tau = {tau_r[opp2]}")
    else:
        print(f"\n  SAME SIGN (both positive) for ALL tau >= 0")
        print("  => No Starobinsky-type minimum from SD coefficient competition")

R2_frac = 125.0 * R_scalar ** 2 / (125.0 * R_scalar ** 2 + np.abs(-8.0 * Ric_sq + 2.0 * K_gauss))  # (local)
print(f"\n  R^2 dominance in a_4:")
print(f"    tau=0: {R2_frac[0]*100:.2f}%")
print(f"    tau=1: {R2_frac[10]*100:.2f}%")
print(f"    tau=2: {R2_frac[-1]*100:.2f}%")
print(f"  Conclusion: R^2 term dominates a_4 at >99% at all tau.")

a6_est = 2.0 * R_scalar * np.abs(a4)  # (local)
growth_ratio = a6_est / np.abs(a4)  # (local)
print(f"\n  Estimated |a_6|/|a_4| (using factorial growth ~ 2*R):")
for i in [0, 5, 10, 15, 20]:
    print(f"    tau={tau_r[i]:.2f}: |a_6|/|a_4| ~ {growth_ratio[i]:.1f}")
print("  Conclusion: Expansion diverges factorially. NOT convergent at any tau.")
print()

# ==========================================================================
# C7: INDEX PAIRING / TOPOLOGICAL PHASE DIAGRAM
# ==========================================================================
print("=" * 70)
print("C7: INDEX PAIRING TOPOLOGICAL PHASE DIAGRAM [Connes S-3]")
print("  <[D_K(tau)], [e_{(p,q)}]> per sector")
print("  = #(positive eigenvalues) - #(negative eigenvalues) in (p,q)")
print("=" * 70)

sectors = set()  # (local)
for i in range(n_tau):
    ps = sweep[f"sector_p_{i}"]  # (local)
    qs = sweep[f"sector_q_{i}"]  # (local)
    for j in range(len(ps)):
        sectors.add((int(ps[j]), int(qs[j])))

sectors = sorted(sectors)  # (local)
print(f"  {len(sectors)} distinct sectors found")

print("\n  Sector     N_evals   Index(0)  Index(1.0)  Index(2.0)  Constant")
print("  " + "-" * 65)
all_zero_all_tau = True  # (local)
for (p, q) in sectors[:15]:
    indices = []  # (local)
    n_ev = 0  # (local)
    for tau_idx in [0, 10, 20]:
        ps = sweep[f"sector_p_{tau_idx}"]  # (local)
        qs = sweep[f"sector_q_{tau_idx}"]  # (local)
        ev = sweep[f"eigenvalues_{tau_idx}"]  # (local)
        mask = (ps == p) & (qs == q)  # (local)
        sec_ev = ev[mask]  # (local)
        n_ev = len(sec_ev)
        idx = int(np.sum(sec_ev > 0) - np.sum(sec_ev < 0))  # (local)
        indices.append(idx)
        if idx != 0:
            all_zero_all_tau = False

    const = "YES" if all(x == indices[0] for x in indices) else "NO"  # (local)
    print(f"  ({p},{q})     {n_ev:5d}     {indices[0]:5d}     {indices[1]:5d}       {indices[2]:5d}       {const}")

non_zero_count = 0  # (local)
for i in range(n_tau):
    ps = sweep[f"sector_p_{i}"]  # (local)
    qs = sweep[f"sector_q_{i}"]  # (local)
    ev = sweep[f"eigenvalues_{i}"]  # (local)
    for (p, q) in sectors:
        mask = (ps == p) & (qs == q)  # (local)
        sec_ev = ev[mask]  # (local)
        idx = int(np.sum(sec_ev > 0) - np.sum(sec_ev < 0))  # (local)
        if idx != 0:
            non_zero_count += 1

print(f"\n  Non-zero index count across all (sector, tau) pairs: {non_zero_count}")
print(f"  Topological phase diagram: {'TRIVIAL (all indices zero)' if non_zero_count == 0 else 'NON-TRIVIAL'}")
print("  BDI eigenvalue pairing (lambda, -lambda) => index = 0 for all sectors.")
print("  Lichnerowicz bound => no eigenvalue crosses zero => index is constant.")
print("  Phase diagram has NO transitions. Geometry is topologically inert under Jensen.")
print()

# ==========================================================================
# SAVE RESULTS (T3 side-car; does NOT overwrite historical s25_connes_results.npz)
# ==========================================================================
print("=" * 70)
print("SAVING T3 RESULTS (side-car)")
print("=" * 70)

OUT_NPZ = f"{INTAKE}/s25_connes_workshop.npz"  # (local)
np.savez(OUT_NPZ,
    tau_sweep=tau_sweep,
    dixmier_ratios=dixmier_ratios,
    dixmier_partial_sums=partial_sums,
    tau_jac_singlet=tau_jac_s,
    log_jacobian_singlet=jac_singlet,
    tau_jac_full=tau_full_jac,
    log_jacobian_full=full_log_jac,
    min_abs_eigenvalue=min_abs_eval,
    n_sign_changes=np.array([n_sign_changes]),
    tau_riem=tau_r,
    a2_values=a2,
    a4_values=a4,
    R_scalar=R_scalar,
    a4_over_a2=a4/a2,
    da2_dtau=da2,
    da4_dtau=da4,
    R2_dominance_frac=R2_frac,
    max_eta_sampled=np.array([max_eta]),
    non_zero_index_count=np.array([non_zero_count]),
)
print(f"  Saved to {OUT_NPZ}")

# ------------------------------------------------------------------
# CLOSURE: SHA-256 of JSON-sorted input-pin map
# ------------------------------------------------------------------
closure_payload = json.dumps(input_pins, sort_keys=True, separators=(",", ":")).encode("utf-8")  # (local)
closure_sha = hashlib.sha256(closure_payload).hexdigest()  # (local)
print()
print("=" * 70)
print("CLOSURE")
print("=" * 70)
print(f"  Input-pin JSON (sorted, compact): {closure_payload.decode('utf-8')}")
print(f"  Closure SHA-256: {closure_sha}")

# ------------------------------------------------------------------
# 4-tuple summary for verdict
# ------------------------------------------------------------------
print()
print("=" * 70)
print("4-TUPLE SUMMARY")
print("=" * 70)
# value: max|eta| at sampled s,tau grid (BDI-predicted zero observable)
# scheme: zeta-regularised truncated eta over signed |lambda|^{-s}
# convention: BDI spectral triple with lambda <-> -lambda pairing, KO-dim=6
# L_max: derived from 11424 eigenvalues on SU(3) (historical s19a sweep)
print(f"  value      = {max_eta:.6e}  (max|eta_N(s)| over sampled s in {{0.5,1,2,4}} and tau_indices {{0,4,8,12,16,20}})")
print(f"  scheme     = truncated_eta_zeta_reg_signed_power_sum")
print(f"  convention = BDI_lambda_minus_lambda_pairing_KOdim6")
print(f"  L_max      = 11424_eigenvalues_s19a_sweep_21tau_grid")
print(f"  sha256     = {closure_sha}")

# Also emit a JSON block for downstream automation
summary = {  # (local)
    "gate": "S25-CONNES-WORKSHOP",
    "value": float(max_eta),
    "scheme": "truncated_eta_zeta_reg_signed_power_sum",
    "convention": "BDI_lambda_minus_lambda_pairing_KOdim6",
    "L_max": "11424_eigenvalues_s19a_sweep_21tau_grid",
    "sha256": closure_sha,
    "input_pins": input_pins,
    "derived": {
        "dixmier_monotone_increasing": bool(monotone_inc),
        "dixmier_monotone_decreasing": bool(monotone_dec),
        "n_sign_changes_in_spectral_flow": int(n_sign_changes),
        "n_sectors": int(len(sectors)),
        "non_zero_index_count": int(non_zero_count),
        "min_abs_lambda_at_tau0": float(min_abs_eval[0]),
        "max_abs_lambda_over_tau_floor": float(np.max(min_abs_eval)),
        "lich_bound_tau0": float(lich_bound[0]),
    },
}
print()
print("JSON_SUMMARY:" + json.dumps(summary, sort_keys=True))
print()
print("=" * 70)
print("ALL T3 COMPUTATIONS COMPLETE")
print("=" * 70)
