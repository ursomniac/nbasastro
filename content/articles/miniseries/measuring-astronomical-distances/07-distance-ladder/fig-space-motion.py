"""Schematic: a star's space motion split into radial and transverse parts.
v_r from the Doppler shift (km/s); v_t across the line of sight (km/s); proper motion mu is
the angle v_t covers per year as seen from the Sun. Moving-cluster method: the convergent
point gives theta, the angle between the motion and the line of sight, so v_t = v_r tan(theta),
and then distance = v_t / mu. Not to scale.
"""
import numpy as np
import matplotlib.pyplot as plt
from nbas_style import use, save
c = use()
fig, ax = plt.subplots(figsize=(6.0, 2.3))
fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
S = np.array([0.0, 0.0]); P = np.array([6.0, 0.0])
# line of sight
ax.plot([S[0], P[0] + 2.6], [0, 0], color=c["rule"], lw=1.2, ls="--", zorder=1)
ax.text(P[0] + 2.65, 0.0, "line of sight", color=c["muted"], fontsize=9.5, va="center", ha="left",
        rotation=0)
ax.plot(*S, "o", color=c["a"], ms=11); ax.text(S[0], -0.45, "Sun", color=c["a"], ha="center", va="top")
ax.plot(*P, "o", color=c["strong"], ms=8); ax.text(P[0] - 0.15, -0.35, "star", color=c["strong"],
                                                   ha="right", va="top")
vr, vt = 2.2, 1.6
arrow = dict(arrowstyle="-|>", lw=1.8, mutation_scale=14, shrinkA=0, shrinkB=0)
ax.annotate("", xy=(P[0] + vr, P[1] + vt), xytext=P, arrowprops=dict(arrow, color=c["strong"]))
ax.annotate("", xy=(P[0] + vr, P[1]), xytext=P, arrowprops=dict(arrow, color=c["b"]))
ax.annotate("", xy=(P[0] + vr, P[1] + vt), xytext=(P[0] + vr, P[1]),
            arrowprops=dict(arrow, color=c["a"]))
ax.text(P[0] + vr/2, -0.28, "radial velocity\n(Doppler shift, km/s)", color=c["b"],
        ha="center", va="top", fontsize=9.5)
ax.text(P[0] + vr + 0.15, vt/2, "transverse\nvelocity (km/s)", color=c["a"], ha="left",
        va="center", fontsize=9.5)
ax.text(P[0] + vr*0.62, vt*0.98, "space\nmotion", color=c["strong"], ha="right", va="bottom",
        fontsize=9.5)
# theta arc
th = np.arctan2(vt, vr)
a = np.linspace(0, th, 30)
ax.plot(P[0] + 0.8*np.cos(a), 0.8*np.sin(a), color=c["ink"], lw=1)
ax.text(P[0] + 0.95, 0.22, "θ", color=c["ink"], fontsize=11)
# proper motion angle at the Sun
end = np.array([P[0], vt])
ax.plot([S[0], end[0]], [S[1], end[1]], color=c["muted"], lw=0.9, ls=":")
ax.plot([P[0], P[0]], [0, vt], color=c["muted"], lw=0.9, ls=":")
b = np.linspace(0, np.arctan2(vt, P[0]), 20)
ax.plot(2.2*np.cos(b), 2.2*np.sin(b), color=c["ink"], lw=1)
ax.text(2.35, 0.22, "μ", color=c["ink"], fontsize=11)
ax.text(0.2, 2.65, "μ: proper motion, the angle the star moves across\nthe sky per year, as seen from the Sun",
        color=c["ink"], fontsize=9.5, va="top")
ax.text(0.2, 1.75, "distance = transverse velocity ÷ μ", color=c["strong"], fontsize=10.5, va="top")
ax.text(10.5, -1.15, "Not to scale", color=c["muted"], fontsize=9.5, ha="right")
ax.set_xlim(-0.5, 10.6); ax.set_ylim(-1.3, 2.8)
ax.set_aspect("equal"); ax.axis("off")
save(fig, "fig-space-motion")
