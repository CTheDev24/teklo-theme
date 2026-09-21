(() => {
  if (window.tekloNavigationReady) return;
  window.tekloNavigationReady = true;
  document.addEventListener('click', (event) => {
    const link = event.target.closest('[data-teklo-studio-link]');
    if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const drawer = link.closest('header-drawer');
    if (!drawer || typeof drawer.closeMenuDrawer !== 'function') return;
    const destination = new URL(link.href, window.location.href);
    if (destination.origin !== window.location.origin || destination.pathname !== window.location.pathname || destination.search !== window.location.search || !destination.hash) return;
    const target = document.getElementById(decodeURIComponent(destination.hash.slice(1)));
    const summary = drawer.querySelector('summary');
    if (!target || !summary) return;
    event.preventDefault();
    drawer.closeMenuDrawer(event, summary);
    summary.setAttribute('aria-expanded', 'false');
    window.setTimeout(() => {
      window.location.hash = destination.hash;
      if (!target.hasAttribute('tabindex')) {
        target.setAttribute('tabindex', '-1');
        target.addEventListener('blur', () => target.removeAttribute('tabindex'), { once: true });
      }
      target.focus({ preventScroll: true });
      target.scrollIntoView({ behavior: 'auto', block: 'start' });
    }, 450);
  });
})();
