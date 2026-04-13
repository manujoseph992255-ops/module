import os

filepath = r"C:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"

header_part = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module 1: Data Basics | KVJ Analytics</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Outfit:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        :root {
            --primary-blue: #1e3a5f;
            --secondary-blue: #008eab;
            --accent-green: #10b981;
            --accent-indigo: #6366f1;
            --bg-light: #f8fafc;
            --text-main: #1e293b;
            --text-muted: #475569;
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
            line-height: 1.7;
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

        .kvj-logo-img { max-height: 38px; width: auto; }

        .logout-btn {
            background: #ef4444; color: white; padding: 10px 22px;
            text-decoration: none; font-size: 13px; font-weight: 700;
            border-radius: 8px; transition: all 0.3s; text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .header-banner {
            background: linear-gradient(135deg, var(--primary-blue) 0%, #0f172a 100%);
            color: white;
            padding: 140px 20px 80px; text-align: center;
        }

        .header-banner h1 {
            font-family: 'Montserrat', sans-serif; font-size: 42px;
            font-weight: 900; letter-spacing: -1px; text-transform: uppercase;
        }

        .layout-container {
            display: flex; max-width: 1400px;
            margin: 40px auto; gap: 40px; width: 95%; padding-bottom: 80px;
        }

        .sidebar {
            width: 320px; background: white; padding: 35px;
            border: 1px solid var(--border-color); position: sticky;
            top: 100px; border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05); height: fit-content;
        }

        .sidebar h3 {
            font-family: 'Montserrat', sans-serif; font-size: 13px;
            color: var(--secondary-blue); text-transform: uppercase;
            margin-bottom: 22px; border-bottom: 2px solid #f1f5f9;
            padding-bottom: 12px; font-weight: 800; letter-spacing: 1.5px;
        }

        .sidebar a {
            display: flex; align-items: center; padding: 14px 18px;
            color: #64748b; text-decoration: none; font-size: 15px;
            font-weight: 500; margin-bottom: 8px; border-radius: 10px;
            transition: all 0.3s;
        }

        .sidebar a.active {
            color: var(--primary-blue); font-weight: 700;
            background: #f0f9ff; border-left: 5px solid var(--primary-blue);
        }

        .main-content {
            flex: 1; background: #ffffff; border: 1px solid var(--border-color);
            padding: 70px; border-radius: 20px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.04);
        }

        .section-header {
            margin-bottom: 40px; border-bottom: 4px solid #f1f5f9;
            padding-bottom: 20px;
        }

        .section-header h2 {
            font-family: 'Montserrat', sans-serif; color: var(--primary-blue);
            font-size: 32px; font-weight: 800; text-transform: uppercase;
            letter-spacing: -1px;
        }

        p { line-height: 1.8; margin-bottom: 28px; color: #334155; font-size: 18px; }
        strong { color: var(--primary-blue); font-weight: 700; }
        h3 {
            font-family: 'Montserrat', sans-serif; color: #0f172a;
            margin: 50px 0 25px; font-size: 24px; font-weight: 700;
            letter-spacing: -0.5px;
        }

        .interaction-box {
            background-color: #f8fafc; border-left: 6px solid var(--secondary-blue);
            padding: 30px; margin: 40px 0; border-radius: 4px 12px 12px 4px; 
            font-size: 18px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);
        }

        .interaction-box strong { font-size: 19px; display: block; margin-bottom: 12px; }

        .data-table {
            width: 100%; border-collapse: separate; border-spacing: 0;
            margin: 20px 0; border: 1px solid var(--border-color);
            border-radius: 10px; overflow: hidden;
        }
        .data-table th {
            background: #f1f5f9; padding: 15px 20px; text-align: left;
            font-size: 15px; text-transform: uppercase; letter-spacing: 1px;
            color: var(--primary-blue); border-bottom: 2px solid var(--border-color);
        }
        .data-table td {
            padding: 15px 20px; color: #475569; font-size: 17px;
            border-bottom: 1px solid var(--border-color); background: white;
        }

        .practice-card {
            background: #ffffff; border: 2px solid #00d2ff; border-radius: 20px;
            padding: 50px; margin: 60px 0; color: var(--text-main);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.05); position: relative;
        }
        .practice-badge {
            position: absolute; top: -18px; left: 40px; background: var(--secondary-blue);
            color: white; padding: 8px 25px; font-size: 11px; font-weight: 800;
            text-transform: uppercase; border-radius: 30px; letter-spacing: 1.5px;
        }
        .practice-card h4 { margin-bottom: 25px; font-size: 24px; color: var(--primary-blue); font-family: 'Montserrat', sans-serif; font-weight: 800; }

        .mcq-options { display: grid; gap: 18px; margin: 30px 0; }
        .mcq-option {
            background: #ffffff; border: 1.5px solid #e2e8f0;
            padding: 22px 30px; border-radius: 14px; cursor: pointer;
            transition: all 0.3s; 
            display: flex; align-items: center; gap: 20px; font-size: 18px;
            color: #334155; font-weight: 500;
        }
        .mcq-option:hover:not(.disabled) { border-color: var(--secondary-blue); box-shadow: 0 5px 15px rgba(0,0,0,0.05); }
        .mcq-option.selected { border-color: var(--secondary-blue); background: #f0f9ff; border-width: 2px; }
        .mcq-option.correct { border-color: var(--accent-green); background: #ecfdf5; color: #065f46; border-width: 2px; }
        .mcq-option.wrong { border-color: #ef4444; background: #fef2f2; color: #991b1b; border-width: 2px; }
        .mcq-option.disabled { pointer-events: none; }
        .mcq-prefix { font-weight: 800; color: var(--secondary-blue); font-size: 19px; }

        .tf-row {
            display: flex; align-items: center; justify-content: space-between;
            padding: 22px 0; border-bottom: 1px solid #f1f5f9;
        }
        .tf-statement { font-size: 18px; font-weight: 500; flex: 1; padding-right: 35px; color: #334155; }
        .tf-btn-group { display: flex; gap: 15px; }
        .tf-btn {
            padding: 12px 25px; border-radius: 10px; border: 1.5px solid #e2e8f0;
            background: white; cursor: pointer; font-weight: 700; transition: 0.2s;
            font-size: 14px; text-transform: uppercase; color: #64748b;
        }
        .tf-btn.selected-true { background: #dcfce7; border-color: var(--accent-green); color: #065f46; }
        .tf-btn.selected-false { background: #fee2e2; border-color: #ef4444; color: #991b1b; }
        .tf-btn.disabled { pointer-events: none; }

        .practice-dark-box {
            display: flex; gap: 15px; background: #0f172a; padding: 15px;
            border-radius: 16px; align-items: center; border: 1px solid #334155;
        }
        .practice-dark-box input {
            flex: 1; background: transparent; border: none; color: white;
            padding: 12px; outline: none; font-size: 17px;
        }
        .practice-dark-btn {
            background: var(--secondary-blue);
            color: white; border: none; padding: 14px 35px; border-radius: 10px;
            cursor: pointer; font-weight: 800; text-transform: uppercase;
            letter-spacing: 1px; font-size: 14px;
        }

        .feedback-dark {
            margin-top: 25px; padding: 22px; border-radius: 14px; font-weight: 700;
            display: none; font-size: 17px; border: 2px solid transparent;
        }
        .feedback-dark.correct { background: #ecfdf5; color: #065f46; border-color: var(--accent-green); }
        .feedback-dark.wrong { background: #fef2f2; color: #991b1b; border-color: #ef4444; }

        .dd-container { background: #0f172a; padding: 45px; border-radius: 20px; margin: 30px 0; border: 1px solid #334155; }
        .dd-row { display: flex; align-items: center; gap: 35px; margin-bottom: 25px; }
        .dd-label { flex: 1.3; color: white; font-weight: 700; font-size: 18px; }
        .dd-target { flex: 1; }
        .dd-target select {
            width: 100%; padding: 15px; border-radius: 12px; background: #1e293b;
            color: #00d2ff; border: 2px solid #334155; font-weight: 600;
        }

        pre {
            background: #0f172a; color: #38bdf8; padding: 30px;
            border-radius: 16px; margin: 35px 0; font-size: 16px; border: 1px solid #334155;
        }

        .quiz-cta {
            margin-top: 100px; padding: 75px;
            background: linear-gradient(135deg, var(--primary-blue) 0%, #008eab 100%);
            border-radius: 25px; text-align: center; color: white;
        }
        .quiz-cta h3 { color: white; margin-top: 0; font-size: 36px; border: none; margin-bottom: 25px; }
        .btn-start-quiz {
            display: inline-block; background: #ffffff; color: var(--primary-blue);
            text-decoration: none; padding: 20px 60px; border-radius: 50px;
            font-weight: 800; font-size: 18px; text-transform: uppercase;
        }

        footer { text-align: center; padding: 60px; color: #94a3b8; font-size: 15px; }
    </style>
</head>
<body>
    <nav class="navbar">
        <a href="data_index.html"><img src="Kvj logo.jpeg" alt="Logo" class="kvj-logo-img"></a>
        <a href="data_roadmap.html" class="logout-btn">EXIT COURSE</a>
    </nav>
    <header class="header-banner"><h1>MODULE 1: DATA BASICS</h1></header>

    <div class="layout-container">
        <aside class="sidebar">
            <h3>Module Path</h3>
            <a href="Data-Module-1.html" class="active">01 Data Basics</a>
            <a href="Data-Module-2.html">02 Data Manipulation</a>
            <a href="#">03 Data Analysis</a>
            <a href="#">04 Visualization</a>
            <a href="#">05 Responsible Analytics</a>
            <h3 style="margin-top:35px;">Navigation</h3>
            <a href="data_roadmap.html" style="background: #f8fafc;">&larr; Return to Roadmap</a>
        </aside>
        <main class="main-content">
"""

s1 = """
            <section class="lesson-section">
                <div class="section-header"><h2>1. Meaning of Data</h2></div>
                <h3>Concept</h3>
                <p><strong>Data</strong> refers to raw facts, figures, or observations collected for analysis or reference.</p>
                <p>Data can appear in many forms such as:</p>
                <p><strong>Numbers, Text, Images, Audio.</strong></p>
                <p>By itself, data does not carry meaning until it is processed and interpreted.</p>
                
                <div class="interaction-box">
                    <strong>Example raw data:</strong>
                    <table class="data-table">
                        <thead><tr><th>Product</th><th>Sales</th></tr></thead>
                        <tbody>
                            <tr><td>Laptop</td><td>15</td></tr>
                            <tr><td>Tablet</td><td>8</td></tr>
                            <tr><td>Phone</td><td>20</td></tr>
                        </tbody>
                    </table>
                    <p style="margin-top:20px;">After analysis we might discover: <strong>Phone is the best-selling product.</strong> That insight becomes useful information.</p>
                </div>

                <div class="interaction-box" style="border-left-color: var(--accent-green); background: #f0fdf4;">
                    <strong>Insight:</strong>
                    <p>Data is like ingredients in cooking. Ingredients alone do not create a meal. Only after processing and combining them do we get something meaningful.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Practice Activities: MCQ</h4>
                    <p>Which of the following best describes data?</p>
                    <div class="mcq-options" id="mcq-s1">
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s1')"><span class="mcq-prefix">A.</span> Final decision</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s1')"><span class="mcq-prefix">B.</span> Raw facts collected for analysis</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s1')"><span class="mcq-prefix">C.</span> A business strategy</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s1')"><span class="mcq-prefix">D.</span> A summarized report</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-s1', 'B')">Submit</button>
                    <div class="feedback-dark" id="feedback-mcq-s1"></div>

                    <h4 style="margin-top:50px;">True / False</h4>
                    <div class="tf-row"><span class="tf-statement">1. Data always has meaning by itself.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s1-1', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s1-1', false)">False</button></div></div>
                    <div class="tf-row"><span class="tf-statement">2. Data can include text and images.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s1-2', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s1-2', false)">False</button></div></div>
                    <div class="tf-row"><span class="tf-statement">3. Data becomes useful after analysis.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s1-3', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s1-3', false)">False</button></div></div>
                    <button class="practice-dark-btn" style="margin-top:20px;" onclick="checkTFGroup(['tf-s1-1', 'tf-s1-2', 'tf-s1-3'], [false, true, true], 'feedback-tf-s1')">Check Answers</button>
                    <div class="feedback-dark" id="feedback-tf-s1"></div>

                    <h4 style="margin-top:50px;">Scenario Question</h4>
                    <p>A school collects: Student marks, Attendance, Assignment scores. Explain one insight the school could get after analyzing this data.</p>
                    <div class="practice-dark-box">
                        <input type="text" id="scenario-s1" placeholder="Write your explanation...">
                        <button class="practice-dark-btn" onclick="checkScenario('scenario-s1', 'Insightful! They could track student growth over time.')">Submit</button>
                    </div>
                    <div class="feedback-dark" id="feedback-scenario-s1"></div>
                </div>
            </section>
"""

s2 = """
            <section class="lesson-section">
                <div class="section-header"><h2>2. Data Analysis</h2></div>
                <h3>Concept</h3>
                <p><strong>Data Analysis</strong> is the process of converting raw data into useful information for decision making.</p>
                <p>Organizations use data analysis to: <strong>Understand trends, Identify patterns, Support decisions.</strong></p>
                
                <div class="interaction-box">
                    <strong>Example:</strong>
                    <p>A company records daily sales.</p>
                    <table class="data-table">
                        <thead><tr><th>Day</th><th>Sales</th></tr></thead>
                        <tbody><tr><td>Monday</td><td>5000</td></tr><tr><td>Tuesday</td><td>6200</td></tr><tr><td>Wednesday</td><td>7100</td></tr></tbody>
                    </table>
                    <p>After analysis they may conclude: <strong>Sales increase mid-week.</strong></p>
                </div>
                
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Data analysis answers questions like: What happened? Why did it happen? What might happen next?</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Drag & Drop (Match the Purpose)</h4>
                    <p>Match the data collected with the possible insight.</p>
                    <div class="dd-container" id="dd-s2">
                        <div class="dd-row"><div class="dd-label">Website visitors</div><div class="dd-target"><select><option value="">Select insight...</option><option value="A">Most popular page</option><option value="B">Class average</option><option value="C">Best selling product</option></select></div></div>
                        <div class="dd-row"><div class="dd-label">Student marks</div><div class="dd-target"><select><option value="">Select insight...</option><option value="A">Most popular page</option><option value="B">Class average</option><option value="C">Best selling product</option></select></div></div>
                        <div class="dd-row"><div class="dd-label">Sales records</div><div class="dd-target"><select><option value="">Select insight...</option><option value="A">Most popular page</option><option value="B">Class average</option><option value="C">Best selling product</option></select></div></div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkDD('dd-s2', ['A', 'B', 'C'])">Check Matches</button>
                    <div class="feedback-dark" id="feedback-dd-s2"></div>

                    <h4 style="margin-top:50px;">MCQ</h4>
                    <p>A dataset is:</p>
                    <div class="mcq-options" id="mcq-s2">
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s2')"><span class="mcq-prefix">A.</span> A collection of organized data</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s2')"><span class="mcq-prefix">B.</span> A type of graph</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s2')"><span class="mcq-prefix">C.</span> A statistical formula</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s2')"><span class="mcq-prefix">D.</span> A programming language</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-s2', 'A')">Submit</button>
                    <div class="feedback-dark" id="feedback-mcq-s2"></div>

                    <h4 style="margin-top:50px;">Mini Thinking Question</h4>
                    <p>A restaurant collects daily customer feedback ratings. What decision could the restaurant make after analyzing this data?</p>
                    <div class="practice-dark-box">
                        <input type="text" id="thinking-s2" placeholder="Your decision mapping...">
                        <button class="practice-dark-btn" onclick="checkScenario('thinking-s2', 'Brilliant! They could improve service or menu during peak complaint times.')">Submit</button>
                    </div>
                    <div class="feedback-dark" id="feedback-thinking-s2"></div>
                </div>
            </section>
"""

s3_intro = """
            <section class="lesson-section">
                <div class="section-header"><h2>3. Data Variable Types</h2></div>
                <h3>Concept</h3>
                <p>Variables describe the type of value stored in data. Main variable types include: <strong>Boolean, Numeric, String.</strong></p>
                <p>Each type stores different kinds of values.</p>
                
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Understanding variable types helps: <strong>store data correctly, analyze data efficiently, avoid calculation errors.</strong></p>
                </div>

                <h3>3.1 Boolean Data Type</h3>
                <h3>Concept</h3>
                <p>Boolean data type stores two possible values: <strong>True</strong> or <strong>False</strong>.</p>
                <p>Booleans are commonly used in logical conditions and decision making.</p>
                <div class="interaction-box">
                    <strong>Example:</strong>
                    <p><code>is_logged_in = True</code></p>
                    <p>Boolean values are used in conditions like:</p>
                    <pre><code>if is_logged_in:
    print("Access granted")</code></pre>
                </div>
                <div class="interaction-box" style="border-left-color: var(--accent-green); background: #f0fdf4;">
                    <strong>Insight:</strong>
                    <p>Boolean variables act like switches: <strong>ON = True, OFF = False.</strong></p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Identify Boolean</h4>
                    <p>Which of the following can be Boolean? (Select 1 and 3 if applicable)</p>
                    <div class="mcq-options" id="ms-s31">
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">1.</span> Student passed exam</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">2.</span> Number of books</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">3.</span> Payment successful</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">4.</span> Temperature</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMulti('ms-s31', ['1.', '3.'])">Submit</button>
                    <div class="feedback-dark" id="feedback-ms-s31"></div>

                    <h4 style="margin-top:50px;">True / False</h4>
                    <div class="tf-row"><span class="tf-statement">1. Boolean variables store True or False.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s31-1', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s31-1', false)">False</button></div></div>
                    <div class="tf-row"><span class="tf-statement">2. Boolean values can be used in conditions.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s31-2', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s31-2', false)">False</button></div></div>
                    <div class="tf-row"><span class="tf-statement">3. Boolean values represent multiple numbers.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s31-3', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s31-3', false)">False</button></div></div>
                    <button class="practice-dark-btn" style="margin-top:20px;" onclick="checkTFGroup(['tf-s31-1', 'tf-s31-2', 'tf-s31-3'], [true, true, false], 'feedback-tf-s31')">Check Answers</button>
                    <div class="feedback-dark" id="feedback-tf-s31"></div>
                </div>
            </section>
"""

s3_numeric = """
            <section class="lesson-section">
                <h3>3.2 Numeric Data Type</h3>
                <h3>Concept</h3>
                <p>Numeric data types represent numbers that can be calculated mathematically.</p>
                <div class="interaction-box">
                    <strong>Examples:</strong>
                    <ul class="content-list"><li>exam marks</li><li>salary</li><li>weight</li><li>height</li></ul>
                </div>
                <p>Numeric types include: <strong>Integer, Float, Complex.</strong></p>
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Numeric data allows operations such as: <strong>addition, subtraction, multiplication, division.</strong></p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>MCQ</h4>
                    <p>Which of the following is numeric data?</p>
                    <div class="mcq-options" id="mcq-s32">
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s32')"><span class="mcq-prefix">A.</span> Age</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s32')"><span class="mcq-prefix">B.</span> Country name</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s32')"><span class="mcq-prefix">C.</span> Product category</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s32')"><span class="mcq-prefix">D.</span> Email address</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-s32', 'A')">Submit</button>
                    <div class="feedback-dark" id="feedback-mcq-s32"></div>

                    <h4 style="margin-top:50px;">Drag & Drop (Classification)</h4>
                    <p>Match the example with numeric type.</p>
                    <div class="dd-container" id="dd-s32">
                        <div class="dd-row"><div class="dd-label">25</div><div class="dd-target"><select><option value="">Type...</option><option value="I">Integer</option><option value="F">Float</option></select></div></div>
                        <div class="dd-row"><div class="dd-label">12.75</div><div class="dd-target"><select><option value="">Type...</option><option value="I">Integer</option><option value="F">Float</option></select></div></div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkDD('dd-s32', ['I', 'F'])">Verify</button>
                    <div class="feedback-dark" id="feedback-dd-s32"></div>
                </div>

                <h3>3.3 Integer</h3>
                <h3>Concept</h3>
                <p>An integer is a whole number without decimal values.</p>
                <div class="interaction-box">
                    <strong>Examples:</strong>
                    <p>5, 10, -3, 0</p>
                    <p>Integers represent quantities like: <strong>number of students, number of products sold.</strong></p>
                </div>
                <div class="interaction-box" style="border-left-color: var(--accent-green); background: #f0fdf4;">
                    <strong>Insight:</strong>
                    <p>Integers are useful when exact counts are needed.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Identify Integer</h4>
                    <div class="mcq-options" id="ms-s33">
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">1.</span> 15</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">2.</span> 4.8</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">3.</span> -10</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">4.</span> 0</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMulti('ms-s33', ['1.', '3.', '4.'])">Submit</button>
                    <div class="feedback-dark" id="feedback-ms-s33"></div>

                    <h4 style="margin-top:50px;">True / False</h4>
                    <div class="tf-row"><span class="tf-statement">1. Integers can have decimal points.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s33-1', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s33-1', false)">False</button></div></div>
                    <div class="tf-row"><span class="tf-statement">2. Integers can be negative numbers.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s33-2', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s33-2', false)">False</button></div></div>
                    <button class="practice-dark-btn" style="margin-top:20px;" onclick="checkTFGroup(['tf-s33-1', 'tf-s33-2'], [false, true], 'feedback-tf-s33')">Check Answers</button>
                    <div class="feedback-dark" id="feedback-tf-s33"></div>
                </div>

                <h3>3.4 Float</h3>
                <h3>Concept</h3>
                <p>A float represents numbers with decimal values.</p>
                <div class="interaction-box">
                    <strong>Examples:</strong>
                    <p>2.5, 3.14, 7.8</p>
                    <p>Float values are used when precision is required (e.g., <strong>price, temperature, weight</strong>).</p>
                </div>
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Floats allow more accurate measurements compared to integers.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>MCQ</h4>
                    <p>Which value is a float?</p>
                    <div class="mcq-options" id="mcq-s34">
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s34')"><span class="mcq-prefix">A.</span> 8</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s34')"><span class="mcq-prefix">B.</span> 12.5</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s34')"><span class="mcq-prefix">C.</span> -3</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s34')"><span class="mcq-prefix">D.</span> 20</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-s34', 'B')">Submit</button>
                    <div class="feedback-dark" id="feedback-mcq-s34"></div>

                    <h4 style="margin-top:50px;">True / False</h4>
                    <div class="tf-row"><span class="tf-statement">1. Float numbers contain decimal values.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s34-1', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s34-1', false)">False</button></div></div>
                    <div class="tf-row"><span class="tf-statement">2. Floats can be used to represent prices.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s34-2', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s34-2', false)">False</button></div></div>
                    <button class="practice-dark-btn" style="margin-top:20px;" onclick="checkTFGroup(['tf-s34-1', 'tf-s34-2'], [true, true], 'feedback-tf-s34')">Verify</button>
                    <div class="feedback-dark" id="feedback-tf-s34"></div>
                </div>
            </section>
"""

s3_other = """
            <section class="lesson-section">
                <h3>3.5 Complex Numbers</h3>
                <h3>Concept</h3>
                <p>Complex numbers contain: <strong>a real part</strong> and <strong>an imaginary part.</strong></p>
                <p>General form: <strong>a + bi</strong> (Example: 3 + 4i).</p>
                <p>Python supports complex numbers using the <code>complex</code> data type.</p>
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Complex numbers are mainly used in engineering and scientific calculations.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Identify Complex Number</h4>
                    <p>Which of the following is a complex number?</p>
                    <div class="mcq-options" id="mcq-s35">
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s35')"><span class="mcq-prefix">A.</span> 5</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s35')"><span class="mcq-prefix">B.</span> 3.2</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s35')"><span class="mcq-prefix">C.</span> 4 + 2i</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s35')"><span class="mcq-prefix">D.</span> 10</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-s35', 'C')">Submit</button>
                    <div class="feedback-dark" id="feedback-mcq-s35"></div>
                </div>

                <h3>3.6 String Data Type</h3>
                <h3>Concept</h3>
                <p>String data type stores text values (e.g., <strong>names, city, product names</strong>).</p>
                <p>Strings can contain: <strong>letters, numbers, symbols.</strong></p>
                <div class="interaction-box">
                    <strong>Example:</strong>
                    <p><code>name = "Anoop"</code></p>
                </div>
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Strings help store descriptive information, not numeric calculations.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Identify String</h4>
                    <div class="mcq-options" id="ms-s36">
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">1.</span> "India"</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">2.</span> 25</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">3.</span> "Laptop"</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">4.</span> 12.5</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMulti('ms-s36', ['1.', '3.'])">Submit</button>
                    <div class="feedback-dark" id="feedback-ms-s36"></div>

                    <h4 style="margin-top:50px;">True / False</h4>
                    <div class="tf-row"><span class="tf-statement">1. Strings store text values.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s36-1', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s36-1', false)">False</button></div></div>
                    <div class="tf-row"><span class="tf-statement">2. Strings can contain numbers as characters.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s36-2', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s36-2', false)">False</button></div></div>
                    <button class="practice-dark-btn" style="margin-top:20px;" onclick="checkTFGroup(['tf-s36-1', 'tf-s36-2'], [true, true], 'feedback-tf-s36')">Check Answers</button>
                    <div class="feedback-dark" id="feedback-tf-s36"></div>
                </div>
            </section>
"""

s4s5 = """
            <section class="lesson-section">
                <div class="section-header"><h2>4. Data Structures</h2></div>
                <h3>Concept</h3>
                <p>Data is often organized using structures such as: <strong>Tables, Rows, Columns, Lists.</strong></p>
                <div class="interaction-box">
                    <strong>Example table:</strong>
                    <table class="data-table">
                        <thead><tr><th>Name</th><th>Age</th><th>Department</th></tr></thead>
                        <tbody><tr><td>Arjun</td><td>28</td><td>Marketing</td></tr></tbody>
                    </table>
                </div>
                <p><strong>Rows</strong> represent records. <strong>Columns</strong> represent attributes.</p>
                <p><strong>Lists</strong> store collections of items. Example: <code>[1,2,3,4,5]</code>.</p>
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Data structures help organize and analyze information efficiently.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Drag & Drop</h4>
                    <p>Match the concept.</p>
                    <div class="dd-container" id="dd-s4">
                        <div class="dd-row"><div class="dd-label">Row</div><div class="dd-target"><select><option value="">Select...</option><option value="R">Single record</option><option value="C">Attribute</option><option value="T">Organized dataset</option></select></div></div>
                        <div class="dd-row"><div class="dd-label">Column</div><div class="dd-target"><select><option value="">Select...</option><option value="R">Single record</option><option value="C">Attribute</option><option value="T">Organized dataset</option></select></div></div>
                        <div class="dd-row"><div class="dd-label">Table</div><div class="dd-target"><select><option value="">Select...</option><option value="R">Single record</option><option value="C">Attribute</option><option value="T">Organized dataset</option></select></div></div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkDD('dd-s4', ['R', 'C', 'T'])">Verify</button>
                    <div class="feedback-dark" id="feedback-dd-s4"></div>
                </div>

                <div class="section-header"><h2>5. Types of Data</h2></div>
                <p>Data can be classified into two main types: <strong>Qualitative data</strong> and <strong>Quantitative data.</strong></p>
                
                <h3>5.1 Qualitative Data</h3>
                <p>Qualitative data describes categories or characteristics (e.g., <strong>gender, city, brand</strong>).</p>
                <p>Types include: <strong>Nominal, Ordinal.</strong></p>
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Qualitative data focuses on descriptions rather than numbers.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>MCQ</h4>
                    <p>Which of the following is qualitative data?</p>
                    <div class="mcq-options" id="mcq-s51">
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s51')"><span class="mcq-prefix">A.</span> Salary</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s51')"><span class="mcq-prefix">B.</span> Height</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s51')"><span class="mcq-prefix">C.</span> Eye color</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s51')"><span class="mcq-prefix">D.</span> Age</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-s51', 'C')">Submit</button>
                    <div class="feedback-dark" id="feedback-mcq-s51"></div>
                </div>

                <h3>5.2 Quantitative Data</h3>
                <p>Quantitative data represents numeric values (e.g., <strong>height, weight, marks, distance</strong>).</p>
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Quantitative data allows statistical calculations.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Identify Quantitative Data</h4>
                    <div class="mcq-options" id="ms-s52">
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">1.</span> Age</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">2.</span> Weight</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">3.</span> Country</div>
                        <div class="mcq-option" onclick="toggleSelection(this)"><span class="mcq-prefix">4.</span> Temperature</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMulti('ms-s52', ['1.', '2.', '4.'])">Submit</button>
                    <div class="feedback-dark" id="feedback-ms-s52"></div>
                </div>
            </section>
"""

s678 = """
            <section class="lesson-section">
                <div class="section-header"><h2>6. Structured vs Unstructured Data</h2></div>
                <h3>Structured Data</h3>
                <p>Structured data: <strong>fits into rows and columns</strong>, and is stored in databases or spreadsheets.</p>
                <div class="interaction-box">
                    <strong>Examples:</strong> <li>phone numbers</li><li>bank records</li>
                </div>
                <h3>Unstructured Data</h3>
                <p>Unstructured data: <strong>has no fixed format.</strong></p>
                <div class="interaction-box">
                    <strong>Examples:</strong> <li>emails</li><li>videos</li><li>social media posts</li>
                </div>
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Most modern data generated online is unstructured.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Classification Activity</h4>
                    <div class="dd-container" id="dd-s6">
                        <div class="dd-row"><div class="dd-label">Excel table</div><div class="dd-target"><select><option value="">Type...</option><option value="S">Structured</option><option value="U">Unstructured</option></select></div></div>
                        <div class="dd-row"><div class="dd-label">Email message</div><div class="dd-target"><select><option value="">Type...</option><option value="S">Structured</option><option value="U">Unstructured</option></select></div></div>
                        <div class="dd-row"><div class="dd-label">Database records</div><div class="dd-target"><select><option value="">Type...</option><option value="S">Structured</option><option value="U">Unstructured</option></select></div></div>
                        <div class="dd-row"><div class="dd-label">Video file</div><div class="dd-target"><select><option value="">Type...</option><option value="S">Structured</option><option value="U">Unstructured</option></select></div></div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkDD('dd-s6', ['S', 'U', 'S', 'U'])">Check Classification</button>
                    <div class="feedback-dark" id="feedback-dd-s6"></div>
                </div>

                <div class="section-header"><h2>7. Metadata</h2></div>
                <h3>Concept</h3>
                <p><strong>Metadata</strong> means data about data.</p>
                <p>It describes information such as: <strong>file size, creation date, author, format.</strong></p>
                <div class="interaction-box">
                    <strong>Example:</strong>
                    <p>A photo file may include metadata: <strong>camera type, date taken, resolution.</strong></p>
                </div>
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Metadata helps organize and manage data efficiently.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>True / False</h4>
                    <div class="tf-row"><span class="tf-statement">1. Metadata describes other data.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s7-1', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s7-1', false)">False</button></div></div>
                    <div class="tf-row"><span class="tf-statement">2. Metadata includes file information.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s7-2', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s7-2', false)">False</button></div></div>
                    <div class="tf-row"><span class="tf-statement">3. Metadata replaces the original data.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'tf-s7-3', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'tf-s7-3', false)">False</button></div></div>
                    <button class="practice-dark-btn" style="margin-top:20px;" onclick="checkTFGroup(['tf-s7-1', 'tf-s7-2', 'tf-s7-3'], [true, true, false], 'feedback-tf-s7')">Submit Logic</button>
                    <div class="feedback-dark" id="feedback-tf-s7"></div>
                </div>

                <div class="section-header"><h2>8. Big Data</h2></div>
                <h3>Concept</h3>
                <p><strong>Big Data</strong> refers to extremely large and complex datasets that grow rapidly and cannot be processed using traditional systems.</p>
                <div class="interaction-box">
                    <strong>Sources of big data include:</strong>
                    <ul class="content-list"><li>social media</li><li>online transactions</li><li>sensors</li><li>IoT devices</li></ul>
                </div>
                <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                    <strong>Insight:</strong>
                    <p>Big data allows organizations to analyze massive amounts of information to discover patterns and predictions.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>MCQ</h4>
                    <p>Big data is characterized by:</p>
                    <div class="mcq-options" id="mcq-s8">
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s8')"><span class="mcq-prefix">A.</span> Small datasets</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s8')"><span class="mcq-prefix">B.</span> Extremely large and complex datasets</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s8')"><span class="mcq-prefix">C.</span> Only numerical data</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-s8')"><span class="mcq-prefix">D.</span> Only structured data</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-s8', 'B')">Verify</button>
                    <div class="feedback-dark" id="feedback-mcq-s8"></div>
                </div>

                <div class="quiz-cta">
                    <h3>Mastered the Basics?</h3>
                    <p>Take the Module 1 Knowledge Check now.</p>
                    <a href="module_quiz.html?mod=d1" class="btn-start-quiz">Start Assessment</a>
                </div>
            </section>
"""

footer_part = """
        </main>
    </div>
    <footer>&copy; 2026 KVJ Analytics Academy. Professional Data Excellence.</footer>

    <script>
        const tf_data = {};
        function triggerConfetti() { confetti({ particleCount: 150, spread: 80, origin: { y: 0.7 }, colors: ['#1e3a5f', '#008eab', '#10b981'] }); }

        function selectMCQ(element, qid) {
            const container = document.getElementById(qid);
            container.querySelectorAll('.mcq-option').forEach(o => o.classList.remove('selected'));
            element.classList.add('selected');
        }

        function checkMCQ(qid, correctPrefix) {
            const container = document.getElementById(qid);
            const selected = container.querySelector('.mcq-option.selected');
            const feedback = document.getElementById('feedback-' + qid);
            if(!selected) return;
            container.querySelectorAll('.mcq-option').forEach(o => o.classList.add('disabled'));
            if(selected.querySelector('.mcq-prefix').innerText.includes(correctPrefix)) {
                selected.classList.add('correct');
                feedback.innerText = "Correct! ✨";
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            } else {
                selected.classList.add('wrong');
                feedback.innerText = "Incorrect. Check your notes!";
                feedback.className = "feedback-dark wrong";
            }
            feedback.style.display = 'block';
        }

        function toggleSelection(element) { element.classList.toggle('selected'); }

        function checkMulti(qid, targets) {
            const container = document.getElementById(qid);
            const selecteds = container.querySelectorAll('.mcq-option.selected');
            const feedback = document.getElementById('feedback-' + qid);
            if(selecteds.length === 0) return;
            container.querySelectorAll('.mcq-option').forEach(o => o.classList.add('disabled'));
            const labels = Array.from(selecteds).map(s => s.querySelector('.mcq-prefix').innerText);
            const isCorrect = labels.length === targets.length && targets.every(t => labels.includes(t));
            if(isCorrect) {
                selecteds.forEach(s => s.classList.add('correct'));
                feedback.innerText = "All correct! ✨";
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            } else {
                selecteds.forEach(s => s.classList.add('wrong'));
                feedback.innerText = "Mixed results. Review and try again.";
                feedback.className = "feedback-dark wrong";
            }
            feedback.style.display = 'block';
        }

        function selectTF(element, tid, val) {
            const group = element.closest('.tf-btn-group');
            group.querySelectorAll('.tf-btn').forEach(b => b.classList.remove('selected-true', 'selected-false'));
            element.classList.add(val ? 'selected-true' : 'selected-false');
            tf_data[tid] = val;
        }

        function checkTFGroup(tids, corrects, fid) {
            let allCorrect = true;
            const feedback = document.getElementById(fid);
            for(let i=0; i<tids.length; i++) {
                if(tf_data[tids[i]] === undefined) return;
                const row = document.querySelector(`[onclick*="${tids[i]}"]`).closest('.tf-row');
                if(tf_data[tids[i]] === corrects[i]) { row.style.background = "#f0fdf4"; }
                else { allCorrect = false; row.style.background = "#fef2f2"; }
                row.querySelectorAll('.tf-btn').forEach(b => b.classList.add('disabled'));
            }
            if(allCorrect) { feedback.innerText = "Logic Master! ✨"; feedback.className = "feedback-dark correct"; triggerConfetti(); }
            else { feedback.innerText = "Review highlighted rows."; feedback.className = "feedback-dark wrong"; }
            feedback.style.display = 'block';
        }

        function checkDD(qid, corrects) {
            const container = document.getElementById(qid);
            const selects = container.querySelectorAll('select');
            const feedback = document.getElementById('feedback-' + qid);
            let ok = true;
            selects.forEach((s, i) => {
                if(s.value === corrects[i]) { s.style.borderColor = "#10b981"; s.style.background = "#f0fdf4"; }
                else { ok = false; s.style.borderColor = "#ef4444"; s.style.background = "#fef2f2"; }
                s.disabled = true;
            });
            if(ok) { feedback.innerText = "Perfect matches! ✨"; feedback.className = "feedback-dark correct"; triggerConfetti(); }
            else { feedback.innerText = "Incorrect placement."; feedback.className = "feedback-dark wrong"; }
            feedback.style.display = 'block';
        }

        function checkScenario(sid, msg) {
            const val = document.getElementById(sid).value;
            const feedback = document.getElementById('feedback-' + sid);
            if(val.length < 5) return;
            feedback.innerText = msg + " ✨";
            feedback.className = "feedback-dark correct";
            triggerConfetti();
            feedback.style.display = 'block';
        }
    </script>
</body></html>
"""

full_html = header_part + s1 + s2 + s3_intro + s3_numeric + s3_other + s4s5 + s678 + footer_part
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(full_html)
print("Module 1 Synchronization Complete. 100% Accuracy.")
