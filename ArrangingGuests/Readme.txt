Student: Minh Vu
Email: minhvu@pdx.edu

My program language: Python
My machine: Macintosh with Processor 2.4 GHz Intel Core i5 on Mac OS X 10.7.5
I compiled it on Mac OS terminal. The command line of it is: python hw1.py

How my program works:
- It creates 2 tables: currentTable, tempTable and 2 scores: currentScore, bestScore
- It  will call Arrange function to arrange the guests into their positions
- Every time Arrange function is called it will try to swap 2 different guests then calculate the score, if it is the highest at that time, bestScore will be updated
- After 10 times try to swap, it chooses the best solution and update the table
- Based on this new table, it will continue Arrange the guests (10 more times again to find the best) until the time is over
 
My Algorithm:
The way I used to approach this problem is simple. I use random method first then use Greedy algorithm.
First, I create a table with all the guests are arranged randomly.
Second I will try to swap this table 10 times. Every time is called one epoch, in one epoch, I will swap 2 different guests .After that I will choose the table with the highest score to create a new table (Greedy).
After having the new table, I repeat step 2, do swapping 10 more times to find the new best score.
The repeating step will continue until the time runs out.

Testing:
I ran each test case 20 times and turn in the best score I found.
Beside I create 3 different test cases to test the program, 20 times for each.
I checked the  Score function few times and its results were right to my manual calculation.
 
Discussion:
My algorithm is a heuristic one since it can help the a good solution quickly. Clearly it is hard to find the best solution.
Based on the random method, it tries to find a better solution each time it swaps persons. The reason I choose the best solution of 10 times is that I think if every time we find a better solution, we update the table intermediately, it may take us easily to a worse way. So if we choose the best of 10, it may reduce the bad solution it takes.

The solution:
Instance 1: 100
Instance 2: 508
Instance 3: 132