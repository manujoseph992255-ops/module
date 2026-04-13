import re

with open('Data-Module-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace MCQ submit buttons
html = re.sub(
    r'(<button class="practice-dark-btn" onclick="checkMCQ\(\'(.*?)\', \'.*?\'\)">.+?</button>)',
    r'\1\n                    <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMCQ(\'\2\')">&#8635; Reset</button>',
    html
)

# Replace Multi submit buttons
html = re.sub(
    r'(<button class="practice-dark-btn" onclick="checkMulti\(\'(.*?)\', \[.*?\]\)">.+?</button>)',
    r'\1\n                    <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMulti(\'\2\')">&#8635; Reset</button>',
    html
)

# Replace TF Group submit buttons
html = re.sub(
    r'(<button class="practice-dark-btn" [^>]*onclick="checkTFGroup\(\[(.*?)\], \[.*?\], \'(.*?)\'\)"[^>]*>.+?</button>)',
    r'\1\n                    <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetTFGroup([\2], \'\3\')">&#8635; Reset</button>',
    html
)

# Add reset functions to scripts
js_to_add = '''
        function resetMCQ(qid) {
            const container = document.getElementById(qid);
            if(container) {
                container.querySelectorAll('.mcq-option').forEach(o => {
                    o.classList.remove('selected', 'correct', 'wrong', 'disabled');
                });
            }
            const feedback = document.getElementById('feedback-' + qid);
            if(feedback) feedback.style.display = 'none';
        }

        function resetMulti(qid) {
            resetMCQ(qid);
        }

        function resetTFGroup(tids, fid) {
            tids.forEach(tid => {
                const btn = document.querySelector(`[onclick*="${tid}"]`);
                if(btn) {
                    const rowContainer = btn.closest('.tf-row');
                    if(rowContainer) {
                        rowContainer.style.background = '';
                        rowContainer.querySelectorAll('.tf-btn').forEach(b => b.classList.remove('selected-true', 'selected-false', 'disabled'));
                    }
                }
                delete tf_data[tid];
            });
            const feedback = document.getElementById(fid);
            if(feedback) feedback.style.display = 'none';
        }
'''

if 'function resetMCQ(qid)' not in html:
    html = html.replace('function selectMCQ', js_to_add + '\n        function selectMCQ')

image_html = '''                <div style="text-align: center; margin: 40px 0;">
                    <img src="Data-Hierarchy.png" alt="Data Types Hierarchy: Data -> Categorical/Numerical -> Nominal/Ordinal/Interval/Ratio" style="max-width: 100%; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
                </div>
'''

search_str = '''                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Quantitative data allows statistical calculations like totals and averages.</p>
                </div>'''

if 'Data-Hierarchy.png' not in html and search_str in html:
    html = html.replace(search_str, search_str + '\n\n' + image_html)

with open('Data-Module-1.html', 'w', encoding='utf-8') as f:
    f.write(html)
