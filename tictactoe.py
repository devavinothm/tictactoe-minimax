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
    num_x = 0
    num_o = 0
    for row in board:
        for coll in row:
            if coll == X:
                num_x += 1
            elif coll == O:
                num_o += 1

    if num_o == num_x:
        return X
    
    else:
        return O
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]

    if board[row][col] != EMPTY:
        raise Exception("Invalid Action")
    
    board_copy = copy.deepcopy(board)

    turn = player(board_copy)

    board_copy[row][col] = turn

    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for row in board:
            for coll in row:
                if coll == EMPTY:
                    return False
    
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == X:
        cur_result = (None, -math.inf)
        for action in actions(board):
            score = minimax_algorithm(result(board, action), False)
            if score == 1:
                return action
            if score > cur_result[1]:
                cur_result = (action, score)

        return cur_result[0]
    
    cur_result = (None, math.inf)
    for action in actions(board):
        score = minimax_algorithm(result(board, action), True)
        if score == -1:
            return action
        if score < cur_result[1]:
            cur_result = (action, score)

    return cur_result[0]

def minimax_algorithm(board, is_max):
    """ The AI player logic recursive algorithm to get the optimal move """
    if terminal(board):
        return utility(board)
    
    if is_max:
        cur_result = -math.inf
        for action in actions(board):
            cur_result = max(cur_result, minimax_algorithm(result(board, action), False))
        
        return cur_result
    
    cur_result = math.inf
    for action in actions(board):
        cur_result = min(cur_result, minimax_algorithm(result(board, action), True))
    
    return cur_result