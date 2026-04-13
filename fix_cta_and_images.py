import re

path = r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix quiz-cta - remove old and replace with fully explicit inline styles
old_cta_pattern = r'<div class="quiz-cta"[^>]*>.*?</div>'
new_cta = '''<div class="quiz-cta" style="margin-top:60px; padding:40px; background:linear-gradient(135deg,#1e3a5f 0%,#008eab 100%); border-radius:12px; text-align:center; box-shadow:0 10px 30px rgba(0,142,171,0.2);">
                <h3 style="color:#ffffff !important; margin-top:0; font-size:24px; font-family:Montserrat,sans-serif; font-weight:800;">Ready for the Knowledge Check?</h3>
                <p style="color:#ffffff !important; opacity:0.95; margin-bottom:25px;">Test your understanding of the core foundations of Data Analytics.</p>
                <a href="module_quiz.html?mod=data1" style="display:inline-block; background:#ffffff; color:#1e3a5f; text-decoration:none; padding:16px 40px; border-radius:30px; font-weight:800; font-size:15px; text-transform:uppercase; letter-spacing:1px;">Start Assessment &rarr;</a>
            </div>'''

html = re.sub(old_cta_pattern, new_cta, html, flags=re.DOTALL)

# 2. Fix the broken unstructured data icon URL
html = html.replace(
    'https://img.icons8.com/isometric/100/documents.png',
    'https://img.icons8.com/isometric/100/file-cabinet.png'
)

# 3. Build a "Clean vs. Uncleaned Dataset" HTML visual
clean_vs_uncleaned = '''
            <div style="margin: 40px 0;">
                <p><strong>Visual Comparison:</strong> Raw (Uncleaned) vs Processed (Cleaned) Dataset</p>
                <div style="display:flex; gap:20px; flex-wrap:wrap; margin-top:20px;">
                    <!-- Uncleaned -->
                    <div style="flex:1; min-width:280px; background:#fff1f2; border:1.5px solid #fca5a5; border-radius:12px; padding:20px; overflow-x:auto;">
                        <div style="font-weight:800; color:#dc2626; font-size:13px; letter-spacing:1px; text-transform:uppercase; margin-bottom:12px;">&#10005; Uncleaned / Raw Data</div>
                        <table style="width:100%; border-collapse:collapse; font-size:13px;">
                            <thead>
                                <tr style="background:#fee2e2;">
                                    <th style="padding:8px 10px; text-align:left; border-bottom:1px solid #fca5a5;">Name</th>
                                    <th style="padding:8px 10px; text-align:left; border-bottom:1px solid #fca5a5;">Age</th>
                                    <th style="padding:8px 10px; text-align:left; border-bottom:1px solid #fca5a5;">Revenue (INR)</th>
                                    <th style="padding:8px 10px; text-align:left; border-bottom:1px solid #fca5a5;">Region</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">Arjun Kumar</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">28</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">85000</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">Mumbai</td></tr>
                                <tr style="background:#fef2f2;"><td style="padding:7px 10px; border-bottom:1px solid #fee2e2; color:#dc2626;">NULL</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2; color:#dc2626;">???</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2; color:#dc2626;">N/A</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2; color:#dc2626;">delhi</td></tr>
                                <tr><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">priya sharma</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">-5</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">120000</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">Bengaluru</td></tr>
                                <tr style="background:#fef2f2;"><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">Arjun Kumar</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">28</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2; color:#dc2626;">85000 Rs</td><td style="padding:7px 10px; border-bottom:1px solid #fee2e2;">Mumbai</td></tr>
                                <tr><td style="padding:7px 10px;">Rohit Singh</td><td style="padding:7px 10px;">32</td><td style="padding:7px 10px;">97500</td><td style="padding:7px 10px; color:#dc2626;">HYDER ABAD</td></tr>
                            </tbody>
                        </table>
                        <ul style="margin-top:12px; padding-left:20px; font-size:12px; color:#dc2626; line-height:1.8;">
                            <li>Missing values (NULL, N/A)</li>
                            <li>Inconsistent casing (delhi, HYDER ABAD)</li>
                            <li>Invalid values (Age -5, ??? )</li>
                            <li>Duplicate rows</li>
                            <li>Mixed format (85000 Rs)</li>
                        </ul>
                    </div>
                    <!-- Cleaned -->
                    <div style="flex:1; min-width:280px; background:#f0fdf4; border:1.5px solid #86efac; border-radius:12px; padding:20px; overflow-x:auto;">
                        <div style="font-weight:800; color:#16a34a; font-size:13px; letter-spacing:1px; text-transform:uppercase; margin-bottom:12px;">&#10003; Cleaned / Processed Data</div>
                        <table style="width:100%; border-collapse:collapse; font-size:13px;">
                            <thead>
                                <tr style="background:#dcfce7;">
                                    <th style="padding:8px 10px; text-align:left; border-bottom:1px solid #86efac;">Name</th>
                                    <th style="padding:8px 10px; text-align:left; border-bottom:1px solid #86efac;">Age</th>
                                    <th style="padding:8px 10px; text-align:left; border-bottom:1px solid #86efac;">Revenue (INR)</th>
                                    <th style="padding:8px 10px; text-align:left; border-bottom:1px solid #86efac;">Region</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">Arjun Kumar</td><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">28</td><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">85,000</td><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">Mumbai</td></tr>
                                <tr style="background:#f0fdf4;"><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">Priya Sharma</td><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">31</td><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">1,20,000</td><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">Bengaluru</td></tr>
                                <tr><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">Rohit Singh</td><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">32</td><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">97,500</td><td style="padding:7px 10px; border-bottom:1px solid #dcfce7;">Hyderabad</td></tr>
                            </tbody>
                        </table>
                        <ul style="margin-top:12px; padding-left:20px; font-size:12px; color:#16a34a; line-height:1.8;">
                            <li>No missing values</li>
                            <li>Consistent title case</li>
                            <li>Valid values only</li>
                            <li>Duplicates removed</li>
                            <li>Uniform currency format</li>
                        </ul>
                    </div>
                </div>
            </div>
'''

# Insert after the product-sales table in section 1 (first table in doc)
# Find the first occurrence of </table> that follows the section header for "1. Meaning of Data"
insert_marker = '<div class="section-header" style="margin-top: 60px;">\n                <h2>2. Data Analysis</h2>'
if insert_marker in html and 'clean_vs_uncleaned' not in html:
    html = html.replace(insert_marker, clean_vs_uncleaned + '\n' + insert_marker)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Done!")
