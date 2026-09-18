import sys

with open('index.html', 'r') as f:
    content = f.read()

old_blocks96 = """  } else if(tab==='blocks96'){
    const m=new Map(); for(const b of Array.from({length:96},(_,i)=>i+1)){m.set(b,[])}
    for(const x of r.inRange)if(typeof x.mcp==='number')m.get(x.block)?.push(x.mcp);
    const rows=[...m.entries()].map(([b,v])=>({b,v}));
    html=table(['Block No.','Time Block','Hour','Selected?','Record Count','Average MCP','Maximum MCP','Minimum MCP','Median','Price Spread'],rows.map(x=>{
      const b=x.b,v=x.v;return [b,timeForBlock(b),Math.floor((b-1)/4)+1,r.blocks.includes(b)?'YES':'NO',v.length,fmt(avg(v)),fmt(v.length?Math.max(...v):null),fmt(v.length?Math.min(...v):null),fmt(median(v)),fmt(v.length?Math.max(...v)-Math.min(...v):null)]
    }));"""

new_blocks96 = """  } else if(tab==='blocks96'){
    const m=new Map(); for(const b of Array.from({length:96},(_,i)=>i+1)){m.set(b,[])}
    for(const x of r.inRange){
      if(typeof x.mcp==='number'){
        const vol = (typeof x.volume === 'number' && !isNaN(x.volume)) ? x.volume : 1;
        m.get(x.block)?.push({mcp: x.mcp, volume: vol});
      }
    }
    const rows=[...m.entries()].map(([b,v])=>({b,v}));
    html=table(['Block No.','Time Block','Hour','Selected?','Record Count','Average MCP','Weighted Avg (Vol)','Maximum MCP','Minimum MCP','Median','Price Spread'],rows.map(x=>{
      const b=x.b, v_objs=x.v;
      const mcps = v_objs.map(o => o.mcp);
      let sumProduct = 0; let sumVol = 0;
      v_objs.forEach(o => { sumProduct += o.mcp * o.volume; sumVol += o.volume; });
      const wAvg = sumVol > 0 ? (sumProduct / sumVol) : avg(mcps);
      return [b,timeForBlock(b),Math.floor((b-1)/4)+1,r.blocks.includes(b)?'YES':'NO',v_objs.length,fmt(avg(mcps)),fmt(wAvg),fmt(v_objs.length?Math.max(...mcps):null),fmt(v_objs.length?Math.min(...mcps):null),fmt(median(mcps)),fmt(v_objs.length?Math.max(...mcps)-Math.min(...mcps):null)]
    }));"""

content = content.replace(old_blocks96, new_blocks96)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched blocks96 table")
