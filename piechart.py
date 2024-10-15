import numpy as np
import matplotlib.pyplot as plt 

cars = ["BMW", "Ferrari", "Porsche", "Lambo"]
ratings = [5, 4.5, 4.2, 2]
explodes = [0, 0, 0, 0.2]
plt.pie(ratings, labels=cars,
        explode=explodes,
        autopct="%.2f%%", pctdistance=0.8, 
        startangle=90)
plt.show()