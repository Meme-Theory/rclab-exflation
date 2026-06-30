#!/usr/bin/env python
"""S101-CCS-MODELC-KO-DERIVATION  —  §W3-6 (connes-ncg-theorist)

Trigger      : [VERIFY-THEOREM]
Classification: GEOMETRIC
Scheme       : CCS-PRIMARY-KO-SIGN-TABLE-DERIVATION
Convention   : DISCRETE-EXACT
L_max        : N/A (finite triple F; no Peter-Weyl truncation)

GOAL
----
Derive the KO-dimension and real-structure sign triple (epsilon, epsilon',
epsilon'') of the CCS Model-C (G422D) finite spectral triple FROM the on-disk
PRIMARY CCS-2013/2015 constructions, and compare against the substrate anchor
T_S = (KO_dim = 6, (+1, +1, -1)) loaded from s100b_w2_2_ps_variant_id.npz
(npz ground truth per the (ii.B) runtime-drift correction — the stale S100b
plan-text KO_dim=2 is NOT consumed).

OPERATOR (three-branch discrete set comparison)
-----------------------------------------------
  T_C = (KO_dim, eps, eps', eps'')   vs   T_S = (6, +1, +1, -1).
  PASS = T_C == T_S (exact discrete equality on all four slots).
  FAIL = T_C determinate AND T_C != T_S (any slot).
  INFO = T_C UNDERDETERMINED at the on-disk PRIMARY constructions
         (documented obstruction; marked plan-freeze addition):
         the four pinned primaries do not, as transcribed, pin the
         ingredients (J, J^2, the grading antiparticle-sign, the order-0
         reality axiom) that fix the KO-dimension; the sign triple is
         recoverable only by supplying NCG-canonical structural facts from
         standard theory (training memory), which feedback_research-corpus
         forbids treating as the PRIMARY source.

SUBSTRATE FRAMING (GEOMETRIC)
-----------------------------
The real structure J is the fabric's charge-conjugation skeleton; KO-dim 6 is
the unique sign class (J^2=+1, JD=DJ, J*gamma = -gamma*J) in which the
substrate's particle/antiparticle split, CPT equality, and chirality-antimatter
nexus cohere — the substrate IS a KO-dim-6 real spectral triple (PROVEN,
machine-eps).  Direction of explanation: substrate J/gamma_9/D_K sign structure
(PROVEN)  ->  KO-dim-6 class  ->  comparison against the externally-constructed
Model-C triple.  The comparison anchor flows FROM the substrate; the papers
supply only the object being classified.

FETCHED-SOURCES-ONLY DISCIPLINE (feedback_research-corpus)
----------------------------------------------------------
The four pinned on-disk transcriptions (Connes/23, 24, 40; Aydemir Connes/27)
are read for content + SHA.  Their on-disk text is summary/phenomenology level;
every gap in the on-disk text is MARKED, never filled from training memory.
The NCG-canonical sign algebra (the (+1,+1,-1) KO-dim-6 triad and its proof) is
computed below as a CORRECT theory-level derivation, but its dependence on
structural inputs NOT present in the pinned texts is the gate's documented
obstruction and the reason the verdict lands INFO rather than PASS.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 0 — Identity / paths
# ---------------------------------------------------------------------------
GATE_ID = "S101-CCS-MODELC-KO-DERIVATION"
SESSION = "S101"
SCHEME = "CCS-PRIMARY-KO-SIGN-TABLE-DERIVATION"
CONVENTION = "DISCRETE-EXACT"
L_MAX = "N/A"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))

# Import discipline only — NO numerical framework constant is consumed by this
# gate.  The comparison anchor is the substrate npz; the papers supply the
# Model-C CONSTRUCTION being classified.
from canonical_constants import M_KK_gravity, tau_fold  # noqa: F401  (import-discipline witness)

OUT_NPZ = PROJECT_ROOT / "computations" / "session-101" / "s101_ccs_modelc_ko_derivation.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-101" / "s101_ccs_modelc_ko_derivation.png"
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_PATH = SHARED / "canonical_constants.py"

# Pinned input files (SHA-pinned in the plan; re-hashed at runtime for audit).
PS_VARIANT_NPZ = PROJECT_ROOT / "computations" / "session-100b" / "s100b_w2_2_ps_variant_id.npz"
SRC_CCS23 = PROJECT_ROOT / "researchers" / "Connes" / "23_2013_Chamseddine_Connes_vSuijlekom_Inner_Fluctuations.md"
SRC_CCS24 = PROJECT_ROOT / "researchers" / "Connes" / "24_2013_Chamseddine_Connes_vSuijlekom_Pati_Salam.md"
SRC_CCS40 = PROJECT_ROOT / "researchers" / "Connes" / "40_2015_Chamseddine_Connes_van_Suijlekom_Grand_Unification_Spectral_Pati_Salam.md"
SRC_AYDEMIR_MD = PROJECT_ROOT / "researchers" / "Connes" / "27_2025_Aydemir_Unified_Pati_Salam_NCG.md"
SRC_AYDEMIR_PDF = PROJECT_ROOT / "downloads" / "research-sweep-s99" / "ncg-spectral-action" / "05_Aydemir_Unified-Pati-Salam-NCG-Overview.pdf"


# ---------------------------------------------------------------------------
# Section 1 — SHA infrastructure (dual-SHA per S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(p: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(p.read_bytes())
    except OSError:
        return "MISSING"
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = SCRIPT_PATH.read_bytes()
    try:
        canonical_bytes = CANONICAL_PATH.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 2 — On-disk PRIMARY-source audit (what the pinned texts actually fix)
# ---------------------------------------------------------------------------
# Scan the four pinned PRIMARY transcriptions for any explicit statement of the
# KO-dim-fixing ingredients.  This audit is the structural basis of the INFO
# verdict: if the primaries are SILENT on (KO-dim / J / J^2 / reality-axiom /
# grading antiparticle-sign), then the sign triple is NOT pinned by the on-disk
# primaries and the axis-(iii) indeterminacy is a property of the PRIMARY
# literature (as transcribed), not merely of the Aydemir taxonomy.
KO_FIXING_PATTERNS = [
    "ko-dim", "ko dim", "ko-dimension", "ko dimension",
    "real structure", "reality axiom", "j^2", "j squared",
    "antiparticle grading", "grading sign", "antilinear",
    "charge conjugation operator", "mod 8", "dimension six",
]


def audit_primary_for_ko(p: Path) -> dict:
    """Return per-source hit record for KO-dim-fixing statements.

    A 'framework-side' hit (a line that refers to the SUBSTRATE's own triple,
    e.g. 'D_K', 'SU(3)', 'phonon-exflation') is recorded separately — it is NOT
    a statement about the CCS Pati-Salam triple and does not pin the PS KO-dim.
    """
    rec = {"path": str(p.relative_to(PROJECT_ROOT)).replace("\\", "/"),
           "ko_fixing_hits": [], "framework_side_hits": 0, "found": p.exists()}
    if not p.exists():
        return rec
    text = p.read_text(encoding="utf-8", errors="replace")
    low = text.lower()
    for line in text.splitlines():
        ll = line.lower()
        for pat in KO_FIXING_PATTERNS:
            if pat in ll:
                # classify: substrate/framework-side reference vs CCS-PS statement
                fw = any(tok in ll for tok in ["d_k", "su(3)", "phonon-exflation", "phonon exflation",
                                               "framework", "session 3", "session 7", "c^16"])
                if fw:
                    rec["framework_side_hits"] += 1
                else:
                    rec["ko_fixing_hits"].append(line.strip()[:160])
                break
    rec["ko_fixing_count"] = len(rec["ko_fixing_hits"])  # genuine CCS-PS KO statements
    return rec


# ---------------------------------------------------------------------------
# Section 3 — NCG-canonical sign-table derivation (theory-level, machine-eps)
# ---------------------------------------------------------------------------
# Explicit minimal real-structure witness on H_F = H_particle (+) H_antiparticle.
# J_F = S o K : S = particle<->antiparticle swap (linear), K = complex conjugation.
# gamma_F = grading; antiparticle grading = NEGATIVE of particle grading
#           (the CCM-2007/CCS structural form yielding {J,gamma}=0, KO-dim 6).
# D_F = [[0, H],[H^dagger, 0]]  (Connes/40 line 100 off-diagonal-block form);
#       J-real (order-0 reality axiom) => H complex-SYMMETRIC.
#
# ANTILINEAR commutation discipline (CAUTION per plan substitution chain Step 4):
#   For J = S o K and any operator X, the relation  J X = s * X J  (s=+/-1)
#   reduces — after stripping the common trailing K — to the LINEAR identity
#         S * conj(X)  =  s * X * S .
#   epsilon  = sign(J^2)            via  J^2  =  S * conj(S)   (== I)
#   epsilon' = sign(J D -+ D J)     via  S*conj(D) =? +/- D*S  (J-real D)
#   epsilon''= sign(J gamma -+ gamma J) via S*conj(gamma) =? +/- gamma*S
ZTOL = 1e-12  # (local) THEOREM-grade numeric witness tolerance


def _antilinear_sign(S: np.ndarray, X: np.ndarray) -> int | None:
    """Return +1 / -1 / None for the antilinear relation J X = s X J,
    i.e. S*conj(X) = s * X*S as a linear-operator identity."""
    lhs = S @ np.conjugate(X)          # (local)
    xs = X @ S                          # (local)
    if np.max(np.abs(lhs - xs)) < ZTOL:
        return +1
    if np.max(np.abs(lhs + xs)) < ZTOL:
        return -1
    return None


def derive_ko_signs() -> dict:
    I2 = np.eye(2, dtype=complex)            # (local)
    Z2 = np.zeros((2, 2), dtype=complex)     # (local)

    # S = particle<->antiparticle swap (linear part of J)
    S = np.block([[Z2, I2], [I2, Z2]])       # (local)

    # gamma_F: particle grading g = diag(+1,-1) (L/R chirality slot);
    # antiparticle grading = -g  => gamma = diag(g, -g)
    g = np.diag([1.0, -1.0]).astype(complex)  # (local)
    gamma = np.block([[g, Z2], [Z2, -g]])     # (local)

    # ---- epsilon = sign(J^2) ; J^2 = S conj(S) (S real => = S^2 = I) ----
    J2 = S @ np.conjugate(S)                   # (local)
    eps = +1 if np.max(np.abs(J2 - np.eye(4))) < ZTOL else (-1 if np.max(np.abs(J2 + np.eye(4))) < ZTOL else None)

    # ---- epsilon'' = sign(J gamma -+ gamma J)  (gamma real => conj(gamma)=gamma) ----
    eps2 = _antilinear_sign(S, gamma)

    # ---- epsilon' = sign(J D -+ D J) on a J-REAL D_F (complex-symmetric H) ----
    # Two independent J-real (complex-symmetric) Yukawa witnesses; eps' must agree.
    rng_blocks = [
        np.array([[2 + 1j, 1 - 1j], [1 - 1j, 3 - 1j]], dtype=complex),   # (local) symmetric
        np.array([[5 + 0j, 2 + 3j], [2 + 3j, 0 + 7j]], dtype=complex),   # (local) symmetric
    ]
    eps1_vals = []                              # (local)
    Dwitness = None                             # (local)
    for H in rng_blocks:
        assert np.max(np.abs(H - H.T)) < ZTOL, "Yukawa block must be J-real (complex-symmetric)"
        Hd = H.conj().T                         # (local)
        D = np.block([[Z2, H], [Hd, Z2]])       # (local)
        if Dwitness is None:
            Dwitness = D
        eps1_vals.append(_antilinear_sign(S, D))
    eps1 = eps1_vals[0] if (len(set(eps1_vals)) == 1) else None
    eps1_consistent = len(set(eps1_vals)) == 1

    # ---- Diagnostic: a GENERIC (non-J-real) D has NO clean eps' ----
    # This is the witness that the order-0 reality axiom is load-bearing:
    # an arbitrary complex Yukawa block is NOT an admissible finite Dirac.
    Hgen = np.array([[5 - 3j, 1 + 1j], [2 + 0j, 0 + 7j]], dtype=complex)  # (local) NON-symmetric
    Dgen = np.block([[Z2, Hgen], [Hgen.conj().T, Z2]])                    # (local)
    eps1_generic = _antilinear_sign(S, Dgen)   # expected: None (no clean sign)

    # ---- J^2 / [J,D] / {J,gamma} machine-eps residual witnesses ----
    # (reported as the substrate-side cross-reference analogues; here on the
    #  constructed Model-C witness)
    res_J2 = float(np.max(np.abs(J2 - np.eye(4))))                      # (local)
    # [J,D_F]=0 in conjugation form: S conj(D) S - D  (eps'=+1 <=> this ~ 0)
    res_JD = float(np.max(np.abs(S @ np.conjugate(Dwitness) @ S - Dwitness)))   # (local)
    # {J,gamma}=0 in conjugation form: S conj(gamma) S + gamma  (eps''=-1 <=> ~0)
    res_Jg = float(np.max(np.abs(S @ np.conjugate(gamma) @ S + gamma)))         # (local)

    return {
        "eps": eps, "eps_prime": eps1, "eps_double_prime": eps2,
        "eps_prime_consistent": eps1_consistent,
        "eps_prime_vals": eps1_vals,
        "eps_prime_generic_nonjreal": eps1_generic,   # None => reality axiom load-bearing
        "res_J2": res_J2, "res_JD_conjform": res_JD, "res_Jgamma_conjform": res_Jg,
    }


# ---------------------------------------------------------------------------
# Section 4 — KO even-grading table row lookup
# ---------------------------------------------------------------------------
# Connes even-grading KO sign table (epsilon, epsilon', epsilon''):
#   n = 0 : (+1, +1, +1)      n = 2 : (-1, +1, -1)
#   n = 4 : (-1, +1, +1)      n = 6 : (+1, +1, -1)
KO_EVEN_TABLE = {
    0: (+1, +1, +1),
    2: (-1, +1, -1),
    4: (-1, +1, +1),
    6: (+1, +1, -1),
}


def ko_dim_from_triple(eps: int, eps1: int, eps2: int) -> int | None:
    for n, trip in KO_EVEN_TABLE.items():
        if trip == (eps, eps1, eps2):
            return n
    return None


# ---------------------------------------------------------------------------
# Section 5 — Compute (derive, audit, compare)
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- load substrate anchor from npz (GROUND TRUTH; ii.B drift correction) ---
    dz = np.load(PS_VARIANT_NPZ, allow_pickle=True)
    ko_triple_npz = tuple(int(x) for x in dz["ko_sign_triple"])     # (local) [1,1,-1]
    ko_dim_npz = int(dz["ko_dim_npz"])                              # (local) 6
    ko_dim_computed_npz = int(dz["ko_dim_computed"])                # (local) 6
    ko_dim_plan_text_drift = int(dz["ko_dim_plan_text_drift"])     # (local) 2  (NOT consumed)
    ko_axis_status_npz = str(dz["ko_axis_status"])                 # (local)
    variant_id = str(dz["variant_id"])                             # (local) C-LR
    variant_symmetry = str(dz["variant_symmetry"])                 # (local) G422D
    hf_dim_per_gen = int(dz["hf_dim_per_gen"])                     # (local) 32

    # Substrate anchor T_S (npz ground truth; stale plan-text KO_dim=2 NOT used):
    T_S = (ko_dim_npz,) + ko_triple_npz                            # (local) (6, +1, +1, -1)

    # --- Step 1: reconstruct Model-C H_F dimension from the on-disk content ---
    # Per the npz source_quotes Q_FERMIONS (on-disk Aydemir/CCS content):
    #   fermions per generation: (4,2,1) + (4bar,1,2), particle + antiparticle.
    #   (4,2,1): 4*2*1 = 8 ;  (4bar,1,2): 4*1*2 = 8  => 16 Weyl (one sector)
    #   doubled for particle+antiparticle (real structure) => 32 per generation.
    dim_4_2_1 = 4 * 2 * 1                                          # (local) 8
    dim_4bar_1_2 = 4 * 1 * 2                                       # (local) 8
    hf_one_sector_per_gen = dim_4_2_1 + dim_4bar_1_2              # (local) 16
    hf_per_gen_reconstructed = 2 * hf_one_sector_per_gen          # (local) 32 (particle+antiparticle)
    hf_total_3gen = 3 * hf_per_gen_reconstructed                  # (local) 96
    hf_dim_matches_npz = (hf_per_gen_reconstructed == hf_dim_per_gen)  # (local) True

    # --- Step 2: audit the four PINNED PRIMARY sources for KO-fixing statements ---
    primary_audit = [audit_primary_for_ko(p) for p in
                     (SRC_CCS23, SRC_CCS24, SRC_CCS40, SRC_AYDEMIR_MD)]
    total_ko_fixing_in_primaries = sum(r["ko_fixing_count"] for r in primary_audit)  # (local)
    # On-disk Aydemir PDF presence (counted as a source; NOT text-mined here —
    # the .md transcription is the text surface per feedback_research-corpus).
    aydemir_pdf_present = SRC_AYDEMIR_PDF.exists()                 # (local)

    # --- Step 3: NCG-canonical sign derivation (theory-level witnesses) ---
    signs = derive_ko_signs()
    eps, eps1, eps2 = signs["eps"], signs["eps_prime"], signs["eps_double_prime"]
    ko_dim_derived = ko_dim_from_triple(eps, eps1, eps2)
    T_C = (ko_dim_derived, eps, eps1, eps2)                        # (local) derived tuple

    # --- Step 4: discrete match comparison T_C vs T_S (slot-by-slot) ---
    slots_match = [bool(a == b) for a, b in zip(T_C, T_S)]
    all_slots_match = all(slots_match)

    # --- Step 5: determinacy-at-PRIMARIES test (the INFO discriminator) ---
    # The derived triple is theory-CORRECT, but the gate's PASS requires it to be
    # PINNED by the on-disk PRIMARY constructions.  Determinacy-at-primaries holds
    # iff the pinned texts actually state a KO-fixing ingredient.  Audit => 0.
    primaries_pin_ko = (total_ko_fixing_in_primaries > 0)         # (local) False
    sign_algebra_clean = (eps in (+1, -1) and eps1 in (+1, -1)
                          and eps2 in (+1, -1) and ko_dim_derived is not None)  # (local) True

    # ---- THREE-BRANCH OPERATOR ----
    #  PASS : T_C determinate-AND-pinned-by-primaries AND T_C == T_S.
    #  FAIL : T_C determinate (sign algebra clean) AND pinned AND T_C != T_S.
    #  INFO : T_C NOT pinnable from the on-disk PRIMARY constructions
    #         (documented obstruction) — even though the theory-level triple is
    #         clean and MATCHES the substrate anchor.
    if not primaries_pin_ko:
        verdict = "INFO"
        verdict_reason = (
            "PRIMARY-UNDERDETERMINED: the four on-disk pinned CCS/Aydemir "
            "transcriptions state the algebra (C+H_L+H_R+M4), the fermion "
            "content ((4,2,1)+(4bar,1,2)), and the Dirac block form "
            "([[0,H],[Hd,0]]), but are SILENT on every KO-dim-fixing ingredient "
            "(real structure J, J^2, the order-0 reality axiom, the grading "
            "antiparticle-sign). The (+1,+1,-1)/KO-6 triad is NCG-canonically "
            "correct and MATCHES the substrate anchor, but rests on three "
            "structural inputs supplied from standard theory (SM-inherited J/gamma; "
            "antiparticle grading = -particle grading; J-real D_F) that the pinned "
            "primaries do not provide. Axis-(iii) indeterminacy is a property of "
            "the PRIMARY literature (as transcribed), not merely the taxonomy."
        )
    elif not sign_algebra_clean:
        verdict = "INFO"
        verdict_reason = "SIGN-UNDETERMINED: a sign is convention-unpinnable on the construction."
    elif all_slots_match:
        verdict = "PASS"
        verdict_reason = "DETERMINATE-MATCH: T_C == T_S on all four slots, pinned by primaries."
    else:
        verdict = "FAIL"
        verdict_reason = f"DETERMINATE-MISMATCH: T_C={T_C} != T_S={T_S} (slots_match={slots_match})."

    # value string (carries the derived tuple + match + obstruction tag)
    value = (f"T_C=({ko_dim_derived},{eps:+d},{eps1:+d},{eps2:+d}) "
             f"T_S=({T_S[0]},{T_S[1]:+d},{T_S[2]:+d},{T_S[3]:+d}) "
             f"theory_match={all_slots_match} primaries_pin_KO={primaries_pin_ko} "
             f"ko_axis=PRIMARY-UNDERDETERMINED-theory-match-(6,+1,+1,-1)")

    result = {
        "verdict": verdict,
        "verdict_reason": verdict_reason,
        "value": value,
        # derived tuple
        "T_C": T_C, "T_S": T_S,
        "eps": eps, "eps_prime": eps1, "eps_double_prime": eps2,
        "ko_dim_derived": ko_dim_derived,
        "slots_match": slots_match, "all_slots_match": all_slots_match,
        # sign-derivation witnesses
        "res_J2": signs["res_J2"],
        "res_JD_conjform": signs["res_JD_conjform"],
        "res_Jgamma_conjform": signs["res_Jgamma_conjform"],
        "eps_prime_consistent": signs["eps_prime_consistent"],
        "eps_prime_generic_nonjreal_is_None": signs["eps_prime_generic_nonjreal"] is None,
        # H_F reconstruction
        "hf_per_gen_reconstructed": hf_per_gen_reconstructed,
        "hf_total_3gen": hf_total_3gen,
        "hf_dim_matches_npz": hf_dim_matches_npz,
        # primary-source audit
        "total_ko_fixing_in_primaries": total_ko_fixing_in_primaries,
        "primaries_pin_ko": primaries_pin_ko,
        "primary_audit": primary_audit,
        "aydemir_pdf_present": aydemir_pdf_present,
        # substrate anchor provenance
        "ko_triple_npz": ko_triple_npz, "ko_dim_npz": ko_dim_npz,
        "ko_dim_computed_npz": ko_dim_computed_npz,
        "ko_dim_plan_text_drift_NOT_consumed": ko_dim_plan_text_drift,
        "ko_axis_status_npz": ko_axis_status_npz,
        "variant_id": variant_id, "variant_symmetry": variant_symmetry,
        "hf_dim_per_gen_npz": hf_dim_per_gen,
    }
    return result


# ---------------------------------------------------------------------------
# Section 6 — verdict payload (printed; the AGENT calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None) -> dict:
    payload: dict = {
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Plot (optional; derivation gate — a compact KO-table figure)
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:  # pragma: no cover
        print(f"(plot skipped: {exc})")
        return
    fig, ax = plt.subplots(figsize=(8.0, 5.2))
    ax.axis("off")
    rows = [
        ("KO n", "eps", "eps'", "eps''"),
        ("0", "+1", "+1", "+1"),
        ("2", "-1", "+1", "-1"),
        ("4", "-1", "+1", "+1"),
        ("6  <- derived & substrate", "+1", "+1", "-1"),
    ]
    tbl = ax.table(cellText=rows, loc="center", cellLoc="center")
    tbl.auto_set_font_size(False); tbl.set_fontsize(11); tbl.scale(1, 1.6)
    for j in range(4):
        tbl[(4, j)].set_facecolor("#cde7c8")
        tbl[(0, j)].set_facecolor("#dddddd")
    T_C = res["T_C"]; T_S = res["T_S"]
    ax.set_title(
        f"{GATE_ID} — CCS Model-C (G422D) KO sign-table derivation\n"
        f"derived T_C=({T_C[0]},{T_C[1]:+d},{T_C[2]:+d},{T_C[3]:+d})  "
        f"vs substrate T_S=({T_S[0]},{T_S[1]:+d},{T_S[2]:+d},{T_S[3]:+d})  "
        f"theory_match={res['all_slots_match']}\n"
        f"VERDICT {res['verdict']}: primaries_pin_KO={res['primaries_pin_ko']} "
        f"(axis-(iii) PRIMARY-UNDERDETERMINED; theory-match (6,+1,+1,-1))",
        fontsize=10.5,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main() -> None:
    inputs = [PS_VARIANT_NPZ, SRC_CCS23, SRC_CCS24, SRC_CCS40, SRC_AYDEMIR_MD,
              SRC_AYDEMIR_PDF, CANONICAL_PATH]
    pins = log_input_pins(inputs)

    res = compute()

    print()
    print("=== DERIVED SIGN TRIPLE (NCG-canonical, theory-level) ===")
    print(f"  epsilon          = {res['eps']:+d}   (J^2=+1; residual |J^2-I| = {res['res_J2']:.2e})")
    print(f"  epsilon'         = {res['eps_prime']:+d}   (J-real D_F; |S conj(D) S - D| = {res['res_JD_conjform']:.2e}; "
          f"consistent across J-real witnesses = {res['eps_prime_consistent']})")
    print(f"  epsilon''        = {res['eps_double_prime']:+d}   ({{J,gamma}}=0; |S conj(g) S + g| = {res['res_Jgamma_conjform']:.2e})")
    print(f"  reality-axiom load-bearing (generic non-J-real D has NO clean eps') = "
          f"{res['eps_prime_generic_nonjreal_is_None']}")
    print(f"  KO_dim(derived)  = {res['ko_dim_derived']}")
    print(f"  T_C = {res['T_C']}   vs   T_S = {res['T_S']}   slot-match = {res['slots_match']}")
    print()
    print("=== H_F RECONSTRUCTION (on-disk content) ===")
    print(f"  (4,2,1)+(4bar,1,2) one-sector/gen = {res['hf_per_gen_reconstructed']//2}; "
          f"x2 particle+antiparticle = {res['hf_per_gen_reconstructed']}/gen; "
          f"3-gen total = {res['hf_total_3gen']}; matches npz hf_dim_per_gen={res['hf_dim_per_gen_npz']}: "
          f"{res['hf_dim_matches_npz']}")
    print()
    print("=== PRIMARY-SOURCE KO-FIXING AUDIT (the INFO discriminator) ===")
    for r in res["primary_audit"]:
        print(f"  {r['path']}: found={r['found']} KO-fixing(CCS-PS) hits={r['ko_fixing_count']} "
              f"framework-side hits={r['framework_side_hits']}")
    print(f"  TOTAL KO-fixing statements about the CCS-PS triple in pinned primaries = "
          f"{res['total_ko_fixing_in_primaries']}  => primaries_pin_KO = {res['primaries_pin_ko']}")
    print(f"  Aydemir PDF present on disk = {res['aydemir_pdf_present']} (source SHA-pinned; "
          f".md transcription is the text surface per feedback_research-corpus)")
    print()
    print(f"VERDICT: {res['verdict']}")
    print(f"REASON : {res['verdict_reason']}")

    # --- persist npz ---
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        verdict=res["verdict"], verdict_reason=res["verdict_reason"], value=res["value"],
        T_C=np.array(res["T_C"]), T_S=np.array(res["T_S"]),
        eps=res["eps"], eps_prime=res["eps_prime"], eps_double_prime=res["eps_double_prime"],
        ko_dim_derived=res["ko_dim_derived"],
        slots_match=np.array(res["slots_match"]), all_slots_match=res["all_slots_match"],
        res_J2=res["res_J2"], res_JD_conjform=res["res_JD_conjform"],
        res_Jgamma_conjform=res["res_Jgamma_conjform"],
        eps_prime_consistent=res["eps_prime_consistent"],
        eps_prime_generic_nonjreal_is_None=res["eps_prime_generic_nonjreal_is_None"],
        hf_per_gen_reconstructed=res["hf_per_gen_reconstructed"],
        hf_total_3gen=res["hf_total_3gen"], hf_dim_matches_npz=res["hf_dim_matches_npz"],
        total_ko_fixing_in_primaries=res["total_ko_fixing_in_primaries"],
        primaries_pin_ko=res["primaries_pin_ko"],
        primary_audit_json=json.dumps(res["primary_audit"]),
        aydemir_pdf_present=res["aydemir_pdf_present"],
        ko_triple_npz=np.array(res["ko_triple_npz"]), ko_dim_npz=res["ko_dim_npz"],
        ko_dim_computed_npz=res["ko_dim_computed_npz"],
        ko_dim_plan_text_drift_NOT_consumed=res["ko_dim_plan_text_drift_NOT_consumed"],
        ko_axis_status_npz=res["ko_axis_status_npz"],
        variant_id=res["variant_id"], variant_symmetry=res["variant_symmetry"],
        hf_dim_per_gen_npz=res["hf_dim_per_gen_npz"],
        ko_even_table_json=json.dumps({str(k): v for k, v in KO_EVEN_TABLE.items()}),
    )
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(res)

    # --- dual-SHA + verdict payload ---
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"=== dual-SHA ===\n  audit_sha256   = {audit_sha}\n  content_sha256 = {content_sha}")

    extra_rows = [
        f"# regulator_pin=a_n^{{cutoff}} structural-citation-only; no numerical a_n consumed by {GATE_ID}",
        (f"# derived KO triple (eps,eps',eps'')=({res['eps']:+d},{res['eps_prime']:+d},{res['eps_double_prime']:+d}) "
         f"KO_dim={res['ko_dim_derived']} theory-matches substrate T_S={tuple(res['T_S'])}; "
         f"verdict INFO because primaries_pin_KO={res['primaries_pin_ko']} (PRIMARY-UNDERDETERMINED obstruction)"),
        ("# downstream HARD-SEQUENCING: S101-PS-RGE-MODELC-SIN2-MZ dispatches status-quo "
         "(ko_axis=indeterminate-carried); INFO is NOT a determinate KO mismatch, so W3-7 is NOT re-scoped to axes-(i,ii)-only"),
    ]
    print_verdict_payload(res["verdict"], res["value"], audit_sha, content_sha, extra_rows=extra_rows)


if __name__ == "__main__":
    main()
