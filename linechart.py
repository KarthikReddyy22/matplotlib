import numpy as np
import matplotlib.pyplot as plt 

years = [2001 + x for x in range(17)]
weight = [76, 78, 79, 80, 82, 84, 85, 86, 89, 90, 92, 93, 94, 96, 94, 93, 93]

#plt.plot(years, weight, c='r', lw="2", linestyle="--")
plt.plot(years, weight, "r--", lw="2")
plt.show()