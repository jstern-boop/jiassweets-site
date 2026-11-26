# Jia's Sweets website

Built and hosted by Island Pixel Studios.

- `docs/` – the published website. GitHub Pages: branch `main`, folder `/docs`. Cloudflare Pages later: build output directory `docs`, no build command.
- `tools/build.py` – generates every page in `docs/`. Edit content here, then run `python3 tools/build.py`.
  - Bump `VER` after any CSS/JS change so phones load the new files.
  - `NOINDEX = True` hides the site from search engines until launch. Set to `False` at launch and rebuild.
- Contact form: replace `WEB3FORMS_KEY_AT_LAUNCH` in `tools/build.py` with the Web3Forms access key at launch.
- Images in `docs/images/` are Jia's own product photos. Pink dashed "Jia's words go here" boxes mark text she still needs to supply.
