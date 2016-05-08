# Conecta4-
Conecta 4, última versión

Práctica de Fundamentos de los sistemas inteligentes 

Irene Marina Quintero Ceballos y Judit del Carmen Correa Luciano

###############################################Definición práctica############################################################

En el fichero heuristica.py se implementaron las diferentes heuristicas para los distintos modos de dificultad del juego
Además en el fichero run.py se implementó la petición de modos de dificultad, así como el jugador inicial
Por último en el fichero games.py añadimos una variable global heur en la cual se especifica la heuristica seleccionada
y un método def_heur(heuristica) el cual define heur según los parámetros introducidos por el usuario


###############################################heuristica.py##################################################################

En este fichero nos encontramos tres métodos heuristicah0, heuristicah1 y heuristicah2 las cuales se corresponden con nivel
fácil, medio y difícil respectivamente.

- heuristicah0: utilizamos la biblioteca proporcionada en python random, y simplemente devolvemos un valor al azar para el state
pasado

- heuristicah1: utilizamos simplemente el state.utility el cual nos dice si una rama es ganadora, perdedora o empate y devolvemos
valores muy altos para las victorias, muy pequeño para las derrotas y 0 para los empates

- heuristicah2: en esta tenemos en cuenta el jugador que le toca mover de forma que si tiene muchas fichas seguidas la heuristica
aumenta y si por el contrario es el rival la heuristica decrementa. Si sabemos que una rama es ganadora se calcula la heuristica,
por el contrario si sabemos que es perdedora devolvemos un valor negativo muy bajo y cero si es empate.
