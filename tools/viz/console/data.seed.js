// Ainulindalë Exflation — representative data slice.
// Hand-curated from the repository's knowledge base for the console exhibit.
// Values sourced from: tools/knowledge-index.json, computations/canonical_constants.py,
// and the Ainulindale Exflation Nutshell.md "The Numbers" table.

window.AE_DATA = (() => {
  // ------------------------------------------------------------------
  // Canonical constants
  // ------------------------------------------------------------------
  const CONSTANTS = [
    { id:'M_KK',         name:'M_KK',              value:'1e16 GeV',        tag:'mass scale',   note:'Kaluza-Klein scale; sets unit for all internal dynamics',                     src:'canonical_constants.py §B' },
    { id:'tau_fold',     name:'τ_fold',            value:'0.190',           tag:'moduli',       note:'Jensen deformation value where B2 group velocity vanishes',                   src:'T-ACOUSTIC-40' },
    { id:'tau_W',        name:'τ_0 (Weinberg)',    value:'0.2994',          tag:'moduli',       note:'sin²θ_W = e^(−4τ)/(1+e^(−4τ)) fixes τ₀ from experiment',                    src:'Session ≤34' },
    { id:'alpha_disp',   name:'α (curvature)',     value:'1.987',           tag:'dispersion',   note:'Dispersion curvature at the fold; sets acoustic-Hawking T',                   src:'T-ACOUSTIC-40' },
    { id:'T_a',          name:'T_acoustic',        value:'0.112 M_KK',      tag:'temperature',  note:'√α/(4π). Acoustic Hawking temperature of the phononic horizon',              src:'T-ACOUSTIC-40' },
    { id:'T_Gibbs',      name:'T_Gibbs',           value:'0.113 M_KK',      tag:'temperature',  note:'From 8-mode BCS partition function. Agrees with T_a to 0.7%',                 src:'Session 39' },
    { id:'S_full',       name:'S_full',            value:'250,361 M_KK',    tag:'spectral',     note:'Spectral action at fold — total Dirac-sea weight',                             src:'CUTOFF-SA-37' },
    { id:'dS_dtau',      name:'dS/dτ',             value:'+58,673',         tag:'spectral',     note:'Monotone upward — no equilibrium along Jensen',                                src:'Session 36' },
    { id:'E_cond',       name:'E_cond',            value:'−0.156 M_KK',     tag:'BCS',          note:'B2 Cooper-pair condensation energy',                                           src:'Session 35' },
    { id:'grad_ratio',   name:'Gradient ratio',    value:'6,596 : 1',       tag:'impedance',    note:'|dS_full/dτ| / |dE_BCS/dτ|. Acoustic impedance mismatch',                     src:'FRIED-39' },
    { id:'Gamma_refl',   name:'Γ reflection',      value:'0.99970',         tag:'impedance',    note:'99.97% back-reaction reflected. The 0.03% is all of physics',                src:'Derived' },
    { id:'N_pairs',      name:'N_pairs',           value:'59.8',            tag:'transit',      note:'Parker-creation quasiparticle pairs through the fold',                        src:'Session 38' },
    { id:'B2_retention', name:'B2 retention',      value:'89.1%',           tag:'transit',      note:'B2 diagonal-ensemble retention after transit',                                 src:'B2-DECAY-40' },
    { id:'omega_B2',     name:'ω_B2 collective',   value:'3.245 M_KK',      tag:'resonance',    note:'97.5% of energy-weighted sum rule in a single mode',                           src:'QRPA-40' },
    { id:'EWSR',         name:'EWSR concentration',value:'97.5%',           tag:'resonance',    note:'Single mode carries nearly all oscillator strength',                           src:'QRPA-40' },
    { id:'ratio_B2B1',   name:'ω_B2 / ω_B1',       value:'1.988',           tag:'resonance',    note:'Parametric 2:1 — B2 → 2·B1 resonance; 0.6% detuned',                          src:'QRPA-40' },
    { id:'H_min',        name:'Hessian min eig',   value:'+1,572',          tag:'stability',    note:'Min eigenvalue across 22 tested transverse directions',                        src:'HESS-40' },
    { id:'dLam_ratio',   name:'ΔΛ / S_fold',       value:'2.85 × 10⁻⁶',     tag:'CC',           note:'Cosmological-constant transit shift (before Carlip)',                          src:'CC-TRANSIT-40' },
    { id:'phi_Paasch',   name:'φ (Paasch)',        value:'1.53158',         tag:'mass',         note:'From x = e^(−x²); organizes PDG masses on 6 spiral arms',                     src:'Nutshell §1' },
    { id:'fN',           name:'fN',                value:'2 · φ_golden',    tag:'mass',         note:'Verified to 1.6 × 10⁻⁶ precision',                                             src:'Nutshell §1' },
    { id:'g_ratio',      name:'g₁/g₂ at fold',     value:'0.684',           tag:'gauge',        note:'e^(−2·0.190); SM value 0.553 at M_Z',                                          src:'Session ≤45' },
    { id:'p_alignment',  name:'p (Paasch align.)', value:'1.2 × 10⁻⁸',      tag:'mass',         note:'Statistical significance, 6 sequences',                                        src:'Nutshell §1' },
    { id:'a2_SD',        name:'a₂',                value:'0.728235',        tag:'spectral',     note:'Seeley-DeWitt a₂; Einstein-Hilbert coefficient',                               src:'S46 / S60s' },
  ];

  // ------------------------------------------------------------------
  // Theorems & closures (sampled from knowledge-index.json)
  // ------------------------------------------------------------------
  const THEOREMS = [
    { id:'T5',  name:'Barrett classification',                        status:'PROVEN',  session:'11',  area:'NCG',       statement:'Valid D_F guaranteed for KO-dim 6 + C³²' },
    { id:'T6',  name:'D_K block-diagonality',                         status:'PROVEN',  session:'22b', area:'spectral',  statement:'Exact in Peter-Weyl to 8.4×10⁻¹⁵ for any left-invariant metric', precision:'8.4e-15' },
    { id:'T7',  name:'[iK₇, D_K] = 0',                                 status:'PROVEN',  session:'34',  area:'symmetry',  statement:'Jensen breaks SU(3) → U(1)₇ exactly at all τ' },
    { id:'T8',  name:'[J, D_K(τ)] = 0',                                status:'PROVEN',  session:'17a', area:'symmetry',  statement:'CPT hardwired theorem — J commutes with D_K identically' },
    { id:'T9',  name:'CP = 0 structural',                              status:'PROVEN',  session:'3',   area:'symmetry',  statement:'Structural CP vanishing' },
    { id:'T11', name:'Jensen metric diagonal',                         status:'PROVEN',  session:'—',   area:'geometry',  statement:'g_τ = 3·diag(e^{2τ}×3, e^{−2τ}×4, e^τ) in Gell-Mann basis' },
    { id:'T12', name:'Weinberg angle relation',                        status:'PROVEN',  session:'—',   area:'gauge',     statement:'sin²θ_W = e^(−4τ)/(1+e^(−4τ)); τ₀ = 0.2994' },
    { id:'T13', name:'Spectral action trace theorem',                  status:'PROVEN',  session:'48',  area:'spectral',  statement:'S[UDU†] = S[D]; SA blind to U(1)₇ phase' },
    { id:'T14', name:'BCS instability is a 1D theorem',                status:'PROVEN',  session:'35',  area:'BCS',       statement:'Any g > 0 flows to strong coupling' },
    { id:'T16', name:'Mean-field BCS gives Δ = 0',                     status:'PROVEN',  session:'53',  area:'BCS',       statement:'Physical gap is beyond-mean-field (ED, instanton)' },
    { id:'T18', name:'BCS gradient exceeds geometric at fold',          status:'PROVEN',  session:'53',  area:'BCS',       statement:'|dE_cond/dV_KK| = 1.30' },
    { id:'T19', name:'Van Hove amplification',                         status:'PROVEN',  session:'53',  area:'spectral',  statement:'400× derivative-to-value ratio at fold' },
    { id:'T20', name:'BLV acoustic metric',                            status:'PROVEN',  session:'4',   area:'acoustic',  statement:'a_acoustic = a_geom · √(ρ/c_s)' },
    { id:'T21', name:'229× sound-speed hierarchy',                     status:'PROVEN',  session:'—',   area:'acoustic',  statement:'c_fabric/c_Gold = 229.5 → 2.72 acoustic e-folds' },
    { id:'T27', name:'OTOC growth t^1.9',                              status:'PROVEN',  session:'38',  area:'chaos',     statement:'No Lyapunov exponent — sub-ballistic scrambling' },
    { id:'T29', name:'Thouless conductance',                           status:'PROVEN',  session:'40',  area:'integrable',statement:'g_T = 0.087 for B2 subsystem' },
    { id:'T31', name:'Diagonal ensemble 89%',                          status:'PROVEN',  session:'40',  area:'integrable',statement:'Information retention after transit' },
    { id:'T40', name:'Berry projection PASS @ machine ε',              status:'PROVEN',  session:'62',  area:'NCG',       statement:'|A_coset|² = 3/2 + (3/2)e^{−4τ} exact across τ ∈ [0,0.5]', precision:'<2e-14' },
  ];

  // ------------------------------------------------------------------
  // Gates (with verdicts)
  // ------------------------------------------------------------------
  const GATES = [
    { id:'CUTOFF-SA-37',  verdict:'PASS',       session:'37', claim:'Spectral action monotone across cutoffs' },
    { id:'T-ACOUSTIC-40', verdict:'PASS',       session:'40', claim:'Acoustic Hawking T matches Gibbs T to 0.7%' },
    { id:'HESS-40',       verdict:'PASS',       session:'40', claim:'28D Hessian positive definite, 22/22 tested' },
    { id:'GSL-40',        verdict:'PASS',       session:'40', claim:'0/499 steps violate generalized second law' },
    { id:'CC-TRANSIT-40', verdict:'DIAGNOSTIC', session:'40', claim:'ΔΛ/S_fold = 2.85×10⁻⁶ — subject to Carlip' },
    { id:'B2-DECAY-40',   verdict:'PASS',       session:'40', claim:'B2 diagonal ensemble 89.1% retention' },
    { id:'B2-INTEG-40',   verdict:'PASS',       session:'40', claim:'8 Richardson-Gaudin conserved charges' },
    { id:'QRPA-40',       verdict:'PASS',       session:'40', claim:'EWSR concentration 97.5% in ω_B2' },
    { id:'KZ-D/H-3',      verdict:'PASS',       session:'3',  claim:'D/H = 2.74×10⁻⁵ vs observed 2.53×10⁻⁵ (~8%)' },
    { id:'FIRAS-CMB',     verdict:'OPEN',       session:'—',  claim:'Reproduce FIRAS blackbody from substrate modes' },
    { id:'T(z)=T0(1+z)',  verdict:'OPEN',       session:'—',  claim:'Scaling relation for CMB temperature' },
    { id:'A2-ROOT',       verdict:'HYPOTHESIS', session:'—',  claim:'6 Paasch angles from SU(3) Weyl group' },
    { id:'DIRAC-φ',       verdict:'OPEN',       session:'—',  claim:'φ = 1.53158 emerges from Dirac spectrum on (SU(3), g_s)' },
    { id:'COMMUTANT-A_F', verdict:'OPEN',       session:'6',  claim:'End_{U(2)}(Δ₈) ≅ ℂ ⊕ ℍ ⊕ M₃(ℂ)' },
    { id:'BERRY-PROJECTION-62', verdict:'PASS', session:'62', claim:'|A_coset|² selection rule, 16/136,480 modes' },
  ];

  // ------------------------------------------------------------------
  // Equations — the "atlas". Each variable links to a constant or to itself.
  // ------------------------------------------------------------------
  const EQUATIONS = [
    {
      id:'null_geodesic',
      title:'Null geodesic on M⁴ × K',
      tex:'|\\vec v|^{2} + g_{K}(v^{V},v^{V}) = c^{2}',
      vars:[
        { sym:'\\vec v',   refId:null,      desc:'3-velocity in M⁴' },
        { sym:'v^{V}',     refId:null,      desc:'Internal velocity on K = SU(3)' },
        { sym:'g_{K}',     refId:'T11',     desc:'Jensen-deformed metric on SU(3)' },
        { sym:'c',         refId:null,      desc:'Relay speed from full (4+8)D null cone' },
      ],
      cites:['T11','T20','T21'],
      session:'Baptista Paper 16',
      tier:'axiom',
      story:'A particle at rest in M⁴ is moving at full c internally. Mass = energy of that internal oscillation.'
    },
    {
      id:'KK_curvature',
      title:'KK curvature decomposition',
      tex:'R_{P} = R_{M} + R_{K} - |F|^{2} - |S|^{2} - |N|^{2}',
      vars:[
        { sym:'R_P', refId:null, desc:'Curvature of total space P = M⁴ × K' },
        { sym:'R_M', refId:null, desc:'4D spacetime curvature (gravity)' },
        { sym:'R_K', refId:null, desc:'Internal SU(3) curvature' },
        { sym:'F',   refId:null, desc:'Connection curvature (gauge)' },
        { sym:'S',   refId:null, desc:'Second fundamental form (Higgs)' },
        { sym:'N',   refId:null, desc:'Mean curvature (volume mode)' },
      ],
      cites:['T40'],
      session:'Baptista Paper 13',
      tier:'axiom',
      story:'Five channels. |N|² = 0 along Jensen — the crystal changes shape, not size.'
    },
    {
      id:'spectral_action',
      title:'Bosonic spectral action',
      tex:'S_B = \\operatorname{Tr}\\, f\\!\\left(\\frac{D^{2}}{\\Lambda^{2}}\\right) = f_{0}\\,a_{0}\\,\\Lambda^{4} + f_{2}\\,a_{2}\\,\\Lambda^{2} + f_{4}\\,a_{4} + \\cdots',
      vars:[
        { sym:'D',       refId:null,     desc:'Dirac operator on (SU(3), g_τ)' },
        { sym:'\\Lambda',refId:'M_KK',   desc:'UV cutoff set by M_KK' },
        { sym:'a_0',     refId:'S_full', desc:'Cosmological constant term' },
        { sym:'a_2',     refId:'a2_SD',  desc:'Einstein-Hilbert — = 1/(16πG)' },
        { sym:'a_4',     refId:null,     desc:'Yang-Mills + Higgs potential' },
      ],
      cites:['T13','T19'],
      session:'Session 37, 46',
      tier:'core',
      story:'One functional, three physical scales separated by powers of Λ. The sea\'s weight is the CC; its curvature-coupling is G_N.'
    },
    {
      id:'jensen_metric',
      title:'Jensen metric on SU(3)',
      tex:'g_{\\tau} = 3 \\cdot \\mathrm{diag}\\!\\left(e^{2\\tau}\\!\\cdot\\! 3,\\; e^{-2\\tau}\\!\\cdot\\! 4,\\; e^{\\tau}\\right)',
      vars:[
        { sym:'\\tau',   refId:'tau_fold', desc:'Jensen deformation parameter' },
      ],
      cites:['T11'],
      session:'Pre-7',
      tier:'axiom',
      story:'Diagonal in Gell-Mann basis. Three exponential eigenvalue scales — and those exponentials are where φ is whispering from.'
    },
    {
      id:'weinberg',
      title:'Weinberg angle from τ',
      tex:'\\sin^{2}\\theta_{W} = \\frac{e^{-4\\tau}}{1 + e^{-4\\tau}}',
      vars:[
        { sym:'\\tau', refId:'tau_W', desc:'Fixes τ₀ = 0.2994 from sin²θ_W = 0.23122' },
      ],
      cites:['T12'],
      session:'—',
      tier:'prediction',
      story:'The electroweak angle is a single number on the Jensen curve.'
    },
    {
      id:'acoustic_hawking',
      title:'Acoustic Hawking temperature',
      tex:'T_{a} = \\frac{\\sqrt{\\alpha}}{4\\pi}',
      vars:[
        { sym:'\\alpha', refId:'alpha_disp', desc:'Curvature of dispersion relation at the fold' },
        { sym:'T_a',     refId:'T_a',        desc:'= 0.112 M_KK' },
      ],
      cites:['T-ACOUSTIC-40'],
      session:'40',
      tier:'prediction',
      story:'Horizon T and partition-function T agree to 0.7% with zero free parameters. The cavity is in thermal equilibrium with itself.'
    },
    {
      id:'paasch_master',
      title:'Paasch mass quantization',
      tex:'N(j) = \\left(\\frac{m_{j}}{m_{e}}\\right)^{2/3};\\quad x = e^{-x^{2}} \\Rightarrow \\varphi = 1.53158',
      vars:[
        { sym:'\\varphi', refId:'phi_Paasch', desc:'Mass quantization base; NOT fitted' },
        { sym:'m_j',      refId:null,         desc:'Observed PDG mass' },
      ],
      cites:['A2-ROOT','DIRAC-φ'],
      session:'Nutshell §1',
      tier:'empirical',
      story:'6 sequences at specific angles. p ~ 1.2×10⁻⁸. Proton to 5×10⁻⁷. Scaffolding-independent.'
    },
    {
      id:'gradient_ratio',
      title:'Acoustic impedance mismatch',
      tex:'\\Gamma = \\frac{Z_{K}-Z_{M}}{Z_{K}+Z_{M}} = 0.99970 \\;\\; ; \\;\\; \\left|\\frac{dS_{\\text{full}}/d\\tau}{dE_{\\text{BCS}}/d\\tau}\\right| = 6{,}596',
      vars:[
        { sym:'\\Gamma',      refId:'Gamma_refl',  desc:'99.97% reflection' },
        { sym:'dS/d\\tau',    refId:'dS_dtau',     desc:'+58,673 (monotone)' },
        { sym:'E_{\\text{BCS}}', refId:'E_cond',   desc:'−0.156 M_KK' },
      ],
      cites:['CUTOFF-SA-37','T18'],
      session:'39',
      tier:'core',
      story:'A phonon cannot hold the lattice in place. 99.97% of back-reaction reflects. The 0.03% that leaks is every observation we have ever made.'
    },
    {
      id:'resonance_ratio',
      title:'Parametric 2:1 resonance',
      tex:'\\frac{\\omega_{B2}}{\\omega_{B1}} = 1.988 \\approx 2',
      vars:[
        { sym:'\\omega_{B2}', refId:'omega_B2',  desc:'Collective B2 frequency' },
        { sym:'\\omega_{B1}', refId:'ratio_B2B1',desc:'B1 band frequency' },
      ],
      cites:['QRPA-40'],
      session:'40',
      tier:'prediction',
      story:'Detuned parametric resonance. One B2 quantum can convert to two B1 quanta — and the 0.6% detuning protects B2 from decay.'
    },
    {
      id:'CC_transit',
      title:'CC transit shift',
      tex:'\\frac{\\Delta\\Lambda}{S_{\\text{fold}}} = 2.85\\times 10^{-6}',
      vars:[
        { sym:'\\Delta\\Lambda', refId:'dLam_ratio', desc:'Pre-Carlip residual' },
        { sym:'S_{\\text{fold}}',refId:'S_full',     desc:'250,361 M_KK' },
      ],
      cites:['CC-TRANSIT-40'],
      session:'40',
      tier:'prediction',
      story:'The memory of the transit, before Carlip suppression. Topological residuals are the open question.'
    },
  ];

  // ------------------------------------------------------------------
  // Sessions (selected) + tagged edges — nodes for the graph view
  // ------------------------------------------------------------------
  const SESSIONS = [
    { id:'S3',  label:'KZ sim → D/H = 2.74e-5',    area:'simulation', p:0.10 },
    { id:'S7',  label:'KO-dim = 6',                 area:'NCG',        p:0.12 },
    { id:'S11', label:'Barrett classification',     area:'NCG',        p:0.13 },
    { id:'S17a',label:'[J, D_K] = 0 (CPT)',          area:'symmetry',   p:0.15 },
    { id:'S22b',label:'D_K block-diagonality',      area:'spectral',   p:0.16 },
    { id:'S34', label:'U(1)₇ breaking',              area:'symmetry',   p:0.17 },
    { id:'S35', label:'BCS instability 1D theorem', area:'BCS',        p:0.18 },
    { id:'S36', label:'dS/dτ = +58,673',             area:'spectral',   p:0.18 },
    { id:'S37', label:'Spectral-action monotonicity',area:'spectral',  p:0.20 },
    { id:'S38', label:'Parker pairs: N = 59.8',     area:'transit',    p:0.21 },
    { id:'S39', label:'T_Gibbs = 0.113',             area:'transit',   p:0.22 },
    { id:'S40', label:'HESS-40 • QRPA • T_a',        area:'stability',  p:0.25 },
    { id:'S46', label:'a₂ = 0.728235',               area:'spectral',   p:0.27 },
    { id:'S48', label:'Spectral-action trace thm',   area:'spectral',   p:0.28 },
    { id:'S53', label:'Van Hove 400×',               area:'BCS',        p:0.30 },
    { id:'S57', label:'Leggett partition',           area:'BCS',        p:0.31 },
    { id:'S60', label:'NCG chain 7/7',               area:'NCG',        p:0.34 },
    { id:'S62', label:'Berry projection PASS',       area:'NCG',        p:0.36 },
    { id:'S65', label:'CC budget',                   area:'CC',         p:0.37 },
    { id:'S73b',label:'M1 convergence',              area:'simulation', p:0.38 },
    { id:'S74', label:'W0/ζ joint',                  area:'CC',         p:0.39 },
    { id:'S78', label:'DESI DR3 update',             area:'cosmo',      p:0.40 },
    { id:'S80', label:'Computation review',                area:'review',     p:0.40 },
    { id:'S82', label:'Latest',                      area:'review',     p:0.40 },
  ];

  // Edges: tagged relations between entities (sampled S81 schema)
  const EDGES = [
    { from:'S37', to:'S36', rel:'depends-on' },
    { from:'S40', to:'S37', rel:'uses' },
    { from:'S40', to:'S36', rel:'uses' },
    { from:'S40', to:'S39', rel:'confirms' },
    { from:'S39', to:'S38', rel:'follows' },
    { from:'S38', to:'S35', rel:'depends-on' },
    { from:'S35', to:'S34', rel:'requires' },
    { from:'S34', to:'S22b',rel:'specializes' },
    { from:'S22b',to:'S11', rel:'depends-on' },
    { from:'S11', to:'S7',  rel:'depends-on' },
    { from:'S53', to:'S35', rel:'revisits' },
    { from:'S53', to:'S37', rel:'tests' },
    { from:'S48', to:'S37', rel:'extends' },
    { from:'S46', to:'S40', rel:'calibrates' },
    { from:'S62', to:'S46', rel:'uses' },
    { from:'S65', to:'S40', rel:'aggregates' },
    { from:'S74', to:'S65', rel:'refines' },
    { from:'S78', to:'S74', rel:'updates' },
    { from:'S60', to:'S11', rel:'completes' },
    { from:'S57', to:'S53', rel:'follows' },
    { from:'S73b',to:'S38', rel:'validates' },
    { from:'S82', to:'S78', rel:'continues' },
    { from:'S80', to:'S74', rel:'reviews' },
    { from:'S17a',to:'S11', rel:'specializes' },
    { from:'S3',  to:'S38', rel:'bridges' },
  ];

  // ------------------------------------------------------------------
  // Dirac spectrum approximation for the Bell view.
  // Real count: 155,984 eigenvalues across branches B1/B2/B3 with multiplicities
  // from SU(3) irreps. For display we generate a structured representative
  // spectrum (band edges, degeneracies, fold pinch).
  // ------------------------------------------------------------------
  function buildSpectrum(tau){
    // Three branches with known hierarchies from nutshell
    //   B2 (adjoint) — lowest, flattest, fold pinch at τ=0.190
    //   B1 (fundamental) — first overtone
    //   B3 (higher reps) — optical branch above Debye cutoff
    const rng = mulberry32(0xAE1234);
    const points = [];
    const NB2 = 380, NB1 = 520, NB3 = 720;
    const foldDip = Math.exp(-Math.pow((tau - 0.190) * 14, 2));

    for (let i = 0; i < NB2; i++){
      const k = i / NB2;
      const base = 0.845 + 0.42 * k * k;
      const pinch = 0.32 * foldDip * Math.exp(-Math.pow((k - 0.05) * 6, 2));
      const val = base - pinch + 0.008 * (rng()-0.5);
      points.push({ branch:'B2', k, val, angle: (k * 360 + 30) % 360 });
    }
    for (let i = 0; i < NB1; i++){
      const k = i / NB1;
      const base = 1.22 + 0.55 * k * k + 0.08 * Math.sin(k * 6.28 * 2);
      const val = base + 0.06 * (tau - 0.190) * (1 - k) + 0.01 * (rng()-0.5);
      points.push({ branch:'B1', k, val, angle: (k * 360) % 360 });
    }
    for (let i = 0; i < NB3; i++){
      const k = i / NB3;
      const base = 2.10 + 0.9 * k + 0.1 * Math.sin(k * 6.28 * 3);
      const val = base + 0.02 * (rng()-0.5);
      points.push({ branch:'B3', k, val, angle: (k * 360 + 15) % 360 });
    }
    return points;
  }

  function mulberry32(seed){
    return function(){
      seed |= 0; seed = seed + 0x6D2B79F5 | 0;
      let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }

  // ------------------------------------------------------------------
  // Paasch spiral — 6 sequences with PDG mass proxies
  // ------------------------------------------------------------------
  const PAASCH = (() => {
    // Log-spiral with base phi. Six ray angles.
    const angles_deg = [12, 72, 132, 192, 252, 312]; // 60° apart w/ a 12° offset
    const labels_per_ray = [
      ['e','μ','τ','c','t'],                 // leptons/up-type
      ['ν','π⁰','η','ϒ(1S)','Z'],
      ['π±','K','ρ','φ','ϒ(3S)'],
      ['d','s','b','W','H'],                 // down-type
      ['u','η\'','J/ψ','Λ_c','B'],
      ['p','n','Δ','Σ','Ξ'],
    ];
    return angles_deg.map((a,i) => ({ angle:a, labels:labels_per_ray[i] }));
  })();

  // ------------------------------------------------------------------
  // Probability trajectory (conditional, ~30 sessions worth)
  // ------------------------------------------------------------------
  const TRAJECTORY = SESSIONS.map((s,i) => ({ t:i, label:s.id, p:s.p }));

  // ------------------------------------------------------------------
  // Researchers / analyst personas
  // ------------------------------------------------------------------
  const RESEARCHERS = [
    { id:'paasch',       label:'Paasch (mass quantization)',  hue:155 },
    { id:'baptista',     label:'Baptista (KK geometry)',       hue: 35 },
    { id:'jensen',       label:'Jensen (TT-deformation)',      hue:200 },
    { id:'tesla-voice',  label:'Tesla (resonance)',            hue:300 },
    { id:'connes',       label:'Connes (NCG)',                 hue: 60 },
    { id:'verlinde',     label:'Verlinde (emergence)',         hue:260 },
    { id:'einstein',     label:'Einstein (substrate principle)',hue:  0 },
    { id:'quantum-acoustics', label:'Quantum-acoustics (voice)',hue:180 },
    { id:'nazarewicz',   label:'Nazarewicz (nuclear analogy)', hue:220 },
    { id:'gen-physicist',label:'Gen-physicist (adversary)',    hue:330 },
  ];

  return {
    CONSTANTS, THEOREMS, GATES, EQUATIONS,
    SESSIONS, EDGES, TRAJECTORY, RESEARCHERS, PAASCH,
    buildSpectrum,
  };
})();
