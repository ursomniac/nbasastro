# Member Images Feature Plan

## Series & Content Structure

- Series name: **"From the Eyepiece"** (or TBD)
- Bi-weekly articles, controlled by `date:` front matter
- Article front matter includes `image:` field for the card thumbnail / widget
- Series slug: `from-the-eyepiece` (or similar)
- ~8–10 images per article max; increase frequency if volume grows

---

## Step 1: Add `contributors` Taxonomy

In `hugo.toml`/`config.toml`, add:

```toml
[taxonomies]
  contributor = "contributors"
```

- No custom layout needed yet — Hugo generates contributor archive pages automatically
- Add `contributors: ["Name"]` to article front matter when known
- Phase 2: customize contributor page layout to show images

---

## Step 2: Create `member-image` Shortcode

File: `layouts/shortcodes/member-image.html`

**Parameters (all optional except `src`):**

| Param | Description |
|---|---|
| `src` | Image filename (required) |
| `by` | Contributor name |
| `when` | Date/time of observation |
| `where` | Location (freeform, e.g. "North Adams, MA") |
| `scope` | Telescope/equipment |
| `exposure` | Exposure info |
| `object` | DSO name/designation |

**Inner content** (`.Inner`): optional short commentary, rendered below metadata.

```
{{< member-image src="m13.jpg" by="John Smith" scope='8" Dob' 
    exposure="30x60s" object="M13" where="North Adams, MA" >}}
Surprisingly steady night — 45 min integration before clouds.
{{< /member-image >}}
```

**Rendering:** image + optional metadata block + optional commentary. Style to match existing `nbas-image` shortcode where possible.

**Test:** Create a scratch article, drop in 2–3 `member-image` calls with varying levels of metadata (some full, some minimal, one with commentary), verify layout.

---

## Step 3: Create `member-gallery` Series Page (minimal)

- Use default Hugo series layout for now
- Lists all "From the Eyepiece" articles in reverse-chronological order
- Revisit layout after a few issues are published and usage patterns are clear

---

## Step 4: Sidebar Widget

File: `layouts/partials/widget-member-images.html` (or equivalent for your theme)

**Logic:**
1. Find the most recent article in the series
2. `shuffle` its image list, take `index . 0` — random image, refreshed on nightly rebuild
3. Fall back to article's `image:` front matter if no image list available
4. Link to the article

**Test:** Confirm widget appears in sidebar, image varies across rebuilds, link is correct.

---

## Step 5: First Real Article

- Collect member image submissions
- Publish first "From the Eyepiece" article using the new shortcode
- Verify DSO metadata cross-links work (existing `dso_messier` etc. taxonomy)
- Verify contributor taxonomy page generates correctly

---

## Deferred / Phase 2

- Custom contributor page layout (show images, not just article list)
- Per-image hover metadata (if desired)
- Decide on series name if "From the Eyepiece" doesn't stick
- Custom series landing page if default layout isn't sufficient
