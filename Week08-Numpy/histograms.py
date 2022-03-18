#messing with histograms
#Author: Orla Corry 

import numpy as np
import matplotlib.pyplot as plt

'''
np.random.seed(1) #this makes sure that the same random data is used each time the program is run 
normData = np.random.normal(size = 10000)
plt.hist(normData)
plt.show()
'''  #this comments out lines of code 

#piecharts
fruit = np.array(["apples", "oranges", "Bananas"])
numbers = np.array([23, 77, 500])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()