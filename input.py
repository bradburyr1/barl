import csv
import os
import numpy as np
from sklearn import svm
   
answer = input("In this experiment, we'll be asking you a series of 15 questions related to tech companies. These questions are either 'yes' or 'no'. At the end, the program will try to guess which company you were thinking about. If it's right, you'll tell it so with a 'yes'. If it's wrong, you'll say 'no', and you'll have an opportunity to tell it which company you were thinking of. Is this ok? Y/n: ")
if (answer == 'Y' or answer == 'y'):

	answerArray = [];
	i = 1
	with open('questions.txt', 'r') as q:
		for x in q:
			ans = input("\n"+x)
			
			if (ans == 'Y' or ans == 'y'):
				print("You replied 'yes' to question " + str(i))
				answerArray.append(ans)
			elif(ans == 'N' or ans == 'n'):
				print("You replied 'no' to question " + str(i))
				answerArray.append(ans)
				

			i += 1
		
	
	#2-dim train data array
	w, h = 15, 16;
	train_data = [[0 for x in range(w)] for y in range(h)]

	#train target array
	h2 = 16
	train_target = [0 for x in range(h2)]

	#train target with numbers instead of numbers
	tt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

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
			
	answerArray = [w.replace('y', '1') for w in answerArray]
	answerArray = [w.replace('n', '0') for w in answerArray]
	
	answerArray = np.reshape(answerArray, (15, 1)).T
			
	#print(train_data)
	#train the svm classifier
	s = svm.SVC(kernel = 'rbf') # 'rbf', 'poly', 'linear', 'sigmoid', etc.
	s.fit(train_data, tt)
	
	#you are ready to predict/test
	decisions = s.predict(answerArray)

	#print(decisions)

	print("\nPrediction: " + str(train_target[decisions[0]-1]))
	
	answerArray = np.append(answerArray, str(train_target[decisions[0]-1]))
	
	ans = input("Is it right?\n")
	
	ans = ans.replace('y', '1')
	ans = ans.replace('n', '0')
	
	answerArray= np.append(answerArray, ans)

	with open('test_data.csv', 'a', newline='\n') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(answerArray)
			
elif (answer == 'N' or answer == 'n'):
	print("You said 'no'.")
