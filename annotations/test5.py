## downloaded 10/15/2020 from stackoverflow
## https://stackoverflow.com/questions/46472533/how-to-put-a-bounding-box-around-groups-of-subplots-while-using-gridspec

from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(9,9))
fig.suptitle(' title ', fontsize=12,
             bbox={'facecolor':'none', 'alpha':0.5, 'pad':5})

colors=["crimson", "indigo", "limegreen", "gold"]

for i in range(4):
    #outer
    outergs = gridspec.GridSpec(1, 1)
    outergs.update(bottom=(i//2)*.47+0.01,left=(i%2)*.5+0.02,
                   top=(1+i//2)*.47-0.01,  right=(1+i%2)*.5-0.02)
    outerax = fig.add_subplot(outergs[0])
    outerax.tick_params(axis='both',which='both',bottom=0,left=0,
                        labelbottom=0, labelleft=0)
    outerax.set_facecolor(colors[i])
    outerax.patch.set_alpha(0.3)

    #inner
    gs = gridspec.GridSpec(2, 2)
    gs.update(bottom=(i//2)*.47+0.05,left=(i%2)*.5+0.08,
                   top=(1+i//2)*.47-0.05,  right=(1+i%2)*.5-0.05,
                   wspace=0.35, hspace=0.35)
    for k in range(4):
        ax = fig.add_subplot(gs[k])
        ax.set_title('Axes Title {}'.format(k+1), color=colors[i])

plt.show()