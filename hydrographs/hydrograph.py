import matplotlib.pyplot as plt
import geologic.lithology as lith
import skeletons.single_plot_skeleton as sps


def plot_hydrograph():
    fig = plt.figure(figsize=(10, 10))
    lith.plot_section()
    ax0 = plt.Axes(fig, [.075, .2, .7, .70])
    sps.add_title(x_guide=0.88, y_guide=0.08, title="Figure X.Y",
                  subtitle="This Figure needs more text", font1=16, font2=12,
                  bbox={'facecolor': 'none', 'alpha': 0.5, 'pad': 60})
    fig.add_axes(ax0)
    ax0.set_ylabel('Depth (ft)')
    pass


if __name__ == '__main__':
    plot_hydrograph()
    plt.show()
