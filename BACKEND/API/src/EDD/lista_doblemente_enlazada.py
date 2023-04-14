class Nodo:
    def __init__(self, id, nombre, email):
        self.id = id
        self.name = nombre
        self.email = email
        self.nodo_anterior = None
        self.nodo_siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def agregar(self, id, nombre, email):
        nuevo_nodo = Nodo(id, nombre, email)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.nodo_anterior = self.cola
            self.cola.nodo_siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamaño += 1

    def eliminar(self, id):
        nodo_actual = self.cabeza
        while nodo_actual is not None and nodo_actual.id != id:
            nodo_actual = nodo_actual.nodo_siguiente
        if nodo_actual is not None:
            if nodo_actual == self.cabeza:
                self.cabeza = self.cabeza.nodo_siguiente
                if self.cabeza is not None:
                    self.cabeza.nodo_anterior = None
            elif nodo_actual == self.cola:
                self.cola = self.cola.nodo_anterior
                if self.cola is not None:
                    self.cola.nodo_siguiente = None
            else:
                nodo_actual.nodo_anterior.nodo_siguiente = nodo_actual.nodo_siguiente
                nodo_actual.nodo_siguiente.nodo_anterior = nodo_actual.nodo_anterior
            self.tamaño -= 1

    def actualizar(self, id, nombre, email):
        nodo_actual = self.cabeza
        while nodo_actual is not None and nodo_actual.id != id:
            nodo_actual = nodo_actual.nodo_siguiente
        if nodo_actual is not None:
            nodo_actual.name = nombre
            nodo_actual.email = email

    def buscar(self, id):
        nodo_actual = self.cabeza
        while nodo_actual is not None and nodo_actual.id != id:
            nodo_actual = nodo_actual.nodo_siguiente
        if nodo_actual is not None:
            return {nodo_actual.id: {"nombre": nodo_actual.name, "email": nodo_actual.email}}
        else:
            return None

    def imprimir_lista(self):
        nodo_actual = self.cabeza
        data= []
        while nodo_actual is not None:
            data.append({"id": nodo_actual.id, "nombre": nodo_actual.name, "email": nodo_actual.email})
            nodo_actual = nodo_actual.nodo_siguiente
        return data


    def imprimir(self):
        with open("lista.dot", "w") as archivo_dot:
            archivo_dot.write("digraph G {\n")
            archivo_dot.write("rankdir=LR;\n") # agregar esta línea para imprimir hacia la derecha
            archivo_dot.write("node [shape=rect];\n") # agregar esta línea para usar la forma de rectángulo para cada nodo
            nodo_actual = self.cabeza
            while nodo_actual is not None:
                archivo_dot.write(f"  {nodo_actual.id} [label=\"{nodo_actual.name}\\n{nodo_actual.email}\"]\n")
                if nodo_actual.nodo_siguiente is not None:
                    archivo_dot.write(f"  {nodo_actual.id} -> {nodo_actual.nodo_siguiente.id}\n")
                if nodo_actual.nodo_anterior is not None:
                    archivo_dot.write(f"  {nodo_actual.id} -> {nodo_actual.nodo_anterior.id}\n")
                nodo_actual = nodo_actual.nodo_siguiente
            archivo_dot.write("}")
              
	