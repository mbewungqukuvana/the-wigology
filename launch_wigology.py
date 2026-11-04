"""Start Streamlit with The Wigology's branded pre-React loading screen.

The splash is inserted into Streamlit's HTML shell, so it appears before
Streamlit's JavaScript UI. This leaves the existing app, owner authentication,
and Streamlit routes/websockets unchanged.
"""

from __future__ import annotations

import os
from pathlib import Path
import re
import subprocess
import sys


STYLE = r"""
<style id="wigology-preload-style">
  html, body { background: #F7F3EB !important; }
  #root { opacity: 0; }
  html.wigology-ready #root { opacity: 1; }
  #wigology-preload {
    position: fixed; inset: 0; z-index: 2147483647;
    display: flex; align-items: center; justify-content: center;
    box-sizing: border-box; padding: 2rem;
    background: #F7F3EB; color: #38251F;
    transition: opacity .55s ease, visibility .55s ease;
  }
  #wigology-preload.wigology-done {
    opacity: 0; visibility: hidden; pointer-events: none;
  }
  #wigology-preload .wigology-splash-inner { text-align: center; max-width: 95vw; }
  #wigology-preload .wigology-splash-name {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(2.6rem, 7vw, 5rem);
    font-weight: 400; letter-spacing: -.04em; line-height: 1.12;
    animation: wigology-splash-reveal 1.2s ease-out both;
  }
  #wigology-preload .wigology-splash-tagline {
    margin-top: 1.2rem; font-family: Arial, sans-serif;
    font-size: clamp(.58rem, 1.3vw, .82rem);
    letter-spacing: .23em; color: #755C4C;
    animation: wigology-splash-reveal 1.2s .22s ease-out both;
  }
  #wigology-preload .wigology-splash-note {
    margin-top: 2rem; color: #755C4C; font: 12px Arial, sans-serif;
  }
  #wigology-preload button {
    margin-top: .8rem; background: transparent; color: #38251F;
    border: 1px solid #38251F; padding: .7rem 1rem;
    font: 12px Arial, sans-serif; cursor: pointer;
  }
  #wigology-preload [hidden] { display: none !important; }
  @keyframes wigology-splash-reveal {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
  }
  @media (prefers-reduced-motion: reduce) {
    #wigology-preload *, #wigology-preload { animation: none !important; transition: none !important; }
  }
</style>
"""

SPLASH = r"""
<div id="wigology-preload" role="status" aria-live="polite" aria-label="The Wigology is loading">
  <div class="wigology-splash-inner">
    <div class="wigology-splash-name">The Wigology.</div>
    <div class="wigology-splash-tagline">THE ART &amp; SCIENCE OF HAIR</div>
    <div class="wigology-splash-note" id="wigology-splash-note" hidden>Taking longer than usual to load…</div>
    <button id="wigology-splash-show" type="button" hidden>Show website</button>
  </div>
</div>
<script id="wigology-preload-script">
(() => {
  const overlay = document.getElementById('wigology-preload');
  const note = document.getElementById('wigology-splash-note');
  const show = document.getElementById('wigology-splash-show');
  const started = performance.now();
  const minDurationMs = 2200;
  let finished = false;
  let scheduled = false;

  function finish() {
    if (finished) return;
    finished = true;
    document.documentElement.classList.add('wigology-ready');
    overlay.classList.add('wigology-done');
    window.setTimeout(() => overlay.remove(), 650);
    observer.disconnect();
  }

  function appHasRendered() {
    const root = document.getElementById('root');
    if (!root) return false;
    const main = root.querySelector('[data-testid="stMain"]');
    if (!main) return false;
    // Look for actual app content, not Streamlit's empty grey skeletons.
    const selectors = [
      '.wigology-home-copy', '.wigology-shop-intro',
      '.wig-science-pattern-stage', '.wig-builder-title',
      '[data-testid="stException"]',
      'h1', 'h2', 'h3', 'input', 'button', '[data-testid="stImage"] img'
    ];
    return selectors.some(selector => {
      const element = main.querySelector(selector);
      return element && element.getClientRects().length > 0;
    });
  }

  function checkReady() {
    if (finished || scheduled || !appHasRendered()) return;
    scheduled = true;
    const wait = Math.max(0, minDurationMs - (performance.now() - started));
    window.setTimeout(finish, wait);
  }

  const observer = new MutationObserver(checkReady);
  observer.observe(document.documentElement, { childList: true, subtree: true });
  document.addEventListener('DOMContentLoaded', checkReady, { once: true });
  window.setTimeout(checkReady, 1000);
  // If startup fails, offer a way to reveal Streamlit's error screen.
  window.setTimeout(() => {
    if (!finished) { note.hidden = false; show.hidden = false; }
  }, 12000);
  show.addEventListener('click', finish);
})();
</script>
"""


def add_splash(index_html: str) -> str:
    """Insert the splash once into a Streamlit frontend index.html."""
    if 'id="wigology-preload"' in index_html:
        return index_html
    if "</head>" not in index_html.lower():
        raise RuntimeError("Streamlit index.html has no closing </head> tag")
    index_html, head_count = re.subn(
        r"</head\s*>", lambda _: STYLE + "\n</head>", index_html,
        count=1, flags=re.IGNORECASE,
    )
    index_html, body_count = re.subn(
        r"<body\b[^>]*>", lambda match: match.group(0) + "\n" + SPLASH,
        index_html, count=1, flags=re.IGNORECASE,
    )
    if head_count != 1 or body_count != 1:
        raise RuntimeError("Could not insert Wigology splash into Streamlit HTML")
    return index_html


def main() -> None:
    import streamlit

    index_path = Path(streamlit.__file__).resolve().parent / "static" / "index.html"
    if not index_path.is_file():
        raise SystemExit(f"Streamlit frontend HTML not found at {index_path}")
    current = index_path.read_text(encoding="utf-8")
    updated = add_splash(current)
    if updated != current:
        index_path.write_text(updated, encoding="utf-8")
        print("The Wigology branded loading screen installed.", flush=True)
    else:
        print("The Wigology branded loading screen already installed.", flush=True)

    port = os.environ.get("PORT", "8501")
    cmd = [
        sys.executable, "-m", "streamlit", "run", "main.py",
        "--server.address=0.0.0.0", f"--server.port={port}",
        "--server.headless=true",
    ]
    raise SystemExit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
