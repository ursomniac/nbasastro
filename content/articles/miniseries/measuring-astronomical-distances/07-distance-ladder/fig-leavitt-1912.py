"""Leavitt's 1912 period-luminosity data, replotted.
Source: H. S. Leavitt (statement), E. C. Pickering (signed), "Periods of 25 Variable Stars in
the Small Magellanic Cloud," Harvard College Observatory Circular 173 (1912), Table I.
Columns used: Harvard number, photographic magnitude at maximum and minimum, period (days).
Lines are least-squares fits made here (magnitude vs log10 period), not Leavitt's own lines.
"""
import numpy as np
import matplotlib.pyplot as plt
from nbas_style import use, save
c = use()
T = [  # H, max, min, period (d)
 (1505,14.8,16.1,1.25336),(1436,14.8,16.4,1.6637),(1446,14.8,16.4,1.7620),
 (1506,15.1,16.3,1.87502),(1413,14.7,15.6,2.17352),(1460,14.4,15.7,2.913),
 (1422,14.7,15.9,3.501),(842,14.6,16.1,4.2897),(1425,14.3,15.3,4.547),
 (1742,14.3,15.5,4.9866),(1646,14.4,15.4,5.311),(1649,14.3,15.2,5.323),
 (1492,13.8,14.8,6.2926),(1400,14.1,14.8,6.650),(1355,14.0,14.8,7.483),
 (1374,13.9,15.2,8.397),(818,13.6,14.7,10.336),(1610,13.4,14.6,11.645),
 (1365,13.8,14.8,12.417),(1351,13.4,14.4,13.08),(827,13.4,14.3,13.47),
 (822,13.0,14.6,16.75),(823,12.2,14.1,31.94),(824,11.4,12.8,65.8),(821,11.2,12.1,127.0)]
assert len(T) == 25
P = np.array([t[3] for t in T]); mx = np.array([t[1] for t in T]); mn = np.array([t[2] for t in T])
lp = np.log10(P)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.6))
fig.subplots_adjust(left=0.09, right=0.98, top=0.88, bottom=0.15, wspace=0.28)
for ax, x in ((a1, P), (a2, lp)):
    ax.plot(x, mx, "o", color=c["a"], ms=5.5, label="at maximum light")
    ax.plot(x, mn, "s", color=c["b"], ms=4.5, label="at minimum light")
    ax.invert_yaxis(); ax.grid(True)
for y, col, ls in ((mx, c["a"], "-"), (mn, c["b"], "--")):
    k, b = np.polyfit(lp, y, 1)
    xx = np.linspace(0.0, 2.2, 10)
    a2.plot(xx, k*xx + b, color=col, lw=1.4, ls=ls)
    print("fit slope", round(k, 2), "intercept", round(b, 2))
a1.set_xlabel("Period (days)"); a1.set_ylabel("Apparent magnitude (brighter ↑)")
a2.set_xlabel("Logarithm of period (days)")
a1.set_title("Period", fontsize=10.5, color=c["strong"])
a2.set_title("Logarithm of period: a straight line", fontsize=10.5, color=c["strong"])
a1.set_xlim(0, 135); a2.set_xlim(0, 2.2)
for ax in (a1, a2): ax.set_ylim(16.7, 10.8)
a1.legend(loc="lower right", frameon=False, fontsize=9.5)
save(fig, "fig-leavitt-1912")
