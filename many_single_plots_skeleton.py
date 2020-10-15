import matplotlib.pyplot as plt
import single_plot_skeleton as sps


def plot():
    fig, ax = plt.subplots(1, 1)
    ax.set_position([0.11, 0.15, 0.85, -.3])
    x = [x for x in range(100)]
    y = [x * x for x in range(100)]
    sps.add_title(fig)
    plt.plot(x, y, label='data')
    plt.legend(loc='lower left', bbox_to_anchor=(0.38, 1.01), ncol=2,
               borderaxespad=0, frameon=False)
    plt.show()
    # return fig


def plots():
    for i in range(1000):
        plot()


if __name__ == '__main__':
    plots()
