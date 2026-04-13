import re

# 1. Update excel_roadmap.html
try:
    with open('excel_roadmap.html', 'r', encoding='utf-8') as f:
        roadmap = f.read()

    old_buttons = """                <div class="card-buttons">
                    <a href="Excel-Module-11.html" class="btn-roadmap btn-study">Study Material</a>
                    <a href="module_quiz.html?mod=ex11" class="btn-roadmap btn-quiz">Assessment</a>
                </div>"""
                
    new_button = """                <div class="card-buttons">
                    <a href="Excel-Module-11.html" class="btn-roadmap btn-quiz" style="font-size: 14px; padding: 15px;">Start Practicals</a>
                </div>"""
                
    roadmap = roadmap.replace(old_buttons, new_button)
    
    with open('excel_roadmap.html', 'w', encoding='utf-8') as f:
        f.write(roadmap)
    print('Updated roadmap buttons.')
except Exception as e:
    print('Error updating roadmap:', e)


# 2. Generate Excel-Module-11.html from Excel-Module-4.html
try:
    with open('Excel-Module-4.html', 'r', encoding='utf-8') as f:
        mod11 = f.read()
        
    # Update title and Banner
    mod11 = mod11.replace('<title>Module 4: Structured Data | KVJ Analytics</title>', '<title>Module 11: Practicals | KVJ Analytics</title>')
    mod11 = mod11.replace('MODULE 4: STRUCTURED DATA', 'MODULE 11: CAPSTONE PRACTICALS')

    # Update active class in sidebar
    mod11 = mod11.replace('<a href="Excel-Module-4.html" class="active">04 Structured Data</a>', '<a href="Excel-Module-4.html">04 Structured Data</a>')
    
    # Add Module 11 link to sidebar before the Navigation header
    sidebar_insert = '            <a href="Excel-Module-10-1.html">10 Master Capstone</a>\n            <a href="Excel-Module-11.html" class="active">11 Practicals</a>'
    mod11 = mod11.replace('<a href="Excel-Module-10-1.html">10 Master Capstone</a>', sidebar_insert)

    # Make sure all other files have Module 11 in their sidebar as well! We'll just patch the sidebar for all files later if needed.
    
    # Generate the main content for Practicals
    new_content = """
            <div class="section-header">
                <h2>11. Master Practicals</h2>
                <p style="font-weight: 600; color: var(--secondary-blue);">Real-World Business Execution</p>
            </div>

            <div class="interaction-box" style="background-color: #f0fdf4; border-left-color: #10b981; margin-bottom: 40px;">
                <strong>Simulation Dataset</strong>
                <p style="margin-top:10px; margin-bottom: 20px;">Download the raw dataset below to begin your practical assignment. You will execute the following logic directly within the worksheet.</p>
                
                <a href="#" onclick="alert('Downloading Simulation Dataset: Sales_Data_Q3_Final.xlsx'); return false;" style="display: inline-flex; align-items: center; gap: 10px; background: #10b981; color: white; padding: 12px 25px; border-radius: 8px; font-weight: 700; text-decoration: none; transition: transform 0.2s;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                    Download Sales_Data_Q3_Final.xlsx
                </a>
            </div>

            <h3>Core Execution Steps</h3>
            <p>Perform the following calculations within the downloaded <strong>Sales</strong> worksheet. Use robust, change-proof formulas.</p>
            
            <ol style="margin-left: 20px; color: #334155; font-size: 16px; line-height: 1.8;">
                <li style="margin-bottom: 12px;">Calculate the <strong>Sales Amount</strong> for each individual transaction.</li>
                <li style="margin-bottom: 12px;">Calculate the <strong>Discount Amount</strong> for each individual transaction.</li>
                <li style="margin-bottom: 12px;">Calculate the <strong>Net Sales</strong> for each individual transaction.</li>
                <li style="margin-bottom: 12px;">Determine the <strong>Total Net Sales Amount</strong> across all records.</li>
                <li style="margin-bottom: 12px;">Calculate the <strong>Average Net Sales Amount</strong>.</li>
                <li style="margin-bottom: 12px;">Calculate the <strong>Median Net Sales Amount</strong> to understand typical spend.</li>
                <li style="margin-bottom: 12px;">Calculate the <strong>Standard Deviation</strong> of the Net Sales Amount to measure volatility.</li>
                <li style="margin-bottom: 12px;">Calculate the <strong>Maximum Net Sales Amount</strong> pointing to your Hero Product transaction.</li>
            </ol>

            <h3 style="margin-top: 40px;">Advanced Logic & Structuring</h3>
            <p>Once your core metrics are calculated, complete the following modeling and formatting steps.</p>

            <ol start="9" style="margin-left: 20px; color: #334155; font-size: 16px; line-height: 1.8;">
                <li style="margin-bottom: 12px;">Use an <strong>IF() function</strong> to flag any transaction with a Discount Amount greater than ₹500 as "High Discount". Otherwise, label it "Standard".</li>
                <li style="margin-bottom: 12px;">Format the Net Sales column to display as <strong>Currency (₹)</strong> with zero decimal places.</li>
                <li style="margin-bottom: 12px;">Convert the entire dynamic range of the Sales dataset into a structured <strong>Database Object (Table)</strong> formatting it professionally.</li>
                <li style="margin-bottom: 12px;">Create a <strong>Pivot Table</strong> on a separate, dedicated worksheet showing the Total Net Sales Amount broken down by Product Category.</li>
                <li style="margin-bottom: 12px;">Insert a visual <strong>Slicer</strong> connected to your Pivot Table based on the "Region" field, allowing instant interactive filtering across territories.</li>
            </ol>

            <div style="text-align: center; margin-top: 60px;">
                <button onclick="alert('Practicals Submitted Successfully for Evaluation!');" class="btn-roadmap btn-quiz" style="font-size: 16px; padding: 18px 50px; border-radius: 30px; cursor: pointer;">Submit Final Project</button>
            </div>
            
            <hr style="border:0; border-top: 2px solid #f1f5f9; margin: 50px 0;">
"""
    # Exclude the gamified practice panels since the user said "no material and assessment... add a fake link ... and practicals". The whole page IS the assessment!
    end_tag = '<!-- Footer Navigation -->'
    start_tag = '<main class="main-content">'

    if start_tag in mod11 and end_tag in mod11:
        pre = mod11.split(start_tag)[0]
        post = mod11.split(end_tag)[1]
        mod11 = pre + start_tag + new_content + end_tag + post
        
    # Remove the illustration container (floating panel) as this page shouldn't have distractions
    mod11 = re.sub(r'<style>\s*\.illustration-container[\s\S]*?</div>\s*</div>', '', mod11)

    with open('Excel-Module-11.html', 'w', encoding='utf-8') as f:
        f.write(mod11)
        
    print('Created Excel-Module-11.html.')
    
except Exception as e:
    print('Error creating Module 11:', e)

# 3. Patch the sidebars in all Excel-Module files to include the 11th Module
for filepath in glob.glob('Excel-Module-*.html'):
    if '-11' in filepath: continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '11 Practicals' not in content:
            sidebar_insert = '            <a href="Excel-Module-10-1.html">10 Master Capstone</a>\\n            <a href="Excel-Module-11.html">11 Practicals</a>'
            content = content.replace('            <a href="Excel-Module-10-1.html">10 Master Capstone</a>', sidebar_insert)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception as e:
        print(f'Error updating sidebar in {filepath}: {e}')
