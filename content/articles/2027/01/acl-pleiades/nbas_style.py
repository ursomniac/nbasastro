"""NBAS figure style. One look for the site (dark) and the book (light).

Usage in a figure script:
    from nbas_style import use, save
    c = use()                 # theme from NBAS_THEME env var: "web" (default) or "print"
    ... draw with c["ink"], c["a"], c["b"], c["muted"], c["rule"] ...
    save(fig, "fig-name")     # writes fig-name.svg and fig-name.png (print: -print suffix)

Colors are the site's own: page #1a2a44, text #d1d1d1, rules #3a4a64,
gold #d4af37 (table headers), blue #4aa3df (miniseries badge).
"""
import os
import matplotlib as mpl
import matplotlib.pyplot as plt

THEMES = {
    "web": dict(bg="#1a2a44", ink="#d1d1d1", strong="#ffffff", muted="#8f9bb0",
                rule="#3a4a64", a="#d4af37", b="#4aa3df"),
    "print": dict(bg="#ffffff", ink="#222222", strong="#000000", muted="#6b7280",
                  rule="#c9ced6", a="#9a7b14", b="#1f6fa8"),
}

def use(theme=None):
    theme = theme or os.environ.get("NBAS_THEME", "web")
    c = dict(THEMES[theme], name=theme)
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Liberation Sans", "Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 10.5,
        "figure.facecolor": c["bg"], "axes.facecolor": c["bg"], "savefig.facecolor": c["bg"],
        "text.color": c["ink"], "axes.labelcolor": c["ink"],
        "axes.edgecolor": c["rule"], "xtick.color": c["muted"], "ytick.color": c["muted"],
        "grid.color": c["rule"], "grid.linewidth": 0.6,
        "axes.spines.top": False, "axes.spines.right": False,
        "lines.linewidth": 2.0, "lines.solid_capstyle": "round",
        "axes.prop_cycle": mpl.cycler(color=[c["a"], c["b"], c["muted"]]),
        "svg.fonttype": "path",      # text as outlines: identical everywhere
        "savefig.dpi": 200,          # 7.2 in wide -> 1440 px, 2x a 720 px column
    })
    return c

def save(fig, name):
    theme = os.environ.get("NBAS_THEME", "web")
    stem = name if theme == "web" else f"{name}-print"
    fig.savefig(f"{stem}.svg")
    fig.savefig(f"{stem}.png")
    plt.close(fig)
    return stem
