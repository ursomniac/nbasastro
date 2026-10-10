"""fig-tuning-fork-peculiar: Hubble's tuning fork with the article's galaxies placed
by their catalog (RC3/NED) types. Schematic only -- glyphs are not to scale.
Types used: M51 SA(s)bc pec; NGC 7714 SB(s)b? pec; NGC 660 SB(s)a pec;
NGC 7252 (R)SA(r)0; NGC 337 SB(s)d; NGC 520 'pec' (no Hubble type)."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch

INK="#333333"; MUTE="#8a8a8a"; ACC="#D55E00"
plt.rcParams.update({"font.family":"DejaVu Sans","svg.fonttype":"none"})
fig,ax=plt.subplots(figsize=(11,5.9)); ax.set_xlim(0,11); ax.set_ylim(-3.75,3.1); ax.axis("off")

def ell(x,y,q):
    ax.add_patch(Ellipse((x,y),0.62,0.62*q,fc="#d9d9d9",ec=INK,lw=1.2))
def spiral(x,y,wind,bar=False,ls="-",col=INK):
    t=np.linspace(0,wind,120)
    r0=0.10 if not bar else 0.17
    r=r0+ (0.36-r0)*t/t.max()
    for s in (0,np.pi):
        ax.plot(x+r*np.cos(t+s),y+0.8*r*np.sin(t+s),color=col,lw=1.4,ls=ls)
    if bar: ax.plot([x-0.17,x+0.17],[y,y],color=col,lw=3,solid_capstyle="round")
    else: ax.add_patch(Ellipse((x,y),0.16,0.13,fc=col,ec=col))
def lab(x,y,s,c=INK): ax.text(x,y,s,ha="center",va="top",fontsize=11,color=c)

# handle: ellipticals and S0
for x,q,n in [(0.7,1.0,"E0"),(1.8,0.7,"E3"),(2.9,0.4,"E7")]:
    ell(x,0,q); lab(x,-0.45,n)
ax.add_patch(Ellipse((4.2,0),0.70,0.20,fc="#d9d9d9",ec=INK,lw=1.2)); ax.add_patch(Ellipse((4.2,0),0.22,0.22,fc="#bdbdbd",ec=INK,lw=1.0))
lab(4.2,-0.45,"S0")
ax.plot([1.15,1.4],[0,0],color=MUTE,lw=1); ax.plot([2.2,2.5],[0,0],color=MUTE,lw=1); ax.plot([3.3,3.75],[0,0],color=MUTE,lw=1)
# prongs
up=[(5.7,1.25,"Sa",5.2),(7.1,1.55,"Sb",4.0),(8.5,1.85,"Sc",3.0)]
dn=[(5.7,-1.25,"SBa",5.2),(7.1,-1.55,"SBb",4.0),(8.5,-1.85,"SBc",3.0)]
ax.plot([4.65,5.25],[0.15,0.95],color=MUTE,lw=1); ax.plot([4.65,5.25],[-0.15,-0.95],color=MUTE,lw=1)
for row,b in ((up,False),(dn,True)):
    for i,(x,y,n,w) in enumerate(row):
        spiral(x,y,w,bar=b); lab(x,y-0.42,n)
        if i<2: ax.plot([x+0.45,row[i+1][0]-0.45],[y+0.08*np.sign(y),row[i+1][1]-0.08*np.sign(y)],color=MUTE,lw=1)
# later extension (de Vaucouleurs)
for (x,y,n,b) in [(9.9,2.15,"Sd",False),(9.9,-2.15,"SBd",True)]:
    spiral(x,y,2.0,bar=b,ls=(0,(3,2)),col=MUTE); lab(x,y-0.42,n,MUTE)
ax.text(9.9,2.75,"added later\n(de Vaucouleurs)",ha="center",va="center",fontsize=8.5,color=MUTE,style="italic")
ax.text(0.35,2.85,"Hubble's tuning fork (1936)",fontsize=14,color=INK,weight="bold",va="center")
ax.text(0.35,2.45,"Sorted by shape. No axis for time, no slot for an event.",fontsize=10.5,color=INK,va="center")
ax.text(1.8,0.75,"ellipticals",ha="center",fontsize=9.5,color=MUTE,style="italic")
ax.text(7.1,2.35,"spirals",ha="center",fontsize=9.5,color=MUTE,style="italic")
ax.text(7.1,-0.95,"barred spirals",ha="center",fontsize=9.5,color=MUTE,style="italic")

def tag(x,y,txt,tx,ty,ha="center"):
    ax.plot([x],[y],marker="D",ms=7,mfc=ACC,mec="white",mew=1,zorder=5)
    ax.annotate(txt,(x,y),(tx,ty),ha=ha,va="center",fontsize=9.5,color=ACC,weight="bold",
                arrowprops=dict(arrowstyle="-",color=ACC,lw=1),zorder=6)
tag(7.8,1.15,"M51\nSbc pec",7.8,0.45)
tag(4.2,0.28,"NGC 7252\nS0 (!)",4.2,1.25)
tag(5.25,-1.62,"NGC 660\nSBa pec",4.55,-2.45)
tag(6.65,-1.92,"NGC 7714\nSBb pec",6.3,-2.75)
tag(9.45,-2.5,"NGC 337\nSBd",8.75,-2.95)
ax.add_patch(FancyBboxPatch((1.0,-2.75),2.3,1.15,boxstyle="round,pad=0.08",fc="white",ec=ACC,lw=1.3,ls=(0,(4,2))))
ax.plot([1.3],[-1.95],marker="D",ms=7,mfc=ACC,mec="white",mew=1)
ax.text(1.5,-1.95,"NGC 520",fontsize=9.5,color=ACC,weight="bold",va="center")
ax.text(1.12,-2.42,'catalog type: "pec"\nnot on the fork at all',fontsize=9,color=INK,va="center")
ax.text(10.9,-3.6,'"pec" = peculiar: the catalog\'s way of saying "this type, but something happened"',
        ha="right",fontsize=8.5,color=MUTE,style="italic")
for ext,kw in (("svg",{}),("png",{"dpi":200})):
    fig.savefig(f"/mnt/user-data/outputs/fig-tuning-fork-peculiar.{ext}",bbox_inches="tight",facecolor="white",**kw)
