"""Color-magnitude (H-R) diagram of the Hyades, from Hipparcos.
Members: 132 Hipparcos stars within 16 deg of the cluster center, 30-65 pc, whose proper motions
match the cluster's mean space motion (from the 110 radial-velocity members used in
fig-moving-cluster) to within 3 km/s or 8 mas/yr. Absolute magnitudes from each star's own
Hipparcos parallax. Background: all Hipparcos stars within 25 pc (1,515). Data: HYG v4.1
(CC BY-SA 4.0). The Hipparcos catalog stops near V = 12, so the faint end of the cluster's
main sequence (and its white dwarfs) is missing here.
"""
import pandas as pd
import matplotlib.pyplot as plt
from nbas_style import use, save
c = use()
h = pd.read_csv("hyades_cmd.csv"); f = pd.read_csv("field25.csv")
fig, ax = plt.subplots(figsize=(5.0, 5.4))
fig.subplots_adjust(left=0.15, right=0.97, top=0.97, bottom=0.11)
ax.scatter(f.ci, f.absmag, s=5, color=c["muted"], alpha=0.55, lw=0, label="stars within 25 pc (all ages)")
ax.scatter(h.ci, h.absmag, s=16, color=c["a"], lw=0, label="Hyades members")
ax.plot(0.65, 4.83, marker="o", ms=9, mfc="none", mec=c["b"], mew=1.6)
ax.annotate("the Sun", xy=(0.62, 4.95), xytext=(1.05, 3.2), color=c["b"], fontsize=10,
            va="center", arrowprops=dict(arrowstyle="-", color=c["b"], lw=0.8))
ax.annotate("four red giants:\nγ, δ¹, ε and θ¹ Tauri", xy=(1.0, 0.35), xytext=(1.1, -0.9),
            color=c["strong"], fontsize=9.5, va="center",
            arrowprops=dict(arrowstyle="-", color=c["strong"], lw=0.8))
ax.text(0.2, 7.9, "main sequence", color=c["a"], fontsize=10.5, rotation=-52, ha="center")
ax.set_xlim(-0.25, 1.75); ax.set_ylim(12, -1.8)
ax.set_xlabel("Color (B − V): bluer ←   → redder")
ax.set_ylabel("True brightness (absolute magnitude)")
ax.grid(True, alpha=0.6)
ax.legend(loc="lower left", frameon=False, fontsize=9.5)
save(fig, "fig-hyades-cmd")
