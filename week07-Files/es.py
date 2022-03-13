#Write a program that reads in a text file and outputs the number of e's it contains
#Author: Orla Corry 

#import sys #importing sys.argv will allow to take the filename from an argument on the command line

#import sys

filename = "moby-dick.txt"
with open(filename, "rt") as f:
    data = f.read()
    print(data)
