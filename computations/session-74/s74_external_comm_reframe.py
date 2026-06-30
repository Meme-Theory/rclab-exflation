#!/usr/bin/env python3
"""
S74 W4-S : EXTERNAL-COMM-REFRAME-74
===================================

Audit external-facing documents for hype/PASS language that misrepresents the
framework's evidential status, and propose structural-floor replacements.

Carry-forward: S73B mack-vdd workshop R2 #1 -- external communication must
reflect constraint-mapped status, not rhetorical victories.

Flagged patterns:
  - "0.01 OOM PASS"  (CC hype: a gate passed with a 0.01-OOM delta is only
                      evidence if the prior range is wide; 0.01 OOM is a
                      re-labeled floor, not a discriminator)
  - "n_s PASS Planck 1-sigma"  (prediction-observation distance treated as
                                rhetorical victory without stating the
                                pre-registered band or Bayes factor penalty)
  - "131.8 GeV matches to 5%"  (the "matches to X%" locution hides the
                                absence of resolution; 5% of 125 GeV is 6.3
                                GeV, wider than the prior range for most
                                BSM Higgs-like states)
  - "within 1.9 sigma"  (flexibility posturing; 1.9-sigma is a TENSION,
                         not a PASS, and the framework has zero free
                         parameters so there is no slack to absorb it)
  - "strongest quantitative result"  (rhetorical superlative; violates the
                                      structural-floor vocabulary rule)
  - "honest probability assessment" (narrative probability unsupported by
                                     constraint surface)

Pre-registered gate:
  PASS if >= 5 instances of flagged language replaced
  INFO if 2-4
  FAIL if 0-1

NOTE: This script ONLY produces an audit table. It does NOT edit the
external-facing documents. Replacement proposals are for W4 review.
"""

import sys
import os
import numpy as np

# Canonical constants import (per project rule)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    m_H_obs,           # 125.1 GeV (PDG 2024)
    planck_ns,         # 0.9649 (Planck 2018)
    planck_ns_err,     # 0.0042 (Planck 2018 1-sigma)
)

# ------------------------------------------------------------------
# Flagged instances: (doc_path, line, old_phrase, new_phrase, category)
# ------------------------------------------------------------------

# Each entry is (file, approx_line, category, OLD snippet, NEW snippet, rationale)

INSTANCES = [
    # ---------- phonon_exflation_cosmology.md ----------
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 451,
        "category": "n_s sigma-hype",
        "old": ("This is 1.9sigma from the Planck observed value n_s = 0.9649 +/- 0.0042, "
                "with zero free parameters."),
        "new": ("Gate verdict: n_s(Hubble slow-roll) = 0.9567 vs Planck 0.9649 +/- 0.0042. "
                "Delta/sigma = 1.95; the predicted value lies outside the Planck 1-sigma "
                "band but inside the 2-sigma band. Interpretation is conditional on the "
                "tau-to-N transfer, which is uncomputed; until that transfer is fixed the "
                "result is a structural benchmark, not a discriminator."),
        "rationale": ("'1.9 sigma from Planck' is tension, not agreement; framing it as "
                      "closeness hides that the predicted value is outside the 1-sigma band "
                      "and that the scale transfer tau->N is unresolved."),
    },
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 557,
        "category": "m_H within-X%-hype",
        "old": ("The Higgs mass prediction from the Gilkey ratio alone gives "
                "m_H(tree) = 134 GeV, within 7% of observation."),
        "new": ("Gate verdict: m_H(tree, Gilkey ratio a_4/a_2) = 134 GeV vs PDG 125.1 GeV. "
                "Absolute deviation: 8.9 GeV (7.1%). The tree-level value is a structural "
                "floor of the spectral-action construction; the 2-loop RGE prediction of "
                "160 GeV is the surviving prediction-layer number, which overshoots the "
                "observed value by 28% and requires KK-threshold corrections "
                "(delta_BCS in [0.20, 0.30]) that are not derived from first principles."),
        "rationale": ("'within 7% of observation' treats the distance as small, but 7% "
                      "of 125 GeV is 8.9 GeV -- wider than the entire experimental "
                      "uncertainty and wider than most BSM Higgs-like prior ranges. "
                      "The 2-loop answer (160 GeV) is the real prediction, and it is "
                      "not 'close'."),
    },
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 558,
        "category": "n_s sigma-hype",
        "old": ("The spectral index n_s = 0.9567 from the Hubble slow-roll extraction "
                "of the spectral action at the fold lies within 1.9sigma of the Planck "
                "measurement, with zero free parameters"),
        "new": ("Gate verdict: n_s(spectral action slow-roll at fold) = 0.9567. Planck "
                "2018: n_s = 0.9649 +/- 0.0042. Delta/sigma = 1.95, outside the 1-sigma "
                "band. The pre-registered band for a passing verdict was [0.955, 0.975]; "
                "the value sits 0.0017 inside the lower edge of that band but outside "
                "Planck's own 1-sigma interval. Alternative spectral methods (Gilkey "
                "ratio, discrete modes) give 0.76-0.80, well outside any physical prior. "
                "This is a scheme-dependent structural floor, not a settled prediction."),
        "rationale": ("'within 1.9 sigma' is standard hype language; the constraint-map "
                      "reading is: inside the framework's own pre-registered band, "
                      "outside Planck's 1-sigma band, and scheme-dependent across "
                      "different extraction methods by >20%."),
    },
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 503,
        "category": "m_H within-X%-hype",
        "old": ("m_H(tree) = 134 +/- 7 GeV, within 7.1% of the observed 125.1 GeV "
                "with zero free parameters."),
        "new": ("m_H(tree) = 134 +/- 7 GeV. Gate verdict: tree-level prediction lies "
                "7.1% (8.9 GeV) above PDG 125.1 GeV; the 1-sigma tree-level uncertainty "
                "envelope (127-141 GeV) does not include the observed value. The "
                "surviving reconciliation route is KK-threshold corrections, which "
                "are themselves an additional model layer with their own uncomputed "
                "priors. Structural-floor assessment: within-band at the 7% tolerance, "
                "discriminating only if the prior range exceeds 30%."),
        "rationale": ("'within 7.1%' is an undisclosed prior-range claim; without "
                      "stating the prior, the percentage is uninterpretable. 7% of 125 "
                      "GeV is larger than the experimental uncertainty band of Higgs "
                      "mass (~0.17 GeV)."),
    },
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 606,
        "category": "rhetorical superlative",
        "old": ("The Higgs mass prediction -- 134 GeV at tree level from zero geometric "
                "free parameters across a prediction space spanning five orders of "
                "magnitude -- is the strongest quantitative result."),
        "new": ("The Higgs mass prediction -- 134 GeV at tree level from zero geometric "
                "free parameters -- is a structural floor of the spectral-action "
                "construction. The 1-sigma tree-level envelope (127-141 GeV) does not "
                "contain the observed 125.1 GeV; the 2-loop prediction of 160 GeV "
                "overshoots observation by 28%. The prior range is model-dependent and "
                "has not been computed as a probability envelope; the five-OOM range is "
                "a parameter-space volume, not a Bayesian prior. Label: structural-floor "
                "result, prediction layer uncomputed."),
        "rationale": ("'strongest quantitative result' is a rhetorical superlative and "
                      "mis-identifies the 5-OOM 'prediction range' as evidence; this "
                      "range is the parameter-space volume before the spectral-action "
                      "construction fixes it, not a Bayesian prior, and the 28% "
                      "deviation at 2-loop is the real prediction-layer number."),
    },
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 595,
        "category": "summary table percent-match",
        "old": ("| Higgs mass (tree-level) | 134 GeV | 125.1 GeV | 7.1% | a_4/a_2 = 0.414 "
                "via Gilkey |"),
        "new": ("| m_H (tree, a_4/a_2)   | 134 GeV | 125.1 GeV | 7.1% (8.9 GeV) | "
                "Structural floor | Spectral action "
                "zeroth pass; outside PDG band, no free parameters |"),
        "rationale": ("Add an explicit layer label (Structural floor vs Prediction layer) "
                      "and show the absolute deviation (8.9 GeV) alongside the percent. "
                      "A table that shows only '7.1%' compresses the prior-range "
                      "argument out of view."),
    },
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 596,
        "category": "summary table percent-match",
        "old": ("| Higgs mass (2-loop RG) | 160 GeV | 125.1 GeV | 28% | CCM + SM RGE; "
                "KK threshold path to 125 |"),
        "new": ("| m_H (2-loop RGE) | 160 GeV | 125.1 GeV | 28% (35 GeV) | "
                "Prediction layer | Overshoots PDG; "
                "reconciliation route (delta_BCS in [0.20, 0.30]) is a separate uncomputed "
                "model layer |"),
        "rationale": ("Same layer-labeling as above; plus make explicit that the "
                      "reconciliation route is an additional assumption."),
    },
    {
        "doc": "phonon_exflation_cosmology.md",
        "line": 597,
        "category": "summary table sigma-hype",
        "old": ("| Spectral index n_s | 0.9567 | 0.9649 +/- 0.0042 | 1.9 sigma | "
                "Hubble slow-roll from S(tau) |"),
        "new": ("| n_s (SA slow-roll) | 0.9567 | 0.9649 +/- 0.0042 | 1.95 sigma (outside 1-sig, inside 2-sig) | "
                "Structural floor, scheme-dep | "
                "Alternative extractions give 0.76-0.80; tau-to-N transfer is uncomputed. |"),
        "rationale": ("Same layer-labeling; make the tension explicit ('outside 1-sigma') "
                      "and state the scheme dependence in the same cell."),
    },
    # ---------- README.md ----------
    {
        "doc": "README.md",
        "line": 5,
        "category": "narrative probability",
        "old": ("Built over ~10 weeks across 51 structured research sessions using "
                "Claude Code's agent orchestration. 28 specialized AI agents, 12 skills, "
                "33 research domains, 630+ computation scripts, 12 proven theorems at "
                "machine epsilon, 21 closed stabilization mechanisms, and an honest "
                "probability assessment: **2-4%** that the framework describes reality."),
        "new": ("Built over ~70+ structured research sessions. The project produces a "
                "constraint-mapped surface: structural walls (permanent theorems), "
                "closed mechanism families, and surviving routes with pre-registered "
                "gates. The framework's evidential status is the shape of this surface, "
                "not a probability number; see sessions/evoi-framework.md for current "
                "pre-registered gates and surviving regions."),
        "rationale": ("'honest probability assessment: 2-4%' propagates a narrative-"
                      "probability methodology that was explicitly retired in favor of "
                      "constraint-surface reporting. The effort-based EVOI framework "
                      "tracks what has been mapped, not a single scalar."),
    },
    {
        "doc": "README.md",
        "line": 56,
        "category": "percent-agreement hype",
        "old": ("| **Agreement** | **0.7%** | **Zero free parameters** |"),
        "new": ("| Internal consistency | Delta(T_acoustic / T_Gibbs) = 0.007 | "
                "Structural identity, internal check (not observational) |"),
        "rationale": ("'0.7% Agreement' reads like an observational match; in fact "
                      "T_acoustic and T_Gibbs are both internal derived quantities from "
                      "the same spectrum. The 0.7% is an internal consistency check, "
                      "not a prediction vs data comparison."),
    },
    {
        "doc": "README.md",
        "line": 286,
        "category": "narrative probability trajectory",
        "old": ("Prior (theoretical):                       2-5%\n"
                "After KO-dim=6 (Sessions 7-8):           10-15%\n"
                "After SM quantum numbers (Session 7):     25-35%\n"
                "After Baptista geometry (Session 17b):    40-50%\n"
                "After Session 19d (TT discovery):         45-52%    <-- PEAK\n"
                "After Session 20b (TT Casimir closed):    32-40%\n"
                "After K-1e DECISIVE CLOSURE (Session 23): 8% (panel), 5% (Sagan)\n"
                "After V-1 CLOSED (Session 24):            5% (panel), 3% (Sagan)\n"
                "After Session 26 P1/P2/P3:               3-5% (panel), 2-4% (Sagan)\n"
                "After Session 51 (SA-Goldstone):          2-4% (panel), 2-4% (Sagan)"),
        "new": ("Probability trajectory retired (S73-S74 methodology update). The "
                "framework's evidential state is now reported as a constraint surface: "
                "proven structural walls, closed mechanism families, surviving routes, "
                "and pre-registered gates with current verdicts. See "
                "sessions/evoi-framework.md for the live EVOI-prioritized gate list "
                "and summary/atlas-*.md for the constraint atlas."),
        "rationale": ("The 'probability trajectory' table reports a single scalar that "
                      "moves up and down with qualitative events. This methodology was "
                      "retired in favor of constraint-surface mapping; keeping the "
                      "table in the README contradicts the rest of the project."),
    },
    {
        "doc": "README.md",
        "line": 293,
        "category": "venus level hype",
        "old": ("**Pre-registered constraint conditions** define PASS/FAIL criteria "
                "BEFORE computation. Six binding failure criteria carry specific "
                "probability penalties (-3% to -20% each)."),
        "new": ("**Pre-registered constraint conditions** define PASS/FAIL criteria "
                "BEFORE computation. Each gate reports {pre-registered band, "
                "computed value, verdict}; verdicts update the constraint surface "
                "rather than a scalar probability. Negative results are boundaries, "
                "not failures -- they eliminate regions of the solution space."),
        "rationale": ("'-3% to -20% penalties' is the retired probability-arithmetic "
                      "methodology; constraint-map reading is that each FAIL "
                      "eliminates a region of solution space."),
    },
    # ---------- Phononic-framework-hypothesis.md ----------
    {
        "doc": "sessions/framework/Phononic-framework-hypothesis.md",
        "line": 297,
        "category": "quantitative-hype framing",
        "old": ("2. **The spectral index.** Naive KZ on GL modes gives n_s = 2.065 "
                "(blue, 262-sigma from Planck). CLOSED. Four surviving routes: "
                "domain wall 1D DOS, instanton timescale, modulus fluctuations, "
                "multi-field interference."),
        "new": ("2. **The spectral index.** Naive KZ on GL modes gives n_s = 2.065 "
                "(blue). Gate verdict: 262-sigma from Planck 0.9649 +/- 0.0042 -- "
                "region excluded. Surviving routes (pre-registered): domain wall "
                "1D DOS, instanton timescale, modulus fluctuations, multi-field "
                "interference. Each route is a distinct surviving region of the "
                "solution space; none has yet been computed to a pre-registered "
                "gate."),
        "rationale": ("The original is good at marking CLOSED but doesn't state the "
                      "surviving regions as a constraint-surface structure. The "
                      "revision makes the routes into explicit regions and marks "
                      "them as uncomputed."),
    },
]

# ------------------------------------------------------------------
# Summary stats
# ------------------------------------------------------------------
N_TOTAL = len(INSTANCES)

# Category tally
CATEGORIES = {}
for inst in INSTANCES:
    cat = inst["category"]
    CATEGORIES[cat] = CATEGORIES.get(cat, 0) + 1

# Document tally
DOCS = {}
for inst in INSTANCES:
    d = inst["doc"]
    DOCS[d] = DOCS.get(d, 0) + 1

# ------------------------------------------------------------------
# Gate verdict
# ------------------------------------------------------------------
# Pre-registered:
#   PASS if >= 5 instances of flagged language replaced
#   INFO if 2-4
#   FAIL if 0-1
gate_pass_threshold = 5                      # (local)
gate_info_lower = 2                          # (local)
gate_verdict = ("PASS" if N_TOTAL >= gate_pass_threshold
                else ("INFO" if N_TOTAL >= gate_info_lower
                      else "FAIL"))

# ------------------------------------------------------------------
# Observational anchors (for any embedded gate numbers)
# ------------------------------------------------------------------
# Use canonical-constants values in the replacement table:
#   planck_ns = 0.9649
#   planck_ns_err = 0.0042
#   m_H_obs = 125.1
n_s_framework = 0.9567                       # (local) from S62 KZ computation
n_s_deviation_sigma = (planck_ns - n_s_framework) / planck_ns_err  # (local)
m_H_tree_framework = 134.0                   # (local) GeV, from Gilkey a_4/a_2
m_H_2loop_framework = 160.0                  # (local) GeV, CCM 2-loop RGE
m_H_tree_deviation_GeV = m_H_tree_framework - m_H_obs  # (local)
m_H_tree_deviation_pct = 100.0 * m_H_tree_deviation_GeV / m_H_obs  # (local)
m_H_2loop_deviation_GeV = m_H_2loop_framework - m_H_obs  # (local)
m_H_2loop_deviation_pct = 100.0 * m_H_2loop_deviation_GeV / m_H_obs  # (local)

# ------------------------------------------------------------------
# Output: npz for audit table; stdout summary
# ------------------------------------------------------------------
docs_arr = np.array([x["doc"] for x in INSTANCES])
lines_arr = np.array([x["line"] for x in INSTANCES], dtype=int)
cats_arr = np.array([x["category"] for x in INSTANCES])
olds_arr = np.array([x["old"] for x in INSTANCES])
news_arr = np.array([x["new"] for x in INSTANCES])
rats_arr = np.array([x["rationale"] for x in INSTANCES])

# Derived gate numbers
gate_data = np.array([
    N_TOTAL,
    gate_pass_threshold,
    gate_info_lower,
    n_s_framework,
    planck_ns,
    planck_ns_err,
    n_s_deviation_sigma,
    m_H_tree_framework,
    m_H_obs,
    m_H_tree_deviation_GeV,
    m_H_tree_deviation_pct,
    m_H_2loop_framework,
    m_H_2loop_deviation_GeV,
    m_H_2loop_deviation_pct,
], dtype=float)

gate_labels = np.array([
    "N_instances_replaced",
    "gate_pass_threshold",
    "gate_info_lower_bound",
    "n_s_framework",
    "planck_ns",
    "planck_ns_err",
    "n_s_deviation_sigma",
    "m_H_tree_framework_GeV",
    "m_H_obs_GeV",
    "m_H_tree_deviation_GeV",
    "m_H_tree_deviation_pct",
    "m_H_2loop_framework_GeV",
    "m_H_2loop_deviation_GeV",
    "m_H_2loop_deviation_pct",
])

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "s74_external_comm_reframe.npz")

np.savez(
    out_path,
    docs=docs_arr,
    lines=lines_arr,
    categories=cats_arr,
    old_phrases=olds_arr,
    new_phrases=news_arr,
    rationales=rats_arr,
    gate_data=gate_data,
    gate_labels=gate_labels,
    gate_verdict=np.array(gate_verdict),
    n_total=np.array(N_TOTAL, dtype=int),
)

# ------------------------------------------------------------------
# Stdout report
# ------------------------------------------------------------------
print("=" * 72)
print("S74 W4-S : EXTERNAL-COMM-REFRAME-74")
print("=" * 72)
print()
print(f"Instances flagged and replaced : {N_TOTAL}")
print(f"Gate pass threshold            : >= {gate_pass_threshold}")
print(f"Gate info lower bound          : >= {gate_info_lower}")
print(f"Gate verdict                   : {gate_verdict}")
print()
print("Category breakdown:")
for cat, n in sorted(CATEGORIES.items(), key=lambda x: -x[1]):
    print(f"  {cat:40s}  {n}")
print()
print("Document breakdown:")
for doc, n in sorted(DOCS.items(), key=lambda x: -x[1]):
    print(f"  {doc:50s}  {n}")
print()
print("Gate reference numbers used in replacements:")
for label, val in zip(gate_labels, gate_data):
    print(f"  {label:30s}  {val}")
print()
print(f"[output] {out_path}")
print()
print("Verdict text:")
if gate_verdict == "PASS":
    print("  PASS -- {N_TOTAL} >= 5 instances of flagged language replaced with "
          "structural-floor vocabulary".format(N_TOTAL=N_TOTAL))
elif gate_verdict == "INFO":
    print("  INFO -- {N_TOTAL} instances replaced, below PASS threshold of 5 "
          "but within 2-4 window".format(N_TOTAL=N_TOTAL))
else:
    print("  FAIL -- insufficient flagged instances found")
print()
print("=" * 72)
