#Juego de ta-te-ti.

def imprimir_tablero(tablero):
    """
    Imprime el tablero.
    """
    print('Estado actual del tablero.')
    print('|', tablero[0][0], '|', tablero[0][1], '|', tablero[0][2], '|')
    print('|', tablero[1][0], '|', tablero[1][1], '|', tablero[1][2], '|')
    print('|', tablero[2][0], '|', tablero[2][1], '|', tablero[2][2], '|')
    continuar()

tablero = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]

def elegir_ficha():
    """
    Muestra el menú para elegir ficha.
    """
    print('1. X')
    print('2. O')

def continuar():
    """
    Muestra mensaje de continuación en la consola.
    """
    print()
    print('Presione enter para continuar...', end='')
    input()
    print()

juego_terminado = False
turno_x = True
jugador_1 = ''
jugador_2 = ''

imprimir_tablero(tablero)
elegir_ficha()

while True:
    jugador_1 = input('Seleccione su ficha (Las X empiezan): ')
    if jugador_1 == 'X':
        jugador_2 == 'O'
        print('El jugador 1 utiliza las "X" y el jugador 2 las "O".')
        break
    elif jugador_1 == 'O':
        jugador_2 == 'X'
        print('El jugador 1 utiliza las "O" y el jugador 2 las "X".')
        break
    else:
        print()
        print('Debe ingresar una opción válida (X/O)')
        elegir_ficha()
        continuar()


while not juego_terminado:
    while True:
        try:
            Casillero = int(input('Ingrese el casillero que desea jugar (1-9 comenzando de arriba a la izquierda): '))
            if 0 < Casillero <=9:
                if Casillero == 1:
                    if tablero[0][0] == '_':
                        tablero[0][0] = 'X' if turno_x else 'O'
                        break
                    elif tablero[0][0] == 'X' or 'O':
                        print('Casillero ocupado.')
                        imprimir_tablero(tablero)
                if Casillero == 2:
                    if tablero[0][1] == '_':
                        tablero[0][1] = 'X' if turno_x else 'O'
                        break
                    elif tablero[0][1] == 'X' or 'O':
                        print('Casillero ocupado.')
                        imprimir_tablero(tablero)
                if Casillero == 3:
                    if tablero[0][2] == '_':
                        tablero[0][2] = 'X' if turno_x else 'O'
                        break
                    elif tablero[0][2] == 'X' or 'O':
                        print('Casillero ocupado.')
                        imprimir_tablero(tablero)
                if Casillero == 4:
                    if tablero[1][0] == '_':
                        tablero[1][0] = 'X' if turno_x else 'O'
                        break
                    elif tablero[1][0] == 'X' or 'O':
                        print('Casillero ocupado.')
                        imprimir_tablero(tablero)
                if Casillero == 5:
                    if tablero[1][1] == '_':
                        tablero[1][1] = 'X' if turno_x else 'O'
                        break
                    elif tablero[1][1] == 'X' or 'O':
                        print('Casillero ocupado.')
                        imprimir_tablero(tablero)
                if Casillero == 6:
                    if tablero[1][2] == '_':
                        tablero[1][2] = 'X' if turno_x else 'O'
                        break
                    elif tablero[1][2] == 'X' or 'O':
                        print('Casillero ocupado.')
                        imprimir_tablero(tablero)
                if Casillero == 7:
                    if tablero[2][0] == '_':
                        tablero[2][0] = 'X' if turno_x else 'O'
                        break
                    elif tablero[2][0] == 'X' or 'O':
                        print('Casillero ocupado.')
                        imprimir_tablero(tablero)
                if Casillero == 8:
                    if tablero[2][1] == '_':
                        tablero[2][1] = 'X' if turno_x else 'O'
                        break
                    elif tablero[2][1] == 'X' or 'O':
                        print('Casillero ocupado.')
                        imprimir_tablero(tablero)
                if Casillero == 9:
                    if tablero[2][2] == '_':
                        tablero[2][2] = 'X' if turno_x else 'O'
                        break
                    elif tablero[2][2] == 'X' or 'O':
                        print('Casillero ocupado.')
                        imprimir_tablero(tablero)
            else:
                print('Opcion no valida. Debe ingresar un numero del 1 al 9.')
                imprimir_tablero(tablero)
        except:
            print('Opcion invalida, debe ingresar una opcion del 1 al 9: ')
            imprimir_tablero(tablero)
    imprimir_tablero(tablero)
    if (tablero[0][0] == tablero[0][1] == tablero[0][2] and tablero[0][0] != '_' or tablero[1][0] == tablero[1][1] == tablero[1][2] and tablero[1][0] != '_' or tablero[2][0] == tablero[2][1] == tablero[2][2] and tablero[2][0] != '_' or tablero[0][0] == tablero[1][0] == tablero[2][0] and tablero[0][0] != '_' or tablero[0][1] == tablero[1][1] == tablero[2][1] and tablero[0][1] != '_' or tablero[0][2] == tablero[1][2] == tablero[2][2] and tablero[0][2] != '_' or tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != '_' or tablero[2][0] == tablero[1][1] == tablero[0][2] and tablero[2][0] != '_' ):
        print('El ganador es: X!!' if turno_x else 'El ganador es: O!!')
        juego_terminado = True
    if tablero [0][0] and tablero [0][1] and tablero [0][2] and tablero [1][0] and tablero [1][1] and tablero [1][2] and tablero [2][0] and tablero [2][1] and tablero [2][2] != '_':
        print('Empate! No quedan jugadas posibles para ganar.')
        continuar()
        juego_terminado = True
    turno_x = not turno_x

