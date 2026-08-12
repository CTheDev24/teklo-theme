(() => {
  if (window.tekloMediaPrepare) {
    window.tekloMediaPrepare();
    return;
  }
  const initialized = new WeakSet();
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  function prepare(root = document) {
    root.querySelectorAll('[data-teklo-media] video').forEach((video) => {
      if (reducedMotion.matches) {
        video.pause();
        return;
      }
      if (initialized.has(video)) return;
      initialized.add(video);
      video.muted = true;
      video.pause();
      const observer = new IntersectionObserver(([entry]) => {
        if (entry.isIntersecting && !reducedMotion.matches) {
          const promise = video.play();
          if (promise) promise.catch(() => {});
        } else video.pause();
      }, { threshold: 0.35 });
      observer.observe(video);
    });
  }
  window.tekloMediaPrepare = prepare;
  prepare();
  document.addEventListener('shopify:section:load', (event) => prepare(event.target));
  reducedMotion.addEventListener?.('change', () => {
    document.querySelectorAll('[data-teklo-media] video').forEach((video) => video.pause());
    if (!reducedMotion.matches) prepare();
  });
})();
