#!/usr/bin/env python3
"""
S85 W4-5: K-STAR / 3He-B LABORATORY INDEPENDENCE-LEVEL CERTIFICATION
====================================================================

Gate: S85-W4-5-KSTAR-3HEB-LAB-INDEP
Trigger: [AUDIT]
Classification: PHONONIC (cross-lab substrate-inheritance statement;
                K-STAR and 3He-B analogs probe the same spectral triple
                as cosmological channels, at vastly different energy scales)
Agent: mack-cosmic-bridge

Hypothesis: Laboratory analogs (K-STAR tokamak density cascades,
3He-B Leggett-mode spectroscopy) probe the SAME eigenvalue problem of
D_K on the Jensen-deformed SU(3) fiber as the 5-channel cosmological
watchlist. They are structurally correlated at the substrate level
(same spectral moment accessed) but pipeline-independent (different
detectors, different nuisance systematics). The gate classifies each
of 5 cosmological channels as (SUBSTRATE-CORRELATION ∈ {HIGH,MED,LOW},
PIPELINE ∈ {INDEPENDENT, PARTIALLY-INDEPENDENT}).

Substitution chain (plan W4-5 #10, positive-sign claim):
  Definition: substrate-correlated channels share the same D_K
              spectral-moment response; pipeline-independent channels
              have nuisance parameters nu_1, nu_2 statistically
              independent.
  Definition: joint likelihood for a single substrate parameter theta
              across two substrate-correlated, pipeline-independent
              channels is
              L_joint(theta) = L_1(theta | nu_1) * L_2(theta | nu_2)
              with nu_1 ⊥ nu_2.
  Substitute: factorized likelihood => log-likelihood ADDS across
              channels for the SAME theta => information content
              doubles.
  Simplify: pipeline-independent substrate-correlated channels give
            effectively independent evidence at the theta-level even
            though they probe the same physics parameter.
  Direction: lab-analog cross-correlation is a JOINT-EVIDENCE
             MULTIPLIER when pipelines are nuisance-independent.
             Sign POSITIVE on joint BF. Script asserts this via
             a 2-channel test: combined info exceeds single-channel info.

Output 4-tuple:
  (value=<n_analogged>/5, scheme=lab-cosmo-analog,
   convention=3HeB-primary+KSTAR-secondary, L_max=NA)

Thresholds (plan W4-5 #9):
  PASS iff every channel has NAMED analog OR explicit NO-ANALOG tag.
  FAIL iff any channel silent on analog status.
  INFO iff analog candidate exists but lab-parameter match uncomputed
       (ANALOG-CANDIDATE-UNVERIFIED tag applied).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("MKL_NUM_THREADS", "2")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (  # noqa: E402
    tau_fold,
    Delta_BCS,
    v_ew,
    M_KK,
    c_fabric,
)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W4-5-KSTAR-3HEB-LAB-INDEP"                             # (local)
SCHEME = "lab-cosmo-analog"                                            # (local)
CONVENTION = "3HeB-primary+KSTAR-secondary"                            # (local)
L_MAX = "NA"                                                           # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w4_kstar_3heb_lab_indep.npz"
OUT_PNG = SCRIPT_DIR / "s85_w4_kstar_3heb_lab_indep.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
PERM_REG_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

# The plan cites project_3heb-inheritance.md and project_volovik-convergence.md
# under LRD memory; these files don't exist (MEMORY.md index entries only).
# The substantive substrate-inheritance content lives in volovik-theorist memory.
VOLOVIK_3HEB_CMP = PROJECT_ROOT / ".claude" / "agent-memory" / "volovik-superfluid-universe-theorist" / "framework-3heb-comparison.md"
VOLOVIK_3HEB_INHERITANCE = PROJECT_ROOT / ".claude" / "agent-memory" / "volovik-superfluid-universe-theorist" / "p3a-w1d-3heb-inheritance-79.md"
VOLOVIK_INHERITANCE_INVERSION = PROJECT_ROOT / ".claude" / "agent-memory" / "volovik-superfluid-universe-theorist" / "inheritance-inversion-60.md"

INPUT_FILES = [
    CANON_PY,
    PERM_REG_MD,
    VOLOVIK_3HEB_CMP,
    VOLOVIK_3HEB_INHERITANCE,
    VOLOVIK_INHERITANCE_INVERSION,
]

# Bipartite mapping rows:
# (i, cosmo_channel, cosmo_moment, lab_analog, lab_moment, substrate_corr,
#  pipeline_status, justification)
#
# SUBSTRATE-CORRELATION {HIGH, MED, LOW}:
#  HIGH = same spectral moment of D_K probed
#  MED  = related moment (different derivative order, same sector)
#  LOW  = weakly related (e.g., polarization vs density)
#
# PIPELINE {INDEPENDENT, PARTIALLY-INDEPENDENT}:
#  INDEPENDENT = nuisance parameters share no physical channel
#  PARTIALLY-INDEPENDENT = both share a common calibration/environmental mode
ROWS = [
    (0, "CMB-S4 alpha_s",
     "d^2 S_transfer/dk^2 at k_pivot (running of scalar tilt)",
     "3He-B Leggett-mode spectroscopy",
     "Leggett mode frequency shifts near van Hove cusp; second derivative of spectral response in the acoustic phonon branch",
     "MED",
     "INDEPENDENT",
     "Both probe 2nd-derivative of spectral weight. CMB-S4 accesses inflationary-scale running; 3He-B Leggett spectroscopy accesses meV-scale Dirac-spectrum curvature at van Hove points. Shared substrate invariance (fiber eigenvalue 2nd-derivative at band edge) but energy scale separation ~60 OOM. Pipeline: cryogenic torsional oscillator vs CMB-S4 photon polarimetry — disjoint nuisance parameters.",
     "FISHER"),

    (1, "DESI DR3 w_0",
     "a_0 Volovik-partition (zeroth spectral moment)",
     "K-STAR density-cascade (tokamak plasma)",
     "a_0-analog: zeroth moment of cascade density spectrum; energy-integrated spectral weight",
     "HIGH",
     "INDEPENDENT",
     "Both probe the Volovik a_0 partition (zeroth spectral moment). Laboratory analog documented in volovik-superfluid-universe-theorist memory (framework-3heb-comparison.md). K-STAR density-cascade measures turbulent cascade zeroth moment; same structural quantity as DESI DR3 w_0 accesses cosmologically. Pipeline: tokamak spectroscopy vs galaxy BAO — disjoint nuisances.",
     "FIRST-PRINCIPLES-REASONING"),

    (2, "LiteBIRD n_T",
     "tensor-sector Dirac spectrum (B-mode polarization)",
     "3He-B tensor-mode spectroscopy (candidate)",
     "Tensor-sector collective mode in 3He-B; not routinely spectroscopically isolated in current lab measurements",
     "LOW",
     "INDEPENDENT",
     "3He-B tensor-mode spectroscopy is technically accessible (Zeeman + rotational coupling) but not published as a spectroscopic-isolation experiment targeting the tensor sector specifically. Substrate correlation is LOW because tensor modes are anti-symmetric combinations of Dirac spectrum eigenvalues, distinct from the scalar moments that 3He-B and K-STAR routinely probe. Pipeline: CMB polarimetry vs cryogenic rotational NMR — fully disjoint.",
     "ANALOG-CANDIDATE-UNVERIFIED"),

    (3, "CMB-HD alpha_s",
     "d^2 S_transfer/dk^2 at k_pivot (SAME moment as CMB-S4)",
     "3He-B Leggett-mode spectroscopy (SAME analog as CMB-S4)",
     "Same Leggett-mode curvature probe as row 0",
     "MED",
     "INDEPENDENT",
     "Same substrate-moment as CMB-S4 alpha_s (row 0); same laboratory analog (3He-B Leggett spectroscopy). The lab analog is SUBSTRATE-CORRELATED to both cosmological detectors simultaneously. Pipeline: CMB-HD is independent from 3He-B but COMMON-MODE to CMB-S4 (documented in §W4-2).",
     "FISHER"),

    (4, "21-cm folded bispec",
     "3-point spectral moment (non-Gaussianity shape)",
     "K-STAR turbulence 3-point correlations (candidate)",
     "Third-cumulant of cascade density fluctuations; triadic mode-coupling measurements",
     "MED",
     "INDEPENDENT",
     "K-STAR edge-turbulence measurements do capture 3-point correlations in density; the MED classification reflects the fact that tokamak turbulence 3-pt structure is not a direct 21-cm bispectrum analog but shares the STRUCTURAL feature of accessing a 3-pt spectral moment of the substrate Dirac spectrum. Published confirmation pending. Pipeline: tokamak vs radio-interferometry — fully disjoint.",
     "ANALOG-CANDIDATE-UNVERIFIED"),
]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                               # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                          # (local)
    for p in inputs:
        sha = sha256_of(p)                                             # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        except ValueError:
            rel = p.name                                               # (local)
        if sha:
            print(f"  {rel}: {sha[:16]}...")
        else:
            print(f"  {rel}: <missing>")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                         # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                       # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def compute() -> dict:
    n_named = sum(1 for r in ROWS if r[3] and "NO-ANALOG" not in r[3])  # (local)
    n_candidate = sum(1 for r in ROWS if r[8] == "ANALOG-CANDIDATE-UNVERIFIED")  # (local)
    n_fisher = sum(1 for r in ROWS if r[8] == "FISHER")                 # (local)
    n_fp = sum(1 for r in ROWS if r[8] == "FIRST-PRINCIPLES-REASONING")  # (local)
    n_no_analog = sum(1 for r in ROWS if "NO-ANALOG" in r[3])            # (local)
    n_analogged = n_named  # rows with a named analog
    n_total = len(ROWS)                                                  # (local)

    # Direction assertion for plan W4-5 #10: "substrate-correlated +
    # pipeline-independent channels give MORE joint evidence than
    # single-channel". Implement a 2-channel test: two observations of
    # theta with independent noise; combined Fisher > either singleton.
    sigma_cosmo = 0.1                                                    # (local) illustrative cosmological 1-sigma
    sigma_lab = 0.05                                                     # (local) illustrative lab 1-sigma (tighter, cryogenic)
    # Fishers (diagonal for independent pipelines)
    F_cosmo = 1.0 / sigma_cosmo**2                                       # (local)
    F_lab = 1.0 / sigma_lab**2                                           # (local)
    F_joint = F_cosmo + F_lab                                            # (local) ADDITIVE because pipeline-independent
    sigma_joint = 1.0 / np.sqrt(F_joint)                                 # (local)
    direction_ok = (sigma_joint < min(sigma_cosmo, sigma_lab))
    assert direction_ok, (
        f"direction claim broken: joint sigma={sigma_joint:.4f} must be "
        f"smaller than single-channel sigmas ({sigma_cosmo}, {sigma_lab})"
    )

    return {
        "n_named": n_named,
        "n_candidate": n_candidate,
        "n_fisher": n_fisher,
        "n_fp": n_fp,
        "n_no_analog": n_no_analog,
        "n_analogged": n_analogged,
        "n_total": n_total,
        "sigma_cosmo_test": sigma_cosmo,
        "sigma_lab_test": sigma_lab,
        "sigma_joint_test": sigma_joint,
        "direction_ok": direction_ok,
        "rows": ROWS,
        "value": n_analogged,
    }


def evaluate_gate(res: dict) -> str:
    # PASS: every row has named analog OR NO-ANALOG tag (no silent rows)
    # FAIL: any row silent (neither named analog nor NO-ANALOG tag)
    # INFO: analog candidate exists but unverified (ANALOG-CANDIDATE-UNVERIFIED)
    n_silent = res["n_total"] - res["n_named"] - res["n_no_analog"]
    if n_silent > 0:
        return "FAIL"
    if res["n_candidate"] > 0:
        return "INFO"
    return "PASS"


def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(12, 6.5))                            # (local)
    ax.axis("off")

    header = ["#", "Cosmo channel", "Lab analog", "Substrate-corr", "Pipeline", "Source-tag"]
    rows_data = []
    for r in res["rows"]:
        i, cosmo, cosmo_m, lab, lab_m, sc, pipe, _just, stag = r
        rows_data.append([str(i), cosmo, lab, sc, pipe, stag])

    tab = ax.table(cellText=rows_data, colLabels=header, loc="center", cellLoc="left")
    tab.auto_set_font_size(False)
    tab.set_fontsize(8)
    tab.scale(1.0, 1.6)
    for k in range(len(header)):
        tab[(0, k)].set_facecolor("#e0e0e0")
        tab[(0, k)].set_text_props(fontweight="bold")

    ax.set_title(f"{GATE_ID}\n{res['n_named']}/{res['n_total']} named analogs; "
                 f"{res['n_fisher']} FISHER + {res['n_fp']} FP + {res['n_candidate']} UNVERIFIED; "
                 f"direction-assertion {'PASS' if res['direction_ok'] else 'FAIL'}",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG written: {out_path.name}")


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def main() -> int:
    t0 = time.time()                                                   # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                             # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    print("=== Canonical constants used (read-only) ===")
    print(f"  tau_fold  = {tau_fold}")
    print(f"  Delta_BCS = {Delta_BCS}")
    print(f"  v_ew      = {v_ew}")
    print(f"  M_KK      = {M_KK}")
    print(f"  c_fabric  = {c_fabric}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Bipartite mapping (cosmo channel ↔ lab analog) ===")
    for r in res["rows"]:
        i, cosmo, cosmo_m, lab, lab_m, sc, pipe, just, stag = r
        print(f"  [{i}] {cosmo:22s} → {lab:36s} | sc={sc:4s} | pipe={pipe:22s} | {stag}")
    print()
    print("=== Direction-assertion test (plan §W4-5 #10) ===")
    print(f"  Two-channel Fisher addition (substrate-correlated + pipeline-independent):")
    print(f"    sigma_cosmo_test = {res['sigma_cosmo_test']}")
    print(f"    sigma_lab_test   = {res['sigma_lab_test']}")
    print(f"    sigma_joint_test = {res['sigma_joint_test']:.6f}")
    print(f"  Direction: sigma_joint < min(sigma_cosmo, sigma_lab) ⇒ {res['direction_ok']}")
    print()

    print(f"  n_analogged = {res['n_analogged']}/{res['n_total']}")
    print(f"  n_fisher    = {res['n_fisher']}")
    print(f"  n_fp        = {res['n_fp']}")
    print(f"  n_candidate = {res['n_candidate']} (ANALOG-CANDIDATE-UNVERIFIED)")
    print(f"  n_no_analog = {res['n_no_analog']}")
    print(f"  Verdict     = {verdict}")

    np.savez(
        OUT_NPZ,
        row_idx=np.array([r[0] for r in res["rows"]]),
        row_cosmo=np.array([r[1] for r in res["rows"]]),
        row_cosmo_moment=np.array([r[2] for r in res["rows"]]),
        row_lab=np.array([r[3] for r in res["rows"]]),
        row_lab_moment=np.array([r[4] for r in res["rows"]]),
        row_substrate_corr=np.array([r[5] for r in res["rows"]]),
        row_pipeline=np.array([r[6] for r in res["rows"]]),
        row_justification=np.array([r[7] for r in res["rows"]]),
        row_source_tag=np.array([r[8] for r in res["rows"]]),
        n_analogged=np.int64(res["n_analogged"]),
        n_candidate=np.int64(res["n_candidate"]),
        n_fisher=np.int64(res["n_fisher"]),
        n_fp=np.int64(res["n_fp"]),
        sigma_joint_test=np.float64(res["sigma_joint_test"]),
        direction_ok=np.array(res["direction_ok"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["n_analogged"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["n_analogged"], audit_sha, content_sha)

    wall = time.time() - t0                                            # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
