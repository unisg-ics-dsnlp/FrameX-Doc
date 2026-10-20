# FrameX-Doc
Documentation of the FrameX Tool. Part of the Hybrid AI course at HSG.

Built with [mdBook](https://github.com/rust-lang/mdBook), hosted on GitHub Pages.

## Local preview

```bash
mdbook serve --open
# or: mdbook build
```

Source pages are in `src/`, structure in `src/SUMMARY.md`.

## Scope

The book covers public [FrameX-Core](https://gitlab.com/ds-unisg/framex-core)
0.4.4, its Python hosts, and the hybrid patterns from Studio EX06 and
Siegfried Handschuh's *Hybrid AI Patterns* (October 2026). Source revisions,
reading references and public-export limitations are in
`src/hybrid/sources.md`. The course PDFs are not redistributed here.

Update `src/SUMMARY.md` and the relevant index pages when adding chapters.
The generated `book/` directory is ignored. CI builds with mdBook 0.5.4 and
deploys pushes to `main` to GitHub Pages.

## Check executable documentation

After installing FrameX-Core and its Python package:

```bash
python3 scripts/check-examples.py --binary /absolute/path/to/framex
mdbook build
```

The checks run without model calls. They compare tutorial query answers,
expectations, the family example, extraction receipt scenarios and Python
exercise output, then run the tool-query host and scripted dialogue. Live
model examples need separately configured providers and are not part of this
offline check.
