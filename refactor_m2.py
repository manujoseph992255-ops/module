
import os

with open('Data-Module-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Practice Card 1 (Section 1)
pc1_old = """<div class="practice-card">
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
            </div>"""

pc1_new = """<div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <h4>Knowledge Check: Data Manipulation</h4>
                <p>Which of the following best describes data manipulation?</p>
                <div class="mcq-options" id="mcq-m2-1">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-1')"><span class="mcq-prefix">A.</span> Collecting data from sensors</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-1')"><span class="mcq-prefix">B.</span> Preparing and modifying data for analysis</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-1')"><span class="mcq-prefix">C.</span> Visualizing data with charts</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-1')"><span class="mcq-prefix">D.</span> Making business decisions</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m2-1', 'B', 'Correct! Preparation is key.')">Verify</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMCQ_v2('mcq-m2-1')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-mcq-m2-1"></div>

                <p style="margin-top: 30px;"><strong>True or False:</strong></p>
                <div class="tf-row" id="tf-row-m2-1-1"><span class="tf-statement">1. Data manipulation improves data quality.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-1-1', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-1-1', false)">False</button></div></div>
                <div class="tf-row" id="tf-row-m2-1-2"><span class="tf-statement">2. Raw data is always ready for analysis without modification.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-1-2', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-1-2', false)">False</button></div></div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkTFGroup_v2(['tf-m2-1-1', 'tf-m2-1-2'], [true, false], 'feedback-tf-m2-1')">Check Answers</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetTFGroup_v2(['tf-m2-1-1', 'tf-m2-1-2'], 'feedback-tf-m2-1')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-tf-m2-1"></div>
            </div>"""

html = html.replace(pc1_old, pc1_new)

# Update MCQ 2 (ETL)
mcq2_old = """<div class="mcq-options" id="mcq-opts-m2-2">
                    <div class="mcq-option" onclick="selectMCQ('m2-2', 'A', 'B', 'Transform is the middle step.')"><span class="mcq-prefix">A.</span> Extract, Transfer, Load</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-2', 'B', 'B', 'Exactly right!')"><span class="mcq-prefix">B.</span> Extract, Transform, Load</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-2', 'C', 'B', 'Linking is not part of ETL.')"><span class="mcq-prefix">C.</span> Enter, Transform, Link</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-2', 'D', 'B', 'Export is different from Extract.')"><span class="mcq-prefix">D.</span> Export, Transfer, Link</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-2"></div>"""

mcq2_new = """<div class="mcq-options" id="mcq-m2-2">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-2')"><span class="mcq-prefix">A.</span> Extract, Transfer, Load</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-2')"><span class="mcq-prefix">B.</span> Extract, Transform, Load</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-2')"><span class="mcq-prefix">C.</span> Enter, Transform, Link</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-2')"><span class="mcq-prefix">D.</span> Export, Transfer, Link</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m2-2', 'B', 'Exactly right!')">Verify</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMCQ_v2('mcq-m2-2')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-mcq-m2-2"></div>"""

html = html.replace(mcq2_old, mcq2_new)

# Update MCQ 3 (File Formats)
mcq3_old = """<div class="mcq-options" id="mcq-opts-m2-3">
                    <div class="mcq-option" onclick="selectMCQ('m2-3', 'A', 'B', 'XML uses tags.')"><span class="mcq-prefix">A.</span> XML</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-3', 'B', 'B', 'Correct!')"><span class="mcq-prefix">B.</span> CSV</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-3', 'C', 'B', 'JSON uses key-value pairs.')"><span class="mcq-prefix">C.</span> JSON</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-3', 'D', 'B', 'SQL is a language, not a file format.')"><span class="mcq-prefix">D.</span> SQL</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-3"></div>"""

mcq3_new = """<div class="mcq-options" id="mcq-m2-3">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-3')"><span class="mcq-prefix">A.</span> XML</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-3')"><span class="mcq-prefix">B.</span> CSV</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-3')"><span class="mcq-prefix">C.</span> JSON</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-3')"><span class="mcq-prefix">D.</span> SQL</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m2-3', 'B', 'Correct!')">Verify</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMCQ_v2('mcq-m2-3')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-mcq-m2-3"></div>"""

html = html.replace(mcq3_old, mcq3_new)

# Update T/F 3
tf3_old = """<p style="margin-top: 20px;"><strong>True or False:</strong></p>
                <div class="tf-row" id="tf-row-m2-3-1"><span class="tf-statement">1. JSON stores data using key-value pairs.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF('m2-3-1', 1, true, true, 'Spot on!')">True</button><button class="tf-btn" onclick="selectTF('m2-3-1', 1, false, true, '')">False</button></div></div>
                <div class="tf-row" id="tf-row-m2-3-2"><span class="tf-statement">2. CSV files are commonly used for spreadsheet data.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF('m2-3-2', 2, true, true, 'Excel loves CSVs.')">True</button><button class="tf-btn" onclick="selectTF('m2-3-2', 2, false, true, '')">False</button></div></div>"""

tf3_new = """<p style="margin-top: 30px;"><strong>True or False:</strong></p>
                <div class="tf-row" id="tf-row-m2-3-1"><span class="tf-statement">1. JSON stores data using key-value pairs.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-3-1', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-3-1', false)">False</button></div></div>
                <div class="tf-row" id="tf-row-m2-3-2"><span class="tf-statement">2. CSV files are commonly used for spreadsheet data.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-3-2', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-3-2', false)">False</button></div></div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkTFGroup_v2(['tf-m2-3-1', 'tf-m2-3-2'], [true, true], 'feedback-tf-m2-3')">Check Answers</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetTFGroup_v2(['tf-m2-3-1', 'tf-m2-3-2'], 'feedback-tf-m2-3')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-tf-m2-3"></div>"""

html = html.replace(tf3_old, tf3_new)

# Update MCQ 4.1
mcq4_1_old = """<div class="mcq-options" id="mcq-opts-m2-4-1">
                    <div class="mcq-option" onclick="selectMCQ('m2-4-1', 'A', 'B', 'Duplicates are repeated records.')"><span class="mcq-prefix">A.</span> duplicates</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-1', 'B', 'B', 'Correct!')"><span class="mcq-prefix">B.</span> null values</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-1', 'C', 'B', '')"><span class="mcq-prefix">C.</span> indexes</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-1', 'D', 'B', 'Metadata is data about data.')"><span class="mcq-prefix">D.</span> metadata</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-4-1"></div>"""

mcq4_1_new = """<div class="mcq-options" id="mcq-m2-4-1">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-1')"><span class="mcq-prefix">A.</span> duplicates</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-1')"><span class="mcq-prefix">B.</span> null values</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-1')"><span class="mcq-prefix">C.</span> indexes</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-1')"><span class="mcq-prefix">D.</span> metadata</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m2-4-1', 'B', 'Correct!')">Verify</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMCQ_v2('mcq-m2-4-1')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-mcq-m2-4-1"></div>"""

html = html.replace(mcq4_1_old, mcq4_1_new)

# Update T/F 4.2
tf4_2_old = """<div class="tf-row" id="tf-row-m2-4-2"><span class="tf-statement">Special characters can cause problems during data processing.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF('m2-4-2', 1, true, true, 'True! They often break scripts.')">True</button><button class="tf-btn" onclick="selectTF('m2-4-2', 1, false, true, '')">False</button></div></div>"""

tf4_2_new = """<div class="tf-row" id="tf-row-m2-4-2"><span class="tf-statement">Special characters can cause problems during data processing.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-4-2', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-4-2', false)">False</button></div></div>
            <button class="practice-dark-btn" style="margin-top:10px;" onclick="checkTFGroup_v2(['tf-m2-4-2'], [true], 'feedback-tf-m2-4-2')">Check Answer</button>
            <button class="practice-dark-btn" style="background:#334155; margin-left:10px; margin-top:10px;" onclick="resetTFGroup_v2(['tf-m2-4-2'], 'feedback-tf-m2-4-2')">&#8635; Reset</button>
            <div class="feedback-dark" id="feedback-tf-m2-4-2"></div>"""

html = html.replace(tf4_2_old, tf4_2_new)

# Update MCQ 4.3
mcq4_3_old = """<div class="mcq-options" id="mcq-opts-m2-4-3">
                    <div class="mcq-option" onclick="selectMCQ('m2-4-3', 'A', 'A', 'Correct! Consistency prevents search errors.')"><span class="mcq-prefix">A.</span> Improves formatting consistency</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-3', 'B', 'A', 'Spaces occupy very little space.')"><span class="mcq-prefix">B.</span> Reduces file size</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-3', 'C', 'A', 'It doesn\\'t delete rows.')"><span class="mcq-prefix">C.</span> Deletes rows</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-3', 'D', 'A', 'Charts are for visualization.')"><span class="mcq-prefix">D.</span> Creates charts</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-4-3"></div>"""

mcq4_3_new = """<div class="mcq-options" id="mcq-m2-4-3">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-3')"><span class="mcq-prefix">A.</span> Improves formatting consistency</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-3')"><span class="mcq-prefix">B.</span> Reduces file size</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-3')"><span class="mcq-prefix">C.</span> Deletes rows</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-3')"><span class="mcq-prefix">D.</span> Creates charts</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m2-4-3', 'A', 'Correct! Consistency prevents search errors.')">Verify</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMCQ_v2('mcq-m2-4-3')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-mcq-m2-4-3"></div>"""

html = html.replace(mcq4_3_old, mcq4_3_new)

# Update MCQ 4.4
mcq4_4_old = """<div class="mcq-options" id="mcq-opts-m2-4-4">
                    <div class="mcq-option" onclick="selectMCQ('m2-4-4', 'A', 'B', '')"><span class="mcq-prefix">A.</span> Ignored</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-4', 'B', 'B', 'Correct! Keep it unique.')"><span class="mcq-prefix">B.</span> Removed</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-4', 'C', 'B', '')"><span class="mcq-prefix">C.</span> Multiplied</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-4-4', 'D', 'B', '')"><span class="mcq-prefix">D.</span> Added</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-4-4"></div>"""

mcq4_4_new = """<div class="mcq-options" id="mcq-m2-4-4">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-4')"><span class="mcq-prefix">A.</span> Ignored</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-4')"><span class="mcq-prefix">B.</span> Removed</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-4')"><span class="mcq-prefix">C.</span> Multiplied</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-4-4')"><span class="mcq-prefix">D.</span> Added</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m2-4-4', 'B', 'Correct! Keep it unique.')">Verify</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMCQ_v2('mcq-m2-4-4')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-mcq-m2-4-4"></div>"""

html = html.replace(mcq4_4_old, mcq4_4_new)

# Update MCQ 5.1
mcq5_1_old = """<div class="mcq-options" id="mcq-opts-m2-5-1">
                    <div class="mcq-option" onclick="selectMCQ('m2-5-1', 'A', 'B', '')"><span class="mcq-prefix">A.</span> Delete records</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-1', 'B', 'B', 'Correct!')"><span class="mcq-prefix">B.</span> Arrange data logically</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-1', 'C', 'B', '')"><span class="mcq-prefix">C.</span> Create duplicates</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-1', 'D', 'B', '')"><span class="mcq-prefix">D.</span> Remove columns</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-5-1"></div>"""

mcq5_1_new = """<div class="mcq-options" id="mcq-m2-5-1">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-5-1')"><span class="mcq-prefix">A.</span> Delete records</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-5-1')"><span class="mcq-prefix">B.</span> Arrange data logically</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-5-1')"><span class="mcq-prefix">C.</span> Create duplicates</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-5-1')"><span class="mcq-prefix">D.</span> Remove columns</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m2-5-1', 'B', 'Correct!')">Verify</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMCQ_v2('mcq-m2-5-1')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-mcq-m2-5-1"></div>"""

html = html.replace(mcq5_1_old, mcq5_1_new)

# Update T/F 5.2
tf5_2_old = """<div class="tf-row" id="tf-row-m2-5-2"><span class="tf-statement">Filtering hides records that do not meet the condition.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF('m2-5-2', 1, true, true, 'Correct!')">True</button><button class="tf-btn" onclick="selectTF('m2-5-2', 1, false, true, '')">False</button></div></div>"""

tf5_2_new = """<div class="tf-row" id="tf-row-m2-5-2"><span class="tf-statement">Filtering hides records that do not meet the condition.</span><div class="tf-buttons"><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-5-2', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'tf-m2-5-2', false)">False</button></div></div>
            <button class="practice-dark-btn" style="margin-top:10px;" onclick="checkTFGroup_v2(['tf-m2-5-2'], [true], 'feedback-tf-m2-5-2')">Check Answer</button>
            <button class="practice-dark-btn" style="background:#334155; margin-left:10px; margin-top:10px;" onclick="resetTFGroup_v2(['tf-m2-5-2'], 'feedback-tf-m2-5-2')">&#8635; Reset</button>
            <div class="feedback-dark" id="feedback-tf-m2-5-2"></div>"""

html = html.replace(tf5_2_old, tf5_2_new)

# Update MCQ 5.3
mcq5_3_old = """<div class="mcq-options" id="mcq-opts-m2-5-3">
                    <div class="mcq-option" onclick="selectMCQ('m2-5-3', 'A', 'B', '')"><span class="mcq-prefix">A.</span> Data values</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-3', 'B', 'B', 'Correct! Rows to Columns.')"><span class="mcq-prefix">B.</span> Data orientation</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-3', 'C', 'B', '')"><span class="mcq-prefix">C.</span> Data types</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-5-3', 'D', 'B', '')"><span class="mcq-prefix">D.</span> Data accuracy</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-5-3"></div>"""

mcq5_3_new = """<div class="mcq-options" id="mcq-m2-5-3">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-5-3')"><span class="mcq-prefix">A.</span> Data values</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-5-3')"><span class="mcq-prefix">B.</span> Data orientation</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-5-3')"><span class="mcq-prefix">C.</span> Data types</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-5-3')"><span class="mcq-prefix">D.</span> Data accuracy</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m2-5-3', 'B', 'Correct! Rows to Columns.')">Verify</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMCQ_v2('mcq-m2-5-3')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-mcq-m2-5-3"></div>"""

html = html.replace(mcq5_3_old, mcq5_3_new)

# Update MCQ 6
mcq6_old = """<div class="mcq-options" id="mcq-opts-m2-6">
                    <div class="mcq-option" onclick="selectMCQ('m2-6', 'A', 'B', '')"><span class="mcq-prefix">A.</span> visualize data</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-6', 'B', 'B', 'Correct! Summarization is the core.')"><span class="mcq-prefix">B.</span> summarize data</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-6', 'C', 'B', '')"><span class="mcq-prefix">C.</span> collect data</div>
                    <div class="mcq-option" onclick="selectMCQ('m2-6', 'D', 'B', '')"><span class="mcq-prefix">D.</span> delete data</div>
                </div>
                <div class="feedback-dark" id="feedback-m2-6"></div>"""

mcq6_new = """<div class="mcq-options" id="mcq-m2-6">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-6')"><span class="mcq-prefix">A.</span> visualize data</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-6')"><span class="mcq-prefix">B.</span> summarize data</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-6')"><span class="mcq-prefix">C.</span> collect data</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m2-6')"><span class="mcq-prefix">D.</span> delete data</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m2-6', 'B', 'Correct! Summarization is the core.')">Verify</button>
                <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetMCQ_v2('mcq-m2-6')">&#8635; Reset</button>
                <div class="feedback-dark" id="feedback-mcq-m2-6"></div>"""

html = html.replace(mcq6_old, mcq6_new)

# Update script section
script_v2 = """
        // Interaction Logic v2 (Synced with Module 1 but with Dark Feedback)
        const tf_data_v2 = {};

        function selectMCQ_v2(element, qid) {
            const container = document.getElementById(qid);
            container.querySelectorAll('.mcq-option').forEach(o => o.classList.remove('selected'));
            element.classList.add('selected');
        }

        function checkMCQ_v2(qid, correctPrefix, successMsg) {
            const container = document.getElementById(qid);
            const selected = container.querySelector('.mcq-option.selected');
            const feedback = document.getElementById('feedback-' + qid);
            if(!selected) return;
            
            // Disable options
            container.querySelectorAll('.mcq-option').forEach(o => o.classList.add('disabled'));
            
            if(selected.innerText.trim().startsWith(correctPrefix + ".")) {
                selected.classList.add('correct');
                feedback.innerHTML = "Correct! " + successMsg + " ✨";
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            } else {
                selected.classList.add('wrong');
                // Find correct one to highlight
                container.querySelectorAll('.mcq-option').forEach(o => {
                    if(o.innerText.trim().startsWith(correctPrefix + ".")) o.classList.add('correct');
                });
                feedback.innerHTML = "Incorrect. Try again!";
                feedback.className = "feedback-dark wrong";
            }
        }

        function resetMCQ_v2(qid) {
            const container = document.getElementById(qid);
            container.querySelectorAll('.mcq-option').forEach(o => {
                o.classList.remove('selected', 'correct', 'wrong', 'disabled');
            });
            const feedback = document.getElementById('feedback-' + qid);
            feedback.style.display = "none";
        }

        function selectTF_v2(element, tid, val) {
            const row = element.closest('.tf-row');
            row.querySelectorAll('.tf-btn').forEach(b => b.classList.remove('selected-true', 'selected-false'));
            element.classList.add(val ? 'selected-true' : 'selected-false');
            tf_data_v2[tid] = val;
        }

        function checkTFGroup_v2(tids, corrects, fid) {
            let allCorrect = true;
            const feedback = document.getElementById(fid);
            
            // Check if all answered
            for(let i=0; i<tids.length; i++) {
                if(tf_data_v2[tids[i]] === undefined) {
                    feedback.innerHTML = "Please answer all questions.";
                    feedback.className = "feedback-dark wrong";
                    feedback.style.display = "block";
                    return;
                }
            }

            for(let i=0; i<tids.length; i++) {
                const row = document.getElementById('tf-row-' + tids[i]);
                const buttons = row.querySelectorAll('.tf-btn');
                buttons.forEach(b => b.classList.add('disabled'));
                
                if(tf_data_v2[tids[i]] === corrects[i]) {
                    // Highlight correct buttons
                    buttons.forEach(b => {
                        if((b.innerText === 'True' && corrects[i]) || (b.innerText === 'False' && !corrects[i])) b.classList.add('correct');
                    });
                } else {
                    allCorrect = false;
                    buttons.forEach(b => {
                        if((b.innerText === 'True' && tf_data_v2[tids[i]]) || (b.innerText === 'False' && !tf_data_v2[tids[i]])) b.classList.add('wrong');
                        if((b.innerText === 'True' && corrects[i]) || (b.innerText === 'False' && !corrects[i])) b.classList.add('correct');
                    });
                }
            }

            if(allCorrect) {
                feedback.innerHTML = "All correct! Well done. 🎉";
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            } else {
                feedback.innerHTML = "Some answers are incorrect. Review the highlights!";
                feedback.className = "feedback-dark wrong";
            }
            feedback.style.display = "block";
        }

        function resetTFGroup_v2(tids, fid) {
            tids.forEach(tid => {
                const row = document.getElementById('tf-row-' + tid);
                row.querySelectorAll('.tf-btn').forEach(b => {
                    b.classList.remove('selected-true', 'selected-false', 'correct', 'wrong', 'disabled');
                });
                delete tf_data_v2[tid];
            });
            const feedback = document.getElementById(fid);
            feedback.style.display = "none";
        }
"""

# Replace the old script section with the new logic
# We'll replace the existing checkDark, selectMCQ, selectTF with script_v2
start_script_replace = "function selectMCQ(qid, selected, correct, successMsg) {"
end_script_replace = "function selectTF(qid, idx, isTrue, isCorrect, feedbackMsg) {"
# Actually let's just find the whole block from checkDark to selectTF end

# We'll just append it to the end for now and remove the old ones if they are in the way
# Or better, replace the specific functions.

# Based on previous view_file:
# 616:         function checkDark(id, correctAns, successMsg) {
# ...
# 688:         }

html = html.replace("        function checkDark(id, correctAns, successMsg) {", "        function checkDark(id, correctAns, successMsg) {") # keep checkDark for scenario

# Let's just remove the buggy ones and add the v2 ones.
html = html.replace("""        function selectMCQ(qid, selected, correct, successMsg) {
            const container = document.getElementById(`mcq-opts-${qid}`);
            const feedback = document.getElementById(`feedback-${qid}`);
            const options = container.getElementsByClassName('mcq-option');
            
            // Disable all options
            for (let opt of options) {
                opt.classList.add('disabled');
                opt.removeAttribute('onclick');
            }

            const selectedOpt = Array.from(options).find(o => o.innerText.trim().startsWith(selected + "."));
            const correctOpt = Array.from(options).find(o => o.innerText.trim().startsWith(correct + "."));

            selectedOpt.classList.add('selected-anim');

            if (selected === correct) {
                selectedOpt.classList.add('correct');
                feedback.innerHTML = "Correct! " + successMsg + " 🎉";
                feedback.className = "feedback-dark correct";
                triggerConfetti();
            } else {
                selectedOpt.classList.add('wrong');
                correctOpt.classList.add('correct');
                feedback.innerHTML = `Incorrect. The correct answer is ${correct}.`;
                feedback.className = "feedback-dark wrong";
            }
        }""", "")

html = html.replace("""        function selectTF(qid, idx, isTrue, isCorrect, feedbackMsg) {
            const row = document.getElementById(`tf-row-${qid}-${idx}`);
            const buttons = row.getElementsByClassName('tf-btn');
            const feedback = document.getElementById(`feedback-${qid}`);
            
            // Disable buttons in this row
            for (let btn of buttons) {
                btn.classList.add('disabled');
                btn.removeAttribute('onclick');
            }

            const selectedBtn = isTrue ? buttons[0] : buttons[1];
            const otherBtn = isTrue ? buttons[1] : buttons[0];

            if (isTrue === isCorrect) {
                selectedBtn.classList.add('correct');
                if (feedbackMsg) {
                    feedback.innerHTML = "Correct! " + feedbackMsg + " 🎉";
                    feedback.className = "feedback-dark correct";
                    triggerConfetti();
                }
            } else {
                selectedBtn.classList.add('wrong');
                otherBtn.classList.add('correct');
                if (feedbackMsg) {
                    feedback.innerHTML = "✗ Not quite. Try again!";
                    feedback.className = "feedback-dark wrong";
                }
            }
        }""", script_v2)

# Fix Scenario feedback mismatch
html = html.replace("checkDark('m2-scenario', 'Transform', 'Correct! Transform handles cleaning and combining.')", "checkDark('m2-scenario', 'Transform', 'Correct! Transform handles cleaning and combining.')")

# Update CSS for selected state in v2
html = html.replace(".mcq-option.selected-anim {", ".mcq-option.selected { border-color: #00d2ff; background: #2d3748; transform: translateX(5px); }\n        .mcq-option.selected-anim {")

# T/F button selected states
tf_css = """
        .tf-btn.selected-true { background: #00d2ff !important; color: white !important; border-color: #00d2ff !important; }
        .tf-btn.selected-false { background: #4b5563 !important; color: white !important; border-color: #4b5563 !important; }
"""
html = html.replace(".tf-btn:hover:not(.disabled) {", tf_css + "\n        .tf-btn:hover:not(.disabled) {")

with open('Data-Module-2.html', 'w', encoding='utf-8') as f:
    f.write(html)
