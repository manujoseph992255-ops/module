import os
import re

files_to_update = [
    "style.css",
    "sql_roadmap.html",
    "roadmap.html",
    "ai_roadmap.html",
    "sql_intro.html",
    "intro.html",
    "marian_analytics.html"
]

# Regex to match the CSS block for .nav-back and .nav-back:hover
nav_back_css_pattern = re.compile(r'\s*\.nav-back\s*\{[^}]+\}\s*\.nav-back:hover\s*\{[^}]+\}', re.DOTALL)

new_nav_back_css = """
        .nav-back {
            font-size: 0.95rem;
            font-weight: 600;
            color: white !important;
            background-color: #193855;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.3s ease;
            padding: 12px 28px;
            border-radius: 30px;
            box-shadow: 0 10px 20px rgba(25, 56, 85, 0.3);
        }

        .nav-back:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 25px rgba(25, 56, 85, 0.4);
            background-color: #11283f;
        }"""

for f in files_to_update:
    path = os.path.join(r"c:\Users\kj anand\Downloads\Quiz DD", f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # special case for style.css indentation
        if f == 'style.css':
            replacement = new_nav_back_css.replace('        ', '')
            new_content = nav_back_css_pattern.sub('\n' + replacement, content)
        else:
            new_content = nav_back_css_pattern.sub(new_nav_back_css, content)
        
        if content != new_content:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated CSS in {f}")
        else:
            print(f"No changes required for {f} (regex failed or already updated)")
    else:
        print(f"File not found: {path}")
