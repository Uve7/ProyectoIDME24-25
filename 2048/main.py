#importacion de librerias
from os import system 
import pygame 
import constantes
import sys

print(dir(constantes))
print(dir(constantes))
#inicializacion de Pygame
pygame.init()

#creacion de la pantalla
screen = pygame.display.set_mode((constantes.ScreenWidth, constantes.ScreenHeight))

#titulo del juego
pygame.display.set_caption("2048")

#creacion de matriz para el tablero
tablero = [[0] * 4 for _ in range(4)] #crea los elementos numéricos a 0 para que no se muestren

#variable que controla el estado del juego
gameOver = False
gameWon = False

#funciones necesarias para el juego
def dibujaPantalla (): #pone en blanca la pantalla
    screen.fill(constantes.blanco)

#controla la pantalla segun los eventos que ocurran
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #evento que cierra la pantalla al pulsar la X
            pygame.quit() 
    dibujaPantalla()
    pygame.display.flip()

           
    
