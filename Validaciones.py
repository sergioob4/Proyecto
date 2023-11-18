# Validaciones del sistema.

#  Validacion de las opciones numericas:
def validar_opcion_numerica(opcion, minimo, maximo, mensaje):
    while not opcion.isnumeric() or (int(opcion) < minimo or int(opcion) > maximo):
        print("Opción invalida. Por favor intente de nuevo.")
        opcion = input(mensaje)
    return int(opcion)


# Validacion de strings:
def validar_string(palabra, mensaje):
    aux = palabra.replace(" ", "")
    aux = aux.lower()
    aux = aux.replace("á", "a")
    aux = aux.replace("é", "e")
    aux = aux.replace("í", "i")
    aux = aux.replace("ó", "o")
    aux = aux.replace("ú", "u")
    aux = aux.replace("ñ", "n")
    
    if not aux.isalpha():
        print("Dato invalido. Intente de nuevo.")
        palabra = validar_string(palabra,mensaje)
    return palabra

def validar_strings(palabra, palabra2):
    palabra = palabra.replace(" ", "")
    palabra2 = palabra2.replace(" ", "")
    palabra = palabra.lower()
    palabra2 = palabra2.lower()
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")
    palabra = palabra.replace("ñ", "n")
    palabra2 = palabra2.replace("á", "a")
    palabra2 = palabra2.replace("é", "e")
    palabra2 = palabra2.replace("í", "i")
    palabra2 = palabra2.replace("ó", "o")
    palabra2 = palabra2.replace("ú", "u")
    palabra2 = palabra2.replace("ñ", "n")
    if palabra == palabra2:
        return True
    else:
        return False
    
# Validaciones de usuarios:  
def validar_usuario(usuario, mensaje, bd_usuarios, modo):
    usuario = usuario.replace(" ", "")
    while not usuario.isalnum():
        print("Usuario no válido. Intente nuevamente.")
        usuario = input(mensaje)
    
    ocupado = usuario_existe(usuario.lower(), bd_usuarios)
    if modo == "crear":
        if ocupado == None:
            return usuario.lower()
        else:
            print("El usuario ya Existe. Intente nuevamente.")
            usuario = input(mensaje)
            validar_usuario(usuario, mensaje, bd_usuarios, modo)
    elif modo == "iniciar":
        if ocupado != None:
            return ocupado
        else:
            print("Usuario no registrado. ")
            return None
    return usuario


def validar_hashtag(hashtag, mensaje):
    hashtag = hashtag.replace(" ", "")
    hashtag = hashtag.replace("#", "")
    
    while not hashtag.isalnum():
        print("Hashtag no válido. Intente nuevamente.")
        hashtag = input(mensaje)
    hashtag = "#" + hashtag
    
    return hashtag

def usuario_existe(usuario, bd_usuarios):
    for usuario_bd in bd_usuarios:
        if usuario_bd.usuario == usuario:
            return usuario_bd
    return None

def buscar_usuario(bd_usuarios):
    usuario = input("Ingrese el usuario: ")
    usuario = validar_usuario(usuario, "Ingrese el usuario: ", bd_usuarios, "iniciar")
    return usuario

def buscar_cardep(bd_usuarios):
    cardep = input("Ingrese el departamento/carrera: ")
    cardep = validar_string(cardep, "Ingrese el departamento/carrera: ")
    lista = []
    for usuario in bd_usuarios:
        if validar_strings(usuario.area, cardep):
            lista.append(usuario)
    return lista

def buscar_en_feed(id, feed):
    for publicacion in feed:
        if publicacion.referencia == id:
            return publicacion
    return None

def buscar_interaccion(user, feed):
    cantidad = 0
    for p in user.publicaciones:
        cantidad += len(p.likes)
        cantidad += len(p.comentarios)
    for publicacion in feed:
        for like in publicacion.likes:
            if like.usuario == user:
                cantidad += 1
                break
        for comentario in publicacion.comentarios:
            if comentario.usuario == user:
                cantidad += 1
    return cantidad


