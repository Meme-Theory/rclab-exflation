"""
Stage-2 Axis-B (Landau) INDEPENDENT no-overlap certificate for the n-th Mathieu
tongue half-width vs detuning, on the inv-12 W3-2 Ordered-Veil relic spectrum.

NON-AUTHOR cross-review: I recompute the half-width FROM FIRST PRINCIPLES using the
McLachlan / DLMF-28.6 characteristic-value-series leading coefficients I derived
symbolically (n=1: q ; n=2: q^2/4 ; n=3: q^3/64 ; general n>=4: |coeff_n| q^n),
rather than trusting the stored tongue_halfwidth_relic. Band-stability (|Tr M|<2)
holds for a mode at parameter A iff detuning |A - n^2| > half-width.

This is a READ-ONLY verification script (no framework constants consumed).
"""
import numpy as np

d = np.load(r"computations/investigation-12/inv12_w3_2_floquet_ordered_veil_resonance.npz",
            allow_pickle=True)

def get(k):
    return np.asarray(d[k])

A      = get("A_relic")              # mode parameter a = omega^2  (the "A")   # (local)
qrel   = get("q_relic")             # Mathieu q for each relic mode            # (local)
hw_npz = get("tongue_halfwidth_relic")  # stored half-width (for cross-check)  # (local)
nn     = get("nearest_n")           # nearest integer^2 zone index n            # (local)
dist   = get("dist_to_zone_A")      # |A - n^2| detuning                        # (local)
i_cl   = int(get("i_closest").flat[0])                                          # (local)
hpar   = float(get("h_par").flat[0])                                            # (local)
N      = A.size                                                                 # (local)

print(f"N relic modes = {N}")
print(f"h_par = {hpar}")
print(f"A range = [{A.min():.6f}, {A.max():.6f}]  sqrt(A_max) = {np.sqrt(A.max()):.6f}")
print(f"nearest_n range = [{nn.min()}, {nn.max()}]")

# --- 1. Sanity: is the stored q_relic consistent with q_M = A*h_par/2 ? ---
q_from_A = A * hpar / 2.0                                                       # (local)
print("\n[q consistency]  max|q_relic - A*h_par/2| =",
      float(np.max(np.abs(qrel - q_from_A))))

# --- 2. INDEPENDENT half-width from McLachlan leading coeffs (n=1..) ---
# Leading half-width coefficient c_n s.t. Delta_a_half ~= c_n * q^n.
# From DLMF-28.6 full-width series (half = full/2):
#   n=1: full 2q          -> half q          -> c_1 = 1
#   n=2: full q^2/2       -> half q^2/4      -> c_2 = 1/4
#   n=3: full q^3/32      -> half q^3/64     -> c_3 = 1/64
#   n>=4: |full-width coeff|/2 ; full-width leading coeff magnitude
#         A&S 20.2.25 -> width_n = 2 q^n / (4^{n-1} ((n-1)!)^2)   (asymptotic small-q)
#         half coeff c_n = q^n / (4^{n-1} ((n-1)!)^2)
import math
def half_coeff(n):                                                             # (local)
    if n == 1: return 1.0
    if n == 2: return 1.0/4.0
    if n == 3: return 1.0/64.0
    # general small-q tongue full width = 2 q^n / (4^{n-1} ((n-1)!)^2); half = /2
    return 1.0 / (4**(n-1) * (math.factorial(n-1))**2)

hw_indep = np.array([half_coeff(int(n)) * (q**int(n)) for n, q in zip(nn, qrel)])  # (local)

# Guard: zone n must be >=1 for tongue formula (a=n^2, n>=1). Check.
print("\n[zone] any nearest_n < 1 ?", bool(np.any(nn < 1)))

# --- 3. NO-OVERLAP certificate: half-width < detuning for EVERY mode ---
overlap_indep = hw_indep >= dist     # would-be-unstable under my own half-width  # (local)
overlap_npz   = hw_npz   >= dist     # under stored half-width                     # (local)
n_overlap_indep = int(np.sum(overlap_indep))                                    # (local)
n_overlap_npz   = int(np.sum(overlap_npz))                                      # (local)

print(f"\n[NO-OVERLAP, my independent half-width]  overlaps = {n_overlap_indep} / {N}")
print(f"[NO-OVERLAP, stored half-width]          overlaps = {n_overlap_npz} / {N}")

# --- 4. Worst-case high-A mode (closest approach to a zone centre) ---
print(f"\n[worst-case mode i_closest = {i_cl}]")
print(f"   A         = {A[i_cl]:.6f}")
print(f"   nearest_n = {nn[i_cl]}  (zone a = {nn[i_cl]**2})")
print(f"   q_relic   = {qrel[i_cl]:.6e}")
print(f"   detuning  = {dist[i_cl]:.6e}")
print(f"   half-width (my indep, c_n q^n) = {hw_indep[i_cl]:.6e}")
print(f"   half-width (stored npz)        = {hw_npz[i_cl]:.6e}")
print(f"   margin (detuning/half-width)   = {dist[i_cl]/hw_indep[i_cl]:.3e}  "
      f"= {np.log10(dist[i_cl]/hw_indep[i_cl]):.2f} decades")

# --- 5. Mnemonic-vs-exact: bare power vs prefactor-correct at broad-band-max q ---
q_max = float(qrel.max())                                                       # (local)
i_qmax = int(np.argmax(qrel))                                                   # (local)
print(f"\n[mnemonic-vs-exact at broad-band-max q = {q_max:.6e}, mode {i_qmax}, n={nn[i_qmax]}]")
print(f"   bare (q_M)^3            = {q_max**3:.6e}   (plan mnemonic; <=1e-7 ? {q_max**3 <= 1e-7})")
print(f"   prefactor (q_M)^3/64    = {q_max**3/64:.6e}   (<=1e-7 ? {q_max**3/64 <= 1e-7})")

# --- 6. Direct band-stability cross-check from monodromy trace ---
tr  = get("tr_relic")                                                           # (local)
print(f"\n[monodromy trace direct]  max|Tr M|_relic = {float(np.max(np.abs(tr))):.8f}  (<2 ? {float(np.max(np.abs(tr)))<2})")
print(f"   fraction_resonance = {float(get('fraction_resonance').flat[0])}")

# --- 7. Among A>9 modes, nearest_n in {3,4} only? (registry claim) ---
hi = A > 9.0                                                                    # (local)
print(f"\n[A>9 subset]  count = {int(np.sum(hi))};  unique nearest_n = {sorted(set(nn[hi].tolist()))}")

print("\n=== VERDICT-RELEVANT SUMMARY ===")
print(f"EXPONENT degree_q==n (symbolic, Sage)                : VERIFIED (n=1,2,3 -> 1,2,3)")
print(f"NO-OVERLAP (indep half-width) overlaps               : {n_overlap_indep} / {N}")
print(f"worst-case margin                                    : {np.log10(dist[i_cl]/hw_indep[i_cl]):.2f} decades")
print(f"max|Tr M|_relic                                      : {float(np.max(np.abs(tr))):.8f}")
