"""delta Cephei's size, to scale with the Sun and Mercury's orbit.
Radius 41.2-45.3 solar radii over the pulsation cycle (Wikipedia, citing Bailleul et al. 2026;
angular diameter 1.409-1.55 mas). Mercury's mean orbital radius 0.387 AU = 83.2 solar radii
(1 AU = 215.0 solar radii). All circles to scale.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from nbas_style import use, save
c = use()
fig, ax = plt.subplots(figsize=(3.8, 4.15))
fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
ax.add_patch(Circle((0, 0), 83.2, fill=False, ec=c["muted"], lw=1.0, ls="--"))
ax.add_patch(Circle((0, 0), 45.3, fc=c["a"], ec="none", alpha=0.35))
ax.add_patch(Circle((0, 0), 41.2, fc=c["a"], ec="none", alpha=0.85))
ax.add_patch(Circle((62, -15), 1.0, fc=c["strong"], ec="none"))
ax.annotate("the Sun", xy=(62, -15), xytext=(60, -34), color=c["strong"], fontsize=10,
            ha="center", va="top", arrowprops=dict(arrowstyle="-", color=c["strong"], lw=0.8))
ax.text(0, 4, "δ Cephei", color=c["bg"], fontsize=12, ha="center", va="center", fontweight="bold")
ax.text(0, -8, "41–45 × the Sun's\nradius", color=c["bg"], fontsize=9.5, ha="center", va="center")
ax.text(0, 86, "Mercury's orbit", color=c["muted"], fontsize=9.5, ha="center", va="bottom")
ax.text(0, -88, "Pale ring: how far it swells at its largest", color=c["a"], fontsize=9.5,
        ha="center", va="top")
ax.set_xlim(-92, 92); ax.set_ylim(-104, 96); ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-delta-cep-size")
