import sys

with open('index.html', 'r') as f:
    content = f.read()

old_month_stats = """function reportMonthStats(rows){
  const vals=rows.map(x=>x.mcp).filter(v=>typeof v==='number'&&Number.isFinite(v));
  if(!vals.length) return {count:0,avg:0,max:0,min:0,maxRow:null,minRow:null,maxAudit:'N/A',minAudit:'N/A',finalAudit:'N/A'};
  const max=Math.max(...vals);
  const positives=vals.filter(v=>v>0);
  const min=positives.length?Math.min(...positives):0;
  const maxRow=rows.find(x=>x.mcp===max)||null;
  const minRow=rows.find(x=>x.mcp===min)||null;
  const maxAudit=max<=10000?'OK':'ERROR';
  const minAudit=min>=0?'OK':'ERROR';
  const finalAudit=maxAudit==='OK'&&minAudit==='OK'?'✓ VERIFIED':'✗ CHECK';
  return {count:rows.length,avg:avg(vals)||0,max,min,maxRow,minRow,maxAudit,minAudit,finalAudit};
}"""

new_month_stats = """function reportMonthStats(rows){
  const valid=rows.filter(x=>typeof x.mcp==='number'&&Number.isFinite(x.mcp));
  const vals=valid.map(x=>x.mcp);
  if(!vals.length) return {count:0,avg:0,weightedAvg:0,max:0,min:0,maxRow:null,minRow:null,maxAudit:'N/A',minAudit:'N/A',finalAudit:'N/A'};
  
  let sumProduct=0; let sumVol=0;
  valid.forEach(r => {
    const vol = (typeof r.volume === 'number' && !isNaN(r.volume)) ? r.volume : 1;
    sumProduct += r.mcp * vol;
    sumVol += vol;
  });
  const weightedAvg = sumVol > 0 ? (sumProduct / sumVol) : (avg(vals) || 0);

  const max=Math.max(...vals);
  const positives=vals.filter(v=>v>0);
  const min=positives.length?Math.min(...positives):0;
  const maxRow=valid.find(x=>x.mcp===max)||null;
  const minRow=valid.find(x=>x.mcp===min)||null;
  const maxAudit=max<=10000?'OK':'ERROR';
  const minAudit=min>=0?'OK':'ERROR';
  const finalAudit=maxAudit==='OK'&&minAudit==='OK'?'✓ VERIFIED':'✗ CHECK';
  return {count:valid.length,avg:avg(vals)||0,weightedAvg,max,min,maxRow,minRow,maxAudit,minAudit,finalAudit};
}"""
content = content.replace(old_month_stats, new_month_stats)

old_metric_defs = """  const metricDefs={
    selectedBlocks:['Selected Blocks', x=>x.count?x.count.toLocaleString():'0','count'],
    avg:['Selected Average MCP (₹/MWh)', x=>fmt(x.avg),'avg'],
    max:['Maximum MCP (₹/MWh)', x=>fmt(x.max),'max'],"""
new_metric_defs = """  const metricDefs={
    selectedBlocks:['Selected Blocks', x=>x.count?x.count.toLocaleString():'0','count'],
    avg:['Selected Average MCP (₹/MWh)', x=>fmt(x.avg),'avg'],
    weightedAvg:['Weighted Avg (Volume) ₹/MWh', x=>fmt(x.weightedAvg),'avg'],
    max:['Maximum MCP (₹/MWh)', x=>fmt(x.max),'max'],"""
content = content.replace(old_metric_defs, new_metric_defs)

old_groups = """  const groupDefs=[
    ['Market Summary',['selectedBlocks','avg','max','min']],"""
new_groups = """  const groupDefs=[
    ['Market Summary',['selectedBlocks','avg','weightedAvg','max','min']],"""
content = content.replace(old_groups, new_groups)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched report calculations")
