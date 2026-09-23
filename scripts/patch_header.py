import re
from pathlib import Path

p = Path("index.html")
t = p.read_text(encoding="utf-8")

t, n = re.subn(
    r'<div class="wrap">\s*<header id="mast">',
    '<header id="mast">',
    t,
    count=1,
)
print("unwrap", n)
t, n = re.subn(
    r'</header>\s*<main id="panel-pt"',
    '</header>\n<div class="wrap">\n<main id="panel-pt"',
    t,
    count=1,
)
print("rewrap", n)
t, n = re.subn(
    r'padding: 3rem 1.25rem calc\(var\(--chrome-bottom\) \+ 2rem\)',
    'padding: 1.5rem 1.25rem calc(var(--chrome-bottom) + 2rem)',
    t,
    count=1,
)
print("pad", n)
p.write_text(t, encoding="utf-8")
print("order ok", t.find('id="mast"') < t.find('class="wrap"'))
