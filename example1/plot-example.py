import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # just some fake data
    xs = [0, 1, 2, 3, 4, 5]
    ys = [3, 0, 1, 2, 0, 4]

    fig_file = "plot.png"
    plt.plot(xs, ys, 'b:')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Very Important Plot')
    plt.savefig(fig_file)
