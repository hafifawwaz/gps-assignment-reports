// Click a figure in a page to see it larger, in an overlay on the same page (no new window).
// The overlay shows the image up to 90% of the window, at most twice its own size so it stays sharp.
// Click anywhere or press Esc to close. Images inside a link (e.g. a PDF's first page) keep their link.
(function () {
  const MIN_SIZE = 120; // smaller images (icons, chips) are left alone

  function open(img) {
    const overlay = document.createElement("div");
    overlay.className = "zoom-overlay";
    const big = document.createElement("img");
    big.src = img.currentSrc || img.src;
    big.alt = img.alt || "";
    const w = img.naturalWidth || img.width;
    const h = img.naturalHeight || img.height;
    const scale = Math.min(2, (window.innerWidth * 0.9) / w, (window.innerHeight * 0.88) / h);
    big.style.width = Math.round(w * scale) + "px";
    overlay.appendChild(big);
    if (img.alt) {
      const cap = document.createElement("div");
      cap.className = "zoom-caption";
      cap.textContent = img.alt;
      overlay.appendChild(cap);
    }
    const close = () => {
      overlay.remove();
      document.removeEventListener("keydown", onKey);
      document.documentElement.classList.remove("zoom-open");
    };
    const onKey = (e) => { if (e.key === "Escape") close(); };
    overlay.addEventListener("click", close);
    document.addEventListener("keydown", onKey);
    document.documentElement.classList.add("zoom-open");
    document.body.appendChild(overlay);
  }

  function setup() {
    document.querySelectorAll(".md-content .md-typeset img").forEach((img) => {
      if (img.closest("a") || img.dataset.zoom) return;
      img.dataset.zoom = "1";
      const mark = () => {
        if (img.naturalWidth >= MIN_SIZE) img.classList.add("zoomable");
      };
      img.complete ? mark() : img.addEventListener("load", mark);
      img.addEventListener("click", () => { if (img.classList.contains("zoomable")) open(img); });
    });
  }

  if (window.document$) window.document$.subscribe(setup);
  else document.addEventListener("DOMContentLoaded", setup);
})();
