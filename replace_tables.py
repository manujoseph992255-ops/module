import re
import random
from datetime import datetime, timedelta

def generate_finance_rows(count):
    products = ['UltraBook Pro', 'Tablet X', 'SmartPhone 12', 'Monitor 27"', 'Wireless Mouse', 'Keyboard RGB', 'Headphones ANC']
    regions = ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Hyderabad']
    statuses = ['Completed', 'Completed', 'Completed', 'Pending', 'Failed']
    
    rows = []
    base_date = datetime(2023, 10, 1)
    
    for i in range(1, count + 1):
        txn_id = f"TXN-{10000 + i}"
        date = (base_date + timedelta(days=i%10, hours=i%8)).strftime("%Y-%m-%d")
        region = random.choice(regions)
        product = random.choice(products)
        units = random.randint(1, 15)
        revenue = units * random.randint(1500, 45000)
        status = random.choice(statuses)
        
        row_html = f"<tr><td>{txn_id}</td><td>{date}</td><td>{region}</td><td>{product}</td><td>{units}</td><td>₹{revenue:,}</td><td>{status}</td></tr>"
        rows.append(row_html)
        
    return "\n".join(rows)

full_table = f"""
                <div class="interaction-box">
                    <strong>Data Source: Enterprise Sales & Finance Records (Sample)</strong>
                </div>
                <table class="data-table">
                    <tr><th>Txn ID</th><th>Date</th><th>Region</th><th>Product</th><th>Units</th><th>Revenue (INR)</th><th>Status</th></tr>
                    {generate_finance_rows(25)}
                </table>
"""

with open(r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html", 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any orange colors if they somehow exist
html = html.replace('#f97316', 'var(--primary-blue)')
html = html.replace('#ea580c', 'var(--secondary-blue)')

# Section 1 table
# Old: <tr><th>Product</th><th>Sales</th></tr> <tr><td>Laptop</td><td>15</td></tr> ...
table_pattern_1 = r'<table class="data-table">\s*<tr><th>Product.*?</table>'
if re.search(table_pattern_1, html, re.DOTALL):
    html = re.sub(table_pattern_1, f"""<table class="data-table">
                    <tr><th>Txn ID</th><th>Date</th><th>Region</th><th>Product</th><th>Units</th><th>Revenue (INR)</th><th>Status</th></tr>
                    {generate_finance_rows(5)}
                </table>""", html, flags=re.DOTALL)

# Section 2 table
table_pattern_2 = r'<table class="data-table">\s*<tr><th>Day.*?</table>'
if re.search(table_pattern_2, html, re.DOTALL):
    html = re.sub(table_pattern_2, f"""<table class="data-table">
                    <tr><th>Txn ID</th><th>Date</th><th>Region</th><th>Product</th><th>Units</th><th>Revenue (INR)</th><th>Status</th></tr>
                    {generate_finance_rows(8)}
                </table>""", html, flags=re.DOTALL)


# Section 4 table (Data structures)
table_pattern_3 = r'<table class="data-table">\s*<tr><th>Name.*?</table>'
if re.search(table_pattern_3, html, re.DOTALL):
    html = re.sub(table_pattern_3, full_table, html, flags=re.DOTALL)

with open(r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html", 'w', encoding='utf-8') as f:
    f.write(html)

print("Tables updated.")
