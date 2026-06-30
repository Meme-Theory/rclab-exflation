#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-LEGGETT-GAMMA-GRAV
================================================================================
Gate:   S96-LEGGETT-GAMMA-GRAV   (trigger [SIGN], classification PHONONIC)
Agent:  gen-physicist (cross-domain workhorse; dissonance D1 Gamma_grav margin)
Plan:   sessions/session-plan/session-96-plan-w3.md  ## §W3-2
WP:     sessions/archive/session-96/session-96-w3-workingpaper.md  ### §W3-2

HYPOTHESIS
--------------------------------------------------------------------------------
The Leggett-channel GGE dark-matter quasiparticle's gravitational decay rate
Gamma_grav (the PHYSICAL surviving rate), computed FRESH from the canonical
Eq. QA-9 graviton vertex with substrate-pinned canonical parameters, satisfies
Gamma_grav < H_0 by a large dimensionless margin (Gamma_grav/H_0 << 1) across the
substrate-derived epsilon-band [0.005, 0.011] -- discharging the CRITICAL
conditional under Omega_DM h^2 = 0.120 (LEGGETT-GRAV-DECAY-67) with an EXPLICIT
first-principles margin number, RE-PINNED from canonical constants (resolving D1:
the S95 LEGGETT-GRAV-DECAY-CONDITIONAL row only CITED the S67/S73a archive figure
~8.85e-66 as a falsifier-inventory annotation; it was never re-pinned from a
canonical first-principles compute).

THE D1 PHYSICS (the dissonance the gate discharges; settled S66 workshop -> S67 -> S73a):
--------------------------------------------------------------------------------
The knowledge graph lists this gate SIMULTANEOUSLY as a defined PASS gate
(PASS: Gamma_grav<H_0) AND in "UNCOMPUTED decisive tests / 4 CRITICAL". That
simultaneity IS the dissonance, and it has a precise physical origin:

  CHANNEL (a) -- the NAIVE single-Leggett 4D vertex L -> g+g.  Eq. QA-9
    Gamma_KK = eps^2 * omega_L^3 * Delta^2 / (64*pi*M_Pl^4) * (omega_L/M_KK)^4
    gives Gamma_KK/H_0 ~ 10^{29}-10^{39} (S66 Eq. QA-10: "cosmologically instant",
    flagged as a GENUINE PROBLEM -- this is the "UNCOMPUTED CRITICAL" reading).
    This channel does NOT survive: it is FORBIDDEN EXACTLY by Z_2 parity
    (a_2(phi_23)=a_2(-phi_23); cos is even; Delta n_L = -1 is ODD => Gamma_single = 0
    to ALL orders, S67/S73a PROVEN) AND by graviton-gap kinematic protection
    (each KK graviton costs ~M_KK; 2*M_KK >> omega_L=0.138 M_KK).

  CHANNEL (b) -- the PHYSICAL surviving channel: pair annihilation 2L -> 2g
    (Delta n_L = -2 is EVEN => ALLOWED). Gamma_pair = n_L * <sigma v> with
    <sigma v> = xi_eff^2 * m_L^2 / (960*pi*M_Pl^4), xi_eff = frac_d2a2 * phi_zp^2,
    n_L = Omega_DM * rho_crit / m_L. This gives Gamma_pair/H_0 ~ 9.28e-66 (the
    archive anchor ~8.85e-66 IS this pair-channel margin) -- the "defined PASS" reading.

The gate's DELIVERABLE margin is the PHYSICAL surviving rate Gamma_grav := Gamma_pair
(channel b). Channel (a) is reported as the naive/forbidden rate with the graviton-gap
+ Z_2-parity protection as the STRUCTURAL REASON it is irrelevant to relic survival.
Reading the QA-9 single-Leggett vertex magnitude AS the survival margin is the error
this gate corrects -- it is the wrong observable; the surviving-channel rate is the right one.

SUBSTRATE ARROW (phononic-framing.md; never inverted):
    D_K eigenvalues -> Leggett inter-band coherence mode omega_L = 0.138 M_KK
    -> Z_2 parity of a_2(phi_23) + graviton-gap kinematic protection (the graviton
       gap forbids single-Leggett decay the way the BCS gap forbids quasiparticle decay)
    -> physical surviving decay-rate margin Gamma_pair / H_0.
The dark matter IS a Leggett-channel GGE quasiparticle of the fabric, NOT a particle
moving IN a gravitational background. H_0 enters as the READOUT of the emergent expansion
rate the relic must outlive, NOT as an external clock the relic decays in.

--------------------------------------------------------------------------------
SUBSTITUTION CHAIN ([SIGN] trigger -- MANDATORY, math-scripts.md
                   §"Double-Check Logic Before Compute")
--------------------------------------------------------------------------------
Claim: "Gamma_grav (physical surviving rate) < H_0 by a large dimensionless margin
        (Gamma_grav/H_0 << 1) ==> the Leggett-channel DM relic SURVIVES to today
        ==> Omega_DM h^2=0.120 stands; the CRITICAL conditional LEGGETT-GRAV-DECAY-67
        is satisfied with an explicit margin (resolving D1)."

Step 1 -- Definitions (cite canonical source):
  Eq. QA-9 (naive single-Leggett, channel a):
    Gamma_KK = eps^2 * omega_L^3 * Delta^2 / (64*pi * M_Pl^4) * (omega_L/M_KK)^4
                   [Eq. QA-9, session-66-mack-qa-workshop.md:354]
  Z_2 parity selection rule:  Gamma_single(L->g+g) = 0 EXACTLY (S67/S73a PROVEN).
  Physical surviving channel (b), pair annihilation 2L->2g:
    <sigma v> = xi_eff^2 * m_L^2 / (960*pi*M_Pl^4)   [S67 §6; Kolb-Turner conformal coupling]
    Gamma_pair = n_L * <sigma v>,   n_L = Omega_DM * rho_crit / m_L
    xi_eff = frac_d2a2 * phi_zp^2   [effective conformal coupling; frac_d2a2 from S67]
  omega_L        = omega_L1 = 0.138 M_KK                 [canonical_constants.py:679]
  m_L            = omega_L1 * M_KK_gravity (GeV)         [Leggett mass in GeV]
  Delta_BCS      = 0.4642547394830737 (M_KK units)       [canonical, R-protected, BCS-GAP-CANONICAL-70]
  M_KK           = M_KK_gravity = 7.428660036284456e16 GeV  [canonical, CONST-FREEZE-42]
  M_Pl           = M_Pl_reduced = 2.435e18 GeV           [canonical_constants.py:37, CODATA 2018]
  epsilon        = Delta_Leggett/Delta_Josephson in [0.005, 0.011]  [S56 gap ratio band]
  Omega_DM       = 0.2657   rho_crit = 4.08e-47 GeV^4    [canonical_constants.py:90,95]
  H_0            = H_0_inv_s = 2.184e-18 s^{-1}          [canonical_constants.py:73]
                   (equivalently H_0_GeV = 1.438e-42 GeV, line 74)
  hbar           = hbar_GeV_s = 6.582119569e-25 GeV*s    [canonical_constants.py:66]

Step 2 -- Substitute (dimensional bookkeeping; M_KK units -> GeV; no simplification yet):
  All M_KK-unit quantities -> GeV by multiplying by M_KK_gravity:
    omega_L_GeV   = omega_L1 * M_KK_gravity ;  m_L = omega_L_GeV
    Delta_BCS_GeV = Delta_BCS * M_KK_gravity
  CRITICAL dimensional note (CC1): (omega_L/M_KK)^4 = (0.138 M_KK / 1 M_KK)^4 = (0.138)^4
    is DIMENSIONLESS (ratio of two M_KK quantities; picks up NO units).
  Channel (a): Gamma_KK(GeV) = eps^2 * omega_L_GeV^3 * Delta_BCS_GeV^2 / (64*pi*M_Pl_GeV^4)
                                       * (omega_L1)^4
    [numerator omega^3*Delta^2 = GeV^5; /M_Pl^4 = GeV^{-4}; net GeV^1; (omega/M_KK)^4 dimensionless]
  Channel (b): <sigma v>(GeV^{-2}) = xi_eff^2 * m_L^2 / (960*pi*M_Pl_GeV^4)
               n_L(GeV^3) = Omega_DM * rho_crit_GeV4 / m_L
               Gamma_pair(GeV) = n_L * <sigma v>   [GeV^3 * GeV^{-2} = GeV^1]
  Gamma (s^{-1}) = Gamma(GeV) / hbar_GeV_s

Step 3 -- Simplify to canonical form (the dimensionless margin; one step per line):
  Gamma_grav := Gamma_pair  (the PHYSICAL surviving channel; single channel = 0 by Z_2)
  ratio = Gamma_grav / H_0   (both in GeV, OR both in s^{-1} -- ratio convention-free)
  Suppression budget for channel (b):
    1/M_Pl^4 graviton coupling + relic dilution n_L/m_L + xi_eff^2 Z_2-second-order coupling
    => Gamma_pair/H_0 ~ 1e-65 (the archive pair-channel anchor).
  For channel (a) the explicit factors (reported as diagnostic; channel forbidden):
    (omega_L/M_KK)^4 = (0.138)^4 = 3.6266e-4 ;  (M_KK/M_Pl)^4 ~ 8.66e-7 ;  eps^2 ~ 6.4e-5.
  margin_OOM = log10(H_0 / Gamma_grav)

Step 4 -- Direction / sign read-off (ONLY now):
  ratio = Gamma_pair/H_0 << 1  (expected ~1e-65 per the S67/S73a archive cross-check ~8.85e-66)
  ==> Gamma_grav < H_0 ==> the Leggett DM relic does NOT decay within a Hubble time
  ==> Omega_DM h^2 = 0.120 stands (CRITICAL conditional satisfied).
  sign_verdict PASS iff ratio < 1 (direction matches predicted survival) across the WHOLE
    epsilon-band; FAIL iff ratio >= 1 anywhere in the band (DM sector would collapse).
  magnitude_verdict PASS iff ratio < 1 with margin_OOM > 1 (decisively safe); INFO iff
    1 <= ratio < 10 (marginal, re-flag); FAIL iff ratio >= 10.

Conclusion: A ratio << 1 with the predicted direction across the epsilon-band confirms
  Gamma_grav<H_0 from canonical first-principles pins (NOT the cited S67 archive figure),
  discharging D1: the gate verdict PASS-confirms nazarewicz's PASS reading WHILE supplying
  the explicit margin number the open-CRITICAL readers (landau/mack/hawking) correctly noted
  was uncomputed -- AND explicitly reconciles WHY the gate read as both "PASS" and "UNCOMPUTED
  CRITICAL": the naive QA-9 single-Leggett channel (~10^{39} H_0) is the open-problem flag, but
  it is Z_2-FORBIDDEN to exactly zero; the physical surviving pair channel is ~1e-65 H_0. A
  ratio >= 1 (not expected) would FAIL the conditional -- informative either way
  (math-scripts.md §"All Results Are Good Results").

--------------------------------------------------------------------------------
PRE-REGISTERED VERDICT RUBRIC ([SIGN]; gate-block §W3-2)
operator: inequality -> ratio = Gamma_grav(physical surviving)/H_0 (vs 1)
strict_PASS_boundary: ratio < 1 (the decay-vs-Hubble crossover at ratio=1)
PASS : ratio < 1 with margin_OOM > 1 across the WHOLE epsilon-band -> relic survives;
       LEGGETT-GRAV-DECAY-67 satisfied with explicit margin; D1 resolved
INFO : 1 <= ratio < 10 (marginal) -> re-flag MARGINAL-PENDING-REFINEMENT
FAIL : ratio >= 10 anywhere in band -> Leggett-DM corridor collapses

3-tuple companion (schema-v2, [SIGN] directional pre-reg):
  sign_verdict      PASS iff ratio < 1 across the whole band (predicted survival direction)
  magnitude_verdict PASS/INFO/FAIL on ratio vs (1 / 10)
  regime_verdict    VALID iff (dimensional bookkeeping closes: (omega_L/M_KK)^4 dimensionless)
                    AND (canonical SHA pins match) AND (closed-form rate, no truncation regime)
                    AND (CC2 anchor cross-check within OOM band)
Composite collapse per gate-verdicts.md.

NO SCHEMATIC helper consumed; CLASS=FULL (closed-form Eq. QA-9 + pair-channel rate from
canonical scalar pins + substrate frac_d2a2/phi_zp from the S67 pinned npz), per
substrate-first-canonical-sourcing.md §(iv). regulator_pin=N/A (tree graviton-vertex decay
rate, not a Seeley-DeWitt heat-kernel moment). The S67/S73a archive figure ~8.85e-66 is the
CROSS-CHECK ANCHOR (CC2), NOT the pin -- this gate RE-DERIVES the margin from canonical pins.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) CPU thread cap; scalar arithmetic over an 11-pt band, no matrices
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: from canonical_constants import *) ---
SHARED = Path(__file__).resolve().parent                           # (local) this script lives in computations/_shared/
sys.path.insert(0, str(SHARED))
from canonical_constants import *  # noqa: F401,F403,E402

# explicit names actually used (also covered by the star import; named for clarity/audit)
from canonical_constants import (  # noqa: E402
    omega_L1, Delta_BCS, M_KK_gravity, M_Pl_reduced,
    H_0_inv_s, H_0_GeV, hbar_GeV_s, PI,
    Omega_DM, rho_crit_GeV4,
)

# ---------------------------------------------------------------------------
# Paths + identity
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]                        # (local) project root (parent of computations/)
GATE_ID = "S96-LEGGETT-GAMMA-GRAV"                                # (local)
SCHEME = "QA-9-graviton-vertex"                                   # (local) plan-pinned
CONVENTION = "GAMMA-GRAV-OVER-H0-DIMENSIONLESS-MARGIN"           # (local) plan-pinned
L_MAX = "N/A"                                                    # (local) closed-form rate; no spectral truncation
SCHEMA_VERSION = "S84+"                                           # (local)

# Option A supersedes pin (gate-verdicts.md): the FULL 64-char audit_sha256 of the prior emission
# whose pair-channel value (1.11e-68) used an unjustified xi_eff*(eps/omega_L1) ansatz. The original
# line stays on disk byte-for-byte; this run APPENDS a corrective line with supersedes=<this>.
SUPERSEDES_AUDIT_SHA = "37c46ca0b2ead4afd2f681971dc5d824006f17c52430fc77bb9c9493277fcd9c"  # (local)

SCRIPT_PATH = Path(__file__).resolve()                                                         # (local)
CANONICAL_CONSTANTS = SHARED / "canonical_constants.py"                                         # (local)
S67_NPZ = ROOT / "computations" / "session-67" / "s67_leggett_grav_decay.npz"                  # (local) CC2 anchor + substrate frac_d2a2/phi_zp
S73A_NPZ = ROOT / "computations" / "session-73" / "s73a_leggett_grav_decay.npz"                # (local) CC2 anchor
VERDICT_FILE = ROOT / "computations" / "session-96" / "s96_gate_verdicts.txt"                  # (local) canonical path
NPZ_OUT = ROOT / "computations" / "session-96" / "s96_w3_2_leggett_gamma_grav.npz"             # (local)
PNG_OUT = ROOT / "computations" / "session-96" / "s96_w3_2_leggett_gamma_grav.png"             # (local)

# Pre-registered epsilon-band (S56 Leggett-Josephson gap ratio) -- 11-point linspace
EPS_MIN = 0.005   # (local) plan-pinned band lower edge
EPS_MAX = 0.011   # (local) plan-pinned band upper edge
N_EPS = 11        # (local) plan-pinned 11-point linspace

# Pre-registered thresholds (inequality-class) on the PHYSICAL surviving margin Gamma_pair/H_0
PASS_RATIO = 1.0      # (local) PASS iff ratio < 1 (the decay-vs-Hubble crossover)
INFO_RATIO = 10.0     # (local) INFO iff 1 <= ratio < 10; FAIL iff ratio >= 10
MARGIN_OOM_FLOOR = 1.0  # (local) magnitude PASS requires margin_OOM > 1 (decisively safe)

# CC2 cross-check anchor (S67/S73a archive PAIR-channel margin; ANCHOR not pin)
ARCHIVE_MARGIN_ANCHOR = 8.85e-66   # (local) S95 LEGGETT-GRAV-DECAY-CONDITIONAL cited ratio (cross-check only)
CC2_OOM_TOL = 1.5                  # (local) accept CC2 agreement if |OOM(ratio) - OOM(anchor)| <= 1.5 OOM


# ---------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema; matches s95 reference implementation)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(ROOT))  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema.)"""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v, supersedes=None):
    """Single canonical dual-SHA verdict line + dual-SHA companion row + schema-v2
    3-tuple companion row ([SIGN] directional pre-reg). Append-only single open('a').
    `supersedes` (full 64-char old audit_sha256) tags a corrective re-emission per
    gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence":
    the ORIGINAL line stays on disk byte-for-byte; this corrective line APPENDS with the tag."""
    sup_value = f" supersedes={supersedes}" if supersedes else ""   # (local) tag in value= field
    sup_companion = (f" SUPERSEDES audit_sha256={supersedes} (prior pair-channel value 1.11e-68 used an "
                     f"unjustified xi_eff*(eps/omega_L1) ansatz; corrected to the epsilon-INDEPENDENT "
                     f"canonical GL pair prescription xi_eff=frac_d2a2*phi_zp^2; composite stays PASS)"
                     if supersedes else "")   # (local)
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}{sup_value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] Leggett-channel GGE DM gravitational decay margin "
        f"Gamma_grav/H_0 (PHYSICAL surviving pair channel 2L->2g) via Eq.QA-9 family; "
        f"single-Leggett L->g+g FORBIDDEN EXACTLY by Z_2 parity (=0) + graviton-gap kinematic protection; "
        f"D1 dissonance discharged (re-pinned from canonical, NOT the cited S67/S73a archive ~8.85e-66); "
        f"naive QA-9 single channel ~10^39 H_0 is the open-problem flag but Z_2-killed to 0; "
        f"CLASS=FULL (closed-form QA-9/pair rate from canonical scalar pins + S67 substrate frac_d2a2/phi_zp, NO SCHEMATIC helper); "
        f"regulator_pin=N/A (tree graviton-vertex decay rate, not a Seeley-DeWitt moment){sup_companion}\n"
    )
    tuple_row = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] §W3-2 Step-4 directional pre-reg: "
        f"SIGN=ratio<1 across whole epsilon-band (predicted relic survival, physical pair channel); "
        f"MAG=ratio vs 1/10; "
        f"REGIME=dimensional bookkeeping closes ((omega_L/M_KK)^4 dimensionless) + canonical SHA pins match "
        f"+ closed-form rate (no truncation regime) + CC2 archive-anchor cross-check within OOM band)\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)


# ---------------------------------------------------------------------------
# Eq. QA-9 (channel a, naive single-Leggett) + pair channel (channel b, physical)
# ---------------------------------------------------------------------------
def gamma_qa9_single_GeV(eps, omega_L_GeV, Delta_BCS_GeV, M_Pl_GeV, soft_mode_factor):
    """Eq. QA-9 NAIVE single-Leggett L->g+g decay rate in GeV (channel a; FORBIDDEN by Z_2).

    Gamma_KK = eps^2 * omega_L^3 * Delta^2 / (64*pi*M_Pl^4) * (omega_L/M_KK)^4
    (session-66-mack-qa-workshop.md:354; S67 s67_leggett_grav_decay.py:550-553).
    Numerator omega^3*Delta^2 = GeV^5, /M_Pl^4 = GeV^{-4}, net GeV^1; soft_mode_factor dimensionless.
    This is the OPEN-PROBLEM rate (~10^29-10^39 H_0); it is Z_2-killed to exactly 0 physically.
    """
    return (eps ** 2) * (omega_L_GeV ** 3) * (Delta_BCS_GeV ** 2) \
        / (64.0 * PI * (M_Pl_GeV ** 4)) * soft_mode_factor  # (local)


def gamma_pair_GeV(xi_eff, m_L_GeV, M_Pl_GeV, Omega_DM_v, rho_crit_v):
    """Physical surviving pair-annihilation rate 2L->2g in GeV (channel b; ALLOWED, Delta n_L=-2 even).

    <sigma v> = xi_eff^2 * m_L^2 / (960*pi*M_Pl^4)   [S67 §6; Kolb-Turner conformal coupling]
    n_L = Omega_DM * rho_crit / m_L ;  Gamma_pair = n_L * <sigma v>.
    GeV^{-2} * GeV^3 = GeV^1.
    """
    sigma_v = (xi_eff ** 2) * (m_L_GeV ** 2) / (960.0 * PI * (M_Pl_GeV ** 4))  # (local) GeV^-2
    n_L = Omega_DM_v * rho_crit_v / m_L_GeV  # (local) GeV^3
    return n_L * sigma_v, sigma_v, n_L  # (local) GeV, GeV^-2, GeV^3


def load_substrate_pair_params(npz_path: Path):
    """Load substrate xi_eff inputs from the S67 pinned npz (frac_d2a2, phi_1q).
    frac_d2a2 = (d^2 a_2/d phi^2)/a_2 (Z_2 second-order coupling fraction); phi_1q = single-quantum
    zero-point phase amplitude. xi_eff = frac_d2a2 * phi_zp^2. Returns (frac_d2a2, phi_1q_S52, phi_1q_S59)."""
    d = np.load(npz_path, allow_pickle=True)  # (local)
    frac = float(np.asarray(d["frac_d2a2"]).ravel()[0])  # (local)
    phi_s52 = float(np.asarray(d["phi_1q_S52"]).ravel()[0])  # (local)
    phi_s59 = float(np.asarray(d["phi_1q_S59"]).ravel()[0])  # (local)
    return frac, phi_s52, phi_s59


def load_archive_pair_ratio(npz_path: Path):
    """Extract the archive Gamma_pair_over_H0 for the CC2 cross-check (ANCHOR, not pin)."""
    if not npz_path.exists():
        return None, f"{npz_path.name}: MISSING"
    try:
        d = np.load(npz_path, allow_pickle=True)  # (local)
    except Exception as e:  # noqa: BLE001
        return None, f"{npz_path.name}: load-error {type(e).__name__}"
    keys = list(d.keys())  # (local)
    for k in ("Gamma_physical_over_H0", "Gamma_pair_over_H0_S59", "Gamma_pair_over_H0_GL",
              "Gamma_pair_over_H0_S52", "Gamma_pair_over_H0_Vbare"):
        if k in keys:
            try:
                v = float(np.asarray(d[k]).ravel()[0])  # (local)
                if v > 0:
                    return v, f"{npz_path.name}:{k}={v:.4e}"
            except Exception:  # noqa: BLE001
                pass
    return None, f"{npz_path.name}: keys={keys[:6]} (no pair-ratio key; const anchor used)"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"=== {GATE_ID} ===")
    print("=" * 78)

    # ---- (1) input pins ----
    input_files = {
        "script": SCRIPT_PATH,
        "canonical": CANONICAL_CONSTANTS,
        "s67_leggett_grav_decay": S67_NPZ,
        "s73a_leggett_grav_decay": S73A_NPZ,
    }
    print("\nINPUT SHA-256 PINS:")
    pins = log_input_pins(input_files)

    print("\n  canonical constants imported (Step-1 definitions):")
    print(f"    omega_L1      = {omega_L1}  (Leggett-1 frequency, M_KK)")
    print(f"    Delta_BCS     = {Delta_BCS}  (R-protected BCS gap, M_KK; BCS-GAP-CANONICAL-70)")
    print(f"    M_KK_gravity  = {M_KK_gravity:.6e}  GeV (CONST-FREEZE-42)")
    print(f"    M_Pl_reduced  = {M_Pl_reduced:.6e}  GeV (CODATA 2018)")
    print(f"    Omega_DM      = {Omega_DM}   rho_crit_GeV4 = {rho_crit_GeV4:.3e} GeV^4")
    print(f"    H_0_inv_s     = {H_0_inv_s:.6e}  s^-1     H_0_GeV = {H_0_GeV:.6e} GeV")
    print(f"    hbar_GeV_s    = {hbar_GeV_s:.6e}  GeV*s")

    # ---- (2) Step-2 dimensional bookkeeping: M_KK units -> GeV ----
    print("\n" + "-" * 78)
    print("Step 2 -- dimensional bookkeeping (M_KK units -> GeV)")
    print("-" * 78)
    omega_L_GeV = omega_L1 * M_KK_gravity        # (local) 0.138 M_KK -> GeV
    m_L_GeV = omega_L_GeV                         # (local) Leggett mass in GeV
    Delta_BCS_GeV = Delta_BCS * M_KK_gravity     # (local) BCS gap M_KK -> GeV
    M_Pl_GeV = M_Pl_reduced                      # (local) already GeV
    soft_mode_ratio = omega_L1                   # (local) = omega_L/M_KK (both M_KK; dimensionless)
    soft_mode_factor = soft_mode_ratio ** 4      # (local) (omega_L/M_KK)^4 = (0.138)^4
    mkk_mpl_ratio4 = (M_KK_gravity / M_Pl_GeV) ** 4   # (local) (M_KK/M_Pl)^4 graviton-coupling ratio
    print(f"  omega_L_GeV   = omega_L1 * M_KK_gravity = {omega_L_GeV:.6e} GeV  (= m_L)")
    print(f"  Delta_BCS_GeV = Delta_BCS * M_KK_gravity = {Delta_BCS_GeV:.6e} GeV")
    print(f"  M_Pl_GeV      = {M_Pl_GeV:.6e} GeV")
    print(f"  CC1: (omega_L/M_KK)^4 = (0.138)^4 = {soft_mode_factor:.6e}  (DIMENSIONLESS)")
    print(f"       [plan-stated value 3.6266e-4; match = {abs(soft_mode_factor - 3.6266e-4) < 1e-7}]")
    print(f"  (M_KK/M_Pl)^4 graviton-coupling ratio = {mkk_mpl_ratio4:.6e}")

    # substrate pair-channel coupling (from S67 pinned npz: frac_d2a2, phi_zp)
    frac_d2a2, phi_s52, phi_s59 = load_substrate_pair_params(S67_NPZ)  # (local)
    xi_eff = frac_d2a2 * (phi_s52 ** 2)   # (local) effective conformal coupling (GL/S52 single-quantum amplitude)
    print(f"  substrate (S67 npz): frac_d2a2={frac_d2a2:.6f}  phi_zp(S52)={phi_s52:.6f}  "
          f"=> xi_eff = frac_d2a2*phi_zp^2 = {xi_eff:.6f}")

    # ---- (3a) CHANNEL (a): Eq. QA-9 NAIVE single-Leggett vertex over the epsilon-band ----
    print("\n" + "=" * 78)
    print("CHANNEL (a) -- Eq. QA-9 NAIVE single-Leggett L->g+g (OPEN-PROBLEM rate; Z_2-FORBIDDEN to 0)")
    print("=" * 78)
    eps_band = np.linspace(EPS_MIN, EPS_MAX, N_EPS)   # (local) S56 gap-ratio band
    gamma_qa9_GeV_band = gamma_qa9_single_GeV(eps_band, omega_L_GeV, Delta_BCS_GeV, M_Pl_GeV, soft_mode_factor)  # (local)
    gamma_qa9_inv_s_band = gamma_qa9_GeV_band / hbar_GeV_s     # (local)
    ratio_qa9_band = gamma_qa9_inv_s_band / H_0_inv_s          # (local) naive single-channel ratio (~10^39)
    print(f"  {'epsilon':>10} {'Gamma_QA9_GeV':>15} {'ratio_QA9/H_0':>15}")
    for e, gG, r in zip(eps_band, gamma_qa9_GeV_band, ratio_qa9_band):
        print(f"  {e:>10.6f} {gG:>15.4e} {r:>15.4e}")
    print(f"  => naive QA-9 single-Leggett ratio mid-band = {float(ratio_qa9_band[N_EPS//2]):.4e} (>> 1)")
    print("     This reproduces S66 Eq. QA-10 'cosmologically instant' OPEN-PROBLEM flag.")
    print("     PHYSICALLY this channel = 0 EXACTLY: Z_2 parity (Delta n_L=-1 ODD, S67/S73a PROVEN)")
    print("     + graviton-gap kinematic protection (2*m_graviton ~ 2*M_KK >> omega_L=0.138 M_KK).")
    gamma_single_physical = 0.0   # (local) Z_2-forbidden EXACTLY
    print(f"  Gamma_single (physical, Z_2-forbidden) = {gamma_single_physical}  (EXACTLY zero)")

    # ---- (3b) CHANNEL (b): PHYSICAL surviving pair annihilation 2L->2g ----
    print("\n" + "=" * 78)
    print("CHANNEL (b) -- PHYSICAL surviving pair annihilation 2L->2g (ALLOWED, Delta n_L=-2 EVEN)")
    print("=" * 78)
    # CANONICAL pair-channel prescription (S67/S73a, the established physics): xi_eff = frac_d2a2*phi_zp^2
    # with NO epsilon factor. epsilon (eps_canonical=0.003743) enters ONLY the FORBIDDEN single-Leggett
    # channel (a) via Gamma_eps = eps^2*...; it does NOT appear in the pair channel
    # (S67 s67_leggett_grav_decay.py:448 xi_eff=frac_d2a2*phi_zp**2; :456 sigma_v=xi_eff^2*m_L^2/(960pi M_Pl^4);
    # the conformal-coupling M_Pl^2 ratio cancels, S67:439-440 => no epsilon). The PHYSICAL pair margin is
    # therefore a SINGLE canonical VALUE, epsilon-INDEPENDENT. The epsilon-band-robustness axis lives on
    # channel (a) (the forbidden single channel), reported above. We broadcast the canonical value across
    # the band to make the epsilon-independence explicit and keep the array shapes for plotting.
    # [RECONCILIATION: a prior emission (audit_sha256=37c46ca0..277fcd9c, value=1.11e-68) applied an
    #  unjustified xi_eff*(eps/omega_L1) ansatz to the pair channel, pushing the headline ~2.5 OOM below
    #  its own CC2 archive re-pin. That ansatz had NO first-principles basis (S67 pair channel is epsilon-
    #  independent); the canonical value 3.31e-66 below reproduces the S67 archive Gamma_pair_over_H0_S52
    #  EXACTLY and equals the CC2 re-pin. See gate-verdicts.md §"Option A" supersedes protocol.]
    #
    # phi_zp pin (GL/S52 vs V_bare/S59): phi_zp = 1/sqrt(2*omega_L*I_L) (S67:392-393). The plan §W3-2 pins
    # omega_L = omega_L1 = 0.138 M_KK (the GL-Josephson / canonical_constants value), so the CANONICAL phi_zp
    # is the GL/S52 value (=> xi_eff = frac_d2a2*phi_zp^2 = 2.131). The V_bare/S59 value (omega_L=0.04923 =>
    # xi_eff=5.973) is the cross-check SIBLING, not the canonical pin.
    gamma_pair_canon_GeV, sigma_v_canon, n_L_canon = gamma_pair_GeV(xi_eff, m_L_GeV, M_Pl_GeV, Omega_DM, rho_crit_GeV4)  # (local) CANONICAL GL pair rate
    ratio_pair_canon = (gamma_pair_canon_GeV / hbar_GeV_s) / H_0_inv_s  # (local) canonical pair margin (= headline)
    # broadcast the canonical (epsilon-independent) pair value across the epsilon-band:
    gamma_pair_GeV_band = np.full(N_EPS, gamma_pair_canon_GeV)   # (local) epsilon-INDEPENDENT physical pair margin
    sigma_v_band = np.full(N_EPS, sigma_v_canon)                 # (local)
    n_L_band = np.full(N_EPS, n_L_canon)                         # (local)
    gamma_pair_inv_s_band = gamma_pair_GeV_band / hbar_GeV_s    # (local)
    ratio_pair_band = gamma_pair_inv_s_band / H_0_inv_s         # (local) PHYSICAL margin (s^-1 convention)
    ratio_pair_band_GeV = gamma_pair_GeV_band / H_0_GeV         # (local) GeV-convention cross-check
    margin_OOM_band = np.log10(H_0_inv_s / gamma_pair_inv_s_band)   # (local) margin_OOM = log10(H_0/Gamma)

    # V_bare/S59 cross-check sibling (non-canonical omega_L=0.04923; brackets the anchor with GL):
    xi_eff_Vbare = frac_d2a2 * (phi_s59 ** 2)   # (local) cross-check sibling coupling
    gamma_pair_Vbare_GeV, _, _ = gamma_pair_GeV(xi_eff_Vbare, m_L_GeV, M_Pl_GeV, Omega_DM, rho_crit_GeV4)  # (local)
    ratio_pair_Vbare = (gamma_pair_Vbare_GeV / hbar_GeV_s) / H_0_inv_s  # (local)

    print(f"  m_L = {m_L_GeV:.4e} GeV   <sigma v>(canon GL) = {sigma_v_canon:.4e} GeV^-2   "
          f"n_L(canon) = {n_L_canon:.4e} GeV^3")
    print(f"  CANONICAL xi_eff(GL) = frac_d2a2*phi_zp(GL)^2 = {xi_eff:.6f}  (NO epsilon factor)")
    print(f"  Gamma_pair(canon GL) = {gamma_pair_canon_GeV:.4e} GeV   "
          f"Gamma_pair/H_0(canon GL) = {ratio_pair_canon:.4e}  [= HEADLINE; epsilon-INDEPENDENT]")
    print(f"  cross-check sibling Vbare: xi_eff(Vbare)={xi_eff_Vbare:.4f}  Gamma_pair/H_0(Vbare)={ratio_pair_Vbare:.4e}")
    print(f"\n  {'epsilon':>10} {'Gamma_pair_GeV':>15} {'ratio_pair/H_0':>15} {'ratio(GeV)':>15} {'margin_OOM':>11}  (pair = epsilon-INDEPENDENT)")
    for e, gG, r, rG, m in zip(eps_band, gamma_pair_GeV_band, ratio_pair_band, ratio_pair_band_GeV, margin_OOM_band):
        print(f"  {e:>10.6f} {gG:>15.4e} {r:>15.4e} {rG:>15.4e} {m:>11.2f}")

    # ---- headline: the gate margin IS the physical surviving rate (channel b) ----
    Gamma_grav_GeV_band = gamma_pair_GeV_band     # (local) physical surviving rate = pair channel
    Gamma_grav_inv_s_band = gamma_pair_inv_s_band # (local)
    ratio_band = ratio_pair_band                  # (local) THE gate margin
    i_mid = N_EPS // 2                             # (local)
    eps_mid = float(eps_band[i_mid])              # (local)
    ratio_mid = float(ratio_band[i_mid])         # (local) headline Gamma_grav/H_0
    margin_OOM_mid = float(margin_OOM_band[i_mid])   # (local) headline margin_OOM
    ratio_max = float(np.max(ratio_band))        # (local) worst-case (largest) ratio in band
    ratio_min = float(np.min(ratio_band))        # (local)
    margin_OOM_min = float(np.min(margin_OOM_band))  # (local) smallest margin in band

    conv_reldev = float(np.max(np.abs(ratio_pair_band - ratio_pair_band_GeV) / ratio_pair_band))  # (local)
    conv_consistent = bool(conv_reldev < 1e-3)   # (local) two unit conventions agree (H_0_GeV/H_0_inv_s rounding ~3e-4)

    print(f"\n  GATE MARGIN (physical surviving Gamma_grav/H_0) mid-band = {ratio_mid:.6e}   margin_OOM = {margin_OOM_mid:.2f}")
    print(f"  ratio band: [{ratio_min:.4e}, {ratio_max:.4e}]   margin_OOM min = {margin_OOM_min:.2f}")
    print(f"  convention cross-check (s^-1 vs GeV ratio) max-reldev = {conv_reldev:.3e}  consistent={conv_consistent}")

    # ---- (4) CC2: S67/S73a archive pair-channel cross-check (ANCHOR, not pin) ----
    print("\n" + "-" * 78)
    print("CC2 -- S67/S73a archive PAIR-channel margin cross-check (ANCHOR ~8.85e-66, NOT the pin)")
    print("-" * 78)
    r67, note67 = load_archive_pair_ratio(S67_NPZ)      # (local)
    r73a, note73a = load_archive_pair_ratio(S73A_NPZ)   # (local)
    print(f"  S67  archive pair ratio: {note67}")
    print(f"  S73a archive pair ratio: {note73a}")
    print(f"  S95 cited archive ratio anchor = {ARCHIVE_MARGIN_ANCHOR:.4e}")
    # compare the canonical (S67 xi_eff) fresh pair ratio to the archive pair ratio + the cited anchor
    oom_canon = float(np.log10(ratio_pair_canon))         # (local)
    oom_anchor = float(np.log10(ARCHIVE_MARGIN_ANCHOR))   # (local)
    cc2_oom_gap = abs(oom_canon - oom_anchor)             # (local) OOM distance fresh-vs-anchor
    cc2_consistent = bool(cc2_oom_gap <= CC2_OOM_TOL)     # (local)
    print(f"  fresh canonical pair ratio OOM = {oom_canon:.2f}   anchor OOM = {oom_anchor:.2f}   "
          f"|gap| = {cc2_oom_gap:.2f} OOM")
    print(f"  CC2 consistent (|gap| <= {CC2_OOM_TOL:.1f} OOM)? {cc2_consistent}")
    if r73a is not None:
        cc2_archive_reldev = abs(np.log10(ratio_pair_canon) - np.log10(r73a))  # (local)
        print(f"  fresh-vs-S73a-archive pair ratio |OOM gap| = {cc2_archive_reldev:.3f}")
    # headline-vs-CC2 internal consistency: SAME canonical GL prescription => they are IDENTICAL by construction
    headline_eq_cc2 = bool(abs(ratio_mid - ratio_pair_canon) / ratio_pair_canon < 1e-12)  # (local)
    print(f"  HEADLINE (mid-band) = {ratio_mid:.6e}  vs  CC2 canonical re-pin = {ratio_pair_canon:.6e}  "
          f"=> IDENTICAL (same canonical GL prescription)? {headline_eq_cc2}")
    if r67 is not None:
        cc2_archive_GL_match = bool(abs(np.log10(ratio_pair_canon) - np.log10(r67)) < 1e-6)  # (local)
        print(f"  fresh canonical GL ratio reproduces S67 archive Gamma_pair_over_H0_S52 EXACTLY (|OOM gap|<1e-6)? "
              f"{cc2_archive_GL_match}")
    print("  NOTE: this gate RE-DERIVES the margin from canonical pins; the archive figure is a"
          " cross-check anchor only (resolving D1: cited -> re-pinned). Headline == CC2 re-pin by"
          " construction (same canonical GL prescription); both 0.43 OOM from the cited anchor.")

    # ---- (5) VERDICT (composite collapse rule; gate-verdicts.md) ----
    print("\n" + "=" * 78)
    print("VERDICT (inequality ratio<1 on the PHYSICAL surviving margin; composite collapse)")
    print("=" * 78)
    band_all_below_1 = bool(ratio_max < PASS_RATIO)    # (local) whole-band survival
    band_any_ge_info = bool(ratio_max >= INFO_RATIO)   # (local) any FAIL-level ratio in band

    # sign_verdict: predicted direction is ratio < 1 (relic survives) across the whole band
    sign_v = "PASS" if band_all_below_1 else "FAIL"    # (local)

    # magnitude_verdict: PASS iff ratio<1 with margin_OOM>1 everywhere; INFO iff 1<=ratio<10; FAIL iff >=10
    if band_all_below_1 and (margin_OOM_min > MARGIN_OOM_FLOOR):
        mag_v = "PASS"   # (local)
    elif band_any_ge_info:
        mag_v = "FAIL"   # (local) some ratio reached the >=10 ceiling
    else:
        mag_v = "INFO"   # (local) 1 <= ratio < 10 somewhere, or margin_OOM <= 1

    # regime_verdict: VALID iff dimensional bookkeeping closes + convention-consistent
    #   + closed-form (no truncation regime) + CC2 anchor cross-check within OOM band
    cc1_ok = bool(abs(soft_mode_factor - 3.6266e-4) < 1e-7)   # (local) (0.138)^4 dimensionless check
    regime_ok = bool(cc1_ok and conv_consistent and cc2_consistent)  # (local)
    regime_v = "VALID" if regime_ok else ("MARGINAL" if (cc1_ok and conv_consistent) else "BREAKDOWN")  # (local)

    # composite collapse rule (PRE-REGISTERED; gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"   # (local)
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

    print(f"  whole-band ratio < 1?            {band_all_below_1}  (ratio_max = {ratio_max:.4e})")
    print(f"  margin_OOM min across band       {margin_OOM_min:.2f}  (PASS needs > {MARGIN_OOM_FLOOR:.0f})")
    print(f"  sign_verdict                     = {sign_v}   (predicted ratio<1 survival)")
    print(f"  magnitude_verdict                = {mag_v}")
    print(f"  regime_verdict                   = {regime_v}   (CC1={cc1_ok}, conv={conv_consistent}, CC2={cc2_consistent})")
    print(f"  COMPOSITE                        = {composite}")

    # ---- physics statement ----
    print("\n" + "-" * 78)
    if composite == "PASS":
        print(f"  Gamma_grav (physical surviving pair channel) < H_0 by {margin_OOM_mid:.1f} OOM across the whole")
        print("  epsilon-band (epsilon-INDEPENDENT canonical GL pair prescription), RE-PINNED from")
        print("  canonical Eq. QA-9-family parameters (NOT the cited")
        print("  S67/S73a archive figure). The naive single-Leggett QA-9 vertex (~10^39 H_0, the")
        print("  S66 'cosmologically instant' OPEN-PROBLEM flag) is FORBIDDEN EXACTLY by Z_2 parity")
        print("  (Delta n_L=-1 odd) + graviton-gap kinematic protection -- the STRUCTURAL REASON the")
        print("  surviving rate is enormous. The Leggett-channel GGE DM relic does NOT gravitationally")
        print("  decay within a Hubble time; Omega_DM h^2=0.120 STANDS. D1 RESOLVED: PASS-confirms")
        print("  nazarewicz's reading WHILE supplying the explicit margin number landau/mack/hawking")
        print("  flagged as uncomputed, AND reconciling the 'PASS gate' vs 'UNCOMPUTED CRITICAL' split.")
    elif composite == "INFO":
        print("  Gamma_grav/H_0 is marginal (1 <= ratio < 10 somewhere in the band): re-flag")
        print("  LEGGETT-GRAV-DECAY-67 as MARGINAL-PENDING-REFINEMENT.")
    else:
        print("  Gamma_grav >= H_0 somewhere in the band: the Leggett-channel DM corridor collapses")
        print("  (a major constraint-map update -- a different DM relic would be required).")

    # ---- dual-prior posterior re-allocation (D1) ----
    if composite == "PASS":
        posterior = "Track A (nazarewicz PASS-confirm) -> 0.97; D1 RESOLVED: PASS-confirmed WITH explicit margin"  # (local)
    elif composite == "FAIL":
        posterior = "Track B (CRITICAL-open) -> 0.9; D1 resolved the OTHER way: DM corridor collapses"  # (local)
    else:
        posterior = "INFO -> re-flag; margin genuinely marginal (neither track fully favored)"  # (local)
    print(f"\n  dual-prior posterior re-allocation: {posterior}")

    # ---- (6) data file (full float64 round-trip) ----
    value_str = (  # (local) compact, audit-greppable; ratio to 3 sig figs + margin_OOM to 1 decimal
        f"composite={composite};Gamma_grav_over_H0={ratio_mid:.3e};margin_OOM={margin_OOM_mid:.1f};"
        f"channel=pair_2L_to_2g_physical_surviving_epsilon_INDEPENDENT;single_L_to_gg=0_EXACT_Z2_forbidden;"
        f"eps_mid={eps_mid:.4f};ratio_band_min={ratio_min:.3e};ratio_band_max={ratio_max:.3e};"
        f"margin_OOM_band_min={margin_OOM_min:.1f};whole_band_below_1={band_all_below_1};"
        f"Gamma_grav_GeV_mid={float(Gamma_grav_GeV_band[i_mid]):.3e};Gamma_grav_inv_s_mid={float(Gamma_grav_inv_s_band[i_mid]):.3e};"
        f"ratio_pair_canon_GL={ratio_pair_canon:.3e};ratio_pair_Vbare={ratio_pair_Vbare:.3e};headline_eq_CC2={headline_eq_cc2};"
        f"naive_QA9_single_ratio_mid={float(ratio_qa9_band[i_mid]):.3e}_FORBIDDEN_Z2;"
        f"soft_mode_factor=(0.138)^4={soft_mode_factor:.4e};MKK_MPl4={mkk_mpl_ratio4:.3e};"
        f"omega_L_GeV={omega_L_GeV:.4e};Delta_BCS_GeV={Delta_BCS_GeV:.4e};xi_eff_GL={xi_eff:.4f};xi_eff_Vbare={xi_eff_Vbare:.4f};frac_d2a2={frac_d2a2:.4f};"
        f"CC1_dimless_ok={cc1_ok};conv_consistent={conv_consistent};conv_reldev={conv_reldev:.2e};"
        f"CC2_anchor={ARCHIVE_MARGIN_ANCHOR:.3e};CC2_oom_gap={cc2_oom_gap:.2f};CC2_consistent={cc2_consistent};"
        f"sign_verdict={sign_v};magnitude_verdict={mag_v};regime_verdict={regime_v};"
        f"PASS_ratio={PASS_RATIO};INFO_ratio={INFO_RATIO};CLASS=FULL;regulator_pin=N/A_QA9_tree_graviton_vertex;"
        f"D1_resolution=re-pinned_from_canonical_NOT_archive_citation;graviton_gap_kinematic_protection=structural_reason"
    )

    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        # epsilon-band arrays (full float64) -- physical surviving (pair) channel
        eps_band=eps_band,
        Gamma_grav_GeV_band=Gamma_grav_GeV_band, Gamma_grav_inv_s_band=Gamma_grav_inv_s_band,
        ratio_band=ratio_band, ratio_pair_band_GeV=ratio_pair_band_GeV, margin_OOM_band=margin_OOM_band,
        sigma_v_band=sigma_v_band, n_L_band=n_L_band,
        # naive QA-9 single channel (diagnostic; Z_2-forbidden)
        gamma_qa9_GeV_band=gamma_qa9_GeV_band, ratio_qa9_band=ratio_qa9_band,
        gamma_single_physical=gamma_single_physical,
        # headline scalars (full float64)
        ratio_mid=ratio_mid, margin_OOM_mid=margin_OOM_mid, eps_mid=eps_mid,
        ratio_min=ratio_min, ratio_max=ratio_max, margin_OOM_min=margin_OOM_min,
        Gamma_grav_GeV_mid=float(Gamma_grav_GeV_band[i_mid]), Gamma_grav_inv_s_mid=float(Gamma_grav_inv_s_band[i_mid]),
        ratio_pair_canon=ratio_pair_canon, gamma_pair_canon_GeV=gamma_pair_canon_GeV,
        sigma_v_canon=sigma_v_canon, n_L_canon=n_L_canon,
        ratio_pair_Vbare=ratio_pair_Vbare, xi_eff_Vbare=xi_eff_Vbare, headline_eq_cc2=headline_eq_cc2,
        supersedes_audit_sha=SUPERSEDES_AUDIT_SHA,
        # dimensional bookkeeping
        omega_L_GeV=omega_L_GeV, m_L_GeV=m_L_GeV, Delta_BCS_GeV=Delta_BCS_GeV, M_Pl_GeV=M_Pl_GeV,
        soft_mode_factor=soft_mode_factor, mkk_mpl_ratio4=mkk_mpl_ratio4,
        xi_eff=xi_eff, frac_d2a2=frac_d2a2, phi_zp_S52=phi_s52, phi_zp_S59=phi_s59,
        # canonical pins echoed
        omega_L1=omega_L1, Delta_BCS=Delta_BCS, M_KK_gravity=M_KK_gravity,
        M_Pl_reduced=M_Pl_reduced, H_0_inv_s=H_0_inv_s, H_0_GeV=H_0_GeV, hbar_GeV_s=hbar_GeV_s,
        Omega_DM=Omega_DM, rho_crit_GeV4=rho_crit_GeV4,
        # cross-checks
        cc1_dimless_ok=cc1_ok, conv_consistent=conv_consistent, conv_reldev=conv_reldev,
        archive_margin_anchor=ARCHIVE_MARGIN_ANCHOR, cc2_oom_gap=cc2_oom_gap, cc2_consistent=cc2_consistent,
        archive_r67=(r67 if r67 is not None else np.nan), archive_r73a=(r73a if r73a is not None else np.nan),
        # verdict
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=composite,
        PASS_ratio=PASS_RATIO, INFO_ratio=INFO_RATIO, margin_OOM_floor=MARGIN_OOM_FLOOR,
        EPS_MIN=EPS_MIN, EPS_MAX=EPS_MAX, N_EPS=N_EPS,
        posterior=posterior,
        D1_resolution="re-pinned_from_canonical_Eq_QA9_family_NOT_S67_S73a_archive_citation",
    )
    print(f"\n  npz  -> {NPZ_OUT.relative_to(ROOT)}")

    # ---- (7) plot ----
    fig, axes = plt.subplots(1, 2, figsize=(13.0, 5.2))

    # Panel 1: physical surviving Gamma_grav/H_0 across the epsilon-band, with the two channels.
    ax = axes[0]
    ax.semilogy(eps_band, ratio_band, "o-", color="tab:blue", lw=2.0, ms=6,
                label=r"$\Gamma_{grav}/H_0$ physical (pair $2L\to2g$)")
    ax.semilogy(eps_band, ratio_qa9_band, "s--", color="tab:gray", lw=1.4, ms=4, alpha=0.7,
                label=r"naive QA-9 single $L\to gg$ ($Z_2$-FORBIDDEN $=0$)")
    ax.axhline(1.0, color="tab:red", lw=1.8, ls="-",
               label=r"$\Gamma_{grav}=H_0$ crossover (PASS boundary)")
    ax.axhline(ARCHIVE_MARGIN_ANCHOR, color="tab:green", lw=1.4, ls="--",
               label=fr"S67/S73a archive anchor $\sim${ARCHIVE_MARGIN_ANCHOR:.2e}")
    ax.axhspan(1e-72, 1.0, color="green", alpha=0.07, zorder=0, label="PASS region (ratio < 1)")
    ax.set_xlabel(r"$\epsilon = \Delta_{Leggett}/\Delta_{Josephson}$  (S56 band)")
    ax.set_ylabel(r"$\Gamma_{grav}/H_0$  (dimensionless margin)")
    ax.set_title(r"Leggett-DM gravitational decay margin $\Gamma_{grav}/H_0$"
                 "\n" fr"physical (pair) mid-band $={ratio_mid:.2e}$  (margin $\sim${margin_OOM_mid:.0f} OOM below $H_0$)",
                 fontsize=10)
    ax.legend(loc="center right", fontsize=7.0)
    ax.grid(ls=":", alpha=0.4)

    # Panel 2: the two channels + the Z_2/graviton-gap protection (structural reason).
    ax = axes[1]
    chan_labels = ["naive QA-9\nsingle L->gg\n(forbidden)",
                   "physical\npair 2L->2g\n(SURVIVES)"]  # (local)
    chan_vals = [float(ratio_qa9_band[i_mid]), ratio_mid]  # (local)
    colors = ["tab:gray", "tab:blue"]  # (local)
    xpos = np.arange(len(chan_vals))  # (local)
    ax.bar(xpos, chan_vals, color=colors, alpha=0.85, edgecolor="k", zorder=3, log=True)
    for xi, vi in zip(xpos, chan_vals):
        ax.annotate(f"{vi:.2e}", (xi, vi), textcoords="offset points",
                    xytext=(0, 6), ha="center", fontsize=8.6)
    ax.axhline(1.0, color="tab:red", lw=1.6, ls="-", zorder=2, label=r"$\Gamma=H_0$ (PASS boundary)")
    ax.set_xticks(xpos)
    ax.set_xticklabels(chan_labels, fontsize=8.4)
    ax.set_ylabel(r"$\Gamma/H_0$  (log scale)")
    ax.set_title(f"{GATE_ID}\nnaive single channel $Z_2$-killed; pair channel "
                 fr"$\sim10^{{{oom_canon:.0f}}}\,H_0$  (composite: {composite})",
                 fontsize=9.6)
    ax.legend(loc="upper right", fontsize=7.6)
    ax.grid(axis="y", ls=":", alpha=0.4)

    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"  png  -> {PNG_OUT.relative_to(ROOT)}")

    # ---- (8) dual-SHA + verdict line ----
    print("\n" + "-" * 78)
    print("Dual-SHA closure + verdict-line emission")
    print("-" * 78)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
                   supersedes=SUPERSEDES_AUDIT_SHA)
    print(f"\n  verdict line appended (supersedes {SUPERSEDES_AUDIT_SHA[:16]}...) -> {VERDICT_FILE.relative_to(ROOT)}")

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md §"During computation")
    print(f"\n4-TUPLE OUTPUT TAG: (value={ratio_mid:.3e}/{composite}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
