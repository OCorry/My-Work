#Program that takes in a fload and rounds it down to an int
#Author Orla Corry 

#need to import math floor as Python doesnt have it automatically 
import math
numberToFloor =float(input("Enter a float number"))
flooredNumber = math.floor(numberToFloor)
print ("{} floored is {}" .format(numberToFloor, flooredNumber))
