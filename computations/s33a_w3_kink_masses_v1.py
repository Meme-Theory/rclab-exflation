#!/usr/bin/env python3
"""
Session 33a Step 5: W_3 Kink Mass Ratios vs phi_paasch.

Compare A_2 Toda / W_3 M(6,5) minimal model kink mass ratios to
phi_paasch = 1.531580.

Mathematical background:
    The Z_3 Potts model at criticality is described by the W_3 minimal model
    M(6,5) with central charge c = 4/5. Its kink spectrum is determined by
    the Bethe ansatz / exact S-matrix approach.

    The A_2 affine Toda field theory (integrable deformation of W_3 minimal
    model) has particles with exact mass ratios:
        m_1 = m_2 (degenerate doublet, Z_3 symmetry)
    Higher-mass particles form a bootstrap structure.

    The A_2 Toda mass spectrum is:
        m_a/m_1 for each particle species a.

    For the A_n-1 Toda theories, the mass spectrum is:
        m_a/m_1 = sin(a*pi/n) / sin(pi/n)   for a = 1, ..., n-1

    For A_2: n = 3, so a = 1, 2
        m_1/m_1 = 1
        m_2/m_1 = sin(2*pi/3) / sin(pi/3) = 1 (degenerate doublet)

    The GOLDEN RATIO appears in A_4 Toda (E8 related):
        m_2/m_1 = 2*cos(pi/5) = phi = 1.6180...
    This is NOT the A_2 system.

    For the W_3 minimal model M(6,5), the scaling dimensions of primary
    fields are:
        Delta = {0, 2/5, 7/5, 3, 2/3, 1/15, ...}
    Kink masses between adjacent Z_3 vacua are related to these dimensions.

    Additional mass ratios from conformal perturbation theory of the Z_3
    Potts model (the phi_{2,1} perturbation deforming M(6,5)):
    The particle spectrum was computed by Fateev-Zamolodchikov and
    Reshetikhin-Smirnov. The result: the spectrum consists of a doublet
    (m_1 = m_2) and their bound states with specific mass ratios.

Author: sim (phonon-exflation-sim)
Date: 2026-03-06
"""

import numpy as np

# ─────────────────────────────────────────────────────────────
# 1. phi_paasch target
# ─────────────────────────────────────────────────────────────

phi_paasch = 1.531580
tolerance = 0.02  # 2%
window_low = phi_paasch * (1 - tolerance)
window_high = phi_paasch * (1 + tolerance)
print(f"Target: phi_paasch = {phi_paasch}")
print(f"2% tolerance window: [{window_low:.4f}, {window_high:.4f}]")

# ─────────────────────────────────────────────────────────────
# 2. A_n Toda field theory mass spectra
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("A_n TODA FIELD THEORY MASS RATIOS")
print(f"{'=' * 70}")

# General formula for A_{n-1} simply-laced Toda:
# m_a / m_1 = sin(a*pi/n) / sin(pi/n)  for a = 1, ..., n-1

all_ratios = {}

for n in range(2, 10):  # A_1 through A_8
    masses = []
    for a in range(1, n):
        ratio = np.sin(a * np.pi / n) / np.sin(np.pi / n)
        masses.append((a, ratio))
    print(f"\n  A_{n-1} (n={n}):")
    for a, r in masses:
        match = "*** MATCH ***" if window_low <= r <= window_high else ""
        print(f"    m_{a}/m_1 = sin({a}pi/{n})/sin(pi/{n}) = {r:.6f} {match}")
        all_ratios[f'A{n-1}_m{a}/m1'] = r

# ─────────────────────────────────────────────────────────────
# 3. E-type Toda mass ratios (E6, E7, E8)
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("E-TYPE TODA MASS RATIOS")
print(f"{'=' * 70}")

# E6 masses (from Dorey, 1991): normalized to m_1
# E6 has 6 particles, masses given by Coxeter exponents
# Coxeter number h = 12, exponents: 1, 4, 5, 7, 8, 11
e6_exponents = [1, 4, 5, 7, 8, 11]
e6_masses = [np.sin(e * np.pi / 12) / np.sin(np.pi / 12) for e in e6_exponents]
print(f"\n  E6 (h=12, exponents {e6_exponents}):")
for i, (e, m) in enumerate(zip(e6_exponents, e6_masses)):
    match = "*** MATCH ***" if window_low <= m <= window_high else ""
    all_ratios[f'E6_m{i+1}/m1'] = m
    print(f"    m({e})/m(1) = sin({e}pi/12)/sin(pi/12) = {m:.6f} {match}")

# E7: Coxeter number h = 18, exponents: 1, 5, 7, 9, 11, 13, 17
e7_exponents = [1, 5, 7, 9, 11, 13, 17]
e7_masses = [np.sin(e * np.pi / 18) / np.sin(np.pi / 18) for e in e7_exponents]
print(f"\n  E7 (h=18, exponents {e7_exponents}):")
for i, (e, m) in enumerate(zip(e7_exponents, e7_masses)):
    match = "*** MATCH ***" if window_low <= m <= window_high else ""
    all_ratios[f'E7_m{i+1}/m1'] = m
    print(f"    m({e})/m(1) = sin({e}pi/18)/sin(pi/18) = {m:.6f} {match}")

# E8: Coxeter number h = 30, exponents: 1, 7, 11, 13, 17, 19, 23, 29
e8_exponents = [1, 7, 11, 13, 17, 19, 23, 29]
e8_masses = [np.sin(e * np.pi / 30) / np.sin(np.pi / 30) for e in e8_exponents]
print(f"\n  E8 (h=30, exponents {e8_exponents}):")
for i, (e, m) in enumerate(zip(e8_exponents, e8_masses)):
    match = "*** MATCH ***" if window_low <= m <= window_high else ""
    all_ratios[f'E8_m{i+1}/m1'] = m
    print(f"    m({e})/m(1) = sin({e}pi/30)/sin(pi/30) = {m:.6f} {match}")

# ─────────────────────────────────────────────────────────────
# 4. Z_3 Potts / W_3 specific ratios
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("Z_3 POTTS / W_3 M(6,5) SPECIFIC RATIOS")
print(f"{'=' * 70}")

# The Z_3 Potts model perturbed by its thermal operator corresponds to
# the A_2 affine Toda theory. The particle content is:
# - Two degenerate particles m_1 = m_2 (Z_3 doublet)
# - No higher particles in A_2 (only 2 particles for A_2)

# For the phi_{1,2} perturbation (magnetic direction), the spectrum
# is different and related to the Ising / tricritical Ising perturbed CFT.

# W_3 M(6,5) primary fields and their scaling dimensions:
# (r,s) with 1 <= r <= 4, 1 <= s <= 5 (p=6, p'=5)
# Delta_{r,s} = [(6*s - 5*r)^2 - 1] / 120
print("\n  W_3 M(6,5) scaling dimensions (c = 4/5):")
p, pp = 6, 5
dims = {}
for r in range(1, p):
    for s in range(1, pp):
        Delta = ((p * s - pp * r)**2 - 1) / (4 * p * pp)
        key = f'({r},{s})'
        dims[key] = Delta

# Sort by Delta
for key, Delta in sorted(dims.items(), key=lambda x: x[1]):
    print(f"    Delta{key} = {Delta:.6f}")

# Ratios of scaling dimensions
print("\n  Ratios of non-zero scaling dimensions:")
non_zero_dims = [(k, v) for k, v in sorted(dims.items(), key=lambda x: x[1]) if v > 0.001]
ratio_list = []
for i in range(len(non_zero_dims)):
    for j in range(i + 1, len(non_zero_dims)):
        ki, di = non_zero_dims[i]
        kj, dj = non_zero_dims[j]
        r = dj / di
        ratio_list.append((f'Delta{kj}/Delta{ki}', r))
        all_ratios[f'W3_Delta{kj}/Delta{ki}'] = r

# Check for matches
matches_dim_ratio = [(name, r) for name, r in ratio_list if window_low <= r <= window_high]
if matches_dim_ratio:
    print(f"\n  MATCHES in scaling dimension ratios:")
    for name, r in matches_dim_ratio:
        print(f"    {name} = {r:.6f}")
else:
    print(f"\n  No matches in scaling dimension ratios")

# ─────────────────────────────────────────────────────────────
# 5. Additional exact mass ratios
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("ADDITIONAL EXACT RATIOS FROM INTEGRABLE FIELD THEORIES")
print(f"{'=' * 70}")

# D-type Toda: D_n mass spectrum
# D_4 (relevant because SU(3) ~ A_2, and D_4 has triality related to Z_3):
# D_4 particles: m_v = m_s = m_c (three nodes equivalent by triality)
# and m_0 (central node). Mass ratio: m_0/m_v = 2*cos(pi/6) = sqrt(3)
d4_ratio = np.sqrt(3)
all_ratios['D4_m0/mv'] = d4_ratio
print(f"\n  D_4 (triality): m_0/m_v = sqrt(3) = {d4_ratio:.6f}")

# sqrt(7/3) -- the bi-invariant SU(3) algebraic invariant
sqrt73 = np.sqrt(7.0/3.0)
all_ratios['sqrt(7/3)'] = sqrt73
print(f"\n  sqrt(7/3) (SU(3) bi-invariant): {sqrt73:.6f}")
print(f"    Relative to phi_paasch: {sqrt73/phi_paasch:.6f} "
      f"({'matches' if window_low <= sqrt73 <= window_high else 'no match'})")

# 2*cos(pi/7) -- appears in various TBA systems
cos_pi7 = 2 * np.cos(np.pi / 7)
all_ratios['2cos(pi/7)'] = cos_pi7
print(f"\n  2*cos(pi/7): {cos_pi7:.6f}")

# Specific check: are there ratios involving sin/cos with small integer arguments
# that give phi_paasch?
print(f"\n  Systematic search for 2*cos(pi/n) near phi_paasch:")
for n in range(3, 50):
    r = 2 * np.cos(np.pi / n)
    if window_low <= r <= window_high:
        print(f"    2*cos(pi/{n}) = {r:.6f} *** MATCH ***")
        all_ratios[f'2cos(pi/{n})'] = r

print(f"\n  Systematic search for sin(a*pi/n)/sin(pi/n) near phi_paasch:")
for n in range(3, 50):
    for a in range(2, n):
        r = np.sin(a * np.pi / n) / np.sin(np.pi / n)
        if window_low <= r <= window_high:
            print(f"    sin({a}pi/{n})/sin(pi/{n}) = {r:.6f} *** MATCH ***")
            all_ratios[f'sin({a}pi/{n})/sin(pi/{n})'] = r

# ─────────────────────────────────────────────────────────────
# 6. Gate evaluation
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("GATE EVALUATION: W3-33a")
print(f"{'=' * 70}")

# Find all matches within 2% window
matches = [(name, r) for name, r in all_ratios.items()
           if window_low <= r <= window_high]

# Sort by proximity to phi_paasch
matches.sort(key=lambda x: abs(x[1] - phi_paasch))

print(f"\n  All mass ratios within 2% of phi_paasch = {phi_paasch}:")
if matches:
    for name, r in matches:
        pct = abs(r - phi_paasch) / phi_paasch * 100
        print(f"    {name} = {r:.6f} ({pct:.3f}% off)")
else:
    print(f"    NONE")

# Also check 5% window
matches_5pct = [(name, r) for name, r in all_ratios.items()
                if phi_paasch * 0.95 <= r <= phi_paasch * 1.05]
matches_5pct.sort(key=lambda x: abs(x[1] - phi_paasch))

# Find closest overall
closest = min(all_ratios.items(), key=lambda x: abs(x[1] - phi_paasch))
print(f"\n  Closest ratio overall: {closest[0]} = {closest[1]:.6f} "
      f"({abs(closest[1]-phi_paasch)/phi_paasch*100:.3f}% off)")

# Verdict
if matches:
    verdict = "PASS"
    print(f"\n  >>> W3-33a verdict: PASS ({len(matches)} match(es) within 2%) <<<")
elif matches_5pct:
    verdict = "SOFT PASS"
    print(f"\n  >>> W3-33a verdict: SOFT PASS ({len(matches_5pct)} match(es) within 5%) <<<")
else:
    verdict = "FAIL"
    print(f"\n  >>> W3-33a verdict: FAIL (no matches within 5%) <<<")

print(f"  Interpretation: {'phi_paasch from conformal universality' if verdict != 'FAIL' else 'spectral-geometric origin preserved'}")

# ─────────────────────────────────────────────────────────────
# 7. Save
# ─────────────────────────────────────────────────────────────

# Save all ratios and results
ratio_names = np.array(list(all_ratios.keys()))
ratio_values = np.array(list(all_ratios.values()))

np.savez('tier0-computation/s33a_w3_kink_masses.npz',
         phi_paasch=np.array([phi_paasch]),
         tolerance=np.array([tolerance]),
         ratio_names=ratio_names,
         ratio_values=ratio_values,
         verdict=np.array([verdict]),
         closest_name=np.array([closest[0]]),
         closest_value=np.array([closest[1]]),
         n_matches_2pct=np.array([len(matches)]),
         n_matches_5pct=np.array([len(matches_5pct)]),
         )
print("\nData saved: tier0-computation/s33a_w3_kink_masses.npz")

# ─────────────────────────────────────────────────────────────
# 8. Summary
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("SUMMARY: W3-33a")
print(f"{'=' * 70}")
print(f"  phi_paasch = {phi_paasch}")
print(f"  Searched: A_n Toda (n=2..9), E6/E7/E8, D4, W_3 M(6,5) scaling dims,")
print(f"            2cos(pi/n) (n=3..49), sin(a*pi/n)/sin(pi/n) (n=3..49)")
print(f"  Total ratios checked: {len(all_ratios)}")
print(f"  Matches within 2%: {len(matches)}")
print(f"  Matches within 5%: {len(matches_5pct)}")
print(f"  Closest: {closest[0]} = {closest[1]:.6f}")
print(f"  Verdict: {verdict}")
