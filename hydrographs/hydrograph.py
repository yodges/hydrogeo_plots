import matplotlib.pyplot as plt
import geologic.lithology as lith
import skeletons.single_plot_skeleton as sps
import skeletons.boundingbox as bb


def plot_hydrograph():
    fig = plt.figure(figsize=(12, 10))
    bb.plot_boundary_box()
    lith.plot_section()
    ax0 = plt.Axes(fig, [.075, .2, .7, .70])
    sps.add_title(x_guide=0.9, y_guide=0.115, title="Figure X.Y",
                  subtitle="subtitle", font1=16, font2=12,
                  bbox={'facecolor': 'none', 'alpha': 0.5, 'pad': 44})
    fig.add_axes(ax0)
    ax0.set_ylabel('Depth (ft)')
    legend_guide = 0.3
    x = [x for x in range(100)]
    y = [x * x for x in range(100)]
    plt.plot(x, y, label='data')
    y2 = [5 * x for x in range(100)]
    plt.plot(x, y2, label='data2')
    plt.legend(loc='lower left', bbox_to_anchor=(legend_guide, 1.01), ncol=2,
               borderaxespad=0, frameon=False)
    plt.show()


if __name__ == '__main__':
    plot_hydrograph()
