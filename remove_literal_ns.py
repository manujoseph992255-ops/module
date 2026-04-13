import os

def remove_literal_newlines():
    directory = r'c:\Users\kj anand\Downloads\Quiz DD'
    target = r'\n'
    
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if target in content:
                new_content = content.replace(target, '')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Cleaned {filename}")

if __name__ == "__main__":
    remove_literal_newlines()
