"""
S84 W2c-19: S84-UNPINNED-L2-AUDIT
==================================

Gate: S84-UNPINNED-L2-AUDIT [AUDIT] META
Agent: lizzi-spectral-functional-theorist
Session: S84, Wave 2c
Dispatch: session-84-plan-w2c.md §W2c-19

HYPOTHESIS
----------
The 5 UNPINNED rows in the Sec VII.K-META atlas (S83 Lizzi synthesis Sec II.4)
are L1-unpinned by construction. Under L2 Zubarev canonicalization (W1-G1
substrate-action choice), each UNPINNED row either (a) shifts by factor < 1.5
relative to its L1 reading -- indicating L2 provides the missing pin, promoting
the row to L2-pinned; or (b) shifts by factor > 3 -- indicating the row is
genuinely unpinned by either layer, and represents a structural degeneracy of
the Sec VII.K-META classification.

SUBSTRATE FRAMING
-----------------
UNPINNED rows are observables whose substrate-derivable scheme is ambiguous at
L1. The audit asks whether the substrate-action layer removes the ambiguity.
Direction: D_K spectrum -> S_Zubarev local-min -> regulator choice -> observable
value. Failure to pin at L2 means the substrate itself is ambiguous on that
observable, not that we lack a coordinate system.

FIVE UNPINNED ROWS (Sec VII.K-META)
-----------------------------------
#13 r_max               (S82 W2-2 FAIL 1.33e+4)
#17 w_0 Zubarev branch  (G51 branch iv, -0.998)
#18 w_0 zeta branch     (G51 branch iii)
#24 a_2-cluster         (S82 W2-8 60.35% var)
#38 mu_eff Lindblad-K   (S82 W3-8 INFO 8.58e-4)

METHOD
------
For each row:
  1. Obtain L1 reading O_L1 from S82/S83 anchor NPZ.
  2. Compute O_L2 under L2 Zubarev canonicalization at L_max=5, tau=0.19.
  3. shift_factor = max(|O_L1|, |O_L2|) / min(|O_L1|, |O_L2|).
  4. PROMOTE-L2 if <1.5; BORDERLINE if 1.5-3; GENUINE-UNPINNED if >3.

MACHINERY PIN (PRDR)
--------------------
- L_max = 5 (matches W1-G1 anchor; Row #24 special -- var reduces to 0 under
  strict L2 single-scheme collapse, handled by centroid-deviation fallback).
- scan_range: 5 UNPINNED rows, fixed per Sec VII.K-META Lizzi synthesis Sec II.4.
- tolerance: shift_factor to 3 sig figs. No CC-5 residual check here (non-
  composable rows; see cross-check 2).
- scheme: Zubarev-L2 canonicalization (Lambda_Z matched to S_Zubarev local-min).
- convention: CC-5 Mellin decomposition when composable; direct reading else.
- random_seed: 42 (deterministic; row-level arithmetic).
- GPU path: not needed -- all five rows reduce to scalar arithmetic because the
  anchor NPZs already contain the per-regulator computed values at L_max=5.

PASS / FAIL / INFO THRESHOLDS
------------------------------
PASS: all 5 shift_factor < 1.5 (UNPINNED collapses to L2-pinned).
FAIL: any shift_factor > 3 (genuinely unpinned; Sec VII.K-META structural gap).
INFO: 1-2 rows in 1.5-3 band (borderline; partial promotion).

ANCHORS
-------
- W1-G1 Zubarev sha=227a5913...
- W1-G3 zeta sha=2343920a...
- S_Zubarev = 3.806e+3 at L_max=5, tau=0.19.

ENV
---
Python: phonon-exflation-sim/.venv312/Scripts/python.exe
OMP_NUM_THREADS=8 (CPU; scalar arithmetic)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

# Canonical constants (MANDATORY)
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (  # noqa: E402
    tau_fold,
    Delta_BCS,
    M_KK,
    w0_FW,
)

# Row-to-file mapping (plan §W2c-19 line 179-184)
SCRIPT_DIR = Path(__file__).parent
INPUTS = {
    "row_13": SCRIPT_DIR / "s82_w2_2_unified_backreact_79.npz",
    "row_17_18": SCRIPT_DIR / "s83_w3_g51_w0_regulator.npz",
    "row_24": SCRIPT_DIR / "s82_w2_8_a2_cluster_test.npz",
    "row_38": SCRIPT_DIR / "s82_w3_8_mu_eff_lk.npz",
    "L2_anchor": SCRIPT_DIR / "s83_w1_g3_regulator_priority_proof.npz",
    "canon": SCRIPT_DIR / "canonical_constants.py",
}


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def log_input_shas() -> dict[str, str]:
    shas = {}
    for name, path in INPUTS.items():
        try:
            shas[name] = sha256(path)
        except Exception as exc:  # pragma: no cover
            shas[name] = f"MISSING:{exc}"
    print("=== Input SHA-256 pins ===")
    for name, sha in shas.items():
        short = sha[:16] if len(sha) >= 16 else sha
        print(f"  {name:<14s} {short}...  ({INPUTS[name].name})")
    return shas


def classify(shift_factor: float) -> str:
    """PROMOTE-L2 <1.5; BORDERLINE 1.5-3; GENUINE-UNPINNED >3."""
    if shift_factor < 1.5:
        return "PROMOTE-L2"
    if shift_factor > 3.0:
        return "GENUINE-UNPINNED"
    return "BORDERLINE"


def shift_factor(O_L1: float, O_L2: float) -> float:
    """shift_factor = max(|O_L1|, |O_L2|) / min(|O_L1|, |O_L2|).

    Dimensionless; always >= 1. Handles zero/near-zero with epsilon floor for
    row #24 when L2 collapses to a single scheme (variance -> 0 strictly).
    """
    a, b = abs(float(O_L1)), abs(float(O_L2))
    EPS = 1e-12  # (local) tiny floor to avoid divide-by-zero
    a = max(a, EPS)
    b = max(b, EPS)
    return max(a, b) / min(a, b)


def main() -> int:
    print("=" * 70)
    print("S84 W2c-19: UNPINNED-L2-AUDIT (lizzi-spectral-functional-theorist)")
    print("=" * 70)
    print(f"tau_fold = {tau_fold}")
    print(f"Delta_BCS = {Delta_BCS}")
    print(f"L_max     = 5")
    print(f"scheme    = Zubarev-L2 canonicalization")

    # --- Input SHAs ---
    input_shas = log_input_shas()
    print()

    # =====================================================================
    # ROW #13: r_max (backreaction ratio, W2-2 FAIL)
    # =====================================================================
    d13 = np.load(INPUTS["row_13"], allow_pickle=True)
    # Substitution chain row #13:
    #   Def: r_max = (Delta rho) / rho_total = rho_p / rho_bg at tau_fold.
    #   L1 reading: W2-2 zeta-regulator backreaction cap at fold gives
    #     O_L1 = max_ratio_tau = 1.33253e+4 (FAIL vs PASS_THRESH=0.1).
    #   L2 reading: same W2-2 computation but using Zubarev self-consistent
    #     saturation (max_ratio_sc_tau), where saturation identity enforces
    #     rho_p/rho_bg -> 1 by construction at Zubarev's entropy-max fold.
    #     O_L2 = max_ratio_sc_tau = 1.0 (W2-2 CC4 saturation identity PASS).
    #   Interpretation: zeta lets the backreaction run unbounded (unpinned UV);
    #     Zubarev saturates it (substrate-action UV-finite at fold). If the two
    #     disagree by >3 orders, row is genuinely unpinned across layers.
    O_L1_13 = float(d13["max_ratio_tau"])  # (local) zeta-scheme r_max at fold
    O_L2_13 = float(d13["max_ratio_sc_tau"])  # (local) Zubarev sc-saturation r_max
    sf_13 = shift_factor(O_L1_13, O_L2_13)  # (local)
    cls_13 = classify(sf_13)  # (local)
    print(f"Row #13 r_max              O_L1={O_L1_13:.6e}  O_L2={O_L2_13:.6e}  "
          f"shift={sf_13:.3e}  -> {cls_13}")

    # =====================================================================
    # ROW #17: w_0 under Zubarev branch (G51 branch iv)
    # =====================================================================
    d17 = np.load(INPUTS["row_17_18"], allow_pickle=True)
    # Substitution chain row #17:
    #   Def: w_0 = pressure / energy-density of GGE relic at N=N_pivot.
    #   L1 reading (row #17 branch-iv label): canonical target -- mixed-scheme
    #     Friedmann-compatible w_0 from S58-A: O_L1 = w_0_S58_A = -0.918.
    #     [This is the L1 value that W2a-13 registry reads as "w_0 target".]
    #   L2 reading: Zubarev regulator pure branch -- O_L2 = w_0_Zubarev = -0.998.
    #   Plan predicts shift |L1/L2| = 0.918/0.998 = 0.920 -> 1/0.920 = 1.087.
    #   Expected: PROMOTE-L2 (shift ~ 1.09 < 1.5). Verifies plan cross-check #3.
    O_L1_17 = float(d17["w_0_S58_A"])  # (local) mixed-scheme target ~-0.918
    O_L2_17 = float(d17["w_0_Zubarev"])  # (local) -0.998 G51 branch iv
    sf_17 = shift_factor(O_L1_17, O_L2_17)  # (local)
    cls_17 = classify(sf_17)  # (local)
    print(f"Row #17 w_0 Zubarev        O_L1={O_L1_17:.6e}  O_L2={O_L2_17:.6e}  "
          f"shift={sf_17:.3f}  -> {cls_17}")

    # =====================================================================
    # ROW #18: w_0 under zeta branch (G51 branch iii), recomputed at L2
    # =====================================================================
    # Substitution chain row #18:
    #   Def: w_0 as row #17 but initial data from zeta branch of G51.
    #   L1 reading: O_L1 = w_0_zeta = -0.9165 (G51 branch iii, pure zeta).
    #   L2 reading: Start from zeta-branch initial data, reapply Zubarev
    #     canonicalization (which moves the regulator to the S_Zubarev local-min).
    #     The canonicalization evacuates the zeta-specific IR tail into the
    #     Zubarev entropy-max weighting, so O_L2 converges to w_0_Zubarev = -0.998
    #     (same substrate-action minimum regardless of initial-branch label --
    #     this IS the L2 uniqueness claim of W1-G1).
    O_L1_18 = float(d17["w_0_zeta"])  # (local) -0.9165 G51 branch iii
    O_L2_18 = float(d17["w_0_Zubarev"])  # (local) -0.998 (L2 canonical)
    sf_18 = shift_factor(O_L1_18, O_L2_18)  # (local)
    cls_18 = classify(sf_18)  # (local)
    print(f"Row #18 w_0 zeta          O_L1={O_L1_18:.6e}  O_L2={O_L2_18:.6e}  "
          f"shift={sf_18:.3f}  -> {cls_18}")

    # =====================================================================
    # ROW #24: a_2-cluster (W2-8 FAIL 60.35% var)
    # =====================================================================
    d24 = np.load(INPUTS["row_24"], allow_pickle=True)
    # Substitution chain row #24:
    #   Def: a_2-cluster variance = stdev across 5-regulator-scheme evaluations
    #     of the Seeley-DeWitt a_2 coefficient at L_max=5, tau=0.19.
    #   L1 reading: O_L1 = var_a2_full = 0.6035 (60.35% relative variance
    #     across schemes = zeta, SDW, anomaly, f*, Gaussian, exp-decay).
    #     [P4-C-label of the gate has var_a2_P4C = 0.0614 which is the
    #      tightness-sub-label; the FAIL was on the full 5-scheme spread.]
    #   L2 reading: Drop the 4 non-Zubarev regulators. Under strict L2 single-
    #     scheme collapse, only ONE scheme remains -- var(1-element set) = 0.
    #     var_L2_strict = 0.0.
    #     By the shift_factor definition, max/min with min=0 diverges ->
    #     1/EPS = 1e+12 -- under the strict reading, row #24 is DIVERGENT
    #     (mathematical classification: trivially unpinned because the observable
    #     itself is a cross-scheme measure and L2 restriction kills it).
    #   OPERATIONAL fallback: Use the centroid-dev proxy:
    #     shift_24_proxy = |a_2^Zubarev - mean(a_2 across 5)| / stdev(a_2 across 5)
    #     mapped back to ratio scale as max(1, shift_24_proxy).
    #     Report BOTH strict and proxy values; take the strict (DIVERGENT) as
    #     the authoritative classification because the gate asks about
    #     cross-layer pinning, not centroid distance.
    O_L1_24 = float(d24["var_a2_full"])  # (local) 0.6035 5-scheme spread
    # f_2_numeric array: [SDW, anomaly, f*, Gaussian, exp-decay]; Zubarev is
    # NOT in this 5-set (the W2-8 scheme atlas does NOT include Zubarev as a
    # named element because Zubarev at a_2 slot aliases into the "exp-decay"
    # family with Lambda_Z cutoff). Under strict L2 collapse, only the Zubarev
    # "exp-decay" element remains, and var -> 0.
    schemes_24 = [str(s) for s in d24["schemes"]]  # (local)
    f_2_numeric = np.asarray(d24["f_2_numeric"], dtype=float)  # (local)
    mean_f_2 = float(np.mean(f_2_numeric))  # (local) centroid
    std_f_2 = float(np.std(f_2_numeric))  # (local) cluster stdev
    # Zubarev nearest element: "exp-decay" (with Lambda_Z cutoff) at index 4
    idx_zub = schemes_24.index("exp-decay")  # (local)
    a_2_zub = float(f_2_numeric[idx_zub])  # (local) Zubarev-proxy value
    centroid_dev = abs(a_2_zub - mean_f_2) / max(std_f_2, 1e-12)  # (local)
    # STRICT L2: var collapses to 0
    O_L2_24_strict = 0.0  # (local)
    sf_24_strict = shift_factor(O_L1_24, O_L2_24_strict)  # (local) DIVERGENT
    # PROXY L2: centroid deviation
    sf_24_proxy = max(1.0, centroid_dev)  # (local)
    # Authoritative: strict reading (the gate is about cross-layer pinning)
    sf_24 = sf_24_strict  # (local)
    cls_24 = classify(sf_24)  # (local)
    print(f"Row #24 a_2-cluster       O_L1={O_L1_24:.6e}  "
          f"O_L2_strict={O_L2_24_strict:.6e}  shift_strict={sf_24_strict:.3e}  "
          f"proxy={sf_24_proxy:.3e}  -> {cls_24}")
    print(f"         schemes used: {schemes_24}  "
          f"f_2_Zub-proxy(exp-decay) = {a_2_zub:.4f}  "
          f"mean={mean_f_2:.4f}  std={std_f_2:.4f}")

    # =====================================================================
    # ROW #38: mu_eff Lindblad-Keldysh (S82 INFO 8.58e-4)
    # =====================================================================
    d38 = np.load(INPUTS["row_38"], allow_pickle=True)
    # Substitution chain row #38:
    #   Def: mu_eff = effective chemical potential of the GGE relic in the
    #     Lindblad-Keldysh formulation, at mode resolution L_max=5.
    #   L1 reading: O_L1 = mu_eff_S77_ref = 8.580e-4 (canonical S77 A3 anchor,
    #     zeta-scheme exponential Lindblad kernel, no detailed-balance enforce).
    #   L2 reading: O_L2 = mu_eff_LK_with_DB = 8.741e-4 (Lindblad-Keldysh
    #     WITH detailed balance enforced; Zubarev temporal cutoff replaces
    #     exponential Lindblad kernel). The Zubarev temporal cutoff is the
    #     L2 canonical choice at the mu_eff slot because it is the unique
    #     temporal regulator that satisfies the Zubarev entropy-max substrate-
    #     action minimum on the reduced density matrix evolution.
    #   Plan S82-INFO pattern: "mu_eff_LK=8.5760e-04 within factor 2 of S77 A3".
    O_L1_38 = float(d38["mu_eff_S77_ref"])  # (local) 8.58e-4
    O_L2_38 = float(d38["mu_eff_LK_with_DB"])  # (local) 8.741e-4
    sf_38 = shift_factor(O_L1_38, O_L2_38)  # (local)
    cls_38 = classify(sf_38)  # (local)
    print(f"Row #38 mu_eff LK          O_L1={O_L1_38:.6e}  O_L2={O_L2_38:.6e}  "
          f"shift={sf_38:.3f}  -> {cls_38}")

    # =====================================================================
    # Aggregate: table + master verdict
    # =====================================================================
    print()
    print("=" * 70)
    print("UNPINNED-L2-AUDIT 5-row shift-factor table")
    print("=" * 70)
    rows = [
        ("#13", "r_max",            O_L1_13, O_L2_13, sf_13, cls_13),
        ("#17", "w_0_Zubarev",      O_L1_17, O_L2_17, sf_17, cls_17),
        ("#18", "w_0_zeta",         O_L1_18, O_L2_18, sf_18, cls_18),
        ("#24", "a_2_cluster",      O_L1_24, O_L2_24_strict, sf_24, cls_24),
        ("#38", "mu_eff_LK",        O_L1_38, O_L2_38, sf_38, cls_38),
    ]
    print(f"{'Row':>4s} {'Name':<14s} {'O_L1':>14s} {'O_L2':>14s} {'shift':>12s}  {'Class':<18s}")
    print("-" * 70)
    for rid, name, o1, o2, sf, cls in rows:
        print(f"{rid:>4s} {name:<14s} {o1:>14.6e} {o2:>14.6e} {sf:>12.3e}  {cls:<18s}")

    shifts = np.array([sf_13, sf_17, sf_18, sf_24, sf_38], dtype=float)  # (local)
    max_shift = float(np.max(shifts))  # (local)
    n_promote = int(sum(1 for r in rows if r[5] == "PROMOTE-L2"))  # (local)
    n_border = int(sum(1 for r in rows if r[5] == "BORDERLINE"))  # (local)
    n_genuine = int(sum(1 for r in rows if r[5] == "GENUINE-UNPINNED"))  # (local)
    print("-" * 70)
    print(f"PROMOTE-L2: {n_promote}/5   BORDERLINE: {n_border}/5   "
          f"GENUINE-UNPINNED: {n_genuine}/5   max_shift = {max_shift:.3e}")

    # Verdict thresholds:
    #   PASS: all 5 shift < 1.5 AND max_shift < 1.5
    #   FAIL: any shift > 3
    #   INFO: 1-2 rows in [1.5, 3]
    if n_genuine >= 1:
        verdict = "FAIL"
        reason = (f"{n_genuine} of 5 UNPINNED rows is GENUINE-UNPINNED "
                  f"(shift>3). UNPINNED bucket is NOT redundant with L2 -- "
                  f"Sec VII.K-META has structural degeneracy that neither L1 "
                  f"nor L2 pins. Theorem scope must restrict.")
    elif n_border >= 1 and n_promote + n_border == 5:
        verdict = "INFO"
        reason = (f"{n_promote}/5 PROMOTE-L2 and {n_border}/5 BORDERLINE "
                  f"(shift in [1.5,3]). Partial promotion; the "
                  f"UNPINNED bucket is partially redundant with L2.")
    elif n_promote == 5:
        verdict = "PASS"
        reason = ("All 5 UNPINNED rows promote to L2-pinned. UNPINNED bucket "
                  "is fully redundant and collapses into L2-SA sub-bucket. "
                  "W2a-13 distribution 26/2/1/8/5 revises to 26/2/1/13/0.")
    else:
        verdict = "INFO"
        reason = "Mixed classification; manual review required."

    print()
    print("=" * 70)
    print(f"VERDICT: {verdict}")
    print("=" * 70)
    print(f"Reason: {reason}")
    print(f"max_shift = {max_shift:.3e}  (PASS<1.5, INFO 1.5-3, FAIL>3)")

    # Cross-check #1 (meta): NOT-R-protected prediction.
    # Sec VII.K-META rule: R-protected rows have shift <=1.5; NOT-R-protected >=2.5.
    # Predict all 5 UNPINNED rows are NOT-R-protected.
    r_prot_ok = int(sum(1 for s in shifts if s >= 2.5))  # (local)
    print(f"Cross-check #1: NOT-R-protected count = {r_prot_ok}/5 "
          f"(predicted 5/5 per Sec VII.K-META meta-principle).")

    # Cross-check #3 (w_0 consistency): |w_0_zeta|/|w_0_Zubarev| ~ 1.087
    cc3_ratio = abs(O_L1_17) / abs(O_L2_17)  # (local)
    cc3_pred = 0.918 / 0.998  # (local) 0.9198
    cc3_err = abs(cc3_ratio - cc3_pred) / cc3_pred  # (local) relative
    print(f"Cross-check #3: |w_0_L1|/|w_0_L2|={cc3_ratio:.4f} "
          f"vs predicted {cc3_pred:.4f}  rel_err={cc3_err:.2e}")

    # =====================================================================
    # Build output npz + closure SHA
    # =====================================================================
    out_path = SCRIPT_DIR / "s84_w2c_unpinned_l2_audit.npz"
    np.savez(
        out_path,
        row_ids=np.array([r[0] for r in rows]),
        row_names=np.array([r[1] for r in rows]),
        O_L1=np.array([r[2] for r in rows], dtype=float),
        O_L2=np.array([r[3] for r in rows], dtype=float),
        shift_factor=shifts,
        classification=np.array([r[5] for r in rows]),
        max_shift=max_shift,
        n_promote=n_promote,
        n_borderline=n_border,
        n_genuine_unpinned=n_genuine,
        verdict=verdict,
        reason=reason,
        sf_24_strict=sf_24_strict,
        sf_24_proxy=sf_24_proxy,
        a_2_Zub_proxy=a_2_zub,
        a_2_mean_5scheme=mean_f_2,
        a_2_std_5scheme=std_f_2,
        cc1_not_r_protected=r_prot_ok,
        cc3_w0_ratio=cc3_ratio,
        cc3_predicted=cc3_pred,
        cc3_rel_err=cc3_err,
        L_max=5,
        tau_fold_used=tau_fold,
        scheme="Zubarev-L2",
        convention="CC5",
        W1_G1_anchor_sha="227a5913",
        W1_G3_anchor_sha="2343920a",
        S_Zubarev_anchor=3.806e+3,
        input_shas=json.dumps(input_shas),
    )
    print(f"\nOutput npz: {out_path}")

    # Closure SHA: SHA-256 of the ordered input-pin map (canonical per S81+ rules).
    ordered_pins = json.dumps(
        [[k, input_shas[k]] for k in sorted(input_shas.keys())],
        sort_keys=True,
    ).encode()
    closure_sha = hashlib.sha256(ordered_pins).hexdigest()
    print(f"closure_sha = {closure_sha}")

    # =====================================================================
    # Verdict line
    # =====================================================================
    verdict_line = (
        f"S84-UNPINNED-L2-AUDIT: {verdict} -- "
        f"value={max_shift:.3e} scheme=Zubarev-L2 convention=CC5 L_max=5 "
        f"sha256={closure_sha}\n"
    )
    verdict_path = SCRIPT_DIR / "s84_gate_verdicts.txt"
    with verdict_path.open("a", encoding="utf-8") as fh:
        fh.write(verdict_line)
    print(f"\nVerdict line appended to {verdict_path}:")
    print(f"  {verdict_line.strip()}")

    # Final 4-tuple tag
    print(f"\nFinal 4-tuple: "
          f"(value={max_shift:.3e}, scheme=Zubarev-L2, convention=CC5, L_max=5)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
