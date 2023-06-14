class Factura:
    id=1
    def __init__(self,nombre,direccion,nit,monto,cantidad_boletos,asientos: list,sala):
        self.nombre=nombre
        self.direccion=direccion
        self.nit=nit
        self.monto=monto
        self.cantidad_boletos=cantidad_boletos
        self.asientos=asientos
        self.sala=sala
        self.boleto="#USACIPC2_202100639_"+str(Factura.id)
        self.id=Factura.id
        Factura.id+=1
    
    def ObtenerNombre(self):
        return self.nombre
    
    def ObtenerDireccion(self):
        return self.direccion
    
    def ObtenerNit(self):
        return self.nit
    
    def ObtenerMonto(self):
        return self.monto
    
    def ObtenerCantidadBoletos(self):
        return self.cantidad_boletos
    
    def ObtenerAsientos(self):
        return self.asientos
    
    def ObtenerSala(self):
        return self.sala
    
    def ObtenerId(self):
        return self.id
    
    def ObtenerNombreBoleto(self):
        return self.boleto

    