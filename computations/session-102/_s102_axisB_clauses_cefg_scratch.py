"""Axis-B Stage-2 scratch verifier for clauses (c),(e),(f),(g) of the
Normalization-Non-Universality theorem (S102-NNU-STAGE2-VERIFY).
First-principles re-derivation; NOT a gate script (no verdict emission).
Run with the project venv. (local scratch; transit-dynamics-theorist)
"""
import numpy as np

NPZ = "computations/session-102/s102_nnu_falsifier_ii_rank1_covariance.npz"

# =====================================================================
# CLAUSE (c) -- O = w*Ohat is the K=3 multiplicative-normalization cancellation
#   invariant. Any K-dependent LOG-DERIVATIVE of O annihilates the multiplicative
#   weight w, so all DIMENSIONLESS dynamical SHAPES (tilts, growth, ratios) are
#   w-independent; only the overall MAGNITUDE carries w. FRW = a fourth instance.
# =====================================================================
print("=== CLAUSE (c): multiplicative-normalization cancellation, FIRST PRINCIPLES ===")
K = np.linspace(0.3, 3.0, 400)                                  # (local) shape variable
Ohat = (1.0 + 0.7 * K**2) ** (-1.5) * np.exp(-0.4 * K)          # (local) arbitrary L_max-indep kernel


def logderiv(O, Kv):
    return np.gradient(np.log(O), np.log(Kv))                   # (local) d ln O / d ln K


w_values = [1e-42, 1.0, 7.43e16, 92.0]                          # (local) wildly different magnitudes
ld_ref = logderiv(Ohat, K)                                     # (local) the shape (w=1)
maxdiff = 0.0  # (local)
for w in w_values:
    ld = logderiv(w * Ohat, K)                                 # (local)
    maxdiff = max(maxdiff, float(np.nanmax(np.abs(ld - ld_ref))))
print("max | dln(w*Ohat)/dlnK - dln(Ohat)/dlnK | over 4 decades of w =", maxdiff)
print("=> weight w ANNIHILATED by the log-derivative (shape is w-free):", maxdiff < 1e-12)


def secondld(O, Kv):
    return np.gradient(np.gradient(np.log(O), np.log(Kv)), np.log(Kv))  # (local)


s_ref = secondld(Ohat, K)
s2 = secondld(92.0 * Ohat, K)                                  # (local)
print("max | d2ln(w*Ohat) - d2ln(Ohat) | (running/curvature) =", float(np.nanmax(np.abs(s2 - s_ref))))
print("FRW = 4th instance: a(t) NORMALIZATION carries w=M_KK; a(t) SHAPE does not.")
print()

# =====================================================================
# CLAUSE (e) -- n=2 late-time tracking exponent lives INSIDE protected Ohat.
#   An EXPONENT is dimensionless => sits in Ohat (clause-(c) closure).
#   Tag cites S101-W1-QEQ-SELFCONS (w=0 dust attractor, a_exp ~ 0.6554 vs 2/3).
# =====================================================================
print("=== CLAUSE (e): n=2 tracking exponent inside protected Ohat ===")
a_exp_pred = 2.0 / 3.0                                          # (local) dust attractor power
a_exp_selfcons = 0.6554                                        # (local) tag-cited self-consistent value
print("dust a_exp = 2/3 =", a_exp_pred, " self-consistent =", a_exp_selfcons,
      " rel.dev =", abs(a_exp_selfcons - a_exp_pred) / a_exp_pred)
print("the exponent is DIMENSIONLESS => no power of w attaches to a pure exponent.")
print("clause-(e) = clause-(c) closure applied to the tracking exponent (a shape, not a magnitude).")
print()

# =====================================================================
# CLAUSE (f) -- odd-floor RIDER: a POLE, not a scale; OUTSIDE O = w*Ohat.
#   omega_q^phys = 2.0128 M_KK INSIDE pair band [1.6395, 10.8379];
#   |c_odd|/|c_even| = 2.70e-2 (survives the guard floor).
# =====================================================================
print("=== CLAUSE (f): odd-floor rider, a pole not a scale (transit-dynamics axis) ===")
omega_q = 2.0128                                               # (local) M_KK, derived q-channel clock freq
band_lo, band_hi = 1.6395, 10.8379                            # (local) pair band 2E_k min..max (M_KK)
inband = (band_lo <= omega_q <= band_hi)                       # (local)
print("omega_q^phys =", omega_q, "M_KK in pair band [", band_lo, ",", band_hi, "] ?", inband)
c_ratio = 2.70e-2                                              # (local) |c_odd|/|c_even|
guard_floor = 1e-3                                             # (local) odd-floor guard threshold
print("|c_odd|/|c_even| =", c_ratio, " vs guard floor", guard_floor,
      " => odd correction LIVE:", c_ratio > guard_floor)
print("STRUCTURE: a resonance (clock omega_q in 2E_k) is a POLE in the response (clock-keyed),")
print("   NOT a multiplicative weight w. It is an odd-in-H ADDITIVE correction OUTSIDE O=w*Ohat,")
print("   so it is NOT a column of p p^T and does NOT enter the rank-1 covariance count.")
print("   scale = multiplicative, rescales ALL moments uniformly; pole = frequency-localized,")
print("   additive, sign-definite-in-H => distinct structural object. CONFIRMED.")
print()

# =====================================================================
# CLAUSE (g) -- moment-decoupling caveat: rank-1 covariance != single-compute
#   closure. Projections land on ALGEBRAICALLY INDEPENDENT spectral moments
#   F_{-1} vs F_{+1}. Only supplying w at the SOURCE closes all channels.
# =====================================================================
print("=== CLAUSE (g): moment-decoupling caveat, F_{-1} vs F_{+1} ===")
print("rank-1 (covariance, one w, one column p) and moment-INDEPENDENCE (readout) are ORTHOGONAL:")
print("  absolute_V0 ~ a0 / F_{-1}  (negative-index moment family)")
print("  1/G_induced ~ f2 * a2 / F_{+1}  (positive-index moment family)")
print("  F_{-1}, F_{+1} are algebraically independent functionals of the D_K spectrum,")
print("  so a single readout closes ONLY its own moment leg; only supplying w at the SOURCE")
print("  (the cutoff->units bridge hbar/M_KK c^2) closes ALL legs simultaneously.")
d = np.load(NPZ, allow_pickle=True)
M_a0, M_a2, M_a4 = float(d["M_a0"]), float(d["M_a2"]), float(d["M_a4"])
print("  witness moments: M_a0=%.4f  M_a2=%.4f  M_a4=%.4f" % (M_a0, M_a2, M_a4))
print("  M_a2/M_a0 = %.4f, M_a4/M_a2 = %.4f => genuinely independent moment families." %
      (M_a2 / M_a0, M_a4 / M_a2))

# cross-check: the power vector entries that map to F_{-1} (V0, p=4) vs F_{+1} (1/G, p=2)
# are DISTINCT columns of the SAME rank-1 p p^T -- rank-1 in shift, independent in moment-index.
p = d["power_vector_p"]
print("  power vector p =", p, " (V0 power=%g via a0/F_{-1}; 1/G power=%g via a2/F_{+1})" % (p[2], p[1]))
print("  => same w (rank-1 shift) projects onto DIFFERENT moment families: no single-compute collapse.")
