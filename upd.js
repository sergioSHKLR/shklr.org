(function () {
  function clearAndReload() {
    var jobs = [];
    if ("serviceWorker" in navigator) {
      jobs.push(
        navigator.serviceWorker.getRegistrations().then(function (regs) {
          return Promise.all(regs.map(function (r) { return r.unregister(); }));
        })
      );
    }
    if (window.caches) {
      jobs.push(
        caches.keys().then(function (keys) {
          return Promise.all(keys.map(function (k) { return caches.delete(k); }));
        })
      );
    }
    return Promise.all(jobs).catch(function () {});
  }
  function label() {
    var lang = (document.documentElement.lang || "").toLowerCase();
    return lang.indexOf("en") === 0 ? "Update" : "Atualizar";
  }
  function icon() {
    return '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 15V3"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/></svg>';
  }
  function paint() {
    document.querySelectorAll(".settings-ver, .version-line").forEach(function (el) {
      var btn = el.querySelector("[data-force-update]");
      if (!btn) {
        btn = document.createElement("button");
        btn.type = "button";
        btn.className = "upd";
        btn.setAttribute("data-force-update", "1");
        btn.innerHTML = icon() + '<span></span>';
        btn.addEventListener("click", function (ev) {
          ev.preventDefault();
          ev.stopPropagation();
          btn.disabled = true;
          clearAndReload().then(function () {
            var url = new URL(location.href);
            url.searchParams.set("_up", String(Date.now()));
            location.replace(url.pathname + url.search + url.hash);
          });
        });
        el.appendChild(btn);
      }
      var span = btn.querySelector("span");
      if (span) span.textContent = label();
    });
  }
  var style = document.createElement("style");
  style.textContent = "#settings .settings-ver,#settings .version-line{display:inline-flex;align-items:center;gap:.45rem;flex-wrap:wrap}#settings button.upd{display:inline-flex;align-items:center;gap:.35rem;height:auto;min-height:0;min-width:0;margin:0;padding:.2rem .6rem;border:1px solid var(--line,#ccc);border-radius:999px;background:transparent;color:inherit;font-family:Quicksand,system-ui,sans-serif;font-size:.72rem;font-weight:600;line-height:1.2;cursor:pointer}#settings button.upd svg{width:18px;height:18px;display:block}#settings button.upd:disabled{opacity:.45;cursor:default}";
  document.head.appendChild(style);
  new MutationObserver(paint).observe(document.documentElement, { childList: true, subtree: true, attributes: true, attributeFilter: ["lang"] });
  paint();
})();
