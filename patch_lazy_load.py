import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <img without loading= with <img loading="lazy"
new_content = re.sub(r'<img(?![^>]*\bloading=)([^>]*)>', r'<img loading="lazy"\1>', content, flags=re.IGNORECASE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Patch applied.")
