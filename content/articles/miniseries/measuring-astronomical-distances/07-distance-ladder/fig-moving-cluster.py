"""The Hyades' proper motions converge on one point of the sky.
Data: HYG database v4.1 (astronexus, CC BY-SA 4.0), Hipparcos-based positions, proper motions,
distances and radial velocities. Members: stars within 15 deg of the cluster center, 30-70 pc,
with a radial velocity, whose space velocity is within 4 km/s of the sample median
(110 stars). Convergent point = direction of the members' mean space velocity:
RA 6h30.0m, Dec +6.8 deg (computed here). Arrows: proper motion over 50,000 years.
Gnomonic projection: great circles (the stars' paths on the sky) are straight lines.
"""
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from nbas_style import use, save
c = use()
m = pd.read_csv("hyades_members.csv")
V = m[["vx", "vy", "vz"]].values.mean(axis=0)
u = V / np.linalg.norm(V)
cp_ra = np.degrees(np.arctan2(u[1], u[0])) % 360
cp_de = np.degrees(np.arcsin(u[2]))
ra0, de0 = np.radians(81.0), np.radians(12.0)          # projection center
def gnom(ra_deg, de_deg):
    a, d = np.radians(ra_deg), np.radians(de_deg)
    cosc = np.sin(de0)*np.sin(d) + np.cos(de0)*np.cos(d)*np.cos(a - ra0)
    x = np.cos(d)*np.sin(a - ra0) / cosc
    y = (np.cos(de0)*np.sin(d) - np.sin(de0)*np.cos(d)*np.cos(a - ra0)) / cosc
    return -np.degrees(x), np.degrees(y)               # east to the left, as on the sky
ra = m.ra.values * 15; de = m.dec.values
T = 50000.0
ra2 = ra + m.pmra.values/1000/3600*T/np.cos(np.radians(de))
de2 = de + m.pmdec.values/1000/3600*T
x1, y1 = gnom(ra, de); x2, y2 = gnom(ra2, de2)
cx, cy = gnom(cp_ra, cp_de)
fig, ax = plt.subplots(figsize=(7.2, 4.4))
fig.subplots_adjust(left=0.03, right=0.97, top=0.97, bottom=0.03)
# extend each star's OWN direction of motion (straight in this projection); the lines are
# not forced through the convergent point, they meet there because the motions are parallel
for i in range(len(m)):
    dx, dy = x2[i] - x1[i], y2[i] - y1[i]
    k = (cx - x1[i]) / dx                      # run each ray as far as the convergent point's x
    ax.plot([x1[i], x1[i] + k*dx], [y1[i], y1[i] + k*dy], color=c["rule"], lw=0.6, zorder=1)
size = np.clip(12 - 1.6*(m.mag.values - 3.4), 1.5, 12)
ax.scatter(x1, y1, s=size**1.4, color=c["strong"], zorder=3, lw=0)
for i in range(len(m)):
    ax.annotate("", xy=(x2[i], y2[i]), xytext=(x1[i], y1[i]),
                arrowprops=dict(arrowstyle="-|>", color=c["a"], lw=1.0,
                                mutation_scale=7, shrinkA=0, shrinkB=0), zorder=2)
ax.plot(cx, cy, marker="X", ms=12, color=c["b"], zorder=4)
ax.text(cx, cy - 1.3, "Convergent point", color=c["b"], ha="center", va="top", fontsize=10.5)
# reference stars (not members)
x, y = gnom(68.98, 16.51)
ax.plot(x, y, "o", mfc="none", mec=c["b"], ms=9, mew=1.4, zorder=5)
ax.annotate("Aldebaran (foreground,\nnot a member)", xy=(x, y), xytext=(x - 17.0, y + 7.0),
            color=c["b"], fontsize=9.5, ha="left", va="center",
            arrowprops=dict(arrowstyle="-", color=c["b"], lw=0.8))
x, y = gnom(88.79, 7.41)
ax.plot(x, y, "o", mfc="none", mec=c["muted"], ms=8, mew=1.2, zorder=4)
ax.text(x, y + 0.9, "Betelgeuse", color=c["muted"], fontsize=9.5, ha="center", va="bottom")
hx, hy = gnom(66.75, 15.87)
ax.text(hx + 5.5, hy + 8.5, "The Hyades", color=c["strong"], fontsize=12, ha="center")
ax.text(0.02, 0.03, "Arrows: each star's motion over 50,000 years (Hipparcos proper motions)",
        transform=ax.transAxes, color=c["muted"], fontsize=9.5)
ax.set_aspect("equal")
ax.set_xlim(cx - 4, max(x1) + 2)        # gnom() already puts east on the left
ax.set_ylim(min(min(y1), cy) - 4, max(y1) + 3)
ax.axis("off")
save(fig, "fig-moving-cluster")
print("CP", cp_ra/15, cp_de)
