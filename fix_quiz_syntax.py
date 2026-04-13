import json

data4 = [
    { "id": 1, "type": "MCQ", "q": "<strong>Chart Selection:</strong> Which visual chart is generally the best choice for displaying continuous trends over a period of time?", "options": ["Bar Chart", "Line Chart", "Pie Chart", "Scatter Plot"], "a": 1 },
    { "id": 2, "type": "MTF", "q": "<strong>Visualization Best Practices:</strong> Match the chart type to its most effective use case.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", "options": ["Pie Chart", "Bar Chart", "Scatter Plot", "Waterfall Chart"], "labels": ["Showing parts of a whole (percentages)", "Comparing nominal categorical data", "Showing correlation between two continuous variables", "Visualizing cumulative profit/cost changes"], "a": { "Pie Chart": "Showing parts of a whole (percentages)", "Bar Chart": "Comparing nominal categorical data", "Scatter Plot": "Showing correlation between two continuous variables", "Waterfall Chart": "Visualizing cumulative profit/cost changes" } },
    { "id": 3, "type": "DD", "q": "<strong>Dashboard Design:</strong> You are designing a professional executive dashboard.<br><br>When graphing a distribution of age groups, you should use a [b1]. To highlight the 'vital few' categories that cause 80% of customer complaints, use a [b2].", "options": [["Histogram", "Line Chart", "Pie Chart"], ["Pareto Chart", "Scatter Plot", "Radar Chart"]], "a": ["Histogram", "Pareto Chart"] },
    { "id": 4, "type": "TF", "q": "<strong>Clarity & Aesthetics:</strong> Evaluate the following visual design principles.<br><br>Select True or False for each statement.", "options": ["3D effects in bar charts significantly improve data readability.", "The '30-Second Insight' rule means a dashboard should take 30 seconds to load.", "A misleading axis (e.g., not starting at zero) can distort the perception of a Bar chart."], "a": [False, False, True] },
    { "id": 5, "type": "MCQ2", "q": "<strong>Data Storytelling:</strong> Which two elements are critical for effective data storytelling in a corporate presentation?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", "options": ["Using clear, descriptive titles and labels", "Hiding the axes to make the chart look minimalist", "Using contrasting colors to draw attention to key insights", "Applying a different font for every single data point"], "a": [0, 2] },
    { "id": 6, "type": "MCQ", "q": "<strong>Data Hierarchy:</strong> What does the 'Ink-to-Data Ratio' rule essentially recommend?", "options": ["Use as much ink as possible to make the chart bold.", "Remove non-essential visual clutter (borders, gridlines) to focus on the data.", "Only print charts using black ink.", "Ensure all data labels are underlined."], "a": 1 },
    { "id": 7, "type": "SHORT", "q": "<strong>Pareto Principle:</strong> The Pareto chart is based on the rule that what percentage of effects come from 20% of the causes? (Enter the number alone)", "a": "80" },
    { "id": 8, "type": "TF", "q": "<strong>Advanced Charts:</strong> Consider specialized visual tools.<br><br>Select True or False for each statement.", "options": ["A Heatmap uses color gradients to represent data intensity or density.", "Box plots are primarily used to show categorical sales margins.", "A Scatter Plot requires two numerical axes."], "a": [True, False, True] }
]

data5 = [
    { "id": 1, "type": "MCQ", "q": "<strong>Data Applications:</strong> Which of the following is an example of an algorithm applying Predictive Analysis in the real world?", "options": ["A thermostat that adjusts temperature based on the current time.", "A streaming service recommending movies based on your viewing history.", "A car dashboard displaying the current tire pressure.", "A cash register printing a receipt."], "a": 1 },
    { "id": 2, "type": "TF", "q": "<strong>Data Ethics:</strong> Evaluate the following statements on data ethics and security.<br><br>Select True or False for each statement.", "options": ["Data bias in training sets can lead to discriminatory AI models.", "Anonymizing data means to attach a person's explicit name to their records.", "Transparency involves hiding how user data is collected and processed."], "a": [True, False, False] },
    { "id": 3, "type": "MTF", "q": "<strong>Ethics Principles:</strong> Match the data governance concept with its correct definition.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", "options": ["Privacy", "Security", "Compliance", "Bias Mitigation"], "labels": ["Respecting user consent and data rights", "Protecting data from unauthorized access or breaches", "Adhering to legal standards like GDPR or CCPA", "Ensuring models represent diverse populations fairly"], "a": { "Privacy": "Respecting user consent and data rights", "Security": "Protecting data from unauthorized access or breaches", "Compliance": "Adhering to legal standards like GDPR or CCPA", "Bias Mitigation": "Ensuring models represent diverse populations fairly" } },
    { "id": 4, "type": "DD", "q": "<strong>Regulations:</strong> You are setting up user data policies for a European application.<br><br>You must ensure strict adherence to the [b1] framework, which protects consumer privacy and data rights in the EU. For California residents, you would reference [b2].", "options": [["GDPR", "HIPAA", "SOX"], ["CCPA", "HIPAA", "PCI-DSS"]], "a": ["GDPR", "CCPA"] },
    { "id": 5, "type": "MCQ2", "q": "<strong>Data Security:</strong> Which two practices are standard methods for protecting sensitive data?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", "options": ["Data Encryption", "Posting data to a public GitHub repo", "Role-Based Access Control (RBAC)", "Storing passwords in plain text"], "a": [0, 2] },
    { "id": 6, "type": "MCQ", "q": "<strong>Algorithmic Impact:</strong> What is a potential negative consequence of using historical data that contains human prejudices to train a machine learning model?", "options": ["Algorithmic Bias", "Data Encryption", "Data Normalization", "Increased Data Velocity"], "a": 0 },
    { "id": 7, "type": "TF", "q": "<strong>Ethics in Action:</strong> Review the scenarios concerning data rights.<br><br>Select True or False for each statement.", "options": ["Users generally have the right to request deletion of their personal data under GDPR.", "Data Security and Data Privacy are exactly the same concept.", "A company is ethically bound to protect user data even if it has no legal obligation."], "a": [True, False, True] },
    { "id": 8, "type": "SHORT", "q": "<strong>Acronym Check:</strong> What does the European privacy regulation acronym GDPR stand for?<br><span style='font-size: 15px; font-style: italic;'>Enter the exact term.</span>", "a": "General Data Protection Regulation" }
]

def format_js_objects(data_list):
    out = "[\n"
    for i, item in enumerate(data_list):
        items_str = []
        for k, v in item.items():
            if isinstance(v, str) and not k in ['id', 'a']:
                v_esc = v.replace('"', '\\"')
                items_str.append(f'{k}: "{v_esc}"')
            elif isinstance(v, (dict, list, bool, int, float)) or k == 'a':
                val_str = json.dumps(v)
                items_str.append(f'{k}: {val_str}')
            elif k == 'id':
                if isinstance(v, str):
                    items_str.append(f"id: '{v}'")
                else:
                    items_str.append(f"id: {v}")
        row = "        { " + ", ".join(items_str) + " }"
        if i < len(data_list) - 1:
            row += ","
        out += row + "\n"
    out += "    ]"
    return out

with open("quiz_data_test.js", "r", encoding="utf-8") as f:
    text = f.read()

# Fix d1 -> data1, d2 -> data2
text = text.replace('"d1": [', '"data1": [')
text = text.replace('"d2": [', '"data2": [')

# Inject data4 and data5 before the closing bracket of the entire file
text = text.replace("};", f',\n    "data4": {format_js_objects(data4)},\n    "data5": {format_js_objects(data5)}\n}};')

# Let's save it directly to quiz_data.js
with open("quiz_data.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Restored syntax from quiz_data_test.js, formatted properly, added data4 and data5.")
