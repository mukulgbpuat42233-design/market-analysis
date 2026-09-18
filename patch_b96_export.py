import sys

with open('index.html', 'r') as f:
    content = f.read()

old_b96 = """  const blockValues = Array.from({ length: 97 }, () => []);
  for (const x of r.inRange) {
    if (x.block >= 1 && x.block <= 96 && typeof x.mcp === 'number' && Number.isFinite(x.mcp)) {
      blockValues[x.block].push(x.mcp);
    }
  }
  for (let b = 1; b <= 96; b++) {
    const v = blockValues[b];
    b96.push([
      b, timeForBlock(b), Math.floor((b - 1) / 4) + 1,
      r.blocks.includes(b) ? 'YES' : 'NO',
      v.length, avg(v),
      v.length ? Math.max(...v) : null,
      v.length ? Math.min(...v) : null,
      median(v),
      v.length ? Math.max(...v) - Math.min(...v) : null
    ]);
  }"""

new_b96 = """  const blockValues = Array.from({ length: 97 }, () => []);
  for (const x of r.inRange) {
    if (x.block >= 1 && x.block <= 96 && typeof x.mcp === 'number' && Number.isFinite(x.mcp)) {
      const vol = (typeof x.volume === 'number' && !isNaN(x.volume)) ? x.volume : 1;
      blockValues[x.block].push({mcp: x.mcp, volume: vol});
    }
  }
  for (let b = 1; b <= 96; b++) {
    const v_objs = blockValues[b];
    const mcps = v_objs.map(o => o.mcp);
    let sumProduct = 0; let sumVol = 0;
    v_objs.forEach(o => { sumProduct += o.mcp * o.volume; sumVol += o.volume; });
    const wAvg = sumVol > 0 ? (sumProduct / sumVol) : avg(mcps);
    
    b96.push([
      b, timeForBlock(b), Math.floor((b - 1) / 4) + 1,
      r.blocks.includes(b) ? 'YES' : 'NO',
      v_objs.length, avg(mcps), wAvg,
      v_objs.length ? Math.max(...mcps) : null,
      v_objs.length ? Math.min(...mcps) : null,
      median(mcps),
      v_objs.length ? Math.max(...mcps) - Math.min(...mcps) : null
    ]);
  }"""

content = content.replace(old_b96, new_b96)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched b96 export array")
