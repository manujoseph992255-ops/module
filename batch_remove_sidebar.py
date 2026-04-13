import os
import re

directory = r"C:\Users\kj anand\Downloads\Quiz DD"
files = [f for f in os.listdir(directory) if f.endswith(".html") and 
         (f.startswith("Module-") or f.startswith("SQL-Module-") or f.startswith("AI-Module-"))]

def remove_sidebar(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Adjust .layout-container CSS
    # Remove:
    # .layout-container {
    #     display: flex;
    #     max-width: 1300px;
    #     margin: 40px auto;
    #     gap: 40px;
    #     width: 95%;
    #     padding-bottom: 60px;
    # }
    # To:
    # .layout-container {
    #     max-width: 900px;
    #     margin: 40px auto;
    #     width: 95%;
    #     padding-bottom: 60px;
    # }
    
    layout_pattern = re.compile(r'\.layout-container\s*\{[^}]*display:\s*flex;[^}]*max-width:\s*1300px;[^}]*gap:\s*40px;[^}]*\}', re.DOTALL)
    new_layout_css = """.layout-container {
            max-width: 900px;
            margin: 40px auto;
            width: 95%;
            padding-bottom: 60px;
        }"""
    content = layout_pattern.sub(new_layout_css, content)

    # 2. Remove .sidebar CSS blocks
    sidebar_css_pattern = re.compile(r'/\* Sidebar Navigation \*/\s*\.sidebar\s*\{[^}]*\}\s*\.sidebar\s*h3\s*\{[^}]*\}\s*\.sidebar\s*a\s*\{[^}]*\}\s*\.sidebar\s*a\.active\s*\{[^}]*\}\s*\.sidebar\s*a:hover:not\(\.active\)\s*\{[^}]*\}', re.DOTALL)
    content = sidebar_css_pattern.sub('', content)

    # 3. Remove flex: 1 from .main-content CSS
    main_content_pattern = re.compile(r'\.main-content\s*\{[^}]*flex:\s*1;[^}]*\}', re.DOTALL)
    def fix_main_content(match):
        return match.group(0).replace('flex: 1;', '')
    content = main_content_pattern.sub(fix_main_content, content)

    # 4. Remove sidebar HTML
    # <nav class="sidebar"> ... </nav>
    sidebar_html_pattern = re.compile(r'<nav class="sidebar">.*?</nav>', re.DOTALL)
    content = sidebar_html_pattern.sub('', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filepath}")

for filename in files:
    remove_sidebar(os.path.join(directory, filename))
