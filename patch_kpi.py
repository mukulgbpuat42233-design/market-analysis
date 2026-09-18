import sys

with open('index.html', 'r') as f:
    content = f.read()

old_kpis = """$('kpis').innerHTML=[
    ['Selected Blocks',r.blocks.length+' / 96'],
    ['Selected Records',r.valid.length.toLocaleString()],
    ['Average MCP','₹ '+fmt(r.avg)+'/MWh'],
    ['Maximum MCP','₹ '+fmt(r.max)+'/MWh'],
    ['Minimum MCP','₹ '+fmt(r.min)+'/MWh'],
    ['Median / Spread','₹ '+fmt(r.median)+' / ₹ '+fmt(r.spread)]
  ].map(x=>`<div class="kpi"><div class="v">${x[1]}</div><div class="l">${x[0]}</div></div>`).join('');"""

new_kpis = """$('kpis').innerHTML=[
    ['Selected Blocks',r.blocks.length+' / 96'],
    ['Selected Records',r.valid.length.toLocaleString()],
    ['Average MCP','₹ '+fmt(r.avg)+'/MWh'],
    ['Weighted Avg (by Vol)','₹ '+fmt(r.weightedAvg)+'/MWh'],
    ['Maximum MCP','₹ '+fmt(r.max)+'/MWh'],
    ['Minimum MCP','₹ '+fmt(r.min)+'/MWh'],
    ['Median / Spread','₹ '+fmt(r.median)+' / ₹ '+fmt(r.spread)]
  ].map(x=>`<div class="kpi"><div class="v">${x[1]}</div><div class="l">${x[0]}</div></div>`).join('');"""

content = content.replace(old_kpis, new_kpis)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched KPIs")
