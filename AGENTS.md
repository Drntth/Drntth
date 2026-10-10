# Drntth

Commit prefix: [DRNTTH]

## Purpose

GitHub profile README: short introduction, focus areas, tech stack, selected public projects and a link to the portfolio site. Finished; changes are occasional content updates.

## Stack

Markdown with inline HTML (centered blocks, shields.io badges), rendered by GitHub on the profile page. No build, no tooling.

## Structure

- `README.md`: English profile (shown on the GitHub profile).
- `README.hu.md`: Hungarian version, linked from the English one.

## Conventions and gotchas

- `README.md` and `README.hu.md` change together and keep the same structure.
- The Projects table lists only public, presentable projects; descriptions match the portfolio site's project entries. Keep the table columns aligned.
- Name: short form "Dorina Tóth" (en) and "Tóth Dorina" (hu).
- Never publish a phone number, address or birth date.
- Markdown inside an HTML block renders only after a blank line following the opening tag.
- Inline HTML is intentional; markdownlint MD033/MD041 warnings on the header are expected.
