# Technical Diagnostic & Handover Report: Astronomy.js Integration

## 1. Project Context
*   **Environment:** Hugo (Themless), static website.
*   **Hosting:** Local development (MacOS) transitioning to GitHub Pages.
*   **Library:** `astronomy.js` (Don Cross), ~9,000 lines, Node.js-compiled version (CommonJS).
*   **Location:** `/static/js/astronomy.js`.
*   **Target Output:** A real-time astronomical dashboard for Sun, Moon, and 8 planets (including Pluto).

## 2. Verified Library "DNA" (Critical)
The following behaviors were verified through browser-based inspection and failed iterations:
*   **Format:** The file is a CommonJS module. It crashes in the browser unless `window.exports = {};` is defined **before** the script loads.
*   **Scope:** Once the `exports` shield is provided, the library pollutes the **global window scope** with its internal functions instead of nesting them under a namespace.
*   **Object Names:** The library uses full property names: `azimuth` and `altitude` (NOT `az` and `alt`).
*   **Initialization:** Being a large file using ES6 classes (like `AstroTime`), it is subject to the **Temporal Dead Zone**. It cannot be called until the browser has fully parsed the 9,000 lines.

## 3. Function Inventory (The "Secret Decoder Ring")
Verified function signatures from the internal directory:
*   `MakeTime(Date)`: Returns the required time object.
*   `Observer(lat, lon, height)`: Returns the observer object.
*   `Equator(body, time, observer, aberrationBool, nutationBool)`: Returns `{ra, dec, dist}`.
*   `Horizon(time, observer, ra, dec, refractionOption)`: Returns `{azimuth, altitude}`.
    *   *Constraint:* `refractionOption` MUST be the string `"normal"` or `"none"`. Booleans (`true`) or nulls cause validation crashes.
*   `VisualMagnitude(body, time)`: Returns brightness.
    *   *Constraint:* Crashes on `"Sun"` and `"Moon"`. These must be handled with hardcoded constants or distinct functions (e.g., `MoonMagnitude`).
*   `Illumination(body, time)`: Returns `{phase}`.

## 4. The "Death Spiral" Log (Avoid These)
1.  **Do NOT** use `type="module"` or `import()`. It creates a strict scope that breaks the `exports` shim.
2.  **Do NOT** use `Astro.` or `Lib.` prefixes. The functions exist as bare globals (e.g., `Equator()`).
3.  **Do NOT** use `absURL` or `relURL` if the site is in a subfolder; use root-relative paths like `/js/astronomy.js`.
4.  **Do NOT** pass `true` as the last argument to `Horizon()`; it expects `"normal"`.

## 5. Final Working Foundation (The Last Stable Logic)
To reconstruct the dashboard, the next agent must:
1.  Provide `window.exports = {}`.
2.  Load the script via standard `<script src="/js/astronomy.js"></script>`.
3.  Wrap execution in a `window.addEventListener('load', ...)` or a retry loop to ensure `AstroTime` is initialized.
4.  Call global functions directly: `MakeTime`, `Equator`, `Horizon`.
5.  Use `hor.azimuth` and `hor.altitude`.
6.  Exclude `Sun` and `Moon` from `VisualMagnitude` calls.

## 6. Directory Inspection Tool
If the next agent needs to re-verify the "Secret Decoder Ring," they should run this snippet in the shortcode:
```javascript
console.log(Object.keys(window).filter(k => typeof window[k] === 'function' && k.match(/^[A-Z]/)));
```

***

**Proactive Follow-up:** This report contains the verified state of the **CommonJS-to-Browser** bridge. Use this to skip the first 10 steps of environmental setup and move directly to **formatting the dashboard data**.

