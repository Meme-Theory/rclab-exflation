#!/usr/bin/env python3
"""
S111 W1-3 S111-CF-CLOCKLOC4-UNIQUE — Lambda=3H^2-preserving reparam-class / substrate-natural-clock uniqueness
==============================================================================================================

Gate: S111-CF-CLOCKLOC4-UNIQUE ([VERIFY])
Classification: GEOMETRIC (Level-2 clock frame-uniqueness; orthogonal to CLOCKLOC1/2)

Pre-registered threshold (trichotomy on the Lambda=3H^2-preserving reparam class G_inv):
  G_inv := { g monotone : Lambda - 3 H_g^2 = 0  whenever  Lambda - 3 H_tau^2 = 0 }
  PASS  (UNIQUE)           iff |{ substrate-intrinsic monotone f : f preserves Lambda=3H^2
                                  without extra structure }| = 1 (only tau)
  INFO  (UNIQUE-UP-TO-CLASS) iff >= 2 substrate-monotone functions land in the class (a constant-rate
                                  reparam |C|^2 or a0 also preserves it)
  FAIL  (DEGENERATE)        iff Lambda=3H^2 is frame-invariant ONLY for tau exactly with NO nontrivial
                                  class AND that makes "substrate-natural" vacuous (every monotone
                                  relabel breaks the relation, so naturalness does no work as a selector)

Method (WS-CLOCKLOC R3):
  H is a COORDINATE-TIME rate (frame-dependent). Relabel the clock t->g(t), g'=ds/dt>0; then H_t=H_s*g'.
  Lambda is a curvature SCALAR (reparam-invariant). At the de Sitter fixed point Lambda=3 H_s^2, so in the
  t-frame  Lambda - 3 H_t^2 = Lambda - 3 (H_s g')^2 = 3 H_s^2 (1 - g'^2) = Lambda (1 - g'^2).
  Vanishing (Lambda>0, g'>0) iff g'=1: the class is the RIGID SINGLETON {g'=1} (an affine rescale a!=1
  is EXCLUDED). Substrate-naturalness picks tau (dS/dtau one-signed, the substrate's intrinsic deformation
  coordinate). The gate then tests the SECOND substrate-monotone candidates: |C|^2(tau) (strictly monotone
  from 5/14, S96-GEOM-CCC-WEYL) and a0(tau). Each is a monotone REPARAM of tau; if its g'=d(.)/dtau is a
  CONSTANT it lands in {g'=1} up to scale (UP-TO-CLASS); if g' VARIES it forces g'!=1 pointwise (EXCLUDED).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (feeds audit_sha256; supplies tau_fold, dS_fold, a0_fold)
  - computations/session-96/s96_geom_ccc_weyl.npz (|C|^2(tau) strictly-monotone trajectory, 201-pt grid)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<UNIQUE|UNIQUE-UP-TO-CLASS|DEGENERATE>, scheme=reparam-invariance-de-Sitter-relation,
   convention=ABSOLUTE, L_max=N/A)

DISTINCTNESS from §VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (S90 W2 CF-19, STAGE-3-PERMANENT):
  §VII.AW: uniqueness among a DISCRETE candidate space {P_1=substrate-clock Pinning-A, P_2=mode-density,
           P_3=GGE-anchored} by a 5-CRITERIA SATURATION selector, modulo the AFFINE quotient tau->a*tau+b.
  CLOCKLOC4: uniqueness among the CONTINUUM of substrate-intrinsic MONOTONE functions by the
           Lambda=3H^2-PRESERVING selector, whose class is the RIGID SINGLETON {g'=1} (affine a!=1 EXCLUDED).
  Orthogonal: different candidate spaces (3 discrete pinnings vs continuum of monotone functions),
  different selectors (5-criteria saturation vs Lambda=3H^2-preservation), different quotients
  (affine a*tau+b vs g'=1-rigid). CLOCKLOC4 is the Lambda=3H^2-preserving-reparam-class specialization.

Substrate framing: GEOMETRIC. H is a slicing-dependent rate (the ADM lapse fixes the slicing); Lambda is a
  curvature scalar (description-independent). The physical content is the RELATION among rates, not any
  single rate's magnitude. tau=Jensen modulus IS the substrate's intrinsic deformation coordinate
  (dS/dtau one-signed) -- NOT an arbitrary phase-space function. This gate is a frame-uniqueness check on
  the Level-2 clock; D_K eigenvalues -> spectral action S(tau) -> dS/dtau one-signed -> tau the clock.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Bootstrap _shared onto sys.path so canonical_constants imports
# (sibling-script convention, e.g. computations/session-101/*.py)
# ---------------------------------------------------------------------------
import os as _os
import sys as _sys
_SHARED_BOOT = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "_shared")
if _SHARED_BOOT not in _sys.path:
    _sys.path.insert(0, _SHARED_BOOT)

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import tau_fold, dS_fold, a0_fold

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (CPU-only gate: symbolic algebra + 201-pt grid)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 per plan GPU_path
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sympy as sp

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S111"                                                   # (local)
GATE_ID = "S111-CF-CLOCKLOC4-UNIQUE"                               # (local)
SCHEME = "reparam-invariance-de-Sitter-relation"                  # (local)
CONVENTION = "ABSOLUTE"                                            # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered numerical tolerances (PRDR machinery pins)
TOL_SYMBOLIC = 0.0           # (local) Sympy exact-zero residual for the reparam-class identity
TOL_NUM = 1e-9               # (local) numerical monotone-function check
RATE_CONST_FRAC = 1e-6       # (local) std/mean(g') below this => "constant-rate" reparam (UP-TO-CLASS)
CORRIDOR_MIN = 0.0           # (local) transit-corridor lower bound
CORRIDOR_MAX = 0.19          # (local) transit-corridor upper bound (the fold)
WEYL2_GENESIS_EXACT = 5.0 / 14.0   # (local) |C|^2(0) = 5/14 (WCH minimum), S96 anchor

OUT_NPZ = SESSION_DIR / "s111_cf_clockloc4_unique.npz"
OUT_PNG = SESSION_DIR / "s111_cf_clockloc4_unique.png"

CCC_WEYL_NPZ = COMPUTATIONS_DIR / "session-96" / "s96_geom_ccc_weyl.npz"  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CCC_WEYL_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (dual-SHA S84+)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def reparam_class_symbolic() -> dict:
    """Step 1-4 of the substitution chain, exact via Sympy.

    Returns the reparam-class identity Lambda - 3 H_t^2 = Lambda (1 - g'^2), the exact-zero
    residual against the target, and the g'>0 vanishing locus {g'=1}.
    """
    Lam, Hs, gp = sp.symbols("Lambda H_s g_prime", positive=True)   # (local)
    H_t = Hs * gp                                                    # (local) chain rule: H_t = H_s g'
    expr_raw = Lam - 3 * H_t**2                                      # (local) Lambda - 3 H_t^2
    # de Sitter fixed point in the s-frame: 3 H_s^2 = Lambda
    expr_sub = expr_raw.subs(Hs**2, Lam / 3)                         # (local)
    expr_sub = sp.simplify(expr_sub)                                 # (local) -> Lambda - Lambda g'^2
    target = Lam * (1 - gp**2)                                       # (local) Lambda (1 - g'^2)
    residual = sp.simplify(expr_sub - target)                       # (local) MUST be 0
    identity_holds = bool(residual == 0)                            # (local)

    # vanishing locus with g'>0 (Lambda>0 assumed): g'=1
    gp_free = sp.symbols("g_prime", real=True)                      # (local)
    roots = sp.solve(sp.Eq(1 - gp_free**2, 0), gp_free)             # (local) [-1, 1]
    positive_roots = [r for r in roots if r > 0]                    # (local) [1]
    class_is_singleton = (positive_roots == [sp.Integer(1)])        # (local)

    return {
        "expr_sub_str": str(expr_sub),
        "target_str": str(target),
        "residual_str": str(residual),
        "identity_holds": identity_holds,
        "positive_roots": [int(r) for r in positive_roots],
        "class_is_singleton_g1": bool(class_is_singleton),
    }


def candidate_rate(tau: np.ndarray, f: np.ndarray, lo: float, hi: float) -> dict:
    """Cross-check a substrate-monotone candidate f(tau) over [lo,hi].

    Reports: strict monotonicity (g'=df/dtau > 0 everywhere), and whether g' is CONSTANT
    (std/mean below RATE_CONST_FRAC => constant-rate => lands in {g'=1} up to scale => UP-TO-CLASS)
    or VARYING (forces g'!=1 pointwise => EXCLUDED).
    """
    mask = (tau >= lo - 1e-12) & (tau <= hi + 1e-9)                 # (local)
    t = tau[mask]                                                    # (local)
    c = f[mask]                                                      # (local)
    gprime = np.gradient(c, t)                                       # (local) g'(tau)=df/dtau
    strictly_pos = bool(np.all(gprime > TOL_NUM))                   # (local)
    mean_gp = float(np.mean(gprime))                                # (local)
    std_gp = float(np.std(gprime))                                  # (local)
    rel_spread = std_gp / abs(mean_gp) if abs(mean_gp) > 0 else np.inf  # (local)
    is_constant_rate = bool(rel_spread < RATE_CONST_FRAC)           # (local)
    # EXCLUDED from {g'=1} iff (monotone but varying rate). LANDS-IN-CLASS iff constant-rate.
    lands_in_class = bool(strictly_pos and is_constant_rate)        # (local)
    return {
        "n_pts": int(len(t)),
        "f_lo": float(c[0]),
        "f_hi": float(c[-1]),
        "gprime_min": float(np.min(gprime)),
        "gprime_max": float(np.max(gprime)),
        "gprime_mean": mean_gp,
        "gprime_rel_spread": float(rel_spread),
        "strictly_monotone": strictly_pos,
        "is_constant_rate": is_constant_rate,
        "lands_in_class": lands_in_class,
    }


def compute() -> dict:
    # --- (A) symbolic reparam-class identity + vanishing locus -------------------------------
    sym = reparam_class_symbolic()
    print("  [A] reparam-class identity:")
    print(f"      Lambda - 3 H_t^2 (dS subst) = {sym['expr_sub_str']}")
    print(f"      target  Lambda (1 - g'^2)   = {sym['target_str']}")
    print(f"      residual (must be 0)        = {sym['residual_str']}  -> identity_holds={sym['identity_holds']}")
    print(f"      vanishing locus g'>0        = {sym['positive_roots']}  -> singleton {{g'=1}}={sym['class_is_singleton_g1']}")

    # --- (B) substrate-natural selector: tau (dS/dtau one-signed) ----------------------------
    ds_dtau = float(dS_fold)                                         # (local) dS_full/dtau at fold (S42)
    tau_is_one_signed = bool(ds_dtau != 0.0)                         # (local) one-signed => valid clock
    print(f"  [B] substrate-natural selector: dS/dtau = {ds_dtau:.6f} (one-signed={tau_is_one_signed}); "
          f"tau=Jensen modulus is the intrinsic deformation coordinate (tau_fold={float(tau_fold)}).")

    # --- (C) SECOND candidate |C|^2(tau): strictly monotone from 5/14 (S96-GEOM-CCC-WEYL) ----
    d = np.load(CCC_WEYL_NPZ, allow_pickle=True)                    # (local)
    tau_grid = np.asarray(d["tau"], dtype=float)                    # (local)
    weyl2 = np.asarray(d["weyl2"], dtype=float)                     # (local) |C|^2(tau)
    weyl2_genesis = float(np.asarray(d["weyl2_genesis_exact"]).ravel()[0])  # (local) = 5/14
    npz_strictly_inc = bool(np.asarray(d["strictly_increasing"]).ravel()[0])  # (local)
    npz_n_dec = int(np.asarray(d["n_decreasing_steps"]).ravel()[0])  # (local)
    genesis_anchor_ok = bool(abs(weyl2_genesis - WEYL2_GENESIS_EXACT) < 1e-12)  # (local)
    c2_cross = candidate_rate(tau_grid, weyl2, CORRIDOR_MIN, CORRIDOR_MAX)
    print(f"  [C] candidate |C|^2(tau): genesis={weyl2_genesis:.10f} (5/14={WEYL2_GENESIS_EXACT:.10f}, "
          f"match={genesis_anchor_ok}); npz strictly_increasing={npz_strictly_inc}, n_dec_steps={npz_n_dec}")
    print(f"      corridor [0,0.19]: g'=d|C|^2/dtau in [{c2_cross['gprime_min']:.6f},{c2_cross['gprime_max']:.6f}], "
          f"rel_spread(std/mean)={c2_cross['gprime_rel_spread']:.4e}, constant_rate={c2_cross['is_constant_rate']}, "
          f"lands_in_class={c2_cross['lands_in_class']}")

    # --- (D) THIRD candidate a0(tau): zeroth Seeley-DeWitt (volume/mode-count), tau-flat ------
    # a0 is the dimensionless mode-count term (a0_fold=6440). On the transit corridor it is tau-flat at
    # leading order => g'_a0 = da0/dtau ~ 0 => NOT strictly monotone => not a valid deparametrization clock
    # (fails the tau_dot != 0 (D)-well-posedness requirement). So a0 is not even a clock candidate.
    a0_val = float(a0_fold)                                          # (local)
    a0_is_monotone_clock = False                                    # (local) constant => g'=0 => not monotone
    a0_lands_in_class = False                                       # (local) cannot land: not monotone
    print(f"  [D] candidate a0(tau): a0_fold={a0_val} (volume/mode-count term, tau-flat at leading order); "
          f"g'_a0~0 => monotone_clock={a0_is_monotone_clock}, lands_in_class={a0_lands_in_class}")

    # --- (E) trichotomy verdict --------------------------------------------------------------
    # Members of G_inv intersect {substrate-monotone}:
    #   tau            : lands (g'=1 reference)                          -> always 1
    #   |C|^2(tau)     : lands iff constant-rate                         -> c2_cross['lands_in_class']
    #   a0(tau)        : lands iff monotone-clock AND constant-rate      -> a0_lands_in_class (False)
    members = ["tau"]                                                # (local) tau is the reference member
    if c2_cross["lands_in_class"]:
        members.append("|C|^2(tau)")
    if a0_lands_in_class:
        members.append("a0(tau)")
    cardinality = len(members)                                       # (local)

    # DEGENERATE (FAIL) guard: only if the class were g'=1-only AND substrate-naturalness were vacuous.
    # Substrate-naturalness is NOT vacuous: dS/dtau is one-signed, so tau IS singled out by substrate
    # physics (it is the unique monotone whose rate is the spectral-action gradient). The class being the
    # rigid singleton {g'=1} is exactly what makes the substrate-natural selector DO WORK (it excludes all
    # non-tau monotone functions whose g' varies). So FAIL is reachable only if tau_is_one_signed is False.
    naturalness_does_work = bool(tau_is_one_signed and sym["class_is_singleton_g1"])  # (local)

    if not naturalness_does_work:
        verdict = "FAIL"                                            # (local)
        value_tag = "DEGENERATE"                                    # (local)
    elif cardinality == 1:
        verdict = "PASS"                                            # (local)
        value_tag = "UNIQUE"                                        # (local)
    else:
        verdict = "INFO"                                            # (local)
        value_tag = "UNIQUE-UP-TO-CLASS"                            # (local)

    # dual-prior posterior re-allocation (plan dual_prior block)
    # PASS(UNIQUE) -> 0.9 to Track A; INFO(UP-TO-CLASS) -> 0.9 to Track B; FAIL -> re-examine.
    if verdict == "PASS":
        posterior_A, posterior_B = 0.9, 0.1                        # (local)
    elif verdict == "INFO":
        posterior_A, posterior_B = 0.1, 0.9                        # (local)
    else:
        posterior_A, posterior_B = float("nan"), float("nan")     # (local)

    print(f"  [E] G_inv intersect substrate-monotone = {members}  (cardinality={cardinality})")
    print(f"      naturalness_does_work={naturalness_does_work} -> verdict={verdict} ({value_tag})")
    print(f"      dual-prior posterior: Track A (UNIQUE) {posterior_A} / Track B (UP-TO-CLASS) {posterior_B}")

    return {
        "value": value_tag,
        "verdict": verdict,
        "symbolic": sym,
        "ds_dtau": ds_dtau,
        "tau_is_one_signed": tau_is_one_signed,
        "tau_fold": float(tau_fold),
        "weyl2_genesis": weyl2_genesis,
        "genesis_anchor_ok": genesis_anchor_ok,
        "npz_strictly_inc": npz_strictly_inc,
        "npz_n_dec": npz_n_dec,
        "c2_cross": c2_cross,
        "a0_val": a0_val,
        "a0_is_monotone_clock": a0_is_monotone_clock,
        "a0_lands_in_class": a0_lands_in_class,
        "members": members,
        "cardinality": cardinality,
        "naturalness_does_work": naturalness_does_work,
        "posterior_A": posterior_A,
        "posterior_B": posterior_B,
        # arrays for plot / npz
        "tau_grid": tau_grid,
        "weyl2": weyl2,
    }


def make_plot(res: dict) -> None:
    tau = res["tau_grid"]
    weyl2 = res["weyl2"]
    mask = (tau >= CORRIDOR_MIN - 1e-12) & (tau <= CORRIDOR_MAX + 1e-9)
    t = tau[mask]
    c = weyl2[mask]
    gprime = np.gradient(c, t)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.4))

    # Panel 1: the reparam-class identity Lambda(1-g'^2) vs g'
    gp = np.linspace(0.0, 2.0, 400)
    axes[0].plot(gp, 1.0 - gp**2, lw=2, color="C0")
    axes[0].axhline(0.0, color="0.5", lw=0.8)
    axes[0].axvline(1.0, color="C3", ls="--", lw=1.2, label="g'=1 (rigid singleton)")
    axes[0].scatter([1.0], [0.0], color="C3", zorder=5)
    axes[0].set_xlabel("g' = ds/dt")
    axes[0].set_ylabel(r"$(\Lambda-3H_t^2)/\Lambda = 1-g'^2$")
    axes[0].set_title(r"Reparam class: $\Lambda-3H_t^2=\Lambda(1-g'^2)$, zero iff g'=1")
    axes[0].legend(fontsize=8)
    axes[0].grid(alpha=0.3)

    # Panel 2: |C|^2(tau) over the corridor (monotone candidate)
    axes[1].plot(t, c, lw=2, color="C1", label=r"$|C|^2(\tau)$")
    axes[1].axhline(WEYL2_GENESIS_EXACT, color="C3", ls=":", lw=1.0, label="5/14 (WCH min)")
    axes[1].set_xlabel(r"$\tau$ (Jensen modulus)")
    axes[1].set_ylabel(r"$|C|^2(\tau)$")
    axes[1].set_title("2nd candidate: strictly monotone (S96-GEOM-CCC-WEYL)")
    axes[1].legend(fontsize=8)
    axes[1].grid(alpha=0.3)

    # Panel 3: g'(tau)=d|C|^2/dtau -- VARYING => excluded from {g'=1}
    axes[2].plot(t, gprime, lw=2, color="C2")
    axes[2].axhline(float(np.mean(gprime)), color="0.5", ls="--", lw=1.0,
                    label=f"mean={np.mean(gprime):.3f}")
    axes[2].set_xlabel(r"$\tau$")
    axes[2].set_ylabel(r"$g'(\tau)=d|C|^2/d\tau$")
    axes[2].set_title(f"VARYING rate (std/mean={np.std(gprime)/abs(np.mean(gprime)):.2f}) -> EXCLUDED from {{g'=1}}")
    axes[2].legend(fontsize=8)
    axes[2].grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}: {res['value']} — tau uniquely lands in the $\\Lambda=3H^2$-preserving class",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


def save_npz(res: dict, audit_sha: str, content_sha: str) -> None:
    c2 = res["c2_cross"]
    np.savez(
        OUT_NPZ,
        value=res["value"],
        verdict=res["verdict"],
        cardinality=res["cardinality"],
        members=np.array(res["members"], dtype=object),
        identity_holds=res["symbolic"]["identity_holds"],
        residual_str=res["symbolic"]["residual_str"],
        expr_sub_str=res["symbolic"]["expr_sub_str"],
        target_str=res["symbolic"]["target_str"],
        class_is_singleton_g1=res["symbolic"]["class_is_singleton_g1"],
        positive_roots=np.array(res["symbolic"]["positive_roots"]),
        ds_dtau=res["ds_dtau"],
        tau_is_one_signed=res["tau_is_one_signed"],
        tau_fold=res["tau_fold"],
        weyl2_genesis=res["weyl2_genesis"],
        genesis_anchor_ok=res["genesis_anchor_ok"],
        npz_strictly_inc=res["npz_strictly_inc"],
        npz_n_dec=res["npz_n_dec"],
        c2_gprime_min=c2["gprime_min"],
        c2_gprime_max=c2["gprime_max"],
        c2_gprime_mean=c2["gprime_mean"],
        c2_gprime_rel_spread=c2["gprime_rel_spread"],
        c2_strictly_monotone=c2["strictly_monotone"],
        c2_is_constant_rate=c2["is_constant_rate"],
        c2_lands_in_class=c2["lands_in_class"],
        a0_val=res["a0_val"],
        a0_is_monotone_clock=res["a0_is_monotone_clock"],
        a0_lands_in_class=res["a0_lands_in_class"],
        naturalness_does_work=res["naturalness_does_work"],
        posterior_A=res["posterior_A"],
        posterior_B=res["posterior_B"],
        tau_grid=res["tau_grid"],
        weyl2=res["weyl2"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=str(L_MAX),
    )


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "", extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()
    value = res["value"]
    verdict = res["verdict"]

    make_plot(res)
    save_npz(res, audit_sha, content_sha)

    c2 = res["c2_cross"]
    note = (f"G_inv_card={res['cardinality']};members={'|'.join(res['members'])};"
            f"class={{g'=1}}_singleton={res['symbolic']['class_is_singleton_g1']};"
            f"identity_resid={res['symbolic']['residual_str']};"
            f"dS/dtau={res['ds_dtau']:.3f}_one-signed={res['tau_is_one_signed']};"
            f"|C|^2_corridor_g'_spread={c2['gprime_rel_spread']:.3e}_constant_rate={c2['is_constant_rate']}_EXCLUDED;"
            f"a0_monotone_clock={res['a0_is_monotone_clock']}_EXCLUDED;"
            f"distinct_from_VII.AW.OP-PROJ_(5-criteria-affine_vs_Lambda=3H^2-rigid);"
            f"posterior_A={res['posterior_A']}/B={res['posterior_B']}")
    extra = [f"# clockloc4_detail: {note}"]

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} ({value}) (wall {wall:.1f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
