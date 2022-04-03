#messing with objects
#Author: Orla Corry 

from os import name


class nameofclass:
    name =""  #attribute
    last ="" #attribute 
    def getfullname(self):
        return self.name + ' ' + self.last #function 
    

inst =nameofclass()
inst2 = nameofclass()

inst.name = 'Orla'
inst2.last = 'Corry'
person = inst
inst.last = 'Blogs'
#print(person.name)
print(person.getfullname()) #will show error as there is no attribute last in object - so define the attributes above