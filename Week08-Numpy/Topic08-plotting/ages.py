#program that makes a list of ages and has the same number of random values as salaries
#ranges 21:65
#make a scatter plot of this data 
#Author: Orla Corry 


import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000 
numberOfEntries = 100
low = 21
high = 65
size =numberOfEntries
np.random.seed(1) #random numbers are the same each time to make it easier to debug

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low, high, size) #absolute values set at top 

plt.scatter(ages, salaries) #this will be random
#plt.show() #commenting this out so that both the scatter and the line will print on the same plot

#add another line to existing plot that shows y=xsquared

xpoints = np.array(range(1,101))
ypoints =xpoints*xpoints 

plt.plot(xpoints, ypoints, color = "yellow")
plt.show()


