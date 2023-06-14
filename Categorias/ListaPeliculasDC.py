from .Pelicula import Pelicula

class ListaDobleCircular:

    def __init__(self):
        self.primero=None
        self.ultimo=None

    def InsertarPelicula(self,titulo,director,anio,fecha,hora):
        nueva_pelicula=Pelicula(titulo,director,anio,fecha,hora)

        if self.primero is None:
            nueva_pelicula.siguiente=nueva_pelicula
            nueva_pelicula.anterior=nueva_pelicula
            self.primero=nueva_pelicula
            self.ultimo=nueva_pelicula

        else:
            nueva_pelicula.anterior=self.ultimo
            self.ultimo.siguiente=nueva_pelicula
            nueva_pelicula.siguiente=self.primero
            self.primero.anterior=nueva_pelicula
            self.ultimo=nueva_pelicula
        
    def MostrarPeliculas(self):
        aux=self.primero

        while True:
            print("\tTítulo de la Pelicula: "+aux.ObtenerTitulo())
            print("\tPelicula dirigida por: "+aux.ObtenerDirector())
            print("\tEl año del estreno de la Película es: "+aux.ObtenerAnio())
            print("\tFecha de la Función: "+aux.ObtenerFecha())
            print("\tHora de la Función"+aux.ObtenerHora())
            aux=aux.siguiente
            if aux==self.primero:
                break
    
    def NuevaPelicula(self,titulo):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                return False
            aux=aux.siguiente
        return True
    
    def EliminarPelicula(self,titulo):
        if self.primero is None:
             print("la lista esta vacia")
        else:
            aux = self.primero
            while aux is not None:
                if aux.ObtenerTitulo() == titulo:
                    if aux == self.primero:
                        self.ultimo.siguiente=aux.siguiente
                        aux.siguiente.anterior=self.ultimo
                        self.primero=aux.siguiente
                        aux.anterior=None
                        aux.siguiente=None
                    elif aux == self.ultimo:
                        aux.anterior.siguiente=self.primero
                        self.primero.anterior=aux.anterior
                        self.ultimo=aux.anterior
                        aux.siguiente=None
                        aux.anterior=None
                    else:
                        aux.anterior.siguiente = aux.siguiente
                        aux.siguiente.anterior = aux.anterior
                        aux.siguiente=None
                        aux.anterior=None
                    return
                aux = aux.siguiente
                if aux==self.primero:
                    break
            print("Pelicula NO encontrada")

    def ModificarDirector(self,titulo,director):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.director=director
            aux=aux.siguiente
            if aux==self.primero:
                break

    def ModificarAnio(self,titulo,anio):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.anio=anio
            aux=aux.siguiente
            if aux==self.primero:
                break


    def ModificarFecha(self,titulo,fecha):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.fecha=fecha
            aux=aux.siguiente
            if aux==self.primero:
                break

    def ModificarHora(self,titulo,hora):
        aux=self.primero

        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                aux.hora=hora
            aux=aux.siguiente
            if aux==self.primero:
                break

    
    def MostrarDetallePelicula(self,titulo):
        aux=self.primero

        while True:
            if aux.ObtenerTitulo()==titulo:
                print("\tTítulo de la Pelicula: "+aux.ObtenerTitulo())
                print("\tPelicula dirigida por: "+aux.ObtenerDirector())
                print("\tEl año del estreno de la Película es: "+aux.ObtenerAnio())
                print("\tFecha de la Función: "+aux.ObtenerFecha())
                print("\tHora de la Función"+aux.ObtenerHora())
                break
            aux=aux.siguiente
            if aux==self.primero:
                break

    def MostrarCartelera(self):
        aux=self.primero

        while True:
            print("\t***"+aux.ObtenerTitulo())
            aux=aux.siguiente
            if aux==self.primero:
                break
    
    def DevolverPelicula(self,titulo):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                return aux
            aux=aux.siguiente
            if aux==self.primero:
                return None
        
    
    def ExistePeli(self,titulo):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerTitulo()==titulo:
                return True
            aux=aux.siguiente
            if aux==self.primero:
                return None

    def EscribirXML(self):
        aux=self.primero
        texto_peli="\t\t<peliculas>\n"
        while True:
            texto_peli=texto_peli+"\t\t\t<pelicula>\n"
            texto_peli=texto_peli+"\t\t\t\t<titulo>"+str(aux.ObtenerTitulo())+"</titulo>\n"
            texto_peli=texto_peli+"\t\t\t\t<director>"+str(aux.ObtenerDirector())+"</director>\n"
            texto_peli=texto_peli+"\t\t\t\t<anio>"+str(aux.ObtenerAnio())+"</anio>\n"
            texto_peli=texto_peli+"\t\t\t\t<fecha>"+str(aux.ObtenerFecha())+"</fecha>\n"
            texto_peli=texto_peli+"\t\t\t\t<hora>"+str(aux.ObtenerHora())+"</hora>\n"
            texto_peli=texto_peli+"\t\t\t</pelicula>\n"
            aux=aux.siguiente
            if aux==self.primero:
                texto_peli=texto_peli+"\t\t</peliculas>\n"
                return texto_peli



            

            




