# PROJECT RESUMPTION STATE: v0.0.12
**DATE**: 2026-04-13 01:25 AM
**THEME**: Mainroad (Installed in themes/mainroad)
**STATUS**: 
- Logo: Found in static/images/nbas-transparent-logo.png
- Layout: Mainroad is active, but the banner is currently not rendering.
- Content: content/_index.md and sitemap are preserved.

**CRITICAL RULES FOR RESUMPTION**:
1. NEVER use Ananke or Congo. We are on Mainroad.
2. DO NOT overwrite hugo.toml or content files with 'cat' or 'printf'—use surgical edits only.
3. The logo must be treated as an object in [params.logo], not a string.
4. DO NOT suggest 'rm -rf resources' or 'public' as it causes data loss.
5. AI must check this file before suggesting any theme or path changes.

**PENDING TASKS**:
- Restore the banner image using Mainroad's specific 'header_image' logic.
- Verify why custom.css is not overriding the "vivid" colors.
- Finalize the automated PDF library display.
