
import os

content_html = """
            <div class="section-header">
                <h2>1. Data Manipulation</h2>
            </div>
            <h3>Concept</h3>
            <p><strong>Data manipulation</strong> refers to the process of modifying, organizing, and preparing data so it can be analyzed effectively. It is an essential step before performing data analysis because raw data often contains missing values, duplicate records, inconsistent formats, and errors.</p>
            <p>Data manipulation ensures the dataset becomes accurate, consistent, and usable.</p>

            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>Think of data manipulation like preparing ingredients before cooking. Before cooking you must wash vegetables, cut ingredients, and remove spoiled items. Similarly, data must be cleaned and organized before analysis.</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <h4>Knowledge Check: Data Manipulation</h4>
                <p>Which of the following best describes data manipulation?</p>
                <div class="mcq-options" id="mcq-opts-m2-1">
                    <div class="mcq-option" onclick="selectMCQ('m2-1', 'A', 'B', 'Collecting data is extraction.')"><span class="mcq-prefix">A.</span> Collecting data from sensors</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-1', 'B', 'B', 'Correct! Preparation is key.')"><span class="mcq-prefix">B.</span> Preparing and modifying data for analysis</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-1', 'C', 'B', 'Visualization comes after manipulation.')"><span class="mcq-prefix">C.</span> Visualizing data with charts</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-1', 'D', 'B', 'Decisions are made based on the analysis.')"><span class="mcq-prefix">D.</span> Making business decisions</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-1"></div>

                <p style="margin-top: 20px;"><strong>True or False:</strong></p>
                <div class="tf-row" id="tf-row-m2-1-1"><span class="tf-statement">1. Data manipulation improves data quality.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF('m2-1-1', 1, true, true, 'Quality is the goal!')">True</button><button class="tf-btn" onclick="selectTF('m2-1-1', 1, false, true, '')">False</button></div></div>
                <div class="tf-row" id="tf-row-m2-1-2"><span class="tf-statement">2. Raw data is always ready for analysis without modification.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF('m2-1-2', 2, true, false, '')">True</button><button class="tf-btn" onclick="selectTF('m2-1-2', 2, false, false, 'Raw data is almost never perfect.')">False</button></div></div>
            </div>

            <div class="section-header">
                <h2>2. ETL Process</h2>
            </div>
            <p><strong>ETL</strong> stands for <strong>Extract, Transform, and Load</strong>. It is a common process used to move and prepare data for analysis.</p>
            
            <h3>2.1 Extract</h3>
            <p>Data is collected from various sources, such as databases, files, websites, and applications. The extracted data is temporarily stored in a staging area.</p>
            
            <h3>2.2 Transform</h3>
            <p>In this stage, the extracted data is cleaned and converted into a useful format. Examples include removing duplicates, correcting errors, and converting formats.</p>
            
            <h3>2.3 Load</h3>
            <p>After transformation, the cleaned data is stored in a target system, such as a data warehouse or database.</p>

            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>ETL ensures that data from different sources becomes consistent and ready for analysis.</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <h4>Knowledge Check: ETL</h4>
                <p>What does ETL stand for?</p>
                <div class="mcq-options" id="mcq-opts-m2-2">
                    <div class="mcq-option" onclick="selectMCQ('m2-2', 'A', 'B', 'Transform is the middle step.')"><span class="mcq-prefix">A.</span> Extract, Transfer, Load</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-2', 'B', 'B', 'Exactly right!')"><span class="mcq-prefix">B.</span> Extract, Transform, Load</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-2', 'C', 'B', 'Linking is not part of ETL.')"><span class="mcq-prefix">C.</span> Enter, Transform, Link</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-2', 'D', 'B', 'Export is different from Extract.')"><span class="mcq-prefix">D.</span> Export, Transfer, Link</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-2"></div>

                <p style="margin-top: 20px;"><strong>Drag & Match:</strong> Match the ETL step with its description.</p>
                <div class="dnd-options" id="opts-m2-etl">
                    <div class="dnd-option" draggable="true" data-val="E">Extract</div>
                    <div class="dnd-option" draggable="true" data-val="T">Transform</div>
                    <div class="dnd-option" draggable="true" data-val="L">Load</div>
                </div>

                <div class="dd-container" id="dd-m2-etl">
                    <div class="dd-row"><div class="dd-label">Collect data from sources</div><div class="dd-target dnd-target" id="target-m2-e">Drop here...</div></div>
                    <div class="dd-row"><div class="dd-label">Clean and process data</div><div class="dd-target dnd-target" id="target-m2-t">Drop here...</div></div>
                    <div class="dd-row"><div class="dd-label">Store data into database</div><div class="dd-target dnd-target" id="target-m2-l">Drop here...</div></div>
                </div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkDND('dd-m2-etl', ['E', 'T', 'L'])">Check Matching</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetDND('dd-m2-etl', 'opts-m2-etl')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-dd-m2-etl"></div>

                <div class="practice-space-dark" style="margin-top: 30px;">
                    <h3>Scenario Question</h3>
                    <p>A company collects sales data from an online store, a physical store, and a mobile app. Explain which ETL stage combines and cleans this data.</p>
                    <div class="practice-dark-box">
                        <input type="text" id="ans-m2-scenario" placeholder="Type the stage name (e.g., Load)...">
                        <button class="practice-dark-btn" onclick="checkDark('m2-scenario', 'Transform', 'Correct! Transform handles cleaning and combining.')">Submit</button>
                    </div>
                    <div id="feedback-m2-scenario" class="feedback-dark"></div>
                </div>
            </div>

            <div class="section-header">
                <h2>3. Common Data File Formats</h2>
            </div>
            <p>Data is often stored and transferred using common file formats such as <strong>CSV, XML, and JSON.</strong></p>
            
            <h3>CSV (Comma Separated Values)</h3>
            <p>Data is separated by commas. It is often used for spreadsheets and tabular data.</p>
            <div class="interaction-box">
                <strong>Example:</strong>
                <pre>Name,Age,City\nArjun,28,Kochi</pre>
            </div>

            <h3>XML (Extensible Markup Language)</h3>
            <p>Uses tags to describe data structure, similar to HTML.</p>
            <div class="interaction-box">
                <strong>Example:</strong>
                <pre>&lt;name&gt;Arjun&lt;/name&gt;</pre>
            </div>

            <h3>JSON (JavaScript Object Notation)</h3>
            <p>Stores data in key-value pairs. It is lightweight and easy for machines to parse.</p>
            <div class="interaction-box">
                <strong>Example:</strong>
                <pre>{\n  "name": "Arjun",\n  "age": 28\n}</pre>
            </div>

            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>These formats make it easy to exchange data between systems and applications.</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <h4>Knowledge Check: File Formats</h4>
                <p>Which file format stores data separated by commas?</p>
                <div class="mcq-options" id="mcq-opts-m2-3">
                    <div class="mcq-option" onclick="selectMCQ('m2-3', 'A', 'B', 'XML uses tags.')"><span class="mcq-prefix">A.</span> XML</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-3', 'B', 'B', 'Correct!')"><span class="mcq-prefix">B.</span> CSV</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-3', 'C', 'B', 'JSON uses key-value pairs.')"><span class="mcq-prefix">C.</span> JSON</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-3', 'D', 'B', 'SQL is a language, not a file format.')"><span class="mcq-prefix">D.</span> SQL</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-3"></div>

                <p style="margin-top: 20px;"><strong>True or False:</strong></p>
                <div class="tf-row" id="tf-row-m2-3-1"><span class="tf-statement">1. JSON stores data using key-value pairs.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF('m2-3-1', 1, true, true, 'Spot on!')">True</button><button class="tf-btn" onclick="selectTF('m2-3-1', 1, false, true, '')">False</button></div></div>
                <div class="tf-row" id="tf-row-m2-3-2"><span class="tf-statement">2. CSV files are commonly used for spreadsheet data.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF('m2-3-2', 2, true, true, 'Excel loves CSVs.')">True</button><button class="tf-btn" onclick="selectTF('m2-3-2', 2, false, true, '')">False</button></div></div>
            </div>

            <div class="section-header">
                <h2>4. Data Cleaning</h2>
            </div>
            <p><strong>Data cleaning</strong> is the process of identifying and correcting errors or inconsistencies in a dataset. The goal is to ensure data becomes <strong>accurate, complete, and consistent.</strong></p>
            
            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>Poor data quality leads to wrong analysis and incorrect decisions. Cleaning data improves reliability.</p>
            </div>

            <h3>4.1 Handling Missing Values</h3>
            <p>Missing values occur when data is not recorded or is unavailable. They are often represented as <strong>NULL</strong> or <strong>NaN</strong>.</p>
            <div class="interaction-box">
                <strong>Example:</strong>
                <table class="data-table">
                    <tr><th>Name</th><th>Age</th></tr>
                    <tr><td>John</td><td>24</td></tr>
                    <tr><td>Sarah</td><td><span style="color:red">NULL</span></td></tr>
                </table>
            </div>
            <p>Missing values can be handled by replacing them with the <strong>mean or median</strong>, or by <strong>removing rows</strong> entirely.</p>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Missing values in a dataset are often called:</p>
                <div class="mcq-options" id="mcq-opts-m2-4-1">
                    <div class="mcq-option" onclick="selectMCQ('m2-4-1', 'A', 'B', 'Duplicates are repeated records.')"><span class="mcq-prefix">A.</span> duplicates</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-1', 'B', 'B', 'Correct!')"><span class="mcq-prefix">B.</span> null values</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-1', 'C', 'B', '')"><span class="mcq-prefix">C.</span> indexes</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-1', 'D', 'B', 'Metadata is data about data.')"><span class="mcq-prefix">D.</span> metadata</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-4-1"></div>
            </div>

            <h3>4.2 Removing Special Characters</h3>
            <p>Special characters (like @, #, $, %, &) can cause processing errors. They should be removed or encoded correctly.</p>
            <div class="tf-row" id="tf-row-m2-4-2"><span class="tf-statement">Special characters can cause problems during data processing.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF('m2-4-2', 1, true, true, 'True! They often break scripts.')">True</button><button class="tf-btn" onclick="selectTF('m2-4-2', 1, false, true, '')">False</button></div></div>

            <h3>4.3 Trimming Spaces</h3>
            <p>Extra spaces at the beginning or end of text (e.g., "  fruits  ") should be removed to ensure consistent matching.</p>
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Why is trimming spaces important?</p>
                <div class="mcq-options" id="mcq-opts-m2-4-3">
                    <div class="mcq-option" onclick="selectMCQ('m2-4-3', 'A', 'A', 'Correct! Consistency prevents search errors.')"><span class="mcq-prefix">A.</span> Improves formatting consistency</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-3', 'B', 'A', 'Spaces occupy very little space.')"><span class="mcq-prefix">B.</span> Reduces file size</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-3', 'C', 'A', 'It doesn\'t delete rows.')"><span class="mcq-prefix">C.</span> Deletes rows</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-3', 'D', 'A', 'Charts are for visualization.')"><span class="mcq-prefix">D.</span> Creates charts</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-4-3"></div>
            </div>

            <h3>4.4 Removing Duplicates</h3>
            <p>Duplicate records can lead to incorrect counts and wrong statistics. One of the duplicate records must be removed.</p>
            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>Duplicate data can cause incorrect counts and wrong statistics.</p>
            </div>
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Duplicate records should be:</p>
                <div class="mcq-options" id="mcq-opts-m2-4-4">
                    <div class="mcq-option" onclick="selectMCQ('m2-4-4', 'A', 'B', '')"><span class="mcq-prefix">A.</span> Ignored</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-4', 'B', 'B', 'Correct! Keep it unique.')"><span class="mcq-prefix">B.</span> Removed</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-4', 'C', 'B', '')"><span class="mcq-prefix">C.</span> Multiplied</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-4', 'D', 'B', '')"><span class="mcq-prefix">D.</span> Added</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-4-4"></div>
            </div>

            <div class="section-header">
                <h2>5. Organizing Data</h2>
            </div>
            <p>After cleaning, data is organized using methods like <strong>Sorting, Filtering, Slicing, Transposing, Appending, and Truncating.</strong></p>
            
            <h3>5.1 Sorting</h3>
            <p><strong>Sorting</strong> arranges data in ascending or descending order (e.g., sorting employees by salary).</p>
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Sorting data helps to:</p>
                <div class="mcq-options" id="mcq-opts-m2-5-1">
                    <div class="mcq-option" onclick="selectMCQ('m2-5-1', 'A', 'B', '')"><span class="mcq-prefix">A.</span> Delete records</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-1', 'B', 'B', 'Correct!')"><span class="mcq-prefix">B.</span> Arrange data logically</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-1', 'C', 'B', '')"><span class="mcq-prefix">C.</span> Create duplicates</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-1', 'D', 'B', '')"><span class="mcq-prefix">D.</span> Remove columns</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-5-1"></div>
            </div>

            <h3>5.2 Filtering</h3>
            <p><strong>Filtering</strong> selects records based on specific conditions (e.g., show only employees with a salary > 50,000).</p>
            <div class="tf-row" id="tf-row-m2-5-2"><span class="tf-statement">Filtering hides records that do not meet the condition.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF('m2-5-2', 1, true, true, 'Correct!')">True</button><button class="tf-btn" onclick="selectTF('m2-5-2', 1, false, true, '')">False</button></div></div>

            <h3>5.3 Transposing</h3>
            <p><strong>Transposing</strong> changes rows into columns or columns into rows.</p>
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Transposing changes:</p>
                <div class="mcq-options" id="mcq-opts-m2-5-3">
                    <div class="mcq-option" onclick="selectMCQ('m2-5-3', 'A', 'B', '')"><span class="mcq-prefix">A.</span> Data values</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-3', 'B', 'B', 'Correct! Rows to Columns.')"><span class="mcq-prefix">B.</span> Data orientation</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-3', 'C', 'B', '')"><span class="mcq-prefix">C.</span> Data types</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-3', 'D', 'B', '')"><span class="mcq-prefix">D.</span> Data accuracy</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-5-3"></div>
            </div>

            <div class="section-header">
                <h2>6. Aggregating Data</h2>
            </div>
            <p><strong>Aggregation</strong> means combining multiple data values to produce summary results like <strong>Sum, Count, and Average.</strong></p>
            
            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>Aggregation helps understand overall trends instead of individual records.</p>
            </div>

            <h3>6.1 Grouping (SUM, COUNT, AVG)</h3>
            <ul>
                <li><strong>SUM:</strong> Total value (e.g., Total sales per region).</li>
                <li><strong>COUNT:</strong> Number of records (e.g., Number of employees per department).</li>
                <li><strong>AVG:</strong> Mean value (e.g., Average salary per department).</li>
            </ul>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <h4>Knowledge Check: Aggregation</h4>
                
                <p><strong>Drag & Match:</strong> Match the metric with its description.</p>
                <div class="dnd-options" id="opts-m2-agg">
                    <div class="dnd-option" draggable="true" data-val="S">Sum</div>
                    <div class="dnd-option" draggable="true" data-val="C">Count</div>
                    <div class="dnd-option" draggable="true" data-val="A">Average</div>
                </div>

                <div class="dd-container" id="dd-m2-agg">
                    <div class="dd-row"><div class="dd-label">Total value</div><div class="dd-target dnd-target" id="target-m2-s">Drop here...</div></div>
                    <div class="dd-row"><div class="dd-label">Number of records</div><div class="dd-target dnd-target" id="target-m2-c">Drop here...</div></div>
                    <div class="dd-row"><div class="dd-label">Mean value</div><div class="dd-target dnd-target" id="target-m2-a">Drop here...</div></div>
                </div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkDND('dd-m2-agg', ['S', 'C', 'A'])">Check Aggregation</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetDND('dd-m2-agg', 'opts-m2-agg')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-dd-m2-agg"></div>

                <p style="margin-top: 30px;">Aggregation is mainly used to:</p>
                <div class="mcq-options" id="mcq-opts-m2-6">
                    <div class="mcq-option" onclick="selectMCQ('m2-6', 'A', 'B', '')"><span class="mcq-prefix">A.</span> visualize data</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-6', 'B', 'B', 'Correct! Summarization is the core.')"><span class="mcq-prefix">B.</span> summarize data</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-6', 'C', 'B', '')"><span class="mcq-prefix">C.</span> collect data</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-6', 'D', 'B', '')"><span class="mcq-prefix">D.</span> delete data</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-6"></div>
            </div>

            <!-- Quiz CTA -->
            <div class="quiz-cta">
                <h3>Module 2 Assessment Ready.</h3>
                <p>Test your skills in data manipulation, ETL, and cleaning.</p>
                <a href="module_quiz.html?mod=d2" class="btn-start-quiz">Start Assessment &rarr;</a>
            </div>
"""

# Now add the missing JS functions for DND
js_to_add = """
        // Drag and Drop Logic
        let draggedItem = null;

        document.addEventListener('dragstart', (e) => {
            if (e.target.classList.contains('dnd-option')) {
                draggedItem = e.target;
                e.target.style.opacity = '0.5';
            }
        });

        document.addEventListener('dragend', (e) => {
            if (e.target.classList.contains('dnd-option')) {
                e.target.style.opacity = '1';
            }
        });

        document.addEventListener('dragover', (e) => {
            e.preventDefault();
        });

        document.addEventListener('drop', (e) => {
            e.preventDefault();
            const target = e.target.closest('.dnd-target');
            if (target && draggedItem) {
                target.innerHTML = draggedItem.innerText;
                target.setAttribute('data-ans', draggedItem.getAttribute('data-val'));
                target.classList.add('filled');
            }
        });

        function checkDND(containerId, correctAnswers) {
            const container = document.getElementById(containerId);
            const targets = container.getElementsByClassName('dnd-target');
            const feedback = document.getElementById(`feedback-${containerId}`);
            let allCorrect = true;
            let allFilled = true;

            for (let i = 0; i < targets.length; i++) {
                const userVal = targets[i].getAttribute('data-ans');
                if (!userVal) { allFilled = false; break; }
                if (userVal !== correctAnswers[i]) allCorrect = false;
            }

            if (!allFilled) {
                feedback.innerHTML = "Please complete all fields.";
                feedback.className = "feedback-dark wrong";
            } else if (allCorrect) {
                feedback.innerHTML = "Correct! Well done. 🎉";
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            } else {
                feedback.innerHTML = "Incorrect. Try again!";
                feedback.className = "feedback-dark wrong";
            }
        }

        function resetDND(containerId, optsId) {
            const container = document.getElementById(containerId);
            const targets = container.getElementsByClassName('dnd-target');
            const feedback = document.getElementById(`feedback-${containerId}`);
            
            for (let t of targets) {
                t.innerHTML = "Drop here...";
                t.removeAttribute('data-ans');
                t.classList.remove('filled');
            }
            feedback.style.display = "none";
        }
"""

with open('Data-Module-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the main content
start_marker = '<main class="main-content">'
end_marker = '</main>'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx) + len(end_marker)

new_main = start_marker + '\n' + content_html + '\n' + end_marker
html = html[:start_idx] + new_main + html[end_idx:]

# Insert the JS functions before the closing script tag or before another function
script_end_marker = '</script>'
# We'll put it before the last script tag
last_script_idx = html.rfind(script_end_marker)
html = html[:last_script_idx] + js_to_add + html[last_script_idx:]

with open('Data-Module-2.html', 'w', encoding='utf-8') as f:
    f.write(html)
