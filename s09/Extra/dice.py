# -*- coding: utf-8 -*-

import random

'''
Juego de dados.
Programa que permite a dos usuarios jugar al 21 con dos dados.
'''
player1 = {}    #diccionario vacío 
player2 = {}    #diccionario vacío

def newPlayer(playerNum=1):
    player = {
        'name': input('Ingrese el nombre del jugador ' +str(playerNum) + ': '),
        'points': 0,
        'score': 0
    }
    return player
    

def menu():
    print('''
    Menú del juego
        a. Jugar
        b. Ver puntajes
        c. Salir
    ''')
    option = input('Seleccione una opción ')

    if option.lower() == 'a':
        play()
        menu()
    elif option.lower() == 'b':
        printScore()
        menu()
    elif option.lower() == 'c':
        print('Fin del Juego... Gracias! \U0001F3B2 \U0001F3B2')
    else:
        print('Opción incorrecta')

def start():
    print("\n\n ****** Juego de dados \U0001F3B2  ****** \n\n")
    # global player1 
    # player1 = newPlayer(1)
    # global player2
    # player2 = newPlayer(2)
     
    #la funcion globals() devuelve un diccionario de todas las variables globales.
    #que pueden ser accesadas/modificadas desde adentro de la funcion.
    players = globals()
    players['player1'] = newPlayer(1)
    players['player2'] = newPlayer(2)
    input('\nPresione enter para empezar...')
    menu()
    

def printPoints(type='points'):
    print('Puntaje:')
    print(player1['name'], ': ', player1[type])
    print(player2['name'], ': ', player2[type])

def play(player):
    dice1 = rollDice()
    dice2 = rollDice()

    if player == 1:
        player1['points'] += (dice1 + dice2)
    else:
        player2['points'] += (dice1 + dice2)

    printPoints('points')

    continuePlaying = True if input('Continua o pasa? c = Continuar, p = pasar: ').lower() == 'c' else False

    if continuePlaying:
        play(player)
    else:
        play(1 if player == 2 else 2)


def rollDice(max=6)
    min = 1
    result = random.randint(min, max)
    print("\U0001F3B2 = ", result )

start()