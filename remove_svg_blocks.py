path = r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find and remove structured vs unstructured block
# It starts with the marker line and ends before the practice-card for section 6
start1 = html.find('\n            <div style="display:flex;gap:24px;flex-wrap:wrap;margin:30px 0;">\n\n                <!-- Structured Data SVG -->')
if start1 != -1:
    end1 = html.find('</div>\n            </div>\n\n', start1)
    if end1 != -1:
        end1 = html.find('\n', end1 + len('</div>\n            </div>\n\n')) + 1
        block1 = html[start1:end1]
        html = html.replace(block1, '')
        print("Removed structured/unstructured block")
    else:
        print("Could not find end of structured block")
else:
    print("Could not find start of structured block")

# Find and remove clean vs uncleaned block
start2 = html.find('\n            <div style="margin:30px 0;">\n                <p><strong>Visual: Raw Data vs. Cleaned Data</strong>')
if start2 != -1:
    end2 = html.find('\n            </div>\n\n', start2)
    if end2 != -1:
        block2 = html[start2:end2 + len('\n            </div>\n\n')]
        html = html.replace(block2, '')
        print("Removed clean/uncleaned block")
    else:
        print("Could not find end of clean block")
else:
    print("Could not find start of clean block")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Structured SVG still present:", 'STRUCTURED DATA' in html)
print("Uncleaned SVG still present:", 'RAW / UNCLEANED' in html)
