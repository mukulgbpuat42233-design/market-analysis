import re

with open('index.html', 'r') as f:
    content = f.read()

idx_print = content.find("function printAiReport()")
idx_start = content.find("<script type=\"module\">", idx_print)

# Just find the FIRST </script> after idx_start
idx_end = content.find("</script>", idx_start)

if idx_start != -1 and idx_end != -1:
    bad_part = content[idx_start : idx_end + len("</script>")]
    content = content.replace(bad_part, "")
    with open('index.html', 'w') as f:
        f.write(content)
    print("Fixed!")
else:
    print("Could not find limits", idx_start, idx_end)
