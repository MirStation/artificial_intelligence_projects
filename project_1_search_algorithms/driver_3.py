#!/usr/bin/python3

import sys
import math
import copy

class Board:
    
    def __init__(self, board):
        self.__board = board
        self.__board_size = len(board)
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                if self.__board[i][j] == 0:
                    self.__empty_i = i
                    self.__empty_j = j

    def get_empty_position(self):
        return [self.__empty_i, self.__empty_j]
    
    def get_board_matrix(self):
        return copy.deepcopy(self.__board)

    def print_board(self):
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                print(self.__board[i][j],"\t", end='')
            print()

    def get_board_size(self):
        return self.__board_size

    def equal_to(self, board):
        if self.__board_size == board.get_board_size():
            other_board = board.get_board_matrix()
            for i in range(self.__board_size):
                for j in range(self.__board_size):
                    if self.__board[i][j] != other_board[i][j]:
                        return False
        else:
            return False
                        
        return True

    def __move_up(self):
        if self.__empty_i - 1 >= 0:
            new_board = copy.deepcopy(self.__board)
            new_board[self.__empty_i][self.__empty_j] = new_board[self.__empty_i - 1][self.__empty_j]
            new_board[self.__empty_i - 1][self.__empty_j] = 0
            return Board(new_board)
        return None

    def __move_down(self):
        if self.__empty_i + 1 < self.__board_size:
            new_board = copy.deepcopy(self.__board)
            new_board[self.__empty_i][self.__empty_j] = new_board[self.__empty_i + 1][self.__empty_j]
            new_board[self.__empty_i + 1][self.__empty_j] = 0
            return Board(new_board)
        return None

    def __move_left(self):
        if self.__empty_j - 1 >= 0:
            new_board = copy.deepcopy(self.__board)
            new_board[self.__empty_i][self.__empty_j] = new_board[self.__empty_i][self.__empty_j - 1]
            new_board[self.__empty_i][self.__empty_j - 1] = 0
            return Board(new_board)
        return None

    def __move_right(self):
        if self.__empty_j + 1 < self.__board_size:
            new_board = copy.deepcopy(self.__board)
            new_board[self.__empty_i][self.__empty_j] = new_board[self.__empty_i][self.__empty_j + 1]
            new_board[self.__empty_i][self.__empty_j + 1] = 0
            return Board(new_board)
        return None

    def move(self, action):
        if action == 'Up' or action == 'Down':
            if action == 'Up':
                return self.__move_up()
            else:
                return self.__move_down()
        elif action == 'Left' or action == 'Right':
            if action == 'Left':
                return self.__move_left()
            else:
                return self.__move_right()
        return None


class BoardNode:
    
    def __init__(self, board, parent, cost, move, depth):
        self._board = board
        self._parent = parent
        self._cost = cost
        self._move = move
        self._depth = depth

    def get_board(self):
        return self._board

    def get_parent(self):
        return self._parent

    def get_cost(self):
        return self._cost

    def get_move(self):
        return self._move

    def get_depth(self):
        return self._depth

def make_board_matrix(board_values, board_size):
    k = 0
    board = []
    for i in range(board_size):
        board_row = []
        for j in range(board_size):
            board_row.append(board_values[k])
            k += 1
        board.append(board_row)
    return board

search_method = sys.argv[1]

board_values = sys.argv[2].split(',')
for i in range(len(board_values)):
    board_values[i] = int(board_values[i])

board_size = int (math.sqrt(len(board_values)))

board_matrix = make_board_matrix(board_values, board_size)
board = Board(board_matrix)
print(board.get_empty_position())

board.print_board()
print()
board = board.move('Right')
board.print_board()
print()
board = board.move('Down')
board.print_board()
print()
board = board.move('Left')
board.print_board()
print()
board = board.move('Up')
board.print_board()
print()
print(board.move('Up'))
print(board.move('Left'))

board_matrix = make_board_matrix([8,7,0,6,5,4,3,2,1], board_size)
board = Board(board_matrix)
print(board.get_empty_position())

board.print_board()
print()
board = board.move('Left')
board.print_board()
print()
board = board.move('Down')
board.print_board()
print()
board = board.move('Right')
board.print_board()
print()
board = board.move('Up')
board.print_board()
print()
print(board.move('Up'))
print(board.move('Right'))

board_matrix = make_board_matrix([8,7,6,5,4,3,2,1,0], board_size)
board = Board(board_matrix)
print(board.get_empty_position())

board.print_board()
print()
board = board.move('Left')
board.print_board()
print()
board = board.move('Up')
board.print_board()
print()
board = board.move('Right')
board.print_board()
print()
board = board.move('Down')
board.print_board()
print()
print(board.move('Down'))
print(board.move('Right'))

board_matrix = make_board_matrix([8,7,6,5,4,3,0,2,1], board_size)
board = Board(board_matrix)
print(board.get_empty_position())

board.print_board()
print()
board = board.move('Right')
board.print_board()
print()
board = board.move('Up')
board.print_board()
print()
board = board.move('Left')
board.print_board()
print()
board = board.move('Down')
board.print_board()
print()
print(board.move('Down'))
print(board.move('Left'))

board_matrix = make_board_matrix([8,7,6,5,0,4,3,2,1], board_size)
board = Board(board_matrix)
print(board.get_empty_position())

board.print_board()
print()
board.move('Up').print_board()
print()
board.move('Down').print_board()
print()
board.move('Left').print_board()
print()
board.move('Right').print_board()
print()
print(board.move('Up').move('Up'))
print(board.move('Down').move('Down'))
print(board.move('Right').move('Right'))
print(board.move('Left').move('Left'))



