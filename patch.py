import sys

with open('index.html', 'r') as f:
    content = f.read()

old_func = "function clearSelection(){ $('customBlocks').value='';$('b1').value=1;$('b2').value=96; if(S.rows.length)setDateDefaults() }"
new_func = """function clearSelection(){ 
  if (confirm('Are you sure you want to reset your selection? Any active segment-specific analysis calculations, including growth tracking, will be reset.')) {
    $('customBlocks').value='';$('b1').value=1;$('b2').value=96; if(S.rows.length)setDateDefaults();
  }
}"""

if old_func in content:
    content = content.replace(old_func, new_func)
    with open('index.html', 'w') as f:
        f.write(content)
    print("Updated clearSelection")
else:
    print("Could not find clearSelection")
