import statistics

numeros = []
nuevoNumero = ''

while nuevoNumero != '0':
    nuevoNumero = input("Ingresa un numero o presiona 0 para salir: ")
    if nuevoNumero != 0:
        numeros.append(nuevoNumero)
def a():
    for i in range (len(numeros)):
        numeros[i] = int(numeros[i])
a()

mean = 0
numeros.pop()
list =  numeros
mean = statistics.mean(list)

def c():
    print("Los numero agregados son: {}".format(numeros))
    print("El promedio de {} es: {}".format(numeros, mean))
c()