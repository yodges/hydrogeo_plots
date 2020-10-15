## downloaded 10/14/2020 from stackoverflow
## https://stackoverflow.com/questions/17458580/embedding-small-plots-inside-subplots-in-matplotlib
import matplotlib.pyplot as plt
import numpy as np


def add_subplot_axes(ax, rect, facecolor='w'):
    fig = plt.gcf()
    box = ax.get_position()
    width = box.width
    height = box.height
    inax_position = ax.transAxes.transform(rect[0:2])
    transFigure = fig.transFigure.inverted()
    infig_position = transFigure.transform(inax_position)
    x = infig_position[0]
    y = infig_position[1]
    width *= rect[2]
    height *= rect[3]  # <= Typo was here
    subax = fig.add_axes([x, y, width, height], facecolor=facecolor)
    x_labelsize = subax.get_xticklabels()[0].get_size()
    y_labelsize = subax.get_yticklabels()[0].get_size()
    x_labelsize *= rect[2] ** 0.5
    y_labelsize *= rect[3] ** 0.5
    subax.xaxis.set_tick_params(labelsize=x_labelsize)
    subax.yaxis.set_tick_params(labelsize=y_labelsize)
    return subax

def add_corner_subplot(ax,rect,facecolor='w'):
    fig = plt.gcf()
    ax.axis([0, 10, 0, 10])
    box = ax.get_position()
    x = .9
    y = .8
    titleblock = fig.add_axes([x, y, box.width, box.height], facecolor=facecolor)
    return titleblock

def example1():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    rect = [0.2, 0.2, 0.7, 0.7]
    ax1 = add_corner_subplot(ax, rect)
    #ax2 = add_subplot_axes(ax1, rect)
    #ax3 = add_subplot_axes(ax2, rect)
    plt.show()


def example2():
    fig = plt.figure(figsize=(10, 10))
    axes = []
    subpos = [0.2, 0.6, 0.3, 0.3]
    x = np.linspace(-np.pi, np.pi)
    for i in range(1, 5):
        axes.append(fig.add_subplot(2, 2, i))
    for axis in axes:
        axis.set_xlim(-np.pi, np.pi)
        axis.set_ylim(-1, 3)
        axis.plot(x, np.sin(x))
        subax1 = add_subplot_axes(axis, subpos)
        subax2 = add_subplot_axes(subax1, subpos)
        subax1.plot(x, np.sin(x))
        subax2.plot(x, np.sin(x))


if __name__ == '__main__':
    example1()
    plt.show()
