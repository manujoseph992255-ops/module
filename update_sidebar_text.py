import os
import re

def replace_sidebar_text():
    directory = r'c:\Users\kj anand\Downloads\Quiz DD'
    target_pattern = re.compile(r'<a href="Excel-Module-10-1\.html">10 Master Capstone</a>')
    replacement = '<a href="Excel-Module-10-1.html">10 Master Capstone Simulation</a>'
    
    # Check for other variations too just in case
    target_pattern_v2 = re.compile(r'>10 Master Capstone<')
    replacement_v2 = '>10 Master Capstone Simulation<'

    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = target_pattern.sub(replacement, content)
            new_content = target_pattern_v2.sub(replacement_v2, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated sidebar in {filename}")

if __name__ == "__main__":
    replace_sidebar_text()
