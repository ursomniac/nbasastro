"""Secular parallax in real data: the reflex of the Sun's motion.
Data: Hipparcos stars via HYG v4.1 (CC BY-SA 4.0). Stars are binned in 20-degree cells on the
sky; each arrow is the AVERAGE proper motion of the stars in that cell (cells with >= 8 stars).
One distance shell: 10-40 pc (4,166 stars). (Two shells were tried; the far-shell arrows were
too short to read at this scale.) Arrows show the average drift over
150,000 years. Individual stars move every which way; the average flows away from the solar
apex (RA 18h28m, Dec +30; Wikipedia, Solar apex) toward the antapex.
"""
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from nbas_style import use, save
c = use()
d = pd.read_csv("hip_pm.csv")
T = 150000.0
def sky(ra_deg, dec_deg):
    lon = np.radians(-(((ra_deg + 180) % 360) - 180))   # RA increases to the left
    return lon, np.radians(dec_deg)
fig = plt.figure(figsize=(7.2, 4.3))
ax = fig.add_axes([0.03, 0.10, 0.94, 0.86], projection="aitoff")
ax.grid(True, color=c["rule"], lw=0.5)
ax.set_xticklabels([]); ax.set_yticklabels([])
ax.set_facecolor(c["bg"])
for lo, hi, col, lw in [(10, 40, c["a"], 1.4)]:
    s = d[(d.dist > lo) & (d.dist < hi)]
    step = 20
    for dc in range(-90 + step//2, 90, step):
        band = s[(s.dec >= dc - step/2) & (s.dec < dc + step/2)]
        nra = max(1, int(round(360*np.cos(np.radians(dc))/step)))
        for i in range(nra):
            r0 = i*360/nra
            cell = band[(band.ra*15 >= r0) & (band.ra*15 < r0 + 360/nra)]
            if len(cell) < 8: continue
            ra_c, de_c = r0 + 180/nra, dc
            pa = cell.pmra.mean()/1000/3600*T / np.cos(np.radians(de_c))
            pd_ = cell.pmdec.mean()/1000/3600*T
            x0, y0 = sky(ra_c, de_c); x1, y1 = sky(ra_c + pa, np.clip(de_c + pd_, -89, 89))
            if abs(x1 - x0) > np.pi: continue          # skip arrows that wrap the map edge
            ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                        arrowprops=dict(arrowstyle="-|>", color=col, lw=lw, mutation_scale=7,
                                        shrinkA=0, shrinkB=0))
for name, ra, dec in [("apex", 18*15 + 7, 30), ("antapex", 6*15 + 7, -30)]:
    x, y = sky(ra, dec)
    ax.plot(x, y, marker="X", ms=11, color=c["strong"], mec=c["bg"], zorder=5)
    dy, va = (0.13, "bottom") if name == "apex" else (-0.13, "top")
    ax.text(x, y + dy, "Solar " + name, color=c["strong"], fontsize=10, ha="center",
            va=va, zorder=6)
fig.text(0.05, 0.04, "→  average motion of the stars 10–40 parsecs away, in each patch of sky",
         color=c["a"], fontsize=10)
fig.text(0.97, 0.04, "average drift over 150,000 years", color=c["muted"], fontsize=9.5, ha="right")
save(fig, "fig-secular-parallax")
