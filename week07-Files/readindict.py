#program to read in a dict object from a file
#Author: Orla Corry 


import json
filename ="testdict.json"

def readDict():
    #this will throw an error if the file doesnt exist 
    #it should readily just return an empty dict
    #we can do this later
    with open(filename) as f:
        return json.load(f)

#test the function 

somedict =readDict()
print(somedict)