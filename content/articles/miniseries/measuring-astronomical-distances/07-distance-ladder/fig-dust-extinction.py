"""Trumpler's test with modern data: dimming by dust vs distance for open clusters.
Data: Cantat-Gaudin et al. 2020, A&A 640, A1 (VizieR J/A+A/640/A1, table1): 1,867 clusters
with neural-network extinction AVNN (mag) and distance DistPc. Gold line: median AVNN in
distance bins. Blue dashed: 0.7 mag per kpc, Trumpler's 1930 average (arXiv 1406.6073).
"""
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from nbas_style import use, save
c = use()
t = pd.read_csv("cantat_table1.csv").dropna(subset=["AVNN", "DistPc"])
t["d"] = t.DistPc/1000
fig, ax = plt.subplots(figsize=(7.2, 3.9))
fig.subplots_adjust(left=0.09, right=0.97, top=0.95, bottom=0.14)
ax.scatter(t.d, t.AVNN, s=5, color=c["muted"], alpha=0.5, lw=0)
edges = np.array([0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0])
mid, med = [], []
for lo, hi in zip(edges[:-1], edges[1:]):
    s = t[(t.d >= lo) & (t.d < hi)]
    if len(s) >= 15:
        mid.append(s.d.median()); med.append(s.AVNN.median())
ax.plot(mid, med, "o-", color=c["a"], lw=2.2, ms=5, label="median of the clusters at that distance")
x = np.linspace(0, 6, 10)
ax.plot(x, 0.7*x, "--", color=c["b"], lw=1.6, label="Trumpler 1930: about 0.7 magnitudes per kiloparsec")
for name, lab, dx, dy in [("Melotte_22", "Pleiades", 0.15, 0.35), ("NGC_2168", "M35", 0.1, -0.45),
                          ("NGC_2158", "NGC 2158", 0.15, 0.4)]:
    r = t[t.Cluster == name].iloc[0]
    ax.plot(r.d, r.AVNN, "o", ms=7, mfc="none", mec=c["strong"], mew=1.3)
    ax.annotate(lab, xy=(r.d, r.AVNN), xytext=(r.d + dx, r.AVNN + dy), color=c["strong"],
                fontsize=9.5, arrowprops=dict(arrowstyle="-", color=c["strong"], lw=0.7))
ax.set_xlim(0, 6); ax.set_ylim(0, 5)
ax.set_xlabel("Distance (kiloparsecs)")
ax.set_ylabel("Dimming by dust (magnitudes)")
ax.grid(True, alpha=0.6)
ax.legend(loc="upper left", frameon=False, fontsize=9.5)
save(fig, "fig-dust-extinction")
