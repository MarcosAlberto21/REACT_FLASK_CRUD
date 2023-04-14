import os


class Nodo:
    def __init__(self, salon, horario, descripcion):
        self.salon = salon
        self.horario = horario
        self.descripcion = descripcion
        self.abajo = None
        self.arriba = None
        self.derecha = None
        self.izquierda = None


class NodoCabecera:
    def __init__(self, salon):
        self.salon = salon
        self.derecha = None
        self.izquierda = None
        self.abajo = None


class NodoLateral:
    def __init__(self, horario):
        self.horario = horario
        self.abajo = None
        self.arriba = None
        self.derecha = None


class Matriz:
    def __init__(self):
        self.cabecera = None
        self.cola_cabecera = None
        self.cabecera_tamanio = 0
        self.lateral = None
        self.cola_lateral = None
        self.lateral_tamanio = 0

    def insertar(self, salon, horario, descripcion):
        nuevo_nodo = Nodo(salon, horario, descripcion)
        # crea nodos cabecera si no existen
        if self.cabecera is None:
            self.cabecera = NodoCabecera(salon)
            self.cabecera_tamanio += 1
        else:
            nodo_nuevo_cabezera = NodoCabecera(salon)

            nodo_actual = self.cabecera
            while nodo_actual is not None:
                # reordena los nodos de menor a mayor
                # primero verifica si el nodo actual es mayor que el nuevo nodo y vuelvelo la cabeza
                if nodo_actual.salon > salon:
                    self.cabecera = nodo_nuevo_cabezera
                    nodo_nuevo_cabezera.derecha = nodo_actual
                    nodo_actual.izquierda = nodo_nuevo_cabezera
                    break
                # si el nodo actual es menor que el nuevo nodo y no tiene nada a la derecha, lo agrega
                elif nodo_actual.derecha is None:
                    nodo_actual.derecha = nodo_nuevo_cabezera
                    nodo_nuevo_cabezera.izquierda = nodo_actual
                    break
                # si el nodo actual es menor que el nuevo nodo y el nodo a la derecha es mayor que el nuevo nodo, lo agrega
                elif nodo_actual.derecha.salon > salon:
                    nodo_nuevo_cabezera.derecha = nodo_actual.derecha
                    nodo_actual.derecha.izquierda = nodo_nuevo_cabezera
                    nodo_actual.derecha = nodo_nuevo_cabezera
                    nodo_nuevo_cabezera.izquierda = nodo_actual
                    break
            
                nodo_actual = nodo_actual.derecha
        # crea nodos laterales si no existen
        if self.lateral is None:
            self.lateral = NodoLateral(horario)
            self.lateral_tamanio += 1
        else:
            nodo_nuevo_lateral = NodoLateral(horario)
            # vuelve a recorrer la lista para ordenar los nodos de menor a mayor
            nodo_actual = self.lateral
            while nodo_actual is not None:
                # reordena los nodos de menor a mayor
                # primero verifica si el nodo actual es mayor que el nuevo nodo y vuelvelo la cabeza
                if nodo_actual.horario > horario:
                    nodo_nuevo_lateral.abajo = nodo_actual
                    nodo_actual.arriba = nodo_nuevo_lateral
                    self.lateral = nodo_nuevo_lateral
                    break
                # si el nodo actual es menor que el nuevo nodo y no tiene nada a la derecha, lo agrega
                elif nodo_actual.abajo is None:
                    nodo_actual.abajo = nodo_nuevo_lateral
                    nodo_nuevo_lateral.arriba = nodo_actual
                    break
                # si el nodo actual es menor que el nuevo nodo y el nodo a la derecha es mayor que el nuevo nodo, lo agrega
                elif nodo_actual.abajo.horario > horario:
                    nodo_nuevo_lateral.abajo = nodo_actual.abajo
                    nodo_actual.abajo.arriba = nodo_nuevo_lateral
                    nodo_actual.abajo = nodo_nuevo_lateral
                    nodo_nuevo_lateral.arriba = nodo_actual
                    break

                nodo_actual = nodo_actual.abajo

        lateral = self.obtener_nodo_lateral(horario)
        cabecera = self.obtener_nodo_cabecera(salon)

        print(lateral.horario, lateral)
        print(cabecera.salon, cabecera)
        
        if lateral is not None and cabecera is not None:
            self.insertar_nodo_matriz(nuevo_nodo, cabecera, lateral)
        else:
            print("No se pudo insertar el nodo, verifique los datos ingresados")

    def insertar_nodo_matriz(self, nodo_nuevo, nodo_cabecera, nodo_lateral):
        print("creando nodo matriz")
        print("nodo cabecera: ", nodo_cabecera.salon, nodo_cabecera.abajo)
        print("nodo lateral: ", nodo_lateral.horario, nodo_lateral.derecha)

        if nodo_cabecera.abajo is None:
            print("no hay nada en la cabecera hacia abajo")
            nodo_cabecera.abajo = nodo_nuevo
            # nodo_nuevo.arriba = nodo_cabecera
        else:
            print("ya existe algo en la cabecera hacia abajo")
            nodo_actual = nodo_cabecera.abajo
            print(nodo_actual.horario)
            while nodo_actual.abajo is not None:
                # primero verifica si el nodo nuevo es menor para insertarlo al inicio
                if nodo_actual.horario > nodo_nuevo.horario:
                    nodo_nuevo.abajo = nodo_actual
                    nodo_actual.arriba = nodo_nuevo
                    nodo_cabecera.abajo = nodo_nuevo
                    break
                # si el nodo nuevo es mayor y tine algo abajo, lo agregamos en medio
                elif nodo_actual.horario < nodo_nuevo.horario and nodo_actual.abajo.horario > nodo_nuevo.horario:
                    nodo_nuevo.abajo = nodo_actual.abajo
                    nodo_actual.abajo.arriba = nodo_nuevo
                    nodo_actual.abajo = nodo_nuevo
                    nodo_nuevo.arriba = nodo_actual
                    break
                # si el nodo nuevo es mayor que el nodo actual y no tiene nada abajo, lo agrega
                elif nodo_actual.abajo.horario > nodo_nuevo.horario:
                    nodo_nuevo.abajo = nodo_actual.abajo
                    nodo_actual.abajo.arriba = nodo_nuevo
                    nodo_actual.abajo = nodo_nuevo
                    nodo_nuevo.arriba = nodo_actual
                    break

                                
                nodo_actual = nodo_actual.abajo


        if nodo_lateral.derecha is None:
            nodo_lateral.derecha = nodo_nuevo
            # nodo_nuevo.izquierda = nodo_lateral
        else:
            nodo_actual = nodo_lateral.derecha
            while nodo_actual.derecha is not None:
                # primero verifica si el nodo nuevo es menor para insertarlo al inicio
                if nodo_actual.salon > nodo_nuevo.salon:
                    nodo_nuevo.derecha = nodo_actual
                    nodo_actual.izquierda = nodo_nuevo
                    nodo_lateral.derecha = nodo_nuevo
                    break
                # si el nodo nuevo es mayor y tine algo abajo, lo agregamos en medio
                elif nodo_actual.salon < nodo_nuevo.salon and nodo_actual.derecha.salon > nodo_nuevo.salon:
                    nodo_nuevo.derecha = nodo_actual.derecha
                    nodo_actual.derecha.izquierda = nodo_nuevo
                    nodo_actual.derecha = nodo_nuevo
                    nodo_nuevo.izquierda = nodo_actual
                    break
                # si el nodo nuevo es mayor que el nodo actual y no tiene nada abajo, lo agrega
                elif nodo_actual.derecha.salon > nodo_nuevo.salon:
                    nodo_nuevo.derecha = nodo_actual.derecha
                    nodo_actual.derecha.izquierda = nodo_nuevo
                    nodo_actual.derecha = nodo_nuevo
                    nodo_nuevo.izquierda = nodo_actual
                    break

                nodo_actual = nodo_actual.derecha


    def obtener_nodo_lateral(self, horario):
        nodo_actual = self.lateral
        while nodo_actual is not None:
            if nodo_actual.horario == horario:
                break
            nodo_actual = nodo_actual.abajo
        return nodo_actual

    def obtener_nodo_cabecera(self, salon):
        nodo_actual = self.cabecera
        while nodo_actual is not None:
            if nodo_actual.salon == salon:
                break
            nodo_actual = nodo_actual.derecha
        return nodo_actual

    # grafica la matriz y la guarda en un archivo .dot

    def graficar(self):
        archivo = open("matriz.dot", "w")
        archivo.write("digraph G {\n")
        archivo.write("node[shape=box];\n")
        archivo.write(
            "Mt[ label = \"Matrix\", width = 1.5, style = filled, fillcolor = firebrick1, group = 1 ];\n")
        archivo.write(self.crea_nodos_laterales() + "\n")
        archivo.write(self.crea_nodos_cabecera() + "\n")
        archivo.write(self.crea_nodos_matriz_por_lateral() + "\n")
        archivo.write(self.crea_enlaces_matriz_por_lateral() + "\n")
        archivo.write(self.crea_enlaces_matriz_por_cabecera() + "\n")

        archivo.write("}\n")
        archivo.close()
        # ahora creamos el archivo .png
        os.system("dot -Tpng matriz.dot -o matriz.png")

    def crea_nodos_laterales(self):
        nodo_actual = self.lateral
        dot = ""
        while nodo_actual is not None:
            #  U0 [label = "Estructuras"    pos = "5.3,3.5!" width = 1.5 style = filled, fillcolor = bisque1, group = 1 ];
            dot += "L" + str(nodo_actual.horario) + " [label = \"" + str(
                nodo_actual.horario) + "\"    pos = \"5.3,3.5!\" width = 1.5 style = filled, fillcolor = bisque1, group = 1 ];\n"
            nodo_actual = nodo_actual.abajo

        # relaciona los nodos laterales
        nodo_actual = self.lateral
        dot += "Mt -> L" + str(nodo_actual.horario) + ";\n"
        while nodo_actual is not None:
            if nodo_actual.abajo is not None and nodo_actual.abajo.horario != nodo_actual.horario:
                dot += "L" + str(nodo_actual.horario) + \
                                     " -> L" + \
                                         str(nodo_actual.abajo.horario) + ";\n"
            # if nodo_actual.arriba is not None and nodo_actual.arriba.horario != nodo_actual.horario:
            #     dot += "L" + str(nodo_actual.horario) + \
            #                          " -> L" + \
            #                              str(nodo_actual.arriba.horario) + ";\n"
            nodo_actual = nodo_actual.abajo

        return dot

    def crea_nodos_cabecera(self):
        nodo_actual = self.cabecera
        dot = ""

        while nodo_actual is not None:
            #  U0 [label = "Estructuras"    pos = "5.3,3.5!" width = 1.5 style = filled, fillcolor = bisque1, group = 1 ];
            dot += "H" + str(nodo_actual.salon) + " [label = \"" + str(nodo_actual.salon) + \
                             "\"    pos = \"5.3,3.5!\" width = 1.5 style = filled, fillcolor = lightskyblue, group = " + \
                                 str(int(nodo_actual.salon)+1)+" ];\n"

            nodo_actual = nodo_actual.derecha

        # relaciona los nodos cabecera
        nodo_actual = self.cabecera
        dot += "Mt -> H" + str(nodo_actual.salon) + ";\n"

        while nodo_actual is not None:
            if nodo_actual.derecha is not None and nodo_actual.derecha.salon != nodo_actual.salon:
                dot += "H" + str(nodo_actual.salon) + \
                                      " -> H" + \
                                          str(nodo_actual.derecha.salon) + ";\n"
            # if nodo_actual.izquierda is not None and nodo_actual.izquierda.salon != nodo_actual.salon:
            #     dot += "H" + str(nodo_actual.salon) + \
            #                           " -> H" + \
            #                               str(nodo_actual.izquierda.salon) + ";\n"

            nodo_actual = nodo_actual.derecha

        # { rank = same; Mt; A0; A1; A2; A3; A4; }/
        # posiciona los nodos cabecera en el mismo nivel
        nodo_actual = self.cabecera
        dot += "{ rank = same; Mt; "
        while nodo_actual is not None:
            dot += "H" + str(nodo_actual.salon) + "; "
            nodo_actual = nodo_actual.derecha
        dot += "};\n"

        return dot

    def crea_nodos_matriz_por_lateral(self):
        # se pueden crear por la cabecera tambien
        # recorre los laterales de izquierda a derecha
        nodo_actual = self.lateral
        dot = ""
        while nodo_actual is not None:
            nodo_aux = nodo_actual.derecha
            while nodo_aux is not None:
                dot += "NODO" + str(nodo_aux.salon)+str(nodo_aux.horario)+"[label = \""+"salon:"+str(nodo_aux.salon)+"\n"+"Horario:"+str(
                    nodo_aux.horario)+"\n" + nodo_aux.descripcion+"\" width = 1.5, group = " + str(int(nodo_aux.salon)+1)+" ];\n "
                nodo_aux = nodo_aux.derecha

            nodo_actual = nodo_actual.abajo

        return dot

    def crea_enlaces_matriz_por_lateral(self):
        nodo_actual = self.lateral
        dot = ""
        while nodo_actual is not None:
            dot += "L" + str(nodo_actual.horario) + " -> NODO" + str(nodo_actual.derecha.salon) + str(nodo_actual.horario) + ";\n"
            nodo_aux = nodo_actual.derecha
            while nodo_aux.derecha is not None:
                if nodo_aux.derecha is not None:
                    dot += "NODO" +str(nodo_aux.salon)+str(nodo_aux.horario)+ "->"+ "NODO" + str(nodo_aux.derecha.salon) + str(nodo_aux.derecha.horario) + ";\n"
                
                # if nodo_aux.izquierda is not None and nodo_aux.izquierda.salon != nodo_aux.salon:
                #     dot += "NODO" +str(nodo_aux.salon)+str(nodo_aux.horario)+ "->"+ "NODO" + str(nodo_aux.izquierda.salon) + str(nodo_aux.izquierda.horario) + ";\n"
                
                nodo_aux = nodo_aux.derecha

            nodo_actual = nodo_actual.abajo
        
        
        # posiciona los nodos de la matriz en el mismo nivel
        nodo_actual = self.lateral
        while nodo_actual is not None:
            dot += "\n{ rank = same; "
            dot += "L" + str(nodo_actual.horario) + "; "
            nodo_aux = nodo_actual.derecha
            while nodo_aux is not None:
                dot += "NODO" +str(nodo_aux.salon)+str(nodo_aux.horario)+"; "
                nodo_aux = nodo_aux.derecha
            nodo_actual = nodo_actual.abajo
            dot += "};\n"

        return dot
    
    def crea_enlaces_matriz_por_cabecera(self):
        nodo_actual = self.cabecera
        dot = ""
        while nodo_actual is not None:
            dot += "H" + str(nodo_actual.salon) + " -> NODO" + str(nodo_actual.salon) + str(nodo_actual.abajo.horario) + ";\n"
            nodo_aux = nodo_actual.abajo
            while nodo_aux.abajo is not None:
                if nodo_aux.abajo is not None:
                    dot += "NODO" +str(nodo_aux.salon)+str(nodo_aux.horario)+ "->"+ "NODO" + str(nodo_aux.abajo.salon) + str(nodo_aux.abajo.horario) + ";\n"
                
                # if nodo_aux.arriba is not None and nodo_aux.arriba.horario != nodo_aux.horario:
                #     dot += "NODO" +str(nodo_aux.salon)+str(nodo_aux.horario)+ "->"+ "NODO" + str(nodo_aux.arriba.salon) + str(nodo_aux.arriba.horario) + ";\n"
                
                nodo_aux = nodo_aux.abajo

            nodo_actual = nodo_actual.derecha
        
        return dot