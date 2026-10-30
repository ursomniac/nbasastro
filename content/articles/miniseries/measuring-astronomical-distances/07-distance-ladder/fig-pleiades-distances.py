"""Pleiades distance by method. Values (pc):
pre-Hipparcos MS fitting ~132 (Percival et al. 2005, astro-ph/0409362: (m-M)0 ~5.6)
Hipparcos 1997 catalog, van Leeuwen 1999: 118.3 +/- 3.5 (Galli et al. 2017, arXiv 1610.05641)
Hipparcos new reduction, van Leeuwen 2009 (2007 reduction): 120.2 +/- 1.5 (Melis et al. 2014)
HST FGS, Soderblom et al. 2005: 134.6 +/- 3.1 (Galli et al. 2017)
VLBI, Melis et al. 2014: 136.2 +/- 1.2
Gaia DR2, Gaia Collaboration 2018: parallax 7.364 mas -> 135.8 (no error bar drawn)
"""
import matplotlib.pyplot as plt
from nbas_style import use, save
c = use()
rows = [  # label, year label, value, err, family
    ("Main-sequence fitting", "before 1997", 132.0, None, "ms"),
    ("Hipparcos", "1997 catalog", 118.3, 3.5, "hip"),
    ("Hipparcos", "2009, new reduction", 120.2, 1.5, "hip"),
    ("Hubble parallaxes", "2005", 134.6, 3.1, "other"),
    ("Radio VLBI parallaxes", "2014", 136.2, 1.2, "other"),
    ("Gaia DR2 parallaxes", "2018", 135.8, None, "other"),
]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
fig.subplots_adjust(left=0.36, right=0.97, top=0.95, bottom=0.17)
ax.axvspan(132, 138, color=c["rule"], alpha=0.45, lw=0)
for i, (lab, yr, v, e, fam) in enumerate(rows):
    y = len(rows) - 1 - i
    col = c["a"] if fam == "hip" else c["b"]
    mk = "s" if fam == "hip" else ("D" if fam == "ms" else "o")
    if e:
        ax.errorbar(v, y, xerr=e, fmt=mk, color=col, ms=7, capsize=3, lw=1.6)
    else:
        ax.plot(v, y, mk, color=col, ms=7)
    ax.text(v + (e or 0) + 0.8, y, f"{v:.1f}", va="center", fontsize=9.5, color=c["ink"])
    ax.text(109.6, y, lab, ha="right", va="center", color=c["strong"], fontsize=10.5,
            transform=ax.transData, clip_on=False)
    ax.text(109.6, y - 0.32, yr, ha="right", va="center", color=c["muted"], fontsize=9.5,
            transform=ax.transData, clip_on=False)
ax.set_xlim(110, 142)
ax.set_ylim(-0.7, len(rows) - 0.4)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.set_xlabel("Distance to the Pleiades (parsecs)")
ax.text(135, len(rows) - 0.55, "the methods that agree", ha="center", va="center",
        fontsize=9.5, color=c["muted"])
save(fig, "fig-pleiades-distances")
