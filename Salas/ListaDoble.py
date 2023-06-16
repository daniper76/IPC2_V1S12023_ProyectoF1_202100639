from .Sala import Sala

class ListaDoble:

    def __init__(self):
        self.primero=None
        self.ultimo=None
    
    def InsertarSala(self,numero,asientos):
        nueva_sala=Sala(numero,asientos)
        if self.primero is None:
            self.primero = nueva_sala
            self.ultimo = nueva_sala
        else:
            nueva_sala.anterior = self.ultimo
            self.ultimo.siguiente = nueva_sala
            self.ultimo = nueva_sala
    
    def MostrarSalas(self):
        aux=self.primero
        print("********Salas de Cine:*********\n")
        while aux is not None:
            print("Número de Sala: "+aux.ObtenerNumero())
            print("\tNúmero de Asientos: "+str(aux.ObtenerAsientos())+"\n")
            aux=aux.siguiente

    def eliminar(self,numero):
        if self.primero is None:
             print("la lista esta vacia")
        else:
            aux = self.primero
            while aux is not None:
                if aux.ObtenerNumero() == numero:
                    if aux == self.primero:
                        self.primero = self.primero.siguiente
                        self.primero.anterior = None
                    elif aux == self.ultimo:
                        self.ultimo = self.ultimo.anterior
                        self.ultimo.siguiente = None
                    else:
                        aux.anterior.siguiente = aux.siguiente
                        aux.siguiente.anterior = aux.anterior
                    print("ELIMINADO")
                    return
                aux = aux.siguiente
            print("Sala No Encontrada")
    
    def ModificarNumero(self,numero,nuevo_numero):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNumero()==numero:
                aux.numero=nuevo_numero
            aux=aux.siguiente
    
    def ModificarAsientos(self,numero,asientos):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNumero()==numero:
                aux.asientos=asientos
            aux=aux.siguiente
    
    def MostrarDetalleSala(self,numero):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNumero()==numero:
                print("El número de Sala es: "+aux.ObtenerNumero())
                print("\tCantidad de Asientos:"+aux.ObtenerAsientos())
                break
            aux=aux.siguiente
    
    def ExisteSala(self,numero):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNumero()==numero:
                return True
            aux=aux.siguiente
        return False
    
    def escribirXML(self):
        if self.primero is None:
            print("La lista esta vacia")
        else:
            archivo = open("Salas.xml", "w")
            archivo.write("<cines>\n")
            archivo.write("\t<cine>\n")
            archivo.write("\t\t<salas>\n")

            aux = self.primero
            while aux is not None:
                archivo.write("\t\t\t<sala>\n")
                archivo.write("\t\t\t\t<numero>" + str(aux.ObtenerNumero()) + "</numero>\n")
                archivo.write("\t\t\t\t<asientos>" + str(aux.ObtenerAsientos()) + "</asientos>\n")
                archivo.write("\t\t\t</sala>\n")
                aux = aux.siguiente
            archivo.write("\t\t</salas>\n")
            archivo.write("\t</cine>\n")
            archivo.write("</cines>")
            archivo.close()      

    def MostrarNumeroSalas(self):
        aux=self.primero
        print("********Salas de Cine:*********\n")
        while aux is not None:
            print("\t*"+str(aux.ObtenerNumero()))
            aux=aux.siguiente



