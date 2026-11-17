import os
import xml.etree.ElementTree as ET

assets_dir = r"C:\Users\ragha\OneDrive\Documents\GitHub\raghav1902\assets"
os.makedirs(assets_dir, exist_ok=True)

# -------------------------------------------------------------
# 1. FIXED HERO SVG (NO OVERLAP, ROBUST SVG WITHOUT TRANSLATE RESET)
# -------------------------------------------------------------
hero_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="420" viewBox="0 0 1200 420" role="img" aria-label="Raghav Kakrania - Full-Stack &amp; AI Systems Developer">
  <defs>
    <linearGradient id="bg-base" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070a13"/>
      <stop offset="50%" stop-color="#0d1424"/>
      <stop offset="100%" stop-color="#05070c"/>
    </linearGradient>
    <linearGradient id="primary-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#818cf8"/>
      <stop offset="50%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#34d399"/>
    </linearGradient>
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#818cf8" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#1e293b" stop-opacity="0.8"/>
    </linearGradient>
    <linearGradient id="term-header" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#141c2e"/>
      <stop offset="100%" stop-color="#0e1526"/>
    </linearGradient>
    <filter id="glow-blur" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="70"/>
    </filter>
    <pattern id="grid-dots" width="32" height="32" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.2" fill="#38bdf8" fill-opacity="0.08"/>
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#6366f1" stroke-width="0.5" stroke-opacity="0.03"/>
    </pattern>
    <clipPath id="hero-clip">
      <rect width="1200" height="420" rx="24"/>
    </clipPath>
  </defs>

  <style>
    .mono { font-family: 'JetBrains Mono', Consolas, 'Liberation Mono', Menlo, monospace; }
    .sans { font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  </style>

  <g clip-path="url(#hero-clip)">
    <!-- Base Background -->
    <rect width="1200" height="420" fill="url(#bg-base)"/>
    <rect width="1200" height="420" fill="url(#grid-dots)"/>

    <!-- Ambient Glowing Orbs -->
    <circle cx="1060" cy="80" r="190" fill="#6366f1" opacity="0.28" filter="url(#glow-blur)"/>
    <circle cx="1180" cy="360" r="170" fill="#06b6d4" opacity="0.20" filter="url(#glow-blur)"/>
    <circle cx="120" cy="400" r="160" fill="#818cf8" opacity="0.16" filter="url(#glow-blur)"/>
    <circle cx="580" cy="40" r="140" fill="#10b981" opacity="0.10" filter="url(#glow-blur)"/>

    <!-- LEFT SIDE: Identity & Info (Strictly x=64 to x=630) -->
    <!-- Top Status Pill -->
    <g transform="translate(64, 38)">
      <rect x="0" y="0" width="370" height="36" rx="18" fill="#0d1424" fill-opacity="0.9" stroke="#1f2c4a" stroke-width="1.2"/>
      <circle cx="20" cy="18" r="5" fill="#10b981"/>
      <text x="36" y="23" class="mono" font-size="12" font-weight="600" fill="#38bdf8" letter-spacing="1">AVAILABLE FOR OPPORTUNITIES</text>
      <text x="312" y="23" class="sans" font-size="12" fill="#64748b">|</text>
      <text x="325" y="23" class="sans" font-size="12" font-weight="600" fill="#94a3b8">2026</text>
    </g>

    <!-- Main Title -->
    <text x="64" y="136" class="sans" font-size="52" font-weight="800" letter-spacing="-1.5" fill="#ffffff">
      Raghav <tspan fill="url(#primary-grad)">Kakrania</tspan>
    </text>

    <!-- Subtitle Role -->
    <text x="64" y="174" class="mono" font-size="19" font-weight="600" fill="#38bdf8" letter-spacing="0.5">
      Full-Stack &amp; AI Systems Developer
    </text>

    <!-- Bio Description -->
    <text x="64" y="210" class="sans" font-size="14.5" fill="#cbd5e1" font-weight="400">
      B.Tech CSE (AI &amp; DS) at Poornima University, Jaipur. Architecting
    </text>
    <text x="64" y="232" class="sans" font-size="14.5" fill="#94a3b8" font-weight="400">
      scalable web products with <tspan fill="#e2e8f0" font-weight="600">Next.js 14, React, FastAPI</tspan> &amp; <tspan fill="#34d399" font-weight="600">RAG AI search</tspan>.
    </text>

    <!-- Stats Badges Bar (Left Side) -->
    <g transform="translate(64, 268)">
      <g transform="translate(0, 0)">
        <rect width="132" height="56" rx="12" fill="#0e1526" stroke="#1e293b" stroke-width="1.2"/>
        <text x="14" y="25" class="sans" font-size="17" font-weight="700" fill="#38bdf8">9+ Badges</text>
        <text x="14" y="43" class="sans" font-size="11" fill="#64748b">Credly Verified</text>
      </g>
      <g transform="translate(142, 0)">
        <rect width="136" height="56" rx="12" fill="#0e1526" stroke="#1e293b" stroke-width="1.2"/>
        <text x="14" y="25" class="sans" font-size="17" font-weight="700" fill="#a78bfa">2+ Internships</text>
        <text x="14" y="43" class="sans" font-size="11" fill="#64748b">Optisoft &amp; Technit</text>
      </g>
      <g transform="translate(288, 0)">
        <rect width="144" height="56" rx="12" fill="#0e1526" stroke="#1e293b" stroke-width="1.2"/>
        <text x="14" y="25" class="sans" font-size="17" font-weight="700" fill="#34d399">15.8k+ Indexed</text>
        <text x="14" y="43" class="sans" font-size="11" fill="#64748b">Legal Judgments</text>
      </g>
      <g transform="translate(442, 0)">
        <rect width="130" height="56" rx="12" fill="#0e1526" stroke="#1e293b" stroke-width="1.2"/>
        <text x="14" y="25" class="sans" font-size="17" font-weight="700" fill="#f59e0b">Jaipur, IN</text>
        <text x="14" y="43" class="sans" font-size="11" fill="#64748b">Rajasthan, India</text>
      </g>
    </g>

    <!-- Core Stack Pills (Left Bottom) -->
    <g transform="translate(64, 355)">
      <text x="0" y="16" class="mono" font-size="11.5" fill="#64748b" letter-spacing="1.5">// CORE</text>
      <rect x="68" y="0" width="76" height="24" rx="6" fill="#131e36" stroke="#223254" stroke-width="1"/>
      <text x="106" y="16" text-anchor="middle" class="mono" font-size="11" fill="#38bdf8">Next.js</text>

      <rect x="152" y="0" width="72" height="24" rx="6" fill="#131e36" stroke="#223254" stroke-width="1"/>
      <text x="188" y="16" text-anchor="middle" class="mono" font-size="11" fill="#38bdf8">FastAPI</text>

      <rect x="232" y="0" width="86" height="24" rx="6" fill="#131e36" stroke="#223254" stroke-width="1"/>
      <text x="275" y="16" text-anchor="middle" class="mono" font-size="11" fill="#38bdf8">ChromaDB</text>

      <rect x="326" y="0" width="90" height="24" rx="6" fill="#131e36" stroke="#223254" stroke-width="1"/>
      <text x="371" y="16" text-anchor="middle" class="mono" font-size="11" fill="#34d399">Gemini ADK</text>

      <rect x="424" y="0" width="78" height="24" rx="6" fill="#131e36" stroke="#223254" stroke-width="1"/>
      <text x="463" y="16" text-anchor="middle" class="mono" font-size="11" fill="#a78bfa">MongoDB</text>
    </g>

    <!-- RIGHT SIDE: Fixed Position Terminal Card at x=670 (ABSOLUTE POSITIONING, NO TRANSFORM COLLISION) -->
    <g transform="translate(670, 48)">
      <!-- Outer Card -->
      <rect x="0" y="0" width="466" height="324" rx="16" fill="#0c1222" fill-opacity="0.96" stroke="url(#card-border)" stroke-width="1.5"/>

      <!-- Header Bar -->
      <path d="M 0 16 C 0 7.16 7.16 0 16 0 L 450 0 C 458.84 0 466 7.16 466 16 L 466 38 L 0 38 Z" fill="url(#term-header)"/>
      <line x1="0" y1="38" x2="466" y2="38" stroke="#1f2c4a" stroke-width="1"/>

      <!-- Window Dots -->
      <circle cx="22" cy="19" r="6" fill="#ef4444"/>
      <circle cx="42" cy="19" r="6" fill="#f59e0b"/>
      <circle cx="62" cy="19" r="6" fill="#10b981"/>

      <!-- Tab Title -->
      <text x="233" y="23" text-anchor="middle" class="mono" font-size="12" fill="#94a3b8">raghav@system: ~/profile.ts</text>

      <!-- Code Snippet -->
      <g transform="translate(24, 66)" class="mono" font-size="13">
        <text y="0" fill="#818cf8">interface <tspan fill="#38bdf8">Engineer</tspan> <tspan fill="#cbd5e1">{</tspan></text>
        <text y="24" fill="#64748b">  // Full-Stack &amp; AI Systems Builder</text>
        
        <text y="48" fill="#e2e8f0">  name<tspan fill="#818cf8">:</tspan> <tspan fill="#34d399">"Raghav Kakrania"</tspan><tspan fill="#94a3b8">;</tspan></text>
        <text y="72" fill="#e2e8f0">  role<tspan fill="#818cf8">:</tspan> <tspan fill="#34d399">"Full-Stack &amp; AI Systems"</tspan><tspan fill="#94a3b8">;</tspan></text>
        <text y="96" fill="#e2e8f0">  stack<tspan fill="#818cf8">:</tspan> <tspan fill="#cbd5e1">[</tspan><tspan fill="#38bdf8">"Next14"</tspan><tspan fill="#94a3b8">, </tspan><tspan fill="#38bdf8">"React"</tspan><tspan fill="#94a3b8">, </tspan><tspan fill="#38bdf8">"FastAPI"</tspan><tspan fill="#cbd5e1">]</tspan><tspan fill="#94a3b8">;</tspan></text>
        <text y="120" fill="#e2e8f0">  ai<tspan fill="#818cf8">:</tspan> <tspan fill="#cbd5e1">[</tspan><tspan fill="#34d399">"RAG Engine"</tspan><tspan fill="#94a3b8">, </tspan><tspan fill="#34d399">"Gemini ADK"</tspan><tspan fill="#cbd5e1">]</tspan><tspan fill="#94a3b8">;</tspan></text>
        <text y="144" fill="#e2e8f0">  credentials<tspan fill="#818cf8">:</tspan> <tspan fill="#34d399">"9x Credly Badges (GCP)"</tspan><tspan fill="#94a3b8">;</tspan></text>
        <text y="168" fill="#e2e8f0">  openToWork<tspan fill="#818cf8">:</tspan> <tspan fill="#f59e0b">true</tspan><tspan fill="#94a3b8">;</tspan></text>
        <text y="192" fill="#cbd5e1">}</text>

        <!-- Command Exec Output Box -->
        <g transform="translate(0, 218)">
          <rect x="-4" y="-14" width="422" height="28" rx="6" fill="#131b2e" stroke="#23314f" stroke-width="1"/>
          <text x="8" y="4" fill="#34d399">$ <tspan fill="#e2e8f0">raghav.deploy()</tspan> <tspan fill="#64748b">→ status: </tspan><tspan fill="#38bdf8">200 OK</tspan> <tspan fill="#10b981">✓</tspan></text>
        </g>
      </g>
    </g>
  </g>

  <!-- Border Frame -->
  <rect x="0.6" y="0.6" width="1198.8" height="418.8" rx="23.4" fill="none" stroke="#1f2c4a" stroke-width="1.2"/>
</svg>"""

with open(os.path.join(assets_dir, "hero.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg.strip())

# -------------------------------------------------------------
# 2. FIXED STACK SVG (XML ESCAPED &amp;)
# -------------------------------------------------------------
sections = [
    {
        "category": "LANGUAGES",
        "color": "#38bdf8",
        "skills": ["JavaScript (ES6+)", "TypeScript", "Python 3", "SQL", "C", "HTML5 / CSS3"]
    },
    {
        "category": "FRONTEND",
        "color": "#818cf8",
        "skills": ["Next.js 14", "React.js", "Tailwind CSS", "State Management", "Responsive UI"]
    },
    {
        "category": "BACKEND &amp; DB",
        "color": "#34d399",
        "skills": ["Node.js", "Express.js", "FastAPI", "MongoDB Atlas", "MySQL", "ChromaDB", "REST APIs"]
    },
    {
        "category": "AI &amp; RAG",
        "color": "#f59e0b",
        "skills": ["RAG Architecture", "Gemini Multi-Agent", "Gemini ADK", "Gemini Vision OCR", "Groq LLM", "Transformers"]
    },
    {
        "category": "CLOUD &amp; TOOLS",
        "color": "#a78bfa",
        "skills": ["Google Cloud (GCP)", "Terraform (IaC)", "Compute Engine", "GKE", "Git / GitHub", "Vercel", "Render"]
    }
]

total_w = 1050
row_h = 58
header_h = 16
total_h = header_h + len(sections) * row_h + 16

rows_svg = ""
curr_y = header_h + 10

for i, sec in enumerate(sections):
    cat_svg = f"""<text x="32" y="{curr_y + 24}" class="mono" font-size="11.5" font-weight="700" letter-spacing="2" fill="{sec['color']}">{sec['category']}</text>"""
    
    pills_svg = ""
    start_x = 210
    for s in sec["skills"]:
        s_escaped = s.replace("&", "&amp;")
        pw = len(s) * 7.2 + 20
        pills_svg += f"""<rect x="{start_x}" y="{curr_y + 4}" width="{pw}" height="30" rx="9" fill="#101726" stroke="#1e293b" stroke-width="1.1"/>
<text x="{start_x + pw/2}" y="{curr_y + 23.5}" text-anchor="middle" class="sans" font-size="12" font-weight="500" fill="#e2e8f0">{s_escaped}</text>
"""
        start_x += pw + 8

    sep_svg = f"""<line x1="32" y1="{curr_y + 44}" x2="{total_w - 32}" y2="{curr_y + 44}" stroke="#141c2e" stroke-width="1"/>""" if i < len(sections) - 1 else ""

    rows_svg += f"""<g>
  {cat_svg}
  {pills_svg}
  {sep_svg}
</g>
"""
    curr_y += row_h

stack_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{total_h}" viewBox="0 0 {total_w} {total_h}" role="img" aria-label="Technical Skills and Architecture Matrix">
  <defs>
    <linearGradient id="stack-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#0b101c"/>
    </linearGradient>
    <clipPath id="stack-clip">
      <rect width="{total_w}" height="{total_h}" rx="20"/>
    </clipPath>
  </defs>

  <style>
    .sans {{ font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    .mono {{ font-family: 'JetBrains Mono', Consolas, monospace; }}
  </style>

  <g clip-path="url(#stack-clip)">
    <rect width="{total_w}" height="{total_h}" fill="url(#stack-grad)"/>
    <circle cx="980" cy="40" r="140" fill="#6366f1" opacity="0.08"/>
    <circle cx="80" cy="{total_h}" r="120" fill="#06b6d4" opacity="0.06"/>
    {rows_svg}
  </g>

  <rect x="0.6" y="0.6" width="{total_w - 1.2}" height="{total_h - 1.2}" rx="19.4" fill="none" stroke="#1e293b" stroke-width="1.2"/>
</svg>"""

with open(os.path.join(assets_dir, "stack.svg"), "w", encoding="utf-8") as f:
    f.write(stack_svg.strip())

# -------------------------------------------------------------
# 3. FIXED PROJECT CARDS (ALL 8 WITH 100% ESCAPED XML)
# -------------------------------------------------------------
projects = [
    {
        "filename": "p-investoriq.svg",
        "num": "01",
        "category": "AI PLATFORM · FEATURED",
        "title": "InvestorIQ CRM Studio",
        "desc_l1": "AI investor intelligence platform using Gemini Vision OCR to parse",
        "desc_l2": "pitch decks &amp; Excel rosters into verified, deduplicated contacts.",
        "tags": ["Next.js 14", "Gemini OCR", "MongoDB", "Tailwind"],
        "action": "Live Demo ↗",
        "accent": "#38bdf8",
        "badge_color": "#818cf8"
    },
    {
        "filename": "p-dhaaraai.svg",
        "num": "02",
        "category": "LEGALTECH RAG · FLAGSHIP",
        "title": "DhaaraAI Legal Intelligence",
        "desc_l1": "Advanced LegalTech RAG engine indexing 15,800+ Supreme Court",
        "desc_l2": "judgments for statutory search &amp; source-grounded Indian law advice.",
        "tags": ["React.js", "FastAPI", "ChromaDB", "Groq LLM"],
        "action": "Live Demo ↗",
        "accent": "#34d399",
        "badge_color": "#10b981"
    },
    {
        "filename": "p-droneco.svg",
        "num": "03",
        "category": "ENTERPRISE CRM · PRODUCTION",
        "title": "Droneco Lead &amp; Fee CRM",
        "desc_l1": "Coaching institute management portal with strict JWT RBAC,",
        "desc_l2": "installment fee tracking, high-security audit logs &amp; MongoDB Atlas.",
        "tags": ["React.js", "Node.js", "Express", "JWT RBAC"],
        "action": "Live Demo ↗",
        "accent": "#a78bfa",
        "badge_color": "#8b5cf6"
    },
    {
        "filename": "p-smartcv.svg",
        "num": "04",
        "category": "AI AUDITOR · NLP",
        "title": "SmartCV Resume Analyzer",
        "desc_l1": "Automated ATS resume auditor evaluating candidate profiles against",
        "desc_l2": "job specs, calculating match scores &amp; highlighting skill gaps.",
        "tags": ["React.js", "Flask", "NLP", "Gemini LLM"],
        "action": "Source Code ↗",
        "accent": "#f59e0b",
        "badge_color": "#f59e0b"
    },
    {
        "filename": "p-emi.svg",
        "num": "05",
        "category": "FINTECH ENGINE · PERFORMANCE",
        "title": "EMI Ledger Calculator",
        "desc_l1": "Zero-dependency financial math engine computing loan amortisation,",
        "desc_l2": "prepayment interest savings &amp; interactive dynamic charts on Vercel.",
        "tags": ["JavaScript", "Financial Math", "Vercel"],
        "action": "Live Demo ↗",
        "accent": "#38bdf8",
        "badge_color": "#0ea5e9"
    },
    {
        "filename": "p-fastapi.svg",
        "num": "06",
        "category": "ASYNC MICROSERVICE · HIGH-CONCURRENCY",
        "title": "FastAPI Library Microservice",
        "desc_l1": "High-throughput asynchronous university library REST API with",
        "desc_l2": "compound indexing in PyMongo, OpenAPI specs &amp; automated borrowing.",
        "tags": ["FastAPI", "Python 3", "PyMongo", "Swagger"],
        "action": "Source Code ↗",
        "accent": "#10b981",
        "badge_color": "#059669"
    },
    {
        "filename": "p-currency.svg",
        "num": "07",
        "category": "FINTECH UI · LIVE RATES",
        "title": "Currency Converter Pro",
        "desc_l1": "Real-time FX converter &amp; travel expense planner with live financial",
        "desc_l2": "APIs, offline caching, and a sleek boarding-pass ticket aesthetic.",
        "tags": ["React.js", "FX API", "CSS3", "Vercel"],
        "action": "Source Code ↗",
        "accent": "#38bdf8",
        "badge_color": "#0ea5e9"
    },
    {
        "filename": "p-urban-park.svg",
        "num": "08",
        "category": "SMART CITY IOT · REAL-TIME",
        "title": "UrbanPark Smart Parking",
        "desc_l1": "MERN stack parking slot discovery system featuring live availability",
        "desc_l2": "synchronization with Socket.io &amp; OTP-based reservation verification.",
        "tags": ["MERN Stack", "Socket.io", "MongoDB", "Express"],
        "action": "Source Code ↗",
        "accent": "#34d399",
        "badge_color": "#10b981"
    }
]

for p in projects:
    tags_svg = ""
    curr_x = 28
    for tag in p["tags"]:
        w = len(tag) * 8 + 24
        tag_escaped = tag.replace("&", "&amp;")
        tags_svg += f"""<rect x="{curr_x}" y="162" width="{w}" height="28" rx="8" fill="#131c2e" stroke="#223254" stroke-width="1"/>
<text x="{curr_x + w//2}" y="180.5" text-anchor="middle" font-family="'JetBrains Mono', Consolas, monospace" font-size="12" font-weight="500" fill="{p['accent']}">{tag_escaped}</text>
"""
        curr_x += w + 8

    card_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="540" height="216" viewBox="0 0 540 216" role="img" aria-label="{p['title']}">
  <defs>
    <linearGradient id="top-bar-{p['num']}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{p['badge_color']}"/>
      <stop offset="100%" stop-color="{p['accent']}"/>
    </linearGradient>
    <clipPath id="clip-{p['num']}">
      <rect width="540" height="216" rx="18"/>
    </clipPath>
  </defs>

  <style>
    .sans {{ font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    .mono {{ font-family: 'JetBrains Mono', Consolas, monospace; }}
  </style>

  <g clip-path="url(#clip-{p['num']})">
    <rect width="540" height="216" fill="#0b101c"/>
    <rect width="540" height="3.5" fill="url(#top-bar-{p['num']})"/>
    
    <circle cx="500" cy="30" r="110" fill="{p['badge_color']}" opacity="0.08"/>
    <circle cx="40" cy="200" r="90" fill="{p['accent']}" opacity="0.05"/>

    <text x="28" y="38" class="mono" font-size="11.5" font-weight="600" letter-spacing="1.5" fill="{p['badge_color']}">
      {p['num']} // {p['category']}
    </text>

    <text x="28" y="74" class="sans" font-size="22" font-weight="700" letter-spacing="-0.4" fill="#ffffff">
      {p['title']}
    </text>

    <text x="28" y="108" class="sans" font-size="13.5" fill="#94a3b8">
      {p['desc_l1']}
    </text>
    <text x="28" y="130" class="sans" font-size="13.5" fill="#94a3b8">
      {p['desc_l2']}
    </text>

    {tags_svg}

    <text x="512" y="181" text-anchor="end" class="sans" font-size="13.5" font-weight="700" fill="{p['accent']}">
      {p['action']}
    </text>
  </g>

  <rect x="0.6" y="0.6" width="538.8" height="214.8" rx="17.4" fill="none" stroke="#1f2c47" stroke-width="1.2"/>
</svg>"""

    with open(os.path.join(assets_dir, p["filename"]), "w", encoding="utf-8") as f:
        f.write(card_svg.strip())

print("Regenerated all SVGs with 100% valid XML and proper positioning.")
