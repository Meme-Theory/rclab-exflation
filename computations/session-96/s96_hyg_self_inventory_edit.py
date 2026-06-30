# -*- coding: utf-8 -*-
"""
S96-HYG-SELF-INVENTORY  (METHODOLOGY-class)
Atomic section-scoped splice of FOUR omitted PROVEN results into the capstone
sessions/framework/phonic-exflation-equation.md  §7.1 / §7.2 / §9.

This is NOT a threshold-producing compute. It:
  (1) reads the capstone in full,
  (2) splices ONLY the §7.1 table rows (+ §7.2 falsifier rows + §9 spine clause),
      preserving every other byte verbatim,
  (3) computes content_sha256 over the §7/§9 capstone_section_diff (the inserted
      block text), audit_sha256 over the ordered input-pin map,
  (4) fsync + os.replace (atomic) under concurrent-contention discipline,
  (5) appends the canonical dual-SHA + schema-v2 3-tuple verdict line.

NO truncate-and-rewrite of the verdict file: append_verdict-style atomic open("a").
NO bulk append to the capstone: read -> splice exact anchors -> os.replace.
"""
import hashlib
import os
import sys
from pathlib import Path

# Canonical-constants import (math-scripts.md MANDATORY): the f·σ₈ scorecard values are
# canonical pins, not transcriptions — import them so a future canonical re-pin propagates
# here automatically rather than silently drifting from a hardcoded literal.
sys.path.insert(0, str(Path(r"C:\sandbox\Ainulindale Exflation") / "computations" / "_shared"))
from canonical_constants import (  # noqa: E402
    f_FW,
    f_LCDM,
    fsigma8_product_suppression_FW_max_pct,
    f_bare_suppression_FW_pct,
)

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
CAPSTONE = ROOT / "sessions" / "framework" / "phonic-exflation-equation.md"
CANON = ROOT / "computations" / "_shared" / "canonical_constants.py"
VERDICTS = ROOT / "computations" / "session-96" / "s96_gate_verdicts.txt"

GATE_ID = "S96-HYG-SELF-INVENTORY"
SCHEME = "scorecard-self-inventory-completion"
CONVENTION = "row-with-provenance-and-Layer-tag"
LMAX = "N/A"


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# ---------------------------------------------------------------------------
# The four inserted blocks (verbatim from PROVEN priors; transcribe, do not derive).
# Values pinned from canonical_constants.py + knowledge MCP (see WP MCP Pre-Compute Audit).
# ---------------------------------------------------------------------------

# (A) §7.1 -- THREE new rows: f*sigma8 (a2 growth), normal ordering (a4/fiber neutrino),
#     c_s^2=0 (a2 Goldstone, SCORECARD pointer to W7-8 registry).
ROW_FSIGMA8 = (
    "| **f·σ₈(z)†** (RSD growth) | `a₂` growth / E33 | "
    "**−4.058%** f·σ₈ PRODUCT suppression vs ΛCDM at z=0.51 (zero-free-parameter; "
    "`f_FW=0.525492` vs `f_LCDM=0.527130`, bare-f −0.311% — the PRODUCT, NOT bare-f) | "
    "DESI-5yr / Euclid RSD | **PASS-class** (S₈-tension-relieving sign; S77 PROVEN / "
    "S96-OBS-FSIGMA8-FORECAST; σ-dist 1.013 DESI-Y5 / 1.534 Euclid) |"
)
ROW_NU_ORDER = (
    "| **ν mass ordering** | `a₄`/fiber neutrino / E-seesaw | "
    "**Normal B1<B2<B3** (zero-free-parameter; dynamical via the τ=0.107 B1↓-below-B2 "
    "crossing of D_K's (1,1,0)-sector) | NuFit-6.0 (NO preferred ~2.5σ) | "
    "**PASS** (structural, machine-ε; S8/S34–36/S52/S56) |"
)
ROW_CS2 = (
    "| **c_s² (dark-sector sound speed)** | `a₂` Goldstone / Kasparov-factorized | "
    "**0 exactly** (Layer-1 topological; `m_Goldstone^{4D}=0` by Kasparov product "
    "factorization; bound `<9.21×10⁻⁴`, scheme-independent) | dark-sector c_s² (DES/KiDS, "
    "future) | **PASS-class** (SCORECARD pointer; full §VII registry anatomy = W7-8) |"
)

# (B) §7.2 -- TWO new falsifier rows (#5 f*sigma8, #6 normal ordering); fill the
#     existing #3->#7 gap WITHOUT relabeling any existing row. Forecast sigma-distances
#     are the in-session scorecard entry; the DESI/Euclid + JUNO/DUNE forecast ROWS in
#     falsifier-master-inventory.md route to mack-cosmic-bridge (sole writer).
FROW_FSIGMA8 = (
    "| **#5** | f·σ₈(z) | **DESI-5yr 2029 → Euclid 2030s** | "
    "zero-parameter RSD discriminator; −4.058% product suppression, S₈-tension-relieving "
    "sign (σ-dist 1.013 DESI-Y5 / 1.534 Euclid; the *shape+sign* breaks the static-σ₈ "
    "degeneracy) |"
)
FROW_NU_ORDER = (
    "| **#6** | ν mass ordering | **JUNO 2026+ / DUNE 2030s** | "
    "zero-parameter normal-ordering prediction (B1<B2<B3, dynamical τ=0.107 crossing); "
    "a NO-vs-IO detector verdict is a clean yes/no on the (1,1,0)-sector substrate ordering |"
)

# (C) §9 geometry/topology spine -- the Omega=0 trivial-holonomy clause.
#     SCOPED to "computed invariants are trivial", NOT "topology is nontrivial".
SPINE_OMEGA = (
    " The **trivial Berry holonomy** is the cleanest illustration of this survival: "
    "the closed-loop holonomy on the Jensen line is `γ=0` and the Fubini–Study distance "
    "`d_FS=0` (S61; the SU(3) connection is flat ⇒ the **computed holonomy invariants are "
    "trivial** — read as *the invariants we computed came out trivial*, NOT as a claim that "
    "the substrate topology is nontrivial), and that triviality is a representation-theoretic "
    "fact that survives the continuum dissolution unchanged."
)


def main():
    # Guard: the prose rows quote rounded forms of these canonical pins. Assert the
    # imported canonical values still round to the quoted forms (drift tripwire).
    assert round(f_FW, 6) == 0.525492, f"f_FW drift: {f_FW}"  # (local)
    assert round(f_LCDM, 6) == 0.527130, f"f_LCDM drift: {f_LCDM}"  # (local)
    assert abs(fsigma8_product_suppression_FW_max_pct - (-4.058)) < 1e-9, \
        f"product-supp drift: {fsigma8_product_suppression_FW_max_pct}"  # (local)
    assert abs(f_bare_suppression_FW_pct - (-0.311)) < 1e-9, \
        f"bare-f drift: {f_bare_suppression_FW_pct}"  # (local)

    text = CAPSTONE.read_text(encoding="utf-8")
    original_len = len(text.encode("utf-8"))

    # --- Anchor 1: §7.1 -- after the sigma_8 row ---
    anchor_sigma8 = (
        "| **σ₈†** | `a₂` growth / E33 | **0.799** (zero-free-parameter) | "
        "Planck `0.829`; lensing `~0.76` | VIABLE (~2σ between, not a resolution) |"
    )
    if anchor_sigma8 not in text:
        sys.stderr.write("ANCHOR-FAIL: §7.1 sigma_8 row not found verbatim\n")
        sys.exit(2)
    insert_71 = anchor_sigma8 + "\n" + ROW_FSIGMA8 + "\n" + ROW_NU_ORDER + "\n" + ROW_CS2
    if text.count(anchor_sigma8) != 1:
        sys.stderr.write("ANCHOR-FAIL: §7.1 sigma_8 anchor not unique\n")
        sys.exit(2)
    text = text.replace(anchor_sigma8, insert_71, 1)

    # --- Anchor 2: §7.2 -- after the #3 alpha_s falsifier row ---
    anchor_f3 = (
        "| **#3** | α_s | **CMB-S4 2030 → CMB-HD 2035** | "
        "~34σ-reach falsifier of the `s=3` Mellin-residue identity at the matched channel |"
    )
    if anchor_f3 not in text or text.count(anchor_f3) != 1:
        sys.stderr.write("ANCHOR-FAIL: §7.2 #3 falsifier row not found/unique\n")
        sys.exit(2)
    insert_72 = anchor_f3 + "\n" + FROW_FSIGMA8 + "\n" + FROW_NU_ORDER
    text = text.replace(anchor_f3, insert_72, 1)

    # --- Anchor 3: §9 spine -- append the Omega=0 clause to the geometry/topology spine.
    # Anchor on the closing sentence of the spine blockquote (the FI ratio-observables list end).
    anchor_spine = (
        "every honest gap lives on the dissolving side."
    )
    if anchor_spine not in text or text.count(anchor_spine) != 1:
        sys.stderr.write("ANCHOR-FAIL: §9 spine closing sentence not found/unique\n")
        sys.exit(2)
    insert_spine = anchor_spine + SPINE_OMEGA
    text = text.replace(anchor_spine, insert_spine, 1)

    # --- content_sha256 over the §7/§9 capstone_section_diff (the inserted block) ---
    # The diff text is the ordered concatenation of every inserted row/clause.
    section_diff = "\n".join([
        ROW_FSIGMA8, ROW_NU_ORDER, ROW_CS2,
        FROW_FSIGMA8, FROW_NU_ORDER,
        SPINE_OMEGA.strip(),
    ])
    content_sha = sha256_text(section_diff)

    # --- audit_sha256 over the ordered input-pin map ---
    pinmap = "\n".join([
        f"_gate_id={GATE_ID}",
        f"_scheme={SCHEME}",
        f"_convention={CONVENTION}",
        f"_L_max={LMAX}",
        f"capstone_section_diff_sha={content_sha}",
        f"capstone_pre_edit_sha={sha256_file(CAPSTONE)}",  # capstone state BEFORE this run's replace
        f"canonical_sha={sha256_file(CANON)}",
        f"pin:f_FW={f_FW!r}",
        f"pin:f_LCDM={f_LCDM!r}",
        f"pin:fsigma8_product_suppression_FW_max_pct={fsigma8_product_suppression_FW_max_pct!r}",
        f"pin:f_bare_suppression_FW_pct={f_bare_suppression_FW_pct!r}",
        "pin:sigma8_fw=0.793166",
        "pin:c_s2=0_Kasparov_bound_lt_9.21e-4",
        "pin:nu_ordering=Normal_B1<B2<B3_tau_cross=0.107",
        "pin:Omega_holonomy=0_d_FS=0_S61",
    ])
    audit_sha = sha256_text(pinmap)

    # --- atomic write: tmp -> fsync -> os.replace ---
    tmp = CAPSTONE.with_suffix(".md.s96w75.tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, CAPSTONE)

    new_len = len(text.encode("utf-8"))

    # --- verdict line: canonical + dual-SHA companion + schema-v2 3-tuple companion ---
    # SIGN: substitution chain Step 4 predicts discriminating_power(f*sigma8) > discriminating_power(sigma8)
    #       => omitting f*sigma8 UNDER-states LSS reach => adding it STRENGTHENS the inventory.
    #       Computed direction: the MORE discriminating observable was ABSENT, the LESS present
    #       => sign matches predicted direction => sign_verdict=PASS.
    # MAGNITUDE: artifact-existence set-membership; all 4 rows landed => PASS.
    # REGIME: documentation edit, no expansion / numerical window => VALID.
    value = (
        "rows_landed=4;"
        "f_sigma8_PRODUCT_supp=-4.058pct@z0.51(bare_f=-0.311pct;f_FW=0.525492,f_LCDM=0.527130);"
        "nu_ordering=Normal_B1<B2<B3_tau_cross=0.107_zeroparam;"
        "c_s2=0_Kasparov_bound<9.21e-4_SCORECARD_pointer_to_W7-8;"
        "Omega_holonomy=0_d_FS=0_scoped_computed-invariants-trivial_NOT_topology-nontrivial;"
        f"capstone_bytes={original_len}->{new_len};"
        "f_sigma8_MORE_discriminating_than_static_sigma8(shape+sign_breaks_degeneracy)=True;"
        "falsifier_rows(f_sigma8_DESI/Euclid;nu_JUNO/DUNE)_route_to_mack-cosmic-bridge"
    )
    canonical = (
        f"{GATE_ID}: PASS -- value='{value}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={LMAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; content over §7/§9 capstone_section_diff (6 inserted blocks); audit over ordered input-pin map"
    )
    tuple3 = (
        "# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        "sign = substitution-chain Step 4 predicts discriminating_power(f·σ₈) > discriminating_power(σ₈) "
        "[z-dependent shape + zero-parameter -4.058% suppression sign breaks degeneracies the static σ₈~0.799 cannot] "
        "=> the MORE discriminating observable (f·σ₈) was ABSENT while the LESS (σ₈) PRESENT => omitting it UNDER-states LSS reach "
        "=> computed direction matches predicted => PASS; "
        "mag = artifact-existence set-membership, all 4 PROVEN rows landed with value+provenance+Layer tag => PASS; "
        "regime = documentation Edit on §7.1/§7.2/§9, no small-parameter expansion / numerical window => VALID"
    )

    with open(VERDICTS, "a", encoding="utf-8") as f:
        f.write(canonical + "\n")
        f.write(companion + "\n")
        f.write(tuple3 + "\n")

    print("=== INPUT SHAs (first 20 lines of stdout) ===")
    print(f"capstone_pre_edit (BEFORE replace) : recorded in pinmap")
    print(f"canonical_constants.py             : {sha256_file(CANON)}")
    print(f"content_sha256 (§7/§9 diff)        : {content_sha}")
    print(f"audit_sha256   (input-pin map)     : {audit_sha}")
    print(f"capstone bytes {original_len} -> {new_len}  (delta=+{new_len - original_len})")
    print("=== 4-tuple ===")
    print(f"value=4-row-set scheme={SCHEME} convention={CONVENTION} L_max={LMAX}")
    print("VERDICT: PASS (4 rows landed)")
    sys.exit(0)


if __name__ == "__main__":
    main()
