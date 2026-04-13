import os
import re

directories = [
    r"c:\Users\kj anand\Downloads\Quiz DD",
    r"c:\Users\kj anand\Downloads\Form 9A"
]

# Patterns for removal
# 1. The entire DIV block
div_pattern = re.compile(r'\s*<div class="quick-contact-bar">.*?</div>', re.DOTALL)

# 2. CSS rules. We'll look for the class name and match until the next closing brace 
# that is followed by something that isn't another rule of ours, or just match the block.
# Since we know the block of classes we use:
# .quick-contact-bar, .quick-contact-bar a, .qc-phone, .qc-whatsapp, .qc-email, .qc-icon, .qc-divider
css_patterns = [
    re.compile(r'\s*\.quick-contact-bar\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.quick-contact-bar\s+a\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.quick-contact-bar\s+a:hover\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.qc-phone\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.qc-whatsapp\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.qc-email\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.qc-icon\s*\{.*?\}', re.DOTALL),
    re.compile(r'\s*\.qc-divider\s*\{.*?\}', re.DOTALL)
]

# 3. If we added the <style> wrapper, we should remove it too if it's now empty
empty_style_pattern = re.compile(r'\s*<style>\s*</style>', re.DOTALL)

count_removed = 0

def is_module_page(filename):
    fname = filename.lower()
    if "module" in fname:
        return True
    if fname in ["ai_project.html", "marian_analytics.html", "python_game.html", "test_skulpt.html", "tmp_chart.html", "repro.html"]:
        return True
    return False

for directory in directories:
    if not os.path.exists(directory):
        continue
    
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
            
        if is_module_page(filename):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content
            
            # Remove the div
            new_content = div_pattern.sub("", new_content)
            
            # Remove the CSS rules
            for pattern in css_patterns:
                new_content = pattern.sub("", new_content)
                
            # Clean up empty style tags
            new_content = empty_style_pattern.sub("", new_content)

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Removed contact bar from: {filename}")
                count_removed += 1

print(f"Done. Removed from {count_removed} files.")
