#Jose Daniel Mercqado Vernaza
letras = []
new_letra = ''
###Ingresar las letras a la variable "letras"
while True:
    new_letra = (input('Ingrese una letra, o ingrese un numero para terminar: '))
    if new_letra.isalpha():
        letras.append(new_letra)
        cadena = letras
        ###IMPORTANTE: Codigo reutilizado de "S3-TRABAJO PRÁCTICO EXPERIMENTAL_1, ejercicio e(resuelto por mi)"
        ###cuenta las vocales y consonantes y las compara
        def contadortotal():
            total = len(cadena)
            return total

        totalChar = contadortotal()

        def contarvocales():
            contador = 0
            for letra in cadena:
                if letra.lower() in "aeiou":
                    contador += 1
            return contador

        vocales = contarvocales()

        def cantidadconsonantes():
            cons = totalChar - vocales
            return cons

        consonantes = cantidadconsonantes()
        ###en el caso que se ingrese un numero se cerrara el bucle
    else:
        print("!!!!!!!!!!!!! Error, se ingresaron numeros !!!!!!!!!!!!!!")
        print(letras)
        if vocales and consonantes == 0:
            quit()
        ###cerrado el bucle comparamos las letras
        def mayoria():
            if vocales > consonantes:
                print("En el texto", cadena, "hay mas vocales que consonantes")
            elif vocales == consonantes:
                print("Hay la misma cantidad de vocales y consonantes")
            else:
                print("En el texto", cadena, "hay mas consonantes que vocales")

        ###invocamos la funcion mayoria()
        mayoria()
        quit()

