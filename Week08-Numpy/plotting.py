#messing with matplotlib
#Author Orla Corry 

import numpy as np
import matplotlib.pyplot as plt

xpoints =np.array(range(1,101))
ypoints = xpoints*xpoints

plt.plot(xpoints, ypoints)
#plt.show() #commented this out to allow to save below

#to save:
#plt.savefig('messingwithplots.png')

#to add a lable 
plt.plot(xpoints, ypoints, label= "xsquared")
plt.plot (xpoints, xpoints, label="straight", color ="pink") #to add another plot 
plt.legend() #call the legend 

randompoints = np.random.randint(1, 10000, 100)
plt.scatter(xpoints, randompoints, label="random")
plt.show()