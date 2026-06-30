#!/usr/bin/env python
"""
S85-W2-ALPHA-S-AXIOM-MINIMALITY-AU

Audit of the NCG-axiom minimality for the alpha_s derivation (a_4 Seeley-DeWitt
coefficient). The plan §W2-1 (session-85-plan-w2.md) specifies a 7-axiom
CCM-2007 roster and asks: which subset is LOAD-BEARING for the a_4 coefficient
that pins alpha_s?

Reference: Chamseddine-Connes-Marcolli 2007, §2.1; standard 7-axiom NCG roster
from Connes 1995 "Noncommutative geometry and reality".

Gate verdict: PASS if subset_cardinality <= 5, i.e. at least 2 axioms are
non-load-bearing for a_4 -> alpha_s.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Input SHA pins (logged in first 20 stdout lines)
# ---------------------------------------------------------------------------
INPUT_FILES = [
    "researchers/Connes/10_2007_Chamseddine_Connes_Marcolli_Gravity_standard_model.md",
    ".claude/agent-memory/connes-ncg-theorist/s83-w3-g54-hp-even-audit.md",
    "sessions/permanent-results-registry.md",
]


def sha256_of(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return "MISSING"
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# The 7-axiom NCG-SM roster (Connes 1995 + CCM-2007 §2.1)
# ---------------------------------------------------------------------------
AXIOMS = [
    {
        "id": "dim",
        "name": "Dimension",
        "statement": "Spectral dimension of (A, H, D) is a non-negative integer d; "
                     "eigenvalues lambda_n of |D| satisfy Weyl asymptotics "
                     "lambda_n ~ n^(1/d).",
        "invoked": True,
        "invocation_site": "Heat-kernel expansion Tr(exp(-t D^2)) ~ sum_k t^((k-d)/2) a_k; "
                           "a_4 is the k=4 coefficient in d=4 mod 8 convention.",
        "structural_dependency": "Without dimension axiom, heat-kernel index k of "
                                 "Seeley-DeWitt expansion is undefined; a_4 is "
                                 "structurally tied to d=4 conv.",
    },
    {
        "id": "reg",
        "name": "Regularity",
        "statement": "a and [D, a] lie in the smooth domain of delta^n = [|D|, .] "
                     "for all n (CCM-2007 auto-satisfied on finite A_F).",
        "invoked": True,
        "invocation_site": "Symbol of heat kernel requires smooth a; "
                           "Seeley-DeWitt coefficients are local integrals of "
                           "smooth jets of D^2.",
        "structural_dependency": "Without regularity, the heat kernel trace expansion "
                                 "fails to converge / loses asymptotic form.",
    },
    {
        "id": "fin",
        "name": "Finiteness",
        "statement": "The space H_inf = intersect_n Dom(D^n) is finitely-generated "
                     "projective module over A. On finite A_F: dim H_F < inf.",
        "invoked": True,
        "invocation_site": "Trace_F in a_4 = integral tr_F(E_2) dvol on M4 x F "
                           "requires finite-dim trace over H_F = C^32.",
        "structural_dependency": "Without finiteness, tr_F diverges; "
                                 "g_3^2 coefficient extraction (which pins alpha_s) "
                                 "requires a convergent sum over F.",
    },
    {
        "id": "real",
        "name": "Reality (J)",
        "statement": "Anti-unitary J: H -> H with J^2 = epsilon, J D = epsilon'' D J, "
                     "J gamma = epsilon' gamma J. KO-6 row: (eps, eps', eps'') = (+1,+1,-1).",
        "invoked": True,
        "invocation_site": "Fermionic action (1/2)<J psi, D psi> doubles to full "
                           "Dirac action; reality enforces absence of "
                           "fermion-doubling / Majorana structure which affects "
                           "Yukawa traces in c (Tr Y^*Y) feeding a_2, "
                           "but a_4 uses (Y^*Y)^2 trace (d-term of CCM-2007 eq. 3.14). "
                           "Without J, (Y^*Y)^2 trace structure is not well-defined.",
        "structural_dependency": "Reality is load-bearing for the fermionic "
                                 "closure that produces the d-term in a_4 (Higgs "
                                 "quartic) via coupling to right-handed neutrinos.",
    },
    {
        "id": "order1",
        "name": "First-order",
        "statement": "[[D, a], J b J^{-1}] = 0 for all a, b in A. "
                     "This is the 'bimodule' compatibility of D with left/right "
                     "A-actions.",
        "invoked": True,
        "invocation_site": "Inner-fluctuation decomposition D -> D + A + JAJ^{-1} "
                           "separates into gauge (from M4 sector) + Higgs (from F sector). "
                           "a_4 produces Yang-Mills Tr F^2 terms FROM the inner "
                           "fluctuation. Without first-order, no clean YM extraction, "
                           "no g_i^2 coefficients, no alpha_s.",
        "structural_dependency": "First-order is the gauge-sector backbone of "
                                 "a_4. Breaking first-order (even weakly as in "
                                 "Bochniak-Sitarz 2021) re-routes the a_4 "
                                 "structure; alpha_s depends on the 'strict' "
                                 "first-order decomposition.",
    },
    {
        "id": "orient",
        "name": "Orientability",
        "statement": "There exists a Hochschild cycle c of degree d with pi(c) = gamma "
                     "(volume form / chirality on F).",
        "invoked": False,
        "invocation_site": "Orientability selects the volume form / chirality "
                           "grading, not the eigenvalue content of D. "
                           "a_4 = Tr f(D^2/Lambda^2) is symmetric in lambda_n^2; "
                           "does not depend on the sign / orientation of the "
                           "grading cycle.",
        "structural_dependency": "a_4 coefficient extraction uses tr_F over the "
                                 "UNGRADED trace (even Seeley-DeWitt coefficient, "
                                 "k=4 even), so the orientation cycle is NOT invoked. "
                                 "Physical picture: alpha_s depends on g_3^2 "
                                 "(gauge coupling magnitude), not on the chirality sign.",
    },
    {
        "id": "PD",
        "name": "Poincare duality",
        "statement": "The intersection form on K-theory K_*(A) x K_*(A) -> Z "
                     "is non-degenerate.",
        "invoked": False,
        "invocation_site": "Poincare duality is a K-theoretic TOPOLOGICAL statement "
                           "on the algebra A; a_4 is a LOCAL spectral-action integral. "
                           "The eigenvalue spectrum of D does not invoke K-theory "
                           "of A in its computation.",
        "structural_dependency": "PD is used to CLASSIFY admissible finite algebras "
                                 "(CCM-2007 Theorem 2.1) -- i.e. to establish that "
                                 "A_F = C + H + M_3(C) is the UNIQUE choice. "
                                 "But GIVEN A_F, the a_4 coefficient on (A_F, H_F, D_F) "
                                 "is computed without invoking PD. Classification "
                                 "axiom, not computation axiom.",
    },
]


# ---------------------------------------------------------------------------
# Pre-registered thresholds
# ---------------------------------------------------------------------------
PASS_MAX = 5   # (local) subset_cardinality <= 5 -> PASS
FAIL_MIN = 7   # (local) subset_cardinality == 7 -> FAIL
# INFO = 6 (marginal)


def main() -> int:
    # Log input SHAs (first 20 lines)
    print("=" * 70)
    print("S85-W2-ALPHA-S-AXIOM-MINIMALITY-AU")
    print("=" * 70)
    input_shas: dict[str, str] = {}
    for f in INPUT_FILES:
        sha = sha256_of(f)
        input_shas[f] = sha
        print(f"INPUT  {f}  sha256={sha}")
    print("-" * 70)

    # Count invoked axioms
    invoked = [a for a in AXIOMS if a["invoked"]]
    not_invoked = [a for a in AXIOMS if not a["invoked"]]
    subset_cardinality = len(invoked)

    # Verdict
    if subset_cardinality <= PASS_MAX:
        verdict = "PASS"
    elif subset_cardinality == 6:
        verdict = "INFO"
    else:
        verdict = "FAIL"

    # Build closure hash from pin-map (input SHAs + axiom invocation tally)
    pin_map_str = json.dumps(
        {
            "inputs": input_shas,
            "invoked_ids": sorted([a["id"] for a in invoked]),
            "not_invoked_ids": sorted([a["id"] for a in not_invoked]),
            "subset_cardinality": subset_cardinality,
        },
        sort_keys=True,
    )
    closure_sha = hashlib.sha256(pin_map_str.encode()).hexdigest()
    content_sha = hashlib.sha256(
        json.dumps({"axioms": AXIOMS}, sort_keys=True).encode()
    ).hexdigest()

    # Emit JSON
    out_json = {
        "gate_id": "S85-W2-ALPHA-S-AXIOM-MINIMALITY-AU",
        "verdict": verdict,
        "value_4tuple": {
            "value": subset_cardinality,
            "scheme": "axiom-invocation-trace",
            "convention": "CCM-2007",
            "L_max": "N/A",
        },
        "axiom_table": AXIOMS,
        "invoked_ids": [a["id"] for a in invoked],
        "not_invoked_ids": [a["id"] for a in not_invoked],
        "closure_sha256": closure_sha,
        "content_sha256": content_sha,
        "input_shas": input_shas,
    }
    out_path = Path(__file__).with_suffix(".json")
    out_path.write_text(json.dumps(out_json, indent=2))
    print(f"WROTE {out_path}")

    # Print 7-row axiom table
    print("-" * 70)
    print(f"{'ID':<8}{'Name':<22}{'Invoked':<10}Invocation site")
    print("-" * 70)
    for a in AXIOMS:
        flag = "Y" if a["invoked"] else "N"
        print(f"{a['id']:<8}{a['name']:<22}{flag:<10}{a['invocation_site'][:35]}...")
    print("-" * 70)
    print(f"Subset cardinality = {subset_cardinality} / 7")
    print(f"Invoked:     {', '.join(a['id'] for a in invoked)}")
    print(f"Not invoked: {', '.join(a['id'] for a in not_invoked)}")
    print(f"VERDICT: {verdict}")
    print(f"closure_sha256 = {closure_sha}")
    print(f"content_sha256 = {content_sha}")

    # Final 4-tuple line
    print(
        f"4-tuple: value={subset_cardinality}, scheme=axiom-invocation-trace, "
        f"convention=CCM-2007, L_max=N/A"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
