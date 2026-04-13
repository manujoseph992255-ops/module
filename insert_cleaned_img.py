import re

path = r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

clean_uncleaned_svg = '''
            <div style="margin:30px 0;">
                <p><strong>Visual: Raw Data vs. Cleaned Data</strong></p>
                <div style="display:flex;gap:24px;flex-wrap:wrap;margin-top:16px;">

                    <!-- UNCLEANED -->
                    <div style="flex:1;min-width:270px;">
                        <svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:12px;box-shadow:0 6px 24px rgba(220,38,38,0.15);">
                            <rect width="380" height="220" rx="12" fill="#fff1f2" stroke="#fca5a5" stroke-width="1.5"/>
                            <!-- Title bar -->
                            <rect x="0" y="0" width="380" height="36" rx="12" fill="#dc2626"/>
                            <rect x="0" y="24" width="380" height="12" fill="#dc2626"/>
                            <text x="14" y="23" font-family="Montserrat,sans-serif" font-size="12" font-weight="800" fill="#fff">&#10005; RAW / UNCLEANED DATA</text>
                            <!-- Header row -->
                            <rect x="14" y="44" width="352" height="22" rx="3" fill="#fee2e2"/>
                            <text x="20"  y="59" font-family="monospace" font-size="10.5" font-weight="bold" fill="#991b1b">Name</text>
                            <text x="120" y="59" font-family="monospace" font-size="10.5" font-weight="bold" fill="#991b1b">Age</text>
                            <text x="175" y="59" font-family="monospace" font-size="10.5" font-weight="bold" fill="#991b1b">Revenue</text>
                            <text x="285" y="59" font-family="monospace" font-size="10.5" font-weight="bold" fill="#991b1b">City</text>
                            <!-- Row 1 -->
                            <text x="20"  y="81" font-family="monospace" font-size="10.5" fill="#374151">Arjun Kumar</text>
                            <text x="120" y="81" font-family="monospace" font-size="10.5" fill="#374151">28</text>
                            <text x="175" y="81" font-family="monospace" font-size="10.5" fill="#374151">85000</text>
                            <text x="285" y="81" font-family="monospace" font-size="10.5" fill="#374151">Mumbai</text>
                            <!-- Row 2 – missing values -->
                            <rect x="14" y="86" width="352" height="22" rx="3" fill="#fee2e2"/>
                            <text x="20"  y="101" font-family="monospace" font-size="10.5" fill="#dc2626">NULL</text>
                            <text x="120" y="101" font-family="monospace" font-size="10.5" fill="#dc2626">???</text>
                            <text x="175" y="101" font-family="monospace" font-size="10.5" fill="#dc2626">N/A</text>
                            <text x="285" y="101" font-family="monospace" font-size="10.5" fill="#dc2626">delhi</text>
                            <!-- Row 3 – invalid age -->
                            <text x="20"  y="122" font-family="monospace" font-size="10.5" fill="#374151">priya sharma</text>
                            <text x="120" y="122" font-family="monospace" font-size="10.5" fill="#dc2626">-5</text>
                            <text x="175" y="122" font-family="monospace" font-size="10.5" fill="#374151">120000</text>
                            <text x="285" y="122" font-family="monospace" font-size="10.5" fill="#374151">Bengaluru</text>
                            <!-- Row 4 – duplicate + mixed format -->
                            <rect x="14" y="128" width="352" height="22" rx="3" fill="#fee2e2"/>
                            <text x="20"  y="143" font-family="monospace" font-size="10.5" fill="#374151">Arjun Kumar</text>
                            <text x="120" y="143" font-family="monospace" font-size="10.5" fill="#374151">28</text>
                            <text x="175" y="143" font-family="monospace" font-size="10.5" fill="#dc2626">85000 Rs</text>
                            <text x="285" y="143" font-family="monospace" font-size="10.5" fill="#374151">Mumbai</text>
                            <!-- Row 5 -->
                            <text x="20"  y="164" font-family="monospace" font-size="10.5" fill="#374151">Rohit Singh</text>
                            <text x="120" y="164" font-family="monospace" font-size="10.5" fill="#374151">32</text>
                            <text x="175" y="164" font-family="monospace" font-size="10.5" fill="#374151">97500</text>
                            <text x="285" y="164" font-family="monospace" font-size="10.5" fill="#dc2626">HYDER ABAD</text>
                            <text x="20"  y="200" font-family="sans-serif" font-size="9.5" fill="#dc2626">Errors: Missing values · Invalid age · Duplicate row · Mixed format</text>
                        </svg>
                    </div>

                    <!-- CLEANED -->
                    <div style="flex:1;min-width:270px;">
                        <svg viewBox="0 0 380 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;border-radius:12px;box-shadow:0 6px 24px rgba(22,163,74,0.15);">
                            <rect width="380" height="220" rx="12" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
                            <!-- Title bar -->
                            <rect x="0" y="0" width="380" height="36" rx="12" fill="#16a34a"/>
                            <rect x="0" y="24" width="380" height="12" fill="#16a34a"/>
                            <text x="14" y="23" font-family="Montserrat,sans-serif" font-size="12" font-weight="800" fill="#fff">&#10003; CLEANED / PROCESSED DATA</text>
                            <!-- Header row -->
                            <rect x="14" y="44" width="352" height="22" rx="3" fill="#dcfce7"/>
                            <text x="20"  y="59" font-family="monospace" font-size="10.5" font-weight="bold" fill="#166534">Name</text>
                            <text x="130" y="59" font-family="monospace" font-size="10.5" font-weight="bold" fill="#166534">Age</text>
                            <text x="190" y="59" font-family="monospace" font-size="10.5" font-weight="bold" fill="#166534">Revenue (INR)</text>
                            <text x="310" y="59" font-family="monospace" font-size="10.5" font-weight="bold" fill="#166534">City</text>
                            <!-- Row 1 -->
                            <text x="20"  y="81" font-family="monospace" font-size="10.5" fill="#14532d">Arjun Kumar</text>
                            <text x="130" y="81" font-family="monospace" font-size="10.5" fill="#14532d">28</text>
                            <text x="190" y="81" font-family="monospace" font-size="10.5" fill="#14532d">&#8377;85,000</text>
                            <text x="310" y="81" font-family="monospace" font-size="10.5" fill="#14532d">Mumbai</text>
                            <!-- Row 2 -->
                            <rect x="14" y="86" width="352" height="22" rx="3" fill="#dcfce7"/>
                            <text x="20"  y="101" font-family="monospace" font-size="10.5" fill="#14532d">Priya Sharma</text>
                            <text x="130" y="101" font-family="monospace" font-size="10.5" fill="#14532d">31</text>
                            <text x="190" y="101" font-family="monospace" font-size="10.5" fill="#14532d">&#8377;1,20,000</text>
                            <text x="310" y="101" font-family="monospace" font-size="10.5" fill="#14532d">Bengaluru</text>
                            <!-- Row 3 -->
                            <text x="20"  y="122" font-family="monospace" font-size="10.5" fill="#14532d">Rohit Singh</text>
                            <text x="130" y="122" font-family="monospace" font-size="10.5" fill="#14532d">32</text>
                            <text x="190" y="122" font-family="monospace" font-size="10.5" fill="#14532d">&#8377;97,500</text>
                            <text x="310" y="122" font-family="monospace" font-size="10.5" fill="#14532d">Hyderabad</text>
                            <!-- Row 4 -->
                            <rect x="14" y="128" width="352" height="22" rx="3" fill="#dcfce7"/>
                            <text x="20"  y="143" font-family="monospace" font-size="10.5" fill="#14532d">Sneha Iyer</text>
                            <text x="130" y="143" font-family="monospace" font-size="10.5" fill="#14532d">26</text>
                            <text x="190" y="143" font-family="monospace" font-size="10.5" fill="#14532d">&#8377;72,300</text>
                            <text x="310" y="143" font-family="monospace" font-size="10.5" fill="#14532d">Delhi</text>
                            <text x="20"  y="200" font-family="sans-serif" font-size="9.5" fill="#16a34a">&#10003; No missing values · Valid ages · Uniform format · No duplicates</text>
                        </svg>
                    </div>

                </div>
            </div>
'''


pattern_2 = '<div class="section-header" style="margin-top: 60px;">\n                <h2>2. Data Analysis</h2>'
if pattern_2 in html and 'CLEANED / PROCESSED DATA' not in html:
    html = html.replace(pattern_2, clean_uncleaned_svg + '\n' + pattern_2)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Insertion of clean vs uncleaned SVG done.")
