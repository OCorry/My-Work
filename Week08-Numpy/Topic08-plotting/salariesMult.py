#messing with plots
#program that adds 5% to each salary 
#Author: Orla Corry


import numpy as np
#save absolute values as vairiables from the beginning
np.random.seed(1) #used so that the random numbers generated are the same each time program is run 
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
salariesMult = salaries *1.5 #adding 5% to each salary - this will print as a float 
newSalaries = salariesMult.astype(int)  #this will print as and int
print (salariesMult)
print (newSalaries)