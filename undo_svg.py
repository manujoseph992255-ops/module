import re

path = r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove structured vs unstructured SVG block
html = re.sub(
    r'\s*<div style="display:flex;gap:24px;flex-wrap:wrap;margin:30px 0;">.*?<!-- Unstructured Data SVG -->.*?</div>\s*</div>\s*</div>',
    '',
    html, flags=re.DOTALL
)

# Remove clean vs uncleaned SVG block
html = re.sub(
    r'\s*<div style="margin:30px 0;">\s*<p><strong>Visual: Raw Data.*?</div>\s*</div>\s*</div>\s*</div>',
    '',
    html, flags=re.DOTALL
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed SVG illustrations.")
print("Structured SVG still present:", 'STRUCTURED DATA' in html)
print("Uncleaned SVG still present:", 'RAW / UNCLEANED' in html)
