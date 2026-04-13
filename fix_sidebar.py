import os
import re

new_css = """\.quick-contact-bar {
            position: fixed;
            top: 50%;
            right: 0;
            transform: translateY(-50%);
            background: #1e1e1e;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 15px 0;
            width: 64px;
            z-index: 9999;
            box-shadow: -4px 0 15px rgba(0,0,0,0.25);
            border-radius: 12px 0 0 12px;
            box-sizing: border-box;
        }
        .quick-contact-bar a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            margin: 6px 0;
            border-radius: 50%;
            transition: transform 0.2s;
            text-decoration: none;
            box-sizing: border-box;
        }
        .quick-contact-bar a:hover {
            transform: scale(1.1);
        }
        .qc-phone {
            background-color: #2196f3;
        }
        .qc-whatsapp {
            background-color: #4caf50;
        }
        .qc-email {
            background: linear-gradient(135deg, #ef5350, #ffb74d);
        }
        .qc-icon {
            width: 22px;
            height: 22px;
            fill: white;
            display: block;
        }
        .qc-divider {
            width: 60%;
            height: 1px;
            background: rgba(255,255,255,0.15);
            margin: 4px 0;
        }"""

# Remove the escaped dot before quick-contact-bar for actual replacement text
replacement_text = new_css.replace('\.quick-contact-bar', '.quick-contact-bar')

fixed_count = 0
for filename in os.listdir("."):
    if filename.endswith(".html"):
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        if ".quick-contact-bar" in content:
            # We'll replace everything from .quick-contact-bar { to the end of .qc-divider { ... }
            pattern = re.compile(r'\.quick-contact-bar\s*\{.*?\.qc-divider\s*\{[^\}]*\}', re.DOTALL)
            
            if pattern.search(content):
                content = pattern.sub(replacement_text, content)
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(content)
                fixed_count += 1
                
print(f"Fixed sidebar CSS in {fixed_count} files.")
