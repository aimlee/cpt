import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 16, 1)
y = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
plt.plot(x, y)
plt.show()
