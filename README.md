# Jia's Sweets website

Built and hosted by Island Pixel Studios.

- `site/` – the published website (Cloudflare Pages build output directory: `site`, no build command).
- `tools/build.py` – generates every page in `site/`. Edit content here, then run `python3 tools/build.py`.
  - Bump `VER` after any CSS/JS change so phones load the new files.
  - `NOINDEX = True` hides the site from search engines until launch. Set to `False` at launch and rebuild.
- Contact form: replace `WEB3FORMS_KEY_AT_LAUNCH` in `tools/build.py` with the Web3Forms access key at launch.
- Images in `site/images/` are Jia's own product photos. Pink dashed "Jia's words go here" boxes mark text she still needs to supply.
