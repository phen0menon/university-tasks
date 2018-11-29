import numpy as np
import matplotlib.pyplot as plt


class Exercise():
    def get_mandelbrot_set(self):
        threshold = 50
        n_max = 50

        x = np.linspace(-2, 1, 1000)
        y = np.linspace(-1.5, 1.5, 1000)

        c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

        z = c

        for j in range(n_max):
            z = z ** 2 + c

        set = abs(z) < threshold
        return set

    def draw_plot(self, matr):
        plt.imshow(matr.T, extent=[-2, 1, -1.5, 1.5])
        plt.gray()
        plt.show()

obj = Exercise()
obj.draw_plot(obj.get_mandelbrot_set())
