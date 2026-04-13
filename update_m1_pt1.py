import sys

html_content = """
            <div class="section-header">
                <h2>1. Meaning of Data</h2>
                <p style="font-weight: 600; color: var(--secondary-blue);">Foundational Definitions</p>
            </div>
            
            <h3>Concept</h3>
            <p><strong>Data</strong> refers to raw facts, figures, or observations collected for analysis or reference. Data can appear in many forms such as:</p>
            <ul class="content-list">
                <li>Numbers</li>
                <li>Text</li>
                <li>Images</li>
                <li>Audio</li>
            </ul>
            <p>By itself, data does not carry meaning until it is processed and interpreted.</p>
            
            <div class="interaction-box">
                <strong>Example Raw Data:</strong>
                <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background: #e2e8f0;">
                        <th style="padding: 10px; border: 1px solid #cbd5e1;">Product</th>
                        <th style="padding: 10px; border: 1px solid #cbd5e1;">Sales</th>
                    </tr>
                    <tr><td style="padding: 10px; border: 1px solid #cbd5e1;">Laptop</td><td style="padding: 10px; border: 1px solid #cbd5e1;">15</td></tr>
                    <tr><td style="padding: 10px; border: 1px solid #cbd5e1;">Tablet</td><td style="padding: 10px; border: 1px solid #cbd5e1;">8</td></tr>
                    <tr><td style="padding: 10px; border: 1px solid #cbd5e1;">Phone</td><td style="padding: 10px; border: 1px solid #cbd5e1;">20</td></tr>
                </table>
                <p style="margin-top: 15px;">After analysis we might discover: <strong>Phone is the best-selling product.</strong> That insight becomes useful information.</p>
            </div>

            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Data is like ingredients in cooking. Ingredients alone do not create a meal. Only after processing and combining them do we get something meaningful.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p>Which of the following best describes data?</p>
                <div class="practice-dark-box">
                    <input type="text" id="ans-meaning-mcq" placeholder="Type A, B, C, or D...">
                    <button class="practice-dark-btn" onclick="checkDark('meaning-mcq', 'B', 'Correct! Data is raw facts collected for analysis.')">Submit</button>
                </div>
                <div id="feedback-meaning-mcq" class="feedback-dark"></div>

                <p style="margin-top: 20px;"><strong>True or False:</strong></p>
                <ul style="color: #9ca3af; font-size: 14px; margin-bottom: 10px;">
                    <li>Data always has meaning by itself. (Type F1)</li>
                    <li>Data can include text and images. (Type T2)</li>
                    <li>Data becomes useful after analysis. (Type T3)</li>
                </ul>
                <div class="practice-dark-box">
                    <input type="text" id="ans-meaning-tf" placeholder="e.g. False, True, True">
                    <button class="practice-dark-btn" onclick="checkDark('meaning-tf', 'false, true, true', 'Correct! All true.')">Submit</button>
                </div>
                <div id="feedback-meaning-tf" class="feedback-dark"></div>
            </div>

            <div class="practice-space-dark">
                <h3>Scenario Question</h3>
                <p>A school collects: Student marks, Attendance, and Assignment scores. Explain one insight the school could get after analyzing this data.</p>
                <div class="practice-dark-box">
                    <input type="text" id="ans-scenario" placeholder="Your answer...">
                    <button class="practice-dark-btn" onclick="checkDark('scenario', 'insight', 'Great! For example, identifying struggling students or tracking overall attendance patterns.')">Submit</button>
                </div>
                <div id="feedback-scenario" class="feedback-dark"></div>
            </div>

            <div class="section-header">
                <h2>2. Data Analysis</h2>
            </div>
            <h3>Concept</h3>
            <p><strong>Data Analysis</strong> is the process of converting raw data into useful information for decision making. Organizations use data analysis to:</p>
            <ul class="content-list">
                <li>Understand trends</li>
                <li>Identify patterns</li>
                <li>Support decisions</li>
            </ul>
            
            <div class="interaction-box">
                <strong>Example:</strong>
                <p>A company records daily sales.</p>
                <table style="width: 100%; border-collapse: collapse; margin-top: 10px; margin-bottom: 15px;">
                    <tr style="background: #e2e8f0;">
                        <th style="padding: 10px; border: 1px solid #cbd5e1;">Day</th>
                        <th style="padding: 10px; border: 1px solid #cbd5e1;">Sales</th>
                    </tr>
                    <tr><td style="padding: 10px; border: 1px solid #cbd5e1;">Monday</td><td style="padding: 10px; border: 1px solid #cbd5e1;">5000</td></tr>
                    <tr><td style="padding: 10px; border: 1px solid #cbd5e1;">Tuesday</td><td style="padding: 10px; border: 1px solid #cbd5e1;">6200</td></tr>
                    <tr><td style="padding: 10px; border: 1px solid #cbd5e1;">Wednesday</td><td style="padding: 10px; border: 1px solid #cbd5e1;">7100</td></tr>
                </table>
                <p>After analysis they may conclude: <strong>Sales increase mid-week.</strong></p>
            </div>

            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Data analysis answers questions like: What happened? Why did it happen? What might happen next?</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p><strong>Drag & Drop Equivalent: Match the Purpose</strong></p>
                <p>Match the data collected with the possible insight:</p>
                <div class="dd-container">
                    <div class="dd-row">
                        <div class="dd-label">Website visitors &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-analysis-1">
                                <option value="">Select Insight...</option>
                                <option value="avg">Class average</option>
                                <option value="pop">Most popular page</option>
                                <option value="best">Best selling product</option>
                            </select>
                        </div>
                    </div>
                    <div class="dd-row">
                        <div class="dd-label">Student marks &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-analysis-2">
                                <option value="">Select Insight...</option>
                                <option value="avg">Class average</option>
                                <option value="pop">Most popular page</option>
                                <option value="best">Best selling product</option>
                            </select>
                        </div>
                    </div>
                    <div class="dd-row">
                        <div class="dd-label">Sales records &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-analysis-3">
                                <option value="">Select Insight...</option>
                                <option value="avg">Class average</option>
                                <option value="pop">Most popular page</option>
                                <option value="best">Best selling product</option>
                            </select>
                        </div>
                    </div>
                    <button class="practice-dark-btn" style="margin-top: 10px;" onclick="checkDDAnalysis()">Check Matches</button>
                </div>
                <div id="feedback-analysis-dd" class="feedback-dark"></div>

                <p style="margin-top: 20px;"><strong>MCQ:</strong> A dataset is:</p>
                <div class="practice-dark-box">
                    <input type="text" id="ans-dataset-mcq" placeholder="Type A, B, C, or D...">
                    <button class="practice-dark-btn" onclick="checkDark('dataset-mcq', 'A', 'Correct! A dataset is a collection of organized data.')">Submit</button>
                </div>
                <div id="feedback-dataset-mcq" class="feedback-dark"></div>
                
                <p style="margin-top: 20px;"><strong>Mini Thinking Question:</strong> A restaurant collects daily customer feedback ratings. What decision could the restaurant make after analyzing this data?</p>
                <div class="practice-dark-box">
                    <input type="text" id="ans-mini-thinking" placeholder="Your answer...">
                    <button class="practice-dark-btn" onclick="checkDark('mini-thinking', 'menu', 'Excellent! They could improve their menu, change staff behavior, etc.')">Submit</button>
                </div>
                <div id="feedback-mini-thinking" class="feedback-dark"></div>
            </div>

            <div class="section-header">
                <h2>3. Data Variable Types</h2>
            </div>
            <h3>Concept</h3>
            <p>Variables describe the type of value stored in data. Main variable types include <strong>Boolean, Numeric, and String</strong>. Each type stores different kinds of values.</p>
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Understanding variable types helps store data correctly, analyze data efficiently, and avoid calculation errors.</p>
            </div>

            <h3>3.1 Boolean Data Type</h3>
            <p>Boolean data type stores two possible values: <strong>True</strong> or <strong>False</strong>. Booleans are commonly used in logical conditions and decision making.</p>
            <pre><span class="comment"># Example:</span>
is_logged_in = <span class="keyword">True</span>
<span class="keyword">if</span> is_logged_in:
    <span class="function">print</span>(<span class="string">"Access granted"</span>)</pre>
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Boolean variables act like switches: ON = True, OFF = False.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p>Which of the following can be Boolean? (e.g., 1 and 3)</p>
                <ol style="margin-left: 20px; color: #9ca3af;">
                    <li>Student passed exam</li>
                    <li>Number of books</li>
                    <li>Payment successful</li>
                    <li>Temperature</li>
                </ol>
                <div class="practice-dark-box">
                    <input type="text" id="ans-bool-id" placeholder="e.g., 1 and 3">
                    <button class="practice-dark-btn" onclick="checkDark('bool-id', '1 and 3', 'Correct! These are Yes/No states.')">Submit</button>
                </div>
                <div id="feedback-bool-id" class="feedback-dark"></div>
                
                <p style="margin-top: 20px;"><strong>True or False:</strong></p>
                <ul style="color: #9ca3af; font-size: 14px; margin-bottom: 10px;">
                    <li>Boolean variables store True or False. (Type T1)</li>
                    <li>Boolean values can be used in conditions. (Type T2)</li>
                    <li>Boolean values represent multiple numbers. (Type F3)</li>
                </ul>
                <div class="practice-dark-box">
                    <input type="text" id="ans-bool-tf" placeholder="e.g. True, True, False">
                    <button class="practice-dark-btn" onclick="checkDark('bool-tf', 'true, true, false', 'Correct! Great job.')">Submit</button>
                </div>
                <div id="feedback-bool-tf" class="feedback-dark"></div>
            </div>
            
            <h3>3.2 Numeric Data Type</h3>
            <p>Numeric data types represent numbers that can be calculated mathematically. Examples: exam marks, salary, weight, height. Numeric types include Integer, Float, Complex.</p>
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Numeric data allows operations such as addition, subtraction, multiplication, and division.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p><strong>MCQ:</strong> Which of the following is numeric data?</p>
                <div class="practice-dark-box">
                    <input type="text" id="ans-numeric-mcq" placeholder="Type A, B, C, or D...">
                    <button class="practice-dark-btn" onclick="checkDark('numeric-mcq', 'A', 'Correct! Age is numeric data.')">Submit</button>
                </div>
                <div id="feedback-numeric-mcq" class="feedback-dark"></div>
                
                <p style="margin-top: 20px;"><strong>Classification: Match example with numeric type.</strong></p>
                <div class="dd-container">
                    <div class="dd-row">
                        <div class="dd-label">25 &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-num-1">
                                <option value="">Select Type...</option>
                                <option value="integer">Integer</option>
                                <option value="float">Float</option>
                            </select>
                        </div>
                    </div>
                    <div class="dd-row">
                        <div class="dd-label">12.75 &rarr;</div>
                        <div class="dd-target">
                            <select id="dd-num-2">
                                <option value="">Select Type...</option>
                                <option value="integer">Integer</option>
                                <option value="float">Float</option>
                            </select>
                        </div>
                    </div>
                    <button class="practice-dark-btn" style="margin-top: 10px;" onclick="checkDDNum()">Check Matches</button>
                </div>
                <div id="feedback-num-dd" class="feedback-dark"></div>
            </div>

            <h3>3.3 Integer</h3>
            <p>An integer is a whole number without decimal values. Examples: 5, 10, -3, 0. Integers represent quantities like number of students or products sold.</p>
            <div class="interaction-box" style="background: rgba(0, 210, 255, 0.05); border-left-color: #00d2ff;">
                <strong>Insight:</strong>
                <p>Integers are useful when exact counts are needed.</p>
            </div>

            <div class="practice-space-dark">
                <h3>Practice Activities</h3>
                <p>Which of these are integers? 15, 4.8, -10, 0 (e.g., 1, 3, 4)</p>
                <div class="practice-dark-box">
                    <input type="text" id="ans-int-id" placeholder="e.g., 1, 3, 4">
                    <button class="practice-dark-btn" onclick="checkDark('int-id', '1, 3, 4', 'Correct! Those are whole numbers.')">Submit</button>
                </div>
                <div id="feedback-int-id" class="feedback-dark"></div>
                
                <p style="margin-top: 20px;"><strong>True or False:</strong></p>
                <ul style="color: #9ca3af; font-size: 14px; margin-bottom: 10px;">
                    <li>Integers can have decimal points. (Type F1)</li>
                    <li>Integers can be negative numbers. (Type T2)</li>
                </ul>
                <div class="practice-dark-box">
                    <input type="text" id="ans-int-tf" placeholder="e.g. False, True">
                    <button class="practice-dark-btn" onclick="checkDark('int-tf', 'false, true', 'Correct!')">Submit</button>
                </div>
                <div id="feedback-int-tf" class="feedback-dark"></div>
            </div>
"""
import os

filepath = r"C:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"
with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

import re
# We want to replace <main class="main-content"> ... upto closing tag <div class="quiz-cta">, no 
# we'll replace the full <main> content.
# But there isn't enough memory in my string for all sections, I'll build it.
