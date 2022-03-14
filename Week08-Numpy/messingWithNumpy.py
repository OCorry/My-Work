#messing with numpy
#Author: Orla Corry 

import numpy as np
listOfNumbers =[1,2,3,4,5,6]  #prints out list with commas between numbers
numbers = np.array([1,2,3,4,5]) #the Numpy array prints out the array differntly to a list - has no commas

#numpy allows you to add a number to a list
#numbers= numbers + 3

#or multiply a list by a number
#numbers = numbers*3

#or multiply with another array 
numbers = numbers* np.array([5,4,3,2,1])
print(listOfNumbers)
print(numbers)

#Random Number Geneerator:
#randomNumbers = np.random.randint(100,200,5) #between 100 and 200 and i want 5 random numbers
#randomNumbers = np.random.randint(600,1000,10)#between 600 and 1000 and i want 10 random numbers
#print(randomNumbers)

#To get a normal distribution around the number 10
randomNumbers = np.random.normal(size = 100)
print(randomNumbers)

