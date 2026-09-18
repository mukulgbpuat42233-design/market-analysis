import sys

with open('index.html', 'r') as f:
    content = f.read()

# Tab Monthly
old_monthly = """html=table(['S.No.','Month','Year','Selected Blocks','Record Count','Average MCP','Maximum MCP','Minimum MCP','Median','Price Spread'],rows.map((x,i)=>{const [y,m]=x.key.split('-');return [i+1,mName(+m),y,r.blocks.join(', '),x.count,fmt(x.avg),fmt(x.max),fmt(x.min),fmt(x.median),fmt(x.spread)]}));"""
new_monthly = """html=table(['S.No.','Month','Year','Selected Blocks','Record Count','Average MCP','Weighted Avg (Vol)','Maximum MCP','Minimum MCP','Median','Price Spread'],rows.map((x,i)=>{const [y,m]=x.key.split('-');return [i+1,mName(+m),y,r.blocks.join(', '),x.count,fmt(x.avg),fmt(x.weightedAvg),fmt(x.max),fmt(x.min),fmt(x.median),fmt(x.spread)]}));"""
content = content.replace(old_monthly, new_monthly)

# Tab Weekly
old_weekly = """html=table(['S.No.','Week','Selected Blocks','Record Count','Average MCP','Maximum MCP','Minimum MCP','Median','Price Spread'],rows.map((x,i)=>[i+1,x.key,r.blocks.join(', '),x.count,fmt(x.avg),fmt(x.max),fmt(x.min),fmt(x.median),fmt(x.spread)]));"""
new_weekly = """html=table(['S.No.','Week','Selected Blocks','Record Count','Average MCP','Weighted Avg (Vol)','Maximum MCP','Minimum MCP','Median','Price Spread'],rows.map((x,i)=>[i+1,x.key,r.blocks.join(', '),x.count,fmt(x.avg),fmt(x.weightedAvg),fmt(x.max),fmt(x.min),fmt(x.median),fmt(x.spread)]));"""
content = content.replace(old_weekly, new_weekly)

# Tab Yearly
old_yearly = """html=table(['S.No.','Year','Selected Blocks','Record Count','Average MCP','Maximum MCP','Minimum MCP','Median','Price Spread'],rows.map((x,i)=>[i+1,x.key,r.blocks.join(', '),x.count,fmt(x.avg),fmt(x.max),fmt(x.min),fmt(x.median),fmt(x.spread)]));"""
new_yearly = """html=table(['S.No.','Year','Selected Blocks','Record Count','Average MCP','Weighted Avg (Vol)','Maximum MCP','Minimum MCP','Median','Price Spread'],rows.map((x,i)=>[i+1,x.key,r.blocks.join(', '),x.count,fmt(x.avg),fmt(x.weightedAvg),fmt(x.max),fmt(x.min),fmt(x.median),fmt(x.spread)]));"""
content = content.replace(old_yearly, new_yearly)

# Tab Daily
old_daily = """html=table(['S.No.','Date','Selected Blocks','Record Count','Average MCP','Maximum MCP','Minimum MCP','Median','Price Spread'],rows.map((x,i)=>[i+1,x.key,r.blocks.join(', '),x.count,fmt(x.avg),fmt(x.max),fmt(x.min),fmt(x.median),fmt(x.spread)]));"""
new_daily = """html=table(['S.No.','Date','Selected Blocks','Record Count','Average MCP','Weighted Avg (Vol)','Maximum MCP','Minimum MCP','Median','Price Spread'],rows.map((x,i)=>[i+1,x.key,r.blocks.join(', '),x.count,fmt(x.avg),fmt(x.weightedAvg),fmt(x.max),fmt(x.min),fmt(x.median),fmt(x.spread)]));"""
content = content.replace(old_daily, new_daily)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched basic tables")
