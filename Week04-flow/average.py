#program that keeps reading numbers until the user enters a 0
    #program should append each of them to a list
#program should then print out each of the numbers entered and the average of them

#author: Orla Corry 

numbers = []

number = int(input("enter number (0 to quit):"))

while number != 0:
    numbers.append(number)

    #read the next number and check if 0
    number = int(input("enter a number (0 to quit):"))

for value in numbers:
    print(value)

#average is to be a float
average = float(sum(numbers)) / len(numbers)
print("the average is {}" .format(average))