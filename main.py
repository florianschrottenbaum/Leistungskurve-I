#Imports
import load_data
import sort
import plot
#import data from load_data
data = load_data.load_data('activity.csv')
#import PowerOriginallist
PowerOriginal = data['PowerOriginal']
#sort poweroriginal
PowerOriginal = sort.bubble_sort(PowerOriginal)
#plot creation and save
plot.plotcreation(PowerOriginal)