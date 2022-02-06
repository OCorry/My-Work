#Why does the expression below cause an error:
    #message = 'I have eaten ' +99 + 'burritos'
#Need to change the 99 from an int to a str 

burritos = 99
message = (("I have eaten " + str(burritos) + " burritos"))
print (message)

