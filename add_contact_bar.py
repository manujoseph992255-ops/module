import os
import re

source_file = "Data-Module-1.html"

with open(source_file, "r", encoding="utf-8") as f:
    src_content = f.read()

# Extract CSS block
# Look for something like: .quick-contact-bar { ... }
css_match = re.search(r"(\.quick-contact-bar\s*\{.*?\.qc-divider\s*\{.*?\})", src_content, re.DOTALL)
if css_match:
    css_block = css_match.group(1)
    # The regex above might not capture the full block properly. Let's do a better search.

# Better CSS search:
css_match = re.search(r"(\.quick-contact-bar\s*\{[^\}]+\}.*?\.qc-divider\s*\{[^\}]+\})", src_content, re.DOTALL)

# Let's just find the start of ".quick-contact-bar {" and end at the last closing brace before "</style>"
css_start = src_content.find(".quick-contact-bar {")
css_end = src_content.find("</style>", css_start)
if css_start != -1 and css_end != -1:
    # Need to go back to the closing brace before </style> or just take up to </style>
    css_block = "\n        " + src_content[css_start:css_end].strip()
else:
    print("Could not find CSS block")
    css_block = ""

# Extract HTML block
# Look for <div class="quick-contact-bar"> ... </div>
html_start = src_content.find('<div class="quick-contact-bar">')
html_end = src_content.find('</div>', src_content.find('<a href="mailto:ajaythomas', html_start)) + 6
if html_start != -1 and html_end != -1:
    html_block = src_content[html_start:html_end]
else:
    print("Could not find HTML block")
    html_block = ""


count = 0
if css_block and html_block:
    for filename in os.listdir("."):
        if filename.endswith(".html") and filename != source_file:
            # Skip non-curriculum files optionally, but let's just do all that have </body>
            if "index" in filename or "roadmap" in filename or "module_quiz" in filename or "course_selection.html" in filename:
                continue
                
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "quick-contact-bar" in content:
                continue # Already has it
            
            # Insert CSS just before </style>
            # But wait, some files might not have <style> at all?
            # They all have <style>, but if not, insert into <head>
            if "</style>" in content:
                content = content.replace("</style>", css_block + "\n    </style>", 1)
            else:
                content = content.replace("</head>", "<style>\n" + css_block + "\n    </style>\n</head>", 1)
            
            # Insert HTML just before </body>
            if "</body>" in content:
                content = content.replace("</body>", html_block + "\n\n</body>")
                
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added sidebar to {filename}")
            count += 1
            
print(f"Finished adding sidebar to {count} files.")
