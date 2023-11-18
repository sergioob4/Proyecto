import datetime

class Comentario():
    def __init__(self, usuario, publicacion, comentario):
        self.id = id
        self.usuario = usuario
        self.publicacion = publicacion
        self.comentario = comentario
        self.fecha = datetime.datetime.now()

    def mostrar_comentario(self, indice):
        print(f"{indice}. {self.usuario.usuario}:  {self.comentario}\n{self.fecha}\n")