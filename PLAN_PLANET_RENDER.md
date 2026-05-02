# Implementation Plan: Dynamic Planetary Shortcode for Hugo

## 1. Goal
Create a Hugo shortcode that uses **astronomia** for astronomical calculations and **three.js** for 3D rendering to display Jupiter and Mars at their current rotational phases.

---

## 2. Asset Preparation
Instead of multiple images, we use a single high-resolution texture map for each planet.

*   **Projection Type:** Equirectangular (2:1 aspect ratio).
*   **Sources:** 
    *   **Jupiter:** NASA Juno/Cassini merged maps.
    *   **Mars:** Viking Colorized Global Mosaic.
*   **Location:** Store in `assets/images/planets/`.

---

## 3. Data Logic (Astronomia)
The JavaScript logic will handle the real-time positioning:

1.  **Time Input:** Convert current system time to Julian Date (JD).
2.  **Jupiter Rotation:** Use System II longitude to track the **Great Red Spot**.
3.  **Mars Rotation:** Use standard physical ephemeris to find the central meridian.
4.  **Output:** A single degree value ($0^\circ$ to $359^\circ$) representing the longitude facing Earth.

---

## 4. Visual Rendering (Three.js)
Based on the WebGL examples, the rendering pipeline will:

*   **Geometry:** Create a `SphereGeometry`.
*   **Material:** Apply a `MeshStandardMaterial` using the planet texture.
*   **Lighting:** Add a `DirectionalLight` to simulate sunlight and an `AmbientLight` for visibility.
*   **Rotation:** Set `sphere.rotation.y` to the value calculated by astronomia.
    *   *Note:* Remember to convert degrees to radians: $rad = deg \times (\pi / 180)$.

---

## 5. Hugo Integration
*   **Shortcode:** `{{< planet name="jupiter" >}}`.
*   **Asset Pipeline:** Use Hugo Pipes (`js.Build`) to bundle the libraries.
*   **Container:** A responsive `<div>` that scales the WebGL canvas to fit your page layout.

---

## 6. Known Constraints
*   **GRS Drift:** Jupiter's Red Spot drifts over time; include a configurable offset variable.
*   **Performance:** Use `requestAnimationFrame` for smooth rendering, but ensure it pauses when the planet is off-screen to save resources.
