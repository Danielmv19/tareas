#Crea un programa que lea un entero, n, de teclado y construya una matriz de
#tamaño n × n. Cada posición debe contener su orden en la matriz (desde 0 hasta n 2 − 1. Por ejemplo, si n es 3, deberá crearse la matriz


def matriz():
    try:
       numero= int(input("ingrese un numero entero positivo :\n> "))
       while numero <= 0:
           print("favor ingresar un numero mayor a cero.")
           numero = int(input("ingrese un numero entero positivo::\n> "))
       valor_ini= 0
       matriz_cad = ""
       for g in range(numero):
           fl = []
           for h in range(numero):
               fl.append(valor_ini)
               valor_ini += 1
               matriz_cad += str(fl) + "\n"
       print(matriz_cad)
    except ValueError as i:
        print("Error: ", i)

if __name__ == '__main__':
    opcion = "1"
    while(opcion != "0"):
        opcion = input(" Dijite 1 para ejecutar el programa.\n Dijite 0 para Salir del Programa:\n>")
        if opcion == "1":
            matriz()
        else:
           if opcion != "0":
               print("favor seleccionar una de las opciones del menu ")
    print("Finalizando la ejecucion del programa")