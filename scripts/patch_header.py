import re
from pathlib import Path

p = Path("index.html")
t = p.read_text(encoding="utf-8")

if '<div class="wrap">' in t and '<header id="mast">' in t:
    t = t.replace('<div class="wrap">\n <header id="mast">', '<header id="mast">', 1)
    t = t.replace('<div class="wrap"><header id="mast">', '<header id="mast">', 1)
    t = t.replace('</header>\n <main id="panel-pt"', '</header>\n<div class="wrap">\n <main id="panel-pt"', 1)
    t = t.replace('</header><main id="panel-pt"', '</header><div class="wrap"><main id="panel-pt"', 1)

t = t.replace(
    '.wrap { max-width: 44rem; margin: 0 auto; padding: 3rem 1.25rem calc(var(--chrome-bottom) + 2rem); }',
    '.wrap { max-width: 44rem; margin: 0 auto; padding: 1.5rem 1.25rem calc(var(--chrome-bottom) + 2rem); }',
)
p.write_text(t, encoding="utf-8")
print("moved", t.find('id="mast"') < t.find('class="wrap"'))
