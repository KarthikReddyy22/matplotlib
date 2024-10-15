import numpy as np
import matplotlib.pyplot as plt 

cars = ["BMW", "Ferrari", "Porsche", "Lambo"]
ratings = [5, 4.5, 4.2, 2]

plt.bar(cars, ratings, color="red", width=0.5)
plt.show()