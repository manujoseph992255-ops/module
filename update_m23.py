import re

with open('Excel-Module-1-1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the title and header
html = re.sub(r'<title>.*?</title>', '<title>Module 2.3: Logical Functions | KVJ Analytics</title>', html)
html = re.sub(r'<h1>MODULE 1: ARCHITECTURAL DATA MODELING</h1>', '<h1>MODULE 2: ADVANCED LOOKUPS & LOGIC</h1>', html)

# Replace the active class in sidebar (move from 1.1 to 2.3)
html = html.replace('href="Excel-Module-1-1.html" class="active"', 'href="Excel-Module-1-1.html"')
html = html.replace('href="Excel-Module-2-3.html"', 'href="Excel-Module-2-3.html" class="active"')

# The main content to inject
new_content = """        <main class="main-content">
            <div class="section-header">
                <h2>2.3 Logical Functions</h2>
                <p style="font-weight: 600; color: var(--secondary-blue);">Mastering Conditional Architecture</p>
            </div>

            <div class="interaction-box">
                <strong>Strategic Logic</strong>
                <p style="margin-top:10px;">Logical functions allow your data models to make decisions automatically. By chaining IF, AND, OR, and NOT, you transform static data into intelligent, dynamic business rules.</p>
            </div>

            <div class="practice-space">
                <h3 style="margin-top:0; color: #1e3a5f;">Core Logical Functions</h3>
                
                <h4 style="color: #0284c7; margin-bottom: 5px;">1. IF Function</h4>
                <p style="margin-top:0;">Returns one value if a condition is <strong>TRUE</strong> and another if it is <strong>FALSE</strong>.</p>
                <div style="background: #f8fafc; padding: 15px; border-radius: 8px; border-left: 4px solid #0ea5e9; font-size: 14px;">
                    <strong>Example:</strong> If a sale is over ₹5,000, label it "Premium"; otherwise, "Standard."<br>
                    <code style="display:block; margin-top:8px; color: #d946ef;">=IF(Sales > 5000, "Premium", "Standard")</code>
                </div>

                <h4 style="color: #0284c7; margin-top: 25px; margin-bottom: 5px;">2. AND Function</h4>
                <p style="margin-top:0;">Returns <strong>TRUE</strong> only if <em>all</em> conditions are met.</p>
                <div style="background: #f8fafc; padding: 15px; border-radius: 8px; border-left: 4px solid #10b981; font-size: 14px;">
                    <strong>Example:</strong> Trigger a bonus only if Sales > ₹1,00,000 AND Attendance > 95%.<br>
                    <code style="display:block; margin-top:8px; color: #d946ef;">=AND(Sales > 100000, Attendance > 0.95)</code>
                </div>

                <h4 style="color: #0284c7; margin-top: 25px; margin-bottom: 5px;">3. OR Function</h4>
                <p style="margin-top:0;">Returns <strong>TRUE</strong> if at least <em>one</em> condition is met.</p>
                <div style="background: #f8fafc; padding: 15px; border-radius: 8px; border-left: 4px solid #f59e0b; font-size: 14px;">
                    <strong>Example:</strong> Flag an invoice for review if it is Overdue OR the amount exceeds ₹50,000.<br>
                    <code style="display:block; margin-top:8px; color: #d946ef;">=OR(Status = "Overdue", Amount > 50000)</code>
                </div>

                <h4 style="color: #0284c7; margin-top: 25px; margin-bottom: 5px;">4. NOT Function</h4>
                <p style="margin-top:0;">Reverses the logic (TRUE becomes FALSE). Useful for excluding specific criteria.</p>
                <div style="background: #f8fafc; padding: 15px; border-radius: 8px; border-left: 4px solid #ef4444; font-size: 14px;">
                    <strong>Example:</strong> Identify all boutique branches that are NOT located in the "South" region.<br>
                    <code style="display:block; margin-top:8px; color: #d946ef;">=NOT(Region = "South")</code>
                </div>
            </div>

            <!-- Footer Navigation -->
            <div class="module-navigation" style="display: flex; gap: 15px; justify-content: space-between; flex-wrap: wrap; margin-top: 40px; padding-top: 30px; border-top: 1px solid #e2e8f0;">
                <a href="excel_index.html" class="nav-btn nav-home">
                    Home
                </a>
                
                <a href="Excel-Module-2-4.html" class="nav-btn nav-next">
                    Next Topic
                </a>

                <a href="module_quiz.html?mod=ex2" class="nav-btn nav-assess">
                    Assessment
                </a>
            </div>
        </main>"""

# Replace the <main>...</main> content using re.sub with DOTALL
main_pattern = re.compile(r'<main class="main-content">.*?</main>', re.DOTALL)
html = main_pattern.sub(new_content, html)

# Remove the interactivity scripts for this specific page 
html = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)

with open('Excel-Module-2-3.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Created Excel-Module-2-3.html successfully")
