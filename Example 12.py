#three days prices are shown below:
    #Day 1 = [74.25,76.06,69.5,72.55]
    #Day 2 = [56.03,68.71,62.89,56.42]
    #Day 3 = [59.3,72.07,77.65,66.46]
    
import matplotlib.pyplot as plt
Day1=[74.25,76.06,69.5,72.55]
Day2=[56.03,68.71,62.89,56.42]
Day3=[59.3,72.07,77.65,66.46]
finlist=[Day1,Day2,Day3]
plt.boxplot(finlist,labels=['Day1','Day2','DAy3'])
plt.title("prices")
plt.show()