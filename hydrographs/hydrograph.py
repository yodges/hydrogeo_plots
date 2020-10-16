import matplotlib.pyplot as plt
import pandas as pd
import geologic.lithology as lith
import skeletons.single_plot_skeleton as sps
import skeletons.boundingbox as bb
import os


# TODO add geologic legend to bottom
# TODO colorcode lines by formation symbology
# TODO read all wells from single dataset (one for wl data, one for hydrogeology, etc)
# TODO change lithology to pd.read_csv instead of read_excel

def prep_data():
    fn = 'wl_sldl.csv'
    wlpath = {'wd': os.getcwd()}
    wlpath = {'input': os.path.join(wlpath['wd'], 'hydrographs', 'input', fn)}
    df = pd.read_csv(wlpath['input'])
    df['date'] = pd.to_datetime(df['date'])
    df = pd.pivot_table(df, index=df['date'], columns=df['well id'])
    return df


def plot_title_labels(ax, df):
    sps.add_title(x_guide=0.915, y_guide=0.095, title="Figure X.Y",
                  subtitle="subtitle", font1=16, font2=12,
                  bbox={'facecolor': 'none', 'alpha': 0.5, 'pad': 30})
    ax.set_ylabel('Elevation (ft, msl)')
    ax.set_title('Suptitle')
    axes = plt.gca()
    axes.yaxis.grid()
    legend_guide = 0.1
    labels = [df['wl'][f'SDLD{id}'].name for id in range(1, 7)]
    plt.legend(labels, loc='lower left', bbox_to_anchor=(legend_guide, -0.1),
               ncol=6, borderaxespad=0, frameon=False)


def set_colors(dfs, symbology):
    colors = {}
    for i in dfs['Well'].itertuples():
        well_id = getattr(i, 'well_id')
        well_top = getattr(i, 'Depth_Top_ft')
        well_bot = getattr(i, 'Depth_Bot_ft')
        for j in dfs['Lithology'].itertuples():
            material = getattr(j, 'Material')
            lay_top = getattr(j, 'Depth_Top_ft')
            lay_bot = getattr(j, 'Depth_Bot_ft')
            if well_top >= lay_top and well_bot <= lay_bot:
                colors[well_id] = symbology['Lithology'][material]['color']
    return colors


def plot_hydrograph():
    df = prep_data()
    fig = plt.figure(figsize=(12, 10))
    bb.plot_boundary_box(facecolor='none')
    dfs, well, symbology = lith.plot_section()
    colors = set_colors(dfs, symbology)
    print(colors)
    ax0 = plt.Axes(fig, [.075, .2, .7, .70])
    fig.add_axes(ax0)
    #plt.plot(df.index, df['wl'], c=colors)
    for color in colors.keys():
        plt.plot(df.index, df['wl'][color], color=colors[color], linewidth=2)
    plot_title_labels(ax0, df)
    plt.show()
