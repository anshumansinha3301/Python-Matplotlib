#Write a program to plot a scatter graph taking three random distributions in X1,Y1
#(both with shape as (250,)having randomly generated integers)
#and plotted against each other with vary sizes.
import numpy as np
import matplotlib.pyplot as plt
#random distributions X1 and Y1
X1 = np.random.randint(1, 100, size=(250,))
Y1 = np.random.randint(1, 100, size=(250,))
#varying sizes and colors
sizes = np.random.choice(range(10, 100), size=(250,))
colors = np.random.rand(250, 3)  # Random RGB colors
plt.scatter(X1, Y1, s=sizes, c=colors, alpha=0.7)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Varying Sizes and Colors")
plt.show()
