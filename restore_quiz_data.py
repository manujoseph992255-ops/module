import re

def restore():
    path = r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the end of ex10.
    # From my research, ex10 ends with "    ]" and then the next line should be "data4" or similar.
    # Actually, I know ex10 ends at line 1665 in the original.
    # Let's find "ex10": [ ... ] block closing bracket.
    
    match = re.search(r'"ex10":\s*\[.*?\n\s+\]', content, re.DOTALL)
    if not match:
        print("Could not find ex10 block.")
        return

    prefix = content[:match.end()]
    
    # The original data4, data5, and mockdata1 content (re-created from previous turn research)
    original_suffix = """
,    "data4": [
        { id: 1, type: "MCQ", q: "<strong>Chart Selection:</strong> Which visual chart is generally the best choice for displaying continuous trends over a period of time?", options: ["Bar Chart", "Line Chart", "Pie Chart", "Scatter Plot"], a: 1 },
        { id: 2, type: "MTF", q: "<strong>Visualization Best Practices:</strong> Match the chart type to its most effective use case.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Pie Chart", "Bar Chart", "Scatter Plot", "Waterfall Chart"], labels: ["Showing parts of a whole (percentages)", "Comparing nominal categorical data", "Showing correlation between two continuous variables", "Visualizing cumulative profit/cost changes"], a: {"Pie Chart": "Showing parts of a whole (percentages)", "Bar Chart": "Comparing nominal categorical data", "Scatter Plot": "Showing correlation between two continuous variables", "Waterfall Chart": "Visualizing cumulative profit/cost changes"} },
        { id: 3, type: "DD", q: "<strong>Dashboard Design:</strong> You are designing a professional executive dashboard.<br><br>When graphing a distribution of age groups, you should use a [b1]. To highlight the 'vital few' categories that cause 80% of customer complaints, use a [b2].", options: [["Histogram", "Line Chart", "Pie Chart"], ["Pareto Chart", "Scatter Plot", "Radar Chart"]], a: ["Histogram", "Pareto Chart"] },
        { id: 4, type: "TF", q: "<strong>Clarity & Aesthetics:</strong> Evaluate the following visual design principles.<br><br>Select True or False for each statement.", options: ["3D effects in bar charts significantly improve data readability.", "The '30-Second Insight' rule means a dashboard should take 30 seconds to load.", "A misleading axis (e.g., not starting at zero) can distort the perception of a Bar chart."], a: [false, false, true] },
        { id: 5, type: "MCQ2", q: "<strong>Data Storytelling:</strong> Which two elements are critical for effective data storytelling in a corporate presentation?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["Using clear, descriptive titles and labels", "Hiding the axes to make the chart look minimalist", "Using contrasting colors to draw attention to key insights", "Applying a different font for every single data point"], a: [0, 2] },
        { id: 6, type: "MCQ", q: "<strong>Data Hierarchy:</strong> What does the 'Ink-to-Data Ratio' rule essentially recommend?", options: ["Use as much ink as possible to make the chart bold.", "Remove non-essential visual clutter (borders, gridlines) to focus on the data.", "Only print charts using black ink.", "Ensure all data labels are underlined."], a: 1 },
        { id: 7, type: "SHORT", q: "<strong>Pareto Principle:</strong> The Pareto chart is based on the rule that what percentage of effects come from 20% of the causes? (Enter the number alone)", a: "80" },
        { id: 8, type: "TF", q: "<strong>Advanced Charts:</strong> Consider specialized visual tools.<br><br>Select True or False for each statement.", options: ["A Heatmap uses color gradients to represent data intensity or density.", "Box plots are primarily used to show categorical sales margins.", "A Scatter Plot requires two numerical axes."], a: [true, false, true] }
    ],
    "data5": [
        { id: 1, type: "MCQ", q: "<strong>Data Applications:</strong> Which of the following is an example of an algorithm applying Predictive Analysis in the real world?", options: ["A thermostat that adjusts temperature based on the current time.", "A streaming service recommending movies based on your viewing history.", "A car dashboard displaying the current tire pressure.", "A cash register printing a receipt."], a: 1 },
        { id: 2, type: "TF", q: "<strong>Data Ethics:</strong> Evaluate the following statements on data ethics and security.<br><br>Select True or False for each statement.", options: ["Data bias in training sets can lead to discriminatory AI models.", "Anonymizing data means to attach a person's explicit name to their records.", "Transparency involves hiding how user data is collected and processed."], a: [true, false, false] },
        { id: 3, type: "MTF", q: "<strong>Ethics Principles:</strong> Match the data governance concept with its correct definition.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Privacy", "Security", "Compliance", "Bias Mitigation"], labels: ["Respecting user consent and data rights", "Protecting data from unauthorized access or breaches", "Adhering to legal standards like GDPR or CCPA", "Ensuring models represent diverse populations fairly"], a: {"Privacy": "Respecting user consent and data rights", "Security": "Protecting data from unauthorized access or breaches", "Compliance": "Adhering to legal standards like GDPR or CCPA", "Bias Mitigation": "Ensuring models represent diverse populations fairly"} },
        { id: 4, type: "DD", q: "<strong>Regulations:</strong> You are setting up user data policies for a European application.<br><br>You must ensure strict adherence to the [b1] framework, which protects consumer privacy and data rights in the EU. For California residents, you would reference [b2].", options: [["GDPR", "HIPAA", "SOX"], ["CCPA", "HIPAA", "PCI-DSS"]], a: ["GDPR", "CCPA"] },
        { id: 5, type: "MCQ2", q: "<strong>Data Security:</strong> Which two practices are standard methods for protecting sensitive data?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["Data Encryption", "Posting data to a public GitHub repo", "Role-Based Access Control (RBAC)", "Storing passwords in plain text"], a: [0, 2] },
        { id: 6, type: "MCQ", q: "<strong>Algorithmic Impact:</strong> What is a potential negative consequence of using historical data that contains human prejudices to train a machine learning model?", options: ["Algorithmic Bias", "Data Encryption", "Data Normalization", "Increased Data Velocity"], a: 0 },
        { id: 7, type: "TF", q: "<strong>Ethics in Action:</strong> Review the scenarios concerning data rights.<br><br>Select True or False for each statement.", options: ["Users generally have the right to request deletion of their personal data under GDPR.", "Data Security and Data Privacy are exactly the same concept.", "A company is ethically bound to protect user data even if it has no legal obligation."], a: [true, false, true] },
        { id: 8, type: "SHORT", q: "<strong>Acronym Check:</strong> What does the European privacy regulation acronym GDPR stand for?<br><span style='font-size: 15px; font-style: italic;'>Enter the exact term.</span>", a: "General Data Protection Regulation" }
    ],
    "mockdata1": [
    {
        "id": 1,
        "type": "MCQ",
        "q": "<strong>Data Fundamentals:</strong> What is raw data that has been processed and turned into something meaningful called?",
        "options": [
            "Information",
            "Metadata",
            "Storage",
            "Draft"
        ],
        "a": 0
    },
    {
        "id": 2,
        "type": "TF",
        "q": "<strong>Data Types:</strong> Consider the nature of qualitative and quantitative data.<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "options": [
            "Qualitative data focuses on numbers and measurements.",
            "Blood type represents categorical qualitative data.",
            "Quantitative data can be discrete or continuous.",
            "The number of children in a household is continuous data."
        ],
        "a": [
            false,
            true,
            true,
            false
        ]
    },
    {
        "id": 3,
        "type": "DD",
        "q": "<strong>Structured vs Unstructured:</strong> You are evaluating different data sources for an enterprise data warehouse.<br><br>Complete the classification by selecting the correct option from the drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "An email body text is [b1] data, while a SQL database table containing customer names is [b2] data.",
        "options": [
            [
                "Structured",
                "Semi-structured",
                "Unstructured"
            ],
            [
                "Structured",
                "Semi-structured",
                "Unstructured"
            ]
        ],
        "a": [
            "Unstructured",
            "Structured"
        ]
    },
    {
        "id": 4,
        "type": "MTF",
        "q": "<strong>Data Attributes:</strong> Match the numeric data type scale with its correct example.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>",
        "options": [
            "Nominal Data",
            "Ordinal Data",
            "Interval Data",
            "Ratio Data"
        ],
        "labels": [
            "Hair Color",
            "Customer Satisfaction (1-5)",
            "Temperature in Celsius",
            "Annual Salary"
        ],
        "a": {
            "Nominal Data": "Hair Color",
            "Ordinal Data": "Customer Satisfaction (1-5)",
            "Interval Data": "Temperature in Celsius",
            "Ratio Data": "Annual Salary"
        }
    },
    {
        "id": 5,
        "type": "MCQ2",
        "q": "<strong>Big Data:</strong> Which two of the following statements accurately describe the defining characteristics (the 'V's) of Big Data?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>",
        "options": [
            "Volume refers to the massive scale of data generated.",
            "Variety means Big Data only consists of numerical records.",
            "Velocity refers to the speed at which data is generated and processed.",
            "Veracity indicates that all Big Data is 100% accurate and clean."
        ],
        "a": [
            0,
            2
        ]
    },
    {
        "id": 6,
        "type": "SHORT",
        "q": "<strong>Metadata:</strong> Provide the term that is commonly defined as 'data about other data'.<br><span style='font-size: 15px; font-style: italic;'>Enter the exact term.</span>",
        "a": "Metadata"
    },
    {
        "id": 7,
        "type": "TF",
        "q": "<strong>Reviewing Data Formats:</strong> Evaluate the following statements regarding data formats.<br><br>Select True or False for each statement.",
        "options": [
            "Audio files are examples of unstructured data.",
            "A spreadsheet with rows and columns is unstructured data.",
            "Metadata helps organize and locate data without opening the file itself."
        ],
        "a": [
            true,
            false,
            true
        ]
    },
    {
        "id": 8,
        "type": "MCQ",
        "q": "<strong>Data Categories:</strong> Which of the following is an example of Discrete Quantitative data?",
        "options": [
            "The exact weight of an apple (e.g., 152.4g)",
            "The number of employees in a company",
            "The eye color of the employees",
            "The temperature recorded in an office"
        ],
        "a": 1
    },
    {
        "id": 9,
        "type": "MCQ",
        "q": "<strong>Data Preparation:</strong> Which process involves identifying and removing errors, duplicates, and inconsistencies from a dataset?",
        "options": [
            "Data Mining",
            "Data Cleaning",
            "Data Storage",
            "Data Visualization"
        ],
        "a": 1
    },
    {
        "id": 10,
        "type": "DD",
        "q": "<strong>Data Life Cycle:</strong> You are organizing the phases of the Data Analytics Life Cycle. The typical first step after defining the objective is to [b1] the data, and after cleaning, the next immediate step is to [b2] the data.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "options": [
            [
                "Collect",
                "Analyze",
                "Visualize",
                "Archive"
            ],
            [
                "Collect",
                "Analyze",
                "Visualize",
                "Archive"
            ]
        ],
        "a": [
            "Collect",
            "Analyze"
        ]
    },
    {
        "id": 11,
        "type": "MTF",
        "q": "<strong>Life Cycle Phases:</strong> Match each action to the correct phase of the Data Life Cycle.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>",
        "options": [
            "Data Collection",
            "Data Wrangling",
            "Data Analysis",
            "Data Visualization"
        ],
        "labels": [
            "Gathering records from an API",
            "Converting date formats and merging tables",
            "Applying statistical models",
            "Creating a dashboard chart"
        ],
        "a": {
            "Data Collection": "Gathering records from an API",
            "Data Wrangling": "Converting date formats and merging tables",
            "Data Analysis": "Applying statistical models",
            "Data Visualization": "Creating a dashboard chart"
        }
    },
    {
        "id": 12,
        "type": "TF",
        "q": "<strong>Data Quality:</strong> You are reviewing a newly acquired dataset.<br><br>For each statement below, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "options": [
            "Missing values can skew analysis results if not handled.",
            "Data visualization should always precede data cleaning.",
            "ETL stands for Extract, Transform, Load."
        ],
        "a": [
            true,
            false,
            true
        ]
    },
    {
        "id": 13,
        "type": "MCQ2",
        "q": "<strong>Wrangling Techniques:</strong> What are two common activities performed during Data Wrangling?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>",
        "options": [
            "Filtering out unwanted rows",
            "Presenting findings to executives",
            "Joining multiple datasets together",
            "Publishing data to the public internet"
        ],
        "a": [
            0,
            2
        ]
    },
    {
        "id": 14,
        "type": "SHORT",
        "q": "<strong>Exploratory Analysis:</strong> What does the acronym EDA stand for in the context of the data life cycle?<br><span style='font-size: 15px; font-style: italic;'>Enter the exact three words.</span>",
        "a": "Exploratory Data Analysis"
    },
    {
        "id": 15,
        "type": "MCQ",
        "q": "<strong>Phase Priorities:</strong> Why is data cleaning considered one of the most critical steps in the data life cycle?",
        "options": [
            "It is the fastest step in the process.",
            "It ensures that the insights generated are accurate and reliable.",
            "It automatically generates predictive dashboards.",
            "It replaces the need for data collection."
        ],
        "a": 1
    },
    {
        "id": 16,
        "type": "TF",
        "q": "<strong>Analysis Flow:</strong> Evaluate standard practices in a professional data environment.<br><br>Select True or False for each statement.",
        "options": [
            "Data visualization is primarily used to store data efficiently.",
            "Deploying models is often the final actionable step of advanced predictive life cycles.",
            "Data governance policies dictate how data is managed throughout its life cycle."
        ],
        "a": [
            false,
            true,
            true
        ]
    },
    {
        "id": 17,
        "type": "MCQ",
        "q": "<strong>Analytical Modes:</strong> Which type of analysis utilizes historical data to answer the question 'Why did it happen?'",
        "options": [
            "Descriptive",
            "Diagnostic",
            "Predictive",
            "Prescriptive"
        ],
        "a": 1
    },
    {
        "id": 18,
        "type": "MTF",
        "q": "<strong>Analysis Mapping:</strong> Match the type of analysis to the fundamental question it answers.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>",
        "options": [
            "Descriptive Analysis",
            "Diagnostic Analysis",
            "Predictive Analysis",
            "Prescriptive Analysis"
        ],
        "labels": [
            "What happened?",
            "Why did it happen?",
            "What is likely to happen?",
            "What action should we take?"
        ],
        "a": {
            "Descriptive Analysis": "What happened?",
            "Diagnostic Analysis": "Why did it happen?",
            "Predictive Analysis": "What is likely to happen?",
            "Prescriptive Analysis": "What action should we take?"
        }
    },
    {
        "id": 19,
        "type": "DD",
        "q": "<strong>Applying Frameworks:</strong> You are advising a hospital on reducing patient wait times.<br><br>Reviewing last month's average wait time is an example of [b1] analysis. Building a model to schedule doctors based on forecasted future patient arrivals is an example of [b2] analysis.",
        "options": [
            [
                "Descriptive",
                "Prescriptive",
                "Diagnostic"
            ],
            [
                "Predictive",
                "Descriptive",
                "Prescriptive"
            ]
        ],
        "a": [
            "Descriptive",
            "Prescriptive"
        ]
    },
    {
        "id": 20,
        "type": "TF",
        "q": "<strong>Analysis Traits:</strong> Evaluate the characteristics of the four main types of data analysis.<br><br>Select True or False for each statement.",
        "options": [
            "Descriptive analysis uses machine learning to forecast trends.",
            "Predictive analysis guarantees the exact future outcome.",
            "Prescriptive analysis often involves optimization algorithms."
        ],
        "a": [
            false,
            false,
            true
        ]
    },
    {
        "id": 21,
        "type": "MCQ2",
        "q": "<strong>Predictive Modeling:</strong> Which two techniques are most commonly associated with Predictive Analytics?<br><span style='font-size: 15px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>",
        "options": [
            "Machine Learning Models",
            "Counting Total Monthly Sales",
            "Statistical Forecasting",
            "Generating PDF Invoices"
        ],
        "a": [
            0,
            2
        ]
    },
    {
        "id": 22,
        "type": "MCQ",
        "q": "<strong>Real-World Usage:</strong> A retail dashboard shows that sales dropped by 15% last quarter. The analyst discovers this was due to a supply chain disruption. What type of analysis did the analyst perform to find the cause?",
        "options": [
            "Descriptive Analysis",
            "Diagnostic Analysis",
            "Prescriptive Analysis",
            "Predictive Analysis"
        ],
        "a": 1
    },
    {
        "id": 23,
        "type": "SHORT",
        "q": "<strong>Terminology:</strong> Providing recommendations on how to handle upcoming market trends falls under which phase of analysis? (Examples: Descriptive, Diagnostic, Predictive, Prescriptive)",
        "a": "Prescriptive"
    },
    {
        "id": 24,
        "type": "TF",
        "q": "<strong>Business Value:</strong> Assess the value curve of analytics.<br><br>Select True or False for each statement.",
        "options": [
            "Prescriptive analysis typically offers higher business value than descriptive reporting.",
            "Diagnostic analysis looks purely at future trends.",
            "Descriptive analytics is usually the foundational starting point for organizations."
        ],
        "a": [
            true,
            false,
            true
        ]
    },
    {
        "id": 25,
        "type": "MCQ",
        "q": "<strong>Correlation Analysis:</strong> Refer to the scatter plot below showing the relationship between Variable X and Variable Y. What type of correlation is demonstrated?",
        "options": [
            "Positive Correlation",
            "Negative Correlation",
            "No Correlation",
            "Exponential Growth"
        ],
        "a": 0,
        "chart": {
            "type": "scatter",
            "data": {
                "datasets": [
                    {
                        "label": "Variable X vs Variable Y",
                        "data": [
                            {
                                "x": 10,
                                "y": 20
                            },
                            {
                                "x": 20,
                                "y": 10
                            },
                            {
                                "x": 30,
                                "y": 32
                            },
                            {
                                "x": 40,
                                "y": 30
                            },
                            {
                                "x": 50,
                                "y": 38
                            },
                            {
                                "x": 60,
                                "y": 19
                            },
                            {
                                "x": 70,
                                "y": 44
                            },
                            {
                                "x": 80,
                                "y": 55
                            }
                        ],
                        "backgroundColor": "#4472c4",
                        "pointRadius": 8
                    }
                ]
            },
            "options": {
                "responsive": true,
                "maintainAspectRatio": false,
                "scales": {
                    "x": {
                        "title": {
                            "display": true,
                            "text": "Variable X",
                            "font": {
                                "weight": "bold",
                                "size": 16
                            }
                        },
                        "min": 0,
                        "max": 90,
                        "ticks": {
                            "stepSize": 10
                        }
                    },
                    "y": {
                        "title": {
                            "display": true,
                            "text": "Variable Y",
                            "font": {
                                "weight": "bold",
                                "size": 16
                            }
                        },
                        "min": 0,
                        "max": 60,
                        "ticks": {
                            "stepSize": 10
                        }
                    }
                },
                "plugins": {
                    "legend": {
                        "display": false
                    }
                }
            }
        }
    }
]
};"""
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(prefix + original_suffix)
    print("Restore successful.")

if __name__ == "__main__":
    restore()
