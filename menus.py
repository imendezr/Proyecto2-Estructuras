import gato
from gato import pygame
from gato import sys


class Boton:
    # Misc
    FUENTE = ('cambria', 40)

    # Constructor
    def __init__(self, imagen, pos_x, pos_y, entrada_texto):
        pygame.init()
        self.fuente = pygame.font.SysFont(Boton.FUENTE[0], Boton.FUENTE[1])
        self.imagen = pygame.transform.scale(imagen, (470, 120))
        self.rect = self.imagen.get_rect(center=(pos_x, pos_y))
        self.entrada_texto = entrada_texto
        self.texto = self.fuente.render(self.entrada_texto, True, "white")
        self.rect_texto = self.texto.get_rect(center=(pos_x, pos_y))

    def update(self, pantalla):
        if self.imagen is not None:
            pantalla.blit(self.imagen, self.rect)
        pantalla.blit(self.texto, self.rect_texto)

    def comprobar_entrada(self, posicion):
        if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def cambiar_color(self, posicion):
        if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.texto = self.fuente.render(self.entrada_texto, True, "grey")
        else:
            self.texto = self.fuente.render(self.entrada_texto, True, "white")


class MenuCPU:
    # Assets
    BOTON_IMG = pygame.image.load("assets/boton2.png")

    # Misc
    ANCHO = 900
    ALTO = 900
    COLOR_FONDO = (214, 201, 227)

    def __init__(self):
        self.pantalla = pygame.display.set_mode((MenuCPU.ANCHO, MenuCPU.ALTO))
        self.boton = Boton(MenuCPU.BOTON_IMG, 450, 200, "Facil")
        self.boton2 = Boton(MenuCPU.BOTON_IMG, 450, 400, "Normal")
        self.boton3 = Boton(MenuCPU.BOTON_IMG, 450, 600, "Dificil")

    def mostrar(self):
        while True:
            pygame.display.set_caption('SELECCIONE LA DIFICULTAD')
            self.pantalla.fill(MenuCPU.COLOR_FONDO)

            self.boton.update(self.pantalla)
            self.boton2.update(self.pantalla)
            self.boton3.update(self.pantalla)

            self.boton.cambiar_color(pygame.mouse.get_pos())
            self.boton2.cambiar_color(pygame.mouse.get_pos())
            self.boton3.cambiar_color(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton.comprobar_entrada(pygame.mouse.get_pos()):
                        return True
                    if self.boton2.comprobar_entrada(pygame.mouse.get_pos()):
                        return True
                    if self.boton3.comprobar_entrada(pygame.mouse.get_pos()):
                        return gato.Gato().jugador_vs_cpu(3)

            pygame.display.update()


class MenuPrincipal:
    # Assets
    ICONO_IMG = pygame.image.load('assets/juego_gato.png')
    BOTON_IMG = pygame.image.load("assets/boton.png")

    # Misc
    ANCHO = 900
    ALTO = 900
    COLOR_FONDO = (214, 201, 227)

    def __init__(self):
        pygame.display.set_icon(MenuPrincipal.ICONO_IMG)
        self.pantalla = pygame.display.set_mode((MenuPrincipal.ANCHO, MenuPrincipal.ALTO))
        self.boton = Boton(MenuPrincipal.BOTON_IMG, 450, 200, "Jugador vs Jugador")
        self.boton2 = Boton(MenuPrincipal.BOTON_IMG, 450, 400, "Jugador vs Maquina")
        self.boton3 = Boton(MenuPrincipal.BOTON_IMG, 450, 600, "Salir")

    def mostrar(self):
        delay = False
        while True:
            pygame.display.set_caption('JUEGO DEL GATO')
            self.pantalla.fill(MenuPrincipal.COLOR_FONDO)

            self.boton.update(self.pantalla)
            self.boton2.update(self.pantalla)
            self.boton3.update(self.pantalla)

            self.boton.cambiar_color(pygame.mouse.get_pos())
            self.boton2.cambiar_color(pygame.mouse.get_pos())
            self.boton3.cambiar_color(pygame.mouse.get_pos())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.boton.comprobar_entrada(pygame.mouse.get_pos()):
                        if not delay:
                            delay = gato.Gato().jugador_vs_jugador()
                    if self.boton2.comprobar_entrada(pygame.mouse.get_pos()):
                        if not delay:
                            delay = MenuCPU().mostrar()
                    if self.boton3.comprobar_entrada(pygame.mouse.get_pos()):
                        if not delay:
                            pygame.quit()
                            sys.exit()
            delay = False

            pygame.display.update()
