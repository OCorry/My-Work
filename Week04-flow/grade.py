#This is a program that reads in a students pecentage   
#and prints out the corresponding grade

#Author Orla Corry 

percentage = float(input("Enter the percentage"))

#Be careful with ands and ors
if (percentage >= 0) or (percentage <= 100):
    print ("please enter a number between 0 and 100")
elif percentage < 40: #this is greater than 0
    print("Fail")
elif percentage < 50: #40-49
    print("Pass")
elif percentage < 60:#50-59
    print("Merit1")
elif percentage < 70: #60-69
    print("Merit20")
else:
    print ("Destinction") #70-100
