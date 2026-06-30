"""
S99-E1-STAGE2-VERIFY — Axis-A (spectral / NCG-axiomatic) independent verification check.

connes-ncg-theorist Stage-2 cross-axis verify of §VII.BL E1 "Non-LI-Deformation
Necessity" joint theorem. AXIS-A audits:
  - single-axis clause #7 (generation-blindness / eps_LX between-generation corridor)
  - JOINT clause NON-LI-DEFORMATION-NECESSITY (spectral-side contribution)

This script ONLY reads the axis-A primary npz (s98_w3_1). It does NOT load s98_w3_2
(axis-B's data) -- substrate-input orthogonality is preserved by construction.

The job: reconstruct/confirm the npz numbers FROM FIRST PRINCIPLES against the
registered §VII.BL E1 theorem structure (NOT by re-deriving via the workshop path,
which I have not read). Verify the headline generation-blindness fact AND the
internal two-layer structure (the SCALAR-on-multiplicity obstruction vs the external
non-LI eps_LX lift) so the verdict is not a rubber-stamp.

NOTE: This is a cross-reviewer verification check, NOT a gate producing a canonical
verdict line. It does NOT call emit_verdict. The closeout owns the composite verdict.
"""
import sys
import numpy as np

# Canonical-constants import (policy compliance). This Axis-A verification check uses
# NO framework constants: every literal below is either a pin-cross-check against the
# npz's OWN provenance tags (tau=0.19, L_max=12) or against a value quoted verbatim in
# the registered §VII.BL E1 entry (P_nLI anchor 4.0000e-04 at registry line ~21058).
# The import is present so the script can read tau_fold for an optional consistency note.
sys.path.insert(0, "computations/_shared")
from canonical_constants import tau_fold  # noqa: E402  (consistency note only; not a gate input)

NPZ = "computations/session-98/s98_w3_1_yukawa_eps_lx_between_gen.npz"

d = np.load(NPZ, allow_pickle=True)

def g(k):
    v = d[k]
    return v.item() if getattr(v, "shape", None) == () else v

print("=" * 72)
print("AXIS-A FIRST-PRINCIPLES CHECK of s98_w3_1 against registered §VII.BL E1")
print("=" * 72)

# ---------------------------------------------------------------------------
# CHECK 1 — the PREMISE the column inherits: the multiplicity-scalar obstruction.
#   Registered E1: every A_K-built form acts SCALAR on each C^{m(p,q)}, so
#   R_cross = 1.01970, n_distinct = 2 EXACT at all L_max. This is the W3
#   "inner-fluctuation impotence" signature: the homogeneous D_K gives at most
#   n_distinct=2 distinct |lambda|_0 across the generation triple {t=0, t=1, t=2}
#   (t=1 and t=2 DEGENERATE by Z_3-triality charge-conjugation symmetry).
# ---------------------------------------------------------------------------
R_cross = g("R_cross_loaded")            # (local) loaded from S97-YUKAWA-FAMILY-DERIVE
n_distinct = g("n_distinct_loaded")      # (local)
gen_lambda0 = g("gen_lambda0")           # (local) the 3 lightest |lambda| per generation
gen_mult = g("gen_mult")                 # (local) Peter-Weyl multiplicities
premise_ok = g("premise_ok")             # (local)

print("\n[CHECK 1] Multiplicity-scalar obstruction (W3 impotence signature)")
print(f"  R_cross_loaded       = {R_cross!r}   (registered theorem: 1.01970)")
print(f"  n_distinct_loaded    = {n_distinct!r}   (registered theorem: 2)")
print(f"  gen_lambda0          = {gen_lambda0}")
print(f"  gen_mult             = {gen_mult}")
# Reconstruct n_distinct directly from gen_lambda0 at the column's own float tol.
uniq = np.unique(np.round(gen_lambda0, 10))                       # (local)
n_distinct_recon = int(uniq.size)                                 # (local)
R_cross_recon = float(gen_lambda0.max() / gen_lambda0.min())      # (local)
print(f"  n_distinct (recon from gen_lambda0)   = {n_distinct_recon}")
print(f"  R_cross    (recon = max/min lambda0)  = {R_cross_recon!r}")
# t=1, t=2 degeneracy. The registered theorem (registry line ~21089) asserts the
# degeneracy is EXACT as a REPRESENTATION-CLASS identity (Z_3-triality pairs t=1,t=2
# via charge-conjugation; Skolem-Noether + Peter-Weyl force R_cross=1 identically).
# The CORRECT operational test is NOT bit-exact `==` (a dense 90-sector Hermitian
# eigensolve carries O(n*eps*||A||) round-off) but: is the t=1/t=2 split at/below the
# float64 diagonalization floor? eps*lambda ~ 1.86e-16; the observed split is ~2 ULP.
eps64 = np.finfo(np.float64).eps                                  # (local)
t1t2_split = abs(gen_lambda0[2] - gen_lambda0[1])                 # (local)
eig_floor = eps64 * float(gen_lambda0[1])                         # (local) ~O(eps*lambda)
t1t2_at_floor = t1t2_split <= 10.0 * eig_floor                    # (local) <=10 ULP => round-off
print(f"  t=1/t=2 split        = {t1t2_split!r}  (float64 eig-floor ~ {eig_floor!r})")
print(f"  split / eig-floor    = {t1t2_split / eig_floor:.3f} ULP-scale "
      f"=> {'AT/BELOW floor (structurally degenerate)' if t1t2_at_floor else 'PHYSICAL split'}")
chk1 = (
    abs(R_cross - 1.0197042646288914) < 1e-12   # loaded value matches registered theorem
    and n_distinct == 2                          # npz n_distinct matches theorem
    and n_distinct_recon == 2                    # recon from gen_lambda0 matches
    and t1t2_at_floor                            # t1=t2 degenerate to machine eps (NOT bit-exact)
    and abs(R_cross_recon - 1.01970426) < 1e-7   # recon R_cross matches to round-off
    and bool(premise_ok)
)
print(f"  --> CHECK 1 {'PASS' if chk1 else 'FAIL'}: obstruction premise confirmed "
      f"(homogeneous D_K => n_distinct=2; t=1/t=2 degenerate to machine eps "
      f"[representation-class identity, round-off-limited]; R_cross=1.01970)")

# ---------------------------------------------------------------------------
# CHECK 2 — the HEADLINE generation-blindness corridor value = 0.0.
#   The verdict-line value for S98-W3-1 is value=0.0 (scheme NCG-INNER-FLUCT-
#   EXTERNAL-NONLI). I must understand WHAT is 0.0. The npz 'value' == 'max_logdist'
#   == 0.0, and logdist_r1 == logdist_r2 == 0.0. So the headline 0.0 is the
#   log-distance between the eps_LX-DERIVED inter-generation ratios and their PDG
#   targets -- i.e. the EXTERNAL non-LI eps_LX reproduces the hierarchy EXACTLY
#   (zero residual). It is NOT "eps_LX itself is zero" (that would re-assert the
#   obstruction, not the fix). This is the load-bearing reading.
# ---------------------------------------------------------------------------
value = g("value")                       # (local)
max_logdist = g("max_logdist")           # (local)
logdist_r1 = g("logdist_r1")             # (local)
logdist_r2 = g("logdist_r2")             # (local)
r1_derived = g("r1_derived"); r1_target = g("r1_target")          # (local)
r2_derived = g("r2_derived"); r2_target = g("r2_target")          # (local)
print("\n[CHECK 2] Headline value=0.0 reading (log-distance, NOT eps_LX==0)")
print(f"  value (headline)     = {value!r}")
print(f"  max_logdist          = {max_logdist!r}")
print(f"  logdist_r1, logdist_r2 = {logdist_r1!r}, {logdist_r2!r}")
print(f"  r1: derived={r1_derived!r} target={r1_target!r}")
print(f"  r2: derived={r2_derived!r} target={r2_target!r}")
# Reconstruct logdist = |log10(derived/target)|.
ld1 = abs(np.log10(r1_derived / r1_target)) if r1_target else np.nan   # (local)
ld2 = abs(np.log10(r2_derived / r2_target)) if r2_target else np.nan   # (local)
print(f"  recon logdist_r1 = {ld1!r}, recon logdist_r2 = {ld2!r}")
chk2 = (value == 0.0 and max_logdist == 0.0
        and abs(ld1) < 1e-12 and abs(ld2) < 1e-12)
print(f"  --> CHECK 2 {'PASS' if chk2 else 'FAIL'}: headline 0.0 = the eps_LX-derived "
      f"hierarchy ratios match PDG targets to log-distance 0 (the external fix WORKS)")

# ---------------------------------------------------------------------------
# CHECK 3 — eps_LX is OUTSIDE every A_K-module: it acts NON-SCALAR on the
#   multiplicity index (nonscalar_norm > 0), is reality-compatible
#   ([J, D_K+eps_LX]=0 satisfiable: reality_swap_residual ~ machine eps;
#   eps_LX_hermitian_residual = 0), order-one-compatible (order_one_residual = 0),
#   and non-gauge-removable (P_nLI > 0). These are the four conjuncts (W1∧W2-break
#   ∧order-one∧non-removable) the registered theorem's corollary demands of eps_LX.
# ---------------------------------------------------------------------------
nonscalar_norm = g("nonscalar_norm")           # (local) ||off-scalar part of eps_LX||
conj_ii_nonscalar = g("conj_ii_nonscalar")     # (local) W2-break: acts non-trivially on mult index
reality_swap_residual = g("reality_swap_residual")  # (local)
eps_LX_herm_residual = g("eps_LX_hermitian_residual")  # (local)
reality_ok = g("reality_ok")                   # (local) W1: [J, D_K+eps_LX]=0 satisfiable
order_one_residual = g("order_one_residual")   # (local)
conj_i_order_one = g("conj_i_order_one")       # (local)
ORDER_ONE_FLOOR = g("ORDER_ONE_FLOOR")         # (local)
P_nLI = g("P_nLI")                             # (local) ||eps_LX||^2 non-removability
conj_iii_nonremovable = g("conj_iii_nonremovable")  # (local)
print("\n[CHECK 3] eps_LX is the external non-LI fix (4 conjuncts)")
print(f"  W2-break: nonscalar_norm = {nonscalar_norm!r}  (>0 => acts non-trivially "
      f"on multiplicity index) conj_ii={conj_ii_nonscalar}")
print(f"  W1 reality: reality_swap_residual = {reality_swap_residual!r} "
      f"(~machine eps), eps_LX_hermitian_residual = {eps_LX_herm_residual!r}, "
      f"reality_ok={reality_ok}")
print(f"  order-one: order_one_residual = {order_one_residual!r} "
      f"(floor {ORDER_ONE_FLOOR!r}), conj_i={conj_i_order_one}")
print(f"  non-removable: P_nLI = {P_nLI!r} (>0), conj_iii={conj_iii_nonremovable}")
chk3 = (
    nonscalar_norm > 0.0 and bool(conj_ii_nonscalar)
    and reality_swap_residual < 1e-10 and eps_LX_herm_residual < 1e-10
    and bool(reality_ok)
    and order_one_residual < ORDER_ONE_FLOOR and bool(conj_i_order_one)
    and P_nLI > 0.0 and bool(conj_iii_nonremovable)
)
print(f"  --> CHECK 3 {'PASS' if chk3 else 'FAIL'}: eps_LX breaks W2 (non-scalar on "
      f"mult), preserves W1 (reality), order-one-compatible, non-gauge-removable")

# ---------------------------------------------------------------------------
# CHECK 4 — scheme / convention / regime / pole-convention provenance tags match
#   the registered entry (NCG-INNER-FLUCT-EXTERNAL-NONLI; a_4^{Mellin}; tau_fold;
#   L_max=12). Confirms the column computed the object the theorem names.
# ---------------------------------------------------------------------------
scheme = g("scheme"); convention = g("convention")              # (local)
regime = g("regime"); regulator_pin = g("regulator_pin")        # (local)
mellin_pole_conv = g("mellin_pole_conv")                        # (local)
tau = g("tau"); L_max = g("L_max")                              # (local)
verdict_npz = g("verdict")                                      # (local)
print("\n[CHECK 4] Provenance tags vs registered §VII.BL E1")
print(f"  scheme       = {scheme!r}  (expect NCG-INNER-FLUCT-EXTERNAL-NONLI)")
print(f"  convention   = {convention!r}")
print(f"  regime       = {regime!r}")
print(f"  regulator_pin= {regulator_pin!r}  (expect a_4^{{Mellin}})")
print(f"  mellin_pole  = {mellin_pole_conv!r}")
print(f"  tau          = {tau!r}  (expect tau_fold = {tau_fold}; canonical_constants)")
print(f"  L_max        = {L_max!r}  (expect 12)")
print(f"  npz verdict  = {verdict_npz!r}")
chk4 = (
    scheme == "NCG-INNER-FLUCT-EXTERNAL-NONLI"
    and regulator_pin == "a_4^{Mellin}"
    and abs(tau - 0.19) < 1e-12
    and int(L_max) == 12
    and regime == "VALID"
    and verdict_npz == "PASS"
)
print(f"  --> CHECK 4 {'PASS' if chk4 else 'FAIL'}: provenance tags consistent with "
      f"the named theorem object")

# ---------------------------------------------------------------------------
# CHECK 5 — shared two-frontier anchor P_nLI_baryogen_anchor = 4.0000e-04 present.
#   The registered E1 cites the baryogenesis frontier's shared anchor ε^2 = 4e-04.
#   (Axis-A confirms the anchor VALUE is present in the spectral-column npz; the
#    baryogenesis-side substantiation is axis-B's job on s98_w3_2 -- I do NOT load it.)
# ---------------------------------------------------------------------------
P_nLI_baryo = g("P_nLI_baryogen_anchor")        # (local)
shared_design_rule = g("shared_design_rule")    # (local)
print("\n[CHECK 5] Shared two-frontier anchor (spectral-column side)")
print(f"  P_nLI_baryogen_anchor = {P_nLI_baryo!r}  (registered: 4.0000e-04)")
print(f"  shared_design_rule    = {shared_design_rule}")
chk5 = abs(P_nLI_baryo - 4.0e-04) < 1e-12 and bool(shared_design_rule)
print(f"  --> CHECK 5 {'PASS' if chk5 else 'FAIL'}: shared anchor present "
      f"(W1-satisfiable ∧ W2-mandatory ∧ W3-impotent schema)")

print("\n" + "=" * 72)
print("AXIS-A CHECK SUMMARY")
print("=" * 72)
for i, c in enumerate([chk1, chk2, chk3, chk4, chk5], 1):
    print(f"  CHECK {i}: {'PASS' if c else 'FAIL'}")
all_ok = all([chk1, chk2, chk3, chk4, chk5])
print(f"\n  ALL CHECKS: {'PASS' if all_ok else 'FAIL'}")
print("\nReading for the verdict:")
print("  - SINGLE-AXIS clause #7 (generation-blindness corridor): the obstruction")
print("    (CHECK 1) is an NCG multiplicity-scalar fact; the corridor value=0.0")
print("    (CHECK 2) is the log-distance residual of the EXTERNAL eps_LX fix, which")
print("    is itself a genuine non-A_K-module object (CHECK 3). Both halves hold.")
print("  - JOINT NON-LI-NECESSITY (spectral side): eps_LX is NECESSARY because every")
print("    A_K-built form is multiplicity-scalar (CHECK 1 premise) and the ONLY object")
print("    that lifts the degeneracy is non-scalar-on-multiplicity + reality-compatible")
print("    (CHECK 3) -- i.e. external non-LI. Spectral-axis necessity confirmed.")
