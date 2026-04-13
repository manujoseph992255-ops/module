import re

with open("module_quiz.html", "r", encoding="utf-8") as f:
    html = f.read()

with open("new_mods.json", "r", encoding="utf-8") as f:
    new_mods = f.read()

# The string to find is between "const quizData = {" and "\"mock2\": ["
pattern = re.compile(r'(const quizData = \{\s*)(.*?)(\s*"mock2": \[)', re.DOTALL)

def replace_func(m):
    return m.group(1) + new_mods + "," + m.group(3)

new_html = pattern.sub(replace_func, html)

with open("module_quiz.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Replacement complete.")
