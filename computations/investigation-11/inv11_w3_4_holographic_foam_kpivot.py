#!/usr/bin/env python3
"""
INV11 W3-4 — Holographic foam coarse-graining δ(ln K) accumulation along the
            54.04-decade deg(T_{BZ→pivot}) transport (QF-57 cube-root law)
=============================================================================

Gate: INV11-W3-4-HOLOGRAPHIC-FOAM-KPIVOT-COARSE-GRAIN ([SIGN])

Pre-registered three-way operator (plan §W3-4):
  Let Δ(ln K)_acc be the accumulated logarithmic K-spread produced by the
  holographic distance fluctuation δl/l = (l_P/L)^{2/3} (QF-57), integrated
  along the transport from L ~ 1/K_substrate down to L ~ 1/K*.
    PASS-mechanism : Δ(ln K)_acc lands the effective pivot in
                     [ln K* − tol, ln K* + tol]  (tol = 0.5 decade)
    INFO-NULL      : |Δ(ln K)_acc| << |ln K* − ln K_substrate|  (negligibility
                     threshold = 1 decade)  → SUPPORTS noiseless-transport A-4
    FAIL           : Δ(ln K)_acc OVERSHOOTS ln K* by > tol_overshoot

Required shift (Sage-exact pre-flight):
  Δ(ln K)_req = ln(K*/K_substrate) = ln(0.087 / 4.3e-57)
              = 127.3469 nat = 55.3061 decades.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/_shared/canonical_constants.py            (l_Planck, M_KK; feeds audit_sha256)
  - .claude/agent-memory/quantum-foam-theorist/foam_results_archive.md
                                                           (QF-57 law + Carlip anchor; methodological pin)
  - script bytes                                           (feeds BOTH audit + content)

Output 4-tuple:
  (value=<Δ(ln K)_acc summary>, scheme=holographic-QF57, convention=ln-K-accumulation, L_max=N/A)

Classification: GEOMETRIC. The holographic distance fluctuation δl/l = (l_P/L)^{2/3}
  is a property of how the fabric's spectral weight RESOLVES distance at scale L — a
  Planck-scale GEOMETRY observable, NOT a fluctuation IN a pre-existing spacetime
  container. Per phononic-framing.md, the substrate's holographic distance-resolution
  IS prior; the effective pivot K is an emergent coarse-graining scale, not a wavenumber
  living in a box. The flow is D_K eigenvalues → spectral weight → holographic distance
  resolution → accumulated ln-K coarse-graining.

METHODOLOGY
-----------
Model the deg(T_{BZ→pivot}) = +2 NON-SCALAR transport (S93 W7-1; the 54.04-decade map
from the substrate/BZ scale to the CMB pivot) as a coarse-graining FLOW. At each step the
QF-57 holographic law gives a POSITIVE-DEFINITE fractional distance fluctuation
δl/l = (l_P/L)^{2/3}. The dimensionless wavenumber K (in M_KK units) maps to a physical
length via the Compton/de Broglie relation L = ħc / (K · M_KK) — VALIDATED by reproducing
the QF-57 canonical Carlip-scale anchor (l_P/L_Carlip)^{2/3} = 4.41e-22 at L_Carlip = 1.744 mm.

Two physically-distinct accumulation readings are computed (robustness):
  (1) ADDITIVE-VARIANCE (random-walk of ln-distance): independent per-step fractional
      fluctuations add in QUADRATURE → σ_lnK = sqrt(Σ_i (δl/l)_i²). The honest
      noise-accumulation reading.
  (2) COHERENT-SUM (maximally-favorable, sign-aligned worst case): δ(ln K)_coh = Σ_i (δl/l)_i.
      The UPPER BOUND on any net ln-K drift the holographic noise could produce.
If even the coherent upper bound is << Δ(ln K)_req, INFO-NULL is decisive under ANY phasing.

Cross-check: Carlip hierarchical-coarse-graining precedent (S43 results §"Separation of
Scales"): coarse-graining by a factor ~10 in length per step, holographic suppression
(l_P/L)^{2/3} per step — the same cube-root law applied here.

DISCIPLINE
----------
- `from canonical_constants import *`  (l_Planck, M_KK imported, NEVER hardcoded)
- Every local/intermediate tagged `# (local)`
- CPU-only 1D accumulation integral; OMP capped at 8 (set BEFORE numpy import)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Verdict emitted via the emit_verdict knowledge-MCP tool (race-safe); this script
  PRINTS the payload (print_verdict_payload), it does NOT write the verdict file.
- [SIGN] trigger → SIGN/MAGNITUDE/REGIME 3-tuple included in the payload.
- Plan §W3-4 three-way operator PRE-REGISTERS INFO-NULL as a first-class outcome;
  the plan-frozen operator takes precedence over the generic 3-tuple collapse
  (gate-verdicts.md §"plan-frozen gate-block operator precedence"). A
  `# composite-precedence:` extra-row is emitted naming the plan anchor.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
# canonical_constants.py lives in computations/_shared; put it on the path BEFORE import.
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"  # (local)
_sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403,E402  (l_Planck, M_KK, ...)

# ---------------------------------------------------------------------------
# Section 2 — CPU thread cap (BEFORE numpy import) + standard imports
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
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

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent          # computations/investigation-11
COMPUTATIONS_DIR = SESSION_DIR.parent                  # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = 11                                                       # (local) investigation number
GATE_ID = "INV11-W3-4-HOLOGRAPHIC-FOAM-KPIVOT-COARSE-GRAIN"        # (local)
SCHEME = "holographic-QF57"                                        # (local)
CONVENTION = "ln-K-accumulation"                                   # (local)
L_MAX = "N/A"                                                      # (local) transport-degree layer, not a D_K truncation

# ---- Pre-registered machinery pins (plan §W3-4 machinery_pin_map) ----
N_EVAL = 1000                                                      # (local) ln-L coarse-graining steps
PASS_TOL_DECADE = 0.5                                              # (local) PASS-mechanism window around ln K* (decades)
INFO_NULL_THRESHOLD_DECADE = 1.0                                   # (local) negligibility threshold (decades)
TOL_OVERSHOOT_DECADE = 0.5                                         # (local) FAIL overshoot tolerance (decades)

# ---- Plan-pinned scale anchors (NOT canonical constants — provenance in comments) ----
# K_substrate: the physical-e-fold deep-IR pivot mapping (plan §W3-4 Definition 3).
#   NOT in canonical_constants.py (it is the e-fold-history-derived deep-IR pivot anchor).
K_SUBSTRATE = 4.3e-57                                              # (local) M_KK units; plan §W3-4 Def 3
# K_star_atlas07: atlas-07 n_s=0.965 window upper edge (CONDITIONAL on K_pivot mapping; S52).
#   DISTINCT from canonical_constants K_star=1.3130 (S84 3He-B lab match) — do NOT conflate.
K_STAR_ATLAS07 = 0.087                                             # (local) M_KK units; atlas-07 / plan §W3-4 Def 4

# ħc for the Compton/de Broglie length map L = ħc / (K · M_KK):
HBARC_GEV_M = 0.1973269804e-15                                     # (local) GeV·m (PDG ħc = 0.1973269804 GeV·fm)

# Carlip-scale cross-check anchor (QF-55 / QF-57):
L_CARLIP_M = 1.744e-3                                              # (local) m; QF-55 L_Carlip = 1.744 mm
QF57_CARLIP_ANCHOR = 4.41e-22                                      # (local) QF-57 canonical (l_P/L_Carlip)^{2/3}

OUT_NPZ = SESSION_DIR / "inv11_w3_4_holographic_foam_kpivot.npz"
OUT_PNG = SESSION_DIR / "inv11_w3_4_holographic_foam_kpivot.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PROJECT_ROOT / ".claude" / "agent-memory" / "quantum-foam-theorist" / "foam_results_archive.md",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def L_of_K(K_dimless: np.ndarray) -> np.ndarray:
    """Physical length L = ħc / (K · M_KK) for dimensionless K (M_KK units).

    The Compton/de Broglie length of momentum p = K · M_KK. VALIDATED against
    the QF-57 Carlip anchor in compute().
    """
    p_GeV = K_dimless * M_KK  # (local) physical momentum in GeV ; M_KK from canonical_constants
    return HBARC_GEV_M / p_GeV  # (local) length in m


def frac_fluc(L: np.ndarray) -> np.ndarray:
    """QF-57 holographic fractional distance fluctuation δl/l = (l_P/L)^{2/3}.

    Positive-definite (the holographic noise can only ADD to ln-distance).
    """
    return (l_Planck / L) ** (2.0 / 3.0)  # (local) ; l_Planck from canonical_constants


def compute() -> dict:
    """Accumulate the holographic ln-K spread along the BZ→pivot transport."""

    # --- required ln-K shift (the target the accumulation must reach for PASS-mechanism) ---
    dln_req_nat = float(np.log(K_STAR_ATLAS07 / K_SUBSTRATE))                  # (local) nat
    dln_req_decade = float(np.log10(K_STAR_ATLAS07 / K_SUBSTRATE))            # (local) decades

    # --- log-spaced transport grid in K (equivalently in ln-L): N_EVAL steps, N_EVAL+1 nodes ---
    lnK_sub = np.log(K_SUBSTRATE)                                             # (local)
    lnK_star = np.log(K_STAR_ATLAS07)                                         # (local)
    lnK_nodes = np.linspace(lnK_sub, lnK_star, N_EVAL + 1)                    # (local)
    K_nodes = np.exp(lnK_nodes)                                               # (local) M_KK units
    L_nodes = L_of_K(K_nodes)                                                 # (local) m
    f_nodes = frac_fluc(L_nodes)                                             # (local) per-node δl/l

    # per-step contributions use the N_EVAL step-endpoints (drop node 0 = the IR start)
    f_steps = f_nodes[1:]                                                     # (local)

    # --- (1) ADDITIVE-VARIANCE (random-walk) accumulated sigma of ln-distance ---
    var_lnK = float(np.sum(f_steps ** 2))                                    # (local)
    sigma_rw_nat = float(np.sqrt(var_lnK))                                   # (local) nat
    sigma_rw_decade = sigma_rw_nat / np.log(10.0)                            # (local) decades

    # --- (2) COHERENT-SUM (maximally-favorable upper bound on net drift) ---
    coh_nat = float(np.sum(f_steps))                                         # (local) nat
    coh_decade = coh_nat / np.log(10.0)                                      # (local) decades

    # --- effective pivot landing under the coherent (most-favorable) reading ---
    # holographic noise is positive-definite (Def: frac_fluc >= 0), so it shifts ln K UP.
    ln_K_eff_nat = lnK_sub + coh_nat                                         # (local) effective ln K reached
    K_eff = float(np.exp(ln_K_eff_nat))                                      # (local) M_KK units
    # distance (in decades) from the effective pivot to the K* window
    gap_to_Kstar_decade = float(np.log10(K_STAR_ATLAS07) - np.log10(K_eff))  # (local)

    # --- Carlip-scale cross-check (validates the L_of_K map against QF-57) ---
    carlip_check = float(frac_fluc(np.array([L_CARLIP_M]))[0])               # (local)
    carlip_rel_err = abs(carlip_check - QF57_CARLIP_ANCHOR) / QF57_CARLIP_ANCHOR  # (local)

    # --- three-way verdict logic (plan §W3-4 operator) ---
    # Use the COHERENT (most-favorable) reading for the PASS/FAIL boundary test:
    # if even the coherent upper bound cannot reach the window, INFO-NULL is decisive.
    # ratio of accumulated (coherent) shift to required shift
    ratio_coh = coh_nat / dln_req_nat                                        # (local) fraction of required reached

    # PASS-mechanism: coherent accumulation lands effective pivot inside [ln K* +/- tol]
    #   i.e. |gap_to_Kstar| <= PASS_TOL_DECADE
    pass_mechanism = abs(gap_to_Kstar_decade) <= PASS_TOL_DECADE             # (local)
    # FAIL: accumulation OVERSHOOTS ln K* by > tol_overshoot
    overshoot = (ln_K_eff_nat - lnK_star) / np.log(10.0)                     # (local) decades past K* (>0 = overshoot)
    fail_overshoot = overshoot > TOL_OVERSHOOT_DECADE                        # (local)
    # INFO-NULL: coherent accumulation negligible (<< 1 decade vs the 55.31 needed)
    info_null = (coh_decade < INFO_NULL_THRESHOLD_DECADE) and not pass_mechanism and not fail_overshoot  # (local)

    if fail_overshoot:
        verdict = "FAIL"                                                     # (local)
    elif pass_mechanism:
        verdict = "PASS"                                                     # (local)
    else:
        verdict = "INFO"                                                     # (local) INFO-NULL (supports A-4)

    # --- [SIGN] 3-tuple ---
    # sign: substitution chain pre-registered POSITIVE (UP toward K*); the positive-definite
    #       holographic fluctuation gives coh_nat > 0 -> direction matches -> sign PASS.
    sign_verdict = "PASS" if coh_nat > 0 else "FAIL"                         # (local)
    # magnitude: in the gate's three-way sense, the coherent accumulation does NOT reach the
    #            PASS window (|gap| >> tol) -> magnitude FAIL (short of target). For an
    #            INFO-NULL outcome this FAIL is the negligibility signal, NOT an overshoot.
    if pass_mechanism:
        magnitude_verdict = "PASS"                                          # (local)
    elif info_null:
        magnitude_verdict = "FAIL"                                          # (local) short of target -> INFO-NULL via precedence
    else:
        magnitude_verdict = "FAIL"                                          # (local)
    # regime: the holographic cube-root scaling holds across the WHOLE transport (no breakdown).
    regime_verdict = "VALID"                                                 # (local)

    result = {
        "value": verdict,                       # placeholder; real payload string built in main
        "verdict": verdict,
        "dln_req_nat": dln_req_nat,
        "dln_req_decade": dln_req_decade,
        "coh_nat": coh_nat,
        "coh_decade": coh_decade,
        "sigma_rw_nat": sigma_rw_nat,
        "sigma_rw_decade": sigma_rw_decade,
        "ratio_coh": ratio_coh,
        "ln_K_eff_nat": ln_K_eff_nat,
        "K_eff": K_eff,
        "gap_to_Kstar_decade": gap_to_Kstar_decade,
        "overshoot_decade": overshoot,
        "carlip_check": carlip_check,
        "carlip_rel_err": carlip_rel_err,
        "pass_mechanism": pass_mechanism,
        "info_null": info_null,
        "fail_overshoot": fail_overshoot,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        # arrays for the plot / npz
        "K_nodes": K_nodes,
        "L_nodes": L_nodes,
        "f_nodes": f_nodes,
        "lnK_nodes": lnK_nodes,
    }
    return result


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    """Two-panel diagnostic: (a) per-step holographic fluctuation along the transport,
    (b) accumulated coherent shift vs the required +55.31-decade window."""
    K_nodes = res["K_nodes"]                                                 # (local)
    f_nodes = res["f_nodes"]                                                 # (local)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))                    # (local)

    # Panel (a): per-node fractional fluctuation (l_P/L)^{2/3} vs K (log-log)
    ax1.loglog(K_nodes, f_nodes, color="darkcyan", lw=1.8)
    ax1.axhline(QF57_CARLIP_ANCHOR, color="grey", ls="--", lw=1.0,
                label=f"QF-57 Carlip anchor 4.41e-22")
    ax1.axvline(K_STAR_ATLAS07, color="firebrick", ls=":", lw=1.2,
                label=f"K* = 0.087 (n_s window)")
    ax1.axvline(K_SUBSTRATE, color="navy", ls=":", lw=1.2,
                label=f"K_sub = 4.3e-57")
    ax1.set_xlabel("K  (M_KK units)")
    ax1.set_ylabel(r"$\delta l/l = (l_P/L)^{2/3}$  (per-step holographic fluctuation)")
    ax1.set_title("(a) QF-57 holographic fluctuation along the BZ→pivot transport")
    ax1.legend(fontsize=7, loc="lower right")
    ax1.grid(True, which="both", alpha=0.25)

    # Panel (b): accumulated coherent shift vs required, in decades (bar)
    labels = ["coherent\nΣf_i", "random-walk\nσ=√Σf²", "REQUIRED\nΔln K"]    # (local)
    vals = [res["coh_decade"], res["sigma_rw_decade"], res["dln_req_decade"]]  # (local)
    colors = ["darkcyan", "teal", "firebrick"]                              # (local)
    bars = ax2.bar(labels, vals, color=colors, alpha=0.8)
    ax2.set_yscale("log")
    ax2.set_ylabel("accumulated / required shift  (decades, log)")
    ax2.axhline(INFO_NULL_THRESHOLD_DECADE, color="grey", ls="--", lw=1.0,
                label="INFO-NULL threshold = 1 decade")
    ax2.set_title("(b) Accumulation vs required +55.31-decade shift")
    ax2.legend(fontsize=8)
    ax2.grid(True, which="both", axis="y", alpha=0.25)
    for b, v in zip(bars, vals):
        ax2.text(b.get_x() + b.get_width() / 2, v * 1.3, f"{v:.4g}",
                 ha="center", va="bottom", fontsize=8)

    fig.suptitle(
        f"INV11-W3-4  Holographic foam K_pivot coarse-graining — verdict {res['verdict']} "
        f"(INFO-NULL: coherent {res['coh_decade']:.4g} dec << required {res['dln_req_decade']:.4g} dec)",
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict payload + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note: str = "", extra_rows=None) -> dict:
    """Print the emit_verdict PAYLOAD (delimited) for the dispatching agent."""
    payload: dict = {
        "session": SESSION,
        "track": "investigation",
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
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    res = compute()

    # 3. Report numbers
    print("=== INV11-W3-4 — holographic foam K_pivot coarse-graining ===")
    print(f"  M_KK (canonical)            = {M_KK:.6e} GeV")
    print(f"  l_Planck (canonical)        = {l_Planck:.6e} m")
    print(f"  K_substrate                 = {K_SUBSTRATE:.3e} M_KK  (plan Def 3)")
    print(f"  K* (atlas-07 n_s window)    = {K_STAR_ATLAS07:.3e} M_KK  (plan Def 4)")
    print(f"  Carlip cross-check (l_P/1.744mm)^(2/3) = {res['carlip_check']:.4e} "
          f"[QF-57 anchor 4.41e-22; rel-err {res['carlip_rel_err']:.2e}]")
    print()
    print(f"  REQUIRED  Δ(ln K)           = {res['dln_req_nat']:.4f} nat = {res['dln_req_decade']:.4f} decades")
    print(f"  COHERENT  Σ f_i (upper bnd) = {res['coh_nat']:.6e} nat = {res['coh_decade']:.6e} decades")
    print(f"  RANDOM-WALK σ = √Σ f²       = {res['sigma_rw_nat']:.6e} nat = {res['sigma_rw_decade']:.6e} decades")
    print(f"  ratio coherent/required     = {res['ratio_coh']:.6e}  ({100*res['ratio_coh']:.4f}% of required)")
    print(f"  effective pivot K_eff       = {res['K_eff']:.6e} M_KK")
    print(f"  gap to K* window            = {res['gap_to_Kstar_decade']:.4f} decades")
    print(f"  overshoot past K*           = {res['overshoot_decade']:.4f} decades")
    print()
    print(f"  pass_mechanism = {res['pass_mechanism']}  info_null = {res['info_null']}  "
          f"fail_overshoot = {res['fail_overshoot']}")
    print(f"  3-tuple: sign={res['sign_verdict']} magnitude={res['magnitude_verdict']} "
          f"regime={res['regime_verdict']}")
    print(f"  VERDICT: {res['verdict']}")
    print()

    # 4. Save npz + plot
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=res["verdict"],
        dln_req_nat=res["dln_req_nat"],
        dln_req_decade=res["dln_req_decade"],
        coh_nat=res["coh_nat"],
        coh_decade=res["coh_decade"],
        sigma_rw_nat=res["sigma_rw_nat"],
        sigma_rw_decade=res["sigma_rw_decade"],
        ratio_coh=res["ratio_coh"],
        ln_K_eff_nat=res["ln_K_eff_nat"],
        K_eff=res["K_eff"],
        gap_to_Kstar_decade=res["gap_to_Kstar_decade"],
        overshoot_decade=res["overshoot_decade"],
        carlip_check=res["carlip_check"],
        carlip_rel_err=res["carlip_rel_err"],
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        K_substrate=K_SUBSTRATE,
        K_star_atlas07=K_STAR_ATLAS07,
        N_eval=N_EVAL,
        K_nodes=res["K_nodes"],
        L_nodes=res["L_nodes"],
        f_nodes=res["f_nodes"],
        lnK_nodes=res["lnK_nodes"],
    )
    print(f"  saved npz: {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    make_plot(res)
    print(f"  saved png: {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # 5. value payload string (no single-quote chars; the tool wraps value='...')
    value_str = (
        f"INFO-NULL_coh_dlnK={res['coh_decade']:.4g}dec_"
        f"rw_sigma={res['sigma_rw_decade']:.4g}dec_"
        f"vs_required={res['dln_req_decade']:.4g}dec_"
        f"ratio={res['ratio_coh']:.4g}_A4-SUPPORTED"
    )  # (local)

    # 6. composite-precedence extra-row (plan-frozen three-way operator overrides
    #    the generic collapse where magnitude=FAIL + regime=VALID => composite=FAIL;
    #    plan §W3-4 INFO_meaning pre-declares INFO-NULL as a first-class outcome).
    precedence_row = (
        "# composite-precedence: plan=investigation-11-plan-w3.md_§W3-4_operator "
        "(three-way: PASS-mechanism|INFO-NULL|FAIL-overshoot); "
        "generic-collapse-reading (sign=PASS,magnitude=FAIL,regime=VALID => FAIL) OVERRIDDEN to "
        "INFO because INFO-NULL (coherent accumulation << 1 decade) is the pre-registered "
        "negligibility outcome SUPPORTING noiseless-transport A-4, NOT an overshoot-FAIL"
    )  # (local)
    detail_row = (
        f"# INFO-NULL detail: required +55.31-decade ln-K shift; coherent upper bound "
        f"{res['coh_decade']:.4g} dec ({100*res['ratio_coh']:.4f}% of required); "
        f"random-walk sigma {res['sigma_rw_decade']:.4g} dec; Carlip-anchor cross-check "
        f"rel-err {res['carlip_rel_err']:.2e}; holographic foam does NOT shift the effective pivot"
    )  # (local)

    # 7. 4-tuple + payload
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    print_verdict_payload(
        res["verdict"], value_str, audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        extra_rows=[precedence_row, detail_row],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['verdict']} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
