import Input
from Printer import *

#Posibles variables para el funcionamiento del juego.
nombre = ""  
dinero = 0
decisiones = []
stats = []

nombre = input("Dime tu nombre, y no me mientas.")
input("NARRADOR: Vale hijo puta, esto es un test. NO va a ser divertido, NO va a tener puto sentido, y lo mas probable es que NO tenga "
    "final.\n"
    "NARRADOR: Lo que sí tendrá son bugs.\n"
    "NARRADOR: Algunas veces te hablaré y querré que me respondas, otras veces con que le des al ENTER me vale.\n"
    "NARRADOR: Si ves que paro de hablar y has terminado de leerme, dale al ENTER para continuar.\n"
    "(Ahora hay que darle al ENTER)")

#esta parte del codigo controla el input que hace el jugador.
#cuando pone print, el prorama no espera nada, si pone input, espera una respuesta del jugador.
print("NARRADOR: Fantástico. Otras veces querré una respuesta concreta. Por ejemplo:")
input_correcto = False
while not input_correcto:
    user_input = input("Introduce 'SI JODER' para continuar\n")
    input_correcto = (user_input == "SI JODER")

'''
print("NARRADOR: ESE ES EL PUTO ESPIRITU.")
print("NARRADOR: Vale, te comento. Está la cosa muy mal, que mal está todo, está todo fatal.")
print("NARRADOR: Nuestra historia se sitúa en un futuro distópico, en el año...")
input()
'''

input("NARRADOR: ESE ES EL PUTO ESPIRITU.\n"
                "NARRADOR: Vale, te comento. Está la cosa muy mal, que mal está todo, está todo fatal.\n"
                "NARRADOR: Nuestra historia se sitúa en un futuro distópico, en el año...\n")


input("NARRADOR: ah joder. Espera que miro...")
input("NARRADOR: ...no hombre, esto tiene que estar mal... dame un minuto que lo compruebe...")
input("NARRADOR: pues no está mal, no. La historia es en el 2025. Puta mierda...")
input("NARRADOR: siempre te imaginas estas cosas más lejos, ¿sabes? pensaba que este marrón se lo iban a comer mis nietos, no yo...")
input("NARRADOR: ...")

input("*se enciende un cigarro, abre la ventana y empieza a fumar apoyado en el alfeizar, dándote la espalda*")
input("NARRADOR: ...aunque claro, tampoco es que vaya a tener nietos...")
input("NARRADOR: ...porque para tener nietos primero hay que tener hijos...")
input("NARRADOR: ...y para tener hijos lo suyo es tener una relación sana...")
input("NARRADOR: ...y para eso lo suyo sería tener una mente sana...")
input("NARRADOR: ...y una buena forma de llegar a eso es vivir en un ambiente que te invite a crecer y expresarte...")
input("VECINO ESTRESADO: ¡¡POR DIOS CIERRA LA PUTA BOCA CON TUS DEPRESIONES MENTALES, QUE ME QUEDAN DOS HORAS DE SUEÑO!!")
input("*A lo que abre la boca para contestar, un viento poluto entra por la ventana, empujando el humo del cigarro de vuelta a la habitación,\n"
    "junto con varios nuevos y emocionantes humos provenientes del exterior*\n"
    "*Al menos el humo tiene facilidad para hacer amigos*")
input("NARRADOR: *tose*")
input("NARRADOR: *continua tosiendo*")

print("*Tira la colilla por la ventana y la cierra*")
print("*Una aplicación en su reloj inteligente le avisa de que ha sido multado por TIRAR BASURA, y pide que valore la sanción de 1 a 5 estrellas.*")

valoracion = -1 #damos un valor a la variable para que pueda entrar en el while
while valoracion not in [1,2,3,4,5]: #pide por teclado un numero que sea diferente 
    valoracion = Input.pideInt("*¿Qué valoración le pone el NARRADOR a su multa? (Introduce un número del 1 al 5)")

print("*El olor a humedad y moho de las paredes se inserta en tu cerebro*")
print("NARRADOR: DESPIERTA. Tienes un deber para con la sociedad.")
print("NARRADOR: Esta gran nación espera mucho de ti,")
print("NARRADOR: eso dicen las noticias de media noche y los programas \n"
"del corazón, sin olvidar las revistas de suplementos alimenticios.")
print("*PUM, PUM PUM")
print("*La negra fina puerta vibra fuerte tras ser golpeada desde el exterior*")
print("NARRADOR: ¿Qué cojones pasa ahora?")
input(print("1. Abrir la puerta"))
print("NARRADOR: OPCION 2: permanecer en silencio.")