#Write a program that puts 10 randim numbers into a queue(list)
    #the program should then output all the values in the queue 
    #then take the numbers from the queue one at a time, print it and the current numbers still in the queue

#Author: Orla Corry 

import random #random is not built into python
queue =[] #list
numberOfNumbers = 10
rangeTo = 100 #up to 100

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

print("queue is {}" .format(queue))

while len(queue) != 0:

    currentNumber = queue.pop(0)
    print("current Number is {} and the queue is {}" .format(currentNumber, queue))

print ("the queue is now empty")
