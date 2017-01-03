# Student: Minh Vu
# Email: minhvu@pdx.edu
#---------------------------

import string
import random
import  time
def ReadInput(file):					# Read the input file
	inFile = open(file,'r')
	inputLines = []
	for line in inFile.readlines():
		line.split()
		inputLines.append(line)
	inFile.close()
	global numGuests
	numGuests = GetNumGuests(inputLines)
	data = [[0 for x in range(numGuests)] for y in range(numGuests)]

	for i in range(1,numGuests+1):
		data[i-1] = inputLines[i].split(' ')
	for a in range(numGuests):
		for b in range(numGuests):
			data[a][b] = int(data[a][b])
	return data
def GetNumGuests(value):
	numGuests = string.atof(value[0])
	numGuests = int(numGuests)
	return numGuests
def IdentifyGender(n):					# identify the gender of guest
	global numGuests
	if n <= numGuests/2-1 and n >= 0:
		gender = 0      # female
	else:
		gender = 1		# male
	return gender
def h(p1,p2,data):
	return data[p1][p2]
def RandomTable(table):			# Arrange all the guests randomly
	global numGuests
	list1 = [x for x in range(numGuests)]
	list2= []
	i = 0
	b = 0
	while(i < numGuests):
		number = random.choice([x for x in list1 if x not in list2])
		list2.append(number)
		if i < numGuests/2:
			table[0][i] = int(number)
		else:
			table[1][b] = int(number)
			b = b + 1
		i = i + 1
	return table
def Score(table,aSide,refer):  # Calculate the total score of the table
	score = 0
	adjScore = AdjacentScore(table,aSide,refer)
	oppScore = OppositeScore(table,aSide,refer)
	score = adjScore + oppScore
	return score
def AdjacentScore(table,aSide,refer):      # Calculate the Adjacent Score
	score = 0
	for i in range(2):
		for j in range(aSide-1):
			if IdentifyGender(table[i][j]) != IdentifyGender(table[i][j+1]):
				score = score + 1
			score = score + h(table[i][j],table[i][j+1],refer) + h(table[i][j+1],table[i][j],refer)
	return score
def OppositeScore(table,aSide,refer):	  # Calculate the Opposite Score	
	score = 0
	for i in range(aSide):
		if IdentifyGender(table[0][i]) != IdentifyGender(table[1][i]):
			score = score + 2
		score = score + h(table[0][i],table[1][i],refer) + h(table[1][i],table[0][i],refer)
	return score
def RandomAPosition():						# Random a position
	global numGuests
	position = random.randint(0,numGuests-1)
	return position
def TryToSwap(currentTable):				# Swap 2 different persons
	global numGuests
	newTable = [[0 for x in range(numGuests/2)] for y in range(2)]
	for i in range(2):
		for j in range(numGuests/2):
			newTable[i][j] = currentTable[i][j]
	person1 = RandomAPosition()
	person2 = RandomAPosition()

	while person1 == person2: 				# Different person
		person2 = RandomAPosition()
	a = FindPosition(person1)
	b = FindPosition(person2)
	if(a == 1):								# Recalculate the person's position
		person1 = person1 - numGuests/2
	if(b == 1):
		person2 = person2 - numGuests/2
	temp = 0
	temp = newTable[a][person1]
	newTable[a][person1] = newTable[b][person2]
	newTable[b][person2] = temp
	return newTable
def FindPosition(number):
	global numGuests
	if number <= numGuests/2 -1:
		return 0
	return 1
def Arrange(currentTable,refer,currentScore):		# Arrange all the guests
	global numGuests
	global bestScore
	global tempTable
	newTable = TryToSwap(currentTable)
	newScore = Score(newTable,numGuests/2,refer)
	if newScore >= bestScore:
		bestScore = newScore
		for i in range(2):
			for j in range(numGuests/2):
				tempTable[i][j] = newTable[i][j]
#---------------------------------------------------------------------------------------------------------
# main function
starttime = time.time()
numGuests = 0
bestScore = 0
epoch = 0	
input = ReadInput("hw1-inst1.txt")
currentTable = [[-1 for x in range(numGuests/2)] for y in range(2)]
tempTable = [[-1 for x in range(numGuests/2)] for y in range(2)]
currentTable= RandomTable(currentTable)
currentScore = Score(currentTable,numGuests/2,input)
bestScore = currentScore
endtime = time.time()
while endtime - starttime < 60:
	while epoch < 10:
		epoch = epoch + 1
		Arrange(currentTable,input,currentScore)
	if currentScore <= bestScore:
		currentScore = bestScore
		for i in range(2):
			for j in range(numGuests/2):
				currentTable[i][j] = tempTable[i][j]
	epoch = 0				
	endtime = time.time()
print bestScore
output = file("hw1-soln1.txt","w")
output.write(str(bestScore)+"\n")
number = 0
for x in range(2):
	for y in range(numGuests/2):
		output.write(str(number)+"\t"+str(currentTable[x][y])+"\n")
		number = number + 1
	
