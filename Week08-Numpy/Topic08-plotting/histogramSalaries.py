import matplotlib.pyplot as plt
import numpy as np

#program to plot as histogram of salaries from question on on lab 
minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1) #so the random numbers are the same each time the program is run 
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
plt.hist(salaries)
plt.savefig("HistOfSalaries.png")