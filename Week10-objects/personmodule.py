#Demonstration of a module
#Author: Orla Corry 
import datetime as dt # importing datetime for dob
def gethealthdata(person):
    print ("get health data:" , person['firstname'])

def displayperson(person):
    print(person)

if __name__ =='__main__':
    person1 = {
        'firstname': 'Orla',
        'lastname': 'Corry',
        'dob': dt.date(2010,1,1),
        'height': 180,
        'weight': 100
    }
displayperson(person1)
gethealthdata(person1)
