(() => {
  if (window.tekloMediaPrepare) {
    window.tekloMediaPrepare();
    return;
  }
  const instances = new Map();
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const mobile = window.matchMedia('(max-width: 749px)');
  function prepare(root = document) {
    const containers = [...root.querySelectorAll('[data-teklo-media]')];
    if (root.matches?.('[data-teklo-media]')) containers.unshift(root);
    containers.forEach((container) => {
      if (instances.has(container)) return;
      const videos = [...container.querySelectorAll('video')];
      if (!videos.length) return;
      const button = container.querySelector('[data-teklo-media-toggle]');
      const label = button?.querySelector('[data-teklo-media-label]');
      const abort = new AbortController();
      const options = { signal: abort.signal };
      let visible = false;
      let userPaused = false;
      const activeVideo = () => videos.find((video) => getComputedStyle(video).display !== 'none');
      const updateButton = () => {
        if (!button) return;
        const active = activeVideo();
        button.hidden = reducedMotion.matches || !active || active.error !== null;
        if (label) label.textContent = active && !active.paused ? button.dataset.pauseLabel : button.dataset.playLabel;
      };
      const sync = () => {
        const active = activeVideo();
        videos.forEach((video) => {
          if (video === active && visible && !userPaused && !reducedMotion.matches && !document.hidden && !video.error) {
            const pending = video.play();
            pending?.then(() => {
              if (!visible || userPaused || reducedMotion.matches || document.hidden || video !== activeVideo()) video.pause();
            }).catch(updateButton);
          } else video.pause();
        });
        updateButton();
      };
      videos.forEach((video) => {
        video.muted = true;
        video.pause();
        video.addEventListener('playing', () => {
          video.classList.add('is-ready');
          updateButton();
        }, options);
        video.addEventListener('pause', updateButton, options);
        video.addEventListener('error', () => {
          video.classList.remove('is-ready');
          updateButton();
        }, options);
      });
      button?.addEventListener('click', () => {
        const video = activeVideo();
        if (!video) return;
        userPaused = !video.paused;
        sync();
      }, options);
      const observer = new IntersectionObserver(([entry]) => {
        visible = entry.isIntersecting;
        sync();
      }, { threshold: 0.15 });
      observer.observe(container.querySelector('.teklo-hero-film__media') || container);
      instances.set(container, {
        sync,
        destroy() {
          observer.disconnect();
          abort.abort();
          videos.forEach((video) => video.pause());
        }
      });
      updateButton();
    });
  }
  const syncAll = () => instances.forEach((instance) => instance.sync());
  window.tekloMediaPrepare = prepare;
  prepare();
  document.addEventListener('shopify:section:load', (event) => prepare(event.target));
  document.addEventListener('shopify:section:unload', (event) => {
    instances.forEach((instance, container) => {
      if (event.target === container || event.target.contains(container)) {
        instance.destroy();
        instances.delete(container);
      }
    });
  });
  reducedMotion.addEventListener('change', syncAll);
  mobile.addEventListener('change', syncAll);
  document.addEventListener('visibilitychange', syncAll);
})();
