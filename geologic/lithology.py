## TODO: add simple plotting functions for hydrogeologic or lithologic section on a particular axis
## TODO: include this in script with hydographs to plot multiport waterlevels with section ala USGS san diego wells

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Patch, FancyBboxPatch
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

dirs = {'wd': os.getcwd()}
dirs = {'input': os.path.join(dirs['wd'], 'input'),
        'output': os.path.join(dirs['wd'], 'output')
        }
units = {'L': dict(depth='ft', diam='in', datum='bgs')}
unit_conv = {'L': {'ft/in': 1 / 12,
                   'in/ft': 12}}
well = dict(name='Template Well', ID='Template_Well', profile='Dynamic')

files = dict(input=dict(workbook=well['ID'] + '_Data.xlsx',
                        worksheet=['Lithology']),
             output={'table': dict(workbook=well['ID'] + '_Profile.xlsx'),
                     'figure': dict(format='png', dpi=200, transparent=False)
                     })
# fig, axs = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(10, 10), dpi=files['output']['figure']['dpi'],
#                         constrained_layout=True)

ax_specs = dict(bore=dict(max=dict(radius=48 / 2, depth=678),
                          min=dict(radius=48 / 2, depth=0)))

symbology = {'Lithology': dict(gravel=dict(hatch='', color=(255 / 255, 204 / 255, 153 / 255, 0.3)),
                               sand=dict(hatch='', color=(255 / 255, 255 / 255, 153 / 255, 0.3)),
                               silt=dict(hatch='', color=(204 / 255, 255 / 255, 153 / 255, 0.3)),
                               clay=dict(hatch='', color=(153 / 255, 204 / 255, 255 / 255, 0.3))),
             'label': dict(title={'fontsize': 'x-large'},
                           axis={'fontsize': 'large'},
                           ticks={'fontsize': 'large'},
                           data={'fontsize': 'small'})}


def import_dfs():
    dfs = {'input': {}}
    print('Importing data from:', files['input']['workbook'])
    for ws in files['input']['worksheet']:
        dfs['input'][ws] = pd.read_excel(os.path.join(dirs['input'], files['input']['workbook']), sheet_name=ws)
        print('\tImported:', ws)
    return dfs


dfs = import_dfs()


def plot_wellbore(dfs=dfs['input'], ax_specs=ax_specs['bore'], symbology=symbology,
                  units=units):
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
    fig = plt.figure(figsize=(10,10))
    ax0 = plt.Axes(fig, [.075, .2, .7, .70])
    fig.add_axes(ax0)
    ax_well = plt.Axes(fig, [.85, .2, .1, .70])
    fig.add_axes(ax_well)
    #ax_well.set_position([0.8, -0.1, .2, 1])
    ax_well.set_ylabel('Depth (' + units['L']['depth'] + ' ' + units['L']['datum'] + ')',
                       fontsize=symbology['label']['axis']['fontsize'])
    ax_well.yaxis.set_minor_locator(AutoMinorLocator())
    ax_well.set_ylim([ax_specs['max']['depth'], ax_specs['min']['depth']])
    ax_well.set_xlim([-1 * ax_specs['min']['radius'], ax_specs['max']['radius']])
    ax_well.set_xticks(ticks=[])
    ax_well.tick_params(axis='both', labelsize=symbology['label']['ticks']['fontsize'], labelleft=True)
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
    # A. plot lithology
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


plot_wellbore()
#axs[1].set_title(well['name'], fontsize=symbology['label']['title']['fontsize'])
plt.show()