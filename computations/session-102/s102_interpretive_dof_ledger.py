#!/usr/bin/env python3
"""
S102 W5-5  —  S102-INTERPRETIVE-DOF-LEDGER  (mack-cosmic-bridge, sole-writer falsifier surface)

Assemble the consolidated interpretive-DOF ledger: the FOUR referee-M2 post-hoc rescopings,
each row carrying {original tension, rescoping move, atlas-09 item cross-reference, NEW binding
test}. The binding-test column is the load-bearing deliverable — a rescoping without a forward
falsification route is unfalsifiable bookkeeping (per feedback_reporting-framing.md: inflation's
flexibility = unfalsifiability, NOT strength; a legitimate rescoping points FORWARD to a test).

CLASSIFICATION: NON-PHONONIC (register-maintenance / scientific-integrity). This gate does NOT
compute a substrate observable. It CROSS-REFERENCES four EXISTING rescopings (each already
recorded in registers — atlas-09 / atlas-08-freshness / falsifier-master-inventory / canonical
constants) and ADDS the binding-test column citing ALREADY-PINNED values. No new sign/direction/
threshold is derived; each cited binding-test value carries its own upstream substitution chain
in its originating gate. The ledger ASSEMBLES; it does not re-derive.

PASS predicate (artifact-existence-with-content): 4 rescoping rows present, each with
{tension, rescoping, atlas-09 ref, binding test} non-empty.

Verdict semantics (pre-registered, plan §W5-5 PASS/FAIL/INFO):
  PASS  = all 4 rescopings assemble with a POPULATED, NAMED binding test AND a RESOLVING
          atlas-09 item cross-reference.
  FAIL  = a rescoping row cannot be assembled (atlas-09 ref does not resolve to ANY anchor,
          or a binding-test entry has NO identifiable NEW test).
  INFO  = the 4 rescopings assemble and ALL binding-test entries are POPULATED, but >=1 row's
          FORMAL atlas-09 retraction-row is genuinely PENDING (the rescoping currently lives in
          a sibling register-of-record — atlas-08-freshness / falsifier-master-inventory — and
          its atlas-09 formal row has not yet been authored). The row is marked
          atlas09_status=PENDING-formal-row with the NEAREST-resolving atlas-09 anchor + the
          register-of-record named, rather than left blank (fix-in-session,
          feedback_fix-in-session-never-defer.md).

On-disk reconciliation (orchestrator-verified state, this session):
  atlas-09-retractions.md = 214 lines, 46 items, scope "Sessions 1-88", git-UNMODIFIED this
  session. Only Item 37 (w_0 R_918->R_842) is a clean atlas-09 row for the four rescopings;
  Item 36 (eps_H Spectral Functional Crisis) is the NEAREST anchor for the alpha_s SCHEME-
  dependence family but the finer transport-degree rescoping (S92->S93 deg(T)=+2 NON-SCALAR)
  is a DISTINCT claim whose formal atlas-09 row is PENDING; SF54 + CGWB rescopings are S96/S100a-
  era and live in atlas-08-freshness + falsifier-master-inventory, formal atlas-09 rows PENDING.
  => honest verdict is INFO (every binding test populated; atlas-09 formal-row cross-ref partial).

Outputs:
  - sessions/framework/registry/interpretive-dof-ledger.md   (the consolidated register)
  - computations/session-102/s102_interpretive_dof_ledger.npz (machine record)
  - verdict payload PRINTED (agent calls emit_verdict; NO open-coded verdict-file append)
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # text assembly; CPU-cap (no GPU)

import sys
import json
import hashlib
import datetime
import numpy as np

# ---- canonical constants (MANDATORY; never hardcode framework values) ----
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared"))
from canonical_constants import (
    alpha_s_substrate_distance_1,   # -0.08587279  (substrate/BZ leaf, CMB-S4/CMB-HD channel)
    alpha_s_pivot_goldstone,        # 0.0          (CMB-pivot leaf, +0.67sigma vs Planck)
    w0_FW,                          # -0.918       (Volovik partition canonical; PRIMARY)
    A_FS_first_sound_ring,          # 0.204        (first-sound BAO ring amplitude c2^2/c1^2)
)

# ---- repo root + paths ----
HERE = os.path.dirname(os.path.abspath(__file__))                       # (local)
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))                  # (local)
LEDGER_PATH = os.path.join(ROOT, "sessions", "framework", "registry", "interpretive-dof-ledger.md")  # (local)
NPZ_PATH = os.path.join(HERE, "s102_interpretive_dof_ledger.npz")       # (local)
CANON_PATH = os.path.join(ROOT, "computations", "_shared", "canonical_constants.py")  # (local)
ATLAS09_PATH = os.path.join(ROOT, "sessions", "framework", "Atlas", "atlas-09-retractions.md")  # (local)
INV_PATH = os.path.join(ROOT, "sessions", "framework", "registry", "falsifier-master-inventory.md")  # (local)

GATE_ID = "W5-5-S102-INTERPRETIVE-DOF-LEDGER"  # (local)
SCHEME = "N/A-ledger-assembly"                  # (local)
CONVENTION = "INTERPRETIVE-DOF-LEDGER-CONSOLIDATED"  # (local)
LMAX = "N/A"                                     # (local)


def sha256_file(path):  # (local)
    if not os.path.exists(path):
        return "ABSENT-" + "0" * 56
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def sha256_text(text):  # (local)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# =====================================================================================
#  The FOUR referee-M2 rescopings. Each carries the load-bearing binding-test column.
#  Values are CROSS-REFERENCED from pinned canonical constants / register rows, NOT re-derived.
# =====================================================================================

# q-median for SF54 binding test: read from the S100a SF54-mapping npz (the LRD re-scope output).
# Cited as a cross-reference (NOT hardcoded as a framework constant; it is an upstream gate output).
q_substrate_median = None  # (local)
sf54_band = None           # (local)
frame_ratio_median = None  # (local)
accel_frac = None          # (local)
sf54_npz = os.path.join(HERE, "..", "session-100a", "s100a_w1_sf54_mapping.npz")  # (local)
sf54_src = "S100a-W1-1-SF54-MAPPING (s100a_w1_sf54_mapping.npz)"  # (local)
sf54_audit = "f41bdf1fc80562daabe09784a1dee0d9e93e0bb3a549dcdd061f5d6b1e290002"  # (local)
if os.path.exists(sf54_npz):
    _d = np.load(sf54_npz, allow_pickle=True)  # (local)
    q_substrate_median = float(_d["q_corrected_median"])      # -0.8661659540367223
    sf54_band = (float(_d["sf54_band_lo"]), float(_d["sf54_band_hi"]))  # (-0.97, 0.81)
    frame_ratio_median = float(_d["frame_ratio_median"])      # ~26.10x  (conformal-frame)
    accel_frac = float(_d["accel_frac_corr"])                 # 0.6677  (q<0 fraction post-fold)

# alpha_s scalar-transport tension (the moment-identity reading, now relocated off-pivot)
alpha_s_planck_sigma_scalar_transport = -12.146  # (local)  Planck-2018 alpha_s = -0.0045 +/- 0.0067
alpha_s_pivot_sigma_matched = 0.67               # (local)  matched pivot channel: +0.67sigma consistent

# CGWB binding-test channels (the LSS replacement for the retired GW-detector flagship)
bao_ring_snr_desi5yr = 8.6341   # (local)  Row #72 first-sound ring SNR DESI-5yr
cgwb_fpeak_decades_above_detectors = 28.929  # (local)  S98 gate: +28.9 decades above HF ceiling

# w_0 binding-test: DESI DR3 binary containment in R_842 rectangle
w0_branch_iv = -0.842454        # (local)  branch-(iv) SECONDARY (R_842 center); PRIMARY = w0_FW = -0.918
R_842_w0_window = (-0.942, -0.742)  # (local)  R_842 = [-0.942,-0.742] x [-0.2,0.2]

rescopings = [
    {
        "id": 1,
        "name": "alpha_s transport-degree (scale-and-channel separation)",
        "tension": (
            "Single-Planck-pivot comparison gave alpha_s^substrate = -0.08587279 vs Planck-2018 "
            "(-0.0045 +/- 0.0067) = -12.146 sigma — read as a 'first multi-sigma falsifier' (12.15 sigma "
            "Planck-18 / 13.99 sigma Aiola-2020). The substrate value was being compared against the "
            "WRONG datum (a BZ-scale O(M_KK) running put up against the CMB pivot)."
        ),
        "rescoping": (
            "SCALE-AND-CHANNEL re-scope (S92 AH-TR-1 -> S93 W7-1): the framework carries TWO scale-"
            "separated alpha_s observables, not one — a substrate-distance running (alpha_s_substrate_"
            "distance_1 = %.8f, inside the BZ, s=3 Mellin pole) and a Goldstone-pivot running "
            "(alpha_s_pivot_goldstone = %.1f, CMB pivot). WHICH a detector measures is set by the "
            "single computable transport degree deg(T_BZ->pivot). S93 W7-1 RESOLVED deg=+2 NON-SCALAR "
            "(w(L_max).kappa(k) factorization_holds=False) => the scalar-transport (-12.146 sigma) reading "
            "is the FALSIFIED leaf; it RELOCATES off-pivot as a SCALE-MISMATCH (NOT a falsification). "
            "Matched channels: pivot image ~0 vs Planck = +0.67 sigma (consistent)."
            % (alpha_s_substrate_distance_1, alpha_s_pivot_goldstone)
        ),
        "atlas09_item": "Item 36 (eps_H Spectral Functional Crisis) — NEAREST anchor",
        "atlas09_status": "PENDING-formal-row",
        "atlas09_note": (
            "Item 36 records the n_s/alpha_s SCHEME-dependence family (eps_H sign-flip across cutoffs; "
            "the functional-class-conditional reading). The transport-degree rescoping is a DISTINCT, "
            "FINER claim (a scale/channel separation set by deg(T)=+2, not a cutoff-family ambiguity); "
            "its formal atlas-09 CORRECTION row is PENDING. Register-of-record: "
            "falsifier-master-inventory.md Row #3.rescope-AH-TR-1 (CLOSED-NON-SCALAR-TRANSPORT-RESOLVED) "
            "+ canonical_constants alpha_s_substrate_distance_1 / alpha_s_pivot_goldstone + "
            "cross-pillar-bridge-corpus.md section 23 (SCALE-AND-CHANNEL-TAGGING, alpha_s = instance 2)."
        ),
        "binding_test": (
            "CMB-S4 (2030, sigma_alpha_s ~ 2.3e-3 => ~37 sigma reach) / CMB-HD (2035, sigma_alpha_s ~ 1.1e-3 "
            "=> ~78 sigma reach) measurement of the SUBSTRATE-SENSITIVITY channel: the substrate-distance "
            "running alpha_s^substrate = %.8f is a falsifiable ~34-sigma-class discriminator there. The "
            "-12.146 sigma did NOT vanish — it MOVED to the matched substrate-sensitivity channel as a "
            "live ~34-sigma prediction (a strength, per feedback_reporting-framing.md, NOT defined out of "
            "existence). The pivot leaf (alpha_s ~ 0, +0.67 sigma) is the matched Planck-channel reading."
            % alpha_s_substrate_distance_1
        ),
        "binding_test_status": "POPULATED",
        "binding_instrument": "CMB-S4 2030 / CMB-HD 2035 (substrate-sensitivity channel)",
        "binding_anchor_audit": "S93-W7-1 deg(T)=+2 (line 155); inventory Row #3.rescope-AH-TR-1",
    },
    {
        "id": 2,
        "name": "SF54 deceleration band",
        "tension": (
            "The SCALE-FACTOR-54 gate carried a deceleration band q: -0.97 -> +0.81 (Connes-distance "
            "proxy). The substrate q(z) did NOT reproduce the SF54 band: S96-W1-VOLOVIK-2FLUID FAIL "
            "(band not reproduced; q_min_volovik = -0.1115, upper edge unreachable). Apparent failure "
            "to match the SF54 deceleration-acceleration trajectory."
        ),
        "rescoping": (
            "Frame-robust re-scope (S100a LRD re-scope, S100a-W1-1-SF54-MAPPING): q is a LOG-DERIVATIVE "
            "frame-INVARIANT (Spearman rho = 1.0 between bare and corrected q). The S99/S96 band-MISS is "
            "FRAME-ROBUST — SF54 is simply the WRONG conformal frame (frame_ratio_median ~ %.1fx faster "
            "Connes-distance frame). The substrate is MOSTLY-ACCELERATING post-fold (q<0 fraction = %.4f). "
            "SF54 axis is CLOSED frame-robust; the surviving cosmic-time route (C1) is the KV back-"
            "reaction channel (CF-S101-W1-QEQ), NOT the SF54 band."
            % (frame_ratio_median if frame_ratio_median is not None else float("nan"),
               accel_frac if accel_frac is not None else float("nan"))
        ),
        "atlas09_item": "atlas-08-freshness-S100 Q13 (tau-evolution -> cosmic time / C1)",
        "atlas09_status": "PENDING-formal-row",
        "atlas09_note": (
            "The SF54 frame-robust closure is an S100a-era rescoping recorded in atlas-08-freshness-S100 "
            "(Q13: 'SF54 axis CLOSED frame-robust (wrong band, different conformal frame ~26x faster); "
            "C1 stays ASSUMED'). It is NOT yet a formal atlas-09 CORRECTION row (atlas-09 scope ends at "
            "S88). Register-of-record: atlas-08-freshness-S100 Q13 + gate S100a-W1-1-SF54-MAPPING + "
            "little-red-dots-synthesis.md (SCALE-FACTOR-54 deceleration band)."
        ),
        "binding_test": (
            "The substrate q(z) itself: median q = %.4f (S100a SF54-mapping npz; band [%.2f, %.2f]); the "
            "substrate is mostly-accelerating post-fold (q<0 fraction %.4f). Because q is a frame-INVARIANT "
            "log-derivative, ANY observational reconstruction of the late-time deceleration parameter q(z) "
            "(DESI/Euclid expansion history; SNIa Hubble-flow) BINDS the substrate prediction directly — "
            "frame choice cannot rescue a band-miss. The forward C1 (tau -> cosmic time) closure routes "
            "through the KV back-reaction channel, whose q(z) image is the binding observable."
            % (q_substrate_median if q_substrate_median is not None else float("nan"),
               sf54_band[0] if sf54_band else float("nan"),
               sf54_band[1] if sf54_band else float("nan"),
               accel_frac if accel_frac is not None else float("nan"))
        ),
        "binding_test_status": "POPULATED",
        "binding_instrument": "DESI/Euclid expansion-history q(z) + SNIa Hubble-flow (frame-invariant)",
        "binding_anchor_audit": sf54_audit + " (" + sf54_src + ")",
    },
    {
        "id": 3,
        "name": "CGWB retired-to-different-instrument (GW -> LSS migration)",
        "tension": (
            "The CGWB was the flagship LISA discriminator (acoustic vs Companion-null). But the acoustic "
            "peak FREQUENCY evaporates to GHz+: S96-OBS-CGWB-PEAK-FREQ FAIL (f_obs = 8.4835e39 Hz, +28.9 "
            "decades above the optimistic HF-detector ceiling, +42.45 decades above LISA). The CGWB peak "
            "is a member of NO GW-detector band (PTA / LISA / LIGO-ET / resonant-HF) — GW-detector-sterile."
        ),
        "rescoping": (
            "GW -> LSS migration (S96 W8-2 / S97 re-pin): the falsifier does NOT vanish; it RELOCATES to "
            "the correct instrument. The substrate has ONE frequency scale (M_KK); the fold radiates at it "
            "(~1e40 Hz, above every GW detector); the acoustic IMPRINT lives at the matter-clustering scale "
            "(k1 = 0.0193 Mpc^-1) where galaxy surveys operate. The GW-detector flagship is RETIRED; the "
            "surviving structural companions (wall=0 null; (A)/(C) regulator-class split 47.081 OOM) are "
            "NON-detector-testable STRUCTURAL-ORTHOGONAL-COMPANIONS, never co-primary."
        ),
        "atlas09_item": "falsifier-master-inventory Row #7.audit-3 (GW->LSS migration) + capstone section 7.2",
        "atlas09_status": "PENDING-formal-row",
        "atlas09_note": (
            "The GW-detector-flagship retirement is an S96/S97-era rescoping recorded in falsifier-master-"
            "inventory Row #7.audit-2/audit-3 + capstone section 7.2 (the GW-detector-flagship-retirement "
            "note). It is NOT yet a formal atlas-09 CORRECTION row (atlas-09 scope ends at S88; the project "
            "memory explicitly flags 'No retirement; no D09 needed' for the ACOUSTIC (A)-class Omega_GW, "
            "which stays LIVE — it is the GW-DETECTOR FREQUENCY/peak that migrated, NOT the acoustic "
            "signal). Register-of-record: inventory Row #7.audit-3 + gate S96-OBS-CGWB-PEAK-FREQ + "
            "S98-KAPPA-INDEP-FROM-CGWB-FREQ."
        ),
        "binding_test": (
            "The LIVE near-term zero-parameter acoustic falsifiers at the LSS instrument (the GW flagship's "
            "replacement): (P4) First-sound BAO ring — inventory Row #72 (S96-OBS-FIRST-SOUND-RING PASS), "
            "A_FS = %.6f = c2^2/c1^2 at k1 = 0.0193150 Mpc^-1 (r1 = 325.30 Mpc), SNR %.4f DESI-5yr / 5.0789 "
            "DESI-DR1, NO LCDM counterpart — a DESI/Euclid P(k) measurement; (P5) f.sigma_8 growth "
            "suppression — inventory Row #71 (S96-OBS-FSIGMA8-FORECAST INFO), product_supp_max = -4.058%% "
            "@ z=0.51, S8-relieving, sigma_DESI5yr = 1.013. The GW peak FREQUENCY axis is detector-sterile "
            "(+28.9 decades out-of-band) and is NOT the binding test; the BAO ring + f.sigma_8 are."
            % (A_FS_first_sound_ring, bao_ring_snr_desi5yr)
        ),
        "binding_test_status": "POPULATED",
        "binding_instrument": "DESI/Euclid P(k) — first-sound BAO ring (Row #72) + f.sigma_8 (Row #71)",
        "binding_anchor_audit": "Row #72 b74ccd56...955c (SNR 8.6341); Row #71 S96-OBS-FSIGMA8-FORECAST",
    },
    {
        "id": 4,
        "name": "w_0 R_918 -> R_842 falsifier-rectangle migration",
        "tension": (
            "The R_918 = [-1.05,-0.85] x [-0.2,+0.2] DESI w_0-w_a falsifier rectangle was SELF-FALSIFYING "
            "under the post-S83 branch-(iv) canonical: w_0_pred = -0.842454 fell +0.007546 OUTSIDE the "
            "R_918 upper edge -0.85. The framework's own pre-registered falsifier window excluded its own "
            "branch-(iv) prediction."
        ),
        "rescoping": (
            "Rectangle migration (S84 W1b-9): R_918 -> R_842 = [-0.942,-0.742] x [-0.2,0.2], centered on "
            "-0.842 (nearest half-decimal to -0.842454), half-width PRESERVED at 0.100 in w_0; restores "
            "self-consistency WITHOUT resizing. Dual canonical: PRIMARY w0_FW = %.3f (Volovik partition "
            "four-fold lock, re-confirmed CLEAN S100b W1-4); SECONDARY branch-(iv) = %.6f (R_842 center; "
            "W0-workshop promotion CONDITIONAL on DR3 PASS). [S86 W13-3 cited a STALE R_918 rectangle — a "
            "Class-(c) PIN-DRIFT-FROM-STALE-SOURCE calibration instance.]"
            % (w0_FW, w0_branch_iv)
        ),
        "atlas09_item": "Item 37 (R_918 -> R_842 Rectangle Migration) — RESOLVES CLEANLY",
        "atlas09_status": "RESOLVED",
        "atlas09_note": (
            "This is the ONE rescoping with a clean atlas-09 formal CORRECTION row (Item 37, S84 W1b-9 -> "
            "S86 W13-3). The R_918 historical SHA 7f23a7c6...5c140 is retained as a forward-pointer "
            "reference. Register-of-record: atlas-09 Item 37 + falsifier-master-inventory Row #1 (+ sub-"
            "rows 1.w0-branch-resolution-s100b, 1.w0-branch-iv-evaluator-s101)."
        ),
        "binding_test": (
            "DESI DR3 BINARY CONTAINMENT in R_842 = [%.3f, %.3f] x [-0.2, 0.2] (window OPEN 2026-04-23, "
            "data ~2027): a DR3 (w_0, w_a) central inside R_842 corroborates; outside falsifies. CAVEAT "
            "(branch-(iv) OBJECT STATUS, S102 W5-2): the branch-(iv) evaluator EXISTS but is NOT "
            "truncation-converged (L_max spread 0.130419); the SECONDARY -0.842454 stability is UNVERIFIED "
            "(rho_B(L) derivation-inadmissible post-S86 R_JE retirement, S101 W4-3). PRIMARY w0_FW = %.3f "
            "is the clean binding value; the section-5 DR3 reversal protocol [-0.86,-0.83] stays ARMED "
            "UNMODIFIED. The binding instrument is DESI DR3, NOT DES-SN reanalysis on DR2 BAO."
            % (R_842_w0_window[0], R_842_w0_window[1], w0_FW)
        ),
        "binding_test_status": "POPULATED",
        "binding_instrument": "DESI DR3 2026 / extended SNIa (R_842 binary containment)",
        "binding_anchor_audit": "atlas-09 Item 37; inventory Row #1 e0fcfb4f...4991",
    },
]


# =====================================================================================
#  Verdict logic (pre-registered)
# =====================================================================================
all_binding_populated = all(r["binding_test_status"] == "POPULATED" for r in rescopings)  # (local)
all_atlas09_resolve = all(r["atlas09_status"] == "RESOLVED" for r in rescopings)           # (local)
any_binding_open = any(r["binding_test_status"] == "OPEN-no-binding-test-yet" for r in rescopings)  # (local)
n_pending = sum(1 for r in rescopings if r["atlas09_status"] == "PENDING-formal-row")       # (local)
n_resolved = sum(1 for r in rescopings if r["atlas09_status"] == "RESOLVED")                # (local)

if any_binding_open or any(not r["binding_test"].strip() for r in rescopings):
    VERDICT = "FAIL"  # (local)  a binding-test entry has no identifiable NEW test
elif all_binding_populated and all_atlas09_resolve:
    VERDICT = "PASS"  # (local)  all 4 rows fully assembled with resolving atlas-09 refs
else:
    VERDICT = "INFO"  # (local)  every binding test populated; >=1 atlas-09 formal-row PENDING

value_payload = (
    "n_rescopings=%d;binding_populated=%d/4;atlas09_resolved=%d/4;atlas09_pending_formal_row=%d/4;"
    "rows=[alpha_s-transport-deg+2,SF54-q-median%.4f,CGWB-GW-to-LSS,w0-R918->R842];"
    "binding_tests=[CMB-S4/HD-alpha_s-substrate%.8f,substrate-q(z)-median%.4f-vs-SF54,"
    "BAO-ring-SNR%.4f+f.sigma_8,DESI-DR3-R842-containment];ledger=interpretive-dof-ledger.md"
) % (
    len(rescopings),
    sum(1 for r in rescopings if r["binding_test_status"] == "POPULATED"),
    n_resolved, n_pending,
    q_substrate_median if q_substrate_median is not None else float("nan"),
    alpha_s_substrate_distance_1,
    q_substrate_median if q_substrate_median is not None else float("nan"),
    bao_ring_snr_desi5yr,
)


# =====================================================================================
#  Build the consolidated ledger markdown
# =====================================================================================
def build_ledger_text():  # (local)
    now = datetime.datetime.now().strftime("%Y-%m-%d")  # (local)
    L = []  # (local)
    L.append("# Interpretive-DOF Ledger — The Framework's Post-Hoc Rescopings and Their Forward Binding Tests")
    L.append("")
    L.append("ingested-by: /weave --update")
    L.append("")
    L.append("**Sole writer**: `mack-cosmic-bridge` (falsifier/observable surface, per `feedback_mack-bridge-role.md`).")
    L.append("**Produced by**: gate `%s` (Session 102, Wave 5, item 25), `%s` on %s." % (GATE_ID, os.path.basename(__file__), now))
    L.append("**Companion to**: the falsifier-surface freeze (S102 item 24). Together they pin BOTH what the framework predicts")
    L.append("AND how its past rescopings remain falsifiable.")
    L.append("")
    L.append("## Purpose (scientific integrity, substrate-first)")
    L.append("")
    L.append("A *rescoping* is a post-hoc reinterpretation of a tension (a relocation of the claim, a scale/channel")
    L.append("re-tag, an instrument migration, a falsifier-window move). A rescoping is **scientifically legitimate")
    L.append("only if the rescoped claim is STILL falsifiable** — it must point FORWARD to a test, not backward to a")
    L.append("salvaged result. This is the substrate-first discipline applied to the framework's OWN interpretive")
    L.append("history. Per `feedback_reporting-framing.md`: a model's *flexibility* to absorb any datum is")
    L.append("**unfalsifiability, NOT strength** (the inflation lesson). The load-bearing column below is therefore")
    L.append("the **binding test** — the NEW test that NOW BINDS each rescoped claim. A rescoping without a binding")
    L.append("test is unfalsifiable bookkeeping and is flagged `OPEN-no-binding-test-yet` (cross-ref `evoi-framework.md`")
    L.append("section 6 standing-gap ledger), never left blank.")
    L.append("")
    L.append("Substrate framing (NON-PHONONIC, register-maintenance): this ledger does NOT compute a substrate")
    L.append("observable. It CROSS-REFERENCES four existing rescopings and ADDS the binding-test column citing")
    L.append("ALREADY-PINNED values. Each binding-test value carries its own upstream substitution chain in its")
    L.append("originating gate; the ledger ASSEMBLES, it does not re-derive. Every binding test points FORWARD")
    L.append("(`D_K spectrum -> emergent observable -> measurement`), preserving the substrate-IS direction.")
    L.append("")
    L.append("## atlas-09 cross-reference reconciliation (on-disk state, this session)")
    L.append("")
    L.append("`atlas-09-retractions.md` is 214 lines, 46 items, scope **Sessions 1-88** (git-unmodified this session).")
    L.append("Of the four rescopings, only **Item 37** (w_0 R_918->R_842) is a clean atlas-09 formal CORRECTION row.")
    L.append("**Item 36** (eps_H Spectral Functional Crisis) is the NEAREST atlas-09 anchor for the alpha_s SCHEME-")
    L.append("dependence family, but the finer **transport-degree** rescoping (S92->S93 deg(T)=+2 NON-SCALAR) is a")
    L.append("DISTINCT claim whose formal atlas-09 row is PENDING. The **SF54** and **CGWB** rescopings are S96/S100a-")
    L.append("era; they live in `atlas-08-freshness-S100` + `falsifier-master-inventory.md` and their formal atlas-09")
    L.append("rows are PENDING (atlas-09's scope ends at S88). Per `feedback_fix-in-session-never-defer.md`, each")
    L.append("PENDING row below names its NEAREST-resolving atlas-09 anchor AND its register-of-record, rather than")
    L.append("claiming a cross-reference that does not resolve. **Verdict: INFO** — every binding test is POPULATED")
    L.append("(not FAIL); the atlas-09 FORMAL-row cross-reference is partial (%d/4 resolved, %d/4 PENDING-formal-row)." % (n_resolved, n_pending))
    L.append("")
    L.append("**Carry-forward (genuine future register-maintenance, 4-field):** author the three PENDING formal")
    L.append("atlas-09 rows — *what*: add atlas-09 CORRECTION rows for (i) alpha_s transport-degree separation,")
    L.append("(ii) SF54 frame-robust closure, (iii) CGWB GW->LSS migration; *inputs*: this ledger + the named")
    L.append("registers-of-record; *gate*: atlas-09 row-existence + cross-ref resolve; *effort*: <1 wave (atlas")
    L.append("editor, register-maintenance). Until authored, the register-of-record citations below ARE the")
    L.append("authoritative cross-references.")
    L.append("")
    L.append("## Consolidated Table")
    L.append("")
    L.append("| # | Rescoping | Original tension | Rescoping move | atlas-09 item (status) | **NEW binding test** | Binding instrument |")
    L.append("|:-:|:----------|:-----------------|:---------------|:-----------------------|:---------------------|:-------------------|")
    for r in rescopings:
        atlas_cell = "%s — **%s**" % (r["atlas09_item"], r["atlas09_status"])  # (local)
        row = "| %d | %s | %s | %s | %s | **[%s]** %s | %s |" % (
            r["id"],
            r["name"],
            r["tension"].replace("\n", " ").replace("|", "\\|"),
            r["rescoping"].replace("\n", " ").replace("|", "\\|"),
            atlas_cell.replace("|", "\\|"),
            r["binding_test_status"],
            r["binding_test"].replace("\n", " ").replace("|", "\\|"),
            r["binding_instrument"].replace("|", "\\|"),
        )  # (local)
        L.append(row)
    L.append("")
    L.append("## Per-row detail (atlas-09 cross-reference notes + binding-test anchors)")
    L.append("")
    for r in rescopings:
        L.append("### Rescoping %d — %s" % (r["id"], r["name"]))
        L.append("")
        L.append("- **Original tension**: %s" % r["tension"].replace("\n", " "))
        L.append("- **Rescoping move**: %s" % r["rescoping"].replace("\n", " "))
        L.append("- **atlas-09 cross-reference**: %s (**%s**). %s" % (r["atlas09_item"], r["atlas09_status"], r["atlas09_note"].replace("\n", " ")))
        L.append("- **NEW binding test** [%s]: %s" % (r["binding_test_status"], r["binding_test"].replace("\n", " ")))
        L.append("- **Binding instrument**: %s" % r["binding_instrument"])
        L.append("- **Binding-test anchor (audit)**: %s" % r["binding_anchor_audit"])
        L.append("")
    L.append("## Cited pinned values (cross-references; NOT re-derived here)")
    L.append("")
    L.append("| Quantity | Value | Source |")
    L.append("|:---------|:------|:-------|")
    L.append("| `alpha_s_substrate_distance_1` | %.8f | canonical_constants (S92 AH-TR-1; substrate/BZ leaf) |" % alpha_s_substrate_distance_1)
    L.append("| `alpha_s_pivot_goldstone` | %.1f | canonical_constants (S92; CMB-pivot leaf, +0.67 sigma) |" % alpha_s_pivot_goldstone)
    L.append("| substrate q(z) median | %s | S100a-W1-1-SF54-MAPPING npz (`q_corrected_median`) |" % (("%.6f" % q_substrate_median) if q_substrate_median is not None else "N/A"))
    L.append("| SF54 band | [%s, %s] | S100a-W1-1-SF54-MAPPING npz |" % ((("%.2f" % sf54_band[0]) if sf54_band else "N/A"), (("%.2f" % sf54_band[1]) if sf54_band else "N/A")))
    L.append("| conformal-frame ratio (median) | %s | S100a-W1-1-SF54-MAPPING npz (~26x faster CD frame) |" % (("%.3f" % frame_ratio_median) if frame_ratio_median is not None else "N/A"))
    L.append("| `A_FS_first_sound_ring` | %.6f | canonical_constants (S96; BAO ring amplitude c2^2/c1^2) |" % A_FS_first_sound_ring)
    L.append("| first-sound ring SNR (DESI-5yr) | %.4f | inventory Row #72 (S96-OBS-FIRST-SOUND-RING) |" % bao_ring_snr_desi5yr)
    L.append("| `w0_FW` (PRIMARY) | %.3f | canonical_constants (S58 Volovik four-fold lock) |" % w0_FW)
    L.append("| branch-(iv) w_0 (SECONDARY) | %.6f | R_842 center; truncation-UNVERIFIED (S101 W4-3) |" % w0_branch_iv)
    L.append("")
    L.append("## Verdict")
    L.append("")
    L.append("`%s`: **%s** — %s" % (GATE_ID, VERDICT, value_payload))
    L.append("")
    L.append("4 rescopings assembled; binding-test column populated for all 4; %d/4 atlas-09 formal rows resolve" % n_resolved)
    L.append("cleanly (Item 37 / w_0), %d/4 PENDING-formal-row (named register-of-record + nearest atlas-09 anchor)." % n_pending)
    L.append("The interpretive degrees of freedom the framework has used are now in ONE auditable place with their")
    L.append("forward falsification routes.")
    L.append("")
    return "\n".join(L) + "\n"


# ---- input-pin map -> dual SHA (audit over script+canonical+pinmap; content over script) ----
script_sha = sha256_file(os.path.abspath(__file__))  # (local)
canon_sha = sha256_file(CANON_PATH)                  # (local)
atlas09_sha = sha256_file(ATLAS09_PATH)              # (local)
inv_sha = sha256_file(INV_PATH)                      # (local)

ledger_text = build_ledger_text()  # (local)

# write the consolidated ledger (single-shot)
with open(LEDGER_PATH, "w", encoding="utf-8") as fh:
    fh.write(ledger_text)

ledger_content_sha = sha256_text(ledger_text)  # (local)

pin_map = {  # (local)  ordered input-pin map
    "gate_id": GATE_ID,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max": LMAX,
    "script_sha256": script_sha,
    "canonical_constants_sha256": canon_sha,
    "atlas09_sha256": atlas09_sha,
    "falsifier_inventory_sha256": inv_sha,
    "ledger_content_sha256": ledger_content_sha,
    "n_rescopings": len(rescopings),
    "verdict": VERDICT,
}
pin_blob = json.dumps(pin_map, sort_keys=True).encode("utf-8")  # (local)
audit_sha256 = hashlib.sha256(pin_blob).hexdigest()             # (local)
content_sha256 = hashlib.sha256(ledger_text.encode("utf-8") + script_sha.encode("utf-8")).hexdigest()  # (local)

# write machine record
np.savez(
    NPZ_PATH,
    n_rescopings=len(rescopings),
    verdict=VERDICT,
    n_atlas09_resolved=n_resolved,
    n_atlas09_pending=n_pending,
    alpha_s_substrate=alpha_s_substrate_distance_1,
    alpha_s_pivot=alpha_s_pivot_goldstone,
    q_substrate_median=(q_substrate_median if q_substrate_median is not None else float("nan")),
    bao_ring_snr=bao_ring_snr_desi5yr,
    w0_FW=w0_FW,
    w0_branch_iv=w0_branch_iv,
    audit_sha256=audit_sha256,
    content_sha256=content_sha256,
    gate_id=GATE_ID,
)


def print_verdict_payload():  # (local)  the script PRINTS; the agent calls emit_verdict
    # SHA-pin log (first lines of stdout)
    print("=== INPUT-PIN SHA LOG ===")
    print("script_sha256              =", script_sha)
    print("canonical_constants_sha256 =", canon_sha)
    print("atlas09_sha256             =", atlas09_sha)
    print("falsifier_inventory_sha256 =", inv_sha)
    print("ledger_content_sha256      =", ledger_content_sha)
    print("=========================")
    print()
    print("LEDGER written:", LEDGER_PATH)
    print("NPZ written   :", NPZ_PATH)
    print()
    print("rescopings assembled:", len(rescopings))
    print("  binding-test populated:", sum(1 for r in rescopings if r["binding_test_status"] == "POPULATED"), "/ 4")
    print("  atlas-09 RESOLVED     :", n_resolved, "/ 4")
    print("  atlas-09 PENDING-row  :", n_pending, "/ 4")
    print()
    # the 4-tuple output tag (final non-verdict line per gate-verdicts.md)
    print("OUTPUT-4TUPLE: (value=<see payload>, scheme=%s, convention=%s, L_max=%s)" % (SCHEME, CONVENTION, LMAX))
    print()
    print("=== VERDICT PAYLOAD (call emit_verdict with these) ===")
    payload = {
        "session": 102,
        "gate_id": GATE_ID,
        "verdict": VERDICT,
        "value": value_payload,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": LMAX,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "schema_version": "S84+",
    }
    print(json.dumps(payload, indent=2))
    return payload


if __name__ == "__main__":
    print_verdict_payload()
    sys.exit(0)  # exit 0 regardless of scientific verdict (verdict is data, not exit code)
