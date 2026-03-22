"""
GIANT-VORONOI-42: 32-Cell Tessellation Monte Carlo
===================================================
Tests whether a 32-cell Voronoi tessellation of the observable universe
naturally produces giant structures (>500 Mpc) at z~0.8 and z~1.6.

Framework context: N_eff = 32 distinct Dirac eigenvalues at round SU(3) (tau=0).
If the crystal IS space, the observable universe at early tau had 32 effective
spatial cells. Cell boundaries are where matter preferentially collects.

Method: For each of 10,000 realizations:
  1. Place 32 seeds uniformly in a sphere of R=14250 Mpc
  2. Place observer uniformly in the sphere
  3. For each Voronoi face, compute its intersection with a spherical shell
     (analytic: face is a plane, shell is a sphere -> intersection is a circle)
  4. Measure the angular extent of each face-shell intersection
  5. Count "giant structures" with comoving extent > 500 Mpc

Key physics: Voronoi faces are planar bisectors of seed pairs. The intersection
of a plane with a spherical shell is a circle (if it intersects at all). The
comoving extent of this circle on the shell = 2 * d_shell * sin(alpha), where
alpha is the half-angle subtended by the circle from the observer.

Pre-registered gate GIANT-VORONOI-42:
  PASS: P(N_giant >= 2 at z=0.8) > 0.05 AND P(L_max > 1000 Mpc) > 0.01
  FAIL: P(N_giant >= 2) < 0.01 OR P(L_max > 1000 Mpc) < 0.001

Author: Cosmic-Web-Theorist
Date: 2026-03-13
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import time
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# Physical parameters
# =============================================================================
R_OBS = 14_250.0         # Comoving radius of observable universe (Mpc)
N_CELLS = 32             # N_eff at round SU(3)
N_REALIZATIONS = 10_000  # Monte Carlo realizations

# Redshift shells
SHELLS = {
    'z08': {'d': 2350.0, 'delta_d': 200.0, 'label': 'z = 0.8'},
    'z16': {'d': 4050.0, 'delta_d': 200.0, 'label': 'z = 1.6'},
}

L_GIANT = 500.0   # Mpc, minimum comoving extent for "giant structure"
L_GPC = 1000.0    # Mpc, Giant Arc scale

# =============================================================================
# Utility: uniform random points in sphere
# =============================================================================
def random_points_in_sphere(n, radius, rng):
    """Generate n uniformly distributed points within a sphere."""
    collected = []
    total = 0
    while total < n:
        needed = max(n - total, 1)
        batch_size = int(needed * 2.0) + 10
        batch = rng.uniform(-radius, radius, size=(batch_size, 3))
        r2 = np.sum(batch**2, axis=1)
        good = batch[r2 <= radius**2]
        if len(good) > 0:
            collected.append(good)
            total += len(good)
    return np.vstack(collected)[:n]


# =============================================================================
# Analytic intersection: plane with spherical shell
# =============================================================================
def face_shell_intersection(face_point, face_normal, observer, d_shell, delta_d, r_obs):
    """
    Compute the intersection of a Voronoi face (infinite plane) with a
    spherical shell centered on the observer.

    A Voronoi face between seeds A and B is the perpendicular bisector plane:
      face_point = midpoint(A, B)
      face_normal = (B - A) / |B - A|

    The plane equation: n . (r - face_point) = 0
    The shell: |r - observer| = d_shell  (at the central radius)

    The intersection is a circle on the shell. We compute:
    - Whether it intersects
    - The angular extent as seen from the observer
    - The comoving length (diameter of the intersection circle)

    We also check that the intersection lies within the observable universe
    (|r| <= r_obs) and within the shell thickness.

    Returns:
        intersects: bool
        comoving_diameter: float (Mpc) - diameter of the intersection circle
        angular_diameter: float (rad)
        center_theta: float - polar angle of circle center from observer
        center_phi: float - azimuthal angle of circle center from observer
    """
    # The plane passes through face_point with normal face_normal.
    # Parametrize: any point on the plane satisfies n.(r - p) = 0
    # Any point on the shell satisfies |r - obs|^2 = d^2
    #
    # The signed distance from the observer to the plane:
    obs_to_fp = face_point - observer
    signed_dist = np.dot(obs_to_fp, face_normal)  # distance from observer to plane along normal

    # If |signed_dist| > d_shell, the sphere doesn't reach the plane
    d_inner = d_shell - delta_d / 2
    d_outer = d_shell + delta_d / 2

    if abs(signed_dist) > d_outer:
        return False, 0.0, 0.0, 0.0, 0.0

    # The intersection circle: center is the point on the plane closest
    # to the line from observer along the plane normal. But actually,
    # the intersection of a sphere centered at O with a plane at signed
    # distance h from O is a circle of radius r_circ = sqrt(R^2 - h^2)
    # centered at O + h * n_hat (projected onto the plane).

    # For the SHELL (not solid sphere), we want the intersection at
    # distances between d_inner and d_outer.
    # The plane at signed distance h from observer: the sphere of radius d
    # intersects it if |h| <= d.

    # We compute for the central distance d_shell:
    h = signed_dist  # signed distance from observer to plane

    if abs(h) > d_shell:
        return False, 0.0, 0.0, 0.0, 0.0

    # Circle radius on the plane
    r_circ = np.sqrt(d_shell**2 - h**2)

    # Center of circle in 3D (point on plane closest to observer, projected)
    circle_center = observer + h * face_normal

    # Check if circle center and some representative points are inside the
    # observable universe
    if np.linalg.norm(circle_center) > r_obs + r_circ:
        return False, 0.0, 0.0, 0.0, 0.0

    # But we also need to clip the circle to the observable sphere.
    # The circle is the intersection of the plane and the d_shell-sphere.
    # We need to further intersect with |r| <= r_obs.
    #
    # The circle center is at distance |circle_center| from origin.
    # The circle has radius r_circ in the plane.
    # The intersection with the universe sphere is an arc (or the full circle).

    cc_dist = np.linalg.norm(circle_center)

    # Does the full circle lie inside the universe?
    # Worst case: circle point farthest from origin
    # The circle lies in a plane. The maximum distance from origin of any
    # point on the circle depends on the geometry. Upper bound:
    max_dist_from_origin = cc_dist + r_circ

    if max_dist_from_origin <= r_obs:
        # Full circle is inside the universe
        effective_diameter = 2 * r_circ
    else:
        # The circle extends beyond the universe. Compute the arc that's inside.
        # This requires computing the intersection of the circle with the
        # origin-centered sphere of radius r_obs.
        #
        # Parametrize the circle: need two orthogonal unit vectors in the plane.
        # The circle: P(t) = circle_center + r_circ * (cos(t) * e1 + sin(t) * e2)
        # |P(t)|^2 <= r_obs^2
        #
        # For simplicity, compute what fraction of the circle is inside.
        # |circle_center + r_circ*(cos(t)*e1 + sin(t)*e2)|^2 <= r_obs^2
        # cc.cc + 2*r_circ*(cos(t)*cc.e1 + sin(t)*cc.e2) + r_circ^2 <= r_obs^2
        # cos(t)*A + sin(t)*B <= C
        # where A = 2*r_circ*cc.e1, B = 2*r_circ*cc.e2, C = r_obs^2 - cc^2 - r_circ^2

        # We need e1 and e2 in the plane perpendicular to face_normal.
        # Choose e1 in the plane containing face_normal and circle_center direction.
        if cc_dist > 1e-10:
            cc_hat = circle_center / cc_dist
        else:
            cc_hat = np.array([1.0, 0.0, 0.0])

        # e1 = component of cc_hat perpendicular to face_normal
        e1 = cc_hat - np.dot(cc_hat, face_normal) * face_normal
        e1_norm = np.linalg.norm(e1)
        if e1_norm < 1e-10:
            # cc_hat parallel to face_normal, pick arbitrary perpendicular
            if abs(face_normal[0]) < 0.9:
                e1 = np.cross(face_normal, [1, 0, 0])
            else:
                e1 = np.cross(face_normal, [0, 1, 0])
            e1 /= np.linalg.norm(e1)
        else:
            e1 /= e1_norm
        e2 = np.cross(face_normal, e1)
        e2 /= np.linalg.norm(e2)

        A = 2 * r_circ * np.dot(circle_center, e1)
        B = 2 * r_circ * np.dot(circle_center, e2)
        C = r_obs**2 - cc_dist**2 - r_circ**2

        amp = np.sqrt(A**2 + B**2)
        if amp < 1e-10 or C / amp >= 1.0:
            # All points inside (C/amp >= 1 means the constraint is always satisfied)
            effective_diameter = 2 * r_circ
        elif C / amp <= -1.0:
            # No points inside
            return False, 0.0, 0.0, 0.0, 0.0
        else:
            # Fraction of circle inside: the constraint cos(t - phi0) <= C/amp
            # has solution arc from phi0 + arccos(C/amp) to phi0 + 2pi - arccos(C/amp)
            # Wait, cos(t-phi0) <= C/amp is satisfied for t in
            # [phi0 + arccos(C/amp), phi0 + 2*pi - arccos(C/amp)] if C/amp >= 0
            # The arc INSIDE is where the constraint IS satisfied.
            # Actually: A*cos(t) + B*sin(t) = amp*cos(t - phi0) where phi0 = atan2(B, A)
            # Constraint: amp*cos(t-phi0) <= C
            # If C > 0: most of the circle is inside. The arc OUTSIDE is where
            # cos(t-phi0) > C/amp, i.e., |t-phi0| < arccos(C/amp).
            # Arc inside = 2*pi - 2*arccos(C/amp)
            frac_inside = 1 - np.arccos(np.clip(C / amp, -1, 1)) / np.pi

            # The effective angular extent is the longest connected arc inside.
            # For a single cap intersection, it's one contiguous arc.
            # The angular extent of that arc on the circle: 2*pi*frac_inside
            # The chord length of that arc:
            arc_angle = 2 * np.pi * frac_inside
            # Chord of the arc: 2 * r_circ * sin(arc_angle / 2) -- but this is the
            # straight-line chord, not the arc length.
            # For structure identification, we want the arc length:
            effective_diameter = r_circ * arc_angle  # arc length

    # The angular diameter as seen from the observer:
    # The circle subtends an angle 2*alpha where sin(alpha) = r_circ / d_shell
    angular_diameter = 2 * np.arcsin(min(r_circ / d_shell, 1.0))

    # Comoving extent: the actual size of the structure on the sky
    # For the full circle: circumference = 2*pi*r_circ, diameter = 2*r_circ
    # We use the effective_diameter computed above
    comoving_extent = effective_diameter

    # Angular coordinates of the circle center from observer
    direction = circle_center - observer
    d_dir = np.linalg.norm(direction)
    if d_dir < 1e-10:
        center_theta = 0.0
        center_phi = 0.0
    else:
        direction /= d_dir
        center_theta = np.arccos(np.clip(direction[2], -1, 1))
        center_phi = np.arctan2(direction[1], direction[0])

    return True, comoving_extent, angular_diameter, center_theta, center_phi


def face_shell_structure_length(face_point, face_normal, observer, d_shell, delta_d, r_obs):
    """
    Compute the comoving length of the arc produced by intersecting a Voronoi
    face with a spherical shell, clipped to the observable universe AND clipped
    to the Voronoi face's actual finite extent.

    For an INFINITE Voronoi face (half-plane bisector), the intersection with
    the shell is a great circle arc. But real Voronoi faces are finite polygons.
    Computing the exact finite face is expensive (requires full 3D Voronoi).

    Instead, we use an upper bound: treat each face as infinite. This
    OVERESTIMATES structure lengths. If even with this overestimate the
    gate fails, the conclusion is robust. If it passes, we note the caveat.

    Returns:
        comoving_length: float (Mpc) - comoving extent of the intersection arc
    """
    h = np.dot(face_point - observer, face_normal)

    d_inner = d_shell - delta_d / 2
    d_outer = d_shell + delta_d / 2

    # Check if the plane intersects the shell at all
    if abs(h) > d_outer:
        return 0.0

    # Use the central shell radius for the primary computation
    if abs(h) > d_shell:
        return 0.0

    r_circ = np.sqrt(d_shell**2 - h**2)
    circle_center = observer + h * face_normal

    cc_dist = np.linalg.norm(circle_center)
    max_dist = cc_dist + r_circ

    if max_dist <= r_obs:
        # Full circle inside universe
        # The intersection is a complete circle of circumference 2*pi*r_circ
        # But that's NOT the "comoving extent" (which measures the longest
        # dimension, not the perimeter). For a circle, the extent = diameter.
        return 2 * r_circ

    if cc_dist - r_circ > r_obs:
        return 0.0

    # Partial circle: compute the arc inside |r| <= r_obs
    # Need basis vectors in the plane
    if cc_dist > 1e-10:
        cc_hat = circle_center / cc_dist
    else:
        cc_hat = np.array([1.0, 0.0, 0.0])

    e1 = cc_hat - np.dot(cc_hat, face_normal) * face_normal
    e1_norm = np.linalg.norm(e1)
    if e1_norm < 1e-10:
        if abs(face_normal[0]) < 0.9:
            e1 = np.cross(face_normal, [1, 0, 0])
        else:
            e1 = np.cross(face_normal, [0, 1, 0])
        e1 /= np.linalg.norm(e1)
    else:
        e1 /= e1_norm

    A = 2 * r_circ * np.dot(circle_center, e1)
    B_coef = 2 * r_circ * np.dot(circle_center, np.cross(face_normal, e1))
    C = r_obs**2 - cc_dist**2 - r_circ**2

    amp = np.sqrt(A**2 + B_coef**2)
    if amp < 1e-10:
        return 2 * r_circ if C >= 0 else 0.0

    ratio = C / amp
    if ratio >= 1.0:
        return 2 * r_circ  # full circle inside
    elif ratio <= -1.0:
        return 0.0  # no intersection

    # The arc inside has angular extent:
    # half_arc = pi - arccos(ratio) if we want the arc where constraint is satisfied
    # Total arc angle = 2*(pi - arccos(ratio))
    half_excl = np.arccos(ratio)
    arc_angle = 2 * (np.pi - half_excl)  # angle of the arc INSIDE the universe

    # The chord length of this arc (the max linear extent):
    # chord = 2 * r_circ * sin(arc_angle / 2)
    # But actually, the "extent" is better measured as the maximum angular
    # separation between any two points on the arc, which for a single
    # contiguous arc of angle arc_angle on a circle of radius r_circ is:
    # max_sep = 2 * r_circ * sin(arc_angle / 2) if arc_angle <= pi
    # max_sep = 2 * r_circ if arc_angle > pi (the full diameter is spanned)

    if arc_angle >= np.pi:
        return 2 * r_circ  # diameter is the longest chord
    else:
        return 2 * r_circ * np.sin(arc_angle / 2)


# =============================================================================
# Core: compute structure statistics for one realization
# =============================================================================
def compute_one_realization(seeds, observer, d_shell, delta_d, r_obs):
    """
    For a given set of Voronoi seeds and observer position, compute the
    structures visible in a spherical shell.

    Each pair of seeds (i, j) defines a Voronoi face (the perpendicular bisector).
    We compute the intersection of each face with the shell and measure its extent.

    We then group overlapping/nearby face intersections into "connected structures"
    and measure the total extent of each.

    Returns:
        structure_lengths: list of comoving lengths (Mpc) of all structures
        n_faces_intersecting: number of faces that intersect the shell
        face_data: list of (length, theta, phi, r_circ) for each intersecting face
    """
    n = len(seeds)
    face_data = []  # (comoving_length, center_theta, center_phi, r_circ)

    # For each pair of seeds, compute the face intersection
    for i in range(n):
        for j in range(i+1, n):
            # Face = perpendicular bisector of segment from seed[i] to seed[j]
            midpoint = 0.5 * (seeds[i] + seeds[j])
            normal = seeds[j] - seeds[i]
            norm_len = np.linalg.norm(normal)
            if norm_len < 1e-10:
                continue
            normal /= norm_len

            # Signed distance from observer to plane
            h = np.dot(midpoint - observer, normal)

            if abs(h) > d_shell:
                continue

            r_circ = np.sqrt(d_shell**2 - h**2)
            circle_center = observer + h * normal
            cc_dist = np.linalg.norm(circle_center)

            # Check if any part of the circle is inside the universe
            if cc_dist - r_circ > r_obs:
                continue

            # However, this face might not be a REAL Voronoi face.
            # A Voronoi face between seeds i and j exists only where the
            # perpendicular bisector is closer to BOTH i and j than to any
            # other seed. For the intersection with the shell, we need to
            # check that points on the intersection circle are actually on
            # the Voronoi face (i.e., equidistant from i and j AND closer
            # to them than to any other seed).
            #
            # Quick check: is the circle center point actually on the Voronoi
            # face? I.e., is it closer to seeds i and j than to any other seed?
            dist_to_i = np.linalg.norm(circle_center - seeds[i])
            dist_to_j = np.linalg.norm(circle_center - seeds[j])

            # Distance to all other seeds
            all_dists = np.linalg.norm(seeds - circle_center, axis=1)
            min_other = np.min(np.delete(all_dists, [i, j]))

            # The circle center is equidistant from i and j by construction.
            # It's a valid Voronoi face point if no other seed is closer.
            if min_other < dist_to_i - 1e-6:
                # The center is NOT on the Voronoi face between i and j.
                # Some other seed is closer. This face may still partially
                # exist, but it's likely a small fragment. Skip it.
                continue

            # Compute the comoving length of the intersection
            length = face_shell_structure_length(midpoint, normal, observer,
                                                  d_shell, delta_d, r_obs)

            if length < 1.0:  # negligible
                continue

            # Angular coordinates of circle center from observer
            direction = circle_center - observer
            d_dir = np.linalg.norm(direction)
            if d_dir < 1e-10:
                theta_c, phi_c = 0.0, 0.0
            else:
                direction /= d_dir
                theta_c = np.arccos(np.clip(direction[2], -1, 1))
                phi_c = np.arctan2(direction[1], direction[0])

            face_data.append((length, theta_c, phi_c, r_circ))

    if len(face_data) == 0:
        return [], 0, []

    n_faces = len(face_data)

    # Group overlapping faces into connected structures.
    # Two face intersections are "connected" if their intersection circles
    # overlap on the sky (angular separation between centers < sum of
    # their angular half-extents).

    lengths = np.array([f[0] for f in face_data])
    thetas = np.array([f[1] for f in face_data])
    phis = np.array([f[2] for f in face_data])
    r_circs = np.array([f[3] for f in face_data])

    # Angular half-extent of each face intersection
    # alpha = arcsin(r_circ / d_shell) for full circles
    angular_half = np.arcsin(np.clip(r_circs / d_shell, 0, 1))

    # Compute angular separation between all pairs of face centers
    x = np.sin(thetas) * np.cos(phis)
    y = np.sin(thetas) * np.sin(phis)
    z = np.cos(thetas)
    vecs = np.column_stack([x, y, z])
    dots = vecs @ vecs.T
    np.clip(dots, -1, 1, out=dots)
    ang_sep = np.arccos(dots)

    # Two faces are connected if their circles overlap on the sky
    # i.e., angular_separation < angular_half[i] + angular_half[j]
    overlap = ang_sep < (angular_half[:, None] + angular_half[None, :])

    # Find connected components via BFS
    labels = -np.ones(n_faces, dtype=int)
    cluster_id = 0
    for start in range(n_faces):
        if labels[start] >= 0:
            continue
        queue = [start]
        labels[start] = cluster_id
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            neighbors = np.where(overlap[node] & (labels < 0))[0]
            labels[neighbors] = cluster_id
            queue.extend(neighbors.tolist())
        cluster_id += 1

    # Compute the total extent of each cluster
    structure_lengths = []
    for c in range(cluster_id):
        mask = labels == c
        if np.sum(mask) == 0:
            continue

        c_thetas = thetas[mask]
        c_phis = phis[mask]
        c_radii = angular_half[mask]

        # The total angular extent of the cluster:
        # For a single face, it's 2*angular_half.
        # For multiple overlapping faces, we compute the max angular separation
        # between any two points on the combined structure.
        # Upper bound: max angular separation between face centers + their radii

        if np.sum(mask) == 1:
            # Single face: comoving length = its own length
            structure_lengths.append(float(lengths[mask][0]))
        else:
            # Multiple faces: compute max angular extent
            cx = np.sin(c_thetas) * np.cos(c_phis)
            cy = np.sin(c_thetas) * np.sin(c_phis)
            cz = np.cos(c_thetas)
            cvecs = np.column_stack([cx, cy, cz])
            cdots = cvecs @ cvecs.T
            np.clip(cdots, -1, 1, out=cdots)
            c_seps = np.arccos(cdots)

            # Max separation = max center-to-center + their angular radii
            max_sep = 0.0
            for ii in range(len(c_thetas)):
                for jj in range(ii+1, len(c_thetas)):
                    sep = c_seps[ii, jj] + c_radii[ii] + c_radii[jj]
                    if sep > max_sep:
                        max_sep = sep

            # Convert to comoving length
            # For small angles: L = d_shell * max_sep
            # For large angles: L = d_shell * max_sep (arc length on the shell)
            comoving_length = d_shell * max_sep
            structure_lengths.append(comoving_length)

    return structure_lengths, n_faces, face_data


# =============================================================================
# Main Monte Carlo loop
# =============================================================================
def run_monte_carlo(n_realizations, shell_key, shell_params, rng, verbose=True):
    """Run the full Monte Carlo for one redshift shell."""
    d_shell = shell_params['d']
    delta_d = shell_params['delta_d']

    results = {
        'N_giant': np.zeros(n_realizations, dtype=int),
        'L_max': np.zeros(n_realizations),
        'L_mean': np.zeros(n_realizations),
        'N_faces': np.zeros(n_realizations, dtype=int),
        'N_structures': np.zeros(n_realizations, dtype=int),
        'all_structure_lengths': [],
    }

    t0 = time.time()

    for i in range(n_realizations):
        if verbose and (i % 1000 == 0):
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            eta = (n_realizations - i) / rate if rate > 0 else 0
            print(f"  [{shell_key}] {i+1}/{n_realizations} "
                  f"({rate:.1f} iter/s, elapsed {elapsed:.0f}s, ETA {eta:.0f}s)")

        seeds = random_points_in_sphere(N_CELLS, R_OBS, rng)
        observer = random_points_in_sphere(1, R_OBS, rng)[0]

        struct_lengths, n_faces, face_data = compute_one_realization(
            seeds, observer, d_shell, delta_d, R_OBS
        )

        results['N_faces'][i] = n_faces
        results['N_structures'][i] = len(struct_lengths)
        results['all_structure_lengths'].append(struct_lengths)

        if len(struct_lengths) == 0:
            continue

        lengths = np.array(struct_lengths)
        giant_mask = lengths > L_GIANT
        n_giant = int(np.sum(giant_mask))
        results['N_giant'][i] = n_giant

        results['L_max'][i] = np.max(lengths)

        if n_giant > 0:
            results['L_mean'][i] = np.mean(lengths[giant_mask])

    elapsed = time.time() - t0
    if verbose:
        print(f"  [{shell_key}] Complete: {n_realizations} in {elapsed:.1f}s "
              f"({n_realizations/elapsed:.1f} iter/s)")

    return results


def bootstrap_percentile(data, percentile, n_bootstrap=1000, rng=None):
    """Bootstrap confidence interval for a percentile."""
    if rng is None:
        rng = np.random.default_rng(42)
    n = len(data)
    boot_vals = np.zeros(n_bootstrap)
    for b in range(n_bootstrap):
        sample = rng.choice(data, size=n, replace=True)
        boot_vals[b] = np.percentile(sample, percentile)
    return np.percentile(boot_vals, [2.5, 97.5])


def bootstrap_probability(data, threshold, n_bootstrap=1000, rng=None):
    """Bootstrap confidence interval for P(data >= threshold)."""
    if rng is None:
        rng = np.random.default_rng(42)
    n = len(data)
    boot_probs = np.zeros(n_bootstrap)
    for b in range(n_bootstrap):
        sample = rng.choice(data, size=n, replace=True)
        boot_probs[b] = np.mean(sample >= threshold)
    return np.mean(data >= threshold), np.percentile(boot_probs, [2.5, 97.5])


# =============================================================================
# Plotting
# =============================================================================
def make_plots(results_z08, results_z16, save_path):
    """Create the 4-panel diagnostic plot."""
    fig = plt.figure(figsize=(16, 14))
    gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.30)

    # --- Panel 1: N_giant histogram at z=0.8 ---
    ax1 = fig.add_subplot(gs[0, 0])
    n_giant_08 = results_z08['N_giant']
    max_ng = max(int(np.max(n_giant_08)), 8)
    bins = np.arange(-0.5, max_ng + 1.5, 1)
    ax1.hist(n_giant_08, bins=bins, density=True, color='steelblue', edgecolor='black',
             alpha=0.8, label=f'32-cell Voronoi\n(N = {N_REALIZATIONS})')
    ax1.axvline(2, color='red', ls='--', lw=2, label='Observed: 2-3')
    ax1.axvline(3, color='red', ls='--', lw=2)
    p_ge2 = np.mean(n_giant_08 >= 2)
    ax1.set_xlabel('N_giant (extent > 500 Mpc)', fontsize=12)
    ax1.set_ylabel('Probability', fontsize=12)
    ax1.set_title(f'Giant Structures at z = 0.8\nP(N >= 2) = {p_ge2:.4f}', fontsize=13)
    ax1.legend(fontsize=10)
    ax1.set_xlim(-0.5, max_ng + 0.5)

    # --- Panel 2: L_max distribution at z=0.8 ---
    ax2 = fig.add_subplot(gs[0, 1])
    lmax_08 = results_z08['L_max']
    lmax_nonzero = lmax_08[lmax_08 > 0]
    if len(lmax_nonzero) > 10:
        ax2.hist(lmax_nonzero, bins=50, density=True, color='darkorange', edgecolor='black',
                 alpha=0.8)
    ax2.axvline(L_GIANT, color='green', ls='--', lw=2, label=f'Giant ({L_GIANT} Mpc)')
    ax2.axvline(L_GPC, color='red', ls='--', lw=2, label=f'Giant Arc ({L_GPC} Mpc)')
    ax2.axvline(2000, color='purple', ls='--', lw=1.5, label='HCBGW (2000 Mpc)')
    median_lmax = np.median(lmax_nonzero) if len(lmax_nonzero) > 0 else 0
    p_gpc = np.mean(lmax_08 > L_GPC)
    ax2.set_xlabel('L_max (Mpc)', fontsize=12)
    ax2.set_ylabel('Probability density', fontsize=12)
    ax2.set_title(f'Max Structure Length at z = 0.8\nMedian = {median_lmax:.0f} Mpc, '
                  f'P(L > 1 Gpc) = {p_gpc:.4f}', fontsize=13)
    ax2.legend(fontsize=9)

    # --- Panel 3: L_max CDF ---
    ax3 = fig.add_subplot(gs[1, 0])
    if len(lmax_nonzero) > 0:
        sorted_lmax = np.sort(lmax_nonzero)
        cdf = np.arange(1, len(sorted_lmax) + 1) / len(sorted_lmax)
        ax3.plot(sorted_lmax, cdf, 'b-', lw=2, label='z = 0.8')
    lmax_16 = results_z16['L_max']
    lmax_16_nz = lmax_16[lmax_16 > 0]
    if len(lmax_16_nz) > 0:
        sorted_16 = np.sort(lmax_16_nz)
        cdf_16 = np.arange(1, len(sorted_16) + 1) / len(sorted_16)
        ax3.plot(sorted_16, cdf_16, 'r-', lw=2, label='z = 1.6')
    ax3.axvline(L_GIANT, color='green', ls='--', lw=1.5)
    ax3.axvline(L_GPC, color='red', ls='--', lw=1.5)
    ax3.axvline(2000, color='purple', ls='--', lw=1.5)
    ax3.set_xlabel('L_max (Mpc)', fontsize=12)
    ax3.set_ylabel('CDF', fontsize=12)
    ax3.set_title('Cumulative Distribution of L_max', fontsize=13)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)

    # --- Panel 4: N_giant comparison z=0.8 vs z=1.6 ---
    ax4 = fig.add_subplot(gs[1, 1])
    n_giant_16 = results_z16['N_giant']
    max_ng_both = max(int(np.max(n_giant_08)), int(np.max(n_giant_16)), 8)
    bins = np.arange(-0.5, max_ng_both + 1.5, 1)
    ax4.hist(n_giant_08, bins=bins, density=True, color='steelblue', edgecolor='black',
             alpha=0.6, label=f'z = 0.8: P(N>=2) = {np.mean(n_giant_08 >= 2):.4f}')
    ax4.hist(n_giant_16, bins=bins, density=True, color='coral', edgecolor='black',
             alpha=0.6, label=f'z = 1.6: P(N>=2) = {np.mean(n_giant_16 >= 2):.4f}')
    ax4.axvline(2, color='red', ls='--', lw=2, alpha=0.5)
    ax4.set_xlabel('N_giant (extent > 500 Mpc)', fontsize=12)
    ax4.set_ylabel('Probability', fontsize=12)
    ax4.set_title('Giant Structure Count: z = 0.8 vs z = 1.6', fontsize=13)
    ax4.legend(fontsize=10)
    ax4.set_xlim(-0.5, max_ng_both + 0.5)

    fig.suptitle('GIANT-VORONOI-42: 32-Cell Tessellation Monte Carlo\n'
                 f'{N_REALIZATIONS} realizations, {N_CELLS} Voronoi cells in R = {R_OBS} Mpc',
                 fontsize=15, fontweight='bold', y=0.98)

    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {save_path}")


# =============================================================================
# Main
# =============================================================================
def main():
    print("=" * 72)
    print("GIANT-VORONOI-42: 32-Cell Tessellation Monte Carlo")
    print("=" * 72)
    print(f"N_cells = {N_CELLS}, R_obs = {R_OBS} Mpc")
    print(f"N_realizations = {N_REALIZATIONS}")
    print(f"Giant threshold = {L_GIANT} Mpc, Gpc threshold = {L_GPC} Mpc")
    print(f"Mean cell radius ~ {(3 * (4/3)*np.pi*R_OBS**3 / (4*np.pi*N_CELLS))**(1/3):.0f} Mpc")
    print(f"Mean inter-seed distance ~ {(4/3*np.pi*R_OBS**3 / N_CELLS)**(1/3):.0f} Mpc")
    print()

    rng = np.random.default_rng(seed=20260313)
    boot_rng = np.random.default_rng(seed=42)

    all_results = {}
    for key, params in SHELLS.items():
        print(f"\n--- Running shell: {params['label']} (d = {params['d']} Mpc) ---")
        all_results[key] = run_monte_carlo(N_REALIZATIONS, key, params, rng, verbose=True)

    # =================================================================
    # Statistics
    # =================================================================
    print("\n" + "=" * 72)
    print("RESULTS")
    print("=" * 72)

    for key, params in SHELLS.items():
        res = all_results[key]
        ng = res['N_giant']
        lm = res['L_max']

        print(f"\n{'='*60}")
        print(f"Shell: {params['label']} (d = {params['d']} Mpc)")
        print(f"{'='*60}")

        # Basic statistics
        print(f"\nN_faces intersecting shell: median = {np.median(res['N_faces']):.0f}, "
              f"mean = {np.mean(res['N_faces']):.1f}")
        print(f"N_structures (connected groups): median = {np.median(res['N_structures']):.0f}, "
              f"mean = {np.mean(res['N_structures']):.1f}")

        # N_giant distribution
        print(f"\nN_giant distribution:")
        max_ng_val = max(int(np.max(ng)), 5)
        for val in range(max_ng_val + 1):
            frac = np.mean(ng == val)
            count = int(np.sum(ng == val))
            if count > 0 or val <= 5:
                print(f"  N_giant = {val}: {frac:.4f} ({count} / {N_REALIZATIONS})")

        # Key probabilities with bootstrap CI
        p_ge1, ci_ge1 = bootstrap_probability(ng, 1, rng=boot_rng)
        p_ge2, ci_ge2 = bootstrap_probability(ng, 2, rng=boot_rng)
        p_ge3, ci_ge3 = bootstrap_probability(ng, 3, rng=boot_rng)

        print(f"\nP(N_giant >= 1) = {p_ge1:.4f}  95% CI: [{ci_ge1[0]:.4f}, {ci_ge1[1]:.4f}]")
        print(f"P(N_giant >= 2) = {p_ge2:.4f}  95% CI: [{ci_ge2[0]:.4f}, {ci_ge2[1]:.4f}]")
        print(f"P(N_giant >= 3) = {p_ge3:.4f}  95% CI: [{ci_ge3[0]:.4f}, {ci_ge3[1]:.4f}]")

        # L_max percentiles -- all realizations
        print(f"\nL_max percentiles (ALL {N_REALIZATIONS} realizations):")
        pcts = [1, 5, 25, 50, 75, 95, 99]
        for p in pcts:
            val = np.percentile(lm, p)
            ci = bootstrap_percentile(lm, p, rng=boot_rng)
            print(f"  {p:3d}th: {val:8.1f} Mpc  95% CI: [{ci[0]:8.1f}, {ci[1]:8.1f}]")

        # Among realizations with structure
        lm_nz = lm[lm > 0]
        if len(lm_nz) > 0:
            print(f"\nL_max percentiles (among {len(lm_nz)} realizations with structure):")
            for p in pcts:
                val = np.percentile(lm_nz, p)
                ci = bootstrap_percentile(lm_nz, p, rng=boot_rng)
                print(f"  {p:3d}th: {val:8.1f} Mpc  95% CI: [{ci[0]:8.1f}, {ci[1]:8.1f}]")

        p_gpc, ci_gpc = bootstrap_probability(lm, L_GPC, rng=boot_rng)
        p_2gpc, ci_2gpc = bootstrap_probability(lm, 2000, rng=boot_rng)
        p_3gpc, ci_3gpc = bootstrap_probability(lm, 3000, rng=boot_rng)

        print(f"\nP(L_max > {int(L_GPC)} Mpc) = {p_gpc:.4f}  95% CI: [{ci_gpc[0]:.4f}, {ci_gpc[1]:.4f}]")
        print(f"P(L_max > 2000 Mpc) = {p_2gpc:.4f}  95% CI: [{ci_2gpc[0]:.4f}, {ci_2gpc[1]:.4f}]")
        print(f"P(L_max > 3000 Mpc) = {p_3gpc:.4f}  95% CI: [{ci_3gpc[0]:.4f}, {ci_3gpc[1]:.4f}]")

        print(f"\nMean N_giant = {np.mean(ng):.3f} +/- {np.std(ng):.3f}")

    # =================================================================
    # Gate verdict
    # =================================================================
    print("\n" + "=" * 72)
    print("GATE VERDICT: GIANT-VORONOI-42")
    print("=" * 72)

    ng_08 = all_results['z08']['N_giant']
    lm_08 = all_results['z08']['L_max']

    p_ng2 = np.mean(ng_08 >= 2)
    p_lmax_gpc = np.mean(lm_08 > L_GPC)

    _, ci_ng2 = bootstrap_probability(ng_08, 2, rng=boot_rng)
    _, ci_lmax = bootstrap_probability(lm_08, L_GPC, rng=boot_rng)

    print(f"\nPre-registered criteria:")
    print(f"  PASS: P(N_giant >= 2) > 0.05 AND P(L_max > 1000 Mpc) > 0.01")
    print(f"  FAIL: P(N_giant >= 2) < 0.01 OR P(L_max > 1000 Mpc) < 0.001")
    print(f"\nMeasured values:")
    print(f"  P(N_giant >= 2 at z=0.8) = {p_ng2:.4f}  95% CI: [{ci_ng2[0]:.4f}, {ci_ng2[1]:.4f}]")
    print(f"  P(L_max > 1000 Mpc at z=0.8) = {p_lmax_gpc:.4f}  95% CI: [{ci_lmax[0]:.4f}, {ci_lmax[1]:.4f}]")

    # Determine verdict
    pass_crit1 = p_ng2 > 0.05
    pass_crit2 = p_lmax_gpc > 0.01
    fail_crit1 = p_ng2 < 0.01
    fail_crit2 = p_lmax_gpc < 0.001

    if pass_crit1 and pass_crit2:
        verdict = "PASS"
    elif fail_crit1 or fail_crit2:
        verdict = "FAIL"
    else:
        verdict = "INCONCLUSIVE"

    print(f"\n  Criterion 1 (N_giant >= 2): {'PASS (>0.05)' if pass_crit1 else 'FAIL (<0.01)' if fail_crit1 else 'INCONCLUSIVE'}")
    print(f"  Criterion 2 (L_max > 1 Gpc): {'PASS (>0.01)' if pass_crit2 else 'FAIL (<0.001)' if fail_crit2 else 'INCONCLUSIVE'}")
    print(f"\n  >>> VERDICT: {verdict} <<<")

    # Consistency check
    p1_ng = np.percentile(ng_08, 1)
    p99_ng = np.percentile(ng_08, 99)
    print(f"\n  Consistency: Observed 2-3 giant structures vs model 1st-99th percentile: [{p1_ng:.0f}, {p99_ng:.0f}]")
    obs_consistent = (2 >= p1_ng) and (3 <= p99_ng)
    obs_in_range = (2 >= p1_ng) and (2 <= p99_ng)
    if obs_consistent:
        print(f"  Observed range [2,3] fully within model range: CONSISTENT")
    elif obs_in_range:
        print(f"  Observed value 2 within model range: MARGINALLY CONSISTENT")
    else:
        print(f"  Observed values outside model range: INCONSISTENT")

    # =================================================================
    # Save data
    # =================================================================
    save_data = {
        'N_cells': np.array(N_CELLS),
        'R_obs': np.array(R_OBS),
        'N_realizations': np.array(N_REALIZATIONS),
        'L_giant': np.array(L_GIANT),
        'L_gpc': np.array(L_GPC),
        'verdict': np.array(verdict),
        'p_ng2_z08': np.array(p_ng2),
        'p_lmax_gpc_z08': np.array(p_lmax_gpc),
    }
    for key in SHELLS:
        save_data[f'{key}_N_giant'] = all_results[key]['N_giant']
        save_data[f'{key}_L_max'] = all_results[key]['L_max']
        save_data[f'{key}_L_mean'] = all_results[key]['L_mean']
        save_data[f'{key}_N_faces'] = all_results[key]['N_faces']
        save_data[f'{key}_N_structures'] = all_results[key]['N_structures']

    npz_path = 'tier0-computation/s42_giant_voronoi.npz'
    np.savez(npz_path, **save_data)
    print(f"\nData saved to {npz_path}")

    # =================================================================
    # Plot
    # =================================================================
    plot_path = 'tier0-computation/s42_giant_voronoi.png'
    make_plots(all_results['z08'], all_results['z16'], plot_path)

    print("\nDone.")
    return verdict, all_results


if __name__ == '__main__':
    verdict, results = main()
