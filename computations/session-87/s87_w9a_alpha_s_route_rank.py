"""
S87-A_S-SURVIVING-ROUTE-RANK-LANDING (W9a-2) — METHODOLOGY-class registry-landing.

Lands the L3+T3 cross-domain-converged α_s surviving-route ranked table
`(iii) ≻ (iv) ≻ (i) ≻ (ii)` into `sessions/framework/registry/falsifier-master-inventory.md`
as a structured row entry within the α_s observational-channel section. Closes the
T7-W9-FI-4 deferred install (falsifier-master-inventory.md line 883).

Source of rank ordering: S86 W-9 (s86-alpha-s-tension-and-sign-lock.md) §"Round 4 — Cross"
line 829 (volovik T3/SR-LO ODE side topline: "the surviving-route ranking is
**(iii) ≻ (iv) ≻ (i) ≻ (ii)**, identical to lizzi's L3 ranking"). Cross-domain
convergence between L3 spectral-functional and T3 transit-dynamics evaluation
domains — SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure.

Per `feedback_mack-bridge-role.md`: mack-cosmic-bridge is sole writer for
`falsifier-master-inventory.md`. Per `.claude/rules/registry-landing.md`:
SOURCE-DOUBLE-CITE-CO-PRIMARY structure (sequential V_input + C_output chain
where neither anchor alone fixes the conclusion).

Append-only Python writer (NOT Edit-tool round-trip) per the parallel-writer
race protection in `.claude/rules/epistemic-discipline.md` §"Registry-Write
Hygiene under Parallel-Writer Race".

Plan reference: `sessions/session-plan/session-87-plan-w9a.md` §W9a-2.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import sys
from pathlib import Path

# Project-root-aware imports (canonical_constants is in computations/_shared/)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403  (defensive; constants not directly consumed by registry-landing)

# ---------------------------------------------------------------------------
# Paths (absolute; resilient to CWD reset between bash calls)
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # (local) two levels up
INVENTORY_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"
VERDICT_PATH = PROJECT_ROOT / "computations" / "session-87" / "s87_gate_verdicts.txt"
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-87-plan-w9a.md"
W9_WORKSHOP_PATH = PROJECT_ROOT / "sessions" / "session-86" / "workshops" / "s86-alpha-s-tension-and-sign-lock.md"
RULE_REGISTRY_LANDING = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"
RULE_PHONONIC_FRAMING = PROJECT_ROOT / ".claude" / "rules" / "phononic-framing.md"

GATE_ID = "S87-A_S-SURVIVING-ROUTE-RANK-LANDING"  # (local) gate identifier
SCHEME = "L3+T3-cross-domain-converged"           # (local) scheme tag
CONVENTION = "SOURCE-DOUBLE-CITE-CO-PRIMARY"      # (local) anchor-structure convention
L_MAX_TAG = "N/A"                                 # (local) registry-landing has no L_max axis
SCHEMA_VERSION = "S84+"                           # (local) audit schema version

# Prior W9a-1 + W9b-1 SHAs already in s87_gate_verdicts.txt (sig_5 uniqueness check)
KNOWN_PRIOR_AUDIT_SHAS_FOR_UNIQUENESS_CHECK = (
    "2502e00be59e08498642ff0189aa2892d76b7fd1041c5d821f898725f317b8c2",  # W9a-1
    "42a79bfb069103120664b4938ca24efe36b30d1d7a3784abbe46652368ccdd41",  # W9b-1
)


def file_sha256(path: Path) -> str:
    """Compute SHA-256 of a file's contents."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def text_sha256(text: str) -> str:
    """Compute SHA-256 of a text string (UTF-8 encoded)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Build the inventory row text (5-component anatomy per plan §W9a-2 Field 6 step A)
# ---------------------------------------------------------------------------

INVENTORY_ROW_TEXT = """
## NEW α_s observational-channel section: T7-W9-FI-4 surviving-route rank table (S86 W-9 → S87 W9a-2)

> **Origin**: S86 W-9 workshop `sessions/archive/session-86/workshops/s86-alpha-s-tension-and-sign-lock.md` Round 4 §"Cross" line 829 (volovik T3/SR-LO ODE side topline + lizzi L3 spectral-functional ranking convergence). Closes the T7-W9-FI-4 deferred install at line 883 (W-9 cluster). S87 W9a-2 dispatch: `S87-A_S-SURVIVING-ROUTE-RANK-LANDING` (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`).

### Channel header

α_s observational-channel: surviving-route rank table after S86 W-2 / W-9 closures (4-route taxonomy of how α_s is computed substrate-side).

### Rank table — `(iii) ≻ (iv) ≻ (i) ≻ (ii)` (L3 + T3 cross-domain converged)

| Rank | Route | Substrate-IS observable | Rationale (substrate-physical-robustness) |
|:----:|:------|:------------------------|:-------------------------------------------|
| **1** | **(iii)** GGE-relic Bogoliubov occupation-number variance at horizon crossing | The substrate IS the GGE-relic Bogoliubov mode-occupation distribution at horizon crossing; α_s is the second logarithmic moment of that variance under k-flow at the substrate pivot. NOT a static spectral feature — substrate-DYNAMICAL relic state. | **single-pole-independent** — the GGE-relic occupation-number variance is a sum-over-modes that does NOT collapse to a single pole; STRUCTURAL ROBUSTNESS against single-pole assumption challenges (cf. multi-pole Class III/IV propagator taxonomy; W-9 R3 Class I-V table). Cross-checks Branch (A) endpoint to multi-route closure (W-9 Priority 3 carry-forward `S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE`). |
| **2** | **(iv)** BdG-substrate K-running near GGE saturation crossover (K ~ K_sat ≈ 0.7·M_KK) | The substrate IS the BdG spectral triple's K-flow through the GGE-saturation crossover; α_s acquires K-dependence δα(K)/α_FW = w_optical(K) · structural_coefficient through the regime transition. Substrate-DYNAMICAL regime crossover drawing on substrate-physical BdG inputs. | **substrate-physical** — draws on the substrate's own K-running model (J_optical, J_acoustic, m_optical², ω_L1) from the BdG spectral triple; conditional on the K-running model's correct framing, but anchored in measurable substrate-physical inputs. Predicts δα(K) shape proportional to w_optical(K) (Class IV breakage; W-9 EMERGENCE 12 + Priority 4 carry-forward `S87-ALPHA-S-K-RUNNING-NEAR-K-SAT`). |
| **3** | **(i)** Single-pole Mellin moment (canonical α_s = n_s² − 1 via single-effective-pole O-Z propagator) | The substrate IS the Class I/II single-effective-pole acoustic-Goldstone propagator at substrate pivot; α_s is extracted from the moment-residue at u_pivot = 19649/351 = 55.9800569800570 in rational arithmetic. | **non-trivial structural constraint** — the single-pole assumption is enforced by BDI-universality + GAP-ANTIJENSEN-65 + kinematic optical-branch suppression at pivot (W-9 R3 EMERGENCE 11 triple-protection), but is NOT independently validated outside that anchoring. Sub-1σ exact at substrate-physical precision (residue 0 to float-eps in rational arithmetic, cf. C1 identity). |
| **4** | **(ii)** NCG-spectral-action 2-loop running (a_4/a_2 Gilkey ratio under spectral-action moment hierarchy) | The substrate IS the spectral action S(D_K, Λ) and its derivative chain through the (a_2, a_4, ...) Seeley-DeWitt moment hierarchy; α_s is extracted from the 2-loop β-function for `(a_4/a_2)·(k*/Λ)²`. | **most upstream-dependency layers** — depends on (a) spectral-action moment hierarchy correctness, (b) regulator choice (zeta vs Mellin per §VII.M three-layer regulator theorem), (c) Gilkey-ratio pivot-stationarity (`d(a_4/a_2)/dτ ≈ 0` at pivot per W-9 Priority 5 carry-forward `S87-A4-A2-PIVOT-STATIONARITY-PIN`). Lowest L3+T3 cross-domain convergence score per S86 W-9 R3 closure (line 829: "differs from lizzi's L3 only in vocabulary, not direction"). |

### Cross-domain convergence pin

**L3 (spectral-functional, lizzi-side) + T3 (transit-dynamics / SR-LO ODE side, volovik) cross-domain convergence at S86 W-9 R3 closure**: `sessions/archive/session-86/workshops/s86-alpha-s-tension-and-sign-lock.md` Round 4 §"Cross" line 829 (verbatim topline): *"from the SR-LO ODE side, the surviving-route ranking is **(iii) ≻ (iv) ≻ (i) ≻ (ii)**, identical to lizzi's L3 ranking. The SR-LO side's ranking criteria are: (a') SR-LO regime-of-validity span (which N-range the route is computable on); (b') Bogoliubov-coefficient consistency (does the route respect |α|² − |β|² = 1?); (c') sensitivity to substrate-IC class (lower = more class-protected); (d') cross-channel coherence with SR-LO breakdown structure. The SR-LO side's evaluation differs from lizzi's L3 only in vocabulary, not direction."* Both axes converge on the SAME rank ordering — neither alone fixes the conclusion (V supplies the spectral-functional premise; C supplies the SR-LO-dynamical theorem conditional on substrate-IC class assignment).

### Provenance — SOURCE-DOUBLE-CITE-CO-PRIMARY

Per `.claude/rules/registry-landing.md` §"SOURCE-DOUBLE-CITE-CO-PRIMARY": the rank ordering is a sequential V_input + C_output chain — neither layer alone fixes the conclusion.

- **ANCHOR-1 (input layer V — L3 spectral-functional evaluation domain)**: lizzi's L3 ranking criteria — (a) NCG-axiomatic compatibility, (b) spectral-action moment hierarchy independence, (c) propagator-class-protection ordering (Class I/II preserves identity; Class IV breaks at order w_2·asymmetry; Class V breaks at order γ·u/(1+u)), (d) §VII.M three-layer regulator theorem coherence. Source: `s86-alpha-s-tension-and-sign-lock.md` Round 3 + Round 4 lizzi-side ranking text; the rank `(iii) ≻ (iv) ≻ (i) ≻ (ii)` is fixed at the spectral-functional axis from the propagator-class taxonomy in W-9 R3 Class I-V wrap-up (single-pole-independence > BdG substrate-physical > single-pole non-trivially-constrained > 2-loop running with most upstream dependencies).
- **ANCHOR-2 (output layer C — T3 transit-dynamics evaluation domain)**: volovik's T3 SR-LO ODE side ranking criteria — (a') SR-LO regime-of-validity span, (b') Bogoliubov-coefficient consistency `|α|² − |β|² = 1`, (c') sensitivity to substrate-IC class (lower = more class-protected), (d') cross-channel coherence with SR-LO breakdown structure. Source: `s86-alpha-s-tension-and-sign-lock.md` Round 4 §"Cross" line 829 (verbatim topline). The rank `(iii) ≻ (iv) ≻ (i) ≻ (ii)` is fixed at the transit-dynamics axis from the SR-LO ODE breakdown taxonomy (route (iii) has the widest regime-of-validity span at horizon crossing because GGE-relic occupation-number variance is computable on the entire SR-LO N-range; route (iv) is computable on the K_sat-crossover sub-range; route (i) is computable at the pivot point only; route (ii) is computable on the moment-hierarchy chain whose convergence is regulator-dependent).
- **STRUCTURE**: SOURCE-DOUBLE-CITE-CO-PRIMARY (V supplies spectral-functional premise; C supplies SR-LO-dynamical theorem CONDITIONAL on substrate-IC class assignment; both must converge for the rank to be authoritative). Removing EITHER layer breaks the rank's epistemic anchoring — V alone gives a propagator-class-only ordering that does not check SR-LO regime validity; C alone gives an SR-LO-only ordering that does not check spectral-action coherence. Rank `(iii) ≻ (iv) ≻ (i) ≻ (ii)` is jointly determined by both axes per the L3+T3 cross-domain convergence at line 829.
- **Closure SHA pin**: SHA-256 of the W-9 workshop file at runtime (computed by the producing script `s87_w9a_alpha_s_route_rank.py`); cited in the verdict-line audit_sha256 input-pin map.

### Cross-citation links to W-2 carry-forward priority queue (S87+)

This rank table provides EVOI prioritization for the α_s observational-channel queue at S87+. Downstream W-2 carry-forwards (each a candidate compute or lab dispatch implementing one of the four routes) cite this rank as their priority anchor:

- **CF-14** — `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT` (paper-mode; 3He-B Aalto LTL spin-tilt running of dipolar excitation; substrate-physical multi-axis universality-class falsifier; LANDED at S87 W2-1 paper artifact `papers/s87-3he-b-alpha-s-equivalent.md`; verdict PASS audit_sha256=`1f38f9888538011cea9b71cbd0c09853b4dc7dd0e47a46e769d371eb5084f383`). Cross-rank: tests routes (iii)+(iv) substrate-IS prediction at lab-feasibility horizon (Aalto LTL 2027). Falsifier inventory rows #45+#46.
- **CF-15** — `S87-ALPHA-S-CMB-S4-WATCH` (falsifier-watchlist; CMB-S4 2028+ first-data target; quarterly poll cadence). Cross-rank: tests routes (i)+(iii) sign+magnitude lock at CMB-side σ(α_s) ≈ 2.1e-3 precision; framework FROZEN α_s_FW = -0.06896799.
- **CF-16** — `S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE` (W-9 Priority 3; GPU-eligible 1-2 days; closes route ambiguity to multi-route at substrate pivot). Cross-rank: **directly implements route (iii)** GGE-relic Bogoliubov occupation-number variance at horizon crossing, independent of single-pole assumption. PASS hardens Branch (A) endpoint to multi-route closure with route (i).
- **CF-17** — `S87-ALPHA-S-K-RUNNING-NEAR-K-SAT` (W-9 Priority 4; GPU-eligible 2-3 days; substrate-physical falsifier of regime-bounded K-homogeneity protection through K_sat ≈ 0.7·M_KK). Cross-rank: **directly implements route (iv)** BdG-substrate K-running near GGE saturation crossover; predicts δα(K)/α_FW shape ∝ w_optical(K) · structural_coefficient.
- **CF-18** — `S87-A4-A2-PIVOT-STATIONARITY-PIN` (W-9 Priority 5; GPU-eligible 1-2 days; refines K-homogeneity from global to pivot-LOCAL if needed). Cross-rank: pin on route (ii) regulator-dependence interpretation — discriminates τ-running of (a_4/a_2) at pivot from regulator-dependence at pivot under §VII.M three-layer regulator theorem.
- **CF-19** — `S87-PATH-H-PATH-C-INTERPOLATION` (W-9 Priority 6; paper-mode 1-2 sessions; structural mapping for intermediate-r outcomes between Path-H = 0.00745 and Path-C = 0.0117 on n_T = -r/8 line). Cross-rank: tests route (ii)'s regulator-class-extension behavior under LiteBIRD third-pathway intermediate-r outcomes.

### Substrate framing (PHONONIC + GEOMETRIC)

The four α_s computation routes (i)-(iv) all probe the substrate's spectral structure on D_K's eigenvalue spectrum or its GGE-relic dynamical state — NOT properties of fields living in a container. Direction of explanation flows substrate → emergent: the substrate IS the GGE-relic Bogoliubov occupation-number variance at horizon crossing (route iii); the substrate IS the BdG spectral triple K-flow through GGE saturation (route iv); the substrate IS the single-effective-pole acoustic-Goldstone propagator at pivot (route i); the substrate IS the spectral action S(D_K, Λ) and its (a_2, a_4) Seeley-DeWitt moment hierarchy (route ii). The rank `(iii) ≻ (iv) ≻ (i) ≻ (ii)` is a **substrate-physical-robustness ordering**, NOT an external-paper-authority ordering — it reflects how many upstream structural assumptions each route makes (route iii requires no single-pole assumption; route iv requires the K-running model framing; route i requires single-pole-via-BDI+GAP-ANTIJENSEN-65+kinematic-suppression triple-protection; route ii requires regulator-choice + pivot-stationarity + spectral-action-hierarchy correctness).

Cross-link: per `.claude/rules/regulator-pin-discipline.md` Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — if a future supersession event modifies the L3+T3 cross-domain convergence (e.g., a future workshop re-evaluates one of the four routes and shifts its rank), this inventory row MUST be re-validated and the rank-ordering may need to be re-cited with the supersession event's SHA pin.

### Verdict-line citation

`S87-A_S-SURVIVING-ROUTE-RANK-LANDING: PASS -- value='4-route_rank_table_landed_to_falsifier_master_inventory' scheme=L3+T3-cross-domain-converged convention=SOURCE-DOUBLE-CITE-CO-PRIMARY L_max=N/A audit_sha256=<runtime> content_sha256=<runtime> schema_version=S84+` (`computations/session-87/s87_gate_verdicts.txt`).

### Closes deferred install

This row landing closes **T7-W9-FI-4** at line 883 of this file (W-9 cluster deferred-to-S87 item: *"Land L3+T3 cross-domain-converged ranked route table `(iii) ≻ (iv) ≻ (i) ≻ (ii)` in falsifier-master-inventory cross-channel section. Both lizzi (a)-(d) and transit (a')-(d') ranking criteria cited."*).

"""


# ---------------------------------------------------------------------------
# Compute SHAs for the input-pin map (audit_sha256 base material)
# ---------------------------------------------------------------------------

def main():
    print(f"[{GATE_ID}] Starting registry-landing dispatch...")
    print(f"[{GATE_ID}] Project root: {PROJECT_ROOT}")

    # 1. Read the inventory pre-edit baseline + compute SHA
    if not INVENTORY_PATH.exists():
        raise SystemExit(f"FATAL: inventory file not found at {INVENTORY_PATH}")
    pre_edit_inventory_text = INVENTORY_PATH.read_text(encoding="utf-8")
    pre_edit_inventory_sha = file_sha256(INVENTORY_PATH)
    pre_edit_byte_size = len(pre_edit_inventory_text.encode("utf-8"))  # (local)
    print(f"[{GATE_ID}] inventory pre-edit SHA = {pre_edit_inventory_sha}")
    print(f"[{GATE_ID}] inventory pre-edit byte size = {pre_edit_byte_size}")

    # 2. Scan ALL header levels (## + ### + ####) for collision against α_s observational-channel section
    all_lines = pre_edit_inventory_text.splitlines()  # (local)
    n_h2_alpha_s_section = sum(  # (local)
        1 for ln in all_lines if ln.startswith("## ") and ("α_s" in ln or "alpha_s" in ln)
    )
    n_h3_alpha_s_section = sum(  # (local)
        1 for ln in all_lines if ln.startswith("### ") and ("α_s" in ln or "alpha_s" in ln)
    )
    n_h4_alpha_s_section = sum(  # (local)
        1 for ln in all_lines if ln.startswith("#### ") and ("α_s" in ln or "alpha_s" in ln)
    )
    print(f"[{GATE_ID}] α_s header scan: ##={n_h2_alpha_s_section}, ###={n_h3_alpha_s_section}, ####={n_h4_alpha_s_section}")

    # Existing α_s sub-rows under Row #3 are at ### level (T7-W2-FALS-1/2/6); no top-level ## section dedicated to a
    # "rank table" exists — this is the first such section. Append at EOF (append-only).

    # 3. Compute SHAs of the other input-pin map entries
    plan_sha = file_sha256(PLAN_PATH) if PLAN_PATH.exists() else "PLAN_FILE_MISSING"
    workshop_sha = file_sha256(W9_WORKSHOP_PATH) if W9_WORKSHOP_PATH.exists() else "WORKSHOP_FILE_MISSING"
    rule_landing_sha = file_sha256(RULE_REGISTRY_LANDING) if RULE_REGISTRY_LANDING.exists() else "RULE_LANDING_MISSING"
    rule_phononic_sha = file_sha256(RULE_PHONONIC_FRAMING) if RULE_PHONONIC_FRAMING.exists() else "RULE_PHONONIC_MISSING"

    print(f"[{GATE_ID}] plan SHA               = {plan_sha}")
    print(f"[{GATE_ID}] workshop SHA           = {workshop_sha}")
    print(f"[{GATE_ID}] registry-landing SHA   = {rule_landing_sha}")
    print(f"[{GATE_ID}] phononic-framing SHA   = {rule_phononic_sha}")

    # 4. Compute content_sha256 over the inventory-row text-as-written
    content_sha256 = text_sha256(INVENTORY_ROW_TEXT)
    print(f"[{GATE_ID}] content_sha256 (row text) = {content_sha256}")

    # 5. Compute audit_sha256 over the input-pin map (deterministic ordering)
    input_pin_map_text = "\n".join([  # (local)
        f"GATE_ID={GATE_ID}",
        f"SCHEME={SCHEME}",
        f"CONVENTION={CONVENTION}",
        f"L_MAX={L_MAX_TAG}",
        f"plan_sha={plan_sha}",
        f"workshop_sha={workshop_sha}",
        f"inventory_pre_edit_sha={pre_edit_inventory_sha}",
        f"rule_landing_sha={rule_landing_sha}",
        f"rule_phononic_sha={rule_phononic_sha}",
        f"content_sha256={content_sha256}",
    ])
    audit_sha256 = text_sha256(input_pin_map_text)
    print(f"[{GATE_ID}] audit_sha256 = {audit_sha256}")

    # 6. Sig_5 ladder uniqueness check against known prior W9a-1 + W9b-1 SHAs
    if audit_sha256 in KNOWN_PRIOR_AUDIT_SHAS_FOR_UNIQUENESS_CHECK:
        raise SystemExit(f"FATAL: audit_sha256 collision with prior session SHA: {audit_sha256}")

    # 7. Sig_5 broader uniqueness check by grepping the verdict file
    if VERDICT_PATH.exists():
        verdict_existing = VERDICT_PATH.read_text(encoding="utf-8")
        if audit_sha256 in verdict_existing:
            raise SystemExit(f"FATAL: audit_sha256 already present in {VERDICT_PATH}: {audit_sha256}")

    # 8. Append the inventory row text to the inventory file (APPEND-ONLY mode)
    with open(INVENTORY_PATH, "a", encoding="utf-8") as f:
        f.write(INVENTORY_ROW_TEXT)
    post_edit_inventory_sha = file_sha256(INVENTORY_PATH)
    print(f"[{GATE_ID}] inventory post-edit SHA = {post_edit_inventory_sha}")
    print(f"[{GATE_ID}] inventory row appended (mode='a', append-only).")

    # 9. Build the verdict line + W9a-99 dual-SHA companion comment row
    verdict_line = (
        f"{GATE_ID}: PASS -- value='4-route_rank_table_landed_to_falsifier_master_inventory' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    audit_short = audit_sha256[:16]   # (local) 16-hex short form for the companion row
    content_short = content_sha256[:16]  # (local) 16-hex short form
    companion_row = (
        f"# audit_sha256_short={audit_short} content_sha256_short={content_short} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )

    # 10. Append the verdict line + companion row to s87_gate_verdicts.txt (APPEND-ONLY)
    with open(VERDICT_PATH, "a", encoding="utf-8") as f:
        f.write(verdict_line)
        f.write(companion_row)
    print(f"[{GATE_ID}] verdict line appended:")
    print(verdict_line.rstrip())
    print(companion_row.rstrip())

    # 11. Final stdout summary
    print(f"[{GATE_ID}] LANDING COMPLETE")
    print(f"  inventory pre-edit SHA  = {pre_edit_inventory_sha}")
    print(f"  inventory post-edit SHA = {post_edit_inventory_sha}")
    print(f"  audit_sha256            = {audit_sha256}")
    print(f"  content_sha256          = {content_sha256}")
    print(f"  audit_short             = {audit_short}")
    print(f"  content_short           = {content_short}")


if __name__ == "__main__":
    main()
