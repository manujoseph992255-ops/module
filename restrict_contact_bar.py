import os
import re

directories = [
    r"c:\Users\kj anand\Downloads\Quiz DD",
    r"c:\Users\kj anand\Downloads\Form 9A"
]

# Patterns for removal
div_pattern = re.compile(r'\s*<div class="quick-contact-bar">.*?</div>', re.DOTALL)
css_pattern = re.compile(r'\s*<style>\s*\.quick-contact-bar\s*\{.*?</style>', re.DOTALL)

# More aggressive CSS removal for rules inside larger blocks
css_rules = [
    re.compile(r'\s*\.quick-contact-bar\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.quick-contact-bar\s+a\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.quick-contact-bar\s+a:hover\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.qc-phone\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.qc-whatsapp\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.qc-email\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.qc-icon\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.qc-divider\s*\{.*?\}', re.DOTALL)
]
empty_style_pattern = re.compile(r'\s*<style>\s*</style>', re.DOTALL)

count_removed = 0

# Exception list: ONLY these pages should have the sidebar
exceptions = [
    os.path.join(r"c:\Users\kj anand\Downloads\Quiz DD", "landing.html").lower(),
    os.path.join(r"c:\Users\kj anand\Downloads\Form 9A", "form.html").lower()
]

for directory in directories:
    if not os.path.exists(directory):
        continue
    
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
            
        full_path = os.path.join(directory, filename).lower()
        
        # If it's NOT an exception, remove the bar
        if full_path not in exceptions:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content
            
            # Remove DIV
            new_content = div_pattern.sub("", new_content)
            
            # Remove CSS Block
            new_content = css_pattern.sub("", new_content)
            
            # Remove individual CSS rules
            for pattern in css_rules:
                new_content = pattern.sub("", new_content)
                
            # Clean up empty styles
            new_content = empty_style_pattern.sub("", new_content)

            if new_content != content:
                with open(full_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Removed sidebar from: {filename}")
                count_removed += 1

print(f"Done. Removed from {count_removed} files. Sidebar remains ONLY on landing.html and form.html.")
