import re

with open('Data-Module-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS adjustments
html = html.replace('padding: 50px; margin: 60px 0;', 'padding: 30px; margin: 40px 0;')
html = html.replace('gap: 18px; margin: 30px 0;', 'gap: 12px; margin: 20px 0;')
html = html.replace('padding: 22px 30px;', 'padding: 15px 20px;')
html = html.replace('padding: 22px 0;', 'padding: 12px 0;')

# Inline styling adjustments
html = html.replace('margin-top:50px;', 'margin-top:30px;')
html = html.replace('margin-top: 50px;', 'margin-top: 30px;')
html = html.replace('<h4 style="margin-top:50px;">', '<h4 style="margin-top:30px;">')

with open('Data-Module-1.html', 'w', encoding='utf-8') as f:
    f.write(html)
