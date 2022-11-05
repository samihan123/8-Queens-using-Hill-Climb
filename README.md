# 8-Queens-using-Hill-Climb

# N- Queen Problem:
The N-queens problem is about placing ‘n’ queens on an ‘n × n’ chessboard. Each queen occupies one square on the grid and no two queens share the same square. Two queens would attack each other if either of them can travel diagonally, horizontally, vertically, or and hit the square the other queen is on. The problem is to place the queens such that no two queens are attacking each other. Goal state is achieved when all the n queens are place such that no two queens are attacking each other in any way possible. 


The N-queens problem can be solved using Hill-Climbing Search Algorithm .In the hill-climbing search; in every step we replace the current node with its highest valued neighbor. If we are considering the heuristic value, then we replace the current node with the neighbor with lowest heuristic value. 

*Explanation of functions used:* 
  1. get_h() = This method is used to get the heuristic value of  the given state
  2. get_h_pos() = This method is used to get heuristic for that specific queen depending upon the location of the queen
  3. generate_heuristic_table()=This method is used to  generate heuristic table for the successors
  4. get_min_h() = This method is used to  find lowest heuristic
  5. get_random_min_successor()= This method is used to find all indexes of lowest heuristics and it will choose one randomly among them for further process
  6.	get_q_in_column()= This function is used to get position of queen in the given column
  7.	get_board()= This function is used to  create chess board of n*n dimensions 
  8.	get_queens_on_board()= This function is used to place queen in chess board depdning upon how many queens user want. It will place only those number of queens on the chess board
  9.	print_board()= This function is used to print the chess board which consist of location of queens and blanks.
  10.	hill_climbing()= This method is used to perform main hill climbing algorithm depending upon the user’s input.  
  
  There are four variants of hill climbing algorithm which are involved in this program those are:
  1. Hill Climbing
  2. Hill Climbing with SideWays move
  3. Hill Climbing with random restart without sideways move
  4. Hill Climbing with random restart with sideways move



Following is python code of Hill Climbing algortihm.
Code performs 4 type of Hill climbing they are as follows:

1. Hill Climbing
2. Hill Climbing with SideWays move
3. Hill Climbing with random restart without sideways move
4. Hill Climbing with random restart with sideways move

Following are the input it would take from the user

1. Numbers of queens.
2. Choice of hill climbing algorithm
3. Total Number of Iterration


'''


	Enter the number of queens
	8

	1. Hill Climbing
	2. Hill Climbing with SideWays move
	3. Hill Climbing with random restart without sideways move
	4. Hill Climbing with random restart with sideways move
	1

	Enter the number of executions
	100
  
  
'''

It would show the search sequences from four random initial configurations.
In the end it would dispay the statistics for the given run.

'''

    sample output:
    Total Run = 100
    Success = 13
    Failure = 87
    Average number of steps when Success = 4.230769230769231
    Average nNumber of steps when Failure = 4.114942528735632
    Success Rate = 13.0 %
    Failure Rate = 87.0 %

'''
