from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

def plot_boundary_box():
    fig = plt.gcf()
    outergs = gridspec.GridSpec(1, 1)
    outergs.update(bottom=.01, left=.01,
                   top=.99, right=.99)
    outerax = fig.add_subplot(outergs[0])
    outerax.tick_params(axis='both', which='both', bottom=0, left=0,
                        labelbottom=0, labelleft=0)