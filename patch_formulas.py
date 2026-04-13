import os

with open('Excel-Module-11.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace 1-3
html = html.replace('<li style="margin-bottom: 12px;">Calculate the <strong>Sales Amount</strong> for each individual transaction.</li>',
'''<li style="margin-bottom: 25px;">Calculate the <strong>Sales Amount</strong> for each individual transaction.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans1" placeholder="Enter Excel formula (e.g. =C2*D2)">
                        <button onclick="verifyText('ans1', 'fb1')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb1" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>''')

html = html.replace('<li style="margin-bottom: 12px;">Calculate the <strong>Discount Amount</strong> for each individual transaction.</li>',
'''<li style="margin-bottom: 25px;">Calculate the <strong>Discount Amount</strong> for each individual transaction.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans2" placeholder="Enter Excel formula used">
                        <button onclick="verifyText('ans2', 'fb2')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb2" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>''')

html = html.replace('<li style="margin-bottom: 12px;">Calculate the <strong>Net Sales</strong> for each individual transaction.</li>',
'''<li style="margin-bottom: 25px;">Calculate the <strong>Net Sales</strong> for each individual transaction.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans3" placeholder="Enter Excel formula used">
                        <button onclick="verifyText('ans3', 'fb3')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb3" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>''')

# Replace 9-13
html = html.replace('<li style="margin-bottom: 12px;">Use an <strong>IF() function</strong> to flag any transaction with a Discount Amount greater than ₹500 as "High Discount". Otherwise, label it "Standard".</li>',
'''<li style="margin-bottom: 25px;">Use an <strong>IF() function</strong> to flag any transaction with a Discount Amount greater than ₹500 as "High Discount". Otherwise, label it "Standard".
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans9" placeholder="Paste your resulting IF() formula here">
                        <button onclick="verifyText('ans9', 'fb9')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb9" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>''')

html = html.replace('<li style="margin-bottom: 12px;">Format the Net Sales column to display as <strong>Currency (₹)</strong> with zero decimal places.</li>',
'''<li style="margin-bottom: 25px;">Format the Net Sales column to display as <strong>Currency (₹)</strong> with zero decimal places.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans10" placeholder="What keyboard shortcut or menu option did you use?">
                        <button onclick="verifyText('ans10', 'fb10')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb10" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>''')

html = html.replace('<li style="margin-bottom: 12px;">Convert the entire dynamic range of the Sales dataset into a structured <strong>Database Object (Table)</strong> formatting it professionally.</li>',
'''<li style="margin-bottom: 25px;">Convert the entire dynamic range of the Sales dataset into a structured <strong>Database Object (Table)</strong> formatting it professionally.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans11" placeholder="Enter Table Shortcut used (e.g. Ctrl+T)">
                        <button onclick="verifyText('ans11', 'fb11')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb11" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>''')

html = html.replace('<li style="margin-bottom: 12px;">Create a <strong>Pivot Table</strong> on a separate, dedicated worksheet showing the Total Net Sales Amount broken down by Product Category.</li>',
'''<li style="margin-bottom: 25px;">Create a <strong>Pivot Table</strong> on a separate, dedicated worksheet showing the Total Net Sales Amount broken down by Product Category.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans12" placeholder="Did you place it on a 'New Worksheet' or 'Existing'?">
                        <button onclick="verifyText('ans12', 'fb12')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb12" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>''')

html = html.replace('<li style="margin-bottom: 12px;">Insert a visual <strong>Slicer</strong> connected to your Pivot Table based on the "Region" field, allowing instant interactive filtering across territories.</li>',
'''<li style="margin-bottom: 25px;">Insert a visual <strong>Slicer</strong> connected to your Pivot Table based on the "Region" field, allowing instant interactive filtering across territories.
                    <div class="practice-box" style="margin-top: 10px;">
                        <input type="text" id="ans13" placeholder="Which field was used for the Slicer?">
                        <button onclick="verifyText('ans13', 'fb13')" style="background: var(--secondary-blue);">Verify</button>
                    </div>
                    <div id="fb13" class="feedback" style="margin-top: 8px; margin-bottom: 0;"></div>
                </li>''')


# Update JS logic to include verifyText
old_js = """            <script>
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
            </script>"""

new_js = """            <script>
                // Verify numeric metrics (strips strings)
                function verifyMetric(inputId, feedbackId) {
                    const val = document.getElementById(inputId).value.replace(/[^0-9.]/g, '');
                    const fb = document.getElementById(feedbackId);
                    
                    if (val === '') {
                        fb.className = "feedback wrong";
                        fb.innerHTML = "⚠️ Please enter a numeric value to verify.";
                        fb.style.display = "block";
                        return;
                    }
                    
                    fb.className = "feedback correct";
                    fb.innerHTML = "✅ Value <strong>" + val + "</strong> recorded successfully!";
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

                // Verify text/formula answers (allows strings)
                function verifyText(inputId, feedbackId) {
                    const val = document.getElementById(inputId).value.trim();
                    const fb = document.getElementById(feedbackId);
                    
                    if (val === '') {
                        fb.className = "feedback wrong";
                        fb.innerHTML = "⚠️ Please enter your formula or action taken.";
                        fb.style.display = "block";
                        return;
                    }
                    
                    fb.className = "feedback correct";
                    fb.innerHTML = "✅ Input <strong>" + val + "</strong> recorded successfully!";
                    fb.style.display = "block";
                    
                    if (typeof confetti !== "undefined") {
                        confetti({
                            particleCount: 50,
                            spread: 60,
                            origin: { y: 0.8 },
                            colors: ['#38bdf8', '#818cf8', '#a3e635']
                        });
                    }
                }
            </script>"""

html = html.replace(old_js, new_js)

with open('Excel-Module-11.html', 'w', encoding='utf-8') as f:
    f.write(html)
    print('All remaining inputs injected and JS updated.')
