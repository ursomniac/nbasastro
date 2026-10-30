"""Landmarks of the lower distance ladder, each with the rung that put it in reach.
Distances (pc): 61 Cyg 3.5 (parsecs-vs-light-years); Hyades 47.5 (Gaia DR2); Pleiades 136
(VLBI 136.2, Gaia DR2 135.8); delta Cep ~260 (HST 2002 ~273; Anderson 2015 244+/-10);
M35 ~860 (~2,800 ly, APOD 2021-05-10); NGC 2158 4,298 (Cantat-Gaudin et al. 2020, table1);
M13 7,400 (A06 table); Galactic center 8,200 (GRAVITY 2019).
"Parallax c. 1900" band: errors ~40 mas (Russell 1910) -> parallax ~ error beyond ~25 pc.
"""
import numpy as np
import matplotlib.pyplot as plt
from nbas_style import use, save
c = use()
L = [  # name, pc, rung, label side (+1 above, -1 below), ly string
    ("61 Cygni", 3.5, "parallax", +1, "11 ly"),
    ("Hyades", 47.5, "moving cluster", -1, "155 ly"),
    ("Pleiades", 136, "main-sequence fitting", +1, "444 ly"),
    ("δ Cephei", 260, "Cepheid calibrator", -1, "~850 ly"),
    ("M35", 860, "main-sequence fitting", +1, "2,800 ly"),
    ("NGC 2158", 4300, "main-sequence fitting", -1, "~14,000 ly"),
    ("M13", 7400, "RR Lyrae", +1, "24,000 ly"),
    ("Galactic center", 8200, "RR Lyrae", -1, "26,700 ly"),
]
fig, ax = plt.subplots(figsize=(7.2, 4.4))
fig.subplots_adjust(left=0.30, right=0.97, top=0.96, bottom=0.13)
ax.set_xscale("log"); ax.set_xlim(1.5, 200000)
n = len(L)
ax.set_ylim(-0.8, n - 0.3)
ax.axvspan(1.5, 25, color=c["b"], alpha=0.22, lw=0)
ax.text(6.2, -0.5, "parallax,\nc. 1900", color=c["b"], fontsize=9.5,
        ha="center", va="center")
for i, (name, d, rung, side, ly) in enumerate(L):
    y = n - 1 - i
    ax.plot([1.5, d], [y, y], color=c["rule"], lw=0.8, zorder=1)
    ax.plot(d, y, "o", color=c["a"], ms=7, zorder=3)
    pc = f"{d:,.0f} pc" if d < 1000 else f"{d/1000:.1f} kpc"
    if name == "61 Cygni": pc = "3.5 pc"
    if name == "Hyades": pc = "47.5 pc"
    approx = "~" if name in ("δ Cephei", "NGC 2158", "M35") else ""
    ax.text(d*1.25, y, f"{approx}{pc} ({ly.lstrip('~')})", va="center",
            color=c["ink"], fontsize=9.5)
    ax.text(1.3, y + 0.13, name, ha="right", va="center", color=c["strong"], fontsize=10.5,
            clip_on=False)
    ax.text(1.3, y - 0.24, rung, ha="right", va="center", color=c["muted"], fontsize=9.5,
            clip_on=False)
ax.set_yticks([]); ax.spines["left"].set_visible(False)
ax.set_xticks([10, 100, 1000, 10000, 100000])
ax.set_xticklabels(["10 pc", "100 pc", "1 kpc", "10 kpc", "100 kpc"])
ax.set_xlabel("Distance (logarithmic: each step is 10\u00d7 farther)")
save(fig, "fig-rung-reach")
