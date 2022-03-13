import json
filename = "storedata.json"

students = []

def displayMenu ():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View Student")
    print("\t(s) save")
    print("\t(l) load")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/l/q):").strip()

    return choice 

def doAdd(students):
    currentStudent ={}
    currentStudent ["name"] = input("enter name:")
    currentStudent ["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    modules =[]
    moduleName =input("\tEnter the first module name (blank to quit):").strip()

    while moduleName !="":
        module ={}
        module["name"] = moduleName
        module["grade"] =int(input("\t\tEnter grade:"))
        modules.append(module)

        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules 

def displayModules(modules):
    print("\tName   \tGrade")
    for module in modules:
        print("\t{} \t{}" .format(module["name"], module["grade"]))
    

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);

def doSave(students):
    with open(filename, "wt") as f:
        json.dump(students, f)
    print("saved")

def doLoad():
    with open (filename, "rt") as f:
        return json.load(f)
    

#main program
#students is now a global variable 
#
choice = displayMenu()
while choice != 'q':
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == "s":
        doSave(students)
    elif choice == "v":
        doView(students)
    elif choice == "l":
        students = doLoad()

    else:
        print("invalid choice")
    choice = displayMenu()

