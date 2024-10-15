import numpy as np
import matplotlib.pyplot as plt 

ages = np.random.normal(20, 1.5, 1000)

plt.boxplot(ages)
plt.show()