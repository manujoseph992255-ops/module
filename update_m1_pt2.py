import sys, re

filepath = r"C:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"

html_parts = []

html_parts.append("""
            <h3>3.4 Float</h3>
            <p>A float represents numbers with decimal values. Examples: 2.5, 3.14, 7.8. Float values are used when precision is required (e.g., price, temperature, weight).</p>
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Floats allow more accurate measurements compared to integers.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p><strong>MCQ:</strong> Which value is a float?</p>
                <ol style="margin-left: 20px; color: #9ca3af; list-style-type: upper-alpha;">
                    <li>8</li>
                    <li>12.5</li>
                    <li>-3</li>
                    <li>20</li>
                </ol>
                <div class="practice-dark-box">
                    <input type="text" id="ans-float-mcq" placeholder="Type A, B, C, or D...">
                    <button class="practice-dark-btn" onclick="checkDark('float-mcq', 'B', 'Correct! 12.5 contains a decimal value.')">Submit</button>
                </div>
                <div id="feedback-float-mcq" class="feedback-dark"></div>
                
                <p style="margin-top: 20px;"><strong>True or False:</strong></p>
                <ul style="color: #9ca3af; font-size: 14px; margin-bottom: 10px;">
                    <li>Float numbers contain decimal values. (Type T1)</li>
                    <li>Floats can be used to represent prices. (Type T2)</li>
                </ul>
                <div class="practice-dark-box">
                    <input type="text" id="ans-float-tf" placeholder="e.g. True, True">
                    <button class="practice-dark-btn" onclick="checkDark('float-tf', 'true, true', 'Correct!')">Submit</button>
                </div>
                <div id="feedback-float-tf" class="feedback-dark"></div>
            </div>

            <h3>3.5 Complex Numbers</h3>
            <p>Complex numbers contain a real part and an imaginary part. General form: <code>a + bi</code>. Example: <code>3 + 4i</code>. Python supports complex numbers using the complex data type.</p>
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Complex numbers are mainly used in engineering and scientific calculations.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p><strong>Identify Complex Number:</strong> Which of the following is a complex number?</p>
                <ol style="margin-left: 20px; color: #9ca3af; list-style-type: upper-alpha;">
                    <li>5</li>
                    <li>3.2</li>
                    <li>4 + 2i</li>
                    <li>10</li>
                </ol>
                <div class="practice-dark-box">
                    <input type="text" id="ans-complex-id" placeholder="Type A, B, C, or D...">
                    <button class="practice-dark-btn" onclick="checkDark('complex-id', 'C', 'Correct! 4 + 2i has a real and imaginary part.')">Submit</button>
                </div>
                <div id="feedback-complex-id" class="feedback-dark"></div>
            </div>

            <div class="section-header">
                <h2>3.6 String Data Type</h2>
            </div>
            <p>String data type stores text values. Examples: names, city, product names. Strings can contain letters, numbers, and symbols.</p>
            <pre><span class="comment"># Example:</span>
name = <span class="string">"Anoop"</span></pre>
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Strings help store descriptive information, not numeric calculations.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p>Which of the following is a string? (e.g., 1 and 3)</p>
                <ol style="margin-left: 20px; color: #9ca3af;">
                    <li>"India"</li>
                    <li>25</li>
                    <li>"Laptop"</li>
                    <li>12.5</li>
                </ol>
                <div class="practice-dark-box">
                    <input type="text" id="ans-string-id" placeholder="e.g., 1 and 3">
                    <button class="practice-dark-btn" onclick="checkDark('string-id', '1 and 3', 'Correct! Text surrounded by quotes is a string.')">Submit</button>
                </div>
                <div id="feedback-string-id" class="feedback-dark"></div>
                
                <p style="margin-top: 20px;"><strong>True or False:</strong></p>
                <ul style="color: #9ca3af; font-size: 14px; margin-bottom: 10px;">
                    <li>Strings store text values. (Type T1)</li>
                    <li>Strings can contain numbers as characters. (Type T2)</li>
                </ul>
                <div class="practice-dark-box">
                    <input type="text" id="ans-string-tf" placeholder="e.g. True, True">
                    <button class="practice-dark-btn" onclick="checkDark('string-tf', 'true, true', 'Correct!')">Submit</button>
                </div>
                <div id="feedback-string-tf" class="feedback-dark"></div>
            </div>

            <div class="section-header">
                <h2>4. Data Structures</h2>
            </div>
            <p>Data is often organized using structures such as Tables, Rows, Columns, and Lists. Tables organize structured data.</p>
            <div class="interaction-box">
                <strong>Example Table:</strong>
                <table style="width: 100%; border-collapse: collapse; margin-top: 10px; margin-bottom: 15px;">
                    <tr style="background: #e2e8f0;">
                        <th style="padding: 10px; border: 1px solid #cbd5e1;">Name</th>
                        <th style="padding: 10px; border: 1px solid #cbd5e1;">Age</th>
                        <th style="padding: 10px; border: 1px solid #cbd5e1;">Department</th>
                    </tr>
                    <tr><td style="padding: 10px; border: 1px solid #cbd5e1;">Arjun</td><td style="padding: 10px; border: 1px solid #cbd5e1;">28</td><td style="padding: 10px; border: 1px solid #cbd5e1;">Marketing</td></tr>
                </table>
            </div>
            <ul class="content-list">
                <li><strong>Rows</strong> represent records.</li>
                <li><strong>Columns</strong> represent attributes.</li>
                <li><strong>Lists</strong> store collections of items (e.g., <code>[1,2,3,4,5]</code>).</li>
            </ul>
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Data structures help organize and analyze information efficiently.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p><strong>Drag & Drop Equivalent: Match the concept.</strong></p>
                <div class="dd-container">
                    <div class="dd-row">
                        <div class="dd-label">Single record &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-struct-1">
                                <option value="">Select Concept...</option>
                                <option value="row">Row</option>
                                <option value="column">Column</option>
                                <option value="table">Table</option>
                            </select>
                        </div>
                    </div>
                    <div class="dd-row">
                        <div class="dd-label">Attribute &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-struct-2">
                                <option value="">Select Concept...</option>
                                <option value="row">Row</option>
                                <option value="column">Column</option>
                                <option value="table">Table</option>
                            </select>
                        </div>
                    </div>
                    <div class="dd-row">
                        <div class="dd-label">Organized dataset &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-struct-3">
                                <option value="">Select Concept...</option>
                                <option value="row">Row</option>
                                <option value="column">Column</option>
                                <option value="table">Table</option>
                            </select>
                        </div>
                    </div>
                    <button class="practice-dark-btn" style="margin-top: 10px;" onclick="checkDDStruct()">Check Matches</button>
                </div>
                <div id="feedback-struct-dd" class="feedback-dark"></div>
            </div>

            <div class="section-header">
                <h2>5. Types of Data</h2>
            </div>
            <p>Data can be classified into two main types: <strong>Qualitative data</strong> and <strong>Quantitative data</strong>.</p>

            <h3>5.1 Qualitative Data</h3>
            <p>Qualitative data describes categories or characteristics. Examples: gender, city, brand. Types include Nominal and Ordinal.</p>
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Qualitative data focuses on descriptions rather than numbers.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p><strong>MCQ:</strong> Which of the following is qualitative data?</p>
                <ol style="margin-left: 20px; color: #9ca3af; list-style-type: upper-alpha;">
                    <li>Salary</li>
                    <li>Height</li>
                    <li>Eye color</li>
                    <li>Age</li>
                </ol>
                <div class="practice-dark-box">
                    <input type="text" id="ans-qual-mcq" placeholder="Type A, B, C, or D...">
                    <button class="practice-dark-btn" onclick="checkDark('qual-mcq', 'C', 'Correct! Eye color is a category or characteristic.')">Submit</button>
                </div>
                <div id="feedback-qual-mcq" class="feedback-dark"></div>
            </div>

            <h3>5.2 Quantitative Data</h3>
            <p>Quantitative data represents numeric values. Examples: height, weight, marks, distance.</p>
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Quantitative data allows statistical calculations.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p>Which of these are quantitative? 1. Age, 2. Weight, 3. Country, 4. Temperature (e.g., 1, 2, 4)</p>
                <div class="practice-dark-box">
                    <input type="text" id="ans-quant-id" placeholder="e.g., 1, 2, 4">
                    <button class="practice-dark-btn" onclick="checkDark('quant-id', '1, 2, 4', 'Correct! These are all numeric values.')">Submit</button>
                </div>
                <div id="feedback-quant-id" class="feedback-dark"></div>
            </div>
""")

html_parts.append("""
            <div class="section-header">
                <h2>6. Structured vs Unstructured Data</h2>
            </div>
            <h3>Structured Data</h3>
            <p>Structured data fits into rows and columns and is typically stored in databases or spreadsheets. Examples: phone numbers, bank records.</p>
            
            <h3>Unstructured Data</h3>
            <p>Unstructured data has no fixed format. Examples: emails, videos, social media posts.</p>
            
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Most modern data generated online is unstructured.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p><strong>Classification Activity:</strong> Classify the following.</p>
                <div class="dd-container">
                    <div class="dd-row">
                        <div class="dd-label">Excel table &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-structtype-1">
                                <option value="">Select Type...</option>
                                <option value="structured">Structured</option>
                                <option value="unstructured">Unstructured</option>
                            </select>
                        </div>
                    </div>
                    <div class="dd-row">
                        <div class="dd-label">Email message &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-structtype-2">
                                <option value="">Select Type...</option>
                                <option value="structured">Structured</option>
                                <option value="unstructured">Unstructured</option>
                            </select>
                        </div>
                    </div>
                    <div class="dd-row">
                        <div class="dd-label">Database records &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-structtype-3">
                                <option value="">Select Type...</option>
                                <option value="structured">Structured</option>
                                <option value="unstructured">Unstructured</option>
                            </select>
                        </div>
                    </div>
                    <div class="dd-row">
                        <div class="dd-label">Video file &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-structtype-4">
                                <option value="">Select Type...</option>
                                <option value="structured">Structured</option>
                                <option value="unstructured">Unstructured</option>
                            </select>
                        </div>
                    </div>
                    <button class="practice-dark-btn" style="margin-top: 10px;" onclick="checkDDStructType()">Check Matches</button>
                </div>
                <div id="feedback-structtype-dd" class="feedback-dark"></div>
            </div>

            <div class="section-header">
                <h2>7. Metadata</h2>
            </div>
            <h3>Concept</h3>
            <p><strong>Metadata</strong> means data about data. It describes information such as file size, creation date, author, format.</p>
            
            <div class="interaction-box">
                <strong>Example:</strong>
                <p>A photo file may include metadata: camera type, date taken, resolution.</p>
            </div>
            
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Metadata helps organize and manage data efficiently.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p><strong>True or False:</strong></p>
                <ul style="color: #9ca3af; font-size: 14px; margin-bottom: 10px;">
                    <li>Metadata describes other data. (Type T1)</li>
                    <li>Metadata includes file information. (Type T2)</li>
                    <li>Metadata replaces the original data. (Type F3)</li>
                </ul>
                <div class="practice-dark-box">
                    <input type="text" id="ans-meta-tf" placeholder="e.g. True, True, False">
                    <button class="practice-dark-btn" onclick="checkDark('meta-tf', 'true, true, false', 'Correct! Excellent job.')">Submit</button>
                </div>
                <div id="feedback-meta-tf" class="feedback-dark"></div>
            </div>

            <div class="section-header">
                <h2>8. Big Data</h2>
            </div>
            <h3>Concept</h3>
            <p><strong>Big Data</strong> refers to extremely large and complex datasets that grow rapidly and cannot be processed using traditional systems. Sources of big data include social media, online transactions, sensors, and IoT devices.</p>
            
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Big data allows organizations to analyze massive amounts of information to discover patterns and predictions.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p><strong>MCQ:</strong> Big data is characterized by:</p>
                <ol style="margin-left: 20px; color: #9ca3af; list-style-type: upper-alpha;">
                    <li>Small datasets</li>
                    <li>Extremely large and complex datasets</li>
                    <li>Only numerical data</li>
                    <li>Only structured data</li>
                </ol>
                <div class="practice-dark-box">
                    <input type="text" id="ans-bigdata-mcq" placeholder="Type A, B, C, or D...">
                    <button class="practice-dark-btn" onclick="checkDark('bigdata-mcq', 'B', 'Correct! Welcome to Big Data.')">Submit</button>
                </div>
                <div id="feedback-bigdata-mcq" class="feedback-dark"></div>
            </div>
""")

with open('update_m1_script_pt2.py', 'w') as f:
    f.write("html_parts = []\n")
    for part in html_parts:
        f.write(f"html_parts.append({repr(part)})\n")
