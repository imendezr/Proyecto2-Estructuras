import pygame
import sys
import time
import random


class Gato:
    # Assets
    #ICONO_IMG = pygame.image.load('assets/juego_gato.png')
    TABLERO_IMG = pygame.image.load("assets/tablero.png")
    X_IMG = pygame.image.load("assets/X.png")
    O_IMG = pygame.image.load("assets/O.png")

    # Misc
    ANCHO = 900
    ALTO = 900
    COLOR_FONDO = (214, 201, 227)

    # Constructor
    def __init__(self):
        self.pantalla = pygame.display.set_mode((Gato.ANCHO, Gato.ALTO))
        self.tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.tablero_grafico = [[[None, None], [None, None], [None, None]],
                                [[None, None], [None, None], [None, None]],
                                [[None, None], [None, None], [None, None]]]
        self.ficha = 'X'

    def renderizar_tablero(self, tablero, x_img, o_img):
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == 'X':  # Crea imagen de X
                    self.tablero_grafico[i][j][0] = x_img
                    self.tablero_grafico[i][j][1] = x_img.get_rect(center=(j * 300 + 150, i * 300 + 150))
                elif tablero[i][j] == 'O':  # Crea imagen de O
                    self.tablero_grafico[i][j][0] = o_img
                    self.tablero_grafico[i][j][1] = o_img.get_rect(center=(j * 300 + 150, i * 300 + 150))

    def agregar_ficha(self, tablero, tablero_grafico, ficha):
        pos_actual = pygame.mouse.get_pos()
        x_convertida = (pos_actual[0] - 65) / 835 * 2
        y_convertida = pos_actual[1] / 835 * 2
        if tablero[round(y_convertida)][round(x_convertida)] != 'O' and tablero[round(y_convertida)][round(x_convertida)] != 'X':
            tablero[round(y_convertida)][round(x_convertida)] = ficha
            if ficha == 'O':
                ficha = 'X'
            else:
                ficha = 'O'

        self.renderizar_tablero(tablero, Gato.X_IMG, Gato.O_IMG)

        for i in range(3):
            for j in range(3):
                if tablero_grafico[i][j][0] is not None:
                    self.pantalla.blit(tablero_grafico[i][j][0], tablero_grafico[i][j][1])

        return tablero, ficha

    def agregar_ficha_cpu(self, tablero, tablero_grafico, ficha, pos):
        pos_x = pos[0]
        pos_y = pos[1]
        if tablero[round(pos_x)][round(pos_y)] != 'O' and tablero[round(pos_x)][round(pos_y)] != 'X':
            tablero[round(pos_x)][round(pos_y)] = ficha
            if ficha == 'O':
                ficha = 'X'
            else:
                ficha = 'O'

        self.renderizar_tablero(tablero, Gato.X_IMG, Gato.O_IMG)

        for i in range(3):
            for j in range(3):
                if tablero_grafico[i][j][0] is not None:
                    self.pantalla.blit(tablero_grafico[i][j][0], tablero_grafico[i][j][1])

        return tablero, ficha

    def verificar_ganador(self, tablero):
        ganador = None
        # horizontal
        for row in range(0, 3):
            if (tablero[row][0] == tablero[row][1] == tablero[row][2]) and (tablero[row][0] is not None):
                ganador = tablero[row][0]
                for i in range(0, 3):
                    self.tablero_grafico[row][i][0] = pygame.image.load(f"assets/ganador {ganador}.png")
                    self.pantalla.blit(self.tablero_grafico[row][i][0], self.tablero_grafico[row][i][1])
                pygame.display.update()
                return ganador
        # vertical
        for col in range(0, 3):
            if (tablero[0][col] == tablero[1][col] == tablero[2][col]) and (tablero[0][col] is not None):
                ganador = tablero[0][col]
                for i in range(0, 3):
                    self.tablero_grafico[i][col][0] = pygame.image.load(f"assets/ganador {ganador}.png")
                    self.pantalla.blit(self.tablero_grafico[i][col][0], self.tablero_grafico[i][col][1])
                pygame.display.update()
                return ganador
        # diagonal izq-der
        if (tablero[0][0] == tablero[1][1] == tablero[2][2]) and (tablero[0][0] is not None):
            ganador = tablero[0][0]
            self.tablero_grafico[0][0][0] = pygame.image.load(f"assets/ganador {ganador}.png")
            self.pantalla.blit(self.tablero_grafico[0][0][0], self.tablero_grafico[0][0][1])
            self.tablero_grafico[1][1][0] = pygame.image.load(f"assets/ganador {ganador}.png")
            self.pantalla.blit(self.tablero_grafico[1][1][0], self.tablero_grafico[1][1][1])
            self.tablero_grafico[2][2][0] = pygame.image.load(f"assets/ganador {ganador}.png")
            self.pantalla.blit(self.tablero_grafico[2][2][0], self.tablero_grafico[2][2][1])
            pygame.display.update()
            return ganador
        # diagonal der-izq
        if (tablero[0][2] == tablero[1][1] == tablero[2][0]) and (tablero[0][2] is not None):
            ganador = tablero[0][2]
            self.tablero_grafico[0][2][0] = pygame.image.load(f"assets/ganador {ganador}.png")
            self.pantalla.blit(self.tablero_grafico[0][2][0], self.tablero_grafico[0][2][1])
            self.tablero_grafico[1][1][0] = pygame.image.load(f"assets/ganador {ganador}.png")
            self.pantalla.blit(self.tablero_grafico[1][1][0], self.tablero_grafico[1][1][1])
            self.tablero_grafico[2][0][0] = pygame.image.load(f"assets/ganador {ganador}.png")
            self.pantalla.blit(self.tablero_grafico[2][0][0], self.tablero_grafico[2][0][1])
            pygame.display.update()
            return ganador

        if ganador is None:
            for i in range(len(tablero)):
                for j in range(len(tablero)):
                    if tablero[i][j] != 'X' and tablero[i][j] != 'O':
                        return None
            return "EMPATE"

    def jugador_vs_jugador(self):
        pygame.display.set_caption('JUGADOR VS JUGADOR')
        self.pantalla.fill(Gato.COLOR_FONDO)
        self.pantalla.blit(Gato.TABLERO_IMG, (64, 64))
        pygame.display.update()
        partida_finalizada = False

        # Bucle j1 vs j2
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.tablero, self.ficha = self.agregar_ficha(self.tablero, self.tablero_grafico, self.ficha)

                    if partida_finalizada:
                        return True

                    if self.verificar_ganador(self.tablero) is not None:
                        partida_finalizada = True

                    pygame.display.update()

    def movimientos_restantes(self, tablero_grafico):
        for i in range(3):
            for j in range(3):
                if tablero_grafico[i][j][0] is None:
                    return True
        return False

    def evaluar(self, tablero_grafico):
        # Verificando filas para victoria de X , O.
        for row in range(3):
            if (tablero_grafico[row][0] == tablero_grafico[row][1] and tablero_grafico[row][1] == tablero_grafico[row][2]):
                if (tablero_grafico[row][0][0] == 'X'):
                    return 10
                elif (tablero_grafico[row][0][0] == 'O'):
                    return -10

        # Verificando columnas para victoria de X , O.
        for col in range(3):

            if (tablero_grafico[0][col] == tablero_grafico[1][col] and tablero_grafico[1][col] == tablero_grafico[2][col]):

                if (tablero_grafico[0][col][0] == 'X'):
                    return 10
                elif (tablero_grafico[0][col][0] == 'O'):
                    return -10

        # Verificando diagonales para victoria de X , O.
        if (tablero_grafico[0][0] == tablero_grafico[1][1] and tablero_grafico[1][1] == tablero_grafico[2][2]):

            if (tablero_grafico[0][0][0] == 'X'):
                return 10
            elif (tablero_grafico[0][0][0] == 'O'):
                return -10

        if (tablero_grafico[0][2] == tablero_grafico[1][1] and tablero_grafico[1][1] == tablero_grafico[2][0]):

            if (tablero_grafico[0][2][0] == 'X'):
                return 10
            elif (tablero_grafico[0][2][0] == 'O'):
                return -10

        # Si ninguno ha ganado
        return 0

    # Considera todas las posibles jugadas
    def minimax(self, tablero_grafico, profundidad, turno_max):
        puntaje = self.evaluar(tablero_grafico)

        # si max ha ganado retorna su puntaje
        if (puntaje == 10):
            return puntaje

        # si min ha ganado retorna su puntaje
        if (puntaje == -10):
            return puntaje

        # si no hay ganador ni movimientos restantes es empate
        if (self.movimientos_restantes(tablero_grafico) == False):
            return 0

        # Turno maximizador
        if (turno_max):
            mejor = -1000

            for i in range(3):
                for j in range(3):

                    if (tablero_grafico[i][j][0] is None):
                        # Hace el movimiento
                        tablero_grafico[i][j][0] = 'X'

                        # Valor maximo con recursion
                        mejor = max(mejor, self.minimax(tablero_grafico,
                                                      profundidad + 1,
                                                      not turno_max))

                        # Deshace el movimiento
                        tablero_grafico[i][j][0] = None
            return mejor

        # Turno minimizador
        else:
            mejor = 1000

            for i in range(3):
                for j in range(3):

                    if (tablero_grafico[i][j][0] is None):
                        # Hace el movimiento
                        tablero_grafico[i][j][0] = 'O'

                        # Valor minimo con recursion
                        mejor = min(mejor, self.minimax(tablero_grafico, profundidad + 1, not turno_max))

                        # Deshace el movimiento
                        tablero_grafico[i][j][0] = None
            return mejor

    # Retorna mejor movimiento para el jugador
    def buscar_mejor_movimiento(self, tablero_grafico):
        mejor_valor = -1000
        mejor_movimiento = (-1, -1)

        # Recorre el tablero, evalua funcion minmax para espacios vacios
        for i in range(3):
            for j in range(3):

                if (tablero_grafico[i][j][0] is None):
                    # Hace el movimiento
                    tablero_grafico[i][j][0] = 'X'

                    # Evalua movimiento
                    valor_movimiento = self.minimax(tablero_grafico, 0, False)

                    # Deshace el movimiento
                    tablero_grafico[i][j][0] = None

                    if valor_movimiento > mejor_valor:
                        mejor_movimiento = (i, j)
                        mejor_valor = valor_movimiento

        #print("Valor del mejor movimiento es:", mejor_valor)
        #print()
        return mejor_movimiento # Retorna posicion con valor optimo

    def jugador_vs_cpu(self, dificultad):
        pygame.display.set_caption('JUGADOR VS CPU')
        self.pantalla.fill(Gato.COLOR_FONDO)
        self.pantalla.blit(Gato.TABLERO_IMG, (64, 64))
        pygame.display.update()
        partida_finalizada = False

        # Bucle j1 vs cpu
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.ficha == 'X' and event.type == pygame.MOUSEBUTTONDOWN:
                    self.tablero, self.ficha = self.agregar_ficha(self.tablero, self.tablero_grafico, self.ficha)

                    if partida_finalizada:
                        return True

                    if self.verificar_ganador(self.tablero) is not None:
                        partida_finalizada = True

                    pygame.display.update()

                elif self.ficha == 'O':
                    if dificultad == 1:
                        mejor_movimiento = self.movimiento_cpu(self.tablero, 'O', 1)
                        mejor_movimiento = self.convertir_pos(mejor_movimiento)
                        self.tablero, self.ficha = self.agregar_ficha_cpu(self.tablero, self.tablero_grafico,
                                                                          self.ficha, mejor_movimiento)

                        if partida_finalizada:
                            return True

                        if self.verificar_ganador(self.tablero) is not None:
                            partida_finalizada = True

                        pygame.display.update()

                    if dificultad == 2:
                        mejor_movimiento = self.movimiento_cpu(self.tablero, 'O', 2)
                        mejor_movimiento = self.convertir_pos(mejor_movimiento)
                        self.tablero, self.ficha = self.agregar_ficha_cpu(self.tablero, self.tablero_grafico,
                                                                          self.ficha, mejor_movimiento)

                        if partida_finalizada:
                            return True

                        if self.verificar_ganador(self.tablero) is not None:
                            partida_finalizada = True

                        pygame.display.update()

                    if dificultad == 3:
                        mejor_movimiento = self.buscar_mejor_movimiento(self.tablero_grafico)
                        self.tablero, self.ficha = self.agregar_ficha_cpu(self.tablero, self.tablero_grafico, self.ficha, mejor_movimiento)

                        if partida_finalizada:
                            return True

                        if self.verificar_ganador(self.tablero) is not None:
                            partida_finalizada = True

                        pygame.display.update()

    def convertir_pos(self, pos):

        if pos == 1:
            return [2, 0]
        elif pos == 2:
            return [2, 1]
        elif pos == 3:
            return [2, 2]
        elif pos == 4:
            return [1, 0]
        elif pos == 5:
            return [1, 1]
        elif pos == 6:
            return [1, 2]
        elif pos == 7:
            return [0, 0]
        elif pos == 8:
            return [0, 1]
        elif pos == 9:
            return [0, 2]

    def espacio_disponible(self, tablero, movimiento):
        return tablero[movimiento] != 'X' or 'O'

    def copiar_tablero(self, tablero):
        copia_tablero = []
        for i in tablero:
            copia_tablero.append(i)
        return copia_tablero

    def probar_movimiento_ganador(self, tablero, letra, movimiento):
        copia_tablero = self.copiar_tablero(tablero)
        self.realizar_movimiento_cpu(copia_tablero, letra, movimiento)
        return self.es_ganador(copia_tablero, letra)

    def probar_movimiento(self, tablero, letra, movimiento):
        copia_tablero = self.copiar_tablero(tablero)
        self.realizar_movimiento_cpu(copia_tablero, letra, movimiento)
        movimientos_ganadores = 0
        for j in range(1, 10):
            if self.probar_movimiento_ganador(copia_tablero, letra, j) and self.espacio_disponible(copia_tablero, j):
                movimientos_ganadores += 1
        return movimientos_ganadores > 1

    def es_ganador(self, tablero, letra):
        return ((tablero[7] == letra and tablero[8] == letra and tablero[9] == letra) or
                (tablero[4] == letra and tablero[5] == letra and tablero[6] == letra) or
                (tablero[1] == letra and tablero[2] == letra and tablero[3] == letra) or
                (tablero[7] == letra and tablero[4] == letra and tablero[1] == letra) or
                (tablero[8] == letra and tablero[5] == letra and tablero[2] == letra) or
                (tablero[9] == letra and tablero[6] == letra and tablero[3] == letra) or
                (tablero[7] == letra and tablero[5] == letra and tablero[3] == letra) or
                (tablero[9] == letra and tablero[5] == letra and tablero[1] == letra))

    def realizar_movimiento_cpu(self, tablero, letra, movimiento):
        tablero[movimiento] = letra

    def chooseRandomMoveFromList(self, tablero, lista_movimientos):
        movimientos_posibles = []
        for i in lista_movimientos:
            if self.espacio_disponible(tablero, i):
                movimientos_posibles.append(i)

        if len(movimientos_posibles) != 0:
            return random.choice(movimientos_posibles)
        else:
            return None

    def movimiento_cpu(self, tablero, letra_cpu, dificultad):
        if letra_cpu == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        for i in range(1, 10):
            if self.espacio_disponible(tablero, i) and self.probar_movimiento_ganador(tablero, letra_cpu, i):
                return i

        for i in range(1, 10):
            if self.espacio_disponible(tablero, i) and self.probar_movimiento_ganador(tablero, playerLetter, i):
                return i

        if dificultad == 2:
            for i in range(1, 10):
                if self.espacio_disponible(tablero, i) and self.probar_movimiento(tablero, letra_cpu, i):
                    return i

            for i in range(1, 10):
                if self.espacio_disponible(tablero, i) and self.probar_movimiento(tablero, playerLetter, i):
                    return i

        move = self.chooseRandomMoveFromList(tablero, [1, 3, 7, 9])
        if move is not None:
            return move

        if self.espacio_disponible(tablero, 5):
            return 5

        return self.chooseRandomMoveFromList(tablero, [2, 4, 6, 8])
