# MISSION_PLAN: Planetary Dashboard & Visualization
**VERSION:** 1.0.0  
**STATUS:** ACTIVE  
**ROOT:** https://nbasastro.org + /

---

## PHASE 1: CORE DATA STABILIZATION (COMPLETED)
* [x] **Engine:** Integration of `astronomy-engine` (Don Cross).
* [x] **Observer:** Geolocation for Adams, MA (42.7, -73.1).
* [x] **Ephemeris:** RA, DEC, AZ, ALT, MAG, and Phase for all major bodies.
* [x] **Events:** Rise/Set/Transit (Sidereal calculation bypass).
* [x] **Jupiter System:** Galilean moon positions in Jupiter Radii (Scaled).

---

## PHASE 2: SYSTEM EXPANSION (V0.20.0)
*Target: Integration of **Astronomia** library for specialized physical parameters.*

* [ ]  **Jupiter GRS:** 
    * Implement System II Longitude calculation.
    * Track GRS drift (Current ref: ~375°).
    * Visibility flag: `TRUE` if GRS is within ±90° of Central Meridian.
* [*] **Saturn’s Rings:**
    * Calculate **B** (tilt relative to Earth).
    * Calculate **P** (Position angle of the North pole).
* [*] **Inner Planet Phases:** 
    * Detailed illuminated fraction and "appearance" (e.g., Crescent vs. Gibbous).
* [ ] **Mars/Saturn/Uranus Moons:**
    * Expanding the moon dashboard to include Deimos/Phobos and Titan.

---

## PHASE 3: DYNAMIC ASSET PIPELINE (V0.30.0)
*Target: Connecting math to visual assets.*

* **Asset Prep:**
    * [*] Source high-res NASA planetary textures (PNG/Transparent).
    * Source moon "sprite" icons. ???
* **Canvas Layering:**
    * Create an `AstroCanvas` component.
    * Layer 1: Static star field.
    * Layer 2: Scaled planet image.
    * Layer 3: Moon coordinate overlay.
* **Physical Orientation:**
    * Apply `rotate()` transforms to the Canvas based on calculated Position Angle (P) so the dashboard matches the eyepiece view.
    * [ ] Moon
    * [ ] Mars
    * [ ] Jupiter
---

## PHASE 4: THE TELESCOPE VIEW (V1.0.0)
*Target: Interactive visual rendering.*

* **Simulation Mode:**
    * User-defined magnification (FOV) settings.
    * Inversion toggle (Refractor vs. Newtonian/SCT view).
* **Time Scrubbing:**
    * Allow users to slide time forward/backward to watch moon transits and ring shadow movements.
* **Shadow Transits:**
    * Logic to detect and render shadows cast by moons onto the planetary disk.

---

## CRITICAL PROJECT CONSTRAINTS
1. **Library Hybridization:** Use `astronomy-engine` for speed/positions and `astronomia` for physical geometry.
2. **Statelessness:** Ensure calculations remain client-side (JS) for real-time responsiveness.
3. **The Plus Rule:** All asset paths MUST follow the `domain + /path` protocol to avoid Hugo truncation.

[CANARY: NEBULA] | [STATUS: ACTIVE] | [V: 0.19.0]
