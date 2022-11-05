"""
Crea un programa que lea un string y guarde en una lista todas las consonantes
"""
lista = []
texto = (input("Ingrese una frase: ").lower())
vocales = ("a" ,"e" ,"i" ,"o" ,"u")


for letra in vocales:
    texto = texto.replace(letra, "")

def a():
    lista.extend(texto)
a()
def mostrar_resultados():
    lista.remove(" ")
    print("las consonantes de la frase son: {}".format(lista))
    print(type(lista))

mostrar_resultados()
