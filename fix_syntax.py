import re
import json

with open("module_quiz.html", "r", encoding="utf-8") as f:
    html = f.read()

# We need to fix the quizData object specifically.
# The issue is literal newlines inside double-quoted strings for "code": "..."
# Or we can just use backticks for all "code" properties.

def fix_code_strings(match):
    content = match.group(1)
    # If it contains literal newlines, it's a syntax error in JS for ""
    # We can either escape them with \n or use backticks.
    # Let's use backticks to be safe and clean.
    return f'"code": `{content}`'

# This pattern might be tricky if content has escaped double quotes.
# But since we are looking for literal newlines, it's distinctive.
# Let's try to match "code": "..." where the string spans multiple lines.
pattern = re.compile(r'"code":\s*"(.*?)"', re.DOTALL)

fixed_html = pattern.sub(fix_code_strings, html)

with open("module_quiz.html", "w", encoding="utf-8") as f:
    f.write(fixed_html)

print("Syntax fix applied.")
