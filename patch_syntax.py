import sys

with open('index.html', 'r') as f:
    content = f.read()

bad_snippet = """          const volumeRaw = meta.volume >= 0 ? x[meta.volume] : null;
          const volumeBlank = volumeRaw === null || volumeRaw === undefined || String(volumeRaw).trim() === '';
          const volume = volumeBlank ? null : num(volumeRaw);
      const volumeRaw = meta.volume >= 0 ? x[meta.volume] : null;
      const volumeBlank = volumeRaw === null || volumeRaw === undefined || String(volumeRaw).trim() === '';
      const volume = volumeBlank ? null : num(volumeRaw);"""

good_snippet = """      const volumeRaw = meta.volume >= 0 ? x[meta.volume] : null;
      const volumeBlank = volumeRaw === null || volumeRaw === undefined || String(volumeRaw).trim() === '';
      const volume = volumeBlank ? null : num(volumeRaw);"""

if bad_snippet in content:
    content = content.replace(bad_snippet, good_snippet)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Patched syntax error")
else:
    print("Snippet not found")
