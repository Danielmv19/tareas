pila = []
new_chart = ''
char_ascii = ''

while new_chart != '*':
    new_chart = input('Ingresa un caracter o * para finalizar: ')
    if new_chart != '*':
        pila.append(new_chart)

print("Los caracteres ingresados son: {} ".format(pila))

for x in range(len(pila)):
    new_chart = pila.pop()
    char_ascii = "El codigo ASCII de '{}' es: {}".format(new_chart, ord(new_chart))
    print(char_ascii)