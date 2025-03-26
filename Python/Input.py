#metodo para controlar los inputs

def pideInt(mensaje):
    correcto = False
    while not correcto:
        try:
            numero = int(input(mensaje))
            print(numero)
            correcto = True
        except:
            correcto = False
    return numero