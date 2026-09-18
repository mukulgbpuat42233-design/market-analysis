import sys

with open('index.html', 'r') as f:
    content = f.read()

old_group = """function groupRows(keyFn){
  const m=new Map();
  for(const r of S.results.valid){const k=keyFn(r);if(!m.has(k))m.set(k,[]);m.get(k).push(r.mcp)}
  return [...m.entries()].map(([k,v])=>({key:k,count:v.length,avg:avg(v),max:Math.max(...v),min:Math.min(...v),median:median(v),spread:Math.max(...v)-Math.min(...v)}));
}"""
new_group = """function groupRows(keyFn){
  const m=new Map();
  for(const r of S.results.valid){
    const k=keyFn(r);
    if(!m.has(k))m.set(k,[]);
    const vol = (typeof r.volume === 'number' && !isNaN(r.volume)) ? r.volume : 1;
    m.get(k).push({ mcp: r.mcp, volume: vol });
  }
  return [...m.entries()].map(([k,v])=>{
    const mcps = v.map(x => x.mcp);
    let sumProduct = 0; let sumVol = 0;
    v.forEach(x => { sumProduct += x.mcp * x.volume; sumVol += x.volume; });
    const wAvg = sumVol > 0 ? (sumProduct / sumVol) : avg(mcps);
    return {
      key:k, count:v.length, avg:avg(mcps), weightedAvg: wAvg,
      max:Math.max(...mcps), min:Math.min(...mcps), median:median(mcps), spread:Math.max(...mcps)-Math.min(...mcps)
    };
  });
}"""
content = content.replace(old_group, new_group)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched groupRows")
