from os import system 
import pygame #importacion de la libreria pygame
import constantes


print(dir(constantes))
#inicializacion de Pygame
pygame.init()

#creacion de la pantalla
screen = pygame.display.set_mode((constantes.ScreenWidth, constantes.ScreenHeight))

#titulo del juego
pygame.display.set_caption("2048")

#controla la pantalla segun los eventos que ocurran
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
           
    
