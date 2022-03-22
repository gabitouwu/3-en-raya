import random

def dibujarTablero(tablero):
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   |')

def ingresaLetraJugador():
    letra = ''
    while not (letra == 'X' or letra == 'O'):
        letra = input('¿Deseas ser X o O?\n').upper()

    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienComienza():
    if random.randint(0, 1) == 0:
        return 'La computadora'
    else:
        return 'El jugador'
0
def jugarDeNuevo():
    r = input('¿Deseas volver a jugar? (S/N)\n')
    if r == '':
        return True

    if r.startswith('s') or r.startswith('S'):
        return True
    else:
        return False
 
def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra

def esGanador(ta, le):
    return ((ta[7] == le and ta[8] == le and ta[9] == le) or #horizontal
            (ta[4] == le and ta[5] == le and ta[6] == le) or #horizontal medio
            (ta[1] == le and ta[2] == le and ta[3] == le) or #horizontal inferior
            (ta[7] == le and ta[4] == le and ta[1] == le) or #vertical izquierda
            (ta[8] == le and ta[5] == le and ta[2] == le) or #vertical medio
            (ta[9] == le and ta[6] == le and ta[3] == le) or #vertical derecha
            (ta[7] == le and ta[5] == le and ta[3] == le) or #diagonal
            (ta[9] == le and ta[5] == le and ta[1] == le)) #diagonal

def obtenerDuplicadoTablero(tablero):
    dupTablero = []

    for i in tablero:
        dupTablero.append(i)

    return dupTablero

def hayEspacioLibre(tablero, jugada):
    return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero):
    jugada = ' '
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('¿Cuál es tu próxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elegirAzarDeLista(tablero, listaJugada):
    jugadasPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero, i):
            jugadasPosibles.append(i)

    if len(jugadasPosibles) != 0:
        return random.choice(jugadasPosibles)
    else:
        return None

def obtenerJugadaComputadora(tablero, letraComputadora):
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'

    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)
            if esGanador(copia, letraComputadora):
                return i

    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(tablero, i):
            hacerJugada(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i

    jugada = elegirAzarDeLista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada

    if hayEspacioLibre(tablero, 5):
        return 5

    return elegirAzarDeLista(tablero, [2, 4, 6, 8])
    
def tableroCompleto(tablero):
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True

print('¡Bienvenido al Ta Te Ti!')

while True:
    elTablero = [' '] * 10

    letraJugador, letraComputadora = ingresaLetraJugador()

    turno = quienComienza()
    print(turno + ' irá primero.')

    juegoEnCurso = True

    while juegoEnCurso:
        if turno == 'El jugador':
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)
            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('¡Felicidades, has ganado!')
                juegoEnCurso = False

            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'La computadora'
        else:
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            hacerJugada(elTablero, letraComputadora, jugada)

            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('¡La computadora te ha vencido! Has perdido.')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'El jugador'

    if not jugarDeNuevo():
        break

