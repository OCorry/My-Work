#Program to divide one numbr by another 
#Need to convert X from a str to int when reading in 
#Need to convert Y from a str to a int when reading in 
#Author: Orla Corry 

X = int(input("enter first number"))
Y = int(input("Enter second number"))
answer = int(X//Y) #// gives the int division 
remainder = int(X%Y) # % gives the remainder

print("{} divided by {} is {} with remainder {}" .format(X, Y, answer, remainder))
