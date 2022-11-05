print('                                             \n')


print("░ ¤ Ejercicio C.-                                                                      ░")
print("░ ¤ Dado el siguiente arreglo [5,99,12,5,36,-96,54,1]                                  ░")
print("░ ¤ Ordenar de manera ascendente (de menor a mayor) utilizando el método de inserción. ░\n")

def insercion(arreglo): 
    for i in range(len(arreglo)):
        for j in range(i,0,-1):
            if(arreglo[j-1] > arreglo[j]):
                aux=arreglo[j];
                arreglo[j]=arreglo[j-1];
                arreglo[j-1]=aux; 
Arreglo_ordenar = [5,99,12,5,36,-96,54,1];
print("Arreglo antes  :",Arreglo_ordenar);
insercion(Arreglo_ordenar);
print("Arreglo despues:",Arreglo_ordenar);