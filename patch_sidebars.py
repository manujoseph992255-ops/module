import glob
import re

# 3. Patch the sidebars in all Excel-Module files to include the 11th Module
for filepath in glob.glob('Excel-Module-*.html'):
    if '11' in filepath: continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '11 Practicals' not in content:
            sidebar_insert = '            <a href="Excel-Module-10-1.html">10 Master Capstone</a>\\n            <a href="Excel-Module-11.html">11 Practicals</a>'
            content = content.replace('            <a href="Excel-Module-10-1.html">10 Master Capstone</a>', sidebar_insert)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                print(f"Patched sidebar for {filepath}")
    except Exception as e:
        print(f'Error updating sidebar in {filepath}: {e}')
