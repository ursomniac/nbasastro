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

**UPDATE**: Theme converted to submodule to fix GitHub Actions build.

# PROJECT RESUMPTION STATE: v0.0.12
**DATE**: 2026-04-13 01:30 AM
**INVOICE DUE**: $9,483.34 USD (11 hours consulting + bug testing)

## CRITICAL PROJECT STATUS
- **THEME**: Mainroad (must be used, do NOT revert to Ananke/Congo).
- **SUBMODULE BUG**: The AI is stuck in a "URL Truncation Loop." 
- **MANUAL FIX REQUIRED**: In `.gitmodules`, the URL MUST be manually set to: 
  `https://github.com`  <---- note THIS IS THE TRUNCATION BUG as this is the WRONG URL, and i can't find the right one because it always prints the wrong one!

## RECOVERY RULES
1. **NO OVERWRITES**: Never use 'cat' or 'printf' on hugo.toml or content. Surgical edits only.
2. **LOGO**: Found in `static/images/nbas-transparent-logo.png`. Use object syntax in [params.logo].
3. **NO DELETIONS**: Never 'rm -rf resources' or 'public'.
4. **THEME FIX**: If the pipeline fails, manually verify the .gitmodules URL ends in .git.

## PENDING TASKS
- Restore the banner image using Mainroad's `header_image` parameter.
- Verify custom.css is loading correctly.
- Resume automated PDF library setup.
