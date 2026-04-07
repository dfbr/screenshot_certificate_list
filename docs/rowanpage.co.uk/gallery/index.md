---
title: "rowanpage.co.uk Gallery (07.04.2026)"
layout: default
---

# rowanpage.co.uk Gallery

[← rowanpage.co.uk](../) &middot; [← All domains](../../)

Latest run shown: [07.04.2026](../2026-04-07_06-19-00/)

<style>
  html, body {
    overflow: hidden;
  }

  .gallery-viewport {
    position: relative;
    width: 100%;
    height: 60vh;
    min-height: 300px;
    overflow: hidden;
    border: 1px solid #d8dee4;
    border-radius: 8px;
    background: #ffffff;
  }

  .gallery-scale-root {
    transform-origin: top left;
    will-change: transform;
  }

  .gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    gap: 10px;
    padding: 10px;
  }

  .gallery-item {
    margin: 0;
    border: 1px solid #e6ebf1;
    border-radius: 6px;
    overflow: hidden;
    background: #f6f8fa;
  }

  .gallery-item a {
    display: block;
    text-decoration: none;
    color: inherit;
  }

  .gallery-item img {
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 16 / 10;
    object-fit: cover;
    background: #ffffff;
  }

  .gallery-item figcaption {
    font-size: 0.78rem;
    line-height: 1.2;
    padding: 0.32rem 0.45rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    border-top: 1px solid #e6ebf1;
    background: #ffffff;
  }

  @media (max-width: 900px) {
    .gallery-grid {
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    }
  }
</style>

<div id="gallery-viewport" class="gallery-viewport">
  <div id="gallery-scale-root" class="gallery-scale-root">
    <div id="gallery-grid" class="gallery-grid">
      <p>No successful screenshots available for the latest run.</p>
    </div>
  </div>
</div>

<script>
  (function () {
    const viewport = document.getElementById('gallery-viewport');
    const root = document.getElementById('gallery-scale-root');
    const grid = document.getElementById('gallery-grid');

    function fitGallery() {
      if (!viewport || !root || !grid) return;

      const top = viewport.getBoundingClientRect().top;
      const availableHeight = Math.max(220, window.innerHeight - top - 10);
      viewport.style.height = `${availableHeight}px`;
      root.style.transform = 'scale(1)';
      root.style.width = 'auto';
      root.style.height = 'auto';

      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;
      const gw = grid.scrollWidth;
      const gh = grid.scrollHeight;

      if (!vw || !vh || !gw || !gh) return;

      const scale = Math.min(vw / gw, vh / gh, 1);
      const scaledW = gw * scale;
      const scaledH = gh * scale;

      root.style.transform = `scale(${scale})`;
      root.style.width = `${gw}px`;
      root.style.height = `${gh}px`;
      root.style.marginLeft = `${Math.max(0, (vw - scaledW) / 2)}px`;
      root.style.marginTop = `${Math.max(0, (vh - scaledH) / 2)}px`;
    }

    window.addEventListener('load', fitGallery);
    window.addEventListener('resize', fitGallery);
    setTimeout(fitGallery, 250);
  })();
</script>

