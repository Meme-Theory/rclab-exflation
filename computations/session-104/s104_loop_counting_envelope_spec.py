"""S104-LOOP-COUNTING-ENVELOPE-SPEC — SPEC-ONLY gate (Wave 5, item 4).

Classify the Zhong 2604.27585 loop-counting finite-size exponent as EITHER
  (A) Level-2-BINDING  — an HKR/Connes-Karoubi image binding Level-1 with a
      DEFINED c_continuum (genuinely distinct lab-anchored derivation of the
      substrate's L^{-alpha} truncation envelope; registry-eligible), OR
  (B) Level-2-NON-binding — reduces to the MANDATORY-K=3 multiplicative-
      normalization-cancellation identity f^{(L_max)} = w(L_max).g(K); no HKR
      image; c_continuum undefined; registry-PASS-INELIGIBLE.

NO numerical envelope exponent is fitted this wave. The deliverable is the
SPEC: the (A)/(B) binding-class determination under the PRE-REGISTERED
discriminator, the named c_continuum reference (or its recorded absence), and
a 4-field S105 binding-determination compute spec.

Composed-with canonical state (verified via knowledge MCP, NOT recomputed):
  - S94-MULT-NORM-CANCELLATION-K3  : PASS, MANDATORY K=3 (math-scripts.md
    §"Multiplicative-normalization cancellation invariants").
  - §VII.AF.1                      : PROVEN, Pillar III<->IV HKR bridge, L^{-3}
    Level-2-BINDING at d=4 substrate-distance-1 pole s=3, match/envelope=0.0950.
  - W16 Layer-2-Non-Binding Bare-Decomposition Wall: bare L^{-alpha} on
    Tr(D_K^{-2s}) with NO HKR image to a partner-pillar continuum observable
    DOES NOT bind Level-1; registry-PASS requires an explicit HKR/Connes-Karoubi
    bridge map citation on ||HKR(c_L) - c_continuum||.

Substrate-first framing (phononic-framing.md): the lab skin-effect acoustic
lattice is a PROJECTION of the substrate truncation, never the other way
around. The substrate IS the finite-L spectral triple whose moments are robust;
Zhong's lattice MODELS a simplified shadow of that robustness.

GEOMETRIC. CPU-only (string-valued spec record + schematic plot; no linear
algebra). Verdict emitted via the race-safe emit_verdict knowledge-MCP tool;
this script PRINTS the payload via print_verdict_payload.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (import discipline; tau_fold anchors the spectral triple) ---
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import tau_fold  # noqa: E402  (single anchor; no hardcoded framework constant)

# ----------------------------------------------------------------------------
# Gate identity (read by print_verdict_payload)
# ----------------------------------------------------------------------------
SESSION = "S104"
GATE_ID = "S104-LOOP-COUNTING-ENVELOPE-SPEC"
SCHEME = "LOOP-COUNTING-LEVEL-2-BINDING-DISCRIMINATOR-SPEC"
CONVENTION = "SUBSTRATE-IS-TRUNCATION-ENVELOPE-NAMING"
L_MAX = "N/A"  # structural (HKR-image existence), not a single-L_max evaluation

OUT_DIR = Path(__file__).resolve().parent
NPZ_PATH = OUT_DIR / "s104_loop_counting_envelope_spec.npz"
PNG_PATH = OUT_DIR / "s104_loop_counting_envelope_spec.png"

# Input files (content-pinned at runtime for the audit SHA).
CANONICAL_CONSTANTS = OUT_DIR.parent / "_shared" / "canonical_constants.py"
ZHONG_PDF = (
    OUT_DIR.parent.parent
    / "downloads"
    / "research-sweep-s103"
    / "topological-matter-exotics"
    / "10_Zhong_Universal-Spectral-Moments-Dispersive-Proliferative-Transition.pdf"
)


def _sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def _sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: "list[str] | None" = None,
) -> dict:
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the race-safe
    knowledge-MCP emit_verdict tool (gate-verdicts.md §"Race-Safe Emission"). The
    script does NOT write the verdict file; it prints the delimited JSON the agent
    extracts. Keyed to the module-level identity constants. (Inline per the W5-2
    sibling convention, computations/session-104/s104_bmv_sn_contrast_spec.py:468-490.)
    """
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


# ----------------------------------------------------------------------------
# SPEC RECORD — the binding-class determination (string-valued; no bridge numerics)
# ----------------------------------------------------------------------------
# Step 1 (substrate L_max-robustness, MANDATORY-K=3): f^{(L_max)}(K) = w(L_max).g(K),
#   g(K) L_max-INDEPENDENT; any log-derivative L_n[f] = d^n ln f/d(ln K)^n annihilates
#   w(L_max). The ROBUST quantity is a dimensionless ratio/log-derivative in which the
#   multiplicative prefactor CANCELS EXACTLY -> the L_max-plateau is a STRUCTURAL IDENTITY,
#   not a converging difference. There is NO c_continuum: the substrate ratio is
#   IDENTICALLY 1 (the L-dependence vanishes by cancellation, it does not converge to a limit).
substrate_robustness_mechanism = "multiplicative-cancellation_ratio_w(L_max)_cancels_c_continuum_identically_1"  # (local)

# Step 3 (Zhong loop-counting law, read from the ON-DISK PDF, Eqs. 1-4):
#   Tr H^m = sum_{|O|=m} w(O)  over length-m closed walks (loops) on the lattice  (Eq. 1-2)
#   per-site moment M_m := (1/N) Tr H^m  ->  w_m  as L->inf   (w_m = fully-sampled bulk loop weight)
#   relative error r(m,L) := |M_m - w_m| / w_m = (|Omega_e|/N).(delta-bar_m / w_m)   (Eq. 3)
#   scaling law r(m,L) ∝ f(m)/L ,  f(m) ∝ m^2  in the |H_ii|>>|H_i!=j| regime          (Eq. 4)
zhong_observable = "r(m,L)=|M_m - w_m|/w_m  (normalized FINITE-to-CONTINUUM DIFFERENCE; M_m=(1/N)TrH^m)"  # (local)
zhong_c_continuum = "w_m = thermodynamic-limit bulk loop weight (DEFINED, nonzero; M_m -> w_m as L->inf)"  # (local)
zhong_envelope_exponent_symbolic = "L^{-1} (r ∝ f(m)/L; f(m) ∝ m^2 large-on-site regime)"  # (local)
zhong_operator_hermiticity = "NON-Hermitian H (skin-effect lattice; directed-loop weight w(O) on a non-reciprocal graph)"  # (local)

# Step 4 (substitution — the discriminator, evaluated STRUCTURALLY this wave):
#   Substitute the substrate factorization f^{(L_max)}=w(L_max).g(K) into Zhong's r(m,L).
#   Zhong's robust observable is r = ||M_m(finite) - w_m(continuum)|| / w_m: a NORMALIZED
#   DIFFERENCE from a DEFINED nonzero limit w_m, NOT a log-derivative of a multiplicatively-
#   factored trace. The missing-boundary-loop deficit delta-bar_m is a genuine boundary-shell
#   shortfall RELATIVE TO the bulk reference w_m -- it is NOT the w(L_max) prefactor's
#   L-dependence cancelling in a ratio.
#   => Case (B) (reduces to the cancellation identity) is FALSIFIED: r does NOT reduce to the
#      cancellation identity; w_m is a DEFINED c_continuum distinct from "the substrate ratio
#      identically 1." The two robustness mechanisms are STRUCTURALLY DIFFERENT.
case_B_reduction = False  # loop-counting r(m,L) does NOT reduce to the multiplicative-cancellation identity
case_B_reason = "r=||M_m-w_m||/w_m is a normalized DIFFERENCE from a DEFINED limit w_m, not a cancelling-prefactor log-derivative; delta-bar_m is a boundary-shell deficit relative to w_m, not the w(L_max) L-dependence"  # (local)

#   Case (A) (Level-2-BINDING) requires BOTH: (a) the ||.-c_continuum|| SHAPE with defined
#   c_continuum [SATISFIED: c_continuum = w_m], AND (b) an HKR / Connes-Karoubi / K-theory
#   image binding Zhong's lab M_m to a substrate-IS Level-1 cohomology class [NOT NAMEABLE
#   at spec-time -- see the two obstructions below].
case_A_shape_satisfied = True  # ||M_m - w_m||/w_m HAS the binding SHAPE; c_continuum = w_m defined nonzero
# Obstruction (1) — HERMITICITY MISMATCH: the loop-counting moment definition
#   Tr H^m = sum directed-loop weights is NON-Hermitian-SPECIFIC. On the Hermitian D_K
#   (AZ class BDI, T^2=+1, self-adjoint) the directed-loop weight over a non-reciprocal
#   graph has NO analog: the skin effect (extensive boundary accumulation from
#   non-reciprocity) does not exist for self-adjoint D_K. The robust observable's very
#   DEFINITION lacks a Hermitian-D_K image.
obstruction_hermiticity = "Tr H^m directed-loop weight is non-Hermitian-specific; Hermitian D_K (BDI) has no non-reciprocal directed-loop / skin-effect analog"  # (local)
# Obstruction (2) — NO NAMED HKR IMAGE: §VII.AF.1's binding envelope is L^{-3} via an
#   explicit HKR L_max->inf boundary map ∘ Connes-Karoubi pairing at Mellin pole s=3
#   (HP^1 <-> Peotta-Toermae BZ-trace cohomology class). Zhong supplies c_continuum=w_m
#   and an L^{-1} rate but NO HKR/Connes-Karoubi/K-theory boundary map from w_m to a
#   substrate Level-1 class. Whether the lab M_m IS the HKR image of a substrate
#   cohomology class is UNDETERMINED at spec-time and cannot be settled WITHOUT the
#   numerical reduction (does substituting f^{(L_max)}=w.g into a NORMALIZED moment
#   reproduce alpha_loop, and does that L^{-1} carry an HKR image, or is it the bare
#   Mellin-truncation rate W16 forbids?).
obstruction_no_hkr = "no HKR/Connes-Karoubi/K-theory map from w_m to a substrate Level-1 cohomology class is nameable at spec-time; §VII.AF.1 binding needs the explicit HP^1<->BZ-trace image"  # (local)
case_A_hkr_image_nameable = False  # the (A)-defining HKR image cannot be NAMED at spec-time

# ----------------------------------------------------------------------------
# Spec-completeness 3-conjunct boolean (the operator):
#   SPEC_complete := binding_class_determined AND c_continuum_named_or_absent AND s105_spec_emitted
# ----------------------------------------------------------------------------
# binding_class_determined := the exponent is CLASSIFIED (A) or (B) per the discriminator.
#   Case (B) is FALSIFIED (case_B_reduction=False). Case (A) SHAPE is satisfied but its
#   defining HKR-image clause is NOT settleable at spec-time (case_A_hkr_image_nameable=False).
#   => the exponent is candidate-(A)-on-STRUCTURE but the decisive (A)-vs-(B) SETTLEMENT is
#      UNDECIDED at spec-time -> binding_class_determined = False (the pre-registered INFO
#      intermediate: HKR-image existence cannot be settled without the numerical reduction).
binding_class_determined = (case_B_reduction is True) or (case_A_shape_satisfied and case_A_hkr_image_nameable)
binding_class_token = "candidate-A-on-structure_HKR-image-UNDECIDED-at-spec-time_pending-numerical-reduction"

# c_continuum_named_or_absent := (A) c_continuum named OR (B) recorded absent.
#   c_continuum = w_m IS NAMED (the thermodynamic-limit bulk loop weight). Satisfied.
c_continuum_named_or_absent = True
c_continuum_reference = zhong_c_continuum  # "w_m = thermodynamic-limit bulk loop weight (DEFINED, nonzero)"

# s105_spec_emitted := the 4-field (what/inputs/gate/effort) S105 compute spec is written
#   (to this .npz AND the WP). Satisfied by this script + the WP §W5-4 section.
s105_what = "Numerical binding determination: substitute the substrate factorization f^{(L_max)}=w(L_max).g(K) into a NORMALIZED moment observable and test (i) does it reproduce a finite-to-continuum DIFFERENCE r∝L^{-alpha} with a DEFINED c_continuum (NOT identically 1), and (ii) does that L^{-alpha} carry an HKR/Connes-Karoubi image to a substrate Level-1 cohomology class (Case A) or reduce to the bare Mellin-truncation rate W16 forbids (Case B)?"  # (local)
s105_inputs = "L_max-scan of the substrate D_K normalized moments over [10, Friedrich-Baer cutoff] (JOINT-CONSIDERATION with S104-VIIAM-L11-ANCHOR L=11 + S104-BRANCH-IV-DIRECT-L1314 {12,13,14} -- NO double-schedule); §VII.AF.1 L^{-3} envelope SHAPE as the binding template; W16 wall as the ineligibility criterion; Zhong Eqs. 1-4 as the lab observable definition (any a_n citation carries a_n^{Mellin}/a_n^{Pauli-Villars} per regulator-pin-discipline.md)"  # (local)
s105_gate = "PASS=(A) Level-2-BINDING (HKR image named + defined c_continuum != 1) -> S105 registry-landing compute (a genuinely distinct lab-anchored envelope derivation); INFO/(B)=Level-2-NON-binding (reduces to cancellation identity OR no HKR image nameable) -> confirm-internal note, the envelope question is internal/not-bridgeable, NO registry landing"  # (local)
s105_effort = "1 compute gate (normalized-moment L_max-scan + HKR-image existence test); a (B)/internal outcome reduces it to a confirm-internal note"  # (local)
s105_spec_emitted = True

spec_complete = bool(binding_class_determined and c_continuum_named_or_absent and s105_spec_emitted)

# ----------------------------------------------------------------------------
# Verdict mapping (PRE-REGISTERED rubric, §W5-4):
#   PASS = binding_class_determined (clean A or B) AND c_continuum_named_or_absent AND s105_spec_emitted
#   INFO = the exponent is STATEABLE as an envelope candidate but the binding-class
#          discriminator is UNDECIDED at spec-time (HKR-image existence cannot be settled
#          without the numerical reduction) -> registry-INCOMPLETE-PENDING; S105 prerequisite
#          = the numerical reduction f^{(L_max)}=w.g vs alpha_loop.
#   FAIL = neither a binding HKR image NOR a reduction to the cancellation identity is
#          nameable (no substrate analog of the loop-counting moment on Hermitian D_K).
# A FAIL would require BOTH case_A_shape and a Case-B reduction to be impossible to even
# STATE. Here Case (A) is STATEABLE-as-candidate (shape satisfied, c_continuum named) and
# Case (B) is decisively FALSIFIED -- the construction IS mappable as a candidate, so NOT FAIL.
# The decisive (A)/(B) SETTLEMENT is HKR-undecidable at spec-time -> INFO (the pre-registered
# intermediate), NOT a clean PASS.
if spec_complete:
    verdict = "PASS"
elif (case_A_shape_satisfied or (case_B_reduction is False)) and c_continuum_named_or_absent and s105_spec_emitted:
    # construction is mappable-as-candidate (stateable) but the A/B settlement is undecided
    verdict = "INFO"
else:
    verdict = "FAIL"

# ----------------------------------------------------------------------------
# .npz record (string-valued spec; the (A)/(B) token + named c_continuum)
# ----------------------------------------------------------------------------
np.savez(
    NPZ_PATH,
    gate_id=GATE_ID,
    verdict=verdict,
    scheme=SCHEME,
    convention=CONVENTION,
    tau_fold_anchor=float(tau_fold),
    # spec-completeness booleans
    binding_class_determined=bool(binding_class_determined),
    c_continuum_named_or_absent=bool(c_continuum_named_or_absent),
    s105_spec_emitted=bool(s105_spec_emitted),
    spec_complete=bool(spec_complete),
    # binding-class determination tokens
    binding_class_token=binding_class_token,
    case_B_reduction=bool(case_B_reduction),
    case_B_reason=case_B_reason,
    case_A_shape_satisfied=bool(case_A_shape_satisfied),
    case_A_hkr_image_nameable=bool(case_A_hkr_image_nameable),
    obstruction_hermiticity=obstruction_hermiticity,
    obstruction_no_hkr=obstruction_no_hkr,
    # the named c_continuum reference (NOT absent)
    c_continuum_reference=c_continuum_reference,
    c_continuum_status="NAMED (w_m, defined nonzero) -- distinct from substrate ratio identically 1",
    # the two mechanisms contrasted
    substrate_robustness_mechanism=substrate_robustness_mechanism,
    zhong_observable=zhong_observable,
    zhong_envelope_exponent_symbolic=zhong_envelope_exponent_symbolic,
    zhong_operator_hermiticity=zhong_operator_hermiticity,
    # S105 4-field spec
    s105_what=s105_what,
    s105_inputs=s105_inputs,
    s105_gate=s105_gate,
    s105_effort=s105_effort,
    # adjacency / joint-consideration
    adjacency_note="JOINT-CONSIDERATION (dedup-ledger (c), NO shared pins) with S104-VIIAM-L11-ANCHOR + S104-BRANCH-IV-DIRECT-L1314 (closed PRE-REG-INC this session; Sym^13/14 irrep wall, Gelfand-Tsetlin (p,0) builder CF routes to S105); loop-counting alpha and Friedrich-Baer envelope NOT double-scheduled at S105 plan-freeze",
    composed_with="S94-MULT-NORM-CANCELLATION-K3 (PASS,K=3); VII.AF.1 (L^-3 Level-2-binding); W16 Layer-2-Non-Binding Bare-Decomposition Wall",
)

# ----------------------------------------------------------------------------
# .png schematic — loop-counting envelope route vs multiplicative-cancellation identity
# ----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.4))

# Panel A: the two robustness mechanisms contrasted
axL = axes[0]
axL.axis("off")
axL.set_title("Binding-class discriminator: two robustness mechanisms", fontsize=11, fontweight="bold")
axL.text(
    0.02, 0.95,
    "SUBSTRATE (Case-B candidate) — multiplicative cancellation\n"
    r"  $f^{(L_{max})}(K) = w(L_{max})\cdot g(K)$,  $g$ $L_{max}$-INDEP" "\n"
    r"  $\frac{d^n \ln f}{d(\ln K)^n}$ annihilates $w(L_{max})$  (K=3 IDENTITY)" "\n"
    "  robust = dimensionless RATIO; prefactor CANCELS exactly\n"
    r"  $\Rightarrow$ NO $c_{continuum}$: substrate ratio $\equiv 1$" "\n"
    "  (L-dependence VANISHES, does not converge to a limit)",
    transform=axL.transAxes, va="top", ha="left", fontsize=9.0,
    family="monospace",
    bbox=dict(boxstyle="round", fc="#eef3ff", ec="#3a5a9a"),
)
axL.text(
    0.02, 0.50,
    "ZHONG loop-counting (Case-A signature) — convergence\n"
    r"  $M_m := \frac{1}{N}\mathrm{Tr}\,H^m \to w_m$  as $L\to\infty$" "\n"
    r"  $r(m,L) = \frac{|M_m - w_m|}{w_m} \propto \frac{f(m)}{L}$,  $f(m)\propto m^2$" "\n"
    "  robust = normalized DIFFERENCE from a DEFINED limit\n"
    r"  $\Rightarrow$ $c_{continuum} = w_m$ DEFINED, nonzero" "\n"
    r"  has the $\|\cdot - c_{continuum}\|$ binding SHAPE",
    transform=axL.transAxes, va="top", ha="left", fontsize=9.0,
    family="monospace",
    bbox=dict(boxstyle="round", fc="#fff0ee", ec="#9a3a3a"),
)
axL.text(
    0.02, 0.10,
    "Case (B) FALSIFIED: r is a normalized DIFFERENCE, not a\n"
    "cancelling-prefactor log-derivative. NOT the K=3 identity.",
    transform=axL.transAxes, va="top", ha="left", fontsize=8.6, color="#7a1f1f",
)

# Panel B: the (A)/(B) decision tree + the spec-time obstruction
axR = axes[1]
axR.axis("off")
axR.set_title("(A)/(B) settlement: HKR-image gate (UNDECIDED at spec-time)", fontsize=11, fontweight="bold")
axR.text(
    0.02, 0.95,
    "(A) Level-2-BINDING requires BOTH:\n"
    r"   (a) $\|\cdot - c_{continuum}\|$ shape, $c_{continuum}$ defined  $\rightarrow$ SATISFIED ($w_m$)" "\n"
    "   (b) HKR/Connes-Karoubi image  ->  substrate Level-1 class\n"
    "                                         ->  NOT NAMEABLE @ spec-time",
    transform=axR.transAxes, va="top", ha="left", fontsize=9.0, family="monospace",
    bbox=dict(boxstyle="round", fc="#f2fff2", ec="#3a9a4a"),
)
axR.text(
    0.02, 0.62,
    "Obstruction (1) HERMITICITY:\n"
    r"  $\mathrm{Tr}\,H^m$ = directed-loop weights on a non-reciprocal graph" "\n"
    "  is NON-Hermitian-specific; Hermitian $D_K$ (BDI) has\n"
    "  no skin-effect / directed-loop analog.\n\n"
    "Obstruction (2) NO HKR IMAGE:\n"
    r"  §VII.AF.1 binds via explicit HKR $L\to\infty$ ∘ Connes-" "\n"
    r"  Karoubi @ $s=3$ (HP$^1\leftrightarrow$ BZ-trace). Zhong gives $w_m$" "\n"
    "  + $L^{-1}$ but NO such map -> W16 ineligibility risk.",
    transform=axR.transAxes, va="top", ha="left", fontsize=8.8, family="monospace",
    bbox=dict(boxstyle="round", fc="#fffdf0", ec="#9a8a3a"),
)
axR.text(
    0.02, 0.12,
    "VERDICT: INFO  (registry-INCOMPLETE-PENDING)\n"
    "binding class = candidate-(A)-on-structure; HKR-image\n"
    "UNDECIDED. S105 prereq = numerical reduction f=w·g vs " r"$\alpha_{loop}$.",
    transform=axR.transAxes, va="top", ha="left", fontsize=9.0, color="#1f4f7a", fontweight="bold",
    bbox=dict(boxstyle="round", fc="#eef6ff", ec="#1f4f7a"),
)

fig.suptitle(
    f"{GATE_ID}  —  loop-counting envelope route vs multiplicative-cancellation identity\n"
    "substrate IS the robust spectral triple; the skin-effect acoustic lattice is its PROJECTION (IS not IN)",
    fontsize=10.5,
)
fig.tight_layout(rect=(0, 0, 1, 0.93))
fig.savefig(PNG_PATH, dpi=130)
plt.close(fig)

# ----------------------------------------------------------------------------
# dual-SHA + verdict payload
# ----------------------------------------------------------------------------
# content_sha256 = SHA over the script source (per audit_discriminators content_sha256_inputs=[script]).
this_script_text = Path(__file__).read_text(encoding="utf-8")
content_sha = _sha256_text(this_script_text)

# audit_sha256 = closure over the ordered input-pin map (script + canonical + pinmap).
input_pin_map = {
    "01_script_sha256": content_sha,
    "02_canonical_constants_sha256": _sha256_file(CANONICAL_CONSTANTS),
    "03_zhong_pdf_sha256": _sha256_file(ZHONG_PDF),
    "04_gate_id": GATE_ID,
    "05_scheme": SCHEME,
    "06_convention": CONVENTION,
    "07_verdict": verdict,
    "08_binding_class_token": binding_class_token,
    "09_case_B_reduction": str(case_B_reduction),
    "10_case_A_hkr_image_nameable": str(case_A_hkr_image_nameable),
    "11_c_continuum_reference": c_continuum_reference,
    "12_tau_fold": f"{float(tau_fold):.6f}",
}
audit_sha = _sha256_text(json.dumps(input_pin_map, separators=(",", ":"), sort_keys=True))

# log input SHAs in the first stdout lines (gate-verdicts.md §"During computation")
print(f"[INPUT-SHA] canonical_constants.py = {input_pin_map['02_canonical_constants_sha256']}")
print(f"[INPUT-SHA] Zhong_2604.27585.pdf    = {input_pin_map['03_zhong_pdf_sha256']}")
print(f"[INPUT-SHA] script (content_sha256) = {content_sha}")
print(f"[CLOSURE]   audit_sha256            = {audit_sha}")
print()
print(f"[SPEC] binding_class_determined = {binding_class_determined}")
print(f"[SPEC] case_B_reduction         = {case_B_reduction}  (Case-B reduction to cancellation identity)")
print(f"[SPEC] case_A_shape_satisfied   = {case_A_shape_satisfied}  (||.-c_continuum|| shape; c_continuum=w_m)")
print(f"[SPEC] case_A_hkr_image_nameable= {case_A_hkr_image_nameable}  (HKR image nameable at spec-time)")
print(f"[SPEC] c_continuum_named_or_absent = {c_continuum_named_or_absent}  (named: w_m)")
print(f"[SPEC] s105_spec_emitted        = {s105_spec_emitted}")
print(f"[SPEC] spec_complete            = {spec_complete}")
print(f"[SPEC] binding_class_token      = {binding_class_token}")
print()
print(f"[ARTIFACT] {NPZ_PATH}")
print(f"[ARTIFACT] {PNG_PATH}")
print()

# Descriptive value payload (no single-quote chars; the tool wraps value='...')
value_payload = (
    f"verdict={verdict};binding_class_determined={binding_class_determined};"
    f"binding_class_token={binding_class_token};"
    f"case_B_reduction_to_cancellation_identity={case_B_reduction}_FALSIFIED;"
    f"case_A_shape_satisfied={case_A_shape_satisfied}_c_continuum=w_m_DEFINED;"
    f"case_A_HKR_image_nameable_at_spec_time={case_A_hkr_image_nameable};"
    f"c_continuum_named_or_absent={c_continuum_named_or_absent}_NAMED_w_m;"
    f"s105_spec_emitted={s105_spec_emitted};"
    f"obstruction1=hermiticity_TrH^m_non-Hermitian-specific_no_Hermitian_D_K_directed-loop_analog;"
    f"obstruction2=no_HKR_Connes-Karoubi_map_w_m_to_substrate_Level1_class;"
    f"registry=INCOMPLETE-PENDING_S105prereq=numerical_reduction_f=w.g_vs_alpha_loop;"
    f"JOINT-CONSIDERATION_with_S104-VIIAM-L11-ANCHOR_S104-BRANCH-IV-DIRECT-L1314_no_double-schedule"
)

# trigger=VERIFY -> NO 3-tuple; regulator_pin N/A this wave (recorded as a companion row note)
print_verdict_payload(
    verdict,
    value_payload,
    audit_sha,
    content_sha,
    companion_note=f"{GATE_ID} spec-completeness (binding-class discriminator); composed-with S94-MULT-NORM-CANCELLATION-K3 + VII.AF.1 + W16",
    extra_rows=[
        "# regulator_pin=N/A (spec names the envelope FORM, not an a_n evaluation; any S105 a_n carries a_n^{Mellin}/a_n^{Pauli-Villars} per regulator-pin-discipline.md)",
    ],
)

sys.exit(0)
