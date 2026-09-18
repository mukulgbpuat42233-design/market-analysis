import sys

with open('index.html', 'r') as f:
    content = f.read()

old_results = """const blocks=uiBlocks;
    S.results={blocks,d1,d2,inRange,valid,allSelectedCount:inRange.length,avg:avg(vals),max:mx,min:mn,median:median(vals),spread:mx-mn,
      maxRows:valid.filter(r=>r.mcp===mx),minRows:valid.filter(r=>r.mcp===mn)};"""

new_results = """const blocks=uiBlocks;
    let sumProduct = 0;
    let sumVolume = 0;
    valid.forEach(r => {
      const vol = (typeof r.volume === 'number' && !isNaN(r.volume)) ? r.volume : 1; // Fallback to unweighted if no vol
      sumProduct += (r.mcp * vol);
      sumVolume += vol;
    });
    const weightedAvg = sumVolume > 0 ? (sumProduct / sumVolume) : avg(vals);
    
    S.results={blocks,d1,d2,inRange,valid,allSelectedCount:inRange.length,avg:avg(vals), weightedAvg: weightedAvg, max:mx,min:mn,median:median(vals),spread:mx-mn,
      maxRows:valid.filter(r=>r.mcp===mx),minRows:valid.filter(r=>r.mcp===mn)};"""

content = content.replace(old_results, new_results)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched results calculation")
