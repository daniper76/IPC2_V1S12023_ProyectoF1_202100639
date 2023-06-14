from .NodoUsuario import NodoUsuario

class ListaSimple:

    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def InsertarUsuario(self,nombre,apellido,telefono,correo,contrasenia,rol='cliente'):
        nuevo_usuario=NodoUsuario(nombre,apellido,telefono,correo,contrasenia,rol)
        
        if self.primero == None:
            self.primero = nuevo_usuario
            self.ultimo = nuevo_usuario
        else: 
            self.ultimo.siguiente = nuevo_usuario
            self.ultimo = nuevo_usuario
    
    def MostrarUsuarios(self):
        aux=self.primero
        while aux is not None:
            print('-----Detalle del Usuario-------')
            print('Nombre: '+aux.ObtenerNombre())
            print('Apellido: '+aux.ObtenerApellido())
            print('Teléfono: '+aux.ObtenerTelefono())
            print('Correo: '+aux.ObtenerCorreo())
            print('Contraseña: '+aux.ObtenerContrasenia())
            print('Rol: '+aux.ObtenerRol())
            aux=aux.siguiente
    
    def EliminarUsuario(self,correo):

        self.ExistenciaUsuario(correo)
        aux=self.primero
        anterior=None
        while aux is not None:
            if aux.ObtenerCorreo()==correo:
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
    
    def ModificarNombre(self,correo,nombre):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==correo:
                aux.nombre=nombre
            aux=aux.siguiente

    def ModificarApellido(self,correo,apellido):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==correo:
                aux.apellido=apellido
            aux=aux.siguiente

    def ModificarTelefono(self,correo,telefono):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==correo:
                aux.telefono=telefono
            aux=aux.siguiente

    def ModificarContrasenia(self,correo,contrasenia):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==correo:
                aux.contrasenia=contrasenia
            aux=aux.siguiente

    def NuevoUsuario(self,correo):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==correo:
                return False
            aux=aux.siguiente
        return True
    
    def ValidarUsuario(self,correo,contrasenia):
        aux=self.primero
        while aux is not None:
            if (aux.ObtenerCorreo()==correo and aux.ObtenerContrasenia()==contrasenia):
                return aux.ObtenerRol()
            aux=aux.siguiente
        return False
    
    def ExistenciaUsuario(self,correo):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==correo:
                return "Se eliminó el usuario con correro: "+aux.ObtenerCorreo()
            aux=aux.siguiente
        return "El usuario no existe"

    def MostrarDetalleUsuario(self,correo):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==correo:
                print('-----Detalle del Usuario-------')
                print('Nombre: '+aux.ObtenerNombre())
                print('Apellido: '+aux.ObtenerApellido())
                print('Teléfono: '+aux.ObtenerTelefono())
                print('Correo: '+aux.ObtenerCorreo())
                print('Contraseña: '+aux.ObtenerContrasenia())
                print('Rol: '+aux.ObtenerRol())
            aux=aux.siguiente
    
    def AgregarPeliculaFavorita(self,usuario,pelicula):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==usuario:
                aux.ObtenerFavoritos().append(pelicula)
                break
            aux=aux.siguiente
    
    def ExisteFavorito(self,usuario,pelicula):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==usuario:
                lista_favoritos=aux.ObtenerFavoritos()
                if len(lista_favoritos)==0:
                    return False
                else:
                    for fav in lista_favoritos:
                        if fav.titulo==pelicula:
                            return True
                    return False
            aux=aux.siguiente
    
    def MostrarFavoritos(self,usuario):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==usuario:
                lista_favoritos=aux.ObtenerFavoritos()
                for fav in lista_favoritos:
                    print("-----------------------------------")
                    print("Título: "+str(fav.titulo))
                    print("Dirigido por: "+str(fav.director))
                    print("Año de Estreno: "+str(fav.anio))
            aux=aux.siguiente

    def GuardarFactura(self,usuario,factura):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==usuario:
                aux.ObtenerFacturas().append(factura)
            aux=aux.siguiente

    def MostrarHistorial(self,usuario):
        aux=self.primero
        while aux is not None:
            if aux.ObtenerCorreo()==usuario:
                historial=aux.ObtenerFacturas()
                for factura in historial:
                    print("-----------Boleto "+str(factura.boleto)+"--------------")
                    print("\tCliente: "+str(factura.nombre))
                    print("\tDireccion: "+str(factura.direccion))
                    print("\tNit: "+str(factura.nit))
                    print("\tMonto: "+str(factura.monto))
                    print("\tCantidad de Boletos: "+str(factura.cantidad_boletos))
                    total_asientos=factura.asientos
                    for asiento in total_asientos:
                        print("Asiento: "+str(asiento))
                    print("\tSala: "+str(factura.sala))
            aux=aux.siguiente  

    def escribirXML(self):
        if self.primero is None:
            print("La lista esta vacia")
        else:
            archivo = open("Usuarios.xml", "w")
            archivo.write("<usuarios>\n")

            aux = self.primero
            while aux is not None:
                archivo.write("\t<usuario>\n")
                archivo.write("\t\t<rol>" + str(aux.ObtenerRol()) + "</rol>\n")
                archivo.write("\t\t<nombre>" + str(aux.ObtenerNombre()) + "</nombre>\n")
                archivo.write("\t\t<apellido>" + str(aux.ObtenerApellido()) + "</apellido>\n")
                archivo.write("\t\t<telefono>" + str(aux.ObtenerTelefono()) + "</telefono>\n")
                archivo.write("\t\t<correo>" + str(aux.ObtenerCorreo()) + "</correo>\n")
                archivo.write("\t\t<contrasena>" + str(aux.ObtenerContrasenia()) + "</contrasena>\n")
                archivo.write("\t</usuario>\n")
                aux = aux.siguiente
            archivo.write("</usuario>")
            archivo.close()      

                    
                

            


            

            



        

    
    




    






            

        


