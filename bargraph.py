import csv
import os
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
   
w, h = 4, 16;
analysis_data = [[0 for x in range(w)] for y in range(h)]
#2: Number of times it was what the user was thinking
#3: number of times it was correctly guessed
#4: how often it was predicted, right or wrong
   
#Open the CSV file for train data
with open('data_analysis.csv', 'rt') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	i = 0
	#Loop through the rows of the file
	for row in reader:
		k = 0
		#Loop through the elements of each row, assign to arrays
		for x in range(len(row)):
			analysis_data[i][x] = row[k]
			k += 1
		i += 1
			
# print(analysis_data[0][0])
# print(analysis_data[0][1])
# print(analysis_data[0][2])
# print(analysis_data[0][3])
h2 = 16
real = [0 for x in range(h2)]
names = [0 for x in range(h2)]
j = 0
for x in range(16):
	#print(analysis_data[x][1])
	real[x] = analysis_data[x][1]
	names[x] = analysis_data[x][0]
	j += 1
#print(real)
y_pos = np.arange(len(analysis_data))
 
plt.barh(y_pos, real, align='center', alpha=0.5)
plt.yticks(y_pos, names)
plt.ylabel('Number Times')
plt.title('Number of times that users thought about the website')
plt.show()

#Pie chart by type 
# social = [analysis_data[0][0], analysis_data[1][0], analysis_data[2][0], analysis_data[3][0], analysis_data[4][0]]
# search = [analysis_data[5][0], analysis_data[6][0], analysis_data[7][0]]
# store = [analysis_data[8][0], analysis_data[9][0], analysis_data[10][0], analysis_data[11][0]]
# stream = [analysis_data[12][0], analysis_data[13][0], analysis_data[14][0], analysis_data[15][0]]

socialTot = int(analysis_data[0][1]) + int(analysis_data[1][1]) + int(analysis_data[2][1]) + int(analysis_data[3][1]) + int(analysis_data[4][1])
searchTot = int(analysis_data[5][1]) + int(analysis_data[6][1]) + int(analysis_data[7][1])
storeTot = int(analysis_data[8][1]) + int(analysis_data[9][1]) + int(analysis_data[10][1]) + int(analysis_data[11][1])
streamTot = int(analysis_data[12][1]) + int(analysis_data[13][1]) + int(analysis_data[14][1]) + int(analysis_data[15][1])

plt.rcParams.update({'font.size': 18})

labels = "Social", "Search", "E-Commerce", "Stream"
explode = (0, 0, 0, 0)  # explode any slice you want
sizes = [socialTot, searchTot, storeTot, streamTot]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()