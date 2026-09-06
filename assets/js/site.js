(function () {
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => nav.classList.toggle("open"));
  }

  document.querySelectorAll("[data-tabs]").forEach((root) => {
    const tabs = root.querySelectorAll(".tab");
    const panels = root.querySelectorAll(".mission-panel");
    tabs.forEach((tab) => {
      tab.addEventListener("click", () => {
        const id = tab.getAttribute("data-tab");
        tabs.forEach((t) => t.classList.toggle("active", t === tab));
        panels.forEach((p) => p.classList.toggle("active", p.id === id));
        history.replaceState(null, "", "#" + id);
      });
    });
    const hash = (location.hash || "").replace("#", "");
    if (hash) {
      const match = root.querySelector('.tab[data-tab="' + hash + '"]');
      if (match) match.click();
    }
  });
})();
