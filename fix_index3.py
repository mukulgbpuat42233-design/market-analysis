import re

with open('index.html', 'r') as f:
    content = f.read()

# find the <script type="module"> after "printAiReport()"
idx_print = content.find("function printAiReport()")
idx_start = content.find("      <script type=\"module\">", idx_print)
idx_end = content.find("</script></body>", idx_start)

if idx_start != -1 and idx_end != -1:
    bad_part = content[idx_start : idx_end + len("</script>")]
    content = content.replace(bad_part, "")
    with open('index.html', 'w') as f:
        f.write(content)
    print("Fixed!")
else:
    print("Could not find limits")
