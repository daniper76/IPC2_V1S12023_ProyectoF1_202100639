class Pelicula:
    id=1
    
    def __init__(self,titulo,director,anio,fecha,hora):
        self.titulo=titulo
        self.director=director
        self.anio=anio
        self.fecha=fecha
        self.hora=hora
        self.siguiente=None
        self.anterior=None
        self.id=Pelicula.id
        Pelicula.id+=1
    
    def ObtenerTitulo(self):
        return self.titulo
    
    def ObtenerDirector(self):
        return self.director
    
    def ObtenerAnio(self):
        return self.anio
    
    def ObtenerFecha(self):
        return self.fecha
    
    def ObtenerHora(self):
        return self.hora
    
    def ObtenerId(self):
        return self.id
