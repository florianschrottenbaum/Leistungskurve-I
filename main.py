#Imports
import load_data
import numpy as np
import matplotlib as plt
import sort
data = load_data.load_data('activity.csv')
#import PowerOriginallist
PowerOriginal = data['PowerOriginal']
#sort poweroriginal
PowerOriginal = sort.bubble_sort(PowerOriginal)
#plot
xaxis = np.arange(1, 1805)
plt.pyplot.plot(xaxis,PowerOriginal)
#plotoptions
xaxisticks=[0,300,600,900,1200,1500,1800]
labelsxaxis = ['0','5','10','15','20','25','30']
plt.pyplot.xticks(xaxisticks, labelsxaxis)
plt.pyplot.xlabel('Time [min]')
plt.pyplot.ylabel('Power [W]')
#showing Plot
plt.pyplot.show()
plt.pyplot.savefig('figures/PowerOriginal.png')