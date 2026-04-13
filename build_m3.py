import os
import glob
import re

# 1. Update links in all HTML files
html_files = glob.glob('Excel-Module-*.html') + ['excel_roadmap.html']
for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update sidebar link text and href
        content = re.sub(r'<a href="Excel-Module-3-1\.html"[^>]*>03 [^<]+</a>', '<a href="Excel-Module-3.html">03 The Power of Referencing</a>', content)
        
        # In roadmap, update module 3 title and links
        if filepath == 'excel_roadmap.html':
            content = content.replace('<h3>3. Financial & HR Model Engineering</h3>', '<h3>3. The Power of Referencing</h3>')
            content = content.replace('"Excel-Module-3-1.html"', '"Excel-Module-3.html"')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f'Error processing {filepath}: {e}')

# 2. Build Excel-Module-3.html based on Excel-Module-2.html
with open('Excel-Module-2.html', 'r', encoding='utf-8') as f:
    mod3 = f.read()

# Update title
mod3 = mod3.replace('<title>Module 2: Advanced Lookups & Logic | KVJ Analytics</title>', '<title>Module 3: The Power of Referencing | KVJ Analytics</title>')
mod3 = mod3.replace('MODULE 2: ADVANCED Lookups & LOGIC', 'MODULE 3: THE POWER OF REFERENCING')
mod3 = mod3.replace('MODULE 2: ADVANCED LOOKUPS & LOGIC', 'MODULE 3: THE POWER OF REFERENCING')

# Update active class in sidebar
mod3 = mod3.replace('<a href="Excel-Module-2.html" class="active">02 Advanced Lookups & Logic</a>', '<a href="Excel-Module-2.html">02 Advanced Lookups & Logic</a>')
mod3 = mod3.replace('<a href="Excel-Module-3.html">03 The Power of Referencing</a>', '<a href="Excel-Module-3.html" class="active">03 The Power of Referencing</a>')

# Generate the main content
new_content = """
            <div class="section-header">
                <h2>3. The Power of Referencing</h2>
                <p style="font-weight: 600; color: var(--secondary-blue);">The "DNA" of a Spreadsheet</p>
            </div>

            <div class="interaction-box">
                <strong>Strategic Definition</strong>
                <p style="margin-top:10px;">Referencing determines how formulas behave when they are copied or moved. A professional model must be <strong>"Change-Proof"</strong>—updating one cell should update the entire report.</p>
            </div>

            <h3>1. Relative Reference (The Default)</h3>
            <p>The cell address changes based on the relative position when you copy the formula.</p>
            <ul>
                <li><strong>Application:</strong> Calculating the "Total Cost" for 500 different textile items. You write the formula once <code>(=Price * Quantity)</code>, and as you drag it down, Excel automatically adjusts for each row.</li>
            </ul>

            <h3>2. Absolute Reference (The Anchor)</h3>
            <p>Used when you need to point to a specific cell that must never change, such as a GST Rate, a Discount %, or a fixed Budget Goal.</p>
            <ul>
                <li><strong>How to Lock:</strong> Pressing <code>F4</code> converts a reference (e.g., <code>B1</code>) into an absolute one (<code>$B$1</code>).</li>
                <li><strong>Application:</strong> Multiplying every transaction by a single 18% GST cell. By locking that cell, your formula won't "drift" into empty cells when copied.</li>
            </ul>

            <h3>3. Mixed Reference (The Professional’s Secret)</h3>
            <p>A mixed reference locks either the Row (<code>A$1</code>) or the Column (<code>$A1</code>), but not both. This is essential for creating complex data matrices.</p>
            <ul>
                <li style="margin-bottom: 20px;">
                    <strong>Column Lock ($A1):</strong> The column stays fixed, but the row can change.
                    <br><span style="color:var(--text-muted); font-size:14px;">→ <strong>Use Case:</strong> Comparing different product prices against a fixed list of boutique names in Column A.</span>
                </li>
                <li>
                    <strong>Row Lock (A$1):</strong> The row stays fixed, but the column can change.
                    <br><span style="color:var(--text-muted); font-size:14px;">→ <strong>Use Case:</strong> Applying different seasonal growth percentages (listed in Row 1) across various departments.</span>
                </li>
            </ul>

            <h3 style="margin-top: 40px;">Reference Types Summary</h3>
            <div style="overflow-x:auto;">
                <table style="width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 15px;">
                    <thead style="background: var(--primary-blue); color: white; border-radius: 8px;">
                        <tr>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--border-color);">Reference Type</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--border-color);">Format</th>
                            <th style="padding: 12px; text-align: left; border: 1px solid var(--border-color);">Behavior when Copied</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="background: white;">
                            <td style="padding: 12px; border: 1px solid var(--border-color);"><strong>Relative</strong></td>
                            <td style="padding: 12px; border: 1px solid var(--border-color); color: var(--secondary-blue); font-family: monospace; font-size: 16px;">A1</td>
                            <td style="padding: 12px; border: 1px solid var(--border-color);">Both Column and Row change.</td>
                        </tr>
                        <tr style="background: #f8fafc;">
                            <td style="padding: 12px; border: 1px solid var(--border-color);"><strong>Absolute</strong></td>
                            <td style="padding: 12px; border: 1px solid var(--border-color); color: var(--secondary-blue); font-family: monospace; font-size: 16px;">$A$1</td>
                            <td style="padding: 12px; border: 1px solid var(--border-color);">Neither Column nor Row changes (Total Lock).</td>
                        </tr>
                        <tr style="background: white;">
                            <td style="padding: 12px; border: 1px solid var(--border-color);"><strong>Mixed (Row)</strong></td>
                            <td style="padding: 12px; border: 1px solid var(--border-color); color: var(--secondary-blue); font-family: monospace; font-size: 16px;">A$1</td>
                            <td style="padding: 12px; border: 1px solid var(--border-color);">Column changes; Row is locked.</td>
                        </tr>
                        <tr style="background: #f8fafc;">
                            <td style="padding: 12px; border: 1px solid var(--border-color);"><strong>Mixed (Col)</strong></td>
                            <td style="padding: 12px; border: 1px solid var(--border-color); color: var(--secondary-blue); font-family: monospace; font-size: 16px;">$A1</td>
                            <td style="padding: 12px; border: 1px solid var(--border-color);">Column is locked; Row changes.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <hr style="border:0; border-top: 2px solid #f1f5f9; margin: 50px 0;">

            <!-- MCQ Block -->
            <div class="practice-space">
                <h3 style="margin-top:0;">Knowledge Check: The Anchor</h3>
                <p>You need to apply a single <strong>18% GST Rate</strong> (located in cell <code>D1</code>) to 500 rows of transactions. The reference to <code>D1</code> must <em>never drift</em> when you drag the formula down. Which format should you use?</p>
                <div style="display:flex; flex-direction:column; gap:12px; margin-top:15px;">
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="A"> &nbsp;A. =B2 * D1
                    </label>
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="B"> &nbsp;B. =B2 * $D$1
                    </label>
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="C"> &nbsp;C. =B2 * $D1
                    </label>
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="D"> &nbsp;D. =B2 * D$1
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
                <h3 style="margin-top:0;">Interactive Match: Referencing Logic</h3>
                <p>Select the correct reference format that corresponds to the description of how it behaves when copied.</p>

                <div style="display:grid; grid-template-columns:1fr auto 1fr; gap:14px 16px; align-items:center; margin-top:20px;">
                    <!-- Row 1 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0; font-family: monospace; font-size: 16px;">A1</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m1" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select Behavior —</option>
                        <option value="relative">Both Column and Row change</option>
                        <option value="absolute">Neither Column nor Row changes</option>
                        <option value="col_lock">Column is locked; Row changes</option>
                        <option value="row_lock">Column changes; Row is locked</option>
                    </select>

                    <!-- Row 2 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0; font-family: monospace; font-size: 16px;">$A$1</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m2" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select Behavior —</option>
                        <option value="relative">Both Column and Row change</option>
                        <option value="absolute">Neither Column nor Row changes</option>
                        <option value="col_lock">Column is locked; Row changes</option>
                        <option value="row_lock">Column changes; Row is locked</option>
                    </select>

                    <!-- Row 3 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0; font-family: monospace; font-size: 16px;">A$1</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m3" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select Behavior —</option>
                        <option value="relative">Both Column and Row change</option>
                        <option value="absolute">Neither Column nor Row changes</option>
                        <option value="col_lock">Column is locked; Row changes</option>
                        <option value="row_lock">Column changes; Row is locked</option>
                    </select>

                    <!-- Row 4 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0; font-family: monospace; font-size: 16px;">$A1</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m4" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select Behavior —</option>
                        <option value="relative">Both Column and Row change</option>
                        <option value="absolute">Neither Column nor Row changes</option>
                        <option value="col_lock">Column is locked; Row changes</option>
                        <option value="row_lock">Column changes; Row is locked</option>
                    </select>
                </div>

                <div style="display:flex; gap:12px; align-items:center; margin-top:25px;">
                    <button class="mcq-btn" onclick="checkMatch()">Check All Matches</button>
                    <button class="reset-btn" onclick="resetMatch()">Reset All</button>
                </div>
                <div id="match-fb" class="feedback"></div>
            </div>

            <script>
                // Make sure confetti is loaded
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
                        fb.innerHTML = "✅ Correct! Using an absolute reference ($D$1) anchors both the column and row perfectly.";
                        celebrate();
                    } else {
                        fb.className = "feedback wrong";
                        fb.innerHTML = "❌ Not quite. Remember, an absolute reference must have $ signs before BOTH the column letter and row number.";
                    }
                }

                function resetMCQ(name, feedbackId) {
                    document.querySelectorAll('input[name="' + name + '"]').forEach(r => r.checked = false);
                    const fb = document.getElementById(feedbackId);
                    fb.className = 'feedback'; fb.innerHTML = '';
                }

                function checkMatch() {
                    const answers = { m1: 'relative', m2: 'absolute', m3: 'row_lock', m4: 'col_lock' };
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
                        fb.innerHTML = "✅ Perfect Score! All 4 matches are correct.";
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
# We need to account for <main class="main-content">
start_tag = '<main class="main-content">'
end_tag = '<!-- Footer Navigation -->'

if start_tag in mod3 and end_tag in mod3:
    pre = mod3.split(start_tag)[0]
    post = mod3.split(end_tag)[1]
    mod3 = pre + start_tag + new_content + end_tag + post

# Update floating illustrations
ill_str = '''        <div class="illustration-card" style="animation-delay: 0s;">
            <img src="https://img.icons8.com/color/96/code-fork.png" alt="IF">
            <span>Condition</span>
        </div>
        <div class="illustration-card" style="animation-delay: 1.5s;">
            <img src="https://img.icons8.com/color/96/merge-git.png" alt="AND/OR">
            <span>Logic</span>
        </div>
        <div class="illustration-card" style="animation-delay: 3s;">
            <img src="https://img.icons8.com/color/96/refresh.png" alt="NOT">
            <span>Reverse</span>
        </div>'''
        
new_ill_str = '''        <div class="illustration-card" style="animation-delay: 0s;">
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
mod3 = mod3.replace(ill_str, new_ill_str)

with open('Excel-Module-3.html', 'w', encoding='utf-8') as f:
    f.write(mod3)

print("Created Excel-Module-3.html and updated all references!")
