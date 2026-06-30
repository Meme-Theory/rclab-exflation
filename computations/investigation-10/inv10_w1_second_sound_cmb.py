#!/usr/bin/env python3
"""
INV10 W1-3 — Second-sound CMB horizon multipole (revive-or-retire)
==================================================================

Gate: INV10-W1-3-SECOND-SOUND-CMB ([VERIFY])

Pre-registered threshold (plan §W1-3):
  PASS iff ℓ_second_sound = π·(c_fabric/c_Gold) is reproduced to <= 0.5% of the
  S53 value 720.9 (a reproduction check on the formula with the CURRENT
  canonical four-speed values) AND placed against Planck TT with a rendered
  REVIVE/RETIRE verdict. This is a VERIFY + characterization gate.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py  (c_fabric, c_Gold; feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  Planck TT peak/trough positions are EXTERNAL observational anchors, hardcoded
  with `# (local)` PLANCK provenance comments (not substrate constants).

Output 4-tuple:
  (value=720.93, scheme=FW, convention=RATIO, L_max=N/A)

Classification: PHONONIC

METHODOLOGY
-----------
The substrate IS a two-component resonator (a Goldstone sector at c_Gold and the
fabric phonon sector at c_fabric). Second sound IS its out-of-phase entropy wave,
PROVEN undamped (Q=75,989, S44 W6-2 / S68 obs horizon). The CMB multipole of a
sound horizon is ℓ = π·(d_geom/d_acoustic) = π·(c_fabric/c_Gold): the angular
projection of the horizon scale set by the SPEED RATIO (dimensionless, so the
multipole is independent of the M_KK scale). We (A) recompute ℓ_second_sound with
the current canonical speeds and check reproduction vs S53 720.9; (B) place 721
against the Planck 2018 TT acoustic-peak ladder (peaks + troughs), computing the
σ-distance to the nearest peak in peak-width units AND the local ΛCDM-curve
slope context; (C) render REVIVE (substrate-distinct resolvable feature) or
RETIRE (coincident with the standard ℓ₂→ℓ₃ third-peak shoulder / unresolvable).
Planck TT is the EXTERNAL anchor (methodological); the ℓ formula + Q=75,989 are
the substrate-first sources. The inventory-row WRITE is session-track mack
sole-writer — this gate produces the value + the verdict only.

DISCIPLINE
----------
- `from canonical_constants import *` (c_fabric, c_Gold)
- Every local/intermediate tagged `# (local)`
- numpy CPU, OMP_NUM_THREADS=8 cap (scalar arithmetic; no matrix >= 100x100)
- SHA-256 of all input files logged in first 20 lines of stdout
- dual-SHA (audit + content) emitted; verdict via emit_verdict MCP tool
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403  (provides c_fabric, c_Gold)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # cap before numpy import

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent          # computations/investigation-10/
COMPUTATIONS_DIR = SESSION_DIR.parent                  # computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "10"                                          # (local) investigation number
GATE_ID = "INV10-W1-3-SECOND-SOUND-CMB"                # (local)
SCHEME = "FW"                                           # (local)
CONVENTION = "RATIO"                                    # (local) ℓ ∝ c_fabric/c_Gold speed ratio
L_MAX = "N/A"                                           # (local) sound-speed-ratio gate, not a D_K compute

# Pre-registered reproduction threshold (define BEFORE running)
S53_REFERENCE_L = 720.9                                 # (local) S53 CMB-53 output-file value (l_second_sound)
REPRODUCTION_TOL_FRAC = 0.005                           # (local) 0.5% reproduction tolerance vs S53

# --- Planck 2018 TT acoustic-peak ladder (EXTERNAL observational anchors) ---
# PLANCK provenance: Planck 2018 results VI (cosmological parameters) +
# the well-established TT acoustic-peak positions. Peak (maxima) multipoles:
PLANCK_PEAKS = np.array([220.0, 537.5, 810.8, 1120.0, 1444.0])   # (local) PLANCK ℓ₁..ℓ₅ maxima
PLANCK_TROUGHS = np.array([410.0, 675.0, 965.0, 1290.0])         # (local) PLANCK 1st..4th TT minima
# Peak-width scale: the inter-peak spacing Δℓ_acoustic ≈ ℓ_A ≈ 300 (the acoustic
# scale; consecutive peak spacing ℓ_{n+1}-ℓ_n ≈ 270-310). Used as the peak-width
# unit for the σ-distance (a feature within ~1 peak-width of a peak is on its shoulder).
PLANCK_PEAK_WIDTH = 290.0                                        # (local) PLANCK mean inter-peak Δℓ (peak-width unit)
# Half-width of one peak's resolvable shoulder ~ half the inter-peak spacing:
PLANCK_PEAK_HALFWIDTH = PLANCK_PEAK_WIDTH / 2.0                  # (local) ≈145; a feature within this of a peak is unresolvable from it

OUT_NPZ = SESSION_DIR / "inv10_w1_second_sound_cmb.npz"
OUT_PNG = SESSION_DIR / "inv10_w1_second_sound_cmb.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # (A) Recompute the second-sound CMB horizon multipole with CURRENT speeds.
    #     ℓ_second_sound = π·(c_fabric/c_Gold)  [S53 CMB-53 second-sound horizon formula]
    speed_ratio = c_fabric / c_Gold                         # (local) 209.97368021 / 0.915
    l_second_sound = np.pi * speed_ratio                    # (local) the substrate-IS multipole

    # Reproduction check vs S53 output-file value 720.9
    repro_frac = abs(l_second_sound - S53_REFERENCE_L) / S53_REFERENCE_L  # (local)
    repro_pass = repro_frac <= REPRODUCTION_TOL_FRAC        # (local)

    # Companion horizons in the same two-sound hierarchy (S53 context, for the plot):
    l_geom = np.pi * 1.0                                    # (local) geometric horizon = full sky (=3.14)

    # (B) Planck TT placement: σ-distance to the nearest PEAK in peak-width units.
    dist_to_peaks = np.abs(PLANCK_PEAKS - l_second_sound)   # (local) |ℓ_2s − ℓ_peak_n|
    i_nearest_peak = int(np.argmin(dist_to_peaks))          # (local)
    l_nearest_peak = float(PLANCK_PEAKS[i_nearest_peak])    # (local)
    d_nearest_peak = float(dist_to_peaks[i_nearest_peak])   # (local) multipoles
    sigma_peak = d_nearest_peak / PLANCK_PEAK_WIDTH         # (local) σ-distance in peak-width units

    # σ-distance to nearest TROUGH (a feature ON a trough is the most distinct from peaks):
    dist_to_troughs = np.abs(PLANCK_TROUGHS - l_second_sound)  # (local)
    i_nearest_trough = int(np.argmin(dist_to_troughs))         # (local)
    l_nearest_trough = float(PLANCK_TROUGHS[i_nearest_trough]) # (local)
    d_nearest_trough = float(dist_to_troughs[i_nearest_trough])  # (local)

    # Interval placement: is ℓ_2s strictly between two consecutive peaks?
    l2_peak = float(PLANCK_PEAKS[1])                        # (local) ℓ₂ ≈ 537.5
    l3_peak = float(PLANCK_PEAKS[2])                        # (local) ℓ₃ ≈ 810.8
    in_l2_l3_interval = (l2_peak < l_second_sound < l3_peak)  # (local)

    # Resolvability test: a feature within one peak-HALFWIDTH (~145) of a standard
    # peak sits on that peak's shoulder and is NOT resolvable as a substrate-distinct
    # feature on the smooth ΛCDM TT curve. RESOLVABLE iff the σ-distance to the
    # NEAREST peak exceeds 0.5 peak-widths (i.e. d > halfwidth).
    resolvable_from_peak = d_nearest_peak > PLANCK_PEAK_HALFWIDTH  # (local)

    # (C) Revive-or-retire decision (rendered from the placement, not pre-judged):
    #   REVIVE iff: reproduction passes AND ℓ_2s falls in a peak-to-peak interval
    #               AND it is RESOLVABLE from the nearest standard peak (d > halfwidth).
    #   RETIRE   iff: reproduction passes BUT ℓ_2s is UNRESOLVABLE — within one
    #               peak-halfwidth of a standard peak (here ℓ₃), i.e. coincident with
    #               the standard third-peak shoulder ⇒ no substrate-distinct signature.
    #   FAIL (reproduction) iff: repro_frac > 0.5% (speeds drifted off S53).
    if not repro_pass:
        decision = "REPRODUCTION-FAIL"                     # (local)
    elif in_l2_l3_interval and resolvable_from_peak:
        decision = "REVIVE"                                # (local)
    else:
        decision = "RETIRE"                                # (local) coincident with standard peak shoulder

    return {
        "value": float(l_second_sound),
        "speed_ratio": float(speed_ratio),
        "l_geom": float(l_geom),
        "S53_reference": S53_REFERENCE_L,
        "repro_frac": float(repro_frac),
        "repro_pass": bool(repro_pass),
        "l_nearest_peak": l_nearest_peak,
        "i_nearest_peak": i_nearest_peak,
        "d_nearest_peak": d_nearest_peak,
        "sigma_peak": float(sigma_peak),
        "l_nearest_trough": l_nearest_trough,
        "d_nearest_trough": d_nearest_trough,
        "l2_peak": l2_peak,
        "l3_peak": l3_peak,
        "in_l2_l3_interval": bool(in_l2_l3_interval),
        "peak_halfwidth": PLANCK_PEAK_HALFWIDTH,
        "resolvable_from_peak": bool(resolvable_from_peak),
        "decision": decision,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    ell = np.linspace(2, 1500, 1500)  # (local) multipole axis

    # Schematic ΛCDM-like TT envelope (peaks at PLANCK_PEAKS, troughs between):
    # damped cosine modulation purely for visual placement context (NOT a fit).
    ell_A = PLANCK_PEAK_WIDTH                                   # (local) acoustic scale
    phase = np.pi * (ell - PLANCK_PEAKS[0]) / ell_A             # (local)
    damping = np.exp(-(ell / 1400.0) ** 1.8)                    # (local) Silk-damping-like envelope
    tt_schematic = (0.5 * (1 + np.cos(2 * phase)) * damping)    # (local) 0..1 schematic

    ax.plot(ell, tt_schematic, color="0.55", lw=1.3,
            label="ΛCDM TT (schematic envelope, placement context)")
    for j, lp in enumerate(PLANCK_PEAKS):
        ax.axvline(lp, color="0.75", ls=":", lw=0.9)
        ax.text(lp, 1.02, f"ℓ{j+1}", color="0.4", ha="center", fontsize=8)
    for lt in PLANCK_TROUGHS:
        ax.axvline(lt, color="0.85", ls=":", lw=0.7)

    lv = r["value"]
    ax.axvline(lv, color="crimson", lw=2.2,
               label=f"ℓ_second_sound = π·(c_fabric/c_Gold) = {lv:.2f}")
    ax.axvspan(lv - r["peak_halfwidth"], lv + r["peak_halfwidth"],
               color="crimson", alpha=0.08,
               label=f"±peak-halfwidth ({r['peak_halfwidth']:.0f})")

    ax.set_xlim(2, 1500)
    ax.set_ylim(0, 1.12)
    ax.set_xlabel("multipole  ℓ")
    ax.set_ylabel("TT power (schematic, arb. units)")
    ax.set_title(
        f"Second-sound CMB horizon: ℓ={lv:.2f}  |  nearest peak ℓ₃={r['l_nearest_peak']:.1f} "
        f"(d={r['d_nearest_peak']:.0f}, {r['sigma_peak']:.2f} peak-widths)  |  {r['decision']}"
    )
    ax.legend(loc="upper right", fontsize=8, framealpha=0.9)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload (race-safe emit_verdict path)
# ---------------------------------------------------------------------------
def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    payload: dict = {
        "session": int(SESSION),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    r = compute()

    # --- substitution chain (substituted numbers; per math-scripts.md) ---
    print("=== substitution chain (INV10-W1-3) ===")
    print(f"  Step 1: ℓ_second_sound := π·(c_fabric/c_Gold)        [S53 CMB-53 horizon formula]")
    print(f"  Step 2: c_fabric = {c_fabric} M_KK                    [S42, canonical]")
    print(f"  Step 3: c_Gold   = {c_Gold} M_KK                      [GL-JOSEPHSON-52, canonical]")
    print(f"  Step 4: speed_ratio = c_fabric/c_Gold = {r['speed_ratio']:.4f}")
    print(f"  Step 5: ℓ_second_sound = π·{r['speed_ratio']:.4f} = {r['value']:.4f}")
    print(f"  Step 6: reproduction vs S53 720.9: |Δ|/720.9 = {r['repro_frac']*100:.4f}%  "
          f"(tol 0.5%) -> {'PASS' if r['repro_pass'] else 'FAIL'}")
    print(f"  Step 7: Planck placement: ℓ₂={r['l2_peak']:.1f} < {r['value']:.2f} < ℓ₃={r['l3_peak']:.1f} "
          f"-> in ℓ₂→ℓ₃ interval: {r['in_l2_l3_interval']}")
    print(f"          nearest peak = ℓ₃ ≈ {r['l_nearest_peak']:.1f}; d = {r['d_nearest_peak']:.1f} multipoles "
          f"= {r['sigma_peak']:.3f} peak-widths")
    print(f"          nearest trough = {r['l_nearest_trough']:.1f}; d = {r['d_nearest_trough']:.1f}")
    print(f"          resolvable from nearest peak (d > halfwidth {r['peak_halfwidth']:.0f})? "
          f"{r['resolvable_from_peak']}")
    print(f"  -> DECISION: {r['decision']}")
    print()

    # --- gate verdict mapping ---
    # [VERIFY] gate: PASS = reproduction passes AND a revive/retire verdict is
    # rendered (REVIVE => live falsifiable feature). RETIRE => composite INFO
    # (the multipole reproduces cleanly but is unresolvable from the standard
    # peak shoulder — the prediction is closed honestly, not a reproduction
    # failure). REPRODUCTION-FAIL => FAIL (speeds drifted off S53).
    if r["decision"] == "REPRODUCTION-FAIL":
        verdict = "FAIL"  # (local)
    elif r["decision"] == "REVIVE":
        verdict = "PASS"  # (local)
    else:  # RETIRE
        verdict = "INFO"  # (local) reproduces, but unresolvable -> retire to atlas-09

    tuple4 = (f"(value={r['value']:.4f}, scheme={SCHEME}, "
              f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"4-tuple: {tuple4}")

    np.savez(
        OUT_NPZ,
        l_second_sound=r["value"],
        speed_ratio=r["speed_ratio"],
        c_fabric=c_fabric,
        c_Gold=c_Gold,
        l_geom=r["l_geom"],
        S53_reference=r["S53_reference"],
        repro_frac=r["repro_frac"],
        repro_pass=r["repro_pass"],
        planck_peaks=PLANCK_PEAKS,
        planck_troughs=PLANCK_TROUGHS,
        planck_peak_width=PLANCK_PEAK_WIDTH,
        peak_halfwidth=r["peak_halfwidth"],
        l_nearest_peak=r["l_nearest_peak"],
        d_nearest_peak=r["d_nearest_peak"],
        sigma_peak=r["sigma_peak"],
        l_nearest_trough=r["l_nearest_trough"],
        d_nearest_trough=r["d_nearest_trough"],
        in_l2_l3_interval=r["in_l2_l3_interval"],
        resolvable_from_peak=r["resolvable_from_peak"],
        decision=r["decision"],
        verdict=verdict,
    )
    print(f"saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(r)
    print(f"saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    note = (f"l_second_sound={r['value']:.4f} (S53 repro {r['repro_frac']*100:.4f}%); "
            f"nearest Planck peak l3={r['l_nearest_peak']:.1f} d={r['d_nearest_peak']:.0f} "
            f"({r['sigma_peak']:.2f} peak-widths); decision={r['decision']}; "
            f"second-sound Q=75989 PROVEN S44/S68")
    print_verdict_payload(
        verdict,
        f"{r['value']:.4f}",
        audit_sha,
        content_sha,
        companion_note=note,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
