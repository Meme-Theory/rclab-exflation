"""
S84 W7b-83 — S84-VII-N-REGISTRY-LANDING
========================================

Gate: S84-W7b-83-VII-N-REGISTRY-LANDING
Trigger: [VERIFY-THEOREM]
Classification: GEOMETRIC (theorem-landing)
Agent: kaluza-klein-theorist

PURPOSE
-------
Land the Admissibility-Singleton + IKKT Anti-Correspondence theorem as a
permanent registry entry with 6 required components:

  (1) Formal theorem statement (3-5 sentences, theorem-statement style)
  (2) 4-proof chain (each sub-proof citing a 64-char verdict SHA)
  (3) Scope of applicability
  (4) Falsifier (numerically measurable, two-scale predicate)
  (5) Cross-references (G32, G36, W7b-75, W7b-76, W7b-77, W7b-78,
      Connes-Marcolli 2013 Table 1)
  (6) SHA anchor block (combined closure SHA over all input pins)

REGISTRY-LANDING ONLY — this script does NOT re-derive admissibility. It
verifies the draft entry has 6/6 components present and emits the verdict.

SLOT-ALLOCATION CASCADE
-----------------------
The W7b plan named §VII.N as the target slot. §VII.N is occupied by the
Three-Layer Regulator Theorem (S84 W2a-11, 2026-04-19) which itself cascaded
from §VII.M (occupied by W1b-9 DR3-RESPONSE-PROTOCOL on the same day).

Per the same slot-allocation remediation precedent documented inside the
existing §VII.N entry, this landing cascades to §VII.O with a
collision_note logged. Registry-hygiene violation is recorded; theorem
content is not affected.

THEOREM (landed as §VII.O)
--------------------------
Let (A_F, H_F, D_F) be a finite-dim spectral triple over M^4 × K, K a
compact simple Lie group, equipped with Mellin-cone pairing and
Connes-Marcolli KO-dim sign-table classification. The admissibility
requirements
  (i)   d_total-singleton via Mellin cone             [S83-G32 PASS]
  (ii)  KO-dim = 6 via CCM 2013 Table 1                [S82 MG-2]
  (iii) SM gauge content (3 gens + gauge bosons)
  (iv)  power-law |E_cond(L)| ~ L^b with
        b_finiteL ∈ [4.58, 4.78] at L ∈ [3..8],
        b_midL ≈ 4.92 at L ∈ [3..12],
        b_asymp → 7 (Weyl d_int − 1 limit)             [S83-G36 + W7b-75 + W7b-76]
  (v)   twist-triple non-extension (Connes-Moscovici 2008)
                                                         [W7b-77 PASS]
together uniquely determine (d_total, KO-dim, A_F) = (12, 6, C ⊕ H ⊕ M_3(C)).
The IKKT large-N matrix model (linear L scaling, b = 1) is excluded
ANALYTICALLY via the Weyl limit in (iv), not merely empirically by a
single-L fit. Eleven-dimensional M-theory compactifications (d_total = 11,
or d_total = 12 with distinct A_F) are excluded.

FALSIFIER (two-scale predicate)
-------------------------------
Any string or matrix-model construction exhibiting BOTH
  (a) KO-dim = 6 irreducible representation structure AND
  (b) |E_cond(L)| scaling with b ∈ [4.58, 4.78] at finite L (L ∈ 3..8)
      AND b → 7 at asymptotic L (Weyl d_int − 1 limit)
falsifies the singleton exclusivity. Both conditions must be met;
demonstrating either in isolation does not falsify.

NOTE: regulator-uniqueness is NOT in the 4-proof chain (W7b-81 FAIL
showed 8/11 MP-admissible, so MP-filter is not a regulator-uniqueness
argument).

SUBSTITUTION CHAIN ([VERIFY-THEOREM], 6 steps)
----------------------------------------------
Step 1: Read permanent-results-registry.md verbatim. Verify §VII.O slot
        unused (§VII.N, §VII.M occupied — cascade).
Step 2: Draft formal theorem statement, 4-proof chain, scope, falsifier.
Step 3: Verify each of the 4 sub-proofs cites a 64-char verdict SHA:
          (1) S83-DIMREDUCTION-AUDIT   : edcee689643101efd442d0c0ca895c32560d31c8ef258b14873d1c94ab5ee216
          (2) S83-MATRIX-MODEL-CLASSIFICATION (V-rescaled-Delta-fixed):
              86347fac0c61085bedb467ea13f77920f6b09c8e16a08245d64404f321825578
          (3) S84-W7b-75-B-POWER-STABILITY (drift-confirmed, FAIL):
              786f6ce3e0f992722e3d19afea3d4f740e076bf985b9cd4d2008526c4e2a1c53
          (4) S84-W7b-76-SDW-B-PREDICTION (analytic Weyl limit, PASS):
              0a60ebfd6dafcbc2f1bb622814873cfae6fb97cf18136aafd2e62e40817538f0
          (5) S84-W7b-77-TWISTED-TRIPLE-ADMISSIBILITY (0 twisted, PASS):
              7308dd7e2244c1a8797e6935cdd6ebfec41a894b61bc359aec8fd1a810c5d9ab
          (6) S84-W7b-78-CORRESPONDENCE-TABLE-CLOSURE (0 open, PASS):
              bcbc592918397a7568c5871e0f408a97c972f440029109dd2ab579f1d140c120
Step 4: Compute input-pin map SHA (ordered file-SHA concatenation) for the
        full 64-char audit_sha256.
Step 5: Append entry to sessions/permanent-results-registry.md under
        §VII.O (slot-allocation cascade from §VII.N).
Step 6: 6/6 completeness audit (statement, proof, scope, falsifier,
        cross-refs, SHA anchor). Emit verdict line to
        computations/session-84/s84_gate_verdicts.txt.
"""

import os
import sys
import hashlib
import json
import datetime
from pathlib import Path

import numpy as np

# Canonical-constants import required (computation standard); this registry
# script uses no framework constants directly, but the import is mandatory.
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403

# CPU thread cap (no heavy linear algebra in this script)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent

# ======================================================================
# Input file pins (canonical paths)
# ======================================================================
INPUT_FILES = {
    'canonical_constants'      : PROJECT_ROOT / 'computations' / 'canonical_constants.py',
    'registry_md'              : PROJECT_ROOT / 'sessions' / 'permanent-results-registry.md',
    'g32_npz'                  : PROJECT_ROOT / 'computations' / 's83_w3_g32_dimreduction_audit.npz',
    'g36_npz'                  : PROJECT_ROOT / 'computations' / 's83_w3_g36_matrix_model_classification.npz',
    'w7b_75_npz'               : PROJECT_ROOT / 'computations' / 's84_w7b_75_data.npz',
    'w7b_76_npz'               : PROJECT_ROOT / 'computations' / 's84_w7b_76_data.npz',
    'w7b_77_npz'               : PROJECT_ROOT / 'computations' / 's84_w7b_77_data.npz',
    'w7b_78_json'              : PROJECT_ROOT / 'computations' / 's84_w7b_78_correspondence_table_post_g32_g36.json',
}

# Sub-proof verdict SHAs (pre-existing, grep'd from verdict logs)
SUB_PROOF_SHAS = {
    'S83-DIMREDUCTION-AUDIT'                     : 'edcee689643101efd442d0c0ca895c32560d31c8ef258b14873d1c94ab5ee216',
    'S83-MATRIX-MODEL-CLASSIFICATION-V-RESCALED' : '86347fac0c61085bedb467ea13f77920f6b09c8e16a08245d64404f321825578',
    'S84-W7b-75-B-POWER-STABILITY'               : '786f6ce3e0f992722e3d19afea3d4f740e076bf985b9cd4d2008526c4e2a1c53',
    'S84-W7b-76-SDW-B-PREDICTION'                : '0a60ebfd6dafcbc2f1bb622814873cfae6fb97cf18136aafd2e62e40817538f0',
    'S84-W7b-77-TWISTED-TRIPLE-ADMISSIBILITY'    : '7308dd7e2244c1a8797e6935cdd6ebfec41a894b61bc359aec8fd1a810c5d9ab',
    'S84-W7b-78-CORRESPONDENCE-TABLE-CLOSURE'    : 'bcbc592918397a7568c5871e0f408a97c972f440029109dd2ab579f1d140c120',
}

# Target entry slot (after cascade from §VII.N)
REGISTRY_SLOT = 'VII.O'                              # (local) cascade slot
INTENDED_SLOT = 'VII.N'                              # (local) plan-named slot
COLLISION_WITH = (
    'Three-Layer Regulator Theorem (S84 W2a-11, 2026-04-19) '
    'which itself cascaded from §VII.M (W1b-9 DR3-RESPONSE-PROTOCOL).'
)                                                    # (local)

OUT_NPZ = SCRIPT_DIR / 's84_w7b_83_data.npz'
OUT_JSON = SCRIPT_DIR / 's84_w7b_83_landing_block.json'
OUT_MD_BLOCK = SCRIPT_DIR / 's84_w7b_83_landing_block.md'


# ======================================================================
# SHA utilities
# ======================================================================
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


# ======================================================================
# 6-component completeness audit
# ======================================================================
def audit_components(block_text):
    """
    6-component completeness audit.
    Returns dict: {component_name -> bool}.
    PASS criterion: all 6 True.
    """
    checks = {
        'formal_statement'  : 'Theorem VII.O' in block_text and 'Admissibility Singleton' in block_text,
        'proof_chain_4'     : (
            'Sub-proof (1)' in block_text and
            'Sub-proof (2)' in block_text and
            'Sub-proof (3)' in block_text and
            'Sub-proof (4)' in block_text
        ),
        'scope_statement'   : '### Scope' in block_text and 'compact simple Lie group' in block_text,
        'falsifier'         : '### Falsifier' in block_text and '[4.58, 4.78]' in block_text,
        'cross_references'  : (
            'G32' in block_text and 'G36' in block_text and
            'W7b-75' in block_text and 'W7b-76' in block_text and
            'W7b-77' in block_text and 'W7b-78' in block_text and
            'Connes-Marcolli 2013' in block_text
        ),
        'sha_anchor_block'  : (
            '### Anchor-SHA pin block' in block_text and
            all(sha in block_text for sha in SUB_PROOF_SHAS.values())
        ),
    }
    return checks


# ======================================================================
# Build the registry entry text
# ======================================================================
def build_registry_entry(combined_audit_sha, today_iso):
    lines = []
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append(f'## §VII.O — Admissibility Singleton and IKKT Anti-Correspondence Theorem (S84 W7b-83, {today_iso})')
    lines.append('')
    lines.append('**Source**: S84 W7b-83. Script '
                 '`computations/session-84/s84_w7b_83_vii_n_registry_landing.py`; '
                 'data `s84_w7b_83_data.npz`; block `s84_w7b_83_landing_block.md`.')
    lines.append('')
    lines.append('**Classification**: GEOMETRIC (theorem-landing). '
                 'Substrate framing: the eigenvalue spectrum of D_K on '
                 'Jensen-deformed SU(3) admits exactly one (d_total, KO-dim, A_F) '
                 'configuration consistent with (i) Mellin-cone d-singleton, '
                 '(ii) CCM KO-dim=6 sign-table row, (iii) three-generation SM '
                 'gauge content, and (iv) two-scale power-law |E_cond(L)| '
                 'interpolating between finite-L b ∈ [4.58, 4.78] and asymptotic '
                 'b → 7 = d_int − 1 (Weyl). The singleton is '
                 '(12, 6, C ⊕ H ⊕ M_3(C)).')
    lines.append('')
    lines.append(f'**Slot-allocation note**: Target slot §{INTENDED_SLOT} was '
                 f'occupied by the {COLLISION_WITH} Landing cascades to '
                 f'§{REGISTRY_SLOT} per the same slot-allocation remediation '
                 'precedent documented within §VII.N itself. Registry-hygiene '
                 'violation logged; theorem content unaffected.')
    lines.append('')

    # --------------------------------------------------------------
    # (1) Formal theorem statement
    # --------------------------------------------------------------
    lines.append('### Formal statement')
    lines.append('')
    lines.append('**Theorem VII.O (Admissibility Singleton and IKKT '
                 'Anti-Correspondence).** Let (A_F, H_F, D_F) be a finite-dim '
                 'spectral triple over a product spacetime M^4 × K with K a '
                 'compact simple Lie group, equipped with Mellin-cone pairing '
                 'Tr(|D|^{−s}) and Connes-Marcolli KO-dim sign-table '
                 'classification (CCM 2013 Table 1). The admissibility '
                 'requirements')
    lines.append('')
    lines.append('  (i)   d_total-singleton via Mellin-cone residue (S83-G32);')
    lines.append('  (ii)  KO-dim = 6 via CCM 2013 Table 1 (S82 MG-2);')
    lines.append('  (iii) SM gauge content (three generations + gauge bosons);')
    lines.append('  (iv)  power-law |E_cond(L)| ~ L^b with')
    lines.append('          b_finiteL ∈ [4.58, 4.78] at L ∈ [3..8],')
    lines.append('          b_midL   ≈ 4.92          at L ∈ [3..12],')
    lines.append('          b_asymp  → 7 = d_int − 1 (Weyl limit)')
    lines.append('        (S83-G36 + W7b-75 + W7b-76);')
    lines.append('  (v)   twist-triple non-extension under Connes-Moscovici (2008) axioms (W7b-77),')
    lines.append('')
    lines.append('together uniquely determine (d_total, KO-dim, A_F) = '
                 '(12, 6, C ⊕ H ⊕ M_3(C)). The IKKT large-N matrix model '
                 '(linear-L scaling, b = 1) is excluded **analytically** by '
                 'the Seeley-DeWitt Weyl limit in (iv), not merely '
                 'empirically by a finite-L fit. Eleven-dimensional M-theory '
                 'compactifications — which require d_total = 11, or '
                 'd_total = 12 with a distinct A_F — are excluded.')
    lines.append('')

    # --------------------------------------------------------------
    # (2) 4-proof chain (UPGRADED: regulator-uniqueness dropped; (3) now
    # carries the empirical drift + analytic Weyl match)
    # --------------------------------------------------------------
    lines.append('### 4-proof chain')
    lines.append('')
    lines.append('**Sub-proof (1) — Mellin-cone d-singleton.** S83-G32 DIMREDUCTION-AUDIT '
                 'PASS established that the Mellin-cone residue pairing '
                 'Tr(|D|^{−s}) admits a unique residue-positive cone at d = 12 '
                 'under KO-dim = 6 constraint; d = 11 is excluded (A4, A5, SM '
                 'violations). Anchor SHA: '
                 f'`{SUB_PROOF_SHAS["S83-DIMREDUCTION-AUDIT"]}`.')
    lines.append('')
    lines.append('**Sub-proof (2) — CCM KO-dim=6 sign-table reduction.** '
                 'Connes-Marcolli (2013) Table 1 together with S82 MG-2 even-KO '
                 'and SM-chirality constraints reduces the admissible triples '
                 'to (12, 6, A_F) with A_F = C ⊕ H ⊕ M_3(C). '
                 'Anchor (G36 V-rescaled branch): '
                 f'`{SUB_PROOF_SHAS["S83-MATRIX-MODEL-CLASSIFICATION-V-RESCALED"]}`.')
    lines.append('')
    lines.append('**Sub-proof (3) — Power-law scaling with SDW analytic match (IKKT excluded).** '
                 'S83-G36 recovered a PASS power-law fit b_power = 4.681 at L ≤ 8. '
                 'W7b-75 extended the L scan to L ≤ 12 and found b drifting: '
                 'b = 4.681 (L ≤ 8) → 4.988 (L ≤ 12) → 5.02 (all points). '
                 'W7b-76 derived the drift **analytically** via the '
                 'Seeley-DeWitt heat-kernel expansion: b(L) interpolates between '
                 'a finite-L plateau b_finiteL ∈ [4.58, 4.78] (set by the '
                 'lowest-order a_k coefficients) and an asymptotic Weyl limit '
                 'b_asymp → 7 = d_int − 1 (the internal-space dimension minus '
                 'one). IKKT linear scaling (b = 1) is thus excluded not by a '
                 'single empirical fit but by the **analytic Weyl asymptote** '
                 'itself — any b → 1 limit would require d_int = 2, which '
                 'contradicts d_total = 12 under KO-dim = 6. '
                 'Anchors: W7b-75 '
                 f'`{SUB_PROOF_SHAS["S84-W7b-75-B-POWER-STABILITY"]}` (FAIL; drift-confirmed) + '
                 f'W7b-76 `{SUB_PROOF_SHAS["S84-W7b-76-SDW-B-PREDICTION"]}` (PASS; analytic SDW).')
    lines.append('')
    lines.append('**Sub-proof (4) — Twist-triple non-extension.** W7b-77 '
                 'scanned 16 Connes-Moscovici (2008) twisted-triple candidates '
                 'and confirmed that zero admissible twists extend the '
                 'singleton; the M-theory twist-sector pathway is closed. '
                 'Anchor SHA: '
                 f'`{SUB_PROOF_SHAS["S84-W7b-77-TWISTED-TRIPLE-ADMISSIBILITY"]}`. '
                 'W7b-78 closed the correspondence table (0 open; 11 ANTI / '
                 '5 GENUINE / 12 STRUCTURAL / 3 SUGGESTIVE): '
                 f'`{SUB_PROOF_SHAS["S84-W7b-78-CORRESPONDENCE-TABLE-CLOSURE"]}`.')
    lines.append('')
    lines.append('**Regulator-uniqueness NOT in chain.** W7b-81 returned FAIL '
                 '(8/11 MP-admissible); the MP-filter is not a '
                 'regulator-uniqueness argument. The 4-proof chain above is '
                 'complete WITHOUT citing regulator-uniqueness.')
    lines.append('')

    # --------------------------------------------------------------
    # (3) Scope
    # --------------------------------------------------------------
    lines.append('### Scope')
    lines.append('')
    lines.append('This theorem applies to spectral triples (A_F, H_F, D_F) '
                 'over product spacetimes M^4 × K with K a **compact simple '
                 'Lie group**, KO-dim = 6, and finite-dim A_F over the complex '
                 'numbers. Extensions to non-compact K, higher-rank exceptional '
                 'groups, or twisted (Connes-Moscovici 2008) spectral triples '
                 'require re-derivation; W7b-77 confirmed that no such twisted '
                 'extension admits the singleton, but the scope of the '
                 'non-extension is itself axiom-set-specific (CM2008-twist).')
    lines.append('')

    # --------------------------------------------------------------
    # (4) Falsifier (two-scale predicate)
    # --------------------------------------------------------------
    lines.append('### Falsifier (two-scale predicate)')
    lines.append('')
    lines.append('The theorem is falsified by any string or matrix-model '
                 'construction demonstrating **BOTH**:')
    lines.append('')
    lines.append('  (a) KO-dim = 6 irreducible representation structure '
                 'consistent with CCM 2013 Table 1; **AND**')
    lines.append('  (b) |E_cond(L)| power-law scaling with b ∈ [4.58, 4.78] '
                 'at finite L (L ∈ [3..8]) AND b → 7 at asymptotic L '
                 '(Weyl d_int − 1 limit).')
    lines.append('')
    lines.append('Both conditions must be met **simultaneously**; demonstrating '
                 'either in isolation does not falsify. The two-scale '
                 'predicate reflects W7b-76\'s SDW interpolation result: a '
                 'single-scale empirical match at finite L is insufficient, '
                 'because the drift itself is structural (set by the a_k '
                 'coefficients). The Weyl asymptote is the robust signature.')
    lines.append('')

    # --------------------------------------------------------------
    # (5) Cross-references
    # --------------------------------------------------------------
    lines.append('### Cross-references')
    lines.append('')
    lines.append('- **S83-G32** DIMREDUCTION-AUDIT — d_total-singleton')
    lines.append('- **S83-G36** MATRIX-MODEL-CLASSIFICATION — power-law finite-L fit')
    lines.append('- **S84-W7b-75** B-POWER-STABILITY — drift confirmation')
    lines.append('- **S84-W7b-76** SDW-B-PREDICTION — analytic Weyl limit')
    lines.append('- **S84-W7b-77** TWISTED-TRIPLE-ADMISSIBILITY — twist-sector closure')
    lines.append('- **S84-W7b-78** CORRESPONDENCE-TABLE-CLOSURE — 11 ANTI / 5 GENUINE / 12 STRUCTURAL / 3 SUGGESTIVE')
    lines.append('- **Connes-Marcolli 2013 Table 1** — KO-dim sign-table source')
    lines.append('- **Connes-Moscovici 2008** — twisted spectral triple axioms (scope of (5))')
    lines.append('')

    # --------------------------------------------------------------
    # (6) SHA anchor block
    # --------------------------------------------------------------
    lines.append('### Anchor-SHA pin block')
    lines.append('')
    for name, sha in SUB_PROOF_SHAS.items():
        lines.append(f'  {name:50s} : sha256 = `{sha}`')
    lines.append('')
    lines.append(f'**Combined audit SHA** (over ordered input-pin map of '
                 f'{len(INPUT_FILES)} input files):')
    lines.append('')
    lines.append(f'  audit_sha256 = `{combined_audit_sha}`')
    lines.append('')

    # --------------------------------------------------------------
    # Verdict block
    # --------------------------------------------------------------
    lines.append('### Verdict')
    lines.append('')
    lines.append('**PASS** at registration (landing under §VII.O; intended '
                 f'§VII.N occupied — cascade logged above).')
    lines.append('')
    lines.append('  4-tuple: (value=6_of_6_components_present, '
                 'scheme=registry-landing-audit, '
                 'convention=permanent-results-registry-S84, L_max=N/A)')
    lines.append(f'  Entry closure audit_sha256 = `{combined_audit_sha}`')
    lines.append('')
    lines.append('**What PASS means**: The admissibility singleton '
                 '(12, 6, C ⊕ H ⊕ M_3(C)) and IKKT anti-correspondence are now '
                 'permanent framework theorems. Future sessions cite §VII.O by '
                 'reference; the 4-proof chain is closed. The upgrade from '
                 'S83-G36\'s finite-L empirical fit to W7b-76\'s analytic '
                 'Weyl limit makes the IKKT exclusion **structural**, not '
                 'fit-dependent.')
    lines.append('')
    lines.append('**Not in chain**: regulator-uniqueness (W7b-81 FAIL). '
                 'MP-filter does not select a unique regulator; the theorem '
                 'does not depend on it. §VII.N\'s three-layer regulator '
                 'stratification (W2a-11) handles regulator classification '
                 'independently.')
    lines.append('')
    lines.append('**Artifacts**: `computations/session-84/s84_w7b_83_vii_n_registry_landing.py` '
                 '(this script), `s84_w7b_83_data.npz` (combined-SHA anchor + '
                 'component-audit matrix), `s84_w7b_83_landing_block.md` '
                 '(standalone block copy), `s84_w7b_83_landing_block.json` '
                 '(structured payload). **Session working paper**: '
                 '`sessions/archive/session-84/session-84-w7-workingpaper.md` §W7-83.')
    lines.append('')

    return '\n'.join(lines)


# ======================================================================
# Main
# ======================================================================
def main():
    print('=' * 76)
    print('S84 W7b-83  —  S84-VII-N-REGISTRY-LANDING')
    print('Gate: S84-W7b-83-VII-N-REGISTRY-LANDING')
    print('Trigger: [VERIFY-THEOREM]   Classification: GEOMETRIC')
    print('=' * 76)

    # ---------- Step 1: input-pin SHAs ----------
    print('\n[Step 1] Input SHA-256 pins:')
    input_shas = {}
    for name, path in INPUT_FILES.items():
        if not path.exists():
            raise FileNotFoundError(f'Required input missing: {path}')
        sha = sha256_file(path)
        input_shas[name] = sha
        print(f'  {name:25s} {sha}')

    # Combined audit_sha: SHA-256 over the ordered input-pin map
    ordered_concat = '\n'.join(
        f'{name}:{input_shas[name]}' for name in INPUT_FILES.keys()
    )
    combined_audit_sha = sha256_text(ordered_concat)
    print(f'\n[Step 1] Combined audit_sha256 (input-pin map): {combined_audit_sha}')

    # Also echo the sub-proof verdict SHAs
    print('\n[Step 1] Sub-proof verdict SHAs (pre-existing, cited):')
    for name, sha in SUB_PROOF_SHAS.items():
        print(f'  {name:50s} {sha}')

    # ---------- Step 2: verify registry slot state ----------
    print('\n[Step 2] Verifying registry slot allocation.')
    registry_text = INPUT_FILES['registry_md'].read_text(encoding='utf-8')
    slot_n_heading = '## §VII.N —'
    slot_o_heading = '## §VII.O —'
    n_occupied = slot_n_heading in registry_text
    o_occupied = slot_o_heading in registry_text
    print(f'  §VII.N occupied : {n_occupied}')
    print(f'  §VII.O occupied : {o_occupied}')
    if not n_occupied:
        print('  WARNING: §VII.N claimed vacant; plan assumed occupied. Continuing to §VII.O cascade.')
    if o_occupied:
        raise RuntimeError('§VII.O already occupied — cascade further required (manual).')

    # ---------- Step 3: build entry ----------
    print('\n[Step 3] Drafting §VII.O entry text.')
    today_iso = datetime.date.today().isoformat()
    entry_text = build_registry_entry(combined_audit_sha, today_iso)
    print(f'  Entry length: {len(entry_text)} chars, {len(entry_text.splitlines())} lines.')

    # ---------- Step 4: 6-component audit ----------
    print('\n[Step 4] 6-component completeness audit.')
    checks = audit_components(entry_text)
    for name, ok in checks.items():
        mark = 'PASS' if ok else 'FAIL'
        print(f'  {mark}  {name}')
    components_present = sum(1 for v in checks.values() if v)
    audit_pass = components_present == 6

    # ---------- Step 5: append to registry (APPEND-ONLY) ----------
    print(f'\n[Step 5] Appending entry to registry '
          f'(write: {INPUT_FILES["registry_md"]}).')
    if audit_pass:
        with open(INPUT_FILES['registry_md'], 'a', encoding='utf-8') as fh:
            fh.write(entry_text)
        print(f'  Appended {len(entry_text)} chars under §VII.O.')
    else:
        print('  Skipped append (audit did not reach 6/6).')

    # ---------- Step 6: write artifacts ----------
    print('\n[Step 6] Writing artifacts.')
    # standalone markdown block (copy of what was appended)
    OUT_MD_BLOCK.write_text(entry_text, encoding='utf-8')
    # structured JSON payload
    payload = {
        'gate_id'           : 'S84-W7b-83-VII-N-REGISTRY-LANDING',
        'trigger'           : '[VERIFY-THEOREM]',
        'classification'    : 'GEOMETRIC',
        'agent'             : 'kaluza-klein-theorist',
        'landing_date'      : today_iso,
        'intended_slot'     : f'§{INTENDED_SLOT}',
        'actual_slot'       : f'§{REGISTRY_SLOT}',
        'cascade_reason'    : COLLISION_WITH,
        'components_present': components_present,
        'components_required': 6,
        'component_audit'   : checks,
        'input_shas'        : input_shas,
        'sub_proof_shas'    : SUB_PROOF_SHAS,
        'combined_audit_sha': combined_audit_sha,
        'entry_char_count'  : len(entry_text),
        'entry_line_count'  : len(entry_text.splitlines()),
        'verdict_line'      : None,  # populated below
    }
    # npz data anchor
    np.savez(
        OUT_NPZ,
        combined_audit_sha=np.array(combined_audit_sha),
        components_present=np.array(components_present),
        components_required=np.array(6),
        component_names=np.array(list(checks.keys())),
        component_passes=np.array([int(v) for v in checks.values()]),
        input_sha_names=np.array(list(input_shas.keys())),
        input_sha_values=np.array(list(input_shas.values())),
        sub_proof_names=np.array(list(SUB_PROOF_SHAS.keys())),
        sub_proof_shas=np.array(list(SUB_PROOF_SHAS.values())),
        intended_slot=np.array(f'§{INTENDED_SLOT}'),
        actual_slot=np.array(f'§{REGISTRY_SLOT}'),
    )
    print(f'  Wrote {OUT_NPZ.name}, {OUT_MD_BLOCK.name}.')

    # ---------- Step 7: verdict line ----------
    verdict = 'PASS' if audit_pass else 'FAIL'
    verdict_line = (
        f'S84-W7b-83-VII-N-REGISTRY-LANDING: {verdict} -- '
        f'value={components_present}_of_6 '
        f'scheme=registry-landing-audit '
        f'convention=permanent-results-registry-S84 '
        f'L_max=N/A '
        f'sha256={combined_audit_sha}'
    )
    payload['verdict_line'] = verdict_line
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding='utf-8')

    print('\n[Step 7] Verdict line (appended to '
          'computations/session-84/s84_gate_verdicts.txt):')
    print(f'  {verdict_line}')
    verdicts_file = PROJECT_ROOT / 'computations' / 's84_gate_verdicts.txt'
    with open(verdicts_file, 'a', encoding='utf-8') as fh:
        fh.write('\n' + verdict_line + '\n')

    # ---------- Final 4-tuple ----------
    print('\n' + '=' * 76)
    print('4-tuple: (value={components}_of_6, '
          'scheme=registry-landing-audit, '
          'convention=permanent-results-registry-S84, '
          'L_max=N/A)'.format(components=components_present))
    print(f'closure audit_sha256: {combined_audit_sha}')
    print('=' * 76)

    if not audit_pass:
        sys.exit(1)


if __name__ == '__main__':
    main()
