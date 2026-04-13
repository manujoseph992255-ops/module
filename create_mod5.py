import re

html_content = """
            <div class="section-header">
                <h2>1. Responsible Data Analytics</h2>
            </div>
            <h3>Concept</h3>
            <p><strong>Responsible analytics</strong> refers to the practice of handling data ethically, securely, and legally during collection, analysis, and reporting.</p>
            <p>It ensures that data is:</p>
            <ul>
                <li>used properly</li>
                <li>protected from misuse</li>
                <li>interpreted fairly</li>
            </ul>

            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>Just because you can use data does not mean you should use it without responsibility.</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <h4>Knowledge Check</h4>
                <p>Responsible analytics mainly focuses on:</p>
                <div class="mcq-options" id="mcq-m5-1">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-1')"><span class="mcq-prefix">A.</span> Increasing data size</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-1')"><span class="mcq-prefix">B.</span> Ethical and secure use of data</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-1')"><span class="mcq-prefix">C.</span> Data visualization</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-1')"><span class="mcq-prefix">D.</span> Data storage only</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m5-1', 'B', 'Correct! Responsibility covers ethics and security.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m5-1"></div>

                <p style="margin-top: 30px;"><strong>True / False:</strong></p>
                <div class="tf-row" id="tf-row-m5-1"><span class="tf-statement">Responsible analytics ensures data is used ethically.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_v2(this, 'm5-1', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'm5-1', false)">False</button></div></div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkTFGroup_v2(['m5-1'], [true], 'feedback-tf-m5-1')">Check Answer</button>
                <div class="feedback-dark" id="feedback-tf-m5-1"></div>
            </div>

            <div class="section-header">
                <h2>2. Data Privacy Laws</h2>
            </div>
            <h3>Concept</h3>
            <p>Organizations must follow data privacy laws to protect user information.</p>
            <p>Some important laws include:</p>
            <ul>
                <li><strong>GDPR</strong> (General Data Protection Regulation)</li>
                <li><strong>FERPA</strong> (Education data protection)</li>
                <li><strong>HIPAA</strong> (Health data protection)</li>
                <li><strong>PCI</strong> (Payment card data security)</li>
            </ul>
            <p>These laws regulate:</p>
            <ul>
                <li>how data is collected</li>
                <li>how data is stored</li>
                <li>how data is shared</li>
            </ul>

            <div class="interaction-box" style="border-left-color: #ef4444; background: #fef2f2;">
                <strong>Insight:</strong>
                <p>Violating data privacy laws can lead to:</p>
                <ul>
                    <li>legal penalties</li>
                    <li>loss of customer trust</li>
                </ul>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which of the following is a data privacy regulation?</p>
                <div class="mcq-options" id="mcq-m5-2">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-2')"><span class="mcq-prefix">A.</span> JSON</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-2')"><span class="mcq-prefix">B.</span> GDPR</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-2')"><span class="mcq-prefix">C.</span> CSV</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-2')"><span class="mcq-prefix">D.</span> SQL</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m5-2', 'B', 'Exactly! GDPR protects general privacy.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m5-2"></div>

                <p style="margin-top: 30px;"><strong>True / False:</strong></p>
                <div class="tf-row" id="tf-row-m5-2"><span class="tf-statement">Data privacy laws protect personal information.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_v2(this, 'm5-2', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'm5-2', false)">False</button></div></div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkTFGroup_v2(['m5-2'], [true], 'feedback-tf-m5-2')">Check Answer</button>
                <div class="feedback-dark" id="feedback-tf-m5-2"></div>
            </div>

            <div class="section-header">
                <h2>3. Personally Identifiable Information (PII)</h2>
            </div>
            <h3>Concept</h3>
            <p><strong>PII</strong> refers to any information that can identify an individual.</p>
            <p>Examples:</p>
            <ul>
                <li>name</li>
                <li>phone number</li>
                <li>email address</li>
                <li>Aadhaar number</li>
            </ul>
            <p>Organizations must protect PII to prevent misuse.</p>

            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong>
                <p>PII is sensitive and must be:</p>
                <ul>
                    <li>secured</li>
                    <li>anonymized when needed</li>
                </ul>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which of the following is PII? (Select all that apply)</p>
                <div class="mcq-options" id="mcq-m5-3">
                    <div class="mcq-option" onclick="this.classList.toggle('selected')"><span class="mcq-prefix">1.</span> Customer name</div>
                    <div class="mcq-option" onclick="this.classList.toggle('selected')"><span class="mcq-prefix">2.</span> Product price</div>
                    <div class="mcq-option" onclick="this.classList.toggle('selected')"><span class="mcq-prefix">3.</span> Email address</div>
                    <div class="mcq-option" onclick="this.classList.toggle('selected')"><span class="mcq-prefix">4.</span> Sales total</div>
                </div>
                <button class="practice-dark-btn" onclick="
                    let selected = Array.from(document.getElementById('mcq-m5-3').querySelectorAll('.selected')).map(el => el.querySelector('.mcq-prefix').innerText[0]);
                    let fb = document.getElementById('feedback-mcq-m5-3');
                    fb.style.display = 'block';
                    if(selected.includes('1') && selected.includes('3') && selected.length === 2) {
                        fb.className = 'feedback-dark correct'; fb.innerText = 'Correct! Name and Email are PII.'; triggerConfetti();
                        document.getElementById('mcq-m5-3').querySelectorAll('.selected').forEach(el => el.classList.add('correct'));
                    } else {
                        fb.className = 'feedback-dark wrong'; fb.innerText = 'Incorrect. Think about what can identify a person.';
                    }
                ">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m5-3"></div>
            </div>

            <div class="section-header">
                <h2>4. Data Security</h2>
            </div>
            <h3>Concept</h3>
            <p>Data security involves protecting data from:</p>
            <ul>
                <li>unauthorized access</li>
                <li>breaches</li>
                <li>loss</li>
            </ul>
            <p>Methods include:</p>
            <ul>
                <li>encryption</li>
                <li>access control</li>
                <li>secure storage</li>
            </ul>

            <div class="interaction-box" style="border-left-color: #ef4444; background: #fef2f2;">
                <strong>Insight:</strong>
                <p>Without security, data can be stolen, misused, or leaked.</p>
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which of the following helps protect data?</p>
                <div class="mcq-options" id="mcq-m5-4">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-4')"><span class="mcq-prefix">A.</span> Deleting data</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-4')"><span class="mcq-prefix">B.</span> Encryption</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-4')"><span class="mcq-prefix">C.</span> Visualization</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-4')"><span class="mcq-prefix">D.</span> Sorting</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m5-4', 'B', 'Correct! Encryption protects data from unauthorized access.')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m5-4"></div>
            </div>

            <div class="section-header">
                <h2>5. Data Anonymization</h2>
            </div>
            <h3>Concept</h3>
            <p>Anonymization means removing personal identifiers from data so individuals cannot be identified.</p>
            <div class="interaction-box">
                <strong>Example:</strong>
                <p>Instead of: <i>Name: Anoop</i></p>
                <p>Use: <strong>User ID: 101</strong></p>
            </div>
            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong> Anonymization allows data to be used for analysis without compromising privacy.
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <div class="tf-row" id="tf-row-m5-5"><span class="tf-statement">Anonymization removes personal identity from data.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_v2(this, 'm5-5', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'm5-5', false)">False</button></div></div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkTFGroup_v2(['m5-5'], [true], 'feedback-tf-m5-5')">Verify</button>
                <div class="feedback-dark" id="feedback-tf-m5-5"></div>
            </div>

            <div class="section-header">
                <h2>6. Bias in Data</h2>
            </div>
            <h3>Concept</h3>
            <p><strong>Bias</strong> refers to errors or unfair patterns in data collection or interpretation.</p>
            <p>Common types of bias:</p>
            <ul>
                <li>Confirmation bias</li>
                <li>Sampling bias</li>
                <li>Motivational bias</li>
            </ul>

            <div class="interaction-box" style="border-left-color: #ef4444; background: #fef2f2;">
                <strong>Insight:</strong> Biased data leads to incorrect conclusions and unfair decisions.
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Which of the following is a type of bias?</p>
                <div class="mcq-options" id="mcq-m5-6">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-6')"><span class="mcq-prefix">A.</span> Sorting</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-6')"><span class="mcq-prefix">B.</span> Sampling bias</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-6')"><span class="mcq-prefix">C.</span> Filtering</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-6')"><span class="mcq-prefix">D.</span> Aggregation</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m5-6', 'B', 'Correct!')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m5-6"></div>
            </div>

            <div class="section-header">
                <h2>7. Types of Bias</h2>
            </div>

            <h3>7.1 Confirmation Bias</h3>
            <p>Occurs when analysts focus only on data that supports their belief.</p>
            <div class="interaction-box" style="border-left-color: #ef4444; background: #fef2f2;">
                <strong>Insight:</strong> Ignoring opposite data leads to wrong conclusions.
            </div>
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>An analyst selects only data that supports their opinion. This is an example of:</p>
                <div class="mcq-options" id="mcq-m5-71">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-71')"><span class="mcq-prefix">A.</span> Sampling bias</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-71')"><span class="mcq-prefix">B.</span> Confirmation bias</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-71')"><span class="mcq-prefix">C.</span> Data cleaning</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-71')"><span class="mcq-prefix">D.</span> Aggregation</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m5-71', 'B', 'Correct!')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m5-71"></div>
            </div>

            <h3>7.2 Sampling Bias</h3>
            <p>Occurs when the sample does not represent the whole population.</p>
            <div class="interaction-box">
                <strong>Example:</strong> Surveying only urban customers and ignoring rural customers.
            </div>
            <div class="interaction-box" style="border-left-color: #ef4444; background: #fef2f2;">
                <strong>Insight:</strong> Poor sampling leads to inaccurate results.
            </div>
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <div class="tf-row" id="tf-row-m5-72"><span class="tf-statement">Sampling bias occurs when data is not representative of the population.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_v2(this, 'm5-72', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'm5-72', false)">False</button></div></div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkTFGroup_v2(['m5-72'], [true], 'feedback-tf-m5-72')">Verify</button>
                <div class="feedback-dark" id="feedback-tf-m5-72"></div>
            </div>

            <h3>7.3 Motivational Bias</h3>
            <p>Occurs when data is interpreted to support a desired outcome.</p>
            <div class="interaction-box" style="border-left-color: #ef4444; background: #fef2f2;">
                <strong>Insight:</strong> This bias can lead to manipulated conclusions.
            </div>
            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <p>Motivational bias occurs when:</p>
                <div class="mcq-options" id="mcq-m5-73">
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-73')"><span class="mcq-prefix">A.</span> Data is randomly collected</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-73')"><span class="mcq-prefix">B.</span> Data is interpreted to support a goal</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-73')"><span class="mcq-prefix">C.</span> Data is cleaned</div>
                    <div class="mcq-option" onclick="selectMCQ_v2(this, 'mcq-m5-73')"><span class="mcq-prefix">D.</span> Data is stored</div>
                </div>
                <button class="practice-dark-btn" onclick="checkMCQ_v2('mcq-m5-73', 'B', 'Correct!')">Verify</button>
                <div class="feedback-dark" id="feedback-mcq-m5-73"></div>
            </div>

            <div class="section-header">
                <h2>8. Ethical Data Usage</h2>
            </div>
            <h3>Concept</h3>
            <p>Ethical data usage means:</p>
            <ul>
                <li>using data responsibly</li>
                <li>avoiding misuse</li>
                <li>ensuring fairness</li>
            </ul>
            <p>Examples:</p>
            <ul>
                <li>not sharing personal data without consent</li>
                <li>avoiding manipulation of results</li>
            </ul>
            <div class="interaction-box" style="border-left-color: var(--accent-indigo); background: #f5f3ff;">
                <strong>Insight:</strong> Ethics ensures trust in data and analytics.
            </div>

            <div class="practice-card">
                <div class="practice-badge">PRACTICE</div>
                <div class="tf-row" id="tf-row-m5-8"><span class="tf-statement">Using data without user consent is ethical.</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF_v2(this, 'm5-8', true)">True</button><button class="tf-btn" onclick="selectTF_v2(this, 'm5-8', false)">False</button></div></div>
                <button class="practice-dark-btn" style="margin-top:15px;" onclick="checkTFGroup_v2(['m5-8'], [false], 'feedback-tf-m5-8')">Verify</button>
                <div class="feedback-dark" id="feedback-tf-m5-8"></div>
            </div>

            <div class="quiz-cta">
                <h3>Responsible Analytics Mastery Complete!</h3>
                <p>You've learned how to handle data securely, ethically, and without bias.</p>
                <a href="module_quiz.html?mod=data5" class="btn-start-quiz">Start Final Assessment &rarr;</a>
            </div>
"""

with open('Data-Module-4.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Update title and header
text = re.sub(r'<title>.*?</title>', '<title>Module 5: Responsible Analytics Practices | KVJ Analytics</title>', text)
text = re.sub(r'<h1>MODULE 4: DATA VISUALIZATION</h1>', '<h1>MODULE 5: RESPONSIBLE ANALYTICS</h1>', text)

# Update sidebar active class
text = text.replace('<a href="Data-Module-4.html" class="active">04 Visualization</a>', '<a href="Data-Module-4.html">04 Visualization</a>')
text = text.replace('<a href="#">05 Responsible Analytics</a>', '<a href="Data-Module-5.html" class="active">05 Responsible Analytics</a>')

# Replace main content
text = re.sub(r'<main class="main-content">.*?</main>', f'<main class="main-content">{html_content}</main>', text, flags=re.DOTALL)

with open('Data-Module-5.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Data-Module-5.html created successfully.")
