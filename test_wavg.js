const mcp = [1000, 2000, 3000];
const vol = [10, 20, 30];
const v = mcp.map((m, i) => ({mcp: m, volume: vol[i]}));

let sumProduct = 0; let sumVol = 0;
v.forEach(x => { sumProduct += x.mcp * x.volume; sumVol += x.volume; });
const wAvg = sumVol > 0 ? (sumProduct / sumVol) : 0;
console.log("wAvg", wAvg);
