import matplotlib.pyplot as plt


def add_title(fig):
    x_guide = 0.88
    y_guide = .1
    fig.suptitle('                  \n'
                 '                 ', x=x_guide, y=y_guide - .01,
                 bbox={'facecolor': 'none', 'alpha': 0.5, 'pad': 25})
    plt.text(x=x_guide, y=y_guide, s="My title", fontsize=12, ha="center", fontweight='bold', transform=fig.transFigure)
    plt.text(x=x_guide, y=y_guide / 2, s="My title in different size", fontsize=8, ha="center",
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
