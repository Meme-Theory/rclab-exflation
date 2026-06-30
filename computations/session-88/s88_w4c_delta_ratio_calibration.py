"""S88-CLASS-B-DELTA-RATIO-CALIBRATION
================================================================
Three-method cross-comparison of (Delta_B/Delta_A) at the
polycritical point P_pc=21.22 bar, T_pc=2.273 mK:
  Greywall thermometric        ~ 0.96 +/- 0.02   (literature)
  Halperin-Hammel ladder       ~ 0.965 +/- 0.01  (literature)
  Volovik q-theory canonical   = 1.9597/2.0302 = 0.96528 (Sage exact)

Pre-registration: sessions/session-plan/session-88-plan-w4c.md
                  Section §W4c-34 (lines 533-646).

PASS predicate (line 595):
    All three methods extracted; inter-method dispersion D_max <= 2%;
    q-theory value 0.96528 lies within Greywall + HH band.

INFO (line 597): 2% < D_max <= 5%.
FAIL (line 596): D_max > 5%; OR any method missing OR systematic-
uncertainty extraction absent.

Substitution chain Step 5 (plan lines 615-620):
  D_max = max|method_i - method_j|/q_theory
        = max(0.005, 0.005, 0.0003)/0.96528
        ~ 0.005   [< 2% PASS threshold]
  Direction: D_max < 0.020 -> PASS.

Solo-mode: this gate is COMPUTATIONAL (does not pre-register a
protocol document). The mack inventory row #54b sub-row update
remains a Wave-5 mack-batch deliverable, but the gate's PASS/
FAIL/INFO verdict is determined by the substrate-vs-laboratory
inter-method dispersion D_max, not by mack inventory presence.
This gate's PASS path IS reachable in solo mode.

Author: volovik-superfluid-universe-theorist (S88 W4c-34 PRIMARY).
"""
from __future__ import annotations
import os
# === X2 bootstrap ===
import sys as _x2_sys, pathlib as _x2_pathlib, re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError("Phase 2b: tools not found")
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, project_root as _x2_project_root
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
# === end X2 ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")
import hashlib, json, sys  # noqa: E402
from pathlib import Path  # noqa: E402
import numpy as np  # noqa: E402

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
from canonical_constants import tau_fold  # noqa: E402

GATE_ID    = "S88-CLASS-B-DELTA-RATIO-CALIBRATION"
WP_ID      = "S88-W4c-34"
SCHEME     = "three-method-cross-validation"
CONVENTION = "q-theory-canonical-anchor"
L_MAX      = "N/A-laboratory-anchor"

SCRIPT_PATH    = resolve_script(88, 's88_w4c_delta_ratio_calibration.py')
VERDICT_OUT    = resolve_output(88, 's88_gate_verdicts.txt')
NPZ_PATH       = resolve_output(88, 's88_w4c_delta_ratio_calibration.npz')
PNG_PATH       = resolve_output(88, 's88_w4c_delta_ratio_calibration.png')
PLAN_PATH      = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w4c.md"
INHERITANCE_FAL = PROJECT_ROOT / ".claude" / "rules" / "inheritance-falsifier-protocol.md"

# Plan §W4c-34 machinery pin (lines 571-583)
DELTA_A_OVER_KBTC  = 2.0302   # (local) plan line 571 canonical
DELTA_B_OVER_KBTC  = 1.9597   # (local) plan line 572 canonical
SC_CORR_A          = 1.151    # (local) plan line 573 strong-coupling A
SC_CORR_B          = 1.111    # (local) plan line 574 strong-coupling B
DELTA_RATIO_GREYWALL_VAL = 0.96    # (local) plan line 611 literature central
DELTA_RATIO_GREYWALL_ERR = 0.02    # (local) plan line 611 systematic uncertainty
DELTA_RATIO_HH_VAL       = 0.965   # (local) plan line 614 literature central
DELTA_RATIO_HH_ERR       = 0.01    # (local) plan line 614 systematic uncertainty
DISPERSION_PASS_THRESHOLD = 0.020  # (local) plan line 577 (2%)
DISPERSION_INFO_THRESHOLD = 0.05   # (local) plan line 578 (5%)
P_PC_BAR           = 21.22    # (local) plan line 579
T_PC_K             = 2.273e-3 # (local) plan line 580

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def closure_hash(pin_map: dict) -> str:
    return hashlib.sha256(json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()

def main() -> int:
    print(f"\n=== {GATE_ID} ===")

    # --- Step 1: q-theory canonical ratio
    delta_ratio_q = DELTA_B_OVER_KBTC / DELTA_A_OVER_KBTC  # (local)
    print(f"Step 1: (Delta_B/Delta_A)_q = {DELTA_B_OVER_KBTC}/{DELTA_A_OVER_KBTC} = {delta_ratio_q:.10f}")

    # --- Step 2: Strong-coupling cross-check
    sc_corr_ratio = SC_CORR_B / SC_CORR_A  # (local)
    sc_match_residual = abs(sc_corr_ratio - delta_ratio_q)  # (local)
    print(f"Step 2: SC_corr_B/SC_corr_A = {SC_CORR_B}/{SC_CORR_A} = {sc_corr_ratio:.10f}")
    print(f"        |SC_ratio - delta_q| = {sc_match_residual:.6f}  (consistency check)")

    # --- Step 3+4: Greywall + Halperin-Hammel literature values
    delta_ratio_greywall = DELTA_RATIO_GREYWALL_VAL  # (local)
    delta_ratio_HH       = DELTA_RATIO_HH_VAL        # (local)
    print(f"Step 3: Greywall thermometric = {delta_ratio_greywall} +/- {DELTA_RATIO_GREYWALL_ERR}")
    print(f"Step 4: Halperin-Hammel ladder = {delta_ratio_HH} +/- {DELTA_RATIO_HH_ERR}")

    # --- Step 5: Inter-method dispersion D_max
    methods = np.array([delta_ratio_greywall, delta_ratio_HH, delta_ratio_q])  # (local)
    method_names = ["Greywall_thermometric", "Halperin_Hammel_ladder", "Volovik_q_theory"]
    pairwise = []  # (local)
    for i in range(3):
        for j in range(i + 1, 3):
            pairwise.append((method_names[i], method_names[j], abs(methods[i] - methods[j])))
    max_pair = max(pairwise, key=lambda x: x[2])
    inter_method_dispersion = max_pair[2] / delta_ratio_q  # (local) relative to q-theory canonical
    print(f"Step 5: max pairwise = |{max_pair[0]} - {max_pair[1]}| = {max_pair[2]:.6f}")
    print(f"        D_max (relative to q-theory) = {inter_method_dispersion:.6f}")

    # --- Step 6: PASS/INFO/FAIL
    q_in_greywall_band = abs(delta_ratio_q - delta_ratio_greywall) <= DELTA_RATIO_GREYWALL_ERR  # (local)
    q_in_HH_band       = abs(delta_ratio_q - delta_ratio_HH)       <= DELTA_RATIO_HH_ERR        # (local)
    q_in_band = q_in_greywall_band and q_in_HH_band
    print(f"Step 6: q in Greywall band? {q_in_greywall_band}; q in HH band? {q_in_HH_band}")

    if inter_method_dispersion <= DISPERSION_PASS_THRESHOLD and q_in_band:
        verdict = "PASS"
        sign_v, mag_v, regime_v = "PASS", "PASS", "VALID"
    elif inter_method_dispersion <= DISPERSION_INFO_THRESHOLD:
        verdict = "INFO"
        sign_v, mag_v, regime_v = "PASS", "INFO", "VALID"
    else:
        verdict = "FAIL"
        sign_v, mag_v, regime_v = "FAIL", "FAIL", "VALID"

    value_field = (f"D_max={inter_method_dispersion:.6f};"
                   f"PASS_threshold={DISPERSION_PASS_THRESHOLD};INFO_threshold={DISPERSION_INFO_THRESHOLD};"
                   f"delta_ratio_greywall={delta_ratio_greywall};delta_ratio_HH={delta_ratio_HH};"
                   f"delta_ratio_q={delta_ratio_q:.10f};SC_corr_match_residual={sc_match_residual:.6f};"
                   f"q_in_greywall_band={q_in_greywall_band};q_in_HH_band={q_in_HH_band};"
                   f"max_pair=|{max_pair[0]}-{max_pair[1]}|={max_pair[2]:.6f}")
    print(f"\nverdict={verdict}; sign={sign_v}; mag={mag_v}; regime={regime_v}")

    # --- Save .npz + .png
    np.savez(
        NPZ_PATH,
        delta_ratio_greywall=delta_ratio_greywall,
        delta_ratio_greywall_err=DELTA_RATIO_GREYWALL_ERR,
        delta_ratio_HH=delta_ratio_HH,
        delta_ratio_HH_err=DELTA_RATIO_HH_ERR,
        delta_ratio_q=delta_ratio_q,
        delta_A_over_kBTc=DELTA_A_OVER_KBTC,
        delta_B_over_kBTc=DELTA_B_OVER_KBTC,
        SC_corr_A=SC_CORR_A,
        SC_corr_B=SC_CORR_B,
        SC_corr_ratio=sc_corr_ratio,
        SC_match_residual=sc_match_residual,
        inter_method_dispersion=inter_method_dispersion,
        dispersion_PASS_threshold=DISPERSION_PASS_THRESHOLD,
        dispersion_INFO_threshold=DISPERSION_INFO_THRESHOLD,
        verdict=verdict,
        P_pc_bar=P_PC_BAR,
        T_pc_K=T_PC_K,
    )
    print(f"NPZ saved: {NPZ_PATH.name}")

    # Bar chart
    import matplotlib  # noqa: E402
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # noqa: E402
    fig, ax = plt.subplots(figsize=(8, 5))
    methods_x = np.arange(3)
    values = [delta_ratio_greywall, delta_ratio_HH, delta_ratio_q]
    errors = [DELTA_RATIO_GREYWALL_ERR, DELTA_RATIO_HH_ERR, 0.0]  # q-theory canonical: no error
    labels = ["Greywall\nthermometric", "Halperin-Hammel\nladder", "Volovik\nq-theory (canonical)"]
    colors = ["#4477AA", "#EE6677", "#228833"]
    bars = ax.bar(methods_x, values, yerr=errors, capsize=8, color=colors, edgecolor="black", alpha=0.85)
    ax.axhline(delta_ratio_q, color="#228833", linestyle="--", linewidth=1.2, alpha=0.7,
               label=f"q-theory canonical = {delta_ratio_q:.5f}")
    ax.set_xticks(methods_x)
    ax.set_xticklabels(labels)
    ax.set_ylabel(r"$\Delta_B / \Delta_A$  at $P_{pc}=21.22$ bar")
    ax.set_title(f"Three-Method Calibration of $(\\Delta_B/\\Delta_A)$ at Polycritical Point\n"
                 f"D_max = {inter_method_dispersion:.4f} (PASS @ <{DISPERSION_PASS_THRESHOLD}); verdict = {verdict}")
    ax.set_ylim(0.92, 1.00)
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    ax.legend(loc="upper right")
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.003, f"{val:.5f}",
                ha="center", va="bottom", fontsize=9)
    plt.tight_layout()
    plt.savefig(PNG_PATH, dpi=150)
    plt.close()
    print(f"PNG saved: {PNG_PATH.name}")

    # --- Dual-SHA verdict line
    pin_map = {
        "_gate_id": GATE_ID, "_wp_id": WP_ID, "_scheme": SCHEME,
        "_convention": CONVENTION, "_L_max": L_MAX,
        "delta_A_over_kBTc": DELTA_A_OVER_KBTC,
        "delta_B_over_kBTc": DELTA_B_OVER_KBTC,
        "SC_corr_A": SC_CORR_A, "SC_corr_B": SC_CORR_B,
        "delta_ratio_q": delta_ratio_q,
        "delta_ratio_greywall": delta_ratio_greywall,
        "delta_ratio_greywall_err": DELTA_RATIO_GREYWALL_ERR,
        "delta_ratio_HH": delta_ratio_HH,
        "delta_ratio_HH_err": DELTA_RATIO_HH_ERR,
        "inter_method_dispersion": inter_method_dispersion,
        "SC_corr_match_residual": sc_match_residual,
        "q_in_greywall_band": q_in_greywall_band,
        "q_in_HH_band": q_in_HH_band,
        "P_pc_bar": P_PC_BAR, "T_pc_K": T_PC_K,
        "dispersion_PASS_threshold": DISPERSION_PASS_THRESHOLD,
        "dispersion_INFO_threshold": DISPERSION_INFO_THRESHOLD,
        "tau_fold_canonical": float(tau_fold),
        "plan_path_sha256": sha256_file(PLAN_PATH),
        "inheritance_falsifier_protocol_sha256": sha256_file(INHERITANCE_FAL),
        "script_sha256": sha256_file(SCRIPT_PATH),
        "npz_sha256": sha256_file(NPZ_PATH),
        "verdict": verdict, "sign_verdict": sign_v, "mag_verdict": mag_v, "regime_verdict": regime_v,
    }
    audit_sha = closure_hash(pin_map)
    content_sha = sha256_file(NPZ_PATH)  # content-SHA over the data artifact for COMPUTE-class
    print(f"audit_sha256:   {audit_sha}\ncontent_sha256: {content_sha}")

    canonical_line = (f"{GATE_ID}: {verdict} -- value='{value_field}' "
                      f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
                      f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n")
    companion_line = (f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
                      f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n")
    schema_v2_line = (f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
                      f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n")
    existing = VERDICT_OUT.read_text(encoding="utf-8") if VERDICT_OUT.exists() else ""
    if any(line.startswith(GATE_ID + ":") for line in existing.splitlines()):
        print(f"Verdict for {GATE_ID} present; skipping.")
    else:
        with open(VERDICT_OUT, "a", encoding="utf-8") as fh:
            fh.write(canonical_line); fh.write(companion_line); fh.write(schema_v2_line)
            fh.flush(); os.fsync(fh.fileno())
        print("Verdict appended.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
