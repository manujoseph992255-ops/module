import re
import os

directory = r"c:\Users\kj anand\Downloads\Quiz DD"

modules = [f for f in os.listdir(directory) if f.endswith('.html') and 'Module' in f]

quiz_cta_css = """
        /* Quiz CTA Styling */
        .quiz-cta {
            margin-top: 60px;
            padding: 40px;
            background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
            border-radius: 12px;
            text-align: center;
            color: white;
            box-shadow: 0 10px 30px rgba(0, 142, 171, 0.2);
        }
        .quiz-cta h3 { color: #ffffff !important; margin-top: 0; font-size: 24px; border: none; padding: 0; }
        .quiz-cta p { color: #ffffff !important; opacity: 0.95; margin-bottom: 25px; }
        .btn-start-quiz {
            display: inline-block;
            background: #ffffff;
            color: var(--primary-blue);
            text-decoration: none;
            padding: 16px 40px;
            border-radius: 30px;
            font-weight: 800;
            font-size: 15px;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s;
        }
        .btn-start-quiz:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            background: #f8fafc;
        }
"""

illustration_html = """
            <div class="illustration-container-inline" style="display: flex; gap: 30px; margin: 30px 0; justify-content: center; flex-wrap: wrap;">
                <div class="illustration-card" style="background: white; border: 1px solid var(--border-color); border-radius: 15px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); text-align: center; width: 220px;">
                    <img src="https://img.icons8.com/isometric/100/database.png" alt="Structured Data" style="width: 80px; margin-bottom: 10px;">
                    <span style="display: block; font-weight: 800; color: var(--primary-blue); font-size: 14px; text-transform: uppercase;">Structured Data</span>
                    <p style="font-size: 12px; color: var(--text-muted); margin-top: 5px; line-height: 1.4; margin-bottom: 0;">Spreadsheets, SQL Tables, Rows & Columns</p>
                </div>
                <div class="illustration-card" style="background: white; border: 1px solid var(--border-color); border-radius: 15px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); text-align: center; width: 220px;">
                    <img src="https://img.icons8.com/isometric/100/documents.png" alt="Unstructured Data" style="width: 80px; margin-bottom: 10px;">
                    <span style="display: block; font-weight: 800; color: var(--primary-blue); font-size: 14px; text-transform: uppercase;">Unstructured Data</span>
                    <p style="font-size: 12px; color: var(--text-muted); margin-top: 5px; line-height: 1.4; margin-bottom: 0;">Emails, Videos, Social Media, Audio Files</p>
                </div>
            </div>
"""

for mod in modules:
    path = os.path.join(directory, mod)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    changed = False
    
    # 1. Insert CSS if missing
    if '.quiz-cta {' not in html:
        html = html.replace('</style>', quiz_cta_css + '\n</style>')
        changed = True
        print(f"Added CSS to {mod}")

    # 2. Add image specifically for Data-Module-1.html
    if mod == 'Data-Module-1.html':
        if 'illustration-container-inline' not in html:
            # We insert it right after the insight box in section 6
            pattern = re.compile(r'(<h2>6\. Structured vs Unstructured Data</h2>.*?<strong>Insight:</strong> Most modern data generated online is unstructured.\s*</div>)', re.DOTALL)
            match = pattern.search(html)
            if match:
                html = html.replace(match.group(1), match.group(1) + illustration_html)
                changed = True
                print("Added illustration to Data-Module-1.html")

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

print("Done fixing HTML and CSS.")
