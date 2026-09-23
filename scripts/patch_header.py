import re
from pathlib import Path

p = Path("index.html")
t = p.read_text(encoding="utf-8")

css = """
#mail-link {
  position: absolute; top: .6rem; right: .75rem;
  width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;
  color: #888; text-decoration: none; border-radius: 8px;
}
#mail-link:hover { color: var(--fg); background: rgba(0,0,0,.06); }
html[data-theme="dark"] #mail-link:hover { background: rgba(255,255,255,.08); }
#mail-link svg { width: 1.15rem; height: 1.15rem; }
#mast { position: relative; }
#contact {
  position: fixed; left: 50%; top: 50%; width: min(640px, 94vw);
  max-height: min(86vh, calc(100% - var(--chrome-bottom) - 2rem));
  background: var(--lift); color: var(--fg); border: 1px solid var(--line);
  border-radius: 12px; z-index: 530; display: flex; flex-direction: column;
  box-shadow: 0 16px 48px rgba(0,0,0,.28);
  transform: translate(-50%, -46%) scale(.96); opacity: 0; pointer-events: none;
  transition: transform .24s cubic-bezier(.22,1,.36,1), opacity .24s ease;
}
#contact.is-open { transform: translate(-50%, -50%) scale(1); opacity: 1; pointer-events: auto; display: flex !important; }
#contact > header {
  display: flex; align-items: center; justify-content: space-between;
  flex: 0 0 var(--ctrl-h); height: var(--ctrl-h); padding: 0 .5rem 0 1rem;
  border-bottom: 1px solid var(--line); font-family: var(--sans); font-weight: 600; font-size: .95rem;
}
#contact > header button {
  width: var(--ctrl-h); height: var(--ctrl-h); padding: 0; border: none;
  background: transparent; color: var(--fg); display: flex; align-items: center; justify-content: center; cursor: pointer;
}
#contact > header svg { width: 1.25rem; height: 1.25rem; }
#contact iframe { width: 100%; flex: 1 1 auto; min-height: 420px; border: 0; background: #fff; }
"""

if "#mail-link {" not in t:
    t = t.replace("#bar-title { font-size: 1rem; letter-spacing: .1em; }", "#bar-title { font-size: 1rem; letter-spacing: .1em; }\n" + css)

if 'id="mail-link"' not in t:
    t = t.replace(
        '<header id="mast">',
        '<header id="mast"><a id="mail-link" href="https://mail.hover.com/" title="correio" aria-label="correio"><i data-lucide="mail"></i></a>',
        1,
    )

pt_block = ''' <h2>Correio</h2>
 <a class="card neutral" href="https://mail.hover.com/"><span><strong>Entrar no correio</strong><span class="muted">sergio@doutrina.org \u2014 Hover</span></span></a>
 <a class="card neutral" href="https://docs.google.com/forms/d/e/1FAIpQLSc7ZRs6usX8DhTixnerMX68QtRT0o-bz9PmTtn8OKK0z2vhsw/viewform?usp=sharing"><span><strong>Formul\u00e1rio</strong><span class="muted">Mensagem p\u00fablica</span></span></a>'''
en_block = ''' <h2>Mail</h2>
 <a class="card neutral" href="https://mail.hover.com/"><span><strong>Open mailbox</strong><span class="muted">sergio@doutrina.org \u2014 Hover</span></span></a>
 <a class="card neutral" href="https://docs.google.com/forms/d/e/1FAIpQLSc7ZRs6usX8DhTixnerMX68QtRT0o-bz9PmTtn8OKK0z2vhsw/viewform?usp=sharing"><span><strong>Contact form</strong><span class="muted">Public message</span></span></a>'''

t = t.replace(pt_block, ' <p><button type="button" class="card neutral" id="btn-contact-pt" style="width:100%;cursor:pointer;font:inherit;text-align:left"><span><strong>Mensagem</strong><span class="muted">Formul\u00e1rio p\u00fablico</span></span></button></p>')
t = t.replace(en_block, ' <p><button type="button" class="card neutral" id="btn-contact-en" style="width:100%;cursor:pointer;font:inherit;text-align:left"><span><strong>Message</strong><span class="muted">Public form</span></span></button></p>')

# fallback regex if emdash encoding differs
t = re.sub(
    r'<h2>Correio</h2>\s*<a class="card neutral" href="https://mail.hover.com/">.*?</a>\s*<a class="card neutral" href="https://docs.google.com/forms/[^"]+">.*?</a>',
    '<p><button type="button" class="card neutral" id="btn-contact-pt" style="width:100%;cursor:pointer;font:inherit;text-align:left"><span><strong>Mensagem</strong><span class="muted">Formul\u00e1rio p\u00fablico</span></span></button></p>',
    t,
    count=1,
    flags=re.S,
)
t = re.sub(
    r'<h2>Mail</h2>\s*<a class="card neutral" href="https://mail.hover.com/">.*?</a>\s*<a class="card neutral" href="https://docs.google.com/forms/[^"]+">.*?</a>',
    '<p><button type="button" class="card neutral" id="btn-contact-en" style="width:100%;cursor:pointer;font:inherit;text-align:left"><span><strong>Message</strong><span class="muted">Public form</span></span></button></p>',
    t,
    count=1,
    flags=re.S,
)

t = t.replace('<p>Mailbox: sergio@doutrina.org</p>', '')

if 'id="contact"' not in t:
    modal = '''
<div id="contact" class="modal" hidden role="dialog" aria-modal="true" aria-labelledby="contact-title">
<header>
<span id="contact-title">Mensagem</span>
<button type="button" id="btn-close-contact" aria-label="Close"><i data-lucide="x"></i></button>
</header>
<iframe title="Contact form" src="https://docs.google.com/forms/d/e/1FAIpQLSc7ZRs6usX8DhTixnerMX68QtRT0o-bz9PmTtn8OKK0z2vhsw/viewform?embedded=true"></iframe>
</div>
'''
    t = t.replace('<div id="settings"', modal + '<div id="settings"', 1)

if 'id="btn-contact-bar"' not in t:
    t = t.replace(
        '<button type="button" id="btn-settings"',
        '<button type="button" id="btn-contact-bar" aria-expanded="false" aria-controls="contact" title="Mensagem" aria-label="Mensagem"><i data-lucide="message-circle"></i></button>\n<button type="button" id="btn-settings"',
        1,
    )

js = """
    const contact = document.getElementById("contact");
    const contactTitle = document.getElementById("contact-title");
    function openContact() {
      if (settings.classList.contains("is-open")) closeSettings();
      scrim.hidden = false;
      contact.hidden = false;
      requestAnimationFrame(() => {
        scrim.classList.add("is-open");
        contact.classList.add("is-open");
      });
      const bar = document.getElementById("btn-contact-bar");
      if (bar) bar.setAttribute("aria-expanded", "true");
    }
    function closeContact() {
      contact.classList.remove("is-open");
      const bar = document.getElementById("btn-contact-bar");
      if (bar) bar.setAttribute("aria-expanded", "false");
      if (!settings.classList.contains("is-open")) scrim.classList.remove("is-open");
      setTimeout(() => {
        if (!contact.classList.contains("is-open")) contact.hidden = true;
        if (!settings.classList.contains("is-open") && !contact.classList.contains("is-open")) scrim.hidden = true;
      }, 240);
    }
    ["btn-contact-pt", "btn-contact-en", "btn-contact-bar"].forEach((id) => {
      const el = document.getElementById(id);
      if (el) el.addEventListener("click", (e) => { e.stopPropagation(); openContact(); });
    });
    const closeC = document.getElementById("btn-close-contact");
    if (closeC) closeC.addEventListener("click", closeContact);
"""

if "function openContact()" not in t:
    t = t.replace(
        "btnSettings.addEventListener",
        js + "\n    btnSettings.addEventListener",
        1,
    )
    t = t.replace(
        "scrim.addEventListener(\"click\", closeSettings);",
        "scrim.addEventListener(\"click\", () => { closeSettings(); closeContact(); });",
        1,
    )
    t = t.replace(
        'if (e.key === "Escape" && settings.classList.contains("is-open")) closeSettings();',
        'if (e.key === "Escape") { closeSettings(); closeContact(); }',
        1,
    )
    # localize contact title with language
    t = t.replace(
        "title.textContent = c.title;",
        "title.textContent = c.title;\n      if (contactTitle) contactTitle.textContent = next === \"en\" ? \"Message\" : \"Mensagem\";",
        1,
    )

p.write_text(t, encoding="utf-8")
print("mail-link", "id=\"mail-link\"" in t)
print("contact", "id=\"contact\"" in t)
print("hover cards", t.count("mail.hover.com"))
print("openContact", "function openContact" in t)
