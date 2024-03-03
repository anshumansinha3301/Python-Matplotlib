#Create an array, A, in the range 1 to 20 with values 1.25 apart. Another array B, contains
#the log values of elements of A
#WAP to create a scatter plot of first vs second array(array A vs B)

import matplotlib.pyplot as plt
import numpy as np
A = np.arange(1,20,1.25)
B = np.log(A)
plt.plot(A,B,'ro')
plt.xlabel('Random Values')
plt.ylabel('Logarithm Values')
plt.show()