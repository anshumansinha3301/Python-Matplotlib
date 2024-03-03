#Consider the arrays of previous example and create an array C that stores the log10
#values of the elements in the array A.
import matplotlib.pyplot as plt
import numpy as np

A=np.arange(1,20,1.25)
B=np.log(A)
C=np.log10(A)
plt.plot(A,B,'ro')
plt.plot(A,C,'b^')
plt.xlabel('Random Values')
plt.ylabel('Logarithm Values')
plt.show()