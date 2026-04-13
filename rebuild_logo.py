import re

def parse_svg(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    # regex to find paths: <path d="..." fill="..." transform="..." />
    # transform is optional
    path_pattern = re.compile(r'<path\s+d="([^"]+)"\s+fill="([^"]+)"\s*(?:transform="([^"]+)")?\s*/?>')
    paths = []
    
    for match in path_pattern.finditer(content):
        d = match.group(1)
        fill = match.group(2)
        transform = match.group(3) or ""
        
        # Determine color: Red-ish or Blue-ish
        # Red usually starts with #9, #8, #7, #6, #A
        # Blue usually starts with #0, #1, #2, #3, #4
        color = "blue" if fill.lower().startswith(('#0', '#1', '#2', '#3', '#4')) else "red"
        
        # Simple bounding box estimate from transform for grouping
        # translate(x, y)
        x_off, y_off = 0, 0
        if transform:
            m = re.search(r'translate\(([\d.-]+),?\s*([\d.-]+)?\)', transform)
            if m:
                x_off = float(m.group(1))
                y_off = float(m.group(2)) if m.group(2) else 0
        
        paths.append({
            'd': d,
            'fill': fill,
            'transform': transform,
            'color': color,
            'x': x_off,
            'y': y_off,
            'raw': match.group(0)
        })
    
    return paths

def group_paths(paths):
    # Calculate global center
    avg_x = sum(p['x'] for p in paths) / len(paths)
    avg_y = sum(p['y'] for p in paths) / len(paths)
    
    groups = {
        'redTop': [],
        'redLeft': [],
        'blueBottom': [],
        'blueRight': []
    }
    
    for p in paths:
        if p['color'] == 'red':
            if p['y'] < avg_y:
                groups['redTop'].append(p)
            else:
                groups['redLeft'].append(p) # Using Left as a broad category for non-top red
        else:
            if p['y'] >= avg_y:
                groups['blueBottom'].append(p)
            else:
                groups['blueRight'].append(p) # Using Right for non-bottom blue
                
    return groups

def generate_grouped_svg(groups):
    output = []
    for g_id, g_paths in groups.items():
        # Map IDs to actual classes
        layer_class = "red-layer" if "red" in g_id.lower() else "blue-layer"
        output.append(f'                <g id="{g_id}">')
        for p in g_paths:
            # Reconstruct path with class
            # Ensure transform is kept if it existed
            t_str = f' transform="{p["transform"]}"' if p["transform"] else ""
            output.append(f'                    <path d="{p["d"]}" fill="{p["fill"]}"{t_str} class="logo-path {layer_class}" />')
        output.append('                </g>')
    return "\n".join(output)

paths = parse_svg(r'C:\Users\kj anand\Downloads\Quiz DD\Logo marian.svg')
groups = group_paths(paths)
output_text = generate_grouped_svg(groups)

with open(r'C:\Users\kj anand\Downloads\Quiz DD\fixed_groups.txt', 'w', encoding='utf-8') as f:
    f.write(output_text)
print("Saved to fixed_groups.txt")
