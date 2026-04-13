import re

with open('Excel-Module-2-3.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add confetti script to head if not present
if 'canvas-confetti' not in html:
    html = html.replace('</title>', '</title>\n    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>')

# 2. Prepare the interactive content blocks
interactive_content = """
            <hr style="border:0; border-top: 2px solid #f1f5f9; margin: 50px 0;">

            <!-- MCQ Block -->
            <div class="practice-space">
                <h3 style="margin-top:0;">Choose the Correct Option</h3>
                <p>You need to flag a supplier invoice for review if its status is <strong>Overdue</strong> OR if the <strong>amount exceeds ₹50,000</strong>. Which function structure is most appropriate?</p>
                <div style="display:flex; flex-direction:column; gap:12px; margin-top:15px;">
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="A"> &nbsp;A. =AND(Status="Overdue", Amount>50000)
                    </label>
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="B"> &nbsp;B. =OR(Status="Overdue", Amount>50000)
                    </label>
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="C"> &nbsp;C. =IF(Status="Overdue", Amount>50000)
                    </label>
                    <label class="mcq-option">
                        <input type="radio" name="mcq1" value="D"> &nbsp;D. =NOT(Status="Overdue")
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
                <h3 style="margin-top:0;">Match the Following</h3>
                <p>Match each Logical Function on the left with its correct behavior on the right. Select the right answer from each dropdown.</p>

                <div style="display:grid; grid-template-columns:1fr auto 1fr; gap:14px 16px; align-items:center; margin-top:20px;">
                    <!-- Row 1 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0;">IF() Function</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m1" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select —</option>
                        <option value="all">Returns TRUE only if all conditions are met</option>
                        <option value="any">Returns TRUE if at least one condition is met</option>
                        <option value="branch">Returns one value if TRUE, another if FALSE</option>
                        <option value="reverse">Reverses the logic entirely</option>
                    </select>

                    <!-- Row 2 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0;">AND() Function</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m2" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select —</option>
                        <option value="all">Returns TRUE only if all conditions are met</option>
                        <option value="any">Returns TRUE if at least one condition is met</option>
                        <option value="branch">Returns one value if TRUE, another if FALSE</option>
                        <option value="reverse">Reverses the logic entirely</option>
                    </select>

                    <!-- Row 3 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0;">OR() Function</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m3" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select —</option>
                        <option value="all">Returns TRUE only if all conditions are met</option>
                        <option value="any">Returns TRUE if at least one condition is met</option>
                        <option value="branch">Returns one value if TRUE, another if FALSE</option>
                        <option value="reverse">Reverses the logic entirely</option>
                    </select>

                    <!-- Row 4 -->
                    <div style="background:#f8fafc; padding:12px 16px; border-radius:8px; font-weight:600; color:#1e3a5f; border:1px solid #e2e8f0;">NOT() Function</div>
                    <div style="color:#94a3b8; font-size:20px;">&rarr;</div>
                    <select id="m4" style="padding:10px; border-radius:8px; border:1px solid #e2e8f0; font-size:14px; width:100%;">
                        <option value="">— Select —</option>
                        <option value="all">Returns TRUE only if all conditions are met</option>
                        <option value="any">Returns TRUE if at least one condition is met</option>
                        <option value="branch">Returns one value if TRUE, another if FALSE</option>
                        <option value="reverse">Reverses the logic entirely</option>
                    </select>
                </div>

                <div style="display:flex; gap:12px; align-items:center; margin-top:25px;">
                    <button class="mcq-btn" onclick="checkMatch()">Check All Matches</button>
                    <button class="reset-btn" onclick="resetMatch()">Reset All</button>
                </div>
                <div id="match-fb" class="feedback"></div>
            </div>

            <script>
                /* === Confetti Burst === */
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

                /* === MCQ === */
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
                        fb.innerHTML = "✅ Correct! The OR statement is perfect for this requirement.";
                        celebrate();
                    } else {
                        fb.className = "feedback wrong";
                        fb.innerHTML = "❌ Not quite. Remember, we need to trigger if AT LEAST ONE of the conditions is true.";
                    }
                }

                function resetMCQ(name, feedbackId) {
                    document.querySelectorAll('input[name="' + name + '"]').forEach(r => r.checked = false);
                    const fb = document.getElementById(feedbackId);
                    fb.className = 'feedback'; fb.innerHTML = '';
                }

                /* === Match the Following === */
                function checkMatch() {
                    const answers = { m1: 'branch', m2: 'all', m3: 'any', m4: 'reverse' };
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
            
            <!-- Footer Navigation -->"""

if '<!-- MCQ Block -->' not in html:
    html = html.replace('<!-- Footer Navigation -->', interactive_content)

with open('Excel-Module-2-3.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Interactive JavaScript and HTML block patched successfully!")
