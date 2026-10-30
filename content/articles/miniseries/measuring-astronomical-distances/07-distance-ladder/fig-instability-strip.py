"""Where the pulsating stars live on the H-R diagram.
Background: Hipparcos stars within 200 pc (HYG v4.1, CC BY-SA 4.0); temperature from B-V
(Ballesteros 2012 formula), luminosity from HYG (V band, no bolometric correction: approximate).
Lines of constant radius are exact: L = R^2 (T / 5772 K)^4.
Instability strip: SCHEMATIC band, drawn approximately (warm edge ~7,500 K, cool edge ~5,800 K
at Cepheid luminosities, both slanting cooler with brightness); not a fitted boundary.
delta Cep: L ~1,900 Lsun (Gallenne et al. 2021, via Wikipedia); T from L and mean radius 43 Rsun
-> ~5,800 K (computed). RR Lyr: L 49 Lsun, T 6,125 K (Wikipedia). Sun: 1 Lsun, 5,772 K.
"""
import numpy as np, pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from nbas_style import use, save
c = use()
b = pd.read_csv("hr_bg.csv")
fig, ax = plt.subplots(figsize=(5.0, 5.2))
fig.subplots_adjust(left=0.16, right=0.96, top=0.97, bottom=0.11)
ax.set_xscale("log"); ax.set_yscale("log")
ax.scatter(b.teff, b.lum, s=2, color=c["muted"], alpha=0.35, lw=0, zorder=1)
T = np.logspace(np.log10(2500), np.log10(40000), 100)
for R, lab in [(0.1, "0.1"), (1, "1"), (10, "10"), (100, "100")]:
    L = R**2*(T/5772)**4
    ax.plot(T, L, color=c["rule"], lw=1, ls="--", zorder=0)
    i = np.argmin(abs(L - 3e-4*10**(np.log10(R)*2.4)))
    xt = 3100 if R < 50 else 3300
    yt = R**2*(xt/5772)**4
    ax.text(xt*0.97, yt, f"{lab}", color=c["muted"], fontsize=9.5, ha="right", va="bottom")
# schematic instability strip
strip = Polygon([(7600, 10), (6600, 10), (5200, 3e4), (6200, 3e4)], closed=True,
                fc=c["b"], ec="none", alpha=0.30, zorder=2)
ax.add_patch(strip)
ax.text(5050, 3500, "instability strip", color=c["b"], fontsize=10, ha="center", va="center",
        rotation=78, zorder=6)
ax.annotate("Cepheids (star: δ Cephei)", xy=(5800, 1900), xytext=(15000, 9e3), color=c["strong"], fontsize=10.5,
            ha="center", arrowprops=dict(arrowstyle="-", color=c["strong"], lw=0.8))
ax.annotate("RR Lyrae stars (star: RR Lyrae)", xy=(6125, 49), xytext=(15000, 400), color=c["strong"], fontsize=10.5,
            ha="center", arrowprops=dict(arrowstyle="-", color=c["strong"], lw=0.8))
for name, Tm, Lm in [("δ Cephei", 5800, 1900), ("RR Lyrae", 6125, 49), ("the Sun", 5772, 1.0)]:
    ax.plot(Tm, Lm, marker="*", ms=12, color=c["a"], mec=c["bg"], mew=0.6, zorder=5)
ax.text(5772*0.88, 1.0, "the Sun", color=c["a"], fontsize=10, ha="left", va="center", zorder=6)
ax.text(9500, 0.6, "main sequence", color=c["strong"], fontsize=10, rotation=-42, ha="center")
ax.set_xlim(30000, 2800); ax.set_ylim(1e-4, 1e5)
ax.set_xticks([30000, 10000, 6000, 3000]); ax.set_xticklabels(["30,000", "10,000", "6,000", "3,000"])
ax.xaxis.set_minor_formatter(plt.NullFormatter())
ax.set_yticks([1e-4, 1e-2, 1, 1e2, 1e4]); ax.set_yticklabels(["0.0001", "0.01", "1", "100", "10,000"])
ax.set_xlabel("Surface temperature (K)")
ax.set_ylabel("Luminosity (Sun = 1)")
ax.text(29000, 6e4, "Dashed lines: radius in Suns\nInstability strip: schematic", color=c["muted"], fontsize=9.5, va="top")
save(fig, "fig-instability-strip")
