import os
import glob

directory = r"c:/Users/kj anand/Downloads/Quiz DD"

html_files = glob.glob(os.path.join(directory, "*.html"))
js_files = glob.glob(os.path.join(directory, "*.js"))

all_files = html_files + js_files

for file_path in all_files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace logic:
        # First, we replace 'index.html' with '__TEMP_LOGIN__'
        # Then, 'course_selection.html' with 'index.html'
        # Finally, '__TEMP_LOGIN__' with 'login.html'
        
        if "index.html" in content or "course_selection.html" in content:
            new_content = content.replace("index.html", "__TEMP_LOGIN__")
            new_content = new_content.replace("course_selection.html", "index.html")
            new_content = new_content.replace("__TEMP_LOGIN__", "login.html")
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated: {os.path.basename(file_path)}")
    except Exception as e:
        print(f"Error processing {os.path.basename(file_path)}: {e}")
