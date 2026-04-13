import json
import re
import os

# Module 1: 16 Questions
DATA1 = [
    { "id": 1, "type": "MCQ", "q": "1. What is Data?<br>Which statement best describes data?", "options": ["Processed information ready for decision making", "Raw facts and figures collected for analysis", "A business strategy", "A summarized report"], "a": 1 },
    { "id": 2, "type": "TF", "q": "2. True or False<br>Data becomes meaningful only after processing and analysis.", "options": ["Data becomes meaningful only after processing and analysis."], "a": [True] },
    { "id": 3, "type": "MCQ", "q": "3. Which Data Type Stores Text?<br>Which data type can store a sentence or phrase?", "options": ["Integer", "Boolean", "String", "Float"], "a": 2 },
    { "id": 4, "type": "MCQ", "q": "4. Identify the Data Type<br>Select the correct data type for the value below.<br><code>is_logged_in = True</code>", "options": ["Integer", "Boolean", "String", "Float"], "a": 1 },
    { "id": 5, "type": "MTF", "q": "5. Drag and Drop<br>Match the data structure with the description.", "options": ["Table", "Row", "Column", "List"], "labels": ["Multiple rows and columns", "Single record in a dataset", "Attribute or field", "Collection of items"], "a": { "Table": "Multiple rows and columns", "Row": "Single record in a dataset", "Column": "Attribute or field", "List": "Collection of items" } },
    { "id": 6, "type": "MCQ", "q": "6. Which Data Structure Describes This Data?<br><code>[\"Aabid\", \"Jesenia\", \"Mark\"]</code>", "options": ["Table", "List", "Graph", "Matrix"], "a": 1 },
    { "id": 7, "type": "MCQ", "q": "7. Multiple Choice<br>Which of the following is quantitative data?", "options": ["Eye color", "Age", "Country name", "Product category"], "a": 1 },
    { "id": 8, "type": "TF", "q": "8. True or False<br>Qualitative data describes categories rather than numeric values.", "options": ["Qualitative data describes categories rather than numeric values."], "a": [True] },
    { "id": 9, "type": "MTF", "q": "9. Match the Data Type<br>Drag each example to the correct category.", "options": ["Gender", "Height", "Temperature", "Country"], "labels": ["Qualitative Data (A)", "Quantitative Data (A)", "Quantitative Data (B)", "Qualitative Data (B)"], "a": { "Gender": "Qualitative Data (A)", "Country": "Qualitative Data (B)", "Height": "Quantitative Data (A)", "Temperature": "Quantitative Data (B)" } },
    { "id": 10, "type": "MCQ", "q": "10. Structured vs Unstructured Data<br>Which of the following is structured data?", "options": ["Video file", "Email message", "Excel table", "Social media post"], "a": 2 },
    { "id": 11, "type": "MCQ", "q": "11. What is Metadata?<br>Metadata refers to:", "options": ["Raw data collected from sensors", "Data about other data", "Unstructured data", "Numerical calculations"], "a": 1 },
    { "id": 12, "type": "MCQ", "q": "12. Example of Metadata<br>Which of the following is an example of metadata?", "options": ["The image itself", "The creation date of a file", "The text inside a document", "The number of users on a website"], "a": 1 },
    { "id": 13, "type": "MCQ", "q": "13. Big Data<br>Which statement best describes big data?", "options": ["Small datasets stored in spreadsheets", "Extremely large and complex datasets", "Only structured data", "Only text data"], "a": 1 },
    { "id": 14, "type": "MTF", "q": "14. Drag and Drop \u2013 Statistical Metrics<br>Match the metric with the description.", "options": ["Sum", "Max", "Min", "Average"], "labels": ["Total of values", "Largest value", "Smallest value", "Mean of values"], "a": { "Sum": "Total of values", "Max": "Largest value", "Min": "Smallest value", "Average": "Mean of values" } },
    { "id": 15, "type": "MCQ", "q": "15. Data Classification<br>Person A has 5 coins and Person B has 10 coins. The number of coins represents:", "options": ["Qualitative data", "Quantitative data", "Metadata", "Ordinal data"], "a": 1 },
    { "id": 16, "type": "MCQ", "q": "16. Data Insight Question<br>A company records: Customer age, Purchase amount, Product category. Which of these variables is qualitative data?", "options": ["Age", "Purchase amount", "Product category", "All of the above"], "a": 2 }
]

# Module 2: 7 Questions
DATA2 = [
    { "id": 1, "type": "MCQ", "q": "Which of the following is an example of data cleaning?", "options": ["Arranging Excel rows in order for easy reading", "Ensuring a Word table uses a consistent font", "Adding quotation marks to a tab-delimited file", "Removing non-printable characters from a comma-delimited file"], "a": 3 },
    { "id": 2, "type": "MTF", "q": "You are performing descriptive analytics on quarterly sales data. Match the metric with the description.", "options": ["Average", "Max", "Min", "Sum"], "labels": ["Mean value of sales", "Largest value", "Smallest value", "Total of all values"], "a": { "Average": "Mean value of sales", "Max": "Largest value", "Min": "Smallest value", "Sum": "Total of all values" } },
    { "id": 3, "type": "MCQ2", "q": "You need to create a data view based on aggregations for sales data from the last five years. Which two aggregation methods should you use?", "options": ["Filtering", "Pivoting", "Merging", "Grouping"], "a": [1, 3] },
    { "id": 4, "type": "MCQ", "q": "Your company summarized a large dataset for your region. You need to compare results from urban and rural communities. What is the fastest way to obtain this information?", "options": ["Review data from neighboring regions", "Aggregate the data", "Disaggregate the data", "Collect a new data sample"], "a": 2 },
    { "id": 5, "type": "DND", "q": "Complete the data organization scenarios by dragging the correct method to each situation.", "code": "<div style='display:grid; grid-template-columns: 1fr auto; gap:15px; align-items:center;'><div>Arrange distributed items from highest to lowest</div> [target1]<div>Display only items greater than 500</div> [target2]<div>Extract a subset of the dataset containing only the 'Sales' column</div> [target3]</div>", "options": ["Sorting", "Filtering", "Slicing", "Truncating", "Transposing", "Appending"], "a": ["Sorting", "Filtering", "Slicing"] },
    { "id": 6, "type": "MCQ", "q": "As part of an ETL process, which action represents Transformation?", "options": ["Changing data from summary level to detailed level", "Converting data from one data type or structure to another", "Retrieving data from multiple sources into one destination", "Importing a percentage of rows from the source data"], "a": 1 },
    { "id": 8, "type": "MCQ", "q": "A file named coursesdata contains structured data. Which programming language could be used to read this data and import it into a database?", "options": ["SQL", "Python", "HTML", "CSS"], "a": 1 }
]

# Module 3: 8 Questions
DATA3 = [
    { "id": 1, "type": "MCQ", "q": "A retail manager notices a sudden 20% spike in weekend umbrella sales. Which analysis should the manager use to find the <b>root cause</b> for this unexpected increase?", "options": ["Predictive Analysis", "Diagnostic Analysis", "Descriptive Analysis", "Prescriptive Analysis"], "a": 1 },
    { "id": 2, "type": "TF", "q": "A hospital uses historical patient records to forecast how many beds will be needed on Friday nights.<br><br><b>True or False:</b> This is an example of Predictive Analysis.", "options": ["This is an example of Predictive Analysis."], "a": [True] },
    { "id": 3, "type": "DD", "q": "A travel app processes millions of raw GPS coordinates to suggest nearby hotels to tourists.<br><br>The process of converting these raw coordinates into <b>meaningful suggestions</b> is called generating ______.<br><br>Select the correct answer from the dropdown.", "code": "Raw GPS Data \u2192 [b1]", "options": ["Noise", "Insights", "Errors", "Files"], "a": ["Insights"] },
    { "id": 4, "type": "MCQ", "q": "Which of the following activities is <b>NOT</b> an example of data analysis?", "options": ["Identifying patterns in student test scores", "Predicting customer churn based on usage", "Manually changing the font color of a final report", "Summarizing monthly sales by region"], "a": 2 },
    { "id": 5, "type": "MTF", "q": "Match the type of analysis with the <b>real-world scenario</b> it represents.<br><span style='font-size:12px;font-style:italic;'>Note: You will receive partial credit for each correct match.</span>", "options": ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"], "labels": ["Calculating last month's revenue", "Finding why profit dropped in June", "Estimating next year's market growth", "Recommending an automated budget cut"], "a": { "Descriptive": "Calculating last month's revenue", "Diagnostic": "Finding out why profit dropped in June", "Predictive": "Estimating next year's market growth", "Prescriptive": "Recommending an automated budget cut" } },
    { "id": 6, "type": "MCQ", "q": "An e-commerce manager prints a weekly report showing exactly how many laptops were sold in every city.<br><br>Which type of analysis does this report represent?", "options": ["Predictive", "Prescriptive", "Descriptive", "Diagnostic"], "a": 2 },
    { "id": 7, "type": "TF", "q": "<b>True or False:</b> Diagnostic analysis is primarily used to forecast whether a company's stock price will rise next month.", "options": ["Diagnostic analysis forecasts future outcomes."], "a": [False] },
    { "id": 8, "type": "DD", "q": "A logistics company uses historical traffic trends to <b>estimate</b> exactly when a package will arrive at its destination.<br><br>Predictive analysis is used here to ______ the arrival time.", "code": "Predictive Analysis \u2192 [b1] delivery times", "options": ["Ignore", "Predict", "Delete", "Store"], "a": ["Predict"] }
]

# Module 4: 8 Questions
DATA4 = [
    { "id": 1, "type": "MCQ", "q": "<strong>Chart Selection:</strong> Which visual chart is generally the best choice for displaying continuous trends over a period of time?", "options": ["Bar Chart", "Line Chart", "Pie Chart", "Scatter Plot"], "a": 1 },
    { "id": 2, "type": "MTF", "q": "<strong>Visualization Best Practices:</strong> Match the chart type to its most effective use case.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", "options": ["Pie Chart", "Bar Chart", "Scatter Plot", "Waterfall Chart"], "labels": ["Showing parts of a whole (percentages)", "Comparing nominal categorical data", "Showing correlation between two continuous variables", "Visualizing cumulative profit/cost changes"], "a": {"Pie Chart": "Showing parts of a whole (percentages)", "Bar Chart": "Comparing nominal categorical data", "Scatter Plot": "Showing correlation between two continuous variables", "Waterfall Chart": "Visualizing cumulative profit/cost changes"} },
    { "id": 3, "type": "DD", "q": "<strong>Dashboard Design:</strong> You are designing a professional executive dashboard.<br><br>When graphing a distribution of age groups, you should use a [b1]. To highlight the 'vital few' categories that cause 80% of customer complaints, use a [b2].", "options": [["Histogram", "Line Chart", "Pie Chart"], ["Pareto Chart", "Scatter Plot", "Radar Chart"]], "a": ["Histogram", "Pareto Chart"] },
    { "id": 4, "type": "TF", "q": "<strong>Clarity & Aesthetics:</strong> Evaluate the following visual design principles.<br><br>Select True or False for each statement.", "options": ["3D effects in bar charts significantly improve data readability.", "The '30-Second Insight' rule means a dashboard should take 30 seconds to load.", "A misleading axis (e.g., not starting at zero) can distort the perception of a Bar chart."], "a": [False, False, True] },
    { "id": 5, "type": "MCQ2", "q": "<strong>Data Storytelling:</strong> Which two elements are critical for effective data storytelling in a corporate presentation?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", "options": ["Using clear, descriptive titles and labels", "Hiding the axes to make the chart look minimalist", "Using contrasting colors to draw attention to key insights", "Applying a different font for every single data point"], "a": [0, 2] },
    { "id": 6, "type": "MCQ", "q": "<strong>Data Hierarchy:</strong> What does the 'Ink-to-Data Ratio' rule essentially recommend?", "options": ["Use as much ink as possible to make the chart bold.", "Remove non-essential visual clutter (borders, gridlines) to focus on the data.", "Only print charts using black ink.", "Ensure all data labels are underlined."], "a": 1 },
    { "id": 7, "type": "SHORT", "q": "<strong>Pareto Principle:</strong> The Pareto chart is based on the rule that what percentage of effects come from 20% of the causes? (Enter the number alone)", "a": "80" },
    { "id": 8, "type": "TF", "q": "<strong>Advanced Charts:</strong> Consider specialized visual tools.<br><br>Select True or False for each statement.", "options": ["A Heatmap uses color gradients to represent data intensity or density.", "Box plots are primarily used to show categorical sales margins.", "A Scatter Plot requires two numerical axes."], "a": [True, False, True] }
]

# Module 5: 25 Questions
DATA5 = [
    {"id": 1, "type": "MCQ", "q": "What is an example of machine learning in predictive analysis?", "options": ["Thermostat adjusts temperature based on time", "Streaming service recommends movies based on past viewing", "Vehicle shows maintenance warning", "Computer goes to sleep at low battery"], "a": 1},
    {"id": 2, "type": "MCQ2", "q": "Which two data points are NON-sensitive PII?", "options": ["Bank account number", "Medical records", "Date of birth", "Job title"], "a": [2, 3]},
    {"id": 3, "type": "TF", "q": "<strong>Data Mining:</strong> Select True or False for each statement.", "options": ["Data mining is used to find anomalies", "Data mining summarizes raw data from large datasets", "Data mining reviews underlying details in a table"], "a": [True, True, False]},
    {"id": 4, "type": "MTF", "q": "<strong>Types of Analysis:</strong> Match each analysis type with the question it answers.", "options": ["What happened?", "Why did it happen?", "What will happen?", "What should we do next?", "Is there enough evidence to draw a conclusion?"], "labels": ["Descriptive Analysis", "Diagnostic Analysis", "Predictive Analysis", "Prescriptive Analysis", "Hypothesis Testing"], "a": {"What happened?": "Descriptive Analysis", "Why did it happen?": "Diagnostic Analysis", "What will happen?": "Predictive Analysis", "What should we do next?": "Prescriptive Analysis", "Is there enough evidence to draw a conclusion?": "Hypothesis Testing"}},
    {"id": 5, "type": "MCQ2", "q": "While handling PII during a project, which three principles should you follow?", "options": ["Limit PII usage to necessary data", "Remove PII after analysis", "Retain PII for future use", "Request all available PII", "Track PII usage"], "a": [0, 1, 4]},
    {"id": 6, "type": "MCQ", "q": "Before analysis, what should you do to validate the dataset?", "options": ["Analyze purchase trends", "Calculate statistics", "Verify date ranges and values", "Create aggregations"], "a": 2},
    {"id": 7, "type": "MCQ", "q": "How is machine learning used in hiring?", "options": ["Defines job qualifications", "Predicts applicant performance using past data", "Converts data format", "Queries database"], "a": 1},
    {"id": 8, "type": "MCQ", "q": "You run a t-test with \u03b1 = 0.01. Which p-value leads to rejecting the null hypothesis?", "options": ["0.001", "0.011", "0.09", "0.10"], "a": 0},
    {"id": 9, "type": "MCQ", "q": "To test differences in student scores:", "options": ["Use medians, p > 0.05 \u2192 significant", "Use means, p < 0.05 \u2192 significant", "Use medians, p < 0.05 \u2192 significant", "Use means, p > 0.05 \u2192 significant"], "a": 1},
    {"id": 10, "type": "MCQ", "q": "What is the goal of laws like GDPR, FERPA, HIPAA?", "options": ["Tax companies", "Protect personal data", "Share industry data", "Protect companies"], "a": 1},
    {"id": 11, "type": "MCQ", "q": "How can you protect PII while still linking data later?", "options": ["Remove PII completely", "Convert to numeric values", "Use pseudonymization", "Shuffle data randomly"], "a": 2},
    {"id": 12, "type": "MCQ", "q": "Which level gives the most precise analysis?", "options": ["Years", "Months", "Weeks", "Days", "Hours"], "a": 4},
    {"id": 13, "type": "MCQ", "q": "Which concept allows detailed data exploration?", "options": ["Granularity", "Completeness", "Interpretability", "Transparency"], "a": 0},
    {"id": 14, "type": "TF", "q": "<strong>Machine Learning:</strong> Select True or False for each statement.", "options": ["ML can predict rain using patterns", "ML can predict exam results without historical data", "ML can detect fraud based on patterns"], "a": [True, False, True]},
    {"id": 15, "type": "MCQ", "q": "Where is AI most useful?", "options": ["Predicting vehicle maintenance", "Calculating averages", "Recording sales", "Interpreting small datasets"], "a": 0},
    {"id": 16, "type": "MCQ2", "q": "Which of the following are conceptually related to AI?", "options": ["Automation", "Machine Learning", "Stakeholder Mapping", "Cost-benefit Analysis"], "a": [0, 1]},
    {"id": 17, "type": "MCQ2", "q": "Why is small sample data risky for statistical modeling?", "options": ["Not representative", "Less precise", "Faster analysis", "Easier collection"], "a": [0, 1]},
    {"id": 18, "type": "MCQ", "q": "You accept only supporting evidence and ignore opposing data. This is:", "options": ["Motivated reasoning", "Confirmation bias", "Sampling bias", "Anchoring bias"], "a": 1},
    {"id": 19, "type": "MCQ", "q": "You collect survey data only from local gyms to assess an entire city's health. This is:", "options": ["Anchoring bias", "Confirmation bias", "Sampling bias", "Motivated bias"], "a": 2},
    {"id": 20, "type": "MCQ", "q": "If \u03b1 = 0.05 and p = 0.017:", "options": ["Accept H\u2080", "Reject H\u2080", "Modify H\u2080", "Fail to reject H\u2080"], "a": 1},
    {"id": 21, "type": "MCQ2", "q": "Select three standard applications of Machine Learning:", "options": ["Time series analysis", "Anomaly detection", "Data classification", "Small dataset analysis", "Singular events"], "a": [0, 1, 2]},
    {"id": 22, "type": "MCQ2", "q": "Which standard tools can transform XML data into Excel format?", "options": ["Python", "Power Query", "Microsoft Word", "JSON"], "a": [0, 1]},
    {"id": 23, "type": "MCQ", "q": "A global social media platform tracks millions of clicks, likes, and interactions every minute. What type of data is this?", "options": ["Continuous data", "Imputed data", "Qualitative data", "Big Data"], "a": 3},
    {"id": 24, "type": "MCQ", "q": "You construct a theory and then only search for evidence that aligns with your desired outcome. This is:", "options": ["Motivated reasoning", "Anchoring bias", "Sampling bias", "Affinity bias"], "a": 0},
    {"id": 25, "type": "MCQ", "q": "What is the primary, overarching goal of data protection laws?", "options": ["Share data openly", "Protect personal data", "Tax companies", "Reduce storage"], "a": 1}
]

def inject():
    path = r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Anchor point: the end of "ex10" block.
    # Look for "ex10": [ ... ]
    match = re.search(r'"ex10":\s*\[.*?\n\s+\]', content, re.DOTALL)
    if not match:
        print("Could not find ex10 block.")
        return

    end_pos = match.end()
    
    # We want to remove any existing data1-5 that might follow ex10 before adding ours,
    # OR we can just find where quizData ends and append there.
    # Actually, the file ends with "};". Let's just find the last "};" and insert before it.
    
    # But wait, we want to stay within the quizData object.
    # Let's find the closing brace of quizData.
    last_brace_pos = content.rfind("};")
    if last_brace_pos == -1:
        last_brace_pos = content.rfind("}")
    
    if last_brace_pos == -1:
        print("Could not find closing brace.")
        return

    # To be safe, let's remove any existing "data1" through "data5" keys from the content first.
    # This is tricky with regex. Let's instead just rebuild the suffix.
    
    prefix = content[:end_pos]
    
    # Check if there are other things after ex10 that we want to keep (like mockdata1)
    suffix = content[end_pos:]
    
    # Remove existing data1-5 keys from suffix
    for i in range(1, 6):
        pattern = r',\s*"data' + str(i) + r'":\s*\[.*?\]'
        suffix = re.sub(pattern, "", suffix, flags=re.DOTALL)
        # Also try without quotes
        pattern = r',\s*data' + str(i) + r':\s*\[.*?\]'
        suffix = re.sub(pattern, "", suffix, flags=re.DOTALL)

    # Now build the new data blocks
    new_blocks = ""
    for name, data in [("data1", DATA1), ("data2", DATA2), ("data3", DATA3), ("data4", DATA4), ("data5", DATA5)]:
        json_data = json.dumps(data, indent=8)
        new_blocks += f',\n    "{name}": {json_data}'

    # Reassemble
    # Insert new_blocks immediately after ex10's closing bracket
    final_content = prefix + new_blocks + suffix
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print("Injection successful.")

if __name__ == "__main__":
    inject()
