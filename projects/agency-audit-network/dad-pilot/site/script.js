(function () {
  const tabs = document.querySelectorAll('[data-tab]');
  const panels = document.querySelectorAll('.tab-panel');

  function setActive(name) {
    tabs.forEach((t) => {
      const isActive = t.dataset.tab === name;
      t.classList.toggle('is-active', isActive);
      t.setAttribute('aria-selected', isActive ? 'true' : 'false');
    });
    panels.forEach((p) => {
      p.classList.toggle('is-active', p.dataset.panel === name);
    });
    if (history.replaceState) {
      history.replaceState(null, '', '#' + name);
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  tabs.forEach((t) => {
    t.addEventListener('click', () => setActive(t.dataset.tab));
  });

  const hash = window.location.hash.replace('#', '');
  if (hash && document.querySelector(`[data-tab="${hash}"]`)) {
    setActive(hash);
  } else {
    setActive('overview');
  }
})();
