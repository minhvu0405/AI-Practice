# Student: Minh Vu
# Email: minhvu@pdx.edu
#---------------------------

import string
import  time
import copy
import random
def ReadInput(file):					# Read the full data file (all distances)
	inFile = open(file,'r')
	inputLines = []
	for line in inFile.readlines():
		line.split()
		inputLines.append(line)
	inFile.close()
	numline = len(inputLines)
	att = line.count(' ')+1
	data = [[0 for x in range(att)] for y in range(numline)]
	for i in range(numline):
		data[i] = inputLines[i].split(' ')
	temp = 'namecity'
	count = 0
	global nameCities
	for i in range(numline):
		a = data[i][0]
		if(a != temp ):
			count = count + 1
			temp = a
			nameCities.append(temp)
	global TotalCities
	TotalCities = count
	global index
	index = MakeIndex(data,att,numline)
	return data
def MakeIndex(data,att,numline):				# Make a matrix to store all the distance between cities
	indextable = [[0 for i in range(TotalCities)] for y in range(TotalCities)]
	line = [0 for i in range(att-1)]
	for i in range(numline):
		for j in range(att-1):
			line[j] = nameCities.index(data[i][j])
		indextable[line[0]][line[1]] = data[i][j+1]
	for i in range(TotalCities):
		for j in range(TotalCities):
			indextable[i][j] = string.atof(indextable[i][j])
	return indextable
def Distance(cityA,cityB):								# Distance between 2 cities
	a = nameCities.index(cityA)
	b = nameCities.index(cityB)
	return index[a][b]
def TotalDistance(list):
	total = 0
	for i in range(numTravelCities-1):
		total = Distance(list[i],list[i+1]) + total
	total = Distance(list[i+1],list[0]) + total
	return total
	
def CitiesTravel(file):									# Read the list of cities we need to make tour
	inFile = open(file,'r')
	inputLines = []
	for line in inFile.readlines():
		line.split()
		inputLines.append(line)
	inFile.close()
	global numTravelCities
	numline = len(inputLines)
	numTravelCities = numline
	listcity = []
	listcity = inputLines
	for i in range(numline):
		listcity[i] = listcity[i].rstrip('\n')
	return listcity
def RandomAPosition():									# Random a position
	position = random.randint(0,numTravelCities-1)
	return position
def RandomTour():										# Arrange the tours randomly
	list1 = [x for x in range(numTravelCities)]
	list2= []
	tour = [0 for i in range(numTravelCities)]
	i = 0
	b = 0
	while(i < numTravelCities):
		number = random.choice([x for x in list1 if x not in list2])
		list2.append(number)
		tour[i] = listcities[number]
		i = i + 1
	return tour
def SwapTour(currentTour):									# Swap two different tours
	newTour = [0 for i in range(numTravelCities)]
	newTour = copy.deepcopy(currentTour)
	city1 = RandomAPosition()
	city2 = RandomAPosition()
	while(city1 == city2):
		city1 = RandomAPosition()
		city2 = RandomAPosition()
	temp = 0
	temp = newTour[city1]
	newTour[city1] = newTour[city2]
	newTour[city2] = temp
	return newTour
def ArrangeNewTour(currentTour,currMileage):				# Arrange the new tour
	global bestMileage
	global bestTour
	tempTour = SwapTour(currentTour)
	newMileage = TotalDistance(tempTour)
	if newMileage <= bestMileage:
		bestMileage = newMileage
	bestTour = copy.deepcopy(tempTour)
def Display(): 												# Display the result
	output = file("large-instance-solution.txt","w")
	output.write(str(bestMileage)+"\n")
	global listcities
	listcities.sort()
	position = currentTour.index(listcities[0])
	if position > 0 and position < numTravelCities-1:
		a = listcities.index(currentTour[position-1])
		b = listcities.index(currentTour[position+1])
		if a < b:
			i = position
			while i >= 0:
				output.write(currentTour[i]+"\n")
				i = i - 1
			i = numTravelCities-1
			while i >= position:
				output.write(currentTour[i]+"\n")
				i = i - 1
		else:
			i = position
			while i <= numTravelCities-1:
				output.write(currentTour[i]+"\n")
				i = i + 1
			i = 0
			while i <= position:
				output.write(currentTour[i]+"\n")
				i = i + 1 
	elif position == numTravelCities-1:
		a = listcities.index(currentTour[0])
		b = listcities.index(currentTour[position-1])
		if a < b:
			output.write(currentTour[position]+"\n")
			i = 0
			while i <= position:
				output.write(currentTour[i]+"\n")
				i = i + 1
		else:
			i = position
			while i >= 0:
				output.write(currentTour[i]+"\n")
				i = i - 1
	elif position == 0:
		a = listcities.index(currentTour[position+1])
		b = listcities.index(currentTour[numTravelCities-1])
		if a < b: 
			i = 0
			while i <= numTravelCities-1:
				output.write(currentTour[i]+"\n")
				i = i + 1
			output.write(currentTour[0]+"\n")
		else:
			output.write(currentTour[0]+"\n")
			i = numTravelCities-1
			while i >= 0:
				output.write(currentTour[i]+"\n")
				i = i - 1
# main function
starttime = time.time()
TotalCities = 0
nameCities = []
index = []
numTravelCities = 0
rawdata = ReadInput("oregon-mileage.txt")
listcities = CitiesTravel("large-instance.txt")
bestTour = [0 for i in range(numTravelCities)]
currentTour = [0 for i in range(numTravelCities)]
currentTour = RandomTour()
currMileage = TotalDistance(currentTour)
bestMileage = currMileage
newTour = [0 for i in range(numTravelCities)]
epoch = 0
endtime = time.time()
while endtime - starttime < 60:				# run in 1 min
	while epoch < 50:						# swap 50 times
		epoch = epoch + 1
		ArrangeNewTour(currentTour,currMileage)
	if currMileage >= bestMileage:
		currentMileage = bestMileage
		currentTour = copy.deepcopy(bestTour)
	epoch = 0
	endtime = time.time()
Display()




