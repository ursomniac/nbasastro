"""Pleiades distance measurements vs. publication year.
Values (pc, ±1σ) from the primary abstracts where available, else the Melis et al. 2012
compilation (IAU Symp., 'Toward a VLBI resolution', Table 1, updated from Soderblom et al. 2005):
  van Leeuwen 1999, Hipparcos                    118.3 ± 3.5   (Melis 2012 table)
  Pinsonneault et al. 1998, main-sequence fit    131.9 ± 2.4   (Melis 2012 table)
  Gatewood et al. 2000, Allegheny parallaxes     130.9 ± 7.4   (Melis 2012 table)
  Pan, Shao & Kulkarni 2004, Atlas orbit         135.0 ± 2.0   (Melis 2012 table)
  Munari et al. 2004, eclipsing binary HD 23642  132 ± 2       (A&A 418, L31 abstract)
  Soderblom et al. 2005, HST FGS (3 stars)       134.6 ± 3.1   (AJ 129, 1616 abstract)
  van Leeuwen 2009, Hipparcos new reduction      120.2 ± 1.9   (A&A 497, 209; via Melis 2014)
  Melis et al. 2014, VLBI                        136.2 ± 1.2   (Science 345, 1029 abstract)
  Cantat-Gaudin+ 2020, Gaia DR2 parallaxes       136.1         (our median of 952 members' parallaxes,
                                                               J/A+A/640/A1/nodup; statistical error ~0.1 pc,
                                                               smaller than the DR2 calibration offset ~0.5 pc;
                                                               plotted without an error bar)
"""
from nbas_style import use, save
import matplotlib.pyplot as plt

c = use()
hip = [(1999, 118.3, 3.5, "Hipparcos\n1999"), (2009, 120.2, 1.9, "Hipparcos\nnew reduction 2009")]
oth = [(1998, 131.9, 2.4, "main-sequence\nfitting"),
       (2000, 130.9, 7.4, "ground-based\nparallaxes"),
       (2003.8, 135.0, 2.0, "orbit of\nAtlas"),
       (2004.2, 132.0, 2.0, "eclipsing\nbinary"),
       (2005, 134.6, 3.1, "Hubble\nparallaxes"),
       (2014, 136.2, 1.2, "radio (VLBI)\nparallaxes"),
       (2020, 136.1, 0.0, "Gaia")]

fig, ax = plt.subplots(figsize=(7.2, 3.9))
fig.subplots_adjust(left=0.09, right=0.98, top=0.95, bottom=0.13)
ax.grid(axis="y")
for x, y, e, _ in oth:
    ax.errorbar(x, y, yerr=e, fmt="o", ms=6, color=c["b"], ecolor=c["b"], elinewidth=1.6, capsize=3)
for x, y, e, _ in hip:
    ax.errorbar(x, y, yerr=e, fmt="s", ms=6.5, color=c["a"], ecolor=c["a"], elinewidth=1.6, capsize=3)

def lab(x, y, s, dx=0, dy=0, ha="center", va="bottom", col=None):
    ax.annotate(s, (x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va,
                fontsize=9.5, color=col or c["ink"], linespacing=1.05)

lab(1999, 118.3-3.5, "Hipparcos\n1999", dy=-4, va="top", col=c["a"])
lab(2009, 120.2-1.9, "Hipparcos, new\nreduction 2009", dy=-4, va="top", col=c["a"])
lab(1998, 131.9-2.4, "main-sequence\nfitting", dx=-2, dy=-4, va="top")
lab(2000, 130.9+7.4, "ground-based\nparallaxes", dy=3)
lab(2003.8, 135.0+2.0, "orbit of\nAtlas", dx=-6, dy=3, ha="right")
lab(2004.2, 132.0-2.0, "eclipsing\nbinary", dy=-4, va="top")
lab(2005, 134.6+3.1, "Hubble\nparallaxes", dx=6, dy=3, ha="left")
lab(2014, 136.2+1.2, "radio (VLBI)\nparallaxes", dy=4)
lab(2020, 136.1, "Gaia", dy=8)

ax.set_xlim(1995.5, 2021.5)
ax.set_ylim(110, 146)
ax.set_xlabel("Year published")
ax.set_ylabel("Distance (parsecs)")
ax.text(0.015, 0.97, "■ Hipparcos   ● other methods", transform=ax.transAxes, va="top",
        fontsize=9.5, color=c["muted"])
save(fig, "fig-pleiades-distance-history")
