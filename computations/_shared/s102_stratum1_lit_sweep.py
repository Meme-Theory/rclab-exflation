"""
S102-STRATUM1-LIT-SWEEP — MathSciNet / zbMATH / arXiv novelty sweep.

Session 102, Wave 3, item 13 (Stratum-1 pre-submission checklist box 3).

NON-COMPUTE gate. PASS predicate = artifact-existence-with-content: a documented,
structured literature search trace across the mathscinet / zbmath / paper-search (arXiv)
MCP servers for the Stratum-1 item-6/item-7 core, plus a categorical novelty disposition
(CLASSICAL / KNOWN-TECHNIQUE / CANDIDATE-NOVEL / NOT-RELEVANT) per query family.

Item-6 core   : the FULL Dirac spectrum along the Jensen line of SU(3)
                (155,984 eigenvalues with multiplicity at L_max=10; 78,080 unique;
                 crossing structure incl. the (1,1,0) crossing at tau=0.107).
Item-7 core   : the van Hove DOS cusp at the Jensen deformation parameter
                (tau_fold = 0.190; non-stationary-cusp uniqueness).

Cross-reference: cold-read-s101/03-stratum1-novelty-audit.md  §1 (12-row triage table),
rows 6 (CANDIDATE-NOVEL) and 7 (CANDIDATE-NOVEL as a property of #6).

The search-trace records were collected LIVE by the spectral-geometer agent via the MCP
servers (mathscinet status FREE-tier-only; zbmath search_zbmath / search_msc; paper-search
search_arxiv; Google-Scholar AVOIDED per project_paper-search-scholar-rate-limit). Each
record is the agent's transcription of a query's {query, server, hit_count, top_IDs,
disposition}; this script PINS those records, derives the novelty disposition, and prints
the verdict payload (the agent calls emit_verdict — the script never writes the verdict file).

The artifact is the trace itself + the disposition, NOT a numerical comparison.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # before numpy; tiny job, CPU-only
import sys
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import tau_fold  # noqa: E402  (Jensen fold / DOS-cusp pin; query context)

# ----------------------------------------------------------------------------
# Documentation literals (NOT framework constants used in a numerical comparison;
# they contextualize the query families and appear in the triage table / project graph).
# ----------------------------------------------------------------------------
N_EIG_WITH_MULT = 155984      # (local) L_max=10 eigenvalue count w/ multiplicity (triage row 6)
N_EIG_UNIQUE = 78080          # (local) L_max=10 unique eigenvalue count (project-graph; framing.md)
L_MAX_CONTEXT = 10            # (local) truncation cited in the item-6 claim
TAU_110_CROSSING = 0.107      # (local) the (1,1,0) crossing tau cited in triage row 6
TAU_DOS_CUSP = float(tau_fold)  # (local) DOS cusp tau = tau_fold = 0.190 (triage row 7)

# ----------------------------------------------------------------------------
# Disposition rubric (categorical; from the gate block + novelty-audit §1).
# ----------------------------------------------------------------------------
DISPOSITION_VALUES = ("CLASSICAL", "KNOWN-TECHNIQUE", "CANDIDATE-NOVEL", "NOT-RELEVANT")

# ----------------------------------------------------------------------------
# THE SEARCH TRACE.
# One record per (query family, server, query string) actually executed by the agent.
# `hit_count` is the server's reported total; `top_ids` lists the top relevant hits the
# agent inspected (id + 1-line tag); `disposition` is the per-record relevance call:
#   - the disposition records whether THAT query surfaced PRIOR ART for item-6/7
#     (CANDIDATE-NOVEL = no prior art found by this query for the SU(3)-Jensen-line core),
#   - KNOWN-TECHNIQUE = surfaced an adjacent standard method / adjacent space (NOT the core),
#   - CLASSICAL = surfaced a textbook/known theorem for the tau=0 endpoint or a bound,
#   - NOT-RELEVANT = the query family returned only off-topic hits.
# A FOUND-PRIOR-ART record (a published source reproducing item-6 full-Jensen-line spectrum
# OR item-7 DOS cusp) would carry disposition 'FOUND-PRIOR-ART' and flip the verdict to FAIL.
# ----------------------------------------------------------------------------
SEARCH_TRACE = [
    # ---- Family (i): "Dirac spectrum SU(3)" ----
    {
        "family": "(i) Dirac spectrum SU(3)",
        "server": "zbmath/search_zbmath",
        "query": "ti:Dirac ti:spectrum ti:SU(3)",
        "hit_count": 1,
        "top_ids": [
            "Zbl 900147539 / arXiv:1209.3812 — Lai & Teh, 'Dirac spectrum and spectral "
            "action of SU(3)' (2012): BI-INVARIANT SU(3) Dirac spectrum + spectral action "
            "via Poisson summation. In project corpus (Lai-Teh map)."
        ],
        "disposition": "CLASSICAL",
        "note": "The single relevant published SU(3) Dirac spectrum. BI-INVARIANT only = the "
                "tau=0 ENDPOINT of the Jensen line (Fegan/Parthasarathy case, triage row 5). "
                "Prior art for the tau=0 slice; NOT for tau>0 deformation, crossings, or DOS cusp.",
    },
    {
        "family": "(i) Dirac spectrum SU(3)",
        "server": "paper-search/search_arxiv",
        "query": "Dirac operator spectrum SU(3) left-invariant metric",
        "hit_count": 15,
        "top_ids": [
            "quant-ph/0603190 (Cartan decomposition su(N)) — NOT-RELEVANT",
            "hep-th/0305233 (SU(3) Skyrme model) — NOT-RELEVANT",
            "hep-ex/0305022 (DIRAC pionium spectrometer) — NOT-RELEVANT (name collision)",
            "math/0206187 (Majid, Dirac on quantum group C_q[SL_2] at roots of unity) — "
            "adjacent (q-deformed SU(2)), NOT SU(3) left-invariant",
        ],
        "disposition": "NOT-RELEVANT",
        "note": "No hit treats the SU(3) Dirac eigenvalue spectrum on a left-invariant metric. "
                "'DIRAC' name-collisions with the CERN pionium experiment dominate.",
    },
    # ---- Family (ii): left-invariant Dirac eigenvalues, compact Lie group ----
    {
        "family": "(ii) left-invariant Dirac eigenvalues / compact Lie group",
        "server": "paper-search/search_arxiv",
        "query": "Fegan eigenvalues Dirac operator compact symmetric space bi-invariant metric "
                 "spectral action",
        "hit_count": 12,
        "top_ids": [
            "math/0501410, math/0501411 (Milhorat) — FIRST eigenvalue of Dirac on compact "
            "spin symmetric spaces; rep-theoretic. KNOWN-TECHNIQUE adjacency.",
            "arXiv:1909.08283 (Milhorat) — first eigenvalue, OUTER symmetric spaces.",
            "arXiv:1407.2167 (Milhorat) — first eigenvalue, Kähler/Quaternion-Kähler.",
            "arXiv:0710.2911 (Gordon-Schueth-Sutton) — spectral ISOLATION of bi-invariant "
            "metrics within left-invariant (LAPLACE).",
        ],
        "disposition": "KNOWN-TECHNIQUE",
        "note": "Milhorat = FIRST eigenvalue only (not the full spectrum, not along a "
                "deformation). Gordon-Schueth-Sutton = the deep adjacency: studies the "
                "left-invariant deformation NEIGHBOURHOOD of the bi-invariant point, but for "
                "the LAPLACIAN, as isospectrality/rigidity — NOT a computed Dirac spectrum.",
    },
    # ---- Family (iii): Lauret-school output post-2022 (deforming Fegan) ----
    {
        "family": "(iii) Lauret-school deformation track (post-2022)",
        "server": "paper-search/search_arxiv",
        "query": "Lauret Dirac operator eigenvalues compact Lie group left-invariant metric "
                 "deformation",
        "hit_count": 15,
        "top_ids": [
            "arXiv:2004.00350 (E.A. Lauret) — diameter & LAPLACE eigenvalue estimates, "
            "left-invariant metrics on compact Lie groups (EGS conjecture). LAPLACE, not Dirac.",
            "arXiv:1906.03325 (E.A. Lauret) — smallest LAPLACE eigenvalue, naturally reductive.",
            "arXiv:1706.09012 (E.A. Lauret) — spectral uniqueness of bi-invariant metrics on "
            "Sp(n) (LAPLACE).",
            "arXiv:2506.21725 (J. Lauret & Montedoro 2025) — pluriclosed metrics on compact "
            "semisimple groups; NOT spectral.",
        ],
        "disposition": "KNOWN-TECHNIQUE",
        "note": "The Lauret school's left-invariant-metric output is LAPLACE-Beltrami "
                "(eigenvalue bounds, diameter, EGS conjecture, isospectrality) — NOT the Dirac "
                "operator. No SU(3) Dirac deformation line.",
    },
    {
        "family": "(iii) Lauret-school deformation track (Boldt-Lauret Dirac)",
        "server": "paper-search/search_arxiv",
        "query": "Boldt Lauret Dirac operator spectrum spheres SU(2) representation",
        "hit_count": 15,
        "top_ids": [
            "arXiv:1412.2599 (Boldt & Lauret 2014) — explicit formula for Dirac MULTIPLICITIES "
            "on LENS SPACES Gamma\\Spin(2m)/Spin(2m-1); Dirac-isospectrality.",
            "arXiv:1504.03121 (Boldt 2015) — Dirac spectral RIGIDITY on 3-dim lens spaces.",
            "math/0501410 (Milhorat) — first eigenvalue, symmetric spaces.",
        ],
        "disposition": "KNOWN-TECHNIQUE",
        "note": "The canonical Boldt-Lauret Dirac results are on LENS SPACES (quotients of the "
                "round sphere), NOT SU(3), and the metric is the round-sphere quotient, NOT a "
                "left-invariant deformation line. Rep-theoretic Dirac-multiplicity METHOD is "
                "adjacent technique; the SU(3)/3-sphere complete results (Hitchin/Bär/Boldt-"
                "Lauret) are the triage row-6 anchor for 'SU(2)/3-sphere known, SU(3) open'.",
    },
    {
        "family": "(iii) Lauret-school deformation track (Einstein/Jensen deformation)",
        "server": "paper-search/search_arxiv",
        "query": "Jensen Einstein metric deformation Dirac operator homogeneous space spectral "
                 "action",
        "hit_count": 15,
        "top_ids": [
            "arXiv:1405.7304 (Fischmann-Krattenthaler-Somberg) — CONFORMAL POWERS of Dirac on "
            "Einstein manifolds. Different operator; NOT-RELEVANT to spectrum-along-deformation.",
            "arXiv:1206.1306 (Chrysikos-Sakane) — homogeneous EINSTEIN metrics on flag "
            "manifolds; metric classification, NOT Dirac spectrum.",
            "arXiv:2508.11652 (Alexa 2025) — 'Spectral Deformation Flow and Dimension "
            "Recovery'; shifted LAPLACE-Beltrami spectral flow C_n(tau); adjacent FRAMEWORK "
            "(the project's cubic-point comparison), NOT the SU(3) Dirac spectrum.",
        ],
        "disposition": "NOT-RELEVANT",
        "note": "Jensen's 1973 metrics appear in the DG literature (Einstein-metric "
                "instability, Lauret-Lauret 2021+, Schwahn 2023 — triage row 4) but NOT paired "
                "with a Dirac spectrum. Alexa 2025 is an adjacent spectral-flow framework, not "
                "prior art for the SU(3) Dirac spectrum.",
    },
    # ---- Family (iv): "Jensen deformation" Dirac / SU(3) ----
    {
        "family": "(iv) 'Jensen deformation' Dirac / SU(3)",
        "server": "knowledge-MCP/search_knowledge+trace_entity",
        "query": "Jensen line SU(3) Dirac spectrum; van Hove cusp Dirac compact group "
                 "(internal project graph — NOT external literature)",
        "hit_count": 0,
        "top_ids": [
            "Internal only: S88-JENSEN-DIM-SPECTRUM, S85-VAN-HOVE-CUSP-THEOREM, atlas-07 "
            "Petrov classification, S102-FEGAN-TAU0-SPECTRUM-VALIDATION (PASS). NO external-"
            "literature entity.",
        ],
        "disposition": "CANDIDATE-NOVEL",
        "note": "The project graph holds the Jensen-deformed SU(3) Dirac spectrum + van Hove "
                "cusp as INTERNAL results; it is NOT a literature record. Confirms the object "
                "exists internally; the EXTERNAL novelty question is answered by families "
                "(i)-(iii),(v),(vi). 'Jensen deformation' is a framework label, absent from "
                "the external Dirac-spectrum literature.",
    },
    # ---- Family (v): MSC 58J50 / 53C30 / 22E46 — Dirac eigenvalue intersection ----
    {
        "family": "(v) MSC 58J50 spectral problems / 53C30 homogeneous / 22E46",
        "server": "zbmath/search_msc",
        "query": "58J50  (verify MSC class)",
        "hit_count": 2,
        "top_ids": [
            "58J50 — Spectral problems; spectral geometry; scattering theory on manifolds "
            "(confirmed). Parent 58Jxx.",
        ],
        "disposition": "NOT-RELEVANT",
        "note": "MSC-tree confirmation that 58J50 is the correct spectral-geometry class; "
                "the document sweep is the next record.",
    },
    {
        "family": "(v) MSC 58J50 — Dirac eigenvalues",
        "server": "zbmath/search_zbmath",
        "query": "cc:58J50 ti:Dirac ti:eigenvalues",
        "hit_count": 43,
        "top_ids": [
            "Zbl 1220814 (Bär 1998) — extrinsic Dirac eigenvalue BOUNDS.",
            "Zbl 1477791 (Landi-Rovelli 1997) — 'GR in terms of Dirac eigenvalues' "
            "(spectral-action-style program; NOT an SU(3) spectrum).",
            "Hijazi / Friedrich / Ammann / Bär-Dahl / Milhorat (multiple) — first-eigenvalue "
            "& lower-bound results, Killing spinors, twistor operators.",
            "Zbl 1398347 (Agricola-Ammann-Friedrich 1999) — Dirac vs Laplace eigenvalues on a "
            "2-torus (closest 'compare Dirac spectrum to Laplace' instance; T^2, not SU(3)).",
        ],
        "disposition": "KNOWN-TECHNIQUE",
        "note": "The entire 58J50 Dirac-eigenvalue surface is eigenvalue BOUNDS / first-"
                "eigenvalue / isospectrality / Killing-spinor — the paper's standard toolkit "
                "(triage rows 1-3). NO full Dirac spectrum along a left-invariant SU(3) "
                "deformation; NO Dirac DOS on a deformed group.",
    },
    {
        "family": "(v) bibliographic resolution of the bi-invariant SU(3) anchor",
        "server": "mathscinet/lookup_mr_reference (FREE tier; MRef)",
        "query": "Lai & Teh, Dirac spectrum and spectral action of SU(3), 2012, arXiv:1209.3812",
        "hit_count": 1,
        "top_ids": [
            "MR3153451 — Teh, 'Dirac Spectra, Summation Formulae, and the Spectral Action', "
            "PhD thesis, Caltech 2013 (encompasses the Lai-Teh arXiv:1209.3812 paper).",
        ],
        "disposition": "CLASSICAL",
        "note": "MathSciNet MCP is FREE-tier (no API key) -> keyword search unavailable; "
                "lookup_mr_reference resolves the canonical MR ID. The matched thesis is the "
                "BI-INVARIANT SU(3) Dirac-spectrum + spectral-action source = the tau=0 "
                "endpoint. Prior art for the tau=0 slice ONLY.",
    },
    # ---- Family (vi): density of states / van Hove, Dirac, compact group ----
    {
        "family": "(vi) density of states / van Hove singularity — Dirac, homogeneous space",
        "server": "paper-search/search_arxiv",
        "query": "density of states van Hove singularity Dirac operator homogeneous space "
                 "spectral geometry",
        "hit_count": 15,
        "top_ids": [
            "cond-mat: PdTe2 (1911.08733), graphene SDW (1104.5334), KFe2As2 (1807.00193), "
            "FCC lattice (2204.05815), TaSe2 (2211.01780), HOVHS twisted bilayer (1901.05432) "
            "— all CONDENSED-MATTER band-theory DOS.",
            "arXiv:1512.05069 (Dietz et al.) — 'Dirac billiards at the van Hove "
            "singularities': microwave-resonator GRAPHENE ANALOG, not a manifold Dirac DOS.",
            "arXiv:2404.12073 (Davies 2024) — van Hove singularities in the DOS of a chaotic "
            "system via periodic operators (Fibonacci tiling); math-ph, NOT a compact-group "
            "Dirac DOS.",
        ],
        "disposition": "NOT-RELEVANT",
        "note": "The van Hove singularity is classical band-theory (van Hove 1953). EVERY DOS/"
                "van-Hove hit is condensed-matter lattice physics or a chaotic-dynamics "
                "periodic-operator analog. NONE treats the DOS of a Dirac SPECTRUM on a "
                "deformed compact Lie group. The Dirac-DOS-cusp-along-a-Jensen-line object is "
                "unoccupied territory. Confirms item-7 CANDIDATE-NOVEL.",
    },
]


def compute_disposition(trace):
    """Derive the gate disposition from the trace.

    novelty_confirmed := no record carries disposition 'FOUND-PRIOR-ART' for the
    item-6 full-Jensen-line SU(3) Dirac spectrum or the item-7 DOS cusp, AND every
    query family (i)-(vi) has at least one recorded disposition.
    """
    families_required = {"(i)", "(ii)", "(iii)", "(iv)", "(v)", "(vi)"}
    families_covered = {rec["family"].split()[0] for rec in trace}  # (local)
    coverage_ok = families_required.issubset(families_covered)      # (local)

    found_prior_art = [r for r in trace if r["disposition"] == "FOUND-PRIOR-ART"]  # (local)
    # Adjacency inventory (KNOWN-TECHNIQUE / CLASSICAL) — re-scopes the claim, does not refute.
    adjacencies = [r for r in trace
                   if r["disposition"] in ("KNOWN-TECHNIQUE", "CLASSICAL")]  # (local)
    candidate_novel_families = sorted({
        r["family"].split()[0] for r in trace if r["disposition"] == "CANDIDATE-NOVEL"
    })  # (local)

    novelty_confirmed = coverage_ok and (len(found_prior_art) == 0)  # (local)
    return {
        "coverage_ok": coverage_ok,
        "families_covered": sorted(families_covered),
        "n_records": len(trace),
        "n_found_prior_art": len(found_prior_art),
        "n_adjacencies": len(adjacencies),
        "candidate_novel_families": candidate_novel_families,
        "novelty_confirmed": novelty_confirmed,
    }


def make_plot(trace, summary, path):
    """Disposition tally per query family — visual of the saturated sweep."""
    fams = ["(i)", "(ii)", "(iii)", "(iv)", "(v)", "(vi)"]  # (local)
    fam_labels = ["(i)\nDirac\nspec\nSU(3)", "(ii)\nleft-inv\nDirac\neig",
                  "(iii)\nLauret\nschool", "(iv)\nJensen\nlabel", "(v)\nMSC\n58J50",
                  "(vi)\nDOS /\nvan Hove"]  # (local)
    colors = {"CLASSICAL": "#4477AA", "KNOWN-TECHNIQUE": "#66CCEE",
              "CANDIDATE-NOVEL": "#228833", "NOT-RELEVANT": "#BBBBBB",
              "FOUND-PRIOR-ART": "#EE6677"}  # (local)
    fig, ax = plt.subplots(figsize=(11, 6))
    bottoms = {f: 0 for f in fams}  # (local)
    for disp in ("CLASSICAL", "KNOWN-TECHNIQUE", "CANDIDATE-NOVEL", "NOT-RELEVANT",
                 "FOUND-PRIOR-ART"):
        heights = []  # (local)
        for f in fams:
            recs = [r for r in trace if r["family"].split()[0] == f
                    and r["disposition"] == disp]  # (local)
            heights.append(len(recs))
        if sum(heights) == 0:
            continue
        ax.bar(range(len(fams)), heights, bottom=[bottoms[f] for f in fams],
               color=colors[disp], label=disp, edgecolor="white")
        for i, f in enumerate(fams):
            bottoms[f] += heights[i]
    ax.set_xticks(range(len(fams)))
    ax.set_xticklabels(fam_labels, fontsize=8)
    ax.set_ylabel("query records (per family)")
    ax.set_title("S102-STRATUM1-LIT-SWEEP — disposition tally per query family\n"
                 f"novelty_confirmed={summary['novelty_confirmed']}  "
                 f"(prior-art hits={summary['n_found_prior_art']}, "
                 f"records={summary['n_records']}, adjacencies={summary['n_adjacencies']})")
    ax.legend(loc="upper right", fontsize=8)
    ax.text(0.01, 0.98,
            "item-6 (full Jensen-line SU(3) Dirac spectrum) + item-7 (DOS cusp): CANDIDATE-NOVEL\n"
            "only published SU(3) Dirac spectrum = Lai-Teh/Teh BI-INVARIANT (tau=0 endpoint)\n"
            "Lauret-school left-inv output = LAPLACE; Boldt-Lauret Dirac = LENS SPACES; "
            "van-Hove DOS = condensed-matter",
            transform=ax.transAxes, fontsize=7, va="top", ha="left",
            bbox=dict(boxstyle="round", fc="#FFFFCC", ec="#999999", alpha=0.9))
    fig.tight_layout()
    fig.savefig(path, dpi=130)
    plt.close(fig)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    """audit_sha256 = SHA-256 over the ordered input-pin map (JSON, sorted keys)."""
    blob = json.dumps(pin_map, sort_keys=True, ensure_ascii=False).encode("utf-8")  # (local)
    return hashlib.sha256(blob).hexdigest()


def print_verdict_payload(verdict, value, scheme, convention, l_max,
                          audit_sha, content_sha):
    """Print the payload the agent passes to emit_verdict. Script never writes the verdict file."""
    print("\n===VERDICT-PAYLOAD===")
    print(json.dumps({
        "session": 102,
        "gate_id": "S102-STRATUM1-LIT-SWEEP",
        "verdict": verdict,
        "value": value,
        "scheme": scheme,
        "convention": convention,
        "l_max": l_max,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }, ensure_ascii=False))
    print("===END-VERDICT-PAYLOAD===")


def main():
    here = os.path.dirname(__file__)  # (local)
    out_dir = os.path.normpath(os.path.join(here, "..", "session-102"))  # (local)
    script_path = os.path.abspath(__file__)  # (local)

    # ---- input-file SHAs (logged in first 20 lines of stdout per gate-verdicts.md) ----
    audit_md = os.path.normpath(os.path.join(here, "..", "..",
                                             "cold-read-s101", "03-stratum1-novelty-audit.md"))  # (local)
    canon_py = os.path.join(here, "canonical_constants.py")  # (local)
    in_sha = {}  # (local)
    for nm, p in (("novelty_audit", audit_md), ("canonical_constants", canon_py)):
        in_sha[nm] = sha256_file(p) if os.path.exists(p) else "MISSING"

    summary = compute_disposition(SEARCH_TRACE)  # (local)

    print("S102-STRATUM1-LIT-SWEEP — input SHA-256 pins:")
    print(f"  novelty_audit       = {in_sha['novelty_audit']}")
    print(f"  canonical_constants = {in_sha['canonical_constants']}")
    print(f"  tau_fold (imported) = {TAU_DOS_CUSP}")
    print(f"  L_max context       = {L_MAX_CONTEXT}; N_eig w/mult = {N_EIG_WITH_MULT}; "
          f"unique = {N_EIG_UNIQUE}; (1,1,0) crossing tau = {TAU_110_CROSSING}")
    print(f"  search-trace records = {summary['n_records']}; "
          f"families covered = {summary['families_covered']}")
    print(f"  prior-art hits = {summary['n_found_prior_art']}; "
          f"adjacencies (KNOWN-TECHNIQUE/CLASSICAL) = {summary['n_adjacencies']}")
    print(f"  CANDIDATE-NOVEL families = {summary['candidate_novel_families']}")
    print(f"  novelty_confirmed = {summary['novelty_confirmed']}")

    # ---- verdict: PASS iff novelty confirmed with complete trace ----
    verdict = "PASS" if summary["novelty_confirmed"] else "FAIL"  # (local)
    value = (f"novelty_confirmed={summary['novelty_confirmed']};"
             f"records={summary['n_records']};"
             f"families={''.join(summary['families_covered'])};"
             f"prior_art={summary['n_found_prior_art']};"
             f"adjacencies={summary['n_adjacencies']};"
             f"item6=CANDIDATE-NOVEL;item7=CANDIDATE-NOVEL;"
             f"bi-inv_SU(3)_endpoint=Lai-Teh/Teh_MR3153451_arXiv1209.3812;"
             f"Lauret-left-inv=LAPLACE;BoldtLauret-Dirac=LENS-SPACES;"
             f"vanHove-DOS=condensed-matter;MathSciNet=FREE-tier-MRef-only")  # (local)
    scheme = "STRUCTURED-LIT-SWEEP-DOCUMENTED-TRACE"  # (local)
    convention = "NOVELTY-AUDIT-12-ROW-TRIAGE-CROSSREF"  # (local)
    l_max = "N/A"  # (local)

    # ---- save the data artifact (structured trace records + summary) ----
    npz_path = os.path.join(out_dir, "s102_stratum1_lit_sweep.npz")  # (local)
    png_path = os.path.join(out_dir, "s102_stratum1_lit_sweep.png")  # (local)
    np.savez(
        npz_path,
        search_trace_json=json.dumps(SEARCH_TRACE, ensure_ascii=False),
        summary_json=json.dumps(summary, ensure_ascii=False),
        input_sha_json=json.dumps(in_sha, ensure_ascii=False),
        disposition_values=np.array(DISPOSITION_VALUES),
        n_records=summary["n_records"],
        n_found_prior_art=summary["n_found_prior_art"],
        novelty_confirmed=summary["novelty_confirmed"],
        tau_dos_cusp=TAU_DOS_CUSP,
        tau_110_crossing=TAU_110_CROSSING,
        n_eig_with_mult=N_EIG_WITH_MULT,
        n_eig_unique=N_EIG_UNIQUE,
        l_max_context=L_MAX_CONTEXT,
        verdict=verdict,
        value=value,
    )
    make_plot(SEARCH_TRACE, summary, png_path)

    # ---- content SHA (over the script) + audit SHA (over the ordered pin map) ----
    content_sha = sha256_file(script_path)  # (local)
    pin_map = {                                            # (local)
        "01_script_content_sha256": content_sha,
        "02_novelty_audit_sha256": in_sha["novelty_audit"],
        "03_canonical_constants_sha256": in_sha["canonical_constants"],
        "04_gate_id": "S102-STRATUM1-LIT-SWEEP",
        "05_scheme": scheme,
        "06_convention": convention,
        "07_n_records": summary["n_records"],
        "08_families_covered": summary["families_covered"],
        "09_novelty_confirmed": summary["novelty_confirmed"],
        "10_value": value,
    }
    audit_sha = closure_hash(pin_map)  # (local)

    print(f"\n  npz  -> {npz_path}")
    print(f"  png  -> {png_path}")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    print_verdict_payload(verdict, value, scheme, convention, l_max, audit_sha, content_sha)
    sys.exit(0)


if __name__ == "__main__":
    main()
