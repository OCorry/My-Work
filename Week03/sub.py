#Program to subtract one number from another by reading in 2 numbers
#X is a str so need to convert to an int when reading in 
#Y is a str so need to convert to an int when reading in 
#Author Orla Corry 

X = int(input("Enter First Number:"))
Y = int(input("Enter Second Number:"))
answer = X - Y
print ('{} minus {} is {}' .format (X, Y, answer))