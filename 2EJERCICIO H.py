"""
Representar el siguiente árbol mediante código en Python. Mostrar por pantalla sus elementos.
"""
class nodopr:
    def __init__(self,nombre,valor,padre):
        self.valor = valor
        self.nombre = nombre
        self.padre =  padre
        self.izq = None
        self.der = None

class Arbol:
    def __init__(self):
        self.raiz_p = None

    def arborden(self,nodo):
        if nodo != None:
            self.arborden(nodo.izq)
            print(nodo.nombre, end = ", ")
            self.arborden(nodo.der)

    def mostrar(self,nodo,cont):
        if nodo == None:
            return
        else:
            self.mostrar(nodo.der,cont+1)
            for i in range(cont):
                print("      ",end = "")
            print(nodo.nombre)
            self.mostrar(nodo.izq,cont+1);

    def insertar(self,nodo,car,n):
        if(nodo == None):
            self.raiz_p = nodopr(car,n,None)
            return
        if nodo.valor < n : 
            if(nodo.der == None):
                nodo.der = nodopr(car,n,nodo)
            else:
                self.insertar(nodo.der,car,n)
        else: 
            if nodo.izq == None :
                nodo.izq = nodopr(car,n,nodo)
            else:
                self.insertar(nodo.izq,car,n)

arbol = Arbol()
arbol.insertar(None,"Pablo",8)
arbol.insertar(arbol.raiz_p,"Pedro",4)
arbol.insertar(arbol.raiz_p,"Ramon",11)
arbol.insertar(arbol.raiz_p,"Carlos",2)
arbol.insertar(arbol.raiz_p,"Pepe",6)
arbol.insertar(arbol.raiz_p,"Anibal",9)
arbol.insertar(arbol.raiz_p,"Sandra",13)
arbol.insertar(arbol.raiz_p,"Lady",1)
arbol.insertar(arbol.raiz_p,"Luis",3)
arbol.insertar(arbol.raiz_p,"Pamela",5)
arbol.insertar(arbol.raiz_p,"Clara",7)
arbol.insertar(arbol.raiz_p,"Ines",10)
arbol.insertar(arbol.raiz_p,"Juan",12)

def mostrar_pantalla():
    print("\nMostrando el Arbol Completo :\n")
    arbol.mostrar(arbol.raiz_p,0)

mostrar_pantalla()