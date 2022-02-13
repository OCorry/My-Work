#Program that asks the user to input a number and the program will tell the user if the number is odd or even

number = int(input("enter an integer"))

if (number % 2 )== 0:
    print ("{} is an even number" .format(number))
else:
    print ("{} is an odd nunber" .format(number))