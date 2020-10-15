import matplotlib.pyplot as plt
import skeletons.single_plot_skeleton as sps


def plot(title="Figure X.Y", subtitle="This Figure"):
    legend_guide = 0.3
    fig, ax = plt.subplots(1, 1)
    ax.set_position([0.11, 0.15, 0.85, -.3])
    x = [x for x in range(100)]
    y = [x * x for x in range(100)]
    sps.add_title(fig, title=title, subtitle=subtitle)
    plt.plot(x, y, label='data')
    y2 = [5 * x for x in range(100)]
    plt.plot(x, y2, label='data2')
    plt.legend(loc='lower left', bbox_to_anchor=(legend_guide, 1.01), ncol=2,
               borderaxespad=0, frameon=False)
    plt.show()


def plots():
    for i in range(1):
        plot()


if __name__ == '__main__':
    plots()
