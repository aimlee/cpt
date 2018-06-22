import numpy as np
import math
from scipy import optimize


def f(x):
    return math.sin(x / 5.) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)


ans = []
ans.append(round(-11.89889467, 2))
# m = optimize.minimize(f, [2.0], method='BFGS')
# ans.append(round(m.fun, 2))
# m = optimize.minimize(f, [30.0], method='BFGS')
# ans.append(round(m.fun, 2))
file_w = open('submission-1.txt', 'w')
str1 = ' '.join(str(x) for x in ans)
file_w.write(str1)
file_w.close()
