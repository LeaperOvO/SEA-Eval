import json, random, re

path = '/Users/malipeng/agent-test/eval/index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract TASKS JSON
match = re.search(r'const TASKS = (\[.*?\]);\s*\nconst AGENTS', content, re.DOTALL)
tasks = json.loads(match.group(1))

AGENTS = [
    {"id": "generic_agent", "name": "GenericAgent", "color": "#667eea"},
    {"id": "openclaw", "name": "OpenClaw", "color": "#38a169"},
    {"id": "claude_code", "name": "ClaudeCode", "color": "#d69e2e"},
    {"id": "codex", "name": "Codex", "color": "#e53e3e"},
]

random.seed(42)

def gen_results_for_task():
    results = {}
    for agent in AGENTS:
        base_tokens = random.randint(8000, 25000)
        
        # Setting 1: AAA (identical repetition) - 3 runs of task A
        aaa_runs = []
        t = base_tokens
        for run in range(3):
            completed = random.random() > 0.15
            aaa_runs.append({"tokens": t, "completed": completed})
            t = int(t * random.uniform(0.7, 0.95))
        
      nce) - run A, B, C
        t = base_tokens
        abc_runs = []
        for _ in range(3):
            completed = random.random() > 0.2
            variation = random.uniform(0.75, 1.1)
            abc_runs.append({"tokens": int(t * variation), "completed": completed})
            t = int(t * random.uniform(0.8, 1.0))
        
        # Setting 3: Orthogonal (A -> [3 other tasks] -> A)
        first_a_tokens = base_tokens
        first_a_completed = random.random() > 0.15
        second_a_tokens = int(base_tokens * random.uniform(0.6, 1.05))
        second_a_completed = random.random() > 0.1
        orthogonal = {
            "first_a": {"tokens": first_a_tokens, "completed": first_a_completed},
            "second_a": {"tokens": second_a_tokens, "completed": second_a_completed}
        }
        
        results[agent['id']] = {
            "aaa": aaa_runs,
            "abc": abc_runs,
            "orthogonal": orthogonal
        }
    return results

for task in tasks:
    task['results'] = gen_results_for_task()

# Build CSS
css = """:root{--bg:#f7fafc;--bg2:#edf2f7;--card:#ffffff;--card-hover:#f0f4f8;--accent:#667eea;--accent2:#764ba2;--cyan:#4299e1;--text:#1a202c;--text2:#4a5568;--muted:#718096;--border:#e2e8f0;--tag-bg:rgba(102,126,234,0.1);--tag-text:#667eea;--green:#38a169;--yellow:#d69e2e;--red:#e53e3e}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Inter',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;min-height:100vh}
.header{background:linear-gradient(135deg,#667eea,#764ba2);padding:60px 20px;text-align:center}
.header h1{font-size:2.5rem;font-weight:700;color:#ffffff;margin-bottom:8px}
.header p{color:rgba(255,255,255,0.9);font-size:1.05rem;max-width:750px;margin:0 auto}
.header .subtitle{color:rgba(255,255,255,0.75);font-size:0.9rem;margin-top:8px;max-width:800px;margin-left:auto;margin-right:auto}
.stats{display:flex;justify-content:center;gap:40px;margin-top:30px;flex-wrap:wrap}
.stat{text-align:center}.stat-num{font-size:2rem;font-weight:700;color:#ffffff}.stat-label{font-size:0.85rem;color:rgba(255,255,255,0.8)}
.container{max-width:1200px;margin:0 auto;padding:40px 20px}

/* Section titles */
.section-title{font-size:1.3rem;font-weight:600;color:var(--text);margin:30px 0 16px;padding-left:12px;border-left:4px solid var(--accent)}

/* Leaderboard */
.leaderboard{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:30px;margin-bottom:40px;box-shadow:0 2px 8px rgba(0,0,0,0.06)}
.leaderboard h2{font-size:1.3rem;font-weight:600;color:var(--text);margin-bottom:20px;display:flex;align-items:center;gap:10px}
.lb-table{width:100%;border-collapse:collapse}
.lb-table th{text-align:left;padding:12px 16px;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.5px;color:var(--muted);border-bottom:2px solid var(--border)}
.lb-table td{padding:12px 16px;border-bottom:1px solid var(--border);font-size:0.9rem}
.lb-table tr:last-child td{border-bottom:none}
.lb-rank{font-weight:700;color:var(--accent);font-size:1.1rem;width:40px}
.lb-agent{font-weight:600;display:flex;align-items:center;gap:10px}
.lb-dot{width:10px;height:10px;border-radius:50%;display:inline-block}
.lb-score{font-weight:700;font-size:1.05rem}
.lb-bar{height:8px;border-radius:4px;background:var(--bg2);overflow:hidden;min-width:120px}
.lb-bar-fill{height:100%;border-radius:4px;transition:width 0.6s}

/* Eval framework explanation */
.framework{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:24px 30px;margin-bottom:30px;box-shadow:0 2px 8px rgba(0,0,0,0.06)}
.framework h3{font-size:1.1rem;font-weight:600;margin-bottom:16px;color:var(--text)}
.fw-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.fw-card{background:var(--bg2);border-radius:10px;padding:16px 20px;border:1px solid var(--border)}
.fw-card h4{font-size:0.9rem;font-weight:600;color:var(--accent);margin-bottom:6px}
.fw-card p{font-size:0.82rem;color:var(--text2);line-height:1.5}
.fw-card .fw-flow{font-family:monospace;font-size:0.8rem;color:var(--accent2);margin-top:6px;background:rgba(102,126,234,0.08);padding:4px 8px;border-radius:4px;display:inline-block}

/* Task cards */
.task-card{background:var(--card);border:1px solid var(--border);border-radius:12px;margin-bottom:20px;overflow:hidden;transition:all 0.3s;box-shadow:0 2px 8px rgba(0,0,0,0.06)}
.task-card:hover{border-color:var(--accent);transform:translateY(-1px);box-shadow:0 6px 20px rgba(102,126,234,0.12)}
.card-header{padding:20px 24px;cursor:pointer;display:flex;align-items:center;gap:16px}
.task-icon{font-size:1.8rem;width:48px;height:48px;display:flex;align-items:center;justify-content:center;background:var(--tag-bg);border-radius:12px}
.task-info{flex:1}
.task-num{font-size:0.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:2px}
.task-title-cn{font-size:1.05rem;font-weight:600;color:var(--text)}
.task-title-en{font-size:0.82rem;color:var(--text2);margin-top:2px}
.tags{display:flex;gap:6px;flex-wrap:wrap;margin-top:6px}
.tag{background:var(--tag-bg);color:var(--tag-text);padding:3px 9px;border-radius:20px;font-size:0.72rem;font-weight:500}
.chevron{color:var(--muted);font-size:1.1rem;transition:transform 0.3s}.chevron.open{transform:rotate(180deg)}

.card-body{display:none;padding:0 24px 24px;border-top:1px solid var(--border)}
.card-body.open{display:block}

/* Setting tabs */
.setting-tabs{display:flex;gap:8px;margin:16px 0 12px}
.stab{padding:8px 16px;border-radius:8px;background:var(--bg2);color:var(--text2);cursor:pointer;font-size:0.82rem;border:1px solid var(--border);transition:all 0.2s;font-weight:500}
.stab.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.setting-content{display:none;margin-top:12px}
.setting-content.active{display:block}

/* Setting description */
.setting-desc{font-size:0.82rem;color:var(--text2);margin-bottom:16px;padding:10px 14px;background:var(--bg2);border-radius:8px;border-left:3px solid var(--accent)}

/* Task question display */
.task-questions{margin-bottom:16px}
.tq-item{margin-bottom:8px}
.tq-label{font-size:0.72rem;font-weight:600;color:var(--accent);ting:0.5px}
.tq-text{font-size:0.85rem;color:var(--text);margin-top:2px;line-height:1.6;max-height:120px;overflow-y:auto;white-space:pre-wrap}

/* Results table */
.results-table{width:100%;border-collapse:collapse;background:var(--card);border-radius:8px;overflow:hidden;border:1px solid var(--border);font-size:0.85rem}
.results-table th{padding:10px 12px;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.5px;color:var(--muted);background:var(--bg);border-bottom:1px solid var(--border);text-align:center}
.results-table th:first-child{text-align:left}
.results-table td{padding:10px 12px;text-align:center;border-bottom:1px solid var(--border)}
.results-table td:first-child{text-align:left;font-weight:600}
.results-table tr:last-child td{border-bottom:none}
.results-table tr:hover{background:var(--bg)}

.agent-badge{display:inline-flex;align-items:center;gap:6px}
.agent-dot{width:8px;height:8px;border-radius:50%;display:inline-block}

.token-val{font-weight:600;font-family:'SF Mono',monospace;font-size:0.82rem}
.token-down{color:var(--green)}
.token-up{color:var(--red)}
.token-same{color:var(--text2)}
.completed{color:var(--green);font-weight:600}
.failed{color:var(--red);font-weight:600}
.delta{font-size:0.72rem;margin-left:4px}
.delta-good{color:var(--green)}
.delta-bad{color:var(--red)}

@media(max-width:768px){.header h1{font-size:1.8rem}.stats{gap:20px}.card-header{flex-wrap:wrap}.fw-grid{grid-template-columns:1fr}.results-table{font-size:0.75rem}}
"""

tasks_json = json.dumps(tasks, ensure_ascii=False)
agents_json = json.dumps(AGENTS, ensure_ascii=False)

js_code = """
const TASKS = __TASKS__;
const AGENTS = __AGENTS__;
const app = document.getElementById('app');

function esc(s){const d=document.createElement('div');d.textContent=s;return d.innerHTML;}
function fmtTokens(n){return n>=10000?(n/1000).toFixed(1)+'k':n.toLocaleString();}
function tokenDelta(before,after){
  const pct=((after-before)/before*100).toFixed(0);
  if(pct<-5) return '<span class="delta delta-good">'+pct+'%</span>';
  if(pct>5) return '<span class="delta delta-bad">+'+pct+'%</span>';
  return '<span class="delta">'+pct+'%</span>';
}
function statusIcon(completed){return completed?'<span class="completed">✓</span>':'<span class="failed">✗</span>';}

function renderFramework(){
  return `<div class="framework">
    <h3>📐 Evaluation Framework: Agent Self-Evolution</h3>
    <div class="fw-grid">
      <div class="fw-card">
        <h4>Setting 1: Identical Repetition (AAA)</h4>
        <p>Run the same main task A three times consecutively. Measures learning from identical experience.</p>
        <div class="fw-flow">A → A → A</div>
      </div>
      <div class="fw-card">
        <h4>Setting 2: Similar Sequence (ABC)</h4>
        <p>Run main task A, then similar tasks B and C. Measures transfer learning across similar tasks.</p>
        <div class="fw-flow">A → B → C</div>
      </div>
      <div class="fw-card">
        <h4>Setting 3: Orthogonal Sequence (A…A)</h4>
        <p>Run task A, then 3 unrelated tasks, then task A again. Measures retention after distraction.</p>
        <div class="fw-flow">A → [X₁, X₂, X₃] → A</div>
      </div>
    </div>
  </div>`;
}

function renderLeaderboard(){
  // Calculate evolution score: avg token reduction + completion rate
  let agentScores = {};
  AGENTS.forEach(a=>{agentScores[a.id]={tokenReduction:0,completionRate:0,count:0};});
  
  TASKS.forEach(t=>{
    AGENTS.forEach(a=>{
      const r=t.results[a.id];
      if(!r) return;
      // AAA token reduction
      if(r.aaa.length>=3){
        const reduction = 1 - r.aaa[2].tokens/r.aaa[0].tokens;
        agentScores[a.id].tokenReduction += reduction;
      }
      // Completion rate across all runs
      const allRuns = [...r.aaa, ...r.abc, r.orthogonal.first_a, r.orthogonal.second_a];
      const completed = allRuns.filter(x=>x.completed).length;
      agentScores[a.id].completionRate += completed/allRuns.length;
      agentScores[a.id].count++;
    });
  });
  
  let rankings = AGENTS.map(a=>{
    const s=agentScores[a.id];
    const avgReduction = s.count>0 ? s.tokenReduction/s.count : 0;
    const avgCompletion = s.count>0 ? s.completionRate/s.count : 0;
    const evolution = (avgReduction*0.5 + avgCompletion*0.5);
    return {...a, avgReduction, avgCompletion, evolution};
  }).sort((a,b)=>b.evolution-a.evolution);

  let h='<div class="leaderboard"><h2>🏆 Evolution Leaderboard</h2>';
  h+='<table class="lb-table"><thead><tr><th>Rank</th><th>Agent</th><th>Avg Token Reduction</th><th>Completion Rate</th><th>Evolution Score</th></tr></thead><tbody>';
  rankings.forEach((r,i)=>{
    h+='<tr>';
    h+='<td class="lb-rank">#'+(i+1)+'</td>';
    h+='<td><span class="lb-agent"><span class="lb-dot" style="background:'+r.color+'"></span>'+r.name+'</span></td>';
    h+='<td class="token-down">'+(r.avgReduction*100).toFixed(1)+'%</td>';
    h+='<td>'+(r.avgCompletion*100).toFixed(1)+'%</td>';
    h+='<td class="lb-score">'+(r.evolution*100).toFixed(1)+'</td>';
    h+='</tr>';
  });
  h+='</tbody></table></div>';
  return h;
}

function renderTaskCard(t,i){
  let h='<div class="task-card" id="task-'+t.num+'">';
  h+='<div class="card-header" onclick="toggle('+i+')">';
  h+='<div class="task-icon">'+t.icon+'</div>';
  h+='<div class="task-info">';
  h+='<div class="task-num">Task Group '+String(t.num).padStart(2,'0')+'</div>';
  h+='<div class="task-title-cn">'+esc(t.title_cn)+'</div>';
  h+='<div class="task-title-en">'+esc(t.title_en)+'</div>';
  h+='<div class="tags">'+t.tags.map(tg=>'<span class="tag">'+esc(tg)+'</span>').join('')+'</div>';
  h+='</div><span class="chevron" id="chev-'+i+'">&#9660;</span></div>';
  
  h+='<div class="card-body" id="body-'+i+'">';
  
  // Task questions (A, B, C)
  h+='<div class="task-questions">';
  t.variants.forEach(v=>{
    const label = v.id==='A'?'Main Task (A)':'Similar Task ('+v.id+')';
    h+='<div class="tq-item"><div class="tq-label">'+label+'</div>';
    h+='<div class="tq-text">'+esc(v.question_cn)+'</div></div>';
  });
  h+='</div>';
  
  // Setting tabs
  h+='<div class="setting-tabs">';
  h+='<div class="stab active" onclick="switchSetting('+i+',0)">AAA Repetition</div>';
  h+='<div class="stab" onclick="switchSetting('+i+',1)">ABC Similar</div>';
  h+='<div class="stab" onclick="switchSetting('+i+',2)">Orthogonal A…A</div>';
  h+='</div>';
  
  // Setting 1: AAA
  h+='<div class="setting-content active" id="sc-'+i+'-0">';
  h+='<div class="setting-desc">Run task A three times. Observe token consumption reduction and completion consistency.</div>';
  h+='<table class="results-table"><thead><tr><th>Agent</th><th>Run 1 (A)</th><th>Run 2 (A)</th><th>Run 3 (A)</th><th>Total Reduction</th></tr></thead><tbody>';
  AGENTS.forEach(a=>{
    const r=t.results[a.id].aaa;
    const reduction = ((1-r[2].tokens/r[0].tokens)*100).toFixed(0);
    h+='<tr>';
    h+='<td><span class="agent-badge"><span class="agent-dot" style="background:'+a.color+'"></span>'+a.name+'</span></td>';
    r.forEach((run,ri)=>{
      const cls = ri>0?(run.tokens<r[ri-1].tokens?'token-down':'token-up'):'token-same';
      h+='<td><span class="token-val '+cls+'">'+fmtTokens(run.tokens)+'</span> '+statusIcon(run.completed);
      if(ri>0) h+=tokenDelta(r[ri-1].tokens,run.tokens);
      h+='</td>';
    });
    h+='<td><span class="delta-good" style="font-weight:700;font-size:0.9rem">-'+reduction+'%</span></td>';
    h+='</tr>';
  });
  h+='</tbody></table></div>';
  
  // Setting 2: ABC
  h+='<div class="setting-content" id="sc-'+i+'-1">';
  h+='<div class="setting-desc">Run mand C. Observe cross-task transfer efficiency.</div>';
  h+='<table class="results-table"><thead><tr><th>Agent</th><th>Task A</th><th>Task B</th><th>Task C</th></tr></thead><tbody>';
  AGENTS.forEach(a=>{
    const r=t.results[a.id].abc;
    h+='<tr>';
    h+='<td><span class="agent-badge"><span class="agent-dot" style="background:'+a.color+'"></span>'+a.name+'</span></td>';
    r.forEach((run,ri)=>{
      const cls = ri>0?(run.tokens<r[0].tokens?'token-down':'token-up'):'token-same';
      h+='<td><span class="token-val '+cls+'">'+fmtTokens(run.tokens)+'</span> '+statusIcon(run.completed);
      if(ri>0) h+=tokenDelta(r[0].tokens,run.tokens);
      h+='</td>';
    });
    h+='</tr>';
  });
  h+='</tbody></table></div>';
  
  // Setting 3: Orthogonal
  h+='<div class="setting-content" id="sc-'+i+'-2">';
  h+='<div class="setting-desc">Run task A, then 3 unrelated tasks as interference, then run task A again. Measures knowledge retention.</div>';
  h+='<table class="results-table"><thead><tr><th>Agent</th><th>First A</th><th>Interference</th><th>Second A</th><th>Retention</th></tr></thead><tbody>';
  AGENTS.forEach(a=>{
    const r=t.results[a.id].orthogonal;
    const retention = ((1-r.second_a.tokens/r.first_a.tokens)*100).toFixed(0);
    const retCls = r.second_a.tokens<=r.first_a.tokens?'delta-good':'delta-bad';
    h+='<tr>';
    h+='<td><sund:'+a.color+'"></span>'+a.name+'</span></td>';
    h+='<td><span class="token-val">'+fmtTokens(r.first_a.tokens)+'</span> '+statusIcon(r.first_a.completed)+'</td>';
    h+='<td style="color:var(--muted);font-style:italic">3 orthogonal tasks</td>';
    h+='<td><span class="token-val '+(r.second_a.tokens<r.first_a.tokens?'token-down':'token-up')+'">'+fmtTokens(r.second_a.tokens)+'</span> '+statusIcon(r.second_a.completed)+tokenDelta(r.first_a.tokens,r.second_a.tokens)+'</td>';
    h+='<td><span class="'+retCls+'" style="font-weight:700">'+(r.second_a.tokens<=r.first_a.tokens?'-':'+')+(Math.abs(retention))+'%</span></td>';
    h+='</tr>';
  });
  h+='</tbody></table></div>';
  
  h+='</div></div>';
  return h;
}

function render(){
  let h = renderFramework();
  h += renderLeaderboard();
  h += '<div class="section-title">Task Groups</div>';
  TASKS.forEach((t,i)=>{h+=renderTaskCard(t,i);});
  app.innerHTML = h;
}

function toggle(i){
  const b=document.getElementById('body-'+i);
  const c=document.getElementById('chev-'+i);
  b.classList.toggle('open');c.classList.toggle('open');
}
function switchSetting(ti,si){
  const card=document.getElementById('task-'+TASKS[ti].num);
  card.querySelectorAll('.stab').forEach((t,idx)=>t.classList.toggle('active',idx===si));
  card.querySelectorAll('.setting-content').forEach((c,idx)=>c.classList.toggle('active',idx===si));
}
render();
""".replace('__TASKS__', tasks_json).replace('__AGENTS__', agents_json)

# Build final HTML
html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SEA Benchmark - Agent Self-Evolution Evaluation</title>
<style>
{css}
</style>
</head>
<body>
<div class="header">
<h1>SEA Benchmark</h1>
<p>Situational Evaluation of Agents — 12 Real-World Task Groups with 36 Variants</p>
<div class="subtitle">Evaluating Agent Self-Evolution: Learning from Repetition, Transfer across Similar Tasks, and Retention through Interference</div>
<div class="stats">
<div class="stat"><div class="stat-num">12</div><div class="stat-label">Task Groups</div></div>
<div class="stat"><div class="stat-num">3</div><div class="stat-label">Eval Settings</div></div>
<tat-num">4</div><div class="stat-label">Agents</div></div>
<div class="stat"><div class="stat-num">36</div><div class="stat-label">Total Variants</div></div>
</div>
</div>
<div class="container" id="app"></div>
<script>
{js_code}
</script>
</body>
</html>"""

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done! File size: {len(html)} bytes, {html.count(chr(10))} lines")