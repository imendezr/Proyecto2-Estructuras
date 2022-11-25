import random

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

