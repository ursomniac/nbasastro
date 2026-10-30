"""Finder chart for delta Cephei, after the style of the AAVSO educational chart (our own data
and drawing). Stars from the HYG database v4.1 (astronexus, CC BY-SA 4.0; V magnitudes from
Hipparcos-era catalogs). Stereographic projection, north up, east left.
Comparison sequence (V, rounded to 0.1, shown x10 without decimal point, AAVSO convention):
  zeta Cep 3.39 -> 34, iota Cep 3.50 -> 35, eps Cep 4.18 -> 42, nu Cep 4.25 -> 43 (tiny-amplitude
  variable, 4.23-4.28), lambda Cep 5.05 -> 50.
delta Cep range 3.5-4.4 (V; GCVS/SEDS 3.48-4.37). mu Cep marked as a variable (do not use).
"""
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from nbas_style import use, save
c = use()
d = pd.read_csv("cep_field.csv")
ra0, de0 = np.radians(22.4*15), np.radians(68.0)
def proj(ra_h, dec):
    a, dd = np.radians(np.asarray(ra_h)*15), np.radians(np.asarray(dec))
    k = 2/(1 + np.sin(de0)*np.sin(dd) + np.cos(de0)*np.cos(dd)*np.cos(a - ra0))
    x = k*np.cos(dd)*np.sin(a - ra0)
    y = k*(np.cos(de0)*np.sin(dd) - np.sin(de0)*np.cos(dd)*np.cos(a - ra0))
    return -np.degrees(x), np.degrees(y)       # east left
fig, ax = plt.subplots(figsize=(5.0, 6.6))
fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
X, Y = proj(d.ra, d.dec)
d["x"], d["y"] = X, Y
def star(key):
    r = d[d.key == key].iloc[0]; return r.x, r.y
# stick figure
for a, b in [("Alp", "Bet"), ("Bet", "Gam"), ("Gam", "Iot"), ("Iot", "Bet"), ("Iot", "Zet"), ("Zet", "Alp")]:
    (x1, y1), (x2, y2) = star(a), star(b)
    ax.plot([x1, x2], [y1, y2], color=c["muted"], lw=0.9, zorder=1)
# stars
sz = lambda m: (6.2 - m)**1.9 * 3.2
for _, r in d.iterrows():
    if r.key == "Del":
        continue
    ax.scatter(r.x, r.y, s=sz(r.mag), color=c["strong"], lw=0, zorder=3)
# delta Cep: variable symbol
dx, dy = star("Del")
ax.scatter(dx, dy, s=70, facecolor=c["bg"], edgecolor=c["a"], lw=1.6, zorder=4)
for ang in (0, 90, 180, 270):
    t = np.radians(ang); ax.plot([dx + 0.32*np.cos(t), dx + 0.6*np.cos(t)],
                                 [dy + 0.32*np.sin(t), dy + 0.6*np.sin(t)], color=c["a"], lw=1.4, zorder=4)
ax.text(dx - 0.75, dy - 0.1, "δ", color=c["a"], fontsize=15, ha="right", va="center", fontweight="bold")
ax.text(dx, dy - 1.0, "3.5–4.4", color=c["a"], fontsize=9.5, ha="center", va="center")
# Greek labels (offsets in plot degrees; x is flipped later so +x = left on the page)
greek = {"Alp": ("α", (-0.75, 0.3)), "Bet": ("β", (0.75, 0.3)), "Gam": ("γ", (-0.75, 0.3)),
         "Iot": ("ι", (-0.7, 0.2)), "Zet": ("ζ", (-0.75, 0.05)), "Eps": ("ε", (-0.6, -0.5)),
         "Mu": ("μ", (0.65, 0.0)), "Lam": ("λ", (0.6, 0.45)), "Nu": ("ν", (0.6, 0.35)),
         "Xi": ("ξ", (0.6, 0.0)), "Eta": ("η", (0.65, 0.0))}
for k, (g, (ox, oy)) in greek.items():
    x, y = star(k)
    ax.text(x + ox, y + oy, g, color=c["strong"], fontsize=13, ha="center", va="center")
# comparison magnitudes (x10, AAVSO style), underlined with a short rule
comps = {"Zet": ("34", (0.85, -0.1)), "Iot": ("35", (0.8, -0.35)), "Eps": ("42", (0.75, -0.75)),
         "Nu": ("43", (0.7, -0.55)), "Lam": ("50", (1.4, 0.45))}
for k, (lab, (ox, oy)) in comps.items():
    x, y = star(k)
    ax.text(x + ox, y + oy, lab, color=c["b"], fontsize=10.5, ha="center", va="center")
ax.text(star("Mu")[0] + 0.3, star("Mu")[1] - 0.75, "variable", color=c["muted"], fontsize=9.5,
        ha="center", va="center")
# scale bar and compass
xs, ys = 9.5, -11.3
ax.plot([xs, xs - 5], [ys, ys], color=c["ink"], lw=1.2)
for xx in (xs, xs - 5): ax.plot([xx, xx], [ys - 0.2, ys + 0.2], color=c["ink"], lw=1.2)
ax.text(xs - 2.5, ys - 0.55, "5°", color=c["ink"], fontsize=10, ha="center", va="top")
ax.annotate("", xy=(8.8, 14.2), xytext=(8.8, 12.4),
            arrowprops=dict(arrowstyle="-|>", color=c["ink"], lw=1.0))
ax.text(9.4, 14.0, "N", color=c["ink"], fontsize=10, ha="left", va="center")
ax.annotate("", xy=(7.0, 12.4), xytext=(8.8, 12.4),
            arrowprops=dict(arrowstyle="-|>", color=c["ink"], lw=1.0))
ax.text(6.6, 12.4, "E", color=c["ink"], fontsize=10, ha="right", va="center")
ax.text(-10.3, 14.8, "Cepheus", color=c["strong"], fontsize=12, ha="left", va="top")
ax.text(-10.3, 13.8, "Comparison magnitudes ×10\n(42 = magnitude 4.2)", color=c["b"],
        fontsize=9.5, ha="left", va="top")
ax.text(-10.3, -12.2, "Stars to magnitude 5.5", color=c["muted"], fontsize=9.5, ha="left", va="bottom")
ax.set_aspect("equal"); ax.axis("off")
ax.set_xlim(-10.5, 10.5)       # proj() already puts east on the left
ax.set_ylim(-12.5, 15.0)
save(fig, "fig-delta-cep-chart")
