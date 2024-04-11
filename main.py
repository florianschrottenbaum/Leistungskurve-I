#Imports
import load_data
import numpy as np
import matplotlib as plt
import sort
#import data from load_data
data = load_data.load_data('activity.csv')
#import PowerOriginallist
PowerOriginal = data['PowerOriginal']
#sort poweroriginal
PowerOriginal = sort.bubble_sort(PowerOriginal)
#plot
xaxis = np.arange(1, 1805)
plt.pyplot.plot(xaxis,PowerOriginal)
#plotoptions
xaxisticks=[]
labelsxaxis=[]
for counter in range(0,len(PowerOriginal),300):
    xaxisticks.append(counter)
    labelsxaxis.append(str(counter/60))
plt.pyplot.xticks(xaxisticks, labelsxaxis)
plt.pyplot.xlabel('Time [min]')
plt.pyplot.ylabel('Power [W]')
plt.pyplot.title('Power-Curve')
#saving the plot
plt.pyplot.savefig('figures/PowerOriginal.png')
#showing Plot
plt.pyplot.show()