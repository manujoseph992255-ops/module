with open('Data-Module-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = "Which of the following can be Boolean? (Select 1 and 3 if applicable)"
replacement = "Which of the following can be Boolean? (Select 2 options)"

html = html.replace(target, replacement)

with open('Data-Module-1.html', 'w', encoding='utf-8') as f:
    f.write(html)
