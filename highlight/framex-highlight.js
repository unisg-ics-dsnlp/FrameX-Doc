// Custom highlight.js grammar for FrameX (explicit-variable F-Logic).
// Registered as `framex`; also aliased to `prolog` (which highlight.js does
// not ship) so existing ```prolog fences highlight automatically.
// mdBook runs its own highlight pass first and leaves unknown languages
// untouched, so this file re-highlights those blocks afterwards.
(function () {
  function framexGrammar(hljs) {
    var def = {
      name: 'FrameX',
      keywords: {
        keyword:
          'world open closed prefix declare subproperty inverse transitive symmetric ' +
          'expect external using extends AND OR',
        literal: 'true false unknown'
      },
      contains: [
        // Line comments.
        hljs.COMMENT('//', '$'),
        // "Double-quoted strings".
        hljs.QUOTE_STRING_MODE,
        // Numbers such as revision 4.
        hljs.NUMBER_MODE,
        // Variables: ?Name, ?Device, ?Revision.
        {
          className: 'variable',
          begin: /\?[A-Za-z_][A-Za-z0-9_]*/
        },
        // Query marker: ?-
        {
          className: 'operator',
          begin: /\?-/
        },
        // Rule, slot, namespace and path operators: <- -> :: :
        {
          className: 'operator',
          begin: /<-?|->|::/
        },
        // Classes are Capitalized CamelCase by convention: Person, DirectAntenna.
        // (Requires a lowercase second letter so AND/OR stay keywords.)
        {
          className: 'title',
          begin: /\b[A-Z][a-z][A-Za-z0-9_]*/
        }
      ]
    };
    // Only claim `prolog` if highlight.js has no grammar for it.
    if (!hljs.getLanguage('prolog')) {
      def.aliases = ['prolog'];
    }
    return def;
  }

  function register() {
    if (!window.hljs) {
      return false;
    }
    try {
      if (!window.hljs.getLanguage('framex')) {
        window.hljs.registerLanguage('framex', framexGrammar);
      }
    } catch (e) {
      return false;
    }
    return true;
  }

  // A block is truly highlighted only if it contains highlight spans.
  // (mdBook adds the bare `hljs` class to every block at runtime, even
  // unhighlighted ones, so the class alone proves nothing.)
  function isHighlighted(el) {
    return el.querySelector('span[class*="hljs-"]') !== null;
  }

  function apply() {
    if (!register()) {
      return;
    }
    document
      .querySelectorAll('pre code.language-framex, pre code.language-prolog')
      .forEach(function (el) {
        if (isHighlighted(el)) {
          return;
        }
        try {
          if (window.hljs.highlightElement) {
            window.hljs.highlightElement(el);
          } else if (window.hljs.highlightBlock) {
            window.hljs.highlightBlock(el);
          }
        } catch (e) {
          /* leave the block as plain text */
        }
      });
  }

  // Register immediately: this script loads after highlight.js but before
  // mdBook's own highlight pass runs, so mdBook picks the grammar up itself.
  // The apply() pass on top covers every ordering.
  register();

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', apply);
    } else {
      apply();
    }
  }

  // Export the grammar for testing outside the browser.
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = framexGrammar;
  }
})();
