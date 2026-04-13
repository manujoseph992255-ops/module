with open('Data-Module-1.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = content.replace("\\'feedback", "'feedback")

with open('Data-Module-1.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
