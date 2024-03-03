#first 10 terms of fibonacci series are stored in a list namely fib
#  fib = [0,1,1,2,3,5,8,13,21,34]
#WAP to plot fibonacci terms and their square root with two separate line on same plot
import matplotlib.pyplot as plt
import numpy as np
fib=[0,1,1,2,3,5,8,13,21,34]
sqfib=np.sqrt(fib)
fib=[0,1,1,2,3,5,8,13,21,34]
sqfib=np.sqrt(fib)
plt.figure(figsize=(10,7))
plt.plot(range(1,11),fib,'co',markersize=5,
linestyle="solid",markeredgecolor='r')
plt.plot(range(1,11),sqfib,'k+',markersize=7,
linestyle="solid",markeredgecolor='r')
plt.show()