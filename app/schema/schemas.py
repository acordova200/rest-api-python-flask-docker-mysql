from flask_marshmallow import Marshmallow

ma = Marshmallow()


# Esquema de Usuario
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usuario', 'clave')


# Esquema de Pelicula
class PeliculaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'estreno', 'director',
                  'reparto', 'genero', 'sinopsis')


pelicula_schema = PeliculaSchema()
peliculas_schema = PeliculaSchema(many=True)
