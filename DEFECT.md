# TECHNICAL AUDIT: NBAS ASTRO V0.19.0 TAXONOMY DEFECTS
**Author:** AI Assistant  
**Date:** April 29, 2026  
**Context:** Hugo v0.160.1 Environment  

## 1. ARCHITECTURAL DEFECTS (THE "MELTDOWN" CAUSES)

### 1.1 Taxonomy Lookup Collision
**Defect:** Specific overrides for Messier/NGC/Stars were ignored by the engine, causing a fallback to `layouts/_default/taxonomy.html`.
**Analysis:** In Hugo v0.160.1, the naming convention is extremely rigid. The engine expects a pluralized directory (`layouts/taxonomies/`) and a dual-suffix file naming system (`[name].terms.html` for the list of objects vs `[name].term.html` for the list of articles). 
**Current State:** The site is in a "Default Fallback" state, treating scientific data as if it were editorial "Series" content.

### 1.2 Block Namespace Collision
**Defect:** The "Series" and "Tags" pages lost their layout/styling during scientific template edits.
**Analysis:** Using `{{ define "main" }}` in multiple template files in this version of Hugo can lead to global namespace pollution. If the engine loads a scientific template last, it overwrites the "main" block for the entire site, including the Editorial and Tags pages.

## 2. DATA RENDERING DEFECTS (THE "UI" ISSUES)

### 2.1 Lexicographical vs. Numerical Sorting
**Defect:** Messier and Caldwell objects are sorted as `1, 10, 100, 11...`
**Analysis:** Hugo v0.160.1 treats `.Title` and `.Term` as strings. String sorting evaluates character by character. 
**Current State:** The "math" fixes using `Scratch` and `printf` failed because the engine's map iteration does not respect numeric casting of string keys without explicit weight assignment.

### 2.2 Pagination Leakage
**Defect:** Scientific lists (Messier/Caldwell) are being paginated at 10 items per page.
**Analysis:** The site-wide `paginate = 10` setting in `hugo.toml` is being inherited by the `_default` template. 
**Current State:** Users cannot see the full catalog at once, violating the requirement for "all-on-one-page" observational lists.

### 2.3 Contextual Branding "Noise"
**Defect:** The "Series" (Newsletter) dropdown appears on scientific pages (e.g., Variable Stars).
**Analysis:** The `article-card.html` partial lacks a conditional check to see *where* it is being rendered. It is currently hardcoded to display editorial "Series" metadata even when the user's intent is scientific research.

## 3. COMPONENT ANALYSIS & REMEDIATION TASKS

### 3.1 Template Refactoring
*   **Defect:** Shared logic between Tags, Series, and Science.
*   **Remediation:** Create a strict firewall. Scientific taxonomies must use the `.terms.html` and `.term.html` naming convention to force Hugo out of the `_default` fallback loop.

### 3.2 Metadata Weighting
*   **Defect:** Lack of numeric sort control.
*   **Remediation:** The 219+ `_index.md` files for Messier and Caldwell objects require a `weight: [int]` parameter. This is the only 100% stable method in v0.160.1 to force 1, 2, 3... ordering.

### 3.3 Partial Logic Update
*   **Defect:** `article-card.html` metadata pollution.
*   **Remediation:** Implement a context check. If the parent page is a scientific taxonomy (prefixed with `dso_`, `sso_`, or `stars_`), the card must suppress editorial branding (Series name, newsletter dates).

## 4. INVENTORY OF "GHOST" FILES
**Defect:** The filesystem contains orphaned and colliding files from previous iterations.
**Analysis:** Files like `layouts/taxonomy/taxonomy.html` or `layouts/section/dso_messier.html` may still be affecting the build pipeline.
**Remediation:** A full purge of the `layouts/taxonomy/`, `layouts/taxonomies/`, and `layouts/section/` directories is required to return to a clean "Known Good" state.
