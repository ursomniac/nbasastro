ALGORITHM DrawLunarPhase(percentage, Radius):
    // 1. Standardize phase P to 0.0 - 1.0 range
    Set P = percentage MOD 1.0

    // 2. Calculate Terminator X-position (Sweep from Right to Left)
    // This happens twice: once for waxing, once for waning.
    IF P <= 0.5 THEN
        Set W = cos(PI * (P / 0.5))
    ELSE
        Set W = cos(PI * ((P - 0.5) / 0.5))
    END IF

    // 3. Process every pixel (x, y) in the image
    FOR each pixel (x, y) in MoonDisk:
        Set dx = x - center_x
        Set dy = y - center_y

        // Use the equation of an ellipse to find the terminator line
        Set x_term = W * SQRT(Radius^2 - dy^2)

        IF P <= 0.5 THEN
            // WAXING: Growing from right edge. Light everything to the RIGHT.
            IF dx > x_term THEN Draw "WHITE" ELSE Draw "BLACK"
        ELSE
            // WANING: Receding to left edge. Light everything to the LEFT.
            IF dx < x_term THEN Draw "WHITE" ELSE Draw "BLACK"
        END IF
    END FOR
END ALGORITHM

