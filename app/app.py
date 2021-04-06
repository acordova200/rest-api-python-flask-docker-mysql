from flask import Flask
from database import db
from sqlalchemy_utils import create_database, database_exists
from routes.routes import blue_print
from flask_jwt_extended import JWTManager
import datetime
import os


app = Flask(__name__)

# Base de Datos
db_usuario = os.environ.get('DB_USUARIO')
db_clave = os.environ.get('DB_CLAVE')
db_host = os.environ.get('DB_HOST')
db_nombre = os.environ.get('DB_NOMBRE')

DB_URL = f'mysql+pymysql://{db_usuario}:{db_clave}@{db_host}/{db_nombre}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=12)

# JWT
jwt = JWTManager(app)

# inicializamos SQLAlchemy
db.init_app(app)


# instanciamos las rutas
app.register_blueprint(blue_print)

# Creamos la Base de Datos
with app.app_context():
    if not database_exists(DB_URL):
        create_database(DB_URL)
    db.create_all()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
