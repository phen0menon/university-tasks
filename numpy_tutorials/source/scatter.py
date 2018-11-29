import numpy as np
import matplotlib.pyplot as plt


n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
f = np.arctan2(y, x)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(x, y, s=75, c=f, alpha=0.5)
plt.xlim(-1.5, 1.5)
plt.xticks(())
plt.ylim(-1.5, 1.5)
plt.yticks(())
plt.show()