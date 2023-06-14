from xml.dom import minidom
from Usuarios.ListaSimple import ListaSimple
from Categorias.ListaCategorias import ListaCategorias
from Salas.ListaDoble import ListaDoble


def LecturaUsuarios(archivo,lista_usuarios: ListaSimple):
    
    doc=minidom.parse(str(archivo))
    raices=doc.getElementsByTagName("usuarios")

    for raiz in raices:
        listado_usuarios=raiz.getElementsByTagName("usuario")

        for usuario in listado_usuarios:
            nombre=usuario.getElementsByTagName("nombre")
            apellido=usuario.getElementsByTagName("apellido")
            telefono=usuario.getElementsByTagName("telefono")
            correo=usuario.getElementsByTagName("correo")
            contrasena=usuario.getElementsByTagName("contrasena")
            rol=usuario.getElementsByTagName("rol")

            nombre_usuario=str(nombre[0].firstChild.nodeValue)
            apellido_usuario = str(apellido[0].firstChild.nodeValue)
            telefono_usuario=str(telefono[0].firstChild.nodeValue)
            correo_usuario=str(correo[0].firstChild.nodeValue)
            contrasena_usuario=str(contrasena[0].firstChild.nodeValue)
            rol_usuario=str(rol[0].firstChild.nodeValue)

            nuevo_usuario=lista_usuarios.NuevoUsuario(correo_usuario)
            if nuevo_usuario:
                lista_usuarios.InsertarUsuario(nombre_usuario,apellido_usuario,telefono_usuario,correo_usuario,contrasena_usuario,rol_usuario)

def LecturaCategorias(archivo,lista_categorias: ListaCategorias):

    doc=minidom.parse(str(archivo))
    raices=doc.getElementsByTagName("categorias")

    for raiz in raices:
        categorias=raiz.getElementsByTagName("categoria")
        id=1
        for categoria in categorias:
            nombre=categoria.getElementsByTagName("nombre")
            nombre_categoria=str(nombre[0].firstChild.nodeValue)
            lista_categorias.InsertarCategoria(nombre_categoria)
            listado_peliculas=categoria.getElementsByTagName("peliculas")
            for peliculas in listado_peliculas:
                pelicula=peliculas.getElementsByTagName("pelicula")
                for peli in pelicula:
                    titulo=peli.getElementsByTagName("titulo")
                    director=peli.getElementsByTagName("director")
                    anio=peli.getElementsByTagName("anio")
                    fecha=peli.getElementsByTagName("fecha")
                    hora=peli.getElementsByTagName("hora")
                    titulo_peli=str(titulo[0].firstChild.nodeValue)
                    director_peli=str(director[0].firstChild.nodeValue)
                    anio_peli=str(anio[0].firstChild.nodeValue)
                    fecha_peli=str(fecha[0].firstChild.nodeValue)
                    hora_peli=str(hora[0].firstChild.nodeValue)
                    lista_categorias.BuscarListaPeliculas(id).InsertarPelicula(titulo_peli,director_peli,anio_peli,fecha_peli,hora_peli)

            id+=1

def LectuuraSalas(archivo,lista_salas: ListaDoble):
    doc=minidom.parse(str(archivo))
    raices=doc.getElementsByTagName("cines")
    
    for raiz in raices:
        cines=raiz.getElementsByTagName("cine")

        for cine in cines:
            listado_salas=cine.getElementsByTagName("salas")
            for salas in listado_salas:
                grupo_salas=salas.getElementsByTagName("sala")

                for sala in grupo_salas:
                    numero=sala.getElementsByTagName("numero")
                    asientos=sala.getElementsByTagName("asientos")
                    numero_sala=str(numero[0].firstChild.nodeValue)
                    asientos_sala=str(asientos[0].firstChild.nodeValue)
                    lista_salas.InsertarSala(numero_sala,asientos_sala)
    








