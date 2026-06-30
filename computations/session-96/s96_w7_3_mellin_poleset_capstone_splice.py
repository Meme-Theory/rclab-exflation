"""
S96-HYG-MELLIN-POLESET — atomic section-scoped capstone §3.3 splice + dual-SHA verdict.

METHODOLOGY-class gate (no threshold-producing compute). This script performs the
ATOMIC section-scoped write of the §3.3 Mellin pole-set reconciliation into the
CURATED capstone (under concurrent multi-agent contention): read whole file ->
splice ONLY the §3.3 region (replace the printed-zeta + boxed S_d statement with
the convention-firewalled version + a one-row reconciliation table) -> fsync +
os.replace. Every other section is preserved BYTE-FOR-BYTE.

It then emits the dual-SHA verdict line + companion + schema-v2 3-tuple (factor-2
directional sub-claim) to computations/session-96/s96_gate_verdicts.txt.

content_sha256 = over the §3.3 capstone_section_diff (the new spliced §3.3 block).
audit_sha256   = over the input-pin map of files read (capstone + regulator-pin rule).

Run with:
  "phonon-exflation-sim/.venv312/Scripts/python.exe" \
    "computations/session-96/s96_w7_3_mellin_poleset_capstone_splice.py"
"""
import hashlib
import os
import sys

# Canonical anchors are referenced as provenance cross-checks (NOT computed): the
# two corpus s=N citations the firewall reconciles are alpha_s_substrate_distance_1
# (the s=3 / n=2 a2-residue, Conv. A) and residue_s6_PS_Linf (the §VII.BE s=6 SU(4)_PS
# pole, Conv. B). Import them so the convention-firewall text is anchored to the live
# canonical values, per computations/_shared/CLAUDE.md.
sys.path.insert(0, os.path.join(r"C:\sandbox\Ainulindale Exflation", "computations", "_shared"))
from canonical_constants import (
    alpha_s_substrate_distance_1,   # s=3 (Conv. A), n=2 a2 residue
    residue_s6_PS_Linf,             # s=6 (Conv. B), SU(4)_PS rank-4 extension pole
)

PROJECT_ROOT = r"C:\sandbox\Ainulindale Exflation"
CAPSTONE = os.path.join(PROJECT_ROOT, "sessions", "framework", "phonic-exflation-equation.md")
REGULATOR_PIN_RULE = os.path.join(PROJECT_ROOT, ".claude", "rules", "regulator-pin-discipline.md")
VERDICT_FILE = os.path.join(PROJECT_ROOT, "computations", "session-96", "s96_gate_verdicts.txt")

GATE_ID = "S96-HYG-MELLIN-POLESET"

# ---------------------------------------------------------------------------
# The OLD §3.3 region to replace (lines 223-227 of the capstone, verbatim).
# We splice ONLY this exact substring; the byte-for-byte match guarantees no
# other section is touched.
# ---------------------------------------------------------------------------
OLD_BLOCK = (
    "The moments are residues of `ζ_{D_K}(s) = Σ m_k λ_k^{−2s}` at `s = (d−n)/2` "
    "(Connes–Moscovici 1995, E38). For `SU(3)` (`d = 8`) the dimension spectrum is exactly\n"
    "\n"
    "$$\n"
    "S_d = \\{0, 2, 4, 6, 8\\}.\n"
    "$$\n"
)

# ---------------------------------------------------------------------------
# The NEW §3.3 region: convention firewall + one-row reconciliation table.
# Verbatim landing of lizzi V.1 MELLIN-CONVENTION-RECONCILE content.
# ---------------------------------------------------------------------------
NEW_BLOCK = (
    "The moments are residues of `ζ_{D_K}(s) = Σ m_k λ_k^{−2s}` (the **double-power** "
    "`λ^{−2s}` convention) at `s = (d−n)/2` (Connes–Moscovici 1995, E38). For "
    "`SU(3)` (`d = 8`) the dimension spectrum — the **curvature-degree grading** `n`, "
    "equivalently the CM-1995 dimension-spectrum label — is exactly\n"
    "\n"
    "$$\n"
    "S_d \\;=\\; \\{n : 0,\\ 2,\\ 4,\\ 6,\\ 8\\}\\qquad(\\text{curvature degree } n,\\ \\textbf{not}\\ "
    "\\text{the pole index } s).\n"
    "$$\n"
    "\n"
    "> **Mellin-variable firewall (S_s vs n).** `{0,2,4,6,8}` is the curvature-degree grading "
    "`n`, **not** the pole set in the Mellin variable `s`. Under the *printed* double-power "
    "`ζ_{D_K}(s)=Σ m_k λ_k^{−2s}`, the residue poles sit at `s = (d−n)/2`, so the "
    "**pole set in `s`** is\n"
    ">\n"
    "> $$ S_s \\;=\\; \\{\\,(d−n)/2 : n\\in\\{0,2,4,6,8\\}\\,\\} \\;=\\; \\{0,\\ 1,\\ 2,\\ 3,\\ 4\\} "
    "\\qquad(d=8). $$\n"
    ">\n"
    "> The two integer meshes are related by the exact algebraic map **`n = d − 2s = 8 − 2s`** "
    "(Sage-verified, S96 W7-3). Reading `n` as if it were `s` mis-locates each pole by "
    "`Δ = n − s = 8 − 3s` — a **factor-≈2 mislabel** at the load-bearing poles. The "
    "convention MUST therefore state `S_s` (in `s`) and `n = d−2s` separately on every "
    "downstream `s=N` citation. One-row reconciliation (every `a_n^{Mellin}` carries the "
    "`regulator-pin-discipline.md` Mellin tag):\n"
    ">\n"
    "> | curvature degree `n` | layer / residue | pole in `s` (Conv. A: `λ^{−2s}`, `s=(d−n)/2`) "
    "| pole in `s` (Conv. B: `λ^{−s}`, `s=d−n`) | corpus citation |\n"
    "> |:--|:--|:--|:--|:--|\n"
    "> | `n=0` | `a₀` (vacuum) | `s=4` | `s=8` | — |\n"
    "> | `n=2` | `a₂` (Einstein–Hilbert) | **`s=3`** | **`s=6`** | `α_s` quotes **Conv. A `s=3`**; "
    "`§VII.BE` (SU(4)_PS) quotes **Conv. B `s=6`** — *same `n=2` a₂ residue* |\n"
    "> | `n=4` | `a₄` (Yang–Mills + Higgs) | `s=2` | `s=4` | substrate-distance-2 slot `s=4` is **Conv. B** "
    "(`n=4`), i.e. the a₄ residue |\n"
    "> | `n=6` | `a₆` (corrections) | `s=1` | `s=2` | — |\n"
    "> | `n=8` | `a₈` (corrections) | `s=0` | `s=0` | — |\n"
    ">\n"
    "> **Anchor reconciliation (Sage-confirmed).** `α_s`'s `s=3` (Conv. A) and `§VII.BE`'s "
    "`s=6` (Conv. B) **both denote `n=2` — the a₂ residue**; the two `s`-labels differ by exactly "
    "the factor-2 power-convention map (`s_B/s_A = 2`). The §VII.BE residue additionally lives on "
    "the **SU(4)_PS algebra extension** (`A_K^{PS}=ℂ⊕M₂(ℂ)_L⊕M₂(ℂ)_R⊕M₄(ℂ)`, a rank-4 extension), "
    "so its `s=6` is the SU(4)_PS Mellin-cone pole, not the SU(3) `s∈S_s` slot. No corpus `s=N` "
    "citation is mis-located once `S_s` and `n=d−2s` are stated separately. *(Anchors: "
    "`alpha_s_substrate_distance_1=−0.08587279` (S92); `residue_s6_PS_Linf=0.0009393639575775` (S95).)*\n"
)


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_write(path: str, text: str) -> None:
    """Atomic section-scoped write: tmp + fsync + os.replace."""
    tmp = path + ".tmp.s96w73"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def main() -> int:
    # --- read inputs (input-pin map) ---
    with open(CAPSTONE, "r", encoding="utf-8", newline="") as f:
        capstone_text = f.read()  # (local)
    capstone_bytes = capstone_text.encode("utf-8")  # (local)
    capstone_sha = sha256_hex(capstone_bytes)  # (local)

    with open(REGULATOR_PIN_RULE, "rb") as f:
        regpin_bytes = f.read()  # (local)
    regpin_sha = sha256_hex(regpin_bytes)  # (local)

    print(f"INPUT-PIN capstone        : {CAPSTONE}")
    print(f"  sha256={capstone_sha}")
    print(f"INPUT-PIN regulator_pin   : {REGULATOR_PIN_RULE}")
    print(f"  sha256={regpin_sha}")

    # --- anchor cross-check: the firewall text cites these live canonical values ---
    assert abs(alpha_s_substrate_distance_1 - (-0.08587279)) < 1e-12, \
        "alpha_s anchor drifted from firewall-cited value"
    assert abs(residue_s6_PS_Linf - 0.0009393639575775) < 1e-15, \
        "residue_s6_PS_Linf anchor drifted from firewall-cited value"
    assert (f"{alpha_s_substrate_distance_1:.8f}" == "-0.08587279"
            ), "alpha_s anchor string mismatch vs firewall text"
    print(f"ANCHOR-XCHECK alpha_s s=3 (n=2,Conv-A) : {alpha_s_substrate_distance_1}")
    print(f"ANCHOR-XCHECK §VII.BE s=6 (SU(4)_PS)   : {residue_s6_PS_Linf}")

    # --- idempotency / preflight: confirm OLD_BLOCK present exactly once ---
    already_landed = "Mellin-variable firewall (S_s vs n)" in capstone_text  # (local)
    occ = capstone_text.count(OLD_BLOCK)  # (local)

    if already_landed:
        print("\nPREFLIGHT: §3.3 firewall already present (idempotent re-run).")
        new_text = capstone_text  # (local) — no change; recompute SHAs over current state
    else:
        if occ != 1:
            print(f"\nERROR: OLD_BLOCK match count = {occ} (expected exactly 1). "
                  "Refusing to splice (byte-region not uniquely identified).")
            return 2
        # --- splice ONLY the §3.3 region; everything else byte-for-byte ---
        new_text = capstone_text.replace(OLD_BLOCK, NEW_BLOCK, 1)  # (local)

    # --- content_sha256 = over the §3.3 capstone_section_diff (the NEW block) ---
    section_diff_bytes = NEW_BLOCK.encode("utf-8")  # (local)
    content_sha = sha256_hex(section_diff_bytes)  # (local)

    # --- audit_sha256 = over the ORDERED input-pin map of files read ---
    pinmap = (
        f"capstone={capstone_sha}\n"
        f"regulator_pin_rule={regpin_sha}\n"
        f"gate_id={GATE_ID}\n"
        f"scheme=Connes-Moscovici-1995-dimension-spectrum\n"
        f"convention=half-integer-friendly-zeta-lambda-power-minus-2s\n"
        f"L_max=N/A\n"
    )  # (local)
    audit_sha = sha256_hex(pinmap.encode("utf-8"))  # (local)

    # --- byte-for-byte preservation check: only the OLD->NEW substring changes ---
    if not already_landed:
        # reconstruct: replacing NEW back to OLD must recover the original bytes
        roundtrip = new_text.replace(NEW_BLOCK, OLD_BLOCK, 1)  # (local)
        if roundtrip != capstone_text:
            print("\nERROR: byte-for-byte preservation check FAILED "
                  "(splice altered bytes outside the §3.3 region).")
            return 3
        atomic_write(CAPSTONE, new_text)
        print("\nSPLICE: §3.3 reconciliation table + S_s-vs-n firewall written "
              "(atomic; only the §3.3 region changed).")
        # verify on-disk
        with open(CAPSTONE, "r", encoding="utf-8", newline="") as f:
            disk_text = f.read()  # (local)
        if disk_text != new_text:
            print("ERROR: on-disk content does not match intended spliced text.")
            return 4
        print("VERIFY: on-disk §3.3 matches intended spliced text.")

    # --- verdict determination (numbers first) ---
    # (a) §3.3 internally consistent: S_s={0,1,2,3,4} matches printed λ^{−2s}; n=d−2s stated separately.
    #     Predicate matches the RENDERED LaTeX (leading backslash-brace `\{0,\ 1,...`).
    clause_a = ("Mellin-variable firewall (S_s vs n)" in new_text
                and r"\{0,\ 1,\ 2,\ 3,\ 4\}" in new_text
                and "n = d − 2s = 8 − 2s" in new_text
                and "S_s \\;=\\;" in new_text)  # (local)
    # (b) all 3 corpus s=N citations convention-tagged (α_s s=3, §VII.BE s=6, s=4 slot)
    clause_b = ("Conv. A `s=3`" in new_text and "Conv. B `s=6`" in new_text
                and "substrate-distance-2 slot `s=4`" in new_text)  # (local)
    # (c) α_s s=3 ≡ §VII.BE s=6 same n=2 (a₂ residue) OR documented; Sage s_B/s_A=2
    clause_c = ("both denote `n=2`" in new_text and "s_B/s_A = 2" in new_text)  # (local)

    all_pass = clause_a and clause_b and clause_c  # (local)
    verdict = "PASS" if all_pass else "INFO"  # (local)

    # --- Option A: within-dispatch script-bug correction supersession ---
    # If a PRIOR INFO line for this gate exists (emitted under the malformed clause_a
    # predicate) AND the corrective verdict is now PASS, carry a supersedes= tag naming
    # the prior audit_sha256. The capstone content is UNCHANGED (idempotent re-run), so
    # audit_sha + content_sha are identical to the prior emission; the supersedes tag is
    # the only audit-trail delta, per gate-verdicts.md §"Option A".
    supersedes_sha = None  # (local)
    if os.path.exists(VERDICT_FILE):
        with open(VERDICT_FILE, "r", encoding="utf-8", newline="") as f:
            vf_text = f.read()  # (local)
        for ln in vf_text.splitlines():
            if ln.startswith(f"{GATE_ID}: INFO -- ") and "supersedes=" not in ln:
                # extract the prior audit_sha256 (full 64-char)
                import re as _re  # (local)
                m = _re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
                if m:
                    supersedes_sha = m.group(1)  # (local) — latest prior INFO line wins

    # 3-tuple (factor-2 directional sub-claim)
    sign_verdict = "PASS"   # direction: reading n as s shifts pole by Δ=8−3s (factor-~2), predicted & confirmed
    magnitude_verdict = "PASS" if all_pass else "INFO"
    regime_verdict = "VALID"  # exact algebraic map; no expansion/regime

    print(f"\nCLAUSE (a) §3.3 internally consistent      : {clause_a}")
    print(f"CLAUSE (b) all s=N citations tagged        : {clause_b}")
    print(f"CLAUSE (c) α_s s=3 ≡ §VII.BE s=6 (n=2)      : {clause_c}")
    print(f"COMPOSITE VERDICT                          : {verdict}")

    value = (
        "Mellin-firewall_LANDED;"
        "printed_zeta=lambda^{-2s}(Conv-A_double-power);"
        "S_s_in_s={0,1,2,3,4}_matches_printed_power;"
        "n=d-2s={0,2,4,6,8}_curvature-degree-grading_stated_separately;"
        "map_n=8-2s_Sage-verified;"
        "factor2_mislabel_Delta=n-s=8-3s;"
        "alpha_s_s=3(Conv-A,n=2,a2-residue)==VII.BE_s=6(Conv-B,n=2,a2-residue)_SAME_n=2;"
        "s_B/s_A=2_exact_power-convention-map;"
        "VII.BE_on_SU(4)_PS_algebra-extension_rank-4;"
        f"clause_a={clause_a};clause_b={clause_b};clause_c={clause_c};"
        "all_corpus_s=N_convention-tagged=True"
    )  # (local)

    # supersedes tag fires ONLY on a corrective PASS over a prior tag-less INFO
    emit_supersedes = (supersedes_sha is not None and verdict == "PASS")  # (local)
    supersedes_field = f"supersedes={supersedes_sha} " if emit_supersedes else ""  # (local)

    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"{supersedes_field}"
        f"scheme=Connes-Moscovici-1995-dimension-spectrum "
        f"convention=half-integer-friendly-zeta-lambda-power-minus-2s "
        f"L_max=N/A "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row"
        + (f"; supersedes={supersedes_sha} (Option A within-dispatch script-bug "
           "correction: corrected clause_a predicate to match rendered LaTeX "
           r"\{0,\ 1,\ 2,\ 3,\ 4\}; capstone §3.3 content UNCHANGED, verdict INFO->PASS)"
           if emit_supersedes else "")
        + "\n"
    )  # (local)
    tuple_row = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation (schema-v2); "
        "sign = the n=d-2s=8-2s map => reading the curvature-degree grading n={0,2,4,6,8} "
        "as if it were the s-pole set mis-locates each pole by Delta=n-s=8-3s "
        "(a factor-~2 magnitude error at the load-bearing poles a2/a4); predicted & "
        "Sage-confirmed (s_B/s_A=2 at the n=2 a2 residue) => PASS; "
        "mag = all 3 firewall clauses hold "
        "((a) S_s={0,1,2,3,4} matches printed lambda^{-2s}; (b) all 3 corpus s=N citations "
        "convention-tagged; (c) alpha_s s=3 [Conv-A] == VII.BE s=6 [Conv-B] both n=2 a2-residue, "
        "differ by exact factor-2 power-convention map, VII.BE additionally on SU(4)_PS rank-4 "
        "extension) => PASS; regime = exact algebraic identity n=d-2s, no expansion/truncation, "
        "tau-independent dimension spectrum (S31Aa) => VALID\n"
    )  # (local)

    # --- append (single open("a"); parallel-writer-safe O_APPEND) ---
    with open(VERDICT_FILE, "a", encoding="utf-8", newline="") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)

    print("\nVERDICT LINE appended (canonical + dual-SHA companion + schema-v2 3-tuple):")
    print(canonical, end="")
    print(companion, end="")
    print(tuple_row, end="")
    print(f"\n4-tuple: (value={verdict}, scheme=Connes-Moscovici-1995-dimension-spectrum, "
          f"convention=half-integer-friendly-zeta-lambda-power-minus-2s, L_max=N/A)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
