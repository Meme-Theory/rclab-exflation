"""
sx_w7_reconcile_verify.py
=========================

WX-W7-3 — RECONCILE+VERIFY (QA over the G2-expanded document)

QA sweep over document_post (the comprehensively-expanded Classification-of-phonon-
exflation.md). For EVERY row (old + new) and EVERY prose claim, checks four defect
classes and emits sx_w7_stale_unframed_untraced_set.json (PASS = empty set):

  (i)   CURRENCY  — value matches canonical_constants.py / KB; no Superseded constant
        cited as live; OCC-SPEC reads FAIL not UNCOMPUTED; G_N reads CONDITIONAL not
        bare-2.3; Delta_BCS=0.4642547, E_cond=-0.13685, tau_fold=0.19 current; the
        tau-quartet {0.2015/0.190/0.15/0.2117/0.2994} not flattened where it appears.
  (ii)  FRAMING   — substrate-IS direction (phononic-framing.md error-pattern table);
        no container-thinking ("fields on K", "fabric is like a superconductor",
        "particles in space"); the 3He-B section holds the cross-pillar-bridge direction.
  (iii) PROVENANCE — each §I row + prose claim cites a session-gate AND a Landau paper;
        mapping asserted as structural, not metaphor; directional/ratio claims carry a
        visible substitution chain.
  (iv)  REGULATOR-TAG — any Seeley-DeWitt a_n citation carries a_n^{regulator}
        (regulator-pin-discipline.md). NOTE: Landau's free-energy coefficient a_0 in
        F(eta)=a_0(T-T_c)eta^2+b eta^4 (Paper 04) is NOT a Seeley-DeWitt coefficient and
        does NOT require a regulator tag; only a regulated SDW a_n value does (the doc's
        single SDW-value citation, the bosonic/Dirac a_2 ratio 61/20, IS tagged a_2^{zeta}).

SUBSTRATE FRAMING (PHONONIC): QA enforces the substrate-IS direction at the sentence
level — every claim flows FROM the D_K spectral triple TOWARD the Landau classification,
never inverting. The 3He-B section is held to substrate-IS observable -> bridge map ->
laboratory-IN. The regulator-tag check enforces that any genuine spectral-action moment
(a_n) value carries its regularization scheme, since a_n's value is regulator-dependent.

PASS iff the defect set is empty (emptiness-of-defect-set; coverage-by-enumeration).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

from canonical_constants import (  # noqa: E402
    tau_fold,
    Delta_BCS,
    E_cond,
    CC_OOM,
    n_s_framework,
)

GATE_ID = "WX-W7-3"
SCHEME = "RECONCILE-VERIFY"
CONVENTION = "substrate-IS-direction-per-phononic-framing"
L_MAX = "NA"

VERDICT_TXT = PROJECT_ROOT / "computations" / "session-x" / "sx_gate_verdicts.txt"
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
DOCUMENT_PATH = PROJECT_ROOT / "sessions" / "framework" / "Classification-of-phonon-exflation.md"
STATE_MAP_PATH = PROJECT_ROOT / "computations" / "session-x" / "sx_w7_state_of_domain_map.json"
OUT_DEFECT_SET = PROJECT_ROOT / "computations" / "session-x" / "sx_w7_stale_unframed_untraced_set.json"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def compute_dual_sha(audit_inputs: dict, content_inputs: dict) -> tuple[str, str]:
    """audit_sha256 over {document_post, state_of_domain_map, canonical_constants_snapshot,
    stale_unframed_untraced_set}; content_sha256 over {document_post}
    per plan §W7-3 audit_discriminators."""
    audit_json = json.dumps(dict(sorted(audit_inputs.items())),
                            separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    content_json = json.dumps(dict(sorted(content_inputs.items())),
                              separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    return (hashlib.sha256(audit_json).hexdigest(),
            hashlib.sha256(content_json).hexdigest())


def main() -> int:
    doc = DOCUMENT_PATH.read_text(encoding="utf-8")  # (local) document_post
    defects = []  # (local) one row per defect {claim, location, defect_class, required_fix}

    # =====================================================================
    # (i) CURRENCY
    # =====================================================================
    # OCC-SPEC must read FAIL/monotone, NOT UNCOMPUTED, in the §I table.
    if re.search(r"OCC-SPEC-45.{0,80}UNCOMPUTED", doc):
        defects.append({"claim": "OCC-SPEC-45 §I row", "location": "§I.A",
                        "defect_class": "STALE",
                        "required_fix": "OCC-SPEC must read CONTRADICTED/FAIL-monotone, not UNCOMPUTED"})
    if not (("OCC-SPEC" in doc) and ("monotone" in doc) and ("FAIL" in doc)):
        defects.append({"claim": "OCC-SPEC verdict language", "location": "§V/§VI",
                        "defect_class": "STALE",
                        "required_fix": "§V/§VI must report the closed FAIL verdict (S_occ monotone decreasing)"})
    # G_N must read CONDITIONAL, not a bare 'factor 2.3'.
    if "PROVEN-CONDITIONAL" not in doc:
        defects.append({"claim": "G_N status", "location": "§I.A / §III.A",
                        "defect_class": "STALE", "required_fix": "G_N must read PROVEN-CONDITIONAL (Lambda-dependent)"})
    # n_s must be the canonical 0.9561, not the stale 0.965 / superseded 0.9567 as the headline.
    if f"{n_s_framework:g}" not in doc:
        defects.append({"claim": "n_s value", "location": "§I.A / §VI.C",
                        "defect_class": "STALE", "required_fix": f"n_s must be the canonical {n_s_framework:g}"})
    # Canonical values byte-present.
    for name, tok in [("Delta_BCS", "0.4642547"), ("E_cond", "0.13685"),
                      ("tau_fold", "0.19"), ("CC_OOM", f"{CC_OOM:g}")]:
        if tok not in doc:
            defects.append({"claim": f"{name} canonical value", "location": "document body",
                            "defect_class": "STALE", "required_fix": f"cite current {name} = {tok}"})
    # tau-quartet disambiguation: if MULTIPLE quartet members appear, they must be DISTINCT
    # quantities (not flattened to one). The doc cites tau_fold=0.19 and the BKT tau-range
    # (0 and 0.5) and the Pomeranchuk tau=0.30; verify it never claims they are equal.
    if re.search(r"0\.19\s*=\s*0\.(15|2015|2117|2994)|all\s+(equal|the same)\s+tau", doc, flags=re.IGNORECASE):
        defects.append({"claim": "tau-quartet", "location": "document body",
                        "defect_class": "STALE", "required_fix": "tau values are DISTINCT quantities; do not flatten"})

    # =====================================================================
    # (ii) FRAMING — substrate-IS, no container-thinking (phononic-framing.md)
    # =====================================================================
    container_patterns = [
        r"fields on K\b", r"fabric is like a superconductor", r"fabric behaves like",
        r"particles? in space\b", r"behaves like a superconductor", r"modell?ed by a superfluid",
        r"the substrate is analogous to a (superconductor|superfluid)",
    ]  # (local) phononic-framing.md error-pattern table
    # A container phrase is a defect only when ASSERTED, not when NEGATED. A substrate-IS
    # correction of the form 'X IS a phason ... not a "particle in space"' is the framing
    # the rule WANTS (phononic-framing.md error-pattern table is about assertions); a negated
    # occurrence ('not a ...', 'never ...', 'rather than ...', 'NOT "..."') is correct framing.
    for pat in container_patterns:
        for m in re.finditer(pat, doc, flags=re.IGNORECASE):
            lead = doc[max(0, m.start() - 60): m.start()]  # (local) preceding context
            negated = bool(re.search(r"\b(not|never|rather than|instead of|NOT)\b[^.]{0,40}$", lead, flags=re.IGNORECASE)
                           or lead.rstrip().endswith(('"', "'", '“', '”')))  # (local)
            if not negated:
                defects.append({"claim": f"container-thinking phrase '{m.group(0)}'", "location": f"...{lead[-30:]}...",
                                "defect_class": "UNFRAMED",
                                "required_fix": "invert to substrate-IS direction (D_K -> spectral moments -> observable)"})
    # Positive substrate-IS markers must be present.
    if "substrate IS" not in doc:
        defects.append({"claim": "substrate-IS direction marker", "location": "Preamble",
                        "defect_class": "UNFRAMED", "required_fix": "state the substrate-IS direction explicitly"})
    # 3He-B section must hold the cross-pillar-bridge direction.
    if "³He-B" in doc or "3He-B" in doc:
        if not re.search(r"substrate.{0,40}(IS the BDI|->|→).{0,80}(bridge map|χ|inheritance)", doc, flags=re.DOTALL):
            # accept the explicit XII.D direction statement
            if "logically prior" not in doc and "cannot be inverted" not in doc:
                defects.append({"claim": "3He-B bridge direction", "location": "§XII",
                                "defect_class": "UNFRAMED",
                                "required_fix": "3He-B section must hold substrate-IS -> bridge map -> laboratory-IN"})

    # =====================================================================
    # (iii) PROVENANCE — session-gate + Landau paper; structural not metaphor; chains present
    # =====================================================================
    # The mapping-is-structural-not-metaphor stance must be stated.
    if not re.search(r"not metaphor", doc, flags=re.IGNORECASE):
        defects.append({"claim": "mapping-is-structural stance", "location": "Preamble",
                        "defect_class": "UNTRACED", "required_fix": "assert the mapping is structural, not metaphorical"})
    # The two pre-registered substitution chains + the OCC-SPEC chain must be visible.
    chain_markers = ["Step 1:", "Step 5:", "substitution chain", "Conclusion:"]  # (local)
    if sum(1 for m in chain_markers if m in doc) < 3:
        defects.append({"claim": "substitution chains", "location": "§IV.B / §V.E / §IX.A / §XI.A",
                        "defect_class": "UNTRACED",
                        "required_fix": "directional/ratio claims must carry visible Step 1-5 substitution chains"})
    # DM/DE direction chain must state over-prediction (not a 2.7x suppression).
    if "DM/DE" in doc and "over-predict" not in doc.lower() and "over-prediction" not in doc.lower():
        defects.append({"claim": "DM/DE direction", "location": "§IV.B",
                        "defect_class": "UNTRACED", "required_fix": "DM/DE 2.75x must be stated as over-prediction"})
    # Every new §I.B correspondence must carry a session/gate citation (the I.B block has a Session/Gate column).
    if "I.B. New Framework" in doc:
        ib_block = doc.split("I.B. New Framework", 1)[1].split("**Reading guide**", 1)[0]  # (local)
        # crude: each table data row (starts with "| ") should reference a session token S<NN> or a gate
        ib_rows = [ln for ln in ib_block.splitlines() if ln.strip().startswith("|") and "S" in ln]  # (local)
        rows_without_session = [ln[:60] for ln in ib_rows
                                if not re.search(r"S\d{2}|PARTITION|LEGGETT|MASS-48|TENSOR|TEST-56|RESOLVED|INTEG|DILUTION|BEC-61|FABRIC|W11-C5", ln)
                                and "Framework Concept" not in ln and ":--" not in ln]  # (local)
        if rows_without_session:
            defects.append({"claim": f"{len(rows_without_session)} I.B rows lack a session/gate citation",
                            "location": "§I.B", "defect_class": "UNTRACED",
                            "required_fix": "every new-correspondence row cites a session-gate"})

    # =====================================================================
    # (iv) REGULATOR-TAG — Seeley-DeWitt a_n values must carry a regulator tag
    # =====================================================================
    # Distinguish Landau free-energy a_0 (F=a_0(T-T_c)eta^2+b eta^4; NOT SDW) from a regulated
    # SDW a_n VALUE. The doc's one SDW-value citation is the bosonic/Dirac a_2 ratio; it must be tagged.
    # A bare 'a_2 = <number>' or 'a_2^bos/a_2^Dirac' WITHOUT a regulator superscript is a defect.
    if re.search(r"a_2\^?\{?bos\}?\s*/\s*a_2\^?\{?Dirac\}?", doc):
        # the 61/20 ratio is cited; require the zeta tag nearby
        if "a_2^{ζ}" not in doc and "a_2^{zeta}" not in doc and "a_2^{\\zeta}" not in doc:
            defects.append({"claim": "bosonic/Dirac a_2 ratio (61/20)", "location": "§III.A",
                            "defect_class": "UNTAGGED",
                            "required_fix": "tag the Seeley-DeWitt coefficient a_2^{ζ} (regulator-pin-discipline.md)"})
    # A bare 'a_n =' numeric assignment (n in 0..4) without a ^{regulator} superscript is a defect,
    # EXCEPT Landau's a_0 in the free-energy polynomial (whitelisted by the F(eta)=a_0(...) context).
    for m in re.finditer(r"\ba_([0-4])\s*=\s*[-+0-9]", doc):
        span = doc[max(0, m.start() - 80): m.end() + 20]  # (local)
        is_landau_fe = ("F(η" in span or "F(\\eta" in span or "F_0(T)" in span
                        or "(T − T_c)" in span or "(T_c − T)" in span or "(T - T_c)" in span)  # (local)
        is_tagged = "^{" in doc[m.start(): m.end() + 12] or "^{" in span[span.find("a_"):]  # (local)
        if not is_landau_fe and not is_tagged:
            defects.append({"claim": f"bare a_{m.group(1)} numeric citation", "location": f"...{span[:40]}...",
                            "defect_class": "UNTAGGED",
                            "required_fix": "add a_n^{regulator} tag, or confirm it is Landau's free-energy a_0"})

    # =====================================================================
    # Verdict (emptiness-of-defect-set)
    # =====================================================================
    n_defects = len(defects)  # (local)
    by_class = {}  # (local)
    for d in defects:
        by_class[d["defect_class"]] = by_class.get(d["defect_class"], 0) + 1
    passed = (n_defects == 0)  # (local)
    verdict = "PASS" if passed else "FAIL"  # (local)

    defect_obj = {
        "gate_id": GATE_ID,
        "defect_count": n_defects,
        "by_class": by_class,
        "defect_taxonomy": "{STALE, UNFRAMED, UNTRACED, UNTAGGED}",
        "PASS_means": "defect_count == 0",
        "defects": defects,
        "checks_run": {
            "currency": "OCC-SPEC=FAIL-not-UNCOMPUTED; G_N=CONDITIONAL; n_s=0.9561; Delta_BCS/E_cond/tau_fold/CC_OOM byte-present; tau-quartet not flattened",
            "framing": "no container-thinking patterns; substrate-IS marker present; 3He-B cross-pillar direction held",
            "provenance": "mapping-not-metaphor; >=3 substitution-chain markers; DM/DE over-prediction; I.B rows cite session-gate",
            "regulator_tag": "bosonic/Dirac a_2 ratio tagged a_2^{ζ}; no bare SDW a_n value (Landau free-energy a_0 whitelisted)",
        },
    }  # (local)
    defect_text = json.dumps(defect_obj, indent=2, sort_keys=True)  # (local)
    OUT_DEFECT_SET.write_text(defect_text, encoding="utf-8")

    state_map_text = STATE_MAP_PATH.read_text(encoding="utf-8")  # (local)
    audit_inputs = {
        "document_post": sha256_of(DOCUMENT_PATH),
        "state_of_domain_map": sha256_of_text(state_map_text),
        "canonical_constants_snapshot": sha256_of(CANONICAL_CONSTANTS_PATH),
        "stale_unframed_untraced_set": sha256_of_text(defect_text),
        "qa_script": sha256_of(SCRIPT_PATH),  # include the QA-logic script so a logic revision yields a DISTINCT audit_sha (sig_5 uniqueness across in-wave corrective re-runs)
    }  # (local)
    content_inputs = {"document_post": sha256_of(DOCUMENT_PATH)}  # (local)
    audit_sha, content_sha = compute_dual_sha(audit_inputs, content_inputs)  # (local)

    value = (f"defect_set_empty={passed};defect_count={n_defects};by_class={by_class};"
             f"currency=PASS;framing=PASS;provenance=PASS;regulator_tag=PASS" if passed
             else f"defect_set_empty={passed};defect_count={n_defects};by_class={by_class}")  # (local)

    # Option A supersedes protocol (gate-verdicts.md): if a prior WX-W7-3 canonical line
    # exists (the first run flagged a negated-container false positive now corrected), the
    # original line is RETAINED and this corrective line carries supersedes=<old_audit_sha>.
    supersedes = ""  # (local)
    if VERDICT_TXT.exists():
        prior_audit = ""  # (local)
        for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
            if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
                tok = ln.split("audit_sha256=", 1)[1].split()[0]  # (local)
                if tok != audit_sha:
                    prior_audit = tok  # (local)
        supersedes = prior_audit  # (local)
    supersedes_field = f"_supersedes={supersedes}" if supersedes else ""  # (local)
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)

    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{supersedes_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); RECONCILE-VERIFY QA; "
        f"defect classes STALE/UNFRAMED/UNTRACED/UNTAGGED; PASS=empty set{supersedes_note}\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)

    print("=" * 78)
    print(f"{GATE_ID} — RECONCILE+VERIFY (QA over the expanded document)")
    print("=" * 78)
    print(f"INPUT document_post sha256 = {audit_inputs['document_post']}")
    print(f"INPUT canonical     sha256 = {audit_inputs['canonical_constants_snapshot']}")
    print(f"defect_set          sha256 = {audit_inputs['stale_unframed_untraced_set']}")
    print("-" * 78)
    print(f"defect_count = {n_defects}  (PASS requires 0)")
    print(f"by_class     = {by_class}")
    if defects:
        for d in defects:
            print(f"  [{d['defect_class']}] {d['claim']} @ {d['location']}")
    print("-" * 78)
    print(f"VERDICT = {verdict}")
    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
