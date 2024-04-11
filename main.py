import load_data
import numpy as np
import matplotlib as plt
import sort
data = load_data.load_data('activity.csv')
#Liste mit den Keys
keysList = list(data.keys())
print(keysList)
#Listen mit den einzelnen Werten zu den Kategorien
PowerOriginal = data['PowerOriginal']
#Sortieren der Listen
PowerOriginal = sort.bubble_sort(PowerOriginal)
#plot
xaxis = np.arange(1, 1805)
plt.pyplot.plot(xaxis,PowerOriginal)
plt.pyplot.show()