import json

with open('firebase-applet-config.json') as f:
    config = f.read().strip()

with open('index.html', 'r') as f:
    content = f.read()

import re
content = re.sub(
    r'const firebaseConfig = {[^}]+};',
    f'const firebaseConfig = {config};',
    content
)

with open('index.html', 'w') as f:
    f.write(content)
