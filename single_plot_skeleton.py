import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_position([0.11, -.06, 0.85, 0.7])
    fig.suptitle('Figure X.Y \n'
                 'This Figure', x=.88, y=.115, fontsize=14, fontweight='bold',
                 bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10})
    x = [x for x in range(1000)]
    y = [x*x for x in range(1000)]
    ax.plot(x,y)

    return fig

if __name__ == '__main__':
    main()
    plt.show()