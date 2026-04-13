import os
import re

directory_quiz = r"c:\Users\kj anand\Downloads\Quiz DD"
directory_form = r"c:\Users\kj anand\Downloads\Form 9A"

# Regex for the CSS block (matching what was added)
# It starts with <style> and contains .quick-contact-bar
css_pattern = re.compile(r'    <style>\s+\.quick-contact-bar\s*\{.*?    </style>\s*', re.DOTALL)

# Regex for the HTML block
html_pattern = re.compile(r'    <div class="quick-contact-bar">.*?    </div>\s*', re.DOTALL)

count_removed = 0

for directory in [directory_quiz, directory_form]:
    if not os.path.exists(directory):
        continue
    
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
            
        # Target only files with "Module" in the name
        if "module" in filename.lower():
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = css_pattern.sub("", content)
            new_content = html_pattern.sub("", new_content)

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Removed contact bar from: {filename}")
                count_removed += 1

print(f"Done. Removed from {count_removed} files.")
