#importacion de librerias
from os import system 
import pygame 
import constantes
import sys
import random
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
#controla parámetros de la pantalla
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
                text_rect = text.get_rect(center=(j * constantes.CellSize + constantes.CellSize //2, 
                                           i* constantes.CellSize + constantes.CellSize //2)) 
                #blit dibuja una imagen dentro de otra, el texto text en la coordenada text_rect
                screen.blit(text,text_rect) 

            #diferentes mensajes dependiendo de si ganas o pierdes                    
            if gameWon:
                text = fuenteMensaje.render("¡Enhorabuena! Has ganado, presiona R para reiniciar", True, constantes.rojo) #mensaje, suavizado, color
                screen.blit(text, (50, constantes.ScreenHeight // 2-20)) #posicion del texto
            elif gameOver:
                text = fuenteMensaje.render("¡Eres malísima¡ Has perdido, presiona R para reinicar.", True, constantes.rojo)
                screen.blit(text, (50, constantes.ScreenHeight // 2-20))

#genera nuevo numero en cada celda cuando es 0
def generateNewNumber():
    empty = [(i,j) for i in range(4) for j in range (4) if tablero[i][j] == 0 ]
    
    #pregunta cuando algo esta vacio
    if empty:
        i, j = random.choice(empty) #genera en una celda vacía aletoria
        tablero[i][j]=random.choice([2, 4]) #genera un numero aletorio entre 2 y 4 en la celda anterior 

#guarda en una lista todos los numeros que no son 0
def compress(nums):
    newNums = [num for num in nums if num !=0] #itera en una lista los numeros que no son 0
    nums[:] = newNums + [0] * (4-len(newNums)) #guarda los numeros 

#combinacion de los numeros iguales
def merge(nums):
    for i in range(3):
        if nums [i] == nums [i + 1] and nums [i] !=0: 
            nums[i] *= 2  #multiplica por 2 cuando las celdas son iguales 
            nums[i+1] = 0 #controla que cuando es 0 no pase

#funcion para mover hacia la izquierda
def moveLeft():
    moved = False #indica que todavia no se ha movido
    for i in range(4):
        original =tablero[i][:] #coge las filas completas, sin contar la columna
        #compress y merge hace que se compriman y expandan las filas
        compress(tablero[i])
        merge(tablero[i])
        compress(tablero[i])
        #compara el tablero actual con el movimiento
        if original != tablero[i]:
            moved = True
    return moved
    
#funcion para mover hacia la derecha
def moveRight():
    moved = False
    for i in range(4):
        original =tablero[i][:]
        tablero[i].reverse() #a la vuelta la tablero para poder mover las columnas hacia el otro lado
        compress(tablero[i])
        merge(tablero[i])
        compress(tablero[i])
        tablero[i].reverse()
        if original != tablero[i]:
            moved = True
    return moved
    
#funcion para mover hacia arriba
def moveUp():
    moved = False
    for j in range(4):
        #genera una lista con las columna
        column = [tablero[i][j] for i in range(4)]
        original = column[:]
        compress(column)
        merge(column)
        compress(column) 
        for i in range(4):
            tablero[i][j]  = column[i]     
        if original != column:
            moved = True
    return moved

#funcion para mover hacia arriba
def moveDown():
    moved = False
    for j in range(4):
        #genera una lista con las columna
        column = [tablero[i][j] for i in range(4)]
        original = column[:]
        column.reverse()
        compress(column)
        merge(column)
        compress(column)
        column.reverse() 
        for i in range(4):
            tablero[i][j]  = column[i]     
        if original != column:
            moved = True
    return moved

#funciona controla la condicion de victoria
def checkkWin():
    return any(2048 in row for row in tablero)

#funcion que controla la condicion de derrota
def checkLoss():
    if any(0 in row for row in tablero):
        return False
    for i in range(4):
        for j in range(3):
            if tablero[i][j] == tablero[i][j+1] or tablero[j][i] == tablero [j + 1][i]:
                return False
    return True

#resetea el juego
def resetGame():
    global tablero, gameOver, gameWon
    tablero = [[0] * 4 for _ in range(4)]
    gameOver = False
    gameWon = False
    generateNewNumber()
    generateNewNumber()

resetGame()

#controla la pantalla segun los eventos que ocurran
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #evento que cierra la pantalla al pulsar la X
            pygame.quit() 
            sys.exit()
        elif event.type == pygame.KEYDOWN: #evento que controla cuando se presiona una tecla
            if event.key == pygame.K_r:
                resetGame()
            if not gameOver and not gameWon: #controla los eventos necesarios para mover el tablero
                moved = False
                if event.key == pygame.K_LEFT:
                    moved = moveLeft()
                elif event.key == pygame.K_RIGHT:
                   moved = moveRight()
                elif event.key == pygame.K_UP:
                   moved = moveUp()
                elif event.key == pygame.K_DOWN:
                   moved = moveDown()
            
            #controla los sucesos cuando se mueve el tablero
            if moved:
                generateNewNumber()
                if checkkWin():
                    gameWon = True
                elif checkLoss():
                    gameOver = True
            

    dibujaPantalla() #llama a la funcion
    pygame.display.flip() #actualiza la pantalla




           
    
