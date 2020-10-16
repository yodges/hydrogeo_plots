import matplotlib.pyplot as plt
import pandas as pd
import geologic.lithology as lith
import skeletons.single_plot_skeleton as sps
import skeletons.boundingbox as bb
import os


def read_data():
    fn = 'wl_sldl.csv'
    wlpath = {'wd': os.getcwd()}
    wlpath = {'input': os.path.join(wlpath['wd'], 'hydrographs', 'input', fn)}
    df = pd.read_csv(wlpath['input'])
    df['date'] = pd.to_datetime(df['date'])
    df = pd.pivot_table(df, index=df['date'], columns=df['well id'])
    return df


def plot_hydrograph():
    df = read_data()
    print(df.head())
    fig = plt.figure(figsize=(12, 10))
    bb.plot_boundary_box()
    lith.plot_section()
    ax0 = plt.Axes(fig, [.075, .2, .7, .70])
    sps.add_title(x_guide=0.9, y_guide=0.115, title="Figure X.Y",
                  subtitle="subtitle", font1=16, font2=12,
                  bbox={'facecolor': 'none', 'alpha': 0.5, 'pad': 44})
    fig.add_axes(ax0)
    ax0.set_ylabel('Depth (ft)')
    plt.plot(df.index, df['wl'])
    legend_guide = 0.1
    plt.legend([df['wl']['SDLD1'].name, df['wl']['SDLD2'].name, df['wl']['SDLD3'].name, df['wl']['SDLD4'].name,
                df['wl']['SDLD5'].name, df['wl']['SDLD6'].name], loc='lower left',
               bbox_to_anchor=(legend_guide, 1.01), ncol=6, borderaxespad=0, frameon=False)
    plt.show()
