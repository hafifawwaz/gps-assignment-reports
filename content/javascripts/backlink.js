// "Back to <page>" button: when a page is opened from another page of this site (a link in a note,
// the knowledge map, a section list), show a button at the top that returns to that page.
// Remembered per page for the browser tab (sessionStorage), so it survives a reload.
(function () {
  const SITE = " - GPS Staypoint Assignment";
  const strip = (url) => url.split("#")[0];
  const store = {
    get(k) { try { return JSON.parse(sessionStorage.getItem(k)); } catch (e) { return null; } },
    set(k, v) { try { sessionStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* storage off */ } },
    del(k) { try { sessionStorage.removeItem(k); } catch (e) { /* storage off */ } },
  };

  const here = strip(location.href);
  const key = "back:" + location.pathname;
  const last = store.get("back:last");
  const nav = (performance.getEntriesByType("navigation")[0] || {}).type || "navigate";

  if (nav === "navigate") {
    const fromHere = last && document.referrer && strip(document.referrer) === last.href && last.href !== here;
    if (fromHere) store.set(key, last);
    else store.del(key);  // opened directly or from outside: no origin to go back to
  }
  // The page heading (the <title> carries the lowercase sidebar label); the home page is "Home".
  const h1 = document.querySelector(".md-content h1");
  const home = !document.title.endsWith(SITE);
  const title = home ? "Home" : (h1 ? h1.textContent.trim() : document.title.slice(0, -SITE.length));
  store.set("back:last", { href: here, title: title });

  const origin = store.get(key);
  const inner = document.querySelector(".md-content__inner");
  if (!origin || !inner || origin.href === here) return;

  const a = document.createElement("a");
  a.className = "backlink-button";
  a.href = origin.href;
  const label = document.createElement("span");
  label.className = "backlink-label";
  label.textContent = "← Back to";
  const target = document.createElement("span");
  target.className = "backlink-target";
  target.textContent = origin.title;
  a.append(label, " ", target);
  a.addEventListener("click", (e) => {
    // Return through history when possible, so the origin page keeps its scroll position.
    if (document.referrer && strip(document.referrer) === origin.href && history.length > 1) {
      e.preventDefault();
      history.back();
    }
  });
  inner.insertBefore(a, inner.firstChild);
})();
