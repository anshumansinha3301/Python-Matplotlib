#Marks is a list that stores marks of a student in 10 units tests.
#Write a program to plot the student's performance in these 10 units tests.
import matplotlib.pyplot as plt
week=[1,2,3,4,5,6,7,8,9,10]
Marks =[12,10,10,15,17,25,12,22,35,40]

#plotting line graph
plt.plot(week, Marks)
plt.xlabel('week')
plt.ylabel('Unit Test Marks')
plt.show()
