import re

with open("module_quiz.html", "r", encoding="utf-8") as f:
    data = f.read()

# Match the content inside <script> tags
script_match = re.search(r'<script>(.*?)</script>', data, re.DOTALL)
if script_match:
    script = script_match.group(1)
    
    # Check for literal newlines in double-quoted strings
    # This is a bit naive but should find common issues
    lines = script.splitlines()
    for i, line in enumerate(lines):
        # Count double quotes
        quotes = line.count('"')
        if quotes % 2 != 0:
            # Check if it continues on the next line
            print(f"Possible unclosed string at line {i+1}: {line.strip()}")
            
    # Check for unescaped double quotes inside strings
    # This is harder with regex, but let's look for suspicious patterns
    # Like " ... " ... " on one line where middle ones aren't escaped
    for i, line in enumerate(lines):
        # Find all strings like "..."
        matches = re.findall(r'"(.*?)"', line)
        for m in matches:
            if '"' in m: # This shouldn't happen with non-greedy (.*?)
                 pass # Actually (.*?) will stop at the first "
        
        # Another check: look for "Code Content" + result
        if 'print("' in line and '")' in line:
             if line.count('"') > 2 and '\\"' not in line:
                  print(f"Suspicious quotes at line {i+1}: {line.strip()}")
else:
    print("No script tag found")
