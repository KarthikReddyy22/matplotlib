import numpy as np
import matplotlib.pyplot as plt 

x = np.random.random(1000) * 100
y = np.random.random(1000) * 100

plt.scatter(x , y, c="red", marker="*", s=150, alpha=0.3)
plt.show() 