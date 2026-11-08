"""C09 thumbnail (600x600): the halo view, square crop around the Galaxy, no overlays or text.
Uses the cached raw render and the shared stretch from fig-view-from.py."""
import importlib.util, pickle, numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
spec = importlib.util.spec_from_file_location("v", "fig-view-from.py"); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
img = v.stretch(pickle.load(open(v.cache_name("halo"), "rb")))
h, w = img.shape; cx = w // 2; half = h // 2
sq = img[:, cx - half: cx + half]                      # full height, centered square
fig = plt.figure(figsize=(3, 3)); ax = fig.add_axes([0, 0, 1, 1])
ax.imshow(sq, origin="lower", cmap="gray", vmin=0, vmax=1); ax.axis("off")
fig.savefig("thumbnail.png", dpi=200, facecolor="black")
