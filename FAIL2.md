# MISSION CRITICAL: Astronomy.js Integration Recovery Handoff

## 1. Environment & Library DNA
- **Engine:** Hugo (Themless/Static).
- **Library:** `astronomy.js` (Don Cross). ~9,000 lines.
- **Build Type:** CommonJS (Node-compiled). 
- **Browser Bridge:** Requires `window.exports = {}` defined **before** script load to prevent crash.
- **Namespace:** Functions and classes are members of the `exports` object, not direct window globals.
- **Protocol:** ES6 Classes. `AstroTime` and `Observer` **MUST** be invoked with `new`.

## 2. The "Secret Decoder Ring" (Verified Signatures)
- `new Observer(lat, lon, height)`: Constructor for observer location.
- `MakeTime(date)`: Factory function returning an `AstroTime` object.
- `Equator(body, time, observer, aberration, nutation)`: Returns `{ra, dec, dist}`.
- `Horizon(time, observer, ra, dec, refraction)`: Returns `{azimuth, altitude}`.
  - **CRITICAL:** `refraction` MUST be the string `"normal"` or `"none"`. Integers or nulls crash the validator.
- `Illumination(body, time)`: Returns `{phase, phase_angle, helio_dist, mag_dist}`.
- `VisualMagnitude(body, time)`: High-level wrapper for planetary magnitude.
  - **CRITICAL:** Crashes on `"Sun"` and `"Moon"`. Handle with hardcoded constants or `MoonMagnitude`.
- `SaturnMagnitude(pa, hd, md, tilt, time)`: Specialized for Saturn's rings.
- `Body`: An Enum object. Access via `exports.Body.Jupiter` etc. Use of strings (e.g., "Jupiter") in physical calculations often results in `NaN` or `0.0`.

## 3. Death Spiral Post-Mortem (Avoid These)
1. **Scope Leak:** Calling `VisualMagnitude` without the `exports` prefix when the shim is active.
2. **Context Decay:** Passing strings to `Illumination` resulted in `NaN` magnitudes because physical distances were not calculated.
3. **Temporal Dead Zone:** The 400kb file takes ~100-200ms to parse. Logic must be wrapped in a retry loop checking for `window.exports.MakeTime`.
4. **Incorrect Mapping:** Using `VisualMagnitude(body, pa, hd, md)` (4 args) failed because the library expects `(body, time)`.

## 4. Current Task Status
- **Task 1 (Reconstruction):** Table renders RA, DEC, AZ, ALT successfully. MAG and PHASE are currently failing (0.0/NaN) due to improper `Body` enum usage and `Illumination` object property access.
- **Task 2-N (Expansion):** Planned additions: Rise/Set times (`SearchRiseSet`), Transits (`SearchTransit`), and Conjunctions (`Pair`).

## 5. Required Context for Next Agent
The replacement agent MUST request:
1. `head -n 200 static/js/astronomy.js` to verify the `exports` list.
2. `console.log(Object.keys(window.exports))` output from the user's browser to confirm available namespace.
3. A `JSON.stringify` dump of the `Illumination` object for any body to confirm property names (e.g., `phase` vs `phase_fraction`).

[CANARY: NEBULA] | [STATUS: RECOVERY_READY] | [V: 0.19.0]

