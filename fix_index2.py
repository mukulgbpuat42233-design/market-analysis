import re

with open('index.html', 'r') as f:
    content = f.read()

# Let's find exactly the spot to remove
start_str = "      <script type=\"module\">"
# find the first occurrence of start_str after "printAiReport"
idx_print = content.find("function printAiReport()")
if idx_print != -1:
    idx_start = content.find(start_str, idx_print)
    if idx_start != -1:
        # find the next </script></body>
        idx_end = content.find("</script></body>", idx_start)
        if idx_end != -1:
            bad_part = content[idx_start : idx_end + len("</script></body>")]
            print("Found bad part, removing it")
            content = content.replace(bad_part, "</body>")
            with open('index.html', 'w') as f:
                f.write(content)
            print("Successfully removed bad injection")
        else:
            print("Could not find </script></body>")
    else:
        print("Could not find start_str")
else:
    print("Could not find printAiReport")

