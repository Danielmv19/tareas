# Literal E

#Crear un programa para ingresar solo letras en una pila, el ingreso se detendrá cuando se
#ingrese un número. Después de que finalice el ingreso deberá mostrar los elementos
#ingresados, además deberá presentar cuantas vocales y cuantas consonantes se ingresaron en la pila.



from Pila import Pila
def ContVocales(pila):
    vocal = {'a', 'e', 'i', 'o', 'u'}
    num_vocales = 0
    for el in pila:
        if el in vocal:
            num_vocales += 1
    return num_vocales


def ContConsonantes(pila):
    vocal = {'a', 'e', 'i', 'o', 'u'}
    num_consonant = 0
    for el in pila:
        if el not in vocal:
            num_consonant += 1
    return num_consonant


def IngrSoloLetras():
    pila = Pila()
    while True:
        entrada = input("ingrese una letra, si ingresa un numero o un caracter la ejecucion termina: ")
        if entrada.isalpha():
            pila.apilar(entrada)
        else:
            break
    print("las letras ingresadas son: ", pila.obtenerPila())
    print("El numero de vocales ingresados son: ", ContVocales(pila.obtenerPila()))
    print("El numero de consonantes ingresados son: ", ContConsonantes(pila.obtenerPila()))


def Main():
    while (True):
        menu = input("Dijite 1 para ejecutar el programa, caso contrario dijite 0 para Salir:\n>")
        if menu == "1":
            IngrSoloLetras()
        else:
            print("Finalizando la ejecucion del programa")
            break

Main()