class Sala:
    id=1
    def __init__(self,numero,asientos):
        self.numero=numero
        self.asientos=asientos
        self.id=Sala.id
        Sala.id+=1
        self.siguiente=None
        self.anterior=None

    def ObtenerNumero(self):
        return self.numero
    
    def ObtenerAsientos(self):
        return self.asientos

    def ObtenerId(self):
        return self.id
    
