cat > HANDOFF.md << 'EOF'
# NBAS Site Handoff — v0.20.0

## Branch
`solsys4` on `nbasastro` Hugo site

## What's Done
- Jupiter globe: working, calibrated MAP_LONGITUDE_OFFSET=317.4, no animation
- Mars globe: working, camera-based latitude, MAP_LONGITUDE_OFFSET needs calibration
- SSD sidebar widget: live, uses window.SolarSystem, shows objects above horizon
- astronomia.js loaded globally in baseof_footer.html
- Solar System Dashboard at /solar-system-dashboard/

## Next Tasks
1. SSD HTML refactor (layout/styling unification)
2. Sidebar widgets: APOD, ISS flyovers, better weather, Meteoblue seeing
3. Documentation for article contributors (4 paths)
4. Social networking toggle to enable
5. V1.0.0 push

## Key Files
- layouts/shortcodes/sso-table.html — main SSD (711 lines)
- assets/js/jupiter-globe.js — Jupiter renderer
- assets/js/mars-globe.js — Mars renderer  
- assets/js/sso.js — all astronomy math
- layouts/partials/ssd-widget.html — sidebar widget
- layouts/partials/baseof_sidebar_public.html — sidebar
- layouts/partials/baseof_footer.html — global scripts
EOF
