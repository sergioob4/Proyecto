from Validaciones import *
from datetime import datetime #Lo usamos para colocar las fechas
from Comentario import Comentario
from Like import Like

class Multimedia():
    def __init__(self, usuario, tipo, descripcion, hashtag):
        self.usuario = usuario
        self.tipo = tipo
        self.descripcion = descripcion
        self.hashtag = hashtag
        self.fecha = datetime.now()
        self.comentarios = []
        self.likes = []
        
# Agregar likes a una publicacion:   
    def dar_like(self, usuario):
        encontrado = False
        for like in self.likes:
                if like.usuario == usuario:
                    self.likes.remove(like)
                    print("Le has quitado el like a la publicación.")
                    encontrado = True
                    break
            
        if not encontrado:
            like = Like(usuario, self)
            self.likes.append(like)
            print("Le has dado like a la publicación.")
    
# Comentar Publicaciones:
    def comentar(self, usuario):
        comentario = input("Ingrese su comentario : ")
        comentario = validar_string(comentario, "Ingrese su comentario : ")
        comentario = Comentario(usuario, self, comentario)
        self.comentarios.append(comentario)
        print("Comentario agregado exitosamente.")
    
# Mostrar Publicaciones:
    def mostrar_publicacion(self, indice):
        print(f"{indice}.- Usuario: {self.usuario.usuario}\nTipo: {self.tipo}\nDescripción: {self.descripcion}\nHashtag: {self.hashtag}\nFecha: {self.fecha}\nLikes: {len(self.likes)}\n")
        indice_C = 1
        for comentario in self.comentarios:
            print(f"{indice_C}- Usuario: {comentario.usuario.usuario}\nComentario: {comentario.comentario}\n")
            indice_C += 1