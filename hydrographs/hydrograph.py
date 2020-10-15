import matplotlib as plt
import geologic.lithology as lith
import skeletons.single_plot_skeleton as sps

fig = plt.figure(figsize=(10, 10))

sps.add_title()

lith.import_dfs()
lith.plot_section()


def plot_hydrograph():
    pass


if __name__ == '__main__':
    plot_hydrograph()
