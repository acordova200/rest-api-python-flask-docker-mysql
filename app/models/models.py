from database import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(70), nullable=False, unique=True)
    clave = db.Column(db.String(100), nullable=False)

    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave


class Pelicula(db.Model):
    __tablename__ = 'peliculas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False, unique=True)
    estreno = db.Column(db.String(20))
    director = db.Column(db.String(100))
    reparto = db.Column(db.String(250))
    genero = db.Column(db.String(125))
    sinopsis = db.Column(db.String(250))

    def __init__(self, nombre, estreno, director, reparto, genero, sinopsis):
        self.nombre = nombre
        self.estreno = estreno
        self.director = director
        self.reparto = reparto
        self.genero = genero
        self.sinopsis = sinopsis
