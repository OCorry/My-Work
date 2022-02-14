#program to gengerate a random number between 0 and 100 to guess
#author: Orla Corry 

guess = int(input("Please guess the number:"))
import random
numberToGuess = random.randint (1, 100)

while guess != numberToGuess:
    if guess < numberToGuess:
        print("too Low")
    else:
        print("too high")
    guess = int(input("Please guess again:"))


print("Well done! Yes the number was" , numberToGuess)