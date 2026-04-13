import sys

def check_syntax(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Try to find the start of the object
        start = content.find('{')
        if start == -1:
            print("Error: No opening brace found.")
            return

        # Simple brace counting
        stack = []
        line_num = 1
        col_num = 1
        for i, char in enumerate(content):
            if char == '\n':
                line_num += 1
                col_num = 1
            else:
                col_num += 1
                
            if char == '{' or char == '[':
                stack.append((char, line_num, col_num))
            elif char == '}' or char == ']':
                if not stack:
                    print(f"Error: Unmatched {char} at line {line_num}, col {col_num}")
                    return
                top, l, c = stack.pop()
                if (char == '}' and top != '{') or (char == ']' and top != '['):
                    print(f"Error: Mismatched {top} and {char} at line {line_num}, col {col_num} (Opening at line {l}, col {c})")
                    return
        
        if stack:
            print(f"Error: {len(stack)} unmatched opening braces/brackets left.")
            for char, l, c in stack:
                print(f"  Unmatched {char} at line {l}, col {c}")
        else:
            print("Brace/bracket balance check passed.")
            
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    check_syntax("c:/Users/kj anand/Downloads/Quiz DD/quiz_data.js")
