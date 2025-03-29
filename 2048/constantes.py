from os import system  

#declaración de las dimensiones de la pantala
ScreenWidth = 400
ScreenHeight = 400

#declaración de las dimensiones de cada celda
CellSize = ScreenWidth/4

#colores del juego
blanco  = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)

#diccionario con loscolores de los numeros
colors = {
    0: (204,192,179),
    2: (238,228,218),
    4: (237,224,179),
    8: (242,177,121),
    16: (245,149,99),
    32: (246,124,95),
    64: (246,94,59),
    128: (237,207,114),
    256: (237,204,97),
    512: (237,200,80),
    1024: (237,197,63),
    2048: (237,194,46),
}