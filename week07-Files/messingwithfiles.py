#create a file called count.txt and put a 0 in it
#author: Orla Corry



filename = "count.txt"
with open(filename, 'wt') as f:
    f.write("0")

print(filename)

filename ="count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number
#test it
num = readNumber()
print(num)



