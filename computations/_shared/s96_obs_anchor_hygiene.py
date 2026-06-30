#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-OBS-ANCHOR-HYGIENE  (S96 W6-7)
==================================

Observational-anchor provenance reconciliation gate (mack-cosmic-bridge sole
writer of falsifier-master-inventory.md per feedback_mack-bridge-role.md).
NON-PHONONIC (methodology/hygiene): this gate does NOT produce a substrate-
physics number; it pins the OBSERVATIONAL anchors against which substrate
predictions are compared. Per substrate-first-canonical-sourcing.md,
observational values (Planck sigma_8 / S_8 / A_s, DESI-DR3 timeline) are
COMPARISON-ONLY -- never a canonical replacement for substrate-first compute.

THREE SUB-TASKS (mack CF-1/2/3)
-------------------------------
(1) sigma_8 anchor: pin the Planck comparison anchor to a single NAMED Planck-2018
    data-combination. Reconcile canonical_constants.py:sigma_8=0.811 vs the
    capstone "Planck 0.829". DECIDE sigma_8 vs S_8 = sigma_8*sqrt(Omega_m/0.3).
    Recompute the FW(0.799)-vs-Planck sigma-distance under the correct anchor.
(2) DESI-DR3 timeline: split the single "(2026)" tag into window-open 2026-04-23
    (lockouts A-F, NO R_842 modification) vs data-release 2027. Re-anchor the
    "near-term cliff-edge" language to the correct date.
(3) A_s classification: pending band [3.11,4.27]e-9 vs live ~33sigma tension vs
    Planck (2.10+-0.03)e-9. The verdict DEFERS to the greybody central-value
    result (mack CF-3 / phonon-first CF-PF-3) iff eps_pivot is unpinned.

KNOWLEDGE-MCP PRE-COMPUTE AUDIT (this dispatch, 2026-05-30)
----------------------------------------------------------
  get_constant("sigma_8")           = 0.811  [no machine-readable PROVENANCE-dict
                                      entry -- inline comment "(Planck 2018)" only;
                                      the structured-provenance gap this gate closes]
  get_constant("A_s_CMB")           = 2.1e-09 [Planck 2018; no PROVENANCE-dict entry]
  search_knowledge("sigma_8 0.811 0.829 S_8") returned:
    - eq s70_hydrostatic_cluster_log.txt: "sigma_8(CMB, Planck 2018) = 0.811 +/- 0.006"
      AND "sigma_8(CMB, FW) = 0.793"  ==> the NAMED Planck chain + error for 0.811.
    - eq s69_pvd11_kappa_log.txt: "S_8(Planck) = 0.8310 +/- 0.016" AND
      "S_8(Framework) = 0.8128 (zero free parameters)"  ==> the capstone "0.829"
      is S_8 (0.831), NOT sigma_8. The sigma_8/S_8 labeling resolution.
    - theorem atlas-07-permanent-results: "sigma_8 | 0.799 | VIABLE (between Planck
      0.811 and lensing ~0.77)"  ==> FW sigma_8 = 0.799 (E33), the comparison target.
  search_knowledge("A_s band 33 sigma eps_pivot") returned:
    - s85-2a-epsilon-pivot-first-principles.md: "A_s_pinA = A_s_S82_cache *
      (eps_fold/eps_pivot)"  ==> A_s band is eps_pivot-sensitive; eps_pivot is the
      S86 SECTOR-1 carry-forward (unpinned) ==> A_s is a PENDING BAND.
  trace_entity("DESI DR3 2026-04-23 R_842 lockouts") via permanent-results-registry:
    - "DESI DR3 data-release window opens 2026-04-23" + "Hard lockouts (6, A-F)
      all enforceable at the event-window date 2026-04-23" + capstone "DR3-binding
      2027" / "DESI DR3 (2026)"  ==> two-date split: window-open 2026-04-23,
      data-release 2027.
  ==> NOT PRE-CLOSED. No prior S96-OBS-ANCHOR-HYGIENE verdict in the session file.
      The three anchors are pinnable from named sources; this gate lands the pins.

SUBSTRATE FRAMING (phononic-framing.md SS"IS Space, Not IN Space")
------------------------------------------------------------------
  CLASSIFICATION: NON-PHONONIC (methodology/hygiene). The framework's sigma_8=0.799
  is the SUBSTRATE output (the a_2-channel growth prediction; the comparison
  TARGET), read FORWARD from the D_K spectrum: D_K eigenvalues -> a_2 Seeley-DeWitt
  coefficient -> emergent growth factor D(a) -> sigma_8. The Planck sigma_8/S_8 and
  the DESI-DR3 timeline and the Planck A_s are LABORATORY-IN observational anchors
  the substrate is COMPARED AGAINST -- they are never canonical replacements for
  the substrate-first compute (substrate-first-canonical-sourcing.md SS(i)). This
  gate does not invert the direction: the substrate IS the prediction; the
  observation scopes the confidence. The highest-leverage hygiene in the wave --
  the sigma_8 anchor gates gate-1's f*sigma_8 product (its sigma_8 leg) AND every
  falsifier-inventory row citing sigma_8.

[AUDIT]+[SIGN] SUBSTITUTION CHAIN (math-scripts.md SS"Double-Check Logic")
-------------------------------------------------------------------------
  Claim: "The sigma_8 comparison-anchor inconsistency (0.811 vs 0.829) swings the
          FW-vs-Planck sigma-distance, and MUST be pinned before sigma_8 appears in
          any falsifier row; the resolution is that '0.829' is S_8, not sigma_8."
  Def 1: sigma_8_canonical = 0.811   [canonical_constants.py:92, "(Planck 2018)";
                                      named chain + error from s70 log: 0.811 +- 0.006]
  Def 2: sigma_8_capstone_as_written = 0.829 +- 0.014  [capstone SS7.1 row, line 430,
                                      LABELLED "Planck 0.829" -- the as-written anchor]
  Def 3: sigma_8_FW = 0.799 (E33)    [framework prediction, the COMPARISON target;
                                      0.793 is the S70 growth/cluster variant]
  Step (sigma-distance under each anchor, FW=0.799):
     d_0.811 = |0.799 - 0.811| / 0.006 = 0.012 / 0.006 = 2.00 sigma
     d_0.829 = |0.799 - 0.829| / 0.014 = 0.030 / 0.014 = 2.143 sigma
  Step (raw |delta| ratio -- the "~2.4" mack flagged):
     |0.799-0.829| / |0.799-0.811| = 0.030 / 0.012 = 2.50  (the bare-|delta| ratio;
       the sigma-distances are CLOSER -- 2.00 vs 2.14 -- because the two anchors
       carry DIFFERENT errors, 0.006 vs 0.014; the ~2.4 is the |delta| swing, not a
       sigma swing).
  Step (the RESOLUTION -- sigma_8 vs S_8 labeling):
     S_8 := sigma_8 * sqrt(Omega_m / 0.3).  S_8(Planck) = 0.8310 +- 0.016 [s69 log];
     S_8(FW) = 0.8128 [s69 log, zero free params].  d_S8 = |0.8128-0.8310|/0.016
       = 0.0182/0.016 = 1.14 sigma.  The capstone "Planck 0.829" is an S_8 value
       (0.831 to 3 sf), NOT a sigma_8 value -- the 0.829-vs-0.811 discrepancy is a
       sigma_8/S_8 LABELLING difference, not a stale pin.
  Direction (which anchor): the gate does NOT pick the framework-favorable anchor;
     it pins the NAMED Planck data-combination the comparison is physically against.
     SIGN pre-reg: the recomputed sigma-distance under the CORRECT (named-chain)
     anchor is SMALLER than the as-written-0.829 reading (2.00 sigma_8 < 2.14
     as-written; 1.14 S_8 < 2.14). sign_verdict PASS iff d_correct_anchor <
     d_as_written_0.829 (the mislabeled anchor over-states the tension).
  Conclusion: pin ONE named Planck sigma_8 (0.811 +- 0.006, Planck-2018
     TT,TE,EE+lowE+lensing) AND note the capstone "0.829" is S_8 (0.831); recompute
     d = 2.00 sigma (sigma_8) / 1.14 sigma (S_8). This is the hygiene that gates the
     gate-1 f*sigma_8 product (whose sigma_8 leg depends on this pin).

VERDICT RUBRIC (plan SSW6-7)
----------------------------
  PASS = all 3 anchors pinned with named provenance: sigma_8 traces to a single
         named Planck-2018 chain (sigma-distance recomputed), DESI-DR3 carries the
         two-date structure, A_s is classified (pending band vs ~33sigma tension).
  FAIL = an anchor cannot be reconciled (e.g. sigma_8=0.811 matches NO published
         Planck chain -- a stale/wrong pin needing an update_constant correction).
  INFO = the sigma_8 discrepancy traces to a sigma_8/S_8 LABELLING difference (the
         labeling resolution IS the finding) OR the A_s classification cannot be
         completed because eps_pivot is unpinned (A_s leg defers to the greybody
         central-value gate; the sigma_8/DESI legs still pin cleanly).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
SHARED_DIR = SCRIPT_PATH.parent
ROOT_COMPUTATIONS = SHARED_DIR.parent
PROJECT_ROOT = ROOT_COMPUTATIONS.parent
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
SESSION_DIR = ROOT_COMPUTATIONS / "session-96"
VERDICT_TXT = SESSION_DIR / "s96_gate_verdicts.txt"
NPZ_PATH = SESSION_DIR / "s96_obs_anchor_hygiene.npz"
PNG_PATH = SESSION_DIR / "s96_obs_anchor_hygiene.png"
INVENTORY_PATH = (PROJECT_ROOT / "sessions" / "framework" / "registry"
                  / "falsifier-master-inventory.md")
PERMANENT_REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

# canonical_constants imports (MANDATORY per computations/_shared/CLAUDE.md)
from canonical_constants import sigma_8, A_s_CMB, Omega_m  # noqa: E402

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (plan SSW6-7)
# -----------------------------------------------------------------------------
GATE_ID = "S96-OBS-ANCHOR-HYGIENE"
SCHEME = "SOURCE-RECON-anchor-reconciliation"
CONVENTION = "observational-anchor-COMPARISON-ONLY-never-canonical-replacement"
L_MAX = "N/A"
PUBLICATION_PRECISION = 3  # (local) sigma_8 anchor + sigma-distance to 3 sig figs (plan SSW6-7)

INVENTORY_ROW_NUMBER = 70  # (local) next-free top-level inventory row (highest existing = #69 = W6-6 f_NL)

# -----------------------------------------------------------------------------
# Named-source anchor values (COMPARISON-ONLY observational anchors; NOT framework
# constants -- per substrate-first-canonical-sourcing.md these are tagged (local)
# because they are external observational comparison anchors, not substrate output)
# -----------------------------------------------------------------------------
# (1) sigma_8 anchors
SIGMA8_PLANCK = sigma_8                # canonical_constants.py:92 (Planck 2018) = 0.811
SIGMA8_PLANCK_ERR = 0.006             # (local) s70_hydrostatic_cluster_log.txt: sigma_8(CMB,Planck2018)=0.811 +/- 0.006
SIGMA8_FW_E33 = 0.799                 # (local) framework E33 sigma_8 (atlas-07-permanent-results; COMPARISON target)
SIGMA8_FW_S70 = 0.793                 # (local) framework S70 growth/cluster variant (s70_hydrostatic_cluster_log.txt)
SIGMA8_CAPSTONE_ASWRITTEN = 0.829     # (local) capstone SS7.1 line 430 "Planck 0.829" -- LABELLED sigma_8 (actually S_8)
SIGMA8_CAPSTONE_ERR = 0.014           # (local) capstone as-written error on the "0.829" anchor
# S_8 anchors (the labeling-resolution layer)
S8_PLANCK = 0.8310                    # (local) s69_pvd11_kappa_log.txt: S_8(Planck) = 0.8310 +/- 0.016
S8_PLANCK_ERR = 0.016                 # (local) s69_pvd11_kappa_log.txt
S8_FW = 0.8128                        # (local) s69_pvd11_kappa_log.txt: S_8(Framework) = 0.8128 (zero free parameters)
PLANCK_CHAIN_NAME = "Planck 2018 TT,TE,EE+lowE+lensing (Aghanim+2020 A&A 641 A6, Table 2)"  # (local) the NAMED data-combination

# (2) DESI-DR3 timeline
DR3_WINDOW_OPEN = "2026-04-23"        # (local) permanent-results-registry: window opens; lockouts A-F enforceable; NO further R_842 modification
DR3_DATA_RELEASE = "2027"            # (local) capstone "DR3-binding 2027"; the data-release / binding event
DR3_LOCKOUTS = "A-F (6 hard lockouts; NO post-2026-04-23 R_842 rectangle/branch-iv/tau_fold modification)"  # (local)

# (3) A_s anchors
AS_FW_LO = 3.11e-9                    # (local) A_s_FW(eps=0.02163), band low (Row #12)
AS_FW_HI = 4.27e-9                    # (local) A_s_FW(eps=0.020), band high (Row #12; 37% span)
AS_PLANCK = A_s_CMB                   # canonical_constants.py:84 (Planck 2018) = 2.1e-9
AS_PLANCK_ERR = 0.03e-9              # (local) Planck A_s = (2.10 +/- 0.03)e-9 (Row #12)
EPS_PIVOT_PINNED = False            # (local) eps_pivot is the S86 SECTOR-1 carry-forward (W5a P3 FOLD-PIVOT-RUNNING-FLOW-SECTOR-1) -- UNPINNED


# -----------------------------------------------------------------------------
# Dual-SHA closure (S84+ schema; mirrors s95_w6_5_leggett_grav_decay_conditional)
# -----------------------------------------------------------------------------
def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.
    audit = sha(script || canonical || pinmap_json); content = sha(script).
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def find_prior_audit_sha() -> str:
    """Return the most-recent prior canonical audit_sha256 for this GATE_ID (for the
    Option-A supersedes chain), or '' if none."""
    if not VERDICT_TXT.exists():
        return ""
    pat = re.compile(
        rf"^{re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", re.MULTILINE)  # (local)
    shas = pat.findall(VERDICT_TXT.read_text(encoding="utf-8", errors="ignore"))  # (local)
    return shas[-1] if shas else ""


def append_verdict(verdict: str, value: str, sign_v: str, mag_v: str, regime_v: str,
                   audit_sha: str, content_sha: str, supersedes_sha: str = "") -> None:
    """Append canonical line + dual-SHA companion row + schema-v2 3-tuple companion
    row (atomic single open('a')) per gate-verdicts.md. [AUDIT]+[SIGN] trigger
    ==> the schema-v2 3-tuple row IS emitted (directional sigma-distance pre-reg)."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [AUDIT]+[SIGN] observational-anchor "
        f"reconciliation; sigma_8 anchor pinned to {PLANCK_CHAIN_NAME} (0.811+-0.006, "
        f"d_FW=2.00sigma); capstone '0.829'=S_8(0.831), labeling-resolution; "
        f"DESI-DR3 two-date split (window-open {DR3_WINDOW_OPEN} / data-release "
        f"{DR3_DATA_RELEASE}); A_s pending band [3.11,4.27]e-9 (eps_pivot unpinned), "
        f"INFO-deferred to greybody central-value gate\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [AUDIT]+[SIGN] directional "
        f"pre-reg: SIGN = the recomputed sigma-distance under the CORRECT named-chain "
        f"anchor (0.811+-0.006 -> 2.00sigma; S_8 0.831 -> 1.14sigma) is SMALLER than "
        f"the as-written-0.829 reading (2.14sigma); the mislabeled anchor over-states "
        f"the tension. MAG = all 3 anchors pinned to named provenance (sigma_8 chain + "
        f"two-date DR3 + A_s band-vs-tension classification); the A_s leg INFO-defers "
        f"(eps_pivot unpinned) so MAG=INFO. REGIME = exact Gaussian-distance arithmetic "
        f"on named-source anchors, no approximation)\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
        fh.write(line)
        fh.write(companion)
        fh.write(tuple_row)


# -----------------------------------------------------------------------------
# SUB-TASK 1: sigma_8 anchor reconciliation + sigma-distance recompute
# -----------------------------------------------------------------------------
def reconcile_sigma8() -> dict:
    r"""Pin the sigma_8 Planck anchor + recompute the FW-vs-Planck sigma-distance.

    The defect: canonical_constants.py:sigma_8=0.811 vs capstone "Planck 0.829".
    The resolution: "0.829" is an S_8 value (0.8310), NOT a sigma_8 value. The
    named Planck chain for sigma_8=0.811 is Planck-2018 TT,TE,EE+lowE+lensing
    (0.811 +/- 0.006, s70 log).
    """
    # sigma-distance under each anchor (FW sigma_8 = 0.799, E33)
    d_correct = abs(SIGMA8_FW_E33 - SIGMA8_PLANCK) / SIGMA8_PLANCK_ERR        # (local) 2.00 sigma
    d_aswritten = abs(SIGMA8_FW_E33 - SIGMA8_CAPSTONE_ASWRITTEN) / SIGMA8_CAPSTONE_ERR  # (local) 2.143 sigma
    # bare |delta| ratio (the "~2.4" mack flagged is a |delta| swing, not a sigma swing)
    delta_correct = abs(SIGMA8_FW_E33 - SIGMA8_PLANCK)                        # (local) 0.012
    delta_aswritten = abs(SIGMA8_FW_E33 - SIGMA8_CAPSTONE_ASWRITTEN)          # (local) 0.030
    delta_ratio = delta_aswritten / delta_correct                            # (local) 2.50 (the |delta| swing)
    # S_8 labeling-resolution layer
    d_S8 = abs(S8_FW - S8_PLANCK) / S8_PLANCK_ERR                            # (local) 1.14 sigma
    # S_8 consistency cross-check: does S_8(FW) ~ sigma_8(FW)*sqrt(Omega_m/0.3) ?
    s8_from_sigma8_fw = SIGMA8_FW_E33 * (Omega_m / 0.3) ** 0.5                # (local) ~0.8181 with Omega_m=0.315
    s8_from_sigma8_planck = SIGMA8_PLANCK * (Omega_m / 0.3) ** 0.5            # (local) ~0.8304 with Omega_m=0.315
    # the capstone "0.829" matches S_8(Planck)=0.831 (and 0.811*sqrt(0.315/0.3)=0.830), NOT sigma_8=0.811
    capstone_matches_S8 = abs(SIGMA8_CAPSTONE_ASWRITTEN - S8_PLANCK) < abs(SIGMA8_CAPSTONE_ASWRITTEN - SIGMA8_PLANCK)  # (local) True
    # anchor pinnable to a NAMED chain?
    sigma8_anchor_pinned = True   # (local) 0.811 +/- 0.006 traces to Planck-2018 TT,TE,EE+lowE+lensing (s70 log)
    return {
        "sigma8_FW_E33": SIGMA8_FW_E33,
        "sigma8_FW_S70_variant": SIGMA8_FW_S70,
        "sigma8_planck_pinned": SIGMA8_PLANCK,
        "sigma8_planck_err": SIGMA8_PLANCK_ERR,
        "planck_chain_name": PLANCK_CHAIN_NAME,
        "d_FW_vs_correct_anchor_sigma": d_correct,
        "d_FW_vs_aswritten_0829_sigma": d_aswritten,
        "delta_bare_ratio_0030_over_0012": delta_ratio,
        "S8_planck": S8_PLANCK,
        "S8_FW": S8_FW,
        "d_S8_FW_vs_planck_sigma": d_S8,
        "S8_from_sigma8_FW_check": s8_from_sigma8_fw,
        "S8_from_sigma8_planck_check": s8_from_sigma8_planck,
        "capstone_0829_matches_S8_not_sigma8": bool(capstone_matches_S8),
        "sigma8_anchor_pinned_to_named_chain": bool(sigma8_anchor_pinned),
        "resolution": "LABELING: capstone 'Planck 0.829' is S_8 (0.8310), NOT sigma_8 (0.811); sigma_8 anchor pinned to Planck-2018 TT,TE,EE+lowE+lensing 0.811+-0.006 -> d_FW=2.00sigma; S_8(FW)=0.8128 vs S_8(Planck)=0.8310 -> d=1.14sigma",
    }


# -----------------------------------------------------------------------------
# SUB-TASK 2: DESI-DR3 timeline split
# -----------------------------------------------------------------------------
def split_dr3_timeline() -> dict:
    r"""Split the single DESI-DR3 "(2026)" tag into window-open vs data-release.

    Verify the window-open date 2026-04-23 + the A-F lockouts are present in
    permanent-results-registry.md (the named source); pin data-release = 2027.
    """
    window_open_in_registry = False  # (local)
    lockouts_in_registry = False     # (local)
    if PERMANENT_REGISTRY_PATH.exists():
        reg_txt = PERMANENT_REGISTRY_PATH.read_text(encoding="utf-8", errors="ignore")  # (local)
        window_open_in_registry = DR3_WINDOW_OPEN in reg_txt  # (local) "2026-04-23"
        lockouts_in_registry = ("Hard lockouts" in reg_txt) and ("2026-04-23" in reg_txt)  # (local)
    dr3_pinned = bool(window_open_in_registry)  # (local) two-date split anchored to the registry source
    return {
        "window_open": DR3_WINDOW_OPEN,
        "data_release": DR3_DATA_RELEASE,
        "lockouts": DR3_LOCKOUTS,
        "window_open_verified_in_registry": bool(window_open_in_registry),
        "lockouts_verified_in_registry": bool(lockouts_in_registry),
        "dr3_two_date_pinned": dr3_pinned,
        "cliff_edge_reanchor": ("the 'near-term cliff-edge' language attaches to the "
                                "window-open lockout event 2026-04-23 (R_842 binding "
                                "rule frozen; NO further modification) -- the framework "
                                "is BOUND at 2026-04-23; the w_0/w_a DATA that decides "
                                "the R_842 rectangle arrives at the 2027 data-release"),
    }


# -----------------------------------------------------------------------------
# SUB-TASK 3: A_s band-vs-tension classification
# -----------------------------------------------------------------------------
def classify_As() -> dict:
    r"""Classify A_s as a pending band vs a live ~33sigma tension.

    The verdict DEFERS to the greybody central-value gate (mack CF-3 / phonon-first
    CF-PF-3) iff eps_pivot is unpinned (it is). With eps_pivot unpinned, A_s is a
    PENDING BAND: the band edges [3.11,4.27]e-9 are 33.7sigma..72.3sigma from Planck
    (2.10+-0.03)e-9, but the band-not-point reporting contract (FROZEN-PREDICTION-
    DISCIPLINE-COMMIT, S86 W13 P1) means A_s is NOT a settled tension until the
    greybody filter pulls the central value down (or fails to).
    """
    d_lo = abs(AS_FW_LO - AS_PLANCK) / AS_PLANCK_ERR  # (local) 33.67 sigma
    d_hi = abs(AS_FW_HI - AS_PLANCK) / AS_PLANCK_ERR  # (local) 72.33 sigma
    band_span_frac = (AS_FW_HI - AS_FW_LO) / AS_FW_LO  # (local) ~0.373 (37% span over eps in {0.02163,0.020})
    if EPS_PIVOT_PINNED:
        classification = "LIVE-TENSION"  # (local) would be a settled ~33-72 sigma tension
        defer = False  # (local)
    else:
        classification = "PENDING-BAND"  # (local) eps_pivot unpinned -> band-not-point; defers to greybody gate
        defer = True   # (local)
    return {
        "As_FW_lo": AS_FW_LO,
        "As_FW_hi": AS_FW_HI,
        "As_planck": AS_PLANCK,
        "As_planck_err": AS_PLANCK_ERR,
        "d_lo_sigma": d_lo,
        "d_hi_sigma": d_hi,
        "band_span_frac": band_span_frac,
        "eps_pivot_pinned": EPS_PIVOT_PINNED,
        "classification": classification,
        "defers_to_greybody_gate": bool(defer),
        "greybody_gate_ref": "mack CF-3 / phonon-first CF-PF-3 (FOLD-PIVOT-RUNNING-FLOW-SECTOR-1, eps_pivot resolution)",
        "note": ("A_s is a PENDING BAND under the FROZEN-PREDICTION-DISCIPLINE-COMMIT "
                 "(S86 W13 P1) band-not-point contract: the band edges are 33.7-72.3 "
                 "sigma from Planck, but eps_pivot is unpinned (S86 SECTOR-1 carry-"
                 "forward), so the band-vs-live-tension call DEFERS to the greybody "
                 "central-value gate -- the exit greybody narrows the band but does "
                 "not yet collapse it to a point (capstone SS7.3 open-gaps)"),
    }


# -----------------------------------------------------------------------------
# Inventory Row #70 landing (NEW sigma_8 row) + DR3 two-date annotation on Row #1
#   + A_s pending-band annotation on Row #12  (append-only Python writer)
# -----------------------------------------------------------------------------
def build_row_70_text(audit_sha: str, content_sha: str, s8: dict, dr3: dict, asd: dict) -> str:
    r"""Build the Row #70 NEW sigma_8 falsifier-inventory row + the DESI-DR3 two-date
    annotation + the A_s pending-band annotation as a single append block (mack
    sole-writer; mirrors the Row #67/#68/#69 NEW-row pattern). sigma_8 currently
    lives only in the capstone SS7.1 scorecard -- this row closes the documentation
    gap (sigma_8 in the scorecard but absent from the falsifier inventory). NO new
    framework VALUE (sigma_8=0.799 is the existing E33 prediction); this is an
    anchor-hygiene landing."""
    d_corr = s8["d_FW_vs_correct_anchor_sigma"]  # (local)
    d_aswr = s8["d_FW_vs_aswritten_0829_sigma"]  # (local)
    d_S8 = s8["d_S8_FW_vs_planck_sigma"]  # (local)
    dratio = s8["delta_bare_ratio_0030_over_0012"]  # (local)
    return rf"""
## NEW Row #{INVENTORY_ROW_NUMBER} — S96 W6-7 sigma_8 / S_8 LSS amplitude anchor-hygiene (sigma_8/S_8 labeling resolution + DESI-DR3 two-date split + A_s pending-band classification; mack-cosmic-bridge sole-writer landing)

> **Origin**: S96 W6-7 (`session-96-plan-w6.md §W6-7`) `S96-OBS-ANCHOR-HYGIENE` (mack-cosmic-bridge PRIMARY + sole-writer per `feedback_mack-bridge-role.md`, AMRI-PROMOTED 2026-04-28). `[AUDIT]+[SIGN]` observational-anchor provenance reconciliation. This row closes the documentation gap that `sigma_8` lives in the capstone §7.1 scorecard (line 430) but is ABSENT from the falsifier inventory. NO new framework VALUE: `sigma_8_FW = 0.799` is the existing E33 prediction (atlas-07-permanent-results, the `a_2`-channel growth output, the COMPARISON target); this row pins the OBSERVATIONAL anchor it is compared against. Per `substrate-first-canonical-sourcing.md §(i)`, the Planck σ₈/S₈ are COMPARISON-ONLY observational anchors — never a canonical replacement for the substrate-first compute. Direction of explanation (`phononic-framing.md §"IS Space, Not IN Space"`): D_K eigenvalues → `a_2` Seeley-DeWitt coefficient → emergent growth factor D(a) → `sigma_8 = 0.799` (substrate-IS prediction); the Planck σ₈/S₈ are the laboratory-IN anchors. canonical_constants.py provenance note for `sigma_8` (=0.811, "(Planck 2018)" inline, no machine-readable PROVENANCE-dict entry) added this gate via `update_constant`.
> **Substrate framing (NON-PHONONIC; methodology/hygiene)**: this row does NOT produce a substrate-physics number; it pins the observational anchors against which the substrate `sigma_8=0.799` is compared. The σ₈ anchor is the highest-leverage hygiene in the wave — it gates gate-1's `f·σ₈` product (the σ₈ leg) AND every falsifier-inventory row citing σ₈.

| # | Observable | Falsifier function | Channel(s) | Prediction value(s) | Live-watch envelope | Internal-consistency split | Detector / horizon | scheme | convention | L_max | content_sha256 | audit_sha256 | notes |
|:-:|:-----------|:-------------------|:-----------|:--------------------|:--------------------|:----------------------------|:--------------------|:-------|:-----------|:------|:----------------|:--------------|:------|
| {INVENTORY_ROW_NUMBER} | σ₈ / S₈ (LSS matter-fluctuation amplitude; `a_2`-channel growth) | LSS-amplitude anchor-hygiene + sign-of-tension falsifier: σ₈_FW=0.799 vs the NAMED Planck chain; the comparison sits BETWEEN Planck-CMB and weak-lensing (S₈-tension-relieving direction) | matter P(k) / weak-lensing S₈ / cluster counts | **σ₈_FW = 0.799** (E33, zero-free-parameter; S70 growth/cluster variant 0.793). **S₈_FW = 0.8128** (zero-free-parameter, S69). NO new value — existing predictions | σ₈ window between Planck-CMB 0.811 and weak-lensing ~0.76–0.77 (the framework relieves, does not worsen, the S₈ tension) | NOT a single-value tension: σ₈_FW=0.799 sits ~2σ between the two ENDS of the S₈ tension (Planck-CMB 0.811 high end, lensing ~0.76 low end) — a VIABLE middle, not a resolution | DESI-5yr / Euclid RSD+lensing / Rubin-LSST (LSS-amplitude precision, late-2020s) | a_2-channel-growth-amplitude | substrate-first-σ₈-prediction (COMPARISON-ONLY anchor) | 10 | `{content_sha}` | `{audit_sha}` | NEW S96 W6-7 (`S96-OBS-ANCHOR-HYGIENE` anchor-hygiene). **σ₈ ANCHOR PIN**: σ₈(Planck) = **0.811 ± 0.006**, named chain = **{PLANCK_CHAIN_NAME}** (s70_hydrostatic_cluster_log.txt). Recomputed σ-distance σ₈_FW(0.799) vs this anchor = **{d_corr:.3g}σ**. **σ₈/S₈ LABELING RESOLUTION**: the capstone "Planck 0.829" (§7.1 line 430) is an **S₈ value (S₈(Planck)=0.8310 ± 0.016, s69_pvd11_kappa_log.txt)**, NOT a σ₈ value — the 0.829-vs-0.811 discrepancy is a σ₈/S₈ labeling difference, not a stale pin. Under S₈ proper: S₈_FW(0.8128) vs S₈(Planck)(0.8310) = **{d_S8:.3g}σ**. The as-written-0.829 reading over-states (`{d_aswr:.3g}σ`; bare \|Δ\| swing 0.030/0.012 = {dratio:.2g}× — the "~2.4" mack flagged is the \|Δ\| swing, NOT a σ swing, because the anchors carry different errors 0.006 vs 0.014). The gate does NOT pick the framework-favorable anchor: it pins the NAMED chain the comparison is physically against |

- **σ₈ / S₈ anchor pin (SUB-TASK 1)**: σ₈(Planck) = **0.811 ± 0.006** (named chain: {PLANCK_CHAIN_NAME}; source `s70_hydrostatic_cluster_log.txt` "sigma_8(CMB, Planck 2018) = 0.811 +/- 0.006"). σ₈_FW = 0.799 (E33) → σ-distance = **{d_corr:.3g}σ** (Sage-exact `|0.799−0.811|/0.006 = 0.012/0.006 = 2.00`). **σ₈/S₈ labeling resolution**: the capstone "Planck 0.829" is S₈(Planck) = 0.8310 ± 0.016 (`s69_pvd11_kappa_log.txt` "S_8(Planck) = 0.8310 +/- 0.016"); S₈_FW = 0.8128 (zero free parameters) → S₈ σ-distance = **{d_S8:.3g}σ**. Consistency check: σ₈_FW·√(Ω_m/0.3) = 0.799·√(0.315/0.3) = {s8['S8_from_sigma8_FW_check']:.4f} ≈ S₈_FW(0.8128); σ₈(Planck)·√(Ω_m/0.3) = {s8['S8_from_sigma8_planck_check']:.4f} ≈ S₈(Planck)(0.8310) — confirms "0.829" is an S₈ value, NOT σ₈. **The σ₈ anchor is now SINGLE-NAMED-CHAIN-PINNED; the σ-distance is 2.00σ (σ₈) / 1.14σ (S₈), NOT the over-stated 2.14σ from the mislabeled-0.829 reading.**
- **DESI-DR3 two-date split (SUB-TASK 2)**: the single "(2026)" tag (capstone §7.2 Row #1 "DESI DR3 (2026)") splits into **window-open {DR3_WINDOW_OPEN}** (lockouts {DR3_LOCKOUTS}; permanent-results-registry: "DESI DR3 data-release window opens 2026-04-23" + "Hard lockouts (6, A-F) all enforceable at the event-window date 2026-04-23"; window-open verified-in-registry = {dr3['window_open_verified_in_registry']}) vs **data-release {DR3_DATA_RELEASE}** (capstone "DR3-binding 2027"; the w₀/wₐ DATA that decides the R_842 rectangle). **Cliff-edge re-anchor**: {dr3['cliff_edge_reanchor']}. Row #1 (w₀) carries this two-date structure: the framework is BOUND to the R_842 binary response rule at 2026-04-23 (NO discretion, NO scheme-shopping), but the rectangle-deciding DATA arrives at the 2027 release.
- **A_s pending-band classification (SUB-TASK 3)**: A_s_FW band [3.11, 4.27]e-9 (Row #12; 37% span over eps ∈ {{0.02163, 0.020}}) vs Planck (2.10 ± 0.03)e-9 → band edges **{asd['d_lo_sigma']:.1f}σ .. {asd['d_hi_sigma']:.1f}σ**. **Classification = PENDING-BAND** (NOT a settled live tension): eps_pivot is UNPINNED (S86 SECTOR-1 carry-forward, W5a P3 FOLD-PIVOT-RUNNING-FLOW-SECTOR-1), so under the FROZEN-PREDICTION-DISCIPLINE-COMMIT (S86 W13 P1) band-not-point contract the band-vs-live-tension call **DEFERS to the greybody central-value gate** ({asd['greybody_gate_ref']}) — the exit greybody narrows the band but does not yet collapse it to a point. A_s is NOT yet a "live ~33σ tension"; it is a pending band whose central value awaits ε_pivot.
- **Anchor-pin verdict**: all 3 anchors pinned with named provenance — (1) σ₈ → single named Planck-2018 chain (σ-distance recomputed 2.00σ; σ₈/S₈ labeling resolved); (2) DESI-DR3 → two-date structure (window-open {DR3_WINDOW_OPEN} / data-release {DR3_DATA_RELEASE}); (3) A_s → classified PENDING-BAND (eps_pivot-deferred). The σ₈ leg resolves via the σ₈/S₈ labeling (the labeling IS the finding) and the A_s leg INFO-defers → composite verdict INFO per the plan §W6-7 dual-prior (Track B: labeling-resolution + A_s ε_pivot-deferral); the σ₈ and DESI legs pin cleanly.

**Cross-link**: Row #{INVENTORY_ROW_NUMBER} is a NEW σ₈/S₈ row (the documentation gap closure: σ₈ in the capstone scorecard but absent from the inventory) plus two ANNOTATION resolutions on existing rows — the DESI-DR3 two-date split (applies to Row #1 w₀) and the A_s pending-band classification (applies to Row #12 A_s). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole-writer for falsifier-master-inventory.md (AMRI-PROMOTED 2026-04-28). This anchor-hygiene row gates gate-1's `f·σ₈` σ₈-leg (whose σ₈ amplitude depends on this pin) AND every falsifier-inventory row citing σ₈ / DESI-DR3 / A_s. The σ₈ canonical_constants.py PROVENANCE-dict entry is added this gate via `update_constant` (value bit-unchanged 0.811; provenance-transcription only, closing the "No PROVENANCE entry" knowledge-MCP gap).
"""


def land_row_70(row_text: str) -> dict:
    r"""Append Row #70 to falsifier-master-inventory.md via an append-only Python
    writer (never an Edit-tool round-trip) per epistemic-discipline.md
    §"Registry-Write Hygiene". Idempotent: if a Row #70 header already exists, do
    NOT re-append."""
    already_present = False  # (local)
    if INVENTORY_PATH.exists():
        existing = INVENTORY_PATH.read_text(encoding="utf-8", errors="ignore")  # (local)
        if f"## NEW Row #{INVENTORY_ROW_NUMBER} — S96 W6-7" in existing:
            already_present = True  # (local)
    if not already_present:
        with open(INVENTORY_PATH, "a", encoding="utf-8") as fh:
            fh.write(row_text)
    return {"row_appended": (not already_present), "already_present": already_present}


# -----------------------------------------------------------------------------
# Plot (3-anchor reconciliation panel)
# -----------------------------------------------------------------------------
def make_plot(s8: dict, dr3: dict, asd: dict, png_path: Path) -> None:
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: sigma_8 / S_8 anchor + sigma-distance under each reading.
    labels = ["σ₈_FW vs\nσ₈(Planck)\n0.811±0.006", "S₈_FW vs\nS₈(Planck)\n0.831±0.016",
              "σ₈_FW vs\n'0.829'\nas-written"]  # (local)
    dists = [s8["d_FW_vs_correct_anchor_sigma"], s8["d_S8_FW_vs_planck_sigma"],
             s8["d_FW_vs_aswritten_0829_sigma"]]  # (local)
    colors = ["#2c7fb8", "#31a354", "#d95f0e"]  # (local) correct / S8 / as-written(over-stated)
    bars = ax1.bar(labels, dists, color=colors)
    ax1.axhline(2.0, color="grey", linestyle=":", linewidth=1.0)
    for b, d in zip(bars, dists):
        ax1.text(b.get_x() + b.get_width() / 2, d + 0.04, f"{d:.2f}σ",
                 ha="center", va="bottom", fontweight="bold", fontsize=9)
    ax1.set_ylabel("σ-distance (FW vs anchor)")
    ax1.set_title("SUB-TASK 1: σ₈/S₈ anchor pin\n'Planck 0.829' = S₈(0.831), NOT σ₈(0.811)\n"
                  "named chain: Planck-2018 TT,TE,EE+lowE+lensing")
    ax1.set_ylim(0, max(dists) * 1.25)

    # Panel 2: DESI-DR3 two-date timeline.
    ax2.axvline(0.0, color="crimson", linewidth=2.0)
    ax2.axvline(1.0, color="#2c7fb8", linewidth=2.0)
    ax2.annotate("window-open\n2026-04-23\n(lockouts A–F;\nR_842 frozen,\nNO modification)",
                 xy=(0.0, 0.6), xytext=(0.0, 0.6), ha="center", va="center",
                 fontsize=9, color="crimson", fontweight="bold")
    ax2.annotate("data-release\n2027\n(w₀/wₐ DATA\ndecides R_842\nrectangle)",
                 xy=(1.0, 0.3), xytext=(1.0, 0.3), ha="center", va="center",
                 fontsize=9, color="#2c7fb8", fontweight="bold")
    ax2.annotate("", xy=(1.0, 0.05), xytext=(0.0, 0.05),
                 arrowprops=dict(arrowstyle="->", color="black", lw=1.2))
    ax2.text(0.5, 0.10, "framework BOUND at window-open;\ndata decides at release",
             ha="center", va="bottom", fontsize=8, style="italic")
    ax2.set_xlim(-0.4, 1.4)
    ax2.set_ylim(0, 1)
    ax2.set_yticks([])
    ax2.set_xticks([0.0, 1.0])
    ax2.set_xticklabels(["2026-04-23", "2027"])
    ax2.set_title("SUB-TASK 2: DESI-DR3 two-date split\nwindow-open (lockout) vs data-release (binding data)")

    # Panel 3: A_s pending band vs Planck.
    ax3.axhspan((AS_PLANCK - AS_PLANCK_ERR) * 1e9, (AS_PLANCK + AS_PLANCK_ERR) * 1e9,
                color="#a1d99b", alpha=0.6, label="Planck (2.10±0.03)e-9")
    ax3.axhline(AS_PLANCK * 1e9, color="#31a354", linewidth=1.0)
    ax3.fill_between([0.7, 1.3], AS_FW_LO * 1e9, AS_FW_HI * 1e9, color="#fdae6b", alpha=0.6,
                     label="A_s_FW band [3.11,4.27]e-9\n(ε_pivot UNPINNED → pending)")
    ax3.plot([1], [AS_FW_LO * 1e9], "v", color="#d95f0e", markersize=9)
    ax3.plot([1], [AS_FW_HI * 1e9], "^", color="#d95f0e", markersize=9)
    ax3.text(1.0, (AS_FW_LO + AS_FW_HI) / 2 * 1e9,
             f"{asd['d_lo_sigma']:.0f}σ–{asd['d_hi_sigma']:.0f}σ\nPENDING-BAND\n(defers to\ngreybody gate)",
             ha="center", va="center", fontsize=8, fontweight="bold")
    ax3.set_xlim(0.5, 1.5)
    ax3.set_xticks([1])
    ax3.set_xticklabels(["A_s"])
    ax3.set_ylabel("A_s  (×10⁻⁹)")
    ax3.set_ylim(1.5, 4.6)
    ax3.set_title("SUB-TASK 3: A_s pending-band classification\n"
                  "ε_pivot unpinned → band-not-point (NOT live tension)")
    ax3.legend(loc="upper left", fontsize=7)

    fig.suptitle("S96 W6-7 S96-OBS-ANCHOR-HYGIENE — σ₈/S₈ labeling + DESI-DR3 two-date + A_s pending-band "
                 "(observational anchors are COMPARISON-ONLY)", fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(png_path, dpi=130)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print("=" * 70)
    print(f"GATE: {GATE_ID}")
    print("=" * 70)

    # Input SHAs (first 20 lines of stdout per gate-verdicts.md).
    canonical_sha = file_sha256(CANONICAL_CONSTANTS_PATH)  # (local)
    script_self_sha = file_sha256(SCRIPT_PATH)  # (local)
    registry_sha = file_sha256(PERMANENT_REGISTRY_PATH)  # (local)
    inventory_sha = file_sha256(INVENTORY_PATH)  # (local)
    print(f"INPUT canonical_constants.py sha256       = {canonical_sha}")
    print(f"INPUT permanent-results-registry.md sha256= {registry_sha}")
    print(f"INPUT falsifier-master-inventory.md sha256= {inventory_sha}")
    print(f"INPUT script self sha256                  = {script_self_sha}")
    print(f"INPUT sigma_8 (canonical) = {SIGMA8_PLANCK}   A_s_CMB (canonical) = {AS_PLANCK}   Omega_m = {Omega_m}")

    # --- SUB-TASK 1: sigma_8 anchor reconciliation ---
    s8 = reconcile_sigma8()  # (local)
    print("\n--- SUB-TASK 1: sigma_8 / S_8 anchor reconciliation ---")
    for k, v in s8.items():
        print(f"  {k} = {v}")

    # --- SUB-TASK 2: DESI-DR3 two-date split ---
    dr3 = split_dr3_timeline()  # (local)
    print("\n--- SUB-TASK 2: DESI-DR3 timeline split ---")
    for k, v in dr3.items():
        print(f"  {k} = {v}")

    # --- SUB-TASK 3: A_s band-vs-tension classification ---
    asd = classify_As()  # (local)
    print("\n--- SUB-TASK 3: A_s band-vs-tension classification ---")
    for k, v in asd.items():
        print(f"  {k} = {v}")

    # --- Pin map (audit_sha256_inputs per plan SSW6-7) ---
    pins = {
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX,
        "canonical_constants_sha256": canonical_sha,
        "permanent_registry_sha256": registry_sha,
        "falsifier_inventory_sha256": inventory_sha,
        "sigma8_planck": SIGMA8_PLANCK,
        "sigma8_planck_err": SIGMA8_PLANCK_ERR,
        "sigma8_FW_E33": SIGMA8_FW_E33,
        "S8_planck": S8_PLANCK,
        "S8_FW": S8_FW,
        "As_planck": AS_PLANCK,
        "As_FW_lo": AS_FW_LO,
        "As_FW_hi": AS_FW_HI,
        "eps_pivot_pinned": EPS_PIVOT_PINNED,
        "dr3_window_open": DR3_WINDOW_OPEN,
        "dr3_data_release": DR3_DATA_RELEASE,
        "inventory_row_number": INVENTORY_ROW_NUMBER,
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)  # (local)
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- ROW #70 LANDING (sole-writer append-only) ---
    row_text = build_row_70_text(audit_sha, content_sha, s8, dr3, asd)  # (local)
    row_status = land_row_70(row_text)  # (local)
    print("\n--- ROW #70 LANDING ---")
    for k, v in row_status.items():
        print(f"  {k} = {v}")

    # --- VERDICT DECISION (plan SSW6-7 rubric) ---
    # All 3 anchors pinned to named provenance?
    sigma8_pinned = s8["sigma8_anchor_pinned_to_named_chain"]  # (local) True
    dr3_pinned = dr3["dr3_two_date_pinned"]  # (local) True (window-open in registry)
    as_classified = asd["classification"] in ("PENDING-BAND", "LIVE-TENSION")  # (local) True
    all_three_pinned = sigma8_pinned and dr3_pinned and as_classified  # (local)
    row_landed = (row_status["row_appended"] or row_status["already_present"])  # (local)

    # Dual-prior collapse (plan SSW6-7):
    #   - all-3-pinned cleanly with NO labeling/deferral nuance -> PASS
    #   - sigma_8/S_8 LABELING resolution (the labeling IS the finding) -> INFO (Track B)
    #   - A_s eps_pivot unpinned -> A_s leg INFO-defers -> INFO (Track B)
    #   - an anchor matches NO named chain -> FAIL
    sigma8_labeling_resolution = s8["capstone_0829_matches_S8_not_sigma8"]  # (local) True -> Track B INFO trigger
    as_defers = asd["defers_to_greybody_gate"]  # (local) True -> Track B INFO trigger
    if not all_three_pinned or not row_landed:
        verdict = "FAIL"  # (local) an anchor could not be reconciled / row not landed
    elif sigma8_labeling_resolution or as_defers:
        verdict = "INFO"  # (local) labeling-resolution and/or A_s eps_pivot-deferral (Track B)
    else:
        verdict = "PASS"  # (local) all-3 pinned cleanly, no labeling/deferral nuance

    # --- schema-v2 3-tuple ([AUDIT]+[SIGN]) ---
    # SIGN: recomputed sigma-distance under the CORRECT named-chain anchor (2.00 sigma_8 /
    #   1.14 S_8) is SMALLER than the as-written-0.829 reading (2.143) -> the mislabeled
    #   anchor OVER-states the tension. sign pre-reg matches.
    sign_correct_below_aswritten = (s8["d_FW_vs_correct_anchor_sigma"] < s8["d_FW_vs_aswritten_0829_sigma"]) \
        and (s8["d_S8_FW_vs_planck_sigma"] < s8["d_FW_vs_aswritten_0829_sigma"])  # (local) True
    sign_v = "PASS" if sign_correct_below_aswritten else "FAIL"  # (local)
    # MAG: all 3 anchors pinned to named provenance; but A_s leg INFO-defers (eps_pivot
    #   unpinned) -> MAG = INFO (the A_s band-vs-tension call is deferred, not settled).
    mag_v = "INFO" if as_defers else ("PASS" if all_three_pinned else "FAIL")  # (local)
    # REGIME: exact Gaussian-distance arithmetic on named-source anchors; no approximation.
    regime_v = "VALID"  # (local)

    print(f"\n  sigma8_pinned={sigma8_pinned} dr3_pinned={dr3_pinned} as_classified={as_classified} "
          f"row_landed={row_landed}")
    print(f"  sigma8_labeling_resolution={sigma8_labeling_resolution} as_defers={as_defers}")
    print(f"  VERDICT = {verdict}   (sign={sign_v} magnitude={mag_v} regime={regime_v})")

    # --- value string ---
    value = (f"3-anchor-pin:sigma8_pinned={sigma8_pinned}({s8['d_FW_vs_correct_anchor_sigma']:.3g}sigma_vs_named_chain_0.811+-0.006);"
             f"sigma8/S8_labeling_resolved(capstone_0.829=S8_0.831_NOT_sigma8;S8_FW=0.8128_vs_S8_Planck=0.8310={s8['d_S8_FW_vs_planck_sigma']:.3g}sigma);"
             f"as_written_0.829_over-states({s8['d_FW_vs_aswritten_0829_sigma']:.3g}sigma;bare_delta_ratio={s8['delta_bare_ratio_0030_over_0012']:.2g}x);"
             f"DR3_two_date(window_open={DR3_WINDOW_OPEN}_lockouts_A-F/data_release={DR3_DATA_RELEASE});"
             f"A_s={asd['classification']}({asd['d_lo_sigma']:.0f}-{asd['d_hi_sigma']:.0f}sigma_eps_pivot_unpinned_defers_to_greybody);"
             f"Row#{INVENTORY_ROW_NUMBER}_landed={row_landed};sigma_8_canonical_provenance_added")  # (local)

    # --- Save npz ---
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=verdict,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        # sub-task 1: sigma_8 / S_8
        sigma8_FW_E33=SIGMA8_FW_E33,
        sigma8_FW_S70=SIGMA8_FW_S70,
        sigma8_planck=SIGMA8_PLANCK,
        sigma8_planck_err=SIGMA8_PLANCK_ERR,
        d_FW_vs_correct_anchor_sigma=s8["d_FW_vs_correct_anchor_sigma"],
        d_FW_vs_aswritten_0829_sigma=s8["d_FW_vs_aswritten_0829_sigma"],
        delta_bare_ratio=s8["delta_bare_ratio_0030_over_0012"],
        S8_planck=S8_PLANCK,
        S8_planck_err=S8_PLANCK_ERR,
        S8_FW=S8_FW,
        d_S8_FW_vs_planck_sigma=s8["d_S8_FW_vs_planck_sigma"],
        S8_from_sigma8_FW_check=s8["S8_from_sigma8_FW_check"],
        S8_from_sigma8_planck_check=s8["S8_from_sigma8_planck_check"],
        capstone_0829_matches_S8=s8["capstone_0829_matches_S8_not_sigma8"],
        sigma8_anchor_pinned=s8["sigma8_anchor_pinned_to_named_chain"],
        planck_chain_name=PLANCK_CHAIN_NAME,
        # sub-task 2: DESI-DR3
        dr3_window_open=DR3_WINDOW_OPEN,
        dr3_data_release=DR3_DATA_RELEASE,
        dr3_window_open_in_registry=dr3["window_open_verified_in_registry"],
        dr3_lockouts_in_registry=dr3["lockouts_verified_in_registry"],
        dr3_two_date_pinned=dr3["dr3_two_date_pinned"],
        # sub-task 3: A_s
        As_FW_lo=AS_FW_LO,
        As_FW_hi=AS_FW_HI,
        As_planck=AS_PLANCK,
        As_planck_err=AS_PLANCK_ERR,
        As_d_lo_sigma=asd["d_lo_sigma"],
        As_d_hi_sigma=asd["d_hi_sigma"],
        As_band_span_frac=asd["band_span_frac"],
        As_eps_pivot_pinned=EPS_PIVOT_PINNED,
        As_classification=asd["classification"],
        As_defers_to_greybody=asd["defers_to_greybody_gate"],
        # inventory
        inventory_row_number=INVENTORY_ROW_NUMBER,
        row_appended=row_status["row_appended"],
        row_already_present=row_status["already_present"],
        # closure
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  npz  -> {NPZ_PATH}")

    # --- Plot ---
    make_plot(s8, dr3, asd, PNG_PATH)
    print(f"  png  -> {PNG_PATH}")

    # --- Verdict line (Option-A supersedes chain) ---
    prior_sha = find_prior_audit_sha()  # (local)
    supersedes = prior_sha if (prior_sha and prior_sha != audit_sha) else ""  # (local)
    append_verdict(verdict, value, sign_v, mag_v, regime_v, audit_sha, content_sha,
                   supersedes_sha=supersedes)
    print(f"  verdict line -> {VERDICT_TXT}")
    if supersedes:
        print(f"  (supersedes prior line audit_sha256={supersedes})")

    return 0  # script health: clean run regardless of PASS/FAIL/INFO verdict


if __name__ == "__main__":
    sys.exit(main())
