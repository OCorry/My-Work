#Write a program that stores a student name and a list of her courses and grades in a dict
#The program should then output her data
#Author: Orla Corry 

student ={ #using {to open the dict
    "name" : "Mary", #dict
    "modules" : [       #using [ to open the list of dicts
        {"courseName" : "Programming",
        "grade": 45         #dict within a dict (using {} to show start and finish of 'sub dict')
        },
        {"courseName" :"History",
        "grade" : 99        #dict within a dict (using {} to show start and finish of 'sub dict')
        }
    ]   #using ] to close the list of dicts
}       #using } to close the  original Student dict 

print ("Student: {}" .format(student["name"]))
for module in student ["modules"]:
    print (" \t {} \t : {}" .format(module["courseName"], module["grade"]))


