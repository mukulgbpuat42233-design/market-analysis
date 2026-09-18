import sys

with open('index.html', 'r') as f:
    content = f.read()

old_export_summary = """['Average Market Clearing Price (MCP)', r.avg],
    ['Maximum Peak MCP', r.max],"""
new_export_summary = """['Average Market Clearing Price (MCP)', r.avg],
    ['Weighted Average MCP (by Volume)', r.weightedAvg],
    ['Maximum Peak MCP', r.max],"""
content = content.replace(old_export_summary, new_export_summary)

old_export_periods = """['Period', 'Record Count', 'Average MCP (₹/MWh)', 'Maximum MCP (₹/MWh)', 'Minimum MCP (₹/MWh)', 'Median (₹/MWh)', 'Price Spread']"""
new_export_periods = """['Period', 'Record Count', 'Average MCP (₹/MWh)', 'Weighted Avg MCP (₹/MWh)', 'Maximum MCP (₹/MWh)', 'Minimum MCP (₹/MWh)', 'Median (₹/MWh)', 'Price Spread']"""
content = content.replace(old_export_periods, new_export_periods)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched export")
