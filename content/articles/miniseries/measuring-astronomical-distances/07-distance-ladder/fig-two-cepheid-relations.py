"""Schematic: classical vs Type II Cepheid period-luminosity relations.
Only the offset is quantitative: ~1.5 mag (Baade 1952; IAU Trans. VIII, 397), which is a
factor 10**(1.5/5) = 2.0 in distance. Lines drawn parallel for clarity; slopes, zero points
and period ranges are NOT to scale.
"""
import numpy as np
import matplotlib.pyplot as plt
from nbas_style import use, save
c = use()
fig, ax = plt.subplots(figsize=(5.0, 3.9))
fig.subplots_adjust(left=0.14, right=0.97, top=0.96, bottom=0.14)
x = np.linspace(0.0, 1.6, 50)
slope = 2.4
classical = -slope * x          # magnitude units, schematic
typeII = classical + 1.5
ax.plot(x, classical, color=c["a"], lw=2.4)
ax.plot(x, typeII, color=c["b"], lw=2.4, ls="--")
ax.text(0.05, -2.55, "Classical Cepheids\n(young, in galaxy disks)",
        color=c["a"], fontsize=10, ha="left", va="center")
ax.text(1.55, -0.55, "Type II Cepheids\n(old stars)",
        color=c["b"], fontsize=10, ha="right", va="center")
xa = 0.95
ax.annotate("", xy=(xa, -slope*xa), xytext=(xa, -slope*xa + 1.5),
            arrowprops=dict(arrowstyle="<->", color=c["strong"], lw=1.3))
ax.annotate("1.5 magnitudes\n= 2\u00d7 in distance", xy=(xa - 0.01, -slope*xa + 0.75),
            xytext=(0.05, 2.1), color=c["strong"], fontsize=10, va="center", ha="left",
            arrowprops=dict(arrowstyle="-", color=c["muted"], lw=0.8))
ax.set_ylim(2.6, -4.3)
ax.set_xticks([])
ax.set_yticks([]); 
ax.set_xlabel("Pulsation period (longer →)")
ax.set_ylabel("True brightness (brighter ↑)")
ax.text(1.58, 2.1, "Schematic: only the gap\nbetween the lines is to scale",
        color=c["muted"], fontsize=9.5, ha="right", va="center")
save(fig, "fig-two-cepheid-relations")
