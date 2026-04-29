# PROPOSAL: TEMPLATE-BASED NUMERIC FIX (V0.19.6)
**Goal:** Fix the numeric order (1, 2, 3...) and the "Big Card" look for scientific catalogs without creating physical folders in `content/` or modifying the editorial `_default/taxonomy.html`.

## 1. THE LOGIC DEFECT
In Hugo v0.160.1, the engine treats all taxonomy terms (like "1", "10", "2") as **strings**. 
*   **Alphabetical Sort:** `1, 10, 11, 2, 20` (Standard dictionary behavior).
*   **Numeric Sort (Target):** `1, 2, 10, 11, 20` (Mathematical behavior).

Since there are no physical `_index.md` files to hold a `weight` parameter, the fix must happen entirely within the rendering logic of a specific template.

## 2. THE SOLUTION: "CAST-AND-SORT" OVERRIDES
We will create isolated templates in `layouts/taxonomy/` using the strict naming convention required by your version of Hugo. These files will "intercept" the scientific data before it falls back to the broken `_default` cards.

### A. For Messier & Caldwell (Numeric Grid)
**File:** `layouts/taxonomy/dso_messier.terms.html`  
**File:** `layouts/taxonomy/dso_caldwell.terms.html`  

**Mechanism:** 
1.  Range over all terms found in articles.
2.  Use a math-based `Scratch` map to pad the IDs (e.g., "1" becomes "001").
3.  Display the objects in a tight grid of small "Badges" instead of "Series Cards."

### B. For NGC & Other (Searchable Table)
**File:** `layouts/taxonomy/dso_ngc.terms.html`  

**Mechanism:**
1.  A compact, paginated list showing the Object ID and the number of articles.
2.  Suppresses the "By NBAS" and "Jan 1, 0001" metadata.

### C. For The Term View (The Article Cards)
**File:** `layouts/taxonomy/taxonomy.term.html`

**Mechanism:**
1.  This triggers when you click a specific object (e.g., /dso_messier/42/).
2.  It renders the standard `article-card.html` but passes a flag to **suppress the Series dropdown**, keeping the focus on the scientific context.

## 3. WHY THIS IS STABLE
*   **Zero Content Change:** You do not need to create 200+ folders or `_index.md` files.
*   **Zero Editorial Impact:** Your Newsletter and Series pages continue to use `_default/taxonomy.html` exactly as they do now.
*   **Strict Suffixes:** By using `.terms.html` and `.term.html`, we follow the precise lookup rules of your Hugo version, preventing the "Death Spiral" of template collisions.

## 4. IMPLEMENTATION RISKS
*   **Sorting Complexity:** If the ID contains letters (e.g., "7320C"), the numeric cast needs a fallback to standard sorting to avoid build errors.
*   **Style Sync:** New CSS classes will be needed to make the "Badges" look professional and distinct from the "Series Cards."
