#!/usr/bin/env python3
"""
S85 W1b-8: PLANCK-DESI-2025-ALPHA-S-RECALIBRATION (REAL-DATA REVISION)
========================================================================

Gate: S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION
Trigger: [AUDIT]
Classification: META (canonical-constants recalibration)
Agent: mack-cosmic-bridge

Hypothesis: The framework's canonical alpha_s = -0.0045 +/- 0.0067
(Planck 2018) may need recalibration against post-2018 CMB data.
Gate tests whether the post-2018 best-combined central shifts
more than sigma_Planck_2018/3 from the 2018 value.

Source audit (2026-04-23):

  Plan §W1b-8 originally named {Planck PR4 Tristram 2023, DESI DR2}.
  Verified:
  - Tristram PR4 (arXiv:2309.10034): baseline LCDM only; no alpha_s.
  - DESI 2024 III (arXiv:2404.03000): BAO only; no alpha_s.
  - DESI 2024 VI (arXiv:2404.03002): w_0/w_a/m_nu only; no alpha_s.

  The ACTUAL post-Planck-2018 alpha_s update comes from ACT DR4
  (Aiola et al. 2020, arXiv:2007.07288), which fits extended
  LCDM+dns/dlnk explicitly in Table 5. From that table (page 28):

    Column:         ACT        ACT+WMAP    ACT+Planck   Planck alone
    dns/dlnk:    0.069±0.029  0.0128±0.0081  0.0023±0.0063  -0.0067±0.0067

  The ACT+Planck combination (column 3) is the most-informative
  Planck-inclusive joint fit post-2018. This is the correct source
  for a 2020-era recalibration; the plan's PR4+DR2 named sources
  don't publish alpha_s.

  Note: The canonical alpha_s_canon = -0.0045 +/- 0.0067 traces
  to Planck 2018 VI (Aghanim et al. 1807.06209, TT,TE,EE+lowE+lensing).
  ACT DR4 Table 5 column 4 reports a near-equivalent Planck-alone
  value (-0.0067 +/- 0.0067) using ACT's own tau prior; these two
  Planck-alone values are within 1-sigma.

Substitution chain (Python-verified):

  Step 1: alpha_2018 = -0.0045, sigma_2018 = 0.0067
          (Planck 2018 VI, TT,TE,EE+lowE+lensing, LCDM+alpha_s
           extension).

  Step 2: alpha_2020_ACTPlanck = 0.0023, sigma = 0.0063
          (ACT DR4 Table 5 column 3, ACT+Planck joint, LCDM+dns/dlnk;
           arXiv:2007.07288, Aiola et al. 2020).

  Step 3: Use ACT+Planck as the post-2018 best-combined central
          (it supersedes Planck-alone since it ADDS independent
          ACT data to Planck's likelihood). This means we do NOT
          double-count; we substitute ACT+Planck for "Planck alone
          with post-2018 update" in the combined inference.

  Step 4: Delta_alpha := alpha_2020 - alpha_2018
                       = 0.0023 - (-0.0045)
                       = +0.0068

  Step 5: |Delta_alpha| = 0.0068

  Step 6: |Delta_alpha| / sigma_2018 = 0.0068 / 0.0067 = 1.015
          (just over 1-sigma; framework pin drifted by ~1 sigma
           with post-2018 data).

  Step 7: Compare to plan thresholds:
          PASS iff |Delta| < sigma_2018/3 = 0.00223
          FAIL iff |Delta| > sigma_2018   = 0.00670
          INFO iff sigma/3 <= |Delta| <= sigma
          0.0068 > 0.0067 => FAIL (just barely; by 1.5% over threshold)

  Alternative combinations (for audit robustness):
    (a) ACT+WMAP (Table 5 col 2, Planck-independent): alpha = 0.0128 +/- 0.0081
        inverse-var combined with Planck 2018:
          alpha_comb = 0.002528, sigma = 0.005164
          Delta = 0.00703 => also FAIL (by 5% over)
    (b) ACT alone (Table 5 col 1): 0.069 +/- 0.029
        inverse-var combined with Planck 2018 (ACT-only has near-zero weight):
          alpha_comb = -0.000776, sigma = 0.006530
          Delta = 0.00372 => INFO (between sigma/3 and sigma)

  All three combinations show SHIFT > sigma/3; two of three give
  FAIL (Delta >= sigma). The honest verdict is FAIL.

  Direction: The framework's canonical alpha_s_canon = -0.0045 is
             positively-offset from the post-2018 best-combined value
             by ~1 sigma. Under plan §Cross-wave rule 6, on FAIL the
             canonical constant must be updated. Recommended new pin:
             alpha_s_canon_2020 = +0.0023 +/- 0.0063 (ACT+Planck).

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - downloads/2309.10034.pdf (Tristram PR4)
  - downloads/2404.03000.pdf (DESI 2024 III BAO)
  - downloads/2404.03002.pdf (DESI 2024 VI cosmology)

Output 4-tuple:
  (value=<|Delta_alpha|>=0.0>, scheme=inv-var-weighted-combination, convention=Planck-pivot, L_max=n/a)

Thresholds (plan §W1b-8):
  - PASS iff |Delta_alpha| < sigma_2018/3 (= 2.23e-3)
  - FAIL iff |Delta_alpha| > sigma_2018 (= 6.7e-3)
  - INFO iff sigma/3 <= |Delta| <= sigma
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
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION"          # (local)
SCHEME = "inv-var-weighted-combination"                             # (local)
CONVENTION = "Planck-pivot"                                         # (local)
L_MAX_LABEL = "n/a"                                                 # (local)

# Planck 2018 TT,TE,EE+lowE+lensing (baseline)
ALPHA_2018 = -0.0045                                                # (local) Planck 2018 central
SIGMA_2018 = 0.0067                                                 # (local) Planck 2018 1-sigma

# Thresholds
PASS_FRAC = 1.0 / 3.0                                               # (local) |Delta| < sigma/3
FAIL_FRAC = 1.0                                                     # (local) |Delta| > sigma

# Cached source PDFs (from downloads/)
TRISTRAM_PR4_PDF = PROJECT_ROOT / "downloads" / "2309.10034.pdf"
DESI_III_PDF = PROJECT_ROOT / "downloads" / "2404.03000.pdf"
DESI_VI_PDF = PROJECT_ROOT / "downloads" / "2404.03002.pdf"
ACT_DR4_PDF = PROJECT_ROOT / "downloads" / "2007.07288.pdf"          # Aiola 2020 post-2018 alpha_s
PLANCK_VI_PDF = PROJECT_ROOT / "downloads" / "1807.06209.pdf"        # Aghanim 2020 (canonical alpha_s)

# ACT DR4 Table 5 values (extracted 2026-04-23 from 2007.07288 p.28)
ACT_ALONE_ALPHA = 0.069                                              # (local, col 1)
ACT_ALONE_SIGMA = 0.029                                              # (local, col 1)
ACT_WMAP_ALPHA = 0.0128                                              # (local, col 2, Planck-independent)
ACT_WMAP_SIGMA = 0.0081                                              # (local, col 2)
ACT_PLANCK_ALPHA = 0.0023                                            # (local, col 3, post-2018 best-combined)
ACT_PLANCK_SIGMA = 0.0063                                            # (local, col 3)
ACT_PLANCK_REFERENCE_ALPHA = -0.0067                                 # (local, col 4, ACT's Planck-alone reference)
ACT_PLANCK_REFERENCE_SIGMA = 0.0067                                  # (local, col 4)

OUT_NPZ = SCRIPT_DIR / "s85_w1b_planck_desi_2025_alpha_s_recalibration.npz"
OUT_MD = SCRIPT_DIR / "s85_w1b_planck_desi_2025_alpha_s_recalibration.md"
OUT_PNG = SCRIPT_DIR / "s85_w1b_planck_desi_2025_alpha_s_recalibration.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"

INPUT_FILES = [CANON_PY]
for p in (TRISTRAM_PR4_PDF, DESI_III_PDF, DESI_VI_PDF, ACT_DR4_PDF, PLANCK_VI_PDF):
    if p.exists():
        INPUT_FILES.append(p)


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


def grep_pdf_for_alpha_s(pdf_path: Path) -> dict:
    """Return {'status', 'total_pages', 'hits', 'has_alpha_s_tabulation'}."""
    try:
        from pypdf import PdfReader
    except ImportError:
        return {"status": "pypdf-unavailable"}
    if not pdf_path.exists():
        return {"status": "pdf-missing"}
    import re
    reader = PdfReader(str(pdf_path))                               # (local)
    total_text = "\n".join((p.extract_text() or "") for p in reader.pages)  # (local)
    patterns = [r"alpha_?s\s*[=]", r"α_?s\s*[=]", r"dn_?s\s*/\s*d\s*ln\s*k",
                r"running[-\s]of[-\s]running", r"d²ln"]            # (local)
    hits = {}                                                       # (local)
    for pat in patterns:
        m = re.findall(pat, total_text, re.IGNORECASE)
        if m:
            hits[pat] = len(m)
    return {
        "status": "scanned",
        "total_pages": len(reader.pages),
        "total_chars": len(total_text),
        "hits": hits,
        "has_alpha_s_tabulation": len(hits) > 0,
    }


def compute() -> dict:
    # Scan plan's originally named sources (document their absence)
    pr4_scan = grep_pdf_for_alpha_s(TRISTRAM_PR4_PDF)
    d3_scan = grep_pdf_for_alpha_s(DESI_III_PDF)
    d6_scan = grep_pdf_for_alpha_s(DESI_VI_PDF)

    # Primary analysis: use ACT DR4 ACT+Planck as post-2018 best-combined.
    # This supersedes Planck-alone because it ADDS ACT's independent
    # information to the same parameter inference (no double-counting).
    alpha_primary = ACT_PLANCK_ALPHA                                # (local) 0.0023
    sigma_primary = ACT_PLANCK_SIGMA                                # (local) 0.0063

    Delta_primary = alpha_primary - ALPHA_2018                      # (local) +0.0068
    abs_Delta_primary = abs(Delta_primary)                          # (local)
    frac_primary = abs_Delta_primary / SIGMA_2018                   # (local)

    # Audit-robustness: also compute under alternative combinations
    # (a) Strict-independent inverse-variance: Planck 2018 + ACT+WMAP
    w_2018 = 1.0 / SIGMA_2018 ** 2                                  # (local)
    w_AW = 1.0 / ACT_WMAP_SIGMA ** 2                                # (local)
    alpha_altA = (w_2018 * ALPHA_2018 + w_AW * ACT_WMAP_ALPHA) / (w_2018 + w_AW)  # (local)
    sigma_altA = 1.0 / (w_2018 + w_AW) ** 0.5                       # (local)
    Delta_altA = alpha_altA - ALPHA_2018                            # (local)

    # (b) Planck 2018 + ACT-alone (strict independence; ACT carries little weight)
    w_A = 1.0 / ACT_ALONE_SIGMA ** 2                                # (local)
    alpha_altB = (w_2018 * ALPHA_2018 + w_A * ACT_ALONE_ALPHA) / (w_2018 + w_A)  # (local)
    sigma_altB = 1.0 / (w_2018 + w_A) ** 0.5                        # (local)
    Delta_altB = alpha_altB - ALPHA_2018                            # (local)

    pass_thresh = PASS_FRAC * SIGMA_2018                            # (local) 0.00223
    fail_thresh = FAIL_FRAC * SIGMA_2018                            # (local) 0.00670

    return {
        "value": abs_Delta_primary,
        "alpha_2018": ALPHA_2018,
        "sigma_2018": SIGMA_2018,
        # Primary: ACT+Planck supersedes Planck-alone
        "alpha_primary_2020": alpha_primary,
        "sigma_primary_2020": sigma_primary,
        "Delta_alpha": Delta_primary,
        "abs_Delta_alpha": abs_Delta_primary,
        "fraction_of_sigma": frac_primary,
        # Alternative combinations
        "alpha_altA_planck_actwmap": alpha_altA,
        "sigma_altA_planck_actwmap": sigma_altA,
        "Delta_altA": Delta_altA,
        "alpha_altB_planck_actalone": alpha_altB,
        "sigma_altB_planck_actalone": sigma_altB,
        "Delta_altB": Delta_altB,
        # Raw ACT DR4 Table 5 values
        "ACT_alone_alpha": ACT_ALONE_ALPHA,
        "ACT_alone_sigma": ACT_ALONE_SIGMA,
        "ACT_WMAP_alpha": ACT_WMAP_ALPHA,
        "ACT_WMAP_sigma": ACT_WMAP_SIGMA,
        "ACT_Planck_alpha": ACT_PLANCK_ALPHA,
        "ACT_Planck_sigma": ACT_PLANCK_SIGMA,
        "ACT_ref_alpha": ACT_PLANCK_REFERENCE_ALPHA,
        "ACT_ref_sigma": ACT_PLANCK_REFERENCE_SIGMA,
        # Thresholds
        "pass_threshold": pass_thresh,
        "fail_threshold": fail_thresh,
        # Plan's originally-named (absent) sources
        "pr4_scan": pr4_scan,
        "desi_III_scan": d3_scan,
        "desi_VI_scan": d6_scan,
    }


def evaluate_gate(res: dict) -> str:
    d = res["abs_Delta_alpha"]                                      # (local)
    if d < res["pass_threshold"]:
        return "PASS"
    if d > res["fail_threshold"]:
        return "FAIL"
    return "INFO"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_LABEL} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def write_disposition_md(res: dict, audit_sha: str, content_sha: str,
                         out_path: Path) -> None:
    def row(scan_label, scan):
        hits = scan.get("hits", {})
        return (f"| {scan_label} | {scan.get('status')} | "
                f"{scan.get('total_pages', '—')} | "
                f"{sum(hits.values()) if hits else 0} | "
                f"{'YES' if scan.get('has_alpha_s_tabulation') else 'NO'} |")

    text = f"""# alpha_s recalibration: Planck 2018 → ACT DR4 (post-2018 real data)

**Gate**: {GATE_ID}

## Audit: plan-named sources do NOT tabulate alpha_s

| Source | Status | Pages | alpha_s hits | Has tabulation |
|:-------|:-------|:------|:-------------|:---------------|
{row('Tristram et al. 2023 PR4 (arXiv:2309.10034)', res['pr4_scan'])}
{row('DESI 2024 III BAO (arXiv:2404.03000)',       res['desi_III_scan'])}
{row('DESI 2024 VI Cosmology (arXiv:2404.03002)',  res['desi_VI_scan'])}

Planck PR4 runs baseline-LCDM only; DESI is a BAO/late-universe experiment and doesn't measure inflationary α_s.

## Real post-2018 source: ACT DR4 (Aiola 2020, arXiv:2007.07288 Table 5)

| Combination | α_s = dns/dlnk | σ |
|:-----------|:---------------|:--|
| ACT alone            | {res['ACT_alone_alpha']:+.4f}  | {res['ACT_alone_sigma']:.4f} |
| ACT+WMAP (P-indep)   | {res['ACT_WMAP_alpha']:+.4f}  | {res['ACT_WMAP_sigma']:.4f} |
| **ACT+Planck**       | **{res['ACT_Planck_alpha']:+.4f}**  | **{res['ACT_Planck_sigma']:.4f}** ← primary post-2018 best-combined |
| Planck-alone (ACT's τ prior) | {res['ACT_ref_alpha']:+.4f}  | {res['ACT_ref_sigma']:.4f} |

## Primary analysis: ACT+Planck (post-2018 best) vs Planck 2018 canonical

| Quantity | Value |
|:---------|:------|
| α_2018 (canonical) | {res['alpha_2018']:+.4f} ± {res['sigma_2018']:.4f} (Planck 2018 VI) |
| α_2020 (ACT+Planck) | {res['alpha_primary_2020']:+.4f} ± {res['sigma_primary_2020']:.4f} (Aiola 2020 Table 5 col 3) |
| Δα = α_2020 − α_2018 | **{res['Delta_alpha']:+.6f}** |
| \\|Δα\\| / σ_2018 | **{res['fraction_of_sigma']:.4f}** |

Thresholds (plan §W1b-8): PASS iff |Δα| < σ/3 = {res['pass_threshold']:.6f}; FAIL iff > σ = {res['fail_threshold']:.6f}.

## Audit-robustness: alternative combinations

| Combination | α_combined | σ_combined | Δα | Ratio Δα/σ_2018 |
|:-----------|:-----------|:-----------|:---|:----------------|
| Planck 2018 + ACT+WMAP (altA, inverse-var, Planck-independent) | {res['alpha_altA_planck_actwmap']:+.6f} | {res['sigma_altA_planck_actwmap']:.6f} | {res['Delta_altA']:+.6f} | {abs(res['Delta_altA'])/res['sigma_2018']:.3f} |
| Planck 2018 + ACT-alone (altB, inverse-var) | {res['alpha_altB_planck_actalone']:+.6f} | {res['sigma_altB_planck_actalone']:.6f} | {res['Delta_altB']:+.6f} | {abs(res['Delta_altB'])/res['sigma_2018']:.3f} |

## What this result means

The framework's canonical `alpha_s = -0.0045 ± 0.0067` (Planck 2018) has
drifted by |Δα| = {res['abs_Delta_alpha']:.4f} when post-2018 ACT DR4
data is incorporated. All three treatments (ACT+Planck primary, ACT+WMAP
alt, ACT-alone alt) show |Δα| > σ_2018/3, meaning the canonical pin is
no longer within the PASS band.

Under plan §Cross-wave rule 6, FAIL (|Δα| > σ_2018) triggers a
canonical-constants update. Recommended new pin:
```
alpha_s_canon_2020 = +0.0023 ± 0.0063  (ACT+Planck, Aiola 2020 Table 5)
```
All pre-update S85 verdicts remain permanent per `.claude/rules/gate-verdicts.md`,
but future gates consuming `alpha_s_canon` should use the 2020 value.

## Provenance

- audit_sha256:   {audit_sha}
- content_sha256: {content_sha}
- schema_version: S84+
- Source SHAs pinned at runtime (Planck 2018 VI, Tristram PR4, DESI III, DESI VI, ACT DR4)
"""
    out_path.write_text(text, encoding="utf-8")
    print(f"  MD written: {out_path.name}")


def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(10.0, 5.4))                     # (local)
    x = np.linspace(-0.03, 0.03, 600)                               # (local)

    # Planck 2018 posterior
    pdf_2018 = np.exp(-0.5*((x - res["alpha_2018"]) / res["sigma_2018"])**2)
    pdf_2018 /= pdf_2018.max()
    ax.plot(x, pdf_2018, color="#1a5fb4", lw=2,
            label=rf"Planck 2018: {res['alpha_2018']:+.4f} ± {res['sigma_2018']:.4f}")
    ax.fill_between(x, 0, pdf_2018, color="#1a5fb4", alpha=0.15)

    # ACT+Planck post-2018 posterior (primary)
    pdf_act = np.exp(-0.5*((x - res["alpha_primary_2020"]) / res["sigma_primary_2020"])**2)
    pdf_act /= pdf_act.max()
    ax.plot(x, pdf_act, color="#b03030", lw=2,
            label=rf"ACT+Planck 2020: {res['alpha_primary_2020']:+.4f} ± {res['sigma_primary_2020']:.4f}")
    ax.fill_between(x, 0, pdf_act, color="#b03030", alpha=0.18)

    # Thresholds
    ax.axvspan(res["alpha_2018"] - res["pass_threshold"],
               res["alpha_2018"] + res["pass_threshold"],
               color="#2a7a2a", alpha=0.15,
               label=rf"PASS band (±σ/3 = {res['pass_threshold']:.4f})")
    ax.axvspan(res["alpha_2018"] - res["fail_threshold"],
               res["alpha_2018"] - res["pass_threshold"],
               color="#b08030", alpha=0.08)
    ax.axvspan(res["alpha_2018"] + res["pass_threshold"],
               res["alpha_2018"] + res["fail_threshold"],
               color="#b08030", alpha=0.08,
               label=rf"INFO band (σ/3 to σ)")
    ax.axvline(0, color="k", lw=0.5, alpha=0.4)

    # Δα annotation
    ax.annotate(rf"$\Delta\alpha$ = {res['Delta_alpha']:+.4f} ({res['fraction_of_sigma']:.2f}σ)",
                xy=(res["alpha_primary_2020"], 0.55),
                xytext=(0.01, 0.75),
                arrowprops=dict(arrowstyle="->", color="#333"),
                fontsize=10, color="#333")

    ax.set_xlabel(r"$\alpha_s = dn_s/d\ln k$")
    ax.set_ylabel("posterior (normalized)")
    ax.set_title(rf"{GATE_ID}: |Δα|/σ = {res['fraction_of_sigma']:.3f}")
    ax.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"  PNG written: {out_path.name}")


def main() -> int:
    t0 = time.time()                                                # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: alpha_2018 = {res['alpha_2018']}, sigma_2018 = {res['sigma_2018']}")
    print(f"  Step 2: Plan-named sources: absence audit:")
    for label, scan in [("PR4 Tristram 2023", res["pr4_scan"]),
                        ("DESI 2024 III BAO", res["desi_III_scan"]),
                        ("DESI 2024 VI cosmology", res["desi_VI_scan"])]:
        print(f"          {label}: pages={scan.get('total_pages', '?')}, "
              f"alpha_s tabulation={scan.get('has_alpha_s_tabulation', False)}")
    print(f"  Step 3: Real post-2018 source = ACT DR4 Aiola 2020 (arXiv:2007.07288 Table 5):")
    print(f"          ACT alone    : {res['ACT_alone_alpha']:+.4f} +/- {res['ACT_alone_sigma']:.4f}")
    print(f"          ACT+WMAP     : {res['ACT_WMAP_alpha']:+.4f} +/- {res['ACT_WMAP_sigma']:.4f}")
    print(f"          ACT+Planck   : {res['ACT_Planck_alpha']:+.4f} +/- {res['ACT_Planck_sigma']:.4f}  <-- primary")
    print(f"          Planck alone : {res['ACT_ref_alpha']:+.4f} +/- {res['ACT_ref_sigma']:.4f}  (ACT's tau prior)")
    print(f"  Step 4: Primary (ACT+Planck) vs Planck 2018:")
    print(f"          alpha_2020 = {res['alpha_primary_2020']:+.4f}")
    print(f"          Delta_alpha = {res['alpha_primary_2020']:+.4f} - ({res['alpha_2018']:+.4f}) = "
          f"{res['Delta_alpha']:+.6f}")
    print(f"  Step 5: |Delta| = {res['abs_Delta_alpha']:.6f}")
    print(f"  Step 6: |Delta|/sigma_2018 = {res['fraction_of_sigma']:.4f}")
    print(f"  Step 7: Thresholds: PASS<{res['pass_threshold']:.6f}, FAIL>{res['fail_threshold']:.6f}")
    print(f"          verdict: {verdict}")
    print(f"  Step 8: Audit-robustness (alternative combinations):")
    print(f"          altA Planck+ACT+WMAP: alpha={res['alpha_altA_planck_actwmap']:+.6f}, "
          f"Delta={res['Delta_altA']:+.6f} ({abs(res['Delta_altA'])/res['sigma_2018']:.3f} sigma)")
    print(f"          altB Planck+ACT-alone: alpha={res['alpha_altB_planck_actalone']:+.6f}, "
          f"Delta={res['Delta_altB']:+.6f} ({abs(res['Delta_altB'])/res['sigma_2018']:.3f} sigma)")
    print()

    np.savez(
        OUT_NPZ,
        alpha_2018=np.float64(res["alpha_2018"]),
        sigma_2018=np.float64(res["sigma_2018"]),
        alpha_primary_2020=np.float64(res["alpha_primary_2020"]),
        sigma_primary_2020=np.float64(res["sigma_primary_2020"]),
        Delta_alpha=np.float64(res["Delta_alpha"]),
        abs_Delta_alpha=np.float64(res["abs_Delta_alpha"]),
        fraction_of_sigma=np.float64(res["fraction_of_sigma"]),
        alpha_altA_planck_actwmap=np.float64(res["alpha_altA_planck_actwmap"]),
        sigma_altA_planck_actwmap=np.float64(res["sigma_altA_planck_actwmap"]),
        Delta_altA=np.float64(res["Delta_altA"]),
        alpha_altB_planck_actalone=np.float64(res["alpha_altB_planck_actalone"]),
        sigma_altB_planck_actalone=np.float64(res["sigma_altB_planck_actalone"]),
        Delta_altB=np.float64(res["Delta_altB"]),
        ACT_alone_alpha=np.float64(res["ACT_alone_alpha"]),
        ACT_alone_sigma=np.float64(res["ACT_alone_sigma"]),
        ACT_WMAP_alpha=np.float64(res["ACT_WMAP_alpha"]),
        ACT_WMAP_sigma=np.float64(res["ACT_WMAP_sigma"]),
        ACT_Planck_alpha=np.float64(res["ACT_Planck_alpha"]),
        ACT_Planck_sigma=np.float64(res["ACT_Planck_sigma"]),
        pr4_has_alpha_s=np.array(res["pr4_scan"].get("has_alpha_s_tabulation", False)),
        desi_VI_has_alpha_s=np.array(res["desi_VI_scan"].get("has_alpha_s_tabulation", False)),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    write_disposition_md(res, audit_sha, content_sha, OUT_MD)
    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["abs_Delta_alpha"], SCHEME, CONVENTION, L_MAX_LABEL)
    print(tag)
    append_verdict(verdict, res["abs_Delta_alpha"], audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
