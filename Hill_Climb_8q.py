# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:40:37 2021

@author: sjawalka
"""
from random import randint
from copy import deepcopy

# n*n board
board_n = 8
success = 0
l_minima = 0
shoulder = 0
steps_count = 0
restart = 0
success_steps_count = []
failure_steps_count = []
restart_count = []


##############################################################################
# Class Node,structure of chess board
##############################################################################
class Node:
    def __init__(self, board, h=0, h_table=[], children=[]):
        '''
        

        Parameters
        ----------
        board : array
            chess board.
        h : Int, heuristic value
            heuristic value of chess board. The default is 0.
        h_table : Int, optional
            n*n heuristic table. The default is [].
        children : array, optional
            to get to the next state. The default is [].

        Returns
        -------
        None.

        '''
        self.board = board
        self.h = h
        self.heur_table = h_table
        self.children = children

    ##########################################################################
    # get the total heuristic value of given board
    ##########################################################################
    def get_h(self, board):
        '''
        

        Parameters
        ----------
        board : array
            chess board.

        Returns
        -------
        heuristic_val : int
           total heuristic value .

        '''
        heuristic_val = 0
        for j in range(board_n):
            for i in range(board_n):
                if board[i][j] == 'Q':
                    # print(calc_h_pos(boardPos, i, j))
                    heuristic_val += (self.get_h_pos(board, i, j))
        return heuristic_val

    ##########################################################################
    # get heuristic for that specific position
    #########################################################################
    def get_h_pos(self, board, i, j):
        '''
        

        Parameters
        ----------
        board : array
            n*n chess board.
        i : int
            row.
        j : int
            column.

        Returns
        -------
        num_of_attacks : TYPE
            number of attack at that possition.

        '''
        num_of_attacks = 0
        k = 1
        j += k
        while j < board_n:
            if board[i][j] == 'Q':
                num_of_attacks += 1
            if i + k < board_n and board[i + k][j] == 'Q':
                num_of_attacks += 1
            if i - k > -1 and board[i - k][j] == 'Q':
                num_of_attacks += 1
            k += 1
            j += 1
        return num_of_attacks

    ##########################################################################
    # generate heurictic table for all combination
    ##########################################################################
    def generate_heuristic_table(self):
        '''
        

        Returns
        -------
        heuristic table, each square would consists the h value.

        '''
        h_table = [[0] * board_n for i in range(board_n)]
        for j in range(board_n):
            x = get_q_in_column(self.board, j)
            for i in range(board_n):
                if x == i:
                    h_table[i][j] = float('inf')
                else:
                    children = deepcopy(self.board)
                    children[i][j], children[x][j] = children[x][j], children[i][j]
                    h_table[i][j] = self.get_h(children)
        self.heur_table = h_table
        # return h_table

    ########################################################################
    # find lowest heuristic
    ########################################################################
    def get_min_h(self, h_table):
        '''
        

        Parameters
        ----------
        h_table : array
            heuristic table.

        Returns
        -------
        mini : int
            minimum values.

        '''
        mini = float('inf')
        x = -1
        for arr in h_table:
            if mini > min(arr):
                mini = min(arr)
            x += 1
        return mini

    ########################################################################
    # Find all indexes of lowest heuristics and choose one randomly
    ########################################################################
    def get_random_min_successor(self, h_table, min_h):
        '''
        

        Parameters
        ----------
        h_table : htable
            heuristic table.
        min_h : TYPE
            minimum heuristic.

        Returns
        -------
        i : int
            row.
        j : int
            column.

        '''
        random_min_h_list = []
        for i in range(0, board_n):
            for j in range(0, board_n):
                if h_table[i][j] == min_h:
                    random_min_h_list.append((i * 10) + j)
        if random_min_h_list:
            rand_pos = randint(0, len(random_min_h_list) - 1)
            i = int(random_min_h_list[rand_pos] / 10)
            j = random_min_h_list[rand_pos] % 10
        return i, j


############################################################################
# get position of Q in given list and column
#############################################################################
def get_q_in_column(board, col_n):
    '''
    

    Parameters
    ----------
    board : array
        chess board.
    col_n : int
        column number.

    Returns
    -------
    i : int
        row.

    '''
    for i in range(board_n):
        if board[i][col_n] == 'Q':
            return i
    return None


##########################################################################
# create chess board
##########################################################################
def get_board():
    '''
    get the board

    Returns
    -------
    list
        chess board.

    '''
    # create an board without queens
    return [['-'] * board_n for i in range(board_n)]


##########################################################################
# place queen in chess board
##########################################################################
def get_queens_on_board(board):
    '''
    place queens on board randomly

    Parameters
    ----------
    board : list
        chess board.

    Returns
    -------
    board : array
        places queen on board randomly.

    '''
    # place queen randomly
    for i in range(0, board_n):
        board[randint(0, board_n-1)][i] = 'Q'

    return board


#########################################################################
# print board
#########################################################################
def print_board(board=[]):
    '''
    Print board

    Parameters
    ----------
    board : array, optional
        print the board in format. The default is [].

    Returns
    -------
    None.

    '''
    i = 0
    #l = list(str(range(0,board_n+1)))
    l = list(map(str, range(0, board_n)))
    l = ['','',*l]
    print(' '.join(l))
    for row in board:
        print(str(i) + ' ' + ' '.join(map(str, row)), end='\n')
        i += 1


#########################################################################
# hill climbing algorithm
##########################################################################
def hill_climbing(current, curr_heur, l_count, choice, print_count):
    '''
    

    Parameters
    ----------
    current : object
        current state.
    curr_heur : int
        current node heuristic.
    l_count : int
        total run.
    choice : int
        choice of hill climb.
    print_count : int
        total print require.

    Returns
    -------
    None.

    '''
    global success
    global steps_count
    global shoulder
    global l_minima
    global restart

    # check if initial state is goal state, then no need to perform hill climb
    if curr_heur == 0:
        if print_count > 0:
            print("Success")
        success += 1
        return
    steps_count += 1

    current.generate_heuristic_table()
    # print(print_board(current.heur_table))

    # x_min, y_min, min_heur = current.get_lowest_h(current.heur_table, False)
    min_heur = current.get_min_h(current.heur_table)
    x_min, y_min = current.get_random_min_successor(current.heur_table, min_heur)

    #print(x_min, y_min)

    child_board = deepcopy(current.board)
    x_q = get_q_in_column(current.board, y_min)
    child_board[x_min][y_min], child_board[x_q][y_min] = child_board[x_q][y_min], child_board[x_min][y_min]
    child_node = Node(child_board)
    if print_count > 0:
        print_board(child_node.board)
        print("Heuristic of node :", min_heur)

    if min_heur == 0:
        if print_count > 0:
            print("Success")
        success += 1
        success_steps_count.append(steps_count)
        restart_count.append(restart)
    elif (choice == 2 or choice == 4) and min_heur == curr_heur:
        # side ways move
        l_count -= 1
        if l_count != 0:
            hill_climbing(child_node, min_heur, l_count, choice, print_count)
        else:
            if choice == 4:
                restart += 1
                board = get_board()
                queen_board = get_queens_on_board(board)
                queen_board_obj = Node(queen_board)
                current_heur = queen_board_obj.get_h(queen_board_obj.board)
                if print_count > 0:
                    print("Restart hill climb")
                    print_board(queen_board_obj.board)
                    print("Heuristic of node :", current_heur)
                hill_climbing(queen_board_obj, current_heur, 100, choice, print_count)
            else:
                shoulder += 1
                failure_steps_count.append(steps_count)
                if print_count > 0:
                    print("Failure, Shoulder found")

    elif min_heur >= curr_heur:
        if choice == 3 or choice == 4:
            restart += 1
            board = get_board()
            queen_board = get_queens_on_board(board)
            queen_board_obj = Node(queen_board)
            current_heur = queen_board_obj.get_h(queen_board_obj.board)
            if print_count > 0:
                print("Restart hill climb")
                print_board(queen_board_obj.board)
                print("Heuristic of node :", current_heur)
            hill_climbing(queen_board_obj, queen_board_obj.get_h(queen_board_obj.board), 100, choice, print_count)
        else:
            if print_count > 0:
                print("Failure, local minima Found")
            l_minima += 1
            failure_steps_count.append(steps_count)
    else:
        hill_climbing(child_node, min_heur, l_count, choice, print_count)


##########################################################################
# main function
##########################################################################
def main():
    global board_n, steps_count, restart
    board_n = int(input("Enter the number of queens\n"))
    choice = int(input("1. Hill Climbing\n"
                       "2. Hill Climbing with SideWays move\n"
                       "3. Hill Climbing with random restart without sideways move\n"
                       "4. Hill Climbing with random restart with sideways move\n"))
    run = int(input("Enter the number of executions\n"))

    print_count = 4

    for i in range(0, run):
        if print_count > 0:
            print("-" * 50)
        steps_count = 0
        restart = 0
        board = get_board()
        root_board = get_queens_on_board(board)
        root = Node(root_board)
        current_heur = root.get_h(root.board)
        if print_count > 0:
            print_board(root_board)
            print("Heuristic of node :", current_heur)
        hill_climbing(root, current_heur, 100, choice, print_count)
        print_count -= 1
        if print_count > 0:
            print("-" * 50)

    if choice == 1 or choice == 2:
        print("Total Run = {run}\nSuccess = {su}\nFailure = {lm}"
              "\nAverage number of steps when Success = {avg1}"
              "\nAverage nNumber of steps when Failure = {avg2}"
              .format(run=run, su=success, lm=l_minima + shoulder,
                      avg1=(sum(success_steps_count) /
                            len(success_steps_count)) if len(success_steps_count) > 0 else 0,
                      avg2=(sum(failure_steps_count) /
                            len(failure_steps_count)) if
                      len(failure_steps_count) > 0 else 0))
    if choice == 3 or choice == 4:
        print("Total Run = {run}\n"
              "\nAverage number of random restarts required = {avg1}"
              "\nAverage number of steps required = {avg2}"
              .format(run=run,
                      avg1=(sum(restart_count) / len(restart_count))
                      if len(restart_count) > 0 else 0,
                      avg2=(sum(success_steps_count) /
                            len(success_steps_count)) if
                      len(success_steps_count) > 0 else 0))
    success_rate = (success / run) * 100
    print("Success Rate = {sr} %".format(sr=success_rate))
    print("Failure Rate = {fr} %".format(fr=((run - success) / run) * 100))


main()