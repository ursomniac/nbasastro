"""Pleiades colour-magnitude diagram.

Data:
- Members: Cantat-Gaudin et al. 2020 (A&A 640, A1), VizieR J/A+A/640/A1/nodup, Cluster=Melotte_22,
  retrieved 2026-11-06 via the CfA VizieR mirror (file members-m45.tsv). 952 stars, all proba >= 0.7,
  Gaia DR2 G = 5.43 to 17.96. Gaia DR2 photometry as listed (G, BP-RP); no extinction correction
  (A_V = 0.18 for the cluster in Cantat-Gaudin 2020 table1 -> small; noted in caption).
- The member list contains no stars brighter than G ~ 5.4, so seven named stars are missing.
  Added from HYG v4.1 (Hipparcos V and B-V) and converted with the Johnson-Cousins relations of
  Evans et al. 2018 (A&A 616, A4, Table A.2):
      G - V    = -0.02907 - 0.02385 x - 0.2297 x^2 - 0.001768 x^3      (x = B-V)
      BP - RP  = -0.04212 + 1.286 x - 0.09494 x^2
  Check on Celaeno and Asterope (in both catalogs): G agrees to 0.01 mag; converted BP-RP is
  ~0.05 bluer than Gaia's. Plotted with a distinct marker.
- Right axis: absolute magnitude for 136.2 pc (Melis et al. 2014): distance modulus 5.67.
"""
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from nbas_style import use, save

c = use()
f = '/mnt/user-data/uploads/8298188c-members-m45.tsv'
L = [l for l in open(f).read().splitlines() if not l.startswith('#') and l.strip()]
g = pd.DataFrame([r.split('\t') for r in L[3:]], columns=L[0].split('\t'))
g['G'] = pd.to_numeric(g['Gmag'], errors='coerce'); g['C'] = pd.to_numeric(g['BP-RP'], errors='coerce')
g = g.dropna(subset=['G', 'C'])

h = pd.read_csv('/home/claude/astronexus/hyg-database/hyg/CURRENT/hygdata_v41.csv', low_memory=False)
named = ['Alcyone', 'Atlas', 'Electra', 'Maia', 'Merope', 'Taygeta', 'Pleione']
b = h[h.proper.isin(named)].copy()
x = b.ci
b['G'] = b.mag + (-0.02907 - 0.02385*x - 0.2297*x**2 - 0.001768*x**3)
b['C'] = -0.04212 + 1.286*x - 0.09494*x**2

DM = 5*np.log10(136.2) - 5

fig, ax = plt.subplots(figsize=(7.2, 6.4))
fig.subplots_adjust(left=0.10, right=0.88, top=0.97, bottom=0.09)
ax.scatter(g.C, g.G, s=6, color=c['b'], alpha=0.75, lw=0, label='Gaia members (952)')
ax.scatter(b.C, b.G, s=46, marker='*', color=c['a'], lw=0, label='brightest stars, from Hipparcos')
ax.invert_yaxis()
ax.set_xlim(-0.55, 3.7); ax.set_ylim(18.5, 1.8)
ax.set_xlabel('Color, Gaia BP − RP   (blue ←   → red)')
ax.set_ylabel('Apparent brightness, Gaia G (mag)')
ax.grid(alpha=0.5)

ax2 = ax.twinx()
ax2.set_ylim(ax.get_ylim()[0] - DM, ax.get_ylim()[1] - DM)
ax2.set_ylabel('Absolute magnitude, M$_G$')
ax2.spines['right'].set_visible(True); ax2.spines['right'].set_color(c['rule'])

# labels for the named stars: a column at the right with thin leader lines
pts = [(r.proper, r.C, r.G) for _, r in b.iterrows()]
for n in ['Celaeno', 'Asterope']:
    s_ = h[h.proper == n].iloc[0]
    gi = ((g.G - (s_.mag - 0.03)).abs()).idxmin()
    pts.append((n, g.C[gi], g.G[gi]))
pts.sort(key=lambda t: t[2])
for k, (n, xx, yy) in enumerate(pts):
    ly = 2.6 + 0.47 * k
    ax.annotate(n, (xx, yy), xytext=(0.32, ly), textcoords='data', ha='left', va='center',
                fontsize=9.5, color=c['ink'],
                arrowprops=dict(arrowstyle='-', color=c['muted'], lw=0.6, shrinkA=2, shrinkB=3))
ax.text(1.75, 11.0, 'main sequence', fontsize=10.5, color=c['muted'], rotation=-27, ha='center')
ax.text(-0.5, 16.75, 'Brown dwarfs and the lithium boundary lie below\nthis plot, too faint for the Gaia member list.',
        fontsize=9.5, color=c['muted'], ha='left', va='bottom')
leg = ax.legend(loc='upper right', fontsize=9.5, frameon=False)
save(fig, 'fig-pleiades-cmd')
