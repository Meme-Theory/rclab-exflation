# -*- coding: utf-8 -*-
"""(local probe 3 — NOT a deliverable) §W6-2 post-run npz integrity inspection."""
import numpy as np
from pathlib import Path

d = np.load(Path(__file__).parent / "s100b_nonabelian_metric_fraction.npz", allow_pickle=True)

na = d["na_integrand"]
ab = d["ab_integrand"]
im = d["NA_im_tm"]
F = d["F_plaq"]
gap = d["gap12"]

print("na_integrand: min=%.6e max=%.6e mean=%.6e std=%.3e" % (na.min(), na.max(), na.mean(), na.std()))
print("  value at corner (0,50) =", na[0, 50], " at (0,49) =", na[0, 49], " at (1,50) =", na[1, 50])
print("  value at center (25,25) =", na[25, 25], " at (40,10) =", na[40, 10])
print("  interior-only (2:-2,2:-2): min=%.6e max=%.6e mean=%.6e" %
      (na[2:-2, 2:-2].min(), na[2:-2, 2:-2].max(), na[2:-2, 2:-2].mean()))
imax = np.unravel_index(na.argmax(), na.shape)
print("  argmax:", imax, " gap12 there =", gap[imax])
print()
print("ab_integrand: min=%.6e max=%.6e mean=%.6e" % (ab.min(), ab.max(), ab.mean()))
diff = ab - na
print("ab-na: min=%.3e max=%.3e mean=%.3e  (within-multiplet content)" % (diff.min(), diff.max(), diff.mean()))
print()
print("Im map: max|.|=%.3e at" % np.max(np.abs(im)), np.unravel_index(np.abs(im).argmax(), im.shape))
print()
nz = np.abs(F) > 1e-6
print("F_plaq: nonzero(>1e-6) plaquettes:", int(nz.sum()), "of", F.size)
for (i, j) in zip(*np.where(nz)):
    print("   plaq (%d,%d): F=%.6f  (tau~%.3f mu~%.3f)" % (i, j, F[i, j], 0.10 + 0.004 * (i + 0.5), -0.10 + 0.004 * (j + 0.5)))
print("sum F/(2pi) =", F.sum() / (2 * np.pi))
print()
# where does state-vs-proj deviate?
# recompute rel_dev pattern proxy: we saved only frac; reconstruct from saved fields
print("I_NA=%.12e  I_Ab=%.12e  numerator=%.6e" % (float(d["I_NA"]), float(d["I_Ab"]), float(d["numerator"])))
print("I_NA_state=%.12e I_Ab_state=%.12e" % (float(d["I_NA_state"]), float(d["I_Ab_state"])))
print("I_NA exact-1.5 deviation: %.3e" % (float(d["I_NA"]) - 1.5))
print()
# is na exactly constant?
print("na: |na - 37.5| max = %.3e" % np.max(np.abs(na - 37.5)))
print("na unique-ish sample:", na[::25, ::25])
print()
print("B2: I_NA_b2=%.9e I_Ab_b2=%.6e f=%.3e" % (float(d["I_NA_b2"]), float(d["I_Ab_b2"]), float(d["f_nonAb_b2"])))
wb2 = d["wit_b2"]; wp = d["wit_pair"]
print("wit_b2: max=%.3e mean=%.3e median=%.3e" % (wb2.max(), wb2.mean(), np.median(wb2)))
print("  argmax:", np.unravel_index(wb2.argmax(), wb2.shape))
print("wit_pair: max=%.3e mean=%.3e median=%.3e" % (wp.max(), wp.mean(), np.median(wp)))
print("  argmax:", np.unravel_index(wp.argmax(), wp.shape))
print()
ap = d["A_prot"]
print("A_prot: max=%.3e mean=%.3e median=%.3e" % (ap.max(), ap.mean(), np.median(ap)))
print("  argmax:", np.unravel_index(ap.max(axis=2).argmax(), ap.shape[:2]), " (corner region?)")
print("  A_prot at (25,25):", ap[25, 25], " at (0,50):", ap[0, 50], " at (5,45):", ap[5, 45])
print("  fraction of nodes with max_a A_prot < 1e-12:", float(np.mean(ap.max(axis=2) < 1e-12)))
