from pathlib import Path
p = Path("index.html")
t = p.read_text(encoding="utf-8")
old = "#mast {\n  box-sizing: border-box;\n  width: 100%;\n  margin: 0;"
new = "#mast {\n  box-sizing: border-box;\n  width: 100vw;\n  max-width: 100vw;\n  position: relative;\n  left: 50%;\n  right: 50%;\n  margin-left: -50vw;\n  margin-right: -50vw;"
if old in t:
    t = t.replace(old, new, 1)
    print("css fullbleed")
else:
    print("css block missing")
t = t.replace("padding: 3rem 1.25rem calc(var(--chrome-bottom) + 2rem)", "padding: 1.25rem 1.25rem calc(var(--chrome-bottom) + 2rem)", 1)
p.write_text(t, encoding="utf-8")
