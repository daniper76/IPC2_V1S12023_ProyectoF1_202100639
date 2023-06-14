from .ListaPeliculasDC import ListaDobleCircular

class Categoria:
    id=1

    def __init__(self,nombre):
        self.nombre=nombre
        self.lista_peliculas=ListaDobleCircular()
        self.siguiente=None
        self.id=Categoria.id
        Categoria.id+=1

    def ObtenerNombre(self):
        return self.nombre
    
    def ObtenerListaPeliculas(self):
        return self.lista_peliculas
    
    def ObtenerId(self):
        return self.id
    
    

    

    
        