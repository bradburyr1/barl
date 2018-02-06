import csv
import os
import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
   
w, h = 2, 11;
analysis_data = [[0 for x in range(w)] for y in range(h)]
#2: Number of times it was what the user was thinking
#3: number of times it was correctly guessed
#4: how often it was predicted, right or wrong
   
#Open the CSV file for train data
with open('confusion.csv', 'rt') as csvfile:
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
h2 = 11
nums = [0 for x in range(h2)]
names = [0 for x in range(h2)]
j = 0
for x in range(11):
	#print(analysis_data[x][1])
	nums[x] = analysis_data[x][1]
	names[x] = analysis_data[x][0]
	j += 1
#print(real)
y_pos = np.arange(len(analysis_data))
 
plt.barh(y_pos, nums, align='center', alpha=0.5)
plt.yticks(y_pos, names)
plt.ylabel('')
plt.title('How often the program confused the website with a competitor')
plt.show()