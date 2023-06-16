from .Categoria import Categoria

class ListaCategorias:

    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def InsertarCategoria(self,nombre):
        nueva_categoria=Categoria(nombre)
        
        if self.primero == None:
            self.primero = nueva_categoria
            self.ultimo = nueva_categoria
        else: 
            self.ultimo.siguiente = nueva_categoria
            self.ultimo = nueva_categoria
    
    def MostrarCategoriasPeliculas(self):
        aux=self.primero
        while aux is not None:
            print('-----Detalle de la Categoría-------')
            print('Nombre: '+aux.ObtenerNombre())
            aux.ObtenerListaPeliculas().MostrarPeliculas()
            aux=aux.siguiente
        
    def MostrarCategorias(self):
        aux=self.primero
        print("-----------Categorías------------\n")
        while aux is not None:
            print("\t*"+str(aux.ObtenerNombre()))
            aux=aux.siguiente
            
    
    def EliminarCategoria(self,nombre):

        self.ExistenciaCategoria()
        aux=self.primero
        anterior=None
        while aux is not None:
            if (aux.ObtenerNombre()==nombre):
                if aux==self.primero:
                    self.primero=aux.siguiente
                    aux.siguiente=None
                else:
                    anterior.siguiente=aux.siguiente
                    aux.siguiente=None
                    if(aux==self.ultimo):
                        self.ultimo=anterior
            
            anterior=aux
            aux=aux.siguiente
    
    def ModificarNombre(self,nombre):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNombre()==nombre:
                aux.nombre=nombre
            aux=aux.siguiente


    def NuevaCategoria(self,nombre):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNombre()==nombre:
                return False
            aux=aux.siguiente
        return True
    

    
    def ExistenciaCategoria(self,nombre):
        aux=self.primero
        while aux is not None:
            if(aux.ObtenerNombre()==nombre):
                return "Se eliminó la categoría: "+str(nombre)
            aux=aux.siguiente
        return "La categoría no existe"
    
    def BuscarListaPeliculas(self,id):
        aux=self.primero
        while aux is not None:
            if(aux.ObtenerId()==int(id)):
                return aux.ObtenerListaPeliculas()
            aux=aux.siguiente
    
    def BuscarCategorias(self,categoria):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNombre()==categoria:
                return True
            aux=aux.siguiente
        return False
    
    def ObtenerListaPeliculas(self,categoria):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNombre()==categoria:
                return aux.ObtenerListaPeliculas()
            aux=aux.siguiente
    
    def EliminarPelicula(self,titulo):
        aux=self.primero
        while aux is not None:
            aux.ObtenerListaPeliculas().EliminarPelicula(titulo)
            aux=aux.siguiente

    def ModificarDirector(self,titulo,director):
        aux=self.primero
        while aux is not None:
            aux.ObtenerListaPeliculas().ModificarDirector(titulo,director)
            aux=aux.siguiente

    def ModificarAnio(self,titulo,anio):
        aux=self.primero
        while aux is not None:
            aux.ObtenerListaPeliculas().ModificarAnio(titulo,anio)
            aux=aux.siguiente

    def ModificarFecha(self,titulo,fecha):
        aux=self.primero
        while aux is not None:
            aux.ObtenerListaPeliculas().ModificarFecha(titulo,fecha)
            aux=aux.siguiente

    def ModificarHora(self,titulo,hora):
        aux=self.primero
        while aux is not None:
            aux.ObtenerListaPeliculas().ModificarHora(titulo,hora)
            aux=aux.siguiente
    
    def MostrarDetallePelicula(self,titulo):
        aux=self.primero
        while aux is not None:
            aux.ObtenerListaPeliculas().MostrarDetallePelicula(titulo)
            aux=aux.siguiente

    def MostrarCartelera(self,categoria):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNombre()==categoria:
                print('\n-----Detalle de la Categoría-------')
                print('Nombre: '+aux.ObtenerNombre())
                aux.ObtenerListaPeliculas().MostrarCartelera()
                break
            aux=aux.siguiente

    def MostrarCarteleraCompleta(self):
        aux=self.primero
        while aux is not None:
            
            print('\n-----Detalle de la Categoría-------')
            print('Nombre: '+aux.ObtenerNombre())
            aux.ObtenerListaPeliculas().MostrarCartelera()
            aux=aux.siguiente
    
    def CategoriaDevolverPelicula(self,titulo):
        aux=self.primero
        while aux is not None:
            pelicula=aux.ObtenerListaPeliculas().DevolverPelicula(titulo)
            if pelicula is not None:
                return pelicula
            aux=aux.siguiente
    
    def ExistePelicula(self,titulo):
        aux=self.primero
        while aux is not None:
            llave=aux.ObtenerListaPeliculas().ExistePeli(titulo)
            if llave:
                return True
            aux=aux.siguiente
        return False
    
    def escribirXML(self):
        texto="<categorias>\n"
        aux=self.primero
        while aux is not None:
            texto=texto+"\t<categoria>\n"
            texto=texto+"\t\t<nombre>"+str(aux.ObtenerNombre())+"</nombre>\n"
            texto=texto+aux.ObtenerListaPeliculas().EscribirXML()
            texto=texto+"\t</categoria>\n"
            aux=aux.siguiente
        texto=texto+"</categorias>\n"
        archivo = open("Categorias.xml", "w")
        archivo.write(texto)
        archivo.close()

    def HayCategoria(self,nombre):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerNombre()==nombre:
                return True
            aux=aux.siguiente
        return False



            
