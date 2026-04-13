import re

path = r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the old HTML table comparison block
html = re.sub(
    r'\s*<div style="margin: 40px 0;">\s*<p><strong>Visual Comparison:</strong>.*?</div>\s*</div>\s*</div>',
    '',
    html, flags=re.DOTALL
)

# 2. SVG-image-style clean vs uncleaned dataset visual
svg_images_html = '''
            <div style="margin:40px 0;">
                <p><strong>Visual: Uncleaned vs Cleaned Dataset</strong></p>
                <div style="display:flex; gap:24px; flex-wrap:wrap; margin-top:16px;">

                    <!-- UNCLEANED SVG IMAGE -->
                    <div style="flex:1;min-width:280px;">
                        <div style="font-size:12px;font-weight:800;color:#dc2626;letter-spacing:1px;text-transform:uppercase;margin-bottom:8px;">&#10005; Raw / Uncleaned Data</div>
                        <svg viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:10px;box-shadow:0 4px 20px rgba(0,0,0,0.12);">
                            <rect width="420" height="230" rx="10" fill="#fff1f2" stroke="#fca5a5" stroke-width="1.5"/>
                            <!-- header row -->
                            <rect x="0" y="0" width="420" height="36" rx="10" fill="#fee2e2"/>
                            <rect x="0" y="26" width="420" height="10" fill="#fee2e2"/>
                            <text x="16" y="23" font-family="monospace" font-size="12" font-weight="bold" fill="#991b1b">Name</text>
                            <text x="130" y="23" font-family="monospace" font-size="12" font-weight="bold" fill="#991b1b">Age</text>
                            <text x="195" y="23" font-family="monospace" font-size="12" font-weight="bold" fill="#991b1b">Revenue</text>
                            <text x="320" y="23" font-family="monospace" font-size="12" font-weight="bold" fill="#991b1b">City</text>
                            <!-- Row 1 - ok -->
                            <text x="16" y="58" font-family="monospace" font-size="11.5" fill="#374151">Arjun Kumar</text>
                            <text x="130" y="58" font-family="monospace" font-size="11.5" fill="#374151">28</text>
                            <text x="195" y="58" font-family="monospace" font-size="11.5" fill="#374151">85000</text>
                            <text x="320" y="58" font-family="monospace" font-size="11.5" fill="#374151">Mumbai</text>
                            <!-- Row 2 - missing values -->
                            <rect x="8" y="65" width="404" height="28" rx="4" fill="#fef2f2"/>
                            <text x="16" y="84" font-family="monospace" font-size="11.5" fill="#dc2626">NULL</text>
                            <text x="130" y="84" font-family="monospace" font-size="11.5" fill="#dc2626">???</text>
                            <text x="195" y="84" font-family="monospace" font-size="11.5" fill="#dc2626">N/A</text>
                            <text x="320" y="84" font-family="monospace" font-size="11.5" fill="#dc2626">delhi</text>
                            <!-- Row 3 - invalid -->
                            <text x="16" y="112" font-family="monospace" font-size="11.5" fill="#374151">priya sharma</text>
                            <text x="130" y="112" font-family="monospace" font-size="11.5" fill="#dc2626">-5</text>
                            <text x="195" y="112" font-family="monospace" font-size="11.5" fill="#374151">120000</text>
                            <text x="320" y="112" font-family="monospace" font-size="11.5" fill="#374151">Bengaluru</text>
                            <!-- Row 4 - duplicate -->
                            <rect x="8" y="119" width="404" height="28" rx="4" fill="#fef2f2"/>
                            <text x="16" y="138" font-family="monospace" font-size="11.5" fill="#374151">Arjun Kumar</text>
                            <text x="130" y="138" font-family="monospace" font-size="11.5" fill="#374151">28</text>
                            <text x="195" y="138" font-family="monospace" font-size="11.5" fill="#dc2626">85000 Rs</text>
                            <text x="320" y="138" font-family="monospace" font-size="11.5" fill="#374151">Mumbai</text>
                            <!-- Row 5 -->
                            <text x="16" y="165" font-family="monospace" font-size="11.5" fill="#374151">Rohit Singh</text>
                            <text x="130" y="165" font-family="monospace" font-size="11.5" fill="#374151">32</text>
                            <text x="195" y="165" font-family="monospace" font-size="11.5" fill="#374151">97500</text>
                            <text x="320" y="165" font-family="monospace" font-size="11.5" fill="#dc2626">HYDER ABAD</text>
                            <!-- Legend labels -->
                            <text x="16" y="200" font-family="sans-serif" font-size="10" fill="#dc2626">&#9679; Missing values   &#9679; Invalid age   &#9679; Duplicate row   &#9679; Mixed format</text>
                        </svg>
                    </div>

                    <!-- CLEANED SVG IMAGE -->
                    <div style="flex:1;min-width:280px;">
                        <div style="font-size:12px;font-weight:800;color:#16a34a;letter-spacing:1px;text-transform:uppercase;margin-bottom:8px;">&#10003; Processed / Cleaned Data</div>
                        <svg viewBox="0 0 420 230" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:10px;box-shadow:0 4px 20px rgba(0,0,0,0.12);">
                            <rect width="420" height="230" rx="10" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
                            <!-- header row -->
                            <rect x="0" y="0" width="420" height="36" rx="10" fill="#dcfce7"/>
                            <rect x="0" y="26" width="420" height="10" fill="#dcfce7"/>
                            <text x="16" y="23" font-family="monospace" font-size="12" font-weight="bold" fill="#166534">Name</text>
                            <text x="140" y="23" font-family="monospace" font-size="12" font-weight="bold" fill="#166534">Age</text>
                            <text x="205" y="23" font-family="monospace" font-size="12" font-weight="bold" fill="#166534">Revenue (INR)</text>
                            <text x="335" y="23" font-family="monospace" font-size="12" font-weight="bold" fill="#166534">City</text>
                            <!-- Row 1 -->
                            <text x="16" y="58" font-family="monospace" font-size="11.5" fill="#14532d">Arjun Kumar</text>
                            <text x="140" y="58" font-family="monospace" font-size="11.5" fill="#14532d">28</text>
                            <text x="205" y="58" font-family="monospace" font-size="11.5" fill="#14532d">&#8377;85,000</text>
                            <text x="335" y="58" font-family="monospace" font-size="11.5" fill="#14532d">Mumbai</text>
                            <!-- Row 2 -->
                            <rect x="8" y="65" width="404" height="28" rx="4" fill="#dcfce7"/>
                            <text x="16" y="84" font-family="monospace" font-size="11.5" fill="#14532d">Priya Sharma</text>
                            <text x="140" y="84" font-family="monospace" font-size="11.5" fill="#14532d">31</text>
                            <text x="205" y="84" font-family="monospace" font-size="11.5" fill="#14532d">&#8377;1,20,000</text>
                            <text x="335" y="84" font-family="monospace" font-size="11.5" fill="#14532d">Bengaluru</text>
                            <!-- Row 3 -->
                            <text x="16" y="112" font-family="monospace" font-size="11.5" fill="#14532d">Rohit Singh</text>
                            <text x="140" y="112" font-family="monospace" font-size="11.5" fill="#14532d">32</text>
                            <text x="205" y="112" font-family="monospace" font-size="11.5" fill="#14532d">&#8377;97,500</text>
                            <text x="335" y="112" font-family="monospace" font-size="11.5" fill="#14532d">Hyderabad</text>
                            <!-- checkmark icon effect -->
                            <text x="16" y="200" font-family="sans-serif" font-size="10" fill="#16a34a">&#9679; No missing values   &#9679; Title case names   &#9679; Uniform INR format   &#9679; No duplicates</text>
                        </svg>
                    </div>
                </div>
            </div>
'''

# 3. Fix broken unstructured icon (use a different isometric icon)
html = html.replace(
    'https://img.icons8.com/isometric/100/file-cabinet.png',
    'https://img.icons8.com/isometric/100/stack-of-paper.png'
)
html = html.replace(
    'https://img.icons8.com/isometric/100/documents.png',
    'https://img.icons8.com/isometric/100/stack-of-paper.png'
)

# 4. Insert the SVG visual before Section 2
insert_marker = '<div class="section-header" style="margin-top: 60px;">\n                <h2>2. Data Analysis</h2>'
if insert_marker in html and 'SVG-image-style' not in html:
    html = html.replace(insert_marker, svg_images_html + '\n' + insert_marker)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
