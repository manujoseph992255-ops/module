import re

filepath = r"C:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match the main-content div and its contents
# We want to keep the <main class="main-content"> opening tag and the closing </main>
# and clear everything in between.
# However, the previous edit already added <!-- Content Removed as per User Request -->
# But there is leftover content after the scripts. 
# Let's find the first <main class="main-content"> and the corresponding closing </main> or footer.

# Actually, the previous edit produced:
# 829:         <main class="main-content">
# 830:             <!-- Content Removed as per User Request -->
# 831:         </main>
# 832:     </div>
# 833: 
# 834:     <script ...>
# ...
# 843:     </script>
# 844:                 <strong>Insight:</strong>

# It seems the replace_file_content call inserted the replacement but didn't delete the lines outside the TargetContent within the range.
# Let's just match the block starting from the duplicate "Insight" section until the end.

# Wait, let's just rewrite the whole file with the template structure.
# I'll grab the head and head styles, then the body and layout container, and stop there.

head_part = content.split('<header class="header-banner">')[0]
banner_part = '<header class="header-banner">\n        <h1>MODULE 1: DATA BASICS</h1>\n    </header>\n'
sidebar_part = """
    <div class="layout-container">
        <nav class="sidebar">
            <h3>Module Path</h3>
            <a href="Data-Module-1.html" class="active">01 Data Basics</a>
            <a href="Data-Module-2.html">02 Data Manipulation</a>
            <a href="#">03 Data Analysis</a>
            <a href="#">04 Visualization</a>
            <a href="#">05 Responsible Analytics</a>

            <h3 style="margin-top:25px;">Navigation</h3>
            <a href="data_roadmap.html" style="background: #f8f9fa;">&larr; Return to Roadmap</a>
        </nav>

        <main class="main-content">
            <!-- Content Removed as per User Request -->
        </main>
    </div>
"""
script_part = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        function triggerConfetti() {
            confetti({
                particleCount: 100,
                spread: 70,
                origin: { y: 0.6 }
            });
        }
    </script>
</body>
</html>
"""

new_content = head_part + banner_part + sidebar_part + script_part

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully cleared content from Data-Module-1.html")
