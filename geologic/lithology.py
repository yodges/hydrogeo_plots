import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Patch, FancyBboxPatch
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)


def import_dfs():
    dirs = {'wd': os.getcwd()}
    dirs = {'input': os.path.join(dirs['wd'],'geologic', 'input'),
            'output': os.path.join(dirs['wd'], 'geologic', 'output')
            }

    well = dict(name='Template Well', ID='Template_Well', profile='Dynamic')

    files = dict(input=dict(workbook=well['ID'] + '_Data.xlsx',
                            worksheet=['Lithology']),
                 output={'table': dict(workbook=well['ID'] + '_Profile.xlsx'),
                         'figure': dict(format='png', dpi=200, transparent=False)
                         })

    dfs = {'input': {}}
    print('Importing data from:', files['input']['workbook'])
    for ws in files['input']['worksheet']:
        dfs['input'][ws] = pd.read_excel(os.path.join(dirs['input'], files['input']['workbook']), sheet_name=ws)
        print('\tImported:', ws)
    return dfs['input']


def plot_section(dfs=import_dfs(), well=dict(name='Template Well', ID='Template_Well', profile='Dynamic')):
    '''
    This function plots borehole lithology and/or well construction.

    INPUTS:
    - ax: pyplot axes object to plot wellbore onto
    - dfs: dictionary of dataframes containing intervals and attributes of each component
        - Required attribute fieldnames per dataframe:
            A. Lithology:
                1. 'Depth_Top_[units]'
                2. 'Depth_Bot_[units]'
                3. 'Material'
            B. Well Components (any dataframe ame specified in well_components):
                1. 'Depth_Top_[units]'
                2. 'Depth_Bot_[units]'
                1. 'Diam_Top_[units]'
                2. 'Diam_Bot_[units]'
                5. 'Material'
            C. Water Levels (plots in borehole lithology if no well attributes are provided)
    - well_components: list of components to consider for well construction (i.e., annulus, well casing/screen, pump)
    - ax_specs: dictionary of axes min and max dimensions
    - symbology: dictionary of symbology for each component (lithology, well_components, water levels)
    - units: dictionary of units
    '''
    ax_specs = dict(max=dict(radius=48 / 2, depth=678),
                    min=dict(radius=48 / 2, depth=0))

    symbology = {'Lithology': dict(gravel=dict(hatch='', color='green'),
                                   sand=dict(hatch='', color='lightblue'),
                                   silt=dict(hatch='', color='gold'),
                                   clay=dict(hatch='', color='crimson')),
                 'label': dict(title={'fontsize': 'x-large'},
                               axis={'fontsize': 'large'},
                               ticks={'fontsize': 'large'},
                               data={'fontsize': 'small'})}
    units = {'L': dict(depth='ft', diam='in', datum='bgs')}
    fig = plt.gcf()
    ax_well = plt.Axes(fig, [.85, .2, .1, .70])
    fig.add_axes(ax_well)
    ax_well.yaxis.set_minor_locator(AutoMinorLocator())
    ax_well.set_ylim([ax_specs['max']['depth'], ax_specs['min']['depth']])
    ax_well.set_xlim([-1 * ax_specs['min']['radius'], ax_specs['max']['radius']])
    ax_well.set_xticks(ticks=[])
    ax_well.tick_params(axis='both', labelsize=symbology['label']['ticks']['fontsize'], labelleft=True)
    ax_well.set_title(well['name'], fontsize=symbology['label']['title']['fontsize'])
    # polygon vertices indices
    idx = {'depth': {'rows': {'top': np.array([0.5, 1], dtype=np.int),
                              'bot': np.array([2, 3], dtype=np.int)},
                     'col': int(1)
                     },
           'diam': {'rows': {'left': np.array([0, 3], dtype=np.int),
                             'right': np.array([1, 2], dtype=np.int)},
                    'col': int(0)
                    }
           }

    dims = {'Lithology': {}}
    for r in dfs['Lithology'].itertuples():
        dims['Lithology'][r.Index] = {}
        for k in symbology['Lithology'].keys():
            if k in getattr(r, 'Material'):
                dims['Lithology'][r.Index][k] = np.zeros((4, 2))
                # x-axis values
                dims['Lithology'][r.Index][k][idx['diam']['rows']['left'],
                                              idx['diam']['col']] = ax_specs['min']['radius'] * -1
                dims['Lithology'][r.Index][k][idx['diam']['rows']['right'],
                                              idx['diam']['col']] = ax_specs['max']['radius']
                # y-axis values
                dims['Lithology'][r.Index][k][idx['depth']['rows']['top'],
                                              idx['depth']['col']] = getattr(r, 'Depth_Top_' + units['L']['depth'])
                dims['Lithology'][r.Index][k][idx['depth']['rows']['bot'],
                                              idx['depth']['col']] = getattr(r, 'Depth_Bot_' + units['L']['depth'])

                ax_well.add_patch(
                    Polygon(dims['Lithology'][r.Index][k], closed=True, hatch=symbology['Lithology'][k]['hatch'],
                            facecolor=symbology['Lithology'][k]['color'], edgecolor='k'))
    return fig
