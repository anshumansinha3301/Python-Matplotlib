#WAP to plot a line chart to depict the changing weekly onion prices for four weeks
import matplotlib.pyplot as plt
week=[1,2,3,4]
prices=[40,80,100,50,]#onion prices

#plotting line graph
plt.plot(week,prices)
plt.xlabel('week')
plt.ylabel('onion prices(Rs.)')
plt.show()