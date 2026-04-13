import re

html_content = """
            <div class="section-header">
                <h2>1. Data Visualization</h2>
            </div>
            <h3>Concept</h3>
            <p><strong>Data visualization</strong> is the process of representing data using visual elements such as:</p>
            <ul>
                <li>charts</li>
                <li>graphs</li>
                <li>dashboards</li>
            </ul>
            <p>It helps transform complex data into easy-to-understand visuals.</p>

            <div class="interaction-box">
                <strong>Example:</strong>
                <p>Instead of showing a table of sales numbers, a bar chart can quickly show:</p>
                <ul>
                    <li>which product sells the most</li>
                    <li>which region performs better</li>
                </ul>
            </div>

            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>Humans understand visuals faster than numbers.<br>Visualization helps in quick decision-making and better communication.</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <h4>Knowledge Check</h4>
                <p>What is the main purpose of data visualization?</p>
                <div class="mcq-options" id="mcq-m4-1">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-1')"><span class="mcq-prefix">A.</span> Store data</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-1')"><span class="mcq-prefix">B.</span> Make data easier to understand</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-1')"><span class="mcq-prefix">C.</span> Delete data</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-1')"><span class="mcq-prefix">D.</span> Collect data</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m4-1', 'B', 'Correct! Visuals simplify interpretation.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m4-1"></div>

                <p style="margin-top: 30px;"><strong>True / False:</strong></p>
                <div class="tf-row" id="tf-row-m4-1"><span class="tf-statement">Data visualization helps in faster understanding of data.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_v2(this, 'm4-1', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'm4-1', false)">False</button></div></div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkTFGroup_v2(['m4-1'], [true], 'feedback-tf-m4-1')">Check Answer</button>
                <div class="feedback-dark" id="feedback-tf-m4-1"></div>
            </div>

            <div class="section-header">
                <h2>2. Reporting Data Effectively</h2>
            </div>
            <h3>Concept</h3>
            <p><strong>Data reporting</strong> involves presenting data in a structured format so that stakeholders can understand it easily.</p>
            <p>Common reporting formats:</p>
            <ul>
                <li>tables</li>
                <li>dashboards</li>
                <li>charts</li>
            </ul>
            <p>Good reporting should:</p>
            <ul>
                <li>be clear</li>
                <li>be simple</li>
                <li>highlight key insights</li>
            </ul>

            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>A good report does not just show data &mdash; it tells a story.</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which of the following is used to present data effectively?</p>
                <div class="mcq-options" id="mcq-m4-2">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-2')"><span class="mcq-prefix">A.</span> Raw data only</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-2')"><span class="mcq-prefix">B.</span> Tables and charts</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-2')"><span class="mcq-prefix">C.</span> Programming code</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-2')"><span class="mcq-prefix">D.</span> Logs</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m4-2', 'B', 'Exactly! Structured visuals are essential.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m4-2"></div>
            </div>

            <div class="section-header">
                <h2>3. Types of Data Visualization</h2>
            </div>
            <p>Different visualizations are used for different purposes.</p>

            <h3>3.1 Comparison Charts</h3>
            <h3>Concept</h3>
            <p>Used to compare values between categories.</p>
            <p>Examples:</p>
            <ul>
                <li>bar chart</li>
                <li>column chart</li>
            </ul>
            
            <div class="interaction-box">
                <strong>Example:</strong>
                <p>Compare sales of different products.</p>
            </div>
            <div class="interaction-box" style="border-left-color: #f59e0b; background: #fffbeb;">
                <strong>Insight:</strong> Use comparison charts when you want to answer:<br><strong>"Which is higher or lower?"</strong>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which chart is best for comparing categories?</p>
                <div class="mcq-options" id="mcq-m4-31">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-31')"><span class="mcq-prefix">A.</span> Pie chart</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-31')"><span class="mcq-prefix">B.</span> Bar chart</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-31')"><span class="mcq-prefix">C.</span> Histogram</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-31')"><span class="mcq-prefix">D.</span> Scatter plot</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m4-31', 'B', 'Correct!')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m4-31"></div>
            </div>

            <h3>3.2 Trend Charts</h3>
            <h3>Concept</h3>
            <p>Used to show changes over time.</p>
            <p>Example: line chart</p>
            <div class="interaction-box">
                <strong>Example:</strong> Monthly sales growth.
            </div>
            <div class="interaction-box" style="border-left-color: #f59e0b; background: #fffbeb;">
                <strong>Insight:</strong> Trend charts answer:<br><strong>"How data changes over time?"</strong>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which chart is best for showing trends?</p>
                <div class="mcq-options" id="mcq-m4-32">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-32')"><span class="mcq-prefix">A.</span> Pie chart</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-32')"><span class="mcq-prefix">B.</span> Line chart</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-32')"><span class="mcq-prefix">C.</span> Bar chart</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-32')"><span class="mcq-prefix">D.</span> Table</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m4-32', 'B', 'Correct!')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m4-32"></div>
            </div>

            <h3>3.3 Distribution Charts</h3>
            <h3>Concept</h3>
            <p>Used to show how data is spread across values.</p>
            <p>Example: histogram</p>
            <div class="interaction-box" style="border-left-color: #f59e0b; background: #fffbeb;">
                <strong>Insight:</strong> Distribution helps identify:<br>
                <ul>
                    <li>patterns</li>
                    <li>outliers</li>
                    <li>spread of data</li>
                </ul>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which chart shows data distribution?</p>
                <div class="mcq-options" id="mcq-m4-33">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-33')"><span class="mcq-prefix">A.</span> Histogram</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-33')"><span class="mcq-prefix">B.</span> Pie chart</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-33')"><span class="mcq-prefix">C.</span> Line chart</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-33')"><span class="mcq-prefix">D.</span> Table</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m4-33', 'A', 'Correct!')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m4-33"></div>
            </div>

            <h3>3.4 Correlation Charts</h3>
            <h3>Concept</h3>
            <p>Used to show relationship between two variables.</p>
            <p>Example: scatter plot</p>
            
            <div class="interaction-box">
                <strong>Example:</strong>
                <p>Relationship between:</p>
                <ul>
                    <li>advertising spend</li>
                    <li>sales</li>
                </ul>
            </div>
            <div class="interaction-box" style="border-left-color: #f59e0b; background: #fffbeb;">
                <strong>Insight:</strong> Correlation does not always mean causation.
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which chart shows relationship between variables?</p>
                <div class="mcq-options" id="mcq-m4-34">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-34')"><span class="mcq-prefix">A.</span> Scatter plot</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-34')"><span class="mcq-prefix">B.</span> Pie chart</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-34')"><span class="mcq-prefix">C.</span> Bar chart</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-34')"><span class="mcq-prefix">D.</span> Histogram</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m4-34', 'A', 'Correct!')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m4-34"></div>
            </div>

            <div class="section-header">
                <h2>4. Interpreting Data Visualizations</h2>
            </div>
            <h3>Concept</h3>
            <p>Interpreting visualization means understanding what the data is telling us.</p>
            <p>It involves:</p>
            <ul>
                <li>identifying trends</li>
                <li>comparing values</li>
                <li>spotting patterns</li>
            </ul>
            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong> A chart is useful only if you can <strong>interpret it correctly</strong>.
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p><strong>True / False</strong></p>
                <div class="tf-row" id="tf-row-m4-int"><span class="tf-statement">A chart can be misleading if not interpreted properly.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_v2(this, 'm4-int', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'm4-int', false)">False</button></div></div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkTFGroup_v2(['m4-int'], [true], 'feedback-tf-m4-int')">Verify</button>
                <div class="feedback-dark" id="feedback-tf-m4-int"></div>
            </div>

            <div class="section-header">
                <h2>5. Avoiding Misinterpretation and Bias</h2>
            </div>
            <h3>Concept</h3>
            <p>Visualizations can sometimes be misleading due to:</p>
            <ul>
                <li>incorrect scaling</li>
                <li>missing data</li>
                <li>exaggerated differences</li>
            </ul>
            
            <p>Types of bias include:</p>
            <ul>
                <li>visual bias</li>
                <li>sampling bias</li>
                <li>misleading axes</li>
            </ul>

            <div class="interaction-box" style="border-left-color: #ef4444; background: #fef2f2;">
                <strong>Insight:</strong>
                <p>Always check:</p>
                <ul>
                    <li>axis scale</li>
                    <li>labels</li>
                    <li>data source</li>
                </ul>
                <p>before trusting a visualization.</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which of the following can make a chart misleading?</p>
                <div class="mcq-options" id="mcq-m4-bias">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-bias')"><span class="mcq-prefix">A.</span> Correct labeling</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-bias')"><span class="mcq-prefix">B.</span> Proper scaling</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-bias')"><span class="mcq-prefix">C.</span> Manipulated axis scale</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-bias')"><span class="mcq-prefix">D.</span> Clear data</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m4-bias', 'C', 'Correct! Manipulating the scale is a common way to distort data.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m4-bias"></div>

                <p style="margin-top: 30px;"><strong>True / False</strong></p>
                <div class="tf-row" id="tf-row-m4-bias-tf"><span class="tf-statement">Changing the axis scale can distort interpretation of data.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_v2(this, 'm4-bias-tf', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'm4-bias-tf', false)">False</button></div></div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkTFGroup_v2(['m4-bias-tf'], [true], 'feedback-tf-m4-bias')">Check Answer</button>
                <div class="feedback-dark" id="feedback-tf-m4-bias"></div>
            </div>

            <div class="section-header">
                <h2>6. Communicating Insights</h2>
            </div>
            <h3>Concept</h3>
            <p>Communication of data means explaining findings clearly to others.</p>
            
            <p>Good communication includes:</p>
            <ul>
                <li>simple language</li>
                <li>clear visuals</li>
                <li>meaningful insights</li>
            </ul>

            <div class="interaction-box">
                <strong>Example:</strong>
                <p>Instead of saying: <i>"Sales increased"</i></p>
                <p>Say: <strong>"Sales increased by 20% compared to last quarter"</strong></p>
            </div>

            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong> Data is valuable only when it is understood and communicated effectively.
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which is the best way to communicate insights?</p>
                <div class="mcq-options" id="mcq-m4-comm">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-comm')"><span class="mcq-prefix">A.</span> Show raw data only</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-comm')"><span class="mcq-prefix">B.</span> Use clear visuals and explanations</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-comm')"><span class="mcq-prefix">C.</span> Use complex language</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m4-comm')"><span class="mcq-prefix">D.</span> Hide key information</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m4-comm', 'B', 'Exactly! Clarity is the goal of communication.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m4-comm"></div>
            </div>

            <div class="quiz-cta">
                <h3>Visualization Mastery Complete!</h3>
                <p>You've learned how to turn raw data into powerful visuals and impactful reports.</p>
                <a href="module_quiz.html?mod=data4" class="btn-start-quiz">Start Final Assessment &rarr;</a>
            </div>
"""

with open('Data-Module-4.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<main class="main-content">.*?</main>', f'<main class="main-content">{html_content}</main>', text, flags=re.DOTALL)

with open('Data-Module-4.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Data-Module-4.html updated successfully.")
