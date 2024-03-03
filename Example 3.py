import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.,10,0.1)
a = np.cos(x)
b = np.sin(x)
plt.plot(x,a,'b')
plt.plot(x,b,'r')
plt.show()
