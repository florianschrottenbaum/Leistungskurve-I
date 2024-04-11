import load_data
import numpy as np
import matplotlib as plt
data = load_data.load_data('activity.csv')
#print(data)
keysList = list(data.keys())
print(keysList)

HeartRate = (data['HeartRate'])










xaxis = np.arange(1, 1805)
#plt.pyplot.plot(xaxis,HeartRate)
#plt.pyplot.show()
