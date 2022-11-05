#  Crea un programa que lea dos strings de la misma longitud, los guarde intercalados en una lista.
#  Por último, mostrar el contenido de la lista. Por ejemplo, si introducimos hola caracola y adios marieta, debería mostrarse haodleao scamraarcioeltaa.


def CadIntercaladas():
    salida = False
    while not salida:
        strings1 = input("Ingrese el primer strings:")
        strings2 = input("Ingrese el segundo strings:")
        lista_resultado = []
        if len(strings1) == len(strings2):
            for i in range(len(strings1)):
                lista_resultado.append(strings1[i])
                lista_resultado.append(strings2[i])
            salida = True
        else:
            print("los strings debe ser de la misma longitud")
            salida = False
    print("El Resultado de los string ingresados es:","".join(lista_resultado))

def Main():
    while(True):
        Menu = input("\nDijite 1 para ejecutar el programa, caso contrario dijite 0 para Salir:\n>")
        if Menu == "1":
            CadIntercaladas()
        else:
            print("*Finalizando la ejecucion del programa*")
            break
Main()