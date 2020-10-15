## downloaded 10/14/2020 from matplotlib website
## https://matplotlib.org/3.3.1/tutorials/text/text_intro.html
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_position([0.11, -.09, 0.85, 0.88])


# Set titles for the figure and the subplot respectively
fig.suptitle('Figure x.y \n'
             'this', x=.8, y=.12, fontsize=14, fontweight='bold')

ax.set_title('axes title')

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')


# Set both x- and y-axis limits to [0, 10] instead of default [0, 1]
ax.axis([0, 10, 0, 10])

ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)

ax.plot([2], [1], 'o')
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax2 = fig.add_axes([5, 5, 0.2, 0.2])

plt.show()
