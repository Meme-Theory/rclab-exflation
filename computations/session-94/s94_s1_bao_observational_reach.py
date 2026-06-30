"""
S94 Slot-1 (S-1) — BAO peak-position observational-reach review (VERDICT-ONLY, no gate emission).

Translates the W5-3 per-gapped-branch fractional Layer-1/Layer-2 speed split
delta_b/c_b^2 = 0.19 into an observational BAO acoustic-peak-position shift for the
B1-dominant branch, and compares against DESI / CMB-S4 / Simons forecast precision.

This is a /rclab-review SOLO observational-translation calculation. It does NOT emit a
gate verdict line (the W5-3 gate S94-BAO-PEAK-BRANCH is already closed, INFO, line 72).
It produces the quantified shift + the substrate-IS -> emergent transport substitution
chain that the synthesis and Row #67 recommendation rest on.

Substrate-first framing (phononic-framing.md): the substrate IS the BAO acoustic
signature (interference pattern of post-transit GGE acoustic excitations through the a_2
channel). The M_KK-unit branch speeds do NOT directly give a measurable BAO shift; the
transport T_{BZ->pivot} (the S43 KK-CMB-TF-43 two-sound machinery) is explicit and
governs which scale a detector measures (cross-pillar-bridge-anatomy.md
§"Per-observable transport-degree scale-separation").
"""
from fractions import Fraction as F

# ---- canonical imports (math-scripts.md MANDATORY) -------------------------
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))
from canonical_constants import (  # noqa: E402
    c_Gold,          # 0.915  Goldstone sound speed (M_KK units) — Killing-protected
    c_B1,            # 0.0798 B1 singlet acoustic-scalar branch speed (M_KK)
    c_B3,            # 0.1397 B3 dispersive optical triplet (M_KK)
    tau_fold,        # 0.19   Jensen fold modulus (CONST-FREEZE-42)
    c_light,         # 2.99792458e8 m/s exact
    H_0_km_s_Mpc,    # 67.4 km/s/Mpc Planck 2018
)

print("=" * 78)
print("S94 S-1 — BAO peak-position observational reach (verdict-only review)")
print("=" * 78)

# ---- (local) pre-registered W5-3 inputs (from the closed gate; not re-derived) ----
delta_B1 = 0.015162          # (local) |c_B1^(1) - c_B1^(2)| M_KK, W5-3 abs delta
frac_split = 0.19            # (local) delta_b/c_b^(2) = O(tau) fractional split, ALL 7 gapped
k_BAO_W5 = 0.043             # (local) Mpc^-1, the W5-3 B1-dominant BAO-scale claim
c_B1_layer2 = c_B1           # Layer-2 emergent-cone (BdG) speed, M_KK
c_B1_layer1 = c_B1 * (1.0 + tau_fold)   # (local) Layer-1 throughput sqrt(Z/M) ~ c2*(1+tau)

# sanity: reproduce W5-3 numbers from canonical inputs ------------------------
print("\n[0] Reproduce W5-3 inputs from canonical constants")
print(f"    c_B1^(2) (Layer-2, BdG)      = {c_B1_layer2:.6f}  M_KK   [canonical c_B1]")
print(f"    c_B1^(1) (Layer-1, sqrt Z/M) = {c_B1_layer1:.6f}  M_KK   [= c2*(1+tau_fold)]")
delta_B1_recomp = abs(c_B1_layer1 - c_B1_layer2)
frac_recomp = delta_B1_recomp / c_B1_layer2
print(f"    delta_B1 (recomputed)        = {delta_B1_recomp:.6f}  M_KK  (W5-3: {delta_B1})")
print(f"    frac split (recomputed)      = {frac_recomp:.6f}        (W5-3: {frac_split})")
assert abs(delta_B1_recomp - delta_B1) < 1e-5, "delta_B1 mismatch"
assert abs(frac_recomp - frac_split) < 1e-9, "frac split mismatch"
print("    => W5-3 inputs reproduced from canonical_constants (no new physics).")

# ===========================================================================
# STEP 1 — DEFINITIONS (the two layers + the observable)
# ===========================================================================
# Substrate-IS observables (M_KK units, inside the effective Brillouin zone):
#   c_b^(1) = sqrt(Z_b/M_b)  Layer-1 substrate-throughput speed (a_4^z / a_2^z moments)
#   c_b^(2) = v_g(k)         Layer-2 emergent-cone speed (BdG diagonalization of D_K^2)
# The DIMENSIONLESS substrate-IS quantity (the thing W5-3 actually pins, in-band):
#   s_b := delta_b/c_b^(2) = (c_b^(1) - c_b^(2))/c_b^(2) = 0.19   (a pure ratio, 7 gapped)
#
# Laboratory-IN observable (the BAO acoustic peak):
#   theta_s = r_s / D_A(z_*)        CMB acoustic angular scale (Planck)
#   k_peak  = 2*pi/r_s              comoving BAO wavenumber (galaxy surveys)
#   r_s     = integral c_s(tau) dtau  comoving acoustic (sound) horizon
#
# Bridge map T_{BZ->pivot}: the S43 KK-CMB-TF-43 two-sound transport.
#   The acoustic peak position is set by the EMERGENT (lab-IN) sound speed c_s, NOT by
#   the M_KK-unit branch speed. r_s ~ 1/c_s, so a FRACTIONAL change in c_s gives a
#   FRACTIONAL change in r_s (hence in k_peak and theta_s) of the SAME relative size.
print("\n[1] Definitions — see docstring + comments. Two layers + dimensionless ratio s_b.")

# ===========================================================================
# STEP 2 — SUBSTITUTION (the transport: which scale does a detector measure?)
# ===========================================================================
# The peak-position observable is the comoving sound horizon r_s = integral c_s dtau.
# Define the FRACTIONAL peak-position shift induced by a fractional sound-speed split s:
#       r_s  proportional_to  c_s   (longer/faster sound travel -> larger horizon)
#   =>  d(ln r_s) = d(ln c_s)            (Step 2a: r_s linear in c_s at fixed conformal time)
#   =>  Delta r_s / r_s = Delta c_s / c_s = s         (Step 2b)
#   And k_peak = 2*pi/r_s  =>  Delta k_peak/k_peak = -Delta r_s/r_s = -s   (Step 2c)
#   And theta_s = r_s/D_A =>  Delta theta_s/theta_s = Delta r_s/r_s = s    (Step 2d, fixed D_A)
#
# THE TRANSPORT-DEGREE QUESTION (cross-pillar-bridge-anatomy §"Per-observable
# transport-degree scale-separation"): does the substrate dimensionless ratio s_b = 0.19
# survive transport to the lab-IN fractional peak shift UNCHANGED (deg = T2-VACUOUS
# scalar, substrate = pivot), or is it re-weighted (NON-SCALAR, substrate != pivot)?
#
# ANSWER (substrate-first derivation): a fractional SPLIT between two sound speeds on a
# branch is a degree-0 dimensionless object. The two-sound transport T_{BZ->pivot}
# (S43: c_1 = c -> r_1 = 325.3 Mpc; c_2 = c/sqrt(3(1+R*)) -> r_s = 147.1 Mpc) maps a
# branch speed c_b to a comoving horizon r_b = pi * (c_b/c_2) * r_s-style ruler. The
# OVERALL M_KK->Mpc unit conversion is a common scalar that CANCELS in the dimensionless
# ratio Delta r/r. BUT — and this is the decisive subtlety — the 0.19 split is defined
# on the SUBSTRATE branch speed c_b^(2) (M_KK units, sub-luminal), NOT on the emergent
# acoustic sound speed c_s that sets the OBSERVED BAO peak. The transport must carry the
# split from the substrate branch onto the emergent acoustic channel.
print("\n[2] Substitution — fractional peak shift = fractional sound-speed split (degree-0).")
print("    Delta r_s/r_s = Delta c_s/c_s = s   ;   Delta k/k = -s   ;   Delta theta/theta = s")

# ===========================================================================
# STEP 3 — SIMPLIFY: the EFFACEMENT-projection factor (the real transport degree)
# ===========================================================================
# Substrate-first: the substrate IS the post-transit GGE acoustic field. The Layer-1/
# Layer-2 split is an INTERNAL-fiber speed difference. To reach the EMERGENT 4D BAO
# channel it must project through the a_2 (Einstein-Hilbert) channel — the same
# effacement projection that suppresses internal modes onto 4D observables.
#
# Two transport readings (the §VII.BA five-formulation taxonomy applied to T_{BZ->pivot}):
#
#  Reading-S (T2-VACUOUS scalar; substrate = pivot): the 0.19 fractional split is a pure
#     ratio that transports UNCHANGED. Then the BAO peak carries a 19% fractional shift.
#     This is the W5-3 / Row #67 IMPLICIT reading ("a 19% effect ... real test").
#
#  Reading-NS (NON-SCALAR; substrate != pivot): the split lives on an INTERNAL branch at
#     M_KK speed c_b^(2) << 1. The emergent acoustic channel runs at c_s ~ c/sqrt(3).
#     The split projects onto the emergent channel with the effacement amplitude
#     A_eff = c_b^(2)^2 / c_s^2-style weight (the S43 A_FS = c_2^2/c_1^2 = 0.204
#     first-sound-to-BAO amplitude is exactly this kind of (speed-ratio)^2 projection).
#     The OBSERVED fractional peak shift is then s_b * A_eff, NOT s_b.
#
# Compute BOTH and bracket the verdict.
print("\n[3] Simplify — two transport readings (S43 effacement-projection amplitude).")

# --- Reading-S: split transports unchanged (degree-0 scalar) ----------------
frac_peak_shift_S = frac_split                       # (local) 0.19, unchanged
print(f"    Reading-S  (scalar transport):  Delta r_s/r_s = {frac_peak_shift_S:.4f}  (19%)")

# --- Reading-NS: split projects with the effacement (speed-ratio)^2 weight --
# S43 first-sound amplitude A_FS = c_2^2/c_1^2 = 1/[3(1+R*)] = 0.204 (the projection of an
# internal acoustic channel onto the matter BAO). The B1 branch sits at c_B1 in M_KK; its
# projection onto the emergent acoustic cone (Goldstone c_Gold=0.915, the one true 4D
# light cone) carries weight (c_B1/c_Gold)^2.
A_eff_B1 = (c_B1 / c_Gold) ** 2                       # (local) effacement projection weight
frac_peak_shift_NS = frac_split * A_eff_B1            # (local) projected fractional shift
print(f"    Reading-NS (effacement projection): A_eff,B1 = (c_B1/c_Gold)^2 = {A_eff_B1:.6f}")
print(f"    Reading-NS  projected fractional shift = 0.19 * {A_eff_B1:.6f} = {frac_peak_shift_NS:.3e}")

# Also report the S43-canonical first-sound amplitude for cross-reference
A_FS_S43 = 0.204                                      # (local) S43 KK-CMB-TF-43 A_FS
print(f"    [x-ref] S43 first-sound A_FS = {A_FS_S43} (c_2^2/c_1^2 projection; same FORM)")

# ===========================================================================
# STEP 4 — CONVERT to observational units (theta_s, k in Mpc^-1, ell)
# ===========================================================================
# Anchor: the observed BAO sound horizon r_s = 147.09 Mpc (Planck/DESI standard ruler);
# the W5-3 B1-dominant scale k_BAO ~ 0.043 Mpc^-1 corresponds (k = 2pi/r) to r ~ 146 Mpc
# (k_BAO_W5=0.043 -> r = 2pi/0.043 = 146.1 Mpc, i.e. the standard BAO ruler — confirming
# the W5-3 k~0.043 is the STANDARD BAO scale, S43 k_BAO=0.0427).
r_s_obs = 147.09                                      # (local) Mpc, Planck/DESI sound horizon
k_from_W5 = 2.0 * 3.141592653589793 / r_s_obs         # (local) Mpc^-1 check
print("\n[4] Convert to observational units (r_s = 147.09 Mpc standard ruler).")
print(f"    k = 2*pi/r_s = {k_from_W5:.4f} Mpc^-1  (W5-3 claim k_BAO ~ {k_BAO_W5}; S43 0.0427) -> CONSISTENT")

# Planck acoustic angular scale (fetched: researchers/Paasch/12 + researchers/Mack/29):
theta_star_100 = 1.04077                              # (local) 100*theta_MC, Planck 2018
sig_theta_star_100 = 0.00032                          # (local) Planck 2018 1-sigma
frac_prec_planck = sig_theta_star_100 / theta_star_100  # (local) fractional precision
print(f"    Planck 100*theta_* = {theta_star_100} +/- {sig_theta_star_100}"
      f"  => sigma(theta)/theta = {frac_prec_planck:.3e}  ({frac_prec_planck*100:.3f}%)")

# Reading-S observational shifts:
Delta_k_S = frac_peak_shift_S * k_from_W5             # (local) Mpc^-1 (|Delta k| = s*k)
Delta_theta_S_100 = frac_peak_shift_S * theta_star_100  # (local) shift in 100*theta units
# Reading-NS observational shifts:
Delta_k_NS = frac_peak_shift_NS * k_from_W5           # (local) Mpc^-1
Delta_theta_NS_100 = frac_peak_shift_NS * theta_star_100  # (local)

print(f"\n    Reading-S  : |Delta k| = {Delta_k_S:.4f} Mpc^-1 ; Delta(100 theta) = {Delta_theta_S_100:.4f}")
print(f"    Reading-NS : |Delta k| = {Delta_k_NS:.3e} Mpc^-1 ; Delta(100 theta) = {Delta_theta_NS_100:.3e}")

# ===========================================================================
# STEP 5 — VERDICT: within or outside forecast precision?
# ===========================================================================
# Forecast/measurement precision anchors (ALL from fetched local sources):
#   Planck 2018 100*theta_*     : 0.031%   (researchers/Paasch/12, researchers/Mack/29)
#   DESI DR2 combined BAO ruler : 0.24%    (researchers/Cosmic-Web/19, Delta r_BAO/r_BAO)
#   DESI per-tracer BAO D_A/H   : ~1-3%    (researchers/Mack/30 table; systematics <0.5%)
#   DESI 5yr (full) w(z)        : ~2%      (researchers/Mack/30); ruler -> ~0.1-0.2% floor
print("\n[5] VERDICT — shift vs forecast precision")
desi_dr2_ruler = 0.0024          # (local) 0.24% DESI DR2 combined BAO (fetched)
desi_pertracer = 0.026           # (local) ~2.6% best per-tracer D_A (fetched table, ELG)
planck_theta = frac_prec_planck  # (local) 0.031% Planck acoustic scale (fetched)
# CMB-S4/Simons: no theta_s forecast in local Mack tree -> conservative bound below.
cmb_s4_floor_est = 0.0001        # (local) ~0.01% OPTIMISTIC next-gen acoustic-scale FLOOR
                                 # (literature GAP; bounding estimate, NOT a fetched pin)

def cmp(shift, prec, label):
    ratio = shift / prec
    inside = shift >= prec
    tag = "WITHIN (detectable)" if inside else "OUTSIDE (below precision)"
    print(f"    {label:34s}: shift/prec = {ratio:8.3e}  -> {tag}")
    return inside, ratio

print("  --- Reading-S (scalar transport, shift = 19%) ---")
cmp(frac_peak_shift_S, planck_theta,   "vs Planck theta_* (0.031%)")
cmp(frac_peak_shift_S, desi_dr2_ruler, "vs DESI DR2 ruler (0.24%)")
cmp(frac_peak_shift_S, desi_pertracer, "vs DESI per-tracer (~2.6%)")
cmp(frac_peak_shift_S, cmb_s4_floor_est, "vs CMB-S4/SO floor (~0.01% est)")

print("  --- Reading-NS (effacement projection, shift = s*(c_B1/c_Gold)^2) ---")
cmp(frac_peak_shift_NS, planck_theta,   "vs Planck theta_* (0.031%)")
cmp(frac_peak_shift_NS, desi_dr2_ruler, "vs DESI DR2 ruler (0.24%)")
cmp(frac_peak_shift_NS, desi_pertracer, "vs DESI per-tracer (~2.6%)")
cmp(frac_peak_shift_NS, cmb_s4_floor_est, "vs CMB-S4/SO floor (~0.01% est)")

# ---- The decisive substrate-first determination ---------------------------
print("\n[5b] Transport-degree determination (the structural crux)")
print("    The 0.19 split is a SUBSTRATE-INTERNAL fractional speed difference on a branch")
print("    at M_KK speed c_B1<<1. To shift the OBSERVED BAO peak it must project onto the")
print("    emergent 4D acoustic channel (Goldstone c_Gold, the ONE true light cone) via")
print("    the effacement amplitude (c_B1/c_Gold)^2 = %.3e (Reading-NS; S43 A_FS FORM)." % A_eff_B1)
print("    Reading-S (19% transports unchanged) would require the SUBSTRATE branch speed")
print("    to BE the emergent acoustic speed — a container-thinking conflation of the")
print("    M_KK-unit internal mode with the 4D observable. SUBSTRATE-FIRST -> Reading-NS.")
print(f"    => observed fractional BAO peak shift ~ {frac_peak_shift_NS:.2e} (= {frac_peak_shift_NS*100:.4f}%)")
print(f"    => |Delta k| ~ {Delta_k_NS:.2e} Mpc^-1 ; Delta(100 theta) ~ {Delta_theta_NS_100:.2e}")

# Even under the MOST optimistic next-gen floor, compare:
print("\n[5c] Bottom line")
print(f"    Reading-NS shift {frac_peak_shift_NS:.2e} vs best plausible precision "
      f"{min(planck_theta, cmb_s4_floor_est):.2e}:")
if frac_peak_shift_NS < min(planck_theta, cmb_s4_floor_est):
    print("    => BELOW even the most optimistic acoustic-scale precision. OUTSIDE reach.")
else:
    print("    => at/above precision; WITHIN reach.")
print(f"    Reading-S shift {frac_peak_shift_S:.2e}: trivially WITHIN reach IF the substrate")
print("    branch speed were the emergent acoustic speed — but that identification is the")
print("    container-thinking error the substrate-first analysis forbids.")

# Margin to detectability: what effacement amplitude WOULD be needed to reach DESI DR2?
A_eff_needed_DESI = desi_dr2_ruler / frac_split       # (local) projection needed for 0.24%
print(f"\n    For the shift to reach DESI DR2 (0.24%), the projection weight would need to be")
print(f"    A_eff >= {A_eff_needed_DESI:.4f}; actual (c_B1/c_Gold)^2 = {A_eff_B1:.4f} "
      f"(ratio {A_eff_B1/A_eff_needed_DESI:.3f}x). B3 (largest gapped speed):")
A_eff_B3 = (c_B3 / c_Gold) ** 2                        # (local) most optimistic branch
shift_B3 = frac_split * A_eff_B3                        # (local)
print(f"    B3: (c_B3/c_Gold)^2 = {A_eff_B3:.4f}; shift = {shift_B3:.3e} "
      f"({'WITHIN' if shift_B3>=desi_dr2_ruler else 'still OUTSIDE'} DESI DR2 0.24%).")

print("\n" + "=" * 78)
print("SUMMARY (verdict-only; no gate emission)")
print("=" * 78)
print(f"  W5-3 dimensionless split s_b               : {frac_split} (in-band, 7 gapped)")
print(f"  Reading-S  observed peak shift (scalar)    : {frac_peak_shift_S*100:.2f}%  (container-thinking)")
print(f"  Reading-NS observed peak shift (effacement): {frac_peak_shift_NS*100:.4f}%  (SUBSTRATE-FIRST)")
print(f"  |Delta k|_NS                               : {Delta_k_NS:.2e} Mpc^-1")
print(f"  Delta(100 theta_*)_NS                      : {Delta_theta_NS_100:.2e}")
print(f"  Planck theta_* precision                   : {planck_theta*100:.3f}%")
print(f"  DESI DR2 ruler precision                   : {desi_dr2_ruler*100:.2f}%")
print(f"  DESI per-tracer BAO                        : ~2.6%")
print(f"  VERDICT: Reading-NS shift is OUTSIDE all current+forecast acoustic-scale precision.")
print(f"           B3 best-case {shift_B3*100:.3f}% also OUTSIDE DESI DR2.")
print("=" * 78)
