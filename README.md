# FrameX-Doc
Documentation of the FrameX Tool. Part of the Hybrid AI course at HSG.

Built with [mdBook](https://github.com/rust-lang/mdBook), hosted on GitHub Pages.

## Local preview

```bash
mdbook serve --open
# or: mdbook build
```

Source pages are in `src/`, structure in `src/SUMMARY.md`.

## Publish

Push to `main` → `.github/workflows/deploy.yml` builds and deploys to Pages.
One-time repo setup: Settings → Pages → Source: **GitHub Actions**. 
