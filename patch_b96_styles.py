import sys

with open('index.html', 'r') as f:
    content = f.read()

old_cols_96 = """  ws96['!cols'] = [{ wch: 10 }, { wch: 18 }, { wch: 8 }, { wch: 12 }, { wch: 14 }, { wch: 16 }, { wch: 16 }, { wch: 16 }, { wch: 16 }, { wch: 16 }];
  applyHeader(ws96, { s: { c: 0 }, e: { c: 9 } }, 0, headerStyle);"""
new_cols_96 = """  ws96['!cols'] = [{ wch: 10 }, { wch: 18 }, { wch: 8 }, { wch: 12 }, { wch: 14 }, { wch: 16 }, { wch: 16 }, { wch: 16 }, { wch: 16 }, { wch: 16 }, { wch: 16 }];
  applyHeader(ws96, { s: { c: 0 }, e: { c: 10 } }, 0, headerStyle);"""
content = content.replace(old_cols_96, new_cols_96)

old_refs_96 = """    const refAvg = 'F' + rowIdx;
    if (ws96[refAvg]) {
      ws96[refAvg].s = { fill: { fgColor: { rgb: isSolar ? "FEF9C3" : (isPeak ? "FFEDD5" : "EFF6FF") } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: isPeak ? "C2410C" : "1D4ED8" } }, alignment: { horizontal: "right" }, border: thinBorder };
      ws96[refAvg].z = '₹#,##0.00';
    }
    const refMax = 'G' + rowIdx;
    if (ws96[refMax]) {
      ws96[refMax].s = { fill: { fgColor: { rgb: "FEF2F2" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "DC2626" } }, alignment: { horizontal: "right" }, border: thinBorder };
      ws96[refMax].z = '₹#,##0.00';
    }
    const refMin = 'H' + rowIdx;
    if (ws96[refMin]) {
      ws96[refMin].s = { fill: { fgColor: { rgb: "F0FDF4" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "16A34A" } }, alignment: { horizontal: "right" }, border: thinBorder };
      ws96[refMin].z = '₹#,##0.00';
    }
    const refMed = 'I' + rowIdx;
    if (ws96[refMed]) {
      ws96[refMed].s = { fill: { fgColor: { rgb: rowBg } }, font: { name: "Arial", sz: 10 }, alignment: { horizontal: "right" }, border: thinBorder };
      ws96[refMed].z = '₹#,##0.00';
    }
    const refSpr = 'J' + rowIdx;"""
new_refs_96 = """    const refAvg = 'F' + rowIdx;
    if (ws96[refAvg]) {
      ws96[refAvg].s = { fill: { fgColor: { rgb: isSolar ? "FEF9C3" : (isPeak ? "FFEDD5" : "EFF6FF") } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: isPeak ? "C2410C" : "1D4ED8" } }, alignment: { horizontal: "right" }, border: thinBorder };
      ws96[refAvg].z = '₹#,##0.00';
    }
    const refWAvg = 'G' + rowIdx;
    if (ws96[refWAvg]) {
      ws96[refWAvg].s = { fill: { fgColor: { rgb: isSolar ? "FEF9C3" : (isPeak ? "FFEDD5" : "F5F3FF") } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "6D28D9" } }, alignment: { horizontal: "right" }, border: thinBorder };
      ws96[refWAvg].z = '₹#,##0.00';
    }
    const refMax = 'H' + rowIdx;
    if (ws96[refMax]) {
      ws96[refMax].s = { fill: { fgColor: { rgb: "FEF2F2" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "DC2626" } }, alignment: { horizontal: "right" }, border: thinBorder };
      ws96[refMax].z = '₹#,##0.00';
    }
    const refMin = 'I' + rowIdx;
    if (ws96[refMin]) {
      ws96[refMin].s = { fill: { fgColor: { rgb: "F0FDF4" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "16A34A" } }, alignment: { horizontal: "right" }, border: thinBorder };
      ws96[refMin].z = '₹#,##0.00';
    }
    const refMed = 'J' + rowIdx;
    if (ws96[refMed]) {
      ws96[refMed].s = { fill: { fgColor: { rgb: rowBg } }, font: { name: "Arial", sz: 10 }, alignment: { horizontal: "right" }, border: thinBorder };
      ws96[refMed].z = '₹#,##0.00';
    }
    const refSpr = 'K' + rowIdx;"""
content = content.replace(old_refs_96, new_refs_96)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched 96 block Excel styles")
