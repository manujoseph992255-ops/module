import sys, re
import update_m1_script
import update_m1_script_pt2

# Combine the HTML parts
all_parts = update_m1_script.html_parts + update_m1_script_pt2.html_parts
combined_html = "".join(all_parts)

filepath = r"C:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# Replace the inner html of main-content
# Find <main class="main-content"> and </main>
start_str = '<main class="main-content">'
end_str = '</main>'

start_idx = text.find(start_str)
if start_idx == -1:
    print("Error: Could not find <main class=\"main-content\">")
    sys.exit(1)

start_idx += len(start_str)

end_idx = text.rfind(end_str)
if end_idx == -1:
    print("Error: Could not find </main>")
    sys.exit(1)

new_main = combined_html + """
            <div class="quiz-cta">
                <h3>Module 1 Complete!</h3>
                <p>Ready to test your knowledge on Data Basics?</p>
                <a href="module_quiz.html?mod=d1" class="btn-start-quiz">Start Assessment &rarr;</a>
            </div>
"""

new_text = text[:start_idx] + "\n" + new_main + "\n        " + text[end_idx:]

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_text)

print("Successfully updated Data-Module-1.html")
