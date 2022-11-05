#literal D
# Crear un programa para ingresar números enteros a una pila, se ingresarán los números hasta
# que el valor que se ingrese sea cero, en ese momento debe presentar los elementos que se
#han ingresado a la pila y el promedio

from Pila import Pila

def Promed(lst):
    try:
        div = sum(lst.obtenerPila()) / lst.tamano()
        return div
    except ZeroDivisionError:
        return 0

def CalpromedioPilas():
    pila = Pila()
    cont = 1
    num = -1
    while num != 0:
        try:
            num = int(input("Dijite un numero entero, si el numero ingresado es cero el programa termina la ejecion n°" + str(cont) + ": "))
            if num == 0:
                break
            else:
                pila.apilar(num)
                cont += 1
        except ValueError as e:
            print(e)
    print("los numero ingresados son: ", pila.obtenerPila())
    print("El promedio de los numeros ingresados es: ", round(Promed(pila), 2))

def Main():
    while(True):
        opp = input("\nDijite 1 para ejecutar el programa, caso contrario dijite 0 para Salir:\n>")
        if opp == "1":
            CalpromedioPilas()
        else:
            print("*Cerrando programa*")
            break
Main()