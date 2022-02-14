#program that keeps prompting user to guess a number until the user guesses the right number
#author: Orla Corry

numberToGuess = 30

guess =int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("wrong")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was " , numberToGuess)
