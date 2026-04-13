import os
import re

files = [
    "Module-1.html", "Module-2.html", "Module-3.html", "Module-4.html", "Module-5.html", "Module-6.html",
    "AI-Module-1.html", "AI-Module-2.html", "AI-Module-3.html", "AI-Module-4.html", "AI-Module-5.html", "AI-Module-6.html",
    "SQL-Module-1.html", "SQL-Module-2.html", "SQL-Module-3.html", "SQL-Module-4.html", "SQL-Module-5.html", "SQL-Module-6.html"
]

# Regex to match the CSS block for .nav-back and .nav-back:hover
nav_back_css_pattern = re.compile(r'\s*\.nav-back\s*\{[^}]+\}\s*\.nav-back:hover\s*\{[^}]+\}', re.DOTALL)

# Regex to match the HTML block wrapping the logo and the back button
nav_back_html_pattern = re.compile(r'<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*1\.5rem;">\s*<a href="[^"]+" class="nav-back">\s*<svg[^>]*>.*?</svg>\s*Back\s*</a>\s*(<a [^>]+><img [^>]+></a>)\s*</div>', re.DOTALL)

for f in files:
    path = os.path.join(r"c:\Users\kj anand\Downloads\Quiz DD", f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        new_content = nav_back_css_pattern.sub('', content)
        new_content = nav_back_html_pattern.sub(r'\1', new_content)
        
        if content != new_content:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes required for {f} (maybe already clean or regex failed)")
    else:
        print(f"File not found: {path}")
