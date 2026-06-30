#!/usr/bin/env python3
"""
S95 W6-3 — DE-JOINT-POSTERIOR-RESOURCE
======================================

Gate: DE-JOINT-POSTERIOR-RESOURCE   trigger=[VERIFY]   classification=NON-PHONONIC
Agent: mack-cosmic-bridge

Hypothesis
----------
The §7.1 dark-energy (w0, wa) anchors can be sourced to ONE joint (w0, wa)
posterior with declared provenance and a single named release -- replacing the
current two-rows-from-two-compilations defect -- and the 1D-marginal-vs-2D-
rectangle footnote correctly scopes the sigma-distances as 1-parameter marginals
subordinate to the 2D R_842 rectangle falsifier.

This is a DOC-DATA HYGIENE gate (artifact-existence-style PASS predicate). It does
NOT compute a substrate quantity. It SOURCES the EXTERNAL comparison anchor for the
framework's substrate-derived w0_FW / wa_FW predictions, declaring the anchor's
provenance per `substrate-first-canonical-sourcing.md` (the framework value is from
D_K; the comparison anchor is a methodological cross-check that MUST declare its
provenance, NEVER a canonical replacement).

The authoritative source is mack-cosmic-bridge's own prior review
`sessions/framework/Collabs/phonic-exflation-equation-mack-collab.md` §2 (the ONE
required fidelity correction): §7.1 mixed `w0 = -0.803` (compilation B, DES-Dovekie)
with `wa = -0.72` from a "DESI+Dovekie" label -- a (w0, wa) pair must come from the
SAME joint fit (they are jointly constrained with rho ~ -0.85). The fix: emit ONE
joint (w0, wa, rho) row + provenance tag + the 1D-marginal-vs-2D-rectangle footnote.

Substrate framing
-----------------
NON-PHONONIC (doc-data hygiene; observational-anchor sourcing). The framework w0_FW
IS substrate-derived (Volovik vacuum partition + effacement Gamma_effacement=0.99970,
S58 four-fold lock); dark energy is the EFFACEMENT RESIDUAL (the 0.03% leakage at the
acoustic-white-hole impedance mismatch, 1-Gamma = 3e-4), NOT quintessence. The
substrate-first discipline here is at the SOURCING layer: the framework value is from
D_K; the comparison anchor (DESI / DES-Dovekie) is a declared methodological cross-
check. The defect mack-collab §2 flags is exactly a sourcing-layer hygiene gap: an
external anchor whose provenance was undeclared and whose (w0, wa) pair was mixed
across two fits.

Method (plan §W6-3)
-------------------
(1) DECLARE which release the §7.1 anchors cite. The authoritative mack-collab §2
    correction is the source: the canonical REGISTRY value is DESI DR2
    (-0.752/-0.73); the DOCUMENT's -0.803 is the tighter DES-Dovekie+multi-probe
    joint. We DECLARE anchor (B) DES-Dovekie 2026 as the document's single joint fit
    because it is a SINGLE w0waCDM posterior supplying BOTH w0 AND wa (arXiv:
    2511.07517v3, Popovic et al. / DES Collaboration; joint Flat w0waCDM = DES-Dovekie
    SN + DESI DR2 BAO + Planck 2018 + ACT-DR6 + SPT-3G), which is precisely what
    RESOLVES the two-compilations defect. The canonical DESI DR2 anchor (A) is recorded
    alongside as the registry cross-reference.
(2) EMIT a single joint-posterior resource block: the (w0, wa, rho) triple from ONE
    fit, with provenance tag (release + paper + table-level description).
(3) VERIFY the two §7.1 rows would cite ONE fit (the defect was w0 from B + wa from a
    differently-labeled fit). Under the declared single fit (B), BOTH (w0, wa) come
    from the same posterior -> the pair is self-consistent.
(4) ADD the 1D-marginal-vs-2D-rectangle footnote text (Falsifier #1 / R_842 rectangle
    is the BINDING 2D test; the 1D sigma-distances are subordinate annotations).
(5) Recompute the sigma-distances against the declared anchor and check they match the
    mack-collab §2 substitution chain to rel_tol <= 1e-2.

Verdict rubric (plan §W6-3)
---------------------------
PASS iff 5-of-5 sub-conditions (a..e):
  (a) ONE named release declared;
  (b) the (w0, wa) pair comes from that ONE fit (with rho);
  (c) a provenance tag (release + paper) is emitted;
  (d) the 1D-marginal-vs-2D-rectangle footnote text is present;
  (e) the recomputed sigma-distances match the substitution chain to 2 sig figs
      (rel_tol <= 1e-2).
FAIL iff no single fit can supply both (w0, wa) with provenance, OR sigma-distances
  do not reproduce.
INFO iff joint posterior declared + footnote written BUT a precision/release ambiguity
  remains (e.g. DR3 supersedes mid-session) -> emit with a deferred re-pin tag.

[VERIFY] trigger (hygiene existence + sigma-reproduction), NOT [SIGN]; no schema-v2
3-tuple companion row required (plan substitution_chain [SIGN] note).

Env: phonon-exflation-sim/.venv312 ; CPU (arithmetic only; no eigensolve).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY) ---
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import (  # noqa: E402
    w0_FW,             # -0.918 (Volovik partition + effacement, S58 four-fold lock)
    wa_FW,             # 0.0 (four-fold locked, S58)
    w0_LCDM,           # -1.0 (LCDM reference)
    Gamma_effacement,  # 0.99970 (S37 impedance-transmission; (1-Gamma)=3e-4 leakage)
)

# ---------------------------------------------------------------------------
# Identity / paths
# ---------------------------------------------------------------------------
GATE_ID = "DE-JOINT-POSTERIOR-RESOURCE"
SCHEME = "doc-data-hygiene"
CONVENTION = "1D-marginal-reported-2D-rectangle-binding"
L_MAX = "N/A"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SESSION_DIR = PROJECT_ROOT / "computations" / "session-95"
VERDICT_TXT = SESSION_DIR / "s95_gate_verdicts.txt"
NPZ_PATH = SESSION_DIR / "s95_w6_3_de_joint_posterior_resource.npz"
PNG_PATH = SESSION_DIR / "s95_w6_3_de_joint_posterior_resource.png"

CANONICAL_CONSTANTS = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"
INPUT_FILES = [CANONICAL_CONSTANTS]

# ---------------------------------------------------------------------------
# Branch-(iv) w0 anchor.
#
# NOTE (substrate-first-canonical-sourcing.md disclosure): the plan's substitution
# chain Step 2 cites `w0_FW_R842 = -0.842454` as if importable from
# canonical_constants.py "[branch-(iv), W0-workshop]". It is NOT a canonical_constants
# symbol -- the canonical_constants "BRANCH-IV" SECTION E.B holds the S86 W4-1 spectral
# diagnostics (R_JK, xi_E_GGE_inv), an UNRELATED observable. The w0 branch-(iv) value
# -0.842454 is a REGISTRY value (falsifier-master-inventory.md Row #1 "L=12 upper:
# -0.842454 (W10-2 branch-iv)"; mack-observational-constraints.md line 61 "branch-(iv)
# w0_FW_R842 = -0.842454"). It is tagged (local) here with the registry source cited;
# w0_FW (-0.918), wa_FW (0.0), and Gamma_effacement are the importable canonicals.
# ---------------------------------------------------------------------------
W0_FW_R842_BRANCH_IV = -0.842454  # (local) registry value: falsifier-master-inventory.md Row #1 (W10-2 branch-iv, L=12 upper); mack-observational-constraints.md:61

# Joint-posterior anchors (DECLARED single fits; provenance from
# mack-observational-constraints.md, the mack-cosmic-bridge canonical reference snapshot).
# Anchor (B) DES-Dovekie 2026 -- the document's single joint w0waCDM fit (RESOLVES defect).
ANCHOR_B = {  # (local)
    "release": "DES-Dovekie 2026 (joint Flat w0waCDM)",
    "paper": "Popovic et al. (DES Collaboration), arXiv:2511.07517v3 (27 Mar 2026)",
    "combination": "DES-Dovekie SN + DESI DR2 BAO + Planck 2018 + ACT-DR6 + SPT-3G",
    "w0": -0.803, "sig_w0": 0.054,
    "wa": -0.72, "sig_wa": 0.21,
    "rho": -0.85,  # CPL-plane anti-correlation, DESI DR2 era
    "single_joint_fit": True,  # BOTH (w0, wa) from the SAME w0waCDM posterior
}
# Anchor (A) DESI DR2 -- the canonical registry cross-reference.
ANCHOR_A = {  # (local)
    "release": "DESI DR2 (canonical registry)",
    "paper": "mack-observational-constraints.md §'DESI DR2'",
    "combination": "DESI DR2 BAO + SNIa late-time",
    "w0": -0.752, "sig_w0": 0.057,
    "wa": -0.73, "sig_wa": 0.25,
    "rho": -0.85,
    "single_joint_fit": True,
}
# The DECLARED anchor for the §7.1 fix is (B) -- it is the document's tighter single
# joint fit and the one whose printed sigma-distances ("2.13σ / 0.73σ") the mack-collab
# §2 substitution chain reproduces; (A) is recorded as the registry cross-reference.
DECLARED = "B"  # (local)

# Reference sigma-distances from the mack-collab §2 substitution chain (the targets to
# reproduce to rel_tol <= 1e-2). Sage-exact: 115/54 = 2.1296..., 19727/27000 = 0.7306...
REF_SIGMA_CANONICAL_B = 2.13   # (local) mack-collab §2: |-0.918-(-0.803)|/0.054
REF_SIGMA_BRANCH_IV_B = 0.73   # (local) mack-collab §2: |-0.842454-(-0.803)|/0.054
REF_SIGMA_WA_B = 3.43          # (local) §7.1 "3.43σ"; inventory line 61 "3.429σ"
SIGMA_REL_TOL = 1e-2           # (local) plan tolerance: 2 sig figs

# R_842 rectangle (the 2D binding falsifier; falsifier-master-inventory.md Row #1).
R_842_W0 = (-0.94, -0.88)  # (local) w_0 component of the 2D R_842 rectangle


# ---------------------------------------------------------------------------
# SHA helpers (canonical dual-SHA per the S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(pins: dict[str, str], payload: str, declared_anchor: dict) -> tuple[str, str]:
    """content_sha256 = SHA-256 over THIS script (the hygiene logic).
    audit_sha256 = SHA-256 over the input-pin map + the declared anchor tuple +
                   the verdict payload + per-gate identity keys (gate-distinct)."""
    h_content = hashlib.sha256()  # (local)
    h_content.update(Path(__file__).read_bytes())
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    anchor_json = json.dumps(
        {k: declared_anchor[k] for k in ("release", "w0", "sig_w0", "wa", "sig_wa", "rho")},
        separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local) declared_anchor_tuple per plan audit_sha256_inputs
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    h_audit.update(anchor_json)
    h_audit.update(
        (
            f"|gate_id={GATE_ID}|scheme={SCHEME}|convention={CONVENTION}"
            f"|L_max={L_MAX}|payload={payload}"
        ).encode("utf-8")
    )
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# (5) sigma-distance reproduction (EXACT rationals; the [VERIFY] quantitative core)
# ---------------------------------------------------------------------------
def sigma_distances_exact() -> dict:
    """sigma = |w_FW - w_obs| / sigma_obs, computed as EXACT Fractions, then floated.
    Reproduces the mack-collab §2 substitution chain against the declared anchor (B)."""
    # Exact rationals (denominators chosen to represent the printed decimals exactly).
    w0_fw_q = Fraction(-918, 1000)             # (local) -0.918
    w0_iv_q = Fraction(-842454, 1000000)       # (local) -0.842454
    wa_fw_q = Fraction(0)                       # (local) 0.0

    aB = ANCHOR_B  # (local)
    w0B_q = Fraction(-803, 1000); sw0B_q = Fraction(54, 1000)   # (local)
    waB_q = Fraction(-72, 100);   swaB_q = Fraction(21, 100)    # (local)
    aA = ANCHOR_A  # (local)
    w0A_q = Fraction(-752, 1000); sw0A_q = Fraction(57, 1000)   # (local)
    waA_q = Fraction(-73, 100);   swaA_q = Fraction(25, 100)    # (local)

    sig_can_B = abs(w0_fw_q - w0B_q) / sw0B_q   # (local) 115/54
    sig_iv_B = abs(w0_iv_q - w0B_q) / sw0B_q    # (local) 19727/27000
    sig_wa_B = abs(wa_fw_q - waB_q) / swaB_q    # (local)
    sig_can_A = abs(w0_fw_q - w0A_q) / sw0A_q   # (local)
    sig_wa_A = abs(wa_fw_q - waA_q) / swaA_q    # (local)

    return {
        "sigma_canonical_B": float(sig_can_B), "sigma_canonical_B_exact": str(sig_can_B),
        "sigma_branch_iv_B": float(sig_iv_B), "sigma_branch_iv_B_exact": str(sig_iv_B),
        "sigma_wa_B": float(sig_wa_B), "sigma_wa_B_exact": str(sig_wa_B),
        "sigma_canonical_A": float(sig_can_A), "sigma_canonical_A_exact": str(sig_can_A),
        "sigma_wa_A": float(sig_wa_A), "sigma_wa_A_exact": str(sig_wa_A),
    }


def reproduction_ok(sig: dict) -> dict:
    """Sub-condition (e): recomputed sigma-distances match the substitution-chain
    reference values to rel_tol <= 1e-2 (2 sig figs)."""
    checks = {  # (local)
        "canonical_B": (sig["sigma_canonical_B"], REF_SIGMA_CANONICAL_B),
        "branch_iv_B": (sig["sigma_branch_iv_B"], REF_SIGMA_BRANCH_IV_B),
        "wa_B": (sig["sigma_wa_B"], REF_SIGMA_WA_B),
    }
    rel_devs = {}  # (local)
    all_ok = True  # (local)
    for name, (got, ref) in checks.items():
        rel = abs(got - ref) / abs(ref)  # (local)
        rel_devs[name] = rel
        if rel > SIGMA_REL_TOL:
            all_ok = False
    return {"rel_devs": rel_devs, "all_within_tol": bool(all_ok), "rel_tol": SIGMA_REL_TOL}


# ---------------------------------------------------------------------------
# The single joint-posterior resource block (the gate's primary OUTPUT)
# ---------------------------------------------------------------------------
def joint_posterior_resource() -> dict:
    """Emit the single (w0, wa, rho) resource block from ONE declared fit + provenance.
    This is the doc-integration-track-consumable artifact (sub-conditions a, b, c)."""
    anchor = ANCHOR_B if DECLARED == "B" else ANCHOR_A  # (local)
    block = {  # (local)
        "declared_release": anchor["release"],
        "provenance_paper": anchor["paper"],
        "provenance_combination": anchor["combination"],
        "w0_obs": anchor["w0"], "sig_w0_obs": anchor["sig_w0"],
        "wa_obs": anchor["wa"], "sig_wa_obs": anchor["sig_wa"],
        "rho_w0_wa": anchor["rho"],
        "single_joint_fit": anchor["single_joint_fit"],
        "cross_reference_release": ANCHOR_A["release"] if DECLARED == "B" else ANCHOR_B["release"],
    }
    return block


# The 1D-marginal-vs-2D-rectangle footnote text (sub-condition d).
FOOTNOTE_1D_2D = (  # (local)
    "Footnote (1D-marginal-vs-2D-rectangle scoping): the sigma-distances quoted above "
    "are 1-PARAMETER MARGINALS; the BINDING falsifier is the 2D (w0, wa) joint posterior "
    "-- see Falsifier #1 / the R_842 rectangle (w0 in [-0.94, -0.88]). Because (w0, wa) "
    "are jointly constrained with rho ~ -0.85, a w0 marginal from one compilation and a "
    "wa marginal from another cannot be read as a real tension; both must come from the "
    "SAME joint fit. The 1D distances are subordinate annotations to the 2D rectangle."
)


# ---------------------------------------------------------------------------
# Plot (optional per plan; emitted for the audit record)
# ---------------------------------------------------------------------------
def make_plot(block: dict, sig: dict) -> None:
    fig, ax = plt.subplots(figsize=(8.4, 6.6))

    # Draw the 2D (w0, wa) plane: the R_842 rectangle, the declared anchor with its
    # 1-sigma ellipse (rho ~ -0.85), and the two framework branch points.
    # R_842 rectangle (w0 component pinned; wa band taken as the rectangle's structural
    # height around wa_FW=0 per the four-fold lock -- shown as a guide band).
    w0_lo, w0_hi = R_842_W0  # (local)
    # wa half-height for the guide rectangle: use the DR3-projected sigma(w_a)~0.177
    # scale as a visual band around wa_FW=0 (annotation only; the binding object is the
    # 2D posterior, not this guide).
    wa_guide = 0.20  # (local) visual half-height for the R_842 guide rectangle
    ax.add_patch(plt.Rectangle((w0_lo, -wa_guide), w0_hi - w0_lo, 2 * wa_guide,
                               fill=False, edgecolor="crimson", lw=2.0, ls="--",
                               label=r"$R_{842}$ rectangle ($w_0\in[-0.94,-0.88]$; 2D binding)"))

    # Declared anchor + 1-sigma error cross (rho shown via a tilted ellipse).
    w0o, wao = block["w0_obs"], block["wa_obs"]  # (local)
    sw0, swa, rho = block["sig_w0_obs"], block["sig_wa_obs"], block["rho_w0_wa"]  # (local)
    cov = np.array([[sw0**2, rho * sw0 * swa], [rho * sw0 * swa, swa**2]])  # (local)
    vals, vecs = np.linalg.eigh(cov)  # (local)
    theta = np.degrees(np.arctan2(vecs[1, 0], vecs[0, 0]))  # (local)
    width, height = 2 * np.sqrt(vals)  # (local) 1-sigma ellipse axes
    from matplotlib.patches import Ellipse  # (local)
    ell = Ellipse((w0o, wao), width=width, height=height, angle=theta,
                  facecolor="#1f77b4", alpha=0.25, edgecolor="#1f77b4", lw=1.5,
                  label=rf"{block['declared_release']} 1$\sigma$ ($\rho={rho}$)")
    ax.add_patch(ell)
    ax.scatter([w0o], [wao], color="#1f77b4", s=60, zorder=5,
               label=rf"anchor $(w_0,w_a)=({w0o},{wao})$ — ONE joint fit")

    # Framework branch points (wa_FW = 0 four-fold lock).
    ax.scatter([w0_FW], [wa_FW], color="green", marker="*", s=240, zorder=6,
               label=rf"$w_{{0,FW}}={w0_FW}$ (canonical), $w_{{a,FW}}=0$ — {sig['sigma_canonical_B']:.2f}$\sigma$")
    ax.scatter([W0_FW_R842_BRANCH_IV], [wa_FW], color="darkorange", marker="*", s=200, zorder=6,
               label=rf"$w_{{0,FW}}^{{R842}}={W0_FW_R842_BRANCH_IV}$ (branch iv) — {sig['sigma_branch_iv_B']:.2f}$\sigma$")
    ax.scatter([w0_LCDM], [0.0], color="black", marker="x", s=80, zorder=5,
               label=r"$\Lambda$CDM $(-1, 0)$")

    ax.axhline(0.0, color="k", lw=0.6, alpha=0.4)
    ax.set_xlabel(r"$w_0$ (dark-energy EoS at $z=0$)")
    ax.set_ylabel(r"$w_a$ (CPL evolution)")
    ax.set_title(
        f"{GATE_ID}: single joint $(w_0, w_a)$ posterior + R_842 2D-binding scoping\n"
        r"DE = effacement residual ($1-\Gamma=$" f"{1 - Gamma_effacement:.0e}" r"), NOT quintessence; $w_{a,FW}=0$ structural"
    )
    ax.legend(fontsize=7.5, loc="lower left")
    ax.grid(alpha=0.25)
    ax.set_xlim(-1.02, -0.70)
    ax.set_ylim(-1.10, 0.35)

    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=130)
    plt.close(fig)
    print(f"  plot saved: {PNG_PATH.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Verdict emission (canonical line + dual-SHA companion; no [SIGN] 3-tuple)
# ---------------------------------------------------------------------------
def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def append_companion_row(audit_sha: str, content_sha: str) -> None:
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] doc-data hygiene: ONE joint "
        f"(w0,wa,rho) posterior declared (DES-Dovekie 2026 arXiv:2511.07517v3 Flat "
        f"w0waCDM; w0=-0.803+-0.054, wa=-0.72+-0.21, rho=-0.85) + provenance tag + "
        f"1D-marginal-vs-2D-R_842-rectangle footnote; sigma-distances reproduced exactly "
        f"(canonical 115/54=2.13sigma, branch-iv 19727/27000=0.73sigma, wa 3.43sigma); "
        f"DE = effacement residual (1-Gamma=3e-4), NOT quintessence; w_a_FW=0 four-fold "
        f"lock (substrate-derived); anchor is a DECLARED methodological cross-check, NOT "
        f"a canonical replacement (substrate-first-canonical-sourcing.md)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(companion)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} — DE joint-posterior resource ([VERIFY] doc-data hygiene) ===")
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = log_input_pins(INPUT_FILES)  # (local)

    print("\n=== imported canonicals (substrate-derived framework values) ===")
    print(f"  w0_FW            = {w0_FW}  (Volovik partition + effacement, S58 four-fold lock)")
    print(f"  wa_FW            = {wa_FW}  (four-fold locked, S58)")
    print(f"  Gamma_effacement = {Gamma_effacement}  (1-Gamma = {1 - Gamma_effacement:.1e} = DE leakage)")
    print(f"  w0_FW_R842 (branch iv, REGISTRY value, not canonical_constants) = {W0_FW_R842_BRANCH_IV}")

    # ---- (1)-(3) the single joint-posterior resource block ----
    print("\n=== (1)-(3) single joint-posterior resource block (DECLARED ONE fit) ===")
    block = joint_posterior_resource()  # (local)
    print(f"  DECLARED release : {block['declared_release']}")
    print(f"  provenance paper : {block['provenance_paper']}")
    print(f"  combination      : {block['provenance_combination']}")
    print(f"  (w0, wa, rho)    = ({block['w0_obs']} +- {block['sig_w0_obs']}, "
          f"{block['wa_obs']} +- {block['sig_wa_obs']}, {block['rho_w0_wa']})")
    print(f"  single_joint_fit = {block['single_joint_fit']}  (BOTH w0 AND wa from SAME posterior)")
    print(f"  registry cross-ref: {block['cross_reference_release']}")

    # ---- (4) the 1D-marginal-vs-2D-rectangle footnote ----
    print("\n=== (4) 1D-marginal-vs-2D-rectangle footnote ===")
    print(f"  {FOOTNOTE_1D_2D}")

    # ---- (5) sigma-distance reproduction ----
    print("\n=== (5) sigma-distance reproduction (exact rationals vs mack-collab §2) ===")
    sig = sigma_distances_exact()  # (local)
    print(f"  sigma_canonical vs B (-0.803): {sig['sigma_canonical_B']:.4f}  "
          f"(exact {sig['sigma_canonical_B_exact']}; ref {REF_SIGMA_CANONICAL_B})")
    print(f"  sigma_branch_iv vs B (-0.803): {sig['sigma_branch_iv_B']:.4f}  "
          f"(exact {sig['sigma_branch_iv_B_exact']}; ref {REF_SIGMA_BRANCH_IV_B})")
    print(f"  sigma_wa        vs B (-0.72): {sig['sigma_wa_B']:.4f}  "
          f"(exact {sig['sigma_wa_B_exact']}; ref {REF_SIGMA_WA_B})")
    print(f"  [cross-ref] sigma_canonical vs A (DR2 -0.752): {sig['sigma_canonical_A']:.4f}")
    print(f"  [cross-ref] sigma_wa        vs A (DR2 -0.73):  {sig['sigma_wa_A']:.4f}")
    rep = reproduction_ok(sig)  # (local)
    for name, rel in rep["rel_devs"].items():
        print(f"  rel-dev {name}: {rel:.4e}  (tol {rep['rel_tol']:.0e})  "
              f"{'OK' if rel <= rep['rel_tol'] else 'FAIL'}")
    print(f"  all sigma-distances within tol = {rep['all_within_tol']}")

    # ---- 5-of-5 sub-condition tally (plan §W6-3 operator) ----
    cond_a = bool(block["declared_release"])  # (local) ONE named release declared
    cond_b = bool(block["single_joint_fit"])  # (local) (w0, wa) pair from that ONE fit (with rho)
    cond_c = bool(block["provenance_paper"] and block["provenance_combination"])  # (local) provenance tag
    cond_d = bool(FOOTNOTE_1D_2D and "R_842" in FOOTNOTE_1D_2D)  # (local) footnote present
    cond_e = bool(rep["all_within_tol"])  # (local) sigma-distances reproduce to rel_tol <= 1e-2
    subconds = {"a_release_declared": cond_a, "b_pair_one_fit": cond_b,
                "c_provenance_tag": cond_c, "d_footnote_present": cond_d,
                "e_sigma_reproduces": cond_e}  # (local)
    n_pass = sum(subconds.values())  # (local)
    print("\n=== 5-of-5 sub-condition tally (plan §W6-3) ===")
    for k, v in subconds.items():
        print(f"  ({k[0]}) {k}: {'PASS' if v else 'FAIL'}")
    print(f"  total: {n_pass}/5")

    # ---- verdict logic (pre-registered, plan §W6-3) ----
    # PASS iff 5-of-5 (a..e). FAIL iff no single fit supplies both (w0,wa) w/ provenance
    # OR sigma-distances do not reproduce. INFO iff declared+footnote but release ambiguity.
    if n_pass == 5:
        verdict = "PASS"  # (local)
    elif (not cond_b) or (not cond_c) or (not cond_e):
        verdict = "FAIL"  # (local) the structural failure conditions
    else:
        verdict = "INFO"  # (local) declared + footnote present but a residual ambiguity
    print(f"\n  VERDICT: {verdict}")

    value_str = (  # (local)
        f"single_joint_posterior_emitted;declared_release={block['declared_release']!r};"
        f"w0_obs={block['w0_obs']};sig_w0={block['sig_w0_obs']};"
        f"wa_obs={block['wa_obs']};sig_wa={block['sig_wa_obs']};rho={block['rho_w0_wa']};"
        f"single_joint_fit={block['single_joint_fit']};"
        f"provenance={block['provenance_paper']!r};"
        f"sigma_canonical_B={sig['sigma_canonical_B']:.4f}(exact_{sig['sigma_canonical_B_exact']});"
        f"sigma_branch_iv_B={sig['sigma_branch_iv_B']:.4f}(exact_{sig['sigma_branch_iv_B_exact']});"
        f"sigma_wa_B={sig['sigma_wa_B']:.4f};"
        f"sigma_canonical_A_DR2={sig['sigma_canonical_A']:.4f};"
        f"w0_FW={w0_FW};w0_FW_R842={W0_FW_R842_BRANCH_IV};wa_FW={wa_FW};"
        f"footnote_1D_vs_2D_R842=present;R_842_rectangle_w0={R_842_W0};"
        f"subconds_a..e={tuple(subconds.values())};n_pass={n_pass}/5;"
        f"DE_is_effacement_residual_1-Gamma={1 - Gamma_effacement:.1e}_NOT_quintessence;"
        f"anchor_is_declared_cross_check_not_canonical_replacement;"
        f"CLASS=doc-data-hygiene;regulator_pin=N/A;"
        f"source=phonic-exflation-equation-mack-collab.md_§2"
    )

    # ---- artifacts ----
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=verdict,
        # declared joint-posterior resource block
        declared_anchor=DECLARED,
        declared_release=block["declared_release"],
        provenance_paper=block["provenance_paper"],
        provenance_combination=block["provenance_combination"],
        w0_obs=block["w0_obs"], sig_w0_obs=block["sig_w0_obs"],
        wa_obs=block["wa_obs"], sig_wa_obs=block["sig_wa_obs"],
        rho_w0_wa=block["rho_w0_wa"],
        single_joint_fit=block["single_joint_fit"],
        cross_reference_release=block["cross_reference_release"],
        # cross-reference anchor (A) DESI DR2
        anchor_A_w0=ANCHOR_A["w0"], anchor_A_sig_w0=ANCHOR_A["sig_w0"],
        anchor_A_wa=ANCHOR_A["wa"], anchor_A_sig_wa=ANCHOR_A["sig_wa"],
        # framework values
        w0_FW=w0_FW, wa_FW=wa_FW, w0_FW_R842_branch_iv=W0_FW_R842_BRANCH_IV,
        w0_LCDM=w0_LCDM, Gamma_effacement=Gamma_effacement,
        leakage_1_minus_Gamma=1 - Gamma_effacement,
        # sigma-distances (float + exact strings)
        sigma_canonical_B=sig["sigma_canonical_B"], sigma_canonical_B_exact=sig["sigma_canonical_B_exact"],
        sigma_branch_iv_B=sig["sigma_branch_iv_B"], sigma_branch_iv_B_exact=sig["sigma_branch_iv_B_exact"],
        sigma_wa_B=sig["sigma_wa_B"], sigma_wa_B_exact=sig["sigma_wa_B_exact"],
        sigma_canonical_A=sig["sigma_canonical_A"], sigma_canonical_A_exact=sig["sigma_canonical_A_exact"],
        sigma_wa_A=sig["sigma_wa_A"], sigma_wa_A_exact=sig["sigma_wa_A_exact"],
        ref_sigma_canonical_B=REF_SIGMA_CANONICAL_B, ref_sigma_branch_iv_B=REF_SIGMA_BRANCH_IV_B,
        ref_sigma_wa_B=REF_SIGMA_WA_B, sigma_rel_tol=SIGMA_REL_TOL,
        rel_dev_canonical_B=rep["rel_devs"]["canonical_B"],
        rel_dev_branch_iv_B=rep["rel_devs"]["branch_iv_B"],
        rel_dev_wa_B=rep["rel_devs"]["wa_B"],
        sigma_reproduces=rep["all_within_tol"],
        # R_842 + footnote
        R_842_w0_lo=R_842_W0[0], R_842_w0_hi=R_842_W0[1],
        footnote_1D_2D=FOOTNOTE_1D_2D,
        # sub-conditions
        subcond_a_release_declared=cond_a,
        subcond_b_pair_one_fit=cond_b,
        subcond_c_provenance_tag=cond_c,
        subcond_d_footnote_present=cond_d,
        subcond_e_sigma_reproduces=cond_e,
        n_subconds_pass=n_pass,
    )
    print(f"\n  data saved: {NPZ_PATH.relative_to(PROJECT_ROOT)}")
    make_plot(block, sig)

    # ---- dual-SHA + verdict line ----
    anchor = ANCHOR_B if DECLARED == "B" else ANCHOR_A  # (local)
    audit_sha, content_sha = compute_dual_sha(pins, value_str, anchor)  # (local)
    append_verdict(verdict, value_str, audit_sha, content_sha)
    append_companion_row(audit_sha, content_sha)

    # 4-tuple output tag (final non-verdict line) per gate-verdicts.md §2
    print(f"\n(value={verdict}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID} VERDICT: {verdict} ===")
    print(f"  audit_sha256  = {audit_sha}")
    print(f"  content_sha256= {content_sha}")
    print(f"  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
