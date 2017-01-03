# Student: Minh Vu
# Email: minhvu@pdx.edu
#---------------------------
# 11 10 9
# 8 7 6
# 5 4 3 
# 2 1 0
# Rule of the Board:   0 = empty

import copy
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2
WIN_I = ((-2,-1),(-1,1),(1,2),(0,0),(0,0),(0,0),(-2,-1),(-1,1),(1,2),(-2,-1),(-1,1),(1,2))
WIN_J = ((0,0),(0,0),(0,0),(-2,-1),(-1,1),(1,2),(-2,-1),(-1,1),(1,2),(2,1),(1,-1),(-1,-2))
INF = 2147483646
DRAW = 0


last_i = -1
last_j = -1
# Get the value of a cell on the board
def getCell(i,j,board):
	return board[i][j]

# A player makes a move on the board
def putCell(player,j,newboard):
	global last_i
	global last_j
	for i in range(3,-1,-1):
		if newboard[i][j] == 0:
			newboard[i][j] = player
			last_i = i
			last_j = j
			return newboard
	return -1

# Check the range of two different coordinates on the board
def inRange(a,b):
	return 0<=a and a<=3 and 0<=b and b<=2
 
# Check whether a player wins
def checkPlayerWin(player,board):
	global last_i
	global last_j
	for wincase in range(12):
		t0i = last_i + WIN_I[wincase][0]
		t0j = last_j + WIN_J[wincase][0]
		t1i = last_i + WIN_I[wincase][1]
		t1j = last_j + WIN_J[wincase][1]
		if inRange(t0i,t0j) and inRange(t1i,t1j):
			if board[t0i][t0j] == player and board[t1i][t1j] == player:
				return True
	return False
			
# The move of player 1
def moveP1(curboard,depth):
	#~ print "P1:"
	#~ print depth
	#~ print(curboard)
	#~ raw_input()
	minval = INF+1
	if checkPlayerWin(PLAYER_2,curboard):
		return INF
	for column in range(3):
		if curboard[0][column] == EMPTY:
			newboard = copy.deepcopy(curboard)
			newboard = putCell(PLAYER_1,column,newboard)
			value = moveP2(newboard,depth+1)
			if value <= minval:
				minval = value
	
	if minval == INF+1:
		return DRAW
	return minval

# The move of player 2	
def moveP2(curboard,depth):
	#~ print "P2:"
	#~ print depth
	#~ print(curboard)
	#~ raw_input()
	maxval = -INF-1
	if checkPlayerWin(PLAYER_1,curboard):
		return -INF
	for column in range(3):
		if curboard[0][column] == EMPTY:
			newboard = copy.deepcopy(curboard)
			newboard = putCell(PLAYER_2,column,newboard)
			value = moveP1(newboard,depth+1)
			if value >= maxval:
				maxval = value
	
	if maxval == -INF-1:
		return DRAW
	return maxval

# Main Function
board = [[0 for x in range(3)] for y in range(4)]      # create the board
print moveP1(board,0)				       # call the player 1 to play and go on, finally print out the score


