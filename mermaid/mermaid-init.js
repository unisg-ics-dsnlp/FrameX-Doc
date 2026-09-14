// Loads Mermaid from a pinned CDN and renders ```mermaid code blocks.
// If the CDN is unreachable, the blocks stay readable as plain code.
(function () {
  var CDN = 'https://cdn.jsdelivr.net/npm/mermaid@10.9.3/dist/mermaid.min.js';

  function render() {
    document.querySelectorAll('pre code.language-mermaid').forEach(function (code) {
      var pre = code.parentElement;
      var div = document.createElement('div');
      div.className = 'mermaid';
      div.textContent = code.textContent;
      pre.replaceWith(div);
    });
    window.mermaid.initialize({ startOnLoad: false, securityLevel: 'strict' });
    if (window.mermaid.run) {
      window.mermaid.run();
    } else {
      window.mermaid.contentLoaded();
    }
  }

  if (document.querySelector('pre code.language-mermaid')) {
    var s = document.createElement('script');
    s.src = CDN;
    s.onload = render;
    // onerror: leave the code blocks as-is (readable fallback).
    document.head.appendChild(s);
  }
})();
