import re

def analyze_quiz_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find the main quizData object
        start_match = re.search(r'var\s+quizData\s*=\s*\{', content)
        if not start_match:
            print("Error: quizData not found")
            return
            
        start_pos = start_match.end()
        
        # Scan for keys at depth 1
        depth = 0
        idx = start_pos
        current_key = None
        results = []
        
        while idx < len(content):
            char = content[idx]
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
            elif char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
            
            # Look for keys at depth 0 (relative to the object interior)
            if depth == 0:
                # Key pattern: "key": [ or 'key': [
                key_match = re.search(r'["\'](\w+)["\']\s*:\s*\[', content[idx:idx+100])
                if key_match:
                    key = key_match.group(1)
                    # Count questions in this array
                    q_count = 0
                    a_depth = 1
                    a_idx = idx + key_match.end()
                    while a_depth > 0 and a_idx < len(content):
                        if content[a_idx] == '[': a_depth += 1
                        elif content[a_idx] == ']': a_depth -= 1
                        elif content[a_idx] == '{' and a_depth == 1:
                            q_count += 1
                        a_idx += 1
                    results.append((key, q_count))
                    idx = a_idx - 1 # Skip the array
            idx += 1
            if char == '}' and depth == -1: break # End of quizData
            
        for key, count in results:
            print(f"Key: {key}, Questions: {count}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_quiz_data("c:/Users/kj anand/Downloads/Quiz DD/quiz_data.js")
