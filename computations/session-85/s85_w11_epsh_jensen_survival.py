"""
S85 W11-1 — EPSH-JENSEN-SURVIVAL
================================

Gate: S85-EPSH-JENSEN-SURVIVAL
Trigger: [VERIFY-THEOREM]
Classification: GEOMETRIC (Hopf-cyclic 1-cocycle stability under Jensen
                deformation of the transverse sector of the codim-1
                foliation of SU(3))

Question: Does the Heitsch 1-cocycle representative [eps_H] survive the
admissible Jensen range tau in [0, 0.4] with HP^1 norm strictly bounded
above 1e-4, extending the S83 W1-G2 tau_fold pointwise result to a
corridor-wide survival?

CANONICAL SETUP:
  - [eps_H] is represented by the S83 Dixmier-trace-proxy diagnostic
    heitsch_ratio(tau) = |d(cocycle)/dtau| / |cocycle(tau)|
    where cocycle(tau) = eps_H_rep * dixmier(tau) / n_modes(tau),
    dixmier(tau) = sum |lambda_n(tau)|^{-4},
    lambda_n = sqrt(C_2(p,q)) * exp(-tau*rho(p,q)),
    rho(p,q) = p + q.
  - Algebraic identity (epsilon_H and n_modes both cancel in the ratio
    since they factor identically into cocycle_plus and cocycle_minus):
        heitsch_ratio(tau) = 4 * <rho>_W(tau),
    where <rho>_W is the weighted average with weights
        W(p,q; tau) = 2*dim(p,q)/C_2(p,q)^2 * exp(4*tau*rho(p,q)).
  - This is the plan's "HP^1 norm" under the Jensen-deformed-omega_J
    convention (re-labeling of the S83 diagnostic, lines 78-82 of the
    plan's substitution chain).

L_MAX RECONCILIATION (plan pin vs anchor):
  Plan §W11-1 item 7 pins L_max = 10. Plan §9 anchor requires
  reproducing heitsch_ratio(tau_fold=0.19) = 16.197719 +/- 1e-3.
  Sage verification of the algebraic identity h_ratio = 4*<rho>_W at
  tau=0.19 gives:
    L_max=3  -> 9.067
    L_max=5  -> 16.197710  (matches anchor to 5 decimals)
    L_max=7  -> 24.179
    L_max=10 -> 36.345     (2.2x anchor)
  The anchor is DEFINITIONALLY an L_max=5 value. We run the primary
  scan at L_max=5 to preserve anchor reproducibility (source-material
  fidelity per CLAUDE.md "never conflate what the source material says
  with what the plan asserts"), and include L_max=10 as an INFO
  cross-check showing the survival direction is L_max-robust. The
  verdict 4-tuple records L_max=5 (actual). This is documented as a
  pre-registration reconciliation, not convention-shopping (no threshold
  is changed; only the label in the 4-tuple and the physical L used).

SUBSTITUTION CHAIN (plan §10, survival-direction claim):
  Def 1:  H(tau) = integral_F omega_J ^ d omega_J       [Heitsch cocycle]
  Def 2:  heitsch_ratio(tau) = H(tau) / ||bdry||_{HP^0} [S83 normalization]
  Def 3:  ||[eps_H](tau)||_{HP^1} := |heitsch_ratio(tau)|  [plan convention]
  Step 1: h(tau_fold=0.19) = 16.197719                   [S83 anchor]
  Step 2: omega_J(tau) smooth in tau                     [Jensen C^infty]
  Step 3: H(tau) smooth in tau                           [integral of smooth forms]
  Step 4: If H(tau*)=0 => [eps_H] exact at tau*, disjoint corridor breaks.
  Direction: PASS = |h(tau)| > 1e-4 on [0, 0.4].
             FAIL = |h(tau*)| < 1e-4 somewhere.
  Conclusion (structural): h(tau) = 4*<rho>_W, all W>0, all rho>=1.
             Therefore h(tau) >= 4 * min_rho = 4 * 1 = 4 for all tau >= 0,
             regardless of L_max. Hence the gate is structurally bounded
             above 4 >> 1e-4. PASS is guaranteed by the algebraic form
             alone. The MEASURED physical content of this gate is:
             (i) anchor reproduction, (ii) monotonicity sign of d h/dtau.

PASS/FAIL/INFO (plan §9):
  PASS: min_{tau in [0,0.4]} h(tau) > 1e-4 AND monotonicity resolved.
  FAIL: exists tau* with h(tau*) < 1e-4 (cannot occur per above proof).
  INFO: endpoint-derivative instability at tau=0 or tau=0.40 forces
        one-sided-stencil ambiguity at the boundary -- report where
        monotonicity IS resolved, defer endpoints.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, H_fold, S_fold, dS_fold, d2S_fold,
    M_KK, Vol_SU3_Haar, Delta_BCS, J_C2,
)

# -----------------------------------------------------------------------------
# SHA-256 input pinning
# -----------------------------------------------------------------------------

def sha256_of(obj):
    s = json.dumps(obj, sort_keys=True, default=str).encode()
    return hashlib.sha256(s).hexdigest()


def sha256_of_file(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception as e:
        return f"<unavailable:{e}>"


# Static file SHAs (input pins per plan §6)
S83_ANCHOR_NPZ = Path(__file__).parent / "s83_w1_g2_epsilon_h_promotion.npz"
CANON_CONSTANTS = Path(__file__).parent / "canonical_constants.py"

s83_anchor_sha = sha256_of_file(S83_ANCHOR_NPZ)
canon_sha = sha256_of_file(CANON_CONSTANTS)

# Gate-pinned machinery (plan §7 PRDR)
L_max = 5                       # (local) reconciled from plan's L_max=10 to match
                                # anchor heitsch_ratio(0.19)=16.197719 (L_max=5)
L_max_plan_pin = 10             # (local) plan's pinned value, used for INFO cross-check
N_eval = 41                     # (local) tau-grid cardinality
TAU_MIN = 0.0                   # (local)
TAU_MAX = 0.4                   # (local)
STEP = 0.01                     # (local)
TOLERANCE = 1e-4                # (local) PASS floor on |heitsch_ratio|
ANCHOR_TAU = 0.19               # (local) S83 anchor point
ANCHOR_VALUE = 16.197719        # (local) S83 W1-G2 heitsch_ratio anchor
ANCHOR_TOL = 1e-3               # (local) anchor sanity tolerance
SEED = 85011                    # (local) RNG seed (no MC needed but pinned per plan)

INPUT_PINS = {
    "gate": "S85-EPSH-JENSEN-SURVIVAL",
    "plan_section": "W11-1",
    "tau_fold": tau_fold,
    "H_fold": H_fold,
    "S_fold": S_fold,
    "dS_fold": dS_fold,
    "d2S_fold": d2S_fold,
    "M_KK": M_KK,
    "Vol_SU3_Haar": Vol_SU3_Haar,
    "J_C2": J_C2,
    "L_max_actual": L_max,
    "L_max_plan_pin": L_max_plan_pin,
    "N_eval": N_eval,
    "tau_range": [TAU_MIN, TAU_MAX],
    "step_size": STEP,
    "tolerance": TOLERANCE,
    "anchor_tau": ANCHOR_TAU,
    "anchor_value": ANCHOR_VALUE,
    "anchor_tol": ANCHOR_TOL,
    "random_seed": SEED,
    "scheme": "Heitsch-1-cocycle-HP1-norm",
    "convention": "Jensen-deformed-omega_J-transverse",
    "s83_anchor_npz_sha": s83_anchor_sha,
    "canonical_constants_sha": canon_sha,
}
input_sha = sha256_of(INPUT_PINS)

print("=" * 78)
print("S85 W11-1 -- EPSH-JENSEN-SURVIVAL")
print("=" * 78)
print(f"Input pins (first 20-line SHA log):")
for k, v in list(INPUT_PINS.items())[:18]:
    print(f"  {k} = {v}")
print(f"INPUT_SHA256 = {input_sha}")
print()

# -----------------------------------------------------------------------------
# Jensen Dirac spectrum (matches S83 W1-G2 exactly)
# -----------------------------------------------------------------------------

def su3_casimir(p, q):
    return (p*p + p*q + q*q + 3*p + 3*q) / 3.0


def su3_dimension(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def jensen_dirac_eigenvalues(L_max_, tau):
    """Jensen-deformed Dirac spectrum at given L_max, tau (S83 formula)."""
    evals = []
    dims = []
    labels = []
    for p in range(L_max_ + 1):
        for q in range(L_max_ + 1 - p):
            if p == 0 and q == 0:
                continue
            c2 = su3_casimir(p, q)
            dim = su3_dimension(p, q)
            rho = p + q
            lam = np.sqrt(c2) * np.exp(-tau * rho)
            for _ in range(dim):
                evals.append(+lam)
                evals.append(-lam)
            dims.append(dim)
            labels.append((p, q))
    return np.array(sorted(evals)), dims, labels


# -----------------------------------------------------------------------------
# epsilon_H_rep (mode-equation form, matches S83 Step 2 exactly)
# -----------------------------------------------------------------------------

dln_rho_dtau_at_fold = dS_fold / S_fold                          # (local)
dH_dtau_at_fold = (H_fold / 2.0) * dln_rho_dtau_at_fold          # (local)
epsilon_H_mode_eqn = 1.0 - (dH_dtau_at_fold / H_fold)            # (local)
epsilon_H_rep = epsilon_H_mode_eqn                               # (local) canonical

print(f"epsilon_H_rep (canonical, mode-equation form) = {epsilon_H_rep:.6f}")
print()

# -----------------------------------------------------------------------------
# CM Dixmier-proxy cocycle and heitsch_ratio -- exact S83 formula
# -----------------------------------------------------------------------------

def compute_cocycle(evals, eps_H):
    pos = evals[evals > 1e-10]
    dixmier = np.sum(1.0 / pos**4)
    cocycle = eps_H * dixmier / len(pos)
    return cocycle, dixmier, len(pos)


def heitsch_ratio_at(tau, L_max_, eps_H):
    """S83 exact formula: |delta_GV_proxy| / |cocycle_value|."""
    h = 1e-4                                                     # (local) stencil step
    ev_0, _, _ = jensen_dirac_eigenvalues(L_max_, tau)
    ev_p, _, _ = jensen_dirac_eigenvalues(L_max_, tau + h)
    ev_m, _, _ = jensen_dirac_eigenvalues(L_max_, tau - h)
    c_0, d_0, _ = compute_cocycle(ev_0, eps_H)
    c_p, _, _ = compute_cocycle(ev_p, eps_H)
    c_m, _, _ = compute_cocycle(ev_m, eps_H)
    delta_GV = (c_p - c_m) / (2.0 * h)                           # (local)
    ratio = abs(delta_GV) / max(abs(c_0), 1e-20)                 # (local)
    return ratio, c_0, delta_GV, d_0

# -----------------------------------------------------------------------------
# STEP 1 -- Anchor check at tau = 0.19 (L_max = 5)
# -----------------------------------------------------------------------------

anchor_ratio, anchor_cocycle, anchor_dGV, anchor_dix = heitsch_ratio_at(
    ANCHOR_TAU, L_max, epsilon_H_rep)
anchor_err = abs(anchor_ratio - ANCHOR_VALUE)
anchor_pass = (anchor_err < ANCHOR_TOL)

print(f"STEP 1 -- Anchor check at tau = {ANCHOR_TAU}, L_max = {L_max}")
print(f"  heitsch_ratio(tau_fold) = {anchor_ratio:.6f}")
print(f"  target (S83 W1-G2)      = {ANCHOR_VALUE}")
print(f"  abs difference          = {anchor_err:.6e}")
print(f"  within +/-{ANCHOR_TOL}?         = {anchor_pass}")
print()

# -----------------------------------------------------------------------------
# STEP 2 -- Tau-sweep at L_max = 5 (primary), 41 points in [0, 0.4]
# -----------------------------------------------------------------------------

tau_grid = np.linspace(TAU_MIN, TAU_MAX, N_eval)
h_ratios = np.zeros(N_eval)
cocycles = np.zeros(N_eval)
dGVs = np.zeros(N_eval)
dixmiers = np.zeros(N_eval)

print(f"STEP 2 -- Tau-sweep (L_max = {L_max}, N_eval = {N_eval})")
for i, tau in enumerate(tau_grid):
    r, c, dGV, d = heitsch_ratio_at(tau, L_max, epsilon_H_rep)
    h_ratios[i] = r
    cocycles[i] = c
    dGVs[i] = dGV
    dixmiers[i] = d
    if i % 10 == 0 or i == N_eval - 1:
        print(f"  tau = {tau:.3f}  h_ratio = {r:.6f}  cocycle = {c:.4e}")

min_ratio = h_ratios.min()
max_ratio = h_ratios.max()
argmin = int(np.argmin(h_ratios))
argmax = int(np.argmax(h_ratios))
print()
print(f"  min |h_ratio| = {min_ratio:.6f} at tau = {tau_grid[argmin]:.3f}")
print(f"  max |h_ratio| = {max_ratio:.6f} at tau = {tau_grid[argmax]:.3f}")
print(f"  PASS floor (1e-4) exceeded at all 41 tau values? {bool(np.all(h_ratios > TOLERANCE))}")
print()

# -----------------------------------------------------------------------------
# STEP 3 -- Monotonicity via finite-difference stencil
# -----------------------------------------------------------------------------

def deriv_4th_order(y, dx):
    """4th-order centered stencil interior; 3-point one-sided at endpoints."""
    n = len(y)
    d = np.zeros(n)
    # Interior: 4th-order centered
    for i in range(2, n-2):
        d[i] = (-y[i+2] + 8*y[i+1] - 8*y[i-1] + y[i-2]) / (12 * dx)
    # Near-boundary: 2nd-order centered
    d[1] = (y[2] - y[0]) / (2 * dx)
    d[n-2] = (y[n-1] - y[n-3]) / (2 * dx)
    # Endpoints: one-sided 3-point
    d[0] = (-3*y[0] + 4*y[1] - y[2]) / (2 * dx)
    d[n-1] = (3*y[n-1] - 4*y[n-2] + y[n-3]) / (2 * dx)
    return d


dh_dtau = deriv_4th_order(h_ratios, STEP)
sign_dh = np.sign(dh_dtau)
monotonic_increasing = bool(np.all(dh_dtau > 0))
monotonic_decreasing = bool(np.all(dh_dtau < 0))
extremum_count = int(np.sum(np.diff(sign_dh) != 0))
# Endpoint-ambiguity flag: if the interior is monotonic but endpoint stencils
# have opposite sign from interior, the monotonicity at boundary is "ambiguous"
interior_sign = np.sign(np.median(dh_dtau[2:-2]))
endpoint_ambiguous = bool(
    sign_dh[0] != interior_sign or sign_dh[-1] != interior_sign
)

print(f"STEP 3 -- Monotonicity (4th-order stencil interior, 3-point endpoints)")
print(f"  dh/dtau range: [{dh_dtau.min():.4f}, {dh_dtau.max():.4f}]")
print(f"  monotonic increasing? {monotonic_increasing}")
print(f"  monotonic decreasing? {monotonic_decreasing}")
print(f"  sign-change count: {extremum_count}")
print(f"  endpoint ambiguous? {endpoint_ambiguous}")
print()

# -----------------------------------------------------------------------------
# STEP 4 -- L_max cross-check (plan-pinned L_max = 10 for INFO)
# -----------------------------------------------------------------------------

print(f"STEP 4 -- L_max cross-check (plan pin L_max = {L_max_plan_pin})")
anchor_ratio_L10, _, _, _ = heitsch_ratio_at(ANCHOR_TAU, L_max_plan_pin, epsilon_H_rep)
min_L10, _, _, _ = heitsch_ratio_at(TAU_MIN, L_max_plan_pin, epsilon_H_rep)
max_L10, _, _, _ = heitsch_ratio_at(TAU_MAX, L_max_plan_pin, epsilon_H_rep)
print(f"  heitsch_ratio(tau_fold, L_max=10) = {anchor_ratio_L10:.6f}")
print(f"  heitsch_ratio(tau=0.0, L_max=10)  = {min_L10:.6f}")
print(f"  heitsch_ratio(tau=0.4, L_max=10)  = {max_L10:.6f}")
print(f"  L_max=10 minimum exceeds 1e-4? {min_L10 > TOLERANCE}")
print(f"  L_max=10 monotonic increasing (endpoints)? {max_L10 > min_L10}")
print()

# -----------------------------------------------------------------------------
# STEP 5 -- Verdict
# -----------------------------------------------------------------------------

main_floor_pass = bool(min_ratio > TOLERANCE)
monotonicity_resolved = (monotonic_increasing or monotonic_decreasing) and not endpoint_ambiguous

if main_floor_pass and monotonicity_resolved and anchor_pass:
    verdict = "PASS"
    reason = (f"min|h_ratio|={min_ratio:.4f} > 1e-4 ; strict monotone "
              f"{'increase' if monotonic_increasing else 'decrease'} resolved ; "
              f"anchor reproduced to {anchor_err:.2e}")
elif main_floor_pass and monotonicity_resolved and not anchor_pass:
    verdict = "INFO"
    reason = (f"survival floor + monotonicity OK but anchor mismatch "
              f"{anchor_err:.2e} > {ANCHOR_TOL}")
elif main_floor_pass and endpoint_ambiguous:
    verdict = "INFO"
    reason = (f"survival floor OK but monotonicity ambiguous at endpoints "
              f"(plan INFO clause: tau=0 Jensen-trivial / tau=0.4 range edge)")
elif main_floor_pass and extremum_count > 0:
    verdict = "INFO"
    reason = (f"survival floor OK; {extremum_count} sign-change(s) in dh/dtau "
              f"-- non-monotonic corridor")
elif not main_floor_pass:
    verdict = "FAIL"
    reason = (f"min|h_ratio|={min_ratio:.6e} < {TOLERANCE} "
              f"at tau={tau_grid[argmin]:.3f} -- [eps_H] becomes exact locally")
else:
    verdict = "INFO"
    reason = "mixed conditions -- see diagnostics"

print("=" * 78)
print(f"VERDICT = {verdict}")
print(f"Reason: {reason}")
print("=" * 78)
print()

# -----------------------------------------------------------------------------
# STEP 6 -- 4-tuple and closure SHA
# -----------------------------------------------------------------------------

scheme_tag = "Heitsch-1-cocycle-HP1-norm"
convention_tag = "Jensen-deformed-omega_J-transverse"

# content_sha256 = SHA of the gate's physical output (value, verdict, tags)
CONTENT_PINS = {
    "gate": "S85-EPSH-JENSEN-SURVIVAL",
    "value": float(min_ratio),
    "scheme": scheme_tag,
    "convention": convention_tag,
    "L_max": L_max,
    "verdict": verdict,
    "anchor_ratio_L5": float(anchor_ratio),
    "min_at_tau": float(tau_grid[argmin]),
    "max_at_tau": float(tau_grid[argmax]),
    "monotonic_increasing": monotonic_increasing,
    "endpoint_ambiguous": endpoint_ambiguous,
}
content_sha = sha256_of(CONTENT_PINS)

# audit_sha256 = SHA of the full audit chain (input pins + content SHA + diagnostics)
AUDIT_PINS = {
    "input_sha256": input_sha,
    "content_sha256": content_sha,
    "anchor_ratio_L10_cross": float(anchor_ratio_L10),
    "max_ratio": float(max_ratio),
    "anchor_pass": bool(anchor_pass),
    "monotonic_decreasing": monotonic_decreasing,
    "extremum_count": extremum_count,
    "dh_dtau_min": float(dh_dtau.min()),
    "dh_dtau_max": float(dh_dtau.max()),
    "schema_version": "S84+",
}
audit_sha = sha256_of(AUDIT_PINS)

# Single-line Pattern A (S84+ dual-SHA format, matching prior S85 convention
# e.g. S85-W10-W0-L-INVERTED-BRANCH-ENUMERATION line in s85_gate_verdicts.txt)
verdict_line = (
    f"S85-EPSH-JENSEN-SURVIVAL: {verdict} -- "
    f"value={min_ratio:.6f} scheme={scheme_tag} convention={convention_tag} "
    f"L_max={L_max} "
    f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+"
)

print(f"4-tuple: (value={min_ratio:.6f}, scheme={scheme_tag}, "
      f"convention={convention_tag}, L_max={L_max})")
print(f"CONTENT_SHA256 = {content_sha}")
print(f"AUDIT_SHA256   = {audit_sha}")
print()
print("Verdict line (S84+ dual-SHA format, Pattern A):")
print(verdict_line)
print()

# -----------------------------------------------------------------------------
# STEP 7 -- Append verdict + save outputs
# -----------------------------------------------------------------------------

VERDICT_FILE = Path(__file__).parent / "s85_gate_verdicts.txt"
# Idempotency guard: skip append if this exact content_sha is already logged
existing = VERDICT_FILE.read_text(encoding="utf-8") if VERDICT_FILE.exists() else ""
if f"content_sha256={content_sha}" in existing:
    print(f"Verdict line already present (content_sha256={content_sha[:16]}...); skipping append.")
else:
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(verdict_line + "\n")
    print(f"Verdict line appended to: {VERDICT_FILE}")

out_npz = Path(__file__).parent / "s85_w11_epsh_jensen_survival.npz"
np.savez_compressed(
    out_npz,
    tau_grid=tau_grid,
    h_ratios=h_ratios,
    cocycles=cocycles,
    delta_GV=dGVs,
    dixmiers=dixmiers,
    dh_dtau=dh_dtau,
    anchor_ratio_L5=anchor_ratio,
    anchor_ratio_L10=anchor_ratio_L10,
    L_max=L_max,
    L_max_plan_pin=L_max_plan_pin,
    verdict=verdict,
    content_sha=content_sha,
    audit_sha=audit_sha,
    input_sha=input_sha,
)
print(f"npz saved: {out_npz}")

out_png = Path(__file__).parent / "s85_w11_epsh_jensen_survival.png"
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
ax = axes[0, 0]
ax.plot(tau_grid, h_ratios, 'o-', color='C0', ms=4)
ax.axhline(TOLERANCE, color='r', linestyle='--', alpha=0.7,
           label=f'PASS floor = {TOLERANCE}')
ax.axvline(ANCHOR_TAU, color='k', linestyle=':', alpha=0.5, label=f'tau_fold')
ax.scatter([ANCHOR_TAU], [ANCHOR_VALUE], color='C3', s=60, zorder=5,
           label=f'anchor = {ANCHOR_VALUE}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\|[\varepsilon_H](\tau)\|_{HP^1}$')
ax.set_title(f'Heitsch HP^1 norm across Jensen tau-corridor, L_max={L_max}')
ax.legend(fontsize=9)
ax.set_yscale('log')

ax = axes[0, 1]
ax.plot(tau_grid, dh_dtau, 'o-', color='C2', ms=3)
ax.axhline(0, color='k', linestyle=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$d\|\varepsilon_H\|/d\tau$')
ax.set_title(f'Monotonicity (4th-order stencil); extrema = {extremum_count}')

ax = axes[1, 0]
L_cross = [3, 5, 7, 10]
vals_cross = []
for Lc in L_cross:
    r, _, _, _ = heitsch_ratio_at(ANCHOR_TAU, Lc, epsilon_H_rep)
    vals_cross.append(r)
ax.plot(L_cross, vals_cross, 'o-', color='C4', ms=8)
ax.axhline(ANCHOR_VALUE, color='C3', linestyle='--', alpha=0.7,
           label=f'S83 anchor {ANCHOR_VALUE}')
ax.set_xlabel(r'$L_{\rm max}$')
ax.set_ylabel(r'$\|[\varepsilon_H](\tau_{\rm fold})\|_{HP^1}$')
ax.set_title(f'L_max sensitivity at tau_fold={ANCHOR_TAU}')
ax.legend(fontsize=9)

ax = axes[1, 1]
ax.axis('off')
summary = (
    f"GATE: S85-EPSH-JENSEN-SURVIVAL\n\n"
    f"L_max actual (anchor-matching) = {L_max}\n"
    f"L_max plan pin                 = {L_max_plan_pin}\n\n"
    f"tau sweep: [{TAU_MIN}, {TAU_MAX}], {N_eval} pts\n"
    f"min |h| = {min_ratio:.4f} at tau={tau_grid[argmin]:.3f}\n"
    f"max |h| = {max_ratio:.4f} at tau={tau_grid[argmax]:.3f}\n"
    f"PASS floor (1e-4) exceeded: {bool(np.all(h_ratios > TOLERANCE))}\n\n"
    f"anchor |h(0.19)| = {anchor_ratio:.6f}\n"
    f"anchor target    = {ANCHOR_VALUE}\n"
    f"anchor err       = {anchor_err:.2e}\n"
    f"anchor pass?     = {anchor_pass}\n\n"
    f"monotonic increasing? {monotonic_increasing}\n"
    f"extremum count      = {extremum_count}\n"
    f"endpoint ambiguous? {endpoint_ambiguous}\n\n"
    f"VERDICT: {verdict}\n"
    f"content_sha: {content_sha[:16]}...\n"
    f"audit_sha:   {audit_sha[:16]}...\n"
)
ax.text(0.02, 0.98, summary, transform=ax.transAxes, family='monospace',
        va='top', fontsize=9)

plt.suptitle(f'S85 W11-1 EPSH-JENSEN-SURVIVAL -- {verdict}', fontsize=13)
plt.tight_layout()
plt.savefig(out_png, dpi=120)
plt.close()
print(f"png saved: {out_png}")
print()
print("[S85 W11-1 COMPLETE]")
