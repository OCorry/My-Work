#Write a program that reads in a text file and outputs the number of e's it contains
#I am assuming that the client is looking for the number of lower case e's as it is lowecase in the request and they dont specify
#Author: Orla Corry 

#import sys #importing sys.argv will allow to take the filename from an argument on the command line

import sys 

    #with open(sys.argv[1], 'rt') as f:
    #data = f.read()  #using f.read() as a variable so it can be changed more easily 
    #print (data)
    #https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python
    #I did this simply to make sure the file would read before moving on to researching the letter counting part of the task

def letterFrequency(f, letter): #defining the function
    
    with open(sys.argv[1], 'rt') as f: #open the file in read text mode 
 
    # store content of the file in a variable
         numberOfEs = f.read()
 
         return numberOfEs.count(letter)  # calling the function
 
 
# calling the function to print out the number of e's in the text 
print(letterFrequency('f', 'e')) #dont need to specifically define that it's lower case here as Python is case sensitive anyway 

#https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/