import json
import re

with open("quiz_data_test.js", "r", encoding="utf-8") as f:
    text = f.read()

# Fix d1 -> data1, d2 -> data2
text = text.replace('"d1": [', '"data1": [')
text = text.replace('"d2": [', '"data2": [')

# We'll do a simple state machine to find the full extent of the array to replace
def replace_block_smart(key, new_text, full_src):
    start_str = '"' + key + '": ['
    idx = full_src.find(start_str)
    if idx == -1:
        return full_src
        
    start_bracket_idx = idx + len(start_str) - 1
    bracket_count = 0
    end_idx = -1
    for i in range(start_bracket_idx, len(full_src)):
        if full_src[i] == '[':
            bracket_count += 1
        elif full_src[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end_idx = i
                break
                
    if end_idx != -1:
        return full_src[:idx] + f'"{key}": {new_text}' + full_src[end_idx+1:]
    return full_src

# We will read data1 to data5 strings directly from the formatted js objects
# I'll just import populate_data_quizzes to get the python objects
from populate_data_quizzes import format_js_objects, data1, data2, data3, data4, data5

# data3 in test is named "data3". We replace it.
text = replace_block_smart("data1", format_js_objects(data1), text)
text = replace_block_smart("data2", format_js_objects(data2), text)
text = replace_block_smart("data3", format_js_objects(data3), text)

# data4 and data5 don't exist in quiz_data_test.js, so we append them before the final `};`
text = text.replace("};", f',\n    "data4": {format_js_objects(data4)},\n    "data5": {format_js_objects(data5)}\n}};')

with open("quiz_data.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Restored and injected safely")
