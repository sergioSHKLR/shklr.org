const LANG = "shklr-lang";
const THEME = "shklr-theme";
const panels = { pt: document.getElementById("panel-pt"), en: document.getElementById("panel-en") };
const tags = { pt: document.getElementById("tagline-pt"), en: document.getElementById("tagline-en") };
const settings = document.getElementById("settings");
const scrim = document.getElementById("scrim");
const btnSettings = document.getElementById("btn-settings");
const title = document.getElementById("settings-title");
const hint = document.getElementById("set-hint");
const langLegend = document.getElementById("set-lang-legend");
const themeLegend = document.getElementById("set-theme-legend");
const copy = {
pt: { title: "Ajustes", hint: "Idioma e tema desta página.", lang: "Idioma", theme: "Tema", sys: "Sistema", light: "Claro", dark: "Escuro" },
en: { title: "Settings", hint: "Language and theme for this page.", lang: "Language", theme: "Theme", sys: "System", light: "Light", dark: "Dark" }
};
function applyLang(lang) {
 const next = lang === "en" ? "en" : "pt";
 document.documentElement.lang = next === "pt" ? "pt-BR" : "en";
 panels.pt.hidden = next !== "pt";
 panels.en.hidden = next !== "en";
 tags.pt.hidden = next !== "pt";
 tags.en.hidden = next !== "en";
 const c = copy[next];
 title.textContent = c.title;
 const legal = document.getElementById("colo-legal-label");
 const name = document.getElementById("colo-name");
 if (legal) legal.textContent = next === "en" ? "Legal notice" : "Aviso legal";
 if (name) name.textContent = next === "en" ? "SHKLR · family name, independent project" : "SHKLR · sobrenome, projeto independente";
 const contactHeading = document.getElementById("contact-title");
 if (contactHeading) contactHeading.textContent = next === "en" ? "Message" : "Mensagem";
 hint.textContent = c.hint;
 langLegend.textContent = c.lang;
 themeLegend.textContent = c.theme;
 document.getElementById("set-sys").textContent = c.sys;
 document.getElementById("set-light").textContent = c.light;
 document.getElementById("set-dark").textContent = c.dark;
 document.querySelectorAll('input[name="ui-lang"]').forEach((el) => { el.checked = el.value === next; });
 try { localStorage.setItem(LANG, next); } catch (e) {}
}
function applyTheme(mode) {
 const next = mode === "light" || mode === "dark" ? mode : "sys";
 document.documentElement.dataset.theme = next;
 document.querySelectorAll('input[name="ui-theme"]').forEach((el) => { el.checked = el.value === next; });
 try { localStorage.setItem(THEME, next); } catch (e) {}
}
function openSettings() {
 scrim.hidden = false; settings.hidden = false;
 requestAnimationFrame(() => { scrim.classList.add("is-open"); settings.classList.add("is-open"); });
 btnSettings.setAttribute("aria-expanded", "true");
}
function closeSettings() {
 scrim.classList.remove("is-open"); settings.classList.remove("is-open");
 btnSettings.setAttribute("aria-expanded", "false");
 setTimeout(() => { if (!settings.classList.contains("is-open")) { settings.hidden = true; if (!anyOpen()) scrim.hidden = true; } }, 240);
}
document.querySelectorAll('a[href^="http"]').forEach((a) => { a.target = "_blank"; a.rel = "noopener noreferrer"; });
let lang = "pt"; let theme = "sys";
try {
 const sl = localStorage.getItem(LANG);
 if (sl === "en" || sl === "pt") lang = sl;
 else if (/^en\b/i.test(navigator.language || "")) lang = "en";
 const st = localStorage.getItem(THEME);
 if (st === "light" || st === "dark" || st === "sys" || st === "system") theme = st === "system" ? "sys" : st;
} catch (e) {}
applyLang(lang); applyTheme(theme);
document.querySelectorAll('input[name="ui-lang"]').forEach((el) => el.addEventListener("change", () => applyLang(el.value)));
document.querySelectorAll('input[name="ui-theme"]').forEach((el) => el.addEventListener("change", () => applyTheme(el.value)));
const contact = document.getElementById("contact");
function openContact() {
 if (settings.classList.contains("is-open")) closeSettings();
 const frame = document.getElementById("contact-frame");
 if (frame && !frame.getAttribute("src")) frame.src = frame.dataset.src || "";
 scrim.hidden = false; contact.hidden = false;
 requestAnimationFrame(() => { scrim.classList.add("is-open"); contact.classList.add("is-open"); });
 const bar = document.getElementById("btn-contact-bar");
 if (bar) bar.setAttribute("aria-expanded", "true");
}
function closeContact() {
  if (!contact) return;
  contact.classList.remove("is-open");
 const bar = document.getElementById("btn-contact-bar");
 if (bar) bar.setAttribute("aria-expanded", "false");
 if (!settings.classList.contains("is-open")) scrim.classList.remove("is-open");
 setTimeout(() => { if (!contact.classList.contains("is-open")) contact.hidden = true; if (!anyOpen()) scrim.hidden = true; }, 240);
}
const barC = document.getElementById("btn-contact-bar");
if (barC) barC.addEventListener("click", (e) => { e.stopPropagation(); openContact(); });
const closeC = document.getElementById("btn-close-contact");
if (closeC) closeC.addEventListener("click", closeContact);
btnSettings.addEventListener("click", (e) => { e.stopPropagation(); if (settings.classList.contains("is-open")) closeSettings(); else openSettings(); });
document.getElementById("btn-close-settings").addEventListener("click", closeSettings);
const viewer = document.getElementById("viewer");
const viewerTitle = document.getElementById("viewer-title");
const viewerImg = document.getElementById("viewer-img");
const viewerFrame = document.getElementById("viewer-frame");
function anyOpen(){ return [settings, contact, viewer].some((el) => el && el.classList.contains("is-open")); }
function hideViewerPdf() {
  const pdf = document.getElementById("viewer-pdf");
  if (!pdf) return;
  pdf.hidden = true;
  pdf.removeAttribute("href");
}
function closeViewer(){ if (!viewer) return; viewer.classList.remove("is-open"); setTimeout(() => { if (!viewer.classList.contains("is-open")) { viewer.hidden = true; viewerFrame.removeAttribute("src"); viewerImg.removeAttribute("src"); hideViewerPdf(); } if (!anyOpen()) scrim.hidden = true; }, 240); }
function openViewer(){ if (settings.classList.contains("is-open")) closeSettings(); if (contact.classList.contains("is-open")) closeContact(); viewer.hidden = false; scrim.hidden = false; requestAnimationFrame(() => { scrim.classList.add("is-open"); viewer.classList.add("is-open"); }); }
const closeV = document.getElementById("btn-close-viewer");
if (closeV) closeV.addEventListener("click", closeViewer);
document.querySelectorAll("[data-portrait]").forEach((btn) => {
 btn.addEventListener("click", () => {
  const src = btn.getAttribute("data-portrait");
  if (!src || !viewerImg) return;
  const en = document.documentElement.lang === "en";
  if (viewerTitle) viewerTitle.textContent = (en ? btn.dataset.portraitTitleEn : btn.dataset.portraitTitlePt) || "";
  if (viewerFrame) { viewerFrame.hidden = true; viewerFrame.removeAttribute("src"); }
  hideViewerPdf();
  viewerImg.hidden = false;
  viewerImg.alt = (btn.querySelector("img") && btn.querySelector("img").alt) || "";
  viewerImg.src = src;
  openViewer();
 });
});
document.querySelectorAll("[data-poster]").forEach((a) => {
  a.addEventListener("click", (e) => {
    e.preventDefault();
    const en = document.documentElement.lang === "en";
    if (viewerTitle) viewerTitle.textContent = (en ? a.dataset.titleEn : a.dataset.titlePt) || a.textContent;
    if (viewerFrame) { viewerFrame.hidden = true; viewerFrame.removeAttribute("src"); }
    viewerImg.hidden = false;
    viewerImg.alt = a.textContent.trim();
    viewerImg.src = a.dataset.png || "";
    const pdf = document.getElementById("viewer-pdf");
    if (pdf) {
      pdf.hidden = false;
      pdf.href = a.href;
      pdf.target = "_blank";
      pdf.rel = "noopener";
      pdf.textContent = en ? "PDF for printing" : "PDF para impressão";
    }
    openViewer();
  });
});
document.querySelectorAll(".tl button").forEach((btn) => {
 btn.addEventListener("click", () => {
 const open = btn.getAttribute("aria-expanded") === "true";
 const root = btn.closest("ol");
 root.querySelectorAll("button").forEach((b) => { b.setAttribute("aria-expanded", "false"); const body = b.nextElementSibling; if (body) body.hidden = true; });
 if (!open) { btn.setAttribute("aria-expanded", "true"); const body = btn.nextElementSibling; if (body) body.hidden = false; }
 });
});
scrim.addEventListener("click", () => { closeSettings(); closeContact(); closeViewer(); });
document.addEventListener("keydown", (e) => { if (e.key === "Escape") { closeSettings(); closeContact(); closeViewer(); } });
const thoughts = {
pt: [
 "O conforto que você almeja é a recompensa pelos desafios que evitou.",
 "Minhas feridas não me preocupam tanto quanto o bem que poderia ter feito enquanto eu estava distraído com minha dor.",
 "A utilidade de uma alma é uma função da aplicação consciente de seu livre-arbítrio.",
 "Imersos no amor de Deus, por que esmolar migalhas de afeição de terceiros?",
 "Se o que foi compartilhado não mudou ato ou pensamento, continue mesmo assim.",
 "Conhecimento é estéril sem ação. Passos pequenos e consistentes.",
 "A distância da felicidade é a que pomos entre o interesse próprio e o propósito divino."
],
en: [
 "The comfort you long for is the reward for the challenges you avoided.",
 "My wounds worry me less than the good I might have done while distracted by the pain.",
 "The usefulness of a soul is a function of the conscious use of free will.",
 "Immersed in God’s love, why beg crumbs of affection from others?",
 "If what was shared did not change an act or a thought, keep going anyway.",
 "Knowledge is sterile without action. Small, consistent steps.",
 "The distance from happiness is the distance we put between self-interest and purpose."
]
};
let thoughtI = Math.floor(Date.now() / 86400000) % thoughts.pt.length;
function paintThoughts() {
 document.querySelectorAll("[data-thought]").forEach((el) => {
  const panel = el.closest("main");
  const lang = panel && panel.id === "panel-en" ? "en" : "pt";
  el.textContent = thoughts[lang][thoughtI];
 });
}
function nextThought() {
 thoughtI = (thoughtI + 1) % thoughts.pt.length;
 paintThoughts();
}
paintThoughts();
document.querySelectorAll("[data-thought-next]").forEach((btn) => btn.addEventListener("click", nextThought));
if (window.lucide) lucide.createIcons({ attrs: { "stroke-width": 2.5 } });
document.querySelectorAll(".logo-mark").forEach((el) => el.setAttribute("stroke-width", "3.5"));
