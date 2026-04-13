import os
import re

html_block = """    <div class="quick-contact-bar">
        <a href="tel:+918593850720" class="qc-phone" title="Call Us">
            <svg class="qc-icon" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
        </a>
        <div class="qc-divider"></div>
        <a href="https://wa.me/918593850720" class="qc-whatsapp" title="WhatsApp Us" target="_blank">
            <svg class="qc-icon" viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.71.44 3.32 1.24 4.74L2 22l5.48-1.44c1.38.74 2.95 1.15 4.56 1.15 5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2zm0 18.22c-1.42 0-2.8-.38-4.04-1.11l-.29-.17-3 .79.8-2.92-.19-.3A8.09 8.09 0 013.93 11.9c0-4.47 3.63-8.1 8.1-8.1 4.47 0 8.1 3.63 8.1 8.1s-3.63 8.1-8.1 8.1zm4.45-6.04c-.24-.12-1.44-.71-1.66-.79-.22-.08-.38-.12-.54.12-.16.24-.62.79-.76.95-.14.16-.28.18-.52.06-1.54-.74-2.6-1.39-3.6-2.92-.12-.18 0-.28.12-.4.12-.12.24-.28.36-.42.12-.14.16-.24.24-.4.08-.16.04-.3-.02-.42-.06-.12-.54-1.3-.74-1.78-.2-.48-.4-.42-.54-.42h-.46c-.16 0-.42.06-.64.3-.22.24-.84.82-.84 2s.86 2.32.98 2.48c.12.16 1.68 2.56 4.08 3.56.58.24 1.02.38 1.38.48.58.18 1.1.16 1.52.1.46-.08 1.44-.58 1.64-1.14.2-.56.2-1.04.14-1.14-.06-.1-.22-.16-.46-.28z"/></svg>
        </a>
        <div class="qc-divider"></div>
        <a href="mailto:info@thestrategist.co.in" class="qc-email" title="Email Us">
            <svg class="qc-icon" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </a>
    </div>"""

css_block = """<style>
        .quick-contact-bar {
            position: fixed;
            top: 50%;
            right: 0;
            transform: translateY(-50%);
            background: #111;
            display: flex;
            flex-direction: column;
            padding: 10px 5px;
            z-index: 9999;
            box-shadow: -2px 0 10px rgba(0,0,0,0.5);
        }
        .quick-contact-bar a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            margin: 5px 0;
            border-radius: 50%;
            transition: transform 0.2s;
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
            width: 24px;
            height: 24px;
            fill: white;
        }
        .qc-divider {
            width: 100%;
            height: 1px;
            background: #333;
            margin: 5px 0;
        }
    </style>"""

directory = r"c:\Users\kj anand\Downloads\Quiz DD"

count_updated = 0
count_added = 0
count_skipped = 0

for filename in os.listdir(directory):
    if not filename.endswith(".html"):
        continue
    
    if "quiz" in filename.lower():
        count_skipped += 1
        continue
        
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # Check if contact bar is present
    if "quick-contact-bar" in content:
        # Update email if old one is found inside qc-email
        # We can also just globally find mailto:.*?" class="qc-email"
        new_content = re.sub(r'href="mailto:[^"]*"\s+class="qc-email"', 'href="mailto:info@thestrategist.co.in" class="qc-email"', content)
        if new_content != content:
            content = new_content
            modified = True
        count_updated += 1
    else:
        # Add CSS and HTML
        # Insert CSS just before </style> or in <head>
        if "</head>" in content:
            content = content.replace("</head>", f"{css_block}\n</head>")
            # Insert HTML just before </body>
            if "</body>" in content:
                content = content.replace("</body>", f"{html_block}\n</body>")
            modified = True
            count_added += 1

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print(f"Added to {count_added} files.")
print(f"Updated in {count_updated} files.")
print(f"Skipped {count_skipped} files.")
