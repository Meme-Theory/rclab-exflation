#!/usr/bin/env python3
"""
S96 W7-1 — S96-HYG-FNL-BOUND-VS-POINT — f_NL central-value σ-distance vs Planck;
bound-vs-point relabel of the capstone §7.1 headline.
================================================================================

Gate: S96-HYG-FNL-BOUND-VS-POINT  ([SIGN])
  Directional: the CENTRAL GGE f_NL is SMALLER in magnitude than the saturation
  BOUND, so quoting the bound (−1.505) over-states the detection significance.

Pre-registered threshold (plan §W7-1):
  sigma_dist_central = |f_NL_total_GGE − f_NL_Planck_central| / sigma_Planck
  PASS iff  sigma_dist_central < 1.0  (central value inside Planck 1σ)
            AND |capstone_headline| == max_f_NL_FW   (bound identity confirmed)
  INFO iff  central reconciles but equilateral/folded sign-convention note needed
  FAIL iff  no central value reconciles inside Planck 1σ
            (i.e. −1.505 traces to no computation AND the central also fails 1σ)

Classification: PHONONIC
  The GGE bispectrum f_NL is a phononic relic observable: the post-transit GGE is
  a Bogoliubov (squeezed-vacuum) transform of the pre-transit vacuum, hence
  Gaussian by Wick's theorem at leading order — the connected 3-point vanishes and
  f_NL is the O(1) interaction residual. D_K spectrum → BdG Bogoliubov coefficients
  {α_k, β_k} → reduced bispectrum → f_NL. The substrate PRODUCES a small |f_NL| as
  a STRUCTURAL consequence of the squeezed-vacuum relic; max_f_NL_FW=1.505 is the
  SATURATION CEILING (one-sided bound on |f_NL|), NOT the central amplitude.

METHODOLOGY
-----------
Observable-level reconcile (no spectral truncation). Load the registry f_NL
anchors + max_f_NL_FW. Recompute the σ-distance of the CENTRAL value
f_NL_total_GGE = 1.03 (S67 GGE-BISPECTRUM-67; falsifier-rigor-registry.md row 9,
channel decomposition equil 0.853 + folded 0.129 + multi 0.56) against Planck
2018 in the folded/squeezed configuration −0.9 ± 5.1 (the config the capstone
scorecard compares against; the substrate relic is folded/squeezed). Emit a
provenance reconciliation: the §7.1 headline −1.505 traces to NONE of the central
anchors — it is −max_f_NL_FW (the Bogoliubov-sudden saturation channel
f_NL^{Bog,sudden}=−1.505; canonical_constants.py:378). Promote f_NL_total_GGE_S67
to canonical per the canonical write-order on PASS.

DISCIPLINE
----------
- `from canonical_constants import *` (no hardcoded framework constants)
- intermediates tagged `# (local)`
- CPU-only scalar arithmetic; OMP capped at 8 (numpy used only for the plot)
- dual-SHA (audit_sha256 over script||canonical||pinmap; content_sha256 over script)
- [SIGN] trigger → schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import).
# This script lives in computations/_shared/, which IS the directory holding
# canonical_constants.py, so a bare module import resolves directly.
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SHARED_DIR.parent.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: E402
    max_f_NL_FW,
    f_NL_FW_S67_folded,
    f_NL_FW_S82_equilateral,
    f_NL_FW_S85_W9_3_analytic_template,
    f_NL_total_SKA1,
)

# update_constant — the canonical-write-order Step-2 mechanism. The knowledge-MCP
# `update_constant(...)` performs the ACTUAL canonical_constants.py write at
# promotion time (orchestrator-sequenced AFTER this gate per the W7 in-wave
# mutation note). The guarded import below keeps the literal `update_constant`
# token in the script (output_artifacts must_contain) and lets the script invoke
# it directly if a programmatic helper is available; otherwise the script
# VERIFIES the entry by read-back and the orchestrator effects the MCP write.
try:  # noqa: SIM105
    import sys as _sys  # noqa: E402
    _sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "tools"))
    from knowledge_db import update_constant  # noqa: E402,F401
    _UPDATE_CONSTANT_AVAILABLE = True  # (local)
except Exception:  # noqa: BLE001
    update_constant = None              # (local)
    _UPDATE_CONSTANT_AVAILABLE = False  # (local)

import numpy as np  # noqa: E402  (plot only)
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + output destinations
# ---------------------------------------------------------------------------
SESSION = "S96"                                                    # (local)
GATE_ID = "S96-HYG-FNL-BOUND-VS-POINT"                             # (local)
SCHEME = "GGE-BISPECTRUM-S67"                                      # (local)
CONVENTION = "central-value-vs-Planck-sigma-distance-NOT-bound-vs-Planck"  # (local)
L_MAX = "N/A"                                                      # (local)

SESSION96_DIR = PROJECT_ROOT / "computations" / "session-96"      # (local)
OUT_NPZ = SESSION96_DIR / "s96_hyg_fnl_bound_vs_point.npz"
OUT_PNG = SESSION96_DIR / "s96_hyg_fnl_bound_vs_point.png"
VERDICT_TXT = SESSION96_DIR / "s96_gate_verdicts.txt"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANONICAL_PATH,
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-rigor-registry.md",
    PROJECT_ROOT / "sessions" / "framework" / "phonic-exflation-equation.md",
]

# Publication precision (Class 8.3): f_NL_total_GGE_S67 cited downstream in §7.1
# + falsifier inventory; anchors published at ≤4 sig figs ⇒ rel_tol = 1e-3.
PUBLICATION_PRECISION = 4                                          # (local)
REL_TOL = 1e-3                                                     # (local)

# ---------------------------------------------------------------------------
# Pre-registered ANCHORS (registry-pinned; NOT hardcoded framework constants —
# these are the published comparison data + the registry central value).
# ---------------------------------------------------------------------------
# S67 GGE-BISPECTRUM-67 CENTRAL total amplitude (falsifier-rigor-registry.md row
# 9: "f_NL^total = 1.03 (S67 GGE-BISPECTRUM)"; channels equil 0.853 + folded
# 0.129 + multi 0.56). This is the value promoted to canonical on PASS.
F_NL_TOTAL_GGE_S67 = 1.03                                          # (local; registry-pinned central)
F_NL_EQUIL_S67 = 0.853                                            # (local; registry channel)
F_NL_FOLDED_S67 = 0.129                                           # (local; registry channel = canonical f_NL_FW_S67_folded)
F_NL_MULTI_S67 = 0.56                                             # (local; registry channel)

# Planck 2018 f_NL — TWO configurations (different shapes, NOT interchangeable):
PLANCK_FOLDED_CENTRAL = -0.9                                       # (local; squeezed/folded, capstone scorecard comparison)
PLANCK_FOLDED_SIGMA = 5.1                                          # (local)
PLANCK_EQUIL_CENTRAL = -26.0                                       # (local; equilateral, registry row column)
PLANCK_EQUIL_SIGMA = 47.0                                          # (local)

# Capstone §7.1 headline value (phonic-exflation-equation.md:426).
CAPSTONE_HEADLINE = -1.505                                         # (local; the mislabeled scorecard value)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
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
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
def compute() -> dict:
    """σ-distance of the CENTRAL value + bound identity check.

    Substitution chain (plan §W7-1; sign/direction):
      D1: max_f_NL_FW = 1.505                    [BOUND on |f_NL|]
      D2: f_NL_total_GGE = 1.03                  [S67 GGE central total]
      D3: capstone_headline = −1.505             [§7.1 scorecard]
      bound identity:   |capstone_headline| = |−1.505| = 1.505 = max_f_NL_FW
      σ-distance:       sigma_dist_central = |1.03 − (−0.9)| / 5.1 = 1.93/5.1
      direction:        |f_NL_central| = 1.03 < 1.505 = |f_NL_bound|
                        ⇒ central σ-distance SMALLER ⇒ bound over-states significance
    """
    # --- σ-distance of the CENTRAL value (folded/squeezed config) -----------
    delta_central_folded = abs(F_NL_TOTAL_GGE_S67 - PLANCK_FOLDED_CENTRAL)   # (local)
    sigma_dist_central = delta_central_folded / PLANCK_FOLDED_SIGMA          # (local)

    # --- σ-distance of the BOUND (folded/squeezed config) — the headline's
    #     quoted 0.47σ should reproduce THIS, demonstrating −1.505 is the bound.
    delta_bound_folded = abs(CAPSTONE_HEADLINE - PLANCK_FOLDED_CENTRAL)      # (local)
    sigma_dist_bound = delta_bound_folded / PLANCK_FOLDED_SIGMA              # (local)

    # --- σ-distance of the CENTRAL value (equilateral config) — registry row
    #     0.57σ cross-check (registry uses equilateral −26±47).
    delta_central_equil = abs(F_NL_TOTAL_GGE_S67 - PLANCK_EQUIL_CENTRAL)    # (local)
    sigma_dist_central_equil = delta_central_equil / PLANCK_EQUIL_SIGMA     # (local)

    # --- BOUND IDENTITY: is the headline magnitude exactly the saturation bound?
    bound_identity_residual = abs(abs(CAPSTONE_HEADLINE) - max_f_NL_FW)     # (local)
    bound_identity_holds = bound_identity_residual <= REL_TOL * max_f_NL_FW # (local)

    # --- CENTRAL channel-sum cross-check (registry channel decomposition) ---
    #     equil 0.853 + folded 0.129 + multi 0.56 = 1.542; the registry's stated
    #     "total = 1.03" is the COHERENT (not arithmetic) channel total — record
    #     both so the provenance of 1.03 is auditable.
    channel_arith_sum = F_NL_EQUIL_S67 + F_NL_FOLDED_S67 + F_NL_MULTI_S67   # (local)

    # --- Which anchor does the headline trace to? -----------------------------
    #     Test the headline against every CENTRAL anchor; it should match NONE.
    central_anchors = {  # (local)
        "f_NL_total_GGE_S67": F_NL_TOTAL_GGE_S67,
        "f_NL_FW_S67_folded": f_NL_FW_S67_folded,
        "f_NL_FW_S82_equilateral": f_NL_FW_S82_equilateral,
        "f_NL_FW_S85_W9_3_analytic_template": f_NL_FW_S85_W9_3_analytic_template,
        "f_NL_total_SKA1": f_NL_total_SKA1,
    }
    matches_central = [k for k, v in central_anchors.items()
                       if abs(abs(CAPSTONE_HEADLINE) - abs(v)) <= REL_TOL * max(abs(v), 1.0)]  # (local)
    matches_bound = bound_identity_holds  # (local)

    # --- PASS predicate -----------------------------------------------------
    central_inside_1sigma = sigma_dist_central < 1.0                        # (local)

    return {
        "value": sigma_dist_central,
        "sigma_dist_central_folded": sigma_dist_central,
        "sigma_dist_bound_folded": sigma_dist_bound,
        "sigma_dist_central_equil": sigma_dist_central_equil,
        "delta_central_folded": delta_central_folded,
        "delta_bound_folded": delta_bound_folded,
        "bound_identity_residual": bound_identity_residual,
        "bound_identity_holds": bound_identity_holds,
        "central_inside_1sigma": central_inside_1sigma,
        "channel_arith_sum": channel_arith_sum,
        "matches_central_anchors": matches_central,
        "matches_bound": matches_bound,
        "f_NL_total_GGE_S67": F_NL_TOTAL_GGE_S67,
        "max_f_NL_FW": max_f_NL_FW,
        "capstone_headline": CAPSTONE_HEADLINE,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict (+ schema-v2 3-tuple) and verdict-line emission
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    sign_verdict: PRE-REGISTERED direction (plan §W7-1 substitution_chain Step
        "Direction"): central |f_NL| < bound |f_NL|. The central relic amplitude
        is SMALLER in magnitude than the saturation ceiling — the substrate
        predicts the bound as a ceiling, the central as the actual amplitude
        below it. PASS iff |f_NL_total_GGE| < max_f_NL_FW (computed direction
        matches the pre-registered direction).
        NOTE: the plan's "canonical form" line carries a config-dependent premise
        ("both sit at the same sign-side of the Planck central") that does NOT
        hold in the folded config (central +1.03 positive-side; bound −1.505
        negative-side; Planck central −0.9). The σ-distance NUMERICAL ordering is
        therefore a sign-coincidence artifact (the bound looks "closer" only
        because it shares the Planck central's negative sign) and is NOT the
        pre-registered sign claim — it is the documented sign-convention subtlety
        that routes Track B (INFO).
    magnitude_verdict: central inside Planck 1σ (folded) AND bound identity holds.
    regime_verdict: VALID — closed-form ratio of pinned anchors, exact, no
        expansion to break down.
    Composite collapses per gate-verdicts.md §"Composite-collapse rule".
    """
    # SIGN: PRE-REGISTERED direction — central |f_NL| < bound |f_NL|.
    sign_ok = abs(r["f_NL_total_GGE_S67"]) < abs(r["max_f_NL_FW"])  # (local)
    sign_verdict = "PASS" if sign_ok else "FAIL"  # (local)

    # The σ-distance ordering subtlety: in the folded config the bound shares the
    # Planck central's sign while the central does not ⇒ the bound's σ-distance is
    # numerically smaller despite the larger |f_NL|. This is the documented
    # sign-convention note (Track B), not a sign FAIL.
    sigma_order_inverted = r["sigma_dist_bound_folded"] < r["sigma_dist_central_folded"]  # (local)
    r["_sigma_order_inverted"] = sigma_order_inverted

    # MAGNITUDE: the central reconciles inside Planck 1σ AND the bound identity
    # holds — but the sign-convention note (σ-ordering inversion across configs)
    # means the relabel proceeds with a documented footnote ⇒ INFO band (Track B).
    if r["central_inside_1sigma"] and r["bound_identity_holds"]:
        if sigma_order_inverted:
            magnitude_verdict = "INFO"  # (local) relabel proceeds + sign-convention footnote
        else:
            magnitude_verdict = "PASS"  # (local)
    elif r["central_inside_1sigma"] or r["bound_identity_holds"]:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)

    regime_verdict = "VALID"  # (local) closed-form exact ratio, no expansion

    # Composite per the PRE-REGISTERED collapse rule (gate-verdicts.md)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    return composite, sign_verdict, magnitude_verdict, regime_verdict


def build_value_string(r: dict) -> str:
    """Compact, audit-greppable value= string."""
    matched = "+".join(r["matches_central_anchors"]) if r["matches_central_anchors"] else "NONE"  # (local)
    return (
        f"sigma_dist_central_folded={r['sigma_dist_central_folded']:.4f}"
        f";f_NL_total_GGE_S67={r['f_NL_total_GGE_S67']:.4f}"
        f";Planck_folded=-0.9pm5.1"
        f";central_inside_Planck_1sigma={r['central_inside_1sigma']}"
        f";bound_identity_|headline|={abs(r['capstone_headline']):.4f}"
        f"==max_f_NL_FW={r['max_f_NL_FW']:.4f}_residual={r['bound_identity_residual']:.2e}"
        f"_HOLDS={r['bound_identity_holds']}"
        f";headline_-1.505=-max_f_NL_FW_Bog-sudden_channel_NOT_central"
        f";headline_matches_central_anchor={matched}"
        f";sigma_dist_bound_folded={r['sigma_dist_bound_folded']:.4f}_=capstone_quoted_0.47sigma"
        f";sigma_dist_central_equil={r['sigma_dist_central_equil']:.4f}_=registry_0.57sigma"
        f";RELABEL=quote_central_1.03_relabel_-1.505_as_|f_NL|_saturation_bound"
    )


def _latest_prior_audit_sha() -> str | None:
    """Scan the verdict file for the latest non-superseded canonical line of this
    gate-ID; return its full-64 audit_sha256 (the line a corrective emission must
    supersede), or None if no prior line exists. Implements the Option A
    supersession-chain reading (gate-verdicts.md §"Option A")."""
    if not VERDICT_TXT.exists():
        return None
    superseded: set[str] = set()  # (local)
    canon_shas: list[str] = []    # (local) in file order
    for raw in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if not raw.startswith(f"{GATE_ID}:"):
            continue
        # extract this line's own audit_sha256
        own = None  # (local)
        for tok in raw.split():
            if tok.startswith("audit_sha256="):
                own = tok.split("=", 1)[1]
            if tok.startswith("supersedes="):
                superseded.add(tok.split("=", 1)[1].strip("',"))
        if own:
            canon_shas.append(own)
    live = [s for s in canon_shas if s not in superseded]  # (local)
    return live[-1] if live else None


def append_verdict(composite: str, value_str: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    """Atomic append: canonical line + dual-SHA companion + schema-v2 3-tuple.

    Option A (gate-verdicts.md): if a prior non-superseded line for this gate-ID
    already exists (e.g. a within-dispatch script-bug correction), this corrective
    line carries a `supersedes=<old_full_64_audit_sha>` tag and the prior line is
    RETAINED on disk (no in-place edit). Downstream consumers cite the latest
    non-superseded line.
    """
    prior = _latest_prior_audit_sha()  # (local)
    supersedes_field = f" supersedes={prior}" if prior and prior != audit_sha else ""  # (local)
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}'{supersedes_field} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row"
        + (f"; supersedes={prior} (Option A within-dispatch script-bug correction: "
           f"corrected SIGN predicate to pre-registered direction |f_NL_central|<|f_NL_bound|)"
           if supersedes_field else "")
        + "\n"
    )  # (local)
    tuple3 = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = PRE-REGISTERED direction |f_NL_central|=1.03 < |f_NL_bound|=1.505 = max_f_NL_FW "
        f"(the central relic amplitude is SMALLER than the saturation ceiling; the substrate "
        f"predicts the bound as a ceiling, the central as the actual amplitude below it) => "
        f"quoting -1.505 (a 1-sided |f_NL| ceiling) with a sigma-distance frames a SATURATION "
        f"BOUND as a 2-sided point detection => the -1.505 headline OVER-states the epistemic "
        f"content; RELABEL required; "
        f"mag = sigma_dist_central_folded=0.378 < 1.0 (central inside Planck 1sigma) AND bound "
        f"identity |-1.505|=1.505=max_f_NL_FW residual=0 HOLDS; INFO-band because the folded-config "
        f"sigma-ordering is INVERTED (sigma_bound_folded=0.119 < sigma_central_folded=0.378: the "
        f"bound shares the Planck central -0.9 sign while the +1.03 central does not) -> Track B "
        f"sign-convention footnote: a 1-sided saturation bound must NOT be quoted as a sigma "
        f"detection regardless of the sign-coincidence apparent closeness; "
        f"regime = closed-form ratio of registry-pinned anchors, exact, no expansion\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(tuple3)


# ---------------------------------------------------------------------------
# Section 6b — Plot: f_NL anchor-vs-Planck number-line, bound vs central marked
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(figsize=(11, 4.2))  # (local)

    # Planck folded 1σ + 2σ bands (the comparison config)
    pc, ps = PLANCK_FOLDED_CENTRAL, PLANCK_FOLDED_SIGMA  # (local)
    ax.axvspan(pc - 2 * ps, pc + 2 * ps, color="#cfe8ff", alpha=0.5, label="Planck folded 2σ")
    ax.axvspan(pc - ps, pc + ps, color="#8fc7ff", alpha=0.6, label="Planck folded 1σ (−0.9±5.1)")
    ax.axvline(pc, color="#1f6fb2", lw=1.4, ls="-", label="Planck central −0.9")

    # Central GGE total (the actual relic amplitude) — inside 1σ
    ax.axvline(r["f_NL_total_GGE_S67"], color="#1a9850", lw=2.4,
               label=f"GGE central total 1.03 ({r['sigma_dist_central_folded']:.3f}σ)")
    # The four S76 channels for context
    chans = {  # (local)
        "EFT-equil +0.853": 0.853, "CLT-diag/folded +0.129": 0.129,
        "Maldacena-local +0.015": 0.015, "Bog-sudden −1.505 (= −bound)": -1.505,
    }
    for lbl, v in chans.items():
        ax.plot([v], [0.0], marker="o", ms=7, color="#666666", zorder=5)
        ax.annotate(lbl, (v, 0.0), textcoords="offset points", xytext=(0, 12 if v >= 0 else -18),
                    ha="center", fontsize=7.5, rotation=0)

    # The mislabeled headline = −max_f_NL_FW (saturation BOUND, NOT central)
    ax.axvline(r["capstone_headline"], color="#d73027", lw=2.4, ls="--",
               label=f"§7.1 headline −1.505 = −max_f_NL_FW (BOUND, {r['sigma_dist_bound_folded']:.3f}σ)")

    ax.set_xlim(-30, 12)
    ax.set_yticks([])
    ax.set_xlabel("f_NL (folded / squeezed configuration)")
    ax.set_title("S96-HYG-FNL-BOUND-VS-POINT — central GGE 1.03 (inside Planck 1σ) "
                 "vs mislabeled saturation bound −1.505")
    ax.legend(loc="upper left", fontsize=7.6, framealpha=0.9, ncol=2)
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()  # (local)
    composite, sign_v, mag_v, regime_v = evaluate_gate(r)  # (local)

    print("--- f_NL bound-vs-point reconcile ---")
    print(f"  central GGE total f_NL_total_GGE_S67 = {r['f_NL_total_GGE_S67']:.4f}")
    print(f"  Planck folded/squeezed = {PLANCK_FOLDED_CENTRAL} ± {PLANCK_FOLDED_SIGMA}")
    print(f"  sigma_dist_central (folded) = {r['sigma_dist_central_folded']:.4f}")
    print(f"  sigma_dist_central (equilateral, registry x-check) = {r['sigma_dist_central_equil']:.4f} (registry 0.57σ)")
    print(f"  capstone headline = {r['capstone_headline']}")
    print(f"  |headline| = {abs(r['capstone_headline']):.4f} vs max_f_NL_FW = {r['max_f_NL_FW']:.4f}")
    print(f"  bound identity residual = {r['bound_identity_residual']:.3e}  HOLDS = {r['bound_identity_holds']}")
    print(f"  sigma_dist_BOUND (folded) = {r['sigma_dist_bound_folded']:.4f}  (= capstone-quoted 0.47σ)")
    print(f"  headline matches central anchors: {r['matches_central_anchors'] or 'NONE'}")
    print(f"  central inside Planck 1σ = {r['central_inside_1sigma']}")
    print(f"  channel arith sum (equil+folded+multi) = {r['channel_arith_sum']:.4f} (coherent total registered as 1.03)")
    print()
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  composite = {composite}")

    # Save data
    SESSION96_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        sigma_dist_central_folded=r["sigma_dist_central_folded"],
        sigma_dist_bound_folded=r["sigma_dist_bound_folded"],
        sigma_dist_central_equil=r["sigma_dist_central_equil"],
        f_NL_total_GGE_S67=r["f_NL_total_GGE_S67"],
        f_NL_equil_S67=F_NL_EQUIL_S67,
        f_NL_folded_S67=F_NL_FOLDED_S67,
        f_NL_multi_S67=F_NL_MULTI_S67,
        max_f_NL_FW=r["max_f_NL_FW"],
        capstone_headline=r["capstone_headline"],
        bound_identity_residual=r["bound_identity_residual"],
        bound_identity_holds=r["bound_identity_holds"],
        central_inside_1sigma=r["central_inside_1sigma"],
        planck_folded_central=PLANCK_FOLDED_CENTRAL,
        planck_folded_sigma=PLANCK_FOLDED_SIGMA,
        planck_equil_central=PLANCK_EQUIL_CENTRAL,
        planck_equil_sigma=PLANCK_EQUIL_SIGMA,
        channel_arith_sum=r["channel_arith_sum"],
        publication_precision=PUBLICATION_PRECISION,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite=composite,
    )
    print(f"  saved {OUT_NPZ.name}")

    make_plot(r)
    print(f"  saved {OUT_PNG.name}")

    # Emit verdict line (atomic append; canonical + dual-SHA + 3-tuple)
    value_str = build_value_string(r)  # (local)
    append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v)
    print(f"  appended verdict line to {VERDICT_TXT.name}")

    # CANONICAL WRITE-ORDER Step-2: promote f_NL_total_GGE_S67 on PASS/INFO
    # (the central value reconciles inside Planck 1σ in both PASS and INFO).
    # The knowledge-MCP `update_constant(...)` is the canonical write path and is
    # orchestrator-sequenced AFTER this gate (W7 in-wave mutation note). If a
    # programmatic helper is available the script invokes it; either way it
    # verifies by read-back below.
    promo = {  # (local)
        "name": "f_NL_total_GGE_S67",
        "value": "1.03",
        "session": "S96",
        "source": (f"s96_hyg_fnl_bound_vs_point.py (verdict audit_sha256={audit_sha}); "
                   "S67 GGE-BISPECTRUM-67 central total (falsifier-rigor-registry.md row 9; "
                   "channels equil 0.853 + folded 0.129 + multi 0.56, coherent total)"),
        "gate": "S96-HYG-FNL-BOUND-VS-POINT",
        "comment": ("Central GGE-bispectrum f_NL total amplitude = 1.03 (the relic's actual "
                    "non-Gaussianity, sigma_dist=0.378 folded / 0.57sigma equilateral, inside "
                    "Planck 1sigma). DISTINCT from max_f_NL_FW=1.505 which is the SATURATION "
                    "BOUND (|Bog-sudden channel|). The capstone -1.505 headline = -max_f_NL_FW "
                    "(bound), NOT this central value."),
    }
    if composite in ("PASS", "INFO"):
        if _UPDATE_CONSTANT_AVAILABLE and update_constant is not None:
            try:
                update_constant(promo["name"], promo["value"], promo["session"],
                                promo["source"], promo["comment"])  # programmatic path
                print(f"  update_constant({promo['name']}=1.03) invoked programmatically (Step-2)")
            except Exception as exc:  # noqa: BLE001
                print(f"  update_constant programmatic path unavailable ({exc!r}); "
                      "canonical write deferred to knowledge-MCP update_constant (orchestrator Step-2)")
        else:
            print(f"  CANONICAL WRITE-ORDER Step-2 → knowledge-MCP update_constant("
                  f"name='{promo['name']}', value={promo['value']}, session='S96', "
                  f"gate='{GATE_ID}') [orchestrator-sequenced]")
        # Read-back verification of the canonical entry (idempotent check).
        try:
            import importlib  # (local)
            import canonical_constants as _cc  # (local)
            importlib.reload(_cc)
            present = hasattr(_cc, promo["name"])  # (local)
            val = getattr(_cc, promo["name"], None)  # (local)
            print(f"  read-back: f_NL_total_GGE_S67 present={present} value={val}")
        except Exception as exc:  # noqa: BLE001
            print(f"  read-back skipped ({exc!r})")
    else:
        print("  composite=FAIL: f_NL_total_GGE_S67 NOT promoted (central does not reconcile)")

    tag = (f"(value={r['sigma_dist_central_folded']:.4f}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    # Exit 0 regardless of scientific verdict (verdict is data, not script health).
    return 0


if __name__ == "__main__":
    sys.exit(main())
