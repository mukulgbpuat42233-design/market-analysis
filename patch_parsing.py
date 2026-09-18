import sys

with open('index.html', 'r') as f:
    content = f.read()

# Patch 1: findHeaderRowAndIndexes
old_header = "const selected=headerIndex(r,['Selected','Selected?','Selected Block','Selection']);"
new_header = """const selected=headerIndex(r,['Selected','Selected?','Selected Block','Selection']);
    const volume=headerIndex(r,['MCV','Volume','Final Scheduled Volume','Final Scheduled Vol','Scheduled Volume','Scheduled Vol','Volume MW','Volume MWh','Total Volume','Total Vol','Market Clearing Volume','MCV MW','MCV MWh']);"""
content = content.replace(old_header, new_header)

old_return = "return {row:i,date,block,time,mcp,hour:headerIndex(r,['Hour']),selected};"
new_return = "return {row:i,date,block,time,mcp,volume,hour:headerIndex(r,['Hour']),selected};"
content = content.replace(old_return, new_return)

# Patch 2: Single import
old_single_extract = """const mcp = mcpBlank ? null : num(raw);
      const selected = meta.selected >= 0 ? String(x[meta.selected] ?? '').trim().toUpperCase() === 'YES' : null;"""
new_single_extract = """const mcp = mcpBlank ? null : num(raw);
      const volumeRaw = meta.volume >= 0 ? x[meta.volume] : null;
      const volumeBlank = volumeRaw === null || volumeRaw === undefined || String(volumeRaw).trim() === '';
      const volume = volumeBlank ? null : num(volumeRaw);
      const selected = meta.selected >= 0 ? String(x[meta.selected] ?? '').trim().toUpperCase() === 'YES' : null;"""
content = content.replace(old_single_extract, new_single_extract)

old_single_push = "date: d, hour, block, time, mcp, mcpBlank, invalidMcp,"
new_single_push = "date: d, hour, block, time, mcp, mcpBlank, invalidMcp, volume,"
content = content.replace(old_single_push, new_single_push)

# Patch 3: Batch import
old_batch_extract = """const mcp = mcpBlank ? null : num(raw);"""
new_batch_extract = """const mcp = mcpBlank ? null : num(raw);
          const volumeRaw = meta.volume >= 0 ? x[meta.volume] : null;
          const volumeBlank = volumeRaw === null || volumeRaw === undefined || String(volumeRaw).trim() === '';
          const volume = volumeBlank ? null : num(volumeRaw);"""
content = content.replace(old_batch_extract, new_batch_extract)

old_batch_push = "date: d, hour, block, time, mcp"
new_batch_push = "date: d, hour, block, time, mcp, volume"
content = content.replace(old_batch_push, new_batch_push)

with open('index.html', 'w') as f:
    f.write(content)

print("Patched parsing logic")
