import load_data
import numpy as np
import matplotlib as plt
daten = load_data.load_data('activity.csv')
Heartrate = (daten['HeartRate'])
xachse = np.arange(1, 1805)
plt.pyplot.plot(xachse,Heartrate)
plt.pyplot.show()