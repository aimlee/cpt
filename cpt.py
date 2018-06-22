import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sts

norm_rv = sts.norm(0, 5)
sample = norm_rv.rvs(1000)

x = np.linspace(-25, 25, 1000)
pdf = norm_rv.pdf(x)

plt.plot(x, pdf, label='theoretical CDF')
plt.ylabel('$F(x)$')
plt.xlabel('$x$')
plt.hist(sample, normed=True)

x = [5, 10, 50]
a = np.array([])

for i in x:
    b = np.array([])
    for j in range(1000):
        sampleCurrent = norm_rv.rvs(i)
        b = np.append(b, np.mean(sampleCurrent))
    a = np.append(a, b)
a = a.reshape((3, 1000))

common_params = dict(
    range=(-5, 5),
    normed=True,
    histtype='step',
    label='5'
)

plt.title('Default')

plt.hist(a[0], **common_params)
common_params['label'] = '10'
plt.hist(a[1], **common_params)
common_params['label'] = '50'
plt.hist(a[2], **common_params)
plt.legend()


plt.show()
