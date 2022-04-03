#messing wtih init
#Author: Orla Corry 

class Person:
    def __init__ (self, first, last):
        self.firstname= first
        self.lastname =last

    def fullname(self):
        return self.firstname + ' ' + self.lastname


person1 = Person('Orla', 'Corry')
print (person1.firstname)

print(person1.fullname())