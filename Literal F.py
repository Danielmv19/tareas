import statistics

numeros = []
nuevoNumero = ''

while nuevoNumero != 0:
    nuevoNumero = int(input('Ingrese un numero, o ingrese 0 para terminar: '))
    if nuevoNumero != 0:
        numeros.append(nuevoNumero)

mean = 0
def presentar_datos():
    print(mean)
    print(numeros)

def promedio():
    mean = statistics.mean(numeros)
promedio()
presentar_datos()