import re
from pathlib import Path

p = Path("index.html")
t = p.read_text(encoding="utf-8")

css = """
#mast {
  box-sizing: border-box;
  width: 100%;
  margin: 0;
  padding: 1.5rem 1.25rem 1.25rem;
  background: #fff;
  color: #111;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: .35rem;
  border-bottom: 1px solid var(--line);
  font-family: var(--sans);
}
html[data-theme="dark"] #mast { background: #111; color: #f0f0f0; border-bottom-color: #333; }
@media (prefers-color-scheme: dark) {
  html[data-theme="sys"] #mast { background: #111; color: #f0f0f0; border-bottom-color: #333; }
}
#mast .library-mark { width: 56px; height: 56px; color: #cc0000; display: flex; align-items: center; justify-content: center; }
#mast .library-mark svg { width: 56px; height: 56px; }
#mast h1 {
  margin: 0;
  font-family: var(--sans);
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: .12em;
  line-height: 1.2;
}
#mast .library-cta { margin: 0; font-size: .9rem; color: #555; font-weight: 400; }
html[data-theme="dark"] #mast .library-cta { color: #a0a0a0; }
@media (prefers-color-scheme: dark) {
  html[data-theme="sys"] #mast .library-cta { color: #a0a0a0; }
}
#bar-title { font-size: 1rem; letter-spacing: .1em; }
"""

if "#mast {" not in t:
    t = t.replace("[hidden] { display: none !important; }", "[hidden] { display: none !important; }\n" + css)

new = (
    '<header id="mast">'
    '<div class="library-mark" aria-hidden="true">'
    '<i data-lucide="circle" class="logo-mark"></i>'
    "</div>"
    '<h1 id="brand"><span>shklr</span></h1>'
    '<p class="library-cta" id="tagline-pt">Projeto independente \u2014 n\u00e3o \u00e9 entidade registrada</p>'
    '<p class="library-cta" id="tagline-en" hidden>Independent project \u2014 not a registered entity</p>'
    "</header>"
)

t2, n = re.subn(r"<header>\s*<p id=\"brand\">.*?</header>", new, t, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f"header replace failed: {n}")
t = t2
t = re.sub(r"#brand \{[^}]+\}", "", t, count=1)
# move mast outside wrap so it is full-bleed like the family sites
t = t.replace('<div class="wrap">\n' + new, new + '\n<div class="wrap">')
t = t.replace('<div class="wrap">' + new, new + '<div class="wrap">')
p.write_text(t, encoding="utf-8")
print("ok")
