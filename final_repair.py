import json
import re

# Correct Data 5 Questions (from previous turn)
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

# Placeholders for data1-4 (to be filled or improved later)
# Using generic but relevant data analysis questions
DATA1 = [{"id": 1, "type": "MCQ", "q": "What is raw data that has been processed and turned into something meaningful called?", "options": ["Information", "Metadata", "Storage", "Draft"], "a": 0}]
DATA2 = [{"id": 1, "type": "MCQ", "q": "Which process involves removing errors and inconsistencies from a dataset?", "options": ["Data Wrangling", "Data Cleaning", "Data Mining", "Data Storage"], "a": 1}]
DATA3 = [{"id": 1, "type": "MCQ", "q": "Which type of analysis explains 'Why did it happen?'", "options": ["Descriptive", "Diagnostic", "Predictive", "Prescriptive"], "a": 1}]
DATA4 = [{"id": 1, "type": "MCQ", "q": "Which chart is best for showing a trend over time?", "options": ["Bar Chart", "Line Chart", "Pie Chart", "Histogram"], "a": 1}]

def repair_quiz_data():
    with open("quiz_data.js", "r", encoding="utf-8") as f:
        content = f.read()

    # Find the end of ex10. We expect "ex10": [ ... ]
    # We'll use a regex that matches the ex10 block and stops at its closing bracket.
    # Identifying ex10 closing point:
    match = re.search(r'"ex10":\s*\[.*?\n\s+\]', content, re.DOTALL)
    if not match:
         # Try without quotes
         match = re.search(r'ex10:\s*\[.*?\n\s+\]', content, re.DOTALL)
    
    if match:
        end_pos = match.end()
        # Truncate content at the end of ex10
        new_content = content[:end_pos]
        
        # Now append the data arrays
        data_blocks = [
            ("data1", DATA1),
            ("data2", DATA2),
            ("data3", DATA3),
            ("data4", DATA4),
            ("data5", DATA5)
        ]
        
        for key, data in data_blocks:
            json_str = json.dumps(data, indent=8).replace('}', '    }')
            new_content += f',\n\n    "{key}": {json_str}'
            
        new_content += "\n};\n"
        
        with open("quiz_data.js", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully repaired quiz_data.js and added data1-data5.")
    else:
        print("Error: Could not find ex10 block to use as anchor.")

if __name__ == "__main__":
    repair_quiz_data()
