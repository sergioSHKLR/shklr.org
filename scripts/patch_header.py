import re
from pathlib import Path

p = Path("index.html")
t = p.read_text(encoding="utf-8")
t2, n = re.subn(
    r'<a class="card neutral" href="\./images/[^\"]+" download="[^"]+\.png">[^<]*</a>',
    "",
    t,
)
print("removed", n)
p.write_text(t2, encoding="utf-8")
