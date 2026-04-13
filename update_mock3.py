import json
import re

mock3_questions = [
    {
        "id": 1,
        "type": "DD",
        "q": "You are developing a Python program that stores log information in a file. The program must:<br>• Open a file named log.txt<br>• Append new messages without deleting existing data<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "file = open(\"log.txt\", \"[b1]\")\nfile.[b2](\"System started\")\nfile.close()",
        "options": [["r", "w", "a"], ["read", "write", "append"]],
        "a": ["a", "write"]
    },
    {
        "id": 2,
        "type": "MCQ",
        "q": "You are reviewing code written by a developer that checks whether a number exists in a list.<br><br>What will the program output?",
        "code": "numbers = [10, 20, 30, 40]\nprint(20 in numbers)",
        "options": ["False", "True", "20", "Error"],
        "a": 1
    },
    {
        "id": 3,
        "type": "DND",
        "q": "You are developing a program that processes numbers from 1 to 10. The program must:<br>• Stop the loop immediately when the number 7 is encountered.<br><br>Complete the code by moving the correct code segment into the blank.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct placement.</span>",
        "code": "for i in range(1, 11):\n    if i == 7:\n        [target1]\n    print(i)",
        "options": ["break", "continue", "pass"],
        "a": ["break"]
    },
    {
        "id": 4,
        "type": "DD",
        "q": "You are creating a program that stores student marks. The program must:<br>• Add a new mark to the list<br>• Sort the list<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "marks = [70, 85, 60]\nmarks.[b1](90)\nmarks.[b2]()\nprint(marks)",
        "options": [["append", "insert", "sort", "sorted"], ["append", "insert", "sort", "sorted"]],
        "a": ["append", "sort"]
    },
    {
        "id": 5,
        "type": "TF",
        "q": "You are reviewing the following Python code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "code": "score = 75\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Fail\")",
        "options": ["The program prints Pass when score is 75.", "The program prints Fail when score is below 50.", "The else block executes when the condition is False."],
        "a": [True, True, True]
    },
    {
        "id": 6,
        "type": "DD",
        "q": "You are developing a Python program that reads data from a file. The program must:<br>• Check if the file records.txt exists.<br>• Read and print its contents if it exists.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "import os\nif [b1](\"records.txt\"):\n    file = open(\"records.txt\",\"r\")\n    print(file.[b2]())\n    file.close()",
        "options": [["os.path.exists", "os.exists", "os.path.check"], ["read", "write", "open"]],
        "a": ["os.path.exists", "read"]
    },
    {
        "id": 7,
        "type": "DD",
        "q": "You are creating a program that generates a random number between 1 and 100.<br><br>Complete the code by selecting the correct option.",
        "code": "import random\nnum = random.[b1](1,100)\nprint(num)",
        "options": ["randint", "rand", "range", "random"],
        "a": ["randint"]
    },
    {
        "id": 8,
        "type": "MCQ",
        "q": "You are reviewing the following code:<br><br>What is the output?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["1 2 3", "0 1 2", "0 1 2 3", "1 2"],
        "a": 1
    },
    {
        "id": 9,
        "type": "TF",
        "q": "You are reviewing the following code:<br><br>Select True or False.",
        "code": "x = 10\nif x > 5:\n    print(\"High\")\nelse:\n    print(\"Low\")",
        "options": ["The program prints High.", "The program prints Low when x = 10.", "The if block runs when the condition is True."],
        "a": [True, False, True]
    },
    {
        "id": 10,
        "type": "DD",
        "q": "You are writing a program that checks whether a number exists in a list.<br><br>Complete the code.",
        "code": "numbers = [5,10,15]\nif 10 [b1] numbers:\n    print(\"Found\")",
        "options": ["in", "is", "==", "not"],
        "a": ["in"]
    },
    {
        "id": 11,
        "type": "SHORT",
        "q": "Review the following code:<br><br>How many lines of output will be printed?<br><span style='font-size: 12px; font-style: italic;'>Enter the number as an integer.</span>",
        "code": "for i in range(2):\n    for j in range(2):\n        print(i,j)",
        "a": "4"
    },
    {
        "id": 12,
        "type": "DD",
        "q": "You are creating a loop that prints numbers until 5.<br><br>Complete the code.",
        "code": "x = 1\n[b1] x <= 5:\n    print(x)\n    x += 1",
        "options": ["if", "for", "while"],
        "a": ["while"]
    },
    {
        "id": 13,
        "type": "MCQ",
        "q": "You are teaching a new colleague how to build reusable components in Python.<br><br>Which keyword defines a function?",
        "options": ["function", "define", "def", "func"],
        "a": 2
    },
    {
        "id": 14,
        "type": "SHORT",
        "q": "You are reviewing a basic math utility function in a financial application.<br><br>What is the output of this code?",
        "code": "def add(a,b):\n    return a+b\nprint(add(3,7))",
        "a": "10"
    },
    {
        "id": 15,
        "type": "TF",
        "q": "You are implementing a default greeting for a user profile system.<br><br>Review the following code and select True or False for each statement.",
        "code": "def greet(name=\"Student\"):\n    print(\"Hello\",name)",
        "options": ["greet() prints Hello Student", "greet(\"Ana\") prints Hello Ana", "Default parameters must be declared first."],
        "a": [True, True, False]
    },
    {
        "id": 16,
        "type": "MCQ",
        "q": "You are developing a script that processes color themes from the command line.<br>Program execution:<br><code>python script.py Red Blue</code><br><br>What is the output?",
        "code": "import sys\nprint(sys.argv[1])",
        "options": ["script.py", "Red", "Blue", "Error"],
        "a": 1
    },
    {
        "id": 17,
        "type": "DD",
        "q": "You are building a text parser that needs to extract the first letter of a company name.<br><br>Complete the code that prints the first character of a string.",
        "code": "text = \"Python\"\nprint(text[[b1]])",
        "options": ["0", "1", "-1", "2"],
        "a": ["0"]
    },
    {
        "id": 18,
        "type": "TF",
        "q": "You are reviewing the coding standards for a new team project regarding code documentation.<br><br>Select True or False for each statement.",
        "code": "# calculate total\ntotal = 10 + 5",
        "options": ["Comments are ignored during execution.", "Comments improve code readability.", "Comments change program output."],
        "a": [True, True, False]
    },
    {
        "id": 19,
        "type": "MCQ",
        "q": "You are debugging an automated billing formula that calculates a total including flat fees and multipliers.<br><br>Evaluate the following expression. What is the output?",
        "code": "print(10 + 5 * 2)",
        "options": ["30", "20", "25", "15"],
        "a": 1
    },
    {
        "id": 20,
        "type": "DD",
        "q": "You are updating a data export tool that must overwrite previous export files with new data.<br><br>Complete the code to overwrite file contents.",
        "code": "file = open(\"data.txt\",\"[b1]\")\nfile.write(\"Hello\")\nfile.close()",
        "options": ["r", "a", "w"],
        "a": ["w"]
    },
    {
        "id": 21,
        "type": "MCQ",
        "q": "You are developing a lottery application that selects a winner from a list of predefined grades.<br><br>What does this program do?",
        "code": "import random\nprint(random.choice([\"A\",\"B\",\"C\"]))",
        "options": ["Prints entire list", "Prints random element from list", "Sorts list", "Removes element"],
        "a": 1
    },
    {
        "id": 22,
        "type": "TF",
        "q": "You are working on a logic controller that compares sensor threshold values.<br><br>Select True or False for each statement.",
        "code": "print(10 > 5)",
        "options": ["Output is True", "Result type is Boolean", "Comparison operators produce numbers."],
        "a": [True, True, False]
    },
    {
        "id": 23,
        "type": "SHORT",
        "q": "You are developing an inventory system and need to determine the total number of items currently in stock.<br><br>What is the printed answer?",
        "code": "nums = [1,2,3,4,5]\nprint(len(nums))",
        "a": "5"
    },
    {
        "id": 24,
        "type": "DD",
        "q": "You are writing a program to extract the name from a JSON payload containing student records.<br><br>Complete the code.",
        "code": "student = {\"name\":\"Rahul\",\"age\":20}\nprint(student[\"[b1]\"])",
        "options": ["name", "Rahul", "age", "student"],
        "a": ["name"]
    },
    {
        "id": 25,
        "type": "TF",
        "q": "You are designing a data deduplication routine and have decided to use Sets.<br><br>Select True or False for each statement concerning Sets.",
        "options": ["Sets allow duplicate values.", "Sets store unique elements.", "Sets are unordered."],
        "a": [False, True, True]
    },
    {
        "id": 26,
        "type": "MCQ",
        "q": "You are storing fixed configuration coordinates that must not be changed during execution. You choose to use a tuple.<br><br>Which statement describes tuples?",
        "options": ["Mutable sequence", "Immutable sequence", "Unordered structure", "Dynamic list"],
        "a": 1
    },
    {
        "id": 27,
        "type": "TF",
        "q": "You are investigating memory optimization techniques and reviewing variable assignments.<br><br>Select True or False for each statement.",
        "code": "a = 10\nb = 10\nprint(a is b)",
        "options": ["Output may be True", "is checks memory identity", "== checks value equality."],
        "a": [True, True, True]
    },
    {
        "id": 28,
        "type": "DD",
        "q": "You are building a robust calculation engine that must safely handle unexpected mathematical operations without crashing.<br><br>Complete the code.",
        "code": "try:\n    print(10/0)\n[b1] ZeroDivisionError:\n    print(\"Cannot divide\")",
        "options": ["except", "catch", "handle"],
        "a": ["except"]
    },
    {
        "id": 29,
        "type": "TF",
        "q": "You are finalizing a database connection script that must guarantee cleanup processes execute.<br><br>Select True or False concerning the finally block.",
        "options": ["finally always executes", "finally runs only when error occurs", "finally runs even if no exception happens."],
        "a": [True, False, True]
    },
    {
        "id": 30,
        "type": "DD",
        "q": "You are writing automated tests for a data processing pipeline to strictly ensure variable types.<br><br>Complete the test statement.",
        "code": "self.[b1](5, int)",
        "options": ["assertTrue", "assertEqual", "assertIsInstance", "assertIn"],
        "a": ["assertIsInstance"]
    },
    {
        "id": 31,
        "type": "MCQ",
        "q": "You are auditing a complex pricing algorithm to ensure operations are calculated in the correct order.<br><br>What is the output?",
        "code": "print((10+5)*2)",
        "options": ["20", "30", "25", "15"],
        "a": 1
    },
    {
        "id": 32,
        "type": "MTF",
        "q": "You are developing a string sanitizer that extracts specific substrings from a filename.<br><br>Match the sliced outputs:",
        "code": "text = \"pythonprogram\"",
        "options": ["text[:6]", "text[6:]"],
        "labels": ["python", "program", "prog", "pythonp"],
        "a": {"text[:6]": "python", "text[6:]": "program"}
    },
    {
        "id": 33,
        "type": "SHORT",
        "q": "You are writing a task scheduler that stops processing tasks early if a certain threshold is met.<br><br>How many numbers are printed?",
        "code": "for i in range(5):\n    if i == 3:\n        break\n    print(i)",
        "a": "3"
    },
    {
        "id": 34,
        "type": "DD",
        "q": "You are conducting a code review and spot an assignment inside a conditional check.<br><br>Correct the operator.",
        "code": "if x [b1] 5:\n    print(\"Hello\")",
        "options": ["==", "=", "!=", "="],
        "a": ["=="]
    },
    {
        "id": 35,
        "type": "DD",
        "q": "You are building a queue management system and need to add a new customer ID to the end of a list.<br><br>Complete the code.",
        "code": "numbers = [1,2,3]\nnumbers.[b1](4)",
        "options": ["append", "add", "insert", "extend"],
        "a": ["append"]
    },
    {
        "id": 36,
        "type": "MCQ2",
        "q": "You are developing a log reading utility that extracts historical data safely.<br><br>Which two code segments correctly read file content? (Choose 2.)",
        "options": [
            "with open(\"data.txt\",\"r\") as f:\n    print(f.read())",
            "f=open(\"data.txt\",\"r\")\nprint(f.read())\nf.close()",
            "open(\"data.txt\").write()",
            "open(\"data.txt\").append()"
        ],
        "a": [0, 1]
    },
    {
        "id": 37,
        "type": "MCQ",
        "q": "You are verifying a complex gate condition in a security access script.<br><br>What is the output?",
        "code": "print(True or False)",
        "options": ["True", "False", "None", "Error"],
        "a": 0
    },
    {
        "id": 38,
        "type": "DD",
        "q": "You are creating a game mechanic that spawns an item between specific coordinate limits.<br><br>Complete the code.",
        "code": "import random\nprint(random.[b1](1,10))",
        "options": ["randrange", "rand", "random", "choose"],
        "a": ["randrange"]
    },
    {
        "id": 39,
        "type": "MCQ",
        "q": "You are developing an automated maintenance script that removes temporary files.<br><br>Which function deletes a file?",
        "options": ["os.delete()", "os.remove()", "os.erase()", "os.clean()"],
        "a": 1
    },
    {
        "id": 40,
        "type": "SHORT",
        "q": "You are calculating a running total of scores but must skip the calculation for a specific round.<br><br>What is the output?",
        "code": "total = 0\nfor i in range(1,6):\n    if i == 3:\n        continue\n    total += i\nprint(total)",
        "a": "12"
    }
]

file_path = "c:\\Users\\kj anand\\Downloads\\Quiz DD\\quiz_data.js"
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Generate the JSON string for the questions
questions_json = json.dumps(mock3_questions, indent=4)

# Replace "mock3": [] with "mock3": [ ... ]
pattern = r'"mock3":\s*\[\]'
replacement = f'"mock3": {questions_json}'
new_content = re.sub(pattern, lambda _: replacement, content)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_content)

print("Mock 3 updated successfully.")
