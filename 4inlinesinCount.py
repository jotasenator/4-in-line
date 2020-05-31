# -*- coding: utf-8 -*-

# adaptacion de Tic Tac Toe por James Shah https://dev.to/jamesshah/the-classic-tictactoe-game-in-python-cpi
# Implementacion de humano vs humano del juego 4 en linea


theBoard = {'36': ' ', '37': ' ', '38': ' ', '39': ' ', '40': ' ', '41': ' ', '42': ' ',
            '29': ' ', '30': ' ', '31': ' ', '32': ' ', '33': ' ', '34': ' ', '35': ' ',
            '22': ' ', '23': ' ', '24': ' ', '25': ' ', '26': ' ', '27': ' ', '28': ' ',
            '15': ' ', '16': ' ', '17': ' ', '18': ' ', '19': ' ', '20': ' ', '21': ' ',
            '8': ' ', '9': ' ', '10': ' ', '11': ' ', '12': ' ', '13': ' ', '14': ' ',
            '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' '
            }

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):

    print(board['36'] + '|' + board['37'] + '|' + board['38'] + '|' +
          board['39'] + '|' + board['40'] + '|' + board['41'] + '|' + board['42'])
    print('-+-+-+-+-+-+-')
    print(board['29'] + '|' + board['30'] + '|' + board['31'] + '|' +
          board['32'] + '|' + board['33'] + '|' + board['34'] + '|' + board['35'])
    print('-+-+-+-+-+-+-')
    print(board['22'] + '|' + board['23'] + '|' + board['24'] + '|' +
          board['25'] + '|' + board['26'] + '|' + board['27'] + '|' + board['28'])
    print('-+-+-+-+-+-+-')
    print(board['15'] + '|' + board['16'] + '|' + board['17'] + '|' +
          board['18'] + '|' + board['19'] + '|' + board['20'] + '|' + board['21'])
    print('-+-+-+-+-+-+-')
    print(board['8'] + '|' + board['9'] + '|' + board['10'] + '|' + board['11'] +
          '|' + board['12'] + '|' + board['13'] + '|' + board['14'])
    print('-+-+-+-+-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'] + '|' +
          board['4'] + '|' + board['5'] + '|' + board['6'] + '|' + board['7'])


def game():

    global turn  # si no hay error en la funcion victoria

    turn = 'X'

    while True:
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        try:  # evitando que el programa se rompa si move tomaun valor distinto de numeros 1 a 42

            lista_move = ['1', '2', '3', '4', '5', '6', '7']

            if move in lista_move:

                if theBoard[move] == ' ':
                    theBoard[move] = turn

                else:

                    print("..you can't do that.\nMove to which place?")

                    continue  # sino cuando turn tomaria no seria la misma ficha de juego

            elif move not in lista_move:

                if theBoard[move] == ' ' and theBoard[str(int(move)-7)] != ' ':
                    theBoard[move] = turn

                else:
                    print("...you can't do that :).\nMove to which place?")

                    continue  # sino cuando turn tomaria no seria la misma ficha de juego
        except KeyError:  # capturando el error cuando move es distinto de numeros 1 a 42

            print("..you can't do that either.\nMove to which place?")

            continue  # sino cuando turn tomaria no seria la misma ficha de juego

    # Despues de 7 jugadas ya existe posibilidad de que el primer jugador gane

        # horizontales
        cabezasH = [1, 8, 15, 22, 29, 36]

        lista = [i for i in range(1, 43)]

        for numeroH in cabezasH:

            for i in range(0, 4):

                listaH = lista[numeroH + i - 1:numeroH + i + 3]

                if theBoard[str(listaH[0])] == theBoard[str(listaH[1])] == theBoard[str(listaH[2])] == theBoard[str(listaH[3])] != ' ':
                    victory()
                    play_again()

        # verticales
        intervalos = [i for i in range(1, 22)]

        for numeroV in intervalos:

            listaV = [numeroV, numeroV + 7, numeroV + 14, numeroV + 21]

            if theBoard[str(listaV[0])] == theBoard[str(listaV[1])] == theBoard[str(listaV[2])] == theBoard[str(listaV[3])] != ' ':
                victory()
                play_again()

        # diagonales

        lista_diagonal1 = [1, 2, 3, 4, 8, 9, 10, 11, 15, 16, 17, 18]
        lista_diagonal2 = [4, 5, 6, 7, 11, 12, 13, 18, 19, 20, 14, 21]

        for i, j in zip(lista_diagonal1, lista_diagonal2):

            listaD1 = [i, i+8, i+16, i+24]
            listaD2 = [j, j+6, j+12, j+18]

            if theBoard[str(listaD1[0])] == theBoard[str(listaD1[1])] == theBoard[str(listaD1[2])] == theBoard[str(listaD1[3])] != ' ' or theBoard[str(listaD2[0])] == theBoard[str(listaD2[1])] == theBoard[str(listaD2[2])] == theBoard[str(listaD2[3])] != ' ':
                victory()
                play_again()

        # el empate
        lista_empate = []

        for j in board_keys:

            for i in theBoard[j]:

                if i != ' ':

                    lista_empate.append(i)

            if len(lista_empate) == 42:

                tie()
                play_again()

# el cambio de la ficha que le toca en turno!!!
        if turn == 'O':
            turn = 'X'
        else:
            turn = 'O'

# si hay victoria


def victory():

    printBoard(theBoard)
    print("\nGame Over.\n")
    print(" **** " + turn + " won. ****")

# si hay empate


def tie():

    printBoard(theBoard)
    print("\nGame Over.\n")
    print("It's a Tie!!")

# si desea jugar de nuevo o no


def play_again():

    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

    elif restart == "n" or restart == "N":
        print('gg well played')
        quit()

    else:

        play_again()


game()
