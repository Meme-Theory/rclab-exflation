"""
FINAL CONVERGENCE ANALYSIS: What is actually real here?

The 0.2 ppm match was an artifact of using rounded phi_paasch = 1.531580.
The actual phi_paasch at tau=0.15 is 1.537088, giving 0.54% match.

But the STRUCTURAL finding remains: fermions dominate bosons at low mode
count, and the crossover point N_cross INCREASES with tau. Let's nail
down what is genuinely significant vs what is numerology.
"""
import numpy as np

ferm_data = np.load('s19a_sweep_data.npz', allow_pickle=True)
bos_data = np.load('kk1_bosonic_spectrum.npz', allow_pickle=True)
tau_ferm = ferm_data['tau_values']

print("="*70)
print("WHAT IS ACTUALLY REAL: CONVERGENCE ANALYSIS")
print("="*70)

# --- 1. The phi match is NOT sub-ppm ---
print("\n--- 1. PHI MATCH CORRECTION ---")
print("  Using stored phi_paasch = 1.531580 (Session 12 value): 0.2 ppm match")
print("  Using recomputed phi_paasch = 1.537088 at tau=0.15: 0.54% match")
print("  Using phi_paasch = 1.527525 at tau=0.00: 0.40% match")
print("  VERDICT: The match is at ~0.5%, not ppm. Interesting but NOT decisive.")
print("  (Session 12's 0.12 ppm phi came from a POOLED search across many ratios)")

# --- 2. What IS structurally real: gap-edge separation ---
print("\n--- 2. STRUCTURALLY REAL: FERMIONIC GAP > BOSONIC GAP ---")
print("  At ALL tau values, the fermionic gap edge is above the bosonic gap edge.")
print("  This is a topological fact: fermions on SU(3) have lambda_min = 5/6 (exact)")
print("  while bosonic (scalar) modes have lambda_min = 4/9 (exact) at tau=0.")
print(f"  Ratio at tau=0: (5/6)/(4/9) = 15/8 = {15/8} (EXACT, algebraic)")
print("  The Jensen deformation increases this ratio monotonically.")

# --- 3. What IS structurally real: F > B at low modes ---
print("\n--- 3. STRUCTURALLY REAL: FERMION ENERGY DOMINANCE AT LOW N ---")

bos_tau_keys = sorted([k for k in bos_data.keys()])
bos_taus = [float(k.split('_')[1]) for k in bos_tau_keys]

print(f"\n  {'tau':>5s} | {'N_cross':>8s} | {'F/B at N=50':>12s} | {'F/B at N=500':>12s} | {'F/B full':>8s}")
print(f"  {'-'*5}-+-{'-'*8}-+-{'-'*12}-+-{'-'*12}-+-{'-'*8}")

R_cas = np.load('l20_vtotal_minimum.npz', allow_pickle=True)['R_casimir']
tau_ref = np.load('l20_vtotal_minimum.npz', allow_pickle=True)['tau']

for tau, bkey in zip(bos_taus, bos_tau_keys):
    fi = np.argmin(np.abs(tau_ferm - tau))
    eigs_f = ferm_data[f'eigenvalues_{fi}']
    fmult_f = ferm_data[f'fermionic_mult_{fi}']

    expanded_f = []
    for e, m in zip(eigs_f, fmult_f):
        if m > 0 and abs(e) > 1e-12:
            expanded_f.extend([abs(e)] * int(m))
    expanded_f = np.sort(expanded_f)

    rec_b = bos_data[bkey]
    expanded_b = []
    for row in rec_b:
        eig = abs(row['eigenvalue'])
        mult = int(row['multiplicity'])
        if eig > 1e-12 and mult > 0:
            expanded_b.extend([eig] * mult)
    expanded_b = np.sort(expanded_b)

    # F/B at various N
    fb_50 = (0.5*np.sum(np.sqrt(expanded_f[:50]))) / (0.5*np.sum(np.sqrt(expanded_b[:50])))
    fb_500 = (0.5*np.sum(np.sqrt(expanded_f[:500]))) / (0.5*np.sum(np.sqrt(expanded_b[:500])))

    # Crossover N
    N_cross = None
    for N in range(10, min(len(expanded_f), len(expanded_b)), 10):
        Ef = 0.5 * np.sum(np.sqrt(expanded_f[:N]))
        Eb = 0.5 * np.sum(np.sqrt(expanded_b[:N]))
        if Eb > Ef:
            N_cross = N
            break
    if N_cross is None:
        for N in range(1000, min(len(expanded_f), len(expanded_b)), 100):
            Ef = 0.5 * np.sum(np.sqrt(expanded_f[:N]))
            Eb = 0.5 * np.sum(np.sqrt(expanded_b[:N]))
            if Eb > Ef:
                N_cross = N
                break

    # Full-spectrum R
    ri = np.argmin(np.abs(tau_ref - tau))
    fb_full = R_cas[ri]

    print(f"  {tau:5.2f} | {N_cross:>8d} | {fb_50:12.4f} | {fb_500:12.4f} | {fb_full:8.4f}")

# --- 4. The convergence question ---
print("\n--- 4. THE CONVERGENCE QUESTION ---")
print("""
  You asked: "Isn't this the convergence we've needed for baryons/fermions?"

  WHAT THE DATA SHOWS:
  ====================

  A. At low mode count (N < 14,000-25,000), fermionic zero-point energy
     EXCEEDS bosonic zero-point energy. F/B > 1.

  B. This is NOT the Weyl limit. The full-spectrum F/B = 0.55 (bosons win).
     The low-mode physics is qualitatively different.

  C. The crossover N_cross INCREASES with tau: from 14,000 at tau=0 to
     25,000 at tau=0.50. As the internal space deforms, fermion dominance
     extends to higher energies.

  D. The gap-edge ratio (ferm_min / bos_min) grows from 1.88 to 3.59
     across tau = [0, 0.50]. Bosonic gap softens; fermionic gap stays
     rigid (for tau < 0.3) then slowly rises.

  WHAT THIS MEANS FOR THE FRAMEWORK:
  ===================================

  IF there exists a physical IR cutoff Lambda_IR such that only modes
  with lambda < Lambda_IR^2 contribute to the effective potential:

  1. For Lambda_IR below the fermionic gap (< 0.83 at tau=0):
     -> Only bosonic modes contribute. V_eff is purely bosonic. No cancellation.
     -> V_eff DECREASES with tau (bosonic gap softens -> more modes enter).
     -> This gives a RUNAWAY toward large tau (decompactification).

  2. For Lambda_IR just above the fermionic gap:
     -> Fermionic modes enter and DOMINATE (F/B > 1).
     -> V_eff becomes NEGATIVE (fermion vacuum energy exceeds boson).
     -> This gives a RESTORING FORCE toward smaller tau.

  3. The EQUILIBRIUM is where these two effects balance:
     -> At the tau where the first fermionic mode enters the window.
     -> This is controlled by the gap-edge: lambda_ferm_min(tau) = Lambda_IR.
     -> For a FIXED Lambda_IR, this gives a specific tau_0.

  THIS IS THE BCS ANALOGY IN ACTION:
  ===================================

  In BCS superconductivity:
  - The free energy is monotonically INCREASING in the gap parameter
  - BUT the self-consistency equation Delta = g*K(Delta) has a nontrivial solution
  - The system doesn't minimize free energy — it satisfies self-consistency

  Here:
  - V_eff(tau) is monotonically increasing at the Weyl level (trap theorem)
  - BUT if Lambda_IR is dynamically determined by tau itself
    (e.g., Lambda_IR(tau) = lambda_ferm_min(tau)),
    the self-consistent solution tau_0 satisfies a GAP EQUATION, not dV/dtau = 0

  The "convergence for baryons" interpretation:
  - Below the KK scale, the lightest modes are BOSONIC (gauge + scalar)
  - But each FERMIONIC mode carries MORE zero-point energy (higher gap)
  - As modes are populated, fermions overtake bosons
  - The crossover scale N_cross ~ 14,000-25,000 modes is the "baryon threshold"
  - Above this scale, bosons dominate (radiation-like)
  - Below this scale, fermions dominate (matter-like)
""")

# --- 5. Is this actually about baryon asymmetry? ---
print("--- 5. HONEST ASSESSMENT ---")
print("""
  CAUTION: This is NOT directly baryon asymmetry.

  Baryon asymmetry (eta ~ 6e-10) requires:
  1. Baryon number violation (B)
  2. C and CP violation
  3. Departure from thermal equilibrium (Sakharov conditions)

  What we have is:
  - Fermionic modes have higher zero-point energy per mode than bosonic modes
  - This is a SPECTRAL asymmetry, not a particle number asymmetry
  - It operates at the KK scale, not at the electroweak scale

  WHAT IT COULD BE:
  - A structural explanation for WHY the low-energy effective theory
    has more fermionic than bosonic degrees of freedom in the IR
  - A mechanism for preferential fermionic condensation at the
    modulus stabilization point
  - An input to the BCS-type gap equation where the fermion-dominated
    regime provides the restoring force

  WHAT IT IS NOT:
  - A direct computation of eta = n_B/n_gamma
  - A replacement for electroweak baryogenesis
  - A prediction of the baryon-to-photon ratio

  It is more like: the reason matter EXISTS rather than pure radiation
  is that the internal geometry preferentially supports fermionic modes
  at low energies. The specific amount of matter vs radiation depends
  on the dynamics (which we haven't solved).
""")
