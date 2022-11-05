# Crear una función que recibe una lista de números enteros y un número entero n de forma que modifique la lista de manera que cuando encuentre un
# elemento en la lista igual al número n sea reemplazado por un * en esa posición de la lista.


def Modi_lista(list, n_ente):
    encontrado = False
    for h in range(len(list)):
        if list[h] == n_ente:
            encontrado = True
            list[h] = " * "
    if encontrado:
         print("La lista fue actualizada : ", list)
    else:
       print("El numero que dijito no se encuentra registrado, debido a eso, la lista no se ha cambiado. ")

if __name__ == '__main__':
    opcion = "1"
    while (opcion != "0"):
        opcion = input(" Dijite 1 para ejecutar el programa.\n Dijite 0 para Salir del Programa:\n>")
        if opcion == "1":
            try:
               lista = []
               num_solicitado = None
               n = int(input("Ingrese el numero de elementos que quiere en la lista: "))
               if n <= 0:
                   print("Error: el numero de elementos que ingreso no valido.")
               else:
                   pos = 0
                   while pos < n:
                       try:
                          v = int(input(f"favor dijite el numero  nº {pos+1}: "))
                          lista.append(v)
                          pos += 1
                       except ValueError as j:
                            print(j)
                   try:
                     num_solicitado = int(input("Ingrese el numero que desea reemplazar por '*': "))
                   except ValueError as j:
                        print(j)
                   print("La lista ingresada es: ", lista)
                   
                   Modi_lista(lista, num_solicitado)
            except ValueError as j:
                 print(j)
        else:
           if opcion != "0":
               print("Favor seleccionar una de las opciones del menu")
    print("Finalizando la ejecucion del programa")