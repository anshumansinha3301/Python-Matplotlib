#Write a program to plot scattering graph taking a random distribution in X and Y
#(both with shape as (100,)having randomly generated integers)
#and plotted against each other.

import numpy as np
import matplotlib.pyplot as plt
X=np.random.randint(1,100,size=(100,))
Y=np.random.randint(1,100,size=(100,))
plt.scatter(X,Y,color='r')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()