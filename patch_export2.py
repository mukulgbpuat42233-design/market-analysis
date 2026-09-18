import sys

with open('index.html', 'r') as f:
    content = f.read()

old_period_map = """...rows.map(x => [x.key, x.count, x.avg, x.max, x.min, x.median, x.spread])"""
new_period_map = """...rows.map(x => [x.key, x.count, x.avg, x.weightedAvg, x.max, x.min, x.median, x.spread])"""
content = content.replace(old_period_map, new_period_map)

old_b96_header = """const b96 = [['Block No.', 'Time Block', 'Hour', 'Selected?', 'Record Count', 'Average MCP', 'Maximum MCP', 'Minimum MCP', 'Median', 'Price Spread']];"""
new_b96_header = """const b96 = [['Block No.', 'Time Block', 'Hour', 'Selected?', 'Record Count', 'Average MCP', 'Weighted Avg (Vol)', 'Maximum MCP', 'Minimum MCP', 'Median', 'Price Spread']];"""
content = content.replace(old_b96_header, new_b96_header)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched export map")
