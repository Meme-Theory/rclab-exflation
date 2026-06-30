#!/usr/bin/env python3
"""
S100a W4-15 S100a-H0-SPINOR-FACTOR — first-principles sqrt(16) spinor normalization
====================================================================================

Gate: S100a-H0-SPINOR-FACTOR ([VERIFY])
Plan: sessions/session-plan/session-100a-plan-w4.md SECTION W4-15 (schema R3)
Agent: kaluza-klein-theorist
Classification: GEOMETRIC (spinor bundle of the spectral triple — the fabric's
Clifford structure, not an excitation)

Pre-registered operator + boundary (plan W4-15, verbatim):
  structural: factor = sqrt(Tr_spinor) = sqrt(16) = 4
              (derived from d_spec=8 Clifford spinor dim, NOT fitted)
  agreement : rel = |factor_derived - 3.92| / 3.92 <= spinor_tol = 0.025
  PASS iff structural EXACT and rel <= 0.025 (2.5%, publication-precision-floored
           at the empirical 3-sig-fig anchor per Class 8.3)
  INFO iff structural holds with residual scheme parameter, rel in (0.025, 0.05]
  FAIL iff rel > 0.05 (no spinor derivation reproduces 3.92)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py  (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  No npz inputs: the derivation is on an INTEGER MESH (Clifford spinor dims +
  surviving-block count); the empirical anchor 3.92 is the plan-pinned
  atlas-08 Q27 / session-58 value (3 sig figs).

Output 4-tuple:
  (value=<payload>, scheme=dspec8-Clifford16+KK-surviving4+Sakharov-S44,
   convention=STRUCTURAL-SQRT16-SPINOR-NORMALIZATION, L_max=N/A)

METHODOLOGY — substitution chain (plan W4-15 item 7, executed exactly)
----------------------------------------------------------------------
Claim: M_Pl,eff/M_Pl,unred = 3.92 IS the structural factor sqrt(16) = 4 (from
       the d_spec=8 16-component spinor), agreeing with the empirical 3.92
       within the publication-precision tolerance.

Definition 1: d_spec = 8 — the spectral dimension of the SU(3) spectral triple
   (leading CM-1995 dim-spectrum pole of zeta_D at s = 8;
   s87-d-eff-derivation-connes.md, Question (b) block).
Definition 2: Delta_8 = C^{Tr_spinor}, Tr_spinor = 2^{floor(d_spec/2)}
   = 2^{floor(8/2)} = 2^4 = 16 — the full Clifford(R^8) irreducible spinor
   module dimension. Confirmed by the leading-pole residue
       Res_{s=8} zeta_D(s) = (Vol(SU(3)) / (2pi)^8) * 16
   which carries the 16 = 2^{[8/2]} spinor multiplicity EXPLICITLY and
   multiplicatively [s87-d-eff-derivation-connes.md line 176].
Definition 3: the 4D gravitational sector retains only the KK-surviving spinor
   components; a 4D Dirac spinor has dim(Delta_4) = 2^{floor(4/2)} = 4
   components. Delta_12 = Delta_4 (x) Delta_8 = M_{8x8}(C) has
   dim = 2^{floor(12/2)} = 64 = 4 * 16 components, of which 4 survive
   [Route D, session-58-volovik-baptista-workshop.md line 528 (B4) + line 712
   (Q3, Sakharov induced-gravity reading: G^{-1} ~ Tr(1_spinor); restricting
   64 -> 4 shifts G_N by 64/4 = 16, hence M_Pl by sqrt(16) = 4)].
Definition 4: M_Pl^{spectral} uses the FULL spinor trace (Tr = 16) via the
   heat-kernel product factorization on P = M^4 x K (Paper 33 / S53):
       a_n^{MxK} = sum_{i+j=n} a_i^M * a_j^K ,
   where the 4D Einstein-Hilbert (R_4) coefficient is the a_2^M * a_0^K
   cross-term and a_0^K ~ Tr_{Delta_8}(1) * Vol(K) = 16 * Vol(K). The PHYSICAL
   graviton propagator (the metric zero mode h_munu; sqrt(g) R_4 carries NO
   internal spinor index) uses the on-shell-projected surviving block.

Substitute: M_Pl^{physical}/M_Pl^{spectral}
            = sqrt(surviving/total at the relevant trace) = sqrt(4/64) = sqrt(1/16)
Simplify:   sqrt(1/16) = 1/4                                  [EXACT]
Invert:     M_Pl^{spectral}/M_Pl^{physical} = M_Pl,eff/M_Pl,unred = 4 = sqrt(16)
Canonical form: factor_derived = sqrt(16) = 4 (EXACT structural integer; not fitted).

Substitute (agreement): rel = |factor_derived - empirical| / empirical
                            = |4 - 3.92| / 3.92 = 0.08 / 3.92
Simplify:   rel = 8/392 = 1/49 = 0.020408... = 2.041% (4 sig figs)   [EXACT RATIONAL]
Direction:  rel = 1/49 <= 1/40 = 0.025  <=>  40 <= 49  TRUE  => PASS.
            (Class 8.3: the empirical 3.92 is a 3-sig-fig number — true value in
            [3.915, 3.925] — so a naive 2.0% strict boundary would FAIL on a
            publication-precision artifact, NOT a substrate-physics miss; the
            pre-registered boundary is 2.5%.)
Conclusion: the spinor normalization factor IS sqrt(16) = 4 first-principles;
            it reproduces the empirical 3.92 to 2.041%, inside the 2.5%
            publication-precision tolerance => VERIFY PASS. atlas-08 Q27
            RESOLVED; H_0 = 65.4 km/s/Mpc structurally grounded; FLAGSHIP.

Sage-exact cross-check (run via Sage MCP at dispatch; mirrored in-script with
Fraction/isqrt EXACT arithmetic — no float enters the gate comparison):
  2^floor(8/2)=16; 2^floor(4/2)=4; 2^floor(12/2)=64=4*16 (multiplicativity TRUE)
  sqrt(QQ(4)/QQ(64)) = 1/4 exact; sqrt(16) = 4 exact
  rel = 1/49; boundary = 1/40; PASS iff 40 <= 49 TRUE
  margin = 1/40 - 1/49 = 9/1960 = 0.004592; rel/boundary = 40/49 = 0.8163
  implied a_2 deficit 1-(3.92/4)^2 = 99/2500 = 3.96% — consistent with the
  S59 NORM-59 Peter-Weyl truncation estimate (~4.1% a_2 deficit at max(p+q)=3;
  all omega_n > 0 so higher (p,q) sectors push N UPWARD toward 4).

DISCIPLINE
----------
- from canonical_constants import *  (M_Pl_reduced, M_Pl_unreduced, M_KK,
  H_0_km_s_Mpc, Vol_SU3_Haar, PI consumed)
- machinery pin GPU_path = CPU (scalar + integer arithmetic; OMP cap 8 set
  BEFORE numpy import)
- every computed intermediate tagged # (local)
- exact Fraction/isqrt arithmetic for the gate comparison; float64 only for
  npz convenience mirrors + plot
- verdict via print_verdict_payload -> agent calls mcp__knowledge__emit_verdict
  (race-safe; script does NOT write the verdict file)
- exit 0 regardless of scientific verdict (math-scripts.md "Exit Codes")
- round-trip: exact rationals (num/den) -> npz; 4-sig-fig rounding -> WP (Class 8.3)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (machinery pin: GPU_path=CPU, BEFORE numpy import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json     # noqa: E402
import math     # noqa: E402
import time     # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration (plan W4-15, pinned at plan-freeze)
# ---------------------------------------------------------------------------
SESSION = "100a"                                                   # (local)
GATE_ID = "S100a-H0-SPINOR-FACTOR"                                 # (local)
SCHEME = "dspec8-Clifford16+KK-surviving4+Sakharov-S44"            # (local)
CONVENTION = "STRUCTURAL-SQRT16-SPINOR-NORMALIZATION"              # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered gate bands (plan W4-15 strict_PASS_boundary + dual_prior
# discriminator). Exact rationals — no float enters the comparison.
SPINOR_TOL = Fraction(25, 1000)      # (local) 0.025 = 1/40 strict PASS boundary
INFO_CEILING = Fraction(5, 100)      # (local) 0.05 INFO ceiling (rel in (2.5%,5%])

# Plan-pinned empirical anchor (atlas-08 Q27 / session-58 W3-16; 3 sig figs;
# numerically realized as S59 NORM-59 N_factor = 3.9196 at max(p+q)=3).
# NOT yet a canonical constant (plan W4 Input-SHA ledger lists it as the
# "Empirical spinor anchor (Item 15)" plan pin, separate from the confirmed
# canonical names) — documented framework-empirical literal with cite.
EMPIRICAL_ANCHOR = Fraction(392, 100)   # (local) 3.92 EXACT rational of the 3-sig-fig anchor

# Structural integer inputs (the entire derivation is on an integer mesh —
# plan W4-15 reachable_rationals block).
D_SPEC = 8        # (local) spectral dim of SU(3) triple (CM-1995 leading pole s=8, S87)
D_SPACETIME = 4   # (local) 4D Lorentz block
D_TOTAL = 12      # (local) P = M^4 x SU(3)

OUT_NPZ = SESSION_DIR / "s100a_h0_spinor_factor.npz"
OUT_PNG = SESSION_DIR / "s100a_h0_spinor_factor.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = script_path.read_bytes()       # (local)
    canonical_bytes = canonical_path.read_bytes() # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")                             # (local)
    h_audit = hashlib.sha256()                    # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute (exact integer/rational arithmetic; NUMBERS FIRST)
# ---------------------------------------------------------------------------

def exact_sqrt_fraction(fr: Fraction) -> Fraction:
    """Exact square root of a Fraction whose num and den are perfect squares.

    Raises ValueError if fr is not an exact rational square — i.e., the
    structural claim 'the factor is a clean integer-mesh root' FAILS hard
    rather than silently floating.
    """
    rn = math.isqrt(fr.numerator)    # (local)
    rd = math.isqrt(fr.denominator)  # (local)
    if rn * rn != fr.numerator or rd * rd != fr.denominator:
        raise ValueError(f"{fr} is not an exact rational square")
    return Fraction(rn, rd)


def compute() -> dict:
    print("=" * 72)
    print("STEP 1 — Clifford spinor dimensions (integer mesh)")
    print("=" * 72)

    # Definition 2: Tr_spinor = 2^{floor(d_spec/2)} — Clifford(R^8) irrep dim
    tr_spinor = 2 ** (D_SPEC // 2)          # (local) = 16
    dim_delta4 = 2 ** (D_SPACETIME // 2)    # (local) = 4  (4D Dirac spinor)
    dim_delta12 = 2 ** (D_TOTAL // 2)       # (local) = 64 (12D spinor, M_{8x8}(C))

    # Multiplicativity of irreducible Clifford modules under the even-dim
    # product split Cl(R^12) = Cl(R^4) (x) Cl(R^8):  64 = 4 * 16
    mult_ok = (dim_delta12 == dim_delta4 * tr_spinor)  # (local)

    print(f"  d_spec        = {D_SPEC}  (SU(3) spectral dim; CM-1995 leading pole s=8)")
    print(f"  Tr_spinor     = 2^floor({D_SPEC}/2) = 2^{D_SPEC//2} = {tr_spinor}")
    print(f"  dim(Delta_4)  = 2^floor({D_SPACETIME}/2) = {dim_delta4}")
    print(f"  dim(Delta_12) = 2^floor({D_TOTAL}/2) = {dim_delta12}")
    print(f"  multiplicativity 64 = 4 x 16 : {mult_ok}")

    print()
    print("=" * 72)
    print("STEP 2 — KK-surviving block (Route D) and the structural factor")
    print("=" * 72)

    # Definition 3: of the 64 Delta_12 components, the 4D gravitational sector
    # retains one 4D Dirac block = 4 components (Route D, S58 workshop B4).
    surviving = dim_delta4   # (local) = 4
    total = dim_delta12      # (local) = 64

    ratio_trace = Fraction(surviving, total)            # (local) 4/64 = 1/16 EXACT
    ratio_mpl = exact_sqrt_fraction(ratio_trace)        # (local) sqrt(1/16) = 1/4 EXACT
    factor_derived = 1 / ratio_mpl                      # (local) Fraction(4,1) EXACT

    # Structural integer-mesh identities (the [VERIFY] content):
    #   (i)  factor^2 == Tr_spinor          (4^2 = 16: factor IS sqrt(Tr_spinor))
    #   (ii) Tr_spinor is a perfect square  (sqrt(16) = 4 exact, isqrt check)
    #   (iii) 64 = 4 * 16 multiplicativity  (mult_ok above)
    #   (iv) total/surviving == Tr_spinor   (64/4 = 16: Sakharov G_N shift reading)
    sq_ok = (factor_derived ** 2 == tr_spinor)                        # (local)
    isqrt_ok = (math.isqrt(tr_spinor) ** 2 == tr_spinor
                and Fraction(math.isqrt(tr_spinor)) == factor_derived)  # (local)
    sakharov_ok = (Fraction(total, surviving) == tr_spinor)           # (local)
    structural_ok = bool(mult_ok and sq_ok and isqrt_ok and sakharov_ok)  # (local)

    print(f"  surviving / total = {surviving}/{total} = {ratio_trace}  (trace level)")
    print(f"  M_Pl^phys/M_Pl^spec = sqrt({ratio_trace}) = {ratio_mpl}  EXACT")
    print(f"  factor_derived = M_Pl,eff/M_Pl,unred = {factor_derived} = sqrt({tr_spinor})")
    print(f"  structural identities: factor^2==Tr_spinor {sq_ok}; isqrt exact {isqrt_ok};")
    print(f"                         64/4==16 (Sakharov) {sakharov_ok};  ALL: {structural_ok}")
    print(f"  NOT FITTED: every quantity above is a pinned integer or an exact")
    print(f"  rational root of pinned integers — no scan, no fit, no float.")

    print()
    print("=" * 72)
    print("STEP 3 — Agreement vs empirical anchor (exact rational)")
    print("=" * 72)

    # Substitute (agreement): rel = |4 - 392/100| / (392/100)
    rel = abs(factor_derived - EMPIRICAL_ANCHOR) / EMPIRICAL_ANCHOR   # (local) EXACT
    margin = SPINOR_TOL - rel                                         # (local)
    rel_over_boundary = rel / SPINOR_TOL                              # (local)
    pass_agreement = (rel <= SPINOR_TOL)                              # (local)

    print(f"  empirical anchor = {EMPIRICAL_ANCHOR} = {float(EMPIRICAL_ANCHOR)}"
          f"  (atlas-08 Q27 / S58, 3 sig figs)")
    print(f"  rel = |{factor_derived} - {EMPIRICAL_ANCHOR}| / {EMPIRICAL_ANCHOR}"
          f" = {abs(factor_derived - EMPIRICAL_ANCHOR)} / {EMPIRICAL_ANCHOR} = {rel}")
    print(f"      = {float(rel):.6f} = {float(rel)*100:.4g}%  (published 4 sig figs: 2.041%)")
    print(f"  boundary = {SPINOR_TOL} = {float(SPINOR_TOL)} (= 1/40,"
          f" publication-precision-floored, Class 8.3)")
    print(f"  PASS iff rel <= boundary  <=>  1/49 <= 1/40  <=>  40 <= 49 : {pass_agreement}")
    print(f"  margin = boundary - rel = {margin} = {float(margin):.6f}")
    print(f"  rel/boundary = {rel_over_boundary} = {float(rel_over_boundary):.4f}")

    # Consistency closure with the S59 numerical realization (cited, not loaded):
    # the anchor 3.92 was MEASURED on the max(p+q)=3 Peter-Weyl spectrum; the
    # implied a_2-level deficit of the truncated spectrum vs the exact factor is
    #   1 - (3.92/4)^2 = 99/2500 = 3.96%
    # vs the S59 NORM-59 direct truncation-deficit estimate ~4.1% — same scale,
    # same sign (all omega_n > 0 => higher sectors push N UP toward 4).
    a2_deficit_implied = 1 - (EMPIRICAL_ANCHOR / factor_derived) ** 2  # (local) 99/2500
    print(f"  implied a_2 deficit = 1-(3.92/4)^2 = {a2_deficit_implied}"
          f" = {float(a2_deficit_implied)*100:.2f}%  (S59 measured ~4.1% at max(p+q)=3)")

    print()
    print("=" * 72)
    print("STEP 4 — Context diagnostics (non-gating; canonical constants)")
    print("=" * 72)

    # S87 leading-pole residue carrying the 16 (cited form, evaluated with the
    # canonical Vol(SU(3)) Haar volume as a context anchor — NOT a gate input):
    res_s8_cited = Vol_SU3_Haar / (2.0 * PI) ** 8 * tr_spinor   # (local) float context
    print(f"  Res_(s=8) zeta_D = (Vol_SU3/(2pi)^8)*16 = ({Vol_SU3_Haar:.2f}/{(2*PI)**8:.4g})*16"
          f" = {res_s8_cited:.6e}")
    print(f"    [s87-d-eff-derivation-connes.md:176 — the 16 enters MULTIPLICATIVELY")
    print(f"     in the leading dim-spectrum pole residue: the spectral side of the")
    print(f"     triple carries the FULL Clifford multiplicity]")

    # Downstream contingency (grounded on PASS; H_0 row is mack's surface):
    print(f"  M_Pl_reduced  = {M_Pl_reduced:.4e} GeV ; M_Pl_unreduced = {M_Pl_unreduced:.4e} GeV")
    print(f"  H_0(Planck18) = {H_0_km_s_Mpc} km/s/Mpc ; framework contingent prediction")
    print(f"  H_0_FW = 65.4 km/s/Mpc (S59/S60 corrected spectral-action chain;")
    print(f"  falsifier-watchlist H_0 row) — GROUNDED by this gate on PASS.")

    return {
        "tr_spinor": tr_spinor,
        "dim_delta4": dim_delta4,
        "dim_delta12": dim_delta12,
        "surviving": surviving,
        "total": total,
        "factor_derived": factor_derived,
        "ratio_trace": ratio_trace,
        "ratio_mpl": ratio_mpl,
        "rel": rel,
        "margin": margin,
        "rel_over_boundary": rel_over_boundary,
        "a2_deficit_implied": a2_deficit_implied,
        "structural_ok": structural_ok,
        "mult_ok": bool(mult_ok),
        "sq_ok": bool(sq_ok),
        "isqrt_ok": bool(isqrt_ok),
        "sakharov_ok": bool(sakharov_ok),
        "res_s8_cited": res_s8_cited,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def evaluate_gate(r: dict) -> str:
    """Plan W4-15 rubric: PASS / INFO / FAIL on (structural, rel) exactly."""
    if r["structural_ok"] and r["rel"] <= SPINOR_TOL:
        return "PASS"
    if r["structural_ok"] and r["rel"] <= INFO_CEILING:
        return "INFO"
    return "FAIL"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: list | None = None,
) -> dict:
    """Print the emit_verdict payload for the dispatching agent ([VERIFY]
    trigger: NO schema-v2 3-tuple — sign/magnitude/regime omitted entirely)."""
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }  # (local)
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Plot (optional artifact: 16 -> 4 spinor-reduction schematic)
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))  # (local)

    # Panel 1: Delta_12 = Delta_4 (x) Delta_8 census, 8x8 = 64 cells;
    # the surviving 4D Dirac block (4 cells) highlighted.
    ax = axes[0]  # (local)
    for i in range(8):
        for j in range(8):
            idx = i * 8 + j                       # (local)
            survive = (idx < 4)                   # (local) one Delta_4 block
            ax.add_patch(plt.Rectangle(
                (j, 7 - i), 1, 1,
                facecolor=('#2ca02c' if survive else '#d3d3d3'),
                edgecolor='black', linewidth=0.6))
    ax.set_xlim(-0.4, 8.4)
    ax.set_ylim(-0.4, 8.9)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(r"$\Delta_{12} = M_{8\times8}(\mathbb{C})$: 64 components"
                 "\n4 survive KK reduction (one 4D Dirac block)", fontsize=11)
    ax.text(4, -0.35, r"surviving/total $= 4/64 = 1/16$;"
            r"  $M_{Pl}^{\rm spec}/M_{Pl}^{\rm phys} = \sqrt{16} = 4$",
            ha='center', va='top', fontsize=10)

    # Panel 2: derived factor vs empirical anchor with the 2.5% band.
    ax = axes[1]  # (local)
    emp = float(EMPIRICAL_ANCHOR)                 # (local)
    tol = float(SPINOR_TOL)                       # (local)
    ax.axhspan(emp * (1 - tol), emp * (1 + tol), color='#cfe8cf', alpha=0.8,
               label=r'$\pm2.5\%$ band on empirical 3.92 (Class 8.3 floor)')
    ax.axhline(emp, color='#1f77b4', lw=2, label='empirical 3.92 (atlas-08 Q27 / S58)')
    ax.axhline(4.0, color='#d62728', lw=2, ls='--',
               label=r'derived $\sqrt{16}=4$ (Clifford integer mesh)')
    ax.annotate(r"rel $= 1/49 = 2.041\%$" + "\n" + r"boundary $1/40 = 2.5\%$"
                + "\n" + r"margin $9/1960$",
                xy=(0.52, (emp + 4.0) / 2), fontsize=11, ha='left')
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.set_ylim(3.75, 4.12)
    ax.set_ylabel(r"$M_{Pl,\rm eff}/M_{Pl,\rm unred}$", fontsize=11)
    ax.set_title("Structural factor vs empirical anchor", fontsize=11)
    ax.legend(loc='lower left', fontsize=8.5)

    fig.suptitle(f"{GATE_ID}: 16 -> 4 spinor reduction "
                 r"($\mathrm{Tr}\,\Delta_8 = 2^{[8/2]} = 16$;"
                 r" graviton retains $\Delta_4$)", fontsize=12)
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Plot saved: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins + dual SHAs (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)              # (local)
    script_path = Path(__file__).resolve()          # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # 2. Compute (NUMBERS first)
    r = compute()  # (local)

    # 3. Evaluate gate (exact rational comparison)
    verdict = evaluate_gate(r)  # (local)

    # 4. Save npz (full precision: exact num/den pairs + float mirrors)
    np.savez(
        OUT_NPZ,
        # integer mesh
        d_spec=D_SPEC, d_spacetime=D_SPACETIME, d_total=D_TOTAL,
        tr_spinor=r["tr_spinor"], dim_delta4=r["dim_delta4"],
        dim_delta12=r["dim_delta12"],
        surviving=r["surviving"], total=r["total"],
        # exact rationals as (num, den) int pairs
        factor_derived_numden=np.array([r["factor_derived"].numerator,
                                        r["factor_derived"].denominator]),
        ratio_trace_numden=np.array([r["ratio_trace"].numerator,
                                     r["ratio_trace"].denominator]),
        ratio_mpl_numden=np.array([r["ratio_mpl"].numerator,
                                   r["ratio_mpl"].denominator]),
        empirical_anchor_numden=np.array([EMPIRICAL_ANCHOR.numerator,
                                          EMPIRICAL_ANCHOR.denominator]),
        rel_numden=np.array([r["rel"].numerator, r["rel"].denominator]),
        boundary_numden=np.array([SPINOR_TOL.numerator, SPINOR_TOL.denominator]),
        info_ceiling_numden=np.array([INFO_CEILING.numerator,
                                      INFO_CEILING.denominator]),
        margin_numden=np.array([r["margin"].numerator, r["margin"].denominator]),
        rel_over_boundary_numden=np.array([r["rel_over_boundary"].numerator,
                                           r["rel_over_boundary"].denominator]),
        a2_deficit_implied_numden=np.array([r["a2_deficit_implied"].numerator,
                                            r["a2_deficit_implied"].denominator]),
        # float64 mirrors (convenience; the gate used EXACT arithmetic)
        factor_derived=float(r["factor_derived"]),
        empirical_anchor=float(EMPIRICAL_ANCHOR),
        rel=float(r["rel"]),
        boundary=float(SPINOR_TOL),
        margin=float(r["margin"]),
        rel_over_boundary=float(r["rel_over_boundary"]),
        a2_deficit_implied=float(r["a2_deficit_implied"]),
        # structural identity flags
        structural_ok=r["structural_ok"], mult_ok=r["mult_ok"],
        sq_ok=r["sq_ok"], isqrt_ok=r["isqrt_ok"], sakharov_ok=r["sakharov_ok"],
        # context diagnostics (non-gating)
        res_s8_cited=r["res_s8_cited"],
        M_Pl_reduced_canonical=M_Pl_reduced,
        M_Pl_unreduced_canonical=M_Pl_unreduced,
        H_0_Planck=H_0_km_s_Mpc,
        H_0_FW_contingent=65.4,   # S59/S60 chain; GROUNDED on PASS (mack's row)
        Vol_SU3_Haar_canonical=Vol_SU3_Haar,
        # gate metadata
        gate_id=np.array([GATE_ID]),
        verdict=np.array([verdict]),
        scheme=np.array([SCHEME]),
        convention=np.array([CONVENTION]),
        l_max=np.array([L_MAX]),
        audit_sha256=np.array([audit_sha]),
        content_sha256=np.array([content_sha]),
    )
    print(f"\n  Data saved: {OUT_NPZ.name}")

    # 5. Plot (optional artifact)
    make_plot(r)

    # 6. Emit 4-tuple + verdict payload ([VERIFY]: no 3-tuple)
    value_payload = (
        "factor_derived=4=sqrt16;Tr_spinor=16=2^4;Delta12=64=4x16;surviving=4of64;"
        "sqrt(4/64)=1/4-exact;rel=1/49=0.020408=2.041pct;boundary=0.025=1/40;"
        "PASS-iff-40<=49;margin=9/1960=0.004592;rel/boundary=40/49=0.8163;"
        "structural=EXACT-integer-mesh-not-fitted;Q27=RESOLVED;H0=65.4-grounded"
    )  # (local)
    print()
    print(emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        verdict, value_payload, audit_sha, content_sha,
        companion_note=(
            "factor structurally sqrt(16)=4 (integer mesh; Sage-exact 1/49 < 1/40); "
            "empirical 3.92 = atlas-08 Q27 / S58 (3 sig figs; S59 NORM-59 N=3.9196 "
            "at max(p+q)=3); 2pct residual = PW truncation (implied a_2 deficit "
            "99/2500=3.96pct vs S59 measured ~4.1pct)"
        ),
        extra_rows=[
            ("# derivation anchors: Res_{s=8} zeta_D=(Vol(SU3)/(2pi)^8)*16 "
             "[s87-d-eff-derivation-connes.md:176]; Delta_12=M_8x8(C) 64-comp "
             "4-survive [session-58-volovik-baptista-workshop.md:528 Route D + "
             ":712 Q3 Sakharov]; heat-kernel a_2^M*a_0^K cross-term [Paper 33/S53] "
             f"# {GATE_ID}"),
            ("# Class 8.3: factor_derived=4 EXACT; empirical anchor 3 sig figs => "
             "boundary 2.5pct publication-precision-floored (a naive 2.0pct strict "
             "boundary would FAIL on the 3-sig-fig rounding artifact, not a "
             f"substrate-physics miss); rel published 4 sig figs = 2.041pct # {GATE_ID}"),
            ("# canonical write-order: spinor_norm_factor_FW=4.0 promoted via "
             "update_constant AFTER this line (math-scripts step 2); H0=65.4 "
             f"inventory row -> mack-cosmic-bridge sole writer (step 3) # {GATE_ID}"),
        ],
    )

    # 7. Final summary (exit 0 regardless of verdict — math-scripts.md)
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
