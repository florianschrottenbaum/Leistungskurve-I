import numpy as np
import matplotlib as plt
def plotcreation(signal):
    #plot
    xaxis = np.arange(1, len(signal)+1)
    plt.pyplot.plot(xaxis,signal)
    #plotoptions
    xaxisticks=[]
    labelsxaxis=[]
    for counter in range(0,len(signal),300):
        xaxisticks.append(counter)
        labelsxaxis.append(str(counter/60))
    plt.pyplot.xticks(xaxisticks, labelsxaxis)
    plt.pyplot.xlabel('Time [min]')
    plt.pyplot.ylabel('Power [W]')
    plt.pyplot.title('Power-Curve')
    #saving the plot
    plt.pyplot.savefig('figures/PowerCurve.png')
    #showing Plot
    plt.pyplot.show()
