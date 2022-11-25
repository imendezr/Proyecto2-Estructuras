#from Modulo_Jug_Jug import *
import pygame, sys

from pygame.locals import *



#inicio
pygame.init()
SCREEN = pygame.display.set_mode((900, 900))
#boton
main_font = pygame.font.SysFont("cambria", 50)

#icono
pygame.display.set_caption('Juego del gato')
icono = pygame.image.load('gatoimagen.png')
pygame.display.set_icon(icono)


#imagenes
BOARD = pygame.image.load("Board.png")
X_IMG = pygame.image.load("X.png")
O_IMG = pygame.image.load("O.png")

#colores
BG_COLOR = (214,201,227)



board = [[1,2,3], [4,5,6], [7,8,9]]
graphical_board = [[[None,None], [None,None], [None,None]],
                    [[None,None], [None,None],[None,None]],
                    [[None,None], [None,None],[None,None]]]
to_move = 'X'


#llenar pantalla
SCREEN.fill(BG_COLOR)
SCREEN.blit(BOARD, (64,64))


#actualizar pantalla
pygame.display.update()

#pantalla1
class Button():

    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    #actualiza
    def update(self):
        SCREEN.blit(self.image, self.rect)
        SCREEN.blit(self.text, self.text_rect)

    #revisa el boton
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("Button Press!")
            return 1;



    #cambia color de letra
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "grey")
        else:
            self.text = main_font.render(self.text_input, True, "white")


button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (470, 120))
button = Button(button_surface, 400, 200, "Jugador vs Jugador")
button1 = Button(button_surface, 400, 400, "Jugador vs Maquina")
button2 = Button(button_surface, 400, 600, "Salir")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())

    SCREEN.fill(BG_COLOR)

    button.update()
    button1.update()
    button2.update()

    button.changeColor(pygame.mouse.get_pos())
    button1.changeColor(pygame.mouse.get_pos())
    button2.changeColor(pygame.mouse.get_pos())



    pygame.display.update()



'''
#codigo sin interfaz
class Gato:

    def __init__(self):
        self.j1_simbolo = ''
        self.j2_simbolo = ''
        self.turno = 0

    def disposicion_tablero(self):
        print("-----------")
        print(' 1' + ' |' + ' 2' + ' |' + ' 3')
        print("-----------")
        print(' 4' + ' |' + ' 5' + ' |' + ' 6')
        print("-----------")
        print(' 7' + ' |' + ' 8' + ' |' + ' 9')
        print("-----------")

    def mostrar_tablero(self, tablero):
        print("-----------")
        print(" " + tablero[1] + " |" + " " + tablero[2] + " |" + " " + tablero[3])
        print("-----------")
        print(" " + tablero[4] + " |" + " " + tablero[5] + " |" + " " + tablero[6])
        print("-----------")
        print(" " + tablero[7] + " |" + " " + tablero[8] + " |" + " " + tablero[9])
        print("-----------")

    def elegir_entrada(self):
        simbolo = " "
        while simbolo != "x" or simbolo != "o":
            simbolo = input("Jugador 1 elige x,o: ")

            if simbolo == "o":
                self.j1_simbolo = 'o'
                self.j2_simbolo = 'x'
                break
            elif simbolo == "x":
                self.j1_simbolo = 'x'
                self.j2_simbolo = 'o'
                break
            else:
                print("Entrada invalida!\n")

    def primer_turno(self):
        if random.randint(0, 1) == 0:
            print("\nJugador 2 comenzara el juego")
            self.turno = 2

        else:
            print("\nJugador 1 comenzara el juego")
            self.turno = 1


    def turno_jugador(self, tablero, simbolo, posicion):
        tablero[posicion] = simbolo

    def espacio_libre(self, tablero, posicion):
        return tablero[posicion] == " "

    def tablero_lleno(self, tablero):
        for i in range(1, 10):
            if self.espacio_libre(tablero, i):
                return False
        return True

    def elegir_posicion(self, tablero):
        posicion = 0

        while posicion not in range(1, 10) or not self.espacio_libre(tablero, posicion):
            posicion = int(input('Elige la posicion para tu siguiente jugada (1-9): '))
        return posicion

    def verificar_ganador(self, tablero, simbolo):
        return ((tablero[7] == simbolo and tablero[8] == simbolo and tablero[9] == simbolo) or
                (tablero[4] == simbolo and tablero[5] == simbolo and tablero[6] == simbolo) or
                (tablero[1] == simbolo and tablero[2] == simbolo and tablero[3] == simbolo) or
                (tablero[7] == simbolo and tablero[4] == simbolo and tablero[1] == simbolo) or
                (tablero[8] == simbolo and tablero[5] == simbolo and tablero[2] == simbolo) or
                (tablero[9] == simbolo and tablero[6] == simbolo and tablero[3] == simbolo) or
                (tablero[7] == simbolo and tablero[5] == simbolo and tablero[3] == simbolo) or
                (tablero[9] == simbolo and tablero[5] == simbolo and tablero[1] == simbolo))

    opciones_menu_principal = {
        1: 'Jugador vs Jugador',
        2: 'Jugador vs CPU',
        3: 'Salir',
    }

    opciones_menu_cpu = {
        1: 'Facil',
        2: 'Normal',
        3: 'Dificil',
    }

    def mostrar_menu_principal(self):
        print('Que desea hacer?')
        for key in self.opciones_menu_principal.keys():
            print(key, '--', self.opciones_menu_principal[key])

    def mostrar_menu_cpu(self):
        print('Seleccione la dificultad:')
        for key in self.opciones_menu_cpu.keys():
            print(key, '--', self.opciones_menu_cpu[key])

    def opcion1(self):
        while True:
            tableroJuego = [' '] * 10
            self.elegir_entrada()
            # turno = self.primer_turno()
            self.primer_turno()
            partida_en_curso = True

            while partida_en_curso:
                if self.turno == 1:
                    self.mostrar_tablero(tableroJuego)
                    print("Jugador 1")
                    posicion = self.elegir_posicion(tableroJuego)
                    self.turno_jugador(tableroJuego, self.j1_simbolo, posicion)

                    if self.verificar_ganador(tableroJuego, self.j1_simbolo):
                        self.mostrar_tablero(tableroJuego)
                        print('Felicitaciones! Jugador 1 ha ganado.')
                        partida_en_curso = False
                    else:
                        if self.tablero_lleno(tableroJuego):
                            self.mostrar_tablero(tableroJuego)
                            print('Empate!')
                            break
                        else:
                            self.turno = 2
                elif self.turno == 2:
                    self.mostrar_tablero(tableroJuego)
                    print("Jugador 2")
                    posicion = self.elegir_posicion(tableroJuego)
                    self.turno_jugador(tableroJuego, self.j2_simbolo, posicion)

                    if self.verificar_ganador(tableroJuego, self.j2_simbolo):
                        self.mostrar_tablero(tableroJuego)
                        print('Felicitaciones! Jugador 2 ha ganado.')
                        partida_en_curso = False
                    else:
                        if self.tablero_lleno(tableroJuego):
                            self.mostrar_tablero(tableroJuego)
                            print('Empate!')
                            break
                        else:
                            self.turno = 1
            self.j1_simbolo = ''
            self.j2_simbolo = ''
            self.turno = 0
            break

    def opcion2(self):
        while (True):
            self.mostrar_menu_cpu()
            opcion = ''
            try:
                opcion = int(input('Ingrese su eleccion: '))
            except:
                print('Entrada invalida. Por favor ingrese un numero ...')
            if opcion == 1:
                print('Falta de programar')
                exit()
            elif opcion == 2:
                print('Falta de programar')
                exit()
            elif opcion == 3:
                print('Falta de programar')
                exit()
            else:
                print('Opcion invalida. Por favor ingrese un numero del 1 al 3.')


    def iniciar(self):
        print("BIENVENIDO AL JUEGO DEL GATO\n")
        print("Esta es la disposicion del tablero:")
        self.disposicion_tablero()
        print("\nInstrucciones:")
        print("Cuando sea su turno, ingrese un numero (1-9) para indicar la posicion que desea jugar.\n")

        while (True):
            self.mostrar_menu_principal()
            opcion = ''
            try:
                opcion = int(input('Ingrese su eleccion: '))
            except:
                print('Entrada invalida. Por favor ingrese un numero ...')
            if opcion == 1:
                print('\n'*30) # alternativa a cls (no funciona en pycharm)
                self.opcion1()
            elif opcion == 2:
                print('\n'*30) # alternativa a cls (no funciona en pycharm)
                self.opcion2()
            elif opcion == 3:
                print('\n' * 30)  # alternativa a cls (no funciona en pycharm)
                print('Saliendo de la aplicacion')
                exit()
            else:
                print('Opcion invalida. Por favor ingrese un numero del 1 al 3.')

'''