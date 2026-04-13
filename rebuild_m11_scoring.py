import re

with open('Excel-Module-11.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the entire Core Execution Steps block including the list and the old submit button
new_core_html = """            <h3>Core Execution Steps</h3>
            <p>Perform the following calculations within the downloaded <strong>Sales</strong> worksheet. Use robust, change-proof formulas.</p>
            
            <ol id="practicals-list" style="margin-left: 35px; color: #334155; font-size: 16px; line-height: 1.8;">
                <li id="li-q1" style="margin-bottom: 25px;">In the Sales worksheet, calculate the Total Sales from Column M.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans1" placeholder="">
                    </div>
                </li>
                <li id="li-q2" style="margin-bottom: 25px;">In the Sales worksheet, calculate the Total Discount Amount from Column N.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans2" placeholder="">
                    </div>
                </li>
                <li id="li-q3" style="margin-bottom: 25px;">In the Sales worksheet, in Cell S4, calculate the Total Net Sales Amount from Column O.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans3" placeholder="">
                    </div>
                </li>
                <li id="li-q4" style="margin-bottom: 25px;">In the Sales worksheet, in Cell T4, calculate the Average Net Sales Amount from Column O.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans4" placeholder="">
                    </div>
                </li>
                <li id="li-q5" style="margin-bottom: 25px;">In the Sales worksheet, in Cell U4, calculate the Median Net Sales Amount from Column O.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans5" placeholder="">
                    </div>
                </li>
                <li id="li-q6" style="margin-bottom: 25px;">In the Sales worksheet, in Cell S7, calculate the Standard Deviation of Net Sales Amount from Column O.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans6" placeholder="">
                    </div>
                </li>
                <li id="li-q7" style="margin-bottom: 25px;">In the Sales worksheet, in Cell T7, calculate the Maximum Net Sales Amount from Column O.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans7" placeholder="">
                    </div>
                </li>
                <li id="li-q8" style="margin-bottom: 25px;">In the Sales worksheet, in Cell U7, calculate the Minimum Net Sales Amount from Column O.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans8" placeholder="">
                    </div>
                </li>
            </ol>

            <div id="results-panel" style="display: none; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; padding: 25px; margin-top: 40px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
                <h3 id="score-text" style="color: var(--primary-blue); margin-top: 0; font-family: 'Montserrat', sans-serif;"></h3>
                <p id="wrong-answers-info" style="margin-bottom: 20px; color: #64748b; font-size: 15px;"></p>
                <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                    <button id="btn-retake" onclick="retakeWrong()" style="display: none; background: #64748b; color: white; border: none; padding: 12px 35px; border-radius: 30px; font-weight: 700; cursor: pointer; transition: background 0.3s;">Retake Wrong Answers</button>
                    <a id="btn-pract2" href="Excel-Module-11-2.html" style="display: none; background: #10b981; color: white; border: none; padding: 12px 35px; border-radius: 30px; font-weight: 700; cursor: pointer; text-decoration: none; transition: background 0.3s;">Go to Practical 2 &rarr;</a>
                </div>
            </div>

            <div style="text-align: center; margin-top: 60px;">
                <button id="btn-submit-main" onclick="submitPracticals()" class="btn-roadmap btn-quiz" style="font-size: 17px; padding: 20px 60px; border-radius: 30px; cursor: pointer; background: var(--primary-blue); color: white; border: none; font-weight: 700; box-shadow: 0 10px 20px rgba(30, 58, 95, 0.2); transition: all 0.3s;">Submit All Answers</button>
            </div>"""

# Find core steps start
start_marker = r"<h3>Core Execution Steps</h3>"
# Find end of that section (before the hr)
end_marker = r'<hr style="border:0; border-top: 2px solid #f1f5f9; margin: 50px 0;">'

pattern = f"{start_marker}.*?{end_marker}"
html = re.sub(pattern, f"{new_core_html}\n            {end_marker}", html, flags=re.DOTALL)

# 2. Update JavaScript
new_js = """            <script>
                const answerKey = [9996027, 477403, 9518624, 15858, 13041, 11077, 49140, 2285];
                let wrongIndices = [];

                function submitPracticals() {
                    wrongIndices = [];
                    let score = 0;
                    
                    for (let i = 1; i <= 8; i++) {
                        const input = document.getElementById('ans' + i);
                        const userVal = parseInt(input.value.replace(/[^0-9]/g, '')) || 0;
                        const correctVal = answerKey[i-1];
                        const li = document.getElementById('li-q' + i);
                        
                        if (userVal === correctVal) {
                            score++;
                            li.style.color = "#10b981";
                            li.style.background = "#f0fdf4";
                            li.style.borderRadius = "8px";
                            li.style.padding = "10px";
                            li.style.marginLeft = "25px";
                        } else {
                            wrongIndices.push(i);
                            li.style.color = "#ef4444";
                            li.style.background = "#fef2f2";
                            li.style.borderRadius = "8px";
                            li.style.padding = "10px";
                            li.style.marginLeft = "25px";
                        }
                    }

                    const panel = document.getElementById('results-panel');
                    const scoreText = document.getElementById('score-text');
                    const infoText = document.getElementById('wrong-answers-info');
                    const btnRetake = document.getElementById('btn-retake');
                    const btnNext = document.getElementById('btn-pract2');

                    panel.style.display = "block";
                    scoreText.innerHTML = "Score: " + score + " / 8";
                    
                    if (score === 8) {
                        infoText.innerHTML = "Perfect! All metrics match the Strategic Decision Matrix exactly.";
                        btnRetake.style.display = "none";
                        btnNext.style.display = "inline-block";
                        if (typeof confetti !== "undefined") {
                            confetti({ particleCount: 150, spread: 70, origin: { y: 0.6 } });
                        }
                    } else {
                        infoText.innerHTML = "You have " + (8 - score) + " incorrect metrics. Please review your Excel calculations.";
                        btnRetake.style.display = "inline-block";
                        btnNext.style.display = "none";
                    }
                    
                    // Smooth scroll to results
                    panel.scrollIntoView({ behavior: 'smooth' });
                }

                function retakeWrong() {
                    for (let i = 1; i <= 8; i++) {
                        if (wrongIndices.includes(i)) {
                            const input = document.getElementById('ans' + i);
                            input.value = "";
                            const li = document.getElementById('li-q' + i);
                            li.style.color = "#334155";
                            li.style.background = "transparent";
                            li.style.padding = "0";
                            li.style.marginLeft = "35px";
                        }
                    }
                    document.getElementById('results-panel').style.display = "none";
                }
            </script>"""

# Replace the entire script block
html = re.sub(r'<script>.*?</script>', new_js, html, flags=re.DOTALL)

with open('Excel-Module-11.html', 'w', encoding='utf-8') as f:
    f.write(html)
    print("Module 11 Rebuilt with Scored Metrics.")
