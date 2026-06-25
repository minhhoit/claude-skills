# Personal Skills

A private workflow pack for a solo-parent founder building toward financial independence while working a 9-5. These five skills encode recurring personal workflows so Claude applies them automatically, without re-explaining context each time.

| Skill | Fires when you… | Gives you |
|-------|-----------------|-----------|
| `youtube-policy-script` | write/review any YouTube script, hook, idea | policy verdict → retention script → titles → thumbnail |
| `en-demo-coach` | write/fix English for demos, emails, practice | natural rewrite + ≤2 L1 coaching notes |
| `decision-triage` | ask what to do tonight / whether to take on X | do-tonight / defer / drop, sized to your energy |
| `product-copy` | write copy for Content Pilot or GearPickle | paste-ready, feature→benefit copy in voice |
| `backend-conventions` | write/review backend or AI code | in-stack code + cost/ops guardrails |

## Setup

These follow the Agent Skills standard (one folder, `SKILL.md` per skill). Three ways to use them:

**Claude.ai** — zip a skill folder (the folder must sit at the root of the zip), then Settings → Customize → Skills → `+` → Create skill → upload. Requires Code execution enabled. Toggle per chat from the Skills menu.

**Claude Code** — copy a skill folder into `~/.claude/skills/` (personal) or `.claude/skills/` (project).

**Fill the placeholders.** Several skills contain `[điền: ...]` markers for private specifics (your YouTube policy post-mortem checklist, your stack/conventions, your brand voice, recurring L1 errors). Edit those before relying on the skill — they're what make it yours.

## Note on this repo

`personal/` is intentionally isolated from the upstream skill collection and is **not** scanned by the repo's integrity test or the Codex/Gemini/Hermes sync scripts by default. To include it in those, add `"personal"` to the `SKILL_DOMAINS` list in `tests/test_skill_integrity.py` and the `SKILL_DOMAINS` dict in each `scripts/sync-*-skills.py`.
