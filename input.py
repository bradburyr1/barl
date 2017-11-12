import csv
import os
   
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
	
	
	answerArray = [w.replace('y', '1') for w in answerArray]
	answerArray = [w.replace('n', '0') for w in answerArray]

	#with open('test_data_insert.csv', 'a', newline='\n') as csv_file:
	with open('test_data_insert.csv', 'w') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(answerArray)
		
	import prediction
			
elif (answer == 'N' or answer == 'n'):
	print("You said 'no'.")
