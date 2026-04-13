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
            <div class="interaction-box" style="border-left-color: var(--secondary-blue); background: #f5f3ff;">
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
                <strong>Example: a company records daily sales.</strong>
                <table class="data-table">
                    <tr><th>Day</th><th>Sales</th></tr>
                    <tr><td>Monday</td><td>5000</td></tr>
                    <tr><td>Tuesday</td><td>6200</td></tr>
                    <tr><td>Wednesday</td><td>7100</td></tr>
                </table>
                <p>After analysis they may conclude: <strong>Sales increase mid-week.</strong></p>
            </div>
            <div class="interaction-box" style="border-left-color: var(--secondary-blue); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>Data analysis answers questions like: What happened? Why did it happen? What might happen next?</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p><strong>Drag & Drop (Match the Purpose)</strong></p>
                <p>Match the data collected with the possible insight.</p>
                <div class="dd-container">
                    <div class="mcq-option" style="cursor:default">
                        <strong>Website visitors: </strong>
                        <select style="margin-left:auto; padding:5px; border-radius:4px;" id="dd-1">
                            <option value="">Select Insight...</option>
                            <option value="Class average">Class average</option>
                            <option value="Most popular page">Most popular page</option>
                            <option value="Best selling product">Best selling product</option>
                        </select>
                    </div>
                    <div class="mcq-option" style="cursor:default">
                        <strong>Student marks: </strong>
                        <select style="margin-left:auto; padding:5px; border-radius:4px;" id="dd-2">
                            <option value="">Select Insight...</option>
                            <option value="Class average">Class average</option>
                            <option value="Most popular page">Most popular page</option>
                            <option value="Best selling product">Best selling product</option>
                        </select>
                    </div>
                    <div class="mcq-option" style="cursor:default">
                        <strong>Sales records: </strong>
                        <select style="margin-left:auto; padding:5px; border-radius:4px;" id="dd-3">
                            <option value="">Select Insight...</option>
                            <option value="Class average">Class average</option>
                            <option value="Most popular page">Most popular page</option>
                            <option value="Best selling product">Best selling product</option>
                        </select>
                    </div>
                </div>
                <button class="practice-dark-btn" onclick="checkDDGroup(['dd-1', 'dd-2', 'dd-3'], ['Most popular page', 'Class average', 'Best selling product'], 'feedback-dd-1')">Verify Matches</button>
                <div class="feedback-dark" id="feedback-dd-1"></div>

                <div style="margin-top:30px;">
                    <p>A dataset is:</p>
                    <div id="mcq-m1-2">
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-2')"><span class="mcq-prefix">A.</span> A collection of organized data</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-2')"><span class="mcq-prefix">B.</span> A type of graph</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-2')"><span class="mcq-prefix">C.</span> A statistical formula</div>
                        <div class="mcq-option" onclick="selectMCQ(this, 'mcq-m1-2')"><span class="mcq-prefix">D.</span> A programming language</div>
                    </div>
                    <button class="practice-dark-btn" onclick="checkMCQ('mcq-m1-2', 'A', 'Correct! A dataset is organized data.')">Verify</button>
                    <div class="feedback-dark" id="feedback-mcq-m1-2"></div>
                </div>
                
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
            <div class="interaction-box" style="border-left-color: var(--secondary-blue); background: #f5f3ff;">
                <strong>Insight:</strong> Understanding variable types helps store data correctly, analyze data efficiently, and avoid calculation errors.
            </div>

            <h3 style="margin-top:40px;">3.1 Boolean Data Type</h3>
            <p>Boolean data type stores two possible values: <strong>True</strong> or <strong>False</strong>. Booleans are commonly used in logical conditions and decision making.</p>
            <div class="interaction-box">
                <strong>Example:</strong> <code>is_logged_in = True</code><br>
                Boolean values are used in conditions like:<br><br>
                <code>if is_logged_in:<br>&nbsp;&nbsp;&nbsp;&nbsp;print("Access granted")</code>
            </div>
            
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p><strong>Identify Boolean:</strong> Which of the following can be Boolean? (Select True for yes)</p>
                <div class="tf-row" id="tf-row-bool-1"><span class="tf-statement">Student passed exam</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'bool-1', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'bool-1', false)">No</button></div></div>
                <div class="tf-row" id="tf-row-bool-2"><span class="tf-statement">Number of books</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'bool-2', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'bool-2', false)">No</button></div></div>
                <div class="tf-row" id="tf-row-bool-3"><span class="tf-statement">Payment successful</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'bool-3', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'bool-3', false)">No</button></div></div>
                <div class="tf-row" id="tf-row-bool-4"><span class="tf-statement">Temperature</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'bool-4', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'bool-4', false)">No</button></div></div>
                <button class="practice-dark-btn" onclick="checkTFGroup(['bool-1', 'bool-2', 'bool-3', 'bool-4'], [true, false, true, false], 'feedback-bool-id')">Check Answers</button>
                <div class="feedback-dark" id="feedback-bool-id"></div>

                <div style="margin-top:30px;">
                    <p><strong>True / False</strong></p>
                    <div class="tf-row" id="tf-row-m1-3a"><span class="tf-statement">Boolean variables store True or False.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'm1-3a', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'm1-3a', false)">False</button></div></div>
                    <div class="tf-row" id="tf-row-m1-3b"><span class="tf-statement">Boolean values can be used in conditions.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'm1-3b', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'm1-3b', false)">False</button></div></div>
                    <div class="tf-row" id="tf-row-m1-3c"><span class="tf-statement">Boolean values represent multiple numbers.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'm1-3c', true)">True</button><button class="tf-btn" onclick="selectTF(this, 'm1-3c', false)">False</button></div></div>
                    <button class="practice-dark-btn" onclick="checkTFGroup(['m1-3a', 'm1-3b', 'm1-3c'], [true, true, false], 'feedback-tf-boolean')">Check Answers</button>
                    <div class="feedback-dark" id="feedback-tf-boolean"></div>
                </div>
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

                <div style="margin-top:30px;">
                <p><strong>Drag & Drop (Classification)</strong></p>
                <p>Match the example with numeric type.</p>
                <div class="dd-container">
                    <div class="mcq-option" style="cursor:default">
                        <strong>25: </strong>
                        <select style="margin-left:auto; padding:5px; border-radius:4px;" id="dd-num-1">
                            <option value="">Select Type...</option>
                            <option value="Integer">Integer</option>
                            <option value="Float">Float</option>
                        </select>
                    </div>
                    <div class="mcq-option" style="cursor:default">
                        <strong>12.75: </strong>
                        <select style="margin-left:auto; padding:5px; border-radius:4px;" id="dd-num-2">
                            <option value="">Select Type...</option>
                            <option value="Integer">Integer</option>
                            <option value="Float">Float</option>
                        </select>
                    </div>
                </div>
                <button class="practice-dark-btn" onclick="checkDDGroup(['dd-num-1', 'dd-num-2'], ['Integer', 'Float'], 'feedback-dd-num')">Verify Matches</button>
                <div class="feedback-dark" id="feedback-dd-num"></div>
                </div>
            </div>

            <h3 style="margin-top:40px;">3.3 Integer | 3.4 Float | 3.5 Complex | 3.6 String</h3>
            <p><strong>Integer:</strong> A whole number without decimals (e.g., 5, -3, 0). Used when counts are needed.</p>
            <p><strong>Float:</strong> Represents numbers with decimal values (e.g., 2.5, 3.14). Used for precision like price or weight.</p>
            <p><strong>Complex:</strong> Contains real and imaginary parts (e.g., 3 + 4i). Used in scientific calculations.</p>
            <p><strong>String:</strong> Stores text values (e.g., names, cities). Can contain letters, numbers, symbols.</p>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>

                <p><strong>Identify Integer:</strong> Which of these are integers? (Select True for yes)</p>
                <div class="tf-row" id="tf-row-int-1"><span class="tf-statement">15</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'int-1', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'int-1', false)">No</button></div></div>
                <div class="tf-row" id="tf-row-int-2"><span class="tf-statement">4.8</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'int-2', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'int-2', false)">No</button></div></div>
                <div class="tf-row" id="tf-row-int-3"><span class="tf-statement">-10</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'int-3', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'int-3', false)">No</button></div></div>
                <div class="tf-row" id="tf-row-int-4"><span class="tf-statement">0</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'int-4', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'int-4', false)">No</button></div></div>
                <button class="practice-dark-btn" onclick="checkTFGroup(['int-1', 'int-2', 'int-3', 'int-4'], [true, false, true, true], 'feedback-int-id')">Check Answers</button>
                <div class="feedback-dark" id="feedback-int-id"></div>
                
                <div style="margin-top: 30px;">
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

                <div style="margin-top: 30px;">
                    <p>Which of the following is a string?</p>
                    <div class="tf-row" id="tf-row-str-1"><span class="tf-statement">"India"</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'str-1', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'str-1', false)">No</button></div></div>
                    <div class="tf-row" id="tf-row-str-2"><span class="tf-statement">25</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'str-2', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'str-2', false)">No</button></div></div>
                    <div class="tf-row" id="tf-row-str-3"><span class="tf-statement">"Laptop"</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'str-3', true)">Yes</button><button class="tf-btn" onclick="selectTF(this, 'str-3', false)">No</button></div></div>
                    <button class="practice-dark-btn" onclick="checkTFGroup(['str-1', 'str-2', 'str-3'], [true, false, true], 'feedback-str-id')">Check Answers</button>
                    <div class="feedback-dark" id="feedback-str-id"></div>
                </div>

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

            <div class="quiz-cta" style="margin-top:60px;">
                <h3>Ready for the Knowledge Check?</h3>
                <p>Test your understanding of the core foundations of Data Analytics.</p>
                <a href="module_quiz.html?mod=data1" class="btn-start-quiz">Start Assessment &rarr;</a>
            </div>
"""

new_data1_questions = [
    {
        "id": 1,
        "type": "MCQ",
        "q": "<strong>What is Data?</strong><br>Which statement best describes data?",
        "options": ["Processed information ready for decision making", "Raw facts and figures collected for analysis", "A business strategy", "A summarized report"],
        "a": 1
    },
    {
        "id": 2,
        "type": "TF",
        "q": "<strong>True or False</strong><br>For the statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Data becomes meaningful only after processing and analysis.</span>",
        "options": ["Data becomes meaningful only after processing and analysis."],
        "a": [True]
    },
    {
        "id": 3,
        "type": "MCQ",
        "q": "<strong>Which Data Type Stores Text?</strong><br>Which data type can store a sentence or phrase?",
        "options": ["Integer", "Boolean", "String", "Float"],
        "a": 2
    },
    {
        "id": 4,
        "type": "MCQ",
        "q": "<strong>Identify the Data Type</strong><br>Select the correct data type for the value below.<br><code>is_logged_in = True</code>",
        "options": ["Integer", "Boolean", "String", "Float"],
        "a": 1
    },
    {
        "id": 5,
        "type": "MTF",
        "q": "<strong>Drag and Drop</strong><br>Match the data structure with the description.",
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
        "q": "<strong>Which Data Structure Describes This Data?</strong><br><code>[\"Aabid\", \"Jesenia\", \"Mark\"]</code>",
        "options": ["Table", "List", "Graph", "Matrix"],
        "a": 1
    },
    {
        "id": 7,
        "type": "MCQ",
        "q": "<strong>Multiple Choice</strong><br>Which of the following is quantitative data?",
        "options": ["Eye color", "Age", "Country name", "Product category"],
        "a": 1
    },
    {
        "id": 8,
        "type": "TF",
        "q": "<strong>True or False</strong><br>For the statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Qualitative data describes categories rather than numeric values.</span>",
        "options": ["Qualitative data describes categories rather than numeric values."],
        "a": [True]
    },
    {
        "id": 9,
        "type": "DD",
        "q": "<strong>Match the Data Type</strong><br>Select the correct category for each example from the drop-down.",
        "code": "Gender is [b1] \n Height is [b2] \n Temperature is [b3] \n Country is [b4]",
        "options": [["Qualitative Data", "Quantitative Data"], ["Qualitative Data", "Quantitative Data"], ["Qualitative Data", "Quantitative Data"], ["Qualitative Data", "Quantitative Data"]],
        "a": ["Qualitative Data", "Quantitative Data", "Quantitative Data", "Qualitative Data"]
    },
    {
        "id": 10,
        "type": "MCQ",
        "q": "<strong>Structured vs Unstructured Data</strong><br>Which of the following is structured data?",
        "options": ["Video file", "Email message", "Excel table", "Social media post"],
        "a": 2
    },
    {
        "id": 11,
        "type": "MCQ",
        "q": "<strong>What is Metadata?</strong><br>Metadata refers to:",
        "options": ["Raw data collected from sensors", "Data about other data", "Unstructured data", "Numerical calculations"],
        "a": 1
    },
    {
        "id": 12,
        "type": "MCQ",
        "q": "<strong>Example of Metadata</strong><br>Which of the following is an example of metadata?",
        "options": ["The image itself", "The creation date of a file", "The text inside a document", "The number of users on a website"],
        "a": 1
    },
    {
        "id": 13,
        "type": "MCQ",
        "q": "<strong>Big Data</strong><br>Which statement best describes big data?",
        "options": ["Small datasets stored in spreadsheets", "Extremely large and complex datasets", "Only structured data", "Only text data"],
        "a": 1
    },
    {
        "id": 14,
        "type": "MTF",
        "q": "<strong>Drag and Drop – Statistical Metrics</strong><br>Match the metric with the description.",
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
        "q": "<strong>Data Classification</strong><br>Person A has 5 coins and Person B has 10 coins. The number of coins represents:",
        "options": ["Qualitative data", "Quantitative data", "Metadata", "Ordinal data"],
        "a": 1
    },
    {
        "id": 16,
        "type": "MCQ",
        "q": "<strong>Data Insight Question</strong><br>A company records: Customer age, Purchase amount, Product category.<br>Which of these variables is qualitative data?",
        "options": ["Age", "Purchase amount", "Product category", "All of the above"],
        "a": 2
    }
]

print("Starting to update Data-Module-1.html...")

with open('Data-Module-1.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update main content using safe string replacement
start_tag = '<main class="main-content">'
end_tag = '</main>'

start_idx = text.find(start_tag)
end_idx = text.find(end_tag)

if start_idx != -1 and end_idx != -1:
    before = text[:start_idx + len(start_tag)]
    after = text[end_idx:]
    
    # Add floating contact button CSS
    css_addition = """
    <style>
        .quick-contact-bar {
            position: fixed;
            top: 50%;
            right: 0;
            transform: translateY(-50%);
            background: #111;
            display: flex;
            flex-direction: column;
            padding: 10px 5px;
            z-index: 9999;
            box-shadow: -2px 0 10px rgba(0,0,0,0.5);
        }
        .quick-contact-bar a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            margin: 5px 0;
            border-radius: 50%;
            transition: transform 0.2s;
        }
        .quick-contact-bar a:hover {
            transform: scale(1.1);
        }
        .qc-phone {
            background-color: #2196f3;
        }
        .qc-whatsapp {
            background-color: #4caf50;
        }
        .qc-email {
            background: linear-gradient(135deg, #ef5350, #ffb74d);
        }
        .qc-icon {
            width: 24px;
            height: 24px;
            fill: white;
        }
        .qc-divider {
            width: 100%;
            height: 1px;
            background: #333;
            margin: 5px 0;
        }
        
    </style>
"""
    # Insert Contact Bar HTML before </body>
    contact_bar_html = """
    <div class="quick-contact-bar">
        <a href="tel:+918593850720" class="qc-phone" title="Call Us">
            <svg class="qc-icon" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
        </a>
        <div class="qc-divider"></div>
        <a href="https://wa.me/918593850720" class="qc-whatsapp" title="WhatsApp Us" target="_blank">
            <svg class="qc-icon" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.71.44 3.32 1.24 4.74L2 22l5.48-1.44c1.38.74 2.95 1.15 4.56 1.15 5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2zm0 18.22c-1.42 0-2.8-.38-4.04-1.11l-.29-.17-3 .79.8-2.92-.19-.3A8.09 8.09 0 013.93 11.9c0-4.47 3.63-8.1 8.1-8.1 4.47 0 8.1 3.63 8.1 8.1s-3.63 8.1-8.1 8.1zm4.45-6.04c-.24-.12-1.44-.71-1.66-.79-.22-.08-.38-.12-.54.12-.16.24-.62.79-.76.95-.14.16-.28.18-.52.06-1.54-.74-2.6-1.39-3.6-2.92-.12-.18 0-.28.12-.4.12-.12.24-.28.36-.42.12-.14.16-.24.24-.4.08-.16.04-.3-.02-.42-.06-.12-.54-1.3-.74-1.78-.2-.48-.4-.42-.54-.42h-.46c-.16 0-.42.06-.64.3-.22.24-.84.82-.84 2s.86 2.32.98 2.48c.12.16 1.68 2.56 4.08 3.56.58.24 1.02.38 1.38.48.58.18 1.1.16 1.52.1.46-.08 1.44-.58 1.64-1.14.2-.56.2-1.04.14-1.14-.06-.1-.22-.16-.46-.28z"/></svg>
        </a>
        <div class="qc-divider"></div>
        <a href="mailto:ajaythomas@kvjanalytics.onmicrosoft.com" class="qc-email" title="Email Us">
            <svg class="qc-icon" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </a>
    </div>
"""

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
            feedback.innerHTML = msg;
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
    function checkDDGroup(ids, corrects, fbid) {
        let allRight = true;
        ids.forEach((q, idx) => {
            const el = document.getElementById(q);
            if(el.value !== corrects[idx]) allRight = false;
        });
        const feedback = document.getElementById(fbid);
        if(allRight) {
            feedback.innerText = "All matches correct!";
            feedback.className = 'feedback-dark correct';
        } else {
            feedback.innerText = "Try checking your dropdown selections again!";
            feedback.className = 'feedback-dark wrong';
        }
    }
</script>
</body>
"""
    updated_text = before + "\\n" + html_content + "\\n" + after
    updated_text = updated_text.replace("</head>", css_addition + "</head>")
    updated_text = updated_text.replace("</body>", contact_bar_html + custom_js)

    with open('Data-Module-1.html', 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print("Updated Data-Module-1.html successfully.")

# Update quiz_data.js safely
print("Updating quiz_data.js for data1...")
with open('quiz_data.js', 'r', encoding='utf-8') as f:
    quiz_js = f.read()

new_json_str = '"data1": ' + json.dumps(new_data1_questions, indent=8)

# we can use split and join to safely replace the exact section
parts = re.split(r'"data1": \[.*?\],?\s*"data2"', quiz_js, flags=re.DOTALL)
if len(parts) == 2:
    patch = parts[0] + new_json_str + ',\\n    "data2"' + parts[1]
    with open('quiz_data.js', 'w', encoding='utf-8') as f:
        f.write(patch)
    print("Updated quiz_data.js successfully.")
else:
    print("Could not find the exact pattern in quiz_data.js")

