
import os

def sync_layout():
    # Paths to the files
    m1_path = r'c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html'
    m2_path = r'c:\Users\kj anand\Downloads\Quiz DD\Data-Module-2.html'
    
    with open(m1_path, 'r', encoding='utf-8') as f:
        m1_html = f.read()
    
    with open(m2_path, 'r', encoding='utf-8') as f:
        m2_html = f.read()
    
    # 1. Extract CSS block from M1
    import re
    css_match = re.search(r'<style>(.*?)</style>', m1_html, re.DOTALL)
    if not css_match:
        print("Could not find style block in M1")
        return
    m1_css = css_match.group(1)
    
    # 2. Update M2 CSS block
    m2_html = re.sub(r'<style>(.*?)</style>', f'<style>{m1_css}</style>', m2_html, flags=re.DOTALL)
    
    # 3. Extract Sidebar from M1
    sidebar_match = re.search(r'<aside class="sidebar">(.*?)</aside>', m1_html, re.DOTALL)
    if not sidebar_match:
        print("Could not find sidebar in M1")
        return
    m1_sidebar = sidebar_match.group(0)
    
    # 4. Correct Sidebar for M2 (set active link)
    m1_sidebar = m1_sidebar.replace('class="active"', '')
    m1_sidebar = m1_sidebar.replace('href="Data-Module-2.html"', 'href="Data-Module-2.html" class="active"')
    
    # 5. Insert Sidebar into M2's .layout-container
    # M2's layout container currently:
    # <div class="layout-container">
    #     <main class="main-content">
    
    layout_container_pattern = r'<div class="layout-container">\s*<main class="main-content">'
    m2_html = re.sub(layout_container_pattern, f'<div class="layout-container">\n        {m1_sidebar}\n        <main class="main-content">', m2_html)
    
    # 6. Update Layout Container max-width to match M1 (already done by CSS sync)
    
    # 7. Final check for any inconsistencies (e.g., Skulpt script)
    # M2 uses Skulpt, M1 doesn't. Keep Skulpt scripts in M2.
    
    with open(m2_path, 'w', encoding='utf-8') as f:
        f.write(m2_html)
    print("Successfully synced Module 2 layout with Module 1")

if __name__ == "__main__":
    sync_layout()
