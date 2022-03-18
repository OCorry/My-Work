#messing with plots
#program that adds makes a list of 10 random nos from 20000 to 80000 and random salaries are the same each time
#Author: Orla Corry


import numpy as np
#save absolute values as vairiables from the beginning
np.random.seed(1) #used so that the random numbers generated are the same each time program is run 
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5000 #making another array of numbers that has salaries plus 5000

print (salaries)