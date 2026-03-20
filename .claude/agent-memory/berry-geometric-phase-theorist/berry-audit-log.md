# Berry Paper Audit Log (2026-02-21)

## Fixed Issues (16 total across 10 files)

### Paper 01 (Berry Phase)
- **Concept**: Statement "Berry phase is gauge-dependent" was wrong for closed loops. Fixed to: gauge-invariant mod 2pi, continuous values in general, quantized to pi only at diabolical points.

### Paper 03 (Diabolical Points)
- **Title**: "Three-Terminal Quantum Dots" -> "Triangles" (Berry & Wilkinson studied quantum billiards in triangles)
- **Math**: Nonsensical self-referential energy gap formula replaced with correct two-level avoided crossing formula.

### Paper 06 (Maslov Index)
- **Author**: Added K.E. Mount as co-author (Berry & Mount, not Berry alone)
- **Journal**: J. Phys. A Vol. 5 pp. 341-343 -> Rep. Prog. Phys. Vol. 35 pp. 315-397

### Paper 07 (Optical Vortices)
- **Journal**: J. Opt. A Vol. 15 pp. 207-210 -> Proc. SPIE 3487 pp. 1-5 (1998 conference proceedings)
- **Math**: Removed garbled inline self-correction ("Wait, that's not quite right...") and incorrect Berry phase formula (m^2 pi). Replaced with correct winding phase 2pi*m.

### Paper 08 (Pancharatnam)
- **Journal**: Nature Vol. 326 pp. 277-278 -> J. Mod. Optics Vol. 34 pp. 1401-1407

### Paper 09 (Catastrophe Optics)
- **Author**: Added C. Upstill as co-author (Berry & Upstill, not Berry alone)

### Paper 10 (BGS Conjecture)
- **Journal**: Berry's analysis was listed as PRL 56 pp. 2256-2259 -> Proc. R. Soc. A Vol. 400 pp. 229-251
- **Math**: Form factor K(k) was incorrectly labeled GOE when it was actually GUE formula. Added correct GOE form factor.

### Paper 11 (QHE/Chern)
- **Source**: Fabricated citation Phys. Rev. B Vol. 31 pp. 3794-3805 (no such Berry paper). Replaced with composite attribution: Berry (Proc. R. Soc. A 392), TKNN (PRL 49), Xiao/Chang/Niu (Rev. Mod. Phys. 82).
- **Math**: Anomalous velocity sign error (missing minus sign). Semiclassical EOM had wrong prefactor structure.

### Paper 12 (Trace Formula)
- **Author**: K.E. Keating -> J.P. Keating (Jonathan P. Keating)
- **Pages**: 4839-4866 -> 4839-4849

### Paper 13 (Beam Shift)
- **Math**: Abstract GH shift formula sign inconsistency with derivation section. Harmonized to positive sign convention.

### Paper 14 (Synthesis)
- **Source**: Fabricated citation Rev. Mod. Phys. Vol. 81 pp. 1441-1451 (2009). No such paper exists. Replaced with composite attribution noting multiple Berry publications (1988-2010).

### INDEX.md
- Paper 03 title corrected
- Paper 06 journal corrected
- Paper 11 attribution corrected
- Paper 14 year/source corrected
- BGS-3 form factor equation corrected (GUE label, GOE formula added)
- QH-2 anomalous velocity sign corrected (three locations)

## Unfixable / Needs Further Verification
- Paper 05 (AB Scattering): Berry & Gover, J. Phys. A 22, 4697-4704 (1989) -- could not confirm or deny. Plausible but unverified.
- Paper 12 title: File uses descriptive title "Semiclassical Trace Formula and Scattering Resonances" but actual Berry-Keating 1990 paper title is "A rule for quantizing chaos?"
- Paper 13: Berry & Balazs, J. Mod. Opt. 37, 845-860 (1990) -- could not confirm exact citation.
