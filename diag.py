import re
with open(r"c:\Users\kj anand\Downloads\Ceriport SQL 1 (1).html", "r", encoding="utf-8", errors="replace") as f:
    content = f.read()
ids = re.findall(r'<div[^>]+id="([^"]+)"', content)
print("First 20 div IDs:", ids[:20])
pages = re.findall(r'<div[^>]+id="(page[^"]+)"', content)
print("Page divs:", pages[:10])

# Show structural sample around first page-like div
idx = content.find('id="page')
if idx > -1:
    print("\nSample around first page div:")
    print(repr(content[idx-10:idx+500]))
else:
    # Try to find any positioned divs
    pos_divs = re.findall(r'<div[^>]*style="[^"]*top\s*:', content, re.IGNORECASE)
    print(f"Positioned divs count: {len(pos_divs)}")
    if pos_divs:
        print("Sample:", repr(pos_divs[0][:200]))
    
    # Find the section with content
    idx2 = content.find("DBMS")
    if idx2 > -1:
        print("\nContent around 'DBMS':")
        print(repr(content[idx2-200:idx2+500]))
