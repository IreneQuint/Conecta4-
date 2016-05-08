import games
from utils import *

#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial

#Seleccion de la dificultad
print "1-Para nivel facil"
print "2-Para nivel medio"
print "3-Para nivel dificil"
heuristica=input("Seleccione nivel de dificultad: ")
games.def_heur(heuristica)

print "Seleccione jugador inicial"
print "1 maquina"
print "2 usuario"
jugador = input("Seleccion: ")
if (jugador == 1):
    game.initial.to_move = 'X'
    player = 'X'
elif (jugador == 2):
    game.initial.to_move = 'O'
    player = 'O'
else:
    print "Jugador incorrecto"
    exit()

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        player = 'X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        if(state.to_move=='O'):
            print "Gano: X"
        else:
            print "Gano: O"
        break
