import sys

with open('index.html', 'r') as f:
    content = f.read()

# UI Checkbox
old_checkbox = """<label class="metric-option"><input type="checkbox" class="metric-check" value="avg" checked onchange="updateMetricSummary()"><span>Selected Average MCP ₹/MWh</span><b class="metric-order-badge"></b></label>"""
new_checkbox = """<label class="metric-option"><input type="checkbox" class="metric-check" value="avg" checked onchange="updateMetricSummary()"><span>Selected Average MCP ₹/MWh</span><b class="metric-order-badge"></b></label>
            <label class="metric-option"><input type="checkbox" class="metric-check" value="weightedAvg" checked onchange="updateMetricSummary()"><span>Weighted Avg (Volume) ₹/MWh</span><b class="metric-order-badge"></b></label>"""
content = content.replace(old_checkbox, new_checkbox)

# Metric Definitions
old_def = """const metricsDef = {
  selectedBlocks:'Selected Blocks', avg:'Selected Average MCP ₹/MWh', max:'Maximum MCP ₹/MWh', min:'Minimum MCP ₹/MWh',
  maxDate:'Max MCP Date', maxBlock:'Max MCP Block', maxTime:'Max MCP Time', minDate:'Min MCP Date', minBlock:'Min MCP Block', minTime:'Min MCP Time'
};"""
new_def = """const metricsDef = {
  selectedBlocks:'Selected Blocks', avg:'Selected Average MCP ₹/MWh', weightedAvg:'Weighted Avg (Volume) ₹/MWh', max:'Maximum MCP ₹/MWh', min:'Minimum MCP ₹/MWh',
  maxDate:'Max MCP Date', maxBlock:'Max MCP Block', maxTime:'Max MCP Time', minDate:'Min MCP Date', minBlock:'Min MCP Block', minTime:'Min MCP Time'
};"""
content = content.replace(old_def, new_def)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched UI metrics checkboxes and definitions")
