path = r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

depth = 0
# Show all transitions around where depth first drops near or below 1 
for i, line in enumerate(lines, 1):
    opens = line.count('<div')
    closes = line.count('</div>')
    depth += opens - closes
    if depth <= 1 and i > 100:
        print(f"L{i} depth={depth} | {line.rstrip()[:100]}")
        if depth < 0:
            break
