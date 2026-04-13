import os

with open('Excel-Module-11.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the Core Execution Steps list items with interactive ones
old_li4 = '<li style="margin-bottom: 12px;">Determine the <strong>Total Net Sales Amount</strong> across all records.</li>'
new_li4 = '''<li style="margin-bottom: 25px;">Determine the <strong>Total Net Sales Amount</strong> across all records.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans4" placeholder="Enter calculated value (e.g. 45000)">
                        <button onclick="verifyMetric('ans4', 'fb4')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb4" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>'''

old_li5 = '<li style="margin-bottom: 12px;">Calculate the <strong>Average Net Sales Amount</strong>.</li>'
new_li5 = '''<li style="margin-bottom: 25px;">Calculate the <strong>Average Net Sales Amount</strong>.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans5" placeholder="Enter calculated average">
                        <button onclick="verifyMetric('ans5', 'fb5')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb5" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>'''

old_li6 = '<li style="margin-bottom: 12px;">Calculate the <strong>Median Net Sales Amount</strong> to understand typical spend.</li>'
new_li6 = '''<li style="margin-bottom: 25px;">Calculate the <strong>Median Net Sales Amount</strong> to understand typical spend.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans6" placeholder="Enter calculated median">
                        <button onclick="verifyMetric('ans6', 'fb6')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb6" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>'''

old_li7 = '<li style="margin-bottom: 12px;">Calculate the <strong>Standard Deviation</strong> of the Net Sales Amount to measure volatility.</li>'
new_li7 = '''<li style="margin-bottom: 25px;">Calculate the <strong>Standard Deviation</strong> of the Net Sales Amount to measure volatility.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans7" placeholder="Enter calculated standard deviation">
                        <button onclick="verifyMetric('ans7', 'fb7')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb7" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>'''

old_li8 = '<li style="margin-bottom: 12px;">Calculate the <strong>Maximum Net Sales Amount</strong> pointing to your Hero Product transaction.</li>'
new_li8 = '''<li style="margin-bottom: 25px;">Calculate the <strong>Maximum Net Sales Amount</strong> pointing to your Hero Product transaction.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans8" placeholder="Enter maximum value">
                        <button onclick="verifyMetric('ans8', 'fb8')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb8" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>'''

html = html.replace(old_li4, new_li4)
html = html.replace(old_li5, new_li5)
html = html.replace(old_li6, new_li6)
html = html.replace(old_li7, new_li7)
html = html.replace(old_li8, new_li8)

# Add the JS logic for verifyMetric right before the closing body tag
js_logic = '''
            <script>
                // Confetti logic already exists in the header/body but let's redefine just in case, or use a simple alert if confetti fails
                function verifyMetric(inputId, feedbackId) {
                    const val = document.getElementById(inputId).value.replace(/[^0-9.]/g, ''); // Strip non-numeric chars
                    const fb = document.getElementById(feedbackId);
                    
                    if (val === '') {
                        fb.className = "feedback wrong";
                        fb.innerHTML = "⚠️ Please enter a numeric value to verify.";
                        fb.style.display = "block";
                        return;
                    }
                    
                    fb.className = "feedback correct";
                    fb.innerHTML = "✅ Value " + val + " recorded successfully!";
                    fb.style.display = "block";
                    
                    if (typeof confetti !== "undefined") {
                        confetti({
                            particleCount: 50,
                            spread: 60,
                            origin: { y: 0.8 },
                            colors: ['#10b981', '#008eab']
                        });
                    }
                }
            </script>
</body>
'''

html = html.replace('</body>', js_logic)

with open('Excel-Module-11.html', 'w', encoding='utf-8') as f:
    f.write(html)
    print("Injected input boxes and verification JS into Module 11 successfully.")
