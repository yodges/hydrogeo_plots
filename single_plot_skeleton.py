import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_position([0.11, -.06, 0.85, 0.7])
    fig.suptitle('Figure X.Y \n'
                 'This Figure', x=.88, y=.115, fontsize=14, fontweight='bold',
                 bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
    x = [x for x in range(100)]
    y = [x*x for x in range(100)]
    ax.set_yscale('linear')
    ax.plot(x,y, label='data')
    ax.legend(loc='lower left', bbox_to_anchor=(0.38, 1.01), ncol=2,
              borderaxespad=0, frameon=False)
    return fig

if __name__ == '__main__':
    main()
    plt.show()