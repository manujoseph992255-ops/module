with open('Data-Module-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("resetMCQ(\\'", "resetMCQ('")
html = html.replace("\\')", "')")
html = html.replace("resetMulti(\\'", "resetMulti('")
html = html.replace("resetTFGroup([\\'", "resetTFGroup(['")
html = html.replace("\\', \\'", "', '")
html = html.replace("\\'], \\'", "'], '")

with open('Data-Module-1.html', 'w', encoding='utf-8') as f:
    f.write(html)
