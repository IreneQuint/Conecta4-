import random
import games
from utils import *

# Nivel facil donde la maquina jugara aleatoriamente
def heuristicah0(state):
    return random.randint(0, 10)


# Nivel medio intenta no dejarte ganar pero se puede ganar
def heuristicah1(state):
    if (state.utility == 1):
        return infinity
    elif (state.utility == -1):
        return -infinity
    else:
        return 0


# Nivel dificil
def heuristicah2(state):
    heuristica = 0

    if state.utility != 0:
        return state.utility * infinity
    else:
        mov_leg = legal_moves(state)
        for pos in mov_leg:

            heuristica += k_in_row(state.board, pos, 'X', (0, 1))
            heuristica += k_in_row(state.board, pos, 'X', (1, 0))
            heuristica += k_in_row(state.board, pos, 'X', (1, 1))
            heuristica += k_in_row(state.board, pos, 'X', (-1, -1))

            heuristica -= k_in_row(state.board, pos, 'O', (0, 1))
            heuristica -= k_in_row(state.board, pos, 'O', (1, 0))
            heuristica -= k_in_row(state.board, pos, 'O', (1, 1))
            heuristica -= k_in_row(state.board, pos, 'O', (-1, -1))

        return (heuristica)


def k_in_row(board, move, player, (delta_x, delta_y)):
    "Return true if there is a line through move on board for player."
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y), '.') == player or board.get((x, y), '.') == '.':
        if (board.get((x, y), '.') == player):
            n += 1
        x, y = x + delta_x, y + delta_y
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
    x, y = move
    while board.get((x, y), '.') == player or board.get((x, y), '.') == '.':
        if (board.get((x, y), '.') == player):
            n += 1
        x, y = x - delta_x, y - delta_y
        if x > 7 or x < 0 or y > 6 or y < 0:
            break

    n -= 1  # Because we counted move itself twice
    return n


def legal_moves(state):
    "Legal moves are any square not yet taken."
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
