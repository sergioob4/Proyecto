from Admin import *
from Sistem import *
from Usuario import *
from multimedia import *
import os


# Menu de inicio:
def menu():
    # Hacemos toda la carga inicial del precargado
    if os.stat("C:/Users/Sergio/Desktop/Proyecto/usuarios.txt").st_size == 0:
        importar = True
    else:
        importar = False
    if importar:
        bd_usuarios, feed = iniciar_api()
        cargar_posts(feed)
        cargar_usuarios(bd_usuarios)

    else:
        bd_usuarios = []
        feed = []
        bd_usuarios = leer_usuarios(bd_usuarios)
        feed = leer_posts(feed)
    
    eliminados = []
# Usuario creado sergioob4 como admin, ademas se borraron algunos posts como prueba 
    
    while True: #Menu principal
        principal = input("Bienvenido a Metrogram \n\n1-Iniciar sesión\n2-Registrarse\n3-Salir\n")
        
        principal= validar_opcion_numerica(principal, 1, 3, "1. Iniciar sesión\n2. Registrarse\n3. Salir\n")
        
        if principal == 1: #Inicio de sesesion:
            usuario = input("Bienvenido ingrese su su nombre de usuario : ")
            usuario = validar_usuario(usuario, "Bienvenido ingrese su username :  ",bd_usuarios, "iniciar")
            if usuario != None and usuario.tipo_usuario != "admin":
                
                while True: #Menu de usuario:
                    opcion = input("\nBienvenido, ¿Qué desea hacer?\n1-Ver publicaciones\n2-Ver perfil\n3-Subir multimedia\n4-Buscar una cuenta \n5-Configuracion \n6-Cerrar sesión\n")
                    opcion = validar_opcion_numerica(opcion, 1, 6, "1. Ver publicaciones\n2. Ver perfil\n3. Subir multimedia\n4. Buscar una cuenta \n5. Configuracion \n6. Cerrar sesión\n")
                    
                    if opcion == 1:
                        usuario.ver_publicaciones(feed, usuario, bd_usuarios)
                        cargar_usuarios(bd_usuarios)
                        cargar_posts(feed)
                    elif opcion == 2:
                        usuario.ver_perfil()
                    elif opcion == 3:
                        usuario.crear_publicacion(feed)
                        cargar_usuarios(bd_usuarios)
                        cargar_posts(feed)   
                    elif opcion == 4:
                        filtro = input("\nSelecciona el criterio de búsqueda:\n1. Usuario\n2. Departamento/Carrera\n")
                        filtro = validar_opcion_numerica(filtro, 1, 2, "Selecciona el criterio de búsqueda:\n1. Usuario\n2. Departamento/Carrera\n")
                        if filtro == 1:
                            user = buscar_usuario(bd_usuarios)
                            if user != None:
                                user.ver_perfil()
                                if not user in usuario.amigos:
                                    seg = input("¿Desea seguir a este usuario?\n1. Sí\n2. No\n")
                                    seg = validar_opcion_numerica(seg, 1, 2, "¿Desea seguir a este usuario?\n1. Sí\n2. No\n")
                                    if seg == 1:
                                        usuario.seguir(user)
                                        cargar_usuarios(bd_usuarios)
                                else:
                                    seg = input("¿Desea dejar de seguir a este usuario?\n1. Sí\n2. No\n")
                                    seg = validar_opcion_numerica(seg, 1, 2, "¿Desea dejar de seguir a este usuario?\n1. Sí\n2. No\n")
                                    if seg == 1:
                                        usuario.dejar_de_seguir(user)
                                        cargar_usuarios(bd_usuarios)
                            else:
                                print("No existe ese usuario.")
                        elif filtro == 2:
                            usuarios = buscar_cardep(bd_usuarios)
                            if usuarios != None:
                                for user in usuarios:
                                    if not user == usuario:
                                        user.ver_perfil()
                                        if not user in usuario.amigos:
                                            seg = input("¿Desea seguir a este usuario?\n1-Sí\n2-No\n")
                                            seg = validar_opcion_numerica(seg, 1, 2, "¿Desea seguir a este usuario?\n1-Sí\n2-No\n")
                                            if seg == 1:
                                                usuario.seguir(user)
                                                cargar_usuarios(bd_usuarios)
                                        else:
                                            seg = input("¿Desea dejar de seguir a este usuario?\n1-Sí\n2-No\n")
                                            seg = validar_opcion_numerica(seg, 1, 2, "¿Desea dejar de seguir a este usuario?\n1-Sí\n2-No\n")
                                            if seg == 1:
                                                usuario.dejar_de_seguir(user)
                                                cargar_usuarios(bd_usuarios)
                            else:
                                print("No hay usuarios con ese departamento/carrera.")
                             
                    elif opcion == 5:
                        opcion = input("\n**** CONFIGURACION **** \n 1.Editar Perfil \n2.Eliminar comentario de un post\n 3.Gestionar mis seguidos\n 4.Eliminar Cuenta \n 5.Salir \n")
                        opcion = validar_opcion_numerica(opcion, 1, 5, "**** CONFIGURACION **** \n 1.Editar Perfil \n2.Eliminar comentario de un post\n 3.Gestionar mis seguidos\n 4.Eliminar Cuenta \n 5.Salir \n")
                        if opcion == 1:
                            usuario.editar_perfil(bd_usuarios)
                            cargar_usuarios(bd_usuarios)
                        elif opcion == 4:
                            opcion = input("¿Está seguro que desea eliminar su cuenta?\n1. Sí\n2. No\n")
                            usuario.eliminar_cuenta(bd_usuarios)
                            cargar_usuarios(bd_usuarios)
                            cargar_posts(feed) 
                            break 
                        elif opcion == 2:
                            indice = 1
                            for post in usuario.publicaciones:
                                if len(post.comentarios) != 0:
                                    post.mostrar_publicacion(indice)
                                    while True:
                                        opcion = input("¿Desea eliminar un comentario?\n1. Sí\n2. No\n")
                                        opcion = validar_opcion_numerica(opcion, 1, 2, "¿Desea eliminar un comentario?\n1. Sí\n2. No\n")
                                        if opcion == 1:
                                            comentario = input("Ingrese el indice del comentario que desea eliminar: ")
                                            comentario = validar_opcion_numerica(comentario, 1, len(post.comentarios), "Ingrese el indice del comentario que desea eliminar: ")
                                            post.comentarios.pop(comentario-1)
                                            print("Comentario eliminado exitosamente.")
                                            cargar_usuarios(bd_usuarios)
                                            cargar_posts(feed)
                                        elif opcion == 2:
                                            break
                        elif opcion == 3:
                            usuario.ver_amigos()
                            s = input("¿Desea dejar de seguir a alguien?\n1. Sí\n2. No\n")
                            s = validar_opcion_numerica(s, 1, 2, "¿Desea dejar de seguir a alguien?\n1. Sí\n2. No\n")
                            if s == 1:
                                user = input("Ingrese el usuario que desea dejar de seguir: ")
                                user = validar_usuario(user, "Ingrese el usuario que desea dejar de  seguir: ", bd_usuarios, "iniciar")                               
                                usuario.dejar_de_seguir(user)
                                cargar_usuarios(bd_usuarios)
                                
                            else:
                                break
                    elif opcion == 6:
                        break
            elif usuario != None and usuario.tipo_usuario == "admin":
                
                while True: #Menu de administradores:

                    print("\nBienvenido administrador, ¿Qué desea hacer?\n1. Moderar Posts\n2. Eliminar Usuario\n3. Informes de Publicaciones\n4. Informe de Interaccion\n 5. Informes de Moderacion\n 6. Cerrar sesión\n")
                    opcion = input("Ingrese una opción: ")
                    opcion = validar_opcion_numerica(opcion, 1, 6, "Bienvenido administrador, ¿Qué desea hacer?\n1. Moderar Posts\n2. Eliminar Usuario\n3. Informes de Publicaciones\n4. Informe de Interaccion\n 5. Informes de Moderacion\n 6. Cerrar sesión\n")
                    if opcion == 1:
                        salir = False
                        indice = 1
                        for post in feed:
                            if salir:
                                break
                            while True:
                                post.mostrar_publicacion(indice)                                
                                print("\n1. Eliminar Post\n2. Eliminar un Comentario\n3. Siguiente Post\n4. Salir\n")
                                opcion = input("Ingrese una opción: ")
                                opcion = validar_opcion_numerica(opcion, 1, 4, "1. Eliminar Post\n2. Eliminar un Comentario\n3. Siguiente Post\n4. Salir\n")
                                if opcion == 1:
                                    feed.remove(post)
                                    post.usuario.publicaciones.remove(post)
                                    post.usuario.infracciones += 1
                                    print("Post eliminado exitosamente.")
                                    cargar_usuarios(bd_usuarios)
                                    cargar_posts(feed)
                                    break
                                elif opcion == 2:
                                    if len(post.comentarios) > 0:
                                        comentario = input("Ingrese el indice del comentario que desea eliminar: ")
                                        comentario = validar_opcion_numerica(comentario, 1, len(post.comentarios), "Ingrese el indice del comentario que desea eliminar: ")
                                        post.comentarios[comentario-1].usuario.infracciones += 1
                                        post.comentarios.pop(comentario-1)
                                        print("Comentario eliminado exitosamente.")
                                        cargar_usuarios(bd_usuarios)
                                        cargar_posts(feed)
                                        
                                    else:
                                        print("Este post no tiene comentarios.")
                                elif opcion == 3:
                                    break
                                elif opcion == 4:
                                    salir = True
                                    break
                            indice += 1
                    elif opcion == 2:
                        for user in bd_usuarios:
                            if user.infracciones >= 3:
                                user.ver_perfil()
                                print(f"Cantidad de infracciones: {user.infracciones}\n")
                                while True:
                                    opcion = input("¿Desea eliminar este usuario?\n1. Sí\n2. No\n")
                                    opcion = validar_opcion_numerica(opcion, 1, 2, "¿Desea eliminar este usuario?\n1. Sí\n2. No\n")
                                    if opcion == 1:
                                        eliminados.append(user)
                                        bd_usuarios.remove(user)
                                        
                                        for x in feed:
                                            if x.usuario.usuario == user.usuario:
                                                feed.remove(x)
                                        for u in bd_usuarios:
                                            if user in u.amigos:
                                                u.amigos.remove(user)
                                                print("si lo elimina")
                                            for post in u.publicaciones:
                                                for like in post.likes:
                                                    if like.usuario.usuario == user.usuario:
                                                        post.likes.remove(like)
                                                for coment in post.comentarios:
                                                    if coment.usuario.usuario == user.usuario:
                                                        post.comentarios.remove(coment)
                                        print("Usuario eliminado exitosamente.")
                                        cargar_usuarios(bd_usuarios)
                                        cargar_posts(feed)
                                        break
                                    elif opcion == 2:
                                        break
                    
                    elif opcion == 3: #Menu de informe de publicaciones:
                        print("**** Informe de Publicaciones ****")
                        op = input("1. Usuarios con mayor cantidad de publicaciones\n2. Carreras con mayor cantidad de publicaciones\n")
                        op = validar_opcion_numerica(op, 1, 2, "1. Usuarios con mayor cantidad de publicaciones\n2. Carreras con mayor cantidad de publicaciones\n")
                        if op == 1:
                            usuarios = sorted(bd_usuarios, key=lambda usuario: len(usuario.publicaciones), reverse=True)
                            indice = 1
                            for usuario in usuarios:
                                print(f"{indice}.- Usuario: {usuario.usuario}\nCantidad de publicaciones: {len(usuario.publicaciones)}\n")
                                indice += 1
                                if indice == 6:
                                    break
                        elif op == 2:
                            carreras = {}
                            for usuario in bd_usuarios:
                                if usuario.area in carreras.keys():
                                    carreras[usuario.area] += len(usuario.publicaciones)
                                else:
                                    carreras[usuario.area] = len(usuario.publicaciones)
                            carreras = sorted(carreras.items(), key=lambda x: x[1], reverse=True)
                            limite = 0
                            for carrera in carreras:
                                print(f"Carrera: {carrera[0]}\nCantidad de publicaciones: {carrera[1]}\n")
                                limite += 1
                                if limite == 5:
                                    break
                    
                    elif opcion == 4: #Menu de informe de interaccion 
                        print("**** Informe de Interaccion ****")
                        op = input("1. Posts con mayor cantidad de interacciones\n2. Usuarios con mayor cantidad interacciones\n")
                        op = validar_opcion_numerica(op, 1, 2, "1. Usuarios con mayor cantidad de publicaciones\n2. Usuarios con mayor cantidad interacciones\n")
                        if op == 1:
                            posts = sorted(feed, key=lambda post: len(post.likes)+ len(post.comentarios), reverse=True)
                            indice = 1
                            for post in posts:
                                print(f"{indice}.- Usuario: {post.usuario.usuario}\nCantidad de interacciones: {len(post.likes)}\n")
                                indice += 1
                                if indice == 6:
                                    break
                        if op == 2:
                            usuarios = sorted(bd_usuarios, key=lambda usuario: buscar_interaccion(usuario, feed), reverse=True)
                            indice = 1
                            for usuario in usuarios:
                                print(f"{indice}.- Usuario: {usuario.usuario}\nCantidad de interacciones: {buscar_interaccion(usuario, feed)}\n")
                                indice += 1
                                if indice == 6:
                                    break
                    elif opcion == 5: #Mneu de informe de moderacion
                        print("**** Informe de Moderacion ****")
                        op = input("1. Usuarios con la mayor cantidad de post tumbados \n2. Carreras con mayor comentarios inadecuados. \n3. Usuarios eliminados por infracciones.")
                        op = validar_opcion_numerica(op, 1, 3, "1. Usuarios con la mayor cantidad de post tumbados \n2. Carreras con mayor comentarios inadecuados. \n3. Usuarios eliminados por infracciones.")
                        if op ==1:
                            usuarios = sorted(bd_usuarios, key=lambda usuario: usuario.infracciones, reverse=True)
                            indice = 1
                            for usuario in usuarios:
                                print(f"{indice}.- Usuario: {usuario.usuario}\nCantidad de infracciones: {usuario.infracciones}\n")
                                indice += 1
                                if indice == 6:
                                    break
                        elif op == 2:
                            carreras = {}
                            for usuario in bd_usuarios:
                                if usuario.area in carreras.keys():
                                    carreras[usuario.area] += usuario.infracciones
                                else:
                                    carreras[usuario.area] = usuario.infracciones
                            carreras = sorted(carreras.items(), key=lambda x: x[1], reverse=True)
                            indice = 1
                            for carrera in carreras:
                                print(f"{indice}.- Carrera: {carrera[0]}\nCantidad de infracciones: {carrera[1]}\n")
                                indice += 1
                                if indice == 6:
                                    break
                        elif op == 3:
                            for user in eliminados:
                                print(f"Usuario: {user.usuario}\n")
                    elif opcion == 6:
                        break
        elif principal == 2:
            usuario = crear_usuario(bd_usuarios)
            usuario.seguir_automaticamente(bd_usuarios)
            bd_usuarios.append(usuario)
            cargar_usuarios(bd_usuarios)
            
        elif principal == 3:
            break

