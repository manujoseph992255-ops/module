import re
import json
import update_mock2
import update_mock3

def replace_array_for_key(text, key, new_json):
    start_match = re.search(r'"' + key + r'"\s*:\s*\[', text)
    if not start_match:
        print(f"Key {key} not found")
        return text
    start_idx = start_match.end() - 1 # points to '['
    
    bracket_count = 0
    end_idx = -1
    in_string = False
    escape = False
    
    for i in range(start_idx, len(text)):
        char = text[i]
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
            continue
        if char == '"' and not in_string:
            in_string = True
            continue
        elif char == '"' and in_string:
            in_string = False
            continue
            
        if not in_string:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    end_idx = i
                    break
                    
    if end_idx != -1:
        return text[:start_match.start()] + f'"{key}": ' + new_json + text[end_idx+1:]
    else:
        print(f"Could not find end of array for {key}")
        return text

with open('quiz_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

new_mock2 = json.dumps(update_mock2.mock2_questions, indent=4)
new_mock3 = json.dumps(update_mock3.mock3_questions, indent=4)

text = replace_array_for_key(text, 'mock2', new_mock2)
text = replace_array_for_key(text, 'mock3', new_mock3)

with open('quiz_data.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Safely replaced mock2 and mock3 arrays.")
