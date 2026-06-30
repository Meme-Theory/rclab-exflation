#!/usr/bin/env python
"""
s89_w6_d_max_measurement_w9b_2_vs_pv_pipeline.py — S89 W6-7 (A.41)
====================================================================

D_max measurement: W9b-2 SCHEMATIC output vs SCHEMATIC PV-pipeline
proxy at substrate-distance-2 pole s=4.

Honest disclosure
-----------------
Plan §W6-7 §4 designates a CO-AUTHOR (connes-ncg-theorist) for the
"FULL physical PV pipeline at Λ_UV = M_KK = 7.428660036284456e+16 GeV"
that this gate compares against. The orchestrator-direct dispatch path
chosen for W6 (per user adjudication; per `wave-classification.md
§"Dispatch consequences"` METHODOLOGY-class) does NOT invoke a
specialist subagent.

The substrate-canonical "FULL PV pipeline" of S61/S78 is referenced
conceptually in `_spectral_action_regulators.py` lines 26-30
("These are SCHEMATIC regulators ... NOT the full physical
regularizations used in the S61/S78 Pauli-Villars pipeline (which
uses Lambda_UV = M_KK as the physical cutoff)"). It is NOT a
packaged module. Without the connes-ncg-theorist CO-author and a
packaged S61/S78 PV pipeline reference, this gate's substantive
SCHEMATIC-vs-FULL-physical D_max measurement is structurally
**deferred**. The cross-wave A.14 npz
`s89_w3_a14_substrate_cocycle_ratio_regulator_class_invariance_scan.npz`
is also unavailable (W3 has not closed A.14 yet).

What this script DOES
---------------------
Compute a SCHEMATIC-vs-SCHEMATIC PROXY D_max as a methodology
demonstration:

    W9b_2_schematic        = w9b_npz['rho_S_s4']  (Spearman ρ at s=4)
    S61_S78_PV_proxy       = pauli_villars_a_n(n=2, L_max=L_max, Vol_SU3_Haar)
                              from _spectral_action_regulators.py
                              (L_max pinned at runtime; see body below)
                              (SCHEMATIC PV; NOT the full physical PV)

    D_max = |log10(|W9b_2_schematic|) − log10(|S61_S78_PV_proxy|)|

This measures the regulator-class spread between W9b-2's atlas-
projection observable and the SCHEMATIC PV scheme — useful for
methodology calibration but NOT the substantive substrate-physics
measurement the plan envisions.

Per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY at K=4:
  - convention= field carries the `-SCHEMATIC-vs-SCHEMATIC-PROXY` suffix.
  - working-paper section discloses SCHEMATIC-vs-FULL deferral.
  - this gate's verdict is INFO (not PASS) acknowledging the deferral.

Substrate framing
-----------------
The D_max IS the methodology-floor F-image of the substrate-physics
SCHEMATIC-vs-FULL regulator invariance predicate. The proxy
substitution is honestly disclosed; the substantive measurement
remains queued for the CO-author dispatch.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import json
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import M_KK, Vol_SU3_Haar  # noqa: E402
from _spectral_action_regulators import (  # noqa: E402
    pauli_villars_a_n,
    zeta_a_n,
    REGULATOR_NAMES,
)


def main() -> int:
    out_dir = Path(__file__).resolve().parent
    npz_path = Path("computations/session-87/s87_w9b_pole_specificity_scan.npz")

    # ----- Load W9b-2 SCHEMATIC output -----
    if not npz_path.exists():
        report = {
            "gate": "S89-D-MAX-MEASUREMENT-W9B-2-VS-FULL-PV-PIPELINE",
            "verdict": "INFO",
            "reason": f"W9b-2 npz not found at {npz_path}",
        }
        print(json.dumps(report, indent=2))
        return 0

    npz = np.load(npz_path, allow_pickle=True)
    keys_avail = sorted(list(npz.keys()))
    # Plan §6 referenced 'rho_S_at_s_eq_4'; actual npz key is 'rho_S_s4'
    rho_key_candidates = ("rho_S_at_s_eq_4", "rho_S_s4")
    rho_key = next((k for k in rho_key_candidates if k in keys_avail), None)
    if rho_key is None:
        report = {
            "gate": "S89-D-MAX-MEASUREMENT-W9B-2-VS-FULL-PV-PIPELINE",
            "verdict": "INFO",
            "reason": f"None of {rho_key_candidates} found in npz; "
                      f"available={keys_avail[:30]}",
        }
        print(json.dumps(report, indent=2))
        return 0
    w9b2_schematic = float(np.array(npz[rho_key]).flatten()[0])

    # Pull Vol_SU3_Haar from npz if present (canonical session-87 value)
    if "Vol_SU3_Haar" in keys_avail:
        v_haar = float(np.array(npz["Vol_SU3_Haar"]).flatten()[0])
    else:
        v_haar = float(Vol_SU3_Haar)

    # ----- SCHEMATIC PV proxy at substrate-distance-2 pole s=4 -----
    # Substrate-distance-2 ↔ a_4 in the spectral-action moment hierarchy;
    # n=2 in the regulator API means "second-pole / a_4-equivalent" by
    # the convention used elsewhere in this codebase.
    L_max = 10  # (local) plan-pinned operational truncation per W6-7 §7
    pv_proxy = pauli_villars_a_n(n=2, L_max=L_max, Vol_SU3_Haar=v_haar)
    zeta_proxy = zeta_a_n(n=2, L_max=L_max, Vol_SU3_Haar=v_haar)

    # ----- D_max measurement -----
    if abs(w9b2_schematic) < 1e-300 or abs(pv_proxy) < 1e-300:
        report = {
            "gate": "S89-D-MAX-MEASUREMENT-W9B-2-VS-FULL-PV-PIPELINE",
            "verdict": "FAIL",
            "reason": ("Underflow on log10: |w9b2_schematic|="
                       f"{abs(w9b2_schematic):.3e}, "
                       f"|pv_proxy|={abs(pv_proxy):.3e}"),
        }
        print(json.dumps(report, indent=2))
        return 1

    log_w9b = math.log10(abs(w9b2_schematic))
    log_pv = math.log10(abs(pv_proxy))
    d_max = abs(log_w9b - log_pv)

    # ----- 4-band severity classification per epistemic-discipline.md -----
    if d_max < 0.1:
        severity = "NO-ACTION"
    elif d_max < 1.0:
        severity = "ADVISORY (S2)"
    elif d_max < 3.0:
        severity = "MANDATORY (S1)"
    else:
        severity = "HARD-HALT"

    # ----- Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY routing -----
    class_d_routing = {
        "class_taxonomy": "Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY",
        "severity_band": severity,
        "calibration_corpus_match": "W9b-2 (S87)",
        "reclassification_source": "S88 W-24 V.1 / B.61 (Class-(f) → Class-(d))",
        "remediation_steps": [
            "Verify derivation chain: SCHEMATIC `_spectral_action_regulators.py` "
            "consumes substrate-distance-2 pole s=4 spectral moment via "
            "Casimir-spectrum sum; the SCHEMATIC version is a derivative form "
            "of the FULL physical PV pipeline at Λ_UV = M_KK.",
            "Ratio check: r = |W9b_2_schematic| / |PV_proxy|; "
            f"|log10(r)| = {d_max:.6f}; 4-band classification: {severity}.",
            "Algebraic-equivalence audit: SCHEMATIC and FULL-physical "
            "differ in Casimir-spectrum normalization and M_PV² scaling. "
            "If the SCHEMATIC and FULL formulas coincide modulo a closed-form "
            "scalar multiplier reducible to canonical_constants pins, "
            "downgrade severity by 1 band (CF-W6-7-A pending CO-author dispatch).",
        ],
    }

    # ----- Plot -----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 4.5))
        labels = ["W9b-2 SCHEMATIC\n(rho_S at s=4)", "PV proxy\n(SCHEMATIC PV)",
                  "zeta proxy\n(SCHEMATIC zeta)"]
        values = [abs(w9b2_schematic), abs(pv_proxy), abs(zeta_proxy)]
        ax.bar(labels, values, color=["#3a6ea5", "#a5573a", "#73a53a"])
        ax.set_yscale("log")
        ax.set_ylabel("|value|  (log scale)")
        ax.set_title(
            f"S89 W6-7  W9b-2 SCHEMATIC vs SCHEMATIC PV proxy at s=4\n"
            f"D_max = {d_max:.4f}  →  {severity}  "
            f"(CO-author connes-ncg dispatch DEFERRED)"
        )
        plt.tight_layout()
        plot_path = out_dir / "s89_w6_d_max_measurement_w9b_2_vs_pv_pipeline.png"
        plt.savefig(plot_path, dpi=120)
        plt.close(fig)
    except Exception as e:
        plot_path = None
        plot_err = str(e)
    else:
        plot_err = None

    # ----- Save .npz -----
    npz_out_path = out_dir / "s89_w6_d_max_measurement_w9b_2_vs_pv_pipeline.npz"
    np.savez(
        npz_out_path,
        w9b2_schematic=np.array([w9b2_schematic]),
        pv_proxy=np.array([pv_proxy]),
        zeta_proxy=np.array([zeta_proxy]),
        log_w9b2=np.array([log_w9b]),
        log_pv_proxy=np.array([log_pv]),
        d_max=np.array([d_max]),
        severity_band=np.array([severity], dtype="U64"),
        L_max=np.array([L_max]),
        M_KK_GeV=np.array([float(M_KK)]),
        Vol_SU3_Haar=np.array([v_haar]),
        regulator_names=np.array(list(REGULATOR_NAMES)),
        deferred_co_author=np.array(["connes-ncg-theorist"], dtype="U64"),
        deferred_cross_wave_input=np.array(["s89_w3_a14_npz"], dtype="U64"),
    )

    # ----- Verdict per plan §9 -----
    # PASS: "M1∧M2∧M3∧M4 satisfied AND D_max measurable AND severity-band
    #         classifiable AND Class-(d) routing tag emitted"
    # INFO: "D_max measurable but >= 0.1 (severity ADVISORY or higher)"
    if d_max >= 0.1:
        verdict = "INFO"
    else:
        verdict = "PASS"
    # Override: deliberately downgrade to INFO when CO-author is deferred,
    # since the substantive substrate-physics finding requires the FULL
    # PV pipeline (not the SCHEMATIC proxy used here).
    if verdict == "PASS":
        # Even if numerically D_max < 0.1, we still INFO-flag deferral
        # so downstream consumers don't read this as a substantive PASS.
        verdict = "INFO"
        verdict_note = "Numerical D_max < 0.1 but verdict downgraded to INFO due to CO-author + cross-wave A.14 deferral"
    else:
        verdict_note = ""

    report = {
        "gate": "S89-D-MAX-MEASUREMENT-W9B-2-VS-FULL-PV-PIPELINE",
        "rho_key_used": rho_key,
        "w9b2_schematic_value": w9b2_schematic,
        "w9b2_schematic_log10": log_w9b,
        "pv_proxy_value": pv_proxy,
        "pv_proxy_log10": log_pv,
        "zeta_proxy_value": zeta_proxy,
        "d_max": d_max,
        "severity_band": severity,
        "lambda_uv_GeV": float(M_KK),
        "L_max": L_max,
        "Vol_SU3_Haar": v_haar,
        "class_d_routing": class_d_routing,
        "deferral_disclosure": {
            "co_author_required": "connes-ncg-theorist (per plan §W6-7 §4)",
            "co_author_dispatched": False,
            "co_author_dispatch_reason_for_deferral":
                "User-adjudicated W6 dispatch path is orchestrator-direct "
                "(per plan classification METHODOLOGY-class); subagent "
                "dispatch was not invoked.",
            "cross_wave_A14_npz_available": False,
            "cross_wave_A14_npz_path":
                "computations/session-89/s89_w3_a14_*.npz (W3 not closed)",
            "schematic_vs_full_physical": {
                "w9b_2_side": "SCHEMATIC (per `_spectral_action_regulators.py` docstring lines 23-30)",
                "pv_pipeline_side": "SCHEMATIC PROXY via `pauli_villars_a_n`; "
                                    "the FULL physical S61/S78 PV pipeline at "
                                    "Λ_UV = M_KK is conceptually-referenced "
                                    "but NOT a packaged module.",
                "honest_disclosure": "This D_max is a SCHEMATIC-vs-SCHEMATIC "
                                     "PROXY measurement; the substantive "
                                     "SCHEMATIC-vs-FULL-physical D_max remains "
                                     "queued for CO-author dispatch.",
            },
        },
        "verdict": verdict,
        "verdict_note": verdict_note,
        "carry_forward":
            "CF-W6-7-A: re-dispatch W6-7 with connes-ncg-theorist CO-author + W3 A.14 "
            "npz available; use FULL physical PV pipeline at Λ_UV = M_KK.",
        "outputs": {
            "npz": str(npz_out_path),
            "png": str(plot_path) if plot_path else None,
            "plot_error": plot_err,
        },
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
