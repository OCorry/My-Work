#testing that variables are of the correct type
#Author: Orla Corry

#Test that age is an int
Age = 30

#Test that distance is a float
Distance = 1.2

print (type(Age))
print (type(Distance))

#Test that Hello is a str
"Hello" 
print (type("hello"))

#Test that mylist is a list
mylist =["red", "orange", "yellow"]
print (type(mylist))

#Test that A > B is a bool 

A = 4
B = 5
A > B
print (type(A > B))


i = 3
fl = 3.5
isa = True
memo = "how now Brown Cow"
lots = []

print("variable {} is of type: {} and value: {}" .format("i", type(i), i))
print("variable {} is type: {} and value: {}" .format("fl",type(fl), fl))
print ("variable {} is type: {} and value {}" .format("isa", type(isa), isa))
print ("variable {} is type: {} and value: {}" .format("memo", type(memo), memo))
print ("variable {} is type: {} and value: {}" .format("lots", type(lots), lots))