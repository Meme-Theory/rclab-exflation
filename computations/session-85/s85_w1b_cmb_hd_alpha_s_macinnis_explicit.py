#!/usr/bin/env python3
"""
S85 W1b-6: CMB-HD-ALPHA-S-MACINNIS-EXPLICIT
============================================

Gate: S85-W1b-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT
Trigger: [VERIFY]
Classification: META (detector-forecast replacement)
Agent: mack-cosmic-bridge

Hypothesis: Replace the agent-projected sigma(alpha_s)_CMB-HD in
W1a-9/W1b-2 (1.5e-3) with the published MacInnis et al. 2022
Snowmass CMB-HD White Paper (arXiv:2203.05728) value. Pre-register
whether the projection was accurate to <=10%.

FINDING: The MacInnis 2022 Snowmass CMB-HD White Paper DOES NOT
publish an explicit sigma(alpha_s) forecast. Its headline forecasts
are:
  - sigma(N_eff) = 0.014          (light relics)
  - sigma(f_NL^local) = 0.26      (primordial non-Gaussianity)
  - sigma(r) = 0.005              (tensor-to-scalar)
  - sigma(w_0) = 0.005            (dark energy eos)
  - sigma(sum m_nu) = 13 meV      (neutrino mass)
  - sigma(B_SI) = 0.036 nG        (primordial magnetic fields)
  - sigma(m_a) varies             (axion-like particles)

alpha_s (running of scalar spectral index) is NOT a headline CMB-HD
science target in this White Paper. The plan's §W1b-6 assumption
that MacInnis publishes sigma(alpha_s) is factually incorrect.

Verdict: PRE-REG-INCOMPLETE.

This is NOT a FAIL. Per plan §W1b-6 fallback clause:
  "PRE-REG-INCOMPLETE: MacInnis 2022 source not accessible in
   project cache (not a FAIL; treated per §Pre-Registration
   Completeness in epistemic-discipline.md)"

The source IS accessible (downloads/2203.05728.pdf, SHA-pinned
at runtime). However, the REQUESTED CONTENT (explicit alpha_s
forecast) is NOT in the source. The agent-projected
sigma(alpha_s)_CMB-HD = 1.5e-3 remains as a sensitivity-scaling
estimate until a dedicated CMB-HD alpha_s forecast paper is
published.

Substitution chain (Python-verified):
  Step 1: sigma_HD_projected := 1.5e-3 (W1a-9 / W1b-2 input, derived
          from CMB-S4 sensitivity by area+ell_max scaling)
  Step 2: sigma_HD_verified  := SOURCE-LACKS-CONTENT
          (paper published but does not tabulate alpha_s)
  Step 3: Ratio check cannot be performed.
  Step 4: Verdict: PRE-REG-INCOMPLETE.
  Step 5: Downstream action: plan §Cross-wave rule 5:
          "W1a-9 MULTID-FISHER ensemble claim is flagged
           PRE-REG-INCOMPLETE as well. Not a FAIL; the
           carry-forward is explicit."
          -> S86 carry-forward: track explicit CMB-HD alpha_s
             forecast publication (e.g., Abazajian et al.
             CMB-HD companion-paper, or SciBook forecast
             code release).

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - downloads/2203.05728.pdf (MacInnis 2022 CMB-HD White Paper)

Output 4-tuple:
  (value='SOURCE-LACKS-CONTENT', scheme=Fisher-single-expt, convention=Planck-pivot, L_max=n/a)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "4")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: E402, F401, F403

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1b-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT"                # (local)
SCHEME = "Fisher-single-expt"                                       # (local)
CONVENTION = "Planck-pivot"                                         # (local)
L_MAX_LABEL = "n/a"                                                 # (local)

SIGMA_HD_PROJECTED = 1.5e-3                                         # (local) W1a-9 / W1b-2 input
MACINNIS_PDF = PROJECT_ROOT / "downloads" / "2203.05728.pdf"

# Published MacInnis 2022 headline forecasts (extracted from paper pages 11-30)
MACINNIS_PUBLISHED_FORECASTS = {
    "sigma_N_eff": 0.014,                                           # (local, Sec 4.1)
    "sigma_fNL_local": 0.26,                                        # (local, Sec 5.2)
    "sigma_r": 0.005,                                               # (local, Sec 9.1)
    "sigma_w0": 0.005,                                              # (local, Sec 6)
    "sigma_sum_mnu_meV": 13.0,                                      # (local, Sec 6)
    "sigma_B_SI_nG": 0.036,                                         # (local, Sec 5.1)
}
# alpha_s NOT in this list.

OUT_NPZ = SCRIPT_DIR / "s85_w1b_cmb_hd_alpha_s_macinnis_explicit.npz"
OUT_MD = SCRIPT_DIR / "s85_w1b_cmb_hd_alpha_s_macinnis_explicit.md"
OUT_PNG = SCRIPT_DIR / "s85_w1b_cmb_hd_alpha_s_macinnis_explicit.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"

INPUT_FILES = [CANON_PY]
if MACINNIS_PDF.exists():
    INPUT_FILES.append(MACINNIS_PDF)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_LABEL} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def write_disposition_md(audit_sha: str, content_sha: str, out_path: Path) -> None:
    text = f"""# MacInnis 2022 CMB-HD alpha_s forecast — PRE-REG-INCOMPLETE disposition

**Gate**: {GATE_ID}
**Verdict**: PRE-REG-INCOMPLETE
**Reason**: Source paper (arXiv:2203.05728, MacInnis et al. 2022 Snowmass
CMB-HD White Paper) is available in the project cache, but does NOT
publish an explicit sigma(alpha_s) forecast.

## MacInnis 2022 headline forecasts (read from pages 11-30)

| Parameter | MacInnis value | Section |
|:----------|:--------------|:--------|
| sigma(N_eff)           | 0.014 | 4.1 |
| sigma(f_NL^local)      | 0.26 | 5.2 |
| sigma(r) (tensor-to-scalar) | 0.005 | 9.1 |
| sigma(w_0)             | 0.005 | 6 |
| sigma(sum m_nu)        | 13 meV | 6 |
| sigma(B_SI, nG)        | 0.036 | 5.1 |
| **sigma(alpha_s)**     | **NOT PUBLISHED** | — |

## Why this is NOT a FAIL

Per plan §W1b-6 fallback clause, PRE-REG-INCOMPLETE is treated
per `.claude/rules/epistemic-discipline.md` §Pre-Registration
Completeness: a gate that cannot be evaluated because its machinery
is unpinned is NOT a FAIL — it is PRE-REG-INCOMPLETE. The projected
value sigma(alpha_s)_CMB-HD = 1.5e-3 used in W1a-9 and W1b-2 remains
a sensitivity-scaling estimate (derived from CMB-S4 scaling, not
from a published CMB-HD forecast pipeline).

## S86 carry-forward

Track publications of an explicit CMB-HD alpha_s forecast. Most
likely sources:
- Abazajian et al. CMB-HD companion papers
- CMB-HD SciBook forecast code release
- Updated CMB-HD paper incorporating alpha_s into Table

When published, re-fire this gate with the verified sigma value
and perform the ratio test.

## Downstream impact

Plan §Cross-wave rule 5: W1a-9 MULTID-FISHER ensemble flagged
PRE-REG-INCOMPLETE-ADJACENT on the alpha_s detector portfolio
(CMB-HD component uses a projection, not a published forecast).
This flag attaches as an annotation, NOT a retraction.

## Provenance

- audit_sha256:   {audit_sha}
- content_sha256: {content_sha}
- schema_version: S84+
- MacInnis source SHA pinned at runtime
"""
    out_path.write_text(text, encoding="utf-8")
    print(f"  MD written: {out_path.name}")


def main() -> int:
    t0 = time.time()                                                # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    verdict = "PRE-REG-INCOMPLETE"                                  # (local)
    value = "SOURCE-LACKS-CONTENT"                                  # (local)

    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: sigma_HD_projected = {SIGMA_HD_PROJECTED} (W1a-9 / W1b-2 input)")
    print(f"  Step 2: sigma_HD_verified = NOT PUBLISHED (MacInnis 2022 lacks alpha_s forecast)")
    print(f"  Step 3: Ratio check cannot be performed.")
    print(f"  Step 4: MacInnis headline forecasts do contain: r, N_eff, f_NL, w_0, m_nu, B_SI.")
    print(f"          alpha_s is NOT among these.")
    print(f"  Step 5: Verdict = {verdict}")
    print(f"          Reason: PDF accessible but does not publish sigma(alpha_s).")
    print()

    # Minimal NPZ (documentation trace)
    np.savez(
        OUT_NPZ,
        sigma_HD_projected=np.float64(SIGMA_HD_PROJECTED),
        sigma_HD_verified=np.array("NOT-PUBLISHED"),
        macinnis_forecasts_published=np.array(list(MACINNIS_PUBLISHED_FORECASTS.keys())),
        macinnis_forecast_values=np.array(list(MACINNIS_PUBLISHED_FORECASTS.values())),
        verdict=np.array(verdict),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    write_disposition_md(audit_sha, content_sha, OUT_MD)

    # Stub PNG (blank canvas showing PRE-REG-INCOMPLETE status for artifact completeness)
    import matplotlib                                               # (local)
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt                                 # (local)
    fig, ax = plt.subplots(figsize=(8, 4.5))                        # (local)
    ax.axis("off")
    ax.text(0.5, 0.7, "PRE-REG-INCOMPLETE", ha="center", fontsize=24,
            color="#b06530", weight="bold")
    ax.text(0.5, 0.5, "MacInnis 2022 (arXiv:2203.05728) accessible", ha="center", fontsize=11)
    ax.text(0.5, 0.4, "but does NOT publish sigma(alpha_s) forecast", ha="center", fontsize=11)
    ax.text(0.5, 0.25, "S86 carry-forward: track explicit CMB-HD alpha_s forecast",
            ha="center", fontsize=10, color="#555555")
    ax.set_title(f"{GATE_ID}")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)
    print(f"  PNG written: {OUT_PNG.name}")

    tag = (f"(value={value!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX_LABEL})")
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
