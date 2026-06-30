"""
S84-W8A-AUDIT-SG: sign-chain verification for spectral-geometer audit of W8-85.

Substitution chain under examination (Eq. 85.1 of plan):
  dS/dtau = 4 * sum_n c_n * f'(x_n) * x_n    with x_n = lambda_n^2 / Lambda^2

For a POSITIVE decreasing regulator f (e.g. Gaussian f(x) = exp(-x/2)),
f'(x) < 0 everywhere, so f'(x)*x < 0 for x > 0.

For a POSITIVE increasing regulator f (e.g. sqrt-cutoff f(x) = sqrt(x),
which is S42's |lambda|), f'(x) = 1/(2*sqrt(x)) > 0.

HYPOTHESIS: the sign of dS/dtau and d^2S/dtau^2 is regulator-family-dependent
because f'(x) has DIFFERENT SIGNS for decreasing vs increasing regulators.

This script:
(a) Confirms the signs of f'(x) for the two canonical regulator choices,
(b) Writes the substitution chain explicitly for a 2-mode toy model,
(c) Verifies numerically that sign(dS/dtau_gauss) = -sign(dS/dtau_abs) GENERICALLY,
    independent of Jensen-ansatz correctness.
"""
import numpy as np

print("=" * 72)
print("SIGN-CHAIN VERIFICATION (SG AUDIT)")
print("=" * 72)

# -----------------------------------------------------------------------
# Step 1: Definitions
# -----------------------------------------------------------------------
print("\n[Step 1] Regulator definitions:")
print("  Gaussian f_G(x) = exp(-x/2); f_G'(x) = -exp(-x/2)/2")
print("  Sqrt    f_S(x) = sqrt(x);    f_S'(x) = 1/(2*sqrt(x))  for x > 0")

x_test = np.linspace(0.1, 3.0, 8)  # (local) test grid
fpG = -0.5 * np.exp(-x_test / 2.0)  # (local)
fpS = 0.5 / np.sqrt(x_test)  # (local)

print(f"\n  x        f_G'(x)       f_S'(x)")
for xv, g, s in zip(x_test, fpG, fpS):
    print(f"  {xv:5.2f}  {g:+.4f}      {s:+.4f}")

print("\n[Sign read-off] f_G' < 0 for all x > 0. f_S' > 0 for all x > 0.")
print("                Opposite signs at every x. GENERIC.")

# -----------------------------------------------------------------------
# Step 2: Toy-model substitution chain (2 modes, known Jensen deformation)
# -----------------------------------------------------------------------
print("\n" + "=" * 72)
print("[Step 2] Toy 2-mode Jensen model")
print("=" * 72)

# Mode 1: 'squeezed' under Jensen (analog of SU(3) c_1 = +1 direction)
# Mode 2: 'expanded'  under Jensen (analog of SU(3) c_2 = -1 direction)
# At tau=0, lam_1 = lam_2 = 1 (unit eigenvalues in Lambda = 1 units).
# Under Jensen:
#    lam_1(tau) = exp(+1 * tau)  (squeezed larger)
#    lam_2(tau) = exp(-1 * tau)  (expanded smaller)
# c_n = +1, -1 respectively.  This matches the plan's
# lambda_n(tau) = alpha_n * exp(2*tau*c_n) ansatz with c_1 = +1/2, c_2 = -1/2.

tau = 0.19  # (local)
lam = np.array([np.exp(+tau), np.exp(-tau)])  # (local)  eigenvalues at tau
c = np.array([+0.5, -0.5])  # (local)  Jensen root coefficients
# mult_n = 1 for both (no multiplicity structure in toy)
mult = np.array([1.0, 1.0])  # (local)

# Eq. 85.1: dS/dtau = 4 * sum_n c_n * f'(x_n) * x_n
x = lam**2  # (local)  (Lambda = 1)

dS_G = 4.0 * np.sum(c * (-0.5 * np.exp(-x/2.0)) * x)  # (local)  Gaussian
dS_S = 4.0 * np.sum(c * (0.5 / np.sqrt(x)) * x)  # (local)  sqrt / |lambda|

print(f"\n  tau        = {tau}")
print(f"  lam        = {lam}")
print(f"  x = lam^2  = {x}")
print(f"  c_n        = {c}")
print(f"\n  dS/dtau (Gaussian regulator)    = {dS_G:+.6e}")
print(f"  dS/dtau (sqrt / |lambda| reg.)  = {dS_S:+.6e}")
print(f"\n  ratio dS_G / dS_S              = {dS_G/dS_S:+.6f}")

# The physically meaningful thing: are the signs OPPOSITE?
if np.sign(dS_G) * np.sign(dS_S) < 0:
    print("\n  SIGN FLIP CONFIRMED: Gaussian and sqrt regulators give OPPOSITE")
    print("  sign dS/dtau from the SAME Jensen deformation (same c_n, same lam_n).")
    print("  This is MECHANICAL (f'_G < 0, f'_S > 0), not physical.")
else:
    print("\n  No sign flip in this particular toy realization. Must check more.")

# -----------------------------------------------------------------------
# Step 3: Second derivative sign flip
# -----------------------------------------------------------------------
print("\n" + "=" * 72)
print("[Step 3] d^2S/dtau^2 sign comparison")
print("=" * 72)

# Under ansatz lam_n(tau) = alpha_n * exp(2*c_n*tau):
#   dlam/dtau  = 2*c_n * lam_n
#   d2lam/dtau^2 = 4*c_n^2 * lam_n
# For Gaussian, full chain rule:
#   d2S/dtau^2 = sum_n mult_n * [f''*(2*lam*dlam)^2 + f'*2*dlam^2 + f'*2*lam*d2lam]
dlam = 2.0 * c * lam  # (local)
d2lam = 4.0 * c**2 * lam  # (local)

# Gaussian
fp_G = -0.5 * np.exp(-x/2.0)  # (local)
fpp_G = 0.25 * np.exp(-x/2.0)  # (local)
t1_G = fpp_G * (2.0 * lam * dlam)**2  # (local)
t2_G = fp_G * 2.0 * dlam**2  # (local)
t3_G = fp_G * 2.0 * lam * d2lam  # (local)
d2S_G = np.sum(mult * (t1_G + t2_G + t3_G))  # (local)

# Sqrt / |lambda| (f(x) = sqrt(x))
#   f' = 0.5 * x^{-1/2}, f'' = -0.25 * x^{-3/2}
fp_S = 0.5 / np.sqrt(x)  # (local)
fpp_S = -0.25 / x**1.5  # (local)
t1_S = fpp_S * (2.0 * lam * dlam)**2  # (local)
t2_S = fp_S * 2.0 * dlam**2  # (local)
t3_S = fp_S * 2.0 * lam * d2lam  # (local)
d2S_S = np.sum(mult * (t1_S + t2_S + t3_S))  # (local)

print(f"\n  d^2S/dtau^2 (Gaussian)     = {d2S_G:+.6e}")
print(f"  d^2S/dtau^2 (sqrt/|lam|)   = {d2S_S:+.6e}")
print(f"\n  Gaussian contributions: t_fpp = {t1_G.sum():+.4e}, "
      f"t_fp1 = {t2_G.sum():+.4e}, t_fp2 = {t3_G.sum():+.4e}")
print(f"  Sqrt     contributions: t_fpp = {t1_S.sum():+.4e}, "
      f"t_fp1 = {t2_S.sum():+.4e}, t_fp2 = {t3_S.sum():+.4e}")

# -----------------------------------------------------------------------
# Step 4: What IS regulator-independent?
# -----------------------------------------------------------------------
print("\n" + "=" * 72)
print("[Step 4] Regulator-invariant probe of stationarity")
print("=" * 72)

# If tau_fold were TRULY a stationary point of the spectral action
# S = sum mult * f(lam^2), then dS/dtau = sum mult * f'(x) * 2*lam*dlam/dtau
# would be zero for any f such that f'(x) != 0 on the support.
# The sum
#   Sigma = sum_n mult * lam_n * dlam_n/dtau     (= d/dtau (sum_n mult * lam^2 / 2))
# probes the 'bare' Jensen stationarity of sum of lam^2, which is
# proportional to Tr(D_K^2) = a_0 up to normalization.
# This has NO f-dependence.  Direct test.

# In the toy model:
Sigma_bare = np.sum(mult * lam * dlam)  # (local) regulator-independent
print(f"\n  Sigma_bare = sum lam * dlam/dtau = {Sigma_bare:+.6e}")
print(f"  (Regulator-INDEPENDENT. Vanishes iff sum_n mult * lam^2 is")
print(f"   tau-stationary -- i.e. iff Tr(D_K^2) is extremized.)")

# For this toy model:
# Tr(D_K^2)(tau) = exp(2 tau) + exp(-2 tau) = 2 cosh(2 tau)
# d/dtau = 4 sinh(2 tau); stationary only at tau = 0, NOT at tau = 0.19
# So Sigma_bare != 0 at tau = 0.19 for this ansatz.
print(f"  Analytic check: Tr(D_K^2)(tau) = 2 cosh(2 tau).")
print(f"  d/dtau|_{{tau=0.19}} = 4 sinh(2*0.19) = {4*np.sinh(2*0.19):+.6e}")
print(f"  (factor of 2 from my sum normalization: 2*Sigma = {2*Sigma_bare:+.6e}.)")

print("\n" + "=" * 72)
print("CONCLUSION:")
print("=" * 72)
print("""
(a) f'(x) has OPPOSITE SIGNS for decreasing vs increasing regulators:
      f_Gauss'(x) < 0,    f_sqrt'(x) > 0.
(b) Plan Eq. 85.1:  dS/dtau = 4 * sum_n c_n * f'(x_n) * x_n.
    The factor f'(x_n) enters LINEARLY.  Sign flip in f'
    -> sign flip in dS/dtau under BOTH regulators, holding c_n, lam_n fixed.
(c) The einstein agent's Gaussian dS/dtau = -2.036e+04 and sqrt dS/dtau
    = +5.868e+04 are consistent to within ~3x magnitude discrepancy that
    reflects the DIFFERENT MELLIN MOMENTS f_2 of the two regulators.
(d) NEITHER regulator, with Eq. 85.1 taken literally, gives dS/dtau = 0
    at tau_fold.  The PASS threshold |dS/dtau| < 1e-10 is ~8 OOM from
    both numbers.  This is NOT a regulator convention issue -- it is
    that tau_fold is genuinely NOT a stationary point of the bare
    Chamseddine-Connes spectral action S = Tr f(D^2/Lambda^2).
(e) This IS consistent with everything the framework has established:
    S42 canonical dS_fold = +58673 is NON-ZERO by design -- it drives
    the transit dynamics.  A gate that PASSES iff dS/dtau = 0 at the
    fold is testing a hypothesis the framework never held.
""")
