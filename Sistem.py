from Validaciones import *
from Usuario import Usuario
from multimedia import Multimedia 
from requests import request
import pickle #
import	os # 

# Esta funcion crea las instancia de la clase usuario o usuarios 
def crear_usuario(bd):
    nombre = input("Ingrese su nombre: ")
    nombre = validar_string(nombre, "Ingrese su nombre: ")
    
    apellido = input("Ingrese su apellido: ")
    apellido = validar_string(apellido, "Ingrese su apellido: ")
    
    correo = input("Ingrese su correo: ")
    
    
    usuario = input("Ingrese su usuario: ")
    usuario = validar_usuario(usuario, "Ingrese su usuario: " ,bd, "crear")
    
    tipo = input("Ingrese su tipo de usuario: ")
    tipo = validar_string(tipo, "Ingrese su tipo de usuario: ")
    
    area = input("Ingrese su departamento/carrera: ")
    area = validar_string(area, "Ingrese su departamento/carrera: ")
    
    return Usuario(nombre, apellido, correo, usuario,tipo, area)

# Cargar los datos de la api:
def insertar_api(usapi):
    bd_usuarios = []
    for usuario in usapi: #Con el for recorremos la api y creamos instancias
        if usuario["type"] == "professor":
            user = Usuario(usuario["firstName"], usuario["lastName"], usuario["email"], usuario["username"].lower(), usuario["type"], usuario["department"])
            user.id = usuario["id"]
            
            bd_usuarios.append(user)
        else:
            user = Usuario(usuario["firstName"], usuario["lastName"], usuario["email"], usuario["username"].lower(), usuario["type"], usuario["major"])
            user.id = usuario["id"]
            bd_usuarios.append(user)
    return bd_usuarios

# Aqui con los seguidos de los usarios:
def seguidos_api(bd_usuarios, api):
    for usuario in bd_usuarios:
        for usuario_api in api:
            if usuario.id == usuario_api["id"]:
                usuario.seguidos = usuario_api["following"]
                break
    
    for usuario in bd_usuarios:
        seguidos_final = []
        for seguido in usuario.seguidos:
            for usuario_bd in bd_usuarios:
                if seguido == usuario_bd.id:
                    seguidos_final.append(usuario_bd)
                    break
        usuario.seguidos = seguidos_final

# Cargamos las publicaciones de la api
def publicacion_api(bd_usuarios, api):
    feed = []
    for publicacion in api:
        for usuario in bd_usuarios:
            if publicacion["publisher"] == usuario.id:
                date = publicacion["date"]
                publicacion = Multimedia(usuario, publicacion["type"], publicacion["caption"], publicacion["tags"])
                publicacion.fecha = date
                feed.append(publicacion)
                usuario.publicaciones.append(publicacion)
                break
    return feed

# Iniciamos la api
def iniciar_api():
    request_users = request("GET", "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/08d4d2ce028692d71e9f8c32ea8c29ae24efe5b1/users.json")
    ausuarios = request_users.json()
    bd_usuarios = insertar_api(ausuarios)
    seguidos_api(bd_usuarios, ausuarios)
    for usuario in bd_usuarios:
        usuario.seguir_automaticamente(bd_usuarios)
    request_api = request("GET", "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/posts.json")
    apub = request_api.json()
    feed = publicacion_api(bd_usuarios, apub)
    return bd_usuarios, feed




# Pasar los usuarios al txt :
def cargar_usuarios(usuarios):
    escritura_binaria=open("C:/Users/Sergio/Desktop/Proyecto/usuarios.txt","wb")
    pickle.dump(usuarios,escritura_binaria)

    escritura_binaria.close()

def leer_usuarios(usuarios):

    leer_binario= open("C:/Users/Sergio/Desktop/Proyecto/usuarios.txt","rb")
    usuarios=pickle.load(leer_binario)
    leer_binario.close()
    return usuarios

# Pasar los posts al txt 
def cargar_posts(posts):
    escritura_binaria=open("C:/Users/Sergio/Desktop/Proyecto/posts.txt","wb")
    pickle.dump(posts,escritura_binaria)

    escritura_binaria.close()

# Leer los posts
def leer_posts(posts):

    leer_binario= open("C:/Users/Sergio/Desktop/Proyecto/posts.txt","rb")
    posts=pickle.load(leer_binario)
    leer_binario.close()
    return posts
