#making plots 
#Author: Orla Corry 

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints*xpoints #x squared

plt.plot(xpoints, ypoints)
plt.savefig("plotting1")


