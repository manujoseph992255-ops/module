import re
import os

source_path = r"c:\Users\kj anand\Downloads\Ceriport SQL 1 (1).html"
target_path = r"c:\Users\kj anand\Downloads\Quiz DD\SQL-Module-1.html"

with open(source_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Regex to find all page divs
page_pattern = re.compile(r'<div id="(page_\d+)"[^>]*>(.*?)</div>\s*</div>\s*</div>', re.DOTALL)
# Regex to find text elements within a page
element_pattern = re.compile(r'<div class="pdf24_01" style="left:([\d.]+)em;top:([\d.]+)em;">(.*?)</div>', re.DOTALL)

def clean_span(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    return text.strip()

def html_escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

SQL_KEYWORDS = ['CREATE ', 'DROP ', 'ALTER ', 'INSERT ', 'UPDATE ', 'DELETE ', 'SELECT ', 'USE ', 'TRUNCATE ', 'WHERE ', 'SET ', 'FROM ', 'VALUES ', 'INTO ', 'ORDER ', 'GROUP ', 'HAVING ', 'JOIN ', 'INNER ', 'LEFT ', 'RIGHT ', 'BETWEEN ', 'LIKE ', 'AND ', 'OR ']

def is_code_line(text):
    u = text.strip().upper()
    return any(u.startswith(k) for k in SQL_KEYWORDS) or u.startswith('(')

def generate_table(rows):
    html = '<table class="content-table"><tbody>'
    for i, row in enumerate(rows):
        is_header = (i == 0)
        html += '<tr class="header-row">' if is_header else '<tr>'
        tag = 'th' if is_header else 'td'
        for cell in row:
            html += f'<{tag}>{html_escape(cell)}</{tag}>'
        html += '</tr>'
    html += '</tbody></table>'
    return html

# ── Interspersed Practice Content ─────────────────────────────────────────────

PRACTICE_MAP = {
    6: '''<div class="sql-practice-area">
                    <h3 style="color: #60a5fa;">Practice: Create a Database & Table</h3>
                    <div style="display: flex; gap: 30px; margin-bottom: 20px;">
                        <div style="flex: 1;">
                            <p style="color: #94a3b8; margin-bottom: 15px;">Create a database named <code>StudentManagement</code> and use it. Then create a table named <code>Students</code> with columns <code>ID</code> (INT) and <code>Name</code> (VARCHAR(50)).</p>
                            <textarea id="editor-1" class="sql-editor" placeholder="Write your SQL here...">-- Write your SQL code here
</textarea>
                            <button class="check-btn" onclick="runSQL('1', 'create_table', 'Students')">Run Query</button>
                        </div>
                        <div style="width: 300px;">
                            <h4 style="color: #fff; font-size: 13px; margin-bottom: 10px; text-transform: uppercase;">Goal Structure</h4>
                            <table class="sql-results-table" style="font-size: 12px;">
                                <tr><th>Column</th><th>Type</th></tr>
                                <tr><td>ID</td><td>INT</td></tr>
                                <tr><td>Name</td><td>VARCHAR</td></tr>
                            </table>
                        </div>
                    </div>
                    <div id="output-1" class="sql-output-box"></div>
                    <p id="feedback-1" class="feedback-text" style="display:none; margin-top: 10px; font-weight: 700;"></p>
                </div>''',
    16: '''<div class="practice-space">
                    <h3>Knowledge Check: Keys</h3>
                    <p style="margin-bottom: 15px; font-weight: 600;">Which SQL key uniquely identifies a record but can contain one NULL value?</p>
                    <div class="option-card" onclick="checkAnswer(this, false)">Primary Key</div>
                    <div class="option-card" onclick="checkAnswer(this, true)">Unique Key</div>
                    <div class="option-card" onclick="checkAnswer(this, false)">Foreign Key</div>
                    <p id="feedback-k1" class="feedback-text" style="margin-top: 15px; font-weight: 700; display: none;"></p>
                </div>''',
    24: '''<div class="practice-space">
                    <h3>Knowledge Check: Normalization</h3>
                    <p style="margin-bottom: 15px; font-weight: 600;">Removal of Partial Dependency is characteristic of which Normal Form?</p>
                    <div class="option-card" onclick="checkAnswer(this, false)">1NF</div>
                    <div class="option-card" onclick="checkAnswer(this, true)">2NF</div>
                    <div class="option-card" onclick="checkAnswer(this, false)">3NF</div>
                    <p id="feedback-k2" class="feedback-text" style="margin-top: 15px; font-weight: 700; display: none;"></p>
                </div>''',
    47: '''<div class="practice-space">
                    <h3>Knowledge Check: Data Types</h3>
                    <p style="margin-bottom: 15px; font-weight: 600;">Which data type is best for storing large amounts of text content?</p>
                    <div class="option-card" onclick="checkAnswer(this, false)">CHAR</div>
                    <div class="option-card" onclick="checkAnswer(this, false)">VARCHAR(50)</div>
                    <div class="option-card" onclick="checkAnswer(this, true)">TEXT</div>
                    <p id="feedback-k3" class="feedback-text" style="margin-top: 15px; font-weight: 700; display: none;"></p>
                </div>''',
    68: '''<div class="sql-practice-area">
                    <h3 style="color: #60a5fa;">Practice: Inserting Data</h3>
                    <div style="display: flex; gap: 30px; margin-bottom: 20px;">
                        <div style="flex: 1;">
                            <p style="color: #94a3b8; margin-bottom: 15px;">Insert a record into the <code>Students</code> table: ID=101, Name='Rahul'.</p>
                            <textarea id="editor-2" class="sql-editor" placeholder="Write your SQL here...">-- Insert student record here
</textarea>
                            <button class="check-btn" onclick="runSQL('2', 'insert', 'Students')">Run Query</button>
                        </div>
                        <div style="width: 300px;">
                            <h4 style="color: #fff; font-size: 13px; margin-bottom: 10px; text-transform: uppercase;">Expected Result</h4>
                            <table class="sql-results-table" style="font-size: 12px;">
                                <tr><th>ID</th><th>Name</th></tr>
                                <tr><td>101</td><td>Rahul</td></tr>
                            </table>
                        </div>
                    </div>
                    <div id="output-2" class="sql-output-box"></div>
                    <p id="feedback-2" class="feedback-text" style="display:none; margin-top: 10px; font-weight: 700;"></p>
                </div>''',
    85: '''<div class="sql-practice-area">
                    <h3 style="color: #60a5fa;">Practice: Update & Delete</h3>
                    <div style="display: flex; gap: 30px; margin-bottom: 20px;">
                        <div style="flex: 1;">
                            <p style="color: #94a3b8; margin-bottom: 15px;">Update the student with ID 101 to set Name = 'Rohit', then delete record with ID 101.</p>
                            <textarea id="editor-3" class="sql-editor" placeholder="Write your SQL here...">-- Write update and delete queries
</textarea>
                            <button class="check-btn" onclick="runSQL('3', 'delete', 'Students')">Run Query</button>
                        </div>
                        <div style="width: 300px;">
                            <h4 style="color: #fff; font-size: 13px; margin-bottom: 10px; text-transform: uppercase;">Goal Output</h4>
                            <div style="color: #94a3b8; font-size: 12px; font-style: italic; border: 1px solid #334155; padding: 10px; border-radius: 4px;">Table should be empty after deletion.</div>
                        </div>
                    </div>
                    <div id="output-3" class="sql-output-box"></div>
                    <p id="feedback-3" class="feedback-text" style="display:none; margin-top: 10px; font-weight: 700;"></p>
                </div>''',
    100: '''<div class="sql-practice-area">
                    <h3 style="color: #60a5fa;">Practice: Selecting Data</h3>
                    <div style="display: flex; gap: 30px; margin-bottom: 20px;">
                        <div style="flex: 1;">
                            <p style="color: #94a3b8; margin-bottom: 15px;">Select all columns from the <code>Students</code> table.</p>
                            <textarea id="editor-4" class="sql-editor" placeholder="Write your SQL here...">-- Write your select query
</textarea>
                            <button class="check-btn" onclick="runSQL('4', 'select', 'Students')">Run Query</button>
                        </div>
                        <div style="width: 300px;">
                            <h4 style="color: #fff; font-size: 13px; margin-bottom: 10px; text-transform: uppercase;">Expected Output</h4>
                            <table class="sql-results-table" style="font-size: 12px;">
                                <tr><th>ID</th><th>Name</th></tr>
                                <tr><td>101</td><td>Rahul</td></tr>
                            </table>
                            <p style="color: #64748b; font-size: 11px; margin-top: 5px;">(Note: Output depends on previous insert/update steps)</p>
                        </div>
                    </div>
                    <div id="output-4" class="sql-output-box"></div>
                    <p id="feedback-4" class="feedback-text" style="display:none; margin-top: 10px; font-weight: 700;"></p>
                </div>'''
}

CASE_STUDY_FINAL = '''<h2 style="margin: 40px 0 20px; font-weight: 800; font-size: 26px;">Case Study: Sales Management</h2>
                <div class="sql-practice-area" style="border: 2px solid var(--accent);">
                    <h3 style="color: #60a5fa;">Final Case Study: Execute All Steps</h3>
                    <div style="display: flex; gap: 30px; margin-bottom: 20px;">
                        <div style="flex: 1;">
                            <p style="color: #94a3b8; margin-bottom: 15px;">Run all steps: Create Orders table, insert 3 records, update ID 3, delete low value orders, and select remaining.</p>
                            <textarea id="editor-5" class="sql-editor" style="height: 250px;">-- Write full sequence: CREATE, INSERTs, UPDATE, DELETE, SELECT
</textarea>
                            <button class="check-btn" onclick="runSQL('5', 'select', 'Orders')">Execute All Steps</button>
                        </div>
                        <div style="width: 350px;">
                            <h4 style="color: #fff; font-size: 13px; margin-bottom: 10px; text-transform: uppercase;">Final Expected Table</h4>
                            <table class="sql-results-table" style="font-size: 12px;">
                                <tr><th>OrderID</th><th>CustomerName</th><th>Product</th><th>Quantity</th><th>OrderDate</th><th>Total</th></tr>
                                <tr><td>1</td><td>John Smith</td><td>Laptop</td><td>1</td><td>2024-01-10</td><td>75000.00</td></tr>
                                <tr><td>2</td><td>Mary Johnson</td><td>Mobile Phone</td><td>3</td><td>2024-02-15</td><td>75000.00</td></tr>
                            </table>
                        </div>
                    </div>
                    <div id="output-5" class="sql-output-box"></div>
                    <p id="feedback-5" class="feedback-text" style="display:none; margin-top: 10px; font-weight: 700;"></p>
                </div>'''

# ── Extraction Logic ───────────────────────────────────────────────────────────

slides_html = []

for m_page in page_pattern.finditer(content):
    page_id = m_page.group(1)
    page_num = int(page_id.split('_')[1])
    page_content = m_page.group(2)
    
    elems = []
    for m_elem in element_pattern.finditer(page_content):
        left = float(m_elem.group(1))
        top = float(m_elem.group(2))
        text = clean_span(m_elem.group(3))
        if text:
            elems.append({'left': left, 'top': top, 'text': text})
    
    if not elems:
        continue
    
    # Sort elements by top (row) then left (column)
    elems.sort(key=lambda x: (round(x['top'], 1), x['left']))
    
    page_parts = [f'<div class="slide-block" id="slide-{page_num}">']
    
    rows = []
    current_row = []
    last_top = -1
    for e in elems:
        if last_top == -1 or abs(e['top'] - last_top) < 0.5:
            current_row.append(e)
        else:
            rows.append(current_row)
            current_row = [e]
        last_top = e['top']
    if current_row:
        rows.append(current_row)
    
    idx = 0
    # Determine Slide Title
    if rows and len(rows[0]) == 1 and len(rows[0][0]['text']) < 60 and not is_code_line(rows[0][0]['text']):
        page_parts.append(f'<h2 class="slide-title">{html_escape(rows[0][0]["text"])}</h2>')
        idx = 1
    
    code_buf = []
    list_buf = []
    
    def flush_code():
        if code_buf:
            page_parts.append(f'<pre>{html_escape(os.linesep.join(code_buf))}</pre>')
            code_buf.clear()
            
    def flush_list():
        if list_buf:
            page_parts.append('<ul>' + ''.join(f'<li>{html_escape(item)}</li>' for item in list_buf) + '</ul>')
            list_buf.clear()

    skip_until_next_block = False
    while idx < len(rows):
        row = rows[idx]
        row_text = ' '.join(cell['text'] for cell in row)

        # Suppress original solution markers
        if "Expected Answer" in row_text or "Expected Result" in row_text:
            flush_code()
            flush_list()
            # Do not append this row, and effectively stop showing code in this block
            # because the next thing is usually a <pre> with the answer.
            skip_until_next_block = True
            idx += 1
            continue
        
        if skip_until_next_block:
            # If we are in skip mode, we only skip code lines (the actual solution)
            if is_code_line(row_text) or len(row_text) < 5: 
                idx += 1
                continue
            else:
                skip_until_next_block = False

        is_table = len(row) > 1 and all(abs(row[i+1]['left'] - row[i]['left']) > 10 for i in range(len(row)-1))
        
        if is_table:
            flush_code()
            flush_list()
            table_rows = []
            while idx < len(rows) and len(rows[idx]) == len(row):
                table_rows.append([cell['text'] for cell in rows[idx]])
                idx += 1
            page_parts.append(generate_table(table_rows))
            continue
        
        if len(row) == 1 and len(row[0]['text']) < 50 and row[0]['text'].isupper():
            flush_code()
            flush_list()
            page_parts.append(f'<h4>{html_escape(row[0]["text"])}</h4>')
        elif is_code_line(row_text):
            flush_list()
            code_buf.append(row_text)
        elif row_text.startswith(('●', '•', '○')):
            flush_code()
            list_buf.append(row_text.lstrip('●•○ '))
        elif code_buf:
            code_buf.append(row_text)
        else:
            flush_code()
            flush_list()
            page_parts.append(f'<p>{html_escape(row_text)}</p>')
        
        idx += 1
    
    flush_code()
    flush_list()
    page_parts.append('</div>')
    slides_html.append('\n'.join(page_parts))
    
    if page_num in PRACTICE_MAP:
        slides_html.append(PRACTICE_MAP[page_num])

slides_html.append(CASE_STUDY_FINAL)
final_integrated_content = '\n\n'.join(slides_html)

# ── Assemble ──────────────────────────────────────────────────────────────────

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL Module 1 | KVJ Analytics</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Outfit:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.6.2/sql-wasm.js"></script>
    <style>
        :root {{
            --primary: #1a202c;
            --secondary: #2d3748;
            --accent: #4a90e2;
            --accent-glow: rgba(74, 144, 226, 0.3);
            --bg-body: #f8fafc;
            --card-bg: rgba(255, 255, 255, 0.9);
            --text-main: #2d3748;
            --text-muted: #718096;
            --border: #e2e8f0;
            --success: #48bb78;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        
        body {{ 
            font-family: 'Outfit', sans-serif; 
            background: var(--bg-body);
            color: var(--text-main); 
            line-height: 1.7;
        }}

        .navbar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.2rem 4rem;
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid var(--border);
            position: fixed;
            top: 0; width: 100%;
            z-index: 1000;
        }}

        .kvj-logo-img {{ max-height: 38px; }}

        .exit-btn {{
            background: #f1f5f9;
            color: #64748b;
            padding: 10px 22px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            border-radius: 8px;
            transition: all 0.3s;
            text-transform: uppercase;
            border: 1px solid #e2e8f0;
        }}
        .exit-btn:hover {{ background: #e2e8f0; color: #1e293b; }}

        .header-banner {{ 
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: white; 
            padding: 140px 20px 80px; 
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        .header-banner h1 {{ 
            font-family: 'Montserrat', sans-serif;
            font-size: 42px; 
            font-weight: 900; 
            letter-spacing: -1.5px; 
            position: relative;
            z-index: 1;
        }}

        .layout-container {{
            display: flex;
            max-width: 1400px;
            margin: -40px auto 60px;
            gap: 40px;
            width: 95%;
            position: relative;
            z-index: 2;
        }}

        .sidebar {{
            width: 320px;
            background: white;
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.05);
            height: fit-content;
            position: sticky;
            top: 100px;
        }}

        .sidebar a {{ 
            display: flex; 
            padding: 14px 18px; 
            color: #64748b; 
            text-decoration: none; 
            font-size: 15px; 
            font-weight: 600;
            margin-bottom: 8px;
            border-radius: 12px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .sidebar a:hover {{ background: #f1f5f9; color: var(--accent); transform: translateX(5px); }}
        .sidebar a.active {{ 
            background: var(--accent); 
            color: white; 
            box-shadow: 0 8px 15px var(--accent-glow);
        }}

        .main-content {{ 
            flex: 1;
            background: white; 
            padding: 80px;
            border-radius: 24px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.04);
        }}

        .section-header h2 {{ 
            font-family: 'Montserrat', sans-serif;
            font-size: 32px; 
            font-weight: 900; 
            color: var(--primary);
            margin-bottom: 15px;
        }}
        .section-header p {{ font-size: 18px; color: var(--text-muted); }}

        pre {{
            background: #1e293b;
            color: #e2e8f0;
            padding: 25px;
            border-radius: 14px;
            font-family: 'Fira Code', monospace;
            font-size: 14px;
            margin: 25px 0;
            overflow-x: auto;
        }}

        .content-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: #fff;
            color: #1a202c;
        }}
        .content-table th, .content-table td {{
            border: 1px solid #e2e8f0;
            padding: 12px;
            text-align: left;
        }}
        .content-table th {{ background: #f8fafc; font-weight: 700; }}
        
        .slide-block {{
            margin-bottom: 50px;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 30px;
        }}
        .slide-title {{
            color: var(--primary);
            font-size: 24px;
            font-weight: 800;
            margin-top: 30px;
        }}

        .practice-space {{
            margin: 50px 0;
            padding: 40px;
            background: #f0f7ff;
            border-radius: 20px;
            border: 2px dashed #cbd5e1;
        }}
        .option-card {{
            background: white;
            padding: 15px 20px;
            border-radius: 12px;
            margin-bottom: 12px;
            cursor: pointer;
            border: 2px solid transparent;
            font-weight: 500;
        }}
        .option-card:hover {{ border-color: var(--accent); }}
        .option-card.correct {{ background: #d1fae5; border-color: #10b981; }}
        .option-card.wrong {{ background: #fee2e2; border-color: #ef4444; }}

        .sql-practice-area {{ background: #1e293b; padding: 25px; border-radius: 16px; margin: 30px 0; }}
        .sql-editor {{
            width: 100%; height: 120px; background: #2d3748; color: #e2e8f0;
            border: 1px solid #4a5568; border-radius: 8px; padding: 15px;
            font-family: 'Fira Code', monospace; font-size: 14px; margin-bottom: 15px;
        }}
        .sql-output-box {{
            background: #0f172a; color: #10b981; padding: 15px; border-radius: 8px;
            font-family: monospace; font-size: 13px; margin-top: 15px; display: none;
        }}
        .check-btn {{ background: var(--accent); color: white; border: none; padding: 12px 25px; border-radius: 8px; cursor: pointer; font-weight: 700; }}

        @media (max-width: 1024px) {{
            .layout-container {{ flex-direction: column; }}
            .sidebar {{ width: 100%; position: static; }}
            .main-content {{ padding: 40px; }}
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <a href="sql_index.html"><img src="Kvj logo.jpeg" alt="KVJ Analytics Logo" class="kvj-logo-img"></a>
        <a href="sql_roadmap.html" class="exit-btn">Roadmap</a>
    </nav>

    <header class="header-banner">
        <h1 id="module-title-header">SQL MODULE 1</h1>
    </header>

    <div class="layout-container">
        <nav class="sidebar">
            <h3>Learning Path</h3>
            <a href="SQL-Module-1.html" class="active">1. Foundations of SQL</a>
            <a href="SQL-Module-2.html">2. Data Retrieval</a>
            <a href="SQL-Module-3.html">3. Complex Filtering</a>
            <a href="SQL-Module-4.html">4. Relational Joins</a>
            <a href="SQL-Module-5.html">5. Data Aggregation</a>
            <a href="SQL-Module-6.html">6. Advanced Subqueries</a>
        </nav>

        <main class="main-content">
            <div class="section-header">
                <h2>Module 1: Foundations of SQL &amp; RDBMS</h2>
                <p>Complete Certiport SQL Module 1 content — 113 slides with tables and practice.</p>
            </div>
            
            <div class="lesson-text">
{final_integrated_content}
            </div>

            <div style="margin-top: 60px; padding: 40px; background: var(--primary); color: white; border-radius: 20px; text-align: center;">
                <h3 style="margin-bottom: 15px;">Module 1 Complete!</h3>
                <p style="margin-bottom: 25px; opacity: 0.9;">You've mastered the foundations of SQL and RDBMS. Next, we will explore Data Retrieval (Module 2).</p>
                <a href="SQL-Module-2.html" class="check-btn" style="background: white; color: var(--primary); text-decoration: none;">Continue to Module 2 &rarr;</a>
            </div>
        </main>
    </div>

    <script>
        let db;
        initSqlJs({{ locateFile: file => `https://cdnjs.cloudflare.com/ajax/libs/sql.js/1.6.2/${{file}}` }}).then(SQL => {{
            db = new SQL.Database();
        }});

        function runSQL(id, type, tableName) {{
            const code = document.getElementById(`editor-${{id}}`).value;
            const output = document.getElementById(`output-${{id}}`);
            const feedback = document.getElementById(`feedback-${{id}}`);
            output.style.display = 'block';
            output.innerHTML = '';
            output.className = 'sql-output-box';

            try {{
                const res = db.exec(code);
                
                // If it was a modifying query (INSERT, UPDATE, DELETE), 
                // automatically show the table state afterwards
                let displayRes = res;
                if (res.length === 0 && tableName && (code.toUpperCase().includes('INSERT') || code.toUpperCase().includes('UPDATE') || code.toUpperCase().includes('DELETE'))) {{
                    displayRes = db.exec(`SELECT * FROM ${{tableName}}`);
                }}

                if (displayRes.length > 0) {{
                    let table = '<table class="sql-results-table"><tr>';
                    displayRes[0].columns.forEach(col => table += `<th>${{col}}</th>`);
                    table += '</tr>';
                    displayRes[0].values.forEach(row => {{
                        table += '<tr>';
                        row.forEach(val => table += `<td>${{val}}</td>`);
                        table += '</tr>';
                    }});
                    table += '</table>';
                    output.innerHTML = table;
                }} else if (res.length === 0) {{
                    output.innerHTML = 'Query executed successfully.';
                }}

                // Basic validation
                let isCorrect = false;
                if (type === 'create_table') {{
                    const check = db.exec(`SELECT name FROM sqlite_master WHERE type='table' AND name='${{tableName}}'`);
                    isCorrect = check.length > 0;
                }} else if (type === 'insert') {{
                    const check = db.exec(`SELECT COUNT(*) FROM ${{tableName}}`);
                    isCorrect = check[0].values[0][0] > 0;
                }} else if (type === 'select') {{
                    isCorrect = res.length > 0;
                }} else if (type === 'delete') {{
                    const check = db.exec(`SELECT COUNT(*) FROM ${{tableName}}`);
                    isCorrect = check[0].values[0][0] == 0;
                }}

                if (isCorrect) {{
                    feedback.style.display = 'block';
                    feedback.style.color = '#10b981';
                    feedback.innerText = '✅ Correct! Great job.';
                }}
            }} catch (err) {{
                output.style.display = 'block';
                output.className = 'sql-output-box error';
                output.innerText = 'Error: ' + err.message;
            }}
        }}

        function checkAnswer(el, isCorrect) {{
            const cards = el.parentElement.querySelectorAll('.option-card');
            cards.forEach(c => c.classList.remove('correct', 'wrong'));
            const feedback = el.parentElement.querySelector('.feedback-text');
            
            if (isCorrect) {{
                el.classList.add('correct');
                feedback.innerText = '✅ Correct!';
                feedback.style.color = '#10b981';
            }} else {{
                el.classList.add('wrong');
                feedback.innerText = '❌ Incorrect. Try again.';
                feedback.style.color = '#ef4444';
            }}
            feedback.style.display = 'block';
        }}
    </script>
</body>
</html>'''

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Build Complete. Total Pages: {len(slides_html)}")
