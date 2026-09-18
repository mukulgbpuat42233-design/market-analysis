import sys

with open('index.html', 'r') as f:
    content = f.read()

old_header = """      ['Period', 'Record Count', 'Average MCP (₹/MWh)', 'Maximum MCP (₹/MWh)', 'Minimum MCP (₹/MWh)', 'Median MCP (₹/MWh)', 'Price Spread (₹/MWh)'],"""
new_header = """      ['Period', 'Record Count', 'Average MCP (₹/MWh)', 'Weighted Avg (Vol)', 'Maximum MCP (₹/MWh)', 'Minimum MCP (₹/MWh)', 'Median MCP (₹/MWh)', 'Price Spread (₹/MWh)'],"""
content = content.replace(old_header, new_header)

old_cols = """    wsPeriod['!cols'] = [{ wch: 16 }, { wch: 14 }, { wch: 22 }, { wch: 22 }, { wch: 22 }, { wch: 22 }, { wch: 22 }];
    applyHeader(wsPeriod, { s: { c: 0 }, e: { c: 6 } }, 0, headerStyle);"""
new_cols = """    wsPeriod['!cols'] = [{ wch: 16 }, { wch: 14 }, { wch: 22 }, { wch: 22 }, { wch: 22 }, { wch: 22 }, { wch: 22 }, { wch: 22 }];
    applyHeader(wsPeriod, { s: { c: 0 }, e: { c: 7 } }, 0, headerStyle);"""
content = content.replace(old_cols, new_cols)

# We also need to fix the reference letters in the Excel export for periodic sheets
old_refs = """      const refAvg = 'C' + rowIdx;
      if (wsPeriod[refAvg]) {
        wsPeriod[refAvg].s = { fill: { fgColor: { rgb: "EFF6FF" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "1D4ED8" } }, alignment: { horizontal: "right" }, border: thinBorder };
        wsPeriod[refAvg].z = '₹#,##0.00';
      }
      const refMax = 'D' + rowIdx;
      if (wsPeriod[refMax]) {
        wsPeriod[refMax].s = { fill: { fgColor: { rgb: "FEF2F2" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "DC2626" } }, alignment: { horizontal: "right" }, border: thinBorder };
        wsPeriod[refMax].z = '₹#,##0.00';
      }
      const refMin = 'E' + rowIdx;
      if (wsPeriod[refMin]) {
        wsPeriod[refMin].s = { fill: { fgColor: { rgb: "F0FDF4" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "16A34A" } }, alignment: { horizontal: "right" }, border: thinBorder };
        wsPeriod[refMin].z = '₹#,##0.00';
      }
      const refMed = 'F' + rowIdx;
      if (wsPeriod[refMed]) {
        wsPeriod[refMed].s = { fill: { fgColor: { rgb: bg } }, font: { name: "Arial", sz: 10 }, alignment: { horizontal: "right" }, border: thinBorder };
        wsPeriod[refMed].z = '₹#,##0.00';
      }
      const refSpr = 'G' + rowIdx;"""
new_refs = """      const refAvg = 'C' + rowIdx;
      if (wsPeriod[refAvg]) {
        wsPeriod[refAvg].s = { fill: { fgColor: { rgb: "EFF6FF" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "1D4ED8" } }, alignment: { horizontal: "right" }, border: thinBorder };
        wsPeriod[refAvg].z = '₹#,##0.00';
      }
      const refWAvg = 'D' + rowIdx;
      if (wsPeriod[refWAvg]) {
        wsPeriod[refWAvg].s = { fill: { fgColor: { rgb: "F5F3FF" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "6D28D9" } }, alignment: { horizontal: "right" }, border: thinBorder };
        wsPeriod[refWAvg].z = '₹#,##0.00';
      }
      const refMax = 'E' + rowIdx;
      if (wsPeriod[refMax]) {
        wsPeriod[refMax].s = { fill: { fgColor: { rgb: "FEF2F2" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "DC2626" } }, alignment: { horizontal: "right" }, border: thinBorder };
        wsPeriod[refMax].z = '₹#,##0.00';
      }
      const refMin = 'F' + rowIdx;
      if (wsPeriod[refMin]) {
        wsPeriod[refMin].s = { fill: { fgColor: { rgb: "F0FDF4" } }, font: { name: "Arial", sz: 10, bold: true, color: { rgb: "16A34A" } }, alignment: { horizontal: "right" }, border: thinBorder };
        wsPeriod[refMin].z = '₹#,##0.00';
      }
      const refMed = 'G' + rowIdx;
      if (wsPeriod[refMed]) {
        wsPeriod[refMed].s = { fill: { fgColor: { rgb: bg } }, font: { name: "Arial", sz: 10 }, alignment: { horizontal: "right" }, border: thinBorder };
        wsPeriod[refMed].z = '₹#,##0.00';
      }
      const refSpr = 'H' + rowIdx;"""
content = content.replace(old_refs, new_refs)

with open('index.html', 'w') as f:
    f.write(content)
print("Patched periodic Excel styles")
