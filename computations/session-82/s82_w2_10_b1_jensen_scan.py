#!/usr/bin/env python3
"""
S82 W2-10 — B1-JENSEN-SCAN (Jensen tau-scan of J_u1 on B1 acoustic branch)
==========================================================================

Gate: S82-B1-JENSEN-SCAN ([SIGN])

Pre-registered threshold (S80 plan L1528-L1535):
  HYPOTHESIS: J_u1(tau) has definite sign across tau in {0.15, 0.17, 0.19, 0.21, 0.25}.
  PASS iff J_u1 monotone (consistent sign, 0 sign changes)
  INFO iff sign changes exactly once (1 sign change)
  FAIL iff multiple sign changes (>=2 sign changes)

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s54_tb_hamiltonian.py (defines canonical Jensen-law J_u1(tau))

Output 4-tuple:
  (value=<n_sign_changes>, scheme=B1-ACOUSTIC, convention=JENSEN-TAU-SCAN, L_max=5)

Classification: PHONONIC
  B1 = acoustic (singlet u(1)) phononic branch of substrate Dirac spectrum.
  J_u1(tau) = B1 intra-branch Josephson stiffness under Jensen deformation.

METHODOLOGY
-----------
J_u1(tau) is the per-branch Josephson coupling for the B1 (acoustic, u(1) singlet)
branch under Jensen deformation of SU(3). From s54_tb_hamiltonian.py lines 248-267
(canonical volume-preserving metric scaling):

    J_u1(tau) = J_u1(tau_fold) * exp(2 * (tau_fold - tau))

with J_u1(tau_fold) = 0.038 M_KK from canonical_constants.py line 293
(S47 TEXTURE-CORR-48). The exponent factor 2 matches the u(1) direction's
dimensionality d_u1 = 1 through the volume-preserving constraint
L_u1 * L_su2^3 * L_C2^4 = 1.

The scan evaluates J_u1 at tau in {0.15, 0.17, 0.19, 0.21, 0.25} per S80 L1532.
Sign sequence is counted. Since J_u1 is product of a strictly positive canonical
constant and exp() (strictly positive), structural result is sign = +1 for all tau.

SUBSTITUTION CHAIN (MANDATORY — [SIGN] trigger)
------------------------------------------------
Step 1 [definition]:
  J_u1(tau) := J_u1(tau_fold) * exp(2 * (tau_fold - tau))    [s54 l. 265-267]
  J_u1(tau_fold) = 0.038 M_KK > 0                           [canonical l. 293]
  tau_fold = 0.19                                            [canonical l. 124]

Step 2 [substitution at scan points]:
  tau = 0.15:  exponent = 2*(0.19 - 0.15) = +0.08
  tau = 0.17:  exponent = 2*(0.19 - 0.17) = +0.04
  tau = 0.19:  exponent = 2*(0.19 - 0.19) =  0.00
  tau = 0.21:  exponent = 2*(0.19 - 0.21) = -0.04
  tau = 0.25:  exponent = 2*(0.19 - 0.25) = -0.12

Step 3 [simplification / canonical form]:
  J_u1(tau) = (0.038) * exp(2*(tau_fold - tau))
  Product of strictly positive canonical constant and exp() function.
  exp(x) > 0 for all real x, so J_u1(tau) > 0 for all tau.
  d/dtau [J_u1(tau)] = -2 * J_u1(tau) < 0  =>  J_u1 is strictly decreasing in tau.

Step 4 [direction from canonical form]:
  sign(J_u1(tau)) = +1 for every tau in the scan.
  n_sign_changes = 0 (structurally, since exp > 0 always).
  => PASS (monotone, consistent sign) by S80 L1533.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every intermediate tagged `# (local)`
- No GPU needed (5-point scalar eval)
- SHA-256 of all input files logged first
- 4-tuple printed as final non-verdict line
- Gate verdict appended to s82_gate_verdicts.txt with full 64-char SHA
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S82"                                                    # (local)
GATE_ID = "S82-B1-JENSEN-SCAN"                                     # (local)
SCHEME = "B1-ACOUSTIC"                                             # (local)
CONVENTION = "JENSEN-TAU-SCAN"                                     # (local)
L_MAX = 5                                                          # (local) 5 tau points

# Pre-registered scan per S80 L1532
TAU_SCAN = [0.15, 0.17, 0.19, 0.21, 0.25]                          # (local)

# Output destinations
OUT_NPZ = resolve_output(82, 's82_w2_10_b1_jensen_scan.npz')
OUT_PNG = resolve_output(82, 's82_w2_10_b1_jensen_scan.png')
VERDICT_TXT = resolve_output(82, 's82_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(54, 's54_tb_hamiltonian.py'),
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 pinning
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Canonical Jensen law
# ---------------------------------------------------------------------------
def J_u1_of_tau(tau: float) -> float:
    """u(1) hypercharge Josephson coupling at tau.

    Canonical law from s54_tb_hamiltonian.py lines 265-267:
      J_u1(tau) = J_u1(tau_fold) * exp(2 * (tau_fold - tau))

    Volume-preserving metric scaling: exponent factor 2 matches d_u1 = 1.
    J_u1(tau_fold) = 0.038 M_KK (canonical_constants.py line 293).
    """
    return J_u1 * np.exp(2.0 * (tau_fold - tau))


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute():
    """Evaluate J_u1(tau) at pre-registered scan points, count sign changes."""
    taus = np.array(TAU_SCAN, dtype=float)                         # (local)
    J_vals = np.array([J_u1_of_tau(t) for t in taus])              # (local)
    signs = np.sign(J_vals).astype(int)                            # (local)

    # Count sign CHANGES (transitions). A zero is NOT a sign change unless a
    # flip occurs across it; we mark any change in sign across adjacent points.
    n_sign_changes = int(np.sum(np.diff(signs) != 0))              # (local)

    # Monotonicity of J_u1 itself (structural cross-check)
    diffs = np.diff(J_vals)                                        # (local)
    strictly_decreasing = bool(np.all(diffs < 0.0))                # (local)

    # Cross-check: analytic derivative d/dtau [J_u1] = -2*J_u1(tau)
    analytic_deriv = -2.0 * J_vals                                 # (local)
    # Numerical derivative at interior points
    tau_mid = 0.5 * (taus[:-1] + taus[1:])                         # (local)
    num_deriv = np.diff(J_vals) / np.diff(taus)                    # (local)
    analytic_deriv_mid = -2.0 * J_u1 * np.exp(2.0 * (tau_fold - tau_mid))  # (local)
    deriv_rel_err = np.max(np.abs(num_deriv - analytic_deriv_mid)
                           / np.abs(analytic_deriv_mid))           # (local)

    return {
        "taus": taus,
        "J_u1_vals": J_vals,
        "signs": signs,
        "n_sign_changes": n_sign_changes,
        "strictly_decreasing": strictly_decreasing,
        "analytic_deriv": analytic_deriv,
        "num_deriv": num_deriv,
        "tau_mid": tau_mid,
        "analytic_deriv_mid": analytic_deriv_mid,
        "deriv_rel_err": deriv_rel_err,
        "value": n_sign_changes,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate evaluation
# ---------------------------------------------------------------------------
def evaluate_gate(n_sign_changes: int) -> str:
    """PASS = 0 changes (monotone sign); INFO = 1; FAIL = >=2 (per S80 L1533-L1535)."""
    if n_sign_changes == 0:
        return "PASS"
    if n_sign_changes == 1:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 8 — Outputs
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, closure_sha) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def save_npz(results, closure_sha):
    np.savez(
        OUT_NPZ,
        taus=results["taus"],
        J_u1_vals=results["J_u1_vals"],
        signs=results["signs"],
        n_sign_changes=np.array(results["n_sign_changes"]),
        strictly_decreasing=np.array(results["strictly_decreasing"]),
        analytic_deriv=results["analytic_deriv"],
        num_deriv=results["num_deriv"],
        analytic_deriv_mid=results["analytic_deriv_mid"],
        deriv_rel_err=np.array(results["deriv_rel_err"]),
        tau_fold=np.array(tau_fold),
        J_u1_at_fold=np.array(J_u1),
        closure_sha=np.array(closure_sha, dtype=object),
        scheme=np.array(SCHEME, dtype=object),
        convention=np.array(CONVENTION, dtype=object),
    )


def save_png(results):
    fig, ax = plt.subplots(figsize=(7.0, 4.8))                     # (local)
    taus = results["taus"]                                         # (local)
    J = results["J_u1_vals"]                                       # (local)

    # Dense curve for visual continuity
    tau_dense = np.linspace(0.13, 0.27, 200)                       # (local)
    J_dense = J_u1 * np.exp(2.0 * (tau_fold - tau_dense))          # (local)

    ax.plot(tau_dense, J_dense, color="#1f77b4", lw=1.4, alpha=0.55,
            label=r"$J_{u(1)}(\tau)$ (canonical Jensen law)")
    ax.plot(taus, J, "o", color="#d62728", ms=7, zorder=5,
            label=r"scan points (S80 L1532)")
    ax.axvline(tau_fold, color="k", lw=0.8, ls="--", alpha=0.6,
               label=rf"$\tau_{{\mathrm{{fold}}}} = {tau_fold}$")
    ax.axhline(0.0, color="grey", lw=0.5, alpha=0.4)

    # Sign annotations
    for t, j, s in zip(taus, J, results["signs"]):
        sign_txt = "+" if s > 0 else ("0" if s == 0 else "-")      # (local)
        ax.annotate(f"sign={sign_txt}", (t, j),
                    xytext=(0, 12), textcoords="offset points",
                    fontsize=8, ha="center", color="#444444")

    ax.set_xlabel(r"$\tau$ (Jensen deformation parameter)")
    ax.set_ylabel(r"$J_{u(1)}(\tau)$  (M$_{\mathrm{KK}}$)")
    ax.set_title(
        f"S82 W2-10: B1 (acoustic) Jensen tau-scan of $J_{{u(1)}}$ -- "
        f"sign changes = {results['n_sign_changes']}"
    )
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                               # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...  (full: {closure})")
    print()

    print(f"Canonical inputs:")
    print(f"  tau_fold = {tau_fold}")
    print(f"  J_u1(tau_fold) = {J_u1}  (M_KK)")
    print(f"  Jensen law: J_u1(tau) = J_u1(fold) * exp(2 * (tau_fold - tau))")
    print()

    results = compute()
    value = int(results["value"])                                  # (local)

    print(f"tau-scan of J_u1(tau) on B1 (acoustic branch):")
    print(f"  {'tau':>6}  {'J_u1':>14}  {'sign':>5}")
    for t, j, s in zip(results["taus"], results["J_u1_vals"], results["signs"]):
        print(f"  {t:>6.3f}  {j:>14.9f}  {int(s):>+5d}")
    print()
    print(f"Sign sequence: {results['signs'].tolist()}")
    print(f"Number of sign changes: {value}")
    print(f"Strictly decreasing in tau: {results['strictly_decreasing']}")
    print(f"Analytic derivative check (max rel err vs numerical): "
          f"{results['deriv_rel_err']:.3e}")
    print()

    verdict = evaluate_gate(value)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    save_npz(results, closure)
    save_png(results)
    append_verdict(verdict, value, closure)

    wall = time.time() - t0                                        # (local)
    print()
    print(f"=== {GATE_ID}: {verdict}  (wall {wall:.2f}s) ===")
    print(f"NPZ:  {OUT_NPZ.name}")
    print(f"PNG:  {OUT_PNG.name}")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
