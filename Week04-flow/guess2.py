numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too Low")
    else:
        print("too high")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was" , numberToGuess)