import json
import re

mock2_questions = [
    # FROM MOCK 1 (Questions 1-20)
    {
        "id": 1,
        "type": "DD",
        "q": "You are developing a Python application that requires unit testing. You need to:<br>• Import the correct module.<br>• Verify that a value is an instance of a specific class.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "[b1] unittest\nclass TestExample(unittest.TestCase):\n    def test_instance(self):\n        self.[b2](5, int)\n\nif __name__ == \"__main__\":\n    unittest.main()",
        "options": [["define", "import", "include", "using"], ["assertEqual", "assertTrue", "assertIsInstance", "assertIn"]],
        "a": ["import", "assertIsInstance"]
    },
    {
        "id": 2,
        "type": "MCQ",
        "q": "You are part of a development team maintaining a large Python project. You need to add notes in your code so other developers can understand its purpose and logic.<br><br>What is the correct way to add a single-line comment in Python?",
        "options": ["Use /* comment */", "Use <!-- comment -->", "Use # comment", "Use // comment"],
        "a": 2
    },
    {
        "id": 3,
        "type": "DD",
        "q": "You are writing a program that assigns a random room number. The program must:<br>• Ensure that the room number is not already assigned.<br>• Generate a new random number if it is already in use.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>",
        "code": "import random\nroomsAssigned = []\nroom_number = 1\nwhile room_number in roomsAssigned:\n    [b1]\nroomsAssigned.append(room_number)",
        "options": ["room_number = random.randint(1, 50)", "room_number += 1", "random.choice(room_number)"],
        "a": ["room_number = random.randint(1, 50)"]
    },
    {
        "id": 4,
        "type": "DD",
        "q": "A company requires a program that:<br>• Opens a file named report.txt.<br>• Writes the text \"End of listing\" into the file.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "file = open(\"report.txt\", \"[b1]\")\nfile.[b2](\"End of listing\")\nfile.close()",
        "options": [["r", "w", "a"], ["write", "read", "append"]],
        "a": ["w", "write"]
    },
    {
        "id": 5,
        "type": "DD",
        "q": "You are writing a program that:<br>• Prompts the user for a number.<br>• Converts the input to an integer.<br>• Handles invalid input without crashing.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>",
        "code": "while True:\n    try:\n        x = int(input(\"Enter a number: \"))\n        break\n    [b1] ValueError:\n        print(\"Invalid number.\")",
        "options": ["except", "catch", "error", "handle"],
        "a": ["except"]
    },
    {
        "id": 6,
        "type": "DD",
        "q": "You are developing a file-processing program. Before opening a file, the program must:<br>• Verify that the file exists.<br>• Read and display its contents if it exists.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "import os\nif [b1](\"data.txt\"):\n    file = open(\"data.txt\", \"r\")\n    print(file.[b2]())\n    file.close()",
        "options": [["os.path.exists", "os.exists", "os.path.check"], ["read", "write", "open"]],
        "a": ["os.path.exists", "read"]
    },
    {
        "id": 7,
        "type": "DND",
        "q": "You are building a program that prints all prime numbers between 2 and 20. The program must:<br>• Loop through numbers from 2 to 20.<br>• Determine whether each number is prime.<br>• Stop checking a number once a divisor is found.<br><br>Complete the code by moving the appropriate code segment into the correct location.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct placement.</span>",
        "code": "for p in range(2, 21):\n    is_prime = True\n    for i in range(2, p):\n        if p % i == 0:\n            is_prime = False\n            [target1]\n    if is_prime:\n        print(p)",
        "options": ["break", "continue", "pass"],
        "a": ["break"]
    },
    {
        "id": 8,
        "type": "DD",
        "q": "You are comparing two lists to determine whether they contain the same values in the same order.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>",
        "code": "numList = [1, 2, 3]\nalphaList = [\"a\", \"b\", \"c\"]\nif [b1]:\n    print(\"Equal\")\nelse:\n    print(\"Not Equal\")",
        "options": ["numList == alphaList", "numList is alphaList", "numList != alphaList", "numList in alphaList"],
        "a": ["numList == alphaList"]
    },
    {
        "id": 9,
        "type": "MCQ",
        "q": "You are creating a console-based application. You use the following statement:<br><br><div class='code-snippet' style='margin:0;'>data = input()</div><br>What does this statement do?",
        "options": ["Creates an HTML input field", "Prompts the user to enter text in the console", "Displays system input devices", "Opens a message dialog"],
        "a": 1
    },
    {
        "id": 10,
        "type": "TF",
        "q": "You are reviewing the following function.<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "code": "def grosspay(hours=40, rate=25, pieces=0, piecerate=0, salary=0):\n    if pieces > 0:\n        return pieces * piecerate\n    if salary > 0:\n        pass\n    if hours > 40:\n        overtime = (hours - 40) * (1.5 * rate)\n        return overtime + (40 * rate)\n    else:\n        return hours * rate",
        "options": ["Calling grosspay() results in a syntax error.", "Calling grosspay(salary=50000) returns None.", "Calling grosspay(pieces=500, piecerate=4) returns 2000."],
        "a": [False, False, True]
    },
    {
        "id": 11,
        "type": "DD",
        "q": "You are writing a program that repeatedly accepts user input. The program must:<br>• Prompt the user to enter a word.<br>• Display the number of characters in the word.<br>• Continue until the user enters \"QUIT\".<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>",
        "code": "word = input(\"Enter a word (or QUIT to exit): \")\n[b1] word != \"QUIT\":\n    print(len(word))\n    word = input(\"Enter a word (or QUIT to exit): \")",
        "options": ["if", "for", "while"],
        "a": ["while"]
    },
    {
        "id": 12,
        "type": "TF",
        "q": "You are reviewing the following conditional statements.<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "code": "if num1 == num2:\n    print(\"Equal\")\nif num1 < num2:\n    print(\"Less\")\nif num1 > num2:\n    print(\"Greater\")\nif num2 == num1:\n    print(\"Same\")",
        "options": ["The first print statement executes only when the values are equal.", "The second print statement executes only when num1 is less than num2.", "The third print statement executes only when num1 is greater than num2.", "The final condition is logically redundant."],
        "a": [True, True, True, True]
    },
    {
        "id": 13,
        "type": "DD",
        "q": "You are developing a function that counts how many words in a list contain a specific letter.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "def count_letter(letter, word_list):\n    count = 0\n    for [b1]:\n        if [b2]:\n            count += 1\n    return count",
        "options": [["word in word_list", "letter in word", "word_list in letter", "word == letter"], ["word in word_list", "letter in word", "word_list in letter", "word == letter"]],
        "a": ["word in word_list", "letter in word"]
    },
    {
        "id": 14,
        "type": "DND",
        "q": "You are creating a guessing game. The program must:<br>• Generate a random number between 1 and 10.<br>• Allow the user up to three guesses.<br>• Stop immediately if the correct guess is entered.<br><br>Complete the code by moving the appropriate code segments into the correct locations.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct placement.</span>",
        "code": "from random import randint\ntarget = randint(1, 10)\nchance = 1\n[target1]\n    guess = int(input(\"Guess: \"))\n    if guess == target:\n        print(\"Correct!\")\n        [target2]\n    [target3]",
        "options": ["break", "chance += 1", "while chance <= 3:"],
        "a": ["while chance <= 3:", "break", "chance += 1"]
    },
    {
        "id": 15,
        "type": "DD",
        "q": "You are developing a function to calculate admission fees. The program must:<br>• Assign a free rate for children under 5.<br>• Assign a discounted rate for students aged 5 to 17.<br>• Assign a higher rate for non-students aged 5 to 17.<br>• Assign a standard adult rate otherwise.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "elif age >= 5 and age <= 17 and not school:\n    rate = [b1]\nelse:\n    rate = [b2]",
        "options": [["20", "50", "10"], ["20", "50", "10"]],
        "a": ["20", "50"]
    },
    {
        "id": 16,
        "type": "MCQ",
        "q": "You are reviewing the following script.<br>The program is executed using the following command:<br><code>python script.py Apple Banana Mango</code><br><br>What is the output?",
        "code": "import sys\nprint(sys.argv[2])",
        "options": ["script.py", "Apple", "Banana", "Mango"],
        "a": 2
    },
    {
        "id": 17,
        "type": "DD",
        "q": "You are creating a function that reverses a string.<br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>",
        "code": "def reverse_name(backward_name):\n    forward_name = \"\"\n    length = len(backward_name) - 1\n    while length >= 0:\n        forward_name += [b1]\n        length -= 1\n    return forward_name",
        "options": ["backward_name[length]", "backward_name", "forward_name[length]"],
        "a": ["backward_name[length]"]
    },
    {
        "id": 18,
        "type": "TF",
        "q": "You are reviewing the following function.<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "code": "def calc_power(x, y):\n    comment = \"# return the value\"\n    return x ** y  # exponent",
        "options": ["The string in line 2 is treated as a comment.", "The function returns x raised to the power y.", "The inline comment does not affect execution.", "Removing the comment changes the output."],
        "a": [False, True, True, False]
    },
    {
        "id": 19,
        "type": "MCQ",
        "q": "You are evaluating the following expression.<br><br>What is the value of answer?",
        "code": "answer = (9 % 4 * 10) // 2 ** 3 + 4",
        "options": ["5", "6", "4", "3"],
        "a": 0
    },
    {
        "id": 20,
        "type": "MCQ",
        "q": "You are reviewing the following function.<br><br>An error occurs when executing this code. What is the most likely cause?",
        "code": "def read_file(file):\n    if os.path.isfile(file):\n        data = open(file, 'r')\n        for line in data:\n            print(line)",
        "options": ["isfile requires two parameters", "os module is not imported", "The path must be absolute", "open requires a different mode"],
        "a": 1
    },

    # FROM MOCK 3 / NEW (Questions 21-40) - These were the first 20 of Mock 3
    {
        "id": 21,
        "type": "DD",
        "q": "You are developing a Python program that stores log information in a file. The program must:<br>• Open a file named log.txt<br>• Append new messages without deleting existing data<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "file = open(\"log.txt\", \"[b1]\")\nfile.[b2](\"System started\")\nfile.close()",
        "options": [["r", "w", "a"], ["read", "write", "append"]],
        "a": ["a", "write"]
    },
    {
        "id": 22,
        "type": "MCQ",
        "q": "You are reviewing code written by a developer that checks whether a number exists in a list.<br><br>What will the program output?",
        "code": "numbers = [10, 20, 30, 40]\nprint(20 in numbers)",
        "options": ["False", "True", "20", "Error"],
        "a": 1
    },
    {
        "id": 23,
        "type": "DND",
        "q": "You are developing a program that processes numbers from 1 to 10. The program must:<br>• Stop the loop immediately when the number 7 is encountered.<br><br>Complete the code by moving the correct code segment into the blank.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct placement.</span>",
        "code": "for i in range(1, 11):\n    if i == 7:\n        [target1]\n    print(i)",
        "options": ["break", "continue", "pass"],
        "a": ["break"]
    },
    {
        "id": 24,
        "type": "DD",
        "q": "You are creating a program that stores student marks. The program must:<br>• Add a new mark to the list<br>• Sort the list<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "marks = [70, 85, 60]\nmarks.[b1](90)\nmarks.[b2]()\nprint(marks)",
        "options": [["append", "insert", "sort", "sorted"], ["append", "insert", "sort", "sorted"]],
        "a": ["append", "sort"]
    },
    {
        "id": 25,
        "type": "TF",
        "q": "You are reviewing the following Python code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>",
        "code": "score = 75\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Fail\")",
        "options": ["The program prints Pass when score is 75.", "The program prints Fail when score is below 50.", "The else block executes when the condition is False."],
        "a": [True, True, True]
    },
    {
        "id": 26,
        "type": "DD",
        "q": "You are developing a Python program that reads data from a file. The program must:<br>• Check if the file records.txt exists.<br>• Read and print its contents if it exists.<br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        "code": "import os\nif [b1](\"records.txt\"):\n    file = open(\"records.txt\",\"r\")\n    print(file.[b2]())\n    file.close()",
        "options": [["os.path.exists", "os.exists", "os.path.check"], ["read", "write", "open"]],
        "a": ["os.path.exists", "read"]
    },
    {
        "id": 27,
        "type": "DD",
        "q": "You are creating a program that generates a random number between 1 and 100.<br><br>Complete the code by selecting the correct option.",
        "code": "import random\nnum = random.[b1](1,100)\nprint(num)",
        "options": ["randint", "rand", "range", "random"],
        "a": ["randint"]
    },
    {
        "id": 28,
        "type": "MCQ",
        "q": "You are reviewing the following code:<br><br>What is the output?",
        "code": "for i in range(3):\n    print(i)",
        "options": ["1 2 3", "0 1 2", "0 1 2 3", "1 2"],
        "a": 1
    },
    {
        "id": 29,
        "type": "TF",
        "q": "You are reviewing the following code:<br><br>Select True or False.",
        "code": "x = 10\nif x > 5:\n    print(\"High\")\nelse:\n    print(\"Low\")",
        "options": ["The program prints High.", "The program prints Low when x = 10.", "The if block runs when the condition is True."],
        "a": [True, False, True]
    },
    {
        "id": 30,
        "type": "DD",
        "q": "You are writing a program that checks whether a number exists in a list.<br><br>Complete the code.",
        "code": "numbers = [5,10,15]\nif 10 [b1] numbers:\n    print(\"Found\")",
        "options": ["in", "is", "==", "not"],
        "a": ["in"]
    },
    {
        "id": 31,
        "type": "SHORT",
        "q": "Review the following code:<br><br>How many lines of output will be printed?<br><span style='font-size: 12px; font-style: italic;'>Enter the number as an integer.</span>",
        "code": "for i in range(2):\n    for j in range(2):\n        print(i,j)",
        "a": "4"
    },
    {
        "id": 32,
        "type": "DD",
        "q": "You are creating a loop that prints numbers until 5.<br><br>Complete the code.",
        "code": "x = 1\n[b1] x <= 5:\n    print(x)\n    x += 1",
        "options": ["if", "for", "while"],
        "a": ["while"]
    },
    {
        "id": 33,
        "type": "MCQ",
        "q": "You are teaching a new colleague how to build reusable components in Python.<br><br>Which keyword defines a function?",
        "options": ["function", "define", "def", "func"],
        "a": 2
    },
    {
        "id": 34,
        "type": "SHORT",
        "q": "You are reviewing a basic math utility function in a financial application.<br><br>What is the output of this code?",
        "code": "def add(a,b):\n    return a+b\nprint(add(3,7))",
        "a": "10"
    },
    {
        "id": 35,
        "type": "TF",
        "q": "You are implementing a default greeting for a user profile system.<br><br>Review the following code and select True or False for each statement.",
        "code": "def greet(name=\"Student\"):\n    print(\"Hello\",name)",
        "options": ["greet() prints Hello Student", "greet(\"Ana\") prints Hello Ana", "Default parameters must be declared first."],
        "a": [True, True, False]
    },
    {
        "id": 36,
        "type": "MCQ",
        "q": "You are developing a script that processes color themes from the command line.<br>Program execution:<br><code>python script.py Red Blue</code><br><br>What is the output?",
        "code": "import sys\nprint(sys.argv[1])",
        "options": ["script.py", "Red", "Blue", "Error"],
        "a": 1
    },
    {
        "id": 37,
        "type": "DD",
        "q": "You are building a text parser that needs to extract the first letter of a company name.<br><br>Complete the code that prints the first character of a string.",
        "code": "text = \"Python\"\nprint(text[[b1]])",
        "options": ["0", "1", "-1", "2"],
        "a": ["0"]
    },
    {
        "id": 38,
        "type": "TF",
        "q": "You are reviewing the coding standards for a new team project regarding code documentation.<br><br>Select True or False for each statement.",
        "code": "# calculate total\ntotal = 10 + 5",
        "options": ["Comments are ignored during execution.", "Comments improve code readability.", "Comments change program output."],
        "a": [True, True, False]
    },
    {
        "id": 39,
        "type": "MCQ",
        "q": "You are debugging an automated billing formula that calculates a total including flat fees and multipliers.<br><br>Evaluate the following expression. What is the output?",
        "code": "print(10 + 5 * 2)",
        "options": ["30", "20", "25", "15"],
        "a": 1
    },
    {
        "id": 40,
        "type": "DD",
        "q": "You are updating a data export tool that must overwrite previous export files with new data.<br><br>Complete the code to overwrite file contents.",
        "code": "file = open(\"data.txt\",\"[b1]\")\nfile.write(\"Hello\")\nfile.close()",
        "options": ["r", "a", "w"],
        "a": ["w"]
    }
]

file_path = "c:\\Users\\kj anand\\Downloads\\Quiz DD\\quiz_data.js"
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

questions_json = json.dumps(mock2_questions, indent=4)

pattern = r'"mock2":\s*\[\]'
replacement = f'"mock2": {questions_json}'
new_content = re.sub(pattern, lambda _: replacement, content)

with open(file_path, 'w', encoding='utf-8') as file:
    file.write(new_content)

print("Mock 2 updated successfully.")
