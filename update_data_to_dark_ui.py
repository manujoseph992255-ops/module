import os
import re

directory = r"c:\Users\kj anand\Downloads\Quiz DD"
modules = ["Data-Module-1.html", "Data-Module-2.html", "Data-Module-3.html", "Data-Module-4.html", "Data-Module-5.html", "AI-Module-1.html", "AI-Module-2.html", "AI-Module-3.html", "AI-Module-4.html", "AI-Module-5.html", "AI-Module-6.html"]

dark_css = """
        /* Dark UI for Practice (matching Python coding-practice) */
        .practice-card {
            background: #1e293b;
            border-radius: 12px;
            padding: 30px;
            margin: 40px 0;
            color: #f8fafc;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            position: relative;
            border: none;
        }
        .practice-badge {
            display: none;
        }
        .practice-card h3 { 
            margin-top: 0; color: #38bdf8; font-size: 22px; font-weight: 700; border: none; padding-bottom: 0; margin-bottom: 20px; font-family: 'Outfit', sans-serif;
        }
        .practice-card p { color: #e2e8f0; font-size: 16px; margin-bottom: 20px; }
        .practice-card strong { color: #f8fafc; font-weight: 800; }
        
        .mcq-option {
            background: #0f172a; border: 1px solid #334155;
            padding: 15px 20px; border-radius: 8px; margin-bottom: 10px;
            cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 15px;
            color: #e2e8f0;
        }
        .mcq-option:hover { background: #1e293b; border-color: #38bdf8; }
        .mcq-option.selected { border-width: 2px; border-color: #38bdf8; }
        .mcq-option.correct { border-color: #10b981; background: rgba(16, 185, 129, 0.1); color: #10b981; }
        .mcq-option.wrong { border-color: #ef4444; background: rgba(239, 68, 68, 0.1); color: #ef4444; }
        .mcq-prefix { font-weight: 800; color: #38bdf8; }

        .tf-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid #334155; }
        .tf-statement { color: #e2e8f0; font-size: 15px; }
        .tf-btn { padding: 6px 15px; border: 1px solid #334155; background: #0f172a; color: #e2e8f0; border-radius: 6px; cursor: pointer; font-weight: 600; font-size: 13px; transition: all 0.2s; }
        .tf-btn.selected { background: #38bdf8; color: #0f172a; border-color: #38bdf8; }
        .tf-btn.correct { background: #10b981 !important; border-color: #10b981 !important; color: white !important; }
        .tf-btn.wrong { background: #ef4444 !important; border-color: #ef4444 !important; color: white !important; }

        .practice-dark-btn {
            background: #38bdf8; color: #0f172a; border: none;
            padding: 12px 25px; border-radius: 8px; font-weight: 700;
            font-size: 16px; cursor: pointer; transition: transform 0.2s; margin-top: 20px;
            margin-right: 10px; font-family: 'Outfit', sans-serif;
        }
        .practice-reset-btn {
            background: #334155; color: #f8fafc; border: none;
            padding: 12px 25px; border-radius: 8px; font-weight: 700;
            font-size: 16px; cursor: pointer; transition: transform 0.2s; margin-top: 20px;
            font-family: 'Outfit', sans-serif;
        }
        .practice-dark-btn:hover, .practice-reset-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
        .practice-reset-btn:hover { background: #475569; }

        .feedback-dark { margin-top: 15px; padding: 12px; border-radius: 8px; font-weight: 600; font-size: 14px; display: none; }
        .feedback-dark.correct { background: rgba(16, 185, 129, 0.1); color: #10b981; border: 1px solid #10b981; display: block; }
        .feedback-dark.wrong { background: rgba(239, 68, 68, 0.1); color: #ef4444; border: 1px solid #ef4444; display: block; }

        .dd-container select { 
            padding: 10px 15px; border-radius: 8px; background: #0f172a; 
            color: #f8fafc; border: 1px solid #334155; font-weight: 600;
            width: 220px; outline: none; transition: border-color 0.2s;
        }
        .dd-container select:focus { border-color: #38bdf8; }
        
        .mcq-option strong { margin-right: 10px; color: #f8fafc; }
        .dd-container select option { background: #0f172a; color: #f8fafc; }
"""

for module in modules:
    filepath = os.path.join(directory, module)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove old practice-card styles safely
    old_css_patterns = [
        r'\.practice-card \{.*?\}',
        r'\.practice-badge \{.*?\}',
        r'\.mcq-option \{.*?\}',
        r'\.mcq-option:hover \{.*?\}',
        r'\.mcq-option\.selected \{.*?\}',
        r'\.mcq-option\.correct \{.*?\}',
        r'\.mcq-option\.wrong \{.*?\}',
        r'\.tf-row \{.*?\}',
        r'\.tf-btn \{.*?\}',
        r'\.tf-btn\.selected \{.*?\}',
        r'\.tf-btn\.correct \{.*?\}',
        r'\.tf-btn\.wrong \{.*?\}',
        r'\.practice-dark-btn \{.*?\}',
        r'\.practice-reset-btn \{.*?\}',
        r'\.practice-dark-btn:hover.*?\}',
        r'\.practice-reset-btn:hover.*?\}',
        r'\.feedback-dark \{.*?\}',
        r'\.feedback-dark\.correct \{.*?\}',
        r'\.feedback-dark\.wrong \{.*?\}',
        r'\.dd-label \{.*?\}',
        r'\.dd-target select \{.*?\}',
        r'\.dd-target select:focus \{.*?\}',
        r'\.mcq-prefix \{.*?\}',
        r'\.dd-container select \{.*?\}',
        r'\.dd-container select:focus \{.*?\}',
    ]

    new_content = content
    for p in old_css_patterns:
        new_content = re.sub(p, '', new_content, flags=re.DOTALL)

    # Insert new dark CSS before </style>
    if "Dark UI for Practice" not in new_content:
        new_content = new_content.replace('</style>', dark_css + '\n</style>')

    # Regex loop to process and replace each one properly so we grab up to exactly the first <p>
    def replace_practice_header(match):
        p_tag_content = match.group(1)
        
        # Remove the leading "<strong>...:</strong> " from p_tag_content if it exists, use it as title maybe
        title = "Interactive"
        m_title = re.search(r'<strong>(.*?):?</strong>\s*(.*)', p_tag_content)
        if m_title and len(m_title.group(1).replace(":", "").strip()) > 0:
            title = m_title.group(1).replace(":", "").strip()
            rest = m_title.group(2)
            new_p = f'<p><strong>Challenge:</strong> {rest}</p>'
        else:
            new_p = f'<p><strong>Challenge:</strong> {p_tag_content}</p>'
            
        return f'<div class="practice-card">\n    <h3>Practice: {title}</h3>\n    {new_p}'

    # Sometimes it has <div class="practice-badge">PRACTICE</div> ...
    pattern = r'<div class="practice-card">\s*<div class="practice-badge">.*?</div>\s*<p>(.*?)</p>'
    new_content = re.sub(pattern, replace_practice_header, new_content, flags=re.IGNORECASE | re.DOTALL)
    
    # And if any already changed to <h3> but no challenge strong tag?
    # Leave it.

    # Button text replacements:
    # Python has "Run & Check"
    new_content = re.sub(r'>Verify<', '>Run & Check<', new_content)
    new_content = re.sub(r'>Verify Matches<', '>Run & Check<', new_content)
    new_content = re.sub(r'>Check Answers<', '>Run & Check<', new_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Updated data modules CSS to match dark python ui")
