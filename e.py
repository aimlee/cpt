import numpy as np
import scipy.optimize as so

x = np.arange(1, 30, 1)
y = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
m = so.minimize(y)
print m
# file_w = open('submission-2.txt', 'w')
# str1 = ' '.join(str(round(x, 2)) for x in c)
# file_w.write(str1)
# file_w.close()
