import glob
import re

for filepath in glob.glob('Excel-Module-*.html'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Scope the generic 'li' rules to 'ul li' only
        content = re.sub(r'li\s*{\s*position:\s*relative;\s*padding-left:\s*28px;\s*margin-bottom:\s*12px;\s*color:\s*#334155;\s*}', 
                         r'ul li { position: relative; padding-left: 28px; margin-bottom: 12px; color: #334155; }\n        ol li { margin-bottom: 12px; color: #334155; padding-left: 8px; }', content)
                         
        content = re.sub(r'li::before\s*{', r'ul li::before {', content)
        
        # Also fix any inline styles on the ol in Module 11 to give numbers room
        if filepath == 'Excel-Module-11.html':
            content = content.replace('style="margin-left: 20px; color: #334155; font-size: 16px; line-height: 1.8;"', 
                                      'style="margin-left: 35px; color: #334155; font-size: 16px; line-height: 1.8;"')
                                      
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Fixed CSS in {filepath}")
    except Exception as e:
        print(f"Error in {filepath}: {e}")
