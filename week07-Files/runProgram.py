#A program to count how many times a program is run 
#Author: Orla Corry 

filename = "count.txt"
def readNumber():
    with open (filename) as f:
        number =int(f.read())
        return number

def writeNumber(number):
    with open (filename, 'wt') as f:
        #write takes a string so we neeed to convert
        f.write(str(number))

#main
num = readNumber()
num += 1
print("we have run this program {} times" , format(num))
writeNumber(num)