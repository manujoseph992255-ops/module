import os
import re

directories = [
    r"c:\Users\kj anand\Downloads\Quiz DD",
    r"c:\Users\kj anand\Downloads\Form 9A"
]

# Robust regex to find the contact bar div
div_pattern = re.compile(r'\s*<div class="quick-contact-bar">.*?</div>', re.DOTALL)

# Regular expression to find the CSS related to the contact bar
# Look for blocks that start with .quick-contact-bar or are clearly related
# We added them at the end of the head.
css_pattern = re.compile(r'\s*<style>\s*\.quick-contact-bar\s*\{.*?</style>', re.DOTALL)

count_removed = 0

for directory in directories:
    if not os.path.exists(directory):
        continue
    
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
            
        # Target: Module pages
        if "module" in filename.lower():
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            new_content = content
            
            # Remove the div
            new_content = div_pattern.sub("", new_content)
            
            # Remove the CSS block
            # If it was added by our previous script, it's a separate <style> block
            new_content = css_pattern.sub("", new_content)
            
            # If it was an existing file that we updated, it might be inside an existing style block.
            # But in that case, we might want to be more careful.
            # Let's check for any remaining .quick-contact-bar styles if they were inside another block.
            if ".quick-contact-bar" in new_content:
                # Find the index of .quick-contact-bar
                # And remove from there until the close of the style block?
                # Actually, our added block was always at the end of head.
                # Let's try to remove Specifically the block we added in the previous turn.
                pass

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Removed from {filename}")
                count_removed += 1

print(f"Total files updated: {count_removed}")
