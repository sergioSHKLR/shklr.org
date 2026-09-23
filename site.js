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
function closeViewer(){ if (!viewer) return; viewer.classList.remove("is-open"); setTimeout(() => { if (!viewer.classList.contains("is-open")) { viewer.hidden = true; viewerFrame.removeAttribute("src"); viewerImg.removeAttribute("src"); } if (!anyOpen()) scrim.hidden = true; }, 240); }
function openViewer(){ if (settings.classList.contains("is-open")) closeSettings(); if (contact.classList.contains("is-open")) closeContact(); viewer.hidden = false; scrim.hidden = false; requestAnimationFrame(() => { scrim.classList.add("is-open"); viewer.classList.add("is-open"); }); }
const closeV = document.getElementById("btn-close-viewer");
if (closeV) closeV.addEventListener("click", closeViewer);
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
if (window.lucide) lucide.createIcons({ attrs: { "stroke-width": 2.5 } });
document.querySelectorAll(".logo-mark").forEach((el) => el.setAttribute("stroke-width", "3.5"));
