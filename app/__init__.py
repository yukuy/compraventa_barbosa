# app/__init__.py

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


db = SQLAlchemy()

# Inicializar la aplicación Flask
app = Flask(__name__)
app.config.from_object(config)



# Inicializar SQLAlche
db.init_app(app)

# Inicializa Flask-Mail
mail = Mail(app)

#configuracion de almacenamiento de cloudinary
config.init_cloudinary()
    
# Importar controladores y modelos
from app import controlMotos
from app import controlUser
from app import comentarios
from app import historial
from app import calificaciones
from app import creditos

# Crear la base de datos y las tablas al ejecutar la aplicación
with app.app_context():
    db.create_all()  # Esto creará las tablas si aún no existen
    
    from app import db  # Importa db desde tu aplicación


