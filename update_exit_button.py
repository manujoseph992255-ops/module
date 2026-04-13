import glob
import re

files = glob.glob('*Module-*.html')
processed = 0

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use positive lookahead to preserve the tag but replace text inside
    updated_content, num_subs = re.subn(r'(<a\s+[^>]*class=["\'][^"\']*(?:logout-btn|exit-btn)[^"\']*["\'][^>]*>)\s*.*?\s*(</a>)', r'\1EXIT\2', content)
    
    if num_subs > 0:
        if content != updated_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated {file_path}")
            processed += 1

print(f"Total files updated: {processed}")
