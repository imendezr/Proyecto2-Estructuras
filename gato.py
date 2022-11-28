import pygame
import sys


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
        return mejor_movimiento # Retorna espacio con valor optimo

    def jugador_vs_cpu(self, level):
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
                    if level == 3:
                        mejor_movimiento = self.buscar_mejor_movimiento(self.tablero_grafico)
                        self.tablero, self.ficha = self.agregar_ficha_cpu(self.tablero, self.tablero_grafico, self.ficha, mejor_movimiento)

                        if partida_finalizada:
                            return True

                        if self.verificar_ganador(self.tablero) is not None:
                            partida_finalizada = True

                        pygame.display.update()
