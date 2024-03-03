#Prof Awasthi is doing some research in the field of environment. For some plotting 
#purpose, he has generated some data as:
#mu = 100,   sigma = 15, x = mu _ sigma * numpy.random.randn(10000)
#y = mu + 30 * np.random.randn(10000)

import numpy as np 
import matplotlib.pyplot as plt
mu=100
sigma=15
x=mu+sigma*np.random.randn(10000)
y=mu+30*np.random.randn(10000)
plt.hist([x,y],bins=100,histtype='barstacked')
plt.title('Reseach data Histogram')
plt.show()