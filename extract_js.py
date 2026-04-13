import re

try:
    with open('module_quiz.html', 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    if match:
        with open('test.js', 'w', encoding='utf-8') as f:
            f.write(match.group(1))
        print("Script successfully extracted to test.js")
    else:
        print("No <script> block found")
except Exception as e:
    print(f"Error: {e}")
