"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cntX = 0
    cntO = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                cntX+=1
            elif board[i][j] == O:
                cntO+=1
    if cntX == cntO:
        return X
    if cntX > cntO:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result_set = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == None:
                result_set.add((i,j))
    return result_set
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] != None:
        raise NameError("invalid Move")
    if player(new_board) == X:
        new_board[action[0]][action[1]] = X
    else:
        new_board[action[0]][action[1]] = O
    
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if(board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] == X):
            return X
        elif (board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] == O):
            return O
        
        if(board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] == X):
            return X
        elif (board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] == O):
            return O
        
    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == X):
        return X
    elif(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == O):
        return O
    
    if(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == X):
        return X
    elif(board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == O):
        return O
    return None
    raise NotImplementedError


def terminal(board):
    if winner(board) != None:
        return True
    if len(actions(board)) == 0:
        return True
    return False
    raise NotImplementedError


def utility(board):
    if(winner(board) == X):
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    if(terminal(board)):
        print("1")
        return None
    if(player(board) == X):
        res = tuple()
        temp = -10
        for ac in actions(board):
            newB = result(board,ac)
            if(minValue(newB)>=temp):
                res = ac
                temp = minValue(newB)
        return res
    elif player(board) == O:
        res = tuple()
        temp = 10
        for ac in actions(board):
            newB = result(board,ac)
            if(maxValue(newB)<=temp):
                res = ac
                temp = maxValue(newB)
        return res
    raise NotImplementedError

def maxValue(board):
    v = -100000
    if(terminal(board)):
        return utility(board)
    for ac in actions(board):
        v = max(v, minValue(result(board,ac)))
    return v
    
def minValue(board):
    v = 1000000
    if(terminal(board)):
        return utility(board)
    for ac in actions(board):
        v = min(v, maxValue(result(board,ac)))
    return v

