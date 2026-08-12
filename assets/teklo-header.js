(() => {
  const initialize = (root = document) => {
    root.querySelectorAll('[data-teklo-overlay-header]').forEach((header) => {
      if (header.dataset.tekloHeaderReady === 'true') return;
      header.dataset.tekloHeaderReady = 'true';
      const section = header.closest('.section-header');
      section?.classList.add('section-header--teklo-overlay');
      let observer;
      let resizeFrame;

      const observeBoundary = () => {
        observer?.disconnect();
        const firstSection = document.querySelector('#MainContent > .shopify-section');
        if (!firstSection) {
          header.classList.add('header-wrapper--teklo-solid');
          return;
        }

        observer = new IntersectionObserver(
          ([entry]) => {
            const heroHasPassed = !entry.isIntersecting && entry.boundingClientRect.bottom <= header.offsetHeight;
            header.classList.toggle('header-wrapper--teklo-solid', heroHasPassed);
          },
          { rootMargin: `-${Math.round(header.offsetHeight)}px 0px 0px 0px`, threshold: 0 }
        );
        observer.observe(firstSection);
      };

      const handleResize = () => {
        cancelAnimationFrame(resizeFrame);
        resizeFrame = requestAnimationFrame(observeBoundary);
      };

      header.tekloRefresh = observeBoundary;
      observeBoundary();
      window.addEventListener('resize', handleResize, { passive: true });
      header.tekloCleanup = () => {
        observer?.disconnect();
        cancelAnimationFrame(resizeFrame);
        window.removeEventListener('resize', handleResize);
        section?.classList.remove('section-header--teklo-overlay');
      };
    });
  };

  const refresh = () => {
    document.querySelectorAll('[data-teklo-overlay-header]').forEach((header) => header.tekloRefresh?.());
  };

  initialize();
  document.addEventListener('shopify:section:load', (event) => {
    initialize(event.target);
    requestAnimationFrame(refresh);
  });
  document.addEventListener('shopify:section:reorder', () => requestAnimationFrame(refresh));
  document.addEventListener('shopify:section:unload', (event) => {
    event.target.querySelectorAll('[data-teklo-overlay-header]').forEach((header) => header.tekloCleanup?.());
    requestAnimationFrame(refresh);
  });
})();
