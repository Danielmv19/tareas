cadena = "Mi perro se encuentra contemplando el cielo"
cadena = cadena.strip(" ")
def contador_total():
    total = len(cadena)
    return total

totalChar = contador_total()

def contar_vocales():
    contador = 0
    for letra in cadena:
        if letra.lower() in "aeiou":
            contador += 1
    return contador
    
vocales = contar_vocales()

def cantidad_consonantes():
    cons = totalChar - vocales
    return cons

consonantes = cantidad_consonantes()

def mayoria():
    if vocales > consonantes:
        print("En el texto", cadena, "hay mas vocales que consonantes")
    else:
        print("En el texto", cadena, "hay mas consonantes que vocales")

#print("vocales", vocales)
#print("cpnsonantes", consonantes)
#print("total", totalChar)

mayoria()




