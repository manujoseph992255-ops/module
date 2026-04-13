import json
import re

DATA5_JSON = [
    {
        "id": "q1",
        "type": "mcq",
        "question": "1. What is an example of machine learning in predictive analysis?",
        "options": [
            "A. Thermostat adjusts temperature based on time",
            "B. Streaming service recommends movies based on past viewing",
            "C. Vehicle shows maintenance warning",
            "D. Computer goes to sleep at low battery"
        ],
        "answer": "B. Streaming service recommends movies based on past viewing"
    },
    {
        "id": "q2",
        "type": "multiselect",
        "question": "2. Which two data points are NON-sensitive PII?",
        "options": [
            "Bank account number",
            "Medical records",
            "Date of birth",
            "Job title"
        ],
        "answer": ["Date of birth", "Job title"]
    },
    {
        "id": "q3",
        "type": "truefalse",
        "question": "3. True/False Statements on Data Mining",
        "statements": [
            { "text": "Data mining is used to find anomalies", "answer": True },
            { "text": "Data mining summarizes raw data from large datasets", "answer": True },
            { "text": "Data mining reviews underlying details in a table", "answer": False }
        ]
    },
    {
        "id": "q4",
        "type": "match",
        "question": "4. Match each analysis type with the question it answers:",
        "pairs": [
            { "left": "What happened?", "right": "Descriptive Analysis" },
            { "left": "Why did it happen?", "right": "Diagnostic Analysis" },
            { "left": "What will happen?", "right": "Predictive Analysis" },
            { "left": "What should we do next?", "right": "Prescriptive Analysis" },
            { "left": "Is there enough evidence to draw a conclusion?", "right": "Hypothesis Testing" }
        ],
        "options": [
            "Descriptive Analysis",
            "Diagnostic Analysis",
            "Predictive Analysis",
            "Prescriptive Analysis",
            "Hypothesis Testing"
        ]
    },
    {
        "id": "q5",
        "type": "multiselect",
        "question": "5. While handling PII during a project, which three principles should you follow?",
        "options": [
            "Limit PII usage to necessary data",
            "Remove PII after analysis",
            "Retain PII for future use",
            "Request all available PII",
            "Track PII usage"
        ],
        "answer": ["Limit PII usage to necessary data", "Remove PII after analysis", "Track PII usage"]
    },
    { "id": "q6", "type": "mcq", "question": "6. Before analysis, what should you do to validate the dataset?", "options": [ "A. Analyze purchase trends", "B. Calculate statistics", "C. Verify date ranges and values", "D. Create aggregations" ], "answer": "C. Verify date ranges and values" },
    { "id": "q7", "type": "mcq", "question": "7. How is machine learning used in hiring?", "options": [ "A. Defines job qualifications", "B. Predicts applicant performance using past data", "C. Converts data format", "D. Queries database" ], "answer": "B. Predicts applicant performance using past data" },
    { "id": "q8", "type": "mcq", "question": "8. You run a t-test with α = 0.01. Which p-value leads to rejecting the null hypothesis?", "options": ["A. 0.001", "B. 0.011", "C. 0.09", "D. 0.10"], "answer": "A. 0.001" },
    { "id": "q9", "type": "mcq", "question": "9. To test differences in student scores:", "options": ["A. Use medians, p > 0.05 → significant", "B. Use means, p < 0.05 → significant", "C. Use medians, p < 0.05 → significant", "D. Use means, p > 0.05 → significant"], "answer": "B. Use means, p < 0.05 → significant" },
    { "id": "q10", "type": "mcq", "question": "10. What is the goal of laws like GDPR, FERPA, HIPAA?", "options": ["A. Tax companies", "B. Protect personal data", "C. Share industry data", "D. Protect companies"], "answer": "B. Protect personal data" },
    { "id": "q11", "type": "mcq", "question": "11. How can you protect PII while still linking data later?", "options": ["A. Remove PII completely", "B. Convert to numeric values", "C. Use pseudonymization", "D. Shuffle data randomly"], "answer": "C. Use pseudonymization" },
    { "id": "q12", "type": "mcq", "question": "12. Which level gives the most precise analysis?", "options": ["A. Years", "B. Months", "C. Weeks", "D. Days", "E. Hours"], "answer": "E. Hours" },
    { "id": "q13", "type": "mcq", "question": "13. Which concept allows detailed data exploration?", "options": ["A. Granularity", "B. Completeness", "C. Interpretability", "D. Transparency"], "answer": "A. Granularity" },
    {
        "id": "q14",
        "type": "truefalse",
        "question": "14. True/False Statements on Machine Learning",
        "statements": [
            { "text": "ML can predict rain using patterns", "answer": True },
            { "text": "ML can predict exam results without historical data", "answer": False },
            { "text": "ML can detect fraud based on patterns", "answer": True }
        ]
    },
    { "id": "q15", "type": "mcq", "question": "15. Where is AI most useful?", "options": ["A. Predicting vehicle maintenance", "B. Calculating averages", "C. Recording sales", "D. Interpreting small datasets"], "answer": "A. Predicting vehicle maintenance" },
    {
        "id": "q16",
        "type": "multiselect",
        "question": "16. Which are related to AI?",
        "options": ["Automation", "Machine Learning", "Stakeholder Mapping", "Cost-benefit Analysis"],
        "answer": ["Automation", "Machine Learning"]
    },
    {
        "id": "q17",
        "type": "multiselect",
        "question": "17. Why is small sample data risky?",
        "options": ["Not representative", "Less precise", "Faster analysis", "Easier collection"],
        "answer": ["Not representative", "Less precise"]
    },
    { "id": "q18", "type": "mcq", "question": "18. You accept only supporting evidence and ignore opposing data. This is:", "options": ["A. Motivated reasoning", "B. Confirmation bias", "C. Sampling bias", "D. Anchoring bias"], "answer": "B. Confirmation bias" },
    { "id": "q19", "type": "mcq", "question": "19. You collect data only from gyms. This is:", "options": ["A. Anchoring bias", "B. Confirmation bias", "C. Sampling bias", "D. Motivated bias"], "answer": "C. Sampling bias" },
    { "id": "q20", "type": "mcq", "question": "20. If α = 0.05 and p = 0.017:", "options": ["A. Accept H₀", "B. Reject H₀", "C. Modify H₀", "D. Fail to reject H₀"], "answer": "B. Reject H₀" },
    {
        "id": "q21",
        "type": "multiselect",
        "question": "21. Select three ML uses:",
        "options": ["Time series analysis", "Anomaly detection", "Data classification", "Small dataset analysis", "Singular events"],
        "answer": ["Time series analysis", "Anomaly detection", "Data classification"]
    },
    {
        "id": "q22",
        "type": "multiselect",
        "question": "22. Which tools can transform XML data into Excel format?",
        "options": ["Python", "Power Query", "Microsoft Word", "JSON"],
        "answer": ["Python", "Power Query"]
    },
    { "id": "q23", "type": "mcq", "question": "23. A social media platform tracks clicks, likes, and interactions. What type of data is this?", "options": ["A. Continuous data", "B. Imputed data", "C. Qualitative data", "D. Big Data"], "answer": "D. Big Data" },
    { "id": "q24", "type": "mcq", "question": "24. You only accept evidence supporting your belief. This is:", "options": ["A. Motivated reasoning", "B. Anchoring bias", "C. Sampling bias", "D. Affinity bias"], "answer": "A. Motivated reasoning" },
    { "id": "q25", "type": "mcq", "question": "25. What is one goal of data protection laws?", "options": ["A. Share data openly", "B. Protect personal data", "C. Tax companies", "D. Reduce storage"], "answer": "B. Protect personal data" }
]

def update_quiz_data():
    with open("quiz_data.js", "r", encoding="utf-8") as f:
        content = f.read()
    
    # We find the final closing brace of the quizData object
    data5_str = "    ,\n    data5: " + json.dumps(DATA5_JSON, indent=8).replace('}', '    }') + "\n"
    
    if content.strip().endswith('};'):
        content = content.strip()[:-2] + data5_str + "};\n"
        with open("quiz_data.js", "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully appended data5 to the end of quizData.")
    else:
        print("Error: quiz_data.js doesn't end with }; as expected.")

if __name__ == "__main__":
    update_quiz_data()
