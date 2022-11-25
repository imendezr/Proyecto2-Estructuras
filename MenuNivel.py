import pygame, sys
from pygame.locals import *



#inicio
pygame.init()
SCREEN = pygame.display.set_mode((900, 800))
#boton
main_font = pygame.font.SysFont("cambria", 40)

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
button = Button(button_surface, 400, 200, "Facil")
button1 = Button(button_surface, 400, 400, "Normal")
button2 = Button(button_surface, 400, 600, "Dificil")



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


