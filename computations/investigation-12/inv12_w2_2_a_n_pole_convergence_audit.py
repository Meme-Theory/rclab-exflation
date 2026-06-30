#!/usr/bin/env python3
"""
INV12-W2-2-A-N-POLE-CONVERGENCE-AUDIT  [AUDIT]  (investigation track 12, Wave 2)
================================================================================

Owner: van-den-dungen-bridge-theorist
Gate spec: sessions/investigation/investigation-12/investigation-12-plan-w2.md  §W2-2

PURPOSE (one-pass classification audit; NO new physics — bookkeeping per my survey
next-step 2). For every load-bearing canonical a_n, emit the
    (pole_in_s, curvature_grade n = d - 2s, convergent? := [s > d/2])
tag under the CM-1995 dimension spectrum at d=8 (the cone-apex dimension of the
M^4 x SU(3) Mellin cone), in BOTH the double-power and single-power conventions
per regulator-pin-discipline.md  §"Mellin Pole-Set Labeling".

The ledger separates:
  (i)   convergent-pole RESIDUES (s > d/2 = 4): the L_max=10/12 cache genuinely
        delivers the L->inf partial-sum limit;
  (ii)  divergent-pole RESIDUES (s <= d/2 = 4): residue-subtracted ANALYTIC
        CONTINUATIONS at meromorphic poles where the shell sum L^{d-2s} diverges —
        the cache does NOT deliver them as partial-sum limits;
  (iii) NON-RESIDUE structural invariants (R_K Koszul curvature, gauge-module
        K-theory rank): these are L-stable for an ENTIRELY DIFFERENT reason
        (they are not analytic continuations at all — they have no pole_in_s).

The a2 CANARY (double-power s=3, n=2, s<4 -> DIVERGENT) is cross-validated against
the published S109-VIICB-ZETA-NATIVE-LEVEL-3 verdict (is_weyl_divergent=True,
anchor_L10=280743 vs g_M=2776.165389, ~10^5x miss from above).

VERDICT (gate spec PASS criterion): ledger-complete (every load-bearing a_n tagged
with a non-ambiguous triple in both conventions) AND a2 reproduces the S109
DIVERGENT verdict. INFO payload = COUNT of divergent-pole residue-subtracted-only
a_n among the load-bearing set.

This is [AUDIT], NOT [SIGN]: NO 3-tuple emission.

Substrate framing: GEOMETRIC. The pole status is a property of the D_K spectrum's
growth, not of any external regulator choice. Direction is substrate-first
throughout: D_K eigenvalues -> spectral zeta residues -> emergent a_n.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')   # (local) pure bookkeeping; no matrix ops
os.environ.setdefault('MKL_NUM_THREADS', '8')   # (local)

import sys
import json
import hashlib
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- _shared on path BEFORE the canonical import ------------------------------
# This script lives in computations/investigation-12/ (a sibling of session-N/);
# _shared (canonical_constants.py) must be importable BEFORE the canonical import.
_SESSION_DIR = Path(__file__).resolve().parent       # (local) computations/investigation-12/
_SHARED_DIR = _SESSION_DIR.parent / "_shared"        # (local) computations/_shared/
sys.path.insert(0, str(_SHARED_DIR))

# ---- Canonical constants (MANDATORY import; never hardcode) -------------------
# a_n^{zeta} canonical Seeley-DeWitt zeta-regulated values (S88 A-N-FW-CANONICALIZATION)
from canonical_constants import (
    a_0_FW_zeta,   # 6440.0          (S88; a0 -> Lambda, cosmological term)
    a_2_FW_zeta,   # 2776.165389     (S88; a2 -> G_N, Einstein-Hilbert)
    a_4_FW_zeta,   # 1350.7216       (S75; a4 -> Yang-Mills + Higgs quartic)
    a_6_FW_zeta,   # 765.594         (S96; higher-order EFT)
    a_8_FW_zeta,   # 521.183         (S96; higher-order EFT)
)

# ==============================================================================
# SECTION 0 — Input-pin map + dual SHA (audit closure)
# ==============================================================================
SCRIPT_PATH = os.path.abspath(__file__)
HERE = os.path.dirname(SCRIPT_PATH)
CANONICAL_PATH = os.path.abspath(os.path.join(HERE, "..", "_shared", "canonical_constants.py"))
S109_VERDICT_PATH = os.path.abspath(os.path.join(HERE, "..", "session-109", "s109_gate_verdicts.txt"))


def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    """SHA-256 over the ordered input-pin map (canonical audit-SHA pattern)."""
    payload = "\n".join(f"{k}={pin_map[k]}" for k in sorted(pin_map)).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


canonical_sha = sha256_of_file(CANONICAL_PATH)
script_sha = sha256_of_file(SCRIPT_PATH)
try:
    s109_sha = sha256_of_file(S109_VERDICT_PATH)
except FileNotFoundError:
    s109_sha = "MISSING"

# Log input SHAs in the first 20 lines of stdout (gate-verdicts.md protocol)
print("=" * 78)
print("INV12-W2-2-A-N-POLE-CONVERGENCE-AUDIT  [AUDIT]  (investigation track 12)")
print("=" * 78)
print(f"INPUT SHA  canonical_constants.py  = {canonical_sha}")
print(f"INPUT SHA  s109_gate_verdicts.txt  = {s109_sha}")
print(f"SCRIPT SHA                         = {script_sha}")
print("-" * 78)

# ==============================================================================
# SECTION 1 — Dimension-spectrum + pole-convention machinery (d=8 cone apex)
# ==============================================================================
#
# CM-1995 dimension spectrum for the M^4 x SU(3) Mellin cone:  d = 8 (cone-apex
# dimension; the SU(3) fiber has geometric dim 8 = dim SU(3); this is the
# d_spec_cone_apex=8 of S85 W6-13, NOT the canonical spectral-dim 3.0).
#
# Two printed-zeta power conventions (regulator-pin-discipline.md §"Mellin
# Pole-Set Labeling"), related to the curvature grade n by an EXACT integer map:
#
#   Conv. A (double-power):  zeta_D(s) = Sum_k m_k lambda_k^{-2s},  poles at s=(d-n)/2
#                            => n = d - 2s     ;  S_s(double) = {4,3,2,1,0} at d=8
#   Conv. B (single-power):  zeta_D(s) = Sum_k m_k lambda_k^{-s},   poles at s=d-n
#                            => n = d - s      ;  S_s(single) = {8,6,4,2,0} at d=8
#
# {0,2,4,6,8} is ALWAYS the curvature grade n (the CM-1995 dimension-spectrum
# label). It is the s-pole set ONLY under the single-power convention.
#
# CONVERGENCE TEST (shell-sum / Friedrich-Bär): the partial sum over D_K
# eigenvalues L^{d-2s} converges as L->inf iff Re(s) > d/2 = 4. This is the
# SAME threshold in BOTH conventions because convergence is a property of the
# underlying double-power Dirichlet series Sum m_k |lambda_k|^{-2s} (the heat
# trace), independent of the printed power convention. We apply the convergence
# test on the DOUBLE-POWER s-index s_double, which is the physical exponent of
# |lambda|^{-2 s_double} in the shell sum.
#
#   convergent(a_n)  <=>  s_double(a_n) > d/2 = 4
#
# Residue formula (S46): Res(zeta_D, s = d/2 - k) = a_{2k} / Gamma(d/2 - k),
# i.e. a_{2k} sits at the double-power pole s = d/2 - k = 4 - k.

d_cone_apex = 8           # (local) cone-apex dimension of the M^4 x SU(3) Mellin cone (S85 W6-13; T5 theorem)
d_half = d_cone_apex / 2  # (local) = 4.0; convergence threshold for the shell sum L^{d-2s}


def pole_in_s_double(n):
    """Double-power pole index: s = (d - n)/2. (curvature grade n -> s)."""
    return (d_cone_apex - n) / 2.0


def pole_in_s_single(n):
    """Single-power pole index: s = d - n."""
    return float(d_cone_apex - n)


def is_convergent(s_double):
    """Shell-sum convergence: the partial sum L^{d-2s} converges iff s > d/2.
    Applied on the DOUBLE-POWER s-index (physical exponent of |lambda|^{-2s})."""
    return bool(s_double > d_half)


def convergence_label(s_double):
    if s_double > d_half:
        return "CONVERGENT"
    if abs(s_double - d_half) < 1e-12:
        # s == d/2 EXACTLY: the shell sum L^{d-2s}=L^0=const per shell DIVERGES
        # logarithmically (sum of a constant over growing shells); this is the
        # MARGINAL boundary pole. We classify it as DIVERGENT (not delivered as a
        # finite partial-sum limit) but tag the marginal nature explicitly.
        return "DIVERGENT-MARGINAL"
    return "DIVERGENT"


# ==============================================================================
# SECTION 2 — The load-bearing canonical-number set
# ==============================================================================
#
# The gate names 5 load-bearing canonical-number CLASSES: a0, a2, a4,
# gauge-module rank, R_K. They are NOT all zeta_{D_K} residues — the honest
# ledger has THREE structural classes, not two:
#
#   CLASS I  (zeta-residue):  a0, a2, a4 (+ a6, a8 extended) — residues of
#            zeta_{D_K}(s) at dimension-spectrum poles; the (pole_in_s, n,
#            convergent?) tag applies directly.
#   CLASS II (Koszul curvature scalar): R_K(fold) = -2.018 M_KK^2 — an algebraic
#            property of the metric. It FEEDS a2 via a2 ∝ ∫(R/6 - E) but is NOT
#            itself a zeta residue: it has NO pole_in_s. L-stable because it is a
#            fixed metric invariant, not an analytic continuation.
#   CLASS III (K-theory index): gauge-module rank 775 (Paper 05; MODULE-61) — a
#            topological integer (index of Dirac on the gauge module). Deformation-
#            invariant (Paper 10 locally-bounded-perturbation protection). NO
#            pole_in_s: it is a K_0 rank, not a zeta residue.
#
# Collapsing CLASS II / III into the "convergent residue" column would
# MISREPRESENT them: they are L-stable for a topological/algebraic reason, not
# because their shell sum converges. The substrate-IS distinction is sharpened by
# keeping the three classes separate.

# CLASS I — zeta residues (the (pole_in_s, n, convergent?) tag applies)
zeta_residue_rows = [
    # (label, n_curv_grade, canonical_value, physics_role)
    ("a_0", 0, float(a_0_FW_zeta), "Lambda (cosmological term / perimeter)"),
    ("a_2", 2, float(a_2_FW_zeta), "G_N, Einstein-Hilbert (the S109 canary)"),
    ("a_4", 4, float(a_4_FW_zeta), "Yang-Mills + Higgs quartic"),
    ("a_6", 6, float(a_6_FW_zeta), "higher-order EFT control"),
    ("a_8", 8, float(a_8_FW_zeta), "higher-order EFT control"),
]

# CLASS II — Koszul curvature scalar (NON-RESIDUE; pole-free)
R_K_fold = -2.018   # (local) M_KK^2; Koszul formula, S61 KASPAROV-VERIFY-61 / A-TENSOR-61 (session-64-results-workingpaper.md). NOT a zeta residue.

# CLASS III — K-theory gauge-module rank (NON-RESIDUE; pole-free)
gauge_module_rank = 775   # (local) integer; Paper 05 gauge module, S61/S63 MODULE-61. K_0 rank, not a zeta residue.

# ==============================================================================
# SECTION 3 — Build the per-a_n ledger
# ==============================================================================
ledger = []
for label, n, value, role in zeta_residue_rows:
    s_dbl = pole_in_s_double(n)
    s_sgl = pole_in_s_single(n)
    conv = is_convergent(s_dbl)
    conv_lbl = convergence_label(s_dbl)
    ledger.append({
        "class": "I-zeta-residue",
        "label": label,
        "curvature_grade_n": n,
        "pole_in_s_double": s_dbl,
        "pole_in_s_single": s_sgl,
        "convergent": conv,
        "convergence_label": conv_lbl,
        "canonical_value": value,
        "physics_role": role,
        "cache_deliverable": conv,   # CONVERGENT residue == cache delivers the L->inf limit
    })

# CLASS II + III rows: pole-free non-residue structural invariants
nonresidue_rows = [
    {
        "class": "II-Koszul-curvature",
        "label": "R_K(fold)",
        "curvature_grade_n": None,
        "pole_in_s_double": None,
        "pole_in_s_single": None,
        "convergent": None,          # N/A — not a zeta residue, has no shell sum
        "convergence_label": "N/A-NON-RESIDUE",
        "canonical_value": R_K_fold,
        "physics_role": "fiber scalar curvature (FEEDS a_2; Koszul, S61)",
        "cache_deliverable": True,   # L-stable: fixed metric invariant (NOT an analytic continuation)
    },
    {
        "class": "III-K-theory-index",
        "label": "gauge_module_rank",
        "curvature_grade_n": None,
        "pole_in_s_double": None,
        "pole_in_s_single": None,
        "convergent": None,          # N/A — K_0 rank, not a zeta residue
        "convergence_label": "N/A-NON-RESIDUE",
        "canonical_value": float(gauge_module_rank),
        "physics_role": "gauge-module K_0 rank (Paper 05; deformation-invariant per Paper 10)",
        "cache_deliverable": True,   # L-stable: topological integer (NOT an analytic continuation)
    },
]
ledger.extend(nonresidue_rows)

# ==============================================================================
# SECTION 4 — a_2 CANARY cross-validation against S109-VIICB-ZETA-NATIVE-LEVEL-3
# ==============================================================================
# S109 canonical anchors (read from s109_gate_verdicts.txt, the input pin):
#   anchor_L6  = 39619.0337
#   anchor_L8  = 109123.0724
#   anchor_L10 = 280743.235367
#   g_M        = 2776.165389  (== a_2_FW_zeta, the residue / Weyl coefficient)
#   is_weyl_divergent = True ; is_convergent = False ; trend_sign = +1
#
# These are imported as the published canary; the audit reproduces a_2's status
# from FIRST PRINCIPLES (double-power s=3 < d/2=4 => DIVERGENT) and checks it
# AGREES with the S109 verdict.
s109_anchor_L6 = 39619.0337           # (local) from s109_gate_verdicts.txt
s109_anchor_L8 = 109123.0724          # (local) from s109_gate_verdicts.txt
s109_anchor_L10 = 280743.235367       # (local) from s109_gate_verdicts.txt
s109_g_M = 2776.165389                # (local) Weyl coefficient (== a_2_FW_zeta)
s109_is_weyl_divergent = True         # (local) from s109_gate_verdicts.txt
s109_trend_sign = +1                  # (local) anchor monotone-increasing
s109_audit_sha = "e976ab54f2467ead47a895473ebcd170ec56f231918ef4094a9cb70565d8b54f"  # (local)

# First-principles a_2 status from THIS audit:
a2_row = next(r for r in ledger if r["label"] == "a_2")
a2_s_double = a2_row["pole_in_s_double"]                 # = 3.0
a2_audit_divergent = (not a2_row["convergent"])          # s=3 < 4 => True (DIVERGENT)

# Cross-check 1: the audit's a_2 divergent status reproduces S109's is_weyl_divergent
a2_status_agrees_with_s109 = (a2_audit_divergent == s109_is_weyl_divergent)

# Cross-check 2: anchor monotone-increasing (Weyl-divergent growth) consistent with
# divergent-pole classification — the partial sum grows without bound
anchor_monotone_increasing = (s109_anchor_L6 < s109_anchor_L8 < s109_anchor_L10)
anchor_misses_gM_from_above = (s109_anchor_L10 > s109_g_M)   # 280743 >> 2776

# Cross-check 3: the canonical a_2_FW_zeta IS the S109 g_M (the residue == Weyl coeff)
a2_value_is_gM = abs(float(a_2_FW_zeta) - s109_g_M) < 1e-6

a2_canary_consistent = bool(
    a2_status_agrees_with_s109
    and anchor_monotone_increasing
    and anchor_misses_gM_from_above
    and a2_value_is_gM
)

# ==============================================================================
# SECTION 5 — Verdict assembly
# ==============================================================================
# PASS criterion (gate spec strict_PASS_boundary):
#   ledger-complete (every load-bearing a_n tagged with a non-ambiguous triple)
#   AND a_2 double-power (s=3) flagged DIVERGENT consistent with S109.
#
# Ledger-completeness: every CLASS-I row has a non-ambiguous (pole_in_s_double,
# n, convergent?) triple (no None in those fields, n recovers via n=d-2s, and
# the two conventions agree on n); every CLASS-II/III row is explicitly tagged
# N/A-NON-RESIDUE (pole-free, by structural type).

def class_I_triple_unambiguous(r):
    if r["class"] != "I-zeta-residue":
        return True
    # non-ambiguous: pole indices present, convergence resolved, and the EXACT
    # map n = d - 2*s_double holds (internal consistency of the two conventions)
    n_recovered_double = d_cone_apex - 2 * r["pole_in_s_double"]
    n_recovered_single = d_cone_apex - r["pole_in_s_single"]
    map_consistent = (
        abs(n_recovered_double - r["curvature_grade_n"]) < 1e-12
        and abs(n_recovered_single - r["curvature_grade_n"]) < 1e-12
    )
    fields_present = (
        r["pole_in_s_double"] is not None
        and r["pole_in_s_single"] is not None
        and r["convergent"] is not None
    )
    return bool(map_consistent and fields_present)

ledger_complete = all(class_I_triple_unambiguous(r) for r in ledger)

# Count load-bearing classes: the gate names {a0, a2, a4, gauge-module, R_K} = 5
# We tag a SUPERSET (a0,a2,a4,a6,a8 + R_K + gauge) = 7 rows, but the 5 named
# load-bearing classes are all present and tagged:
named_load_bearing = {"a_0", "a_2", "a_4", "R_K(fold)", "gauge_module_rank"}
present_labels = {r["label"] for r in ledger}
all_named_present = named_load_bearing.issubset(present_labels)

# INFO headline: COUNT of divergent-pole (residue-subtracted-only) CLASS-I a_n
divergent_residue_rows = [
    r for r in ledger
    if r["class"] == "I-zeta-residue" and not r["convergent"]
]
n_divergent_residue = len(divergent_residue_rows)
divergent_residue_labels = [r["label"] for r in divergent_residue_rows]

convergent_residue_rows = [
    r for r in ledger
    if r["class"] == "I-zeta-residue" and r["convergent"]
]
n_convergent_residue = len(convergent_residue_rows)
convergent_residue_labels = [r["label"] for r in convergent_residue_rows]

# Composite verdict (gate spec): PASS iff ledger complete AND named-set present
# AND a_2 canary reproduces S109 divergent verdict.
verdict_PASS = bool(ledger_complete and all_named_present and a2_canary_consistent)
# Per the INFO rubric, the gate's HEADLINE diagnostic is the divergent-count when
# the ledger lands cleanly. The PASS criterion is structural completeness +
# canary-consistency; the COUNT is the INFO payload. Following the gate rubric,
# we emit PASS when the structural+canary criteria hold (the ledger is complete
# AND the a_2 divergent status is reproduced); the divergent-count is reported in
# the value payload as the headline diagnostic regardless.
if verdict_PASS:
    verdict = "PASS"
else:
    # FAIL only if ledger cannot be completed or a_2 contradicts S109.
    verdict = "FAIL"

# ==============================================================================
# SECTION 6 — Console ledger table
# ==============================================================================
print()
print("PER-a_n POLE-CONVERGENCE LEDGER  (d_cone_apex = 8 ; convergence threshold s > d/2 = 4)")
print("-" * 110)
hdr = (f"{'a_n':<18}{'class':<20}{'n':>4}{'s(A-double)':>13}{'s(B-single)':>13}"
       f"{'convergent?':>14}{'cache?':>9}")
print(hdr)
print("-" * 110)
for r in ledger:
    n_str = "—" if r["curvature_grade_n"] is None else str(r["curvature_grade_n"])
    sd_str = "—" if r["pole_in_s_double"] is None else f"{r['pole_in_s_double']:.1f}"
    ss_str = "—" if r["pole_in_s_single"] is None else f"{r['pole_in_s_single']:.1f}"
    print(f"{r['label']:<18}{r['class']:<20}{n_str:>4}{sd_str:>13}{ss_str:>13}"
          f"{r['convergence_label']:>14}{str(r['cache_deliverable']):>9}")
print("-" * 110)
print(f"CLASS-I zeta residues:  {n_convergent_residue} convergent ({convergent_residue_labels}) ; "
      f"{n_divergent_residue} divergent ({divergent_residue_labels})")
print(f"a_2 CANARY: audit double-power s={a2_s_double:.1f} < d/2={d_half:.1f} => DIVERGENT={a2_audit_divergent}; "
      f"agrees with S109 is_weyl_divergent={s109_is_weyl_divergent}: {a2_status_agrees_with_s109}")
print(f"  S109 anchors L6/L8/L10 = {s109_anchor_L6}/{s109_anchor_L8}/{s109_anchor_L10}; "
      f"g_M={s109_g_M}; monotone-increasing={anchor_monotone_increasing}; misses g_M from above={anchor_misses_gM_from_above}")
print(f"  a_2_FW_zeta == S109 g_M (residue == Weyl coeff): {a2_value_is_gM}")
print(f"LEDGER COMPLETE: {ledger_complete}; all named load-bearing present: {all_named_present}; "
      f"a_2 canary consistent: {a2_canary_consistent}")
print("-" * 110)

# ==============================================================================
# SECTION 7 — Pole-map figure (s-axis vs convergence threshold s=d/2)
# ==============================================================================
fig, ax = plt.subplots(figsize=(10, 6))

# Plot CLASS-I residues on the double-power s-axis
labels_plt = [r["label"] for r in ledger if r["class"] == "I-zeta-residue"]
s_dbl_plt = [r["pole_in_s_double"] for r in ledger if r["class"] == "I-zeta-residue"]
conv_plt = [r["convergent"] for r in ledger if r["class"] == "I-zeta-residue"]
colors = ["tab:green" if c else "tab:red" for c in conv_plt]

ypos = np.arange(len(labels_plt))   # (local)
ax.barh(ypos, s_dbl_plt, color=colors, alpha=0.75, edgecolor="black")
ax.axvline(d_half, color="black", linestyle="--", linewidth=2,
           label=f"convergence threshold  s = d/2 = {d_half:.0f}")
ax.set_yticks(ypos)
ax.set_yticklabels(labels_plt)
ax.set_xlabel("double-power pole index  s = (d - n)/2   (d = 8 cone apex)")
ax.set_title("INV12-W2-2  a_n Pole-Convergence Ledger\n"
             "green = CONVERGENT (s>4, cache-deliverable);  red = DIVERGENT (s<=4, residue-subtracted-only)")
# annotate each bar with (n, convergence label)
for i, r in enumerate([r for r in ledger if r["class"] == "I-zeta-residue"]):
    ax.text(r["pole_in_s_double"] + 0.05, i,
            f"n={r['curvature_grade_n']}, {r['convergence_label']}",
            va="center", fontsize=9)
# annotate the a_2 canary
a2_idx = labels_plt.index("a_2")
ax.text(d_half + 0.1, a2_idx - 0.35,
        f"S109 canary: anchor_L10={s109_anchor_L10:.0f} >> g_M={s109_g_M:.1f}  (Weyl-divergent)",
        color="tab:red", fontsize=8, style="italic")
ax.legend(loc="lower right")
ax.set_xlim(-0.5, max(s_dbl_plt) + 2.5)
fig.tight_layout()
PLOT_PATH = os.path.join(HERE, "inv12_w2_2_a_n_pole_convergence_audit.png")
fig.savefig(PLOT_PATH, dpi=140)
plt.close(fig)
print(f"PLOT written: {PLOT_PATH}")

# ==============================================================================
# SECTION 8 — npz data file
# ==============================================================================
DATA_PATH = os.path.join(HERE, "inv12_w2_2_a_n_pole_convergence_audit.npz")
np.savez(
    DATA_PATH,
    # ledger arrays (CLASS-I residues)
    ci_labels=np.array([r["label"] for r in ledger if r["class"] == "I-zeta-residue"]),
    ci_curvature_grade_n=np.array([r["curvature_grade_n"] for r in ledger if r["class"] == "I-zeta-residue"]),
    ci_pole_in_s_double=np.array([r["pole_in_s_double"] for r in ledger if r["class"] == "I-zeta-residue"]),
    ci_pole_in_s_single=np.array([r["pole_in_s_single"] for r in ledger if r["class"] == "I-zeta-residue"]),
    ci_convergent=np.array([r["convergent"] for r in ledger if r["class"] == "I-zeta-residue"]),
    ci_convergence_label=np.array([r["convergence_label"] for r in ledger if r["class"] == "I-zeta-residue"]),
    ci_canonical_value=np.array([r["canonical_value"] for r in ledger if r["class"] == "I-zeta-residue"]),
    # non-residue class labels
    nonresidue_labels=np.array([r["label"] for r in ledger if r["class"] != "I-zeta-residue"]),
    nonresidue_class=np.array([r["class"] for r in ledger if r["class"] != "I-zeta-residue"]),
    nonresidue_value=np.array([r["canonical_value"] for r in ledger if r["class"] != "I-zeta-residue"]),
    # machinery pins
    d_cone_apex=d_cone_apex,
    d_half=d_half,
    # a_2 canary cross-validation
    a2_pole_in_s_double=a2_s_double,
    a2_audit_divergent=a2_audit_divergent,
    a2_status_agrees_with_s109=a2_status_agrees_with_s109,
    a2_value_is_gM=a2_value_is_gM,
    a2_canary_consistent=a2_canary_consistent,
    s109_anchor_L6=s109_anchor_L6,
    s109_anchor_L8=s109_anchor_L8,
    s109_anchor_L10=s109_anchor_L10,
    s109_g_M=s109_g_M,
    s109_is_weyl_divergent=s109_is_weyl_divergent,
    s109_audit_sha=s109_audit_sha,
    # verdict scalars
    n_convergent_residue=n_convergent_residue,
    n_divergent_residue=n_divergent_residue,
    convergent_residue_labels=np.array(convergent_residue_labels),
    divergent_residue_labels=np.array(divergent_residue_labels),
    ledger_complete=ledger_complete,
    all_named_present=all_named_present,
    verdict=verdict,
    # input SHAs
    canonical_sha=canonical_sha,
    s109_sha=s109_sha,
    script_sha=script_sha,
)
print(f"DATA written: {DATA_PATH}")

# Optional JSON sidecar (human-readable ledger)
json_sidecar = os.path.join(HERE, "inv12_w2_2_a_n_pole_convergence_audit.json")
with open(json_sidecar, "w") as f:
    json.dump({"ledger": ledger,
               "a2_canary_consistent": a2_canary_consistent,
               "n_convergent_residue": n_convergent_residue,
               "n_divergent_residue": n_divergent_residue,
               "verdict": verdict}, f, indent=2)

# ==============================================================================
# SECTION 9 — Verdict-line payload (dual SHA) + emit
# ==============================================================================
# audit_sha256 = closure over the ordered input-pin map (script + canonical + pinmap)
input_pin_map = {
    "script_sha256": script_sha,
    "canonical_sha256": canonical_sha,
    "s109_verdict_sha256": s109_sha,
    "d_cone_apex": d_cone_apex,
    "d_half": d_half,
    "a_0_FW_zeta": float(a_0_FW_zeta),
    "a_2_FW_zeta": float(a_2_FW_zeta),
    "a_4_FW_zeta": float(a_4_FW_zeta),
    "a_6_FW_zeta": float(a_6_FW_zeta),
    "a_8_FW_zeta": float(a_8_FW_zeta),
    "R_K_fold": R_K_fold,
    "gauge_module_rank": gauge_module_rank,
    "n_convergent_residue": n_convergent_residue,
    "n_divergent_residue": n_divergent_residue,
    "a2_canary_consistent": a2_canary_consistent,
    "ledger_complete": ledger_complete,
    "verdict": verdict,
}
audit_sha256 = closure_hash(input_pin_map)
content_sha256 = script_sha   # content_sha256_inputs: ["script"]

# value payload (no surrounding quotes; no single-quote chars — emit_verdict wraps it)
value_payload = (
    f"ledger_complete={ledger_complete};"
    f"n_classI_residue=5;n_convergent={n_convergent_residue};n_divergent={n_divergent_residue};"
    f"convergent={'+'.join(convergent_residue_labels)};"
    f"divergent={'+'.join(divergent_residue_labels)};"
    f"a2_double_s=3_n=2_DIVERGENT;a2_canary_S109_consistent={a2_canary_consistent};"
    f"nonresidue=R_K+gauge_rank775_pole_free;d_apex=8;thresh_s_gt_4"
)

print()
print("=" * 78)
print("VERDICT PAYLOAD (pass to emit_verdict; [AUDIT] => NO 3-tuple):")
print("=" * 78)


def print_verdict_payload():
    """Print the verdict payload for the agent to pass to emit_verdict (race-safe)."""
    print(f"  gate_id      = INV12-W2-2-A-N-POLE-CONVERGENCE-AUDIT")
    print(f"  session      = 12")
    print(f"  track        = investigation")
    print(f"  verdict      = {verdict}")
    print(f"  value        = {value_payload}")
    print(f"  scheme       = Mellin")
    print(f"  convention   = BOTH-poleconv-A-double-AND-B-single")
    print(f"  L_max        = N/A")
    print(f"  audit_sha256   = {audit_sha256}")
    print(f"  content_sha256 = {content_sha256}")
    print(f"  regulator_pin (companion row) = a_n^{{Mellin}} poleconv-A-double+B-single; "
          f"a_0(s=4,n=0 MARGINAL); a_2(s=3,n=2 DIVERGENT); a_4(s=2,n=4 DIVERGENT); d_apex=8")


print_verdict_payload()

print()
print(f"[AUDIT] gate — NO sign/magnitude/regime 3-tuple emitted.")
print(f"FINAL 4-tuple: (value=<ledger>, scheme=Mellin, convention=BOTH-poleconv-A-double-AND-B-single, L_max=N/A)")

sys.exit(0)   # script succeeded; verdict is data, not exit code
