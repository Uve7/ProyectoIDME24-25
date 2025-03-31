#importacion de librerias
from os import system 
import pygame 
import constantes
import sys

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
def dibujaPantalla (): #controla parámetros de la pantalla
    screen.fill(constantes.blanco) #llama a la constante blanco para poner la pantalla en blanco
    
    font = pygame.font.Font(None,40) #creación de una fuente específica
    fuenteMensaje = pygame.font.Font(None, 30) #creción de una fuente para los mensajes

    for i in range(4): #control del valor de cada celda
        for j in range(4):
            value = tablero [i][j]
            color = constantes.colors.get(value, constantes.colors[0]) #pone cad avalor en el color especificado en constantes
            
            #dibuja cada celda, rect dice que es un rectángulo. Coge las coordenadas y el color especificado
            pygame.draw.rect(screen, color,
                             (j * constantes.CellSize, #coordenada 
                              i * constantes.CellSize, #coordenada
                                  constantes.CellSize, 
                                  constantes.CellSize, #widht:0
                              ))
            if value != 0: #hay que dibujar el numero cuando sea distinto de 0
                text = font.render(str(value), True, constantes.negro) #convertimos el valor a string, el true es para suavizar y cogemos la cosntante negro
                
                #pone el texto en el centro de la celda
                text_rect = text.get_rect(j * constantes.CellSize + constantes.CellSize //2, 
                                           i* constantes.CellSize + constantes.CellSize //2) 
                #blit dibuja una imagen dentro de otra, el texto text en la coordenada text_rect
                screen.blit(text,text_rect) 

            #diferentes mensajes dependiendo de si ganas o pierdes                    
            if gameWon:
                text = fuenteMensaje.render("¡Enhorabuena! Has ganado, presiona R para reiniciar", True, constantes.rojo) #mensaje, suavizado, color
                screen.blit(text, (50, constantes.ScreenHeight // 2-20)) #posicion del texto
            elif gameOver:
                text = fuenteMensaje.render("¡Eres malísima¡ Has perdido, presiona R para reinicar.", True, constantes.rojo)
                screen.blit(text, (50, constantes.ScreenHeight // 2-20))

              
#controla la pantalla segun los eventos que ocurran
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #evento que cierra la pantalla al pulsar la X
            pygame.quit() 
            sys.exit()
    dibujaPantalla() #llama a la funcion
    pygame.display.flip() #actualiza la pantalla




           
    
