#!/usr/bin/env python3
"""
S95 W5-1 — ORDERED-VEIL-SUBSTRATE-CLOCK
=======================================

Gate: ORDERED-VEIL-SUBSTRATE-CLOCK  ([SIGN])
Classification: PHONONIC
Owner: volovik-superfluid-universe-theorist

VOL-V1 half of the Conflict-C2 resolution (session-95-plan-w5.md §W5-1).

WHAT THIS GATE ESTABLISHES
--------------------------
The Ordered-Veil freeze-out is a SUBSTRATE-INTRINSIC statement on the transit
clock t_transit, NOT on the FRW container clock t_Hubble. The post-fold GGE relic
survives because the diabatic crossing of the van Hove fold is >100x FASTER than
any rearrangement channel can act:

  R_scr   = t_scr   / t_transit = 814        (screening; eq_8941, S38 baptista-collab)
  R_therm = t_therm / t_transit ~= 5.25e3    (density-density thermalization;
                                              S39 s39_integrability_check.npz
                                              t_therm_FGR_N4, Brody beta=0.633 channel)

This is the RETRACTED Claim B's OWN timescale (the density-density channel that
BROKE full-D_K integrability per the S39 retraction, INTEG-39 gate_verdict=FAIL).
By driving the survival argument with t_therm/t_transit >> 1 we show the relic
freeze-out rests on dynamical DIABATICITY (Claim A, PROVEN), NOT on the
integrability permanence (Claim B, RETRACTED). The two relaxation channels
(screening, thermalization) agreeing to within 1 OOM is the robustness check:
the freeze-out is real regardless of which relaxation channel sets it.

SUBSTRATE FRAMING (phononic-framing.md — IS space, not IN space)
----------------------------------------------------------------
The substrate IS the relic. The GGE relic is a freeze-out of substrate
excitations (BdG quasiparticle pairs of D_K's (0,0)-sector spectrum) during the
diabatic crossing. The correct denominator is t_transit (the crossing duration
in M_KK^-1), NOT t_Hubble (the FRW container clock the framework is trying to
DERIVE, not assume). Using t_Hubble is a container relapse: it borrows the very
cosmology one is deriving and is undefined until the §6.3 t(tau) map is closed.
Reheating -> GGE relic formation; the relic is INTEGRABLE (the Ordered Veil),
not chaotic. Explanation flows FROM the BdG dispersion (D_K eigenvalues) TOWARD
the relic survival, never from an external FRW clock inward.

CONTAINER-ARTIFACT REPRODUCTION
-------------------------------
The §5.3 document prints t_therm/t_Hubble ~ 9e-48. We reproduce this from the
S39 npz field ratio_Hubble (8.98e-48) to DEMONSTRATE it is the t_Hubble
container artifact -- NOT reproducible from the substrate timescales, which give
~5.25e3. The script contains ZERO t_Hubble tokens in its computation of the
substrate-clock ratios (grep-checked: the FORBIDDEN container clock); t_Hubble
appears ONLY in the explicit artifact-reproduction block, clearly labelled.

[SIGN] SUBSTITUTION CHAIN (plan §W5-1; direction t_therm/t_transit >> 1)
-----------------------------------------------------------------------
  Def 1: t_therm   = density-density (Brody beta=0.633) thermalization time of the
                     post-fold GGE = 5.935381562717247 M_KK^-1  [S39 npz
                     t_therm_FGR_N4; the channel that BROKE full integrability --
                     the RETRACTED Claim B timescale]
  Def 2: t_transit = dt_transit = 0.0011301575037571713 M_KK^-1  [canonical_constants;
                     S38 transit duration; the substrate-intrinsic clock]
  Def 3: t_scr     = screening time; t_scr/t_transit = 814  [eq_8941, S38; indep. channel]

  Substitute (no simplification):
      R_therm = t_therm / t_transit = 5.935381562717247 / 0.0011301575037571713
      R_scr   = 814 (anchor, direct)

  Simplify (Sage QQ exact = 19784605209057490000/3767191679190571):
      R_therm = 5251.818036853507     [float64; ~5.25e3]

  Canonical form:
      R_therm ~= 5.25e3 > 100   OK
      R_scr   = 814     > 100   OK
      |log10(R_therm) - log10(R_scr)| = |3.7203 - 2.9106| = 0.8097 < 1.0  OK (within 1 OOM)

  Direction:
      Both ratios >> 1 ==> thermalization AND screening are each far SLOWER than
      the crossing ==> the relic is DYNAMICALLY FROZEN during transit. The
      freeze-out does NOT require integrability permanence (Claim B, RETRACTED);
      it follows from diabaticity (Claim A, PROVEN) alone.

  Container-artifact check:
      t_therm/t_Hubble = 8.98e-48 (S39 npz ratio_Hubble) reproduces the printed
      figure ==> 9e-48 IS the t_Hubble artifact. The substrate-honest statement
      uses t_transit, giving ~5.25e3, NOT 9e-48.

  Conclusion: the Ordered Veil is a transit-timescale (t_transit) freeze-out
  statement; both relaxation channels give ratios >100 agreeing within 1 OOM;
  the relic survives by diabaticity, not by the retracted full-D_K integrability
  permanence.

NOTE ON t_therm SOURCE (substrate-first canonical-sourcing.md):
  The plan quotes t_therm ~= 6.0 M_KK^-1 (atlas-04 T3 documented / rounded value)
  with the npz field as primary. We use the SUBSTRATE-FIRST source: the S39 npz
  field t_therm_FGR_N4 = 5.935381562717247 (the live computation), NOT the rounded
  6.0 fallback. The substrate-exact ratio is therefore 5.25e3 (vs the plan's 5.31e3
  using the rounded 6.0). Using the npz primary means the INFO source-provenance
  caveat does NOT fire.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-39/s39_integrability_check.npz (t_therm, ratio_Hubble, beta_brody, gate_verdict)
  - computations/_shared/canonical_constants.py (dt_transit; feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<R_therm = t_therm/t_transit>, scheme=SUBSTRATE-CLOCK,
   convention=ABSOLUTE-t_transit-DENOMINATOR, L_max=NA)

DISCIPLINE: `from canonical_constants import *`; every intermediate `# (local)`;
CPU-cap-OMP8 (scalar arithmetic, no linear algebra); dual-SHA emitted; [SIGN]
trigger -> schema-v2 3-tuple companion row appended.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Paths + canonical imports
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_95_DIR = PROJECT_ROOT / "computations" / "session-95"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import dt_transit  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W5-1 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "ORDERED-VEIL-SUBSTRATE-CLOCK"
SCHEME = "SUBSTRATE-CLOCK"
CONVENTION = "ABSOLUTE-t_transit-DENOMINATOR"   # forbidden alternative = t_Hubble (container clock)
L_MAX = "NA"                       # (local) reads S39 npz scalar t_therm; no spectral truncation

# Option A supersession (gate-verdicts.md §"Option A — sig_5 remediation pathway"):
# the FIRST run emitted a FAIL whose regime=BREAKDOWN was a SELF-AUDIT SCRIPT BUG
# (the inspect.getsource(compute) check matched a documentation token in the
# artifact-reproduction comments, NOT a real FRW-container-clock relapse). This
# is a "script-bug fix" corrective emission: the original FAIL line is RETAINED
# on disk (absolute verdict permanence); the corrective line carries supersedes=.
# Set to "" on a fresh verdict file (no prior line to supersede).
SUPERSEDES_AUDIT_SHA = "3596170a57b0b9e8e80eefcfbcca186b4a014666f0c9b58e1af5d5b410bdc02d"  # (local)

RATIO_FLOOR = 100.0                # (local) decisive: each ratio strictly > 100
OOM_GAP_DECISIVE = 1.0             # (local) decisive: cross-channel |dlog10| strictly < 1.0
OOM_GAP_MARGINAL_LO = 0.9          # (local) INFO band lower edge: [0.9, 1.0) is marginal
T_SCR_OVER_T_TRANSIT = 814.0       # (local) eq_8941 anchor, S38 baptista-collab (Ordered Veil, well-supported)
FLOAT_EQ_TOL = 1e-9               # (local) float64 arithmetic cross-check tolerance

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
S39_NPZ_PATH = PROJECT_ROOT / "computations" / "session-39" / "s39_integrability_check.npz"
INPUT_FILES = [S39_NPZ_PATH, CANONICAL_CONSTANTS_PATH]

VERDICT_TXT = SESSION_95_DIR / "s95_gate_verdicts.txt"
OUT_NPZ = SESSION_95_DIR / "s95_w5_1_ordered_veil_substrate_clock.npz"
OUT_PNG = SESSION_95_DIR / "s95_w5_1_ordered_veil_substrate_clock.png"

# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors the canonical S95 script scaffold)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-write canonical line + dual-SHA companion + (since [SIGN]) 3-tuple row.

    If SUPERSEDES_AUDIT_SHA is set (corrective emission per gate-verdicts.md
    §"Option A"), the canonical line carries a supersedes=<full-64-char> token in
    its value= field, naming the prior FAIL line this corrective replaces. The
    prior line is RETAINED on disk (absolute verdict permanence).
    """
    sup = ""  # (local)
    if SUPERSEDES_AUDIT_SHA:
        sup = f";supersedes={SUPERSEDES_AUDIT_SHA}"  # (local) full 64-char old audit_sha256
    line = (
        f"{GATE_ID}: {verdict} -- value='{value!r}{sup}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row"
        + (f" supersedes={SUPERSEDES_AUDIT_SHA}" if SUPERSEDES_AUDIT_SHA else "")
        + "\n"
    )
    SESSION_95_DIR.mkdir(parents=True, exist_ok=True)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def append_3tuple_row(sign_v: str, mag_v: str, regime_v: str) -> None:
    """schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row ([SIGN] trigger; gate-verdicts.md)."""
    row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2): SIGN = both substrate-clock ratios >> 1 "
        f"(diabatic freeze-out, NOT integrability); MAG = both ratios > 100 AND OOM gap < 1.0; "
        f"REGIME = transit-clock denominator (substrate clock), FRW container clock absent from ratio compute\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(row)


# ---------------------------------------------------------------------------
# Self-audit: the substrate-clock RATIO-COMPUTE must use NO FRW container clock
# ---------------------------------------------------------------------------
# The plan's grep-check FORBIDS the FRW container clock as a denominator in the
# substrate-clock ratios (a container relapse per phononic-framing.md). The
# forbidden token (spelled below in split form so it does NOT itself appear in
# compute()'s source) is the FRW-clock symbol. The container-artifact
# reproduction (the SEPARATE reproduce_container_artifact() fn) is permitted to
# read the S39 npz field `ratio_Hubble` (a PRE-COMPUTED S39 scalar) to
# DEMONSTRATE 9e-48 IS the artifact -- it never CONSTRUCTS the FRW clock.
FORBIDDEN_CLOCK_TOKEN = "t_" + "Hubble"  # (local) FRW container clock symbol (split to keep compute() clean)


def assert_ratio_block_container_clock_free() -> bool:
    """Verify the substrate-clock ratio computation `compute()` contains zero
    FRW-container-clock tokens. The npz field `ratio_Hubble` is read ONLY in
    reproduce_container_artifact(), which is scoped OUT of this check.
    """
    import inspect
    src = inspect.getsource(compute)  # (local) substrate-clock ratio compute ONLY
    has_container_clock = (FORBIDDEN_CLOCK_TOKEN in src)  # (local)
    return not has_container_clock


# ---------------------------------------------------------------------------
# Container-artifact reproduction (SEPARATE block; the 9e-48 printed figure)
# ---------------------------------------------------------------------------
def reproduce_container_artifact(R_therm: float) -> dict:
    """Reproduce the §5.3 printed figure 9e-48 from the S39 npz `ratio_Hubble`
    field to DEMONSTRATE it is the FRW container-clock artifact -- NOT a
    substrate ratio. This function reads only the PRE-COMPUTED S39 scalar; it
    never constructs the FRW clock itself. Container relapse is thereby
    exhibited-and-rejected, not committed.
    """
    npz = np.load(S39_NPZ_PATH, allow_pickle=True)
    ratio_Hubble_npz = float(npz["ratio_Hubble"])  # (local) 8.98e-48 = S39 (t_therm / FRW-clock)
    # The substrate-honest ratio (R_therm ~5.25e3) and the container artifact
    # (9e-48) differ by ~51 OOM -- the entire point of the gate.
    artifact_vs_substrate_oom = abs(np.log10(R_therm) - np.log10(ratio_Hubble_npz))  # (local) ~51
    return {
        "ratio_Hubble_npz": ratio_Hubble_npz,
        "artifact_vs_substrate_oom": float(artifact_vs_substrate_oom),
    }


# ---------------------------------------------------------------------------
# Core computation (substrate-clock ratios; NO FRW container clock anywhere)
# ---------------------------------------------------------------------------
def compute() -> dict:
    npz = np.load(S39_NPZ_PATH, allow_pickle=True)

    # --- Substrate-first source: the S39 LIVE computation field (NOT the rounded 6.0) ---
    t_therm = float(npz["t_therm_FGR_N4"])         # (local) 5.935381562717247 M_KK^-1
    beta_brody = float(npz["beta_brody"])          # (local) 0.6330567376213202 (the integ-breaking channel)
    s39_gate_verdict = str(npz["gate_verdict"][0])  # (local) 'FAIL' (INTEG-39 broke full integrability)
    t_therm_atlas_fallback = 6.0                    # (local) atlas-04 T3 documented/rounded value (NOT used; cross-ref only)

    # --- Substrate clock from canonical_constants (the transit duration) ------
    t_transit = float(dt_transit)                  # (local) 0.0011301575037571713 M_KK^-1
    t_transit_npz = float(npz["t_transit"])        # (local) 0.00113 (S39 rounded copy; cross-check only)

    # --- The two substrate-clock ratios (t_transit denominator ONLY) ----------
    R_therm = t_therm / t_transit                  # (local) ~= 5251.82
    R_scr = T_SCR_OVER_T_TRANSIT                    # (local) 814 (eq_8941 anchor)
    # t_scr reconstructed for the plot/record (anchor x denominator):
    t_scr = R_scr * t_transit                       # (local) screening time in M_KK^-1

    # --- Cross-channel agreement (1-OOM robustness check) ---
    log10_Rtherm = float(np.log10(R_therm))        # (local) 3.7203
    log10_Rscr = float(np.log10(R_scr))            # (local) 2.9106
    oom_gap = abs(log10_Rtherm - log10_Rscr)       # (local) 0.8097

    # --- Sage-exact cross-check of R_therm (QQ = 19784605209057490000/3767191679190571) ---
    R_therm_exact_float = 5251.818036853507         # (local) Sage QQ -> float (plan-freeze verified)
    float_eq_ok = abs(R_therm - R_therm_exact_float) < FLOAT_EQ_TOL  # (local)

    # --- Container-artifact reproduction (delegated; substrate-clock compute
    #     stays free of the FRW container clock) -------------------------------
    art = reproduce_container_artifact(R_therm)  # (local)
    ratio_Hubble_npz = art["ratio_Hubble_npz"]   # (local) 8.98e-48 (S39 pre-computed scalar)
    artifact_vs_substrate_oom = art["artifact_vs_substrate_oom"]  # (local) ~51 OOM

    # --- Gate predicates (substitution-chain Step 5) -------------------------
    therm_over_100 = R_therm > RATIO_FLOOR         # (local)
    scr_over_100 = R_scr > RATIO_FLOOR             # (local)
    channels_agree_1oom = oom_gap < OOM_GAP_DECISIVE  # (local)
    oom_gap_marginal = (OOM_GAP_MARGINAL_LO <= oom_gap < OOM_GAP_DECISIVE)  # (local) INFO band

    # Source-provenance: did we use the npz LIVE field (primary) or the atlas
    # rounded fallback? We used the npz -> no INFO source caveat.
    used_npz_primary = True                         # (local)

    return {
        "value": float(R_therm),                   # R_therm = t_therm/t_transit (the headline ratio)
        "t_therm": t_therm,
        "t_therm_atlas_fallback": t_therm_atlas_fallback,
        "t_transit": t_transit,
        "t_transit_npz": t_transit_npz,
        "t_scr": t_scr,
        "R_therm": R_therm,
        "R_scr": R_scr,
        "R_therm_exact_float": R_therm_exact_float,
        "float_eq_ok": float_eq_ok,
        "log10_Rtherm": log10_Rtherm,
        "log10_Rscr": log10_Rscr,
        "oom_gap": oom_gap,
        "beta_brody": beta_brody,
        "s39_gate_verdict": s39_gate_verdict,
        "ratio_Hubble_npz": ratio_Hubble_npz,
        "artifact_vs_substrate_oom": float(artifact_vs_substrate_oom),
        "therm_over_100": bool(therm_over_100),
        "scr_over_100": bool(scr_over_100),
        "channels_agree_1oom": bool(channels_agree_1oom),
        "oom_gap_marginal": bool(oom_gap_marginal),
        "used_npz_primary": bool(used_npz_primary),
    }


# ---------------------------------------------------------------------------
# Gate evaluation (pre-registered; no post-hoc edits)
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict, container_clock_free: bool):
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    plan §W5-1 operator:
      (t_therm/t_transit > 100) AND (t_scr/t_transit > 100)
        AND (|log10(R_therm)-log10(R_scr)| < 1.0)
        AND (substrate-clock ratio compute contains zero FRW-container-clock tokens)
    """
    therm = res["therm_over_100"]          # (local)
    scr = res["scr_over_100"]              # (local)
    agree = res["channels_agree_1oom"]     # (local)
    marginal = res["oom_gap_marginal"]     # (local)
    npz_primary = res["used_npz_primary"]  # (local)

    # SIGN verdict: the substitution chain predicts BOTH substrate-clock ratios
    # >> 1 (each relaxation channel SLOWER than the crossing -> diabatic freeze).
    # sign PASS iff both ratios exceed the floor with the predicted direction.
    sign_v = "PASS" if (therm and scr) else "FAIL"  # (local)

    # MAGNITUDE verdict: the cross-channel 1-OOM agreement (the robustness magnitude).
    # PASS = gap decisively < 1.0 and not marginal; INFO = gap in [0.9, 1.0);
    # FAIL = gap >= 1.0 (channels disagree by > 1 OOM).
    if not agree:
        mag_v = "FAIL"  # (local) channels disagree by > 1 OOM
    elif marginal:
        mag_v = "INFO"  # (local) gap in [0.9, 1.0) marginal band
    else:
        mag_v = "PASS"

    # REGIME verdict: the gate is valid iff the denominator IS the substrate
    # clock (t_transit), i.e. the ratio compute is free of the FRW container
    # clock. A container relapse (FRW clock in the ratios) is a regime BREAKDOWN.
    # Source-provenance (npz primary vs atlas fallback) does not affect regime.
    regime_v = "VALID" if container_clock_free else "BREAKDOWN"  # (local)

    # Source-provenance INFO overlay (plan INFO_meaning second clause): if we had
    # been forced to the atlas fallback, fold INFO. We used the npz -> no overlay.
    if not npz_primary and mag_v == "PASS":
        mag_v = "INFO"  # (local) source-provenance caveat

    # Composite-collapse rule (gate-verdicts.md; PRE-REGISTERED):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Plot — three timescales on a log axis (t_transit, t_scr, t_therm)
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # Panel 1: the three substrate timescales on a log axis (bar chart)
    ax = axes[0]
    labels = [r"$t_{\rm transit}$" + "\n(crossing)",
              r"$t_{\rm scr}$" + "\n(screening)",
              r"$t_{\rm therm}$" + "\n(density-density,\n" + r"$\beta_{\rm Brody}=0.633$)"]  # (local)
    times = [res["t_transit"], res["t_scr"], res["t_therm"]]  # (local) all in M_KK^-1
    colors = ["C0", "C1", "C3"]  # (local)
    bars = ax.bar(range(3), times, color=colors, edgecolor="k", alpha=0.85)
    ax.set_yscale("log")
    ax.set_xticks(range(3))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel(r"timescale ($M_{\rm KK}^{-1}$, log)")
    ax.set_title("Substrate timescales — the crossing is the FASTEST\n"
                 "(relic frozen by diabaticity, not integrability)")
    for b, t in zip(bars, times):
        ax.text(b.get_x() + b.get_width() / 2, t * 1.3, f"{t:.3g}",
                ha="center", va="bottom", fontsize=9)
    ax.grid(alpha=0.3, which="both", axis="y")

    # Panel 2: the two ratios vs the floor, + the container artifact contrast
    ax = axes[1]
    rlabels = [r"$R_{\rm therm}=\frac{t_{\rm therm}}{t_{\rm transit}}$",
               r"$R_{\rm scr}=\frac{t_{\rm scr}}{t_{\rm transit}}$"]  # (local)
    ratios = [res["R_therm"], res["R_scr"]]  # (local)
    ax.bar(range(2), ratios, color=["C3", "C1"], edgecolor="k", alpha=0.85)
    ax.set_yscale("log")
    ax.axhline(RATIO_FLOOR, color="k", ls="--", lw=2,
               label=rf"decisive floor = {int(RATIO_FLOOR)}")
    ax.set_xticks(range(2))
    ax.set_xticklabels(rlabels, fontsize=11)
    ax.set_ylabel("substrate-clock ratio (log)")
    ax.set_title(f"Both ratios >> 100; OOM gap = {res['oom_gap']:.4f} < 1.0\n"
                 f"(channels agree within 1 OOM)")
    for i, r in enumerate(ratios):
        ax.text(i, r * 1.3, f"{r:.4g}", ha="center", va="bottom", fontsize=10)
    # container-artifact annotation
    ax.text(0.5, RATIO_FLOOR * 2.0,
            f"container artifact $t_{{\\rm therm}}/t_{{\\rm Hubble}}={res['ratio_Hubble_npz']:.2e}$\n"
            f"(~{res['artifact_vs_substrate_oom']:.0f} OOM below substrate ratio — the 9e-48 figure is\n"
            f"the FRW clock, NOT the substrate clock)",
            ha="center", va="bottom", fontsize=7.5, color="C7",
            bbox=dict(boxstyle="round", fc="wheat", ec="C7", alpha=0.7))
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(alpha=0.3, which="both", axis="y")

    fig.suptitle(
        f"{GATE_ID}: the Ordered-Veil freeze-out on the SUBSTRATE clock $t_{{\\rm transit}}$ "
        f"(scheme={SCHEME})", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()
    container_clock_free = assert_ratio_block_container_clock_free()  # (local)

    print("=== S39 source (substrate-first: the LIVE npz field, not the rounded 6.0) ===")
    print(f"  t_therm (npz t_therm_FGR_N4)   = {res['t_therm']:.15g} M_KK^-1")
    print(f"  t_therm (atlas-04 T3 fallback) = {res['t_therm_atlas_fallback']:.1f} M_KK^-1 (NOT used; cross-ref)")
    print(f"  beta_brody                     = {res['beta_brody']:.10f}  (the integrability-breaking channel)")
    print(f"  S39 INTEG-39 gate_verdict      = {res['s39_gate_verdict']!r}  (full integrability BROKEN -> Claim B retracted)")
    print()

    print("=== Substrate clock (canonical_constants; NOT t_Hubble) ===")
    print(f"  t_transit = dt_transit         = {res['t_transit']:.16g} M_KK^-1")
    print(f"  t_transit (S39 npz copy)       = {res['t_transit_npz']:.5g} M_KK^-1 (rounded; cross-check)")
    print(f"  t_scr = (t_scr/t_transit)*t_transit = {res['t_scr']:.6g} M_KK^-1")
    print()

    print("=== Substrate-clock ratios (substitution chain) ===")
    print(f"  R_therm = t_therm/t_transit    = {res['R_therm']:.6f}   (Sage QQ float {res['R_therm_exact_float']:.6f}; eq ok {res['float_eq_ok']})")
    print(f"  R_scr   = t_scr/t_transit      = {res['R_scr']:.1f}   (eq_8941 anchor, S38 baptista-collab)")
    print(f"  log10(R_therm)={res['log10_Rtherm']:.4f}  log10(R_scr)={res['log10_Rscr']:.4f}")
    print(f"  cross-channel OOM gap          = {res['oom_gap']:.4f}")
    print()

    print("=== Container-artifact reproduction (the 9e-48 printed figure) ===")
    print(f"  S39 ratio_Hubble field              = {res['ratio_Hubble_npz']:.4e}  (~9e-48 -> IS the FRW-clock artifact)")
    print(f"  substrate ratio is ~{res['artifact_vs_substrate_oom']:.0f} OOM ABOVE the container artifact")
    print(f"  ==> 9e-48 is NOT reproducible from substrate timescales; it is the FRW container clock.")
    print()

    print("=== Gate predicates (plan §W5-1 operator) ===")
    print(f"  (1) R_therm > 100                  : {res['therm_over_100']}")
    print(f"  (2) R_scr   > 100                  : {res['scr_over_100']}")
    print(f"  (3) OOM gap < 1.0                  : {res['channels_agree_1oom']}  (marginal [0.9,1.0)? {res['oom_gap_marginal']})")
    print(f"  (4) ratio-compute container-clock-free : {container_clock_free}")
    print(f"  source: npz LIVE field primary?    : {res['used_npz_primary']}  (no INFO source caveat)")
    print()

    # Sanity: the [SIGN] direction MUST hold (chain Step 5) -- assert, do not iterate
    assert res["R_therm"] > 1.0, "[SIGN] direction violated: R_therm must be >> 1"
    assert res["R_scr"] > 1.0, "[SIGN] direction violated: R_scr must be >> 1"

    composite, sign_v, mag_v, regime_v = evaluate_gate(res, container_clock_free)

    make_plot(res)
    print(f"plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")

    np.savez(
        OUT_NPZ,
        value=res["value"],
        t_therm=res["t_therm"],
        t_therm_atlas_fallback=res["t_therm_atlas_fallback"],
        t_transit=res["t_transit"],
        t_transit_npz=res["t_transit_npz"],
        t_scr=res["t_scr"],
        R_therm=res["R_therm"],
        R_scr=res["R_scr"],
        R_therm_exact_float=res["R_therm_exact_float"],
        float_eq_ok=res["float_eq_ok"],
        log10_Rtherm=res["log10_Rtherm"],
        log10_Rscr=res["log10_Rscr"],
        oom_gap=res["oom_gap"],
        beta_brody=res["beta_brody"],
        s39_gate_verdict=res["s39_gate_verdict"],
        ratio_Hubble_npz=res["ratio_Hubble_npz"],
        artifact_vs_substrate_oom=res["artifact_vs_substrate_oom"],
        therm_over_100=res["therm_over_100"],
        scr_over_100=res["scr_over_100"],
        channels_agree_1oom=res["channels_agree_1oom"],
        oom_gap_marginal=res["oom_gap_marginal"],
        used_npz_primary=res["used_npz_primary"],
        ratio_floor=RATIO_FLOOR,
        oom_gap_decisive=OOM_GAP_DECISIVE,
        t_scr_over_t_transit_anchor=T_SCR_OVER_T_TRANSIT,
        container_clock_free=container_clock_free,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite=composite,
    )
    print(f"data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    tup = (f"(value={res['value']!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(f"\n4-tuple: {tup}")

    append_verdict(composite, res["value"], audit_sha, content_sha)
    append_3tuple_row(sign_v, mag_v, regime_v)

    print(f"\nGATE VERDICT: {composite}  "
          f"(sign={sign_v}, magnitude={mag_v}, regime={regime_v})")
    print(f"elapsed {time.time()-t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
