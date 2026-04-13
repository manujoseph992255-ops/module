import re

with open(r"c:\Users\kj anand\Downloads\Ceriport SQL 1 (1).html", "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

# Find the page_0 div and show its structure
idx = content.find('id="page_0"')
print("Content around page_0 (500 chars after):")
print(repr(content[idx:idx+800]))
print()

# Find positioned element pattern
pos = re.findall(r'<div[^>]*style="[^"]*top\s*:\s*[\d.]+px[^"]*left\s*:\s*[\d.]+px[^"]*"[^>]*>', content[:5000])
print(f"Positioned divs in first 5000 chars: {len(pos)}")
if pos:
    print("Sample:", repr(pos[0][:300]))
