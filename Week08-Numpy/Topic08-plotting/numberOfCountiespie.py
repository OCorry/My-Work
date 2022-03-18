#a program that has a list of counties and shows them on a pie chart 
#pick from 5 counties
#make some counties appear more than others 
#this will demonstrate making a pie plot of the unique occurences of values in an array 
#Author: Orla Corry 


import numpy as np
import matplotlib.pyplot as plt

#make an array of occurences
possibleCounties = ["Mayo", "Galway", "Roscommon", "Dublin", "Donegal"]
#pick 100 randomly from possible counties with the frequence set in p

counties =np.random.choice(
    possibleCounties ,
    p=[0.1, 0.3, 0.2, 0.12, 0.28] ,
    size =[100])

#we need the number of occurrences of each county 
#this returns a tuple of the unique values and how ,many times they appear 
unique, counts =np.unique(counties, return_counts=True)
#we can now put this into a pie plot 
plt.pie(counts, labels= unique)
plt.savefig("numberofcounties.png")
