import string
import sys


def plot_lines():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(0, 2 * np.pi, 200)
    print(f"{x = }")
    y = np.sin(x)
    print(f"{y = }")
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


def plot_scatter():
    import matplotlib.pyplot as plt
    import random
    x = [random.random() for _ in range(30)]
    y = [random.random() for _ in range(30)]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    plt.show()


def plot_barchart():
    import matplotlib.pyplot as plt
    import random
    x = [random.randint(10, 100) for _ in range(10)]
    y = list(string.ascii_uppercase[:10])
    fig, ax = plt.subplots()
    ax.bar( y, x)
    plt.show()


def plot_histogram():
    import matplotlib.pyplot as plt
    import random
    data = [random.gauss(0, 1) for _ in range(1000)]  # N(0, 1) normal
    fig, ax = plt.subplots()
    # data and the number of bins
    n, bins, patches = ax.hist(data, 20, density=True)
    plt.show()


def plot_boxplot():
    import matplotlib.pyplot as plt
    import numpy as np
    data = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (100, 3))
    fig, ax = plt.subplots()
    bplot = ax.boxplot(data)
    plt.show()


def plot_multiplots_and_export():
    import matplotlib.pyplot as plt
    import random
    import numpy as np
    x1 = np.linspace(0, 2 * np.pi, 200)
    y1 = np.sin(x1)
    x2 = [random.random() for _ in range(30)]
    y2 = [random.random() for _ in range(30)]
    fig, axs = plt.subplots(1, 2)
    axs[0].plot(x1, y1)
    axs[1].scatter(x2, y2)
    plt.show()
    fig.savefig('plot_multiplot_and_export.pdf')
    plt.close(fig)


def plot_legend():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    z = np.cos(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="sin(x)")
    ax.plot(x, z, label="cos(x)")
    ax.legend()
    plt.show()


def plot_titles_and_text():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    z = np.cos(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="sin(x)")
    ax.plot(x, z, label="cos(x)")
    ax.legend()
    ax.set_title('Plot Title')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()


def plot_axes():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)
    z = np.cos(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="sin(x)")
    ax.plot(x, z, label="cos(x)")
    ax.legend()
    ax.set_title('Plot Title')
    fig.suptitle('Useful for multiple plots')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True, linestyle='-.')
    ax.tick_params(axis='y', labelcolor='r', labelsize='medium', width=3)
    ax.set_xlim(6, 0)
    ax.axhline(0, color='black', linewidth=2)
    plt.show()


def main():
    # plot_lines()
    # plot_scatter()
    # plot_barchart()
    # plot_histogram()
    # plot_boxplot()
    # plot_multiplots_and_export()
    # plot_legend()
    # plot_titles_and_text()
    plot_axes()
    return 0


if __name__ == '__main__':
    sys.exit(main())
