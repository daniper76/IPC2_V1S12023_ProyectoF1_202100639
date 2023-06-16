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
    print('***************Bienvenido********************')
    print('---------------Menú---------------')
    print('1.-Iniciar Sesión')
    print('2.-Registrar Usuarios')
    print('3.-Ver listados de Peliculas')
    print('4.-Salir :)')
    eleccion=input("Por favor ingresar el número de la opción deseada: ")
    if eleccion=='1':
        correo_guardado=input('Ingrese su correro registrado: ')
        contrasenia_guardado=input('Ingrese su contraseña: ')
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
                    while True:
                        categorias.MostrarCategorias()
                        ver_categoria=input("\nIngrese la categoría de películas deseada: ")
                        existe_categoria=categorias.HayCategoria(ver_categoria)
                        if existe_categoria:
                            categorias.MostrarCartelera(ver_categoria)
                            break
                        else:
                            print("No existe la categoria,ingrese una válida\n")
                elif opcion_cliente=="2":
                    categorias.MostrarCarteleraCompleta()
                elif opcion_cliente=="3":
                    while True:
                        categorias.MostrarCarteleraCompleta()
                        detalle_pelicula=input("Ingrese el título de la Película")
                        existe_pelicula=categorias.ExistePelicula(detalle_pelicula)
                        if existe_pelicula:
                            categorias.MostrarDetallePelicula(detalle_pelicula)
                            break
                        else:
                            print("No existe película, ingrese una existente\n")
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
                            elif (existe_peli==True and existe_lista_fav==True):
                                print("La película ya esta en favoritos")
                            else:
                                print("La película no existe")
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
                                            print("El precio de cada boleto es de Q42.00\n")
                                            cantidad=input("Ingresar la cantidad de boletos que desea: ")
                                            precio=int(cantidad)*42
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
                                            print("\nLa sala no existe, ingresar una sala correcta\n")
                                else:
                                    print("\nNo existe la pelicula, ingresar una de cartelera\n")

                        elif opcion_compra=="2":
                            flag_factura=False
                
                elif opcion_cliente=="6":
                    usuarios.MostrarHistorial(correo_guardado)
                elif opcion_cliente=="7":
                    flag_cliente=False
                else:
                    print("\nOpción Invalida, ingrese una correcta\n")



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
                            print("\n Archivo Cargado\n")
                        elif opcion_cargar=='2':
                            archivo=input("Ingrese el nombre del Archivo: ")
                            LecturaCategorias(archivo,categorias)
                            print("\n Archivo Cargado\n")
                        elif opcion_cargar=='3':
                            archivo=input("Ingrese el nombre del Archivo: ")
                            LectuuraSalas(archivo,salas)
                            print("\n Archivo Cargado\n")
                        elif opcion_cargar=='4':
                            flag_cargar=False
                        else:
                            print("\nOpción Inválida, ingrese una opción correcta\n")
                
                elif opcion_admin=='2':
                    flag_gestionar_pelis=True
                    while flag_gestionar_pelis:
                        print("-----Menú Gestionar Películas-----\n")
                        print("1-.Crear Película")
                        print("2-.Borrar Película")
                        print("3-.Modificar Película")
                        print("4.-Mostrar Película")
                        print("5.-Mostrar Listado de Películas")
                        print("6.-Salir\n")

                        opcion_gestionar_pelis=input("Ingrese el número de la opción que desea realizar: ")

                        if opcion_gestionar_pelis=='1':
                            categoria_buscada=input("Ingrese la categoria de la Pelicula")
                            existe_categoria=categorias.BuscarCategorias(categoria_buscada)
                            if existe_categoria:
                                while True:
                                    titulo=input("Ingrese el título de la Película: ")
                                    director=input("Ingrese por quien fue dirigida la Película: ")
                                    anio=input("Ingrese el año de Estreno: ")
                                    fecha=input("Ingrese la fecha de la Función: ")
                                    hora=input("Ingrese la hora de la Función: ")
                                    existe_pelicula=categorias.ExistePelicula(titulo)
                                    if existe_pelicula==False:
                                        categorias.ObtenerListaPeliculas(categoria_buscada).InsertarPelicula(titulo,director,anio,fecha,hora)
                                        break
                                    else:
                                        print("\nYa existe la película, ingrese una nueva\n")
                            else:
                                categorias.InsertarCategoria(categoria_buscada)
                                while True:
                                    titulo=input("Ingrese el título de la Película: ")
                                    director=input("Ingrese por quien fue dirigida la Película: ")
                                    anio=input("Ingrese el año de Estreno: ")
                                    fecha=input("Ingrese la fecha de la Función: ")
                                    hora=input("Ingrese la hora de la Función: ")
                                    existe_pelicula=categorias.ExistePelicula(titulo)
                                    if existe_peli==False:
                                        categorias.ObtenerListaPeliculas(categoria_buscada).InsertarPelicula(titulo,director,anio,fecha,hora)
                                        break
                                    else:
                                        print("\nnLa película ya existe, ingrese una nueva\n")
                        
                        elif opcion_gestionar_pelis=='2':
                            while True:
                                categorias.MostrarCarteleraCompleta()
                                print("")
                                pelicula_eliminar=input("Ingrese el título de la Película que desea eliminar")
                                existe_pelicula=categorias.ExistePelicula(pelicula_eliminar)
                                if existe_pelicula:
                                    categorias.EliminarPelicula(pelicula_eliminar)
                                    print("\nPelícula Eliminada\n")
                                    break
                                else:
                                    print("\n No existe película, ingrese una existente")
                        
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
                                    while True:
                                        categorias.MostrarCarteleraCompleta()
                                        print("")
                                        titulo_modificar=input("Ingresar el título que se desea modificar ")
                                        existe_peli=categorias.ExistePelicula(titulo_modificar)
                                        if existe_peli:
                                            nuevo_director=input("Ingresar el nuevo dato: ")
                                            categorias.ModificarDirector(titulo_modificar,nuevo_director)
                                            print("Película modificada")
                                            break
                                        else:
                                            print("No existe la película, ingrese una válida")
                                elif opcion_modificar=='2':
                                    while True:
                                        categorias.MostrarCarteleraCompleta()
                                        print("")
                                        titulo_modificar=input("Ingresar el título que se desea modificar ")
                                        existe_peli=categorias.ExistePelicula(titulo_modificar)
                                        if existe_peli:
                                            nuevo_anio=input("Ingresar el nuevo dato: ")
                                            categorias.ModificarAnio(titulo_modificar,nuevo_anio)
                                            print("Película modificada")
                                            break
                                        else:
                                            print("No existe la película, ingrese una válida")
                                elif opcion_modificar=='3':
                                    while True:
                                        categorias.MostrarCarteleraCompleta()
                                        print("")
                                        titulo_modificar=input("Ingresar el título que se desea modificar ")
                                        existe_peli=categorias.ExistePelicula(titulo_modificar)
                                        if existe_peli:
                                            nueva_fecha=input("Ingresar el nuevo dato: ")
                                            categorias.ModificarFecha(titulo_modificar,nueva_fecha)
                                            print("Usuario Modificado")
                                            break
                                        else:
                                            print("No existe película, ingrese una válida")
                                elif opcion_modificar=='4':
                                    while True:
                                        categorias.MostrarCarteleraCompleta()
                                        print("")
                                        titulo_modificar=input("Ingresar el título que se desea modificar ")
                                        existe_peli=categorias.ExistePelicula(titulo_modificar)
                                        if existe_peli:
                                            nueva_hora=input("Ingresar el nuevo dato: ")
                                            categorias.ModificarHora(titulo_modificar,nueva_hora)
                                            print("Película Modificada")
                                            break
                                        else:
                                            print("No existe película")                                    
                                elif opcion_modificar=='5':
                                    flag_modificar_peli=False
                                else:
                                    print("Opción invalida, ingrese una opción válida")
                        
                        elif opcion_gestionar_pelis=='4':
                            while True:
                                categorias.MostrarCarteleraCompleta()
                                print("")
                                pelicula_detalle=input("Ingrese el titulo de la película: ")
                                existe=categorias.ExistePelicula(pelicula_detalle)
                                if existe:
                                    categorias.MostrarDetallePelicula(pelicula_detalle)
                                    break
                                else:
                                    print("No existe la película, ingrese una existente")

                        elif opcion_gestionar_pelis=='5':
                            categorias.MostrarCategoriasPeliculas()
                        elif opcion_gestionar_pelis=='6':
                            flag_gestionar_pelis=False
                        else:
                            print("Opción seleccionada incorrecta, Ingrese una opción válida")

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
                            while True:
                                nombre=input('Ingrese su nombre')
                                apellido=input('Ingrese su apellido')
                                telefono=input('Ingrese su teléfono')
                                correo=input('Ingrese su correo electrónico')
                                contrasenia=input('Ingrese su contraseña')
                                rol=input("Ingrese el rol del usuario")
                                confirmacion=usuarios.NuevoUsuario(correo)
                                if confirmacion:
                                    usuarios.InsertarUsuario(nombre,apellido,telefono,correo,contrasenia,rol)
                                    print("Usuario Agregado")
                                    break
                                else:
                                    print("El usuario ya existe")
                        elif opcion_gestionar_usuarios=='2':
                            while True:
                                usuarios.MostrarCorreosUsuarios()
                                print("")
                                correo_eliminar=input("Ingrese el correo del Usuario a Eliminar")
                                existe_usuario=usuarios.NuevoUsuario(correo_eliminar)
                                if existe_usuario==False:
                                    usuarios.EliminarUsuario(correo_eliminar)
                                    print("Usuario Eliminado")
                                    break
                                else:
                                    print("No existe el usuario, ingrese uno existente")
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
                                    while True:
                                        usuarios.MostrarCorreosUsuarios()
                                        print("")
                                        correo_modificar=input("Ingrese el correo del usuario: ")
                                        nuevo_usuario=usuarios.NuevoUsuario(correo_modificar)
                                        if nuevo_usuario==False:
                                            nombre_modificar=input("Ingrese el nuevo nombre: ")
                                            usuarios.ModificarNombre(correo_modificar,nombre_modificar)
                                            print("Usuario Modificado")
                                            break
                                        else:
                                            print("El usuario no existe, ingrese uno existente")
                                elif opcion_modificar_usuario=='2':
                                    while True:
                                        usuarios.MostrarCorreosUsuarios()
                                        print("")
                                        correo_modificar=input("Ingrese el correo del usuario: ")
                                        nuevo_usuario=usuarios.NuevoUsuario(correo_modificar)
                                        if nuevo_usuario==False:
                                            apellido_modificar=input("Ingrese el nuevo apellido: ")
                                            usuarios.ModificarApellido(correo_modificar,apellido_modificar)
                                            print("Usuario Modificado")
                                            break
                                        else:
                                            print("El usuario no existe, ingrese uno nuevo")
                                elif opcion_modificar_usuario=='3':
                                    while True:
                                        usuarios.MostrarCorreosUsuarios()
                                        print("")
                                        correo_modificar=input("Ingrese el correo del usuario")
                                        nuevo_usuario=usuarios.NuevoUsuario(correo_modificar)
                                        if nuevo_usuario==False:
                                            telefono_modificar=input("Ingrese el nuevo teléfono")
                                            usuarios.ModificarTelefono(correo_modificar,telefono_modificar)
                                            print("Usuario Modificado")
                                            break
                                        else:
                                            print("No existe el usuario, ingrese uno nuevo")
                                elif opcion_modificar_usuario=='4':
                                    while True:
                                        usuarios.MostrarCorreosUsuarios()
                                        print("")
                                        correo_modificar=input("Ingrese el correo del usuario")
                                        nuevo_usuario=usuarios.NuevoUsuario(correo_modificar)
                                        if nuevo_usuario==False:
                                            contracena_modificar=input("Ingrese la nueva contraseña")
                                            usuarios.ModificarContrasenia(correo_modificar,contracena_modificar)
                                            print("Usuario Modificado")
                                            break
                                        else:
                                            print("No existe usuario, ingrese uno valido")
                                elif opcion_modificar_usuario=='5':
                                    flag_modificar_usuarios=False
                                else:
                                    print("Opción Inválida, ingrese una opción inválida")
                        
                        elif opcion_gestionar_usuarios=='4':
                            while True:
                                usuarios.MostrarCorreosUsuarios()
                                print("")
                                usuario_detalle=input("Ingrese el correo del usuario: ")
                                nuevo_usuario=usuarios.NuevoUsuario(usuario_detalle)
                                if nuevo_usuario==False:
                                    usuarios.MostrarDetalleUsuario(usuario_detalle)
                                    break
                                else:
                                    print("No existe el usuario, ingrese uno nuevo")
                        
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
                            while True:
                                numero=input("Ingrese el número de la Sala: ")
                                asientos=input("Ingrese la cantidad de asientos de la Sala: ")
                                existe_sala_ya=salas.ExisteSala(numero)
                                if existe_sala_ya==False:
                                    salas.InsertarSala(numero,asientos)
                                    break
                                else:
                                    print("\nLa sala ya existe, ingrese una sala nueva\n")
                        
                        elif opcion_gestionar_salas=="2":
                            llave_eliminar_sala=True
                            while llave_eliminar_sala:
                                salas.MostrarNumeroSalas()
                                print("")
                                numero_eliminar=input("Ingrese el número de Sala que desea eliminar")
                                existe_sala_eliminar=salas.ExisteSala(numero_eliminar)
                                if existe_sala_eliminar==True:
                                    salas.eliminar(numero_eliminar)
                                    print("Sala eliminada")
                                    llave_eliminar_sala=False
                                else:
                                    print("Ingrese una sala existente")

                        
                        elif opcion_gestionar_salas=="3":
                            flag_modificar_sala=True
                            while flag_modificar_sala:
                                print("-----Menú Modificar Salas-----\n")
                                print("1-.Modificar Número")
                                print("2-.Modificar Asientos")
                                print("3-.Salir")
                                opcion_modificar_sala=input("Ingrese el número de la carácteristica a eliminar: ")
                                if opcion_modificar_sala=="1":
                                    while True:
                                        salas.MostrarNumeroSalas()
                                        print("")
                                        numero_modificar=input("Ingrese el número de Sala: ")
                                        existe_sala_modificar=salas.ExisteSala(numero_modificar)
                                        if existe_sala_modificar==True:
                                            nuevo_numero=input("Ingrese el nuevo número para la Sala: ")
                                            salas.ModificarNumero(numero_modificar,nuevo_numero)
                                            break
                                        else:
                                            print("La sala no existe")
                                elif opcion_modificar_sala=="2":
                                    while True:
                                        salas.MostrarNumeroSalas()
                                        print("")
                                        numero_modificar=input("Ingrese el número de Sala: ")
                                        existe_sala_modificar=salas.ExisteSala(numero_modificar)
                                        if existe_sala_modificar:
                                            nuevo_asientos=input("Ingrese el nuevo número de asientos para la Sala")
                                            salas.ModificarAsientos(numero_modificar,nuevo_asientos)
                                            break
                                        else:
                                            print("No existe la sala")
                                elif opcion_modificar_sala=="3":
                                    flag_modificar_sala=False
                                else:
                                    print("Opción inválida, ingrese una opción correcta")
                        
                        elif opcion_gestionar_salas=="4":
                            salas.MostrarNumeroSalas()
                            print("")
                            sala_buscar=input("Ingrese el número de Sala:")
                            salas.MostrarDetalleSala(sala_buscar)

                        elif opcion_gestionar_salas=="5":
                            salas.MostrarSalas()
                        
                        elif opcion_gestionar_salas=="6":
                            flag_gestionar_salas=False
                        else:
                            print("")
                            
                elif opcion_admin=='5':
                    usuarios.escribirXML()
                    categorias.escribirXML()
                    salas.escribirXML()
                    print("\nArchivos XML actualizados :)\n")

                elif opcion_admin=='6':
                    flag_admin=False  

                else:
                    print("Opción Inválida, por favor ingresar una correcta")        

        else:
            print("Usuario Inválido :/")

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
        else:
            print("\nYa existe un usuario con ese correo :/\n")

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
                flag_ver_algo=True
                while flag_ver_algo:
                    categorias.MostrarCategorias()
                    print("")
                    categoria_ver=input("Ingresar la categoría de películas que desea ver: ")
                    print("")
                    llave_categoria=categorias.HayCategoria(categoria_ver)
                    if llave_categoria:
                        categorias.MostrarCartelera(categoria_ver)
                        print("")
                        flag_ver_algo=False
                    else:
                        print("La categoría no existe, ingrese una de lista")
            elif opcion_ver=="3":
                flag_ver_detalle=True
                while flag_ver_detalle:
                    categorias.MostrarCarteleraCompleta()
                    print("")
                    pelicula_ver=input("Ingrese el título de la película que desea ver: ")
                    print("")
                    llave_peliculas=categorias.ExistePelicula(pelicula_ver)
                    if llave_peliculas:
                        categorias.MostrarDetallePelicula(pelicula_ver)
                        print("")
                        flag_ver_detalle=False
                    else:
                        print("No existe la película, ingrese una de la lista")
            elif  opcion_ver=="4":
                flag_ver_peli=False
            else:
                print("Opción inválida, ingrese una opción válida")
    
    elif eleccion=='4':
        flag=False
    else:
        print("Opción inválida, Ingrese una opción válida")








