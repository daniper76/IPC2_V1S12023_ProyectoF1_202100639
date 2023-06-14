from Categorias.ListaCategorias import ListaCategorias
from Usuarios.ListaSimple import ListaSimple
from Salas.ListaDoble import ListaDoble
from LecturaArchivo import*
from Usuarios.Factura import Factura 
flag=True
usuarios=ListaSimple()
usuarios.InsertarUsuario("Daniel","Peuch","37324046","danper76@ipc2.com","password","Administrador")
categorias=ListaCategorias()
salas=ListaDoble()

while flag:
    print('***************Bienvenido a Ovni********************')
    print('---------------Menú---------------')
    print('1.-Iniciar Sesión')
    print('2.-Registrar Usuarios')
    print('3.-Ver listados de Peliculas')
    print('4.-Salir :)')
    eleccion=input("Por favor ingresar el número de la opción deseada")
    if eleccion=='1':
        correo_guardado=input('Ingrese su correro registrado')
        contrasenia_guardado=input('Ingrese su contraseña')
        rol_encontrado=usuarios.ValidarUsuario(correo_guardado,contrasenia_guardado)
        if str(rol_encontrado).lower()=="cliente":
            flag_cliente=True
            while flag_cliente:

                print("\/\/\/\/\/*MENU CLIENTE*\/\/\/\/\/\n")
                print("1-.Ver Peliculas por Categoria")
                print("2-.Ver Listado General de Películas")
                print("3-.Ver Detalle de una Película")
                print("4-.Peliculas Favoritas")
                print("5-.Comprar Boletos")
                print("6-.Ver Historial")
                print("7-.Salir")   
                opcion_cliente=input("Seleccione el número de la opción deseada: ")

                if opcion_cliente=="1":
                    ver_categoria=input("Ingrese la categoría de películas deseada: ")
                    categorias.MostrarCartelera(ver_categoria)
                elif opcion_cliente=="2":
                    categorias.MostrarCarteleraCompleta()
                elif opcion_cliente=="3":
                    detalle_pelicula=input("Ingrese el título de la Película")
                    categorias.MostrarDetallePelicula(detalle_pelicula)
                elif opcion_cliente=="4":
                    flag_peli_favorita=True
                    while flag_peli_favorita:
                        print("----------Menú Películas Favoritas----------")
                        print("1-.Agregar Película Favorita")
                        print("2-.Ver Listado de Películas Favoritas")
                        print("3-.Salir")
                        opcion_peli_favorita=input("Seleccione el número de la opción deseada: ")

                        if opcion_peli_favorita=="1":
                            categorias.MostrarCarteleraCompleta()
                            nuevo_favorito=input("Ingresar el título de la pelicula que desea agregar a Favoritos")
                            existe_peli=categorias.ExistePelicula(nuevo_favorito)
                            existe_lista_fav=usuarios.ExisteFavorito(correo_guardado,nuevo_favorito)
                            if (existe_peli==True and existe_lista_fav==False):
                                pelicula_agregar=categorias.CategoriaDevolverPelicula(nuevo_favorito)
                                usuarios.AgregarPeliculaFavorita(correo_guardado,pelicula_agregar)

                        elif opcion_peli_favorita=="2":
                            print("Las películas favoritas del cliente se muestran a contiuación: ")
                            usuarios.MostrarFavoritos(correo_guardado)
                        
                        elif opcion_peli_favorita=="3":
                            flag_peli_favorita=False

                elif opcion_cliente=="5": 
                    flag_factura=True
                    while flag_factura:
                        print("-------Menú Compra de Boletos------")
                        print("1-.Comprar Boletos")
                        print("2-.Salir")
                        opcion_compra=input("Ingrese el número de la opción deseada: ")
                        if opcion_compra=="1":
                            flag_compra=True
                            while flag_compra:
                                categorias.MostrarCarteleraCompleta()
                                print("")
                                print("A continuación se muestran la cartelera: \n")
                                ver_pelicula=input("Ingrese el título de la Película: ")
                                print("")
                                existe_pelicula=categorias.ExistePelicula(ver_pelicula)

                                if existe_pelicula==True:
                                    print("Se muestra el detalle de la pelicula seleccionada: \n")
                                    categorias.MostrarDetallePelicula(ver_pelicula)
                                    print("")
                                    flag_sala_correcta=True
                                    while flag_sala_correcta:
                                        print("A continuación se muestra detalle de las salas disponibles: \n")
                                        salas.MostrarSalas()
                                        print("")
                                        eleccion_sala=input("Ingresar el número de sala : ")
                                        existe_sala=salas.ExisteSala(eleccion_sala)
                                        if existe_sala:
                                            print("--------Detalle de Sala-------")
                                            salas.MostrarDetalleSala(eleccion_sala)
                                            print("")
                                            print("El precio de cada boleto es de Q75.00\n")
                                            cantidad=input("Ingresar la cantidad de boletos que desea: ")
                                            precio=int(cantidad)*75
                                            print("El monto total es de: "+str(precio))
                                            id=0
                                            lista_asientos=[]
                                            while int(id)<int(cantidad):
                                                no_asiento=input("Ingrese el número del Asiento: ")
                                                lista_asientos.append(no_asiento)
                                                id+=1
                                            nombre_compra=input("Ingrese a nombre de quien se girará la factura: ")
                                            direccion=input("Ingrese su dirección: ")
                                            nit=input("Ingrese su NIT: ")
                                            factura=Factura(nombre_compra,direccion,nit,precio,cantidad,lista_asientos,eleccion_sala)
                                            usuarios.GuardarFactura(correo_guardado,factura)
                                            flag_sala_correcta=False
                                            flag_compra=False

                                        else:
                                            print("La sala no existe, ingresar una sala correcta")
                                else:
                                    print("No existe la pelicula, ingresar una de cartelera\n")

                        elif opcion_compra=="2":
                            flag_factura=False
                
                elif opcion_cliente=="6":
                    usuarios.MostrarHistorial(correo_guardado)
                elif opcion_cliente=="7":
                    flag_cliente=False



        elif str(rol_encontrado).lower()=="administrador":
            flag_admin=True
            while flag_admin:
                print("\/\/\/\/\/*MENU ADMINISTRADOR*\/\/\/\/\/\n")
                print("1-.Cargar Archivos")
                print("2-.Gestionar Películas")
                print("3-.Gestionar Usuarios")
                print("4-.Gestionar Salas")
                print("5-.Actualizar Archivos XML")
                print("6-.Salir")
                opcion_admin=input("Seleccione el número de la opción deseada: ")
                if opcion_admin=='1':
                    flag_cargar=True
                    while flag_cargar:
                        print("-----Menú Cargar-----\n")
                        print("1-.Cargar XML Usuarios")
                        print("2-.Cargar XML Categorías y Películas")
                        print("3-.Cargar XML Salas")
                        print("4.-Salir\n")
                        opcion_cargar=input("Ingresar el número de Opción Deseada: ")
                        if opcion_cargar=='1':
                            archivo=input("Ingrese el nombre del Archivo: ")
                            LecturaUsuarios(archivo,usuarios)
                        elif opcion_cargar=='2':
                            archivo=input("Ingrese el nombre del Archivo: ")
                            LecturaCategorias(archivo,categorias)
                        elif opcion_cargar=='3':
                            archivo=input("Ingrese el nombre del Archivo: ")
                            LectuuraSalas(archivo,salas)
                        elif opcion_cargar=='4':
                            flag_cargar=False
                        else:
                            print("Opción Inválida")
                
                elif opcion_admin=='2':
                    flag_gestionar_pelis=True
                    while flag_gestionar_pelis:
                        print("-----Menú Gestionar Películas-----\n")
                        print("1-.Crear Película")
                        print("2-.Borrar Película")
                        print("3-.Modificar Película")
                        print("4.-Mostrar Película")
                        print("5.-Mostrar Listado de Películas")
                        print("6.-Salir")

                        opcion_gestionar_pelis=input("Ingrese el número de la opción que desea realizar: ")

                        if opcion_gestionar_pelis=='1':
                            categoria_buscada=input("Ingrese la categoria de la Pelicula")
                            existe_categoria=categorias.BuscarCategorias(categoria_buscada)
                            if existe_categoria:
                                titulo=input("Ingrese el título de la Película: ")
                                director=input("Ingrese por quien fue dirigida la Película: ")
                                anio=input("Ingrese el año de Estreno: ")
                                fecha=input("Ingrese la fecha de la Función: ")
                                hora=input("Ingrese la hora de la Función: ")
                                categorias.ObtenerListaPeliculas(categoria_buscada).InsertarPelicula(titulo,director,anio,fecha,hora)
                            else:
                                categorias.InsertarCategoria(categoria_buscada)
                                titulo=input("Ingrese el título de la Película: ")
                                director=input("Ingrese por quien fue dirigida la Película: ")
                                anio=input("Ingrese el año de Estreno: ")
                                fecha=input("Ingrese la fecha de la Función: ")
                                hora=input("Ingrese la hora de la Función: ")
                                categorias.ObtenerListaPeliculas(categoria_buscada).InsertarPelicula(titulo,director,anio,fecha,hora)
                        
                        elif opcion_gestionar_pelis=='2':
                            pelicula_eliminar=input("Ingrese el título de la Película que desea eliminar")
                            categorias.EliminarPelicula(pelicula_eliminar)
                        
                        elif opcion_gestionar_pelis=='3':
                            flag_modificar_peli=True
                            if flag_modificar_peli:
                                print("--------Menú Modificar Pelicula------")
                                print("1-.Director o Directores")
                                print("2-.Año de Estreno")
                                print("3-.Fecha de la Función")
                                print("4-.Hora de la Función")
                                print("5-.Salir\n")
                                opcion_modificar=input("Ingresar el número de la opción que desea realizar: ")
                                print("")
                                if opcion_modificar=='1':
                                    titulo_modificar=input("Ingresar el título que se desea modificar ")
                                    nuevo_director=input("Ingresar el nuevo dato: ")
                                    categorias.ModificarDirector(titulo_modificar,nuevo_director)
                                elif opcion_modificar=='2':
                                    titulo_modificar=input("Ingresar el título que se desea modificar ")
                                    nuevo_anio=input("Ingresar el nuevo dato: ")
                                    categorias.ModificarAnio(titulo_modificar,nuevo_anio)
                                elif opcion_modificar=='3':
                                    titulo_modificar=input("Ingresar el título que se desea modificar ")
                                    nueva_fecha=input("Ingresar el nuevo dato: ")
                                    categorias.ModificarFecha(titulo_modificar,nueva_fecha)
                                elif opcion_modificar=='4':
                                    titulo_modificar=input("Ingresar el título que se desea modificar ")
                                    nueva_hora=input("Ingresar el nuevo dato: ")
                                    categorias.ModificarHora(titulo_modificar,nueva_hora)
                                elif opcion_modificar=='5':
                                    flag_modificar_peli=False
                        
                        elif opcion_gestionar_pelis=='4':
                            pelicula_detalle=input("Ingrese el titulo de la película: ")
                            categorias.MostrarDetallePelicula(pelicula_detalle)

                        elif opcion_gestionar_pelis=='5':
                            categorias.MostrarCategoriasPeliculas()
                        elif opcion_gestionar_pelis=='6':
                            flag_gestionar_pelis=False

                elif opcion_admin=='3':
                    flag_gestionar_usuarios=True
                    while flag_gestionar_usuarios:
                        print("-----Menú Gestionar Usuarios-----\n")
                        print("1-.Crear Usuario")
                        print("2-.Borrar Usuario")
                        print("3-.Modificar Usuario")
                        print("4.-Mostrar Usuario")
                        print("5.-Mostrar Listado de Usuarios")
                        print("6.-Salir\n")
                        opcion_gestionar_usuarios=input("Ingresar el número de la opción que desea realizar: ")
                        print("")
                        if opcion_gestionar_usuarios=='1':
                            nombre=input('Ingrese su nombre')
                            apellido=input('Ingrese su apellido')
                            telefono=input('Ingrese su teléfono')
                            correo=input('Ingrese su correo electrónico')
                            contrasenia=input('Ingrese su contraseña')
                            rol=input("Ingrese el rol del usuario")
                            confirmacion=usuarios.NuevoUsuario(correo)
                            if confirmacion:
                                usuarios.InsertarUsuario(nombre,apellido,telefono,correo,contrasenia,rol)
                        elif opcion_gestionar_usuarios=='2':
                            correo_eliminar=input("Ingrese el correo del Usuario a Eliminar")
                            usuarios.EliminarUsuario(correo_eliminar)
                        elif opcion_gestionar_usuarios=='3':
                            flag_modificar_usuarios=True
                            while flag_modificar_usuarios:
                                print("--------Menú Modificar Usuario--------")
                                print("1-.Nombre")
                                print("2-.Apellido")
                                print("3-.Teléfono")
                                print("4.-Contraseña")
                                print("5-.Salir\n")
                                opcion_modificar_usuario=input("Ingrese el número de la opción que desea realizar")
                                print("")
                                if opcion_modificar_usuario=='1':
                                    correo_modificar=input("Ingrese el correo del usuario")
                                    nombre_modificar=input("Ingrese el nuevo nombre")
                                    usuarios.ModificarNombre(correo_modificar,nombre_modificar)
                                elif opcion_modificar_usuario=='2':
                                    correo_modificar=input("Ingrese el correo del usuario")
                                    apellido_modificar=input("Ingrese el nuevo apellido")
                                    usuarios.ModificarApellido(correo_modificar,apellido_modificar)
                                elif opcion_modificar_usuario=='3':
                                    correo_modificar=input("Ingrese el correo del usuario")
                                    telefono_modificar=input("Ingrese el nuevo teléfono")
                                    usuarios.ModificarTelefono(correo_modificar,telefono_modificar)
                                elif opcion_modificar_usuario=='4':
                                    correo_modificar=input("Ingrese el correo del usuario")
                                    contracena_modificar=input("Ingrese la nueva contraseña")
                                    usuarios.ModificarContrasenia(correo_modificar,contracena_modificar)
                                elif opcion_modificar_usuario=='5':
                                    flag_modificar_usuarios=False
                                else:
                                    print("Opción Inválida")
                        
                        elif opcion_gestionar_usuarios=='4':
                            usuario_detalle=input("Ingrese el correo del usuario: ")
                            usuarios.MostrarDetalleUsuario(usuario_detalle)
                        
                        elif opcion_gestionar_usuarios=='5':
                            usuarios.MostrarUsuarios()

                        elif opcion_gestionar_usuarios=='6':
                            flag_gestionar_usuarios=False
                
                elif opcion_admin=='4':
                    flag_gestionar_salas=True
                    while flag_gestionar_salas:
                        print("-----Menú Gestionar Salas-----\n")
                        print("1-.Crear Sala")
                        print("2-.Borrar Sala")
                        print("3-.Modificar Sala")
                        print("4.-Mostrar Sala")
                        print("5.-Mostrar Listado de Salas")
                        print("6.-Salir\n")
                        opcion_gestionar_salas=input("Ingresar el número de la opción que desea realizar: ")
                        print("")
                        
                        if opcion_gestionar_salas=="1":
                            numero=input("Ingrese el número de la Sala")
                            asientos=input("Ingrese la cantidad de asientos de la Sala")
                            salas.InsertarSala(numero,asientos)
                        
                        elif opcion_gestionar_salas=="2":
                            numero_eliminar=input("Ingrese el número de Sala que desea eliminar")
                            salas.eliminar(numero_eliminar)
                        
                        elif opcion_gestionar_salas=="3":
                            flag_modificar_sala=True
                            while flag_modificar_sala:
                                print("-----Menú Modificar Salas-----\n")
                                print("1-.Modificar Número")
                                print("2-.Modificar Asientos")
                                print("3-.Salir")
                                opcion_modificar_sala=input("Ingrese el número de la carácteristica a eliminar: ")
                                if opcion_modificar_sala=="1":
                                    numero_modificar=input("Ingrese el número de Sala")
                                    nuevo_numero=input("Ingrese el nuevo número para la Sala")
                                    salas.ModificarNumero(numero_modificar,nuevo_numero)
                                elif opcion_modificar_sala=="2":
                                    numero_modificar=input("Ingrese el número de Sala")
                                    nuevo_asientos=input("Ingrese el nuevo número de asientos para la Sala")
                                    salas.ModificarAsientos(numero_modificar,nuevo_asientos)
                                elif opcion_modificar_sala=="3":
                                    flag_modificar_sala=False
                        
                        elif opcion_gestionar_salas=="4":
                            sala_buscar=input("Ingrese el número de Sala:")
                            salas.MostrarDetalleSala(sala_buscar)

                        elif opcion_gestionar_salas=="5":
                            salas.MostrarSalas()
                        
                        elif opcion_gestionar_salas=="6":
                            flag_gestionar_salas=False
                            
                elif opcion_admin=='5':
                    usuarios.escribirXML()
                    categorias.escribirXML()
                    salas.escribirXML()

                elif opcion_admin=='6':
                    flag_admin=False  

                else:
                    print("Opción Inválida, por favor ingresar una correcta")        

        else:
            print("Usuario Ote Inválido :/")

    elif eleccion=='2':
        print('-------------Registrar Usuario------------')
        nombre=input('Ingrese su nombre')
        apellido=input('Ingrese su apellido')
        telefono=input('Ingrese su teléfono')
        correo=input('Ingrese su correo electrónico')
        contrasenia=input('Ingrese su contraseña')
        confirmacion=usuarios.NuevoUsuario(correo)
        if confirmacion:
            usuarios.InsertarUsuario(nombre,apellido,telefono,correo,contrasenia)

    elif eleccion=='3':
        flag_ver_peli=True
        while flag_ver_peli:
            print("---------------Menú Visualizar Películas---------------\n")
            print("1-.Ver Listado General")
            print("2-.Ver Listado de Películas por Categorías")
            print("3-.Ver Detalle de Película")
            print("4-.Salir\n")
            opcion_ver=input("Ingrese el número de la opción que desea realizar\n")
            if opcion_ver=="1":
                categorias.MostrarCarteleraCompleta()
            
            elif opcion_ver=="2":
                categoria_ver=input("Ingresar la categoría de películas que desea ver: ")
                print("")
                categorias.MostrarCartelera(categoria_ver)
                print("")
            elif opcion_ver=="3":
                pelicula_ver=input("Ingrese el título de la película que desea ver: ")
                print("")
                categorias.MostrarDetallePelicula(pelicula_ver)
                print("")
    elif eleccion=='4':
        flag=False








