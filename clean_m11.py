import re

with open('Excel-Module-11.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove <strong> tags from within the <li> questions (only in the first <ol>)
def remove_bold(match):
    content = match.group(1)
    # Remove all <strong> tags within this block
    cleaned = re.sub(r'</?strong>', '', content)
    return f'<ol style="margin-left: 35px; color: #334155; font-size: 16px; line-height: 1.8;">{cleaned}'

html = re.sub(r'<ol style="margin-left: 35px; color: #334155; font-size: 16px; line-height: 1.8;">(.*?)</ol>', remove_bold, html, flags=re.DOTALL)

# 2. Remove Verify buttons
html = re.sub(r'<button onclick="verify.*?</button>', '', html)

# 3. Remove placeholder text from inputs
html = re.sub(r'placeholder=".*?"', 'placeholder="Type your answer here..."', html)

# 4. Clean up any leftover empty practice-box margins if needed (or just keep them as containers)
# The user said "avoid this text inside this" pointing to placeholder, so I replaced with a generic "Type your answer here..." or I can make it empty.
html = re.sub(r'placeholder="Type your answer here\.\.\."', 'placeholder=""', html)

with open('Excel-Module-11.html', 'w', encoding='utf-8') as f:
    f.write(html)
    print("Cleaned Module 11: Removed bold, verify buttons, and placeholders.")
