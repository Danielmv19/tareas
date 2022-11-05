cadena = "abc"
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

print("vocales", vocales)
print("cpnsonantes", consonantes)
print("total", totalChar)


#contador_total()#
#print(f"En la cadena '{cadena}'' hay {cantidad} vocales")#
