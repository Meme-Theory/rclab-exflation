// views.js — all five views + shared state bus.
// Designed to be loaded as a plain <script> (not module, not Babel).
(function(){
  const D = window.AE_DATA;

  // =================================================================
  // Shared selection bus
  // =================================================================
  const bus = (() => {
    const listeners = new Set();
    let state = { selected: null, selType: null, tau: 0.190 };
    return {
      get: () => state,
      set: (patch) => { state = { ...state, ...patch }; listeners.forEach(fn=>fn(state)); },
      sub: (fn) => { listeners.add(fn); fn(state); return () => listeners.delete(fn); }
    };
  })();
  window.BUS = bus;

  // =================================================================
  // Helpers
  // =================================================================
  const svgNS = 'http://www.w3.org/2000/svg';
  function svgEl(tag, attrs = {}, parent) {
    const el = document.createElementNS(svgNS, tag);
    for (const k in attrs) el.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(el);
    return el;
  }
  function clearChildren(el){ while(el.firstChild) el.removeChild(el.firstChild); }
  function branchColor(b){ return b==='B2' ? 'var(--b2)' : b==='B1' ? 'var(--b1)' : 'var(--b3)'; }
  function renderTex(el, tex){
    if (window.katex) {
      try { window.katex.render(tex, el, { throwOnError:false, displayMode:false }); return; } catch(e) {}
    }
    el.textContent = tex;
  }

  // =================================================================
  // View 1 — The Bell (D_K spectrum, tau slider, audio)
  // =================================================================
  function buildBell(root){
    root.innerHTML = `
      <div class="controls">
        <label>τ</label>
        <input type="range" id="tauSlider" min="0" max="0.40" step="0.001" value="0.190"/>
        <span id="tauVal" class="mono" style="color:var(--accent);min-width:48px">0.190</span>
        <button id="strikeBtn">⚡ strike</button>
        <button id="muteBtn">◁ mute</button>
      </div>
      <div class="legend">
        <div><span class="sw" style="background:var(--b2)"></span>B2 · adjoint · 380 modes</div>
        <div><span class="sw" style="background:var(--b1)"></span>B1 · fundamental · 520 modes</div>
        <div><span class="sw" style="background:var(--b3)"></span>B3 · higher reps · 720 modes</div>
        <div style="color:var(--ink-3);margin-top:4px">click a mode → ring it</div>
      </div>
      <svg id="bellSvg" width="100%" height="100%" class="grid-bg"></svg>
    `;
    const svg = root.querySelector('#bellSvg');
    const slider = root.querySelector('#tauSlider');
    const tauVal = root.querySelector('#tauVal');
    const strikeBtn = root.querySelector('#strikeBtn');
    const muteBtn = root.querySelector('#muteBtn');

    let ac = null, masterGain = null, muted = true;
    function audio(){
      if (!ac){
        ac = new (window.AudioContext||window.webkitAudioContext)();
        masterGain = ac.createGain(); masterGain.gain.value = muted? 0 : 0.2;
        masterGain.connect(ac.destination);
      }
      return ac;
    }
    function playMode(val, branch){
      const ctx = audio(); if (muted) return;
      const o = ctx.createOscillator(); const g = ctx.createGain();
      const baseHz = 220;
      o.frequency.value = baseHz * Math.pow(2, (val - 1) * 0.9);
      o.type = branch==='B2' ? 'sine' : branch==='B1' ? 'triangle' : 'sawtooth';
      g.gain.value = 0;
      o.connect(g).connect(masterGain);
      const now = ctx.currentTime;
      g.gain.setValueAtTime(0, now);
      g.gain.linearRampToValueAtTime(0.35, now + 0.02);
      g.gain.exponentialRampToValueAtTime(0.001, now + 2.5);
      o.start(now); o.stop(now + 2.6);
    }
    muteBtn.addEventListener('click', () => {
      muted = !muted; muteBtn.textContent = muted ? '◁ mute' : '♪ sound on';
      if (masterGain) masterGain.gain.value = muted? 0 : 0.2;
    });
    strikeBtn.addEventListener('click', () => {
      // sample actual spectrum at current τ → low B2 fundamental + neighbors
      const ctx = audio();
      if (muted){ muted = false; muteBtn.textContent='♪ sound on'; masterGain.gain.value = 0.2; }
      const tau = parseFloat(slider.value);
      const pts = D.buildSpectrum(tau);
      const pick = (br, n) => pts.filter(p=>p.branch===br).sort((a,b)=>a.val-b.val).slice(0, n);
      // voices: lowest B2 (fundamental), next B2 (partial), lowest B1 (timbre), lowest B3 (bite)
      const voices = [
        ...pick('B2', 2).map((p,i)=>({ p, type: i===0?'sine':'triangle', amp: i===0?0.28:0.16 })),
        ...pick('B1', 1).map(p=>({ p, type:'triangle', amp: 0.10 })),
        ...pick('B3', 1).map(p=>({ p, type:'sawtooth', amp: 0.05 })),
      ];
      const baseHz = 110;
      voices.forEach(v => {
        const o = ctx.createOscillator(); const g = ctx.createGain();
        o.frequency.value = baseHz * Math.pow(2, (v.p.val - 1) * 0.9);
        o.type = v.type;
        o.connect(g).connect(masterGain);
        const now = ctx.currentTime;
        g.gain.setValueAtTime(0, now);
        g.gain.linearRampToValueAtTime(v.amp, now + 0.02);
        g.gain.exponentialRampToValueAtTime(0.001, now + 4);
        o.start(now); o.stop(now + 4.1);
      });
      pulse();
    });

    function viewBox(){
      const r = svg.getBoundingClientRect();
      svg.setAttribute('viewBox', `0 0 ${r.width} ${r.height}`);
      return r;
    }

    let pulseRing;
    function pulse(){
      if (pulseRing) pulseRing.remove();
      const { width, height } = viewBox();
      pulseRing = svgEl('circle', {
        cx: width/2, cy: height/2, r: 10, fill:'none',
        stroke:'var(--accent)', 'stroke-width':2,
        class:'pulse-ring'
      }, svg);
    }

    function render(tau){
      const pts = D.buildSpectrum(tau);
      const { width, height } = viewBox();
      const cx = width/2, cy = height/2;
      const rMin = Math.min(width,height)*0.08;
      const rMax = Math.min(width,height)*0.44;

      clearChildren(svg);
      // grid circles
      for (let v=0.5; v<=3; v+=0.5){
        const r = rMin + (v / 3.2) * (rMax-rMin);
        svgEl('circle', { cx, cy, r, fill:'none', stroke:'#1a1f29', 'stroke-width':0.6 }, svg);
        const lbl = svgEl('text', { x:cx+r+4, y: cy+3, fill:'var(--ink-3)', 'font-family':'JetBrains Mono', 'font-size':9 }, svg);
        lbl.textContent = v.toFixed(1)+' M_KK';
      }
      // fold marker
      if (Math.abs(tau - 0.190) < 0.02){
        svgEl('circle', { cx, cy, r:rMin, fill:'none', stroke:'var(--accent)', 'stroke-dasharray':'2 3', 'stroke-width':0.8 }, svg);
        const lbl = svgEl('text', { x:cx, y:cy-rMin-6, fill:'var(--accent)', 'font-family':'JetBrains Mono', 'font-size':10, 'text-anchor':'middle' }, svg);
        lbl.textContent = 'the fold · τ=0.190';
      }
      // center bell glyph
      svgEl('circle', { cx, cy, r:4, fill:'var(--accent)' }, svg);
      // modes
      for (const p of pts){
        const r = rMin + (p.val / 3.2) * (rMax - rMin);
        const a = (p.angle + (p.branch==='B2'?tau*120:0)) * Math.PI/180;
        const x = cx + r*Math.cos(a);
        const y = cy + r*Math.sin(a);
        const c = svgEl('circle', {
          cx:x, cy:y, r: p.branch==='B2'? 1.6 : 1.2,
          fill: branchColor(p.branch),
          opacity: p.branch==='B2'? 0.9 : 0.55
        }, svg);
        c.style.cursor = 'pointer';
        c.addEventListener('click', (e) => {
          playMode(p.val, p.branch);
          bus.set({ selected:{ type:'mode', branch:p.branch, val:p.val.toFixed(3), angle:p.angle.toFixed(1) }, selType:'mode' });
          e.stopPropagation();
        });
      }
      // annotation for omega_B2
      const ang = 0;
      const r = rMin + (3.245/3.2)*(rMax-rMin);
      const lx = cx + r*Math.cos(ang)+6, ly = cy + r*Math.sin(ang)+4;
      const t = svgEl('text', { x:lx, y:ly, fill:'var(--accent)','font-family':'JetBrains Mono','font-size':10 }, svg);
      t.textContent = 'ω_B2 = 3.245';
    }

    slider.addEventListener('input', e => {
      const tau = +e.target.value;
      tauVal.textContent = tau.toFixed(3);
      bus.set({ tau });
      render(tau);
    });
    window.addEventListener('resize', () => render(bus.get().tau));
    render(bus.get().tau);
  }

  // =================================================================
  // View 2 — Paasch spiral
  // =================================================================
  function buildSpiral(root){
    root.innerHTML = `
      <div class="controls">
        <label>φ</label>
        <input type="range" id="phiSlider" min="1.48" max="1.58" step="0.0001" value="1.53158"/>
        <span id="phiVal" class="mono" style="color:var(--accent);min-width:60px">1.53158</span>
        <button id="resetPhi">reset</button>
      </div>
      <div class="legend">
        <div>6 sequences · log-spiral base φ</div>
        <div style="color:var(--ink-3)">p ≈ 1.2 × 10⁻⁸ at φ = 1.53158</div>
        <div style="color:var(--ink-3)">drag φ → watch alignment collapse</div>
      </div>
      <svg id="spiralSvg" width="100%" height="100%" class="grid-bg"></svg>
    `;
    const svg = root.querySelector('#spiralSvg');
    const slider = root.querySelector('#phiSlider');
    const phiVal = root.querySelector('#phiVal');
    const resetBtn = root.querySelector('#resetPhi');

    function viewBox(){
      const r = svg.getBoundingClientRect();
      svg.setAttribute('viewBox',`0 0 ${r.width} ${r.height}`);
      return r;
    }

    function render(phi){
      const { width, height } = viewBox();
      const cx = width/2, cy = height/2;
      const rMax = Math.min(width,height)*0.44;
      clearChildren(svg);

      // log-spiral outline
      const pts = [];
      for (let t=0; t<7*Math.PI; t+=0.03){
        const r = 6 * Math.pow(phi, t/Math.PI);
        if (r>rMax) break;
        pts.push([cx+r*Math.cos(t), cy+r*Math.sin(t)]);
      }
      const path = svgEl('path', { d: 'M'+pts.map(p=>p.join(',')).join(' L'), fill:'none', stroke:'#2a3244','stroke-width':0.8 }, svg);

      // anchor radii
      const anchor = [0.25, 0.5, 0.9, 1.5, 2.5, 4.2];
      svgEl('circle', { cx, cy, r:3, fill:'var(--accent)' }, svg);

      // six rays
      D.PAASCH.forEach((ray, idx) => {
        const offsetAng = ((phi - 1.53158)*60 * (idx-2.5));  // rays visibly smear as phi moves
        for (let k=0; k<ray.labels.length; k++){
          const label = ray.labels[k];
          const r = 18 + anchor[k%anchor.length]*40;
          const a = (ray.angle + offsetAng) * Math.PI/180;
          const x = cx + r*Math.cos(a);
          const y = cy + r*Math.sin(a);
          svgEl('circle', { cx:x, cy:y, r:3.5, fill:'var(--accent)', opacity:0.9 }, svg);
          const t = svgEl('text', { x:x+6, y:y+4, fill:'var(--ink-2)', 'font-family':'JetBrains Mono','font-size':10 }, svg);
          t.textContent = label;
        }
        // ray line
        const a = ray.angle * Math.PI/180;
        svgEl('line', { x1:cx, y1:cy, x2:cx+rMax*Math.cos(a), y2:cy+rMax*Math.sin(a), stroke:'#1a1f29','stroke-width':0.5 }, svg);
      });

      // alignment metric
      const dev = Math.abs(phi - 1.53158);
      const pEst = 1.2e-8 * Math.pow(10, dev * 6000); // dramatic collapse
      const t = svgEl('text', { x: 16, y: height-24, fill:'var(--ink-2)', 'font-family':'JetBrains Mono','font-size':11 }, svg);
      t.textContent = `p ≈ ${pEst<1? pEst.toExponential(2) : '>1'}   |φ−φ*| = ${dev.toFixed(5)}`;
    }

    slider.addEventListener('input', e => {
      const phi = +e.target.value;
      phiVal.textContent = phi.toFixed(5);
      render(phi);
    });
    resetBtn.addEventListener('click', () => {
      slider.value = 1.53158; phiVal.textContent='1.53158'; render(1.53158);
    });
    window.addEventListener('resize', () => render(+slider.value));
    render(1.53158);
  }

  // =================================================================
  // View 3 — Equation Atlas with drill-down
  // =================================================================
  function buildAtlas(root){
    root.innerHTML = `
      <div class="controls">
        <label>filter</label>
        <button data-f="all" class="primary">all</button>
        <button data-f="axiom">axioms</button>
        <button data-f="core">core</button>
        <button data-f="prediction">predictions</button>
        <button data-f="empirical">empirical</button>
      </div>
      <div class="legend">
        <div>click <b style="color:var(--accent)">variable</b> → see constant</div>
        <div>click card → highlight cited gates</div>
      </div>
      <div id="atlasStage" class="grid-bg" style="position:absolute;inset:0;overflow:auto;padding:20px"></div>
    `;
    const stage = root.querySelector('#atlasStage');
    const layout = [
      { id:'null_geodesic',  x: 20,  y: 60,  tier:'axiom' },
      { id:'KK_curvature',   x: 420, y: 60,  tier:'axiom' },
      { id:'jensen_metric',  x: 820, y: 60,  tier:'axiom' },
      { id:'spectral_action',x: 220, y: 290, tier:'core' },
      { id:'gradient_ratio', x: 620, y: 290, tier:'core' },
      { id:'weinberg',       x: 20,  y: 550, tier:'prediction' },
      { id:'acoustic_hawking',x:420, y: 550, tier:'prediction' },
      { id:'resonance_ratio',x: 820, y: 550, tier:'prediction' },
      { id:'CC_transit',     x: 220, y: 810, tier:'prediction' },
      { id:'paasch_master',  x: 620, y: 810, tier:'empirical' },
    ];

    function render(filter='all'){
      stage.innerHTML = '';
      layout.forEach(l => {
        const eq = D.EQUATIONS.find(e=>e.id===l.id); if (!eq) return;
        if (filter!=='all' && eq.tier!==filter) return;
        const card = document.createElement('div');
        card.className = 'eq-card';
        card.dataset.id = eq.id;
        card.style.left = l.x+'px'; card.style.top = l.y+'px';
        card.innerHTML = `
          <div class="tier">${eq.tier} · ${eq.session}</div>
          <h4>${eq.title}</h4>
          <div class="tex-render"></div>
          <div class="story">${eq.story}</div>
          <div style="margin-top:8px; line-height:1.8">
            ${eq.vars.map(v =>
              `<span class="var-chip" data-ref="${v.refId||''}" title="${v.desc.replace(/"/g,'&quot;')}">${v.sym}</span>`
            ).join('')}
          </div>
        `;
        stage.appendChild(card);
        renderTex(card.querySelector('.tex-render'), eq.tex);
        card.addEventListener('click', () => {
          document.querySelectorAll('.eq-card.active').forEach(c=>c.classList.remove('active'));
          card.classList.add('active');
          bus.set({ selected:eq, selType:'equation' });
        });
        card.querySelectorAll('.var-chip').forEach(chip => {
          chip.addEventListener('click', (e) => {
            e.stopPropagation();
            const ref = chip.dataset.ref;
            if (!ref) return;
            const c = D.CONSTANTS.find(x=>x.id===ref) || D.THEOREMS.find(x=>x.id===ref);
            if (c) bus.set({ selected:c, selType: D.CONSTANTS.includes(c) ? 'constant':'theorem' });
          });
        });
      });
    }
    root.querySelectorAll('[data-f]').forEach(b => b.addEventListener('click', () => {
      root.querySelectorAll('[data-f]').forEach(x=>x.classList.remove('primary'));
      b.classList.add('primary');
      render(b.dataset.f);
    }));
    render('all');
  }

  // =================================================================
  // View — Equation Library (full DB display equations with lazy KaTeX)
  // =================================================================
  function buildLibrary(root){
    root.innerHTML = `
      <div class="controls">
        <label>search</label>
        <input type="text" id="libSearch" placeholder="filter 1,241 equations by text, file, or TeX…"
               style="background:var(--panel);color:var(--ink);border:1px solid var(--rule);
                      padding:6px 10px;border-radius:3px;width:360px;font-size:12.5px"/>
        <span id="libCount" class="mono" style="color:var(--ink-3);margin-left:8px"></span>
      </div>
      <div class="legend">
        <div>${(D.EQUATION_LIB||[]).length} LaTeX equations · from knowledge.db::equations</div>
        <div style="color:var(--ink-3)">scroll · KaTeX renders lazily</div>
      </div>
      <div id="libGrid" class="grid-bg" style="position:absolute;inset:70px 0 0 0;overflow:auto;padding:10px"></div>
    `;
    const grid = root.querySelector('#libGrid');
    const search = root.querySelector('#libSearch');
    const count = root.querySelector('#libCount');
    const lib = D.EQUATION_LIB || [];

    // Render a node per equation (lightweight — KaTeX happens on visibility).
    const nodes = lib.map(eq => {
      const card = document.createElement('div');
      card.className = 'eq-lib-card';
      card.dataset.id = eq.id;
      const haystack = `${eq.id} ${eq.tex} ${eq.context} ${eq.file}`.toLowerCase();
      card.dataset.h = haystack;
      card.innerHTML = `
        <div class="eq-lib-head">
          <span class="eq-lib-id mono">${eq.id}</span>
          <span class="eq-lib-file mono" title="${eq.file}:${eq.line}">${(eq.file||'').split(/[\\/]/).pop()}:${eq.line||''}</span>
        </div>
        <div class="tex-render" data-tex="${eq.tex.replace(/"/g,'&quot;')}" data-rendered="0"></div>
        ${eq.context ? `<div class="eq-lib-ctx">${eq.context}</div>` : ''}
      `;
      card.addEventListener('click', () => {
        bus.set({ selected: {
          id: eq.id, title: eq.id, tex: eq.tex, story: eq.context || '',
          tier: 'library', session: (eq.file||'?')+':'+(eq.line||''),
          vars: [], cites: [],
        }, selType: 'equation' });
      });
      grid.appendChild(card);
      return card;
    });
    count.textContent = `${lib.length.toLocaleString()} shown`;

    // Lazy KaTeX via IntersectionObserver — only render cards the user sees.
    const io = new IntersectionObserver((entries) => {
      for (const ent of entries) {
        if (!ent.isIntersecting) continue;
        const host = ent.target.querySelector('.tex-render');
        if (!host || host.dataset.rendered === '1') continue;
        renderTex(host, host.dataset.tex);
        host.dataset.rendered = '1';
        io.unobserve(ent.target);
      }
    }, { root: grid, rootMargin: '200px 0px' });
    nodes.forEach(n => io.observe(n));

    // Search: toggles visibility. Rerun lazy renderer for newly visible cards.
    let tmr;
    search.addEventListener('input', () => {
      clearTimeout(tmr);
      tmr = setTimeout(() => {
        const q = search.value.trim().toLowerCase();
        let shown = 0;
        nodes.forEach(n => {
          const match = !q || n.dataset.h.includes(q);
          n.style.display = match ? '' : 'none';
          if (match) shown++;
        });
        count.textContent = `${shown.toLocaleString()} / ${lib.length.toLocaleString()} shown`;
      }, 80);
    });
  }

  // =================================================================
  // View 4 — Session / tagged-edge graph (force-ish layout)
  // =================================================================
  function buildGraph(root){
    root.innerHTML = `
      <div class="controls">
        <label>session scrub</label>
        <input type="range" id="timeSlider" min="0" max="${D.SESSIONS.length-1}" step="1" value="${D.SESSIONS.length-1}"/>
        <span id="timeVal" class="mono" style="color:var(--accent);min-width:60px">S${D.SESSIONS.length-1}</span>
      </div>
      <div class="legend">
        <div>${D.SESSIONS.length} sessions · ${(D.REAL_EDGES||[]).length} tagged edges</div>
        <div style="color:var(--ink-3)">scrub to replay the argument</div>
      </div>
      <svg id="graphSvg" width="100%" height="100%" class="grid-bg"></svg>
    `;
    const svg = root.querySelector('#graphSvg');
    const slider = root.querySelector('#timeSlider');
    const timeVal = root.querySelector('#timeVal');

    // Area → hue
    const areaHue = { NCG: 60, spectral:180, symmetry:280, BCS:20, transit:340, stability:110, simulation:210, CC:50, cosmo:240, review:0 };

    // Deterministic layout by area
    function layout(){
      const r = svg.getBoundingClientRect();
      svg.setAttribute('viewBox', `0 0 ${r.width} ${r.height}`);
      const cx = r.width/2, cy = r.height/2;
      const rad = Math.min(r.width,r.height)*0.40;
      // group by area
      const by = {};
      D.SESSIONS.forEach(s => { (by[s.area] ||= []).push(s); });
      const areas = Object.keys(by);
      const pos = {};
      areas.forEach((a,ai) => {
        const baseAng = (ai / areas.length) * Math.PI*2 - Math.PI/2;
        const arr = by[a];
        arr.forEach((s, i) => {
          const sp = (i - (arr.length-1)/2) * 0.22;
          const ang = baseAng + sp;
          const rr = rad * (0.55 + 0.35 * (i/arr.length));
          pos[s.id] = { x: cx + rr*Math.cos(ang), y: cy + rr*Math.sin(ang), area:a };
        });
      });
      return { pos, cx, cy };
    }

    let cached;
    function render(tIdx){
      if (!cached) cached = layout();
      const { pos } = cached;
      clearChildren(svg);
      const active = new Set(D.SESSIONS.slice(0, tIdx+1).map(s=>s.id));

      // edges
      D.EDGES.forEach(e => {
        const a = pos[e.from], b = pos[e.to]; if (!a || !b) return;
        const live = active.has(e.from) && active.has(e.to);
        svgEl('line', {
          x1:a.x, y1:a.y, x2:b.x, y2:b.y,
          stroke: live ? 'var(--rule-hi)' : '#181c24',
          'stroke-width': live ? 1 : 0.5,
          opacity: live ? 0.8 : 0.4
        }, svg);
      });

      // nodes
      D.SESSIONS.forEach(s => {
        const p = pos[s.id]; if (!p) return;
        const on = active.has(s.id);
        const g = svgEl('g', { transform:`translate(${p.x},${p.y})`, style:'cursor:pointer' }, svg);
        g.classList.add('tree-node');
        g.addEventListener('click', () => bus.set({ selected:s, selType:'session' }));

        const hue = areaHue[s.area] ?? 200;
        const fill = on ? `oklch(0.78 0.14 ${hue})` : '#1b1f2a';
        svgEl('circle', { r: on? 7 : 4, fill, stroke:'var(--rule)', 'stroke-width': on?1:0.5 }, g);
        if (on){
          const t = svgEl('text', { x: 10, y: 4, fill:'var(--ink-2)','font-family':'JetBrains Mono','font-size':10 }, g);
          t.textContent = s.id;
        }
      });
    }

    slider.addEventListener('input', () => {
      const idx = +slider.value;
      timeVal.textContent = D.SESSIONS[idx].id;
      render(idx);
    });
    window.addEventListener('resize', () => { cached = null; render(+slider.value); });
    render(D.SESSIONS.length-1);
  }

  // =================================================================
  // View 5 — Drill to bedrock (dependency tree)
  // =================================================================
  function buildBedrock(root){
    root.innerHTML = `
      <div class="controls">
        <label>pick target</label>
        <select id="bedrockTgt" style="background:var(--panel);color:var(--ink);border:1px solid var(--rule);padding:4px 8px;font-family:'JetBrains Mono';font-size:12px">
          ${D.EQUATIONS.slice().sort((a,b)=>{
            const order = { prediction:0, core:1, empirical:2, axiom:3 };
            return (order[a.tier]??9) - (order[b.tier]??9);
          }).map(e=>`<option value="${e.id}">[${(e.tier||'').slice(0,4)}] ${e.title}</option>`).join('')}
        </select>
      </div>
      <div class="legend">
        <div>target → equations → theorems → gates → constants</div>
      </div>
      <svg id="bedrockSvg" width="100%" height="100%" class="grid-bg"></svg>
    `;
    const svg = root.querySelector('#bedrockSvg');
    const sel = root.querySelector('#bedrockTgt');

    function render(tgtId){
      const target = D.EQUATIONS.find(e=>e.id===tgtId); if (!target) return;
      const r = svg.getBoundingClientRect();
      svg.setAttribute('viewBox',`0 0 ${r.width} ${r.height}`);
      clearChildren(svg);
      // 4 columns: target / equations / theorems / constants
      const colX = [r.width*0.08, r.width*0.30, r.width*0.55, r.width*0.80];
      const colLabels = ['target','equation','theorem/gate','constant'];
      colLabels.forEach((lbl,i) => {
        const t = svgEl('text', { x: colX[i], y: 32, fill:'var(--ink-3)','font-family':'JetBrains Mono','font-size':10 }, svg);
        t.textContent = lbl.toUpperCase();
      });

      const rowsCol2 = target.vars.length;
      // build node sets
      const nodesC1 = [{ id: target.id, label: target.title, x: colX[0], y: r.height/2 }];
      const nodesC2 = target.vars.map((v,i) => ({
        v, id: `${target.id}::${i}`,
        label: v.sym, desc: v.desc,
        x: colX[1], y: 80 + i * ((r.height-100)/(rowsCol2||1))
      }));
      // theorem nodes from cites
      const thmIds = target.cites || [];
      const nodesC3 = thmIds.map((tid,i) => {
        const t = D.THEOREMS.find(x=>x.id===tid) || D.GATES.find(x=>x.id===tid);
        return { id:tid, label:tid, desc: t? (t.statement||t.claim||'') : '', x: colX[2], y: 60 + i*((r.height-80)/Math.max(1,thmIds.length)) };
      });
      const refIds = target.vars.map(v=>v.refId).filter(Boolean);
      const nodesC4 = refIds.map((cid,i) => {
        const c = D.CONSTANTS.find(x=>x.id===cid) || D.THEOREMS.find(x=>x.id===cid);
        return { id:cid, label: c?.name||cid, val: c?.value||c?.precision||'', x: colX[3], y: 60 + i*((r.height-80)/Math.max(1,refIds.length)) };
      });

      // edges target→vars
      nodesC2.forEach(n => drawEdge(nodesC1[0], n));
      // vars→constants by refId
      nodesC2.forEach(n => {
        const c = nodesC4.find(x => x.id === n.v.refId);
        if (c) drawEdge(n, c);
      });
      // target→theorems
      nodesC3.forEach(n => drawEdge(nodesC1[0], n, true));

      // draw nodes
      [...nodesC1, ...nodesC2, ...nodesC3, ...nodesC4].forEach(n => drawNode(n));

      function drawEdge(a,b,dashed){
        const mx = (a.x+b.x)/2;
        const d = `M ${a.x+80} ${a.y} C ${mx} ${a.y}, ${mx} ${b.y}, ${b.x-6} ${b.y}`;
        svgEl('path', { d, fill:'none', stroke:'var(--rule-hi)','stroke-width':0.8, 'stroke-dasharray': dashed?'3 3':'' , opacity: 0.7 }, svg);
      }
      function drawNode(n){
        const g = svgEl('g', { transform:`translate(${n.x},${n.y})`, style:'cursor:pointer' }, svg);
        g.classList.add('tree-node');
        const w = 140, h = 34;
        svgEl('rect', { x:0, y:-h/2, width:w, height:h, rx:3, fill:'var(--panel)', stroke:'var(--rule-hi)' }, g);
        const l = svgEl('text', { x:8, y:-3, fill:'var(--ink)','font-family':'JetBrains Mono','font-size':11 }, g);
        l.textContent = String(n.label).slice(0,28);
        const d = svgEl('text', { x:8, y:12, fill:'var(--ink-3)','font-family':'JetBrains Mono','font-size':9.5 }, g);
        d.textContent = (n.val||n.desc||'').toString().slice(0,32);
        g.addEventListener('click', () => {
          const data = D.CONSTANTS.find(x=>x.id===n.id)
                    || D.THEOREMS.find(x=>x.id===n.id)
                    || D.GATES.find(x=>x.id===n.id)
                    || D.EQUATIONS.find(x=>x.id===n.id);
          if (data) bus.set({ selected:data, selType: D.CONSTANTS.includes(data)?'constant':D.THEOREMS.includes(data)?'theorem':D.GATES.includes(data)?'gate':'equation' });
        });
      }
    }
    sel.addEventListener('change', () => render(sel.value));
    window.addEventListener('resize', () => render(sel.value));
    render(sel.value || D.EQUATIONS[0].id);
  }

  // =================================================================
  // Inspector (right rail) — reacts to bus.selected
  // Tabbed panels with search — handles 1000s of entries.
  // =================================================================
  function buildInspector(root){
    const tabDefs = [
      { key:'gates',     label:'Gates',       data: D.GATES,             count: (D.GATES||[]).length },
      { key:'constants', label:'Constants',   data: D.CONSTANTS,         count: (D.CONSTANTS||[]).length },
      { key:'theorems',  label:'Theorems',    data: D.THEOREMS,          count: (D.THEOREMS||[]).length },
      { key:'closed',    label:'Closed',      data: D.CLOSED_MECHANISMS, count: (D.CLOSED_MECHANISMS||[]).length },
      { key:'open',      label:'Open',        data: D.OPEN_CHANNELS,     count: (D.OPEN_CHANNELS||[]).length },
      { key:'res',       label:'Researchers', data: D.RESEARCHERS,       count: (D.RESEARCHERS||[]).length },
    ];

    root.innerHTML = `
      <div class="insp-title">Inspector</div>
      <div id="inspBody"></div>
      <div class="insp-tabs" id="inspTabs">
        ${tabDefs.map((t,i) => `<div class="insp-tab${i===0?' active':''}" data-k="${t.key}">${t.label} <span>${t.count}</span></div>`).join('')}
      </div>
      <input type="text" id="inspSearch" class="insp-search" placeholder="filter…"/>
      <div class="insp-list insp-list-scroll" id="inspList"></div>
    `;
    const body = root.querySelector('#inspBody');
    const list = root.querySelector('#inspList');
    const searchInp = root.querySelector('#inspSearch');

    // ── Cross-link footer for inspector cards. Lands at meme-engine.com/research/<type>/<id>
    // ── when the console is served alongside the docs corpus there. Standalone deploys
    // ── without the /research/ surface still render the card; the link just 404s.
    function _archiveLink(type, id, label){
      if (!id) return '';
      const slug = String(id).split('/').map(encodeURIComponent).join('/');
      const text = label || 'View in archive →';
      return `<p class="insp-archive"><a href="/research/${type}/${slug}/" style="color:var(--b1);font-family:'JetBrains Mono';font-size:11px;text-decoration:none;border-bottom:1px dotted currentColor">${text}</a></p>`;
    }
    const tabsEl = root.querySelector('#inspTabs');

    let activeKey = 'gates';

    // Pre-compute the set of constants that have any edge in REAL_EDGES
    // (i.e. are surfable anchors in the fanout view). Used to colorize
    // inspector rows and cards in blue (--b1) so the user can see at a
    // glance which constants are "live" terminals in the graph.
    const _inspEdges = D.REAL_EDGES || [];
    const ANCHOR_CONSTANTS = new Set();
    for (const e of _inspEdges){
      if (e.srcType === 'constants') ANCHOR_CONSTANTS.add(e.src);
      if (e.tgtType === 'constants') ANCHOR_CONSTANTS.add(e.tgt);
    }

    function rowFor(key, item){
      const row = document.createElement('div');
      row.className = 'insp-row';
      let left = '', right = '';
      if (key === 'gates') {
        const v = item.verdict;
        const cls = v==='PASS'?'pass':v==='OPEN'?'open':(v==='DIAGNOSTIC'||v==='HYPOTHESIS')?'diag':'fail';
        left = `<span class="pill ${cls}">${v}</span> <b>${item.id}</b>`;
        right = `S${item.session}`;
        row.dataset.h = `${item.id} ${item.claim||''} ${item.session||''}`.toLowerCase();
        row.addEventListener('click', () => bus.set({ selected:item, selType:'gate' }));
      } else if (key === 'constants') {
        const isAnchor = ANCHOR_CONSTANTS.has(item.id);
        const nameStyle = isAnchor ? ' style="color:var(--b1)"' : '';
        left = `<b${nameStyle}>${item.name}</b> <span class="mono" style="color:var(--accent);margin-left:4px">${item.value}</span>`;
        right = item.tag;
        row.dataset.h = `${item.id} ${item.name} ${item.tag} ${item.note||''}`.toLowerCase();
        if (isAnchor) row.classList.add('insp-anchor-row');
        row.addEventListener('click', () => bus.set({ selected:item, selType:'constant' }));
      } else if (key === 'theorems') {
        left = `<b>${(item.name||item.id).slice(0,52)}</b>`;
        right = item.session;
        row.dataset.h = `${item.id} ${item.name||''} ${item.statement||''}`.toLowerCase();
        row.addEventListener('click', () => bus.set({ selected:item, selType:'theorem' }));
      } else if (key === 'closed') {
        left = `<b>${item.name.slice(0,52)}</b>`;
        right = item.session || '';
        row.dataset.h = `${item.name} ${item.closed_by||''} ${item.gate||''}`.toLowerCase();
        row.addEventListener('click', () => bus.set({ selected:item, selType:'closed' }));
      } else if (key === 'open') {
        left = `<b>${item.name.slice(0,52)}</b>`;
        right = item.session || '';
        row.dataset.h = `${item.name} ${item.detail||''} ${item.status||''}`.toLowerCase();
        row.addEventListener('click', () => bus.set({ selected:item, selType:'open' }));
      } else if (key === 'res') {
        left = `<span class="sw" style="display:inline-block;width:8px;height:8px;background:oklch(0.75 0.14 ${item.hue});border-radius:50%;margin-right:6px"></span><b>${item.label}</b>`;
        right = `${item.cites||''}·`;
        row.dataset.h = `${item.id} ${item.label}`.toLowerCase();
      }
      row.innerHTML = `<div>${left}</div><span>${right}</span>`;
      return row;
    }

    function renderList(){
      const def = tabDefs.find(t => t.key === activeKey);
      const q = searchInp.value.trim().toLowerCase();
      list.innerHTML = '';
      const frag = document.createDocumentFragment();
      let shown = 0;
      for (const item of (def.data || [])){
        const r = rowFor(activeKey, item);
        if (q && !r.dataset.h.includes(q)) continue;
        frag.appendChild(r);
        shown++;
      }
      list.appendChild(frag);
      searchInp.placeholder = `filter ${shown} ${def.label.toLowerCase()}…`;
    }
    tabsEl.addEventListener('click', (e) => {
      const t = e.target.closest('.insp-tab'); if (!t) return;
      activeKey = t.dataset.k;
      tabsEl.querySelectorAll('.insp-tab').forEach(x => x.classList.toggle('active', x===t));
      searchInp.value = '';
      renderList();
    });
    let tmr;
    searchInp.addEventListener('input', () => { clearTimeout(tmr); tmr = setTimeout(renderList, 70); });
    renderList();

    bus.sub(state => {
      const s = state.selected;
      if (!s){ body.innerHTML = `<div class="insp-card"><div class="kicker">Idle</div><p>Click anything — a mode, a variable, a session, a gate — and its provenance lights up here.</p></div>`; return; }
      if (state.selType === 'mode') {
        body.innerHTML = `
          <div class="insp-card">
            <div class="kicker">Dirac mode</div>
            <h3>branch ${s.branch}</h3>
            <p class="val">λ = ${s.val} M_KK</p>
            <p>angular position: ${s.angle}°</p>
            <p style="color:var(--ink-3)">One of 155,984 eigenvalues of D_K on Jensen-deformed SU(3). Click the mute toggle and tap modes to ring them.</p>
          </div>`;
        return;
      }
      if (state.selType === 'constant') {
        // Compute fanout-degree to decide if the card is "surfable".
        // We import-by-reference the same REAL_EDGES the fanout uses, so a
        // constant only gets the surf affordance if it actually has neighbors.
        const _edges = D.REAL_EDGES || [];
        let _deg = 0;
        for (const e of _edges){
          if (e.srcType === 'constants' && e.src === s.id) _deg++;
          if (e.tgtType === 'constants' && e.tgt === s.id) _deg++;
        }
        const surfable = _deg > 0 && typeof window !== 'undefined' && window.AE_SHOW;
        body.innerHTML = `
          <div class="insp-card${surfable ? ' insp-surfable' : ''}"
               style="${surfable ? 'cursor:pointer' : ''}"
               title="${surfable ? 'click → surf to fanout (' + _deg + ' edges)' : ''}">
            <div class="kicker"${surfable ? ' style="color:var(--b1)"' : ''}>Constant · ${s.tag}${surfable ? ' · ' + _deg + ' edges →' : ''}</div>
            <h3${surfable ? ' style="color:var(--b1)"' : ''}>${s.name}</h3>
            <p class="val">${s.value}</p>
            <p>${s.note}</p>
            <p style="color:var(--ink-3);font-family:'JetBrains Mono';font-size:11px">src: ${s.src}</p>
            ${_archiveLink('constants', s.id)}
          </div>`;
        if (surfable) {
          body.querySelector('.insp-card').addEventListener('click', () => {
            // Try in-place animated swap (collapse + expand) if fanout view
            // is already alive on screen. AE_FANOUT_SWAP returns false if
            // its view was torn down (we're on a different tab) — in that
            // case, switch to fanout and let buildFanout do the spin-in.
            if (window.AE_FANOUT_SWAP && window.AE_FANOUT_SWAP(s.id)) return;
            window.AE_FANOUT_ANCHOR = s.id;
            if (window.AE_SHOW) window.AE_SHOW('fanout');
          });
        }
        return;
      }
      if (state.selType === 'theorem') {
        body.innerHTML = `
          <div class="insp-card">
            <div class="kicker">Theorem · ${s.area||''}</div>
            <h3>${s.name}</h3>
            <p>${s.statement||''}</p>
            <p><span class="pill pass">${s.status||'PROVEN'}</span> <span class="pill">Session ${s.session||'—'}</span>${s.precision?`<span class="pill">ε ≤ ${s.precision}</span>`:''}</p>
            ${_archiveLink('theorems', s.id)}
          </div>`;
        return;
      }
      if (state.selType === 'gate') {
        const cls = s.verdict==='PASS'?'pass':s.verdict==='OPEN'?'open':s.verdict==='DIAGNOSTIC'?'diag':'fail';
        body.innerHTML = `
          <div class="insp-card">
            <div class="kicker">Gate</div>
            <h3>${s.id}</h3>
            <p>${s.claim}</p>
            <p><span class="pill ${cls}">${s.verdict}</span> <span class="pill">Session ${s.session}</span></p>
            ${_archiveLink('gates', s.id)}
          </div>`;
        return;
      }
      if (state.selType === 'equation') {
        const el = document.createElement('div');
        el.className = 'insp-card';
        el.innerHTML = `
          <div class="kicker">Equation · ${s.tier}</div>
          <h3>${s.title}</h3>
          <div class="tex-render" style="font-size:15px;margin:6px 0"></div>
          <p>${s.story}</p>
          <p>${(s.cites||[]).map(c=>`<span class="pill">${c}</span>`).join('')}</p>
        `;
        body.innerHTML = '';
        body.appendChild(el);
        renderTex(el.querySelector('.tex-render'), s.tex);
        return;
      }
      if (state.selType === 'session') {
        body.innerHTML = `
          <div class="insp-card">
            <div class="kicker">Session · ${s.area}</div>
            <h3>${s.id} — ${s.label}</h3>
            <p>conditional probability: <span class="val">${(s.p*100).toFixed(0)}%</span></p>
            ${_archiveLink('sessions', s.id)}
          </div>`;
        return;
      }
      if (state.selType === 'closed') {
        body.innerHTML = `
          <div class="insp-card">
            <div class="kicker">Closed mechanism · Session ${s.session||'—'}</div>
            <h3>${s.name}</h3>
            ${s.closed_by ? `<p><b style="color:var(--ink)">closed by:</b> ${s.closed_by}</p>` : ''}
            ${s.gate ? `<p><span class="pill">Gate ${s.gate}</span></p>` : ''}
            ${_archiveLink('mechanisms', s.id)}
          </div>`;
        return;
      }
      if (state.selType === 'open') {
        body.innerHTML = `
          <div class="insp-card">
            <div class="kicker">Open channel · Session ${s.session||'—'}</div>
            <h3>${s.name}</h3>
            ${s.detail ? `<p>${s.detail}</p>` : ''}
            ${s.status ? `<p><b style="color:var(--ink)">status:</b> ${s.status}</p>` : ''}
          </div>`;
        return;
      }
    });
  }

  // =================================================================
  // Probability trajectory (bottom strip)
  // =================================================================
  function buildTrajectory(root){
    root.innerHTML = `
      <div class="title">Probability trajectory · conditional on φ from Dirac spectrum</div>
      <svg id="trajSvg" width="100%" height="140"></svg>
    `;
    const svg = root.querySelector('#trajSvg');
    function render(){
      const r = svg.getBoundingClientRect();
      svg.setAttribute('viewBox',`0 0 ${r.width} 140`);
      clearChildren(svg);
      const pad = 40;
      const w = r.width - pad*2, h = 100;
      const data = D.TRAJECTORY;
      const maxP = 0.45;
      const x = i => pad + (i/(data.length-1)) * w;
      const y = p => 120 - (p / maxP) * h;

      // grid
      [0.1, 0.2, 0.3, 0.4].forEach(g => {
        svgEl('line', { x1:pad, x2:pad+w, y1:y(g), y2:y(g), stroke:'#181c24','stroke-width':0.6 }, svg);
        const t = svgEl('text', { x:pad-8, y:y(g)+3, fill:'var(--ink-3)','font-family':'JetBrains Mono','font-size':9,'text-anchor':'end' }, svg);
        t.textContent = (g*100).toFixed(0)+'%';
      });

      const path = 'M '+data.map((d,i)=>`${x(i)},${y(d.p)}`).join(' L ');
      svgEl('path', { d:path, fill:'none', stroke:'var(--accent)', 'stroke-width':1.4 }, svg);
      data.forEach((d,i) => {
        const g = svgEl('g', { transform:`translate(${x(i)},${y(d.p)})`, style:'cursor:pointer' }, svg);
        svgEl('circle', { r:3, fill:'var(--accent)' }, g);
        if (i % 3 === 0 || i===data.length-1){
          const t = svgEl('text', { x:0, y:16, fill:'var(--ink-3)','font-family':'JetBrains Mono','font-size':9,'text-anchor':'middle' }, svg);
          t.textContent = d.label;
        }
        g.addEventListener('click', () => {
          const s = D.SESSIONS.find(x=>x.id===d.label);
          if (s) bus.set({ selected:s, selType:'session' });
        });
      });

      // annotations
      svgEl('text', {
        x: x(data.length-1), y: y(data[data.length-1].p)-8,
        fill:'var(--accent)','font-family':'JetBrains Mono','font-size':10, 'text-anchor':'end'
      }, svg).textContent = `now · ${(data[data.length-1].p*100).toFixed(0)}%`;
    }
    window.addEventListener('resize', render);
    render();
  }

  // =================================================================
  // Wordmap (tiny equation-symbol cloud)
  // =================================================================
  function buildWordmap(root){
    root.innerHTML = `
      <div class="title">Equation wordmap · click to filter</div>
      <div id="wordCloud"></div>
    `;
    const cloud = root.querySelector('#wordCloud');
    // tokenise equation TeX
    const freq = new Map();
    const TOKEN_RE = /\\[A-Za-z]+|[A-Za-z_][A-Za-z0-9_]*|\d+\.\d+|[=+\-*/^]/g;
    D.EQUATIONS.forEach(e => {
      (e.tex.match(TOKEN_RE)||[]).forEach(t => {
        if (/^(mathrm|diag|frac|operatorname|text|cdot|times|Rightarrow|sqrt|left|right)$/.test(t.replace('\\',''))) return;
        freq.set(t, (freq.get(t)||0)+1);
      });
    });
    const sorted = [...freq.entries()].sort((a,b)=>b[1]-a[1]).slice(0, 44);
    sorted.forEach(([tok,c]) => {
      const size = 11 + Math.min(8, c*1.5);
      const span = document.createElement('span');
      span.className = 'wordtag';
      span.style.fontSize = size+'px';
      span.textContent = tok;
      span.addEventListener('click', () => {
        // find which equations use this token; pick the first as the selection
        const eq = D.EQUATIONS.find(e => (e.tex.match(TOKEN_RE)||[]).includes(tok));
        if (eq) bus.set({ selected:eq, selType:'equation' });
        document.querySelectorAll('.wordtag').forEach(s=>s.classList.remove('active'));
        span.classList.add('active');
      });
      cloud.appendChild(span);
    });
  }

  // =================================================================
  // View 6 — Provenance fan-out (radial graph anchored on a constant)
  // Center node = anchor constant. Ring 1 = direct neighbors via REAL_EDGES.
  // Ring 2 = neighbors-of-neighbors (forward chain). Edge color by edge type.
  // =================================================================
  function buildFanout(root){
    // Edge-type → color (S86 user-curated palette: Brown/White/Slate/Red).
    // Unspecified types follow existing groupings: cross_validates → Brown
    // (with reproduces/confirms), grounds → White (with depends_on/derived_from),
    // feeds_into + implies → Slate (with bounds/enables), closed_by + supersedes
    // stay at accent (special closure events).
    const TYPE_COLOR = {
      reproduces:      'var(--edge-reproduces)',  // brown
      depends_on:      'var(--edge-depends)',     // white
      derived_from:    'var(--edge-depends)',     // white
      grounds:         'var(--edge-depends)',     // white
      confirms:        'var(--edge-reproduces)',  // brown
      cross_validates: 'var(--edge-reproduces)',  // brown
      bounds:          'var(--edge-bounds)',      // slate
      feeds_into:      'var(--edge-bounds)',      // slate
      enables:         'var(--edge-bounds)',      // slate
      implies:         'var(--edge-bounds)',      // slate
      closed_by:       'var(--accent)',           // brass — special closure
      supersedes:      'var(--accent)',           // brass — special closure
      refutes:         'var(--edge-refutes)',     // red
    };
    // Node type → fill (visual hierarchy: anchor brass, gates panel-hi, theorems b1, etc.)
    const NODE_FILL = {
      anchor:           'var(--accent)',
      constants:        'var(--panel-hi)',
      gates:            'var(--b2)',
      theorems:         'var(--b1)',
      closed_mechanisms:'var(--b3)',
      open_channels:    'var(--gate-open)',
      data_provenance:  'var(--ink-3)',
      sessions:         'var(--rule-hi)',
      classes:          'var(--accent)',  // class supernode shares anchor brass
    };
    function nodeFill(type){ return NODE_FILL[type] || 'var(--panel)'; }

    // Role → fill (S86; class-anchor mode only — used to color ring-1 member
    // nodes by the role they play in the anchored class). Maps the 7-axis
    // canonical_classes.py taxonomy onto the user-curated role palette.
    const ROLE_COLOR = {
      PRIMARY:           'var(--role-primary)',            // blue
      PRECONDITION:      'var(--role-precondition)',       // indigo
      EMERGENT_FROM:     'var(--role-emergent_from)',      // violet
      CONSEQUENCE:       'var(--role-consequence)',        // green
      OBSERVABLE_OUTPUT: 'var(--role-observable_output)',  // yellow
      DERIVED:           'var(--role-derived)',            // deep-orange
      RELATED:           'var(--role-related)',            // teal
    };

    // Build degree map across REAL_EDGES so the constants dropdown can rank.
    const edges = D.REAL_EDGES || [];
    const classEdges = D.CLASS_EDGES || [];
    const classes = D.CLASSES || [];
    const constantDegree = new Map();
    for (const e of edges){
      if (e.srcType === 'constants') constantDegree.set(e.src, (constantDegree.get(e.src)||0) + 1);
      if (e.tgtType === 'constants') constantDegree.set(e.tgt, (constantDegree.get(e.tgt)||0) + 1);
    }
    // Build a name→display map from CONSTANTS so dropdown shows pretty names.
    const constName = new Map((D.CONSTANTS||[]).map(c => [c.id, c.name || c.id]));
    // Class id → metadata map (for fast lookup in render branching).
    const classById = new Map(classes.map(c => [c.id, c]));
    // Class candidates ranked by member count (descending). Sub-classes are
    // marked so the dropdown can indent them visually.
    const classCandidates = [...classes]
      .sort((a, b) => (b.members_count || 0) - (a.members_count || 0));
    // Ranked constant candidates (only those that actually have edges).
    const candidates = [...constantDegree.entries()]
      .filter(([id]) => true)
      .sort((a, b) => b[1] - a[1]);
    // Default anchor: prefer CC_ratio (legible + well-populated) when present;
    // otherwise fall back to the highest-degree candidate.
    const PREFERRED_DEFAULT = 'CC_ratio';
    const fallbackId = constantDegree.has(PREFERRED_DEFAULT)
      ? PREFERRED_DEFAULT
      : (candidates.length ? candidates[0][0] : ((D.CONSTANTS||[])[0]?.id || ''));

    // True iff anchorId names a class (used to branch render mode).
    function isClassAnchor(id){ return classById.has(id); }

    root.innerHTML = `
      <div class="controls">
        <label>anchor</label>
        <select id="fanAnchor" style="background:var(--panel);color:var(--ink);border:1px solid var(--rule);padding:4px 8px;font-family:'JetBrains Mono';font-size:12px;min-width:280px">
          ${classCandidates.length ? `<optgroup label="▣ classes">${classCandidates.map(c => {
            const indent = (c.tier || 0) > 0 ? '  └─ ' : '';
            const n = c.members_count || 0;
            const label = (c.name || c.id || '').slice(0, 38);
            return `<option value="${c.id}">${indent}${label} · ${n} member${n===1?'':'s'}</option>`;
          }).join('')}</optgroup>` : ''}
          ${candidates.length ? `<optgroup label="○ constants">${candidates.map(([id, n]) =>
            `<option value="${id}">${(constName.get(id)||id).slice(0,32)} · ${n} edge${n===1?'':'s'}</option>`
          ).join('')}</optgroup>` : ''}
        </select>
        <button id="fanReset">reset</button>
      </div>
      <div class="legend">
        <div>${edges.length} typed edges in REAL_EDGES · ${classEdges.length} class edges</div>
        <div style="color:var(--ink-3);margin-top:4px">center → ring 1 (direct) → ring 2 (chain) · class anchors show members by role</div>
        <div style="margin-top:6px">
          <div style="color:var(--ink-3);font-size:10px;margin-bottom:2px">edge types</div>
          <span class="sw" style="background:var(--edge-reproduces)"></span>reproduces / confirms
          <br><span class="sw" style="background:var(--edge-depends)"></span>depends_on / derived_from
          <br><span class="sw" style="background:var(--edge-bounds)"></span>bounds / enables
          <br><span class="sw" style="background:var(--edge-refutes)"></span>refutes
          <div style="color:var(--ink-3);font-size:10px;margin-top:8px;margin-bottom:2px">class roles</div>
          <span class="sw" style="background:var(--role-primary)"></span>PRIMARY
          <br><span class="sw" style="background:var(--role-precondition)"></span>PRECONDITION
          <br><span class="sw" style="background:var(--role-emergent_from)"></span>EMERGENT_FROM
          <br><span class="sw" style="background:var(--role-consequence)"></span>CONSEQUENCE
          <br><span class="sw" style="background:var(--role-observable_output)"></span>OBSERVABLE_OUTPUT
          <br><span class="sw" style="background:var(--role-derived)"></span>DERIVED
          <br><span class="sw" style="background:var(--role-related)"></span>RELATED
        </div>
      </div>
      <svg id="fanSvg" width="100%" height="100%" class="grid-bg"></svg>
    `;

    const svg = root.querySelector('#fanSvg');
    const sel = root.querySelector('#fanAnchor');
    const resetBtn = root.querySelector('#fanReset');

    function findEntity(type, id){
      if (type === 'constants')         return (D.CONSTANTS||[]).find(x => x.id === id);
      if (type === 'gates')             return (D.GATES||[]).find(x => x.id === id);
      if (type === 'theorems')          return (D.THEOREMS||[]).find(x => x.id === id);
      if (type === 'closed_mechanisms') return (D.CLOSED_MECHANISMS||[]).find(x => x.id === id);
      if (type === 'open_channels')     return (D.OPEN_CHANNELS||[]).find(x => x.id === id);
      if (type === 'classes')           return classById.get(id);  // S86: class anchor support
      return null;
    }
    function selTypeFor(type){
      return ({
        constants: 'constant', gates: 'gate', theorems: 'theorem',
        closed_mechanisms: 'closed', open_channels: 'open',
        classes: 'class',  // S86: inspector receives 'class' selType for class clicks
      })[type] || null;
    }
    function nodeLabel(type, id){
      if (type === 'constants') return constName.get(id) || id;
      const ent = findEntity(type, id);
      if (ent) return (ent.name || ent.id || id);
      return id;
    }

    function viewBox(){
      const r = svg.getBoundingClientRect();
      svg.setAttribute('viewBox', `0 0 ${r.width} ${r.height}`);
      return r;
    }

    // Pan/zoom state — persists across anchor changes within this view.
    const view = { tx: 0, ty: 0, scale: 1 };
    function applyTransform(){
      const w = svg.querySelector('g.fanWorld');
      if (w) w.setAttribute('transform',
        `translate(${view.tx} ${view.ty}) scale(${view.scale})`);

      // Counter-scale labels so font stays at fixed pixel size and the
      // (lx, ly) offset from the node center stays at fixed pixel distance.
      // Math: text is at (lx, ly) inside a g translate(p.x,p.y) inside world
      // scale(s). World scales position by s; text's own scale(1/s) cancels
      // the world scale on the text glyphs only. Net screen offset from node:
      //   ((lx, ly) * (1/s)) * s  =  (lx, ly).  ✓ pixel-stable.
      const inv = 1 / view.scale;
      const labels = svg.querySelectorAll('.fanout-label');
      for (const t of labels){
        t.setAttribute('transform', `scale(${inv})`);
      }

      // Declutter at low zoom — ring-2 labels disappear below scale 1.0,
      // ring-1 labels disappear below 0.55. Anchor label always visible.
      const showR1 = view.scale > 0.55;
      const showR2 = view.scale > 1.00;
      for (const t of svg.querySelectorAll('.fanout-label-r1')){
        t.style.display = showR1 ? '' : 'none';
      }
      for (const t of svg.querySelectorAll('.fanout-label-r2')){
        t.style.display = showR2 ? '' : 'none';
      }
    }

    function render(anchorId, opts = {}){
      clearChildren(svg);
      const world = svgEl('g', { class: 'fanWorld' }, svg);
      applyTransform();
      const { width, height } = viewBox();
      const cx = width / 2, cy = height / 2;
      // fanContent holds rings + edges + neighbor nodes. Anchor stays directly
      // in `world` so the collapse/expand animation visually emanates from a
      // stationary center.
      const fanContent = svgEl('g', { class: 'fanContent' }, world);
      // Animation is driven per-leaf by applyT() — fanContent is a passive
      // container, no group transform. Each node carries its home (x,y) as
      // data attributes; each edge carries its two endpoints. applyT(t)
      // interpolates every node + edge between center (t=0) and home (t=1)
      // with a slight spiral twist for "string-pull" feel.
      const r1 = Math.min(width, height) * 0.22;
      const r2 = Math.min(width, height) * 0.40;

      // S86: class-anchor mode. When anchorId names a class, ring 1 = its
      // member constants from CLASS_EDGES (color-coded by role downstream)
      // and ring 2 is skipped (members alone are 7-34 nodes; ring 2 would
      // explode visually and drown the role-coloring). Constant-anchor
      // mode keeps the original two-ring REAL_EDGES path.
      const classMode = isClassAnchor(anchorId);

      // Ring 1: every edge that touches the anchor.
      const ring1 = [];
      if (classMode){
        // Class anchor — contains-edges from CLASS_EDGES.
        for (const ce of classEdges){
          if (ce.type === 'contains' && ce.src === anchorId && ce.tgtType === 'constants'){
            ring1.push({ neighborType: ce.tgtType, neighborId: ce.tgt, edge: ce, dir: 'out' });
          }
        }
      } else {
        // Constant anchor — REAL_EDGES (direction-agnostic).
        for (const e of edges){
          if (e.tgt === anchorId && e.tgtType === 'constants'){
            ring1.push({ neighborType: e.srcType, neighborId: e.src, edge: e, dir: 'in' });
          } else if (e.src === anchorId && e.srcType === 'constants'){
            ring1.push({ neighborType: e.tgtType, neighborId: e.tgt, edge: e, dir: 'out' });
          }
        }
      }
      // Ring 2: forward-chain (constant-anchor only — skipped for classes).
      const ring2 = [];
      if (!classMode){
        const seen = new Set([`constants::${anchorId}`, ...ring1.map(n => `${n.neighborType}::${n.neighborId}`)]);
        for (const n of ring1){
          for (const e of edges){
            if (e.src === n.neighborId && e.srcType === n.neighborType){
              const k = `${e.tgtType}::${e.tgt}`;
              if (seen.has(k)) continue;
              seen.add(k);
              ring2.push({ parent: n, neighborType: e.tgtType, neighborId: e.tgt, edge: e, dir: 'out' });
            }
            if (e.tgt === n.neighborId && e.tgtType === n.neighborType){
              const k = `${e.srcType}::${e.src}`;
              if (seen.has(k)) continue;
              seen.add(k);
              ring2.push({ parent: n, neighborType: e.srcType, neighborId: e.src, edge: e, dir: 'in' });
            }
          }
        }
      }

      // ring circles
      for (const r of [r1, r2]){
        svgEl('circle', { cx, cy, r, fill:'none', stroke:'#1a1f29', 'stroke-width':0.6, 'stroke-dasharray':'2 4' }, fanContent);
      }

      // place ring-1 nodes evenly around the circle
      const ring1Pos = new Map();
      const N1 = Math.max(ring1.length, 1);
      ring1.forEach((n, i) => {
        const ang = (i / N1) * 2*Math.PI - Math.PI/2;
        ring1Pos.set(`${n.neighborType}::${n.neighborId}`, {
          x: cx + r1 * Math.cos(ang), y: cy + r1 * Math.sin(ang), ang, n,
        });
      });

      // ring-2 nodes orbit around their ring-1 parent; spread by sibling count
      const ring2Pos = new Map();
      const childrenByParent = new Map();
      for (const c of ring2){
        const k = `${c.parent.neighborType}::${c.parent.neighborId}`;
        if (!childrenByParent.has(k)) childrenByParent.set(k, []);
        childrenByParent.get(k).push(c);
      }
      for (const [pk, children] of childrenByParent){
        const parent = ring1Pos.get(pk);
        if (!parent) continue;
        const span = Math.PI / 4; // ±22.5° around the parent's angle
        children.forEach((c, i) => {
          const t = children.length === 1 ? 0 : (i / (children.length - 1) - 0.5);
          const ang = parent.ang + t * span;
          ring2Pos.set(`${c.neighborType}::${c.neighborId}`, {
            x: cx + r2 * Math.cos(ang), y: cy + r2 * Math.sin(ang), ang, c,
          });
        });
      }

      // edges first (so nodes overdraw)
      function drawEdge(ax, ay, bx, by, type, comment, srcLag, tgtLag){
        const mx = (ax + bx) / 2, my = (ay + by) / 2;
        // gentle curve toward the midpoint nudged perpendicular to the chord
        const dx = bx - ax, dy = by - ay;
        const len = Math.sqrt(dx*dx + dy*dy) || 1;
        const nx = -dy / len, ny = dx / len;
        const bend = Math.min(28, len * 0.12);
        const path = svgEl('path', {
          d: `M ${ax} ${ay} Q ${mx + nx*bend} ${my + ny*bend} ${bx} ${by}`,
          fill: 'none',
          stroke: TYPE_COLOR[type] || 'var(--rule-hi)',
          'stroke-width': 1,
          opacity: 0.55,
          'data-edge-ax': ax, 'data-edge-ay': ay,
          'data-edge-bx': bx, 'data-edge-by': by,
          'data-src-lag': srcLag != null ? srcLag : 0,
          'data-tgt-lag': tgtLag != null ? tgtLag : 0,
        }, fanContent);
        if (comment){
          const title = svgEl('title', {}, path);
          title.textContent = `[${type}] ${comment}`;
        }
      }

      // anchor → ring 1
      for (const [, p] of ring1Pos){
        drawEdge(cx, cy, p.x, p.y, p.n.edge.type, p.n.edge.comment, 0, 0.30);  // anchor → ring1
      }
      // ring 1 → ring 2
      for (const [, p] of ring2Pos){
        const pk = `${p.c.parent.neighborType}::${p.c.parent.neighborId}`;
        const parent = ring1Pos.get(pk);
        if (!parent) continue;
        drawEdge(parent.x, parent.y, p.x, p.y, p.c.edge.type, p.c.edge.comment, 0.30, 1.00);  // ring1 → ring2
      }

      // anchor node — class supernode (radius 10) or constant anchor (radius 8).
      // Both carry a `name` field, so the label expression is unchanged.
      const anchorEnt = findEntity(classMode ? 'classes' : 'constants', anchorId);
      const anchorG = svgEl('g', { transform:`translate(${cx},${cy})`, style:'cursor:pointer' }, world);
      anchorG.classList.add('tree-node');
      svgEl('circle', { r: classMode ? 10 : 8, fill: nodeFill('anchor'), stroke:'var(--rule-hi)', 'stroke-width':1 }, anchorG);
      const at = svgEl('text', { x: 0, y: -16, fill:'var(--b1)', 'font-family':'JetBrains Mono','font-size':14, 'font-weight':600, 'text-anchor':'middle', class:'fanout-label fanout-label-anchor' }, anchorG);
      at.textContent = (anchorEnt?.name || anchorId);
      anchorG.addEventListener('click', () => {
        if (anchorEnt) bus.set({ selected: anchorEnt, selType: classMode ? 'class' : 'constant' });
      });

      // ring nodes (1 + 2 share the same drawing logic)
      function drawNode(p, ringIdx){
        const type = ringIdx === 1 ? p.n.neighborType : p.c.neighborType;
        const id   = ringIdx === 1 ? p.n.neighborId   : p.c.neighborId;
        // S86: class-anchor mode colors ring-1 nodes by role from the
        // CLASS_EDGES entry (`p.n.edge.role`); falls back to nodeFill(type)
        // for unknown roles or any constant-anchor node. Ring 2 is empty
        // in classMode (see Edit 3b-i), so ringIdx===2 always uses nodeFill.
        const role = (ringIdx === 1 && p.n && p.n.edge) ? p.n.edge.role : null;
        const fill = (classMode && role && ROLE_COLOR[role])
          ? ROLE_COLOR[role]
          : nodeFill(type);
        const g = svgEl('g', {
          transform:`translate(${p.x},${p.y})`,
          style:'cursor:pointer',
          'data-home-x': p.x, 'data-home-y': p.y,
          'data-lag': ringIdx === 1 ? 0.30 : 1.00,  // ring-2 is the whip tip
        }, fanContent);
        g.classList.add('tree-node');
        svgEl('circle', { r: ringIdx===1 ? 6 : 4, fill, stroke:'var(--rule)', 'stroke-width':0.8 }, g);
        // label outside the ring (radially)
        const labelDist = ringIdx === 1 ? 12 : 9;
        const lx = (p.x - cx) === 0 && (p.y - cy) === 0 ? labelDist : Math.cos(p.ang) * labelDist;
        const ly = (p.x - cx) === 0 && (p.y - cy) === 0 ? 4 : Math.sin(p.ang) * labelDist + 3;
        const isConst = (type === 'constants');
        const t = svgEl('text', {
          x: lx, y: ly,
          fill: isConst ? 'var(--b1)' : 'var(--ink-2)',
          'font-family':'JetBrains Mono',
          'font-size': ringIdx===1 ? 12 : 11,
          'font-weight': isConst ? 600 : 400,
          'text-anchor': p.ang > Math.PI/2 || p.ang < -Math.PI/2 ? 'end' : 'start',
          class: ringIdx === 1 ? 'fanout-label fanout-label-r1' : 'fanout-label fanout-label-r2',
        }, g);
        t.textContent = String(nodeLabel(type, id)).slice(0, ringIdx===1 ? 28 : 22);
        g.addEventListener('click', (e) => {
          e.stopPropagation();
          const ent = findEntity(type, id);
          const st = selTypeFor(type);
          if (ent && st) bus.set({ selected: ent, selType: st });
        });
      }
      for (const [, p] of ring1Pos) drawNode(p, 1);
      for (const [, p] of ring2Pos) drawNode(p, 2);

      // header text: anchor + degree summary (class mode shows role breakdown)
      const summaryY = 22;
      const hdr = svgEl('text', {
        x: 16, y: height - 14, fill:'var(--ink-3)',
        'font-family':'JetBrains Mono','font-size':10,
      }, svg);
      if (classMode){
        const roleCounts = {};
        for (const r of ring1){
          const role = (r.edge && r.edge.role) || 'UNKNOWN';
          roleCounts[role] = (roleCounts[role] || 0) + 1;
        }
        const roleStr = Object.entries(roleCounts)
          .sort((a, b) => b[1] - a[1])
          .map(([r, c]) => `${r}=${c}`)
          .join(' · ');
        hdr.textContent = `class: ${anchorId}  ·  members: ${ring1.length}  ·  ${roleStr || 'no members'}  ·  ${ring1.length === 0 ? 'pick another class' : 'click any member → constant view'}`;
      } else {
        hdr.textContent = `anchor: ${anchorId}  ·  ring 1: ${ring1.length}  ·  ring 2: ${ring2.length}  ·  ${ring1.length + ring2.length === 0 ? 'no edges — pick another constant' : 'click any node → inspector'}`;
      }

      // Seed collapsed geometry synchronously before paint, so animateExpand
      // starts from t=0 instead of flashing the home layout for one frame.
      // Mode='expand', t_phase=0 → all elements at center.
      if (opts.collapsedStart && typeof applyT === 'function') applyT(0, 'expand', -1);
    }

    // ---- Anchor swap animation: per-string interpolation with spiral twist ----
    //
    // Phase 1 (collapse, 600ms easeInCubic — gravity-pull):
    //   each ring node + edge endpoint slides from home → center along a
    //   spiral arc; t goes 1 → 0 with t³ easing so motion is slow at first
    //   and accelerates as it nears the center (gravity feel).
    //
    // Phase 2 (render new anchor; applyT(0) seeds inline geometry to prevent
    //   pre-animation flash).
    //
    // Phase 3 (expand, 1100ms easeOutCubic — drag-decel):
    //   from collapsed cluster at center, every endpoint flings outward;
    //   t goes 0 → 1 with 1−(1−t)³ easing so motion is fast at first and
    //   decelerates as endpoints approach their new home positions (drag).
    //
    // The spiral comes from rotating each home offset by (1−t)·TWIST_MAX
    // before scaling by t. Each string therefore traces its own arc rather
    // than the whole group rotating uniformly.
    const TWIST_MAX = Math.PI / 4;   // ~45° wind-up at full collapse
    const LAG_SPAN = 0.40;           // outer strings start LAG_SPAN later
    const MOTION_BEND_K = 0.22;      // extra path-bow during transit (peaks at t=0.5)
    const NODE_LAG_R1 = 0.30;        // ring-1 nodes wait this long before joining
    const NODE_LAG_R2 = 1.00;        // ring-2 nodes are the tip of the whip
    // Easing curves chosen for physical feel:
    //  - easeInQuad (t²): "gravity pull" — visible motion throughout, accel
    //    builds to a plunge at the end. Cubic was too backloaded.
    //  - easeOutCubic (1−(1−t)³): "drag deceleration" — fast fling on
    //    release, slow approach to rest.
    function easeInQuad(k){ return k*k; }
    function easeOutCubic(k){ return 1 - Math.pow(1-k, 3); }

    // applyT: drives every leaf element's geometry from a single phase
    // progress value. Behaviors:
    //   • per-element lag — outer strings (ring-2, lag=1.0) start later than
    //     inner (ring-1, lag=0.3) than anchor edges (lag=0.3). Whip cascade.
    //   • motion-bow — each string adds extra perpendicular bend = sin(π·t)
    //     × len × K, peaking at mid-transit and zero at rest. Strings bow
    //     under their own motion instead of staying chord-straight.
    //   • spiral twist — (1−t)·TWIST_MAX·twistSign. CW in both phases via
    //     opposite signs (see animateCollapse/Expand).
    //
    // Args:
    //   t_phase ∈ [0, 1]  — linear phase progress (0=phase start, 1=end)
    //   mode    ∈ {'collapse','expand'} — direction (mode controls which way
    //     the per-element t_local sweeps)
    //   twistSign ∈ {±1} — visual rotation direction
    function applyT(t_phase, mode, twistSign = +1){
      const fc = svg.querySelector('g.fanContent');
      if (!fc) return;
      const r = svg.getBoundingClientRect();
      const cx2 = r.width / 2, cy2 = r.height / 2;
      const isExpand = (mode === 'expand');

      // lagMap: convert (t_phase, lag) → t_local ∈ [0, 1]
      // Element with lag=0 follows t_phase directly. Element with lag=1
      // waits until t_phase ≥ LAG_SPAN, then ramps to 1.
      // For collapse (t_local goes 1→0 over the phase), invert.
      const lagMap = (lag) => {
        const t_lagged = Math.max(0, Math.min(1,
          (t_phase - lag * LAG_SPAN) / (1 - LAG_SPAN)));
        return isExpand ? t_lagged : 1 - t_lagged;
      };

      for (const n of fc.querySelectorAll('g[data-home-x]')){
        const lag = +n.dataset.lag || 0;
        const t = lagMap(lag);
        const twist = (1 - t) * TWIST_MAX * twistSign;
        const cT = Math.cos(twist), sT = Math.sin(twist);
        const dx = (+n.dataset.homeX) - cx2, dy = (+n.dataset.homeY) - cy2;
        const rx = dx * cT - dy * sT;
        const ry = dx * sT + dy * cT;
        n.setAttribute('transform', `translate(${cx2 + rx*t},${cy2 + ry*t})`);
      }

      for (const e of fc.querySelectorAll('path[data-edge-ax]')){
        // Per-endpoint lag: each endpoint follows its own node's cascade.
        // Without this, ring1→ring2 edges would scale both endpoints with
        // the slower (ring2) lag, detaching the source end from the actual
        // ring1 node which is using the faster (ring1) lag.
        const sLag = +e.dataset.srcLag || 0;
        const tLag = +e.dataset.tgtLag || 0;
        const tA = lagMap(sLag);
        const tB = lagMap(tLag);
        const twA = (1 - tA) * TWIST_MAX * twistSign;
        const twB = (1 - tB) * TWIST_MAX * twistSign;
        const cTA = Math.cos(twA), sTA = Math.sin(twA);
        const cTB = Math.cos(twB), sTB = Math.sin(twB);
        const ax = +e.dataset.edgeAx, ay = +e.dataset.edgeAy;
        const bx = +e.dataset.edgeBx, by = +e.dataset.edgeBy;
        const aDx = ax - cx2, aDy = ay - cy2;
        const bDx = bx - cx2, bDy = by - cy2;
        const aRx = aDx*cTA - aDy*sTA, aRy = aDx*sTA + aDy*cTA;
        const bRx = bDx*cTB - bDy*sTB, bRy = bDx*sTB + bDy*cTB;
        const aX = cx2 + aRx*tA, aY = cy2 + aRy*tA;
        const bX = cx2 + bRx*tB, bY = cy2 + bRy*tB;
        const mx = (aX+bX)/2, my = (aY+bY)/2;
        const dx = bX-aX, dy = bY-aY;
        const len = Math.sqrt(dx*dx + dy*dy) || 1;
        const nx = -dy/len, ny = dx/len;
        // Motion-bow: peak when at least one endpoint is mid-transit.
        // Use max of the two endpoint motion contributions so the bow stays
        // visible while either end is moving.
        const motion = Math.max(Math.sin(Math.PI * tA), Math.sin(Math.PI * tB));
        const bend = Math.min(28, len * 0.12) + len * MOTION_BEND_K * motion;
        e.setAttribute('d', `M ${aX} ${aY} Q ${mx + nx*bend} ${my + ny*bend} ${bX} ${bY}`);
      }

      // Each label's opacity follows its parent node's t_local — so labels
      // fade in/out in cascade with the nodes they attach to.
      for (const lbl of fc.querySelectorAll('.fanout-label')){
        const par = lbl.closest('[data-lag]');
        if (par){
          const lag = +par.dataset.lag || 0;
          lbl.style.opacity = String(Math.max(0, lagMap(lag)));
        }
      }
    }

    function animateString(duration, easing, mode, twistSign){
      return new Promise(resolve => {
        if (!svg.querySelector('g.fanContent')){ resolve(); return; }
        applyT(0, mode, twistSign);  // seed initial state — prevents pre-paint flash
        const start = performance.now();
        function frame(now){
          const k = Math.min(1, (now - start) / duration);
          const eased = easing(k);
          applyT(eased, mode, twistSign);
          if (k < 1) requestAnimationFrame(frame);
          else resolve();
        }
        requestAnimationFrame(frame);
      });
    }
    function animateCollapse(){ return animateString( 900, easeInQuad,   'collapse', +1); }
    function animateExpand()  { return animateString(1200, easeOutCubic, 'expand',   -1); }

    let swapping = false;
    async function animateSwap(newAnchorId){
      if (swapping) return;
      swapping = true;
      try {
        if (svg.querySelector('g.fanContent')) await animateCollapse();
        view.tx = 0; view.ty = 0; view.scale = 1;
        render(newAnchorId, { collapsedStart: true });
        await animateExpand();
      } finally {
        swapping = false;
      }
    }

    sel.addEventListener('change', () => animateSwap(sel.value));
    resetBtn.addEventListener('click', () => {
      view.tx = 0; view.ty = 0; view.scale = 1;
      sel.value = fallbackId; render(fallbackId);  // reset is a snap, no twist
    });
    window.addEventListener('resize', () => render(sel.value));

    // ---- Scroll-zoom (anchored on cursor) + drag-to-pan ----
    svg.style.cursor = 'grab';
    svg.addEventListener('wheel', (ev) => {
      ev.preventDefault();
      const r = svg.getBoundingClientRect();
      const px = ev.clientX - r.left;
      const py = ev.clientY - r.top;
      const factor = ev.deltaY < 0 ? 1.15 : (1 / 1.15);
      const newScale = Math.max(0.2, Math.min(8, view.scale * factor));
      // keep the world point under the cursor stationary across zoom
      view.tx = px - (px - view.tx) * (newScale / view.scale);
      view.ty = py - (py - view.ty) * (newScale / view.scale);
      view.scale = newScale;
      applyTransform();
    }, { passive: false });

    let panning = false; let lastX = 0; let lastY = 0;
    svg.addEventListener('mousedown', (ev) => {
      // Don't pan if mousedown is on a node — let the click handler fire.
      if (ev.target.closest('.tree-node')) return;
      panning = true; lastX = ev.clientX; lastY = ev.clientY;
      svg.style.cursor = 'grabbing';
      ev.preventDefault();
    });
    window.addEventListener('mousemove', (ev) => {
      if (!panning) return;
      view.tx += ev.clientX - lastX;
      view.ty += ev.clientY - lastY;
      lastX = ev.clientX; lastY = ev.clientY;
      applyTransform();
    });
    window.addEventListener('mouseup', () => {
      if (!panning) return;
      panning = false;
      svg.style.cursor = 'grab';
    });

    // Honor a global anchor hint (set by the inspector's "surf" click) so
    // the fanout opens centered on whatever the user just clicked. Includes
    // both constant IDs (existing) and class IDs (S86; surfable from class
    // entries in the inspector once the class card lands).
    const candidateIds = new Set([
      ...candidates.map(c => c[0]),
      ...classCandidates.map(c => c.id),
    ]);
    let initialAnchor = fallbackId;
    if (typeof window !== 'undefined'
        && window.AE_FANOUT_ANCHOR
        && candidateIds.has(window.AE_FANOUT_ANCHOR)) {
      initialAnchor = window.AE_FANOUT_ANCHOR;
      window.AE_FANOUT_ANCHOR = null;  // consume — single-use
    }
    if (initialAnchor){
      sel.value = initialAnchor;
      render(initialAnchor, { collapsedStart: true });
      // Spin-in on first mount (also fires when surfing from inspector card)
      animateExpand();
    }

    // Expose an in-place animated swap so the inspector card can collapse-
    // then-expand WITHOUT going through AE_SHOW (which destroys the SVG).
    // Returns false if this fanout view has been torn down (different tab
    // is active) so the caller can fall back to AE_SHOW + anchor hint.
    window.AE_FANOUT_SWAP = (anchorId) => {
      if (!svg.isConnected) return false;        // stale: view was destroyed
      if (anchorId === sel.value) return true;   // same anchor — no-op
      sel.value = anchorId;
      animateSwap(anchorId);
      return true;
    };
  }

  // =================================================================
  // View 7 — Plan-vs-state Δ(P, S) graph diff
  // Side-by-side: planned DAG | realized DAG; deviating edges highlighted.
  // Δ-norm trace per session at the bottom.
  // Data: plan_state_diff.json (generated by build_plan_state_diff.py).
  // =================================================================
  function buildPlanStateDiff(root){
    root.innerHTML = `
      <div class="controls">
        <label>session</label>
        <select id="psSession" style="background:var(--panel);color:var(--ink);border:1px solid var(--rule);padding:4px 8px;font-family:'JetBrains Mono';font-size:12px;min-width:120px"></select>
        <label style="margin-left:8px">show</label>
        <button data-show="all" class="primary">all edges</button>
        <button data-show="diff">deviating only</button>
      </div>
      <div class="legend">
        <div><b>plan-DAG</b> (left) <b>·</b> <b>realized-DAG</b> (right)</div>
        <div style="margin-top:6px">
          <span class="sw" style="background:var(--rule-hi)"></span>edge in both (intersection)
          <br><span class="sw" style="background:var(--gate-fail)"></span>planned · not realized
          <br><span class="sw" style="background:var(--gate-open)"></span>realized · not planned
        </div>
        <div style="color:var(--ink-3);margin-top:6px">click a gate or input → inspector</div>
      </div>
      <div id="psStage" style="position:absolute;inset:0;display:flex;flex-direction:column">
        <div id="psStatus" class="mono" style="position:absolute;inset:46% 0 auto 0;text-align:center;color:var(--ink-3);font-size:13px;z-index:5">loading plan_state_diff.json…</div>
        <svg id="psSvg" width="100%" height="100%" class="grid-bg"></svg>
      </div>
    `;
    const svg = root.querySelector('#psSvg');
    const sel = root.querySelector('#psSession');
    const status = root.querySelector('#psStatus');
    const showAllBtn = root.querySelector('button[data-show="all"]');
    const showDiffBtn = root.querySelector('button[data-show="diff"]');

    let DATA = null;
    let mode = 'all';

    function fail(msg){
      status.textContent = msg;
      status.style.color = 'var(--gate-fail)';
    }
    function ok(msg){
      status.textContent = msg;
      status.style.color = 'var(--ink-3)';
    }

    function viewBox(){
      const r = svg.getBoundingClientRect();
      svg.setAttribute('viewBox', `0 0 ${r.width} ${r.height}`);
      return r;
    }

    // Wave label parser: "S85-W3-CF-5-...", "S85-W1a-...", "S85-FOLDED-..." (no wave)
    function waveOf(gateId){
      const m = /^S\d+-(W\d+[a-z]?)-/.exec(gateId);
      return m ? m[1] : 'misc';
    }
    // Input-type ordering for vertical layout (outer column)
    const TYPE_ORDER = { gate: 0, constant: 1, file: 2, ref: 3 };
    const TYPE_FILL = {
      gate:     'var(--b2)',
      constant: 'var(--accent)',
      file:     'var(--ink-2)',
      ref:      'var(--ink-3)',
    };

    function entityFor(tok, kind){
      if (kind === 'constant') return (D.CONSTANTS || []).find(x => x.id === tok || x.name === tok);
      if (kind === 'gate')     return (D.GATES || []).find(x => x.id === tok);
      return null;
    }
    function selTypeFor(kind){
      return ({ constant:'constant', gate:'gate' })[kind] || null;
    }

    // Build positions for one DAG panel.
    function buildPanelPositions(panelLeft, panelRight, edges, gates, inputs){
      const yTop = 56, yBot = (svg.getBoundingClientRect().height) - 90;
      const gateX = panelLeft + 80;
      const inputX = panelRight - 110;
      const gatePos = new Map();
      // Sort gates by wave, then by id
      const gatesSorted = [...gates].sort((a, b) => {
        const wa = waveOf(a), wb = waveOf(b);
        if (wa !== wb) return wa.localeCompare(wb);
        return a.localeCompare(b);
      });
      gatesSorted.forEach((g, i) => {
        const t = gatesSorted.length === 1 ? 0.5 : (i / (gatesSorted.length - 1));
        gatePos.set(g, { x: gateX, y: yTop + t * (yBot - yTop), wave: waveOf(g) });
      });

      const inputPos = new Map();
      const inputsSorted = [...inputs].sort((a, b) => {
        const ka = TYPE_ORDER[a.kind] ?? 9, kb = TYPE_ORDER[b.kind] ?? 9;
        if (ka !== kb) return ka - kb;
        return a.tok.localeCompare(b.tok);
      });
      inputsSorted.forEach((it, i) => {
        const t = inputsSorted.length === 1 ? 0.5 : (i / (inputsSorted.length - 1));
        inputPos.set(`${it.kind}::${it.tok}`, {
          x: inputX, y: yTop + t * (yBot - yTop), kind: it.kind, tok: it.tok,
        });
      });
      return { gatePos, inputPos };
    }

    function drawPanel(panelLeft, panelRight, label, edges, sessRec, deviationFilter){
      const W = panelRight - panelLeft;
      // Panel header
      const hdr = svgEl('text', {
        x: panelLeft + W/2, y: 30,
        fill: 'var(--accent)', 'font-family':'JetBrains Mono',
        'font-size': 12, 'text-anchor':'middle',
      }, svg);
      hdr.textContent = label;

      // Gates and inputs on this side
      const gates = new Set(edges.map(e => e.src));
      const inputs = new Map();
      for (const e of edges){
        const k = `${e.kind}::${e.tgt}`;
        if (!inputs.has(k)) inputs.set(k, { tok: e.tgt, kind: e.kind });
      }
      const { gatePos, inputPos } = buildPanelPositions(
        panelLeft, panelRight, edges, gates, [...inputs.values()],
      );

      // Edges first
      for (const e of edges){
        const a = gatePos.get(e.src);
        const b = inputPos.get(`${e.kind}::${e.tgt}`);
        if (!a || !b) continue;
        // Determine deviation status — needed for color + filter
        const devKey = `${e.src}::${e.kind}::${e.tgt}`;
        const dev = sessRec.devSet.get(devKey);
        if (deviationFilter && !dev) continue;
        let stroke = 'var(--rule-hi)';
        let dash = '';
        let opacity = 0.45;
        if (dev === 'PLANNED_NOT_REALIZED'){
          stroke = 'var(--gate-fail)'; dash = '3 3'; opacity = 0.85;
        } else if (dev === 'REALIZED_NOT_PLANNED'){
          stroke = 'var(--gate-open)'; dash = '3 3'; opacity = 0.85;
        }
        const mx = (a.x + b.x) / 2;
        svgEl('path', {
          d: `M ${a.x+30} ${a.y} C ${mx} ${a.y}, ${mx} ${b.y}, ${b.x-6} ${b.y}`,
          fill: 'none', stroke, 'stroke-width': dev ? 1.2 : 0.6,
          'stroke-dasharray': dash, opacity,
        }, svg);
      }

      // Gate nodes (inner column)
      let prevWave = null;
      for (const [gid, p] of gatePos){
        // Wave divider on first appearance
        if (p.wave !== prevWave){
          const t = svgEl('text', {
            x: p.x - 60, y: p.y + 3,
            fill: 'var(--ink-3)', 'font-family':'JetBrains Mono',
            'font-size': 9, 'text-anchor':'end',
          }, svg);
          t.textContent = p.wave;
          prevWave = p.wave;
        }
        const g = svgEl('g', { transform:`translate(${p.x},${p.y})`, style:'cursor:pointer' }, svg);
        g.classList.add('tree-node');
        svgEl('rect', { x: -28, y: -7, width: 56, height: 14, rx: 2, fill:'var(--panel)', stroke:'var(--rule-hi)', 'stroke-width':0.6 }, g);
        const t = svgEl('text', {
          x: 0, y: 3, fill: 'var(--ink-2)', 'font-family':'JetBrains Mono',
          'font-size': 9, 'text-anchor':'middle',
        }, g);
        // Compact gate label: drop session prefix and wave prefix if redundant
        const short = gid.replace(/^S\d+-(W\d+[a-z]?-)?/, '');
        t.textContent = short.slice(0, 14);
        const title = svgEl('title', {}, g);
        title.textContent = gid;
        g.addEventListener('click', () => {
          const ent = (D.GATES || []).find(x => x.id === gid);
          if (ent) bus.set({ selected: ent, selType: 'gate' });
        });
      }

      // Input nodes (outer column)
      for (const [, p] of inputPos){
        const g = svgEl('g', { transform:`translate(${p.x},${p.y})`, style:'cursor:pointer' }, svg);
        g.classList.add('tree-node');
        svgEl('circle', { r: 3.5, fill: TYPE_FILL[p.kind] || 'var(--ink-3)' }, g);
        const t = svgEl('text', {
          x: 8, y: 3, fill: 'var(--ink-2)', 'font-family':'JetBrains Mono',
          'font-size': 9.5, 'text-anchor':'start',
        }, g);
        t.textContent = String(p.tok).slice(0, 28);
        const title = svgEl('title', {}, g);
        title.textContent = `${p.kind}: ${p.tok}`;
        g.addEventListener('click', () => {
          const ent = entityFor(p.tok, p.kind);
          const st = selTypeFor(p.kind);
          if (ent && st) bus.set({ selected: ent, selType: st });
        });
      }
    }

    function drawTrace(sessions, currentId){
      const r = svg.getBoundingClientRect();
      const baseY = r.height - 50;
      const traceY = r.height - 16;
      const padX = 30;
      const W = r.width - padX*2;
      const N = sessions.length;
      const maxDelta = Math.max(1, ...sessions.map(s => s.delta_norm));
      svgEl('text', {
        x: padX, y: baseY, fill:'var(--ink-3)','font-family':'JetBrains Mono','font-size':10,
      }, svg).textContent = `Δ-norm trace (${sessions.length} session${sessions.length===1?'':'s'})`;

      sessions.forEach((s, i) => {
        const t = N === 1 ? 0.5 : (i / (N - 1));
        const x = padX + t * W;
        const h = (s.delta_norm / maxDelta) * 22;
        const y = traceY - h;
        const isCurrent = s.session_id === currentId;
        svgEl('rect', {
          x: x - 6, y, width: 12, height: h,
          fill: isCurrent ? 'var(--accent)' : 'var(--rule-hi)',
          opacity: isCurrent ? 0.95 : 0.6,
          style: 'cursor:pointer',
        }, svg).addEventListener('click', () => { sel.value = s.session_id; render(); });
        const label = svgEl('text', {
          x, y: traceY + 8, fill: isCurrent ? 'var(--accent)' : 'var(--ink-3)',
          'font-family':'JetBrains Mono', 'font-size': 9, 'text-anchor':'middle',
        }, svg);
        label.textContent = `${s.session_id}·${s.delta_norm}`;
      });
    }

    function render(){
      if (!DATA){ return; }
      const sid = sel.value;
      const sess = DATA.sessions.find(x => x.session_id === sid);
      if (!sess){ fail(`session ${sid} not found in JSON`); return; }
      ok('');
      clearChildren(svg);
      const r = viewBox();

      // Build deviation lookup so panel rendering can flag edges.
      const devSet = new Map();
      for (const d of sess.deviating_edges){
        devSet.set(`${d.src}::${d.kind}::${d.tgt}`, d.deviation);
      }
      const sessRec = { ...sess, devSet };

      // Two panels: planned (left) and realized (right)
      const halfW = r.width / 2;
      const filterDev = (mode === 'diff');
      drawPanel(0,        halfW,    `plan-DAG · ${sess.gate_count_planned} gates`, sess.planned_edges, sessRec, filterDev);
      drawPanel(halfW + 4, r.width, `realized-DAG · ${sess.gate_count_realized} gates`, sess.realized_edges, sessRec, filterDev);

      // Center divider
      svgEl('line', {
        x1: halfW + 2, y1: 12, x2: halfW + 2, y2: r.height - 70,
        stroke:'var(--rule)', 'stroke-width': 0.8, 'stroke-dasharray': '4 6',
      }, svg);

      // Δ-norm trace
      drawTrace(DATA.sessions, sid);

      // Top-line summary
      svgEl('text', {
        x: r.width/2, y: r.height - 60, fill:'var(--ink-3)',
        'font-family':'JetBrains Mono','font-size':10, 'text-anchor':'middle',
      }, svg).textContent =
        `${sid}  ·  Δ-norm = ${sess.delta_norm}  ·  ` +
        `missing (planned, not run): ${sess.missing_gates.length}  ·  ` +
        `extra (run, not planned): ${sess.extra_gates.length}`;
    }

    function bindControls(){
      sel.addEventListener('change', render);
      showAllBtn.addEventListener('click', () => {
        mode = 'all';
        showAllBtn.classList.add('primary');
        showDiffBtn.classList.remove('primary');
        render();
      });
      showDiffBtn.addEventListener('click', () => {
        mode = 'diff';
        showDiffBtn.classList.add('primary');
        showAllBtn.classList.remove('primary');
        render();
      });
      window.addEventListener('resize', () => render());
    }

    fetch('plan_state_diff.json')
      .then(r => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then(json => {
        DATA = json;
        if (!DATA.sessions || !DATA.sessions.length){
          fail('plan_state_diff.json has no sessions; run build_plan_state_diff.py');
          return;
        }
        sel.innerHTML = DATA.sessions
          .map(s => `<option value="${s.session_id}">${s.session_id} · Δ=${s.delta_norm}</option>`)
          .join('');
        sel.value = DATA.sessions[DATA.sessions.length - 1].session_id;
        bindControls();
        render();
      })
      .catch(err => {
        fail(`could not load plan_state_diff.json: ${err.message}. Run: tools/viz/console/build_plan_state_diff.py`);
      });
  }

  // =================================================================
  // View 8 — Chain-of-custody Genealogy ("red string on the wall")
  // Renders any anchor entity (gate / constant / theorem / mechanism /
  // session / researcher) as the center of a bidirectional ladder:
  //   4 upstream depths · ANCHOR · 4 downstream depths
  // Each chain entry is color-coded by lens (authorship / citation /
  // custody / logical) — toggleable via chip bar. Clicking an entry
  // deep-links to /research/<type>/<id>/ in the meme-engine-web docs
  // corpus. No client BFS; the sidecar is pre-computed upstream.
  // Data: chain_of_custody.json (built by build_chain_of_custody.py).
  // =================================================================
  function buildGenealogy(root){
    root.innerHTML = `
      <div class="gen-shell">
        <header class="gen-head">
          <div class="gen-anchor-picker">
            <div class="anchor-type-tags" id="genTypeTags"></div>
            <input id="genQ" type="text" autocomplete="off" spellcheck="false" placeholder="Search"/>
            <ul class="results" id="genResults" hidden></ul>
          </div>
          <div class="gen-lens-chips">
            <span class="lens-label">Lenses</span>
            <button class="lens-chip" data-lens="logical"    aria-pressed="true">Logical <span class="count">0</span></button>
            <button class="lens-chip" data-lens="custody"    aria-pressed="true">Custody <span class="count">0</span></button>
            <button class="lens-chip" data-lens="authorship" aria-pressed="true">Authorship <span class="count">0</span></button>
            <button class="lens-chip" data-lens="citation"   aria-pressed="true">Citation <span class="count">0</span></button>
          </div>
        </header>
        <div class="gen-stats" id="genStats"></div>
        <div class="gen-ladder" id="genLadder"><div class="gen-msg">Loading chain_of_custody.json…</div></div>
      </div>
    `;
    const shell      = root.querySelector('.gen-shell');
    const input      = root.querySelector('#genQ');
    const resultsUl  = root.querySelector('#genResults');
    const statsBar   = root.querySelector('#genStats');
    const ladder     = root.querySelector('#genLadder');

    // Routable types → /research/<segment>/<id>/ on meme-engine.com.
    //   - closed_mechanisms folds into mechanisms (manifest collapses both)
    //   - researchers (kebab-case agent IDs in the sidecar) → /research/agents/
    //     because the web build's "researchers" collection holds PascalCase
    //     historical-physicist names; the kebab-case agent dir is "agents/".
    // Unlisted types (data_provenance / equations / open_channels) render
    // as text-only chain entries; the sidecar surfaces them but no doc page exists.
    const ROUTE_SEG = {
      gates: 'gates',
      constants: 'constants',
      theorems: 'theorems',
      mechanisms: 'mechanisms',
      closed_mechanisms: 'mechanisms',
      sessions: 'sessions',
      researchers: 'agents',
    };

    // Human-readable type labels (singular, for the anchor column header).
    const TYPE_LABEL = {
      gates: 'Gate',
      constants: 'Constant',
      theorems: 'Theorem',
      mechanisms: 'Mechanism',
      closed_mechanisms: 'Mechanism · closed',
      sessions: 'Session',
      researchers: 'Researcher',
    };

    // Typeahead grouping order: small/distinctive collections first so the
    // empty-query default isn't a wall of 2,500 gates. Within a group, sort
    // naturally (numeric-aware) by title or id.
    const TYPE_RANK = {
      closed_mechanisms: 0,
      researchers: 1,
      sessions: 2,
      theorems: 3,
      mechanisms: 4,
      constants: 5,
      gates: 6,
    };

    // Lens-priority ordering within a level (matches builder convention).
    const LENS_ORDER = { logical: 0, custody: 1, citation: 2, authorship: 3 };

    let DATA = null;
    let ID_INDEX = null;   // { gates: Set<string>, constants: Set<string>, ... }
    let anchorList = [];   // [{ key, type, id, title, up, down, degree, searchKey }] degree-desc
    let highlighted = -1;
    let selectedType = null; // if set, the type-tag filter is active
    const lensOn = { logical: true, custody: true, authorship: true, citation: true };

    // Ordered list of (type, short-label) for the type-tag radial row. Order
    // mirrors TYPE_RANK so the smallest/most-distinctive collections lead.
    const TYPE_TAGS = [
      ['closed_mechanisms', 'closed'],
      ['researchers',       'researchers'],
      ['sessions',          'sessions'],
      ['theorems',          'theorems'],
      ['mechanisms',        'mechanisms'],
      ['constants',         'constants'],
      ['gates',             'gates'],
    ];

    function deepLinkFor(type, id){
      const seg = ROUTE_SEG[type];
      if (!seg) return null;
      // If the index loaded, gate the link on the ID being known to the web
      // build. Without the index (sidecar missing), fall back to emitting the
      // link — better than text-only across the board.
      if (ID_INDEX && ID_INDEX[seg] && !ID_INDEX[seg].has(id)) return null;
      return `/research/${seg}/${id}/`;
    }

    function escapeHtml(s){
      return String(s ?? '').replace(/[&<>"']/g, c =>
        ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]));
    }

    function renderResults(filterTerm){
      const q = (filterTerm || '').trim().toLowerCase();
      let matches;
      let withSections;
      if (selectedType){
        // Type-tag active: scope to that type, then optionally narrow by query.
        let scoped = anchorList.filter(a => a.type === selectedType);
        if (q) scoped = scoped.filter(a => a.searchKey.includes(q));
        matches = scoped;
        withSections = false;
      } else if (q){
        // Typed query, no type filter: full filter across all anchors.
        matches = anchorList.filter(a => a.searchKey.includes(q)).slice(0, 200);
        withSections = false;
      } else {
        // Empty query, no type filter: per-type sample so every collection
        // surfaces in the default view. Click a type-tag to see all of one.
        const PER_TYPE = 25;
        const seen = {};
        matches = [];
        for (const a of anchorList){
          const c = seen[a.type] || 0;
          if (c < PER_TYPE){ matches.push(a); seen[a.type] = c + 1; }
        }
        withSections = true;
      }
      if (!matches.length){
        resultsUl.innerHTML =
          '<li class="empty"><span class="kicker">no match</span><span class="label">No anchors found</span><span class="degree"></span></li>';
        resultsUl.hidden = false;
        highlighted = -1;
        return;
      }
      // Type totals (for section header counts in the empty-query view).
      const typeTotals = {};
      if (withSections){
        for (const a of anchorList) typeTotals[a.type] = (typeTotals[a.type] || 0) + 1;
      }
      const html = [];
      let lastType = null;
      let pickIdx = 0;
      for (const a of matches){
        if (withSections && a.type !== lastType){
          const sampleN = matches.filter(x => x.type === a.type).length;
          const total = typeTotals[a.type] || sampleN;
          const more = total > sampleN ? `${sampleN} of ${total}` : `${total}`;
          html.push(
            `<li class="section">`
              + `<span class="kicker">${escapeHtml(a.type)}</span>`
              + `<span class="label">${more}</span>`
              + `<span class="degree">${total > sampleN ? 'type to filter' : 'all'}</span>`
            + `</li>`);
          lastType = a.type;
        }
        html.push(
          `<li data-key="${escapeHtml(a.key)}" data-idx="${pickIdx}"${pickIdx===0?' class="active"':''}>`
            + `<span class="kicker">${escapeHtml(a.type)}</span>`
            + `<span class="label">${escapeHtml(a.title || a.id)}</span>`
            + `<span class="degree">↑${a.up} · ↓${a.down}</span>`
          + `</li>`);
        pickIdx++;
      }
      resultsUl.innerHTML = html.join('');
      resultsUl.hidden = false;
      highlighted = 0;
    }

    function renderEntry(e){
      const key = `${e.type}:${e.id}`;
      const isAnchor = !!(DATA && DATA.anchors && DATA.anchors[key]);
      const route = deepLinkFor(e.type, e.id);
      const title = e.title || e.id;
      const viaHtml   = `<span class="via">${escapeHtml(e.via)}</span>`;
      const titleHtml = `<span class="title">${escapeHtml(title)}</span>`;
      const idHtml    = `<span class="id">${escapeHtml(e.type)}:${escapeHtml(e.id)}</span>`;

      // Three states: pivot (entry is itself an anchor, click re-roots the
      // ladder), ext (no anchor data but a /research/ page exists), or text.
      // For pivots, set href to the /research/ route so modifier-clicks
      // (Cmd/Ctrl/Shift/middle) still open the doc in a new tab — only the
      // plain click is intercepted into pickAnchor() by the ladder delegate.
      if (isAnchor){
        const href = route || '#';
        return `<a class="chain-entry lens-${e.lens} pivot" href="${href}" data-anchor-key="${escapeHtml(key)}">`
          + viaHtml + titleHtml + idHtml + `</a>`;
      }
      if (route){
        return `<a class="chain-entry lens-${e.lens} ext" href="${route}">`
          + viaHtml + titleHtml + idHtml + `</a>`;
      }
      return `<span class="chain-entry lens-${e.lens} no-route">`
        + viaHtml + titleHtml + idHtml + `</span>`;
    }

    function updateLensCounts(entry){
      const counts = { logical: 0, custody: 0, authorship: 0, citation: 0 };
      for (const dir of ['upstream','downstream']){
        const buckets = entry[dir] || {};
        for (const d in buckets){
          for (const e of buckets[d]){
            if (counts[e.lens] != null) counts[e.lens]++;
          }
        }
      }
      for (const name in counts){
        const el = root.querySelector(`.lens-chip[data-lens="${name}"] .count`);
        if (el) el.textContent = counts[name];
      }
    }

    function renderAnchor(key){
      if (!DATA) return;
      const entry = DATA.anchors[key];
      if (!entry){
        ladder.innerHTML = `<div class="gen-msg">Unknown anchor: ${escapeHtml(key)}</div>`;
        statsBar.innerHTML = '';
        return;
      }
      try { localStorage.setItem('ae.gen.anchor', key); } catch(e){}
      const a = entry.anchor || {};
      const s = entry.stats || {};
      const route = deepLinkFor(a.type, a.id);

      const metaBits = [];
      metaBits.push(`↑ <b>${s.total_upstream ?? 0}</b> · ↓ <b>${s.total_downstream ?? 0}</b>`);
      if (a.verdict)   metaBits.push(`verdict <span class="v">${escapeHtml(a.verdict)}</span>`);
      if (a.session)   metaBits.push(`session <b>${escapeHtml(a.session)}</b>`);
      if (a.closed_by) metaBits.push(`closed by <b>${escapeHtml(a.closed_by)}</b>`);
      const trunc = s.truncated_at_depth
        ? `<span class="trunc">truncated at depth ${s.truncated_at_depth} (top ${DATA.config.top_k_per_level}/level)</span>`
        : '';

      statsBar.innerHTML =
        `<span class="anchor-title">${escapeHtml(a.title || a.id)}</span>`
        + `<span class="anchor-meta">${metaBits.join(' · ')}</span>`
        + trunc;

      updateLensCounts(entry);

      // Filter empty depth columns so the anchor isn't marooned with dead
      // space (e.g. a researcher with 0 upstream + 4 downstream layers).
      const cols = [];
      for (let d = 4; d >= 1; d--){
        const entries = (entry.upstream || {})[String(d)] || [];
        if (entries.length) cols.push({ kind:'up', depth:d, entries });
      }
      cols.push({ kind:'anchor' });
      for (let d = 1; d <= 4; d++){
        const entries = (entry.downstream || {})[String(d)] || [];
        if (entries.length) cols.push({ kind:'down', depth:d, entries });
      }

      const sortedEntries = arr => arr.slice().sort((x, y) => {
        const lx = LENS_ORDER[x.lens] ?? 9;
        const ly = LENS_ORDER[y.lens] ?? 9;
        if (lx !== ly) return lx - ly;
        return String(x.id).localeCompare(String(y.id));
      });

      ladder.innerHTML = cols.map(col => {
        if (col.kind === 'anchor'){
          const verdictRow   = a.verdict   ? `<div class="meta">verdict: <span class="v">${escapeHtml(a.verdict)}</span></div>` : '';
          const sessionRow   = a.session   ? `<div class="meta">session: <b>${escapeHtml(a.session)}</b></div>` : '';
          const closedByRow  = a.closed_by ? `<div class="meta">closed by: <b>${escapeHtml(a.closed_by)}</b></div>` : '';
          const openDoc      = route
            ? `<a class="open-doc" href="${route}">Open docs →</a>`
            : `<div class="meta" style="color:var(--ink-3);margin-top:8px">(no /research/ page for this type)</div>`;
          const typeLabel = TYPE_LABEL[a.type] || a.type || 'Anchor';
          return `
            <div class="gen-col anchor" data-anchor="1">
              <div class="gen-col-head anchor">${escapeHtml(typeLabel)}</div>
              <div class="gen-col-body">
                <div class="anchor-card">
                  <div class="kicker">${escapeHtml(a.type)}</div>
                  <div class="title">${escapeHtml(a.title || a.id)}</div>
                  <div class="id">${escapeHtml(a.type)}:${escapeHtml(a.id)}</div>
                  ${verdictRow}${sessionRow}${closedByRow}
                  ${openDoc}
                </div>
              </div>
            </div>`;
        }
        const arrow = col.kind === 'up' ? '←' : '→';
        const dirLabel = col.kind === 'up' ? 'Upstream' : 'Downstream';
        const headHtml = `${arrow} ${dirLabel} <span class="depth">d${col.depth}</span>`;
        const sorted = sortedEntries(col.entries);
        const body = sorted.map(renderEntry).join('');
        return `<div class="gen-col"><div class="gen-col-head">${headHtml}</div><div class="gen-col-body">${body}</div></div>`;
      }).join('');

      // Center the anchor in the horizontal scroll viewport on first render.
      // Defer one frame so flex layout has settled before we read offsetLeft.
      requestAnimationFrame(() => {
        const anchorEl = ladder.querySelector('.gen-col[data-anchor]');
        if (!anchorEl) return;
        const target = anchorEl.offsetLeft + anchorEl.offsetWidth / 2 - ladder.clientWidth / 2;
        ladder.scrollLeft = Math.max(0, target);
      });

      // Surface to the bus so the shared inspector can react if it wants.
      bus.set({ selected: { id: a.id, type: a.type, key, title: a.title }, selType: 'gen-anchor' });
    }

    function syncLensClasses(){
      for (const name in lensOn){
        shell.classList.toggle(`hide-${name}`, !lensOn[name]);
      }
      try { localStorage.setItem('ae.gen.lenses', JSON.stringify(lensOn)); } catch(e){}
    }

    function restoreLenses(){
      try {
        const raw = localStorage.getItem('ae.gen.lenses');
        if (raw){
          const stored = JSON.parse(raw);
          for (const k in lensOn){
            if (typeof stored[k] === 'boolean') lensOn[k] = stored[k];
          }
        }
      } catch(e){}
      for (const name in lensOn){
        const chip = root.querySelector(`.lens-chip[data-lens="${name}"]`);
        if (chip) chip.setAttribute('aria-pressed', lensOn[name] ? 'true' : 'false');
      }
    }

    function pickAnchor(key){
      input.value = '';
      resultsUl.hidden = true;
      renderAnchor(key);
    }

    input.addEventListener('input',  () => renderResults(input.value));
    input.addEventListener('focus',  () => { if (anchorList.length) renderResults(input.value); });
    input.addEventListener('keydown', ev => {
      if (resultsUl.hidden) return;
      const items = [...resultsUl.querySelectorAll('li[data-key]')];
      if (!items.length) return;
      if (ev.key === 'ArrowDown'){
        ev.preventDefault();
        highlighted = Math.min(highlighted + 1, items.length - 1);
      } else if (ev.key === 'ArrowUp'){
        ev.preventDefault();
        highlighted = Math.max(highlighted - 1, 0);
      } else if (ev.key === 'Enter'){
        ev.preventDefault();
        const it = items[Math.max(highlighted, 0)];
        if (it) pickAnchor(it.dataset.key);
        return;
      } else if (ev.key === 'Escape'){
        resultsUl.hidden = true;
        return;
      } else {
        return;
      }
      items.forEach((el, i) => el.classList.toggle('active', i === highlighted));
      items[highlighted] && items[highlighted].scrollIntoView({ block: 'nearest' });
    });
    resultsUl.addEventListener('click', ev => {
      const li = ev.target.closest('li[data-key]');
      if (li) pickAnchor(li.dataset.key);
    });
    document.addEventListener('click', ev => {
      if (!root.contains(ev.target)){ resultsUl.hidden = true; return; }
      const picker = root.querySelector('.gen-anchor-picker');
      if (picker && !picker.contains(ev.target)) resultsUl.hidden = true;
    });
    root.querySelectorAll('.lens-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        const lens = chip.dataset.lens;
        lensOn[lens] = !lensOn[lens];
        chip.setAttribute('aria-pressed', lensOn[lens] ? 'true' : 'false');
        syncLensClasses();
      });
    });

    function renderTypeTags(){
      const host = root.querySelector('#genTypeTags');
      if (!host) return;
      const counts = {};
      for (const a of anchorList) counts[a.type] = (counts[a.type] || 0) + 1;
      host.innerHTML = TYPE_TAGS
        .filter(([t]) => counts[t])  // hide tags whose type has no anchors (mechanisms is 0)
        .map(([t, label]) =>
          `<button class="type-tag" data-type="${t}" aria-pressed="false">`
            + `${escapeHtml(label)} <span class="count">${counts[t]}</span>`
          + `</button>`).join('');
      host.querySelectorAll('.type-tag').forEach(tag => {
        tag.addEventListener('click', () => setSelectedType(tag.dataset.type));
      });
    }

    function setSelectedType(t){
      // Toggle off if same; otherwise switch.
      selectedType = (selectedType === t) ? null : t;
      root.querySelectorAll('.type-tag').forEach(el => {
        const on = el.dataset.type === selectedType;
        el.classList.toggle('active', on);
        el.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
      renderResults(input.value);
      input.focus();
    }

    // Delegate ladder clicks: a plain left-click on a pivot entry re-anchors
    // the view; modifier-clicks (Cmd/Ctrl/Shift/Alt/middle) fall through to
    // the browser so /research/<...>/ opens in a new tab as expected.
    ladder.addEventListener('click', ev => {
      const pivot = ev.target.closest('a.chain-entry.pivot');
      if (!pivot) return;
      if (ev.button !== 0) return;
      if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey) return;
      ev.preventDefault();
      const key = pivot.getAttribute('data-anchor-key');
      if (key) pickAnchor(key);
    });

    function ingestIdIndex(rawIndex){
      if (!rawIndex || typeof rawIndex !== 'object') return null;
      const out = {};
      for (const k in rawIndex){
        const v = rawIndex[k];
        if (Array.isArray(v)) out[k] = new Set(v);
      }
      return out;
    }

    function go(json, indexJson){
      DATA = json;
      ID_INDEX = ingestIdIndex(indexJson);
      window.AE_CHAIN_OF_CUSTODY = json;
      if (indexJson) window.AE_RESEARCH_ID_INDEX = indexJson;

      const list = [];
      for (const key in json.anchors){
        const a = json.anchors[key];
        const ac = a.anchor || {};
        const s = a.stats || {};
        const up = s.total_upstream || 0;
        const down = s.total_downstream || 0;
        list.push({
          key,
          type: ac.type,
          id: ac.id,
          title: ac.title || ac.id,
          up, down,
          degree: up + down,
          searchKey: `${key} ${ac.title || ''} ${ac.id || ''}`.toLowerCase(),
        });
      }
      // Type-grouped natural sort: small collections (researchers, sessions,
      // theorems) lead so the empty-query picker shows distinctive anchors
      // first instead of a wall of high-degree gates. Within a group, sort
      // naturally (numeric-aware) by title so "session 10" precedes "session 89".
      const naturalCmp = (x, y) => String(x).localeCompare(String(y), undefined, { numeric: true, sensitivity: 'base' });
      list.sort((x, y) => {
        const rx = TYPE_RANK[x.type] ?? 99;
        const ry = TYPE_RANK[y.type] ?? 99;
        if (rx !== ry) return rx - ry;
        return naturalCmp(x.title || x.id, y.title || y.id);
      });
      anchorList = list;

      renderTypeTags();
      restoreLenses();
      syncLensClasses();

      let start = null;
      try { start = localStorage.getItem('ae.gen.anchor'); } catch(e){}
      if (!start || !json.anchors[start]) start = anchorList[0] && anchorList[0].key;
      if (start) renderAnchor(start);
    }

    if (window.AE_CHAIN_OF_CUSTODY && window.AE_RESEARCH_ID_INDEX){
      go(window.AE_CHAIN_OF_CUSTODY, window.AE_RESEARCH_ID_INDEX);
      return;
    }
    // Load chain payload + ID allowlist in parallel; tolerate index 404 (run
    // outside meme-engine-web — fall back to ungated links).
    // Prefer chain_of_custody.json.gz when served (the web sync gzips it
    // because the raw 50+ MB JSON exceeds Cloudflare's 25 MB asset cap);
    // fall back to plain .json when running upstream directly.
    const fetchChain = window.AE_CHAIN_OF_CUSTODY
      ? Promise.resolve(window.AE_CHAIN_OF_CUSTODY)
      : fetch('chain_of_custody.json.gz').then(rsp => {
          if (rsp.ok) {
            const stream = rsp.body.pipeThrough(new DecompressionStream('gzip'));
            return new Response(stream).json();
          }
          return fetch('chain_of_custody.json').then(r => {
            if (!r.ok) throw new Error(`HTTP ${r.status}`);
            return r.json();
          });
        });
    const fetchIndex = window.AE_RESEARCH_ID_INDEX
      ? Promise.resolve(window.AE_RESEARCH_ID_INDEX)
      : fetch('research_id_index.json').then(rsp => rsp.ok ? rsp.json() : null).catch(() => null);

    Promise.all([fetchChain, fetchIndex])
      .then(([chainJson, indexJson]) => go(chainJson, indexJson))
      .catch(err => {
        ladder.innerHTML =
          `<div class="gen-msg">Could not load chain_of_custody.json: ${escapeHtml(err.message)}.<br/>`
          + `Run <code>tools/viz/console/build_chain_of_custody.py</code> upstream, then re-sync.</div>`;
      });
  }

  // =================================================================
  // View 8b — Theorem Tracks (formerly the default Genealogy)
  // Slot×track structural theorems (S85 workshop files) cluster per slot;
  // cross-track edges within a cluster are the tree-to-graph step.
  // Proven theorems orbit the perimeter, area-hued. Citations as faint
  // curves between proven theorems.
  // Data: theorem_genealogy.json (built by build_theorem_genealogy.py).
  // =================================================================
  function buildTheoremTracks(root){
    root.innerHTML = `
      <div class="controls">
        <label>filter</label>
        <button data-f="all" class="primary">all</button>
        <button data-f="structural">structural only</button>
        <button data-f="cross">cross-track edges</button>
      </div>
      <div class="legend">
        <div><b>slots</b>: each cluster is one structural theorem proven via multiple machineries</div>
        <div style="margin-top:6px">
          <span class="sw" style="background:var(--accent)"></span>cross-track edge (same theorem)
          <br><span class="sw" style="background:var(--rule-hi)"></span>depends-on / citation
        </div>
        <div style="color:var(--ink-3);margin-top:6px">click a node → inspector</div>
        <div id="genHdr" class="mono" style="color:var(--ink-3);margin-top:6px;font-size:10.5px"></div>
      </div>
      <svg id="genSvg" width="100%" height="100%" class="grid-bg"></svg>
      <div id="genStatus" class="mono" style="position:absolute;left:16px;bottom:16px;color:var(--ink-3);font-size:11px"></div>
    `;
    const svg = root.querySelector('#genSvg');
    const status = root.querySelector('#genStatus');
    const hdr = root.querySelector('#genHdr');
    let DATA = null;
    let filter = 'all';

    // Area → hue (matches buildGraph)
    const areaHue = {
      NCG: 60, spectral: 180, symmetry: 280, BCS: 20,
      transit: 340, stability: 110, simulation: 210,
      CC: 50, cosmo: 240, gauge: 310, geometry: 130,
      acoustic: 170, general: 200,
    };
    function hueFor(area){ return areaHue[area] ?? 200; }

    function viewBox(){
      const r = svg.getBoundingClientRect();
      svg.setAttribute('viewBox', `0 0 ${r.width} ${r.height}`);
      return r;
    }

    function layoutNodes(structural, proven){
      const { width, height } = viewBox();
      const cx = width / 2, cy = height / 2;
      const innerR = Math.min(width, height) * 0.18;     // slot-cluster ring
      const outerR = Math.min(width, height) * 0.42;     // proven-orbit ring

      // Group structural by slot. Place each slot at a cardinal angle.
      const bySlot = new Map();
      for (const n of structural){
        if (!bySlot.has(n.slot)) bySlot.set(n.slot, []);
        bySlot.get(n.slot).push(n);
      }
      const slotKeys = [...bySlot.keys()].sort();
      const slotAngle = new Map();
      slotKeys.forEach((k, i) => {
        slotAngle.set(k, (i / slotKeys.length) * 2 * Math.PI - Math.PI/2);
      });

      const positions = new Map();
      // Place structural nodes — small triangle/line within each slot cluster.
      for (const [slot, members] of bySlot){
        const ang = slotAngle.get(slot);
        const cxS = cx + innerR * Math.cos(ang);
        const cyS = cy + innerR * Math.sin(ang);
        const rad = 26;
        members.sort((a, b) => a.track.localeCompare(b.track));
        members.forEach((n, k) => {
          const t = members.length === 1 ? 0
            : (k / members.length) * 2 * Math.PI;
          positions.set(n.id, {
            x: cxS + rad * Math.cos(t),
            y: cyS + rad * Math.sin(t),
            slot, slot_x: cxS, slot_y: cyS,
          });
        });
      }

      // Place proven nodes on the outer ring, grouped by area.
      const byArea = new Map();
      for (const n of proven){
        if (!byArea.has(n.area)) byArea.set(n.area, []);
        byArea.get(n.area).push(n);
      }
      const areas = [...byArea.keys()].sort();
      areas.forEach((a, ai) => {
        const baseAng = (ai / areas.length) * 2 * Math.PI - Math.PI/2;
        const arr = byArea.get(a);
        arr.forEach((n, i) => {
          const sp = (i - (arr.length - 1) / 2) * 0.06;
          const ang = baseAng + sp;
          const r = outerR * (0.85 + 0.18 * (i % 5) / 5);
          positions.set(n.id, {
            x: cx + r * Math.cos(ang),
            y: cy + r * Math.sin(ang),
            area: a,
          });
        });
      });

      return { positions, slotAngle, innerR, cx, cy };
    }

    function drawEdge(a, b, kind){
      let stroke = 'var(--rule)';
      let dash = '';
      let opacity = 0.35;
      let width = 0.6;
      if (kind === 'cross_track'){
        stroke = 'var(--accent)'; dash = '3 3';
        opacity = 0.9; width = 1.4;
      } else if (kind === 'cites'){
        stroke = 'var(--rule-hi)'; opacity = 0.45; width = 0.7;
      } else if (kind === 'depends_on'){
        stroke = 'var(--ink-3)'; opacity = 0.25; width = 0.5;
      }
      const mx = (a.x + b.x) / 2;
      svgEl('path', {
        d: `M ${a.x} ${a.y} Q ${mx} ${(a.y + b.y) / 2} ${b.x} ${b.y}`,
        fill: 'none', stroke, 'stroke-width': width,
        'stroke-dasharray': dash, opacity,
      }, svg);
    }

    function entityFor(node){
      if (node.kind === 'proven'){
        return (D.THEOREMS || []).find(x => x.id === node.id) || node;
      }
      // structural — synthesize a theorem-shape so the inspector card renders.
      return {
        id: node.id,
        name: node.name,
        statement: node.statement || `${node.session} slot ${node.slot} · track ${node.track}`,
        session: node.session,
        area: node.area,
        status: 'STRUCTURAL',
      };
    }

    function render(){
      if (!DATA){ return; }
      clearChildren(svg);
      const r = viewBox();
      const { width, height } = r;

      const structural = DATA.nodes.filter(n => n.kind === 'structural');
      const proven = DATA.nodes.filter(n => n.kind === 'proven');
      const showStructuralOnly = (filter === 'structural');
      const showCrossOnly = (filter === 'cross');

      const nodes = showStructuralOnly ? structural : DATA.nodes;
      const { positions, slotAngle, innerR, cx, cy } = layoutNodes(structural, showStructuralOnly ? [] : proven);

      // Slot cluster rings + label
      for (const [slot, ang] of slotAngle){
        const sx = cx + innerR * Math.cos(ang);
        const sy = cy + innerR * Math.sin(ang);
        svgEl('circle', { cx: sx, cy: sy, r: 38, fill:'none', stroke:'var(--rule)', 'stroke-width':0.5, 'stroke-dasharray':'2 4' }, svg);
        const t = svgEl('text', {
          x: sx, y: sy - 46,
          fill: 'var(--accent)', 'font-family':'JetBrains Mono', 'font-size':12, 'text-anchor':'middle',
        }, svg);
        t.textContent = slot;
      }

      // Edges
      for (const e of DATA.edges){
        if (showCrossOnly && e.kind !== 'cross_track') continue;
        if (showStructuralOnly && e.kind !== 'cross_track') continue;
        const a = positions.get(e.src), b = positions.get(e.tgt);
        if (!a || !b) continue;
        drawEdge(a, b, e.kind);
      }

      // Nodes
      for (const n of nodes){
        const p = positions.get(n.id);
        if (!p) continue;
        const g = svgEl('g', { transform:`translate(${p.x},${p.y})`, style:'cursor:pointer' }, svg);
        g.classList.add('tree-node');
        if (n.kind === 'structural'){
          const hue = hueFor(n.area);
          svgEl('circle', { r: 7, fill: `oklch(0.78 0.14 ${hue})`, stroke: 'var(--accent)', 'stroke-width': 0.8 }, g);
          // small label: track only (slot already in cluster ring)
          const t = svgEl('text', { x: 9, y: 3, fill: 'var(--ink-2)', 'font-family':'JetBrains Mono','font-size': 9 }, g);
          t.textContent = n.track;
        } else {
          const hue = hueFor(n.area);
          svgEl('circle', { r: 3.5, fill: `oklch(0.72 0.10 ${hue})`, stroke: 'var(--rule)', 'stroke-width': 0.4 }, g);
        }
        const title = svgEl('title', {}, g);
        title.textContent = `${n.id} · ${n.name || ''} · ${n.area || ''}`;
        g.addEventListener('click', () => {
          const ent = entityFor(n);
          bus.set({ selected: ent, selType: 'theorem' });
        });
      }

      hdr.textContent =
        `${DATA.summary.structural_nodes} structural · ${DATA.summary.proven_nodes} proven · ` +
        `${DATA.summary.cross_track_edges} cross-track edges`;
    }

    fetch('theorem_genealogy.json')
      .then(rsp => {
        if (!rsp.ok) throw new Error(`HTTP ${rsp.status}`);
        return rsp.json();
      })
      .then(json => {
        DATA = json;
        if (!DATA.nodes || !DATA.nodes.length){
          status.textContent = 'theorem_genealogy.json has no nodes; run build_theorem_genealogy.py';
          return;
        }
        root.querySelectorAll('button[data-f]').forEach(b => b.addEventListener('click', () => {
          filter = b.dataset.f;
          root.querySelectorAll('button[data-f]').forEach(x => x.classList.remove('primary'));
          b.classList.add('primary');
          render();
        }));
        window.addEventListener('resize', () => render());
        render();
      })
      .catch(err => {
        status.textContent = `could not load theorem_genealogy.json: ${err.message}. Run: tools/viz/console/build_theorem_genealogy.py`;
      });
  }

  // =================================================================
  // View 9 — Falsifier Gantt timeline
  // Rows from master_inventory.json (the AMRI-promoted falsifier-watchlist).
  // EVOI rank → row order (FLAGSHIP at top); detector window → bar extent.
  // Data: master_inventory.json (built by build_master_inventory.py).
  // =================================================================
  function buildGantt(root){
    root.innerHTML = `
      <div class="controls">
        <label>sort</label>
        <button data-sort="evoi" class="primary">by EVOI</button>
        <button data-sort="time">by data year</button>
      </div>
      <div class="legend">
        <div><b>EVOI ranking</b> — colored bars sorted by priority</div>
        <div style="margin-top:6px">
          <span class="sw" style="background:var(--gate-pass)"></span>FLAGSHIP
          <br><span class="sw" style="background:var(--gate-open)"></span>FLAGSHIP-JOINT / SECONDARY
          <br><span class="sw" style="background:var(--gate-diag)"></span>DERIVED / LONG-TERM
          <br><span class="sw" style="background:var(--ink-3)"></span>CONTINGENT
        </div>
        <div style="color:var(--ink-3);margin-top:6px">click bar → inspector</div>
      </div>
      <svg id="gtSvg" width="100%" height="100%" class="grid-bg"></svg>
      <div id="gtStatus" class="mono" style="position:absolute;left:16px;bottom:16px;color:var(--ink-3);font-size:11px"></div>
    `;
    const svg = root.querySelector('#gtSvg');
    const status = root.querySelector('#gtStatus');
    let DATA = null;
    let sortMode = 'evoi';

    // EVOI-class → bar fill (token-style; falls back to --ink-3)
    function evoiFill(cls){
      const k = (cls || '').toUpperCase();
      if (k.startsWith('FLAGSHIP-JOINT')) return 'var(--gate-open)';
      if (k.startsWith('FLAGSHIP'))       return 'var(--gate-pass)';
      if (k.startsWith('SECONDARY'))      return 'var(--gate-open)';
      if (k.startsWith('DERIVED'))        return 'var(--gate-diag)';
      if (k.startsWith('LONG-TERM'))      return 'var(--gate-diag)';
      if (k.startsWith('CONTINGENT'))     return 'var(--ink-3)';
      return 'var(--rule-hi)';
    }

    function viewBox(){
      const r = svg.getBoundingClientRect();
      svg.setAttribute('viewBox', `0 0 ${r.width} ${r.height}`);
      return r;
    }

    function render(){
      if (!DATA) return;
      clearChildren(svg);
      const r = viewBox();
      const padL = 200, padR = 60, padT = 56, padB = 40;
      const W = r.width - padL - padR;
      const H = r.height - padT - padB;
      const rows = DATA.rows.slice();
      if (sortMode === 'time'){
        rows.sort((a, b) => a.t_low - b.t_low || a.evoi_rank - b.evoi_rank);
      } else {
        rows.sort((a, b) => a.evoi_rank - b.evoi_rank || a.t_low - b.t_low);
      }
      const rowH = Math.max(20, H / Math.max(1, rows.length));

      // Time axis range — extends from minimum t_low - 0.5 to max t_high + 0.5,
      // but clamps to the present-2040 frame for stability.
      const tMin = Math.min(DATA.current_year - 0.5, ...rows.map(x => x.t_low));
      const tMax = Math.max(2040, ...rows.map(x => x.t_high));
      const xOf = t => padL + ((t - tMin) / (tMax - tMin)) * W;

      // Year grid + labels (every year)
      for (let y = Math.ceil(tMin); y <= Math.floor(tMax); y++){
        svgEl('line', {
          x1: xOf(y), x2: xOf(y),
          y1: padT - 8, y2: r.height - padB + 4,
          stroke: y === DATA.current_year ? 'var(--accent)' : '#1a1f29',
          'stroke-width': y === DATA.current_year ? 1 : 0.4,
          'stroke-dasharray': y === DATA.current_year ? '' : '2 4',
          opacity: y === DATA.current_year ? 0.9 : 0.6,
        }, svg);
        const label = svgEl('text', {
          x: xOf(y), y: padT - 14,
          fill: y === DATA.current_year ? 'var(--accent)' : 'var(--ink-3)',
          'font-family':'JetBrains Mono','font-size': 9.5, 'text-anchor':'middle',
        }, svg);
        label.textContent = String(y);
      }
      // "now" caption
      svgEl('text', {
        x: xOf(DATA.current_year), y: padT - 26,
        fill: 'var(--accent)','font-family':'JetBrains Mono','font-size':10, 'text-anchor':'middle',
      }, svg).textContent = 'now';

      // Header strip: column titles
      svgEl('text', {
        x: 16, y: padT - 14,
        fill: 'var(--ink-3)','font-family':'JetBrains Mono','font-size': 10,
      }, svg).textContent = 'PREDICTION';
      svgEl('text', {
        x: 90, y: padT - 14,
        fill: 'var(--ink-3)','font-family':'JetBrains Mono','font-size': 10,
      }, svg).textContent = 'EVOI';

      // Rows
      rows.forEach((row, i) => {
        const y = padT + i * rowH + rowH * 0.5;

        // Row label (prediction id)
        const lbl = svgEl('text', {
          x: 16, y: y + 3,
          fill: 'var(--ink)', 'font-family':'JetBrains Mono','font-size': 11,
        }, svg);
        lbl.textContent = row.prediction_id;

        // EVOI rank tag
        const tag = svgEl('text', {
          x: 90, y: y + 3,
          fill: evoiFill(row.evoi_class), 'font-family':'JetBrains Mono','font-size': 10,
        }, svg);
        tag.textContent = (row.evoi_class || '').split(/[\s(/]/, 1)[0] || '—';

        // Detector micro-text under the prediction id
        const det = svgEl('text', {
          x: 16, y: y + 14,
          fill: 'var(--ink-3)', 'font-family':'JetBrains Mono','font-size': 9,
        }, svg);
        det.textContent = (row.detector || '').slice(0, 26);

        // Row separator
        svgEl('line', {
          x1: padL, x2: r.width - padR,
          y1: y - rowH * 0.5 + 2, y2: y - rowH * 0.5 + 2,
          stroke: '#181c24', 'stroke-width': 0.5,
        }, svg);

        // The Gantt bar
        const x0 = xOf(row.t_low);
        const x1 = xOf(row.t_high);
        const barH = Math.min(16, rowH * 0.5);
        const fill = evoiFill(row.evoi_class);
        const g = svgEl('g', { style: 'cursor:pointer' }, svg);
        g.classList.add('tree-node');
        const rect = svgEl('rect', {
          x: x0, y: y - barH/2, width: Math.max(8, x1 - x0), height: barH,
          rx: 2, fill, opacity: 0.85,
          stroke: 'var(--rule)', 'stroke-width': 0.6,
        }, g);
        // sigma label inside/right of bar
        const sigmaLbl = svgEl('text', {
          x: x1 + 6, y: y + 3,
          fill: 'var(--ink-2)', 'font-family':'JetBrains Mono','font-size':10,
        }, svg);
        sigmaLbl.textContent = (row.sigma_distance || '').slice(0, 18);

        // Tooltip + click
        const title = svgEl('title', {}, g);
        title.textContent =
          `${row.prediction_id}  ·  ${row.evoi_class}\n` +
          `prediction: ${row.framework_prediction}\n` +
          `detector:  ${row.detector}\n` +
          `window:    ${row.t_low.toFixed(1)} – ${row.t_high.toFixed(1)}\n` +
          `σ-dist:    ${row.sigma_distance || '—'}\n` +
          `xcorr:     ${row.xcorr_class || '—'}\n` +
          `gate:      ${row.framework_gate || '—'}`;
        g.addEventListener('click', () => {
          // Synthesize an open-channel-shaped record so the existing
          // inspector card type renders cleanly.
          const synth = {
            id:      `inv:${row.prediction_id}`,
            name:    `${row.prediction_id}  (${row.evoi_class})`,
            detail:  `Detector: ${row.detector}\nWindow: ${row.data_year || `${row.t_low.toFixed(1)}–${row.t_high.toFixed(1)}`}\nσ-distance: ${row.sigma_distance}\nPrediction: ${row.framework_prediction}`,
            status:  `${row.status}  ·  xcorr: ${row.xcorr_class || 'N/A'}`,
            session: row.framework_gate || '—',
          };
          bus.set({ selected: synth, selType: 'open' });
        });
      });

      status.textContent =
        `${DATA.rows.length} rows · ${DATA.source} · sorted by ${sortMode === 'evoi' ? 'EVOI rank' : 'data year'}`;
    }

    fetch('master_inventory.json')
      .then(rsp => {
        if (!rsp.ok) throw new Error(`HTTP ${rsp.status}`);
        return rsp.json();
      })
      .then(json => {
        DATA = json;
        if (!DATA.rows || !DATA.rows.length){
          status.textContent = 'master_inventory.json has no rows; run build_master_inventory.py';
          return;
        }
        root.querySelectorAll('button[data-sort]').forEach(b => b.addEventListener('click', () => {
          sortMode = b.dataset.sort;
          root.querySelectorAll('button[data-sort]').forEach(x => x.classList.remove('primary'));
          b.classList.add('primary');
          render();
        }));
        window.addEventListener('resize', () => render());
        render();
      })
      .catch(err => {
        status.textContent = `could not load master_inventory.json: ${err.message}. Run: tools/viz/console/build_master_inventory.py`;
      });
  }

  // =================================================================
  // Expose
  // =================================================================
  window.AE_VIEWS = { buildBell, buildSpiral, buildAtlas, buildLibrary, buildGraph, buildBedrock, buildFanout, buildPlanStateDiff, buildGenealogy, buildTheoremTracks, buildGantt, buildInspector, buildTrajectory, buildWordmap };
})();
