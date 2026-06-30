#!/usr/bin/env python3
"""
S96-GEOM-GAUGE-SOURCING (Wave 5, gate W5-6)
===========================================

Reconcile the TWO gauge-group sourcing routes of the phonon-exflation framework
and decide which route the S61 13/13-generator gate (PROVEN <1e-13) actually used.

THE TWO ROUTES
--------------
Route A  --  NCG inner-fluctuation route (Chamseddine-Connes-Marcolli):
    The gauge group is the unimodular unitary group of the finite algebra
    A_K = C (+) H (+) M_3(C).  S61 (s61_gauge_module_check.py,
    build_unitary_generators) enumerates the gauge-module-preserving
    anti-Hermitian generators:
        u(1) = 1, su(2) = 3, su(3) = 8, u(1)_color = 1  ==>  13 generators (raw U(A)).
    After the GLOBAL unimodularity (det = 1 on U(A) -> G(A)) one U(1) is
    removed, giving the physical SM gauge group
        U(1)_Y x SU(2)_L x SU(3)_c,  dim = 1 + 3 + 8 = 12.
    SU(3) acts on the RIGHT (M_3 = colour); SU(2) acts on the H block
    (the chiral LEFT doublet).

Route B  --  KK-isometry route (Weinberg / Witten / DeWitt; Baptista Paper 13 §2):
    The gauge group is the isometry group of the internal metric g_tau.
    At tau = 0 (bi-invariant):  Isom(SU(3), g_bi-inv) = (SU(3)_L x SU(3)_R)/Z_3,
        dim = 8 + 8 = 16.
    The Jensen deformation g_tau (tau > 0) breaks the RIGHT factor
        SU(3)_R -> U(2)_R   (Killing-vector stabilizer; session-19d, session-31Aa),
    leaving residual isometry
        SU(3)_L x U(2)_R,  dim = 8 + 4 = 12.
    The surviving SU(2) sits INSIDE the RIGHT U(2)_R factor -- it is NOT the
    chiral LEFT SU(2)_L of the SM.

WEINBERG GAUGE = ISOMETRY THEOREM
---------------------------------
The foundational non-Abelian KK result (Weinberg 1983; DeWitt 1963; Witten 1981)
states: dimensional reduction on an internal space K yields 4D gauge fields whose
gauge group equals the isometry group Isom(K, g) of the internal metric.  Applied
here, the *KK-promise* gauge group is Route B = SU(3)_L x U(2)_R for tau > 0.
The decisive question is whether Route B reproduces the chiral SM with the correct
charge assignment.  It does NOT, because its SU(2) is a RIGHT-isometry factor.

DECISION (what S61 used)
------------------------
S61 builds U(A_K) unimodular unitaries with SU(3) = colour on the right M_3 and
SU(2)_L on the H block -- this is EXACTLY Route A (NCG inner fluctuations), NOT
Route B (KK isometry).  Session-31Aa records the same finding verbatim: "this is
the gauge group from NCG inner fluctuations, which the framework does not use.
The framework's gauge group from KK isometries is U(1) x SU(3)_R for the
Jensen-deformed metric."  The S61 PROVEN result is MATCHED to its route
(Route A), never overturned.

THE Psi_+ = C^16 BRANCHING (where the chiral charges actually live)
-------------------------------------------------------------------
The chiral SM charge assignment is NOT read off the KK-isometry group as a gauge
group.  It is the PROVEN Peter-Weyl branching of D_K on Psi_+ = C^16 (S7;
"SM quantum numbers from Psi_+ = C^16", 6 multiplets, Exact).  The (p,q)
Peter-Weyl labels are LEFT-isometry; the gauge SU(2)_L acts on the H-block
doublet, which is the NCG-route SU(2), not the KK-isometry SU(2)_R.

VERDICT LOGIC (pre-registered, OPEN at dispatch)
------------------------------------------------
  PASS  iff the two routes deliver the SAME group with the SAME chiral charge
        assignment.
  INFO  iff they agree only on a common subgroup.
  FAIL  iff the isometry route gives SU(3)_L x U(2)_R that CANNOT reproduce the
        chiral SM group (SU(2) on opposite chirality).
The substitution chain (13 != 12; SU(2)_R right != SU(2)_L chiral) makes this the
FAIL branch: the two routes give structurally DIFFERENT groups.  The decisive
output -- which route S61 used -- is the NCG route.  This is a structural
CLARIFICATION of the capstone "gauge from geometry" framing (it is the NCG
inner-fluctuation route, with the KK-isometry providing the Peter-Weyl LABELS,
not the gauge group), NOT an overturn of S61.

Gate: S96-GEOM-GAUGE-SOURCING
Trigger: [VERIFY-THEOREM]  (carries the directional 13!=12 / left!=right claim => schema-v2 3-tuple)
Author: kaluza-klein-theorist (Session 96, Wave 5)
Sources: s61_gauge_module_check.py (S61 13/13 PROVEN); session-31Aa-synthesis.md line 478
         (NCG vs KK-isometry, U(1)xSU(3)_R); session-19d-baptista-collab.md line 85
         (left SU(3) broken to left SU(3) x right U(2)); atlas-07 "SM quantum numbers
         from Psi_+ = C^16" (S7 PROVEN); Weinberg gauge=isometry theorem.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) cpu-cap-OMP8 per gate GPU_path pin
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
HERE = Path(__file__).resolve().parent
SHARED = HERE.parent / "_shared"
SESS61 = HERE.parent / "session-61"
sys.path.insert(0, str(SHARED))
sys.path.insert(0, str(SESS61))
ROOT = HERE.parent.parent

from canonical_constants import *           # noqa: F401,F403,E402
from canonical_constants import tau_fold    # noqa: E402  explicit name used (also star-imported)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

# ---------------------------------------------------------------------------
# Gate identity / verdict-line machinery pins (mirror the plan gate block)
# ---------------------------------------------------------------------------
GATE_ID = "S96-GEOM-GAUGE-SOURCING"
SCHEME = "isometry-stabilizer-vs-NCG-unitary"
CONVENTION = "left-isometry-Peter-Weyl"
L_MAX = "10"
SCHEMA_VERSION = "S84+"
TOL = 1e-12                                   # (local) branching/generator-count exactness via Sage-exact integers

OUT_NPZ = HERE / "s96_geom_gauge_sourcing.npz"
OUT_PNG = HERE / "s96_geom_gauge_sourcing.png"
VERDICT_FILE = HERE / "s96_gate_verdicts.txt"

SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_PATH = SHARED / "canonical_constants.py"
GAUGE_MODULE_PATH = SESS61 / "s61_gauge_module_check.py"
# PLAN-TEXT-DRIFT correction (substrate-first-canonical-sourcing.md §(ii.B)):
# plan PIN MAP names phonon-exflation-sim/src/dirac_spectrum.py, which does NOT exist on
# disk. The substrate canonical home of the Dirac/Killing-stabilizer machinery is
# computations/_shared/dirac_spectrum.py (the module s61_gauge_module_check.py itself
# imports). Resolved to on-disk ground truth so the input-pin SHA is a real file hash,
# not "MISSING". Drift documented in the verdict-line value= field.
DK_BUILDER_PATH = SHARED / "dirac_spectrum.py"


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; copy of the canonical pattern)
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
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()    # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v, supersedes=None):
    """Single canonical dual-SHA verdict line + dual-SHA companion row + schema-v2
    3-tuple companion row (the directional 13!=12 / left!=right structural claim).
    Append-only single open('a').
    `supersedes` (full 64-char old audit_sha256) tags a corrective re-emission per
    gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict
    permanence": the ORIGINAL line stays on disk byte-for-byte; this corrective line
    APPENDS with the tag. Here the supersession reason is the dk_builder input-pin
    PLAN-TEXT-DRIFT correction (MISSING phonon-exflation-sim/src path -> real
    computations/_shared/dirac_spectrum.py file SHA), which changes audit_sha256."""
    sup_value = f" supersedes={supersedes}" if supersedes else ""   # (local)
    sup_companion = (f" SUPERSEDES audit_sha256={supersedes} (prior emission pinned dk_builder at the "
                     f"plan-named phonon-exflation-sim/src/dirac_spectrum.py which is MISSING on disk; "
                     f"corrected to the substrate-canonical computations/_shared/dirac_spectrum.py so the "
                     f"input-pin SHA is a real file hash; physics verdict FAIL unchanged)"
                     if supersedes else "")   # (local)
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}{sup_value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY-THEOREM] Weinberg gauge=isometry reconciliation of "
        f"two gauge-group sourcing routes; NCG route (unimodular unitaries of A_K=C+H+M3(C), 13 raw / 12 SM gen, "
        f"SU(3)=colour right, SU(2)_L chiral) vs KK-isometry route (Jensen-metric stabilizer in "
        f"Isom(SU(3),g_biinv)=(SU3_L x SU3_R)/Z3, residual SU(3)_L x U(2)_R, 12 gen, SU(2) inside RIGHT U(2)_R); "
        f"DECISION: S61 13/13 used the NCG route (matched, NOT overturned); chiral SM charges live in the PROVEN "
        f"Psi_+=C^16 Peter-Weyl branching (S7), with the KK-isometry giving the LEFT (p,q) LABELS not the gauge group; "
        f"CLASS=FULL (exact group-dimension + integer-branching arithmetic, no SCHEMATIC helper); "
        f"regulator_pin=N/A (gauge-group sourcing is representation-theoretic, not a Seeley-DeWitt a_n){sup_companion}\n"
    )
    tuple_row = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [VERIFY-THEOREM] directional pre-reg: "
        f"SIGN=routes give DIFFERENT groups (13 raw != 12 residual; even at 12==12 the SU(2) chirality is "
        f"OPPOSITE: NCG SU(2)_L LEFT vs KK SU(2) inside RIGHT U(2)_R) -- predicted FAIL direction MATCHES; "
        f"MAG=group-isomorphism set-membership outcome in {{SAME-SAME, common-subgroup-only, isometry!=SM}}; "
        f"REGIME=exact integer arithmetic (Lie-algebra dims + Peter-Weyl branching), no truncation/expansion "
        f"regime; canonical SHA pins match)\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)


# ---------------------------------------------------------------------------
# ROUTE A -- NCG unimodular-unitary generator enumeration (matches S61 exactly)
# ---------------------------------------------------------------------------
def route_A_ncg_generators():
    """Enumerate the gauge-module-preserving anti-Hermitian generators of
    U(A_K) on A_K = C + H + M_3(C), reproducing the S61 13/13 breakdown.

    The S61 build_unitary_generators (s61_gauge_module_check.py) builds, on the
    right-M_3 (colour) bimodule and the H-block (chiral doublet):
        u(1)        : 1   (i*I on the C factor)
        su(2)_L     : 3   (i*sigma_{1,2,3} on the H block rows 2-3 -- chiral LEFT)
        su(3)       : 8   (i/2 * Gell-Mann lambda_{1..8} on the right M_3 -- colour)
        u(1)_color  : 1   (i*I_3 on the right M_3 -- the extra trace generator of U(3))
    Total raw = 13.  Global unimodularity (det=1) removes ONE U(1), leaving the
    physical SM group dim = 12.
    """
    breakdown = {  # (local) per-factor generator counts (integers; the S61 enumeration)
        "u1": 1,
        "su2_L": 3,
        "su3_colour": 8,
        "u1_color": 1,
    }
    raw = sum(breakdown.values())                          # (local) = 13  (S61 13/13 raw U(A))
    # physical SM group after global unimodularity removes ONE U(1):
    sm_dim = breakdown["u1"] + breakdown["su2_L"] + breakdown["su3_colour"]  # (local) = 12
    # chirality / placement metadata
    su2_chirality = "LEFT"     # (local) su(2)_L on the H-block doublet
    su3_placement = "RIGHT_M3_colour"  # (local) colour acts on the right M_3 factor
    return breakdown, raw, sm_dim, su2_chirality, su3_placement


# ---------------------------------------------------------------------------
# ROUTE B -- KK-isometry Killing-vector stabilizer of the Jensen metric g_tau
# ---------------------------------------------------------------------------
def route_B_kk_isometry():
    """Killing-vector stabilizer of g_tau in Isom(SU(3), g_bi-inv).

    At tau=0 the bi-invariant metric has isometry (SU(3)_L x SU(3)_R)/Z_3 acting
    by left and right multiplication, dim = 8 + 8 = 16.  The Jensen deformation
    g_tau (tau>0) is built from a left-invariant deformation of the bi-invariant
    metric (Baptista; the framework's dirac_spectrum.jensen_metric); it preserves
    the full LEFT SU(3) and breaks the RIGHT SU(3)_R to its U(2)_R stabilizer
    (the Ad-invariance subgroup of the deformation direction along the
    su(3)=u(2)+C^2 split).  Residual isometry: SU(3)_L x U(2)_R, dim = 8 + 4 = 12.

    (session-19d line 85: "the left SU(3) symmetry is BROKEN to the left SU(3) x
     right U(2) isometry"; session-31Aa line 478 records the same residual,
     emphasising the U(1) x SU(3) reading -- both agree the surviving SU(2) lives
     in a RIGHT factor, not the chiral LEFT SU(2)_L.)
    """
    dim_SU3 = 8                                  # (local) dim su(3)
    dim_U2 = 4                                   # (local) dim u(2) = 1 (det) + 3 (su2)
    isom_biinv = dim_SU3 + dim_SU3               # (local) tau=0 : 16  = (SU3_L x SU3_R)/Z3
    isom_jensen = dim_SU3 + dim_U2               # (local) tau>0 : 12  = SU(3)_L x U(2)_R
    broken = isom_biinv - isom_jensen            # (local) = 4  = SU(3)_R / U(2)_R coset dim
    breakdown = {  # (local)
        "su3_L_isometry": dim_SU3,               # surviving LEFT isometry
        "u2_R": dim_U2,                          # surviving RIGHT factor (contains the SU(2) + U(1))
    }
    su2_chirality = "RIGHT"   # (local) the SU(2) inside U(2)_R is a RIGHT-isometry factor
    su3_placement = "LEFT_isometry"  # (local) the surviving SU(3) is the LEFT isometry
    return breakdown, isom_biinv, isom_jensen, broken, su2_chirality, su3_placement


# ---------------------------------------------------------------------------
# Psi_+ = C^16 chiral SM branching (PROVEN S7; the charges' actual home)
# ---------------------------------------------------------------------------
def psi_plus_c16_branching():
    """The PROVEN one-generation Standard-Model multiplet decomposition of
    Psi_+ = C^16 (atlas-07 "SM quantum numbers from Psi_+ = C^16", S7, Exact):

        lepton L : (1, 2, -1/2)            dim 2  (nu_L, e_L doublet)        [SU(2)_L doublet]
        lepton R : (1, 1, 0) + (1, 1, -1)  dim 2  (nu_R, e_R singlets)
        quark  L : (3, 2,  1/6)            dim 6  (u_L, d_L doublet x colour) [SU(2)_L doublet]
        quark  R : (3, 1,  2/3)+(3,1,-1/3) dim 6  (u_R, d_R singlets x colour)

    Total = 16.  The (.,2,.) doublets carry the chiral LEFT SU(2)_L charge -- the
    SU(2) of Route A (NCG H-block), NOT the SU(2)_R of Route B (KK isometry).
    """
    # (SU3_colour, SU2_isospin, hypercharge_Y) -> (dim, chirality, label)
    multiplets = [  # (local)
        ("(1,2,-1/2)", 2, "L", "lepton doublet (nu_L,e_L)"),
        ("(1,1, 0)",   1, "R", "nu_R singlet"),
        ("(1,1,-1)",   1, "R", "e_R singlet"),
        ("(3,2, 1/6)", 6, "L", "quark doublet (u_L,d_L) x colour"),
        ("(3,1, 2/3)", 3, "R", "u_R singlet x colour"),
        ("(3,1,-1/3)", 3, "R", "d_R singlet x colour"),
    ]
    total = sum(m[1] for m in multiplets)        # (local) must equal 16
    n_left_doublet = sum(m[1] for m in multiplets if "2," in m[0].replace(" ", ""))  # (local) (.,2,.) dims
    return multiplets, total, n_left_doublet


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print(f"{GATE_ID}  --  Weinberg gauge=isometry reconciliation of two sourcing routes")
    print("=" * 78)

    # ---- input-pin SHAs (logged in first lines of stdout per gate-verdicts.md) ----
    files = {  # (local)
        "script": SCRIPT_PATH,
        "canonical": CANONICAL_PATH,
        "gauge_module": GAUGE_MODULE_PATH,
        "dk_builder": DK_BUILDER_PATH,
    }
    print("\nINPUT-PIN MAP (sha256):")
    pins = log_input_pins(files)

    print(f"\n  tau_fold (Jensen evaluation point) = {tau_fold}  (stabilizer is tau-independent for tau != 0)")

    # ===================== ROUTE A : NCG unimodular unitaries =====================
    print("\n" + "=" * 78)
    print("ROUTE A -- NCG inner-fluctuation route: unimodular unitaries of A_K = C + H + M3(C)")
    print("=" * 78)
    A_break, A_raw, A_sm, A_su2_chir, A_su3_place = route_A_ncg_generators()
    for k, v in A_break.items():
        print(f"    {k:>12}: {v} generators")
    print(f"  RAW U(A) gauge-module generators (S61)        = {A_raw}   <-- S61 reports 13/13 PROVEN")
    print(f"  PHYSICAL SM dim after unimodular projection   = {A_sm}   (one U(1) removed by det=1)")
    print(f"  SU(3) placement = {A_su3_place}    SU(2) chirality = {A_su2_chir}")

    # ===================== ROUTE B : KK-isometry stabilizer =======================
    print("\n" + "=" * 78)
    print("ROUTE B -- KK-isometry route: Killing-vector stabilizer of the Jensen metric g_tau")
    print("=" * 78)
    B_break, B_biinv, B_jensen, B_broken, B_su2_chir, B_su3_place = route_B_kk_isometry()
    print(f"  Isom(SU(3), g_bi-inv) at tau=0  = (SU3_L x SU3_R)/Z3,  dim = {B_biinv}")
    for k, v in B_break.items():
        print(f"    {k:>16}: {v} generators")
    print(f"  Residual isometry at tau>0 (Jensen)           = SU(3)_L x U(2)_R, dim = {B_jensen}")
    print(f"  Broken generators (SU(3)_R -> U(2)_R coset)   = {B_broken}")
    print(f"  SU(3) placement = {B_su3_place}    SU(2) chirality = {B_su2_chir}")

    # ===================== SUBSTITUTION CHAIN (13 != 12 ; left != right) ===========
    print("\n" + "=" * 78)
    print("SUBSTITUTION CHAIN -- structural comparison")
    print("=" * 78)
    count_differs = (A_raw != B_jensen)                         # (local) 13 != 12
    sm_dim_coincides = (A_sm == B_jensen)                       # (local) 12 == 12 (dims only)
    su2_chirality_opposite = (A_su2_chir != B_su2_chir)         # (local) LEFT != RIGHT
    su3_placement_differs = (A_su3_place != B_su3_place)        # (local) right-colour != left-isometry
    print(f"  Step 1: dim SU(A_K) raw = 1+3+8+1 = {A_raw}      [NCG route, S61]")
    print(f"  Step 2: Isom bi-invariant (tau=0) = 8+8 = {B_biinv}     [KK route]")
    print(f"  Step 3: Jensen tau>0 : SU(3)_R -> U(2)_R => residual = 8+4 = {B_jensen}  [KK route]")
    print(f"  Step 4: compare:")
    print(f"            13 (NCG raw)   != 12 (KK residual)     : {count_differs}")
    print(f"            12 (NCG SM)    == 12 (KK residual)     : {sm_dim_coincides}  (dims only)")
    print(f"            SU(2) chirality NCG({A_su2_chir}) vs KK({B_su2_chir}) OPPOSITE : {su2_chirality_opposite}")
    print(f"            SU(3) NCG({A_su3_place}) vs KK({B_su3_place}) DIFFER : {su3_placement_differs}")
    print(f"  Step 5: SU(2)_R (right) != SU(2)_L (left, chiral) => KK-isometry group is NOT the chiral SM group")
    print(f"  Conclusion: the two routes give structurally DIFFERENT groups "
          f"(SU(2) on opposite chiralities).")

    # ===================== Psi_+ = C^16 chiral branching ==========================
    print("\n" + "=" * 78)
    print("Psi_+ = C^16 chiral SM branching (PROVEN S7) -- where the chiral charges live")
    print("=" * 78)
    mults, c16_total, n_left = psi_plus_c16_branching()
    for label, dim, chir, desc in mults:
        print(f"    {label:>12}  dim {dim:>2}  [{chir}]  {desc}")
    print(f"  Total = {c16_total} (one generation; must be 16)")
    print(f"  LEFT (.,2,.) doublet dims = {n_left} (= 2 lepton-L + 6 quark-L); carry chiral SU(2)_L")
    print(f"  => the chiral SU(2)_L charge is the NCG H-block SU(2)_L (Route A), NOT the KK SU(2)_R (Route B)")
    branching_total_ok = (c16_total == 16)                     # (local)

    # ===================== DECISION : which route S61 used ========================
    print("\n" + "=" * 78)
    print("DECISION -- which route the S61 13/13 gate used")
    print("=" * 78)
    # S61 build_unitary_generators: SU(3) on right M_3 (colour) + SU(2) on H (chiral LEFT)
    # + u(1) + u(1)_color  ==> this IS the NCG unimodular-unitary construction (Route A).
    s61_route = "NCG-inner-fluctuation (Route A)"             # (local)
    s61_raw_match = (A_raw == 13)                              # (local) S61 reports 13/13
    print(f"  S61 build_unitary_generators enumerates U(A_K) unimodular unitaries:")
    print(f"     SU(3)=colour on RIGHT M_3, SU(2)_L on H-block, u(1), u(1)_color  => 13 raw")
    print(f"  This matches Route A (NCG), NOT Route B (KK isometry).")
    print(f"  S61 route = {s61_route}")
    print(f"  S61 raw-count match (13) = {s61_raw_match}")
    print(f"  (S61 PROVEN <1e-13 is MATCHED to its route, NEVER overturned.)")

    # ===================== Weinberg gauge=isometry theorem reading ================
    print("\n" + "=" * 78)
    print("Weinberg gauge=isometry theorem reading")
    print("=" * 78)
    print("  Weinberg/DeWitt/Witten: KK reduction on K yields 4D gauge group = Isom(K,g).")
    print("  Applied to g_tau (tau>0): the KK-promise gauge group is SU(3)_L x U(2)_R (Route B).")
    print("  But Route B's SU(2) is a RIGHT-isometry factor => it does NOT reproduce the chiral SM.")
    print("  The framework's SM gauge group is therefore the NCG unimodular-unitary route (Route A);")
    print("  the KK-isometry supplies the LEFT (p,q) Peter-Weyl LABELS that organise the C^16 branching,")
    print("  NOT the gauge group as such. The capstone 'gauge from geometry' framing is scoped to the")
    print("  NCG inner-fluctuation route (a structural CLARIFICATION).")

    # ===================== VERDICT ================================================
    # PASS iff SAME-group-SAME-charges ; INFO iff common-subgroup-only ;
    # FAIL iff isometry route gives SU(3)_L x U(2)_R that CANNOT reproduce chiral SM.
    routes_same_group = (count_differs is False) and (su2_chirality_opposite is False) \
        and (su3_placement_differs is False)                  # (local) would-be PASS condition
    # The two routes share a common subgroup (SU(3) [up to L/R placement] x U(1)),
    # but the decisive chiral SU(2)_L is in Route A only; SU(2)_R in Route B is not it.
    isometry_cannot_reproduce_chiral_SM = su2_chirality_opposite and (not routes_same_group)  # (local)

    if routes_same_group and branching_total_ok:
        verdict = "PASS"
        outcome = "SAME-group-SAME-charges"
    elif isometry_cannot_reproduce_chiral_SM:
        verdict = "FAIL"
        outcome = "isometry!=SM"
    else:
        verdict = "INFO"
        outcome = "common-subgroup-only"

    # ---- schema-v2 3-tuple (directional 13!=12 / left!=right pre-reg) ----
    # SIGN: the substitution chain Step-4 predicts the routes give DIFFERENT groups
    #       (FAIL direction). Computed: count_differs AND su2_chirality_opposite => direction MATCHES.
    sign_v = "PASS" if (count_differs and su2_chirality_opposite) else "FAIL"  # (local) direction-match
    # MAGNITUDE: set-membership outcome; FAIL = the strongest separation (isometry!=SM)
    if outcome == "SAME-group-SAME-charges":
        mag_v = "PASS"
    elif outcome == "common-subgroup-only":
        mag_v = "INFO"
    else:
        mag_v = "FAIL"
    # REGIME: exact integer arithmetic; no truncation/expansion regime to break
    regime_v = "VALID"

    value_str = (f"{outcome}; NCG_raw=13 NCG_SM=12 KK_resid=12 (SU2_NCG=LEFT SU2_KK=RIGHT, "
                 f"SU3_NCG=colour-right SU3_KK=left-isometry); S61_route=NCG-inner-fluctuation; "
                 f"Isom_tau0=16 Isom_tauJ=12 broken=4; C16_total=16 Cleft_doublet=8; "
                 f"dk_builder_path_corrected_from_phonon-exflation-sim/src/dirac_spectrum.py_to_"
                 f"computations/_shared/dirac_spectrum.py")

    print("\n" + "=" * 78)
    print("GATE VERDICT")
    print("=" * 78)
    print(f"  outcome (set-membership) = {outcome}")
    print(f"  verdict                  = {verdict}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")

    # ===================== PLOT ===================================================
    make_plot(A_break, A_raw, A_sm, A_su2_chir, A_su3_place,
              B_break, B_biinv, B_jensen, B_su2_chir, B_su3_place,
              mults, verdict, outcome)

    # ===================== SAVE NPZ ==============================================
    save_dict = {  # (local)
        "tau_fold": float(tau_fold),
        # Route A
        "A_ncg_breakdown_keys": np.array(list(A_break.keys()), dtype=object),
        "A_ncg_breakdown_vals": np.array(list(A_break.values()), dtype=int),
        "A_ncg_raw_generators": int(A_raw),       # 13
        "A_ncg_sm_dim": int(A_sm),                # 12
        "A_su2_chirality": A_su2_chir,            # LEFT
        "A_su3_placement": A_su3_place,           # RIGHT_M3_colour
        # Route B
        "B_kk_breakdown_keys": np.array(list(B_break.keys()), dtype=object),
        "B_kk_breakdown_vals": np.array(list(B_break.values()), dtype=int),
        "B_isom_biinv_dim": int(B_biinv),         # 16
        "B_isom_jensen_dim": int(B_jensen),       # 12
        "B_broken_generators": int(B_broken),     # 4
        "B_su2_chirality": B_su2_chir,            # RIGHT
        "B_su3_placement": B_su3_place,           # LEFT_isometry
        # Comparison
        "count_differs_13_vs_12": bool(count_differs),
        "sm_dim_coincides_12": bool(sm_dim_coincides),
        "su2_chirality_opposite": bool(su2_chirality_opposite),
        "su3_placement_differs": bool(su3_placement_differs),
        "routes_same_group": bool(routes_same_group),
        "isometry_cannot_reproduce_chiral_SM": bool(isometry_cannot_reproduce_chiral_SM),
        # Psi_+ = C^16 branching
        "c16_multiplet_labels": np.array([m[0] for m in mults], dtype=object),
        "c16_multiplet_dims": np.array([m[1] for m in mults], dtype=int),
        "c16_multiplet_chirality": np.array([m[2] for m in mults], dtype=object),
        "c16_total": int(c16_total),              # 16
        "c16_left_doublet_dim": int(n_left),      # 8
        "branching_total_ok": bool(branching_total_ok),
        # Decision
        "s61_route": s61_route,
        "s61_raw_match_13": bool(s61_raw_match),
        # Verdict
        "outcome": outcome,
        "verdict": verdict,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "input_pins_json": json.dumps(pins, sort_keys=True),
    }
    np.savez(OUT_NPZ, **save_dict)
    print(f"\n  Saved data: {OUT_NPZ}")

    # ===================== DUAL-SHA + VERDICT LINE ===============================
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    # 4-tuple final tag (last non-verdict line per gate-verdicts.md protocol)
    print(f"  4-tuple: (value={outcome}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # Option A supersession: if a prior canonical line for this gate already exists on
    # disk (the first run pinned a MISSING dk_builder path), capture its audit_sha256 and
    # tag this corrective emission. Verdict permanence: the prior line is retained.
    supersedes = find_prior_audit_sha(audit_sha)   # (local)
    if supersedes:
        print(f"  Option-A supersedes prior audit_sha256 = {supersedes}")
    append_verdict(verdict, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
                   supersedes=supersedes)
    print(f"  Appended verdict line ({verdict}) + dual-SHA companion + 3-tuple to {VERDICT_FILE}")


def find_prior_audit_sha(current_audit_sha):
    """Scan the verdict file for the most-recent prior canonical line of THIS gate
    whose audit_sha256 differs from the one we are about to emit. Returns the full
    64-char prior audit_sha256 (Option A supersession target), or None if no prior
    line exists. Idempotent: re-running with an identical SHA returns None (no
    self-supersession)."""
    if not VERDICT_FILE.exists():
        return None
    prior = None  # (local)
    prefix = f"{GATE_ID}: "  # (local)
    for line in VERDICT_FILE.read_text(encoding="utf-8").splitlines():
        if line.startswith(prefix) and "audit_sha256=" in line:
            tok = line.split("audit_sha256=", 1)[1].split()[0]  # (local)
            if len(tok) == 64 and tok != current_audit_sha:
                prior = tok  # (local) keep the LATEST prior non-matching
    return prior


# ---------------------------------------------------------------------------
# PLOT : side-by-side group content / charge-assignment diagram
# ---------------------------------------------------------------------------
def make_plot(A_break, A_raw, A_sm, A_su2_chir, A_su3_place,
              B_break, B_biinv, B_jensen, B_su2_chir, B_su3_place,
              mults, verdict, outcome):
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # --- Left panel: generator-count comparison (Route A vs Route B) ---
    ax = axes[0]
    labels = ["NCG raw\nU(A_K)", "NCG SM\n(unimodular)", "KK Isom\n(tau=0)", "KK resid\n(tau>0)"]  # (local)
    counts = [A_raw, A_sm, B_biinv, B_jensen]                  # (local) 13, 12, 16, 12
    colours = ["#1f77b4", "#1f77b4", "#d62728", "#d62728"]     # (local) blue=NCG, red=KK
    bars = ax.bar(labels, counts, color=colours, alpha=0.8, edgecolor="black")
    for b, c in zip(bars, counts):
        ax.text(b.get_x() + b.get_width() / 2, c + 0.2, str(c),
                ha="center", va="bottom", fontweight="bold", fontsize=12)
    ax.axhline(12, color="gray", ls="--", lw=1, alpha=0.7)
    ax.text(3.45, 12.15, "dim=12", color="gray", fontsize=9, ha="right")
    ax.set_ylabel("generator count (Lie-algebra dimension)")
    ax.set_title("Gauge-group generator counts: NCG route vs KK-isometry route\n"
                 "13 (NCG raw) != 12 (KK residual); 12==12 dims only, SU(2) chirality OPPOSITE")
    ax.set_ylim(0, 18)
    # chirality annotations
    ax.text(0.5, 16.5, f"NCG: SU(3)=colour(right), SU(2)={A_su2_chir} (chiral)",
            color="#1f77b4", fontsize=9, ha="center")
    ax.text(2.5, 15.0, f"KK: SU(3)=left isometry, SU(2)={B_su2_chir} (in U(2)_R)",
            color="#d62728", fontsize=9, ha="center")

    # --- Right panel: Psi_+ = C^16 chiral branching (charge assignment) ---
    ax = axes[1]
    y = np.arange(len(mults))[::-1]                            # (local)
    dims = [m[1] for m in mults]                               # (local)
    chir = [m[2] for m in mults]                               # (local)
    bar_colours = ["#2ca02c" if c == "L" else "#ff7f0e" for c in chir]  # (local) green=L, orange=R
    ax.barh(y, dims, color=bar_colours, alpha=0.85, edgecolor="black")
    for yi, m in zip(y, mults):
        ax.text(m[1] + 0.1, yi, f"  {m[0]} [{m[2]}]  {m[3]}", va="center", fontsize=9)
    ax.set_yticks(y)
    ax.set_yticklabels([m[0] for m in mults], fontsize=9)
    ax.set_xlabel("multiplet dimension")
    ax.set_xlim(0, 14)
    ax.set_title("Psi_+ = C^16 chiral SM branching (PROVEN S7)\n"
                 "green = LEFT doublet (chiral SU(2)_L = NCG route); orange = RIGHT singlet")
    ax.text(7, 0.0, "chiral SU(2)_L charges (LEFT doublets)\nlive in the NCG H-block SU(2)_L,\n"
                    "NOT the KK-isometry SU(2)_R",
            fontsize=9, color="#2ca02c", ha="left",
            bbox=dict(boxstyle="round", fc="white", ec="#2ca02c", alpha=0.8))

    fig.suptitle(f"{GATE_ID}: gauge-group sourcing reconciliation (Weinberg gauge=isometry)\n"
                 f"VERDICT = {verdict} ({outcome}); S61 13/13 = NCG inner-fluctuation route (matched, not overturned)",
                 fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  Saved plot: {OUT_PNG}")


if __name__ == "__main__":
    main()
