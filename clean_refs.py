import re

with open('Excel-Module-11.html', 'r', encoding='utf-8') as f:
    html = f.read()

# List of regex patterns to remove cell/column references
# Note: Using non-greedy matches and handling optional commas/spaces
patterns = [
    r" from Column [A-Z]",
    r" in Cell [S-U][47], ",
    r" from Column O"
]

for p in patterns:
    html = re.sub(p, "", html)

# Double check "in Cell S4" (without comma cases)
html = html.replace("in Cell S4, ", "")
html = html.replace("in Cell T4, ", "")
html = html.replace("in Cell U4, ", "")
html = html.replace("in Cell S7, ", "")
html = html.replace("in Cell T7, ", "")
html = html.replace("in Cell U7, ", "")

with open('Excel-Module-11.html', 'w', encoding='utf-8') as f:
    f.write(html)
    print("Cleaned Module 11: Removed cell and column references.")
