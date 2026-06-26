// Free your Mind — shared site behaviour.

// Top bar turns solid after the hero. Inner pages use body.solid-nav
// to stay solid from the top, so only run the toggle when a full hero exists.
(function () {
  const hero = document.querySelector(".hero");
  if (hero && !document.body.classList.contains("solid-nav")) {
    const onScroll = () => {
      const t = hero.offsetHeight - 80;
      document.body.classList.toggle("is-scrolled", window.scrollY > t);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }
})();

// Mobile menu toggle.
(function () {
  const btn = document.querySelector(".nav-toggle");
  const tabs = document.querySelector(".top-tabs");
  if (!btn || !tabs) return;
  const setOpen = (open) => {
    document.body.classList.toggle("nav-open", open);
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.textContent = open ? "Close" : "Menu";
  };
  btn.addEventListener("click", () => setOpen(!document.body.classList.contains("nav-open")));
  tabs.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => setOpen(false)));
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") setOpen(false); });
  window.addEventListener("resize", () => { if (window.innerWidth > 860) setOpen(false); }, { passive: true });
})();

// Scroll reveal.
(function () {
  const els = document.querySelectorAll(".reveal");
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (els.length && "IntersectionObserver" in window && !reduce) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.12 });
    els.forEach((el) => io.observe(el));
  } else {
    els.forEach((el) => el.classList.add("in"));
  }
})();
