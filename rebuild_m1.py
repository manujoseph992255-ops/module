import json
import re

html_content = """
            <div class="section-header">
                <h2>1. Meaning of Data</h2>
            </div>
            <h3>Concept</h3>
            <p>Data refers to raw facts, figures, or observations collected for analysis or reference.</p>
            <p>Data can appear in many forms such as:</p>
            <ul class="content-list">
                <li>Numbers</li>
                <li>Text</li>
                <li>Images</li>
                <li>Audio</li>
            </ul>
            <p>By itself, data does not carry meaning until it is processed and interpreted.</p>
            <div class="interaction-box">
                <strong>Example raw data:</strong>
                <table class="data-table">
                    <tr><th>Product</th><th>Sales</th></tr>
                    <tr><td>Laptop</td><td>15</td></tr>
                    <tr><td>Tablet</td><td>8</td></tr>
                    <tr><td>Phone</td><td>20</td></tr>
                </table>
                <p>After analysis we might discover: <strong>Phone is the best-selling product.</strong> That insight becomes useful information.</p>
            </div>
            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>Data is like ingredients in cooking. Ingredients alone do not create a meal. Only after processing and combining them do we get something meaningful.</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which of the following best describes data?</p>
                <div id="mcq-m1-1">
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-1')"><span class="mcq-prefix">A.</span> Final decision</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-1')"><span class="mcq-prefix">B.</span> Raw facts collected for analysis</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-1')"><span class="mcq-prefix">C.</span> A business strategy</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-1')"><span class="mcq-prefix">D.</span> A summarized report</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ('mcq-m1-1', 'B', 'Correct! Data consists of raw facts.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m1-1"></div>

                <div style="margin-top:30px;">
                    <p><strong>True / False</strong></p>
                    <div class="tf-row" id="tf-row-m1-1a"><span class="tf-statement">Data always has meaning by itself.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'm1-1a', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'm1-1a', false)">False</button></div></div>
                    <div class="tf-row" id="tf-row-m1-1b"><span class="tf-statement">Data can include text and images.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'm1-1b', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'm1-1b', false)">False</button></div></div>
                    <div class="tf-row" id="tf-row-m1-1c"><span class="tf-statement">Data becomes useful after analysis.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'm1-1c', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'm1-1c', false)">False</button></div></div>
                    <button class="practice-dark-btn" onclick="checkTFGroup(['m1-1a', 'm1-1b', 'm1-1c'], [false, true, true], 'feedback-tf-1')">Check Answers</button>
                    <div class="feedback-dark" id="feedback-tf-1"></div>
                </div>

                <div style="margin-top:30px;">
                    <p><strong>Scenario Question</strong></p>
                    <p>A school collects: Student marks, Attendance, Assignment scores. Explain one insight the school could get after analyzing this data.</p>
                    <textarea style="width:100%; padding:10px; margin-top:10px; border:1px solid #e2e8f0; border-radius:5px;" rows="3" placeholder="Type your answer here..."></textarea>
                </div>
            </div>

            <div class="section-header" style="margin-top: 60px;">
                <h2>2. Data Analysis</h2>
            </div>
            <h3>Concept</h3>
            <p>Data Analysis is the process of converting raw data into useful information for decision making. Organizations use data analysis to:</p>
            <ul class="content-list">
                <li>Understand trends</li>
                <li>Identify patterns</li>
                <li>Support decisions</li>
            </ul>
            <div class="interaction-box">
                <strong>Example:</strong>
                <p>A company records daily sales.</p>
                <table class="data-table">
                    <tr><th>Day</th><th>Sales</th></tr>
                    <tr><td>Monday</td><td>5000</td></tr>
                    <tr><td>Tuesday</td><td>6200</td></tr>
                    <tr><td>Wednesday</td><td>7100</td></tr>
                </table>
                <p>After analysis they may conclude: <strong>Sales increase mid-week.</strong></p>
            </div>
            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>Data analysis answers questions like: What happened? Why did it happen? What might happen next?</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>A dataset is:</p>
                <div id="mcq-m1-2">
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-2')"><span class="mcq-prefix">A.</span> A collection of organized data</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-2')"><span class="mcq-prefix">B.</span> A type of graph</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-2')"><span class="mcq-prefix">C.</span> A statistical formula</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-2')"><span class="mcq-prefix">D.</span> A programming language</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ('mcq-m1-2', 'A', 'Correct! A dataset is an organized collection.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m1-2"></div>
                
                <div style="margin-top:30px;">
                    <p><strong>Mini Thinking Question:</strong> A restaurant collects daily customer feedback ratings. What decision could the restaurant make after analyzing this data?</p>
                    <textarea style="width:100%; padding:10px; margin-top:10px; border:1px solid #e2e8f0; border-radius:5px;" rows="3" placeholder="Type your answer here..."></textarea>
                </div>
            </div>

            <div class="section-header" style="margin-top: 60px;">
                <h2>3. Data Variable Types</h2>
            </div>
            <h3>Concept</h3>
            <p>Variables describe the type of value stored in data. Main variable types include: Boolean, Numeric, String. Each type stores different kinds of values.</p>
            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong> Understanding variable types helps store data correctly, analyze data efficiently, and avoid calculation errors.
            </div>

            <h3 style="margin-top:40px;">3.1 Boolean Data Type</h3>
            <p>Boolean data type stores two possible values: <strong>True</strong> or <strong>False</strong>. Booleans are commonly used in logical conditions and decision making.</p>
            <div class="interaction-box">
                <strong>Example:</strong> <code>is_logged_in = True</code><br>
                Boolean values are used in conditions like:<br>
                <code>if is_logged_in:<br>    print("Access granted")</code>
            </div>
            
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p><strong>Identify Boolean:</strong> Which of the following can be Boolean? (Select all that apply)</p>
                <div class="tf-row" id="tf-row-bool-1"><span class="tf-statement">Student passed exam</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'bool-1', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'bool-1', false)">No</button></div></div>
                <div class="tf-row" id="tf-row-bool-2"><span class="tf-statement">Number of books</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'bool-2', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'bool-2', false)">No</button></div></div>
                <div class="tf-row" id="tf-row-bool-3"><span class="tf-statement">Payment successful</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'bool-3', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'bool-3', false)">No</button></div></div>
                <div class="tf-row" id="tf-row-bool-4"><span class="tf-statement">Temperature</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'bool-4', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'bool-4', false)">No</button></div></div>
                <button class="practice-dark-btn" onclick="checkTFGroup(['bool-1', 'bool-2', 'bool-3', 'bool-4'], [true, false, true, false], 'feedback-bool-id')">Check Answers</button>
                <div class="feedback-dark" id="feedback-bool-id"></div>
            </div>

            <h3 style="margin-top:40px;">3.2 Numeric Data Type</h3>
            <p>Numeric data types represent numbers that can be calculated mathematically. Examples: exam marks, salary, weight, height. Numeric types include Integer, Float, Complex.</p>
            
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which of the following is numeric data?</p>
                <div id="mcq-m1-3">
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-3')"><span class="mcq-prefix">A.</span> Age</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-3')"><span class="mcq-prefix">B.</span> Country name</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-3')"><span class="mcq-prefix">C.</span> Product category</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-3')"><span class="mcq-prefix">D.</span> Email address</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ('mcq-m1-3', 'A', 'Correct!')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m1-3"></div>
            </div>

            <h3 style="margin-top:40px;">3.3 Integer | 3.4 Float | 3.5 Complex | 3.6 String</h3>
            <p><strong>Integer:</strong> A whole number without decimals (e.g., 5, -3, 0). Used when counts are needed.</p>
            <p><strong>Float:</strong> Represents numbers with decimal values (e.g., 2.5, 3.14). Used for precision like price or weight.</p>
            <p><strong>Complex:</strong> Contains real and imaginary parts (e.g., 3 + 4i). Used in scientific calculations.</p>
            <p><strong>String:</strong> Stores text values (e.g., names, cities). Can contain letters, numbers, symbols.</p>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which value is a float?</p>
                <div id="mcq-m1-4">
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-4')"><span class="mcq-prefix">A.</span> 8</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-4')"><span class="mcq-prefix">B.</span> 12.5</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-4')"><span class="mcq-prefix">C.</span> -3</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-4')"><span class="mcq-prefix">D.</span> 20</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ('mcq-m1-4', 'B', 'Correct! 12.5 has a decimal point.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m1-4"></div>
            </div>

            <div class="section-header" style="margin-top: 60px;">
                <h2>4. Data Structures</h2>
            </div>
            <p>Data is often organized using structures such as Tables, Rows, Columns, and Lists.</p>
            <ul class="content-list">
                <li><strong>Table:</strong> Organize structured data.</li>
                <li><strong>Row:</strong> Single record in a dataset.</li>
                <li><strong>Column:</strong> Attribute or field.</li>
                <li><strong>List:</strong> Collection of items.</li>
            </ul>

            <div class="section-header" style="margin-top: 60px;">
                <h2>5. Types of Data</h2>
            </div>
            <p><strong>Qualitative Data:</strong> Describes categories or characteristics (e.g., gender, city, brand). Types include Nominal and Ordinal.</p>
            <p><strong>Quantitative Data:</strong> Represents numeric values allowing statistical calculations (e.g., height, weight, distance).</p>
            
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which of the following is qualitative data?</p>
                <div id="mcq-m1-5">
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-5')"><span class="mcq-prefix">A.</span> Salary</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-5')"><span class="mcq-prefix">B.</span> Height</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-5')"><span class="mcq-prefix">C.</span> Eye color</div>
                    <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-5')"><span class="mcq-prefix">D.</span> Age</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ('mcq-m1-5', 'C', 'Correct! It is a descriptive category.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m1-5"></div>
            </div>

            <div class="section-header" style="margin-top: 60px;">
                <h2>6. Structured vs Unstructured Data | 7. Metadata | 8. Big Data</h2>
            </div>
            <p><strong>Structured Data:</strong> Fits into rows and columns (e.g., bank records).</p>
            <p><strong>Unstructured Data:</strong> Has no fixed format (e.g., emails, videos, social media).</p>
            <p><strong>Metadata:</strong> Data about data. Describes file size, creation date, author.</p>
            <p><strong>Big Data:</strong> Extremely large and complex datasets from social media, sensors, IoT devices.</p>

            <div class="quiz-cta">
                <h3>Ready for the Knowledge Check?</h3>
                <p>Test your understanding of the core foundations of Data Analytics.</p>
                <a href="module_quiz.html?mod=data1" class="btn-start-quiz">Start Assessment &rarr;</a>
            </div>
"""

new_data1_questions = [
    {
        "id": 1,
        "type": "MCQ",
        "q": "1. What is Data?<br>Which statement best describes data?",
        "options": ["Processed information ready for decision making", "Raw facts and figures collected for analysis", "A business strategy", "A summarized report"],
        "a": 1
    },
    {
        "id": 2,
        "type": "TF",
        "q": "2. True or False<br>Data becomes meaningful only after processing and analysis.",
        "options": ["Data becomes meaningful only after processing and analysis."],
        "a": [True]
    },
    {
        "id": 3,
        "type": "MCQ",
        "q": "3. Which Data Type Stores Text?<br>Which data type can store a sentence or phrase?",
        "options": ["Integer", "Boolean", "String", "Float"],
        "a": 2
    },
    {
        "id": 4,
        "type": "MCQ",
        "q": "4. Identify the Data Type<br>Select the correct data type for the value below.<br><code>is_logged_in = True</code>",
        "options": ["Integer", "Boolean", "String", "Float"],
        "a": 1
    },
    {
        "id": 5,
        "type": "MTF",
        "q": "5. Drag and Drop<br>Match the data structure with the description.",
        "options": ["Table", "Row", "Column", "List"],
        "labels": ["Multiple rows and columns", "Single record in a dataset", "Attribute or field", "Collection of items"],
        "a": {
            "Table": "Multiple rows and columns",
            "Row": "Single record in a dataset",
            "Column": "Attribute or field",
            "List": "Collection of items"
        }
    },
    {
        "id": 6,
        "type": "MCQ",
        "q": "6. Which Data Structure Describes This Data?<br><code>[\"Aabid\", \"Jesenia\", \"Mark\"]</code>",
        "options": ["Table", "List", "Graph", "Matrix"],
        "a": 1
    },
    {
        "id": 7,
        "type": "MCQ",
        "q": "7. Multiple Choice<br>Which of the following is quantitative data?",
        "options": ["Eye color", "Age", "Country name", "Product category"],
        "a": 1
    },
    {
        "id": 8,
        "type": "TF",
        "q": "8. True or False<br>Qualitative data describes categories rather than numeric values.",
        "options": ["Qualitative data describes categories rather than numeric values."],
        "a": [True]
    },
    {
        "id": 9,
        "type": "MTF",
        "q": "9. Match the Data Type<br>Drag each example to the correct category.",
        "options": ["Gender", "Height", "Temperature", "Country"],
        "labels": ["Qualitative Data (A)", "Quantitative Data (A)", "Quantitative Data (B)", "Qualitative Data (B)"],
        "a": {
            "Gender": "Qualitative Data (A)",
            "Country": "Qualitative Data (B)",
            "Height": "Quantitative Data (A)",
            "Temperature": "Quantitative Data (B)"
        }
    },
    {
        "id": 10,
        "type": "MCQ",
        "q": "10. Structured vs Unstructured Data<br>Which of the following is structured data?",
        "options": ["Video file", "Email message", "Excel table", "Social media post"],
        "a": 2
    },
    {
        "id": 11,
        "type": "MCQ",
        "q": "11. What is Metadata?<br>Metadata refers to:",
        "options": ["Raw data collected from sensors", "Data about other data", "Unstructured data", "Numerical calculations"],
        "a": 1
    },
    {
        "id": 12,
        "type": "MCQ",
        "q": "12. Example of Metadata<br>Which of the following is an example of metadata?",
        "options": ["The image itself", "The creation date of a file", "The text inside a document", "The number of users on a website"],
        "a": 1
    },
    {
        "id": 13,
        "type": "MCQ",
        "q": "13. Big Data<br>Which statement best describes big data?",
        "options": ["Small datasets stored in spreadsheets", "Extremely large and complex datasets", "Only structured data", "Only text data"],
        "a": 1
    },
    {
        "id": 14,
        "type": "MTF",
        "q": "14. Drag and Drop – Statistical Metrics<br>Match the metric with the description.",
        "options": ["Sum", "Max", "Min", "Average"],
        "labels": ["Total of values", "Largest value", "Smallest value", "Mean of values"],
        "a": {
            "Sum": "Total of values",
            "Max": "Largest value",
            "Min": "Smallest value",
            "Average": "Mean of values"
        }
    },
    {
        "id": 15,
        "type": "MCQ",
        "q": "15. Data Classification<br>Person A has 5 coins and Person B has 10 coins. The number of coins represents:",
        "options": ["Qualitative data", "Quantitative data", "Metadata", "Ordinal data"],
        "a": 1
    },
    {
        "id": 16,
        "type": "MCQ",
        "q": "16. Data Insight Question<br>A company records: Customer age, Purchase amount, Product category. Which of these variables is qualitative data?",
        "options": ["Age", "Purchase amount", "Product category", "All of the above"],
        "a": 2
    }
]

print("Starting to update Data-Module-1.html...")

# Read the HTML Module file
with open('Data-Module-1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the inner content
updated_text = re.sub(r'(<main class="main-content">).*?(</main>)', rf'\1\n{html_content}\n\2', text, flags=re.DOTALL)

# Add necessary custom js scripts at the bottom for in-page interactivity
custom_js = """
<script>
    let selections = {};
    function selectMCQ(el, qid) {
        const parent = document.getElementById(qid);
        parent.querySelectorAll('.mcq-option').forEach(o => o.classList.remove('selected', 'correct', 'wrong'));
        el.classList.add('selected');
        selections[qid] = el.innerText[0]; // store A, B, C...
    }
    function checkMCQ(qid, correct, msg) {
        const parent = document.getElementById(qid);
        const feedback = document.getElementById('feedback-' + qid);
        const sel = parent.querySelector('.selected');
        if(!sel) return;
        if(selections[qid] === correct) {
            sel.classList.add('correct');
            feedback.innerText = msg;
            feedback.className = 'feedback-dark correct';
            if(typeof confetti !== 'undefined') confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
        } else {
            sel.classList.add('wrong');
            feedback.innerText = 'Try again!';
            feedback.className = 'feedback-dark wrong';
        }
    }
    function selectTF(el, qid, val) {
        const row = document.getElementById('tf-row-' + qid);
        row.querySelectorAll('.tf-btn').forEach(b => b.classList.remove('selected', 'correct', 'wrong'));
        el.classList.add('selected');
        selections[qid] = val;
    }
    function checkTFGroup(qids, corrects, fbid) {
        let allRight = true;
        qids.forEach((q, idx) => {
            const row = document.getElementById('tf-row-' + q);
            const sel = row.querySelector('.selected');
            if(!sel) allRight = false;
            else if (selections[q] !== corrects[idx]) allRight = false;
        });
        const feedback = document.getElementById(fbid);
        if(allRight) {
            feedback.innerText = "All correct!";
            feedback.className = 'feedback-dark correct';
            if(typeof confetti !== 'undefined') confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
        } else {
            feedback.innerText = "One or more are incorrect. Try again!";
            feedback.className = 'feedback-dark wrong';
        }
    }
</script>
</body>
"""

updated_text = updated_text.replace("</body>", custom_js)

with open('Data-Module-1.html', 'w', encoding='utf-8') as f:
    f.write(updated_text)

print("Updated Data-Module-1.html successfully.")

# Update quiz_data.js
print("Updating quiz_data.js for data1...")
with open('quiz_data.js', 'r', encoding='utf-8') as f:
    quiz_js = f.read()

# Replace the "data1": [...] block
new_json_str = '"data1": ' + json.dumps(new_data1_questions, indent=8)

patch = re.sub(r'"data1": \[.*?\],?\s*"data2"', new_json_str + ',\n    "data2"', quiz_js, flags=re.DOTALL)

with open('quiz_data.js', 'w', encoding='utf-8') as f:
    f.write(patch)

print("Update complete!")
