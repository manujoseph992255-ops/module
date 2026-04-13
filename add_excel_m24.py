import os
import re

dir_path = r"c:\Users\kj anand\Downloads\Quiz DD"

# Create Excel-Module-2-4.html based on 2-3
m23_path = os.path.join(dir_path, "Excel-Module-2-3.html")
m24_path = os.path.join(dir_path, "Excel-Module-2-4.html")
roadmap_path = os.path.join(dir_path, "excel_roadmap.html")

with open(m23_path, "r", encoding="utf-8") as f:
    m23_content = f.read()

# Replace the title and header
m24_content = m23_content.replace("<title>Module 2.3: Boolean Logic in Retrieval", "<title>Module 2.4: Strategic Logic & Functions")

new_main_content = """
            <div class="section-header">
                <h2>2.4 Strategic Logic & Functions</h2>
                <p style="font-weight: 600; color: var(--secondary-blue);">Mean, Variance, and Decision Making</p>
            </div>

            <div class="interaction-box">
                <strong>The Strategic Logic:</strong>
                <p style="margin-top:10px;">A manager's primary role is to maintain the "Mean" (Average) and minimize "Variance" (Risk).</p>
            </div>

            <h3>1. Statistical Functions</h3>
            <ul>
                <li><strong>Central Tendency:</strong> Using <code>SUM</code>, <code>AVERAGE</code>, and <code>MEDIAN</code> to identify the "Boutique Pulse."</li>
                <li style="margin-top: 15px;"><strong>The Volatility Check:</strong> Utilizing <code>STDEV.P</code> to measure sales consistency.
                    <ul style="margin-top: 10px; margin-bottom: 0;">
                        <li><strong>High Std Dev:</strong> Indicates unpredictable footfall; requires higher "Safety Stock" levels.</li>
                        <li><strong>Low Std Dev:</strong> Indicates stable demand; allows for "Just-in-Time" inventory.</li>
                    </ul>
                </li>
                <li style="margin-top: 15px;"><strong>Outlier Detection:</strong> Using <code>MIN</code> and <code>MAX</code> to identify "Hero Products" versus "Dead Stock" that is consuming liquid capital.</li>
            </ul>

            <!-- Practice 1 -->
            <div class="practice-space">
                <h3 style="margin-top:0;">Practice: Outlier Detection</h3>
                <p style="margin-bottom: 20px;">Which function would you use to find the single highest-performing "Hero Product" in the sales range B2:B100?</p>
                <div class="practice-box">
                    <input type="text" id="prac1" placeholder="Type function name here (e.g. SUM)">
                    <button onclick="checkExcel('prac1', 'MAX', 'fb1')">Submit</button>
                </div>
                <div id="fb1" class="feedback"></div>
            </div>

            <hr style="border:0; border-top:1px solid var(--border-color); margin: 40px 0;">

            <h3>2. Logical Functions</h3>
            <ul>
                <li><strong>IF:</strong> Returns one value if a condition is TRUE and another if it is FALSE.
                    <br><span style="color:var(--text-muted); font-size:14px; display:block; margin-top:5px; margin-bottom:5px;"><em>Example: If a sale is over ₹5,000, label it "Premium"; otherwise, "Standard."</em></span>
                </li>
                <li><strong>AND:</strong> Returns TRUE only if all conditions are met.
                    <br><span style="color:var(--text-muted); font-size:14px; display:block; margin-top:5px; margin-bottom:5px;"><em>Example: Trigger a bonus only if Sales > ₹1,00,000 AND Attendance > 95%.</em></span>
                </li>
                <li><strong>OR:</strong> Returns TRUE if at least one condition is met.
                    <br><span style="color:var(--text-muted); font-size:14px; display:block; margin-top:5px; margin-bottom:5px;"><em>Example: Flag an invoice for review if it is Overdue OR the amount exceeds ₹50,000.</em></span>
                </li>
                <li><strong>NOT:</strong> Reverses the logic.
                    <br><span style="color:var(--text-muted); font-size:14px; display:block; margin-top:5px; margin-bottom:5px;"><em>Example: Identify all boutique branches that are NOT located in the "South" region.</em></span>
                </li>
            </ul>

            <!-- Practice 2 -->
            <div class="practice-space">
                <h3 style="margin-top:0;">Practice: Multi-Condition Logic</h3>
                <p style="margin-bottom: 20px;">Which logical function should wrap around multiple conditions if a manager wants to flag an employee who meets <strong>every single one</strong> of the criteria?</p>
                <div class="practice-box">
                    <input type="text" id="prac2" placeholder="Type function name here (e.g. IF)">
                    <button onclick="checkExcel('prac2', 'AND', 'fb2')">Submit</button>
                </div>
                <div id="fb2" class="feedback"></div>
            </div>

            <script>
                function checkExcel(inputId, correctAns, feedbackId) {
                    const val = document.getElementById(inputId).value.toUpperCase().replace(/\s+/g, '');
                    const feedback = document.getElementById(feedbackId);
                    if(val.includes(correctAns)) {
                        feedback.className = "feedback correct";
                        feedback.innerHTML = "✅ Correct! " + correctAns + " is the right function.";
                    } else {
                        feedback.className = "feedback wrong";
                        feedback.innerHTML = "❌ Incorrect. Remember, look at the key functions listed above.";
                    }
                }
            </script>

            <div class="next-btn-container" style="display: flex; justify-content: space-between; flex-wrap:wrap; text-align:center;">
                <a href="Excel-Module-2-3.html" class="prev-btn" style="flex:100%">&larr; Back to Topic 2.3</a>
                <p style="margin: 20px 0; font-weight: 700; color: var(--primary-blue); flex:100%;">End of Module 2: Advanced Lookups & Logical Architecture</p>
                <a href="module_quiz.html?mod=ex2" class="next-btn" style="flex:100%">Start Assessment &checkmark;</a>
            </div>
"""

# Extract the main content area using standard string split to avoid regex escaping errors with JS code
parts = m24_content.split('<div class="section-header">', 1)
main_before = parts[0]
main_after = parts[1].split('</main>', 1)[1]

m24_content = main_before + new_main_content + '\n        </main>' + main_after

with open(m24_path, "w", encoding="utf-8") as f:
    f.write(m24_content)

# Update Excel-Module-2-3.html to remove the assessment link and add a next button
m23_replacement = """<div class="next-btn-container" style="display: flex; justify-content: space-between;">
                <a href="Excel-Module-2-2.html" class="prev-btn">&larr; Previous Page</a>
                <a href="Excel-Module-2-4.html" class="next-btn">Next: Strategic Logic &rarr;</a>
            </div>"""
m23_content_fixed = re.sub(r'<div class="next-btn-container">.*?</div>', m23_replacement, m23_content, flags=re.DOTALL)
with open(m23_path, "w", encoding="utf-8") as f:
    f.write(m23_content_fixed)

# Update roadmap to add 2.4
with open(roadmap_path, "r", encoding="utf-8") as f:
    rm_content = f.read()

# Add 2.4 under module 2
rm_fixed = rm_content.replace('<li>2.3 Boolean Arrays & Filters</li>', '<li>2.3 Boolean Arrays & Filters</li>\n                    <li>2.4 Strategic Logic & Functions</li>')

with open(roadmap_path, "w", encoding="utf-8") as f:
    f.write(rm_fixed)

print("Done. 2.4 created, 2.3 linking updated, roadmap updated.")
