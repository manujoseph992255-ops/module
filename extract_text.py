
import re
import os

source_path = r"c:\Users\kj anand\Downloads\Ceriport SQL 1 (1).html"
output_path = r"c:\Users\kj anand\Downloads\extracted_sql_content.txt"

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pages are in <div id="page_X" ...>
pages = re.findall(r'<div id="page_(\d+)"[^>]*>(.*?)</div>\s*</div>\s*</div>', content, re.DOTALL)

extracted = []

for page_num, page_content in pages:
    extracted.append(f"--- PAGE {page_num} ---")
    # Text is in <div class="pdf24_01" ...><span ...>Text</span></div>
    # There can be multiple spans or just text.
    # Let's find all text within class="pdf24_01"
    text_divs = re.findall(r'<div class="pdf24_01"[^>]*>(.*?)</div>', page_content, re.DOTALL)
    for div in text_divs:
        # Strip tags to get clean text
        text = re.sub(r'<[^>]+>', '', div).strip()
        if text:
            extracted.append(text)
    extracted.append("\n")

with open(output_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(extracted))

print(f"Extracted content to {output_path}")
