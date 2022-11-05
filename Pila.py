class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)

    def obtenerPila(self):
        return self.items
