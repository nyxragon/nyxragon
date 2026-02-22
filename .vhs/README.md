# Terminal GIFs (VHS)

These [VHS](https://github.com/charmbracelet/vhs) tape files generate the **letter-by-letter typing** terminal GIFs used in the profile README: real typing, output, then `clear` and repeat.

## Generate GIFs

**Option A – GitHub Action**  
Push changes to `.vhs/`, `scripts/`, `experience`, or `focus`, or run the workflow **Generate terminal GIFs (VHS)** manually. It will produce `assets/whoami.gif`, `assets/experience.gif`, `assets/focus.gif` and commit them.

**Option B – Local**  
Install [VHS](https://github.com/charmbracelet/vhs) (requires ttyd + ffmpeg), then from repo root:

```bash
vhs .vhs/whoami.tape
vhs .vhs/experience.tape
vhs .vhs/focus.tape
```

GIFs are written to `assets/`. The custom `whoami` output comes from `scripts/whoami`; `cat experience` and `cat focus` use the repo files `experience` and `focus`.
