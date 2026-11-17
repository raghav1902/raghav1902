import os

assets_dir = r"C:\Users\ragha\OneDrive\Documents\GitHub\raghav1902\assets"

extra_projects = [
    {
        "filename": "p-currency.svg",
        "num": "07",
        "category": "FINTECH UI · LIVE RATES",
        "title": "Currency Converter Pro",
        "desc_l1": "Real-time FX converter & travel expense planner with live financial",
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
        "desc_l2": "synchronization with Socket.io & OTP-based reservation verification.",
        "tags": ["MERN Stack", "Socket.io", "MongoDB", "Express"],
        "action": "Source Code ↗",
        "accent": "#34d399",
        "badge_color": "#10b981"
    }
]

for p in extra_projects:
    tags_svg = ""
    curr_x = 28
    for tag in p["tags"]:
        w = len(tag) * 8 + 24
        tags_svg += f"""<rect x="{curr_x}" y="162" width="{w}" height="28" rx="8" fill="#131c2e" stroke="#223254" stroke-width="1"/>
<text x="{curr_x + w//2}" y="180.5" text-anchor="middle" font-family="'JetBrains Mono', Consolas, monospace" font-size="12" font-weight="500" fill="{p['accent']}">{tag}</text>
"""
        curr_x += w + 8

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="540" height="216" viewBox="0 0 540 216" role="img" aria-label="{p['title']}">
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
        f.write(svg.strip())
    print(f"Created {p['filename']}")
