Student: Minh Vu
Email : minhvu@pdx.edu
My program language: Python
My machine: Macintosh with Processor 2.4 GHz Intel Core i5 on Mac OS X 10.7.5
I compiled it on Mac OS terminal. The command line to compile it: python final.py

How my program works:
- It creates 2 lists: currentTour, bestTable and 2 scores: currMileage, bestMileage
- It  will call Arrange function to arrange a new tour
- Every time Arrange function is called it will try to swap 2 different cities then calculate the total mileage, if it is the highest at that time, bestMileage will be updated
- After 10 times try to swap, it chooses the best solution and update the current tour
- Based on this current tour, it will continue Arrange the cities (10 more times again to find the best) until the time is over
 
My Algorithm:
The way I used to approach this problem is using the local search. I use random method first then use Greedy algorithm.
First, I create a tour with all the cities are arranged randomly.
Second I will try to swap this tour 50 times. Every time is called one epoch, in one epoch, I will swap 2 different cities .After that I will choose the tour with the highest score to create a new tour (Greedy).
After having the new tour, I repeat step 2, do swapping 10 more times to find the new best mileage.
The repeating step will continue until the time runs out.

Testing:
I ran each test case 100 times and turn in the best result I found.
Beside I create 2 different test cases to test the program, 20 times for each.
I checked the  Total Distance function few times and its results were right to my manual calculation.
 
Discussion:
My method depends much on the initial tour, if this one has a good result then the final may be good. So I let it run 1000 times to choose the best result before it uses the algorithm.
The way I think may improve this method is we can use Greedy algorithm earlier to initialize a good tour, then let it swap randomly. It is like we randomly make a good tour then use Greedy algorithm to make it better.

The solution:
Instance 1: 1130.0
Instance 2: 1680.0
Instance 3: 1906.0