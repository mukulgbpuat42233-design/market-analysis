import sys

with open('index.html', 'r') as f:
    content = f.read()

old_ai = """  if (rowsToAnalyze.length) {
    const mcps = rowsToAnalyze.map(x => x.mcp);
    summary.totalAnalyzedBlocks = rowsToAnalyze.length;
    summary.avgMcp = Math.round(avg(mcps));
    summary.minMcp = Math.min(...mcps);
    summary.maxMcp = Math.max(...mcps);
    summary.medianMcp = Math.round(median(mcps));"""

new_ai = """  if (rowsToAnalyze.length) {
    const mcps = rowsToAnalyze.map(x => x.mcp);
    summary.totalAnalyzedBlocks = rowsToAnalyze.length;
    summary.avgMcp = Math.round(avg(mcps));
    
    let sumProduct = 0; let sumVol = 0;
    rowsToAnalyze.forEach(r => {
      const vol = (typeof r.volume === 'number' && !isNaN(r.volume)) ? r.volume : 1;
      sumProduct += (r.mcp * vol);
      sumVol += vol;
    });
    summary.weightedAvgMcp = sumVol > 0 ? Math.round(sumProduct / sumVol) : summary.avgMcp;

    summary.minMcp = Math.min(...mcps);
    summary.maxMcp = Math.max(...mcps);
    summary.medianMcp = Math.round(median(mcps));"""

content = content.replace(old_ai, new_ai)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched AI summary")
