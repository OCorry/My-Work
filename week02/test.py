weight = float(input("Enter your weight:"))
height = float(input("Enter your height:"))
bmi = weight /(height/100)**2
print ('{} equals {} divided by {} '.format(bmi, weight, height/100))