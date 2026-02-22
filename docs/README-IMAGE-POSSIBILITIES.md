# Image & GIF possibilities in GitHub README

Summary of what works and what doesn’t for profile READMEs (from public docs and community findings).

---

## What works

### 1. **Direct image / GIF in Markdown or HTML**
- Store file in repo (e.g. `assets/whoami-illusion.gif`).
- Use `<img src="assets/whoami-illusion.gif" />` or `![](assets/whoami-illusion.gif)`.
- GIFs animate; no size limit beyond repo/renderer behavior.

### 2. **SVG as a separate file**
- Store `.svg` in repo, reference with `<img src="assets/card.svg" />` or `![](assets/card.svg)`.
- GitHub renders the SVG when it’s loaded as an **external file** via `img` (or markdown image syntax), not when it’s inline in the markdown.

### 3. **Base64 image in Markdown**
- `<img src="data:image/gif;base64,..." />` works in README.
- Good for small images; large GIFs make the README huge and hard to edit.

### 4. **External image URLs**
- `<img src="https://example.com/image.gif" />` works if the URL is public and allowed by GitHub (no hotlink protection, etc.).
- Risk: external links can break or change.

### 5. **Table layout (text + GIF)**
- One cell: text or SVG card.
- Other cell: `<img src="assets/your.gif" />`.
- Reliable way to get “text + GIF” side by side on GitHub.

---

## What doesn’t work (or is unreliable)

### 1. **Image inside SVG (`<image href="...">`)**
- GitHub serves README images via **camo** with a CSP that effectively allows only `data:` for nested resources.
- External URLs in SVG (e.g. `href="whoami-illusion.gif"` or `https://raw.githubusercontent.com/...`) are **blocked** when the SVG is rendered in the README.
- So the GIF “inside the card” (inside the SVG) does **not** show on GitHub; only the rest of the SVG (e.g. text) does.

References:
- [SVG image tag doesn't work on github README](https://stackoverflow.com/questions/72151299/svg-image-tag-doesnt-work-on-github-readme)  
- GitHub adds `?sanitize=true` to SVG URLs and strips/restricts external references.

### 2. **Inline SVG in Markdown**
- Pasting full SVG markup into the README is not a supported way to “render” an SVG on GitHub; it’s treated as code or raw HTML and won’t show as an image.

### 3. **iframe**
- GitHub Flavored Markdown does not allow iframes (e.g. Pinterest embed); they are stripped.

---

## Workaround: GIF inside SVG using data URI

The only way to have the GIF **inside** the same SVG and still satisfy GitHub’s CSP is to **inline the GIF as a data URI** inside the SVG (no external URL):

- In the SVG: `<image href="data:image/gif;base64,R0lGOD..." />`
- The SVG file (or the image tag) must be loaded as a normal README image (e.g. `<img src="assets/whoami-full.svg" />`).

**Trade-offs:**
- The SVG file becomes much larger (GIF size × ~1.33 for base64).
- You need to regenerate the SVG whenever you change the GIF (e.g. with a small script).

If you want, we can add a script that builds `whoami-full.svg` from the text layout + `whoami-illusion.gif` inlined as base64 so you get “GIF inside the card” on GitHub.

---

## Practical recommendation for “whoami + GIF”

- **Option A – GIF inside card (single asset):**  
  Use one SVG with the GIF inlined as `data:image/gif;base64,...`. Requires a build step to embed the GIF.
- **Option B – GIF beside card (no build step):**  
  Use a table: left cell = whoami SVG (text only), right cell = `<img src="assets/whoami-illusion.gif" />`. Works today and is easy to maintain.
