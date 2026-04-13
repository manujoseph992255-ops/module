import os, re

directory = r'c:\Users\kj anand\Downloads\Quiz DD'

patterns = [
    re.compile(r'\s*<a href="tel:[^"]*" class="qc-phone"[^>]*>.*?</a>', re.DOTALL),
    re.compile(r'\s*<a href="https://wa\.me/[^"]*" class="qc-whatsapp"[^>]*>.*?</a>', re.DOTALL),
    re.compile(r'\s*<a href="mailto:[^"]*" class="qc-email"[^>]*>.*?</a>', re.DOTALL),
    re.compile(r'\s*<div class="qc-divider"></div>'),
    re.compile(r'<div class="quick-contact-bar">\s*</div>'),
]

count = 0
for filename in os.listdir(directory):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content
    for pattern in patterns:
        content = pattern.sub('', content)
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Cleaned: ' + filename)
        count += 1

print('Done. Cleaned ' + str(count) + ' files.')
