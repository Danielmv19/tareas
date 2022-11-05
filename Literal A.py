"""
Crea un programa que lea una secuencia de caracteres, guarde cada carácter en una posición
de una lista y finalmente muestre la secuencia invertida.
"""
cadena = input("ingrese un texto: ")
lista = []
cadenainvertida = []
i = len(cadena)

while i > 0:
    cadenainvertida += cadena[i - 1]
    i -= 1

salida = "".join(cadenainvertida)

def mostrar_resultado():
    print("Frase invertida: {}".format(salida))
    print(type(salida))

def ingresardatos_lista():
    lista.append(salida)

ingresardatos_lista()
mostrar_resultado()