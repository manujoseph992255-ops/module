import glob
import re

# 1. Update links in all HTML files
html_files = glob.glob('Excel-Module-*.html') + ['excel_roadmap.html']
for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update sidebar link text and href
        content = re.sub(r'<a href="Excel-Module-4-1\.html"[^>]*>04 [^<]+</a>', '<a href="Excel-Module-4.html">04 Structured Data</a>', content)
        content = re.sub(r'<a href="Excel-Module-4\.html"[^>]*>04 [^<]+</a>', '<a href="Excel-Module-4.html">04 Structured Data</a>', content)
        
        # In roadmap, update module 4 title, links, and bullets
        if filepath == 'excel_roadmap.html':
            content = content.replace('<h3>4. Dynamic Array Architecture</h3>', '<h3>4. Structured Data (Tables)</h3>')
            content = content.replace('"Excel-Module-4-1.html"', '"Excel-Module-4.html"')
            
            # Replace the bullet points
            old_bullets = """                <ul>
                    <li>SPILL mechanics & structural logic</li>
                    <li>FILTER, SORT, and UNIQUE frameworks</li>
                    <li>Multi-dimensional functional layers</li>
                </ul>"""
            new_bullets = """                <ul>
                    <li>Self-Healing Data (Ctrl+T)</li>
                    <li>Structured Referencing</li>
                    <li>Interactive Slicers</li>
                </ul>"""
            content = content.replace(old_bullets, new_bullets)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f'Error processing {filepath}: {e}')

# 2. Build Excel-Module-4.html based on Excel-Module-3.html
with open('Excel-Module-3.html', 'r', encoding='utf-8') as f:
    mod4 = f.read()

# Update title and Banner
mod4 = mod4.replace('<title>Module 3: The Power of Referencing | KVJ Analytics</title>', '<title>Module 4: Structured Data | KVJ Analytics</title>')
mod4 = mod4.replace('MODULE 3: THE POWER OF REFERENCING', 'MODULE 4: STRUCTURED DATA')

# Update active class in sidebar
mod4 = mod4.replace('<a href="Excel-Module-3.html" class="active">03 The Power of Referencing</a>', '<a href="Excel-Module-3.html">03 The Power of Referencing</a>')
mod4 = mod4.replace('<a href="Excel-Module-4.html">04 Structured Data</a>', '<a href="Excel-Module-4.html" class="active">04 Structured Data</a>')

# Generate the main content
new_content = """
            <div class="section-header">
                <h2>4. Structured Data</h2>
                <p style="font-weight: 600; color: var(--secondary-blue);">The Power of Tables</p>
            </div>

            <div class="interaction-box">
                <strong>The Strategic Logic</strong>
                <p style="margin-top:10px;">Transitioning from a static "Range" to a functional <strong>Database Object</strong> allows for seamless scaling. Professional models rely on structures that update automatically without human intervention.</p>
            </div>

            <h3>1. Self-Healing Data</h3>
            <p>Tables (shortcut: <code>Ctrl+T</code>) automatically expand to include new rows in all connected Pivot Tables and Charts.</p>
            <ul>
                <li style="margin-bottom: 18px;">
                    <strong>The Old Way:</strong> Manually expanding the formulas and ranges from <code>A2:D500</code> to <code>A2:D600</code> at the end of every month.
                </li>
                <li>
                    <strong>The Professional Way:</strong> Adding new data to the bottom of the Table; the Table instantly ingests the rows, extending all calculations and formatting automatically.
                </li>
            </ul>

            <h3>2. Structured Referencing</h3>
            <p>Using readable headers instead of cryptic cell addresses, making models significantly easier to audit and transfer to colleagues.</p>
            <ul>
                <li style="margin-bottom: 20px;">
                    <strong>Structured ($B$2:$B$500):</strong> <code>=SUM(SalesTable[Revenue])</code>
                    <br><span style="color:var(--text-muted); font-size:14px;">→ <strong>Advantage:</strong> The formula is written in plain English, and "Revenue" will always point to the entire revenue column regardless of how many rows are added.</span>
                </li>
            </ul>

            <h3>3. Interactive Slicers</h3>
            <p>Turning a standard list into a visual cockpit. Slicers are floating, hyper-visual filters connected directly to your structured Table.</p>
            <ul>
                <li>
                    <strong>Visual Filtering:</strong> Instantly filter huge datasets. Clicking "Kochi" or "Silk" on a slicer updates every visible calculation instantly, transforming raw tables into mini-dashboards.
                </li>
            </ul>

            <hr style="border:0; border-top: 2px solid #f1f5f9; margin: 50px 0;">

            <!-- MCQ Block -->
            <div class="practice-space">
                <h3 style="margin-top:0;">Knowledge Check: Database Objects</h3>
                <p>A static range requires you to manually update the source data reference in all connected Pivot Tables every time new data is pasted at the bottom. What is the keyboard shortcut to convert this static range into a <strong>self-healing Database Object (Table)</strong>?</p>
                <div style="display:flex; flex-direction:column; gap:12px; margin-top:15px;">
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="A"> &nbsp;A. Ctrl + C
                    </label>
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="B"> &nbsp;B. Ctrl + T
                    </label>
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="C"> &nbsp;C. Ctrl + Shift + L
                    </label>
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="D"> &nbsp;D. Alt + F1
                    </label>
                </div>
                <div style="display:flex; gap:12px; align-items:center; margin-top:20px;">
                    <button class="mcq-btn" onclick="checkMCQ('mcq1','B','mcq-fb1')">Submit Answer</button>
                    <button class="reset-btn" onclick="resetMCQ('mcq1','mcq-fb1')">Reset</button>
                </div>
                <div id="mcq-fb1" class="feedback"></div>
            </div>

            <!-- Match the Following Block -->
            <div class="practice-space" style="margin-top:30px;">
                <h3 style="margin-top:0;">Interactive Match: Table Features</h3>
                <p>Match the Excel Table feature/concept on the left with its corresponding description on the right.</p>

                <div style="display:grid; grid-template-columns:1fr auto 1fr; gap:14px 16px; align-items:center; margin-top:20px;">
                    <!-- Row 1 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0;">Structured Referencing</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m1" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select Description —</option>
                        <option value="reference">Uses plain english column names (e.g. SalesTable[Revenue])</option>
                        <option value="self_healing">Automatically expands to include newly pasted rows</option>
                        <option value="slicer">Visual buttons that act as an interactive cockpit filter</option>
                        <option value="static">Uses cryptic, hardcoded addresses (e.g. C2:C500)</option>
                    </select>

                    <!-- Row 2 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0;">Self-Healing Data</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m2" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select Description —</option>
                        <option value="reference">Uses plain english column names (e.g. SalesTable[Revenue])</option>
                        <option value="self_healing">Automatically expands to include newly pasted rows</option>
                        <option value="slicer">Visual buttons that act as an interactive cockpit filter</option>
                        <option value="static">Uses cryptic, hardcoded addresses (e.g. C2:C500)</option>
                    </select>

                    <!-- Row 3 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0;">Interactive Slicers</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m3" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select Description —</option>
                        <option value="reference">Uses plain english column names (e.g. SalesTable[Revenue])</option>
                        <option value="self_healing">Automatically expands to include newly pasted rows</option>
                        <option value="slicer">Visual buttons that act as an interactive cockpit filter</option>
                        <option value="static">Uses cryptic, hardcoded addresses (e.g. C2:C500)</option>
                    </select>

                    <!-- Row 4 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#e11d48; border:1px solid #e2e8f0;">Static Range</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m4" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select Description —</option>
                        <option value="reference">Uses plain english column names (e.g. SalesTable[Revenue])</option>
                        <option value="self_healing">Automatically expands to include newly pasted rows</option>
                        <option value="slicer">Visual buttons that act as an interactive cockpit filter</option>
                        <option value="static">Uses cryptic, hardcoded addresses (e.g. C2:C500)</option>
                    </select>
                </div>

                <div style="display:flex; gap:12px; align-items:center; margin-top:25px;">
                    <button class="mcq-btn" onclick="checkMatch()">Check All Matches</button>
                    <button class="reset-btn" onclick="resetMatch()">Reset All</button>
                </div>
                <div id="match-fb" class="feedback"></div>
            </div>

            <script>
                function celebrate() {
                    if (typeof confetti !== "undefined") {
                        confetti({
                            particleCount: 120,
                            spread: 80,
                            origin: { y: 0.6 },
                            colors: ['#1e3a5f', '#008eab', '#10b981', '#f59e0b', '#f472b6']
                        });
                        setTimeout(() => confetti({ particleCount: 60, spread: 120, origin: { x: 0.1, y: 0.7 }, colors: ['#38bdf8','#818cf8','#a3e635']}), 200);
                        setTimeout(() => confetti({ particleCount: 60, spread: 120, origin: { x: 0.9, y: 0.7 }, colors: ['#fb7185','#fbbf24','#34d399']}), 400);
                    }
                }

                function checkMCQ(name, correct, feedbackId) {
                    const selected = document.querySelector('input[name="' + name + '"]:checked');
                    const fb = document.getElementById(feedbackId);
                    if (!selected) {
                        fb.className = "feedback wrong";
                        fb.innerHTML = "⚠️ Please select an option first.";
                        return;
                    }
                    if (selected.value === correct) {
                        fb.className = "feedback correct";
                        fb.innerHTML = "✅ Correct! Ctrl+T instantly converts any data block into a smart Table.";
                        celebrate();
                    } else {
                        fb.className = "feedback wrong";
                        fb.innerHTML = "❌ Not quite. Remember, 'T' stands for Table.";
                    }
                }

                function resetMCQ(name, feedbackId) {
                    document.querySelectorAll('input[name="' + name + '"]').forEach(r => r.checked = false);
                    const fb = document.getElementById(feedbackId);
                    fb.className = 'feedback'; fb.innerHTML = '';
                }

                function checkMatch() {
                    const answers = { m1: 'reference', m2: 'self_healing', m3: 'slicer', m4: 'static' };
                    let score = 0;
                    for (const [id, val] of Object.entries(answers)) {
                        const el = document.getElementById(id);
                        el.style.borderColor = el.value === val ? '#10b981' : '#ef4444';
                        el.style.boxShadow = el.value === val ? '0 0 0 2px rgba(16,185,129,0.25)' : '0 0 0 2px rgba(239,68,68,0.25)';
                        if (el.value === val) score++;
                    }
                    const fb = document.getElementById('match-fb');
                    if (score === 4) {
                        fb.className = "feedback correct";
                        fb.innerHTML = "✅ Perfect Score! All 4 concepts matched perfectly.";
                        celebrate();
                    } else {
                        fb.className = "feedback wrong";
                        fb.innerHTML = "❌ " + score + "/4 correct. Dropdowns highlighted red need revisiting.";
                    }
                }

                function resetMatch() {
                    ['m1','m2','m3','m4'].forEach(id => {
                        const el = document.getElementById(id);
                        el.value = ''; el.style.borderColor = '#e2e8f0'; el.style.boxShadow = 'none';
                    });
                    const fb = document.getElementById('match-fb');
                    fb.className = 'feedback'; fb.innerHTML = '';
                }
            </script>
"""

# Replace the content between <div class="section-header"> and <!-- Footer Navigation --> 
start_tag = '<main class="main-content">'
end_tag = '<!-- Footer Navigation -->'

if start_tag in mod4 and end_tag in mod4:
    pre = mod4.split(start_tag)[0]
    post = mod4.split(end_tag)[1]
    mod4 = pre + start_tag + new_content + end_tag + post

# Update floating illustrations
ill_str = '''        <div class="illustration-card" style="animation-delay: 0s;">
            <img src="https://img.icons8.com/color/96/table-1.png" alt="Relative">
            <span>Relative</span>
        </div>
        <div class="illustration-card" style="animation-delay: 1.5s;">
            <img src="https://img.icons8.com/color/96/lock--v1.png" alt="Absolute">
            <span>Fixed</span>
        </div>
        <div class="illustration-card" style="animation-delay: 3s;">
            <img src="https://img.icons8.com/color/96/view-carousel.png" alt="Mixed">
            <span>Mixed</span>
        </div>'''
        
new_ill_str = '''        <div class="illustration-card" style="animation-delay: 0s;">
            <img src="https://img.icons8.com/color/96/database.png" alt="Database">
            <span>Object</span>
        </div>
        <div class="illustration-card" style="animation-delay: 1.5s;">
            <img src="https://img.icons8.com/color/96/code.png" alt="Formula">
            <span>Syntax</span>
        </div>
        <div class="illustration-card" style="animation-delay: 3s;">
            <img src="https://img.icons8.com/color/96/slider.png" alt="Slicer">
            <span>Slicers</span>
        </div>'''
mod4 = mod4.replace(ill_str, new_ill_str)

with open('Excel-Module-4.html', 'w', encoding='utf-8') as f:
    f.write(mod4)

print("Created Excel-Module-4.html and updated all references!")
