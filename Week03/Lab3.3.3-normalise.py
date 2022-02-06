#Program to read in a string and strips 
#gets rid of any unnecessary spaces .strip()
#it will convert all letters to lower case  .lower()
#it will also output the length of the original string and the new normalised one 

rawString =input("please enter a string:")
normalisedString = rawString.strip() .lower()
lengthOfRawString =len(rawString)
lengthOfNormalised = len(normalisedString)

print("That string normalised is :{}".format(normalisedString))
print("we reduced the input string from {} to {} characters" .format (lengthOfRawString, lengthOfNormalised))