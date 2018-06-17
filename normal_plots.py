import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

# Create plots for normal distributions of standard devitions 1/4 , 1/2 , 1 , 2

mu = 0
variance1 = 1/4
variance2 = 1/2
variance3 = 1
variance4 = 2
sigma1 = math.sqrt(variance1)
sigma2 = math.sqrt(variance2)
sigma3 = math.sqrt(variance3)
sigma4 = math.sqrt(variance4)
x1 = np.linspace(mu - 3*sigma1, mu + 3*sigma1, 100)
x2 = np.linspace(mu - 3*sigma2, mu + 3*sigma2, 100)
x3 = np.linspace(mu - 3*sigma3, mu + 3*sigma3, 100)
x4 = np.linspace(mu - 3*sigma4, mu + 3*sigma4, 100)
plt.plot(x1,mlab.normpdf(x1, mu, sigma1))
plt.plot(x2,mlab.normpdf(x2, mu, sigma2))
plt.plot(x3,mlab.normpdf(x3, mu, sigma3))
plt.plot(x4,mlab.normpdf(x4, mu, sigma4))
plt.show()
