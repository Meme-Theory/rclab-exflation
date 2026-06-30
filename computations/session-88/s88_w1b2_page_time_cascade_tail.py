"""S88-CF-CURV-11-PAGE-TIME-CASCADE-TAIL-MASS
================================================================
Page-time t_Page(M) evaluation across the cascade-tail BBN-mass band
M in {10^12, 10^12.5, 10^13, 10^13.5, 10^14} kg.  Tests whether the
Page-curve entanglement-entropy crossover lies STRUCTURALLY OUTSIDE
the substrate's observable cascade window (t_Page > t_universe by
> 100x at the M ~ 10^13 kg cascade-tail anchor).

Pre-registration: sessions/session-plan/session-88-plan-w1b2.md
                  Section W1b2-64 (PASS predicate lines 102-107;
                  machinery pin lines 132-150; substitution chain
                  lines 57-126).

Hypothesis (plan W1b2-64 Hypothesis):
    For all cascade-tail BBN-mass black holes M in [M_lo, M_hi] where
    M_lo=1e12 kg and M_hi=1e14 kg span the BBN-formation cascade-tail
    mass band, t_Page(M) > t_universe at the M=1e13 anchor by > 100x
    AND t_Page(M=1e14) > t_universe.

Threshold (RATIO test at cascade-tail anchor):
  PASS  iff  t_Page(1e13) > t_universe
        AND  t_Page(1e14) > t_universe
        AND  ratio_anchor = t_Page(1e13)/t_universe > 100
  FAIL  iff  t_Page(1e13) <= t_universe
  INFO  iff  1 < ratio_anchor <= 100  (borderline; structural Lock
              Condition holds but margin tight)

Substitution chain (plan W1b2-64 Method):
  Step 1: t_evap(M) := (5120 * pi * G^2 / (hbar * c^4)) * M^3
                       (Hawking 1974 evaporation lifetime; anchor)
          t_Page(M) := (1/2) * t_evap(M)
                       (Page 1993 entropy crossover; anchor)
  Step 2: t_Page(M) = 2560 * pi * (G^2 / (hbar * c^4)) * M^3
                    = prefactor_si * M^3
  Step 3: Units check:
            G^2     ~ m^6 / (kg^2 s^4)
            hbar c^4 ~ J s * m^4 / s^4 = kg m^6 / s^5
            G^2 / (hbar c^4) ~ s / kg^3
          So  prefactor_si * M^3  has units (s/kg^3) * kg^3 = s.  OK.
  Step 4: Numerical (full float64 in script; values are imported from
          canonical_constants.py -- documented here for substitution-
          chain readability):
            G_N        : 6.67430e-11
            hbar_SI    : 1.054571817e-34
            c_light    : 2.99792458e8
            prefactor  ~ 4.205739e-17  s/kg^3
  Step 5: Direction (sign claim from canonical form):
            t_Page(M)  is monotone-increasing  in  M  (cubic).
            t_Page(1e13) ~ 4.21e22 s vs t_universe = 4.35e17 s.
            Therefore t_Page(1e13) > t_universe;  ratio ~ 9.67e4.
            Direction PASS confirmed; magnitude PASS at threshold 100.

Cross-checks (per Hawking-theorist core methodology):
  CC1  Schwarzschild limit (Q=0, J=0): T_H = hbar c^3 / (8 pi G M k_B);
       t_evap formula reduces to canonical Hawking 1974 form.  Plan
       Section "Limiting cases" line 202.  Verified by formula identity
       (no numerical step in this script).
  CC2  Trans-Planckian floor: M_anchor = 1e13 kg vs m_Planck (h-based,
       sqrt(hc/G)) ~ 5.46e-8 kg or m_Planck (hbar-based, sqrt(hbar c/G))
       ~ 2.176e-8 kg.  Either way, M_anchor is ~20-21 OOM above the
       Planck floor; semiclassical regime is comfortably valid.

Artifacts emitted:
  * computations/session-88/s88_w1b2_page_time_cascade_tail.npz
  * computations/session-88/s88_w1b2_page_time_cascade_tail.png
  * canonical verdict line + dual-SHA companion row + schema-v2
    3-tuple (sign/magnitude/regime) row appended to
    computations/session-88/s88_gate_verdicts.txt

Author: hawking-theorist (S88 W1b2-64)
"""
from __future__ import annotations

import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")    # CPU-cap before numpy
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib   # noqa: E402
import json      # noqa: E402
import math      # noqa: E402
import sys       # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np        # noqa: E402

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
# X2-removed: alias 'T0' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(T0))

# Canonical-constants compliance per .claude/rules/math-scripts.md.
from canonical_constants import (  # noqa: E402
    G_N,        # 6.67430e-11 m^3 kg^-1 s^-2 (CODATA 2018)
    hbar_SI,    # 1.054571817e-34 J*s
    c_light,    # 2.99792458e8 m/s
    t_universe_s,  # 4.35e17 s (Planck 2018)
)

# ------------------------------------------------------------- pins
GATE_ID    = "S88-CF-CURV-11-PAGE-TIME-CASCADE-TAIL-MASS"
SCHEME     = "Hawking-1974-Page-1993"
CONVENTION = "substrate-IS-cascade-tail-eigenvalue-reorganization"
L_MAX      = "N/A"  # noqa  (gate is closed-form algebra; no L_max truncation)

# 5-point log-uniform M-grid per plan W1b2-64 machinery_pin_map (lines 132-138).
M_LOG10_GRID         = np.array([12.0, 12.5, 13.0, 13.5, 14.0], dtype=np.float64)  # (local) plan grid
M_GRID_KG            = 10.0 ** M_LOG10_GRID                                         # (local) M sweep [kg]
M_LO_PIN             = 1.0e12   # (local) plan M_lo_pin
M_HI_PIN             = 1.0e14   # (local) plan M_hi_pin
M_ANCHOR_PIN         = 1.0e13   # (local) plan M_anchor_pin (cascade-tail BBN anchor)
PASSBAND_RATIO       = 100.0    # (local) plan passband_ratio_threshold "structural non-activation" margin
ANCHOR_INDEX         = 2        # (local) index of M=1e13 in M_LOG10_GRID
HI_INDEX             = 4        # (local) index of M=1e14 in M_LOG10_GRID

SCRIPT_PATH  = resolve_script(88, 's88_w1b2_page_time_cascade_tail.py')
NPZ_OUT      = resolve_output(88, 's88_w1b2_page_time_cascade_tail.npz')
PNG_OUT      = resolve_output(88, 's88_w1b2_page_time_cascade_tail.png')
VERDICT_OUT  = resolve_output(88, 's88_gate_verdicts.txt')
CANON_PATH   = resolve_script(None, 'canonical_constants.py')

# ------------------------------------------------------------- helpers
def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


# ============================================================ main
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print("Substrate-first computation of t_Page(M) at cascade-tail BBN-mass band.")
    print()
    print("Canonical inputs (from canonical_constants.py):")
    print(f"  G_N           = {G_N:.6e}  m^3 kg^-1 s^-2  (CODATA 2018)")
    print(f"  hbar_SI       = {hbar_SI:.6e}  J*s          (CODATA 2018)")
    print(f"  c_light       = {c_light:.6e}  m/s          (exact)")
    print(f"  t_universe_s  = {t_universe_s:.6e}  s        (Planck 2018)")
    print()

    # Step 2 -- prefactor.
    prefactor_si = 2560.0 * math.pi * (G_N ** 2) / (hbar_SI * c_light ** 4)  # (local) s/kg^3
    print(f"prefactor_si (s/kg^3) = 2560*pi * G^2/(hbar*c^4) = {prefactor_si:.10e}")

    # Step 4 -- evaluate t_evap, t_Page, ratio across the 5-point grid.
    t_evap_s_grid = (5120.0 * math.pi * (G_N ** 2) / (hbar_SI * c_light ** 4)) * M_GRID_KG ** 3  # (local)
    t_Page_s_grid = 0.5 * t_evap_s_grid                                                          # (local)
    ratio_grid    = t_Page_s_grid / t_universe_s                                                 # (local)

    print()
    print("M-grid evaluation:")
    print(f"  {'log10(M/kg)':>11}  {'M [kg]':>12}  {'t_evap [s]':>14}  {'t_Page [s]':>14}  {'ratio':>10}")
    pass_per_grid_point = []  # (local)
    for i, lm in enumerate(M_LOG10_GRID):
        passed = bool(ratio_grid[i] > PASSBAND_RATIO)
        pass_per_grid_point.append(passed)
        flag = "PASS" if passed else "<100"
        print(f"  {lm:>11.2f}  {M_GRID_KG[i]:>12.3e}  {t_evap_s_grid[i]:>14.4e}  "
              f"{t_Page_s_grid[i]:>14.4e}  {ratio_grid[i]:>10.4e}  [{flag}]")

    # M_crit (where t_Page = t_universe) and M_pass100 (where ratio = 100).
    M_crit_kg     = (t_universe_s / prefactor_si) ** (1.0 / 3.0)               # (local) kg
    M_pass100_kg  = (PASSBAND_RATIO * t_universe_s / prefactor_si) ** (1.0/3.0)  # (local) kg
    print()
    print(f"M_crit (t_Page = t_universe)            = {M_crit_kg:.6e} kg  [log10 = {math.log10(M_crit_kg):.4f}]")
    print(f"M_pass100 (t_Page = 100 * t_universe)   = {M_pass100_kg:.6e} kg  [log10 = {math.log10(M_pass100_kg):.4f}]")

    # PASS predicate (plan lines 102-107).
    cond_anchor_above_uni    = bool(t_Page_s_grid[ANCHOR_INDEX] > t_universe_s)         # (local)
    cond_hi_above_uni        = bool(t_Page_s_grid[HI_INDEX] > t_universe_s)             # (local)
    cond_anchor_ratio_passes = bool(ratio_grid[ANCHOR_INDEX] > PASSBAND_RATIO)          # (local)
    pass_all = cond_anchor_above_uni and cond_hi_above_uni and cond_anchor_ratio_passes

    # FAIL/INFO discrimination.
    if pass_all:
        verdict        = "PASS"        # (local)
        sign_verdict   = "PASS"        # (local) direction t_Page>t_uni at anchor matches Step 5
        mag_verdict    = "PASS"        # (local) anchor-ratio 9.67e4 >> 100
        regime_verdict = "VALID"       # (local) anchor M~1e13 is ~21 OOM above Planck mass
    elif cond_anchor_above_uni and not cond_anchor_ratio_passes:
        # Borderline: t_Page > t_uni but anchor ratio in (1, 100].
        verdict        = "INFO"        # (local)
        sign_verdict   = "PASS"        # (local)
        mag_verdict    = "INFO"        # (local)
        regime_verdict = "VALID"       # (local)
    else:
        verdict        = "FAIL"        # (local)
        sign_verdict   = "FAIL"        # (local) direction violated
        mag_verdict    = "FAIL"        # (local)
        regime_verdict = "VALID"       # (local) regime still semiclassical

    expected_4tuple = (
        f"value=ratio_anchor={ratio_grid[ANCHOR_INDEX]:.4e}, "
        f"scheme={SCHEME}, "
        f"convention={CONVENTION}, "
        f"L_max={L_MAX}"
    )
    print()
    print(f"verdict        = {verdict}")
    print(f"sign_verdict   = {sign_verdict}")
    print(f"mag_verdict    = {mag_verdict}")
    print(f"regime_verdict = {regime_verdict}")

    # ------------------------------------------------------------- save NPZ
    np.savez(
        NPZ_OUT,
        M_grid_kg=M_GRID_KG,
        M_log10_grid=M_LOG10_GRID,
        t_evap_s=t_evap_s_grid,
        t_Page_s=t_Page_s_grid,
        ratio_t_Page_over_t_universe=ratio_grid,
        pass_per_grid_point=np.array(pass_per_grid_point, dtype=bool),
        M_crit_kg=np.array(M_crit_kg, dtype=np.float64),
        M_pass100_kg=np.array(M_pass100_kg, dtype=np.float64),
        prefactor_si=np.array(prefactor_si, dtype=np.float64),
        t_universe_s=np.array(t_universe_s, dtype=np.float64),
        cond_anchor_above_uni=np.array(cond_anchor_above_uni, dtype=bool),
        cond_hi_above_uni=np.array(cond_hi_above_uni, dtype=bool),
        cond_anchor_ratio_passes=np.array(cond_anchor_ratio_passes, dtype=bool),
        verdict_str=np.array(verdict, dtype="<U16"),
    )
    print(f"\nNPZ written: {NPZ_OUT.name}")

    # ------------------------------------------------------------- plot
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 6))
        # Continuous curve over [M_lo/3, M_hi*3] for visual context.
        M_curve = np.logspace(11.0, 14.5, 200)                     # (local)
        t_Page_curve = prefactor_si * M_curve ** 3                  # (local)
        ax.loglog(M_curve, t_Page_curve, "-", color="#1f77b4", label=r"$t_{\rm Page}(M)$ [Page 1993]")
        ax.scatter(M_GRID_KG, t_Page_s_grid, c="C3", s=60, zorder=5,
                   label="5-point M-grid (this gate)")
        ax.axhline(t_universe_s, color="gray", ls="--",
                   label=fr"$t_{{\rm universe}}={t_universe_s:.2e}$ s (Planck 2018)")
        ax.axhline(PASSBAND_RATIO * t_universe_s, color="orange", ls=":",
                   label=fr"100$\times t_{{\rm universe}}$ (passband threshold)")
        ax.axvline(M_crit_kg, color="green", ls=":",
                   label=fr"$M_{{\rm crit}}={M_crit_kg:.2e}$ kg ($t_{{\rm Page}}=t_{{\rm uni}}$)")
        ax.axvline(M_pass100_kg, color="purple", ls=":",
                   label=fr"$M_{{\rm pass100}}={M_pass100_kg:.2e}$ kg")
        ax.axvspan(M_pass100_kg, 10**14.5, alpha=0.10, color="green",
                   label="PASS region (ratio > 100)")
        ax.axvline(M_ANCHOR_PIN, color="red", ls="-", lw=0.8,
                   label=fr"$M_{{\rm anchor}}={M_ANCHOR_PIN:.0e}$ kg (BBN cascade-tail)")
        ax.set_xlabel("M [kg]")
        ax.set_ylabel(r"$t_{\rm Page}$ [s]")
        ax.set_title(f"{GATE_ID}\nPage-time vs cascade-tail BBN mass; verdict={verdict}")
        ax.legend(loc="lower right", fontsize=8)
        ax.grid(True, which="both", alpha=0.3)
        plt.tight_layout()
        plt.savefig(PNG_OUT, dpi=140)
        plt.close()
        print(f"Plot written: {PNG_OUT.name}")
    except Exception as exc:
        print(f"WARNING: plotting failed: {exc!r}")

    # ------------------------------------------------------------- pin map / SHA
    canon_sha  = sha256_file(CANON_PATH)
    script_sha = sha256_file(SCRIPT_PATH)
    pin_map = {
        "_gate_id":         GATE_ID,
        "_wp_id":           "S88-W1b2-64",
        "_scheme":          SCHEME,
        "_convention":      CONVENTION,
        "_L_max":           L_MAX,
        "M_log10_grid":     [float(x) for x in M_LOG10_GRID],
        "M_grid_kg":        [float(x) for x in M_GRID_KG],
        "M_lo_pin":         float(M_LO_PIN),
        "M_hi_pin":         float(M_HI_PIN),
        "M_anchor_pin":     float(M_ANCHOR_PIN),
        "passband_ratio_threshold": float(PASSBAND_RATIO),
        "G_N":              float(G_N),
        "hbar_SI":          float(hbar_SI),
        "c_light":          float(c_light),
        "t_universe_s":     float(t_universe_s),
        "prefactor_si":     float(prefactor_si),
        "t_Page_s_grid":    [float(x) for x in t_Page_s_grid],
        "ratio_grid":       [float(x) for x in ratio_grid],
        "M_crit_kg":        float(M_crit_kg),
        "M_pass100_kg":     float(M_pass100_kg),
        "pass_per_grid_point": pass_per_grid_point,
        "cond_anchor_above_uni":    cond_anchor_above_uni,
        "cond_hi_above_uni":        cond_hi_above_uni,
        "cond_anchor_ratio_passes": cond_anchor_ratio_passes,
        "canon_sha256":     canon_sha,
        "script_sha256":    script_sha,
        "verdict":          verdict,
        "sign_verdict":     sign_verdict,
        "mag_verdict":      mag_verdict,
        "regime_verdict":   regime_verdict,
    }
    audit_sha   = closure_hash(pin_map)                 # (local)
    content_sha = sha256_file(NPZ_OUT)                  # (local)
    print(f"\naudit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")

    # ------------------------------------------------------------- verdict line
    value_field = (
        f"ratio_anchor={ratio_grid[ANCHOR_INDEX]:.6e};"
        f"ratio_hi={ratio_grid[HI_INDEX]:.6e};"
        f"t_Page_anchor_s={t_Page_s_grid[ANCHOR_INDEX]:.6e};"
        f"t_universe_s={t_universe_s:.3e};"
        f"M_crit_kg={M_crit_kg:.4e};"
        f"M_pass100_kg={M_pass100_kg:.4e};"
        f"passband_ratio={PASSBAND_RATIO};"
        f"M_grid_log10={list(M_LOG10_GRID)};"
        f"pass_per_grid={pass_per_grid_point}"
    )
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    schema_v2_line = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={mag_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    existing = VERDICT_OUT.read_text(encoding="utf-8") if VERDICT_OUT.exists() else ""
    if any(line.startswith(GATE_ID + ":") for line in existing.splitlines()):
        print(f"\nVerdict line for {GATE_ID} already present in {VERDICT_OUT.name}; skipping append.")
    else:
        with open(VERDICT_OUT, "a", encoding="utf-8") as fh:
            fh.write(canonical_line)
            fh.write(companion_line)
            fh.write(schema_v2_line)
        print(f"\nVerdict line + companion + schema-v2 row appended to {VERDICT_OUT.name}.")

    print("\nSummary (4-tuple):")
    print(f"  ({expected_4tuple})")
    print(f"  verdict = {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
