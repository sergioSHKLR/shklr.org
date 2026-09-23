from pathlib import Path
p = Path("index.html")
t = p.read_text(encoding="utf-8")
t = t.replace('<meta name="author" content="sergioSHKLR, sergio@doutrina.org">', '<meta name="author" content="sergioSHKLR">')
t = t.replace('<p>Mailbox: sergio@doutrina.org</p>', '')
t = t.replace('sergio@doutrina.org \u2014 Hover', 'Hover')
t = t.replace('sergio@doutrina.org — Hover', 'Hover')
p.write_text(t, encoding="utf-8")
print("email left", t.count("sergio@"))
