import re

path = r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

svg_html = '''
            <div style="display:flex;gap:24px;flex-wrap:wrap;margin:30px 0;">
                <!-- Structured Data SVG -->
                <div style="flex:1;min-width:260px;">
                    <svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:12px;box-shadow:0 6px 24px rgba(0,0,0,0.09);">
                        <rect width="360" height="200" rx="12" fill="#eff6ff"/>
                        <text x="180" y="30" font-family="Montserrat,sans-serif" font-size="13" font-weight="800" fill="#1e3a5f" text-anchor="middle" letter-spacing="1">STRUCTURED DATA</text>
                        <!-- Table mockup -->
                        <rect x="30" y="44" width="300" height="26" rx="4" fill="#1e3a5f"/>
                        <text x="65" y="62" font-family="monospace" font-size="11" fill="#fff">ID</text>
                        <text x="120" y="62" font-family="monospace" font-size="11" fill="#fff">Name</text>
                        <text x="210" y="62" font-family="monospace" font-size="11" fill="#fff">Sales</text>
                        <text x="285" y="62" font-family="monospace" font-size="11" fill="#fff">City</text>
                        <!-- rows -->
                        <rect x="30" y="70" width="300" height="22" fill="#dbeafe"/>
                        <text x="65"  y="85" font-family="monospace" font-size="10.5" fill="#1e3a5f">01</text>
                        <text x="120" y="85" font-family="monospace" font-size="10.5" fill="#1e3a5f">Arjun</text>
                        <text x="210" y="85" font-family="monospace" font-size="10.5" fill="#1e3a5f">85,000</text>
                        <text x="285" y="85" font-family="monospace" font-size="10.5" fill="#1e3a5f">Mumbai</text>
                        <rect x="30" y="92" width="300" height="22" fill="#eff6ff"/>
                        <text x="65"  y="107" font-family="monospace" font-size="10.5" fill="#1e3a5f">02</text>
                        <text x="120" y="107" font-family="monospace" font-size="10.5" fill="#1e3a5f">Priya</text>
                        <text x="210" y="107" font-family="monospace" font-size="10.5" fill="#1e3a5f">1,20,000</text>
                        <text x="285" y="107" font-family="monospace" font-size="10.5" fill="#1e3a5f">Delhi</text>
                        <rect x="30" y="114" width="300" height="22" fill="#dbeafe"/>
                        <text x="65"  y="129" font-family="monospace" font-size="10.5" fill="#1e3a5f">03</text>
                        <text x="120" y="129" font-family="monospace" font-size="10.5" fill="#1e3a5f">Rohit</text>
                        <text x="210" y="129" font-family="monospace" font-size="10.5" fill="#1e3a5f">97,500</text>
                        <text x="285" y="129" font-family="monospace" font-size="10.5" fill="#1e3a5f">Pune</text>
                        <text x="180" y="185" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">Rows &amp; Columns — SQL / Spreadsheet</text>
                    </svg>
                </div>

                <!-- Unstructured Data SVG -->
                <div style="flex:1;min-width:260px;">
                    <svg viewBox="0 0 360 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:12px;box-shadow:0 6px 24px rgba(0,0,0,0.09);">
                        <rect width="360" height="200" rx="12" fill="#fdf4ff"/>
                        <text x="180" y="30" font-family="Montserrat,sans-serif" font-size="13" font-weight="800" fill="#7e22ce" text-anchor="middle" letter-spacing="1">UNSTRUCTURED DATA</text>
                        <!-- Email icon -->
                        <rect x="30" y="50" width="90" height="60" rx="6" fill="#ede9fe"/>
                        <rect x="30" y="50" width="90" height="18" rx="6" fill="#7e22ce"/>
                        <text x="75" y="63" font-family="sans-serif" font-size="9" fill="#fff" text-anchor="middle">EMAIL</text>
                        <text x="55" y="85" font-family="monospace" font-size="8" fill="#6b21a8">Dear Team,</text>
                        <text x="55" y="97" font-family="monospace" font-size="8" fill="#6b21a8">Please review...</text>
                        <!-- Video icon -->
                        <rect x="140" y="50" width="80" height="60" rx="6" fill="#fce7f3"/>
                        <polygon points="165,68 165,95 185,81" fill="#db2777"/>
                        <text x="180" y="120" font-family="sans-serif" font-size="9" fill="#be185d" text-anchor="middle">VIDEO</text>
                        <!-- Social post -->
                        <rect x="238" y="50" width="90" height="60" rx="6" fill="#e0f2fe"/>
                        <circle cx="255" cy="65" r="8" fill="#0284c7"/>
                        <rect x="270" y="58" width="50" height="6" rx="3" fill="#bae6fd"/>
                        <rect x="270" y="68" width="38" height="6" rx="3" fill="#bae6fd"/>
                        <text x="270" y="88" font-family="monospace" font-size="8" fill="#0369a1">Great sale today!</text>
                        <text x="180" y="150" font-family="sans-serif" font-size="11" fill="#64748b" text-anchor="middle">No fixed format — Email, Video, Posts</text>
                    </svg>
                </div>
            </div>
'''

pattern = 'Most modern data generated online is unstructured.\n            </div>'
if pattern in html and 'STRUCTURED DATA' not in html:
    html = html.replace(pattern, pattern + '\n' + svg_html)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Insertion done.")
