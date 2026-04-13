import os
import re

files_to_update = [
    "sql_roadmap.html",
    "roadmap.html",
    "ai_roadmap.html",
    "sql_intro.html",
    "intro.html",
    "marian_analytics.html",
    "sql_index.html",
    "python_index.html",
    "ai_index.html",
    "powerbi_index.html"
]

# Regex pattern to match any SVG block that is immediately followed by the text 'Back' (with possible whitespace)
svg_pattern = re.compile(r'<svg[^>]*>.*?</svg>\s*(Back)', re.DOTALL | re.IGNORECASE)

for f in files_to_update:
    path = os.path.join(r"c:\Users\kj anand\Downloads\Quiz DD", f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Remove the SVG, keeping only the 'Back' text
        new_content = svg_pattern.sub(r'\1', content)
        
        if content != new_content:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Removed SVG from {f}")
        else:
            print(f"No changes required for {f}")
    else:
        print(f"File not found: {path}")
