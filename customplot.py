import numpy as np
import matplotlib.pyplot as plt 

years = [2001 + x for x in range(17)]
weight = [76, 78, 79, 80, 82, 84, 85, 86, 89, 90, 92, 93, 94, 96, 94, 93, 93]

#plt.plot(years, weight, c='r', lw="2", linestyle="--")

ticks = list(range(70, 110, 2))

plt.title("Weight of a person", fontsize=20, fontname="Chalkboard")
plt.xlabel("Year")
plt.ylabel("weight")
plt.plot(years, weight, "r--", lw="2")
plt.yticks(ticks, [f"{x}Kg" for x in ticks])
plt.show()