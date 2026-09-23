#!/usr/bin/env python3
from pathlib import Path
import re
import sys

p = Path("index.html")
t = p.read_text(encoding="utf-8")
if "PLACEHOLDER" in t and len(t) < 200:
    sys.exit("index.html is a placeholder; restore a real copy first")

css = """
.asset{display:flex;align-items:flex-end;gap:.45rem;margin:.6rem 0 1rem;max-width:min(100%,368px)}
.thumb-hit{display:block;flex:1 1 auto;min-width:0;padding:0;border:0;background:none;cursor:zoom-in;-webkit-tap-highlight-color:transparent}
.thumb-hit .thumb{margin:0;width:100%;max-width:320px;height:auto;pointer-events:none}
.dl-icon{flex:none;width:44px;height:44px;display:inline-flex;align-items:center;justify-content:center;color:var(--fg);text-decoration:none;border:1px solid var(--line);border-radius:8px;background:var(--lift);-webkit-tap-highlight-color:transparent}
.dl-icon:hover,.dl-icon:focus-visible{color:var(--brand);border-color:var(--brand)}
.dl-icon svg{width:1.25rem;height:1.25rem}
#viewer{position:fixed;left:50%;top:50%;width:min(980px,96vw);height:min(88vh,calc(100% - var(--chrome-bottom) - 1.25rem));background:var(--lift);color:var(--fg);border:1px solid var(--line);border-radius:12px;z-index:530;display:flex;flex-direction:column;box-shadow:0 16px 48px rgba(0,0,0,.28);transform:translate(-50%,-46%) scale(.96);opacity:0;pointer-events:none;transition:transform .24s cubic-bezier(.22,1,.36,1),opacity .24s ease}
#viewer.is-open{transform:translate(-50%,-50%) scale(1);opacity:1;pointer-events:auto;display:flex!important}
#viewer>header{display:flex;align-items:center;justify-content:space-between;flex:0 0 var(--ctrl-h);height:var(--ctrl-h);padding:0 .5rem 0 1rem;border-bottom:1px solid var(--line);font-family:var(--sans);font-weight:600;font-size:.95rem;gap:.5rem}
#viewer>header button{width:var(--ctrl-h);height:var(--ctrl-h);padding:0;border:none;background:transparent;color:var(--fg);display:flex;align-items:center;justify-content:center;cursor:pointer;flex:none}
#viewer>header svg{width:1.25rem;height:1.25rem}
#viewer .stage{flex:1 1 auto;min-height:0;overflow:auto;background:#111;display:flex;align-items:center;justify-content:center;position:relative}
#viewer .stage img{max-width:100%;max-height:100%;width:auto;height:auto;object-fit:contain}
#viewer .stage iframe{width:100%;height:100%;border:0;background:#fff}
@media (max-width:640px){
  #viewer{width:100vw;height:calc(100% - var(--chrome-bottom));max-height:none;border-radius:0;left:0;top:0;transform:none;opacity:0}
  #viewer.is-open{transform:none;left:0;top:0}
}
"""

if 'class="asset"' not in t:
    needle = '#contact iframe { width: 100%; flex: 1 1 auto; min-height: 420px; border: 0; background: #fff; }'
    if needle not in t:
        sys.exit("css anchor missing")
    t = t.replace(needle, needle + "\n" + css)

    def sub(m):
        src, alt, href, name = m.group(1), m.group(2), m.group(3), m.group(4)
        kind = "single" if "portrait" in name else "multi"
        titles = {
            "Livro de Preces": ("Livro de Preces", "Book of Prayers"),
            "Book of Prayers": ("Livro de Preces", "Book of Prayers"),
            "Obras básicas": ("Obras básicas", "Basic works"),
            "Basic works": ("Obras básicas", "Basic works"),
            "Protector": ("Protector", "Protector"),
            "Anguish": ("Anguish", "Anguish"),
        }
        pt, en = titles.get(alt, (alt, alt))
        return (
            f' <div class="asset" data-kind="{kind}" data-pdf="{href}" data-png="{src}" data-name="{name}" data-title-pt="{pt}" data-title-en="{en}">'
            f'<button type="button" class="thumb-hit" data-preview aria-label="{alt}">'
            f'<img class="thumb" src="{src}" alt="{alt}"></button>'
            f'<a class="dl-icon" href="{href}" download="{name}" data-download aria-label="Download"><i data-lucide="download"></i></a></div>'
        )

    pat = r' <img class="thumb" src="([^"]+)" alt="([^"]+)">\n <p class="file-actions"><a class="card neutral" href="([^"]+)" download="([^"]+)">[^<]+</a></p>'
    t, n = re.subn(pat, sub, t)
    if n != 8:
        sys.exit("expected 8 assets, got %s" % n)

if 'id="viewer"' not in t:
    viewer = (
        '\n<div id="viewer" class="modal" hidden role="dialog" aria-modal="true" aria-labelledby="viewer-title">\n'
        '<header><span id="viewer-title"></span>\n'
        '<button type="button" id="btn-close-viewer" aria-label="Close"><i data-lucide="x"></i></button></header>\n'
        '<div class="stage"><img id="viewer-img" alt="" hidden><iframe id="viewer-frame" title="PDF" hidden></iframe></div>\n'
        '</div>\n'
    )
    if '<div id="settings" class="modal"' not in t:
        sys.exit("settings anchor missing")
    t = t.replace('<div id="settings" class="modal"', viewer + '<div id="settings" class="modal"', 1)

js = r'''
const viewer=document.getElementById("viewer");
const viewerTitle=document.getElementById("viewer-title");
const viewerImg=document.getElementById("viewer-img");
const viewerFrame=document.getElementById("viewer-frame");
function anyOpen(){return [settings,contact,viewer].some(el=>el&&el.classList.contains("is-open"));}
function idleScrim(){if(anyOpen())return;scrim.classList.remove("is-open");setTimeout(()=>{if(!anyOpen())scrim.hidden=true;},240);}
function closeViewer(){if(!viewer)return;viewer.classList.remove("is-open");setTimeout(()=>{if(!viewer.classList.contains("is-open")){viewer.hidden=true;viewerFrame.removeAttribute("src");viewerImg.removeAttribute("src");}},240);idleScrim();}
function openViewer(){if(settings.classList.contains("is-open"))closeSettings();if(contact.classList.contains("is-open"))closeContact();viewer.hidden=false;scrim.hidden=false;requestAnimationFrame(()=>{scrim.classList.add("is-open");viewer.classList.add("is-open");});}
async function forceDownload(url,name){try{const res=await fetch(url,{mode:"cors"});if(!res.ok)throw 0;const blob=await res.blob();const href=URL.createObjectURL(blob);const a=document.createElement("a");a.href=href;a.download=name||"file.pdf";document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(href),4000);}catch(e){const a=document.createElement("a");a.href=url;a.download=name||"file.pdf";a.rel="noopener";document.body.appendChild(a);a.click();a.remove();}}
function previewPdf(url){viewerImg.hidden=true;viewerImg.removeAttribute("src");viewerFrame.hidden=false;viewerFrame.src="https://mozilla.github.io/pdf.js/web/viewer.html?file="+encodeURIComponent(url);}
function previewPng(src,alt){viewerFrame.hidden=true;viewerFrame.removeAttribute("src");viewerImg.hidden=false;viewerImg.alt=alt||"";viewerImg.src=src;}
document.querySelectorAll("[data-preview]").forEach(btn=>btn.addEventListener("click",e=>{e.preventDefault();const box=btn.closest(".asset");if(!box)return;const en=document.documentElement.lang==="en";viewerTitle.textContent=(en?box.dataset.titleEn:box.dataset.titlePt)||"";openViewer();if(box.dataset.kind==="single")previewPng(box.dataset.png,btn.querySelector("img")&&btn.querySelector("img").alt||"");else previewPdf(box.dataset.pdf);}));
document.querySelectorAll("[data-download]").forEach(a=>a.addEventListener("click",e=>{e.preventDefault();e.stopPropagation();const box=a.closest(".asset");forceDownload(a.getAttribute("href"),(box&&box.dataset.name)||a.getAttribute("download")||"file.pdf");}));
const closeV=document.getElementById("btn-close-viewer");if(closeV)closeV.addEventListener("click",closeViewer);
'''

old_scrim = 'scrim.addEventListener("click", () => { closeSettings(); closeContact(); });'
new_scrim = js + 'scrim.addEventListener("click", () => { closeSettings(); closeContact(); closeViewer(); });'
if "function closeViewer" not in t:
    if old_scrim not in t:
        sys.exit("scrim anchor missing")
    t = t.replace(old_scrim, new_scrim, 1)
    t = t.replace(
        'if (e.key === "Escape") { closeSettings(); closeContact(); }',
        'if (e.key === "Escape") { closeSettings(); closeContact(); closeViewer(); }',
        1,
    )

p.write_text(t, encoding="utf-8")
print("ok assets", t.count("data-kind="), "viewer", t.count('id="viewer"'), "bytes", len(t))
