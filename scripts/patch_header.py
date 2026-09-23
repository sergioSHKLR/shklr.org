from pathlib import Path
p = Path("index.html")
t = p.read_text(encoding="utf-8")
old = '      if (contactTitle) contactTitle.textContent = next === "en" ? "Message" : "Mensagem";'
new = '      const contactHeading = document.getElementById("contact-title");\n      if (contactHeading) contactHeading.textContent = next === "en" ? "Message" : "Mensagem";'
if old not in t:
    raise SystemExit(repr([ln for ln in t.splitlines() if "contactTitle" in ln][:3]))
t = t.replace(old, new, 1)
p.write_text(t, encoding="utf-8")
print("ok")
