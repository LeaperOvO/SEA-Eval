#!/usr/bin/env python3
import json, os

OUT = "/Users/malipeng/agent-test/eval"
with open(os.path.join(OUT, "tasks_data.json"), "r") as f:
    tasks = json.load(f)

icons = ["\U0001F517","\u2708\uFE0F","\U0001F4CA","\U0001F9EC","\U0001F393","\U0001F6E1\uFE0F","\U0001F4B0","\U0001F3AE","\U0001F331","\U0001F3DB\uFE0F","\U0001F697","\U0001F5A5\uFE0F"]

tags_map = {
    1: ["Supply Chain", "Dependency Analysis", "Open Source"],
    2: ["Multi-Constraint", "Real-time Info", "Route Optimization"],
    3: ["Financial Report", "Data Extraction", "Competitor Analysis"],
    4: ["Paper Reproduction", "Code Implementation", "Algorithm"],
    5: ["Academic Search", "Impact Assessment", "Citation Analysis"],
    6: ["Security", "CVE Analysis", "Risk Assessment"],
    7: ["Funding Analysis", "Business Insight", "Market Analysis"],
    8: ["Game Review", "Multi-source", "Sentiment Analysis"],
    9: ["ESG Report", "Sustainability", "Compliance"],
    10: ["Cultural Heritage", "Conservation", "Multi-dimensional"],
    11: ["Chip Comparison", "Tech Assessment", "Industry Analysis"],
    12: ["Supercomputer", "Performance", "Energy Efficiency"],
}

en_titles = {
    1: "Supply Chain Security Audit",
    2: "Multi-Constraint Travel Planning",
    3: "Semiconductor Financial Analysis",
    4: "AI Paper Reproduction",
    5: "Academic Impact Assessment",
    6: "CVE Vulnerability Analysis",
    7: "Startup Funding Analysis",
    8: "Game Review Aggregation",
    9: "ESG Report Analysis",
    10: "UNESCO Heritage Assessment",
    11: "Autonomous Driving Chip Comparison",
    12: "Supercomputer TOP500 Analysis",
}

focus_map = {
    1: "Multi-source dependency parsing, version conflict detection, security vulnerability correlation",
    2: "Multi-constraint satisfaction, real-time data retrieval, solution optimization",
    3: "Structured data extraction, cross-period comparison, financial metric calculation",
    4: "Paper comprehension, code implementation, experiment reproduction",
    5: "Academic database search, metric calculation, trend analysis",
    6: "Vulnerability technical analysis, impact assessment, remediation generation",
    7: "Business information aggregation, valuation analysis, investment logic",
    8: "Multi-platform data collection, score normalization, opinion synthesis",
    9: "ESG framework understanding, quantitative metric extraction, compliance judgment",
    10: "Multi-dimensional assessment, historical data integration, conservation recommendations",
    11: "Technical spec comparison, performance benchmarking, roadmap evaluation",
    12: "Ranking data analysis, multi-dimensional comparison, trend prediction",
}

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def gen_html():
    total_variants = sum(len(t.get("variants",[])) for t in tasks)
    lines = []
    lines.append("<!DOCTYPE html>")
    lines.append('<html lang="zh-CN"><head>')
    lines.append('<meta charset="UTF-8">')
    lines.append('<meta name="viewport" content="width=device-width,initial-scale=1.0">')
    lines.append('<title>SEA Benchmark - Self-Evolving Agent Evaluation</title>')
    lines.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
    lines.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    lines.append('<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')
    lines.append("<style>")
    lines.append(get_css())
    lines.append("</style></head><body>")
    
    # Header
    lines.append('<header class="header"><div class="header-content">')
    lines.append('<h1>SEA Benchmark</h1>')
    lines.append('<p class="subtitle">Self-Evolving Agent Evaluation</p>')
    lines.append('<p class="desc">A comprehensive benchmark for evaluating AI agents\' ability to self-evolve through complex, real-world research tasks across 12 domains.</p>')
    lines.append('<div class="stats-bar">')
    lines.append('<div class="stat-item"><div class="stat-num">'+str(len(tasks))+'</div><div class="stat-label">Task Groups</div></div>')
    lines.append('<div class="stat-item"><div class="stat-num">'+str(total_variants)+'</div><div class="stat-label">Total Variants</div></div>')
    lines.append('<div class="stat-item"><div class="stat-num">6</div><div class="stat-label">Capability Axes</div></div>')
    lines.append('</div></div></header>')
    
    # Main grid
    lines.append('<main class="container"><div class="task-grid" id="taskGrid">')
    
    for i, task in enumerate(tasks):
        tid = i + 1
        icon = icons[i] if i < len(icons) else "?"
        tags = tags_map.get(tid, [])
        en_title = en_titles.get(tid, "")
        focus = focus_map.get(tid, "")
        
        lines.append('<div class="task-card" data-task="'+str(tid)+'" onclick="toggleCard(this)">')
        lines.append('<div class="task-card-header">')
        lines.append('<div class="task-icon">'+icon+'</div>')
        lines.append('<div class="task-info">')
        lines.append('<div class="task-num">TASK '+str(tid).zfill(2)+'</div>')
        lines.append('<div class="task-title">'+esc(task["title"])+'</div>')
        lines.append('<div class="task-title-en">'+en_title+'</div>')
        lines.append('</div></div>')
        
        # Tags
        lines.append('<div class="task-tags">')
        for tag in tags:
            lines.append('<span class="tag">'+tag+'</span>')
        lines.append('</div>')
        
        # Expanded section
        lines.append('<div class="task-expanded">')
        lines.append('<button class="close-btn" onclick="event.stopPropagation();closeCard(this)">&times;</button>')
        lines.append('<div class="focus-text"><strong>\U0001F3AF '+focus+'</strong></div>')
        
        # Variant tabs
        variants = task.get("variants", [])
        lines.append('<div class="variant-tabs">')
        for vi, v in enumerate(variants):
            cls = "variant-tab active" if vi == 0 else "variant-tab"
            label = v.get("label", "Variant "+str(vi+1))
            lines.append('<div class="'+cls+'" data-variant="'+str(vi)+'" onclick="event.stopPropagation();switchVariant(this,'+str(vi)+')">'+esc(label)+'</div>')
        lines.append('</div>')
        
        # Variant contents
        for vi, v in enumerate(variants):
            cls = "variant-content active" if vi == 0 else "variant-content"
            lines.append('<div class="'+cls+'" data-variant="'+str(vi)+'">')
            
            q = v.get("question", "")
            lines.append('<div class="question-section">')
            lines.append('<div class="section-label">TASK DESCRIPTION</div>')
            lines.append('<div class="question-text">'+esc(q)+'</div>')
            lines.append('</div>')
            
            ofmt = v.get("output_format", "")
            if ofmt:
                lines.append('<div class="question-section">')
                lines.append('<div class="section-label">OUTPUT FORMAT</div>')
                lines.append('<div class="output-format">'+esc(ofmt)+'</div>')
                lines.append('</div>')
            
            lines.append('<div class="results-section">')
            lines.append('<div class="results-title">\U0001F4C8 Evaluation Results</div>')
            lines.append('<p class="result-pending">\u23F3 Results pending - evaluation in progress...</p>')
            lines.append('</div>')
            lines.append('</div>')
        
        lines.append('</div>')  # task-expanded
        lines.append('</div>')  # task-card
    
    lines.append('</div></main>')
    
    # Footer
    lines.append('<footer class="footer">')
    lines.append('<p>SEA Benchmark &copy; 2024 | Self-Evolving Agent Evaluation</p>')
    lines.append('<p style="margin-top:8px">Evaluating AI agents across 12 real-world research domains with 36 task variants</p>')
    lines.append('</footer>')
    
    # JavaScript
    lines.append("<script>")
    lines.append(get_js())
    lines.append("</script></body></html>")
    
    return "\n".join(lines)

def get_css():
    css = ""
    css += ":root{--bg-primary:#0f0f23;--bg-secondary:#1a1a2e;--bg-card:#16213e;--bg-card-hover:#1a2744;"
    css += "--accent-1:#6366f1;--accent-2:#8b5cf6;--accent-3:#06b6d4;"
    css += "--text-primary:#e2e8f0;--text-secondary:#94a3b8;--text-muted:#64748b;"
    css += "--border:#334155;--tag-bg:rgba(99,102,241,0.15);--tag-text:#a5b4fc;"
    css += "--success:#10b981;--warning:#f59e0b;--danger:#ef4444;"
    css += "--radius:12px;--radius-sm:8px;--shadow:0 4px 24px rgba(0,0,0,0.3)}"
    css += "*{margin:0;padding:0;box-sizing:border-box}"
    css += "body{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg-primary);color:var(--text-primary);line-height:1.6;min-height:100vh}"
    css += ".header{background:linear-gradient(135deg,#1e1b4b 0%,#312e81 30%,#4c1d95 70%,#1e1b4b 100%);padding:60px 20px;text-align:center;position:relative;overflow:hidden}"
    css += ".header::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:radial-gradient(ellipse at 50% 0%,rgba(99,102,241,0.15) 0%,transparent 70%)}"
    css += ".header-content{position:relative;z-index:1;max-width:800px;margin:0 auto}"
    css += ".header h1{font-size:3rem;font-weight:700;background:linear-gradient(135deg,#c7d2fe,#a5b4fc,#818cf8);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:12px;letter-spacing:-0.5px}"
    css += ".header .subtitle{font-size:1.15rem;color:#a5b4fc;font-weight:400;margin-bottom:8px}"
    css += ".header .desc{font-size:0.95rem;color:var(--text-secondary);max-width:600px;margin:0 auto}"
    css += ".stats-bar{display:flex;justify-content:center;gap:40px;margin-top:30px;flex-wrap:wrap}"
    css += ".stat-item{text-align:center}"
    css += ".stat-num{font-size:2rem;font-weight:700;color:#c7d2fe}"
    css += ".stat-label{font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px}"
    css += ".container{max-width:1200px;margin:0 auto;padding:40px 20px}"
    css += ".task-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:20px}"
    css += ".task-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;transition:all 0.3s ease;cursor:pointer;animation:fadeIn 0.4s ease forwards;opacity:0}"
    css += "@keyframes fadeIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}"
    for i in range(1,13):
        css += ".task-card:nth-child("+str(i)+"){animation-delay:"+str((i-1)*0.05)+"s}"
    css += ".task-card:hover{background:var(--bg-card-hover);border-color:var(--accent-1);transform:translateY(-2px);box-shadow:var(--shadow)}"
    css += ".task-card.expanded{grid-column:1/-1;cursor:default;transform:none}"
    css += ".task-card.expanded:hover{transform:none}"
    css += ".task-card-header{padding:20px 24px;display:flex;align-items:flex-start;gap:16px}"
    css += ".task-icon{font-size:2rem;flex-shrink:0;width:48px;height:48px;display:flex;align-items:center;justify-content:center;background:rgba(99,102,241,0.1);border-radius:var(--radius-sm)}"
    css += ".task-info{flex:1;min-width:0}"
    css += ".task-num{font-size:0.7rem;text-transform:uppercase;letter-spacing:1.5px;color:var(--accent-3);font-weight:600;margin-bottom:4px}"
    css += ".task-title{font-size:1.05rem;font-weight:600;color:var(--text-primary);margin-bottom:4px;line-height:1.4}"
    css += ".task-title-en{font-size:0.8rem;color:var(--text-muted);font-weight:400}"
    css += ".task-tags{display:flex;flex-wrap:wrap;gap:6px;padding:0 24px 16px}"
    css += ".tag{font-size:0.7rem;padding:3px 10px;border-radius:20px;background:var(--tag-bg);color:var(--tag-text);font-weight:500}"
    css += ".task-expanded{display:none;border-top:1px solid var(--border);position:relative}"
    css += ".task-card.expanded .task-expanded{display:block}"
    css += ".variant-tabs{display:flex;border-bottom:1px solid var(--border);background:rgba(0,0,0,0.2);overflow-x:auto}"
    css += ".variant-tab{padding:12px 24px;font-size:0.85rem;font-weight:500;color:var(--text-secondary);cursor:pointer;border-bottom:2px solid transparent;transition:all 0.2s;white-space:nowrap}"
    css += ".variant-tab:hover{color:var(--text-primary)}"
    css += ".variant-tab.active{color:var(--accent-1);border-bottom-color:var(--accent-1);background:rgba(99,102,241,0.05)}"
    css += ".variant-content{display:none;padding:24px}"
    css += ".variant-content.active{display:block}"
    css += ".question-section{margin-bottom:24px}"
    css += ".section-label{font-size:0.75rem;letter-spacing:1px;color:var(--accent-3);font-weight:600;margin-bottom:10px;display:flex;align-items:center;gap:6px}"
    css += ".section-label::before{content:'';width:3px;height:14px;background:var(--accent-1);border-radius:2px}"
    css += ".question-text{font-size:0.9rem;color:var(--text-primary);line-height:1.8;white-space:pre-wrap;background:rgba(0,0,0,0.2);padding:16px 20px;border-radius:var(--radius-sm);border-left:3px solid var(--accent-2)}"
    css += ".output-format{font-family:'JetBrains Mono',monospace;font-size:0.8rem;background:rgba(0,0,0,0.3);padding:12px 16px;border-radius:var(--radius-sm);color:var(--text-secondary);overflow-x:auto;white-space:pre-wrap;border-left:3px solid var(--accent-3)}"
    css += ".focus-text{font-size:0.82rem;color:var(--text-secondary);margin:0 24px 0;padding:8px 12px;background:rgba(139,92,246,0.08);border-radius:var(--radius-sm);border-left:3px solid var(--accent-2)}"
    css += ".focus-text strong{color:var(--accent-2);font-weight:600}"
    css += ".results-section{margin-top:20px;padding:16px 20px;background:rgba(16,185,129,0.05);border:1px solid rgba(16,185,129,0.2);border-radius:var(--radius-sm)}"
    css += ".results-title{font-size:0.8rem;font-weight:600;color:var(--success);margin-bottom:10px}"
    css += ".result-pending{color:var(--warning);font-size:0.8rem;font-style:italic}"
    css += ".close-btn{position:absolute;top:16px;right:16px;width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,0.1);border:none;color:var(--text-secondary);font-size:1.2rem;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all 0.2s;z-index:10}"
    css += ".close-btn:hover{background:rgba(239,68,68,0.2);color:var(--danger)}"
    css += ".footer{text-align:center;padding:40px 20px;color:var(--text-muted);font-size:0.8rem;border-top:1px solid var(--border);margin-top:60px}"
    css += "@media(max-width:768px){.header h1{font-size:2rem}.task-grid{grid-template-columns:1fr}.stats-bar{gap:20px}.variant-tab{padding:10px 16px;font-size:0.8rem}.variant-content{padding:16px}}"
    return css

def get_js():
    js = """
function toggleCard(card) {
    if (card.classList.contains('expanded')) return;
    document.querySelectorAll('.task-card.expanded').forEach(c => c.classList.remove('expanded'));
    card.classList.add('expanded');
    setTimeout(() => card.scrollIntoView({behavior:'smooth',block:'nearest'}), 100);
}
function closeCard(btn) {
    btn.closest('.task-card').classList.remove('expanded');
}
function switchVariant(tab, idx) {
    var card = tab.closest('.task-card');
    card.querySelectorAll('.variant-tab').forEach(t => t.classList.remove('active'));
    card.querySelectorAll('.variant-content').forEach(c => c.classList.remove('active'));
    tab.classList.add('active');
    card.querySelectorAll('.variant-content')[idx].classList.add('active');
}
"""
    return js

# Main execution
html = gen_html()
out_path = os.path.join(OUT, "index.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Generated {out_path} ({len(html)} bytes)")
