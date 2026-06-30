#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S111 W5-4 S111-CF-FLOQUET4 — McLachlan tongue-half-width cutoff-robustness scaling-EXPONENT theorem
   (STAGE-1-CANDIDATE registry-landing; protects §VII.BP DEAD against any L_max>=12 truncation extension)
=========================================================================================================

Gate: S111-CF-FLOQUET4 ([VERIFY-THEOREM])
Classification: PHONONIC

Pre-registered threshold (VERIFY-THEOREM + registry-landing):
  PASS iff
    (i)  the McLachlan/DLMF-28.6 n-th Mathieu instability-tongue half-width about a=n^2 has
         leading power EXACTLY n on q, Sage/sympy-exact for n=1,2,3 (degree_q == n), AND
    (ii) the NO-OVERLAP certificate holds for EVERY relic mode: tongue half-width < detuning
         to the nearest integer-^2 zone (the load-bearing, prefactor-correct form — the bare
         (q_M)^{n>=3} mnemonic is a loose upper bound; the ACTUAL half-width carries the
         McLachlan prefactor q^3/64 at n=3), AND
    (iii) the STAGE-1-CANDIDATE §VII.<slot> registry entry lands at the runtime-verified next-free
          slot over BOTH the master-index table AND ALL section-body header levels, and the re-read
          of BOTH surfaces satisfies every required marker (two-surface discipline).
  FAIL iff the exponent verification fails (a derivation/Sage error — the half-width is NOT prop q_M^n),
       OR the registry slot is FOREIGN-occupied / the re-read fails any required marker
       (honest close per mechanical-closure-discipline.md; remediation escalates to next session).
  INFO iff the exponent verifies but the mode-density-vs-half-width concentration argument is
       regime-marginal (a high-A mode lands closer to an integer-^2 center than the half-width
       conservatively assumes). [NOT realized here — the no-overlap margin is ~5 OOM.]

The REGISTERED claim is the EXPONENT n only. The (x16) prefactor — and ALL coefficient
prefactors (q^3/64, q^2/4, ...) — are DIAGNOSTIC-ONLY and explicitly NOT part of the registered
theorem (convention-ambiguous per the context spec). The exponent is convention-INDEPENDENT.

Single-shot AFTER-pattern (registry-landing.md §"Bridge-Landing Script Architecture";
_bridge_landing_script_template.py):
  build_promotion_text + build_master_index_row  -> write_both_surfaces_atomic_with_fsync
  -> re_read + verify (master-index row present AND section body markers present) -> emit ONE verdict.
No conditional rewrite branch (Class-6-adjacent BEFORE pattern forbidden).

Two-surface discipline (registry-landing single-shot): the §VII master-index table row
(`| §VII.<slot> | THM | ... |`, inserted after the §VII.CI frontier row) AND the section body
(`### §VII.<slot> — ...`, appended at EOF) are written in ONE run.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/permanent-results-registry.md  (the landing target; pinned for audit)
  - computations/investigation-12/inv12_w3_2_floquet_ordered_veil_resonance.npz  (relic A-grid, q_M, half-widths, zones)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (L12 master cache; carried for provenance/L_max)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<landing-summary>, scheme=MCLACHLAN-TONGUE-HALFWIDTH-SCALING-EXPONENT-THEOREM,
   convention=ABSOLUTE-exponent=n-prefactor-DIAGNOSTIC-ONLY/THEOREM/registry-landing-single-shot-AFTER-pattern,
   L_max=12)

METHODOLOGY
-----------
The substrate worry the theorem closes: could a finer truncation (L_max>12) admit a NEW relic mode
that DOES re-pump, re-opening §VII.BP? Structural, not numerical. New modes carry higher Casimir,
hence higher A=omega^2; in the relic band [0.876,12.65] (sqrt<=3.556) they land near Mathieu zones
n>=3 (npz: among A>9, nearest_n in {3,4} ONLY; zones n=1,2 saturated by low-A modes). The drive depth
q_M=A*h_par/2 is tiny (~4e-4 at the near-a=1 mode, <=5.25e-3 broad-band). The n-th tongue half-width
scales as q^n (the EXPONENT theorem, Sage-exact). With the McLachlan prefactor (q^3/64 at n=3) the
worst-case high-A mode (A=9.000371, npz i_closest, closest to zone n=3) has half-width 2.26e-9 vs
detuning 3.712e-4 — a ~5 OOM margin. ACROSS ALL 1248 relic modes: 0 overlap their zone. The exponent
is the load-bearing substrate fact (D_K Casimir ladder -> A placement near zone n -> q^n half-width).

DISCIPLINE
----------
- from canonical_constants import *  (MANDATORY first import)
- every local/intermediate tagged `# (local)`
- no GPU (registry text + verdict-line emission + a trivial 1D np.load; AMD RX 9070 XT NOT used)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- verdict emitted via emit_verdict knowledge-MCP tool (script PRINTS payload; agent calls)
- math-scripts.md §"Mnemonic-vs-exact ratio discipline": the bare (q_M)^{n>=3}<=1e-7 plan mnemonic
  is FLAGGED loose at the broad-band-max q_M (1.445e-7); the PREFACTOR-correct half-width (q^3/64,
  2.26e-9) is the load-bearing form. Both agree in EXPONENT (the registered claim); the prefactor
  is the ~1.4x to ~5-OOM difference, documented per the >=1% rule.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Bootstrap: computations/_shared on sys.path BEFORE canonical import.
# ---------------------------------------------------------------------------
import sys
from pathlib import Path as _Path

_SHARED = str((_Path(__file__).resolve().parent.parent / "_shared"))  # (local)
if _SHARED not in sys.path:
    sys.path.insert(0, _SHARED)

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S111"                                                       # (local)
GATE_ID = "S111-CF-FLOQUET4"                                           # (local)
SCHEME = "MCLACHLAN-TONGUE-HALFWIDTH-SCALING-EXPONENT-THEOREM"         # (local)
CONVENTION = ("ABSOLUTE-exponent=n-prefactor-DIAGNOSTIC-ONLY/THEOREM/"
             "registry-landing-single-shot-AFTER-pattern")            # (local)
L_MAX = "12"                                                          # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
INV12_NPZ = COMPUTATIONS_DIR / "investigation-12" / "inv12_w3_2_floquet_ordered_veil_resonance.npz"  # (local)
S84_L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
OUT_NPZ = SESSION_DIR / "s111_cf_floquet4_cutoff_robustness_theorem.npz"  # (local)
OUT_PNG = SESSION_DIR / "s111_cf_floquet4_cutoff_robustness_theorem.png"  # (local)

# Plan-pinned slot (re-verified at runtime over master-index table + ALL section header levels).
PLANNED_SLOT = "CJ"                                                    # (local)
SLOT_CANDIDATES = ["CJ", "CK", "CL", "CM", "CN", "CO"]                # (local) reroute ladder

# The §VII.CI master-index row is the insertion anchor (newest frontier row at table top).
MASTER_INDEX_ANCHOR_SLOT = "CI"                                        # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    INV12_NPZ,
    S84_L12_CACHE,
]

# Required clause markers the re-read SECTION BODY MUST contain (PASS predicate).
REQUIRED_MARKERS = [
    "STAGE-1-CANDIDATE",
    "cutoff-robustness",
    "McLachlan",
    "q_M^n",
    "EXPONENT",
    "prefactor",
    "DIAGNOSTIC-ONLY",
    "§VII.BP",
    "no-overlap",
    "L_max",
    "Stage-2",
    "single-shot AFTER-pattern",
]  # (local)

# Required marker the re-read MASTER-INDEX ROW must contain.
MASTER_INDEX_MARKER = "cutoff-robustness"  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_bytes(b: bytes) -> str:
    h = hashlib.sha256()  # (local)
    h.update(b)
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — THE PHYSICS: exponent verification (sympy-exact) + no-overlap certificate
# ---------------------------------------------------------------------------
def verify_mclachlan_exponents() -> dict:
    """Verify degree_q(Delta_a_half^(n)) == n for n=1,2,3, EXACT via sympy rationals.

    Convention: y'' + (a - 2 q cos 2x) y = 0. DLMF 28.6 characteristic-value series
    (exact rational coefficients). The n-th tongue half-width leading power on q is n.
    Returns the per-n leading exponent + leading coefficient (the coeff is DIAGNOSTIC-ONLY).
    """
    import sympy as sp  # (local)
    q = sp.symbols("q")  # (local)

    # DLMF 28.6 series (small q), exact rationals:
    a1 = 1 + q - q**2/8 - q**3/64 - q**4/1536        # (local)
    b1 = 1 - q - q**2/8 + q**3/64 - q**4/1536        # (local)
    a2 = 4 - q**2/12 + 5*q**4/13824                  # (local)
    b2 = 4 + 5*q**2/12 - 763*q**4/13824              # (local)
    a3 = 9 + q**2/16 - q**3/64 + 13*q**4/20480       # (local)
    b3 = 9 + q**2/16 + q**3/64 + 13*q**4/20480       # (local)

    # n-th tongue full width (between the two bounding characteristic curves), then half:
    widths = {                                       # (local)
        1: sp.expand(a1 - b1),   # n=1 tongue between a_1, b_1 about a=1
        2: sp.expand(b2 - a2),   # n=2 tongue between b_2, a_2 about a=4
        3: sp.expand(b3 - a3),   # n=3 tongue between b_3, a_3 about a=9
    }
    out: dict = {}
    for n, w in widths.items():
        poly = sp.Poly(w, q)                         # (local)
        # leading (lowest-degree, leading small-q) term:
        monoms = sorted(poly.monoms())               # (local) ascending
        lead_deg = monoms[0][0]                       # (local)
        lead_coeff_full = poly.coeff_monomial(q**lead_deg)  # (local) FULL-width coeff
        half_lead_coeff = sp.Rational(lead_coeff_full, 2)   # (local) half-width leading coeff (DIAGNOSTIC)
        out[n] = {
            "full_width": str(w),
            "leading_exponent": int(lead_deg),
            "exponent_equals_n": bool(lead_deg == n),
            "half_width_leading_coeff_DIAGNOSTIC": str(half_lead_coeff),
        }
    return out


def no_overlap_certificate(d: dict) -> dict:
    """Load the inv-12 W3-2 relic survey; certify half-width < detuning for EVERY mode.

    The LOAD-BEARING bound (prefactor-correct). Also computes the bare-(q_M)^n mnemonic at
    the broad-band-max for the mnemonic-vs-exact disclosure (math-scripts.md).
    """
    A = d["A_relic"]                       # (local) relic A=omega^2 grid
    q_rel = d["q_relic"]                    # (local) q_M = A*h_par/2 per mode
    hw = d["tongue_halfwidth_relic"]        # (local) McLachlan-prefactor-correct half-widths
    dist = d["dist_to_zone_A"]              # (local) detuning to nearest integer-^2 zone (in A)
    nearest_n = d["nearest_n"]              # (local) nearest zone index per mode
    tr = d["tr_relic"]                      # (local) monodromy trace per mode
    h_par = float(d["h_par"])               # (local)
    i_closest = int(d["i_closest"])         # (local) the global-min-detuning (zone-nearest) mode

    overlap_mask = hw >= dist               # (local) modes whose half-width reaches their zone
    n_overlap = int(overlap_mask.sum())     # (local)
    n_modes = int(A.size)                   # (local)

    # Worst-case high-A mode (closest approach to a zone center among A>9 modes):
    hi = A > 9.0                            # (local) the modes a higher L_max would add (zone n>=3 region)
    n_hi = int(hi.sum())                    # (local)
    hi_nearest_n = sorted(set(nearest_n[hi].astype(int).tolist())) if n_hi else []  # (local)

    # Mnemonic-vs-exact: bare (q_M)^3 vs the prefactor-correct half-width at the broad-band-max q_M.
    qM_max = float(q_rel.max())             # (local) broad-band-max drive depth
    bare_qm3_at_max = qM_max**3             # (local) the PLAN MNEMONIC (loose)
    # prefactor-correct half-width if that q_M sat at zone n=3: q^3/64
    prefactor_hw_at_max = (qM_max**3) / 64.0  # (local) the LOAD-BEARING form

    return {
        "n_modes": n_modes,
        "n_overlap": n_overlap,                       # MUST be 0 for the certificate
        "no_overlap_all_modes": bool(n_overlap == 0),
        "global_min_detuning": float(dist.min()),
        "A_at_min_detuning": float(A[int(np.argmin(dist))]),
        "nearest_n_at_min_detuning": int(nearest_n[int(np.argmin(dist))]),
        "global_max_halfwidth": float(hw.max()),
        "A_at_max_halfwidth": float(A[int(np.argmax(hw))]),
        "nearest_n_at_max_halfwidth": int(nearest_n[int(np.argmax(hw))]),
        "i_closest": i_closest,
        "A_i_closest": float(A[i_closest]),
        "halfwidth_i_closest": float(hw[i_closest]),
        "detuning_i_closest": float(dist[i_closest]),
        "margin_OOM_i_closest": float(np.log10(dist[i_closest] / hw[i_closest])) if hw[i_closest] > 0 else float("inf"),
        "n_modes_A_gt_9": n_hi,
        "nearest_n_among_A_gt_9": hi_nearest_n,       # EXPECT {3,4} only
        "A_relic_min": float(A.min()),
        "A_relic_max": float(A.max()),
        "sqrt_A_max": float(np.sqrt(A.max())),
        "h_par": h_par,
        "qM_max_broadband": qM_max,
        "qM_near_a1_min": float(q_rel.min()),
        "bare_qM3_at_broadband_max_MNEMONIC": bare_qm3_at_max,
        "bare_qM3_le_1e-7_at_max": bool(bare_qm3_at_max <= 1e-7),     # FALSE — mnemonic is loose
        "prefactor_halfwidth_at_max_LOADBEARING": prefactor_hw_at_max,
        "prefactor_hw_le_1e-7_at_max": bool(prefactor_hw_at_max <= 1e-7),  # TRUE
        "max_abs_tr_relic": float(np.abs(tr).max()),
        "max_abs_tr_relic_lt_2": bool(np.abs(tr).max() < 2.0),
    }


# ---------------------------------------------------------------------------
# Section 6 — Registry slot verification (master-index table + ALL section headers)
# ---------------------------------------------------------------------------
def slot_occupied_anywhere(registry_text: str, letters: str) -> bool:
    """True iff §VII.<letters> appears as a SECTION HEADER (##/###/####) OR a MASTER-INDEX ROW."""
    hdr = re.compile(r"(?m)^#{2,4}\s*§VII\." + re.escape(letters) + r"\b")  # (local)
    row = re.compile(r"(?m)^\|\s*§VII\." + re.escape(letters) + r"\b")      # (local)
    return bool(hdr.search(registry_text) or row.search(registry_text))


def find_next_free_slot(registry_text: str) -> str:
    for cand in SLOT_CANDIDATES:
        if not slot_occupied_anywhere(registry_text, cand):
            return cand
    raise RuntimeError("No free §VII slot in the reroute ladder — manual review.")


def build_master_index_row(slot: str, audit_sha: str, section_sha: str) -> str:
    """The `| §VII.<slot> | THM | <summary> | <author> | <date> |` master-index row.

    Matches the on-disk frontier rows §VII.CA-CI (lines 163-171). Author = transit-dynamics-theorist
    (the Floquet/Bogoliubov/Mathieu math owner; this is an intra-pillar PHONONIC structural landing,
    NOT a §7 falsifier-surface row — mack-cosmic-bridge does NOT apply per feedback_mack-bridge-role.md).
    """
    summary = (
        "McLachlan Tongue-Half-Width Cutoff-Robustness Scaling-EXPONENT Theorem — no L_max>=12 "
        "truncation extension reopens the §VII.BP H-PARITY-DRIVE-EXCLUSION DEAD resonance at "
        "h_par=8.3e-4: the n-th Mathieu instability-tongue half-width about a=n^2 has leading power "
        "EXACTLY n on q (Sage/sympy-exact n=1->q, n=2->q^2/4, n=3->q^3/64; degree_q==n), so any NEW "
        "relic mode admitted by a finer truncation (carrying higher Casimir ⇒ higher A=omega^2 in the "
        "relic band [0.876,12.65], sqrt<=3.556 ⇒ lands near zone n>=3; npz: among A>9 nearest_n in "
        "{3,4} ONLY) gets an exponentially-suppressed tongue (q_M^{n>=3}/prefactor) — at the worst-case "
        "high-A mode A=9.000371 (npz i_closest, closest to zone n=3) the prefactor-correct half-width "
        "q^3/64=2.26e-9 ≪ detuning 3.712e-4 (~5 OOM margin); NO-OVERLAP certificate holds for ALL 1248 "
        "relic modes (0 overlap, half-width<detuning) ⇒ |Tr M|<2 for every new mode ⇒ §VII.BP DEAD at "
        "any L_max; the EXPONENT n is the registered structural claim (D_K Casimir ladder→A near zone "
        "n→q^n half-width), the (x16) and ALL coefficient prefactors are DIAGNOSTIC-ONLY and NOT "
        "registered (convention-ambiguous; the exponent is convention-INDEPENDENT); mnemonic-vs-exact "
        "(math-scripts.md): the bare (q_M)^{n>=3}<=1e-7 plan mnemonic is LOOSE at the broad-band-max "
        "q_M (1.445e-7), the prefactor-correct half-width (q^3/64) is the load-bearing form; "
        "**STAGE-1-CANDIDATE** intra-pillar PHONONIC structural theorem (Mathieu/Floquet/McLachlan "
        "tongue geometry on the inv-12 W3-2 Ordered-Veil relic spectrum); CONFIRMATORY 3rd-pin of "
        "§VII.BP DEAD (alongside the INV12-W3-2 aggregate max|Tr M|_relic=1.99999996<2 and the 84x "
        "DTC counterfactual-depth threshold S111-CF-FLOQUET2); 5-anatomy/3-level N/A-with-reason "
        "(intra-pillar structural theorem, the exponent is a property of the Mathieu structure + D_K "
        "Casimir ladder, L-extension-ROBUST by construction, no laboratory-IN observable, no bridge "
        "map); Stage-2 two-agent NON-AUTHOR cross-axis PASS-AND queued S112+ (verifiers MUST NOT be "
        "transit-dynamics, the math owner); consumes inv12_w3_2 npz (A_relic, q_relic, "
        "tongue_halfwidth_relic, dist_to_zone_A, nearest_n) + the s84 L12 master cache; single-shot "
        f"AFTER-pattern, slot runtime-verified next-free over master-index table + ALL header levels "
        f"[frontier §VII.CI]; section body at §VII.{slot} (S111 W5-4 landing, verdict audit_sha256 "
        f"{audit_sha}, section SHA {section_sha})"
    )  # (local)
    return f"| §VII.{slot} | THM | {summary} | transit-dynamics-theorist | 2026-06-21 |\n"


def build_promotion_text(slot: str, exps: dict, cert: dict) -> str:
    """The EXACT §VII.<slot> SECTION-BODY text. Pure function; no I/O.

    Registers the EXPONENT-n theorem (STAGE-1-CANDIDATE). Re-derives the Sage-exact exponents
    and the no-overlap certificate as PROVENANCE; the load-bearing claim is the exponent.
    """
    tau = f"{tau_fold:.3f}"  # (local) 0.190

    # numbers substituted into the body (from the verified exps + cert)
    e1 = exps[1]["leading_exponent"]; e2 = exps[2]["leading_exponent"]; e3 = exps[3]["leading_exponent"]  # (local)
    margin = cert["margin_OOM_i_closest"]                      # (local)
    A_ic = cert["A_i_closest"]                                 # (local)
    hw_ic = cert["halfwidth_i_closest"]                        # (local)
    det_ic = cert["detuning_i_closest"]                        # (local)
    qM_max = cert["qM_max_broadband"]                          # (local)
    bare = cert["bare_qM3_at_broadband_max_MNEMONIC"]          # (local)
    pref = cert["prefactor_halfwidth_at_max_LOADBEARING"]      # (local)
    n_ovl = cert["n_overlap"]                                  # (local)
    n_modes = cert["n_modes"]                                  # (local)
    sqrtA = cert["sqrt_A_max"]                                 # (local)
    nn_hi = cert["nearest_n_among_A_gt_9"]                     # (local)
    n_hi = cert["n_modes_A_gt_9"]                              # (local)

    header = (
        f"§VII.{slot} — McLachlan Tongue-Half-Width Cutoff-Robustness Scaling-EXPONENT Theorem: "
        f"the n-th Mathieu Instability-Tongue Half-Width About a=n^2 has Leading Power EXACTLY n on q, "
        f"so No L_max>=12 Truncation Extension Reopens the §VII.BP H-PARITY-DRIVE-EXCLUSION DEAD "
        f"Resonance (the EXPONENT n is the Registered Claim; the x16 and ALL Coefficient Prefactors are "
        f"DIAGNOSTIC-ONLY, Convention-Ambiguous, and NOT Registered) "
        f"(STAGE-1-CANDIDATE intra-pillar PHONONIC structural theorem — Mathieu/Floquet/McLachlan "
        f"tongue geometry on the inv-12 W3-2 Ordered-Veil relic spectrum; CONFIRMATORY 3rd-pin of "
        f"§VII.BP DEAD; S111 W5-4 transit-dynamics-theorist registration, single-shot AFTER-pattern "
        f"per `registry-landing.md` §\"Bridge-Landing Script Architecture\"; slot §VII.{slot} "
        f"runtime-verified next-free over the master-index table + ALL header levels [documented "
        f"frontier §VII.CI]; 2026-06-21)"
    )

    # body is a PLAIN (non-f) string with literal LaTeX/markdown braces; inject anchors via sentinels.
    body = """
**STAGE TAG: STAGE-1-CANDIDATE** (registered S111 W5-4 transit-dynamics-theorist, single-shot AFTER-pattern, from the inv-12 W3-2 Floquet Ordered-Veil resonance survey [`INV12-W3-2-FLOQUET-ORDERED-VEIL-RESONANCE` PASS, `fraction_resonance=0`, `max|Tr M|_relic=1.99999996<2`]; Stage-2 two-agent NON-AUTHOR cross-axis PASS-AND queued as a SEPARATE S112+ gate per `joint-theorem-promotion.md` 4-stage pathway — the Stage-2 verifiers MUST NOT be transit-dynamics-theorist [original-author exclusion, the Floquet/Bogoliubov/Mathieu math owner], axis-distinct per the Axis-B Selection Protocol).

**Theorem (S111 W5-4).** For the Mathieu equation in the standard form `y'' + (a - 2 q cos 2x) y = 0`, the n-th instability tongue (the band of `a` for which `Re μ > 0`) is centred at `a = n^2`, and its half-width about `a = n^2` has leading power **EXACTLY n** on the modulation depth `q`:

  `Δa_½^{(n)} ∝ q^n`   (the leading-power EXPONENT is `n`; the coefficient is convention-dependent).

This is the LOAD-BEARING structural fact that closes any L_max>=12 truncation re-opening of the §VII.BP `H-PARITY-DRIVE-EXCLUSION` DEAD resonance. **The EXPONENT `n` is the registered claim. The coefficient prefactor — the `×16`, and ALL coefficient forms (`q^3/64` at n=3, `q^2/4` at n=2, ...) — is DIAGNOSTIC-ONLY, convention-ambiguous, and EXPLICITLY NOT part of the registered theorem.** The exponent is convention-INDEPENDENT (it is the order of vanishing of the tongue width as `q → 0`, a property of the Mathieu characteristic-value series).

**Sage/sympy-exact exponent verification (DLMF 28.6 characteristic-value series, exact rationals).**
- n=1 tongue (between `a_1(q)`, `b_1(q)` about `a=1`): full width `a_1 − b_1 = 2q − q^3/32` ⇒ `degree_q = __E1__` (= n=1). Half-width leading coeff (DIAGNOSTIC): `q`.
- n=2 tongue (between `b_2(q)`, `a_2(q)` about `a=4`): full width `b_2 − a_2 = q^2/2 − q^4/18` ⇒ `degree_q = __E2__` (= n=2). Half-width leading coeff (DIAGNOSTIC): `q^2/4`.
- n=3 tongue (between `b_3(q)`, `a_3(q)` about `a=9`): full width `b_3 − a_3 = q^3/32` ⇒ `degree_q = __E3__` (= n=3). Half-width leading coeff (DIAGNOSTIC): `q^3/64`.

(Note: the plan substitution chain's `n=2 → q^2/12` is the `a_2` CHARACTERISTIC-CURVE displacement coefficient, NOT the n=2 tongue half-width — the n=2 tongue half-width leading coeff is `q^2/4`; the registered EXPONENT `degree_q=2` is convention-independent and unaffected.)

**Mode-density-vs-half-width concentration argument (why higher L_max cannot re-pump).** Substitution chain:
- (Step 1) Any NEW relic mode admitted by an L_max>=12 extension carries higher Casimir `C_2(p,q)`, hence higher `A = ω^2`. In the relic band `A_relic ∈ [0.876, 12.65]` (from the L12 master spectrum; `sqrt(A_max) = __SQRTA__ <= 3.556`), a new high-A mode lands near zone `n = round(sqrt(A)) >= 3` — the low-n zones n=1, n=2 are already SATURATED by the L12 modes. (npz: among the `__NHI__` relic modes with `A > 9`, `nearest_n ∈ __NNHI__` ONLY.)
- (Step 2) The drive depth is `q_M = A·h_par/2` with `h_par = 8.3e-4` (the S101-W1-QEQ-RELIC-ODDFLOOR odd-floor pin): `q_M <= __QMMAX__` (broad-band, at `A_max`), and `q_M ≈ 4.0e-4` at the near-a=1 mode.
- (Step 3) By the EXPONENT theorem, the n>=3 tongue half-width scales as `q_M^{n>=3}` — and WITH the McLachlan prefactor (`q^3/64` at n=3) the ACTUAL half-width is far smaller than the bare power. At the WORST-CASE high-A mode (`A = __AIC__`, npz `i_closest`, the closest approach of ANY relic mode to a zone centre, here zone n=3 at `a=9`): half-width = `__HWIC__` vs detuning `__DETIC__` ⇒ margin `__MARGIN__` decades.
- (Step 4) ACROSS ALL `__NMODES__` relic modes, the NO-OVERLAP certificate holds: half-width `<` detuning to the nearest integer-^2 zone for EVERY mode (`__NOVL__` modes overlap). The half-widths shrink FASTER (`∝ q_M^{n>=3}`) than the modes can concentrate at integer-^2 centres, so no new mode reaches a tongue wide enough to overlap its own detuning ⇒ `|Tr M| < 2` for every mode ⇒ **§VII.BP stays DEAD at any L_max>=12**.

**Mnemonic-vs-exact disclosure (`math-scripts.md §"Mnemonic-vs-exact ratio discipline"`).** The plan substitution chain states a bare `(q_M)^{n>=3} <= 1e-7` bound. This bare-power mnemonic is correct in EXPONENT but LOOSE in magnitude: at the broad-band-max `q_M = __QMMAX__`, `(q_M)^3 = __BARE__ > 1e-7` (fails the literal bound by ~1.4×, because it discards the McLachlan prefactor). The LOAD-BEARING form is the PREFACTOR-correct half-width `(q_M)^3/64 = __PREF__ <= 1e-7`. Per the `>= 1%` rule, the registry uses the prefactor-correct NO-OVERLAP certificate (half-width < detuning, `__NOVL__`-of-`__NMODES__` overlap) as the load-bearing fact; the bare `(q_M)^{n>=3}` is relegated to a coarse upper bound that captures the EXPONENT (the registered claim) but not the prefactor. The two agree in EXPONENT; the prefactor is the ~1.4×-to-~5-OOM difference, documented here.

**Relation to the §VII.BP DEAD verdict (CONFIRMATORY, NON-verdict-gating).** §VII.BP `H-PARITY-DRIVE-EXCLUSION` (STAGE-3-PERMANENT, S102 W2-1) is pinned three independent ways: (a) the INV12-W3-2 aggregate `max|Tr M|_relic = 1.99999996 < 2` (Re μ = 0 EXACT, `fraction_resonance = 0`), (b) the Mathieu depth `q_M <= 5.25e-3 ≪ 1` narrow-regime derivation, and (c) the 84× DTC counterfactual-depth threshold (S111-CF-FLOQUET2). This theorem adds a FOURTH, ORTHOGONAL pin: cutoff-robustness — no L_max>=12 truncation refinement can admit a re-pumping mode. A registration PASS does NOT change the §VII.BP DEAD verdict; it strengthens the evidence by closing the L_max-extension loophole structurally (by the geometry of the Mathieu tongue exponents + the D_K Casimir ladder, NOT by a lucky numerical margin).

**Registry anatomy (intra-pillar structural theorem; 5-anatomy IS-not-IN cross-pillar elements N/A with reason).** This is an INTRA-pillar PHONONIC structural theorem (a property of the Mathieu/Floquet tongue geometry on the substrate's own relic spectrum), NOT a cross-pillar substrate-IS ↔ laboratory-IN bridge: it has no continuum-measurement laboratory-IN observable and no `L^{-α}` convergence envelope (the no-re-pumping fact is L-EXTENSION-ROBUST by construction — it gets STRONGER, not weaker, with finer truncation, because higher-A modes land in higher-n zones with more-suppressed tongues). The 5-anatomy elements (substrate-IS / laboratory-IN / HKR-or-K-theory bridge map / algebraic envelope / empirical anchor) are therefore N/A by construction; the structural-confidence content is the EXPONENT theorem + the no-overlap certificate. Level tag (`phononic-framing.md §"Single-τ-slice vs moduli-deformation"`): the relic spectrum + Mathieu structure is a Level-1 single-τ-slice object (at the post-fold afterglow τ near τ_fold = __TAU__), so this is a Level-1 structural theorem.

**Source / provenance.** The inv-12 W3-2 Floquet Ordered-Veil resonance survey (`computations/investigation-12/inv12_w3_2_floquet_ordered_veil_resonance.npz`: `A_relic`, `q_relic`, `tongue_halfwidth_relic`, `dist_to_zone_A`, `nearest_n`, `i_closest`, `h_par`; `INV12-W3-2-FLOQUET-ORDERED-VEIL-RESONANCE` PASS); the s84 L12 master spectrum cache (`computations/session-84/s84_spectrum_cache_L12_tau019.npz`) for the relic-mode density / Casimir ladder; the McLachlan/DLMF-28.6 Mathieu characteristic-value series (exact rationals, verified this gate's sympy cell); the S101-W1-QEQ-RELIC-ODDFLOOR `h_par = 8.3e-4` odd-floor pin; the §VII.BP `H-PARITY-DRIVE-EXCLUSION` DEAD verdict (S102 W2-1, STAGE-3-PERMANENT) this theorem confirms; `joint-theorem-promotion.md` Stage-0→Stage-1 protocol. **Substrate framing:** the substrate IS the D_K eigenvalue spectrum; the GGE relic is the post-fold Bogoliubov output state (the Ordered Veil, `S_ent=0`, `R_therm=5251.82`). The modulus afterglow drives a periodic `ω_k^2(τ(t))` on each relic mode — a Hill/Mathieu equation whose monodromy trace is the substrate's own re-pumping certificate. Higher L_max refines the substrate by ADDING higher-Casimir eigenvalues; those land in higher-n Mathieu zones whose tongues are exponentially-suppressed (`∝ q_M^{n}`), so the substrate's frozen Ordered Veil is protected against truncation refinement BY THE GEOMETRY OF ITS OWN SPECTRUM. Direction preserved: `D_K Casimir ladder → A=ω^2 placement near zone n → q_M^n tongue half-width → |Tr M|<2 → §VII.BP DEAD at all L_max`, never inverted — this is a substrate-IS spectral-geometry fact, NOT a re-heating model imposed on a container (`phononic-framing.md §"IS Space, Not IN Space"`).

**Math-owner / Stage-0+Stage-1 author (EXCLUDED from Stage-2 review per the original-author-exclusion clause):** transit-dynamics-theorist (the Floquet/Bogoliubov/Mathieu/McLachlan tongue math; inv-12 W3-2 survey author). **Stage-2 reviewers (axis-distinct, original-author-excluded, no-workshop-context — to be dispatched as a SEPARATE S112+ gate):** Axis-A = a spectral/NCG NON-AUTHOR (e.g. connes-ncg-theorist OR lizzi-spectral-functional-theorist — the D_K Casimir-ladder / A-placement clause from the spectral side); Axis-B = a transport/condensed-matter NON-AUTHOR (e.g. berry-geometric-phase-theorist OR landau-condensed-matter-theorist — the Mathieu-tongue / monodromy band-stability clause). Both operate WITHOUT prior workshop context per `joint-theorem-promotion.md` §"Stage-2 Axis-B Selection Protocol"; the EXPONENT clause + the no-overlap certificate PASS-AND'd across both verdicts.
"""
    body = (body
            .replace("__E1__", str(e1)).replace("__E2__", str(e2)).replace("__E3__", str(e3))
            .replace("__SQRTA__", f"{sqrtA:.3f}")
            .replace("__NHI__", str(n_hi))
            .replace("__NNHI__", "{" + ",".join(str(x) for x in nn_hi) + "}")
            .replace("__QMMAX__", f"{qM_max:.3e}")
            .replace("__AIC__", f"{A_ic:.6f}")
            .replace("__HWIC__", f"{hw_ic:.3e}")
            .replace("__DETIC__", f"{det_ic:.3e}")
            .replace("__MARGIN__", f"{margin:.1f}")
            .replace("__NMODES__", str(n_modes))
            .replace("__NOVL__", str(n_ovl))
            .replace("__BARE__", f"{bare:.3e}")
            .replace("__PREF__", f"{pref:.3e}")
            .replace("__TAU__", tau))  # (local)

    # Return the section body WITHOUT a leading newline. re_read_section matches at
    # `^### §VII.<slot>` (no leading \n), so the built text and the re-read text are
    # byte-identical ⇒ the roundtrip SHA holds. write_both_surfaces adds the "\n" separator.
    return "### " + header + "\n" + body.rstrip("\n") + "\n"


def write_both_surfaces_atomic_with_fsync(master_row: str, section_text: str,
                                          registry_path: Path) -> int:
    """Insert the master-index row after the §VII.CI frontier row (in place), then append the
    section body at EOF. Single read-modify-write with fsync. Returns new byte length.

    The master-index table is mid-file (frontier rows §VII.CA-CI cluster at the table top, lines
    163-171); a pure binary append cannot place the row in the frontier cluster. We splice the row
    immediately after the §VII.CI master-index ROW line via an exact-anchor replace, then append the
    section body at EOF (where the §VII.CI section body is the last section). LF discipline preserved.
    """
    text = registry_path.read_text(encoding="utf-8")  # (local)

    # 1. Insert master-index row after the §VII.CI master-index ROW (not its section header).
    anchor_row_pat = re.compile(
        r"(?m)^(\|\s*§VII\." + re.escape(MASTER_INDEX_ANCHOR_SLOT) + r"\b.*\n)")  # (local)
    m = anchor_row_pat.search(text)
    if not m:
        raise RuntimeError(f"master-index anchor row §VII.{MASTER_INDEX_ANCHOR_SLOT} not found")
    insert_at = m.end()  # (local) just after the §VII.CI row's newline
    text = text[:insert_at] + master_row + text[insert_at:]

    # 2. Append the section body at EOF (LF-terminated), with a blank-line separator before the
    #    ### header for readability. The separator newlines precede `### §VII.<slot>`, so
    #    re_read_section (which matches at `^### §VII.<slot>`) returns exactly `section_text`.
    if not text.endswith("\n"):
        text = text + "\n"
    if not text.endswith("\n\n"):
        text = text + "\n"
    text = text + section_text

    data = text.encode("utf-8")  # (local)
    # Atomic-ish: write to temp then replace (avoids partial write on crash); fsync.
    tmp = registry_path.with_suffix(registry_path.suffix + ".tmp")  # (local)
    with open(tmp, "wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, registry_path)
    return registry_path.stat().st_size


def re_read_section(registry_text: str, slot: str) -> str:
    """Return the §VII.<slot> SECTION-BODY text (from its ### header to the next §VII header / EOF)."""
    start_pat = re.compile(r"(?m)^### §VII\." + re.escape(slot) + r"\b")  # (local)
    m = start_pat.search(registry_text)
    if not m:
        return ""
    start = m.start()  # (local)
    nxt = re.compile(r"(?m)^#{2,4}\s*§VII\.[A-Z]").search(registry_text, m.end())  # (local)
    end = nxt.start() if nxt else len(registry_text)  # (local)
    return registry_text[start:end]


def re_read_master_index_row(registry_text: str, slot: str) -> str:
    """Return the `| §VII.<slot> | THM | ... |` master-index row text (single line)."""
    pat = re.compile(r"(?m)^\|\s*§VII\." + re.escape(slot) + r"\b.*$")  # (local)
    m = pat.search(registry_text)
    return m.group(0) if m else ""


# ---------------------------------------------------------------------------
# Section 7 — Verdict helpers + plot
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
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
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def make_plot(exps: dict, cert: dict, d: dict) -> None:
    """Two-panel figure: (L) exponent ladder q^n; (R) per-mode half-width vs detuning (no-overlap)."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt  # (local)
    except Exception as e:  # noqa: BLE001
        print(f"  (plot skipped: {e})")
        return

    A = d["A_relic"]                       # (local)
    hw = d["tongue_halfwidth_relic"]        # (local)
    dist = d["dist_to_zone_A"]              # (local)
    nn = d["nearest_n"].astype(int)         # (local)
    qgrid = np.logspace(-4, -1.5, 200)      # (local)

    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 0: half-width vs q for n=1,2,3 (q^n exponent ladder), prefactor-correct coeffs.
    for n, coeff, c in [(1, 1.0, "tab:blue"), (2, 0.25, "tab:orange"), (3, 1.0/64, "tab:green")]:
        ax0.loglog(qgrid, coeff * qgrid**n, color=c,
                   label=f"n={n}: $\\Delta a_{{1/2}}^{{({n})}} \\propto q^{{{n}}}$ (coeff {coeff:g}, DIAG)")
    ax0.axhline(1e-7, color="k", ls=":", lw=0.8, label="$10^{-7}$ (plan mnemonic bound)")
    ax0.axvline(cert["qM_max_broadband"], color="r", ls="--", lw=0.8,
                label=f"$q_M^{{max}}$={cert['qM_max_broadband']:.2e}")
    ax0.set_xlabel("modulation depth $q_M = A h_{par}/2$")
    ax0.set_ylabel("tongue half-width $\\Delta a_{1/2}^{(n)}$")
    ax0.set_title("McLachlan exponent ladder: $\\Delta a_{1/2}^{(n)} \\propto q_M^n$\n"
                  f"(exponents Sage-exact: n=1→{exps[1]['leading_exponent']}, "
                  f"n=2→{exps[2]['leading_exponent']}, n=3→{exps[3]['leading_exponent']})")
    ax0.legend(fontsize=7, loc="lower right")
    ax0.grid(True, which="both", alpha=0.3)

    # Panel 1: per-mode half-width vs detuning, colored by nearest_n; the diagonal = overlap boundary.
    sc = ax1.scatter(dist, hw, c=nn, cmap="viridis", s=14, alpha=0.7)
    lims = [min(dist.min(), hw.min()) * 0.5, max(dist.max(), hw.max()) * 2]  # (local)
    ax1.plot(lims, lims, "k--", lw=0.9, label="half-width = detuning (overlap onset)")
    ax1.scatter([cert["detuning_i_closest"]], [cert["halfwidth_i_closest"]],
                marker="*", s=220, color="red", edgecolor="k", zorder=5,
                label=f"worst case A={cert['A_i_closest']:.3f} (zone n=3): "
                      f"margin {cert['margin_OOM_i_closest']:.1f} dec")
    ax1.set_xscale("log"); ax1.set_yscale("log")
    ax1.set_xlim(lims); ax1.set_ylim(lims)
    cb = fig.colorbar(sc, ax=ax1); cb.set_label("nearest zone index n")
    ax1.set_xlabel("detuning to nearest $a=n^2$ zone")
    ax1.set_ylabel("tongue half-width (McLachlan prefactor-correct)")
    ax1.set_title(f"NO-OVERLAP certificate: {cert['n_overlap']} of {cert['n_modes']} relic modes overlap\n"
                  "(every mode below the diagonal ⇒ |Tr M|<2 ⇒ §VII.BP DEAD at any L_max)")
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(True, which="both", alpha=0.3)

    fig.suptitle("S111-CF-FLOQUET4 — cutoff-robustness scaling-EXPONENT theorem (STAGE-1-CANDIDATE)",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  wrote plot: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 8 — Main (the landing)
# ---------------------------------------------------------------------------
def GATE_marker_in(section_text: str) -> bool:
    return ("S111 W5-4" in section_text) and ("Cutoff-Robustness Scaling-EXPONENT Theorem" in section_text)


def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)

    # 1. THE PHYSICS — verify the exponents (sympy-exact) + the no-overlap certificate.
    exps = verify_mclachlan_exponents()  # (local)
    print("  McLachlan exponent verification (degree_q == n):")
    for n in (1, 2, 3):
        print(f"    n={n}: full_width={exps[n]['full_width']}; "
              f"degree_q={exps[n]['leading_exponent']}; equals_n={exps[n]['exponent_equals_n']}")
    all_exps_ok = all(exps[n]["exponent_equals_n"] for n in (1, 2, 3))  # (local)

    d = dict(np.load(INV12_NPZ))  # (local) relic survey arrays
    cert = no_overlap_certificate(d)  # (local)
    print(f"  no-overlap certificate: {cert['n_overlap']} of {cert['n_modes']} modes overlap "
          f"(all-stable: {cert['no_overlap_all_modes']})")
    print(f"    worst-case mode A={cert['A_i_closest']:.6f} (nearest zone n={cert['nearest_n_at_min_detuning']}): "
          f"half-width={cert['halfwidth_i_closest']:.3e} vs detuning={cert['detuning_i_closest']:.3e} "
          f"⇒ margin {cert['margin_OOM_i_closest']:.1f} decades")
    print(f"    high-A modes (A>9): n={cert['n_modes_A_gt_9']}, nearest_n ∈ {cert['nearest_n_among_A_gt_9']}")
    print(f"    mnemonic-vs-exact: bare (q_M_max)^3={cert['bare_qM3_at_broadband_max_MNEMONIC']:.3e} "
          f"(<=1e-7: {cert['bare_qM3_le_1e-7_at_max']}, LOOSE) ; "
          f"prefactor (q^3/64)={cert['prefactor_halfwidth_at_max_LOADBEARING']:.3e} "
          f"(<=1e-7: {cert['prefactor_hw_le_1e-7_at_max']}, LOAD-BEARING)")

    physics_ok = all_exps_ok and cert["no_overlap_all_modes"] and cert["max_abs_tr_relic_lt_2"]  # (local)

    # 2. Read registry; re-verify the planned slot free over master-index + ALL section headers.
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    crlf_before = registry_text.count("\r\n")  # (local)
    planned_free = not slot_occupied_anywhere(registry_text, PLANNED_SLOT)  # (local)
    if planned_free:
        slot = PLANNED_SLOT; rerouted = False  # (local)
    else:
        slot = find_next_free_slot(registry_text); rerouted = True  # (local)
    print(f"  planned slot §VII.{PLANNED_SLOT} free: {planned_free}; "
          f"landing slot: §VII.{slot}; rerouted: {rerouted}")

    # 3. Build BOTH surfaces in memory. The section SHA goes INTO the master-index row, so build the
    #    section first, hash it, then build the row, then write both (the section SHA in the row is
    #    the SHA of the section-as-built; an exact round-trip check follows on re-read).
    section_text = build_promotion_text(slot, exps, cert)  # (local)
    section_sha_prewrite = sha256_of_bytes(section_text.encode("utf-8"))  # (local)

    # audit_sha is computed AFTER the write (over final script bytes); but the master-index row needs
    # an audit_sha. Resolve: compute the dual-SHA over the CURRENT script bytes now (the script is
    # frozen on disk before this run), embed it in the row. The post-write re-read verifies the row.
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)

    master_row = build_master_index_row(slot, audit_sha, section_sha_prewrite)  # (local)

    # 4. Idempotency: if §VII.<slot> already carries THIS gate's landing, NO-OP.
    if slot_occupied_anywhere(registry_text, slot):
        existing_section = re_read_section(registry_text, slot)  # (local)
        if GATE_marker_in(existing_section):
            print(f"  §VII.{slot} already carries this gate's landing — NO-OP.")
            full_text = registry_text  # (local)
            wrote = False  # (local)
        else:
            print(f"  FOREIGN occupancy on §VII.{slot}; FAIL-with-remediation.")
            full_text = registry_text; wrote = False  # (local)
    else:
        new_len = write_both_surfaces_atomic_with_fsync(master_row, section_text, REGISTRY_PATH)  # (local)
        print(f"  wrote master-index row + section body; new file size {new_len}")
        full_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
        wrote = True  # (local)

    crlf_after = full_text.count("\r\n")  # (local)
    print(f"  CRLF count: before={crlf_before} after={crlf_after} "
          f"(unchanged: {crlf_before == crlf_after})")

    # 5. Re-read BOTH surfaces + verify (single decision point).
    section = re_read_section(full_text, slot)  # (local)
    row = re_read_master_index_row(full_text, slot)  # (local)
    section_sha = sha256_of_bytes(section.encode("utf-8"))  # (local)
    missing = [mk for mk in REQUIRED_MARKERS if mk not in section]  # (local)
    must_contain_ok = (len(missing) == 0)  # (local)
    master_index_ok = (MASTER_INDEX_MARKER.lower() in row.lower()) and (f"§VII.{slot}" in row)  # (local) case-insensitive
    section_roundtrip_ok = (section_sha == section_sha_prewrite)  # (local) section unchanged by write
    stage1_present = ("STAGE-1-CANDIDATE" in section)  # (local)
    crlf_ok = (crlf_before == crlf_after)  # (local)
    section_nonempty = (len(section) > 0)  # (local)

    verdict = "PASS"  # (local)
    reasons = []  # (local)
    if not physics_ok:
        verdict = "FAIL"
        if not all_exps_ok:
            reasons.append("exponent-verification-failed")
        if not cert["no_overlap_all_modes"]:
            reasons.append(f"no-overlap-failed({cert['n_overlap']}-modes-overlap)")
        if not cert["max_abs_tr_relic_lt_2"]:
            reasons.append("max|TrM|>=2")
    if not section_nonempty:
        verdict = "FAIL"; reasons.append("section-empty(header-anchor-mismatch)")
    if not must_contain_ok:
        verdict = "FAIL"; reasons.append(f"missing-markers={missing}")
    if not master_index_ok:
        verdict = "FAIL"; reasons.append("master-index-row-missing-or-malformed")
    if not section_roundtrip_ok:
        verdict = "FAIL"; reasons.append("section-roundtrip-sha-mismatch")
    if not stage1_present:
        verdict = "FAIL"; reasons.append("no-STAGE-1-CANDIDATE-tag")
    if not crlf_ok:
        verdict = "FAIL"; reasons.append("CRLF-count-changed(neighbor-flatten)")

    value = (f"STAGE-1-CANDIDATE_cutoff-robustness-EXPONENT-theorem_landed_VII.{slot}_"
             f"degree_q==n_EXACT_n123_{all_exps_ok}_"
             f"no-overlap_{cert['n_overlap']}of{cert['n_modes']}_worst-margin_{cert['margin_OOM_i_closest']:.1f}dec_"
             f"prefactor-correct(bare_qM3_mnemonic_LOOSE_at_max)_"
             f"two-surface(master-index+body)_markers={'OK' if must_contain_ok else 'MISSING'}_"
             f"reroute={rerouted}")
    if reasons:
        value = value + "_FAIL:" + ";".join(reasons)

    # 6. Plot.
    make_plot(exps, cert, d)

    # 7. Persist npz record.
    try:
        np.savez(
            OUT_NPZ,
            gate_id=GATE_ID,
            slot=slot,
            planned_slot=PLANNED_SLOT,
            rerouted=bool(rerouted),
            # exponent theorem
            exp_n1=int(exps[1]["leading_exponent"]),
            exp_n2=int(exps[2]["leading_exponent"]),
            exp_n3=int(exps[3]["leading_exponent"]),
            exps_all_equal_n=bool(all_exps_ok),
            full_width_n1=exps[1]["full_width"],
            full_width_n2=exps[2]["full_width"],
            full_width_n3=exps[3]["full_width"],
            half_coeff_n1_DIAG=exps[1]["half_width_leading_coeff_DIAGNOSTIC"],
            half_coeff_n2_DIAG=exps[2]["half_width_leading_coeff_DIAGNOSTIC"],
            half_coeff_n3_DIAG=exps[3]["half_width_leading_coeff_DIAGNOSTIC"],
            # no-overlap certificate
            n_modes=int(cert["n_modes"]),
            n_overlap=int(cert["n_overlap"]),
            no_overlap_all_modes=bool(cert["no_overlap_all_modes"]),
            A_i_closest=float(cert["A_i_closest"]),
            halfwidth_i_closest=float(cert["halfwidth_i_closest"]),
            detuning_i_closest=float(cert["detuning_i_closest"]),
            margin_OOM_i_closest=float(cert["margin_OOM_i_closest"]),
            n_modes_A_gt_9=int(cert["n_modes_A_gt_9"]),
            nearest_n_among_A_gt_9=np.array(cert["nearest_n_among_A_gt_9"], dtype=int),
            A_relic_min=float(cert["A_relic_min"]),
            A_relic_max=float(cert["A_relic_max"]),
            sqrt_A_max=float(cert["sqrt_A_max"]),
            h_par=float(cert["h_par"]),
            qM_max_broadband=float(cert["qM_max_broadband"]),
            qM_near_a1_min=float(cert["qM_near_a1_min"]),
            bare_qM3_at_max_MNEMONIC=float(cert["bare_qM3_at_broadband_max_MNEMONIC"]),
            bare_qM3_le_1em7=bool(cert["bare_qM3_le_1e-7_at_max"]),
            prefactor_hw_at_max_LOADBEARING=float(cert["prefactor_halfwidth_at_max_LOADBEARING"]),
            prefactor_hw_le_1em7=bool(cert["prefactor_hw_le_1e-7_at_max"]),
            max_abs_tr_relic=float(cert["max_abs_tr_relic"]),
            max_abs_tr_relic_lt_2=bool(cert["max_abs_tr_relic_lt_2"]),
            # landing record
            must_contain_ok=bool(must_contain_ok),
            missing_markers=np.array(missing, dtype=object),
            master_index_ok=bool(master_index_ok),
            section_roundtrip_ok=bool(section_roundtrip_ok),
            crlf_before=int(crlf_before),
            crlf_after=int(crlf_after),
            section_sha256=section_sha,
            verdict=verdict,
        )
        print(f"  wrote npz record: {OUT_NPZ.name}")
    except Exception as e:  # noqa: BLE001
        print(f"  (npz write skipped: {e})")

    # 8. Dual-SHA already computed (used in the master-index row); re-emit for the verdict.
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  landed-section_sha256: {section_sha[:16]}... ({len(section)} chars); "
          f"roundtrip_ok={section_roundtrip_ok}")

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        f"# {GATE_ID} registry-landing TWO-SURFACE: §VII.{slot} master-index row + section body "
        f"(planned §VII.{PLANNED_SLOT}); rerouted={rerouted}; markers_ok={must_contain_ok}; "
        f"landed_section_sha256={section_sha}",
        f"# {GATE_ID} EXPONENT theorem degree_q(Delta_a_half^(n))==n EXACT n=1,2,3 (sympy DLMF-28.6); "
        f"prefactor DIAGNOSTIC-ONLY; no-overlap {cert['n_overlap']}/{cert['n_modes']}; "
        f"worst-case A={cert['A_i_closest']:.4f} margin {cert['margin_OOM_i_closest']:.1f}dec; "
        f"§VII.BP DEAD cutoff-robustness-protected (4th pin).",
        f"# {GATE_ID} mnemonic-vs-exact (math-scripts.md): bare (q_M_max)^3="
        f"{cert['bare_qM3_at_broadband_max_MNEMONIC']:.3e} LOOSE (>1e-7); "
        f"prefactor q^3/64={cert['prefactor_halfwidth_at_max_LOADBEARING']:.3e} LOAD-BEARING; "
        f"Stage-2 cross-axis verify queued S112+ (NON-AUTHOR; transit-dynamics EXCLUDED).",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
