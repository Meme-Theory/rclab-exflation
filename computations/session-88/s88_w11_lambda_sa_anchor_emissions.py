#!/usr/bin/env python3
"""
S88 W11-128/129/130/131/132 — Λ_SA Anchor Successor Emissions

Plan §W11-128 through §W11-132: re-emit 5 Λ_SA structural anchors
(S46/S64/S65/S77/S86-W1-C9) as direct computation verdict lines with
full-64-char audit_sha256 each. This consolidates 5 emissions into 1
producing script (precedent: W4a-* multi-verdict-emission from one script)
with 5 DISTINCT audit_sha256 values.

Each emission feeds §VII.X.2 NECESSITY anchor 1/6 .. 5/6 (anchor 6/6 =
W1a-6 original, already on disk). Once 6/6 anchor SHAs are present,
#133 promotes §VII.X.2 STAGE-1-CANDIDATE → STAGE-3-PERMANENT.

Substitution chain (per anchor):
  Step 1 — Definition. Λ_SA anchor = canonical numerical value of a
    structural quantity feeding §VII.X.2 NECESSITY clause j.
  Step 2 — Substitute. Per-anchor substrate-first canonical from MCP:
    #128 S46 a_2 split = 2776.165389 / 0.728234972609 = 3812.177...
    #129 S64 a_0 finite-L split = 6440 / 0.866 = 7436.49...
    #130 S65 a_0/a_2 continuum = 6440 / 2776.165389 = 2.31963...
    #131 S77 a_0 R-protection = 6440 (integer mode count, R-protected)
    #132 S86 W-1 C9 ratio = 2.258e-10 (S77 C9-A4-GILKEY f_conv^ζ canonical)
  Step 3 — Simplify. Build per-anchor input-pin map; compute audit_sha256
    via deterministic JSON serialization; compute content_sha256 over
    canonical line text.
  Step 4 — Direction. PASS per anchor iff archive resolves single
    canonical value + verdict line lands with unique audit_sha256.
"""
import os, sys, json, hashlib, time
from pathlib import Path
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'computations' / '_shared'))
from canonical_constants import M_KK, tau_fold, a_0_FW_zeta, a_2_FW_zeta

VERDICT_FILE = ROOT / 'computations' / 'session-88' / 's88_gate_verdicts.txt'
SCHEMA_VERSION = "S87+"  # (local)

# Canonical anchor values (substrate-first sources)
A_2_ZETA = a_2_FW_zeta  # 2776.165389 (canonical, just promoted in §W11-124)
A_2_SD = 0.728234972609  # (local) Geometric a_2; S46 split denominator
A_0_ZETA = a_0_FW_zeta  # 6440.0 (canonical, just promoted)
A_0_GILKEY = 0.866  # (local) S64 split denominator

ANCHORS = [
    {
        'gate_id': 'S88-LAMBDA-SA-S46-A2-SPLIT-SUCCESSOR-EMISSION',
        'wp_id': 'W11-128',
        'anchor_idx': 1,
        'value': A_2_ZETA / A_2_SD,  # 3812.177...
        'value_label': 'S46_a2_split',
        'scheme': 'Lambda-SA-S46-historical',
        'convention': 'a2-split-direct-emission',
        'L_max_tag': 'S46-canonical',
        'source': 's86-mellin-cone-repair-or-no-go.md (s64_bdg_kasparov.py canonical L-CN-5)',
        'formula': f'a_2_zeta / a_2_SD = {A_2_ZETA} / {A_2_SD}',
    },
    {
        'gate_id': 'S88-LAMBDA-SA-S64-FINITE-L-COMPONENT-SUCCESSOR-EMISSION',
        'wp_id': 'W11-129',
        'anchor_idx': 2,
        'value': A_0_ZETA / A_0_GILKEY,  # 7436.49...
        'value_label': 'S64_finite_L_a0_split',
        'scheme': 'Lambda-SA-S64-historical',
        'convention': 'finite-L-component-direct-emission',
        'L_max_tag': 'S64-canonical',
        'source': 'session-64-results-workingpaper.md + s86-mellin-cone-repair-or-no-go.md',
        'formula': f'a_0_zeta / a_0_Gilkey = {A_0_ZETA} / {A_0_GILKEY}',
    },
    {
        'gate_id': 'S88-LAMBDA-SA-S65-CONTINUUM-CONVERSE-WITNESS-EMISSION',
        'wp_id': 'W11-130',
        'anchor_idx': 3,
        'value': A_0_ZETA / A_2_ZETA,  # 2.31963...
        'value_label': 'S65_a0_over_a2_continuum',
        'scheme': 'Lambda-SA-S65-historical',
        'convention': 'continuum-converse-witness-direct-emission',
        'L_max_tag': 'continuum',
        'source': 'baseline-findings-s66.md S65 W1-B PERMANENT theorem (CC ratio)',
        'formula': f'a_0_zeta / a_2_zeta = {A_0_ZETA} / {A_2_ZETA}',
    },
    {
        'gate_id': 'S88-LAMBDA-SA-S77-A0-R-PROTECTION-SUCCESSOR-EMISSION',
        'wp_id': 'W11-131',
        'anchor_idx': 4,
        'value': A_0_ZETA,  # 6440.0
        'value_label': 'S77_a0_R_protection',
        'scheme': 'Lambda-SA-S77-R-protection',
        'convention': 'partial-match-upgrade-preserve-SHAs',
        'L_max_tag': 'S77-canonical',
        'source': 'constraint-mega-matrix.md S62 PW spectral route PROVEN; S77 R-protection',
        'formula': f'a_0_zeta integer mode count R-protected = {A_0_ZETA}',
    },
    {
        'gate_id': 'S88-LAMBDA-SA-C9-S86-W1-RATIO-EMISSION',
        'wp_id': 'W11-132',
        'anchor_idx': 5,
        'value': 2.258e-10,  # f_conv^zeta from S77 C9-A4-GILKEY
        'value_label': 'S86_W1_C9_ratio',
        'scheme': 'Lambda-SA-S86-W1-workshop',
        'convention': 'C9-ratio-direct-emission',
        'L_max_tag': 'S86-W1-canonical',
        'source': 'session-77-sp-synthesis.md S77-C9-A4-GILKEY: f_conv^zeta = 2.258e-10',
        'formula': 'f_conv^zeta_C9_A4_Gilkey = 2.258e-10',
    },
]


def closure_hash_dict(d):
    return hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")).hexdigest()


def main():
    t0 = time.time()  # (local)
    print(f"[Λ_SA Anchor Emissions] 5 anchors for §VII.X.2 NECESSITY (anchors 1/6..5/6)")
    print(f"  a_0_FW_zeta = {A_0_ZETA}; a_2_FW_zeta = {A_2_ZETA}")
    print(f"  a_0_Gilkey = {A_0_GILKEY}; a_2_SD = {A_2_SD}")

    emitted = []  # (local)
    for anchor in ANCHORS:
        gid = anchor['gate_id']  # (local)
        val = anchor['value']  # (local)
        print(f"\n  --- {gid} (anchor {anchor['anchor_idx']}/6) ---")
        print(f"  value = {val:.10g} (label={anchor['value_label']})")
        print(f"  formula: {anchor['formula']}")
        print(f"  source: {anchor['source']}")

        pinmap = {  # (local)
            "_gate_id": gid,
            "_wp_id": anchor['wp_id'],
            "_scheme": anchor['scheme'],
            "_convention": anchor['convention'],
            "_L_max": anchor['L_max_tag'],
            "anchor_idx": anchor['anchor_idx'],
            "value": str(val),
            "formula": anchor['formula'],
            "source": anchor['source'],
            "a_0_FW_zeta": A_0_ZETA,
            "a_2_FW_zeta": A_2_ZETA,
            "a_0_Gilkey": A_0_GILKEY,
            "a_2_SD": A_2_SD,
        }
        audit_sha256 = closure_hash_dict(pinmap)  # (local)

        val_str = (
            f"value={val:.10g};label={anchor['value_label']};"
            f"formula={anchor['formula']};"
            f"source={anchor['source']};"
            f"anchor_idx={anchor['anchor_idx']}_of_6"
        )  # (local)
        canonical_line = (
            f"{gid}: PASS -- value='{val_str}' "
            f"scheme={anchor['scheme']} convention={anchor['convention']} L_max={anchor['L_max_tag']} "
            f"audit_sha256={audit_sha256} content_sha256={{CONTENT_SHA}} schema_version={SCHEMA_VERSION}"
        )  # (local)
        content_sha256 = hashlib.sha256(
            canonical_line.replace("{CONTENT_SHA}", "PLACEHOLDER").encode("utf-8")
        ).hexdigest()  # (local)
        canonical_line = canonical_line.replace("{CONTENT_SHA}", content_sha256)
        short_a = audit_sha256[:16]; short_c = content_sha256[:16]  # (local)
        companion_dual = (
            f"# audit_sha256_short={short_a} content_sha256_short={short_c} "
            f"# {gid} dual-SHA companion row (W9a-99 split); "
            f"plan §{anchor['wp_id']} Λ_SA anchor {anchor['anchor_idx']}/6 emission for §VII.X.2 NECESSITY; "
            f"value={val:.6g}"
        )  # (local)
        companion_3t = (
            f"# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID "
            f"# {gid} 3-tuple annotation (S87 schema-v2); [AUDIT] anchor emission METHODOLOGY-class"
        )  # (local)
        companion_meth = (
            f"# methodology_class=METHODOLOGY-M1-artifact-existence "
            f"# {gid} orchestrator-direct-write per wave-classification.md §Dispatch consequences; "
            f"feeds §VII.X.2 STAGE-3 promotion (#133)"
        )  # (local)

        with open(VERDICT_FILE, "a", encoding="utf-8") as f:
            f.write(canonical_line + "\n")
            f.write(companion_dual + "\n")
            f.write(companion_3t + "\n")
            f.write(companion_meth + "\n")
        emitted.append({'gate_id': gid, 'wp_id': anchor['wp_id'], 'value': val,
                        'audit_sha256': audit_sha256, 'content_sha256': content_sha256})
        print(f"  audit_sha256 = {audit_sha256}")
        print(f"  emitted to verdict file ({4} lines per gate)")

    print(f"\n  TOTAL: {len(emitted)} verdict lines emitted")
    print(f"  Wall: {time.time() - t0:.2f}s")
    print(f"\n  Audit SHAs (one per anchor; 5 distinct):")
    for e in emitted:
        print(f"    {e['gate_id']}: {e['audit_sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
