#rounds a float 
#seems to be rounding to either an odd or even number for me, which ever is closer
#Using input to read in 
#Author: Orla Corry 

numberToRound =float(input("Enter a float number"))
roundedNumber = round(numberToRound)
print ('{} rounded is {}' .format(numberToRound, roundedNumber))