import os
import re

# Update HTML files for wording
files_to_check = [f for f in os.listdir('.') if f.endswith('.html') or f.endswith('.py')]

for filename in files_to_check:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Start Assessment' in content:
        new_content = content.replace('Start Assessment', 'Start Assessment')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated wording in {filename}")

# Update module_quiz.html for MTF displaying
with open('module_quiz.html', 'r', encoding='utf-8') as f:
    quiz_html = f.read()

target = """                else if(q.type === "MTF") {
                    correct = typeof u === 'object' && u !== null && Object.keys(q.a).every(k => u[k] === q.a[k]);
                    userDisp = typeof u === 'object' && u !== null ? JSON.stringify(u).replace(/["{}]/g, "") : userDisp;
                    correctDisp = JSON.stringify(q.a).replace(/["{}]/g, "");
                }"""

replacement = """                else if(q.type === "MTF") {
                    correct = typeof u === 'object' && u !== null && Object.keys(q.a).every(k => u[k] === q.a[k]);
                    userDisp = typeof u === 'object' && u !== null ? '<div style="display:inline-block; vertical-align:top; margin-top:-2px;">' + Object.entries(u).map(([k, v]) => `<strong>${k}</strong> &#8594; ${v}`).join('<br>') + '</div>' : userDisp;
                    correctDisp = '<div style="display:inline-block; vertical-align:top; margin-top:-2px;">' + Object.entries(q.a).map(([k, v]) => `<strong>${k}</strong> &#8594; ${v}`).join('<br>') + '</div>';
                }"""

if target in quiz_html:
    quiz_html = quiz_html.replace(target, replacement)
    with open('module_quiz.html', 'w', encoding='utf-8') as f:
        f.write(quiz_html)
    print("Updated MTF answer formatting in module_quiz.html")
else:
    print("MTF target block not found.")

