import numpy as np
import matplotlib.pyplot as plt


class Exercise():

    def __init__(self):
        self.a = np.linspace(0, 1, 24)
        self.b = np.linspace(0, 1, 12)
        self.c = np.linspace(0, 1, 6)

    def func(self, a, b, c):
        return (a ** b) - c

    def integral(self):
        a_set = self.a[:, np.newaxis, np.newaxis]
        b_set = self.b[np.newaxis, :, np.newaxis]
        c_set = self.c[np.newaxis, np.newaxis, :]

        self.integral = self.func(a_set, b_set, c_set)
        return np.round(self.integral), 5)

ex = Exercise()
print(ex.integral())
