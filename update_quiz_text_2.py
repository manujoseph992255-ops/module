with open('module_quiz.html', 'r', encoding='utf-8') as f:
    quiz_html = f.read()

target = """                else if(q.type === "DD") {
                    correct = Array.isArray(u) && u.every((v, j) => v === q.a[j]);
                    userDisp = Array.isArray(u) ? u.join(", ") : userDisp;
                    correctDisp = q.a.join(", ");
                }
                else if(q.type === "DND") {
                    correct = typeof u === 'object' && u !== null && q.a.every((v, j) => u[j] === v);
                    userDisp = typeof u === 'object' && u !== null ? Object.values(u).join(", ") : userDisp;
                    correctDisp = q.a.join(", ");
                }"""

replacement = """                else if(q.type === "DD") {
                    correct = Array.isArray(u) && u.every((v, j) => v === q.a[j]);
                    userDisp = Array.isArray(u) ? '<div style="display:inline-block; vertical-align:top; margin-top:-2px;">' + u.map((v, i) => `Slot ${i+1}: <strong>${v}</strong>`).join('<br>') + '</div>' : userDisp;
                    correctDisp = '<div style="display:inline-block; vertical-align:top; margin-top:-2px;">' + q.a.map((v, i) => `Slot ${i+1}: <strong>${v}</strong>`).join('<br>') + '</div>';
                }
                else if(q.type === "DND") {
                    correct = typeof u === 'object' && u !== null && q.a.every((v, j) => u[j] === v);
                    userDisp = typeof u === 'object' && u !== null ? '<div style="display:inline-block; vertical-align:top; margin-top:-2px;">' + Object.values(u).map((v, i) => `Slot ${i+1}: <strong>${v}</strong>`).join('<br>') + '</div>' : userDisp;
                    correctDisp = '<div style="display:inline-block; vertical-align:top; margin-top:-2px;">' + q.a.map((v, i) => `Slot ${i+1}: <strong>${v}</strong>`).join('<br>') + '</div>';
                }"""

if target in quiz_html:
    quiz_html = quiz_html.replace(target, replacement)
    with open('module_quiz.html', 'w', encoding='utf-8') as f:
        f.write(quiz_html)
    print("Updated DD and DND answer formatting in module_quiz.html")
else:
    print("DD/DND target block not found.")
