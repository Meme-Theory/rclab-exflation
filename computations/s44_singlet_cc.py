"""
SINGLET-CC-44: Singlet projection of GGE excitation energy.

Physics:
    In Kaluza-Klein reduction on K = SU(3), only the (0,0) singlet component
    of the internal stress-energy tensor T^{MN} sources 4D gravity:

        T^{mu nu}_{4D} = (1/V_K) integral_K T^{mu nu}(x, g) dV_K

    The integral over K projects onto the (0,0) singlet by Peter-Weyl
    orthogonality. The question: what fraction of E_exc transforms as singlet?

    A field phi in SU(3) representation (p,q) of dimension d_{p,q} has
    energy density |phi(g)|^2 * E_k. The modulus-squared |Y^{(p,q)}_{mn}(g)|^2
    decomposes under Clebsch-Gordan as:

        (p,q) tensor (p,q)* = (p,q) tensor (q,p) = sum_{R} C_R * R

    The singlet (0,0) always appears exactly ONCE in this decomposition.
    By Schur orthogonality:

        integral_K |Y^{(p,q)}_{mn}(g)|^2 dV_K = 1/d_{p,q}

    This is exact: the singlet fraction of |Y|^2 is 1/dim(R), independent
    of which basis element (m,n) is occupied.

    For the ENERGY (not just probability), E_singlet = sum_k n_k * E_k * (1/d_k),
    where d_k = dim of the SU(3) irrep containing mode k.

    However, there is a CRITICAL subtlety: the GGE occupies PAIRS of modes
    (k, -k) simultaneously due to BCS. A Cooper pair consists of a particle
    in (p,q) and its time-reverse in (q,p) = (p,q)*. The pair energy density
    is psi_k(g) * psi_{-k}(g), which lives in (p,q) tensor (q,p).
    The singlet component of this tensor product has dimension 1, and the
    total dimension is d_{p,q}^2. So the singlet fraction is 1/d_{p,q}^2.

    BUT: for the diagonal bilinear T^{00} = psi^dagger * psi (not psi*psi),
    we get |psi|^2, and the Schur integral gives 1/d_{p,q} as shown above.

    The Cooper pair wavefunction in coordinate space is:
        Phi_pair(g) = sum_{m,n} u_k * v_k * Y^{(p,q)}_{mn}(g)^2
    for a (p,q)-sector pair. But T^{00} involves |amplitude|^2, not amplitude^2.

    Resolution: T^{00} at point g is the sum of occupied quasiparticle energies
    weighted by the probability density at g. For a BCS quasiparticle in mode k
    with internal wavefunction Y_k(g):

        T^{00}(g) = sum_k n_k * E_qp_k * |Y_k(g)|^2

    Integrating over K:
        T^{00}_{4D} = sum_k n_k * E_qp_k * integral_K |Y_k(g)|^2 dV_K
                     = sum_k n_k * E_qp_k * (1/d_k)

    This is the Schur orthogonality result. The factor 1/d_k is EXACT.

Representations:
    B1: (1,0) + (0,1), d = 3, 1 pair. Singlet fraction: 1/3
    B2: (1,1) adjoint, d = 8, 4 pairs. Singlet fraction: 1/8
    B3: (3,0) + (0,3), d = 10, 3 pairs. Singlet fraction: 1/10

    Note on 1/d vs 1/d^2:
    The 1/d result comes from Schur's orthogonality for matrix elements:
        integral_K D^R_{mn}(g)^* D^R_{m'n'}(g) dV_K = (V_K/d_R) delta_{mm'} delta_{nn'}
    So integral |D^R_{mn}|^2 dV_K = V_K / d_R, giving singlet fraction 1/d_R.

    The 1/d^2 would apply to the overlap integral of TWO DIFFERENT functions
    both in the same irrep — not to the norm-squared of one function. The
    energy density T^{00} is a norm-squared (positive definite), so 1/d applies.

Author: Einstein-Theorist
Session: 44
Gate: SINGLET-CC-44 (PASS if E_singlet/E_total < 0.01)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 1. LOAD DATA
# ============================================================

base = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")

gge = np.load(base / "s39_gge_lambdas.npz", allow_pickle=True)
e42 = np.load(base / "s42_gge_energy.npz", allow_pickle=True)
hf  = np.load(base / "s42_hauser_feshbach.npz", allow_pickle=True)
ed  = np.load(base / "s35_ed_corrected_dos.npz", allow_pickle=True)

# GGE occupation probabilities per branch (pair excitation probability)
p_k = gge['p_k']  # 8 branches
branch_labels = gge['branch_labels']
E_8 = gge['E_8_s38']  # single-particle energies at fold (M_KK)

# Total excitation energy and pair count
E_exc_total = float(e42['E_exc_MKK'])
n_pairs_total = float(e42['n_pairs'])

print("=" * 70)
print("SINGLET-CC-44: Singlet Projection of GGE Excitation Energy")
print("=" * 70)
print()

# ============================================================
# 2. SECTOR DECOMPOSITION
# ============================================================

# Branch assignment: B2[0-3], B1, B3[0-2]
# B2 = (1,1) adjoint, dim = 8
# B1 = (1,0)+(0,1), dim = 3 (fundamental)
# B3 = (3,0)+(0,3), dim = 10

sector_dims = {
    'B2': 8,   # (1,1) adjoint
    'B1': 3,   # (1,0) fundamental
    'B3': 10,  # (3,0) decuplet
}

# Map branches to sectors
branch_sector = ['B2', 'B2', 'B2', 'B2', 'B1', 'B3', 'B3', 'B3']

# Quasiparticle energy: E_qp = sqrt(xi^2 + Delta^2)
# At fold with BCS: from the data
# The BCS ground state has condensation energy E_cond = -0.137 M_KK
# Excitation energy is 50.945 M_KK distributed over 59.8 pairs

# Per-branch contribution to total excitation
# The total excitation energy comes from pair-breaking:
# E_exc = sum_k n_k * 2*E_qp_k  (factor 2 for particle + hole in each pair)
# where n_k is the number of excited pairs in branch k

# From S39 data: p_k = probability of pair excitation per branch
# n_k = total_pairs * (p_k / sum(p_k)) but properly:
# The GGE has 59.8 pairs total. The distribution follows the doorway BRs.

# Method A: Use doorway branching ratios (from Hauser-Feshbach)
BR_B2 = float(e42['doorway_BR_B2'])  # 0.716
BR_B1 = float(e42['doorway_BR_B1'])  # 0.224
BR_B3 = float(e42['doorway_BR_B3'])  # 0.060

# Energy per sector = BR * E_total
E_B2 = BR_B2 * E_exc_total
E_B1 = BR_B1 * E_exc_total
E_B3 = BR_B3 * E_exc_total

print("--- SECTOR DECOMPOSITION (Doorway BR) ---")
print(f"E_exc total = {E_exc_total:.3f} M_KK")
print(f"n_pairs total = {n_pairs_total:.1f}")
print()
print(f"B2 (adjoint, d=8): BR={BR_B2:.4f}, E_B2={E_B2:.3f} M_KK")
print(f"B1 (fund.,   d=3): BR={BR_B1:.4f}, E_B1={E_B1:.3f} M_KK")
print(f"B3 (decup.,  d=10): BR={BR_B3:.4f}, E_B3={E_B3:.3f} M_KK")
print(f"Sum check: {E_B2+E_B1+E_B3:.3f} vs {E_exc_total:.3f}")
print()

# Method B: Use p_k directly from GGE lambdas
# p_k gives the probability each pair is in excited state
# Energy from branch k: proportional to p_k * E_qp_k * multiplicity
# (where multiplicity accounts for how many Cooper pairs are in that branch)

# For the GGE, each branch has exactly one Cooper pair.
# The pair excitation energy is 2*E_k (particle + hole).
# Energy from branch k = p_k * 2*E_k

E_branch = p_k * 2 * E_8
E_total_method_B = np.sum(E_branch)

E_B2_B = np.sum(E_branch[0:4])
E_B1_B = E_branch[4]
E_B3_B = np.sum(E_branch[5:8])

print("--- SECTOR DECOMPOSITION (GGE p_k * 2E_k) ---")
print(f"E_total (method B) = {E_total_method_B:.3f} M_KK")
for i, (bl, pk, ek, eb) in enumerate(zip(branch_labels, p_k, E_8, E_branch)):
    print(f"  {bl}: p_k={pk:.6f}, E_k={ek:.5f}, E_branch={eb:.5f}")
print(f"E_B2 = {E_B2_B:.4f}, E_B1 = {E_B1_B:.4f}, E_B3 = {E_B3_B:.4f}")
print(f"Fractions: B2={E_B2_B/E_total_method_B:.4f}, B1={E_B1_B/E_total_method_B:.4f}, B3={E_B3_B/E_total_method_B:.4f}")
print()

# The two methods give different scales because method B uses 8 pairs
# while the actual GGE has 59.8 pairs. The FRACTIONS are what matter.

# Method C: sector_BR_compound from Hauser-Feshbach (9-sector decomposition)
sector_labels_HF = e42['sector_labels']
sector_BR_compound = e42['sector_BR_compound']
sector_BR_acoustic = e42['sector_BR_acoustic']

print("--- 9-SECTOR DECOMPOSITION (Hauser-Feshbach) ---")
for i, (sl, brc, bra) in enumerate(zip(sector_labels_HF, sector_BR_compound, sector_BR_acoustic)):
    p, q = sl
    dim_pq = int(0.5 * (p+1) * (q+1) * (p+q+2))
    print(f"  ({p},{q}): dim={dim_pq:3d}, BR_compound={brc:.6f}, BR_acoustic={bra:.6f}")
print()

# ============================================================
# 3. SINGLET PROJECTION
# ============================================================

# Schur orthogonality theorem on SU(3):
# For normalized Peter-Weyl basis functions Y^{(p,q)}_{mn}(g):
#   integral_K |Y^{(p,q)}_{mn}(g)|^2 dV_K / V_K = 1/d_{p,q}
#
# Therefore the singlet fraction of T^{00} from modes in (p,q) is 1/d_{p,q}.

# Dimension formula for SU(3): d(p,q) = (p+1)(q+1)(p+q+2)/2

def su3_dim(p, q):
    return (p+1) * (q+1) * (p+q+2) // 2

# Verify dimensions
print("--- SU(3) DIMENSIONS ---")
for (p,q), name in [((0,0),'singlet'), ((1,0),'fund'), ((0,1),'anti-fund'),
                     ((1,1),'adjoint'), ((2,0),'6-dim'), ((0,2),'6-bar'),
                     ((3,0),'10-dim'), ((0,3),'10-bar'), ((2,1),'15-dim')]:
    print(f"  d({p},{q}) = {su3_dim(p,q)} ({name})")
print()

# Method A: Using 3-sector doorway BRs (B1, B2, B3 aggregated)
singlet_frac_A = (BR_B2 / sector_dims['B2'] +
                  BR_B1 / sector_dims['B1'] +
                  BR_B3 / sector_dims['B3'])

E_singlet_A = singlet_frac_A * E_exc_total

print("=" * 70)
print("METHOD A: 3-sector doorway (B1, B2, B3)")
print("=" * 70)
print(f"  E_singlet/E_total = BR_B2/d_B2 + BR_B1/d_B1 + BR_B3/d_B3")
print(f"                    = {BR_B2:.4f}/8 + {BR_B1:.4f}/3 + {BR_B3:.4f}/10")
print(f"                    = {BR_B2/8:.6f} + {BR_B1/3:.6f} + {BR_B3/10:.6f}")
print(f"                    = {singlet_frac_A:.6f}")
print(f"  E_singlet = {E_singlet_A:.4f} M_KK")
print(f"  E_nonsinglet = {E_exc_total - E_singlet_A:.4f} M_KK")
print(f"  Suppression: {1/singlet_frac_A:.1f}x")
print(f"  Log10 suppression: {-np.log10(singlet_frac_A):.3f} orders")
print()

# Method B: Using GGE p_k per branch
singlet_E_B = 0.0
total_E_B = 0.0
for i in range(8):
    d_i = sector_dims[branch_sector[i]]
    e_i = p_k[i] * 2 * E_8[i]
    singlet_E_B += e_i / d_i
    total_E_B += e_i

singlet_frac_B = singlet_E_B / total_E_B

print("=" * 70)
print("METHOD B: Per-branch GGE (p_k * 2*E_k / d_sector)")
print("=" * 70)
print(f"  E_singlet (unnorm) = {singlet_E_B:.6f}")
print(f"  E_total (unnorm) = {total_E_B:.6f}")
print(f"  E_singlet/E_total = {singlet_frac_B:.6f}")
print(f"  Suppression: {1/singlet_frac_B:.1f}x")
print(f"  Log10 suppression: {-np.log10(singlet_frac_B):.3f} orders")
print()

# Method C: Using full 9-sector Hauser-Feshbach compound BRs
singlet_frac_C_compound = 0.0
singlet_frac_C_acoustic = 0.0
for i, sl in enumerate(sector_labels_HF):
    p, q = sl
    d = su3_dim(p, q)
    singlet_frac_C_compound += sector_BR_compound[i] / d
    singlet_frac_C_acoustic += sector_BR_acoustic[i] / d

print("=" * 70)
print("METHOD C: Full 9-sector Hauser-Feshbach")
print("=" * 70)
print(f"  Compound nucleus regime:")
print(f"    E_singlet/E_total = {singlet_frac_C_compound:.6f}")
print(f"    Suppression: {1/singlet_frac_C_compound:.1f}x")
print(f"    Log10 suppression: {-np.log10(singlet_frac_C_compound):.3f} orders")
print(f"  Acoustic regime:")
print(f"    E_singlet/E_total = {singlet_frac_C_acoustic:.6f}")
print(f"    Suppression: {1/singlet_frac_C_acoustic:.1f}x")
print(f"    Log10 suppression: {-np.log10(singlet_frac_C_acoustic):.3f} orders")
print()

# Detail breakdown for compound
print("  Compound breakdown by sector:")
for i, sl in enumerate(sector_labels_HF):
    p, q = sl
    d = su3_dim(p, q)
    contrib = sector_BR_compound[i] / d
    print(f"    ({p},{q}): dim={d:3d}, BR={sector_BR_compound[i]:.6f}, singlet_contrib={contrib:.8f}")
print()

# Detail breakdown for acoustic
print("  Acoustic breakdown by sector:")
for i, sl in enumerate(sector_labels_HF):
    p, q = sl
    d = su3_dim(p, q)
    contrib = sector_BR_acoustic[i] / d
    print(f"    ({p},{q}): dim={d:3d}, BR={sector_BR_acoustic[i]:.6f}, singlet_contrib={contrib:.8f}")
print()

# ============================================================
# 4. CROSS-CHECK: DIRECT SCHUR PROJECTION
# ============================================================

# Cross-check: The (0,0) sector itself contributes with singlet fraction = 1
# (since d(0,0) = 1). All other sectors contribute 1/d.

# For the acoustic BRs, the (0,0) sector has BR = 0.0240.
# That entire contribution IS singlet (trivially). This is a lower bound.

singlet_from_00 = sector_BR_acoustic[0]  # = 0.0240
singlet_from_rest_acoustic = singlet_frac_C_acoustic - singlet_from_00

print("--- CROSS-CHECK: (0,0) contribution ---")
print(f"  Acoustic: singlet from (0,0) alone = {singlet_from_00:.6f}")
print(f"  Acoustic: singlet from non-(0,0)  = {singlet_from_rest_acoustic:.6f}")
print(f"  Compound: singlet from (0,0) alone = {sector_BR_compound[0]:.6f}")
print(f"  Compound: singlet from non-(0,0)  = {singlet_frac_C_compound - sector_BR_compound[0]:.6f}")
print()

# ============================================================
# 5. ALTERNATIVE: 1/d^2 ARGUMENT (TENSOR PRODUCT OF FIELDS)
# ============================================================

# A Cooper pair in BCS has wavefunction Phi(g1, g2) = u*v * Y(g1)*Y(g2)
# where both particles are in the SAME representation but opposite K_7.
# The pair density involves |Phi|^2 ~ |Y(g1)|^2 * |Y(g2)|^2.
# If we integrate over the CENTER-OF-MASS coordinate, the singlet fraction
# of |Y|^2 is 1/d (as above). The pair internal coordinate is irrelevant
# for T^{00} which counts total energy at a point.
#
# HOWEVER, some authors argue the relevant quantity is the pair anomalous
# density F(g) = <psi_up(g) psi_down(g)>, which IS Y^2 (not |Y|^2).
# Y^{(p,q)} * Y^{(p,q)} lives in the SYMMETRIC part of (p,q) x (p,q).
# The singlet of (p,q) x (q,p) has fraction 1/d^2.
# But T^{00} is NOT the anomalous density — it is the energy density.
# T^{00} = psi^dagger * H * psi, which gives |Y|^2, not Y^2.
# So 1/d is correct for T^{00}, not 1/d^2.
#
# For completeness, compute 1/d^2 case:

singlet_frac_d2_A = (BR_B2 / sector_dims['B2']**2 +
                     BR_B1 / sector_dims['B1']**2 +
                     BR_B3 / sector_dims['B3']**2)

singlet_frac_d2_C_compound = 0.0
for i, sl in enumerate(sector_labels_HF):
    p, q = sl
    d = su3_dim(p, q)
    singlet_frac_d2_C_compound += sector_BR_compound[i] / d**2

print("--- ALTERNATIVE: 1/d^2 (anomalous density, NOT physical) ---")
print(f"  Method A (3-sector): E_singlet/E_total = {singlet_frac_d2_A:.8f}")
print(f"  Method C (9-sector compound): E_singlet/E_total = {singlet_frac_d2_C_compound:.8f}")
print(f"  Log10 suppression (A): {-np.log10(singlet_frac_d2_A):.3f} orders")
print(f"  (This is NOT the physical answer — included for comparison only)")
print()

# ============================================================
# 6. FINAL RESULT & GATE VERDICT
# ============================================================

# Use Method C (compound) as canonical — it uses the full 9-sector decomposition
# which properly weights the higher representations
singlet_frac_canonical = singlet_frac_C_compound
E_singlet_canonical = singlet_frac_canonical * E_exc_total

# Cross-method consistency
print("=" * 70)
print("CROSS-METHOD CONSISTENCY")
print("=" * 70)
print(f"  Method A (3-sector doorway): {singlet_frac_A:.6f}")
print(f"  Method B (GGE per-branch):   {singlet_frac_B:.6f}")
print(f"  Method C (9-sector compound): {singlet_frac_C_compound:.6f}")
print(f"  Method C (9-sector acoustic): {singlet_frac_C_acoustic:.6f}")
print(f"  Spread: {min(singlet_frac_A, singlet_frac_B, singlet_frac_C_compound, singlet_frac_C_acoustic):.6f} — {max(singlet_frac_A, singlet_frac_B, singlet_frac_C_compound, singlet_frac_C_acoustic):.6f}")
print()

# Gate evaluation
threshold_pass = 0.01
threshold_fail = 0.50

print("=" * 70)
print("GATE: SINGLET-CC-44")
print("=" * 70)
print(f"  E_singlet / E_total = {singlet_frac_canonical:.6f}")
print(f"  E_singlet = {E_singlet_canonical:.4f} M_KK")
print(f"  E_nonsinglet = {E_exc_total - E_singlet_canonical:.4f} M_KK")
print(f"  Suppression factor: {1/singlet_frac_canonical:.1f}x")
print(f"  Log10(E_singlet/E_total) = {np.log10(singlet_frac_canonical):.3f}")
print()

if singlet_frac_canonical < threshold_pass:
    verdict = "PASS"
    print(f"  VERDICT: **PASS** ({singlet_frac_canonical:.6f} < {threshold_pass})")
    print(f"  Suppression exceeds 2 orders of magnitude.")
elif singlet_frac_canonical > threshold_fail:
    verdict = "FAIL"
    print(f"  VERDICT: **FAIL** ({singlet_frac_canonical:.6f} > {threshold_fail})")
else:
    verdict = "INFO"
    print(f"  VERDICT: **INFO** ({threshold_pass} < {singlet_frac_canonical:.6f} < {threshold_fail})")
    print(f"  Intermediate suppression — less than 2 orders but significant.")

print()

# ============================================================
# 7. CC IMPLICATIONS
# ============================================================

# From CC-ARITH-37: R_CC ~ 112-115 orders (vacuum energy vs observed CC)
# The singlet projection buys log10(1/singlet_frac) orders
orders_gained = -np.log10(singlet_frac_canonical)

print("=" * 70)
print("CC IMPLICATIONS")
print("=" * 70)
print(f"  CC hierarchy problem: ~112 orders (CC-ARITH-37)")
print(f"  Singlet projection buys: {orders_gained:.2f} orders")
print(f"  Remaining after projection: ~{112 - orders_gained:.1f} orders")
print(f"  ")
print(f"  The singlet projection provides ~{orders_gained:.1f} orders of suppression.")
print(f"  This is a STRUCTURAL result (Schur orthogonality, exact),")
print(f"  but alone insufficient to resolve the CC hierarchy.")
print()
print(f"  However, the non-singlet energy is NOT 'dark matter' in the")
print(f"  traditional sense — it is energy in higher KK modes that")
print(f"  does NOT couple to 4D gravity at leading order in KK reduction.")
print(f"  It is truly INVISIBLE to the 4D gravitational sector.")
print()

# Physical interpretation
f_grav = singlet_frac_canonical
f_dark = 1 - f_grav
print(f"  Of E_exc = {E_exc_total:.1f} M_KK:")
print(f"    Gravitating (singlet):     {f_grav*100:.2f}% = {f_grav*E_exc_total:.3f} M_KK")
print(f"    Non-gravitating (non-sing): {f_dark*100:.2f}% = {f_dark*E_exc_total:.3f} M_KK")
print()

# Connection to DM: the non-gravitating fraction doesn't contribute to T^{00}_{4D}
# but it DOES affect KK mode dynamics. If it can be observed through other channels
# (gauge interactions that DO couple non-singlet modes), this predicts a specific
# ratio of "visible" to "gravitating" energy.
print(f"  NOTE: Non-singlet energy couples to SU(3) gauge fields,")
print(f"  not to 4D gravity. This is the reverse of the DM problem:")
print(f"  standard DM gravitates but doesn't gauge-couple.")
print(f"  Here we have energy that gauge-couples but doesn't gravitate.")

# ============================================================
# 8. SAVE DATA
# ============================================================

np.savez(
    base / "s44_singlet_cc.npz",
    # Core results
    E_exc_total=E_exc_total,
    singlet_fraction_methodA=singlet_frac_A,
    singlet_fraction_methodB=singlet_frac_B,
    singlet_fraction_compound=singlet_frac_C_compound,
    singlet_fraction_acoustic=singlet_frac_C_acoustic,
    singlet_fraction_canonical=singlet_frac_canonical,
    singlet_fraction_d2=singlet_frac_d2_A,
    E_singlet=E_singlet_canonical,
    E_nonsinglet=E_exc_total - E_singlet_canonical,
    suppression_factor=1.0/singlet_frac_canonical,
    log10_suppression=orders_gained,
    # Per-sector
    sector_dims_B1=sector_dims['B1'],
    sector_dims_B2=sector_dims['B2'],
    sector_dims_B3=sector_dims['B3'],
    E_B2_doorway=E_B2,
    E_B1_doorway=E_B1,
    E_B3_doorway=E_B3,
    BR_B2=BR_B2,
    BR_B1=BR_B1,
    BR_B3=BR_B3,
    # 9-sector detail
    sector_labels_9=sector_labels_HF,
    sector_BR_compound_9=sector_BR_compound,
    sector_BR_acoustic_9=sector_BR_acoustic,
    # Gate
    gate_name=np.array(["SINGLET-CC-44"]),
    gate_verdict=np.array([verdict]),
    gate_threshold_pass=threshold_pass,
    gate_threshold_fail=threshold_fail,
)

print()
print(f"Data saved to {base / 's44_singlet_cc.npz'}")

# ============================================================
# 9. PLOT
# ============================================================

fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))

# Panel 1: Sector energy decomposition (pie chart)
ax1 = axes[0]
sector_names = ['B2 (1,1)\nd=8', 'B1 (1,0)\nd=3', 'B3 (3,0)\nd=10']
sector_energies = [BR_B2, BR_B1, BR_B3]
colors_sector = ['#2196F3', '#FF9800', '#4CAF50']
wedges, texts, autotexts = ax1.pie(sector_energies, labels=sector_names,
                                     autopct='%1.1f%%', colors=colors_sector,
                                     startangle=90, pctdistance=0.65)
for t in autotexts:
    t.set_fontsize(10)
ax1.set_title('GGE Energy by SU(3) Sector\n(Doorway Branching Ratios)', fontsize=11)

# Panel 2: Singlet fraction per sector (bar chart)
ax2 = axes[1]
sectors = ['B2\n(1,1)', 'B1\n(1,0)', 'B3\n(3,0)', 'Total']
singlet_fracs_per = [1/8, 1/3, 1/10, singlet_frac_canonical]
bars = ax2.bar(sectors, singlet_fracs_per, color=['#2196F3', '#FF9800', '#4CAF50', '#F44336'],
               edgecolor='black', linewidth=0.5)
ax2.set_ylabel('Singlet Fraction (1/d)', fontsize=11)
ax2.set_title('Schur Singlet Projection\n(Orthogonality on SU(3))', fontsize=11)
ax2.axhline(y=threshold_pass, color='red', linestyle='--', alpha=0.7, label=f'PASS threshold ({threshold_pass})')
for bar, frac in zip(bars, singlet_fracs_per):
    ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.005,
             f'{frac:.4f}', ha='center', va='bottom', fontsize=9)
ax2.legend(fontsize=9)
ax2.set_ylim(0, 0.4)

# Panel 3: Energy budget — gravitating vs non-gravitating
ax3 = axes[2]
categories = ['Total\nE_exc', 'Singlet\n(gravitating)', 'Non-singlet\n(dark)']
values = [E_exc_total, E_singlet_canonical, E_exc_total - E_singlet_canonical]
colors_budget = ['#607D8B', '#F44336', '#9E9E9E']
bars3 = ax3.bar(categories, values, color=colors_budget, edgecolor='black', linewidth=0.5)
ax3.set_ylabel('Energy (M_KK)', fontsize=11)
ax3.set_title(f'4D Gravitational Coupling\nSinglet = {singlet_frac_canonical*100:.2f}% of Total', fontsize=11)
for bar, val in zip(bars3, values):
    ax3.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
             f'{val:.2f}', ha='center', va='bottom', fontsize=9)
ax3.set_ylim(0, 60)

plt.tight_layout()
fig.savefig(base / "s44_singlet_cc.png", dpi=150, bbox_inches='tight')
print(f"Plot saved to {base / 's44_singlet_cc.png'}")
print()

# Final summary
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"  Gate SINGLET-CC-44: {verdict}")
print(f"  E_singlet/E_total = {singlet_frac_canonical:.6f}")
print(f"  Singlet suppression: {orders_gained:.2f} orders")
print(f"  Physical: {(1-singlet_frac_canonical)*100:.1f}% of GGE energy is dark to 4D gravity")
print(f"  Schur orthogonality: EXACT (not approximate)")
print("=" * 70)
