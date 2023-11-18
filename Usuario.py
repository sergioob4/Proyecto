from Validaciones import *
from multimedia import Multimedia

# Clase usuario:

class Usuario:
    def __init__(self, nombre, apellido, correo, usuario, tipo_usuario, area):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.usuario = usuario
        self.area = area
        self.tipo_usuario = tipo_usuario
        self.publicaciones = []
        self.amigos = []
        self.infracciones = 0
    
# Metodo especial str   
    def __str__(self): #devuelve una cadena con los atributos
        return f"{self.nombre} {self.apellido} {self.correo} {self.usuario} {self.area}"

# Metodo de editar el perfil:
    def editar_perfil(self):
        while True: #Menu de editar perfil
            
            opcion = input("1. Editar nombre\n2. Editar apellido\n3. Editar correo\n4.Editar departamento/carrera\n5. Salir\nIngrese una opcion: ")
            
            opcion = validar_opcion_numerica(opcion, 1, 5, "1. Editar nombre\n2. Editar apellido\n3. Editar correo\n4. Editar departamento/carrera\n5. Salir\nIngrese una opcion: ")
            
            # Opcion de editar nombre:
            if opcion == 1:
                nombre = input("Ingrese su nuevo nombre: ")
                nombre = validar_string(nombre, "Ingrese su nuevo nombre: ")
                self.nombre = nombre
                print("Nombre editado exitosamente.")
            
            # Opcion de editar apellido:
            elif opcion == 2:
                apellido = input("Ingrese su nuevo apellido: ")
                apellido = validar_string(apellido, "Ingrese su nuevo apellido: ")
                self.apellido = apellido
                print("Apellido editado exitosamente.")
            
            # Opcion de editar correo
            elif opcion == 3:
                correo = input("Ingrese su nuevo correo: ")
                #correo = validar_correo(correo, "Ingrese su nuevo correo: ")
                self.correo = correo
                print("Correo editado exitosamente.")
            
            # Opcion de cambiar el area (departamento/carrera)
            elif opcion == 4:
                area = input("Ingrese su nuevo departamento/carrera: ")
                area = validar_string(area, "Ingrese su nuevo departamento/carrera: ")
                self.area = area
                print("Departamento/Carrera editado exitosamente.")
            
            # Salir del menu de editar usuarios:
            elif opcion == 5:
                
                break

# Metodo de ver perfil:
    def ver_perfil(self):
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCorreo: {self.correo}\nUsuario: {self.usuario}\nDepartamento/Carrera: {self.area}\n")
    
# Metodo de eleminar cuenta:
    def eliminar_cuenta(self, bd_usuarios):
        bd_usuarios.remove(self)
        print("Cuenta eliminada exitosamente.")    
    

# Metodo de elminar comentarios:
    def eliminar_comentarios(self, feed):
        visibles = []
        indice = 1
        for publicacion in feed:
            if publicacion.usuario.usuario == self.usuario:
                publicacion.mostrar_publicacion(indice)
                visibles.append(publicacion)
                indice +=1
        
        opcion = input("¿Desea ver los comentarios de alguna publicación?\n1. Sí\n2. No\n")
        if opcion == "1":
            while True:
                opcion = input("Ingrese el número de la publicación: ")
                opcion = validar_opcion_numerica(opcion, 1, len(visibles), "Ingrese el número de la publicación con la que desea interactuar: ")
                pub = visibles[opcion-1]
                indice = 1
                for comentario in pub.comentarios:
                    comentario.mostrar_comentario(indice)
                    indice += 1
                opcion = input("¿Desea eliminar algún comentario?\n1. Sí\n2. No\n")
                if opcion == "1":
                    opcion = input("Ingrese el número del comentario que desea eliminar: ")
                    opcion = validar_opcion_numerica(opcion, 1, len(pub.comentarios), "Ingrese el número del comentario que desea eliminar: ")
                    pub.comentarios.pop(opcion-1)
                    print("Comentario eliminado exitosamente.")
                opcion = input("¿Desea eliminar otro comentario?\n1. Sí\n2. No\n")
                if opcion == "2":
                    break
                


#  Metodo de ver publicaciones:  
    def ver_publicaciones(self, feed, usuario, bd_usuarios):
        visibles = []
        indice = 1
        for publicacion in feed:
            for amigo in self.amigos:
                if publicacion.usuario.usuario == amigo.usuario:
                    publicacion.mostrar_publicacion(indice)
                    visibles.append(publicacion)
                    indice +=1
                #  Interacciones con las publicaciones:  
        if len(visibles) != 0: 
            opcion = input("¿Desea interactuar con alguna publicación?\n1. Sí\n2. No\n")
            if opcion == "1":
                while True:
                    opcion = input("Ingrese el número de la publicación con la que desea interactuar: ")
                    opcion = validar_opcion_numerica(opcion, 1, len(visibles), "Ingrese el número de la publicación con la que desea interactuar: ")
                    interaccion = input("¿Qué desea hacer?\n1. Dar like\n2. Comentar\n3. Ver Likes\n4. Ver Comentarios\n5. Salir\n")
                    interaccion = validar_opcion_numerica(interaccion, 1,5, "¿Qué desea hacer?\n1. Dar like\n2. Comentar\n3. Ver Likes\n4. Ver Comentarios\n5. Salir\n")
                    if interaccion == 1:
                        visibles[opcion-1].dar_like(usuario)
                    elif interaccion == 2:
                        visibles[opcion-1].comentar(usuario)
                    elif interaccion == 3:
                        print(f"Likes: {len(visibles[opcion-1].likes)}")
                        for like in visibles[opcion-1].likes:
                            print(like.usuario.usuario)
                        if len(visibles[opcion-1].likes) != 0:
                            ver = input("¿Desea ver el perfil de alguno de los usuarios que dieron like?\n1. Sí\n2. No\n")
                            ver = validar_opcion_numerica(ver, 1, 2, "¿Desea ver el perfil de alguno de los usuarios que dieron like?\n1. Sí\n2. No\n")
                            if ver == 1:
                                u = input("Ingrese el usuario: ")
                                u = validar_usuario(u, "Ingrese el usuario: ", bd_usuarios, "iniciar")
                                if u != None:
                                    u.ver_perfil()
                                else:
                                    print("No existe ese usuario.") 
                        
                    elif interaccion == 4:
                        indice = 1
                        
                        for comentario in visibles[opcion-1].comentarios:
                            comentario.mostrar_comentario(indice)
                            indice += 1
                        if len(visibles[opcion-1].comentarios) != 0:
                            ver = input("¿Desea ver el perfil de alguno de los usuarios que comentaron?\n1. Sí\n2. No\n")
                            ver = validar_opcion_numerica(ver, 1, 2, "¿Desea ver el perfil de alguno de los usuarios que comentaron?\n1. Sí\n2. No\n")
                            if ver == 1:
                                u = input("Ingrese el usuario: ")
                                u = validar_usuario(u, "Ingrese el usuario: ", bd_usuarios, "iniciar")
                                if u != None:
                                    u.ver_perfil()
                                else:
                                    print("No existe ese usuario.")
                        
                    elif interaccion == 5:
                        break
                    opcion = input("¿Desea interactuar con otra publicación?\n1. Sí\n2. No\n")
                    if opcion == "2":
                        break
    
# Metodo de crear publicaciones:
    def crear_publicacion(self, feed):
        # Ingrese el tipo de publicaion (foto/video)
        tipo = input("Ingrese el tipo de publicación(foto/video): ") 
        
        # Validamos el str 
        tipo = validar_string(tipo, "Ingrese el tipo de publicación: ")
        
        # Ingrese la descripcion de la publicacion:
        descripcion = input("Ingrese la descripción de la publicación: ")
        
        # Validamos el str
        descripcion = validar_string(descripcion, "Ingrese la descripción de la publicación: ")
        
        # Ingrese el hashtag de la publicacion:
        hashtag = input("Ingrese el hashtag de la publicación: ")
        
        # validamos el str
        hashtag = validar_string(hashtag, "Ingrese el hashtag de la publicación: ")
        
        # Se crea la instancia de la clase multimedia:
        publicacion = Multimedia(self, tipo, descripcion, hashtag)
        feed.append(publicacion)
        self.publicaciones.append(publicacion)
        print("Publicación creada exitosamente.")
        

# Metodo para autoseguir:
    def seguir_automaticamente(self, usuarios):

        for usuario in usuarios:
            if usuario.area == self.area and usuario != self:
                self.amigos.append(usuario)


        
# Metodo para dejar de seguir:
    def dejar_de_seguir(self, user):
        if user != None:
            if user in self.amigos:
                self.amigos.remove(user)
                print(f"Ahora ya no sigues a {user.usuario}")
            else:
                print("No sigues a ese usuario.")
        else:
            print("No existe ese usuario.")

# Metodo para seguir:
    def seguir(self, user):
        if user != None:
            if user not in self.amigos:
                self.amigos.append(user)
                print(f"Ahora sigues a {user.usuario}")
            else:
                print("Ya sigues a ese usuario.")
        else:
            print("No existe ese usuario.")
    
# Metodo para ver amigos:
    def ver_amigos(self):
        for amigo in self.amigos:
            amigo.ver_perfil()