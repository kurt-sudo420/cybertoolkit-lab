# AGENTS.md: read this before every task

## Project facts (never contradict these)
CyberToolkit is an interactive, menu-driven Python 3 program. Standard library only.
- Run it with `python3 cybertoolkit.py`. The only flags are `--version` (prints
  `CyberToolkit 1.1.0`) and `-h`/`--help`. There are no per-tool flags.
- Menu: `1. Port Scanner`, `2. SHA-256 File Hash`, `3. Password Generator`,
  `4. DNS Lookup`, `5. Banner Grabber`, `6. Quit`. Prompt: `Choice: `
- Each tool's prompts and output are defined in cybertoolkit.py. Quote them exactly.
- Tests: `python -m pytest -q`. Website: `docs/`, static, served by GitHub Pages.

## How to work
1. Read before you write: README.md, cybertoolkit.py, and every file you will change.
2. Verify, don't assume. Before you write any claim about the program (a flag, a
   prompt, an output, a requirement), confirm it in the code or by running it.
   For example, `printf '6\n' | python3 cybertoolkit.py` prints the menu.
   If you can't verify something, leave it out.
3. Work in small steps. Run `python -m pytest -q` after each one.
4. When a file needs big changes, rewrite it cleanly instead of stacking patches.
5. Never weaken, skip or delete a test to get a pass. Fix the code instead.
6. Before you stop, go through the task's requirements one by one, check each
   against your files, and write in /agent/agent_notes.md what you verified and how.

## Code style
- Small functions, specific exceptions, type hints on new functions, PEP 8.
- No dead code, no commented-out code, no leftover TODOs or debug prints.

## Web quality bar (docs/)
You cannot see the page, so follow these tokens exactly instead of guessing.

Colours (define as CSS custom properties; all text pairs pass WCAG AA):
- Background `#0f141a`, surface `#161d26`, raised surface `#1c2531`, border `#2a3441`
- Text `#e6edf3`, muted text `#9aa7b4`
- Accent `#2dd4bf` (buttons, focus ring); accent text and links `#5eead4`;
  text on accent buttons `#0f141a`
- Callout: border/icon `#f59e0b`, heading `#fbbf24`, background `#2a2110`

Type:
- Text: `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`
- Code: `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`
- Sizes: 14, 16, 18, 20, 24, 32, 40, 48px. Body 16-18px with line-height 1.6;
  headings line-height 1.2, weight 600-700. Code at least 14px.

Layout and spacing:
- Spacing in multiples of 8px (4px for tight gaps). Sections 80px apart on desktop,
  48px on phones.
- Container max-width 1120px with 24px side padding; paragraphs max 70ch.
- Card radius 8px, button and code radius 6px. One shadow:
  `0 1px 2px rgba(0,0,0,.3), 0 8px 24px rgba(0,0,0,.25)`.
- Check the layout at 375px, 768px and 1280px wide.

Components and behaviour:
- One primary button per section. Buttons are at least 44px tall with clear labels.
- Cards in a grid share the same anatomy and equal heights.
- No glow, neon, blinking, text gradients or decorative animation. Motion only as
  feedback, under 200ms, and off under prefers-reduced-motion.
- Every interactive element has hover, active and :focus-visible states
  (2px accent outline, 2px offset).
- Semantic HTML first; ARIA only where HTML can't express it.
- Icons: inline SVG, 24px, 1.5px stroke, `currentColor`.
- Self-contained: no CDNs, web fonts, trackers or external images.
