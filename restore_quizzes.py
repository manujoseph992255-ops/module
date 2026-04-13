import re

# Read the test file
with open("quiz_data_test.js", "r", encoding="utf-8") as f:
    test_content = f.read()

# Extract blocks d1, d2, data3
# We look for "d1": [ ... ] where ... stops before the next top-level key like "d2": [
def extract_block(key, content):
    pattern = r'(\s*"' + key + r'"\s*:\s*\[.*?\n    \](,?))'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        block = match.group(1)
        if block.endswith(','):
            block = block[:-1] # Remove trailing comma for clean replacement
        return block
    return None

d1_block = extract_block("d1", test_content)
d2_block = extract_block("d2", test_content)
data3_block = extract_block("data3", test_content)

if d1_block: d1_block = d1_block.replace('"d1":', '"data1":')
if d2_block: d2_block = d2_block.replace('"d2":', '"data2":')

# Read current file
with open("quiz_data.js", "r", encoding="utf-8") as f:
    main_content = f.read()

def replace_main_block(key, new_val_str, content):
    replace_pattern = r'(\s*"' + key + r'"\s*:\s*\[.*?\n    \](,?))'
    new_block = new_val_str
    # re.sub with function to preserve commas if needed
    def repl(m):
        comma = m.group(2) if m.group(2) else ""
        return new_block + comma
    new_content = re.sub(replace_pattern, repl, content, count=1, flags=re.DOTALL)
    return new_content

if d1_block:
    main_content = replace_main_block("data1", d1_block, main_content)
    print("Restored data1")
if d2_block:
    main_content = replace_main_block("data2", d2_block, main_content)
    print("Restored data2")
if data3_block:
    main_content = replace_main_block("data3", data3_block, main_content)
    print("Restored data3")

# Write changes
with open("quiz_data.js", "w", encoding="utf-8") as f:
    f.write(main_content)
print("Finished restoring.")
