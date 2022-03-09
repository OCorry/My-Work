#program to overwrite the file with that number 
#Author: Orla Corry 

filename = "count.txt"
def writeNumber(number):
    with open(filename, 'wt') as f:
        #write takes a srtig so we need to convert
        f.write(str(number))

#test it 
writeNumber(3)
#3 is now in the count.txt file instead of 0

