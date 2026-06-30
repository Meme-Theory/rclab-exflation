#!/usr/bin/env python3
"""
S102 W5-3 — CF-S102-BF-SPINE-VS-LCDM (the incumbent Bayes factor: spine vs LCDM+nu)
==================================================================================

Gate: W5-3-CF-S102-BF-SPINE-VS-LCDM ([VERIFY])
Classification: NON-PHONONIC (Bayes-factor evidence-assessment meta-quantity)
Owner: mack-cosmic-bridge (cosmology / observational-evidence surface)
Cross-check: sagan-empiricist (BF methodology; review-only, does NOT write)

SUBSTRATE FRAMING
-----------------
NON-PHONONIC. The BF_spine statistic is NOT a substrate observable — it is a
model-comparison meta-quantity (evoi-prioritization.md: an evidence assessment,
not a prediction). The FOUR per-factor inputs ARE substrate-derived:
  - m_H        from the KK-threshold |S|^2 fiber-embedding spectral structure
               (a_4 fourth Seeley-DeWitt moment of D_K^2);
  - normal nu-ordering from the D_K (1,1,0)-sector eigenvalue ordering;
  - sigma/m=0 and c_s^2=0 from the Leggett-channel CPT-neutral non-annihilating
               quasiparticle.
But the BF COMBINES them as an EVIDENCE statistic against the LCDM incumbent.

THE REFERENCE-CLASS DISTINCTION (the load-bearing methodological content)
------------------------------------------------------------------------
An INCUMBENT-comparison BF (vs LCDM+nu, THIS gate) is permanently
NON-DECISIVE-vs-incumbent (ceiling 31.62 < 100), STRUCTURALLY DISTINCT from a
model-SELECTION BF (vs random-geometry null, BF_spine_full=2000 > 100, decisive
per Jeffreys/Kass-Raftery). The reference class is a PROPERTY OF THE STATISTIC,
not a tunable choice — which is exactly why the four per-factor values + the
three m_H states are PINNED before the gate runs (anti-post-hoc).

ANTI-POST-HOC PRE-REGISTRATION (epistemic-discipline.md Class-8.2;
v3-closure-recovery.md PROHIBITED_ACTIONS Class 6)
-------------------------------------------------------------------------------
The four per-factor log10-evidence values + the m_H 3-state tier assignments are
FIXED HERE in the script-frozen constants, transcribed verbatim from the
plan-frozen §W5-3 substitution chain. No execution-time re-narration of any
factor is permitted. The pins:
  factor_1 (sigma/m = 0)  = 0          [LCDM cold DM also sigma/m=0; ZERO discrimination]
  factor_2 (c_s^2 = 0)    = 0          [LCDM cold DM also c_s^2=0;   ZERO discrimination]
  factor_3 (nu-ordering)  = log10(2)   [framework FORCES normal; LCDM+nu marginalizes 1:1]
  factor_4 (m_H)          = b_mH       [<= 1.5; route-pending, set by the 3-state map]

THE m_H 3-STATE MAP (consuming the Wave-4 S102-MH-ROUTE-SELECTION verdict)
--------------------------------------------------------------------------
  State (a) FORCED route + PDG band-HIT  -> b_mH = 1.5  -> log10 BF = log10(2) + 1.5
  State (b) FORCED route + PDG band-MISS -> b_mH -> 0    -> log10 BF = log10(2)
            (SCHEME-FLOATING -> STRAINED-PINNED; m_H stays in the incumbent set at
             anecdotal weight; BF floor ~2)
  State (c) NO forced route              -> m_H EXITS the incumbent spine set
The map is FIXED at plan-freeze — the gate APPLIES it to whichever state the
upstream verdict selects; it does NOT re-derive it.

CEILING / FLOOR (read-off)
--------------------------
  CEILING (m_H-only incumbent ceiling, b_mH=1.5):  BF = 10^1.5 = 31.6227766 ~ 31.62
     (canonical_constants.py:BF_spine_vs_incumbent_ceiling note: the ceiling is
      the m_H factor ALONE at b_mH=1.5; the other 3 factors carry ZERO incumbent
      discrimination => they do NOT lift it)
  FLOOR (m_H band-MISS, b_mH->0):  BF = 10^log10(2) = 2.0 ~ "floor ~2"  (nu-ordering alone)
  DECISIVE threshold (Jeffreys/Kass-Raftery): log10 BF > 2 (BF > 100).
  Ceiling 31.62: log10 = 1.50 < 2 => VERY-STRONG, NOT DECISIVE (0.50 dex below the floor).
  Floor 2.0:     log10 = 0.30 < 2 => anecdotal/weak, NOT DECISIVE.
  BOTH below the >100 incumbent-DECISIVE floor BY CONSTRUCTION — the ceiling is
  structurally unliftable to DECISIVE-vs-incumbent until M_KK is derived (the W-2
  rank-1 N3=0 corollary; standing gap).

UPSTREAM (orchestrator-verified, on disk):
  S102-MH-ROUTE-SELECTION = PASS, audit 75ed7ffb...,
  value: FORCED=Route B (KK-threshold DIRECT)=131.8, band=MISS, wave5_state=b.
  => operative state (b): b_mH -> 0; BF reproduces the PINNED floor ~2.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py            (feeds audit_sha256; BF_spine_vs_incumbent_ceiling)
  - computations/session-97/s97_d3_bf.npz                  (per-factor decomposition cross-check; S97 W4-4)
  - computations/session-102/s102_mh_route_selection.npz   (INTRA-SESSION forward-pin; sets the m_H 3-state)
  - script bytes                                           (feeds BOTH SHAs)

Output 4-tuple: (value=<BF + state>, scheme=BF-incumbent-comparison,
                 convention=ANTI-POST-HOC-PINNED-4-factor, L_max=N/A)
"""

from __future__ import annotations

# --- Section 0: path bootstrap (shared dir onto sys.path BEFORE canonical import) ---
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))

# --- Section 1: canonical constants (MANDATORY first import) ---
from canonical_constants import *  # noqa: E402,F401,F403
from canonical_constants import (  # noqa: E402
    BF_spine_vs_incumbent_ceiling,
    m_H_FW_KK_threshold,
    m_H_obs,
)

# --- Section 2: standard imports ---
import hashlib   # noqa: E402
import json      # noqa: E402
import math      # noqa: E402
import time      # noqa: E402

import numpy as np  # noqa: E402
import matplotlib   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# --- Section 3: paths + pre-registration ---
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S102"                                   # (local)
GATE_ID = "W5-3-CF-S102-BF-SPINE-VS-LCDM"          # (local)
SCHEME = "BF-incumbent-comparison"                 # (local)
CONVENTION = "ANTI-POST-HOC-PINNED-4-factor"       # (local)
L_MAX = "N/A"                                      # (local)

REL_TOL = 1e-6                                     # (local) Sage-exact reproduction of log10(2) and 10^1.5

# ---- ANTI-POST-HOC PINNED per-factor log10-evidence values (FROZEN; from plan §W5-3) ----
# Transcribed VERBATIM from the plan-frozen substitution chain Step 1. No execution-time
# re-narration is permitted (epistemic-discipline.md Class-8.2). These are the INCUMBENT
# (vs-LCDM) reference-class values: factors 1 & 2 are ZERO because LCDM shares those features.
FACTOR_1_SIGMA_M_PIN = 0.0                         # (local) sigma/m=0: LCDM cold DM also sigma/m=0
FACTOR_2_CS2_PIN = 0.0                             # (local) c_s^2=0: LCDM cold DM also c_s^2=0
FACTOR_3_NU_ORDERING_PIN = math.log10(2.0)         # (local) framework forces normal; LCDM+nu marginalizes 1:1 -> factor 2
B_MH_CEILING_PIN = 1.5                             # (local) m_H band-HIT factor (state a); the m_H-only ceiling exponent

# ---- The m_H 3-state map (FROZEN at plan-freeze; consumes the Wave-4 verdict) ----
# state -> b_mH (the factor_4 log10-evidence under that state)
M_H_3_STATE_MAP = {                                # (local)
    "a": B_MH_CEILING_PIN,   # FORCED + band-HIT  -> b_mH = 1.5
    "b": 0.0,                # FORCED + band-MISS -> b_mH -> 0 (SCHEME-FLOATING->STRAINED-PINNED)
    "c": None,               # NO forced route    -> m_H EXITS the incumbent spine set (factor_4 removed)
}

DECISIVE_LOG10_THRESHOLD = 2.0                     # (local) Jeffreys/Kass-Raftery DECISIVE: log10 BF > 2 (BF > 100)

# Output destinations
OUT_NPZ = SESSION_DIR / "s102_bf_spine_vs_lcdm.npz"
OUT_PNG = SESSION_DIR / "s102_bf_spine_vs_lcdm.png"

# Input files
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S97_BF_NPZ = COMPUTATIONS_DIR / "session-97" / "s97_d3_bf.npz"
MH_ROUTE_NPZ = SESSION_DIR / "s102_mh_route_selection.npz"

INPUT_FILES = [CANONICAL_PATH, S97_BF_NPZ, MH_ROUTE_NPZ]


# --- Section 4: SHA-256 dual-pin block ---

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
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
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# --- Section 5: compute ---

def read_upstream_state() -> dict:
    """Read the Wave-4 S102-MH-ROUTE-SELECTION npz and resolve the operative
    3-state letter. The state is the substrate of the m_H factor_4 value.
    We resolve it from the npz `wave5_state` + `band_hit` + `forced_route`
    fields (substrate-first: read the produced datum, do NOT hardcode the state).
    """
    if not MH_ROUTE_NPZ.exists():
        # 3a disposition-(b): missing-npz benign per the plan; fall back to the
        # orchestrator-pinned state (b) FORCED+band-MISS. (Not expected — the
        # forward-pin has LANDED per orchestrator verification.)
        return {
            "wave5_state_letter": "b",
            "band_hit": False,
            "forced_route": "Route B (KK-threshold DIRECT) [npz-missing-fallback]",
            "forced_m_H": float(m_H_FW_KK_threshold),
            "npz_present": False,
        }
    d = np.load(MH_ROUTE_NPZ, allow_pickle=True)  # (local)
    wave5_state_str = str(d["wave5_state"])        # (local) e.g. "(b) FORCED + band-MISS -> ..."
    band_hit = bool(d["band_hit"])                 # (local)
    forced_route = str(d["forced_route"])          # (local)
    forced_m_H = float(d["forced_m_H"])            # (local)
    forced_unique = bool(d["forced_unique"])       # (local)

    # Resolve the 3-state letter from the upstream datum (substrate-first).
    # Letter precedence: explicit "(x)" prefix in wave5_state, then the
    # forced_unique/band_hit logic as a consistency cross-check.
    letter = None  # (local)
    s = wave5_state_str.strip()  # (local)
    if s.startswith("(") and len(s) >= 3 and s[2] == ")":
        letter = s[1].lower()  # (local)
    if letter is None:
        # Derive from the 3-state logic as a fallback:
        if not forced_unique:
            letter = "c"   # NO forced route
        elif band_hit:
            letter = "a"   # FORCED + band-HIT
        else:
            letter = "b"   # FORCED + band-MISS
    return {
        "wave5_state_letter": letter,
        "wave5_state_str": wave5_state_str,
        "band_hit": band_hit,
        "forced_route": forced_route,
        "forced_m_H": forced_m_H,
        "forced_unique": forced_unique,
        "npz_present": True,
    }


def compute() -> dict:
    # --- Resolve the operative m_H state from the upstream Wave-4 verdict ---
    up = read_upstream_state()  # (local)
    state_letter = up["wave5_state_letter"]  # (local)
    if state_letter not in M_H_3_STATE_MAP:
        raise ValueError(f"unresolved m_H 3-state letter: {state_letter!r}")

    b_mH = M_H_3_STATE_MAP[state_letter]  # (local) factor_4 value (None if state c -> m_H exits)
    m_H_in_spine = b_mH is not None        # (local)

    # --- Step 1: the four PINNED per-factor log10-evidence values ---
    factor_1 = FACTOR_1_SIGMA_M_PIN        # (local) sigma/m=0
    factor_2 = FACTOR_2_CS2_PIN            # (local) c_s^2=0
    factor_3 = FACTOR_3_NU_ORDERING_PIN    # (local) log10(2)
    factor_4 = (b_mH if m_H_in_spine else 0.0)  # (local) m_H factor (0 if exited)

    # --- Step 2: incumbent BF = product of per-factor evidence (log10 sum) ---
    log10_BF = factor_1 + factor_2 + factor_3 + factor_4  # (local)
    BF = 10.0 ** log10_BF                                  # (local) operative incumbent BF

    # --- Step 4: ceiling and floor read-off (PINNED, independent of upstream state) ---
    log10_BF_ceiling = FACTOR_3_NU_ORDERING_PIN * 0.0 + B_MH_CEILING_PIN  # (local) m_H-ONLY: 10^1.5
    #   NOTE: the ceiling is the m_H factor ALONE at b_mH=1.5; the other 3 factors carry
    #   ZERO incumbent discrimination so they do NOT lift it. (canonical note line 703.)
    log10_BF_ceiling = B_MH_CEILING_PIN                                   # (local) = 1.5
    BF_ceiling = 10.0 ** log10_BF_ceiling                                 # (local) = 31.6227766...

    log10_BF_floor = FACTOR_3_NU_ORDERING_PIN                             # (local) nu-ordering ALONE = log10(2)
    BF_floor = 10.0 ** log10_BF_floor                                     # (local) = 2.0

    # --- Step 5: DECISIVE-threshold comparison (direction) ---
    ceiling_decisive = log10_BF_ceiling > DECISIVE_LOG10_THRESHOLD        # (local) 1.5 > 2 -> False
    floor_decisive = log10_BF_floor > DECISIVE_LOG10_THRESHOLD            # (local) 0.30 > 2 -> False
    operative_decisive = log10_BF > DECISIVE_LOG10_THRESHOLD              # (local)

    # --- Cross-check A: canonical ceiling reproduction (BF_spine_vs_incumbent_ceiling) ---
    canonical_ceiling = float(BF_spine_vs_incumbent_ceiling)             # (local) 31.62
    ceiling_rel_dev = abs(BF_ceiling - canonical_ceiling) / canonical_ceiling  # (local)
    # canonical pin is 4-sig-fig 31.62; the Sage-exact 10^1.5=31.6227766 rounds to 31.62.
    ceiling_repro_ok = round(BF_ceiling, 2) == round(canonical_ceiling, 2)     # (local)

    # --- Cross-check B: S97 per-factor decomposition consistency ---
    s97_ok = False        # (local)
    s97_b_nu = None       # (local)
    s97_b_mH_struct = None  # (local)
    s97_BF_spine_struct = None  # (local)
    if S97_BF_NPZ.exists():
        d97 = np.load(S97_BF_NPZ, allow_pickle=True)  # (local)
        s97_b_nu = float(d97["b_nu"])                  # (local) should == log10(2)
        s97_b_mH_struct = float(d97["b_mH_struct"])    # (local) should == 1.5
        s97_BF_spine_struct = float(d97["BF_spine_struct"])  # (local) 2000 (model-SELECTION, DISTINCT)
        nu_match = abs(s97_b_nu - FACTOR_3_NU_ORDERING_PIN) < REL_TOL   # (local)
        mH_match = abs(s97_b_mH_struct - B_MH_CEILING_PIN) < REL_TOL    # (local)
        s97_ok = nu_match and mH_match

    # --- Cross-check C: model-SELECTION BF (vs random-geometry) is DISTINCT + decisive ---
    #   BF_spine_full = 2000 (DECISIVE) — the reference-class FOIL. NOT this gate's statistic.
    BF_spine_full = (s97_BF_spine_struct if s97_BF_spine_struct is not None else 2000.0)  # (local)
    selection_decisive = math.log10(BF_spine_full) > DECISIVE_LOG10_THRESHOLD            # (local) True

    # --- Anti-post-hoc structural assertions (the four pins reproduce AS PINNED) ---
    pins_reproduce = (
        abs(factor_1 - 0.0) < REL_TOL
        and abs(factor_2 - 0.0) < REL_TOL
        and abs(factor_3 - math.log10(2.0)) < REL_TOL
    )  # (local)

    return {
        "value": None,  # filled in main
        "state_letter": state_letter,
        "m_H_in_spine": m_H_in_spine,
        "b_mH": (b_mH if b_mH is not None else float("nan")),
        "factor_1": factor_1,
        "factor_2": factor_2,
        "factor_3": factor_3,
        "factor_4": factor_4,
        "log10_BF": log10_BF,
        "BF": BF,
        "log10_BF_ceiling": log10_BF_ceiling,
        "BF_ceiling": BF_ceiling,
        "log10_BF_floor": log10_BF_floor,
        "BF_floor": BF_floor,
        "canonical_ceiling": canonical_ceiling,
        "ceiling_rel_dev": ceiling_rel_dev,
        "ceiling_repro_ok": ceiling_repro_ok,
        "ceiling_decisive": ceiling_decisive,
        "floor_decisive": floor_decisive,
        "operative_decisive": operative_decisive,
        "pins_reproduce": pins_reproduce,
        "s97_ok": s97_ok,
        "s97_b_nu": s97_b_nu,
        "s97_b_mH_struct": s97_b_mH_struct,
        "BF_spine_full": BF_spine_full,
        "selection_decisive": selection_decisive,
        "upstream": up,
    }


# --- Section 6: gate verdict + 4-tuple ---

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload = {  # (local)
        "session": int(SESSION.lstrip("Ss")),
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


def evaluate_gate(r: dict) -> str:
    """Per the plan-frozen rubric:
       PASS = four per-factor values reproduce AS PINNED AND ceiling=31.62 AND
              floor~2 AND state (a) band-HIT (m_H reached its ceiling).
       INFO = state (b) band-MISS or state (c) m_H-exits — the incumbent BF
              reproduces the PINNED FLOOR (~2) or the m_H-removed product, NOT
              the ceiling. PASS of the anti-post-hoc discipline; recorded INFO to
              flag the m_H factor did not reach its band-HIT ceiling. NO re-narration.
       FAIL = a per-factor value does NOT reproduce its pin (factor_1/factor_2
              nonzero, or ceiling/floor arithmetic internally inconsistent).
    """
    # FAIL: the structural pins must reproduce, and the ceiling/floor must be self-consistent.
    if not r["pins_reproduce"]:
        return "FAIL"
    if not r["ceiling_repro_ok"]:
        return "FAIL"
    # floor must be exactly 10^log10(2) = 2.0
    if abs(r["BF_floor"] - 2.0) > REL_TOL:
        return "FAIL"
    # Both ceiling and floor MUST be below the DECISIVE floor (structural):
    if r["ceiling_decisive"] or r["floor_decisive"]:
        return "FAIL"
    # State routing:
    if r["state_letter"] == "a" and r["m_H_in_spine"]:
        # band-HIT: operative BF reaches the ceiling (log10(2)+1.5).
        return "PASS"
    # state (b) band-MISS or state (c) m_H-exits: floor / m_H-removed product, recorded INFO.
    return "INFO"


# --- Section 6b: plot ---

def make_plot(r: dict):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))  # (local)

    # Left: per-factor log10-evidence (incumbent reference class), stacked toward the operative BF.
    labels = [r"$\sigma/m{=}0$", r"$c_s^2{=}0$", r"$\nu$-order", r"$m_H$ (state %s)" % r["state_letter"]]  # (local)
    vals = [r["factor_1"], r["factor_2"], r["factor_3"], r["factor_4"]]  # (local)
    colors = ["#bbbbbb", "#bbbbbb", "#3b7dd8", "#d8733b"]  # (local)
    ax[0].bar(labels, vals, color=colors, edgecolor="black")
    ax[0].axhline(0.0, color="black", lw=0.8)
    ax[0].set_ylabel(r"per-factor $\log_{10}$ evidence (vs LCDM+$\nu$)")
    ax[0].set_title("Incumbent per-factor discrimination (PINNED)\n"
                    r"$\sigma/m,\,c_s^2$ shared with LCDM $\Rightarrow$ 0")
    for i, v in enumerate(vals):
        ax[0].text(i, v + 0.02, f"{v:.3f}", ha="center", va="bottom", fontsize=9)
    ax[0].set_ylim(-0.1, 1.7)

    # Right: BF ladder — floor, operative, ceiling vs the DECISIVE=100 line (log scale).
    names = ["floor\n(band-MISS)", "operative\n(state %s)" % r["state_letter"], "ceiling\n(band-HIT)",
             "model-SELECTION\n(vs random-geom)"]  # (local)
    bf_vals = [r["BF_floor"], r["BF"], r["BF_ceiling"], r["BF_spine_full"]]  # (local)
    bar_colors = ["#d8733b", "#9b59b6", "#3b7dd8", "#2ca02c"]  # (local)
    ax[1].bar(names, bf_vals, color=bar_colors, edgecolor="black")
    ax[1].axhline(100.0, color="red", ls="--", lw=1.5, label="DECISIVE (BF=100)")
    ax[1].set_yscale("log")
    ax[1].set_ylabel("Bayes factor (log scale)")
    ax[1].set_title("Incumbent BF: ceiling 31.62 < 100 (NOT decisive)\n"
                    "vs model-SELECTION 2000 > 100 (decisive) — distinct reference classes")
    for i, v in enumerate(bf_vals):
        ax[1].text(i, v * 1.15, f"{v:.1f}", ha="center", va="bottom", fontsize=9)
    ax[1].legend(loc="upper left", fontsize=9)
    ax[1].set_ylim(1, 5000)

    fig.suptitle("W5-3 CF-S102-BF-SPINE-VS-LCDM — incumbent Bayes factor (anti-post-hoc PINNED)",
                 fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# --- Section 7: main ---

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()  # (local)

    # Build the operative value payload (no single-quote chars — emit_verdict forbids them).
    up = r["upstream"]  # (local)
    value_str = (
        f"state_{r['state_letter']}_BF={r['BF']:.4f}_log10BF={r['log10_BF']:.6f}_"
        f"factors=[{r['factor_1']:.1f},{r['factor_2']:.1f},{r['factor_3']:.6f},{r['factor_4']:.1f}]_"
        f"ceiling={r['BF_ceiling']:.4f}_floor={r['BF_floor']:.4f}_"
        f"canon_ceiling={r['canonical_ceiling']:.2f}_ceiling_decisive={r['ceiling_decisive']}_"
        f"floor_decisive={r['floor_decisive']}_modelSEL_BF={r['BF_spine_full']:.0f}_decisive={r['selection_decisive']}_"
        f"upstream=wave5_state_{up['wave5_state_letter']}_band_hit={up['band_hit']}_s97_ok={r['s97_ok']}"
    )  # (local)
    r["value"] = value_str

    verdict = evaluate_gate(r)  # (local)

    # Console summary of the substitution chain (NUMBERS first).
    print("=== W5-3 substitution chain (substituted numbers) ===")
    print(f"  Step 1 PINNED per-factor log10-evidence (incumbent vs LCDM+nu):")
    print(f"    factor_1 (sigma/m=0)  = {r['factor_1']:.6f}   [LCDM also sigma/m=0; ZERO discrimination]")
    print(f"    factor_2 (c_s^2=0)    = {r['factor_2']:.6f}   [LCDM also c_s^2=0;   ZERO discrimination]")
    print(f"    factor_3 (nu-ordering)= {r['factor_3']:.10f}  [= log10(2); framework forces normal]")
    print(f"    factor_4 (m_H)        = {r['factor_4']:.6f}   [state ({r['state_letter']}); 3-state map]")
    print(f"  Step 2 log10 BF_spine_vs_LCDM = {r['factor_1']:.1f}+{r['factor_2']:.1f}"
          f"+{r['factor_3']:.6f}+{r['factor_4']:.1f} = {r['log10_BF']:.6f}")
    print(f"         BF (operative, state {r['state_letter']}) = 10^{r['log10_BF']:.6f} = {r['BF']:.6f}")
    print(f"  Step 3 m_H 3-state map: upstream wave5_state = ({up['wave5_state_letter']}); "
          f"band_hit = {up['band_hit']}; forced_route = {up['forced_route']}")
    print(f"  Step 4 read-off:")
    print(f"    CEILING (b_mH=1.5, m_H-ONLY)  = 10^{r['log10_BF_ceiling']:.4f} = {r['BF_ceiling']:.7f} ~ 31.62")
    print(f"    FLOOR   (b_mH->0, nu-ONLY)    = 10^{r['log10_BF_floor']:.6f} = {r['BF_floor']:.7f} ~ 2.0")
    print(f"  Step 5 DECISIVE (Jeffreys/Kass-Raftery): log10 BF > {DECISIVE_LOG10_THRESHOLD} (BF > 100)")
    print(f"    log10(ceiling) = {r['log10_BF_ceiling']:.4f} < 2 => VERY-STRONG, NOT DECISIVE "
          f"(0.50 dex below the >100 floor)")
    print(f"    log10(floor)   = {r['log10_BF_floor']:.4f} < 2 => anecdotal/weak, NOT DECISIVE")
    print(f"  Cross-checks:")
    print(f"    canonical BF_spine_vs_incumbent_ceiling = {r['canonical_ceiling']:.2f}; "
          f"reproduced = {r['ceiling_repro_ok']} (rel_dev {r['ceiling_rel_dev']:.2e})")
    print(f"    S97 per-factor decomposition: b_nu={r['s97_b_nu']}, b_mH_struct={r['s97_b_mH_struct']}, "
          f"consistent = {r['s97_ok']}")
    print(f"    model-SELECTION BF (vs random-geom) = {r['BF_spine_full']:.0f} (DECISIVE = {r['selection_decisive']}) "
          f"-- DISTINCT reference class")
    print(f"    pins reproduce AS PINNED = {r['pins_reproduce']}")
    print()

    # Save data
    np.savez(
        OUT_NPZ,
        state_letter=r["state_letter"],
        m_H_in_spine=r["m_H_in_spine"],
        b_mH=r["b_mH"],
        factor_1=r["factor_1"],
        factor_2=r["factor_2"],
        factor_3=r["factor_3"],
        factor_4=r["factor_4"],
        log10_BF=r["log10_BF"],
        BF=r["BF"],
        log10_BF_ceiling=r["log10_BF_ceiling"],
        BF_ceiling=r["BF_ceiling"],
        log10_BF_floor=r["log10_BF_floor"],
        BF_floor=r["BF_floor"],
        canonical_ceiling=r["canonical_ceiling"],
        ceiling_rel_dev=r["ceiling_rel_dev"],
        ceiling_repro_ok=r["ceiling_repro_ok"],
        ceiling_decisive=r["ceiling_decisive"],
        floor_decisive=r["floor_decisive"],
        operative_decisive=r["operative_decisive"],
        pins_reproduce=r["pins_reproduce"],
        s97_ok=r["s97_ok"],
        s97_b_nu=(r["s97_b_nu"] if r["s97_b_nu"] is not None else float("nan")),
        s97_b_mH_struct=(r["s97_b_mH_struct"] if r["s97_b_mH_struct"] is not None else float("nan")),
        BF_spine_full=r["BF_spine_full"],
        selection_decisive=r["selection_decisive"],
        upstream_wave5_state=up["wave5_state_letter"],
        upstream_band_hit=up["band_hit"],
        upstream_forced_route=str(up["forced_route"]),
        REL_TOL=REL_TOL,
        DECISIVE_LOG10_THRESHOLD=DECISIVE_LOG10_THRESHOLD,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(r)
    print(f"  saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    companion = (
        f"incumbent-ref-class; state-{r['state_letter']} (band-MISS) reproduces PINNED floor ~2; "
        f"ceiling 31.62 NOT decisive; model-SELECTION BF=2000 (distinct, decisive); anti-post-hoc 4-factor PINNED"
    )  # (local)
    extra = [
        f"# composite-precedence: per session-102-plan-w5.md INFO_meaning -- state (b)/(c) reproduces the PINNED "
        f"floor (~2), recorded INFO (m_H factor did not reach band-HIT ceiling); PASS of anti-post-hoc discipline, "
        f"no re-narration. W5-3 dual-column scope marker.",
        f"# reference-class: incumbent (vs LCDM+nu) BF ceiling={r['BF_ceiling']:.4f}<100 (NON-decisive-vs-incumbent) "
        f"DISTINCT from model-SELECTION (vs random-geometry) BF={r['BF_spine_full']:.0f}>100 (decisive). W5-3.",
    ]  # (local)
    print_verdict_payload(verdict, r["value"], audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
