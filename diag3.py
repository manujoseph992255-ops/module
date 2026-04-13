import re

with open(r"c:\Users\kj anand\Downloads\Ceriport SQL 1 (1).html", "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

print(f"Total file size: {len(content):,} chars")

# Find positioned divs anywhere in the file
pos_divs = re.findall(r'<div[^>]*style="[^"]*top\s*:\s*[\d.]+px', content)
print(f"Total positioned divs: {len(pos_divs)}")

# Find pdf24_01 class divs (the text elements from earlier working script)
text_divs = re.findall(r'<div class="pdf24_01"', content)
print(f"pdf24_01 divs: {len(text_divs)}")

# Show sample of a text div
idx = content.find('class="pdf24_01"')
if idx > -1:
    print("\nSample pdf24_01 div:")
    print(repr(content[idx-20:idx+400]))

# Count page divs
page_divs = re.findall(r'id="page_\d+"', content)
print(f"\nTotal page divs: {len(page_divs)}")

# Find where the text content actually starts (after the CSS/font blocks)
idx_dbms = content.find("DBMS")
if idx_dbms > -1:
    print(f"\nFirst 'DBMS' at char position: {idx_dbms:,}")
    # Show surrounding structure
    start = max(0, idx_dbms - 300)
    print(repr(content[start:idx_dbms+200]))

# Try to extract page_1 content between page_1 and page_2
p1_start = content.find('id="page_1"')
p2_start = content.find('id="page_2"')
if p1_start > -1 and p2_start > -1:
    page1 = content[p1_start:p2_start]
    print(f"\nPage 1 length: {len(page1)} chars")
    # Find text elements in page 1
    spans = re.findall(r'<span[^>]*>([^<]+)</span>', page1)
    print(f"Spans in page 1: {len(spans)}")
    for s in spans[:15]:
        s = s.replace('&nbsp;', ' ').strip()
        if s:
            print(f"  '{s}'")
