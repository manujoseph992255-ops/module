import re
import os

path = r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-4.html"
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

if 'triggerConfetti' in text and '</script>' not in text[text.rfind('triggerConfetti'):]:
    text = text.replace('</body>', '</script>\n</body>')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed Data-Module-4.html")
else:
    print("No fix needed or condition not met")
