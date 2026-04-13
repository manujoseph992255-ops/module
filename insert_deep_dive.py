import os

html_to_insert = """
                <h3>Deep Dive: Categorical Data</h3>
                <p>Categorical data is qualitative and lacks mathematical meaning.</p>
                <ul class="content-list" style="margin-bottom: 25px; list-style-type: none; padding-left: 0;">
                    <li>• <strong>Nominal Data:</strong> This is data used for naming or labeling variables without any quantitative value or intrinsic order. Examples include Hair Color (Blonde, Brown, Brunette), Marital Status (Single, Married, Divorced), or Nationality. You cannot say one label is "greater" or "better" than another.</li>
                    <li>• <strong>Ordinal Data:</strong> This data type has nominal properties but also has a clear, natural order or ranking. However, the exact differences between the ranks are unknown or meaningless. For example, Customer Satisfaction (1-Poor, 2-Average, 3-Good, 4-Excellent). We know "Excellent" is better than "Good", but we can't mathematically quantify <i>how much</i> better.</li>
                </ul>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Categorical Practice</h4>
                    <p>Classify the following Categorical data examples as Nominal or Ordinal:</p>
                    <div class="tf-row"><span class="tf-statement">1. Blood Type (A, B, AB, O)</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'dt-cat-1', true)">Nominal</button><button class="tf-btn" onclick="selectTF(this, 'dt-cat-1', false)">Ordinal</button></div></div>
                    <div class="tf-row"><span class="tf-statement">2. Military Rank (Sergeant, Captain, Major)</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'dt-cat-2', false)">Nominal</button><button class="tf-btn" onclick="selectTF(this, 'dt-cat-2', true)">Ordinal</button></div></div>
                    <div class="tf-row"><span class="tf-statement">3. Car Model (Toyota, Honda, Ford)</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'dt-cat-3', true)">Nominal</button><button class="tf-btn" onclick="selectTF(this, 'dt-cat-3', false)">Ordinal</button></div></div>
                    
                    <button class="practice-dark-btn" style="margin-top:20px;" onclick="checkTFGroup(['dt-cat-1', 'dt-cat-2', 'dt-cat-3'], [true, true, true], 'feedback-dt-cat')">Check Answers</button>
                    <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetTFGroup(['dt-cat-1', 'dt-cat-2', 'dt-cat-3'], 'feedback-dt-cat')">&#8635; Reset</button>
                    <div class="feedback-dark" id="feedback-dt-cat"></div>
                </div>

                <h3>Deep Dive: Numerical Data</h3>
                <p>Numerical data is quantitative and can be measured and subjected to mathematical operations.</p>
                <ul class="content-list" style="margin-bottom: 25px; list-style-type: none; padding-left: 0;">
                    <li>• <strong>Interval Data:</strong> Numeric ranges where we know both the order and the exact differences between the values. However, it lacks a "true zero" (a point where none of the quantity exists). A classic example is Temperature in Celsius or Fahrenheit. The difference between 20°C and 30°C is the same as between 30°C and 40°C, but 0°C does not mean "no temperature". Therefore, you cannot say 40°C is "twice as hot" as 20°C.</li>
                    <li>• <strong>Ratio Data:</strong> The ultimate form of numerical data. It has an order, exact intervals between values, AND a true absolute zero meaning absence. Examples include Height, Weight, Age, and Salary. Because there is a true zero (e.g., $0 salary means no salary), you can make meaningful ratios: a $100,000 salary is exactly twice as much as a $50,000 salary.</li>
                </ul>

                <div class="practice-card">
                    <div class="practice-badge">PRACTICE</div>
                    <h4>Numerical Practice</h4>
                    <p>Classify the following Numerical data examples as Interval or Ratio:</p>
                    <div class="tf-row"><span class="tf-statement">1. Number of children in a household</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'dt-num-1', false)">Interval</button><button class="tf-btn" onclick="selectTF(this, 'dt-num-1', true)">Ratio</button></div></div>
                    <div class="tf-row"><span class="tf-statement">2. The year (1990, 2010, 2024)</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'dt-num-2', true)">Interval</button><button class="tf-btn" onclick="selectTF(this, 'dt-num-2', false)">Ratio</button></div></div>
                    <div class="tf-row"><span class="tf-statement">3. Distance from home to office in miles</span><div class="tf-btn-group"><button class="tf-btn" onclick="selectTF(this, 'dt-num-3', false)">Interval</button><button class="tf-btn" onclick="selectTF(this, 'dt-num-3', true)">Ratio</button></div></div>
                    
                    <button class="practice-dark-btn" style="margin-top:20px;" onclick="checkTFGroup(['dt-num-1', 'dt-num-2', 'dt-num-3'], [true, true, true], 'feedback-dt-num')">Check Answers</button>
                    <button class="practice-dark-btn" style="background:#334155; margin-left:10px;" onclick="resetTFGroup(['dt-num-1', 'dt-num-2', 'dt-num-3'], 'feedback-dt-num')">&#8635; Reset</button>
                    <div class="feedback-dark" id="feedback-dt-num"></div>
                </div>
"""

with open('Data-Module-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert the deep dives right after the image
target_marker = """<img src="Data-Hierarchy.png" alt="Data Types Hierarchy: Data -> Categorical/Numerical -> Nominal/Ordinal/Interval/Ratio" style="max-width: 100%; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.05);">
                </div>"""

# Ensure we're inserting safely before the old practice card we want to keep
html = html.replace(target_marker, target_marker + "\n" + html_to_insert)

with open('Data-Module-1.html', 'w', encoding='utf-8') as f:
    f.write(html)
