
        console.log("Quiz script starting...");
        function logout() {
            sessionStorage.clear();
            localStorage.removeItem('strategist_user');
            localStorage.removeItem('strategist_phone');
            localStorage.removeItem('gmail');
            localStorage.removeItem('class_code');
            window.location.href = 'login.html';
        }
        const quizData = {
                "1": [
        { id: 1, type: "MTF", q: "You are reviewing several Python expressions and must determine the data type each expression evaluates to.<br>Move the appropriate data type from the list on the left to the correct expression on the right.<br>You may use each data type once, more than once, or not at all.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["type(25 // 4)", "type(25 / 4)", "type(\"25\")", "type(25 > 4)"], labels: ["int", "float", "str", "bool"], a: { "type(25 // 4)": "int", "type(25 / 4)": "float", "type(\"25\")": "str", "type(25 > 4)": "bool" } },
        { id: 2, type: "MCQ", q: "You are evaluating the following expression:<br><br>What is the value of result?<br><span style='font-size: 12px; font-style: italic;'>Select the correct answer.</span>", code: "result = 5 + 3 * 2 ** 2", options: ["64", "17", "29", "19"], a: 1 },
        { id: 3, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "a = [10, 20, 30]\nb = [10, 20, 30]\nc = a", options: ["a == b evaluates to True.", "a is b evaluates to True.", "a is c evaluates to True.", "b is not c evaluates to True."], a: [true, false, true, true] },
        { id: 4, type: "DD", q: "You are developing a program that manages a list of product prices. The program must: • Add a new price (150) • Sort the list • Reverse the list <br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "prices = [300, 200, 400]\n# Add new price\n[b1]\n# Sort prices\n[b2]\n# Reverse prices\n[b3]", options: ["prices.append(150)", "prices.sort()", "prices.reverse()", "prices.add(150)", "prices.sorted()"], a: ["prices.append(150)", "prices.sort()", "prices.reverse()"] },
        { id: 5, type: "SHORT", q: "Evaluate the following expression:<br><br>What value is printed?<br><span style='font-size: 12px; font-style: italic;'>Enter the number as an integer.</span>", code: "value = (10 % 4 * 3) + 2 ** 2\nprint(value)", a: "10" },
        { id: 6, type: "MTF", q: "You are working with the following string:<br><br>Match each slicing expression to its result.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", code: "word = \"programming\"", options: ["word[:4]", "word[3:7]", "word[7:]"], labels: ["prog", "gram", "ming", "program"], a: { "word[:4]": "prog", "word[3:7]": "gram", "word[7:]": "ming" } },
        { id: 7, type: "MCQ", q: "You are evaluating the following code:<br><br>What is printed?", code: "nums = [5, 10, 15, 20]\nprint(10 in nums)", options: ["True", "False", "10", "Error"], a: 0 },
        { id: 8, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "x = -5\ny = +x\nz = not (x > 0)", options: ["y will store -5.", "z will store True.", "The unary + operator changes the value of x.", "The not operator returns a boolean value."], a: [true, true, false, true] },
        { id: 9, type: "MCQ", q: "You are reviewing the following code:<br><br>What happens when this code executes?", code: "data = [10, 20, 30]\nprint(data[3])", options: ["30 is printed", "None is printed", "IndexError occurs", "0 is printed"], a: 2 },
        { id: 10, type: "MCQ2", q: "You are designing a condition that must evaluate to True only if: • x is greater than 5 AND • y is less than 10 <br><br>Which two expressions meet the requirement?<br><span style='font-size: 12px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)<br>Note: You will receive partial credit for each correct answer.</span>", options: ["x > 5 and y < 10", "x > 5 or y < 10", "(x > 5) and (y < 10)", "x >= 5 and y <= 10"], a: [0, 2] }
    ],
    "2": [
        { id: 1, type: "MCQ", q: "You are writing a program that determines whether a number is positive, negative, or zero. Review the following code:<br><br>What is printed?", code: "num = -5\nif num > 0:\n    print(\"Positive\")\nelif num < 0:\n    print(\"Negative\")\nelse:\n    print(\"Zero\")", options: ["Positive", "Negative", "Zero", "Nothing"], a: 1 },
        { id: 2, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "score = 85\nif score >= 50:\n    if score >= 75:\n        print(\"Distinction\")\n    else:\n        print(\"Pass\")\nelse:\n    print(\"Fail\")", options: ["If score = 60, the output will be \"Pass\".", "If score = 40, the output will be \"Fail\".", "If score = 90, the output will be \"Distinction\".", "If score = 75, the output will be \"Pass\"."], a: [true, true, true, false] },
        { id: 3, type: "SHORT", q: "Review the following code:<br><br>How many lines of output are printed?<br><span style='font-size: 12px; font-style: italic;'>Enter the number as an integer.</span>", code: "count = 1\nwhile count <= 4:\n    print(count)\n    count += 1", a: "4" },
        { id: 4, type: "DD", q: "You are building a program that searches for a value in a list. The program must: • Loop through numbers • Stop immediately once the value 7 is found <br><br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "numbers = [2, 4, 6, 7, 8]\nfor n in numbers:\n    if n == 7:\n        print(\"Found\")\n        [b1]", options: ["break", "continue", "pass"], a: ["break"] },
        { id: 5, type: "MCQ", q: "Review the following code:<br><br>What is printed?", code: "for i in range(1, 6):\n    if i == 3:\n        continue\n    print(i)", options: ["1 2 3 4 5", "1 2 4 5", "3", "1 2 3"], a: 1 },
        { id: 6, type: "MTF", q: "You are analyzing different range() expressions.<br>Match each expression with the correct sequence produced.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["range(4)", "range(1,5)", "range(0,6,2)"], labels: ["0 1 2 3", "1 2 3 4", "0 2 4"], a: { "range(4)": "0 1 2 3", "range(1,5)": "1 2 3 4", "range(0,6,2)": "0 2 4" } },
        { id: 7, type: "MCQ2", q: "You are designing a login validation rule. The program must allow access only if: • age is 18 or older AND • has_id is True <br><br>Which two expressions meet the requirement?<br><span style='font-size: 12px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["age >= 18 and has_id", "age > 18 or has_id", "(age >= 18) and (has_id == True)", "age >= 18 or has_id == True"], a: [0, 2] },
        { id: 8, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "for i in range(3):\n    print(i)\nelse:\n    print(\"Done\")", options: ["The loop prints 0 1 2.", "\"Done\" is printed after the loop completes normally.", "The else block executes only if break is used.", "The else block is optional in a for loop."], a: [true, true, false, true] },
        { id: 9, type: "MCQ", q: "You are reviewing the following code:<br><br>What happens when this code runs?", code: "x = 1\nwhile x < 5:\n    print(x)", options: ["Prints 1 2 3 4", "Prints 1 only", "Infinite loop", "Syntax Error"], a: 2 },
        { id: 10, type: "SHORT", q: "Review the following code:<br><br>How many lines of output are printed?<br><span style='font-size: 12px; font-style: italic;'>Enter the number as an integer.</span>", code: "for i in range(2):\n    for j in range(2):\n        print(i, j)", a: "4" }
    ],
    "3": [
        { id: 1, type: "MCQ", q: "You are creating a console-based application that asks a user to enter their age.<br>Which statement correctly reads input from the console and stores it in a variable named age?", options: ["age = console.read()", "age = input()", "read(age)", "age.input()"], a: 1 },
        { id: 2, type: "DD", q: "You are writing a program that must: • Accept a number from the user • Convert it to an integer • Multiply it by 2 <br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "num = [b1](\"Enter a number: \")\nresult = num * 2\nprint(result)", options: ["int(input)", "int(input())", "input(int)", "float(input())"], a: ["int(input())"] },
        { id: 3, type: "MCQ2", q: "You are writing a billing program. The program must: • Display customer name • Display total amount • Format output as: Name: John, Total: 500 <br><br>Which two code segments correctly meet the requirement?<br><span style='font-size: 12px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["print(\"Name:\", name, \"Total:\", total)", "print(f\"Name: {name}, Total: {total}\")", "print(\"Name: {0}, Total: {1}\".format(name, total))", "print(name + total)"], a: [1, 2] },
        { id: 4, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "f = open(\"data.txt\", \"w\")\nf.write(\"Hello\")\nf.close()", options: ["If the file does not exist, it will be created.", "If the file exists, its previous contents will be overwritten.", "The file must be manually closed.", "\"w\" mode allows reading the file."], a: [true, true, true, false] },
        { id: 5, type: "MCQ", q: "You are writing a logging program.<br>Which file mode allows you to add new content to the end of a file without deleting existing content?", options: ["\"r\"", "\"w\"", "\"a\"", "\"rw\""], a: 2 },
        { id: 6, type: "DD", q: "You are developing a program that: • Opens a file in read mode • Reads all contents • Prints the contents <br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>", code: "file = open(\"info.txt\", \"[b1]\")\ndata = file.[b2]()\nprint(data)\nfile.close()", options: [["r", "w", "a"], ["read", "write", "append"]], a: ["r", "read"] },
        { id: 7, type: "MCQ", q: "You are reviewing the following code:<br><br>What is the advantage of using with in this context?", code: "with open(\"data.txt\", \"r\") as f:\n    content = f.read()", options: ["It makes the file read faster", "It automatically closes the file", "It prevents file overwriting", "It allows writing only"], a: 1 },
        { id: 8, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "import os\nif os.path.exists(\"report.txt\"):\n    print(\"File exists\")", options: ["The os module must be imported before using os.path.exists().", "The function returns True if the file exists.", "os.path.exists() deletes the file if found.", "The function can check for directories as well."], a: [true, true, false, true] },
        { id: 9, type: "SHORT", q: "Review the following script:<br>The program is executed using:<br><code>python script.py Red Blue Green</code><br><br>What is printed?", code: "import sys\nprint(sys.argv[1])", a: "Red" },
        { id: 10, type: "MCQ2", q: "You are designing a program that opens a file. The program must: • Avoid crashing if the file does not exist • Handle the error gracefully <br><br>Which two approaches meet the requirement?<br><span style='font-size: 12px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", code: "A.\ntry:\n    f = open(\"data.txt\", \"r\")\nexcept FileNotFoundError:\n    print(\"File not found\")\n\nB.\nopen(\"data.txt\")\n\nC.\nimport os\nif os.path.exists(\"data.txt\"):\n    f = open(\"data.txt\", \"r\")\n\nD.\nf = open(\"data.txt\", \"w\")", options: ["A", "B", "C", "D"], a: [0, 2] }
    ],
    "4": [
        { id: 1, type: "MCQ", q: "You are writing a Python function that calculates the area of a rectangle.<br>Which code correctly defines the function?", options: ["function area(length, width):", "def area(length, width):", "define area(length, width):", "area(length, width):"], a: 1 },
        { id: 2, type: "SHORT", q: "Review the following function:<br><br>What is printed?<br><span style='font-size: 12px; font-style: italic;'>Enter the number as an integer.</span>", code: "def multiply(a, b):\n    return a * b\n\nresult = multiply(4, 5)\nprint(result)", a: "20" },
        { id: 3, type: "TF", q: "You are reviewing the following function:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "def greet(name, message=\"Hello\"):\n    print(message, name)", options: ["Calling greet(\"John\") prints \"Hello John\".", "Calling greet(\"John\", \"Hi\") prints \"Hi John\".", "Default parameters must always be the first parameter.", "The function can be called using keyword arguments."], a: [true, true, false, true] },
        { id: 4, type: "DD", q: "You are reviewing the following function:<br>Complete the function call so that: price = 100, tax = 20 <br><br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "def calculate_price(price, tax):\n    return price + tax\n\n# Answer Area\ntotal = calculate_price([b1])", options: ["100, 20", "price=100, tax=20", "tax=20, price=100", "20, 100"], a: ["price=100, tax=20"] },
        { id: 5, type: "MCQ", q: "Review the following code:<br><br>What is printed?", code: "x = 10\ndef update():\n    x = 5\nupdate()\nprint(x)", options: ["5", "10", "None", "Error"], a: 1 },
        { id: 6, type: "DD", q: "You are documenting a function so that other developers can understand its purpose. Complete the code by selecting the correct option.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "def add(a, b):\n    [b1]\n    return a + b", options: ["\"\"\"This function adds two numbers\"\"\"", "// This function adds two numbers", "This function adds two numbers", "/* This function adds two numbers */"], a: ["\"\"\"This function adds two numbers\"\"\""] },
        { id: 7, type: "TF", q: "You are reviewing the following function:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "def check_even(num):\n    if num % 2 == 0:\n        return \"Even\"\n    return \"Odd\"", options: ["The function always returns a value.", "If num = 4, the function returns \"Even\".", "If num = 3, the function returns \"Odd\".", "Both return statements will execute for the same input."], a: [true, true, true, false] },
        { id: 8, type: "MCQ", q: "Review the following code:<br><br>What is printed?", code: "def show():\n    print(\"Hello\")\nresult = show()\nprint(result)", options: ["Hello", "Hello None", "None", "Error"], a: 2 },
        { id: 9, type: "MCQ2", q: "You are writing a function that must accept any number of numeric arguments.<br>Which two definitions correctly allow this?<br><span style='font-size: 12px; font-style: italic;'>Each correct answer presents a complete solution. (Choose 2.)</span>", options: ["def total(*numbers):", "def total(numbers):", "def total(**numbers):", "def total(a, b, *numbers):"], a: [0, 3] },
        { id: 10, type: "SHORT", q: "Review the following code:<br><br>What is printed?<br><span style='font-size: 12px; font-style: italic;'>Enter the value as a number.</span>", code: "def calculate_discount(price):\n    if price > 100:\n        return price * 0.9\n    return price\nprint(calculate_discount(120))", a: "108.0" }
    ],
    "5": [
        { id: 1, type: "MCQ", q: "You are writing a program that converts user input to an integer.<br>Which code correctly handles invalid input without crashing?", code: "A.\nx = int(input())\n\nB.\ntry:\n    x = int(input())\nexcept:\n    print(\"Invalid input\")\n\nC.\nhandle:\n    x = int(input())\n\nD.\ncatch ValueError:\n    print(\"Invalid\")", options: ["A", "B", "C", "D"], a: 1 },
        { id: 2, type: "DD", q: "You are writing a program that divides two numbers entered by the user. The program must: • Catch division by zero errors • Display \"Cannot divide by zero\" <br><br>Complete the code by selecting the correct exception type.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "try:\n    result = 10 / 0\nexcept [b1]:\n    print(\"Cannot divide by zero\")", options: ["ValueError", "ZeroDivisionError", "TypeError", "FileNotFoundError"], a: ["ZeroDivisionError"] },
        { id: 3, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "try:\n    f = open(\"data.txt\")\nexcept FileNotFoundError:\n    print(\"File not found\")\nfinally:\n    print(\"Execution completed\")", options: ["The finally block always executes.", "The finally block runs only if an exception occurs.", "The finally block runs even if no exception occurs.", "The except block runs if the file does not exist."], a: [true, false, true, true] },
        { id: 4, type: "MTF", q: "You are designing a program that handles different types of exceptions.<br>Match each exception with the scenario that causes it.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct match.</span>", options: ["Dividing a number by zero", "Converting \"abc\" to int", "Adding string and integer"], labels: ["ValueError", "TypeError", "ZeroDivisionError"], a: { "Dividing a number by zero": "ZeroDivisionError", "Converting \"abc\" to int": "ValueError", "Adding string and integer": "TypeError" } },
        { id: 5, type: "MCQ", q: "You are writing a function that must: • Raise an error if the age entered is negative. <br><br>Which code correctly raises an exception?", code: "A.\nif age < 0:\n    print(\"Invalid age\")\n\nB.\nif age < 0:\n    raise ValueError(\"Invalid age\")\n\nC.\nif age < 0:\n    except ValueError\n\nD.\nif age < 0:\n    error(\"Invalid age\")", options: ["A", "B", "C", "D"], a: 1 },
        { id: 6, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "x = 10\nassert x > 5", options: ["The assertion passes.", "An AssertionError is raised.", "If x = 3, the assertion would fail.", "assert is commonly used in testing."], a: [true, false, true, true] },
        { id: 7, type: "DD", q: "You are writing a unit test to verify that two values are equal.<br>Complete the test method by selecting the correct assertion method.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "import unittest\nclass TestMath(unittest.TestCase):\n    def test_add(self):\n        self.[b1](5, 2 + 3)", options: ["assertEqual", "assertTrue", "assertIs", "assertIn"], a: ["assertEqual"] },
        { id: 8, type: "MCQ", q: "You are reviewing the following code:<br><br>What is a potential issue with this implementation?", code: "def divide(a, b):\n    try:\n        return a / b\n    except:\n        return 0", options: ["It handles only ZeroDivisionError", "It hides all types of errors", "It causes syntax error", "It does not handle division"], a: 1 },
        { id: 9, type: "MCQ2", q: "You are designing a program that opens a file safely. The program must: • Prevent crash if file does not exist • Display an error message <br><br>Which two code segments meet the requirement? (Choose 2.)", code: "A.\ntry:\n    f = open(\"data.txt\", \"r\")\nexcept FileNotFoundError:\n    print(\"File not found\")\n\nB.\nf = open(\"data.txt\", \"r\")\n\nC.\nimport os\nif os.path.exists(\"data.txt\"):\n    f = open(\"data.txt\", \"r\")\nelse:\n    print(\"File not found\")\n\nD.\nf = open(\"data.txt\", \"w\")", options: ["A", "B", "C", "D"], a: [0, 2] },
        { id: 10, type: "SHORT", q: "Review the following code:<br><br>What is missing from this code?", code: "try\n    x = int(\"abc\")\nexcept ValueError\n    print(\"Error\")", a: ":" }
    ],
    "6": [
        { id: 1, type: "MCQ", q: "You are writing a program that uses functions from the random module.<br>Which statement correctly imports the module?", options: ["include random", "using random", "import random", "random.import()"], a: 2 },
        { id: 2, type: "DD", q: "You are developing a game that must generate a random number between 1 and 10 (inclusive).<br>Complete the code by selecting the correct option from the drop-down list.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "import random\nnumber = random.[b1](1, 10)\nprint(number)", options: ["randint", "randrange", "random", "choice"], a: ["randint"] },
        { id: 3, type: "MCQ", q: "Review the following code:<br><br>Which values can be printed?", code: "import random\nprint(random.randrange(0, 10, 2))", options: ["1, 3, 5, 7, 9", "0, 2, 4, 6, 8", "2, 4, 6, 8, 10", "0 to 10 inclusive"], a: 1 },
        { id: 4, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "import os\nif os.path.exists(\"data.txt\"):\n    print(\"File exists\")", options: ["os must be imported before using os.path.exists().", "os.path.exists() returns a boolean value.", "os.path.exists() deletes the file after checking.", "This function can check for directories as well."], a: [true, true, false, true] },
        { id: 5, type: "DD", q: "You are writing a script that must read the first command-line argument provided by the user.<br>Complete the code by selecting the correct option.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for correct selection.</span>", code: "import sys\nvalue = sys.argv[[b1]]\nprint(value)", options: ["0", "1", "2", "-1"], a: ["1"] },
        { id: 6, type: "MCQ", q: "You are writing a program that must calculate the square root of a number.<br>Which code correctly performs this operation?", code: "A.\nimport math\nprint(math.sqrt(16))\n\nB.\nimport math\nprint(math.square(16))\n\nC.\nsqrt(16)\n\nD.\nmath.root(16)", options: ["A", "B", "C", "D"], a: 0 },
        { id: 7, type: "TF", q: "You are reviewing the following code:<br><br>For each statement below, select True or False.<br><span style='font-size: 12px; font-style: italic;'>Note: You will receive partial credit for each correct answer.</span>", code: "import random as r\nprint(r.randint(1,5))", options: ["random is imported with alias r.", "r.randint(1,5) generates a random integer.", "The alias changes how the module works internally.", "Using an alias is optional."], a: [true, true, false, true] },
        { id: 8, type: "MCQ2", q: "You are building a system utility script. The script must: • Check whether a file exists • Generate a random number <br><br>Which two modules must be imported? (Choose 2.)", options: ["sys", "os", "random", "math"], a: [1, 2] },
        { id: 9, type: "MCQ", q: "You are writing a program that lists all files in the current directory.<br>Which code correctly performs this task?", code: "A.\nimport os\nprint(os.listdir())\n\nB.\nprint(list.files())\n\nC.\nimport sys\nprint(sys.files())\n\nD.\nos.files()", options: ["A", "B", "C", "D"], a: 0 },
        { id: 10, type: "SHORT", q: "Review the following code:<br><br>How many different possible outputs can this program produce?<br><span style='font-size: 12px; font-style: italic;'>Enter the number as an integer.</span>", code: "import random\nimport sys\nnumbers = [10, 20, 30, 40]\nindex = random.randint(0, 3)\nprint(numbers[index])", a: "4" }
    ],
            "mock2": [
                { id: 1, type: "DD", q: `You are developing a Python program that stores log information in a file. The program must: • Open a file named log.txt • Append new messages without deleting existing data. <br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style="font-size: 12px; font-style: italic;">Note: You will receive partial credit for each correct selection.</span>`, 
                  code: "file = open(\"log.txt\", \"[b1]\")\nfile.[b2](\"System started\")\nfile.close()", 
                  options: [["r", "w", "a"], ["read", "write", "append"]], a: ["a", "write"] },
                { id: 2, type: "MCQ", q: `You are reviewing code written by a developer that checks whether a number exists in a list.<br><br>What will the program output?<br><span style="font-size: 12px; font-style: italic;">Select the correct answer.</span>`, 
                  code: "numbers = [10, 20, 30, 40]\nprint(20 in numbers)", 
                  options: ["False", "True", "20", "Error"], a: 1 },
                { id: 3, type: "DND", q: `You are developing a program that processes numbers from 1 to 10. The program must: • Stop the loop immediately when the number 7 is encountered. <br><br>Complete the code by moving the correct code segment into the blank.<br><span style="font-size: 12px; font-style: italic;">Note: You will receive partial credit for correct placement.</span>`, 
                  code: "for i in range(1, 11):\n    if i == 7:\n        [target1]\n    print(i)", 
                  options: ["break", "continue", "pass"], a: ["break"] },
                { id: 4, type: "DD", q: `You are creating a program that stores student marks. The program must: • Add a new mark to the list • Sort the list. <br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style="font-size: 12px; font-style: italic;">Note: You will receive partial credit for each correct selection.</span>`, 
                  code: "marks = [70, 85, 60]\nmarks.[b1](90)\nmarks.[b2]()\nprint(marks)", 
                  options: [["append", "insert"], ["sort", "sorted"]], a: ["append", "sort"] },
                { id: 5, type: "TF", q: `You are reviewing the following Python code. For each statement below, select True or False.<br><span style="font-size: 12px; font-style: italic;">Note: You will receive partial credit for each correct answer.</span>`, 
                  code: "score = 75\nif score >= 50:\n    print(\"Pass\")\nelse:\n    print(\"Fail\")", 
                  options: ["The program prints Pass when score is 75.", "The program prints Fail when score is below 50.", "The else block executes when the condition is False."], a: [true, true, true] },
                { id: 6, type: "DD", q: `You are developing a Python program that reads data from a file. The program must: • Check if the file records.txt exists. • Read and print its contents if it exists. <br><br>Complete the code by selecting the correct option from each drop-down list.<br><span style="font-size: 12px; font-style: italic;">Note: You will receive partial credit for each correct selection.</span>`, 
                  code: "import os\nif [b1](\"records.txt\"):\n    file = open(\"records.txt\",\"r\")\n    print(file.[b2]())\n    file.close()", 
                  options: [["os.path.exists", "os.exists", "os.path.check"], ["read", "write", "open"]], a: ["os.path.exists", "read"] },
                { id: 7, type: "DD", q: `You are creating a program that generates a random number between 1 and 100. Complete the code by selecting the correct option.`, 
                  code: "import random\nnum = random.[b1](1,100)\nprint(num)", 
                  options: ["randint", "rand", "range", "random"], a: ["randint"] },
                { id: 8, type: "MCQ", q: `You are reviewing the following code. What is the output?`, 
                  code: "for i in range(3):\n    print(i)", 
                  options: ["1 2 3", "0 1 2", "0 1 2 3", "1 2"], a: 1 },
                { id: 9, type: "TF", q: `You are reviewing the following code. Select True or False.`, 
                  code: "x = 10\nif x > 5:\n    print(\"High\")\nelse:\n    print(\"Low\")", 
                  options: ["The program prints High.", "The program prints Low when x = 10.", "The if block runs when the condition is True."], a: [true, false, true] },
                { id: 10, type: "DD", q: `You are writing a program that checks whether a number exists in a list. Complete the code.`, 
                  code: "numbers = [5,10,15]\nif 10 [b1] numbers:\n    print(\"Found\")", 
                  options: ["in", "is", "==", "not"], a: ["in"] },
                { id: 11, type: "SHORT", q: `Review the following code. How many lines of output will be printed?`, 
                  code: "for i in range(2):\n    for j in range(2):\n        print(i,j)", a: "4" },
                { id: 12, type: "DD", q: `You are creating a loop that prints numbers until 5. Complete the code.`, 
                  code: "x = 1\n[b1] x <= 5:\n    print(x)\n    x += 1", 
                  options: ["if", "for", "while"], a: ["while"] },
                { id: 13, type: "MCQ", q: `Which keyword defines a function in Python?`, 
                  options: ["function", "define", "def", "func"], a: 2 },
                { id: 14, type: "SHORT", q: `What is the output of the following code?`, 
                  code: "def add(a,b):\n    return a+b\nprint(add(3,7))", a: "10" },
                { id: 15, type: "TF", q: `You are reviewing the following Python code. Select True or False.`, 
                  code: "def greet(name=\"Student\"):\n    print(\"Hello\",name)\ngreet()", 
                  options: ["greet() prints Hello Student", "greet(\"Ana\") prints Hello Ana", "Default parameters must be declared first."], a: [true, true, false] },
                { id: 16, type: "MCQ", q: `Program execution: python script.py Red Blue. What is the output?`, 
                  code: "import sys\n# python script.py Red Blue\nprint(sys.argv[1])", 
                  options: ["script.py", "Red", "Blue", "Error"], a: 1 },
                { id: 17, type: "DD", q: `Complete the code that prints the first character of a string.`, 
                  code: "text = \"Python\"\nprint(text[[b1]])", 
                  options: ["0", "1", "-1", "2"], a: ["0"] },
                { id: 18, type: "TF", q: `Select True or False.`, 
                  code: "# calculate total\ntotal = 10 + 5", 
                  options: ["Comments are ignored during execution.", "Comments improve code readability.", "Comments change program output."], a: [true, true, false] },
                { id: 19, type: "MCQ", q: `Evaluate: print(10 + 5 * 2)`, 
                  code: "print(10 + 5 * 2)", options: ["30", "20", "25", "15"], a: 1 },
                { id: 20, type: "DD", q: `Complete the code to overwrite file contents.`, 
                  code: "file = open(\"data.txt\",\"[b1]\")\nfile.write(\"Hello\")\nfile.close()", 
                  options: ["r", "a", "w"], a: ["w"] },
                { id: 21, type: "MCQ", q: `What does this program do?`, 
                  code: "import random\nprint(random.choice([\"A\",\"B\",\"C\"]))", 
                  options: ["Prints entire list", "Prints random element from list", "Sorts list", "Removes element"], a: 1 },
                { id: 22, type: "TF", q: `You are reviewing the following code. Select True or False.`, 
                  code: "print(10 > 5)", 
                  options: ["Output is True", "Result type is Boolean", "Comparison operators produce numbers."], a: [true, true, false] },
                { id: 23, type: "SHORT", q: `What is the output?`, 
                  code: "nums = [1,2,3,4,5]\nprint(len(nums))", a: "5" },
                { id: 24, type: "DD", q: `Complete the code.`, 
                  code: "student = {\"name\":\"Rahul\",\"age\":20}\nprint(student[\"[b1]\"])", 
                  options: ["name", "Rahul", "age", "student"], a: ["name"] },
                { id: 25, type: "TF", q: `Select True or False.`, 
                  options: ["Sets allow duplicate values.", "Sets store unique elements.", "Sets are unordered."], a: [false, true, true] },
                { id: 26, type: "MCQ", q: `Which statement describes tuples?`, 
                  options: ["Mutable sequence", "Immutable sequence", "Unordered structure", "Dynamic list"], a: 1 },
                { id: 27, type: "TF", q: `Select True or False.`, 
                  code: "a = 10\nb = 10\nprint(a is b)", 
                  options: ["Output may be True", "is checks memory identity", "== checks value equality."], a: [true, true, true] },
                { id: 28, type: "DD", q: `Complete the code.`, 
                  code: "try:\n    print(10/0)\n[b1] ZeroDivisionError:\n    print(\"Cannot divide\")", 
                  options: ["except", "catch", "handle"], a: ["except"] },
                { id: 29, type: "TF", q: `Select True or False.`, 
                  options: ["finally always executes", "finally runs only when error occurs", "finally runs even if no exception happens."], a: [true, false, true] },
                { id: 30, type: "DD", q: `Complete the test statement.`, 
                  code: "self.[b1](5, int)", 
                  options: ["assertTrue", "assertEqual", "assertIsInstance", "assertIn"], a: ["assertIsInstance"] },
                { id: 31, type: "MCQ", q: `Evaluate Output?`, 
                  code: "print((10+5)*2)", 
                  options: ["20", "30", "25", "15"], a: 1 },
                { id: 32, type: "MTF", q: `Match outputs for <code>text = "pythonprogram"</code>.`, 
                  options: ["text[:6]", "text[6:]"], labels: ["python", "program", "prog", "pythonp"], a: { "text[:6]": "python", "text[6:]": "program" } },
                { id: 33, type: "SHORT", q: `How many numbers are printed?`, 
                  code: "for i in range(5):\n    if i == 3:\n        break\n    print(i)", a: "3" },
                { id: 34, type: "DD", q: `Select the correct operator.`, 
                  code: "if x [b1] 5:\n    print(\"Hello\")", 
                  options: ["==", "=", "!=", "="], a: ["=="] },
                { id: 35, type: "DD", q: `Complete the code.`, 
                  code: "numbers = [1,2,3]\nnumbers.[b1](4)", 
                  options: ["append", "add", "insert", "extend"], a: ["append"] },
                { id: 36, type: "MCQ2", q: `Which two code segments correctly read file content?`, 
                  options: ["with open(\"data.txt\",\"r\") as f: print(f.read())", "f=open(\"data.txt\",\"r\"); print(f.read()); f.close()", "open(\"data.txt\").write()", "open(\"data.txt\").append()"], a: [0, 1] },
                { id: 37, type: "MCQ", q: `Evaluate Output?`, 
                  code: "print(True or False)", 
                  options: ["True", "False", "None", "Error"], a: 0 },
                { id: 38, type: "DD", q: `Complete the code.`, 
                  code: "import random\nprint(random.[b1](1,10))", 
                  options: ["randrange", "rand", "random", "choose"], a: ["randrange"] },
                { id: 39, type: "MCQ", q: `Which function deletes a file?`, 
                  options: ["os.delete()", "os.remove()", "os.erase()", "os.clean()"], a: 1 },
                { id: 40, type: "SHORT", q: `What is the output?`, 
                  code: "total = 0\nfor i in range(1,6):\n    if i == 3:\n        continue\n    total += i\nprint(total)", a: "12" }
            ],
            "mock1": [
                { id: 1, type: "DD", q: `
                You are developing a Python application that requires unit testing with the unittest module.`, 
                  code: "[b1] unittest\nclass TestExample(unittest.TestCase):\n    def test_instance(self):\n        self.[b2](5, int)", 
                  options: [["import", "define", "include", "using"], ["assertEqual", "assertTrue", "assertIsInstance", "assertIn"]], a: ["import", "assertIsInstance"] },
                { id: 2, type: "MCQ", q: `Select the correct way to add a comment in Python.`, 
                  options: ["Use /* comment */", "Use <!-- comment -->", "Use # comment", "Use // comment"], a: 2 },
                { id: 3, type: "DD", q: `Complete the logic to generate a unique random room number.`, 
                  code: "import random\nroomsAssigned = []\nroom_number = 1\nwhile room_number in roomsAssigned:\n    [b1]\nroomsAssigned.append(room_number)", 
                  options: ["room_number = random.randint(1, 50)", "room_number += 1", "random.choice(room_number)"], a: ["room_number = random.randint(1, 50)"] },
                { id: 4, type: "DD", q: `
                The program must:<br>• Create a file named report.txt<br>• Write "End of listing" to it`, 
                  code: "file = open(\"report.txt\", \"[b1]\")\nfile.[b2](\"End of listing\")\nfile.close()", 
                  options: [["r", "w", "a"], ["write", "read", "append"]], a: ["w", "write"] },
                { id: 5, type: "DD", q: `Complete the code to handle invalid inputs.`, 
                  code: "while True:\n    try:\n        x = int(input(\"Enter a number: \"))\n        break\n    [b1] ValueError:\n        print(\"Invalid number.\")", 
                  options: ["except", "catch", "error", "handle"], a: ["except"] },
                { id: 6, type: "DD", q: `
                Complete the code to check if data.txt exists and read it.`, 
                  code: "import os\nif [b1](\"data.txt\"):\n    file = open(\"data.txt\", \"r\")\n    print(file.[b2]())\n    file.close()", 
                  options: [["os.path.exists", "os.exists", "os.path.check"], ["read", "write", "open"]], a: ["os.path.exists", "read"] },
                { id: 7, type: "DND", q: `Move the correct keyword to stop the inner loop.`, 
                  code: "for p in range(2, 21):\n    is_prime = True\n    for i in range(2, p):\n        if p % i == 0:\n            is_prime = False\n            [target1]\n    if is_prime:\n        print(p)", 
                  options: ["break", "continue", "pass"], a: ["break"] },
                { id: 8, type: "DD", q: `Complete the comparison logic.`, 
                  code: "numList = [1, 2, 3]\nalphaList = [\"a\", \"b\", \"c\"]\nif [b1]:\n    print(\"Equal\")\nelse:\n    print(\"Not Equal\")", 
                  options: ["numList == alphaList", "numList is alphaList", "numList != alphaList", "numList in alphaList"], a: ["numList == alphaList"] },
                { id: 9, type: "MCQ", q: `What does the <code>input()</code> function always return?`, 
                  options: ["Creates an HTML input field", "Prompts the user to enter text in the console", "Displays system input devices", "Opens a message dialog"], a: 1 },
                { id: 10, type: "TF", q: `Complete the analysis for the <code>grosspay</code> function.`, 
                  code: "def grosspay(hours=40, rate=25, pieces=0, piecerate=0, salary=0): ...", 
                  options: ["Calling grosspay() results in a syntax error.", "Calling grosspay(salary=50000) returns None.", "Calling grosspay(pieces=500, piecerate=4) returns 2000."], a: [false, true, true] },
                { id: 11, type: "DD", q: `Complete the logic to exit the loop correctly.`, 
                  code: "word = input(\"Enter a word (or QUIT to exit): \")\n[b1] word != \"QUIT\":\n    print(len(word))\n    word = input(\"Enter a word (or QUIT to exit): \")", 
                  options: ["if", "for", "while"], a: ["while"] },
                { id: 12, type: "TF", q: `Select True or False for the comparison statements.`, 
                  options: ["The first print statement executes only when the values are equal.", "The second print statement executes only when num1 is less than num2.", "The third print statement executes only when num1 is greater than num2.", "The final condition is logically redundant."], a: [true, true, true, true] },
                { id: 13, type: "DD", q: `Complete the loop and condition to count items.`, 
                  code: "def count_letter(letter, word_list):\n    count = 0\n    for [b1]:\n        if [b2]:\n            count += 1\n    return count", 
                  options: [["word in word_list", "word_list in word"], ["letter in word", "word in letter"]], a: ["word in word_list", "letter in word"] },
                { id: 14, type: "DND", q: `Move the code segments to create a valid guessing game.`, 
                  code: "from random import randint\ntarget = randint(1, 10)\nchance = 1\n[target1]\n    guess = int(input(\"Guess: \"))\n    if guess == target:\n        print(\"Correct!\")\n        [target2]\n    [target3]", 
                  options: ["break", "chance += 1", "while chance <= 3:"], a: ["while chance <= 3:", "break", "chance += 1"] },
                { id: 15, type: "DD", q: `Complete the conditional logic for fee calculation.`, 
                  code: "elif age >= 5 and age <= 17 and not school: rate = [b1]\nelse: rate = [b2]", 
                  options: [["20", "50", "10"], ["20", "50"]], a: ["20", "50"] },
                { id: 16, type: "MCQ", q: `Identify the output of the command-line script.`, 
                  code: "import sys\n# python script.py Apple Banana Mango\nprint(sys.argv[2])", 
                  options: ["script.py", "Apple", "Banana", "Mango"], a: 2 },
                { id: 17, type: "DD", q: `Complete the logic to reverse the name.`, 
                  code: "def reverse_name(backward_name):\n    forward_name = \"\"\n    length = len(backward_name) - 1\n    while length >= 0:\n        forward_name += [b1]\n        length -= 1\n    return forward_name", 
                  options: ["backward_name[length]", "backward_name", "forward_name[length]"], a: ["backward_name[length]"] },
                { id: 18, type: "TF", q: `Analyze the impact of comments on code execution.`, 
                  code: "def calc_power(x, y):\n    comment = \"# return the value\"\n    return x ** y  # exponent", 
                  options: ["The string message is treated as a comment.", "The function returns x raised to the power y.", "The inline comment does not affect execution.", "Removing the comment changes the output."], a: [false, true, true, false] },
                { id: 19, type: "MCQ", q: `Evaluate the result of the complex arithmetic expression.`, 
                  code: "answer = (9 % 4 * 10) // 2 ** 3 + 4", 
                  options: ["5", "6", "4", "3"], a: 0 },
                { id: 20, type: "MCQ", q: `Identify the cause of the potential error.`, 
                  code: "def read_file(file):\n    if os.path.isfile(file): ...", 
                  options: ["isfile requires two parameters", "os module is not imported", "The path must be absolute", "open requires a different mode"], a: 1 },
                { id: 21, type: "MCQ2", q: `Which code segments correctly meet the requirements?`, 
                  options: ["from random import randint; print(randint(1, 20) * 5)", "from random import randint; print(randint(0, 20) * 5)", "from random import randrange; print(randrange(0, 100, 5))", "from random import randrange; print(randrange(5, 105, 5))"], a: [0, 3] },
                { id: 22, type: "DD", q: `Complete the branching logic for classification.`, 
                  code: "if [b1]: digits = \"1\"\nelif [b2]: digits = \"2\"", 
                  options: ["num < 10", "num >= 10 and num < 100", "num >= 100", "len(str(num)) == 1"], a: ["num < 10", "num >= 10 and num < 100"] },
                { id: 23, type: "MCQ", q: `Determine the final value of the grade variable.`, 
                  code: "grade = 76; rank = 3\nif grade > 80 and rank >= 3: grade += 10\nelif grade >= 70 and rank > 3: grade += 5\nelse: grade -= 5\nprint(grade)", 
                  options: ["71", "76", "81", "86"], a: 0 },
                { id: 24, type: "MTF", q: `Match each expression to its corresponding data type.`, 
                  options: ["type(+1E10)", "type(5.0)", "type(\"True\")", "type(False)"], labels: ["int", "float", "str", "bool"], a: { "type(+1E10)": "float", "type(5.0)": "float", "type(\"True\")": "str", "type(False)": "bool" } },
                { id: 25, type: "MCQ2", q: `Select the two correct function definition calls.`, 
                  options: ["def get_name():", "def get_name(biker):", "def get_name(name):", "def calc_calories():", "def calc_calories(miles, burn_rate):", "def calc_calories(miles, calories_per_mile):"], a: [0, 5] },
                { id: 26, type: "TF", q: `Analyze the logic of the exponent calculation.`, 
                  code: "base = input(...); exponent = input(...)\nresult = calc_power(base, exponent)\nprint(\"The result is \" + result)", 
                  options: ["The code will generate an error in the input lines.", "The function will correctly compute exponentiation.", "The print statement will generate an error."], a: [false, false, true] },
                { id: 27, type: "TF", q: `Select True or False for the statements about try/except/finally.`, 
                  options: ["A try statement can have one or more except clauses.", "A try statement can have a finally clause without an except clause.", "A try statement can have both except and finally clauses.", "A try statement can have more than one finally clause."], a: [true, true, true, false] },
                { id: 28, type: "TF", q: `Analyze the behavior of opening a file in 'append' mode.`, 
                  code: "f = open(\"python.txt\", \"a\")\nf.write(\"This is a line of text.\")\nf.close()", 
                  options: ["A file named python.txt is created if it does not exist.", "The existing data in the file will be overwritten.", "The file can be opened again after this code runs."], a: [true, false, true] },
                { id: 29, type: "MCQ2", q: `Identify the correct f-string or formatting methods.`, 
                  options: ["print('\"' + item + '\",' + str(sales))", "print('\"{0}\",{1}'.format(item, sales))", "print(item + \",\" + sales)", "print(f'\"{item}\",{sales}')"], a: [1, 3] },
                { id: 30, type: "MCQ", q: `Evaluate the arithmetic expression with modulo and precedence.`, 
                  code: "value1 = 9; value2 = 4\nanswer = (value1 % value2 * 10) / 2.0 ** 3.0 + value2", 
                  options: ["5.667", "5.0", "129", "Syntax Error"], a: 1 },
                { id: 31, type: "DND", q: `Order the operational precedence from first to last.`, 
                  code: "1st: [target1]\nLast: [target2]", 
                  options: ["Addition and Subtraction", "And", "Exponents", "Multiplication and Division", "Parentheses", "Unary positive, negative, not"], a: ["Parentheses", "And"] },
                { id: 32, type: "TF", q: `Select True or False for the default parameter analysis.`, 
                  code: "01 def increment_score(score, bonus, points=1): ...", 
                  options: ["To meet the requirements, you must change line 01.", "If line 01 is not changed, an error occurs with 2 parameters.", "Line 03 modifies the external variable points."], a: [true, true, false] },
                { id: 33, type: "MTF", q: `Match the slice expressions to their resulting strings.`, 
                  options: ["alph[3:6]", "alph[:6]"], labels: ["def", "abcdef", "cde", "defg", "cdef", "abcde"], a: { "alph[3:6]": "def", "alph[:6]": "abcdef" } },
                { id: 34, type: "SHORT", q: `Provide the final value of the product after loop execution.`, 
                  code: "product = 2; n = 5\nwhile (n != 0):\n    product *= n; n -= 1\n    if n == 3: break", a: "2" },
                { id: 35, type: "DD", q: `Select the correct condition to iterate through the list.`, 
                  code: "while [b1]\n    if [b2]", 
                  options: [["(index < 10):", "(index <= 10):"], ["numbers[index] == 6:", "numbers[index] = 6:"]], a: ["(index < 10):", "numbers[index] == 6:"] },
                { id: 36, type: "DD", q: `Complete the operations to manage student scores.`, 
                  code: "# Add score 88\n[b1]\n# Sort\n[b2]\n# Remove lowest\n[b3]", 
                  options: [["scores.append(88)", "scores.add(88)"], ["scores.sort()", "scores.sorted()"], ["scores.remove(min(scores))", "scores.pop(0)"]], a: ["scores.append(88)", "scores.sort()", "scores.remove(min(scores))"] },
                { id: 37, type: "TF", q: `Select True or False for the comparison operators.`, 
                  code: "a = [1, 2, 3]; b = [1, 2, 3]; c = a", 
                  options: ["a == b evaluates to True.", "a is b evaluates to True.", "a is c evaluates to True.", "b is not c evaluates to True."], a: [true, false, true, true] },
                { id: 38, type: "MCQ", q: `Identify the output for the combined logical condition.`, 
                  code: "attempts = 3; locked = False\nif attempts >= 3 and not locked: print(\"Warning\")", 
                  options: ["Access Allowed", "Warning", "Syntax Error", "Nothing"], a: 1 },
                { id: 39, type: "MCQ2", q: `Select the two correct ways to read file contents.`, 
                  options: ["with open(\"data.txt\", \"r\") as f: data = f.read()", "f = open(\"data.txt\", \"r\"); data = f.read()", "f = open(\"data.txt\", \"r\"); data = f.read(); f.close()", "open(\"data.txt\").read()"], a: [0, 2] },
                { id: 40, type: "SHORT", q: `Calculate the total sum after the loop finishes.`, 
                  code: "total = 0\nfor i in range(1, 6):\n    if i == 3: continue\n    total += i\nprint(total)", a: "12" }
            ]
        };

        const params = new URLSearchParams(window.location.search);
        let modId = params.get('mod');
        let mockId = params.get('mock');
        
        if(mockId) modId = "mock" + mockId;
        else modId = modId || "1";

        let currentQuestions = [...(quizData[modId] || quizData["1"])];

        // Shuffle logic for Module Assessments
        if(!mockId) {
            for (let i = currentQuestions.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [currentQuestions[i], currentQuestions[j]] = [currentQuestions[j], currentQuestions[i]];
            }
        }

        let currentIndex = 0;
        let userAnswers = new Array(currentQuestions.length).fill(null);
        let quizStartTime = Date.now();
        let timeLeft = mockId ? 50 * 60 : 10 * 60;

        function startTimer() {
            setInterval(() => {
                if(timeLeft <= 0) return autoSubmit();
                timeLeft--;
                const mins = Math.floor(timeLeft / 60);
                const secs = timeLeft % 60;
                document.getElementById('timer-display').innerText = `${mins}:${secs<10?'0':''}${secs}`;
            }, 1000);
        }

        function loadQuestion() {
            const q = currentQuestions[currentIndex];
            if(!q) {
                document.getElementById('q-text').innerHTML = "<div style='color:#dc2626; font-weight:700;'>ERROR: MODULE DATA NOT FOUND</div><p>Please return to the roadmap and select a valid module.</p>";
                document.getElementById('q-number').innerText = "System Failure";
                return;
            }
            document.getElementById('q-number').innerText = `Question ${currentIndex + 1}`;
            document.getElementById('q-text').innerHTML = q.q;
            
            const codeContainer = document.getElementById('q-code-container');
            codeContainer.innerHTML = q.code ? `<div class='code-snippet'>${q.code.replace(/\n/g, '<br>')}</div>` : "";
            
            const interaction = document.getElementById('interaction-area');
            interaction.innerHTML = "";

            if(q.type === "MCQ" || q.type === "MCQ2") {
                const grid = document.createElement('div');
                grid.className = "options-container options-grid";
                q.options.forEach((opt, i) => {
                    const div = document.createElement('div');
                    div.className = `option ${(userAnswers[currentIndex] === i || (Array.isArray(userAnswers[currentIndex]) && userAnswers[currentIndex].includes(i))) ? 'selected' : ''}`;
                    div.innerHTML = `<span class='label'>${String.fromCharCode(65+i)}</span> ${opt}`;
                    div.onclick = () => handleSelection(i, q.type === "MCQ2");
                    grid.appendChild(div);
                });
                interaction.appendChild(grid);
            } else if(q.type === "SHORT") {
                const area = document.createElement('div');
                area.className = "answer-area";
                area.innerHTML = `<input class="short-answer-input" placeholder="Type your answer here..." value="${userAnswers[currentIndex] || ''}" oninput="userAnswers[currentIndex]=this.value">`;
                interaction.appendChild(area);
            } else if(q.type === "TF") {
                const area = document.createElement('div');
                area.className = "answer-area";
                q.options.forEach((opt, i) => {
                    const row = document.createElement('div');
                    row.className = "mtf-row";
                    row.innerHTML = `<span style="color:#64748b; font-weight:600;">${opt}</span><select class="quiz-dropdown" onchange="updateTF(${i}, this.value)"><option value="">SELECT...</option><option value="true">TRUE</option><option value="false">FALSE</option></select>`;
                    if(userAnswers[currentIndex]?.[i]) row.querySelector('select').value = userAnswers[currentIndex][i];
                    area.appendChild(row);
                });
                interaction.appendChild(area);
            } else if(q.type === "MTF") {
                const area = document.createElement('div');
                area.className = "answer-area";
                q.options.forEach((item, i) => {
                    const row = document.createElement('div');
                    row.className = "mtf-row";
                    row.innerHTML = `<span style="color:#64748b; font-weight:600;">${item}</span><select class="quiz-dropdown" onchange="updateComplex('${item}', this.value)"><option value="">CHOOSE...</option>` + q.labels.map(l => `<option value="${l}">${l}</option>`).join('') + `</select>`;
                    const val = userAnswers[currentIndex]?.[item];
                    if(val) row.querySelector('select').value = val;
                    area.appendChild(row);
                });
                interaction.appendChild(area);
            } else if(q.type === "DD") {
                // Inline Dropdown Logic
                if(q.code) {
                    const codeWithSelects = q.code.replace(/\[b(\d+)\]/g, (match, p1) => {
                        const idx = parseInt(p1) - 1;
                        const optSet = Array.isArray(q.options[0]) ? q.options[idx] : q.options;
                        const val = userAnswers[currentIndex]?.[idx] || "";
                        return `<select class="inline-select" onchange="updateComplex(${idx}, this.value)">
                            <option value="">CHOOSE...</option>
                            ${optSet.map(o => `<option value="${o}" ${o===val?'selected':''}>${o}</option>`).join('')}
                        </select>`;
                    });
                    codeContainer.innerHTML = `<div class='code-snippet' style='text-align:left;'>${codeWithSelects.replace(/\n/g, '<br>')}</div>`;
                } else {
                    const area = document.createElement('div');
                    area.className = "answer-area";
                    q.options.slice(0, (q.q.match(/\[b/g) || []).length || 1).forEach((_, i) => {
                        const row = document.createElement('div');
                        row.className = "mtf-row";
                        row.innerHTML = `<span style="color:#64748b; font-weight:600;">Blank ${i+1}:</span><select class="quiz-dropdown" onchange="updateComplex(${i}, this.value)"><option value="">CHOOSE...</option>` + (Array.isArray(q.options[0]) ? q.options[i] : q.options).map(l => `<option value="${l}">${l}</option>`).join('') + `</select>`;
                        const val = userAnswers[currentIndex]?.[i];
                        if(val) row.querySelector('select').value = val;
                        area.appendChild(row);
                    });
                    interaction.appendChild(area);
                }
            } else if(q.type === "DND") {
                const area = document.createElement('div');
                area.className = "dnd-section";
                const codeWithSlots = q.code.replace(/\[target(\d+)\]/g, (match, p1) => {
                    const idx = parseInt(p1) - 1;
                    const val = (userAnswers[currentIndex] && (typeof userAnswers[currentIndex] === 'object')) ? userAnswers[currentIndex][idx] : null;
                    return `<span class="dnd-target ${val?'filled':''}" ondragover="event.preventDefault()" ondrop="handleDrop(event, ${idx})">${val || ''}</span>`;
                });
                area.innerHTML = `
                    <div class='code-snippet' style='text-align:left;'>${codeWithSlots.replace(/\n/g, '<br>')}</div>
                    <div style="font-weight:800; color:#64748b; margin:25px 0 15px; font-size:12px; letter-spacing:1px; text-transform:uppercase;">Drag segments into the blanks:</div>
                    <div class="dnd-pool">
                        ${q.options.map(opt => `<div class="dnd-item" draggable="true" ondragstart="handleDragStart(event)">${opt}</div>`).join('')}
                    </div>
                `;
                interaction.appendChild(area);
            }

            document.getElementById('btn-prev').disabled = currentIndex === 0;
            document.getElementById('btn-next').innerText = (currentIndex === currentQuestions.length - 1) ? "Finalize" : "Next Step";
        }

        function handleSelection(idx, multi) {
            if(multi) {
                if(!Array.isArray(userAnswers[currentIndex])) userAnswers[currentIndex] = [];
                const pos = userAnswers[currentIndex].indexOf(idx);
                if(pos > -1) userAnswers[currentIndex].splice(pos, 1);
                else userAnswers[currentIndex].push(idx);
            } else { userAnswers[currentIndex] = idx; }
            loadQuestion();
        }

        function updateTF(i, val) { if(!userAnswers[currentIndex]) userAnswers[currentIndex] = []; userAnswers[currentIndex][i] = val; }
        function updateComplex(key, val) { if(!userAnswers[currentIndex]) userAnswers[currentIndex] = (typeof key === 'string' ? {} : []); userAnswers[currentIndex][key] = val; }

        function handleDragStart(e) { e.dataTransfer.setData("text", e.target.innerText); }
        function handleDrop(e, targetIdx) {
            e.preventDefault();
            const val = e.dataTransfer.getData("text");
            if(!userAnswers[currentIndex] || typeof userAnswers[currentIndex] !== 'object') userAnswers[currentIndex] = {};
            userAnswers[currentIndex][targetIdx] = val;
            loadQuestion();
        }

        function prevQuestion() { if(currentIndex > 0) { currentIndex--; loadQuestion(); } }
        function skipQuestion() { userAnswers[currentIndex] = "SKIP"; nextQuestion(); }
        function nextQuestion() {
            if(currentIndex < currentQuestions.length - 1) { currentIndex++; loadQuestion(); }
            else autoSubmit();
        }

        function autoSubmit() {
            let score = 0;
            let results = [];
            const timeTaken = Math.max(0, (mockId ? 50 : 10) * 60 - timeLeft);
            const avgSpeed = (timeTaken / currentQuestions.length).toFixed(1);
            // Skill tracking: categories mapped by question topic keywords
            const skillMap = {
                'File': { total: 0, correct: 0 },
                'Loop': { total: 0, correct: 0 },
                'Function': { total: 0, correct: 0 },
                'Data': { total: 0, correct: 0 },
                'Operator': { total: 0, correct: 0 },
                'Error': { total: 0, correct: 0 }
            };
            const skillKeywords = {
                'File': ['file', 'handling', 'writing', 'read', 'exist', 'delete', 'writing mode'],
                'Loop': ['loop', 'range', 'iteration', 'while', 'break', 'continue', 'nested', 'control'],
                'Function': ['function', 'return', 'parameter', 'argument', 'default', 'reusability', 'definition'],
                'Data': ['list', 'dict', 'tuple', 'set', 'string', 'slicing', 'indexing', 'membership', 'type', 'length', 'append'],
                'Operator': ['operator', 'arithmetic', 'expression', 'boolean', 'logic', 'precedence', 'identity', 'equality', 'conditional', 'evaluation'],
                'Error': ['error', 'exception', 'try', 'except', 'finally', 'testing', 'unit']
            };

            currentQuestions.forEach((q, i) => {
                const u = userAnswers[i];
                let correct = false;
                let userDisp = u === "SKIP" || !u ? "Skipped" : u;
                let correctDisp = q.a;

                // Validation Logic
                if(q.type === "MCQ") {
                    correct = u === q.a;
                    userDisp = u !== null && u !== "SKIP" ? q.options[u] : userDisp;
                    correctDisp = q.options[q.a];
                }
                else if(q.type === "MCQ2") {
                    correct = Array.isArray(u) && u.length === q.a.length && u.every(v => q.a.includes(v));
                    userDisp = Array.isArray(u) ? u.map(idx => q.options[idx]).join(", ") : userDisp;
                    correctDisp = q.a.map(idx => q.options[idx]).join(", ");
                }
                else if(q.type === "SHORT") {
                    correct = u? u.toString().toLowerCase().trim() === q.a.toLowerCase().trim() : false;
                }
                else if(q.type === "TF") {
                    correct = Array.isArray(u) && u.every((v, j) => v === q.a[j].toString());
                    userDisp = Array.isArray(u) ? u.join(", ").toUpperCase() : userDisp;
                    correctDisp = q.a.join(", ").toUpperCase();
                }
                else if(q.type === "MTF") {
                    correct = typeof u === 'object' && u !== null && Object.keys(q.a).every(k => u[k] === q.a[k]);
                    userDisp = typeof u === 'object' && u !== null ? JSON.stringify(u).replace(/["{}]/g, "") : userDisp;
                    correctDisp = JSON.stringify(q.a).replace(/["{}]/g, "");
                }
                else if(q.type === "DD") {
                    correct = Array.isArray(u) && u.every((v, j) => v === q.a[j]);
                    userDisp = Array.isArray(u) ? u.join(", ") : userDisp;
                    correctDisp = q.a.join(", ");
                }
                else if(q.type === "DND") {
                    correct = typeof u === 'object' && u !== null && q.a.every((v, j) => u[j] === v);
                    userDisp = typeof u === 'object' && u !== null ? Object.values(u).join(", ") : userDisp;
                    correctDisp = q.a.join(", ");
                }

                if(correct) score++;
                // Assign to skill category
                const qText = (q.q || '').toLowerCase();
                for(const [skill, kws] of Object.entries(skillKeywords)) {
                    if(kws.some(kw => qText.includes(kw))) {
                        skillMap[skill].total++;
                        if(correct) skillMap[skill].correct++;
                        break;
                    }
                }
                results.push({ q: q.q, code: q.code || '', user: userDisp, correct: correctDisp, isCorrect: correct });
            });

            showResults(score, avgSpeed, results, skillMap);
        }

        function showResults(score, speed, results, skillMap) {
            document.getElementById('quiz-ui').style.display = "none";
            document.getElementById('timer-display').style.display = "none";
            document.getElementById('result-dashboard').style.display = "block";
            
            document.getElementById('res-score').innerText = `${score}/${currentQuestions.length}`;
            document.getElementById('res-accuracy').innerText = `${Math.round(score/currentQuestions.length*100)}%`;
            document.getElementById('res-speed').innerText = `${speed}s`;

            const reviewList = document.getElementById('review-list');
            results.forEach((res, i) => {
                const item = document.createElement('div');
                item.className = "review-item";
                item.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                        <div class="review-q-text">${res.q}</div>
                        <span class="status-pill ${res.isCorrect ? 'status-correct' : 'status-wrong'}">${res.isCorrect ? 'Correct' : 'Incorrect'}</span>
                    </div>
                    ${res.code ? '<div style="padding:6px 0; font-family:monospace; font-size:13px; color:#334155; white-space:pre-wrap; line-height:1.6;">' + res.code.replace(/\\n/g, '<br>') + '</div>' : ''}
                    <div class="ans-row">
                        <span class="ans-label">Your Response:</span>
                        <span class="user-ans">${res.user}</span>
                    </div>
                    <div class="ans-row" id="correct-row-${i}" style="display:none;">
                        <span class="ans-label" style="color:#059669">Correct Answer:</span>
                        <span class="correct-ans" style="display:inline-block">${res.correct}</span>
                    </div>
                    <button class="view-ans-btn" onclick="document.getElementById('correct-row-${i}').style.display='flex'; this.style.display='none'">View Right Answer</button>
                `;
                reviewList.appendChild(item);
            });

            initCharts(score, skillMap);
        }

        function initCharts(score, skillMap) {
            new Chart(document.getElementById('performanceChart'), {
                type: 'doughnut',
                data: { labels: ['Correct', 'Incorrect'], datasets: [{ data: [score, currentQuestions.length - score], backgroundColor: ['#0066ff', '#f1f5f9'], borderWidth: 0 }] },
                options: { cutout: '70%', plugins: { legend: { labels: { color: '#1e293b', font: { size: 12 } } } } }
            });

            // Build radar data from actual skill performance
            const skillLabels = Object.keys(skillMap);
            const skillScores = skillLabels.map(s => {
                const { total, correct } = skillMap[s];
                if(total === 0) return 50; // neutral if no questions in that category
                return Math.round((correct / total) * 100);
            });
            const friendlyLabels = {
                'File': 'File Handling',
                'Loop': 'Loops & Control',
                'Function': 'Functions',
                'Data': 'Data Structures',
                'Operator': 'Operators & Logic',
                'Error': 'Error Handling'
            };

            new Chart(document.getElementById('competencyChart'), {
                type: 'radar',
                data: {
                    labels: skillLabels.map(s => friendlyLabels[s] || s),
                    datasets: [{
                        label: 'Your Score (%)',
                        data: skillScores,
                        borderColor: '#0066ff',
                        backgroundColor: 'rgba(0,102,255,0.12)',
                        pointBackgroundColor: '#0066ff',
                        pointRadius: 4,
                        borderWidth: 2
                    }]
                },
                options: {
                    scales: {
                        r: {
                            min: 0,
                            max: 100,
                            grid: { color: 'rgba(0,0,0,0.07)' },
                            pointLabels: { color: '#1e293b', font: { size: 11, weight: '600' } },
                            ticks: {
                                stepSize: 25,
                                color: '#94a3b8',
                                backdropColor: 'transparent',
                                font: { size: 10 },
                                callback: v => v + '%'
                            }
                        }
                    },
                    plugins: {
                        legend: { display: true, position: 'bottom', labels: { color: '#1e293b', font: { size: 11 } } },
                        tooltip: {
                            callbacks: {
                                label: ctx => ` ${ctx.parsed.r}% accuracy`
                            }
                        }
                    }
                }
            });

            // Bar chart for skill breakdown
            const barColors = ['#0066ff', '#3385ff', '#0052cc', '#4d9aff', '#0040a0', '#66b3ff'];
            new Chart(document.getElementById('barChart'), {
                type: 'bar',
                data: {
                    labels: skillLabels.map(s => friendlyLabels[s] || s),
                    datasets: [{
                        label: 'Score (%)',
                        data: skillScores,
                        backgroundColor: barColors.slice(0, skillLabels.length),
                        borderRadius: 6,
                        barThickness: 28
                    }]
                },
                options: {
                    indexAxis: 'y',
                    scales: {
                        x: { min: 0, max: 100, ticks: { callback: v => v + '%', color: '#94a3b8', font: { size: 10 } }, grid: { color: 'rgba(0,0,0,0.05)' } },
                        y: { ticks: { color: '#1e293b', font: { size: 11, weight: '600' } }, grid: { display: false } }
                    },
                    plugins: {
                        legend: { display: false },
                        tooltip: { callbacks: { label: ctx => ` ${ctx.parsed.x}% accuracy` } }
                    }
                }
            });
        }

        window.onload = () => { startTimer(); loadQuestion(); };
    