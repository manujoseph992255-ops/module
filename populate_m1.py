import os

filepath = r"C:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"

# Define the HTML Parts
header_part = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Module 1: Data Basics | KVJ Analytics</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Outfit:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/skulpt@1.2.0/dist/skulpt.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/skulpt@1.2.0/dist/skulpt-stdlib.js"></script>
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

        /* Top Nav */
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
            background: #dc2626; color: white; padding: 8px 18px;
            text-decoration: none; font-size: 12px; font-weight: 700;
            border-radius: 6px; transition: opacity 0.3s; text-transform: uppercase;
        }

        /* Header Banner */
        .header-banner {
            background: var(--primary-blue); color: white;
            padding: 120px 20px 60px; text-align: center;
        }

        .header-banner h1 {
            font-family: 'Montserrat', sans-serif; font-size: 38px;
            font-weight: 900; letter-spacing: -1px; text-transform: uppercase;
        }

        /* Layout Container */
        .layout-container {
            display: flex; max-width: 1300px;
            margin: 40px auto; gap: 40px; width: 95%; padding-bottom: 60px;
        }

        /* Sidebar Navigation */
        .sidebar {
            width: 300px; background: white; padding: 30px;
            border: 1px solid var(--border-color); position: sticky;
            top: 100px; border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03); height: fit-content;
        }

        .sidebar h3 {
            font-family: 'Montserrat', sans-serif; font-size: 13px;
            color: var(--secondary-blue); text-transform: uppercase;
            margin-bottom: 20px; border-bottom: 2px solid var(--bg-light);
            padding-bottom: 10px; font-weight: 800; letter-spacing: 1px;
        }

        .sidebar a {
            display: flex; align-items: center; padding: 12px 15px;
            color: #555; text-decoration: none; font-size: 14px;
            font-weight: 500; margin-bottom: 5px; border-radius: 8px;
            transition: all 0.2s;
        }

        .sidebar a.active {
            color: var(--primary-blue); font-weight: 700;
            background: #f0f7ff; border-left: 4px solid var(--primary-blue);
        }

        .sidebar a:hover:not(.active) { background: #f8fafc; color: var(--primary-blue); }

        /* Main Content Area */
        .main-content {
            flex: 1; background: #ffffff; border: 1px solid var(--border-color);
            padding: 60px; border-radius: 12px; box-shadow: 0 4px 25px rgba(0, 0, 0, 0.04);
        }

        .section-header {
            margin-bottom: 30px; border-bottom: 3px solid var(--bg-light);
            padding-bottom: 15px;
        }

        .section-header h2 {
            font-family: 'Montserrat', sans-serif; color: var(--primary-blue);
            font-size: 28px; font-weight: 800; text-transform: uppercase;
            letter-spacing: -0.5px;
        }

        /* Content Styles */
        p { line-height: 1.8; margin-bottom: 25px; color: #334155; font-size: 17px; }
        strong { color: var(--primary-blue); font-weight: 700; }
        h3 {
            font-family: 'Montserrat', sans-serif; color: var(--primary-blue);
            margin: 40px 0 20px; font-size: 22px; font-weight: 700;
        }

        .content-list { list-style: none; margin-bottom: 25px; }
        .content-list li {
            position: relative; padding-left: 25px; margin-bottom: 12px;
            color: #334155; font-size: 17px;
        }
        .content-list li::before {
            content: "•"; color: var(--secondary-blue); font-weight: 900;
            font-size: 24px; position: absolute; left: 0; top: -4px;
        }

        .interaction-box {
            background-color: #f7f9fc; border-left: 5px solid var(--secondary-blue);
            padding: 25px; margin: 30px 0; border-radius: 0 10px 10px 0; font-size: 15px;
        }

        /* Practice Space Styling */
        .practice-card {
            background: #ffffff; border: 1px solid var(--border-color);
            border-left: 5px solid var(--secondary-blue); border-radius: 12px;
            padding: 40px; margin: 40px 0; color: var(--text-main);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05); position: relative; overflow: hidden;
        }
        .practice-badge {
            position: absolute; top: 0; right: 0; background: var(--secondary-blue);
            color: white; padding: 6px 15px; font-size: 10px; font-weight: 800;
            text-transform: uppercase; border-radius: 0 0 0 12px; letter-spacing: 1px;
        }
        .practice-card h4 { margin-bottom: 15px; font-size: 18px; color: var(--primary-blue); }

        .mcq-options { display: grid; gap: 12px; margin: 20px 0; }
        .mcq-option {
            background: #f8fafc; border: 2px solid var(--border-color);
            padding: 15px 20px; border-radius: 10px; cursor: pointer;
            transition: all 0.2s; display: flex; align-items: center; gap: 15px;
        }
        .mcq-option:hover:not(.disabled) { border-color: var(--secondary-blue); background: #f0f9ff; }
        .mcq-option.selected { border-color: var(--secondary-blue); background: #f0f9ff; }
        .mcq-option.correct { border-color: #10b981; background: #ecfdf5; color: #065f46; }
        .mcq-option.wrong { border-color: #ef4444; background: #fef2f2; color: #991b1b; }
        .mcq-option.disabled { pointer-events: none; }
        .mcq-prefix { font-weight: 800; color: var(--secondary-blue); }

        .tf-row {
            display: flex; align-items: center; justify-content: space-between;
            padding: 15px 0; border-bottom: 1px solid #eee;
        }
        .tf-row:last-child { border-bottom: none; }
        .tf-statement { font-size: 16px; font-weight: 500; flex: 1; padding-right: 20px; }
        .tf-btn-group { display: flex; gap: 10px; }
        .tf-btn {
            padding: 8px 18px; border-radius: 6px; border: 1px solid var(--border-color);
            background: #f8fafc; cursor: pointer; font-weight: 600; transition: 0.2s;
        }
        .tf-btn:hover:not(.disabled) { border-color: var(--secondary-blue); background: #f0f9ff; }
        .tf-btn.selected-true { background: #dcfce7; border-color: #22c55e; color: #166534; }
        .tf-btn.selected-false { background: #fee2e2; border-color: #ef4444; color: #991b1b; }
        .tf-btn.disabled { pointer-events: none; opacity: 0.7; }

        .scenario-box { margin-top: 20px; }
        .practice-dark-box {
            display: flex; gap: 10px; background: #1e293b; padding: 10px;
            border-radius: 10px; align-items: center;
        }
        .practice-dark-box input {
            flex: 1; background: transparent; border: none; color: white;
            padding: 10px; outline: none; font-family: inherit;
        }
        .practice-dark-btn {
            background: var(--secondary-blue); color: white; border: none;
            padding: 10px 25px; border-radius: 6px; cursor: pointer; font-weight: 700;
        }
        .feedback-dark {
            margin-top: 15px; padding: 15px; border-radius: 8px; font-weight: 700;
            display: none; font-size: 14px;
        }
        .feedback-dark.correct { background: #dcfce7; color: #166534; border: 1px solid #22c55e; }
        .feedback-dark.wrong { background: #fee2e2; color: #991b1b; border: 1px solid #ef4444; }

        .dd-container { background: #1e293b; padding: 30px; border-radius: 12px; margin: 20px 0; }
        .dd-row { display: flex; align-items: center; gap: 20px; margin-bottom: 15px; }
        .dd-label { flex: 1; color: white; font-weight: 600; font-size: 15px; }
        .dd-target { flex: 1; }
        .dd-target select {
            width: 100%; padding: 10px; border-radius: 6px; background: #0f172a;
            color: #00d2ff; border: 1px solid #334155; outline: none; font-family: inherit;
        }

        .btn-try-again {
            background: #475569; color: white; border: none; padding: 10px 20px;
            border-radius: 6px; cursor: pointer; font-weight: 600; display: none; margin-top: 10px;
        }

        @media (max-width: 992px) {
            .layout-container { flex-direction: column; }
            .sidebar { width: 100%; position: static; }
            .main-content { padding: 30px; }
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <a href="data_index.html"><img src="Kvj logo.jpeg" alt="Logo" class="kvj-logo-img"></a>
        <a href="data_roadmap.html" class="logout-btn">EXIT</a>
    </nav>
    <header class="header-banner">
        <h1>MODULE 1: DATA BASICS</h1>
    </header>

    <div class="layout-container">
        <nav class="sidebar">
            <h3>Module Path</h3>
            <a href="Data-Module-1.html" class="active">01 Data Basics</a>
            <a href="Data-Module-2.html">02 Data Manipulation</a>
            <a href="#">03 Data Analysis</a>
            <a href="#">04 Visualization</a>
            <a href="#">05 Responsible Analytics</a>
            <h3 style="margin-top:25px;">Navigation</h3>
            <a href="data_roadmap.html" style="background: #f8f9fa;">&larr; Return to Roadmap</a>
        </nav>

        <main class="main-content">
"""

# CONTENT SECTIONS
s1_meaning_of_data = """
            <section class="lesson-section">
                <div class="section-header">
                    <h2>1. Meaning of Data</h2>
                </div>
                <h3>Concept</h3>
                <p><strong>Data</strong> refers to raw facts, figures, or observations collected for analysis or reference.</p>
                <p>Data can appear in many forms such as:</p>
                <ul class="content-list">
                    <li>Numbers</li>
                    <li>Text</li>
                    <li>Images</li>
                    <li>Audio</li>
                </ul>
                <p>By itself, data does not carry meaning until it is processed and interpreted.</p>
                
                <div class="interaction-box">
                    <strong>Example Raw Data:</strong>
                    <table style="width: 100%; border-collapse: collapse; margin-top: 10px; background: white;">
                        <tr style="background: var(--bg-light);">
                            <th style="padding: 10px; border: 1px solid var(--border-color);">Product</th>
                            <th style="padding: 10px; border: 1px solid var(--border-color);">Sales</th>
                        </tr>
                        <tr><td style="padding: 10px; border: 1px solid var(--border-color);">Laptop</td><td style="padding: 10px; border: 1px solid var(--border-color);">15</td></tr>
                        <tr><td style="padding: 10px; border: 1px solid var(--border-color);">Tablet</td><td style="padding: 10px; border: 1px solid var(--border-color);">8</td></tr>
                        <tr><td style="padding: 10px; border: 1px solid var(--border-color);">Phone</td><td style="padding: 10px; border: 1px solid var(--border-color);">20</td></tr>
                    </table>
                    <p style="margin-top: 15px;">After analysis we might discover: <strong>Phone is the best-selling product.</strong> That insight becomes useful information.</p>
                </div>

                <div class="interaction-box" style="border-left-color: #10b981; background: #f0fdf4;">
                    <strong>Insight:</strong>
                    <p>Data is like ingredients in cooking. Ingredients alone do not create a meal. Only after processing and combining them do we get something meaningful.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Multiple Choice Question</h4>
                    <p>Which of the following best describes data?</p>
                    <div class="mcq-options" id="mcq-1">
                        <div class="mcq-option" onclick="selectMCQ('mcq-1', 'A')"><span class="mcq-prefix">A.</span> Final decision</div>
                        <div class="mcq-option" onclick="selectMCQ('mcq-1', 'B')"><span class="mcq-prefix">B.</span> Raw facts collected for analysis</div>
                        <div class="mcq-option" onclick="selectMCQ('mcq-1', 'C')"><span class="mcq-prefix">C.</span> A business strategy</div>
                        <div class="mcq-option" onclick="selectMCQ('mcq-1', 'D')"><span class="mcq-prefix">D.</span> A summarized report</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-1', 'B', 'Correct! Data is raw facts collected for analysis.')">Submit</button>
                    <button class="btn-try-again" id="reset-mcq-1" onclick="resetMCQ('mcq-1')">Try Again</button>
                    <div class="feedback-dark" id="feedback-mcq-1"></div>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>True / False</h4>
                    <div class="tf-row">
                        <span class="tf-statement">Data always has meaning by itself.</span>
                        <div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_single('tf-1', true)">True</button><button class="tf-btn" onclick="selectTF_single('tf-1', false)">False</button></div>
                    </div>
                    <div class="tf-row">
                        <span class="tf-statement">Data can include text and images.</span>
                        <div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_single('tf-2', true)">True</button><button class="tf-btn" onclick="selectTF_single('tf-2', false)">False</button></div>
                    </div>
                    <div class="tf-row">
                        <span class="tf-statement">Data becomes useful after analysis.</span>
                        <div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_single('tf-3', true)">True</button><button class="tf-btn" onclick="selectTF_single('tf-3', false)">False</button></div>
                    </div>
                    <div style="margin-top: 20px;">
                        <button class="practice-dark-btn" onclick="checkTF_group(['tf-1', 'tf-2', 'tf-3'], [false, true, true])">Check Answers</button>
                        <button class="btn-try-again" id="reset-tf-group-1" onclick="resetTF_group(['tf-1', 'tf-2', 'tf-3'])">Try Again</button>
                    </div>
                    <div class="feedback-dark" id="feedback-tf-group-1"></div>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Scenario Question</h4>
                    <p>A school collects: Student marks, Attendance, Assignment scores. Explain one insight the school could get after analyzing this data.</p>
                    <div class="scenario-box">
                        <div class="practice-dark-box">
                            <input type="text" id="scenario-1" placeholder="Type your explanation here...">
                            <button class="practice-dark-btn" onclick="checkScenario('scenario-1', 'Great! Insights could include identifying struggling students, average attendance trends, or the impact of assignments on marks.')">Submit</button>
                        </div>
                        <div class="feedback-dark" id="feedback-scenario-1"></div>
                    </div>
                </div>
            </section>
"""

s2_data_analysis = """
            <section class="lesson-section">
                <div class="section-header">
                    <h2>2. Data Analysis</h2>
                </div>
                <h3>Concept</h3>
                <p><strong>Data Analysis</strong> is the process of converting raw data into useful information for decision making.</p>
                <p>Organizations use data analysis to:</p>
                <ul class="content-list">
                    <li>Understand trends</li>
                    <li>Identify patterns</li>
                    <li>Support decisions</li>
                </ul>
                <div class="interaction-box">
                    <strong>Example:</strong>
                    <p>A company records daily sales.</p>
                    <table style="width: 100%; border-collapse: collapse; margin-top: 10px; background: white;">
                        <tr style="background: var(--bg-light);">
                            <th style="padding: 10px; border: 1px solid var(--border-color);">Day</th>
                            <th style="padding: 10px; border: 1px solid var(--border-color);">Sales</th>
                        </tr>
                        <tr><td style="padding: 10px; border: 1px solid var(--border-color);">Monday</td><td style="padding: 10px; border: 1px solid var(--border-color);">5000</td></tr>
                        <tr><td style="padding: 10px; border: 1px solid var(--border-color);">Tuesday</td><td style="padding: 10px; border: 1px solid var(--border-color);">6200</td></tr>
                        <tr><td style="padding: 10px; border: 1px solid var(--border-color);">Wednesday</td><td style="padding: 10px; border: 1px solid var(--border-color);">7100</td></tr>
                    </table>
                    <p style="margin-top: 15px;">After analysis they may conclude: <strong>Sales increase mid-week.</strong></p>
                </div>
                <div class="interaction-box" style="border-left-color: #008eab; background: #ecfeff;">
                    <strong>Insight:</strong>
                    <p>Data analysis answers questions like: What happened? Why did it happen? What might happen next?</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Drag & Drop: Match the Purpose</h4>
                    <p>Match the data collected with the possible insight.</p>
                    <div class="dd-container" id="dd-1">
                        <div class="dd-row">
                            <div class="dd-label">Website visitors</div>
                            <div class="dd-target">
                                <select id="dd-1-opt1">
                                    <option value="">Select Insight...</option>
                                    <option value="A">Most popular page</option>
                                    <option value="B">Class average</option>
                                    <option value="C">Best selling product</option>
                                </select>
                            </div>
                        </div>
                        <div class="dd-row">
                            <div class="dd-label">Student marks</div>
                            <div class="dd-target">
                                <select id="dd-1-opt2">
                                    <option value="">Select Insight...</option>
                                    <option value="A">Most popular page</option>
                                    <option value="B">Class average</option>
                                    <option value="C">Best selling product</option>
                                </select>
                            </div>
                        </div>
                        <div class="dd-row">
                            <div class="dd-label">Sales records</div>
                            <div class="dd-target">
                                <select id="dd-1-opt3">
                                    <option value="">Select Insight...</option>
                                    <option value="A">Most popular page</option>
                                    <option value="B">Class average</option>
                                    <option value="C">Best selling product</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkDD('dd-1', ['A', 'B', 'C'])">Check Matches</button>
                    <button class="btn-try-again" id="reset-dd-1" onclick="resetDD('dd-1')">Try Again</button>
                    <div class="feedback-dark" id="feedback-dd-1"></div>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Multiple Choice Question</h4>
                    <p>A dataset is:</p>
                    <div class="mcq-options" id="mcq-2">
                        <div class="mcq-option" onclick="selectMCQ('mcq-2', 'A')"><span class="mcq-prefix">A.</span> A collection of organized data</div>
                        <div class="mcq-option" onclick="selectMCQ('mcq-2', 'B')"><span class="mcq-prefix">B.</span> A type of graph</div>
                        <div class="mcq-option" onclick="selectMCQ('mcq-2', 'C')"><span class="mcq-prefix">C.</span> A statistical formula</div>
                        <div class="mcq-option" onclick="selectMCQ('mcq-2', 'D')"><span class="mcq-prefix">D.</span> A programming language</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-2', 'A', 'Correct! A dataset is a collection of organized data.')">Submit</button>
                    <button class="btn-try-again" id="reset-mcq-2" onclick="resetMCQ('mcq-2')">Try Again</button>
                    <div class="feedback-dark" id="feedback-mcq-2"></div>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Mini Thinking Question</h4>
                    <p>A restaurant collects daily customer feedback ratings. What decision could the restaurant make after analyzing this data?</p>
                    <div class="scenario-box">
                        <div class="practice-dark-box">
                            <input type="text" id="scenario-2" placeholder="Type your thought here...">
                            <button class="practice-dark-btn" onclick="checkScenario('scenario-2', 'Excellent! They could identify low-rated dishes to improve recipes, adjust staff shifts during busy times, or enhance service quality based on common complaints.')">Submit</button>
                        </div>
                        <div class="feedback-dark" id="feedback-scenario-2"></div>
                    </div>
                </div>
            </section>
"""

s3_variable_types = """
            <section class="lesson-section">
                <div class="section-header">
                    <h2>3. Data Variable Types</h2>
                </div>
                <h3>Concept</h3>
                <p>Variables describe the type of value stored in data. Main variable types include:</p>
                <ul class="content-list">
                    <li>Boolean</li>
                    <li>Numeric</li>
                    <li>String</li>
                </ul>
                <p>Each type stores different kinds of values.</p>
                <div class="interaction-box" style="border-left-color: #6366f1; background: #eef2ff;">
                    <strong>Insight:</strong>
                    <p>Understanding variable types helps store data correctly, analyze data efficiently, and avoid calculation errors.</p>
                </div>

                <h3>3.1 Boolean Data Type</h3>
                <p>Boolean data type stores two possible values: <strong>True</strong> or <strong>False</strong>.</p>
                <p>Booleans are commonly used in logical conditions and decision making.</p>
                <pre><code>is_logged_in = True
if is_logged_in:
    print("Access granted")</code></pre>
                <div class="interaction-box">
                    <strong>Switch Analogy:</strong>
                    <p>Boolean variables act like switches: ON = True, OFF = False.</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Identify Boolean</h4>
                    <p>Which of the following can be Boolean? (Select all correct)</p>
                    <div class="mcq-options" id="mcq-3">
                        <div class="mcq-option" onclick="toggleMulti('mcq-3', 'A')"><span class="mcq-prefix">1.</span> Student passed exam</div>
                        <div class="mcq-option" onclick="toggleMulti('mcq-3', 'B')"><span class="mcq-prefix">2.</span> Number of books</div>
                        <div class="mcq-option" onclick="toggleMulti('mcq-3', 'C')"><span class="mcq-prefix">3.</span> Payment successful</div>
                        <div class="mcq-option" onclick="toggleMulti('mcq-3', 'D')"><span class="mcq-prefix">4.</span> Temperature</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMulti('mcq-3', ['A', 'C'], 'Correct! 1 and 3 are Boolean (Yes/No).')">Submit</button>
                    <button class="btn-try-again" id="reset-mcq-3" onclick="resetMulti('mcq-3')">Try Again</button>
                    <div class="feedback-dark" id="feedback-mcq-3"></div>
                </div>

                <h3>3.2 Numeric Data Type</h3>
                <p>Numeric data types represent numbers that can be calculated mathematically.</p>
                <p>Examples: exam marks, salary, weight, height.</p>
                <div class="interaction-box">
                    <strong>Features:</strong>
                    <p>Numeric data allows operations such as addition, subtraction, multiplication, and division.</p>
                </div>
                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Multiple Choice Question</h4>
                    <p>Which of the following is numeric data?</p>
                    <div class="mcq-options" id="mcq-4">
                        <div class="mcq-option" onclick="selectMCQ('mcq-4', 'A')"><span class="mcq-prefix">A.</span> Age</div>
                        <div class="mcq-option" onclick="selectMCQ('mcq-4', 'B')"><span class="mcq-prefix">B.</span> Country name</div>
                        <div class="mcq-option" onclick="selectMCQ('mcq-4', 'C')"><span class="mcq-prefix">C.</span> Product category</div>
                        <div class="mcq-option" onclick="selectMCQ('mcq-4', 'D')"><span class="mcq-prefix">D.</span> Email address</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-4', 'A', 'Correct! Age is represented by numbers.')">Submit</button>
                    <button class="btn-try-again" id="reset-mcq-4" onclick="resetMCQ('mcq-4')">Try Again</button>
                    <div class="feedback-dark" id="feedback-mcq-4"></div>
                </div>

                <h3>3.3 Integer</h3>
                <p>An integer is a whole number without decimal values.</p>
                <p>Examples: 5, 10, -3, 0.</p>
                <div class="interaction-box">
                    <strong>Use Case:</strong>
                    <p>Integers are useful when exact counts are needed (e.g., number of students, products sold).</p>
                </div>

                <h3>3.4 Float</h3>
                <p>A float represents numbers with decimal values.</p>
                <p>Examples: 2.5, 3.14, 7.8.</p>
                <div class="interaction-box">
                    <strong>Precision:</strong>
                    <p>Floats allow more accurate measurements compared to integers (e.g., price, temperature, weight).</p>
                </div>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Drag & Drop: Classification</h4>
                    <div class="dd-container" id="dd-2">
                        <div class="dd-row">
                            <div class="dd-label">25</div>
                            <div class="dd-target">
                                <select id="dd-2-opt1">
                                    <option value="">Select Type...</option>
                                    <option value="INT">Integer</option>
                                    <option value="FLT">Float</option>
                                </select>
                            </div>
                        </div>
                        <div class="dd-row">
                            <div class="dd-label">12.75</div>
                            <div class="dd-target">
                                <select id="dd-2-opt2">
                                    <option value="">Select Type...</option>
                                    <option value="INT">Integer</option>
                                    <option value="FLT">Float</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkDD('dd-2', ['INT', 'FLT'])">Check Types</button>
                    <button class="btn-try-again" id="reset-dd-2" onclick="resetDD('dd-2')">Try Again</button>
                    <div class="feedback-dark" id="feedback-dd-2"></div>
                </div>

                <h3>3.5 Complex Numbers</h3>
                <p>Complex numbers contain a real part and an imaginary part (a + bi).</p>
                <p>Example: 3 + 4i.</p>
                <div class="interaction-box">
                    <strong>Science:</strong>
                    <p>Complex numbers are mainly used in engineering and scientific calculations.</p>
                </div>

                <h3>3.6 String Data Type</h3>
                <p>String data type stores text values.</p>
                <p>Examples: "India", "Laptop", "Anoop". Strings can contain letters, numbers, and symbols.</p>
                <p>Strings help store descriptive information, not numeric calculations.</p>
            </section>
"""

s4_to_s8 = """
            <section class="lesson-section">
                <div class="section-header">
                    <h2>4. Data Structures</h2>
                </div>
                <p>Data is often organized using structures such as Tables, Rows, Columns, and Lists.</p>
                <div class="interaction-box">
                    <strong>Definitions:</strong>
                    <ul class="content-list">
                        <li><strong>Table:</strong> Organized dataset</li>
                        <li><strong>Row:</strong> Single record</li>
                        <li><strong>Column:</strong> Attribute</li>
                    </ul>
                </div>
                <pre><code># Example List
[1, 2, 3, 4, 5]</code></pre>

                <div class="section-header">
                    <h2>5. Types of Data</h2>
                </div>
                <p>Data can be classified into two main types: Qualitative and Quantitative.</p>
                <h3>5.1 Qualitative Data</h3>
                <p>Describes categories or characteristics (e.g., gender, city, eye color).</p>
                <h3>5.2 Quantitative Data</h3>
                <p>Represents numeric values that can be counted or measured (e.g., height, weight, salary).</p>

                <div class="section-header">
                    <h2>6. Structured vs Unstructured Data</h2>
                </div>
                <p><strong>Structured Data:</strong> Fits into rows and columns (e.g., Excel tables, Database records).</p>
                <p><strong>Unstructured Data:</strong> Has no fixed format (e.g., emails, videos, social media posts).</p>

                <div class="section-header">
                    <h2>7. Metadata</h2>
                </div>
                <p><strong>Metadata</strong> means "data about data". It describes information like file size, creation date, author, or resolution.</p>

                <div class="section-header">
                    <h2>8. Big Data</h2>
                </div>
                <p><strong>Big Data</strong> refers to extremely large and complex datasets that grow rapidly and cannot be processed using traditional systems.</p>
                
                <div class="quiz-cta">
                    <h3>Ready for the Knowledge Check?</h3>
                    <p>Test your understanding of the foundational data concepts we've covered.</p>
                    <a href="module_quiz.html?mod=d1" class="btn-start-quiz">Start Assessment</a>
                </div>
            </section>
"""

footer_part = """
        </main>
    </div>

    <footer>
        &copy; 2026 KVJ Analytics. All rights reserved.
    </footer>

    <script>
        function triggerConfetti() {
            confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
        }

        // MCQ Selection
        function selectMCQ(qid, opt) {
            const container = document.getElementById(qid);
            const options = container.querySelectorAll('.mcq-option');
            options.forEach(o => o.classList.remove('selected'));
            const self = Array.from(options).find(o => o.innerText.includes(opt + '.'));
            if(self) self.classList.add('selected');
        }

        function checkMCQ(qid, correctOpt, msg) {
            const container = document.getElementById(qid);
            const options = container.querySelectorAll('.mcq-option');
            const selected = container.querySelector('.mcq-option.selected');
            const feedback = document.getElementById('feedback-' + qid);
            const resetBtn = document.getElementById('reset-' + qid);

            if(!selected) {
                feedback.innerText = "Please select an answer.";
                feedback.className = "feedback-dark wrong";
                feedback.style.display = "block";
                return;
            }

            options.forEach(o => o.classList.add('disabled'));
            if(selected.innerText.includes(correctOpt + '.')) {
                selected.classList.add('correct');
                feedback.innerText = msg + " 🎉";
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            } else {
                selected.classList.add('wrong');
                feedback.innerText = "Incorrect. Try again!";
                feedback.className = "feedback-dark wrong";
                if(resetBtn) resetBtn.style.display = "inline-block";
            }
            feedback.style.display = "block";
        }

        function resetMCQ(qid) {
            const container = document.getElementById(qid);
            const options = container.querySelectorAll('.mcq-option');
            options.forEach(o => {
                o.classList.remove('selected', 'correct', 'wrong', 'disabled');
            });
            document.getElementById('feedback-' + qid).style.display = "none";
            document.getElementById('reset-' + qid).style.display = "none";
        }

        // Multiple Selection
        function toggleMulti(qid, opt) {
            const container = document.getElementById(qid);
            const options = Array.from(container.querySelectorAll('.mcq-option'));
            const self = options.find(o => o.innerText.includes(opt + '.'));
            if(self) self.classList.toggle('selected');
        }

        function checkMulti(qid, corrects, msg) {
            const container = document.getElementById(qid);
            const options = Array.from(container.querySelectorAll('.mcq-option'));
            const selecteds = options.filter(o => o.classList.contains('selected'));
            const feedback = document.getElementById('feedback-' + qid);
            const resetBtn = document.getElementById('reset-' + qid);

            if(selecteds.length === 0) {
                feedback.innerText = "Please select at least one.";
                feedback.className = "feedback-dark wrong";
                feedback.style.display = "block";
                return;
            }

            options.forEach(o => o.classList.add('disabled'));
            const selectedLabels = selecteds.map(o => o.innerText[0]); // A, B, C, D
            const isCorrect = corrects.every(c => selectedLabels.includes(c)) && selectedLabels.length === corrects.length;

            if(isCorrect) {
                selecteds.forEach(o => o.classList.add('correct'));
                feedback.innerText = msg + " 🎉";
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            } else {
                selecteds.forEach(o => o.classList.add('wrong'));
                feedback.innerText = "One or more selections are wrong. Try again!";
                feedback.className = "feedback-dark wrong";
                if(resetBtn) resetBtn.style.display = "inline-block";
            }
            feedback.style.display = "block";
        }

        function resetMulti(qid) { resetMCQ(qid); }

        // True/False
        let tfSelections = {};
        function selectTF_single(qid, val) {
            const row = event.target.closest('.tf-row');
            const btns = row.querySelectorAll('.tf-btn');
            btns.forEach(b => b.classList.remove('selected-true', 'selected-false'));
            event.target.classList.add(val ? 'selected-true' : 'selected-false');
            tfSelections[qid] = val;
        }

        function checkTF_group(qids, corrects) {
            let allCorrect = true;
            let feedbackText = "";
            const feedback = document.getElementById('feedback-tf-group-1');
            const resetBtn = document.getElementById('reset-tf-group-1');

            qids.forEach((id, idx) => {
                if(tfSelections[id] === undefined) { allCorrect = false; feedbackText = "Answer all first!"; }
            });

            if(feedbackText) {
                feedback.innerText = feedbackText;
                feedback.className = "feedback-dark wrong";
                feedback.style.display = "block";
                return;
            }

            qids.forEach((id, idx) => {
                const btn = document.querySelector(`[onclick*="'${id}'"].selected-${tfSelections[id]}`);
                if(tfSelections[id] === corrects[idx]) {
                    btn.closest('.tf-row').style.background = "#f0fdf4";
                } else {
                    allCorrect = false;
                    btn.closest('.tf-row').style.background = "#fef2f2";
                }
                const btns = btn.closest('.tf-btn-group').querySelectorAll('.tf-btn');
                btns.forEach(b => b.classList.add('disabled'));
            });

            if(allCorrect) {
                feedback.innerText = "All correct! 🎉";
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            } else {
                feedback.innerText = "Some answers are wrong. Check the highlights.";
                feedback.className = "feedback-dark wrong";
                resetBtn.style.display = "inline-block";
            }
            feedback.style.display = "block";
        }

        function resetTF_group(qids) {
            qids.forEach(id => {
                delete tfSelections[id];
                const btns = document.querySelectorAll(`[onclick*="'${id}'"]`);
                btns.forEach(b => {
                    b.classList.remove('selected-true', 'selected-false', 'disabled');
                    b.closest('.tf-row').style.background = "transparent";
                });
            });
            document.getElementById('feedback-tf-group-1').style.display = "none";
            document.getElementById('reset-tf-group-1').style.display = "none";
        }

        // Drag & Drop
        function checkDD(id, corrects) {
            const container = document.getElementById(id);
            const selects = container.querySelectorAll('select');
            const feedback = document.getElementById('feedback-' + id);
            const resetBtn = document.getElementById('reset-' + id);
            
            let allCorrect = true;
            selects.forEach((s, idx) => {
                if(s.value === corrects[idx]) { s.style.borderColor = "#10b981"; s.style.background = "#ecfdf5"; }
                else { allCorrect = false; s.style.borderColor = "#ef4444"; s.style.background = "#fef2f2"; }
                s.disabled = true;
            });

            if(allCorrect) {
                feedback.innerText = "Perfect match! 🎉";
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            } else {
                feedback.innerText = "Incorrect matches. Try again!";
                feedback.className = "feedback-dark wrong";
                resetBtn.style.display = "inline-block";
            }
            feedback.style.display = "block";
        }

        function resetDD(id) {
            const container = document.getElementById(id);
            const selects = container.querySelectorAll('select');
            selects.forEach(s => {
                s.value = ""; s.disabled = false;
                s.style.borderColor = "#334155"; s.style.background = "#0f172a";
            });
            document.getElementById('feedback-' + id).style.display = "none";
            document.getElementById('reset-' + id).style.display = "none";
        }

        // Scenario
        function checkScenario(id, msg) {
            const input = document.getElementById(id);
            const feedback = document.getElementById('feedback-' + id);
            if(input.value.length < 10) {
                feedback.innerText = "Please provide a more detailed explanation.";
                feedback.className = "feedback-dark wrong";
            } else {
                feedback.innerText = msg;
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            }
            feedback.style.display = "block";
        }
    </script>
</body>
</html>
"""

full_html = header_part + s1_meaning_of_data + s2_data_analysis + s3_variable_types + s4_to_s8 + footer_part

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Successfully populated Data-Module-1.html with all content.")
