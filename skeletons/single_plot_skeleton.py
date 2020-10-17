import matplotlib.pyplot as plt


def add_title(x_guide=0.88, y_guide=0.1, title="Figure X.Y", subtitle="This Figure", font1=12, font2=8,
              bbox={'facecolor': 'none', 'alpha': 0.5, 'pad': 25, 'linewidth': '1.5'}):
    fig = plt.gcf()
    fig.suptitle('                  \n'
                 '                 ', x=x_guide, y=y_guide - .01,
                 bbox=bbox)
    plt.text(x=x_guide, y=y_guide, s=title, fontsize=font1, ha="center", fontweight='bold', transform=fig.transFigure)
    plt.text(x=x_guide, y=y_guide / 2, s=subtitle, fontsize=font2, ha="center",
             transform=fig.transFigure)
    return fig


def plot():
    fig, ax = plt.subplots(1, 1)
    ax.set_position([0.11, 0.15, 0.85, -.3])
    x = [x for x in range(100)]
    y = [x * x for x in range(100)]
    add_title(fig)
    plt.plot(x, y, label='data')
    plt.legend(loc='lower left', bbox_to_anchor=(0.38, 1.01), ncol=2,
               borderaxespad=0, frameon=False)
    return fig


if __name__ == '__main__':
    plot()
    plt.show()
