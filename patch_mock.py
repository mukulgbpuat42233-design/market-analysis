import sys

with open('index.html', 'r') as f:
    content = f.read()

old_mock = """        mcp = Math.max(750, Math.min(9950, mcp));

      rows.push({
        date: curDate,
        hour: hour,
        block: b,
        time: time,
        mcp: mcp
      });"""

new_mock = """        mcp = Math.max(750, Math.min(9950, mcp));
        
        // Mock Final Scheduled Volume (MCV) based on shape + segment
        let baseVol = segment === 'DAM' ? 250 : (segment === 'RTM' ? 50 : 100);
        let vol = Math.max(5, Math.round(baseVol * shape * (1 + (Math.random() * 0.2 - 0.1))));

      rows.push({
        date: curDate,
        hour: hour,
        block: b,
        time: time,
        mcp: mcp,
        volume: vol
      });"""

content = content.replace(old_mock, new_mock)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched generator")
