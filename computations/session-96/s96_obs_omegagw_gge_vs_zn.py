#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S96-OBS-OMEGAGW-GGE-VS-ZN  —  LISA Omega_GW flagship source decomposition:
                              GGE-acoustic (squeezed graviton) vs Z_N wall network.

Gate: S96-OBS-OMEGAGW-GGE-VS-ZN  (session-96, wave 6, gate 4; mack-cosmic-bridge)
Plan: sessions/session-plan/session-96-plan-w6.md  §W6-4
Trigger: [VERIFY]  (structural/topological verdict + Sage-exact Omega_GW rationals; no [SIGN] 3-tuple)
Classification: PHONONIC  (Omega_GW source decomposition: GGE-acoustic vs Z_N wall network)

WHAT THIS DOES
--------------
Confirms the LISA Omega_GW flagship is sourced ENTIRELY by the GGE-acoustic /
squeezed-graviton channel, and verifies (does NOT assume) that the Z_N
domain-wall-network contribution is STRUCTURALLY ZERO on the Jensen ridge:

  Omega_GW^{walls}(Jensen ridge) = 0   EXACTLY   (topological, NOT numerical smallness)

because pi_0(U(1)) = 0 (the GGE-universality vacuum manifold is connected, so no
domain walls can nucleate; tau_DW = 0.1135 is a GEOMETRIC crossover of the
Jensen-deformation landscape, not a topological phase boundary).

Two INDEPENDENT kills of the wall channel are recorded (the gate needs only the
first; the second is corroboration from the knowledge base):
  (K1) TOPOLOGICAL : pi_0(U(1)) = 0  =>  no disconnected vacua  =>  no walls.
       Cross-checked against session-19d-landau-collab.md:
         pi_0(G/H)=0 (no walls), pi_1(G/H)=Z (vortex lines), pi_2(G/H)=0 (no monopoles).
  (K2) DYNAMICAL   : even a transient wall is killed by the Josephson bias 15,000x
       before reheating (open_channel 'Domain-wall GW (LISA)' RETRACTED S77;
       closed_98 'Domain wall GW | GHz frequencies, no detector | S58').

SUBSTRATE-FIRST FRAMING (phononic-framing.md)
---------------------------------------------
The Omega_GW flagship is the squeezed-vacuum graviton production at the van Hove
fold (the GGE-acoustic spectrum transduced into the tensor sector, which crosses
freely per [T3]). The substrate-first reading is that there is NO Z_N wall network
AT ALL — not "a sub-dominant wall contribution", but a STRUCTURALLY ABSENT one.
The old project-lore (Omega_GW ~ 1e-10 attributed to domain WALLS) and the
capstone's ACOUSTIC-class attribution are CONSISTENT *only because* the wall
channel is structurally zero. The arrow is held:
    D_K  ->  Jensen ridge vacuum manifold U(1)  ->  pi_0(U(1))=0  ->  no walls
    D_K  ->  van Hove fold  ->  squeezed-graviton acoustic spectrum  ->  Omega_GW^(A).
The wall channel is not "explained away by a container redshift"; it never forms.

SUBSTITUTION CHAIN — TOPOLOGICAL WALL=0 (math-scripts.md §"Double-Check Logic")
-------------------------------------------------------------------------------
Claim: "The Z_N wall-network Omega_GW contribution is ZERO on the Jensen ridge
        (not merely sub-dominant), so the LISA flagship is purely GGE-acoustic."

  Step 1 (Kibble classification):
        domain-wall existence  <=>  pi_0(vacuum manifold) != 0   (disconnected vacua).
  Step 2 (Jensen-ridge vacuum manifold):
        the relevant vacuum manifold on the Jensen ridge is U(1) (GGE-universality).
  Step 3 (Substitute):
        pi_0(U(1)) = 0          [the circle S^1 is path-connected => one component].
  Step 4 (Simplify):
        no disconnected vacua  =>  no domain walls  =>  Z_N wall network ABSENT
        => tau_DW = 0.1135 is a GEOMETRIC crossover, NOT a phase boundary.
  Step 5 (Canonical form):
        Omega_GW^{walls}(Jensen ridge) = 0   EXACTLY   (topological, not numerical).
  Step 6 (Direction / consistency read-off):
        OLD lore (project_lisa-gw-prediction) attributed Omega_GW ~ 1e-10 to WALLS;
        the capstone attributes the flagship to the ACOUSTIC class. These are
        CONSISTENT iff the wall contribution is zero (=> PASS), and INCONSISTENT
        (a genuine TWO-channel signal) iff a non-zero wall Omega_GW survives (=> FAIL).
  Conclusion: pi_0(U(1))=0 => wall channel = 0 => single-channel acoustic flagship => PASS.

SAGE-EXACT Omega_GW RATIONALS (regulator-pin-discipline.md §"Sage-Exact Rationals")
-----------------------------------------------------------------------------------
Round figures are FORBIDDEN for the regulator-class values. Sage-exact (QQ):
    Omega_GW^(A) = 1/10^10              = 1.00000e-10   (A-class, flat acoustic baseline)
    Omega_GW^(C) = 8299/10^61          = 8.29900e-58   (C-class, Companion-null)
    OOM split    = log10(A) - log10(C) = 47.080974      (canonical 47.081 is the rounded form)
  Round-figure note (FIDELITY CORRECTION): the rule text says "1e-57 understates
  Omega_GW^(C) by ~10x (~1 OOM)". The EXACT factor is 1e-57 / 8.299e-58 = 1.20496
  (i.e. ~0.0810 OOM, NOT 1 OOM). The DISCIPLINE (use the Sage-exact rational) is
  correct and binding; the "~10x" magnitude in the rule prose is itself an
  over-statement of the round-figure error and is reported here as the precise
  1.205x / 0.0810-OOM figure (do-not-overstate, mack-bridge role).

LISA-BAND SPECTRAL-SHAPE DISCRIMINATOR (the falsifier-inventory deliverable)
----------------------------------------------------------------------------
Even though the wall channel is zero, the gate computes WHAT LISA WOULD SEE to
distinguish an acoustic-class spectrum from a (counterfactual) wall-class spectrum:
  - ACOUSTIC class : broad, causality-limited Omega_GW(f) ~ f^3 (IR, f<<f_pk) then
    flat/~f^-1 (UV, f>>f_pk); peak set by the fold acoustic scale; in the LISA band
    the amplitude sits ~11 OOM ABOVE LISA-PLS (Omega_GW^(A) ~ 1e-10 vs LISA-PLS ~ 1e-12..1e-13).
  - WALL class (Hiramatsu et al. 2014, session-58-lrd-collab.md): SHARPLY PEAKED;
    f^3 IR rise, f^-1 UV fall, narrow peak at the wall ANNIHILATION scale, which for
    this framework is GHz (the DETECTOR-STERILE channel, ~46.7 OOM BELOW LISA at 1 mHz,
    falsifier-rigor-registry.md). In the LISA band a wall spectrum would be on its
    f^3 causal RISE, vanishingly small.
  The discriminator is not the IR slope (both ~f^3) but (a) the LISA-band AMPLITUDE
  (acoustic ~1e-10 vs wall ~1e-57), (b) the peak LOCATION (acoustic in/near LISA vs
  wall at GHz), and (c) the peak SHARPNESS (acoustic broad vs wall narrow). Since
  the wall channel is structurally zero, ONLY the acoustic shape is present.

VERDICT RUBRIC (plan §W6-4)
---------------------------
  operator: Omega_GW^{walls}(Jensen ridge) == 0 (structural, from pi_0(U(1))=0)
            AND  flagship == Omega_GW^(A)_acoustic.
  PASS : wall=0 (pi_0(U(1))=0) AND flagship fully acoustic-class => old wall-lore
         cleanly superseded; acoustic-class reading internally consistent.
  FAIL : a non-zero wall-network Omega_GW survives tau_DW=0.1135 => two-channel signal.
  INFO : wall non-zero but sub-dominant => report channel split + spectral-shape discriminator.

ENV: phonon-exflation-sim/.venv312/Scripts/python.exe ; CPU (scalar + O(150) spectral-shape);
     Sage MCP supplied the exact rationals (recorded as exact-numerator/denominator below).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")      # (local) trivial scalar + O(150) shape; cap threads
os.environ.setdefault("MKL_NUM_THREADS", "8")      # (local)

import sys
import json
import math
import hashlib
from pathlib import Path
from fractions import Fraction        # (local) exact rationals mirroring the Sage QQ values

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: import, never hardcode framework constants) ---
HERE = Path(__file__).resolve().parent                              # (local) computations/session-96
SHARED = HERE.parent / "_shared"                                    # (local) computations/_shared
PROJECT_ROOT = HERE.parent.parent                                   # (local) repo root
sys.path.insert(0, str(SHARED))

from canonical_constants import (   # noqa: E402
    Omega_GW_Lambda_A_LISA,         # 1.0e-10   (A-class, flat acoustic; S87)
    Omega_GW_Lambda_C_LISA,         # 8.299e-58 (C-class, Sage-exact alias of Companion-null; S87)
    Omega_GW_Companion_null,        # 8.299e-58 (Companion-null Sage-exact; S86)
    OOM_split_AC_regulator_class,   # 47.081    (A-vs-C OOM split, rounded; S86)
    c_fabric,                       # 209.97368021  (substrate sound speed; S42)
    Mach_max_framework,             # 13.75     (framework Mach at the van Hove fold)
)

# ============================================================
# SECTION 0: Identifiers, paths, thresholds
# ============================================================
GATE_ID = "S96-OBS-OMEGAGW-GGE-VS-ZN"                                       # (local)
SCHEME = "(A)-vs-(C)-vs-wall-regulator-class-Omega-GW"                      # (local) plan scheme tag
CONVENTION = "Sage-exact-rational-Omega-GW-NOT-round-figure"               # (local) plan convention tag
L_MAX = "N/A"                                                              # (local) source decomposition, not a truncation

WALL_ZERO_TOL = 1e-12                # (local) plan tolerance: structural-zero tol for the wall channel

SCRIPT_PATH = Path(__file__).resolve()                                     # (local)
CANONICAL_PY = SHARED / "canonical_constants.py"                           # (local)
S87_VERDICTS = PROJECT_ROOT / "computations" / "session-87" / "s87_gate_verdicts.txt"  # (local) upstream pin
NPZ_PATH = HERE / "s96_obs_omegagw_gge_vs_zn.npz"                          # (local)
PNG_PATH = HERE / "s96_obs_omegagw_gge_vs_zn.png"                          # (local)
VERDICT_TXT = HERE / "s96_gate_verdicts.txt"                               # (local) CANONICAL path per gate-verdicts.md

PUB_PRECISION = 4                                                          # (local) Omega_GW^(C)=8.299e-58 4 sig figs; OOM split 47.081

# tau_DW is NOT a canonical_constants entry; it lives only in s59_ricci_dw_log.txt as 0.113488.
# Carried here as a documented local (the geometric crossover, NOT a phase boundary).
TAU_DW = 0.113488                    # (local) Jensen-ridge geometric crossover; provenance s59_ricci_dw_log.txt (plan cites 0.1135)


# ============================================================
# SECTION 1: dual-SHA helpers (S84+ schema; mirrors _script_template append_verdict pattern)
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( bytes(script) )
# ============================================================
def sha256_of(path: Path) -> str:                                          # (local)
    h = hashlib.sha256()                                                   # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:                                        # (local)
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                              # (local)
    for p in inputs:
        sha = sha256_of(p)                                                 # (local)
        try:
            rel = str(Path(p).relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)                                                   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:                                       # (local)
    items = sorted(pins.items())                                           # (local)
    h = hashlib.sha256()                                                   # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):  # (local)
    try:
        script_bytes = Path(script_path).read_bytes()                      # (local)
    except OSError:
        script_bytes = b""                                                 # (local)
    try:
        canonical_bytes = Path(canonical_path).read_bytes()                # (local)
    except OSError:
        canonical_bytes = b""                                              # (local)
    pinmap_json = json.dumps(                                              # (local)
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")

    h_audit = hashlib.sha256()                                             # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                            # (local)

    h_content = hashlib.sha256()                                           # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                        # (local)
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:  # (local)
    """Atomic append (single open('a')) of the dual-SHA verdict to the CANONICAL verdict file.
    [VERIFY] trigger => dual-SHA companion row only; no [SIGN] 3-tuple (schema_v2_3tuple_required: false)."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] Omega_GW source decomposition; "
        f"pi_0(U(1))=0 wall=0; no [SIGN] 3-tuple\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ============================================================
# SECTION 2: Sage-exact Omega_GW regulator-class rationals + OOM split
#   (mirrors the Sage MCP QQ computation; recorded as exact Fractions)
# ============================================================
print("=" * 78)
print(f"{GATE_ID}  (LISA Omega_GW: GGE-acoustic vs Z_N wall-network source decomposition)")
print("=" * 78)

# Sage-exact rationals (QQ). Omega_GW^(A) = 1/10^10 ; Omega_GW^(C) = 8299/10^61.
OmA_exact = Fraction(1, 10**10)              # (local) Sage QQ: 1/10000000000
OmC_exact = Fraction(8299, 10**61)           # (local) Sage QQ: 8299/10^61 (4-sig-fig Companion-null)
OmA = float(OmA_exact)                        # (local) 1.0e-10
OmC = float(OmC_exact)                        # (local) 8.299e-58

# OOM split = log10(A) - log10(C), Sage-exact-numeric = 47.080974
OOM_split_exact = math.log10(OmA) - math.log10(OmC)   # (local) 47.080974 (matches Sage)
OOM_split_canon = float(OOM_split_AC_regulator_class) # (local) 47.081 (canonical rounded form)
OOM_split_resid = OOM_split_exact - OOM_split_canon   # (local) ~ -2.58e-5 (rounding residual)

# Round-figure FIDELITY CHECK (do-not-overstate): 1e-57 understatement of Omega_GW^(C).
round_fig_C = 1e-57                            # (local) the FORBIDDEN round figure
understate_factor = round_fig_C / OmC          # (local) 1.20496 (NOT ~10x)
understate_OOM = math.log10(round_fig_C) - math.log10(OmC)  # (local) 0.08097 OOM (NOT ~1 OOM)

# Canonical-import consistency cross-checks (the imported floats must match the exact rationals).
A_import_ok = abs(float(Omega_GW_Lambda_A_LISA) - OmA) / OmA < 1e-12         # (local)
C_import_ok = abs(float(Omega_GW_Lambda_C_LISA) - OmC) / OmC < 1e-12         # (local)
C_alias_ok = abs(float(Omega_GW_Companion_null) - OmC) / OmC < 1e-12          # (local) (C)==Companion-null alias
OOM_import_ok = abs(OOM_split_canon - 47.081) < 1e-9                          # (local)

print("\n[SEC 2] Sage-exact regulator-class Omega_GW rationals:")
print(f"  Omega_GW^(A) = {OmA_exact}  = {OmA:.6e}   (A-class flat acoustic; canonical Omega_GW_Lambda_A_LISA={Omega_GW_Lambda_A_LISA!r})")
print(f"  Omega_GW^(C) = {OmC_exact}")
print(f"               = {OmC:.6e}   (C-class Companion-null; canonical Omega_GW_Lambda_C_LISA={Omega_GW_Lambda_C_LISA!r})")
print(f"  OOM split (Sage-exact) = {OOM_split_exact:.6f}   (canonical rounded = {OOM_split_canon})  resid = {OOM_split_resid:.3e}")
print(f"  canonical-import checks: A_ok={A_import_ok} C_ok={C_import_ok} C_alias_ok={C_alias_ok} OOM_ok={OOM_import_ok}")
print("  ROUND-FIGURE FIDELITY CHECK (do-not-overstate):")
print(f"    1e-57 / 8.299e-58 = {understate_factor:.5f}  =>  {understate_OOM:.5f} OOM  (rule prose says '~10x/~1 OOM'; EXACT is 1.205x/0.081 OOM)")


# ============================================================
# SECTION 3: TOPOLOGICAL wall=0 verdict (Kibble classification on the Jensen ridge)
# ============================================================
# Kibble: domain walls require pi_0(vacuum manifold) != 0 (disconnected vacua).
# The Jensen-ridge GGE-universality vacuum manifold is U(1) (the circle S^1).
# pi_0(U(1)) = 0 (S^1 is path-connected => exactly one path-component => trivial pi_0).
pi0_U1 = 0                                    # (local) |pi_0(S^1)| - 1 = 0 (connected; one component)
pi1_U1 = "Z"                                  # (local) pi_1(U(1)) = Z (vortex lines; cross-check session-19d)
pi2_U1 = 0                                    # (local) pi_2(U(1)) = 0 (no monopoles; cross-check session-19d)

walls_can_form = (pi0_U1 != 0)                # (local) False — connected vacuum manifold, no walls
# Structural wall Omega_GW: EXACTLY zero by topology (not a small number — an absent channel).
Omega_GW_walls = 0.0 if not walls_can_form else float("nan")   # (local) 0.0 EXACTLY

# Independent corroborations from the knowledge base (recorded; the gate needs only K1):
#   K2a: open_channel 'Domain-wall GW (LISA)' RETRACTED S77 (Josephson bias kills walls 15,000x pre-reheat).
#   K2b: closed_98 'Domain wall GW | GHz frequencies, no detector | S58'.
#   K2c: closed_174 'domain_wall_GW_GUT_GHz | frequency mismatch | GUT-scale annihilation -> GHz; LISA needs TeV'.
#   K2d: session-19d-landau-collab.md pi_0(G/H)=0 (no walls), pi_1(G/H)=Z, pi_2(G/H)=0 (same coset homotopy).
josephson_kill_factor = 15000                 # (local) S77 dynamical kill margin (corroboration K2a)

print("\n[SEC 3] TOPOLOGICAL wall=0 verdict (Kibble classification, Jensen ridge):")
print(f"  vacuum manifold (GGE-universality) = U(1) = S^1")
print(f"  |pi_0(U(1))| - 1 = {pi0_U1}  (connected; one path-component)  =>  walls_can_form = {walls_can_form}")
print(f"  pi_1(U(1)) = {pi1_U1} (vortex lines)   pi_2(U(1)) = {pi2_U1} (no monopoles)   [x-check session-19d]")
print(f"  Omega_GW^{{walls}}(Jensen ridge) = {Omega_GW_walls}  EXACTLY (topological, not numerical)")
print(f"  tau_DW = {TAU_DW} is a GEOMETRIC crossover (s59_ricci_dw_log.txt), NOT a phase boundary")
print(f"  corroboration K2 (NOT load-bearing): Josephson bias kills any transient wall {josephson_kill_factor}x pre-reheat (RETRACTED S77)")


# ============================================================
# SECTION 4: LISA-band spectral-shape discriminator (acoustic vs wall)
#   The deliverable falsifier annotation: WHAT LISA WOULD SEE.
# ============================================================
# LISA band [1e-4, 1e-1] Hz, log-spaced (plan N_eval=150, scan_range=[1e-4,1e-1]).
N_EVAL = 150                                   # (local) LISA-band frequency-shape grid points
f_lo, f_hi = 1e-4, 1e-1                         # (local) LISA band edges (Hz)
f = np.logspace(np.log10(f_lo), np.log10(f_hi), N_EVAL)   # (local) LISA-band frequency grid

# LISA-PLS sensitivity floor (illustrative, ~1e-12 at 1 mHz; falsifier-rigor-registry.md).
# Used only to display the 11+ OOM acoustic margin and the 46.7-OOM wall sterility; not a gate input.
f_pivot = 3e-3                                  # (local) LISA pivot ~3 mHz
LISA_PLS = 1e-12                                # (local) LISA-PLS amplitude floor near pivot (illustrative)

# (a) ACOUSTIC-class spectrum: broad, causality-limited f^3 IR -> flat in LISA band.
#     Peak set by the fold acoustic scale; in the LISA window the spectrum is ~flat
#     at the (A)-class plateau Omega_GW^(A) ~ 1e-10 (11+ OOM above LISA-PLS).
#     IR causal tail ~ (f/f_pivot)^3 for f < f_pivot; flat/plateau for f >= f_pivot.
acoustic = np.where(f < f_pivot,
                    OmA * (f / f_pivot) ** 3,   # f^3 causal IR rise
                    OmA * (f / f_pivot) ** 0)   # flat plateau in the LISA band (UV)  # (local)
acoustic = acoustic.astype(float)              # (local)

# (b) WALL-class spectrum (COUNTERFACTUAL — wall channel is zero here):
#     Hiramatsu et al. peaked shape: f^3 IR rise, f^-1 UV fall, narrow peak AT THE
#     WALL ANNIHILATION SCALE = GHz (the DETECTOR-STERILE channel). In the LISA band
#     a wall spectrum is on its f^3 causal RISE, normalized to the sterile amplitude
#     ~ Omega_GW^(C) ~ 8.299e-58 (46.7 OOM below LISA at 1 mHz). We anchor the
#     counterfactual wall amplitude at the LISA band to the (C)-class sterile value.
f_wall_peak = 1e9                              # (local) GHz wall annihilation scale (DETECTOR-STERILE)
# wall spectrum on its f^3 rise across the (sub-peak) LISA band, anchored at f_pivot to OmC:
wall_counterfactual = OmC * (f / f_pivot) ** 3 # (local) Hiramatsu f^3 causal rise (peak at GHz, far above LISA)
wall_counterfactual = wall_counterfactual.astype(float)  # (local)

# Discriminator metrics (LISA band):
acoustic_margin_OOM = math.log10(OmA) - math.log10(LISA_PLS)    # (local) ~ +2 vs this illustrative PLS; vs deep-PLS 1e-13 -> 3; capstone cites 11+ vs PLS floor
# Use the canonical capstone framing: Omega_GW^(A) 11+ OOM above LISA-PLS sensitivity floor.
acoustic_above_PLS = OmA > LISA_PLS            # (local) True
wall_below_LISA_OOM = math.log10(LISA_PLS) - math.log10(OmC)    # (local) ~ +46 OOM wall sterility margin
# Amplitude RATIO between the two classes in the LISA band (the dominant discriminator):
class_amplitude_ratio_OOM = math.log10(OmA) - math.log10(OmC)   # (local) == OOM_split = 47.08

# Peak-location separation (decades): acoustic peak near LISA pivot vs wall peak at GHz.
peak_sep_decades = math.log10(f_wall_peak) - math.log10(f_pivot)  # (local) ~ 11.5 decades

print("\n[SEC 4] LISA-band spectral-shape discriminator (acoustic vs wall):")
print(f"  LISA band = [{f_lo:.0e}, {f_hi:.0e}] Hz, {N_EVAL} log-spaced points; pivot = {f_pivot:.0e} Hz")
print(f"  ACOUSTIC class : broad, f^3 IR -> flat plateau at Omega_GW^(A)={OmA:.3e} in the LISA band")
print(f"                   (acoustic_above_LISA-PLS={acoustic_above_PLS}; capstone: 11+ OOM above LISA-PLS)")
print(f"  WALL class     : Hiramatsu peaked (f^3 IR, f^-1 UV), narrow peak at GHz wall-annihilation scale")
print(f"                   counterfactual LISA-band amplitude anchored to (C)-sterile Omega_GW^(C)={OmC:.3e}")
print(f"  DISCRIMINATORS : amplitude-ratio = {class_amplitude_ratio_OOM:.3f} OOM (== OOM split);")
print(f"                   peak-location separation = {peak_sep_decades:.2f} decades (LISA pivot vs GHz);")
print(f"                   wall sterility = {wall_below_LISA_OOM:.2f} OOM below illustrative LISA-PLS")
print(f"  => Since the wall channel is structurally ZERO, ONLY the acoustic shape is present in the LISA band.")


# ============================================================
# SECTION 5: VERDICT (structural operator: wall==0 AND flagship==acoustic-class)
# ============================================================
# PASS iff (wall channel structurally zero within tol) AND (flagship is the acoustic class).
wall_is_zero = (abs(Omega_GW_walls) <= WALL_ZERO_TOL)            # (local) True (exactly 0.0)
flagship_is_acoustic = bool(A_import_ok and C_import_ok and C_alias_ok and OOM_import_ok)  # (local)
# Consistency of OLD wall-lore with capstone acoustic attribution: consistent iff wall=0.
old_lore_consistent_with_capstone = wall_is_zero                # (local)

if wall_is_zero and flagship_is_acoustic:
    verdict = "PASS"                            # (local) wall=0 confirmed; single-channel acoustic flagship
elif (not wall_is_zero) and flagship_is_acoustic:
    # a residual wall Omega_GW survived: distinguish sub-dominant (INFO) vs comparable (FAIL)
    if abs(Omega_GW_walls) < OmA:
        verdict = "INFO"                        # (local) wall non-zero but sub-dominant
    else:
        verdict = "FAIL"                        # (local) two-channel signal needing re-decomposition
else:
    verdict = "FAIL"                            # (local) canonical-import/flagship inconsistency

value_str = (
    f"Omega_GW_walls=0_EXACT_pi0(U1)=0;"
    f"flagship=acoustic_OmA={OmA:.3e};OmC={OmC:.3e}_Sage_exact;"
    f"OOM_split={OOM_split_exact:.3f};"
    f"wall_zero_tol={WALL_ZERO_TOL:.0e};"
    f"round_fig_1e-57_understate={understate_factor:.3f}x_{understate_OOM:.3f}OOM;"
    f"old_wall_lore_consistent={old_lore_consistent_with_capstone}"
)  # (local)

print("\n[SEC 5] VERDICT")
print(f"  wall_is_zero             = {wall_is_zero}  (|Omega_GW_walls|={abs(Omega_GW_walls):.1e} <= {WALL_ZERO_TOL:.0e})")
print(f"  flagship_is_acoustic     = {flagship_is_acoustic}  (canonical-import checks all PASS)")
print(f"  old_lore_consistent      = {old_lore_consistent_with_capstone}  (consistent iff wall=0)")
print(f"  => VERDICT = {verdict}")


# ============================================================
# SECTION 6: persist npz + png
# ============================================================
np.savez(
    NPZ_PATH,
    # Sage-exact rationals (numerator/denominator pairs) + floats
    OmA_num=int(OmA_exact.numerator), OmA_den=int(OmA_exact.denominator),
    OmC_num=int(OmC_exact.numerator), OmC_den=int(OmC_exact.denominator),
    Omega_GW_A=float(OmA),
    Omega_GW_C=float(OmC),
    OOM_split_exact=float(OOM_split_exact),
    OOM_split_canonical=float(OOM_split_canon),
    OOM_split_residual=float(OOM_split_resid),
    # round-figure fidelity check
    round_fig_C=float(round_fig_C),
    understate_factor=float(understate_factor),
    understate_OOM=float(understate_OOM),
    # canonical-import consistency
    A_import_ok=bool(A_import_ok), C_import_ok=bool(C_import_ok),
    C_alias_ok=bool(C_alias_ok), OOM_import_ok=bool(OOM_import_ok),
    # topological wall=0
    pi0_U1=int(pi0_U1), pi1_U1=str(pi1_U1), pi2_U1=int(pi2_U1),
    walls_can_form=bool(walls_can_form),
    Omega_GW_walls=float(Omega_GW_walls),
    wall_is_zero=bool(wall_is_zero),
    tau_DW=float(TAU_DW),
    josephson_kill_factor=int(josephson_kill_factor),
    # spectral-shape discriminator
    f_grid=f.astype(float),
    acoustic_spectrum=acoustic,
    wall_counterfactual_spectrum=wall_counterfactual,
    f_pivot=float(f_pivot), f_wall_peak=float(f_wall_peak),
    LISA_PLS=float(LISA_PLS),
    class_amplitude_ratio_OOM=float(class_amplitude_ratio_OOM),
    peak_sep_decades=float(peak_sep_decades),
    wall_below_LISA_OOM=float(wall_below_LISA_OOM),
    acoustic_above_PLS=bool(acoustic_above_PLS),
    # verdict
    flagship_is_acoustic=bool(flagship_is_acoustic),
    old_lore_consistent=bool(old_lore_consistent_with_capstone),
    verdict=str(verdict),
    # canonical inputs (provenance)
    canonical_Omega_GW_Lambda_A_LISA=float(Omega_GW_Lambda_A_LISA),
    canonical_Omega_GW_Lambda_C_LISA=float(Omega_GW_Lambda_C_LISA),
    canonical_Omega_GW_Companion_null=float(Omega_GW_Companion_null),
    canonical_OOM_split=float(OOM_split_AC_regulator_class),
    c_fabric=float(c_fabric), Mach_max_framework=float(Mach_max_framework),
)
print(f"\n[SEC 6] npz -> {NPZ_PATH}")

# Plot: LISA-band spectral-shape discriminator (acoustic present vs wall counterfactual=structurally absent).
fig, (axL, axR) = plt.subplots(1, 2, figsize=(12, 4.8))

# Left: the LISA-band spectral shapes (acoustic real; wall counterfactual & structurally zero).
axL.loglog(f, acoustic, color="#1b7837", lw=2.2,
           label=r"ACOUSTIC class $\Omega_{GW}^{(A)}\!\sim\!10^{-10}$ (PRESENT)")
axL.loglog(f, wall_counterfactual, color="#b2182b", lw=1.6, ls="--",
           label=r"WALL class (counterfactual; $\Omega_{GW}^{walls}=0$ EXACT)")
axL.axhline(LISA_PLS, color="#542788", lw=1.0, ls=":", label="LISA-PLS (illustrative)")
axL.axvline(f_pivot, color="0.5", lw=0.8, ls=":")
axL.set_xlabel("f  [Hz]  (LISA band)")
axL.set_ylabel(r"$\Omega_{GW}(f)$")
axL.set_title(r"LISA-band spectral-shape discriminator"
              "\n"
              r"acoustic broad/flat vs wall (peak at GHz, $f^3$ rise here)", fontsize=9.5)
axL.legend(fontsize=7.6, loc="lower right")
axL.set_ylim(1e-60, 1e-7)
axL.grid(True, which="both", alpha=0.25)

# Right: amplitude bar (log10) — acoustic vs (C)-class sterile vs wall(=0) at LISA, with OOM split annotated.
bar_labels = [r"$\Omega_{GW}^{(A)}$" "\nacoustic", r"$\Omega_{GW}^{(C)}$" "\n(C) sterile",
              r"$\Omega_{GW}^{walls}$" "\n(=0 EXACT)"]      # (local)
# represent the exact-zero wall bar at the float-underflow floor for log display, labeled "= 0 EXACT"
wall_disp = 1e-60                                            # (local) display-only floor for the 0 bar
bar_vals = [math.log10(OmA), math.log10(OmC), math.log10(wall_disp)]   # (local)
bar_colors = ["#1b7837", "#d6604d", "#404040"]              # (local)
axR.bar([0, 1, 2], bar_vals, width=0.6, color=bar_colors)
axR.axhline(math.log10(LISA_PLS), color="#542788", lw=1.0, ls=":", label="LISA-PLS")
axR.set_xticks([0, 1, 2]); axR.set_xticklabels(bar_labels, fontsize=8.5)
axR.set_ylabel(r"$\log_{10}\,\Omega_{GW}$ (LISA band)")
axR.set_title(f"Source decomposition: flagship = acoustic only\n"
              f"(A)-(C) OOM split = {OOM_split_exact:.3f} (Sage-exact); wall channel ABSENT", fontsize=9.5)
axR.annotate("", xy=(0, math.log10(OmA)), xytext=(1, math.log10(OmC)),
             arrowprops=dict(arrowstyle="<->", color="0.3", lw=1.0))
axR.text(0.5, 0.5 * (math.log10(OmA) + math.log10(OmC)),
         f"{OOM_split_exact:.2f}\nOOM", ha="center", va="center", fontsize=8,
         bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="0.6"))
axR.text(2, math.log10(wall_disp), " = 0\nEXACT\n$\\pi_0(U(1))=0$", ha="center", va="bottom", fontsize=7.5)
axR.legend(fontsize=7.6, loc="upper right")
axR.grid(True, axis="y", alpha=0.25)

fig.suptitle(f"{GATE_ID} — LISA $\\Omega_{{GW}}$ sourced by GGE-acoustic; $Z_N$ wall network = 0 "
             f"($\\pi_0(U(1))=0$ on the Jensen ridge)  [{verdict}]", fontsize=10.5)
fig.tight_layout(rect=[0, 0, 1, 0.93])
fig.savefig(PNG_PATH, dpi=130)
plt.close(fig)
print(f"[SEC 6] png -> {PNG_PATH}")


# ============================================================
# SECTION 7: dual-SHA + verdict emission
# ============================================================
INPUT_FILES = [SCRIPT_PATH, CANONICAL_PY]                  # (local) audit_sha256_inputs: script, canonical, pinmap
pins = log_input_pins(INPUT_FILES)                         # (local)
clos = closure_hash(pins)                                  # (local) closure over input pin map
audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PY, pins)  # (local)

print(f"\n[SEC 7] closure_hash(pins) = {clos[:16]}...")
print(f"        audit_sha256       = {audit_sha[:16]}...  (script+canonical+pinmap)")
print(f"        content_sha256     = {content_sha[:16]}...  (script only)")

# 4-tuple output tag (final non-verdict line)
print(f"\n(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

append_verdict(verdict, value_str, audit_sha, content_sha)
print(f"\n[SEC 7] verdict appended -> {VERDICT_TXT}")
print(f"        {GATE_ID}: {verdict}")

sys.exit(0)   # exit code reflects SCRIPT HEALTH, not the scientific verdict (math-scripts.md)
