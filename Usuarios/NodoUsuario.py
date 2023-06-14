class NodoUsuario:
    id=1
    
    def __init__(self,nombre,apellido,telefono,correo,contrasenia,rol='cliente'):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.correo=correo
        self.contrasenia=contrasenia
        self.siguiente=None
        self.id=NodoUsuario.id
        self.rol=rol
        self.favoritos=[]
        self.facturas=[]
        NodoUsuario.id+=1
    
    def ObtenerId(self):
        return self.id

    def ObtenerNombre(self):
        return self.nombre
    
    def ObtenerApellido(self):
        return self.apellido
    
    def ObtenerTelefono(self):
        return self.telefono
    
    def ObtenerCorreo(self):
        return self.correo
    
    def ObtenerContrasenia(self):
        return self.contrasenia

    def ObtenerRol(self):
        return self.rol
    
    def ObtenerFavoritos(self):
        return self.favoritos
    
    def ObtenerFacturas(self):
        return self.facturas
        