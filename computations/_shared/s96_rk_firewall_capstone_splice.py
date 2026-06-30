#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
Atomic SECTION-SCOPED splice of the R_K(0) normalization firewall subsection into
the curated capstone `sessions/framework/phonic-exflation-equation.md` Section 8,
mirroring the Section 8.2 a_n firewall structure.

Discipline (CLAUDE.md curated-doc, concurrent contention):
  read whole file -> splice ONLY the Section 8 region (insert §8.2a between the
  §8.2 closing paragraph and `### 8.3`) -> write to a temp file -> fsync ->
  os.replace (atomic). EVERY other byte preserved. NEVER bulk-append. Idempotent:
  if the §8.2a anchor is already present, no-op.
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

_SHARED = Path(__file__).resolve().parent  # (local)
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

# Load-bearing cross-validation: the spliced §8.2a R₁ value MUST equal the
# canonical zeta-triple ratio a₀a₄/a₂² to the published 7 sig figs before we
# write it into the curated capstone.
from canonical_constants import a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta  # noqa: E402

_R1_DOC = 1.128655  # (local)  value spliced into the §8.2a table
_R1_CANON = a_0_FW_zeta * a_4_FW_zeta / a_2_FW_zeta ** 2  # (local)
assert abs(_R1_CANON - _R1_DOC) < 1e-5, (
    f"§8.2a R₁ doc value {_R1_DOC} != canonical a₀a₄/a₂²={_R1_CANON}")

ROOT = _SHARED.parent.parent  # (local)
CAPSTONE = ROOT / "sessions" / "framework" / "phonic-exflation-equation.md"

# Unique anchor: the LAST line of §8.2 (verbatim tail) + the §8.3 header.
ANCHOR_TAIL = 'never "`a₀ > a₂ > a₄`" without the `Λ`-power qualifier.'  # (local)
SECTION_83_HEADER = "### 8.3 Derived scales"  # (local)
IDEMPOTENT_MARKER = "### 8.2a The `R_K(0)` normalization firewall"  # (local)

# The R_K(0) firewall subsection (mirror of §8.2: 3-form table + conversion factors
# + role + convention-direction paragraph + Sage convention-invariance certification).
INSERT_BLOCK = """### 8.2a The `R_K(0)` normalization firewall (the curvature analog of §8.2)

`R_K(0)` — the SU(3)-fiber scalar curvature at genesis — circulates in **three different normalizations**; like the `a_n` triples of §8.2 they are the **same substrate curvature under three scale conventions**, not three rival curvatures (S96-HYG-RK-FIREWALL, baptista V.1):

| `R_K(0)` form | value | conversion to internal | role / source |
|:--|:--|:--|:--|
| internal E3 (**canonical**) | **2** | `×1` (reference) | `R_K(τ) = −¼e⁻⁴ᵗ + 2e⁻ᵗ − ¼ + ½e²ᵗ`; the rational-coefficient internal curvature (`baptista-operator-dk-tau.md`) |
| 12D-reduction (s52) | **4** | `×2` | bi-invariant lift `= 12/α = 12/3`; the 10/12D Kaluza–Klein normalization (`s52_12d_reduction_output.txt`) |
| Baptista Paper-15 eq 3.70 | **1.5** | `×4/3` (internal/P15) | `R_K(τ) = 3/2(2e²ᵗ − 1 + 8(e⁻ᵗ − e⁻⁴ᵗ))`; the Killing-form rational normalization |

The two conversion factors are exact rationals: `R_K^{12D}/R_K^{internal} = 4/2 = ×2` and `R_K^{internal}/R_K^{P15} = 2/1.5 = ×4/3`. **Display the internal E3 form `R_K(0)=2` as *the* `R_K` of the equation** (it is the form entering the E3 closed-form trajectory `R_K(0.19)=2.018` of the Verification ledger); the 12D and Paper-15 forms are the same curvature rescaled, quoted only with their explicit `×2` / `×4/3` tag.

**Why no downstream observable inherits a convention artifact** (Sage-certified to machine-ε; the curvature analog of "only *ratios* survive truncation"). Under any overall rescale `R_K → c·R_K` with `c ∈ {2, 4/3}`-conversion:

- **The FI ratio `R₁ = a₀a₄/a₂² = 1.128655` is invariant.** With `a₀ ∝ V` (degree 0 in `R_K`), `a₂ ∝ R_K·V → c·a₂`, `a₄ ∝ R_K²·V → c²·a₄`, the rescaled ratio is `R₁′ = (a₀)(c²a₄)/(c·a₂)² = a₀a₄/a₂² = R₁` — the `c²` cancels exactly (residual `0`). `R₁` is a topological/representation-theoretic ratio-observable; it lives on the surviving side of the geometry-vs-topology spine (§9).
- **The Wronskian's τ=0 sixth-order zero is invariant in *order*; only its *magnitude* rescales.** `W ∝ R_K′(τ)³` with `R_K′(τ) = e⁻⁴ᵗ(e³ᵗ−1)²` (a second-order zero at τ=0), so `W = e⁻¹²ᵗ(e³ᵗ−1)⁶` has leading Taylor term `729 τ⁶` — a **sixth-order** zero. Under `R_K → c·R_K`: `W → (c·R_K′)³ = c³·W`, leading term `729 c³ τ⁶`. The coefficient picks up `c³` (an overall magnitude rescale; the c³ leading-coefficient ratio is exact at every τ) but the **leading power τ⁶ is unchanged** — the genesis-only spectral-moment degeneracy (the layers algebraically independent everywhere except τ=0) is a convention-invariant structural fact, not a normalization artifact.
- **The Lichnerowicz spectral-gap statement `λ² ≥ R_K/4 > 0` is sign-invariant.** A positive rescale `c > 0` scales `R_K/4` by the same `c` on both sides, preserving `R_K/4 > 0` (`= 0.5, 1.0, 0.375` under the three forms) — the gap stays open under every normalization.

The firewall's one-line rule: **`R_K(0)` rescalings move magnitudes (`R_K` itself, and `W` by `c³`), never the dimensionless invariants (`R₁`, the W τ=0 zero-*order*) or the gap-sign.** Which `c` is canonical is a laboratory bookkeeping choice (internal E3 for the equation; 12D for the Kaluza–Klein lift; Paper-15 for the Killing-form presentation); the substrate physics is identical across all three.

"""  # (local)


def main() -> int:
    text = CAPSTONE.read_text(encoding="utf-8")  # (local)
    n_before = len(text.encode("utf-8"))         # (local)

    if IDEMPOTENT_MARKER in text:
        print(f"IDEMPOTENT: §8.2a R_K firewall already present in capstone; no-op. "
              f"(bytes={n_before})")
        return 0

    # Locate the unique splice anchor: the §8.2 closing-paragraph tail, then the
    # §8.3 header that follows it. Insert the block BETWEEN them.
    if ANCHOR_TAIL not in text:
        print(f"ERROR: §8.2 closing-paragraph anchor not found; refusing to splice "
              f"(capstone structure changed).", file=sys.stderr)
        return 2
    if SECTION_83_HEADER not in text:
        print(f"ERROR: '### 8.3 Derived scales' header not found; refusing to splice.",
              file=sys.stderr)
        return 2

    # The §8.3 header occurrence AFTER the §8.2 tail is the insertion point.
    tail_idx = text.index(ANCHOR_TAIL)                       # (local)
    h83_idx = text.index(SECTION_83_HEADER, tail_idx)        # (local)

    # Splice: everything up to (and including) the blank line(s) before §8.3, then
    # the INSERT_BLOCK, then §8.3 onward. Preserve the existing inter-section spacing
    # exactly: the region [end-of-§8.2-tail-line ... start-of-§8.3] is "\n\n".
    head = text[:h83_idx]    # (local)  ends with the §8.2 paragraph + its trailing "\n\n"
    tail = text[h83_idx:]    # (local)  starts at "### 8.3 Derived scales"
    new_text = head + INSERT_BLOCK + tail  # (local)

    # ---- atomic write: temp file in the same dir -> fsync -> os.replace ----
    n_after = len(new_text.encode("utf-8"))  # (local)
    fd, tmp_path = tempfile.mkstemp(dir=str(CAPSTONE.parent),
                                    prefix=".s96_rk_firewall_", suffix=".tmp")  # (local)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fp:
            fp.write(new_text)
            fp.flush()
            os.fsync(fp.fileno())
        os.replace(tmp_path, CAPSTONE)  # atomic on the same filesystem
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

    # ---- verify: re-read, confirm marker present + byte-delta == inserted block ----
    verify = CAPSTONE.read_text(encoding="utf-8")  # (local)
    ok_marker = IDEMPOTENT_MARKER in verify          # (local)
    # Every pre-existing section header must survive.
    survivors = all(h in verify for h in (
        "### 8.1 Dimensional closure",
        "### 8.2 The `a_n` convention table (the firewall against the one fatal conflation)",
        "### 8.3 Derived scales",
        "### 8.4 The \"1 → 60\" collapse",
        "### 8.5 What this does NOT certify — the genuine residual risk",
        "## §9 — The one equation, and what remains open",
    ))  # (local)
    block_bytes = len(INSERT_BLOCK.encode("utf-8"))  # (local)
    delta = len(verify.encode("utf-8")) - n_before    # (local)
    print(f"SPLICE OK: marker_present={ok_marker} all_section_headers_survive={survivors}")
    print(f"  bytes_before={n_before} bytes_after={len(verify.encode('utf-8'))} "
          f"delta={delta} inserted_block_bytes={block_bytes} "
          f"delta==block_bytes={delta == block_bytes}")
    if not (ok_marker and survivors and delta == block_bytes):
        print("ERROR: post-splice verification FAILED.", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
