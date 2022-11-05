# Crea una matriz de n × m y asigna los valores manualmente. El programa
# debe indicar si la suma de cada columna es el mismo valor.


def matriz_nxm (matriz):
    num_fila = len(matriz)
    todos_iguales = True
    for t in range(num_fila):
            if matriz[0] != matriz[t]:
                todos_iguales = False
    if todos_iguales:
        print("La suma de los valores de las columnas SI son iguales.")
    else:
        print("La suma de los valores de las columnas NO son iguales.")

def construir_matriz():
    try:
       numf = int(input("Porfavor ingrese el numero de filas de la matriz: "))
       numc = int(input("Porfavor ingrese el numero de columnas de la matriz: "))
       while numf <= 0 or numc <= 0:
           print("Ingrese solo numeros mayores a cero.")
           numf = int(input("Ingrese el numero de filas de matriz: "))
           numc = int(input("Ingrese el numero de columnas de matriz: "))
       matriz = [[0 for i in range(numc)] for j in range(numf)]
       print("Matriz inicial: ", matriz)
       matriz_cadena = ""
       sum_columnas = []
       num_fila = len(matriz)
       num_colum = len(matriz[0])
       for g in range(num_fila):
           for d in range(num_colum):
               valor = int(input(f"Ingrese un valor en la fila: {g+1}, columna:{d+1}>"))
       matriz[g][d] = valor
       matriz_cadena += str(matriz) + "\n"
       matriz_cadena = "Matriz = \n" + matriz_cadena.replace("],", "]\n")
       for d in range(num_colum):
           suma_col = 0
           for g in range(num_fila):
               suma_col += matriz[g][d]
           sum_columnas.append(suma_col)
       print(matriz_cadena)
       print("Suma Columnas: ", sum_columnas)
       matriz_nxm (sum_columnas)
    except ValueError as i:
       print("Error: ", i)

if __name__ == '__main__':
    opcion = "1"
    while(opcion != "0"):
        opcion = input(" Dijite 1 para ejecutar el programa.\n Dijite 0 para Salir del Programa:\n>")
        if opcion == "1":
            construir_matriz()
        else:
           if opcion != "0":
               print("favor seleccionar una de las opciones del menu ")
    print("Finalizando la ejecucion del programa")