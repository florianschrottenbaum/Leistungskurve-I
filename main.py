import load_data
import numpy as np
import matplotlib as plt
import sort
data = load_data.load_data('activity.csv')
#Liste mit den Keys
keysList = list(data.keys())
print(keysList)
#Listen mit den einzelnen Werten zu den Kategorien
Duration = data['Duration']
Distance = data['Distance']
OriginalPace = data['OriginalPace']
HeartRate = data['HeartRate']
Cadence = data['Cadence']
PowerOriginal = data['PowerOriginal']
CalculatedPace = data['CalculatedPace']
CalculatedStrideLength = data['CalculatedStrideLength']
CalculatedAerobicEfficiencyPace = data['CalculatedAerobicEfficiencyPace']
CalculatedAerobicEfficiencyPower = data['CalculatedAerobicEfficiencyPower']
CalculatedEfficiencyIndex = data['CalculatedEfficiencyIndex']

xaxis = np.arange(1, 1805)
#plt.pyplot.plot(xaxis,HeartRate)
#plt.pyplot.show()