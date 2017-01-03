# Minh Vu
# CS451
# email: minhvu@pdx.edu
##################

import math
def ReadFile(file,a):
	global NumOfLines	# l
	global NumOfAtt		# att
	global testlines
	global testatt
	inFile = open(file,'r')
	inputLines = []
	for line in inFile.readlines():
		line.split()
		inputLines.append(line)
	inFile.close()
	l = len(inputLines)
	att = line.count(',')+1
	if a == 0:														# If it is a training file
		NumOfLines = l
		NumOfAtt = att
	else:															# If it is a testing file
		testlines = l
		testatt = att
	data = [[0 for x in range(att+1)] for y in range(l)]
	for i in range(l):
		data[i] = inputLines[i].split(',')
	for i in range(l):
		for j in range(att):
			data[i][j] = int(data[i][j])
	return data
# This part is based on the pseudocode in the homework
def Init(a):
	if a == 0:														# If it is a training file		
		for i in range(NumOfLines):
			if data[i][0] == 1:
				N[1] = N[1] + 1
			else:
				N[0] = N[0] + 1
			for j in range(NumOfAtt):
				if data[i][j] == 1:
					F[data[i][0]][j] = F[data[i][0]][j] + 1
	else:															# If it is a testing file
		for i in range(testlines):
			if test[i][0] == 1:
				N_test[1] = N_test[1] + 1
			else:
				N_test[0] = N_test[0] + 1
			for j in range(testatt):
				if test[i][j] == 1:
					F_test[test[i][0]][j] = F_test[test[i][0]][j] + 1
# This part is based on the pseudocode in the homework 
def likelihood(c):	
	for i in range(2):
		L[i] = math.log(N[i] + 0.5) - math.log(N[0] + N[1] + 0.5)
		for j in range(1,NumOfAtt):
			s = F[i][j]
			if c[j] == 0:
				s = N[i] - s
			L[i] = L[i] + math.log(s + 0.5) - math.log(N[i] + 0.5)
	return L
# This part is based on the pseudocode in the homework
def classify(L):
	if L[1] > L[0]:
		return 1
	return 0
# Evaluate the values, compare between the classified list and the real class to calculate the accuracy, TNR, TPR	
def Evaluate(a):
	global acc
	global TNR
	global TPR
	if a == 1:								# If this is a testing file					
		for i in range(testlines):
			if test[i][0] == classified_test[i]:			# Compare the classified list with the real class
				acc = acc + 1								# Increase the accuracy for each right classified instance
				if test[i][0] == 0:							# If it is class 0
					TNR = TNR + 1							# Increase the TNR
				else:										# If it is class 1	
					TPR = TPR + 1							# Increase the TPR
	else:									# If this is a traing file (the whole below process is the same as above)
		for i in range(NumOfLines):
			if data[i][0] == classified[i]:
				acc = acc + 1
				if data[i][0] == 0:
					TNR = TNR + 1
				else:
					TPR = TPR + 1

#---------------------------------Main function----------------------------------#	
NumOfLines = 0			# Number of Lines for the training file
NumOfAtt = 0			# Number of Atrributes for each instance of the training file
testlines = 0			# Number of Lines for the testing file
testatt = 0				# Number of Attributes for each instance of the testing file 
acc = 0					# accuracy	
TNR = 0					# True Negative Rate
TPR = 0					# True Positive Rate
data = ReadFile("spect-orig.train.csv",0)				# create data based on the training file
test = ReadFile("spect-orig.test.csv",1)				# create data based on the testing file
# Create the list F,N and L
F = [[0 for x in range(NumOfAtt)] for y in range(2)]
N = [0 for x in range(2)]
L = [0 for x in range(2)]
classified = [-1 for x in range(NumOfLines)]
F_test = [[0 for x in range(testatt)] for y in range(2)]
N_test = [0 for x in range(2)]
classified_test = [-1 for x in range(testlines)]
# This part is to evaluate the training file
Init(0)													# Initialize values for F,N (of training file)
for i in range(NumOfLines):								# calculate the likelihood of each instance and classify it in the training file
	L = likelihood(data[i])
	case = classify(L)									# classify each instance
	classified[i] = case								# Put the result in a list
Evaluate(0)												# Evaluate the classify process, calculate accuracy,TNR,TPR
print "orig training %s/%s(%s) %s/%s(%s) %s/%s(%s)" %(acc,NumOfLines,float(acc)/float(NumOfLines),TNR,N[0],float(TNR)/float(N[0]),TPR,N[1],float(TPR)/float(N[1]))
# This part is to evaluate the testing file
acc = 0													# Reset Accuracy, TNR, TPR to zero
TNR = 0
TPR = 0
Init(1)													# Initialize values for F,N (of testing file)
for i in range(testlines):								# calculate the likelihood of each instance and classify it in the testing file
	L = likelihood(test[i])
	case = classify(L)
	classified_test[i] = case
Evaluate(1)
print "orig test %s/%s(%s) %s/%s(%s) %s/%s(%s)" %(acc,testlines,float(acc)/float(testlines),TNR,N_test[0],float(TNR)/float(N_test[0]),TPR,N_test[1],float(TPR)/float(N_test[1]))



