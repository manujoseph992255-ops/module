import os
import re

# Update all Data modules to the "Simple UI"
directory = r"c:\Users\kj anand\Downloads\Quiz DD"
data_modules = [
    ("Data-Module-1.html", "DATA BASICS"),
    ("Data-Module-2.html", "DATA LIFECYCLE"),
    ("Data-Module-3.html", "DATA ANALYSIS"),
    ("Data-Module-4.html", "DATA VISUALIZATION"),
    ("Data-Module-5.html", "DATA ETHICS")
]

new_head_style = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module {idx}: {title} | KVJ</title>
    <link
        href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Outfit:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&display=swap"
        rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        :root {
            --primary-blue: #1e3a5f;
            --secondary-blue: #008eab;
            --bg-light: #f6f8fb;
            --text-main: #1d1d1f;
            --text-muted: #4b5563;
            --border-color: #e2e8f0;
            --white: #ffffff;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-light);
            color: var(--text-main);
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            line-height: 1.6;
        }
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 3rem;
            background: #ffffff;
            border-bottom: 1px solid var(--border-color);
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
        }
        .kvj-logo-img { max-height: 35px; width: auto; }
        .logout-btn {
            background: #dc2626;
            color: white;
            padding: 8px 18px;
            text-decoration: none;
            font-size: 12px;
            font-weight: 700;
            border-radius: 6px;
            transition: opacity 0.3s;
            text-transform: uppercase;
        }
        .header-banner {
            background: var(--primary-blue);
            color: white;
            padding: 120px 20px 60px;
            text-align: center;
        }
        .header-banner h1 {
            font-family: 'Montserrat', sans-serif;
            font-size: 38px;
            font-weight: 900;
            letter-spacing: -1px;
            text-transform: uppercase;
        }
        .layout-container {
            display: flex;
            max-width: 1400px;
            margin: 40px auto;
            gap: 40px;
            width: 95%;
            padding-bottom: 60px;
        }
        .sidebar {
            width: 300px;
            flex-shrink: 0;
            background: white;
            padding: 30px;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            position: sticky;
            top: 100px;
            height: fit-content;
        }
        .sidebar h3 {
            font-family: 'Montserrat', sans-serif;
            font-size: 12px;
            font-weight: 800;
            color: var(--secondary-blue);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #f1f5f9;
        }
        .sidebar a {
            display: block;
            padding: 12px 15px;
            color: var(--text-muted);
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            border-radius: 8px;
            margin-bottom: 5px;
            transition: all 0.2s;
        }
        .sidebar a:hover { background: #f8fafc; color: var(--primary-blue); }
        .sidebar a.active {
            background: #eff6ff;
            color: var(--primary-blue);
            font-weight: 700;
            border-left: 4px solid var(--primary-blue);
        }
        .main-content {
            flex: 1;
            background: #ffffff;
            border: 1px solid var(--border-color);
            padding: 40px 60px;
            border-radius: 12px;
        }
        .section-header { margin-bottom: 30px; border-bottom: 3px solid var(--bg-light); padding-bottom: 15px; }
        .section-header h2 {
            font-family: 'Montserrat', sans-serif;
            color: var(--primary-blue);
            font-size: 28px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: -0.5px;
        }
        p { line-height: 1.8; margin-bottom: 25px; color: #334155; font-size: 17px; }
        strong { color: var(--primary-blue); font-weight: 700; }
        h1, h2, h3, h4 { color: var(--primary-blue); font-weight: 700; font-family: 'Montserrat', sans-serif; }
        h3 { font-size: 22px; margin: 40px 0 20px; }
        h4 { font-size: 18px; margin: 30px 0 15px; }
        .interaction-box {
            background-color: #f7f9fc;
            border-left: 5px solid var(--secondary-blue);
            padding: 25px;
            margin: 30px 0;
            border-radius: 0 10px 10px 0;
            font-size: 15px;
        }
        .data-table { width: 100%; border-collapse: collapse; margin: 20px 0; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .data-table th { background: var(--primary-blue); color: white; padding: 12px 15px; text-align: left; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; }
        .data-table td { padding: 12px 15px; border-bottom: 1px solid #edf2f7; font-size: 14px; color: #4a5568; }
        .practice-card { background: #ffffff; border: 2px solid var(--bg-light); border-radius: 12px; padding: 30px; margin: 40px 0; position: relative; }
        .practice-badge { position: absolute; top: -12px; left: 20px; background: var(--secondary-blue); color: white; padding: 4px 12px; border-radius: 4px; font-size: 10px; font-weight: 800; letter-spacing: 1px; }
        .mcq-option { background: #f8fafc; border: 1px solid var(--border-color); padding: 15px 20px; border-radius: 8px; margin-bottom: 10px; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 15px; }
        .mcq-option:hover { background: #f1f5f9; border-color: var(--secondary-blue); }
        .mcq-option.selected { border-width: 2px; }
        .mcq-option.correct { border-color: #10b981; background: #ecfdf5; color: #065f46; }
        .mcq-option.wrong { border-color: #ef4444; background: #fef2f2; color: #991b1b; }
        .tf-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid #f1f5f9; }
        .tf-btn { padding: 6px 15px; border: 1px solid var(--border-color); background: white; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px; transition: all 0.2s; }
        .tf-btn.selected { background: var(--primary-blue); color: white; border-color: var(--primary-blue); }
        .tf-btn.correct { background: #10b981 !important; border-color: #10b981 !important; color: white !important; }
        .tf-btn.wrong { background: #ef4444 !important; border-color: #ef4444 !important; color: white !important; }
        .practice-dark-btn { background: var(--primary-blue); color: white; border: none; padding: 12px 25px; border-radius: 8px; font-weight: 700; font-size: 14px; cursor: pointer; transition: transform 0.2s; margin-top: 20px; }
        .practice-dark-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .feedback-dark { margin-top: 15px; padding: 12px; border-radius: 8px; font-weight: 600; font-size: 14px; display: none; }
        .feedback-dark.correct { background: #f0fdf4; color: #166534; border: 1px solid #bbf7d0; display: block; }
        .feedback-dark.wrong { background: #fef2f2; color: #991b1b; border: 1px solid #fecaca; display: block; }
        .main-content li { list-style: none; position: relative; padding-left: 28px; margin-bottom: 12px; color: #334155; font-size: 16px; }
        .main-content li::before { content: ""; position: absolute; left: 0; top: 8px; width: 8px; height: 8px; background: var(--secondary-blue); border-radius: 2px; transform: rotate(45deg); }
        @media (max-width: 992px) { .layout-container { flex-direction: column; } .sidebar { width: 100%; position: static; margin-bottom: 30px; } .main-content { padding: 30px; } }
    </style>
</head>"""

for i, (filename, title) in enumerate(data_modules):
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. New Head
    idx = i + 1
    head_content = new_head_style.replace("{idx}", str(idx)).replace("{title}", title)
    content = re.sub(r'<head>.*?</head>', head_content, content, flags=re.DOTALL)

    # 2. Navbar & Header Banner
    navbar_header = f"""<body>
    <nav class="navbar">
        <a href="data_index.html"><img src="Kvj logo.jpeg" alt="KVJ Logo" class="kvj-logo-img"></a>
        <a href="data_roadmap.html" class="logout-btn">EXIT</a>
    </nav>
    <header class="header-banner">
        <h1>MODULE {idx}: {title}</h1>
    </header>"""

    # 3. Sidebar setup
    sidebar_links = ""
    sidebar_items = [
        ("Data-Module-1.html", "01 Data Basics"),
        ("Data-Module-2.html", "02 Data Lifecycle"),
        ("Data-Module-3.html", "03 Data Analysis"),
        ("Data-Module-4.html", "04 Data Visualization"),
        ("Data-Module-5.html", "05 Data Ethics")
    ]
    for fn, lbl in sidebar_items:
        active_cls = ' class="active"' if fn == filename else ''
        sidebar_links += f'            <a href="{fn}"{active_cls}>{lbl}</a>\n'

    sidebar_block = f"""
    <div class="layout-container">
        <aside class="sidebar">
            <h3>Module Path</h3>
{sidebar_links}            <h3 style="margin-top:35px;">Navigation</h3>
            <a href="data_roadmap.html" style="background: #f8fafc;">&larr; Return to Roadmap</a>
        </aside>
        <main class="main-content">"""

    # 4. Content Extraction
    # Find start of content (after old hero or content wrapper)
    # Most modules have <div class="main-content"> or <div class="content">
    content_match = re.search(r'(<section class="lesson-section">.*?)<nav class="bottom-nav">', content, re.DOTALL)
    if not content_match:
        content_match = re.search(r'(<section class="lesson-section">.*?)<footer>', content, re.DOTALL)
    
    if content_match:
        inner_content = content_match.group(1)
    else:
        # Fallback for manually edited files
        inner_content = "<!-- Content extraction failed. Please check file structure. -->"

    # 5. Script preservation
    scripts_match = re.search(r'(<script>.*?</script>)', content, re.DOTALL | re.IGNORECASE)
    footer_scripts = scripts_match.group(1) if scripts_match else ""

    final_html = f"""<!DOCTYPE html>
<html lang="en">
{head_content}
{navbar_header}
{sidebar_block}
{inner_content}
        </main>
    </div>
    {footer_scripts}
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_html)

print("UI Standardization Complete!")
