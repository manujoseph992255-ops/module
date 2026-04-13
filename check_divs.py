path = r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()
opens = html.count('<div')
closes = html.count('</div>')
print('Open divs:', opens)
print('Close divs:', closes)
print('Missing closing divs:', opens - closes)
print('Has layout-container:', 'layout-container' in html)
print('Has sidebar:', 'sidebar' in html)
print('Has main-content:', 'main-content' in html)
