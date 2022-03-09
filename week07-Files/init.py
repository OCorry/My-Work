#program to check if a file exisis and check if the path is an existing regular file or not 
#https://www.geeksforgeeks.org/python-os-path-isfile-method/

import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print("file does not exist")
    


#def readNumber():
    #try:
        #with open(filename) as f:
            #number = int(f.read())
            #return number
    #except IOError:
        #return 0