import csv
import numpy as np
from sklearn import svm

#2-dim train data array
w, h = 15, 16;
train_data = [[0 for x in range(w)] for y in range(h)]

#train target array
h2 = 16
train_target = [0 for x in range(h2)]

#train target with numbers instead of numbers
tt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

#2-dim train data array
w, h = 15, 1;
test_data = [[0 for x in range(w)] for y in range(h)]

#Open the CSV file for train data
with open('training_data_no_labels.csv', 'rt') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	i = 0
	#Loop through the rows of the file
	for row in reader:
		k = 0
		#Loop through the elements of each row, assign to train_data
		for x in range(len(row)):
			train_data[i][x] = row[k]
			#print (train_data[i][x])
			k += 1
		i += 1
		
#Open CSV for train target
with open('training_targets.csv', 'rt') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	i = 0
	#Loop through the rows of the file
	for row in reader:
		#print(len(row))
		k = 0
		#Loop through the elements of each row, assign to train_data
		for x in range(len(row)):
			train_target[i] = row[0]
			#print (train_target[i])
			k += 1
		i += 1
		
#Open the CSV file for test data
with open('test_data_insert.csv', 'rt') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	i = 0
	#Loop through the rows of the file
	for row in reader:
		k = 0
		#Loop through the elements of each row, assign to test_data
		for x in range(len(row)):
			test_data[i][x] = row[k]
			#print (test_data[i][x])
			k += 1
		i += 1
		
#print(train_data)
#train the svm classifier
s = svm.SVC(kernel = 'rbf') # 'rbf', 'poly', 'linear', 'sigmoid', etc.
s.fit(train_data, tt)

#you are ready to predict/test
decisions = s.predict(test_data)

#print(decisions)

print("\n Prediction: " + str(train_target[decisions[0]-1]))
